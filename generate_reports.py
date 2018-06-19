from tester import single_tst
from adapter import ad
import os

const_ps_report = os.path.join(os.getcwd(), "pocket_sphinx_reports.tsv")

# debugging via pycharm is not working as /usr/local/libexec/sphinxtrain is not added to the pycharm env $PATH
def run(preprocess_report, lang):
    writer = open(const_ps_report, "w")
    with open(preprocess_report, "r") as fr:
        for line in fr:
            audio_dir, files_folder = line.strip().split('\t')
            ad.run(audio_dir, [[files_folder, "", os.path.basename(files_folder)+".txt"]], lang)
            writer.write(audio_dir + "\t")
            writer.write(os.getcwd()+os.path.sep+single_tst.run(audio_dir, [[files_folder, "", os.path.basename(files_folder)+".txt"]], lang))
            writer.write("\n")

    # ad.run(
    #     "/home/pankaj/asr/data/kannada/train/hassan_test/",
    #     [["/vishwasbhandarkar/1", "", "1.txt"]],
    #     cs.Kannada
    # )
    # single_tst.run(
    #     "/home/pankaj/asr/data/kannada/train/hassan_test/",
    #     [["/vishwasbhandarkar/1", "", "1.txt"]],
    #     cs.Kannada
    # )
