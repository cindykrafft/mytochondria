# HUMAnN

- **Category:** microbiome
- **Papers in survey:** 5
- **Journals:** PNAS (3), Nature (2)
- **Years:** 2023 (1), 2024 (1), 2025 (2), 2026 (1)
- **Versions named:** 3.0 (3), 3.0.0 (1)
- **Pipeline stages it appears in:** quantification (2), read trimming (1), alignment/mapping (1)

## Papers

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **3.0**
- Evidence: Quality-filtered reads were also used as input to HUMAnN v.3.0 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Version used: **3.0**
- Evidence: The sequence data passing the SourceTracker2 filters described above were also subjected to functional analyses using the methodology implemented in HUMAnN 3.0 (ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### Microbiota configuration determines nutritional immune optimization. (PNAS 2023)

- DOI: 10.1073/pnas.2304905120 | PMCID: PMC10710091 | PMID: 38011570
- Version used: **3.0**
- Evidence: These four files were concatenated into a single file for each sample and then analyzed using HUMAnN 3.0 to profile metabolic pathways ( 67 ).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Bowtie2 v2.4.2, HOMER, HUMAnN v3.0, QIIME 2 v2020.2]

### Beneficial metabolic effects of PAHSAs depend on the gut microbiota in diet-induced obese mice but not in chow-fed mice. (PNAS 2024)

- DOI: 10.1073/pnas.2318691121 | PMCID: PMC11252816 | PMID: 38968121
- Evidence: The quality-controlled cleaned reads were then categorized for relative abundance using MetaPhlAn embedded in HUMAnN ( 26 ), where they were mapped against microbial marker genes for microbial species and genes for pathway profiling.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, MultiQC] -> alignment/mapping [BLAST, HUMAnN, MetaPhlAn] -> quantification [HUMAnN, MetaPhlAn] -> dimensionality reduction/clustering [BLAST] -> stage not stated [DADA2]

### Loss of sialic acid side-chain &lt;i&gt;O&lt;/i&gt;-acetylation exacerbates colitis. (PNAS 2025)

- DOI: 10.1073/pnas.2505249122 | PMCID: PMC12403103 | PMID: 40828018
- Version used: **3.0.0**
- Evidence: Functional profiling of metagenomic reads for species-specific and species-agnostic quantification of gene families, enzyme classification modules, and pathways was done by HUMAnN (v3.0.0) ( 62 ) using UniRef and MeraCyc databases.
- Full pipeline: quantification [HUMAnN v3.0.0] -> stage not stated [MetaPhlAn v3.0.7]

