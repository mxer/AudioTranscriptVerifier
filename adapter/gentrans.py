import sys
import codecs


def read_words(words_file):
    return [word for line in open(words_file, 'r',encoding="utf-8") for word in line.split()]

transdir = "J:\\\\New_Corpus"
scriptlist = 	[
					"train\\\\3553\\\\female\\\\3553_female.txt",
					"train\\\\3553\\\\male\\\\3553_male.txt",
					"train\\\\3553\\\\pankaj\\\\3553_pankaj.txt",
					"train\\\\abhishek\\\\abhishek.txt",					
#					"train\\\\sandeep_maheshwari\\\\sandeep_maheshwari_a.txt",
#					"train\\\\sandeep_maheshwari_b\\\\sandeep_maheshwari_b.txt",
                    "train\\\\accomodation\\\\pankaj\\\\accomodation_pankaj.txt",
                    "train\\\\around_town\\\\pankaj\\\\around_town_pankaj.txt",
                    "train\\\\conversations\\\\pankaj\\\\conversations_pankaj.txt",
                    "train\\\\redbus\\\\pankaj\\\\redbus_pankaj.txt",
                    "train\\\\rakhee\\\\snap\\\\pure\\\\train_rakhee_snap_pure.script.txt",
					"train\\\\smriti\\\\smriti.txt",
                    "train\\\\vivek\\\\vivek.txt",
#					"snapdeal\\\\pankaj\\\\snapdeal_pankaj.txt",
#					"snapdeal_search\\\\Part0\\\\Pankaj\\\\snapdeal_search_part0_pankaj.txt",
#					"reinforce\\\\pankaj\\\\reinforce_pankaj.txt"
				]
audiodir = "J:\\\\New_Corpus"
dirlist = 	[
				"train\\\\3553\\\\female\\\\train_audio",
				"train\\\\3553\\\\male\\\\train_audio",
				"train\\\\3553\\\\pankaj\\\\train_audio",
				"train\\\\abhishek\\\\train_audio",					
#				"train\\\\sandeep_maheshwari\\\\train_audio",
#				"train\\\\sandeep_maheshwari_b\\\\train_audio",
                "train\\\\accomodation\\\\pankaj\\\\train_audio",
				"train\\\\around_town\\\\pankaj\\\\train_audio",
				"train\\\\conversations\\\\pankaj\\\\train_audio",
				"train\\\\redbus\\\\pankaj\\\\train_audio",
                "train\\\\rakhee\\\\snap\\\\pure\\\\train_audio",
				"train\\\\smriti\\\\train_audio",
                "train\\\\vivek\\\\train_audio",
#				"snapdeal\\\\pankaj\\\\train_audio",
#				"snapdeal_search\\\\Part0\\\\Pankaj\\\\train_audio",
#				"reinforce\\\\pankaj\\\\train_audio"				
			]

transfile = "etc\\hindi_model_train.transcription"
trfile = "etc\\train.transcription"
super_prompts_file = "etc\\hindi_model_train_prompt.txt"

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





