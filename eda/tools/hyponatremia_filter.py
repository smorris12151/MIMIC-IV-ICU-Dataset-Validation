import pandas as pd
#note: hyponatremia shortened to hn in following script for brevity's sake


def hn_filter(csvPath):
    df = pd.read_csv(csvPath, usecols=['subject_id', 'itemid', 'valuenum'])
    
    serum_sodium_itemids = [220645, 226534, 228389, 228390]
    hn_df = df[df['itemid'].isin(serum_sodium_itemids)]
    hn_df = hn_df[hn_df['valuenum'].notna() &
                      (hn_df['valuenum'] > 80) &
                      (hn_df['valuenum'] < 180)]
    
    hn_csv = hn_df.to_csv('hyponatremia_patients.csv', index = False)
    return hn_csv
