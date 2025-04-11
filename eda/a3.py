import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
#code below parses arg from makefile to determine which dataset to use
parser = argparse.ArgumentParser()
parser.add_argument('--variable', type=int, default=0)
args = parser.parse_args()
print(args.variable)

if args.variable == 1:
    print("success")
    chartevents_path = "filtered_data/hyponatremia_patients.csv"
else:
    chartevents_path = "icu/chartevents.csv"
serum_sodium_itemids = [220645, 226534, 228389, 228390]

# read the first 100M rows from chartevents including charttime
sodium_ts = pd.read_csv(chartevents_path, 
                        nrows=100000000, 
                        usecols=['subject_id', 'charttime', 'itemid', 'valuenum'])

# Filter for sodium measurements using the pre-defined serum sodium itemids
sodium_ts = sodium_ts[sodium_ts['itemid'].isin(serum_sodium_itemids)]

# Filter for valid sodium measurements (exclude implausible values)
sodium_ts = sodium_ts[sodium_ts['valuenum'].notna() &
                      (sodium_ts['valuenum'] > 80) &
                      (sodium_ts['valuenum'] < 180)]

# Convert charttime to datetime
sodium_ts['charttime'] = pd.to_datetime(sodium_ts['charttime'])

def compute_correction_rates(group):
    group = group.sort_values('charttime')
    group['delta_sodium'] = group['valuenum'].diff()
    group['delta_time_hours'] = group['charttime'].diff().dt.total_seconds() / 3600.0
    group['correction_rate'] = group['delta_sodium'] / group['delta_time_hours']
    return group

sodium_rates = sodium_ts.groupby('subject_id').apply(compute_correction_rates).reset_index(drop=True)
# Drop the first measurement per patient (where diff is NaN)
sodium_rates = sodium_rates.dropna(subset=['correction_rate'])

# Remove any infinite correction_rate values (e.g., when delta_time_hours == 0)
sodium_rates = sodium_rates[np.isfinite(sodium_rates['correction_rate'])]

# For safety, consider only intervals with an increase in sodium (positive correction)
sodium_rates = sodium_rates[sodium_rates['correction_rate'] > 0]


# Identify rapid correction intervals: >10 mEq/L in 24 hours (~0.42 mEq/L per hour)
rapid_threshold = 10 / 24.0  # ~0.42 mEq/L per hour
rapid_intervals = sodium_rates[sodium_rates['correction_rate'] >= rapid_threshold]
print(f"Total intervals with rapid correction (>{rapid_threshold:.2f} mEq/L per hour): {len(rapid_intervals)}")

# Histogram of correction rates across all intervals (filtered to 0-3 mEq/L/hr)
plot_rates = sodium_rates[
    np.isfinite(sodium_rates['correction_rate']) &
    (sodium_rates['correction_rate'].between(0, 3))
].copy()

sns.set_context("talk", font_scale=0.9)
plt.figure(figsize=(20, 12))
plt.hist(plot_rates['correction_rate'], bins=50, color='skyblue', edgecolor='black')
plt.xlabel("Sodium Correction Rate (mEq/L per hour)")
plt.ylabel("Frequency")
plt.title("Histogram of Sodium Correction Rates (0-3 mEq/L/hr)")
plt.axvline(rapid_threshold, color='red', linestyle='--', label=f'Rapid Threshold ({rapid_threshold:.2f})')
plt.legend()
plt.savefig("A3_Histogram.png")
