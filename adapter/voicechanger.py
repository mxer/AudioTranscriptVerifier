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
import wave
corpus_dir = "J:\\New_corpus"
wavdirs_and_files = [
						["\\train\\3553\\female","3553_female.raw","3553_female.txt"],
						["\\train\\3553\\male","3553_male.raw","3553_male.txt"],
						["\\train\\3553\\pankaj","3553_pankaj.raw","3553_pankaj.txt"],		
						["\\train\\accomodation\\pankaj","accomodation_pankaj.raw","accomodation_pankaj.txt"],
						["\\train\\conversations\\pankaj","conversations_pankaj.raw","conversations_pankaj.txt"],
						["\\train\\converse_with_receptionist\\org","converse_reception_org.raw","converse_reception_org.txt"],
						["\\train\\converse_with_receptionist\\pankaj","converse_reception_pankaj.raw","converse_reception_pankaj.txt"],
						["\\train\\agra\\avdheshkumar\\script_c1","avdheshkumar_c1.raw","avdheshkumar_c1.txt"],
						["\\train\\agra\\avdheshkumar\\script_c2","avdheshkumar_c2.raw","avdheshkumar_c2.txt"],
						["\\train\\agra\\bhojraj\\script_b1","bhojraj_b1.raw","bhojraj_b1.txt"],
						["\\train\\agra\\deepak\\script_b1","deepak_b1.raw","deepak_b1.txt"],
						["\\train\\agra\\harimohan\\script_d1","harimohan_d1.raw","harimohan_d1.txt"],
						["\\train\\agra\\jeetu\\script_b2","jeetu_b2.raw","jeetu_b2.txt"],
						["\\train\\agra\\jeetu\\script_b3","jeetu_b3.raw","jeetu_b3.txt"],
						["\\train\\agra\\nandini\\script_d2","nandini_d2.raw","nandini_d2.txt"],
						["\\train\\agra\\nitesh\\script_c1","nitesh_c1.raw","nitesh_c1.txt"],
						["\\train\\agra\\nitesh\\script_c2","nitesh_c2.raw","nitesh_c2.txt"],
						["\\train\\agra\\nitesh\\script_c3","nitesh_c3.raw","nitesh_c3.txt"],
						["\\train\\agra\\nitesh\\script_c4","nitesh_c4.raw","nitesh_c4.txt"],
						["\\train\\agra\\nitesh\\script_c5","nitesh_c5.raw","nitesh_c5.txt"],
						["\\train\\agra\\nitesh\\script_e1","nitesh_e1.raw","nitesh_e1.txt"],
						["\\train\\agra\\pankaj\\script_a1","pankaj_a1.raw","pankaj_a1.txt"],
						["\\train\\agra\\pankaj\\script_a2","pankaj_a2.raw","pankaj_a2.txt"],
						["\\train\\agra\\pankaj\\script_a3","pankaj_a3.raw","pankaj_a3.txt"],
						["\\train\\agra\\pankaj\\script_a4","pankaj_a4.raw","pankaj_a4.txt"],
						["\\train\\agra\\pankaj\\script_a5","pankaj_a5.raw","pankaj_a5.txt"],
						["\\train\\agra\\pankaj\\script_b1","pankaj_b1.raw","pankaj_b1.txt"],
						["\\train\\agra\\pankaj\\script_c1","pankaj_c1.raw","pankaj_c1.txt"],
						["\\train\\agra\\pankaj\\script_d1","pankaj_d1.raw","pankaj_d1.txt"],
						["\\train\\agra\\pankaj\\script_d5","pankaj_d5.raw","pankaj_d5.txt"],
						["\\train\\agra\\pankaj\\script_e1","pankaj_e1.raw","pankaj_e1.txt"],
						["\\train\\agra\\pankaj\\script_e2","pankaj_e2.raw","pankaj_e2.txt"],
						["\\train\\agra\\ramavtar\\script_e1","ramavtar_e1.raw","ramavtar_e1.txt"],
						["\\train\\agra\\seema\\script_d3","seema_d3.raw","seema_d3.txt"],
						["\\train\\agra\\swasti\\script_d4","swasti_d4.raw","swasti_d4.txt"],
						["\\train\\agra\\yogendra\\script_c5","yogendra_c5.raw","yogendra_c5.txt"],
						["\\train\\agra\\sanjay\\script_a1","sanjay_a1.raw","sanjay_a1.txt"],
						["\\train\\agra\\sanjay\\script_a2","sanjay_a2.raw","sanjay_a2.txt"],
						["\\train\\agra\\tarni\\script_d1","tarni_d1.raw","tarni_d1.txt"],
						["\\train\\agra\\tarni\\script_d2","tarni_d2.raw","tarni_d2.txt"],
						["\\train\\agra\\tarni\\script_d3","tarni_d3.raw","tarni_d3.txt"],
						["\\train\\agra\\tarni\\script_d4","tarni_d4.raw","tarni_d4.txt"],
						["\\train\\agra\\tarni\\script_d5","tarni_d5.raw","tarni_d5.txt"],
						["\\train\\agra\\utsav\\script_e5","utsav_e5.raw","utsav_e5.txt"],
						["\\train\\agra\\utsav\\script_e4","utsav_e4.raw","utsav_e4.txt"],
						["\\train\\reverie\\sneha\\set_g","sneha_set_g.raw","sneha_set_g.txt"],
						["\\train\\reverie\\sneha\\set_h","sneha_set_h.raw","sneha_set_h.txt"],
						["\\train\\reverie\\sneha\\set_i","sneha_set_i.raw","sneha_set_i.txt"],
						["\\train\\reverie\\sneha\\set_n","sneha_set_n.raw","sneha_set_n.txt"],
						["\\train\\reverie\\amit\\set_a","amit_set_a.raw","amit_set_a.txt"],
						["\\train\\reverie\\amit\\set_b","amit_set_b.raw","amit_set_b.txt"],
						["\\train\\reverie\\amit\\set_c","amit_set_c.raw","amit_set_c.txt"],
						["\\train\\bade_bhai_sahab","bade_bhai_sahab.raw","bade_bhai_sahab.txt"],
						["\\train\\abhishek","abhishek.raw","abhishek.txt"],
						["\\train\\vivek","vivek.raw","vivek.txt"],
						["\\train\\iiith_hindi_sukh\\female\\set_0","iiith_hindi_sukh_female_set_0.raw","iiith_hindi_sukh_female_set_0.txt"],
					]

wavhdr_file = "wavhdr.txt"
targets = {"p85":"-pitch=-2","p115":"-pitch=2","s75":"-tempo=-25","s125":"-tempo=+25","p85_s125":"-pitch=-2 -tempo=+25"}				
convert_util = "..\\bin\\soundstretchD.exe"	
wf = open(wavhdr_file,"w",encoding="utf-8")
for entry in wavdirs_and_files:
	container_dir = corpus_dir + entry[0]
	for tgt in targets:
#		print(tgt)
		newdir = container_dir + "_%s"%(tgt)
#		print(newdir)
		if not os.path.exists(newdir):
			os.makedirs(newdir)
		src = container_dir + "\\" + entry[2]
#		print(src)
		dst = newdir + "\\" + entry[2]
#		print(dir)
		call("copy %s %s"%(src,dst),shell=True)
		src = container_dir + "\\" + entry[1]
		dst = newdir + "\\" + entry[1] + "_%s"%(tgt)
		with open(src, 'rb') as pcmfile:
			pcmdata = pcmfile.read()
		dfn = entry[1][0:len(entry[1])-4]
#		print(dfn)
		dst = newdir + "\\" + dfn + ".wav"
#		print(dst)
		with wave.open(dst, 'wb') as wavfile:
			wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NOT COMPRESSED'))
			wavfile.writeframes(pcmdata)
		
		callstr = convert_util + ' ' + dst + ' ' + newdir + "\\" + dfn + "_%s"%(tgt) + ".wav" + ' ' + targets[tgt]
#		print(callstr)
		call(callstr,shell=True)

		callstr = "del" + " " + dst
#		print(callstr)
		call(callstr,shell=True)
		
		src = newdir + "\\" + dfn +  "_%s"%(tgt) + ".wav"
#		print(src)
		dst = newdir + "\\" + dfn +  "_%s"%(tgt) + ".raw"
#		print(dst)
		with wave.open(src, 'rb') as wavfile:
#			wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NOT COMPRESSED'))
			pcmdata = wavfile.readframes(wavfile.getnframes())

		with open(dst, 'wb') as pcmfile:
			pcmfile.write(pcmdata)
		
		callstr = "del" + " " + src
#		print(callstr)
		call(callstr,shell=True)
		
wf.write("wavdirs_and_files = [\n")
for entry in wavdirs_and_files:
	container_dir = entry[0]
	print(container_dir)
	for tgt in targets:
		newdir = container_dir + "_%s"%(tgt)
		newdir = "\\\\".join(newdir.split("\\"))
		dfn = entry[1][0:len(entry[1])-4]
		src = dfn + "_%s"%(tgt) + ".raw"
		txt = dfn + "_%s"%(tgt) + ".txt"
		hdrentry = "[" + newdir + " ," + src + " ," + txt +"]," 
		print(hdrentry)
		wf.write("\t\t\t\t" + hdrentry+"\n")
wf.write("]\n")
wf.close()