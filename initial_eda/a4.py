import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify itemids for serum sodium (MIMIC-IV known itemids)
serum_sodium_itemids = [220645, 226534, 228389, 228390]
print(f"Using serum sodium itemids: {serum_sodium_itemids}")

# Read the first 100M rows from chartevents.csv, focusing on relevant columns
chartevents_path = "icu/chartevents.csv"
df = pd.read_csv(chartevents_path, nrows=100000000, usecols=['subject_id', 'itemid', 'valuenum'])

# Filter for serum sodium measurements and plausible values
df_sodium = df[df['itemid'].isin(serum_sodium_itemids)]
df_sodium = df_sodium[df_sodium['valuenum'].notna() & (df_sodium['valuenum'] > 80) & (df_sodium['valuenum'] < 180)]

# Load icustays.csv to retrieve ICU length of stay (los)
icustays_path = "icu/icustays.csv"
icustays = pd.read_csv(icustays_path)


# Merge sodium measurements with icustays to bring in 'los'
df_sodium_los = pd.merge(df_sodium, icustays[['subject_id', 'los']], on='subject_id', how='left')

# Visualization: Scatterplot of Serum Sodium vs. ICU Length of Stay
sns.set_context("talk", font_scale=0.9)
plt.figure(figsize=(20, 12))
sns.scatterplot(data=df_sodium_los, x='valuenum', y='los', alpha=0.5)
plt.xlabel("Serum Sodium (mEq/L)")
plt.ylabel("ICU Length of Stay (days)")
plt.title("Scatterplot: Serum Sodium vs. ICU Length of Stay")
plt.savefig("A4_Scatterplot.png")
