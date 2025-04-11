


# Note:

Use command ```make all``` to build environment, download/unzip mimic iv demo dataset, and run all analyses. This will populate the images in this doc.

Upon running `make all`, your file heirarchy should look like this:
![Configured file heirarchy of eda directory](/eda_directory.png)

Also note, for the sake of file downloads, the dataset being used here is the smaller mimic iv DEMO dataset - ergo, the generated diagrams here do not perfectly match those results we found with the proper dataset.. This is an easy swap, assuming you have the original dataset in place of the demo (literally just swap them out in the root directory of this repo.)

To remove the built environment / files / etc, run `make clear`

# A1: Hyponatremia Patient Cohort Identification:

In this analysis, we identify the subset of ICU patients with hyponatremia by processing the first 100 M rows from the MIMIC-IV `chartevents` table. We focus on serum sodium measurements by filtering for known itemids and valid values (80–180 mEq/L). Patients are classified into two groups:

- **Hyponatremia**: Patients with at least one serum sodium measurement below 135 mEq/L.
- **Severe Hyponatremia**: Patients with at least one serum sodium measurement below 120 mEq/L.


We then compare the counts of these patients against the total ICU population (from the `icustays` table) to determine the percentage of patients in each group.

### Conclusion

- **Total Sodium Measurements Processed**: 162,286
- **Patients with Hyponatremia (Na < 135 mEq/L)**: 6,006 (9.19% of ICU patients)
- **Patients with Severe Hyponatremia (Na < 120 mEq/L)**: 256 (0.39% of ICU patients)

The analysis shows that approximately **9.19%** of ICU patients have at least one serum sodium measurement below 135 mEq/L, while only about **0.39%** exhibit severe hyponatremia (Na < 120 mEq/L). This indicates that, in our dataset, hyponatremia (especially its severe form) is relatively uncommon. These findings further emphasize the importance of controlling sodium correction rates, as severe hyponatremia often requires faster correction, but overly rapid correction can lead to brain damage (see A3).

# A2: Assessing Data Availability for Key Clinical Variables in the ICU Dataset:

In this analysis, we assess the **availability** of key clinical variables from the MIMIC-IV ICU dataset by determining how many measurements exist for each variable and what percentage of ICU patients have at least one valid measurement. We focus on variables such as **serum sodium**, **serum potassium**, **patient weight**, **urine output**, and **hypertonic saline (3% NaCl)**. Using the first 100 M rows from the `chartevents` table together with a predefined mapping of variables to itemIDs from the `d_items` table, we filter the data for each variable, count the total and valid (non-missing) measurements, and calculate the number of unique patients with valid measurements. Finally, we compare these counts against the total ICU population (from the `icustays` table) to determine the coverage for each variable.


### Conclusion
The analysis reveals that **serum sodium, serum potassium, and patient weight** are well-documented in the dataset, with each variable having over 140k measurements and valid data for approximately **22–23%** of ICU patients. In contrast, **urine output and hypertonic saline (3% NaCl)** administration have negligible representation. These findings indicate that while serum electrolytes and weight are reliable for further modeling, additional data sources or methods may be required to incorporate urine output and hypertonic saline usage in future hyponatremia treatment models.


# A3: Sodium Correction Rate
In this analysis, we calculate the **rate of change** in serum sodium over time for ICU patients (using the first 100 M rows from the MIMIC-IV `chartevents` table). We define **rapid correction** as >10 mEq/L in 24 hours (~0.42 mEq/L per hour), a threshold recommended to reduce the risk of osmotic demyelination syndrome (see [Tandukar S, Sterns RH, Rondon-Berrios H. Osmotic Demyelination Syndrome following Correction of Hyponatremia by ≤10 mEq/L per Day](https://pmc.ncbi.nlm.nih.gov/articles/PMC8786124/)). We then plot a histogram of sodium correction rates between 0 and 3 mEq/L per hour to see how often corrections exceed this safety threshold.

![Histogram of Sodium Correction Rates (0-3 mEq/L/hr)](A3_Histogram.png)

### Conclusion

From the histogram, we see that while many patients experience slow-to-moderate sodium increases, rapid correction does occur in a portion of intervals. Incorporating a mechanism to prevent overly fast rises in serum sodium is vital for patient safety and should be considered in future hyponatremia treatment models.



# A4: Relationship Between Serum Sodium Levels and ICU Length of Stay:
In this analysis, we load **serum sodium measurements** from the first 100 M rows of the MIMIC-IV `chartevents` table, merge them with **ICU length of stay (LOS) data** from `icustays`, and visualize their relationship. We first filter sodium values to valid `itemid`'s within a plausible range (80–180 mEq/L), then merge these measurements with each patient's LOS via a simple join on `subject_id`. Finally, we plot a scatterplot of sodium (x-axis) vs. LOS (y-axis) to identify potential patterns.

![Scatterplot: Serum Sodium vs ICU Length of Stay](A4_Scatterplot.png)


### Conclusion
- **Broad Distribution**: Most patients cluster around normal sodium values (roughly 130–145 mEq/L) with a wide range of ICU stays—anywhere from a few days up to 40+ days.
- **Long Tails**: A minority of patients have either very high or very low sodium readings, but their LOS spans from short to quite prolonged, suggesting no simple linear correlation.
- **No Clear Trend**: The scatter is relatively diffuse, implying that single sodium measurements alone are not strongly predictive of ICU length of stay. Multiple factors likely influence how long a patient remains in the ICU.

Overall, The broad scatter suggests there's not clear linear relationship between patients sodium level and their LOS. Additional variables or time-based trends may be needed to uncover stronger patterns.
