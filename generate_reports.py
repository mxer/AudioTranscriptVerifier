from tester import single_tst
from adapter import ad
import os

for i, path_l in enumerate(open("dataset_list.txt")):
    path_l = path_l.strip().split("\t")
    ad.run("C:\\Users\\Reverie-IT\\Desktop\\projects\\raw_recorded_data", [path_l])
    os.chdir(os.getcwd() + "//tester")
    single_tst.run("C:\\Users\\Reverie-IT\\Desktop\\projects\\raw_recorded_data", [path_l])
    os.chdir(os.getcwd() + "\\..\\")
    print ("\n\n")
    # if i == 2:
    #     break
