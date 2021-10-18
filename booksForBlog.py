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
    markdown = "\n" + str("| ")
    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"
    markdown += '|'
    for _ in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"
    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"
    return markdown + "\n"

def makeBookRow(content):
    row = [content["title"], content["author"], str(content["rating"]) + "/5", "[![thumbnail of ]("+content["thumbnailAddress"]+")](" + content["googleBooksLink"] + ")"]
    return row


books = list(next(walk(booksPath), (None, None, []))[2])
books.sort()
latestBook = books[len(books)-1]

bookContent = json.load(open(booksPath+latestBook, 'r+'))

del bookContent['backupMetadata']
del bookContent['records']


page = open(booksWebPagePath,'r')
oldPage = page.read()
headers = ["Title", "Authors", "My Rating", "Google Books Link"]
bookTableList = []
for content in bookContent["books"]:
    if(content["state"] == "READ"):
        bookTableList += [makeBookRow(content)]

bookTableList = sorted(bookTableList)
bookTableList = [headers] + bookTableList
bookTableMarkdown = make_markdown_table(bookTableList)
newPage = updateBooks(oldPage, bookTableMarkdown)
page.close()
open(booksWebPagePath, 'w').close()
open(booksWebPagePath, 'w').write(newPage)

