from subprocess import call
import sys
import os
import codecs
import time
import unicodedata2 as uc
import data

flist = data.wavdirs_and_files
outfile = "out.txt"

voice_derivatives = ["p85","p115","s75","s125","p85_s125"]

newflist = []
for entry in flist:
	newflist.append(entry)
	for v in voice_derivatives:
		newdir = entry[0] + "_" + v
		newfile = entry[1].replace(".raw","") + "_" + v + ".raw"
		newentry = [newdir,newfile,entry[2]]
		newflist.append(newentry)
		

		
outf = open(outfile,"w",encoding="utf-8")
outf.write("wavdirs_and_files = [\n")
for entry in newflist:
	outf.write("\t\t[")
	outf.write("\"%s\","%(entry[0]))
	outf.write("\"%s\","%(entry[1]))
	outf.write("\"%s\""%(entry[2]))
	outf.write("],\n")
outf.write("]\n")	
outf.close()