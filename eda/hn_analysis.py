import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hn_df = pd.read_csv("filtered_data/hyponatremia_patients.csv")
d_items_df = pd.read_csv("icu/d_items.csv")


#building array of unique patients
hn_patients = hn_df["subject_id"].unique().tolist()
#All itemids in this dataset are either 220645 or 226534, which equate to sodium measurements; for info on patient input/output, we can filter our input/output arrays by our unique patient ids
hn_input_df = pd.read_csv("icu/inputevents.csv")
hn_output_df = pd.read_csv("icu/outputevents.csv")
hn_ingredients_df = pd.read_csv("icu/ingredientevents.csv")

hn_patients_input = hn_input_df.where(hn_input_df['subject_id'].isin(hn_patients)).dropna()
hn_patients_output = hn_output_df.where(hn_output_df['subject_id'].isin(hn_patients)).dropna()
hn_patients_ingredients = hn_ingredients_df.where(hn_ingredients_df['subject_id'].isin(hn_patients)).dropna()

#merging our filtered dataframes into one master hn patient dataframr
merge_hn = pd.merge(hn_patients_input, hn_patients_output, on = "itemid", how = "outer", suffixes= ("_input", "_output"))
merge_hn = pd.merge(merge_hn, hn_patients_ingredients, on = "itemid", how = "outer", suffixes= ("", "_ingredients"))
print(len(merge_hn['itemid'].unique()))
#Adding a column with itemids' corresponding labels
merge_hn = merge_hn.merge(d_items_df[["itemid", "label"]], on="itemid", how = "left")
print(len(merge_hn['label'].unique()))

