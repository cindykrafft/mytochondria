# Manta

- **Category:** genomics
- **Papers in survey:** 5
- **Journals:** Nature (5)
- **Years:** 2022 (1), 2024 (1), 2025 (2), 2026 (1)
- **Versions named:** 1.6.0 (3), 1.4.0 (1), 0.28.0 (1)
- **Pipeline stages it appears in:** variant calling (1)

## Papers

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **0.28.0**
- Evidence: Structural and copy number variants were called using Manta (v.0.28.0) and Canvas (v.1.3.1) 67 , respectively.
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **1.4.0**
- Evidence: SVs were called using Svaba (v.0.2.1) 61 , Manta (v.1.4.0) 62 and Lumpy (v.0.2.13) 63 , with Svaba used for both indels and SVs.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **1.6.0**
- Evidence: Structural variations were called by Manta (v.1.6.0) applying default settings and SV length >6,000 bp were used for downstream analysis 77 .
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Sequence diversity lost in early pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-025-09031-w | PMCID: PMC12176622 | PMID: 40399685
- Version used: **1.6.0**
- Evidence: CNV breakend annotation with GraphTyper2 We discovered structural variants with Manta (v.1.6.0), merged the variant sites over all individuals with svimmer (git hash 2af9ccf1ac056b9516c25ec4a0121657a9f9ab8e), and finally genotyped them jointly across the entire set with GraphTyper2 (v.2.7.7).
- Full pipeline: alignment/mapping [BWA, Picard, R] -> variant calling [Manta v1.6.0] -> differential/statistical testing [R] -> machine learning [ADMIXTURE] -> stage not stated [PLINK, VEP]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **1.6.0**
- Evidence: The SV callset was also compared against other SV callsets, including public callsets, as well as the 1KCP long-read Sniffles2 callset (jointly called using Sniffles2 (v.2.6.2) 86 ) and the 1KCP short-read callset (generated with Manta (v.1.6.0) 115 and merged using SURVIVOR (v.1.0.6) 116 ) (Supplementary Table 15 ), using Jasmine (v.1.1.5) 87 (--allow_intrasample).
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

