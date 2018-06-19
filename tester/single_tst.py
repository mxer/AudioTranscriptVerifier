# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import time

import os

from tester.lm import lmgen
from adutil import create_fileids
from adutil import create_transcripts
import make_local_pdict as ml
import constants as cs


def run(root_dir, wav_files, language):
    bindir = "bin"
    lmname = os.path.join("tester","etc","test.lm")
    transfile = os.path.join("tester", "etc", "hindi_model_test.transcription")
    trfile = os.path.join("tester", "etc", "test.transcription")
    super_prompts_file = os.path.join("tester","etc","hindi_model_test_prompt.txt")

    infile = os.path.join("tester","etc", "hindi_model_test_prompt.txt")

    FILE_SPLIT = 1

    test_fileid = os.path.join("tester", "etc", "hindi_model_adapt_test.fileids")
    mfc_fileids_file = os.path.join("tester", "etc", "hindi_model_adapt_mfc.fileids")

    wavdir = root_dir
    mfcdir = root_dir
    metadata = "metadata"

    org_model = os.path.join("models","en-us")
    adapt_model = os.path.join("models","en-us-adapt")

    test_dict = "revasr.dic"

    # language_model = "..\\reverie.lm"
    dictionary = test_dict
    hypfile = os.path.join("tester", "result","hindi_adapt.hyp.txt")
    cepdir = wavdir

    discount = 0.3

    wavdirs_and_files = wav_files


    # create train_audio and train_mfc directories
    dirlist = []
    #mfdirlist = []
    for lst in wavdirs_and_files:
        print(lst[0])
        dirlist.append(lst[0])

    print(dirlist)

    # create fileids
    create_fileids(wavdir,dirlist,test_fileid,mfc_fileids_file)

    audiodir = wavdir

    transdir = wavdir
    scriptlist = []

    for lst in wavdirs_and_files:
        scriptlist.append(lst[0] + os.path.sep + lst[2])

    print(scriptlist)

    dirlist = []
    for lst in wavdirs_and_files:
        dirlist.append(os.path.join(lst[0] + os.path.sep + "train_audio"))

    print(dirlist)

    create_transcripts(transfile,super_prompts_file,trfile,scriptlist,dirlist,wavdir)

    ml.create_dictionary(super_prompts_file, test_dict, language)

    # create Language Model
    #LM configuration
    print("LM creation")
    lmgen(infile,lmname)

    language_model = lmname

    print("calling pocketsphinx_batch")
    pocketsphinx_batch_cmd = "pocketsphinx_batch" + " -adcin yes" + \
                             " -cepext" + " " + ".raw" + \
                             " -ctl" + " " + test_fileid + " -lm" + " " + language_model +\
                             " -dict" + " " + dictionary + " -hmm" + " " + adapt_model + \
                             " -cmn" + " " + "current" + " -hyp" + " " + hypfile
    call(pocketsphinx_batch_cmd, shell=True)

    time.sleep(2)

    callcmd = "perl "+os.path.join(bindir,"word_align.pl") + " " + trfile + " " + hypfile
    print(callcmd)
    out_ = '_'.join(wavdirs_and_files[0][0].split(os.path.sep))
    out_file = os.path.join("tester","result",out_+"_test_adapt.txt")
    cmdcall = callcmd + " > "+ out_file
    print(cmdcall)
    call(cmdcall, shell=True)

    return out_file
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
