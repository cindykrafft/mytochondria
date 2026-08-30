# Cellpose

- **Category:** imaging
- **Papers in survey:** 93
- **Journals:** Nature (51), PNAS (34), Cell (6), Science (2)
- **Years:** 2022 (4), 2023 (9), 2024 (21), 2025 (45), 2026 (14)
- **Versions named:** 2.0 (11), 2.2.3 (2), 1.0.2 (2), 1.0 (2), 2.0.5 (1), 2.2.2 (1), 2.0.4 (1), 3.1.0 (1), 3.1.1.1 (1)
- **Pipeline stages it appears in:** machine learning (20), quantification (5), dimensionality reduction/clustering (3), alignment/mapping (1)

## Papers

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: 38 https://github.com/lhqing/ALLCools Cellpose Stringer et al.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Evidence: Briefly, after maximum intensity projection of the 3D data, cells are segmented in 2D using Cellpose.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### Pan-cancer proteogenomics characterization of tumor immunity. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.027 | PMCID: PMC10988632 | PMID: 38359819
- Evidence: Initially, cells were segmented at the whole-slide level utilizing the Cellpose cyto model.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, Enrichr] -> differential/statistical testing [GSVA, SciPy] -> machine learning [R] -> visualisation [GSVA] -> stage not stated [Cellpose, scikit-image]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: Segmentation was then performed using Cellpose 61 with the TissueNet model, allowing identification and segmentation of individual cells ( Figure S5E ).
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Cell segmentation was performed using Cell Boundary Stain signals and an on-board deep learning-based segmentation algorithm (Cellpose v1).
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Perturb-Multimodal: A platform for pooled genetic screens with imaging and sequencing in intact mammalian tissue. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.022 | PMCID: PMC12324982 | PMID: 40513557
- Evidence: Cell segmentation was accomplished using a custom Cellpose model that was trained on images of polyA staining for cytoplasm + nucleus, and Na+/K+ ATPase staining for membrane.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose, XGBoost] -> stage not stated [AnnData, Scanpy]

### Fos ensembles encode and shape stable spatial maps in the hippocampus. (Nature 2022)

- DOI: 10.1038/s41586-022-05113-1 | PMCID: PMC9452297 | PMID: 36002569
- Evidence: Cre probability maps were produced from aligned Cre–GFP images using Cellpose 75 .
- Full pipeline: alignment/mapping [Cellpose] -> registration [Suite2p]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Evidence: Automated segmentation of GFP + cells was performed using a neural network model fine-tuned on manually annotated images using CellPose 62 .
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06812-z | PMCID: PMC10719114 | PMID: 38092916
- Evidence: In brief, cells were segmented based on DAPI and PolyT staining using Cellpose 141 .
- Full pipeline: quantification [UMAP] -> normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [Cellpose, Jupyter, WGCNA, limma, scDblFinder]

### Molecularly defined and spatially resolved cell atlas of the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06808-9 | PMCID: PMC10719103 | PMID: 38092912
- Version used: **2.0**
- Evidence: We performed cell segmentation using the DAPI and total polyA-mRNA signals and a deep learning-based cell segmentation algorithm (Cellpose 2.0) 66 , 67 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose v2.0] -> stage not stated [CellChat, scDblFinder, scikit-learn]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: We trained two Cellpose 43 models to segment NLS–mTagBFP2-labelled nuclei and Sst- RNA-labelled cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: Cells were segmented from maximum-projection fluorescence images using Cellpose 69 .
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Version used: **2.0.4**
- Evidence: Segmentation Cellpose (v.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: For cell segmentation, we utilized a scalable algorithm that leverages CellPose 67 (v3.0) as the segmentation method.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: 3 was performed using a custom-trained Cellpose model 56 .
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: Nuclear segmentation was carried out on the DAPI signal of the first round of imaging using the Cellpose algorithm 68 with the ‘nuclei’ neural network model.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **2.2.2**
- Evidence: Nuclei (DAPI) and TUNEL + nuclei were segmented with Cellpose 2.2.2 68 and counted in the vSVZ and striatum.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Spatially clustered type I interferon responses at injury borderzones. (Nature 2024)

- DOI: 10.1038/s41586-024-07806-1 | PMCID: PMC11374671 | PMID: 39198639
- Evidence: Single mRNA molecules were computationally decoded, and the total transcript signal and DAPI nuclear stain were used to perform cell segmentation with machine learning algorithm Cellpose 52 .
- Full pipeline: quality control [Scanpy, Squidpy] -> normalisation [ImageJ, Scanpy, Seurat, Squidpy] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose, R, SoupX]

### Recognition and control of neutrophil extracellular trap formation by MICL. (Nature 2024)

- DOI: 10.1038/s41586-024-07820-3 | PMCID: PMC11390483 | PMID: 39143217
- Evidence: Fluorescence quantification was conducted by segmenting the DAPI channel using QuPath software (version 0.4.3) with the Cellpose extension ( https://github.com/BIOP/qupath-extension-cellpose ).
- Full pipeline: quantification [Cellpose, QuPath]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Evidence: We segmented the cells in the monolayer with CellPose 53 using the bright-field channel as input.
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Dot counting to determine the transcript numbers for each FOV was performed with FISHQuant 83 using the automatic thresholding function and the cell number was determined by segmenting and counting the nuclei using CellPose 84 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **2.0**
- Evidence: For determining colocalization between Pil1–GFP and Nce102–mScarlet-I, cells were first segmented using Cellpose v.2.0 76 .
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Evidence: MERFISH data processing and analysis MERFISH imaging data were processed using the MERlin pipeline 80 with cell segmentation using CellPose 81 .
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: To create 4D rendering of individual hepatocytes from the mTmG mice, registered images were first imported in Google drive and the online platform ZerocostDL4mic 38 was used to perform Cellpose segmentation 39 on the eGFP (hepatocytes) channel.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **1.0.2**
- Evidence: Cellpose (v.1.0.2) 74 was used to perform image segmentation to determine the boundaries of cells and nuclei.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Florigen activation complex forms via multifaceted assembly in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-025-09704-6 | PMCID: PMC12711580 | PMID: 41225013
- Version used: **2.2.3**
- Evidence: Single-cell nuclear quantification of FD–FT fluorescence signal Individual confocal images of gFT ::FT–mVenus and gFD ::mScarlet1–FD were processed using Cellpose (2.2.3) 67 , 68 and Matlab (MathWorks (2022); MATLAB v.9.13.0 (R2022b)).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [Cellpose v2.2.3] -> stage not stated [AlphaFold, ColabFold, IQ-TREE v1.5.5]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: Vizgen’s post-processing tool was then applied to obtain the cell segmentation on the basis of the DAPI staining using the Cellpose algorithm.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Version used: **2.0**
- Evidence: For cell segmentation, we used an in-house model to segment cells by applying the human-in-the-loop approach introduced in Cellpose (v.2.0) 87 .
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Evidence: CODEX data clustering Whole-cell segmentation was performed with Cellpose 100 using the Cytoplasm model cyto.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Evidence: ROBs and corresponding normal acrocentric chromosomes were identified using centromere FISH signals and segmented manually or with a Cellpose model trained on a combination of the DAPI and centromere signals.
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Version used: **2.0**
- Evidence: Segmentation of nuclei and cytoplasms was performed using Cellpose (v2.0) 70 using the cyto2 model.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: For fixed z -stack images, NeuN-positive cell bodies were segmented in 3D using the pre-trained cyto2 model (Cellpose 67 ).
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Single-cell transcriptomic and genomic changes in the ageing human brain. (Nature 2025)

- DOI: 10.1038/s41586-025-09435-8 | PMCID: PMC12527935 | PMID: 40903571
- Evidence: The Vizgen post-processing tool (VPT, Vizgen) was used to improve cell segmentation with a combination of pre-filtering with a Gaussian filter and the CellPose algorithm.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Cellpose, GATK v4.1.8.1, Picard, Seurat]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Version used: **2.0.5**
- Evidence: Data acquisition and image processing were conducted using an in-house spatial molecular imaging data-processing pipeline 45 . z -stack images were collected, and cell segmentation was performed using Cellpose (v.2.0.5), with robustness evaluated through comparison to Baysor (v.0.6.0).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Version used: **2.0**
- Evidence: Spinal neurons were first segmented using Cellpose 2.0.
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: To quantify the co-occurrence of pixel-level clusters within cell-level metaclusters, we first applied the Cellpose 39 segmentation model using the parameters model_type = “nuclei” and diameter = 30 to the pre-processed DRAQ5 channel of each image.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: Nucleus and cell segmentations were performed using Cellpose 78 , and fluorescence intensity and morphology features were extracted.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: This pipeline consisted of median-based denoising, background correction, Cellpose deep-learning segmentation for cells and nuclei, intensity threshold segmentation for condensates, particle finder and size and sphericity filters.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Evidence: Nucleus segmentation and MERFISH data processing Automated segmentation was performed on the DAPI channel using a custom CellPose model 23 , 24 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Spatial data analysis The detection of cell boundaries was performed with CellPose 56 .
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08885-4 | PMCID: PMC12158776 | PMID: 40240610
- Version used: **2.0**
- Evidence: Outlines of all cells per biopsy were identified in an unbiased way by using Cellpose v.2.0 with the default cyto2 model based on anti-pan-Cadh stains 42 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, scikit-learn] -> differential/statistical testing [GSEA, limma] -> stage not stated [Cellpose v2.0, STRING db]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: We trained a Cellpose 87 , 88 ( https://cellpose.readthedocs.io ; v.3.0.8) model to identify Fos + cells in the maximum-intensity projections using eight manually corrected examples, and then used this model to identify Fos + cells in the remaining images.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Intrinsic electrical activity drives small-cell lung cancer progression. (Nature 2025)

- DOI: 10.1038/s41586-024-08575-7 | PMCID: PMC11922742 | PMID: 39939778
- Evidence: The TrackMate plugin and Cellpose detector pretrained models cyto and cyto2 were used for automated segmentation of cells and tracking during the time lapse recorded for each field of view.
- Full pipeline: alignment/mapping [RSEM] -> machine learning [Cellpose, TrackMate] -> visualisation [QuPath v0.5.0] -> stage not stated [Enrichr, GSEA, ImageJ]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: A Cellpose 40 cell-segmentation model was fine-tuned to segment nuclei in the high-resolution VisiumHD H&E image.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: These regions were loaded into Cellpose 62 , a deep-learning-based segmentation tool, and a custom segmentation model was trained by manually segmenting nucleus objects across ten 2,000 × 2,000 pixel regions in the Cellpose GUI.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Version used: **1.0.2**
- Evidence: Cell segmentation and MERFISH data preprocessing Segmentation of cells was performed using Cellpose (1.0.2) through Vizgen’s laboratory service.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: For cell segmentation and counting, parenchyma cells within the identified regions were segmented using Cellpose 86 , using the cyto2 model with optimized parameters (minimum cell area, 6,400 pixels; cell probability threshold, 2) to ensure accurate detection.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### A spatial atlas of the healthy human liver from live donors. (Nature 2026)

- DOI: 10.1038/s41586-026-10377-y | PMCID: PMC13216088 | PMID: 41986723
- Evidence: Cellpose software version 1.x was used to segment cells from the nuclear DAPI signal.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> machine learning [QuPath] -> visualisation [Scanpy v1.10.0] -> stage not stated [AnnData, Cellpose, GSEA]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: Mito-GFP within a cell were segmented using a custom-trained model in Cellpose 94 .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: ( b ) Zoomed view near a blood vessel (BV) illustrating cell segmentation by Cellpose; each segmented cell (geometric bin) is colored by a cell cluster, with MIDs aggregated within its cell boundary.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Version used: **2.2.3**
- Evidence: Cell segmentation was performed on bright-field images using a custom-trained model of Cellpose (v.2.2.3) 62 , 63 .
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **2.0**
- Evidence: Cellular segmentation was performed with CellProfiler using the Cellpose 2.0 TissueNet segmentation model.
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Germ cells were segmented using Cellpose-SAM 40 on the channel containing the nuclear piRNA pathway protein stain (version 1.1.1 of the plugin, https://github.com/COIL-Edinburgh/ROI_NucleusColocalisation/releases/tag/1.1.1 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Once the images were stitched and corrected for misalignment, we used the DAPI signal to segment nuclei with CellPose 100 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Inhibitory PD-1 axis maintains high-avidity stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09440-x | PMCID: PMC12727512 | PMID: 41299179
- Evidence: Single-cell segmentation was performed with a modified version of Stardist3D 64 on nuclei or with Cellpose 65 on membrane markers.
- Full pipeline: quantification [seaborn] -> normalisation [Matplotlib, scikit-learn] -> dimensionality reduction/clustering [Matplotlib, scikit-learn] -> visualisation [Matplotlib, scikit-image, scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2, napari]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Evidence: Cellpose (v.2 or v.3) 67 was used for cell segmentation as follows.
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### An ATP-gated molecular switch orchestrates human mRNA export. (Nature 2026)

- DOI: 10.1038/s41586-025-09832-z | PMCID: PMC12823420 | PMID: 41198879
- Evidence: For each sample, we prepared four replicates and collected five images each, which were analysed using a Python pipeline using Stardist 100 and Cellpose 101 for image segmentation of the nucleus and cytoplasm.
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Cellpose, Coot, RELION v3.1]

### Two light sensors decode moonlight versus sunlight to adjust a plastic circadian/circalunidian clock to moon phase. (PNAS 2022)

- DOI: 10.1073/pnas.2115725119 | PMCID: PMC9295771 | PMID: 35622889
- Evidence: Nuclei were segmented using Cellpose ( 54 ) on the DAPI channel images.
- Full pipeline: stage not stated [Cellpose, Fiji, ImageJ]

### Topographic map formation and the effects of NMDA receptor blockade in the developing visual system. (PNAS 2022)

- DOI: 10.1073/pnas.2107899119 | PMCID: PMC8872792 | PMID: 35193956
- Evidence: Cell body ROIs were automatically segmented using Cellpose ( 66 ) and then manually processed to remove nonneuronal elements, such as melanophores and radial glia somata. ΔF/F 0 responses were averaged within each ROI; then, optimal stimulus position for each ROI was calculated in same way as pixelwise optimal stimulus positions.
- Full pipeline: stage not stated [Cellpose]

### A synergy between mechanosensitive calcium- and membrane-binding mediates tension-sensing by C2-like domains. (PNAS 2022)

- DOI: 10.1073/pnas.2112390119 | PMCID: PMC8740744 | PMID: 34969839
- Evidence: Specifically, custom Python 3.7 scripts were written based on the Numpy ( 36 ), Scipy ( 37 ), Scikit-image ( 38 ), Allen Cell Structure Segmenter ( 39 ), Cellpose ( 40 ) and Napari libraries ( 41 ).
- Full pipeline: stage not stated [Cellpose, Conda, NumPy, PyMOL, Python v3.7, SciPy]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: First, individual cells were segmented using Cellpose ( 68 ) with custom-trained models for detection of nuclei labeled with SPY650-DNA (HEK293T, MDA-MB468 cells) or entire cells in bright-field images (Jurkat cells).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### Cellular segregation in cocultures is driven by differential adhesion and contractility on distinct timescales. (PNAS 2023)

- DOI: 10.1073/pnas.2213186120 | PMCID: PMC10104523 | PMID: 37011207
- Version used: **1.0**
- Evidence: Segmentation was performed using Cellpose 1.0 ( 65 ).
- Full pipeline: dimensionality reduction/clustering [scikit-image] -> stage not stated [Cellpose v1.0, OpenCV, Python]

### eLemur: A cellular-resolution 3D atlas of the mouse lemur brain. (PNAS 2024)

- DOI: 10.1073/pnas.2413687121 | PMCID: PMC11648901 | PMID: 39630862
- Version used: **2.0**
- Evidence: To benchmark our model against Cellpose 2.0, we followed the hyperparameters described in the original paper ( 56 ) to fine-tune specialist Cellpose models, utilizing our two distinct training datasets for DAPI/NeuN and PV cell types.
- Full pipeline: alignment/mapping [ANTs, Python] -> normalisation [ANTs, Python] -> registration [ANTs, Python] -> machine learning [Cellpose v2.0]

### Regulation of intercellular viscosity by E-cadherin-dependent phosphorylation of EGFR in collective cell migration. (PNAS 2024)

- DOI: 10.1073/pnas.2405560121 | PMCID: PMC11406304 | PMID: 39231206
- Evidence: We used Cellpose ( 46 ) for the cell segmentation.
- Full pipeline: quantification [ImageJ] -> stage not stated [Cellpose, TrackMate]

### Role of RNA structural plasticity in modulating HIV-1 genome packaging and translation. (PNAS 2024)

- DOI: 10.1073/pnas.2407400121 | PMCID: PMC11331132 | PMID: 39110735
- Evidence: Images were processed and analyzed using the Fiji/ImageJ2 software ( 76 ) with the assistance of BaSiC ( 77 ) and Cellpose ( 56 ) plugins.
- Full pipeline: stage not stated [Cellpose]

### Spatial molecular profiling of mixed invasive ductal and lobular breast cancers reveals heterogeneity in intrinsic molecular subtypes, oncogenic signatures, and mutations. (PNAS 2024)

- DOI: 10.1073/pnas.2322068121 | PMCID: PMC11295029 | PMID: 39042692
- Evidence: Single-cell segmentation was performed using Cellpose ( 90 ) and intensity measurements were extracted using scikit-image ( 91 ).
- Full pipeline: differential/statistical testing [GSVA] -> stage not stated [Cellpose, scikit-image]

### Multiplexed in situ hybridization reveals distinct lineage identities for major and minor vein initiation during maize leaf development. (PNAS 2024)

- DOI: 10.1073/pnas.2402514121 | PMCID: PMC11252972 | PMID: 38959034
- Version used: **2.0**
- Evidence: ( B ) Representative transverse section of a maize shoot stained with Calcofluor and segmented with CellPose 2.0.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0, ImageJ]

### A PAK family kinase and the Hippo/Yorkie pathway modulate WNT signaling to functionally integrate body axes during regeneration. (PNAS 2024)

- DOI: 10.1073/pnas.2321919121 | PMCID: PMC11098123 | PMID: 38713625
- Evidence: To measure the coexpression of these genes we segmented the nuclei using the Fiji plugin Cellpose ( 65 ) on high-resolution confocal images.
- Full pipeline: stage not stated [Cellpose]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: Segmentation was performed using Cellpose ( 58 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### Single-nucleus and spatial transcriptomics reveal the cell populations of intercalary meristems in bamboo. (PNAS 2025)

- DOI: 10.1073/pnas.2511701122 | PMCID: PMC12745733 | PMID: 41410774
- Evidence: ( J ) CellPose-based automated segmentation for high-resolution cell identification.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose]

### S-cone-specific circuitry in the outer plexiform layer of a cone-dominant mammal. (PNAS 2025)

- DOI: 10.1073/pnas.2504954122 | PMCID: PMC12674004 | PMID: 41325528
- Evidence: S-cone and photoreceptor densities were obtained from selected locations using a semiautomated method combining ImageJ ( 86 ) and CellPose ( 87 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [Cellpose, ImageJ]

### Acoustic printing of conductive polymers. (PNAS 2025)

- DOI: 10.1073/pnas.2509652122 | PMCID: PMC12685109 | PMID: 41284884
- Version used: **1.0**
- Evidence: The diameter of the inner aqueous core and oil shell was quantified with Cellpose 1.0 ( 45 ) in images acquired with the 50× objective.
- Full pipeline: quantification [Cellpose v1.0]

### Genome integrity relies on rapid recycling of DNA Pol III in bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2511725122 | PMCID: PMC12663971 | PMID: 41264243
- Evidence: This cell mask was created using ilastik and Cellpose ( 58 , 59 ).
- Full pipeline: stage not stated [Cellpose, ilastik]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: Cell segmentation was performed using the neural network-based algorithm Cellpose ( 97 , 98 ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### Temporal and spatial coordination of DNA segregation and cell division in an archaeon. (PNAS 2025)

- DOI: 10.1073/pnas.2513939122 | PMCID: PMC12557731 | PMID: 41091768
- Evidence: Cellular segmentation and tracking were performed using the “cyto2” model implemented in Cellpose ( 60 ), employing a diameter parameter of 22 and utilizing both available channels.
- Full pipeline: quantification [Python] -> visualisation [Python] -> stage not stated [Cellpose, ImageJ, scikit-image]

### Single-cell lysis patterns morphogenesis of eDNA in the matrix of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt; biofilms. (PNAS 2025)

- DOI: 10.1073/pnas.2514210122 | PMCID: PMC12541396 | PMID: 41052342
- Evidence: After comparing deep learning methods, we chose Cellpose-SAM ( 46 ).
- Full pipeline: machine learning [Cellpose]

### Heterogeneity in the coordination of delta cells with beta cells is driven by both paracrine signals and low-density Cx36 gap junctions. (PNAS 2025)

- DOI: 10.1073/pnas.2504151122 | PMCID: PMC12478151 | PMID: 40956879
- Version used: **3.1.1.1**
- Evidence: Images from mTmG mice stained for Cx36, insulin, and somatostatin were first segmented using a custom-trained model in Cellpose 3.1.1.1.
- Full pipeline: machine learning [Cellpose v3.1.1.1] -> stage not stated [Python]

### Single-cell transcriptome combined with genetic tracing reveals a roadmap of fibrosis formation during proliferative vitreoretinopathy. (PNAS 2025)

- DOI: 10.1073/pnas.2424487122 | PMCID: PMC12452882 | PMID: 40920930
- Evidence: By analyzing the shape and size using Cellpose ( 37 ), we found tdT + cells displayed greater variability in shape and were larger in both area and perimeter post-PVR ( Fig.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Monocle, Slingshot] -> visualisation [UMAP] -> stage not stated [Cellpose, GSEA]

### Increased excitatory synapse size in hippocampal place cells compared to silent cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505322122 | PMCID: PMC12167973 | PMID: 40472030
- Evidence: Therefore, to identify the inactive neurons we used Cellpose ( 42 ) on the mean image output of Sute2p to segment all the cells in the FOV.
- Full pipeline: registration [Suite2p] -> stage not stated [Cellpose, ImageJ, Python, SciPy]

### Flocking and giant fluctuations in epithelial active solids. (PNAS 2025)

- DOI: 10.1073/pnas.2421327122 | PMCID: PMC12037054 | PMID: 40249776
- Evidence: Nuclei were first segmented by Cellpose, which were then tracked using the Trackmate plugin of ImageJ.
- Full pipeline: stage not stated [Cellpose, ImageJ]

### Pulsatile basal gene expression as a fitness determinant in bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2413709122 | PMCID: PMC12012556 | PMID: 40193613
- Evidence: Bacteria segmentation was carried out using Cellpose (47) .
- Full pipeline: stage not stated [Cellpose, ImageJ]

### Colony pattern multistability emerges from a bistable switch. (PNAS 2025)

- DOI: 10.1073/pnas.2424112122 | PMCID: PMC12002352 | PMID: 40184178
- Evidence: S14 ), a deep learning-based cell segmentation algorithm, Cellpose ( 60 ), was utilized with the pretrained model “bact_phase_cp3.” Fluorescence Intensity Measurement.
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9] -> quantification [SAMtools v1.9] -> machine learning [Cellpose] -> stage not stated [ImageJ v1.53c]

### Matrix degradation enhances stress relaxation, regulating cell adhesion and spreading. (PNAS 2025)

- DOI: 10.1073/pnas.2416771122 | PMCID: PMC12002262 | PMID: 40131951
- Evidence: Trackmate-Cellpose/Fiji plugin ( 62 ) was used for the analysis.
- Full pipeline: stage not stated [Cellpose]

### Cell extrusion drives neural crest cell delamination. (PNAS 2025)

- DOI: 10.1073/pnas.2416566122 | PMCID: PMC11929498 | PMID: 40063802
- Evidence: Cell density was measured in each region by quantification of cells based on DAPI staining of nuclei using Cellpose ( 76 ).
- Full pipeline: quantification [Cellpose]

### Phased ERK responsiveness and developmental robustness regulate teleost skin morphogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2410430122 | PMCID: PMC11912398 | PMID: 40042905
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Image processing was performed using Fiji, Cellpose, iLastik, Trackmate, and custom Matlab (MathWorks) R2022b software codes.
- Full pipeline: stage not stated [Cellpose]

### BIN1 reduction ameliorates <i>DNM2</i>-related Charcot-Marie-Tooth neuropathy. (PNAS 2025)

- DOI: 10.1073/pnas.2419244122 | PMCID: PMC11912451 | PMID: 40042903
- Evidence: Fiber size distribution and circularity were determined on TA sections stained with HE, using CellPose ( 65 ) software to segment individual fibers and Fiji ( 66 ) to calculate fibers MinFeret diameter and circularity.
- Full pipeline: stage not stated [Cellpose]

### Adeno-associated viruses for efficient gene expression in the axolotl nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2421373122 | PMCID: PMC11912378 | PMID: 40042904
- Version used: **2.0**
- Evidence: Nuclei on cryosections were counted using Cellpose 2.0 using the CPx model.
- Full pipeline: stage not stated [Cellpose v2.0]

### Spatial Patterning Analysis of Cellular Ensembles (SPACE) finds complex spatial organization at the cell and tissue levels. (PNAS 2025)

- DOI: 10.1073/pnas.2412146122 | PMCID: PMC11831171 | PMID: 39903116
- Version used: **2.0**
- Evidence: The JOJO nuclear stain and CD45 membrane stain were supplied to Cellpose 2.0 ( 37 ) to obtain a segmentation mask of individual cells.
- Full pipeline: stage not stated [Cellpose v2.0, ImageJ, Nextflow, R]

### A broadly conserved gram-positive lipoprotein regulates cell elongation. (PNAS 2026)

- DOI: 10.1073/pnas.2610431123 | PMCID: PMC13321084 | PMID: 42335227
- Evidence: These cells were segmented using the Cellpose cyto3 algorithm in mAIcrobe ( 57 ) based on the cytoplasmic GFP marker, and their morphology measured using the precomputed S. aureus membrane epifluorescence model.
- Full pipeline: stage not stated [AlphaFold, Cellpose]

### ERK builds a population of short-lived nascent adhesions that produce persistent edge protrusion and cell migration. (PNAS 2026)

- DOI: 10.1073/pnas.2525452123 | PMCID: PMC13271172 | PMID: 42296347
- Evidence: For talin mutant assays, mNeonGreen-expressing cells were manually selected for inclusion after tracking in a custom MATLAB cell tracking app that combines the Linear Assignment Cell Tracker ( https://github.com/Biofrontiers-ALMC/cell-tracking-toolbox ) for track calculation and Cellpose ( https://www.cellpose.org/ ) for 2D segmentation.
- Full pipeline: quantification [Fiji, ImageJ] -> stage not stated [Cellpose]

### 3D epithelial cell topology tunes signaling range to promote precise patterning. (PNAS 2026)

- DOI: 10.1073/pnas.2522727123 | PMCID: PMC13167770 | PMID: 42090248
- Evidence: Images were segmented using Cellpose ( 25 ) using model:cyto 3 and the following parameters: cell diameter = 60 (70 for Mbs-RNAi), flow threshold = 0.4, cell probability threshold = 0 and stitch threshold = 0.4).
- Full pipeline: stage not stated [Cellpose, napari]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Version used: **3.1.0**
- Evidence: Nuclei segmentation for in vitro samples Cellpose (v3.1.0) was used to segment cell nuclei in 3-D based on DAPI signal ( 98 ).
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

### Deep-tissue transcriptomics and subcellular imaging at high spatial resolution. (Science 2025)

- DOI: 10.1126/science.adq2084 | PMCID: PMC12005972 | PMID: 39977545
- Evidence: Nucleus segmentation was performed with Cellpose 2 ( 22 ), and single-molecule spot detection used RS-FISH ( 21 ).
- Full pipeline: alignment/mapping [BigStitcher] -> registration [BigStitcher, Nextflow] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose]

