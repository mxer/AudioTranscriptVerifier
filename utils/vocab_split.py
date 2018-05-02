# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 02:14:48 2016

@author: pankaj
"""

infiles = [
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_l.tsv",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_m.tsv",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_n.tsv"            
          ]

outfile = "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_engdev_words.txt"
fn = "J:\\New_Corpus\\train\\Reverie\\eng_hin.script.txt"

hindi_words = []  
sf = open(fn,"w",encoding="utf-8")        
for fname in infiles:
    f = open(fname,"r",encoding="utf-8")
    for line in f:
        words = line.split("\t")
        sf.write(words[1])
        for w in words[1].split():
            hindi_words.append(w)
    f.close()
sf.close()    
  
unique_words = set(hindi_words)

wf = open(outfile,"w",encoding="utf-8")

for w in unique_words:
    wf.write(w)
    wf.write("\n")
    
wf.close()
