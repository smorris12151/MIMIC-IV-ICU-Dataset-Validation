################ Demo Dataset EDA Make Commands ################

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


A1: 
	conda run -n eda_env python3 a1.py
A2: 
	conda run -n eda_env python3 a2.py
A3: 
	conda run -n eda_env python3 a3.py
A4: 
	conda run -n eda_env python3 a4.py


run_eda:
	make download_demo_files
	make unzip_demo_files
	make A1 
	make A2
	make A3
	make A4

clean:
	conda remove --name eda_env --all   
	rm -r icu
	rm -f *.tsv
	rm -f *.png
 
