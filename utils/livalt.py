from subprocess import call
import sys
import os
import requests
import json
import shutil
import io
import time

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
#        						["\\train\\others\\sonu_sharma","sankalp_ki_shakti.raw","sankalp_ki_shakti.txt"],
#        						["\\train\\others\\edu\\adyatan","adyatan.raw","adyatan.txt"],
        						["\\train\\others\\hindi_kavita\\manoj_bajpai\\rashmirathi","rashmirathi.raw","rashmirathi.txt"],
                    ]
#check silence file exists
if os.path.isfile(silence) == False:
	print("Silence file not found")
	exit(1)

fsplit_util = "J:\\asr\\bin\\filesplit.exe"
	
# first split the files
for entry in wavdirs_and_files:
	mp3fn = wavdir + entry[0] + "\\" + entry[1].replace(".raw",".mp3")
	rawfn = wavdir + entry[0] + "\\" + entry[1]
	rawdir = wavdir + entry[0] + "\\" + "train_audio"
	if not os.path.exists(rawdir):
		os.makedirs(rawdir)
	print(rawdir)
	callcmd = "sox %s -r 16k -b 16 -e signed -c 1 %s"%(mp3fn,rawfn)
	print(callcmd)
	call(callcmd,shell=True)
	callcmd = fsplit_util + " " + "-i" + " " + rawfn + " " + "-rawlogdir" + " "  + rawdir
	#print(callcmd)
	sys.stdout.flush()
	call(
			callcmd,shell=True
		)

	#count the number of files in train_audio
	fcounter = 0
	transcript_file = wavdir + "\\" + entry[0] + "\\" + entry[2]
	tf = io.open(transcript_file,"w",encoding="utf-8")

	for dirpath, dirnames, filenames in os.walk(rawdir):
		for filename in [f for f in filenames if f.endswith(".raw")]:
			mp3dir = wavdir + entry[0] + "\\train_mp3"
			if not os.path.exists(mp3dir):
				os.makedirs(mp3dir)
			fmp3 = wavdir + entry[0] + "\\train_mp3\\" + filename.replace(".raw",".mp3")
			print(filename)
			print(fmp3)
			rawfn = wavdir + entry[0] + "\\train_audio\\" + filename
			callcmd = "sox -r 16k -b 16 -e signed -c 1 %s %s"%(rawfn,fmp3)
			print(callcmd)
			call(callcmd,shell=True)
			files = {'audio_file' : open(fmp3,'rb')}
			result = requests.post(url, headers = headers, data = data, files = files)
			res = str(result).split()
			resp = res[1].replace("[","").replace("]","").replace(">","")
			print(resp)
			if resp[0] == "2":
				json_data = json.loads(result.text)
				trlen = len(json_data["transcriptions"])
				
			while resp[0] != "2" or trlen == 0:
				time.sleep(1)
				files = {'audio_file' : open(fmp3,'rb')}
				result = requests.post(url, headers = headers, data = data, files = files)
				res = str(result).split()
				resp = res[1].replace("[","").replace("]","").replace(">","")
				if resp[0] == "2":
					json_data = json.loads(result.text)
					trlen = len(json_data["transcriptions"])
				print(resp)
			trans = json_data["transcriptions"][0]
			print(trans)
			restext = trans["utf_text"]
			tf.write(restext + "\n")	
			fcounter += 1
			time.sleep(1)
	