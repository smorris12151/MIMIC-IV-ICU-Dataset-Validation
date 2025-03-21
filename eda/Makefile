download_files: environment.yml
#build conda env:
	conda env create -f environment.yml
#download fileset from Mimic iv website (for size's sake, this is using the demo dataset):
	conda run -n eda_env wget -r -N -c -np https://physionet.org/files/mimic-iv-demo/2.2/
#move uncompressed icu and hosp files to root directory
	mv physionet.org/files/mimic-iv-demo/2.2/icu .
	mv physionet.org/files/mimic-iv-demo/2.2/hosp .


unzip_files: physionet.org
#unzip files
	gunzip icu/*.csv.gz
	gunzip hosp/*.csv.gz
#Remove unneeded files
	rm -r physionet.org


A1: 
	conda run -n eda_env python3 a1.py
A2: 
	conda run -n eda_env python3 a2.py
A3: 
	conda run -n eda_env python3 a3.py
A4: 
	conda run -n eda_env python3 a4.py

all:
	make download_files
	make unzip_files
	make A1
	make A2
	make A3
	make A4

clear:
	rm -r icu
	rm -r hosp
	rm -f *.tsv
	rm -f *.png
	conda remove --name eda_env --all    
