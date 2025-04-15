import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hyponatremia_filter 

'''
The goal of this tool is to filter out hyponatremic patients from our icu dataset, and colate important variables in an easily managed format
This way, we can easily retrieve ALL relevant patient specific data for our analysis, and easily pull out individual patient datasets

'''

#First we use hyponatremia_filter.py to filter out hyponatremic patients from our icu/chartevents csv, and build a dataframe out of it
hn_patients = hyponatremia_filter.hn_filter("icu/chartevents.csv")
hn_df = pd.read_csv("icu/chartevents.csv")
hn_chartevents_df = hn_df.where(hn_df['subject_id'].isin(hn_patients)).dropna()

#We now use the same logic to filter hyponatremic patients from out input, output, and ingredient datasets:
input_df = pd.read_csv("icu/inputevents.csv")
output_df = pd.read_csv("icu/outputevents.csv")
ingredients_df = pd.read_csv("icu/ingredientevents.csv")

hn_input_df = input_df.where(input_df['subject_id'].isin(hn_patients)).dropna()
hn_output_df = output_df.where(output_df['subject_id'].isin(hn_patients)).dropna()
hn_ingredients_df = ingredients_df.where(ingredients_df['subject_id'].isin(hn_patients)).dropna()

#simple tool function for equating itemid to label
d_items_df = pd.read_csv("icu/d_items.csv")
def get_label(itemid):
    label = d_items_df[d_items_df["itemid"] == itemid]["label"].values[0]
    return label

#building empty arrays to populate for total dataframe columns
total_subject_ids = []
total_chartstarttimes = []
total_endtimes = []
total_timespans = []
total_linkorderids = []
total_orderids = []
total_itemids = []
total_labels = []
total_amountvalues = []
total_avuoms = []
total_rates = []
total_rateuoms = []

#tool function for populating the above empty arrays
#note the iterative prototype below; this is undoubtedly not the most computationally efficient methodd. Future builds should ustilize pandas ufuncs for quicker computation.
def array_builder(df):
    for index, row in df.iterrows():
        total_subject_ids.append(row["subject_id"])

        if("charttime" in df.columns):
            total_chartstarttimes.append(row["charttime"])
        elif("starttime" in df.columns):
            total_chartstarttimes.append(row["starttime"])
        else:
            total_chartstarttimes.append("")

        if("endtime" in df.columns):
            total_endtimes.append(row["endtime"])
        else:
            total_endtimes.append(0)

        if("linkorderid" in df.columns):
            total_linkorderids.append(row["linkorderid"])
        else:
            total_linkorderids.append(0)
        if("orderids" in df.columns):
            total_orderids.append(row["orderid"])
        else:
            total_orderids.append(0)
            
        total_itemids.append(row["itemid"])
        total_labels.append(get_label(row["itemid"]))

        if("amount" in df.columns):
            total_amountvalues.append(row["amount"])
            total_avuoms.append(row["amountuom"])
        elif("value" in df.columns):
            total_amountvalues.append(row["value"])
            total_avuoms.append(row["valueuom"])
        else:
            total_amountvalues.append(0)
            total_avuoms.append("")

        if("rate" in df.columns):
            total_rates.append(row["rate"])
            total_rateuoms.append(row["rateuom"])
        else:
            total_rates.append(0)
            total_rateuoms.append("")


#populating our empty arrays:
array_builder(hn_chartevents_df)
array_builder(hn_input_df)
array_builder(hn_ingredients_df)
array_builder(hn_output_df)


#building our finalized hn patient dataframe from our arrays:

df = pd.DataFrame({
    "subject_id": total_subject_ids,
    "chartstart_time": total_chartstarttimes,
    "end_time": total_endtimes,
    "link_orderid": total_linkorderids,
    "orderid": total_orderids,
    "itemid": total_itemids,
    "label": total_labels,
    "amount_value": total_amountvalues,
    "amount_value_unit": total_avuoms,
    "rate": total_rates,
    "rate_unit": total_rateuoms
})
#saving this dataframe to a csv for future processing
df.to_csv("filtered_data/hn_preprocessed_data.csv", index=False)

