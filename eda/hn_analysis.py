import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



hn_df = pd.read_csv("filtered_data/hyponatremia_patients.csv")
d_items_df = pd.read_csv("icu/d_items.csv")

#simple tool function for equating itemid to label
def get_label(itemid):
    label = d_items_df[d_items_df["itemid"] == itemid]["label"].values[0]
    return label


#building array of unique patients
hn_patients = hn_df["subject_id"].unique().tolist()
#All itemids in this dataset are either 220645 or 226534, which equate to sodium measurements; for info on patient input/output, we can filter our input/output arrays by our unique patient ids
hn_input_df = pd.read_csv("icu/inputevents.csv")
hn_output_df = pd.read_csv("icu/outputevents.csv")
hn_ingredients_df = pd.read_csv("icu/ingredientevents.csv")

hn_patients_input = hn_input_df.where(hn_input_df['subject_id'].isin(hn_patients)).dropna()
hn_patients_output = hn_output_df.where(hn_output_df['subject_id'].isin(hn_patients)).dropna()
hn_patients_ingredients = hn_ingredients_df.where(hn_ingredients_df['subject_id'].isin(hn_patients)).dropna()

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
            total_endtimes.append(total_chartstarttimes[index])

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




#populating the arrays:
array_builder(hn_df)
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

print(df)

