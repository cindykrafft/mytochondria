# SCENIC

- **Category:** single-cell
- **Papers in survey:** 76
- **Journals:** Nature (39), PNAS (29), Cell (5), Science (3)
- **Years:** 2021 (5), 2022 (10), 2023 (17), 2024 (14), 2025 (21), 2026 (9)
- **Versions named:** 0.12.1 (2), 0.11.2 (2), 1.2.4 (2), 1.1.2 (2), 0.10.3 (1), 1.3.1 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (16), quantification (2), alignment/mapping (2), normalisation (1), quality control (1), visualisation (1), structure determination (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: Since transcription factor (TF)-defined regulon activities are considered to be a determinant of cell identity, we used SCENIC (single-cell regulatory network inference and clustering), which is a regulon-based, batch-robust feature extraction tool, to adjust for polyp-specific effects ( Aibar et al., 2017 ; Van de Sande et al., 2020 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Charting human development using a multi-endodermal organ atlas and organoid models. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.028 | PMCID: PMC8208823 | PMID: 34019796
- Evidence: ...ps://github.com/rajewsky-lab/novosparc igraph N/A https://github.com/igraph/rigraph MNN Haghverdi et al., 2018 https://rdrr.io/github/LTLA/batchelor/ pySCENIC Aibar et al., 2017 https://github.com/aertslab/pySCENIC Other TSA Plus Cyanine 3 Akoya Biosciences Cat#NEL744001KT TSA Plus Cyanine 5 Akoya Biosciences Cat#NEL745E001KT Corning® Matrigel® (GFR) Basement Membrane Matrix Corning Cat#354230 Cor...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB v2.0, R v3.6.0, SCENIC, Seurat v3.1, igraph]

### COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.053 | PMCID: PMC7857060 | PMID: 33657410
- Version used: **1.1.2**
- Evidence: ...eurat scanpy 1.4.6/1.5.1 Wolf et al., 2018 https://scanpy.readthedocs.io/en/latest/ CSOmap Ren et al., 2020 https://github.com/zhongguojie1998/CSOmap SCENIC 1.1.2-2 Aibar et al., 2017 https://github.com/aertslab/SCENIC Scrublet ( Wolock et al., 2019 ) https://github.com/AllonKleinLab/scrublet Resource availability Lead contact Further information and requests for resources and reagents should be d...
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [SCENIC v1.1.2, Scanpy v1.4.6, Seurat v2.3.0, kallisto, scDblFinder]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: .../html/MAST.html R package zinbwave version 1.10.1 R Bioconductor; Risso et al., 2018 http://bioconductor.org/packages/release/bioc/html/zinbwave.html SCENIC Github; Aibar et al., 2017 https://github.com/aertslab/SCENIC R package SeuratWrappers version 0.1.0 Github https://github.com/satijalab/seurat-wrappers R Package SingleCellSignalR version 1.0 R Bioconductor; Cabello-Aguilar et al., 2020 http:...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 93 https://github.com/theislab/scvelo Monocle 3 (version: 1.0.0) 68,88 https://github.com/cole-trapnell-lab/monocle3 pySCENIC (version: 0.11.2) 59,94 https://github.com/aertslab/pySCENIC ComplexHeatmap (version 2.6.2) Gu et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: TF analysis The pySCENIC analysis in Docker was carried out following three steps 63 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Medin co-aggregates with vascular amyloid-β in Alzheimer's disease. (Nature 2022)

- DOI: 10.1038/s41586-022-05440-3 | PMCID: PMC9712113 | PMID: 36385530
- Evidence: To examine the source of increased MFGE8 expression in patients with Alzheimer’s disease, we further interrogated the RNA-sequencing data by constructing gene regulatory networks using SCENIC 26 to identify genes that are co-regulated with MFGE8 .
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Fiji v2.3, ImageJ v2.3, SCENIC, WGCNA]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: This model was tested for all TFs in the SCENIC 86 mm10 database.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Brain-wide correspondence of neuronal epigenomics and distant projections. (Nature 2023)

- DOI: 10.1038/s41586-023-06823-w | PMCID: PMC10719087 | PMID: 38092919
- Evidence: 43 and the Guide to PHARMACOLOGY database ( https://www.guidetopharmacology.org/DATA/targets_and_families.csv ); neural projection development: Gene Ontology terms GO0031175 Neuron Projection Development and GO0050808 Synapse Organization; TFs: annotation from SCENIC+ (ref.
- Full pipeline: stage not stated [BEDTools, SCENIC, Seurat]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Evidence: SCENIC To evaluate the activity of transcription factor regulons in each cluster of SPNs from PONS- and MED-enriching dissections, we employed SCENIC 60 , 61 .
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: DMR motif scan and TF motif enrichment analysis We used an ensemble motif database from SCENIC+ (ref.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: Gene regulatory network analysis using SCENIC To infer gene regulatory networks, we used the SCENIC pipeline pySCENIC command line interface version (v.0.11.2) 35 .
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Version used: **1.2.4**
- Evidence: Transcription factor regulon analysis with SCENIC SCENIC version 1.2.4 (ref.
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **0.11.2**
- Evidence: Gene regulatory network The Scenic pipeline 74 , 75 was used (pySCENIC, v.0.11.2) to predict TFs and putative target genes regulated in P cells.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: SCENIC was used with default settings in R, and the AUC–regulon table used to generate a new assay in the Seurat object.
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: Transcriptional regulator scores were then computed following the SCENIC workflow 88 , 89 , using the pyscenic package v.0.11.2 as follows: the gene regulatory network was generated using the grn command, then the regulons (transcription factors and their target genes) were identified with using the ctx command using the motif list motifs-v9-nr.hgnc-m0.001-o0.0.tbl (downloaded from cisTarget datab...
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: Validation and benchmarking of CellOracle GRN inference To test whether CellOracle can correctly identify cell-type- or cell-state-specific GRN configurations, we benchmarked our new method against diverse GRN inference algorithms: WGCNA, DCOL, GENIE3 and SCENIC.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Version used: **1.2.4**
- Evidence: Gene-regulatory activity was interrogated by applying SCENIC 1.2.4 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: GRN analysis The SCENIC+ 83 (v1.0.0) pipeline was used to predict transcription factors and putative target genes as well as regulatory genomic regions with binding sites.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Version used: **0.11.2**
- Evidence: ...y upstream motif for a respective transcription factor) was performed using a list of 1,390 human transcription factors ( https://github.com/aertslab/pySCENIC/blob/master/resources/hs_hgnc_curated_tfs.txt ) with the Python version of SCENIC (that is, pySCENIC v.0.11.2) 32 , 67 after importing expression matrices from Seurat to SCANPY (v.1.7.2).
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: SCENIC analysis and computation of regulon module scores The gene regulatory network analysis was performed using pySCENIC with the default parameters 35 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: Transcription factor activity levels were calculated using the pySCENIC pipeline (v.0.10.10).
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **0.12.1**
- Evidence: Gene regulatory network analysis To identify age-related changes in gene expression, we applied the pySCENIC (v.0.12.1) 68 gene regulatory network (GRN) inference tool to our scRNA-seq dataset.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: Regulatory network inference The goal of pySCENIC 97 , 98 is to infer transcription factors and regulatory networks from single-cell gene-expression data.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: Regulon analysis of transcription factors To carry out transcription factor network inference, analysis was performed as previously described 91 using the pySCENIC Python package (v.0.10.3).
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Cellular development and evolution of the mammalian cerebellum. (Nature 2024)

- DOI: 10.1038/s41586-023-06884-x | PMCID: PMC10808058 | PMID: 38029793
- Evidence: Among all mouse and human transcription factor markers, conservation of expression specificity is associated with higher expression levels of their predicted target genes in the respective cell states, as revealed by SCENIC 36 modelling (Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SCENIC]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: Inference of gene regulatory networks Using SCENIC+ (ref.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: For scRNA-seq, output from the Cell Ranger software was analysed using two different pipelines: (1) Scanpy, which is explained in detail under the SCENIC+ analysis; and (2) the Seurat pipeline, which is explained below.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Version used: **0.12.1**
- Evidence: TF activity prediction was conducted using the pySCENIC (v.0.12.1) docker distribution with the default parameter settings.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: Inference of regulatory networks To infer regulon activity, we used the Python implementation of the SCENIC 68 pipeline (pySCENIC).
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: Regulon analysis To identify key transcription factors and quantify the biological activity of their corresponding regulons in the pancreatic ductal adenocarcinoma scRNA‐seq dataset 27 , we applied the single‐cell regulatory network inference and clustering (SCENIC) workflow, as previously described 62 .
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: CM05 regulators in the spleen Inferring regulons We used the pySCENIC 30 , 72 pipeline to infer regulons for the four subsets (B03, B05, CD4T03, and I06) within CM05, performing the analysis separately for the three cellular lineages (B cells, CD4 + T cells, and innate lymphoid cells).
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Evidence: The TF activity for cells with TE or ICM candidate gene KD was evaluated using SCENIC 71 .
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: Regulon analysis We used the normalized discrete myeloid immunomodulatory expression matrix as an input for SCENIC 41 .
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: Of note, moscot comes with a list of TFs for different species (human, mouse and Drosophila ) obtained from the SCENIC+ database 131 .
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Evidence: Gene regulatory network analysis We implemented the SCENIC+ (v0.1.dev448+g2c0bafd) workflow 15 to build GRNs of the developing human neocortex based on the snMultiome data.
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Evidence: SCENIC analysis Gene regulatory networks for each cell population in each condition were calculated using SCENIC 75 .
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: SCENIC analysis of scRNA-seq data False-negative and false-positive cells were removed, and the dataset was divided into 15 libraries as per the sequencing library preparation.
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **0.10.3**
- Evidence: TF analysis Raw counts from the combined PFA object were used as input for the single-cell regulatory network inference and clustering (SCENIC) Python pipeline (pySCENIC, v.0.10.3) 73 , 74 .
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Evidence: Transcription factor activity inference was conducted using pySCENIC with default parameter settings 48 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: Finally, SCENIC+ analysis was performed to study distinct GRNs (eRegulons) active in NSCs and mature astrocytes.
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: On average, one meta cell contains 75 single cells and meta cells representing all the cell types originally presented in the dataset were input to the SCENIC+ workflow.
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: To infer enhancer-driven gene regulatory networks, scRNA-seq and scATAC–seq data were eventually combined into a pseudo-multiome dataset using SCENIC+ 95 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Transcription factor regulon analysis The pySCENIC pipeline (v.0.12.2b0) 66 was utilized to identify active transcription factor modules in scRNA-seq datasets.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Version used: **1.1.2**
- Evidence: The R package SCENIC v.1.1.2-2 was used to perform gene regulatory network analysis on IRI nuclei across all PTC clusters as previously described ( 31 ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### Specification of neuronal subtypes in the spiral ganglion begins prior to birth in the mouse. (PNAS 2022)

- DOI: 10.1073/pnas.2203935119 | PMCID: PMC9860252 | PMID: 36409884
- Evidence: Data was processed and analyzed using the following R-based packages: Seurat (v3.2) ( 47 ), DoubletFinder (v2.0.3) ( 48 ), Harmony (v1.0) ( 49 ), Slingshot (v1.8) ( 17 ), tradeSeq (v1.4)( 20 ), Monocle 3 ( 21 , 50 ), and SCENIC ( 23 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle, SCENIC, Seurat v3.2, Slingshot v1.8, scDblFinder v2.0.3]

### SOX9 and SOX10 control fluid homeostasis in the inner ear for hearing through independent and cooperative mechanisms. (PNAS 2022)

- DOI: 10.1073/pnas.2122121119 | PMCID: PMC9674217 | PMID: 36343245
- Evidence: Single-Cell Regulatory Network Inference and Clustering (SCENIC) regulon analysis also identified reduced SOX10 activity in the mutant RRCs ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [SCENIC]

### Single-cell analyses highlight the proinflammatory contribution of C1q-high monocytes to Behçet's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2204289119 | PMCID: PMC9245671 | PMID: 35727985
- Evidence: Next, we used SCENIC tools ( 45 ) to predict which TFs modulate these DEGs and noted the marked enrichment of TFs that regulate IFN-γ response pathways, including STAT1 and IRF1 ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [UMAP] -> stage not stated [Monocle, SCENIC]

### Transcriptional and functional motifs defining renal function revealed by single-nucleus RNA sequencing. (PNAS 2022)

- DOI: 10.1073/pnas.2203179119 | PMCID: PMC9231607 | PMID: 35696569
- Evidence: SCENIC results showed that there are 47 unique fly TFs that can be mapped to 94 orthologs in the mouse ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [SCENIC] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Transcriptome profiling in swine macrophages infected with African swine fever virus at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2201288119 | PMCID: PMC9171760 | PMID: 35507870
- Evidence: Transcriptional regulatory network analysis was applied to reveal potential core regulators using a modified version of the single-cell regulatory network inference and clustering (SCENIC) pipeline ( 21 ).
- Full pipeline: dimensionality reduction/clustering [SCENIC, UMAP]

### A single factor elicits multilineage reprogramming of astrocytes in the adult mouse striatum. (PNAS 2022)

- DOI: 10.1073/pnas.2107339119 | PMCID: PMC8931246 | PMID: 35254903
- Evidence: Finally, we used coexpression and regulatory relationships to construct gene regulatory networks (pySCENIC) ( 39 ) underlying DLX2-mediated reprogramming.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SCENIC]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Evidence: By analyzing the upstream gene-regulatory networks using SCENIC regulon inference, noncycling DKO MPPs were predicted to increase the activity of several transcription factor networks essential for self-renewal of HSCs ( 76 ).
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### The mechano-chemical circuit drives skin organoid self-organization. (PNAS 2023)

- DOI: 10.1073/pnas.2221982120 | PMCID: PMC10483620 | PMID: 37643215
- Evidence: Gene-Regulatory Network (GRN) analysis by single-cell regulatory network inference and clustering (SCENIC) reveals increased activation of the Yap pathway in basal epidermal cells from D2 to D4 ( Fig.
- Full pipeline: quality control [Seurat v4.0.3] -> dimensionality reduction/clustering [SCENIC, Seurat v4.0.3] -> differential/statistical testing [Seurat v4.0.3]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: Therefore, we performed single-cell regulatory network interference and clustering (SCENIC) ( 34 ) analysis to determine the GRN associated with the transition of transplanted RPE toward adult human RPE (Ref_RPE) ( Fig.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### PHGDH preserves one-carbon cycle to confer metabolic plasticity in chemoresistant gastric cancer during nutrient stress. (PNAS 2023)

- DOI: 10.1073/pnas.2217826120 | PMCID: PMC10214193 | PMID: 37192160
- Evidence: Reconstruction of the gene regulatory network using SCENIC determined that the activity of the ATF4 and CEBPB regulon, which denotes a gene regulatory network with significant motif enrichment, increased upon GLS inhibition in only EMT-type cell clusters ( Fig.
- Full pipeline: dimensionality reduction/clustering [CellChat, R, SCENIC, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> structure determination [SCENIC] -> visualisation [UMAP] -> stage not stated [GSVA]

### Distinct and opposite effects of leukemogenic <i>Idh</i> and <i>Tet2</i> mutations in hematopoietic stem and progenitor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2208176120 | PMCID: PMC9942850 | PMID: 36652477
- Evidence: The raw sequencing reads were first processed and mapped to mouse genome build GRCm38 using the CellRanger software (v2.1.0, 10X Genomics), followed by analysis using Seurat ( 47 , 97 ), SCENIC ( 45 ), and Slingshot ( 46 ) as detailed in SI Appendix , Supplementary Methods .
- Full pipeline: alignment/mapping [SCENIC, Seurat, Slingshot] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, MACS2]

### Dry eye disease in mice activates adaptive corneal epithelial regeneration distinct from constitutive renewal in homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2204134120 | PMCID: PMC9926235 | PMID: 36595669
- Evidence: We used single-cell regulatory network inference and clustering (SCENIC) to discover the GRNs characterizing cell states in the corneal epithelium ( 25 , 26 ).
- Full pipeline: dimensionality reduction/clustering [SCENIC, UMAP] -> stage not stated [Seurat]

### Cellular heterogeneity and dynamics of the human uterus in healthy premenopausal women. (PNAS 2024)

- DOI: 10.1073/pnas.2404775121 | PMCID: PMC11551439 | PMID: 39471215
- Evidence: ( D ) SCENIC-based TF activities differ across stromal, epithelial, blood endothelial, and immune cell subtypes.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [SCENIC]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Version used: **1.3.1**
- Evidence: Intercellular signaling was measured and analyzed with cellchat 1.5.0 ( 84 ). and transcription factor regulons were inferred and analyzed with the SCENIC 1.3.1 ( 45 , 85 ) pipeline.
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Single-cell analysis of treatment-resistant prostate cancer: Implications of cell state changes for cell surface antigen-targeted therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322203121 | PMCID: PMC11252802 | PMID: 38968122
- Evidence: To study tumor cell heterogeneity specifically in CRPC PRAD and NEPC samples and reasoning that lineage plasticity is likely driven by transcription factor (TF) networks, we focused on shared and unique gene-regulatory networks (GRNs) across samples using single-cell regulatory network inference (SCENIC) ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, SCENIC]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: The gene regulatory networks and transcription factor activities were inferred using pySCENIC workflow (version 0.12.1).
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Expression of <i>Atoh1</i>, <i>Gfi1</i>, and <i>Pou4f3</i> in the mature cochlea reprograms nonsensory cells into hair cells. (PNAS 2024)

- DOI: 10.1073/pnas.2304680121 | PMCID: PMC10835112 | PMID: 38266052
- Evidence: ( F ) SCENIC analysis detected the activation of genes associated with Atoh1 and Pou4f3 regulons in reprogrammed hair cells (Rprg HCs).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> stage not stated [SCENIC, scVelo]

### A spatiotemporal molecular atlas of the ovulating mouse ovary. (PNAS 2024)

- DOI: 10.1073/pnas.2317418121 | PMCID: PMC10835069 | PMID: 38252830
- Evidence: Single-cell regulatory network inference and clustering analysis to infer transcription factors and gene regulatory networks for Slide-seq data was performed using pySCENIC package (v0.12.1) ( 58 , 59 ).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SCENIC, scikit-learn] -> visualisation [Squidpy] -> stage not stated [AnnData, CellPhoneDB, Scanpy]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: Regulon analysis was performed using pySCENIC ( 60 ) to infer transcription factor–target interactions and assess regulon activity at the single-cell level.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: GRNs were inferred using the pySCENIC pipeline ( 45 ) (Python implementation of SCENIC).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: For multimodal gene regulatory network inference with SCENIC+, we used cells that passed quality control in both modalities to ensure that each cell had high-quality gene expression and ATAC data. scRNA-seq data dimensionality reduction and visualization.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Cellular cartography reveals mouse prostate organization and determinants of castration resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2427116122 | PMCID: PMC12415206 | PMID: 40854129
- Evidence: Extension of such analysis at the systems level using SCENIC+ ( 27 ) revealed that prostatic LEs are defined by unique TMs, wherein the activity of Gata1/2 , Klf5 , Bhlha15, and Spdef determine the identity of LE1/LE2, LE5, LE7, and LE8, respectively ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB, GSVA, SCENIC]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: To predict the cell type–specific TFs regulating EHT dynamics in mice, regulon activity scores were calculated by the aucell method using SCENIC ( 71 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Acute TREM2 inhibition depletes MAFB-high microglia and hinders remyelination. (PNAS 2025)

- DOI: 10.1073/pnas.2426786122 | PMCID: PMC12002275 | PMID: 40131948
- Evidence: To identify regulons, i.e., transcription factors driving specific microglial signatures, we applied the Single-Cell rEgulatory Network Inference and Clustering (SCENIC) algorithm to our microglial snRNA-seq data ( Dataset S3 ) ( 35 ).
- Full pipeline: alignment/mapping [Monocle, Seurat] -> dimensionality reduction/clustering [Monocle, SCENIC, Seurat, UMAP] -> simulation/modelling [Monocle, Seurat]

### Multiomics analysis unveils the cellular ecosystem with clinical relevance in aldosterone-producing adenomas with &lt;i&gt;KCNJ5&lt;/i&gt; mutations. (PNAS 2025)

- DOI: 10.1073/pnas.2421489122 | PMCID: PMC11892633 | PMID: 40009643
- Evidence: SCENIC analysis ( 33 ) explored key regulatory networks in each steroidogenic cell subtype.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat v2.1.1, SCENIC]

### RORγt-expressing dendritic cells are functionally versatile and evolutionarily conserved antigen-presenting cells. (PNAS 2025)

- DOI: 10.1073/pnas.2417308122 | PMCID: PMC11892598 | PMID: 39993193
- Evidence: ( E ) UMAP display of dimensionality reduction based on target genes and region enrichment scores generated using SCENIC+.
- Full pipeline: dimensionality reduction/clustering [SCENIC, Seurat, UMAP]

### Human MAIT cell response profiles biased toward IL-17 or IL-10 are distinct effector states directed by the cytokine milieu. (PNAS 2025)

- DOI: 10.1073/pnas.2414230122 | PMCID: PMC11831165 | PMID: 39903121
- Evidence: To investigate which transcription factors may be involved in the induction of IL-10, we used the pySCENIC workflow ( 34 ).
- Full pipeline: dimensionality reduction/clustering [UMAP v3.1] -> stage not stated [SCENIC]

### Systematic identification of single transcription factor perturbations that drive cellular and tissue rejuvenation. (PNAS 2026)

- DOI: 10.1073/pnas.2515183123 | PMCID: PMC12799168 | PMID: 41512022
- Evidence: TF perturbations (rows) were clustered by the TF module scores (indicated by the color of the pixels) for selected TF modules (columns) from the SCENIC analysis.
- Full pipeline: dimensionality reduction/clustering [SCENIC]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: ...rythroid cell with a HBZ module z -score > 0, and erythroid as any erythroid cell with individual module z -score of HBA1, HBA2, HBG1, HBG2, HBD > 0. pySCENIC for regulon analysis The pySCENIC package (v0.9.19) was used to identify transcription factors (TFs) and their target genes in the YS and iPSC scRNA-seq datasets.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Distinct myeloid-derived suppressor cell populations in human glioblastoma. (Science 2025)

- DOI: 10.1126/science.abm5214 | PMCID: PMC12836367 | PMID: 39818911
- Evidence: Calculation of transcription factor signaling networks The SCENIC workflow was first used to identify transcription factor activities by cell.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R, SCENIC, velocyto]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: Gene regulatory network (GRN) inference We constructed gene regulatory networks (GRNs) for human, mouse, and marmoset using the SCENIC+ pipeline ( 45 ) on metacells generated by aggregating single cells in similar cell states as described below.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

