# -*- coding: utf-8 -*-
import glob
import os
import io
import pronounce as pr
import Constants as cs

# This script will prepare pronunciation files on the basis of a given phone file

# rootdir = "E:/STT_Apps/data"
rootdir = "E:/STT_Apps/data"
srcdata = [
                ["/train","/odia/odia_mono/odia_male_mono","","odia_male_mono.txt","male",cs.Kannada],
                
		  ]

def createDictionary(inputfile, outputfile, langCode):
	# for entry in srcdata:
	newline = u""
	wordlist = []
	sf = io.open(inputfile,"r",encoding="utf-8")
	for line in sf:
		wl = line.replace("\r", "").replace("\n", "").replace("/", " ").replace(":", u"").replace(u"॑", "").replace(u"|","").replace(u"।", "").replace(u"ʼ", "").replace(u"'", "").replace(u"-", " ").replace(u"…", "").replace(u"+", " ").replace(u'”', "").replace(u"ଵ", u"ୱ").replace("0", "").replace(u"\u200c", "").replace(u"\u200d", "")
		splitted = wl.split(" ")
		for s in splitted:
			wordlist.append(s)
	sf.close()
	pdf = io.open(outputfile,"w",encoding="utf-8")
	wordlist = sorted(set(wordlist))
	mapped = pr.Mappings()
	for word in wordlist:
		pdf.write(newline + word + "\t" + mapped.pronounce(word, langCode))
		newline = u"\n"

	pdf.close()

	print ("***** dictionary file created ********")




