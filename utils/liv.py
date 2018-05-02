from subprocess import call
import sys
import os
import requests
import json
import shutil
import io

wavdir = "J:\\\\New_Corpus"
bindir = "J:\\\\asr\\\\bin"

wavdir = "J:\\\\New_Corpus"
mfcdir = "J:\\\\New_Corpus"
metadata = "metadata"

rootdir = "J:\\\\asr"

silence = "J:\\asr\\utils\\silence.raw"

headers = {'Authorization' : 'Token a6b3157ba0924846cb9466c776a8ee3f1311005d'}
data = {'user' : '30' ,'language' : 'HI'}
url = 'https://dev.liv.ai/liv_transcription_api/recordings/'


wavdirs_and_files = [
        						["\\train\\others\\anurag_sharma\\agyeya","agyeya.raw","agyeya.txt"],
                    ]
#check silence file exists
if os.path.isfile(silence) == False:
	print("Silence file not found")
	exit(1)

# first split the files
for entry in wavdirs_and_files:
	mp3fn = wavdir + entry[0] + "\\" + entry[1].replace(".raw",".mp3")
	print(mp3fn)
	mp3split = '"C:\Program Files (x86)\mp3splt\mp3splt.exe"'
	mp3dir = wavdir + entry[0] + "\\train_mp3"
	callcmd =  mp3split + " -f -t 0.5 -d" + " " + mp3dir + " " + mp3fn + " " +  " -o @n"
	print(callcmd)
	call(callcmd,shell=True)
	mp3list = []
	for root,dirs,files in os.walk(mp3dir):
		for file in files:
			if file.endswith(".mp3"):
				mp3list.append(root + "\\" + file)
		mp3list = sorted(mp3list)
	counter = 0
	train_audio = root.replace("\\train_mp3","\\train_audio")
	if not os.path.exists(train_audio):
		os.makedirs(train_audio)
	transcript_file = wavdir + entry[0] + "\\" + entry[2]
	dstaudfile = wavdir + entry[0] + "\\" + entry[1]
	print(dstaudfile)
	if os.path.isfile(dstaudfile) == True:
		df = io.open(dstaudfile,"wb")
	else:
		df = io.open(dstaudfile,"ab")

	shutil.copyfileobj(open(silence,"rb"),df)

	tf = io.open(transcript_file,"w",encoding="utf-8")
	for file in mp3list:
		rawfn = train_audio + "\\" + "%08d.raw"%(counter)
		files = {'audio_file' : open(file,'rb')}
		res = requests.post(url, headers = headers, data = data, files = files)
		json_data = json.loads(res.text)
		trans = json_data["transcriptions"][0]
		restext = trans["utf_text"]
		print(restext)
		tf.write(restext + "\n")
		callcmd = "sox %s -r 16k -b 16 -e signed -c 1 %s"%(file,rawfn)
		print(callcmd)
		call(callcmd,shell=True)
		shutil.copyfileobj(open(rawfn,"rb"),df)
		shutil.copyfileobj(open(silence,"rb"),df)		
		counter += 1
	tf.close()
	df.close()
