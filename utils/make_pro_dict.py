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
file_list = [
						["agra","avdheshkumar/script_c1","avdheshkumar_c1.raw","avdheshkumar_c1.txt"],
						["agra","avdheshkumar/script_c2","avdheshkumar_c2.raw","avdheshkumar_c2.txt"],
						["agra","bhojraj/script_b1","bhojraj_b1.raw","bhojraj_b1.txt"],
						["agra","deepak/script_b1","deepak_b1.raw","deepak_b1.txt"],
						["agra","harimohan/script_d1","harimohan_d1.raw","harimohan_d1.txt"],
						["agra","Jeetu/script_b2","jeetu_b2.raw","jeetu_b2.txt"],
						["agra","Jeetu/script_b3","jeetu_b3.raw","jeetu_b3.txt"],
						["agra","Jeetu/script_d1","jeetu_d1.raw","jeetu_d1.txt"],
						["agra","nandini/script_d2","nandini_d2.raw","nandini_d2.txt"],
						["agra","nitesh/script_c1","nitesh_c1.raw","nitesh_c1.txt"],
						["agra","nitesh/script_c2","nitesh_c2.raw","nitesh_c2.txt"],
						["agra","nitesh/script_c3","nitesh_c3.raw","nitesh_c3.txt"],
						["agra","nitesh/script_c4","nitesh_c4.raw","nitesh_c4.txt"],
						["agra","nitesh/script_c5","nitesh_c5.raw","nitesh_c5.txt"],
						["agra","nitesh/script_e1","nitesh_e1.raw","nitesh_e1.txt"],
						["agra","pankaj/script_a1","pankaj_a1.raw","pankaj_a1.txt"],
						["agra","pankaj/script_a2","pankaj_a2.raw","pankaj_a2.txt"],
						["agra","pankaj/script_a3","pankaj_a3.raw","pankaj_a3.txt"],
						["agra","pankaj/script_a4","pankaj_a4.raw","pankaj_a4.txt"],
						["agra","pankaj/script_a5","pankaj_a5.raw","pankaj_a5.txt"],
						["agra","pankaj/script_b1","pankaj_b1.raw","pankaj_b1.txt"],
						["agra","pankaj/script_b2","pankaj_b2.raw","pankaj_b2.txt"],
						["agra","pankaj/script_b3","pankaj_b3.raw","pankaj_b3.txt"],
						["agra","pankaj/script_b4","pankaj_b4.raw","pankaj_b4.txt"],
						["agra","pankaj/script_b5","pankaj_b5.raw","pankaj_b5.txt"],
						["agra","pankaj/script_c1","pankaj_c1.raw","pankaj_c1.txt"],
						["agra","pankaj/script_c2","pankaj_c2.raw","pankaj_c2.txt"],
						["agra","pankaj/script_c3","pankaj_c3.raw","pankaj_c3.txt"],
						["agra","pankaj/script_c4","pankaj_c4.raw","pankaj_c4.txt"],
						["agra","pankaj/script_c5","pankaj_c5.raw","pankaj_c5.txt"],
						["agra","pankaj/script_d1","pankaj_d1.raw","pankaj_d1.txt"],
						["agra","pankaj/script_d2","pankaj_d2.raw","pankaj_d2.txt"],
						["agra","pankaj/script_d3","pankaj_d3.raw","pankaj_d3.txt"],
						["agra","pankaj/script_d4","pankaj_d4.raw","pankaj_d4.txt"],
						["agra","pankaj/script_d5","pankaj_d5.raw","pankaj_d5.txt"],
						["agra","pankaj/script_e1","pankaj_e1.raw","pankaj_e1.txt"],
						["agra","pankaj/script_e2","pankaj_e2.raw","pankaj_e2.txt"],
						["agra","ramavtar/script_e1","ramavtar_e1.raw","ramavtar_e1.txt"],
						["agra","seema/script_d3","seema_d3.raw","seema_d3.txt"],
						["agra","swasti/script_d4","swasti_d4.raw","swasti_d4.txt"],
						["agra","yogendra/script_c5","yogendra_c5.raw","yogendra_c5.txt"],
						["agra","sanjay/script_a1","sanjay_a1.raw","sanjay_a1.txt"],
						["agra","sanjay/script_a2","sanjay_a2.raw","sanjay_a2.txt"],
						["agra","sanjay/script_a2","sanjay_a2.raw","sanjay_a2.txt"],
						["agra","tarni/script_d1","tarni_d1.raw","tarni_d1.txt"],
						["agra","tarni/script_d2","tarni_d2.raw","tarni_d2.txt"],
						["agra","tarni/script_d3","tarni_d3.raw","tarni_d3.txt"],
						["agra","tarni/script_d4","tarni_d4.raw","tarni_d4.txt"],
						["agra","tarni/script_d5","tarni_d5.raw","tarni_d5.txt"],
						["agra","utsav/script_e5","utsav_e5.raw","utsav_e5.txt"],
						["agra","utsav/script_e4","utsav_e4.raw","utsav_e4.txt"],
						["reverie","amarjeet/hyb7_0","amarjeet_hyb7_0.raw","amarjeet_hyb7_0.txt"],
						["reverie","amarjeet/hyb7_1","amarjeet_hyb7_1.raw","amarjeet_hyb7_1.txt"],
						["reverie","amarjeet/hyb7_2","amarjeet_hyb7_2.raw","amarjeet_hyb7_2.txt"],
						["reverie","amarjeet/hyb7_3","amarjeet_hyb7_3.raw","amarjeet_hyb7_3.txt"],
						["reverie","amarjeet/hyb7_4","amarjeet_hyb7_4.raw","amarjeet_hyb7_4.txt"],
						["reverie","amarjeet/hyb8_0","amarjeet_hyb8_0.raw","amarjeet_hyb8_0.txt"],
						["reverie","amarjeet/hyb8_1","amarjeet_hyb8_1.raw","amarjeet_hyb8_1.txt"],
						["reverie","amarjeet/hyb8_2","amarjeet_hyb8_2.raw","amarjeet_hyb8_2.txt"],
						["reverie","amarjeet/hyb8_3","amarjeet_hyb8_3.raw","amarjeet_hyb8_3.txt"],
						["reverie","amarjeet/hyb8_4","amarjeet_hyb8_4.raw","amarjeet_hyb8_4.txt"],
						["reverie","arunjeyan/eng0_0","arunjeyan_eng0_0.raw","arunjeyan_eng0_0.txt"],
						["reverie","amogh/eng0_1","amogh_eng0_1.raw","amogh_eng0_1.txt"],		
						["reverie","avinash/hyb0_0","avinash_hyb0_0.raw","avinash_hyb0_0.txt"],		
						["reverie","bhupen/hyb6_0","bhupen_hyb6_0.raw","bhupen_hyb6_0.txt"],		
						["reverie","gitika/hyb5_0","gitika_hyb5_0.raw","gitika_hyb5_0.txt"],		
						["reverie","pakhi/hyb1_0","pakhi_hyb1_0.raw","pakhi_hyb1_0.txt"],		
						["reverie","ranvijay/hyb2_0","ranvijay_hyb2_0.raw","ranvijay_hyb2_0.txt"],		
						["reverie","ranvijay/hyb2_1","ranvijay_hyb2_1.raw","ranvijay_hyb2_1.txt"],		
						["reverie","saikiran/eng1_4","saikiran_eng1_4.raw","saikiran_eng1_4.txt"],		
						["reverie","tinku/hyb2_0","tinku_hyb2_0.raw","tinku_hyb2_0.txt"],		
						["reverie","vivek/hyb9_0","vivek_hyb9_0.raw","vivek_hyb9_0.txt"],		
						["reverie","vivek/hyb9_1","vivek_hyb9_1.raw","vivek_hyb9_1.txt"],		
						["reverie","vivek/hyb9_2","vivek_hyb9_2.raw","vivek_hyb9_2.txt"],		
						["reverie","vivek/hyb9_3","vivek_hyb9_3.raw","vivek_hyb9_3.txt"],		
						["reverie","vivek/hyb9_4","vivek_hyb9_4.raw","vivek_hyb9_4.txt"],		
						["reverie","sneha/set_g","sneha_set_g.raw","sneha_set_g.txt"],
						["reverie","sneha/set_h","sneha_set_h.raw","sneha_set_h.txt"],
						["reverie","sneha/set_i","sneha_set_i.raw","sneha_set_i.txt"],
						["reverie","sneha/set_n","sneha_set_n.raw","sneha_set_n.txt"],
						["reverie","sabith/set_m","sabith_set_m.raw","sabith_set_m.txt"],		
						["reverie","amit_dave/set_a","amit_set_a.raw","amit_set_a.txt"],
						["reverie","amit_dave/set_b","amit_set_b.raw","amit_set_b.txt"],
						["reverie","amit_dave/set_c","amit_set_c.raw","amit_set_c.txt"],
						["reverie","amit_dave/set_d","amit_set_d.raw","amit_set_d.txt"],
						["reverie","amit_dave/set_e","amit_set_e.raw","amit_set_e.txt"],
						["reverie","amit_dave/set_e","amit_set_e.raw","amit_set_e.txt"],
						["reverie","amit_dave/set_f","amit_set_f.raw","amit_set_f.txt"],
						["others","anurag_sharma/andher","andher.raw","andher.txt"],
						["others","anurag_sharma/gharjamai","gharjamai.raw","gharjamai.txt"],
						["others","anurag_sharma/kheti","kheti.raw","kheti.txt"],
						["others","anurag_sharma/ukhade_khambe","ukhade_khambe.raw","ukhade_khambe.txt"], 
						["others","3553/pankaj","3553_pankaj.raw","3553_pankaj.txt"],
						["others","accomodation/pankaj","accomodation_pankaj.raw","accomodation_pankaj.txt"],
						["others","around_town/pankaj","around_town_pankaj.raw","around_town_pankaj.txt"],
						["others","conversations/pankaj","conversations_pankaj.raw","conversations_pankaj.txt"],
						["others","converse_reception/pankaj","converse_reception_pankaj.raw", "converse_reception_pankaj.txt"],
						["others","indic_tts/hindi/male_mono","hindi_male_mono.raw","hindi_male_mono.txt"],
						["others","indic_tts/hindi/female_mono","hindi_female_mono.raw","hindi_female_mono.txt"],
						["others","indic_tts/gujarati/male_mono","gujarati_male_mono.raw","gujarati_male_mono.txt"],
						["others","indic_tts/rajasthani/male_mono","rajasthani_male_mono.raw","rajasthani_male_mono.txt"],
						["others","indic_tts/marathi/male_mono","marathi_male_mono.raw","marathi_male_mono.txt"],
						["others","indic_tts/marathi/female_mono","marathi_female_mono.raw","marathi_female_mono.txt"],
						["others","cmu_indic_hi/axb","cmu_indic_hi_axb.raw","cmu_indic_hi_axb.txt"],
						["others","cmu_indic_hi/sxs","cmu_indic_hi_axb.sxs","cmu_indic_hi_sxs.txt"],
						["others","cmu_indic_mr/aup","cmu_indic_mr_aup.raw","cmu_indic_mr_aup.txt"],
						["others","cmu_indic_mr/slp","cmu_indic_mr_slp.sxs","cmu_indic_mr_slp.txt"],
						["reverie","pankaj/chat0","pankaj_chat0.raw","pankaj_chat0.txt"],
						["reverie","pankaj/chat1","pankaj_chat1.raw","pankaj_chat1.txt"],
						["reverie","pankaj/misc0","pankaj_misc0.raw","pankaj_misc0.txt"],
						["reverie","pankaj/story0_0","taali.raw","taali.txt"],
						["reverie","pankaj/story1_0","story1_0.raw","story1_0.txt"],
						["reverie","pankaj/ith0","pankaj_ith0.raw","pankaj_ith0.txt"],
						["reverie","pankaj/ith1","pankaj_ith1.raw","pankaj_ith1.txt"],
						["reverie","pankaj/ith2","pankaj_ith2.raw","pankaj_ith2.txt"],
						["reverie","pankaj/ith3","pankaj_ith3.raw","pankaj_ith3.txt"],
						["reverie","pankaj/karmabhumi_0","karmabhumi_0.raw","karmabhumi_0.txt"],
						["reverie","pankaj/karmabhumi_1","karmabhumi_1.raw","karmabhumi_1.txt"],
						["reverie","pankaj/karmabhumi_2","karmabhumi_2.raw","karmabhumi_2.txt"],						   
				["test","pankaj/set_a","pankaj_test_set_a.raw","pankaj_test_set_a.txt"],			
						
			]


def pronounce(inword):
	print(inword)
	print("length of in word is %d"%(len(inword)))
	wl = list(inword)
	nw = []
	wrdlen = len(wl)
	chcnt = 0;
	print(wrdlen)
	while chcnt < wrdlen:
		print("chcnt %d"%(chcnt))
		ch = wl[chcnt]
		print(ch)
		chcnt += 1
		print(chcnt)
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
				print("ch in vw_map")
				print(ch)
				nw.append(phone_map[ch])
			else: 
				if ch not in matra_map:
					print(ch)
					print("ch not in matra map")
					print(chcnt)
					if 	chcnt < wrdlen: 
						nch = wl[chcnt]
						print(nch)
						if nch in matra_map:
							print("nch in matra map")
							nw.append(phone_map[ch])
							nw.append(phone_map[nch])
							chcnt += 1
							print(chcnt)
						else:
							nw.append(phone_map[ch])
							nw.append(phone_map[u"अ"])
				else:
					nw.append(phone_map[ch])
				
							
	return " ".join(' '.join(nw).split())

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

