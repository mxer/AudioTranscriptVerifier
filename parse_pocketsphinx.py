# -*- coding: utf-8 -*-
import os
import glob
import shutil
import json
import codecs
from pydub import AudioSegment

# input_file = os.getcwd()+"/../test_adapt.txt"
# input_files_dir = sys.argv[1]
# audio_files_dir = sys.argv[2]
# audio_files_dir = "/Users/Arunjeyantvsv/Office/git_repo/data_collector/"
# transcript_file = sys.argv[3]
report_wr = open(os.getcwd()+"/report.tsv","w")


def calculate(file_):
    if '.raw' in file_:
        try:
            print (file_)
            return AudioSegment.from_raw(file_, channels=1, frame_rate=16000, sample_width=2).duration_seconds
        except Exception as e:
            print ('except', e)


def getduration(s):
    hour = 0
    minute = 0
    seconds = 0
    ss = str(s).split('.')
    if len(ss) >= 2:
        sss = int(ss[0])
        #d = time.strftime('%D:%H:%M:%S (%H Hourrs %M Minutes %S Seconds)', time.gmtime(sss))
        if sss >= 3600:
            hour = sss / 3600
            remain = sss % 3600
            if remain >= 60:
                minute = remain / 60
                seconds = remain % 60
        else:
            hour = 0
            if sss >= 60:
                minute = sss / 60
                seconds = sss % 60
            else:
                seconds = sss

    return str(hour) + ' Hours ' + str(minute) + ' Mins ' + str(seconds) + ' Secs'


def run(ps_report):
    with open(ps_report, 'r') as f:
        for line in f:
            line = line.strip()
            audio_files_dir, input_file = line.split('\t')
            print(audio_files_dir)
            out_crct = os.path.join(audio_files_dir, "correct_ones")
            out_err = os.path.join(audio_files_dir, "error_ones")
            if not os.path.exists(out_crct):
                os.makedirs(out_crct)
            if not os.path.exists(out_err):
                os.makedirs(out_err)
            crct_dur = 0.0
            error_dur = 0.0
            f_crct_dur = {}
            f_err_dur = {}

            print(input_file)

            correct_ones = {}
            error_ones = {}
            # lines = open(transcript_file, 'r', encoding="utf-8").readlines()
            c_dur = 0.0
            e_dur = 0.0

            with codecs.open(input_file, 'r', encoding='utf-8') as f:
                count = 1
                file_ = []
                lines = []
                t_file = ""

                for line in f:
                    file_.append(line.strip())
                    if count % 4 == 0:
                        check = 80.00 <= float(file_[2].split("Accuracy = ")[1].split('%')[0]) <= 100.00
                        out_f = file_[1].split("(")[1].replace(")", "")
                        # print (out_f)
                        # print (file_[2].split("Accuracy = ")[1])
                        out_f = out_f.replace("\\", "/")
                        out_f = out_f.replace("//", "/").lower()

                        filename = os.path.basename(out_f)
                        dirname = os.path.dirname(out_f)
                        dirname_1_lvlup = '/'.join(dirname.split('/')[0:-1]).split(audio_files_dir)[1][1:]

                        print(filename)
                        line_count = int(filename)
                        # print (dirname)
                        # print (dirname_1_lvlup)

                        file_ = []

                        trans_file = \
                            os.path.join(dirname_1_lvlup, os.path.basename(dirname_1_lvlup)) \
                            + ".txt"

                        print(trans_file)

                        if t_file != trans_file:
                            t_file = trans_file
                            lines = codecs.open(t_file, 'r', encoding="utf-8").readlines()
                            # print (len(lines))
                        old_f_path = out_f + ".raw"

                        if check:
                            new_dir_path = out_crct + os.path.sep + dirname_1_lvlup
                            if not os.path.exists(new_dir_path):
                                os.makedirs(new_dir_path)
                            dur = calculate(old_f_path)
                            crct_dur += dur
                            c_dur += dur

                        else:
                            new_dir_path = out_err + os.path.sep + dirname_1_lvlup
                            if not os.path.exists(new_dir_path):
                                os.makedirs(new_dir_path)
                            dur = calculate(old_f_path)
                            error_dur += dur
                            e_dur += dur

                        filename = str("%08d" % (len(glob.glob(new_dir_path + os.path.sep + "train_audio" + os.path.sep + "*raw"))))
                        # print (filename)

                        f_wr = codecs.open(new_dir_path + os.path.sep + os.path.basename(new_dir_path) + ".txt", "a+",
                                           encoding="utf-8")
                        f_wr.write(lines[line_count])
                        new_dir_path = os.path.join(new_dir_path, "train_audio")

                        if not os.path.exists(new_dir_path):
                            os.makedirs(new_dir_path)

                        new_f_path = os.path.join(new_dir_path, filename + ".raw")
                        shutil.copy(old_f_path, new_f_path)

                    count += 1
                f_crct_dur[input_file] = getduration(c_dur)
                f_err_dur[input_file] = getduration(e_dur)
            report_wr.write("total\t" + str(getduration(crct_dur)) + "\t" + str(getduration(error_dur)))
            print("correct_one total duration : ", getduration(crct_dur))
            print("error_one total duration : ", getduration(error_dur))
            with open(os.getcwd() + os.path.sep + "curr_duration_split.txt", "w") as f:
                f.write(json.dumps(f_crct_dur) + "\n")
            with open(os.getcwd() + os.path.sep + "error_duration_split.txt", "w") as f:
                f.write(json.dumps(f_crct_dur) + "\n")

