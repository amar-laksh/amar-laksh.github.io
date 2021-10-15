---
title: 'Writeups for Google CTF 2019: My first CTF (Kinda) - Part 2'
layout: post
sidebar_link: true
tags:
- CTF
- Google CTF 2019
- Security
- Security Challenges
---

## Work Computer - Sandbox

![work_computer.png](/images/ctf_images/google_2019/work_computer.png)

We connect to the given server on the given port and see what we are up against by using netcat (`nc readme.ctfcompetition.com 1337`):
```
> help
Alien's shell
Type program names and arguments, and hit enter.
The following are built in:
  cd
  help
  exit
Use the man command for information on other programs.
>
```

So clearly this is some kind of shell, let's try doing an ls:
```
ls -l
total 8
----------    1 1338     1338            33 Jul  4 12:07 ORME.flag
-r--------    1 1338     1338            28 Jul  4 12:07 README.flag
```

Now we can see that we can at least read `README.flag`, trying to do that we find:
```
> cat README.flag
error: No such file or directory
```
So we find we can't use `cat` or any other kind of usual command to output the flag. How do we know this? Let's try listing all the commands avaialabe in the `/usr/bin/`. We quickly find that there are no commands such as `cat`, `less` etc.

Okay so let's try enumerating all the interesting directories where we can find some obscure program to output our flag:
```
> ls -l /bin /sbin /usr/bin /usr/sbin                                         
/bin:
total 800
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 arch -> /bin/busybox
-rwxr-xr-x    1 65534    65534       796240 Jan 24 07:45 busybox
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 chgrp -> /bin/busybox
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 chown -> /bin/busybox
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 conspy -> /bin/busybox
..............
/sbin:
total 228
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 acpid -> /bin/busybox
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 adjtimex -> /bin/busybox
..............
/usr/bin:
total 1984
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 [ -> /bin/busybox
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 [[ -> /bin/busybox
..............
-rwxr-xr-x    1 65534    65534        25216 Mar 19 09:56 iconv
..............
-rwxr-xr-x    1 65534    65534        83744 Nov 15  2018 scanelf
..............
/usr/sbin:
total 16
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 addgroup -> /bin/busybox
lrwxrwxrwx    1 65534    65534           12 May  9 20:49 adduser -> /bin/busybox
..............
> 
```

Looking through the list I happen to come across two commands I have not seen or noticed before! The commands are: [shuf](https://linux.die.net/man/1/shuf) and [iconv](https://linux.die.net/man/1/iconv). We look up the man pages for them and find that both of them write file contents to stdout! Exactly what we want to do:
```
> shuf README.flag
CTF{4ll_D474_5h4ll_B3_Fr33}

> iconv /challenge/README.flag
CTF{4ll_D474_5h4ll_B3_Fr33}
```

Here's our flag!


## FriendSpaceBookPlusAllAccessRedPremium.com  - Reversing 

![friends.png](/images/ctf_images/google_2019/friends.png)
