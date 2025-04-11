import pandas as pd
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

df = pd.read_csv(chartevents_path, nrows=100000000, usecols=['subject_id', 'itemid', 'valuenum'])
# Load d_items to identify itemids for the clinical variables
d_items_path = "icu/d_items.csv"
d_items = pd.read_csv(d_items_path)
variable_itemids = {
    "Serum Sodium": [220645, 226534, 228389, 228390],
    "Serum Potassium": [220640, 227442],
    "Patient Weight": [224639, 225124, 226512, 226531, 226740, 226741, 226742, 226846, 227854],
    "Urine Output": [227519],
    "Hypertonic Saline (3% NaCl)": [225161],
}
print("Using variable_itemids:")
print(variable_itemids)

results = {}

# Loop over each clinical variable and filter the already loaded 'df'
for var, itemids in variable_itemids.items():
    var_df = df[df['itemid'].isin(itemids)]
    total_count = len(var_df)
    valid_count = var_df['valuenum'].notna().sum()
    missing_count = total_count - valid_count
    # Count unique patients with at least one valid (non-missing) measurement
    patient_ids = var_df[var_df['valuenum'].notna()]['subject_id'].unique()
    results[var] = {
        "total_rows": total_count,
        "valid_count": valid_count,
        "missing_count": missing_count,
        "patient_count": len(patient_ids)
    }


# Load ICU stays to get the denominator: total unique ICU patients
icustays_path = "icu/icustays.csv"
icustays = pd.read_csv(icustays_path)
total_icu_patients = icustays['subject_id'].nunique()

# Report the analysis results for each variable
for var, res in results.items():
    total = res["total_rows"]
    valid = res["valid_count"]
    missing = res["missing_count"]
    patient_count = res["patient_count"]
    missing_percentage = (missing / total * 100) if total > 0 else 0
    patient_percentage = (patient_count / total_icu_patients * 100) if total_icu_patients > 0 else 0
    
    print(f"\nVariable: {var}")
    print(f"  Total measurements encountered: {total}")
    print(f"  Valid (non-missing) measurements: {valid}")
    print(f"  Missing measurements: {missing} ({missing_percentage:.2f}%)")
    print(f"  Percentage of ICU patients with at least one valid measurement: {patient_percentage:.2f}%")
