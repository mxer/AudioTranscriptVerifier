from tester import single_tst
from adapter import ad
import os

# debugging via pycharm is not working as /usr/local/libexec/sphinxtrain is not added to the pycharm env $PATH
ad.run(
    "/home/pankaj/asr/data/kannada/train/hassan_test/",
    [["/vishwasbhandarkar/1","","1.txt"]]
)

single_tst.run(
    "/home/pankaj/asr/data/kannada/train/hassan_test/",
    [["/vishwasbhandarkar/1","","1.txt"]]
)

# for i, path_l in enumerate(open("dataset_list.txt")):
#     path_l = path_l.strip().split("\t")
#     ad.run("C:\\Users\\Reverie-IT\\Desktop\\projects\\raw_recorded_data", [path_l])
#     os.chdir(os.getcwd() + "//tester")
#     single_tst.run("C:\\Users\\Reverie-IT\\Desktop\\projects\\raw_recorded_data", [path_l])
#     os.chdir(os.getcwd() + "\\..\\")
#     print ("\n\n")
    # if i == 2:
    #     break
