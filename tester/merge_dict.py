#import sys
#import os
#import codecs
#import time
import re

dictlist = [
			 "..\\\\eng.dic",
			 "..\\\\revasr.dic",
		   ]
		   
outfile = "..\\\\eng.dic"

dict_dbase = {}
for dictfile in dictlist:
	df = open(dictfile,"r",encoding="utf-8")
	for line in df:
		word,pron = line.rstrip("\n").rstrip("\r").replace("\t"," ",1).split(" ",1)
		word = re.sub(r'\([^)]*\)', '', word)
		word = re.sub(r'\[[^]]*\)', '', word)
		if word not in dict_dbase:
			dict_dbase[word] = []
		if pron not in dict_dbase[word]:
			dict_dbase[word].append(pron)
	df.close()
	
of = open(outfile,"w",encoding = "utf-8")
for key in sorted(dict_dbase):
	value = dict_dbase[key]
	for i in range(0,len(value)):
		if i:
			of.write("%s(%d)\t%s\n"%(key,i+1,value[i]))
		else:
			of.write("%s\t%s\n"%(key,value[i]))
of.close()
