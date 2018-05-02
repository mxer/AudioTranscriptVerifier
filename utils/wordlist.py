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
#						["\\train\\others\\sandeep_maheshwari_a","sandeep_maheshwari_a.raw","sandeep_maheshwari_a.txt"],
#						["\\train\\others\\sandeep_maheshwari_b","sandeep_maheshwari_b.raw","sandeep_maheshwari_b.txt"],
#						["\\train\\others\\smriti","smriti.raw","smriti.txt"],
#						["\\train\\others\\vivek","vivek.raw","vivek.txt"],
#						["\\train\\others\\sharadjoshi\\railyatra","railyatra.raw","railyatra.txt"],
#						["\\train\\others\\arnab\\part_a","arnab_a.raw","arnab_a.txt"],
#						["\\train\\others\\arnab\\part_b","arnab_b.raw","arnab_b.txt"],
#						["\\train\\others\\cmu_indic_hi\\sxs","cmu_indic_hi_sxs.raw","cmu_indic_hi_sxs.txt"],
						["\\train\\others\\cmu_indic_hi\\axb","cmu_indic_hi_axb.raw","cmu_indic_hi_axb.txt"],
#						["\\train\\others\\rakhee\\snap","rakhee_snap.raw","rakhee_snap.txt"],
					]
		
# create local pronuncation dictionaries
#first upload master dictionary in memory
mdict = dict()

mdf = io.open(master_dictionary,"r",encoding="utf-8")

for line in iter(mdf):
	entry = line.replace("\r","").replace("\n","").split()
	word = entry[0].replace("(", " ").split()[0]
	pron = entry[1:]
	pron = ' '.join(pron)
	if word not in mdict:
		mdict[word] = []
		mdict[word].append(pron)
	else:
		if pron not in mdict[word]:
			mdict[word].append(pron)
			
mdf.close()
				
rem_chars = [",","!","@","?",",","(",")",".","*",";",":","\t",u"\u200d"]		
		
word_list = list()		
for entry in wavdirs_and_files:
	filename = wavdir + "\\" + entry[0] + "\\" + entry[2]
	print(filename)
	lwfile = wavdir + "\\" + entry[0] + "\\" + entry[2].replace(".txt","_wl.txt")
	print(lwfile)
	f = io.open(filename,"r",encoding="utf-8")
	lwf = io.open(lwfile,"w",encoding="utf-8")
	lwlist = list()
	for line in iter(f):
		for ch in rem_chars:
			line = line.strip(ch)
		line = line.lower()
		words = line.strip("\r").strip("\n").split()
		for word in words:
			lwlist.append(word)
		lwlist = sorted(set(lwlist))
	for word in lwlist:
		if word not in rem_chars:
			lwf.write(word + "\n")
			word_list.append(word)
	lwf.close()
	f.close()
	
word_list = sorted(set(word_list))

f = io.open(wordfile,"w",encoding="utf-8")

for word in word_list:
	f.write(word + "\n")

f.close()
firsttime = 0

#Now read all local word list.
#check its pronuniciation in the master dict
# if not found then if the word is in english then
# put the word in unk_list if the word is indian
# then generate the pronunication programatically
# and update the local dict as well as master d
for entry in wavdirs_and_files:
	filename = wavdir + "\\" + entry[0] + "\\" + entry[2].replace(".txt","_wl.txt")
	f = io.open(filename,"r",encoding="utf-8")
	dfname = wavdir + "\\" + entry[0] + "\\" + entry[2].replace(".txt",".pdict.txt")
	df = io.open(dfname,"w",encoding="utf-8")
	ldict = dict()
	unkwords = []
	linecounter = 0
	if f is None:
		print("%s IO Error : Aborting !!!!\n"%(filename))
	else:
		for line in iter(f):
			linecounter += 1
			word = line.strip()
			if uc.script(word[0]) == 'Devanagari':
				if (firsttime == 0):
					pron = pr.pronounce(word)
				firsttime = 0
#				print(word + "\t" + pron)
				if word not in ldict:
					ldict[word] = []
					ldict[word].append(pron)
				else:
					if pron not in ldict[word]:
						ldict[word].append(pron)
			else:
				if word in mdict:
					pron = mdict[word]
					if word not in ldict:
						ldict[word] = pron
					else:
						for pr in pron:
							if pr not in ldict[word]:
								ldict[word].append(pron)
				else:
					print("unknown word %s found at %d in file %s"%(word,linecounter,filename))
					unkwords.append(word)
			
	f.close()
	for key in sorted(ldict):
		i = 1
		for pron in ldict[key]:
			if i == 1:
				df.write("%s\t%s\n"%(key,pron))
			else:
				df.write("%s[%d]\t%s\n"%(key,i,pron))
			i += 1
	df.close()
	unfname = wavdir + "\\" + entry[0] + "\\" + entry[2].replace(".txt",".unk.txt")
	unflist = []
	if os.path.exists(unfname):
		os.remove(unfname)
	if len(unkwords) > 0:
		unf = io.open(unfname,"w",encoding="utf-8")
		for word in unkwords:
			unf.write(word + "\n")
		unf.close()
		unflist.append(unfname)
		
	if len(unflist) > 0:
		print("Unknown words found in following files:\n")
		for f in unflist:
			print(f)
	