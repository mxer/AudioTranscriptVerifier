# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import time

import os

from tester.lm import lmgen
from tester.adutil import file_split
from tester.adutil import create_fileids
from tester.adutil import create_transcripts
import make_local_pdict as ml
import constants as cs
from shutil import copyfile

class singleTest:

    bindir = "..\\bin"
    lmname = "..\\tester\\\\etc\\\\test.lm"
    transfile = "etc\\hindi_model_test.transcription"
    trfile = "etc\\test.transcription"
    super_prompts_file = "etc\\hindi_model_test_prompt.txt"
    # phonefile = "..\\\\bin\\\\phonemap.txt"
    # hindi_phone_file = "..\\\\bin\\\\hindiphone.txt"
    infile = "etc\\hindi_model_test_prompt.txt"
    # lminfile = "etc\\\\lminput.txt"
    # vocabfile = "etc\\\\hindi_model_test_vocab.txt"
    # outfile = "..\\\\test.dic"
    # dictutil = "E:\\\\AudioTranscriptVerifier\\\\bin\\\\progen.exe"

    FILE_SPLIT = 1

    test_fileid = "etc\\hindi_model_adapt_test.fileids"
    mfc_fileids_file = "etc\\hindi_model_adapt_mfc.fileids"

    wavdir = "C:\\Users\\Reverie-IT\\Desktop\\projects"
    mfcdir = "C:\\Users\\Reverie-IT\\Desktop\\projects"
    metadata = "metadata"

    rootdir = "C:\\Users\\Reverie-IT\\Desktop\\projects\\AudioTranscriptVerifier"

    org_model = rootdir + "\\\\" + "models\\\\en-us"
    adapt_model = rootdir + "\\\\" + "models\\\\en-us-adapt"

    test_dict = rootdir + "\\\\revasr.dic"

    # language_model = "..\\reverie.lm"
    dictionary = test_dict
    hypfile = "result\\\\hindi_adapt.hyp.txt"
    cepdir = wavdir

    discount = 0.3

    wavdirs_and_files = []
                                
    def __init__(self, files):
        self.wavdirs_and_files = files
        
    def run(self):
        # create train_audio and train_mfc directories
        dirlist = []
        # mfdirlist = []
        for lst in self.wavdirs_and_files:
            print(lst[0])
            dirlist.append(lst[0])

        # for lst in dirlist:
        #    mfdirlist.append(lst + "\\\\train_mfc")

        print(dirlist)

        # create fileids

        create_fileids(self.wavdir, dirlist, self.test_fileid, self.mfc_fileids_file)

        audiodir = transdir = self.wavdir

        transdir = self.wavdir
        scriptlist = []

        for lst in self.wavdirs_and_files:
            scriptlist.append(lst[0] + "\\\\" + lst[2])

        print(scriptlist)

        dirlist = []
        for lst in self.wavdirs_and_files:
            dirlist.append(lst[0] + "\\\\train_audio")

        print(dirlist)

        create_transcripts(self.transfile, self.super_prompts_file, self.trfile, scriptlist, dirlist, self.wavdir)

        ml.createDictionary(self.super_prompts_file, self.test_dict, cs.Kannada)

        # create_dictionary("E:\\\\AudioTranscriptVerifier\\\\eng.dic",super_prompts_file,dictutil,phonefile,test_dict)

        # create Language Model
        # LM configuration
        print("LM creation")
        lmgen(self.infile,self.lmname)
        # lmname = "E:\\New_Corpus\\language_model\\reverie.lm"
        language_model = self.lmname

        print("calling pocketsphinx_batch")
        call(
            "..\\bin\\pocketsphinx_batch" + \
            " -adcin yes" + \
            " -cepdir" + " " + self.cepdir + \
            " -cepext" + " " + ".raw" + \
            " -ctl" + " " + self.test_fileid + \
            " -lm" + " " + language_model + \
            " -dict" + " " + self.dictionary + \
            " -hmm" + " " + self.adapt_model + \
            " -cmn" + " " + "current" + \
            " -hyp" + " " + self.hypfile
            # " -mllr" + " " + metadata + "\\mllr_matrix"
        )

        time.sleep(2)

        callcmd = "perl ..\\bin\\word_align.pl" + " " + self.trfile + " " + self.hypfile
        print(callcmd)
        cmdcall = callcmd + " > result\\\\test_adapt.txt"
        print(cmdcall)
        call(
            cmdcall, shell=True
        )

        '''    
        print("calling pocketsphinx_batch")    
        call(
                "..\\bin\\pocketsphinx_batch" + \
                " -adcin yes" + \
                " -cepdir" + " " + cepdir + \
                " -cepext" + " " + ".raw" + \
                " -ctl" + " " + test_fileid + \
                " -lm" + " " + language_model + \
                " -dict" + " " + dictionary + \
                " -hmm" + " " + org_model + \
                " -hyp" + " " + hypfile
                #" -mllr" + " " + metadata + "\\mllr_matrix" 
          )



        time.sleep(2)    

        callcmd = "perl ..\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
        print(callcmd)
        cmdcall = callcmd + " > result\\\\test.txt"
        print(cmdcall)
        call(
                cmdcall, shell=True
          )

        '''