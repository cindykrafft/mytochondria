# MUSCLE

- **Category:** phylogenetics
- **Papers in survey:** 123
- **Journals:** PNAS (77), Nature (38), Cell (6), Science (2)
- **Years:** 2021 (13), 2022 (25), 2023 (23), 2024 (29), 2025 (23), 2026 (10)
- **Versions named:** 3.8.31 (19), 5.1 (11), 3.8.1551 (8), 3.8 (4), 3.8.425 (2), 3.7 (2), 3.8.155 (1), 3.38.31 (1), 5.2 (1), 3.5 (1)
- **Pipeline stages it appears in:** alignment/mapping (119), structure determination (6), read trimming (6), dimensionality reduction/clustering (3), registration (3), visualisation (2)

## Papers

### Parasitic modulation of host development by ubiquitin-independent protein degradation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.029 | PMCID: PMC8525514 | PMID: 34536345
- Version used: **3.8.31**
- Evidence: Briefly, sequences were aligned with MUSCLE (v3.8.31) configured for highest accuracy.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> stage not stated [Fiji, ImageJ]

### Genetic manipulation of Patescibacteria provides mechanistic insights into microbial dark matter and the epibiotic lifestyle. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.017 | PMCID: PMC10633639 | PMID: 37683634
- Evidence: 72 Sequences of each of the 50 selected proteins were individually aligned using MUSCLE, then concatenated into a curated single curated multiple sequence alignment ( Data S2 ).
- Full pipeline: alignment/mapping [MUSCLE, minimap2] -> dimensionality reduction/clustering [R] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Flye v2.9, HMMER]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: 75 https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb MUSCLE v5 Edgar et al.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **5.1**
- Evidence: ...urnal.pone.0061217 https://doi.org/10.18129/B9.bioc.phyloseq eggNOG 5.0 https://doi.org/10.1093/nar/gky1085 https://github.com/eggnogdb/eggnog-mapper MUSCLE v5.1 https://doi.org/10.1038/s41467-022-34630-w https://www.drive5.com/muscle/ raxmlGUI 2.0 https://doi.org/10.1111/2041-210X.13512 https://antonellilab.github.io/raxmlGUI/ FastTree v2.1 https://doi.org/10.1371/journal.pone.0009490 http://www....
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Human coronavirus HKU1 recognition of the TMPRSS2 host receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.006 | PMCID: PMC12854727 | PMID: 38964328
- Evidence: In MEGA11 96 , these sequences were aligned using the MUSCLE algorithm and a NJ tree was constructed with 1000 bootstrap replications.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [RELION] -> structure determination [RELION, UCSF Chimera] -> stage not stated [PHENIX, Topaz]

### Encoding and decoding selectivity and promiscuity in the human chemokine-GPCR interaction network. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.046 | PMCID: PMC12435897 | PMID: 40273912
- Evidence: Fourth, full length Uniprot sequences for all 46 chemokine paralogs were independently aligned via MUSCLE.
- Full pipeline: alignment/mapping [ANNOVAR, MUSCLE, R] -> stage not stated [Cytoscape, PyMOL, TopHat]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: After removal of duplicates, sequences were clustered at 95% identity using usearch 84 v.8.0.1623 and aligned using MUSCLE 69 v.3.8.31.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Evidence: Resulting sequences were aligned by MUSCLE 88 (option: -fastaout) and poorly aligned positions and divergent regions of cDNA were eliminated by Gblocks v.0.91b 89 (options: -b4 10 -b5 n --b3 5 --t = c).
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Evidence: For phylogenetic analysis, nucleotide or protein sequences of the viruses were first aligned using the ClustalW and the MUSCLE algorithm, respectively.
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Direct activation of a bacterial innate immune system by a viral capsid protein. (Nature 2022)

- DOI: 10.1038/s41586-022-05444-z | PMCID: PMC9712102 | PMID: 36385533
- Evidence: Homologues of Gp57 (Gp8 Bas4 , Gp8 Bas5 and Gp8 Bas8 ) were aligned by MUSCLE 56 .
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> stage not stated [AlphaFold, BLAST, CCP4, PHENIX]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Evidence: Sequences were imported to MEGA-X 56 and aligned using MUSCLE with default parameters.
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **3.8.1551**
- Evidence: The summed 29 FkbM-family proteins were aligned using MUSCLE (v.3.8.1551) 81 with two outgroups involved in proteusin biosynthesis, PoyE ( AFS60641.1 ) and AerE ( AFS60641.1 ) from a different methyltransferase protein family (PF05175).
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Pre-existing polymerase-specific T cells expand in abortive seronegative SARS-CoV-2. (Nature 2022)

- DOI: 10.1038/s41586-021-04186-8 | PMCID: PMC8732273 | PMID: 34758478
- Evidence: Sequences were aligned using the MUSCLE algorithm with the default parameters and percentage identity was calculated in Geneious Prime 2020.1.2 ( www.geneious.com ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [R, ggpubr v0.4.0]

### Plant carbonic anhydrase-like enzymes in neuroactive alkaloid biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-06716-y | PMCID: PMC10700139 | PMID: 37938780
- Evidence: The downloaded CAH proteins and the CAH family proteins identified in our transcriptomic dataset (for a set of 80 proteins total) were aligned using the MUSCLE algorithm and phylogenetic trees were constructed using the neighbour-joining method (100 bootstraps) with the Jukes–Cantor genetic distance model.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [edgeR] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold v1.5.2, HMMER]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Evidence: The reduced set of sequences was aligned with MUSCLE 64 (v.5.1) and the resulting multiple sequence alignment (MSA) used as input for three independent BLASTp 65 searches over the eukaryotic, archaea and bacterial sequences in nr filtered to 70% sequence identity (nr_euk70, nr_arc70, nr_bac70) through the MPI Bioinformatics toolkit as of January 2023.
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Evidence: Multiple alignment of POLG2 protein sequence POLG2 homologues were detected using the best bidirectional BlastP hit (expected < 1 × 10 −3 ) from humans and were aligned using MUSCLE 88 .
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Small protein modules dictate prophage fates during polylysogeny. (Nature 2023)

- DOI: 10.1038/s41586-023-06376-y | PMCID: PMC10432266 | PMID: 37495698
- Evidence: Indeed, the set of non-redundant, full-length TelN proteins from these datasets aligned well using MUSCLE with default parameters 48 .
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, Prokka v1.11, Python]

### Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer. (Nature 2023)

- DOI: 10.1038/s41586-023-05945-5 | PMCID: PMC10232371 | PMID: 37259003
- Version used: **5.1**
- Evidence: Multiple sequence alignment and phylogenetic analysis LanM sequences were aligned using MUSCLE (v5.1) 45 with default parameters.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> structure determination [Coot] -> visualisation [Cytoscape v3.9.1, PyMOL, R v4.1.0] -> stage not stated [IQ-TREE v2.2.0.3]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Evidence: Sequences of sicX and ubiUVT orthologues were aligned using MUSCLE 43 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### Stigma receptors control intraspecies and interspecies barriers in Brassicaceae. (Nature 2023)

- DOI: 10.1038/s41586-022-05640-x | PMCID: PMC9908550 | PMID: 36697825
- Evidence: For the phylogenetic tree of RBOHs, PCPs and SRKs, corresponding sequences were aligned using the MUSCLE algorithm implemented in MEGA X 53 , and constructed using the neighbour-joining method in MEGA X with 1,000 bootstraps.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> stage not stated [ImageJ v1.53c]

### Circadian plasticity evolves through regulatory changes in a neuropeptide gene. (Nature 2024)

- DOI: 10.1038/s41586-024-08056-x | PMCID: PMC11602725 | PMID: 39415010
- Version used: **3.8.1551**
- Evidence: Sequences were assembled and aligned in SnapGene ( www.snapgene.com ) using MUSCLE v.3.8.1551 (ref.
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551, SAMtools v1.19.2] -> variant calling [SAMtools v1.19.2] -> visualisation [R]

### A bacterial immunity protein directly senses two disparate phage proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08039-y | PMCID: PMC11578894 | PMID: 39415022
- Evidence: Homologues of the MCPs or Gp54 Bas11 in BASEL phages were identified by BLASTp 44 searches against each phage genome, and aligned by MUSCLE 45 .
- Full pipeline: alignment/mapping [BLAST, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold]

### The ultra-high affinity transport proteins of ubiquitous marine bacteria. (Nature 2024)

- DOI: 10.1038/s41586-024-07924-w | PMCID: PMC11485210 | PMID: 39261732
- Version used: **3.8.31**
- Evidence: The resulting sequences were filtered to remove a small number of unusually long sequences (>20% greater than mean length) and aligned in MUSCLE v3.8.31 83 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> structure determination [PHENIX, REFMAC] -> stage not stated [AlphaFold]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **5.1**
- Evidence: 4 ), whole polyprotein sequences of the Bole tick virus group were aligned using MAFFT, MUSCLE (v5.1) 65 , and subalignments covering only the putative protein sequences were converted to the.a3m format and used as input for ColabFold structure prediction 19 .
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Version used: **3.8.31**
- Evidence: Each of the 3,954 hit sequences was aligned to the reference sequences using MUSCLE (v3.8.31) to check whether the Ser-Asp-His catalytic triad was contained, resulting in 1,598 aligned sequences containing the conserved catalytic triad.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### A virally encoded tRNA neutralizes the PARIS antiviral defence system. (Nature 2024)

- DOI: 10.1038/s41586-024-07874-3 | PMCID: PMC11464382 | PMID: 39111359
- Version used: **5.1**
- Evidence: The final alignment used to make the tree was carried out using MUSCLE v.5.1.linux64 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HMMER v3.3.2, MUSCLE v5.1] -> structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.7, SPAdes]

### Shifts in receptors during submergence of an encephalitic arbovirus. (Nature 2024)

- DOI: 10.1038/s41586-024-07740-2 | PMCID: PMC11324528 | PMID: 39048821
- Evidence: Phylogenetic analysis Sequences encoding the structural polyprotein (C–E3–E2–(6 K/TF)–E1) of 44 WEEV strains with full genome sequences available (Supplementary Table 1 ) were aligned in MEGA11 using the built-in MUSCLE algorithm 67 .
- Full pipeline: alignment/mapping [MUSCLE]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Version used: **3.8.31**
- Evidence: Multiple alignments of the protein sequences in each group were performed with MUSCLE (v.3.8.31) with default settings 79 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **3.8.31**
- Evidence: Phylogenetic inference and molecular dating A total of 1,086 single-copy orthologous genes were obtained from the above orthogroup sorting and were further aligned by MUSCLE (v.3.8.31) 85 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### DNA glycosylases provide antiviral defence in prokaryotes. (Nature 2024)

- DOI: 10.1038/s41586-024-07329-9 | PMCID: PMC11078745 | PMID: 38632404
- Evidence: Homologues were then subjected to a multiple sequence alignment using MUSCLE v5 with 16 maximum iterations via the Geneious Prime software.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MUSCLE, Python] -> normalisation [Python] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, ColabFold]

### Emergence of fractal geometries in the evolution of a metabolic enzyme. (Nature 2024)

- DOI: 10.1038/s41586-024-07287-2 | PMCID: PMC11041685 | PMID: 38600380
- Version used: **3.8.31**
- Evidence: Phylogenetic analysis and ancestral sequence reconstruction Amino acid sequences of 84 CS genes from Cyanobacteria and marine Gammaproteobacteria as the outgroup were collected from the NCBI Reference Sequence database and aligned using MUSCLE (v.3.8.31) 39 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MotionCor2] -> normalisation [RELION v3.1] -> simulation/modelling [GROMACS v2022.2] -> structure determination [MUSCLE v3.8.31, PHENIX v1.19.2] -> stage not stated [PyMOL v2.5.2, Topaz, UCSF Chimera]

### Divergent evolutionary strategies pre-empt tissue collision in gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09447-4 | PMCID: PMC12527943 | PMID: 40903584
- Evidence: Protein alignments were performed in Geneious by MUSCLE alignment with standard parameters.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [ImageJ, Matplotlib, NumPy, Python, SciPy, seaborn]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **3.38.31**
- Evidence: Sequence of all putative MEIs that passed filtering were re-retrieved along with a flanking sequence (±100 bp) using SAMtools (v.1.15.1) 94 , and then aligned against one another using MUSCLE (v.3.38.31) 95 to distinguish unique MEIs from duplicated insertions of MEIs residing in centromere regions (Supplementary Table 58 ).
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Evidence: Genes and protein similarities were obtained through MUSCLE alignments 115 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Electron flow in hydrogenotrophic methanogens under nickel limitation. (Nature 2025)

- DOI: 10.1038/s41586-025-09229-y | PMCID: PMC12350162 | PMID: 40604290
- Evidence: The maximum-likelihood tree is based on a MUSCLE alignment and was generated using IQ-TREE with LG + I + G4 model of evolution.
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold v3.0, MotionCor2, RELION]

### Naturally ornate RNA-only complexes revealed by cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-09073-0 | PMCID: PMC12286853 | PMID: 40328315
- Evidence: Comparative analysis and multiple alignments for isolated RNA candidates were conducted using cmalign 65 and MUSCLE (v.5) 66 with pairwise comparisons refined using the OWEN program 67 .
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [Coot v0.9.8, MUSCLE] -> visualisation [AlphaFold] -> stage not stated [ChimeraX v1.8, PHENIX, RELION]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: MEI sequences were aligned using the MUSCLE 117 (v.3.8.31) aligner.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **3.8.425**
- Evidence: Amino acid sequences were aligned using MUSCLE v.3.8.425 (ref.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **3.8.1551**
- Evidence: A pairwise alignment was produced for each pair of LTR sequences using MUSCLE (v.3.8.1551) 74 .
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Version used: **5.1**
- Evidence: The rest of the sequences in each cluster were aligned to the representative sequence using MUSCLE (v.5.1) 37 using the Parallel Perturbed ProbCons algorithm (default) or the Super5 algorithm if the cluster contained more than 100 sequences.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Version used: **3.8.31**
- Evidence: Specifically, Nxr/Nar and PmoA/AmoA amino acid reference sequences were downloaded 30 , 88 , 89 and this set of reference sequences was combined with amino acid sequences of homologues from the GROWdb, aligned separately using MUSCLE (v.3.8.31) and run through a Python script for generating phylogenetic trees (ProtPipeliner; https://github.com/WrightonLabCSU/Protpipeliner/tree/main ) 90 , 91 .
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Mechanism of co-transcriptional cap snatching by influenza polymerase. (Nature 2026)

- DOI: 10.1038/s41586-026-10189-0 | PMCID: PMC13128444 | PMID: 41781612
- Evidence: In SnapGene, 7.0.1 two MUSCLE alignments were performed for PA and PB2 (Extended Data Fig.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX v1.6.1, Coot, RELION]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Version used: **3.8.31**
- Evidence: The sequences were aligned using MUSCLE (v3.8.31) 69 and annotated using Jalview (v2.11.3.3) 70 .
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Sustained HIV-1 remission after heterozygous CCR5Δ32 stem cell transplantation. (Nature 2026)

- DOI: 10.1038/s41586-025-09893-0 | PMCID: PMC12916306 | PMID: 41326734
- Version used: **3.8.155**
- Evidence: In brief, sequences were aligned using MUSCLE (v.3.8.155) 74 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.155] -> dimensionality reduction/clustering [R v4.4.1, UMAP] -> stage not stated [MACS2, Seurat]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Version used: **3.8.31**
- Evidence: We constructed consensus sequences for each HA-related gene from HA–LA comparisons using vcf-consensus ( 69 ) based on our SNP data and aligned each HA-related gene using MUSCLE version 3.8.31 ( 85 ).
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Transposition and duplication of MADS-domain transcription factor genes in annual and perennial <i>Arabis</i> species modulates flowering. (PNAS 2021)

- DOI: 10.1073/pnas.2109204118 | PMCID: PMC8488671 | PMID: 34548402
- Evidence: For dN/dS analysis, the original MUSCLE alignment was trimmed by removing positions with more than 20% gaps and then converted into a codon alignment suitable for PAML ( 28 ).
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [BWA, MUSCLE] -> normalisation [R] -> stage not stated [DESeq2]

### Evolution of a σ-(c-di-GMP)-anti-σ switch. (PNAS 2021)

- DOI: 10.1073/pnas.2105447118 | PMCID: PMC8325347 | PMID: 34290147
- Evidence: Homologs were aligned using MUSCLE ( 49 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX, RAxML v8.2.10]

### Global biogeography of chemosynthetic symbionts reveals both localized and globally distributed symbiont groups. (PNAS 2021)

- DOI: 10.1073/pnas.2104378118 | PMCID: PMC8307296 | PMID: 34272286
- Evidence: These core genes were realigned with MUSCLE ( 81 ) and cleaned with trimAl ( 82 ) (parameters in SI Appendix , SI Methods ).
- Full pipeline: quality control [Jupyter] -> read trimming [Jupyter] -> alignment/mapping [IQ-TREE, RAxML v8.2.10] -> quantification [featureCounts] -> registration [MUSCLE] -> visualisation [IQ-TREE, R v6.3] -> stage not stated [HMMER v3.3, SPAdes v3.13.1, eggNOG]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Version used: **3.8.1551**
- Evidence: Each set of five genes (copies in the sequence of the maize B, Bd, Os, Sb, and Zm) was multiple aligned using MUSCLE v3.8.1551 ( 83 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### Transposon-mediated insertional mutagenesis unmasks recessive insecticide resistance in the aphid <i>Myzus persicae</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100559118 | PMCID: PMC8201860 | PMID: 34074777
- Version used: **3.8**
- Evidence: ( 17 ) using MUSCLE version 3.8 ( 53 ).
- Full pipeline: quality control [FastQC, Trim Galore v0.4.5] -> read trimming [FastQC] -> alignment/mapping [HISAT2 v2.1.0, HTSeq] -> differential/statistical testing [edgeR v3.9] -> stage not stated [MUSCLE v3.8]

### Herded and hunted goat genomes from the dawn of domestication in the Zagros Mountains. (PNAS 2021)

- DOI: 10.1073/pnas.2100901118 | PMCID: PMC8237664 | PMID: 34099576
- Evidence: Reads were aligned using bwa to the goat mtDNA reference ( NC_005044.2 ), before realignment to a circularized haplogroup representative, and consensus sequences generated using ANGSD; mtDNA were aligned using MUSCLE ( 76 ).
- Full pipeline: alignment/mapping [MUSCLE] -> registration [MUSCLE] -> differential/statistical testing [ANGSD] -> stage not stated [BCFtools v1.5, BEAST]

### On the evolution of chaperones and cochaperones and the expansion of proteomes across the Tree of Life. (PNAS 2021)

- DOI: 10.1073/pnas.2020885118 | PMCID: PMC8166112 | PMID: 34001607
- Version used: **3.8.31**
- Evidence: The orthologous and paralogous sequences for each chaperone family were aligned using MUSCLE v3.8.31 ( 88 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: Protein sequences from the gene pairs were aligned using MUSCLE ( 74 ).
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### Evolved increases in hemoglobin-oxygen affinity and the Bohr effect coincided with the aquatic specialization of penguins. (PNAS 2021)

- DOI: 10.1073/pnas.2023936118 | PMCID: PMC8020755 | PMID: 33753505
- Evidence: Sequences were aligned using MUSCLE ( 42 ) and then used to estimate phylogenetic trees as described previously ( 40 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [IQ-TREE, PyMOL]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: The protein sequences from these families were aligned with MUSCLE ( 82 ), and the nucleotides for each of those sequences were mapped to the protein alignment.
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Bioremediation of mercury-polluted soil and water by the plant symbiotic fungus <i>Metarhizium robertsii</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214513119 | PMCID: PMC9704736 | PMID: 36375055
- Version used: **3.7**
- Evidence: Protein sequences were aligned using MUSCLE v3.7 with default parameters ( 34 ).
- Full pipeline: alignment/mapping [MUSCLE v3.7] -> differential/statistical testing [MrBayes v3.2.5]

### Extracellular carbonic anhydrase activity promotes a carbon concentration mechanism in metazoan calcifying cells. (PNAS 2022)

- DOI: 10.1073/pnas.2203904119 | PMCID: PMC9546546 | PMID: 36161891
- Evidence: Selected sequences were aligned via the MUSCLE program and further trimmed by the Gblocks Server ( http://molevol.cmima.csic.es/castresana/Gblocks_server.html ), and the 140-aa trimmed sequences were used for the phylogenetic analysis.
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [MAFFT, MUSCLE]

### Discovery of prolactin-like in lamprey: Role in osmoregulation and new insight into the evolution of the growth hormone/prolactin family. (PNAS 2022)

- DOI: 10.1073/pnas.2212196119 | PMCID: PMC9546618 | PMID: 36161944
- Evidence: Sequences of mature proteins ( SI Appendix , Table S3 ) were aligned by the MUSCLE algorithm applied through AliView ( 48 ) software with default settings, and phylogenetic analysis was performed using the likelihood-based phylogenetic maximum likelihood method through SeaView 4.7 ( 49 ).
- Full pipeline: alignment/mapping [MUSCLE]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **3.7**
- Evidence: CDS from each single-copy family were aligned by MUSCLE v3.7 ( https://www.ebi.ac.uk/Tools/msa/muscle/ ) ( 83 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **3.8.31**
- Evidence: Single-copy gene orthogroups were aligned with MUSCLE (v3.8.31) ( 102 ) and concatenated into a superalignment.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Rats and the city: Implications of urbanization on zoonotic disease risk in Southeast Asia. (PNAS 2022)

- DOI: 10.1073/pnas.2112341119 | PMCID: PMC9522346 | PMID: 36122224
- Version used: **3.8**
- Evidence: Multiple sequence alignments and phylogenetic trees were constructed when further analysis was required and were performed using MUSCLE v3.8 and PhyML v3.1, respectively ( 54 , 55 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8] -> stage not stated [QGIS v3.2.3, R, igraph]

### Recurrent emergence of <i>Klebsiella pneumoniae</i> carbapenem resistance mediated by an inhibitory <i>ompK36</i> mRNA secondary structure. (PNAS 2022)

- DOI: 10.1073/pnas.2203593119 | PMCID: PMC9499542 | PMID: 36095213
- Version used: **3.8**
- Evidence: Intact protein sequences of each porin were aligned using MUSCLE v3.8 ( 45 ), and the different variants present were identified, taking into account all amino acid substitutions, insertions, and deletions.
- Full pipeline: alignment/mapping [BCFtools v0.1.19, BLAST v2.6.0, MUSCLE v3.8, SAMtools] -> stage not stated [Prokka v1.14.5, SPAdes v3.9.0]

### Phylogenomic and functional characterization of an evolutionary conserved cytochrome P450-based insecticide detoxification mechanism in bees. (PNAS 2022)

- DOI: 10.1073/pnas.2205850119 | PMCID: PMC9245717 | PMID: 35733268
- Evidence: Clade 3 P450s from 24 species were selected, and protein sequences were aligned using the MUSCLE algorithm ( 56 ) in Geneious (version 10.2.6, Biomatters, New Zealand).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [InterProScan]

### Ancient proteins resolve controversy over the identity of <i>Genyornis</i> eggshell. (PNAS 2022)

- DOI: 10.1073/pnas.2109326119 | PMCID: PMC9995833 | PMID: 35609205
- Version used: **3.8.31**
- Evidence: The predicted coding regions were translated into protein sequences and aligned to the reference protein by MUSCLE v.3.8.31 ( 108 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, MUSCLE v3.8.31] -> stage not stated [AlphaFold, ColabFold, R v4.1, RAxML v1.0.3, phytools]

### ENPP1's regulation of extracellular cGAMP is a ubiquitous mechanism of attenuating STING signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2119189119 | PMCID: PMC9173814 | PMID: 35588451
- Evidence: To determine the histidine conservation in all known NPP sequences, 998 eukaryotic, 1,000 bacterial, and 584 archaeal NPP protein sequences were downloaded from Uniprot and pairwise-aligned using MUSCLE alignment ( 64 ).
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> visualisation [MAFFT]

### Analysis of biodiversity data suggests that mammal species are hidden in predictable places. (PNAS 2022)

- DOI: 10.1073/pnas.2103400119 | PMCID: PMC9168487 | PMID: 35344422
- Version used: **3.5**
- Evidence: Following taxonomic standardization, we grouped sequence records for each gene by family and generated multiple sequence alignments for COI and cytb independently using MUSCLE v3.5 ( 33 ).
- Full pipeline: alignment/mapping [MUSCLE v3.5] -> stage not stated [R v3.6.3]

### Protein cost minimization promotes the emergence of coenzyme redundancy. (PNAS 2022)

- DOI: 10.1073/pnas.2110787119 | PMCID: PMC9168515 | PMID: 35344442
- Version used: **3.8.31**
- Evidence: The sequences were then aligned using MUSCLE v3.8.31 using default parameters.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> stage not stated [Python]

### A conserved mechanism affecting hydride shifting and deprotonation in the synthesis of hopane triterpenes as compositions of wax in oat. (PNAS 2022)

- DOI: 10.1073/pnas.2118709119 | PMCID: PMC8944845 | PMID: 35290128
- Evidence: Multiple alignments of OSC protein sequences were performed ( Dataset S4 ), and a codon matrix was produced using the MUSCLE alignment package in MEGA 7 ( 39 ).
- Full pipeline: alignment/mapping [MUSCLE] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [PyMOL]

### Genomic adaptations for arboreal locomotion in Asian flying treefrogs. (PNAS 2022)

- DOI: 10.1073/pnas.2116342119 | PMCID: PMC9060438 | PMID: 35286217
- Version used: **3.8.31**
- Evidence: Then, we extracted the single gene families and aligned the protein sequences from each family using MUSCLE v3.8.31 ( 54 ) with the default parameters.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> differential/statistical testing [DESeq2 v1.30.0, featureCounts] -> stage not stated [BUSCO]

### Leg length and bristle density, both necessary for water surface locomotion, are genetically correlated in water striders. (PNAS 2022)

- DOI: 10.1073/pnas.2119210119 | PMCID: PMC8892508 | PMID: 35193982
- Evidence: Amino acid sequences were aligned with MUSCLE ( 55 ) and manually adjusted, and selected blocks were used for phylogenetic reconstruction.
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [DESeq2, RSEM] -> differential/statistical testing [DESeq2] -> structure determination [MUSCLE] -> stage not stated [RAxML]

### Convergent evolution of a blood-red nectar pigment in vertebrate-pollinated flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2114420119 | PMCID: PMC8812537 | PMID: 35074876
- Version used: **3.8.31**
- Evidence: Protein sequences were aligned with MUSCLE 3.8.31 ( 42 ) and refined with GBLOCKS 0.91b ( 43 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> structure determination [MUSCLE v3.8.31] -> stage not stated [R]

### A widely distributed phosphate-insensitive phosphatase presents a route for rapid organophosphorus remineralization in the biosphere. (PNAS 2022)

- DOI: 10.1073/pnas.2118122119 | PMCID: PMC8812569 | PMID: 35082153
- Evidence: To determine the phylogeny of PafA, sequences were aligned using MUSCLE and manually inspected for the possession of key amino acid residues using Molecular Evolutionary Genetics Analysis software version X (MEGAX).
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [BLAST] -> differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [HMMER, IQ-TREE]

### Structural insights into how vacuolar sorting receptors recognize the sorting determinants of seed storage proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2111281119 | PMCID: PMC8740768 | PMID: 34983843
- Evidence: ( F ) Sequence of VSR1-PA, pumpkin PV72, pea BP-80, and soybean and French bean VSRs were aligned using the program MUSCLE ( 57 ).
- Full pipeline: alignment/mapping [MUSCLE]

### Acquisition of the arginine deiminase system benefits epiparasitic Saccharibacteria and their host bacteria in a mammalian niche environment. (PNAS 2022)

- DOI: 10.1073/pnas.2114909119 | PMCID: PMC8764695 | PMID: 34992141
- Evidence: Among these seven bacteria, amino acid sequences for the genes’ ADS operon were aligned with MUSCLE ( 52 ) and the resultant percent identity was plotted as a heatmap in R.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE, RAxML v8.2.11] -> visualisation [MUSCLE] -> stage not stated [Python, eggNOG]

### Bimodular architecture of bacterial effector SAP05 that drives ubiquitin-independent targeted protein degradation. (PNAS 2023)

- DOI: 10.1073/pnas.2310664120 | PMCID: PMC10710061 | PMID: 38039272
- Evidence: Sequences of SAP05 homologs, A. thaliana SPLs, and Rpn10 from different organisms were aligned using MUSCLE algorithm on Phylogeny.fr web server ( 56 ) ( https://www.phylogeny.fr/index.cgi ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [AlphaFold]

### Massive intein content in &lt;i&gt;Anaeramoeba&lt;/i&gt; reveals aspects of intein mobility in eukaryotes. (PNAS 2023)

- DOI: 10.1073/pnas.2306381120 | PMCID: PMC10710043 | PMID: 38019867
- Evidence: The sequences were aligned with MUSCLE ( 40 ) (default parameters) and 115 amino acid sites manually selected.
- Full pipeline: alignment/mapping [IQ-TREE, MUSCLE] -> structure determination [IQ-TREE] -> visualisation [Cytoscape] -> stage not stated [BLAST]

### Evidence for an ancient aquatic origin of the RNA viral order &lt;i&gt;Articulavirales&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2310529120 | PMCID: PMC10636315 | PMID: 37906647
- Version used: **5.1**
- Evidence: The remaining sequences were aligned with MUSCLE v5.1 ( 30 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.490, MUSCLE v5.1] -> quantification [RSEM v1.3.0] -> visualisation [R v4.1] -> stage not stated [BLAST v2.0.9]

### Identification of a carbonic anhydrase-Rubisco complex within the alpha-carboxysome. (PNAS 2023)

- DOI: 10.1073/pnas.2308600120 | PMCID: PMC10614612 | PMID: 37862384
- Evidence: Sequences were aligned using MUSCLE ( 52 ).
- Full pipeline: alignment/mapping [MUSCLE, RELION v3.1] -> quantification [ImageJ] -> registration [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, IQ-TREE, PyMOL] -> stage not stated [CTFFIND v4.1]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Evidence: Curated OBP, CSP, and OR protein sequences were aligned in MEGA X using MUSCLE.
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Structural polymorphisms within a common powdery mildew effector scaffold as a driver of coevolution with cereal immune receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2307604120 | PMCID: PMC10410722 | PMID: 37523523
- Evidence: The protein sequences of the members of effector subfamilies were aligned using MUSCLE and then displayed by ESPript3 ( https://espript.ibcp.fr/ESPript/ESPript/ ).
- Full pipeline: alignment/mapping [MUSCLE] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, PHENIX]

### Independent evolution of transposase and TIRs facilitated by recombination between <i>Mutator</i> transposons from divergent clades in maize. (PNAS 2023)

- DOI: 10.1073/pnas.2305298120 | PMCID: PMC10401008 | PMID: 37490540
- Evidence: Homologous regions of mudra and mudrb sequences were aligned using MUSCLE to build neighbor-joining trees.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE]

### Genomic and geographical structure of human cytomegalovirus. (PNAS 2023)

- DOI: 10.1073/pnas.2221797120 | PMCID: PMC10372631 | PMID: 37459519
- Evidence: Multiple sequence alignments were obtained using MAFFT v7 ( 81 ), particularly variable sections were realigned using MUSCLE ( 82 ) and checked manually.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> registration [MAFFT, MUSCLE] -> stage not stated [IQ-TREE, Python, R]

### Nontriplet feature of genetic code in &lt;i&gt;Euplotes&lt;/i&gt; ciliates is a result of neutral evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2221683120 | PMCID: PMC10235951 | PMID: 37216548
- Evidence: The constructed OGGs were aligned with MUSCLE ( 109 ) with the default parameters.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [kallisto] -> stage not stated [BLAST]

### Interactions of TonB-dependent transporter FoxA with siderophores and antibiotics that affect binding, uptake, and signal transduction. (PNAS 2023)

- DOI: 10.1073/pnas.2221253120 | PMCID: PMC10120069 | PMID: 37043535
- Evidence: Ortholog sequences were imported from Uniprot ( 53 ), and sequences were aligned in Geneious Prime by MUSCLE alignment ( 54 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Version used: **3.8.1551**
- Evidence: The DIAMOND BLASTX hit coordinates were used to extract genomic regions corresponding to MCP gene hits before nucleotide sequences were clustered using MMseqs (50% identity across 30% length) to form five main clusters which were individually aligned using MUSCLE v3.8.1551 ( 59 ).
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Deciphering the evolution of flavin-dependent monooxygenase stereoselectivity using ancestral sequence reconstruction. (PNAS 2023)

- DOI: 10.1073/pnas.2218248120 | PMCID: PMC10104550 | PMID: 37014851
- Evidence: The sequences were initially aligned using MUSCLE ( 71 ).
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Whole-genome sequences from wild-type and laboratory-evolved strains define the alleleome and establish its hallmarks. (PNAS 2023)

- DOI: 10.1073/pnas.2218835120 | PMCID: PMC10104531 | PMID: 37011218
- Evidence: Once the AA sequence (and in-frame deletions) of all alleles was determined, the codon sequence for each allele was recreated to include any gaps detected by the MUSCLE alignment of AA sequences, allowing standardized position and codon information across all alleles.
- Full pipeline: alignment/mapping [MUSCLE]

### Transcription factor bHLH121 regulates root cortical aerenchyma formation in maize. (PNAS 2023)

- DOI: 10.1073/pnas.2219668120 | PMCID: PMC10041174 | PMID: 36927156
- Evidence: Protein sequences were aligned using MUSCLE ( 81 ) and a tree was constructed using the FastTree ( 82 ) algorithm.
- Full pipeline: alignment/mapping [MUSCLE] -> variant calling [R, lme4] -> differential/statistical testing [R] -> stage not stated [Bioconductor]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Version used: **3.8.31**
- Evidence: Single copy orthologs were identified between chytrids using the Synima ( 90 ) pipeline with Orthofinder, and aligned using MUSCLE v3.8.31 ( 91 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### Structural insights into the assembly and energy transfer of haptophyte photosystem I-light-harvesting supercomplex. (PNAS 2024)

- DOI: 10.1073/pnas.2413678121 | PMCID: PMC11648859 | PMID: 39642204
- Evidence: The sequences for producing the phylogenetic tree were aligned using MUSCLE with default parameters and the tree was constructed using MEGA X ( 69 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Python]

### Substrate specificity controlled by the exit site of human P4-ATPases, revealed by de novo point mutations in neurological disorders. (PNAS 2024)

- DOI: 10.1073/pnas.2415755121 | PMCID: PMC11536178 | PMID: 39432785
- Evidence: ( D ) The sequences of human ATP11A (UniProt: P98196 ), chicken ATP11A (UniProt: A0A8V0YD23), Fugu ATP11A (UniProt: H2UJQ6), and Xenopus ATP11A (UniProt: A0A6I8QJD9) are aligned using the MUSCLE Program in European Molecular Biology Laboratory-European Bioinformatics Institute (EMBL-EBI).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [UCSF Chimera]

### Disorder-to-order active site capping regulates the rate-limiting step of the inositol pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2400912121 | PMCID: PMC11348189 | PMID: 39145930
- Evidence: The sequences were aligned using MUSCLE with default settings ( 76 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL, UCSF Chimera]

### Exploring a unique class of flavoenzymes: Identification and biochemical characterization of ribosomal RNA dihydrouridine synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2401981121 | PMCID: PMC11317573 | PMID: 39078675
- Version used: **5.1**
- Evidence: Protein sequences were aligned using MUSCLE v5.1 ( 44 ) and visualized using Weblogo3 ( 45 ).
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> visualisation [MUSCLE v5.1] -> stage not stated [AlphaFold]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **5.1**
- Evidence: Both MAFFT v7.490 ( 65 ) and MUSCLE v5.1 ( 70 ) alignment algorithms were used.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### A wound-induced differentiation trajectory for neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2322864121 | PMCID: PMC11260127 | PMID: 38976727
- Version used: **3.8.31**
- Evidence: Sequences were aligned with MUSCLE (v3.8.31) ( 117 ).
- Full pipeline: read trimming [RAxML v8.2.4] -> alignment/mapping [MUSCLE v3.8.31, RAxML v8.2.4] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [BUSCO v3.0.2, Pilon v1.23]

### A niche-derived nonribosomal peptide triggers planarian sexual development. (PNAS 2024)

- DOI: 10.1073/pnas.2321349121 | PMCID: PMC11214079 | PMID: 38889152
- Evidence: MUSCLE alignment of the following protein sequences was performed using Jalview software (using default settings): Drosophila melanogaster Ebony ( NP_524431.2 ), S. mediterrranea NRPS, S. mansoni NRPS (A0A3Q0KR05.1).
- Full pipeline: alignment/mapping [MUSCLE]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Version used: **3.8.31**
- Evidence: These genes were aligned with MUSCLE (v3.8.31) with default parameters ( 39 ).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Premeiotic 24-nt phasiRNAs are present in the <i>Zea</i> genus and unique in biogenesis mechanism and molecular function. (PNAS 2024)

- DOI: 10.1073/pnas.2402285121 | PMCID: PMC11127045 | PMID: 38739785
- Evidence: The resulting sequences were aligned using MUSCLE ( 43 ), and phylogenetic trees were built using IQ-TREE v2.2.0.3 ( 44 ) to assign/curate names of MIR2118 and MIR2275 loci based on orthology.
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MUSCLE, edgeR v4.0.2, featureCounts v1.6.3] -> normalisation [edgeR v4.0.2, featureCounts v1.6.3] -> stage not stated [BEDTools v2.29.2, StringTie v2.1.7]

### A distinct, high-affinity, alkaline phosphatase facilitates occupation of P-depleted environments by marine picocyanobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2312892121 | PMCID: PMC11098088 | PMID: 38713622
- Version used: **3.8.31**
- Evidence: Additionally, UCSF Chimera facilitated comparison of protein structures while MUSCLE v3.8.31 ( 76 ) was used to align protein sequences to identify conserved amino acids.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.3, MUSCLE v3.8.31] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, HMMER, SciPy v1.10.1]

### Genomes of historical specimens reveal multiple invasions of LTR retrotransposons in <i>Drosophila melanogaster</i> during the 19th century. (PNAS 2024)

- DOI: 10.1073/pnas.2313866121 | PMCID: PMC11009621 | PMID: 38564639
- Version used: **3.8.1551**
- Evidence: We extracted the sequences of mostly full-length insertions (based on a length threshold; for Blood and 412: 6,000 to 8,000bp; for Opus: 5,000 to 8,000bp; for the I-element: 4,000 to 6,000) with bedtools ( 78 ) (v2.30.0) and performed multiple sequence alignment using MUSCLE (v3.8.1551) ( 52 ).
- Full pipeline: alignment/mapping [BEDTools, MUSCLE v3.8.1551] -> visualisation [Python, ggplot2] -> stage not stated [Cutadapt, RepeatMasker]

### The evolutionary genomics of adaptation to stress in wild rhizobium bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2311127121 | PMCID: PMC10990125 | PMID: 38507447
- Evidence: Amino acid sequences from 1,542 single-copy core genes were aligned with MUSCLE ( 78 ), concatenated, and trimmed with Trimal ( 79 ).
- Full pipeline: quality control [Prokka v1.13.3] -> read trimming [MUSCLE] -> alignment/mapping [MAFFT v7.475, MUSCLE] -> differential/statistical testing [lme4 v1.1] -> visualisation [R] -> stage not stated [RAxML, SPAdes v3.14.1]

### Fluorescent proteins generate a genetic color polymorphism and counteract oxidative stress in intertidal sea anemones. (PNAS 2024)

- DOI: 10.1073/pnas.2317017121 | PMCID: PMC10945830 | PMID: 38457522
- Evidence: For phylogenetic analyses, sequences were first aligned with MUSCLE ( 81 ) and trimmed with TrimAl ( 82 ).
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [MUSCLE] -> quantification [ImageJ] -> stage not stated [AlphaFold, IQ-TREE v1.6.1, PyMOL v2.4.0]

### Extracellular vesicle formation in <i>Euryarchaeota</i> is driven by a small GTPase. (PNAS 2024)

- DOI: 10.1073/pnas.2311321121 | PMCID: PMC10927574 | PMID: 38408251
- Evidence: The final dataset was aligned with MUSCLE and a phylogenetic tree was constructed using IQ-Tree ( 102 ) with ultrafast bootstrap analysis ( 103 ) using 1,000 bootstrap replicates and default settings, auto-selecting the substitution model ( 104 ).
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R] -> stage not stated [AlphaFold, ImageJ]

### The 10,000-year biocultural history of fallow deer and its implications for conservation policy. (PNAS 2024)

- DOI: 10.1073/pnas.2310051121 | PMCID: PMC10895352 | PMID: 38346198
- Evidence: All sequences were aligned using the MUSCLE algorithm ( 77 ) as implemented in Geneious v.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [MrBayes v3.2.6]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Evidence: Protein sequences were aligned using the MUSCLE algorithm ( 79 ) implemented in MEGA XI software ( 80 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### Methionine synthesis and glycine betaine demethylation are intricately intertwined in cosmopolitan marine bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2426167122 | PMCID: PMC12478193 | PMID: 40956897
- Evidence: To generate these pHMMs, sequences (Top hits) retrieved from BLASTP were aligned using MUSCLE, trimmed and phylogenetic reconstruction by maximum likelihood was performed using IQtree2 ( 58 ) with parameters -m TESTMERGE -bb 1000 -safe.
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [MUSCLE] -> structure determination [MUSCLE]

### A widespread family of molecular chaperones promotes the intracellular stability of type VIIb secretion system-exported toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2503581122 | PMCID: PMC12478183 | PMID: 40953262
- Version used: **3.8.1551**
- Evidence: Protein alignments were performed using MUSCLE v3.8.1551 ( 66 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [IQ-TREE] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Female membrane proteins regulate postmating ovulation in &lt;i&gt;Drosophila melanogaster&lt;/i&gt; by ovulin-dependent and -independent pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2508783122 | PMCID: PMC12452909 | PMID: 40920921
- Evidence: ...er, sechellia, simulans, yakuba, erecta, ananassae, pseudoobscura, persimilis, wil-listoni, grimshawi, virilis, and mojavensis ) using InParanoid and aligned using MUSCLE ( 81 – 83 ).
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> variant calling [lme4] -> differential/statistical testing [emmeans, lme4] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.5.5]

### Surface delivery quantification reveals distinct trafficking efficiencies among clustered protocadherin isoforms. (PNAS 2025)

- DOI: 10.1073/pnas.2514178122 | PMCID: PMC12337331 | PMID: 40737325
- Version used: **5.1**
- Evidence: The sequences of all mouse cPCDHs were manually gathered from UniProt (release 2023_05) ( 65 ), aligned using MUSCLE v.5.1 ( 66 ), and truncated to EC6 (Geneious Prime 2023.1.2 [ https://www.geneious.com ]).
- Full pipeline: alignment/mapping [MUSCLE v5.1, Python, SciPy v1.11.4] -> stage not stated [AlphaFold, seaborn v0.13.0]

### The oncogene SLC35F2 is a high-specificity transporter for the micronutrients queuine and queuosine. (PNAS 2025)

- DOI: 10.1073/pnas.2425364122 | PMCID: PMC12207525 | PMID: 40526720
- Version used: **5.2**
- Evidence: 34 IPR05221 family sequences across different clades/kingdoms and three outgroup sequences, SLC35B1-4/HUT1 were aligned using MUSCLE v5.2 ( 60 ) and trimmed using BMGE v1.12 ( 61 ) with matrix BLOSUM30.
- Full pipeline: read trimming [MUSCLE v5.2] -> alignment/mapping [AlphaFold, MUSCLE v5.2] -> quantification [ImageJ] -> visualisation [Cytoscape v3.10.1]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **3.8**
- Evidence: To reconstruct the phylogeny of LysM-RLKs, a set of 102 protein sequences composed of 8 Marchantia genes and the set described by Buendia et al. supplemented with the L. japonicus EPR3 and EPR3a sequences ( 46 ) was aligned using MUSCLE (v3.8).
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: For genes involved in the MVA and MEP pathways, sequences were aligned using MUSCLE and converted to STO format via ALTER ( http://www.sing-group.org/ALTER/ ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### The emergence and loss of cyclic peptides in &lt;i&gt;Nicotiana&lt;/i&gt; illuminate dynamics and mechanisms of plant metabolic evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2425055122 | PMCID: PMC12037056 | PMID: 40228125
- Evidence: The nonrepetitive elements were aligned using MUSCLE, excluding the tandem repeat regions due to significant variations between genes.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [AlphaFold]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **5.1**
- Evidence: Briefly, the sequences of 16 ribosomal proteins within MAGs were identified using HMMER v3.4 ( http://hmmer.org ) and aligned by MUSCLE v5.1 ( 58 ).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Characterization of diverse Cas9 orthologs for genome and epigenome editing. (PNAS 2025)

- DOI: 10.1073/pnas.2417674122 | PMCID: PMC11929499 | PMID: 40073054
- Version used: **3.8.425**
- Evidence: The Cas9 protein sequences were aligned using MUSCLE 3.8.425 with default parameters in Geneious ( 57 ).
- Full pipeline: alignment/mapping [AlphaFold, MUSCLE v3.8.425] -> stage not stated [BLAST, RAxML]

### Evolutionary rewiring of the dynamic network underpinning allosteric epistasis in NS1 of the influenza A virus. (PNAS 2025)

- DOI: 10.1073/pnas.2410813122 | PMCID: PMC11873825 | PMID: 39977319
- Evidence: The sequences were aligned using MUSCLE (Multiple Sequence Comparison by Log-Expectation) algorithm ( 81 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [NetworkX, OpenMM v7.6.0, Python]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Evidence: The sequences within classes were aligned to one another using MUSCLE ( 87 ) within the R package msa ( 88 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Version used: **5.1**
- Evidence: MUSCLE v5.1 ( 56 ) or MAFFT v7.490 ( 57 ) alignments were generated, as indicated, of FASTA amino acid sequences.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### ClpP2 modulates ClpXP assembly to promote multiple pathogenic phenotypes in &lt;i&gt;&lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2532651123 | PMCID: PMC13056064 | PMID: 41920875
- Evidence: For variant analysis, ClpP1 and ClpP2 protein sequences identified across all isolates were combined with the corresponding PAO1 reference sequences and aligned using MUSCLE.
- Full pipeline: alignment/mapping [MUSCLE]

### Photoreceptor control of &lt;i&gt;Platynereis&lt;/i&gt; growth and lifespan via evolutionarily conserved molecular pathways. (PNAS 2026)

- DOI: 10.1073/pnas.2514719123 | PMCID: PMC13012086 | PMID: 41855267
- Evidence: Hit sequences were aligned using MUSCLE ( 90 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [IQ-TREE, ImageJ]

### Decoding antibody response to MERS-CoV in wild dromedary camels. (PNAS 2026)

- DOI: 10.1073/pnas.2513716123 | PMCID: PMC12913009 | PMID: 41662528
- Version used: **3.8.1551**
- Evidence: Amino acid sequences were aligned using MUSCLE v3.8.1551, and a phylogenetic tree was constructed with IQ-TREE v2.1.4-beta using 1,000 bootstrap replicates ( http://www.iqtree.org/ ).
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.310, MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, PyMOL] -> stage not stated [CCP4]

### Induction of broadly neutralizing HIV antibodies by a two-step mechanism informs vaccine design. (Science 2026)

- DOI: 10.1126/science.aec6396 | PMCID: PMC13308464 | PMID: 42096521
- Evidence: A total of 8,406 env gp140 sequences were aligned using the MUSCLE alignment method and manually inspected using Geneious Prime to improve the alignment results based on codon translation.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [SciPy v0.18.0] -> structure determination [ChimeraX, Coot v0.8.9, PHENIX] -> visualisation [PyMOL]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Evidence: NTD Interface Conservation Analysis The sequences of AMPAR core subunits GluA1, GluA2, GluA3 and GluA4 from a range of vertebrates (mammals, reptiles, amphibians and fish) were downloaded from the Ensembl database ( 88 ) and the region corresponding to the NTD (residues 1-375) was extracted and aligned with MUSCLE ( 89 ) within UniPro UGENE ( 90 ).
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

