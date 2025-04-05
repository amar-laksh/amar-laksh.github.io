#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : booksForBlogs.py
# Author            : Amar Lakshya <amar.lakshya@protonmail.com>
# Date              : 17.10.2021
# Last Modified Date: 17.10.2021
# Last Modified By  : Amar Lakshya <amar.lakshya@protonmail.com>
import json
import os
import re
import shutil
from datetime import date


def updatePage(page, el):
    return re.sub(
        r"(?s)<books>.*?</books>",
        "<books>\n" + str(el) + "\n</books>",
        page,
        count=1,
        flags=re.MULTILINE,
    )


booksList = []
latestBackupDirectory = max(
    [
        f.path
        for f in os.scandir("/home/amar/Downloads/")
        if f.is_dir() and "Openreads-" in f.path
    ],
    key=os.path.getmtime,
)
for f in os.scandir(latestBackupDirectory):
    path = f.path
    # We copy the book images to be shown on the website
    if "jpg" in path:
        shutil.copy(path, "./static/images/books/")
    if "books.backup" in path:
        invalidJson = open(path, "r+")
        books = json.loads(f"[{invalidJson.read().replace('@@@@@', ',')}]")
        for book in books:
            # if the book is completed and its in the current year we append to the book list
            if book["status"] == 0 and str(date.today().year) in book["tags"]:
                booksList += [
                    f"[![thumbnail of {book['title']}](images/books/{book['id']}.jpg)](https://isbnsearch.org/isbn/{book['isbn']})"
                ]

booksWebPagePath = "./content/_index.md"
booksListWithNewLines = "\n" + "\n".join(sorted(booksList)) + "\n"

with open(booksWebPagePath, "r+") as page:
    newPage = updatePage(page.read(), booksListWithNewLines)
    page.seek(0)
    page.write(newPage)
    page.truncate()
