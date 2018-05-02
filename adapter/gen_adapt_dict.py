from subprocess import call
import sys
import codecs

def read_words(words_file):
    return [word for line in open(words_file, 'r',encoding="utf-8") for word in line.split()]
	
	
phonefile = "..\\\\bin\\\\phonemap.txt"
hindi_phone_file = "..\\\\bin\\\\hindiphone.txt"
infile = "etc\\\\hindi_model_train_prompt.txt"
vocabfile = "etc\\\\hindi_model_train_vocab.txt"
outfile = "etc\\hindi_model_train_adaptation.dic"
dictutil = "J:\\\\asr\\\\bin\\\\progen.exe"
#first generate a vocabulary
word_list = read_words(infile)
unique_word_list = set(word_list)
f = open(vocabfile,"w",encoding="utf-8")

for word in unique_word_list:
	f.write("%s\n"%(word))

f.close()

callstr = dictutil + " " + phonefile + " " + vocabfile + " " + outfile
print(callstr)
call(
		callstr,shell=True
	)

