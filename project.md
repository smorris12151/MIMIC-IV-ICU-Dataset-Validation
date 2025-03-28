Project Name: ICU 
\
Team Members: Sam Morris and Harry Ren
\
Team Lead: Harry Ren
\
Below are the details as pulled from the project listing:
# ICU

* Stakeholders
  * Robert Hayden, MD and Prasheen Shah, MD at MaineHealth specializing in Kidney Care (Nephrology)
  * Qingchu Jin, PhD -- Research Scientist (Primary POC), The Roux Institute
* Story
  * Hospitals routinely collect data related to clinical practice. The data contains valuable information on patient care and their response to treatments. Unfortunately, the data are typically stored in archival systems that are inaccessible to researchers. MIMIC-IV is an important exception. It’s a publicly available database sourced from the electronic health records of the Beth Israel Deaconess Medical Center. Information in MIMIC-IV includes patient measurements, orders, diagnoses, procedures, treatments, and deidentified free-text clinical notes. MIMIC-IV supports a wide array of research studies, thereby reducing barriers to conducting clinical research.
* Nephrology specialists at Maine Health are especially interested in hyponatremia treatment for patients in the ICU. Hyponatremia (serum [Na] <135 mEq/L) is the most common electrolyte disorder in hospitals with a 36% in hospital prevalence and has been shown  to increase all-cause mortality and morbidity. Severe hyponatremia (serum [Na] <120 mEq/L) can even lead to 7 - 9% in-hospital mortality. However, >50% of severe hyponatremia patients receive suboptimal clinical management. The consensus treatment of severe hyponatremia are hypertonic saline (3% NaCI) and desmopressin (ddavp). However, the total amount needed for hypertonic saline and whether to use desmopressin heavily depends on the clinician's intuition and expertise. Stakeholders aim to develop a data-driven machine learning based treatment suggestions system to  predict the optimal need for hypertonic saline and desmopressin.
* This project explores the feasibility of using the MIMIC-IV ICU dataset as a suitable resource for studying this problem. Our investigation focuses on addressing the following key questions:
  * How many hyponatremia (serum [Na] <135 mEq/L) and severe hyponatremia (serum [Na] <120 mEq/L) patients are in the MIMIC-IV ICU. Note, patients staying at the ICU will have multiple serum sodium measurements, as long as one sodium measure <120 (severe hyponatremia)  or 135 (general hyponatremia) should be included into the patient cohort.
  * Check if you can find these important clinical variables including serum potassium, serum sodium, patient weight, urine output, urine sodium, urine potassium, treatments hypertonic saline (3% NaCl) and use of desmopressin. Count the percentage of missing values
  * Those above-mentioned features will have multiple measurements during the patient stay with associated timestamp, take a couple of example patients and visualize the time series of these variables.
  * Obtaining some statistics of sequential measurements for the above-mentioned variables. For example, what is the average waiting time between two consecutive serum sodium measurements? What is the average number of samples of serum sodium measurement per patient? Be creative in thinking about the statistics!
* Data
  * MIMIC-IV, a freely accessible electronic health record dataset (2023) https://www.nature.com/articles/s41597-022-01899-x
  * ICU Module documentation in Mimic-IV: https://mimic.mit.edu/docs/iv/modules/icu
  * Where to download the data. https://physionet.org/content/mimiciv/3.1/ Note, you need to finish some CITI training for accessing the clinical data. It should take you ~30 mins - 1hr. Then you need to submit the data request. You can put the supervisor as Philip or Qingchu.
