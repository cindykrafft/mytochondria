# ColabFold

- **Category:** structbio
- **Papers in survey:** 177
- **Journals:** PNAS (109), Nature (51), Cell (13), Science (4)
- **Years:** 2022 (15), 2023 (36), 2024 (60), 2025 (53), 2026 (13)
- **Versions named:** 1.5.5 (12), 1.5.2 (9), 1.3 (3), 1.5.1 (2), 1.2 (2), 1.3.0 (1), 1.5 (1), 1.5.3 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (8), alignment/mapping (8), structure determination (4), simulation/modelling (3), visualisation (1), machine learning (1)

## Papers

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: The ColabFold, an AlphaFold2-based Google notebook, was then used to model how two copies of Tektin 5 molecules interact 32 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Evidence: Complexes between peptides and potential receptors (GPCRs and Amiloride Sensitive Channels) were modeled using a locally installed version of ColabFold - v1.5.2 ( https://github.com/YoshitakaMo/localcolabfold ), derived from the original ColabFold 41 using the state of the art complex modeling tool Alphafold-multimer.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Mechanism of orphan subunit recognition during assembly quality control. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.016 | PMCID: PMC10501995 | PMID: 37480851
- Version used: **1.2**
- Evidence: 35 N/A ColabFold (ver.
- Full pipeline: differential/statistical testing [R] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold v1.2]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: ...z 109 https://cb.csail.mit.edu/cb/topaz/ CryoSPARC V3.3.1 110 https://cryosparc.com AlphaFold2 Multimer 54 , 55 https://github.com/deepmind/alphafold ColabFold 56 https://github.com/sokrypton/ColabFold MAFFT L-INS-i (v7.505) 111 https://mafft.cbrc.jp/alignment/software/ IQTree2.1.3 112 http://www.iqtree.org Consurf 113 https://consurf.tau.ac.il/consurf_index.php Other Superose6 Increase10/300 GL c...
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Evidence: 49 https://github.com/deepmind/alphafold ColabFold Mirdita et al.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: Model building The initial model of HamAB was obtained with the ColabFold.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Structural insights into the diversity and DNA cleavage mechanism of Fanzor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.050 | PMCID: PMC11423790 | PMID: 39208796
- Evidence: Models for each protein were predicted using the ColabFold framework 42 , 44 with 40 recycles and 5 replicates.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.7, PHENIX v1.18] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RELION v4.0, UCSF Chimera v1.16]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: To generate a first approximation of possible structure, we ran the 323 candidate SEP sequences through ColabFold using default parameters.
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### A replisome-associated histone H3-H4 chaperone required for epigenetic inheritance. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.006 | PMCID: PMC11380579 | PMID: 39094570
- Evidence: ...CA018248; GRA: CRA011810; CRA014983; GSE269383 Software and algorithms UCSF Chimera X daily build (2022-10-26) version UCSF Chimera X RRID:SCR_015872 ColabFold Google Colab N/A localColabFold Harvard Medical School O2 computing cluster N/A In-house mass spectrometry data analysis software 109 N/A ChatGPT3.5 (March 24 version) OpenAI RRID:SCR_023775 Clustal Omega UniProt RRID:SCR_001591 JalView Uni...
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, ColabFold, UCSF Chimera] -> stage not stated [AlphaFold, Bowtie2, MACS2]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Evidence: 48 https://github.com/sokrypton/ColabFold Coot Version.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Synthetic protein circuits for programmable control of mammalian cell death. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.031 | PMCID: PMC11127782 | PMID: 38657604
- Version used: **1.5.2**
- Evidence: 105 To examine molecules whose structures are not available, such as engineered GSDMA containing a TEVP cleavage site or leucine zippers, we generated models using AlphaFold2 (ColabFold v1.5.2).
- Full pipeline: visualisation [ImageJ, Matplotlib, PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, Jupyter]

### Mastigoneme structure reveals insights into the O-linked glycosylation code of native hydroxyproline-rich helices. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.005 | PMCID: PMC11015965 | PMID: 38552624
- Evidence: Model building Initial atomic models were generated using AlphaFold2 and ColabFold.
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, ColabFold, InterProScan]

### Principles of cotranslational mitochondrial protein import. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.021 | PMCID: PMC12396113 | PMID: 40795856
- Evidence: In silico protein structure prediction The structure of COQ3-repeat was predicted using ColabFold, 64 a Google Colab-based implementation of AlphaFold, 71 using default settings.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.5, STAR v2.7.10a] -> stage not stated [AlphaFold, ColabFold]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: 31 ) under the ColabFold framework using default parameters and MMseqs2 to search for homologues into the ColabFold database 32 , and manually modified using COOT 33 and ISOLDE 7 against the density map of complex A.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Evidence: 61 ) through ColabFold 62 —an online platform for protein folding.
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Evidence: To predict the structure of Parkin Ubl-bound Hs PINK1 and dimerized Hs PINK1, we used the ColabFold Google Colab notebook called AlphaFold2_complexes 39 .
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### Bacterial cGAS senses a viral RNA to initiate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06743-9 | PMCID: PMC10686824 | PMID: 37968393
- Evidence: A structure of the Ssc-CdnE03 was predicted using AlphaFold (ColabFold).
- Full pipeline: alignment/mapping [Bowtie2, PyMOL, Python] -> visualisation [Bowtie2] -> stage not stated [AlphaFold, ColabFold]

### Plant carbonic anhydrase-like enzymes in neuroactive alkaloid biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-06716-y | PMCID: PMC10700139 | PMID: 37938780
- Version used: **1.5.2**
- Evidence: The structures of Pt CAL-1a, Pt CAL-2a and Pt CAL-3 were modelled using AlphaFold2 through ColabFold (v.1.5.2) 48 .
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [edgeR] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold v1.5.2, HMMER]

### Proteome census upon nutrient stress reveals Golgiphagy membrane receptors. (Nature 2023)

- DOI: 10.1038/s41586-023-06657-6 | PMCID: PMC10620096 | PMID: 37757899
- Evidence: ColabFold implementation of AlphaFold 23 predicts a YIPF3–YIPF4 heterodimer, with both N-terminal regions being largely unstructured (Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Evidence: The prediction of protein complex structures was performed using AlphaFold 72 – 74 v.2.1.0 on the Colab notebook (ColabFold) 75 ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Clustering predicted structures at the scale of the known protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06510-w | PMCID: PMC10584675 | PMID: 37704730
- Evidence: 8 )—which originates from a cultured Lachnospiraceae bacterium that is part of the Culturable Genome Reference 30 of the human gut—using ColabFold 31 and confirmed that it has a similar structure DNA-binding domain structure (TM score of 0.97 and 0.56 in relation to UniProt A0A1C5UEQ5 and human AIM, respectively).
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX v1.5, ColabFold, Matplotlib v3.6.2, seaborn v0.12.2]

### Bacterial pathogens deliver water- and solute-permeable channels to plant cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06531-5 | PMCID: PMC10511319 | PMID: 37704725
- Evidence: AlphaFold2 analysis and cryo-EM imaging To gain functional insights into the AvrE family of bacterial effectors, we constructed their three-dimensional models predicted by AlphaFold2 26 using the fast homology search of MMseqs2 (ColabFold) 27 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [AlphaFold, ColabFold] -> stage not stated [PyMOL v1.8.0.4]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Evidence: Alphafold prediction of ModB structure The Alphafold prediction of ModB structure was performed with AlphaFold2.ipynb (v.1.3.0, https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) with default parameters (use_templates = false, use_amber = false; msa_mode = MMseqs2 (UniRef+Environmental), model_type = “AlphaFold2-ptm”, max_msa = null, pair_mode = unpaired+pair...
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### Central role of Tim17 in mitochondrial presequence protein translocation. (Nature 2023)

- DOI: 10.1038/s41586-023-06477-8 | PMCID: PMC10511324 | PMID: 37527780
- Evidence: Structural prediction of the Tim17–Tim23 heterodimer and heterotetramer as well as the interaction between further subunits of the TIM23 complex (Tim17–Tim23–Mgr2 and Tim17–Tim23–Mgr2–Pam17–Tim21–Tim50) was performed with ColabFold 47 .
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, ImageJ v1.49v, PyMOL]

### Phase separation of FSP1 promotes ferroptosis. (Nature 2023)

- DOI: 10.1038/s41586-023-06255-6 | PMCID: PMC10338336 | PMID: 37380771
- Evidence: Predicted cartoon structure of hFSP1 WT (yellow) S187C (green), L217R (cyan), and Q319K (magenta) by AlphaFold2 or ColabFold.
- Full pipeline: visualisation [CellProfiler v4.1.3] -> stage not stated [AlphaFold, ColabFold, Fiji, ImageJ]

### Programmable protein delivery with a bacterial contractile injection system. (Nature 2023)

- DOI: 10.1038/s41586-023-05870-7 | PMCID: PMC10097599 | PMID: 36991127
- Evidence: In silico protein structure prediction To predict the structure of novel PVC tail fibre designs, we leveraged ColabFold, a Google Colab-based implementation of AlphaFold2 35 – 37 .
- Full pipeline: quantification [ImageJ] -> visualisation [PyMOL v2.5.2] -> stage not stated [AlphaFold, ColabFold]

### Aberrant phase separation and nucleolar dysfunction in rare genetic diseases. (Nature 2023)

- DOI: 10.1038/s41586-022-05682-1 | PMCID: PMC9931588 | PMID: 36755093
- Evidence: Multiple sequence analysis depth plots and per-model pLDDT sequence plots were made using custom scripts based on ColabFold notebook AlphaFold2 with MMseqs2 (ref.
- Full pipeline: visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BEDTools v2.30.0, ColabFold, R, VEP, ggplot2]

### A bacterial immunity protein directly senses two disparate phage proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08039-y | PMCID: PMC11578894 | PMID: 39415022
- Evidence: The structure of CapRel SJ46 in the closed state for comparison with the experimental SAXS curve was also calculated using AlphaFold2 using default parameters (as implemented in ColabFold 38 ) and running the calculations for ten recycles.
- Full pipeline: alignment/mapping [BLAST, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: 22 , 23 ) on ColabFold 37 .
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **1.5.1**
- Evidence: Structures were predicted for each sequence using the ColabFold (v1.5.1) implementation of AlphaFold2 (v2.3) 19 , with default settings but only generating a single model per target, performed using Google Colab cloud computing.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Evidence: Structures were predicted with ColabFold 15 (downloaded 22 June 2022).
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### An intermediate Rb-E2F activity state safeguards proliferation commitment. (Nature 2024)

- DOI: 10.1038/s41586-024-07554-2 | PMCID: PMC11236703 | PMID: 38926571
- Evidence: Protein structural modelling Structures were modelled using ColabFold 56 , a simplified AlphaFold2 algorithm 30 , 57 , without templates ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFAlp2_advanced.ipynb ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [Clustal Omega] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### Structural mechanism of bridge RNA-guided recombination. (Nature 2024)

- DOI: 10.1038/s41586-024-07570-2 | PMCID: PMC11208158 | PMID: 38926616
- Evidence: Model building and validation The models of the IS621–bRNA–dDNA–tDNA synaptic complexes were manually built using COOT 36 , starting from a model predicted by ColabFold 37 .
- Full pipeline: structure determination [ChimeraX] -> visualisation [ChimeraX] -> stage not stated [BLAST, ColabFold]

### DNA glycosylases provide antiviral defence in prokaryotes. (Nature 2024)

- DOI: 10.1038/s41586-024-07329-9 | PMCID: PMC11078745 | PMID: 38632404
- Evidence: Brig1 structural predictions using AlphaFold2 The structure of the intact (261 amino acid) Brig1 protein was predicted using the colab implementation of AlphaFold2 17 , 18 ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) using default settings (except that the amber option was turned on to improve side chain rotamers).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MUSCLE, Python] -> normalisation [Python] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, ColabFold]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: These multiple sequence alignments (MSAs) were uploaded to ColabFold 37 and a total of five AlphaFold predictions were generated for each target.
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Structural basis of Integrator-dependent RNA polymerase II termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07269-4 | PMCID: PMC11062913 | PMID: 38570683
- Evidence: The interface between INTS10 and INTS14 was initially generated using ColabFold 41 and agrees with our cryo-EM density map and previous biochemical data 34 .
- Full pipeline: structure determination [ChimeraX, ColabFold, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Evidence: DCAF16 was built using a combination of models from ColabFold 69 , 70 (v1.3), ModelAngelo 71 (v0.2.2) and manual building in Coot (v0.9.8.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### Functional and evolutionary significance of unknown genes from uncultivated taxa. (Nature 2024)

- DOI: 10.1038/s41586-023-06955-z | PMCID: PMC10849945 | PMID: 38109938
- Evidence: Given the low number of matches obtained, we decided to run de novo structural predictions for all FESNov families by means of ColabFold 35 using the representative sequence of each family as input.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega, DIAMOND] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [R] -> structure determination [Clustal Omega] -> stage not stated [ColabFold, HMMER, eggNOG]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Evidence: Methods MSA generation MSAs were generated using the MMseqs2-based 60 routine implemented in ColabFold 34 .
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Florigen activation complex forms via multifaceted assembly in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-025-09704-6 | PMCID: PMC12711580 | PMID: 41225013
- Evidence: The modelled structure of the FDc–GRF7 and GRF7–FT complex was predicted by ColabFold 39 .
- Full pipeline: alignment/mapping [MAFFT] -> quantification [Cellpose v2.2.3] -> stage not stated [AlphaFold, ColabFold, IQ-TREE v1.5.5]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Evidence: To clarify which homologue has the highest structural similarity to previously characterized proteins and is therefore most likely to have a function similar to that of freshwater cyanobacterial NblAs, we obtained the structures for the corresponding monomers with ColabFold 65 and searched them against the Protein Data Bank (PDB) using Foldseek 66 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Version used: **1.5.5**
- Evidence: Each batch was run through ColabFold (v1.5.5) 34 , 64 , 65 using Tesla T4 GPUs as a first pass, then larger complexes were completed using Tesla A100 GPUs.
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### The Panoptes system uses decoy cyclic nucleotides to defend against phage. (Nature 2025)

- DOI: 10.1038/s41586-025-09557-z | PMCID: PMC12657218 | PMID: 41034579
- Version used: **1.5.5**
- Evidence: The structures were determined using molecular replacement conducted by the Phaser-MR program in the PHENIX suite (v.1.21-5207) 58 using a predicted structural model of Kp OptS generated by ColabFold v.1.5.5, which uses a homology search by MMseqs2 with AlphaFold2 59 .
- Full pipeline: differential/statistical testing [tidyverse] -> structure determination [Coot v1.1.17] -> visualisation [PyMOL, tidyverse] -> stage not stated [AlphaFold, ColabFold v1.5.5, PHENIX]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: The structure was solved by molecular replacement 67 using a ColabFold-generated 68 model (pLDDT = 95.12) of mCpol with residual residues from the C-terminal cleavage site (mCpol-ENLYFQ) in PHENIX 69 .
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: Three-dimensional structures of protein complexes were predicted using the ColabFold 86 implementation of the AlphaFold-Multimer algorithm 87 .
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Evidence: AlphaFold protein co-folding prediction Co-folding of proteins were done by AlphaFold 2 implemented in ColabFold 76 .
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Design of highly functional genome editors by modelling CRISPR-Cas sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-09298-z | PMCID: PMC12422970 | PMID: 40739342
- Evidence: For a small number of sequences, we observed high similarity to natural proteins in the CRISPR–Cas Atlas but low structure prediction confidence, owing to limited homology in the ColabFold sequence database used for predictions.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Complete computational design of high-efficiency Kemp elimination enzymes. (Nature 2025)

- DOI: 10.1038/s41586-025-09136-2 | PMCID: PMC12310539 | PMID: 40533551
- Evidence: The structures of these sequences were modelled using ColabFold AlphaFold2 (refs.
- Full pipeline: dimensionality reduction/clustering [MDTraj] -> simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold, PyMOL, VMD]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Version used: **1.5.2**
- Evidence: AF-M, AlphaLink2 and structural modelling AF-M was run with ColabFold v1.5.2 (ref.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **1.3.0**
- Evidence: 110 ) through ColabFold v.1.3.0 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Targeting protein-ligand neosurfaces with a generalizable deep learning tool. (Nature 2025)

- DOI: 10.1038/s41586-024-08435-4 | PMCID: PMC11903328 | PMID: 39814890
- Evidence: Ten sequences per design were generated and folded with AlphaFold2 in the ColabFold software 50 (single sequence mode).
- Full pipeline: structure determination [Coot v0.9.5] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, ColabFold, PHENIX, RDKit, RoseTTAFold]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **1.5.2**
- Evidence: Alphafold2 and structural homology modelling The structure of M. truncatula CNGC15a homotetramer was predicted with AlphaFold2 multimer, as implemented through ColabFold (v.1.5.2) 55 ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ).
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: Multimer structure prediction LocalColabFold and ColabFold were used to predict multimer structures with the AlphaFold Multimer v.2.3 model.
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### The structure of apolipoprotein B100 from human low-density lipoprotein. (Nature 2025)

- DOI: 10.1038/s41586-024-08467-w | PMCID: PMC11839476 | PMID: 39662503
- Evidence: 4 ) as implemented through ColabFold 47 .
- Full pipeline: simulation/modelling [NAMD v2.14, PHENIX v1.20] -> structure determination [PHENIX v1.20] -> machine learning [PHENIX v1.20] -> visualisation [ChimeraX, VMD v1.9.4] -> stage not stated [AlphaFold, ColabFold]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Version used: **1.5.2**
- Evidence: The structures were predicted for each MMseqs2 cluster representative of each ZorA and ZorB family using ColabFold (v.1.5.2) 71 with the options --num-recycle 3 --num-models 1 --model-type auto --amber --use-gpu-relax.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### Large-scale discovery, analysis and design of protein energy landscapes. (Nature 2026)

- DOI: 10.1038/s41586-026-10465-z | PMCID: PMC13293878 | PMID: 42129553
- Evidence: The protein sequences, provided in FASTA format, were used as input to the ColabFold implementation of AlphaFold 2 96 , which was run on Quest high performance computing facility at Northwestern University.
- Full pipeline: dimensionality reduction/clustering [Snakemake] -> stage not stated [AlphaFold, ColabFold, Jupyter, SciPy]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Evidence: The structure of human CEACAM6 in complex with CcCoV-2B was solved by molecular replacement using PHASER 66 with models of the CEACAM6 ectodomain and CcCoV-2B RBD (residues 496–625) that were generated with ColabFold 73 using the crystal structure of CEACAM6 in complex with the CcCoV-KY43 RBD as a template.
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: AlphaFold2 and AlphaFold3 predictions Structure predictions were done with AlphaFold2 implemented in a google colab notebook 70 available online ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb.Predictions ); predictions using AlphaFold3 71 were done at https://alphafoldserver.com/ .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### DNA damage drives antigen diversification in Trypanosoma brucei. (Nature 2026)

- DOI: 10.1038/s41586-026-10337-6 | PMCID: PMC13233330 | PMID: 41951731
- Evidence: We modelled the structure of these mosaics using ColabFold and their general structures matched AnTat1.1 (Fig.
- Full pipeline: alignment/mapping [ChimeraX v1.7.1] -> dimensionality reduction/clustering [BLAST] -> visualisation [ChimeraX v1.7.1] -> stage not stated [ColabFold, R v4.0.2]

### Capturing dynamic phage-pathogen coevolution by clinical surveillance. (Nature 2026)

- DOI: 10.1038/s41586-026-10136-z | PMCID: PMC12987554 | PMID: 41813903
- Evidence: The structural predictions for TAC PLE4 and Rta were made using ColabFold 46 on COSMIC2 (ref.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [BLAST, ColabFold, IQ-TREE v2.2.0, SPAdes, fastp v0.23.2]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Evidence: Source data Molecular dynamics of CLCC1 function Structural analysis of the homologous domain of CLCC1, as well as Brl1 and Brr6, using ColabFold predicts the formation of a large oligomeric ring structure (Supplementary Fig.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Version used: **1.5.5**
- Evidence: Protein conservation and structure visualization The mouse SPOCD1 TFIIS-M structure was generated using AlphaFold2 45 using the ColabFold v1.5.5 notebook 46 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Cross-regulation of [2Fe-2S] cluster synthesis by ferredoxin-2 and frataxin. (Nature 2026)

- DOI: 10.1038/s41586-025-09822-1 | PMCID: PMC12804074 | PMID: 41372413
- Version used: **1.3**
- Evidence: AlphaFold We used our in-house implementation of ColabFold 1.3 49 , which incorporates AlphaFold 2.2 50 , to generate models for the ISC complex composed of NFS1, ISD11, ACP, ISCU2 and FDX2, with the corresponding Uniprot IDs Q9Y697 , Q9HD34 , O14561 (69–156), Q9H1K1 (35–167) and Q6P4F2 (56-186), respectively.
- Full pipeline: visualisation [PyMOL v3.0] -> stage not stated [AlphaFold v2.2, ColabFold v1.3]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Version used: **1.5.5**
- Evidence: AlphaFold2-Multimer modelling of Cbf1 dimers We predicted structures for Cbf1 dimers from J. lodderae , J. jinghongensis and J. spencerorum using a local installation of ColabFold 1.5.5 (ref.
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Creative destruction: New protein folds from old. (PNAS 2022)

- DOI: 10.1073/pnas.2207897119 | PMCID: PMC9907106 | PMID: 36534803
- Evidence: The 3D structures of these constructs (deposited in FigShare, DOI 10.6084/m9.figshare.19412180 as Files 7 and 8 ( 81 )) were predicted with AlphaFold ( 49 ) in ColabFold ( 85 ) using the single-sequence option.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### FtsEX-independent control of RipA-mediated cell separation in <i>Corynebacteriales</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214599119 | PMCID: PMC9897464 | PMID: 36469781
- Evidence: The predicted structures of the different complexes were obtained with AlphaFold-Multimer by submitting the different sequences to the server at: https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ( 63 ).
- Full pipeline: structure determination [IQ-TREE v2.0.6, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CCP4, ColabFold, HMMER]

### A blast fungus zinc-finger fold effector binds to a hydrophobic pocket in host Exo70 proteins to modulate immune recognition in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2210559119 | PMCID: PMC9618136 | PMID: 36252011
- Evidence: We then modeled rice OsExo70B1 using AlphaFold2 ( 65 ), as implemented in ColabFold ( 66 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, ColabFold]

### The unstructured linker of Mlh1 contains a motif required for endonuclease function which is mutated in cancers. (PNAS 2022)

- DOI: 10.1073/pnas.2212870119 | PMCID: PMC9586283 | PMID: 36215471
- Evidence: The carboxyl-terminal regions of Mlh1 and Pms1 were simultaneously modeled as a 1:1 heterodimer using Alphafold ( 49 ) using the web interface at https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFold2_advanced.ipynb .
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Integrated AlphaFold2 and DEER investigation of the conformational dynamics of a pH-dependent APC antiporter. (PNAS 2022)

- DOI: 10.1073/pnas.2206129119 | PMCID: PMC9407458 | PMID: 35969794
- Evidence: The structure of GadC was modeled using AlphaFold v.2.0.1 using a modified version of ColabFold ( 64 , 108 ).
- Full pipeline: quantification [ImageJ v1.53] -> structure determination [OpenMM] -> stage not stated [AlphaFold v2.0.1, ColabFold, SciPy]

### PTX3 structure determination using a hybrid cryoelectron microscopy and AlphaFold approach offers insights into ligand binding and complement activation. (PNAS 2022)

- DOI: 10.1073/pnas.2208144119 | PMCID: PMC9388099 | PMID: 35939690
- Version used: **1.3**
- Evidence: These were each submitted to the AlphaFold2 server ColabFold (v1.3) ( 52 ) as homotetramers.
- Full pipeline: structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [AlphaFold, ChimeraX, ColabFold v1.3, RELION v3.1]

### Metal cofactor stabilization by a partner protein is a widespread strategy employed for amidase activation. (PNAS 2022)

- DOI: 10.1073/pnas.2201141119 | PMCID: PMC9245657 | PMID: 35733252
- Evidence: AlphaFold2 models were generated using ColabFold ( 65 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, PHENIX]

### Interaction between S4 and the phosphatase domain mediates electrochemical coupling in voltage-sensing phosphatase (VSP). (PNAS 2022)

- DOI: 10.1073/pnas.2200364119 | PMCID: PMC9245683 | PMID: 35733115
- Evidence: Structural Modeling with ColabFold.
- Full pipeline: alignment/mapping [AlphaFold] -> differential/statistical testing [R] -> visualisation [PyMOL] -> stage not stated [ColabFold, ImageJ]

### Co-component signal transduction systems: Fast-evolving virulence regulation cassettes discovered in enteric bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203176119 | PMCID: PMC9214523 | PMID: 35648808
- Evidence: Candidate VtrC-like sequences found in tandem with VtrA-like transmembrane transcription factors were submitted to AlphaFold2 ( 32 ) structure prediction using ColabFold ( 35 ), which replaces the homology detection of AlphaFold2 with MMseqs2 ( 69 ), or with a local adaptation of AlphaFold described three paragraphs below.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, HMMER]

### Ancient proteins resolve controversy over the identity of <i>Genyornis</i> eggshell. (PNAS 2022)

- DOI: 10.1073/pnas.2109326119 | PMCID: PMC9995833 | PMID: 35609205
- Evidence: The protein structure of XCA-1 was inferred using the ColabFold AlphaFold2 notebook ( 101 , 102 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, MUSCLE v3.8.31] -> stage not stated [AlphaFold, ColabFold, R v4.1, RAxML v1.0.3, phytools]

### A mixed-valent Fe(II)Fe(III) species converts cysteine to an oxazolone/thioamide pair in methanobactin biosynthesis. (PNAS 2022)

- DOI: 10.1073/pnas.2123566119 | PMCID: PMC9060507 | PMID: 35320042
- Evidence: The interaction with MbnA was modeled using the newly accessible advanced version of ColabFold ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFold2_advanced.ipynb ) with the following parameters: MbnABC oligomeric ratio of 1:1:1; msa_method jackhmmer; msa_format fas; pair_mode unpaired+paired; pair_cov 50; pair_qid 20; rank_by pTMscore; use_turbo unchecked; num_...
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, PHENIX]

### A hyperpromiscuous antitoxin protein domain for the neutralization of diverse toxin domains. (PNAS 2022)

- DOI: 10.1073/pnas.2102212119 | PMCID: PMC8832971 | PMID: 35121656
- Evidence: Additional structural prediction was carried out for PanA Vib. har. with the AlphaFold2 ( 46 ) Colab notebook with default settings (“advanced” version; https://github.com/sokrypton/ColabFold ).
- Full pipeline: alignment/mapping [PyMOL v2.4.2] -> stage not stated [AlphaFold, ColabFold]

### Identification of a muropeptide precursor transporter from gut microbiota and its role in preventing intestinal inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2306863120 | PMCID: PMC10756304 | PMID: 38127978
- Evidence: We investigated the F4D5:ABC, the ABC-Am, and ABC-Hb heterodimers predictions using AlphaFold2 (AF2) through the Jupyter Notebook inside Google Collaboratory program called ColabFold.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, Jupyter]

### MEnTaT: A machine-learning approach for the identification of mutations to increase protein stability. (PNAS 2023)

- DOI: 10.1073/pnas.2309884120 | PMCID: PMC10710055 | PMID: 38039271
- Evidence: Modeling the structure of PAO using ColabFold ( 52 ) supports this notion, as the model suggests that residues 99 and 222 are close enough to permit such an interaction ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ColabFold]

### In vivo selection of synthetic nucleocapsids for tissue targeting. (PNAS 2023)

- DOI: 10.1073/pnas.2306129120 | PMCID: PMC10655225 | PMID: 37939083
- Evidence: ( G ) Superimposition of miniprotein structures predicted by ColabFold shows distinct conformations, despite similar protein sequences.
- Full pipeline: alignment/mapping [Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold]

### Molecular basis for Nse5-6 mediated regulation of Smc5/6 functions. (PNAS 2023)

- DOI: 10.1073/pnas.2310924120 | PMCID: PMC10636319 | PMID: 37903273
- Evidence: 1 B ) is predicted to form a loop by Alpha-Fold through the open source ColabFold ( Fig.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [ColabFold, RELION v3.0]

### Intracellular <i>Plasmodium</i> aquaporin 2 is important for sporozoite production in the mosquito vector and malaria transmission. (PNAS 2023)

- DOI: 10.1073/pnas.2304339120 | PMCID: PMC10622946 | PMID: 37883438
- Evidence: For folding of PfAPQX, sequences were first adapted manually, and tertiary structures were predicted using the ColabFold server, which uses sequence alignments generated by MMseqs2 and HHsearch followed by AlphaFold Monomer v2.0 to fold custom sequences ( 42 ).
- Full pipeline: alignment/mapping [ColabFold] -> stage not stated [AlphaFold]

### Bacterial SEAL domains undergo autoproteolysis and function in regulated intramembrane proteolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2310862120 | PMCID: PMC10556640 | PMID: 37756332
- Evidence: Protein structures were modeled using AlphaFold2 ( 21 ) and ColabFold run using the Alphafold2 Advanced Colab notebook ( 61 ) ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFold2_advanced.ipynb ) or downloaded (A0A6M4JFI2, A3DC27 , A3DCG3 , and A0A1V4I8Y9) from the Alphafold database ( 62 ) (available at: https://alphafold.ebi.ac.uk/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot] -> stage not stated [AlphaFold, ColabFold, PHENIX v1.20.1]

### Structural basis for binding of <i>Drosophila</i> Smaug to the GPCR Smoothened and to the germline inducer Oskar. (PNAS 2023)

- DOI: 10.1073/pnas.2304385120 | PMCID: PMC10410706 | PMID: 37523566
- Version used: **1.5.2**
- Evidence: For the AlphaFold2 predictions, the ColabFold v1.5.2 web interface ( 60 ) was used with standard settings except for the model_type, which was switched from “auto” to “alphaFold2_multimer_v3”.
- Full pipeline: structure determination [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, PHENIX]

### Pumping iron: A multi-omics analysis of two extremophilic algae reveals iron economy management. (PNAS 2023)

- DOI: 10.1073/pnas.2305495120 | PMCID: PMC10372677 | PMID: 37459532
- Evidence: Protein structure predictions were conducted using ColabFold ( 50 ) ( https://github.com/sokrypton/ColabFold ).
- Full pipeline: alignment/mapping [BLAST] -> visualisation [PyMOL v1.7.4] -> stage not stated [ColabFold, Cytoscape v3.4, OrthoFinder v2.5.2]

### Coordination of apicoplast transcription in a malaria parasite by internal and host cues. (PNAS 2023)

- DOI: 10.1073/pnas.2214765120 | PMCID: PMC10334805 | PMID: 37406097
- Evidence: For ApSigma structural predictions, we used a version of AlphaFold (version 2) available at https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb . that allows single predictions ( 45 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Clustal Omega] -> stage not stated [AlphaFold, ColabFold, R, UCSF Chimera]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Evidence: We predicted the protein structure of UGT66A1 using AlphaFold2 through ColabFold ( 59 , 60 ), resulting in a high-quality prediction ( SI Appendix , Fig.
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### GPCR targeting of E3 ubiquitin ligase MDM2 by inactive β-arrestin. (PNAS 2023)

- DOI: 10.1073/pnas.2301934120 | PMCID: PMC10334748 | PMID: 37399373
- Version used: **1.5.2**
- Evidence: The predicted model for rat Mdm2 was obtained using ColabFold v1.5.2 implementation of AlphaFold2 ( https://github.com/sokrypton/ColabFold ).
- Full pipeline: structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, ColabFold v1.5.2, PyMOL]

### Design of the elusive proteinaceous oxygen donor copper site suggests a promising future for copper for MRI contrast agents. (PNAS 2023)

- DOI: 10.1073/pnas.2219036120 | PMCID: PMC10318980 | PMID: 37364102
- Evidence: A computational model of the copper-bound MB1-2 peptide trimer, generated using ColabFold ( 38 ) and Metal3D ( 39 ), is in good agreement with our proposed design ( Fig.
- Full pipeline: visualisation [PyMOL v1.4] -> stage not stated [ColabFold]

### An end-to-end deep learning method for protein side-chain packing and inverse folding. (PNAS 2023)

- DOI: 10.1073/pnas.2216438120 | PMCID: PMC10266014 | PMID: 37253017
- Evidence: We generated a set of nonnative backbone structures for the CASP13 and CASP14 targets, using AlphaFold2 from ColabFold ( 44 ) with default MSA settings.
- Full pipeline: stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Evolution and diversification of the ACT-like domain associated with plant basic helix-loop-helix transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2219469120 | PMCID: PMC10175843 | PMID: 37126718
- Evidence: The βαββαβ secondary structures and tertiary protein structures of the ACT-like domains were predicted using PSIPRED ( 54 ) and AlphaFold ( 38 , 39 ) via the ColabFold interface ( 55 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [AlphaFold, ColabFold, RAxML v1.1.0]

### TapA acts as specific chaperone in TasA filament formation by strand complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2217070120 | PMCID: PMC10151520 | PMID: 37068239
- Evidence: Three-dimensional structure predictions based on the AlphaFold ( 24 ) algorithm were run via the publicly available ColabFold ( https://github.com/sokrypton/ColabFold ) ( 42 ) infrastructure through Google Colaboratory.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [AlphaFold, ColabFold] -> stage not stated [PyMOL]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Evidence: When no HHpred hit could be found, ColabFold ( 34 ) was used to predict the protein structure using the MAFFT cluster alignment (step VI) as a multiple sequence alignment (MSA) input.
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Clock-regulated coactivators selectively control gene expression in response to different temperature stress conditions in <i>Arabidopsis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216183120 | PMCID: PMC10120023 | PMID: 37036986
- Evidence: The structural models of LNK–RVE complexes were generated by using AlphaFold2 ( 24 ) via the Google Colaboratory (ColabFold) interface ( 25 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyMOL]

### Altered plasma membrane abundance of the sulfatide-binding protein NF155 links glycosphingolipid imbalances to demyelination. (PNAS 2023)

- DOI: 10.1073/pnas.2218823120 | PMCID: PMC10083573 | PMID: 36996106
- Version used: **1.3**
- Evidence: Structural models were generated using a locally installed version of ColabFold version 1.3, implementing AF2 machine learning structure prediction, with default parameters ( 51 , 52 ).
- Full pipeline: dimensionality reduction/clustering [ChimeraX] -> structure determination [ChimeraX] -> machine learning [AlphaFold] -> stage not stated [ColabFold v1.3, ImageJ]

### Characterization of a unique polysaccharide monooxygenase from the plant pathogen <i>Magnaporthe oryzae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2215426120 | PMCID: PMC9974505 | PMID: 36791100
- Evidence: The sequence of Mo PMO9A without its signal peptide [amino acids 1 to 19 by SignalP 6.0 ( 95 ) prediction] was used as an input into the Google Colab notebook: https://github.com/sokrypton/ColabFold (accessed 7/22/2021) using the code in the AlphaFold2_mmseqs2 notebook.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, Cytoscape] -> visualisation [Clustal Omega, Cytoscape] -> stage not stated [AlphaFold, ColabFold, ImageJ, R]

### Crystal structure of LGR ligand α2/β5 from <i>Caenorhabditis elegans</i> with implications for the evolution of glycoprotein hormones. (PNAS 2023)

- DOI: 10.1073/pnas.2218630120 | PMCID: PMC9910494 | PMID: 36574673
- Evidence: AlphaFold models were predicted by ColabFold ( 64 ) and then relaxed and energy-minimized in the Rosetta suite using the FastDesign protocol ( 65 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [CCP4] -> stage not stated [AlphaFold, ColabFold, PHENIX, PyMOL]

### Proteome-wide bioinformatic annotation and functional validation of the monotopic phosphoglycosyl transferase superfamily. (PNAS 2024)

- DOI: 10.1073/pnas.2417572121 | PMCID: PMC11626204 | PMID: 39602253
- Evidence: These remaining sequences were folded using ColabFold ( 43 , 66 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Evidence: For the initial model of CoaX, we used AlphaFold2 ( 64 ) to generate a monomer of CoaX through ColabFold ( 65 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Molecular basis for chemokine recognition and activation of XCR1. (PNAS 2024)

- DOI: 10.1073/pnas.2405732121 | PMCID: PMC11621518 | PMID: 39565315
- Evidence: A molecular model of the inactive XCR1 was generated with AlphaFold 2 using the ColabFold platform on Google Colaboratory.( 57 ) The sequence of human XCR1 was obtained from UniProt ( P46094 )( 82 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ColabFold, GROMACS, PyMOL v3.0.3]

### Comprehensive deletion scan of anti-CRISPR AcrIIA4 reveals essential and dispensable domains for Cas9 inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2413743121 | PMCID: PMC11621469 | PMID: 39570312
- Version used: **1.5.5**
- Evidence: ColabFold (version 1.5.5) ( 49 ), an open-source version of AlphaFold2 ( 21 ), was used to generate the structural models of AcrIIA4 homologs and deletion alleles through ChimeraX; of the predicted structures for each sequence, the highest confidence structure was used (restricting to relaxed structures for the predicted structures for deletion alleles).
- Full pipeline: differential/statistical testing [R, ggplot2] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, ChimeraX, ColabFold v1.5.5]

### Predicting multiple conformations of ligand binding sites in proteins suggests that AlphaFold2 may remember too much. (PNAS 2024)

- DOI: 10.1073/pnas.2412719121 | PMCID: PMC11621821 | PMID: 39565312
- Evidence: The selected protein sequences were used as input for the ColabFold version of AF2 ( 35 , 49 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyMOL]

### The conformational landscape of fold-switcher KaiB is tuned to the circadian rhythm timescale. (PNAS 2024)

- DOI: 10.1073/pnas.2412293121 | PMCID: PMC11551320 | PMID: 39475637
- Evidence: Single-sequence AF2 sampling was performed in ColabFold ( 51 ) using “msa_mode=single_sequence,” dropout=True, num_seeds=16, and all other options set to default.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [ColabFold, SciPy]

### SPATEs promote the survival of &lt;i&gt;Shigella&lt;/i&gt; to the plasma complement system upon local hemorrhage and bacteremia. (PNAS 2024)

- DOI: 10.1073/pnas.2319951121 | PMCID: PMC11551430 | PMID: 39475654
- Evidence: Since the 3D model of the passenger domain of SigA was not available, we generated molecular models for SigA 56-1008 (Uniprot-ID: Q3YXF8 from residue Met56 to Asn1008) using the structure prediction tool AlphaFold and ColabFold ( 27 ), a Web-interfaced implementation of AlphaFold 2.
- Full pipeline: stage not stated [AlphaFold, BLAST, ColabFold, PyMOL v1.8.4]

### Protein language models learn evolutionary statistics of interacting sequence motifs. (PNAS 2024)

- DOI: 10.1073/pnas.2406285121 | PMCID: PMC11551344 | PMID: 39467119
- Evidence: We predicted structure models in AlphaFold2 ( 1 ) using ColabFold ( 30 ); OmegaFold ( 2 ) using the OmegaFold notebook available at https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/omegafold.ipynb ; and ESMFold ( 4 ) using the ESMFold server available at https://esmatlas.com/resources?action=fold .
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [AlphaFold, ColabFold, SciPy]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: We used ColabFold’s implementation of AlphaFold-Multimer ( 51 ), which is shown to have a performance similar to the original implementation of AlphaFold-Multimer while using MMSeqs2 to search genomic databases orders of magnitude faster.
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### Membrane association and polar localization of the &lt;i&gt;Legionella pneumophila&lt;/i&gt; T4SS DotO ATPase mediated by two nonredundant receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2401897121 | PMCID: PMC11474061 | PMID: 39352935
- Evidence: Although small proteins like IcmT could not be definitively placed in this cryo-ET structure, a subcomplex of IcmT interacting with the N terminus of DotO was generated using ColabFold and successfully integrated into the density map ( 14 , 61 ).
- Full pipeline: quantification [ImageJ] -> structure determination [ColabFold] -> stage not stated [AlphaFold]

### Decoding the molecular mechanism of selective autophagy of glycogen mediated by autophagy receptor STBD1. (PNAS 2024)

- DOI: 10.1073/pnas.2402817121 | PMCID: PMC11406230 | PMID: 39236246
- Evidence: ( D ) Ribbon diagram showing the overall structure of the dimeric STBD1 LIR/RB1CC1 Claw complex model predicted by ColabFold.
- Full pipeline: stage not stated [ColabFold]

### Predicting protein conformational motions using energetic frustration analysis and AlphaFold2. (PNAS 2024)

- DOI: 10.1073/pnas.2410662121 | PMCID: PMC11363347 | PMID: 39163334
- Evidence: The MSA and AF2 structure prediction were performed using ColabFold ( 53 ).
- Full pipeline: dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Identification of a family of peptidoglycan transpeptidases reveals that &lt;i&gt;Clostridioides difficile&lt;/i&gt; requires noncanonical cross-links for viability. (PNAS 2024)

- DOI: 10.1073/pnas.2408540121 | PMCID: PMC11348318 | PMID: 39150786
- Version used: **1.5.5**
- Evidence: The VanW and YkuD domains were modeled with AF2 ( 36 ) using MMseqs2 ( 78 ) by running ColabFold v1.5.5 ( 79 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, ColabFold v1.5.5]

### Addressing epistasis in the design of protein function. (PNAS 2024)

- DOI: 10.1073/pnas.2314999121 | PMCID: PMC11348311 | PMID: 39133844
- Evidence: 40 , models generated using ColabFold ( 41 ) ( C ) Hydrogen bonds define the structure of a long loop that caps the active site and interacts with the substrate ( Left and Middle , PDB entry: 1uqz).
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### AlphaFold two years on: Validation and impact. (PNAS 2024)

- DOI: 10.1073/pnas.2315002121 | PMCID: PMC11348012 | PMID: 39133843
- Evidence: COOT ( 46 ) can import predictions from the AlphaFold Database, while ChimeraX ( 47 ) includes an option to generate new predictions in ColabFold ( 48 ).
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, ColabFold, PHENIX, RoseTTAFold]

### Structural basis for coupling of the WASH subunit FAM21 with the endosomal SNX27-Retromer complex. (PNAS 2024)

- DOI: 10.1073/pnas.2405041121 | PMCID: PMC11331091 | PMID: 39116126
- Evidence: AlphaFold2 ( 74 ) predictions were performed using the open-source ColabFold pipeline ( 75 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### A DNA condensation code for linker histones. (PNAS 2024)

- DOI: 10.1073/pnas.2409167121 | PMCID: PMC11331069 | PMID: 39116133
- Evidence: While AlphaFold is known to lack predictive power for modeling disordered regions ( 49 ), a prediction [using ColabFold with the default parameters ( 50 )] gave CH1 PA as mostly alpha helix, with a high confidence score, in contrast to CH1 ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Evidence: The structure of each sequence block was predicted using both ColabFold-AlphaFold2 ( 29 , 30 ) and ESMFold ( 31 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Structure of the flotillin complex in a native membrane environment. (PNAS 2024)

- DOI: 10.1073/pnas.2409334121 | PMCID: PMC11260169 | PMID: 38985763
- Evidence: The AlphaFold structures in this study were mainly generated from the AlphaFold2 implementation in the ColabFold notebooks ( 27 ) running on Google Colaboratory ( 66 ), using the default settings.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [ColabFold, Coot]

### Control of G protein-coupled receptor function via membrane-interacting intrinsically disordered C-terminal domains. (PNAS 2024)

- DOI: 10.1073/pnas.2407744121 | PMCID: PMC11260148 | PMID: 38985766
- Evidence: MD simulations of an mGluR3 construct containing both TM7 and the CTD (residues 796–879) used initial poses generated using AlphaFold2 ( 75 ) and ColabFold ( 76 ) which were equilibrated using the standard CHARMM-GUI-based protocol and scripts followed by a short, 6-ns run using OpenMM ( 77 ) and the CHARMM36m ( 78 ) forcefield and then simulated for 1,370 ns for each of six replicas.
- Full pipeline: simulation/modelling [AlphaFold, ColabFold, OpenMM]

### Pairing interacting protein sequences using masked language modeling. (PNAS 2024)

- DOI: 10.1073/pnas.2311887121 | PMCID: PMC11228504 | PMID: 38913900
- Evidence: Pairing methods employed in AFM and ColabFold.
- Full pipeline: machine learning [AlphaFold] -> stage not stated [ColabFold]

### APACE: AlphaFold2 and advanced computing as a service for accelerated discovery in biophysics. (PNAS 2024)

- DOI: 10.1073/pnas.2311888121 | PMCID: PMC11228474 | PMID: 38913887
- Evidence: However, we successfully addressed this constraint by adapting the ColabFold ( 14 ) code.
- Full pipeline: stage not stated [AlphaFold, ColabFold, Docker, Singularity, Slingshot]

### Machine learning in biological physics: From biomolecular prediction to design. (PNAS 2024)

- DOI: 10.1073/pnas.2311807121 | PMCID: PMC11228481 | PMID: 38913893
- Evidence: Efforts to allow scientists to experiment and fine-tune the Alphafold architecture gave rise to OpenFold ( 63 ) which allows scientists to retrain and analyze an open-source version of the Alphafold pipeline as well as ColabFold ( 64 ) for easy web-based access for those without access to powerful hardware.
- Full pipeline: stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### <i>Vibrio</i> MARTX toxin processing and degradation of cellular Rab GTPases by the cytotoxic effector Makes Caterpillars Floppy. (PNAS 2024)

- DOI: 10.1073/pnas.2316143121 | PMCID: PMC11194500 | PMID: 38861595
- Version used: **1.5.1**
- Evidence: Structure prediction models were generated in ChimeraX v 1.5.dev202207070159 using ColabFold v1.5.1 on the Google Colab virtual machine or with Alphafold2 v 2.2.2 (max template date 2022-05-23) on Northwestern’s Structural Biology Facility cluster.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [QuPath] -> dimensionality reduction/clustering [ChimeraX v1.5, ColabFold v1.5.1] -> stage not stated [AlphaFold]

### <i>Myxococcus xanthus</i> encapsulin cargo protein EncD is a flavin-binding protein with ferric reductase activity. (PNAS 2024)

- DOI: 10.1073/pnas.2400426121 | PMCID: PMC11126975 | PMID: 38748579
- Version used: **1.5.3**
- Evidence: A model of EncD T was generated using ColabFold v1.5.3: AlphaFold2 ( 47 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, ColabFold v1.5.3, MotionCor2, RELION v4.0]

### A finely balanced order-disorder equilibrium sculpts the folding-binding landscape of an antibiotic sequestering protein. (PNAS 2024)

- DOI: 10.1073/pnas.2318855121 | PMCID: PMC11098121 | PMID: 38709926
- Evidence: To generalize these observations across orthologs, we first predict the structure of TipAS from AlphaFold2 (AF2) via the ColabFold interface ( 25 , 26 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Lipid scrambling is a general feature of protein insertases. (PNAS 2024)

- DOI: 10.1073/pnas.2319476121 | PMCID: PMC11047089 | PMID: 38621120
- Evidence: For systems containing more than one chain and for which no structure was available, prediction was performed using AlphaFold-Multimer ( 94 ) which is implemented in ColabFold ( 65 ); for these cases, a total of 24 recycles were used.
- Full pipeline: simulation/modelling [AlphaFold, GROMACS] -> stage not stated [ColabFold]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; telomere-binding proteins TEBP-1 and TEBP-2 adapt the Myb module to dimerize and bind telomeric DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2316651121 | PMCID: PMC11032478 | PMID: 38588418
- Evidence: Alignment of sequences [using Clustal Omega ( 28 )] and structures (using AlphaFold-based ColabFold prediction ( 29 ) of TEBP-1 MCD3) of the MCD3 domain of TEBP-1 and TEBP-2 identified TEBP-1 R364, K412, S413, N416, S419, H420, R422, and K423 as equivalent to TEBP-2 DNA binding residues R357, K405, S406, N409, S412, H413, R415, and K416, suggesting that both proteins use a conserved mechanism to b...
- Full pipeline: alignment/mapping [Clustal Omega, ColabFold] -> structure determination [Coot] -> stage not stated [AlphaFold, PHENIX]

### Reconstitution of a biofilm adhesin system from a sulfate-reducing bacterium in <i>Pseudomonas fluorescens</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2320410121 | PMCID: PMC10990149 | PMID: 38498718
- Version used: **1.5.5**
- Evidence: We employed ColabFold (v1.5.5) to generate structural models of the domains of DvhA using AlphaFold2 with default parameters ( 47 , 48 ).
- Full pipeline: differential/statistical testing [R v4.3.0, ggplot2 v3.4.2] -> visualisation [R v4.3.0, ggplot2 v3.4.2] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL]

### Mechanistic insights into the interactions of TAX1BP1 with RB1CC1 and mammalian ATG8 family proteins. (PNAS 2024)

- DOI: 10.1073/pnas.2315550121 | PMCID: PMC10945755 | PMID: 38437556
- Evidence: To gain further mechanistic insights into the interaction of the TAX1BP1/RB1CC1/NAP1 ternary complex with ATG8 family protein, we also sought to predict the structure of the TAX1BP1/RB1CC1/NAP1/GABARAP complex using ColabFold.
- Full pipeline: stage not stated [ColabFold]

### Context-dependent design of induced-fit enzymes using deep learning generates well-expressed, thermally stable and active enzymes. (PNAS 2024)

- DOI: 10.1073/pnas.2313809121 | PMCID: PMC10945820 | PMID: 38437538
- Evidence: Chimeric enzymes were modeled using the ColabFold ( 26 ) implementation of AlphaFold2 ( Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyTorch]

### A billion years of evolution manifest in nanosecond protein dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2318743121 | PMCID: PMC10927572 | PMID: 38412135
- Evidence: We used ColabFold ( 61 ) to generate AlphaFold-predicted structures, and the Robetta server ( 36 ) for RosettaFold-predicted structures, both with default parameters.
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega, RoseTTAFold] -> stage not stated [ColabFold]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Evidence: Once established the ALOG-DBD DNA structure, we used Alphafold2 ColabFold (AFC) to analyze the interaction between ALOG and BOP proteins.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Mechanism and cellular function of direct membrane binding by the ESCRT and ERES-associated Ca<sup>2+</sup>-sensor ALG-2. (PNAS 2024)

- DOI: 10.1073/pnas.2318046121 | PMCID: PMC10907313 | PMID: 38386713
- Evidence: AlphaFold2 ( https://alphafold.ebi.ac.uk/ ) was run using the ColabFold notebook ( https://colab.research.google.com/github/sokrypton/ColabFold ) using version v1.5.2 on default settings.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis v2.0] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, ImageJ, OpenCV, PyMOL, Python, scikit-image]

### Loss of activation by GABA in vertebrate delta ionotropic glutamate receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2313853121 | PMCID: PMC10861852 | PMID: 38285949
- Evidence: An AlphaFold2 structural model of the Aca GluD LBD was created using ColabFold v2 without template information ( 68 , 69 ).
- Full pipeline: alignment/mapping [MAFFT v7.450] -> visualisation [PyMOL v4.6] -> stage not stated [AlphaFold, AutoDock Vina v4.2, ChimeraX v1.4, ColabFold]

### A novel cysteine-rich adaptor protein is required for mucin packaging and secretory granule stability in vivo. (PNAS 2024)

- DOI: 10.1073/pnas.2314309121 | PMCID: PMC10861859 | PMID: 38285943
- Evidence: In silico modeling using AlphaFold2 ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) suggests that Sgs7 and Sgs3 form a tetrameric structure by virtue of inter- and intramolecular disulfide bonding.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Methylation of ciliary dynein motors involves the essential cytosolic assembly factor DNAAF3/PF22. (PNAS 2024)

- DOI: 10.1073/pnas.2318522121 | PMCID: PMC10835030 | PMID: 38261620
- Evidence: ...ll vertebrate model structures were downloaded from UniProt ( https://www.uniprot.org/ ) while the Chlamydomonas predictions were generated using the ColabFold server ( 29 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyMOL]

### Decoupled evolution of the <i>Sex Peptide</i> gene family and <i>Sex Peptide Receptor</i> in Drosophilidae. (PNAS 2024)

- DOI: 10.1073/pnas.2312380120 | PMCID: PMC10801855 | PMID: 38215185
- Evidence: ( G ) The ColabFold top-ranked prediction of the interactions between SP (shown in green) and SPR (residues coloured by domain).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Arg-Tyr cation-π interactions drive phase separation and β-sheet assembly in native spider dragline silk. (PNAS 2025)

- DOI: 10.1073/pnas.2523198122 | PMCID: PMC12772222 | PMID: 41433062
- Evidence: Molecular dynamics simulations (1 µs) were conducted using GROMACS with the CHARMM36m force field, and structural models were generated with ColabFold and AlphaFold3.
- Full pipeline: simulation/modelling [AlphaFold, ColabFold, GROMACS]

### Molecular mechanisms underlying p62-dependent secretion of the Alzheimer-associated ubiquitin variant UBB&lt;sup&gt;+1&lt;/sup&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504528122 | PMCID: PMC12718301 | PMID: 41364760
- Evidence: Protein sequences of FL UBB +1 and the UBA domain of human SQSTM1/p62 (residues 387 to 436) were submitted to the AlphaFold3-based ColabFold pipeline ( 65 ) for structural prediction of a protein–protein complex.
- Full pipeline: visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold]

### Multiple weak brakes act in concert to control STIM1 and store-operated calcium entry. (PNAS 2025)

- DOI: 10.1073/pnas.2518622122 | PMCID: PMC12718381 | PMID: 41359834
- Evidence: The ColabFold implementation of AlphaFold2 ( 49 , 50 ) was used to generate models for residues 35 to 444 of human STIM1, with the following parameters: Num_relax = 0; Template_mode = none; MSA mode = mmseqs2_uniref_env; Pair_mode = unpaired_paired; Model_type = auto; Num_recycles = 48; Recycle_early_stop_tolerance = auto; Relax_max_iterations = 200; Pairing_strategy = greedy.
- Full pipeline: stage not stated [AlphaFold, ColabFold, ImageJ, Python]

### Structural modeling reveals the allosteric switch controlling the chitin utilization program of &lt;i&gt;&lt;i&gt;Vibrio cholerae&lt;/i&gt;&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2523358122 | PMCID: PMC12704726 | PMID: 41343673
- Evidence: 1 ) were generated using the AF-Mv3 algorithm ( 18 ) in ColabFold ( 16 ) on Indiana University’s BigRed200 and Quartz Supercomputers or using the AlphaFold3 algorithm ( 19 ) on the AlphaFold webserver.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, ColabFold, RoseTTAFold]

### A tripartite protein complex promotes DNA transport during natural transformation in Firmicutes. (PNAS 2025)

- DOI: 10.1073/pnas.2511180122 | PMCID: PMC12663950 | PMID: 41259146
- Evidence: We thank the Integrative Bioinformatics facility for making the ColabFold and multiple sequence alignment-tools pipelines easily accessible at the Institute for Integrative Biology of the Cell for Y.F., J.A., and R.G.
- Full pipeline: alignment/mapping [ColabFold, MAFFT] -> visualisation [AlphaFold, ChimeraX]

### WrtF from &lt;i&gt;Rhizobium tropici&lt;/i&gt; CIAT 899 is a GT-A fold fucosyltransferase that binds its donor nonproductively. (PNAS 2025)

- DOI: 10.1073/pnas.2512460122 | PMCID: PMC12595478 | PMID: 41166418
- Evidence: All structures were determined through molecular replacement using Phaser ( 71 ) in Phenix using a truncated ColabFold model of WrtF.
- Full pipeline: structure determination [Coot] -> stage not stated [ColabFold, PHENIX]

### Ubiquitin-mediated degradation restricts spatiotemporal accumulation of the cytoplasmic male sterility protein WA352 to anthers in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2504381122 | PMCID: PMC12557538 | PMID: 41100672
- Evidence: The structure of WA352 was predicted using AlphaFold2, which is available in ColabFold advanced notebook format at the following website for easy access: https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ( 53 ).
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> quantification [HISAT2, StringTie] -> stage not stated [AlphaFold, ColabFold]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Version used: **1.5**
- Evidence: To this end, we utilized the AlphaFold -based workflow provided by ColabFold v1.5 to predict 3D structures of LDH-As ( 19 ).
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### Glycosylated cannabinoids in &lt;i&gt;Cannabis sativa&lt;/i&gt; and enzyme design to modulate their synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2515688122 | PMCID: PMC12501178 | PMID: 40991441
- Evidence: The structure of CsUGT14 was modeled using AlphaFold2 ColabFold web server ( 43 ).
- Full pipeline: normalisation [R, edgeR] -> stage not stated [AlphaFold, ColabFold, ImageJ]

### A widespread family of molecular chaperones promotes the intracellular stability of type VIIb secretion system-exported toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2503581122 | PMCID: PMC12478183 | PMID: 40953262
- Evidence: AlphaFold2 (ColabFold) was used to predict the models of LtcA and LtcB, which were then used as search models to determine the X-ray crystal structures of the two proteins by molecular replacement ( 61 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [IQ-TREE] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Female membrane proteins regulate postmating ovulation in &lt;i&gt;Drosophila melanogaster&lt;/i&gt; by ovulin-dependent and -independent pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2508783122 | PMCID: PMC12452909 | PMID: 40920921
- Version used: **1.5.5**
- Evidence: Three independent AlphaFold-Multimer prediction screens were performed with ovulin against the above protein lists using the LocalColabFold ( github.com/YoshitakaMo/localcolabfold ) implementation of AlphaFold (ColabFold v1.5.5 and AlphaFold v2.3.2) ( 38 , 39 , 66 ).
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> variant calling [lme4] -> differential/statistical testing [emmeans, lme4] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.5.5]

### A tubulin-MAPKKK pathway engages tubulin isotype interaction for neuroprotection. (PNAS 2025)

- DOI: 10.1073/pnas.2507208122 | PMCID: PMC12403078 | PMID: 40811477
- Evidence: ( F and G ) Models of BEN-1(L246F)/TBA-1 (confidence scores: pLDDT = 90.9 pTM = 0.905 ipTM = 0.909) and BEN-1(L246F)/TBA-2 (confidence scores: pLDDT = 89.9 pTM = 0.906 ipTM = 0.904) heterodimers using ColabFold.
- Full pipeline: stage not stated [ColabFold]

### Nonsubstrate PI(4,5)P<sub>2</sub> interacts with the interdomain linker to control electrochemical coupling in voltage-sensing phosphatase (VSP). (PNAS 2025)

- DOI: 10.1073/pnas.2500651122 | PMCID: PMC12337349 | PMID: 40729387
- Evidence: ( A ) Left : Structural model of Ci-VSP predicted using ColabFold ( 9 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> visualisation [PyMOL, VMD] -> stage not stated [ColabFold]

### SpbR controls lipoteichoic acid length by directly inhibiting signal peptidase SpsB in &lt;i&gt;Staphylococcus aureus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426464122 | PMCID: PMC12260438 | PMID: 40587784
- Evidence: The AlphaFold2_advanced ColabFold notebook was used ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) to model protein complexes ( 63 , 64 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### In silico evolution of globular protein folds from random sequences. (PNAS 2025)

- DOI: 10.1073/pnas.2509015122 | PMCID: PMC12260532 | PMID: 40587803
- Version used: **1.5.5**
- Evidence: ColabFold v1.5.5 was used to predict structures with custom MSAs, which were extracted from PFES ( 70 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, ColabFold v1.5.5, RoseTTAFold]

### Identification of a VPS29 isoform with restricted association to Retriever and Retromer accessory proteins through autoinhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2501111122 | PMCID: PMC12260524 | PMID: 40587794
- Evidence: To obtain the model of VPS29C and VPS29C containing Retromer, we applied the AlphaFold2 neural network of the open-source ColabFold pipeline.
- Full pipeline: alignment/mapping [ChimeraX v1.6.1, PyMOL] -> differential/statistical testing [R] -> machine learning [AlphaFold, ColabFold] -> visualisation [ChimeraX v1.6.1, Cytoscape v3.3, Metascape v3.5, PyMOL] -> stage not stated [IQ-TREE v2.2.5]

### Enzymatic carbon-fluorine bond cleavage by human gut microbes. (PNAS 2025)

- DOI: 10.1073/pnas.2504122122 | PMCID: PMC12184663 | PMID: 40512801
- Evidence: Structural models for the seven initial dehalogenase sequences selected from the HumGut databases, were generated using AF ColabFold ( 69 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R] -> simulation/modelling [AlphaFold, GROMACS] -> visualisation [Cytoscape] -> stage not stated [ColabFold, IQ-TREE]

### Structural basis of the hepatitis B virus X protein in complex with DDB1. (PNAS 2025)

- DOI: 10.1073/pnas.2421325122 | PMCID: PMC12184330 | PMID: 40512786
- Evidence: ...eshold 2.86 (FSC = 0.143) 2.68 (FSC = 0.143) 3.35 (FSC = 0.143) Refinement Initial model used (PDB code) PDB:2B5M and predicted structure model using ColabFold PDB:2B5M and predicted structure model using ColabFold Model composition Nonhydrogen atoms Protein residues Ligands 8,834 1,127 0 8,936 1,141 0 R.m.s. deviations Bond lengths (Å) Bond angles (°) 0.009 0.960 0.004 0.965 Validation MolProbity...
- Full pipeline: simulation/modelling [AlphaFold] -> structure determination [ColabFold] -> stage not stated [RELION]

### HCK regulates NLRP12-mediated PANoptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2422079122 | PMCID: PMC12130821 | PMID: 40408404
- Version used: **1.5.5**
- Evidence: Structure modeling of these protein sequences was performed using AlphaFold2 via ColabFold v1.5.5 ( 34 , 35 ).
- Full pipeline: differential/statistical testing [limma v3.60.2] -> simulation/modelling [R] -> visualisation [ChimeraX v1.8, R] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.8]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Version used: **1.5.5**
- Evidence: AlphaFold structure prediction was performed using ColabFold v1.5.5: AlphaFold2 with MMseqs2 ( 52 , 53 ), providing the amino acid sequence of LalbCCR1 ( LalbChr03g0025491 ).
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### Identification of the lydiamycin biosynthetic gene cluster in a plant pathogen guides structural revision and identification of molecular target. (PNAS 2025)

- DOI: 10.1073/pnas.2424388122 | PMCID: PMC12130866 | PMID: 40388608
- Version used: **1.2**
- Evidence: A structural model of LydA was obtained using ColabFold v1.2 ( 81 ).
- Full pipeline: alignment/mapping [ChimeraX v1.5, Clustal Omega, RAxML] -> visualisation [Cytoscape v3.8.2] -> stage not stated [ColabFold v1.2]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Evidence: To predict the monomeric structure of Bik-1 Gag, we used AlphaFold2 via the ColabFold notebook ( 30 , 71 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### DprA recruits ComM to facilitate recombination during natural transformation in Gram-negative bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2421764122 | PMCID: PMC12012524 | PMID: 40215278
- Version used: **1.5.2**
- Evidence: For all identified DprA homologs, we performed protein structure prediction using AlphaFold v2.3 ( 30 ) as implemented in the ColabFold v1.5.2 pipeline ( 31 ).
- Full pipeline: alignment/mapping [PyMOL v3.0] -> stage not stated [AlphaFold v2.3, ChimeraX v1.9, ColabFold v1.5.2]

### Structural assembly of the PAS domain drives the catalytic activation of metazoan PASK. (PNAS 2025)

- DOI: 10.1073/pnas.2409685122 | PMCID: PMC11962487 | PMID: 40106358
- Evidence: AlphaFold models for rifleman, West African lungfish, and Himalayan leaf-nosed bat PASK were generated using ColabFold with Amber molecular dynamic relaxation ( 25 ).
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold, ChimeraX v1.7, ColabFold, RoseTTAFold]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; uses a GGDEF protein to recruit diacylglycerol kinase to the membrane for lipid recycling. (PNAS 2025)

- DOI: 10.1073/pnas.2414696122 | PMCID: PMC11962490 | PMID: 40100631
- Version used: **1.5.5**
- Evidence: ColabFold v1.5.5 was used to generate AlphaFold2-based models of GdpS–DgkB complexes ( 39 , 40 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.5]

### Conserved leucine-rich repeat proteins in the adhesive projectile slime of velvet worms. (PNAS 2025)

- DOI: 10.1073/pnas.2416282122 | PMCID: PMC11962477 | PMID: 40100627
- Evidence: ( https://golgi.sandbox.google.com/ ), ESMFold, RoseTTAFold2, OmegaFold ( https://github.com/sokrypton/ColabFold ), and Chai-1 ( https://lab.chaidiscovery.com/ ) ( 47 , 48 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, ColabFold]

### A horizontally transferred bacterial gene aids the freezing tolerance of Antarctic bdelloid rotifers. (PNAS 2025)

- DOI: 10.1073/pnas.2421910122 | PMCID: PMC11912409 | PMID: 40035762
- Evidence: Protein structures were predicted with the ColabFold notebook ( 43 ) which is based on AlphaFold21 ( 44 ) and implemented by UCSF ChimeraX v.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.6r, ColabFold]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Evidence: For additional validation of the interaction, we docked in parallel LHL4 for the core complex on the HADDOCK webserver ( 81 ), using the identified cross-links as distance constraints and predicting the pairwise interaction between CP43/CP47 and LHL4 with Alphafold2 multimer algorithm in ColabFold ( 82 ).
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Seesaw protein: Design of a protein that adopts interconvertible alternative functional conformations and its dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2412117122 | PMCID: PMC11848303 | PMID: 39928865
- Evidence: Although ColabFold (an AlphaFold2-based open-source software) ( 38 , 39 ) only predicted all the SSPs as DHFR-biased states ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold, ImageJ]

### Reenacting a mouse genetic evolutionary arms race in yeast reveals that SLXL1/SLX compete with SLY1/2 for binding to Spindlins. (PNAS 2025)

- DOI: 10.1073/pnas.2421446122 | PMCID: PMC11848428 | PMID: 39928872
- Evidence: AlphaFold Multimer structure predictions of protein interactions were performed using ColabFold-MMseqs2 notebook ( 31 ). msa_mode was set to mmseqs2_uniref_env, pair_mode to unpaired_paired, model_type to AlphaFold2-multimer-v2 and num_recycles to 3.
- Full pipeline: alignment/mapping [RepeatMasker] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold]

### The C2 domain augments Ras GTPase-activating protein catalytic activity. (PNAS 2025)

- DOI: 10.1073/pnas.2418433122 | PMCID: PMC11831179 | PMID: 39899710
- Evidence: Monomeric AlphaFold structure predictions were obtained from the AlphaFold Protein Structure Database and multimer predictions were generated using ColabFold.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### High-throughput discovery of inhibitory protein fragments with AlphaFold. (PNAS 2025)

- DOI: 10.1073/pnas.2322412122 | PMCID: PMC11831152 | PMID: 39899719
- Evidence: Materials and Methods ColabFold with AlphaFold2 monomer weights was used to predict fragment–protein interactions.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Plant BCL-DOMAIN HOMOLOG proteins play a conserved role in SWI/SNF complex stability. (PNAS 2025)

- DOI: 10.1073/pnas.2413346122 | PMCID: PMC11761322 | PMID: 39823297
- Evidence: The Arabidopsis (MINU1 HSA -ARP4-ARP7-BDH1) and Human (BRG1 HSA -ACTL6-ACTB-BCL7A) complexes, as well as the chimeric Rtt102–Arabidopsis complex, were modeled with AlphaFold2 (v.2) ( 29 ) and AlphaFold-multimer ( 31 ) using a colab notebook running ColabFold ( 48 ) v1.5.5.
- Full pipeline: stage not stated [AlphaFold, ColabFold, deepTools v3.5.1, ggplot2]

### A divergent two-domain structure of the anti-Müllerian hormone prodomain. (PNAS 2025)

- DOI: 10.1073/pnas.2418088122 | PMCID: PMC11760506 | PMID: 39805014
- Evidence: Only when the experimental structure was provided as a template using ColabFold, did the resulting models approach the conformation of the experimental structure.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Tetrameric PilZ protein stabilizes stator ring in complex flagellar motor and is required for motility in &lt;i&gt;Campylobacter jejuni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2412594121 | PMCID: PMC11725899 | PMID: 39793078
- Evidence: The full-length structure of FlgX was generated using ColabFold, an online implementation of AlphaFold2 ( 60 , 61 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, ColabFold, MotionCor2]

### GSK-3β coordinates axonal microtubule organization through Shot and Tau. (PNAS 2026)

- DOI: 10.1073/pnas.2516746123 | PMCID: PMC12933142 | PMID: 41701831
- Evidence: Our structural in silico analysis using ColabFold/AlphaFold2 suggests that a key GSK-3β target cluster is in a linker region between Shot’s two Eb1 dimer-binding SxIP sites and the SxLP site ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [AlphaFold, ColabFold] -> visualisation [ChimeraX] -> stage not stated [Fiji, ImageJ]

### Soluble adenylyl cyclase in nonmammalian sperm is directly controlled by pH, not by HCO&lt;sub&gt;3&lt;/sub&gt;&lt;sup&gt;-&lt;/sup&gt; or Ca&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2505026123 | PMCID: PMC12867704 | PMID: 41591904
- Version used: **1.5.2**
- Evidence: Modeling in AlphaFold2 v2.2.4 was performed within the ColabFold v1.5.2 pipeline ( 96 ), with multiple sequence alignments generated using MMSeqs2 ( 97 ).
- Full pipeline: alignment/mapping [AlphaFold v2.2.4, ColabFold v1.5.2, MAFFT] -> stage not stated [BLAST, SciPy v1.15.1, statsmodels v0.14.4]

### Dynamic regulation of receptor-modulated endothelial NADPH oxidases. (PNAS 2026)

- DOI: 10.1073/pnas.2531380123 | PMCID: PMC12846790 | PMID: 41557791
- Evidence: ( D ) Docking of p22 (gray structure) with NOX4 (blue structure) modeled by ColabFold.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Proton-selective conductance and gating of the lysosomal cation channel TMEM175. (PNAS 2026)

- DOI: 10.1073/pnas.2503909123 | PMCID: PMC12818570 | PMID: 41533442
- Evidence: To fill the existing gaps between residue 173 and residue 254 in both structures, the Alphafold2-multimer model as implemented by ColabFold was used to generate five individual structures each ( 21 , 22 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> stage not stated [ColabFold, VMD]

### Exploring structural diversity across the protein universe with The Encyclopedia of Domains. (Science 2024)

- DOI: 10.1126/science.adq4946 | PMCID: PMC7618865 | PMID: 39480926
- Evidence: This model features a significant number of structural defects not typical of AF2 models. “Re-folding” the sequence in ColabFold ( 41 ) produces a number of visually striking structures across the five AF2 models, the variation of which, along with their unusually low plDDT scores, strongly indicates that AF2 has hallucinated these folds and that they should likely be disregarded.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: A multiple sequence alignment of 5 concatenated repeats from the 42 orthologs was converted to a3m format and provided as the input for the ColabFold implementation of AlphaFold2 ( 21 , 55 ) with settings --num-recycle 40 --num-models 5.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Molecular mechanism of dynein-dynactin complex assembly by LIS1. (Science 2024)

- DOI: 10.1126/science.adk8544 | PMCID: PMC7615804 | PMID: 38547289
- Evidence: AlphaFold2 prediction All structure predictions were performed using AlphaFold2 through a local installation of ColabFold ( 110 ) running MMseqs2 ( 111 ) for homology searches and AlphaFold2 ( 112 ) or AlphaFold2-Multimer ( 113 ) for the predictions of single or multiple chains, respectively.
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [R] -> registration [MotionCor2, RELION] -> differential/statistical testing [R] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, ImageJ, UCSF Chimera]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: The 47,428 representatives were folded using AlphaFold2 via local ColabFold with default parameters ( fig.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

