# CellChat

- **Category:** single-cell
- **Papers in survey:** 80
- **Journals:** PNAS (40), Nature (34), Science (3), Cell (3)
- **Years:** 2021 (2), 2022 (3), 2023 (10), 2024 (17), 2025 (37), 2026 (11)
- **Versions named:** 1.6.1 (4), 2.1.2 (2), 1.1.3 (1), 1.1.1 (1), 1.5 (1), 1.1.0 (1), 1.6.0 (1), 2.1.1 (1), 0.5.5 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (10), differential/statistical testing (4), quantification (2), variant calling (2), visualisation (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **0.5.5**
- Evidence: Potential cell-cell interactions between the different subclusters of macrophages and mesenchymal cells were identified using CellChat v0.5.5 ( Jin et al., 2021 ).
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: CellChat analysis was performed to infer intercellular communication (CD45.2 + [mutant] and CD45.1 + [WT] cells from ‘10% Dnmt3a R878H/+ BMT’ mice) by integrating the data from scRNA-seq analysis with the ligand-receptor database CellChatDB (v2).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Version used: **2.1.2**
- Evidence: Cell Communication Analysis To evaluate the performance of STAMP in identifying key cell-cell communication, we analyzed the LPS condition at 4 hours using CellChat (v2.1.2), 57 an R package designed to identify intercellular communication from single-cell RNA sequencing data.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Molecularly defined and spatially resolved cell atlas of the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06808-9 | PMCID: PMC10719103 | PMID: 38092912
- Evidence: We used the CellChat database 74 to define the ligand–receptor pairs.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose v2.0] -> stage not stated [CellChat, scDblFinder, scikit-learn]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: LIANA was configured to use the following methods: ‘cellphonedb’, ‘connectome’, ‘logfc’ (iTALK), ‘natmi’, ‘sca’ (SingleCellSignalR), ‘call_cellchat’ (CellChat) and ‘cytotalk’.
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Version used: **1.6.0**
- Evidence: Inference of cell–cell communication was done with CellChat (v.1.6.0), for both single-cell and spatial RNA-seq data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Ligand–receptor interaction analyses Ligand–receptor analyses were performed on the basis of the CellChat package (v.1.0.0; https://github.com/sqjin/CellChat ).
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: ...ChemoCAF for all of the fibroblast and myeloid populations from the scRNA sequencing STAMP tumour atlas. i-j , Communication probability estimated by CellChat for i , CXCL chemokine pathway with fibroblasts subclusters as the sender populations and myeloid subclusters as the receiver and j , CCL chemokine pathway with fibroblasts subclusters as the sender populations and myeloid subclusters as the...
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Version used: **1.1.1**
- Evidence: Cell–cell interaction analysis Cell–cell interaction analysis was performed using LIANA+ (v1.0.4) 89 , CellChat (v1.1.1) 90 and CellPhoneDB v3 (statistical_method) 91 to determine cell–cell interactions occurring in the small intestine during Crohn’s disease.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: Spatial cell–cell interaction at tumour boundary We evaluated the spatial-based cell–cell interaction (CCI) in the ST sample using COMMOT 69 with CellChat database and distance threshold of 1,000 µm, following the same threshold used in the original publication for Visium.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Version used: **1.5**
- Evidence: Intercellular communication analysis was performed using CellChat (v.1.5) 70 .
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Evidence: We used the sketchData() function from CellChat 67 , with default parameters, to select one-third of the sequenced cells for each donor in the homeostatic samples described in Extended Data Fig.
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Bottom right, CellChat ligand–receptor analysis of P60 skin. b , Schematic of the experimental setup to test the role of TNFR1 in clonal expansions. c , Clonal expansion is dependent on TNFR1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Myelin plasticity in the ventral tegmental area is required for opioid reward. (Nature 2024)

- DOI: 10.1038/s41586-024-07525-7 | PMCID: PMC11186775 | PMID: 38839962
- Version used: **1.6.1**
- Evidence: Cell–cell communication analysis and inference was performed using CellChat (v.1.6.1) to calculate the aggregated cell–cell communication networks and identify signals contributing to outgoing or incoming signalling of different cell groups 38 .
- Full pipeline: dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [Seurat v4.3.0] -> stage not stated [CellChat v1.6.1]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: Interactome analysis was performed on human APAP-ALF and mouse APAP-induced liver injury datasets, using CellChat 51 R package v1.6.1 with default parameters.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **1.1.0**
- Evidence: Cell–cell interaction analysis CellChat (v.1.1.0) 45 detected ligand–receptor interactions on integrated sc/snRNA-seq data according to the standard procedures.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **1.6.1**
- Evidence: CCI analysis We applied CellChat (v.1.6.1) 71 to our scRNA-seq dataset to identify region-specific CCIs.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Evidence: Differential cell–cell communication was compared before or after UA treatment using default settings in the CellChat R package.
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Evidence: Cell–cell communication analysis using CellChat To explore intercellular communication among microglial subclusters (MC1–MC3) and other surrounding cell types, we applied CellChat 103 to spatial RNA data from 5 d.p.l. and 10 d.p.l. samples.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: CellChat analysis To investigate potential signalling pathways mediating communication between external cell populations (mesenchymal cell population at E45 and the perichondrium at E53) and the internal cartilaginous model in spatial transcriptomic sections at E45 and E53, we employed CellChat 72 .
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Evidence: We analysed cell–cell interaction using CellChat v.2 (ref.
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **1.6.1**
- Evidence: Then, we used the CellChat (v1.6.1) library to analyse the cell–cell communication patterns.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: Cell–cell communication We used CellChat 69 to infer intercellular communication, based on known receptor–ligand interactions.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: CCC analysis We applied the standard workflow of CellChat 69 (v1.5.0), utilizing single-cell gene expression of ligands and receptors to infer a CCC network.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: To analyse intercellular communication involving the differing KC subclusters to hepatocytes, a CellChat analysis was performed.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: We also validated these results using an alternative tool, CellChat 69 (Extended Data Fig.
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Evidence: Cell–cell communication analysis We used the CellChat package (v.1.6.1) to decipher cell–cell communication networks using its extensive database of known human ligand–receptor interactions.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: The relative strengths of each pathway were calculated using spatial CellChat on n = 2 samples from four timepoints. g , The spatiotemporal differentiation model for intestinal T RM cells.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **1.6.1**
- Evidence: Quantification of ligand–receptor communication using CellChat We implemented CellChat (v.1.6.1) 14 to quantify the strength of interactions among cell types using the default parameter settings (Supplementary Table 8 ).
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Version used: **1.1.3**
- Evidence: Cell–cell communication We used CellChat v1.1.3 38 for the analysis of cell–cell communication, which was performed separately for each of the four stages of tumorigenesis.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: Ligand–receptor analysis Ligand–receptor analysis was performed using the CellChat package 71 .
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **2.1.2**
- Evidence: Immune cell–cell communications were estimated using CellChat (v.2.1.2) 70 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Identification of communication networks and ligand–receptor pairs between epithelial cells and fibroblasts was performed using CellChat by following standard analysis protocols 62 .
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Spatially resolved cell–cell communication analysis Intercellular signalling among spatially resolved cell types was analysed using CellChat (v.2) 36 .
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: Cell–cell interaction Interactions between cell types were inferred using the CellChat 62 package in R with default parameters for cells from astrocytes, CA neurons and neurogenic cells (NSCs, neuroblasts and immature neurons grouped together).
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Evidence: Cell–cell communication analyses CellChat 44 , 79 analysis was used to infer pathway and ligand–receptor interactions among core basal and dividing keratinocyte, papillary fibroblast, pericyte and blood vessel clusters from the E90, P3, P10 and 6 mo porcine skin scRNA-seq datasets in parallel, following the standard CellChat pipeline with the human ligand–receptor database to infer cell–cell commu...
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Evidence: The list was further selected by including only pairs that also met one of the following criteria: (1) present in CellChat’s (CellChatDB.human.rda) curated database for annotations 74 ; (2) present in CellChat protein–protein interaction experimental data (PPI.human.rda); (3) Nichenet 75 database weight >0.9 or (4) Nichenet database weight >0.8 and present in CellTalk 76 (human_lr_pair.txt) or Sin...
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Effects of sex and aging on the immune cell landscape as assessed by single-cell transcriptomic analysis. (PNAS 2021)

- DOI: 10.1073/pnas.2023216118 | PMCID: PMC8379935 | PMID: 34385315
- Evidence: To better understand the effect of sex and age on cellular communication, using our dataset, we conducted a bioinformatics analysis of cell–cell communication using iTALK and CellChat ( 18 , 19 ), which could quantitatively characterize and compare the inferred cell–cell communication, based on the average expression of the ligands and receptors in cell populations.
- Full pipeline: stage not stated [CellChat]

### Transcriptional and functional motifs defining renal function revealed by single-nucleus RNA sequencing. (PNAS 2022)

- DOI: 10.1073/pnas.2203179119 | PMCID: PMC9231607 | PMID: 35696569
- Evidence: CellChat ( 74 ) analysis showed that 12 signaling pathways were prominent in the mouse kidney, including EGF, FGF, GAS, GRN, MIF, MIK, MK, ncWNT, NRG, PTN, SPP1, VISFATIN, and WNT.
- Full pipeline: alignment/mapping [SCENIC] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Deciphering the endometrial niche of human thin endometrium at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2115912119 | PMCID: PMC8872762 | PMID: 35169075
- Evidence: To globally interrogate the incoming and outgoing signaling in endometrial cells, CellChat was applied to investigate cellular cross-talk among different cell types in normal endometrium ( 25 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB]

### Pathogenic TNF-α drives peripheral nerve inflammation in an Aire-deficient model of autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2114406119 | PMCID: PMC8795502 | PMID: 35058362
- Evidence: Given this evidence of prominent cytokine signaling networks, we used CellChat to identify ligand–receptor interactions and predict cell–cell communication inputs and outputs ( 26 ).
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellChat, Seurat]

### Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. (PNAS 2023)

- DOI: 10.1073/pnas.2315096120 | PMCID: PMC10710069 | PMID: 38011564
- Evidence: To investigate potential intercellular communications among keratinocyte subtypes, we employed the CellChat program to visualize the expression levels of the inflammatory factors differentially expressed in HS lesions versus healthy skin ( 40 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [CellChat] -> visualisation [CellChat, HOMER, UMAP]

### Leveraging single-cell RNA sequencing to unravel the impact of aging on stroke recovery mechanisms in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2300012120 | PMCID: PMC10288588 | PMID: 37307473
- Evidence: Hence, we took advantage of CellChat ( 29 ) to infer cell-to-cell communication and explore potential cross talk between MG/MΦ and EC/OL lineage cells ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, R, Seurat]

### PHGDH preserves one-carbon cycle to confer metabolic plasticity in chemoresistant gastric cancer during nutrient stress. (PNAS 2023)

- DOI: 10.1073/pnas.2217826120 | PMCID: PMC10214193 | PMID: 37192160
- Evidence: Analysis of cell-to-cell communication via CellChat revealed active signaling communication among EMT-type cell clusters via the inferred WNT signaling network ( Fig.
- Full pipeline: dimensionality reduction/clustering [CellChat, R, SCENIC, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> structure determination [SCENIC] -> visualisation [UMAP] -> stage not stated [GSVA]

### Self-renewing macrophages in dorsal root ganglia contribute to promote nerve regeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2215906120 | PMCID: PMC9963351 | PMID: 36763532
- Evidence: The cell–cell interactions between different cell types in the DRG dataset were evaluated using CellChat (Version 1.4.0, R package).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Metascape, R]

### Transcriptional reprogramming primes CD8+ T cells toward exhaustion in Myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2024)

- DOI: 10.1073/pnas.2415119121 | PMCID: PMC11648872 | PMID: 39621903
- Evidence: To survey signaling irregularities in ME γδT cells, we used CellChat ( 25 ) to infer intercellular communication networks between γδT cells and other lymphocytes and compared the interaction strengths between cases and controls.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, GSEA]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Evidence: The integrated scRNA-seq datasets were split by genotypes and processed to CellChat ( 36 ) analysis.
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: To understand the cross-talk between tumor cells and other cells within the TME, we used the R package CellChat ( Fig.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Senolytic and senomorphic agent procyanidin C1 alleviates structural and functional decline in the aged retina. (PNAS 2024)

- DOI: 10.1073/pnas.2311028121 | PMCID: PMC11067450 | PMID: 38657052
- Evidence: Furthermore, we utilized the CellChat to analyze the intricate communication networks among different cell types.
- Full pipeline: stage not stated [CellChat]

### The IRG1-itaconate axis protects from cholesterol-induced inflammation and atherosclerosis. (PNAS 2024)

- DOI: 10.1073/pnas.2400675121 | PMCID: PMC11009655 | PMID: 38564634
- Evidence: Cell–cell communication was examined using the CellChat package (v1.6.1) for the entire dataset ( 29 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, ImageJ]

### Heterogeneous osteoimmune profiles via single-cell transcriptomics in osteoporotic patients who fail bisphosphonate treatment. (PNAS 2024)

- DOI: 10.1073/pnas.2316871121 | PMCID: PMC10895260 | PMID: 38346184
- Evidence: CellChat analysis revealed an increased abundance and strength of cell–cell communication in the normal condition compared to osteoporosis, including the identification of normal-specific cell–cell communication patterns ( Fig.
- Full pipeline: quantification [CellChat] -> dimensionality reduction/clustering [UMAP]

### Effective treatment of optic neuropathies by intraocular delivery of MSC-sEVs through augmenting the G-CSF-macrophage pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2305947121 | PMCID: PMC10861878 | PMID: 38289952
- Evidence: Inferring the cell−cell communication patterns (CCC) by CellChat illustrated that MSC-sEVs triggered enormous changes in interactions among the cell clusters in the retinal microenvironment ( Fig.
- Full pipeline: dimensionality reduction/clustering [CellChat, GSEA, UMAP] -> visualisation [UMAP]

### Dysregulated NAMPT signaling underlines the immune-suppressive microenvironment in venous leg ulcers. (PNAS 2025)

- DOI: 10.1073/pnas.2512142122 | PMCID: PMC12772187 | PMID: 41439711
- Evidence: We next employed CellChat ( 26 ) to analyze cell–cell interactions across distinct cellular clusters in both VLUs and NS.
- Full pipeline: dimensionality reduction/clustering [CellChat, UMAP] -> stage not stated [GSEA]

### Breast cancer cell coculture induces normal lung fibroblast transition to CAFs, promoting tumor cell dormancy and therapy resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2423894122 | PMCID: PMC12663926 | PMID: 41269792
- Evidence: Cell–cell signaling inference using CellChat methodology ( 68 ) was then employed to explore the mechanism by which LFs mediated autophagy induction in cocultured MB231 cells.
- Full pipeline: dimensionality reduction/clustering [GSVA, UMAP] -> visualisation [UMAP] -> stage not stated [CellChat]

### Engineering a spatiotemporal macrophage circuit via STING phase separation to override immune suppression in pancreatic cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2504718122 | PMCID: PMC12664005 | PMID: 41264244
- Evidence: Consistently, CellChat analysis positioned these TAM subsets as central signaling hubs orchestrating tumor-stroma crosstalk ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, GSEA]

### A unified framework for identification of cell-type-specific spatially variable genes in spatial transcriptomic studies. (PNAS 2025)

- DOI: 10.1073/pnas.2503952122 | PMCID: PMC12646224 | PMID: 41223223
- Evidence: This was also validated by applying CellChat ( 73 ), whose results revealed that CEACAM signaling pathway was an important component of the cell–cell communication network in this breast cancer dataset ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [LDSC, MAGMA] -> stage not stated [CellChat, R]

### MC1R determines healing outcomes in acute and chronic cutaneous wounds. (PNAS 2025)

- DOI: 10.1073/pnas.2503308122 | PMCID: PMC12646273 | PMID: 41218117
- Evidence: Cell–cell communication was inferred using CellChat, which integrates scRNA-seq with ligand–receptor databases.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, ImageJ, R v4.2.2, Seurat v4.4]

### The RANK/RANKL axis controls vascular dynamics in the bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2425366122 | PMCID: PMC12625855 | PMID: 41183210
- Evidence: Using CellChat, we identified CAR cells, osteoblasts, and osteocytes as potential sources of RANKL supplied to RANK-positive BMECs ( 29 ) ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Serum response factor is essential for endometrial function and prevention of inflammatory fibrosis. (PNAS 2025)

- DOI: 10.1073/pnas.2510060122 | PMCID: PMC12595411 | PMID: 41150713
- Evidence: ( C ) Circle plots display CellChat ligand–receptor analysis of selected signaling pathways among selected cell populations, split by genotype. **** P adj < 0.0001, calculated via Seurat’s FindMarkers function, which uses the nonparametric Wilcoxon rank-sum test.
- Full pipeline: variant calling [CellChat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Single-cell sequencing uncovers sensory neuron-mediated CGRP signaling as a driver of sarcoma progression. (PNAS 2025)

- DOI: 10.1073/pnas.2500161122 | PMCID: PMC12582254 | PMID: 41118222
- Evidence: The R package CellChat ( 33 ) was used to investigate the overall cell–cell network interactions among different types of TME cells, tumor cells with TrkA + neurons ( Fig.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [CellChat, Cytoscape]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: CellChat ( 47 ) (v2.1.2) was used to assess intercellular communication between immune subpopulations in presymptomatic and symptomatic SMA infants.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Cellular cartography reveals mouse prostate organization and determinants of castration resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2427116122 | PMCID: PMC12415206 | PMID: 40854129
- Evidence: Analysis of ligand–receptor interactions by CellPhoneDB and CellChat ( 39 , 40 ) showed dramatic changes in epithelial cell–stromal cell communication after castration, suggesting that physiologically relevant, specific cell–cell interactions occur even while prostatic involution and widespread cell death occur.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB, GSVA, SCENIC]

### Blood-labyrinth barrier damage mediated by granzymes from cytotoxic lymphocytes results in hearing loss in systemic lupus erythematosus. (PNAS 2025)

- DOI: 10.1073/pnas.2423240122 | PMCID: PMC12377648 | PMID: 40794837
- Evidence: To explore the intercellular signaling pathways between these cell types, we performed a cell–cell communication analysis using CellChat algorithms.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cytoscape, GSVA, STRING db]

### Cell-type-informed genotyping of mosaic focal epilepsies reveals cell-autonomous and non-cell-autonomous disease-associated transcriptional programs. (PNAS 2025)

- DOI: 10.1073/pnas.2509622122 | PMCID: PMC12305027 | PMID: 40674414
- Evidence: CellChat Analysis.
- Full pipeline: normalisation [Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [CellChat, fgsea v1.28.0]

### &lt;i&gt;Piezo2&lt;/i&gt;+ mechanosensory neurons orchestrate postnatal development through mechano-chemo-transduction of PDGFA signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2504103122 | PMCID: PMC12280930 | PMID: 40627386
- Evidence: To explore the interaction between sensory nerves and the molar, we integrated the scRNA-seq data from the trigeminal ganglion ( 35 ) and molar ( 36 ) to dissect cell–cell interactions using CellChat.
- Full pipeline: stage not stated [CellChat]

### Immune cell profiling reveals diverse niches of immune residents of the enteric nervous system and potential neuroimmune interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2413692122 | PMCID: PMC12232633 | PMID: 40549903
- Evidence: Transcriptomic profiles of neurons and immune cells were integrated from published scRNAseq data and used for CellChat to predict ligand–receptor interactions.
- Full pipeline: stage not stated [CellChat]

### Astrocytic Ryk signaling coordinates scarring and wound healing after spinal cord injury. (PNAS 2025)

- DOI: 10.1073/pnas.2417400122 | PMCID: PMC12012454 | PMID: 40208942
- Evidence: ( B ) CellChat chord diagram showing changes of strength of cell–cell signaling in Ryk cKO .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Dual genetic tracing demonstrates the heterogeneous differentiation and function of neuromesodermal progenitors in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2402305122 | PMCID: PMC12002027 | PMID: 40178900
- Evidence: We then conducted CellChat analysis to explore the relationships between different clusters.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [CellChat, UMAP]

### An atlas of early human mandibular endochondral and osteogenic paracrine signaling regions of Meckel's cartilage. (PNAS 2025)

- DOI: 10.1073/pnas.2420466122 | PMCID: PMC11962497 | PMID: 40096606
- Evidence: CellPhoneDB and CellChat were used to analyze cell–cell communication networks from the scRNA–seq data.
- Full pipeline: normalisation [Harmony v1.2.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib v3.7.2, UMAP] -> stage not stated [CellChat, CellPhoneDB, Seurat v4.0.0]

### Multiomics analysis unveils the cellular ecosystem with clinical relevance in aldosterone-producing adenomas with &lt;i&gt;KCNJ5&lt;/i&gt; mutations. (PNAS 2025)

- DOI: 10.1073/pnas.2421489122 | PMCID: PMC11892633 | PMID: 40009643
- Version used: **2.1.1**
- Evidence: To explore cellular crosstalk within the TME in APA, we performed cell–cell interaction analysis using CellChat (version 2.1.1) ( 43 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat v2.1.1, SCENIC]

### Engineered immunological niche directs therapeutic development in models of progressive multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2409852122 | PMCID: PMC11848328 | PMID: 39937858
- Evidence: The CellChat package (v.1.6.1) ( 28 ) was used to identify communication between cells, and alterations in communication with disease were identified using differential expression analysis workflow between conditions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [CellChat] -> stage not stated [R, Seurat]

### Astrocytic EphA4 signaling is important for the elimination of excitatory synapses in Alzheimer's disease. (PNAS 2025)

- DOI: 10.1073/pnas.2420324122 | PMCID: PMC11848297 | PMID: 39928878
- Evidence: ( H ) Bar chart showing the communication strengths of the top pathways between CA3 and CA1 excitatory neurons identified by CellChat.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Uterine organoids reveal insights into epithelial specification and plasticity in development and disease. (PNAS 2025)

- DOI: 10.1073/pnas.2422694122 | PMCID: PMC11804710 | PMID: 39883834
- Evidence: CellChat ( 45 ) analysis was then used to identify candidate pathways regulating cell–cell interactions in the developing uterus ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [CellChat, GSEA]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Evidence: Cell–cell communication calculation and analysis was performed using CellChat ( 30 ), an R-based analysis tool.
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### NAT10/ac&lt;sup&gt;4&lt;/sup&gt;C drives intrahepatic cholangiocarcinoma by suppressing transposable elements via chromatin remodeling. (PNAS 2026)

- DOI: 10.1073/pnas.2532263123 | PMCID: PMC13187814 | PMID: 42133812
- Evidence: ( H ) CellChat analysis depicting the interaction quantity and strength between malignant epithelial cells and T cell subsets in NAT10 -high vs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, GSEA]

### Type I interferons induced upon respiratory viral infection impair lung metastatic initiation. (PNAS 2026)

- DOI: 10.1073/pnas.2412919123 | PMCID: PMC13099621 | PMID: 41996163
- Evidence: CellChat was used to identify receptor–ligand interaction changes between the two conditions ( 59 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, GSEA]

### Psoriasis-like disease prevents squamous skin tumor development by neutrophil-driven inflammation. (PNAS 2026)

- DOI: 10.1073/pnas.2536378123 | PMCID: PMC12994166 | PMID: 41802042
- Evidence: ( E ) CellChat-based comparison of ligand-receptor interactions between neutrophils and all other cell clusters in control and DKO *K15 .
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [CellChat, UMAP]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: We also quantitatively inferred cell–cell communications with CellChat ( 74 ) to identify the signal-outgoing and the signal-receiving cell subsets.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Branched actin networks mediate macrophage-dependent host-microbiota homeostasis. (Science 2025)

- DOI: 10.1126/science.adr9571 | PMCID: PMC7618398 | PMID: 41231985
- Evidence: Because an interaction between monocytes or macrophages and regulatory T cells (T reg cells) in the intestine is essential for maintaining tolerance ( 23 ), we assessed the cell-to-cell cross-talk in our scRNA-seq dataset using CellChat ( 24 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Single intramuscular injection of self-amplifying RNA of &lt;i&gt;Nppa&lt;/i&gt; to treat myocardial infarction. (Science 2026)

- DOI: 10.1126/science.adu9394 | PMCID: PMC13124201 | PMID: 41785353
- Evidence: Intercellular communication analysis was conducted using the CellChat R package (version 2.2.0).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, R, Seurat v5.3.0, Slingshot v2.14.0]

