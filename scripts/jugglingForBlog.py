#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import re
import urllib.request
from html.parser import HTMLParser


class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_p = []

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.in_p.append(tag)

    def handle_endtag(self, tag):
        if tag == "p":
            self.in_p.pop()

    def handle_data(self, data):
        if self.in_p:
            print("<p> data :", data)


def updatePage(page, el):
    return re.sub(
        r"(?s)<juggling>.*?</juggling>",
        "<juggling>\n" + str(el) + "\n</juggling>",
        page,
        count=1,
        flags=re.MULTILINE,
    )


indexPath = "./content/_index.md"

knownSiteSwapList = ["3", "40", "(2x,2x)*"]
siteswapListForPage = []


for knownSiteSwap in knownSiteSwapList:
    url = f"https://jugglinglab.org/anim?{knownSiteSwap}"
    jugglingFile = f"./static/images/juggling/{knownSiteSwap}.gif"

    if not os.path.exists(jugglingFile):
        contents = urllib.request.urlopen(url).read()
        match = "".join(re.findall(r'\ssrc="([^"]+)"', str(contents)))
        match = match.replace("&amp;", "&")
        print("image src:", match)
        urllib.request.urlretrieve(str(match), jugglingFile)
    siteswapListForPage += [
        f"[![thumbnail of siteswap pattern: {knownSiteSwap}](images/juggling/{knownSiteSwap}.gif)]({url})"
    ]


with open(indexPath, "r+") as page:
    newPage = updatePage(page.read(), "\n" + "\n".join(siteswapListForPage) + "\n")
    page.seek(0)
    page.write(newPage)
    page.truncate()
