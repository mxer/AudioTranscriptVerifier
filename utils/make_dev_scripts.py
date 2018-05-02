# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import sys
import os
import codecs
import time
import io
import re

import pronounce as pr
import unicodedata2 as uc
import phtochar

import corpus as cp
wavdir = "J:\\new_corpus"
wavdirs_and_files = cp.wavdirs_and_files

prdic = "J:\\asr\\eng.dic"

lcd = dict()

pf = io.open(prdic,"r",encoding="utf-8")
for line in iter(pf):
	word,pron = line.replace("\r","").replace("\n","").split("\t",1)
	lcd[word] = pron
pf.close()

wavdirs_and_files=	[
						["\\train\\agra\\avdheshkumar\\script_c1","avdheshkumar_c1.raw","avdheshkumar_c1.txt"],
					]
					
					
for entry in wavdirs_and_files:
	fname = wavdir + entry[0] + "\\" + entry[2]
	print(fname)
	rf = io.open(fname,"r",encoding="utf-8")
	dfname = wavdir + entry[0] + "\\" + entry[2].replace(".txt","_dev.txt")
	df = io.open(dfname,"w",encoding="utf-8")
	for line in rf:
		line = line.lower().rstrip(" ").replace("\r","").replace("\n","")
		wl = line.split(" ")
		newwl = []
		for w in wl:
			if uc.script(w[0]) == "Devanagari":
				newwl.append(w)
			else:
				print(w)
				newwl.append(phtochar.phone_to_word(lcd[w]))
		newsent = " ".join(newwl)
		df.write(newsent + "\n")
	df.close()