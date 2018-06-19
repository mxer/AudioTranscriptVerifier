import get_user_report as usr_aud_ts_files
import parse_pocketsphinx as parse_ps
import generate_reports as ps_reports
import os
import constants as cs

f_preprocess_report = os.path.join(os.getcwd(), "preprocessing_report.tsv")
lang = "hindi"
lang_code = cs.Hindi

if True:
    # Preprocessing of Audio Files
    users_list = []
        # ["amit.singh@reverieinc.com", "minakshi.sablok@reverieinc.com", "ranvijai.singh@reverieinc.com",
        #           "sangita.ekka@reverieinc.com", "sneha.chandran@reverieinc.com", "tarun.agarwal@reverieinc.com",
        #           "gitika.handique@reverieinc.com"]
    report_writer = open(f_preprocess_report, "w")
    for usr in usr_aud_ts_files.get_users_from_db():
        if usr not in users_list:
            usr_aud_ts_files.init(usr)
            usr_aud_ts_files.download_audio_n_txt(usr, lang)
            usr_aud_ts_files.trimming_audio()
            usr_aud_ts_files.wav_to_raw()
            # a = ['/home/pankaj/asr/AudioTranscriptVerifier/ranvijai.singh@reverieinc.com/2',
            #  '/home/pankaj/asr/AudioTranscriptVerifier/ranvijai.singh@reverieinc.com/3',
            #  '/home/pankaj/asr/AudioTranscriptVerifier/ranvijai.singh@reverieinc.com/1']
            for val in usr_aud_ts_files.single_transcript():
            # for val in a:
                report_writer.write(os.path.dirname(usr_aud_ts_files.out_folder_path) + "\t")
                report_writer.write(val.split(os.getcwd())[1])
                report_writer.write("\n")
            # usr_aud_ts_files.out_folder_path

if True:
    # Using PocketSphinx to generate reports
    ps_reports.run(preprocess_report=f_preprocess_report, lang=lang_code)

if True:
    # PostProcessing --> Parsing the reports, seggregating the audios for training and audios for correction
    parse_ps.run(
        ps_reports.const_ps_report
    )
