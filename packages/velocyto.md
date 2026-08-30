# velocyto

- **Category:** single-cell
- **Papers in survey:** 46
- **Journals:** Nature (26), PNAS (10), Cell (9), Science (1)
- **Years:** 2021 (6), 2022 (9), 2023 (9), 2024 (11), 2025 (7), 2026 (4)
- **Versions named:** 0.17.17 (7), 0.17 (5), 0.17.16 (1), 0.6 (1)
- **Pipeline stages it appears in:** alignment/mapping (8), quantification (7), dimensionality reduction/clustering (5), simulation/modelling (5), normalisation (2), visualisation (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: Overlays were generated based on pre-computed single-cell observation vectors, such as a CytoTRACE score, or the normalized, transformed, and z-scored gene expression values. scRNA-seq, RNA velocity RNA velocity analysis was performed using velocyto CLI version 0.17 ( La Manno et al., 2018 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Evidence: For analysis of RNA velocity, we also recovered both exonic and intronic alignment information using DropEst (Cumulus ( https://cumulus.readthedocs.io/en/latest/drop_seq.html , snapshot 9, dropest_velocyto true, run_dropest true) ( Petukhov et al., 2018 ).
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: R packages velocyto.R ( La Manno et al., 2018 ) and SeuratWrappers were then used to estimate RNA velocity vectors using batch-corrected harmony dimensionality reduction, with velocity parameters kCells = 25, fit.quantile = 0.2 and deltaT = 1 and visualization parameters n = 200, grid.n = 40, arrow.scale = 3, min.grid.cell.mass = 0.5 and scale = ”sqrt.” Trajectories on compartment embeddings were ...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: The preprocessed dataset was merged with spliced and unspliced read counts computed with velocyto, before using scvelo.pp.moments, scvelo.tl.velocity and scvelo.tl.velocity_graph to compute velocities using the stochastic mode in scvelo.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Reads were aligned to the genome using STARsolo (STAR version 2.7.9a) with the flags ‘ –outSAMattributes NH HI AS nM CR CY UR UY –soloFeatures Gene GeneFull SJ Velocyto –readFiles Command zcat –outFilterMultimapNmax 100 –winAnchorMultimapNmax 100 –outMultimapperOrder Random –runRNGseed 777 –outSAMmultNmax 1’ to allow multimapping.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...s://github.com/FelixKrueger/TrimGalore ttest2 MATLAB https://uk.mathworks.com/help/stats/ttest2.heml UMAP McInnes, Healy, Melville arXiv:1802.03426v2 Velocyto ( La Manno et al., 2018 ) http://velocyto.org/ Vireo ( Huang et al., 2019 ) v0.4.0 https://huangyh09.github.io/vireo-manual/about.html WGCNA ( Langfelder and Horvath, 2008 ) https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackage...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Version used: **0.17.17**
- Evidence: Spliced and unspliced matrices for RNA-velocity 43 analysis were computed using the velocyto (0.17.17) pipeline.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 55 https://github.com/alexdobin/STAR Velocyto La Manno et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Serotonin transporter inhibits antitumor immunity through regulating the intratumoral serotonin axis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.032 | PMCID: PMC12255530 | PMID: 40403728
- Evidence: Further analysis was conducted using the Velocyto.R-package (v.0.6).
- Full pipeline: quantification [R, Seurat v4.0.0] -> dimensionality reduction/clustering [GSEA, R, Seurat v4.0.0, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2, velocyto]

### Transcriptional programs of neoantigen-specific TIL in anti-PD-1-treated lung cancers. (Nature 2021)

- DOI: 10.1038/s41586-021-03752-4 | PMCID: PMC8338555 | PMID: 34290408
- Evidence: RNA velocity-based differentiation-trajectory tracing The RNA velocity analysis was performed by first recounting the spliced reads and unspliced reads based on aligned bam files of scRNA-seq data using the velocyto Python package.
- Full pipeline: alignment/mapping [velocyto] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [velocyto] -> structure determination [UMAP] -> visualisation [pheatmap]

### NASH limits anti-tumour surveillance in immunotherapy-treated HCC. (Nature 2021)

- DOI: 10.1038/s41586-021-03362-0 | PMCID: PMC8046670 | PMID: 33762733
- Version used: **0.6**
- Evidence: Velocity and correlation analyses of scRNA-seq data Velocyto (0.6) was used to estimate the spliced and unspliced counts from the pre-aligned bam files 42 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [velocyto v0.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2 v1.28.1] -> stage not stated [R v3.4, scVelo v0.2.2]

### The neurons that restore walking after paralysis. (Nature 2022)

- DOI: 10.1038/s41586-022-05385-7 | PMCID: PMC9668750 | PMID: 36352232
- Evidence: Read alignment Reads were aligned to the most recent Ensembl release (GRCm38.93) using Cell Ranger, and a matrix of UMI counts, including both intronic and exonic reads, was obtained using velocyto 75 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat, velocyto] -> normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.3, fgsea] -> simulation/modelling [Python v2.7] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **0.17.17**
- Evidence: Dynamical modelling of RNA velocity for the multiome scRNA-seq data The unspliced and spliced mRNAs for the scRNA-seq profiles of the multiome data were counted by Velocyto v0.17.17 32 from the position-sorted BAM file containing GEX read alignments, outputted by Cell Ranger ARC in pre-processing.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Evidence: For the RNA velocity analysis, annotated spliced, unspliced and spanning reads in the measured cells were generated in a single loom file using the command line ‘velocyto run_smartseq2 -d 1’ function.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### Single-cell delineation of lineage and genetic identity in the mouse brain. (Nature 2022)

- DOI: 10.1038/s41586-021-04237-0 | PMCID: PMC8770128 | PMID: 34912118
- Evidence: RNA velocity was estimated using the R library velocyto.R 36 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [R v3.6.0, Seurat, scDblFinder v2.0.3, velocyto]

### Evolution of neuronal cell classes and types in the vertebrate retina. (Nature 2023)

- DOI: 10.1038/s41586-023-06638-9 | PMCID: PMC10719112 | PMID: 38092908
- Evidence: To include both exonic and intronic reads in the quantification of gene expression for each sample, regardless of cellular or nuclear origin, we applied velocyto 61 to the corresponding.bam files.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat v4.3.0, ggplot2 v3.4.2] -> visualisation [Seurat v4.3.0, UMAP, ggplot2 v3.4.2]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **0.17**
- Evidence: For the analysis of RNA velocity, spliced and unspliced mRNA count matrices were constructed by using velocyto v.0.17 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: RNA velocity analyses Spliced and unspliced reads were counted from Cell Ranger BAM files for each snCv3 run using velocyto 97 (v.0.17.17) and using the GRCh38 gene annotations prepackaged with the Cell Ranger pipeline.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### CD4<sup>+</sup> T cell-induced inflammatory cell death controls immune-evasive tumours. (Nature 2023)

- DOI: 10.1038/s41586-023-06199-x | PMCID: PMC10307640 | PMID: 37316667
- Evidence: RNA velocity For RNA velocity, count matrices of spliced and unspliced RNA abundances were generated using the velocyto workflow for 10X chromium samples, with the genome annotation file supplied by 10X Genomics for the mm10 genome and a repeat annotation file retrieved from the UCSC genome browser.
- Full pipeline: quantification [velocyto] -> normalisation [AnnData, Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [ImageJ v1.52i, R, scVelo]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: (i) Data preprocessing For simulation of cell identity, we developed our code by modifying Velocyto.py, a Python package for RNA-velocity analysis ( https://velocyto.org ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: RNA velocity and cell fate probabilities Loom files were generated with velocyto 48 and dynamical velocities were computed with scvelo 20 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: Options ‘--soloFeatures Gene GeneFull Velocyto’ were used to generate both exon-only and full-length (pre-mRNA) gene counts, as well as RNA velocity output matrices.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Version used: **0.17.17**
- Evidence: Spliced and unspliced read counts were computed with velocyto (v0.17.17) from the unprocessed data, before using scvelo.pp.moments, scvelo.tl.velocity and scvelo.tl.velocity_graph to compute velocities for the preprocessed droplets. cytoTRACE 93 was used (through the CellRank 94 (v2.0.2) implementation) to obtain another prediction of directionality, independent of RNA velocity (based on the assum...
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: The option “--soloFeatures Gene GeneFull Velocyto” was used to generate both exon-only and full length (pre-mRNA) gene counts, as well as RNA velocity output matrices.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Evidence: RNA velocity analysis was performed by counting spliced and unspliced transcripts in Cell Ranger binary alignment map output files with the velocyto package 31 using the same transcriptome reference gene transfer format file (refdata-gex-GRCh38-2020-A) that was used for the initial Cell Ranger run.
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Acquisition of epithelial plasticity in human chronic liver disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07465-2 | PMCID: PMC11153150 | PMID: 38778114
- Version used: **0.17.17**
- Evidence: RNA velocity Velocyto (v.0.17.17), and velocyto.R (v.0.6) were used to estimate RNA velocity on the basis of the prevalence of spliced and unspliced mRNA 71 .
- Full pipeline: quality control [Seurat v4.0.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [velocyto v0.17.17]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Version used: **0.17.16**
- Evidence: To perform trajectory analysis, the un-spliced and spliced variant count matrix that was calculated using 10× pipeline in velocyto (v0.17.16) was fused with an anndata object containing the UMAP information and cluster identities defined in Seurat analysis.
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: RNA velocity was estimated by distinguishing unspliced and spliced mRNAs using the velocyto package (v.0.17) ( https://velocyto.org/velocyto.py/ 54 ).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Version used: **0.17.17**
- Evidence: For the RNA velocity analysis 24 , loom files were generated using velocyto (v.0.17.17) on all quantified genes. scvelo (v.0.2.5) was used to perform the analysis (that is, filtering, normalization, computing first and second-order moments, and subsequently estimating velocity stochastically).
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Version used: **0.17.17**
- Evidence: For cell trajectory inference, spliced/unspliced reads were generated from Cell Ranger-aligned sequences using the velocyto (v.0.17.17) run10x pipeline 59 .
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Version used: **0.17**
- Evidence: Cell lineage tracing analysis Velocyto (v.0.17) 74 was used to generate the initial.loom file (a format to store the scRNA-seq data for each stage) from the 10X Genomics multiomic output files produced via Cell Ranger.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Version used: **0.17**
- Evidence: Loom files containing the splicing annotation were created for each sample using the velocyto run command from the package velocyto (0.17,17) with default parameters and with no masked intervals.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: The velocyto 121 pipeline was implemented to quantify spliced and unspliced reads from CellRanger output.
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Velocyto Estimates of RNA velocities were calculated for each sample using velocyto 89 v.0.17.17, and combined for each dataset using loompy v.2.0.10.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **0.17.17**
- Evidence: Velocyto analysis The analysis of expression dynamics in scRNA-seq data was performed using velocyto (v.0.17.17) 24 , a package that allows estimating RNA velocities distinguishing between spliced and unspliced mRNAs in standard scRNA-seq protocols.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Computing the Riemannian curvature of image patch and single-cell RNA sequencing data manifolds using extrinsic differential geometry. (PNAS 2021)

- DOI: 10.1073/pnas.2100473118 | PMCID: PMC8307776 | PMID: 34272279
- Evidence: A Python notebook with the dentate gyrus dataset ( 57 ) can be retrieved at https://github.com/velocyto-team/velocyto-notebooks/blob/master/python/DentateGyrus.ipynb .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [velocyto]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Version used: **0.17**
- Evidence: BAM files from HISAT2 were also passed to Velocyto (v0.17) ( 27 ) in order to get spliced and unspliced expression matrices for further downstream analysis. scRNAseq data analysis.
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### Neutrophil and natural killer cell imbalances prevent muscle stem cell-mediated regeneration following murine volumetric muscle loss. (PNAS 2022)

- DOI: 10.1073/pnas.2111445119 | PMCID: PMC9169656 | PMID: 35377804
- Evidence: Loom files were generated using velocyto ( 94 ).
- Full pipeline: dimensionality reduction/clustering [UMAP, scVelo] -> simulation/modelling [scVelo] -> visualisation [ggplot2] -> stage not stated [ImageJ, Seurat, velocyto]

### Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus. (PNAS 2023)

- DOI: 10.1073/pnas.2310163120 | PMCID: PMC10515167 | PMID: 37703282
- Evidence: RNA velocity of single-nucleus transcriptome was evaluated by velocyto package.
- Full pipeline: quality control [R, Seurat v4.1.0] -> alignment/mapping [STAR] -> normalisation [R, Seurat v4.1.0] -> dimensionality reduction/clustering [R, Seurat v4.1.0, UMAP, clusterProfiler] -> stage not stated [Monocle, velocyto]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Evidence: RNAVelocity estimates were obtained using the Velocyto R package ( 49 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: Quantification of nascent (unspliced) and mature (spliced) mRNA levels was performed using the velocyto run10x function from python library velocyto.py (version 0.17.17).
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: RNA velocity analysis was performed with Velocyto ( 38 ) and scVelo ( 39 ), which provided dynamic insights into cell state transitions based on spliced and unspliced mRNA ratios.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Clusters were annotated based on the expression of marker genes. velocyto, and R package, was used to create loom files for velocity analysis and scVelo was used for further downstream RNA velocity analysis ( 28 , 63 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Evidence: RNA velocity ( 63 ) was performed using the Velocyto package, with scVelo using the steady-state model (stochastic option).
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### Bacterial reporter-paired scRNA sequencing reveals cross talk between zinc starvation and zinc toxicity in macrophage antibacterial defense. (PNAS 2026)

- DOI: 10.1073/pnas.2530503123 | PMCID: PMC12993976 | PMID: 41802048
- Version used: **0.17**
- Evidence: Violin plots were generated through Seurat function VlnPlot. mCherry and GFP correlation was performed in R v4.0.4 using Pearson correlation in function “cor.” RNA velocity analysis ( 21 ) was performed using velocyto v0.17 and scVelo v0.2.4 on Python v3.8.8 (Python Software Foundation, Oregon) for Seurat clusters.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, scVelo v0.2.4, velocyto v0.17] -> differential/statistical testing [R v4.0] -> stage not stated [Seurat v4.0.4, scDblFinder v1.4.0]

### Distinct myeloid-derived suppressor cell populations in human glioblastoma. (Science 2025)

- DOI: 10.1126/science.abm5214 | PMCID: PMC12836367 | PMID: 39818911
- Evidence: RNA velocity analysis RNA velocity analysis was performed as previously described using the velocyto.py.python package for annotating transcripts as spliced or unspliced, followed by the velocyto.R R package to perform velocity estimation.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R, SCENIC, velocyto]

