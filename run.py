import sys
import os

# f_name = os.path.join(os.getcwd(),"input")
#
# files_list = []
#
# with open(f_name, 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
#         l_split = line.split("\t")
#         # folder_path, out_file = l_split
#         files_list.append(l_split)

from adapter import ad
from tester import single_tst

audio_dir = "C:\\Users\\Reverie-IT\\Desktop\\projects\\raw_recorded_data"
for line in open(os.getcwd()+"/dataset_list.txt","r").readlines():
    file_ = line.strip().split(":")

    ad.run(audio_dir, [file_])
    break
    # single_tst.run(audio_dir, )



