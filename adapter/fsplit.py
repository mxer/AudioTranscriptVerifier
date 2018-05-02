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
from adutil import file_split
from adutil import create_fileids

wavdir = adcfg.wavdir
bindir = adcfg.bindir
wavdirs_and_files = adcfg.wavdirs_and_files
mfcdir = adcfg.mfcdir
org_model = adcfg.org_model
train_fileid = adcfg.train_fileid
mfc_fileids_file = adcfg.mfc_fileids_file
		   
# First split the raw audio files in audio segments		   
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
	
create_fileids(wavdir,dirlist,train_fileid,mfc_fileids_file)

call("J:\\asr\\bin\\sphinx_fe -argfile" + " " + org_model + "\\feat.params" + \
					 " -samprate 16000" + " -c" + " " + train_fileid + \
				 " -di" + " " + wavdir + \
				 " -do" + " " + mfcdir + \
				 " -ei raw -eo mfc -mswav no",shell=True
				 )

for di in dirlist:
	dirname = wavdir + "\\\\" + di
	print(dirname)
	srcdir = dirname + "\\\\train_audio"
	print(srcdir)
	dstdir = dirname + "\\\\train_mfc"
	callstr = "mkdir" + " " + dstdir
#	print(callstr)
	call(callstr,shell=True)
	callstr = "move" + " " + srcdir + "\\\\*.mfc" + " " + dstdir 
#	print(callstr)
	call(callstr,shell=True)

time.sleep(2)
