# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
import codecs
import io
import os
import time
from subprocess import call
import sys
sys.path.append("/usr/local/libexec/sphinxtrain/")
import constants as cs
import make_local_pdict as ml
from adutil import create_fileids
from adutil import create_transcripts

t_audio = "train_audio"
t_mfc = "train_mfc"


def copy_rename(wf, root_audio_path, root, rawfile, txtfile, i):
    with io.open(os.path.join(root, txtfile), "r", encoding="utf-8") as fr:
        for line in fr:
            print(line)
            wf.write(line.strip() + "\n")

    old_raw_file = os.path.join(root_audio_path, t_audio, rawfile)
    new_raw_file = os.path.join(root_audio_path, t_audio, "%08d"%(i)+".raw")

    if not os.path.exists(new_raw_file):
        os.rename(old_raw_file, new_raw_file)


def run(root_dir, wav_files):
    bindir = "bin"
    transfile = os.path.join( "adapter","etc","hindi_model_train.transcription")
    trfile = os.path.join("adapter","etc","train.transcription")
    super_prompts_file = os.path.join("adapter","etc","hindi_model_train_prompt.txt")

    train_fileid = os.path.join("adapter","etc","hindi_model_adapt.fileids")
    mfc_fileids_file = os.path.join("adapter","etc","hindi_model_adapt_mfc.fileids")

    wavdir = root_dir
    mfcdir = root_dir
    metadata = os.path.join("adapter","metadata")

    org_model = os.path.join("models","en-us")
    adapt_model = os.path.join("models","en-us-adapt")

    train_dict = "train.dic"
    language_model = "reverie.lm"
    dictionary = train_dict
    hypfile = os.path.join("adapter","result","hindi_adapt.hyp.txt")
    cepdir = wavdir

    wavdirs_and_files = wav_files

    # create train_audio and train_mfc directories
    dirlist = []

    for lst in wavdirs_and_files:
        print(lst[0])
        dirlist.append(lst[0])
    i=0

    for dir_ in dirlist:
        root_audio_path = wavdir+ dir_
        train_audio_path = os.path.join(root_audio_path, t_audio)
        if not os.path.exists(train_audio_path):
            os.makedirs(train_audio_path)
        wf = io.open(os.path.join(root_audio_path, os.path.basename(dir_)+".txt"), "w", encoding="utf-8")

        filecounter = 0
        for root, dirs, files in os.walk(root_audio_path):
            if root.endswith(t_audio) or root.endswith(t_mfc):
                continue
            for file in files:
                if file.endswith('.wav'):
                    s = file.split(".wav")
                    print(os.path.join(root, t_audio, s[0] + ".raw"))
                    src_file = os.path.join(root,file)
                    dest_file = os.path.join(root , t_audio , s[0] + ".raw")

                    callcmd = ['sox', src_file, '-b', '16', '-r', '16k', '-c', '1', '-e', 'signed', '-t', 'raw',
                               dest_file]
                    call(callcmd)
                    copy_rename(wf, root_audio_path, root, s[0]+".raw", s[0]+".txt", filecounter)
                    filecounter += 1
        wf.close()

    # Check whether transcripts file lines are equal to no of raw files
    for wav_file in wavdirs_and_files:
        DIR = wavdir+wav_file[0]
        train_audio_path = os.path.join(DIR, t_audio)
        transcriptscnt=0
        rawfilescnt=0
        for name in os.listdir(train_audio_path):
            if os.path.isfile(os.path.join(train_audio_path, name)):
                rawfilescnt = rawfilescnt+1

        with codecs.open(os.path.join(DIR,wav_file[2]),"r",encoding="utf-8") as fr:
            for f in fr:
                transcriptscnt = transcriptscnt+1

        if transcriptscnt != rawfilescnt:
            print("Mismatch in Transcripts and rawfiles count")
            print("Rawfiles_Count= "+str(rawfilescnt))
            print("Transcripts_Count= " + str(transcriptscnt))
            exit(1)

        print("Rawfiles_Count= "+str(rawfilescnt))
        print("Transcripts_Count= " + str(transcriptscnt))

    # create fileids
    create_fileids(wavdir,dirlist,train_fileid,mfc_fileids_file)

    audiodir = wavdir
    transdir = wavdir
    scriptlist = []

    for lst in wavdirs_and_files:
        scriptlist.append(os.path.join(lst[0], lst[2]))
    print(scriptlist)

    dirlist = []
    for lst in wavdirs_and_files:
        dirlist.append(os.path.join(lst[0], t_audio))
    print(dirlist)

    create_transcripts(transfile,super_prompts_file,trfile,scriptlist,dirlist,wavdir)
    ml.create_dictionary(super_prompts_file, train_dict, cs.Kannada)

    dirlist = []
    for lst in wavdirs_and_files:
        print(lst[0])
        dirlist.append(lst[0])

    sphinx_fe_cmd = "sphinx_fe -argfile" + " " + org_model + os.path.sep + "feat.params" + \
                    " -samprate 16000" + " -c" + " " + train_fileid + \
                    " -ei raw -eo mfc -mswav no"
    call(sphinx_fe_cmd, shell=True)

    for di in dirlist:
        dirname = wavdir + os.path.sep + di

        print(dirname)
        srcdir = os.path.join(dirname, t_audio)

        print(srcdir)
        dstdir = os.path.join(dirname, t_mfc)

        callstr = "mkdir " + dstdir
        call(callstr,shell=True)

        callstr = "mv " + srcdir + os.path.sep + "*.mfc " + dstdir
        call(callstr,shell=True)
    time.sleep(2)

    mdef_cmd = "pocketsphinx_mdef_convert" + " -text" + " " + org_model + os.path.sep + "mdef"\
               + " " + org_model + os.path.sep + "mdef.txt"
    call(mdef_cmd, shell=True)
    time.sleep(2)


    print("calling bw")
    bw_cmd = "bw" + " " + "-hmmdir" + " " + org_model + \
                    " -moddeffn" + " " + org_model + os.path.sep + "mdef.txt" + \
                    " -ts2cbfn .ptm. -feat 1s_c_d_dd -svspec 0-12/13-25/26-38" + \
                    " -cmn current -agc none -dictfn" + " " + train_dict + \
                    " -ctlfn" + " " + mfc_fileids_file + " -lsnfn" + " " + transfile + " -accumdir" + " " + metadata
    call(bw_cmd, shell=True)
    time.sleep(2)

    print("calling mllr_solve")

    cmd_mllr = "mllr_solve" + " " + "-meanfn" + " " \
               + org_model + os.path.sep + "means" + " -varfn" + " " + org_model + os.path.sep + "variances" + \
               " -outmllrfn" + " " + metadata + os.path.sep + "mllr_matrix" + " -accumdir" + " " + metadata

    call(cmd_mllr,shell=True)
    time.sleep(2)

    print("copying models")
    callstr = "mkdir " + adapt_model
    print(callstr)
    call(callstr,shell=True)

    cp_cmd = "cp " + os.path.join('models', 'en-us', '*.*') + " " + os.path.join('models', 'en-us-adapt')
    call(cp_cmd, shell=True)

    time.sleep(2)
    print("calling map_adapt")
    map_adapt_cmd = "map_adapt" + " " + "-moddeffn" + " " + org_model + os.path.sep + "mdef.txt"\
                    + " -ts2cbfn .ptm. " + " -meanfn" + " " + org_model + os.path.sep + "means" + \
                    " -varfn" + " " + org_model + os.path.sep + "variances" + \
                    " -mixwfn" + " " + org_model + os.path.sep + "mixture_weights" + \
                    " -tmatfn" + " " + org_model + os.path.sep + "transition_matrices" + \
                    " -accumdir" + " " + metadata + " -mapmeanfn" + " " + adapt_model + os.path.sep + "means" + \
                    " -mapvarfn" + " " + adapt_model + os.path.sep + "variances" + \
                    " -mapmixwfn" + " " + adapt_model + os.path.sep + "mixture_weights" + \
                    " -maptmatfn" + " " + adapt_model + os.path.sep + "transition_matrices"
    call(map_adapt_cmd, shell=True)
    time.sleep(2)

    print("calling sendump")
    sendump_cmd = "mk_s2sendump" + " " + "-pocketsphinx yes" + \
                  " -moddeffn" + " " + adapt_model + os.path.sep + "mdef.txt" + " -mixwfn" + " " + adapt_model + \
                  os.path.sep + "mixture_weights" + " -sendumpfn" + " " + adapt_model + os.path.sep + "sendump"
    call(sendump_cmd, shell=True)
    time.sleep(2)

    '''
    print("calling pocketsphinx_batch")    
    call(
            "bin\\pocketsphinx_batch" + \
            " -adcin yes" + \
            " -cepdir" + " " + cepdir + \
            " -cepext" + " " + ".raw" + \
            " -ctl" + " " + train_fileid + \
            " -lm" + " " + language_model + \
            " -dict" + " " + dictionary + \
            " -hmm" + " " + adapt_model + \
            " -hyp" + " " + hypfile
            #" -mllr" + " " + metadata + "\\mllr_matrix" 
      )
    
        
        
    time.sleep(2)    
        
    callcmd = "perl bin\\word_align.pl" + " " + trfile + " " + hypfile 
    print(callcmd)
    cmdcall = callcmd + " > result\\res_adapt.txt"
    print(cmdcall)
    call(
            cmdcall, shell=True
      )
    '''
    '''    
    print("calling pocketsphinx_batch")    
    call(
            "bin\\pocketsphinx_batch" + \
            " -adcin yes" + \
            " -cepdir" + " " + cepdir + \
            " -cepext" + " " + ".raw" + \
            " -ctl" + " " + train_fileid + \
            " -lm" + " " + language_model + \
            " -dict" + " " + dictionary + \
            " -hmm" + " " + org_model + \
            " -hyp" + " " + hypfile
            #" -mllr" + " " + metadata + "\\mllr_matrix" 
      )
    
        
        
    time.sleep(2)    
        
    c allcmd = "perl bin\\word_align.pl" + " " + trfile + " " + hypfile 
    print(callcmd)
    cmdcall = callcmd + " > result\\res.txt"
    print(cmdcall)
    call(
            cmdcall, shell=True
      )
    '''
