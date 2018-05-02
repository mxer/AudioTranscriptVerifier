from subprocess import call
import sys
import os
import codecs
import time
import unicodedata2 as uc
import re
import adutil

rootdir = "J:\\new_corpus"

wavdirs_and_files = [
						["\\train\\3553\\female","3553_female.raw","3553_female.txt"],
					]

for entry in wavdirs_and_files:
	srcfile = rootdir + entry[0] + "\\" + entry[2]
	dstfile = rootdir + entry[0] + "\\" + entry[2].replace(".","_lt.")
	sf = open(srcfile,"r",encoding="utf-8")
	df = open(dstfile,"w",encoding="utf-8")
	for line in iter(sf):
		wordlist = line.replace("\r","").replace("\n","").split()
		print(wordlist)
		englist = []
		for word in wordlist:
			if uc.script(word) == 'Devanagari':
				callcmd = 'curl -X """POST""" -H """Content-Type: application/json""" -H """Cache-Control: no-cache""" -H """Postman-Token: 697b7df1-ce6b-5caf-a043-a34c98eb7ed1""" -d "'"{"""inArray""":["""भूपेन"""],"""REV-APP-ID""":"""rev.web.com.rev.master""","""REV-API-KEY""":"""9757f28c968b561ea36ffbea2ff562679148""","""webSdk""":0}"'" """http://api.reverieinc.com/parabola/reverseTransliterateSimple"""'
				call(callcmd,shell=True)




