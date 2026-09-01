# ComplexHeatmap

- **Category:** general
- **Papers in survey:** 119
- **Journals:** Nature (57), PNAS (43), Cell (16), Science (3)
- **Years:** 2021 (14), 2022 (18), 2023 (27), 2024 (18), 2025 (29), 2026 (13)
- **Versions named:** 2.6.2 (6), 2.14.0 (4), 2.11.1 (4), 2.16.0 (3), 2.4.3 (3), 2.10.0 (3), 2.2.0 (3), 2.12.1 (1), 2.18.0 (1), 2.12.0 (1)
- **Pipeline stages it appears in:** visualisation (49), dimensionality reduction/clustering (25), normalisation (10), differential/statistical testing (8), quantification (3), variant calling (1)

## Papers

### The interferon landscape along the respiratory tract impacts the severity of COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.016 | PMCID: PMC8373821 | PMID: 34492226
- Evidence: ...ampliSeqRNA plugin ThermoFisher N/A CIBERSORTx Newman et al., 2019 N/A Fast Gene Set Enrichment Analysis package (fGSEA) Korotkevich et al., 2021 N/A ComplexHeatmap package Gu et al., 2016 N/A Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the lead contact, Ivan Zanoni ( ivan.zanoni@childrens.harvard.edu...
- Full pipeline: stage not stated [ComplexHeatmap, GSEA, MACS2]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Version used: **2.7.3**
- Evidence: ...clize v0.4.11 CRAN https://CRAN.R-project.org/package=circlize R package – ggplot2 v3.3.2 CRAN https://CRAN.R-project.org/package=ggplot2 R package – ComplexHeatmap v2.7.3 Bioconductor https://bioconductor.org/packages/ComplexHeatmap/ R package – fgsea v1.16.0 Bioconductor https://bioconductor.org/packages/fgsea/ Python Programming Language v3.8.3 Python https://www.python.org Python package scVel...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **2.4.2**
- Evidence: Density heatmaps were produced using the ‘densityHeatmap’ function from the R package ComplexHeatmap (version 2.4.2), and clustering was completed using Euclidean distance and Ward’s method ( Murtagh and Legendre, 2014 ; Gu, Eils and Schlesner, 2016 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Version used: **2.2.0**
- Evidence: ... et al., 2015 https://www.bioconductor.org/packages/release/bioc/html/limma.html Tidyverse (1.2.1, 1.3.0) ( Wickham, 2019 ) https://www.tidyverse.org ComplexHeatmap (2.2.0) Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html edgeR (3.26.8, 3.28.1) McCarthy et al., 2012 https://bioconductor.org/packages/release/bioc/html/edgeR.html FGSEA (1.10.1) Sergushichev, 20...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Evidence: ...s://bioconductor.org/packages/release/bioc/html/DESeq2.html ComplexHeatMap v2.0.0 Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html VennDiagram v1.6.20 CRAN https://rdrr.io/cran/VennDiagram/ GSEA 4.1.0 Subramanian et al., 2005 and Mootha et al., 2003 https://www.gsea-msigdb.org/gsea/login.jsp;jsessionid=94213B4581121AA02E710A5BE27FBE9F CellRanger v3.1.0 10x Ge...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Version used: **2.6.2**
- Evidence: 93 https://github.com/theislab/scvelo Monocle 3 (version: 1.0.0) 68,88 https://github.com/cole-trapnell-lab/monocle3 pySCENIC (version: 0.11.2) 59,94 https://github.com/aertslab/pySCENIC ComplexHeatmap (version 2.6.2) Gu et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **2.4.3**
- Evidence: Graphics were generated using the ggplot2 3.3.3 ( Wickham, 2009 ), ComplexHeatmap 2.4.3 ( Gu et al., 2016 ), pheatmap 1.0.12 ( Kolde, 2019 ), igraph 1.2.6 ( Csardi and Nepusz, 2006 ), RCy3 2.8.1 ( Gustavsen et al., 2019 ), stringr 1.4.0 ( Wickham, 2019 ), dplyr 1.0.6 ( Wickham et al., 2020 ), and RColorBrewer 1.1-2 ( Neuwirth, 2014 ) R package.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Non-canonical odor coding in the mosquito. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.024 | PMCID: PMC9480278 | PMID: 35985288
- Evidence: Antenna cell marker heatmap (on total cell population): The heatmap in Figure 4B was generated using normalized expression values and the ComplexHeatmap package in R ( R Core Team, 2021 ).
- Full pipeline: normalisation [ComplexHeatmap] -> stage not stated [ImageJ, R, Seurat, ggplot2, scDblFinder, tidyverse]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: .../github.com/CUHIMSR/CytofBatchAdjust ( Schuyler et al., 2019 ) uwot (R package) https://cran.r-project.org/web/packages/uwot/index.html v0.1.8 (CRAN) ComplexHeatmap (R package) ( Gu et al., 2016 ) v1.20.0 (Bioconductor) lme4 (R package) ( Nowicka et al., 2017 ) v1.1-21 (CRAN) multcomp (R package) ( Hothorn et al., 2008 ) v1.4-13 (CRAN) lsmeans (R package) ( Lenth, 2016 ) v2.30-0 (CRAN) phenoptr (R...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: Heatmaps were visualized using ComplexHeatmap.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **2.10.0**
- Evidence: Gene expression profiles across single-cells and metacells were visualized as heatmaps with the ComplexHeatmap 2.10.0 126 R library.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: 102 https://CRAN.R-project.org/package=PRROC ComplexHeatmap R package Guet al.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### Global, site-resolved analysis of ubiquitylation occupancy and turnover rate reveals systems properties. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.024 | PMCID: PMC11136510 | PMID: 38626770
- Version used: **2.6.2**
- Evidence: ...l R package: ggplot2 v3.3.5 N/A http://ggplot2.org/ R package: GGally v2.1.2 N/A https://cran.r-project.org/web/packages/GGally/index.html R package: ComplexHeatmap v2.6.2 Gu et al.
- Full pipeline: stage not stated [AlphaFold, ComplexHeatmap v2.6.2, PyMOL v2.5.0, Python v3.7.1, R, ggplot2 v3.3.5, tidyverse v1.0.5]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: A heatmap representing classical monocyte transcript abundance profiles ( z -score-scaled log 2 -normalized counts) was analyzed with ComplexHeatmap.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Version used: **2.14.0**
- Evidence: 180 The resulting binary state assignments (active or repressive compartments) across the 27,993 100-kb bins were grouped into 25 epigenomic compartment groups using K-means clustering (R kmeans function), and visualized using ComplexHeatmap (v.2.14.0) in R (v.4.2.2).
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Molecular features of human pathological tau distinguish tauopathy-associated dementias. (Cell 2026)

- DOI: 10.1016/j.cell.2025.12.036 | PMCID: PMC13075643 | PMID: 41616780
- Version used: **2.11.1**
- Evidence: Analyses were performed and figures were created in R (v4.1.0) using RStudio (v1.4.1717) with the packages R.utils (v2.11.0), stringr (v1.4.0), GetoptLong (v1.0.5), reshape2 (v1.4.4), circlize (v0.4.13), ComplexHeatmap (v2.11.1), dendsort (v0.3.4), dendextend (v1.15.2), ggplot2 (v3.3.5), ggpubr (v0.4.0), ggdendro (v0.1.22), ggpmisc (v0.4.5), scales (v1.1.1), and gridExtra (v2.3).
- Full pipeline: visualisation [ComplexHeatmap v2.11.1, ggplot2 v3.3.5, ggpubr v0.4.0] -> stage not stated [R v4.1.0]

### Late Quaternary dynamics of Arctic biota from ancient environmental genomics. (Nature 2021)

- DOI: 10.1038/s41586-021-04016-x | PMCID: PMC8636272 | PMID: 34671161
- Evidence: The heat maps showing the mean of a genus’ proportions across all samples within an age interval were generated using the R package ComplexHeatmap 60 .
- Full pipeline: stage not stated [ComplexHeatmap, R, ggplot2]

### Structure-based classification predicts drug response in EGFR-mutant NSCLC. (Nature 2021)

- DOI: 10.1038/s41586-021-03898-1 | PMCID: PMC8481125 | PMID: 34526717
- Evidence: Heat map generation Heat maps and hierarchical clustering were generated by plotting the median log (Mut/WT) value for each cell line and each drug using R and the ComplexHeatmap package 40 2.6.2 (R Foundation for Statistical Computing).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, R] -> differential/statistical testing [ComplexHeatmap, R]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **2.2.0**
- Evidence: Heatmaps were plotted with R package ComplexHeatmap (v2.2.0) 43 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: 1a ) were clustered using z-score and a kmeans of 6 and plotted using ComplexHeatmap 56 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Heatmaps showing log2-fold-changes and enrichments of features such as Figure 5j,k were produced using ComplexHeatmap R package (v.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: RNA-seq data were visualized by using Prism software (v9.3.1; GraphPad) and the ComplexHeatmap R package (v2.2.0) 58 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### Signatures of copy number alterations in human cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04738-6 | PMCID: PMC9242861 | PMID: 35705804
- Evidence: Plotting was performed with base R or with packages ggplot2, ggrepel, RColorBrewer, circlize, ComplexHeatmap, colorspace, seriation, dendextend, beanplot and corrplot.
- Full pipeline: normalisation [RSEM] -> stage not stated [Beagle v5.1, ComplexHeatmap, R, ggplot2, survival (R), tidyverse]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Sex DEG log 2 [FC] values and NE-regulated ATAC site correlation coefficients were hierarchically clustered and visualized using ComplexHeatmap 92 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Omicron escapes the majority of existing SARS-CoV-2 neutralizing antibodies. (Nature 2022)

- DOI: 10.1038/s41586-021-04385-3 | PMCID: PMC8866119 | PMID: 35016194
- Evidence: Two-dimensional t -SNE plots are generated by ggplot2 (v.3.3.3), and heat maps are generated by the ComplexHeatmap package (v.2.6.2).
- Full pipeline: normalisation [MACS2, R] -> dimensionality reduction/clustering [ComplexHeatmap, R, ggplot2 v3.3.3] -> stage not stated [Python]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Evidence: Heatmaps were generated using the ComplexHeatmap 37 package in R.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Evidence: The matrix was plotted using the ComplexHeatmap package in R 79 .
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: OCRs with upregulated accessibility in both T pex and T ex cells compared with CD8 + T cells in acute LCMV infection (log 2 (FC) > 1, FDR < 0.05) were visualized using the Heatmap function in the ComplexHeatmap R package (v.2.8.0).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Dopaminergic systems create reward seeking despite adverse consequences. (Nature 2023)

- DOI: 10.1038/s41586-023-06671-8 | PMCID: PMC10632144 | PMID: 37880370
- Version used: **1.10.2**
- Evidence: The graphical representation was generated using the R package ComplexHeatmap v1.10.2.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [ComplexHeatmap v1.10.2, Cytoscape v3.9.1]

### Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment. (Nature 2023)

- DOI: 10.1038/s41586-023-06564-w | PMCID: PMC10567561 | PMID: 37758944
- Evidence: To plot the heatmap to present the qPCR results, gene expression was scaled and mean centred (using the ‘scale’ function in R) and the heatmap was plotted using the ‘ComplexHeatmap’ package.
- Full pipeline: normalisation [ComplexHeatmap, R, Seurat] -> visualisation [ComplexHeatmap] -> stage not stated [Fiji v1.0, ImageJ v1.0, ggplot2]

### Distinguishing features of long COVID identified through immune profiling. (Nature 2023)

- DOI: 10.1038/s41586-023-06651-y | PMCID: PMC10620090 | PMID: 37748514
- Evidence: Visualization of the bi-clustering was performed using the ComplexHeatmap package in R 79 .
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> visualisation [ComplexHeatmap] -> stage not stated [edgeR, vegan]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Version used: **2.2.0**
- Evidence: Heatmaps were created by using R Bioconductor package ComplexHeatmap v2.2.0 (ref.
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **2.6.2**
- Evidence: Heat maps were generated using ComplexHeatmap (version 2.6.2) to show the average expression of genes from biological replicates of the same genotype.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: Correlation between genome-wide CpG methylation levels were calculated using the R function ‘corr’ and visualized using the ComplexHeatmap package.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Maker heat maps were generated using the package ComplexHeatmap using results from the Seurat::AverageExpression() function as the input after scaling to relative expression per gene using the z- score.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Uridine-derived ribose fuels glucose-restricted pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06073-w | PMCID: PMC10232363 | PMID: 37198494
- Evidence: Heat map visualization of the data was plotted using heatmap2 and ComplexHeatmap packages in R.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5.2, limma] -> visualisation [ComplexHeatmap, ggplot2 v3.3.5, tidyverse v0.8.3] -> stage not stated [GSEA v4.0.3]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **2.11.1**
- Evidence: For generation of heatmaps the R package ComplexHeatmap(v2.11.1) 68 was used.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Evidence: Heat maps and Venn diagrams were generated using the R packages ComplexHeatmap and VennDiagram, respectively.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: Regulon activities were visualized as cluster averages using the R package ComplexHeatmap (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: Volcano plots were generated using the ggplot2 package in R and heat maps were generated using ComplexHeatmap package in R.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **2.12.0**
- Evidence: Methylation, accessibility, and expression values were averaged per cell state or bin and the Pearson correlation of all bins was visualized with ComplexHeatmap 2.12.0 85 .
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **2.14.0**
- Evidence: Count data were normalized using counts per million in the EdgeR package (v.3.40.2) 62 , dimension-reduced through PCA and subjected to heat-map analysis using ComplexHeatmap (v.2.14.0) 63 .
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Heat maps were created using the ComplexHeatmap and pheatmap packages.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: Heatmaps were generated by the ComplexHeatmap R package.
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: These correlation coefficients were calculated to identify similarity patterns in gene–phenotype pairs and visualized in a heat map generated by using the ComplexHeatmap package from R.
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Natural proteome diversity links aneuploidy tolerance to protein turnover. (Nature 2024)

- DOI: 10.1038/s41586-024-07442-9 | PMCID: PMC11153158 | PMID: 38778096
- Evidence: Heat maps were plotted using the ComplexHeatmap package 71 .
- Full pipeline: read trimming [edgeR] -> quantification [R, edgeR] -> normalisation [edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold, GSEA, STRING db, data.table]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Version used: **2.11.1**
- Evidence: Top differentially expressed genes were visualized by heat map via ComplexHeatmap (v2.11.1) package in R.
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **2.10.0**
- Evidence: R (v.4.1.3): cluster (v.2.1.2) 138 , ComplexHeatmap (v.2.10.0) 139 , 140 , data.table (v.1.14.8) 141 , DescTools (v.0.99.48) 142 , dplyr (v.1.1.2) 143 , gdata (v.2.19.0) 144 , ggforce (v.0.4.1) 145 , ggplot2 (v.3.4.2) 146 , ggpmisc (v.0.5.3) 147 , ggpointdensity (v.0.1.0) 148 , ggpubr (v.0.5.0) 149 , ggrastr (v.1.0.2) 150 , ggrepel (v.0.9.3) 151 , grid (v.4.1.3) 152 , gridExtra (v.2.3) 153 , gtabl...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Version used: **2.16.0**
- Evidence: A heatmap was generated with ComplexHeatmap (v2.16.0) and principal component analysis was performed using variance-stabilizing transformation values from DESeq2, stats (v3.6.0) and SummarisedExperiment (v1.16.1).
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Version used: **2.14.0**
- Evidence: The following packages were used: CellRanger v.6.0.1, singleCellTK v.2.8.0, Seurat v.4.3.0, scater v.1.24.0, harmony v.0.1.1, RColorBrewer v.1.1.3, ComplexHeatmap v.2.14.0, ArchR v.1.0.2, muscat v.1.12.1, readr v.2.1.4, ggplot2 v.3.4.2, ggsignif v.0.6.4, ggpubr v.0.6.0, magrittr v.2.0.3, scCoda v.0.1.9 Python package, celda v.1.19.1 and hdWGCNA v.0.4.5.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Additional R packages used include Presto, DESeq2, dplyr, ply, ape, cowplot, Matrix, variancePartition, MAST, HGNChelper, openxlsx, RColorBrewer, gridExtra, ggpubr, ComplexHeatmap, tidyverse, tibble, biomaRt, data.table, glmGamPoi, SeuratWrappers, patchwork, magrittr, s2, gplots, stringr, ggnewscale, ggbreak, coin and dunn.test.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: Heat maps was generated using the ComplexHeatmap package 82 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Finally, normalized enrichment scores of significant selected pathways were represented as a heat map using the ComplexHeatmap R package 74 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **2.11.1**
- Evidence: The R package ComplexHeatmap (v.2.11.1) was used to generate heat maps, and visualization was facilitated using ggplot2 (v.3.3.5), ggpubr (v.0.6.0), ggrepel (v.0.9.2), Statannot (v.0.6.0), Circlize (v.0.4.16), GseaVis (v.0.0.5), Enrichplot (v.1.22.0), GridExtra (v.2.3.0), Pheatmap(v.1.0.12) and DEGreport (v.1.38.5) R packages.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: Counts from all samples for the set of significantly differential peaks were plotted into a heatmap using ComplexHeatmap in R.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: Results were visualized using the ComplexHeatmap R package 67 .
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### Clonal tracing with somatic epimutations reveals dynamics of blood ageing. (Nature 2025)

- DOI: 10.1038/s41586-025-09041-8 | PMCID: PMC12240852 | PMID: 40399669
- Evidence: 70 ) and ComplexHeatmap 71 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, Seurat]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: The visualization of somatic mutation presence across subclones per sample was performed by means of the R package ComplexHeatmap.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: The modular expression trends of DEGs were visualized using the ComplexHeatmap package in R 47 .
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: Heat maps were drawn with the ComplexHeatmap package 41 . g:Profiler 42 or ClusterProfiler were used for Gene Ontology (GO) enrichment analysis.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: The −log 10 P values were visualized as a heat map created with the ComplexHeatmap Bioconductor package (v.2.16.0, using a custom colour palette shown in the scale) 61 , 62 .
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **2.6.2**
- Evidence: All of the plots were generated using R packages ggplot2 and ComplexHeatmap (v.2.6.2).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **2.16.0**
- Evidence: R libraries used: BiocManager v.1.30.22, circlize v.0.4.15, ComplexHeatmap v.2.16.0, drawProteins v.1.20.0, dplyr v.1.1.2, ggplot2 v.3.4.4, ggnewscale v.0.4.10, ggrepel v.0.9.4, PerformanceAnalytics v.2.0.4, RColorBrewer v.1.1-3, stringr v.1.5.1, tidyr v.1.3.0, tidyverse v.2.0.0, ggplot2 v.3.4.4.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Plots were generated using ComplexHeatmap (RRID:SCR_01727) and pheatmap (RRID:SCR_016418) R packages. devDEG analysis The devDEG analysis presented in Fig.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: We used the ComplexHeatmap library in R 63 to generate the heatmaps.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **2.4.3**
- Evidence: Visualization of data by a combination of the ComplexHeatmap (v.2.4.3 and v.2.14.0) 74 , ggplot2 (v.3.3.6 and v.3.5.1) 75 , cowplot (v.1.1.1; https://CRAN.R-project.org/package=cowplot ) and viridis 76 packages.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Genome-wide sweeps create ecological units in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-026-10476-w | PMCID: PMC13322978 | PMID: 42092154
- Version used: **2.12.1**
- Evidence: Statistical analysis Statistical analyses and graphical representations were performed in R (v.4.2.1) 80 using base R statistical functions and ggplot2 (v.3.5.1) 81 , ggpubr (v.0.6.0) 82 , ggtree (v.3.4.4) 83 , ggtreeExtra (v.1.6.1) 84 and ComplexHeatmap (v.2.12.1) 85 .
- Full pipeline: alignment/mapping [MetaPhlAn v4.0.6] -> differential/statistical testing [ComplexHeatmap v2.12.1, ggplot2 v3.5.1, ggpubr v0.6.0] -> stage not stated [Prokka v1.14.6, R, SciPy]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Evidence: Heat maps were plotted using ComplexHeatmap R package 73 (ComplexHeatmap (Bioconductor; http://bioconductor.org/packages/ComplexHeatmap/ ).
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **2.14.0**
- Evidence: UpSet plots were generated using the R packages UpSetR (v.1.4.0) 141 and ComplexUpset (v.1.3.3) 142 , 143 , boxplots and violin plots using ggplot2 (v.3.4.2) 144 , heatmaps using ComplexHeatmap (v.2.14.0) 145 and maps using leaflet (v.2.1.2) 146 .
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **2.16.0**
- Evidence: Postprocessing and data visualization were performed in R (v.4.4.1) using data.table (v.1.14.8), ggplot2 (v.3.4.2), pheatmap (v.1.0.12) and ComplexHeatmap (v.2.16.0).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Evidence: To generate cluster-level gene expression heatmaps, the ComplexHeatmap package 78 in R was used.
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Clustering stability The different conditions (ASD form/differentiation day) were clustered based on the Spearman correlation of log 2 FC of all expressed genes using the Ward.D2 clustering method on Euclidean distances as implemented in the ComplexHeatmap package (v.2.9.3) 135 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **2.18.0**
- Evidence: Heatmaps were created using ComplexHeatmap (v2.18.0 or v2.20.0) and circlize (v0.4.16).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Global monitoring of the impact of the COVID-19 pandemic through online surveys sampled from the Facebook user base. (PNAS 2021)

- DOI: 10.1073/pnas.2111455118 | PMCID: PMC8713788 | PMID: 34903657
- Version used: **2.3.4**
- Evidence: Benchmark data were used for clustering in the visualization (using row clustering method=”complete” in Heatmap from ComplexHeatmap 2.3.4, R 3.6.3, https://www.R-project.org/ ) within geographic regions of the world.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap v2.3.4, R v3.6] -> differential/statistical testing [LightGBM] -> visualisation [ComplexHeatmap v2.3.4, Python v3.8, R v3.6]

### Reprogrammed transsulfuration promotes basal-like breast tumor progression via realigning cellular cysteine persulfidation. (PNAS 2021)

- DOI: 10.1073/pnas.2100050118 | PMCID: PMC8609449 | PMID: 34737229
- Evidence: All analyses were performed in R using the following packages: ggpubr, ggExtra, ComplexHeatmap, circlize, corrr, hyper, DEqMS, and patchwork.
- Full pipeline: differential/statistical testing [R] -> stage not stated [ComplexHeatmap, ImageJ, ggpubr]

### Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself. (PNAS 2021)

- DOI: 10.1073/pnas.2100542118 | PMCID: PMC8449404 | PMID: 34507984
- Evidence: We used the ggplot2 ( 72 ), ggpubr, grid, gridExtra, ggsci, scales, png, ComplexHeatmap ( 73 ), and ggrepel R libraries for visualization.
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [R v3.6.3] -> visualisation [ComplexHeatmap, ggplot2, ggpubr] -> stage not stated [Clustal Omega v1.2]

### Investigating lymphangiogenesis in vitro and in vivo using engineered human lymphatic vessel networks. (PNAS 2021)

- DOI: 10.1073/pnas.2101931118 | PMCID: PMC8346860 | PMID: 34326257
- Evidence: S7 ), using ComplexHeatmap R package version 2.6.2 ( 37 ).
- Full pipeline: alignment/mapping [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, R]

### Transcriptome-based molecular subtypes and differentiation hierarchies improve the classification framework of acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2211429119 | PMCID: PMC9894241 | PMID: 36442087
- Evidence: Unsupervised clustering of top variance genes was conducted in R using the ComplexHeatmap ( 46 ) and a modified consensus clustering workflow.
- Full pipeline: alignment/mapping [kallisto v0.46.2] -> quantification [DESeq2 v1.28.0] -> normalisation [DESeq2 v1.28.0] -> dimensionality reduction/clustering [ComplexHeatmap] -> machine learning [Python]

### Dopamine and GPCR-mediated modulation of DN1 clock neurons gates the circadian timing of sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2206066119 | PMCID: PMC9407311 | PMID: 35969763
- Evidence: Their expression was plotted by the ComplexHeatmap package.
- Full pipeline: dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [Bioconductor, Seurat, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [Picard]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; induces a muted host response in human blood that blunts the recruitment of neutrophils. (PNAS 2022)

- DOI: 10.1073/pnas.2123017119 | PMCID: PMC9351360 | PMID: 35881802
- Evidence: Visualization was performed by using R packages ggplot2 ( 65 ), ComplexHeatmap ( 66 ), and ggVennDiagram ( 67 ).
- Full pipeline: alignment/mapping [Bowtie2 v3.1, HTSeq] -> differential/statistical testing [DESeq2, R v3.5.1] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [limma]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **2.6.2**
- Evidence: Gene expression heatmaps were generated using ComplexHeatmap (v2.6.2).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### Microbiome-associated human genetic variants impact phenome-wide disease risk. (PNAS 2022)

- DOI: 10.1073/pnas.2200551119 | PMCID: PMC9245617 | PMID: 35749358
- Version used: **2.12**
- Evidence: Data parsing and visualization were performed using Tidyverse version 4 ( 129 ) and ComplexHeatmap version 2.12 ( 130 ) packages.
- Full pipeline: variant calling [PLINK] -> visualisation [ComplexHeatmap v2.12] -> stage not stated [R, SAIGE, VEP]

### Caspase-4/11 exacerbates disease severity in SARS-CoV-2 infection by promoting inflammation and immunothrombosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202012119 | PMCID: PMC9173818 | PMID: 35588457
- Evidence: Volcano plots were generated with “EnhancedVolcano” and heatmaps were generated with ComplexHeatmap” using R.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [limma] -> visualisation [DESeq2] -> stage not stated [ComplexHeatmap]

### Parkinson's disease and multiple system atrophy patient iPSC-derived oligodendrocytes exhibit alpha-synuclein-induced changes in maturation and immune reactive properties. (PNAS 2022)

- DOI: 10.1073/pnas.2111405119 | PMCID: PMC8944747 | PMID: 35294277
- Version used: **2.4.3**
- Evidence: Heatmaps of gene expression and fold change between condition versus control were made with ComplexHeatmap version 2.4.3 ( 79 ).
- Full pipeline: differential/statistical testing [ggplot2 v3.3.0] -> stage not stated [ComplexHeatmap v2.4.3, Cytoscape, GSEA]

### Engineered nanoparticles enable deep proteomics studies at scale by leveraging tunable nano-bio interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2106053119 | PMCID: PMC8931255 | PMID: 35275789
- Evidence: The log 10 protein group intensities were plotted and clustered (hclust) using ComplexHeatmap ( Fig.
- Full pipeline: quantification [lme4] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [R, igraph, lme4] -> machine learning [lme4] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold]

### B cell-derived IL-27 promotes control of persistent LCMV infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116741119 | PMCID: PMC8784116 | PMID: 35022243
- Evidence: Packages ggplot2 and ComplexHeatmap were used for additional plotting.
- Full pipeline: read trimming [Seurat v4.0.3] -> dimensionality reduction/clustering [Seurat v4.0.3, UMAP] -> differential/statistical testing [Seurat v4.0.3] -> stage not stated [ComplexHeatmap, R v4.1.0, ggplot2]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: The heat map of these highly methylated regions was drawn by the ComplexHeatmap ( 46 ).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### Peripheral blood TCR clonotype diversity as an age-associated marker of breast cancer progression. (PNAS 2023)

- DOI: 10.1073/pnas.2316763120 | PMCID: PMC10710020 | PMID: 38011567
- Evidence: Hierarchical clustering in the heatmap of DEGs was performed by the Ward.D2 method in the ComplexHeatmap package (v2.14.0).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [survival (R)] -> stage not stated [DESeq2, GSEA, QuPath, R v4.3]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Evidence: The heatmaps showing the pathways analysis results were generated by the ComplexHeatmap R package ( 46 ) using the Corrected Accumulator values generated by MITHrIL ( 35 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Cereblon influences the timing of muscle differentiation in <i>Ciona</i> tadpoles. (PNAS 2023)

- DOI: 10.1073/pnas.2309989120 | PMCID: PMC10614628 | PMID: 37856545
- Version used: **2.10.0**
- Evidence: The heatmap was plotted with the R package ComplexHeatmap version 2.10.0 ( 69 ).
- Full pipeline: differential/statistical testing [R] -> visualisation [ComplexHeatmap v2.10.0] -> stage not stated [Fiji, ImageJ, Seurat v4.3.0]

### MicroRNA-335-5p suppresses voltage-gated sodium channel expression and may be a target for seizure control. (PNAS 2023)

- DOI: 10.1073/pnas.2216658120 | PMCID: PMC10372546 | PMID: 37463203
- Evidence: Heatmaps of mRNA expression were generated using the ComplexHeatmap package in R ( 68 ).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [ComplexHeatmap, DESeq2, R, tidyverse]

### Ancient vertebrate dermal armor evolved from trunk neural crest. (PNAS 2023)

- DOI: 10.1073/pnas.2221120120 | PMCID: PMC10372632 | PMID: 37459514
- Evidence: A subset of genes previously identified as being part of the neural crest gene regulatory network ( 34 ) was then isolated from the count matrix and plotted as a heatmap using ComplexHeatmap ( 60 ) package in Rstudio.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega v1.2.3] -> visualisation [ComplexHeatmap] -> stage not stated [DESeq2, featureCounts]

### Systemic deletion of <i>DMD</i> exon 51 rescues clinically severe Duchenne muscular dystrophy in a pig model lacking <i>DMD</i> exon 52. (PNAS 2023)

- DOI: 10.1073/pnas.2301250120 | PMCID: PMC10629550 | PMID: 37428903
- Evidence: For unsupervised clustering, principal component analysis and hierarchical clustering [ComplexHeatmap R package ( 58 )] were applied.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, R]

### Paf1 complex subunit Rtf1 stimulates H2B ubiquitylation by interacting with the highly conserved N-terminal helix of Rad6. (PNAS 2023)

- DOI: 10.1073/pnas.2220041120 | PMCID: PMC10235976 | PMID: 37216505
- Evidence: Tidyverse, Psych, ComplexHeatmap, and eulerr R packages were used to produce the correlation plots, heatmap, and Venn diagrams.
- Full pipeline: alignment/mapping [DESeq2, STAR v2.7.5a] -> quantification [DESeq2] -> stage not stated [AlphaFold, ComplexHeatmap, featureCounts]

### Species-specific CD4<sup>+</sup> T cells enable prediction of mucosal immune phenotypes from microbiota composition. (PNAS 2023)

- DOI: 10.1073/pnas.2215914120 | PMCID: PMC10041165 | PMID: 36917674
- Evidence: Heatmaps were constructed using either ComplexHeatmap ( 42 ) or ggplot2.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ComplexHeatmap, ggplot2]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: Figures were made using base R (R version 4.1.0) and the R packages ComplexHeatmap ( 130 ), igraph ( 131 ), eulerr ( 132 ), and ggplot2 ( 133 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### Modeling extrahepatic hepatitis E virus infection in induced human primary neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2411434121 | PMCID: PMC11588080 | PMID: 39546567
- Evidence: Data visualization was done in the statistical programming language R with in-house scripts using the libraries tidyverse, tidytSingleCellExperiment, Seurat ggplot2, GO-plot, ComplexHeatmap, and venn.
- Full pipeline: differential/statistical testing [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> visualisation [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> stage not stated [CellProfiler, ImageJ]

### Mitochondrial antioxidants abate SARS-COV-2 pathology in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2321972121 | PMCID: PMC11287122 | PMID: 39008677
- Evidence: Also in R, volcano plots were generated using the “EnhancedVolcano” (version 1.16.0) package, and Heatmaps were generated using the “ComplexHeatmap”( 29 ) (version 2.15.1), and “ggplot2” (version 3.4.1) packages.
- Full pipeline: quantification [DESeq2, R v4.2.2] -> normalisation [DESeq2, R v4.2.2] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ComplexHeatmap, GSEA v4.3.2, ggplot2]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: Visualization of the heatmap was by ComplexHeatmap and pheatmap packages, and bar graphs were created with ggplot2 ( 57 , 58 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### Single-tissue proteomics in <i>Caenorhabditis elegans</i> reveals proteins resident in intestinal lysosome-related organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2322588121 | PMCID: PMC11194598 | PMID: 38861598
- Evidence: The principal component analysis (PCA) was performed using the prcomp function from package stats 4.3.1 in R and the heatmap analysis with complete hierarchical clustering on Euclidean distances was performed using the ComplexHeatmap package v.2.16.0 ( 103 ).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, R, clusterProfiler] -> stage not stated [ggplot2]

### Real-time emulation of future global warming reveals realistic impacts on the phenological response and quality deterioration in rice. (PNAS 2024)

- DOI: 10.1073/pnas.2316497121 | PMCID: PMC11126993 | PMID: 38739807
- Evidence: Heatmaps were prepared based on the TPM data that z-transformed using the R package “ComplexHeatmap” (ver.
- Full pipeline: quantification [ComplexHeatmap] -> visualisation [R, ggplot2] -> stage not stated [DESeq2]

### Isotype switching in human memory B cells sets intrinsic antigen-affinity thresholds that dictate antigen-driven fates. (PNAS 2024)

- DOI: 10.1073/pnas.2313672121 | PMCID: PMC10990115 | PMID: 38502693
- Evidence: Heatmaps of gene expression were generated using the ComplexHeatmap package ( 65 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, GSEA, R, fgsea]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: To create heatmaps, we utilized the Heatmap() function from the R package “ComplexHeatmap”.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: The resulting regulon activity matrix was imported into R for visualization, where the reshape2 package ( 61 ) was used to transform data into a suitable format, ComplexHeatmap ( 62 ) was used to generate clustered heatmaps, and ggplot2 facilitated violin plots, boxplots, and correlation analyses.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Version used: **2.6.2**
- Evidence: Data visualization included volcano plots generated with EnhancedVolcano and heatmaps created using ComplexHeatmap (v2.6.2) in R.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: Visualization was generated with ggplot2 package, heatmaps were created with ComplexHeatmap package ( 63 ), volcano plots with the EnhancedVolcano Package ( 64 ) and GSEA with decoupleR ( 27 ).
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### Metabolic adaptation of glucose-deprived macrophages involves partial gluconeogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2419568122 | PMCID: PMC12595420 | PMID: 41160607
- Evidence: The expression values were plotted using the ComplexHeatmap R package v2.18.0 ( 55 ).
- Full pipeline: normalisation [ggplot2] -> dimensionality reduction/clustering [ggplot2] -> visualisation [ComplexHeatmap, R] -> stage not stated [Seurat v5.1.0]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Voom-normalized expression values were scaled from –2 to 2 prior to generating the heatmap using the ComplexHeatmap package.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Evidence: Hierarchical clustering with the ward D2 method linkage was performed using Euclidean distance and displayed using the ComplexHeatmap R package.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### Coordinated actions of NLR-assembled and glutamate receptor-like calcium channels in plant effector-triggered immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2508018122 | PMCID: PMC12415192 | PMID: 40844808
- Evidence: Heatmaps were generated with the ComplexHeatmap package.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT v7.505] -> stage not stated [ComplexHeatmap, DESeq2 v1.38.0, R, ggplot2 v3.4.2]

### Macroevolutionary changes in natural selection on codon usage reflect evolution of the tRNA pool across a budding yeast subphylum. (PNAS 2025)

- DOI: 10.1073/pnas.2419889122 | PMCID: PMC12260425 | PMID: 40591602
- Evidence: Results were visualized using heatmaps as implemented in the R package ComplexHeatmap.
- Full pipeline: read trimming [fastp, kallisto] -> quantification [fastp, kallisto] -> visualisation [ComplexHeatmap] -> stage not stated [R]

### Metabolic control of glycosylation forms for establishing glycan-dependent protein interaction networks. (PNAS 2025)

- DOI: 10.1073/pnas.2422936122 | PMCID: PMC12207472 | PMID: 40531880
- Evidence: UpSet plots were generated in R using the ComplexHeatmap package in intersect mode.
- Full pipeline: dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.9.1] -> stage not stated [AlphaFold, ComplexHeatmap, STRING db]

### Mycoviruses confer hypovirulence but enhance antifungal volatile organic compound production in a phytopathogenic fungus. (PNAS 2026)

- DOI: 10.1073/pnas.2526822123 | PMCID: PMC13080020 | PMID: 41941638
- Evidence: Hierarchical clustering analysis (HCA) was conducted on unit variance-scaled data and visualized using the ComplexHeatmap package.
- Full pipeline: alignment/mapping [ChimeraX, MAFFT v7.0] -> normalisation [ComplexHeatmap] -> dimensionality reduction/clustering [ComplexHeatmap, HMMER v3.3.2] -> visualisation [ChimeraX, ComplexHeatmap, ImageJ] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.2.6]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: The ComplexHeatmap package was then used to visualize the spline smooth expression pattern of aging-dependent DEGs and the genes were divided into different clusters based on their expression pattern ( 46 ).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Mapping of the viral shunt across widespread coccolithophore blooms using metabolic biomarkers. (PNAS 2026)

- DOI: 10.1073/pnas.2424035123 | PMCID: PMC12891027 | PMID: 41637455
- Evidence: Heatmaps were generated using the R package “ComplexHeatmap” by scaling mesocosm bag 4 and each cruise between 0 and 1.
- Full pipeline: normalisation [ComplexHeatmap, R]

### Plant diversity influences plant volatile emission with varying effects at the species and community levels. (PNAS 2026)

- DOI: 10.1073/pnas.2518326123 | PMCID: PMC12818445 | PMID: 41538247
- Evidence: For data visualization, we used ggplot2 , ggeffects , ComplexHeatmap , and pheatmap ( 96 – 99 ).
- Full pipeline: differential/statistical testing [R v4.5.1, lme4, tidyverse] -> visualisation [ComplexHeatmap, R v4.5.1, ggplot2, pheatmap, tidyverse] -> stage not stated [mothur, phyloseq]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: Differential gene expression was plotted as a heatmap with ComplexHeatmap, and genes and samples were clustered according to complete linkage and the Euclidean distances of gene expression values.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: GSEA analysis and corresponding heatmaps and figures were created using R package fgsea (vfgsea_1.24.0), ComplexHeatmap, and ggplot2 for signatures from MSigDB’s hallmark MTORC1 and custom AR signatures based on our data ( 53 – 55 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: Heatmap was created using the ComplexHeatmap package in R, using Z-transformed VST-normalized read counts for each gene.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

