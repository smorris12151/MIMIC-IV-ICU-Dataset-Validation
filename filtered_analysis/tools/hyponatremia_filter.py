import pandas as pd
'''
note: hyponatremia shortened to hn in following script for brevity's sake
input: path to a csv
outputs: an array of patient ids corresponding to hyponatremic patients
'''
def hn_filter(csvPath):
    df = pd.read_csv(csvPath)
    
    serum_sodium_itemids = [220645, 226534, 228389, 228390]
    hn_df = df[df['itemid'].isin(serum_sodium_itemids)]
    hn_df = hn_df[hn_df['valuenum'].notna() &
                      (hn_df['valuenum'] > 80) &
                      (hn_df['valuenum'] < 180)]
    patients = hn_df["subject_id"].unique().tolist()
    return patients
