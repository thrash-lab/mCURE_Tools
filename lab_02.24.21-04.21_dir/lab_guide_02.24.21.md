# Reference #

## Helpful one-liners ##
- *NOTE*: If a string in the commands below is not the one you need change it out for the string or filename you want to use.

command  | purpose | type of yield
---------| ------- | -------------
`tar -xvf quiz_4_data_dir.tar.gz` | decompress dir
`sed 's:CTT:CTT\n:g' HTCC1062.fna \| grep -c 'CTT'` | count all str occurrences (abiotic "coding" control) | theoretical
`grep -c 'CTT' *.fna` | count line str occurrences (abiotic "coding" control) (proxy for bonding affinity) (approaching biotic yield but still abiotic) | theoretical
`cat HTCC1062.faa \| tr -cd 'L' \| wc -c` | count single character occurrences (biotic yield) | experimental (actual)
`grep -c '^' combined_annotated_reps.tsv` | count total number of proteins annotated | experimental
`grep -o '^e_coli.*Glycine' combined_annotated_reps.tsv` | print full occurrence of organism and protein | experimental
`grep -c '^e_coli.*Glycine' combined_annotated_reps.tsv` | count full occurrence of organism and protein | experimental
`dogmatic -h` | help menu
`dogmatic -prod -i <PATH/TO/INPUT/DATA/DIR> -o <PATH/TO/CREATE/OUTPUT/DIR> -clear` | aa translation | experimental
`dogmatic -prod_hmm -i <PATH/TO/INPUT/DATA/DIR> -o <PATH/TO/CREATE/OUTPUT/DIR> -pfam <PATH/TO/HMM/DB>/pfam-A.hmm -fig pfam_full -q -clear` | aa translation - protein annotation | experimental/percent
`dogmatic -prod_hmm -i <PATH/TO/INPUT/DATA/DIR> -o <PATH/TO/CREATE/OUTPUT/DIR> -pfam <PATH/TO/HMM/DB>/pfam-A.hmm -eval 1e-5 -fig pfam_full -q -clear` | aa translation - protein annotation with adjusted chance values | experimental/percent

## Genome Sizes ##
organism | size | Mbp
---------| ---- | -------
e.coli | 4699674 | 4.7Mbp
HTCC1002 | 1345532 | 1.3Mbp
HTCC1062 | 1327458 | 1.3Mbp

# 1. Filling in the Central Dogma with `dogmatic` #
- Amino acids are essential for life. Last week we introduced amino acid coding potential by counting sense strand codon occurrences, wherein: \
\
*aacp = nt_to_aa_codons/genome*. \
\
This provided us with preliminary insight into what *possible* amino acids might be translated by a given organism. We can make some broad suggestions in regards to potential limiting nutrients and assess the potentials of different organisms to interpret how they might vary in function. This is a nice introduction to comparative genomics, however, if we stopped the story here we would be led down the wrong path. Variables such as where a codon sits along an open reading frame (ORF), mutational bias, and intergenic spacer regions will further dictate what nt sequences will code for a specific aa. So what amino acid coding potential is actually providing us is an indication of 1) aa which would potentially be coded in an abiotic environment (no life. just molecules, energy, and time) AND 2) what nt are required to fulfill these translations.
- For now let's use this measure as an abiotic "coding" control. Given that replicating life evolved ~3.6-3.8Gya we can affirm that our data was not derived from an abiotic environment because we know these sequences were derived from cultivars (life. replicating biotic forces such as transcription factors and regulation, mutational bias and *intergenic spacer regions*). Although many of us study these factors it's the fortunate truth that we can use algorithms to predict with high accuracy what sequences will code for a specific aa. *There's a program for that!* Here we will use `dogmatic` to predict protein sequences. Using Leucine, Histidine, and Glycine compare the aacp values from last week with the actualized amino acid counts or translation fraction (TF), wherein: \
\
*TF = exp_aa/genome*.

- *For this exercise consider the changes you calculate in SAR11 AND between SAR11 and e.coli*

## Leucine (Leu) (L) ##
- Leucine is the major component of the Leucine zipper (a vital protein structure in transcription promotion)
- *NOTE*: all organisms need a significant amount

### Leu ###
organism | affinity_results | affinity_aacp | exp_results | TF
---------| ---------------- | ------------- | ----------- | ---
e.coli | 214279 | 0.046 | 144440 | 0.031 |
HTCC1002 | 71211 | 0.053 | 39562 | 0.029 |
HTCC1062 | 75438 | 0.057 | 39394 | 0.029 |

## Histidine (His) (H) ##
- Histidine is one of the primary components of two-component regulatory systems (a common regulatory mechanism in prokaryotes)
- *NOTE*: minimal histidine is required for histidine kinase efficiency

### His ###
organism | affinity_results | affinity_aacp | exp_results | TF
---------| ---------------- | ------------- | ----------- | ---
e.coli | 79710 | 0.017 | ? | ? |
HTCC1002 | 18776 | 0.014 | ? | ? |
HTCC1062 | 19286 | 0.015 | ? | ? |

## Glycine (Gly) (G) ##
- Glycine is used by most organisms to simply code for proteins (as all aa). (Some organisms have evolved to use glycine in alternative forms of respiration)
- *NOTE*: one of the most abundant aa. Some organisms produce less as an evolutionary tradeoff.

### Gly ###
organism | affinity_results | affinity_aacp | exp_results | TF
---------| ---------------- | ------------- | ----------- | ---
e.coli | 149596 | 0.031 | ? | ? |
HTCC1002 | 24737 | 0.018 | ? | ? |
HTCC1062 | 25462 | 0.019 | ? | ? |

## Thought experiment: filling in the central dogma with `dogmatic` ##
1. Now having both a theoretical and experimental yield of amino acids let's revisit some of the questions from last week.
- Do the 3 organisms share any similar coding potentials?
2. `dogmatic` uses an algorithm called prodigal to predict amino acid translations. Part of the algorithm removes "false positives" (a segment from an abiotic control that doesn't actually fit into a protein prediction *fake news*)
- Given this, what might be said about the observed changes from aacp to TF? (Consider that our *abiotic* control is dependent on chance.)
	- If TF is higher (less false positives) what do you think this means in respect to biochemical significance in the organism (Look at Glycine-SAR11)?
	- If TF is lower (more false positives) what do you think this means in respect to biochemical significance in the organism?
	- Independent of yes or no, is this enough evidence to publish your work (Think about the people dancing on Mars example)?
	- Would we have a greater insight into biochemical affinity if we were to use this method on an entire amino acid sequence?


# 2. `dogmatic` and pfam annotations #
- Now that we have predicted amino acid sequences (proteins) we can begin to make sense of what functions are present in our organisms. To do so we will begin by assessing what annotations we've compiled with `dogmatic`. This program uses a database of hidden markov models (HMMs: statistical algorithms) to interpret an unobservable or "hidden" state(s) within an amino acid sequence.
	- *i.e.* Protein_A should theoretically be in 99% of organisms. The problem is that each organism has an entirely different "version" of protein_A. Furthermore, the organism-specific biotic factors that allow for the production of protein_A make it virtually impossible to equate protein_A.1 and protein_A.2 without producing chance bias (abiotic factors), however we resolve chance bias by calculating maximum-likelihood conditions. HMMs treat each new amino acid read as insufficient evidence UNTIL a given "state" has reached a maximum-likelihood of completion. The completed state is then cached into a prediction and the prediction with the most significant statistical support wins.
- `dogmatic` uses an HMM db called Protein Families Database (pfam). Our working version is pfam v33.1. pfam is constantly curated with statistical revisions and new HMMs. These methods are some of the most powerful tools we have at our disposal. The rapid use of HMM annotations has literally changed the world.
- Run `dogmatic` using one of the codes examples in the reference material. Once you have your outputs fill in the table with occurrence counts.

str | counts |
----| -------|
`Pyruvate kinase` | ? |
`B12` | ? |
`Cytochrome` | ? |
`Cytochrome c` | ? |

## Thought experiment: `dogmatic` and pfam annotations ##
1. How many of the 3 organisms have a pyruvate kinase?
2. What do think a lack of pyruvate kinase means for that organism's ability to initiate TCA cycle?
3. Why do you think we refer to aa translation - protein annotation results as an experimental/percentage yield and not just an experimental yield?
4. The `dogmatic` help menu can be prompted with `dogmatic -h`. Which option would you change if you wanted to cast a wider prediction net? (loosened support for a given state's maximum-likelihood of completion)
