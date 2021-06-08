#!/bin/bash

cd ~
echo 'alias dogmatic="python ~/dogmatic/dogmatic.py"' >> .bashrc
source .bashrc

if [[ $1 == 'mac' ]] ;
then
	conda env create -f ~/dogmatic/dogmatic_dep_mac.yml
else
	conda env create -f ~/dogmatic/dogmatic_dep.yml
fi

conda config --add channels bioconda
conda activate dogmatic
conda install -c bioconda prodigal
conda install -c bioconda hmmer
conda deactivate
source .bashrc
