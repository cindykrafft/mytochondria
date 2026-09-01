# CellPhoneDB

- **Category:** single-cell
- **Papers in survey:** 46
- **Journals:** Nature (27), PNAS (14), Cell (3), Science (2)
- **Years:** 2021 (6), 2022 (10), 2023 (9), 2024 (11), 2025 (8), 2026 (2)
- **Versions named:** 2.0 (3), 4.0.0 (1), 3.0.0 (1), 2.0.0 (1), 2.1.1 (1), 2.1.2 (1)
- **Pipeline stages it appears in:** differential/statistical testing (7), normalisation (2), visualisation (1), quantification (1), dimensionality reduction/clustering (1)

## Papers

### Charting human development using a multi-endodermal organ atlas and organoid models. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.028 | PMCID: PMC8208823 | PMID: 34019796
- Version used: **2.0**
- Evidence: ...an/e1071 presto N/A https://github.com/immunogenomics/presto uwot N/A https://github.com/jlmelville/uwot RANN N/A https://github.com/jefferislab/RANN CellPhoneDB (version 2.0) Efremova et al., 2020 https://github.com/Teichlab/cellphonedb destiny Angerer et al., 2016 https://github.com/theislab/destiny splines N/A https://github.com/cran/splines Quadprog N/A https://github.com/cran/quadprog novoSpa...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB v2.0, R v3.6.0, SCENIC, Seurat v3.1, igraph]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 98 https://github.com/scikit-learn/scikit-learn CellPhoneDB(version: 2.1.7) Vento-Tormo et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Ligand receptor (LR) interactions For each bone ligand receptor interaction pairs between cell types were calculated with CellPhoneDB's 39 statistical analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Version used: **2.0**
- Evidence: Cell–cell communication analysis To infer cell–cell communication and screen for ligands and receptors involved we applied the CellPhoneDB v.2.0 Python package 80 , 81 on the normalized raw counts and fine cell-type annotations from the second trimester intestinal samples (12–17 PCW).
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Version used: **2.1.1**
- Evidence: CellphoneDB Analysis CellPhoneDB (v.2.1.1) was used to estimate cell-cell interactions among the cell types found in the human CD10- fraction using the version 2.0.0 of the database 76 , and the normalized gene expression as input, with default parameters (10% of cells expressing the ligand/receptor).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: Cell–cell communication analysis Cell annotation information and raw count expression matrix were exported from the Seurat file with suggested scripts using the CellPhoneDB protocol 64 , 65 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Evidence: We focused on the CellPhoneDB 91 ligand–receptor method with Omnipath’s ligand–receptor database 92 implemented in LIANA 90 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: CellPhoneDB and CellSign We updated the CellphoneDB database to include: (1) extra manually curated protein cell–cell interactions ( n = 1,852 interactions) and (2) cell–cell interactions involving non-protein ligands such as steroid hormones and other small molecules ( n = 194).
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### A multidimensional coding architecture of the vagal interoceptive system. (Nature 2022)

- DOI: 10.1038/s41586-022-04515-5 | PMCID: PMC8967724 | PMID: 35296859
- Evidence: Cell–cell interactions between organ-innervating UPB + VSNs and indicated organ cell types (or duodenal enteric neuron subtypes) were then analysed using the CellPhoneDB 66 ( https://github.com/Teichlab/cellphonedb,v.2.0.0 ) Python package.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [R, Seurat, UMAP, pheatmap] -> stage not stated [CellPhoneDB, Fiji, ImageJ]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: The total mouse interaction database contains 1,885 interactions (1,261 from CellTalkDb, 917 from CellPhoneDB, 293 of which overlap).
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Evidence: CellPhoneDB neural–GPCR expansion module Using the HUGO Gene Nomenclature Committee (HGNC) 68 library of GPCRs as a master list (HGNC group 139), we used publicly available databases (UniProt, Reactome, IUPHAR and GPCRdb ( https://gpcrdb.org/ ) 69 ) to generate a set of GPCRs with known ligands.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Version used: **2.0**
- Evidence: CellPhoneDB analysis CellPhoneDB 2.0 was used with default settings to assess potential tissue signalling crosstalk 58 .
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: Cell–cell communication analysis with CellPhoneDB To retrieve interactions between invading trophoblast and other cell populations identified in our samples, we used the CellPhoneDB degs_analysis method 13 , 63 ( https://github.com/ventolab/CellphoneDB ) described in ref.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Evidence: Sertoli-germ cell communication analysis We identified ligand–receptor interactions underlying Sertoli-germ cell communications for human, macaque, mouse, opossum and chicken, respectively, using the CellPhoneDB 78 (v.2) approach and recommended parameter settings (parameters method statistical_analysis).
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Version used: **2.0.0**
- Evidence: Prediction of cell–cell interaction with CellPhoneDB Ligand–receptor interaction analysis was performed using the Python package CellPhoneDB (v.2.0.0, Python v.3.8.5) following instructions from the GitHub repository ( https://github.com/Teichlab/cellphonedb ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: Cell–cell interaction analysis Cell–cell interaction analysis was performed using LIANA+ (v1.0.4) 89 , CellChat (v1.1.1) 90 and CellPhoneDB v3 (statistical_method) 91 to determine cell–cell interactions occurring in the small intestine during Crohn’s disease.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Version used: **4.0.0**
- Evidence: Cell–cell interactions Ligand–receptor interactions were inferred using ‘cpdb_analysis_method.call’ in CellPhoneDB (v4.0.0).
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **3.0.0**
- Evidence: Cell–cell interaction analysis CellPhoneDB (v.3.0.0) package 100 was used to infer cell–cell interactions within the prenatal skin scRNA-seq dataset overall and in early/late gestation and within the SkO scRNA-seq dataset overall.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: Ligand–receptor analysis using CellPhoneDB We inferred statistically significant ligand–receptors and their corresponding cell types using CellPhoneDB on a subsampled Ts21 liver dataset, such that the proportion of cells in the reduced sample recapitulated the proportion in the full Ts21 dataset and corresponded to the number of cells in the disomic dataset.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: This set of genes was then parsed with CellPhoneDB (v.3) 66 , CellTalkDB 67 and NicheNet 65 to filter for ligand and receptors and compile a list of their known interactors.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: The methods included were CellPhoneDB 108 , NATMI 109 and SingleCellSignalR 110 . liana_aggregate() with the argument ‘aggregate_how’ set to ‘magnitude’ was run to find consensus ranks of different methods.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: Cell–cell communication analysis The CellPhoneDB 55 , 56 Python package (v.3 .0) was used to infer putative cell–cell interactions.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: Cell–cell communication analysis of human scRNA-seq data Cell–cell communication analysis was performed using CellPhoneDB.org (v.2.1.4) for each dataset at the same stage of development 89 , 90 .
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Macrophage-fibroblast ligand–receptor interactions were interrogated and visualized using CellPhoneDB (version 4, statistical method; experiment 1) 107 .
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: Chemokine ligand and receptor expression analysis A list of human chemokine receptors was compiled from the literature 79 , 80 and their cognate ligands were obtained from CellPhoneDB 81 (Supplementary Table 7 ).
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: Cell–cell communication analysis To disentangle complex cellular crosstalk within and across CMs, we performed ligand–receptor-mediated cell–cell communication analysis using single-cell data with the CellPhoneDB Python package 11 , 27 .
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: CellPhoneDB analysis After identifying cell types in each dataset as described above, we used CellPhoneDB 83 in the most recent v.5 version to identify ligand–receptor interactions in n = 6 healthy livers from our human snRNA-seq dataset ( GSE256398 ).
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: Statistical analyses using CellPhoneDB 30 did not predict strong interactions between GZMK + CD8 + T cells and T H 2 cells (Supplementary Fig.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: Ligand–receptor interactions To identify microenvironment-specific cell–cell communication signals, we performed the statistical ligand–receptor interaction analysis using CellPhoneDB v5 (ref.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: We used the Squidpy 74 integration of CellPhoneDB 75 and Omnipath 76 to identify shifts in receptor–ligand interactions at each time point.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### High-dimensional profiling reveals phenotypic heterogeneity and disease-specific alterations of granulocytes in COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2109123118 | PMCID: PMC8501786 | PMID: 34548411
- Evidence: ( F ) Number of significant interactions between neutrophil subsets and other circulating immune cells from mild ( Top ) and severe ( Bottom ) COVID-19 patients as determined by applying the CellPhoneDB algorithm on a publicly available scRNAseq dataset ( 19 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB]

### Single-cell sequencing reveals suppressive transcriptional programs regulated by MIS/AMH in neonatal ovaries. (PNAS 2021)

- DOI: 10.1073/pnas.2100920118 | PMCID: PMC8157966 | PMID: 33980714
- Evidence: CellPhoneDB Analysis.
- Full pipeline: read trimming [R, Seurat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [CellPhoneDB, CellProfiler]

### A single-cell resolution developmental atlas of hematopoietic stem and progenitor cell expansion in zebrafish. (PNAS 2021)

- DOI: 10.1073/pnas.2015748118 | PMCID: PMC8040670 | PMID: 33785593
- Evidence: To further explore the dynamic cell communication network governing HSPC development, we performed unbiased ligand–receptor analysis of CHT HSPCs and niche cells, including vascular ECs, fibroblasts, neural cells, and epidermal cells using CellPhoneDB ( SI Appendix , Fig.
- Full pipeline: quality control [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, ImageJ]

### Deterministic programming of human pluripotent stem cells into microglia facilitates studying their role in health and disease. (PNAS 2022)

- DOI: 10.1073/pnas.2123476119 | PMCID: PMC9618131 | PMID: 36251998
- Evidence: To this aim, we performed a cell-communication analysis between the MGLs and neuroectoderm clusters using CellPhoneDB ( 39 ).
- Full pipeline: dimensionality reduction/clustering [CellPhoneDB, UMAP]

### Conservation at the uterine-placental interface. (PNAS 2022)

- DOI: 10.1073/pnas.2210633119 | PMCID: PMC9565169 | PMID: 36191208
- Evidence: To predict potential ligand–receptor interactions of invasive trophoblast cells with endothelial cells, macrophages, or NK cells, we used CellPhoneDB ( 47 ) with default settings.
- Full pipeline: quality control [R, Seurat v4.1.0] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v3.16.1] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, MACS2]

### A vasculature niche orchestrates stromal cell phenotype through PDGF signaling: Importance in human fibrotic disease. (PNAS 2022)

- DOI: 10.1073/pnas.2120336119 | PMCID: PMC9060460 | PMID: 35320046
- Evidence: For comprehensive systematic analysis of interlineage interactions, we used CellPhoneDB ( 39 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [CellPhoneDB, R, Seurat]

### Deciphering the endometrial niche of human thin endometrium at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2115912119 | PMCID: PMC8872762 | PMID: 35169075
- Evidence: To dissect out the complex interactions among different cell types, we inferred all potential intercellular communications by analyzing the expression of ligand–receptor pairs using CellPhoneDB ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB]

### Neighbor-specific gene expression revealed from physically interacting cells during mouse embryonic development. (PNAS 2023)

- DOI: 10.1073/pnas.2205371120 | PMCID: PMC9926237 | PMID: 36595695
- Evidence: We did not find the overlap between the genes identified by a ligand–receptor analysis using CellPhoneDB ( 17 ) and the contact-specific genes identified by PIC-seq ( SI Appendix , Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, Enrichr, scDblFinder]

### Paracrine FGF1 signaling directs pituitary architecture and size. (PNAS 2024)

- DOI: 10.1073/pnas.2410269121 | PMCID: PMC11459159 | PMID: 39320918
- Evidence: To identify Tpit-dependent genes involved in cell–cell interactions, we used CellPhoneDB, a software that identifies ligand–receptor pairs between different cell types present in scRNAseq data ( 44 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, Seurat]

### A spatiotemporal molecular atlas of the ovulating mouse ovary. (PNAS 2024)

- DOI: 10.1073/pnas.2317418121 | PMCID: PMC10835069 | PMID: 38252830
- Evidence: For oocytes and cumulus cells in preovulatory follicles, mean expression of annotated ligand–receptor interaction pairs from the Omnipath database was calculated at follicle resolution using the squidpy implementation of the method CellPhoneDB ( 62 ).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SCENIC, scikit-learn] -> visualisation [Squidpy] -> stage not stated [AnnData, CellPhoneDB, Scanpy]

### Multiscale spatial mapping of cell populations across anatomical sites in healthy human skin and basal cell carcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2313326120 | PMCID: PMC10786309 | PMID: 38165934
- Evidence: We also applied CellPhoneDB ( 37 ), a receptor–ligand interaction analytical tool; this revealed a high number of predicted interactions (>100) between RGS5+ and TAGLN+ pericytes and VEC ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellPhoneDB]

### Cellular cartography reveals mouse prostate organization and determinants of castration resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2427116122 | PMCID: PMC12415206 | PMID: 40854129
- Evidence: Analysis of ligand–receptor interactions by CellPhoneDB and CellChat ( 39 , 40 ) showed dramatic changes in epithelial cell–stromal cell communication after castration, suggesting that physiologically relevant, specific cell–cell interactions occur even while prostatic involution and widespread cell death occur.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB, GSVA, SCENIC]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: To further investigate the intercellular communications between LMICs and other cells in the TME, we performed CellPhoneDB ( 17 ) analysis to infer latent cell–cell interactions.
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### An atlas of early human mandibular endochondral and osteogenic paracrine signaling regions of Meckel's cartilage. (PNAS 2025)

- DOI: 10.1073/pnas.2420466122 | PMCID: PMC11962497 | PMID: 40096606
- Evidence: CellPhoneDB and CellChat were used to analyze cell–cell communication networks from the scRNA–seq data.
- Full pipeline: normalisation [Harmony v1.2.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib v3.7.2, UMAP] -> stage not stated [CellChat, CellPhoneDB, Seurat v4.0.0]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: Cell—cell interaction analysis We used the CellPhoneDB Python package (v.3.0) ( 92 , 93 ) to infer cell–cell interactions.
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Version used: **2.1.2**
- Evidence: Cell-cell interaction predictions using CellPhoneDB To assign putative cell–cell interactions within the YS scRNA-seq dataset, we used CellPhoneDB (v2.1.2).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

