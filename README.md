# DS5110 ICU Project
### Validating the MIMIC-IV ICU Dataset for hyponatremia based model training

Authors: Sam Morris and Harry Ren

Our repo is divided into the following categories, with more detailed writeups and reproducibility instructions in their respective directories:

1. Preprocessing (`filtered_analysis`)
2. Initial EDA (`initial_eda`)
3. Desmopressin Based Analyses (`desmopressin_analysis`)

## Preprocessing:
Construction of streamlined dataset for model training through combination of multiple ICU sub-datasets, along with sodium-based filtering to isolate hyponatremic patients.

## Initial EDA:
Original exploratory data analysis on the ICU/chartevents sub-dataset, considering validity of the dataset for model training.

## Desmopressin Analyses:
Further analysis based on Desmopressin administration using the hosp dataset.


## Data Sources:
Demo dataset found here:
[MIMIC-IV Clinical Database Demo](https://physionet.org/content/mimic-iv-demo/2.2/#files-panel)

Full dataset found here:
[MIMIC-IV](https://physionet.org/content/mimiciv/3.1/)
(Note: Credentialed Access Required)
