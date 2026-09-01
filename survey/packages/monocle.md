# Monocle

- **Category:** single-cell
- **Papers in survey:** 107
- **Journals:** PNAS (58), Nature (41), Science (4), Cell (4)
- **Years:** 2021 (10), 2022 (12), 2023 (24), 2024 (16), 2025 (32), 2026 (13)
- **Versions named:** 1.3.1 (2), 1.3.7 (2), 1.2.9 (2), 2.32.0 (1), 2.3.6 (1), 0.2.2 (1), 2.24.0 (1), 1.2.7 (1), 2.28.0 (1), 2.20.0 (1)
- **Pipeline stages it appears in:** simulation/modelling (50), dimensionality reduction/clustering (28), differential/statistical testing (6), alignment/mapping (5), visualisation (4), normalisation (3), quantification (3), structure determination (2), variant calling (1)

## Papers

### Integrated analysis of multimodal single-cell data. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.048 | PMCID: PMC8238499 | PMID: 34062119
- Evidence: We then calculated Moran’s I, a spatial autocorrelation metric proposed to identify trajectory-dependent genes in Monocle3 ( Cao et al., 2019 ), to identify correlated genes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat v3.2.0, Signac v1.0.0]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: ...ters n = 200, grid.n = 40, arrow.scale = 3, min.grid.cell.mass = 0.5 and scale = ”sqrt.” Trajectories on compartment embeddings were calculated using Monocle 3 algorithm ( Qiu et al., 2017 ).
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 93 https://github.com/theislab/scvelo Monocle 3 (version: 1.0.0) 68,88 https://github.com/cole-trapnell-lab/monocle3 pySCENIC (version: 0.11.2) 59,94 https://github.com/aertslab/pySCENIC ComplexHeatmap (version 2.6.2) Gu et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### BCAA-nitrogen flux in brown fat controls metabolic health independent of thermogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.030 | PMCID: PMC11145561 | PMID: 38653240
- Evidence: Raw files were converted to mzXML, and monoisotopic peaks were re-assigned using Monocle 72 .
- Full pipeline: stage not stated [Bioconductor, Monocle]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Version used: **0.2.2**
- Evidence: We used two functions ‘fit_models’ and ‘compare_models’ in R package Monocle3 (v.0.2.2) 80 to perform the differential test.
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: Pseudotime analysis The Monocle 3 R package 68 ( https://cole-trapnell-lab.github.io/monocle3/ ) was used for pseudotime calculation of the co-embedded RNA and ATAC dataset.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### A transcriptomic atlas of mouse cerebellar cortex comprehensively defines cell types. (Nature 2021)

- DOI: 10.1038/s41586-021-03220-z | PMCID: PMC8494635 | PMID: 34616064
- Evidence: Continuity of gene expression To characterize molecular variation across cell types, we attempted to quantify the continuity of scaled gene expression across a given cell type pair, ordered by pseudotime rank (calculated using Monocle2).
- Full pipeline: quantification [Monocle] -> normalisation [Monocle, Seurat v2.3.4] -> dimensionality reduction/clustering [Seurat v2.3.4, UMAP] -> stage not stated [ImageJ]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: The following common, freely available data analysis software was used in this project: scrublet version 0.1 ( https://github.com/swolock/scrublet ), Scanpy version 1.6.0 ( https://github.com/theislab/scanpy ), Monocle versions 2, 3 and 3-alpha ( https://cole-trapnell-lab.github.io/monocle3 ), Seurat version 3 ( https://github.com/satijalab/seurat ) and ggplot2 version 3.3.5 ( https://ggplot2.tidy...
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Evidence: In addition, we also applied the Monocle DDRTree method 66 given its widespread use.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: Trajectory and pseudotime were computed based on the corresponding UMAP using Monocle 3 (ref.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### Single-cell delineation of lineage and genetic identity in the mouse brain. (Nature 2022)

- DOI: 10.1038/s41586-021-04237-0 | PMCID: PMC8770128 | PMID: 34912118
- Evidence: Trajectory analysis of embryonic datasets Trajectory inference and pseudotime calculations were done with Monocle3 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [R v3.6.0, Seurat, scDblFinder v2.0.3, velocyto]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: Inference of cis -co-accessible cCREs Cis -co-accessibility cCREs are predicted for all open regions in each of the 275 cell subclasses separately using Cicero for Monocle 3 72 , 93 with the default parameters and the mouse mm10 genome, scanning the mouse genome with a window size of 500 kb.
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Evidence: The downstream dimension reduction and clustering analysis were carried out with Monocle v3 (ref.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Embryo-scale reverse genetics at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06720-2 | PMCID: PMC10665197 | PMID: 37968389
- Version used: **1.3.1**
- Evidence: Additional clusters of multiplets not removed using this procedure were manually inspected for marker genes and removed. scRNA-seq analysis After RNA and hash-quality filtering, data were processed using the Monocle3 (v.1.3.1) workflow defaults except where specified: estimate_size_factors() , detect_genes(min_expr = 0.1) , preprocess_cds() with 100 principal components (using all genes) for whole...
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Monocle v1.3.1, UMAP] -> differential/statistical testing [GSEA, R] -> stage not stated [ImageJ, fgsea v1.26.0]

### Spatial epigenome-transcriptome co-profiling of mammalian tissues. (Nature 2023)

- DOI: 10.1038/s41586-023-05795-1 | PMCID: PMC10076218 | PMID: 36922587
- Evidence: Monocle2 pseudotime analysis showed a bifurcation in chromatin accessibility but not in RNA expression; one path led to regions close to the ventricular zone (green pixels, Extended Data Fig.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.2] -> visualisation [ArchR v1.0.1, Seurat v4.1] -> stage not stated [Monocle, Signac v1.8]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: The datasets were loaded into R and analysed using the Seurat (v.3) 66 and Monocle3 67 packages.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: CellOracle also works with other pseudotime data, such as Monocle pseudotime and URD pseudotime data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Phenotypic signatures of immune selection in HIV-1 reservoir cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05538-8 | PMCID: PMC9908552 | PMID: 36599977
- Evidence: Dimension reduction and clustering UMAP embeddings in two dimensions of the centred log-ratio values was carried out through the Monocle 3 (ref.
- Full pipeline: quality control [UMAP] -> alignment/mapping [MAFFT, SAMtools v1.9] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [R] -> visualisation [MAFFT, UMAP] -> stage not stated [Cutadapt v2.5]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Version used: **2.3.6**
- Evidence: Trajectory inference and trajectory alignment Trajectory inference was performed with Monocle 2.3.6 (refs.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: Trajectory analysis Monocle3 To infer the developmental trajectory giving rise to MGN or INFLAREs in the ileum IBD, we used monocle3 (v1.3.1) 94 on a subset of data containing cells in the ileum from studies 5 , 6 , 22 .
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: After quality-control filtering to remove low-quality sequenced cells, all downstream analysis, including pseudotime analysis, a technique that models single-cell transcriptional change as a continuum, was performed using the Seurat 63 , 64 , Monocle 65 or dynverse 66 implementations in R.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### Plasmacytoid dendritic cells control homeostasis of megakaryopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07671-y | PMCID: PMC11254756 | PMID: 38987596
- Evidence: Trajectory analysis was performed on the following cell types: metabolic MKPs, late MKP, MK-MEPs, cycling MK-MEPs and early MKPs using Monocle3 80 , 81 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [Monocle] -> stage not stated [DESeq2 v1.30.0, GSEA, Seurat]

### Single-cell atlas of the human brain vasculature across development, adulthood and disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07493-y | PMCID: PMC11324530 | PMID: 38987604
- Evidence: We ordered ECs along a one-dimensional transcriptional gradient using Monocle 88 and TSCAN 89 to examine the AV axis in the different entities.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> stage not stated [Seurat]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Evidence: Pseudotime analysis For the myofibre degeneration trajectory, DCLK1 + (type I), ID1 + (type I), ID1 + (type II), ENOX1 + (type II) and other unperturbed myonuclei were selected for pseudotime analysis using Monocle3 69 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Evidence: Analysis of alveolar cell differentiation states and trajectories Analysis of differentiation trajectories of lung alveolar and malignant cells was performed using Monocle 2 (ref.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: (3) The dimensionality of the data was reduced by PCA (50 components) first on the top 5,000 most highly dispersed genes and then with UMAP (max_components = 2, n_neighbors = 50, min_dist = 0.1, metric = ‘cosine’) using Monocle 3-alpha 14 .
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: Reconstruction of the developmental trajectory Popular computational methods such as Monocle 81 , PAGA 82 , Slingshot 83 and RNA Velocity 84 leverage the gradients in the transcriptomic space to infer a cell-type trajectory.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Evidence: The Seurat object was converted into a cds object in Monocle3 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: 2 , x-axis) onto clusters identified in s (y-axis). v-w , Pseudotime ( v , Monocle3) and UMAP plots separated by condition ( w ) showing potential myeloid differentiation trajectories, including monocyte-to-SAM (top) and microglia-to-DAM (bottom), with monocytes and microglia as root states. x , Schematic showing effect of TGFβ-activated myofibroblasts on SAM/DAM formation. y-z , Violin plots ( y ...
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Version used: **2.32.0**
- Evidence: Cell trajectory analysis Cell trajectory analysis was performed using Monocle2 (v2.32.0) in R (v4.4.1).
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Evidence: ...ia. a , GFP + iMG were isolated from 6-week-old organoids (2 wpt) via FACS and subjected to scRNA-seq. b , UMAP visualization of iMG subclusters. c , Monocle3-based pseudotime analysis reveals the developmental trajectory of iMG. d , Heatmap displaying the top 20 marker genes for each iMG subcluster. e , PCA indicates that iMG exhibit transcriptomic profiles similar to published human iPSC-derived...
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Pseudotime was then inferred on the SCT assay of the extracted epidermal cells using Monocle3 (ref.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Evidence: Generation of synthetic cells To investigate the dynamics of chromatin states during mouse pre-implantation development, we generated synthetic cells as follows: We ordered scRNA-seq cells along the developmental trajectory using Monocle3 (ref.
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: Pseudotime analysis was performed using Monocle3 69 .
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: For trajectory analyses, clones shared between tissue and blood were subsampled and used for UMAP dimensional reduction, and the pseudotime for these cells was calculated by using Monocle3 (ref.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: Ambient-corrected count matrices for the different samples were then merged and converted for further processing with Monocle3-alpha (v2.99.3) 45 ( www.github.com/cole-trapnell-lab/monocle-release/tree/monocle3_alpha ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Cell trajectory analysis for selected populations was performed using the Monocle 3 package 61 .
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Evidence: The analysis was conducted using Monocle 2 (v.2.34.0) 58 .
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: For trajectory inference analyses, Monocle3 (ref.
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **1.3.1**
- Evidence: Tumour cell-type trajectory inference To assist with annotations of tumour subgroups and their hierarchy from stem-like to differentiated, trajectory inference for tumour cells was performed with Monocle3 (v.1.3.1) 68 , 69 .
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **1.3.7**
- Evidence: Construction of pseudotime trajectories Pseudotime trajectories were constructed to model cellular differentiation dynamics using two R packages, Monocle3 (v.1.3.7, https://cole-trapnell-lab.github.io/monocle3 ) and Slingshot (v.2.14.0).
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **1.2.9**
- Evidence: Pseudo-time analyses We conducted pseudotime analysis using Monocle3 (v.1.2.9) to delineate sample trajectories based on signals in genomic regions for all 1,170 tissue-signatures.ICSs.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Evidence: The postnatal integrated interfollicular epidermis keratinocytes were also converted from a Seurat object to a CDA object using the SeuratWrappers package to perform pseudotime analysis in Monocle3 (ref.
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: Monocle3 (ref.
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: Samples were pre-processed using the standard Monocle3 pipeline.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Altered cell and RNA isoform diversity in aging Down syndrome brains. (PNAS 2021)

- DOI: 10.1073/pnas.2114326118 | PMCID: PMC8617492 | PMID: 34795060
- Version used: **0.2.1**
- Evidence: Count matrices and UMAP projections of specific cell types from Seurat analysis were loaded into Monocle3 (v0.2.1).
- Full pipeline: normalisation [Seurat v3.0.3] -> dimensionality reduction/clustering [Monocle v0.2.1, UMAP] -> visualisation [UMAP]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Version used: **2.14**
- Evidence: Pseudotime trajectory was calculated using Monocle2 (version 2.14) ( 47 – 49 ) using the method “DDRTree” with the top 1,000 differentially expressed genes between each of the clusters found from the Seurat clustering.
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Version used: **0.2.3.0**
- Evidence: Gene modules were identified using the R package Monocle3 v.0.2.3.0 ( 75 ), GO and KEGG pathway enrichment analysis was performed using ClusterProfiler v.3.14.3 ( 76 ) and KEGG pathways visualized with GOplot v.1.0.2 ( 77 ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### Early role for a Na<sup>+</sup>,K<sup>+</sup>-ATPase (<i>ATP1A3</i>) in brain development. (PNAS 2021)

- DOI: 10.1073/pnas.2023333118 | PMCID: PMC8237684 | PMID: 34161264
- Evidence: Dots represent individual cells. y axis: log-transformed, scaled expression of ATP1A3 by cell. x axis: pseudotime score (color-coded) for each cell, calculated using the Monocle3 algorithm.
- Full pipeline: normalisation [Monocle] -> dimensionality reduction/clustering [UMAP] -> stage not stated [PyMOL]

### Single-cell atlas of developing murine adrenal gland reveals relation of Schwann cell precursor signature to neuroblastoma phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2022350118 | PMCID: PMC7865168 | PMID: 33500353
- Evidence: A developmental trajectory analysis using Monocle 3 was performed to assess the differentiation route taken by the adrenal primordium cells.
- Full pipeline: normalisation [R, Seurat, limma] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [featureCounts v1.5.2]

### Specification of neuronal subtypes in the spiral ganglion begins prior to birth in the mouse. (PNAS 2022)

- DOI: 10.1073/pnas.2203935119 | PMCID: PMC9860252 | PMID: 36409884
- Evidence: Data was processed and analyzed using the following R-based packages: Seurat (v3.2) ( 47 ), DoubletFinder (v2.0.3) ( 48 ), Harmony (v1.0) ( 49 ), Slingshot (v1.8) ( 17 ), tradeSeq (v1.4)( 20 ), Monocle 3 ( 21 , 50 ), and SCENIC ( 23 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle, SCENIC, Seurat v3.2, Slingshot v1.8, scDblFinder v2.0.3]

### Amelioration of pathologic α-synuclein-induced Parkinson's disease by irisin. (PNAS 2022)

- DOI: 10.1073/pnas.2204835119 | PMCID: PMC9457183 | PMID: 36044549
- Evidence: Monocle was used to reassign monoisotopic peaks ( 46 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [Monocle]

### Tumor-polarized GPX3&lt;sup&gt;+&lt;/sup&gt; AT2 lung epithelial cells promote premetastatic niche formation. (PNAS 2022)

- DOI: 10.1073/pnas.2201899119 | PMCID: PMC9371733 | PMID: 35914155
- Evidence: Furthermore, pseudotime analysis by Monocle 3 indicated that cluster 7, as the end of the pseudo timeline, was not in the same branch as other clusters in AT2 cells ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Monocle, clusterProfiler v3.14.0] -> differential/statistical testing [GSEA, clusterProfiler v3.14.0] -> stage not stated [Seurat v3.0.2]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Evidence: To model the transcriptional dynamics at the otic-epibranchial branching point, we ordered cells along pseudotime using Monocle2 ( 79 ).
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### Single-cell transcriptome and accessible chromatin dynamics during endocrine pancreas development. (PNAS 2022)

- DOI: 10.1073/pnas.2201267119 | PMCID: PMC9245718 | PMID: 35733248
- Evidence: After initial read processing to count transcripts for each gene in each cell ( Dataset S1 ), we used Monocle2 ( 26 ), a single-cell analysis tool, for downstream cell clustering and trajectory analysis ( SI Appendix , Fig.
- Full pipeline: read trimming [Bowtie2, MACS2] -> alignment/mapping [Bowtie2, MACS2] -> quantification [HOMER] -> dimensionality reduction/clustering [Monocle, R] -> simulation/modelling [Monocle] -> visualisation [R]

### Single-cell analyses highlight the proinflammatory contribution of C1q-high monocytes to Behçet's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2204289119 | PMCID: PMC9245671 | PMID: 35727985
- Evidence: These two fates corresponded to the roles of monocytes in replenishing macrophages and DCs ( 39 ) and were confirmed by Monocle 3 ( 40 ) ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [UMAP] -> stage not stated [Monocle, SCENIC]

### Pathogenic TNF-α drives peripheral nerve inflammation in an Aire-deficient model of autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2114406119 | PMCID: PMC8795502 | PMID: 35058362
- Evidence: To test this possibility, we performed pseudotime trajectory analysis using Monocle3 and SeuratWrapper packages to determine the transcriptional fate of immunoregulatory macrophages in groups 1/2 in silico ( Fig.
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellChat, Seurat]

### Antigen perception in T cells by long-term Erk and NFAT signaling dynamics. (PNAS 2023)

- DOI: 10.1073/pnas.2308366120 | PMCID: PMC10756264 | PMID: 38113261
- Version used: **1.2.9**
- Evidence: Analysis was done with Monocle3 (v 1.2.9) ( 96 ), and gene–gene correlations were quantified using LASSO regression ( 71 ) in R.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [Monocle v1.2.9] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle v1.2.9]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: To estimate the stage of differentiation, pseudo-time trajectory analysis was performed using the Monocle3 R software package (version 3.0) algorithm ( 48 ) based on the gene expression pattern.
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Single-cell insights into epithelial morphogenesis in the neonatal mouse uterus. (PNAS 2023)

- DOI: 10.1073/pnas.2316410120 | PMCID: PMC10710066 | PMID: 38019863
- Evidence: Prospective cell trajectories and lineages across pseudotime were predicted with Monocle3 ( 83 ) and differentially expressed genes (DEGs) (FDR P < 0.01) across the pseudotime trajectory determined.
- Full pipeline: quality control [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Monocle] -> simulation/modelling [Monocle]

### MHC class Ib-restricted CD8<sup>+</sup> T cells possess strong tumoricidal activities. (PNAS 2023)

- DOI: 10.1073/pnas.2304689120 | PMCID: PMC10614629 | PMID: 37856544
- Evidence: ( E ) Monocle-generated plots present cell clusters' pseudotime ordering with tissue origin and sub-population color coding.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Evidence: Trajectory analysis was done using Monocle3, which places cells into a trajectory by inferring position by similarity in transcriptional profiles among transcriptomic clusters.
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### Cell type-specific cytonuclear coevolution in three allopolyploid plant species. (PNAS 2023)

- DOI: 10.1073/pnas.2310881120 | PMCID: PMC10556624 | PMID: 37748065
- Evidence: Monocle3 was employed to reconstruct pseudotemporal trajectories for two cotton fiber libraries at different developmental stages.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, UMAP] -> structure determination [Monocle] -> visualisation [UMAP] -> stage not stated [OrthoFinder]

### Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus. (PNAS 2023)

- DOI: 10.1073/pnas.2310163120 | PMCID: PMC10515167 | PMID: 37703282
- Evidence: Pseudotime analysis for shoot regeneration and vascular development was performed using Monocle2 and Monocle3 ( 42 ).
- Full pipeline: quality control [R, Seurat v4.1.0] -> alignment/mapping [STAR] -> normalisation [R, Seurat v4.1.0] -> dimensionality reduction/clustering [R, Seurat v4.1.0, UMAP, clusterProfiler] -> stage not stated [Monocle, velocyto]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Evidence: Differential gene expression tests were performed using the Monocle R package ( 81 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### Glial dysregulation in the human brain in fragile X-associated tremor/ataxia syndrome. (PNAS 2023)

- DOI: 10.1073/pnas.2300052120 | PMCID: PMC10265985 | PMID: 37252957
- Evidence: Following reclustering with Monocle3 ( Fig.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> stage not stated [Seurat]

### A single-cell multiomic analysis of kidney organoid differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2219699120 | PMCID: PMC10193973 | PMID: 37155865
- Version used: **2.20.0**
- Evidence: We used Monocle2 (v2.20.0) ( 76 ) to generate pseudotemporal trajectories during nephron epithelial differentiation as described in our previous paper ( 40 ).
- Full pipeline: quantification [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.20.0] -> stage not stated [MACS2, R, Signac, scDblFinder]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: Differential analysis for the merged clustering was performed on peaks specific to the tumor clusters using Monocle2 ( 54 ) with clusterID as a variable.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### Reprogramming by drug-like molecules leads to regeneration of cochlear hair cell-like cells in adult mice. (PNAS 2023)

- DOI: 10.1073/pnas.2215253120 | PMCID: PMC10151514 | PMID: 37068229
- Evidence: We performed pseudotime trajectory analysis using Monocle3 ( 35 , 36 ) to reveal gene expression kinetics following Dox treatment that induced reprogramming.
- Full pipeline: dimensionality reduction/clustering [Seurat v3.2, UMAP] -> simulation/modelling [Monocle] -> stage not stated [GSEA]

### Cholinergic regulation of vascular endothelial function by human ChAT<sup>+</sup> T cells. (PNAS 2023)

- DOI: 10.1073/pnas.2212476120 | PMCID: PMC10083572 | PMID: 36989306
- Evidence: The sequencing data were aligned to the human genome (assembly GRCh38) and unique feature counts obtained using the inDrop pipeline ( https://github.com/indrops/indrops ), ALRA ( 69 ) and Monocle ( 70 ).
- Full pipeline: alignment/mapping [Monocle] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ] -> stage not stated [MACS2, edgeR]

### Single-nuclei RNA sequencing (snRNA-seq) uncovers trophoblast cell types and lineages in the mature bovine placenta. (PNAS 2023)

- DOI: 10.1073/pnas.2221526120 | PMCID: PMC10041116 | PMID: 36913592
- Evidence: Single-cell trajectory “pseudotime” analysis was conducted using Monocle3 ( 42 ) to better understand how trophoblast cells transition from one state to the next ( Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, Slingshot] -> stage not stated [STRING db]

### c-JUN-mediated transcriptional responses in lymphatic endothelial cells are required for lung fluid clearance at birth. (PNAS 2023)

- DOI: 10.1073/pnas.2215449120 | PMCID: PMC9926280 | PMID: 36595691
- Evidence: ( J ) A pseudotime analysis with Slingshot and Monocle 2 represents the differentiation states of lung LECs proceeding from Cluster 1 to Cluster 3.
- Full pipeline: dimensionality reduction/clustering [GSVA, Monocle, Slingshot, UMAP]

### Cellular heterogeneity and dynamics of the human uterus in healthy premenopausal women. (PNAS 2024)

- DOI: 10.1073/pnas.2404775121 | PMCID: PMC11551439 | PMID: 39471215
- Evidence: ( B ) Joint UMAP projection of cells in all five major cell types, with pseudotime from Monocle3 shown in a color gradient (blue-early; yellow-late), and inferred trajectories shown as green lines.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [SCENIC]

### QSOX1 facilitates dormant esophageal cancer stem cells to evade immune elimination via PD-L1 upregulation and CD8 T cell exclusion. (PNAS 2024)

- DOI: 10.1073/pnas.2407506121 | PMCID: PMC11536095 | PMID: 39432781
- Evidence: ( B ) Pseudotime analysis of tumor cells using Monocle2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ, Monocle]

### Joint trajectory inference for single-cell genomics using deep learning with a mixture prior. (PNAS 2024)

- DOI: 10.1073/pnas.2316256121 | PMCID: PMC11406253 | PMID: 39226366
- Evidence: For systematic benchmarking with real and synthetic datasets, we run PAGA, Monocle 3, and Slingshot via the Dyno platform ( 4 ), which converts these TI methods’ outputs into an estimated trajectory backbone B ^ , estimated cell positions w ~ ^ i ’s, and estimated pseudotime T ^ i ’s.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle, Seurat, Slingshot] -> visualisation [UMAP]

### Hypoxia inducible factor 2α promotes tolerogenic macrophage development during cardiac transplantation through transcriptional regulation of colony stimulating factor 1 receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2319623121 | PMCID: PMC11214057 | PMID: 38889142
- Evidence: To determine whether tolerogenic Ly6c1 monocytes developed into Mrc1 macrophages, we used the Monocle algorithm to map pseudotime ( 16 ), or the progression of gene expression changes that a cell undergoes to transition from one functional state to another.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle]

### DNA hypomethylation ameliorates erosive inflammatory arthritis by modulating interferon regulatory factor-8. (PNAS 2024)

- DOI: 10.1073/pnas.2310264121 | PMCID: PMC10873594 | PMID: 38319963
- Evidence: Trajectory branch analysis using Monocle3 identified 22 gen modules that may contribute cell fate specification of Chil3/Plac8/Ly6c2 + Mo ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [Monocle, R]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Version used: **2.28.0**
- Evidence: The gene expression matrix of mesophyll cells was extracted from the object created by Scanpy and underwent further analysis using the Seurat (v4.3.0.1) ( 118 ) and Monocle (v2.28.0) ( 73 ) pipelines.
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Single-cell RNA sequencing unveils unique transcriptomic signatures of endothelial cells and role of ENO1 in response to disturbed flow. (PNAS 2024)

- DOI: 10.1073/pnas.2318904121 | PMCID: PMC10835041 | PMID: 38261622
- Evidence: ( E ) ECs were color-coded for pseudotime trajectory using the Monocle3 algorithm.
- Full pipeline: normalisation [Seurat v4.0.2] -> dimensionality reduction/clustering [GSEA, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0.2]

### Multiscale spatial mapping of cell populations across anatomical sites in healthy human skin and basal cell carcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2313326120 | PMCID: PMC10786309 | PMID: 38165934
- Evidence: ( J ) Single-cell trajectory gene analysis using Monocle 3 showing root nodes in BCC epithelial cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellPhoneDB]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Version used: **1.2.7**
- Evidence: Pseudotime analysis and RNA velocity analysis were performed on the SP fraction using Monocle 3 v1.2.7 ( 67 ), kb-python v0.27.3 ( 68 ), and scVelo v0.3.1 ( 24 ).
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### The SWI/SNF chromatin-remodeling subunit DPF2 regulates macrophage inflammation in intestinal injury via the CACNA1D-mediated MAPK pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2518762122 | PMCID: PMC12646317 | PMID: 41223220
- Evidence: We applied the Monocle 2 algorithm ( 30 ) to order the macrophage clusters in pseudotime to indicate their differentiation trajectories.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle]

### Joint disruption of &lt;i&gt;Ret&lt;/i&gt; and &lt;i&gt;Ednrb&lt;/i&gt; transcription shifts cell fate trajectories in the enteric nervous system in Hirschsprung disease. (PNAS 2025)

- DOI: 10.1073/pnas.2507062122 | PMCID: PMC12582274 | PMID: 41118220
- Evidence: Trajectory analysis was performed with the Monocle3 package ( 47 ).
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [clusterProfiler] -> stage not stated [Seurat]

### TCR signal-enhancing mutation alters lipid metabolism of thymocytes and impairs antitumor immunity of mature T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2507154122 | PMCID: PMC12557506 | PMID: 41100674
- Evidence: ( G ) Trajectory analysis of all thymic T cells using the Monocle 2 algorithm.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle]

### Single-cell transcriptome combined with genetic tracing reveals a roadmap of fibrosis formation during proliferative vitreoretinopathy. (PNAS 2025)

- DOI: 10.1073/pnas.2424487122 | PMCID: PMC12452882 | PMID: 40920930
- Evidence: ( C ) Trajectory showing the cell fate transition of RPE during EMT, colored by Monocle3 pseudotime assignment.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Monocle, Slingshot] -> visualisation [UMAP] -> stage not stated [Cellpose, GSEA]

### A recurrent de novo damaging variant in &lt;i&gt;EMP2&lt;/i&gt; causes progressive symmetric erythrokeratoderma. (PNAS 2025)

- DOI: 10.1073/pnas.2509896122 | PMCID: PMC12358830 | PMID: 40758889
- Evidence: Keratinocyte differentiation scores were calculated by pseudotemporal ordering of keratinocyte clusters using Monocle 3 ( 65 ) with basal cells as a starting population.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [QuPath] -> dimensionality reduction/clustering [Monocle, Seurat, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ANNOVAR]

### SETDB1 ensures the continuity of embryonic to adult neural stem cells through metabolic alterations in the dentate gyrus. (PNAS 2025)

- DOI: 10.1073/pnas.2424315122 | PMCID: PMC12318225 | PMID: 40699919
- Evidence: 5 H ), which was further corroborated using Monocle3 ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle]

### Testicular somatic and germ cell maturation during rhesus macaque development. (PNAS 2025)

- DOI: 10.1073/pnas.2419995122 | PMCID: PMC12232671 | PMID: 40569389
- Evidence: To achieve this, we performed Monocle lineage trajectory on the germ cells which predicted a lineage trajectory from W8 to the germ cells enriched in the W15 cluster ( Fig.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: Given the distinct characteristics of TFF3+MC4, we applied pseudotime analysis using the Monocle algorithm ( 13 ) to decode the cellular evolutionary dynamics.
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Dmrt2 and Hmx2 direct intercalated cell diversity in the mammalian kidney through antagonistic and supporting regulatory processes. (PNAS 2025)

- DOI: 10.1073/pnas.2418471122 | PMCID: PMC12107187 | PMID: 40354537
- Evidence: Monocle2 Pseudotime Analysis.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Monocle, Seurat]

### Hdac1 as an early determinant of intermediate-exhausted CD8<sup>+</sup> T cell fate in chronic viral infection. (PNAS 2025)

- DOI: 10.1073/pnas.2502256122 | PMCID: PMC12088444 | PMID: 40333757
- Evidence: ( B ) Trajectory analysis of WT and Hdac1 –/– single cells with Monocle, as displayed on combined UMAPs of both genotypes.
- Full pipeline: variant calling [Monocle] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [HOMER] -> simulation/modelling [Monocle] -> visualisation [UMAP]

### NEUROD1 efficiently converts peripheral blood cells into neurons with partial reprogramming by pluripotency factors. (PNAS 2025)

- DOI: 10.1073/pnas.2401387122 | PMCID: PMC12067290 | PMID: 40299704
- Evidence: Trajectory analysis using Monocle3 on UMAP indicated a continuum between NSC cluster and neuron cluster, while showing a notable distinction from iPSC cluster ( Fig.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP, scVelo] -> simulation/modelling [Monocle, UMAP]

### Comparative single-cell analysis of transcriptional bursting reveals the role of genome organization in de novo transcript origination. (PNAS 2025)

- DOI: 10.1073/pnas.2425618122 | PMCID: PMC12067204 | PMID: 40305051
- Evidence: When standard batch correction techniques, such as Monocle3’s implementation of batchelor via “align_cds()” ( 6 , 43 ), are applied to remove species-specific effects, Uniform Manifold Approximation and Projection (UMAP) and Principle Component Analysis (PCA) projections show that these effects have been removed with entirely overlapping cell type assignments despite species-specific differences i...
- Full pipeline: alignment/mapping [Monocle, UMAP] -> normalisation [Monocle, UMAP] -> dimensionality reduction/clustering [Monocle, UMAP]

### Acute TREM2 inhibition depletes MAFB-high microglia and hinders remyelination. (PNAS 2025)

- DOI: 10.1073/pnas.2426786122 | PMCID: PMC12002275 | PMID: 40131948
- Evidence: ( C ) The Monocle prediction of the microglia transition trajectory with Seurat’s cluster information in ( A ) mapped alongside pseudotime tree.
- Full pipeline: alignment/mapping [Monocle, Seurat] -> dimensionality reduction/clustering [Monocle, SCENIC, Seurat, UMAP] -> simulation/modelling [Monocle, Seurat]

### Hypercholesterolemia-induced LXR signaling in smooth muscle cells contributes to vascular lesion remodeling and visceral function. (PNAS 2025)

- DOI: 10.1073/pnas.2417512122 | PMCID: PMC11912459 | PMID: 40035761
- Evidence: We ported the public scRNA-seq data to Monocle 3 ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [Monocle]

### Agouti and BMP signaling drive a naturally occurring fate conversion of melanophores to leucophores in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2424180122 | PMCID: PMC11874323 | PMID: 40305763
- Evidence: Cells were collected by fluorescence-activated cell sorting and captured by Chromium controller (10X Genomics) for scRNA-Seq libraries, mapped with 10X CellRanger and analyzed with Monocle3.
- Full pipeline: alignment/mapping [Monocle] -> quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GEMMA]

### Osteocyte connexin hemichannels and prostaglandin E&lt;sub&gt;2&lt;/sub&gt; release dictate bone marrow mesenchymal stromal cell commitment. (PNAS 2025)

- DOI: 10.1073/pnas.2412144122 | PMCID: PMC11848350 | PMID: 39937859
- Evidence: To examine the developmental pseudotime, two approaches were utilized to visualize the differentiation pathways of mesenchymal progenitors (MPs) within the dataset: RNA pseudotime analysis conducted using Monocle 2 ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [Monocle, UMAP] -> stage not stated [GSEA]

### Retinoic acid antagonizes estrogen signaling to maintain adult uterine cell fate. (PNAS 2025)

- DOI: 10.1073/pnas.2416089122 | PMCID: PMC11804538 | PMID: 39874292
- Evidence: To probe into the origin of SQ2 cells, we conducted cell lineage and pseudotime trajectory inference analysis using the Monocle 3 suite in Partek Flow on the PD 21 tKO sample, when SQ2 cells first began to emerge.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle]

### Diffusive topology preserving manifold distances for single-cell data analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2404860121 | PMCID: PMC11789025 | PMID: 39854240
- Evidence: This is particularly evident in large datasets (Embryoid Body and root atlas), where other algorithms-including DPT ( 18 ), Palantir ( 28 ), and Monocle3 ( 29 ) show clear deviations.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> visualisation [UMAP] -> stage not stated [Monocle, Scanpy, scVelo]

### Characterizing progenitor cells in developing and injured spinal cord: Insights from single-nucleus transcriptomics and lineage tracing. (PNAS 2025)

- DOI: 10.1073/pnas.2413140122 | PMCID: PMC11745359 | PMID: 39761400
- Evidence: Additionally, RNA velocity analysis revealed dynamic changes and lineage relationships between astrocytes and oligodendrocytes, consistent with the Monocle pseudotime trajectory.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle]

### A transcription regulator atlas identifies TOX3 as an Atoh1 coactivator in cerebellar development and tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2527163123 | PMCID: PMC13012119 | PMID: 41849381
- Evidence: ( I ) Monocle3 pseudotime analysis of the six clusters depicting the differentiation trajectory from GNPs1 to GN4.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle]

### Bridging unpaired single-cell multimodal data for integrative analyses with SuperMap. (PNAS 2026)

- DOI: 10.1073/pnas.2505182123 | PMCID: PMC12890892 | PMID: 41650244
- Evidence: We applied Monocle3 to infer the cell differentiation trajectory using the integrated latent embeddings of unpaired data.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [ArchR, Signac]

### Functionally heterogeneous intratumoral CD4&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; double-positive T cells can give rise to single-positive T cells. (PNAS 2026)

- DOI: 10.1073/pnas.2506168123 | PMCID: PMC12849695 | PMID: 41557789
- Evidence: Each point in the resulting 2D embedding corresponds to an individual cell by Monocle ( 41 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Monocle, Scanpy]

### The dawn of spatial omics. (Science 2023)

- DOI: 10.1126/science.abq4964 | PMCID: PMC7614974 | PMID: 37535749
- Evidence: Tools designed for disaggregated data [such as the Seurat, ScateR, Scanpy, and Monocle packages ( 90 – 94 )] can provide good results but need to be used cautiously because the nuances of data generation can cause biases.
- Full pipeline: stage not stated [Monocle, Scanpy, Seurat]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Evidence: The potential differentiation trajectory was inferred and plotted using Monocle3 toolkits ( 97 ).
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Version used: **2.24.0**
- Evidence: Pseudotime trajectory analysis for murine samples We employed Monocle2 (2.24.0) ( 28 ) for pseudotime analysis of basal, Krt4/Krt13 + and secretory cells.
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Version used: **1.3.7**
- Evidence: Unsupervised clustering analysis were performed using Monocle 3 (version 1.3.7).
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

