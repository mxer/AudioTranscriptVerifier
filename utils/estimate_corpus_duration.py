# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import sys
import os
import corpus as cp
import shutil

wavdir = "J:\\New_Corpus"
bindir = "J:\\asr\\bin"

wavdirs_and_files = cp.wavdirs_and_files
wavdirs_and_files = [
						["\\train\\reverie\\pankaj\\story0_0","taali.raw","taali.txt"],
						["\\train\\reverie\\pankaj\\story1_0","story1_0.raw","story1_0.txt"],
						["\\train\\reverie\\pankaj\\story2_0","amatya_ki_kahani.raw","amatya_ki_kahani.txt"],
						["\\train\\reverie\\pankaj\\story3_0","story3_0.raw","story3_0.txt"],
						["\\train\\reverie\\pankaj\\story4_0","story4_0.raw","story4_0.txt"],
						["\\train\\reverie\\pankaj\\story5_0","story5_0.raw","story5_0.txt"],
						["\\train\\reverie\\pankaj\\story6_0","story6_0.raw","story6_0.txt"],
						["\\train\\reverie\\pankaj\\story7_0","story7_0.raw","story7_0.txt"],
						["\\train\\others\\pankaj\\hindi_agri_00","pankaj_hindi_agri_00.raw","pankaj_hindi_agri_00.txt"],
						["\\train\\others\\pankaj\\hindi_agri_01","pankaj_hindi_agri_01.raw","pankaj_hindi_agri_01.txt"],
						["\\train\\others\\pankaj\\hindi_agri_02","pankaj_hindi_agri_02.raw","pankaj_hindi_agri_02.txt"],
						["\\train\\others\\pankaj\\hindi_agri_03","pankaj_hindi_agri_03.raw","pankaj_hindi_agri_03.txt"],
						["\\train\\others\\pankaj\\hindi_agri_04","pankaj_hindi_agri_04.raw","pankaj_hindi_agri_04.txt"],
						["\\train\\others\\pankaj\\lokokti001","pankaj_lokokti_001.raw","pankaj_lokokti_001.txt"],
]		

tsize = 0   
for entry in wavdirs_and_files:
	rawdir = wavdir + "\\" + entry[0] + "\\" + "train_audio"
	#count the number of files in train_audio

	for dirpath, dirnames, filenames in os.walk(rawdir):
		for filename in [f for f in filenames if f.endswith(".raw")]:
			fname = rawdir + "\\" + filename
			fsize = os.path.getsize(fname)
			tsize += fsize
			
corpus_duration = round(((tsize/32000)/60),2)
print("Corpus_duration is %s mins"%(str(corpus_duration)))
		
