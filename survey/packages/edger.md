# edgeR

- **Category:** genomics
- **Papers in survey:** 318
- **Journals:** PNAS (173), Nature (121), Cell (20), Science (4)
- **Years:** 2021 (29), 2022 (61), 2023 (59), 2024 (60), 2025 (76), 2026 (33)
- **Versions named:** 3.36.0 (6), 3.32.1 (6), 3.26.8 (6), 3.30.3 (5), 3.40.2 (4), 3.24.3 (4), 3.42.4 (4), 4.0.16 (3), 4.2.2 (3), 3.34.1 (3)
- **Pipeline stages it appears in:** differential/statistical testing (177), normalisation (98), quantification (46), read trimming (41), alignment/mapping (16), dimensionality reduction/clustering (15), quality control (4), variant calling (3), simulation/modelling (2), visualisation (2), machine learning (1)

## Papers

### Virus-encoded histone doublets are essential and form nucleosome-like structures. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.032 | PMCID: PMC8357426 | PMID: 34297924
- Evidence: Transcript quantification was done using RSEM ( Li and Dewey, 2011 ) (version 1.3.0) and data normalization using the edgeR R package ( Robinson et al., 2010 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [R, RSEM, edgeR] -> normalisation [R, RSEM, edgeR] -> structure determination [PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD v1.9.3]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: We mapped these RNA-seq reads using the same STAR parameters used for the MARS-seq, then transformed raw counts into CPMs using EdgeR ( Robinson et al., 2010 ) and finally averaged expression between replicates.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: ...i and Dewey, 2011 RRID: SCR_013027 Scanpy Wolf et al., 2018 RRID: SCR_018139 Bioconductor R Huber et al., 2015 RRID: SCR_001905 Bioconductor packages edgeR Robinson et al., 2010 RRID: SCR_012802 Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, James E Hudson james.hudson@qimrberghofer.edu...
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Human neutralizing antibodies against SARS-CoV-2 require intact Fc effector functions for optimal therapeutic protection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.026 | PMCID: PMC7879018 | PMID: 33691139
- Evidence: ...wJo FlowJo, LLC v10 GraphPad Prism GraphPad v 9.0.0 Biorender biorender.com N/A flexiWare SCIREQ Inc. v8.1.3 STAR program Dobin et al., 2013 v 2.5.1a EdgeR Robinson et al., 2010 N/A limma Ritchie et al., 2015 N/A RSeQC Liao et al., 2014 v2.6.2 Nanozoomer Digital Pathology Hamamatsu v2 Recombinant DNA Plasmid: rCOV2-2050 in pTwist-mCis_hG1 Zost et al., 2020b N/A Plasmid: rCOV2-2050 in pTwist-mCis_h...
- Full pipeline: quality control [edgeR, limma] -> read trimming [R] -> normalisation [R]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Version used: **3.26.8**
- Evidence: ...kham, 2019 ) https://www.tidyverse.org ComplexHeatmap (2.2.0) Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html edgeR (3.26.8, 3.28.1) McCarthy et al., 2012 https://bioconductor.org/packages/release/bioc/html/edgeR.html FGSEA (1.10.1) Sergushichev, 2016 https://bioconductor.org/packages/release/bioc/html/fgsea.html lme4 (1.1-23) Bates et al., 2015 https://cran...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: The data was processed using the edgeR BioConductor package that was used for outlier detection and differential gene expression analyses.
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **3.36.0**
- Evidence: 3.50.0), edgeR (v.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...t al., 2017 ) https://www.cytosplore.org/ demuxlet ( Kang et al., 2018 ) v2 https://github.com/statgen/demuxlet diffcyt ( Weber et al., 2019 ) v1.8.8 edgeR ( Robinson et al., 2010 ) v3.28.1 https://bioconductor.org/packages/release/bioc/html/edgeR.html EmptyDroplets ( Lun et al., 2019 ) v1.8.0 Entropy ( Hausser, 2009 ) https://strimmerlab.github.io eXploring Genomic Relations (XGR) ( Fang et al., ...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: Read coverage over each gene in the mm9 genome was calculated using Rsubread featurecounts, 85 and differential expression analysis performed using edgeR in RStudio Y.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### Mechanopathology of biofilm-like Mycobacterium tuberculosis cords. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.016 | PMCID: PMC10642369 | PMID: 37865090
- Evidence: Gene expression quantification was performed using R package edgeR.
- Full pipeline: quality control [Bioconductor, FastQC, GSEA, STAR v2.7.10b] -> alignment/mapping [STAR v2.7.10b] -> quantification [R, edgeR] -> stage not stated [ImageJ, MACS2]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Evidence: Briefly, transcript quantification data were summarized to genes using the tximport package and normalized using the trimmed mean of M values (TMM) method in edgeR.
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: To quantify sources of variation in CEV-v1 screens, a matrix of sgRNA counts was assembled as described above and normalized using edgeR 144 calcNormFactors.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Evidence: 38 https://github.com/yanwu2014/swne edgeR Hadjantonakis et al.
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Version used: **3.26.8**
- Evidence: We normalized the datasets with the functions DGEList and calcNormFactors from the edgeR version 3.26.8 package 200 implemented in R v.3.6.3.
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Evidence: 72 The raw counts were processed using EdgeR.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 23 Internal colony Software and algorithms Adobe Illustrator Adobe www.adobe.com BD FACSDiva V8 BD Biosciences http://www.bdbiosciences.com/us/instruments/research/software/flow-cytometry-acquisition/bd-facsdiva-software/m/111112/overview CytExpert Beckman Coulter https://www.beckman.com/flow-cytometry/instruments/cytoflex/software edgeR Robinson et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **4.0.16**
- Evidence: 114 https://software.broadinstitute.org/software/igv/ ggfortify v0.4.11 Tang and Masaaki 115 https://cran.r-project.org/web/packages/ggfortify/index.html DiffBind v2.16.2 Stark and Brown 116 https://hbctraining.github.io/Intro-to-ChIPseq/lessons/08_diffbind_differential_peaks.html EdgeR v4.0.16 Robinson et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 38 https://github.com/loosolab/TOBIAS ; RRID: N/A Oligo software (Mac v7) Molecular Biology Insights https://www.oligo.net/ ; RRID: N/A RSEM algorithm Li and Dewey 89 https://github.com/deweylab/RSEM ; RRID:SCR_000262 Bioconductor edgeR Robinson et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: 188 Differential expression analysis was conducted with DESeq2 174 and/or edgeR.
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **4.2.2**
- Evidence: 207 http://ekhidna2.biocenter.helsinki.fi/dali/ edgeR (v4.2.2) Robinson et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: The matrix was used as input of EdgeR to identify differential interactions with ANOVA tests.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **3.28.1**
- Evidence: For this, inverse scale factors were calculated using EdgeR v3.28.1 (ref.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Identification of SARS-CoV-2 inhibitors using lung and colonic organoids. (Nature 2021)

- DOI: 10.1038/s41586-020-2901-9 | PMCID: PMC8034380 | PMID: 33116299
- Evidence: After further filtering and quality control, R package edgeR 30 was used to calculate RPKM and Log2 counts per million (CPM) matrices as well as perform differential expression analysis.
- Full pipeline: quality control [R, edgeR] -> alignment/mapping [Bowtie2] -> quantification [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, edgeR] -> machine learning [UMAP] -> visualisation [Bowtie2] -> stage not stated [GSEA, Seurat v3.1.0]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **3.30.3**
- Evidence: An overdispersed Poisson model was fitted to each peak using edgeR v3.30.3 (refs.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Maturation and circuit integration of transplanted human cortical organoids. (Nature 2022)

- DOI: 10.1038/s41586-022-05277-w | PMCID: PMC9556304 | PMID: 36224417
- Version used: **3.36.0**
- Evidence: Specifically, the edgeR (version 3.36.0, R package) log-likelihood ratio test was performed between groups on gene counts summed across cells for a given cell class for each sample replicate.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Fiji v2.1.0, ImageJ, R v4.1.2, Seurat v4.1.1, edgeR v3.36.0, scDblFinder]

### Post-translational control of beige fat biogenesis by PRDM16 stabilization. (Nature 2022)

- DOI: 10.1038/s41586-022-05067-4 | PMCID: PMC9433319 | PMID: 35978186
- Evidence: Trimmed mean of M -values (from edgeR) were used to normalize the gene expression.
- Full pipeline: read trimming [edgeR, fastp v0.20.1] -> alignment/mapping [Bowtie2 v2.1.0, RSEM v1.2.15] -> quantification [Salmon v1.4.0] -> normalisation [edgeR] -> stage not stated [Enrichr]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Evidence: Comparison of DE genes between Live-seq and scRNA-seq Differential gene expression analysis was conducted using edgeR 60 v.3.34.0.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### Truncated FGFR2 is a clinically actionable oncogene in multiple cancers. (Nature 2022)

- DOI: 10.1038/s41586-022-05066-5 | PMCID: PMC9436779 | PMID: 35948633
- Version used: **3.26.6**
- Evidence: Read counts for expressed genes were normalized by trimmed mean of M -value (TMM) method using edgeR (v.3.26.6) 98 , 99 .
- Full pipeline: read trimming [edgeR v3.26.6] -> alignment/mapping [BWA v0.7.5a, STAR v2.7.2] -> quantification [RSEM v1.3.0, edgeR v3.26.6, featureCounts v1.6.2] -> normalisation [edgeR v3.26.6] -> differential/statistical testing [R, limma v3.52.1]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Version used: **3.32.1**
- Evidence: Differentially expressed genes were calculated by fitting a quasi-likelihood negative binomial generalized log-linear model as implemented in edgeR (v3.32.1) 63 (false discovery rate (FDR) < 0.15).
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Version used: **3.32.0**
- Evidence: Differential gene expression testing was performed using an NB GLM implemented in the Bioconductor package edgeR (v3.32.0) 52 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Version used: **3.35.1**
- Evidence: Samples obtained after the above steps were then used to detect differentially expressed genes via EdgeR v.3.35.1 (ref.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Evidence: Differentially expressed gene analysis was performed by the ‘EdgeR’ package in R (ref.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Evidence: Differentially abundant clusters were determined using edgeR with a P value significance threshold of 0.05 and log-transformed fold change ≥ 1.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Contrasts between sex and treatment were established (categories = c(DBA_TREATMENT, DBA_CONDITION)), and edgeR 65 was used for differential peak calling.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### TLR7 gain-of-function genetic variation causes human lupus. (Nature 2022)

- DOI: 10.1038/s41586-022-04642-z | PMCID: PMC9095492 | PMID: 35477763
- Evidence: Sequencing was performed using the NextSeq500 platform and analysis was conducted using the following R packages: limma, edgeR and enhanced volcano 49 .
- Full pipeline: dimensionality reduction/clustering [Seurat v4.0.1] -> differential/statistical testing [R, Seurat v4.0.1] -> visualisation [Seurat v4.0.1] -> stage not stated [edgeR, limma]

### CCNE1 amplification is synthetic lethal with PKMYT1 kinase inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-04638-9 | PMCID: PMC9046089 | PMID: 35444283
- Version used: **3.30.3**
- Evidence: Raw counts were processed using the bioconductor package edgeR v3.30.3 in R 60 .
- Full pipeline: quality control [FastQC v0.11.9] -> stage not stated [GSEA, ImageJ v2.0.0, edgeR v3.30.3]

### The cGAS-STING pathway drives type I IFN immunopathology in COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04421-w | PMCID: PMC8891013 | PMID: 35045565
- Version used: **3.26.8**
- Evidence: Subsequently, the TMM normalization step was applied using the package EdgeR (v.3.26.8) 54 .
- Full pipeline: quantification [ImageJ] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [limma v3.40.6] -> stage not stated [Bioconductor]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Version used: **3.34.1**
- Evidence: EdgeR (version 3.34.1) 36 was used to compute differential gene expression using raw read-counts as input.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Gene counts across all samples were merged into one counts matrix using R, and a trimmed mean of M-value (TMM) normalization performed across all samples using the edgeR R package (version 3.32.1) 72 to correct for composition biases and make the transcript counts comparable across all samples 73 , 74 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: ... (v1.16), HISAT2 (v2.1.0) 38 , SAMtools (v1.9) 39 , deepTools 41 (v3.1.0), BEDTools 43 (v2.30.0), data.table (v1.13.2), GenomicFeatures 44 (v1.38.2), edgeR 45 , 46 (v3.28.1), and GAT 47 (v1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: Analogous to species-biased genes, species-biased cCREs are defined as peaks with differential accessibility that are consistently higher in one species compared with in the three other species in the same cell type as identified through differential accessibility analysis performed using EdgeR 26 ( Methods ).
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Plant carbonic anhydrase-like enzymes in neuroactive alkaloid biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-06716-y | PMCID: PMC10700139 | PMID: 37938780
- Evidence: We performed differential expression analysis between samples from new growth leaves (biosynthetically active for HupA production) and mature shoot tissue (inactive for HupA production) using edgeR (ref.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [edgeR] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold v1.5.2, HMMER]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: Differential expression analysis was performed on the count matrix using edgeR with two replicates per condition (with or without 4 h OHT treatment) and differential genes were determined using log-ratio test.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### Distinguishing features of long COVID identified through immune profiling. (Nature 2023)

- DOI: 10.1038/s41586-023-06651-y | PMCID: PMC10620090 | PMID: 37748514
- Evidence: Next, aggregate and clonal enrichment was calculated using edgeR 70 and custom computer scripts.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> visualisation [ComplexHeatmap] -> stage not stated [edgeR, vegan]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Evidence: P-values were calculated with edgeR-LRT with FDR multiple comparison test correction. g .
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: Differential expression testing was performed using the glmLRT function within edgeR and genes were determined as significant if log 2 FC was <1, FDR <0.05 and average log counts per million for the gene was >1.
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Evidence: The edgeR 59 package was used for identifying differentially expressed genes.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### Signalling by senescent melanocytes hyperactivates hair growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06172-8 | PMCID: PMC10284692 | PMID: 37344645
- Version used: **3.2.2**
- Evidence: Differential expression analysis was performed using edgeR v.3.2.2 on protein-coding genes and long non-coding RNAs.
- Full pipeline: alignment/mapping [RSEM v1.2.25, STAR v2.4.2a] -> quantification [RSEM v1.2.25] -> normalisation [RSEM v1.2.25] -> dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [edgeR v3.2.2] -> stage not stated [Metascape]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: The raw read counts of each treatment groups were analysed using edgeR to determine the log 2 fold change between the reads at day 14 relative to day 0.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: The resulting count matrix was analysed in R (v.4.0.5; 31 March 2021) using the edgeR package (v.3.32.1).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### A druggable copper-signalling pathway that drives inflammation. (Nature 2023)

- DOI: 10.1038/s41586-023-06017-4 | PMCID: PMC10131557 | PMID: 37100912
- Version used: **3.30.3**
- Evidence: Counts were normalized using TMM normalization from edgeR (v 3.30.3) 78 .
- Full pipeline: quality control [Nextflow] -> normalisation [R, deepTools, edgeR v3.30.3] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, limma]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **3.36.0**
- Evidence: Transcriptional data analyses Gene level transcription analysis used edgeR (v3.36.0) 47 and limma (v3.50.3) 48 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **3.26.5**
- Evidence: First, trimmed mean of M -values normalization from the edgeR (v.3.26.5) 70 R package was performed on RSEM raw counts.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: A consensus set of loops was then calculated using hicMergeLoops from the HiCExplorer suite 102 and reads were counted in the different replicate 10 kb resolution Hi-C maps to perform the differential loop analysis with EdgeR 103 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Version used: **3.32.1**
- Evidence: Differential gene expression analysis Differential gene expression analysis was performed with limma (limma version 3.46.0, edgeR version 3.32.1) with “cell_or_nucleus” covariate (scRNA-seq or snRNA-seq (including multiome snRNA-seq) origin of each droplet) backwards along the trajectory that was derived using stOrder approach, namely for the following 6 comparisons: VCT-CCC vs VCT (VCT and VCT-p ...
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: The R (3.6.1) package EdgeR 61 (edgeR_3.28.1;limma_3.42.2) was used to identify proteins significantly enriched in NPAS4 or TIP60 immunoprecipitate samples relative to wild-type samples that did not express Flag-tagged proteins.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### mRNA ageing shapes the Cap2 methylome in mammalian mRNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05668-z | PMCID: PMC9891201 | PMID: 36725932
- Evidence: Trimmed mean of M values (TMM) normalization, empirical Bayes estimate of the negative binominal dispersion, and measurement of the changes in gene expression (log 2 fold change) were performed for all samples and replicates at the same time using edgeR 52 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> differential/statistical testing [ImageJ v1.53a] -> visualisation [ImageJ v1.53a] -> stage not stated [BEDTools v2.28.0]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: Differential gene expression analysis Differential RNA expression of genes was tested in R using EdgeR 50 (v.3.28.1) and Limma 51 (including Voom 52 ) (v.3.42.2).
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Version used: **3.34.0**
- Evidence: Then we normalized raw counts across all samples using the calcNormFactors function implemented in the R package edgeR (v.3.34.0), which utilizes the TMM algorithm (weighted trimmed mean of M -values) to compute normalization factors and we log-transformed the data using the voom function from the limma package (v.3.48.3).
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **3.30.0**
- Evidence: Reads per kilobase per million mapped reads (RPKM) and transcripts per million (TPM) gene expression values were calculated from the trimmed mean of M -values (TMM)-normalized counts per million (CPM) values using the Bioconductor package edgeR (v.3.30.0) 64 and R (v.4.0.0) 65 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: Filtering and differential expression testing were performed with edgeR (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Dendritic cells direct circadian anti-tumour immune responses. (Nature 2023)

- DOI: 10.1038/s41586-022-05605-0 | PMCID: PMC9891997 | PMID: 36470303
- Evidence: Differential expression analysis was performed using the R/Bioconductor edgeR package.
- Full pipeline: alignment/mapping [STAR v2.7.0] -> quantification [HTSeq v0.9.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [ImageJ]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: We next used edgeR 96 to iteratively compute DE genes between each organoid differentiation protocol and primary cells of the matching regional neural cell types for every regional neural cell type while correcting for organoid age in days, number of cells per pseudobulk sample, median and standard deviation of the number of detected genes per pseudobulk sample.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: Differential expression analysis was performed using the R package EdgeR 87 , with |log 2 FC| ≥ 1 and nominal P < 0.01 as cut-offs.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: Differential expression analysis from scRNA-seq To find genes differentially expressed between cell clusters or pre-defined populations, a custom pipeline combining edgeR 83 and Seurat’s FindMarkers tool was used.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: For meDIP–seq, differentially methylated regions were identified using MEDIPS 57 with the following settings: diff.method = ‘edgeR’, p.adj = ‘bonferroni’, MeDIP = True, CNV = False, minRowSum = 10.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: We kept samples for analysis that contained at least ten cells, and we used the filterByExpr() function in the edgeR package with default settings to retain genes for differential expression analysis and reduce the burden of multiple test correction, by removing genes with low expression across samples 63 .
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Evidence: Normalization was then performed using calcNormFactors, and differentially expressed genes were determined using edgeR 71 .
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Mitochondrial complex I promotes kidney cancer metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07812-3 | PMCID: PMC11424252 | PMID: 39143213
- Evidence: Differential expression analysis was performed using EdgeR 55 and DESeq 56 .
- Full pipeline: alignment/mapping [STAR v2.7.3] -> differential/statistical testing [DESeq2 v1.14.1, edgeR] -> stage not stated [HTSeq v0.6.1, ImageJ, R, featureCounts]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Evidence: Differential expression analysis was performed using edgeR 108 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Differential expression analysis was performed with edgeR 54 , 55 , comparing each of the induced samples with their uninduced equivalent.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Differential gene expression analysis was performed using edgeR 90 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: To take advantage of robust bulk RNA-seq differential expression frameworks, such as edgeR 118 , in a first step, muscat aggregates measurements for each sample (in each cluster) to obtain pseudobulk data.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Evidence: Count data were normalized using counts per million in the EdgeR package (v.3.40.2) 62 , dimension-reduced through PCA and subjected to heat-map analysis using ComplexHeatmap (v.2.14.0) 63 .
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: Right: log 2 (fold-change) values obtained from edgeR (bottom left of each cell) and from DESeq2 (top right of each cell).
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Differential ATAC–seq analysis was performed as described previously using edgeR and TMM normalization 69 .
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Evidence: Statistical analysis was performed using the EdgeR package 69 .
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: Next, edgeR was used to identify differentially expressed fragments.
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Natural proteome diversity links aneuploidy tolerance to protein turnover. (Nature 2024)

- DOI: 10.1038/s41586-024-07442-9 | PMCID: PMC11153158 | PMID: 38778096
- Evidence: These filtered read counts were then normalized using the trimmed mean of M-values (TMM) method 57 as implemented in edgeR 58 , 59 .
- Full pipeline: read trimming [edgeR] -> quantification [R, edgeR] -> normalisation [edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold, GSEA, STRING db, data.table]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Evidence: Count values were imported and processed using edgeR 44 .
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: The EdgeR package from R was used to build a model and test for differentially expressed (DE) genes.
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: Gene counts were normalized using the TMM (trimmed means of M-values) method and converted into log 2 -transformed counts per million (CPM) using the EdgeR package 51 , 52 .
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Evidence: Gene expression was quantified using salmon against the hg38 version of human transcriptome further processed using txImport and edgeR to generate normalized counts 48 – 50 .
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Evidence: DEGs were identified using edgeR 70 and DESeq2 71 .
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Evidence: Differential expression analysis was performed using the EdgeR package (v.3.40.2) 67 .
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Version used: **3.36.0**
- Evidence: We modelled the salmon-generated count data with quasi-likelihood (QL) negative binomial generalized log-linear models and ran differential expression analysis with edgeR v3.36.0.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: Differential expression analysis (edgeR 60 , v.3.32.1) was conducted using the following steps: (1) transcript filtering for presence/absence and prevalence; (2) library-size normalization using trimmed mean of M values (TMM); (3) estimating per-gene count dispersions; and (4) testing for differentially expressed genes.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: For visualization, counts were CPM normalized with edgeR 105 and batch corrected with the regressBatches function from the batchelor package 106 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Initial attempts to perform hit selection in CROP-seq involved using edgeR, WGCNA and traditional differential expression tests in Seurat (Wilcoxon rank-sum test) 59 – 61 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Version used: **3.32.1**
- Evidence: Transcripts were filtered using the filterByExpr function from the R package edgeR (v.3.32.1) 62 with the following parameters: group set to cell type and time point, min.count to 30, min.total.count to 50, large.n to 20 and min.prop to 0.8.
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Evidence: For evaluating SPP1 expression and its association with EMT in ductal cells (type 1 and 2), raw counts were normalized to counts per million (CPM) using the edgeR package in R (v.4.0.3) and log 2 [CPM + 1] transformed.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Counts were normalized by TMM (edgeR), and residual mean-variance trends were removed using Limma-Voom.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Version used: **4.0.16**
- Evidence: We subsequently used the R package EdgeR (v.4.0.16) to calculate counts per million values from sva-corrected read counts for PCA analysis and plotting.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Evidence: Expression levels of gene features, that is, coding DNA sequences regions from the reference assembly, were quantitated using FeatureCounts (v2.0.3) as raw read counts of the stranded libraries 79 .Differential analysis of quantitated gene features compared with treatment was performed using the software package edgeR on raw sequence counts 80 .
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **4.0.2**
- Evidence: The trimmed mean of M values was calculated for each gene for differential comparisons across samples using edgeR (v.4.0.2) (calcNormFactors()).
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: Read counts were normalized using the trimmed mean of M method implemented in the R Bioconductor package edgeR to determine the abundance of each gene.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: Gene-expression normalization and covariate adjustment Gene counts were input to edgeR.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **3.32.1**
- Evidence: The session used the following libraries: limma (3.46.0), edgeR (3.32.1), tximport (1.18.0), edgeR (3.32.1), sva (3.38.0), RColorBrewer (1.1-2), pheatmap (1.0.12), biomaRt (2.46.3), ggplot2 (3.3.3), gplots (3.1.1), ggfortify (0.4.11), NMF (0.23.0), cluster (2.1.1), fpc (2.2-9), plyr (1.8.6), dplyr (1.0.5), pvclust (2.2-0), ggrepel (0.9.1), amap (0.8-18), gProfileR (0.7.0), xtable (1.8-4), ggpubr (...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Version used: **4.2.0**
- Evidence: Gene count matrices were then loaded into R v.4.4.0, and gene expression levels were estimated using the rpkm function of edgeR v.4.2.0, which accounts for both CDS length and library depth.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### Rewiring endogenous genes in CAR T cells for tumour-restricted payload delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09212-7 | PMCID: PMC12328239 | PMID: 40604285
- Version used: **3.8.5**
- Evidence: Gene counts were normalized using the trimmed means of M -values method and converted into log 2 counts per million using the EdgeR v.3.8.5 package 59 , 60 .
- Full pipeline: quality control [Cutadapt v2.1] -> read trimming [edgeR v3.8.5] -> alignment/mapping [HISAT2] -> normalisation [edgeR v3.8.5] -> dimensionality reduction/clustering [Seurat] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: DEseq2 and edgeR (ref.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: In brief, the peak counts matrix was normalized using ‘cpm(matrix, log = TRUE, prior.count = 5)’ in edgeR followed by quantile normalization using normalize.quantiles of preprocessCore in R.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: ... 77 with the GENCODE human genome build GRCh38.p13 (release 37) 78 ; differential expression using the generalized linear model as implemented by the edgeR Bioconductor R package 79 ; and Gene Ontology (GO) term pathway analysis using the hypergeometric over-representation test with the enrichGO function of the clusterProfiler Bioconductor R package 73 or the Enrichr gene list enrichment analysis ...
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Version used: **4.2.2**
- Evidence: Read count tables were then normalized into fragments per kilobase million (FPKM) then transcripts per million (TPM) using the edgeR 4.2.2 package 54 .
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### Targeting the SHOC2-RAS interaction in RAS-mutant cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-08931-1 | PMCID: PMC12137120 | PMID: 40335703
- Evidence: Differential expression analysis for compound treatments 6 and 7 at 4 h and at 24 h at concentrations of 30 µM and 100 µM in the Mel Juso cell line was performed using the R package edgeR.
- Full pipeline: differential/statistical testing [DESeq2, edgeR] -> stage not stated [Picard, R, fgsea, ggplot2 v3.3.6, ggpubr v0.4.0]

### Regulation of PV interneuron plasticity by neuropeptide-encoding genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08933-z | PMCID: PMC12222018 | PMID: 40307547
- Evidence: Gene-level counts data were imported into R using the tximport package 79 and analysed by edgeR 80 using the estimateGLMRobustDisp model.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> stage not stated [Nextflow v21.03.0, edgeR]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Subsequently, differential expression testing was performed using the edgeR method 50 incorporated in the ‘pbDS’ function.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Differential analysis was done using limma-voom 64 , 65 after TMM normalization 66 of gene level counts with calcNormFactors of edgeR 67 .
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **3.50.3**
- Evidence: For THP-1 RNA-seq analysis, RNA-seq analysis was conducted using the EdgeR (3.50.3) limma (3.36.0) workflow.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **3.38**
- Evidence: Counts were normalized using the trimmed mean of M values method in EdgeR v.3.38 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Changes in neurotensin signalling drive hedonic devaluation in obesity. (Nature 2025)

- DOI: 10.1038/s41586-025-08748-y | PMCID: PMC12119351 | PMID: 40140571
- Version used: **3.24.3**
- Evidence: Differential gene expression analysis was performed using edgeR (version 3.24.3).
- Full pipeline: alignment/mapping [kallisto v0.45.1] -> normalisation [kallisto v0.45.1] -> differential/statistical testing [edgeR v3.24.3] -> stage not stated [DeepLabCut, ImageJ, Python v3.6.7, R v3.5.1]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Each cell type was subset across all ages, then sample-pseudobulked ( n = 4 samples per age, except n = 2 at E16) and passed to the limma-voom pipeline 81 from the edgeR (RRID:SCR_012802) package 82 for differential expression analysis testing.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: The matrices were then CPM-normalized using EdgeR’s DGEList(), calcNormFactors() and cpm() functions 68 .
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Version used: **4.0.16**
- Evidence: ... v.1.33.1-9009, pbapply v.1.7-2, Matrix v.1.6-1.1, scUtils v.0.0.1, magrittr v.2.0.3, igraph v.1.5.1, treeio v.1.26.0, ggh4x v.0.2.6, scales v.1.2.1, edgeR v.4.0.16, limma v.3.58.1, ggtree v.3.10.1, lubridate v.1.9.3, forcats v.1.0.0, stringr v.1.5.0, dplyr v.1.1.3, purrr v.1.0.2, readr v.2.1.4, tidyr v.1.3.0, tibble v.3.2.1, ggplot2 v.3.4.4, tidyverse v.2.0.0, SeuratObject v.4.1.4, Seurat v.4.4.0...
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: To evaluate the relationship between this ILC2 score and TLS signatures 4 , 7 , 8 , we computed the log-transformed normalized gene expression in the TCGA-PAAD dataset described above using the TMM method 86 from edgeR package.
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **3.42.4**
- Evidence: Size factors and dispersion were estimated using the R package edgeR (v.3.42.4) 72 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: The resulting count data were subjected to TMM normalization using the function calcNormFactors in the package edgeR, followed by log transformation by the function voomWithQualityWeights in the package limma.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: PCA was performed on library-size normalized log values computed with edgeR’s (v.3.36.0) cpm function.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: DEGs were identified with edgeR 65 , according to the linear model y ~ diet × time × percentage of ribosomal RNA.
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Evidence: Counts were transformed to geTMM (gene length corrected trimmed mean of M-values) in R using edgeR package 87 .
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Endogenous self-peptides guard immune privilege of the central nervous system. (Nature 2025)

- DOI: 10.1038/s41586-024-08279-y | PMCID: PMC11666455 | PMID: 39476864
- Evidence: After filtering, limma and edgeR were used to build a model and conduct differential expression testing with the lmFit, contrasts.fit and eBayes functions.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR, limma] -> stage not stated [Seurat]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **3.40.2**
- Evidence: The edgeR v.3.40.2 package 70 was used for trimmed mean of M -values normalization and FPKM transformation and the org.Hs.eg.db v.3.16.0 package was used for gene annotation.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **4.2.0**
- Evidence: ...m survival data (‘estimate’) or simulated through corresponding Gompertz models (‘model’), were identified with generalized linear models fitted with edgeR (v4.2.0) package 240 , with experimental site included as a covariate.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **3.40.2**
- Evidence: Differentially expressed genes (false discovery rate (FDR) < 0.05) between the PN types were explored using the edgeR (v.3.40.2) 54 with the trimmed mean of M values normalization, using the dataset of genes expressed in at least ten samples.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: The counts were then loaded into a DGEList object using the edgeR package v4.6.2 for downstream differential expression analysis.
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; repurposes plant O&lt;sub&gt;2&lt;/sub&gt; sensing to regulate post-hypoxia responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10366-1 | PMCID: PMC13216066 | PMID: 42020755
- Evidence: Differentially expressed genes were identified using edgeR 76 (v.3.42.4).
- Full pipeline: quality control [FastQC, featureCounts] -> alignment/mapping [FastQC, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR] -> stage not stated [ImageJ, R v4.3.1]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **3.22.5**
- Evidence: Expression levels were TMM-normalized using edgeR (v.3.22.5) 131 and inverse-normal transformed.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: DEG analyses DEGs for Cux2 cre Atf4 fl mice were determined in Omics playground 63 (v.2.8.19) by performing t -tests (standard, Welch) and limma (no trend, trend, voom), edgeR (QLF, LRT) and DESeq2 (Wald, LRT) tests and taking the highest q value for tests with cutoffs of a false-discovery rate (FDR) of 0.05 and a log 2 -transformed FC of 0.1.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Raw RNA-seq reads were aligned and quantified using the nf-core/rnaseq 95 pipeline with a custom GRCm38 reference containing the Grin1-2b construct, and differential expression analysis was performed using the edgeR package for R 96 .
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Evidence: Briefly, transcript quantification data were summarized to genes using the tximport package 85 and normalized using the trimmed mean of M values method in edgeR 86 .
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Version used: **0.27**
- Evidence: We then conduceted differential gene expression analysis using edgeR (v.0.27).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: Cell-type abundance and statistical analysis We counted the total cells per cell type per sample and computed association statistics between these cell counts and diagnosis of the participants and other AD-related traits using edgeR 56 without the TMM normalization.
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Differential expression Gene counts were normalized using trimmed mean of M values 121 as implemented in the calcNormFactors function from the edgeR package (v.3.26.8) 122 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Version used: **3.36.0**
- Evidence: RNA-seq data processing and analysis The raw read counts were extracted and then normalized by their library size factors and read and gene lengths using edgeR (v.3.36.0) 73 , which was then used to calculate differential genes.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Oral 4'-fluorouridine rescues nonhuman primates from advanced Lassa fever. (Nature 2026)

- DOI: 10.1038/s41586-025-09906-y | PMCID: PMC12935548 | PMID: 41501462
- Version used: **4.4.1**
- Evidence: Thresholded count matrices were exported from nSolver and analysed with limma v.3.62.1 (edgeR v.4.4.1) in R v.4.4.2 58 , 60 ; scripts are available on GitHub ( https://github.com/geisbert-lab/lasv-togo-4fiu ).
- Full pipeline: stage not stated [edgeR v4.4.1, limma v3.62.1]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: EdgeR was used to identify differentially abundant (enriched) guides in sorted samples 68 , and STARS v.1.3 ( https://portals.broadinstitute.org/gpp/public/software/stars ) was used to rank the targeted genes on the basis of enrichment scores of multiple guides.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Differential expression analysis (DEA) was conducted using the Bioconductor EdgeR package (v.3.6).
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **3.20.1**
- Evidence: The processing of the counts and differential expression analysis was performed using limma (v.3.32.2) 58 and EdgeR (v.3.20.1) 59 ) which were also used to perform pairwise differential expression analyses.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Evidence: Genes were filtered by a cross-sample mean of 50 or greater and then normalized using edgeR with calcNormFactors using trimmed mean of M values 65 normalization and log 2 -normalized using voom 66 .
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Version used: **3.40.2**
- Evidence: We summarized the quantification results to gene-level counts using tximport (v.1.26.1), then removed non-protein-coding genes and low-count genes using the filterByExpr function in edgeR (v.3.40.2).
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Evidence: The counts were normalized to remove library size effects using edgeR 58 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### SARS-CoV-2 expresses a microRNA-like small RNA able to selectively repress host genes. (PNAS 2021)

- DOI: 10.1073/pnas.2116668118 | PMCID: PMC8719879 | PMID: 34903581
- Evidence: Differential expression was determined using edgeR ( 69 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, featureCounts] -> differential/statistical testing [edgeR] -> visualisation [BEDTools]

### Tryptophan metabolism and bacterial commensals prevent fungal dysbiosis in <i>Arabidopsis</i> roots. (PNAS 2021)

- DOI: 10.1073/pnas.2111521118 | PMCID: PMC8670527 | PMID: 34853170
- Evidence: ...ance of strains between WT and Mutants was calculated by normalization of raw sequencing counts (TMM normalization, “calcNormFactors” from R package “EdgeR”) and fitting a generalized linear model (“glmFit”) including the replicate effects.
- Full pipeline: quantification [R] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR]

### Engineered SARS-CoV-2 receptor binding domain improves manufacturability in yeast and immunogenicity in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2106845118 | PMCID: PMC8463846 | PMID: 34493582
- Version used: **3.26.8**
- Evidence: Expression values were summarized with tximport version 1.12.3 ( 59 ) and edgeR version 3.26.8 ( 60 , 61 ).
- Full pipeline: differential/statistical testing [DESeq2, GSEA v4.1.0] -> stage not stated [ImageJ, edgeR v3.26.8]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Evidence: Then the R package DiffBind ( 51 ) was used to calculate reads across the merged peaks and calculate differential peaks for each cell type utilizing the edgeR method ( 52 , 53 ).
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself. (PNAS 2021)

- DOI: 10.1073/pnas.2100542118 | PMCID: PMC8449404 | PMID: 34507984
- Evidence: We scaled columns of the count matrix using the calcNormFactors function in the edgeR R library ( 62 , 63 ).
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [R v3.6.3] -> visualisation [ComplexHeatmap, ggplot2, ggpubr] -> stage not stated [Clustal Omega v1.2]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Evidence: Differential gene expression analysis was performed using the edgeR package in R ( 70 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Molecular underpinnings and biogeochemical consequences of enhanced diatom growth in a warming Southern Ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2107238118 | PMCID: PMC8325266 | PMID: 34301906
- Evidence: Differential gene expression at T5 (foldchange magnitude and adjusted P value) was calculated using empirical Bayes quasi-likelihood F-tests (glmQLFTest in edgeR) on taxon-normalized expression values to account for the change in abundance under the different iron and temperature treatments.
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR]

### Transposon-mediated insertional mutagenesis unmasks recessive insecticide resistance in the aphid <i>Myzus persicae</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100559118 | PMCID: PMC8201860 | PMID: 34074777
- Version used: **3.9**
- Evidence: EdgeR version 3.9 ( 52 ) was used to identify significantly DE genes using a corrected P value threshold of P < 0.05 and a fold change >2.
- Full pipeline: quality control [FastQC, Trim Galore v0.4.5] -> read trimming [FastQC] -> alignment/mapping [HISAT2 v2.1.0, HTSeq] -> differential/statistical testing [edgeR v3.9] -> stage not stated [MUSCLE v3.8]

### HIF-1α is a negative regulator of interferon regulatory factors: Implications for interferon production by hypoxic monocytes. (PNAS 2021)

- DOI: 10.1073/pnas.2106017118 | PMCID: PMC8256008 | PMID: 34108245
- Evidence: Gene-level raw counts were calculated using featureCounts (v1.5.2) and normalized by the Trimmed means of M-values normalization method implemented in the edgeR package ( 64 ).
- Full pipeline: quality control [HISAT2 v2.0.5] -> read trimming [edgeR, featureCounts v1.5.2] -> alignment/mapping [HISAT2 v2.0.5] -> normalisation [edgeR, featureCounts v1.5.2]

### Epigenetic inheritance of DNA methylation changes in fish living in hydrogen sulfide-rich springs. (PNAS 2021)

- DOI: 10.1073/pnas.2014929118 | PMCID: PMC8255783 | PMID: 34185679
- Evidence: P value from edgeR ( 72 ) was used to determine the significance of the difference between the two groups for each 100-bp genomic window.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [R, edgeR]

### AGO2 promotes tumor progression in KRAS-driven mouse models of non-small cell lung cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2026104118 | PMCID: PMC8157917 | PMID: 33972443
- Evidence: Estimated counts were used to create DEGList and normalized by trimmed mean of M values (TMM) ( 54 ) using the calcNormFactors of edgeR ( 55 ).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> differential/statistical testing [fgsea, limma] -> stage not stated [GSEA]

### Resetting proteostasis with ISRIB promotes epithelial differentiation to attenuate pulmonary fibrosis. (PNAS 2021)

- DOI: 10.1073/pnas.2101100118 | PMCID: PMC8157939 | PMID: 33972447
- Version used: **3.28.0**
- Evidence: Differential gene expression was performed using edgeR (version 3.28.0).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> alignment/mapping [FastQC, Trimmomatic v0.36] -> differential/statistical testing [edgeR v3.28.0] -> stage not stated [Fiji v1.8.0, HTSeq v0.11.2, ImageJ v1.8.0]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: Differential gene expression analysis was carried out in edgeR ( 82 ).
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### TBK1 recruitment to STING activates both IRF3 and NF-κB that mediate immune defense against tumors and viral infections. (PNAS 2021)

- DOI: 10.1073/pnas.2100225118 | PMCID: PMC8040795 | PMID: 33785602
- Evidence: For DEG (differentially expressed gene) analysis, we used the R package edgeR and followed the user guide ( 62 , 63 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [R v4.0.2, ggplot2]

### Lineage-specific selection and the evolution of virulence in the <i>Candida</i> clade. (PNAS 2021)

- DOI: 10.1073/pnas.2016818118 | PMCID: PMC8000421 | PMID: 33723044
- Evidence: However, both of the statistical approaches assume that there are no technical biases between the two alleles. edgeR and DESeq ( 60 ) were developed to sample the same gene across conditions where this assumption is likely true.
- Full pipeline: differential/statistical testing [edgeR] -> stage not stated [MACS2, R]

### Mitochondrial metabolism is essential for invariant natural killer T cell development and function. (PNAS 2021)

- DOI: 10.1073/pnas.2021385118 | PMCID: PMC8020658 | PMID: 33753493
- Evidence: ( 72 ) for read counting, and edgeR ( 73 ) for differential expression analysis, and g:Profiler for gene enrichment analysis ( 74 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### Comparative analysis of embryo proper and suspensor transcriptomes in plant embryos with different morphologies. (PNAS 2021)

- DOI: 10.1073/pnas.2024704118 | PMCID: PMC8017943 | PMID: 33536344
- Evidence: We used EdgeR (false discovery rate [FDR] <0.05) to identify mRNAs that were more than fivefold more prevalent, or up-regulated, in each embryo region ( SI Appendix , Materials and Methods ).
- Full pipeline: differential/statistical testing [edgeR]

### Pluripotent stem cell-derived epithelium misidentified as brain microvascular endothelium requires ETS factors to acquire vascular fate. (PNAS 2021)

- DOI: 10.1073/pnas.2016950118 | PMCID: PMC7923590 | PMID: 33542154
- Evidence: After further filtering and quality control, R package edgeR ( 67 ) was used to calculate trimmed mean of M-values (TMM) normalization factors.
- Full pipeline: quality control [FastQC v0.11.5, R, edgeR] -> read trimming [R, STAR, edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Version used: **3.30.0**
- Evidence: To call differential accessible peaks, the R package edgeR (version 3.30.0) was used ( 49 ).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### Sunlight exposure exerts immunomodulatory effects to reduce multiple sclerosis severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018457118 | PMCID: PMC7817192 | PMID: 33376202
- Evidence: Bioinformatic analysis was done in R using Kallisto and edgeR .
- Full pipeline: quality control [PLINK v1.90] -> variant calling [PLINK v1.90] -> differential/statistical testing [R v3.6, lme4] -> visualisation [ggplot2] -> stage not stated [edgeR, kallisto]

### A bacterium from a mountain lake harvests light using both proton-pumping xanthorhodopsins and bacteriochlorophyll-based photosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2211018119 | PMCID: PMC9897461 | PMID: 36469764
- Evidence: Normalization and identification of significantly differentially regulated genes (FDR < 0.05) were performed with edgeR.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [featureCounts]

### A novel post-developmental role of the Hox genes underlies normal adult behavior. (PNAS 2022)

- DOI: 10.1073/pnas.2209531119 | PMCID: PMC9894213 | PMID: 36454751
- Evidence: Using edgeR analysis ( 34 ), we identified 233 differentially expressed genes (DEGs) (out of 5,708 total genes detected) in TH>Ubx RNAi neurons relative to wild-type (wt) neurons ( P value < 0.01; Dataset S1 ) ( Fig.
- Full pipeline: differential/statistical testing [edgeR] -> stage not stated [Clustal Omega, ImageJ]

### Transcriptional control of cone photoreceptor diversity by a thyroid hormone receptor. (PNAS 2022)

- DOI: 10.1073/pnas.2209884119 | PMCID: PMC9894165 | PMID: 36454759
- Evidence: Specific TRβ2-HAB peaks were identified by differential analysis of HAB, BirA, and BirA samples using EdgeR ( P <0.05; cutoff >twofold).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [deepTools] -> differential/statistical testing [DESeq2, MACS2 v2.2.7.1, edgeR] -> visualisation [deepTools]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: NMDS analysis was performed using the plotMDS function of edgeR ( 68 ) using the top 500 differentially expressed genes as sorted by adjusted P value and log 2 fold change.
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### CTLA-4 on thymic epithelial cells complements Aire for T cell central tolerance. (PNAS 2022)

- DOI: 10.1073/pnas.2215474119 | PMCID: PMC9860321 | PMID: 36409920
- Evidence: Population-level and single-cell RNA-seq and microarray analyses were performed on published datasets using edgeR for bulk RNA-seq, Seurat for scRNA-seq, and R for microarray analyses.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.1.0, Seurat, edgeR]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: The read counts for all samples were then normalized using the trimmed mean of M method implemented in the R Bioconductor package edgeR to generate the abundance for each gene ( 75 , 76 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Polycomb group (PcG) proteins prevent the assembly of abnormal synaptonemal complex structures during meiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2204701119 | PMCID: PMC9586294 | PMID: 36215502
- Evidence: Gene counts were normalized with the TMM method ( 72 ), and differential expression analysis was performed using a quasi-likelihood F-test ( 73 ), as implemented in the edgeR R package ( 74 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR, deepTools] -> normalisation [R, deepTools, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [MACS2]

### Microbiome composition modulates secondary metabolism in a multispecies bacterial community. (PNAS 2022)

- DOI: 10.1073/pnas.2212930119 | PMCID: PMC9586298 | PMID: 36215464
- Evidence: Counts per million (CPM) were computed in edgeR ( 64 ).
- Full pipeline: alignment/mapping [HTSeq, SAMtools v1.9, fastp v0.20.0] -> quantification [HTSeq, SAMtools v1.9] -> differential/statistical testing [R v4.2] -> stage not stated [Bowtie2 v2.4.2, edgeR, eggNOG]

### Blockade of the protease ADAM17 ameliorates experimental pancreatitis. (PNAS 2022)

- DOI: 10.1073/pnas.2213744119 | PMCID: PMC9586293 | PMID: 36215509
- Evidence: Additional gene annotation was obtained using the biomaRt package (v2.50.1) ( 25 ), and a DGEList object was created with the counts and gene annotation using the edgeR package (v3.36.0) ( 26 ).
- Full pipeline: alignment/mapping [R v4.1.2] -> differential/statistical testing [limma v3.50.0] -> stage not stated [edgeR, pheatmap]

### Ovarian cancer cell fate regulation by the dynamics between saturated and unsaturated fatty acids. (PNAS 2022)

- DOI: 10.1073/pnas.2203480119 | PMCID: PMC9564215 | PMID: 36197994
- Evidence: DEGs between experimental groups were determined and FDR corrected for multiple hypothesis testing with the edgeR package ( 50 ) in R.
- Full pipeline: normalisation [GSEA] -> differential/statistical testing [ImageJ, edgeR] -> stage not stated [RSEM]

### Gaussian curvature-driven direction of cell fate toward osteogenesis with triply periodic minimal surface scaffolds. (PNAS 2022)

- DOI: 10.1073/pnas.2206684119 | PMCID: PMC9564829 | PMID: 36191194
- Evidence: Then, the differential gene expression between the two groups was evaluated by edgeR analysis.
- Full pipeline: differential/statistical testing [edgeR]

### Reduced Satb1 expression predisposes CD4<sup>+</sup> T conventional cells to Treg suppression and promotes transplant survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205062119 | PMCID: PMC9546564 | PMID: 36161903
- Evidence: Differential gene expression (adj P ≤ 0.05) was calculated using quasi-likelihood F-test in edgeR ( 51 – 53 ).
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [STAR v2.5.3a, featureCounts] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [R v3.4.1] -> differential/statistical testing [edgeR]

### Biosensors for inflammation as a strategy to engineer regulatory T cells for cell therapy. (PNAS 2022)

- DOI: 10.1073/pnas.2208436119 | PMCID: PMC9546553 | PMID: 36161919
- Evidence: Gene counts were imported and prefiltered with edgeR:filterByExpr , and the false discovery rate (FDR) was set to 0.05. gene ontology analysis was performed with genes upregulated with a log2 fold change > 1 and FDR < 0.05 using goseq .
- Full pipeline: quality control [DESeq2] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [fgsea, ggplot2]

### Comparative genomics of mortal and immortal cnidarians unveils novel keys behind rejuvenation. (PNAS 2022)

- DOI: 10.1073/pnas.2118763119 | PMCID: PMC9459311 | PMID: 36037356
- Evidence: STAR ( 44 ) was used for aligning RNA sequences of each sample to the assembled T. dohrnii genome and edgeR ( 45 ) and limma ( 46 ) for modeling differential expression between stages, after applying voom ( 47 ) transformation to consider library size variability.
- Full pipeline: alignment/mapping [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [AlphaFold v2.1.2, BUSCO, ChimeraX, GSEA, fgsea]

### Ligand diversity contributes to the full activation of the jasmonate pathway in &lt;i&gt;Marchantia polymorpha&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2202930119 | PMCID: PMC9457472 | PMID: 36037336
- Evidence: ( A ) Analysis of RNA-seq data by K-means clustering of genes differentially expressed [evaluated by EdgeR ( 68 )] in response to mechanical wounding (90 min) in the genotypes indicated (log ratio > 1.5/< −1.5; FDR < 0.05).
- Full pipeline: variant calling [edgeR] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [edgeR]

### Dopamine and GPCR-mediated modulation of DN1 clock neurons gates the circadian timing of sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2206066119 | PMCID: PMC9407311 | PMID: 35969763
- Evidence: Differential expression analysis between nSyb neurons and clock neurons was performed using the Bioconductor package edgeR ( 33 ).
- Full pipeline: dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [Bioconductor, Seurat, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [Picard]

### Adrenergic receptor signaling induced by Klf15, a regulator of regeneration enhancer, promotes kidney reconstruction. (PNAS 2022)

- DOI: 10.1073/pnas.2204338119 | PMCID: PMC9388080 | PMID: 35939709
- Version used: **3.32.1**
- Evidence: Peaks in independent samples were merged and fragments per peak in each sample were counted using featureCounts (2.0.1) and edgeR (3.32.1) software packages to detect differential ATAC-seq peaks (RRID: SCR_012919) (RRID:SCR_012802) ( 19 , 39 ).
- Full pipeline: differential/statistical testing [MACS2 v2.2.6, edgeR v3.32.1, featureCounts v2.0.1] -> stage not stated [BEDTools v2.30.0, HOMER]

### Balanced control of thermogenesis by nuclear receptor corepressors in brown adipose tissue. (PNAS 2022)

- DOI: 10.1073/pnas.2205276119 | PMCID: PMC9388101 | PMID: 35939699
- Evidence: Briefly, this pipeline uses Kallisto to align and quantify reads, EnemblDB to annotate data, edgeR to normalize read counts, and Limma to determine differentially expressed genes (DEGs).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, edgeR, kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR, kallisto] -> differential/statistical testing [R v4.1, edgeR, kallisto] -> stage not stated [Enrichr, SAMtools]

### Postmitotic accumulation of histone variant H3.3 in new cortical neurons establishes neuronal chromatin, transcriptome, and identity. (PNAS 2022)

- DOI: 10.1073/pnas.2116956119 | PMCID: PMC9371731 | PMID: 35930666
- Evidence: Differential gene expression was analyzed using edgeR ( 49 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP]

### Inhibition of CDK8/19 Mediator kinase potentiates HER2-targeting drugs and bypasses resistance to these agents in vitro and in vivo. (PNAS 2022)

- DOI: 10.1073/pnas.2201073119 | PMCID: PMC9371674 | PMID: 35914167
- Evidence: DEG analysis was performed in R using the edgeR package.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [GSEA] -> stage not stated [edgeR]

### P38α MAPK is a gatekeeper of uterine progesterone responsiveness at peri-implantation via Ube3c-mediated PGR degradation. (PNAS 2022)

- DOI: 10.1073/pnas.2206000119 | PMCID: PMC9371708 | PMID: 35914132
- Version used: **3.9**
- Evidence: Differential expression genes were normalized to fragments per kilobase of exon model per million mapped reads (RPKM) using the EdgeR 3.9 package in R with the criteria of fold change significantly greater than 2 or less than 0.5 and P < 0.05.
- Full pipeline: alignment/mapping [edgeR v3.9] -> quantification [edgeR v3.9] -> normalisation [edgeR v3.9] -> differential/statistical testing [edgeR v3.9] -> visualisation [ggplot2]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: Differential expression analysis for transcriptomes and translatomes was achieved using the Bioconductor package edgeR, based on the negative binomial distributions ( 57 ).
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### Nuclear-localized, iron-bound superoxide dismutase-2 antagonizes epithelial lineage programs to promote stemness of breast cancer cells via a histone demethylase activity. (PNAS 2022)

- DOI: 10.1073/pnas.2110348119 | PMCID: PMC9303987 | PMID: 35858297
- Evidence: Differentially expressed genes (DEGs) were identified using EdgeR in NLS-SOD2 compared to WT-SOD2 with a cutoff of ≥1.5-fold increase and false discovery rate (FDR) threshold of 0.01, by generalized linear model (GLM) approach.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [edgeR] -> stage not stated [Cytoscape, GSEA, STRING db]

### Genetic variation that determines &lt;i&gt;TAPBP&lt;/i&gt; expression levels associates with the course of malaria in an HLA allotype-dependent manner. (PNAS 2022)

- DOI: 10.1073/pnas.2205498119 | PMCID: PMC9303992 | PMID: 35858344
- Evidence: The trimmed mean of M-values normalization method, as implemented in the R package edgeR, was used for normalization, and genotypes at SNP positions were determined by using the bcftools (v1.9) mpileup function with sorted binary alignment map files of RNA-sequencing (RNA-Seq) reads aligned to the human reference genome as input ( 50 , 51 ).
- Full pipeline: read trimming [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, Trimmomatic v0.33, edgeR] -> alignment/mapping [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, edgeR] -> variant calling [BCFtools v1.9, R, edgeR] -> normalisation [BCFtools v1.9, R, edgeR]

### Zinc finger protein 280C contributes to colorectal tumorigenesis by maintaining epigenetic repression at H3K27me3-marked loci. (PNAS 2022)

- DOI: 10.1073/pnas.2120633119 | PMCID: PMC9295756 | PMID: 35605119
- Evidence: Transcript abundance was quantified using HTseq (version 0.11.2), and differentially expressed genes were identified using the edgeR package from the R software.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, MACS2 v2.1.6] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> visualisation [deepTools v3.1.3] -> stage not stated [GSEA]

### Enzymes degraded under high light maintain proteostasis by transcriptional regulation in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121362119 | PMCID: PMC9171785 | PMID: 35549553
- Evidence: Differential gene expression was tested using the edgeR quasi-likelihood pipeline ( 78 , 79 ).
- Full pipeline: quality control [FastQC v0.11.7] -> alignment/mapping [SAMtools v1.3.1, featureCounts] -> differential/statistical testing [edgeR] -> stage not stated [Trim Galore]

### Antibody-mediated blockade of the IL23 receptor destabilizes intratumoral regulatory T cells and enhances immunotherapy. (PNAS 2022)

- DOI: 10.1073/pnas.2200757119 | PMCID: PMC9170135 | PMID: 35482921
- Evidence: The resulting sample-wise gene expression table was analyzed using edgeR ( 30 ) with default parameters.
- Full pipeline: stage not stated [R, Seurat, edgeR]

### Chronic inflammatory arthritis drives systemic changes in circadian energy metabolism. (PNAS 2022)

- DOI: 10.1073/pnas.2112781119 | PMCID: PMC9170023 | PMID: 35482925
- Version used: **3.30.3**
- Evidence: Differential expression analysis was run in R ( 41 ) using edgeR (version 3.30.3).
- Full pipeline: differential/statistical testing [Enrichr, R v3.30.3, edgeR v3.30.3]

### &lt;i&gt;Wolbachia&lt;/i&gt; depletion blocks transmission of lymphatic filariasis by preventing chitinase-dependent parasite exsheathment. (PNAS 2022)

- DOI: 10.1073/pnas.2120003119 | PMCID: PMC9169722 | PMID: 35377795
- Version used: **3.30.3**
- Evidence: The aligned RNA sequence expression data were quantified using the program FeatureCounts (v1.5.0-p3) ( 62 ) and used as input into the program edgeR (v3.30.3) ( 63 ) for differential gene expression analysis.
- Full pipeline: alignment/mapping [edgeR v3.30.3, featureCounts v1.5.0] -> quantification [edgeR v3.30.3, featureCounts v1.5.0] -> differential/statistical testing [edgeR v3.30.3, featureCounts v1.5.0]

### <i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import. (PNAS 2022)

- DOI: 10.1073/pnas.2123353119 | PMCID: PMC8931380 | PMID: 35275795
- Evidence: Differentially expressed genes were identified using the R package edgeR, which uses counts per gene in different samples and performs data normalization using the trimmed mean of M-values method ( 49 ).
- Full pipeline: read trimming [Cutadapt v1.3, R, edgeR] -> alignment/mapping [BWA, TopHat, VCFtools] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [SAMtools]

### A commensal-encoded genotoxin drives restriction of <i>Vibrio cholerae</i> colonization and host gut microbiome remodeling. (PNAS 2022)

- DOI: 10.1073/pnas.2121180119 | PMCID: PMC8931321 | PMID: 35254905
- Evidence: To obtain species that might respond to colibactin, edgeR ( 64 ) was used to calculate the fold change and significance of intergroup differences.
- Full pipeline: alignment/mapping [BLAST] -> dimensionality reduction/clustering [BLAST] -> stage not stated [edgeR]

### Molecular mechanisms underlying metamorphosis in the most-ancestral winged insect. (PNAS 2022)

- DOI: 10.1073/pnas.2114773119 | PMCID: PMC8892354 | PMID: 35217609
- Evidence: We searched for nymph-specific or adult-specific genes by edgeR analysis (false discovery rate [FDR] < 0.01), in which penultimate instar nymphs and adults were compared for the head, thorax, abdomen, and wings.
- Full pipeline: differential/statistical testing [edgeR]

### A multiomic study uncovers a bZIP23-PER1A-mediated detoxification pathway to enhance seed vigor in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2026355119 | PMCID: PMC8892333 | PMID: 35217598
- Evidence: Differential expression of transcript was analyzed between the unaged seeds of Kasalath and Jigeng88 rice and across all the aging times for each cultivar using the likelihood ratio test in the DESeq2 or quasi-likelihood method in the EdgeR.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [Cytoscape v3.6] -> stage not stated [R, featureCounts]

### An in-frame deletion mutation in the degron tail of auxin coreceptor <i>IAA2</i> confers resistance to the herbicide 2,4-D in <i>Sisymbrium orientale</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2105819119 | PMCID: PMC8892348 | PMID: 35217601
- Evidence: Counts-per-million (CPM) and gene-expression differences were calculated with the package “edgeR” ( 40 ) using the statistical software R version 3.3 ( 41 ) and an expression threshold of ≥1 CPM in at least two samples.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [SAMtools] -> differential/statistical testing [R v3.3, edgeR] -> stage not stated [BCFtools, BUSCO]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: Differential expression (DE) analyses were conducted using DESeq2 ( 63 ) ( E. nindensis , E. tef , and O. thomaeum ) or edgeR ( 23 ) ( S. stapfianus and S. pyramidalis ), and resulting outputs were processed using Pandas 0.25.0 in Python 3.6.8.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### MadR mediates acyl CoA-dependent regulation of mycolic acid desaturation in mycobacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2111059119 | PMCID: PMC8872791 | PMID: 35165190
- Evidence: The tools included 1) RoundRobin (in-house), 2) RankProduct ( 51 ), 3) significance analysis of microarrays (SAM) ( 52 ), 4) EdgeR ( 53 ), and 5) DESeq2 ( 54 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [DESeq2, R, edgeR]

### Genomic and transcriptomic analyses of the subterranean termite <i>Reticulitermes speratus</i>: Gene duplication facilitates social evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2110361119 | PMCID: PMC8785959 | PMID: 35042774
- Evidence: Transcript abundances were estimated using featureCounts and normalized with the trimmed mean of M-values algorithm in edgeR.
- Full pipeline: read trimming [edgeR, featureCounts] -> alignment/mapping [TopHat v2.1.0] -> quantification [edgeR, featureCounts] -> normalisation [edgeR, featureCounts]

### Neuronal identities derived by misexpression of the POU IV sensory determinant in a protovertebrate. (PNAS 2022)

- DOI: 10.1073/pnas.2118817119 | PMCID: PMC8794889 | PMID: 35042818
- Evidence: For each cell population, the edgeR differential expression analysis package ( 36 ) was used to calculate differentially expressed genes (DEGs) between itself and select cell populations.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [Seurat v2.3.4]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Evidence: Read counts were generated with the Rsubread package function featureCounts in R ( 89 , 90 ). edgeR was used to construct principal component analysis plots of libraries ( 32 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### Convergent evolution of venom gland transcriptomes across Metazoa. (PNAS 2022)

- DOI: 10.1073/pnas.2111392119 | PMCID: PMC8740685 | PMID: 34983844
- Evidence: To identify taxon-specific patterns, we performed differential expression analysis at the gene level for each species separately using edgeR ( 52 ).
- Full pipeline: quality control [kallisto] -> read trimming [kallisto] -> alignment/mapping [RAxML] -> quantification [kallisto] -> normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [Bioconductor, InterProScan]

### Conservation of magnetite biomineralization genes in all domains of life and implications for magnetic sensing. (PNAS 2022)

- DOI: 10.1073/pnas.2108655119 | PMCID: PMC8784154 | PMID: 35012979
- Evidence: Differential gene expression was modeled using a generalized linear model likelihood ratio test implemented in EdgeR ( 58 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2 v2.2.1] -> normalisation [R v3.12.1] -> dimensionality reduction/clustering [R v3.12.1] -> differential/statistical testing [BLAST, edgeR] -> visualisation [R v3.12.1] -> stage not stated [ImageJ]

### Locust density shapes energy metabolism and oxidative stress resulting in divergence of flight traits. (PNAS 2022)

- DOI: 10.1073/pnas.2115753118 | PMCID: PMC8740713 | PMID: 34969848
- Evidence: DEGs were analyzed by using EdgeR software.
- Full pipeline: alignment/mapping [HISAT2] -> stage not stated [edgeR]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Version used: **3.0.8**
- Evidence: Gene count tables were constructed using HTseq ( 46 ) with Ensembl gene annotations and used as input for edgeR 3.0.8 ( 47 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Version used: **3.24.3**
- Evidence: DEG analysis was performed via EdgeR (v3.24.3) algorithm ( 82 ) using IDEAMEX ( 35 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Targeting the lipid kinase PIKfyve upregulates surface expression of MHC class I to augment cancer immunotherapy. (PNAS 2023)

- DOI: 10.1073/pnas.2314416120 | PMCID: PMC10710078 | PMID: 38011559
- Evidence: Data were then analysed with the R package edgeR ( 67 ).
- Full pipeline: stage not stated [R, edgeR]

### Dysregulated CD200-CD200R signaling in early diabetes modulates microglia-mediated retinopathy. (PNAS 2023)

- DOI: 10.1073/pnas.2308214120 | PMCID: PMC10636339 | PMID: 37903272
- Evidence: We then performed a standard EdgeR-limma pipeline analysis on all samples (n = 10) and compiled differentially expressed genes (DEG; >|1.5|FC; FDR < 0.05) for each diabetic condition compared to control.
- Full pipeline: differential/statistical testing [edgeR, limma]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Version used: **3.34.1**
- Evidence: Differential expression was performed with the R package edgeR (v3.34.1) ( 57 ) or DESeq2 (v1.34.0) ( 58 ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### IL-6 trans-signaling in a humanized mouse model of scleroderma. (PNAS 2023)

- DOI: 10.1073/pnas.2306965120 | PMCID: PMC10500188 | PMID: 37669366
- Evidence: Differential gene expression analysis of scRNA-Seq data was performed using Cell Ranger and Loupe Cell Browser software (10× Genomics), which uses a variant of the negative binomial exact test from sSeq and the asymptotic beta test in edgeR depending on sample size ( 79 , 80 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### Impaired age-associated mitochondrial translation is mitigated by exercise and PGC-1α. (PNAS 2023)

- DOI: 10.1073/pnas.2302360120 | PMCID: PMC10483666 | PMID: 37639610
- Evidence: Differential expression analysis of the count matrix was performed with EdgeR.
- Full pipeline: quantification [ImageJ v1.52a, limma] -> differential/statistical testing [edgeR, limma]

### <i>Bcl6</i>, <i>Irf2</i>, and <i>Notch2</i> promote nonclassical monocyte development. (PNAS 2023)

- DOI: 10.1073/pnas.2220853120 | PMCID: PMC10469339 | PMID: 37607223
- Evidence: All gene counts were then imported into the R/Bioconductor package EdgeR and TMM normalization size factors were calculated to adjust for samples for differences in library size.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> normalisation [Bioconductor, edgeR]

### XCR1 expression distinguishes human conventional dendritic cell type 1 with full effector functions from their immediate precursors. (PNAS 2023)

- DOI: 10.1073/pnas.2300343120 | PMCID: PMC10438835 | PMID: 37566635
- Evidence: Eventually, they were analyzed in R using NanoStringNorm ( 77 ) and edgeR ( 78 ), and DEGs were determined with a threshold of false-discovery rate (FDR)–Benjamini–Hochberg adjusted P value of 0.01 and a log2 fold change (FC) of 1.5.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [GSEA, MACS2, Seurat]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Evidence: ... young 4 Mock-infected aged 4 P2-infected young 6 P2-infected aged 6 P21-infected young 5 P21-infected aged 6 The count matrix was filtered using the edgeR ( 45 ) (v3.15) filterByExpr function and including the grouping variable to apply filtration relative to the smallest group size (n = 4).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Version used: **3.26.8**
- Evidence: Gene expression levels in reads per kilobase per million mapped reads (RPKM) values were computed and normalized by effective library size estimated by trimmed mean of M values, using the R package edgeR (v3.26.8) ( 82 ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### EGR4 is critical for cell-fate determination and phenotypic maintenance of geniculate ganglion neurons underlying sweet and umami taste. (PNAS 2023)

- DOI: 10.1073/pnas.2217595120 | PMCID: PMC10235952 | PMID: 37216536
- Version used: **3.12.1**
- Evidence: Differential expression analysis was performed using edgeR (v.3.12.1) ( 60 , 61 ).
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.5] -> differential/statistical testing [GSEA, edgeR v3.12.1] -> stage not stated [ImageJ]

### Circadian clock protein BMAL1 broadly influences autophagy and endolysosomal function in astrocytes. (PNAS 2023)

- DOI: 10.1073/pnas.2220551120 | PMCID: PMC10194014 | PMID: 37155839
- Evidence: We used the EdgeR, Limma, and Voom with Quality Weights packages to normalize and filter data before applying linear modeling and the empirical Bayes method to test for differentially regulated genes ( 19 ).
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Downstream analyses and identification of differentially expressed genes used the EdgeR Bioconductor package ( 97 ).
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Consequences of poly(ethylene oxide) and poloxamer P188 on transcription in healthy and stressed myoblasts. (PNAS 2023)

- DOI: 10.1073/pnas.2219885120 | PMCID: PMC10161009 | PMID: 37094151
- Evidence: The Bioconductor package Empirical Analysis of Digital Gene Expression Data in R (edgeR) was utilized because of its ability to determine differential expression of a dataset with a small number of replicates that is expected to have less than 50% of the genes impacted ( 61 – 63 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [GSEA, STRING db]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: EdgeR was used to assess differential gene expression with default parameters for the estimateDisp and exactTest functions ( 62 , 63 ).
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### On the origin of appetite: GLWamide in jellyfish represents an ancestral satiety neuropeptide. (PNAS 2023)

- DOI: 10.1073/pnas.2221493120 | PMCID: PMC10104569 | PMID: 37011192
- Evidence: To define DEGs, the Benjamini–Hochberg method ( 70 ) was applied on p values produced by edgeR ( 71 ) to perform multiplicity correction for controlling the false discovery rates (FDRs) or q values.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [R, RSEM] -> dimensionality reduction/clustering [R] -> differential/statistical testing [edgeR] -> stage not stated [InterProScan v5.52]

### Cholinergic regulation of vascular endothelial function by human ChAT<sup>+</sup> T cells. (PNAS 2023)

- DOI: 10.1073/pnas.2212476120 | PMCID: PMC10083572 | PMID: 36989306
- Evidence: Single-cell gene expression data of CD4 + T cells were analyzed using the pipeline from SingleCellsExperiment ( 71 ) package using packages BiomaRt ( 72 ), scran ( 73 ), scater, ( 74 ), edgeR ( 75 ) and EnhancedVolcano ( 76 ).
- Full pipeline: alignment/mapping [Monocle] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ] -> stage not stated [MACS2, edgeR]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Version used: **3.24.3**
- Evidence: In R, raw count matrices were generated using HTSeq (v0.11.2), then scale factors were calculated to take into account differences in library sizes using edgeR (v3.24.3), and normalization was performed using limma (v3.38.3) as in (Law et al., 2016).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### RNA interference is essential to modulating the pathogenesis of mosquito-borne viruses in the yellow fever mosquito &lt;i&gt;Aedes aegypti&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213701120 | PMCID: PMC10089172 | PMID: 36893279
- Evidence: The edgeR Bioconductor software package ( https://bioconductor.org/packages/release/bioc/html/edgeR.html ) was used to determine differential expression between replicate datasets.
- Full pipeline: differential/statistical testing [Bioconductor, edgeR]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Evidence: The statistical significance of differential transcription was evaluated using edgeR software ( 55 ), applying a false discovery rate threshold of 0.05.
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### Polyamines and linear DNA mediate bacterial threat assessment of bacteriophage infection. (PNAS 2023)

- DOI: 10.1073/pnas.2216430120 | PMCID: PMC9992862 | PMID: 36802441
- Version used: **3.34.1**
- Evidence: Count tables produced with Rsubread were normalized and tested for differential expression using edgeR v3.34.1 ( 59 ) ( Dataset S1 ).
- Full pipeline: normalisation [edgeR v3.34.1] -> differential/statistical testing [edgeR v3.34.1] -> visualisation [ggplot2, pheatmap]

### Type III interferon drives thymic B cell activation and regulatory T cell generation. (PNAS 2023)

- DOI: 10.1073/pnas.2220120120 | PMCID: PMC9992806 | PMID: 36802427
- Version used: **3.24.3**
- Evidence: For the GSE152453 dataset (National Center for Biotechnology Information Gene Expression Omnibus), raw counts were analyzed using edgeR v3.24.3.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R v4.0.0, Seurat, edgeR v3.24.3, ggplot2, pheatmap]

### Time of day determines postexercise metabolism in mouse adipose tissue. (PNAS 2023)

- DOI: 10.1073/pnas.2218510120 | PMCID: PMC9974500 | PMID: 36780527
- Evidence: Differential gene expression analysis was performed using edgeR, quasi-likelihood negative binomial generalized log-linear model, and the design ~0 + group.
- Full pipeline: alignment/mapping [featureCounts v1.6.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [R]

### Helminth egg derivatives as proregenerative immunotherapies. (PNAS 2023)

- DOI: 10.1073/pnas.2211703120 | PMCID: PMC9974432 | PMID: 36780522
- Evidence: ( F ) Volcano plot of differential expression from bulk RNA sequencing of the muscle 1 wk postinjury and rSEA treatment referenced to saline-treated injuries by the EdgeR analysis.
- Full pipeline: differential/statistical testing [edgeR]

### Definition of the contribution of an Osteopontin-producing CD11c<sup>+</sup> microglial subset to Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2218915120 | PMCID: PMC9963365 | PMID: 36730200
- Evidence: Analysis of differentially expressed genes (DEGs) was performed by a negative binomial model implemented in the R package edgeR (Bioconductor) ( 57 , 58 ), comparing OPN-KO.5XFAD to 5XFAD mice using a one-factor design and default parameters.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [MACS2]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: Raw counts were filtered to keep only genes with at least three counts per million [calculated using edgeR; ( 111 , 112 )] in at least three samples and genes encoded in mitochondrial DNA were removed.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### A sex-biased imbalance between Tfr, Tph, and atypical B cells determines antibody responses in COVID-19 patients. (PNAS 2023)

- DOI: 10.1073/pnas.2217902120 | PMCID: PMC9942838 | PMID: 36669118
- Evidence: Differential cluster abundance analysis by edgeR was performed with diffcyt (v1.10.0) ( 71 ) as implemented in the CATALYST R package (v1.14.0).
- Full pipeline: quantification [edgeR] -> dimensionality reduction/clustering [UMAP, edgeR, ggplot2 v3.3.3] -> differential/statistical testing [edgeR, ggplot2 v3.3.3] -> stage not stated [R v4.0.3]

### Sec22b is a critical and nonredundant regulator of plasma cell maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2213056120 | PMCID: PMC9926242 | PMID: 36595686
- Evidence: The Bioconductor edgeR package was used to import raw counts into R statistical software and compute normalized log2 counts per millions of mapped reads using the weighted trimmed mean of M-values as the normalization procedure.
- Full pipeline: read trimming [Bioconductor, edgeR] -> alignment/mapping [Bioconductor, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [GSEA, clusterProfiler, fgsea] -> differential/statistical testing [Bioconductor, R, edgeR, limma]

### Glutamate-GABA imbalance mediated by miR-8-5p and its STTM regulates phase-related behavior of locusts. (PNAS 2023)

- DOI: 10.1073/pnas.2215660120 | PMCID: PMC9910461 | PMID: 36574679
- Evidence: DEGs were analyzed using EdgeR software.
- Full pipeline: alignment/mapping [HISAT2] -> stage not stated [ImageJ, StringTie, edgeR]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: 20 , 21 . edgeR package in R was used to identify the differentially expressed genes in OIR compared to normoxia at each time point, with an FDR threshold of 0.05.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Evidence: Transcripts Per Million (TPMs) were extracted from the RSEM gene-level results, and the corresponding RSEM-calculated expected counts were used with EdgeR ( 62 ) for between-sample normalization and differential expression analysis.
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### DPF2 reads histone lactylation to drive transcription and tumorigenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2421496121 | PMCID: PMC11648877 | PMID: 39636855
- Version used: **3.055**
- Evidence: Differential gene expression analyses were performed using the “exactTest” function in edgeR v3.055.
- Full pipeline: differential/statistical testing [edgeR v3.055] -> stage not stated [ImageJ]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; inositol hexaphosphate pathways couple to RNA interference and pathogen defense. (PNAS 2024)

- DOI: 10.1073/pnas.2416982121 | PMCID: PMC11626161 | PMID: 39602251
- Evidence: Expression values were estimated, and differentially expressed transcripts were identified using EdgeR.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> differential/statistical testing [edgeR] -> stage not stated [ImageJ]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: First, genes were filtered for those expressed using “edgeR” ( 67 ) function “filterByExp” and defining treatment groups.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Genome-wide profiling of soybean WRINKLED1 transcription factor binding sites provides insight into seed storage lipid biosynthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2415224121 | PMCID: PMC11551420 | PMID: 39475647
- Evidence: The EdgeR package (v3.10.5) was used to obtain normalized expression values using the Trimmed Mean of M-values (TMM) method, and to identify differentially expressed genes between the different genotypes (FDR < 0.05).
- Full pipeline: read trimming [edgeR] -> variant calling [edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [HOMER, MACS2]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: We then used edgeR to normalize and calculate CPM and LCPM matrices.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### Gut bacteria of lepidopteran herbivores facilitate digestion of plant toxins. (PNAS 2024)

- DOI: 10.1073/pnas.2412165121 | PMCID: PMC11494336 | PMID: 39392666
- Evidence: Statistical analysis of OTU abundance and gene expression was performed using R package edgeR.
- Full pipeline: quantification [edgeR] -> differential/statistical testing [R, edgeR]

### Free-swimming bacteria transcriptionally respond to shear flow. (PNAS 2024)

- DOI: 10.1073/pnas.2406688121 | PMCID: PMC11494325 | PMID: 39383001
- Evidence: Thereafter, read counts were loaded into R and normalized using edgeR’s Trimmed Mean of M values algorithm ( 42 ), and the values were converted to counts per million.
- Full pipeline: quality control [HISAT2, featureCounts] -> read trimming [HISAT2, edgeR, featureCounts] -> alignment/mapping [HISAT2, featureCounts] -> quantification [HISAT2, edgeR, featureCounts] -> normalisation [edgeR] -> stage not stated [ImageJ]

### Local adaptation, plasticity, and evolved resistance to hypoxic cold stress in high-altitude deer mice. (PNAS 2024)

- DOI: 10.1073/pnas.2412526121 | PMCID: PMC11474095 | PMID: 39352929
- Evidence: Three outlier samples (three lung, one right ventricle) were removed following visual inspection of multidimensional scaling plots using plotMDS in edgeR ( 75 ) following Chen et al.
- Full pipeline: alignment/mapping [featureCounts v2.0.3] -> normalisation [edgeR] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [R, lme4] -> stage not stated [WGCNA]

### Genetic variation drives cancer cell adaptation to ECM stiffness. (PNAS 2024)

- DOI: 10.1073/pnas.2403062121 | PMCID: PMC11441511 | PMID: 39302966
- Evidence: The edgeR package ( 63 , 64 ) (version 3.36.0) in R (version 4.1.3) was employed for the statistical analysis of the differential methylation data.
- Full pipeline: read trimming [Bismark] -> alignment/mapping [Bismark] -> differential/statistical testing [R v4.1.3, edgeR] -> stage not stated [GSEA v4.1.0, ImageJ, Trim Galore]

### FicD sensitizes cellular response to glucose fluctuations in mouse embryonic fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2400781121 | PMCID: PMC11420183 | PMID: 39259589
- Evidence: To ensure this loss of response was not an artifact of our RNA seq analysis with EdgeR, we compared the EdgeR-defined DEGs to those defined by additional methods (DESeq2, NOISeq, and limma).
- Full pipeline: stage not stated [DESeq2, edgeR, limma]

### Qki5 safeguards spinal motor neuron function by defining the motor neuron-specific transcriptome via pre-mRNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2401531121 | PMCID: PMC11406248 | PMID: 39226364
- Evidence: Differential expression statistics of mRNA abundance were performed with EdgeR.
- Full pipeline: alignment/mapping [Metascape] -> quantification [Metascape, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: To quantify gene expression levels, Transcripts Per Million (TPM) values were computed using the EdgeR program.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Polyomavirus ALTOs, but not MTs, downregulate viral early gene expression by activating the NF-κB pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2403133121 | PMCID: PMC11348336 | PMID: 39141346
- Evidence: Differential expression comparisons between relevant sample groups were performed using Bioconductor’s edgeR ( 43 ).
- Full pipeline: alignment/mapping [Clustal Omega, STAR] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [GSEA]

### Oxysterol binding protein regulates the resolution of TLR-induced cytokine production in macrophages. (PNAS 2024)

- DOI: 10.1073/pnas.2406492121 | PMCID: PMC11331125 | PMID: 39361877
- Version used: **3.26.8**
- Evidence: Normalization (to find counts-per-million (CPM) for each gene) and differential analysis of gene expression was calculated using edgeR version 3.26.8 ( 51 ).
- Full pipeline: quality control [FastQC v0.11.5] -> quantification [ImageJ, limma] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [R, edgeR v3.26.8, limma] -> stage not stated [GSEA, MACS2 v2.1.0, featureCounts]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: To format counts for modeling of differential accessibility in limma, we created a DGElist object and applied calcnormFactors with edgeR (Version 3.34.1) ( 51 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Version used: **3.18**
- Evidence: RPKM values were calculated through R Bioconductor package EdgeR 3.18 ( 87 ).
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### Psychosocial experiences are associated with human brain mitochondrial biology. (PNAS 2024)

- DOI: 10.1073/pnas.2317673121 | PMCID: PMC11228499 | PMID: 38889126
- Evidence: Pseudo-bulk UMI counts normalization was done by using the trimmed mean of M-values (TMM) method of edgeR, and log2 of counts per million174 mapped reads (CPM) were calculated using the voom function of limma (version 3.44.3).
- Full pipeline: read trimming [edgeR, limma v3.44.3] -> alignment/mapping [edgeR, limma v3.44.3] -> normalisation [edgeR, limma v3.44.3] -> differential/statistical testing [R v4.0.4] -> stage not stated [Bioconductor]

### <i>Rickettsia</i> symbionts spread via mixed mode transmission, increasing female fecundity and sex ratio shift by host hormone modulating. (PNAS 2024)

- DOI: 10.1073/pnas.2406788121 | PMCID: PMC11194588 | PMID: 38865267
- Evidence: The edgeR package ( 66 ) was used to identify differentially expressed genes across samples with the absolute value of log 2 ratio ≥ 1 and FDR < 0.01. qRT-PCR. qRT-PCR was conducted as previously described ( 58 , 59 ).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, MAFFT v7.520] -> differential/statistical testing [edgeR] -> structure determination [MrBayes v3.2.7]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles up-regulate and directly transfer adherence factors promoting host cell colonization. (PNAS 2024)

- DOI: 10.1073/pnas.2401159121 | PMCID: PMC11194581 | PMID: 38865261
- Evidence: Briefly, transcript quantification data were summarized to genes using the tximport package and normalized using the trimmed mean of M values (TMM) method in edgeR ( 75 ).
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [Galaxy]

### Premeiotic 24-nt phasiRNAs are present in the <i>Zea</i> genus and unique in biogenesis mechanism and molecular function. (PNAS 2024)

- DOI: 10.1073/pnas.2402285121 | PMCID: PMC11127045 | PMID: 38739785
- Version used: **4.0.2**
- Evidence: Reads mapped to PHAS loci or miRNAs were counted using featureCounts v1.6.3 ( 48 ) with parameter -M and normalized to CPM using edgeR v4.0.2 ( 49 ).
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MUSCLE, edgeR v4.0.2, featureCounts v1.6.3] -> normalisation [edgeR v4.0.2, featureCounts v1.6.3] -> stage not stated [BEDTools v2.29.2, StringTie v2.1.7]

### Cancer-stromal cell interactions in breast cancer brain metastases induce glycocalyx-mediated resistance to HER2-targeting therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322688121 | PMCID: PMC11098130 | PMID: 38709925
- Evidence: Briefly, raw counts were downloaded from the resource paper, which were then converted to Log2 transformed TMM-normalized counts per million [log2 (TMM-CPM + 1)] using edgeR ( 58 ).
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v1.18.1] -> normalisation [edgeR] -> differential/statistical testing [DESeq2 v1.18.1, MACS2 v2.1.1.20160309] -> stage not stated [GSEA, GSVA]

### PML::RARA and GATA2 proteins interact via DNA templates to induce aberrant self-renewal in mouse and human hematopoietic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2317690121 | PMCID: PMC11067031 | PMID: 38648485
- Evidence: ( F–I ) Normalized peptide spectral counts of PML ( F ), RARA ( G ), EP300 ( H ), and GATA2 ( I ) following proximity labeling . **** FDR ≤ 1e-24, **FDR ≤ 0.01, *FDR ≤ 0.05, and n.s. = not significant by edgeR ( 59 ).
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [HOMER]

### Improved RNA stability estimation through Bayesian modeling reveals most <i>Salmonella</i> transcripts have subminute half-lives. (PNAS 2024)

- DOI: 10.1073/pnas.2308814121 | PMCID: PMC10998600 | PMID: 38527194
- Evidence: Log-fold changes were calculated using glmQLFit from edgeR ( 26 ) with a cutoff of 0.25 on the log-fold changes.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [Cutadapt v4.1, HTSeq] -> quantification [HTSeq] -> normalisation [Stan] -> differential/statistical testing [GSEA, Stan] -> simulation/modelling [Stan] -> stage not stated [R, edgeR, limma]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: Differently expressed genes were analyzed using RSEM ( 55 ) and edgeR ( 56 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### tRNA epitranscriptome determines pathogenicity of the opportunistic pathogen <i>Pseudomonas aeruginosa</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2312874121 | PMCID: PMC10945773 | PMID: 38451943
- Evidence: Gene expression was normalized (using trimmed mean of M-values and counts per million from the R package edgeR).
- Full pipeline: read trimming [R, edgeR] -> normalisation [R, edgeR]

### COP1 controls light-dependent chromatin remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2312853121 | PMCID: PMC10895365 | PMID: 38349881
- Evidence: Differentially expressed genes were determined with edgeR over three biological replicates.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, deepTools] -> normalisation [deepTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [ImageJ, MACS2]

### Phase separation of YAP-MAML2 differentially regulates the transcriptome. (PNAS 2024)

- DOI: 10.1073/pnas.2310430121 | PMCID: PMC10873646 | PMID: 38315854
- Evidence: STAR was used to map reads to the human genome (hg38) by default setting. edgeR was applied to the raw counts to identify DEG.
- Full pipeline: dimensionality reduction/clustering [ImageJ] -> stage not stated [edgeR, fastp]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: TMM normalization and differential expression analysis used edgeR package ( 38 ) with adjusted P -value (FDR) < 0.05 and |log 2 FC | > 1.5 criteria.
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### CRISPR-based screening of small RNA modulators of bile susceptibility in <i>Bacteroides thetaiotaomicron</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2311323121 | PMCID: PMC10861873 | PMID: 38294941
- Version used: **3.32.1**
- Evidence: Differential abundance analysis of library members was calculated with edgeR (3.32.1).
- Full pipeline: quantification [edgeR v3.32.1] -> differential/statistical testing [edgeR v3.32.1] -> stage not stated [Python]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Version used: **3.36.0**
- Evidence: The signal was TMM normalized ( 54 ) with calculated normalization factors using edgeR (v3.36.0) ( 55 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### The sleep-wake history contributes to rhythmic BMAL1 chromatin binding in the cerebral cortex but not in the liver. (PNAS 2025)

- DOI: 10.1073/pnas.2515047122 | PMCID: PMC12685114 | PMID: 41296730
- Evidence: The Diffbind’s EdgeR implementation ( 73 ) was used to count aligned reads.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, MultiQC, edgeR] -> visualisation [MultiQC] -> stage not stated [R]

### The immunoproteasome regulates ILC2 responses by modulating mitochondrial capacity. (PNAS 2025)

- DOI: 10.1073/pnas.2518190122 | PMCID: PMC12663963 | PMID: 41264257
- Evidence: Differential gene expression analysis was performed in R ( 4 ) using edgeR.
- Full pipeline: read trimming [fastp] -> quantification [ImageJ] -> differential/statistical testing [R, edgeR] -> stage not stated [QuPath]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Version used: **4.1.25**
- Evidence: The number of reads mapped to each gene was counted using featureCounts v2.0.6 with a reference gene model (XL_9.1 _ v1.8.3.2.primaryTranscripts.gff3; Xenbase) ( 32 , 78 ) and compared using edgeR v4.1.25 ( 82 ) to detect DEGs (FDR < 0.05) between groups.
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Version used: **2.10.0**
- Evidence: Differential expression analysis for RNA was performed using R package edgeR (version 2.10.0) ( 47 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Evidence: Differentially expressed genes were inferred based on edgeR based on the negative binomial distribution model, and genes that showed |log2(FoldChange)| ≥ 1 & padj ≤ 0.05 were regarded as differentially expressed ( Dataset S01 ) ( 39 ).
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### Glycosylated cannabinoids in &lt;i&gt;Cannabis sativa&lt;/i&gt; and enzyme design to modulate their synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2515688122 | PMCID: PMC12501178 | PMID: 40991441
- Evidence: Using the “edgeR” R package, raw counts were normalized by CMP normalization, and low-expressed genes were filtered out ( Dataset S2 ).
- Full pipeline: normalisation [R, edgeR] -> stage not stated [AlphaFold, ColabFold, ImageJ]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Gene expression data were normalized using the TMM method in edgeR ( 34 ) (v4.2.0), and DEGs were identified using limma-voom ( 35 ) (v3.60.0).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Inorganic sulfate is critical for &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; lung tissue colonization and redox balance. (PNAS 2025)

- DOI: 10.1073/pnas.2503966122 | PMCID: PMC12501120 | PMID: 40982672
- Evidence: The filtration of low-abundance reads, normalization, DEG analysis, and z-score calculation were carried out using edgeR ( 74 ).
- Full pipeline: read trimming [Cutadapt v4.9] -> quantification [edgeR] -> normalisation [edgeR] -> stage not stated [ImageJ]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: The bulk RNA-seq pipeline conducted a differential expression analysis on the counts matrix using EdgeR.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: DEGs was calculated using edgeR ( 47 ) with the threshold of FDR < 0.05 and fold change ≥ 2.
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: We used the R package edgeR ( 77 ) to filter and normalize our data prior analysis.
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Patient stratification reveals the molecular basis of disease co-occurrences. (PNAS 2025)

- DOI: 10.1073/pnas.2421060122 | PMCID: PMC12415287 | PMID: 40880536
- Evidence: We performed quality controls using the edgeR pipeline ( 15 ) and we applied within-sample normalization by considering the logarithm of the counts-per-million (log 2 CPM).
- Full pipeline: quality control [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [GSEA, limma]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: ...arnings and messages library(clusterProfiler), library(matrixStats), library(gplots), library(RColorBrewer), library(sqldf), library(hopach), library(edgeR), library(limma), library(GOstats), library(GO.db), library(org.Hs.eg.db), library(org.Mm.eg.db), library(data.table), library(circlize), library(gridExtra), library(ggplot2), library(dplyr)})) # Set new working directory setwd(“”) # Load signi...
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Evidence: The read-count matrix was normalized, and genes expressing transcripts at ≥3 cpm were retained after filtering with edgeR ( 47 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### Mobile gene clusters and coexpressed plant-rhizobium pathways drive partner quality variation in symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2411831122 | PMCID: PMC12337268 | PMID: 40729388
- Evidence: Genes with expression below the cutoff in three out of four replicates are labeled as “absent” in that strain, following a criterion adapted from the filterByExpr function in the edgeR package ( 123 , 124 ) in R ( 122 ) (v4.1.0).
- Full pipeline: differential/statistical testing [R] -> stage not stated [WGCNA, edgeR, eggNOG]

### Sharks and rays have the oldest vertebrate sex chromosome with unique sex determination mechanisms. (PNAS 2025)

- DOI: 10.1073/pnas.2513676122 | PMCID: PMC12318234 | PMID: 40694337
- Version used: **3.42.4**
- Evidence: DEGs were detected by edgeR v3.42.4 ( 97 ).
- Full pipeline: stage not stated [edgeR v3.42.4]

### Complementary genetic and epigenetic changes facilitate rapid adaptation to multiple global change stressors. (PNAS 2025)

- DOI: 10.1073/pnas.2422782122 | PMCID: PMC12305003 | PMID: 40663607
- Evidence: Differentially methylated regions were identified in R version 3.6.0 ( 67 ) using edgeR following the methods described in Chen et al.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bismark v0.22.3, Bowtie2 v2.2.6] -> differential/statistical testing [R v3.6.0, edgeR] -> stage not stated [BEDTools, DESeq2]

### Multiorgan transcriptomics in mice identifies immunoglobulin heavy constant mu (&lt;i&gt;Ighm&lt;/i&gt;) as a tissue-level aging biomarker. (PNAS 2025)

- DOI: 10.1073/pnas.2423142122 | PMCID: PMC12280941 | PMID: 40643973
- Version used: **4.2.1**
- Evidence: Data visualization and analysis were conducted using R platform, with the packages including Rtsne (v0.17) ( 29 ), DESeq2 (v1.44.0) ( 30 ), edgeR (v4.2.1) ( 31 ), and variancePartition (v1.35.5) ( 32 ).
- Full pipeline: read trimming [fastp v0.23.1] -> alignment/mapping [STAR v2.7.11b] -> quantification [ImageJ] -> dimensionality reduction/clustering [edgeR v4.2.1] -> visualisation [edgeR v4.2.1] -> stage not stated [DESeq2, R v4.4.1]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: Low abundance was filtered out, and the remaining transcript counts (median logTPM > 1) were normalized using the EdgeR package to produce counts-per-million values for each sample.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### Multiomics integration prioritizes potential drug targets for multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2425537122 | PMCID: PMC12232717 | PMID: 40577117
- Evidence: DEA was originally performed in this study across 14 blood cell types using the Bayes factor method and the EdgeR method.
- Full pipeline: differential/statistical testing [COLOC v5.2.3, R] -> stage not stated [TwoSampleMR, edgeR]

### Heritable symbiont producing nonribosomal peptide confers extreme heat sensitivity and antifungal protection on its host. (PNAS 2025)

- DOI: 10.1073/pnas.2509873122 | PMCID: PMC12232616 | PMID: 40569380
- Evidence: Thermo Fisher raw files were processed using Proteome Discoverer 2.5 to identify proteins, then differentially enriched proteins (DEPs) identified by trimmed mean of M-value (TMM) normalization of peptide spectral match counts followed by the RUVr/EdgeR quasi-likelihood test, as implemented in Degust ( 51 ).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [MAFFT v7.520, OrthoFinder v2.5.5] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [R, survival (R)]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles suppress IFNε-mediated responses driven by its intracellular bacterial symbiont &lt;i&gt;Mycoplasma hominis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2508297122 | PMCID: PMC12232435 | PMID: 40560611
- Evidence: Briefly, transcript quantification data were summarized to genes using the tximport package and normalized using the trimmed mean of M values (TMM) method in edgeR ( 89 ).
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [GSEA]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: Differential gene expression was analyzed by RSEM ( 58 ) and edgeR ( 59 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: Differential analysis was performed using the limma-voom procedure ( 26 , 27 ) after TMM-normalization ( 28 ) of gene-level counts with calcNormFactors of edgeR ( 29 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### &lt;i&gt;Hamiltonella&lt;/i&gt; symbionts benefit whitefly fertilization by regulating the maternal protein Tudor-mediated piRNA pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2427053122 | PMCID: PMC12184435 | PMID: 40504144
- Evidence: The edgeR package was used to identify differentially expressed genes across samples with the absolute value of log 2 ratio ≥ 1 and a P -value < 0.05.
- Full pipeline: differential/statistical testing [edgeR] -> visualisation [PyMOL v3.1.0] -> stage not stated [AlphaFold, BLAST, ImageJ]

### Spatiotemporal regulation of target mRNA cleavage by 21-nt phasiRNAs in maize anthers. (PNAS 2025)

- DOI: 10.1073/pnas.2422647122 | PMCID: PMC12184425 | PMID: 40498447
- Evidence: Asterisks indicate significant differences ( P ≤ 0.05, calculated by edgeR).
- Full pipeline: quantification [featureCounts v2.0.1] -> stage not stated [edgeR]

### A synthetic jasmonate receptor agonist uncouples the growth-defense trade-off in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2505675122 | PMCID: PMC12184649 | PMID: 40493190
- Evidence: DEGs were analyzed using the R package edgeR ( 39 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> stage not stated [edgeR]

### Structure and organization of full-length epidermal growth factor receptor in extracellular vesicles by cryo-electron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2424678122 | PMCID: PMC12167996 | PMID: 40455995
- Evidence: VLP/EVs containing the protein of interest, differential protein enrichment was computed using the RUVr edgeR-quasi-likelihood model implemented in Degust ( 73 ), requiring a minimum count of two PSMs in at least two samples, and normalizing by Trimmed Mean of M-values.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [IMOD] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX] -> visualisation [EMAN2] -> stage not stated [AlphaFold, ImageJ, MotionCor2, RELION]

### Transcriptomic and proteomic ramifications of segmental amplification in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2422424122 | PMCID: PMC12107188 | PMID: 40372434
- Evidence: Differential expression analysis was performed in R v4.3.1/RStudio (Posit team; Boston, MA) with the following Bioconductor/R packages: edgeR ( 66 , 67 ), limma ( 68 ), glimma, gplots, RcolorBrewer, and Nonnegative Matrix Factorization.
- Full pipeline: differential/statistical testing [Bioconductor, R v4.3, edgeR, limma]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Evidence: Differentially accessible regions (DARs) between each group were assessed using edgeR ( 81 ).
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Bacterial extracellular vesicles target different bacterial species, impairing cell division and diminishing their pathogenicity. (PNAS 2025)

- DOI: 10.1073/pnas.2416652122 | PMCID: PMC12067206 | PMID: 40299696
- Evidence: The differential expression analysis was performed using the edgeR package v3.19 in R ( 59 ) and genes with a P -value below 0.01 and an absolute fold-change of more thanÂ 1.5 were considered to be differentially expressed between the two groups, EV- and Tris-HCl-treated GAS.
- Full pipeline: differential/statistical testing [R, edgeR] -> stage not stated [Cytoscape, ImageJ]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Version used: **4.2.2**
- Evidence: TMM normalization and differential gene expression analysis were performed using the R packages edgeR (v4.2.2) and limma (v3.60.2), respectively.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### microRNA-218-5p coordinates scaling of excitatory and inhibitory synapses during homeostatic synaptic plasticity. (PNAS 2025)

- DOI: 10.1073/pnas.2500880122 | PMCID: PMC12002172 | PMID: 40172961
- Evidence: The general workflow of the differential analysis consisted of genome alignment using Salmon ( 68 ), count-filtering and surrogate variable analysis using the R-package sva ( 69 ), and normalization and model fitting using edgeR ( 70 ).
- Full pipeline: alignment/mapping [edgeR] -> normalisation [edgeR, lme4] -> differential/statistical testing [R v4.0, edgeR] -> stage not stated [emmeans]

### Control of circadian muscle glucose metabolism through the BMAL1-HIF axis in obesity. (PNAS 2025)

- DOI: 10.1073/pnas.2424046122 | PMCID: PMC12002348 | PMID: 40127275
- Evidence: ( D ) Normalized counts (from edgeR) for select genes which were rescued in d mKO mice.
- Full pipeline: normalisation [edgeR] -> stage not stated [HOMER]

### Red-light signaling pathway activates desert cyanobacteria to prepare for desiccation tolerance. (PNAS 2025)

- DOI: 10.1073/pnas.2502034122 | PMCID: PMC11962455 | PMID: 40112114
- Version used: **3.20.7**
- Evidence: Clean reads were aligned to the reference genome with Rockhopper, and differential expression analysis was conducted using edgeR v3.20.7.
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [edgeR v3.20.7] -> dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [edgeR v3.20.7] -> stage not stated [AlphaFold, PyMOL]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Version used: **3.42.4**
- Evidence: Filtering out lowly expressed genes (13,613 genes were kept), normalization and differential expression analysis were performed with the R/Bioconductor package edgeR v.3.42.4 ( 66 ), and statistical significance was assessed with a general linear model, negative binomial distribution, and quasi-likelihood F test.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Evidence: Differentially expressed genes (DEGs) for the different lines were estimated using “ edgeR ” ( 65 ) in R (v4.1.2, R Core Team 2021).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### Light-controlled disruption of cancer cell dormancy via photoswitchable stress hormone receptor degraders. (PNAS 2026)

- DOI: 10.1073/pnas.2528760123 | PMCID: PMC13214037 | PMID: 42166243
- Evidence: Lowly expressed genes were filtered using filterByExpr() from edgeR, and surrogate variable analysis was performed using SEtools::svacor to correct for hidden batch effects.
- Full pipeline: quantification [R] -> normalisation [edgeR] -> differential/statistical testing [R] -> stage not stated [GSEA]

### Suppression rather than activation of the integrated stress response (GCN2-ATF4) pathway extends lifespan in the fly. (PNAS 2026)

- DOI: 10.1073/pnas.2518812123 | PMCID: PMC13142962 | PMID: 42048457
- Evidence: Differential expression analysis was done using the edgeR package and “glmFit” ( 115 ) using an additive model of diet and transgene induction.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [GSEA, edgeR] -> stage not stated [R, minimap2 v2.24]

### Targeting CRTC2 reverses &lt;i&gt;STK11&lt;/i&gt; mutant NSCLC tumor resistance to immunotherapy. (PNAS 2026)

- DOI: 10.1073/pnas.2508762123 | PMCID: PMC13123801 | PMID: 42018410
- Evidence: The EdgeR package was used for Trimmed Mean of M-values (TMM) normalization and differential gene expression analysis ( 41 ).
- Full pipeline: read trimming [edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### A two-component system signaling hub controls enterococcal membrane remodeling in response to daptomycin. (PNAS 2026)

- DOI: 10.1073/pnas.2532437123 | PMCID: PMC13123819 | PMID: 42012956
- Version used: **3.42.4**
- Evidence: Transcriptional differences between DAP-treated and untreated cells (RNA-Seq) were assessed using edgeR (version 3.42.4) and setting an FDR-adjusted P -value of 0.05 as cutoff.
- Full pipeline: differential/statistical testing [edgeR v3.42.4]

### FABP7 controls radial glial scaffold stability during human cortical development. (PNAS 2026)

- DOI: 10.1073/pnas.2523130123 | PMCID: PMC13099611 | PMID: 41984827
- Version used: **3.40.2**
- Evidence: ...ery/acc.cgi?acc=GSE304516 ) ( 47 ); Seurat (v4.4.0, https://satijalab.org/seurat/ ) ( 48 ) for single-cell RNA-seq data normalization and clustering; edgeR (v3.40.2) ( 49 ) for differential gene expression analysis; hdWGCNA (v0.4.00, https://smorabit.github.io/hdWGCNA/ ) ( 50 ) for weighted gene co-expression network construction; irGSEA (v3.3.2, https://github.com/chuiqin/irGSEA ) ( 51 ) for gene...
- Full pipeline: normalisation [Seurat v4.4.0, edgeR v3.40.2] -> dimensionality reduction/clustering [Seurat v4.4.0, UMAP, edgeR v3.40.2] -> differential/statistical testing [Seurat v4.4.0, edgeR v3.40.2] -> visualisation [UMAP] -> stage not stated [GSEA, WGCNA]

### The Nemp1-Nesprin complex mediates cellular responses to matrix mechanics. (PNAS 2026)

- DOI: 10.1073/pnas.2521253123 | PMCID: PMC12956887 | PMID: 41730104
- Evidence: Differential gene expression analysis was then carried out using the R package, edgeR [2].
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [Salmon v1.8.0] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [R, clusterProfiler v4.10.1, edgeR] -> visualisation [pheatmap v1.0.12]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: Genes with 0 counts across all samples were filtered out and the remaining counts were then normalized using TMM with edgeR ( 52 ).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Antagonism of RNA silencing in the yellow fever mosquito, &lt;i&gt;Aedes aegypti&lt;/i&gt;, by the nsP2 protein of the prototype alphavirus. (PNAS 2026)

- DOI: 10.1073/pnas.2521417123 | PMCID: PMC12913014 | PMID: 41662525
- Evidence: For differential expression analysis between replicate datasets, we used the edgeR Bioconductor package ( https://bioconductor.org/packages/release/bioc/html/edgeR.html ).
- Full pipeline: differential/statistical testing [Bioconductor, edgeR]

### Plant-fungi interactions in &lt;i&gt;Marchantia polymorpha&lt;/i&gt; are associated with horizontal gene transfer and terpene metabolism. (PNAS 2026)

- DOI: 10.1073/pnas.2532723123 | PMCID: PMC12890914 | PMID: 41637459
- Evidence: Differentially expressed genes were identified using the edgeR package ( 58 ) in R v4.4.0, separately on each accession.
- Full pipeline: quality control [Nextflow v21.10.6] -> alignment/mapping [Nextflow v21.10.6] -> differential/statistical testing [R v4.4, edgeR] -> stage not stated [BLAST, GEMMA]

### A factor integrating transcription and repression of surface antigen genes in African trypanosomes. (PNAS 2026)

- DOI: 10.1073/pnas.2531377123 | PMCID: PMC12890818 | PMID: 41632842
- Evidence: Two methods were used to calculate statistical significance: using the two-tailed t test of log-transformed RPKM of the three induced to three uninduced samples, and using EdgeR v4 with FDR-correction ( 64 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [BLAST, ImageJ]

### Combination antiviral and anti-inflammatory therapy mitigates persistent neurological deficits in mice post SARS-CoV-2 infection. (PNAS 2026)

- DOI: 10.1073/pnas.2530209123 | PMCID: PMC12799161 | PMID: 41499397
- Evidence: DEGs were identified using the edgeR (negative binomial) feature in CLCGWB (Qiagen, Redwood City, CA) using raw read counts.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.5, Seurat v5.3.0, pheatmap]

### Dietary folic acid prevents peripheral neuropathy in mouse models of neural tube defects and type 2 diabetes. (PNAS 2026)

- DOI: 10.1073/pnas.2528095123 | PMCID: PMC12773702 | PMID: 41481435
- Version used: **3.42.2**
- Evidence: Differential gene expression (DEG) analysis was performed using the R package edgeR v3.42.2 ( 67 ) to compare different conditions.
- Full pipeline: read trimming [fastp v0.20, kallisto v0.46.1] -> alignment/mapping [kallisto v0.46.1] -> quantification [kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [R v3.42.2, edgeR v3.42.2] -> stage not stated [ImageJ]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: For each gene expression analysis, we performed trimmed mean of M values (TMM) normalization and gene-wise generalized linear model regression by edgeR, and the genes displaying significant differential expression were selected according to the following criteria: FDR ≤ 0.05 and |log2(FoldChange)| ≥ 1.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### SPL13 controls a root apical meristem phase change by triggering oriented cell divisions. (Science 2024)

- DOI: 10.1126/science.ado4298 | PMCID: PMC7616863 | PMID: 39541454
- Evidence: The analysis was performed with R software package edgeR (R version 3.5.1).
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [R v3.5.1, edgeR, ggplot2 v3.4.3]

### PIEZO channels link mechanical forces to uterine contractions in parturition. (Science 2025)

- DOI: 10.1126/science.ady3045 | PMCID: PMC12807505 | PMID: 41231991
- Evidence: Differentially expressed genes in each cell type were identified using SVA-EdgeR following a previously published procedure ( 83 ).
- Full pipeline: alignment/mapping [Seurat] -> quantification [CellProfiler] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy, edgeR] -> visualisation [UMAP] -> stage not stated [scDblFinder]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Read counts were adjusted for normalization and filtered in R via package EdgeR ( 51 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

