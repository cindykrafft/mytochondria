# Trimmomatic

- **Category:** genomics
- **Papers in survey:** 291
- **Journals:** PNAS (184), Nature (92), Cell (13), Science (2)
- **Years:** 2021 (36), 2022 (44), 2023 (57), 2024 (67), 2025 (67), 2026 (20)
- **Versions named:** 0.39 (74), 0.36 (49), 0.38 (22), 0.32 (10), 0.33 (5), 0.35 (4), 0.40 (2), 2.6.0 (1), 0.32.3 (1), 0.30 (1)
- **Pipeline stages it appears in:** read trimming (291), alignment/mapping (60), quality control (59), quantification (8), variant calling (2), differential/statistical testing (2), visualisation (2), structure determination (2), normalisation (1)

## Papers

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: ...TAR Dobin et al., 2013 N/A FeatureCounts Liao et al., 2014 N/A DESeq2 Love et al., 2014 N/A Morpheus Broad Institute N/A DAVID Huang et al., 2009 N/A Trimmomatic Bolger et al., 2014 N/A Bowtie2 Langmead and Salzberg, 2012 N/A SAM tools Li et al., 2009 N/A MACS2 Zhang et al., 2008 N/A Bedtools Quinlan and Hall, 2010 N/A Resource availability Lead contact Further information and requests for resourc...
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Version used: **0.39**
- Evidence: ...https://www.flowjo.com FastQC Babraham Institute https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ MultiQC 1.9 MultiQC https://multiqc.info/ Trimmomatic 0.39 USADELLAB http://www.usadellab.org/cms/?page=trimmomatic MiXCR MI Lanoratory https://mixcr.readthedocs.io/en/master/index.html NumPy NumPy https://numpy.org/ Python 3.7.4 Python Software Foundation https://www.python.org/ Other BD FA...
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### In vivo structural characterization of the SARS-CoV-2 RNA genome identifies host proteins vulnerable to repurposed drugs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.008 | PMCID: PMC7871767 | PMID: 33636127
- Evidence: ...forge.net/bowtie2/index.shtml STAR Dobin et al., 2013 https://github.com/alexdobin/STAR samtools ( Li et al., 2009 ) http://samtools.sourceforge.net/ Trimmomatic Bolger et al., 2014 http://www.usadellab.org/cms/?page=trimmomatic Infernal 1.1.3 ( Nawrocki and Eddy, 2013b ) http://eddylab.org/infernal/ RNAstructure ( Reuter and Mathews, 2010 ) https://rna.urmc.rochester.edu/RNAstructure.html ViennaR...
- Full pipeline: read trimming [Bowtie2, SAMtools, Trimmomatic] -> alignment/mapping [MAFFT v7.313] -> differential/statistical testing [SciPy] -> simulation/modelling [UCSF Chimera] -> structure determination [UCSF Chimera] -> visualisation [RAxML v8.2.12] -> stage not stated [AutoDock Vina]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Version used: **0.39**
- Evidence: ...rd Tools v2.9.0 Broad Institute http://broadinstitute.github.io/picard/ STAR aligner v2.7.3a Dobin et al., 2013 N/A SAMTools v1.9 Li et al., 2009 N/A Trimmomatic v0.39 Bolger et al., 2014 N/A CRISPR screen analysis This paper https://github.com/PeterDeWeirdt/coronavirus_screen_analysis Resource Availability Lead Contact Further information and requests for resources and reagents should be directed...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: Low quality DNA end fragments and sequencing adapters were trimmed using Trimmomatic ( http://www.usadellab.org ).
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Early cellular mechanisms of type I interferon-driven susceptibility to tuberculosis. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.002 | PMCID: PMC10757650 | PMID: 38029747
- Version used: **0.36**
- Evidence: Sequence reads were trimmed of adapter sequences and low quality nucleotides with Trimmomatic v.0.36 109 and then mapped to the Mus musculus GRCm38 reference genome with STAR aligner v.2.5.2b 110 .
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR, Trimmomatic v0.36] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: 85 https://github.com/macs3-project/MACS Trimmomatic Bolger et al.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **0.39**
- Evidence: In the differentiated samples (EB, endoderm, mesoderm, ectoderm differentiation), the quality of the first nucleotide was less than Q20 in many cases and the reads were processed with Trimmomatic v0.39.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### A replisome-associated histone H3-H4 chaperone required for epigenetic inheritance. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.006 | PMCID: PMC11380579 | PMID: 39094570
- Evidence: Furthermore, protein assembly was guided by principles of parsimony to produce the smallest set of proteins necessary to account for all observed peptides. eSPAN sequencing analysis After quality control, Trimmomatic was used to remove the adaptor and discard sequencing reads with low-quality 121 .
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, ColabFold, UCSF Chimera] -> stage not stated [AlphaFold, Bowtie2, MACS2]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Version used: **0.36**
- Evidence: 126 N/A Trimmomatic v0.36 Bolger et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### Vertebrate centromeres in mitosis are functionally bipartite structures stabilized by cohesin. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.014 | PMCID: PMC11164432 | PMID: 38744280
- Version used: **0.36**
- Evidence: 78 Addgene plasmid #89767 Software and algorithms ImageJ NIH https://imagej.nih.gov/ij/ Prism 9 GraphPad https://www.graphpad.com/scientific-software/prism/ Imaris Software (v9.7.2) Bitplane https://imaris.oxinst.com/ Trimmomatic v0.36 Bolger et al.
- Full pipeline: read trimming [BWA v0.7.16, Cutadapt v1.18, ImageJ, LAMMPS, Trimmomatic v0.36, deepTools] -> stage not stated [Snakemake]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Version used: **0.33**
- Evidence: We downloaded the raw sequence files from the Gene Expression Omnibus (GEO) with the SRA toolkit (fastq-dump), assessed their quality with FastQC (Babraham Bioinformatics), and removed low-quality reads and bases with Trimmomatic v.0.33 116 .
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: Adapters and low-quality reads were trimmed using Trimmomatic 99 and aligned to the human genome (GRCh38) using Bowtie2.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Version used: **0.32**
- Evidence: Raw transcriptomic reads were trimmed using Trimmomatic v.0.32 (MAXINFO:100:0.2, MINLEN:75) 78 after rRNA removal using SortMeRNA v.2.1 (ref.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: Raw Illumina sequence reads were first processed by Trimmomatic 48 (version 0.39) to remove sequencing adaptors and low-quality reads, using parameters: ILLUMINACLIP:adapters/NexteraPE-PE.fa:2:30:10:1:true LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:75 TOPHRED33.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: A. ciliaticola’ was reconstructed from a metagenomic dataset sampled in 2018, as follows: metagenomic reads (MG_18_C) were trimmed using Trimmomatic 58 v.0.32 as previously described 46 and assembled using metaSPAdes 59 v.3.13.0 and k -mer lengths of 21, 33, 55, 77, 99 and 127.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: RNA-seq read mapping, differential expression analysis and heatmap visualization: Resulting RNA-Seq data was analyzed by removing adaptor sequences using Trimmomatic 70 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: The reads were trimmed by Trimmomatic 69 , then aligned to the mouse genome mm10 by Bowtie2 ( bowtie-bio.sourceforge.net/bowtie2 ) 70 .
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Version used: **0.36**
- Evidence: Raw reads, filtered and corrected using Trimmomatic v.0.36 42 and RCorrector v.1.0.2 43 , were assembled using de novo and reference-guided approaches.
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Decoupling of respiration rates and abundance in marine prokaryoplankton. (Nature 2022)

- DOI: 10.1038/s41586-022-05505-3 | PMCID: PMC9771814 | PMID: 36477536
- Version used: **0.32**
- Evidence: The obtained sequence reads were quality-trimmed using Trimmomatic (v.0.32) 60 using the following settings: -phred33 LEADING:0 TRAILING:5 SLIDINGWINDOW:4:15 MINLEN:36.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [Bowtie2] -> normalisation [SPAdes v3.0.0] -> stage not stated [Prokka]

### Nociceptor neurons affect cancer immunosurveillance. (Nature 2022)

- DOI: 10.1038/s41586-022-05374-w | PMCID: PMC9646485 | PMID: 36323780
- Version used: **0.35**
- Evidence: Sequences were trimmed for sequencing adapters and low-quality 3′ bases using Trimmomatic v.0.35 and aligned to the reference mouse genome version GRCm38 (gene annotation from Gencode v.M23, based on Ensembl 98) using STAR v.2.5.1b (ref.
- Full pipeline: read trimming [STAR v2.5.1b, Trimmomatic v0.35] -> alignment/mapping [STAR v2.5.1b, Trimmomatic v0.35, featureCounts] -> quantification [Bioconductor, RSEM] -> normalisation [Bioconductor, RSEM] -> dimensionality reduction/clustering [R] -> stage not stated [DESeq2 v1.18.1, ImageJ]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Version used: **0.39**
- Evidence: Sequencing reads were quality-filtered, and adapter removal was performed using the Trimmomatic (v0.39) 43 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **0.39**
- Evidence: The raw 16S rRNA gene sequencing reads were demultiplexed and primer and barcode sequences were trimmed using Trimmomatic (v.0.39) 57 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Samples were uniformly processed, including adapter trimming with Trimmomatic and alignment to the hg38 genome build using STAR (2.7.2a) 38 with indexes from GENCODE v30.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **0.36**
- Evidence: Bioinformatic processing For each sample, raw sequencing reads were trimmed using Trimmomatic (v.0.36) and then mapped to the human reference genome (hg38) with STAR (v.2.7.3a).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Version used: **0.36**
- Evidence: Raw sequence files were subjected to pre-processing using Trimmomatic v.0.36 to remove Illumina adaptor sequences and low-quality bases.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: We next used Trimmomatic 92 .
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Version used: **0.39**
- Evidence: Sequencing data processing Sequencing reads were demultiplexed using bcl2fastq v2.20, and subsequently trimmed using Trimmomatic v0.39.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Bacteriophages suppress CRISPR-Cas immunity using RNA-based anti-CRISPRs. (Nature 2023)

- DOI: 10.1038/s41586-023-06612-5 | PMCID: PMC10651486 | PMID: 37853129
- Evidence: RNA-seq analysis Generated reads in FASTQ format were initially processed by removing adaptors and low-quality reads using Trimmomatic 55 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2, MAFFT, SAMtools v1.16.1]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Version used: **0.39**
- Evidence: In brief, reads were trimmed using Trimmomatic (v.0.39) 53 to remove remaining primers from the library.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **0.36**
- Evidence: Analysis of gene expression from RNA-seq data Read data were adapter and quality trimmed using Trimmomatic (v.0.36) 52 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Inhibition of fatty acid oxidation enables heart regeneration in adult mice. (Nature 2023)

- DOI: 10.1038/s41586-023-06585-5 | PMCID: PMC10584682 | PMID: 37758950
- Evidence: Trimmomatic version ≥ 0.36 was used to trim reads after a quality drop below a mean of Q15 in a window of five nucleotides 48 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [FastQC v0.11.8, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Version used: **0.36**
- Evidence: Read quality trimming and adaptor removal was carried out using Trimmomatic (version 0.36).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **0.39**
- Evidence: RNA sequencing data analysis The sequencing data was demultiplexed using bcl2fastq v.2.20.0 provided by Illumina and trimmed using Trimmomatic v.0.39 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Version used: **0.36**
- Evidence: Trimmomatic (v.0.36) 61 was used to trim low-quality regions and adapter sequences from raw reads (parameters: ILLUMINACLIP:TruSeq3-PE-2.fa:2:30:10, LEADING:20, SLIDINGWINDOW:4:20, MINLEN:50).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Version used: **0.32**
- Evidence: Reads were trimmed with Trimmomatic (v.0.32) 66 to remove leading and trailing bases with quality scores of less than 20 as well as any bases that did not have an average quality score of 20 within a sliding window of 4 bases.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### Ageing-associated changes in transcriptional elongation influence longevity. (Nature 2023)

- DOI: 10.1038/s41586-023-05922-y | PMCID: PMC10132977 | PMID: 37046086
- Evidence: RNA-seq alignments and gene expression analysis Raw reads were trimmed with trimmomatic 67 version 0.33 using parameters ‘ILLUMINACLIP:./Trimmomatic-0.33/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:45′ for paired-end datasets and ‘ILLUMINACLIP:./Trimmomatic-0.33/adapters/TruSeq3-SE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:45’ for single-end datase...
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.5.1b, Trimmomatic] -> quantification [StringTie] -> differential/statistical testing [DESeq2 v1.8.2, GSEA] -> stage not stated [kallisto v0.42.5]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: Sequenced reads in FASTQ format were trimmed using the Trimmomatic software (ILLUMINACLIP:adapter.fa:2:30:10 SLIDINGWINDOW:5:20 LEADING:3 TRAILING:3 MINLEN:50).
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Version used: **0.36**
- Evidence: Sequencing data were processed using Trimmomatic (v.0.36) 63 to remove Illumina adapters and low-quality reads (SLIDINGWINDOW:5:20).
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: RNA-seq reads were trimmed for adaptor sequences with Trimmomatic 145 (v.0.39) and the MorexV3 genome annotation was used as reference to estimate read abundance with Kallisto 128 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Evidence: The sequence data were trimmed by Trimmomatic 22 (v.0.36) to remove adaptor and then mapped to the hg38 assembly of the human genome using Bowtie2 (refs.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Evidence: Reads were trimmed of adapter content with Trimmomatic 60 (v.0.39), aligned to the hg19 genome using BWA MEM 61 (0.7.17-r1188) and PCR duplicates were removed using Picard’s MarkDuplicates (v.2.25.3).
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Version used: **0.39**
- Evidence: Adapter content was trimmed from the reads using Trimmomatic (v0.39) 62 .
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Version used: **0.39**
- Evidence: Sequence reads were trimmed to remove adaptor sequences and nucleotides with poor quality using Trimmomatic v.0.39 (ref.
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **0.39**
- Evidence: DNA-seq data analysis Raw reads were trimmed with Trimmomatic (v.0.39) 54 and then mapped to mouse genome (mm10) or human genome (hg38), together with Drosophila melanogaster chromatin (spike-in chromatin), using bowtie2 (v.2.4.1) 55 using the default mode, where multiple alignments are searched and the best one is reported.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: The sequenced paired-end reads were quality-controlled using Trimmomatic 61 version 0.39 with “2:30:10 LEADING:3 TRAILING:20 SLIDINGWINDOW:4:15 MINLEN:5” options and FASTX-Toolkit version 0.0.13 ( https://github.com/agordon/fastx_toolkit ) with “-q 20 -p 80” options.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Version used: **0.35**
- Evidence: Paired-end reads were preprocessed to remove adapter sequences and trim low-quality bases using Trimmomatic v.0.35 (ref.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **0.38**
- Evidence: In brief, raw FASTQ files were retrieved using Kingfisher (v0.3.0) ( https://github.com/wwood/kingfisher-download ), quality trimming and adapter removal using Trimmomatic (v0.38) 62 with parameters SLIDINGWINDOW:4:5, LEADING:5, TRAILING:5, and MINLEN:25 and de novo assembly using MEGAHIT (v1.2.9) 63 with default parameters.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **0.40**
- Evidence: Repeat and gene annotation Paired-end RNA-seq reads for TA10171, TA1675 and TA2576 were first cleaned using Trimmomatic (v0.40) 61 with the following settings “ILLUMINACLIP:TruSeq3-PE.fa:2:30:10:2:True LEADING:30 TRAILING:30 MINLEN:36”.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Version used: **0.39**
- Evidence: Sample quality was assessed using FastQC v0.11.9 39 and MultiQC 1.12 40 ; sample reads were trimmed for both quality and length using Trimmomatic 0.39 41 with the following options: removal of TruSeq adapters sequences; sliding window trimming, clipping the read once the average quality within the window (4 bp) falls below 20; finally, drop the read if it is shorter than 38 bp (Supplementary Table...
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Version used: **0.39**
- Evidence: Analysis of Illumina MiSeq data was performed by trimming the reads with Trimmomatic (v0.39) 59 , and aligning, calling variants and generating consensus sequences with Snippy (v4.6.0; https://github.com/tseemann/snippy ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Evidence: Low quality read removal and adapter trimming was carried out using Trimmomatic V0.36 with the options ILLUMINACLIP: <keepBothReads > =TRUE MAXINFO:35:0.5 MINLEN:35.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Version used: **0.36**
- Evidence: Reads were filtered using Trimmomatic v.0.36 (ref.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Selective haematological cancer eradication with preserved haematopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07456-3 | PMCID: PMC11186773 | PMID: 38778101
- Evidence: We applied minimum paired end reads overlap between 10 and 200 and provided the following Trimmomatic sentence: ILLUMINACLIP:NexteraPE-PE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> quantification [R]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: Raw metagenomic short reads were trimmed using Trimmomatic 38 v.0.39 (ILLUMINACLIP:TruSeq3-PE.fa:2:30:10, LEADING:3, TRAILING:3, SLIDINGWINDOW:4:15, MINLEN:36) and assembled using MEGAHIT 39 v.1.2.9.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Phylogenomics and the rise of the angiosperms. (Nature 2024)

- DOI: 10.1038/s41586-024-07324-0 | PMCID: PMC11111409 | PMID: 38658746
- Evidence: Raw reads were trimmed using Trimmomatic 62 to remove low-quality bases and short sequences.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT v7.480] -> stage not stated [IQ-TREE v2.2.0, R]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **0.39**
- Evidence: FASTQ reads were trimmed using Trimmomatic v.0.39 and aligned to the P. breviceps genome using STAR v.2.7.9a 86 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: Subsequently, reads were filtered to remove low-quality reads and reads shorter than 20 bp using Trimmomatic 73 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### A distinct Fusobacterium nucleatum clade dominates the colorectal cancer niche. (Nature 2024)

- DOI: 10.1038/s41586-024-07182-w | PMCID: PMC11006615 | PMID: 38509359
- Evidence: Raw sequence reads were trimmed with Trimmomatic-0.33 (ref.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v2.4.5] -> machine learning [DADA2] -> stage not stated [BLAST, Flye]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **0.33**
- Evidence: Demultiplexed FASTQ files were trimmed with Trimmomatic (v.0.33) 100 using the parameter SLIDINGWINDOW:5:30.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **0.39**
- Evidence: Sequencing adapters were trimmed with Trimmomatic v0.39 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### On the genetic basis of tail-loss evolution in humans and apes. (Nature 2024)

- DOI: 10.1038/s41586-024-07095-8 | PMCID: PMC10901737 | PMID: 38418917
- Version used: **0.39**
- Evidence: Low-quality reads or bases and Illumina adapter sequences were trimmed using Trimmomatic (v.0.39).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BEDTools v2.30.0, STAR v2.7.2a] -> differential/statistical testing [DESeq2 v1.40.2]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Evidence: The remaining reads were analysed with CRISPResso2 in paired-end mode setting the options for Trimmomatic software v.0.39 (ref.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **0.30**
- Evidence: For quality control, to remove technical sequences, including adapters, PCR primers or fragments thereof, and quality of bases lower than 20, pass filter data of fastq format were processed by Trimmomatic (v0.30) to be high-quality clean data.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Evidence: Low-quality sequences were trimmed using Trimmomatic with default parameters 41 .
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Version used: **0.36**
- Evidence: Quality control of sequenced reads was performed by FastQC (version 0.11.3) and adapter filtration was performed by Trimmomatic version 0.36.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Version used: **0.39**
- Evidence: QC of metagenomic sequencing data We removed host-genome-contaminated reads and low-quality reads from the raw metagenomic sequencing data using KneadData (v.0.7.4), Bowtie2 (v.2.3.4.3) 57 and Trimmomatic (v.0.39) 58 .
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Version used: **0.36**
- Evidence: Reads containing adapters and/or bacteriophage PhiX control sequences were removed and trimmed using Trimmomatic (v.0.36) 41 .
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **0.39**
- Evidence: Sequencing FastQ files were applied to FastQC (v.0.11.9; https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) for quality control, adapters were trimmed by Trimmomatic (v.0.39) 73 , and the genomic fragments were aligned to the human, mouse and whale genome reference (hg19, mm10 and the published bowhead whale genome assembly 13 ) using Burrows–Wheeler Aligner (BWA, v.0.7.19) 74 , then sor...
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Version used: **0.39**
- Evidence: Sequencing adapters and low-quality bases in raw reads were trimmed using Trimmomatic 0.39.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: Regions of interest Reads were trimmed using Trimmomatic 67 (v.0.38) (SLIDINGWINDOW:4:25 MINLEN:100) and used to identify induced prophages using two approaches.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Version used: **0.36**
- Evidence: Sequence reads were processed using Trimmomatic (v.0.36) to remove possible adapter sequences and nucleotides with poor quality 43 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: Only paired-end reads that survived Trimmomatic processing v.0.39 (ILLUMINACLIP:NexteraPE-PE.fa:2:30:7, SLIDINGWINDOW:3:18, MINLENGTH:26) were retained.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Raw sequencing reads were processed using FastQC (Babraham Bioinformatics) and Trimmomatic 72 before alignment to the human genome hg38.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: Trimmomatic was used to remove adapter sequences and low-quality bases from the 3′ end of each read, and the resulting high-quality reads were aligned to the GRCm38 mouse genome using STAR v.2.5.11, which also generated gene-level read counts.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Evidence: Reads were trimmed with Trimmomatic (ILLUMINACLIP:TruSeq2-PE.fa:2:30:10:1:FALSE LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36) and aligned to the cDNA annotation of the reference genome sequence of tomato (SL4.0) using STAR (v.2.6.1.d) 65 .
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Version used: **0.39**
- Evidence: Sequencing reads were trimmed with Trimmomatic (v.0.39) 67 to remove adaptor sequences and bases containing low quality scores.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **0.39**
- Evidence: Target back-mapping, variant calling and creating a sample-specific reference The raw SCO reads were trimmed using Trimmomatic (v.0.39) 110 with the following settings: 2:30:8 LEADING:13 TRAILING:13 SLIDINGWINDOW:4:19 MINLEN:36.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: RNA-seq read mapping, differential expression analysis and heat-map visualization Adaptor sequences were removed from the RNA-seq data using Trimmomatic 55 .
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Version used: **0.39**
- Evidence: Subsequently, the plasmid backbone sequence was trimmed using the Trimmomatic 0.39-2 program 39 .
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: Analysis of single-cell data Reads were cleaned with Trimmomatic 53 and mapped to the genomes of T. chinensis 5 with STARsolo (v.2.7.10b) 54 (STAR…–runThreadN 32–alignIntronMax 10000–soloUMIlen 12–soloCellFilter EmptyDrops_CR–soloFeatures GeneFull–soloMultiMappers EM–soloType CB_UMI_Simple).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **0.39**
- Evidence: Illumina Truseq adaptor, polyA and polyT sequences were trimmed using Trimmomatic v.0.39.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Version used: **0.39**
- Evidence: Gene expression analysis Adaptor sequences were trimmed from the raw sequencing reads using Trimmomatic (v.0.39) 65 , with parameters ILLUMINACLIP:Adapters.fa:2:30:7 SLIDINGWINDOW:4:20 MINLEN:40 in single-end mode.
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Version used: **0.39**
- Evidence: Raw reads were filtered and trimmed with Trimmomatic (v.0.39) 126 before mapping to the reference genome with bwa mem (v.0.7.17-r1188) and duplicates were marked with bamsormadup from biobambam2 ( https://github.com/gt1/biobambam2 ).
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: These reads were trimmed using Trimmomatic 49 (v.0.39) to remove the adaptors and low-quality regions.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **0.39**
- Evidence: Quality control and adapter trimming of the raw whole-genome bisulfite sequencing (WGBS) data was then performed using Trimmomatic (v.0.39).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **0.39**
- Evidence: Reads were trimmed using Trimmomatic 0.39 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **0.38**
- Evidence: 47 ), followed by quality control with Trimmomatic v.0.38 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Evidence: The trailing N bases were also trimmed, similar to the Trimmomatic TRAILING method; (2) The auto adapter was detected for PE data; (3) Trimmed reads shorter than 60 bp were discarded.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Version used: **0.32.3**
- Evidence: ChIP reads were first trimmed using Trimmomatic v.0.32.3 (<30 phred, SLIDINGWINDOW:4:30 option) 63 .
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: For taxonomic analysis, paired-end reads were quality-checked with FastQC v.0.12.0 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and filtered with Trimmomatic 44 v.0.36 to remove adapters and low-quality reads.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **0.39**
- Evidence: The fastq file of ChIP–seq data was quality filtered using Trimmomatic (v.0.39) 64 and mapped to Col-CEN_v1.2 reference genome.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Gut microbiome strain-sharing within isolated village social networks. (Nature 2025)

- DOI: 10.1038/s41586-024-08222-1 | PMCID: PMC11666459 | PMID: 39567691
- Evidence: The resulting reads were screened for human contamination (hg19) with BMTagger and then quality filtered with Trimmomatic 48 (v.0.36, parameters ‘ILLUMINACLIP: nextera_truseq_adapters.fasta:2:30:10:8:true SLIDINGWINDOW: 4:15 LEADING: 3 TRAILING: 3 MINLEN: 50’).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> visualisation [igraph v1.3.5] -> stage not stated [MetaPhlAn, R, vegan v2.6]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **0.39**
- Evidence: Raw FASTQ files were processed with Trimmomatic v.0.39 (parameters: ILLUMINACLIP:TruSeq3-PE.fa:2:30:10, LEADING:3, TRAILING:3, SLIDINGWINDOW:4:15).
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **2.6.0**
- Evidence: The tool BBDuk from BBMap (v.39.01) was used for removing remaining sequencing adapters, while Trimmomatic (v.2.6.0) 89 was used for cropping potentially low-quality bases from the 3′-end and removing short reads such that reads had at most 75 bp and at least 45 bp.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **0.38**
- Evidence: In brief, sequencing adaptors and low-quality bases were trimmed using Trimmomatic v.0.38.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **0.39**
- Evidence: Briefly, reads were trimmed for minimal length of 36-base pairs using Trimmomatic (v.0.39).
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: The sequenced paired-end reads were quality-controlled using Trimmomatic 84 v.0.39 with ‘2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:30’ parameters.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **0.39**
- Evidence: Raw sequencing reads were trimmed using Trimmomatic (v.0.39) 58 , removing leading and trailing bases with Phred scores below 25 and reads with less than 50 nucleotides.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **0.39**
- Evidence: Demultiplexed reads were trimmed of adaptor sequences using Trimmomatic (v.0.39).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Version used: **0.39**
- Evidence: To summarize, reads were first processed using Trimmomatic (v.0.39) (settings TruSeq3-PE-2.fa:2:30:10, minlen 50) followed by alignment with bwa (bwa mem, options -5SP -T0, v.0.7.17-r1198-dirty) to the mm10 (GRCm38) genome reference or the hg38 (GRCh38) reference 67 , 68 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Version used: **0.39**
- Evidence: Raw FASTQ files were processed with Trimmomatic (v.0.39) 64 using the following parameters: ILLUMINACLIP:TruSeq3-PE.fa:2:30:10, LEADING:3, TRAILING:3, and SLIDINGWINDOW:4:15.
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Version used: **0.39**
- Evidence: Retain-seq analysis Adapter content in sequenced episome library reads were trimmed using Trimmomatic (v.0.39) 64 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### Potent neutralization of Marburg virus by a vaccine-elicited antibody. (Nature 2026)

- DOI: 10.1038/s41586-025-09868-1 | PMCID: PMC12893919 | PMID: 41225006
- Version used: **0.39**
- Evidence: Sequencing reads were adapter-trimmed and quality-trimmed using Trimmomatic (v.0.39) 84 and mapped to the VSV-MARV/Musoke GP genome using Geneious Prime 85 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39] -> differential/statistical testing [RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Raw sequencing reads were trimmed and quality-filtered using Trimmomatic and FastQC, respectively.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Version used: **0.36**
- Evidence: Raw sequence data were trimmed using Trimmomatic v0.36 ( 50 ), with a minimum Phred score of 15.
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Version used: **0.36**
- Evidence: The raw reads were filtered to remove potential lower quality reads and artifacts using Trimmomatic v0.36 ( 51 ) and cutadapt v1.16 ( 52 ).
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: Raw FASTQ files were trimmed using Trimmomatic ( 67 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### Coordinated bacterial and plant sulfur metabolism in <i>Enterobacter</i> sp. SA187-induced plant salt stress tolerance. (PNAS 2021)

- DOI: 10.1073/pnas.2107417118 | PMCID: PMC8609655 | PMID: 34772809
- Evidence: Removal of low quality sequences and adaptor sequences, as well as additional trimming of 5′- and 3′-ends of bacteria derived reads, was performed by using Trimmomatic ( 49 ) applying the following parameters: minimum length of 36 bp, mean Phred quality score (Q) greater than 30, leading and trailing bases removal with base quality below 3, sliding window of 4:15.
- Full pipeline: quality control [R] -> read trimming [Trimmomatic] -> alignment/mapping [TopHat v2.0.9, featureCounts v1.6.5] -> quantification [Cufflinks v2.2.0, featureCounts v1.6.5] -> differential/statistical testing [Cufflinks v2.2.0] -> stage not stated [ImageJ]

### Restoring fertility in yeast hybrids: Breeding and quantitative genetics of beneficial traits. (PNAS 2021)

- DOI: 10.1073/pnas.2101242118 | PMCID: PMC8463882 | PMID: 34518218
- Version used: **0.36**
- Evidence: Paired-end raw Illumina sequence reads were quality checked through FastQC 0.11.5 ( 95 ) and trimmed through Trimmomatic 0.36 ( 96 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Version used: **0.38**
- Evidence: We trimmed and quality filtered raw reads using Trimmomatic v0.38 ( 36 ), and reads shorter than 30 bp and below a quality score of 20 were discarded.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **0.36**
- Evidence: Read quality trimming and adapter clipping of paired reads were done using Trimmomatic v0.36 ( 59 ) with the following options: ILLUMINACLIP:/all-PE.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:3:20 MINLEN:100.
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Version used: **0.39**
- Evidence: Trimmomatic version 0.39 ( 65 ) was used to remove low-quality reads and remaining adapter sequences from each read dataset.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### The DME demethylase regulates sporophyte gene expression, cell proliferation, differentiation, and meristem resurrection. (PNAS 2021)

- DOI: 10.1073/pnas.2026806118 | PMCID: PMC8307533 | PMID: 34266952
- Version used: **0.36**
- Evidence: Fragments with low-quality reads or reads with adaptors were filtered using Trimmomatic (v.0.36) ( 76 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0] -> visualisation [R, ggplot2] -> stage not stated [DESeq2, StringTie v2.1.3]

### An ecophysiological explanation for manganese enrichment in rock varnish. (PNAS 2021)

- DOI: 10.1073/pnas.2025188118 | PMCID: PMC8237629 | PMID: 34161271
- Evidence: Read preprocessing included no processing (raw reads), Bloom Filter Read Error Correction ( 79 ) v. r181 (drop_unique_kmer_reads = 1, kmer_size = 33), Trimmomatic ( 80 ) v.
- Full pipeline: read trimming [Trimmomatic] -> stage not stated [DADA2, ImageJ, QIIME 2, R]

### Fifty million years of beetle evolution along the Antarctic Polar Front. (PNAS 2021)

- DOI: 10.1073/pnas.2017384118 | PMCID: PMC8214695 | PMID: 34108239
- Evidence: Before assembly, the raw read fastq files were trimmed using Trimmomatic ( 76 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Clustal Omega, MAFFT] -> dimensionality reduction/clustering [R, RAxML] -> differential/statistical testing [MrBayes v3.2.6] -> structure determination [MAFFT] -> stage not stated [BEAST v2.5]

### Accurate genomic variant detection in single cells with primary template-directed amplification. (PNAS 2021)

- DOI: 10.1073/pnas.2024176118 | PMCID: PMC8214697 | PMID: 34099548
- Evidence: Data were trimmed using Trimmomatic ( 50 ) to remove adapter sequences and low-quality terminal bases, which was followed by GATK 4.1 best practices with genome assembly GRCh38.
- Full pipeline: read trimming [GATK v4.1, Trimmomatic] -> stage not stated [Picard]

### Prespacers formed during primed adaptation associate with the Cas1-Cas2 adaptation complex and the Cas3 interference nuclease-helicase. (PNAS 2021)

- DOI: 10.1073/pnas.2021291118 | PMCID: PMC8179228 | PMID: 34035168
- Evidence: Adapter sequences and low-quality (Phred score < 15) sequences were removed from reads with Trimmomatic ( 65 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2]

### Photosynthesis-independent production of reactive oxygen species in the rice bundle sheath during high light is mediated by NADPH oxidase. (PNAS 2021)

- DOI: 10.1073/pnas.2022702118 | PMCID: PMC8237631 | PMID: 34155141
- Evidence: Briefly, raw reads were processed using Trimmomatic ( 70 ), mapped to the reference rice transcriptome genome (MSU7.0, rice.plantbiology.msu.edu/index.shtml ), and quantified using Salmon ( 71 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> quantification [ImageJ, Trimmomatic] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [ggplot2]

### Epigenetic inheritance of DNA methylation changes in fish living in hydrogen sulfide-rich springs. (PNAS 2021)

- DOI: 10.1073/pnas.2014929118 | PMCID: PMC8255783 | PMID: 34185679
- Evidence: Reads were trimmed to remove adapters and low-quality bases using Trimmomatic ( 68 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [R, edgeR]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Version used: **0.36**
- Evidence: The reads were trimmed with Trimmomatic (version 0.36) ( 56 ) to remove Illumina adapters, low quality reads, and reads smaller than 40 bp.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Resetting proteostasis with ISRIB promotes epithelial differentiation to attenuate pulmonary fibrosis. (PNAS 2021)

- DOI: 10.1073/pnas.2101100118 | PMCID: PMC8157939 | PMID: 33972447
- Version used: **0.36**
- Evidence: FASTQ files were generated using bcl2fast (version 2.19.1) followed by quality control using FastQC, trimming using Trimmomatic (version 0.36), and mapping to the mm10 version of the mouse genome with Spliced Transcripts Alignment to a Reference aligner (STAR, version 2.6.0).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> alignment/mapping [FastQC, Trimmomatic v0.36] -> differential/statistical testing [edgeR v3.28.0] -> stage not stated [Fiji v1.8.0, HTSeq v0.11.2, ImageJ v1.8.0]

### The genomes of ancient date palms germinated from 2,000 y old seeds. (PNAS 2021)

- DOI: 10.1073/pnas.2025337118 | PMCID: PMC8126781 | PMID: 33941705
- Evidence: Reads were demultiplexed and those passing Illumina quality control filters were processed with Trimmomatic ( 71 ) v.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> variant calling [GATK v3.5] -> stage not stated [ADMIXTURE, Picard, R]

### Phylogenomic and ecological analyses reveal the spatiotemporal evolution of global pines. (PNAS 2021)

- DOI: 10.1073/pnas.2022302118 | PMCID: PMC8157994 | PMID: 33941644
- Version used: **0.36**
- Evidence: Raw reads were checked with FastQC (v.0.11.5) ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), trimmed using Trimmomatic (v.0.36) ( 63 ), and then assembled using Trinity (v.20140717) ( 64 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> dimensionality reduction/clustering [phytools v0.7] -> stage not stated [IQ-TREE v2.0, R v3.6.2, ggplot2]

### Predicting transcriptional responses to cold stress across plant species. (PNAS 2021)

- DOI: 10.1073/pnas.2026330118 | PMCID: PMC7958178 | PMID: 33658387
- Version used: **0.38**
- Evidence: The raw reads were quality-filtered, and adaptors were removed from the data with the sequence-preprocessing tool Trimmomatic (v0.38) ( 37 ) (MINLEN = 36, LEADING = 3, TRAILING = 3, SLIDINGWINDOW = 4,15).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [HTSeq v0.6.1, MAFFT v7.149, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [BEAST v5.1, DESeq2] -> simulation/modelling [BEAST v5.1] -> stage not stated [R]

### The synaptonemal complex imposes crossover interference and heterochiasmy in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023613118 | PMCID: PMC8000504 | PMID: 33723072
- Version used: **0.38**
- Evidence: The raw reads were evaluated for quality by using FastQC version 0.11.9 ( 95 ), and then potential adapter sequences were trimmed and low-quality bases were filtered using Trimmomatic version 0.38 ( 96 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.38] -> read trimming [FastQC v0.11.9, Trimmomatic v0.38]

### The imprinted lncRNA <i>Peg13</i> regulates sexual preference and the sex-specific brain transcriptome in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2022172118 | PMCID: PMC7958240 | PMID: 33658376
- Evidence: Raw sequence reads were quality trimmed using Trimmomatic ( 42 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### A versatile platform for locus-scale genome rewriting and verification. (PNAS 2021)

- DOI: 10.1073/pnas.2023952118 | PMCID: PMC7958457 | PMID: 33649239
- Version used: **0.39**
- Evidence: Illumina sequencing adapters were trimmed with Trimmomatic v0.39 ( 55 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9]

### Heat stress destabilizes symbiotic nutrient cycling in corals. (PNAS 2021)

- DOI: 10.1073/pnas.2022653118 | PMCID: PMC7865147 | PMID: 33500354
- Version used: **0.39**
- Evidence: Sequence reads were quality-trimmed and Illumina adapters were removed using Trimmomatic v.0.39 ( 86 ).
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [FastQC v0.11.5, Trimmomatic v0.39] -> alignment/mapping [Salmon v1.0.0] -> quantification [Salmon v1.0.0, lme4] -> differential/statistical testing [R, vegan v2.5] -> stage not stated [ImageJ]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Version used: **0.36**
- Evidence: (v0.4.4), Trimmomatic (v0.36), and Cutadapt (v1.16).
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### Multiclonal human origin and global expansion of an endemic bacterial pathogen of livestock. (PNAS 2022)

- DOI: 10.1073/pnas.2211217119 | PMCID: PMC9897428 | PMID: 36469788
- Version used: **0.36**
- Evidence: Short read sequences were adapter trimmed using Trimmomatic v0.36 ( 35 ) and de novo assembled using SPAdes v3.11.1 ( 36 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36] -> alignment/mapping [phytools] -> differential/statistical testing [BEAST, R] -> simulation/modelling [phytools] -> structure determination [phytools] -> stage not stated [InterProScan v5.52, Prokka v1.13]

### Sex pheromone communication in an insect parasitoid, <i>Campoletis chlorideae</i> Uchida. (PNAS 2022)

- DOI: 10.1073/pnas.2215442119 | PMCID: PMC9894188 | PMID: 36442117
- Evidence: Adapter sequences, poly-N, and low-quality reads were removed by Trimmomatic, and the clean reads were assembled by Trinity v2.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM v1.2.15] -> quantification [RSEM v1.2.15] -> stage not stated [BLAST]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: The reads were trimmed and quality controlled using Trimmomatic ( 75 ) and then assembled using SPAdes ( 76 ) and annotated via Prokka ( 77 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Silencing RNAs expressed from W-linked &lt;i&gt;PxyMasc&lt;/i&gt; "retrocopies" target that gene during female sex determination in &lt;i&gt;Plutella xylostella&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2206025119 | PMCID: PMC9674220 | PMID: 36343250
- Evidence: 15013207) and the poor-quality reads (Phred scores; Q < 20) were removed using Trimmomatic ( 38 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [BLAST, Clustal Omega]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: Adapters were trimmed from the raw reads with Trimmomatic ( 75 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Version used: **0.33**
- Evidence: We used Trimmomatic v0.33 ( 75 ) to remove Illumina adapter sequences and quality-trim reads (minimum q-score of 30 evaluated on 4-base sliding windows; minimum read length of 50) and BBDuk v38.82 ( 76 ) to remove PhiX sequences.
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### Experimental evolution reveals the synergistic genomic mechanisms of adaptation to ocean warming and acidification in a marine copepod. (PNAS 2022)

- DOI: 10.1073/pnas.2201521119 | PMCID: PMC9499500 | PMID: 36095205
- Version used: **0.36**
- Evidence: Raw reads were trimmed for quality and adapter contamination with Trimmomatic v.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [VarScan] -> stage not stated [MrBayes]

### Different classes of genomic inserts contribute to human antibody diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2205470119 | PMCID: PMC9457163 | PMID: 36037353
- Evidence: Illumina reads received from suppression PCR libraries of IGH, IGL, and IGK chain profiling were processed as follows: reads were paired by PEAR software ( 75 ), adapters were removed with Trimmomatic ( 76 ), and constant genes mapped by an in-house script in R ( 73 ).
- Full pipeline: quality control [FastQC] -> read trimming [R, Trim Galore, Trimmomatic] -> alignment/mapping [R, Trimmomatic] -> stage not stated [BEDTools, MACS2, ggplot2]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Reads were trimmed with Trimmomatic ( 51 ) and mapped to hg19 with BWA ( 52 ).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Version used: **0.39**
- Evidence: To infer the binding motif of a TF from DAP-seq data, the PE reads were preprocessed to remove adapters, and low-quality bases were trimmed off using Trimmomatic (version 0.39) ( 57 ) with options ILLUMINACLIP:- TruSeq3-PE.fa:2:40:12:8:true LEADING:10 SLIDINGWINDOW:4:15 MINLEN:50.
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Version used: **0.32**
- Evidence: Reads were trimmed for low-quality bases and adaptor contamination using Trimmomatic (version 0.32) ( 53 ), using the following options: trailing = 15 (cut bases at the end of the read if below a threshold quality of 15), slidingwindow = 4:20 (performs a sliding window trimming, cutting once the average quality within the window falls below a threshold of 20), and illuminaclip = TruSeq3-PE.fa:2:20...
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Historical contingencies and phage induction diversify bacterioplankton communities at the microscale. (PNAS 2022)

- DOI: 10.1073/pnas.2117748119 | PMCID: PMC9335236 | PMID: 35862452
- Version used: **0.36**
- Evidence: Raw sequencing reads were quality trimmed with Trimmomatic v0.36 ( 54 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BEDTools v2.27.0]

### Genetic variation that determines &lt;i&gt;TAPBP&lt;/i&gt; expression levels associates with the course of malaria in an HLA allotype-dependent manner. (PNAS 2022)

- DOI: 10.1073/pnas.2205498119 | PMCID: PMC9303992 | PMID: 35858344
- Version used: **0.33**
- Evidence: Fastp v0.19.7 and Trimmomatic v0.33 with default parameters were used to trim low-quality bases from both ends of each read ( 46 , 47 ).
- Full pipeline: read trimming [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, Trimmomatic v0.33, edgeR] -> alignment/mapping [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, edgeR] -> variant calling [BCFtools v1.9, R, edgeR] -> normalisation [BCFtools v1.9, R, edgeR]

### The evolution of synaptic and cognitive capacity: Insights from the nervous system transcriptome of &lt;i&gt;Aplysia&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122301119 | PMCID: PMC9282427 | PMID: 35867761
- Evidence: Illumina paired-end reads ( n = 2.97 billion) were trimmed with Trimmomatic and processed through three assemblers: DN-Trinity, which was used in all pilot assemblies; genome-guided de novo Trinity (GG-Trinity); and StringTie.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> differential/statistical testing [RAxML] -> stage not stated [BUSCO]

### A long noncoding RNA influences the choice of the X chromosome to be inactivated. (PNAS 2022)

- DOI: 10.1073/pnas.2118182119 | PMCID: PMC9282422 | PMID: 35787055
- Version used: **0.36.6**
- Evidence: Adapters were removed with Trimmomatic v0.36.6 and sequences having an average quality below 20 were eliminated.
- Full pipeline: read trimming [Trimmomatic v0.36.6] -> alignment/mapping [Bowtie2 v2.3.4.2] -> stage not stated [Fiji, ImageJ, SAMtools v1.1.2]

### Metatranscriptomics captures dynamic shifts in mycorrhizal coordination in boreal forests. (PNAS 2022)

- DOI: 10.1073/pnas.2118852119 | PMCID: PMC9245616 | PMID: 35727987
- Evidence: Norway spruce RNA-seq data were preprocessed and aligned with SortmeRNA ( 107 ), Trimmomatic ( 108 ), and Salmon ( 109 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> differential/statistical testing [DESeq2] -> stage not stated [eggNOG]

### Nuclear speckle integrity and function require TAO2 kinase. (PNAS 2022)

- DOI: 10.1073/pnas.2206046119 | PMCID: PMC9231605 | PMID: 35704758
- Evidence: Raw sequence data were trimmed using Trimmomatic ( 45 ).
- Full pipeline: quality control [STAR] -> read trimming [STAR, Trimmomatic] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor v3.11, R v4.0.2]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: Filtering and trimming of reads was performed in Trimmomatic ( 72 ) ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **0.38**
- Evidence: Illumina short read sequencing data from both DNA and RNA were trimmed using Trimmomatic v0.38 ( 43 ) (ILLUMINACLIP:adapters.fa:2:30:10 SLIDINGWINDOW:4:5 LEADING:5 TRAILING:5 MINLEN:25); only reads from pairs where both mates survived trimming were used in downstream analysis.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Version used: **0.38**
- Evidence: Adapter sequences and low-quality regions were removed using Trimmomatic (v0.38) ( 83 ) (ILLUMINACLIP:Y2_adapter_seq.fa:0:6:6 SLIDINGWINDOW:10:20 MINLEN:36).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Version used: **0.32**
- Evidence: The libraries were cleaned using Trimmomatic (version 0.32; command line options: LEADING:20 TRAILING:20 SLIDINGWINDOW:5:20 MINLEN:85, phred33) ( 36 ) and FastQC (version 0.11.3) ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to remove adaptors and low-quality reads.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### A synthetic lethality screen reveals ING5 as a genetic dependency of catalytically dead Set1A/COMPASS in mouse embryonic stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2118385119 | PMCID: PMC9171609 | PMID: 35500115
- Evidence: Raw BCL (basecall) output files were converted into fastq files using bcl2fastq (Illumina, version 2.17.1.14), followed by quality trimming using Trimmomatic ( 67 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [ImageJ, MACS2, Metascape]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Version used: **0.32**
- Evidence: Trimmomatic (version 0.32) was then used to remove adapters, platform-specific sequences, and low-quality leading and trailing bases from reads ( 55 ).
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### A preclinical platform for assessing antitumor effects and systemic toxicities of cancer drug targets. (PNAS 2022)

- DOI: 10.1073/pnas.2110557119 | PMCID: PMC9169916 | PMID: 35442775
- Evidence: Resulting RNA-seq data were analyzed by removing adaptor sequences using Trimmomatic ( 45 ).
- Full pipeline: read trimming [Trimmomatic] -> quantification [ImageJ] -> stage not stated [GSEA]

### Multikingdom interactions govern the microbiome in subterranean cultural heritage sites. (PNAS 2022)

- DOI: 10.1073/pnas.2121141119 | PMCID: PMC9169738 | PMID: 35344401
- Version used: **0.36**
- Evidence: Raw reads were trimmed to eliminate adapters and low-quality reads with Trimmomatic v0.36 ( 48 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> stage not stated [R, eggNOG]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: After sequencing, the individual datasets were quality-trimmed using Trimmomatic ( 58 ).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Diverse methylotrophic methanogenic archaea cause high methane emissions from seagrass meadows. (PNAS 2022)

- DOI: 10.1073/pnas.2106628119 | PMCID: PMC8892325 | PMID: 35165204
- Version used: **0.32**
- Evidence: Adapter and quality trimming of raw metagenomic Illumina reads was performed using Trimmomatic 0.32 ( 69 ) (parameters: LEADING:3 TRAILING:3 SLIDINGWINDOW:4:10 MINLEN:200), and each metagenomic Illumina dataset obtained from 2019 was assembled individually using metaSPAdes 3.13.0 ( 70 ) and standard parameters.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [MAFFT] -> stage not stated [HMMER, IQ-TREE, QGIS, SPAdes]

### The dynamic trophic architecture of open-ocean protist communities revealed through machine-guided metatranscriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2100916119 | PMCID: PMC8851463 | PMID: 35145022
- Version used: **0.36**
- Evidence: Briefly, the reads were quality controlled using Trimmomatic (v0.36) ( 61 ) and normalized using the normalize-by-median.py script from the khmer software package ( 62 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> normalisation [Trimmomatic v0.36, kallisto] -> differential/statistical testing [DESeq2] -> machine learning [XGBoost] -> stage not stated [HMMER v3.1b]

### Definition of a mouse microglial subset that regulates neuronal development and proinflammatory responses in the brain. (PNAS 2022)

- DOI: 10.1073/pnas.2116241119 | PMCID: PMC8872761 | PMID: 35177477
- Version used: **0.36**
- Evidence: After reviewing the quality of the raw data, sequence reads were trimmed to remove possible adapter sequences and nucleotides with poor quality using Trimmomatic v0.36.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> stage not stated [MACS2]

### Engineering and functional analysis of yeast with a monotypic 40S ribosome subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2114445119 | PMCID: PMC8833219 | PMID: 35105807
- Version used: **0.36**
- Evidence: The quality of the raw reads was first evaluated with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), and then low-quality reads were excluded using Trimmomatic (0.36) with default parameters ( 45 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> variant calling [GATK v3.5, SnpEff] -> registration [GATK v3.5] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [Picard]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: Reads were trimmed for quality, sequencing adapters, and mate pair adapters using Trimmomatic ( 42 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Version used: **0.39**
- Evidence: For QuantSeq, raw RNA-seq reads were trimmed using Trimmomatic v.0.39 ( 75 ), and data were aligned using the bowtie2 ( 76 ) algorithm against the hg38 human genome version.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Version used: **0.36.3**
- Evidence: RNA-seq sequencing libraries were trimmed using Trimmomatic (version 0.36.3) ( 87 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### Circadian key component CLOCK/BMAL1 interferes with segmentation clock in mouse embryonic organoids. (PNAS 2022)

- DOI: 10.1073/pnas.2114083119 | PMCID: PMC8746294 | PMID: 34930826
- Evidence: After trimming the adaptor sequences using Trimmomatic ( 41 ), the reads that mapped to ribosomal DNA (GenBank: BK000964.1 ) ( 42 ) were filtered out, and the sequence reads were mapped to the mouse genome (GRCm38/mm10) using spliced transcript alignment to a reference (STAR) ( 43 ), as described previously ( 16 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [DESeq2, Trimmomatic] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, pheatmap]

### No link between population isolation and speciation rate in squamate reptiles. (PNAS 2022)

- DOI: 10.1073/pnas.2113388119 | PMCID: PMC8795558 | PMID: 35058358
- Version used: **0.39**
- Evidence: For the raw sequencing reads per sample, we first trimmed adapters using Trimmomatic v0.39, removed low-quality sequences, and then merged overlapping paired reads using PEAR v0.9.11 ( 93 , 94 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [GATK v4.1.8, RAxML v8.2.11, SAMtools v1.5] -> stage not stated [R, phytools]

### Conservation of magnetite biomineralization genes in all domains of life and implications for magnetic sensing. (PNAS 2022)

- DOI: 10.1073/pnas.2108655119 | PMCID: PMC8784154 | PMID: 35012979
- Evidence: The raw Illumina reads were quality processed with Trimmomatic ( 56 ) (version 0.32), removing adapter contaminants and low-quality sequences and retaining reads ≥25 nucleotides in length with an average sequencing quality of phred 20 across 4 nucleotide sliding windows.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2 v2.2.1] -> normalisation [R v3.12.1] -> dimensionality reduction/clustering [R v3.12.1] -> differential/statistical testing [BLAST, edgeR] -> visualisation [R v3.12.1] -> stage not stated [ImageJ]

### Deconstructing <i>Methanosarcina acetivorans</i> into an acetogenic archaeon. (PNAS 2022)

- DOI: 10.1073/pnas.2113853119 | PMCID: PMC8764690 | PMID: 34992140
- Version used: **0.39**
- Evidence: Trimmomatic v0.39 ( 63 ) was used for quality filtering of the raw reads and Bowtie2 ( 64 ) for the mapping on the reference genome M. acetivorans C2A genome sequence ( 65 ) (accession no.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Sequence quality was assessed using FastQC v 0.11.2 ( 42 ), and quality trimming was done using Trimmomatic ( 43 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### &lt;i&gt;GRASSY TILLERS1&lt;/i&gt; (&lt;i&gt;GT1&lt;/i&gt;) and &lt;i&gt;SIX-ROWED SPIKE1&lt;/i&gt; (&lt;i&gt;VRS1&lt;/i&gt;) homologs share conserved roles in growth repression. (PNAS 2023)

- DOI: 10.1073/pnas.2311961120 | PMCID: PMC10742383 | PMID: 38096411
- Evidence: Sequenced RNA libraries were trimmed for quality using Trimmomatic and mapped to the Zea mays (maize) B73 version 5 genome using STAR 2.7.9a ( 78 , 79 ).
- Full pipeline: read trimming [STAR v2.7.9a, Trimmomatic] -> alignment/mapping [HTSeq, MAFFT, STAR v2.7.9a, Trimmomatic] -> differential/statistical testing [DESeq2] -> visualisation [IQ-TREE, R]

### The emergence and diversification of a zoonotic pathogen from within the microbiota of intensively farmed pigs. (PNAS 2023)

- DOI: 10.1073/pnas.2307773120 | PMCID: PMC10666105 | PMID: 37963246
- Evidence: Raw sequence reads were preprocessed using Trimmomatic V0.36 to remove adaptors, trim poor-quality ends, and delete short sequences (<36 nt) ( 51 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v1.2.2, QUAST v5.0.1] -> stage not stated [Canu v1.9, Prokka v1.14.5, R]

### Evidence for an ancient aquatic origin of the RNA viral order &lt;i&gt;Articulavirales&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2310529120 | PMCID: PMC10636315 | PMID: 37906647
- Version used: **0.38**
- Evidence: Raw sequencing reads were trimmed using Trimmomatic v0.38 ( 47 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.490, MUSCLE v5.1] -> quantification [RSEM v1.3.0] -> visualisation [R v4.1] -> stage not stated [BLAST v2.0.9]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Version used: **0.36**
- Evidence: Sequencing reads were trimmed with Trimmomatic (v0.36) to remove adapters and low-quality sequence (settings: LEADING:5 TRAILING:5 SLIDINGWINDOW:4:20 MINLEN:50).
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Evidence: RNA sequencing data from different tissues were quality-filtered by Trimmomatic ( 65 ). and then assembled by Trinity ( 66 ).
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Version used: **0.36**
- Evidence: The adapters and low-quality reads were removed using Trimmomatic (version 0.36) ( 70 ) with the parameters “ILLUMINACLIP: adapter. fa: 2:30:10 LEADING:20 TRAILING:20 MINLEN:36 SLIDINGWINDOW: 4:20.” The quality-controlled reads were then aligned to the soybean ZH13 reference genome ( 35 ) using Burrows Wheeler Aligner BWA-MEM software ( 71 ) with default parameters and were further filtered by SAM...
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Evidence: The quality of the resultant 150-bp paired-end RNA-seq reads was assessed by FastQC (available at https://qubeshub.org/resources/fastqc ), and low-quality bases/reads were trimmed or filtered out using Trimmomatic ( 62 ) with default parameters (ILLUMINACLIP:adapter:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Widespread use of proton-pumping rhodopsin in Antarctic phytoplankton. (PNAS 2023)

- DOI: 10.1073/pnas.2307638120 | PMCID: PMC10523587 | PMID: 37722052
- Version used: **0.38**
- Evidence: Sequences were quality filtered with Trimmomatic v0.38 and assembled as described in ref.
- Full pipeline: read trimming [Trimmomatic v0.38]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: RNA-seq datasets ( GSE101646 ) were subjected to quality control using FastQC, followed by trimming with Trimmomatic to ensure high-quality data.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Sequencing 4.3 million mutations in wheat promoters to understand and modify gene expression. (PNAS 2023)

- DOI: 10.1073/pnas.2306494120 | PMCID: PMC10515147 | PMID: 37703281
- Version used: **0.39**
- Evidence: Illumina sequencing reads were preprocessed to trim adapters with Trimmomatic v0.39 ( 89 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, SAMtools v1.7] -> stage not stated [VEP]

### Cooperative regulation of coupled oncoprotein synthesis and stability in triple-negative breast cancer by EGFR and CDK12/13. (PNAS 2023)

- DOI: 10.1073/pnas.2221448120 | PMCID: PMC10515179 | PMID: 37695916
- Version used: **0.32**
- Evidence: Sequences were processed using Trimmomatic v0.32 ( 87 ) and reads that were 20 nt or longer after trimming were filtered for further analysis.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [RSEM v1.2.25, STAR v2.4.1a] -> quantification [ImageJ, RSEM v1.2.25] -> differential/statistical testing [DESeq2 v1.22.0] -> stage not stated [Bioconductor]

### Environmental DNA reveals the genetic diversity and population structure of an invasive species in the Laurentian Great Lakes. (PNAS 2023)

- DOI: 10.1073/pnas.2307345120 | PMCID: PMC10500163 | PMID: 37669387
- Version used: **0.39**
- Evidence: Sequencing adapters were trimmed with Trimmomatic v0.39 ( 54 ), and sequence quality was assessed with FastQC version 0.11.8 ( 55 ).
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.39] -> read trimming [FastQC v0.11.8, Trimmomatic v0.39] -> differential/statistical testing [R v4.1] -> stage not stated [DADA2, lme4]

### The genomic landscape of swine influenza A viruses in Southeast Asia. (PNAS 2023)

- DOI: 10.1073/pnas.2301926120 | PMCID: PMC10438389 | PMID: 37552753
- Version used: **0.39**
- Evidence: The NGS reads were checked with FastQC ( 48 ) in Unipro UGENE v40.1 ( 49 ) and were processed by trimming adaptors via Trimmomatic v0.39 ( 50 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.39] -> read trimming [FastQC, Trimmomatic v0.39] -> structure determination [BEAST v10.4, RAxML v1.1.0] -> stage not stated [BLAST v2.2.18, SPAdes v3.15.3]

### Host hydrocarbons protect symbiont transmission from a radical host defense. (PNAS 2023)

- DOI: 10.1073/pnas.2302721120 | PMCID: PMC10400980 | PMID: 37487102
- Evidence: Sequences were quality-controlled and trimmed using FastQC ( 96 ) and Trimmomatic ( 97 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> differential/statistical testing [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> visualisation [ggplot2]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **0.39**
- Evidence: The raw sequencing reads of the remaining 262 accessions were downloaded from the National Center for Biotechnology Information's (NCBI) SRA submission portal, trimmed using Trimmomatic v0.39 ( 70 ) and de novo assembled using Megahit v1.2.9 ( 71 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Echoes of ancient introgression punctuate stable genomic lineages in the evolution of figs. (PNAS 2023)

- DOI: 10.1073/pnas.2222035120 | PMCID: PMC10334730 | PMID: 37399402
- Evidence: For the All- Ficus samples, we trimmed reads using Trimmomatic (ILLUMINACLIP: TruSeq3-PE.fa:2:30:10 HEADCROP:3 LEADING:30 TRAILING:25 SLIDINGWINDOW:4:25 MINLEN:20) ( 59 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.450, RAxML] -> stage not stated [SAMtools]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Evidence: Low-quality reads were removed and adapters were trimmed using Trimmomatic v36 ( 65 ), and error correction was performed using ALLPATHS-LG ( 66 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### &lt;i&gt;Trachymyrmex septentrionalis&lt;/i&gt; ants promote fungus garden hygiene using &lt;i&gt;Trichoderma&lt;/i&gt;-derived metabolite cues. (PNAS 2023)

- DOI: 10.1073/pnas.2219373120 | PMCID: PMC10288546 | PMID: 37319116
- Version used: **0.39**
- Evidence: For the Environmental ITS2 dataset, (NCBI accession: PRJNA763335, SI Appendix , Dataset S1 ) forward reads from 90 samples were processed using Trimmomatic v0.39 ( 65 ) with options SLIDINGWINDOW 5:20 and MINLEN:125 and then processed in R v.3.6.3 using the DADA2 v1.16.0 ( 66 ) ITS workflow ( https://benjjneb.github.io/dada2/ITS_workflow.html , accessed May 26, 2021) except using only forward read...
- Full pipeline: read trimming [DADA2 v1.16.0, Trimmomatic v0.39] -> quantification [phyloseq]

### Adaptive structural and functional evolution of the placenta protects fetal growth in high-elevation deer mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218049120 | PMCID: PMC10288601 | PMID: 37307471
- Evidence: Data were trimmed for adaptor contamination and quality using Trimmomatic ( 95 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [ImageJ v2.0.0, featureCounts] -> stage not stated [R v4.0, WGCNA, emmeans, lme4]

### The developmental basis for scaling of mammalian tooth size. (PNAS 2023)

- DOI: 10.1073/pnas.2300374120 | PMCID: PMC10288632 | PMID: 37307487
- Evidence: 0.9.6 ( 67 )], and Trimmomatic [v.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> differential/statistical testing [R]

### Nontriplet feature of genetic code in &lt;i&gt;Euplotes&lt;/i&gt; ciliates is a result of neutral evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2221683120 | PMCID: PMC10235951 | PMID: 37216548
- Evidence: The resulting read libraries were trimmed with Trimmomatic ( 105 ) with parameters: ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [kallisto] -> stage not stated [BLAST]

### Aneuploidy effects on human gene expression across three cell types. (PNAS 2023)

- DOI: 10.1073/pnas.2218478120 | PMCID: PMC10214149 | PMID: 37192167
- Evidence: RNA-seq data from these three cell types were separately submitted to the following workflow ( SI Appendix , Text S1.1 ): i) FastQC ( 45 ), MultQC ( 46 ), and Trimmomatic ( 47 ) for QC and trimming, ii) Salmon ( 48 ) for transcript quantification with the Y chromosome masked reference transcriptome when mapping female samples and with the YPAR-gene masked one when mapping male samples to reduce mi...
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [DESeq2, FastQC, Trimmomatic] -> quantification [FastQC, Trimmomatic] -> dimensionality reduction/clustering [GSEA] -> stage not stated [R v4.1.0]

### Digital microfluidics-based digital counting of single-cell copy number variation (dd-scCNV Seq). (PNAS 2023)

- DOI: 10.1073/pnas.2221934120 | PMCID: PMC10193948 | PMID: 37155890
- Version used: **0.38**
- Evidence: Trimmomatic (version 0.38) was used to remove the adaptor and barcode sequences from the raw data.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.38] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.9] -> differential/statistical testing [SAMtools v1.9] -> stage not stated [BEDTools]

### Generation of zero-valent sulfur from dissimilatory sulfate reduction in sulfate-reducing microorganisms. (PNAS 2023)

- DOI: 10.1073/pnas.2220725120 | PMCID: PMC10194018 | PMID: 37155857
- Version used: **0.35**
- Evidence: RNA-Seq raw data in fastq format were processed by Trimmomatic (v.0.35) ( 63 ) to acquire the clean reads.
- Full pipeline: read trimming [Trimmomatic v0.35] -> alignment/mapping [Bowtie2 v2.33, HTSeq] -> quantification [HTSeq] -> stage not stated [mothur v1.39]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Version used: **0.35**
- Evidence: Reads were aligned to hg38 using a Bpipe ( 92 ) RNA-Seq pipeline that incorporated FastQC quality control, adaptor trimming with Trimmomatic v.0.35 ( 93 ), mapping with STAR 2.7.3a ( 94 ), summarizing reads over genes with featureCounts ( 95 ), and MultiQC ( 96 ) to summarize the analyses.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Epistasis reduces fitness costs of influenza A virus escape from stem-binding antibodies. (PNAS 2023)

- DOI: 10.1073/pnas.2208718120 | PMCID: PMC10151473 | PMID: 37068231
- Version used: **0.39**
- Evidence: In brief, after removing adapters using Trimmomatic (version 0.39) ( 59 ), reads were aligned to their reference sequence using the option mem from BWA ( 60 ).
- Full pipeline: read trimming [BWA, Trimmomatic v0.39] -> alignment/mapping [BWA, Trimmomatic v0.39] -> stage not stated [GATK, Picard]

### Ancient DNA from a lost Negev Highlands desert grape reveals a Late Antiquity wine lineage. (PNAS 2023)

- DOI: 10.1073/pnas.2213563120 | PMCID: PMC10151551 | PMID: 37068234
- Version used: **0.36**
- Evidence: Adaptor contamination was removed using LeeHom software ( 63 ) and low-quality reads and reads shorter than 25 bp were removed using Trimmomatic version 0.36 ( 64 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.5] -> variant calling [GATK, VCFtools] -> dimensionality reduction/clustering [pheatmap] -> visualisation [ggplot2]

### <i>Salmonella</i> Typhimurium uses the Cpx stress response to detect <i>N</i>-chlorotaurine and promote the repair of oxidized proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2215997120 | PMCID: PMC10083560 | PMID: 36976766
- Version used: **0.39**
- Evidence: After read cleaning (Trimmomatic v0.39), we performed variant calling using Snippy (v4.3.6; https://github.com/tseemann/snippy ) referring to the genome sequence GCF_000022165 (National Center for Biotechnology Information).
- Full pipeline: read trimming [Trimmomatic v0.39] -> variant calling [Trimmomatic v0.39]

### Euglenozoan kleptoplasty illuminates the early evolution of photoendosymbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2220100120 | PMCID: PMC10041101 | PMID: 36927158
- Evidence: Adapters, shortest reads (<36 bp), and poor-quality reads (mean Phred quality value of <15) were removed with the Trimmomatic tool v0.38 ( 41 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [IQ-TREE, MAFFT] -> differential/statistical testing [IQ-TREE] -> stage not stated [BUSCO, SPAdes v3.10.1]

### Experimental evidence for the functional importance and adaptive advantage of A-to-I RNA editing in fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2219029120 | PMCID: PMC10041177 | PMID: 36917661
- Evidence: Low-quality reads and reads containing adapters were removed by Trimmomatic ( 66 ) with default settings.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [R v4.1, featureCounts] -> normalisation [featureCounts] -> visualisation [AlphaFold, R v4.1, UCSF Chimera v1.16] -> stage not stated [BLAST]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **0.36**
- Evidence: We used IsoSeq3 (3.1.0) ( 75 ) and Trimmomatic (0.36) ( 76 ) for pre-processing the raw reads.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Two differentially stable rDNA loci coexist on the same chromosome and form a single nucleolus. (PNAS 2023)

- DOI: 10.1073/pnas.2219126120 | PMCID: PMC9992848 | PMID: 36821584
- Evidence: Briefly, reads were processed by Illumina barcode and quality trimmed with Trimmomatic ( 55 ) and quality assessed with FastQC ( 56 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2] -> visualisation [ImageJ] -> stage not stated [kallisto]

### Definition of the contribution of an Osteopontin-producing CD11c<sup>+</sup> microglial subset to Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2218915120 | PMCID: PMC9963365 | PMID: 36730200
- Version used: **0.36**
- Evidence: After quality check of raw data, sequence reads were trimmed to remove possible adapter sequences and nucleotides with poor quality using Trimmomatic v.0.36.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [MACS2]

### Resurrection genomics provides molecular and phenotypic evidence of rapid adaptation to salinization in a keystone aquatic species. (PNAS 2023)

- DOI: 10.1073/pnas.2217276120 | PMCID: PMC9963159 | PMID: 36730191
- Evidence: Raw sequencing reads were quality trimmed and adaptor contamination removed using Trimmomatic ( 75 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools, BEDTools, SAMtools, VEP]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Version used: **0.39**
- Evidence: Sequencing adaptors were removed using Trimmomatic (version 0.39) ( 108 ), which was also used to trim low-quality bases at the 5′ end of reads (using parameters TRAILING:20 and SLIDINGWINDOW:5:20).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### Community interactions drive the evolution of antibiotic tolerance in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2209043119 | PMCID: PMC9934204 | PMID: 36634144
- Version used: **0.36**
- Evidence: We trimmed all raw sequencing reads using Trimmomatic 0.36, using default settings.
- Full pipeline: read trimming [Trimmomatic v0.36] -> variant calling [freebayes v1.3.2] -> differential/statistical testing [freebayes v1.3.2]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: We removed sequencing and sample barcode adapters as well as trimmed and filtered reads based on quality scores using Illumiprocessor ( 84 ) (v2.09), a wrapper for the read filtering program Trimmomatic ( 85 ) (v0.32).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Non-B-form DNA tends to form in centromeric regions and has undergone changes in polyploid oat subgenomes. (PNAS 2023)

- DOI: 10.1073/pnas.2211683120 | PMCID: PMC9910436 | PMID: 36574697
- Version used: **0.36**
- Evidence: Then, the adaptors and low-quality bases were removed with Trimmomatic v.0.36 ( 67 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA, Trimmomatic v0.36] -> alignment/mapping [BWA, MACS2, SAMtools v1.3.1, deepTools] -> normalisation [deepTools] -> visualisation [deepTools]

### Discovery of antibodies and cognate surface targets for ovarian cancer by surface profiling. (PNAS 2023)

- DOI: 10.1073/pnas.2206751120 | PMCID: PMC9910589 | PMID: 36574667
- Version used: **0.38**
- Evidence: Trimmomatic (version 0.38) was first used to remove fragments with low base calling quality (average Phred score < 30) and clip Illumina adapter sequences from all reads ( 45 ).
- Full pipeline: read trimming [Trimmomatic v0.38]

### Proteomic analysis of the sponge Aggregation Factor implicates an ancient toolkit for allorecognition and adhesion in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2409125121 | PMCID: PMC11670116 | PMID: 39693348
- Evidence: The corrected reads were then quality-trimmed using Trimmomatic via Trinity v.2.4.0 with the default settings ( 76 ).
- Full pipeline: read trimming [PyMOL, Trimmomatic] -> stage not stated [AlphaFold, BUSCO, HMMER]

### Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase. (PNAS 2024)

- DOI: 10.1073/pnas.2423270121 | PMCID: PMC11670102 | PMID: 39689177
- Version used: **0.39**
- Evidence: For single-cell FOODIE data analysis, adapter sequences are first trimmed using Trimmomatic (version 0.39) ( 49 ), followed by mapping to the mouse reference genome mm10 with Bismark (version 0.24.0) ( 48 ).
- Full pipeline: quality control [ArchR, UMAP] -> read trimming [Bismark, Python, Trim Galore v0.6.10, Trimmomatic v0.39] -> alignment/mapping [Bismark, Trim Galore v0.6.10, Trimmomatic v0.39] -> dimensionality reduction/clustering [ArchR, UMAP]

### Mutation-based mechanism and evolution of the potent multidrug efflux pump RE-CmeABC in &lt;i&gt;Campylobacter&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2415823121 | PMCID: PMC11665921 | PMID: 39602248
- Evidence: After sequencing, quality control of the raw sequence reads was done by using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and trimmed by Trimmomatic ( 59 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic] -> alignment/mapping [Bowtie2, MAFFT] -> stage not stated [Python]

### The HUSH epigenetic repressor complex silences PML nuclear body-associated HSV-1 quiescent genomes. (PNAS 2024)

- DOI: 10.1073/pnas.2412258121 | PMCID: PMC11626126 | PMID: 39589886
- Version used: **0.39**
- Evidence: Raw reads were filtered by trimming Illumina adapters and removing low-quality reads using Trimmomatic (v.0.39) with default parameters.
- Full pipeline: read trimming [Bowtie2 v2.5.1, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.1] -> stage not stated [ImageJ]

### Implantable 3D printed hydrogels with intrinsic channels for liver tissue engineering. (PNAS 2024)

- DOI: 10.1073/pnas.2403322121 | PMCID: PMC11588097 | PMID: 39531491
- Version used: **0.36**
- Evidence: Sequence reads were trimmed to remove possible adapter sequences and nucleotides with poor quality using Trimmomatic v.0.36.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> stage not stated [GSEA]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: Raw data processing was performed using FASTQC ( 51 ) to check the reads quality and Trimmomatic ( 52 ) tool to further remove the bases and reads with low quality, adaptors, and barcodes.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### Soil viral-host interactions regulate microplastic-dependent carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2413245121 | PMCID: PMC11551317 | PMID: 39467127
- Version used: **0.36**
- Evidence: Trimmomatic (v0.36) was used for raw data processing and purchased the clean data ( 70 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BLAST, Bowtie2, HMMER] -> quantification [Bowtie2] -> stage not stated [DESeq2, R v4.0.3, vegan]

### A novel &lt;i&gt;N&lt;/i&gt;4,&lt;i&gt;N&lt;/i&gt;4-dimethylcytidine in the archaeal ribosome enhances hyperthermophily. (PNAS 2024)

- DOI: 10.1073/pnas.2405999121 | PMCID: PMC11551388 | PMID: 39471227
- Evidence: Fastq reads were subjected to adapter trimming and quality control using Trimmomatic.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [AlphaFold]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Version used: **0.36**
- Evidence: Raw reads were quality filtered with Trimmomatic 0.36 ( 76 ) then mapped and quantified against the Burmese python reference genome ( 27 ) with STAR 2.7.10a ( 77 ).
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Low-quality reads and sequencing adapters were removed using Trimmomatic [PE -phred33 LEADING:10 TRAILING:10 SLIDINGWINDOW:4:15 MINLEN:50; ( 71 )] and the surviving reads aligned to the B. fruticulosa reference genome using bwa-mem2 ( 72 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: The initial steps involved stringent quality control and decontamination measures using Trimmomatic to eliminate low-quality and contaminated sequences ( 44 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Imprinted X chromosome inactivation in marsupials: The paternal X arrives at the egg with a silent DNA methylation profile. (PNAS 2024)

- DOI: 10.1073/pnas.2412185121 | PMCID: PMC11388282 | PMID: 39190362
- Evidence: All raw reads were trimmed using Trimmomatic ( 46 ) (version 0.38) with a head crop of 10, sliding window of 5:15, and minimum length of 30.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bismark] -> normalisation [R] -> stage not stated [SAMtools]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **0.33.0**
- Evidence: Adapter sequences and low-quality bases were removed from the raw sequencing reads using Trimmomatic (v0.33.0) ( 57 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: Raw reads were trimmed with Trimmomatic, reads were mapped using STAR, and FPKM tables were generated using StringTie.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### UPF1 deficiency enhances mitochondrial ROS which promotes an immunosuppressive microenvironment in pancreatic ductal adenocarcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2401996121 | PMCID: PMC11331118 | PMID: 40591563
- Evidence: Briefly, raw reads were fed into “rna-star” module of Seq-N-Slide which employs Trimmomatic for adaptor trimming and low-quality base removal, STAR for alignment to reference genomes (mm10), fastq_screen for contaminant detection, Picard for base distribution and 5′/3′ biases, and featureCounts to generate genes-samples count matrices.
- Full pipeline: read trimming [Picard, STAR, Trimmomatic, featureCounts] -> alignment/mapping [Picard, STAR, Trimmomatic, featureCounts] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2]

### Lining the small intestine with mycobacteriophages protects from &lt;i&gt;Mycobacterium avium&lt;/i&gt; subsp. &lt;i&gt;paratuberculosis&lt;/i&gt; and eliminates fecal shedding. (PNAS 2024)

- DOI: 10.1073/pnas.2318627121 | PMCID: PMC11331133 | PMID: 39102547
- Evidence: Illumina adaptor sequences were trimmed using Trimmomatic, ( 44 ) and quality control was performed using FastQC v0.12.1 ( 45 ).
- Full pipeline: quality control [FastQC v0.12.1, Trimmomatic] -> read trimming [FastQC v0.12.1, SPAdes v3.15.5, Trimmomatic]

### Amoebozoan testate amoebae illuminate the diversity of heterotrophs and the complexity of ecosystems throughout geological time. (PNAS 2024)

- DOI: 10.1073/pnas.2319628121 | PMCID: PMC11287125 | PMID: 39012821
- Version used: **0.36**
- Evidence: We trimmed primers, adaptors, and low-quality bases from raw Illumina reads using Trimmomatic v.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RAxML v8.2.12] -> stage not stated [BUSCO v5.3.2, IQ-TREE]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: For both experiments, reads were trimmed of adapter sequences and low-quality bases with Trimmomatic ( 37 ) and mapped to a hybrid reference genome of human and Influenza A/California/07/2009 or Influenza A/California/04/2009 (accession nos.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **0.38**
- Evidence: Adapter removal from raw sequencing data was performed using Trimmomatic v0.38 ( 41 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Version used: **0.36**
- Evidence: Adaptor contamination and low-quality reads were removed from fastq files with Trimmomatic 0.36 ( 54 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### Teleost <i>Hox</i> code defines regional identities competent for the formation of dorsal and anal fins. (PNAS 2024)

- DOI: 10.1073/pnas.2403809121 | PMCID: PMC11194558 | PMID: 38861596
- Evidence: Raw sequence reads were cleaned using Trimmomatic ( 58 ) by trimming adapter sequences and low-quality ends (quality score, <30) and manually assembled.
- Full pipeline: read trimming [Trimmomatic]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Version used: **0.38**
- Evidence: Trimmomatic v0.38 ( 89 ) was used to perform adapter removal, quality trimming, and length trimming with default parameters, and trimmed reads were evaluated by FastQC v0.11.8 ( 90 ).
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### Transgenerational increases in DNA methylation in Arabidopsis plants defective in active DNA demethylation. (PNAS 2024)

- DOI: 10.1073/pnas.2320468121 | PMCID: PMC11145202 | PMID: 38768356
- Evidence: For data analysis, low base quality reads were trimmed using Trimmomatic ( 24 ) with parameter “LEADING:20 TRAILING:20 SLIDINGWINDOW:4:15 MINLEN:50.” The remaining high-quality sequences were mapped to Arabidopsis reference genome using BSMAP ( 25 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [R]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Evidence: We performed sequence trimming, adapter removal, and quality filtering with Trimmomatic ( 71 ) on demultiplexed reads from whole genomes of 36 giant hummingbirds.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Decorin suppresses tumor lymphangiogenesis: A mechanism to curtail cancer progression. (PNAS 2024)

- DOI: 10.1073/pnas.2317760121 | PMCID: PMC11067011 | PMID: 38652741
- Version used: **0.36**
- Evidence: Trimmomatic v.0.36 was used for adapter trimming.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2]

### Carbon starvation raises capacities in bacterial antibiotic resistance and viral auxiliary carbon metabolism in soils. (PNAS 2024)

- DOI: 10.1073/pnas.2318160121 | PMCID: PMC11032446 | PMID: 38598339
- Version used: **0.38**
- Evidence: Low-quality reads and adapter sequences were filtered out using Trimmomatic v0.38 (adaptor trimming, average quality = 20), yielding ~733 GB of clean data.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [BLAST v2.5.0] -> stage not stated [HMMER]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Evidence: Sequence quality was assessed using FastQC v 0.11.2 ( 95 ), and quality trimming was done using Trimmomatic ( 96 ) with parameters TRAILING:30 MINLEN:20.
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Aerosolization of viable <i>Mycobacterium tuberculosis</i> bacilli by tuberculosis clinic attendees independent of sputum-Xpert Ultra status. (PNAS 2024)

- DOI: 10.1073/pnas.2314813121 | PMCID: PMC10962937 | PMID: 38470917
- Version used: **0.39**
- Evidence: Briefly, reads were trimmed using Trimmomatic v0.39 ( 60 ) with a sliding window of 5:20, and retaining reads with a minimum length of 20 was used to trim reads.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard v2.9.1, SAMtools v1.5] -> differential/statistical testing [R] -> structure determination [Picard v2.9.1, SAMtools v1.5] -> stage not stated [Kraken2]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: Raw reads were trimmed using Trimmomatic ( 44 ) and quality control was performed using fastqc ( 45 ) to eliminate low-quality reads and adaptors.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Version used: **0.39**
- Evidence: Paired sequencing reads from each library were quality controlled using FastQC (v0.11.9) before being trimmed using Trimmomatic (v0.39), which retains only paired-end reads without adapters and with a phred score greater than 15 in a 4-base sliding window.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Version used: **0.40**
- Evidence: Raw reads were trimmed using Trimmomatic ver.
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### A recent gibbon ape leukemia virus germline integration in a rodent from New Guinea. (PNAS 2024)

- DOI: 10.1073/pnas.2220392121 | PMCID: PMC10861895 | PMID: 38305758
- Version used: **0.27**
- Evidence: The raw sequencing reads were demultiplexed, adaptor sequences, low-quality reads (quality cutoff 20 and minimum read length of 30 nt), and duplicates were removed and merged using Cutadapt v1.15 ( 44 ), Trimmomatic v0.27 ( 45 ), Picard v1.4 ( http://broadinstitute.github.io/picard ), and BBMerge ( 46 ), respectively.
- Full pipeline: read trimming [Cutadapt v1.15, Picard v1.4, Trimmomatic v0.27] -> alignment/mapping [PyMOL v2.4] -> differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7] -> stage not stated [QGIS v3.16.10, RAxML v8.2.11]

### High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310854121 | PMCID: PMC10823218 | PMID: 38241433
- Evidence: After sequencing, adaptor sequences were trimmed using Trimmomatic ( 46 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, Python] -> simulation/modelling [GROMACS, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [BEDTools, SAMtools]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Version used: **0.38**
- Evidence: Reads from six libraries, representing duplicates for each condition (mock, A-485-treated, dCBP-1-treated), were trimmed by Trimmomatic v.0.38 with default setting for paired-end reads, followed by alignment with STAR v.2.7.10b using human genome reference GRCh38.p14.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### A metabolic cell death program downstream of SARM1 couples NAD&lt;sup&gt;+&lt;/sup&gt; depletion to BAX activation and APAF1 degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2522444122 | PMCID: PMC12718333 | PMID: 41364765
- Evidence: In the first step, low-quality reads and those shorter than 36 bp were removed using Trimmomatic with the following command: “java -jar trimmomatic-0.39.jar SE -threads 8 xxx.R1.fastq.gz xxx_0.fastq.gz ILLΜMINACLIP: Genetrap_adapter.fa:2:30:10 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36.” Next, the 5′ common primer sequence of the Gene trap was trimmed using Cutadapt with the command: “cutadapt -j 8 -...
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, Trimmomatic] -> quantification [featureCounts] -> stage not stated [RSEM]

### Ace2 safeguards embryonic hematopoietic stem and progenitor cell production by restraining Nlrp3-mediated pyroptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2515641122 | PMCID: PMC12704739 | PMID: 41348733
- Version used: **0.39**
- Evidence: Then, the original RNA-seq reads used Trimmomatic (v0.39) to filter low-quality reads and trim the linker sequence.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.1.0] -> quantification [StringTie v1.3.3b] -> dimensionality reduction/clustering [clusterProfiler v4.6.1] -> differential/statistical testing [DESeq2 v1.10.1, R v3.2.3] -> stage not stated [GSEA, ImageJ]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Version used: **0.39**
- Evidence: For gene expression quantification, adapter sequences and low-quality bases (Phred quality score < 20) were removed using Trimmomatic (v0.39) ( 71 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### An AINTEGUMENTA phosphoswitch controls bilateral stem cell activity during secondary growth. (PNAS 2025)

- DOI: 10.1073/pnas.2510538122 | PMCID: PMC12663975 | PMID: 41264254
- Evidence: Adaptors were removed with Trimmomatic using default parameters, and read quality was assessed with FastQC.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> quantification [R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3, emmeans] -> stage not stated [Galaxy, ggplot2 v3.4.3]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Version used: **0.39**
- Evidence: Adapter sequences were trimmed using Trimmomatic v0.39 ( 80 ), and the processed reads were mapped to the reference genome using HISAT2 v2.2.1 ( 81 ).
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### Genome-wide strand-specific UV mutagenesis in &lt;i&gt;&lt;i&gt;Escherichia coli&lt;/i&gt;&lt;/i&gt; is directed by the Mfd translocase. (PNAS 2025)

- DOI: 10.1073/pnas.2523368122 | PMCID: PMC12646321 | PMID: 41231941
- Evidence: Paired-end reads were downloaded using fasterq-dump and quality-trimmed with Trimmomatic ( 28 ), applying adapter removal and quality filters with the following parameters: ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36.
- Full pipeline: read trimming [STAR v2.7, Trimmomatic] -> alignment/mapping [SAMtools, STAR v2.7] -> normalisation [deepTools] -> stage not stated [Conda, Snakemake]

### Symbiotic solutions for colony nutrition: Conserved nitrogen recycling within the bacterial pouch of &lt;i&gt;Tetraponera&lt;/i&gt; ants. (PNAS 2025)

- DOI: 10.1073/pnas.2514882122 | PMCID: PMC12595465 | PMID: 41150726
- Evidence: Quality trimming of raw reads was done with Trimmomatic-0.39 ( 70 ), followed by read quality checks using FastQC v0.11.9 ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic] -> read trimming [FastQC v0.11.9, Trimmomatic] -> differential/statistical testing [QUAST] -> stage not stated [BLAST, Flye v2.9, RAxML v8.2.12]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **0.39**
- Evidence: Raw sequencing data were subjected to quality control using Trimmomatic (v.0.39) ( 49 ), and the reads were then sequentially mapped to the Escherichia coli reference with bowtie2 (v.2.5.1) ( 50 ).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **0.39**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **0.38**
- Evidence: Low-quality reads and adapters were removed with Trimmomatic v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Neuronal plasticity at puberty in mouse hypothalamic &lt;i&gt;Kiss1&lt;/i&gt; neurons that control fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2512855122 | PMCID: PMC12582290 | PMID: 41118223
- Version used: **0.38**
- Evidence: Trimmomatic 0.38 and Cutadapt were used to remove low-quality reads and adapter sequences, respectively, and remaining reads were mapped to the Ensembl mm107 mouse reference genome using STAR (v 2.7.9a).
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Version used: **0.39**
- Evidence: We trimmed raw reads of Illumina adapters using Trimmomatic v0.39 ( 74 ) by specifying a “ILLUMINACLIP” parameter of “2:30:10:8:TRUE” and requiring a resulting minimum read length of 36 bp.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### &lt;i&gt;WUSCHEL-D1&lt;/i&gt; upregulation enhances grain number by inducing formation of multiovary-producing florets in wheat. (PNAS 2025)

- DOI: 10.1073/pnas.2510889122 | PMCID: PMC12557809 | PMID: 41086219
- Version used: **0.39**
- Evidence: RNA-seq reads had adaptors trimmed and low-quality reads removed using Trimmomatic v.0.39.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [minimap2] -> stage not stated [BUSCO, Python, hifiasm]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Version used: **0.39**
- Evidence: We used the program Trimmomatic 0.39 ( 63 ) to trim the sequence data to remove Illumina adapter sequences and polyG tails using a sliding window approach (SLIDINGWINDOW:4:20).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Evolution under vancomycin selection drives divergent collateral sensitivity patterns in &lt;i&gt;Staphylococcus aureus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507962122 | PMCID: PMC12501141 | PMID: 40996798
- Version used: **0.39**
- Evidence: The sequencing reads were filtered to remove low-quality bases using Trimmomatic v0.39 ( 74 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> differential/statistical testing [R]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Evidence: Raw FASTQ files were processed with the Sekaly lab pipeline on the Emory AWS platform: After sequencing, reads are processed to remove Illumina adapters and low-quality 3′-end bases using the Trimmomatic software ( 38 ), and then mapped to the reference human genome version GRCh38 using the RNA-seq optimized software STAR ( 39 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### Inverse stable isotope probing-metabolomics (InverSIP) identifies an iron acquisition system in a methane-oxidizing bacterial community. (PNAS 2025)

- DOI: 10.1073/pnas.2507323122 | PMCID: PMC12435222 | PMID: 40901884
- Evidence: Raw metagenomic reads were trimmed using Trimmomatic ( 51 ) and were assembled using the --meta mode of SPAdes v4.0.0 ( 52 ).
- Full pipeline: read trimming [SPAdes v4.0.0, Trimmomatic] -> alignment/mapping [Python]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Version used: **0.26**
- Evidence: Clean reads were obtained using Trimmomatic (v.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### De novo rates of a &lt;i&gt;Trypanosoma&lt;/i&gt;-resistant mutation in two human populations. (PNAS 2025)

- DOI: 10.1073/pnas.2424538122 | PMCID: PMC12415191 | PMID: 40854136
- Evidence: Merged sequences were trimmed from Illumina adapters using Cutadapt ( 105 ) and quality-filtered by Trimmomatic ( 106 ), using a sliding window size of 3 bp, a Phred quality threshold of 30 and a minimum read length threshold of 90 bp.
- Full pipeline: read trimming [Cutadapt, Trimmomatic] -> alignment/mapping [BWA]

### Synergistic action of specialized metabolites from divergent biosynthesis in the human oral microbiome. (PNAS 2025)

- DOI: 10.1073/pnas.2504492122 | PMCID: PMC12403116 | PMID: 40828023
- Evidence: Low-quality sequences were then trimmed from the raw Illumina reads with Trimmomatic ( 64 ).
- Full pipeline: read trimming [Trimmomatic] -> stage not stated [BWA, DESeq2]

### Evolutionarily divergent nidovirus with an exceptionally large genome identified in Pacific oysters undergoing mass mortality. (PNAS 2025)

- DOI: 10.1073/pnas.2426923122 | PMCID: PMC12377751 | PMID: 40758866
- Version used: **0.38**
- Evidence: Raw reads for RNA-Seq samples were quality-controlled and trimmed using Trimmomatic v.0.38 ( 94 ), followed by de novo assembly using SPAdes v.3.15.2 ( 95 ) and MEGAHIT v.1.2.9 ( 96 ), respectively ( SI Appendix , Extended Materials and Methods ).
- Full pipeline: read trimming [MAFFT, SPAdes v3.15.2, Trimmomatic v0.38] -> alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2.1] -> structure determination [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0.3, InterProScan v5.59]

### Deficiency in transmitter release triggers homeostatic transcriptional changes that increase presynaptic excitability. (PNAS 2025)

- DOI: 10.1073/pnas.2322714122 | PMCID: PMC12337328 | PMID: 40729383
- Version used: **0.38**
- Evidence: As described recently ( 71 ), demultiplexed .fastq files were first analyzed with FastQC (ver 0.11.7) ( 79 ) to check for quality and trimmed with Trimmomatic (ver 0.38) ( 80 ).
- Full pipeline: quality control [FastQC v0.11.7, Trimmomatic v0.38] -> read trimming [FastQC v0.11.7, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0, featureCounts] -> normalisation [DESeq2 v1.26.0] -> visualisation [ggplot2 v3.2.1] -> stage not stated [R v4.1.0]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Evidence: We used Trimmomatic-0.39 to remove adapters (ILLUMINACLIP:TruSeq3-PE.fa:2:30:10), trim leading and trailing low quality or N bases (below quality 3) (LEADING:3, TRAILING:3) or when the average quality per base drops below 15 in a 4-base sliding window (SLIDINGWINDOW:4:15), and drop reads <75 bp in length (MINLEN:75).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### A trans-species cytoplasmic polymorphism is associated with seed shape and aridity across multiple species of sunflowers. (PNAS 2025)

- DOI: 10.1073/pnas.2410943122 | PMCID: PMC12337292 | PMID: 40720659
- Version used: **0.22**
- Evidence: For each sample, raw data were trimmed using Trimmomatic (v0.22) ( 85 ), and aligned to only the chloroplast and mitochondrial genomes of Helianthus annuus (NCBI KF815390.1 & DQ383815.1 ) using NextGenMap (v0.5.5) ( 86 ).
- Full pipeline: read trimming [Trimmomatic v0.22] -> alignment/mapping [Trimmomatic v0.22] -> variant calling [GATK] -> stage not stated [BCFtools v1.10.2, IQ-TREE, SAMtools v1.10]

### A preclinical pig model of Angelman syndrome mirrors the early developmental trajectory of the human condition. (PNAS 2025)

- DOI: 10.1073/pnas.2505152122 | PMCID: PMC12318228 | PMID: 40690672
- Version used: **0.39**
- Evidence: Raw sequencing reads were quality-filtered using Trimmomatic v0.39, and alignments were generated for each sample following the GATK v3 Best Practices Workflow ( 67 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.39] -> alignment/mapping [GATK, Trimmomatic v0.39] -> stage not stated [IQ-TREE]

### Complementary genetic and epigenetic changes facilitate rapid adaptation to multiple global change stressors. (PNAS 2025)

- DOI: 10.1073/pnas.2422782122 | PMCID: PMC12305003 | PMID: 40663607
- Version used: **0.36**
- Evidence: Raw reads were trimmed with Trimmomatic v0.36 for quality and adapter contamination.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bismark v0.22.3, Bowtie2 v2.2.6] -> differential/statistical testing [R v3.6.0, edgeR] -> stage not stated [BEDTools, DESeq2]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Version used: **0.39**
- Evidence: Reads were trimmed and quality filtered using Trimmomatic (version 0.39) with default settings.
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Version used: **0.32**
- Evidence: For the nine modern samples, we first trimmed the sequencing adapters from the raw reads using Trimmomatic v0.32 and mapped them to the MITObim-reconstructed mitogenome using BWA mem ( 63 ).
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: We then trimmed adaptor sequences and low-quality read regions using the Trimmomatic software (version 0.4).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: After cleaning the row reads with Trimmomatic ( 57 ), reads were mapped to hg38 by STAR.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Longitudinal sequencing reveals polygenic and epistatic nature of genomic response to selection. (PNAS 2025)

- DOI: 10.1073/pnas.2410452122 | PMCID: PMC12207516 | PMID: 40531879
- Version used: **0.32**
- Evidence: Raw RNA-seq reads were trimmed to remove low quality bases, adapter sequences, and to exclude posttrimmed reads shorter than 20 nt using Trimmomatic 0.32 ( 59 ) and the following parameters: SE ILLUMINACLIP:1:30:7 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:20.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA, Picard] -> variant calling [DESeq2] -> dimensionality reduction/clustering [PLINK] -> stage not stated [R, emmeans]

### Concerted transport and phosphorylation of diacylglycerol at ER-PM contact sites regulate phospholipid dynamics during stress. (PNAS 2025)

- DOI: 10.1073/pnas.2421334122 | PMCID: PMC12167946 | PMID: 40455983
- Version used: **0.36**
- Evidence: The reads were quality-filtered and trimmed using Trimmomatic version 0.36 ( 83 ) with default paired-end mode options.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Clustal Omega, Cufflinks v2.2.1, R] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [AlphaFold, ilastik]

### Allelic variations and gene cluster modularity act as nonlinear bottlenecks for cholera emergence. (PNAS 2025)

- DOI: 10.1073/pnas.2417915122 | PMCID: PMC12146696 | PMID: 40434643
- Version used: **0.36**
- Evidence: Reads were trimmed using Trimmomatic v0.36 ( 77 ) and assembled de novo with SPAdes version 3.11.1 ( 78 ).
- Full pipeline: read trimming [SPAdes v3.11.1, Trimmomatic v0.36]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Version used: **0.39**
- Evidence: Raw Norwegian sequences were trimmed using Trimmomatic v.0.39 ( 103 ), using the settings clip = 100, headclip = 5.
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Version used: **0.36**
- Evidence: Raw sequence reads were trimmed using Trimmomatic v.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Evidence: Raw reads were filtered using Trimmomatic and aligned to the reference genome using STAR v2.11a, allowing for multimapping reads targeting up to 100 loci ( 79 , 80 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Version used: **0.36**
- Evidence: We removed adapter contaminations and trimmed the sequencing reads using Trimmomatic (v.0.36; 61 ) with the following parameters: ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 |LEADING:3 |TRAILING:3 |SLIDINGWINDOW:4:15 |MINLEN:36.
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **0.39**
- Evidence: Raw metagenomic sequences were trimmed using Trimmomatic v0.39 ( 40 ) with specific parameters (ILLUMINACLIP:2:30:10, LEADING:3, SLIDINGWINDOW:4:15, MINLEN:36) before assembly using MetaSPAdes v3.13.0 ( 41 ) with default settings.
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Version used: **0.39**
- Evidence: Raw RNA-seq reads were processed using Trimmomatic (v0.39) ( 78 ) for quality trimming and subsequently mapped to their respective genomes with HISAT2 (v.2.2.1) ( 79 ).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Version used: **0.39**
- Evidence: Raw reads were first quality filtered and trimmed using Trimmomatic v0.39 ( 137 ) with the following parameters: ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 MINLEN:35 SLIDINGWINDOW:4:15.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Version used: **0.3.9**
- Evidence: After a quality check with Fastqc (v0.11.8) ( 84 ) and a trimming step with Trimmomatic (v0.3.9) ( 85 ), only reads with a phred > 28 and a minimum length of 70 bp were retained.
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Version used: **0.39**
- Evidence: Short read quality was assessed using FastQC v0.11.9 ( 76 ) and reads were trimmed using Trimmomatic v0.39 ( 77 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Version used: **0.39**
- Evidence: To ensure high-quality sequences for mapping and downstream analyses, low-quality reads and an adapter were trimmed using Trimmomatic v.0.39 ( 67 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### INDETERMINATE DOMAIN-DELLA protein interactions orchestrate gibberellin-mediated cell elongation in wheat and barley. (PNAS 2026)

- DOI: 10.1073/pnas.2528934123 | PMCID: PMC12867750 | PMID: 41615756
- Version used: **0.39**
- Evidence: Sequencing reads were trimmed for quality and adapter sequences using Trimmomatic 0.39 (parameters SLIDINGWINDOW:4:20; MINLEN:50) ( 49 ), then aligned and quantified using Kallisto against the IWGSC RefSeq v1.2 annotated gene models ( 47 , 50 ).
- Full pipeline: read trimming [Trimmomatic v0.39, kallisto] -> alignment/mapping [Bowtie2, Trimmomatic v0.39, kallisto] -> quantification [Trimmomatic v0.39, kallisto] -> stage not stated [BLAST, ImageJ v1.48v]

### Germline fate determination by a single ARGONAUTE protein in &lt;i&gt;Ectocarpus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518712123 | PMCID: PMC12867755 | PMID: 41604268
- Evidence: Raw reads were processed using Trimmomatic ( 89 ) for quality control and adapter removal.
- Full pipeline: quality control [Trimmomatic] -> read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT, STAR, featureCounts] -> quantification [DESeq2, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Early life-stage thermal resilience is determined by climate-linked regulatory variation. (PNAS 2026)

- DOI: 10.1073/pnas.2518358123 | PMCID: PMC12799179 | PMID: 41505517
- Version used: **0.38**
- Evidence: 0.11.7) ( 118 ) and trimmed the forward and reverse reads using Trimmomatic (v.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Salmon v0.14.1] -> quantification [Salmon v0.14.1] -> stage not stated [DESeq2, R, SAMtools v1.10]

### Combination antiviral and anti-inflammatory therapy mitigates persistent neurological deficits in mice post SARS-CoV-2 infection. (PNAS 2026)

- DOI: 10.1073/pnas.2530209123 | PMCID: PMC12799161 | PMID: 41499397
- Version used: **0.33**
- Evidence: 2 × 50 bp FastQ paired end reads for 8 samples (n = 39.6 Million average reads per sample) were trimmed using Trimmomatic (v 0.33) enabled with the optional “-q” option; 3 bp sliding-window trimming from 3′ end requiring minimum Q3Quality control on raw sequence data for each sample were performed with FastQC.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.5, Seurat v5.3.0, pheatmap]

### Host-microbiome mutualism drives urea carbon salvage and acetogenesis during hibernation. (PNAS 2026)

- DOI: 10.1073/pnas.2518978123 | PMCID: PMC12773770 | PMID: 41481471
- Version used: **0.38**
- Evidence: Trimmomatic v0.38 ( 9 ) was used to remove sequencing adapters and low-quality reads, while host DNA was filtered using bowtie2 v2.2.2 ( 10 ) against the 13-lined ground squirrel genome (GenBank and RefSeq assembly accession = GCA_000236235.1).
- Full pipeline: read trimming [Bowtie2 v2.2.2, Trimmomatic v0.38] -> normalisation [DESeq2, R] -> differential/statistical testing [R] -> stage not stated [HMMER]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Version used: **0.36**
- Evidence: Remaining reads, composed of viral and unclassified reads, were trimmed in two stages: first to remove the random hexamer primers from the forward read and SMARTer TSO from the reverse read, and then to remove Illumina adapter sequences using Trimmomatic version 0.36 ( 56 ), with the ILLUMINACLIP options set to 2:10:7:1:true MINLEN:80.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Version used: **0.39**
- Evidence: Briefly, reads were trimmed using Trimmomatic version 0.39 (settings TruSeq3-PE-2.fa:2:30:10, minlen 50), and aligned using bwa (“bwa mem,” options −5SP -T0, version 0.7.17-r1198-dirty) to mm10 (GRCm38) genome reference or hg38 (GRCh38) reference( 57 , 58 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

