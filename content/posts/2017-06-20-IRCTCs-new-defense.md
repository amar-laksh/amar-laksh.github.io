---
title: Updating CAPTCHA for CAPCTHA's sake? OR How you get to automate the PNR website.
layout: post
date: '2017-06-17'
tags:
- CAPTCHA
- vulnerability analysis
- India
- PNR
---
<!-- more -->
![Old website](/images/old-pnr-status.png)

This was the good old Indian Railways website to track information about a railway ticket by using the *PNR number*. As we will see this was not the best website design so the staff decided to update the U.I. and more importantly the CAPTCHA method used on the webpage.


The update resulted in this:

![New website](/images/new-pnr-status.png)

Now you may ask what's the catch here?

Well let's see what happens when we enter a PNR in the textfield.

This happens:

![New captcha](/images/new-pnr-captcha.png)

The new CAPTCHA system might seem a bit more sophistcated than the simple one used earlier. It is. But...

> *Simplicity is the ultimate sophistication.*
-Leonardo Da Vinci

And sure it became apparent as I had the idea to try the previous solution in my earlier [blog post](https://amar-laksh.github.io/posts/captchas-on-ceo-sites/) to this one.

From the old blog post we know how to extract the digits. We just capture all the multiple digits that is possible in this CAPTCHA and then with a little python help

```python
import time
import pyautogui as do

def lvalue(image, directory):
    leftValue = {}
    for i in do.locateAllOnScreen(
                directory
                +str(image)+'.png'):
        leftValue.update([(i[0],image)])
    return leftValue


def getCaptcha(directory, images):
    captcha = {}
    for image in images:
        captcha.update(lvalue(image, directory))
        print captcha
    return ' '.join(
                map(
                    str
                    ,[captcha[key] for key in sorted(captcha)]
                    )
                )

time.sleep(2)
images = [0,1,2,3,4,5,6,7,8,9,10,11]

expr =  str(
            getCaptcha('./library/pnr/', images)
                .replace('10', '-')
                .replace('11', '+')
                .replace(' ', '')
        )

result = eval(expr)
print expr, ' = ',result
```


and here comes the demo:

![demo](/images/pnr-demo.gif)

and voila we have the right answer to the captcha question!

However, sadly as these weak captchas are on the rise I have decided to put up my code on [github](https://github.com/amar-laksh/capturerer) for others to add to the database.

Happy hacking!



