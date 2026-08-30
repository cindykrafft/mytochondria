# Galaxy

- **Category:** workflow
- **Papers in survey:** 21
- **Journals:** PNAS (12), Nature (7), Science (1), Cell (1)
- **Years:** 2021 (3), 2022 (5), 2023 (2), 2024 (4), 2025 (7)
- **Versions named:** 2.11.40.7 (1), 24.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), read trimming (2), visualisation (1), quality control (1), quantification (1)

## Papers

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: 1072534 Software and algorithms Galaxy platform Afgan et al., 2016 N/A Deeptools Ramírez et al., 2016 N/A STAR Dobin et al., 2013 N/A FeatureCounts Liao et al., 2014 N/A DESeq2 Love et al., 2014 N/A Morpheus Broad Institute N/A DAVID Huang et al., 2009 N/A Trimmomatic Bolger et al., 2014 N/A Bowtie2 Langmead and Salzberg, 2012 N/A SAM tools Li et al., 2009 N/A MACS2 Zhang et al., 2008 N/A Bedtools...
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: All major components of the current pipeline developed here are available on the Galaxy platform, and in modular form with different steps that can be optionally performed ( https://assembly.usegalaxy.eu/ ) 56 .
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Evidence: Reads were processed using workflows managed on the Galaxy platform.
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### Stress response silencing by an E3 ligase mutated in neurodegeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06985-7 | PMCID: PMC10881396 | PMID: 38297121
- Version used: **2.11.40.7**
- Evidence: 52 ) ran on the Galaxy server (Galaxy v.2.11.40.7) 53 using the WT sgCNTRL as control for all samples.
- Full pipeline: alignment/mapping [kallisto v0.48.0] -> quantification [kallisto v0.48.0] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, Cytoscape, Galaxy v2.11.40.7]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: Mass spectrometry data processing Raw data were converted to mzXML format using msconvert (v3.0.19052.1) from the Galaxy platform 72 .
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Evidence: Transcriptomes were analysed on the Galaxy platform 59 using Trim Galore! version 0.4.3.1 (developed by Felix Krueger at the Babraham Institute), HISAT2 version 2.1.0 60 and featureCounts version 1.6.1.0 61 . snRNA-seq of thymic tissue The Chromium GEM-X Single Cell 3′ v4 protocol ( CG000731 , Rev B) was followed starting from step 1.1 according to the manufacturer’s guidelines.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: For this step, we used the phylogenetically closest species available on the Galaxy server: Fusarium (orthoDB v.10).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Stepwise ATP translocation into the endoplasmic reticulum by human SLC35B1. (Nature 2025)

- DOI: 10.1038/s41586-025-09069-w | PMCID: PMC12267056 | PMID: 40399679
- Evidence: The data analysis was performed on the Galaxy platform 53 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, Galaxy, PyMOL]

### Amino acids activate mTORC1 to release roe deer embryos from decelerated proliferation during diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2100500118 | PMCID: PMC8536382 | PMID: 34452997
- Evidence: All FastQ files were analyzed on a local Galaxy server ( 59 ).
- Full pipeline: quality control [FastQC, MultiQC] -> differential/statistical testing [FastQC, MultiQC, R] -> stage not stated [Galaxy, Trim Galore]

### Fever supports CD8<sup>+</sup> effector T cell responses by promoting mitochondrial translation. (PNAS 2021)

- DOI: 10.1073/pnas.2023752118 | PMCID: PMC8237659 | PMID: 34161266
- Evidence: Sequenced libraries were processed with the Galaxy platform and deepTools for quality control ( 37 ), Spliced Transcripts Alignment to a Reference (STAR) ( 38 ) for trimming and mapping, and featureCounts ( 39 ) to quantify mapped reads.
- Full pipeline: quality control [Galaxy, deepTools, featureCounts] -> read trimming [Galaxy, deepTools, featureCounts] -> alignment/mapping [DESeq2, Galaxy, R, deepTools, featureCounts] -> quantification [DESeq2, Galaxy, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [ImageJ, Metascape]

### TGFB2-AS1 inhibits triple-negative breast cancer progression via interaction with SMARCA4 and regulating its targets <i>TGFB2</i> and <i>SOX2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2117988119 | PMCID: PMC9522332 | PMID: 36126099
- Evidence: Metagene profile plots and heat maps were generated from the Galaxy platform using deepTools2 version 3.3.0 ( 59 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5] -> stage not stated [GSEA, Galaxy, MACS2 v2.1.2]

### A scalable framework for the discovery of functional helicase substrates and helicase-driven regulatory switches. (PNAS 2022)

- DOI: 10.1073/pnas.2209608119 | PMCID: PMC9499579 | PMID: 36095194
- Evidence: Bioinformatics analyses were performed with in-house Python scripts and software tools from the Galaxy server ( 45 ).
- Full pipeline: quality control [Cutadapt v1.15, FastQC v0.11.5] -> read trimming [Cutadapt v1.15, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [Galaxy, MACS2, Python]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Evidence: Bioinformatic tools on the Galaxy platform were used to assess read quality, align reads, and call SNPs and indels.
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Evidence: The Galaxy platform [ https://usegalaxy.org/ , ( 78 )] was used to process the whole genome sequencing data.
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: The Galaxy platform ( 36 ) was used for the analysis unless otherwise specified.
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: ChIP-seq data in fastq format were downloaded from SRA and extracted with fastq-dump (v2.9.1) to the Galaxy platform and the public server at usegalaxy.org was used to further process the data.
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles up-regulate and directly transfer adherence factors promoting host cell colonization. (PNAS 2024)

- DOI: 10.1073/pnas.2401159121 | PMCID: PMC11194581 | PMID: 38865261
- Evidence: Raw data were processed using MaxQuant ( 77 ) and MSstats ( 78 ) on the Galaxy server ( https://usegalaxy.org/ ).
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [Galaxy]

### An AINTEGUMENTA phosphoswitch controls bilateral stem cell activity during secondary growth. (PNAS 2025)

- DOI: 10.1073/pnas.2510538122 | PMCID: PMC12663975 | PMID: 41264254
- Evidence: The analysis of the data was performed using the Galaxy platform ( https://usegalaxy.eu/ ) ( 71 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> quantification [R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3, emmeans] -> stage not stated [Galaxy, ggplot2 v3.4.3]

### Bidirectional disruption of &lt;i&gt;GNAS&lt;/i&gt; transcripts causes broad methylation defects in pseudohypoparathyroidism type 1B. (PNAS 2025)

- DOI: 10.1073/pnas.2423271122 | PMCID: PMC12037034 | PMID: 40249781
- Version used: **24.2**
- Evidence: After removing the adaptor sequences on the Galaxy server 24.2.rc1, using Cutadapt, sequences were aligned to the reference genome (GRCh38) using RNA STAR and visualized on Integrative Genomics Viewer (IGV, Ver2.19.1) ( 8 ).
- Full pipeline: alignment/mapping [Cutadapt, Galaxy v24.2, minimap2] -> visualisation [Cutadapt, Galaxy v24.2]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: CUT&RUN data were analyzed using the Galaxy platform.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Evidence: We then counted how many reads overlapped an annotated gene (GENECODE v32 annotations) using HTSeq (v2.0.2) ( 122 ) (htseq-count –stranded=reverse –order=name -f bam –additional-attr=gene_name -m union), and used the output counts files to find DEGs with DESeq2 ( 123 ), run with default parameters within the Galaxy platform ( 124 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

