# AnnData

- **Category:** single-cell
- **Papers in survey:** 58
- **Journals:** Nature (39), Cell (9), PNAS (7), Science (3)
- **Years:** 2021 (3), 2022 (3), 2023 (7), 2024 (12), 2025 (19), 2026 (14)
- **Versions named:** 0.8.0 (4), 0.7.4 (2), 0.11.4 (1), 0.10.7 (1), 0.9.1 (1), 0.7.5.2 (1), 0.10 (1), 0.6.22 (1), 0.11 (1), 0.7.5 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (9), normalisation (7), visualisation (5), simulation/modelling (2), machine learning (2), quality control (1), differential/statistical testing (1), structure determination (1), alignment/mapping (1), quantification (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: This droplet matrix was processed as an AnnData object using our preprocessing pipeline which utilizes the Scanpy toolkit ( Wolf et al., 2018 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **0.7.4**
- Evidence: We trained this network for 400 epochs and used the latent representation as a low dimensional embedding to compute a k-nearest neighbor graph for the integrated cells with k = 15, using SCANPY ( Wolf et al., 2018 ) (version 1.6.0; anndata version 0.7.4) and calculate a UMAP layout ( McInnes et al., 2018 ).
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...ichment results generated using single-cell ATAC-seq This paper Zenodo: https://doi.org/10.5281/zenodo.6120249 CBD-KEY-CITESEQ-ANNDATA : Contains two anndata objects: This paper Zenodo: https://doi.org/10.5281/zenodo.6120249 For the purpose of online visualization a limited version of the gene expression data is also provided via the CZI Science cellxgene Data Portal: https://cellxgene.cziscience....
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Version used: **0.7.5**
- Evidence: 1.6) and anndata (v.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: 64 https://github.com/scverse/anndata BBKNN Polahski et al.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: We used AnnData.concatenate function 193 and repeated the processing as described above.
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: We also used Muon (v.0.1.3) to process the fragment files and generate the AnnData .h5ad files.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Perturb-Multimodal: A platform for pooled genetic screens with imaging and sequencing in intact mammalian tissue. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.022 | PMCID: PMC12324982 | PMID: 40513557
- Evidence: The total number of molecules of each type for each cell was summed, and the result exported as an AnnData objective.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose, XGBoost] -> stage not stated [AnnData, Scanpy]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **0.11**
- Evidence: 74 N/A Plasmid: pOPINB pOPINB was a gift from Ray Owens Addgene plasmid # 41142; http://n2t.net/addgene:41142 ; RRID:Addgene_41142 Plasmid: pOPINK pOPINK was a gift from Ray Owens Addgene plasmid # 41143; http://n2t.net/addgene:41143 ; RRID:Addgene_41143 Software and algorithms anndata (v0.11) Virshup et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: Clustering and determination of homologous cell types Much of the analysis pipeline was based on scanpy infrastructure and AnnData data structures 49 .
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Version used: **0.7.5.2**
- Evidence: For RNA velocity analysis using scVelo v0.2.4, the total, spliced and unspliced count matrices, along with the UMAP embeddings, were exported as an h5ad file using anndata v0.7.5.2 for R.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **0.8.0**
- Evidence: ...9.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-image 0.18.1, squidpy 1.1.2, anndata 0.8.0 and itertools 8.0.0.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: Imaging and behaviour data from each session were imported into the anndata object 58 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### CD4<sup>+</sup> T cell-induced inflammatory cell death controls immune-evasive tumours. (Nature 2023)

- DOI: 10.1038/s41586-023-06199-x | PMCID: PMC10307640 | PMID: 37316667
- Evidence: The count matrices were loaded into the scanpy environment, merged with the previously generated anndata objects and normalized using scvelo.pp.filter_and_normalize.
- Full pipeline: quantification [velocyto] -> normalisation [AnnData, Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [ImageJ v1.52i, R, scVelo]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: The scRNA-seq data need to be prepared in the AnnData format ( https://anndata.readthedocs.io/en/latest/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: The resulting epithelial dataset was further split by region (stomach, small intestine and large intestine), prepared for projection using scANVI_prepare_anndata function (fills 0s for non-overlapping genes) and projected onto the respective healthy reference epithelial region-specific latent space embeddings.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: Furthermore, we assigned the decoded RNA molecules to segmented cells using STRtree (v2.0.6) and subsequently generated AnnData objects following the approach described by Virshup et al.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **0.10.7**
- Evidence: Scanpy v.1.9.1 with anndata v.0.10.7 and the statistics and plotting libraries pandas v.2.2.2, numpy v.1.26.4, scipy v.1.13.0, seaborn v.0.13.2 and matplotlib v.3.8.4 were used for data analysis and visualization.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: We then concatenated all remaining datasets to create a single AnnData 80 object.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Adult skull bone marrow is an expanding and resilient haematopoietic reservoir. (Nature 2024)

- DOI: 10.1038/s41586-024-08163-9 | PMCID: PMC11618084 | PMID: 39537918
- Evidence: Raw counts were imported as AnnData 63 objects.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [Matplotlib, UMAP] -> visualisation [Matplotlib] -> stage not stated [AnnData, ImageJ, Scanpy]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: Matrix files for each pair of samples (GFP and mCherry cells under the same treatment) were read with Scanpy (v.1.9.6) 118 and concatenated in the same AnnData object (v.0.10.3) 119 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **0.9.1**
- Evidence: ...conducted in a Python environment built on Pandas (v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and seaborn (v.0.13.1) 77 packages.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: To perform trajectory analysis, the un-spliced and spliced variant count matrix that was calculated using 10× pipeline in velocyto (v0.17.16) was fused with an anndata object containing the UMAP information and cluster identities defined in Seurat analysis.
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **0.8.0**
- Evidence: DGE matrices were processed using the following R and python packages: Seurat (v.3.2.2) 64 , SeuratDisk (v.0.0.0.9010) 65 , anndata (v.0.8.0) 66 , numpy (v.1.17.5) 67 , pandas (v.1.0.5) 68 , 69 and Scanpy (v.1.9.1) 70 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: Next, we merged the three library files and matched the reconstructed image to the unified AnnData object.
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: Pseudotime calculation For pseudotime and trajectory inference, we converted anndata objects to R object with Zellkonverter and used the R package Slingshot 44 .
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Evidence: The count matrix from each sample was merged into a single AnnData object by Scanpy, and doublets were removed running Scrublet software in Python before conversion to Seurat using SeuratDisk’s function Convert 57 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### A parabrachial hub for need-state control of enduring pain. (Nature 2025)

- DOI: 10.1038/s41586-025-09602-x | PMCID: PMC12630001 | PMID: 41062698
- Evidence: Data integration, standardization and AnnData construction.
- Full pipeline: quantification [NumPy, Scanpy] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP, seaborn] -> visualisation [UMAP, seaborn] -> stage not stated [AnnData, ImageJ]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Evidence: After quality control, raw count matrices and AnnData objects were concatenated, and counts were normalized to transcripts per million using sc.pp.normalize_total, followed by log-transformation with sc.pp.log1p.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: Integrated anndata objects containing multiple scRNA-seq datasets were combined using adata.concatenate() with join=‘outer’.
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: Pre-processing of scRNA-seq data The output obtained from Cell Ranger was read as an AnnData object.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **0.7.4**
- Evidence: ...n plots, error bars and contour figures were generated using the following Python, R and Matlab packages: Python: pandas (v.1.1.5), numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork (v.1.1.3), RColor...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Both the computational analysis library and the code for all analyses are available online through GitHub and Zenodo, as detailed in the Code and Data availability sections. spatiomic comes with support for multiple common microscopy imaging formats and flexibly supports AnnData 74 objects, NumPy 75 arrays and pandas DataFrames 76 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: To cluster cells into niches, we created an anndata object of the neighbourhood matrix for use in Scanpy and corrected for batch effects with Harmony and BBKNN before Leiden clustering.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Count matrices and AnnData objects were then combined using a concatenate function, normalized to log transcripts per million units using the ‘sc.pp.normalize_total’ function, and log-transformed using the ‘sc.pp.log1p’ function.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: We run Scanorama (default settings; knn = 20) 55 on the resulting AnnData object to batch correct across patients.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Evidence: To integrate all species data using SAMap, we first converted Seurat objects with M. undulatus liver and published data ( D. rerio 45 , X. laevis 46 , M. undulatus , M. musculus 47 and H. sapiens 48 ) to anndata objects using the R package loom.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: For further analysis using moscot.time in Python, the Seurat objects were transformed into AnnData 96 objects using SeuratData 97 .
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Version used: **0.8.0**
- Evidence: For other data analysis and plotting tasks, we used Python (3.8.13), pandas (1.4.2), matplotlib (3.5.1), seaborn (0.12.2), numpy (1.21.6), scipy (1.8.0), sklearn (1.0.2), anndata (0.8.0), scanpy (1.9.1), squidpy (1.1.2), tissue-sc (0.0.2), tangram-sc (1.0.3), spage (accessed September 1, 2022), gseapy (1.0.4), umap-learn (0.5.3) and statsmodels (0.13.2).
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: The gene expression table was extracted as an AnnData object for downstream single-cell analysis.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### A spatial atlas of the healthy human liver from live donors. (Nature 2026)

- DOI: 10.1038/s41586-026-10377-y | PMCID: PMC13216088 | PMID: 41986723
- Evidence: Liver cell atlas using snRNA-seq snRNA-seq data were generated from liver tissues of four individuals (M5, M6, M7 and M8) and combined into a single AnnData object.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> machine learning [QuPath] -> visualisation [Scanpy v1.10.0] -> stage not stated [AnnData, Cellpose, GSEA]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: The Seurat object, along with Slingshot pseudotime coordinates, was converted to an AnnData object with Seurat’s Convert function for analysis in Python.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Evidence: Cell-gene count matrices were analysed using a combination of published packages and custom scripts centred around the SCANPY/AnnData ecosystem 73 . scRNA-seq datasets from different mouse models and primary patient samples were analysed separately using similar workflows. scRNA-seq data were compiled into a combined count matrix.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: Clustering using MapMyCells A count matrix as an AnnData object was extracted and uploaded to the Allen Brain Atlas MapMyCells website.
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: After converting the expression space to log [CPM/100 + 1], the anndata object was transposed to the gene space to identify cell cycling genes in a data-driven manner, as previously described 73 , 74 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: First, an AnnData object was created with b2c.read_visium, then filtered to retain bins with at least one count and genes expressed in at least three spots (min_counts = 1, min_cells = 3).
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **0.11.4**
- Evidence: Commonly used Python libraries (Python v3.11.13, matplotlib v3.10, Seaborn v0.13, numpy v2.2.6, pandas v2.3.1, scipy v1.16.0, anndata v0.11.4 and shapely v2.1.1) were applied to visualize spatial distribution of cells.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: ...sible expression format (CEF) file and converted into a hierarchical data format version 5 annotated data (h5ad) file format using the Python package AnnData (see ‘Data availability’); for study II, h5ad file formats were available.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Version used: **0.6.22**
- Evidence: Many of the described preprocessing steps are done via the Python packages Scanpy, version 1.4.3, and AnnData, version 0.6.22 ( 50 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Effects of oxycodone on placental lineages: Evidence from the transcriptome profile of mouse trophoblast giant cells. (PNAS 2024)

- DOI: 10.1073/pnas.2412349121 | PMCID: PMC11551428 | PMID: 39475633
- Evidence: Using the provided Python scripts from Parse Bioscience Pipeline, we generated splice and unspliced matrices from their transcript assignment data file, which contains splicing information for each transcript, and converted the matrices into anndata object ( 85 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, Python, Seurat v5.0.1]

### A spatiotemporal molecular atlas of the ovulating mouse ovary. (PNAS 2024)

- DOI: 10.1073/pnas.2317418121 | PMCID: PMC10835069 | PMID: 38252830
- Evidence: Slide-seq count matrix and the position information for every bead barcode were loaded into an AnnData object using scanpy ( 54 ) (v1.9.1).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SCENIC, scikit-learn] -> visualisation [Squidpy] -> stage not stated [AnnData, CellPhoneDB, Scanpy]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Version used: **0.8.0**
- Evidence: All 12 filtered feature-barcode matrices generated by Cell Ranger were loaded as anndata (v0.8.0) ( 40 ) objects and subsequently merged into a unified dataset.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### ATP-sensitive potassium channels alter glycolytic flux to modulate cortical activity and sleep. (PNAS 2025)

- DOI: 10.1073/pnas.2416578122 | PMCID: PMC11874466 | PMID: 39964713
- Evidence: The anndata package was used to load the log2 normalization files (expression data) and pandas for the data manipulation.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib] -> stage not stated [R]

### Olfactory inputs to appetite neurons in the hypothalamus. (PNAS 2026)

- DOI: 10.1073/pnas.2524926123 | PMCID: PMC12867749 | PMID: 41591908
- Version used: **0.10**
- Evidence: The imputed, cell-by-gene expression matrix (downloaded from the “ABC Atlas Cache”) was processed using Scanpy v1.9 and AnnData v0.10 in Python 3.12.
- Full pipeline: alignment/mapping [Cufflinks] -> quantification [AnnData v0.10, Cufflinks, Matplotlib v3.8, Scanpy v1.9] -> visualisation [Matplotlib v3.8, Python]

### A temporal and spatial atlas of adaptive immune responses in the lymph node following viral infection. (PNAS 2026)

- DOI: 10.1073/pnas.2504742123 | PMCID: PMC12867689 | PMID: 41587309
- Evidence: By integrating the corresponding bead barcode location files downloaded from Curio Bioscience website, slide-seq count matrix with spatial position information for each sample was generated and loaded into an AnnData object using Scanpy (v1.9.8) ( 60 ).
- Full pipeline: stage not stated [AnnData, Docker, Scanpy v1.9.8, SciPy]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: Processed data objects are available for online visualization and download in AnnData format ( 98 ) at https://developmental.cellatlas.io/fetal-immune , as well as trained scVI models for query to reference mapping and trained Celltypist models for cell annotation.
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: SEACell normalization and cell type annotation After SEACell inference, peak accessibility matrices for control and PIMQ were aggregated independently using hard SEACell assignments, resulting in metacell-level AnnData objects (control_meta_ad, pimq_meta_ad).
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Ontogeny of the spinal cord dorsal horn. (Science 2026)

- DOI: 10.1126/science.adx5781 | PMCID: PMC12879194 | PMID: 41505538
- Evidence: PCA embeddings (90PCs) were extracted from the preprocessed AnnData object and then were used to compute diffusion maps (n=50 components) via Palantir, followed by construction of a multiscale diffusion space (X_palantir).
- Full pipeline: quality control [R v4.4.1, Seurat] -> dimensionality reduction/clustering [AnnData, R v4.4.1, Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [ggplot2] -> stage not stated [ImageJ]

