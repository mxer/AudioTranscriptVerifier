from subprocess import call
import sys
import os
import codecs
import time
import unicodedata2 as uc
import re


def file_split(bindir,inraw_file,rawdir):
    if not os.path.exists(rawdir):
        os.makedirs(rawdir)
    print(rawdir)
    sys.stdout.flush()
    callcmd = bindir + "\\\\" + "filesplit.exe" + " " + "-i" + " " + inraw_file + " " + "-rawlogdir" + " "  + rawdir
    #print(callcmd)
    sys.stdout.flush()
    call(
            callcmd,shell=True
        )
    return
    
def create_fileids(audiodir,dirlist,train_fileid,mfc_fileids_file):
    f = open(train_fileid,"w",encoding="utf-8")
    mf = open(mfc_fileids_file,"w",encoding="utf-8")
    filecounter = 0
    global_counter = 0
    for dir in dirlist:
        print(dir)
        filecounter = 0
        for root,dirs,files in os.walk(audiodir + "\\\\" + dir + "\\\\train_audio"):
            for file in files:
                if file.endswith('.raw'):
                    print(file)
                    f.write("%s\\\\%08d\n"%(dir + "\\\\train_audio",filecounter))
                    mfdir = audiodir + "\\\\" + dir + "\\\\train_mfc"
                    if not os.path.exists(mfdir):
                        os.makedirs(mfdir)
                    mf.write("%s\\\\%08d\n"%(audiodir+"\\"+dir + "\\\\train_mfc",filecounter))            
                    filecounter += 1
                    global_counter += 1
    f.close()
    mf.close()
    print("the number of raw files are : %d"%(global_counter))
    
    return
    
def create_transcripts(transfile,super_prompts_file,trfile,scriptlist,dirlist,transdir):
    f = open(transfile,"w",encoding="utf-8")
    sf = open(super_prompts_file,"w",encoding="utf-8")
    tf = open(trfile,"w",encoding="utf-8")
    audiodir = transdir
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
                if line=="\n":
                    continue
                linewords = line.strip().lower().split()
                for word in linewords:
                    if uc.script(word[0]) not in ['Devanagari','Lain']:
                        print(line)
                line = ' '.join(linewords)
                f.write("<s> %s </s> (%s\\\\%08d)\n" % (line,filepath,fcounter))
                tf.write("<s> %s </s> (%s\\\\%08d)\n" % (line,fpath,fcounter))
                sf.write("%s\n" % (line))
                fcounter += 1
        index += 1
    f.close()
    sf.close()        
    tf.close()
    
def read_words(words_file):
    return [word for line in open(words_file, 'r',encoding="utf-8") for word in line.split()]

def merge_dict(dictlist,output_dict):
    dict_dbase = {}
    for dictfile in dictlist:
        df = open(dictfile,"r",encoding="utf-8")
        for line in df:
            word,pron = line.rstrip("\n").rstrip("\r").replace("\t"," ",1).split(" ",1)
            if word not in dict_dbase:
                dict_dbase[word] = []
            if pron not in dict_dbase[word]:
                dict_dbase[word].append(pron)
        df.close()
    
    of = open(output_dict,"w",encoding = "utf-8")
    for key in dict_dbase:
        value = dict_dbase[key]
        for i in range(0,len(value)):
            if i:
                of.write("%s(%d)\t%s\n"%(key,i+1,value[i]))
            else:
                of.write("%s\t%s\n"%(key,value[i]))
    of.close()
    return
        
def create_dictionary(seed_dict,super_prompts_file,dictutil,phonefile,appdic):
    # create a database of the dictionary
    outfile = "temp_hindi.dic"
    vocabfile = 'vocab.txt'
    unique_word_list = sorted(set(read_words(super_prompts_file)))
    f = open(vocabfile,"w",encoding="utf-8")
    unk_hindi_vocab = "unk_hindi.txt"
    unk_english_vocab = "unk_english.txt"    
    uhwf = open(unk_hindi_vocab,"w",encoding="utf-8")
    uewf = open(unk_english_vocab,"w",encoding="utf-8")
    
        
    gdbase = {}
    ldbase = {}
    
    sdf = open(seed_dict,"r",encoding="utf-8")
    
    for line in sdf:
        word,pron = line.replace("\n","").replace("\r","").replace("\t"," ",1).split(" ",1)
        word = re.sub(r'\([^)]*\)', '', word)
        value = []
        if word not in gdbase:
            gdbase[word] = []
            gdbase[word].append(pron)
#            print(word)
#            print(gdbase[word])
        else:
#            print(pron)
            if pron is not None:
#                print(gdbase[word])
                if gdbase[word] is not None and pron not in gdbase[word]:
#                    print(gdbase[word])
#                    print(pron)                
                    gdbase[word].append(pron)
    sdf.close()
    unkhin = 0
    unkeng = 0
#    print(gdbase)
#    gdf = open("gdbase.txt","w",encoding="utf-8")
    for word in unique_word_list:
        f.write("%s\n"%(word))
        if word in gdbase:
#            gdf.write(word+"\n")
            ldbase[word] = gdbase[word]
#            if (gdbase[word] is not None and len(gdbase[word]) > 1):
#                print(ldbase[word])
        else:
            if uc.script(word[0]) == 'Devanagari':
                unkhin = 1
                uhwf.write(word)
                uhwf.write("\n")
            elif uc.script(word[0]) == 'Latin':
                unkeng = 1
                uewf.write(word)
                uewf.write("\n")
            else:
                 print(word)
                 print("Script Not supported\n")
    

#    gdf.close()            
    f.close()
    uhwf.close()
    uewf.close()
#    ldbase = sorted(ldbase)
    af = open(appdic,"w",encoding="utf-8")
#    print(ldbase)
    keylist = [key for key in ldbase]
    keylist = sorted(keylist)
    for key in keylist:
        value = ldbase[key]
        if value is not None:
            for i in range(0,len(value)):
                if i > 0:
                    af.write("%s(%d)\t%s\n"%(key,i+1,value[i]))
                else:
                    af.write("%s\t%s\n"%(key,value[i]))
    af.close()
        
    if (unkhin == 1):
        callstr = dictutil + " " + phonefile + " " + unk_hindi_vocab + " " + outfile
        print(callstr)
        call(callstr,shell=True)
#        print(appdic)
#        print(outfile)
        af = open(appdic,"rb+")
        af.seek(-1,2)
        af.truncate()
        af.close()
        time.sleep(2)
        af = open(appdic,"a",encoding="utf-8")
        s = open(outfile, mode='r', encoding='utf-8-sig').read()
        open(outfile, mode='w', encoding='utf-8').write(s)
    if unkhin == 1:
        hf = open(outfile,"r",encoding="utf-8")
        for line in hf:
#            print(line)
            line = line.replace(" ","",1)
            af.write(line)
        hf.close()
    
    if (unkeng == 1):
        print("Unknown english words found\n")
        ef = open(unk_english_vocab,"r",encoding="utf-8")
        for line in ef:
#            print(line)
            af.write(line)
        ef.close()
    time.sleep(2)
    af.close()
    
    return