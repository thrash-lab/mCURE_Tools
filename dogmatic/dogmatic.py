import os
import sys
import argparse
import subprocess
import shutil
import re
import glob
import shlex
import operator
from collections import defaultdict
from itertools import chain
import time
import ast
import pandas as pd
import numpy as np
from pathlib import Path
import textwrap
from sklearn import preprocessing
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, Normalize
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sklearn.linear_model import LinearRegression
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
from scipy.cluster import hierarchy


parser = argparse.ArgumentParser(prog='dogmatic',\
formatter_class=argparse.RawDescriptionHelpFormatter,\
description='''################################\n\
## Generate products for investigating central metabolism and bioenergetics  ##\n \
\n \
                                         1 0 1 1 0\n \
                                         0 1 1 1 0\n \
ATCGCGAAT >> KRLDWCARD >> [?] >> aldH >> 1 1 0 0 0\n \
                                         0 0 0 1 1\n \
                                         1 1 1 1 0\n \
''',\
epilog = textwrap.dedent('''\
################################
Development: E.W. Getz, 2021
Version: v1.0
Source: https://github.com/bioshaolin/mCURE_Tools
'''))
subcommands = parser.add_argument_group('## sub-commands')
db = parser.add_argument_group('## db arguments')
inputs = parser.add_argument_group('## input arguments')
outputs = parser.add_argument_group('## output arguments')
optional = parser.add_argument_group('## optional arguments')
parser.add_argument('-read', '--read', help="Show Read.me", action="store_true")
parser.add_argument('-dep', '--dependencies', help="print *_dep.yml", action="store_true")
parser.add_argument('-fig_choices', '--figure_choices', help="print figure choices", action="store_true")
subcommands.add_argument('-prod', '--prodigal' ,help="run prodigal", action="store_true")
#subcommands.add_argument('-hmm', '--hmmsearch', help='run hmmsearch', action="store_true")
subcommands.add_argument('-prod_hmm', '--prod_hmm', help="run prodigal/hmmsearch", action="store_true")
db.add_argument('-pfam', help='Specify pfam db path [for -hmm | -prod_hmm]')
#db.add_argument('-bac120', help='Specify bac120 db path [for -hmm | -prod_hmm]')
inputs.add_argument('-i', help="Specify input directory (nt)")
inputs.add_argument('-eval', help="Specify evalue threshold cutoff (default:1e-15)")
outputs.add_argument('-o', help="Specify output directory (prot)")
outputs.add_argument('-fig', help="Output binary map (pfam_full)")
outputs.add_argument('-q', help='Run algorithms with without run printing', action="store_true")
optional.add_argument('-clear', '--clear_all', help="Clear previous outputs from current input directory", action="store_true")
parser._optionals.title="## help arguments"
args = parser.parse_args()

#########
# Help  #
#########

if args.dependencies:
	subprocess.call('cat ~/dogmatic/dogmatic_dep.yml', shell=True)
else:
	pass

if args.figure_choices:
	print('pfam_full')
else:
	pass

#########
# Input #
#########

input_folder = args.i

############################
# specify option clear_all #
############################

if args.clear_all:
	subprocess.call("rm -rf " + args.o, shell=True)
else:
	pass

##########
# Output #
##########

if args.o:
	subprocess.call("mkdir " + args.o, shell=True)
else:
	pass

#####################
# sub-command -prod #
#####################

if args.prodigal:
	for fsa_nt_file in os.listdir(args.i):
		if fsa_nt_file.endswith(".fna"):
			input_path = os.path.join(args.i, fsa_nt_file)
			output_path = re.sub(".fna", ".faa", input_path)
			print(fsa_nt_file, input_path, output_path)

			cmd = "prodigal -i" + " " + input_path + " " "-a" " " + output_path
			print(cmd)
			cmd2 = shlex.split(cmd)
			if args.q:
				devnull = open(os.devnull, 'w')
				subprocess.call(cmd2, stdout=devnull)
			else:
				subprocess.call(cmd2)
				subprocess.call(cmd2)
		else:
			subprocess.call(cmd2)

	for file in os.listdir(args.i):
		if file.endswith('.faa'):
			shutil.move(os.path.join(args.i,file), os.path.join(args.o,file))
			subprocess.call("chmod 777 " + args.o + "/*", shell=True)

#########################
# sub-command -prod_hmm #
#########################

elif args.prod_hmm:

	for fsa_nt_file in os.listdir(args.i):
		if fsa_nt_file.endswith(".fna"):
			input_path = os.path.join(args.i, fsa_nt_file)
			output_path = re.sub(".fna", ".faa", input_path)
			print(fsa_nt_file, input_path, output_path)

			cmd = "prodigal -i" + " " + input_path + " " "-a" " " + output_path
			print(cmd)
			cmd2 = shlex.split(cmd)
			if args.q:
				devnull = open(os.devnull, 'w')
				subprocess.call(cmd2, stdout=devnull)
			else:
				subprocess.call(cmd2)
				subprocess.call(cmd2)
		else:
			pass

	for file in os.listdir(args.i):
		if file.endswith('.faa'):
			shutil.move(os.path.join(args.i,file), os.path.join(args.o,file))
			subprocess.call("chmod 777 " + args.o + "/*", shell=True)

	date = time.strftime("%m.%d.%Y")

	if args.clear_all:
		subprocess.call("rm -rf annotations_dir", shell=True)
	else:
		pass

	subprocess.call("mkdir " + args.o + "/annotations_dir", shell=True)
	subprocess.call("chmod 777 " + args.o + "/annotations_dir", shell=True)
	subprocess.call("mkdir "+ args.o + "/annotations_dir/hmmout_dir", shell=True)
	subprocess.call("chmod 777 "+ args.o + "/annotations_dir/hmmout_dir", shell=True)
	subprocess.call("mkdir "+ args.o + "/annotations_dir/data_products_dir", shell=True)
	subprocess.call("chmod 777 "+ args.o + "/annotations_dir/data_products_dir", shell=True)
	if args.pfam:
		for protein_file in os.listdir(args.o):
			print(input_folder)
			if protein_file.endswith(".faa"):
				input_path_h = os.path.join(args.o, protein_file)
				output_path_h = re.sub(".faa", "_pfam.hmmout", input_path_h)
				print(protein_file, input_path_h, output_path_h)

				if args.eval:
					cmd = "hmmsearch --incE " + args.eval + " --tblout " + output_path_h + " " + args.pfam + " " + input_path_h
					print(cmd)
					cmd2 = shlex.split(cmd)
					if args.q:
						devnull = open(os.devnull, 'w')
						subprocess.call(cmd2, stdout=devnull)
					else:
						subprocess.call(cmd2)
				else:
					cmd = "hmmsearch --incE 1e-15 --tblout " + output_path_h + " " + args.pfam + " " + input_path_h
					print(cmd)
					cmd2 = shlex.split(cmd)
					if args.q:
						devnull = open(os.devnull, 'w')
						subprocess.call(cmd2, stdout=devnull)
					else:
						subprocess.call(cmd2)

		dirs = os.listdir(args.o)
		for filenames in dirs:
			if filenames.endswith(".hmmout"):

				acc = re.sub(".hmmout", "", filenames)
				f = open(args.o+"/"+filenames, 'r')
				o = open(args.o+"/"+filenames+".parsed", 'w')
				hit_dict = {}
				bit_dict = defaultdict(int)
				hit_type = {}
				marker_dict = {}

				for line in f.readlines():
					if line.startswith("#"):
						pass
					else:
						newline = re.sub( '\s+', '\t', line)
						list1 = newline.split('\t')
						print(list1)
						ids = list1[0]
						null = list1[1]
						acc = list1[2]
						hit = list1[3]
						evalue = list1[4]
						bit_score = list1[5]

						if args.eval:
							if float(evalue) <= float(args.eval) and float(bit_score) > 50:
								o.write(ids + "\t" + hit + "\t" + evalue + "\n")
						else:
							if float(evalue) <= 1e-15 and float(bit_score) > 50:
								o.write(ids + "\t" + hit + "\t" + evalue + "\n")

		subprocess.call("rm -f $(find . -size 0)", shell=True)

#	if 4 == 4:
		path=args.o
		sample_list = []
		df_list = []
		allFiles = glob.glob(path + "/*_pfam.hmmout.parsed")
		for file_ in allFiles:
			samples = os.path.basename(file_)
			samples_1 = os.path.splitext(samples)[0]
			samples_2 = os.path.splitext(samples_1)[0]
			sample_list.append(samples_2)
			df = pd.read_csv(file_, index_col=None, dtype=str, header=None, sep="\t").assign(filename=samples_2)
			df.columns = ['prot','pfam_acc','evalue','genome']
			df = df[['genome','prot','pfam_acc','evalue']]
			df['genome'] = df['genome'].str.replace('_pfam', '')
			df.set_index(['genome'], inplace=True)
			df.sort_values(by = ['pfam_acc','evalue'], ascending = [True,True], inplace=True)
			df.drop_duplicates(['pfam_acc'], keep='first', inplace=True)
			print(df)

			info_path = args.pfam
			dirname = os.path.dirname(info_path)
			print(dirname)
			pfam_info = open(dirname+"/pfam-A.dat.revised", "r")
			pfams = defaultdict(list)
			for lines in pfam_info.readlines():
#				line = lines.rstrip("\n")
				line = lines.rstrip()
				tabs = line.split("\t")
				id = tabs[0]
				pfam = tabs[1]
				names = tabs[2]
#				names = tabs[3]
				pfams[pfam] = names

			pfams1 = dict(pfams)
			df['name'] = df['pfam_acc'].map(pfams1).fillna('na')
			print(df)
			df.to_csv(args.o+"/"+str(df.index.values[0])+".tsv", sep="\t")
			df_list.append(df)
			print(df_list)
		df_1 = pd.concat(df_list)
		df_1.sort_values(by = ['pfam_acc'], ascending = [True], inplace=True)
		df_1.to_csv(args.o+"/"+"combined_annotated_reps.tsv", sep="\t")

#		df_1['keys'] = df_1['prot'] + '_' + df_1['pfam_acc'].astype(str)
		df_1 = df_1[['prot','pfam_acc','evalue','name']]
#		print(df_1)

		df_2 = df_1[['pfam_acc','evalue']]
		df_2['evalue'] = 1
		print(df_2)
		df_sample_key = pd.read_csv("~/dogmatic/db/sample_key.tsv", sep="\t" , header=0, index_col=0)
		df_3 = df_2.append(df_sample_key)
		df_3 = df_3.pivot( columns='pfam_acc', values='evalue').fillna(0)
#		df_3.to_csv(args.o+"/"+"temp1.tsv", sep="\t")

		df_3.drop(['zzz'], inplace=True)
		df_3.to_csv(args.o+"/"+"pfam_full_binary.tsv", sep="\t")

		if args.fig:
			if args.fig == 'pfam_full':

				fig = plt.figure()

				colormap_1 = LinearSegmentedColormap.from_list('colorbar', ['#D4D4D4','#990000'], N=2)
				plt.pcolor(df_3, cmap=colormap_1)
				plt.yticks(np.arange(0.5,len(df_3.index)), df_3.index)
				legend = plt.colorbar(ticks=[0, 1])
				plt.tight_layout()
#				plt.show()

				fig.savefig(args.o+"pfam_full_annotation.png", dpi=900)

				subprocess.call("mv -f " + args.o + "/*.hmmout* " + args.o + "/annotations_dir/hmmout_dir", shell=True)
				subprocess.call("mv -f " + args.o + "/*.tsv* " + args.o + "/annotations_dir/data_products_dir", shell=True)
				subprocess.call("mv -f " + args.o + "/annotations_dir/data_products_dir/combined_annotated_reps.tsv " + args.o + "/annotations_dir", shell=True)
				subprocess.call("mv -f " + args.o + "/annotations_dir/data_products_dir/pfam_full_binary.tsv " + args.o + "/annotations_dir", shell=True)
				subprocess.call("mkdir " + args.o + "/annotations_dir/figures_dir", shell=True)
				subprocess.call("chmod 777 " + args.o + "/annotations_dir/figures_dir", shell=True)
				subprocess.call("mv -f " + args.o + "*.png " + args.o +"/annotations_dir/figures_dir", shell=True)
			else:
				pass
		else:
			subprocess.call("mv -f " + args.o + "/*.hmmout* " + args.o + "/annotations_dir/hmmout_dir", shell=True)
			subprocess.call("mv -f " + args.o + "/*.tsv* " + args.o + "/annotations_dir/data_products_dir", shell=True)
			subprocess.call("mv -f " + args.o + "/annotations_dir/data_products_dir/combined_annotated_reps.tsv " + args.o + "/annotations_dir", shell=True)
			subprocess.call("mv -f " + args.o + "/annotations_dir/data_products_dir/pfam_full_binary.tsv " + args.o + "/annotations_dir", shell=True)
			pass
'''
	else:
		pass

	if args.bac120:

		for protein_file in os.listdir(args.o):
			print(input_folder)
			if protein_file.endswith(".faa"):
				input_path_h = os.path.join(args.o, protein_file)
				output_path_h = re.sub(".faa", "_bac.hmmout", input_path_h)
				print(protein_file, input_path_h, output_path_h)

				cmd = "hmmsearch --incE 1e-15 --tblout " + output_path_h + " " + args.bac120 + " " + input_path_h
				print(cmd)
				cmd2 = shlex.split(cmd)
				subprocess.call(cmd2)

#		subprocess.call("mv -f " + args.o + "/*.hmmout* " + args.o + "/annotations_dir", shell=True)
#		pass
#		subprocess.call('python3 ~/mCURE_suite/scripts/py_dir/hmm_dir/hmmsearch_pfam.py ' + args.o + " " + args.db_path ,shell=True)
#		subprocess.call('python ~/ortho_workbench/scripts/py_dir/panG_dir/hmm_dir/hmmsearch_pfam.py '+args.o+"pangenome_dir "+args.db+"pfam_dir",shell=True)
#		subprocess.call('python ~/ortho_workbench/scripts/py_dir/panG_dir/hmm_dir/hmmsearch_nog.py '+args.o+"pangenome_dir "+args.db+"nog_dir",shell=True)
#		subprocess.call('python ~/ortho_workbench/scripts/py_dir/panG_dir/hmm_dir/hmmsearch_kegg.py '+args.o+"pangenome_dir "+args.db+"kegg_dir",shell=True)
#		subporcess.call('python ~/ortho_workbench/scripts/py_dir/panG_dir/hmm_dir/parse_dir/parse_hmm_outs_all.py '+args.o+"pangenome_dir", shell=True)
#	elif args.db in {'tigr,pfam,nog','tigr,nog,pfam','pfam,tigr,nog','pfam,nog,tigr','nog,tigr,pfam','nog,pfam,tigr'}:
#		pass
#	elif args.db in {'tigr,pfam,kegg','tigr,kegg,pfam','pfam,tigr,kegg','pfam,kegg,tigr','kegg,tigr,pfam','kegg,pfam,tigr'}:
#		pass
#	elif args.db in {'tigr,nog,kegg','tigr,kegg,nog','nog,tigr,kegg','nog,kegg,tigr','kegg,tigr,nog','kegg,nog,tigr'}:
#		pass

'''
####################
# renavigate to -h #
####################

if len(sys.argv[1:]) == 0:
	parser.print_help()
	parser.exit()
