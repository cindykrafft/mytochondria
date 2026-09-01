# MetaPhlAn

- **Category:** microbiome
- **Papers in survey:** 11
- **Journals:** Nature (8), PNAS (3)
- **Years:** 2022 (1), 2023 (1), 2024 (2), 2025 (2), 2026 (5)
- **Versions named:** 4.0.6 (2), 4.1 (1), 3.0.7 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), quantification (3)

## Papers

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Evidence: Species-level profiling of metagenomic samples Species-level profiling was performed on all the 9,715 samples with MetaPhlAn 4 (refs.
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Evidence: Taxonomic abundance We estimated the relative abundance of gut microbial species from the cleaned metagenomic reads using Kraken2 (v.2.1.2) 59 in conjunction with Bracken (v.2.6.2) 60 based on the same reference genomes included in the database of SGV-Finder, and MetaPhlAn 3 (ref.
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Gut microbiome strain-sharing within isolated village social networks. (Nature 2025)

- DOI: 10.1038/s41586-024-08222-1 | PMCID: PMC11666459 | PMID: 39567691
- Evidence: Species-level and strain-level profiling Species-level profiling was performed using MetaPhlAn 4 26 using the Jan21 database and default parameters.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> visualisation [igraph v1.3.5] -> stage not stated [MetaPhlAn, R, vegan v2.6]

### Genome-wide sweeps create ecological units in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-026-10476-w | PMCID: PMC13322978 | PMID: 42092154
- Version used: **4.0.6**
- Evidence: Metagenomes were aligned against the MetaPhlAn4 reference database (v.Jan 2022) with MetaPhlAn (v.4.0.6) 23 default settings, and all polymorphic sites with a Phred quality score ≥20 and coverage ≥3 were identified.
- Full pipeline: alignment/mapping [MetaPhlAn v4.0.6] -> differential/statistical testing [ComplexHeatmap v2.12.1, ggplot2 v3.5.1, ggpubr v0.6.0] -> stage not stated [Prokka v1.14.6, R, SciPy]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Version used: **4.0.6**
- Evidence: Unmapped reads were converted to compressed FASTQ with samtools (v.1.15.1) and then used as input for microbiome profiling using MetaPhlAn (v.4.0.6) with the vOct22 reference database.
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **4.1**
- Evidence: Species-level profiling Profiling at the resolution of SGBs was performed with MetaPhlAn (v4.1) 16 , 68 using the vJun23_202307 markers database and using the –unclassified_estimation parameter (Supplementary Table 4 ).
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: These data were processed similarly to Yakut data before running StrainPhlAn4 with default parameters to extract species-specific MetaPhlAn markers.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Evidence: Microbiome taxonomic profiling All microbiome samples from the PREDICT cohorts were profiled using MetaPhlAn 4 (v.4.beta.2, database vJan21_CHOCOPhlAnSGB_202103), without performing read subsampling, as the benefit of occasionally detecting a few additional low-abundance species in samples with a higher number of reads outweighs the potential noise from uneven sequencing depth.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Evidence: MetaPhlAn and StrainPhlAn Analyses.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### Beneficial metabolic effects of PAHSAs depend on the gut microbiota in diet-induced obese mice but not in chow-fed mice. (PNAS 2024)

- DOI: 10.1073/pnas.2318691121 | PMCID: PMC11252816 | PMID: 38968121
- Evidence: The quality-controlled cleaned reads were then categorized for relative abundance using MetaPhlAn embedded in HUMAnN ( 26 ), where they were mapped against microbial marker genes for microbial species and genes for pathway profiling.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, MultiQC] -> alignment/mapping [BLAST, HUMAnN, MetaPhlAn] -> quantification [HUMAnN, MetaPhlAn] -> dimensionality reduction/clustering [BLAST] -> stage not stated [DADA2]

### Loss of sialic acid side-chain &lt;i&gt;O&lt;/i&gt;-acetylation exacerbates colitis. (PNAS 2025)

- DOI: 10.1073/pnas.2505249122 | PMCID: PMC12403103 | PMID: 40828018
- Version used: **3.0.7**
- Evidence: The remaining reads (representing 88 to 97% of the raw reads) were subjected to taxonomic classification of metagenomes using MetaPhlAn (version 3.0.7) ( 61 ).
- Full pipeline: quantification [HUMAnN v3.0.0] -> stage not stated [MetaPhlAn v3.0.7]

