# Bracken

- **Category:** microbiome
- **Papers in survey:** 11
- **Journals:** Nature (6), PNAS (3), Lancet (2)
- **Years:** 2021 (1), 2022 (1), 2023 (2), 2024 (3), 2025 (4)
- **Versions named:** 2.9 (2), 2.6.2 (1)
- **Pipeline stages it appears in:** quantification (5), alignment/mapping (1)

## Papers

### Baricitinib in patients admitted to hospital with COVID-19 (RECOVERY): a randomised, controlled, open-label, platform trial and updated meta-analysis. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)01109-6 | PMCID: PMC9333998 | PMID: 35908569
- Evidence: ...n Bowyer , Aileen Boyd , Jenny Boyd , Laura Boyd , Nicola Boyer , Namoi Boyle , Pauline Boyle , Rosalind Boyle , Louise Boyles , Leanna Brace , Abbey Bracken , Jodie Bradder , Clare J Bradley , Pamela Bradley , Patrick Bradley , Paul Bradley , Joanne Bradley-Potts , Lynne Bradshaw , Zena Bradshaw , Clare Brady , Rebecca Brady , Shirin Brady , Pedro Braga Sardo , Denise Braganza , Megan Braithwaite...
- Full pipeline: stage not stated [Bracken, R v4.0.3]

### Higher dose corticosteroids in patients admitted to hospital with COVID-19 who are hypoxic but not requiring ventilatory support (RECOVERY): a randomised, controlled, open-label, platform trial. (Lancet 2023)

- DOI: 10.1016/s0140-6736(23)00510-x | PMCID: PMC10156147 | PMID: 37060915
- Evidence: ...n Bowyer , Aileen Boyd , Jenny Boyd , Laura Boyd , Nicola Boyer , Namoi Boyle , Pauline Boyle , Rosalind Boyle , Louise Boyles , Leanna Brace , Abbey Bracken , Jodie Bradder , Clare J Bradley , Pamela Bradley , Patrick Bradley , Paul Bradley , Joanne Bradley-Potts , Lynne Bradshaw , Zena Bradshaw , Clare Brady , Rebecca Brady , Shirin Brady , Pedro Braga Sardo , Denise Braganza , Megan Braithwaite...
- Full pipeline: stage not stated [Bracken, R v4.0.3]

### Synergy and oxygen adaptation for development of next-generation probiotics. (Nature 2023)

- DOI: 10.1038/s41586-023-06378-w | PMCID: PMC10412450 | PMID: 37532933
- Evidence: Estimations of strain abundances were obtained using Bracken 55 (v2.6.2) for reads with minimum length of 100 bp.
- Full pipeline: alignment/mapping [Kraken2] -> quantification [Bracken] -> differential/statistical testing [R, vegan] -> stage not stated [Bowtie2 v2.3.5.1, Prokka v1.14.5, SPAdes v3.13.0]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Evidence: Fastq reads were then filtered by size and quality using Nanofilt 55 and classified using Kraken (v2.1.0) 56 followed by Bracken 57 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Version used: **2.6.2**
- Evidence: Taxonomic abundance We estimated the relative abundance of gut microbial species from the cleaned metagenomic reads using Kraken2 (v.2.1.2) 59 in conjunction with Bracken (v.2.6.2) 60 based on the same reference genomes included in the database of SGV-Finder, and MetaPhlAn 3 (ref.
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: We complemented these MAG assignments using Kraken2 46 (v.2.0.8) and Bracken 47 (v.2.5) and a Kraken2-compatible version of the GTDB reference.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **2.9**
- Evidence: Then, clean reads were taxonomically classified using Kraken2 (v.2.1.3) 73 and Bracken (v.2.9) 74 against a GTDB-formatted database based on the Unified Human Gut Genome catalogue 75 (available at http://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0.2/ ).
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **2.9**
- Evidence: Quantification of species abundances based on metagenome sequencing data Taxonomic profiling using metagenome sequencing data was performed through read-level taxonomic assignment with Kraken2 (v.2.1.3) 69 , followed by estimation of relative abundances using Bracken (v.2.9) 70 .
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: The Kraken output was used to estimate read abundances for each species with Bracken ( 73 ).
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Evidence: Bracken was used to quantify species level abundances, and a custom python script was used for formatting.
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### Exposure and health risks of livestock air resistomes. (PNAS 2025)

- DOI: 10.1073/pnas.2403866122 | PMCID: PMC12067279 | PMID: 40294268
- Evidence: Microbial composition in metagenomic data was analyzed using Kraken2 ( 46 ) with standard plus database and re-estimated with Bracken ( 47 ).
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [Bracken, Kraken2, QIIME 2 v2020.11]

