# Prokka

- **Category:** microbiome
- **Papers in survey:** 48
- **Journals:** PNAS (24), Nature (22), Cell (2)
- **Years:** 2021 (5), 2022 (10), 2023 (9), 2024 (14), 2025 (5), 2026 (5)
- **Versions named:** 1.14.5 (6), 1.14.6 (5), 1.13 (5), 1.12 (3), 1.14.0 (2), 1.14 (2), 1.13.3 (2), 1.11 (1), 1.5 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), quality control (3), read trimming (2)

## Papers

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **1.5**
- Evidence: ... Hyatt et al., 2010 https://github.com/hyattpd/Prodigal eggnog-mapper v2.0 Huerta-Cepas et al., 2017 , 2019 https://github.com/eggnogdb/eggnog-mapper Prokka v1.5-135 Seemann, 2014 https://github.com/tseemann/prokka BWA-MEM v0.7.16a-r1181 Li and Durbin, 2009 https://github.com/lh3/bwa Kraken2 Wood et al., 2019 https://github.com/DerrickWood/kraken2 MAFFT v7.453 Katoh et al., 2002 https://mafft.cbrc...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Evidence: 123 https://github.com/rr wick/Unicycler Prokka Seemann 124 https://github.com/ts eemann/prokka ScanLag Levin-Reisman et al.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: The polished MAG had an estimated completeness of 100% with 0.81% contamination (CheckM (v.1.0.18) 70 ) and was annotated using Prokka 71 .
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: Genome annotation and comparative analyses Genome annotation was performed using a modified version of Prokka 62 v.1.13.3 to allow annotation of genes that overlap with tRNA genes.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Decoupling of respiration rates and abundance in marine prokaryoplankton. (Nature 2022)

- DOI: 10.1038/s41586-022-05505-3 | PMCID: PMC9771814 | PMID: 36477536
- Evidence: Functional annotation was first performed using Prokka 71 with the default Swiss-Prot databases supplied by the software.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [Bowtie2] -> normalisation [SPAdes v3.0.0] -> stage not stated [Prokka]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Evidence: The Rapid Annotations based on Subsystem Technology (RAST) server and Prokka software tool were used for gene prediction and annotation of the generated contig.
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### Synergy and oxygen adaptation for development of next-generation probiotics. (Nature 2023)

- DOI: 10.1038/s41586-023-06378-w | PMCID: PMC10412450 | PMID: 37532933
- Version used: **1.14.5**
- Evidence: The hybrid assemblies were annotated using Prokka v1.14.5 ( https://github.com/tseemann/prokka ).
- Full pipeline: alignment/mapping [Kraken2] -> quantification [Bracken] -> differential/statistical testing [R, vegan] -> stage not stated [Bowtie2 v2.3.5.1, Prokka v1.14.5, SPAdes v3.13.0]

### Small protein modules dictate prophage fates during polylysogeny. (Nature 2023)

- DOI: 10.1038/s41586-023-06376-y | PMCID: PMC10432266 | PMID: 37495698
- Version used: **1.11**
- Evidence: Genes were annotated using Prokka (v.1.11) 50 , and annotations were supplemented with NCBI BLASTp searches by hand 51 .
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, Prokka v1.11, Python]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Version used: **1.12**
- Evidence: Gene prediction Gene prediction was performed using Prokka (v.1.12) 86 (prokka --kingdom Archaea --norrna --notrna). rRNA genes and tRNA genes were predicted using Barrnap ( https://github.com/tseemann/barrnap ) and tRNAscan-SE 87 , 88 , respectively.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **1.12**
- Evidence: Prokka version 1.12 and 1.13 (ref.
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Version used: **1.14.6**
- Evidence: The identification and retrieval of the 23 ribosomal markers in our Asgard genome database was based on the proteome annotation performed using Prokka (v.1.14.6) 81 .
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Evidence: For detection of cagA , vacA and ureAB homologues in diverse Helicobacter spp., non- pylori Helicobacter genomes were recovered from either GenBank or Enterobase (Supplementary Table 4 ) and annotated using Prokka.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Diverse anti-defence systems are encoded in the leading region of plasmids. (Nature 2024)

- DOI: 10.1038/s41586-024-07994-w | PMCID: PMC11541004 | PMID: 39385022
- Evidence: Gene calling and initial annotation were performed using prodigal 63 v.3.0.0 and Prokka 64 v.1.14.6.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [ChimeraX] -> stage not stated [BLAST, HMMER, Prokka]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Version used: **1.14.0**
- Evidence: The genes were predicted using Prokka version 1.14.0 with “--kingdom Bacteria --rnammer” options, and rnammer version 1.2.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Version used: **1.14.6**
- Evidence: Functional annotation of GOMC genomes ORFs of genomes in GOMC were predicted using Prokka (v1.14.6) 119 , and functional annotation of the predicted ORFs was conducted.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Version used: **1.13**
- Evidence: All assemblies were therefore annotated using Prokka v1.13 47 with the genus Escherichia as Organism details.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Evidence: Genome sequences were annotated using Prokka software (v1.14.5) to identify genetic features and functional elements 60 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: T. diatomicola genome was at first annotated using Prokka 48 v.1.14.6.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Evidence: We annotated the genomes using Prokka 29 and checked for the presence or absence of the bsh gene.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Version used: **1.14.0**
- Evidence: Trimmed reads of parent strains were used to generate draft genomes by performing de novo assembly using SPAdes (v.3.12) 42 with MismatchCorrector activated (--careful parameter) and annotation with Prokka (v.1.14.0) 43 using the NCBI A. baumannii assembly (ASM975968v1; GCA_009759685.1 ) as the reference.
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Gene prediction and annotation were performed with Prokka 52 v.1.11.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Genome-wide sweeps create ecological units in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-026-10476-w | PMCID: PMC13322978 | PMID: 42092154
- Version used: **1.14.6**
- Evidence: Selected protein-coding genes were annotated using EggNOG (emapper v.2.1.12, database v.5.0.2) 78 and Prokka (v.1.14.6) 79 .
- Full pipeline: alignment/mapping [MetaPhlAn v4.0.6] -> differential/statistical testing [ComplexHeatmap v2.12.1, ggplot2 v3.5.1, ggpubr v0.6.0] -> stage not stated [Prokka v1.14.6, R, SciPy]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **1.14.5**
- Evidence: Assemblies with more than 50% coverage of reference GCA_000893175.1 were annotated using Prokka v.1.14.5, and a core gene alignment was generated using panaroo v.1.3.4.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Chemical capture of diazo metabolites reveals biosynthetic hydrazone oxidation. (Nature 2026)

- DOI: 10.1038/s41586-025-10079-x | PMCID: PMC13061610 | PMID: 41639443
- Evidence: The GenBank documents were annotated with Prokka 64 .
- Full pipeline: visualisation [Cytoscape] -> stage not stated [AlphaFold, BLAST, InterProScan, Prokka]

### Elucidation of an anaerobic pathway for metabolism of l-carnitine-derived γ-butyrobetaine to trimethylamine in human gut bacteria. (PNAS 2021)

- DOI: 10.1073/pnas.2101498118 | PMCID: PMC8364193 | PMID: 34362844
- Evidence: Contigs containing hits were annotated using the Galaxy webtool Prokka ( 62 , 63 ).
- Full pipeline: alignment/mapping [MAFFT v7.455] -> dimensionality reduction/clustering [MAFFT v7.455] -> differential/statistical testing [R v3.6, ggplot2] -> visualisation [IQ-TREE v1.6.12] -> stage not stated [Prokka]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Version used: **1.12**
- Evidence: The resulting contigs were annotated with Prokka (v1.12) ( 56 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Multiclonal human origin and global expansion of an endemic bacterial pathogen of livestock. (PNAS 2022)

- DOI: 10.1073/pnas.2211217119 | PMCID: PMC9897428 | PMID: 36469788
- Version used: **1.13**
- Evidence: Genes were annotated using Prokka v1.13 ( 37 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36] -> alignment/mapping [phytools] -> differential/statistical testing [BEAST, R] -> simulation/modelling [phytools] -> structure determination [phytools] -> stage not stated [InterProScan v5.52, Prokka v1.13]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: The reads were trimmed and quality controlled using Trimmomatic ( 75 ) and then assembled using SPAdes ( 76 ) and annotated via Prokka ( 77 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Deep-branching acetogens in serpentinized subsurface fluids of Oman. (PNAS 2022)

- DOI: 10.1073/pnas.2206845119 | PMCID: PMC9586279 | PMID: 36215489
- Version used: **1.14.5**
- Evidence: Gene prediction and annotation of MAGs was performed with Prodigal v.2.6.3 ( 55 ), as implemented in Prokka v.1.14.5 ( 56 ), using default parameters.
- Full pipeline: read trimming [Clustal Omega v1.2.4] -> alignment/mapping [BLAST, Bowtie2, Clustal Omega v1.2.4, IQ-TREE v1.6.11] -> quantification [Bowtie2] -> differential/statistical testing [IQ-TREE v1.6.11] -> stage not stated [Prokka v1.14.5]

### Recurrent emergence of <i>Klebsiella pneumoniae</i> carbapenem resistance mediated by an inhibitory <i>ompK36</i> mRNA secondary structure. (PNAS 2022)

- DOI: 10.1073/pnas.2203593119 | PMCID: PMC9499542 | PMID: 36095213
- Version used: **1.14.5**
- Evidence: Assemblies were generated for all isolates with available raw sequence data using SPAdes v3.9.0 ( 35 ) and annotated with Prokka v1.14.5 ( 36 ).
- Full pipeline: alignment/mapping [BCFtools v0.1.19, BLAST v2.6.0, MUSCLE v3.8, SAMtools] -> stage not stated [Prokka v1.14.5, SPAdes v3.9.0]

### Sulfur and methane oxidation by a single microorganism. (PNAS 2022)

- DOI: 10.1073/pnas.2114799119 | PMCID: PMC9371685 | PMID: 35914169
- Evidence: Annotation of the assembled genome was performed with the Prokka annotation pipeline (version [v]1.14.6) ( 106 ), MicroScope ( 107 ), and PATRIC ( 108 ) annotation platforms.
- Full pipeline: stage not stated [OrthoFinder, Prokka]

### Plant genetic effects on microbial hubs impact host fitness in repeated field trials. (PNAS 2022)

- DOI: 10.1073/pnas.2201285119 | PMCID: PMC9335298 | PMID: 35867817
- Evidence: Reads were assembled using SPAdes (using the settings --isolate -k 21,33,55,77) and annotated with the software Prokka designed for rapid prokaryotic genome annotation ( 67 , 68 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [Python] -> normalisation [Python] -> stage not stated [Prokka, R, SPAdes, igraph, lme4]

### Recombination resolves the cost of horizontal gene transfer in experimental populations of <i>Helicobacter pylori</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2119010119 | PMCID: PMC8944584 | PMID: 35298339
- Evidence: Gene annotation of all HGT, donor, and ancestral genomes was performed with Prokka ( 74 ) for consistent open reading frame (ORF) identification.
- Full pipeline: alignment/mapping [SAMtools, SPAdes] -> dimensionality reduction/clustering [R] -> stage not stated [Prokka]

### Insight into the symbiotic lifestyle of DPANN archaea revealed by cultivation and genome analyses. (PNAS 2022)

- DOI: 10.1073/pnas.2115449119 | PMCID: PMC8784108 | PMID: 35022241
- Version used: **1.13**
- Evidence: Annotation of genome sequences was carried out using Prokka (ver.
- Full pipeline: stage not stated [HMMER, Prokka v1.13, RAxML, eggNOG v4.5.1]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **1.14.6**
- Evidence: First, the draft genomes of the 20 recipients and three donors ( E. coli ST10 C165 and K. pneumoniae ST11 K93 from Bioproject PRJNA626430; for E. coli β3914, the sequence of the ancestral K-12 strain, NC_000913.3 ) were annotated with Prokka v1.14.6 ( 58 ) with default settings.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### The emergence and diversification of a zoonotic pathogen from within the microbiota of intensively farmed pigs. (PNAS 2023)

- DOI: 10.1073/pnas.2307773120 | PMCID: PMC10666105 | PMID: 37963246
- Version used: **1.14.5**
- Evidence: All genomes were annotated using Prokka v1.14.5 ( 60 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v1.2.2, QUAST v5.0.1] -> stage not stated [Canu v1.9, Prokka v1.14.5, R]

### Predicting the effect of mutations to investigate recent events of selection across 60,472 <i>Escherichia coli</i> strains. (PNAS 2023)

- DOI: 10.1073/pnas.2304177120 | PMCID: PMC10401003 | PMID: 37487088
- Version used: **1.13.3**
- Evidence: Prokka 1.13.3 ( 46 ) was used to detect 298,777,430 coding sequences across these genomes and their corresponding amino acid sequences.
- Full pipeline: stage not stated [IQ-TREE v2.0.3, Prokka v1.13.3]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Evidence: ... * , † ATP-dependent DNA helicase * , † Involved in NER, MMR, HR and rolling circle replication ( 22 ) 1.46 × 10 55 189 7 * Mycobrowser annotation. † Prokka annotation. ‡ Multiple variants in MAB_4141 have been collapsed and the lowest P -value is shown.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Version used: **1.13**
- Evidence: Gene prediction based on phage contigs was performed using Prokka (v1.13) ( 87 ).
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Adaptive evolution of carbapenem-resistant hypervirulent &lt;i&gt;Klebsiella pneumoniae&lt;/i&gt; in the urinary tract of a single patient. (PNAS 2024)

- DOI: 10.1073/pnas.2400446121 | PMCID: PMC11363291 | PMID: 39150777
- Evidence: In addition, genomic characteristics were analyzed using various software and databases: SPAdes-v3.13.0 (genome hybrid assembly), Unicycler-v0.4.7 (genome hybrid assembly), Prokka (annotation), ARDB (drug resistance gene profiles), VFDB (virulence gene profiles), PlasmidFinder (plasmid replicon typing), Kleborate 0.4.0 (O antigen, K antigen, and multilocus sequence typing), Parsnp (Phylogenetic an...
- Full pipeline: stage not stated [Prokka, SPAdes]

### Directed evolution of material-producing microorganisms. (PNAS 2024)

- DOI: 10.1073/pnas.2403585121 | PMCID: PMC11295069 | PMID: 39042685
- Version used: **1.13**
- Evidence: Reference genome assembly combined both long and short reads using Unicycler version 0.4.0 ( 61 ), and annotation was performed with Prokka 1.13 ( 62 ).
- Full pipeline: alignment/mapping [Prokka v1.13] -> quantification [SAMtools v1.3.1] -> differential/statistical testing [SAMtools v1.3.1] -> stage not stated [ImageJ]

### Illuminating the coevolution of photosynthesis and Bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322120121 | PMCID: PMC11194577 | PMID: 38875151
- Version used: **1.14**
- Evidence: All genomes included in the genome taxonomy database (GTDB r95) were annotated using Prokka (v1.14; --kingdom [Bacteria or Archaea] --compliant --locustag [genome assembly accession number]) ( 88 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE v2.1.3, MAFFT] -> stage not stated [AlphaFold, BEAST v2.6.6, Prokka v1.14]

### The evolutionary genomics of adaptation to stress in wild rhizobium bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2311127121 | PMCID: PMC10990125 | PMID: 38507447
- Version used: **1.13.3**
- Evidence: For genome assemblies passing quality control, protein coding sequences were predicted and annotated with Prokka (v.
- Full pipeline: quality control [Prokka v1.13.3] -> read trimming [MUSCLE] -> alignment/mapping [MAFFT v7.475, MUSCLE] -> differential/statistical testing [lme4 v1.1] -> visualisation [R] -> stage not stated [RAxML, SPAdes v3.14.1]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Evidence: All archaeal genomes from GTDB Release 214.0 ( 48 ) were annotated with Prokka ( 49 ) v.1.14.6 using the prokaryotic genetic code 11 to identify homologs of the Pyl biosynthetic genes ( pylBCD ), Pyl incorporation gene ( pylS ), methyl-coenzyme M reductase catalytic subunits ( mcrABG ), component A2, and methylamine-specific methyltransferases ( mttB, mtbB, and mtmB ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Jumbo phage-mediated transduction of genomic islands. (PNAS 2025)

- DOI: 10.1073/pnas.2512465122 | PMCID: PMC12595487 | PMID: 41150720
- Evidence: The three foreign elements were screened for open reading frames (ORFs) by Prokka ( 73 ) in KBase ( 74 ).
- Full pipeline: alignment/mapping [BLAST] -> dimensionality reduction/clustering [R v4.1.2] -> stage not stated [InterProScan, Prokka, eggNOG]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **1.14**
- Evidence: The number of potential tRNA genes within the genomes was assessed using Prokka v1.14 ( 55 ).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Linkage of nucleotide and functional diversity varies across gut bacteria. (PNAS 2026)

- DOI: 10.1073/pnas.2521012123 | PMCID: PMC13168539 | PMID: 42090264
- Version used: **1.14.6**
- Evidence: Briefly, for each reference genome assigned to a given species in the UHGG v2 genome collection, genes were predicted by Prokka v1.14.6 ( 66 ).
- Full pipeline: alignment/mapping [Prokka v1.14.6] -> differential/statistical testing [R v4.2]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Version used: **1.14.5**
- Evidence: Assembled contigs were annotated using Prokka v1.14.5 ( https://github.com/tseemann/prokka ) to identify coding sequences and other genomic features.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

