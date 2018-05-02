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
mfc_fileids_file = adcfg.mfc_fileids_file
metadata = adcfg.metadata

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
create_dictionary(seed_dict,super_prompts_file,dictutil,phonefile,train_dict)

call("J:\\asr\\bin\\pocketsphinx_mdef_convert" + " -text" + " " + org_model + "\\mdef" + " " + org_model + "\\mdef.txt",shell=True)

time.sleep(2)

print("calling bw")
call(
		"J:\\asr\\bin\\bw" + " " + "-hmmdir" + " " + org_model + \
					" -moddeffn" + " " + org_model + "\\mdef.txt" + \
					" -ts2cbfn .ptm. -feat 1s_c_d_dd -svspec 0-12/13-25/26-38" + \
					" -cmn current -agc none -dictfn" + " " + train_dict + \
					" -ctlfn" + " " + mfc_fileids_file + \
					" -lsnfn" + " " + transfile + \
					" -accumdir" + " " + metadata
    )
time.sleep(2)
print("calling mmlr_solve")
call(
		"J:\\asr\\bin\\mllr_solve" + " " + "-meanfn" + " " + org_model + "\\means" + \
								  " -varfn" + " "  + org_model + "\\variances" + \
								  " -outmllrfn" + " " + metadata + "\\mllr_matrix" + \
								  " -accumdir" + " " + metadata,shell=True
    )	

time.sleep(2)

print("copying models")
callstr = "md" + " " + adapt_model
print(callstr)
call(callstr,shell=True)
call("copy J:\\asr\\models\\en-us\\*.* J:\\asr\\models\\en-us-adapt",shell=True)

time.sleep(2)
print("calling map_adapt")
call(
		"J:\\asr\\bin\\map_adapt" + " " + "-moddeffn" + " " + org_model + "\\mdef.txt" + \
						       " -ts2cbfn .ptm. " + \
							   " -meanfn" + " " + org_model + "\\means"  + \
							   " -varfn" + " " + org_model + "\\variances" + \
							   " -mixwfn" + " " + org_model + "\\mixture_weights" + \
							   " -tmatfn" + " " + org_model + "\\transition_matrices" + \
							   " -accumdir" + " " + metadata + \
							   " -mapmeanfn" + " " + adapt_model + "\\means" + \
							   " -mapvarfn" + " " + adapt_model + "\\variances" + \
							   " -mapmixwfn" + " " + adapt_model + "\\mixture_weights" + \
							   " -maptmatfn" + " " + adapt_model + "\\transition_matrices"
    )
	
time.sleep(2)
print("calling sendump")

call(
		"J:\\asr\\bin\\mk_s2sendump" + " " + "-pocketsphinx yes" + \
						            " -moddeffn" + " " + adapt_model + "\\mdef.txt" + \
									" -mixwfn" + " " + adapt_model + "\\mixture_weights" + \
									" -sendumpfn" + " " + adapt_model + "\\sendump" 
    )

time.sleep(2)	
