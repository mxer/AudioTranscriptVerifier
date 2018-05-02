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
					"agnes","angela","celeste","donna","julie","lisa",
					"mister","nerd","old","radio","teen","tough",
					"albert","clarence","edith","jake","jane","sabrina"
				]	
   

for tgt in target_voices:
	morphed_dir = wavdir + "\\" + "morphed" + "\\" + tgt
	if os.path.isdir(morphed_dir) == True:
		shutil.rmtree(morphed_dir)
	if os.path.isdir(morphed_dir) == False:
		os.makedirs(morphed_dir)
		

	
