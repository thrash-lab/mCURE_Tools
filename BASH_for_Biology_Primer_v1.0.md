# BASH_for_Biology_Primer_v1.0 #
### Table of Contents ###
0. Preface
1. Navigation
2. Housekeeping
3. Read and Print
4. Run
5. Edit
6. Package/Environment Management and Install
7. Archive
8. Help
9. Common File Extensions
10. Common Practices
11. Syntax/Regex
12. Useful Example Snippets
13. Helpful links

## 0. Preface ##
### "central dogma" of commands ###
*General command use*: `command [-options] [-input] [-output]`

### Biology Quotes (for contemplation when your stuck) ###
"Chance favors the prepared mind."
- L. Pasteur

"We wish to discuss a structure for the salt of deoxyribose nucleic acid (D.N.A.). This structure has novel features which are of considerable biologic interest."
- R. Franklin (1953, 9 years before J. Watson was awarded the Nobel prize for the discovery of the Double Helix...)

"Life is a DNA software system."
- C. Ventor

"Evolution, to me, is the best designer of all time."
- F. Arnold

"This project is impossible. I don't think I can ever finish this."
- Every researcher who has ever used Bioinformatics and went on to publish their work.

## 1. Navigation (getting around) ##
command | function | i.e.
------- | -------- | ---
`pwd` | print the working (current) directory
`cd` | call a specified directory | `cd genomes_dir`
`home` (*alias*) OR `cd ~` | call home directory
`up` (*alias*) OR `cd ..` | call next directory up
`ll` OR `ls` OR `l` | list files and subdirectories | `ll genomes_dir`
`df` | print memory use with locations

## 2. Housekeeping (clean and organize) ##
command | function | i.e.
------- | -------- | ---
`mkdir` | make a directory | `mkdir genomes_dir`
`chmod` | change permissions of directory or file(s) | `chmod 777 genomes_dir`
`mv` OR `mv -f` | move file(s) and directories | `mv -f HTCC1062.fna genomes_dir`
`cp` OR `cp -f` | copy file(s) | `cp -f genomes_dir/HTCC1062.fna my_genome_copy.fna`
`cp -r` OR `cp -rf` | copy directory | `cp -rf genomes_dir blast_dir`
`rm` OR `rm -f` | remove file(s) | `rm -f my_genome_copy.fna`
`rm -r` OR `rm -rf` | remove directory | `rm -rf blast_dir`
`clear` | clear temp terminal log

## 3. Read and Print (look around) ##
command | function | i.e.
------- | -------- | ---
`cat` | print file text | `cat HTCC1062.fna`
`head` | print some first portion of file text | `head -1 HTCC1062.fna`
`tail` | print some last portion of file text | `tail -1 HTCC1062.fna`
`less` | print small portion of file text | `less HTCC1062.fna`
`echo` | print string | `echo 'sar11_Ia'`
`grep` | find string in file(s) or directory | `grep -c 'GT' HTCC1062.fna`

## 4. Run (use bigger programs) ##
command | function | i.e.
------- | -------- | ---
`source` | run `.sh` scripts and load `.bashrc` | `source .bashrc`
`python` | run `.py` scripts or programs | `python blastp_parse.py`
`atom` (*alias*) | open `atom` text editor

## 5. Edit (change files to serve your needs) ##
command | function | i.e.
------- | -------- | ---
`nano` | in-terminal text editor, edit `.bashrc` | `nano .bashrc`
`sed` | make change or replace string | `sed -e 's:HTCC1062:my_fav_genome:g' HTCC1062.fna`
`awk` | change tab orders, change columns, choose specific tabs | `awk -F "\t" '{print $1 FS $3}' blastp_results.tsv`

## 6. Package/Environment Management and Install (get stuff and set it up) ##
command | function | i.e.
------- | -------- | ---
`wget` | download file(s) or item | `wget ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/Candidatus_Pelagibacter_ubique/latest_assembly_versions/GCF_000012345.1_ASM1234v1/GCF_000012345.1_ASM1234v1_genomic.fna.gz -O HTCC1062.fna.gz`
`curl` | download file(s) or item | `curl ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/Candidatus_Pelagibacter_ubique/latest_assembly_versions/GCF_000012345.1_ASM1234v1/GCF_000012345.1_ASM1234v1_assembly_report.txt -o HTCC1062_assembly_report.txt`
`conda info --envs` | print available conda envs
`conda activate` | activate specified conda env | `conda activate mcure_tools`
`conda deactivate` | deactivate working conda env
`source .bashrc` | refresh `.bashrc`
`pip` | install python packages and programs | `pip install hmmer`
`conda install` | install python packages and programs | `conda install -c bioconda hmmer`
`brew` | install programs (*mac*) (*ubuntu* = linuxbrew) | `brew install blast`
`apt-get` | install programs (*ubuntu*) | `apt-get install ncbi-blast+`
`sudo` | allow root privileges | `sudo apt-get install ncbi-blast+`
`git clone` | download git repo | `git clone https://github.com/bioshaolin/mCURE_Tools.git`

## 7. Archive (make it smaller, larger or change how it's read) ##
command | function | i.e.
------- | -------- | ---
`zip` | compress file(s) by `.zip` | `zip HTCC1062.zip HTCC1062.fna`
`unzip` | decompress file(s) by `.zip` | `unzip HTCC1062.zip`
`gzip` | compress file(s) by `.gz` | `gzip HTCC1062.fna`
`gzip -d` | decompress file(s) by `.gz` | `gzip -d HTCC1062.fna.gz`
`tar -xvf` | compress directory by `.tar.gz` | `tar -xvf genomes_dir.tar.gz genomes_dir/`
`tar -csvf` | decompress directory by `.tar.gz` | `tar -czvf genomes_dir.tar.gz`

## 8. Help (I'm lost. What do I do?) ##
command | function | i.e.
------- | -------- | ---
`man` | print help menu for GNU commands | `man sed`
`-help` OR `-h` | print help menu for installed programs and some GNU commands | `blastp -h`

## 9. Common File Extensions (what is it?) ##
command | function | i.e.
------- | -------- | ---
`.txt` | text file | `assembly_report.txt`
`.md` | markdown OR ReadMe file | `ReadMe.md`
`.tsv` | tab-separated values | `blastp_parsed.tsv`
`.csv` | comma-separated values | `blastp_parsed.csv`
`.zip` | compressed file(s) | `notes.zip`
`.gz` | compressed files(s) | `notes.gz`
`.tar.gz` | compressed directory | `genomes_dir.tar.gz`
`.fasta` OR `.fa` OR `.fna` | fasta nucleotide | `HTCC1062.fna`
`.faa` | fasta amino acid | `HTCC1062.faa`
`.aln` | alignment | `sar11_Ia.faa.aln`
`.hmm` | hidden markov model | `bac120.hmm`
`.dat` OR `.info` | hmm metadata | `pfam-A.info`
`.sh` | shell script | `clean_genome_names.sh`
`.py` | python script | `blastp_parse.py`
`.yml` | environment "mark up" setup | `mcure_tools_env.yml`

## 10. Common Practices (make your life easier) ##
command | function | i.e.
------- | -------- | ---
`_` | underscore gaps in names of file(s) or strings | `HTCC1062_vs_IIIa.parsed.tsv` NOT `HTCC1062 vs IIIa.parsed.tsv`
`2021.02.01` | date outputs and commonly used result file(s) | `HTCC1062_vs_IIIa_2021.02.01.parsed.tsv`
`_dir` | name all directories with `_dir` (*excluding programs*) | `genomes_dir` NOT `genomes`
`mv -f *.gz` | separate compressed file(s) that you need to keep from a working directory | `mv -f *.gz archive_dir`
`nano .bashrc` | familiarize your `.bashrc`
`source .bashrc` | refresh `.bashrc`

## 11. Syntax/Regex (next-level purpose and efficiency) ##
*NOTE*: This is by no means ALL possible regex. This is a curated list that you will most likely find useful throughout your projects.
syntax/regex | function | i.e.
------- | -------- | ---
`~` | home directory | `cd ~`
`.` | any 1 character in a str | `sed -e 's:GT.AAAA:fav_gene:g' HTCC1062.fna`
`.` | working directory | `mv -f ~/genomes_dir/HTCC1062.fna .`
`*` | any number of characters | `sed -e 's:GT*AAAA:fav_gene:g' HTCC1062.fna`
`*` | all followed by | `mv -f *.faa blast_dir`
`\s` | space | `sed -e 's:result\stime:result,time:g' blastp_parse.tsv`
`\t` | tab | `sed -e 's:result\ttime:result,time:g' blastp_parse.tsv`
`\n` | line break | `sed -e 's:result\ntime:result,time:g' blastp_parse.tsv`
`$` | end of line | `sed -e 's:abcd$:abcd1234:g' blastp_parse.tsv`
`$` | array or column number | `awk -F "\t" '{print $1 FS $3}' blastp_results.tsv`
`>` | output into file | `cat *.fna > all_nt.fna`
`\|` | "pipe" commands together (*do this and that*) | `cat HTCC1062.fna \| sed -e 's:GT*AT:fav_gene_1:g' \| sed -e 's:AA*GC:fav_gene_2:g' > fav_gene_deletions.fna`
`;` | run commands after on another | `mv *.fna nt_dir ; mv -f *.fna.aln alignment_dir`
`-r` | generally means recursive (*take action recursively*) | `rm -rf genomes_dir`
`-f` | generally means force (*force an action without asking permission*) | `mv -f HTCC1062.fna blast_dir`

## 12. Useful Example Snippets (some of my go-tos) ##
command | function
------- | --------
`cat *.fna > all_nt.fna` | concatenate all genomes into one file
`cat file.fna \| sed -e 's:GT*AT:fav_gene_1:g' \| sed -e 's:AA*GC:fav_gene_2:g' > fav_gene_deletions.fna` | run a repeat function on multiple strings
`awk -F '\t' '{print $1 FS $3}' blastp_results.tsv > blastp_results_parsed.tsv` | parse desired columns
`grep -c 'GT' *.fna` | count occurrences in each file
`grep -c 'GT' *.fna` | count how many files the str occurs
`grep -o 'GT' *.fna \| wc -l` | count occurrences in entire directory
`ll *.fna \| wc -l` | count how many files have a specific suffix in a directory

## 13. Helpful Links (make your life easier) ##
### Biology ###
link | function
------- | --------
(https://www.ncbi.nlm.nih.gov/) | National Center for Biotechnology Information
(ftp://ftp.ncbi.nlm.nih.gov/) | NCBI ftp server (*rapid data access*)
(https://pubchem.ncbi.nlm.nih.gov/) | NCBI molecular database (*in-depth molecule/nomenclature background*)
(https://blast.ncbi.nlm.nih.gov/Blast.cgi) | NCBI blast GUI
(https://www.embl.de/) | European Molecular Biology Laboratory
(https://www.uniprot.org/) | EMBL database (*in-depth gene/protein background*)
(https://pfam.xfam.org/) | EMBL protein family hmm database
(http://eggnog5.embl.de/#/app/home) |  EMBL ortholog db

### Coding ###
link | function
------- | --------
(https://stackexchange.com/) | q&a community for all things coding and other topics
(https://github.com/bioshaolin/mCURE_Tools) | mCURE git repository
(https://brew.sh/) | brew installation
(https://anaconda.org/bioconda/blast) | conda blast installation
(http://www.metagenomics.wiki/tools/blast/install) | apt-get blast installation
(http://eddylab.org/software/hmmer/Userguide.pdf) | hmmer3 manual
(http://hmmer.org/documentation.html) | hmmer installation
(https://sites.ualberta.ca/~kirchner/513/OpenOffice%20regular%20expression%20list.pdf) | extended regex list

Development: E.W. Getz, 2021 \
Institution: University of Southern California, MBBO \
Version: v1.0
