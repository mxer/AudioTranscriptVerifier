# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 01:15:17 2016

@author: PANKAJ
"""

#LM configuration

import datetime, math, re
discount = 0.25

def lmgen(infile,lmname):
	sentfile =infile
	print("Language model started at %s"%(str(datetime.datetime.now())))
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
#				print(line)
				sent_cnt += 1
				words = re.split('\s',line)
#				for w in words:
#					print(w)
				length = len(words)
#				print(length)
				for index in range(0,length-2):
					s = " ";
					seq = (words[index],words[index+1],words[index+2])
#					print(words[index] + " " + words[index+1] + " " + words[index+2])
					tris = s.join(seq)
					if tris in trigram:
						trigram[tris] += 1
					else:
						trigram[tris] = 1
					s = " "
					seq = (words[index],words[index+1])
					bis=s.join(seq)
#					print(bis,len(bis))
					if bis in bigram:
						bigram[bis] += 1
					else:
						bigram[bis] = 1
					s = words[index]
#					print(s)
					if s in unigram:
						unigram[s] += 1
					else:
						unigram[s] = 1
	
#				print(index)
				s = " "
				seq = (words[index+1],words[index+2])
				bis=s.join(seq)
#				print(bis)
				if bis in bigram:
					bigram[bis] += 1
				else:
					bigram[bis] = 1
		
				s = words[index+1]
#				print(s)
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
#			print(x)
			bwlist = x.split()
			if (bwlist[0] == w1):
#				print(bwlist)
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
	return

