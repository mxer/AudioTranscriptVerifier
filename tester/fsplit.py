# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import sys
import os

wavdir = "J:\\\\New_Corpus"
bindir = "J:\\\\asr\\\\bin"
wavdirs_and_files = [
#						["test\\\\3553\\\\pankaj","3553_pankaj.raw"],
#                        ["test\\\\rakhee\\\\snap\\\\pure","test_rakhee_snap_pure.raw"],
#                        ["test\\\\vivek","test_vivek.raw"],
						["\\train\\others\\edu\\adyatan","adyatan.raw","adyatan.txt"],
					]
		   
for rawfiles in wavdirs_and_files:
	dirname = rawfiles[0]
	inraw_file = wavdir + "\\\\" + dirname + "\\\\" + rawfiles[1]
	rawdir = wavdir + "\\\\" + dirname + "\\\\" + "test_audio"
	if not os.path.exists(rawdir):
		os.makedirs(rawdir)
	print(rawdir)
	sys.stdout.flush()
	callcmd = bindir + "\\\\" + "filesplit.exe" + " " + "-i" + " " + inraw_file + " " + "-rawlogdir" + " "  + rawdir
	#print(callcmd)
	sys.stdout.flush()
	call(
			callcmd,shell=True
		)
		

