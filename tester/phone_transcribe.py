import io

phfile ="phdict.txt"
dictfile = "J:\\asr\\eng.dic"
rootdir = "J:\\New_Corpus"
wavdirs_and_files = [
						["\\\\train\\\\3553\\\\female","3553_female.raw","3553_female.txt"],
						
						
					]

phdict = dict()
revphdict = dict()

phf = io.open(phfile,"r",encoding="utf-8")

for line in iter(phf):
	wl = line.split()
	phdict[wl[0]] = wl[1]
phf.close()

for key in phdict:
	revphdict[phdict[key]] = key


ld = dict()
df = io.open(dictfile,"r",encoding="utf-8")
for line in iter(df):
	entry = line.split("\t",1)
	ld[entry[0]] = entry[1]
df.close()

for entry in wavdirs_and_files:
	ifn = rootdir + "\\" + entry[0] + "\\" + entry[2]
	ofn = rootdir + "\\" + entry[0] + "\\" + entry[2].replace(".","_ph.")
	inf = io.open(ifn,"r",encoding="utf-8")
	otf = io.open(ofn,"w",encoding="utf-8")
	for line in iter(inf):
		wlist = line.split()
		nl = []
		for w in wlist:
			phw = ld[w].split()
			newphw = []
			for p in phw:
				newphw.append(phdict[p])
			word = ''.join(newphw)
			nl.append(word)
		newsent = ' '.join(nl)
		print(newsent)
		otf.write(newsent+"\n")
	inf.close()
	otf.close()
	ifn = rootdir + "\\" + entry[0] + "\\" + entry[2].replace(".","_ph.")
	inf = io.open(ifn,"r",encoding="utf-8")
	for line in iter(inf):
		wlist = line.split()
		nwlist = []
		for w in wlist:
			nw = []
			for ch in w:
				nw.append(revphdict[ch])
			nwlist.append(''.join(nw))
		print(' '.join(nwlist))

