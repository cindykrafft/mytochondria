# scVelo

- **Category:** single-cell
- **Papers in survey:** 64
- **Journals:** Nature (38), PNAS (17), Cell (8), Science (1)
- **Years:** 2021 (4), 2022 (11), 2023 (11), 2024 (18), 2025 (15), 2026 (5)
- **Versions named:** 0.2.4 (7), 0.2.5 (4), 0.24 (2), 0.2.2 (2), 0.3.2 (1), 0.3.1 (1), 0.2.3 (1), 0.3.0 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (15), simulation/modelling (9), quantification (3), normalisation (2), visualisation (2), structure determination (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Version used: **0.2.3**
- Evidence: Then, scVelo version 0.2.3 was used to build models of splicing kinetics to estimate and visualize RNA velocity vector fields in SCENIC integrated UMAP space ( Bergen et al., 2020 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Version used: **0.3.0**
- Evidence: ...– fgsea v1.16.0 Bioconductor https://bioconductor.org/packages/fgsea/ Python Programming Language v3.8.3 Python https://www.python.org Python package scVelo v0.3.0 Bergen et al., 2020 https://scvelo.readthedocs.io/ CellBender Fleming et al., 2019 https://cellbender.readthedocs.io/ Cumulus Li et al., 2020 https://cumulus.readthedocs.io/ Prism 6 GraphPad Software https://www.graphpad.com/scientific-...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 93 https://github.com/theislab/scvelo Monocle 3 (version: 1.0.0) 68,88 https://github.com/cole-trapnell-lab/monocle3 pySCENIC (version: 0.11.2) 59,94 https://github.com/aertslab/pySCENIC ComplexHeatmap (version 2.6.2) Gu et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Mapping transcriptomic vector fields of single cells. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.045 | PMCID: PMC9332140 | PMID: 35108499
- Evidence: The cosine or correlation method is similar to that used by scVelo ( Bergen et al., 2020 ) and can be used to quantify the local consistency of the velocity flow for each cell.
- Full pipeline: quantification [scVelo, scikit-learn] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...b.com/scikit-learn/scikit-learn Scipy ( Virtanen et al., 2020 ) https://scipy.org/ ScVelo ( Bergen et al., 2020 ) v0.1.24 https://github.com/theislab/scvelo Sparse Decomposition of Arrays ( Hore et al., 2016 ) https://jmarchini.org/software/#sda Seaborn Waskom v0.11.1 https://seaborn.pydata.org/ Seurat ( Stuart et al., 2019 ) v3.9.9.9010 SIMON ( Tomic et al., 2019 ) https://genular.org/ singleR ( ...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Based on differently expressed known markers, as well as additional information like number of genes 107 and scVelo 43 implementation of RNA velocity 42 the clusters were annotated with fine cell types, and coarse annotations were refined.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Version used: **0.2.5**
- Evidence: 44 RRID:IMSR_JAX:032770 Oligonucleotides See Table S6 for primer sequences used in this study N/A N/A Software and algorithms BD FACSDiva BD Biosciences RRID: SCR_001456 FCS Express v7 De Novo Software RRID: SCR_016431 Prism v10.1.1 GraphPad RRID: SCR_002798 R v4.3.1 R Core Team RRID: SCR_001905 Cell Ranger v6.1.12 10x Genomics RRID: SCR_017344 scVelo v0.2.5 and v0.17.1 Bergen et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 50 https://bioconductor.org/packages/release/bioc/html/limma.html pheatmap R Kolde 51 https://www.rdocumentation.org/packages/pheatmap/versions/1.0.12/topics/pheatmap Prism 10 GraphPad software https://www.graphpad.com/scientific-software/prism RSEM tool Li and Dewey 52 https://deweylab.github.io/RSEM/ scVelo Bergen et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: Differentiating glia ( COL20A1 ) cluster annotation was based on expression of glial markers, positioning in between differentiating subsets and scVelo results.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### NASH limits anti-tumour surveillance in immunotherapy-treated HCC. (Nature 2021)

- DOI: 10.1038/s41586-021-03362-0 | PMCID: PMC8046670 | PMID: 33762733
- Version used: **0.2.2**
- Evidence: RNA velocity, latent time, root, and terminal states were calculated using the dynamical velocity model from scvelo (0.2.2) 43 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [velocyto v0.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2 v1.28.1] -> stage not stated [R v3.4, scVelo v0.2.2]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: We then used the UMAP embedding matrix computed by the Seurat pipeline to construct the velocity map with the scVelo python package 8 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Evidence: Colored by the pseudotime estimated for each cell with scVelo. p, Smoothed coreHRC, mKi67, and Lgr5 gene signature expression trends in the early and late AKP micrometastasis dataset fitted with Generalized Additive Models as a function of CellRank pseudotime.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **0.2.4**
- Evidence: Next, we used the Velocyto results to learn a generalized dynamical model of RNA velocities by scVelo v0.2.4 66 .
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: Pearson correlation coefficients between cell types for each system, single-cell velocity profiles and latent times were computed using the Scanpy 69 v1.0 and scVelo 70 v0.2.4 tools.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: RNA velocities were calculated using Velo-cyto 46 and analysed with scVelo 47 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Version used: **0.2.4**
- Evidence: For samples at the time of sex specification, we computed RNA velocities 61 to model early somatic development with scVelo (v.0.2.4) 62 following their tutorial.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: Trajectory analysis of activating and inactivating macaque genes We applied scVelo’s dynamical model (release 0.2.3) 52 to derive a shared latent time based on RNA velocity using spliced and unspliced counts from Kallisto.
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Evidence: Mouse trajectories from all fibroblasts and from fascia-to-myofibroblast trajectory clusters were inferred by PAGA with RNA velocity-directed edges using the scvelo toolkit 55 , 56 . ‘Dynamic modeling’ was used under standard settings to calculate velocities.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Version used: **0.2.4**
- Evidence: For RNA velocity analysis using scVelo v0.2.4, the total, spliced and unspliced count matrices, along with the UMAP embeddings, were exported as an h5ad file using anndata v0.7.5.2 for R.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Version used: **0.2.4**
- Evidence: Using scVelo (v.0.2.4) 31 , moments were computed based on the first 20 principal components using the function scvelo.pp.moments() with n_neighbors = 30.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **0.2.4**
- Evidence: 71 ) and RNA velocity was predicted with scVelo v.0.2.4 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Corresponding loom files were loaded into R using the SeuratWrappers function ReadVelocity and converted to Seurat objects using the as.Seurat function. aPT or aTAL trajectory populations were then subset and RNA velocity estimates were calculated using scVelo 98 (v.0.2.4) through a likelihood-based dynamical model.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### CD4<sup>+</sup> T cell-induced inflammatory cell death controls immune-evasive tumours. (Nature 2023)

- DOI: 10.1038/s41586-023-06199-x | PMCID: PMC10307640 | PMID: 37316667
- Evidence: Subsequent analyses were performed using scVelo 62 .
- Full pipeline: quantification [velocyto] -> normalisation [AnnData, Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [ImageJ v1.52i, R, scVelo]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: RNA velocity and cell fate probabilities Loom files were generated with velocyto 48 and dynamical velocities were computed with scvelo 20 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Version used: **0.2.2**
- Evidence: RNA velocity was subsequently calculated using scVelo (v.0.2.2) 27 and further analysed using scanpy (v.1.7.0) 61 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: Velocity analysis 91 was performed using scvelo 92 (v0.2.3).
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: Using pp.moments (n_pcs=10, n_neighbours=30) from the scVelo package (v.0.3.0), first order kinetics matrices were imputed.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: Next, we plotted the STREAM plot using the scVelo package 59 to visualize the cell-type transition matrix.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Evidence: Output loom files were then used in scvelo after export of T N , T CM , T EM and T RM expression matrices containing proximal and distal first-division daughter cells from Seurat and conversion to SCANPY/ANNDATA objects 66 .
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Evidence: This workflow results from an adaptation and integration of CellOracle 71 and scVelo 72 in Python (v.3.7).
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: RNA velocity analysis was processed using the scvelo.pp.moments(n_pcs = 30, n_neighbors = 30) and scvelo.tl.velocity(mode = ‘stochastic’) functions in the scVelo Python package (v.0.2.5) 76 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: Trajectory analysis RNA velocity analysis was conducted using the scVelo package (v0.2.2) with Scanpy (v1.6.1) on Python (v3.8.5).
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Version used: **0.2.4**
- Evidence: RNA velocity analysis RNA velocity analysis 53 was performed using the scVelo (v.0.2.4) package [10].
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Version used: **0.2.5**
- Evidence: For the RNA velocity analysis 24 , loom files were generated using velocyto (v.0.17.17) on all quantified genes. scvelo (v.0.2.5) was used to perform the analysis (that is, filtering, normalization, computing first and second-order moments, and subsequently estimating velocity stochastically).
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Version used: **0.2.5**
- Evidence: Data were merged with gene expression analysis outlined above using scvelo (v.0.2.5) 60 and trajectories were derived using UniTVelo (v.0.2.5.2) 61 configured to run the model based on 1,500 top variable genes.
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Version used: **0.24**
- Evidence: RNA velocity calculations for mesenchymal compartment The scVelo version 0.24 package for Python was used to calculate a ratio of spliced-to-unspliced mRNA abundances in the dataset 88 .
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Evidence: Velocities were computed using the scVelo toolkit (v.0.3.3) 103 , 104 , which estimates transcriptional dynamics across single cells.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Version used: **0.24**
- Evidence: This output file from Velocyto, along with cell annotations and UMAPs from Seurat for each developmental stage, served as input files for scVelo (v.0.24 in a Python environment) 75 to generate RNA velocity plots 75 , 76 (Fig.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: UMAP, t -SNE and heat-map plotting was performed using the Scanpy 59 and scVelo 60 toolkits.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: Interaction scores are averaged across the eight samples, and values are row-normalized. d , The convolved gene expression of cytokines along the crypt–villus axis ordered and displayed with scVelo pooled across all time-course samples for all cells ( n = 8). e , Gene expression trends for TGFβ isoforms separated by timepoint ( n = 2 biological replicates pooled) with representative TGFβ isoform e...
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: Trajectory inference with different trajectory-inference methods We used diffusion pseudo-time 134 , scVelo 39 , veloVI 135 , MultiVelo 136 , CytoTrace 137 and the ConnectivityKernel 16 in CellRank to predict trajectories in the pancreatic endocrinogenesis dataset.
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Version used: **0.2.5**
- Evidence: First-order and second-order moments were computed using scvelo (0.2.5) pp.moments (n_pcs = 30, n_neighbors = 30), and the dynamical model was run with default parameters.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **0.3.2**
- Evidence: The scVelo (v.0.3.2) package 64 in Python was used to infer RNA velocity from nascent transcriptomes.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: NSCs To differentiate astrocytes from NSCs, we performed a subclustering of the NSC/astrocyte population and an RNA velocity analysis using scVelo 55 on the NSC/astrocyte cluster along with neuroblasts, immature neurons and mGCs.
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: Highly variable genes were separately calculated using spliced and unspliced matrices and the top 3,000 genes were used for inferring RNA velocity using scVelo 122 .
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: After concatenation of the spliced and unspliced data from all experiments, the results were merged with the outputs from single-cell analyses performed with Seurat in R, and scVelo 65 was used for further processing.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Neutrophil and natural killer cell imbalances prevent muscle stem cell-mediated regeneration following murine volumetric muscle loss. (PNAS 2022)

- DOI: 10.1073/pnas.2111445119 | PMCID: PMC9169656 | PMID: 35377804
- Evidence: Trajectory analysis was performed on the myogenic cell clusters using scVelo ( 93 ).
- Full pipeline: dimensionality reduction/clustering [UMAP, scVelo] -> simulation/modelling [scVelo] -> visualisation [ggplot2] -> stage not stated [ImageJ, Seurat, velocyto]

### A distinct human cell type expressing MHCII and RORγt with dual characteristics of dendritic cells and type 3 innate lymphoid cells. (PNAS 2023)

- DOI: 10.1073/pnas.2318710120 | PMCID: PMC10756205 | PMID: 38109523
- Evidence: ( F ) Computation of velocity vector length of cells displayed in A as calculated by recovering velocity dynamics using scvelo .
- Full pipeline: dimensionality reduction/clustering [ArchR, Seurat, UMAP] -> stage not stated [scVelo]

### Transition of signal requirement in hematopoietic stem cell development from hemogenic endothelial cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404193121 | PMCID: PMC11294991 | PMID: 39042698
- Evidence: For the velocity analysis, Seurat-generated UMAP was exported to a Jupyter Notebook, and the dynamical model of the scVelo package ( 44 , 45 ) was used to calculate the RNA velocity. scRNA-seq Analysis (E12.5).
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Jupyter, UMAP, scVelo] -> visualisation [Seurat]

### Dissection and integration of bursty transcriptional dynamics for complex systems. (PNAS 2024)

- DOI: 10.1073/pnas.2306901121 | PMCID: PMC11067469 | PMID: 38669186
- Evidence: In contrast to the ODE-based one-state model underlying scVelo , TopicVelo efficiently fits a more faithful physical model that accounts for transcriptional bursting ( Materials and Methods ), adapting a previous model for studying mRNA transport ( 27 ) ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Python, SciPy, scVelo]

### Pharmacological expansion of type 2 alveolar epithelial cells promotes regenerative lower airway repair. (PNAS 2024)

- DOI: 10.1073/pnas.2400077121 | PMCID: PMC11032444 | PMID: 38598345
- Evidence: RNA velocity–based trajectory inference was performed on the selected AECs from each group using the scVelo package (0.2.4, https://github.com/theislab/scvelo ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> stage not stated [Scanpy, scDblFinder]

### Expression of <i>Atoh1</i>, <i>Gfi1</i>, and <i>Pou4f3</i> in the mature cochlea reprograms nonsensory cells into hair cells. (PNAS 2024)

- DOI: 10.1073/pnas.2304680121 | PMCID: PMC10835112 | PMID: 38266052
- Evidence: (Scale bar in B , 50 µm and 20 µm.) We used scVelo to perform RNA-velocity analysis to investigate the probability of cells transitioning from one state to another ( 29 ).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> stage not stated [SCENIC, scVelo]

### Adipose-tissue regulatory T cells are a consortium of subtypes that evolves with age and diet. (PNAS 2024)

- DOI: 10.1073/pnas.2320602121 | PMCID: PMC10823167 | PMID: 38227656
- Evidence: RNA-velocity and CellRank analysis were done with the scvelo and cellrank packages ( 23 , 24 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Scanpy, scVelo]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: RNA velocity analysis was performed with Velocyto ( 38 ) and scVelo ( 39 ), which provided dynamic insights into cell state transitions based on spliced and unspliced mRNA ratios.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Version used: **0.3.1**
- Evidence: Pseudotime analysis and RNA velocity analysis were performed on the SP fraction using Monocle 3 v1.2.7 ( 67 ), kb-python v0.27.3 ( 68 ), and scVelo v0.3.1 ( 24 ).
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Clusters were annotated based on the expression of marker genes. velocyto, and R package, was used to create loom files for velocity analysis and scVelo was used for further downstream RNA velocity analysis ( 28 , 63 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Evidence: Data were analyzed using Seurat and scVelo.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### NEUROD1 efficiently converts peripheral blood cells into neurons with partial reprogramming by pluripotency factors. (PNAS 2025)

- DOI: 10.1073/pnas.2401387122 | PMCID: PMC12067290 | PMID: 40299704
- Evidence: Additionally, RNA velocity analysis using scVelo showed a gap between iPSC area (green cluster) and NSC area (blue cluster), with few connections.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP, scVelo] -> simulation/modelling [Monocle, UMAP]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: ( A ) UMAP with streamline RNA velocity calculated by scVelo.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### Radiation-induced cellular plasticity primes glioblastoma for forskolin-mediated differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2415557122 | PMCID: PMC11892679 | PMID: 40009641
- Evidence: Next, we used scVelo’s dynamical model to compute cell trajectories based on RNA expression and splicing information by calculating RNA velocities, dynamical genes, and latent time ( 31 ) for the three different treatments and the control sample cells that were used as starting point.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Evidence: RNA velocity ( 63 ) was performed using the Velocyto package, with scVelo using the steady-state model (stochastic option).
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### Diffusive topology preserving manifold distances for single-cell data analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2404860121 | PMCID: PMC11789025 | PMID: 39854240
- Evidence: Summary of single-cell datasets used in this study Datasets Number of cells Download link Paul 2,730 “scanpy.datasets.paul15()” Nestorowa 1,656 https://github.com/theislab/paga/blob/master/blood/nestorowa16/nestorowa16.ipynb Pancreas 3,696 https://scvelo.readthedocs.io/en/stable/scvelo.datasets.pancreas/ Lymphoid 8,221 https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129785 Embryoid Body 16,8...
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> visualisation [UMAP] -> stage not stated [Monocle, Scanpy, scVelo]

### Bacterial reporter-paired scRNA sequencing reveals cross talk between zinc starvation and zinc toxicity in macrophage antibacterial defense. (PNAS 2026)

- DOI: 10.1073/pnas.2530503123 | PMCID: PMC12993976 | PMID: 41802048
- Version used: **0.2.4**
- Evidence: Violin plots were generated through Seurat function VlnPlot. mCherry and GFP correlation was performed in R v4.0.4 using Pearson correlation in function “cor.” RNA velocity analysis ( 21 ) was performed using velocyto v0.17 and scVelo v0.2.4 on Python v3.8.8 (Python Software Foundation, Oregon) for Seurat clusters.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, scVelo v0.2.4, velocyto v0.17] -> differential/statistical testing [R v4.0] -> stage not stated [Seurat v4.0.4, scDblFinder v1.4.0]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: First-order-kinetics matrices were imputed for each dataset using the pp.moments function (n_pcs=20, n_neighbours=30) in the scVelo package (v0.2.4).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

