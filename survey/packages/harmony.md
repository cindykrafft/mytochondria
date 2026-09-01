# Harmony

- **Category:** single-cell
- **Papers in survey:** 32
- **Journals:** Nature (23), PNAS (5), Cell (3), Science (1)
- **Years:** 2021 (1), 2022 (2), 2023 (3), 2024 (8), 2025 (8), 2026 (10)
- **Versions named:** 0.1.1 (5), 1.2.3 (2), 1.2.0 (2), 1.2.1 (2), 1.0 (2), 0.1.0 (2), 0.0.5 (1), 3.8 (1), 4.9 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (13), normalisation (10), visualisation (3), quality control (3), quantification (2)

## Papers

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **1.0**
- Evidence: ...utler et al., 2018 https://github.com/satijalab/seurat R package Harmony version 1.0 Github; Korsunsky et al., 2019 https://github.com/immunogenomics/harmony R package MAST version 1.14.0 R Bioconductor; Finak et al., 2015 https://www.bioconductor.org/packages/release/bioc/html/MAST.html R package zinbwave version 1.10.1 R Bioconductor; Risso et al., 2018 http://bioconductor.org/packages/release/b...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: (E) Quantification of the number of DE genes for each major cell type as a function of spatial location using imputed gene expression data derived from Harmony integration.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: The batch effect introduced by the panels and platforms, captured by PC1 was successfully removed using Harmony integration 17 ( Figure 3E ).
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Clathrin-associated AP-1 controls termination of STING signalling. (Nature 2022)

- DOI: 10.1038/s41586-022-05354-0 | PMCID: PMC9605868 | PMID: 36261523
- Version used: **4.9**
- Evidence: Image analysis and quantification were performed by combining PerkinElmer Harmony (v.4.9) and Fiji (v.2.3.0), and data were further processed with KNIME (v.4.3.2) and GraphPad PRISM 9 (v.9.3.1).
- Full pipeline: quantification [Harmony v4.9] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Evidence: (d) UMAP plots of the combined scRNA-seq data after QC filtering (see Github script) and Harmony integration, colored by donor.
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Version used: **0.1.0**
- Evidence: On the basis of this set of highly variable genes and the variance decomposition, we then performed PCA on the whole dataset using denoisePCA, and then used Harmony (v.0.1.0) on the PCs to adjust for library effects 69 .
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **0.0.5**
- Evidence: At this level, we used Harmony (v.0.0.5) 91 and scVI from scvi-tools (v.0.19.0) in parallel for batch correction (again treating each donor as a separate batch) for every broad lineage and observed highly consistent embedding and clustering (data provided on the portal).
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors. (Nature 2024)

- DOI: 10.1038/s41586-024-07943-7 | PMCID: PMC11560846 | PMID: 39385035
- Version used: **0.1.1**
- Evidence: The Seurat R package (v.4.3) was used to analyse the normalized gene–cell matrix and Harmony (v.0.1.1) was applied for batch-effect correction.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> normalisation [DESeq2, Harmony v0.1.1, R, Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: Cells were first separated by their L2 (major cell-type groups) annotation using the shared marker gene approach, and then Harmony integration by pairwise ages for all L2 groups was used to link L3 cell types across ages.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Version used: **3.8**
- Evidence: Manually curated datasets were integrated with Harmony (v.3.8) 66 .
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Single-cell multiplex chromatin and RNA interactions in ageing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07239-w | PMCID: PMC11023937 | PMID: 38538789
- Version used: **0.1.1**
- Evidence: The count matrix from all brains was then integrated using RunHarmony from the harmony R package (v.0.1.1) 60 based on STransform processed data, and regressed out on factors including individual library and experimental batches.
- Full pipeline: alignment/mapping [Bowtie2 v5.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Docker, Harmony v0.1.1, R, Seurat v4.3.0, Snakemake]

### Anti-TIGIT antibody improves PD-L1 blockade through myeloid and T&lt;sub&gt;reg&lt;/sub&gt; cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07121-9 | PMCID: PMC11139643 | PMID: 38418879
- Version used: **1.0**
- Evidence: Batch effects were mitigated using the Harmony (v.1.0) package 54 .
- Full pipeline: alignment/mapping [Bioconductor, R] -> quantification [Bioconductor, R] -> normalisation [Harmony v1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [fgsea] -> stage not stated [Seurat]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Version used: **0.1.1**
- Evidence: Harmony (v.0.1.1) was used to correct the dataset and samples.
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Lineage-resolved atlas of the developing human cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-09033-8 | PMCID: PMC12589122 | PMID: 41193842
- Evidence: Iterative clustering to identify subtypes of cells was performed by subsetting the full Seurat object to only cells that were present in desired clusters, then re-running Harmony integration, cluster identification, and dimensional reduction.
- Full pipeline: dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [Seurat v4.3.0.9002]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: Batch correction was applied to species with more than one age collected using Harmony integration 41 .
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: Harmony integration and uniform manifold approximation and projection (UMAP) revealed clear separation between the two conditions, which indicated that Atrx loss induces considerable changes in the cell transcriptional state (Fig.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Version used: **0.1.1**
- Evidence: Following preprocessing, the skin data were harmonized using the package Harmony (v.0.1.1) 79 with a maximum iteration setting of 20.
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **0.1.1**
- Evidence: A data harmonization method known as Harmony (v.0.1.1) 78 with parameter theta = 0 was applied to remove sample-specific biological differences, addressing variations specific to cell types and states.
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **1.2.3**
- Evidence: For the integration analysis, we merged all high-quality cells from independent TrackerSeq datasets using Seurat (v.5.1.0), performed SCTransform v.2 normalization (regressing out mitochondrial percentage) and PCA, applied Harmony (v.1.2.3; https://github.com/immunogenomics/harmony ) with the IntegrateLayers function, and used the top 30 Harmony embeddings for UMAP visualization and clustering.
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Agouti integrates environmental cues to regulate paternal behaviour. (Nature 2026)

- DOI: 10.1038/s41586-026-10123-4 | PMCID: PMC13019464 | PMID: 41708861
- Evidence: We performed Harmony integration 38 , computed nearest neighbours and identified eight major cell clusters using nearest neighbour modularity optimization, projected onto a uniform manifold and approximation projection embedding (Fig.
- Full pipeline: read trimming [R, scDblFinder] -> dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [DESeq2, Seurat]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **1.2.0**
- Evidence: Batch integration was performed with Harmony (v.1.2.0) 75 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: PCA was performed, and batch correction was implemented through Harmony integration 80 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: To integrate the samples from the two different sequencing runs, the IntegrateLayers function from Seurat was used, with the Harmony integration method run using the SCT assay.
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Version used: **1.2.1**
- Evidence: Annotation of main cell types Objects of different patients and samples were merged, log-normalized and integrated per patient using Harmony (v.1.2.1) 69 .
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Version used: **1.2.1**
- Evidence: Principal components were then further batch-corrected using Harmony (v.1.2.1) 59 algorithm for sample integration, and harmonized components were used as input for Louvain clustering and dimensionality reduction using uniform manifold approximation and projection (UMAP).
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **1.2.3**
- Evidence: We conducted a focused analysis on the CD8 + T cells, performing integration with Harmony (v.1.2.3) 49 using the default parameters (using dataset and donor as covariates), and dimensionality reduction and visualization with Seurat (v.5.2.1) 50 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Resolvin D1 prevents injurious neutrophil swarming in transplanted lungs. (PNAS 2023)

- DOI: 10.1073/pnas.2302938120 | PMCID: PMC10400944 | PMID: 37487095
- Evidence: ( A ) Annotated cell types depicted in Unsupervised UMAP plot clustering of 22,645 cells after quality control and data filtering using Harmony integration.
- Full pipeline: quality control [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Enrichr, ggpubr] -> stage not stated [Seurat v4.0.0]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: As with the fetal grafts, five distinct clusters in the hPSC-derived grafts were identified and visualized using UMAP and graph-based clustering after Harmony integration ( Fig.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: Following quality control, cohorts were combined and the harmony R package corrected the batch effects ( 34 ).
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Integrating single-cell data with biological variables. (PNAS 2025)

- DOI: 10.1073/pnas.2416516122 | PMCID: PMC12067276 | PMID: 40294274
- Evidence: We annotated the dataset using a combined strategy involving Harmony integration, Leiden clustering ( 26 ), and ScType annotation ( 27 ), identifying 13 cell types ( Fig.
- Full pipeline: dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Seurat] -> machine learning [Seurat] -> visualisation [UMAP] -> stage not stated [R]

### An atlas of early human mandibular endochondral and osteogenic paracrine signaling regions of Meckel's cartilage. (PNAS 2025)

- DOI: 10.1073/pnas.2420466122 | PMCID: PMC11962497 | PMID: 40096606
- Version used: **1.2.0**
- Evidence: Batch effects arising from differences in experimental conditions or sequencing runs were corrected via Harmony (v.1.2.0) to harmonize the datasets.
- Full pipeline: normalisation [Harmony v1.2.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib v3.7.2, UMAP] -> stage not stated [CellChat, CellPhoneDB, Seurat v4.0.0]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **0.1.0**
- Evidence: These dimensions were then corrected using Harmony (v.0.1.0) ( 82 ) to facilitate integration between samples.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

