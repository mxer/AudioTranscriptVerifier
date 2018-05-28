# -*- coding: utf-8 -*-
from subprocess import call
import sys
import os
import codecs
import time
import re
import adapter.unicodedata2 as uc
import io

def file_split(bindir,inraw_file,rawdir):
	if not os.path.exists(rawdir):
		os.makedirs(rawdir)
	print(rawdir)
	sys.stdout.flush()
	callcmd = bindir + "\\" + "filesplit.exe" + " " + "-i" + " " + inraw_file + " " + "-rawlogdir" + " "  + rawdir
	#print(callcmd)
	sys.stdout.flush()
	call(
			callcmd,shell=True
		)
	return
	
def create_fileids(audiodir,dirlist,train_fileid,mfc_fileids_file):
	f = io.open(train_fileid,"w",encoding="utf-8")
	mf = io.open(mfc_fileids_file,"w",encoding="utf-8")
	filecounter = 0
	global_counter = 0
	for dir in dirlist:
		print(dir)
		filecounter = 0
		for root,dirs,files in os.walk(audiodir + "\\" + dir + "\\train_audio"):
			for file in files:
				if file.endswith('.raw'):
					print(file)
					arg = unicode("%s\\%08d\n"%(dir + "\\train_audio",filecounter))
					f.write(arg)
					mfdir = audiodir + "\\" + dir + "\\train_mfc"
					if not os.path.exists(mfdir):
						os.makedirs(mfdir)
					arg = unicode("%s\\%08d\n"%(audiodir+"\\"+dir + "\\train_mfc",filecounter))
					mf.write(arg)
					filecounter += 1
					global_counter += 1
	f.close()
	mf.close()
	print("the number of raw files are : %d"%(global_counter))
	
	return
	
def create_transcripts(transfile,super_prompts_file,trfile,scriptlist,dirlist,transdir):
	print(super_prompts_file)
	print(transfile)
	print(trfile)
	f = io.open(transfile,"w",encoding="utf-8")
	sf = io.open(super_prompts_file,"w",encoding="utf-8")
	tf = io.open(trfile,"w",encoding="utf-8")
	audiodir = transdir
	fcounter = 0
	index = 0
	for file in scriptlist:
		filename = transdir + "\\" + file
		print(filename)
		fcounter = 0
		with io.open(filename,"r",encoding="utf-8") as fr:
			filepath = audiodir + "\\" + dirlist[index]
			fpath = dirlist[index]
			print(filepath)
			for line in fr:
				if line=="\n":
					continue
				line = line.strip().lower()
				line = line.replace("\r", "").replace("\n", "").replace("/", " ").replace(":", u"").replace(u"॑", "").replace(u"|","").replace(u"।", "").replace(u"ʼ", "").replace(u"'", "").replace(u"-", " ").replace(u"…", "").replace(u"+", " ").replace(u'”', "").replace(u"ଵ", u"ୱ").replace("0", "").replace(u"\u200c", "").replace(u"\u200d", "")
#				print(line)
				f.write("<s> %s </s> (%s\\%08d)\n" % (line,filepath,fcounter))
				tf.write("<s> %s </s> (%s\\%08d)\n" % (line,fpath,fcounter))
				sf.write("%s\n" % (line))
				fcounter += 1
		index += 1
	f.close()
	sf.close()		
	tf.close()
	
def read_words(words_file):
    return [word for line in io.open(words_file, 'r',encoding="utf-8") for word in line.split()]

def merge_dict(dictlist,output_dict):
	dict_dbase = {}
	for dictfile in dictlist:
		df = io.open(dictfile,"r",encoding="utf-8")
		for line in df:
			word,pron = line.rstrip("\n").rstrip("\r").replace("\t"," ",1).split(" ",1)
			if word not in dict_dbase:
				dict_dbase[word] = []
			if pron not in dict_dbase[word]:
				dict_dbase[word].append(pron)
		df.close()
	
	of = io.open(output_dict,"w",encoding = "utf-8")
	for key in dict_dbase:
		value = dict_dbase[key]
		for i in range(0,len(value)):
			if i:
				of.write("%s(%d)\t%s\n"%(key,i+1,value[i]))
			else:
				of.write("%s\t%s\n"%(key,value[i]))
	of.close()
	return
		
def create_dictionary(seed_dict,super_prompts_file,dictutil,phonefile,appdic):
	# create a database of the dictionary
	outfile = "temp_hindi.dic"
	vocabfile = 'vocab.txt'
	unique_word_list = set(read_words(super_prompts_file))
	f = io.open(vocabfile,"w",encoding="utf-8")
	unk_hindi_vocab = "unk_hindi.txt"
	unk_english_vocab = "unk_english.txt"	
	uhwf = io.open(unk_hindi_vocab,"w",encoding="utf-8")
	uewf = io.open(unk_english_vocab,"w",encoding="utf-8")
	
		
	gdbase = {}
	ldbase = {}
	
	sdf = io.open(seed_dict,"r",encoding="utf-8")
	
	for line in sdf:
#		print(line)
		word,pron = line.rstrip("\n").rstrip("\r").replace("\t"," ",1).split(" ",1)
		word = re.sub(r'\([^)]*\)', '', word)
		value = []
		if word not in gdbase:
			gdbase[word] = []
			gdbase[word].append(pron)
#			print(word)
#			print(gdbase[word])
		else:
#			print(pron)
			if pron is not None:
#				print(gdbase[word])
				if gdbase[word] is not None and pron not in gdbase[word]:
#					print(gdbase[word])
#					print(pron)				
					gdbase[word].append(pron)
	sdf.close()
	unkhin = 0
	unkeng = 0
#	print(gdbase)
#	gdf = io.open("gdbase.txt","w",encoding="utf-8")
	for word in unique_word_list:
		f.write("%s\n"%(word))
		if uc.script(word[0]) == 'Latin':
			word = word.lower()
		if word in gdbase:
#			gdf.write(word+"\n")
			ldbase[word] = gdbase[word]
#			if (gdbase[word] is not None and len(gdbase[word]) > 1):
#				print(ldbase[word])
		else:
			if uc.script(word[0]) == 'Devanagari':
				unkhin = 1
				uhwf.write(word)
				uhwf.write("\n")
			elif uc.script(word[0]) == 'Latin':
				unkeng = 1
				uewf.write(word)
				uewf.write("\n")
			elif str.isnumeric(word[0]) == True:
				unkeng = 1
				uewf.write(word)
				uewf.write("\n")
			else:
				print(word)
				print("script not supported")

#	gdf.close()			
	f.close()
	uhwf.close()
	uewf.close()

#	ldbase = sorted(ldbase)
#	print(type(ldbase))
	print(appdic)
	af = io.open(appdic,"w",encoding="utf-8")
	keylist = sorted([key for key in ldbase])
	for key in keylist:
#		print(key)
		value = ldbase[key]
		if value is not None:
			for i in range(0,len(value)):
				if i > 0:
					af.write("%s(%d)\t%s\n"%(key,i+1,value[i]))
				else:
					af.write("%s\t%s\n"%(key,value[i]))
	af.close()
		
	if (unkhin == 1):
		callstr = dictutil + " " + phonefile + " " + unk_hindi_vocab + " " + outfile
		print(callstr)
		call(callstr,shell=True)
		af = io.open(appdic,"rb+")
		af.seek(-1,2)
		af.truncate()
		af.close()
		time.sleep(2)
		s = io.open(outfile, mode='r', encoding='utf-8-sig').read()
		io.open(outfile, mode='w', encoding='utf-8').write(s)
	if unkhin == 1:
		hf = io.open(outfile,"r",encoding="utf-8")
		af = io.open(appdic,"a",encoding="utf-8")
		for line in hf:
#			print(line)
			line = line.replace(" ","",1)
			af.write(line)
		hf.close()
		af.close()
	if (unkeng == 1):
		print("Unknown english words found\n")
		ef = io.open(unk_english_vocab,"r",encoding="utf-8")
		af = io.open(appdic,"a",encoding="utf-8")
		for line in ef:
#			print(line)
			af.write(line)
		ef.close()
		af.close()
	time.sleep(2)
	
	return