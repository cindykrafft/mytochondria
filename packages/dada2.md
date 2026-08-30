# DADA2

- **Category:** microbiome
- **Papers in survey:** 69
- **Journals:** PNAS (43), Nature (25), Cell (1)
- **Years:** 2021 (8), 2022 (9), 2023 (13), 2024 (16), 2025 (19), 2026 (4)
- **Versions named:** 1.10.0 (2), 1.30 (1), 1.21.0 (1), 1.26.0 (1), 1.24 (1), 1.18.0 (1), 1.18 (1), 3.18 (1), 1.14 (1), 1.16.0 (1)
- **Pipeline stages it appears in:** read trimming (19), machine learning (3), differential/statistical testing (2), quantification (2), alignment/mapping (2), quality control (2), dimensionality reduction/clustering (2), visualisation (1)

## Papers

### Cervicovaginal microbiome and natural history of Chlamydia trachomatis in adolescents and young women. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.011 | PMCID: PMC12035847 | PMID: 39818212
- Evidence: QUANTIFICATION AND STATISTICAL ANALYSIS Sequence reads were clustered into amplicon sequence variants (ASVs) using DADA2 and taxonomy was assigned using a custom cervicovaginal microbiome specific database 27 employing a Naive Bayesian classifier.
- Full pipeline: quantification [DADA2] -> dimensionality reduction/clustering [DADA2] -> differential/statistical testing [DADA2, R, vegan] -> machine learning [DADA2] -> stage not stated [ggplot2, phyloseq]

### Rapid microbial methanogenesis during CO<sub>2</sub> storage in hydrocarbon reservoirs. (Nature 2021)

- DOI: 10.1038/s41586-021-04153-3 | PMCID: PMC8695373 | PMID: 34937895
- Evidence: Raw sequence data were demultiplexed and quality filtered using the q2-demux plugin followed by denoising with DADA2 48 .
- Full pipeline: read trimming [DADA2] -> machine learning [scikit-learn] -> stage not stated [QIIME 2 v2017.4]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Evidence: The paired-end reads were denoised and joined using the DADA2 plugin (v.1.16) 105 using batch-specific trimming length parameters yielding 9.1± 2.0 kb amplicon sequence variants (ASVs) per run for V1–V2, 4.5 ± 1.6 kb for V3–V4 and 6.8 ± 0.67 kb for V5–V6 amplicons.
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Trans-vaccenic acid reprograms CD8&lt;sup&gt;+&lt;/sup&gt; T cells and anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06749-3 | PMCID: PMC10686835 | PMID: 37993715
- Evidence: For Bioinformatics Analysis, unique amplicon sequences variants were inferred from raw reads using the DADA2 pipeline 36 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Cytoscape] -> visualisation [Cytoscape] -> stage not stated [DADA2, GSEA]

### Profiling the human intestinal environment under physiological conditions. (Nature 2023)

- DOI: 10.1038/s41586-023-05989-7 | PMCID: PMC10191855 | PMID: 37165188
- Evidence: Subsequent processing was performed with the R statistical computing environment (v.4.0.3) 44 and DADA2 as previously described 43 using pseudo-pooling 45 . truncLenF and truncLenR parameters were set to 250 and 180, respectively.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DADA2, DESeq2, R, limma v3.48.3] -> stage not stated [Bowtie2 v2.4.1, HMMER, phyloseq]

### The dietary sweetener sucralose is a negative modulator of T cell-mediated responses. (Nature 2023)

- DOI: 10.1038/s41586-023-05801-6 | PMCID: PMC10033444 | PMID: 36922598
- Version used: **1.18**
- Evidence: The fastq files were processed using DADA2 (v1.18) 44 , truncating the forward (respectively reverse) reads to 280 and 210 bases and trimming them by 17 and 21 bases, respectively, with a maximum of two expected errors.
- Full pipeline: read trimming [Cutadapt v2.10, DADA2 v1.18] -> alignment/mapping [Cutadapt v2.10, RSEM v1.3.1] -> stage not stated [DESeq2 v1.30, R v4.0, STAR v2.7.6, phyloseq]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Evidence: Data processing was performed using the DADA2 46 workflow for big datasets ( https://benjjneb.github.io/dada2/bigdata.html ; the workflow adjusted for the V1–V2 region can be found here: https://github.com/mruehlemann/ikmb_amplicon_processing/blob/master/dada2_16S_workflow.R ), resulting in abundance tables of amplicon sequence variants (ASVs).
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: In brief, the DADA2 algorithm was used to denoise the data as well as to remove low-quality reads and chimeras.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Version used: **1.24**
- Evidence: We used the DADA2 v.1.24 pipeline 56 in R to trim, quality-filter denoise and dereplicate the sequences, for generation of ASV tables and to assign taxonomies.
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: Amplicon sequence variants analysis Full-length 16S rRNA gene amplicon sequence variants (FL16s-ASVs) were inferred from demultiplexed HiFi reads using the DADA2 package (version 1.30.0) in R (version 4.3.3) according to the previously described DADA2 for PacBio workflow 53 with slight modifications.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Airborne DNA reveals predictable spatial and seasonal dynamics of fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-07658-9 | PMCID: PMC11269176 | PMID: 38987593
- Version used: **1.18.0**
- Evidence: 62 ), DADA2 v.1.18.0 (ref.
- Full pipeline: read trimming [Cutadapt v4.2] -> differential/statistical testing [lme4] -> stage not stated [DADA2 v1.18.0, R, phyloseq]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: Raw 16S rRNA reads were trimmed, denoised and filtered to remove chimaeric PCR artefacts using DADA2 (ref.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### A distinct Fusobacterium nucleatum clade dominates the colorectal cancer niche. (Nature 2024)

- DOI: 10.1038/s41586-024-07182-w | PMCID: PMC11006615 | PMID: 38509359
- Evidence: NR99 version, and the DADA2 version of the species training set.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v2.4.5] -> machine learning [DADA2] -> stage not stated [BLAST, Flye]

### Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre. (Nature 2024)

- DOI: 10.1038/s41586-024-07180-y | PMCID: PMC10972752 | PMID: 38480893
- Version used: **1.10.0**
- Evidence: In brief, paired-end reads were trimmed, merged and denoised using DADA2 (v1.10.0) 74 to generate an amplicon sequence variant (ASV) table.
- Full pipeline: read trimming [DADA2 v1.10.0] -> alignment/mapping [Clustal Omega v1.2.3, featureCounts] -> stage not stated [HMMER v3.1b, IQ-TREE v1.6.9, QIIME 2 v2019.10]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Evidence: Using the DADA2 package (v1.10.1) in R (v3.5.2), reads underwent further quality filtering as error rates were calculated and removed from the dereplicated reads.
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### The geologic history of marine dissolved organic carbon from iron oxides. (Nature 2025)

- DOI: 10.1038/s41586-025-09383-3 | PMCID: PMC12390840 | PMID: 40804515
- Version used: **1.30**
- Evidence: Sequence analysis was then performed in R v.4.3.1 using DADA2 (v.1.30) (ref.
- Full pipeline: stage not stated [Cutadapt v3.4, DADA2 v1.30]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: For data analysis of microbiota from mice and humans, the paired-end sequences were curated, binned into operational taxonomic units at >97% identity level, and annotated with SILVA release v.132 using DADA2 63 for mice data and v.138 and RDP version 18 databases using Mothur (v.1.40.5) 62 , 64 as previously described 61 for human data.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Functional regimes define soil microbiome response to environmental change. (Nature 2025)

- DOI: 10.1038/s41586-025-09264-9 | PMCID: PMC12390847 | PMID: 40670792
- Evidence: Sequence data analysis Sequencing data preprocessing and assigning taxonomy to ASVs with DADA2 Raw Illumina sequencing reads were stripped of primers, truncated of Phred quality score below 2, trimmed to length 263 for forward reads and 189 for reverse reads (ensuring a 25-nucleotide overlap for most reads), and filtered to a maximum expected error of 4 based on Phred scores; this preprocessing wa...
- Full pipeline: read trimming [DADA2]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **1.21.0**
- Evidence: Computational processing of 16S rRNA amplicon sequences We used the R package DADA2 (v.1.21.0) 58 following its standard operating procedure available from GitHub ( https://benjjneb.github.io/dada2/bigdata.html ).
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **1.26.0**
- Evidence: In all cases, sequencing reads were denoised to obtain ASVs using DADA2 (v.1.26.0) 61 .
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Evidence: Sequences were error-corrected, and counts of error-corrected reads per sample, which we refer to herein as exact sequence variants, were generated with DADA2 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: Specifically, reads were trimmed with cutadapt 61 , PhiX, and quality filtering, read pair merging and amplicon sequence variant resolution was performed with DADA2 62 .
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: 35 ), Deblur 34 and DADA2 (ref.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: For each sample, 3,000 quality filter-passed reads were rearranged in descending order according to the quality value, and then the trimmed reads were uploaded to the DADA2 R package v.1.18.0 to construct ASVs using the filterAndTrim function with standard parameters (maxN = 0, truncQ = 2 and maxEE = 2).
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Pesticide residues alter taxonomic and functional biodiversity in soils. (Nature 2026)

- DOI: 10.1038/s41586-025-09991-z | PMCID: PMC12965876 | PMID: 41606316
- Evidence: Exact sequence variants were identified for bacterial zero-radius OTUs (zOTUs, generated with UPARSE) and 18S eukaryote amplicon sequence variants (ASVs, generated with DADA2) following methodologies established earlier 57 – 59 .
- Full pipeline: normalisation [R] -> stage not stated [DADA2, eggNOG, fastp v0.23.4, vegan]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: For 18S diversity analyses, the taxonomy was inferred with the DADA2 (ref.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Closed microbial communities self-organize to persistently cycle carbon. (PNAS 2021)

- DOI: 10.1073/pnas.2013564118 | PMCID: PMC8609437 | PMID: 34740965
- Evidence: Data were analyzed using QIIME and DADA2 pipelines.
- Full pipeline: stage not stated [DADA2, Python, QIIME 2]

### No evidence for colonization of oral bacteria in the distal gut in healthy adults. (PNAS 2021)

- DOI: 10.1073/pnas.2114152118 | PMCID: PMC8594488 | PMID: 34610963
- Evidence: DADA2 implements a de novo process which distinguishes biological sequences from errors based partly on the former’s higher expected rate of occurrence ( 8 ).
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [BLAST] -> differential/statistical testing [R v3.4] -> stage not stated [DADA2, phyloseq]

### Human variation in gingival inflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2012578118 | PMCID: PMC8271746 | PMID: 34193520
- Evidence: Analysis of merged 300-bp paired-end reads (average length 450 bp) was performed as previously described ( 57 , 58 ) using the Quantitative Insights into Microbial Ecology (QIIME2, version 2018.2) ( 59 ) following the Divisive Amplicon Denoising Algorithm 2 (DADA2) pipeline workflow ( 36 , 60 ) to generate ASVs.
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [DADA2, QIIME 2 v2018.2, R, phyloseq]

### An ecophysiological explanation for manganese enrichment in rock varnish. (PNAS 2021)

- DOI: 10.1073/pnas.2025188118 | PMCID: PMC8237629 | PMID: 34161271
- Evidence: Quality filtering, denoising, merging of paired end reads, and chimera removal were done using DADA2 ( 70 ).
- Full pipeline: read trimming [Trimmomatic] -> stage not stated [DADA2, ImageJ, QIIME 2, R]

### Niche adaptation promoted the evolutionary diversification of tiny ocean predators. (PNAS 2021)

- DOI: 10.1073/pnas.2020955118 | PMCID: PMC8237690 | PMID: 34155140
- Evidence: OTUs were delineated as Amplicon Sequence Variants using Divisive Amplicon Denoising Algorithm 2 (DADA2) ( 69 ) and OTU tables were generated (see details in SI Appendix , SI Methods S1 ).
- Full pipeline: machine learning [AUGUSTUS v3.2.3] -> stage not stated [BUSCO, DADA2, HMMER v3.1b, RAxML v8.0.0, RepeatMasker, SPAdes, eggNOG v4.5]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Evidence: Distinct 16S rRNA amplicon sequence variants (ASVs) were inferred using DADA2 ( 70 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: Amplicon sequence variants were generated from demultiplexed paired-end reads with DADA2 ( 50 ) and taxonomy was assigned based on the DADA2-formatted training dataset [GreenGenes Database Consortium, v13.8 ( 34 )] in R (v3.5) ( 45 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: The output of the DADA2 pipeline (feature table of amplicon sequence variants) was processed for alpha and beta diversity analysis using the phyloseq ( 50 ) and microbiomeSeq ( http://www.github.com/umerijaz/microbiomeSeq ) packages in R.
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Reactive granulopoiesis depends on T-cell production of IL-17A and neutropenia-associated alteration of gut microbiota. (PNAS 2022)

- DOI: 10.1073/pnas.2211230119 | PMCID: PMC9860329 | PMID: 36409919
- Evidence: Sequences were quality-filtered, denoised, and chimera removed by DADA2 plugin ( 61 ) with following parameters: --p-trim-left-f 17; --p-trim-left-r 21; --p-trunc-len-f 280; --p-trunc-len-r 200; --p-max-ee-f 2; and --p-max-ee-r 2.
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [MAFFT] -> stage not stated [DADA2]

### A ridge-to-reef ecosystem microbial census reveals environmental reservoirs for animal and plant microbiomes. (PNAS 2022)

- DOI: 10.1073/pnas.2204146119 | PMCID: PMC9388140 | PMID: 35960845
- Evidence: Sequences were demultiplexed and processed using the MetaFlow|mics analysis pipeline ( 41 ), which uses DADA2 ( 42 ) to filter low-quality reads, denoise the data, and merge forward and reverse reads.
- Full pipeline: read trimming [DADA2] -> stage not stated [R, mothur]

### An approach for evaluating the effects of dietary fiber polysaccharides on the human gut microbiome and plasma proteome. (PNAS 2022)

- DOI: 10.1073/pnas.2123411119 | PMCID: PMC9171781 | PMID: 35533274
- Version used: **1.13.0**
- Evidence: Following demultiplexing, paired-end reads were trimmed to 200 nt, merged, and chimeric sequences were removed (DADA2 v.
- Full pipeline: read trimming [Cutadapt, DADA2 v1.13.0] -> alignment/mapping [Picard, featureCounts] -> stage not stated [Bowtie2]

### The gut microbiome influences host diet selection behavior. (PNAS 2022)

- DOI: 10.1073/pnas.2117537119 | PMCID: PMC9169907 | PMID: 35439064
- Evidence: A total of 1,398,994 raw Illumina sequencing reads (mean of 22,206 per sample ( n = 63) ± 1,111 SE) were paired and quality filtered via the DADA2 pipeline ( 61 ) in QIIME2 (version 2020.4) ( 62 ) using default parameters.
- Full pipeline: visualisation [R] -> stage not stated [DADA2, QIIME 2 v2020.4]

### The Long chain Diol Index: A marine palaeotemperature proxy based on eustigmatophyte lipids that records the warmest seasons. (PNAS 2022)

- DOI: 10.1073/pnas.2116812119 | PMCID: PMC9169758 | PMID: 35412908
- Evidence: Sequences containing an “N” and sequences without primer detection were discarded, using the DADA2 ( 69 ), Biostrings ( 70 ), and ShortReads ( 71 ) packages.
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [Cutadapt, DADA2]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: Taxonomy was assigned using the Silva (silva_nr_v128_train_set) and PR2 (pr2_version_4.10.0) databases formatted for DADA2.
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Top-down and bottom-up cohesiveness in microbial community coalescence. (PNAS 2022)

- DOI: 10.1073/pnas.2111261119 | PMCID: PMC8832967 | PMID: 35105804
- Evidence: The barcodes, indexes, and primers were removed from raw reads, producing FASTQ files with both the forward and reverse reads for each sample, ready for DADA2 analysis ( 34 ).
- Full pipeline: read trimming [QIIME 2 v1.9.0] -> stage not stated [DADA2]

### Integrated genomic and functional analyses of human skin-associated &lt;i&gt;Staphylococcus&lt;/i&gt; reveal extensive inter- and intra-species diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2310585120 | PMCID: PMC10666031 | PMID: 37956283
- Evidence: 16S rRNA amplicon (V1–V3) sequencing data were processed using the DADA2 pipeline version v1.2.0 ( 49 ) and downstream community analysis was carried out using phyloseq ( 50 ) in RStudio (R v4.2.0).
- Full pipeline: alignment/mapping [RAxML v1.1.0] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [DADA2, R v4.2, eggNOG, phyloseq]

### Localized microbially induced inflammation influences distant healthy tissues in the human oral cavity. (PNAS 2023)

- DOI: 10.1073/pnas.2306020120 | PMCID: PMC10576129 | PMID: 37782795
- Evidence: Exact amplicon sequence variant (ASV) sequences generated by the DADA2 ( 43 ) workflow were classified using the expanded Human Oral Microbiome Database (v.
- Full pipeline: stage not stated [DADA2]

### Cooperation and cheating orchestrate Vibrio assemblages and polymicrobial synergy in oysters infected with OsHV-1 virus. (PNAS 2023)

- DOI: 10.1073/pnas.2305195120 | PMCID: PMC10556616 | PMID: 37751557
- Version used: **1.14**
- Evidence: All bioinformatics processes used the next-generation microbiome bioinformatics platform QIIME 2 ( 67 ) (version 2020.2) and grouped sequences in ASV (Amplicon Sequence Variants) using DADA2 v1.14 ( 68 ).
- Full pipeline: quantification [DESeq2 v1.36.0] -> differential/statistical testing [phyloseq] -> structure determination [RAxML] -> stage not stated [DADA2 v1.14, QIIME 2]

### Environmental DNA reveals the genetic diversity and population structure of an invasive species in the Laurentian Great Lakes. (PNAS 2023)

- DOI: 10.1073/pnas.2307345120 | PMCID: PMC10500163 | PMID: 37669387
- Evidence: We analyzed all eDNA and tissue sequences using a custom script ( https://bitbucket.org/cornell_bioinformatics/amplicon/src/master/amplicon_dada2.py ) that involved a modification to the DADA2 pipeline ( 56 ) to allow for the processing of multiple loci.
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.39] -> read trimming [FastQC v0.11.8, Trimmomatic v0.39] -> differential/statistical testing [R v4.1] -> stage not stated [DADA2, lme4]

### Temperature dependence of parasitoid infection and abundance of a diatom revealed by automated imaging and classification. (PNAS 2023)

- DOI: 10.1073/pnas.2303356120 | PMCID: PMC10334780 | PMID: 37399413
- Evidence: Demultiplexed sequence data were processed using the DADA2 method ( 26 ) with some modifications to accommodate nonoverlapping paired reads ( SI Appendix , Supporting Text ).
- Full pipeline: read trimming [DADA2]

### Diversity of plant DNA in stool is linked to dietary quality, age, and household income. (PNAS 2023)

- DOI: 10.1073/pnas.2304441120 | PMCID: PMC10319039 | PMID: 37368926
- Version used: **1.10.0**
- Evidence: Paired reads were quality-filtered by discarding reads with >2 expected errors and truncated at the first base with a quality score ≤ 2, denoised, and merged to produced ASVs using DADA2 v.
- Full pipeline: read trimming [QIIME 2] -> stage not stated [Cutadapt v3.4, DADA2 v1.10.0, phyloseq v1.32.0]

### &lt;i&gt;Trachymyrmex septentrionalis&lt;/i&gt; ants promote fungus garden hygiene using &lt;i&gt;Trichoderma&lt;/i&gt;-derived metabolite cues. (PNAS 2023)

- DOI: 10.1073/pnas.2219373120 | PMCID: PMC10288546 | PMID: 37319116
- Version used: **1.16.0**
- Evidence: ...rom 90 samples were processed using Trimmomatic v0.39 ( 65 ) with options SLIDINGWINDOW 5:20 and MINLEN:125 and then processed in R v.3.6.3 using the DADA2 v1.16.0 ( 66 ) ITS workflow ( https://benjjneb.github.io/dada2/ITS_workflow.html , accessed May 26, 2021) except using only forward reads.
- Full pipeline: read trimming [DADA2 v1.16.0, Trimmomatic v0.39] -> quantification [phyloseq]

### Hydrogen stable isotope probing of lipids demonstrates slow rates of microbial growth in soil. (PNAS 2023)

- DOI: 10.1073/pnas.2211625120 | PMCID: PMC10120080 | PMID: 37036980
- Version used: **1.10.1**
- Evidence: To prepare samples for analysis with the DADA2 (version 1.10.1) bioinformatic pipeline ( 90 ), reads were demultiplexed with adapters and primers were removed using standard settings for cutadapt (version 1.8.1, Martin 2011).
- Full pipeline: read trimming [Cutadapt v1.8.1, DADA2 v1.10.1]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Evidence: DADA2 analysis was utilized to generate amplicon sequence variants (ASV) ( 74 ).
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: Primer sequences were removed using the cutadapt plugin ( 94 ), reads were truncated to a length of 130 bp, filtered, denoised, and chimeric reads were removed using the DADA2 plugin ( 95 ).
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Cross-chiral exponential amplification of an RNA enzyme. (PNAS 2024)

- DOI: 10.1073/pnas.2413668121 | PMCID: PMC11536142 | PMID: 39436654
- Evidence: Sequence reads from rounds 44 to 47 were error-corrected, merged, and compiled using DADA2 ( 66 ), and sequence space was visualized in R using a custom script.
- Full pipeline: visualisation [DADA2]

### Manipulating a host-native microbial strain compensates for low microbial diversity by increasing weight gain in a wild bird population. (PNAS 2024)

- DOI: 10.1073/pnas.2402352121 | PMCID: PMC11513901 | PMID: 39401350
- Evidence: After sequencing samples were processed using the DADA2 pipeline in R ( 80 ), following the dada2 tutorial v1.16 ( 81 ).
- Full pipeline: visualisation [vegan] -> stage not stated [Bioconductor, DADA2, R, lme4, phyloseq]

### The telencephalon is a neuronal substrate for systemic inflammatory responses in teleosts via polyamine metabolism. (PNAS 2024)

- DOI: 10.1073/pnas.2404781121 | PMCID: PMC11441480 | PMID: 39284055
- Evidence: The Divisive Amplicon Denoising Algorithm 2 (DADA2) was utilized for partitioning demultiplexed reads into distinct amplicon sequence variants (ASVs) as described ( 134 ).
- Full pipeline: read trimming [DADA2] -> stage not stated [QIIME 2]

### Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2303439121 | PMCID: PMC11317588 | PMID: 39093948
- Evidence: All initial bioinformatics processing and production of amplicon sequence variants (ASVs) by DADA2 ( 39 ) were conducted within Qiime2 ( 40 ), with taxonomy assigned via the SILVA database (release 132) ( 41 ).
- Full pipeline: quantification [ImageJ v2.0.0] -> dimensionality reduction/clustering [vegan] -> differential/statistical testing [DESeq2, R v3.6.0, phyloseq, vegan] -> visualisation [Cytoscape, R v3.6.0, igraph, phyloseq] -> stage not stated [DADA2]

### Synergistic material-microbe interface toward deeper anaerobic defluorination. (PNAS 2024)

- DOI: 10.1073/pnas.2400525121 | PMCID: PMC11295042 | PMID: 39042683
- Evidence: Raw sequences (45) were first imported into QIIME 2 and subject to assembly, quality control (with a minimum quality score of 25), and feature table construction using DADA2.
- Full pipeline: quality control [DADA2] -> stage not stated [QIIME 2 v2022.2]

### Beneficial metabolic effects of PAHSAs depend on the gut microbiota in diet-induced obese mice but not in chow-fed mice. (PNAS 2024)

- DOI: 10.1073/pnas.2318691121 | PMCID: PMC11252816 | PMID: 38968121
- Evidence: DADA2 was used to analyze 16S sequencing reads at the amplicon sequence variant (ASV) level ( 27 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, MultiQC] -> alignment/mapping [BLAST, HUMAnN, MetaPhlAn] -> quantification [HUMAnN, MetaPhlAn] -> dimensionality reduction/clustering [BLAST] -> stage not stated [DADA2]

### Climate mismatches with ectomycorrhizal fungi contribute to migration lag in North American tree range shifts. (PNAS 2024)

- DOI: 10.1073/pnas.2308811121 | PMCID: PMC11161776 | PMID: 38805274
- Evidence: 29 , which involved processing and denoising Illumina reads with DADA2 ( 62 ) and 454 pyrosequencing reads with QIIME and USEARCH ( 63 ).
- Full pipeline: stage not stated [DADA2, QIIME 2, R]

### Constraining the oxygen requirements for modern microbial eukaryote diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2303754120 | PMCID: PMC10786294 | PMID: 38165897
- Evidence: Denoising quality, chimera check, and clustering were performed using the Divisive Amplicon Denoising Algorithm 2 (DADA2) plugin tool and denoise-paired instruction ( 62 ).
- Full pipeline: dimensionality reduction/clustering [DADA2] -> differential/statistical testing [R] -> machine learning [scikit-learn] -> visualisation [ggplot2, tidyverse] -> stage not stated [QIIME 2]

### Discarded cigarette butts as overlooked reservoirs and amplifiers of antibiotic resistance genes and pathogens in urban green spaces. (PNAS 2025)

- DOI: 10.1073/pnas.2525377122 | PMCID: PMC12595418 | PMID: 41144667
- Evidence: Amplicon sequence variants were identified with DADA2_CCS ( 55 ), and bacterial taxonomy was assigned against the Silva138 database using classify-sklearn with a confidence threshold of 0.7.
- Full pipeline: differential/statistical testing [R v4.3.3, vegan] -> visualisation [ggplot2 v4.6, vegan] -> stage not stated [DADA2, scikit-learn]

### Ecosystem consequences of a nitrogen-fixing proto-organelle. (PNAS 2025)

- DOI: 10.1073/pnas.2503108122 | PMCID: PMC12452926 | PMID: 40920925
- Evidence: Sequences were denoised and demultiplexed using DADA2 in QIIME2 ( 57 ).
- Full pipeline: read trimming [DADA2, QIIME 2] -> stage not stated [R]

### Soil eDNA reflects regionally dominant species rather than local composition of tropical tree communities. (PNAS 2025)

- DOI: 10.1073/pnas.2505772122 | PMCID: PMC12403143 | PMID: 40828011
- Evidence: Sequence data were demultiplexed to intrasample PCR replicates and adaptors/primers trimmed ( 43 , 44 ), denoised with DADA2 ( 41 ), ASV tables curated with LULU ( 45 ) and soil sequences were mapped to LFDP reference library sequences at 100% match in DADA2, then finally a BLASTn search and the MEGAN lowest common ancestor algorithm ( 46 ) used to taxonomically annotate the remaining sequences.
- Full pipeline: read trimming [BLAST, DADA2] -> alignment/mapping [BLAST, DADA2] -> stage not stated [R, vegan]

### Gut sulfide metabolism modulates behavior and brain bioenergetics. (PNAS 2025)

- DOI: 10.1073/pnas.2503677122 | PMCID: PMC12207524 | PMID: 40526718
- Evidence: Amplicon sequence variants were generated with DADA2 and reads were aligned to the Greengenes13_8 reference set for taxonomic classification.
- Full pipeline: alignment/mapping [DADA2] -> stage not stated [QIIME 2]

### Methane-powered sea spiders: Diverse, epibiotic methanotrophs serve as a source of nutrition for deep-sea methane seep &lt;i&gt;Sericosura&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2501422122 | PMCID: PMC12232434 | PMID: 40523202
- Evidence: Raw sequences were then processed with DADA2 [for initial quality trimming, error rate estimation, merging of read pairs, chimeric sequence removal and community data matrix construction ( 45 )] and taxonomy was assigned to the processed ASVs (ASVs at 100% identity) using the SILVA database v138.1 ( 46 ).
- Full pipeline: quality control [FastQC v1.13] -> read trimming [DADA2] -> stage not stated [tidyverse]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Evidence: Merging of paired-end reads, data quality filtering, and denoising was performed using QIIME2 v2023.7 ( 35 ) and the DADA2 plugin ( 36 ) to generate amplicon sequence variants (ASVs).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Competition for shared resources increases dependence on initial population size during coalescence of gut microbial communities. (PNAS 2025)

- DOI: 10.1073/pnas.2322440122 | PMCID: PMC11929384 | PMID: 40063808
- Evidence: DADA2 ( 49 ) was used to filter and truncate reads, assign amplicon sequence variant (ASV) taxonomy based on the SILVA (release 138) reference database ( 94 ), and obtain a phylogeny of all ASVs.
- Full pipeline: read trimming [Cutadapt] -> quantification [R] -> stage not stated [DADA2]

### Eukaryotic phytoplankton drive a decrease in primary production in response to elevated CO&lt;sub&gt;2&lt;/sub&gt; in the tropical and subtropical oceans. (PNAS 2025)

- DOI: 10.1073/pnas.2423680122 | PMCID: PMC11929437 | PMID: 40063804
- Evidence: Quality control of the sequencing reads, identification of the amplicon sequencing variants (ASV, defined by 99% sequence similarity), and primary taxonomic affiliation based on SILVA SSU (version 138) were all conducted by QIIME2 workflow ( 76 ) and the R package DADA2 ( 77 ).
- Full pipeline: quality control [DADA2, QIIME 2, R] -> stage not stated [CDO, vegan]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Evidence: ASVs were generated using DADA2 ( 68 ), implemented within the QIIME 2 ( 69 ) suite (version 2022-2).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Version used: **3.18**
- Evidence: We analyzed the data in R, using the package DADA2 v.
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

