# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 10:44:20 2017
@author: pankaj
"""
from subprocess import call
import sys
import os
import codecs
import time
import io
import re


vowel_map = {	
				"AA" : "आ",	"AE" : "ऐ",	"AH" : "अ",	"AO" : "औ",
				"AW" :"आउ",	"AY" : "आय",	"EH" : "ऍ", 	"EY" : "ए", 
				"IH" : "इ",	"IY" : "ई", 	"OW" : "ओ",	"OY" : "ऑय", 
				"UH" : "उ", 	"UW" : "ऊ"
			}
			
matra_map = {				
				"AA" : "ा",	"AE" : "ै",	"AH" : "",	"AO" : "ौ",
				"AW" :"ाउ",	"AY" : "ाय",	"EH" : "ॅ", 	"EY" : "े", 
				"IH" : "ि",	"IY" : "ी", 	"OW" : "ो",	"OY" : "ॉय", 
				"UH" : "ु", 	"UW" : "ू"
			}
			
consonant_map = {
					"B"  : "ब",	"CH" : "च",	"D" : "ड",	"DH" : "द",
					"ER" : "र",	"F"	 : "फ",	"G" : "ग",	"HH" : "ह",
					"JH" : "ज",	"K"  : "क",	"L" : "ल",	"M"	 : "म",
					"N"	 : "न",  "NG" : "न्ग",	"P" : "प",	"R"	 : "र",
					"S"	 : "स",	"SH" : "श",	"T" : "ट",	"TH" : "थ",
					"V"  : "व",	"W"  : "व",  "Y"	: "य",	"Z"	 : "ज़",
					"ZH" : "झ"
				}
				
input_strings = [
                    "AH M IY R", "AH L AH K AH N AH N D AA", 
                    "K UH T T AA", "JH AH M P AH R", "M EY R IY V IH DH EY SH Y AA T R AA",
                    "IH N T ER S EH P T ER Z","G R AE N T IH NG","G EH G IH N HH AY M ER","P L EY T L AY K","K ER S"
                ]

def phone_to_word(instr):
	first_char = 1
	prev_char = "VOWEL"
	phnlist = instr.split()
	phnlen = len(phnlist)
	chcnt = 0
	chstr = []
	while chcnt < phnlen:
		ch = phnlist[chcnt]
		if first_char == 1:
			if ch in vowel_map:
				chstr.append(vowel_map[ch])
				prev_char = "VOWEL"
			else:
				if (chcnt + 1) < phnlen:
					if phnlist[chcnt+1] in vowel_map:
						chstr.append(consonant_map[ch])
						prev_char = "CONSONANT"
					else:
						if phnlist[chcnt+1] == "ER":
							chstr.append(consonant_map[ch])
						else:
							chstr.append(consonant_map[ch])
							chstr.append("्")
			first_char = 0
			chcnt += 1
		else:
			if ch in vowel_map:
				if prev_char == "CONSONANT":
					chstr.append(matra_map[ch])
					prev_char = "VOWEL"
				else:
					chstr.append(vowel_map[ch])
					prev_char = "VOWEL"
				chcnt += 1
			else:
				if (chcnt + 1) < phnlen:
					if phnlist[chcnt+1] in vowel_map:
						chstr.append(consonant_map[ch])
						prev_char = "CONSONANT"
					else:
						if phnlist[chcnt+1] == "ER":
							chstr.append(consonant_map[ch])
						else:
							chstr.append(consonant_map[ch])
							chstr.append("्")
						prev_char = "CONSONANT"
				else:
					chstr.append(consonant_map[ch])
					prev_char = "CONSONANT"				
				chcnt += 1
	chstr = ''.join(chstr)
	return chstr			
		