# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
import os

audiodir = "J:\\\\New_Corpus"

dirlist = 	[
				"train\\\\3553\\\\female",
#				"train\\\\3553\\\\male",
#				"train\\\\3553\\\\pankaj",
#				"train\\\\abhishek",
#				"train\\\\sandeep_maheshwari",
#				"train\\\\sandeep_maheshwari_b",
#                "train\\\\accomodation\\\\pankaj",
#                "train\\\\around_town\\\\pankaj",
#				"train\\\\conversations\\\\pankaj",
#				"train\\\\redbus\\\\pankaj",
#                "train\\\\rakhee\\\\snap\\\\pure",
#                "train\\\\smriti",
#                "train\\\\vivek",
#				"snapdeal\\\\pankaj",
#				"snapdeal_search\\\\Part0\\\\Pankaj",
#				"reinforce\\\\pankaj"
			]
mfdirlist = [
				"train\\\\3553\\\\female\\\\train_mfc",
#				"train\\\\3553\\\\male\\\\train_mfc",
#				"train\\\\3553\\\\pankaj\\\\train_mfc",
#				"train\\\\abhishek\\\\train_mfc",
#				"train\\\\sandeep_maheshwari\\\\train_mfc",
#				"train\\\\sandeep_maheshwari_b\\\\train_mfc",
#                "train\\\\accomodation\\\\pankaj\\\\train_mfc",
#                "train\\\\around_town\\\\pankaj\\\\train_mfc",
#				"train\\\\conversations\\\\pankaj\\\\train_mfc",
#				"train\\\\redbus\\\\pankaj\\\\train_mfc",
#                "train\\\\rakhee\\\\snap\\\\pure\\\\train_mfc",
#                "train\\\\smriti\\\\train_mfc",
#                "train\\\\vivek\\\\train_mfc",
#				"snapdeal\\\\pankaj\\\\train_mfc",
#				"snapdeal_search\\\\Part0\\\\Pankaj\\\\train_mfc",
#				"reinforce\\\\pankaj\\\\train_mfc"
			]

train_fileid = "etc\\\\hindi_model_adapt.fileids"
mfc_fileids_file = "etc\\\\hindi_model_adapt_mfc.fileids"

f = open(train_fileid,"w",encoding="utf-8")
mf = open(mfc_fileids_file,"w",encoding="utf-8")
filecounter = 0
global_counter = 0
for dir in dirlist:
	print(dir)
	filecounter = 0
	for root,dirs,files in os.walk(audiodir + "\\\\" + dir + "\\\\train_audio"):
		for file in files:
			if file.endswith('.raw'):
				print(file)
				f.write("%s\\\\%08d\n"%(dir + "\\\\train_audio",filecounter))
				mfdir = audiodir + "\\\\" + dir + "\\\\train_mfc"
				if not os.path.exists(mfdir):
					os.makedirs(mfdir)
				mf.write("%s\\\\%08d\n"%(audiodir+"\\"+dir + "\\\\train_mfc",filecounter))			
				filecounter += 1
				global_counter += 1

print("the number of raw files are : %d"%(global_counter))
				
f.close()
mf.close()		

