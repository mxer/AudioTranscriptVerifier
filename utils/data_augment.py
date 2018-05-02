# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 02:14:48 2016

@author: pankaj
"""

from subprocess import call
import sys
import os
import codecs
import time
import io
import re
import shutil
import pronounce as pr
import unicodedata2 as uc
import glob
from random import randint

import corpus as cp

noiseadder = "J:\\asr\\bin\\noiseadder.exe"

wavdir = "J:\\new_corpus"
wavdirs_and_files = cp.wavdirs_and_files
wavdirs_and_files = [
						["\\train\\augmented\\hindi\\male_mono","","hindi_male_mono.txt"],
					]		   

speed_changes = {"s90":"0.9","s110":"1.1"}
noise_effects = [
				"J:\\New_Corpus\\sound_effects\\757.wav",
				"J:\\New_Corpus\\sound_effects\\car.wav",				
				"J:\\New_Corpus\\sound_effects\\cargo_train.wav",
				"J:\\New_Corpus\\sound_effects\\hairdrier.wav",
				"J:\\New_Corpus\\sound_effects\\restaurant.wav",
				"J:\\New_Corpus\\sound_effects\\street.wav",
				"J:\\New_Corpus\\sound_effects\\shopping_mall.wav",
				
			   ]

no_of_noise_effects = len(noise_effects)-1			  
			   
for entry in wavdirs_and_files:
	src_dir = wavdir + entry[0] + "\\" + "train_audio"
	os.chdir(src_dir)

	for spd in speed_changes:
		dst_dir = wavdir + entry[0] + "_" + spd + "\\" + "train_audio"
		print(dst_dir)
		if os.path.isdir(dst_dir):
			shutil.rmtree(dst_dir)
		os.mkdir(dst_dir)
		s = speed_changes[spd]
		srcscript = wavdir + entry[0] + "\\" + entry[2]
		dstscript = wavdir + entry[0] + "_" + spd + "\\" + entry[2]
		print(srcscript)
		print(dstscript)
		shutil.copyfile(srcscript,dstscript)
		for file in glob.glob("*.raw"):
			srcfile = src_dir + "\\" + file
			dstfile = dst_dir + "\\" + file 
			callcmd = "sox -r 16k -b 16 -c 1 -e signed -t raw %s %s speed %s"%(srcfile,dstfile,s)
			print(callcmd)
			call(callcmd,shell=True)

	dst_dir = wavdir + entry[0] + "_" + "noise"
	print(dst_dir)
	if os.path.isdir(dst_dir):
		shutil.rmtree(dst_dir)
	os.mkdir(dst_dir)
	dst_dir = wavdir + entry[0] + "_" + "noise" + "\\" + "train_audio"
	os.mkdir(dst_dir)
	srcscript = wavdir + entry[0] + "\\" + entry[2]
	dstscript = wavdir + entry[0] + "_" + "noise" + "\\" + entry[2]
	print(srcscript)
	print(dstscript)
	shutil.copyfile(srcscript,dstscript)

	for file in glob.glob("*.raw"):
		effectno = randint(0,no_of_noise_effects)
#		print(effectno)
		noisefile = noise_effects[effectno]
#		callcmd = "sox -t wav %s -r 16k -b 16 -c 1 -t raw %s"%(noisefile,noisefile.replace(".wav",".raw"))
#		call(callcmd,shell=True)
		srcfile = src_dir + "\\" + file
		dstfile = dst_dir + "\\" + file 
		callcmd = noiseadder + " " + "%s %s %s %s"%(srcfile,noisefile.replace(".wav",".raw"),dstfile,str(17))
		print(callcmd)
		call(callcmd,shell=True)
	
				
		
			
	