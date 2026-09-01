# Cufflinks

- **Category:** genomics
- **Papers in survey:** 47
- **Journals:** PNAS (36), Nature (9), Cell (2)
- **Years:** 2021 (8), 2022 (10), 2023 (11), 2024 (6), 2025 (7), 2026 (5)
- **Versions named:** 2.2.1 (17), 2.1.1 (3), 2.1.0 (1), 2.0.2 (1), 2.3.1 (1), 2.2.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (27), quantification (25), differential/statistical testing (10), normalisation (5), quality control (1), variant calling (1)

## Papers

### A defective viral genome strategy elicits broad protective immunity against respiratory viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.023 | PMCID: PMC8598942 | PMID: 34852237
- Evidence: Differential gene and transcript expression analysis of mRNA-seq experiments with TopHat-Cufflinks-Cuffdiff pipeline ( Trapnell et al., 2012 ).
- Full pipeline: differential/statistical testing [Cufflinks, TopHat] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Version used: **2.2.1**
- Evidence: Transcript abundance and differential expression were calculated with Cufflinks 2.2.1.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: Cufflinks was used to generate transcript abundance as fragments per kilobase of transcript per million mapped reads (FPKM), and statistical analysis of FPKM values was calculated using R (Bioconductor).
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Targeting myeloid chemotaxis to reverse prostate cancer therapy resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06696-z | PMCID: PMC10686834 | PMID: 37844613
- Version used: **2.2.1**
- Evidence: Gene expression as fragments per kilobase of transcript per million mapped reads (FPKM) was calculated using Cufflinks (v.2.2.1).
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, TopHat v2.0.7] -> quantification [Cufflinks v2.2.1] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSVA v1.4, R]

### Apoptotic stress causes mtDNA release during senescence and drives the SASP. (Nature 2023)

- DOI: 10.1038/s41586-023-06621-4 | PMCID: PMC10584674 | PMID: 37821702
- Evidence: Fragments per kilobase of transcript per million mapped reads (FPKM) values were generated using Cufflinks.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [Cufflinks, FastQC, STAR] -> quantification [Cufflinks, DESeq2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **2.2.1**
- Evidence: Mapped bam files were converted to FPKM using Cufflinks (v.2.2.1) 79 with the “--compatible-hits-norm” option and human GRCh38.p12 transcript reference.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Evolutionary trajectories of small cell lung cancer under therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07177-7 | PMCID: PMC10972747 | PMID: 38480884
- Evidence: Expression levels were determined for uniquely mapped paired-end reads using Cufflinks referring to the human reference genome, and expression levels were quantified as fragments per kilobase exon per million mapped reads (Supplementary Table 10 ).
- Full pipeline: alignment/mapping [Cufflinks] -> quantification [Cufflinks]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **2.1.0**
- Evidence: Read count normalization (FPKM) and differential expression analysis were performed using Cufflinks (v.2.1.0).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **2.2.1**
- Evidence: Fragments per kilobase of transcript per million mapped read values were evaluated using Cufflinks v.2.2.1 (refs.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **2.1.1**
- Evidence: The sorted BAM files were further processed using Cufflinks (v.2.1.1) to quantify the transcript abundances displayed in FPKM.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **2.2.1**
- Evidence: Gene expression as fragments per kilobase of transcript per million mapped reads (FPKM) was calculated using Cufflinks (v.2.2.1).
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Coordinated bacterial and plant sulfur metabolism in <i>Enterobacter</i> sp. SA187-induced plant salt stress tolerance. (PNAS 2021)

- DOI: 10.1073/pnas.2107417118 | PMCID: PMC8609655 | PMID: 34772809
- Version used: **2.2.0**
- Evidence: Transcript assembly, quantification, and differential expression analysis were performed by using Cufflinks version 2.2.0 ( 52 ).
- Full pipeline: quality control [R] -> read trimming [Trimmomatic] -> alignment/mapping [TopHat v2.0.9, featureCounts v1.6.5] -> quantification [Cufflinks v2.2.0, featureCounts v1.6.5] -> differential/statistical testing [Cufflinks v2.2.0] -> stage not stated [ImageJ]

### The ATP-hydrolyzing ectoenzyme E-NTPD8 attenuates colitis through modulation of P2X4 receptor-dependent metabolism in myeloid cells. (PNAS 2021)

- DOI: 10.1073/pnas.2100594118 | PMCID: PMC8488689 | PMID: 34548395
- Version used: **2.1.1**
- Evidence: Fragments per kilobase of exons per million mapped fragments (FPKMs) were calculated using Cufflinks version 2.1.1.
- Full pipeline: alignment/mapping [Cufflinks v2.1.1, TopHat v2.0.12] -> quantification [Cufflinks v2.1.1]

### An introgressed gene causes meiotic drive in <i>Neurospora sitophila</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2026605118 | PMCID: PMC8092558 | PMID: 33875604
- Evidence: A transcriptome was also assembled for W1434 by mapping RNA-sequencing (RNA-seq) reads to the PacBio assembly with STAR ( 48 ) and calling transcripts using Cufflinks ( 49 ).
- Full pipeline: alignment/mapping [Cufflinks] -> differential/statistical testing [RAxML] -> stage not stated [ADMIXTURE, BLAST, IQ-TREE]

### Long-read assembly of a Great Dane genome highlights the contribution of GC-rich sequence and mobile elements to canine genomes. (PNAS 2021)

- DOI: 10.1073/pnas.2016274118 | PMCID: PMC7980453 | PMID: 33836575
- Version used: **2.2.1**
- Evidence: De novo gene models were created based on alignment of RNA-Seq reads using Cufflinks (v2.2.1) ( 48 , 49 ) and, in a non−reference-guided fashion, using Trinity (v2.3.2) ( 50 ).
- Full pipeline: alignment/mapping [Canu v1.3, Cufflinks v2.2.1, minimap2 v2.9] -> stage not stated [RepeatMasker v4.0.7, kallisto v0.46.0]

### Restriction of food intake by PPP1R17-expressing neurons in the DMH. (PNAS 2021)

- DOI: 10.1073/pnas.2100194118 | PMCID: PMC8020659 | PMID: 33753517
- Evidence: TopHat and Cufflinks apps were used to analyze RNA-seq results.
- Full pipeline: stage not stated [Cufflinks, TopHat]

### Prediction of Alzheimer's disease-specific phospholipase c gamma-1 SNV by deep learning-based approach for high-throughput screening. (PNAS 2021)

- DOI: 10.1073/pnas.2011250118 | PMCID: PMC7826347 | PMID: 33397809
- Evidence: To annotate gene expression, fragments per kb per million reads values of each gene were calculated using Cufflinks package (v2.2.1).
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [ANNOVAR, BCFtools v1.3, Cufflinks]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **2.2.1**
- Evidence: The Cufflinks v.2.2.1 ( 100 ) program was employed to calculate the normalized expression level (FPKM) of annotated genes.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### A family of unusual immunoglobulin superfamily genes in an invertebrate histocompatibility complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207374119 | PMCID: PMC9546547 | PMID: 36161920
- Evidence: A reference-guided transcriptome was generated with Cufflinks ( 70 ).
- Full pipeline: alignment/mapping [AlphaFold, HISAT2] -> stage not stated [Cufflinks, HMMER]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **2.2.1**
- Evidence: RNA-sequencing reads were aligned with HISAT2 v2.0.3 ( 90 ), and gene - expression levels were quantified with Cufflinks 2.2.1 ( 91 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Version used: **2.2.1**
- Evidence: Expression abundances (FPKMs) for Zea mays B73 AGPv4 genes ( 49 ) were quantified with Cufflinks (version 2.2.1) ( 52 ).
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Evidence: Cufflinks Reference Annotation Based Transcript (RABT) assembly method ( 55 ) was used to assemble the set of transcript isoforms of each bam file obtained din the mapping step.
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Reads without the insertion tag were separately aligned using Bowtie 2 and differential expression analysis was done between the experimental groups using Cufflinks.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### RNPS1 inhibits excessive tumor necrosis factor/tumor necrosis factor receptor signaling to support hematopoiesis in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200128119 | PMCID: PMC9170173 | PMID: 35482923
- Evidence: Cufflinks and cuffmerge (v.2.1.1) were then used to calculate fragments per kilobase of transcript per million reads mapped and consolidate results across the samples (data were averaged for each genotype/treatment combination).
- Full pipeline: alignment/mapping [Cufflinks] -> variant calling [Cufflinks] -> stage not stated [R]

### The embryonic node behaves as an instructive stem cell niche for axial elongation. (PNAS 2022)

- DOI: 10.1073/pnas.2108935119 | PMCID: PMC8812687 | PMID: 35101917
- Evidence: Transcripts were counted and normalized using Cufflinks ( 61 ) programs cuffquant and cuffnorm , respectively.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [TopHat] -> normalisation [Cufflinks]

### Translational control of <i>E2f1</i> regulates the <i>Drosophila</i> cell cycle. (PNAS 2022)

- DOI: 10.1073/pnas.2113704119 | PMCID: PMC8795540 | PMID: 35074910
- Evidence: E2f1 Isoforms Abundance Estimation via Cufflinks.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, TopHat v2.0.9] -> quantification [Cufflinks]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: FPKM (fragments per kilobase of transcript per million fragments mapped) values and differential gene expression were analyzed using Cufflinks ( 32 ) with default settings.
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Version used: **2.0.2**
- Evidence: Fragments per kilobase of exon per million mapped reads for each gene were calculated using Cufflinks (version 2.0.2) software.
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **2.3.1**
- Evidence: For transcriptome-based prediction, RNA-seq data were mapped against the assembly using HISAT2 v2.2.1 ( 77 ), and the transcripts were converted to gene models using Cufflinks v2.3.1 ( 78 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Version used: **2.2.1**
- Evidence: Using Cufflinks v2.2.1 indexed bam files were quantified against the Gencode mouse vM10 assembly and normalized across all 1,369 samples (1,351 cells, 18 negative control wells).
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### IRIS: Discovery of cancer immunotherapy targets arising from pre-mRNA alternative splicing. (PNAS 2023)

- DOI: 10.1073/pnas.2221116120 | PMCID: PMC10214192 | PMID: 37192158
- Version used: **2.2.1**
- Evidence: Gene expression and AS events were quantified using Cufflinks v2.2.1 ( 55 ) and rMATS v4.1.0 under default parameters, respectively, based on the GENCODE (V26) ( 56 ) gene annotation.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [Cufflinks v2.2.1, DESeq2 v1.26.0, featureCounts v2.0.1] -> normalisation [DESeq2 v1.26.0, featureCounts v2.0.1]

### HY5 functions as a systemic signal by integrating BRC1-dependent hormone signaling in tomato bud outgrowth. (PNAS 2023)

- DOI: 10.1073/pnas.2301879120 | PMCID: PMC10120035 | PMID: 37036969
- Version used: **2.1.1**
- Evidence: The transcript abundances were measured as fragments per kilobase of exon per million fragments mapped (FPKM) by Cufflinks 2.1.1.
- Full pipeline: alignment/mapping [Cufflinks v2.1.1] -> quantification [Cufflinks v2.1.1]

### STING-dependent interferon signatures restrict osteoclast differentiation and bone loss in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2210409120 | PMCID: PMC10104545 | PMID: 37023130
- Version used: **2.2.1**
- Evidence: Differential expression analyses between groups were performed using Cuffdiff (Cufflinks v2.2.1).
- Full pipeline: differential/statistical testing [Cufflinks v2.2.1]

### Circadian regulation of hippocampal function is disrupted with corticosteroid treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2211996120 | PMCID: PMC10104554 | PMID: 37023133
- Evidence: The merged BAM files were analyzed for gene expression differences using Tophat2, Cufflinks, and CuffDiff analyses aligning to the Rn6 genome ( 93 ).
- Full pipeline: alignment/mapping [Cufflinks]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **2.2.1**
- Evidence: Then we generated reference-guided and de novo assembled transcript sequences using Cupcake (5.8) with Iso-Seq reads, and StringTie (1.3.3b) ( 77 ) (-m 300 -j 5 -c 8) and Cufflinks (2.2.1) ( 78 ) (–multi-read-correct –max-intron-length 30000) and Trinity (2.6.6) ( 79 ) (--min_glue 10 --path_reinforcement_distance 30 --min_contig_length 400 --jaccard_clip) with RNA-seq reads.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### METTL3 is essential for normal progesterone signaling during embryo implantation via m<sup>6</sup>A-mediated translation control of progesterone receptor. (PNAS 2023)

- DOI: 10.1073/pnas.2214684120 | PMCID: PMC9945998 | PMID: 36693099
- Version used: **2.2.1**
- Evidence: Mapped reads were assembled by using Cufflinks v2.2.1 ( 72 ).
- Full pipeline: alignment/mapping [Cufflinks v2.2.1] -> stage not stated [HOMER v4.7, ImageJ, MACS2, R]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: Trinity ( 80 ), and Cufflinks [ 81 ; following alignment using TopHat2 ( 82 )] were used to generate de novo transcript assemblies.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Quantification was carried out with the Cufflinks package (version 2.2.1).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### BRCA1 and ELK-1 regulate neural progenitor cell fate in the optic tectum in response to visual experience in <i>Xenopus laevis</i> tadpoles. (PNAS 2024)

- DOI: 10.1073/pnas.2316542121 | PMCID: PMC10801852 | PMID: 38198524
- Evidence: Bioinformatic analysis was conducted using STRING (v10; RRID:SCR_005223), Cytoscape (v3.2.1; RRID:SCR_015784) ( https://www.cytoscape.org/ ), ClueGO (v2.1.7; RRID:SCR_005748), PANTHER (RRID: SCR_004869), ENCODE (RRID:SCR_015482), and Cufflinks suite (v2.2.1; RRID:SCR_014597) ( SI Appendix , Methods ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, Cufflinks, Cytoscape, ImageJ]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: Cufflinks was employed to calculate the fragments per kilobase of transcript per million fragments mapped (FPKM).
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Version used: **2.2.1**
- Evidence: The resulting read alignment was assembled using Cufflinks (v.2.2.1) and fold changes, significance values were calculated using DESeq2 (v.1.20.0).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Lipid raft proteomics identify endothelial myosin-9 (MYH9) as a regulator of low-density lipoprotein transcytosis and atherosclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2509315122 | PMCID: PMC12582289 | PMID: 41134623
- Evidence: Cufflinks ( 58 ) was used to assemble and estimate the relative abundances of transcripts at the gene and transcript level.
- Full pipeline: read trimming [HISAT2] -> alignment/mapping [HISAT2] -> quantification [Cufflinks, ImageJ] -> stage not stated [Metascape]

### Concerted transport and phosphorylation of diacylglycerol at ER-PM contact sites regulate phospholipid dynamics during stress. (PNAS 2025)

- DOI: 10.1073/pnas.2421334122 | PMCID: PMC12167946 | PMID: 40455983
- Version used: **2.2.1**
- Evidence: These read alignments (in BAM format) were used for transcript quantification with the cuffdiff program of the Cufflinks version 2.2.1 package ( 85 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Clustal Omega, Cufflinks v2.2.1, R] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [AlphaFold, ilastik]

### Extrinsic induction of apoptosis and tumor suppression via the p53-Reprimo-Hippo-YAP/TAZ-p73 pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2413126122 | PMCID: PMC11831151 | PMID: 39913207
- Version used: **2.2.1**
- Evidence: Sequenced reads from the RNA-seq experiment were aligned using HISAT2 2.1.0, and the transcriptome was assembled using Cufflinks 2.2.1.
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, HISAT2 v2.1.0] -> stage not stated [GSEA]

### Nf2 orchestrates β-arrestin2-biased PTH1R signaling to couple bone mass with skeletal integrity. (PNAS 2026)

- DOI: 10.1073/pnas.2524671123 | PMCID: PMC13273255 | PMID: 42268882
- Evidence: Differential expression analysis was conducted with Cufflinks ( 67 , 69 ).
- Full pipeline: alignment/mapping [TopHat] -> quantification [ImageJ] -> differential/statistical testing [Cufflinks]

### Lack of synergy between AR-targeted therapies and PARP inhibitors in homologous recombination-proficient prostate cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2515790122 | PMCID: PMC12867744 | PMID: 41591905
- Evidence: The VIPER pipeline ( 50 ) was used for STAR alignment to the hg19 genome ( 51 ), read count normalization using Cufflinks ( 52 ) quality control with RSeQC ( 53 ), and differential expression analysis using DESeq2 ( 54 ).
- Full pipeline: quality control [Cufflinks, DESeq2, STAR] -> alignment/mapping [Cufflinks, DESeq2, STAR] -> quantification [CellProfiler, Cufflinks, DESeq2, STAR] -> normalisation [Cufflinks, DESeq2, STAR] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [Cufflinks, DESeq2, STAR]

### Olfactory inputs to appetite neurons in the hypothalamus. (PNAS 2026)

- DOI: 10.1073/pnas.2524926123 | PMCID: PMC12867749 | PMID: 41591908
- Evidence: Sequenced reads were mapped to the mouse genome (mm10) to generate Fragments Per Kilobase of exon per Million mapped fragments (FPKM) using standard methods (Tophat and Cufflinks) ( 63 , 64 ).
- Full pipeline: alignment/mapping [Cufflinks] -> quantification [AnnData v0.10, Cufflinks, Matplotlib v3.8, Scanpy v1.9] -> visualisation [Matplotlib v3.8, Python]

