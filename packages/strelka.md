# Strelka

- **Category:** genomics
- **Papers in survey:** 20
- **Journals:** Nature (15), PNAS (3), Science (1), Cell (1)
- **Years:** 2021 (2), 2022 (4), 2023 (5), 2024 (3), 2025 (4), 2026 (2)
- **Versions named:** 2.9.10 (4), 2.4.7 (3), 1.0.15 (2), 2.0.15 (1), 2.8.2 (1), 2.9.2 (1)
- **Pipeline stages it appears in:** variant calling (3), alignment/mapping (2), registration (1), normalisation (1)

## Papers

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Evidence: Variant calling was performed using both Strelka (Illumina) and MuTect (The Broad Institute) by comparing each patient’s tumor DNA to a normal reference (same patient’s PBMC DNA).
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: In brief, variants from whole-genome sequencing data were called using four independent callers: GATK v3.8, FreeBayes, Strelka, and Platypus.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Version used: **2.8.2**
- Evidence: We also used Strelka (version 2.8.2) with default parameter settings to identify somatic SNVs and indels 42 .
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: SNVs were called with MutationSeq 46 (probability threshold = 0.9) and Strelka 47 .
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Version used: **2.4.7**
- Evidence: Detecting cancer SNVs, indels and structural variants Read alignment against human reference genome GRCh38-Decoy+EBV was performed with ISAAC (version iSAAC-03.16.02.19) 70 , SNVs and short insertions–deletions (indels) variant calling together with tumour − normal subtraction was performed using Strelka (version 2.4.7) 71 .
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **2.4.7**
- Evidence: Single-nucleotide variants (SNVs) and indels were called using Strelka v.2.4.7 using somatic calling mode.
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **2.9.10**
- Evidence: Somatic mutation calling using bulk data Somatic mutations were called from WES using the Somaticwrapper pipeline v.1.6 ( https://github.com/ding-lab/somaticwrapper ), which includes four different callers, that is, Strelka (v.2.9.10) 56 , MUTECT (v.1.1.7) 57 , VarScan (v.2.3.8) 58 and Pindel (v.0.2.5) 59 .
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Somatic variant calling on tumour and its matched normal BAM file was performed using Strelka 33 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Version used: **1.0.15**
- Evidence: MuTect 1.1.7 and Strelka 1.0.15 were used to call SNV and indels on pre-processed sequencing data.
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### Extrachromosomal DNA in the cancerous transformation of Barrett's oesophagus. (Nature 2023)

- DOI: 10.1038/s41586-023-05937-5 | PMCID: PMC10132967 | PMID: 37046089
- Version used: **2.0.15**
- Evidence: For the Cambridge cohort, TP53 status was determined by identifying somatic coding variants (missense, frameshift, stop-gain or splice-site variants), using Strelka v.2.0.15 (ref.
- Full pipeline: alignment/mapping [BWA] -> registration [GATK] -> differential/statistical testing [SciPy v1.9.1] -> stage not stated [Strelka v2.0.15, VEP]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Version used: **2.9.10**
- Evidence: Mutation calling using WES Somatic mutations were called from WES data using the Somaticwrapper pipeline (v.2.2; https://github.com/ding-lab/somaticwrapper ), which includes four different callers: Strelka (v.2.9.10) 54 , MUTECT (v.1.1.7) 55 , VarScan (v.2.3.8) 56 and Pindel (v.0.2.5) 57 .
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Version used: **2.4.7**
- Evidence: Single-nucleotide variant and indel calling Single-nucleotide variant and small indel calling was performed using Strelka (v2.4.7).
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Version used: **1.0.15**
- Evidence: After a pre-processing step, we employed MuTect 1.1.7 45 and Strelka 1.0.15 46 to identify SNVs and indels in tumour samples compared to normal tissue.
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: The pipeline applies multiple artefact filters such as the read-realignment filter by BLAT 63 and the read orientation bias filters followed by SNV and indel calling with MuTect 64 and Strelka 65 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Version used: **2.9.10**
- Evidence: In brief, structural nucleotide variants were detected in the tumour–normal pairs using Mutect (v1.1.6) 81 , whereas indels were detected using a consensus of Varscan 2 (v2.4.6) 82 , Strelka (v2.9.10) 83 , Scalpel (v0.5.4) 84 and Platypus (v0.8.1.2) 85 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Evidence: Somatic SNVs were called using an in-house mutation caller 4 and short insertions and deletions were called using Strelka 34 , by comparing the aligned reads of the tumour DNA to those of the matching PBMC DNA.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Genomic evidence for inbreeding depression and purging of deleterious genetic variation in Indian tigers. (PNAS 2021)

- DOI: 10.1073/pnas.2023018118 | PMCID: PMC8670471 | PMID: 34848534
- Evidence: We called variants from the BAM files using Strelka with default options ( 90 ).
- Full pipeline: alignment/mapping [ANGSD, GATK] -> registration [GATK] -> stage not stated [Picard, Strelka, VCFtools, VEP]

### Genome editing in plants using the compact editor CasΦ. (PNAS 2023)

- DOI: 10.1073/pnas.2216822120 | PMCID: PMC9942878 | PMID: 36652483
- Version used: **2.9.2**
- Evidence: The recalibrated bam file was further applied to GATK and Strelka (v2.9.2) ( 38 ) for SNPs/InDel calling.
- Full pipeline: read trimming [BWA v0.7.17, Trim Galore] -> alignment/mapping [BWA v0.7.17, Trim Galore] -> stage not stated [GATK v4.2.0.0, R, Strelka v2.9.2]

### Development of an orally bioavailable mSWI/SNF ATPase degrader and acquired mechanisms of resistance in prostate cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2322563121 | PMCID: PMC11009648 | PMID: 38557192
- Evidence: The primary somatic call-set was generated using Strelka based on the following criteria: allele frequency exceeding 0.05 in the 22Rv1-AURs, allele frequency less than 0.01 in the normalized data, a minimum of five variant reads, normal depth surpassing 50, and Somatic Evidence Score (EVS) over the 90th percentile of the overall EVS distribution.
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [Strelka]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Version used: **2.9.10**
- Evidence: Mutations were called independently using Mutect2 (v4.1.7.0), Strelka (v2.9.10) and Octopus (v0.7.0).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

