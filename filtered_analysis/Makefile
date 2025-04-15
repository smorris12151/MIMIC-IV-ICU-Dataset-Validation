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


clean:
	conda remove --name filtered_env --all   
	rm -r filtered_data
	rm -r icu
	rm -f *.tsv
 
