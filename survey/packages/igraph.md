# igraph

- **Category:** general
- **Papers in survey:** 107
- **Journals:** PNAS (48), Nature (47), Cell (10), Science (2)
- **Years:** 2021 (13), 2022 (19), 2023 (18), 2024 (20), 2025 (28), 2026 (9)
- **Versions named:** 1.2.6 (7), 1.2.10 (2), 1.5.1 (2), 2.0.3 (2), 0.11.6 (1), 0.7.1 (1), 1.2.11 (1), 1.3.5 (1), 1.3.2 (1), 1.2.7 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (23), visualisation (18), differential/statistical testing (5), normalisation (3), alignment/mapping (3), simulation/modelling (2), variant calling (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Evidence: Clusters were identified using the SLM or Leiden algorithms with different resolution parameters using the Seurat function FindClusters (method = igraph) based on the nearest neighbor graph.
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### SARS-CoV-2 mRNA vaccination induces functionally diverse antibodies to NTD, RBD, and S2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.005 | PMCID: PMC8185186 | PMID: 34192529
- Version used: **1.2.6**
- Evidence: Clonotypes were assigned using igraph (v1.2.6) network analysis of components generated from CDR3 sequences greater than or equal to 0.85 normalized Levenshtein distance.
- Full pipeline: quantification [PyMOL] -> normalisation [igraph v1.2.6] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [PyMOL] -> visualisation [PyMOL, UMAP] -> stage not stated [R v4.0.2, Seurat v3.2.2]

### Charting human development using a multi-endodermal organ atlas and organoid models. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.028 | PMCID: PMC8208823 | PMID: 34019796
- Evidence: ...https://github.com/cran/splines Quadprog N/A https://github.com/cran/quadprog novoSpaRc Nitzan et al., 2019 https://github.com/rajewsky-lab/novosparc igraph N/A https://github.com/igraph/rigraph MNN Haghverdi et al., 2018 https://rdrr.io/github/LTLA/batchelor/ pySCENIC Aibar et al., 2017 https://github.com/aertslab/pySCENIC Other TSA Plus Cyanine 3 Akoya Biosciences Cat#NEL744001KT TSA Plus Cyanin...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB v2.0, R v3.6.0, SCENIC, Seurat v3.1, igraph]

### Maturation and persistence of the anti-SARS-CoV-2 memory B cell response. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.050 | PMCID: PMC7994111 | PMID: 33571429
- Version used: **1.2.6**
- Evidence: Phylogenetic trees were generated using the Immcantation/IgPhyML toolkit (Immcantation/suite v4.0.0 docker image) and further visualized in R using the Alakazam v1.0.2 and igraph v1.2.6 packages.
- Full pipeline: quality control [Seurat v3.2.2] -> alignment/mapping [R v4.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, igraph v1.2.6] -> stage not stated [Docker, ggplot2 v3.3.2]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **1.2.4.2**
- Evidence: ...roject.org/web/packages/pheatmap/index.html R package ggraph version 2.0.3 R CRAN https://cran.r-project.org/web/packages/ggraph/index.html R package igraph version 1.2.4.2 R CRAN https://cran.r-project.org/web/packages/igraph/index.html R package ggpubr version 0.2.5 R CRAN https://cran.r-project.org/web/packages/ggpubr/index.html R package ggrepel version 0.8.2 R CRAN https://cran.r-project.org/...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **1.2.6**
- Evidence: Graphics were generated using the ggplot2 3.3.3 ( Wickham, 2009 ), ComplexHeatmap 2.4.3 ( Gu et al., 2016 ), pheatmap 1.0.12 ( Kolde, 2019 ), igraph 1.2.6 ( Csardi and Nepusz, 2006 ), RCy3 2.8.1 ( Gustavsen et al., 2019 ), stringr 1.4.0 ( Wickham, 2019 ), dplyr 1.0.6 ( Wickham et al., 2020 ), and RColorBrewer 1.1-2 ( Neuwirth, 2014 ) R package.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Structural and functional characterizations of infectivity and immune evasion of SARS-CoV-2 Omicron. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.019 | PMCID: PMC8786603 | PMID: 35120603
- Version used: **1.2.5**
- Evidence: ...-32480 Omicron S-trimer at pH 5.5 This manuscript PDB ID 7WG7 , EMD-32479 Omicron S-trimer at pH 7.5 This manuscript PDB ID 7WG6 , EMD-32478 Software igraph (1.2.5) N/A https://cran.r-project.org/web/packages/ igraph/index.html Gctf program (v1.06) N/A https://www2.mrc-lmb.cam.ac.uk/download/gctf/ RELION (v3.07) Zivanov et al., 2018 https://www2.mrc-lmb.cam.ac.uk/relion UCSF Chimera N/A https://ww...
- Full pipeline: structure determination [Coot] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, RELION v3.07, UCSF Chimera, igraph v1.2.5]

### SARS-CoV-2 mRNA vaccination elicits a robust and persistent T follicular helper cell response in humans. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.026 | PMCID: PMC8695127 | PMID: 35026152
- Evidence: 0.9.6.3 https://github.com/markvanderloo/stringdist igraph R package v.
- Full pipeline: stage not stated [R, data.table, ggplot2, igraph]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Evidence: 122 Pairwise cell type similarities were visualized as heatmaps with the ComplexHeatmap 2.10.0 126 R library or (ii) as weighted using the igraph R package, 130 with nodes representing cell types and edge widths representing pairwise similarities, and using the Fruchterman and Reingold force-directed layout algorithm.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Louvain clustering was performed on this graph using the cluster_louvain function from the igraph package 58 , 59 with resolutions 0.5 or 1 depending on the annotation step.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Morphological diversity of single neurons in molecularly defined cell types. (Nature 2021)

- DOI: 10.1038/s41586-021-03941-1 | PMCID: PMC8494643 | PMID: 34616072
- Evidence: We then applied the Fast-greedy community detection algorithm using the Python package python-igraph for clustering assignment.
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [STAR v2.5.3] -> dimensionality reduction/clustering [R, UMAP, igraph]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **1.2.6**
- Evidence: The remaining independent components were used to determine clustering (Louvain community detection algorithm igraph v1.2.6 package in R); for each cluster, nearest neighbour and resolution parameters were set to optimize 1:1 mapping between each independent component and a cluster.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: For each superclone SNN graph, different k values were used (TN1=45, TN2=63, TN3 = 65, TN4 = 75, TN5 = 41, TN6=51, TN7 = 35, TN8 = 43, MDA-MB-231 = 93, MDA-EX1=55, MDA-EX2=17, BT-20 =55, MDA-MB-453=65, MDA-MB-157=75), the connected components of the SNN graph were identified using R package ‘igraph’ (v1.2.5) 41 and classified as superclones.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Cells were clustered on the graph using the Infomap graph clustering method 42 as implemented in the iGraph R package ( https://igraph.org ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: Network centrality calculations Counts of binarized interactions following integration of expression datasets with the interaction table were converted into a weighted undirected network graph using the igraph package in R (v.1.2.5).
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### Effective drug combinations in breast, colon and pancreatic cancer cells. (Nature 2022)

- DOI: 10.1038/s41586-022-04437-2 | PMCID: PMC8891012 | PMID: 35197630
- Evidence: Network overlays An interactome of binary, undirected interactions was built in the iGraph R package ( https://cran.r-project.org/web/packages/igraph/citation.html ) using the Reactome 18 human interactions file (accessed April 2021), and all human interactions reported in IntAct 12 (accessed July 2021).
- Full pipeline: stage not stated [ImageJ, R, igraph]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: Resulting force-directed graphs were rearranged using the Fruchterman–Reingold and Kamada–Kawai algorithms implemented in the igraph package and modified and visualized using ggraph.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Version used: **1.2.7**
- Evidence: We used the R package igraph v.1.2.7 to build the network from an incidence matrix of candidate ARGs and excitatory/inhibitory cell types localized to different regions.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: TAD cliques TAD cliques were computed using the igraph R package on an undirected graph representing DSB clustering.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Eigenvector centralities were then computed using igraph and the transcription-factor-to-gene network was visualized using PlotNetwork in chromfunks.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Recombination between heterologous human acrocentric chromosomes. (Nature 2023)

- DOI: 10.1038/s41586-023-05976-y | PMCID: PMC10172130 | PMID: 37165241
- Evidence: Finally, we used the net2communityes.py Python script (delivered in the PGGB repository) to apply the Leiden algorithm 56 , implemented in the igraph tools 59 , to detect the underlying communities in the mapping graph. python3 ~/pggb/scripts/net2communities.py \-e HPRCy1.1Mbps.edges.list.txt \-w HPRCy1.1Mbps.edges.weights.txt \-n HPRCy1.1Mbps.vertices.id2name.chr.txt --accurate-detection To ident...
- Full pipeline: alignment/mapping [Python, igraph] -> stage not stated [BEDTools, PLINK v1.9, R v3.6.3, ggplot2 v3.3.3, tidyverse v1.3.0]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: For these processes, CellOracle uses igraph ( https://igraph.org ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **1.2.6**
- Evidence: Strain–sharing networks Unsupervised networks based on shared strains and species were visualized with R packages ggraph (v2.0.5), igraph (v1.2.6) 127 , and tidygraph (v1.2.0) with stress layout, showing connections with ≥5 shared strains or ≥50 shared species (edges) among individuals (nodes).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: We then performed 10,000 random walks with 200 steps from each tip along edges backwards in pseudotime using the igraph R package (v.1.2.6) ( https://igraph.org/ ).
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Version used: **2.0.3**
- Evidence: TCR similarity networks were built using stringdist v0.9.12 and igraph v2.0.3 (ref.
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: The graph-based approach was implemented using the R package igraph 96 .
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: To evaluate the hierarchy of transcription factor networks, in ( I ) and out degrees ( O ) were computed for each transcription factor and their targets using the igraph R package v.2.0.2 ( https://igraph.org/ ) and hierarchy height ( H ).
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: We then generated a distance adjacency graph of TCRs from different T cells with a distance lower than the threshold, which was clustered to identify TCR clonotype groups using leiden 41 clustering through the igraph package 50 , at a resolution of 1 and using the RBConfigurationVertexPartition partition.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### Network of large pedigrees reveals social practices of Avar communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07312-4 | PMCID: PMC11078744 | PMID: 38658749
- Evidence: The analysis was performed using R and the node measurements were calculated using customized R scripts with the igraph package 95 .
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [BCFtools v1.3, Cytoscape v3.9.1, Picard, igraph]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **1.3.2**
- Evidence: Louvain clusters were identified using igraph (v.1.3.2) 62 at a resolution of 0.5.
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Evidence: We constructed a weighted network of the individuals using the igraph 104 package in R, with the fraction of the genome shared IBD between pairs of individuals as weights.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### Repeated Omicron exposures override ancestral SARS-CoV-2 immune imprinting. (Nature 2024)

- DOI: 10.1038/s41586-023-06753-7 | PMCID: PMC10764275 | PMID: 37993710
- Evidence: Then, a 12-nearest-neighbour graph is built using python-igraph module (v0.9.6).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy, igraph]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Version used: **1.2.6**
- Evidence: Batches were merged using batchelor (v1.6.3) and the batch-corrected dimension was used to build the shared nearest neighbour graph (scran v1.18.7), and batch integration was visually evaluated using igraph (v1.2.6).
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: To annotate HMBA cells that did not integrate with the homologous types, we found k = 10 nearest neighbours on the scVI latent space, and clustered using scanpy leiden (flavor = “igraph”, resolution = 1, n_iterations = 2), and we calculated the ‘experiment’ entropy for each cluster (scipy.stats.entropy; scipy v.1.11.2).
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Parent-of-origin effects on complex traits in up to 236,781 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-09357-5 | PMCID: PMC12527933 | PMID: 40770099
- Evidence: For individuals with more distant relatives (up to the fourth degree), we utilized a clustering approach to segregate relatives by parental sides using the igraph package in R 43 , as previously done 4 .
- Full pipeline: quality control [BCFtools v1.8] -> variant calling [PLINK v1.90b] -> dimensionality reduction/clustering [igraph] -> stage not stated [R, REGENIE v3.2.9]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **0.7.1**
- Evidence: ...g the following Python, R and Matlab packages: Python: pandas (v.1.1.5), numpy (v.1.19.3), anndata (v.0.7.4), scanpy (v.1.6.0), matplotlib (v.3.3.2), igraph (v.0.7.1), seaborn (v.0.9.0) and ‘louvain’ (v.0.6.1); R packages: ggplot2 (v.3.4.4), gplots (v.3.1.3), readr (v.2.1.4), dplyr (v.1.1.2), reshape2 (v.1.4.4), patchwork (v.1.1.3), RColorBrewer (v.1.1.3), ggrepel (v.0.9.4), aplot (v.0.1.10), ggde...
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **1.2.10**
- Evidence: ...b (1.30.1), IRanges (2.28.0), S4Vectors (0.32.3), BiocGenerics (0.40.0), MatrixGenerics (1.6.0), matrixStats (0.61.0), Rtsne (0.15), FlowSOM (2.2.0), igraph (1.2.10), flowCore (2.6.0), pheatmap (1.0.12), BiocManager (1.30.16), viridisLite (0.4.0) and ggplot2 (3.3.5). scRNA-seq analyses of 4T1 and MMTV-PyMT tumours We analysed the Gene Expression Omnibus (GEO) dataset GSE123366 for 4T1 ( GSM3502134...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Version used: **1.2.6**
- Evidence: We used the R package igraph (v1.2.6) to plot the GRN, showing transcription factor-to-target gene links and overlaying additional information such as whether the target gene is a DEG or PTSD GWAS gene.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: We used the igraph R package to visualize the CM networks, with nodes colour-coded by cell type and edge colour gradients scaled to reflect specificity.
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Evidence: Network characterization and analysis was performed using the igraph R package (RRID:SCR_021238; Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Cold memories control whole-body thermoregulatory responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08902-6 | PMCID: PMC12095059 | PMID: 40269165
- Evidence: Pearson’s correlations were computed in all cases after which networks were created using the igraph package.
- Full pipeline: stage not stated [igraph]

### Fine-scale patterns of SARS-CoV-2 spread from identical pathogen sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-08637-4 | PMCID: PMC11964829 | PMID: 40044856
- Evidence: For each node (postcode with a male state prison), we compute eigenvector centrality scores using the R igraph package.
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [Nextstrain, R, ape (R), igraph]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **1.2.11**
- Evidence: R package igraph (v.1.2.11 and v.2.0.3) 69 was used to construct a graph object and the community structure was determined using Louvain •clustering.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Version used: **1.2.10**
- Evidence: To identify clusters, we used graph-based community detection using the Louvain algorithm implemented by the functions buildSNNGraph and cluster_louvain of the package igraph (v.1.2.10).
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Version used: **1.5.1**
- Evidence: ..., CELLECT v.1.3.0, R v.4.3.1, future.apply v.1.11.1-9001, future v.1.33.1-9009, pbapply v.1.7-2, Matrix v.1.6-1.1, scUtils v.0.0.1, magrittr v.2.0.3, igraph v.1.5.1, treeio v.1.26.0, ggh4x v.0.2.6, scales v.1.2.1, edgeR v.4.0.16, limma v.3.58.1, ggtree v.3.10.1, lubridate v.1.9.3, forcats v.1.0.0, stringr v.1.5.0, dplyr v.1.1.3, purrr v.1.0.2, readr v.2.1.4, tidyr v.1.3.0, tibble v.3.2.1, ggplot2 ...
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: Positions were visualized using igraph.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Evidence: We loaded the tree given by MEDALT into R as an igraph object, visualized it using GGally::ggnet2() and calculated pairwise SD using igraph::distances(mode = ‘all’).
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Graph construction was performed with the RcppHNSW 57 package using the first 50 dimensions in harmony, k = 20 and cosine distance, followed by Louvain clustering using the igraph 58 package.
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Gut microbiome strain-sharing within isolated village social networks. (Nature 2025)

- DOI: 10.1038/s41586-024-08222-1 | PMCID: PMC11666459 | PMID: 39567691
- Version used: **1.3.5**
- Evidence: Social network graphs were analysed and geodesic distances and centrality measures were calculated with igraph (v.1.3.5) 46 and plotted with the Fruchterman–Reingold algorithm.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> visualisation [igraph v1.3.5] -> stage not stated [MetaPhlAn, R, vegan v2.6]

### Evolving antibody response to SARS-CoV-2 antigenic shift from XBB to JN.1. (Nature 2025)

- DOI: 10.1038/s41586-024-08315-x | PMCID: PMC11754117 | PMID: 39510125
- Evidence: A k -nearest-neighbour graph was constructed using the python-igraph module (v.0.9.6), and Leiden clustering was applied to assign a cluster to each antibody 57 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, ggplot2 v3.3.3, igraph] -> differential/statistical testing [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: We then used the package ‘igraph’ (v.1.5.0.1) to convert the SCC matrix to an undirected weighted network by considering TME cell states and metaprograms as nodes and SCC scores as edge widths.
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Evidence: For each tissue, a k -nearest neighbour ( k -NN) graph ( k = 5) was constructed using the get.knn function from the FNN package (v.1.1.4.1) 66 and subsequently converted into a graph object with graph_from_edgelist from the igraph package (v.2.1.4) 67 .
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: The igraph package was used to plot a directed and weighted network graph on the adjacency matrix, with edge thickness representing the sum total interaction score.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: Finally, to investigate spatial relationships between spots, we constructed a graph using the igraph::graph() function (v.2.1.4) on the basis of a distance matrix computed from spot coordinates (stats::dist()).
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Version used: **0.11.6**
- Evidence: Statistics on the network were calculated using igraph (v0.11.6) 100 .
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Analysis focused on highly interconnected genes and metabolites within the KEGG glutathione metabolism pathway modules (glutathione biosynthesis and ferroptosis protection), obtained using the MetaboSignal package (v.1.32.1) and the cluster_walktrap algorithm from the igraph package (v.2.0.2).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Defective cytokinin signaling reprograms lipid and flavonoid gene-to-metabolite networks to mitigate high salinity in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2105021118 | PMCID: PMC8640937 | PMID: 34815339
- Evidence: A subnetwork of DEGs in a [( ahp2,3,5 -C + arr1,10,12 -C + ahp2,3,5 -S + arr1,10,12 -S)/4 − (WT-C + WT-S)/2] comparison was then obtained using igraph ( https://igraph.org ) and plotted using Cytoscape ( 99 ).
- Full pipeline: alignment/mapping [clusterProfiler] -> variant calling [ggplot2] -> dimensionality reduction/clustering [R v3.5, clusterProfiler] -> visualisation [Cytoscape, igraph]

### In-cell structures of conserved supramolecular protein arrays at the mitochondria-cytoskeleton interface in mammalian sperm. (PNAS 2021)

- DOI: 10.1073/pnas.2110996118 | PMCID: PMC8609336 | PMID: 34737233
- Evidence: The interaction map for VDAC proteins was generated in R ( 95 ) using the igraph package (version 1.2.4.2).
- Full pipeline: structure determination [ChimeraX, IMOD] -> visualisation [IMOD] -> stage not stated [R, igraph]

### Live imaging of remyelination in the adult mouse corpus callosum. (PNAS 2021)

- DOI: 10.1073/pnas.2025795118 | PMCID: PMC8285919 | PMID: 34244440
- Evidence: Assembling of lineage trees was performed using R software using a custom-made script, and an igraph package was used for trees visualization.
- Full pipeline: visualisation [igraph]

### Network hubs cease to be influential in the presence of low levels of advertising. (PNAS 2021)

- DOI: 10.1073/pnas.2013391118 | PMCID: PMC7896329 | PMID: 33579818
- Evidence: 1 ) and small world networks generated in igraph ( 27 ) as well as the giant components of the Democratic National Committee email network (548 nodes and 2,442 edges), Enron email network (33,696 nodes and 180,811 edges), and a network of retweets and mentions on Twitter (532,325 nodes and 694,606 edges).
- Full pipeline: stage not stated [igraph]

### Calculation of centralities in protein kinase A. (PNAS 2022)

- DOI: 10.1073/pnas.2215420119 | PMCID: PMC9704751 | PMID: 36375071
- Evidence: Normalized centralities were calculated using igraph R library (version 1.2.5) ( 96 ).
- Full pipeline: normalisation [igraph] -> stage not stated [R]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Evidence: We performed this step with the distances() function from the igraph package ( 100 ), using the reciprocal of the edge scores assigned by vConTACT2 as edge weights.
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### Rats and the city: Implications of urbanization on zoonotic disease risk in Southeast Asia. (PNAS 2022)

- DOI: 10.1073/pnas.2112341119 | PMCID: PMC9522346 | PMID: 36122224
- Evidence: Bipartite networks were constructed to examine the interactions between 1) ticks and rodents and 2) microbes and rodents, at each of the three locations across the urban–rural gradient using the R packages bipartite v2.03 and igraph ( 64 , 65 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8] -> stage not stated [QGIS v3.2.3, R, igraph]

### Plant genetic effects on microbial hubs impact host fitness in repeated field trials. (PNAS 2022)

- DOI: 10.1073/pnas.2201285119 | PMCID: PMC9335298 | PMID: 35867817
- Evidence: The inferences of microbe–microbe ecological interactions inferred using SPIEC-EASI were passed to the igraph package ( 61 ), which was used for enforcing simplicity of graphs (no edges that connect vertices to themselves or duplicated edges), computing degree and betweenness centrality of vertices, computing distances between vertices, and plotting.
- Full pipeline: read trimming [Cutadapt] -> quantification [Python] -> normalisation [Python] -> stage not stated [Prokka, R, SPAdes, igraph, lme4]

### Characterization of <i>Pan</i> social systems reveals in-group/out-group distinction and out-group tolerance in bonobos. (PNAS 2022)

- DOI: 10.1073/pnas.2201122119 | PMCID: PMC9245655 | PMID: 35727986
- Evidence: We used the “apcluster” package and function, and the cluster_louvain function of the “igraph” package ( 60 ), to assessed affinity propagation and modularity, respectively.
- Full pipeline: dimensionality reduction/clustering [igraph] -> stage not stated [R]

### Revealing the recent demographic history of Europe via haplotype sharing in the UK Biobank. (PNAS 2022)

- DOI: 10.1073/pnas.2119281119 | PMCID: PMC9233301 | PMID: 35696575
- Evidence: With the pbwt paint chunkcount coancestry matrix as the input, we constructed a network graph using the statistical computing language R ( 59 ) and the “igraph” ( 60 ) package.
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [ADMIXTURE, PLINK, R] -> differential/statistical testing [R, ggplot2, igraph]

### Revisiting the recombinant history of HIV-1 group M with dynamic network community detection. (PNAS 2022)

- DOI: 10.1073/pnas.2108815119 | PMCID: PMC9171507 | PMID: 35500121
- Evidence: We imported the resulting distance matrices into R to generate undirected graphs using the package igraph ( 39 ).
- Full pipeline: alignment/mapping [IQ-TREE v1.3.11.1, R] -> structure determination [IQ-TREE v1.3.11.1] -> stage not stated [Python, igraph]

### Phenotypic determinism and stochasticity in antibody repertoires of clonally expanded plasma cells. (PNAS 2022)

- DOI: 10.1073/pnas.2113766119 | PMCID: PMC9170022 | PMID: 35486691
- Evidence: Edges were drawn between nodes with an edit distance of three or less amino acid mutations and following networks were created by R package igraph.
- Full pipeline: visualisation [PyMOL v2.4.2] -> stage not stated [R, igraph]

### Animal soundscapes reveal key markers of Amazon forest degradation from fire and logging. (PNAS 2022)

- DOI: 10.1073/pnas.2102878119 | PMCID: PMC9170030 | PMID: 35471905
- Evidence: The network analyses were performed with the aid of the following packages in R: “igraph” ( 60 ), “vegan” ( 61 ), and “bipartite” ( 59 ).
- Full pipeline: stage not stated [R, emmeans, igraph]

### MoSBi: Automated signature mining for molecular stratification and subtyping. (PNAS 2022)

- DOI: 10.1073/pnas.2118210119 | PMCID: PMC9169782 | PMID: 35412913
- Evidence: Network visualizations of the MoSBi package are implemented in R using the “igraph” package.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [Cytoscape, Docker, R]

### A vasculature niche orchestrates stromal cell phenotype through PDGF signaling: Importance in human fibrotic disease. (PNAS 2022)

- DOI: 10.1073/pnas.2120336119 | PMCID: PMC9060460 | PMID: 35320046
- Evidence: Visualization was performed using the R packages ggplot2 and igraph ( 15 , 19 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [CellPhoneDB, R, Seurat]

### Engineered nanoparticles enable deep proteomics studies at scale by leveraging tunable nano-bio interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2106053119 | PMCID: PMC8931255 | PMID: 35275789
- Evidence: A pruned network was constructed filtering for coefficients with P value (Satterthwaite’s method) < 0.05 using R libraries (ggraph), (igraph), and (graphlayouts) with layout = “stress.” FDR was estimated using p.adjust() with the Benjamini–Hochberg method.
- Full pipeline: quantification [lme4] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [R, igraph, lme4] -> machine learning [lme4] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold]

### Ship traffic connects Antarctica's fragile coasts to worldwide ecosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2110303118 | PMCID: PMC8784123 | PMID: 35012982
- Evidence: Figures were created in R ( 86 ) using the packages “tidyverse” ( 87 ), “sf” ( 88 ), “tidygraph” ( 103 ), “ggraph” ( 107 ), “nngeo” ( 108 ), “raster” ( 109 ),“rnaturalearth” ( 106 ),“igraph” ( 101 ), “ggrepel” ( 110 ), and “cowplot” ( 89 ).
- Full pipeline: visualisation [igraph, tidyverse] -> stage not stated [R]

### Urbanization and edge effects interact to drive mutualism breakdown and the rise of unstable pathogenic communities in forest soil. (PNAS 2023)

- DOI: 10.1073/pnas.2307519120 | PMCID: PMC10483667 | PMID: 37643216
- Evidence: Networks were analyzed for measures of connectivity, overall topological structure, and taxon importance using the igraph package of R ( 94 ).
- Full pipeline: quality control [R] -> stage not stated [igraph, lme4, vegan]

### Climate change-induced stress disrupts ectomycorrhizal interaction networks at the boreal-temperate ecotone. (PNAS 2023)

- DOI: 10.1073/pnas.2221619120 | PMCID: PMC10450648 | PMID: 37579148
- Evidence: Bipartite network visualizations were generated using the LGL layout algorithm in ‘igraph’ package (version 1.2.6).
- Full pipeline: quantification [emmeans] -> differential/statistical testing [R v4.1.0] -> visualisation [igraph]

### Development potential of nanoenabled agriculture projected using machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2301885120 | PMCID: PMC10288598 | PMID: 37314934
- Evidence: The similarity matrix was obtained from the RF models through the Kamada–Kawai layout algorithm, and the “igraph” package in R 4.0.5 was used to draw the similarity network.
- Full pipeline: stage not stated [Keras, Python v3.8, R v4.0, TensorFlow, igraph, scikit-learn]

### Reductions in home-range size and social interactions among dehorned black rhinoceroses (<i>Diceros bicornis</i>). (PNAS 2023)

- DOI: 10.1073/pnas.2301727120 | PMCID: PMC10288626 | PMID: 37307460
- Evidence: Finally, we compiled area overlap data into a pairwise matrix and built an interaction network based on circular layout using the igraph package ( 56 ), which we used to derive changes to the number of edges (that is, the number of rhinos engaging in social interactions) and network connectivity/density (that is, density of social interactions) between horned and dehorned networks.
- Full pipeline: stage not stated [QGIS, igraph]

### Oceanographic connectivity explains the intra-specific diversity of mangrove forests at global scales. (PNAS 2023)

- DOI: 10.1073/pnas.2209637120 | PMCID: PMC10083552 | PMID: 36996109
- Evidence: All analyses were performed in R (R Development Core Team, 2018) using the R packages “bigmemory,” “data.table,” “dismo,” “doparallel,” “geosphere,” “gstat,” “igraph,” “raster,” and “vegan.” The source code for biophysical modeling is available in Supplementary Information 5 ( 60 ).
- Full pipeline: stage not stated [R, data.table, igraph]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Evidence: S17 ), using the igraph R package.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Estimating human mobility in Holocene Western Eurasia with large-scale ancient genomic data. (PNAS 2023)

- DOI: 10.1073/pnas.2218375120 | PMCID: PMC9992830 | PMID: 36821583
- Evidence: All data analysis and plotting was done in R ( 87 ) with the following packages: checkmate ( 88 ), cowplot ( 89 ), fractional ( 90 ), future ( 91 ), ggh4x ( 92 ), ggnewscale ( 93 ), ggpubr ( 94 ), ggrepel ( 95 ), ggridges ( 96 ), igraph ( 97 ), khroma ( 98 ), latex2exp ( 99 ), lemon ( 100 ), progress ( 101 ), rnaturalearth ( 102 ), sf ( 103 ), smartsnp ( 104 ), viridis ( 105 ), and, finally, the t...
- Full pipeline: quality control [ANGSD] -> stage not stated [R, ggpubr, igraph, tidyverse]

### Transcriptomic congruence analysis for evaluating model organisms. (PNAS 2023)

- DOI: 10.1073/pnas.2202584120 | PMCID: PMC9963430 | PMID: 36730203
- Evidence: ...h, where the unweighted graph is constructed using R packages “KEGGgraph” ( 38 ) and “xml2”, and the shortest path matrix is calculated by R package “igraph” ( 39 ).
- Full pipeline: normalisation [DESeq2] -> stage not stated [R, igraph]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: Figures were made using base R (R version 4.1.0) and the R packages ComplexHeatmap ( 130 ), igraph ( 131 ), eulerr ( 132 ), and ggplot2 ( 133 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: Networks were generated using the igraph package in R.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Module neighborhood statistics were analyzed and visualized using the “igraph” R package ( 71 ).
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Persistent species relationships characterize migrating bird communities across stopover sites and seasons. (PNAS 2024)

- DOI: 10.1073/pnas.2322063121 | PMCID: PMC11348330 | PMID: 39136989
- Evidence: Network analyses were performed with the asnipe ( 81 ) and igraph ( 82 ) packages in RStudio (Version 2022.07.1).
- Full pipeline: quantification [R] -> stage not stated [igraph]

### Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2303439121 | PMCID: PMC11317588 | PMID: 39093948
- Evidence: We used the igraph package ( 51 ) for correlation calculations, network construction, and topology analysis, and Cytoscape ( 52 ) for visualization.
- Full pipeline: quantification [ImageJ v2.0.0] -> dimensionality reduction/clustering [vegan] -> differential/statistical testing [DESeq2, R v3.6.0, phyloseq, vegan] -> visualisation [Cytoscape, R v3.6.0, igraph, phyloseq] -> stage not stated [DADA2]

### On the friendship paradox and inversity: A network property with applications to privacy-sensitive network interventions. (PNAS 2024)

- DOI: 10.1073/pnas.2306412121 | PMCID: PMC11287120 | PMID: 39028691
- Evidence: Simulation and empirical analysis was performed in R software, using igraph and sna packages.
- Full pipeline: simulation/modelling [igraph]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: From the qpWave distances, we formed an igraph object through the igraph package v.1.4.3 ( https://github.com/igraph ) and performed hierarchical clustering with pheatmap v.1.0.12 in R. f -Statistics.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### Estimating the reproduction number and transmission heterogeneity from the size distribution of clusters of identical pathogen sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2305299121 | PMCID: PMC11009662 | PMID: 38568971
- Evidence: The cluster generation was done using the R igraph package ( 52 ).
- Full pipeline: alignment/mapping [R, ape (R)] -> dimensionality reduction/clustering [igraph] -> stage not stated [Nextstrain]

### History constrains the evolution of efficient color naming, enabling historical inference. (PNAS 2024)

- DOI: 10.1073/pnas.2313603121 | PMCID: PMC10927505 | PMID: 38416682
- Evidence: ( 52 ), implemented in the R igraph package ( 53 ).
- Full pipeline: stage not stated [R, igraph]

### Variable expression of <i>MECP2, CDKL5,</i> and <i>FMR1</i> in the human brain: Implications for gene restorative therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2312757121 | PMCID: PMC10907246 | PMID: 38386709
- Evidence: Significant genes were displayed using igraph functionalities.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [igraph]

### Positive associations fuel soil biodiversity and ecological networks worldwide. (PNAS 2024)

- DOI: 10.1073/pnas.2308769121 | PMCID: PMC10861899 | PMID: 38285947
- Evidence: We first converted the adjacency matrices of each individual soil ecological network into the igraph format to calculate some representative topological indices using igraph and ggClusterNet packages in R v.4.1.0.
- Full pipeline: dimensionality reduction/clustering [igraph] -> stage not stated [QIIME 2, vegan]

### Viruses traverse the human proteome through peptide interfaces that can be biomimetically leveraged for drug discovery. (PNAS 2024)

- DOI: 10.1073/pnas.2308776121 | PMCID: PMC10835127 | PMID: 38252831
- Evidence: Network topology measures were computed with the igraph R package ( 47 ).
- Full pipeline: differential/statistical testing [R] -> visualisation [Cytoscape] -> stage not stated [igraph]

### Wild food portfolios: Access to diverse foods stabilizes harvest in wild food systems. (PNAS 2025)

- DOI: 10.1073/pnas.2525571122 | PMCID: PMC12772149 | PMID: 41452987
- Evidence: For presentation, we simplified harvest structures to display major resource groups (e.g., salmon, large land mammals, etc.) and used the network plotting R package igraph , where each “edge” (i.e., interaction between community and harvest resource group) was weighted by per capita harvest (for aesthetic purposes, edges in Fig.
- Full pipeline: quantification [vegan] -> stage not stated [R, igraph]

### Mating system of free-ranging domestic dogs and its consequences for dog evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2421756122 | PMCID: PMC12684915 | PMID: 41284864
- Version used: **2.0.3**
- Evidence: The final genealogy was drawn in R v.4.4.1 ( 73 ) as a network with the R package igraph v.2.0.3 ( 74 ).
- Full pipeline: stage not stated [R v4.4.1, igraph v2.0.3]

### Local and distal changes in dynamics are caused by an L205R Cushing's syndrome mutant in PRKACA. (PNAS 2025)

- DOI: 10.1073/pnas.2502898122 | PMCID: PMC12184650 | PMID: 40504162
- Evidence: ( 24 ) using igraph R library ( 55 , 56 ).
- Full pipeline: stage not stated [igraph]

### Independent transitions to fully planktonic life cycles shaped the global distribution of medusozoans in the epipelagic zone. (PNAS 2025)

- DOI: 10.1073/pnas.2415979122 | PMCID: PMC12146771 | PMID: 40440075
- Evidence: Interactome analysis was performed using the packages igraph [v2.0.3; ( 77 )] and ggraph [v2.2.1; ( 78 )].
- Full pipeline: alignment/mapping [BLAST, phytools] -> differential/statistical testing [tidyverse, vegan] -> stage not stated [R, igraph]

### Group traits moderate the relationship between individual social traits and fitness in gorillas. (PNAS 2025)

- DOI: 10.1073/pnas.2421539122 | PMCID: PMC12107160 | PMID: 40324072
- Evidence: Each individual’s eigenvector centrality was extracted from each of the 100 network draws in each network, using the igraph R package ( 88 ).
- Full pipeline: differential/statistical testing [R, brms] -> stage not stated [igraph]

### LACE-UP: An ensemble machine-learning method for health subtype classification on multidimensional binary data. (PNAS 2025)

- DOI: 10.1073/pnas.2423341122 | PMCID: PMC12054798 | PMID: 40267132
- Evidence: In this simulation, NMI is calculated using the implementation in the package igraph ( 67 ).
- Full pipeline: dimensionality reduction/clustering [Python, UMAP] -> simulation/modelling [igraph]

### Downscaling mutualistic networks from species to individuals reveals consistent interaction niches and roles within plant populations. (PNAS 2025)

- DOI: 10.1073/pnas.2402342122 | PMCID: PMC11848293 | PMID: 39937855
- Evidence: For both the individual and species-based networks, we calculated several network-level metrics, using R packages bipartite ( 126 ) and igraph ( 127 ).
- Full pipeline: stage not stated [R, igraph]

### Epistatic hotspots organize antibody fitness landscape and boost evolvability. (PNAS 2025)

- DOI: 10.1073/pnas.2413884122 | PMCID: PMC11745389 | PMID: 39773024
- Evidence: Specifically, we construct a network in which nodes represent genotypes and edges are drawn between mutational neighbors with a weight being inversely related to their fitness difference, w s s ′ = ( 0.001 + | F ( s ) − F ( s ′ ) | ) − 1 , and then apply the force-directed layout (using function layout_drl from Python’s igraph package).
- Full pipeline: variant calling [igraph] -> dimensionality reduction/clustering [scikit-learn]

### Increasing pesticide diversity impairs soil microbial functions. (PNAS 2025)

- DOI: 10.1073/pnas.2419917122 | PMCID: PMC11745395 | PMID: 39786931
- Evidence: Networks were developed in R (version 4.2.3) using the “Hmisc” and “igraph” packages with Spearman correlation (| r | ≥ 0.60; Benjamini–Hochberg adjusted P < 0.05) ( 97 , 98 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.2.3, eggNOG, igraph]

### Pareto optimality reveals an atlas of cellular archetypes. (PNAS 2026)

- DOI: 10.1073/pnas.2530194123 | PMCID: PMC12993957 | PMID: 41802062
- Version used: **1.5.1**
- Evidence: We then clustered (igraph v1.5.1) the specialist phenotypes according to the graph defined by this adjacency matrix, thereby aligning specialist phenotypes based on their shared genes.
- Full pipeline: alignment/mapping [igraph v1.5.1] -> dimensionality reduction/clustering [WGCNA, igraph v1.5.1] -> simulation/modelling [WGCNA] -> structure determination [WGCNA] -> stage not stated [R v0.0.0.9000, Scanpy v1.10.3]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Evidence: ...eighbors when the Mash distance was ≤0.1, and the resulting network was partitioned with the Fast-Greedy community-detection algorithm implemented in igraph ( 64 ), assigning every plasmid to a unique cluster.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### Deploying synthetic coevolution and machine learning to engineer protein-protein interactions. (Science 2023)

- DOI: 10.1126/science.adh1720 | PMCID: PMC10403280 | PMID: 37499032
- Evidence: Sequence Similarity Network, cluster graph and Specificity Similarity Network Sequence similarity networks and cluster graphs were created via the igraph software package ( 49 ).
- Full pipeline: dimensionality reduction/clustering [igraph] -> visualisation [scikit-learn v1.2.2] -> stage not stated [AlphaFold, MACS2, PyTorch, RoseTTAFold]

### Structural ontogeny of protein-protein interactions. (Science 2026)

- DOI: 10.1126/science.adx6931 | PMCID: PMC12904254 | PMID: 41678610
- Evidence: Sequence similarity networks and community maps were constructed using the igraph software package ( 70 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CCP4, MACS2, SciPy, igraph]

