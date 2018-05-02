# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import sys
import os
import adcfg
import time
from lm import lmgen
from adutil import create_transcripts
from adutil import create_dictionary

wavdirs_and_files = adcfg.wavdirs_and_files
transfile = adcfg.transfile
super_prompts_file = adcfg.super_prompts_file
trfile = adcfg.trfile
wavdir = adcfg.wavdir 
seed_dict = adcfg.seed_dict
dictutil = adcfg.dictutil
phonefile = adcfg.phonefile
train_dict = adcfg.train_dict
org_model = adcfg.org_model
adapt_model = adcfg.adapt_model
train_fileid = adcfg.train_fileid
mfc_fileids_file = adcfg.mfc_fileids_file
metadata = adcfg.metadata
cepdir = adcfg.cepdir

language_model = adcfg.language_model
dictionary = seed_dict
hypfile = "result\\\\hindi_adapt.hyp.txt"

lmname = "train.lm"
infile = super_prompts_file 

lmgen(infile,lmname)
#callstr = ("..\\\\bin\\ngram-count" + " " + "-text" + " " + 
#			infile + " " + "-order 3" + " " + "-lm" + " " + 
#			lmname + " " + "-addsmooth 0.0001")
#print(callstr)
#call(callstr,shell=True)
language_model = lmname
dictionary = train_dict

print("calling pocketsphinx_batch")	
call(
		"J:\\asr\\bin\\pocketsphinx_batch" + \
		" -adcin yes" + \
		" -cepdir" + " " + cepdir + \
		" -cepext" + " " + ".raw" + \
		" -ctl" + " " + train_fileid + \
		" -lm" + " " + language_model + \
		" -dict" + " " + dictionary + \
		" -hmm" + " " + adapt_model + \
		" -hyp" + " " + hypfile
		#" -mllr" + " " + metadata + "\\mllr_matrix" 
    )

	
	
time.sleep(2)	
	
callcmd = "perl J:\\asr\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
print(callcmd)
cmdcall = callcmd + " > result\\\\res_adapt.txt"
print(cmdcall)
call(
		cmdcall, shell=True
    )
	
	
if adcfg.test_against_org_model == 1:	
	print("calling pocketsphinx_batch")	
	call(
		"J:\\asr\\bin\\pocketsphinx_batch" + \
		" -adcin yes" + \
		" -cepdir" + " " + cepdir + \
		" -cepext" + " " + ".raw" + \
		" -ctl" + " " + train_fileid + \
		" -lm" + " " + language_model + \
		" -dict" + " " + dictionary + \
		" -hmm" + " " + org_model + \
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
