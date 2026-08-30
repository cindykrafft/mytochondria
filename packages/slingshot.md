# Slingshot

- **Category:** single-cell
- **Papers in survey:** 58
- **Journals:** PNAS (28), Nature (27), Science (3)
- **Years:** 2021 (3), 2022 (6), 2023 (13), 2024 (10), 2025 (17), 2026 (9)
- **Versions named:** 2.14.0 (3), 2.6.0 (1), 2.8.0 (1), 2.0.0 (1), 1.8.0 (1), 1.4.0 (1), 2.4.0 (1), 1.8 (1)
- **Pipeline stages it appears in:** simulation/modelling (36), dimensionality reduction/clustering (17), visualisation (4), structure determination (3), differential/statistical testing (2), normalisation (1), quantification (1), alignment/mapping (1)

## Papers

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Lineage Trees/Trajectories and Pseudotime The Slingshot R package 51 was used for lineage tree inference and pseudotime cell ordering inference based on the UMAP/Diffusion Map projection.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Version used: **1.4.0**
- Evidence: Trajectories were predicted using the Slingshot 1.4.0 package 44 , using the function slingshot with default settings and starting with the CD62L + T PEX cell cluster.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### A multidimensional coding architecture of the vagal interoceptive system. (Nature 2022)

- DOI: 10.1038/s41586-022-04515-5 | PMCID: PMC8967724 | PMID: 35296859
- Evidence: Tissue layer trajectory was identified using Slingshot 70 , and DEGs along this trajectory were discovered using tradeSeq 71 .
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [R, Seurat, UMAP, pheatmap] -> stage not stated [CellPhoneDB, Fiji, ImageJ]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **2.0.0**
- Evidence: Pseudotime trajectory analysis was performed using the Slingshot (v.2.0.0) R package 69 with default settings.
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: Slingshot requires two inputs: dimensionality reduced data and a clustering of cells.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: To get accurate pseudotime and trajectory estimation, we removed degenerative cell populations in both PT and TAL and inferred the trajectory for single nuclei and single cells separately using the Slingshot package 94 (v.2.0.0).
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: Pseudotime and trajectory inference analyses were performed using Slingshot 57 (v.2.7.0) for principal curve calculation; SingleCellExperiment 58 (v.1.12.0) and scater 59 (v.1.26.1) were used for gene expression visualization over pseudotime (Fig.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Version used: **1.8.0**
- Evidence: For more details please see the following notebook: https://github.com/ventolab/MFI/blob/main/2_inv_troph_trajectory_and_TFs/2-5_MEFISTO_analysis_inv_troph/S3_DEG_comparison_to_MEFISTO_factor_translation.ipynb Trophoblast trajectory inference analysis To derive trophoblast pseudotime based on transcriptomic similarity, we used Slingshot v1.8.0.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: Slingshot 62 (v.2.6.0) was used to establish a minimum spanning tree on the WNN UMAP using the getLineages function based on mutual nearest neighbour-based distance with DP_pos_sel set as start point and SP_CD4_mature and SP_CD8_mature specified as end points.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Selective utilization of glucose metabolism guides mammalian gastrulation. (Nature 2024)

- DOI: 10.1038/s41586-024-08044-1 | PMCID: PMC11499262 | PMID: 39415005
- Version used: **2.8.0**
- Evidence: Pseudotime and trajectory interference analyses were performed using Slingshot (v2.8.0) 71 for principle curve calculation; SingleCellExperiment (v1.22.0) 72 and scater (v.1.28.0) 73 were used for visualization of gene expression over pseudotime.
- Full pipeline: normalisation [Seurat v4.3.0] -> differential/statistical testing [DESeq2 v1.40.1] -> simulation/modelling [Slingshot v2.8.0] -> visualisation [Slingshot v2.8.0] -> stage not stated [ImageJ]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Evidence: The robustness of Monocle 2-based pseudotemporal ordering prediction was validated by independent pseudotime prediction tools including Palantir 51 , Slingshot 52 and Cellrank 53 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: Reconstruction of the developmental trajectory Popular computational methods such as Monocle 81 , PAGA 82 , Slingshot 83 and RNA Velocity 84 leverage the gradients in the transcriptomic space to infer a cell-type trajectory.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: Pseudotime calculation For pseudotime and trajectory inference, we converted anndata objects to R object with Zellkonverter and used the R package Slingshot 44 .
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: Trajectory analysis We performed trajectory analysis with Slingshot 67 .
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Evidence: To infer developmental trajectories, the Slingshot algorithm was applied to the UMAP coordinates, incorporating RNA velocity information to identify lineage structures.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **2.14.0**
- Evidence: Cell gradients were generated using Slingshot (v.2.14.0) and a custom program developed in Matlab (trajectory analysis: https://github.com/Shixuan1/scRNAseq_trajectory_analysis ) using Matlab built-in functions (for example, pca), the Image Processing Toolbox (Matlab v.2020b) and a Matlab umap package ( https://www.mathworks.com/matlabcentral/fileexchange/71902 ). scRNA-seq data integration used c...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### A molecular cell atlas of mouse lemur, an emerging model primate. (Nature 2025)

- DOI: 10.1038/s41586-025-09113-9 | PMCID: PMC12328211 | PMID: 40739356
- Evidence: Trajectory analysis We used two independent methods to characterize spatial and developmental pseudotime cell trajectories: a custom in-house program in Matlab and Slingshot 48 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Pseudotime analysis of Trpc2 mutant and control datasets For each cell type, pseudotime was calculated across all ages from C57BL/6J data using Slingshot 60 on log-normalized gene expression data and the top 20 principal components calculated from 2,000 variable features.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **2.6.0**
- Evidence: Trajectory inference and trajectory-based differential expression analysis Cells belonging to excitatory neuronal lineages, including RG cells, IPC-ENs and glutamatergic neurons, were selected from the whole dataset for trajectory inference using Slingshot (v.2.6.0) 21 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Evidence: We then analysed the possible lineage trajectories using Slingshot ( Methods ), which revealed multiple lineage trajectories that all shared a common path linking the slow-cycling NCC-like cells to the cycling PC-like cells (trajectory no.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Timely TGFβ signalling inhibition induces notochord. (Nature 2025)

- DOI: 10.1038/s41586-024-08332-w | PMCID: PMC11735409 | PMID: 39695233
- Evidence: Pseudotime inference was performed in R using Slingshot 84 for the clusters between PXM and neural.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> stage not stated [PyTorch, R, Scanpy, scDblFinder]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: 85 ) (v.1.1.0) and Slingshot 86 (v.2.16.0) R packages were used to calculate single-cell potency and pseudotime scores.
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **2.14.0**
- Evidence: Construction of pseudotime trajectories Pseudotime trajectories were constructed to model cellular differentiation dynamics using two R packages, Monocle3 (v.1.3.7, https://cole-trapnell-lab.github.io/monocle3 ) and Slingshot (v.2.14.0).
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### In vivo site-specific engineering to reprogram T cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10235-x | PMCID: PMC13083257 | PMID: 41851456
- Evidence: Spectral flow cytometry Preparation of reference controls for spectral flow cytometry For determining optimal controls for unmixing, reference controls for each marker were prepared on Ultra Comp eBeads Plus (Invitrogen 01-3333-42), Slingshot HyParComp (Slingshot SSB-20-A) and cells (1 million human PBMCs), except for LIVE/DEAD blue.
- Full pipeline: visualisation [Python] -> stage not stated [MACS2, Slingshot]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: Trajectory inference analysis To study differentiation within the adipose cell subsets, we performed trajectory analysis using Slingshot 74 .
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: 2c–c” were created by adapting the GeneTrendCurve.Slingshot function in the ExtendSeurat package.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Trajectory inference and differential expression along trajectories The trajectory inference method Slingshot 87 was applied to recover the lineages originating from the coelomic epithelium during Müllerian duct emergence (6–8 PCW).
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Constructing local cell-specific networks from single-cell data. (PNAS 2021)

- DOI: 10.1073/pnas.2113178118 | PMCID: PMC8713783 | PMID: 34903665
- Evidence: Using Slingshot ( 19 ), we estimate the developmental path consists of two trajectories, one ending in upper-layer (U curve) and the other in deep-layer (D curve) excitatory neurons ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot, UMAP] -> stage not stated [Python v3.7.6, WGCNA]

### Single-cell analyses of renal cell cancers reveal insights into tumor microenvironment, cell of origin, and therapy response. (PNAS 2021)

- DOI: 10.1073/pnas.2103240118 | PMCID: PMC8214680 | PMID: 34099557
- Evidence: Slingshot trajectory analysis (a trajectory inference method, also called pseudotime analysis from single-cell gene expression data, which orders cells along a trajectory based on similarities in their expression patterns and determines lineage structure by identifying branching events) revealed that the PT-B cluster was more closely related to PT-A cells ( Fig.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [GSEA]

### Specification of neuronal subtypes in the spiral ganglion begins prior to birth in the mouse. (PNAS 2022)

- DOI: 10.1073/pnas.2203935119 | PMCID: PMC9860252 | PMID: 36409884
- Version used: **1.8**
- Evidence: Data was processed and analyzed using the following R-based packages: Seurat (v3.2) ( 47 ), DoubletFinder (v2.0.3) ( 48 ), Harmony (v1.0) ( 49 ), Slingshot (v1.8) ( 17 ), tradeSeq (v1.4)( 20 ), Monocle 3 ( 21 , 50 ), and SCENIC ( 23 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle, SCENIC, Seurat v3.2, Slingshot v1.8, scDblFinder v2.0.3]

### Disruption of proteostasis causes IRE1 mediated reprogramming of alveolar epithelial cells. (PNAS 2022)

- DOI: 10.1073/pnas.2123187119 | PMCID: PMC9618079 | PMID: 36252035
- Evidence: Trajectory inference analysis using Slingshot starting from the homeostatic AEC2 cells cluster showed a pseudotemporal relationship (trajectory) that first went through the UPR-activated state into the reprogrammed state and terminated at the AEC1 clusters ( Fig.
- Full pipeline: quantification [Fiji v1.8.0, ImageJ v1.8.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [MACS2]

### Active forgetting requires Sickie function in a dedicated dopamine circuit in <i>Drosophila</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2204229119 | PMCID: PMC9499536 | PMID: 36095217
- Evidence: We did not observe Rac1, Slingshot, or Cofilin among the candidates from our co-IP/MS data, indicating that either Sickie has no direct physical interaction with these proteins in the adult head, or the interaction is too weak, sparse, or transient to be captured through antibody pulldowns.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [STRING db, Slingshot]

### Single-cell analyses highlight the proinflammatory contribution of C1q-high monocytes to Behçet's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2204289119 | PMCID: PMC9245671 | PMID: 35727985
- Evidence: To explore the transitional relationships across monocyte subtypes, we determined the pseudotemporal order and reconstructed the differentiation trajectory using a diffusion map ( 36 ), TSCAN ( 37 ), and Slingshot algorithms ( 38 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [UMAP] -> stage not stated [Monocle, SCENIC]

### Cell type-specific attenuation of brassinosteroid signaling precedes stomatal asymmetric cell division. (PNAS 2023)

- DOI: 10.1073/pnas.2303758120 | PMCID: PMC10483622 | PMID: 37639582
- Evidence: This Seurat object was then converted to a SingleCellExperiment object and Slingshot ( 29 ) was used to calculate a pseudotime lineage, using “UMAP” as reducedDim, “Pavement” as starting cluster, and “Mature GC” as end cluster.
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> stage not stated [R]

### Quantifying common and distinct information in single-cell multimodal data with Tilted Canonical Correlation Analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2303647120 | PMCID: PMC10410705 | PMID: 37523521
- Evidence: ( A ) Asynchrony between the ATAC and RNA measured by the residual of predicting the common RNA with the ATAC modality, plotted against Slingshot’s pseudotime ordering of the cells in the glutamatergic 4 lineage of the human brain development dataset.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Slingshot]

### Slingshot homolog-1-mediated Nrf2 sequestration tips the balance from neuroprotection to neurodegeneration in Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2217128120 | PMCID: PMC10374160 | PMID: 37463212
- Evidence: Slingshot homolog-1 (SSH1) is an actin filament (F-actin)–associated protein phosphatase that normally resides in an inactivated state in a reserve pool bound to 14-3-3 protein.
- Full pipeline: stage not stated [Slingshot]

### PHGDH preserves one-carbon cycle to confer metabolic plasticity in chemoresistant gastric cancer during nutrient stress. (PNAS 2023)

- DOI: 10.1073/pnas.2217826120 | PMCID: PMC10214193 | PMID: 37192160
- Evidence: Analysis of developmental lineages using RNA velocity ( 34 ) and trajectory inference with Slingshot ( 35 ) also indicate high lineage potency in clusters 2, 3, 7, and 8 ( Fig.
- Full pipeline: dimensionality reduction/clustering [CellChat, R, SCENIC, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> structure determination [SCENIC] -> visualisation [UMAP] -> stage not stated [GSVA]

### Single-nuclei RNA sequencing (snRNA-seq) uncovers trophoblast cell types and lineages in the mature bovine placenta. (PNAS 2023)

- DOI: 10.1073/pnas.2221526120 | PMCID: PMC10041116 | PMID: 36913592
- Evidence: Slingshot trajectory analysis ( 43 ) provided a similar cell differentiation path ( SI Appendix , Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, Slingshot] -> stage not stated [STRING db]

### Distinct and opposite effects of leukemogenic <i>Idh</i> and <i>Tet2</i> mutations in hematopoietic stem and progenitor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2208176120 | PMCID: PMC9942850 | PMID: 36652477
- Evidence: The raw sequencing reads were first processed and mapped to mouse genome build GRCm38 using the CellRanger software (v2.1.0, 10X Genomics), followed by analysis using Seurat ( 47 , 97 ), SCENIC ( 45 ), and Slingshot ( 46 ) as detailed in SI Appendix , Supplementary Methods .
- Full pipeline: alignment/mapping [SCENIC, Seurat, Slingshot] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, MACS2]

### c-JUN-mediated transcriptional responses in lymphatic endothelial cells are required for lung fluid clearance at birth. (PNAS 2023)

- DOI: 10.1073/pnas.2215449120 | PMCID: PMC9926280 | PMID: 36595691
- Evidence: ( J ) A pseudotime analysis with Slingshot and Monocle 2 represents the differentiation states of lung LECs proceeding from Cluster 1 to Cluster 3.
- Full pipeline: dimensionality reduction/clustering [GSVA, Monocle, Slingshot, UMAP]

### Identification of a unique subset of tissue-resident memory CD4<sup>+</sup> T cells in Crohn's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2204269120 | PMCID: PMC9910620 | PMID: 36574662
- Evidence: Cell lineage and pseudotime inference analysis using Slingshot ( 39 ) by Seurat divided CD4 + lymphocytes into four lineages ( SI Appendix , fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat, Slingshot]

### Single-cell atlas of &lt;i&gt;Leishmania&lt;/i&gt; development in sandflies reveals the heterogeneity of transmitted parasites and their role in infection. (PNAS 2024)

- DOI: 10.1073/pnas.2406776121 | PMCID: PMC11670217 | PMID: 39700146
- Evidence: Next, we used Slingshot ( 9 ) to estimate the temporal ordering of individual cells along an inferred developmental trajectory where cells are ordered by a pseudotime value that can be interpreted as corresponding to a developmental stage.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: ( B ) Trajectory reconstruction by minimum spanning tree (Slingshot) of identified DA neuron clusters along the temporal axis.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Septo-dentate gyrus cholinergic circuits modulate function and morphogenesis of adult neural stem cells through granule cell intermediaries. (PNAS 2024)

- DOI: 10.1073/pnas.2405117121 | PMCID: PMC11459179 | PMID: 39312657
- Evidence: Pseudotime trajectory of analysis was performed with Slingshot ( 42 ), filtering out lowly expressed genes and using a two-dimensional embedding based on PCA of Z-scores of gene expression patterns in rNSC, rNSC-Like, and Neuroblast cells in control and animals Niche Net Analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> differential/statistical testing [R v4.1] -> simulation/modelling [Slingshot] -> structure determination [Seurat] -> stage not stated [Fiji, ImageJ]

### Joint trajectory inference for single-cell genomics using deep learning with a mixture prior. (PNAS 2024)

- DOI: 10.1073/pnas.2316256121 | PMCID: PMC11406253 | PMID: 39226366
- Evidence: To evaluate the performance of VITAE, we conducted a comparison between VITAE and an alternative approach, starting with integration using Seurat CCA ( 24 ), followed by trajectory inference using Slingshot on the integrated embeddings.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle, Seurat, Slingshot] -> visualisation [UMAP]

### APACE: AlphaFold2 and advanced computing as a service for accelerated discovery in biophysics. (PNAS 2024)

- DOI: 10.1073/pnas.2311888121 | PMCID: PMC11228474 | PMID: 38913887
- Evidence: The system interconnect is HPE Slingshot 11, and uses a Dragonfly topology with adaptive routing.
- Full pipeline: stage not stated [AlphaFold, ColabFold, Docker, Singularity, Slingshot]

### Cell cycle plasticity underlies fractional resistance to palbociclib in ER+/HER2- breast tumor cells. (PNAS 2024)

- DOI: 10.1073/pnas.2309261121 | PMCID: PMC10873600 | PMID: 38324568
- Evidence: To identify and characterize trajectories through the cell cycle under palbociclib treatment, we performed trajectory inference using Slingshot ( 70 ) (slingshot v2.7.0).
- Full pipeline: simulation/modelling [Slingshot] -> stage not stated [scikit-learn v0.24.1]

### Self-organized BMP signaling dynamics underlie the development and evolution of digit segmentation patterns in birds and mammals. (PNAS 2024)

- DOI: 10.1073/pnas.2304470121 | PMCID: PMC10786279 | PMID: 38175868
- Evidence: R packages Seurat v3.1.4 ( 79 ), Destiny ( 33 ), Slingshot ( 34 ), and MAST ( 80 ) were used for analyses, and results were visualized in RStudio.
- Full pipeline: quantification [CellProfiler, R] -> visualisation [Seurat v3.1.4, Slingshot]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: To assess CD4+ Naïve to Effector/Memory T cell differentiation, pseudotime trajectory analysis was conducted using Slingshot ( 48 ) (v2.12.0) and tradeSeq ( 49 ) (v1.18.0).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Humanization of CD47 enables development of functional human neutrophils via postirradiation remodeling of the bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2426546122 | PMCID: PMC12478129 | PMID: 40956886
- Evidence: To infer potential stages of neutrophil maturity throughout the blood, BM, and spleen, we used Slingshot ( 54 ) for trajectory inference and highlighted genes that are representative of various stages of neutrophil maturity ( 22 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [R v4.2.3, Seurat v5.0.1]

### Single-cell transcriptome combined with genetic tracing reveals a roadmap of fibrosis formation during proliferative vitreoretinopathy. (PNAS 2025)

- DOI: 10.1073/pnas.2424487122 | PMCID: PMC12452882 | PMID: 40920930
- Evidence: ( E ) UMAP plot showing one predicted pseudotime trajectory generated using Slingshot analysis.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Monocle, Slingshot] -> visualisation [UMAP] -> stage not stated [Cellpose, GSEA]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: 2 A ) and employed three algorithms to infer cellular evolutionary trajectories leveraging distinct computational frameworks, including VECTOR ( 15 ), Monocle ( 13 ), and Slingshot ( 16 ).
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Mapping the developmental profile of ventricular zone-derived neurons in the human cerebellum. (PNAS 2025)

- DOI: 10.1073/pnas.2415425122 | PMCID: PMC12054822 | PMID: 40249772
- Evidence: ( G ) Marker gene expression over PC-lineage pseudotime using Slingshot reveals a transcriptional trajectory of differentiation from neuroepithelial VZ cells to CALB1 + Purkinje cells (PCs).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [R, Seurat v4.0.2]

### TGFb signaling instructs a conserved fibrosis-associated cell state marked by LRRC15. (PNAS 2026)

- DOI: 10.1073/pnas.2536550123 | PMCID: PMC13214008 | PMID: 42160341
- Evidence: Slingshot cell lineage and pseudotime inference analyses identified three lineage trajectories all descendant from alveolar fibroblasts, two of which corresponded to myofibroblast differentiation trajectories (lineages 2 and 3; SI Appendix , Fig.
- Full pipeline: normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.56.1] -> simulation/modelling [Slingshot]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Version used: **2.4.0**
- Evidence: Pseudotime ordering was performed using Slingshot (v2.4.0) ( 12 ) with UMAP coordinates as the reduced-dimensional input and cluster labels as lineage identifiers.
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Pseudo-time analysis was performed with Slingshot ( 75 ) using MAGIC imputed gene expression matrix.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Evidence: (E) Cell lineage inference for basal, suprabasal, and secretory cell populations from the surface airway epithelium using Slingshot.
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

### Single intramuscular injection of self-amplifying RNA of &lt;i&gt;Nppa&lt;/i&gt; to treat myocardial infarction. (Science 2026)

- DOI: 10.1126/science.adu9394 | PMCID: PMC13124201 | PMID: 41785353
- Version used: **2.14.0**
- Evidence: Pseudotime analysis was performed with the tool Slingshot (version 2.14.0).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, R, Seurat v5.3.0, Slingshot v2.14.0]

