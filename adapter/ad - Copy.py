# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:00:39 2016

@author: Pankaj
"""
from subprocess import call
import os
import time
import codecs
from adapter.adutil import file_split
from adapter.adutil import create_fileids
from adapter.adutil import create_transcripts
import make_local_pdict as ml
import constants as cs
import io
from shutil import copyfile

class Ad:

    bindir = "bin"
    # lmname = "E:\\AudioTranscriptVerifier\\adapter\\etc\\adaptation.lm"
    transfile = "adapter\\etc\\hindi_model_train.transcription"
    trfile = "adapter\\etc\\train.transcription"
    super_prompts_file = "adapter\\etc\\hindi_model_train_prompt.txt"
    # phonefile = "..\\bin\\phonemap.txt"
    # hindi_phone_file = "..\\bin\\hindiphone.txt"
    # infile = "etc\\hindi_model_train_prompt.txt"
    # vocabfile = "etc\\hindi_model_train_vocab.txt"
    # outfile = "etc\\hindi_model_train_adaptation.dic"
    # dictutil = "E:\\AudioTranscriptVerifier\\bin\\progen.exe"

    train_fileid = "adapter\\etc\\hindi_model_adapt.fileids"
    mfc_fileids_file = "adapter\\etc\\hindi_model_adapt_mfc.fileids"

    wavdir = "C:\\Users\\Reverie-IT\\Desktop\\projects"
    mfcdir = "C:\\Users\\Reverie-IT\\Desktop\\projects"
    metadata = "metadata"

    rootdir = "C:\\Users\\Reverie-IT\\Desktop\\projects\\AudioTranscriptVerifier"

    org_model = "models\\en-us"
    adapt_model = "models\\en-us-adapt"

    train_dict = "train.dic"
    language_model = "reverie.lm"
    dictionary = train_dict
    hypfile = "adapter\\result\\hindi_adapt.hyp.txt"
    cepdir = wavdir
    wavdirs_and_files = []
    
    def copy_rename(self, wf, root, dir, rawfile, txtfile, i):
        # print(root)
        copyfile(os.path.join(root, rawfile),
                 os.path.join(self.wavdir + "\\" + dir + "\\train_audio", rawfile))
        print(rawfile)
        with io.open(root + "\\" + txtfile, "r", encoding="utf-8") as fr:
            for line in fr:
                print(line)
                wf.write(line.strip() + "\n")

        os.rename(os.path.join(self.wavdir + "\\" + dir + "\\train_audio", rawfile),
                  os.path.join(self.wavdir + "\\" + dir + "\\train_audio\\%08d" % (i) + ".raw"))

        os.rename(os.path.join(root, rawfile),
                  os.path.join(root + "\\%08d" % (i) + "_" + rawfile))

        os.rename(os.path.join(root, txtfile),
                  os.path.join(root + "\\%08d" % (i) + "_" + txtfile))

    def __init__(self, files):
        self.wavdirs_and_files = files

    def run(self):
        # create train_audio and train_mfc directories
        dirlist = []
        filelist = []
        # mfdirlist = []
        for lst in self.wavdirs_and_files:
            print(lst[0])
            dirlist.append(lst[0])
            filelist.append(lst[2])

        i = 0

        for dir in dirlist:
            if not os.path.exists(self.wavdir + "\\" + dir + "\\train_audio"):
                os.makedirs(self.wavdir + "\\" + dir + "\\train_audio")
            wf = io.open(self.wavdir + "\\" + dir + "\\" + os.path.basename(dir) + ".txt", "w", encoding="utf-8")
            # print(dir)
            filecounter = 0
            for root, dirs, files in os.walk(self.wavdir + "\\" + dir):
                if root.endswith("train_audio") or root.endswith("train_mfc"):
                    continue
                for file in files:
                    if file.endswith('.wav'):
                        # print(file)
                        s = file.split(".wav")
                        callcmd = "sox " + root + "\\" + file + " " + root + "\\" + s[0] + ".raw"
                        call(callcmd, shell=True)
                        self.copy_rename(wf, root, dir, file, s[0] + ".txt", i)
                        i = i + 1
            wf.close()

        # Check whether transcripts file lines are equal to no of raw files
        for i,dir in enumerate(dirlist):
            DIR = self.wavdir + "\\" + dir
            print(DIR)
            transcriptscnt = 0
            rawfilescnt = 0
            for name in os.listdir(DIR + "\\" + "train_audio"):
                if os.path.isfile(os.path.join(DIR + "\\" + "train_audio", name)):
                    rawfilescnt = rawfilescnt + 1

            transcriptscnt = len(codecs.open(DIR + "\\" + filelist[i], "r", encoding="utf-8").readlines())

            if transcriptscnt != rawfilescnt:
                print("Mismatch in Transcripts and rawfiles count")
                print("Rawfiles_Count= " + str(rawfilescnt))
                print("Transcripts_Count= " + str(transcriptscnt))
                exit(1)
            print("Rawfiles_Count= " + str(rawfilescnt))
            print("Transcripts_Count= " + str(transcriptscnt))

        # create fileids

        create_fileids(self.wavdir, dirlist, self.train_fileid, self.mfc_fileids_file)

        audiodir = transdir = self.wavdir

        scriptlist = []

        for lst in self.wavdirs_and_files:
            scriptlist.append(lst[0] + "\\" + lst[2])

        print(scriptlist)

        dirlist = []
        for lst in self.wavdirs_and_files:
            dirlist.append(lst[0] + "\\train_audio")

        # print(dirlist)

        create_transcripts(self.transfile, self.super_prompts_file, self.trfile, scriptlist, dirlist, self.wavdir)

        ml.createDictionary(self.super_prompts_file, self.train_dict, cs.Kannada)
        # create_dictionary("..\\eng.dic",super_prompts_file,dictutil,phonefile,train_dict)

        dirlist = []
        for lst in self.wavdirs_and_files:
            print(lst[0])
            dirlist.append(lst[0])

        call("..\\bin\\sphinx_fe -argfile" + " " + self.org_model + "\\feat.params" + \
             " -samprate 16000" + " -c" + " " + self.train_fileid + \
             " -di" + " " + self.wavdir + \
             " -do" + " " + self.mfcdir + \
             " -ei raw -eo mfc -mswav no", shell=True
             )

        for di in dirlist:
            dirname = self.wavdir + "\\" + di
            print(dirname)
            srcdir = dirname + "\\train_audio"
            print(srcdir)
            dstdir = dirname + "\\train_mfc"
            callstr = "mkdir" + " " + dstdir
            #    print(callstr)
            call(callstr, shell=True)
            callstr = "move" + " " + srcdir + "\\*.mfc" + " " + dstdir
            #    print(callstr)
            call(callstr, shell=True)

        time.sleep(2)

        call(
            "..\\bin\\pocketsphinx_mdef_convert" + " -text" + " " + self.org_model + "\\mdef" + " " + self.org_model + "\\mdef.txt",
            shell=True)

        time.sleep(2)

        print("calling bw")
        call(
            "bin\\bw" + " " + "-hmmdir" + " " + self.org_model + \
            " -moddeffn" + " " + self.org_model + "\\mdef.txt" + \
            " -ts2cbfn .ptm. -feat 1s_c_d_dd -svspec 0-12/13-25/26-38" + \
            " -cmn current -agc none -dictfn" + " " + self.train_dict + \
            " -ctlfn" + " " + self.mfc_fileids_file + \
            " -lsnfn" + " " + self.transfile + \
            " -accumdir" + " " + self.metadata
        )
        time.sleep(2)
        print("calling mmlr_solve")
        call(
            "bin\\mllr_solve" + " " + "-meanfn" + " " + self.org_model + "\\means" + \
            " -varfn" + " " + self.org_model + "\\variances" + \
            " -outmllrfn" + " " + self.metadata + "\\mllr_matrix" + \
            " -accumdir" + " " + self.metadata, shell=True
        )

        time.sleep(2)

        print("copying models")
        callstr = "md" + " " + self.adapt_model
        print(callstr)
        call(callstr, shell=True)
        call("copy models\\en-us\\*.* models\\en-us-adapt", shell=True)

        time.sleep(2)
        print("calling map_adapt")
        call(
            "bin\\map_adapt" + " " + "-moddeffn" + " " + self.org_model + "\\mdef.txt" + \
            " -ts2cbfn .ptm. " + \
            " -meanfn" + " " + self.org_model + "\\means" + \
            " -varfn" + " " + self.org_model + "\\variances" + \
            " -mixwfn" + " " + self.org_model + "\\mixture_weights" + \
            " -tmatfn" + " " + self.org_model + "\\transition_matrices" + \
            " -accumdir" + " " + self.metadata + \
            " -mapmeanfn" + " " + self.adapt_model + "\\means" + \
            " -mapvarfn" + " " + self.adapt_model + "\\variances" + \
            " -mapmixwfn" + " " + self.adapt_model + "\\mixture_weights" + \
            " -maptmatfn" + " " + self.adapt_model + "\\transition_matrices"
        )

        time.sleep(2)
        print("calling sendump")

        call(
            "bin\\mk_s2sendump" + " " + "-pocketsphinx yes" + \
            " -moddeffn" + " " + self.adapt_model + "\\mdef.txt" + \
            " -mixwfn" + " " + self.adapt_model + "\\mixture_weights" + \
            " -sendumpfn" + " " + self.adapt_model + "\\sendump"
        )

        time.sleep(2)

        # lmgen(infile,lmname)

        '''
        print("calling pocketsphinx_batch")    
        call(
                "..\\bin\\pocketsphinx_batch" + \
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

        callcmd = "perl ..\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
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
                "..\\bin\\pocketsphinx_batch" + \
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

        c allcmd = "perl ..\\bin\\word_align.pl" + " " + trfile + " " + hypfile 
        print(callcmd)
        cmdcall = callcmd + " > result\\res.txt"
        print(cmdcall)
        call(
                cmdcall, shell=True
          )
        '''