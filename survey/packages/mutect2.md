# Mutect2

- **Category:** genomics
- **Papers in survey:** 47
- **Journals:** Nature (31), PNAS (7), Cell (7), Science (1), Lancet (1)
- **Years:** 2021 (6), 2022 (4), 2023 (12), 2024 (8), 2025 (12), 2026 (5)
- **Versions named:** 1.1.7 (5), 4.5 (1), 4.2.2.0 (1), 4.1.4.1 (1), 4.1.4 (1), 4.1.7.0 (1), 1.1.4 (1), 1.1.45 (1)
- **Pipeline stages it appears in:** variant calling (14), alignment/mapping (6), registration (2), simulation/modelling (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: These somatic mutations were then called using GATK4 Mutect2 in “normal-tumor” paired mode ( Van der Auwera et al., 2013 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Microenvironment drives cell state, plasticity, and drug response in pancreatic cancer. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.017 | PMCID: PMC8822455 | PMID: 34890551
- Version used: **1.1.45**
- Evidence: Single nucleotide variants were called using MuTect v1.1.45, insertions and deletions were called using GATK Indelocator.
- Full pipeline: quality control [RSEM] -> alignment/mapping [GATK v1.6] -> registration [GATK v1.6] -> differential/statistical testing [R v4.0] -> stage not stated [Mutect2 v1.1.45, Picard, Python v3.7.4, Seurat v2.3.4]

### Characterizing genetic intra-tumor heterogeneity across 2,658 human cancer genomes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.009 | PMCID: PMC8054914 | PMID: 33831375
- Evidence: G.G. receives research funds from IBM and Pharmacyclics and is an inventor on patent applications related to MuTect, ABSOLUTE, MutSig, MSMuTect, and POLYSOLVER.
- Full pipeline: quantification [SAMtools] -> stage not stated [GSEA, IMPUTE2, Mutect2, R, fgsea]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Evidence: ...sion 1.6) Lai et al., 2016b https://github.com/AstraZeneca-NGS/VarDict Strelka2 (version 2.9.10) Kim et al., 2018 https://github.com/Illumina/strelka Mutect2 (gatk version 3.8) Cibulskis et al., 2013 https://gatk.broadinstitute.org/hc/en-us/articles/360037593851-Mutect2 freebayes (version 1.1.0.46) Garrison and Marth, 2012 https://github.com/freebayes/freebayes HaplotypeCaller (gatk version 3.8) D...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Version used: **1.1.7**
- Evidence: Somatic variants were detected using two tools (MuTect v1.1.7 & VarScan2 v2.4.1) ( Cibulskis et al., 2013 ; Koboldt et al., 2012 ), using the following method: SAMtools mpileup (version 0.1.19) was used to locate non-reference positions in tumor and germline samples.
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: Ascertainment of CHIP carriage status in ARIC CHIP was previously determined using whole exome sequencing data using GATK Mutect2 118 and ANNOVAR 119 as reported by Bick et al.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Evidence: Variant calling was performed using both Strelka (Illumina) and MuTect (The Broad Institute) by comparing each patient’s tumor DNA to a normal reference (same patient’s PBMC DNA).
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Trametinib versus standard of care in patients with recurrent low-grade serous ovarian cancer (GOG 281/LOGS): an international, randomised, open-label, multicentre, phase 2/3 trial. (Lancet 2022)

- DOI: 10.1016/s0140-6736(21)02175-9 | PMCID: PMC8819271 | PMID: 35123694
- Evidence: Variant calling was performed by use of a majority vote system with three variant caller algorithms: VarDict, Mutect2, and Freebayes.
- Full pipeline: variant calling [Mutect2]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **4.1.4.1**
- Evidence: SNV detection Somatic mutations were first called for each tumour sample separately against matched blood derived buffycoats or adjacent normal tissue samples with Mutect2 (v4.1.4.1) using the options ‘--af-of-alleles-not-in resource 0.0000025 --germline-resource af-onlygnomad.hg38.vcf.gz’ (refs.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Evidence: Post-processed alignments were genotyped using Mutect2, Strelka2, Platypus and SvABA using somatic calling models for each pair of ancestral and end-point cultures, as described below.
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **4.1.4**
- Evidence: Somatic variant calling was performed using Mutect2 (version 4.1.4).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: Tumour-only somatic mutation calling using bulk data For samples for which paired normal samples were not available, tumour-only somatic variants were called using the Mutect2 (tool from GATK v.4.1.2.0) tumour-only version of the Somaticwrapper pipeline ( https://github.com/ding-lab/somaticwrapper/tree/tonly.v1.0 ) with the GDC panel of normal data ( https://gdc.cancer.gov/about-data/gdc-data-proc...
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Rare variant associations with plasma protein levels in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06547-x | PMCID: PMC10567546 | PMID: 37794183
- Version used: **4.2.2.0**
- Evidence: Detecting CH somatic mutations To detect putative CH somatic variants, we used the same GRCh38 genome reference aligned reads as for germline variant calling, and ran somatic variant calling with GATK’s Mutect2 (v.4.2.2.0) 67 .
- Full pipeline: alignment/mapping [GATK, Mutect2 v4.2.2.0] -> variant calling [GATK, Mutect2 v4.2.2.0] -> differential/statistical testing [R] -> stage not stated [SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Evidence: Initial variant calls in the mtDNA and reference NUMT regions are made from mapped WGS data using Mutect2 and HaplotypeCaller, respectively (using GATK v.4.2.6.0), and haplogroup inference is performed using Haplogrep 52 .
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Evolutionary histories of breast cancer and related clones. (Nature 2023)

- DOI: 10.1038/s41586-023-06333-9 | PMCID: PMC10432280 | PMID: 37495687
- Evidence: In the entire WGS analysis, mutation calling was performed by means of paired analysis using a ‘three-caller combination’ to improve the sensitivity and true positive rate, wherein mutations were called by three different callers (Genomon2, Mutect2 (ref.
- Full pipeline: stage not stated [ANNOVAR, MACS2, Mutect2, R, SAMtools]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Evidence: To identify short variants, we performed candidate short somatic variant calling using Mutect2, calling variants in BASIS assemblies (as tumour sample) against input BAC sequences (matched normal).
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: Somatic mutations were identified using Mutect2 53 by comparing to patients’ germline variations.
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Version used: **1.1.7**
- Evidence: MuTect 1.1.7 and Strelka 1.0.15 were used to call SNV and indels on pre-processed sequencing data.
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: Detection of RNA variants RNA-specific variants were called using the somatic variant caller Mutect2 from GATK (v.4.1.7.0) 55 , 86 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Version used: **1.1.7**
- Evidence: MuTect (v.1.1.7) 48 was also used to detect SNVs utilizing annotation files contained in GATK bundle 2.8.
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Evidence: In brief, sequences were aligned with BWA (v.0.7.17) to mm10, and mutations were called using Mutect2 (gatk4: 4.1.8.1).
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: Mutation calling SNVs were called using the Mutect2 (ref.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### Non-viral precision T cell receptor replacement for personalized cell therapy. (Nature 2023)

- DOI: 10.1038/s41586-022-05531-1 | PMCID: PMC9768791 | PMID: 36356599
- Evidence: NSMs identified by at least two mutation callers among VarScan2 and MuTect or MuTect2, VarDictJava and Strelka2 were retained as potential neoantigens 51 – 54 .
- Full pipeline: alignment/mapping [BWA, RSEM] -> quantification [RSEM] -> normalisation [RSEM] -> stage not stated [Mutect2]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Mutation calling was carried out on each isoform/sample bam file using Mutect2 in tumour only mode on each sample using the nf-core sarek pipeline 75 ( https://github.com/nf-core/sarek ).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Evidence: Somatic single-nucleotide variants and insertion or deletion (indel) variants were called using Illumina Dragen 58 and GATK Mutect2 (ref.
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: Somatic short-variant calling Putative somatic SNVs, MNVs and/or indels were identified in each tumour–control pair using multiple accelerated tools (TNhaplotyper, corresponding to MuTect2 57 of GATK3; TNhaplotyper2, corresponding to MuTect2 57 of GATK4; TNsnv, corresponding to MuTect 58 ) and TNscope 59 of Sentieon Genomics software (v.sentieon-genomics-202010.01).
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: Next, the POLYSOLVER mutation-detection script (shell_call_hla_mutations_from_type) was run on matched tumour–normal pairs to call tumour-specific alterations in HLA-aligned sequencing reads using MuTect 118 .
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Evidence: Only SNVs and InDels variants that passed Mutect2 filtering (FILTER = “PASS”) were considered for downstream analyses.
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Evidence: In brief, only MuTect 59 calls marked as ‘KEEP’ were selected and taken into the next step.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Tracking clonal evolution during treatment in ovarian cancer using cell-free DNA. (Nature 2025)

- DOI: 10.1038/s41586-025-09580-0 | PMCID: PMC12629990 | PMID: 41034582
- Evidence: SNV calling was performed on these libraries individually using Mutect2.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Mutect2, Seurat]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: We ran the Mutect2 variant caller 63 on the merged data across all the libraries from each patient.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Version used: **4.5**
- Evidence: Somatic mutations were called by GATK Mutect2 v.4.5 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Version used: **1.1.7**
- Evidence: After a pre-processing step, we employed MuTect 1.1.7 45 and Strelka 1.0.15 46 to identify SNVs and indels in tumour samples compared to normal tissue.
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: The pipeline applies multiple artefact filters such as the read-realignment filter by BLAT 63 and the read orientation bias filters followed by SNV and indel calling with MuTect 64 and Strelka 65 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Immune evasion through mitochondrial transfer in the tumour microenvironment. (Nature 2025)

- DOI: 10.1038/s41586-024-08439-0 | PMCID: PMC11798832 | PMID: 39843734
- Evidence: For each sample, variants were called using Mutect2 in the Genome Analysis Toolkit (v.4.1.8) under mitochondrial mode and with the read filter marked as duplicate disabled.
- Full pipeline: stage not stated [GATK v4.1.8, Mutect2, SnpEff v5.1d]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Evidence: A standard GATK best practice pipeline was used to process the samples and call somatic genetic variants using GATK Mutect2 50 .
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: Mutect2 from the GATK toolkit (v.4.2.0.0) 62 was used to call indels and somatic mutations with the default settings.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Evidence: Somatic variant calling was done using three different tools (cgpCaVEMan 55 v.1.15.2, Mutect2 (ref.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Evidence: Somatic SNVs and short indels were called using Mutect2 (GATK v.4.0) and Strelka2 (v.2.9.10) 60 , 61 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### A rapidly reversible mutation generates subclonal genetic diversity and unstable drug resistance. (PNAS 2021)

- DOI: 10.1073/pnas.2019060118 | PMCID: PMC8639346 | PMID: 34675074
- Evidence: Mutation callers are ineffective in detecting long insertions from short reads: on simulated data, both Mutect2 and HaplotypeCaller often fail to detect tandem duplications longer than 85 bp.
- Full pipeline: variant calling [Mutect2] -> simulation/modelling [Mutect2]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Version used: **1.1.7**
- Evidence: Single nucleotide variants (SNVs) and small insertions and deletions (INDELs) were obtained by taking the union of three callers GATK4 Mutect2 ( http://www.broadinstitute.org/gsa/wiki/index.php/The_Genome_Analysis_Toolkit ) ( 47 ), VarDict (v1.5.8, https://github.com/AstraZeneca-NGS/VarDict ) ( 48 ), and MuTect (v1.1.7, https://github.com/broadinstitute/mutect ) ( 49 ) using default parameters or ...
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Evidence: Variant calling was performed with Mutect2 (GATK version 4.2.0.0), and consensus sequences were generated using bcftools version 1.9.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: Somatic mutations were detected using GATK Mutect2 and FilterMutectCalls ( 17 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Natural history of liver fluke infection underpins epidemiological patterns of biliary cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2423536122 | PMCID: PMC12541340 | PMID: 41071656
- Evidence: We called SNVs and indels using GATK Mutect2 with a panel of normals provided by the Broad Institute and additional filters to remove secondary and supplementary reads.
- Full pipeline: stage not stated [GATK v4.1.4.1, Mutect2, SAMtools v1.9]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Version used: **1.1.4**
- Evidence: In summary, this assay consists of the following standard workflow: Reads are mapped using BWA MEM and indel-realigned and baseQ-recalibrated using GATK; then mutations are called using MuTect (v1.1.4) and SomaticIndelDetector (GATK v2.3.9).
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### A plasma-based DNA test for quantification of disease burden in acute myeloid leukemia patients undergoing bone marrow transplantation. (PNAS 2026)

- DOI: 10.1073/pnas.2537987123 | PMCID: PMC13099560 | PMID: 41980102
- Evidence: Variants in the leukemia cell-containing sample were called using Mutect2 ( https://gatk.broadinstitute.org/hc/en-us/articles/360037593851-Mutect2 ) using remission bone marrow or peripheral blood samples as the matched normal ( SI Appendix , Table S2 ).
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [Picard] -> stage not stated [Mutect2]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Version used: **4.1.7.0**
- Evidence: Mutations were called independently using Mutect2 (v4.1.7.0), Strelka (v2.9.10) and Octopus (v0.7.0).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

