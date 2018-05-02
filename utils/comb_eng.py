# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 02:14:48 2016

@author: pankaj
"""

infiles = [
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_l.txt",            
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_m.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_n.txt",
          ]

outfile = "J:\\New_Corpus\\train\\Reverie\\snapdeal_eng.txt"

outf = open(outfile,"w",encoding="utf-8")

for file in infiles:
    inf = open(file,"r",encoding='utf-8')
    for line in inf:
        outf.write(line)
            
inf.close()
outf.close()
