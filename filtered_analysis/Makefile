################ Demo Dataset Make Commands ################

download_demo_files: environment.yml
#build conda env:
	conda env create -f environment.yml
#download fileset from Mimic iv website (for size's sake, this is using the demo dataset):
	conda run -n filtered_env wget -r -N -c -np https://physionet.org/files/mimic-iv-demo/2.2/
#move uncompressed icu and hosp files to root directory
	mv physionet.org/files/mimic-iv-demo/2.2/icu .

unzip_demo_files: physionet.org
#unzip files
	gunzip icu/*.csv.gz
#Remove unneeded files
	rm -r physionet.org

build_hn_dataset: 
#download and unzip total demo dataset
	make download_demo_files
	make unzip_demo_files
#build empty directory to house filtered csv
	mkdir filtered_data
#import and run 
	conda run -n filtered_env python3 tools/hn_preprocessing.py

#Specifying error message for build_patient_dataset missing dependency (Thanks Claude!)
filtered_data/hn_preprocessed_data.csv:
	$(error The preprocessed data file is missing. Please run 'make build_hn_dataset' first to generate it)

#make command for building patient specific datasets - I used my friend Claude's help for specifying the need for subject id (the ifndef part) :o)
build_patient_dataset: filtered_data/hn_preprocessed_data.csv
ifndef SUBJECT_ID
	$(error SUBJECT_ID is not set. Please provide a subject ID using "make build_patient_dataset SUBJECT_ID=value")
else
	conda run -n filtered_env python3 tools/get_patient_data.py --subject_id=$(SUBJECT_ID)
endif

clean:
	conda remove --name filtered_env --all   
	rm -r filtered_data
	rm -r icu
 
