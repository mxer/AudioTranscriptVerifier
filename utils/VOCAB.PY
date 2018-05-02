

infile = "J:\\New_Corpus\\train\\Reverie\\snapdeal_eng.txt"
outfile = "J:\\New_Corpus\\train\\Reverie\\snapdeal_eng.vocab.txt"

f = open(infile,"r",encoding = "utf-8")
v = open(outfile,"w",encoding="utf-8")

wordlist = []
for line in f:
    for words in line.split():
            wordlist.append(words)
            
wordlist = set(wordlist)

for w in wordlist:
    v.write(w)
    v.write("\n")
    
f.close()
v.close()