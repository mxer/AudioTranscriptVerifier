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
						["\\train\\reverie\\amit_dave\\set_f","amit_set_f.raw","amit_set_f.txt"],
					]		   
	
	
morph_wav_dir = wavdir + "\\" + "for_morphing"
conv_util = "sox.exe"
if os.path.isdir(morph_wav_dir) == True:
	shutil.rmtree(morph_wav_dir)
if os.path.isdir(morph_wav_dir) == False:
	os.makedirs(morph_wav_dir)
				
for entry in wavdirs_and_files:
	src_dir = wavdir + "\\" + entry[0]
	infile = src_dir + "\\" + entry[1]
	tgt_dir = morph_wav_dir
	outfile = tgt_dir + "\\" + '@'.join(entry[0].lstrip("\\").split("\\")) + "." + entry[1].replace(".raw",".wav")
	src_par = "-r 16k -e signed -b 16 -c 1 -t raw"
	dst_par = "-r 44.1k -e signed -b 16 -c 1"
	src = src_par + " " + infile
	dst = dst_par + " " + outfile
	callcmd = conv_util + " " + src + " " + dst
	print(callcmd)
	call(callcmd,shell="True")