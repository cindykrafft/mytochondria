# RSEM

- **Category:** genomics
- **Papers in survey:** 132
- **Journals:** PNAS (62), Nature (56), Cell (12), Science (2)
- **Years:** 2021 (17), 2022 (25), 2023 (27), 2024 (23), 2025 (25), 2026 (15)
- **Versions named:** 1.3.1 (17), 1.3.3 (12), 1.3.0 (8), 1.2.28 (2), 1.2.25 (2), 1.2.30 (2), 1.2.15 (2), 1.2.12 (2), 1.2.22 (2), 1.2.21 (1)
- **Pipeline stages it appears in:** quantification (71), alignment/mapping (62), normalisation (29), differential/statistical testing (5), read trimming (4), quality control (4), visualisation (1)

## Papers

### Microenvironment drives cell state, plasticity, and drug response in pancreatic cancer. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.017 | PMCID: PMC8822455 | PMID: 34890551
- Evidence: After running QC checks using RNaseqQC, gene-level count matrices were generated using RSEM.
- Full pipeline: quality control [RSEM] -> alignment/mapping [GATK v1.6] -> registration [GATK v1.6] -> differential/statistical testing [R v4.0] -> stage not stated [Mutect2 v1.1.45, Picard, Python v3.7.4, Seurat v2.3.4]

### Virus-encoded histone doublets are essential and form nucleosome-like structures. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.032 | PMCID: PMC8357426 | PMID: 34297924
- Evidence: Transcript quantification was done using RSEM ( Li and Dewey, 2011 ) (version 1.3.0) and data normalization using the edgeR R package ( Robinson et al., 2010 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [R, RSEM, edgeR] -> normalisation [R, RSEM, edgeR] -> structure determination [PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD v1.9.3]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: ...in et al., 2013 RRID: SCR_015899 CellRanger N/A RRID: SCR_017344 Cutadapt Martin, 2011 RRID: SCR_011841 RNA-SeQC DeLuca et al., 2012 RRID: SCR_005120 RSEM Li and Dewey, 2011 RRID: SCR_013027 Scanpy Wolf et al., 2018 RRID: SCR_018139 Bioconductor R Huber et al., 2015 RRID: SCR_001905 Bioconductor packages edgeR Robinson et al., 2010 RRID: SCR_012802 Resource availability Lead contact Further inform...
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Osteoclasts recycle via osteomorphs during RANKL-stimulated bone resorption. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.002 | PMCID: PMC7938889 | PMID: 33636130
- Evidence: ... SCR_002798 Scanco SCANCO Medical http://www.scanco.ch/ ; RRID: SCR_017119 R R Project for Statistical Computing www.r-project.org ; RRID: SCR_001905 RSEM ( Li and Dewey, 2011 ) https://github.com/deweylab/RSEM ; RRID: SCR_013027 STAR ( Dobin et al., 2013 ) https://github.com/alexdobin/STAR ; RRID: SCR_015899 Vision DXA Faxitron Bioptics/Hologic https://www.faxitron.com/ Other Hypergeometric p val...
- Full pipeline: alignment/mapping [STAR v2.4.1] -> normalisation [STAR v2.4.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [RSEM, STAR v2.4.1] -> stage not stated [Cutadapt, ImageJ, MAGMA, ggplot2]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: Expression counts were normalized using DESeq2 variance stabilizing transformation (vst) function and transcripts per kilobase million (TPM) values calculated using RSEM with default parameters ( Li and Dewey, 2011 ).
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: Expression values from The Cancer Genome Atlas (TCGA) processed and normalized by RNA-Seq by Expectation Maximization (RSEM) are classified according to PAM50.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: (2021) N/A Nfcore/rnaseq pipeline V 3.5 ( Ewels et al., 2020 ) N/A ( Ewels et al., 2020 ) Nextflow domain specific language V 19.10.0 ( Di Tommaso et al., 2017 ) N/A ( DI Tommaso et al., 2017 ) Singularity V 2.6.0 ( Kurtzer et al., 2017 ) N/A( Kurtzer et al., 2017 ) RSEM-STAR Dobin et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Version used: **1.2.22**
- Evidence: ...eneious.com/download/ bwa-mem Li and Durbin, 2009 http://maq.sourceforge.net/ RepeatMasker Institute for Systems Biology http://www.repeatmasker.org/ RSEM (v1.2.22) Li and Dewey, 2011 http://deweylab.github.io/RSEM/ STAR aligner software (2.5.1b) ENCODE https://www.encodeproject.org/software/star/ Prism Graphpad, https://www.graphpad.com/scientific-software/prism version 8.2.1 R R Core Team and R ...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Arginine reprograms metabolism in liver cancer via RBM39. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.011 | PMCID: PMC10642370 | PMID: 37804830
- Evidence: We computed the log 2 -fold-changes of normalized RSEM gene counts between tumors and the matched non-tumor livers for downstream analysis.
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ, R] -> normalisation [RSEM] -> differential/statistical testing [STAR, limma]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 50 https://bioconductor.org/packages/release/bioc/html/limma.html pheatmap R Kolde 51 https://www.rdocumentation.org/packages/pheatmap/versions/1.0.12/topics/pheatmap Prism 10 GraphPad software https://www.graphpad.com/scientific-software/prism RSEM tool Li and Dewey 52 https://deweylab.github.io/RSEM/ scVelo Bergen et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Version used: **1.2.22**
- Evidence: ...//maq.sourceforge.net/ Ensembl (V109) Ensembl www.ensembl.org UCSC Genome Browser UCSC www.genome.ucsc.edu GENCODE (V43) GENCODE www.gencodegenes.org RSEM (v1.2.22) Li and Dewey 94 http://deweylab.github.io/RSEM/ STAR aligner software (2.5.1b) ENCODE https://www.encodeproject.org/software/star/ DAVID v6.8 Huang da et al.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 38 https://github.com/loosolab/TOBIAS ; RRID: N/A Oligo software (Mac v7) Molecular Biology Insights https://www.oligo.net/ ; RRID: N/A RSEM algorithm Li and Dewey 89 https://github.com/deweylab/RSEM ; RRID:SCR_000262 Bioconductor edgeR Robinson et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: ...o calculate expression estimates, mRNA-seq reads were mapped with STAR (spliced transcripts alignment to a reference, v.2.4.2a) 64 and processed with RSEM using the ‘single-cell-prior’ option (RNA-seq by expectation-maximization, v.1.2.25) 65 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: RSEM 53 (version 1.3.3) was used to quantify gene expression levels using the reads aligned to transcriptome in bam file as input, with parameters: --alignments --estimate-rspd --calc-ci --no-bam-output --seed 12345 --ci-memory 30000 --paired-end --strandedness reverse.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **1.3.3**
- Evidence: ...oordinates into transcriptomic coordinates using the STAR parameter –quantMode TranscriptomeSAM; and quantified isoform and gene expression using the RSEM v1.3.3 parameters (RSEM, RRID:SCR_013027) –bam–seed 12345–paired-end–forward-prob 0.5–single-cell-prior–calc-ci.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Biologically informed deep neural network for prostate cancer discovery. (Nature 2021)

- DOI: 10.1038/s41586-021-03922-4 | PMCID: PMC8514339 | PMID: 34552244
- Evidence: STAR-aligned bam files were passed into RSEM to generate gene-level transcript counts and transcript per million (TPM) quantifications using the GENCODE release 30 gene annotation lifted over to GRCh37.
- Full pipeline: read trimming [Cutadapt v2.2, STAR] -> alignment/mapping [Cutadapt v2.2, RSEM, STAR] -> quantification [RSEM] -> stage not stated [SAMtools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: Basal-normalized transcript expression data (z score) used for this analysis were RNA Seq V2 RSEM.
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Version used: **1.3.1**
- Evidence: Sorted bam files generated in the 2-STAR pass alignment described above where supplied to RSEM version 1.3.1 to count transcripts.
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Arterialization requires the timely suppression of cell growth. (Nature 2021)

- DOI: 10.1038/s41586-020-3018-x | PMCID: PMC7116692 | PMID: 33299176
- Version used: **1.2.30**
- Evidence: Resulting reads were mapped against mouse transcriptome GRCm38.76, and gene expression levels were estimated with RSEM v.1.2.30 36 .
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5] -> alignment/mapping [RSEM v1.2.30] -> normalisation [limma v3.32.10] -> differential/statistical testing [limma v3.32.10] -> stage not stated [GSEA, ImageJ]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **1.2.30**
- Evidence: The expression values of each gene were quantified as transcripts per million (TPM), as well as raw counts, using RSEM (v.1.2.30) 56 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Evidence: RSEM 89 expressions were already log2-transformed and quantile normalized.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: Finally, RSEM 50 (v1.3.0) was used for quantification (Gencode 51 release 25lift37) to obtain expected read counts at the gene and transcript levels.
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### Nociceptor neurons affect cancer immunosurveillance. (Nature 2022)

- DOI: 10.1038/s41586-022-05374-w | PMCID: PMC9646485 | PMID: 36323780
- Evidence: Gene expression levels were obtained both as a read count directly from STAR and computed using RSEM to obtain normalized gene and transcript level expression, in TPM values, for these stranded RNA libraries.
- Full pipeline: read trimming [STAR v2.5.1b, Trimmomatic v0.35] -> alignment/mapping [STAR v2.5.1b, Trimmomatic v0.35, featureCounts] -> quantification [Bioconductor, RSEM] -> normalisation [Bioconductor, RSEM] -> dimensionality reduction/clustering [R] -> stage not stated [DESeq2 v1.18.1, ImageJ]

### Post-translational control of beige fat biogenesis by PRDM16 stabilization. (Nature 2022)

- DOI: 10.1038/s41586-022-05067-4 | PMCID: PMC9433319 | PMID: 35978186
- Version used: **1.2.15**
- Evidence: The reads were mapped to the latest UCSC transcript set using Bowtie2 v.2.1.0 and the gene expression level was estimated using RSEM (v.1.2.15) 41 .
- Full pipeline: read trimming [edgeR, fastp v0.20.1] -> alignment/mapping [Bowtie2 v2.1.0, RSEM v1.2.15] -> quantification [Salmon v1.4.0] -> normalisation [edgeR] -> stage not stated [Enrichr]

### Truncated FGFR2 is a clinically actionable oncogene in multiple cancers. (Nature 2022)

- DOI: 10.1038/s41586-022-05066-5 | PMCID: PMC9436779 | PMID: 35948633
- Version used: **1.3.0**
- Evidence: STAR (v.2.7.3a) 84 and RSEM (v.1.3.0) 100 were used for gene and transcript quantification using the default parameters.
- Full pipeline: read trimming [edgeR v3.26.6] -> alignment/mapping [BWA v0.7.5a, STAR v2.7.2] -> quantification [RSEM v1.3.0, edgeR v3.26.6, featureCounts v1.6.2] -> normalisation [edgeR v3.26.6] -> differential/statistical testing [R, limma v3.52.1]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Version used: **1.3.3**
- Evidence: Gene level quantification and normalization was using RSEM (v1.3.3) 45 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Signatures of copy number alterations in human cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04738-6 | PMCID: PMC9242861 | PMID: 35705804
- Evidence: To test associations between promoter hypermethylation of the HR machinery and CN17, TCGA methylation β values were downloaded from https://portal.gdc.cancer.gov/ and TCGA-normalized gene expression RSEM values were downloaded from https://gdac.broadinstitute.org/ Relationships between log 10 (RSEM) values and mean TSS200 and TSS1500 associated methylation probe β values were initially inspected i...
- Full pipeline: normalisation [RSEM] -> stage not stated [Beagle v5.1, ComplexHeatmap, R, ggplot2, survival (R), tidyverse]

### Genetic instability from a single S phase after whole-genome duplication. (Nature 2022)

- DOI: 10.1038/s41586-022-04578-4 | PMCID: PMC8986533 | PMID: 35355016
- Evidence: The normalized mRNA expression (Illumina HiSeq_RNASeqV2, RSEM) from pan cancer studies were downloaded from https://www.cbioportal.org/ : detailed information about RNA sequencing experiment and tools used can be found at the NCI’s Genomic Data Commons (GDC) portal https://gdc.cancer.gov .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.4] -> normalisation [RSEM] -> stage not stated [Bioconductor, GSEA, ImageJ]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Version used: **1.3.1**
- Evidence: RNA-seq reads were mapped to the human (hg38) using STAR v2.7.3a following ENCODE standard options, read counts were generated using RSEM v1.3.1, and differential expression analysis was performed in R v4.0.2 using the DESeq2 package v1.28.1 40 .
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Version used: **1.3.3**
- Evidence: TPM estimates were obtained using RSEM v1.3.3 with parameter–single-cell-prior.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Glioma synapses recruit mechanisms of adaptive plasticity. (Nature 2023)

- DOI: 10.1038/s41586-023-06678-1 | PMCID: PMC10632140 | PMID: 37914930
- Evidence: For scRNAseq processing of individual biopsy samples, RSEM-normalized gene abundances for the Filbin dataset 36 were downloaded from the Single Cell Portal ( https://singlecell.broadinstitute.org/single_cell , Gene Expression Omnibus (GEO) accession: GSE102130 ).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [ImageJ v2.1.0, RSEM, featureCounts, kallisto] -> normalisation [RSEM] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.36.0] -> visualisation [ImageJ v2.1.0] -> stage not stated [R v4.1.1]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Evidence: Reads were aligned to the mouse genome (Ensembl GRCm38 release 89) using STAR (version 2.5.2a) 51 and gene level counts were obtained using the RSEM package (version 1.3.0) 52 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Platelet factors attenuate inflammation and rescue cognition in ageing. (Nature 2023)

- DOI: 10.1038/s41586-023-06436-3 | PMCID: PMC10468395 | PMID: 37587343
- Version used: **1.3.1**
- Evidence: Alignment of RNA-seq reads to the mouse mm10 transcriptome was performed using STAR (v.2.7.3a) 50 using the ENCODE standard options, read counts were generated using RSEM (v.1.3.1) and differential expression analysis was performed in R (v.3.6.1) using the DESeq2 package (v.1.38.0) 51 (detailed pipeline v.2.0.1 and options are available at GitHub ( https://github.com/emc2cube/Bioinformatics/ )).
- Full pipeline: alignment/mapping [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> quantification [DESeq2, ImageJ, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> stage not stated [Enrichr, Seurat]

### Signalling by senescent melanocytes hyperactivates hair growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06172-8 | PMCID: PMC10284692 | PMID: 37344645
- Version used: **1.2.25**
- Evidence: Gene expression levels were quantified using RSEM v.1.2.25 with expression values normalized into fragments per kilobase of transcript per million mapped reads (FPKM).
- Full pipeline: alignment/mapping [RSEM v1.2.25, STAR v2.4.2a] -> quantification [RSEM v1.2.25] -> normalisation [RSEM v1.2.25] -> dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [edgeR v3.2.2] -> stage not stated [Metascape]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Evidence: Single-cell gene expression analysis Quantification of total gene expression We calculated the TPM for each gene using RSEM ( https://deweylab.github.io/RSEM/ ) with rsem-calculate-expression.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **1.3.3**
- Evidence: The mpmap-RPVG pipeline was compared with Salmon (v.1.9.0) 131 and RSEM (v.1.3.3) 132 .
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **1.3.3**
- Evidence: RSEM (v.1.3.3) 60 was used with default parameters to quantify gene expression from the BAM files aligned to the transcriptome.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Version used: **1.3.1**
- Evidence: RSEM (v.1.3.1) was used to calculate estimated read counts per gene and to quantify a measure of TPM 68 .
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### The dietary sweetener sucralose is a negative modulator of T cell-mediated responses. (Nature 2023)

- DOI: 10.1038/s41586-023-05801-6 | PMCID: PMC10033444 | PMID: 36922598
- Version used: **1.3.1**
- Evidence: Reads were mapped and subsequent gene-level counted using RSEM 1.3.1 (ref.
- Full pipeline: read trimming [Cutadapt v2.10, DADA2 v1.18] -> alignment/mapping [Cutadapt v2.10, RSEM v1.3.1] -> stage not stated [DESeq2 v1.30, R v4.0, STAR v2.7.6, phyloseq]

### Non-viral precision T cell receptor replacement for personalized cell therapy. (Nature 2023)

- DOI: 10.1038/s41586-022-05531-1 | PMCID: PMC9768791 | PMID: 36356599
- Evidence: RNA-seq sequences were mapped to the human genome, quantified and normalized using STAR and RSEM 55 .
- Full pipeline: alignment/mapping [BWA, RSEM] -> quantification [RSEM] -> normalisation [RSEM] -> stage not stated [Mutect2]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: 39 , we subset the data to cells labelled ‘fetal’ and estimated transcripts per million reads for each gene in each cell using RSEM 93 given the STAR 94 mapping results.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: Highly and lowly expressed genes were defined as those with mean RSEM value in the top 25% and bottom 75% of protein-coding genes in TCGA CRC samples with RNA sequencing 7 .
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### A maternal brain hormone that builds bone. (Nature 2024)

- DOI: 10.1038/s41586-024-07634-3 | PMCID: PMC11306098 | PMID: 38987585
- Version used: **1.2.21**
- Evidence: Trimmed reads were then mapped to the mouse genome (v.M20) using STAR (v.2.4), and counts for gene and transcript reads were calculated using RSEM (v.1.2.21).
- Full pipeline: read trimming [RSEM v1.2.21, STAR v2.4] -> alignment/mapping [RSEM v1.2.21, STAR v2.4, kallisto] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy v1.9, scDblFinder]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Evidence: The libraries were sequenced and transcripts per million (TPM) for each gene were generated using RSEM 70 post-alignment with STAR 71 .
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Hypoblast from human pluripotent stem cells regulates epiblast development. (Nature 2024)

- DOI: 10.1038/s41586-023-06871-2 | PMCID: PMC10849967 | PMID: 38052228
- Version used: **1.3.1**
- Evidence: We used the Cell Ranger pipeline (v.3.1.0, 10x Genomics) for all human 10x Genomics single-cell datasets and STAR aligner (v.2.5.1b) and RSEM (v.1.3.1) tool for Smart-Seq datasets.
- Full pipeline: quality control [Seurat] -> read trimming [Cutadapt v1.15, TopHat] -> alignment/mapping [RSEM v1.3.1, STAR, TopHat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Evidence: Differential expression analysis RNA-seq reads were aligned to the reference genome (hg38 or mm10) using STAR aligner, followed by transcript quantification with RSEM.
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **1.3.1**
- Evidence: Raw sequencing data were processed using Cell Ranger (v.2.2, 10x Genomics) for 10x data and with STAR aligner (v.2.6.1a), skewer (v.0.2.2), RSEM (v.1.3.1) and HTSEQ (v.2.0) for SS2 data.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Resulting reads were mapped to the reference transcriptome GRCm38.102 using STAR 71 and gene expression levels were estimated using RSEM 72 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Version used: **1.2.28**
- Evidence: For each sample, the transcripts per million (TPM) were calculated for genes annotated in Ensembl v93 (filtered using the build steps in Cell Ranger Human reference 3.0.0, GRCh38) using RSEM (v1.2.28, rsem-calculate-expression).
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: The mRNA levels were calculated from RNA-sequencing read counts using RNA-Seq V2 RSEM and normalized to TPM.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Version used: **1.3.3**
- Evidence: RNA sequencing analysis Reads were aligned to the GRCh38 genome using STAR (v2.7), and the transcripts were quantified with RSEM (v1.3.3).
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Tumour-wide RNA splicing aberrations generate actionable public neoantigens. (Nature 2025)

- DOI: 10.1038/s41586-024-08552-0 | PMCID: PMC11903331 | PMID: 39972144
- Evidence: Transcript-level expression data (log 2 [RSEM transcripts per million + 0.001]) for all TCGA samples were downloaded from the University of California, Santa Cruz Xena Toil pipeline and transformed into standard TPM values.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, R, RSEM] -> differential/statistical testing [DESeq2, GSEA, R] -> stage not stated [AlphaFold v2.3.2, Picard]

### Intrinsic electrical activity drives small-cell lung cancer progression. (Nature 2025)

- DOI: 10.1038/s41586-024-08575-7 | PMCID: PMC11922742 | PMID: 39939778
- Evidence: Illumina HiSeq 2000 50-nt single-ended reads were mapped to the UCSC mm9 mouse genome build ( http://genome.ucsc.edu/ ) using RSEM 80 (v.1.2.12) and bowtie (v.1.0.1) with default options.
- Full pipeline: alignment/mapping [RSEM] -> machine learning [Cellpose, TrackMate] -> visualisation [QuPath v0.5.0] -> stage not stated [Enrichr, GSEA, ImageJ]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Version used: **1.3.1**
- Evidence: In brief, RNA-seq data were aligned to the human reference genome (hg19) and transcriptome (GENCODE v.19) using STAR (v.2.6.1) 68 , and expression was quantified (transcripts per million) using RSEM (v.1.3.1) 69 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### SKI complex loss renders 9p21.3-deleted or MSI-H cancers dependent on PELO. (Nature 2025)

- DOI: 10.1038/s41586-024-08509-3 | PMCID: PMC11864980 | PMID: 39910293
- Evidence: Next, RNA-SeQ2 and RSEM were run to obtain quality metrics and produce an expected counts matrix ( https://github.com/broadinstitute/depmap_omics/blob/44518acd555e948df66178509ca1feb6c22c8b49/RNA_pipeline/RNA_stranded_rsem_rnaseqc2.wdl ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [ImageJ v1.53k, Picard, RSEM, SciPy]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: Sequencing reads were aligned to the GRCh38 genome (hg38) using the STAR aligner (v2.7.11b) with a pre-built RSEM index 65 .
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: Gene expression levels were quantified with RSEM by calculating uniquely mapped reads as transcripts per million (TPM).
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Version used: **1.3.0**
- Evidence: We aligned raw sequencing reads to hg19 genome by hisat2 (v.2.1.0) and quantified gene counts using RSEM (v.1.3.0) as raw counts.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Version used: **1.3.0**
- Evidence: In short, reads were aligned against the GRCh38 reference genome, which included the EBV sequence NC_007605.1 , and EBV transcripts were quantified using RSEM (v1.3.0).
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: RNA expression data from TCGA, quantified as RNA-seq by expectation maximization (RSEM) values, underwent log 2 (RSEM + 1) transformation for scaling.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Reduced cyclin D3 expression in erythroid cells protects against malaria. (Nature 2026)

- DOI: 10.1038/s41586-026-10110-9 | PMCID: PMC12999499 | PMID: 41708853
- Evidence: RNA-seq reads were aligned using STAR software (v.2.7.10b) 61 against a transcriptome reference generated by RSEM software (v.1.3.1) 62 .
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [ImageJ] -> differential/statistical testing [VCFtools v0.1.12b] -> stage not stated [MACS2]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: RNA-seq data generated were aligned to the mouse reference genome using bowtie and analysed using the RSEM software package with default parameters.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **1.3.1**
- Evidence: Gene expression levels were quantified using RSEM (v.1.3.1) 68 .
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **1.3.0**
- Evidence: The reads were mapped to the human genome (hg38) with Gencode v.25 annotations using STAR (v.2.5.2b) 110 and gene expression was quantified using RSEM (v.1.3.0) 111 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Evidence: For gene-expression analysis in normal and cancer tissue, RSEM-normalized expression data from the TCGA TARGET GTEx cohort ( n = 19,109) were retrieved from the UCSC Xena platform 79 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: Categorization of genes by expression levels Gene-level expected counts were estimated using the RSEM package from alignment BAM files and normalized using the NOIseq R package into reads per kb per million mapped reads (RPKM) values.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **1.3.1**
- Evidence: RSEM (v.1.3.1) was used to quantify expression levels against the mouse genome reference GRCm38 or the human genome reference GRCh38, depending on the analysis 57 (default options).
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Expression data were obtained from the batch-normalized RSEM (RNA-seq by Expectation-Maximization) values from TCGA-LIHC after log 2 transformation with a pseudo-count of 1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Evidence: Fastq files were aligned to mm10 mouse reference genome (GRCm38.39) and per-gene counts quantified by RNA-Seq by Expectation-Maximization (RSEM) (version 1.3.1) based on the gene annotation Mus_musculus.GRCm38.89.chr.gtf.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: The cleaned RNA-seq reads (taken from above de novo transcriptome assembly) were aligned to the gene set by Bowtie ( 70 ) (version 2.2.5), and gene expression levels were estimated by RNA-seq by Expectation Maximization (RSEM) ( 71 ) (version 1.2.12).
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: Reads were mapped using Bowtie 2 within the RSEM package, which was also used to quantify transcript abundance ( 79 ).
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Evidence: Cleaned short reads were aligned to reference genome TAIR10 by Bowtie2 ( 56 ), and expression abundance was calculated by RSEM with default parameters ( 57 ).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### Sex pheromone communication in an insect parasitoid, <i>Campoletis chlorideae</i> Uchida. (PNAS 2022)

- DOI: 10.1073/pnas.2215442119 | PMCID: PMC9894188 | PMID: 36442117
- Version used: **1.2.15**
- Evidence: RSEM v1.2.15 was used to calculate the FPKM (fragments per kilobase of exon model per million mapped fragments).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM v1.2.15] -> quantification [RSEM v1.2.15] -> stage not stated [BLAST]

### Somatic 9p24.1 alterations in HPV<sup>-</sup> head and neck squamous cancer dictate immune microenvironment and anti-PD-1 checkpoint inhibitor activity. (PNAS 2022)

- DOI: 10.1073/pnas.2213835119 | PMCID: PMC9704728 | PMID: 36395141
- Evidence: Gene expression files were obtained from RSEM analysis (level 3).
- Full pipeline: stage not stated [RSEM]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: We calculated the expression (fragments per kilobase per million mapped fragments [FPKM]) of each transcript with RSEM ( 70 ) for each individual.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Combination of common mtDNA variants results in mitochondrial dysfunction and a connective tissue dysregulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212417119 | PMCID: PMC9659340 | PMID: 36322731
- Evidence: Eighteen Human Tourette RNA-sequencing Fastq files, consisting of 6 controls and 12 mutant samples, were processed using the STAR alignment ( 42 ) tool and subsequently normalized using the RSEM ( 43 ) package based upon the hg38 reference genome ( 44 ) and the Gencode version 23 gene annotation ( 45 ).
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [R, limma] -> stage not stated [GSEA]

### Ovarian cancer cell fate regulation by the dynamics between saturated and unsaturated fatty acids. (PNAS 2022)

- DOI: 10.1073/pnas.2203480119 | PMCID: PMC9564215 | PMID: 36197994
- Evidence: Recomputed RNA-Seq by Expectation Maximization (RSEM) expected counts of fallopian tube samples (GTEx) and primary tumor samples from TCGA OC patients were downloaded from the University of California, Santa Cruz (UCSC) Xena Browser.
- Full pipeline: normalisation [GSEA] -> differential/statistical testing [ImageJ, edgeR] -> stage not stated [RSEM]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: Transcript abundance of individual transcriptome datasets are referring to transcripts per million determined by the Trinity pipeline ( 74 ) 2.4.0 (Trinity script ‘align_and_estimate_abundance.pl’) via RSEM ( 75 ) ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **1.3.3**
- Evidence: Expression of the KR01 HLI genes not on duplicated scaffolds ( SI Appendix ) over time under HL and control light conditions was quantified using RSEM v1.3.3 ( 52 ) (--paired-end --bowtie2 --strandedness reverse --estimate-rspd --sort-bam-by-coordinate; using bowtie2 v2.3.5.1).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### MITF deficiency accelerates GNAQ-driven uveal melanoma. (PNAS 2022)

- DOI: 10.1073/pnas.2107006119 | PMCID: PMC9172632 | PMID: 35512098
- Evidence: Z scores were calculated for each queried gene across each patient in the “mRNA expression, RSEM, batch normalized from the Illumina HiSeq_RNAseqV2 RNA-sequencing” dataset.
- Full pipeline: quantification [QuPath] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2 v1.30.1, R v4.0.3] -> differential/statistical testing [Cytoscape] -> visualisation [GSEA]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: RNASeq fastq files were processed using the Spliced Transcripts Alignment to a Reference (STAR) alignment tool and subsequently normalized using the RNA-Seq by Expectation-Maximization (RSEM) package based upon the mm10 reference genome and the gencode version M17 gene annotation.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### Leg length and bristle density, both necessary for water surface locomotion, are genetically correlated in water striders. (PNAS 2022)

- DOI: 10.1073/pnas.2119210119 | PMCID: PMC8892508 | PMID: 35193982
- Evidence: The read count for each transcript was calculated using RSEM ( 60 ).
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [DESeq2, RSEM] -> differential/statistical testing [DESeq2] -> structure determination [MUSCLE] -> stage not stated [RAxML]

### A peptide toxin in ant venom mimics vertebrate EGF-like hormones to cause long-lasting hypersensitivity in mammals. (PNAS 2022)

- DOI: 10.1073/pnas.2112630119 | PMCID: PMC8851504 | PMID: 35131940
- Evidence: Estimates of transcript abundance were made using the RSEM ( 48 ) plugin of Trinity (align_and_estimate_abundance).
- Full pipeline: alignment/mapping [MAFFT v7.304b, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE v2.0.6] -> stage not stated [BLAST]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Version used: **1.2.12**
- Evidence: RSEM v1.2.12 software ( 77 ) was used to estimate read counts using gene information from Ensembl transcriptome version GRCh37.p13.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### p53 deficient breast cancer cells reprogram preadipocytes toward tumor-protective immunomodulatory cells. (PNAS 2023)

- DOI: 10.1073/pnas.2311460120 | PMCID: PMC10756271 | PMID: 38127986
- Evidence: TCGA RNA-Seq expression profiles were downloaded from the cBioPortal website [(mRNA Expression, RSEM (Batch normalized from Illumina HiSeq_RNASeqV2), https://www.cbioportal.org/ ] or from the UCSC Xena Browser.
- Full pipeline: quantification [ImageJ] -> normalisation [RSEM] -> machine learning [MACS2] -> stage not stated [GSEA, Metascape, R v4.0.2]

### A transcriptional program underlying the circannual rhythms of gonadal development in medaka. (PNAS 2023)

- DOI: 10.1073/pnas.2313514120 | PMCID: PMC10756274 | PMID: 38109538
- Version used: **1.2.12**
- Evidence: Clean reads were mapped on the Oryzias latipes reference assembly using bowtie2 (version 2.2.5), and the fragments per kilobase of exon per million fragments mapped (FPKM) were calculated using RSEM (version 1.2.12).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5, RSEM v1.2.12] -> quantification [Bowtie2 v2.2.5, RSEM v1.2.12] -> stage not stated [BLAST, DIAMOND, Metascape v3.5, R v3.5]

### Evidence for an ancient aquatic origin of the RNA viral order &lt;i&gt;Articulavirales&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2310529120 | PMCID: PMC10636315 | PMID: 37906647
- Version used: **1.3.0**
- Evidence: Read abundance was estimated using RSEM v.1.3.0 ( 50 ) implemented in Trinity v.2.5.1 ( 51 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.490, MUSCLE v5.1] -> quantification [RSEM v1.3.0] -> visualisation [R v4.1] -> stage not stated [BLAST v2.0.9]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: Gene expression levels of genes were estimated using RNA-seq by expectation-maximization (RSEM) ( 78 ) and normalized using FPKM (fragments per kilobase of transcript per million mapped reads).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Cooperative regulation of coupled oncoprotein synthesis and stability in triple-negative breast cancer by EGFR and CDK12/13. (PNAS 2023)

- DOI: 10.1073/pnas.2221448120 | PMCID: PMC10515179 | PMID: 37695916
- Version used: **1.2.25**
- Evidence: The TPM (transcripts per million) was computed for each mapped gene and synthetic spike-in RNA using RSEM v1.2.25 ( 89 ).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [RSEM v1.2.25, STAR v2.4.1a] -> quantification [ImageJ, RSEM v1.2.25] -> differential/statistical testing [DESeq2 v1.22.0] -> stage not stated [Bioconductor]

### IL-7R licenses a population of epigenetically poised memory CD8<sup>+</sup> T cells with superior antitumor efficacy that are critical for melanoma memory. (PNAS 2023)

- DOI: 10.1073/pnas.2304319120 | PMCID: PMC10372654 | PMID: 37459511
- Evidence: ( K ) Scatter plot of TCF7 methylation (beta value) and gene expression (RSEM log2) in cohort of human melanoma samples (72).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, STAR, featureCounts] -> alignment/mapping [STAR, featureCounts] -> quantification [STAR, featureCounts] -> differential/statistical testing [DESeq2, R v4.0] -> stage not stated [RSEM]

### The parasite intraerythrocytic cycle and human circadian cycle are coupled during malaria infection. (PNAS 2023)

- DOI: 10.1073/pnas.2216522120 | PMCID: PMC10268210 | PMID: 37279274
- Version used: **1.3.3**
- Evidence: Each participant's set of Fastq files were aligned to human and parasite genome reference files using STAR (version 2.7.5c) ( 44 ) and quantified using RSEM (version 1.3.3) ( 45 ).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7.5c] -> quantification [RSEM v1.3.3, STAR v2.7.5c]

### Succinyl-CoA ligase ADP-forming subunit beta promotes stress granule assembly to regulate redox and drive cancer metastasis. (PNAS 2023)

- DOI: 10.1073/pnas.2217332120 | PMCID: PMC10266061 | PMID: 37253003
- Evidence: Expression of SUCLA2 mRNA (RNAseq RSEM) and clinical data for each cancer type were downloaded from cBioPortal ( http://cbioportal.org/ ) or firebrowse ( http://firebrowse.org/ ) and Kaplan–Meier plots were generated in R environment using survival packages ( https://cran.r-project.org ).
- Full pipeline: quantification [ImageJ] -> stage not stated [RSEM]

### <i>oskar</i> acts with the transcription factor Creb to regulate long-term memory in crickets. (PNAS 2023)

- DOI: 10.1073/pnas.2218506120 | PMCID: PMC10214185 | PMID: 37192168
- Version used: **1.2.29**
- Evidence: 16 , including removing adapters and reads shorter than 20 nucleotides with Cutadapt v3.4 ( 66 ) and quantifying the gene expression in transcripts per million with RSEM v1.2.29 ( 67 ), using STAR v2.7.0e1 ( 68 ) as read mapper against the G. bimaculatus genome ( 36 ) ( SI Appendix , Table S8 ).
- Full pipeline: read trimming [Cutadapt v3.4, RSEM v1.2.29, STAR v2.7.0e] -> alignment/mapping [MAFFT v7.510] -> quantification [Cutadapt v3.4, ImageJ, RSEM v1.2.29, STAR v2.7.0e] -> visualisation [RAxML]

### Targeting SWI/SNF ATPases in H3.3K27M diffuse intrinsic pontine gliomas. (PNAS 2023)

- DOI: 10.1073/pnas.2221175120 | PMCID: PMC10161095 | PMID: 37094128
- Evidence: The resultant RNA-Seq data were aligned to human reference genome by using Bowtie software and analyzed with the RNA-Seq by Expectation-Maximization (RSEM) software tool.
- Full pipeline: alignment/mapping [RSEM] -> normalisation [MACS2 v3.0.0] -> differential/statistical testing [GSEA]

### Phosphatidylserine-positive extracellular vesicles boost effector CD8<sup>+</sup> T cell responses during viral infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210047120 | PMCID: PMC10120060 | PMID: 37040405
- Version used: **1.3.0**
- Evidence: Expression values (TPM) were calculated with the software package RSEM (version 1.3.0).
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler]

### Interrogating bromodomain inhibitor resistance in KMT2A-rearranged leukemia through combinatorial CRISPR screens. (PNAS 2023)

- DOI: 10.1073/pnas.2220134120 | PMCID: PMC10120025 | PMID: 37036970
- Evidence: RSEM was used to quantify read counts per gene.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [RSEM] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GATK v4.1.2.0, GSEA]

### On the origin of appetite: GLWamide in jellyfish represents an ancestral satiety neuropeptide. (PNAS 2023)

- DOI: 10.1073/pnas.2221493120 | PMCID: PMC10104569 | PMID: 37011192
- Evidence: Values of read count data of each gene were calculated using RNA-Seq by Expectation Maximization (RSEM) ( 45 ) with the default setting implemented in Trinity.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [R, RSEM] -> dimensionality reduction/clustering [R] -> differential/statistical testing [edgeR] -> stage not stated [InterProScan v5.52]

### Losartan controls immune checkpoint blocker-induced edema and improves survival in glioblastoma mouse models. (PNAS 2023)

- DOI: 10.1073/pnas.2219199120 | PMCID: PMC9963691 | PMID: 36724255
- Version used: **1.2.19**
- Evidence: Gene expression levels were quantified as transcripts-per-million (TPM) by running RSEM (v1.2.19) in paired-end mode.
- Full pipeline: quantification [RSEM v1.2.19] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [survival (R)] -> visualisation [UMAP] -> stage not stated [ImageJ, R, Seurat v4.0.0, seaborn v0.9.0]

### The lncRNA LUCAT1 is elevated in inflammatory disease and restrains inflammation by regulating the splicing and stability of NR4A2. (PNAS 2023)

- DOI: 10.1073/pnas.2213715120 | PMCID: PMC9910463 | PMID: 36577072
- Version used: **1.3.1**
- Evidence: Remaining reads were aligned to the human genome (assembly GRCh38/hg38) using STAR v2.6.1 ( 63 ), and reads were counted using RSEM v1.3.1.
- Full pipeline: read trimming [Cutadapt, minimap2 v2.17] -> alignment/mapping [RSEM v1.3.1, STAR v2.6.1, minimap2 v2.17] -> stage not stated [Bioconductor v3.14]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: Heatmaps were plotted with pheatmap either using rlog-normalized expression values from RSEM-normalized data.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Version used: **1.3.1**
- Evidence: To quantify transcript levels in each RNA-seq dataset for all genes in the NCBI annotation set (with BcTPS5 added in), RSEM (v1.3.1) ( 61 ) was used with STAR (version 2.7.10a_alpha_220818) ( 60 ) using the “rsem-calculate-expression” pipeline.
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: For RNA quantification, RSEM ( 54 ) was employed to normalize raw read counts, transforming them into TPM (transcripts per million) values, providing a relative expression level that is theoretically comparable across samples.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### Conserved 5-methyluridine tRNA modification modulates ribosome translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2401743121 | PMCID: PMC11363252 | PMID: 39159370
- Version used: **1.3.3**
- Evidence: Reads were mapped to the reference genome Saccharomyces_cerevisiae (ENSEMBL) using STAR v2.7.8a and assigned count estimates to genes with RSEM v1.3.3 ( 58 , 59 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.3] -> alignment/mapping [RSEM v1.3.3, STAR v2.7.8a] -> differential/statistical testing [DESeq2]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **1.3.0**
- Evidence: The abundance of the remaining reads (i.e., non-rRNA reads) was estimated using RSEM v.1.3.0 ( 55 ) implemented in Trinity v.2.5.1 ( 25 ).
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### IFIH1 (MDA5) is required for innate immune detection of intron-containing RNA expressed from the HIV-1 provirus. (PNAS 2024)

- DOI: 10.1073/pnas.2404349121 | PMCID: PMC11260138 | PMID: 38985764
- Version used: **1.3.1**
- Evidence: Quantification of human gene expression was performed on the DolphinNext platform ( 127 ) using RSEM (v1.3.1) software’s rsem-calculate-expression command, utilizing Star aligner (v2.6.1) and human genome version hg38 (Gencode v34 transcript set).
- Full pipeline: alignment/mapping [RSEM v1.3.1] -> quantification [RSEM v1.3.1] -> dimensionality reduction/clustering [limma v3.46.0] -> differential/statistical testing [DESeq2 v1.30.1]

### Intratumoral NKT cell accumulation promotes antitumor immunity in pancreatic cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2403917121 | PMCID: PMC11260137 | PMID: 38980903
- Evidence: In general, FastQC, STAR, featurecounts, RSEM, and GSEA were used for data analysis with the standard setting.
- Full pipeline: quality control [FastQC, RSEM] -> stage not stated [GSEA, ImageJ, MACS2]

### AMBRA1 levels predict resistance to MAPK inhibitors in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2400566121 | PMCID: PMC11194594 | PMID: 38870061
- Evidence: For the correlation analysis between AMBRA1 and NGFR, AXL, and MITF expression, RSEM normalized mRNA data were downloaded from TCGA-SKCM samples (n = 448) through R studio using “TCGAbiolink” package ( 47 ).
- Full pipeline: normalisation [RSEM] -> stage not stated [GSEA, ImageJ v1.52]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: The transcriptomes were mapped using Bowtie2, and the fragments were counted and normalized to fragments per kilobase per million reads using RSEM ( 121 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### A sodium-dependent trehalose transporter contributes to anhydrobiosis in insect cell line, Pv11. (PNAS 2024)

- DOI: 10.1073/pnas.2317254121 | PMCID: PMC10998604 | PMID: 38551840
- Version used: **1.3.1**
- Evidence: Gene expression was quantified using RSEM v1.3.1 (--bowtie2) ( 78 ) and the following downstream analysis was performed using the Trinity package v2.15.1 (abundance_estimates_to_matrix.pl, run_DE_analysis.pl) ( 79 ).
- Full pipeline: quantification [Bowtie2, RSEM v1.3.1] -> stage not stated [HMMER, ImageJ v1.53t]

### Activation of polyamine catabolism promotes glutamine metabolism and creates a targetable vulnerability in lung cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2319429121 | PMCID: PMC10990097 | PMID: 38513095
- Version used: **1.3.3**
- Evidence: Gene-level quantification was counted by RSEM version1.3.3 with the parameter configuration “--paired-end --alignments,” based on bam files obtained from STAR alignment ( 60 ).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.4.2a] -> quantification [RSEM v1.3.3] -> differential/statistical testing [DESeq2, R] -> stage not stated [Metascape]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: Differently expressed genes were analyzed using RSEM ( 55 ) and edgeR ( 56 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Pathogenic GATA2 genetic variants utilize an obligate enhancer mechanism to distort a multilineage differentiation program. (PNAS 2024)

- DOI: 10.1073/pnas.2317147121 | PMCID: PMC10927522 | PMID: 38422019
- Evidence: Center , mRNA levels (TPM) in Lin − progenitors calculated using RSEM ( 68 ).
- Full pipeline: quantification [RSEM] -> stage not stated [GSEA]

### TM4SF19 controls GABP-dependent <i>YAP</i> transcription in head and neck cancer under oxidative stress conditions. (PNAS 2024)

- DOI: 10.1073/pnas.2314346121 | PMCID: PMC10873613 | PMID: 38315837
- Evidence: TCGA data of different types of cancer were obtained from cBioPortal and normalized using RNA-Seq by Expectation-Maximization (RSEM) ( Dataset S1 ).
- Full pipeline: normalisation [RSEM] -> stage not stated [GSEA, ImageJ]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: We accessed the RNA-Seq datasets from the UCSC Xena data hub ( https://toil.xenahubs.net ) using the Xena dataset IDs: TcgaTargetGtex_RSEM_hugo_norm_count.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Disruption of DNA methylation-mediated cranial neural crest proliferation and differentiation causes orofacial clefts in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2317668121 | PMCID: PMC10801837 | PMID: 38194455
- Version used: **1.3.1**
- Evidence: Trimmed and filtered reads were aligned to the Mus musculus genome (mm10) using RSEM v1.3.1 ( 76 ), which utilized STAR v2.7.0 ( 77 ).
- Full pipeline: quality control [FastQC] -> read trimming [RSEM v1.3.1, STAR v2.7.0] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.0] -> variant calling [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### MBNL loss of function in smooth muscle as a model for myotonic dystrophy associated gastrointestinal dysmotility. (PNAS 2025)

- DOI: 10.1073/pnas.2522788122 | PMCID: PMC12718393 | PMID: 41379996
- Evidence: Sequencing results were quality assessed, aligned, normalized, and analyzed using similar methods as previous work ( 124 ) using FastQC version 0.11.9, STAR version 2.7.10b, RSEM algorithm version 1.3.1 ( 125 ), DESeq2 version 1.42.0 for DGE ( 126 ), and rMATS version 4.1.2 for alternative splicing ( 127 ).
- Full pipeline: quality control [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> alignment/mapping [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> variant calling [ImageJ] -> normalisation [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> stage not stated [Metascape]

### A metabolic cell death program downstream of SARM1 couples NAD&lt;sup&gt;+&lt;/sup&gt; depletion to BAX activation and APAF1 degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2522444122 | PMCID: PMC12718333 | PMID: 41364765
- Evidence: RNA-Seq data were analyzed by RSEM as previously described ( 61 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, Trimmomatic] -> quantification [featureCounts] -> stage not stated [RSEM]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: Using the software tool RSEM ( 41 ), the sequencing reads were aligned to the hg38 reference genome and presented as transcripts per million (TPM).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Version used: **1.3.1**
- Evidence: Adapter sequences or poly-A tail from fastq files were trimmed based on fastp, aligned onto genome by STAR (v2.7.10a), and quantified by RSEM (v.1.3.1).
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### Exceptional diversity of allorecognition receptors in a nonvertebrate chordate reveals principles of innate allelic discrimination. (PNAS 2025)

- DOI: 10.1073/pnas.2519372122 | PMCID: PMC12582321 | PMID: 41129228
- Evidence: Raw reads were mapped to FF and FcoR genes using Kallisto and RSEM ( 70 ).
- Full pipeline: alignment/mapping [RSEM, kallisto] -> stage not stated [AlphaFold]

### How to upgrade stolen organelles into permanent plastids: A comparative transcriptomic perspective. (PNAS 2025)

- DOI: 10.1073/pnas.2514821122 | PMCID: PMC12519138 | PMID: 41026821
- Evidence: Read sufficiency using RSEM-based quantification and Bowtie2 mapping showed that more than 88.6% and 89.0% of ODP transcripts were detected with TPM >0.1 from D. capensis and D. kwazulunatalensis , respectively ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM]

### Thalamic CGRP neurons define a spinothalamic pathway for affective pain. (PNAS 2025)

- DOI: 10.1073/pnas.2505889122 | PMCID: PMC12280894 | PMID: 40632570
- Version used: **1.2.28**
- Evidence: The quantification package RSEM (version 1.2.28) was employed to calculate gene expression from BAM files using the default setting changed to pair-end mode.
- Full pipeline: quality control [FastQC] -> quantification [RSEM v1.2.28, ggplot2] -> visualisation [ggplot2]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: Differential gene expression was analyzed by RSEM ( 58 ) and edgeR ( 59 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Expression levels of VzTPS genes were quantified using RSEM, with transcriptome indices built based on VzTPS annotations.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Evidence: RNA-Seq data were analyzed with the STAR-RSEM analysis pipeline implemented in Docker4Seq ( 85 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: To explore the function of Vg genes, gene expression was quantified using STAR ( 108 ) and RSEM ( 109 ).
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: The sequences were aligned to the mm10 genome with the STAR aligner, and gene counts were calculated using RSEM.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **1.3.3**
- Evidence: The high-quality sequences were compared and quantified with RSEM (version 1.3.3) ( 75 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: RSEM ( 64 ) version 1.3.3 with the --forward-prob 0 flag was then used to generate read counts.
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Version used: **1.3.3**
- Evidence: Analyses were performed following the procedure described ( 36 ): Reads were aligned to the GRCh38 genome using STAR (v2.7), and the transcripts were quantified with RSEM (v1.3.3).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Version used: **1.3.0**
- Evidence: Gene-level quantifications using annotation release 86 from Ensembl were generated using RSEM v1.3.0.
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### Identification of antigen-presenting cell-T cell interactions driving immune responses to food. (Science 2025)

- DOI: 10.1126/science.ado5088 | PMCID: PMC12017586 | PMID: 39700315
- Version used: **1.3.1**
- Evidence: Subsequently, genome-mapped BAM files were processed through RSEM (v.
- Full pipeline: alignment/mapping [RSEM v1.3.1, STAR] -> stage not stated [DESeq2, MACS2, R, Seurat v4.1.2]

