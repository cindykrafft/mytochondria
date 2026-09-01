# StarDist

- **Category:** imaging
- **Papers in survey:** 22
- **Journals:** Nature (13), PNAS (7), Cell (2)
- **Years:** 2021 (1), 2022 (2), 2023 (3), 2024 (5), 2025 (8), 2026 (3)
- **Versions named:** 0.3.0 (1)
- **Pipeline stages it appears in:** machine learning (11), normalisation (1), quantification (1)

## Papers

### Parental genome unification is highly error-prone in mammalian embryos. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.013 | PMCID: PMC8162515 | PMID: 33964210
- Evidence: We used the manual annotation for training two machine learning models (StarDist) ( Schmidt et al., 2018 ) to predict labeling masks for nuclei and nucleoli over time.
- Full pipeline: differential/statistical testing [R] -> machine learning [StarDist] -> stage not stated [ImageJ, QuPath v0.2.3, TrackMate]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Akoya PhenoCycler Cell segmentation was performed using StarDist in QuPath (v0.5.0) with a custom Groovy script.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Evidence: Nuclear segmentation was carried out using StarDist, a method for nuclear detection based on the U-Net neural network architecture 56 , 57 .
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### Emergence of large-scale cell death through ferroptotic trigger waves. (Nature 2024)

- DOI: 10.1038/s41586-024-07623-6 | PMCID: PMC11639682 | PMID: 38987590
- Evidence: 11c,e ) were quantified in whole cells by nuclear segmentation using the ImageJ StarDist plugin, followed by nuclear dilation 7 pixels from the nuclear border.
- Full pipeline: alignment/mapping [ImageJ v1.54] -> quantification [StarDist]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Evidence: For segmentation of epithelioid nuclei, a pre-trained StarDist 89 model (he_heavy_augment.zip) was downloaded from https://github.com/stardist/stardist-imagej/tree/master/src/main/resources/models/2D , and an inference instance was deployed using Groovy across the tiles in QuPath, built from source with Tensorflow 90 , with a minimum detection threshold of 0.5.
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: All image analysis was undertaken in QuPath (v0.3.0) 41 with StarDist nuclei detection extension 42 .
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Evidence: Recombined cells were segmented using StarDist with the default parameters ( https://github.com/stardist ) on the GFP channel of mini-colon images.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: To segment images, we used the ImageJ plugin StarDist 66 with default parameters (model – versatile, normalize image – yes, percentile low – 1, percentile high – 99.8, probability – 0.5, overlap threshold – 0.4), which automatically detects cells using neural network models with star-convex shape priors.
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: Segmentation of primary nuclei was done in QuPath v.0.5.1 using the StarDist algorithm on the DAPI channel 84 .
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Evidence: For image analysis, the whole section of the tissue was divided into a tumour compartment, characterized by the nets of tumour cells, and the stroma compartment, the tissue between the tumour nets; and then the individual cell boundaries were determined using the pretrained StarDist algorithm within QuPath 63 .
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Evidence: Subsequently, the StarDist 61 algorithm, using the pretrained 2D_versatile_fluo model, was used for segmentation.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### A travelling-wave strategy for plant-fungal trade. (Nature 2025)

- DOI: 10.1038/s41586-025-08614-x | PMCID: PMC11882455 | PMID: 40011773
- Evidence: Unique colours are automatically attributed to each nucleus via the trained StarDist model.
- Full pipeline: machine learning [StarDist] -> visualisation [Matplotlib] -> stage not stated [SciPy, scikit-image, seaborn]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **0.3.0**
- Evidence: StarDist v.0.3.0, a tool plug-in on FIJI, was used to count the number of nuclei.
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: A StarDist 3D segmentation model was then trained using a manually labelled training dataset created from the synthetic data 68 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: For downstream analysis, cells were segmented on the basis of the DAPI signal using the StarDist plugin in ImageJ (US National Institutes of Health) and the donut algorithm in MACS iQ View.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Mechanical coupling of supracellular stress amplification and tissue fluidization during exit from quiescence. (PNAS 2022)

- DOI: 10.1073/pnas.2201328119 | PMCID: PMC9371707 | PMID: 35914175
- Evidence: First, mitotic cells in a set of images were annotated and used as input data for development of a deep learning model using the StarDist (2D) network, available in the CoLab notebook ( 64 ).
- Full pipeline: registration [Fiji, ImageJ] -> machine learning [StarDist]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Evidence: Briefly, cells were detected using a pretrained StarDist network ( 40 ) and scored based on signal in the 3,3′-Diaminobenzidine (DAB) channel after color deconvolution ( 41 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Geometry-mediated bridging drives nonadhesive stripe wound healing. (PNAS 2023)

- DOI: 10.1073/pnas.2221040120 | PMCID: PMC10161107 | PMID: 37098071
- Evidence: Nuclei identification was done by ImageJ StarDist plugin.
- Full pipeline: alignment/mapping [ImageJ] -> simulation/modelling [ImageJ] -> stage not stated [CellProfiler, StarDist]

### Chloroplasts in plant cells show active glassy behavior under low-light conditions. (PNAS 2023)

- DOI: 10.1073/pnas.2216497120 | PMCID: PMC9934296 | PMID: 36638210
- Evidence: The resulting image shows white circular spots, reminiscent of nuclei training data for the StarDist versatile model ( 81 ).
- Full pipeline: machine learning [StarDist]

### Artificial dynamic structure ensemble-guided rational design of a universal RNA aptamer-based sensing tag. (PNAS 2024)

- DOI: 10.1073/pnas.2414793121 | PMCID: PMC11670126 | PMID: 39705306
- Evidence: For E. coli image analysis, the cell segmentation algorithm StarDist in ImageJ (FIJI) v.1.54f was used and analyzed based on previous work ( 54 ).
- Full pipeline: stage not stated [CellProfiler v4.2.4, ImageJ, StarDist]

### Optimal disk packing of chloroplasts in plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2511696122 | PMCID: PMC12582306 | PMID: 41123999
- Evidence: Chloroplasts were segmented using StarDist ( 112 ).
- Full pipeline: stage not stated [StarDist]

### Therapeutic CD8&lt;sup&gt;+&lt;/sup&gt; T cell tissue retention and immunomodulation during ART interruption fail to prevent SIV rebound. (PNAS 2025)

- DOI: 10.1073/pnas.2501037122 | PMCID: PMC12377730 | PMID: 40811471
- Evidence: Cell segmentation was obtained using StarDist script on whole sections and region of interest were manually selected to define B cell follicles.
- Full pipeline: stage not stated [QuPath, StarDist]

