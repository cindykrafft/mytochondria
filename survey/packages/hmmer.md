# HMMER

- **Category:** phylogenetics
- **Papers in survey:** 162
- **Journals:** PNAS (93), Nature (54), Cell (12), Science (3)
- **Years:** 2021 (19), 2022 (22), 2023 (30), 2024 (38), 2025 (35), 2026 (18)
- **Versions named:** 3.1b (15), 3.3.2 (14), 3.4 (6), 3.3 (4), 3.2.1 (4), 3.1 (3), 3.0 (2), 3.3.0 (1), 3.3.2d (1), 2.3.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (28), dimensionality reduction/clustering (6), machine learning (4), read trimming (2), normalisation (2), quantification (2), visualisation (2), differential/statistical testing (1), structure determination (1)

## Papers

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: For the generation of a phylogenetic tree of the Vipp1-ESCRT-III superfamily, homologs of these proteins were retrieved from Uniprot ( UniProt Consortium, 2019 ) by HMMER ( Finn et al., 2011 ) searching and from InterPro ( Mitchell et al., 2019 ) database, followed by manual inspection.
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: These searches were performed using the hmmsearch tool in HMMER3 ( Mistry et al., 2013 ), using the GA threshold defined in each Pfam HMM model.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **3.1b**
- Evidence: ...ach et al., 2020 https://bitbucket.org/berkeleylab/checkv/src/master/ MCL v14-137 van Dongen, 2000 https://www.micans.org/mcl/index.html?sec_software HMMER v3.1b2 Eddy, 1998 http://hmmer.org/ CrisprCasFinder-2.0.2 Couvin et al., 2018 https://github.com/dcouvin/CRISPRCasFinder GTDB-Tk v0.3.1 Chaumeil et al., 2019 https://github.com/Ecogenomics/GTDBTk Prodigal v2.6.3 Hyatt et al., 2010 https://githu...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: The proteins were matched against HMMs for the markers using hmmsearch ( Eddy, 2011 ), aligned with hmmalign, trimmed with clipkit ( Steenwyk et al., 2020 ), and concatenated into super alignment with the PHYling pipeline ( https://github.com/stajichlab/PHYling_unified ).
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ...11 New England Biolabs E4154 (discontinued) pBbS5k-RFP Addgene 35285 pUC-21 Addgene 49787 Plasmid DNA This study See Table S2 Software and algorithms HMMER https://www.hmmer.org v3.3.1 InterProScan ( Jones et al., 2014 ) v5.51-85.0 MAFFT ( Katoh and Standley, 2013 ) v7.475 trimAI ( Capella-Gutiérrez et al., 2009 ) v1.4 IQtree ( Minh et al., 2020 ) v2.0.4 ModelFinder ( Kalyaanamoorthy et al., 2017 ...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **3.3.2**
- Evidence: 84 http://www.iqtree.org/ MAFFT 7.475 Katoh and Standley 85 https://mafft.cbrc.jp/alignment/server/ HMMER 3.3.2 Mistry et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Genetic manipulation of Patescibacteria provides mechanistic insights into microbial dark matter and the epibiotic lifestyle. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.017 | PMCID: PMC10633639 | PMID: 37683634
- Evidence: 39 N/A hmmscan Eddy et al.
- Full pipeline: alignment/mapping [MUSCLE, minimap2] -> dimensionality reduction/clustering [R] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Flye v2.9, HMMER]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Version used: **3.3.2**
- Evidence: Phylogenetic analyses Representative sequences of CCDC22, CCDC93, COMMD1, COMMD2, COMMD3, COMMD4, COMMD5, COMMD6, COMMD7, COMMD8, COMMD9 and COMMD10 were used to construct HMM profilers (HMMER 3.3.2) which were then searched against 30 proteomes from a representative selection of organisms (from RefSeq 124 and GenBank 125 ) with an E-value threshold of 1 × 10 −5 .
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: We identified Pfam domains in each human protein from Uniprot using HMMER (e-value < 0.00001).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Evidence: 90 database with the HMMER web server 53 using one iteration, resulting in 91 sequences.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Version used: **3.2.1**
- Evidence: 112 N/A HMMER v3.2.1 Wheeler and Eddy 113 N/A IQ-TREE v1.6.12 Nguyen et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### The unique architecture of umbrella toxins permits a two-tiered molecular bet-hedging strategy for interbacterial antagonism. (Cell 2026)

- DOI: 10.1016/j.cell.2025.10.044 | PMCID: PMC13274773 | PMID: 41338195
- Evidence: 65 hmmscan program Eddy et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.8, HMMER, ImageJ, RELION v5.0, UCSF Chimera]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: Carbohydrate-active enzymes were predicted using HMMER, DIAMOND and Hotpep and only annotations made by ≥2 tools were retained.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Highly accurate protein structure prediction with AlphaFold. (Nature 2021)

- DOI: 10.1038/s41586-021-03819-2 | PMCID: PMC8371605 | PMID: 34265844
- Evidence: This dataset excludes proteins with a template (identified by hmmsearch) from the training set with more than 40% sequence identity covering more than 1% of the chain ( n = 3,144 protein chains).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [OpenMM v7.3.1] -> machine learning [HMMER, NumPy, OpenMM v7.3.1, Python, TensorFlow]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **3.1b**
- Evidence: CAZy analysis To predict CAZymes 28 from PROKKA protein output files (.faa files), hmmsearch (v.3.1b2) 101 was run against dbCAN HMMs v8 102 and an e -value cut-off of less than 1 × 10 −5 was used 102 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Prokaryotic viperins produce diverse antiviral molecules. (Nature 2021)

- DOI: 10.1038/s41586-020-2762-2 | PMCID: PMC7610908 | PMID: 32937646
- Version used: **3.2.1**
- Evidence: A homology based-search was performed on the non-redundant eukaryotic proteins database of NCBI using HMMER 3.2.1 33 in the MPI bioinformatics toolkit 34 with 205 non redundant pVips as a seed.
- Full pipeline: stage not stated [HMMER v3.2.1, IQ-TREE]

### Borgs are giant genetic elements with potential to expand metabolic capacity. (Nature 2022)

- DOI: 10.1038/s41586-022-05256-1 | PMCID: PMC9605863 | PMID: 36261517
- Evidence: The coding sequences from this study were searched against Cas gene sequences reported from previous studies 44 using hmmsearch with E < 1 × 10 −5 to identify the full locus.
- Full pipeline: alignment/mapping [BLAST, IQ-TREE v1.6.6, MAFFT, SciPy] -> quantification [SciPy] -> visualisation [BLAST, IQ-TREE v1.6.6, MAFFT] -> stage not stated [HMMER]

### Cryo-EM structure of a type IV secretion system. (Nature 2022)

- DOI: 10.1038/s41586-022-04859-y | PMCID: PMC9259494 | PMID: 35732732
- Evidence: Six rounds of iterative HMMER 67 search with e-value cut-offs of 10 −12 , 10 −12 , 10 −12 , 10 −12 , 10 −6 and 10 −3 , respectively, were used.
- Full pipeline: registration [CTFFIND v4.1] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX v1.18.2, RELION v3.1] -> machine learning [AlphaFold] -> stage not stated [ChimeraX v1.1, HMMER, PyMOL v2.3.2]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **3.1b**
- Evidence: To identify other FkbM-family proteins involved in natural product biosynthesis, the FkbM-family methyltransferase HMM (Methyltransf_21.HMM in Pfam_A) was used to query all protein-coding sequences in MIBiG (v.2.0) 30 using hmmsearch in HMMER v.3.1b2 ( http://hmmer.org/ ) with the default parameters and the --cut_nc PFAM noise cut-off.
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Plant carbonic anhydrase-like enzymes in neuroactive alkaloid biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-06716-y | PMCID: PMC10700139 | PMID: 37938780
- Evidence: Protein sequences encoded by each transcript were annotated with the best-hit Pfam term 54 using HMMER ( http://hmmer.org/ ).
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [edgeR] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold v1.5.2, HMMER]

### Unraveling the functional dark matter through global metagenomics. (Nature 2023)

- DOI: 10.1038/s41586-023-06583-7 | PMCID: PMC10584684 | PMID: 37821698
- Version used: **3.1**
- Evidence: Pfam hits (v.31) were detected with the use of the hmmsearch tool (HMMER v.3.1 package) 34 using the default trusted cut-off.
- Full pipeline: alignment/mapping [Clustal Omega, Python] -> dimensionality reduction/clustering [Clustal Omega] -> differential/statistical testing [R] -> stage not stated [AlphaFold, HMMER v3.1, ggplot2]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Version used: **3.3**
- Evidence: Component 6,732 We have built the Pfam family PF22187 (named DUF6946) using component 6,732 sequences and iteratively searching for homologues using HMMER (v.3.3) 69 .
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Version used: **3.3.2**
- Evidence: 23 ) and converted into a hmm profile using HMMER v.3.3.2 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Genome expansion by a CRISPR trimmer-integrase. (Nature 2023)

- DOI: 10.1038/s41586-023-06178-2 | PMCID: PMC10284694 | PMID: 37316664
- Evidence: The coding sequences were searched against the DEDDh model using hmmsearch with E < 1 × 10 −5 (ref.
- Full pipeline: structure determination [AlphaFold, Coot v0.9.4.1, PHENIX v1.19.2] -> machine learning [Topaz] -> stage not stated [ChimeraX, HMMER]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Evidence: Identification of orthologues in other species For each of the 291 orthologues, we aligned the proteins using MAFFT (v.7.310) 100 , built a hidden Markov Model using hmmbuild in hmmer (v.3.3.2) 101 , then found the best match using hmmsearch in the proteins of the genomes of other species, including the ctenophore B. microptera , the cladorhizid sponge, T. adhaerens 102 , H. vulgaris 12 , N. vecte...
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### Profiling the human intestinal environment under physiological conditions. (Nature 2023)

- DOI: 10.1038/s41586-023-05989-7 | PMCID: PMC10191855 | PMID: 37165188
- Evidence: CAZyme genes were identified using run_dbcan.py (v.3.0.5) 64 with default parameters (searching with HMMER, eCAMI and DIAMOND).
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DADA2, DESeq2, R, limma v3.48.3] -> stage not stated [Bowtie2 v2.4.1, HMMER, phyloseq]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: Diversity of DNA-dependent RNApolB genes We used HMMER 47 v3.1b2 to detect genes matching to the DNA-dependent RNApolB among all 2,550 metagenomic blocks on the basis of a single HMM model.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.3.2**
- Evidence: We used HMMER (v.2.3.2) 76 to identify protein domains using Trinotate’s PFAM-A database and signalP (v.4.1) 77 to predict signal peptides.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Undecaprenyl phosphate translocases confer conditional microbial fitness. (Nature 2023)

- DOI: 10.1038/s41586-022-05569-1 | PMCID: PMC9876793 | PMID: 36450355
- Evidence: In a related effort, to identify annotation-independent homologues of vca0040 , we used a HMMER search with the VCA0040 sequence from wild-type V. cholerae (Supplementary Table 2 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.3] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, ImageJ v1.53, InterProScan, featureCounts]

### Anti-viral defence by an mRNA ADP-ribosyltransferase that blocks translation. (Nature 2024)

- DOI: 10.1038/s41586-024-08102-8 | PMCID: PMC11618068 | PMID: 39443800
- Evidence: Hidden Markov model profiles of CmdT and CmdC were downloaded from DefenseFinder 50 and searched against the RefSeq non-redundant protein database using hmmscan and default parameters.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, NumPy, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, HMMER]

### Diverse anti-defence systems are encoded in the leading region of plasmids. (Nature 2024)

- DOI: 10.1038/s41586-024-07994-w | PMCID: PMC11541004 | PMID: 39385022
- Evidence: Relaxase/ traM and oriT detection Detection of relaxase and traM relaxosome genes was performed using hmmsearch 68 ( e value threshold 10 −6 ) against all the proteins in our dataset.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [ChimeraX] -> stage not stated [BLAST, HMMER, Prokka]

### Growth of complete ammonia oxidizers on guanidine. (Nature 2024)

- DOI: 10.1038/s41586-024-07832-z | PMCID: PMC11410670 | PMID: 39143220
- Evidence: Predicted proteins from all publicly available genomes in GenBank as of 1 July 2022 (429,896 genomes) were screened with hmmsearch 59 using ‘collection HMMs’ for genes related to guanidine metabolism (Fig.
- Full pipeline: alignment/mapping [ImageJ v1.54f] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ImageJ v1.54f, PyMOL, phytools] -> stage not stated [AlphaFold, BEDTools, HMMER]

### A virally encoded tRNA neutralizes the PARIS antiviral defence system. (Nature 2024)

- DOI: 10.1038/s41586-024-07874-3 | PMCID: PMC11464382 | PMID: 39111359
- Version used: **3.3.2**
- Evidence: Domains were detected by HMMsearch (from HMMER 3.3.2) on the E. coli B185 PARIS system, and a first alignment using Mafft v.7.505 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HMMER v3.3.2, MUSCLE v5.1] -> structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.7, SPAdes]

### Bridge RNAs direct programmable recombination of target and donor DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07552-4 | PMCID: PMC11208160 | PMID: 38926615
- Evidence: Two Pfam domains DEDD_Tnp_IS110 (PF01548) and Transposase_20 (PF02371) were used to search against these clustered representative proteins using the hmmsearch tool in the hmmer package 53 .
- Full pipeline: alignment/mapping [BWA, minimap2] -> dimensionality reduction/clustering [HMMER] -> stage not stated [BEDTools, BLAST, Python]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Each branch was extracted to obtain HORhap consensus sequence and HMM further used in HMMER-based HORhap classification tool 44 to produce HORhap annotations.
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### Life-cycle-coupled evolution of mitosis in close relatives of animals. (Nature 2024)

- DOI: 10.1038/s41586-024-07430-z | PMCID: PMC11153136 | PMID: 38778110
- Version used: **3.3.2**
- Evidence: To identify putative orthologues we first searched for homologues with human proteins using phmmer (HMMER 3.3.2, November 2020; http://hmmer.org/ ) 51 .
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [HMMER v3.3.2, ImageJ, Matplotlib, NumPy, OpenCV, Python, SciPy, scikit-image]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Version used: **3.1b**
- Evidence: ...somal RNAs; the RDP classifier 77 v.2.10.2 for the taxonomic classification of predicted 16S rRNA sequences; prodigal 78 v.2.6.3 for gene prediction; HMMER v.3.1b2 ( http://hmmer.org/ ) for HMM homology searches against the Pfam database 79 ; Bowtie2 (ref.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: In the third analysis, we first identified the location of the α-satellite HOR array(s) in each genome assembly using RepeatMasker 65 (v.4.1.0) followed by HumAS-HMMER ( https://github.com/fedorrik/HumAS-HMMER_for_AnVIL ) and subsequently extracted regions enriched with ‘live’ α-satellite HORs (denoted with an ‘L’ in the HumAS-HMMER BED file).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre. (Nature 2024)

- DOI: 10.1038/s41586-024-07180-y | PMCID: PMC10972752 | PMID: 38480893
- Version used: **3.1b**
- Evidence: Identification of RCI-associated genes We searched for RCI-associated gene homologues in the genomes of strains L227-S17 and L227-5C using hmmsearch (v3.1b2) 85 and profile hidden Markov models (HMMs) downloaded from Pfam 86 .
- Full pipeline: read trimming [DADA2 v1.10.0] -> alignment/mapping [Clustal Omega v1.2.3, featureCounts] -> stage not stated [HMMER v3.1b, IQ-TREE v1.6.9, QIIME 2 v2019.10]

### Automated model building and protein identification in cryo-EM maps. (Nature 2024)

- DOI: 10.1038/s41586-024-07215-4 | PMCID: PMC11006616 | PMID: 38408488
- Evidence: These vectors are converted into a hidden Markov model (HMM) profile that is used for a search against the input sequences using HMMER 32 .
- Full pipeline: stage not stated [AlphaFold, HMMER, PHENIX]

### A new family of bacterial ribosome hibernation factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07041-8 | PMCID: PMC10901736 | PMID: 38355796
- Evidence: Evolutionary analysis of Balon To assess phylogenetic distribution of Balon in bacterial species, we carried out three iterations of homology search using the sequence of Balon from P. urativorans (UniProt ID A0A0M3V8U3 ) as an input for a profile hidden Markov model-based analysis with HMMER.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, Coot v0.8.9.2, UCSF Chimera v1.14] -> stage not stated [ChimeraX v1.4, HMMER, PHENIX v1.20.1, RELION v3.1]

### Functional and evolutionary significance of unknown genes from uncultivated taxa. (Nature 2024)

- DOI: 10.1038/s41586-023-06955-z | PMCID: PMC10849945 | PMID: 38109938
- Evidence: (2) Pfam-A 59 , using HMMER 60 hmmsearch against all protein sequences of each family.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega, DIAMOND] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [R] -> structure determination [Clustal Omega] -> stage not stated [ColabFold, HMMER, eggNOG]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Version used: **3.4**
- Evidence: The incidence of nblA and psbA genes in the genomes was assessed by searching ORFs (between stop codons) with hmmsearch from HMMER (v.3.4) 91 using a custom NblA profile (see below) and the PsbA profile TIGR01151.1 from NCBI Protein Family Models.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: 75 ) using Hmmer 76 (v.3.3.1) hmmscan (-E 1e-9).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Microbial iron oxide respiration coupled to sulfide oxidation. (Nature 2025)

- DOI: 10.1038/s41586-025-09467-0 | PMCID: PMC12545173 | PMID: 40866705
- Evidence: This cut-off was embedded in the HMMER profile HMM file as the gathering threshold of the model (HMMER User’s Guide, p.
- Full pipeline: alignment/mapping [MAFFT v7.407, RAxML v8.2.12] -> structure determination [RAxML v8.2.12] -> visualisation [R v4.1] -> stage not stated [AlphaFold v2.3.2, AutoDock Vina v1.1.2, DESeq2 v3.19, HMMER, ImageJ, featureCounts]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **3.3.2d**
- Evidence: The Yq12 repeat annotations were generated using HMMER (v.3.3.2dev) 104 , and identification of Alu insertions was performed as previously described 23 .
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Version used: **3.3.2**
- Evidence: An HMM profile was constructed from the alignment using hmmbuild in HMMER (v.3.3.2) and used to search combined species proteomes with hmmsearch ( E < 1 × 10 −5 ) to identify additional homologs.
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: One asterisk indicates previously characterized; two asterisks indicate characterized in this study. f , Phylogenetic tree of FoTO1 homologues identified by HMMER.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: Next, to identify DRT9 systems that encode a SLATT domain-containing gene, we predicted ORFs in each DRT9 locus using Eggnogg Mapper 37 and used HMMER 38 to search the resulting ORFs with a previously built hidden Markov model (PFAM: PF18160).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **3.3.2**
- Evidence: To assess domain content, each of the Cannabis proteomes was aligned to the Pfam-A.hmm database (last modified 15 November 2021; accessed 20 September 2022) 140 with hmmscan (HMMER 3.3.2 November 2020) 141 on default settings.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **3.1**
- Evidence: BUSCO genes Genome assembly for each isolate was benchmarked with BUSCO (v.5.2.2) (hmmsearch v.3.1 and metaeuk v.5.34c21f2) using the option -m genome flag for the Kingdom fungi odb10 database from orthoDB (v.10).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: These markers were identified in genomes of 411 Asgard archaea and the outgroup by searching against a self-built database composed of all arCOG 63 sequences as well as partial sequences from COG 64 , AsCOG 5 , Pfam 65 and TIGRFAMs 65 , using either BLASTP 66 or HMMER 67 .
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **3.1b**
- Evidence: Relevant A. thaliana orthologous genes containing the required domains were retrieved from TAIR ( https://www.arabidopsis.org ), and profile hidden Markov models (HMMs) were constructed using HMMER (v.3.1b1) on the basis of multiple sequence alignments generated by MAFFT (v.7.475).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: The Yq12 repeat annotations were generated using HMMER 108 (v.3.3.2dev) with published DYZ1 , DYZ2 , DYZ18 , 2k7bp and 3k1bp sequences 52 , followed by manual checking of repeat unit orientation and distance from each other.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: The generated alignment file was converted to Stockholm format using an online sequence conversion tool ( http://sequenceconversion.bugaco.com/converter/biology/sequences/ ), which then served as the input for constructing an HMM file using the ‘hmmbuild’ function in HMMER 94 (v.3.1b2).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Site-saturation mutagenesis of 500 human protein domains. (Nature 2025)

- DOI: 10.1038/s41586-024-08370-4 | PMCID: PMC11754108 | PMID: 39779847
- Evidence: Domains with homology to protein domains in the Megascale dataset were defined using hmmer ( http://hmmer.org/ ) hmmscan against PFAM, and predictors were evaluated on a homologue-free set to prevent leakage from ThermoMPNN training.
- Full pipeline: machine learning [HMMER] -> stage not stated [AlphaFold, R]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Evidence: Evolutionary age of the ZBTB18 gene To evaluate the evolutionary age of the ZBTB18 gene, we used protein sequence similarity (BLASTP 80 and HMMER 81 ) to search our reference database, which is adapted from UniProt 82 and trimmed with a taxonomically informed procedure that optimizes database size while ensuring that species with well-resolved genomes are kept in all major branches of the phylogen...
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: Genes are annotated with Prodigal and coloured on the basis of statistically significant sequence similarity to natural proteins (hmmscan E-value < 0.001). h , The fraction of Prodigal-annotated genes with hmmscan hits between Evo 2 40B and M. genitalium generated by Evo 1. i , Distribut i on of Prodigal-annotated genes from Evo 2-generated M. genitalium compared with the natural genome. j , Distr...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### A membrane-bound nuclease directly cleaves phage DNA during genome injection. (Nature 2026)

- DOI: 10.1038/s41586-026-10207-1 | PMCID: PMC13190303 | PMID: 41741653
- Evidence: Representative examples of SNIPE homologues with distinct N-terminal regions, predicted by HMMER, are shown as schematics.
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> stage not stated [Fiji, HMMER, ImageJ]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Evidence: However, traditional sequence-based searches (PSI-BLAST, HMMER) were unable to identify a metazoan homologue of these proteins.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **3.3.2**
- Evidence: Homologues were aligned with MAFFT (v.7.520, ‘auto’), and hidden Markov model (HMM) profiles were built with HMMER (v.3.3.2, hmmbuild).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: Short-read 16S rRNA gene classification Hidden Markov models (HMM) were made from Rfam 104 v.14.7 seed alignments for Archaea (RF01959), Bacteria (RF00177) and Eukarya (RF01960) using hmmbuild (HMMER 105 v.3.3.2).
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Dated gene duplications elucidate the evolutionary assembly of eukaryotes. (Nature 2026)

- DOI: 10.1038/s41586-025-09808-z | PMCID: PMC12872463 | PMID: 41339551
- Version used: **3.3.2**
- Evidence: Identifying candidate gene families Candidate pre-LECA duplications were identified with the domain origins (DO) pipeline, which consists of the following steps: sequence retrieval (HMMER, v.3.3.2 76 ), filtering and aligning (MAFFT, v.7.508 77 ) these sequences, building new HMMs for iterating this search, clustering the results (MCL, v.22-282 78 ), selecting representatives to produce a represen...
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508] -> dimensionality reduction/clustering [HMMER v3.3.2, MAFFT v7.508] -> visualisation [Matplotlib, seaborn]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **3.4**
- Evidence: We used the hmmsearch command (with the —cut_ga flag) from HMMER (v.3.4; ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Evidence: We mapped the markers to the S. cerevisiae reference proteome using phmmer from the HMMER suite of tools 58 and removed 13 markers that returned the same best hit as other markers in the dataset, resulting in a set of 1,277 markers.
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Version used: **3.3.0**
- Evidence: To evaluate the frequency with which each prompt type generated toxin and antitoxin sequences, remaining protein sequences following sequence complexity and pDockQ filtering (see ‘T2TA sampling and filtering’) were evaluated using HMMER (v3.3.0) hmmscan ( https://hmmer.org ) against the Pfam-A database (v35.0) 79 , 80 .
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### An ancient antimicrobial protein co-opted by a fungal plant pathogen for in planta mycobiome manipulation. (PNAS 2021)

- DOI: 10.1073/pnas.2110968118 | PMCID: PMC8670511 | PMID: 34853168
- Evidence: The alignment as shown in B and C displays the most conserved region of the CSαβ defensin protein family and was performed using HMMER and visualized with Espript3.
- Full pipeline: alignment/mapping [HMMER, SAMtools] -> quantification [ImageJ, R v3.6.1, phyloseq] -> differential/statistical testing [DESeq2] -> visualisation [HMMER]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: To identify members of the R2R3-MYB gene family in eight diploid Fragaria species, the hidden Markov model (HMM) profile for the MYB binding domain (PF00249) retrieved from the Pfam 3.0 database (pfam.xfam.org/) was used to search the Fragaria genomes using the hmmscan program of HMMER (hmmer.org/).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Gram-negative outer-membrane proteins with multiple β-barrel domains. (PNAS 2021)

- DOI: 10.1073/pnas.2104059118 | PMCID: PMC8346858 | PMID: 34330833
- Evidence: One is based on the HMMER ( 16 ) search engine and the other based on PsiBLAST ( 17 ).
- Full pipeline: stage not stated [HMMER]

### A squalene-hopene cyclase in <i>Schizosaccharomyces japonicus</i> represents a eukaryotic adaptation to sterol-limited anaerobic environments. (PNAS 2021)

- DOI: 10.1073/pnas.2105225118 | PMCID: PMC8364164 | PMID: 34353908
- Evidence: HMMER hits with an E-value below 1 × 10 −5 , and a total alignment length (query coverage) exceeding 75% of the query sequence were considered significant.
- Full pipeline: read trimming [RAxML v0.8.1] -> alignment/mapping [HMMER, MAFFT v7.402, RAxML v0.8.1] -> stage not stated [Flye v2.7.1, Pilon v1.18]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Version used: **3.3**
- Evidence: All ORFs were also annotated with Pfam domains ( 72 ) using HMMER v3.3 ( 73 ) (parameters in SI Appendix , SI Methods ).
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### Systematic mining of fungal chimeric terpene synthases using an efficient precursor-providing yeast chassis. (PNAS 2021)

- DOI: 10.1073/pnas.2023247118 | PMCID: PMC8307374 | PMID: 34257153
- Evidence: Putative TSs were identified by searching all predicted amino acid sequences containing HMMER against the Pfam database ( http://pfam.xfam.org , version 28.0).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [HMMER]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Version used: **3.1b**
- Evidence: Predicted genes were functionally annotated using 1) CAZy database from dbCAN v6 ( 90 ) and HMMER 3.1b2 ( 91 ), 2) KEGG [Release 2015-10-12; ( 92 , 93 )], and 3) eggNOG v4.5 ( 94 ), both using BLAST 2.2.28+.
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: HMMER 3 ( 80 ) was used to identify OSC homolog genes.
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### HBD1 protein with a tandem repeat of two HMG-box domains is a DNA clip to organize chloroplast nucleoids in <i>Chlamydomonas reinhardtii</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2021053118 | PMCID: PMC8157925 | PMID: 33975946
- Evidence: We searched for proteins with multiple HMG-box domains by hmmscan search ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [MrBayes, R, RAxML] -> stage not stated [HMMER, ImageJ]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Version used: **3.1**
- Evidence: HMMER (v3.1) ( 65 ) was used to determine how many of the 18, postnatal day 154, information-rich CAZymes could be detected in recipients of the representative DR and FF microbiomes.
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Diel transcriptional oscillations of light-sensitive regulatory elements in open-ocean eukaryotic plankton communities. (PNAS 2021)

- DOI: 10.1073/pnas.2011038118 | PMCID: PMC8017926 | PMID: 33547239
- Version used: **3.1b**
- Evidence: Hmmsearches (HMMER version 3.1b2; parameters: -E 0.001) ( 46 ) on a reference database containing 907 marine-relevant genomes and transcriptomes obtained through the Joint Genome Institute, NCBI, the Marine Microbial Eukaryote Transcriptome Sequence Project ( 111 ), and Roseobase.org , representing a total of 557 unique taxonomic reference organisms ( Dataset S1 ). hmm-identified reference sequenc...
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R] -> stage not stated [HMMER v3.1b, RAxML v8.2.8]

### FtsEX-independent control of RipA-mediated cell separation in <i>Corynebacteriales</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214599119 | PMCID: PMC9897464 | PMID: 36469781
- Evidence: First, we used the HMMER package (v3.3.2) ( 46 ) tool jackhmmer to look for homologs of Mtb RipA in all the proteomes using the GenBank sequence BAB98931.1 as query.
- Full pipeline: structure determination [IQ-TREE v2.0.6, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CCP4, ColabFold, HMMER]

### Marine viral particles reveal an expansive repertoire of phage-parasitizing mobile elements. (PNAS 2022)

- DOI: 10.1073/pnas.2212722119 | PMCID: PMC9618062 | PMID: 36256808
- Evidence: Genes predicted using prodigal ( 53 ) were annotated independently with both EggNOG ( 54 ) using eggNOG-mapper v2 ( 55 ) and VOGdb using hmmsearch ( 56 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [HMMER, IQ-TREE, Medaka, R v9.4, eggNOG, minimap2]

### Molecular convergence by differential domain acquisition is a hallmark of chromosomal passenger complex evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2200108119 | PMCID: PMC9680938 | PMID: 36227914
- Evidence: To detect homologs of BORIs and Survivin in eukaryotes, we optimized multiple-profile HMMs based on iterative reciprocal similarity searches using various tools from the HMMER package version 3.1b2 ( 52 ), similar to a strategy used in our previous work ( 19 , 53 ).
- Full pipeline: stage not stated [HMMER]

### A family of unusual immunoglobulin superfamily genes in an invertebrate histocompatibility complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207374119 | PMCID: PMC9546547 | PMID: 36161920
- Evidence: To determine whether domain 1 was similar to V-set Ig domains in Alr3–Alr38, and to explore the possibility that they were, in fact, homologous, we first used HMMER to compare each sequence to Pfam, a database of hidden Markov models for protein families ( 36 ).
- Full pipeline: alignment/mapping [AlphaFold, HISAT2] -> stage not stated [Cufflinks, HMMER]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Evidence: Seven RGA-related domains and motifs—including NB-ARC, NBS, LRR, TM, STTK, LysM, CC, and TIR—were searched by InterProScan, hmmscan, and phobius from RGAugury pipeline in annotated genes.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Trade-offs of lipid remodeling in a marine predator-prey interaction in response to phosphorus limitation. (PNAS 2022)

- DOI: 10.1073/pnas.2203057119 | PMCID: PMC9457565 | PMID: 36037375
- Evidence: MED193 PlcP via the Ocean Gene Atlas (OGA) web portal ( 18 ). plcP abundance in both metagenomes and metatranscriptomes was obtained by using hmmsearch with an expected threshold of 1e −40 normalized to the median abundance of 10 single-copy marker genes ( 70 , 71 ).
- Full pipeline: quantification [HMMER] -> normalisation [HMMER]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **3.1b**
- Evidence: To obtain quantitative measures of the completeness of the genome assembly, we used BUSCO v.3.0.2 ( 73 ) with BLAST+ v.2.2.28+, HMMER v.3.1b2, and AUGUSTUS v.3.3.2.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Co-component signal transduction systems: Fast-evolving virulence regulation cassettes discovered in enteric bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203176119 | PMCID: PMC9214523 | PMID: 35648808
- Evidence: We used six rounds of iterative HMMER ( 70 ) search with E-value cutoffs of 10 to 12, 10 to 12, 10 to 12, 10 to 12, 10 to 6, and 10 to 3, respectively.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, HMMER]

### Origin and early evolution of the plant terpene synthase family. (PNAS 2022)

- DOI: 10.1073/pnas.2100361119 | PMCID: PMC9169658 | PMID: 35394876
- Version used: **3.0**
- Evidence: The proteomes for all the datasets were searched against the Pfam-A database locally using HMMER 3.0 hmmsearch ( 50 ) with an E value of 1e-5.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [HMMER v3.0, RAxML]

### Phosphonate production by marine microbes: Exploring new sources and potential function. (PNAS 2022)

- DOI: 10.1073/pnas.2113386119 | PMCID: PMC8931226 | PMID: 35254902
- Version used: **3.1b**
- Evidence: Phosphonate biosynthesis and catabolism proteins were identified by homology to a collection of Hidden Markov Models using HMMER version 3.1b2 ( http://hmmer.org/ ) and the trusted cutoffs of each individual model.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler v3.8] -> stage not stated [HMMER v3.1b, eggNOG v4.5.1]

### Amino acid sensor conserved from bacteria to humans. (PNAS 2022)

- DOI: 10.1073/pnas.2110415119 | PMCID: PMC8915833 | PMID: 35238638
- Evidence: PF02743), we scanned proteomes of 31,910 representative bacterial and archaeal genomes from the Genome Taxonomy Database ( 19 ) with the HMMER tool ( 20 ).
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, HMMER, MAFFT, MrBayes]

### Diverse methylotrophic methanogenic archaea cause high methane emissions from seagrass meadows. (PNAS 2022)

- DOI: 10.1073/pnas.2106628119 | PMCID: PMC8892325 | PMID: 35165204
- Evidence: ...equences were predicted using prodigal 2.6.3 ( 71 ) in metagenomic mode, and amino acid sequences were subsequently searched for McrA sequences using hmmscan (of the HMMer package) ( 72 ) and McrA HMM models obtained from PFAM (PF02249.17, PF02745.15) ( 73 ) using trusted cut-offs (–cut_tc).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [MAFFT] -> stage not stated [HMMER, IQ-TREE, QGIS, SPAdes]

### The dynamic trophic architecture of open-ocean protist communities revealed through machine-guided metatranscriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2100916119 | PMCID: PMC8851463 | PMID: 35145022
- Version used: **3.1b**
- Evidence: The putative function was assigned using hmmsearch [from HMMER 3.1b2 ( 69 ) using given trusted cutoff bitscores, –cut_tc] to find the best-scoring gene family from Pfam 31.0 ( 32 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> normalisation [Trimmomatic v0.36, kallisto] -> differential/statistical testing [DESeq2] -> machine learning [XGBoost] -> stage not stated [HMMER v3.1b]

### A widely distributed phosphate-insensitive phosphatase presents a route for rapid organophosphorus remineralization in the biosphere. (PNAS 2022)

- DOI: 10.1073/pnas.2118122119 | PMCID: PMC8812569 | PMID: 35082153
- Evidence: ...ching the Tara ocean metagenome (OM-RGC_v2_metaG) and metatranscriptome (OM-RGC_v2_metaT) databases via the Ocean Gene Atlas web interface, using the hmmsearch function (stringency 1E −60 ).
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [BLAST] -> differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [HMMER, IQ-TREE]

### Ultrafast end-to-end protein structure prediction enables high-throughput exploration of uncharacterized proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2113348119 | PMCID: PMC8795500 | PMID: 35074909
- Evidence: The consensus sequences from each MSA in the BFD were extracted and scanned against the Pfam ( 49 ) and CATH-Gene3D ( 38 , 50 ) HMM libraries using hmmscan ( 51 ) in order to filter out regions corresponding to well-characterized protein families.
- Full pipeline: stage not stated [AlphaFold, HMMER, PyTorch, RoseTTAFold]

### Epistatic models predict mutable sites in SARS-CoV-2 proteins and epitopes. (PNAS 2022)

- DOI: 10.1073/pnas.2113118119 | PMCID: PMC8795541 | PMID: 35022216
- Evidence: Protein domains were detected using the HMMER suite (ref.
- Full pipeline: stage not stated [HMMER, Jupyter, Nextstrain, R]

### Insight into the symbiotic lifestyle of DPANN archaea revealed by cultivation and genome analyses. (PNAS 2022)

- DOI: 10.1073/pnas.2115449119 | PMCID: PMC8784108 | PMID: 35022241
- Evidence: 4.5.1) ( 52 ), hmmscan against Pfam ( 53 ), and MEROPS ( 54 ).
- Full pipeline: stage not stated [HMMER, Prokka v1.13, RAxML, eggNOG v4.5.1]

### Radiation and temperature drive diurnal variation of aerobic methane emissions from Scots pine canopy. (PNAS 2023)

- DOI: 10.1073/pnas.2308516120 | PMCID: PMC10756279 | PMID: 38127980
- Evidence: No mcrA homologs were detected via HMMER screening in any of the samples ( SI Appendix , Table S3 ).
- Full pipeline: differential/statistical testing [R v4.2.1, lme4 v1.1] -> stage not stated [HMMER, emmeans]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **3.3**
- Evidence: 72 , were identified in the RefSeq strains and an Enterobacter cloacae outgroup (accession number GCF_003204095.1) using HMMER v3.3 (option --cut_ga) ( 73 ).
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Diversity, evolution, and classification of the RNA-guided nucleases TnpB and Cas12. (PNAS 2023)

- DOI: 10.1073/pnas.2308224120 | PMCID: PMC10691335 | PMID: 37983496
- Evidence: These aligned regions were converted into two TnpB HMM profiles for HMMER and HHSearch ( 50 – 52 ).
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold]

### Loss of Pde1 function acts as an evolutionary gateway to penicillin resistance in <i>Streptococcus pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2308029120 | PMCID: PMC10576035 | PMID: 37796984
- Version used: **3.2.1**
- Evidence: These were exported from the PubMLST database and multiple sequence alignments were produced from the nucleotide sequences using HMMER v.3.2.1.
- Full pipeline: alignment/mapping [Clustal Omega, HMMER v3.2.1] -> stage not stated [Python, SPAdes v3.15.5]

### Origin of the OAS-RNase L innate immune pathway before the rise of jawed vertebrates via molecular tinkering. (PNAS 2023)

- DOI: 10.1073/pnas.2304687120 | PMCID: PMC10400998 | PMID: 37487089
- Evidence: For the identification of OAS homologs, we used HMMER, BLASTP, or TBLASTN algorithms to search against the proteomes or genomes of cellular organisms with NTase domain (accession: PF01909) sequences as seeds or queries and an e cutoff value of 10 −5 ( 50 ).
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> structure determination [MAFFT] -> stage not stated [AlphaFold, HMMER, IQ-TREE v2.0]

### Horizontal gene transfer underlies the painful stings of asp caterpillars (Lepidoptera: Megalopygidae). (PNAS 2023)

- DOI: 10.1073/pnas.2305871120 | PMCID: PMC10629529 | PMID: 37428925
- Evidence: For example, U-MPTX 8 -Mo12 is annotated by the HMMER algorithm as belonging to the protein family (Pfam) “Insecticidal Crystal Toxin p42” with E value 8.4e −3 , and U-MPTX 8 -Mo15 is annotated by HMMER to belong to the related Pfam “ Clostridium Epsilon Toxin ETX/ Bacillus Mosquitocidal Toxin MTX” with E value 2.2e −2 .
- Full pipeline: stage not stated [BLAST, HMMER]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Evidence: Pfam domains in the downloaded sequences were detected using the Pfam database (version 34) and the hmmscan program ( 77 ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### The cell envelope of <i>Thermotogae</i> suggests a mechanism for outer membrane biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2303275120 | PMCID: PMC10160955 | PMID: 37094164
- Evidence: HMM searches were performed using HMMER with default hmmsearch settings ( http://hmmer.org/ ), and PSI-BLAST searches were conducted using four iterations and an E value of 1e − 10 .
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ChimeraX, HMMER, IQ-TREE v2.1.4, ImageJ, RoseTTAFold]

### Marginal specificity in protein interactions constrains evolution of a paralogous family. (PNAS 2023)

- DOI: 10.1073/pnas.2221163120 | PMCID: PMC10160972 | PMID: 37098061
- Evidence: EnvZ, RstB, and CpxA homologs from the ProGenomes2.0 database were identified and aligned using HMMER; specifically, jckhmmer was used to iteratively search the database for matches to the three kinase domain sequences.
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [Python, SciPy]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Version used: **3.1b**
- Evidence: IV) To detect distantly related MCP genes, an iterative search of the above gene clusters was conducted with JackHMMER (HMMER 3.1b2).
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### A general mechanism for transcription bubble nucleation in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220874120 | PMCID: PMC10083551 | PMID: 36972428
- Evidence: Sequences of σ N were collected using the HMMER webserver ( 47 ).
- Full pipeline: quantification [ImageJ] -> normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [ChimeraX, Coot, RELION v3.1] -> stage not stated [HMMER, PHENIX]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **3.3.2**
- Evidence: Leggt Pfam ( 61 ) domains (PF01019.24) were retrieved from BLAST homologues with at least 40% Pfam query coverage via hmmsearch v3.3.2.
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Pangenomic analysis reveals plant NAD<sup>+</sup> manipulation as an important virulence activity of bacterial pathogen effectors. (PNAS 2023)

- DOI: 10.1073/pnas.2217114120 | PMCID: PMC9963460 | PMID: 36753463
- Evidence: For HMMER ( http://hmmer.org/ ) analysis, Pfam seed alignments for enzyme families (listed in SI Appendix , Table S1 ) were obtained from Pfam ( http://pfam.xfam.org/ ) (downloaded on December 1, 2020).
- Full pipeline: alignment/mapping [Clustal Omega, HMMER] -> stage not stated [AlphaFold]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Evidence: MAC and MIC-limited genes were predicted with “Intronarrator” ( https://github.com/Swart-lab/Intronarrator ) and functionally annotated using HMMER3 (hmmscan) ( 58 ), Pannzer2 ( 59 ), and eggNOG ( 60 ).
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Evidence: To identify autonomous and nonautonomous TEs, repeats were scanned for functional domains against the Database of Protein Families (PFAM; release 35.0) and Conserved Domains Database (CDD; release 3.19) databases, using hmmsearch and rpsblast, respectively ( 98 , 99 , 100 and 101 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### Proteomic analysis of the sponge Aggregation Factor implicates an ancient toolkit for allorecognition and adhesion in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2409125121 | PMCID: PMC11670116 | PMID: 39693348
- Evidence: We also searched the additional sponges using an HMM of the C-termini with hmmsearch in HMMER3 (v3.1b2).
- Full pipeline: read trimming [PyMOL, Trimmomatic] -> stage not stated [AlphaFold, BUSCO, HMMER]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Version used: **3.0**
- Evidence: Both the insect and noninsect arthropod databases were searched against the Pfam database (version 35.0; pfam-legacy.xfam.org ) using HMMER 3.0 ( http://hmmer.org ).
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Version used: **3.1b**
- Evidence: The “hmmscan” in HMMER (v3.1b2) was used for identification and E-value <10 −5 .
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Soil viral-host interactions regulate microplastic-dependent carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2413245121 | PMCID: PMC11551317 | PMID: 39467127
- Evidence: Then, approximately 60 to 70% of vOTUs were annotated and classified by the gene-sharing network method (vcontact2) ( 36 ) referring to public database and protein sequence alignments (hmmscan) with ViPhOG ( 37 ) database ( Dataset S3 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BLAST, Bowtie2, HMMER] -> quantification [Bowtie2] -> stage not stated [DESeq2, R v4.0.3, vegan]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Evidence: BLAST and HMMER results were performed and parsed using the AMOEBAE workflow using a maximum e-value of 0.05 and a minimum difference in e-value order of magnitude of 2 ( 65 ), while JackHMMER results were parsed using in-house scripts (available on Figshare: https://figshare.com/s/a229953e902ebfca95fb ).
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### SHARK enables sensitive detection of evolutionary homologs and functional analogs in unalignable and disordered sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2401622121 | PMCID: PMC11494347 | PMID: 39383002
- Evidence: The performance of SHARK-dive was benchmarked on a withheld testing set of sequence families against 1) local alignment with commonly used matrices such as BLOSUM62 and PAM30 as well as a series of disorder-specific matrices [EDSSMAT, ( 56 )], and 2) widely used alignment-based homology prediction tools BLAST ( 8 ) and HMMER ( 80 ).
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [BLAST]

### Emergent time scales of epistasis in protein evolution. (PNAS 2024)

- DOI: 10.1073/pnas.2406807121 | PMCID: PMC11459137 | PMID: 39325427
- Evidence: The natural MSAs were generated running the hmmsearch command from the HMMer software suite on the UniProt database.
- Full pipeline: stage not stated [HMMER]

### &lt;i&gt;Prevotella&lt;/i&gt; are major contributors of sialidases in the human vaginal microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2400341121 | PMCID: PMC11388281 | PMID: 39186657
- Version used: **3.3.2**
- Evidence: We used HMMER (v3.3.2) to find ribosomal proteins, aligned the sequences with MAFFT (v7.508) and used RAxML (v.8.2.10) to create the phylogenetic trees.
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508, RAxML v8.2.10] -> stage not stated [AlphaFold, InterProScan, Python]

### &lt;i&gt;Lactobacillus&lt;/i&gt; Firm-5-derived succinate prevents honeybees from having diabetes-like symptoms. (PNAS 2024)

- DOI: 10.1073/pnas.2405410121 | PMCID: PMC11388347 | PMID: 39186650
- Version used: **3.3**
- Evidence: We used HMMER v3.3 ( http://hmmer.org/ ) to identify Frd coding genes by HMMs of the frd ABCD against the predicted protein sequences.
- Full pipeline: stage not stated [HMMER v3.3]

### Leveraging coevolutionary insights and AI-based structural modeling to unravel receptor-peptide ligand-binding mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2400862121 | PMCID: PMC11331138 | PMID: 39106311
- Evidence: The HMM profiles were then used as a query for an hmmsearch against 350 predicted proteomes across the entire plant kingdom and some unicellular algae ( 46 ).
- Full pipeline: stage not stated [AlphaFold, HMMER]

### Identification and characterization of a small-molecule metallophore involved in lanthanide metabolism. (PNAS 2024)

- DOI: 10.1073/pnas.2322096121 | PMCID: PMC11317620 | PMID: 39078674
- Evidence: Gene cluster functions were predicted using hmmscan (EMBL webserver) ( 51 , 52 ) and through NCBI BLAST ( 53 ) matches against the rhodopetrobactin BGC from R. palustris TIE-1 ( 25 ).
- Full pipeline: alignment/mapping [DESeq2, StringTie] -> dimensionality reduction/clustering [BLAST, HMMER]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Evidence: We identified related domains in the genomes of some Megaviricetes and Caudoviricetes (i.e., DNA bacteriophage) when we screened the Reference Proteomes database with HMMER ( 37 ), although we found no homologues in RNA viruses.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Multisubstrate specificity shaped the complex evolution of the aminotransferase family across the tree of life. (PNAS 2024)

- DOI: 10.1073/pnas.2405524121 | PMCID: PMC11214133 | PMID: 38885378
- Version used: **3.3.1**
- Evidence: The sequences after length filtration proceed to Pfam annotation by HMMER v3.3.1 (hmmscan with a default setting; E-value cutoff = 0.01) ( 117 ) using Pfam profile hidden Markov models obtained from Pfam v35.0 ( 46 ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [seaborn] -> simulation/modelling [AutoDock Vina v4.2.6] -> stage not stated [AlphaFold v2.1.0, HMMER v3.3.1, RAxML v1.2.0]

### CISD3/MiNT is required for complex I function, mitochondrial integrity, and skeletal muscle maintenance. (PNAS 2024)

- DOI: 10.1073/pnas.2405123121 | PMCID: PMC11145280 | PMID: 38781208
- Evidence: The entire sequence for both proteins was used, including the protein domain portions, as input parameters in Profile HMMER ( phmmer ) to produce associated HMM files and Multiple Sequence Alignment (MSA) FASTA files.
- Full pipeline: alignment/mapping [HMMER] -> simulation/modelling [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### The physical and evolutionary energy landscapes of devolved protein sequences corresponding to pseudogenes. (PNAS 2024)

- DOI: 10.1073/pnas.2322428121 | PMCID: PMC11127006 | PMID: 38739795
- Evidence: Parent protein and pseudogene protein sequences were aligned to their protein family’s hidden Markov model (HMM) profile using the HMMER software package ( 50 ).
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [OpenMM]

### A distinct, high-affinity, alkaline phosphatase facilitates occupation of P-depleted environments by marine picocyanobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2312892121 | PMCID: PMC11098088 | PMID: 38713622
- Evidence: Appropriate e-value thresholds for these HMMs were manually selected using hmmsearch on sequences from Haptophyta, Dinophyceae, Chlorophyta, and Bacillariophyta within UniprotKB.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.3, MUSCLE v3.8.31] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, HMMER, SciPy v1.10.1]

### Machine learning enables identification of an alternative yeast galactose utilization pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2315314121 | PMCID: PMC11067038 | PMID: 38669185
- Evidence: To determine presence/absence of genes in the GAL pathway in each of the genomes of the 1,154 strains included in our study, we conducted sequence similarity searches for the GAL1 , GAL7 , GAL102 , and GAL10 genes using the jackhmmer function from HMMER software, version 3.3.2 ( 59 ).
- Full pipeline: quantification [ggplot2 v3.4.2] -> machine learning [XGBoost v1.7.3, scikit-learn] -> visualisation [ggplot2 v3.4.2] -> stage not stated [HMMER, InterProScan]

### Evolution of homologous recombination rates across bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316302121 | PMCID: PMC11067023 | PMID: 38657048
- Evidence: To verify assembly completeness of the genomes, hidden Markov model profiles of 45 universal bacterial and archaeal protein markers were detected using HMMER as in refs.
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> differential/statistical testing [R] -> simulation/modelling [R] -> stage not stated [HMMER, RAxML]

### What one genus of showy moths can say about migration, adaptation, and wing pattern. (PNAS 2024)

- DOI: 10.1073/pnas.2319726121 | PMCID: PMC11047066 | PMID: 38630713
- Evidence: FMOs and cytochrome P450s encoded by these Arctiinae genomes were identified by mapping each protein to the PFAM database ( 54 ) by HMMER ( 55 ).
- Full pipeline: alignment/mapping [AlphaFold, BUSCO, HMMER, IQ-TREE v1.6.12, MAFFT] -> stage not stated [scikit-learn]

### Carbon starvation raises capacities in bacterial antibiotic resistance and viral auxiliary carbon metabolism in soils. (PNAS 2024)

- DOI: 10.1073/pnas.2318160121 | PMCID: PMC11032446 | PMID: 38598339
- Evidence: To estimate the functions related to organic C metabolisms, the ORFs were annotated against the Carbohydrate-Active enZYmes database (CAZy database) using hmmscan-parser.sh ( https://bcb.unl.edu/dbCAN2/download/Databases/dbCAN-old@UGA/ ) with default parameters.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [BLAST v2.5.0] -> stage not stated [HMMER]

### A sodium-dependent trehalose transporter contributes to anhydrobiosis in insect cell line, Pv11. (PNAS 2024)

- DOI: 10.1073/pnas.2317254121 | PMCID: PMC10998604 | PMID: 38551840
- Evidence: To identify SSF orthologs, we submitted the amino acid sequences to hmmsearch (--domE 1e-3) ( 80 ).
- Full pipeline: quantification [Bowtie2, RSEM v1.3.1] -> stage not stated [HMMER, ImageJ v1.53t]

### Global diversity of enterococci and description of 18 previously unknown species. (PNAS 2024)

- DOI: 10.1073/pnas.2310852121 | PMCID: PMC10927581 | PMID: 38416678
- Evidence: ...tions ( 60 , 61 ); ii) the CARD database (downloaded October 2019) to annotate antibiotic-resistance genes using RGI v5.1.0 ( 62 ); iii) dbCAN (using hmmscan-parser.sh from 07/21/2015 with database v7 downloaded) to identify carbohydrate-active enzymes described in the CAZy database ( 63 , 64 ); iv) AntiSMASH v4.2.0 (run with options: “-c 16 --clusterblast --subclusterblast --knownclusterblast --b...
- Full pipeline: alignment/mapping [IQ-TREE v1.7, MAFFT, Pilon v1.23] -> dimensionality reduction/clustering [HMMER, OrthoFinder v2.3.3]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Evidence: Finally, functional annotation of candidate genes is based on the Trinotate (v3.2.1) pipeline using TransDecoder (v5.5.0), TMHMM, HMMER, BLAST (v2.13.0), RNAmmer (v1.2), and SignalP (v4.1) with UniProt and Pfam databases ( SI Appendix , Note S4 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### Targeted hypermutation of putative antigen sensors in multicellular bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316469121 | PMCID: PMC10907252 | PMID: 38354254
- Evidence: The tree was inferred with IQ-Tree v1.5.5 ( 38 ) using the built-in model selection (optimal model: Q.pfam+F+R10) ( 80 ) and 1000 bootstrap replicates. iTOL ( 81 ) was used to visualize select conflict system-associated domains within 20 kb of the DGR RT that were identified either from the IMG annotations of PFAM domains or via hmmscan ( 82 ) ( Dataset S6 ).
- Full pipeline: read trimming [MAFFT v7.407] -> alignment/mapping [MAFFT v7.407, SAMtools, minimap2 v2.24] -> visualisation [HMMER] -> stage not stated [InterProScan]

### Structural basis and evolutionary pathways of glycerol-1-phosphate transport in marine bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2524546122 | PMCID: PMC12718374 | PMID: 41364767
- Evidence: GpxB and UgpB abundance in both metagenomes and metatranscriptomes was obtained by using hmmsearch with an expected threshold of 1e −80 normalized to the median abundance of 10 single-copy marker genes as described previously ( 43 ).
- Full pipeline: quantification [HMMER] -> normalisation [HMMER] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### Versatile NTP recognition and domain fusions expand the functional repertoire of the ParB-CTPase fold beyond chromosome segregation. (PNAS 2025)

- DOI: 10.1073/pnas.2527592122 | PMCID: PMC12704722 | PMID: 41343662
- Version used: **3.4**
- Evidence: TIGR, PFAM, and KOFAM HMM models of ParB homologues, ParB-CTPase fold, and ParA (TIGR00180.1, PF02195.22, and K03496 , respectively) were searched against each proteome database using hmmsearch (HMMER v3.4, option --cut_ga except for K03496 , e-value <1e−3).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [AlphaFold, AutoDock Vina, Docker, HMMER v3.4, IQ-TREE]

### Combined pesticide pollution enhances the dissemination of the phage-encoded antibiotic resistome in the soil under nitrogen deposition. (PNAS 2025)

- DOI: 10.1073/pnas.2516722122 | PMCID: PMC12519213 | PMID: 41042849
- Version used: **3.1b**
- Evidence: For cases where the DeePhage probability score was inconclusive (0.4 to 0.6), lysogenic marker proteins in phage sequences were identified using “hmmscan” in HMMER (v3.1b2) with an e-value threshold of 10 −5 ( 100 ).
- Full pipeline: read trimming [fastp v0.22.08] -> alignment/mapping [BLAST] -> visualisation [Cytoscape v3.10.0] -> stage not stated [HMMER v3.1b, R v4.0.3, eggNOG, vegan]

### Duplication of a conserved mitochondrial enzyme gene arms parasitoid wasps with venom cytotoxicity and oogenesis regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512820122 | PMCID: PMC12501140 | PMID: 40996803
- Evidence: All candidate genes were manually confirmed in NCBI by blastp according to the domains with the HMMER suite ( https://www.ebi.ac.uk/Tools/hmmer/ ) of Pfam ( 59 ).
- Full pipeline: quality control [fastp] -> alignment/mapping [MAFFT] -> quantification [fastp] -> structure determination [phytools] -> stage not stated [AlphaFold, BLAST, HMMER]

### Genetic dissection of nonconventional introns reveals codominant noncanonical splicing code in &lt;i&gt;Euglena&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509937122 | PMCID: PMC12501133 | PMID: 40986342
- Evidence: Open reading frames were predicted using TransDecoder-v3.0.0 ( https://transdecoder.github.io ) with the parameters: “--retain_pfam_hits, --retain_blastp_hits, and --single_best_orf”, after searches against the Pfam-A (release 30.0) dataset using HMMER-v3.1b2 and the NCBI nonredundant (nr) protein datasets using BLASTP-v2.2.30 with the parameter: “-evalue 1e−5.” Base-Pairing Sequence Prediction.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BLAST, HMMER, ImageJ]

### Evolutionarily conserved grammar rules viral factories of amoeba-infecting members of the hyperdiverse &lt;i&gt;Nucleocytoviricota&lt;/i&gt; phylum. (PNAS 2025)

- DOI: 10.1073/pnas.2515074122 | PMCID: PMC12415211 | PMID: 40864652
- Version used: **3.3.2**
- Evidence: HMM models were constructed with HMMER v3.3.2 ( 75 ).
- Full pipeline: quantification [limma] -> dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> visualisation [limma] -> stage not stated [HMMER v3.3.2, ImageJ]

### FliO is an evolutionarily conserved yet diversified core component of the bacterial flagellar type III secretion system. (PNAS 2025)

- DOI: 10.1073/pnas.2512476122 | PMCID: PMC12403147 | PMID: 40838884
- Evidence: Fabiani et al ( 16 ) employed a sequence-to-profile search tool, HMMER ( 20 ), and Hidden Markov models (HMMs) from the Pfam database ( 21 ), to scan 4,771 NCBI RefSeq genomes for the presence of FliO.
- Full pipeline: visualisation [AlphaFold, PyMOL v3.0] -> stage not stated [HMMER]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Evidence: Domain analysis used HMMER ( 54 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Anthropogenic iron alters the spring phytoplankton bloom in the North Pacific transition zone. (PNAS 2025)

- DOI: 10.1073/pnas.2418201122 | PMCID: PMC12168011 | PMID: 40455985
- Version used: **3.1b**
- Evidence: Assembled and quality-controlled environmental metatranscriptome sequences derived from the Gradients cruises ( 60 , 61 ) were queried for homology to known Fe-stress induced genes using hmmsearch (HMMER version 3.1b2; parameters: -E 0.00001) ( 62 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [kallisto] -> stage not stated [HMMER v3.1b, RAxML]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Evidence: BLASTp and HMMER search retrieved homologs of the human MN1 gene from all gnathostome lineages, including previously unreported homologs in Chondrichthyes, cartilaginous fish ( Fig.
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Functional annotation was performed using DIAMOND BLASTP against the NCBI Non-Redundant Protein Database, Swiss-Prot, and KEGG ( 37 ), while protein domain annotation was conducted using HMMER against Pfam ( 38 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Version used: **3.3.2**
- Evidence: Adding ENS3 Pol to this list, we extracted the reverse transcriptase domain using the PFAM HMMs RVT_1 and RVT_2 (PF00078.28 and PF07727.15) and the hmmsearch tool from HMMER v3.3.2 ( 89 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: To identify vitellogenin ( Vg ) and its receptor ( VgR ) genes, we utilized Bitacora v1.4 ( 94 ) in combination with homology-based tools (NCBI BLAST, HMMER, and GEMOMA) ( 95 – 97 ), manually validated candidate genes, and classified them into Vg , partial Vg ( PVg ), or Vg -like ( Vgl ) subgroups.
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### An integrated AI knowledge graph framework of bacterial enzymology and metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2425048122 | PMCID: PMC12012490 | PMID: 40193601
- Evidence: ANN-based classification achieves a 5.7-fold speed increase relative to DIAMOND and a 19.9-fold speed increase with respect to hmmscan annotation with the PFAM library when annotating 100,000 sequences ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HMMER, PyTorch, Python, SciPy]

### A conserved ARF-DNA interface underlies auxin-triggered transcriptional response. (PNAS 2025)

- DOI: 10.1073/pnas.2501915122 | PMCID: PMC12002309 | PMID: 40168121
- Evidence: AtARF1 (6ycq, chain A) was used as query for the HMMER search (1 iteration), 0.0001 E-value cutoff, UNIREF-90 database.
- Full pipeline: quality control [FastQC] -> alignment/mapping [featureCounts] -> quantification [ilastik v1.3.3] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, HMMER, PyMOL]

### Structural assembly of the PAS domain drives the catalytic activation of metazoan PASK. (PNAS 2025)

- DOI: 10.1073/pnas.2409685122 | PMCID: PMC11962487 | PMID: 40106358
- Evidence: Additionally, structure-based sequence alignments of the PASK PAC motif with PAC motif sequences from SMART, HMMER, and PDB identified the PAC motif of plant histidine kinase Phytochrome C (PhyC) as a close match ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold, ChimeraX v1.7, ColabFold, RoseTTAFold]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **3.4**
- Evidence: Briefly, the sequences of 16 ribosomal proteins within MAGs were identified using HMMER v3.4 ( http://hmmer.org ) and aligned by MUSCLE v5.1 ( 58 ).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Uncovering the hidden RNA virus diversity in Lake Nam Co: Evolutionary insights from an extreme high-altitude environment. (PNAS 2025)

- DOI: 10.1073/pnas.2420162122 | PMCID: PMC11831205 | PMID: 39903107
- Evidence: RdRP sequences were identified through a combination of BLASTp ( 95 ), HMMER searches ( 96 ), and the deep learning algorithm Lucaprot ( 8 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [BLAST, HMMER] -> visualisation [UMAP]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Version used: **3.4**
- Evidence: To reconstruct the phylogeny of CYCLOPS, we recovered protein sequences from a variety of land plants using hmmscan from HMMER v3.4 ( 40 ) with the HMM profile of the CYCLOPS domain (IPR040036).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### Novel Knotted Solenoid fold with order-shifted coil arrangement leads to nontrivial 3&lt;sub&gt;1&lt;/sub&gt; topology. (PNAS 2026)

- DOI: 10.1073/pnas.2525920123 | PMCID: PMC13123833 | PMID: 42018416
- Evidence: Subsequently, a multiple sequence alignment (MSA) was generated using MAFFT ( 63 ), which was then used with HMMER ( 41 ) to perform sequential searches across the entire AlphaFold database, e-value cutoff: 10 − 3 .
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> simulation/modelling [GROMACS v2023.1] -> stage not stated [AlphaFold]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Evidence: Next, hmmsearch ( https://hmmer.org/ ) was used to scan each proteome for the presence of OMPs using the HMM.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### Mycoviruses confer hypovirulence but enhance antifungal volatile organic compound production in a phytopathogenic fungus. (PNAS 2026)

- DOI: 10.1073/pnas.2526822123 | PMCID: PMC13080020 | PMID: 41941638
- Version used: **3.3.2**
- Evidence: For homologous sequence identification, BLASTp and Hmmsearch (HMMER 3.3.2) were employed to search against both the nr database and the clustered nr database to obtain homologous protein sequences.
- Full pipeline: alignment/mapping [ChimeraX, MAFFT v7.0] -> normalisation [ComplexHeatmap] -> dimensionality reduction/clustering [ComplexHeatmap, HMMER v3.3.2] -> visualisation [ChimeraX, ComplexHeatmap, ImageJ] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.2.6]

### Proteome-wide prediction of interactions between structured domains and peptide motifs reveals functionally coherent subnetworks. (PNAS 2026)

- DOI: 10.1073/pnas.2527957123 | PMCID: PMC13080015 | PMID: 41941631
- Evidence: The hmmscan tool from the HMMER suite (version 3.4) ( 67 ) with the Pfam-A HMM profile library searched each protein sequence for Pfam domains associated with ELM classes, and an in-house Perl script was used to search for matches to ELM class regular expressions.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [AlphaFold, HMMER, Python, R, STRING db, scikit-learn]

### Programmed meiotic errors facilitate dichotomous sperm production in the silkworm, &lt;i&gt;Bombyx mori&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2520991123 | PMCID: PMC12956816 | PMID: 41739555
- Evidence: However, d espite this annotation, the protein shares minimal homology with other CENP-E proteins and lacks both the N-terminal motor and C-terminal microtubule-binding domains ( 40 ). psiBLAST and HMMER analyses identified no clear orthologs outside insects ( 41 - 43 ), while HHpred suggests domains associated with flagellar motor function ( 44 , 45 ; Dataset S4 ), consistent with a role in sperm...
- Full pipeline: stage not stated [HMMER]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Version used: **3.4**
- Evidence: 1.2.4 ( 75 ) with default parameters and used the alignments to build HMM profiles using the hmmbuild command of HMMER v.3.4 ( http://hmmer.org/ ).
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

### Host-microbiome mutualism drives urea carbon salvage and acetogenesis during hibernation. (PNAS 2026)

- DOI: 10.1073/pnas.2518978123 | PMCID: PMC12773770 | PMID: 41481471
- Evidence: For the carbon fixation-related analyses, translated proteins from the ORF predictions were compared against the Pfam ( 12 ) profiles for enzymes involved in Wood–Ljungdahl pathway (WLP) carbon fixation, as defined by KEGG ( 13 – 15 ) using HMMER ( 16 ).
- Full pipeline: read trimming [Bowtie2 v2.2.2, Trimmomatic v0.38] -> normalisation [DESeq2, R] -> differential/statistical testing [R] -> stage not stated [HMMER]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Version used: **3.2.1**
- Evidence: We extracted the 580-bp R. ferrumequinum sequence span up to where synteny resumes to the human genome and used hmmscan (HMMER 3.2.1) ( 93 ) to search against the Dfam database ( 94 ) for transposable elements present in the sequence.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: HMMER’s hmmsearch ( 83 ) ( hmmer.org version 3.4) was used to screen these 13 HMM profiles.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Evidence: For lower quality regions that resulted in a ModelAngelo trace but poor side-chain outputs, the HMM profiles were used in HMMER searches ( 57 ) against the L. tarentolae proteome to identify proteins within densities of interest.
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

