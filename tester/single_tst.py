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
import tester.unicodedata2 as uc
from tester.lm import lmgen
from tester.adutil import file_split
from tester.adutil import create_fileids
from tester.adutil import create_transcripts
from tester.adutil import read_words
from tester.adutil import create_dictionary
import make_local_pdict as ml

wavdir = "E:\\\\New_Corpus"
bindir = "E:\\\\asr\\\\bin"
lmname = "E:\\\\asr\\\\tester\\\\etc\\\\test.lm"
transfile = "etc\\hindi_model_test.transcription"
trfile = "etc\\test.transcription"
super_prompts_file = "etc\\hindi_model_test_prompt.txt"
phonefile = "..\\\\bin\\\\phonemap.txt"
hindi_phone_file = "..\\\\bin\\\\hindiphone.txt"
infile = "etc\\\\hindi_model_test_prompt.txt"
lminfile = "etc\\\\lminput.txt"
vocabfile = "etc\\\\hindi_model_test_vocab.txt"
#outfile = "etc\\hindi_model_test_adaptation.dic"
outfile = "..\\\\test.dic"
dictutil = "E:\\\\asr\\\\bin\\\\progen.exe"

FILE_SPLIT = 1

test_fileid = "etc\\\\hindi_model_adapt_test.fileids"
mfc_fileids_file = "etc\\\\hindi_model_adapt_mfc.fileids"

wavdir = "E:\\\\New_Corpus"
mfcdir = "E:\\\\New_Corpus"
metadata = "metadata"

rootdir = "E:\\\\asr"

org_model = rootdir + "\\\\" + "models\\\\en-us"
adapt_model = rootdir + "\\\\" + "models\\\\en-us-adapt"

test_dict = rootdir + "\\\\revasr.dic"

language_model = "..\\reverie.lm"
dictionary = test_dict	
hypfile = "result\\\\hindi_adapt.hyp.txt"
cepdir = wavdir

discount = 0.3

wavdirs_and_files = [
		# ["\\train\\others\\accomodation\\Niyanta","bohni.raw","bohni.txt"],
		# ["\\train\\others\\accomodation\\Final\\anubhav", "anubhav.raw", "anubhav.txt"],
		# ["\\train\\others\\accomodation\\debasish","badegharkibeti.raw","badegharkibeti.txt"]
		# ["\\train\\others\\accomodation\\ToBeVerified\\part4", "part4.raw", "part4.txt"],
		["\\train\\others\\accomodation\\ToBeVerified\\Niyanta\\part12", "part12.raw", "part12.txt"],
					]
								
							
							
# First split the raw audio files in audio segments
if FILE_SPLIT == 1:		  
	for rawfiles in wavdirs_and_files:
		dirname = rawfiles[0]
		inraw_file = wavdir + "\\\\" + dirname + "\\\\" + rawfiles[1]
		rawdir = wavdir + "\\\\" + dirname + "\\\\" + "train_audio"
		file_split(bindir,inraw_file,rawdir)
	
# create train_audio and train_mfc directories
dirlist = []
#mfdirlist = []
for lst in wavdirs_and_files:
	print(lst[0])
	dirlist.append(lst[0])
	
#for lst in dirlist:
#	mfdirlist.append(lst + "\\\\train_mfc")

print(dirlist)

# create fileids

create_fileids(wavdir,dirlist,test_fileid,mfc_fileids_file)



audiodir = wavdir

transdir = wavdir
scriptlist = []

for lst in wavdirs_and_files:
	scriptlist.append(lst[0] + "\\\\" + lst[2])
	
print(scriptlist)

dirlist = []
for lst in wavdirs_and_files:
	dirlist.append(lst[0] + "\\\\train_audio")
	
print(dirlist)

create_transcripts(transfile,super_prompts_file,trfile,scriptlist,dirlist,wavdir)

ml.createDictionary(super_prompts_file, test_dict)

# create_dictionary("E:\\\\asr\\\\eng.dic",super_prompts_file,dictutil,phonefile,test_dict)

# create Language Model
#LM configuration
print("LM creation")
lmgen(infile,lmname)
#lmname = "E:\\New_Corpus\\language_model\\reverie.lm"
language_model = lmname

print("calling pocketsphinx_batch")	
call(
		"E:\\asr\\bin\\pocketsphinx_batch" + \
		" -adcin yes" + \
		" -cepdir" + " " + cepdir + \
		" -cepext" + " " + ".raw" + \
		" -ctl" + " " + test_fileid + \
		" -lm" + " " + language_model + \
		" -dict" + " " + dictionary + \
		" -hmm" + " " + adapt_model + \
		" -cmn" + " " + "current" + \
		" -hyp" + " " + hypfile
		#" -mllr" + " " + metadata + "\\mllr_matrix" 
  )

	
	
time.sleep(2)	
	
callcmd = "perl E:\\asr\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
print(callcmd)
cmdcall = callcmd + " > result\\\\test_adapt.txt"
print(cmdcall)
call(
		cmdcall, shell=True
  )

'''	
print("calling pocketsphinx_batch")	
call(
		"E:\\asr\\bin\\pocketsphinx_batch" + \
		" -adcin yes" + \
		" -cepdir" + " " + cepdir + \
		" -cepext" + " " + ".raw" + \
		" -ctl" + " " + test_fileid + \
		" -lm" + " " + language_model + \
		" -dict" + " " + dictionary + \
		" -hmm" + " " + org_model + \
		" -hyp" + " " + hypfile
		#" -mllr" + " " + metadata + "\\mllr_matrix" 
  )

	
	
time.sleep(2)	
	
callcmd = "perl E:\\asr\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
print(callcmd)
cmdcall = callcmd + " > result\\\\test.txt"
print(cmdcall)
call(
		cmdcall, shell=True
  )

'''  