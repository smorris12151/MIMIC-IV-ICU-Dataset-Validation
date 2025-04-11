################ Demo Dataset Make Commands ################

download_demo_files: environment.yml
#build conda env:
	conda env create -f environment.yml
#download fileset from Mimic iv website (for size's sake, this is using the demo dataset):
	conda run -n eda_env wget -r -N -c -np https://physionet.org/files/mimic-iv-demo/2.2/
#move uncompressed icu and hosp files to root directory
	mv physionet.org/files/mimic-iv-demo/2.2/icu .

unzip_demo_files: physionet.org
#unzip files
	gunzip icu/*.csv.gz
#Remove unneeded files
	rm -r physionet.org

hn_only: 
#download and unzip total demo dataset
	make download_demo_files
	make unzip_demo_files
#build empty directory to house filtered csv
	mkdir filtered_data
#import and run 
	conda run -n eda_env python3 -c "from tools.hyponatremia_filter import hn_filter; hn_filter('icu/chartevents.csv')"
	mv hyponatremia_patients.csv filtered_data
	rm -r icu


################ Total ICU Dataset Make Commands ################

download_total_icu_dataset: environment.yml
	conda env create -f environment.yml
	conda run -n eda_env wget -r -N -c -np --user smorris12151 --ask-password https://physionet.org/files/mimiciv/3.1/icu/


#####################
#default value of var = 0 for non filtered analysis
var ?= 0
A1: 
	conda run -n eda_env python3 a1.py --variable="$(var)"
A2: 
	conda run -n eda_env python3 a2.py --variable="$(var)"
A3: 
	conda run -n eda_env python3 a3.py --variable="$(var)"
A4: 
	conda run -n eda_env python3 a4.py --variable="$(var)"

run_demo_analysis:
	make download_demo_files
	make unzip_demo_files
	make A1 
	make A2
	make A3
	make A4

run_filtered_analysis:
	var=1
	make hn_only
	make A1 var=1
	make A2 var=1
	make A3 var=1
	make A4 var=1

clean:
	conda remove --name eda_env --all   
	rm -r icu
	rm -r filtered_data
	rm -f *.tsv
	rm -f *.png
 
