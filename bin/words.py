# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:04:11 2012

Returns the most-common space-delimited words in a file.

@author: robert
"""
from collections import Counter
import re

def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str

def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str

def getwordbins(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

def main(filename, topwords):
    txt = openfile(filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        print key,value

main('speech.txt', 500)
