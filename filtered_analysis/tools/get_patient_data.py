import numpy as np
import pandas as pd
import argparse

'''
Simple tool to extract patient specific datframe(s) from our pre-processed hn data
I implemented argparse so that we can smoothly call this from a makefile too
'''

#setting up parser to accept patient ids
parser = argparse.ArgumentParser(description='Extract patient data')
parser.add_argument("--subject_id", type = int, required = True, help = 'Patient subject ID')
parser.add_argument("--dataset", type = str, default = "filtered_data/hn_preprocessed_data.csv", help = "Input optional dataframe; defaults to preprocessed hn data")
args = parser.parse_args()

#patient data getter tool, saves a new csv to our filtered data directory
def get_patient_data(filtered_data, subject_id):
    patient_data = filtered_data.xs(subject_id, level='subject_id')
    patient_data.to_csv("filtered_data/patient_" + str(subject_id) + ".csv")

#building our dataframe out of the specified dataset (default is just our preprocessed data), and maintaning heirarchical indexing as done in preprocessing tool
df = pd.read_csv(args.dataset, index_col=["subject_id", "chartstart_time", "itemid"])
#note: this will throw an error if user feeds in an invalid subject id, so gotta have a list of those to reference I guess? I can use the unique values that I based the whole thing off of
get_patient_data(df, args.subject_id)
