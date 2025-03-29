# Story
### High Level Background:
Nephrology specialists at Maine Health are especially interested in hyponatremia treatment for patients in the ICU. However, hyponatremia treatment heavily depends on the clinician's intuition and expertise. Stakeholders aim to develop a data-driven machine learning based treatment suggestions system to predict the optimal need for hypertonic saline and desmopressin (the consensus treatment methods of hyponatremia).

Longterm, the goal is to utilize an existing data set (specifically, the MIMIC-IV ICU dataset) to train the above mentioned model. First though, we need to determine the validity of this dataset for use with modeling hyponatremia cases. 

Since we don't have the time in our semester to actually train the model (nor the computing resources), our goals for this project are chiefly analytical, further explained below.
### Our analytic objectives are:

1. To count and catalog the percentage of patients being administered desmopressin, in hopes of making up for a lack of data regarding hypertonic saline administration and urine output
2. To determine if/how the above datapoints are representative of hyponatremia treatment
3. To consider the frequency of other important clinical variables in the treatment of hyponatremia, such as urine sodium and urine potassium, and to see if these data points can make up for the lack of urine output data
4. To plot the time series of the above variables for multiple patients, to try and visualize overall trends
5. To collect statistics on the above patient examples, such as average wait time between serum sodium measurements, average samples of various clinical variables per patient, etc
6. To assess the overall validity of the ICU Data set as a means for training a mdel to predict the optimal levels of hypertonic saline and desmopressin to administer to hyponatremic patients.

### How do these objectives differ from the original project story / prompt, if at all?
Our EDA on the first 100M rows from the `mimic-iv/icu/chart-events` dataset provided evidence of **negligible representation of hypertonic saline administration and urine output**, two important measurements when considering hyponatremia treatment. 

Ergo, we propose to try to identify trends in corresponding clinical variables (desmopressin administration and urine sodium/potassium, respectively) to see if the dataset is still a valid sample for training a model on hyponatremia treatment.

This is less of a diversion from the original prompt, and more of an elaboration, based on our initial EDA.
# Proposed Approach
### Purpose of our proposed analytic objectives:
High level, we want to see if this ICU dataset is appropriate for training the aforementioned hyponatremia treatment model. Our initial EDA is not so promising, based on the negligible representation of hypertonic saline administration. Hence, the purpose of our analytic objectives is to figure out if and how we can make up for this by leveraging other data points.
### Proposed approach to achieve our objectives:
Our method will be roughly as follows:
1. Write Python scripts to perform further EDA on the `mimic-iv/icu/chart-events` dataset to catalog clinical variables and their relative prevalence; collect these results in a presentable table to see high level statistics.
2. Use Python libraries such as seaborn and matplotlib to build diagrams of the collected data to visualize distribution / trends in our variables
3. Identify the ways that specific patients are delimited in our dataset.
4. Write Python scripts that accept our patient identifiers as parameters and run patient-specific analyses to build diagrams and collect statistics on individual patients, with respect to our above defined clinical variables.
4. Write up a high-level assessment on the validity of the dataset for model-training based on our findings.

### Potential Risks to prevent achieving our objectives:
#### Lack of time / computing resources
We have roughly a month left in the semester; therefore its very important that our goals are within scope. We hope to stay on top of the workload for our remaining weeks through planning/goal setting and regular team meetings - something akin to a Scrum methodology to best utilize our remaining time in this course.

Also, just based on the huge size of the dataset being analyzed, we will need to be efficient in our usage of the Discovery Cluster to make sure we can run the analysis on time - we've previously considered multi-threaded approached, which may prove necessary if we are to crunch ALL of these numbers.

#### Potential lack of patient identifiers
Our goal of patient specific analysis goes out the window if we can't sort out a way to delineate between patient records. That said, our stakeholder suggested that there should be time-stamped records for various patients, so this *should* be a non-issue. 


### Our Unique Contribution
We hope to provide the means for automated individual patient analysis, through original Python scripts. Ideally, this would allow stakeholders to perform more streamlined analysis on the dataset as a whole, potentially opening up further avenues of data analysis / validation. 

We also aim to provide clear documentation for researchers in future classes, such that they can leverage whatever we end up building - this could be especially useful to have as a guide for taking advantage of multi-threaded processing / analysis via the Discovery Cluster, since that tends to be a big scary black box for many students!
