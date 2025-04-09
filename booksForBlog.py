#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
import shutil
import tempfile
import zipfile
from datetime import date


class Status:
    READ = 0
    READING = 1


def updateReadingPage(page, el):
    return re.sub(
        r"(?s)<reading-books>.*?</reading-books>",
        "<reading-books>\n" + str(el) + "\n</reading-books>",
        page,
        count=1,
        flags=re.MULTILINE,
    )


def updatePage(page, el):
    return re.sub(
        r"(?s)<books>.*?</books>",
        "<books>\n" + str(el) + "\n</books>",
        page,
        count=1,
        flags=re.MULTILINE,
    )


booksList = []
readingBooksList = []
latestBackupDirectory = max(
    [
        f.path
        for f in os.scandir("/home/amar/Downloads/")
        if f.is_file() and "Openreads-" in f.path
    ],
    key=os.path.getmtime,
)

# we create a temporary directory and unzip the books backup.
temp_dir = tempfile.TemporaryDirectory()
with zipfile.ZipFile(latestBackupDirectory, "r") as zip_ref:
    zip_ref.extractall(temp_dir.name)

for f in os.scandir(temp_dir.name):
    path = f.path
    # We copy the book images to be shown on the website
    if "jpg" in path:
        shutil.copy(path, "./static/images/books/")
    if "books.backup" in path:
        invalidJson = open(path, "r+")
        books = json.loads(f"[{invalidJson.read().replace('@@@@@', ',')}]")
        for book in books:
            # if the book is being read
            if book["status"] == Status.READING:
                readingBooksList += [
                    f"[![thumbnail of {book['title']}](images/books/{book['id']}.jpg)](https://isbnsearch.org/isbn/{book['isbn']})"
                ]

            # if the book is completed and its in the current year we append to the book list
            if book["status"] == Status.READ and str(date.today().year) in book["tags"]:
                booksList += [
                    f"[![thumbnail of {book['title']}](images/books/{book['id']}.jpg)](https://isbnsearch.org/isbn/{book['isbn']})"
                ]

booksWebPagePath = "./content/_index.md"

with open(booksWebPagePath, "r+") as page:
    newPage = updatePage(page.read(), "\n" + "\n".join(sorted(booksList)) + "\n")
    newPage += updateReadingPage(
        page.read(), "\n" + "\n".join(sorted(readingBooksList)) + "\n"
    )
    page.seek(0)
    page.write(newPage)
    page.truncate()

temp_dir.cleanup()
