# minimap2

- **Category:** genomics
- **Papers in survey:** 173
- **Journals:** Nature (86), PNAS (71), Cell (11), Science (5)
- **Years:** 2021 (15), 2022 (25), 2023 (30), 2024 (31), 2025 (50), 2026 (22)
- **Versions named:** 2.17 (24), 2.24 (16), 2.26 (8), 2.22 (5), 2.20 (4), 2.28 (3), 2.12 (3), 2.15 (2), 2.21 (2), 2.18 (2)
- **Pipeline stages it appears in:** alignment/mapping (140), read trimming (10), variant calling (9), visualisation (5), dimensionality reduction/clustering (2), quality control (1), registration (1), quantification (1)

## Papers

### Generation and transmission of interlineage recombinants in the SARS-CoV-2 pandemic. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.014 | PMCID: PMC8367733 | PMID: 34499854
- Evidence: As part of the COG-UK daily analytical pipeline ( https://github.com/COG-UK/datapipe ), the consensus genome sequences of the complete set of UK samples were aligned to the SARS-CoV-2 reference sequence (GenBank: MN908947.3 ) using Minimap2 ( Li, 2018 ).
- Full pipeline: alignment/mapping [Pangolin, minimap2] -> variant calling [Python] -> structure determination [IQ-TREE v2.1] -> stage not stated [SAMtools, TreeTime]

### A selective sweep in the Spike gene has driven SARS-CoV-2 human adaptation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.007 | PMCID: PMC8260498 | PMID: 34289344
- Evidence: ...3: yeast cloning vector Sikorski and Hieter, 1989 pRS313 pRS313-T7-N This paper N/A Software and algorithms Minimap 2 Li, 2018 https://github.com/lh3/minimap2 MAFFT Katoh and Standley, 2013 https://mafft.cbrc.jp/alignment/software/ OmegaPlus Alachiotis et al., 2012 https://cme.h-its.org/exelixis/web/software/omegaplus/index.html RAiSD Alachiotis and Pavlidis, 2018 https://github.com/alachins/raisd...
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> stage not stated [Pangolin, PyMOL]

### The monoclonal antibody combination REGEN-COV protects against SARS-CoV-2 mutational escape in preclinical and human studies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.002 | PMCID: PMC8179113 | PMID: 34161776
- Evidence: ...ryoSPARC v2.14.2 Punjani et al., 2017 https://cryosparc.com/ The PyMOL Molecular Graphics System, Version 2.4.1 Schrödinger, LLC https://pymol.org/2/ Minimap2 Li, 2018 https://github.com/lh3/minimap2 Swiftbiosciences primerclip software (v0.3.8) Swift Biosciences https://github.com/swiftbiosciences/primerclip Picard package Broad Institute https://github.com/broadinstitute/picard samtools (v1.9) L...
- Full pipeline: variant calling [GATK, Picard, SAMtools v1.9] -> stage not stated [PHENIX v1.19.1, PyMOL, minimap2]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...lore http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ Version 0.6.5 BWA Li, 2013 Version 0.7.5 iVar Grubaugh et al., 2019 Version 1.2.2 Minimap2 Li, 2018 Version 2.17 Baltic Python library https://github.com/evogytis/baltic N/A Artic sequencing bioinformatic pipeline Artic network https://artic.network/ncov-2019 N/A Miniconda Anaconda http://www.anaconda.com Anaconda Version 2-2.4.0 ...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Two-component spike nanoparticle vaccine protects macaques from SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.035 | PMCID: PMC7834972 | PMID: 33577765
- Evidence: ...N/A Flowjo v10 Flowjo N/A UCSF ChimeraX Goddard et al., 2018 N/A GraphPad Prism v7 GraphPad N/A Canu Koren et al., 2017 https://github.com/marbl/canu Minimap2 Li, 2018 https://github.com/lh3/minimap2 Varscan Koboldt et al., 2012 http://varscan.sourceforge.net/ Longshot Edge and Bansal, 2019 https://github.com/pjedge/longshot INTELLISPACE PORTAL 8 software Philips healthcare https://www.philips.sa/...
- Full pipeline: stage not stated [Canu, ChimeraX, minimap2]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Version used: **2.17**
- Evidence: ...p://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis pipeline) GitHub https://github.com/roblanf/sarscov2phylo Minimap2 v2.17 Li, 2018 https://github.com/lh3/minimap2 trimAl v1.2 Capella-Gutiérrez et al., 2009 http://trimal.cgenomics.org RAxML v8.2.12 Stamatakis, 2014 https://cme.h-its.org/exelixis/web/software/raxml CmdStan v2.28.1 The Stan Development Team ...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **2.17**
- Evidence: 1.11) ( Li et al., 2009 ), Minimap2 (v.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **2.17**
- Evidence: ...cingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis pipeline) GitHub,2022 https://github.com/roblanf/sarscov2phylo Minimap2 v2.17 ( Li, 2018 ) https://github.com/lh3/minimap2 trimAl v1.2 ( Capella-Gutiérrez et al., 2009 ) http://trimal.cgenomics.org RAxML v8.2.12 ( Stamatakis, 2014 ) https://cme.h-its.org/exelixis/web/software/raxml BEAST2 v2.6.6 ( Bouckaert et a...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Genetic manipulation of Patescibacteria provides mechanistic insights into microbial dark matter and the epibiotic lifestyle. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.017 | PMCID: PMC10633639 | PMID: 37683634
- Evidence: Reads were mapped to the assembled Se ML1 genome or the Nl TM7x genome (GenBank: NZ_CP007496 ) using minimap2 and variants were called using LoFreq v2.
- Full pipeline: alignment/mapping [MUSCLE, minimap2] -> dimensionality reduction/clustering [R] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Flye v2.9, HMMER]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Version used: **2.17**
- Evidence: ...and Recognition (LASER) This Paper https://doi.org/10.5281/zenodo.7759428 https://github.com/hilgers-lab/LASER R 4.1.1 N/A https://www.R-project.org/ Minimap2 v2.17-r941 Li 87 https://github.com/lh3/minimap2 NanoPlot 1.29.1 N/A https://github.com/wdecoster/NanoPlot guppy-5.0.7 model: dna_r9.4.1_450bps_sup.cfg Oxford Nanopore https://github.com/nanoporetech/pyguppyclient snakePipes v1.2.2 Bhardwaj ...
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### A synthetic differentiation circuit in Escherichia coli for suppressing mutant takeover. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.024 | PMCID: PMC10882425 | PMID: 38320549
- Version used: **2.21**
- Evidence: ...Addgene: 214227 pDSG601 This paper GenBank: OR829929 ; Addgene: 214228 pDSG602 This paper GenBank: OR829930 ; Addgene: 214229 Software and algorithms minimap2 (v.
- Full pipeline: stage not stated [SAMtools v1.12, minimap2 v2.21]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: C. neptuna-MAG was performed using minimap2 (ref.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: Then the cleaned reads were aligned to mm10combine using minimap2 45 (version 2.17) with parameters: -x map-ont -c --secondary=no -t 16.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: For genomes with a combined assembly size larger than 4 Gb, we used Minimap2 90 with parameters -ax map-pb instead of Blasr 91 to overcome reference index size limitations.
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Evolutionary and biomedical insights from a marmoset diploid genome assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03535-x | PMCID: PMC8189906 | PMID: 33910227
- Evidence: To validate this result, we collected sequences of bacterial artificial chromosome mapped to the marmoset Y chromosome from NCBI and mapped them to mCalJac1 with minimap2.
- Full pipeline: alignment/mapping [BCFtools, BWA, GATK, freebayes v1.3.1, minimap2] -> variant calling [GATK, freebayes v1.3.1]

### Platypus and echidna genomes reveal mammalian biology and evolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03039-0 | PMCID: PMC8081666 | PMID: 33408411
- Version used: **2.13**
- Evidence: Assembled Y contigs were mapped to the platypus assembly using BWA MEM and Y-BAC PacBio reads were mapped using minimap2 (v.2.13) 48 .
- Full pipeline: alignment/mapping [BWA, HISAT2, minimap2 v2.13] -> quantification [ggplot2 v3.2.1] -> normalisation [ggplot2 v3.2.1] -> stage not stated [ImageJ v2.0.0, RepeatMasker v4.0.6]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Version used: **2.17**
- Evidence: The data were aligned with minimap2 (v.2.17-r941) 53 to the control RNA sequence and Samtools (v.1.9) 54 stats was used to calculate the run error rate, which amounted to 6.72 %.
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: Nanopore data analysis For Nanopore sequence data, base calling and read alignment were performed using Guppy v.3 and Minimap2, respectively 51 , 52 .
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: The HiFi reads were then mapped to scaffolds using minimap2 and heterozygous SNPs called using DeepVariant 66 .
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: Sequencing reads were aligned to GRCh38 using minimap2 80 version 2.17.
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Version used: **2.17**
- Evidence: Minimap2 v.2.17 (ref.
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### Context-specific emergence and growth of the SARS-CoV-2 Delta variant. (Nature 2022)

- DOI: 10.1038/s41586-022-05200-3 | PMCID: PMC9534748 | PMID: 35952712
- Evidence: All sequences were aligned to the reference Wuhan-Hu-1 (GenBank accession MN908947.3 ) with minimap2 and samples with less than 93% coverage were discarded.
- Full pipeline: alignment/mapping [minimap2] -> structure determination [BEAST v1.10] -> visualisation [Python] -> stage not stated [Pangolin]

### Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission. (Nature 2022)

- DOI: 10.1038/s41586-022-05049-6 | PMCID: PMC9433318 | PMID: 35798029
- Evidence: In brief, sequencing reads were aligned with minimap2 (ref.
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Python] -> stage not stated [SAMtools, kallisto]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Evidence: SNP and indel calling using HiFi reads The HiFi reads were first mapped to SL5.0 using minimap2 (ref.
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **2.21**
- Evidence: Identification of hemizygous genes To identify regions present in MTGs but absent in ATGs, we mapped HiFi reads of each accession to its corresponding MTGs using minimap2 (v.2.21-r1071) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **2.17**
- Evidence: Lastz (v.1.02.00) 76 and Minimap2 (v.2.17-r941) 77 were used to compare the Bamaxiang contig and the 40 kb sequence spanning the ABO gene of the S. scrofa build 11.1 reference genome.
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Version used: **2.17**
- Evidence: Reads were mapped to the custom genome using minimap2 (v.2.17-r941) with the ‘-x map-ont’ parameter.
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Raw fastqs were aligned to a section of chromosome 19 containing the entire UNC13A gene (17690344-17599328; GRCh38.p13) using Minimap2 48 with settings “-ax splice”.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Malaria protection due to sickle haemoglobin depends on parasite genotype. (Nature 2022)

- DOI: 10.1038/s41586-021-04288-3 | PMCID: PMC8810385 | PMID: 34883497
- Evidence: We then used minimap2 60 to align these sequences to a previously generated set of genome assemblies from P. falciparum isolates and laboratory strains 38 (Supplementary Table 7 ), allowing for multiple possible mapping locations.
- Full pipeline: alignment/mapping [MAFFT, STAR v2.7.3a, minimap2] -> variant calling [GATK] -> stage not stated [Stan]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Evidence: The short-read data were mapped using bwa-mem2 (v.2.2.1), with -Y optional parameter, and the long-read data were mapped using minimap2 46 (v.2.22) with the following optional parameters: -x map-ont -a–secondary=no–MD.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### A molnupiravir-associated mutational signature in global SARS-CoV-2 genomes. (Nature 2023)

- DOI: 10.1038/s41586-023-06649-6 | PMCID: PMC10651478 | PMID: 37748513
- Evidence: We mapped these reads to the Hu-1 reference genome using minimap2 and then extracted the number of calls for each base at each position.
- Full pipeline: alignment/mapping [IQ-TREE, TreeTime, minimap2] -> dimensionality reduction/clustering [IQ-TREE, TreeTime] -> structure determination [IQ-TREE, TreeTime] -> stage not stated [Nextstrain]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Version used: **2.17**
- Evidence: These reads were mapped with minimap2 (version 2.17) to both the human reference genome (hg38), and the sequence of the expected lentiviral insert 49 .
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Iso-seq data were mapped using minimap2 75 (v.2.21; parameters: -ax splice -uf –secondary=no -C5) and the redundant isoforms were further collapsed into transcript loci using cDNA_Cupcake (v.12.4.0; http://github.com/Magdoll/cDNA_Cupcake ; parameters: --dun-merge-5-shorter).
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Evidence: Long-read data were basecalled using guppy-basecaller, demultiplexed using guppy-barcoder and aligned to the CFTR BAC reference or the BAC-corrected reference with minimap2.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### A pangenome reference of 36 Chinese populations. (Nature 2023)

- DOI: 10.1038/s41586-023-06173-7 | PMCID: PMC10322713 | PMID: 37316654
- Evidence: Variant identification from the phased assembly The obtained HiFi reads were aligned to the T2T-CHM13 v2.0 reference by minimap2 using the preset parameters -ax map-hifi, and then sorted by samtools sort.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> variant calling [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BCFtools, QUAST v5.2.0, pheatmap v1.0.12]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **2.23**
- Evidence: Genome annotations The unicellular outgroup genome assemblies were annotated by mapping their transcripts from the original assemblies to the Hi-C scaffolded assemblies using minimap2 (v.2.23) 84 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### Increased mutation and gene conversion within human segmental duplications. (Nature 2023)

- DOI: 10.1038/s41586-023-05895-y | PMCID: PMC10172114 | PMID: 37165237
- Version used: **2.24**
- Evidence: Whole-genome alignments and synteny definition Whole-genome alignments were calculated against T2T-CHM13 v1.1 with a copy of GRCh38 chrY using minimap2 v2.24 (ref.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [hifiasm] -> stage not stated [RepeatMasker v4.1.2]

### Widespread somatic L1 retrotransposition in normal colorectal epithelium. (Nature 2023)

- DOI: 10.1038/s41586-023-06046-z | PMCID: PMC10191854 | PMID: 37165195
- Evidence: Long-read, whole-genome sequence analysis Sequenced reads were mapped to the human reference genome (GRCh37) using pbmm2 ( https://github.com/PacificBiosciences/pbmm2 ), a wrapper for minimap2 (ref.
- Full pipeline: read trimming [Bismark] -> alignment/mapping [BWA, Bismark, minimap2] -> stage not stated [Cutadapt, DELLY, Picard]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: Manually fixing issues We used paftools.js asmgene, from the minimap2 repository ( https://github.com/lh3/minimap2/tree/master/misc ) 76 to count the number of apparent gene duplications for each of the assemblies produced by Trio-Hifiasm (v.0.14).
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Version used: **2.12**
- Evidence: To correct sequencing errors, we processed this sequence file to two successive rounds of consensus by aligning Pacbio reads with minimap2 (v.2.12, map-pb setting) 64 and Racon (v.1.3.1) using the default parameters followed by one final round of consensus using the Illumina reads.
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: Passed reads from Minknow were mapped to the reference AAV2 genome ( NC_001401 ) using minimap2 (ref.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **2.20**
- Evidence: The dovetail Omni-C data were aligned to the resulting contigs using minimap2 v2.20 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Insulin-regulated serine and lipid metabolism drive peripheral neuropathy. (Nature 2023)

- DOI: 10.1038/s41586-022-05637-6 | PMCID: PMC9891999 | PMID: 36697822
- Version used: **2.17**
- Evidence: In summary, the raw reads were adapter filtered using the auto-detect parameters in fastp version 20 54 and host (mouse) filtered using minimap2 version 2.17 55 .
- Full pipeline: read trimming [fastp, minimap2 v2.17] -> alignment/mapping [Bowtie2 v2.4.2] -> quantification [ImageJ v1.53e] -> stage not stated [QIIME 2 v2020.11, Stan]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Long reads mapping to the short-read-assembled MAG and the long-read-assembled non-circular contig were extracted using minimap2 (ref.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **2.20**
- Evidence: SNP and SV calling Reciprocal genome alignment, in which each of the pangenome assemblies was aligned to the MorexV3 assembly with the latter acting either as alignment query or reference, was done with Minimap2 (v.2.20) 65 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: The FASTQ files were then aligned to the mouse reference genome (GRCm39) using the Minimap2 aligner (version 2.28) with default parameters.
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **2.26**
- Evidence: Assembly of circular ecDNA contigs ONT reads were aligned to GRCh38 with minimap2 (v.2.26-r1175) 112 with flags -a–L -–D --cs -x map-ont, and coordinate-sorted with samtools (v.1.18) 113 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: Unpaired reads and reads mapped to the PhiX reference genome using minimap2 62 version 2.17-r941 were excluded from further analyses.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Evidence: Additional assemblies were subsequently added to our analysis by using minimap2 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **2.22**
- Evidence: The same long reads were aligned to the Flye contigs (filtered to keep only the longest alternatives) using minimap2 2.22-r1101 (ref.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Version used: **2.17**
- Evidence: For a given genus/sample combination we used minimap2 (v.2.17-r941) 58 to map all reads classified to that genus to corresponding reference genomes of all species within that genus.
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Bridge RNAs direct programmable recombination of target and donor DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07552-4 | PMCID: PMC11208160 | PMID: 38926615
- Evidence: These flanking sequences were then mapped back to the plasmid sequences and the E. coli genome using minimap2 (Li 2018), and assigned as originating from the plasmid or the E. coli genome according to whichever had the higher alignment score.
- Full pipeline: alignment/mapping [BWA, minimap2] -> dimensionality reduction/clustering [HMMER] -> stage not stated [BEDTools, BLAST, Python]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Alignments Pairwise alignments To compute the percentage of sequences aligned and to study structural variants and segmental duplications, the pairwise alignment of the human chromosome X and Y was performed against each of chromosome X and Y of the six ape species using minimap2.24 77 .
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Long and short metagenomic reads were mapped onto contigs using minimap2 (ref.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: The resulting PacBio HiFi contigs were aligned to the T2T-CHM13 reference genome 4 (v.2.0) using minimap2 50 (v.2.24) with the following parameters: -I 15G -a --eqx -x asm20 -s 5000.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Version used: **2.20**
- Evidence: Where possible, the alternate assembly (3.73 Gb, 2.1 Mb contig N50; comprised of nearly identical haplotypes in the primary assembly; discussed in Supplementary Data ), was physically anchored to the most similar chromosome in the primary assembly based on best unique alignments using minimap2 (v.2.20-r1061) 57 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Version used: **2.17**
- Evidence: Hybrid assemblies were generated first from raw ONT reads by CANU (v.2.0) 48 followed by realigning ONT reads to the draft assembly by Minimap2 (v.2.17-r941) 49 .
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: Long-read alignment was carried out by Minimap2 as previously described 49 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Identification of constrained sequence elements across 239 primate genomes. (Nature 2024)

- DOI: 10.1038/s41586-023-06798-8 | PMCID: PMC10808062 | PMID: 38030727
- Evidence: After introducing a minimum contig length cutoff of 1 kb, we generated pairwise alignments between the two assemblies using minimap2 58 (v.
- Full pipeline: alignment/mapping [SAIGE, minimap2] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [RepeatMasker v4.1.2, VEP]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Evidence: Reads were aligned to the GRCh38 genome reference with minimap2 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **2.24**
- Evidence: Long and short reads were mapped independently on the reference genome using minimap2 v.2.24 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Version used: **2.24**
- Evidence: Reads mapping and variant calling The reads of 682 barley genotypes, of which 380 were wild and 302 domesticated, were mapped to the MorexV3 genome sequence assembly 15 using Minimap2 (v2.24) 48 .
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Evidence: The basecalled reads were mapped to a genome of possible reporter transcripts using minimap2 (ref.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Evidence: The FASTQ files were then mapped to BAM files using the command minimap2 -ax map-ont -y../GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.mmi.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Evidence: Nanopore informatic analysis Reads were aligned to N. meningitidis 8013 reference genome and MDAΦ–Kan genome separately using minimap2 (ref.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: For the GRCh38 and CHM13, we used minimap2 (ref.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **2.26**
- Evidence: The T2T status of the assembled chromosomes and the closing status of previously reported gaps 2 were determined relative to the T2T-CHM13 reference genome 4 by factoring in the above quality control information in the evaluation of the contig-to-reference alignment produced with minimap2 (v.2.26) 78 , 79 and mashmap (v.3.1.3) 80 ( Supplementary Methods ).
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Evidence: Reads were then aligned to the GRCg7b chicken genome assembly using minimap2 (ref.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### Feline infectious peritonitis epizootic caused by a recombinant coronavirus. (Nature 2025)

- DOI: 10.1038/s41586-025-09340-0 | PMCID: PMC12408369 | PMID: 40633571
- Evidence: Spike amplicons were identified from the output through alignment with minimap2 56 (v.2.22) to the spike from the first sample we sequenced (1-G7_Gi_6739) for which a consensus was made using the same process, with the correct amplicon identified by BLAST 57 .
- Full pipeline: alignment/mapping [Clustal Omega, minimap2] -> stage not stated [IQ-TREE]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **2.24**
- Evidence: Morex (GenBank accession code EF115541 ) using minimap2 (version 2.24-r1122) 58 with the parameters -ax map-hifi --secondary=no --sam-hit-only.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: For this purpose, chromosomes of subgenomes S1_h1, S1_h2, S3, R3 and R4 were aligned against each other within each linkage group (Rca1–Rca7) by minimap2 76 , 77 using the following command: minimap2 -ax asm5 --eqx -t 16 genome1.fa genome2.fa | samtools sort -@8 > aln.sorted.bam.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **2.24**
- Evidence: We aligned full-length cDNA to the haplotype-resolved Ace High (AH3Ma/b) genomes with minimap2 (v2.24) 75 and gene expression was measured using Salmon v1.6.0 68 .
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: We then integrated the three assemblies by manually comparing them to each other, with a help of reciprocal large-scale alignments generated with minimap2 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Assembly to reference alignment All de novo assemblies were aligned to both GRCh38 as well as to the complete version of the human reference genome T2T-CHM13 (v2) using minimap2 (ref.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Version used: **2.20**
- Evidence: Introgression identification Whole-genome sequencing reads of 20 wild potato species were aligned to the DM reference genome 70 and cultivar haplotypes using minimap2 (v.2.20-r1061) 73 .
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: (2) We mapped HiFi reads to the IRGSP-1.0 reference genome using minimap2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Version used: **2.17**
- Evidence: Determining poly(A) lengths from DRS Basecalled nanopore reads were mapped to the respective transcriptome references (Gencode 26 or Gencode 38 for mouse and human samples, respectively) using Minimap2 2.17 with options -k 14 -ax map-ont –secondary=no, and processed with Samtools 1.9 to filter out supplementary alignments and read mapping to reverse strand (Samtools view -b -F 2320).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Complete sequencing of ape genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08816-3 | PMCID: PMC12058530 | PMID: 40205052
- Evidence: Regions of collinearity and synteny (positive in blue) are contrasted with inverted regions (negative in yellow) and with regions beyond the sensitivity of minimap2 (homology gaps), including centromeres, subterminal and interstitial heterochromatin or other regions of satellite expansion.
- Full pipeline: stage not stated [minimap2]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: Multifasta files with all the single-cell de novo assembled VSGs per experiment, together with the putative ‘donor’ VSGs, were constructed and aligned to VSG-8 with minimap2 (ref.
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Version used: **2.17**
- Evidence: Orthologues with coverage above 50% and 75% identity were lifted from the tomato reference genome Heinz (v.4.0) 70 and the eggplant reference genome Eggplant (v.4.1) 71 using Liftoff (v.1.6.3) 72 using the parameters --copies,--exclude_partial and using both the Gmap (v.2020-10-14) 73 and Minimap2 (v.2.17-r941) 74 aligners.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **2.17**
- Evidence: Genome sequences were aligned to the DMv6.1 reference genome to produce alignment BAM files using Minimap2 (v.2.17) 96 with “-ax asm5”.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **2.15**
- Evidence: Minimap2 (v.2.15-r905) was used for the mapping with the parameter ‘-c -x map-pb’.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### H5N1 clade 2.3.4.4b dynamics in experimentally infected calves and cows. (Nature 2025)

- DOI: 10.1038/s41586-024-08063-y | PMCID: PMC11754106 | PMID: 39321846
- Evidence: Consensus sequences were obtained with an iterative map-to-reference approach with Minimap2 (vs 2.24).
- Full pipeline: stage not stated [minimap2]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: The FLNC reads were then aligned to these clustered reference transcripts using minimap2 73 , optimized for splice junctions.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: Feature generation To generate features, we first perform all-versus-all alignment using minimap2 22 , 50 .
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: ...tural variants in the four sequenced p11568 samples over time, ONT reads from each of p11568 t1–t4 were aligned against the t4 E. faecium contig with minimap2 (ref.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **2.28**
- Evidence: All unitigs generated by Hihiasm were mapped into the haploid genome 54 using minimap2 (2.28) 55 with -cx asm20.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **2.24**
- Evidence: To improve mitochondrial genome assembly, we removed contigs aligned to mitochondrial DNA using minimap2 (v.2.24) 66 (-cxasm5) and reassembled the mitochondrial genome with Unicycler (v.0.5.0) 67 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **2.22**
- Evidence: SyRI (v1.6.3) 83 was used for pairwise variant detection from whole-genome alignments via minimap2 (v.2.22-r1101) 84 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **2.24**
- Evidence: The generated consensus contigs generated were checked for circularization to remap the HiFi reads by Minimap2 v.2.24-r1122.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **2.17**
- Evidence: The entire dataset was then remapped against the initially generated sequence through Minimap2 v.2.17 (ref.
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### Efficient near-telomere-to-telomere assembly of nanopore simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10105-6 | PMCID: PMC13070018 | PMID: 41639459
- Evidence: Each plot, generated using SVbyEye 40 , shows minimap2 38 alignment results of the assemblies to the annotated SMN1 and SMN2 regions within the HG002 Q100 reference.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [hifiasm]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **2.22**
- Evidence: Reads were mapped to the indicated reference genomes (Supplementary Table 2 ) using Minimap2 (v.2.22, --r1109dirty) 52 , with specific alignment parameters optimized for SOS splicing events (minimap2 -ax splice -C 0) and for hybrid spliceosome–SOS splicing events and the F19B2.5.2 5′ UTR locus (minimap2 -ax splice).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: The reads for the selected samples were mapped to the assemblies using Minimap2 (ref.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **2.26**
- Evidence: Read quality and length distribution were assessed using NanoPlot (v.1.41.6) before and after the removal of human reads (read mapping against the human genome (v.38) using minimap2 (v.2.26-r1175)).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Version used: **2.17**
- Evidence: Fastq files were generated using samtools bam2fq (v.1.6) 70 , aligned to a custom reference (hg19_pUC19) comprising the pUC19 sequence appended to the hg19 genome using minimap2 (v.2.17) 71 and sorted and indexed using samtools.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: Omni-C reads were aligned to the HiRise super-scaffolds with Minimap2 51 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: Nanopore reads were mapped using minimap2 ( 68 ) (version 2.15) with parameters “-p 0.3 -ax map-ont” and a fasta file containing the human genome sequence from ENSEMBL release 93 ( ftp://ftp.ensembl.org/pub/release-93/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz ) concatenated to the SARS-CoV-2 sequence, GenBank ID: MN988713.1 , “Severe acute respiratory syndrome coronavir...
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### Use of NAD tagSeq II to identify growth phase-dependent alterations in <i>E. coli</i> RNA NAD<sup>+</sup> capping. (PNAS 2021)

- DOI: 10.1073/pnas.2026183118 | PMCID: PMC8040648 | PMID: 33782135
- Evidence: Two sets of reads generated from the TagSeek step were subjected to TagSeqQuant for aligning to both the reference genome and transcriptome of E. coli strain K-12 substrain MG1655 ( 37 ), with the default alignment parameters of minimap2 ( 38 ).
- Full pipeline: alignment/mapping [minimap2] -> quantification [ImageJ] -> differential/statistical testing [R v3.5] -> stage not stated [DESeq2]

### Long-read assembly of a Great Dane genome highlights the contribution of GC-rich sequence and mobile elements to canine genomes. (PNAS 2021)

- DOI: 10.1073/pnas.2016274118 | PMCID: PMC7980453 | PMID: 33836575
- Version used: **2.9**
- Evidence: To identify large insertion and deletion variants, the Zoey assembly and 6,857 secondary contigs were aligned to CanFam3.1 using minimap2 (version 2.9-r720) with the -asm5 option ( 95 ).
- Full pipeline: alignment/mapping [Canu v1.3, Cufflinks v2.2.1, minimap2 v2.9] -> stage not stated [RepeatMasker v4.0.7, kallisto v0.46.0]

### Accurate SNV detection in single cells by transposon-based whole-genome amplification of complementary strands. (PNAS 2021)

- DOI: 10.1073/pnas.2013106118 | PMCID: PMC7923680 | PMID: 33593904
- Version used: **2.12**
- Evidence: We aligned preprocessed single-cell reads with two mappers, BWA-MEM v0.7.17 ( 38 ) and Minimap2 v2.12 ( 39 ), both with their default settings for short reads.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2 v2.12] -> stage not stated [BEDTools]

### A conserved long noncoding RNA, GAPLINC, modulates the immune response during endotoxic shock. (PNAS 2021)

- DOI: 10.1073/pnas.2016648118 | PMCID: PMC7896317 | PMID: 33568531
- Evidence: Transcripts were aligned to the mouse genome (assembly GRCm38/mm10) using Minimap2.
- Full pipeline: alignment/mapping [minimap2] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> stage not stated [SPAdes]

### Identification and functional validation of super-enhancers in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2215328119 | PMCID: PMC9860255 | PMID: 36409894
- Evidence: The genomic sequences from these ecotypes were aligned to the Col-0 genome (TAIR10) using minimap2 ( 79 ) with parameter “-a”.
- Full pipeline: alignment/mapping [BWA, SAMtools, minimap2] -> stage not stated [BCFtools, BEDTools, R v4.0.4]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: Here we noticed a potential chimeric contig in E2B, which was confirmed as a misassembly by mapping back the raw reads with minimap2 ( 81 ) followed by inspection in IGV ( 83 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Marine viral particles reveal an expansive repertoire of phage-parasitizing mobile elements. (PNAS 2022)

- DOI: 10.1073/pnas.2212722119 | PMCID: PMC9618062 | PMID: 36256808
- Evidence: In the first phase, each read over 5 kb was compared with itself using minimap2 ( 48 ) and lastal ( 49 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [HMMER, IQ-TREE, Medaka, R v9.4, eggNOG, minimap2]

### Taxonomic classification of DNA sequences beyond sequence similarity using deep neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2122636119 | PMCID: PMC9436379 | PMID: 36018838
- Evidence: BERTax is compared against the state-of-the-art database taxonomic classification approaches Kraken2 ( 15 ), sourmash ( 16 ), MMseqs2 ( 14 ), and minimap2 ( 17 ).
- Full pipeline: stage not stated [Kraken2, NumPy v1.19.2, Python v3.7, SciPy v1.6.1, minimap2]

### Repeated translocation of a supergene underlying rapid sex chromosome turnover in <i>Takifugu</i> pufferfish. (PNAS 2022)

- DOI: 10.1073/pnas.2121469119 | PMCID: PMC9191631 | PMID: 35658077
- Evidence: For long-read-only assembly, a Pairwise mApping Format file was generated using Minimap2 ( 73 ) and converted into an assembly graph using Miniasm ( 74 ).
- Full pipeline: alignment/mapping [BWA, minimap2] -> stage not stated [BUSCO, RAxML v0.8]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **2.17**
- Evidence: Minimap2 (v2.17-r941) ( 48 ) was used to align the PacBio RNA (–secondary = no -ax splice) and DNA (--secondary=no -ax map-pb) sequence reads against their respective reference genomes.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: ...one sample in the RNASeq data after bowtie2 ( 55 ) alignment and Salmon ( 56 ) quantification or 2) at least one TPM in the gtf file obtained after a minimap2 ( 57 ) alignment and StringTie ( 58 ) quantification of IsoSeq3 polished long reads.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Domoic acid biosynthesis in the red alga <i>Chondria armata</i> suggests a complex evolutionary history for toxin production. (PNAS 2022)

- DOI: 10.1073/pnas.2117407119 | PMCID: PMC8833176 | PMID: 35110408
- Evidence: To further assess overall genome completeness, we mapped ONT reads to the assembled genome using minimap2 ( 27 ), in which 88% of ONT reads were present in the assembled genome, a clearer indicator of genome completeness.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [AlphaFold, BLAST, BUSCO v4.0.5]

### AnchorWave: Sensitive alignment of genomes with high sequence diversity, extensive structural polymorphism, and whole-genome duplication. (PNAS 2022)

- DOI: 10.1073/pnas.2113075119 | PMCID: PMC8740769 | PMID: 34934012
- Evidence: The start and end positions of the reference full-length CDS to the query genome are lifted over using a splice-aware sequence alignment program [minimap2 ( 19 ) was used in this manuscript].
- Full pipeline: alignment/mapping [SAMtools v1.10, minimap2]

### Dual thermal ecotypes coexist within a nearly genetically identical population of the unicellular marine cyanobacterium &lt;i&gt;Synechococcus&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2315701120 | PMCID: PMC10665897 | PMID: 37972069
- Version used: **2.17**
- Evidence: Filtered reads were mapped to their respective short read assemblies using minimap2 v.2.17 ( 71 ).
- Full pipeline: read trimming [minimap2 v2.17] -> alignment/mapping [BEDTools v2.30, Bowtie2 v2.4.3, SAMtools v1.11, minimap2 v2.17] -> normalisation [SPAdes v3.15.2] -> stage not stated [R]

### mitoSplitter: A mitochondrial variants-based method for efficient demultiplexing of pooled single-cell RNA-seq. (PNAS 2023)

- DOI: 10.1073/pnas.2307722120 | PMCID: PMC10523499 | PMID: 37725654
- Version used: **2.24**
- Evidence: To improve the quality of alignment and reduce the false positive rate of variant calling, the obtained bam files were remapped to the reference genome using minimap2 v2.24 ( 36 ) with parameters: -ax splice -t 8 -G50k -k 21 -w 11 --sr -A2 -B8 -O12,32 -E2,1 -r200 -p.5 -N20 -f1000,5000 -n2 -m20 -s40 -g2000 -2K50m --secondary=no.
- Full pipeline: alignment/mapping [Cutadapt v1.18, STAR v2.7.3a, minimap2 v2.24] -> variant calling [Scanpy v1.9.1, minimap2 v2.24] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> stage not stated [scikit-learn v1.0.2]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Evidence: To validate the scaffold arrangement, Daoli_0.3 was aligned to that of D. cochinchinensis (Dacoc_1.4) using minimap2 and D-GENIES ( 64 ) to produce a dot plot for visualizing similarity, repetitions, breaks, and inversions, with a minimum identity of 0.25.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Version used: **2.2.4**
- Evidence: Support for variant sites was assessed further through minimap2 (2.2.4) alignment to the above Wuhan Hu-1 reference genome.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Origin of the OAS-RNase L innate immune pathway before the rise of jawed vertebrates via molecular tinkering. (PNAS 2023)

- DOI: 10.1073/pnas.2304687120 | PMCID: PMC10400998 | PMID: 37487089
- Evidence: Filtered full-length reads were then mapped onto S. cerevisiae reference genome (GCF_000146045.2_R64) using Minimap2 ( 63 ) and then were converted to the BAM format using SAMTools (v1.9) ( 64 ).
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> structure determination [MAFFT] -> stage not stated [AlphaFold, HMMER, IQ-TREE v2.0]

### Natural genetic variation in the pheromone production of <i>C. elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2221150120 | PMCID: PMC10293855 | PMID: 37339205
- Evidence: We confirmed this deletion by aligning unassembled PacBio long reads for JU1400 (PRJNA692613) to the N2 reference genome using minimap2 ( 41 ) (version 2.17; using the parameters -a -x map-pb ) and inspecting read coverage using IGV ( 42 ) (version 2.8.13).
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools, PLINK v1.9] -> stage not stated [GCTA, R, SnpEff]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Evidence: TIRs were annotated with a modified version of Minimap2 ( 57 ), which can be restricted to only report self-mappings, with parameters optimized for short high-identity hits (-S –rev-only -c -m 30 -n 3 -c -B5 -O6 -E3 -k 10 -s 60).
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Version used: **2.17**
- Evidence: Reads were aligned to the SC5314 reference genome (haplotype A chromosomes) using Minimap2 version 2.17 ( 60 ).
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **2.15**
- Evidence: We then used minimap2 (2.15-r905) ( 69 ) to align the PacBio reads of hybrids to the assembly, with the option “--secondary=no,” and partitioned the species-specific haploid reads.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **2.24**
- Evidence: Nanopore reads were aligned against the reference by minimap2 (v2.24) using the “map-ont” setting.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Correlated substitutions reveal SARS-like coronaviruses recombine frequently with a diverse set of structured gene pools. (PNAS 2023)

- DOI: 10.1073/pnas.2206945119 | PMCID: PMC9945976 | PMID: 36693089
- Evidence: For all RNA viruses studied, we used reference-guided alignment to build consensus genomes by taking whole genome assemblies and aligning them to a reference genome from NCBI (Genbank accessions for reference genomes listed in SI Appendix , Table S5 ) using the program ViralMSA ( 84 ) with Minimap2 as the aligner ( 85 ).
- Full pipeline: alignment/mapping [Nextstrain, minimap2] -> stage not stated [TreeTime]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Version used: **2.17**
- Evidence: PacBio subreads (CLR reads) from a Blepharisma stoltei ATCC 30299 MIC-enriched sample (ENA accession ERR6548140 ( 78 )) were aligned to the somatic genome reference assembly (accession PRJEB40285) ( 37 ) with minimap2 v2.17-r941 ( 79 ), with options: -ax map-pb --secondary=no --MD.
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### The lncRNA LUCAT1 is elevated in inflammatory disease and restrains inflammation by regulating the splicing and stability of NR4A2. (PNAS 2023)

- DOI: 10.1073/pnas.2213715120 | PMCID: PMC9910463 | PMID: 36577072
- Version used: **2.17**
- Evidence: Full-length reads were identified using pychopper v2.5.0 and filtered reads were aligned to the human genome (assembly GRCh38/hg38) using minimap2 v2.17 with the parameters “-ax splice -uf -k14.” Annotations were generated using Stringtie v2.1.5 with the parameters “-g 200 -L –conservative” based on the aligned reads and supported by Gencode annotation v38.
- Full pipeline: read trimming [Cutadapt, minimap2 v2.17] -> alignment/mapping [RSEM v1.3.1, STAR v2.6.1, minimap2 v2.17] -> stage not stated [Bioconductor v3.14]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Evidence: Oxford Nanopore MinION and PacBio long reads from embryonic gDNA ( 32 ) available in the NCBI BioProject PRJNA291918 were mapped with Minimap2 ( 49 ).
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **2.28**
- Evidence: Mapping was performed on mm10 or on the in silico mutant genome using minimap2 version 2.28 ( 68 ) (-ax splice).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Structural duality enables a single protein to act as a toxin-antidote pair for meiotic drive. (PNAS 2024)

- DOI: 10.1073/pnas.2408618121 | PMCID: PMC11551426 | PMID: 39485800
- Evidence: Long-read sequencing data of meiotic mRNAs in S. pombe ( 40 ) were mapped to the reference genome using minimap2 ( 67 ).
- Full pipeline: alignment/mapping [minimap2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Evidence: ( 27 ), which was identified by minimap2 alignment.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **2.24**
- Evidence: Nucleosomal DNA libraries for MAC and MIC ( 81 ) were mapped onto the MIC Falcon assembly ( 82 , 83 )with minimap2 v2.24 (parameter: -ax sr).
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### A combinatorially complete epistatic fitness landscape in an enzyme active site. (PNAS 2024)

- DOI: 10.1073/pnas.2400439121 | PMCID: PMC11317637 | PMID: 39074291
- Evidence: Pairs of files were then aligned using minimap2 ( https://github.com/lh3/minimap2 ) using the following process: “minimap2 –ax sr ref.fasta forward.fastq reverse.fastq -k 5 -w 3,” where ref.fasta is a fasta file containing the Tm 9D8* (parent) reference sequence, forward.fastq is the filtered and trimmed forward fastq file, and reverse.fastq is the matching filtered and trimmed reverse fastq file.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [minimap2] -> stage not stated [NetworkX, Python, scikit-learn]

### Resolving the 22q11.2 deletion using CTLR-Seq reveals chromosomal rearrangement mechanisms and individual variance in breakpoints. (PNAS 2024)

- DOI: 10.1073/pnas.2322834121 | PMCID: PMC11295037 | PMID: 39042694
- Version used: **2.18**
- Evidence: PASS-filtered nanopore reads from the default fast base calling were aligned using minimap2 version 2.18 (parameters: –ax map–ont) ( 60 ).
- Full pipeline: alignment/mapping [BWA, minimap2 v2.18] -> variant calling [Flye] -> stage not stated [Medaka v1.9.1]

### Eliminating malaria vectors with precision-guided sterile males. (PNAS 2024)

- DOI: 10.1073/pnas.2312456121 | PMCID: PMC11228498 | PMID: 38917000
- Evidence: To identify transgene insertion sites, nanopore reads were aligned to the gZBD plasmid sequence (Plasmid #1114H, Addgene #200640 ( 99 )) using minimap2 ( 109 ).
- Full pipeline: alignment/mapping [minimap2]

### Endogenous virophages are active and mitigate giant virus infection in the marine protist <i>Cafeteria burkhardae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2314606121 | PMCID: PMC10945749 | PMID: 38446847
- Version used: **2.22**
- Evidence: The reads were mapped with minimap2 v2.22 ( 46 ) to previously published assemblies of the respective host with annotated integrated virophages ( 33 ).
- Full pipeline: alignment/mapping [minimap2 v2.22] -> stage not stated [BLAST, Flye v2.9.1, SAMtools]

### Environmental radiation exposure at Chornobyl has not systematically affected the genomes or chemical mutagen tolerance phenotypes of local worms. (PNAS 2024)

- DOI: 10.1073/pnas.2314793121 | PMCID: PMC10945782 | PMID: 38442158
- Evidence: Illumina reads were aligned to post-Racon assembly using minimap2/2.17 (minimap2 -ax sr) ( 48 ), and alignments were used to polish assemblies with pilon-1.24 (pilon –geno) ( 49 ).
- Full pipeline: alignment/mapping [GATK v4.3.0.0, R, SAMtools v1.11, VCFtools v0.1.16, minimap2] -> variant calling [GATK v4.3.0.0] -> stage not stated [BCFtools v1.14, Flye v2.8.1, ImageJ]

### Targeted hypermutation of putative antigen sensors in multicellular bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316469121 | PMCID: PMC10907252 | PMID: 38354254
- Version used: **2.24**
- Evidence: To detect the footprints of DGR activity, the PacBio HiFi and Illumina reads were mapped to the PB-PSB1 genome using minimap2 v2.24-r1122 (option -ax map-hifi) ( 87 ) and bwa mem v0.7.17-r1188 (default options) ( 88 ), respectively.
- Full pipeline: read trimming [MAFFT v7.407] -> alignment/mapping [MAFFT v7.407, SAMtools, minimap2 v2.24] -> visualisation [HMMER] -> stage not stated [InterProScan]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Version used: **2.10**
- Evidence: ...hac.cfg, --qscore_filtering, --device ‘cuda:all:100%’ --barcode_kits ‘SQK-PCB109’.” The basecalled reads were mapped to TAIR10 reference genome using Minimap2 (v2.10-r761) ( 109 ) with the parameters “-ax splice, –secondary = no, -G 12000.” Then, the 3′ linker was identified by a customized Python script “adapterFinder.py” with parameter “--mode 1” as previously described ( 26 ).
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Evidence: ...2 ) with parameters “--nano-raw --iterations 2.” Assembled contigs were further polished by NextPolish (v1.3.1) ( https://github.com/Nextomics ) with minimap2_options parameter “-x map-ont” for three rounds using Illumina reads.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Homology-mediated transformation of frog-killing fungus &lt;i&gt;Batrachochytrium dendrobatidis&lt;/i&gt; illuminates chytrid development and pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507572122 | PMCID: PMC12595416 | PMID: 41150711
- Version used: **2.28**
- Evidence: CCS reads were mapped to the assembled genomes using minimap2 v2.28 ( 39 ) with the parameters -ax map-hifi.
- Full pipeline: alignment/mapping [SAMtools v1.14, minimap2 v2.28] -> stage not stated [BLAST, BUSCO v5.2.2, QUAST v5.0.0, R v4.0.2]

### &lt;i&gt;WUSCHEL-D1&lt;/i&gt; upregulation enhances grain number by inducing formation of multiovary-producing florets in wheat. (PNAS 2025)

- DOI: 10.1073/pnas.2510889122 | PMCID: PMC12557809 | PMID: 41086219
- Evidence: The MOV contig (ptg000222l) was individually aligned using minimap2 ( 65 ) (with default parameters) to chromosome 2D across eight high quality wheat genome assemblies, including: Triticum aestivum IWGSC RefSeq v1.0, T. aestivum cultivars Kariega, Mace, Lancer, Landmark, and Norin 61, Triticum spelta , and synthetic hexaploid wheat Chuanmai 104 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [minimap2] -> stage not stated [BUSCO, Python, hifiasm]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **2.11**
- Evidence: Finally, we identified syntenic genomic regions for all candidate autosomal and sex-linked scaffolds on closely related species with chromosome-level genome assemblies ( S. humboldti and C. maguari ) using minimap2 v2.11 ( 87 ) with default parameters ( SI Appendix , Methods ).
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Evidence: Reads were mapped by -x map-ont of minimap2-2.18, and the deletion was confirmed by Integrated Genome Viewer (IGV).
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Evidence: Then, xenic nanopore sequencing data were aligned to the axenic assembly using minimap2 (-ax map-ont) v2.24-r1122 to identify diatom reads in the xenic data ( 92 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Version used: **2.24**
- Evidence: In order to verify the locations of the deletions in each sample, the reads were then mapped to the Araport11 A. thaliana Col-0 genome from Phytozome ( https://phytozome-next.jgi.doe.gov/info/Athaliana_Araport11 ) using minimap2 v2.24-r1122 ( 43 ) and samtools v1.17 ( 44 ) to sort the resulting mapping file.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Tracing SARS-CoV-2 clusters across local scales using genomic data. (PNAS 2025)

- DOI: 10.1073/pnas.2501435122 | PMCID: PMC12358902 | PMID: 40773234
- Version used: **2.24**
- Evidence: Sequences were aligned to the reference genome (GenBank ID: NC_045512.2 ) using minimap2 v2.24 ( 42 ).
- Full pipeline: alignment/mapping [minimap2 v2.24] -> stage not stated [IQ-TREE v2.3.2, R, TreeTime v0.11.2]

### Transcription termination promotes splicing efficiency and fidelity in a compact genome. (PNAS 2025)

- DOI: 10.1073/pnas.2507187122 | PMCID: PMC12358841 | PMID: 40763012
- Evidence: The following parameters were used during alignment “minimap2 -ax splice -G 3000” which set a maximum intron length of 3,000 bp.
- Full pipeline: alignment/mapping [featureCounts, minimap2] -> quantification [DESeq2, featureCounts] -> normalisation [DESeq2] -> stage not stated [BEDTools, SAMtools]

### Cryptic intronic transcriptional initiation generates efficient endogenous mRNA templates for C9orf72-associated RAN translation. (PNAS 2025)

- DOI: 10.1073/pnas.2507334122 | PMCID: PMC12358909 | PMID: 40758885
- Evidence: Sequence alignment was performed using minimap2, aligning reads to the human reference assembly GRCh38.
- Full pipeline: alignment/mapping [minimap2]

### Whole-genome duplication increases genetic diversity and load in outcrossing <i>Arabidopsis arenosa</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2501739122 | PMCID: PMC12337351 | PMID: 40737318
- Version used: **2.22**
- Evidence: Minimap2 (v2.22) ( 99 ) was used to map the Nanopore reads against the reference genome of A. arenosa ( 95 ) with default parameters.
- Full pipeline: alignment/mapping [minimap2 v2.22] -> variant calling [GATK v3.7, R] -> differential/statistical testing [vegan v2.6] -> stage not stated [SnpEff v5.1]

### Synthesis of large single-transcript pathways from oligonucleotide pools: Design of STARBURST, an autobioluminescent reporter. (PNAS 2025)

- DOI: 10.1073/pnas.2508109122 | PMCID: PMC12337302 | PMID: 40729380
- Evidence: Briefly, it uses minibar ( 46 ) to demultiplex reads, chopper ( 47 ) to remove low-quality reads, minimap2 ( 48 ) to map reads to reference sequences, and samtools ( 49 ), bcftools ( 49 ), bedtools ( 50 ), racon ( 51 ), medaka ( 52 ), seqtk ( 53 ), emboss ( 54 ), and parallel ( 55 ) to generate consensus sequences, annotate variants, and output summaries.
- Full pipeline: read trimming [BCFtools, BEDTools, SAMtools, minimap2]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Evidence: Synteny analysis of the sex chromosomes and between haplotypes were performed with whole genome alignment using minimap2/2.27 with default settings and -x asm10 (1% sequence divergence) ( 125 ) and visualized after removing short alignments (<100 kb for multispecies alignment, <500 kb for haplotype alignment) using the R-package Farre-lab/syntenyPlotteR ( 126 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Genomic origins and evolution of neo-sex chromosomes in Pacific Island birds. (PNAS 2025)

- DOI: 10.1073/pnas.2503746122 | PMCID: PMC12337287 | PMID: 40720643
- Version used: **2.26**
- Evidence: Read depth was assessed using minimap2 (2.26-r1175) ( 63 , 64 ).
- Full pipeline: read trimming [Trim Galore v0.6.2, hifiasm] -> alignment/mapping [Trim Galore v0.6.2, hifiasm] -> stage not stated [BUSCO v5.2.2, R, RepeatMasker v4.1.2, SAMtools v1.11, minimap2 v2.26]

### Phage-based delivery of CRISPR-associated transposases for targeted bacterial editing. (PNAS 2025)

- DOI: 10.1073/pnas.2504853122 | PMCID: PMC12318184 | PMID: 40711918
- Evidence: To determine coverage, reads at least 2.5 kb in length were mapped back to the assembled bacterial and phage sequences using the Minimap2 mapper in Geneious Prime with the setting of “Map multiple best matches: To none” ( 56 ) ( https://www.geneious.com ).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Flye]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Version used: **2.18**
- Evidence: Next, using minimap2 (version 2.18) 2), sequencing reads were mapped against the human genome (hg38), and the mapped reads were removed.
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Signal peptide-independent secretion of keratin-19 by pancreatic cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2426218122 | PMCID: PMC12260553 | PMID: 40591600
- Version used: **2.26**
- Evidence: The base called reads were aligned to the reference genome (hg38 for Panc1 and m39 for FC1242) using minimap2 (v2.26) with the parameter “-ax splice.” All primary alignments to KRT19 that have a mapping quality of at least 30 were extracted with “samtools view.” The coverage along the gene was visualized as a UCSC Genome Browser track.
- Full pipeline: alignment/mapping [SAMtools, minimap2 v2.26] -> visualisation [SAMtools, minimap2 v2.26] -> stage not stated [ImageJ]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Version used: **2.26**
- Evidence: 1.13.1 wrapper for the Minimap2 v.2.26 aligner ( 64 , 65 ) in order to identify matching GRC sequences and separately processed using Hifiasm-0.19.9-r616 ( 66 , 67 ) to generate a draft female genome assembly.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### High-throughput metabolic engineering of &lt;i&gt;Yarrowia lipolytica&lt;/i&gt; through gene expression tuning. (PNAS 2025)

- DOI: 10.1073/pnas.2426686122 | PMCID: PMC12168020 | PMID: 40460129
- Evidence: These reads were then mapped to the constructed reference plasmid library using the Minimap2 aligner tool (available at https://github.com/lh3/minimap2 ).
- Full pipeline: alignment/mapping [minimap2] -> quantification [SAMtools] -> stage not stated [Python]

### Genomic map of the functionally extinct northern white rhinoceros (&lt;i&gt;Ceratotherium simum cottoni&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2401207122 | PMCID: PMC12107126 | PMID: 40359041
- Evidence: We aligned the nanopore reads to the reference genome using Minimap2 ( 59 ) with parameters -ax map-ont and kept primary alignments using Samtools ( 60 ) with parameter -F 2308.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BUSCO, Pilon]

### Bidirectional disruption of &lt;i&gt;GNAS&lt;/i&gt; transcripts causes broad methylation defects in pseudohypoparathyroidism type 1B. (PNAS 2025)

- DOI: 10.1073/pnas.2423271122 | PMCID: PMC12037034 | PMID: 40249781
- Evidence: Reads were aligned to GRCh38 using minimap2 ( 35 ), variants were called using Clair3 ( 36 ), followed by phasing using LongPhase ( 37 ).
- Full pipeline: alignment/mapping [Cutadapt, Galaxy v24.2, minimap2] -> visualisation [Cutadapt, Galaxy v24.2]

### Polymorphic transposable elements contribute to variation in recombination landscapes. (PNAS 2025)

- DOI: 10.1073/pnas.2427312122 | PMCID: PMC11962413 | PMID: 40100633
- Version used: **2.24**
- Evidence: We excluded TEs shorter than 200 bp, of INE-1, which is mostly fixed in D. melanogaster ( 67 ), in clusters larger than 10 kb, and shared between strains [inferred using minimap2 (v.
- Full pipeline: dimensionality reduction/clustering [minimap2 v2.24] -> stage not stated [BLAST]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Version used: **2.1.8**
- Evidence: To visualize CNVrs that were heterozygous between haplotypes of the diploid reference genome, we aligned both reference haplotypes using minimap2 v2.1.8 (-k19 -w19 -m200) ( 100 ) and generated dotplots of the alignments.
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Version used: **2.24**
- Evidence: We aligned HiFi and ONT reads (as Chardonnay has ONT reads, while the others only have HiFi) to the genome using Minimap2 (v2.24-r1122) ( 61 ), and gaps were manually filled with Integrative Genomics Viewer (IGV) (v2.13.1) tool ( 62 ).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Version used: **2.17**
- Evidence: Minimap2 (v2.17) ( 27 ) software was used to extend telomeres.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Restriction-modification systems are required for &lt;i&gt;Neisseria gonorrhoeae&lt;/i&gt; pilin antigenic variation. (PNAS 2026)

- DOI: 10.1073/pnas.2602688123 | PMCID: PMC13321361 | PMID: 42335229
- Evidence: The script processes nanopore sequencing data to identify adapter positions by mapping the FASTQ reads to a reference genome using minimap2, detecting adapters with edlib, and splitting reads at adapter sites.
- Full pipeline: read trimming [Matplotlib, minimap2] -> alignment/mapping [SAMtools, minimap2] -> visualisation [Matplotlib]

### Anti-CRISPR-mediated continuous directed evolution of CRISPR-Cas9 in human cells. (PNAS 2026)

- DOI: 10.1073/pnas.2536003123 | PMCID: PMC13229284 | PMID: 42189993
- Evidence: Data were aligned to the dCas9 reference sequence using Oxford Nanopore’s general-purpose alignment program “Minimap2” (minimap2/2.24).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [PHENIX]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: Repeated minimap2 mappings were used in conjunction with D-Genies visualization to determine clear contig to chromosome assignments and manually split chimeric contigs or remove fully chimeric/ repeat segment contigs.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Functional dissection of &lt;i&gt;SPOP&lt;/i&gt; at the amino acid level reveals a comprehensive functional landscape of variants during tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523210123 | PMCID: PMC13167761 | PMID: 42090249
- Evidence: Filtered reads were aligned to SPOP cDNA using minimap2 with the -ax map-ont option ( 50 ), and variants were called from the aligned bam files by GATK AnalyzeSaturationMutagenesis.
- Full pipeline: read trimming [Cutadapt, minimap2] -> alignment/mapping [STAR, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> visualisation [PyMOL] -> stage not stated [DESeq2, GATK, R]

### Suppression rather than activation of the integrated stress response (GCN2-ATF4) pathway extends lifespan in the fly. (PNAS 2026)

- DOI: 10.1073/pnas.2518812123 | PMCID: PMC13142962 | PMID: 42048457
- Version used: **2.24**
- Evidence: For bioinformatic analysis, we used minimap2 (v2.24; 113 ) and Salmon (v1.10.2; 114 ), and we used the BDGP 6.32 genome and associated transcript annotation file as reference files.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [GSEA, edgeR] -> stage not stated [R, minimap2 v2.24]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Version used: **2.17**
- Evidence: Trimmed reads were then aligned to the primary reference assembly and the concatenated haplotype assembly using Minimap2 v2.17-r941.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: The F13-8 de novo assembly was generated using miniasm-0.3 ( 68 ) and minimap2-2.17.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Creation of de novo cryptic splicing for ALS and FTD precision medicine. (Science 2024)

- DOI: 10.1126/science.adk2539 | PMCID: PMC7616720 | PMID: 39361759
- Version used: **2.1**
- Evidence: Alignment was performed using Minimap2 (v2.1) ( 37 ).
- Full pipeline: alignment/mapping [STAR v2.7.0f, minimap2 v2.1] -> quantification [ImageJ, STAR v2.7.0f] -> stage not stated [BEDTools, CellProfiler, R, Snakemake v5.5.4]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Version used: **2.26**
- Evidence: The resulting reads were then mapped to the GRCh38 (human) or GRCm39 (mouse) reference genome without alternate contigs using minimap2 v.2.26 with default settings for alignment of nanopore reads (-x map-ont).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Version used: **2.12**
- Evidence: Then, two aligners, BWA-MEM (v.0.7.17) ( 47 ) and Minimap2 (v.2.12) ( 48 ), were used to map reads to the human reference genome (GRCh37 with decoy) and generate BAM files.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Cryo-EM structure of human telomerase dimer reveals H/ACA RNP-mediated dimerization. (Science 2025)

- DOI: 10.1126/science.adr5817 | PMCID: PMC7618144 | PMID: 40638752
- Evidence: The resulting reads were mapped using minimap2 ( 60 ) with the following parameters: minimap2 -t 8 -ax splice --secondary=no -G 12000.
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Topaz] -> stage not stated [CTFFIND, ChimeraX, ImageJ, PHENIX v1.20, RELION v5.0, UCSF Chimera]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Version used: **2.26**
- Evidence: MSI2-ADAR editing site calling Sequencing reads from three MSI2-ADAR and three control (empty vector) samples were aligned to the human T2T reference genome chm13v2.0 ( 80 ) using minimap2 (v.2.26) ( 81 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

