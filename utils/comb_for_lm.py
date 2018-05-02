# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 02:14:48 2016

@author: pankaj
"""

infiles = [
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_a.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_b.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_c.txt",            
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_d.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_e.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_f.txt",            
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_g.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_h.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_i.txt",            
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_j.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_k.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_l.txt",            
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_m.txt",
            "J:\\New_Corpus\\train\\Reverie\\snapdeal_set_n.txt",
          ]

outfile = "J:\\New_Corpus\\train\\Reverie\\snapdeal_for_lm.txt"

outf = open(outfile,"w",encoding="utf-8")

for file in infiles:
    inf = open(file,"r",encoding='utf-8')
    for line in inf:
        outf.write(line)
            
inf.close()
outf.close()
