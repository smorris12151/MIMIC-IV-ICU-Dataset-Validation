# Project Plan

This document outlines our timeline, measurable milestones, and individual responsibilities for the project, running from **March 30** to **April 16**.

## Timeline & Milestones

### Milestone 1: Data Acquisition and Initial EDA (Already Done)
- **Objective:**  
  - Gain access to the MIMIC-IV ICU dataset and perform an initial exploratory data analysis (EDA) to understand the key clinical variables and identify data gaps (e.g., missing body metrics of hyponatremia patients).
  - Develop detailed visualizations (e.g., tables, charts, and diagrams) to capture the prevalence and trends in variables such as urine sodium, and urine potassium.
- **Measurable Outcome:**  
  Completion of an initial EDA report containing summary statistics and visualizations that highlight critical data features and trends of identified variables.
- **Individual Role:**
  - Harry and Sam design the analysis together.
  - Harry developed prototype analyses in Jupyter Notebook and conducted initial result interpretation.
  - Sam compiled the analyses into formal Python scripts and a Makefile, and finalized the EDA report.

---

### Milestone 2: Patient-Specific Analysis and Synthesis of Findings (March 30 – Apr 13)
- **Objective:**  
  - Develop a series of patient-specific analyses on different dimensions, from sodium & potassium level to waiting time measurement.
  - Generate time-series plots for selected patients showing key clinical variables such as serum sodium, desmopressin administration, urine sodium, and urine potassium.
  - Compute detailed patient-level statistics (e.g., average wait time between serum sodium measurements, number of measurements per patient) to assess data quality and consistency.
  - Synthesize findings from both global and patient-specific analyses to evaluate the overall validity of the dataset for training a hyponatremia treatment model.
  - Finally, based on comprehensive analysis results, select most important & correlated variables for hyponatremia treatment modeling. 
- **Measurable Outcome:**  
  - A suite of patient-specific time-series visualizations and statistical summaries for selected patients.
  - A comprehensive synthesis report that highlights key insights, evaluates the representativeness of clinical variables, and provides recommendations regarding the dataset’s suitability for modeling.
- **Individual Role:**  
  - **Harry:**  
    - Design and implement the patient-specific analysis.
    - Develop time-series plots and conduct analsyis on them.
  - **Sam:**  
    - Analyze detailed patient-level statistics.
    - Aggregate and interpret the findings to compile the synthesis report.

---

### Milestone 3: Final Review, Refinement, & Submission Preparation (Apr 14 – Apr 16)
- **Objective:**  
  Finalize and polish all reports and ensure reproducibility of analysis and plotting scripts.
- **Measurable Outcome:**  
  Completion and submission of all project deliverables by **April 16**.
