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

wavdir = "J:\\\\New_Corpus"
bindir = "J:\\\\asr\\\\bin"
lmname = "J:\\\\asr\\\\tester\\\\etc\\\\test.lm"
transfile = "etc\\hindi_model_test.transcription"
trfile = "etc\\test.transcription"
super_prompts_file = "etc\\hindi_model_test_prompt.txt"
phonefile = "..\\\\bin\\\\phonemap.txt"
hindi_phone_file = "..\\\\bin\\\\hindiphone.txt"
infile = "etc\\\\hindi_model_test_prompt.txt"
vocabfile = "etc\\\\hindi_model_test_vocab.txt"
outfile = "etc\\hindi_model_test_adaptation.dic"
dictutil = "J:\\\\asr\\\\bin\\\\progen.exe"

train_fileid = "etc\\\\hindi_model_adapt.fileids"
mfc_fileids_file = "etc\\\\hindi_model_adapt_mfc.fileids"

wavdir = "J:\\\\New_Corpus"
mfcdir = "J:\\\\New_Corpus"
metadata = "metadata"

rootdir = "J:\\\\asr"

org_model = rootdir + "\\\\" + "models\\\\en-us"
adapt_model = rootdir + "\\\\" + "models\\\\en-us-adapt"

train_dict = outfile
language_model = "etc\\test.lm"
dictionary = "etc\\hindi_model_test_adaptation.dic"	
hypfile = "result\\\\hindi_adapt.hyp.txt"
cepdir = wavdir

discount = 0.3

wavdirs_and_files = [
						
							["\\\\test\\\\3553\\\\pankaj","3553_pankaj.raw","3553_pankaj.txt"],
							["\\\\test\\\\3553\\\\pankaj_a","3553_pankaj_a.raw","3553_pankaj_a.txt"],
#							["\\\\test\\\\rakhee\\\\snap\\\\pure","test_rakhee_snap_pure.raw","test_rakhee_snap_pure.script.txt"],
#							["\\\\test\\\\vivek","test_vivek.raw","test_vivek.txt"],
#							["\\\\test\\\\amjad","amjad_test.raw","amjad_test.txt"],
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
		
audiodir = wavdir
dirlist = []
mfdirlist = []
for lst in wavdirs_and_files:
	print(lst[0])
	dirlist.append(lst[0])
	
for lst in dirlist:
	mfdirlist.append(lst + "\\\\test_mfc")

print(dirlist)
print(mfdirlist)


f = open(train_fileid,"w",encoding="utf-8")
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

transdir = wavdir
scriptlist = []

for lst in wavdirs_and_files:
	scriptlist.append(lst[0] + "\\\\" + lst[2])
	
print(scriptlist)

dirlist = []
for lst in wavdirs_and_files:
	dirlist.append(lst[0] + "\\\\test_audio")
	
print(dirlist)


f = open(transfile,"w",encoding="utf-8")
sf = open(super_prompts_file,"w",encoding="utf-8")
tf = open(trfile,"w",encoding="utf-8")

fcounter = 0
index = 0
for file in scriptlist:
	filename = transdir + "\\\\" + file
	fcounter = 0
	with open(filename,"r",encoding="utf-8") as fr:
		filepath = audiodir + "\\\\" + dirlist[index]
		fpath = dirlist[index]
		print(filepath)
		for line in fr:
			line = line.strip()
			f.write("<s> %s </s> (%s\\\\%08d)\n" % (line,filepath,fcounter))
			tf.write("<s> %s </s> (%s\\\\%08d)\n" % (line,fpath,fcounter))
			sf.write("%s\n" % (line))
			fcounter += 1
	index += 1
f.close()
sf.close()		
tf.close()

def read_words(words_file):
    return [word for line in open(words_file, 'r',encoding="utf-8") for word in line.split()]
	
	
#first generate a vocabulary
word_list = read_words(infile)
unique_word_list = set(word_list)
f = open(vocabfile,"w",encoding="utf-8")

for word in unique_word_list:
	f.write("%s\n"%(word))

f.close()

callstr = dictutil + " " + phonefile + " " + vocabfile + " " + outfile
print(callstr)
call(
		callstr,shell=True
	)

#LM configuration
sentfile =infile

import datetime, math, re

print("Language model started at %s"%(str(datetime.datetime.now())))

wflag = 0	
log10 = math.log(10.0)

if (discount != None):
	if ((discount <= 0.0) or (discount >= 1.0)):
		print("Discount value out of range: must be 0.0 < x < 1.0! ... using 0.5\n")
		discount_mass = 0.5
	else:
		discount_mass = discount
else:
	discount_mass = 0.5
	
deflator = 1.0 - discount_mass

#create count tables
sent_cnt = 0
trigram = {}
bigram = {}
unigram = {}
with open(sentfile,"r",encoding="utf-8") as sf:
	print("senfile opened")
	for line in sf:
		if line in ['\n','\r\n']:
			print ("empty line")
		else:
			line = line.strip()
			line = "<s> " + line + " </s>" 	
			line.join(line.split())
#			print(line)
			sent_cnt += 1
			words = re.split('\s',line)
#			for w in words:
#				print(w)
			length = len(words)
#			print(length)
			for index in range(0,length-2):
				s = " ";
				seq = (words[index],words[index+1],words[index+2])
#				print(words[index] + " " + words[index+1] + " " + words[index+2])
				tris = s.join(seq)
				if tris in trigram:
					trigram[tris] += 1
				else:
					trigram[tris] = 1
				s = " "
				seq = (words[index],words[index+1])
				bis=s.join(seq)
#				print(bis,len(bis))
				if bis in bigram:
					bigram[bis] += 1
				else:
					bigram[bis] = 1
				s = words[index]
#				print(s)
				if s in unigram:
					unigram[s] += 1
				else:
					unigram[s] = 1
	
#			print(index)
			s = " "
			seq = (words[index+1],words[index+2])
			bis=s.join(seq)
#			print(bis)
			if bis in bigram:
				bigram[bis] += 1
			else:
				bigram[bis] = 1
		
			s = words[index+1]
#			print(s)
			if s in unigram:
				unigram[s] += 1
			else:
				unigram[s] = 1
		
			s = words[index+2]
			if s in unigram:
				unigram[s] += 1
			else:
				unigram[s] = 1
	
sf.close()
'''
trif = open("trigrm.txt","w",encoding="utf-8")
for k in trigram:
    trif.write("%s %f\n"%(k,trigram[k]))
trif.close()
trif = open("bigrm.txt","w",encoding="utf-8")
for k in bigram:
    trif.write("%s %f\n"%(k,bigram[k]))
trif.close()
trif = open("unigrm.txt","w",encoding="utf-8")
for k in unigram:
    trif.write("%s %f\n"%(k,unigram[k]))
trif.close()
'''
#print(bigram)
#print(unigram)


if sent_cnt:
	print("%d sentences found\n"%(sent_cnt))
else:
	print("No input")
	exit()
	

lf = open(lmname,"w",encoding="utf-8")

if lf == None:
	print("Can't open LM file")
	exit()
	
unisum = 0
unicount = 0
bicount = 0
tricount = 0

for k in unigram:
	unicount += 1
	unisum += unigram[k]
	
	
for k in bigram:
	bicount += 1

for k in trigram:
	tricount += 1
	
lf.write("\\data\\\n")
lf.write("ngram 1=%d\n"%(unicount))
if(bicount > 0):
	lf.write("ngram 2=%d\n"%(bicount))
if (tricount > 0):
	lf.write("ngram 3=%d\n"%(tricount))
lf.write("\n")

#compute uni probs
uniprob = {}
for k in unigram:
	uniprob[k] = (unigram[k]/unisum) * deflator

alpha = {}

#compute alphas
for k in unigram:
	w1 = k
	sum_denom = 0.0
	for x in bigram:
		bwlist = x.split()
		if (bwlist[0] == w1):
			w2 = bwlist[1]
			sum_denom += uniprob[w2]
	alpha[w1] = discount_mass / (1.0 -sum_denom)
			
	
lf.write("\\1-grams:\n")
klist = []
for k in unigram:
	klist.append(k)
	lf.write("%6.4f %s %6.4f\n"%(math.log(uniprob[k])/log10, k, math.log(alpha[k])/log10))

lf.write("\n")

biprob = {}

#compute bi_probs
for x in bigram:
	bwlist = x.split()
	w1 = bwlist[0]
	biprob[x] = (bigram[x]*deflator)/(unigram[w1])

#for x in biprob:
#	print("%s :: %f"%(x,biprob[x]))

bialpha = {}	
#compute bialphas
for x in bigram:
	w1w2 = x
	sum_denom = 0.0
	for y in trigram:
		twlist = y.split()
		bistr = twlist[0] + " " + twlist[1]
		if (bistr == w1w2):
			w2w3 = twlist[1] + " " + twlist[2]
			sum_denom += biprob[w2w3]
	bialpha[w1w2] = discount_mass / (1.0 - sum_denom)
	
# output the bigrams and trigrams (now that we have the alphas computed)


if (bicount > 0):
	lf.write("\\2-grams:\n")
	for x in bigram:
		lf.write("%6.4f %s %6.4f\n"%(math.log(biprob[x])/log10, x, math.log(bialpha[x])/log10)) 
	
	lf.write("\n")
	
if (tricount > 0):
	lf.write("\\3-grams:\n")
	for x in trigram:
		twlist = x.split()
		w1w2 = twlist[0] + " " + twlist[1]
		lf.write("%6.4f %s\n"%(math.log((trigram[x]*deflator)/bigram[w1w2])/log10, x))
	lf.write("\n")
		
lf.write("\\end\\\n")
lf.close()
time.sleep(2)	


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
cmdcall = callcmd + " > result\\\\test_adapt.txt"
print(cmdcall)
call(
		cmdcall, shell=True
    )
	
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
cmdcall = callcmd + " > result\\\\test.txt"
print(cmdcall)
call(
		cmdcall, shell=True
    )
