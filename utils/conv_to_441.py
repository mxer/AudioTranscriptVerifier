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
						["\\train\\others\\indic_tts\\hindi\\female_mono","","hindi_female_mono.txt"],
					]		   
	
conv_util = "sox.exe"
				
for entry in wavdirs_and_files:
	src_dir = wavdir + entry[0] + "\\" + "wav"
	print(src_dir)
	tgt_dir = wavdir + "\\" + entry[0] + "\\" + "wav441"
	if os.path.isdir(tgt_dir):
		shutil.rmtree(tgt_dir)
	os.mkdir(tgt_dir)
	dst_par = "-r 44.1k -e signed -b 16 -c 1 -t wav"
	for root,dirs,files in os.walk(src_dir):
		for file in files:
			srcfile = root + "\\" + file
			dstfile = tgt_dir + "\\" + file
			src = srcfile
			dst = dst_par + " " + dstfile
			callcmd = conv_util + " " + src + " " + dst
			print(callcmd)
			call(callcmd,shell="True")
	