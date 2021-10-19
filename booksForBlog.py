#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : booksForBlogs.py
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 17.10.2021
# Last Modified Date: 17.10.2021
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>
from os import walk
import json
import re

def updatePage(page, el):
    return re.sub(r'(?s)<books>.*?</books>'
            , '<books>\n'+str(el)+'\n</books>'
            , page, flags = re.MULTILINE)

def makeBookRow(content):
    row ="[![thumbnail of "+content["title"]+"]"
    row += "("+content["thumbnailAddress"]+")]"
    row += "(" + content["googleBooksLink"] + ")"
    return row

def getLatestBookBackup(booksPath):
    books = sorted(list(next(walk(booksPath), (None, None, []))[2]))
    return books[len(books)-1]

booksPath = '../books/'
booksWebPagePath = './content/_index.md'
booksList = []
try:
    latestBook = getLatestBookBackup(booksPath)
    print("Using " + latestBook + " to update book list")
    bookContent = json.load(open(booksPath+latestBook, 'r+'))
    for content in bookContent["books"]:
        if(content["state"] == "READ"):
            booksList += [makeBookRow(content)]

except:
    print("Cant find the book with valid content!")
    exit(1)

del bookContent['backupMetadata']
del bookContent['records']
newLines = "\n"+ '\n'.join(sorted(booksList)) + "\n"

with open(booksWebPagePath,'r+') as page:
    oldPage = page.read()
    newPage = updatePage(oldPage, newLines)
    page.seek(0)
    page.write(newPage)
    page.truncate()
