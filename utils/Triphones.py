# -*- coding: utf-8 -*-
import io
import sys
#sys.path.append('E:/STT_Apps/src/preprocess')
import pronounce_new as pr
from random import shuffle
import Constants as cs
import IndicNormalizer as norm

uniphonelist = []
diphonelist = []
triphonelist = []
uniqueutterancelist = []

def freqsort(cntlst, phonelst, filename):
    for i in range(0, len(cntlst)):
        for j in range(i+1, len(cntlst)):
            if cntlst[i]<cntlst[j]:
                temp = cntlst[i]
                cntlst[i]=cntlst[j]
                cntlst[j]=temp

                temp = phonelst[i]
                phonelst[i] = phonelst[j]
                phonelst[j] = temp
    unifreqfile = io.open(filename, "w",encoding="utf-8")
    for i in range(0, len(cntlst)):
        unifreqfile.write(phonelst[i] + u"\t" + str(cntlst[i]) + u"\n")
    unifreqfile.close()

def addUniphoneFrequency(list):
    # unifreqfile = open("uniphones_freq.txt", "w")
    prevline = ""
    counter = 1
    list.sort()
    cntlst = []
    phonelst = []
    for line in list:
        line = line.replace("\n","")
        if prevline == line:
            counter += 1
        else:
            if prevline!="":
                cntlst.append(counter)
                phonelst.append(prevline)
                # unifreqfile.write(prevline.encode("UTF-8") + "\t" + str(counter) + "\n")
            prevline = line
            counter = 1
    # unifreqfile.close()
    freqsort(cntlst, phonelst, "uniphones_freq.txt")

def addDiphoneFrequency(list):
    # difreqfile = open("diphones_freq.txt", "w")
    prevline = ""
    counter = 1
    list.sort()
    cntlst = []
    phonelst = []
    for line in list:
        line = line.replace("\n","")
        if prevline == line:
            counter += 1
        else:
            if prevline!="":
                cntlst.append(counter)
                phonelst.append(prevline)
                # difreqfile.write(prevline.encode("UTF-8") + "\t" + str(counter) + "\n")
            prevline = line
            counter = 1
    # difreqfile.close()
    freqsort(cntlst, phonelst, "diphones_freq.txt")

def addTriphoneFrequency(list):
    # trifreqfile = open("triphones_freq.txt", "w")
    prevline = ""
    counter = 1
    list.sort()
    cntlst = []
    phonelst = []
    for line in list:
        line = line.replace("\n","")
        if prevline == line:
            counter += 1
        else:
            if prevline!="":
                cntlst.append(counter)
                phonelst.append(prevline)
                # trifreqfile.write(prevline.encode("UTF-8") + "\t" + str(counter) + "\n")
            prevline = line
            counter = 1
    # trifreqfile.close()
    freqsort(cntlst, phonelst, "triphones_freq.txt")

def findUniphones(phones, utterance, uniqueuniphonescount):
    tokens = phones.split(" ")
    i=0
    list = []

    while i < len(tokens):
        j=i
        str = ""
        while j < i+1:
            str = str+tokens[j]+" "
            j = j+1
        str = str.strip()
        list.append(str + "\n")
        i = i+1

    for line in list:
        uniphonelist.append(line)

def findDiphones(phones, utterance, uniquediphonescount):
    tokens = phones.split(" ")
    i=0
    list = []

    while i < len(tokens)-1:
        j=i
        str = ""
        while j < i+2:
            str = str+tokens[j]+" "
            j = j+1
        str = str.strip()
        list.append(str + "\n")
        i = i+1

    for line in list:
        diphonelist.append(line)

def findTriphones(phones, utterance, uniquetriphonescount):
    tokens = phones.split(" ")
    i=0
    list = []

    while i < len(tokens)-2:
        j=i
        str = ""
        while j < i+3:
            str = str+tokens[j]+" "
            j = j+1
        str = str.strip()
        list.append(str + "\n")
        i = i+1

    uniquetriphones = 0
    if 0 < len(triphonelist):
        for c in list:
            isPresent = False
            for line in triphonelist:
                if c==line:
                    isPresent = True
                    break
            if not isPresent:
                uniquetriphones = uniquetriphones+1
            if uniquetriphones == uniquetriphonescount:
                break
    # print uniquetriphones
    if uniquetriphones >= uniquetriphonescount or 0 == len(triphonelist):
        uniqueutterancelist.append(utterance)
    for line in list:
        triphonelist.append(line)

def writeUniqueUtterance():
    uniquefile = io.open("unique_utterance.txt", "w",encoding="utf-8")
    for utterance in uniqueutterancelist:
        uniquefile.write(utterance)
    uniquefile.close()

def generatePhones(filename):
    print("started");
    ff = io.open(filename, "r", encoding="utf-8")
    mappings = pr.Mappings()
    uniquetriphonescount = 1
    llist = ff.readlines()
    shuffle(list)
    for line in llist:
        list = []
        inputTokens = line.split(" ")
        str = ""
        for token in inputTokens:
            str = str + mappings.pronounce(norm.getIndicNormalized(token), cs.Hindi)+" "
        list.append("<SIL>" + " " + str + "</SIL>")

        for c in list:
            findTriphones(c, line, uniquetriphonescount)
            findDiphones(c, line, uniquetriphonescount)
            findUniphones(c, line, uniquetriphonescount)
    addTriphoneFrequency(triphonelist)
    addDiphoneFrequency(diphonelist)
    addUniphoneFrequency(uniphonelist)
    writeUniqueUtterance()

#generatePhones("J:\\New_Corpus\\text_corpus\\93165Hindi_monolingual_sampledata\\Hindi_monolingual_sampledata\\hin_politics and public administration_set2.txt")
generatePhones("J:\\transfer\\revhindi.lmscript.txt")
