# -*- coding: utf-8 -*-
import glob
import os
import io
import pronounce as pr
import Constants as cs

# This script will prepare pronunciation files on the basis of a given phone file

# rootdir = "E:/STT_Apps/data"
rootdir = "E:/STT_Apps/data"
srcdata = [
                ["/train","/odia/odia_mono/odia_male_mono","","odia_male_mono.txt","male",cs.Hindi],
                
		  ]

def createDictionary(inputfile, outputfile):
	for entry in srcdata:
		newline = u""
		wordlist = []
		subroot = entry[0]
		container = entry[1]
		script = entry[3]
		#scriptfile = rootdir + subroot + container + "/" + script
		scriptfile = inputfile
		print("sc = "+scriptfile)
		sf = io.open(scriptfile,"r",encoding="utf-8")
		for line in sf:
			#print line.encode("utf-8")
			#wl = pp.replace(line)
			wl = line.replace("\r", "").replace("\n", "").replace("/", " ").replace(":", u"").replace(u"॑", "").replace(u"|","").replace(u"।", "").replace(u"ʼ", "").replace(u"'", "").replace(u"-", " ").replace(u"…", "").replace(u"+", " ").replace(u'”', "").replace(u"ଵ", u"ୱ").replace("0", "").replace(u"\u200c", "").replace(u"\u200d", "")
			splitted = wl.split(" ")
			for s in splitted:
				wordlist.append(s)
		sf.close()
		#wfile = scriptfile.replace(".txt",".wordlist.txt")
		pdictfile = outputfile
		#wf = io.open(wfile,"w",encoding="utf-8")
		pdf = io.open(pdictfile,"w",encoding="utf-8")
		wordlist = sorted(set(wordlist))
		mapped = pr.Mappings()
		for word in wordlist:
			#wf.write(unicode(newline + word))
			#print word.encode("UTF-8")
			pdf.write(newline + word + "\t" + mapped.pronounce(word, entry[5]))
			newline = u"\n"

		#wf.close()
		pdf.close()

	print ("***** dictionary file created ********")




