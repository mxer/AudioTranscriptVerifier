# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
import time
from subprocess import call

dirlist = 	[
				"test\\\\3553\\\\pankaj",
#				"test\\\\sandeep_maheshwari",
#                "uncurated\\\\snapdeal_most_likely",
                  "test\\\\rakhee\\\\snap\\\\\pure",
                  "test\\\\vivek",
#				"test\\\\3553\\\\male",
#				"accomodation\\\\pankaj",
#				"around_town\\\\pankaj",
#				"conversations\\\\pankaj",
#				"redbus\\\\pankaj",
#				"snapdeal\\\\pankaj",
#				"snapdeal_search\\\\Part0\\\\Pankaj",
#				"reinforce\\\\pankaj"
			]


transfile = "etc\\hindi_model_test.transcription"
trfile = "etc\\test.transcription"
test_fileid = "etc\\\\hindi_model_adapt_test.fileids"
mfc_fileids_file = "etc\\\\hindi_model_adapt_mfc_test.fileids"
wavdir = "J:\\\\New_Corpus"
mfcdir = "J:\\\\New_Corpus"
metadata = "metadata"

rootdir = "J:\\\\asr"

org_model = rootdir + "\\\\" + "models\\\\en-us"
adapt_model = rootdir + "\\\\" + "models\\\\en-us-adapt"

test_dict = "etc\\hindi_model_test.dic"
language_model = "etc\\\\hindi_model_test.lm"
dictionary = "etc\\hindi_model_test.dic"	
hypfile = "result\\\\hindi_adapt_test.hyp.txt"
cepdir = "J:\\\\New_Corpus"

from subprocess import call


print("calling pocketsphinx_batch")	
call(
		"J:\\asr\\bin\\pocketsphinx_batch" + \
		" -adcin yes" + \
		" -cepdir" + " " + cepdir + \
		" -cepext" + " " + ".raw" + \
		" -ctl" + " " + test_fileid + \
		" -lm" + " " + language_model + \
		" -dict" + " " + dictionary + \
		" -hmm" + " " + adapt_model + \
		" -hyp" + " " + hypfile
		#" -mllr" + " " + metadata + "\\mllr_matrix" 
    )

	
	
time.sleep(2)	
	
callcmd = "perl J:\\asr\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
print(callcmd)
cmdcall = callcmd + " > result\\\\res.txt"
print(cmdcall)
call(
		cmdcall, shell=True
    )
