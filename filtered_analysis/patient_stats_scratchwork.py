import numpy as np
import pandas as pd
from datetime import datetime
from tools.get_patient_data import get_patient_data

'''
This python script is just where I've been experimenting with multi indexing of the pre-processed data and testing different tools
I wouldn't bother runnning this, as it was just to help me think through how I would implement the logic in the makefile. 
'''

df = pd.read_csv("filtered_data/hn_preprocessed_data.csv", index_col=["subject_id", "chartstart_time", "itemid"])


print(df.index)
get_patient_data(df, 10005817)
