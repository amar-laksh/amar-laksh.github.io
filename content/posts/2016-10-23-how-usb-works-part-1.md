---
sidebar_link: true
layout: post
title: How USB Works? (Part 1)
description: Hmmm.... Let's See.
tags:
  - usb
  - osdev
fullview: false
published: true
---
<!-- more -->
![The USB 2.0 Symbol](/images/usb20_symbol.jpg)

>The beloved Universal Serial Bus is a very complex yet an ingenious solution to an age-old problem: Connecting Devices!

To start with this apparently epic journey, let's ask ourselves an easy enough question?

HOW DO **DEVICE A** INTERACT WITH **DEVICE B**??

It sure looks trivial at first but let's just consider some of the issues involved:

* DEVICE A has a different hardware architecture than DEVICE B.
* DEVICE A needs to power itself while interacting with DEVICE B.
* DEVICE A is actually a hub & needs to power DEVICE C which wants to communicate with DEVICE B.


It seems  quite clear that these things can get out of hands *rather quickly*, although...

![Something Cool you can't see](/images/there_is_always_a_way.jpg)


So, by the end of this series I hope to answer at least the most common queries related to USB:

* Why does USB have to plugged in a specific way?
* A single USB port can support 127 devices, but How?
* How come USB HID Devices do not require multiple drivers?



## BUT FIRST, LET'S TALK HISTORY!

The USB Specification broadly came in three waves:

* USB 1.0
* USB 2.0
* USB 3.0

**The USB 1.x Era (1994-1998)**

This was the early 90s and people were used to:

* A PS/2 Port for their PS/2 Devices wiith the PS/2 Connectors.
* A Serial Port for their Serial Devices with the RS-232 Connectors.
* A Game Port for their Gaming Devices with the DA-15 Connectors.

Yes, There were many ports and even more connectors in a giant tangled mess in every cupboard
but people didn't complain much, they simply did not have any alternate. The fate of the PC world
was sealed into different pins numbers and sizes.

On 11th November 1994, however, a young Intel architect by the name of Ajay Bhatt, along with the
contributions from the USB-IF (USB Implementers Forum) published a specification for the USB 0.7.


![Low Speed USB Type-A Close-Up Shot](/images/TYPE_A.jpg)

>With the USB specification, the USB-IF had set out to pave the way for replacing an entire pile of different connectors with just one cable; the USB or more specifically the low-speed USB Type-A.


After an year of incremental development, the USB-IF presented the USB 1.0 specification in the November of '95
. This version had support for the pre-existing **low-speed** 1.5 Mbit/s which was ideal for low data
rate devices like Joysticks and finally for data rates upto 12Mbit/s which was called **full-speed**.
The 12Mbit/s rate was intended mainly for the use in disks drives.





**USB 2.x Era (2000-2008)**

By now, everyone had recognised the magic of the ubiqitous USB ports. In the April of 2000, the USB-IF came out with a still better version; The USB 2.0 which added the High Speed data rates of 480 Mbit/s.

