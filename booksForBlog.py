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

booksPath = '../books/'
booksWebPagePath = './content/_index.md'

def updateBooks(page, table):
    updatedPage = re.sub(r'(?s)<books>.*?</books>', '<books>\n'+str(table)+'\n</books>', page, flags = re.MULTILINE)
    return updatedPage

def make_markdown_table(array):
    markdown = "\n"
    for el in array:
        markdown += str(el) + "\n"
    return markdown

def makeBookRow(content):
    row = "[![thumbnail of "+content["title"]+"]("+content["thumbnailAddress"]+")](" + content["googleBooksLink"] + ")"
    return row


books = list(next(walk(booksPath), (None, None, []))[2])
books.sort()
latestBook = books[len(books)-1]
print("Using " + latestBook + " to update book list")

bookContent = json.load(open(booksPath+latestBook, 'r+'))

del bookContent['backupMetadata']
del bookContent['records']


page = open(booksWebPagePath,'r')
oldPage = page.read()
#  headers = ["Title", "Authors", "My Rating", "Google Books Link"]
bookTableList = []
for content in bookContent["books"]:
    if(content["state"] == "READ"):
        bookTableList += [makeBookRow(content)]

bookTableList = sorted(bookTableList)
#  bookTableList = [headers] + bookTableList
bookTableMarkdown = make_markdown_table(bookTableList)
newPage = updateBooks(oldPage, bookTableMarkdown)
page.close()
open(booksWebPagePath, 'w').close()
open(booksWebPagePath, 'w').write(newPage)

