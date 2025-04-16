import pandas as pd

# Serum sodium itemids: Sodium (serum), Sodium (whole blood), and soft versions
serum_sodium_itemids = [220645, 226534, 228389, 228390]
print(f"Using serum sodium itemids: {serum_sodium_itemids}")

# Read the first 100 million rows from chartevents.csv
chartevents_path = "icu/chartevents.csv"
df = pd.read_csv(chartevents_path, nrows=100000000, usecols=['subject_id', 'itemid', 'valuenum'])

# Filter for sodium measurements
sodium_df = df[df['itemid'].isin(serum_sodium_itemids)]

# Filter for valid measurements (exclude implausible values)
sodium_df = sodium_df[sodium_df['valuenum'].notna() &
                      (sodium_df['valuenum'] > 80) &
                      (sodium_df['valuenum'] < 180)]

# Identify unique patients with hyponatremia and severe hyponatremia
hyponatremia_patients = sodium_df[sodium_df['valuenum'] < 135]['subject_id'].unique()
severe_hyponatremia_patients = sodium_df[sodium_df['valuenum'] < 120]['subject_id'].unique()

total_sodium_measurements = len(sodium_df)

print("\nHyponatremia Patient Cohort Results:")
print(f"Total sodium measurements processed: {total_sodium_measurements}")
print(f"Total patients with hyponatremia (Na < 135 mEq/L): {len(hyponatremia_patients)}")
print(f"Total patients with severe hyponatremia (Na < 120 mEq/L): {len(severe_hyponatremia_patients)}")

# Calculate percentage of ICU patients with hyponatremia
icustays = pd.read_csv("icu/icustays.csv")
total_unique_patients = icustays['subject_id'].nunique()

print(f"\nPercentage of ICU patients with hyponatremia: {len(hyponatremia_patients) / total_unique_patients * 100:.2f}%")
print(f"Percentage of ICU patients with severe hyponatremia: {len(severe_hyponatremia_patients) / total_unique_patients * 100:.2f}%")
