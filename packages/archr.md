# ArchR

- **Category:** single-cell
- **Papers in survey:** 49
- **Journals:** Nature (28), PNAS (14), Cell (4), Science (3)
- **Years:** 2021 (4), 2022 (7), 2023 (7), 2024 (5), 2025 (18), 2026 (8)
- **Versions named:** 1.0.2 (7), 1.0.1 (6), 1.0.3 (1), 0.9.5 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (9), quality control (7), visualisation (3), differential/statistical testing (3), quantification (2), normalisation (1)

## Papers

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 102 https://github.com/wheaton5/souporcell ArchR (version: 1.0.1) Granja et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...CNU Barcode primer_S oligo sequence (5′ to 3′): TGTCCAGCACGCTTCAGGCT This paper N/A Software and algorithms ALDEx2 ( Fernandes et al., 2013 ) v1.18.0 ArchR ( Granja et al., 2021 ) v0.9.3 https://www.archrproject.com/ AUCell ( Aibar et al., 2017 ) v1.12.0 BBKNN ( Polański et al., 2020 ) https://github.com/Teichlab/bbknn BLAST ( Altschul et al., 1990 ) https://blast.ncbi.nlm.nih.gov/Blast.cgi CATALY...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: For downstream analyses of snATAC and snRNA data, including dimensionality reduction, clustering, peak calling and annotation, identification of cell-type-specific genes, and TF analysis, we utilized the Scanpy, Muon, and ArchR toolkits.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Design principles of cell-state-specific enhancers in hematopoiesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.017 | PMCID: PMC12173716 | PMID: 40345201
- Evidence: 39 37,082 Differentially accessible regions were identified with ArchR.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ArchR] -> machine learning [TensorFlow] -> stage not stated [R, ggplot2, kallisto, pheatmap]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: The two VTA snATAC-seq libraries were analysed using ArchR software (v.0.9.1) 79 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **1.0.1**
- Evidence: Arrow files were created from the scATAC-seq fragments using ArchR v1.0.1 54 , and doublets were identified and removed with default parameters.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Spatial profiling of chromatin accessibility in mouse and human tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05094-1 | PMCID: PMC9452302 | PMID: 35978191
- Evidence: The fragment file was read into ArchR as a tile matrix with a genome binning size of 5 kb, and pixels that were not on the tissue were removed on the basis of the metadata file generated in the previous step.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [Python, Seurat] -> stage not stated [ArchR, Snakemake]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Version used: **1.0.1**
- Evidence: Marker overlap and compositional stability comparison with ischaemic specimens from our atlas were performed as described previously. snATAC-seq data processing To control the data quality, the fragment files were used as input for the package ArchR (v1.0.1) 65 , and low-quality cells were filtered out based on transcription start site (TSS) enrichment (> 4) and the number of unique fragments (> 3...
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: To analyse the neonatal multiome snATAC data, we used ArchR 88 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: Quality control, dimensionality reduction and clustering of snATAC–seq data The snATAC fragments files were loaded into R (v.4.1.2) using the createArrowFiles function in ArchR 52 .
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **1.0.2**
- Evidence: For multiome ATAC data (10x Genomics), the data processed using CellRanger ARC were further analysed using ArchR (v.1.0.2) 58 .
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Spatial epigenome-transcriptome co-profiling of mammalian tissues. (Nature 2023)

- DOI: 10.1038/s41586-023-05795-1 | PMCID: PMC10076218 | PMID: 36922587
- Version used: **1.0.1**
- Evidence: In regard to ATAC/CUT&Tag spatial data visualization, the fragment file obtained from ATAC/CUT&Tag was read into ArchR v.1.0.1 (ref.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.2] -> visualisation [ArchR v1.0.1, Seurat v4.1] -> stage not stated [Monocle, Signac v1.8]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: For single-cell ATAC-seq, we applied ArchR 73 (v1.0.2) to process the outputs from CellRanger-ARC.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Version used: **1.0.1**
- Evidence: Subsequent analyses on RNA were performed using Seurat (v.3.2.3) 63 , and those on ATAC-seq were performed using ArchR (v.1.0.1) 64 .
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Evidence: The transcription start site enrichment score, number of fragments and doublet score for each nucleus were calculated using ArchR 71 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Evidence: Computational analyses of such data are uniquely enabled by the ability of Slide-tags to seamlessly leverage many existing single-cell computational workflows (for example, Seurat 21 , InferCNV 43 , ArchR 56 ).
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: For 10x Multiome snATAC-seq data, we used the default criteria implemented in ArchR (RRID: SCR_020982 ) 59 : the number of unique nuclear fragments ( n Frags > 1,000) and signal-to-background ratio (transcription start site (TSS) > 3).
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Evidence: The ArchR 95 package was used to load both ATAC and RNA data, incorporating the spatial domain information from SpatialGlue.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Version used: **1.0.2**
- Evidence: We performed scATAC-seq analysis on ArchR (v.1.0.2) 64 .
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Data preparation and analysis. scATAC–seq analysis was previously described using the R package ArchR 24 , 62 , 63 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Version used: **1.0.2**
- Evidence: The following packages were used: CellRanger v.6.0.1, singleCellTK v.2.8.0, Seurat v.4.3.0, scater v.1.24.0, harmony v.0.1.1, RColorBrewer v.1.1.3, ComplexHeatmap v.2.14.0, ArchR v.1.0.2, muscat v.1.12.1, readr v.2.1.4, ggplot2 v.3.4.2, ggsignif v.0.6.4, ggpubr v.0.6.0, magrittr v.2.0.3, scCoda v.0.1.9 Python package, celda v.1.19.1 and hdWGCNA v.0.4.5.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Evidence: A new ArchR gene annotation was generated using the Lawson gtf v.4.3.2 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Evidence: ATAC-seq fragment files were used as inputs to the ArchR 66 (v.1.0.2) analysis pipeline in R (v.4.3.2).
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: For quality control and filtering, using the outputs of CellRanger, we created Arrow files for each sample with cells filtered based on the quality control parameters filterTSS=4 and filterFrags=1000 in ArchR 63 (v1.0.2), an R package for analysing scATAC-seq data.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: To identify differentially enriched cis -regulatory elements per sample per annotation, peaks were first called on the merged snATAC-seq data using the ArchR R package 46 by first creating pseudobulk replicates using addGroupCoverages (minCells=2000, maxCells=5000, minReplicates=2, maxReplicates=5, groupBy=“Sample”, maxFragments=100 * 10^6) and calling reproducible peaks using addReproduciblePeakS...
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Differentially accessible peaks were identified using the getMarkerFeatures() function from the ArchR 89 package using a Wilcoxon rank sum test and accounting for bias introduced by TSSEnrichment and log 10 (nFrags).
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: In addition, we used ArchR ( https://www.archrproject.com/ ) 79 to calculate doublet scores for each single cell and removed those with the top 5% of doublet scores.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Version used: **1.0.1**
- Evidence: We adopted the R package ArchR v1.0.1 68 for the downstream analysis of the scATAC-seq data, following the developers’ default recommendations, unless otherwise indicated.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **1.0.2**
- Evidence: ATAC–seq peak calling, motif enrichment and chromVAR We used ArchR (v1.0.2) 102 to process filtered ATAC fragment files into ArchR projects per organ.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### Ontogeny and transcriptional regulation of Thetis cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10198-z | PMCID: PMC13171621 | PMID: 41634202
- Version used: **1.0.3**
- Evidence: Genome tracks were visualized using the plotBrowserTrack function in ArchR v.1.0.3 with peaks from the TC and ILC3/LTi clusters.
- Full pipeline: read trimming [Seurat v4.4.0] -> alignment/mapping [STAR v2.7.11a] -> dimensionality reduction/clustering [ArchR v1.0.3, Scanpy, UMAP] -> visualisation [ArchR v1.0.3, UMAP]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Using ArchR 92 v.1.0.2, the ArchR object shared by the original authors was subset to only include cell types of interest (VEC, VEC_02_03, LEC, arterial EC, endocardium and muLEC) and pseudo replicates and peak calling using MACS2 (ref.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Similar to RNA, we analysed each ATAC library independently until cell-type annotation to evaluate the quality of the subsequent integrations using the ArchR framework 93 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Integrated spatial multiomics reveals fibroblast fate during tissue repair. (PNAS 2021)

- DOI: 10.1073/pnas.2110025118 | PMCID: PMC8521719 | PMID: 34620713
- Evidence: We identified considerable heterogeneity in accessibility profiles among individual wound fibroblasts, which were clustered into six epigenomically distinct subgroups using the ArchR platform ( 18 ) ( SI Appendix , Figs.
- Full pipeline: dimensionality reduction/clustering [ArchR, UMAP]

### Trained innate immunity, long-lasting epigenetic modulation, and skewed myelopoiesis by heme. (PNAS 2021)

- DOI: 10.1073/pnas.2102698118 | PMCID: PMC8545490 | PMID: 34663697
- Version used: **0.9.5**
- Evidence: Motif enrichment and TF footprinting analyses and the aggregation of cells from each condition to create a bulk track per cluster for peak calling and visualization were carried out using ArchR (version 0.9.5) ( 39 ).
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [R] -> dimensionality reduction/clustering [ArchR v0.9.5, UMAP] -> differential/statistical testing [R] -> visualisation [ArchR v0.9.5] -> stage not stated [HOMER, MACS2, Seurat]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: Such matrices can be produced by tools like ArchR or Signac.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: The preprocessed fragments of all cells were input to ArchR (Version 0.9.4) ( 34 ) to create an ArchR object.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### A distinct human cell type expressing MHCII and RORγt with dual characteristics of dendritic cells and type 3 innate lymphoid cells. (PNAS 2023)

- DOI: 10.1073/pnas.2318710120 | PMCID: PMC10756205 | PMID: 38109523
- Evidence: Dimensionality reduction was computed using Latent Semantic Indexing (LSI), and the result was projected on a two-dimensional UMAP space using ArchR ( 26 ).
- Full pipeline: dimensionality reduction/clustering [ArchR, Seurat, UMAP] -> stage not stated [scVelo]

### Chromatin conformational changes at human satellite II contribute to the senescence phenotype in the tumor microenvironment. (PNAS 2023)

- DOI: 10.1073/pnas.2305046120 | PMCID: PMC10410700 | PMID: 37523559
- Version used: **1.0.2**
- Evidence: Following that, scATAC-seq analyses were performed using ArchR (v.1.0.2) ( 48 ) as reported previously ( 39 ) with slight modifications.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ArchR v1.0.2]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: For ATAC data analysis, fragment files were initially analyzed in ArchR ( 31 ) (v1.0.1) for quality control, retaining cells with at least 1,000 unique nuclear fragments, transcription start site (TSS) ratio of greater than 4, and only singlets (using a filterRatio parameter value of 1).
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase. (PNAS 2024)

- DOI: 10.1073/pnas.2423270121 | PMCID: PMC11670102 | PMID: 39689177
- Evidence: For the single-cell data, ArchR ( 50 ) (version 1.0.2) was employed to perform quality control (with TSS Enrichment > 4 and Number of Unique Fragments > 10), followed by LSI-based dimensionality reduction and clustering using UMAP embedding with default parameters.
- Full pipeline: quality control [ArchR, UMAP] -> read trimming [Bismark, Python, Trim Galore v0.6.10, Trimmomatic v0.39] -> alignment/mapping [Bismark, Trim Galore v0.6.10, Trimmomatic v0.39] -> dimensionality reduction/clustering [ArchR, UMAP]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: Then, two datasets were performed analysis by ArchR (Version 1.0.1) ( 72 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Unified molecular approach for spatial epigenome, transcriptome, and cell lineages. (PNAS 2025)

- DOI: 10.1073/pnas.2424070122 | PMCID: PMC12037033 | PMID: 40249782
- Evidence: For consistency with spatial ATAC-seq analysis, after initial quality control using Seurat, gene expression data were loaded into an ArchR GeneExpression matrix, and dimensionality reduction, clustering, and imputation were performed using ArchR.
- Full pipeline: quality control [ArchR, Seurat] -> read trimming [fastp] -> alignment/mapping [HISAT2, Seurat, fastp] -> quantification [ArchR] -> dimensionality reduction/clustering [ArchR] -> visualisation [ggplot2]

### Single cell-resolved cellular, transcriptional, and epigenetic changes in mouse T cell populations linked to age-associated immune decline. (PNAS 2025)

- DOI: 10.1073/pnas.2425992122 | PMCID: PMC12002302 | PMID: 40163732
- Version used: **1.0.1**
- Evidence: CD4+ and CD8+ T cell clusters were analyzed separately using ArchR v.1.0.1 ( 88 ).
- Full pipeline: quality control [Scanpy v1.4.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [ArchR v1.0.1, MACS2, Seurat, UMAP]

### pTDP-43 levels correlate with cell type-specific molecular alterations in the prefrontal cortex of &lt;i&gt;C9orf72&lt;/i&gt; ALS/FTD patients. (PNAS 2025)

- DOI: 10.1073/pnas.2419818122 | PMCID: PMC11892677 | PMID: 39999167
- Evidence: We obtained a total of 34,874 and 53,331 single-nucleus multiomes (snRNA-seq and snATAC-seq) from the Emory and Mayo cohorts, respectively, after quality control filtration using the ArchR multiome pipeline ( 9 ) and Seurat snRNA-seq guidelines ( 10 ) ( Methods and SI Appendix , Figs.
- Full pipeline: quality control [ArchR, Seurat, SoupX] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [WGCNA]

### Fasting primes small intestinal regeneration after damage via a microbiome-metabolite-chromatin axis. (PNAS 2026)

- DOI: 10.1073/pnas.2529215123 | PMCID: PMC13320697 | PMID: 42335240
- Version used: **1.0.2**
- Evidence: Single-cell ATAC-seq data were processed using ArchR (v1.0.2) pipeline ( 51 ) in R (v4.2.2) with the mm10 genome.
- Full pipeline: dimensionality reduction/clustering [MACS2 v2.2.9.1, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ArchR v1.0.2, GSEA, HOMER, R v1.0.2]

### Bridging unpaired single-cell multimodal data for integrative analyses with SuperMap. (PNAS 2026)

- DOI: 10.1073/pnas.2505182123 | PMCID: PMC12890892 | PMID: 41650244
- Evidence: Furthermore, we conducted motif enrichment analysis based on significant peaks linked to CCL4 using ArchR ( 47 ) with motif database CISBP(v2) ( 48 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [ArchR, Signac]

### Epigenetic plasticity cooperates with cell-cell interactions to direct pancreatic tumorigenesis. (Science 2023)

- DOI: 10.1126/science.add5327 | PMCID: PMC10316746 | PMID: 37167403
- Evidence: Computational analysis: scRNA-seq data were processed with SEQC ( 64 ), filtered with a custom pipeline ( 27 ), and log library size normalized. scATAC-seq data were processed with ArchR ( 65 ).
- Full pipeline: quality control [ArchR] -> normalisation [ArchR] -> visualisation [Python] -> stage not stated [GSEA]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: To quantify chromatin accessibility at the gene level, we adapted the gene scoring approach from ArchR ( 44 ) and implemented a custom calculateBulkGeneScores() function.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **1.0.2**
- Evidence: For chromatin accessibility analyses, we generated custom ArchR (v1.0.2) annotations based on Ensembl v92, only considering protein-coding genes, as we observed that the inclusion of non-coding genes led to reduced and more noisy gene score estimates.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

