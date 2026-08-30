# Signac

- **Category:** single-cell
- **Papers in survey:** 57
- **Journals:** Nature (41), PNAS (12), Science (2), Cell (2)
- **Years:** 2021 (4), 2022 (2), 2023 (12), 2024 (13), 2025 (21), 2026 (5)
- **Versions named:** 1.14.0 (4), 1.12.0 (3), 1.8 (2), 1.9.0 (2), 1.6.0 (2), 1.5.0 (2), 1.10 (1), 1.14 (1), 1.1.0 (1), 1.10.0 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (6), normalisation (6), visualisation (3), quality control (2), differential/statistical testing (1)

## Papers

### Integrated analysis of multimodal single-cell data. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.048 | PMCID: PMC8238499 | PMID: 34062119
- Version used: **1.0.0**
- Evidence: ...s uwot v 0.1.10 McInnes et al., 2018 https://github.com/jlmelville/uwot Presto v1.0.0 Korsunsky et al., 2019 https://github.com/immunogenomics/presto Signac v1.0.0 Stuart et al., 2020 https://satijalab.org/signac/index.html R R Core https://www.r-project.org/ Python Python Software Foundation https://www.python.org/ Resource availability Lead contact Further information and requests for resources ...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat v3.2.0, Signac v1.0.0]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **1.13.0**
- Evidence: Signac (v1.13.0) 117 and Seurat (v5.1.0) 118 were used to import sample files into chromatin assay objects, followed by Seurat objects.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **0.1.4**
- Evidence: The matrices for peak counts were filtered to keep only locations from chromosomes 1–22, X or Y, and processed using Seurat (v3.1.0) and Signac (v0.1.4) software 45 ( https://satijalab.org ).
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Skin-resident innate lymphoid cells converge on a pathogenic effector state. (Nature 2021)

- DOI: 10.1038/s41586-021-03188-w | PMCID: PMC8336632 | PMID: 33536623
- Evidence: The depth-normalized, aggregated, filtered dataset was analysed with Signac [ 67 ] (v0.1.6; https://github.com/timoast/signac ), a Seurat [ 45 ] extension for the analysis of scATAC-seq data, run with random number generator seed set as 1234.
- Full pipeline: normalisation [SciPy, Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Scanpy, UMAP] -> visualisation [UMAP] -> stage not stated [Bioconductor]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: Using Signac ( https://satijalab.org/signac/ v.0.2.5), the binary matrix was normalized with TF-IDF followed by a dimensionality reduction step using singular value decomposition.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Signac 90 was used to generate and store peak-by-cell count matrices for each sample. snATAC markers for each cluster were calculated (FindAllMarkers, test.use = 'LR', vars.to.regress = 'nCount_ATAC', min.pct = 0.1, min.diff.pct = 0.05, logfc.threshold = 0.15).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **1.5.0**
- Evidence: The filtered matrix of WT and Msl2 KO were merged together with Signac (v.1.5.0) 72 and Seurat (v.4.1.0) 73 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: Peak calling for snATAC-seq data To call peaks on snATAC-seq data (from regular snATAC-seq and from snMultiome-seq), we used the MACS2 tool (v.2.2.7.1) 72 through the CallPeaks function of the Signac package (v.1.3.0, https://github.com/timoast/signac ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Version used: **1.4.0**
- Evidence: Processing of single-cell multiome data and GRN inference Initial transcript count and peak accessibility matrices for the multiome data were obtained from sequencing reads with Cell Ranger Arc and further processed using the Seurat (v.4.0.1) and Signac (v.1.4.0) 67 R packages.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Version used: **1.6.0**
- Evidence: ATAC data were normalized by term frequency inverse document frequency (TF-IDF), and partial singular value decomposition (SVD) was performed using RunSVD by Signac (v.1.6.0).
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: SNARE2 accessible chromatin analyses SNARE2 chromatin data were analysed using Signac 74 (v.1.1.1).
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: Matrices were then read into Seurat 50 and Signac 51 using the Read10X_h5 command.
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: Using Signac ( https://satijalab.org/signac/ version 0.2.5), the binary matrix was normalized with term frequency-inverse document frequency (TF-IDF) followed by a dimensionality reduction step using Singular Value Decomposition (SVD).
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Spatial epigenome-transcriptome co-profiling of mammalian tissues. (Nature 2023)

- DOI: 10.1038/s41586-023-05795-1 | PMCID: PMC10076218 | PMID: 36922587
- Version used: **1.8**
- Evidence: Signac v.1.8 (ref.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.2] -> visualisation [ArchR v1.0.1, Seurat v4.1] -> stage not stated [Monocle, Signac v1.8]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Version used: **1.1**
- Evidence: Both the fragment files and the peak count matrices were further preprocessed using Seurat (v.3.2) 19 and Signac (v.1.1) 53 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Exaptation of ancestral cell-identity networks enables C&lt;sub&gt;4&lt;/sub&gt; photosynthesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08204-3 | PMCID: PMC11618092 | PMID: 39567684
- Evidence: For the 10X-multiome (RNA + ATAC) clustering we used Signac 55 .
- Full pipeline: dimensionality reduction/clustering [Seurat, Signac, UMAP] -> differential/statistical testing [OrthoFinder] -> stage not stated [DESeq2, MACS2]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Version used: **1.13**
- Evidence: Processing the multiome data We performed the initial processing of multiome data using Seurat (v5.0.3) and Signac (v1.13) 66 .
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Single-cell CAR T atlas reveals type 2 function in 8-year leukaemia remission. (Nature 2024)

- DOI: 10.1038/s41586-024-07762-w | PMCID: PMC11485231 | PMID: 39322664
- Version used: **1.12.0**
- Evidence: The output per barcode matrices underwent joint RNA and ATAC analysis using Signac (v.1.12.0) 41 and Seurat (v.4) 38 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### The type 2 cytokine Fc-IL-4 revitalizes exhausted CD8&lt;sup&gt;+&lt;/sup&gt; T cells against cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07962-4 | PMCID: PMC11485240 | PMID: 39322665
- Version used: **1.12.0**
- Evidence: Output matrices per barcode underwent joint RNA and ATAC analysis using Signac v.1.12.0 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: Cellranger aggr outputs were used for downstream analysis in R using the Signac package.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: RNA and chromatin profiles of the four datasets were integrated with Signac 96 (v.1.12.0) using the FindIntegrationAnchors function.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: For regulon analyses of single-cell ATAC-seq data, the processed Signac data objects of CAR T products profiled by single-cell ATAC-seq were obtained from a previous study 5 .
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **1.9.0**
- Evidence: The scMultiome ATAC dataset was recounted by Signac (v1.9.0) 45 using the merged peak bed files and processed by Harmony (v0.1.1) 46 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Version used: **1.6.0**
- Evidence: All multiome data were analysed in R v.4.1.3 using packages Signac v.1.6.0 and Seurat v.4.1.0.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Version used: **1.9.0**
- Evidence: The ATAC-filtered feature-barcode matrix generated by Cell Ranger was read into R (v.4.1.1) using Signac (v.1.9.0) 77 , and added as its own assay slot in the Seurat object containing RNA expression counts.
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Version used: **1.8**
- Evidence: We used Library Signac (v.1.8) 93 in R (v.4.1) to read the ATAC data matrices.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Maternal stress triggers early-life eczema through fetal mast cell programming. (Nature 2025)

- DOI: 10.1038/s41586-025-09419-8 | PMCID: PMC12488486 | PMID: 40866704
- Version used: **1.14.0**
- Evidence: The resulting datasets were loaded into Seurat (v.5.1.0) and Signac (v.1.14.0) for downstream analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2 v1.34.0, ImageJ v2.16.0, Seurat, Signac v1.14.0]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Version used: **1.10**
- Evidence: Seurat v.4.3 62 and Signac v.1.10 63 were used for subsequent analyses.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Range extender mediates long-distance enhancer activity. (Nature 2025)

- DOI: 10.1038/s41586-025-09221-6 | PMCID: PMC12267059 | PMID: 40604280
- Evidence: Expression counts and chromatin peak matrices generated from CellRanger were further processed using the Signac R package 83 .
- Full pipeline: alignment/mapping [BEDTools] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER] -> stage not stated [MACS2, R, Signac]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: For quality control and filtering, we used Signac 65 (v1.11.0), a comprehensive R package for the analysis of single-cell chromatin data, to preprocess each snMultiome sample.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: Single-cell RNA-seq and ATAC-seq data were processed using mainly the Seurat and Signac packages in R.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Version used: **1.12.0**
- Evidence: Motif activities for each sample were calculated using the function RunChromVAR in Signac (v.1.12.0) 71 with the JASPAR motif database (2020 version) 72 .
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: The selected cells were processed using the Signac R package 45 to filter the doublets/outliers on the basis of signal per cell distribution analysis and to inspect the cell compartments by means of UMAP visualization after normalization and identification of the most highly variable regions. snRNA-seq data information was used to annotate the cells from corresponding processed data.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens. (Nature 2025)

- DOI: 10.1038/s41586-025-08982-4 | PMCID: PMC12176658 | PMID: 40228524
- Version used: **1.14**
- Evidence: All scATAC–seq analysis was performed with Signac version 1.14, following a standard workflow 67 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.3, Picard, SAMtools v0.1.19] -> normalisation [Seurat v5.1] -> dimensionality reduction/clustering [Seurat v5.1, UMAP] -> stage not stated [Signac v1.14]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: Each library was then processed using Signac 71 v.1.12.0 to remove low-quality cells.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: The ATAC data were processed by term frequency-inverse document frequency (tf-idf) normalization followed by singular-value decomposition using Signac, computing the first 50 singular components.
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Version used: **1.1.0**
- Evidence: Analysis of Tfap2d regulatory regions and SOX11 ChIP–seq data To determine what regions within the Tfap2d locus can be potential enhancers, we re-processed a single-cell ATAC-seq embryonic dataset of the mouse cortex 33 using Signac version 1.1.0 ( https://satijalab.org/signac/ ), to obtain ATAC-seq peaks that are accessible in migrating excitatory neurons in PCD13.5 onwards.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **1.10.0**
- Evidence: The peak-by-nucleus counts for each sample were integrated by reciprocal latent semantic indexing (LSI) projection functions using the R package Signac (v.1.10.0) 52 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: Count data were analysed using the R packages Seurat (v.5) 49 and Signac 50 .
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Version used: **1.3.0**
- Evidence: Data were analysed in R (v.4.1.0) using Seurat (v.4.0.3) 46 and Signac (v.1.3.0) 47 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Peak-by-cell count matrices were integrated across samples using reciprocal latent semantic indexing (LSI) projection in Signac 12 .
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **1.14.0**
- Evidence: We assessed data quality at the individual nucleus level and retained high-quality nuclei using Seurat (v.5.1.0, https://satijalab.org/seurat ) and Signac (v.1.14.0, https://github.com/timoast/signac ), applying the following criteria: total ATAC fragment count (nCount_ATAC) of at least 3,000, transcription start site enrichment scores between 2 and 15, total RNA counts (nCount_RNA) of at least 2,...
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **1.14.0**
- Evidence: Data processing Initial quality control and cell filtering DNA accessibility and gene expression from each cell were analysed simultaneously using Seurat (v.4.0.5 and v.4.3) 61 and Signac (1.14.0) 66 R packages.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: Such matrices can be produced by tools like ArchR or Signac.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### A single-cell multiomic analysis of kidney organoid differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2219699120 | PMCID: PMC10193973 | PMID: 37155865
- Evidence: ATAC-seq peaks in the dataset were identified on all cells together using MACS2 ( 75 ) with the default parameters of Signac’s (v1.5.0) CallPeaks function: --gsize 2.7e9 --nomodel False --shift -100 --extsize 200 --d-min 20 --qvalue 0.05 --broad False ( 57 ).
- Full pipeline: quantification [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.20.0] -> stage not stated [MACS2, R, Signac, scDblFinder]

### Direct neuronal reprogramming by temporal identity factors. (PNAS 2023)

- DOI: 10.1073/pnas.2122168120 | PMCID: PMC10175841 | PMID: 37126716
- Evidence: Filtered output files were analyzed in R (R Core Team, The R project for Statistical Computing) using the Signac package version 1.8.0 ( 76 ).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, Signac] -> stage not stated [Python, Scanpy v1.9.1]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: Filtered cells were then analyzed in Signac ( 32 ) (v1.4), where we performed latent semantic indexing to obtain low-dimensional projections that were used to integrate datasets according to the ATAC integration pipeline ( https://satijalab.org/signac/articles/integrate_atac.html ).
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Long-range &lt;i&gt;Atoh1&lt;/i&gt; enhancers maintain competency for hair cell regeneration in the inner ear. (PNAS 2024)

- DOI: 10.1073/pnas.2418098121 | PMCID: PMC11665905 | PMID: 39671177
- Evidence: Bioinformatic analysis used cellranger, Seurat ( 60 ), Signac ( 61 ), deepTools ( 62 ), DESeq2 ( 63 ), DiffBind ( 64 ), and Homer ( 55 ).
- Full pipeline: stage not stated [DESeq2, Seurat, Signac, deepTools]

### Chronologically inappropriate morphogenesis (&lt;i&gt;Chinmo&lt;/i&gt;) is required for maintenance of larval stages of fall armyworm. (PNAS 2024)

- DOI: 10.1073/pnas.2411286121 | PMCID: PMC11626174 | PMID: 39589873
- Evidence: The single-cell multiomics data were analyzed using the open-source Seurat and Signac packages implemented in the R computing environment ( 58 ).
- Full pipeline: quantification [MACS2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, Seurat, Signac]

### An integrated transcription factor framework for Treg identity and diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2411301121 | PMCID: PMC11388289 | PMID: 39196621
- Version used: **1.4**
- Evidence: Data Analysis. scATAC-seq data analysis was performed using Signac v1.4 ( 98 ), using a common set of open chromatin regions throughout the study.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Signac v1.4]

### Dynamics and variegation in the Treg response to Interleukin-2. (PNAS 2025)

- DOI: 10.1073/pnas.2518991122 | PMCID: PMC12663944 | PMID: 41264258
- Version used: **1.14.0**
- Evidence: Data were processed and analyzed as described ( 17 ) with Signac v1.14.0 ( 58 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat, Signac v1.14.0]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Version used: **4.3.0**
- Evidence: To construct a peak count matrix, we supplied a fragment file and the peak sets described above to Seurat (v1.9.0) ( 44 ) and Signac (version 4.3.0) ( 45 ).
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: Cell state analyses, including gene activity scores and surface protein visualization, were performed using the Seurat/Signac framework ( 43 , 44 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: The RNA/ATAC multiome analysis employed Seurat and Signac ( 50 ) (v1.14.0).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### Bridging unpaired single-cell multimodal data for integrative analyses with SuperMap. (PNAS 2026)

- DOI: 10.1073/pnas.2505182123 | PMCID: PMC12890892 | PMID: 41650244
- Evidence: We benchmarked SuperMap against existing gene activity score calculation methods, including Signac ( 35 ), MAESTRO ( 36 ), and UnpairReg ( 30 ), on 10X Multiome PBMC, 10X Multiome BMMC, and SHARE-seq mouse skin datasets.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [ArchR, Signac]

### Functional maps of a genomic locus reveal confinement of an enhancer by its target gene. (Science 2025)

- DOI: 10.1126/science.ads6552 | PMCID: PMC7618358 | PMID: 40966339
- Evidence: Next, the reprocessed bigwig tracks were downloaded from cistrome ( http://dc2.cistrome.org//genome_browser/bw/X , where X is the cistrome ID) and visualized using the BigwigTrack function from Signac ( 55 ), smoothing over 100bp.
- Full pipeline: alignment/mapping [BWA] -> quantification [deepTools v3.0] -> normalisation [deepTools v3.0] -> visualisation [Signac] -> stage not stated [BCFtools v1.9, MACS2, SnpEff v4.3p]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Version used: **1.5.0**
- Evidence: If not specified otherwise, all downstream analyses were performed with Signac (v1.5.0)( 77 ) and Seurat (v4.1)( 70 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

