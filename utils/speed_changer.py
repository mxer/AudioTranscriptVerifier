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
wavdir = "J:\\new_corpus"
wavdirs_and_files = cp.wavdirs_and_files
wavdirs_and_files = [
						["\\train\\others\\3553\\male","3553_male.raw","3553_male.txt"],
						["\\train\\others\\3553\\female","3553_female.raw","3553_female.txt"],
						["\\train\\others\\3553\\pankaj","3553_pankaj.raw","3553_pankaj.txt"],
]		   

targets = {
					"s90" 	: "0.9",
					"s110"	: "1.1",
		  }
				
bindir = "j:\\asr\\bin"
convert_util = "sox.exe"
	
for entry in wavdirs_and_files:
	rawdir = wavdir + "\\" + entry[0] + "\\" + "train_audio"
	for tgt in targets:
		newrawdir = wavdir + "\\" + entry[0] + "\\" + tgt + "_train_audio"
		print(newrawdir)
		#delete the newrawdir if it already exists
		if os.path.isdir(newrawdir) == True:
			shutil.rmtree(newrawdir)
		os.makedirs(newrawdir)
		#start mixing noise files with the raw files in the train_audio file
		#and store them in newrawdir
		for dirpath, dirnames, filenames in os.walk(rawdir):
			for filename in [f for f in filenames if f.endswith(".raw")]:
				srcpar = "-r 16k -e signed -b 16 -c 1 -t raw"
				dstpar = "-r 16k -e signed -b 16 -c 1 -t raw"
				srcfile = rawdir + "\\" + filename
				dstfile = newrawdir + "\\" + filename
				src = srcpar + " " + srcfile
				dst = dstpar + " " + dstfile
				print(src)
				print(dst)
				callcmd = convert_util + " " + src + " " + dst + " " + "speed" + " " + targets[tgt]
				print(callcmd)
				call(callcmd,shell=True)