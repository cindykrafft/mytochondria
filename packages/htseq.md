# HTSeq

- **Category:** genomics
- **Papers in survey:** 161
- **Journals:** PNAS (89), Nature (61), Cell (9), Science (2)
- **Years:** 2021 (20), 2022 (35), 2023 (31), 2024 (33), 2025 (31), 2026 (11)
- **Versions named:** 0.9.1 (11), 0.6.1 (7), 0.12.4 (6), 0.11.2 (6), 0.6.1p (4), 0.13.5 (4), 2.0.3 (2), 2.0.1 (2), 0.11.1 (2), 0.6.0 (2)
- **Pipeline stages it appears in:** alignment/mapping (82), quantification (73), normalisation (10), differential/statistical testing (6), read trimming (3), quality control (3), dimensionality reduction/clustering (1)

## Papers

### An early cell shape transition drives evolutionary expansion of the human forebrain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.050 | PMCID: PMC8054913 | PMID: 33765444
- Version used: **0.11.2**
- Evidence: ...n/stable/ FASTQC v0.11.5 Andrews, 2010 https://github.com/s-andrews/FastQC HISAT2 v2.0.0-beta Kim et al., 2015 http://daehwankimlab.github.io/hisat2/ HTSeq v0.11.2 Anders et al., 2015 https://htseq.readthedocs.io/en/master/ g:Profiler Reimand et al., 2007 https://biit.cs.ut.ee/gprofiler/gost TCseq Wu and Gu, 2020 https://rdrr.io/bioc/TCseq/f/inst/doc/TCseq.pdf TBR2+ cell counter This paper https:/...
- Full pipeline: quality control [Cutadapt v2.4, FastQC, HISAT2 v2.0.0, HTSeq v0.11.2, Trim Galore] -> stage not stated [R v3.5]

### Soluble ACE2-mediated cell entry of SARS-CoV-2 via interaction with proteins related to the renin-angiotensin system. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.053 | PMCID: PMC7923941 | PMID: 33713620
- Evidence: ...apt Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ Bowtie2 Langmead and Salzberg, 2012 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml HTSeq Anders et al., 2015 https://htseq.readthedocs.io/en/master/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html R Gu et al., 2016 ; Ito and Murphy, 2013 https://www.r-project.org/ UniProt Bairoch et al., 200...
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> stage not stated [Bowtie2, Cutadapt, DESeq2, HTSeq]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Evidence: Transcript abundance estimates were calculated internal to the STAR aligner using the algorithm of htseq-count( Sandler et al., 2014 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Cell surface fluctuations regulate early embryonic lineage sorting. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.022 | PMCID: PMC8896887 | PMID: 35196500
- Evidence: ...q-live-cell-imaging-software Matlab MathWorks https://www.mathworks.com/products/matlab.html Prism 7 Graphpad software, Inc https://www.graphpad.com/ htseq-count ( Anders et al., 2015 ) https://htseq.readthedocs.io/en/master/ DESeq2 ( Love et al., 2014 ) https://bioconductor.org/packages/release/bioc/html/DESeq2.html Sincell ( Juliá et al., 2015 ) http://bioconductor.org/packages/release/bioc/html...
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Bioconductor] -> stage not stated [DESeq2, HTSeq, ImageJ]

### Humanized mouse liver reveals endothelial control of essential hepatic metabolic functions. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.017 | PMCID: PMC10544749 | PMID: 37562401
- Evidence: Raw sequencing reads were aligned to the human–mouse combined genome with STAR ( https://doi.org/10.1093/bioinformatics/bts635 ), annotated and counted with HTSeq ( https://doi.org/10.1093/bioinformatics/btu638 ), normalized using DESeq2 ( https://doi.org/10.1186/s13059-014-0550-8 ) and graphed using the Broad Institute Morpheus web tool.
- Full pipeline: alignment/mapping [DESeq2, HTSeq, STAR] -> normalisation [DESeq2, HTSeq, STAR] -> stage not stated [Seurat v3.2]

### Engineering RNA export for measurement and manipulation of living cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.013 | PMCID: PMC10528933 | PMID: 37437570
- Evidence: Uniquely mapped reads that overlap with genes were counted using HTSeq-count (0.13.5) 81 with default settings except “-m intersection-strict”.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.8a] -> quantification [SciPy v1.4.1] -> normalisation [scikit-image v0.19.2] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.5] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [PyMOL]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Evidence: Reads were quantified to generate gene-level feature counts from the read mapping, with HTSeq-count v.0.11.2 199 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: Read counts for SINEs are derived using HTSeq with mm10 RepeatMasker track as reference.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **0.11.0**
- Evidence: Quantification was performed using HTSeq (v0.11.0) 99 , and the final expression was defined as 2× number of paired-end matches (PM & 1MM) + number of single-end matches to the ERV reference database.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### IgA transcytosis and antigen recognition govern ovarian cancer immunity. (Nature 2021)

- DOI: 10.1038/s41586-020-03144-0 | PMCID: PMC7969354 | PMID: 33536615
- Evidence: Uniquely aligned reads were counted against Gencode v.19 using htseq-count 31 (v.0.6.1) and then normalized using DESeq2 27 taking into account batches and RNA composition bias.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, HTSeq, STAR] -> normalisation [HTSeq] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [GSEA, R v3.6.1]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Version used: **0.11.2**
- Evidence: High-quality sequences were aligned to P. virgatum v5.1 reference genome using GSNAP 65 and counts of reads uniquely mapping to annotated genes were obtained using HTSeq v.0.11.2 85 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Nociceptive nerves regulate haematopoietic stem cell mobilization. (Nature 2021)

- DOI: 10.1038/s41586-020-03057-y | PMCID: PMC7856173 | PMID: 33361809
- Version used: **0.6.1**
- Evidence: HTSeq v0.6.1 was used to count the read numbers mapped of each gene and then FPKM (Fragments Per Kilobase of exon model per Million mapped reads) of each gene was calculated based on the length of the gene and reads count mapped to this gene.
- Full pipeline: alignment/mapping [HTSeq v0.6.1] -> quantification [HTSeq v0.6.1] -> differential/statistical testing [DESeq2, R]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Version used: **0.12.4**
- Evidence: The read counts were obtained with HTSeq (v.0.12.4) 42 by using htseq-count -f bam -r pos -s no –t CDS by using a custom GTF as described elsewhere 20 .
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: Per-gene read counts were produced with htseq-count, which is incorporated in the STAR pipeline 108 .
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Version used: **0.11.4**
- Evidence: Read counts per gene locus were obtained with htseq-count (v.0.11.4) 49 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Evidence: Then, the number of reads per feature (gene) was counted using HTseq (v.0.10.0) 54 with parameter ‘htseq-count -s no -m union -f bam’ and the gene annotation of Ensembl release 87 supplemented with ERCC, EGFP and mCherry features was used.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### A male steroid controls female sexual behaviour in the malaria mosquito. (Nature 2022)

- DOI: 10.1038/s41586-022-04908-6 | PMCID: PMC9352575 | PMID: 35794471
- Version used: **0.9.1**
- Evidence: The numbers of reads mapped to genes were counted using htseq-count (version 0.9.1) with the default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, HTSeq v0.9.1, SAMtools v1.3.1] -> quantification [DESeq2, R v4.0.3] -> normalisation [DESeq2, R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3]

### GTSF1 accelerates target RNA cleavage by PIWI-clade Argonaute proteins. (Nature 2022)

- DOI: 10.1038/s41586-022-05009-0 | PMCID: PMC9385479 | PMID: 35772669
- Version used: **0.9.1**
- Evidence: HTSeq 0.9.1 with default parameters was used to count uniquely mapping reads 81 (steady-state transcript abundance was reported in reads per kilobase per million uniquely mapped reads (RPKM)).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4, HTSeq v0.9.1, RAxML v1.0.0, SAMtools v1.8, STAR v2.3] -> quantification [HTSeq v0.9.1] -> visualisation [Clustal Omega v1.2.4, RAxML v1.0.0] -> stage not stated [Bowtie2 v2.5]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Evidence: Gene expression was quantified using HTSeq-counts (v.0.6.1) (ref.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Evidence: Gene counts were generated using HTSeq-count (v0.4.1).
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **0.11.1**
- Evidence: Finally, mapped reads were sorted and quantified using htseq-count (v.0.11.1) generating a counts table (genes × samples).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Evidence: The aligned file was used to calculate strand-specific read count for each gene using HTSeq-count (version 0.13.5) 35 .
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **0.6.1p**
- Evidence: Gene and transcript abundance estimation Gene expression estimation was performed on the STAR aligned BAM file using HTSeq (version 0.6.1p1) 71 in read strand-aware union overlap resolution mode, where a read would only be assigned to a gene if it only overlapped within an exonic region of one gene, rather than multiple genes.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Version used: **0.13.5**
- Evidence: Uniquely mapping reads in genes were quantified using htseq-count v0.13.5 with parameter -s no.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: Count matrices were extracted using htseq-count with union as resolution-mode and reverse-strand mode.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### Apoptotic stress causes mtDNA release during senescence and drives the SASP. (Nature 2023)

- DOI: 10.1038/s41586-023-06621-4 | PMCID: PMC10584674 | PMID: 37821702
- Evidence: Raw read counts per gene were calculated using htseq-count.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [Cufflinks, FastQC, STAR] -> quantification [Cufflinks, DESeq2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### cGAS-STING drives ageing-related inflammation and neurodegeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-06373-1 | PMCID: PMC10412454 | PMID: 37532932
- Evidence: Bulk RNA analysis For the fibroblasts, RNA was mapped to the human genome assembly hg38 (gencode v36, Ensembl 102) using STAR aligner (v.2.7), and counts were generated with HTSeq Count.
- Full pipeline: alignment/mapping [HTSeq, STAR, featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.38.2, ImageJ, Seurat]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Version used: **0.9.1**
- Evidence: Quantification of gene expression was performed with htseq-count (v.0.9.1) using genes as features.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Version used: **0.11**
- Evidence: Read counts were extracted from the fastq files using HTSeq (v.0.11).
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: The sequencing output files from different lanes were concatenated, aligned to GRCH38 using HISAT2 and transcripts were counted using HTSeq in Python.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: Read count information was generated using HTSeq and normalized using DESeq2.
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Mitotic clustering of pulverized chromosomes from micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-05974-0 | PMCID: PMC10307639 | PMID: 37165191
- Version used: **0.6.1p**
- Evidence: Gene expression counts were generated using HTSeq (v.0.6.1p1) 53 and normalized to transcripts per kilobase million.
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> quantification [ImageJ] -> normalisation [DESeq2, GSEA v4.3.2, HTSeq v0.6.1p] -> differential/statistical testing [DESeq2, GSEA v4.3.2] -> stage not stated [BEDTools]

### RHOJ controls EMT-associated resistance to chemotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05838-7 | PMCID: PMC10076223 | PMID: 36949199
- Evidence: After transcripts were assembled, gene-level counts were obtained using HTSeq and normalized to 20 million aligned reads.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [limma] -> normalisation [HTSeq] -> differential/statistical testing [limma] -> stage not stated [CellProfiler v3.1.9, ImageJ]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Version used: **0.10.0**
- Evidence: Quantification was performed using htseq-count (v.
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: We then used HTSeq-count 40 to quantify the raw counts for all genes based on the mapped reads using the mm10 gene annotation GTF file downloaded from the UCSC genome browser.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Dendritic cells direct circadian anti-tumour immune responses. (Nature 2023)

- DOI: 10.1038/s41586-022-05605-0 | PMCID: PMC9891997 | PMID: 36470303
- Version used: **0.9.1**
- Evidence: Gene expression was quantified using HTSeq (v.0.9.1) 23 .
- Full pipeline: alignment/mapping [STAR v2.7.0] -> quantification [HTSeq v0.9.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [ImageJ]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Evidence: The resulting reads were aligned to the Aus0233 reference genome by Bowtie2 63 (v.2.5.1) using the --no-mixed flag and read counts were generated using htseq-count 64 (v.0.12.4) using the options -r pos -t CDS -m union --nonunique none.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: Raw data were mapped to the Hg19 (SUM149PT, MDA-MB-468) or hg38 (MDA-MB-468 docetaxel experiment, HCC38, HCC1395, HCC1937) genome using STAR and count files were made using HTSeq 60 , 61 .
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **0.12.4**
- Evidence: Reads on each GENCODE annotated gene were counted using HTSeq (v.0.12.4) 60 and then normalized to counts per million (CPM) using edgeR packages in R 61 .
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Mitochondrial complex I promotes kidney cancer metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07812-3 | PMCID: PMC11424252 | PMID: 39143213
- Version used: **0.6.1**
- Evidence: Counts for each gene were generated using htseq-count v0.6.1.
- Full pipeline: alignment/mapping [STAR v2.7.3] -> differential/statistical testing [DESeq2 v1.14.1, edgeR] -> stage not stated [HTSeq v0.6.1, ImageJ, R, featureCounts]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Version used: **0.9.1**
- Evidence: Reads that uniquely aligned to exonic regions were counted with HTSeq (v.0.9.1) 65 with the union setting to produce a count matrix for differential expression analysis using the DESeq2 (ref.
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Version used: **0.9.1**
- Evidence: The number of counts was summarized at the gene level using htseq-count (version 0.9.1).
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Total counts of read fragments aligned to candidate gene regions were derived using the HTSeq program ( https://htseq.readthedocs.io/en/latest/overview.html#overview ) with mouse mm10 refSeq (refFlat table) as a reference and used as a basis for the quantification of gene expression.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### IL-10 constrains sphingolipid metabolism to limit inflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07098-5 | PMCID: PMC10954550 | PMID: 38383790
- Evidence: After sorting the generated SAM files (as the output of alignment) with Picard Toolkit ( https://broadinstitute.github.io/picard/ ; Broad Institute), we counted the number of reads mapped to each gene using HTSeq 69 v0.6.1.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HTSeq, Picard] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v4.3.0]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **0.6.1**
- Evidence: For differentially expressed gene analysis, HTSeq (v0.6.1) estimated gene and convert read counts to transcripts per million from the paired-end clean data.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: The aligned reads were quantified as gene counts using HTSeq 94 with GENCODE release M30 95 .
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Circulating myeloid-derived MMP8 in stress susceptibility and depression. (Nature 2024)

- DOI: 10.1038/s41586-023-07015-2 | PMCID: PMC10901735 | PMID: 38326622
- Version used: **0.12.4**
- Evidence: Counts of reads mapping to genes were obtained using htseq-count v0.12.4 against Ensembl v90 annotation 66 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, HTSeq v0.12.4, STAR v2.5] -> quantification [ImageJ, Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: The htseq-count function of the HTSeq Python package version 0.7.1 72 was used to count uniquely aligned reads at all exons of a gene.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Alternative splicing of latrophilin-3 controls synapse formation. (Nature 2024)

- DOI: 10.1038/s41586-023-06913-9 | PMCID: PMC10830413 | PMID: 38233523
- Evidence: HTSeq was used to count reads.
- Full pipeline: alignment/mapping [STAR] -> quantification [scikit-image v0.20.0] -> stage not stated [CaImAn, DESeq2, HOMER, HTSeq, SciPy v1.10.1]

### Mucosal boosting enhances vaccine protection against SARS-CoV-2 in macaques. (Nature 2024)

- DOI: 10.1038/s41586-023-06951-3 | PMCID: PMC10849944 | PMID: 38096903
- Evidence: Transcript abundance estimates were calculated internally to the STAR aligner using the algorithm of htseq-count.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.9a] -> quantification [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [GSEA]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **0.6.1p**
- Evidence: HTSeq v0.6.1p1 was then used to quantify expression at the gene level.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: Microglia RNA-seq yielded an average of 100 million uniquely mapped reads for each sample, and gene expression levels were quantified using htseq-count 80 .
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Evidence: HTSeq-count (v.0.11.0) 53 was applied to aligned RNA-seq BAM files to count for each gene how many aligned reads overlap with its exons.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: Gene level counts were measured using HTSeq and compared using DESeq2.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **2.0.1**
- Evidence: To count the transcripts number for each gene, we converted the masked genome to protein sequences based on Helixer 121 structural annotation, and then functionally annotated the protein sequences by Mercator4 (v.7.0) 126 with both Prot-scriber and Swissprot databases, then htseq-count (v.2.0.1) 127 was applied to count the transcripts for all annotated proteins.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Unravelling cysteine-deficiency-associated rapid weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-08996-y | PMCID: PMC12267064 | PMID: 40399674
- Evidence: The number of reads in annotated genes was counted using htseq-count version .11.069.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [DESeq2 v1.48, SciPy v1.1.0] -> visualisation [DESeq2 v1.48] -> stage not stated [HTSeq, Python, R]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: Resulting HTSeq 73 matrices from bulk transcriptome were processed in R Studio with DESeq2 74 .
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Reads were aligned to Michigan State University Rice genome v.7 with the STAR aligner 36 , deduplicated using UMI-Tools 37 and counted with HTSeq-Count. scRNA-seq profiling of rice root protoplasts using the 10X Genomics Chromium system For rice seedling harvesting, gel-grown rice seedlings were directly pulled out from the growth media and root tips were cut in the enzyme solution within the opti...
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Plasticity of the mammalian integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-08794-6 | PMCID: PMC12119373 | PMID: 40140574
- Evidence: The aligned reads were summarized using htseq-count 53 .
- Full pipeline: quality control [FastQC v0.11.4] -> read trimming [R] -> alignment/mapping [Bioconductor, HTSeq, featureCounts] -> quantification [ImageJ] -> normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [ImageJ] -> stage not stated [DESeq2]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Evidence: Computational disease positioning based on human TCGA data TCGA data were downloaded using the GenomicDataCommons R package (v.1.12.0; https://bioconductor.org/packages/GenomicDataCommons ) 64 , TCGA ‘HTSeq–counts’ and corresponding clinical annotations.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Version used: **2.0.1**
- Evidence: Alignment of scRNA-seq data and gene-expression quantifications For Smart-seq2 data, raw sequencing reads were aligned to the reference genome (mm10, GRCm38) using STAR (v.2.5.3a) 50 and gene expression was quantified using htseq-count (v.2.0.1) 51 .
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **0.9.1**
- Evidence: Gene read counts were retrieved using HTSeq v.0.9.1.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **2.0.5**
- Evidence: Gene counts were generated using htseq-count (HTSeq v.2.0.5) with the following parameters: --format=bam --minaqual=10 --type=exon --idattr=gene_name --stranded=yes --mode=union using the Ensembl v93 annotation 61 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Evidence: GENCODE annotations (gencode.vM25.annotation.gtf; downloaded in April 2021) and HTSeq-count (v0.13.5) were used to assign the aligned reads to genes.
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **0.9.1**
- Evidence: Read count of aligned reads was performed with HTSeq version 0.9.1 (ref.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Evidence: Counts were generated with HTSeq 74 v.0.7.2.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: Data acquisition and preprocessing RNA sequencing (RNA-seq) data for five cancer cohorts from the publicly available TCGA programme—lung adenocarcinoma (LUAD), lung squamous cell carcinoma (LUSC), non-small cell lung cancer (NSCLC; LUAD + LUSC), pancreatic adenocarcinoma (PDAC) and skin cutaneous melanoma (SKCM)—were downloaded via the UCSC Xena platform in HTSeq-FPKM format.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: After sequencing, data was aligned to the human reference genome Hg38/GRCh38 using HISAT2 54 (v.2.1.0) and the number of reads per gene were calculated using HTSeq count 55 (v.0.5.3).
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Version used: **2.0.3**
- Evidence: Transcript abundance was quantified as transcripts per million using HTSeq v2.0.3 (ref.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **2.0.3**
- Evidence: Aligned reads were quantified using HTSeq (v.2.0.3).
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Follistatin mediates learning and synaptic plasticity via regulation of Asic4 expression in the hippocampus. (PNAS 2021)

- DOI: 10.1073/pnas.2109040118 | PMCID: PMC8488609 | PMID: 34544873
- Evidence: High-throughput sequencing (HTSeq) version 0.6.1 was used to count the reads numbers mapped to each gene.
- Full pipeline: alignment/mapping [HTSeq] -> stage not stated [R, lme4]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Version used: **0.9.1**
- Evidence: Mapping of reads to the genome and gene counts were performed using RNA-STAR v2.7.5b ( 67 ) and Galaxy ( 68 ) through the usegalaxy.eu server, and read counts over genes were obtained using htseq-count v0.9.1+galaxy1 ( 69 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Investigating lymphangiogenesis in vitro and in vivo using engineered human lymphatic vessel networks. (PNAS 2021)

- DOI: 10.1073/pnas.2101931118 | PMCID: PMC8346860 | PMID: 34326257
- Evidence: Only uniquely mapped reads were counted to genes, using “HTSeq-count” package version 0.11.2 with “union” mode ( 39 ).
- Full pipeline: alignment/mapping [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, R]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Evidence: Alignment of sequences to the reference genome of Morex (release 45) ( 26 ) was performed using HTSeq [version 0.10.0 ( 67 )] with the parameters “-r pos -i gene_id -s no–secondary-alignments ignore–supplementary-alignments ignore.” The PCA was performed on the expression data using the normalization procedure rlog() implemented in the R package DESeq2 and the plotPCA() function [version 1.22.2 ( ...
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### CRISPR-based targeting of DNA methylation in <i>Arabidopsis thaliana</i> by a bacterial CG-specific DNA methyltransferase. (PNAS 2021)

- DOI: 10.1073/pnas.2125016118 | PMCID: PMC8201958 | PMID: 34074795
- Evidence: The number of reads mapping to each gene was also calculated by htseq-count ( 30 ) using default parameters.
- Full pipeline: alignment/mapping [Bismark, HTSeq] -> normalisation [deepTools] -> differential/statistical testing [DESeq2]

### Transposon-mediated insertional mutagenesis unmasks recessive insecticide resistance in the aphid <i>Myzus persicae</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100559118 | PMCID: PMC8201860 | PMID: 34074777
- Evidence: Clean reads were aligned to the G006v2 genome assembly using HISAT2 version 2.1.0 ( 50 ) and gene expression estimated using the HTSeq count tool implemented in the HTSeq package ( 51 ).
- Full pipeline: quality control [FastQC, Trim Galore v0.4.5] -> read trimming [FastQC] -> alignment/mapping [HISAT2 v2.1.0, HTSeq] -> differential/statistical testing [edgeR v3.9] -> stage not stated [MUSCLE v3.8]

### Resetting proteostasis with ISRIB promotes epithelial differentiation to attenuate pulmonary fibrosis. (PNAS 2021)

- DOI: 10.1073/pnas.2101100118 | PMCID: PMC8157939 | PMID: 33972447
- Version used: **0.11.2**
- Evidence: Counts were generated using htseq-count (High-Throughput sequencing framework, HTSeq version 0.11.2).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> alignment/mapping [FastQC, Trimmomatic v0.36] -> differential/statistical testing [edgeR v3.28.0] -> stage not stated [Fiji v1.8.0, HTSeq v0.11.2, ImageJ v1.8.0]

### Substrate discrimination and quality control require each catalytic activity of TRAMP and the nuclear RNA exosome. (PNAS 2021)

- DOI: 10.1073/pnas.2024846118 | PMCID: PMC8040639 | PMID: 33782132
- Version used: **0.5.3**
- Evidence: The expression count matrix was then computed from the mapped reads using HTSeq version 0.5.3 ( https://www.huber.embl.de/users/anders/HTSeq/doc/overview.html ) and S. cerevisiae genome version R64-1–1.94.gtf.
- Full pipeline: alignment/mapping [HTSeq v0.5.3, Picard] -> quantification [ImageJ] -> normalisation [Bioconductor] -> differential/statistical testing [Bioconductor]

### Brd4-bound enhancers drive cell-intrinsic sex differences in glioblastoma. (PNAS 2021)

- DOI: 10.1073/pnas.2017148118 | PMCID: PMC8072233 | PMID: 33850013
- Version used: **0.11.1**
- Evidence: The read-count tables for annotated genes in the mm10 gene transfer format (.GTF) file were derived from uniquely aligned reads using HTSeq (version 0.11.1) ( 79 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, HTSeq v0.11.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Predicting transcriptional responses to cold stress across plant species. (PNAS 2021)

- DOI: 10.1073/pnas.2026330118 | PMCID: PMC7958178 | PMID: 33658387
- Version used: **0.6.1**
- Evidence: HTSeq (v 0.6.1) was used to extract the number of reads in each RNA-seq library that were mapped to annotated exons of each gene in each species using union mode ( 46 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [HTSeq v0.6.1, MAFFT v7.149, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [BEAST v5.1, DESeq2] -> simulation/modelling [BEAST v5.1] -> stage not stated [R]

### Primate innate immune responses to bacterial and viral pathogens reveals an evolutionary trade-off between strength and specificity. (PNAS 2021)

- DOI: 10.1073/pnas.2015855118 | PMCID: PMC8020666 | PMID: 33771921
- Evidence: Gene-expression estimates were obtained by summing the number of reads that mapped uniquely to each species-annotated genome using HTSeq-count (version 0.6.1) ( 55 ).
- Full pipeline: read trimming [Trim Galore v0.2.7] -> alignment/mapping [HTSeq] -> normalisation [limma] -> differential/statistical testing [R v3.6.2, limma] -> stage not stated [Cytoscape v3.7.2]

### The imprinted lncRNA <i>Peg13</i> regulates sexual preference and the sex-specific brain transcriptome in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2022172118 | PMCID: PMC7958240 | PMID: 33658376
- Evidence: HTSeq was used for counting reads overlapping into a specific feature (gene) ( 44 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### Lipid droplets in mammalian eggs are utilized during embryonic diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2018362118 | PMCID: PMC7958255 | PMID: 33649221
- Evidence: The reads mapped to separate genes were counted using HTSeq software [with “Union” mode ( 45 )], and for additional verification, pseudoalignment with the use of Kallisto was performed as well ( 46 ).
- Full pipeline: quality control [FastQC, TopHat] -> read trimming [FastQC, TopHat] -> alignment/mapping [FastQC, HTSeq, TopHat, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### OCT4 induces embryonic pluripotency via STAT3 signaling and metabolic mechanisms. (PNAS 2021)

- DOI: 10.1073/pnas.2008890118 | PMCID: PMC7826362 | PMID: 33452132
- Evidence: After removal of inadequate samples according to filtering criteria previously described ( 28 ), alignments were quantified to gene loci with htseq-count ( 87 ) based on annotation from Ensembl 87.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> variant calling [WGCNA] -> quantification [Bioconductor, HTSeq] -> dimensionality reduction/clustering [Bioconductor, WGCNA] -> differential/statistical testing [GSEA, R]

### Muscle injury causes long-term changes in stem-cell DNA methylation. (PNAS 2022)

- DOI: 10.1073/pnas.2212306119 | PMCID: PMC9907067 | PMID: 36534800
- Version used: **0.6.0**
- Evidence: Counts per gene were calculated using htseq-count (version 0.6.0), with gene annotations from Ensembl release 84.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> differential/statistical testing [R] -> stage not stated [DESeq2, HOMER, HTSeq v0.6.0, ImageJ]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Evidence: The gene expression level of the coding genes from GENCODE v30 ( 45 ) was quantified by htseq-count ( 46 ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Hedgehog-interacting protein acts in the habenula to regulate nicotine intake. (PNAS 2022)

- DOI: 10.1073/pnas.2209870119 | PMCID: PMC9674224 | PMID: 36346845
- Evidence: Quantification of aligned reads was performed using htseq-count module, part of the HTSeq framework ( 90 ), version 0.6.0, with “union” mode to handle reads overlapping more than one feature.
- Full pipeline: alignment/mapping [HTSeq, STAR, Scanpy] -> quantification [HTSeq] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Enrichr]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Evidence: Gene expression was quantified with HTSeq, followed by the variance-stabilizing transformation from DESeq2.
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### Long noncoding RNA-mediated activation of PROTOR1/PRR5-AKT signaling shunt downstream of PI3K in triple-negative breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2203180119 | PMCID: PMC9618063 | PMID: 36269860
- Evidence: To identify the pAKT high and pAKT low specimens in TCGA, TCGA-BRCA HTSeq-FPKM ( n = 1,217) data were downloaded from XENA ( https://xenabrowser.net/datapages/ ), and the RPPA-TCGA-BRCA-L4 ( n = 901) data were downloaded from TCPA ( https://tcpaportal.org/tcpa/download.html ).
- Full pipeline: quantification [HTSeq] -> stage not stated [AlphaFold v2.1.1, ImageJ, PyMOL v2.5.0]

### Microbiome composition modulates secondary metabolism in a multispecies bacterial community. (PNAS 2022)

- DOI: 10.1073/pnas.2212930119 | PMCID: PMC9586298 | PMID: 36215464
- Evidence: Resulting SAM (sequence alignment map) files were sorted with samtools v1.9 ( 62 ) and quantified by HTSeq (high throughput sequencing Python library) v0.12.4 ( 63 ) under mode “intersection-strict” against the GFF (general feature format) files previously annotated by prodigal and antiSMASH.
- Full pipeline: alignment/mapping [HTSeq, SAMtools v1.9, fastp v0.20.0] -> quantification [HTSeq, SAMtools v1.9] -> differential/statistical testing [R v4.2] -> stage not stated [Bowtie2 v2.4.2, edgeR, eggNOG]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Version used: **0.11.2**
- Evidence: The uniquely mapped reads were kept and assigned to genes using htseq-count in HTSeq (0.11.2) ( 63 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **0.6.1**
- Evidence: HTSeq v0.6.1 ( 110 ) was employed to count the number of reads mapped to each gene.
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### A kinase-independent function of cyclin-dependent kinase 6 promotes outer radial glia expansion and neocortical folding. (PNAS 2022)

- DOI: 10.1073/pnas.2206147119 | PMCID: PMC9499540 | PMID: 36095192
- Evidence: FASTQ sequences were mapped to the mm10 genome and counted with HTSeq, and the transcripts per kilobase million were then computed.
- Full pipeline: alignment/mapping [HTSeq] -> quantification [ImageJ]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; induces a muted host response in human blood that blunts the recruitment of neutrophils. (PNAS 2022)

- DOI: 10.1073/pnas.2123017119 | PMCID: PMC9351360 | PMID: 35881802
- Evidence: Reads were mapped by Bowtie2.3.1 ( 60 ) to the hg38 reference genome, and uniquely mapped indices were determined by HTSeq-counts ( 61 ).
- Full pipeline: alignment/mapping [Bowtie2 v3.1, HTSeq] -> differential/statistical testing [DESeq2, R v3.5.1] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [limma]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Evidence: HTSeq ( 56 ) was used to count the read numbers mapped of each gene, including known and novel genes.
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### Adaptive laboratory evolution and independent component analysis disentangle complex vancomycin adaptation trajectories. (PNAS 2022)

- DOI: 10.1073/pnas.2118262119 | PMCID: PMC9335240 | PMID: 35858453
- Evidence: The transcriptome analysis was performed using FastQC for quality control, Bowtie2 for mapping, htseq-count to count the number of mapped reads to each gene, and DeSeq2 to assess the differential expression between ancestor and evolved strains.
- Full pipeline: quality control [Bowtie2, FastQC, HTSeq] -> alignment/mapping [Bowtie2, FastQC, HTSeq] -> differential/statistical testing [Bowtie2, FastQC, HTSeq]

### Genetic variation that determines &lt;i&gt;TAPBP&lt;/i&gt; expression levels associates with the course of malaria in an HLA allotype-dependent manner. (PNAS 2022)

- DOI: 10.1073/pnas.2205498119 | PMCID: PMC9303992 | PMID: 35858344
- Version used: **0.6.1**
- Evidence: Trimmed reads were aligned to the human genome (GRCh38 build 88 to 92) by using HISAT2 v2.1.0 and counted with HTSeq (v0.6.1 to 0.9.1) ( 48 , 49 ).
- Full pipeline: read trimming [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, Trimmomatic v0.33, edgeR] -> alignment/mapping [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, edgeR] -> variant calling [BCFtools v1.9, R, edgeR] -> normalisation [BCFtools v1.9, R, edgeR]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Version used: **0.12.4**
- Evidence: Read counts were obtained using HTSeq (v0.12.4).
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### A broadly applicable, stress-mediated bacterial death pathway regulated by the phosphotransferase system (PTS) and the cAMP-Crp cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2118566119 | PMCID: PMC9191683 | PMID: 35648826
- Version used: **0.6.1**
- Evidence: HTSeq v0.6.1 was used to count the read numbers mapped to each gene ( 66 , 67 ).
- Full pipeline: alignment/mapping [HTSeq v0.6.1] -> stage not stated [R]

### An antagonistic pleiotropic gene regulates the reproduction and longevity tradeoff. (PNAS 2022)

- DOI: 10.1073/pnas.2120311119 | PMCID: PMC9170148 | PMID: 35482917
- Version used: **0.9.1**
- Evidence: The unaligned reads were aligned to the C. elegans reference genome (ce11) with Tophat v2.1.1, allowing for two mismatches per read, and unique alignments were quantified by HTSeq v0.9.1.
- Full pipeline: alignment/mapping [HTSeq v0.9.1] -> quantification [HTSeq v0.9.1] -> stage not stated [Bioconductor, DESeq2, ImageJ]

### Signaling from the RNA sensor RIG-I is regulated by ufmylation. (PNAS 2022)

- DOI: 10.1073/pnas.2119531119 | PMCID: PMC9169834 | PMID: 35394863
- Evidence: Gene counts were compiled using the HTSeq tool ( 69 ).
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [HTSeq]

### Variation in upstream open reading frames contributes to allelic diversity in maize protein abundance. (PNAS 2022)

- DOI: 10.1073/pnas.2112516119 | PMCID: PMC9169109 | PMID: 35349347
- Evidence: Reads overlapping computationally identified uORFs were counted by htseq ( 77 ) version 0.11.3 using htseq-count with the argument “–nonunique all” so that reads were not discarded if they mapped to multiple overlapping uORFs or uORFs on different annotated transcripts.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2, HTSeq, SAMtools] -> stage not stated [BLAST, R]

### Prevention of the foreign body response to implantable medical devices by inflammasome inhibition. (PNAS 2022)

- DOI: 10.1073/pnas.2115857119 | PMCID: PMC8944905 | PMID: 35298334
- Evidence: Gene quantification was determined with HTSeq-Counts (v0.6.1p1) ( 51 ).
- Full pipeline: quality control [MultiQC v0.9, featureCounts v1.5.0] -> alignment/mapping [MultiQC v0.9, STAR] -> quantification [DESeq2, HTSeq, R v3.4] -> normalisation [DESeq2, R v3.4] -> dimensionality reduction/clustering [MultiQC v0.9] -> differential/statistical testing [DESeq2, R v3.4] -> stage not stated [ImageJ]

### Gain of gene regulatory network interconnectivity at the origin of vertebrates. (PNAS 2022)

- DOI: 10.1073/pnas.2114802119 | PMCID: PMC8931241 | PMID: 35263228
- Evidence: For the data analysis, reads were aligned against GRCz10 (danRer10) and Bl71 assemblies using STAR v2.5.3a ( 44 ) and were assigned to genes using the HTSeq toolkit v0.11.2 ( 45 ).
- Full pipeline: alignment/mapping [Bowtie2, HTSeq, STAR v2.5.3a, kallisto] -> differential/statistical testing [DESeq2 v1.18.0, R v3.4] -> stage not stated [Cytoscape]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: Counts for each gene were generated using HTSeq-count ( 37 ) using Araport11 ( 38 ) gene and TE annotations.
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### &lt;i&gt;GRASSY TILLERS1&lt;/i&gt; (&lt;i&gt;GT1&lt;/i&gt;) and &lt;i&gt;SIX-ROWED SPIKE1&lt;/i&gt; (&lt;i&gt;VRS1&lt;/i&gt;) homologs share conserved roles in growth repression. (PNAS 2023)

- DOI: 10.1073/pnas.2311961120 | PMCID: PMC10742383 | PMID: 38096411
- Evidence: Reads mapped to genes were counted using HTSeq ( 80 ).
- Full pipeline: read trimming [STAR v2.7.9a, Trimmomatic] -> alignment/mapping [HTSeq, MAFFT, STAR v2.7.9a, Trimmomatic] -> differential/statistical testing [DESeq2] -> visualisation [IQ-TREE, R]

### Tradeoffs in bacterial physiology determine the efficiency of antibiotic killing. (PNAS 2023)

- DOI: 10.1073/pnas.2312651120 | PMCID: PMC10742385 | PMID: 38096408
- Evidence: Expression levels for each gene were quantified using htseq-count.
- Full pipeline: quantification [HTSeq]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: RNA sequencing reads were aligned onto mm10 mouse genome by HISAT2 ( 33 ) and counted by HTSeq ( 34 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We counted reads overlapping exons using HTSeq ( 77 ) based on the Ensembl GRCm38.98 annotation.
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Version used: **0.13.5**
- Evidence: HTSeq (0.13.5) was applied to summarize gene counts.
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### Light cues induce protective anticipation of environmental water loss in terrestrial bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2309632120 | PMCID: PMC10515139 | PMID: 37695906
- Evidence: The number of reads aligning to each gene in the genome was counted using HTSeq-count v0.6.0 ( 64 ), and genes with an average read count of < 1 across all samples ( SI Appendix , Table S6 ) were excluded from further analyses.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, HTSeq, TopHat v2.1.0] -> quantification [HTSeq] -> differential/statistical testing [R]

### A methanotrophic bacterium to enable methane removal for climate mitigation. (PNAS 2023)

- DOI: 10.1073/pnas.2310046120 | PMCID: PMC10466089 | PMID: 37603746
- Evidence: The htseq-count tool from the “HTSeq” framework version 2.0.2 was used with modifications (described below) to attribute the reads to ORFs using the “intersection-nonempty” mode, providing estimates of raw read counts ( 47 ).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> quantification [HTSeq]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Evidence: Reads mapped on exons were calculated, using the HTSeq-count program ( 81 ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: Next, HTSeq was used to sort reads into feature counts.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Chitin utilization by marine picocyanobacteria and the evolution of a planktonic lifestyle. (PNAS 2023)

- DOI: 10.1073/pnas.2213271120 | PMCID: PMC10194020 | PMID: 37159478
- Evidence: The number of reads that aligned to each annotated open reading frame (ORF) in the “sense” orientation was determined using the HTSeq package v0.11.2 ( 70 ) (default parameters, “nonunique all”).
- Full pipeline: alignment/mapping [HTSeq, MAFFT] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2] -> stage not stated [BLAST]

### Generation of zero-valent sulfur from dissimilatory sulfate reduction in sulfate-reducing microorganisms. (PNAS 2023)

- DOI: 10.1073/pnas.2220725120 | PMCID: PMC10194018 | PMID: 37155857
- Evidence: The HTSeq-count (v0.9.1) was used to obtain the read count and function information of each gene according to the mapping results ( 65 ).
- Full pipeline: read trimming [Trimmomatic v0.35] -> alignment/mapping [Bowtie2 v2.33, HTSeq] -> quantification [HTSeq] -> stage not stated [mothur v1.39]

### Rapid cancer cell perineural invasion utilizes amoeboid migration. (PNAS 2023)

- DOI: 10.1073/pnas.2210735120 | PMCID: PMC10151474 | PMID: 37075074
- Evidence: The expression count matrix from the mapped reads was computed using HTSeq ( http://htseq.readthedocs.io/ ), and the raw count matrix was processed using the R/Bioconductor package DESeq ( https://www.bioconductor.org/packages//2.10/bioc/html/DESeq.html ) to normalize the full data set and analyze differential expression between sample groups.
- Full pipeline: alignment/mapping [Bioconductor, HTSeq] -> normalisation [Bioconductor, HTSeq] -> differential/statistical testing [Bioconductor, HTSeq] -> stage not stated [Enrichr, ImageJ v1.52q]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Version used: **0.11.2**
- Evidence: In R, raw count matrices were generated using HTSeq (v0.11.2), then scale factors were calculated to take into account differences in library sizes using edgeR (v3.24.3), and normalization was performed using limma (v3.38.3) as in (Law et al., 2016).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: Reads were aligned to the D. melanogaster genome (dm6 version r6.24) using STAR [version 2.7.5a; ( 109 )] and per-gene read counts were determined using HTSeq [version 0.11.2; ( 110 )].
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### PCIF1-mediated deposition of 5'-cap &lt;i&gt;N&lt;/i&gt;&lt;sup&gt;6&lt;/sup&gt;,2'-&lt;i&gt;O&lt;/i&gt;-dimethyladenosine in ACE2 and TMPRSS2 mRNA regulates susceptibility to SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210361120 | PMCID: PMC9945940 | PMID: 36689652
- Version used: **0.11.2**
- Evidence: Transcripts were quantified using HTSeq (0.11.2), and DEGs were determined using DESeq2.
- Full pipeline: read trimming [Cutadapt v1.18, HISAT2 v2.1.0] -> alignment/mapping [Cutadapt v1.18, HISAT2 v2.1.0] -> quantification [DESeq2, HTSeq v0.11.2] -> stage not stated [SAMtools]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Version used: **1.99.2**
- Evidence: Where necessary, raw data were reanalyzed by bowtie2 (2.3.5) ( 77 ) alignment to the most recent Cryptococcus neoformans H99 or KN99α genome ( fungibd.org ), count matrices generated with HTSeq (1.99.2) ( 78 ) and RNA-seq analysis with Bioconductor DESeq2 (1.22.2) ( 79 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; inositol hexaphosphate pathways couple to RNA interference and pathogen defense. (PNAS 2024)

- DOI: 10.1073/pnas.2416982121 | PMCID: PMC11626161 | PMID: 39602251
- Evidence: Read counts for individual transcripts were produced with HTSeq-count.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> differential/statistical testing [edgeR] -> stage not stated [ImageJ]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: Reads were aligned to the TAIR10 genome using the STAR aligner, deduplicated using UMI-Tools, and counted with HTSeq-Count.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: Then, mapped reads were converted into read counts files with the htseq-count script ( 89 ), which were used in downstream analyses.
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### AMBRA1 controls the translation of immune-specific genes in T lymphocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2416722121 | PMCID: PMC11536168 | PMID: 39436665
- Evidence: Read counts were obtained with HTSeq, using the parameters -m union, -stranded = reverse, and the mm10 genes.gtf file from UCSC.
- Full pipeline: quantification [HTSeq] -> normalisation [pheatmap] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, SAMtools, deepTools]

### YTHDC2 serves a distinct late role in spermatocytes during germ cell differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2309548121 | PMCID: PMC11494341 | PMID: 39378093
- Evidence: Reads for each transcript were extracted using HTSeq (RRID:SCR_005514) ( 21 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### The extension of mammalian pregnancy required taming inflammation: Independent evolution of extended placentation in the tammar wallaby. (PNAS 2024)

- DOI: 10.1073/pnas.2310047121 | PMCID: PMC11494332 | PMID: 39378090
- Evidence: Raw reads were aligned to the tammar wallaby genome v3.0 using hisat2, and reads were counted using htseq-count.
- Full pipeline: alignment/mapping [HISAT2, HTSeq]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: HTSeq-counts were applied to count the overlap of reads with the gene models ( 86 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Version used: **0.6.1p**
- Evidence: Reads in features were counted using htseq-count (v0.6.1p1) as a part of HTSeq ( 51 ) ( https://htseq.readthedocs.io/en/latest/ ).
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### m&lt;sup&gt;6&lt;/sup&gt;A modification plays an integral role in mRNA stability and translation during pattern-triggered immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2411100121 | PMCID: PMC11331096 | PMID: 39116132
- Evidence: The raw counts for each gene were calculated by HTSeq and normalized by DESeq2 for further analyses ( 54 ).
- Full pipeline: read trimming [STAR, Trim Galore] -> alignment/mapping [Bowtie2, STAR, Trim Galore] -> variant calling [Bioconductor] -> normalisation [Bioconductor, DESeq2, HTSeq]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: Gene expression analysis was performed using HTSeq ( 41 ) and DESeq2 ( 42 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Astrocyte-to-microglia communication via Sema4B-Plexin-B2 modulates injury-induced reactivity of microglia. (PNAS 2024)

- DOI: 10.1073/pnas.2400648121 | PMCID: PMC11145257 | PMID: 38781210
- Evidence: Expression levels for each gene were quantified using htseq-count ( 36 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### Macrophage transplantation rescues RNASET2-deficient leukodystrophy by replacing deficient microglia in a zebrafish model. (PNAS 2024)

- DOI: 10.1073/pnas.2321496121 | PMCID: PMC11126979 | PMID: 38753517
- Version used: **2.0**
- Evidence: Counts were generated for each gene using htseq-count v2.0 ( 40 ).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [R v4.3, fgsea v1.28.0, ggplot2 v3.4.4] -> stage not stated [HTSeq v2.0]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Evidence: ...eters ‘--minimum-length=20 --max-n=0.1 --quality-cutoff=30,30’) ( 46 ) and then mapped to the TAIR10 A. thaliana reference genome with HISAT2 ( 47 ). htseq-count was used for read count (parameters: ‘--format=bam --order=name --stranded=no’) ( 48 ), and TPMs calculated as a proxy to absolute gene expression levels.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### Integrated mutational landscape analysis of poorly differentiated high-grade neuroendocrine carcinoma of the uterine cervix. (PNAS 2024)

- DOI: 10.1073/pnas.2321898121 | PMCID: PMC11046577 | PMID: 38625939
- Evidence: Sequencing reads were aligned and processed using HISAT2 ( 47 ) and HTSeq-count ( 48 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [CNVkit, GATK]

### Episymbiotic Saccharibacteria TM7x modulates the susceptibility of its host bacteria to phage infection and promotes their coexistence. (PNAS 2024)

- DOI: 10.1073/pnas.2319790121 | PMCID: PMC11032452 | PMID: 38593079
- Version used: **0.9.1**
- Evidence: HTSeq (v0.9.1) was used to statistically compare the read count value for each gene and DESeq (v1.38.3) was conducted to analyze the differential expressed mRNA.
- Full pipeline: quantification [HTSeq v0.9.1] -> differential/statistical testing [HTSeq v0.9.1] -> stage not stated [IMOD, ImageJ, MotionCor2]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: We estimated read counts on genes/peaks with HTSeq-count v0.13.5 ( 88 ), and then compared adults to juveniles using DESeq2 v1.32.0 ( 89 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Evidence: RNA-seq reads were aligned to the GRCh38 genome using STAR v.2.5.2 ( 97 ), and only uniquely mapped reads with a two-mismatch threshold were considered for downstream analysis and quantified to the gene level using HTSeq ( 98 ).
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Improved RNA stability estimation through Bayesian modeling reveals most <i>Salmonella</i> transcripts have subminute half-lives. (PNAS 2024)

- DOI: 10.1073/pnas.2308814121 | PMCID: PMC10998600 | PMID: 38527194
- Evidence: For quantification, htseq-count with default options was used for counting reads aligning to CDS, sRNA, and ERCC spike-ins, while the 60 base subgenic windows were counted with the option — nonunique all to ensure that overlapping reads are assigned to all overlapping segments.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [Cutadapt v4.1, HTSeq] -> quantification [HTSeq] -> normalisation [Stan] -> differential/statistical testing [GSEA, Stan] -> simulation/modelling [Stan] -> stage not stated [R, edgeR, limma]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Version used: **0.13.5**
- Evidence: Read counts for genes and TEs were obtained with HTSeq (v 0.13.5).
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Evidence: Transcript abundance was then estimated from unique mapped reads into raw counts using HTSeq ( 41 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Evidence: After sequencing, data were aligned to the human reference genome Hg38/GRCh38 using HISAT2 [v2.1.0 ( 61 )] and to calculate the number of reads per gene HTSeq count [v0.5.3 ( 62 )] was used.
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: The quantification of gene expression was obtained with HTSeq-count ( 121 ).
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### Mechanisms of photoreceptor protection upon targeting the &lt;i&gt;Nrl-Nr2e3&lt;/i&gt; pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2500446122 | PMCID: PMC12130857 | PMID: 40397675
- Version used: **0.12.4**
- Evidence: Read counts were calculated using HTSeq (0.12.4) ( 48 ).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [DESeq2 v1.42.0]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Evidence: The number of reads was counted using HTSeq-count (0.6.1p1).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### Phospholipid flippase ATP11A brokers uterine epithelial integrity and function. (PNAS 2025)

- DOI: 10.1073/pnas.2420617122 | PMCID: PMC12054786 | PMID: 40261925
- Evidence: Count tables were assembled with htseq-count (bioconda 2018.11) using the reverse strand and nonunanimous settings, resulting in 40M to 89M gene counts per sample.
- Full pipeline: quality control [R, Seurat v5.1.0] -> alignment/mapping [STAR v2.6.1a] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq, ImageJ v1.53, Metascape]

### PPARα regulates ER-lipid droplet protein Calsyntenin-3β to promote ketogenesis in hepatocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2426338122 | PMCID: PMC12054784 | PMID: 40258152
- Evidence: HTSeq-count was used to extract raw gene counts.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### Diet-regulated transcriptional plasticity of plant parasites in plant-mutualist environments. (PNAS 2025)

- DOI: 10.1073/pnas.2421367122 | PMCID: PMC12037023 | PMID: 40244681
- Evidence: Gene counts were quantified by HTSeq ( 53 ) and analyzed by DESeq2 (53 to yield differential gene expression profiles of G. pallida parasitizing potato roots ± distal and concurrent AM fungal colonization.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, HTSeq, ImageJ] -> differential/statistical testing [DESeq2, HTSeq] -> stage not stated [IQ-TREE]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Version used: **0.13.5**
- Evidence: The number of aligned reads was quantified using HTSeq (version 0.13.5).
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Version used: **0.12.4**
- Evidence: For the sugr-1 silencing experiment, the same packages were used but with FastQC v0.11.8, BBduk v38.34, STAR v2.7.0e, HTSeq v0.12.4, R v3.5.2, DESeq2 v1.22.2, EnhancedVolcano v1.0.1, and gprofiler2 v0.1.6.
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Version used: **0.11.3**
- Evidence: Raw counts were obtained using HTSeq v.0.11.3 ( 65 ).
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Targeting EPHB2/ABL1 restores antitumor immunity in preclinical models of ependymoma. (PNAS 2025)

- DOI: 10.1073/pnas.2319474122 | PMCID: PMC11789170 | PMID: 39841145
- Evidence: Gene read counts were then generated using the Python package HTSeq (htseq-count).
- Full pipeline: quantification [HTSeq] -> dimensionality reduction/clustering [R, STRING db, pheatmap] -> stage not stated [Bioconductor, DESeq2, Seurat]

### Mitochondrial DNA lineages determine tumor progression through T cell reactive oxygen signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2417252121 | PMCID: PMC11725793 | PMID: 39752523
- Evidence: Counts for each gene were quantified using htseq-count ( 56 ) based on the annotations mentioned above.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R] -> stage not stated [MACS2, pheatmap]

### ANAC044 orchestrates mitochondrial stress signaling to trigger iron-induced stem cell death in root meristems. (PNAS 2025)

- DOI: 10.1073/pnas.2411579122 | PMCID: PMC11725852 | PMID: 39793035
- Version used: **0.6.0**
- Evidence: RNA-seq read mapping and raw read counting were conducted using STAR (v 2.6.1) and HTSeq (v 0.6.0), respectively; further downstream analysis was all achieved in R (v 4.3.3) as described in SI Appendix , Materials and Methods .
- Full pipeline: alignment/mapping [HTSeq v0.6.0, R v2.6.1, STAR v2.6.1] -> quantification [HTSeq v0.6.0, R v2.6.1, STAR v2.6.1] -> stage not stated [GSEA]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: To expand the mapping to cover specific MNMR genes of interest not originally included in the filtered transcript set, htseq-count ( 64 ) was used to count the transcript reads in the RNA-seq libraries.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: The quantification process involved marking read duplicates with an in-house UTAP script, followed by quantification using HTSeq-count (DOI: 10.1093/bioinformatics/btu638 ) in union mode.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Evidence: Transcript abundance was quantified with HTSeq-Count v0.12.4 ( 61 ).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Gene-level quantification was conducted with HTSeq ( 42 ) (v0.11.0) using Gencode ( 43 ) V39 primary assembly annotations.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### A bacterial translation activator with an intrinsically disordered RNA-binding region. (PNAS 2026)

- DOI: 10.1073/pnas.2519770123 | PMCID: PMC12818456 | PMID: 41543904
- Evidence: To assess the relative abundance of RNAs copurifying with PhaF in our CLIP/CLAP-seq experiment or to assess the relative abundance of RNAs obtained from total RNA samples, the libraries were mapped to the PAO1 genome using bowtie2, counted with htseq-count ( 61 ), and analyzed with DESeq2 in R ( 62 ). β-Galactosidase Assays.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, HTSeq, R] -> quantification [Bowtie2, DESeq2, HTSeq, R] -> stage not stated [Cutadapt v2.10]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Version used: **0.5.4p**
- Evidence: Transcript abundance was quantified using HTSeq v0.5.4p5.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **2.0.2**
- Evidence: We then counted how many reads overlapped an annotated gene (GENECODE v32 annotations) using HTSeq (v2.0.2) ( 122 ) (htseq-count –stranded=reverse –order=name -f bam –additional-attr=gene_name -m union), and used the output counts files to find DEGs with DESeq2 ( 123 ), run with default parameters within the Galaxy platform ( 124 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

