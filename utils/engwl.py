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

wavdir = "J:\\\\New_Corpus"
bindir = "J:\\\\asr\\\\bin"

wavdir = "J:\\\\New_Corpus"
mfcdir = "J:\\\\New_Corpus"
metadata = "metadata"

rootdir = "J:\\\\asr"

wordfile = "J:\\asr\\wordlist.txt"

master_dictionary = "J:\\asr\\eng.dic"

wavdirs_and_files = cp.wavdirs_and_files
wavdirs_and_files=	[
						["\\train\\reverie\\pankaj\\cmu_ie_0","cmu_ie0.raw","cmu_ie0.txt"],
						["\\train\\reverie\\pankaj\\cmu_ie_1","cmu_ie1.raw","cmu_ie1.txt"],
						["\\train\\reverie\\pankaj\\eng0_0","pankaj_eng0_0.raw","pankaj_eng0_0.txt"],
						["\\train\\reverie\\pankaj\\eng0_1","pankaj_eng0_1.raw","pankaj_eng0_1.txt"],
						["\\train\\reverie\\pankaj\\eng0_2","pankaj_eng0_2.raw","pankaj_eng0_2.txt"],
						["\\train\\reverie\\pankaj\\eng0_3","pankaj_eng0_3.raw","pankaj_eng0_3.txt"],
						["\\train\\reverie\\pankaj\\eng0_4","pankaj_eng0_4.raw","pankaj_eng0_4.txt"],
						["\\train\\reverie\\pankaj\\eng1_0","pankaj_eng1_0.raw","pankaj_eng1_0.txt"],
						["\\train\\reverie\\pankaj\\eng1_1","pankaj_eng1_1.raw","pankaj_eng1_1.txt"],
						["\\train\\reverie\\pankaj\\eng1_2","pankaj_eng1_2.raw","pankaj_eng1_2.txt"],
						["\\train\\reverie\\pankaj\\eng1_3","pankaj_eng1_3.raw","pankaj_eng1_3.txt"],
						["\\train\\reverie\\pankaj\\eng1_4","pankaj_eng1_4.raw","pankaj_eng1_4.txt"],
						["\\train\\reverie\\pankaj\\eng2_0","pankaj_eng2_0.raw","pankaj_eng2_0.txt"],
						["\\train\\reverie\\pankaj\\eng2_1","pankaj_eng2_1.raw","pankaj_eng2_1.txt"],
						["\\train\\reverie\\pankaj\\eng2_2","pankaj_eng2_2.raw","pankaj_eng2_2.txt"],
						["\\train\\reverie\\pankaj\\eng2_3","pankaj_eng2_3.raw","pankaj_eng2_3.txt"],
						["\\train\\reverie\\pankaj\\eng2_4","pankaj_eng2_4.raw","pankaj_eng2_4.txt"],
						["\\train\\reverie\\pankaj\\eng3_0","pankaj_eng3_0.raw","pankaj_eng3_0.txt"],
						["\\train\\reverie\\pankaj\\eng3_1","pankaj_eng3_1.raw","pankaj_eng3_1.txt"],
						["\\train\\reverie\\pankaj\\eng3_2","pankaj_eng3_2.raw","pankaj_eng3_2.txt"],
						["\\train\\reverie\\pankaj\\eng3_3","pankaj_eng3_3.raw","pankaj_eng3_3.txt"],
						["\\train\\reverie\\pankaj\\eng3_4","pankaj_eng3_4.raw","pankaj_eng3_4.txt"],
					]
					
wordset = []					
for entry in wavdirs_and_files:
	fname = wavdir + "\\" + entry[0] + "\\" + entry[2]
	f = io.open(fname,"r",encoding="utf-8")
	for line in iter(f):
		line = line.replace("\r","").replace("\n","")
		wl = line.split()
		for w in wl:
			wordset.append(w.lower())
	f.close()

wordset = sorted(set(wordset))
	
ewf = io.open("engwordfile.txt","w",encoding = "utf-8")
for w in wordset:
	ewf.write(w + "\n")
ewf.close()