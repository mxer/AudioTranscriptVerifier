# -*- coding: utf-8 -*-
import os
import io
from subprocess import call
import unicodedata2 as uc
import requests
import json

phone_map = {
				u"\u0901" 	: u"AH N",				
				u"\u0902"	: u"N",						
				u"\u0903"	: u"AH HH AH",			
				u"\u0904"	: u"EY",			
				u"\u0905"	: u"AH",
				u"\u0906"	: u"AA",
				u"\u0907"	: u"IH",
				u"\u0908"	: u"IY",
				u"\u0909"	: u"UH",
				u"\u090A"	: u"UW",
				u"\u090B"	: u"R IH",
				u"\u090C"	: u"L R IH",
				u"\u090D"	: u"AE",
				u"\u090E"	: u"EY",
				u"\u090F"	: u"EY",
				u"\u0910"	: u"AE",
				u"\u0911"	: u"AO",
				u"\u0912"	: u"OW",
				u"\u0913"	: u"OW",
				u"\u0914"	: u"AO",
				u"\u0915"	: u"K",
				u"\u0916"	: u"K HH",
				u"\u0917"	: u"G",
				u"\u0918"	: u"G HH",
				u"\u0919"	: u"N",
				u"\u091A"	: u"CH",
				u"\u091B"	: u"CH HH",
				u"\u091C"	: u"JH",
				u"\u091D"	: u"JH HH",
				u"\u091E"	: u"N",
				u"\u091F"	: u"T",
				u"\u0920"	: u"TH",
				u"\u0921"	: u"D",
				u"\u0922"	: u"DH",
				u"\u0923"	: u"N",
				u"\u0924"	: u"T",
				u"\u0925"	: u"TH",
				u"\u0926"	: u"D",
				u"\u0927"	: u"DH",
				u"\u0928"	: u"N",
				u"\u0929"	: u"N",
				u"\u092A"	: u"P",
				u"\u092B"	: u"F",
				u"\u092C"	: u"B",
				u"\u092D"	: u"B HH",
				u"\u092E"	: u"M",
				u"\u092F"	: u"Y",
				u"\u0930"	: u"R",
				u"\u0931"	: u"R",
				u"\u0932"	: u"L",
				u"\u0933"	: u"L",
				u"\u0934"	: u"L",
				u"\u0935"	: u"W",
				u"\u0936"	: u"SH",
				u"\u0937"	: u"SH",
				u"\u0938"	: u"S",
				u"\u0939"	: u"HH",
				u"\u093A"	: u"",
				u"\u093B"	: u"",
				u"\u093C"	: u"",
				u"\u093D"	: u"AA",
				u"\u093E"	: u"AA",
				u"\u093F"	: u"IH",
				u"\u0940"	: u"IY",
				u"\u0941"	: u"UH",
				u"\u0942"	: u"UW",
				u"\u0943"	: u"R IH",
				u"\u0944"	: u"",
				u"\u0945"	: u"AE",
				u"\u0946"	: u"EY",
				u"\u0947"	: u"EY",
				u"\u0948"	: u"AE",
				u"\u0949"	: u"AO",
				u"\u094A"	: u"OW",
				u"\u094B"	: u"OW",
				u"\u094C"	: u"AO",
				u"\u094D"	: u"",
				u"\u094E"	: u"",
				u"\u0950"	: u"OW M",
				u"\u0951"	: u"",
				u"\u0952"	: u"",
				u"\u0953"	: u"",
				u"\u0954"	: u"",
				u"\u0955"	: u"",
				u"\u0956"	: u"",
				u"\u0957"	: u"",
				u"\u0958"	: u"K",
				u"\u0959"	: u"K HH",
				u"\u095A"	: u"G",
				u"\u095B"	: u"Z",
				u"\u095C"	: u"D",
				u"\u095D"	: u"DH",
				u"\u095E"	: u"F",
				u"\u095F"	: u"Y",
				u":"		: u"AH HH",
				u"!"		: u"",
				u"'"		: u"",
				u"‘"		: u"",
				u"\u2019"	: u"",
				u"\u200C"	: u"",
				u"\u200D"	: u"",
				u'\u2013'	: u"",				
				u'/'		: u"",
				u'['		: u"",
				u']'		: u"",
				u'*'		: u"",
				u'\u0964'	: u"",							
				u"\u0A81" 	: u"AH N",				
				u"\u0A82"	: u"N",						
				u"\u0A83"	: u"AH HH AH",			
				u"\u0A84"	: u"EY",			
				u"\u0A85"	: u"AH",
				u"\u0A86"	: u"AA",
				u"\u0A87"	: u"IH",
				u"\u0A88"	: u"IY",
				u"\u0A89"	: u"UH",
				u"\u0A8A"	: u"UW",
				u"\u0A8B"	: u"R IH",
				u"\u0A8C"	: u"L R IH",
				u"\u0A8D"	: u"AE",
				u"\u0A8E"	: u"EY",
				u"\u0A8F"	: u"EY",
				u"\u0A90"	: u"AE",
				u"\u0A91"	: u"AO",
				u"\u0A92"	: u"OW",
				u"\u0A93"	: u"OW",
				u"\u0A94"	: u"AO",
				u"\u0A95"	: u"K",
				u"\u0A96"	: u"K HH",
				u"\u0A97"	: u"G",
				u"\u0A98"	: u"G HH",
				u"\u0A99"	: u"N",
				u"\u0A9A"	: u"CH",
				u"\u0A9B"	: u"CH HH",
				u"\u0A9C"	: u"JH",
				u"\u0A9D"	: u"JH HH",
				u"\u0A9E"	: u"N",
				u"\u0A9F"	: u"T",
				u"\u0AA0"	: u"TH",
				u"\u0AA1"	: u"D",
				u"\u0AA2"	: u"DH",
				u"\u0AA3"	: u"N",
				u"\u0AA4"	: u"T",
				u"\u0AA5"	: u"TH",
				u"\u0AA6"	: u"D",
				u"\u0AA7"	: u"DH",
				u"\u0AA8"	: u"N",
				u"\u0AA9"	: u"N",
				u"\u0AAA"	: u"P",
				u"\u0AAB"	: u"F",
				u"\u0AAC"	: u"B",
				u"\u0AAD"	: u"B HH",
				u"\u0AAE"	: u"M",
				u"\u0AAF"	: u"Y",
				u"\u0AB0"	: u"R",
				u"\u0AB1"	: u"R",
				u"\u0AB2"	: u"L",
				u"\u0AB3"	: u"L",
				u"\u0AB4"	: u"L",
				u"\u0AB5"	: u"W",
				u"\u0AB6"	: u"SH",
				u"\u0AB7"	: u"SH",
				u"\u0AB8"	: u"S",
				u"\u0AB9"	: u"HH",
				u"\u0ABA"	: u"",
				u"\u0ABB"	: u"",
				u"\u0ABC"	: u"",
				u"\u0ABD"	: u"AA",
				u"\u0ABE"	: u"AA",
				u"\u0ABF"	: u"IH",
				u"\u0AC0"	: u"IY",
				u"\u0AC1"	: u"UH",
				u"\u0AC2"	: u"UW",
				u"\u0AC3"	: u"R IH",
				u"\u0AC4"	: u"",
				u"\u0AC5"	: u"AE",
				u"\u0AC6"	: u"EY",
				u"\u0AC7"	: u"EY",
				u"\u0AC8"	: u"AE",
				u"\u0AC9"	: u"AO",
				u"\u0ACA"	: u"OW",
				u"\u0ACB"	: u"OW",
				u"\u0ACC"	: u"AO",
				u"\u0ACD"	: u"",
				u"\u0ACE"	: u"",
				u"\u0ACF"	: u"",
				u"\u0AD0"	: u"OW M",
				u"\u0AD1"	: u"",
				u"\u0AD2"	: u"",
				u"\u0AD3"	: u"",
				u"\u0AD4"	: u"",
				u"\u0AD5"	: u"",
				u"\u0AD6"	: u"",
				u"\u0AD7"	: u"",
				u"\u0AD8"	: u"K",
				u"\u0AD9"	: u"K HH",
				u"\u0ADA"	: u"G",
				u"\u0ADB"	: u"Z",
				u"\u0ADC"	: u"D",
				u"\u0ADD"	: u"DH",
				u"\u0ADE"	: u"F",
				u"\u0ADF"	: u"Y",
				u"\u0AE0"	: u"R IY",
				u"\uFEFF"	: u"",




			}
			
vw_map = [
				u"\u0904", u"\u0905", u"\u0906", u"\u0907", u"\u0908", u"\u0909",
				u"\u090A", u"\u090B", u"\u090C", u"\u090D", u"\u090E", u"\u090F",
				u"\u0910", u"\u0911", u"\u0912", u"\u0913", u"\u0914"

				u"\u0A84", u"\u0A85", u"\u0A86", u"\u0A87", u"\u0A88", u"\u0A89",
				u"\u0A8A", u"\u0A8B", u"\u0A8C", u"\u0A8D", u"\u0A8E", u"\u0A8F",
				u"\u0A90", u"\u0A91", u"\u0A92", u"\u0A93", u"\u0A94"
		 ]
		 
				
matra_map = {
				u"\u0901", u"\u0902", u"\u0903", u"\u093D", u"\u093E", u"\u093F", u"\u0940",
				u"\u0941", u"\u0942", u"\u0943", u"\u0944", u"\u0945", u"\u0946", u"\u0947",
				u"\u0948", u"\u0949", u"\u094A", u"\u094B", u"\u094C", u"\u094D", u":",

				u"\u0A81", u"\u0A82", u"\u0A83", u"\u0ABD", u"\u0ABE", u"\u0ABF", u"\u0AC0",
				u"\u0AC1", u"\u0AC2", u"\u0AC3", u"\u0AC4", u"\u0AC5", u"\u0AC6", u"\u0AC7",
				u"\u0AC8", u"\u0AC9", u"\u0ACA", u"\u0ACB", u"\u0ACC", u"\u0ACD", u":",
			}


srcdir = "/home/pankaj/Downloads/audio_corpus/train"


def pronounce(inword):
#	print(inword)
#	print("length of in word is %d"%(len(inword)))
#	inword = "गंगा"
	wl = list(inword)
	nw = []
	wrdlen = len(wl)
	chcnt = 0
#	print(wrdlen)
	while chcnt < wrdlen:
#		print("chcnt %d"%(chcnt))
		ch = wl[chcnt]
#		print(ch)
		chcnt += 1
#		print(chcnt)
		if chcnt == wrdlen:
			if wrdlen == 1:
				if ch in matra_map:
					print(u"error")
				else:
					if ch in vw_map:
						nw.append(phone_map[ch])
					else:
						nw.append(phone_map[ch])
						nw.append(phone_map[u"अ"])
			else:
				nw.append(phone_map[ch])
		else:
			if ch in vw_map:
#				print("ch in vw_map")
#				print(ch)
				nw.append(phone_map[ch])
			else: 
				if ch not in matra_map:
#					print(ch)
#					print("ch not in matra map")
#					print(chcnt)
					if 	chcnt < wrdlen: 
						nch = wl[chcnt]
#						print(nch)
						if nch in matra_map:
#							print("nch in matra map")
							if chcnt+1 < wrdlen:
								nnch = wl[chcnt + 1]
								if nnch == u"\u0901":
									nw.append(phone_map[ch])
									nw.append(phone_map[nch])
									nw.append(phone_map[u"\u0902"])
									chcnt += 2
								else:
									nw.append(phone_map[ch])
									if nch == u"\u0902":
										nw.append("AH")
									nw.append(phone_map[nch])
									chcnt += 1
							else:
								nw.append(phone_map[ch])
								if nch == u"\u0902":
									nw.append("AH")
								nw.append(phone_map[nch])
								chcnt += 1
#							print(chcnt)
						else:
							nw.append(phone_map[ch])
							nw.append(phone_map[u"अ"])
				else:
					nw.append(phone_map[ch])
				
							
	return " ".join(' '.join(nw).split())
'''
rootdir = srcdir
wavdirs_and_files = file_list
pron_file = "app_pro.dict"
prdict = {}

for entry in wavdirs_and_files:
	ifn = rootdir + "/" + entry[0] + "/" + entry[1] + "/" + entry[3].replace(".","_dev.")
	inf = io.open(ifn,"r",encoding="utf-8")
	for line in iter(inf):
		wlist = line.lower().replace(".","").split()
		for w in wlist:
			if w not in prdict:
				prdict[w] = pronounce(w)
	inf.close()
	
pf = io.open(pron_file,"w",encoding="utf-8")
for key in sorted(prdict):
	pf.write(key + "\t" + prdict[key] +"\n")
pf.close()	

'''