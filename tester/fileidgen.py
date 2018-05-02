# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
import os

audiodir = "J:\\\\New_Corpus"

dirlist = 	[
				  "test\\\\3553\\\\pankaj",
                  "test\\\\rakhee\\\\snap\\\\pure",
                  "test\\\\vivek",
			]
mfdirlist = [
				  "test\\\\3553\\\\pankaj\\\\test_mfc",
                 "test\\\\rakhee\\\\snap\\\\pure\\\\test_mfc",
                 "test\\\\vivek\\\\test_mfc",
			]

test_fileid = "etc\\\\hindi_model_adapt_test.fileids"
mfc_fileids_file = "etc\\\\hindi_model_adapt_mfc_test.fileids"

f = open(test_fileid,"w",encoding="utf-8")
mf = open(mfc_fileids_file,"w",encoding="utf-8")
filecounter = 0
global_counter = 0
for dir in dirlist:
	print(dir)
	filecounter = 0
	for root,dirs,files in os.walk(audiodir + "\\\\" + dir + "\\\\test_audio"):
		for file in files:
			if file.endswith('.raw'):
				print(file)
				f.write("%s\\\\%08d\n"%(dir + "\\\\test_audio",filecounter))
				mfdir = audiodir + "\\\\" + dir + "\\\\test_mfc"
				if not os.path.exists(mfdir):
					os.makedirs(mfdir)
				mf.write("%s\\\\%08d\n"%(audiodir+"\\"+dir + "\\\\test_mfc",filecounter))			
				filecounter += 1
				global_counter += 1

print("the number of raw files are : %d"%(global_counter))
				
f.close()
mf.close()		

