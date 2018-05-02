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

import corpus as cp
wavdir = "J:\\new_corpus"
wavdirs_and_files = cp.wavdirs_and_files

phmapfile = "J:\\asr\\utils\\phdict.org.txt"

rem_chars = [",","!","@","?",",","(",")",".","*",";",":"]		

#load the phone map
phnf = io.open(phmapfile,"r",encoding="utf-8")
phmap = dict()
for line in iter(phnf):
	entry = line.replace("\r","").replace("\n","").split()
	phone = entry[0]
	symbol = entry[1]
	phmap[phone] = symbol
	
for entry in wavdirs_and_files:
	filename = wavdir + "\\" + entry[0] + "\\" + entry[2]
	phfile = wavdir + "\\" + entry[0] + "\\" + entry[2].replace(".txt",".phscript.txt")
	dictfile = wavdir + "\\" + entry[0] + "\\" + entry[2].replace(".txt",".pdict.txt")
	f = io.open(filename,"r",encoding="utf-8")
	phf = io.open(phfile,"w",encoding="utf-8")
	df = io.open(dictfile,"r",encoding="utf-8")
	dct = dict()
	for line in df:
		word,pron = line.replace("\r","").replace("\n","").split("\t",1)
		word = word.replace("("," ").split()[0]
		if word not in dct:
			dct[word] = []
		dct[word].append(pron)
	df.close()	
	for line in iter(f):
		for ch in rem_chars:
			line = line.replace(ch,"")
		line = line.replace("-"," ")
		line = line.replace("/"," ")
		line = line.lower()
		words = line.split()
		phline = []
		for word in words:
			pron = dct[word][0].split()
			newpron = []
#			print(pron)
			for ph in pron:
				if ph not in phmap:
					print(word)
					print(ph)
					print(filename)
				newpron.append(phmap[ph])
			phline.append(''.join(newpron))
		newsent = ' '.join(phline)
		phf.write("%s\n"%(newsent))
	phf.close()
	f.close()
	