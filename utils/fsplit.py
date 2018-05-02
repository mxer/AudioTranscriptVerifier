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
#						["\\train\\reverie\\pankaj\\dhuan","dhuan.raw","dhuan.txt"],
#						["\\train\\reverie\\pankaj\\story2_0","amatya_ki_kahani.raw","amatya_ki_kahani.txt"],
#						["\\train\\reverie\\pankaj\\story3_0","story3_0.raw","story3_0.txt"],
#						["\\train\\reverie\\pankaj\\story4_0","story4_0.raw","story4_0.txt"],
#						["\\train\\reverie\\pankaj\\story5_0","story5_0.raw","story5_0.txt"],
#						["\\train\\others\\pankaj\\hindi_agri_00","pankaj_hindi_agri_00.raw","pankaj_hindi_agri_00.txt"],
#						["\\train\\others\\pankaj\\hindi_agri_01","pankaj_hindi_agri_01.raw","pankaj_hindi_agri_01.txt"],
#						["\\train\\others\\pankaj\\hindi_agri_02","pankaj_hindi_agri_02.raw","pankaj_hindi_agri_02.txt"],
#						["\\train\\others\\pankaj\\hindi_agri_03","pankaj_hindi_agri_03.raw","pankaj_hindi_agri_03.txt"],
#						["\\train\\others\\hindi_kavita\\pp\\sannata","sannata_pp.raw","sannata_pp.txt"],
#						["\\train\\morphed\\sabrina\\others\\hindi_kavita\\pp\\sannata","sannata_pp.raw","sannata_pp.txt"],
#						["\\train\\others\\pankaj\\lokokti001","pankaj_lokokti_001.raw","pankaj_lokokti_001.txt"],
						["\\train\\others\\edu\\adyatan","adyatan.raw","adyatan.txt"],
]		   
for entry in wavdirs_and_files:
	rawfilename = wavdir + "\\" + entry[0] + "\\" + entry[1]
	rawdir = wavdir + "\\" + entry[0] + "\\" + "train_audio"
	if os.path.isdir(rawdir) == True:
		shutil.rmtree(rawdir)
	os.makedirs(rawdir)
	sys.stdout.flush()
	if os.path.isfile(rawfilename) == False:
		print("%s doesn't exists aborting"%(rawfilename))
		exit(1)
	#
	callcmd = bindir + "\\" + "filesplit.exe" + " " + "-i" + " " + rawfilename + " " + "-rawlogdir" + " "  + rawdir
	#print(callcmd)
	sys.stdout.flush()
	call(
			callcmd,shell=True
		)
	#count the number of files in train_audio
	fcounter = 0
	for dirpath, dirnames, filenames in os.walk(rawdir):
		for filename in [f for f in filenames if f.endswith(".raw")]:
			fcounter += 1
		
	scriptfile = wavdir + "\\" + entry[0] + "\\" + entry[2]
	if os.path.isfile(scriptfile) == False:
		print("%s doesn't exists aborting"%(scriptfile))
		exit(1)
	with open(scriptfile,encoding="utf-8") as f:
		for i, l in enumerate(f):
			pass
		if fcounter != i+1:
			print(fcounter)
			print(i+1)
			print("Aborting -- Count mismatch for %s"%(scriptfile))
			exit(1)
		

