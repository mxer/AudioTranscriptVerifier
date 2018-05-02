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
						["\\train\\others\\hindi_kavita\\pp\\sannata","sannata_pp.raw","sannata_pp.txt"],
						["\\train\\others\\yunus_khan\\bade_bhai_saahab_a","bade_bhai_saahab_a.raw","bade_bhai_saahab_a.txt"],
						["\\train\\others\\yunus_khan\\bade_bhai_saahab_b","bade_bhai_saahab_b.raw","bade_bhai_saahab_b.txt"],
						["\\train\\others\\yunus_khan\\ekmk","ekmk.raw","ekmk.txt"],
						["\\train\\others\\yunus_khan\\gangreen","gangreen.raw","gangreen.txt"],
						["\\train\\others\\sharadjoshi\\railyatra","railyatra.raw","railyatra.txt"],
						["\\train\\others\\sharadjoshi\\railyatra","railyatra.raw","railyatra.txt"],
						["\\train\\others\\anurag_mishra\\andher","andher.raw","andher.txt"],
						["\\train\\others\\anurag_mishra\\gharjamai","gharjamai.raw","gharjamai.txt"],
						["\\train\\others\\anurag_mishra\\kheti","kheti.raw","kheti.txt"],
						["\\train\\others\\anurag_mishra\\ukhade_khambe","ukhade_khambe.raw","ukhade_khambe.txt"],
						["\\train\\reverie\\amit_dave\\set_a","amit_set_a.raw","amit_set_a.txt"],
						["\\train\\reverie\\amit_dave\\set_b","amit_set_b.raw","amit_set_b.txt"],
						["\\train\\reverie\\amit_dave\\set_c","amit_set_c.raw","amit_set_c.txt"],
						["\\train\\reverie\\amit_dave\\set_d","amit_set_d.raw","amit_set_d.txt"],
						["\\train\\reverie\\amit_dave\\set_e","amit_set_e.raw","amit_set_e.txt"],
						["\\train\\reverie\\amit_dave\\set_e","amit_set_e.raw","amit_set_e.txt"],
						["\\train\\reverie\\amit_dave\\set_f","amit_set_f.raw","amit_set_f.txt"],
					]		   

target_voices = [
					"angela",
#					"agnes","angela","celeste","donna","julie","lisa",
#					"mister","nerd","old","radio","teen","tough",
#					"albert","clarence","edith","jake","jane","sabrina"
				]	
				
morphed_dir = wavdir + "\\" + "train" + "\\" + "morphed"
 
if os.path.isdir(morphed_dir) == True:
	shutil.rmtree(morphed_dir)
if os.path.isdir(morphed_dir) == False:
	os.makedirs(morphed_dir)
   
convert_util = "sox.exe"
for tgt in target_voices:
	dirname = wavdir + "\\" + "morphed" + "\\" + tgt
	if os.path.isdir(morphed_dir + "\\" + tgt) == True:
		shutil.rmtree(morphed_dir + "\\" + tgt)
	if os.path.isdir(morphed_dir + "\\" + tgt) == False:
		os.makedirs(morphed_dir + "\\" + tgt)
	print(dirname)
	# Find the list of iles in the dirname
	for dirpath, dirnames, filenames in os.walk(dirname):
		for filename in [f for f in filenames if f.endswith(".wav")]:
			print(filename)
			basket_dir = filename.split(".",1)[0]
			basket_dir = basket_dir.split("@",1)[1].replace("@","\\")
			newdir = morphed_dir + "\\" + tgt + "\\" + basket_dir
			if os.path.isdir(newdir) == True:
				shutil.rmtree(newdir)
			if os.path.isdir(newdir) == False:
				os.makedirs(newdir)
			dst_par = "-r 16k -e signed -b 16 -c 1 -t raw"
			src = dirname + "\\" + filename
			dst = dst_par + " " + newdir + "\\" + filename.split(".",1)[1].replace(".wav",".raw")
			callcmd = convert_util + " " + src + " " + dst
			print(callcmd)
			call(callcmd,shell=True)
			origdir = wavdir + "\\" + "train" + "\\" + basket_dir
			callcmd = "copy" + " " + origdir + "\\*.txt" + " " + newdir
			call(callcmd,shell=True)