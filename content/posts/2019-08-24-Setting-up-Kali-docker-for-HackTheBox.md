---
title: Setting up a Kali docker container for HackTheBox and other stuff.
layout: post
sidebar_link: true
tags:
- hackthebox
- htb
- kali
- kali linux
---

You wanna practice and that pesky virtual image is too hard/tiresome/pesky to setup and run on your machine?

Well, what about a Kali Linux docker container that you can use all your tools from and also run GUI apps if you're so inclined?!

## Step - 1: Download & Run the Kali Linux Docker image

Here's the official link and honestly it covers almost everything: [Kali Linux Docker](https://www.kali.org/news/official-kali-linux-docker-images/)


## Step -2: Setup your Kali with meta-packages
Another great official link: [Kali meta-packages](https://www.kali.org/news/kali-linux-metapackages/)

## Step -3: Allow VPN connections!
We all know how handy and important VPNs are.
So adding the following command when running your docker container allows connections to pass through(also allowing ipv6):
```
--cap-add=NET_ADMIN --device /dev/net/tun  --sysctl net.ipv6.conf.all.disable_ipv6=0
```

## Step -4: Allow GUI apps to access X server!
Install `xhost` package from your distribution package manager (mostly it's just named `xorg-xhost`)
and run the following command to allow remote hosts to connect to the X server before starting your docker container with:
```
xhost+
```

for the docker GUI X clients we need to add the following arguments to setup the X connection properly:
```
-e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix
```

Tip: Remember to deny remote hosts after closing your docker container! ( just run `xhost -` for it)

## Step -5: Profit!

Here's the complete command:

```
xhost + &&\ 
docker run -ti --cap-add=NET_ADMIN --device /dev/net/tun \
--sysctl net.ipv6.conf.all.disable_ipv6=0 \
-e DISPLAY=:0 -v /tmp/.X11-unix:/tmp/.X11-unix \
YOUR_DOCKER_IMAGE_NAME /bin/bash && xhost -
```

Here's a link for a nifty little script that packages everything (My docker image is named `kali_pt`): [https://github.com/amar-laksh/kali_pt/blob/master/kali.sh](https://github.com/amar-laksh/kali_pt/blob/master/kali.sh)