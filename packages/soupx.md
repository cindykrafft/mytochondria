# SoupX

- **Category:** single-cell
- **Papers in survey:** 33
- **Journals:** Nature (19), PNAS (9), Science (3), Cell (2)
- **Years:** 2021 (1), 2022 (3), 2023 (4), 2024 (11), 2025 (7), 2026 (7)
- **Versions named:** 1.6.2 (5), 1.5.2 (2), 1.6.0 (1), 1.4.8 (1), 1.5.0 (1), 1.4.5 (1), 1.6.1 (1)
- **Pipeline stages it appears in:** quality control (13), dimensionality reduction/clustering (4), normalisation (2), quantification (1)

## Papers

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 73 https://github.com/MarioniLab/DropletUtils cellranger (versions: 3.0.2, 4.0.0) 10X genomics https://github.com/10XGenomics/cellranger cellranger-atac (version: 1.2.0) 10X genomics https://github.com/10XGenomics/cellranger-atac SoupX (version: 1.4.5) Young etal.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Renal PIEZO2 is an essential regulator of renin. (Cell 2026)

- DOI: 10.1016/j.cell.2025.11.013 | PMCID: PMC12695021 | PMID: 41349545
- Version used: **1.6.2**
- Evidence: Ambient RNA contamination was estimated and removed using SoupX v.1.6.2.
- Full pipeline: quality control [SoupX v1.6.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: For each run, we apply the SoupX algorithm 50 with default parameters and function adjustCounts() to remove ambient mRNA from the count matrix.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: To identify marker genes specific to a cluster, we used the TF-IDF approach from the SoupX package v.1.5.0 (ref.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Version used: **1.5.0**
- Evidence: The ambient mRNA contamination was corrected using SoupX (v.1.5.0) 57 .
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Injury prevents Ras mutant cell expansion in mosaic skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06198-y | PMCID: PMC10322723 | PMID: 37344586
- Evidence: 4a , 6a and 7a ) were first processed with SoupX 61 ( https://github.com/constantAmateur/SoupX ) to remove barcodes that most probably represent ambient RNA as opposed to whole cells, using the algorithm’s automated method.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Scanpy v1.6, Seurat, SoupX, scDblFinder, scikit-learn v0.24.2]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Version used: **1.6.0**
- Evidence: For gene expression data, SoupX (v1.6.0) 72 was applied to remove background ambient RNA.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: SoupX 78 was used to estimate potential ambient RNA contamination in all samples, but no sample required any correction.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Spatially clustered type I interferon responses at injury borderzones. (Nature 2024)

- DOI: 10.1038/s41586-024-07806-1 | PMCID: PMC11374671 | PMID: 39198639
- Evidence: Doublets and aggregated nuclei were determined by assessing non-endogenous gene markers (for example, the presence of CM genes such as Myh6 in the fibroblast subset) and ambient RNA were removed using SoupX, which displayed subsets after filtering and removing doublets/multiples.
- Full pipeline: quality control [Scanpy, Squidpy] -> normalisation [ImageJ, Scanpy, Seurat, Squidpy] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose, R, SoupX]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: Single-cell genomics data processing Both scRNA-seq and ADT-seq data were corrected using SoupX 38 to remove free-floating and background RNAs and ADTs.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: We used the Scrublet 46 Python module v0.2.3 to identify potential doublets and the SoupX 47 R package v1.5.2 to automatically calculate and correct for background contamination.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **1.4.8**
- Evidence: Ambient RNA for snRNA-seq was reduced using SoupX (v.1.4.8) 62 with the default settings.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: For each run, SoupX algorithm 48 was run with default parameters to remove ambient mRNA from the count matrix.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Version used: **1.6.2**
- Evidence: Ambient RNA was detected and corrected using R package SoupX v1.6.2.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Filtered cells were corrected for background signature using the SoupX pipeline 41 .
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Glycocalyx dysregulation impairs blood-brain barrier in ageing and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08589-9 | PMCID: PMC11946907 | PMID: 40011765
- Version used: **1.6.2**
- Evidence: Ambient RNA was removed from each sample using SoupX (v1.6.2) and droplets containing multiple nuclei were filtered out using DoubletFinder (v2.0.4).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.32, Metascape] -> visualisation [DESeq2 v1.32] -> stage not stated [ImageJ, Seurat v4.1.1, SoupX v1.6.2, scDblFinder v2.0.4]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Version used: **1.6.2**
- Evidence: Raw UMI count matrices for all samples were first imported using Seurat (v4.1.0) 42 ( www.satijalab.org/seurat ), and immediately subject to ambient RNA correction using a customized version of the SoupX (v1.6.2) R pipeline ( https://github.com/constantAmateur/SoupX ) 43 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **1.6.2**
- Evidence: To estimate ambient RNA and correct for background contamination, the SoupX (v1.6.2) package 82 was used for each sample using raw and filtered feature matrices from the Cell Ranger output.
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Evidence: Subsequently, ambient RNA contamination per sample was assessed using SoupX ( https://github.com/constantAmateur/SoupX ) on the prefiltered data.
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Evidence: Initial dimensionality reduction and clustering were performed to enable removal of cell-free mRNA using SoupX 79 .
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: To identify genes characteristic of each cluster, we performed term frequency–inverse document frequency, a method borrowed from natural-language processing that reflects how important a word (gene) is to a document (cluster) in a corpus (dataset), as implemented in the R library SoupX 78 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Cellular and molecular architecture of submucosal glands in wild-type and cystic fibrosis pigs. (PNAS 2022)

- DOI: 10.1073/pnas.2119759119 | PMCID: PMC8794846 | PMID: 35046051
- Evidence: Matrix data were subjected to ambient RNA correction using the SoupX R package ( 72 ), doublet filtering using the Scrublet Python package ( 73 ), and dead and low-quality cell filtering in Seurat ( 74 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat, SoupX, scDblFinder]

### The developmental hierarchy and scarcity of replicative slender trypanosomes in blood challenges their role in infection maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2306848120 | PMCID: PMC10589647 | PMID: 37824530
- Evidence: As the day 7 -dox sample showed a higher than expected number of droplets with low total RNA, we controlled for potential free RNA in the samples with SoupX ( 48 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Seurat v4.1.0, SoupX]

### High-throughput droplet-based analysis of influenza A virus genetic reassortment by single-virus RNA sequencing. (PNAS 2023)

- DOI: 10.1073/pnas.2211098120 | PMCID: PMC9963642 | PMID: 36730204
- Evidence: Dashed lines distinguish BCs harboring >80% of their UMIs from a single strain that were used in the first iteration of the global contamination fraction (rho) estimation with SoupX, using UMIs from the minor strain as presumed contamination.
- Full pipeline: quality control [SoupX]

### Regional specialization, polyploidy, and seminal fluid transcripts in the &lt;i&gt;Drosophila&lt;/i&gt; female reproductive tract. (PNAS 2024)

- DOI: 10.1073/pnas.2409850121 | PMCID: PMC11536144 | PMID: 39453739
- Version used: **1.5.2**
- Evidence: SoupX v1.5.2 ( 51 ) was used with default parameters to remove cell-free mRNA contamination.
- Full pipeline: quality control [SoupX v1.5.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v2.3.0, R v4.1, Seurat v5.0.3]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Evidence: In case of batch effects, the Harmony ( 56 ) or SoupX ( 57 ) package was utilized for correction.
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: The SoupX pipeline ( 53 ) was used to remove ambient RNA contaminants from each dataset.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### pTDP-43 levels correlate with cell type-specific molecular alterations in the prefrontal cortex of &lt;i&gt;C9orf72&lt;/i&gt; ALS/FTD patients. (PNAS 2025)

- DOI: 10.1073/pnas.2419818122 | PMCID: PMC11892677 | PMID: 39999167
- Evidence: We used SoupX ( 13 ) to detect ambient RNA contamination and found it to be negligible ( SI Appendix , Fig.
- Full pipeline: quality control [ArchR, Seurat, SoupX] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [WGCNA]

### Dissecting the cellular architecture and genetic circuitry of the soybean seed. (PNAS 2025)

- DOI: 10.1073/pnas.2416987121 | PMCID: PMC11725896 | PMID: 39793081
- Version used: **1.6.1**
- Evidence: Ambient RNA contamination was removed using the R package SoupX v1.6.1 using default parameters ( 54 ).
- Full pipeline: quality control [SoupX v1.6.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v4.1.1, WGCNA]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Version used: **1.4.5**
- Evidence: Ambient RNA contamination was corrected using SoupX (v1.4.5) ( 31 ), and putative doublets were identified and removed with DoubletFinder (v2.0) ( 32 ) following 10x Genomics recommendations.
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: The gene expression count matrix for each sample was processed with the following steps: ( 1 ) Estimate doublet with Scrublet ( https://github.com/swolock/scrublet ) ( 88 ); ( 2 ) Estimate and correct the ambient RNA contaminations with SoupX ( https://github.com/constantAmateur/SoupX ) ( 89 ); ( 3 ) Load the corrected counting matrix into Seurat object with log normalization; ( 4 ) Calculate the ...
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: To reduce potential ambient RNA contamination, especially for nuclear libraries, SoupX ( 69 ) was applied to the raw gene count matrix obtained from Cell Ranger, and the corrected read count matrix was used for downstream analyses with Seurat (v4.1)( 70 ) if not specified otherwise.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **1.5.2**
- Evidence: We then used these clusters as input to SoupX (v1.5.2) ( 80 ) to correct the expression of transcripts associated with ambient RNA or cellular debris.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

