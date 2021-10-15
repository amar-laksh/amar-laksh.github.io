---
title: How CAPTCHA is not important? but finding everyone is!
layout: post
date: '2017-03-16'
description: The Election commission thought CAPTCHA should be plain numbers
tags:
- vulnerability analysis
- Election
- India
- CAPTCHA
---

[The Election Commission Of India](/images/eci.png)

>The Elections in India are conducted by this gigantic body of personnels and machines co-ordinating together to form the Election Commission.

The [Wiki](https://en.wikipedia.org/wiki/Election_Commission_of_India) will tell you that this is an old autonomous body for administrating elections in India. However, The Eleciton Commission also deals with maintaining and providing a large number of data-points generated during the elections.


One such point for voters and *power users* is the Voter Infomation website which very usefuly provides the option to search for a voter's information.

<!-- more -->

Now in a normal case, when you might want to see your voter information, you can just simply fill the form and hit that sweet search button. But let's say you want to scan and maybe horde information about select individuals or groups meeting your specific requirements, what will you do then?

A possible solution could be going to the specific [CEO](https://en.wikipedia.org/wiki/Chief_Electoral_Officer) website and download the election pdf rolls and search through the poorly formatted and recorded files.

A better solution however, could be simply spamming the main [Electoral Search](http://electoralsearch.in/) website!

So let's see, this is the website with its quite simplistic CAPTCHA model:

![Electoral Website](/images/electoral_search.png)


All the supposedly secure CAPCTHAs generated on the site just consist of simple numbers ranging from 0 to 9. Now this problem can be easily solved by using AI right? Let's just spin out tensorflow and train ourselves a new model!

Not so fast buddy, as cool as that may be, we really wouldn't want to waste our time building an A.I. for such a "secure" CAPTCHA system, would we?

Instead I give you the ever-useful **pyautogui** with its ever-more useful functions:

![locateOneScreen](/images/locate_on_screen.png)

We'll just use the:
**locateOnScreen(image, grayscale=False)**
function for our menial job. This means that we can store all the possible values and store them as seperate images and use them to identify the numbers on the screen?! Yes and no. Finding numbers are easy but categorizing a whole CAPTCHA sequence in its right form is not.

For Example, the CAPTCHA might be: 1 4 4 6 2

Now you'd surely find 1,4,6 and 2 but what about the order and accounting for repeating digits? Answer? Just looking at the function we are using more closely!
```python
locateOnScreen(image, grayscale=False) #returns the coordinates of the image found!
```

Taking those coordinates and simply by arranging them left-to-right we get all the CAPTCHA sequences in order.

Here's the script:

```python
import pyautogui as do
def getLeftValue(image):
try:
leftValue = [do.locateOnScreen(
		'./CAPTCHA/voterinfo/'
		+str(image)+'.png')][0][0]
except:
leftValue = 0
return leftValue


def getCaptcha():
	images = [1,2,3,4,5,6,7,8,9]
	captcha = {}
	for image in images:
leftValue = getLeftValue(image)
if leftValue != 0:
l = [(leftValue, image)]
captcha.update(l)
return ''.join(map(str,[captcha[key] for key in sorted(captcha)]))

captcha = getCaptcha()
print "The CAPTCHA IS: ", captcha
```

And voila!

![CAPTCHA GIF](/images/captcha.gif)

Now you can rope in the benefits of programmatic spamming!

**NOTE:** To be serious this type of CAPTCHA systems should be removed and replaced as soon as possible by the authorities.

An example of how bad things are for the Commission is the following at the time of writing this post:

**No Searchable Facility**
1. Assam(nsvp.in)
2. Chandigarh(digitalindia.gov.in)
3. Meghalaya(nvsp.in)

**No Captcha**
1. Karnataka
2. Uttar Pradesh
3. Uttarakhand
4. Andra Pradesh
5. Arunachal Pradesh
6. Dadra and Nager Haveli
7. Goa
8. Haryana
9. Jharkhand
10. Kerla
11. Lakshadweep
12. Madhya Pradesh
13. Maharastra
14. Mizoram
15. Nagaland
16. Odisha
17. Rajasthan
18. Sikkim
19. Telangana
20. Tripura
21. West Bengal

**Plain Digit Captcha**
1. Himachal
2. Delhi

**Has Captcha (Can be broken)**
1. Bihar
2. J & K
3. Chattisgarh(only Hindi version is available)
4. Gujrat
5. Manipur(dotted foreground)



**Un-reachable**
1. Andaman & Nicobar Islands
2. Daman & Diu
3. Puducherry
4. Tamil Nadu

**The Entire Captcha is text itself**
1. Punjab (Way to go Punjab)



