#import sys
#import codecs


def read_words(words_file):
    return [word for line in open(words_file, 'r',encoding="utf-8") for word in line.split()]

transdir = "J:\\\\New_Corpus"
scriptlist = 	[
					"test\\\\3553\\\\pankaj\\\\3553_pankaj.txt",
                    "test\\\\rakhee\\\\snap\\\\pure\\\\test_rakhee_snap_pure.script.txt",
                    "test\\\\vivek\\\\test_vivek.script.txt",
				]
audiodir = "J:\\\\New_Corpus"
dirlist = 	[
				"test\\\\3553\\\\pankaj\\\\test_audio",
                "test\\\\rakhee\\\\snap\\\\pure\\\\test_audio",
                "test\\\\vivek\\\\test_audio",
			]

transfile = "etc\\hindi_model_test.transcription"
trfile = "etc\\test.transcription"
super_prompts_file = "etc\\hindi_model_test.script.txt"

f = open(transfile,"w",encoding="utf-8")
sf = open(super_prompts_file,"w",encoding="utf-8")
tf = open(trfile,"w",encoding="utf-8")

fcounter = 0
index = 0
for file in scriptlist:
	filename = transdir + "\\\\" + file
	fcounter = 0
	with open(filename,"r",encoding="utf-8") as fr:
		filepath = audiodir + "\\\\" + dirlist[index]
		fpath = dirlist[index]
		print(filepath)
		for line in fr:
			line = line.strip()
			f.write("<s> %s </s> (%s\\\\%08d)\n" % (line,filepath,fcounter))
			tf.write("<s> %s </s> (%s\\\\%08d)\n" % (line,fpath,fcounter))
			sf.write("%s\n" % (line))
			fcounter += 1
	index += 1
f.close()
sf.close()		
tf.close()





