from driver import MongoDriver
import os
import requests
import glob
import audioread
import datetime
import subprocess
from pydub import AudioSegment
import shutil

client = MongoDriver()
db = client.get_database('data_collector')
user_collection = client.get_collection(db,"users")

train_audio_folder = ""
out_folder_path = ""
const_txt = "txt"
const_wav_raw = "wav_raw"
const_wav_trim = "wav_trim"
const_train_audio = "train_audio"


def init(user_email):
    global out_folder_path
    out_folder_path = os.path.join(os.getcwd(), user_email)

    if not os.path.exists(out_folder_path):
        os.makedirs(out_folder_path)


def download_audio_n_txt(user_email, lang):

    db = client.get_database('data_collector')

    user_collection = client.get_collection(db,"users")
    submissions_collection = client.get_collection(db, "submissions")

    found = user_collection.find_one(
        { "email_id": user_email })

    if found != None :
        print ("found registered user :: " , user_email)
    elif found == None :
        print ("query for registered user ")

    wav_files = glob.glob(out_folder_path+"/*.wav")
    count = len(wav_files)
    print (count)

    for record in submissions_collection.find( {"email_id": user_email, "language": lang}):
        try:
            url = record['audio_url']
            print (url)
            resp = requests.get(url)
            file_name = out_folder_path+"/%08d"%(count)
            wav_file = file_name+".wav"
            txt_file = file_name+".txt"

            with open(wav_file, 'wb') as f:
                f.write(resp.content)

            with open(txt_file, "w", encoding="utf-8") as f:
                f.write(record['text'])

            count += 1
            if count == 120:
                break

        except Exception as e:
            print (e, "   occurred")
            print ("for record :", record)
    wav_files = glob.glob(out_folder_path+"/*.wav")
    
    if len(wav_files) > 0:
        if len(wav_files) == len(glob.glob(out_folder_path+"/*.txt")):
            count = 1

            # wav_folder = os.path.join(out_folder_path, "wav")
            # train_audio_folder = os.path.join(out_folder_path, "train_audio")

            print ("Wav and Text files counts are equal")
            tot_sec = 0
            report_f = os.path.join(out_folder_path,'report.tsv')
            print (report_f)
            report_wr = open(report_f, 'w', encoding='utf-8')
            dir_count = 1
            in_count = 0

            for file_ in wav_files:
                if (count - 1) % 100 == 0 or count == 1:
                    wav_raw_folder = os.path.join(out_folder_path, str(dir_count),"wav_raw")
                    text_folder = os.path.join(out_folder_path, str(dir_count), "txt")

                    if not os.path.exists(wav_raw_folder):
                        os.makedirs(wav_raw_folder)

                    if not os.path.exists(text_folder):
                        os.makedirs(text_folder)
                    dir_count += 1
                    in_count = 0

                print (file_)
                with audioread.audio_open(file_) as f:
                        sec = f.duration
                print (sec)
                report_wr.write(file_+"\t"+str(datetime.timedelta(seconds=round(sec, 0)))+"\n")
                tot_sec += sec
                base_filename = os.path.basename(file_)
                just_name = base_filename.split(".wav")[0]
                dest_name = "%08d"%(in_count)
                os.rename(file_, os.path.join(wav_raw_folder,dest_name+".wav"))
                os.rename(
                    os.path.join(out_folder_path, just_name+".txt"),
                    os.path.join(text_folder, dest_name+".txt"))
                count +=1
                in_count += 1
                
            report_wr.writelines("total\t"+str(datetime.timedelta(seconds=round(tot_sec, 0)))+"\n")
            report_wr.close()
        else:
            print ("txt file count and wav file count are not same.. Pls check")
            exit()
    else:
        print ("Could not get any files")


def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    trim_ms = 0
    assert chunk_size > 0 
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


def trimming_audio():
    # HANDLING TRAILING SILENCE
    print('##### TRIMING TRAILING SILENCE #####')

    for dirname in os.listdir(out_folder_path):
        full_dir_path = os.path.join(out_folder_path, dirname)
        if os.path.isdir(full_dir_path):
            wav_trim_dir = os.path.join(full_dir_path, const_wav_trim)
            wav_raw_dir = os.path.join(full_dir_path, const_wav_raw)
            if not os.path.exists(wav_trim_dir):
                os.makedirs(wav_trim_dir)

            for filename in os.listdir(wav_raw_dir):
                if filename.endswith('.wav'):
                    try:
                        sound = AudioSegment.from_file(
                            os.path.join(wav_raw_dir, filename), format="wav")
                        start_trim = detect_leading_silence(sound)
                        end_trim = detect_leading_silence(sound.reverse())

                        duration = len(sound)
                        trimmed_sound = sound[start_trim:duration-end_trim]

                        silence = AudioSegment.silent(duration=200)
                        result_sound = silence.append(trimmed_sound).append(silence)
                        result_sound.export(
                            os.path.join(wav_trim_dir, filename), format="wav")
                    except Exception as e:
                        print(e)
                        shutil.copy(
                            os.path.join(wav_raw_dir, filename), os.path.join(wav_trim_dir, filename)
                        )
            shutil.rmtree(wav_raw_dir)
    print('>>>>>>>>>> triming silence done')


def wav_to_raw():
    print ('##### RAW FILE CONVERSION #####')

    for dirname in os.listdir(out_folder_path):
        full_dir_path = os.path.join(out_folder_path, dirname)
        if os.path.isdir(full_dir_path):
            wav_trim_dir = os.path.join(full_dir_path, const_wav_trim)
            train_audio_dir = os.path.join(full_dir_path, const_train_audio)

            if not os.path.exists(train_audio_dir):
                os.makedirs(train_audio_dir)

            if os.path.exists(wav_trim_dir):
                for filename in os.listdir(wav_trim_dir):
                    if filename.endswith('.wav'):
                        subprocess.call([
                                'sox',
                                os.path.join(wav_trim_dir, filename),
                                '-b',
                                '16',
                                '-r',
                                '16k',
                                '-c',
                                '1',
                                '-e',
                                'signed',
                                '-t',
                                'raw',
                                os.path.join(train_audio_dir, filename.replace('.wav','.raw'))
                            ])
                shutil.rmtree(wav_trim_dir)

    print ('>>>>>>>>>> RAW conversion done')


def single_transcript():
    folder_paths = []
    print ('##### CREATING SINGLE TRANSCRIPT #####')

    for dirname in os.listdir(out_folder_path):
        full_dir_path = os.path.join(out_folder_path, dirname)
        if os.path.isdir(full_dir_path):
            txt_dir = os.path.join(full_dir_path, const_txt)

            trans = os.path.join(full_dir_path, os.path.basename(dirname)+'.txt')
            transfile =  open(
                trans, "w",encoding="utf-8-sig")


            for filename in sorted(glob.glob(txt_dir+"/*.txt")):
                with open(
                    filename, 'r') as content_file:
                    content = content_file.read()
                    transfile.write(content.strip())
                    transfile.write("\n")
                    print ('copied ' + filename)
            print ('>>>>>>>>>> single transcript file creation done')
            shutil.rmtree(txt_dir)
            folder_paths.append(full_dir_path)
    return folder_paths


def get_users_from_db():
    global user_collection
    users = []
    for usr in user_collection.find():
        email = usr['email_id']
        if email not in users:
            users.append(email)

    return users

