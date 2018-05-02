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
import shutil
import pronounce as pr
import unicodedata2 as uc

import corpus as cp
wavdir = "J://new_corpus"
wavdirs_and_files = cp.wavdirs_and_files
wavdirs_and_files = [
						["\\train\\others\\3553\\male","3553_male.raw","3553_male.txt"],
						["\\train\\others\\3553\\female","3553_female.raw","3553_female.txt"],
]		   

noise_sources = {
					"water" : "J:\\asr\\utils\\water.raw",
					"office": "J:\\asr\\utils\\office.raw",
				}
				
bindir = "j://asr//bin"
noisebin = "noiseadder.exe"
snrlvl = str(20)
	
for entry in wavdirs_and_files:
	rawdir = wavdir + "\\" + entry[0] + "\\" + "train_audio"
	for src in noise_sources:
		newrawdir = wavdir + "\\" + entry[0] + "\\" + src + "_train_audio"
		print(newrawdir)
		#delete the newrawdir if it already exists
		if os.path.isdir(newrawdir) == True:
			shutil.rmtree(newrawdir)
		os.makedirs(newrawdir)
		#start mixing noise files with the raw files in the train_audio file
		#and store them in newrawdir
		for dirpath, dirnames, filenames in os.walk(rawdir):
			for filename in [f for f in filenames if f.endswith(".raw")]:
				infile  = rawdir + "\\" + filename
				outfile = newrawdir + "\\" + filename
				nsfile = noise_sources[src]
				noiseaddarg = infile + " " + nsfile + " " + outfile + " " + snrlvl
				callcmd = bindir + "\\" + noisebin + " " + noiseaddarg
#				print(callcmd)
				call(callcmd,shell=True)