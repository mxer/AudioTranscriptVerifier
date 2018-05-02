# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import os
import time
from adapter.adutil import file_split
from adapter.adutil import create_fileids
from adapter.adutil import create_transcripts
import make_local_pdict as ml
import Constants as cs
import io
from shutil import copyfile

bindir = "E:\\asr\\bin"
# lmname = "E:\\asr\\adapter\\etc\\adaptation.lm"
transfile = "etc\\hindi_model_train.transcription"
trfile = "etc\\train.transcription"
super_prompts_file = "etc\\hindi_model_train_prompt.txt"
# phonefile = "..\\bin\\phonemap.txt"
# hindi_phone_file = "..\\bin\\hindiphone.txt"
# infile = "etc\\hindi_model_train_prompt.txt"
# vocabfile = "etc\\hindi_model_train_vocab.txt"
# outfile = "etc\\hindi_model_train_adaptation.dic"
# dictutil = "E:\\asr\\bin\\progen.exe"

train_fileid = "etc\\hindi_model_adapt.fileids"
mfc_fileids_file = "etc\\hindi_model_adapt_mfc.fileids"

wavdir = "E:\\New_Corpus"
mfcdir = "E:\\New_Corpus"
metadata = "metadata"

rootdir = "E:\\asr"

org_model = rootdir + "\\" + "models\\en-us"
adapt_model = rootdir + "\\" + "models\\en-us-adapt"

train_dict = "..\\train.dic"
language_model = "..\\reverie.lm"
dictionary = train_dict	
hypfile = "result\\hindi_adapt.hyp.txt"
cepdir = wavdir

wavdirs_and_files = [
						["\\train\\others\\accomodation\\ToBeVerified\\cleaned","2.raw","master.txt"],
]

# create train_audio and train_mfc directories
dirlist = []
#mfdirlist = []
for lst in wavdirs_and_files:
	print(lst[0])
	dirlist.append(lst[0])

def copy_rename(root, rawfile, txtfile, i):
	copyfile(os.path.join(root, rawfile),
			 os.path.join(wavdir + "\\" + dir + "\\train_audio", rawfile))

	with io.open(root + "\\" + txtfile, "r", encoding="utf-8") as fr:
		for line in fr:
			wf.write(line)

	os.rename(os.path.join(wavdir + "\\" + dir + "\\train_audio", rawfile),
			  os.path.join(wavdir + "\\" + dir + "\\train_audio\\%08d"%(i) + ".raw"))

i=0

for dir in dirlist:
	if not os.path.exists(wavdir+ "\\"+dir+"\\train_audio"):
		os.makedirs(wavdir+ "\\"+dir+"\\train_audio")
	wf = io.open(wavdir + "\\" + dir + "\\master.txt", "w", encoding="utf-8")
	print(dir)
	filecounter = 0
	for root,dirs,files in os.walk(wavdir + "\\" + dir):
		if root.endswith("train_audio") or root.endswith("train_mfc"):
			continue
		for file in files:
			if file.endswith('.wav'):
				print(file)
				s = file.split(".wav")
				callcmd = "sox " + root + "\\"+file + " " + root + "\\"+ s[0]+".raw"
				call(callcmd,shell=True)
				copy_rename(root, file, s[0]+".txt", i)
				i = i+1
	wf.close()
# exit(1)

#for lst in dirlist:
#	mfdirlist.append(lst + "\\train_mfc")

#print(dirlist)

# create fileids

create_fileids(wavdir,dirlist,train_fileid,mfc_fileids_file)

			
audiodir = wavdir

transdir = wavdir
scriptlist = []

for lst in wavdirs_and_files:
	scriptlist.append(lst[0] + "\\" + lst[2])
	
print(scriptlist)

dirlist = []
for lst in wavdirs_and_files:
	dirlist.append(lst[0] + "\\train_audio")
	
print(dirlist)

create_transcripts(transfile,super_prompts_file,trfile,scriptlist,dirlist,wavdir)

ml.createDictionary(super_prompts_file, train_dict, cs.Kannada)
#create_dictionary("..\\eng.dic",super_prompts_file,dictutil,phonefile,train_dict)

dirlist = []
for lst in wavdirs_and_files:
	print(lst[0])
	dirlist.append(lst[0])

call("E:\\asr\\bin\\sphinx_fe -argfile" + " " + org_model + "\\feat.params" + \
					 " -samprate 16000" + " -c" + " " + train_fileid + \
				 " -di" + " " + wavdir + \
				 " -do" + " " + mfcdir + \
				 " -ei raw -eo mfc -mswav no",shell=True
				 )

for di in dirlist:
	dirname = wavdir + "\\" + di
	print(dirname)
	srcdir = dirname + "\\train_audio"
	print(srcdir)
	dstdir = dirname + "\\train_mfc"
	callstr = "mkdir" + " " + dstdir
#	print(callstr)
	call(callstr,shell=True)
	callstr = "move" + " " + srcdir + "\\*.mfc" + " " + dstdir 
#	print(callstr)
	call(callstr,shell=True)

time.sleep(2)

call("E:\\asr\\bin\\pocketsphinx_mdef_convert" + " -text" + " " + org_model + "\\mdef" + " " + org_model + "\\mdef.txt",shell=True)

time.sleep(2)

print("calling bw")
call(
		"E:\\asr\\bin\\bw" + " " + "-hmmdir" + " " + org_model + \
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
		"E:\\asr\\bin\\mllr_solve" + " " + "-meanfn" + " " + org_model + "\\means" + \
								 " -varfn" + " " + org_model + "\\variances" + \
								 " -outmllrfn" + " " + metadata + "\\mllr_matrix" + \
								 " -accumdir" + " " + metadata,shell=True
  )	

time.sleep(2)

print("copying models")
callstr = "md" + " " + adapt_model
print(callstr)
call(callstr,shell=True)
call("copy E:\\asr\\models\\en-us\\*.* E:\\asr\\models\\en-us-adapt",shell=True)

time.sleep(2)
print("calling map_adapt")
call(
		"E:\\asr\\bin\\map_adapt" + " " + "-moddeffn" + " " + org_model + "\\mdef.txt" + \
						    " -ts2cbfn .ptm. " + \
							  " -meanfn" + " " + org_model + "\\means" + \
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
		"E:\\asr\\bin\\mk_s2sendump" + " " + "-pocketsphinx yes" + \
						      " -moddeffn" + " " + adapt_model + "\\mdef.txt" + \
									" -mixwfn" + " " + adapt_model + "\\mixture_weights" + \
									" -sendumpfn" + " " + adapt_model + "\\sendump" 
  )

time.sleep(2)	


#lmgen(infile,lmname)

'''
print("calling pocketsphinx_batch")	
call(
		"E:\\asr\\bin\\pocketsphinx_batch" + \
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
	
callcmd = "perl E:\\asr\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
print(callcmd)
cmdcall = callcmd + " > result\\res_adapt.txt"
print(cmdcall)
call(
		cmdcall, shell=True
  )
'''
'''	
print("calling pocketsphinx_batch")	
call(
		"E:\\asr\\bin\\pocketsphinx_batch" + \
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
	
c allcmd = "perl E:\\asr\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
print(callcmd)
cmdcall = callcmd + " > result\\res.txt"
print(cmdcall)
call(
		cmdcall, shell=True
  )
'''