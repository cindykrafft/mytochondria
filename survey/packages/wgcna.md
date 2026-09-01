# WGCNA

- **Category:** genomics
- **Papers in survey:** 81
- **Journals:** PNAS (49), Nature (23), Cell (9)
- **Years:** 2021 (12), 2022 (17), 2023 (14), 2024 (16), 2025 (12), 2026 (10)
- **Versions named:** 1.71 (2), 1.7.0 (1), 1.73 (1), 1.69 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (16), differential/statistical testing (4), quantification (4), normalisation (3), simulation/modelling (2), structure determination (2), visualisation (1), variant calling (1)

## Papers

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **1.69**
- Evidence: ...nalR version 1.0 R Bioconductor; Cabello-Aguilar et al., 2020 http://www.bioconductor.org/packages/release/bioc/html/SingleCellSignalR.html R package WGCNA version 1.69 R CRAN; Langfelder and Horvath, 2008 https://cran.r-project.org/web/packages/WGCNA/index.html STRING Database version 11.0 Szklarczyk et al., 2019 ; STRING Database https://string-db.org/ R package clusterProfiler version 3.16.1 R ...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: This paper Zenodo: https://doi.org/10.5281/zenodo.6120249 CBD-KEY-CITESEQ-GEX-WGCNA : WGCNA analysis of selected cell subpopulations.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: 59 https://msstats.org/ WGCNA Langfelder and Horvath 33 https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/ Cytoscape Shannon et al.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **1.71**
- Evidence: 104 https://github.com/atarashansky/SAMap Iterative comparison of co-expression algorithm (ICC) Tirosh and Barkai 31 https://doi.org/10.1186/gb-2007-8-4-r50 WGCNA 1.71 Langfelder and Horvath 105 https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/ Broccoli 1.2 Derelle et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: 116 Weighted correlation network analysis (WGCNA) To identify the different modules of correlated genes in our datasets, WGCNA were used [python version: PyWGCNA 117 ].
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: 98 https://bioconductor.org/packages/impute/ randomForest R package Liaw and Wiener 99 https://CRAN.R-project.org/package=randomForest WGCNA R package Zhang and Horvath 100 ; Langfelder and Horvath 101 https://CRAN.R-project.org/package=WGCNA PRROC R package Grau et al.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### CSF proteomics identifies early changes in autosomal dominant Alzheimer's disease. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.049 | PMCID: PMC11531390 | PMID: 39332414
- Evidence: To determine if specific pathways are dysregulated at different disease stages, we performed weighted gene co-expression network analyses (WGCNA) and then pathway analyses in each module.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.0] -> simulation/modelling [GSVA] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, WGCNA]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: 88 , 111 MEGENA module preservation analysis Module preservation analysis was essentially the same approach as in weighted gene correlation network analysis (WGCNA).
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: Weighted gene co-expression network analysis (WGCNA) of the intestinal tissue transcriptome revealed that the Δ cydAB mutant exhibited reduced infection-associated changes in host processes such as epithelial-mesenchymal transition, reinforcing the notion that ETBF alters host processes to reshape the gut nutritional environment ( Figures S4B and S4C ).
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: In brief, area gene modules defined on the basis of area-associated gene expression patterns 2 , 42 were generated and module eigengene values were determined for each organoid excitatory neuron using the ‘moduleEigengenes’ function from the WGCNA R package 74 .
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: Weighted gene coexpression clustering of AP13 gene annotation RNA-seq libraries was conducted with WGCNA 87 with a power of 6.
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Evidence: Weighted gene coexpression network analysis (WGCNA).
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Medin co-aggregates with vascular amyloid-β in Alzheimer's disease. (Nature 2022)

- DOI: 10.1038/s41586-022-05440-3 | PMCID: PMC9712113 | PMID: 36385530
- Evidence: The heat map shows WGCNA module 3 of the RNA-seq data set, which contains the MFGE8 gene (green) and is associated with Alzheimer’s disease.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Fiji v2.3, ImageJ v2.3, SCENIC, WGCNA]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: Sample connectivity was calculated using the fundamentalNetworkConcepts function in the WGCNA 17 R package, with the signed adjacency matrix (soft power of 2) of the sample biweight midcorrelation as input.
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Evidence: DOCK2 co-expression analysis and GO enrichment analysis We applied the weighted gene co-expression network analysis (WGCNA) algorithm 28 to evaluate co-expressed genes with DOCK2 in COVID-19.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Evidence: Co-expression network WGCNA 46 was applied to the prefiltered expression data from 332 accessions to reconstruct gene modules exhibiting different expression patterns.
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### The mosaic oat genome gives insights into a uniquely healthy cereal crop. (Nature 2022)

- DOI: 10.1038/s41586-022-04732-y | PMCID: PMC9159951 | PMID: 35585233
- Evidence: ...further than 1.5 × the inter-quartile range, the data beyond the end of the whiskers are outliers plotted individually. b , Heatmap representation of WGCNA modules showing the relation between the expected representation of each subgenome in the module based on the overall number of genes per subgenome and the observed one. > 1: higher than expected, < 1 lower than expected.
- Full pipeline: visualisation [WGCNA] -> stage not stated [BUSCO v5.1.2]

### A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06812-z | PMCID: PMC10719114 | PMID: 38092916
- Evidence: 5d , Supplementary Table 8 ), we performed WGCNA analysis 139 on 534 transcription factor marker genes based on their average expression at the subclass level with power = 6 and TOMType = “signed”, and detectCutHeight = 0.998.
- Full pipeline: quantification [UMAP] -> normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [Cellpose, Jupyter, WGCNA, limma, scDblFinder]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Evidence: These metabolites were clustered based on their co-abundance using the R package WGCNA 49 (v.1.72-1).
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Gene module detection and cell assignment To identify expression modules for significant gene sets along the estimated trajectories, we applied the module detection algorithm implemented in the WGCNA package 95 (v.1.70-3) based on the smoothed gene expression matrix with parameters softPower = 10 and minModuleSize = 20.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: Validation and benchmarking of CellOracle GRN inference To test whether CellOracle can correctly identify cell-type- or cell-state-specific GRN configurations, we benchmarked our new method against diverse GRN inference algorithms: WGCNA, DCOL, GENIE3 and SCENIC.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Evidence: For construction of the gene co-expression networks for O. fusiformis and C. teleta , we used the WGCNA package (v.1.70-3) 102 .
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: WGCNA analysis For the WGCNA 24 analysis, the dataset was downsampled to a maximum of 500 cells per perturbation using the subset function with downsample = 500 option in Seurat.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: Gene sets for each of the 62 colour module eigengenes identified by WGCNA in ref.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Weighted gene co-expression network analysis (WGCNA) was performed using an R package.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **1.7.0**
- Evidence: Counts were converted to FPKM in the R package for subsequent analyses: WGCNA (v.1.7.0) was used to cluster gene expression in the full organ set and, after filtering out genes with limited variance and coverage, the ‘softpower’ parameter was estimated to be 20, and clustering was run with a ‘signed’ network type 105 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Initial attempts to perform hit selection in CROP-seq involved using edgeR, WGCNA and traditional differential expression tests in Seurat (Wilcoxon rank-sum test) 59 – 61 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Version used: **1.71**
- Evidence: WGCNA WGCNA (v1.71) in mouse tumour tissues was restricted to genes with greater than or equal to 15 counts in 75% of samples.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### A crucial role for the cortical amygdala in shaping social encounters. (Nature 2025)

- DOI: 10.1038/s41586-024-08540-4 | PMCID: PMC11946885 | PMID: 39939764
- Evidence: All of the above steps were performed using the WGCNA package in R.
- Full pipeline: stage not stated [WGCNA]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Identification of co-regulated transcriptomic modules of ageing and longevity To identify clusters of genes that are co-regulated during ageing and in response to lifespan-modulating interventions, WGCNA 243 was applied to the relative scaled rodent and multi-species meta-datasets, centred within dataset, tissue and sex as described above.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Evidence: WGCNA To identify brain-wide gene co-expression networks, normalized count data for all brain regions were compiled and analysed using the WGCNA package (v1.73) 74 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Network analysis supports convergence over time As transcripts do not act independently, but as part of highly regulated transcriptional networks 78 , we constructed co-expression networks using weighted gene co-expression network analysis (WGCNA) 78 – 80 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Constructing local cell-specific networks from single-cell data. (PNAS 2021)

- DOI: 10.1073/pnas.2113178118 | PMCID: PMC8713783 | PMID: 34903665
- Evidence: It is worth noting that none of these communities are identified by WGCNA ( 24 ) ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot, UMAP] -> stage not stated [Python v3.7.6, WGCNA]

### Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. (PNAS 2021)

- DOI: 10.1073/pnas.2106844118 | PMCID: PMC8713748 | PMID: 34916285
- Evidence: ( A ) The genes with high discriminatory potential to distinguish SB cases and controls significantly enrich an early progenitor class, gene coexpression module identified in a transcriptome WGCNA study of midgestation human cortex ( 35 ).
- Full pipeline: stage not stated [ADMIXTURE, BEDTools, GATK, R, VEP, WGCNA, scikit-learn]

### Sleep loss drives acetylcholine- and somatostatin interneuron-mediated gating of hippocampal activity to inhibit memory consolidation. (PNAS 2021)

- DOI: 10.1073/pnas.2019318118 | PMCID: PMC8364159 | PMID: 34344824
- Evidence: To identify clusters of coregulated transcripts in our RNA-seq data (such as might be expected for genetically defined cell types), we used weighted gene correlation network analysis (WGCNA) ( 20 ) on transcripts with a variance greater than 0.03 ( n = 1662 transcripts; Materials and Methods ).
- Full pipeline: dimensionality reduction/clustering [WGCNA]

### Interpreting machine learning models to investigate circadian regulation and facilitate exploration of clock function. (PNAS 2021)

- DOI: 10.1073/pnas.2103070118 | PMCID: PMC8364196 | PMID: 34353905
- Evidence: As such, we bioinformatically identified coexpression modules ( SI Appendix , Glossary ) from the transcriptomic profiles of the circadian transcripts that were used to train our ML models using weighted gene coexpression network analysis (WGCNA) ( 63 ).
- Full pipeline: differential/statistical testing [LightGBM, XGBoost] -> machine learning [LightGBM, TensorFlow v2.0.0, XGBoost] -> stage not stated [Jupyter, WGCNA]

### Polyploidy underlies co-option and diversification of biosynthetic triterpene pathways in the apple tribe. (PNAS 2021)

- DOI: 10.1073/pnas.2101767118 | PMCID: PMC8157987 | PMID: 33986115
- Evidence: WGCNA was used to identify associated gene groups.
- Full pipeline: alignment/mapping [MUSCLE, RSEM] -> machine learning [AUGUSTUS] -> stage not stated [BUSCO v3.0.2, Canu, HMMER, InterProScan v5.16, Pilon, RepeatMasker, WGCNA]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: Weighted gene coexpression analysis was conducted using the WGCNA package in R ( 23 ).
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### Microbial dynamics of elevated carbon flux in the open ocean's abyss. (PNAS 2021)

- DOI: 10.1073/pnas.2018269118 | PMCID: PMC7848738 | PMID: 33479184
- Evidence: WGCNA.
- Full pipeline: read trimming [SPAdes] -> alignment/mapping [SPAdes] -> structure determination [SPAdes, ggplot2, pheatmap] -> visualisation [Cytoscape, ggplot2, pheatmap] -> stage not stated [BWA v0.7.15, R, WGCNA]

### OCT4 induces embryonic pluripotency via STAT3 signaling and metabolic mechanisms. (PNAS 2021)

- DOI: 10.1073/pnas.2008890118 | PMCID: PMC7826362 | PMID: 33452132
- Evidence: To assess the accuracy of the identified lineages, we used the WGCNA unsupervised clustering method ( 91 ) to identify specific modules of coexpressed genes in each developmental lineage/genotype.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> variant calling [WGCNA] -> quantification [Bioconductor, HTSeq] -> dimensionality reduction/clustering [Bioconductor, WGCNA] -> differential/statistical testing [GSEA, R]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Evidence: Same settings were used when comparing the CGM calling method in this paper with the WGCNA method.
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### Tissue-specific regulation of lipid polyester synthesis genes controlling oxygen permeation into <i>Lotus japonicus</i> nodules. (PNAS 2022)

- DOI: 10.1073/pnas.2206291119 | PMCID: PMC9704718 | PMID: 36375074
- Evidence: Gene clusters that coexpressed together were identified by a weighted correlation network analysis (WGCNA) ( 60 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [ImageJ] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, R] -> stage not stated [RAxML, ggpubr v0.4.0.999, pheatmap]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: The WGCNA package ( 29 ) was used to identify coexpressed genes that were strongly related to specific temporal groups (with options “unsigned correlation” and “minimum cluster size = 30”).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Socioeconomic inequalities in molecular risk for chronic diseases observed in young adulthood. (PNAS 2022)

- DOI: 10.1073/pnas.2103088119 | PMCID: PMC9621370 | PMID: 36252037
- Evidence: The entire genome was clustered using WGCNA to identify clusters of coexpressed networks of genes (25 in total) ( 48 ).
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R, limma] -> stage not stated [Bioconductor]

### Monosomy X in isogenic human iPSC-derived trophoblast model impacts expression modules preserved in human placenta. (PNAS 2022)

- DOI: 10.1073/pnas.2211073119 | PMCID: PMC9546589 | PMID: 36161909
- Evidence: Weighted gene coexpression network analysis (WGCNA) was performed on vst counts, using the WGCNA package ( 85 ), as a signed hybrid network using the biweight midcorrelation raised to a soft thresholding power of 17 (scale-free topology fit ≥0.85).
- Full pipeline: normalisation [GSEA, clusterProfiler] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler] -> stage not stated [WGCNA]

### Winter warming post floral initiation delays flowering via bud dormancy activation and affects yield in a winter annual crop. (PNAS 2022)

- DOI: 10.1073/pnas.2204355119 | PMCID: PMC9522361 | PMID: 36122201
- Evidence: Gene expression modules were measured by the WGCNA (weighted gene coexpression network analysis) package in R ( 37 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HISAT2 v2.2.1] -> normalisation [deepTools v2.3] -> visualisation [deepTools v2.3] -> stage not stated [HOMER, Picard, R, WGCNA]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Evidence: The gene coexpression network analyses were carried out using WGCNA in the R package ( 19 , 20 ).
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### DNA methylation signatures in airway cells from adult children of asthmatic mothers reflect subtypes of severe asthma. (PNAS 2022)

- DOI: 10.1073/pnas.2116467119 | PMCID: PMC9214527 | PMID: 35666868
- Evidence: The CpGs that were differentially methylated only between controls and cases without MA (NMA) or only between controls and cases with MA (FDR < 0.10) were referred to as NMA-DMCs and MA-DMCs, respectively, and were separately clustered into comethylation modules using WGCNA ( 19 ).
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [WGCNA, limma] -> visualisation [pheatmap] -> stage not stated [R]

### DNA methylation clocks for dogs and humans. (PNAS 2022)

- DOI: 10.1073/pnas.2120887119 | PMCID: PMC9173771 | PMID: 35580182
- Evidence: EWAS was performed in each tissue separately using the function standardScreeningNumericTrait from the WGCNA R package ( 59 ).
- Full pipeline: stage not stated [R, WGCNA]

### Pathogen-induced biosynthetic pathways encode defense-related molecules in bread wheat. (PNAS 2022)

- DOI: 10.1073/pnas.2123299119 | PMCID: PMC9169793 | PMID: 35412884
- Evidence: Weighted gene coexpression network analysis (WGCNA) was carried out based on gene expression patterns in the compiled datasets, and an additional set of networks was built for six separate subsample sets: grain, leaf, spike, root, abiotic, and disease ( 12 ).
- Full pipeline: stage not stated [WGCNA]

### Metabolomic selection for enhanced fruit flavor. (PNAS 2022)

- DOI: 10.1073/pnas.2115865119 | PMCID: PMC8860002 | PMID: 35131943
- Evidence: Network analysis was performed using the R package WGCNA ( 51 ).
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [XGBoost] -> visualisation [Cytoscape v3.7.1] -> stage not stated [R, WGCNA]

### Noncanonical HPV carcinogenesis drives radiosensitization of head and neck tumors. (PNAS 2023)

- DOI: 10.1073/pnas.2216532120 | PMCID: PMC10410762 | PMID: 37523561
- Evidence: ( H ) Barplot displaying GSEA-based adjusted P value representing the enrichment of each WGCNA module for probe–gene correlation.
- Full pipeline: variant calling [VarScan] -> differential/statistical testing [GSEA, WGCNA] -> stage not stated [CNVkit, R]

### Adaptive structural and functional evolution of the placenta protects fetal growth in high-elevation deer mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218049120 | PMCID: PMC10288601 | PMID: 37307471
- Evidence: To resolve potential regulatory networks and the sets of coexpressed genes involved, we next applied an unsupervised network-based approach [WGCNA ( 58 )] to our transcriptomic data.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [ImageJ v2.0.0, featureCounts] -> stage not stated [R v4.0, WGCNA, emmeans, lme4]

### A spatiotemporal barrier formed by Follistatin is required for left-right patterning. (PNAS 2023)

- DOI: 10.1073/pnas.2219649120 | PMCID: PMC10268237 | PMID: 37276408
- Evidence: The WGCNA (Weighted correlation network analysis) package ( https://CRAN.R-project.org/package=WGCNA ) was used to analyze the correlation between module eigengenes (genes function as a robust unit) and sample traits (Nodal concentration and Nodal response time).
- Full pipeline: stage not stated [AlphaFold, WGCNA]

### Fear circuit-based neurobehavioral signatures mirror resilience to chronic social stress in mouse. (PNAS 2023)

- DOI: 10.1073/pnas.2205576120 | PMCID: PMC10151471 | PMID: 37068238
- Evidence: We employed weighted gene coexpression network analysis (WGCNA) to identify specific modules of genes that correlate across brain regions and could be critical in determining the subgroups ( Fig.
- Full pipeline: stage not stated [WGCNA]

### Neuron-specific transcriptomic signatures indicate neuroinflammation and altered neuronal activity in ASD temporal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2206758120 | PMCID: PMC10013873 | PMID: 36862688
- Evidence: Weighted gene co-expression network analysis (WGCNA) ( 27 ) was performed to define modules of co-expressed genes from RNA-seq data.
- Full pipeline: quantification [featureCounts v1.6.4] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [DESeq2 v1.22.2, GSEA, WGCNA]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Gene coexpression networks were constructed using “WGCNA” ( 70 ).
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Local adaptation, plasticity, and evolved resistance to hypoxic cold stress in high-altitude deer mice. (PNAS 2024)

- DOI: 10.1073/pnas.2412526121 | PMCID: PMC11474095 | PMID: 39352929
- Evidence: We used WGCNA ( 77 ) to identify modules (sets of genes) that are coexpressed across each tissue type, thereby providing insights into how regulatory mechanisms are affected by treatments.
- Full pipeline: alignment/mapping [featureCounts v2.0.3] -> normalisation [edgeR] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [R, lme4] -> stage not stated [WGCNA]

### Molecular forecasting of domoic acid during a pervasive toxic diatom bloom. (PNAS 2024)

- DOI: 10.1073/pnas.2319177121 | PMCID: PMC11459128 | PMID: 39298472
- Evidence: Weighted gene correlation network analysis (WGCNA) on a highly expressed subset of the de novo assembled P. australis HAB metatranscriptome from the bloom period (April 15th to September 30th) identified seven modules of transcripts with similar expression profiles ( Fig.
- Full pipeline: stage not stated [WGCNA]

### Dual role of neuroplastin in pancreatic β cells: Regulating insulin secretion and promoting islet inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2411234121 | PMCID: PMC11331099 | PMID: 39666939
- Evidence: In addition, weighted gene correlation network analysis (WGCNA) ( 27 ) showed higher expression of gene set related to citrate cycle (TCA cycle) in Nptn f/f ; Ins1 Cre islets ( SI Appendix , Fig.
- Full pipeline: stage not stated [ImageJ, WGCNA]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Evidence: For each species, pairwise biweight midcorrelations (bicor) for all protein-coding genes were calculated using the bicor function from the WGCNA package ( 50 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Evidence: Weighted Gene Coexpression Network Analysis (WGCNA).
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### ZmPILS6 is an auxin efflux carrier required for maize root morphogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2313216121 | PMCID: PMC11145266 | PMID: 38781209
- Evidence: WGCNA.
- Full pipeline: variant calling [R] -> dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.9.1, R] -> stage not stated [ImageJ, WGCNA]

### Species-wide quantitative transcriptomes and proteomes reveal distinct genetic control of gene expression variation in yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2319211121 | PMCID: PMC11087752 | PMID: 38696467
- Evidence: We then computed a WGCNA using the WGCNA R package ( 81 ) to detect coexpression module in both mRNA and peptide normalized abundance.
- Full pipeline: quantification [R, WGCNA] -> normalisation [WGCNA] -> stage not stated [GSEA, fgsea]

### Endogenous retrovirus HERVH-derived lncRNA <i>UCA1</i> controls human trophoblast development. (PNAS 2024)

- DOI: 10.1073/pnas.2318176121 | PMCID: PMC10962953 | PMID: 38483994
- Evidence: To test this hypothesis, we first performed the weighted gene co-expression network analysis (WGCNA) and identified one gene cluster showing a positive relationship to the EO-PE placental transcriptome ( Fig.
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [WGCNA] -> stage not stated [GSEA]

### Cortical &lt;i&gt;miR-709&lt;/i&gt; links glutamatergic signaling to NREM sleep EEG slow waves in an activity-dependent manner. (PNAS 2024)

- DOI: 10.1073/pnas.2220532121 | PMCID: PMC10801902 | PMID: 38207077
- Evidence: Weighted Gene Co-Expression Network Analysis (WGCNA).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [Bioconductor, R, limma] -> stage not stated [WGCNA]

### A predisposed motor bias shapes individuality in vocal learning. (PNAS 2024)

- DOI: 10.1073/pnas.2308837121 | PMCID: PMC10801888 | PMID: 38198530
- Evidence: WGCNA identifies modules of densely interconnected genes by hierarchical clustering based on the topological overlap, a biologically meaningful measure of similarity of expression patterns among all pairs of genes across all individuals, and by assigning each gene to a “Module” based on shared expression patterns.
- Full pipeline: dimensionality reduction/clustering [UMAP, WGCNA] -> visualisation [UMAP] -> stage not stated [Metascape, R, Seurat]

### Engineering chronological lifespan toward a robust yeast cell factory. (PNAS 2025)

- DOI: 10.1073/pnas.2515324122 | PMCID: PMC12646210 | PMID: 41213019
- Evidence: ( D ) Weighted Gene Co-Expression Network Analysis (WGCNA) using proteomic data.
- Full pipeline: stage not stated [WGCNA]

### Factors underlying a latitudinal gradient in the S/G lignin monomer ratio in natural poplar variants. (PNAS 2025)

- DOI: 10.1073/pnas.2503491122 | PMCID: PMC12403099 | PMID: 40833412
- Evidence: The methods used for hierarchical clustering, WGCNA, and GO enrichment analysis are available in SI Appendix .
- Full pipeline: dimensionality reduction/clustering [R, WGCNA] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BCFtools, SAMtools, SnpEff]

### Mobile gene clusters and coexpressed plant-rhizobium pathways drive partner quality variation in symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2411831122 | PMCID: PMC12337268 | PMID: 40729388
- Evidence: WGCNA.
- Full pipeline: differential/statistical testing [R] -> stage not stated [WGCNA, edgeR, eggNOG]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Analysis of Bulk RNA-seq and WGCNA.
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Elevated brain manganese induces motor disease by upregulating the kynurenine pathway of tryptophan metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2423628122 | PMCID: PMC12036984 | PMID: 40244671
- Evidence: Weighted Gene Coexpression Network Analysis (WGCNA) Identifies Coordinated Changes in Metabolic Networks in the Brain of Mn-Exposed Mice.
- Full pipeline: stage not stated [WGCNA]

### pTDP-43 levels correlate with cell type-specific molecular alterations in the prefrontal cortex of &lt;i&gt;C9orf72&lt;/i&gt; ALS/FTD patients. (PNAS 2025)

- DOI: 10.1073/pnas.2419818122 | PMCID: PMC11892677 | PMID: 39999167
- Evidence: ( K ) Significance of WGCNA modules with different levels of pTDP-43.
- Full pipeline: quality control [ArchR, Seurat, SoupX] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [WGCNA]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Evidence: Weighted Gene Coexpression Network Analysis (WGCNA).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Dissecting the cellular architecture and genetic circuitry of the soybean seed. (PNAS 2025)

- DOI: 10.1073/pnas.2416987121 | PMCID: PMC11725896 | PMID: 39793081
- Evidence: We used the R package WGCNA ( 34 , 53 ) to identify modules of coexpressed genes in the LCM dataset.
- Full pipeline: quality control [SoupX v1.6.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v4.1.1, WGCNA]

### Impact of sex chromosomes and gonad type in stress susceptibility in corticostriatal brain regions. (PNAS 2026)

- DOI: 10.1073/pnas.2531920123 | PMCID: PMC13229181 | PMID: 42189975
- Evidence: To identify coexpression modules within the two corticolimbic regions, we applied WGCNA on the variance-stabilized gene expression data ( 78 ).
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.10.3, Metascape] -> stage not stated [Bioconductor, WGCNA]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: Therefore, to identify large patterns of gene expression and regulation present in our dataset, we performed a weighted gene coexpression network analysis (WGCNA) to identify clusters of genes/regulatory elements with similar expression/accessibility patterns (separately for each data type) ( 68 ).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### FABP7 controls radial glial scaffold stability during human cortical development. (PNAS 2026)

- DOI: 10.1073/pnas.2523130123 | PMCID: PMC13099611 | PMID: 41984827
- Evidence: Furthermore, HMGCS1 was identified as a central hub gene in a radial glia-enriched weighted gene coexpression network analysis (WGCNA) module (Cortical-M6), which also included FABP7 itself as a key regulatory node, reinforcing the relevance of MVA pathway suppression within the FABP7 -dependent gene regulatory network ( Fig.
- Full pipeline: normalisation [Seurat v4.4.0, edgeR v3.40.2] -> dimensionality reduction/clustering [Seurat v4.4.0, UMAP, edgeR v3.40.2] -> differential/statistical testing [Seurat v4.4.0, edgeR v3.40.2] -> visualisation [UMAP] -> stage not stated [GSEA, WGCNA]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **1.73**
- Evidence: To investigate patterns of coexpression within and between the oyster host and its microbiome, we conducted independent weighted gene coexpression network analysis (WGCNA) using the WGCNA v.1.73 R package ( 77 ).
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### Pareto optimality reveals an atlas of cellular archetypes. (PNAS 2026)

- DOI: 10.1073/pnas.2530194123 | PMCID: PMC12993957 | PMID: 41802062
- Evidence: PCA, ICA, NMF, WGCNA, and topic modeling reveal coexpression modules ( 78 ), and trajectory inference methods, including Diffusion Pseudotime, reconstruct lineage trajectories, thus inferring dynamics ( 79 , 80 ).
- Full pipeline: alignment/mapping [igraph v1.5.1] -> dimensionality reduction/clustering [WGCNA, igraph v1.5.1] -> simulation/modelling [WGCNA] -> structure determination [WGCNA] -> stage not stated [R v0.0.0.9000, Scanpy v1.10.3]

### Foliar dewdroplet-induced redox cascades promote early flowering in &lt;i&gt;Brassicaceae&lt;/i&gt; plants. (PNAS 2026)

- DOI: 10.1073/pnas.2527021123 | PMCID: PMC12933091 | PMID: 41701847
- Evidence: WGCNA identified coexpression modules (β = 25, R 2 > 0.85).
- Full pipeline: quality control [Bowtie2, DESeq2, FastQC, MACS2] -> stage not stated [WGCNA]

