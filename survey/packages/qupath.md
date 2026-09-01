# QuPath

- **Category:** imaging
- **Papers in survey:** 138
- **Journals:** Nature (83), PNAS (44), Cell (8), Science (3)
- **Years:** 2021 (4), 2022 (13), 2023 (21), 2024 (22), 2025 (46), 2026 (32)
- **Versions named:** 0.5.1 (12), 0.2.3 (7), 0.3.2 (6), 0.4.4 (5), 0.4.3 (4), 0.6.0 (3), 0.3.0 (3), 0.5.0 (2), 0.4.1 (2), 0.5 (1)
- **Pipeline stages it appears in:** quantification (41), machine learning (5), visualisation (2), differential/statistical testing (2), normalisation (1), quality control (1), variant calling (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Evidence: ...90006 AssayMAP Fe(III)-NTA cartridges Agilent G5496-60085 EASY-nLC 1200 Thermo Fisher Scientific LC140 Image Cycler MM3 (TIC) MelTec GmbH & Co.KG N/A QuPath Bankhead et al., 2017 0.2.3 ZEN 3.0 black edition Carl Zeiss AG N/A InForm Akoya Biosciences N/A GraphPad Prism GraphPad Software Version 5.01 Resource availability Lead contact Further information and requests for resources and reagents shoul...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Parental genome unification is highly error-prone in mammalian embryos. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.013 | PMCID: PMC8162515 | PMID: 33964210
- Version used: **0.2.3**
- Evidence: ...ware and algorithms Prism 8 GraphPad Software N/A Fiji (Fiji Is Just ImageJ) Schindelin et al., 2012 PMID: 22743772 Imaris version 9.2.1 Bitplane N/A QuPath (0.2.3) ( Bankhead et al., 2017 ) N/A R ( R Development Core Team, 2019 ) N/A Zen 2.3 (Blue edition) Zeiss N/A Other Zeiss LSM800 microscope Zeiss N/A Zeiss LSM880 microscope Zeiss N/A Zeiss LSM900 microscope Zeiss N/A GERI time lapse system G...
- Full pipeline: differential/statistical testing [R] -> machine learning [StarDist] -> stage not stated [ImageJ, QuPath v0.2.3, TrackMate]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Version used: **0.2.3**
- Evidence: (2021) DOI: 10.1038/s41586-021-03791-x Software and algorithms R version 4.0.5 base packages The R Foundation https://www.rstudio.com/products/rstudio/download/ R version 4.0.5 ggplot2 package The R Foundation https://cran.r-project.org/web/packages/ggplot2/index.html QuPath version 0.2.3 Bankhead et al.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: Slides were mounted in ProLong Diamond, imaged with a Zeiss LSM780 confocal microscope (Carl Zeiss, Oberkochen, Germany) with spectral detector and using spectral unmixing and analyzed using ImageJ and QuPath software.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Evidence: 89 https://imagej.net/Fiji QuPath 90 https://qupath.github.io/ Adobe Photoshop Adobe https://www.adobe.com/au/products/photoshop.html Adobe After Effects Adobe https://www.adobe.com/au/products/aftereffects/campaign/pricing.html Adobe Illustrator CC Adobe https://www.adobe.com/uk/products/illustrator.html Imaris, 9.8.9 Oxford Instruments https://imaris.oxinst.com/versions/9-8 MATLAB MathWorks http...
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: To determine changes in tumor size, tumors were manually segmented using QuPath software.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Safe immunosuppression-resistant pan-cancer immunotherapeutics by velcro-like density-dependent targeting of tumor-associated carbohydrate antigens. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.001 | PMCID: PMC12767472 | PMID: 41005308
- Evidence: ...25216 C57BL/6J Jackson laboratory 000664 Software and algorithms Gensys Imaging analysis Gensys N/A Flowjo FlowJo LLC N/A GraphPad Prism GraphPad N/A QuPath QuPath N/A Xenogen IVIS Living Image 4.5.5 PerkinElmer N/A Aura Imaging software Spectral Imaging N/A Microsoft Excel Microsoft N/A Microsoft PowerPoint Microsoft N/A Biorender biorender.com N/A Highlights “Velcro-like” lectin targeting of hig...
- Full pipeline: stage not stated [QuPath]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Version used: **0.5.0**
- Evidence: Akoya PhenoCycler Cell segmentation was performed using StarDist in QuPath (v0.5.0) with a custom Groovy script.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Dots located outside of nuclei were not included in this analysisFor Meg3 and NKD2 analysis of PDGFRa/b cells images were analyzed using QuPath after segmenting the nuclei and counting cells based on >1 pos. spot per imaging channel.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Version used: **0.2.3**
- Evidence: To classify regions of tumour, stroma, vasculature and necrosis, we trained an artificial neural network (ANN)-based pixel classifier using QuPath (v0.2.3) 56 , which operates on higher-order pixel features over multiple channels and scales within an image.
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Version used: **0.3.2**
- Evidence: Further quantitative analysis of tuft areas and cells (nuclei) per tuft area was performed using QuPath v0.3.2 image analysis software 48 , 49 .
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### A﻿ TMPRSS2 inhibitor acts as a pan-SARS-CoV-2 prophylactic and therapeutic. (Nature 2022)

- DOI: 10.1038/s41586-022-04661-w | PMCID: PMC9095466 | PMID: 35344983
- Evidence: Digital image analysis was performed using QuPath software 65 , 66 v.0.2.3.
- Full pipeline: stage not stated [ImageJ, QuPath]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Version used: **0.4.1**
- Evidence: Quantification of SPNs across major brain regions SPNs were quantified across the eight major brain regions (RFA, M1M2S1, S2, HY, MB, PONS and MED) using QuPath (v.0.4.1).
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **0.3.0**
- Evidence: Slides were imaged on an Aperio Versa 200 and analysed using QuPath (v.0.3.0).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Evidence: Images were analysed using QuPath and ImageJ.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### A spatially resolved timeline of the human maternal-fetal interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06298-9 | PMCID: PMC10356615 | PMID: 37468587
- Version used: **0.4.0**
- Evidence: The IHC slides were scanned using a NanoZoomer Digital Pathology Scanner 2.0RS (Hamamatsu) and analysed using QuPath (v.0.4.0).
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [limma, scikit-learn] -> stage not stated [ImageJ, Jupyter, Python, QuPath v0.4.0, R]

### Immune sensing of food allergens promotes avoidance behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06362-4 | PMCID: PMC10432274 | PMID: 37437602
- Evidence: FCER1A, EPCAM and GDF15 colocalization analysis was carried out in Qupath (QuPath Quantitative Pathology & Bioimage Analysis, v3.0) on the basis of the fluorescent threshold of cells detected by DAPI positivity.
- Full pipeline: stage not stated [ImageJ, QuPath]

### Inhibiting membrane rupture with NINJ1 antibodies limits tissue injury. (Nature 2023)

- DOI: 10.1038/s41586-023-06191-5 | PMCID: PMC10307625 | PMID: 37196676
- Evidence: Neutrophils (Ly6G-positive) were counted using QuPath (RRID: SCR_018257).
- Full pipeline: stage not stated [QuPath, scikit-image v0.19.2]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Version used: **0.3**
- Evidence: Slides were imaged using a Zeiss AxioScan slide scanner and analysed using the QuPath 0.3 source software 50 .
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Evidence: Segmentation and analysis of immunohistochemistry and immunofluorescence images was carried out using QuPath 64 .
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Adeno-associated virus 2 infection in children with non-A-E hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05948-2 | PMCID: PMC7617659 | PMID: 36996873
- Version used: **0.3.2**
- Evidence: Quantification of immune cells After scanning of the whole slide, liver tissue was outlined and the number of positively stained cells (DAB signal for immunohistochemistry or Fast Red signal for ISH) was assessed using software-assisted image analysis (QuPath, v.0.3.2) 36 .
- Full pipeline: read trimming [BWA, IQ-TREE, Trim Galore] -> alignment/mapping [BWA, IQ-TREE, MAFFT, Trim Galore] -> quantification [QuPath v0.3.2] -> differential/statistical testing [R]

### Spatial mapping of mitochondrial networks and bioenergetics in lung cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05793-3 | PMCID: PMC10033418 | PMID: 36922590
- Evidence: The threshold of positive CD 34 staining was identified using QuPath and indicated by red labeling ( c , right panel).
- Full pipeline: alignment/mapping [IMOD] -> stage not stated [ImageJ, QuPath]

### Microglia regulate central nervous system myelin growth and integrity. (Nature 2023)

- DOI: 10.1038/s41586-022-05534-y | PMCID: PMC9812791 | PMID: 36517604
- Version used: **0.3.0**
- Evidence: In brief, we used 29 kV acceleration voltage, 5 nm pixel size and 1.5 µs beam dwell time for digitization and Fiji/TrakEM2 for stitching to allow for in-depth analysis with QuPath 0.3.0.
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [QuPath v0.3.0, ggplot2 v3.3.5]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: We next used QuPath 71 v0.5 with the cellpose 72 v2.2.3 extension to segment T cells with the ‘cyto2’ model from maximum projection of CD3, CD4, CD8 and TCRγδ, with DAPI as the nuclear marker, an expected median diameter of 10 μm and excluding cells with diameters of less than 5 μm.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Version used: **0.4.3**
- Evidence: Immunostaining quantification All histological quantification was performed using QuPath (v.0.4.3; https://github.com/qupath/qupath ) 58 .
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: Quantification of FOXP3 coverage was carried out using QuPath image analysis software (v.0.5.1) 85 .
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Version used: **0.4.1**
- Evidence: Single-cell segmentation was performed within QuPath (v0.4.1) using the standard nuclear segmentation algorithm.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### CRISPR-Cas9 screens reveal regulators of ageing in neural stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07972-2 | PMCID: PMC11525198 | PMID: 39358505
- Evidence: Image analysis and quantification of immunofluorescence staining in brain sections For image analysis, we used the open-source software QuPath ( https://qupath.github.io/ ) 94 .
- Full pipeline: quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Enrichr]

### Mechanisms that clear mutations drive field cancerization in mammary tissue. (Nature 2024)

- DOI: 10.1038/s41586-024-07882-3 | PMCID: PMC11374684 | PMID: 39232148
- Evidence: Ripley analysis using QuPath 69 was performed with a custom-made script (available at https://github.com/BioImaging-NKI/qupath_ripley ).
- Full pipeline: alignment/mapping [BWA, Cutadapt] -> dimensionality reduction/clustering [Python] -> simulation/modelling [Python] -> visualisation [ImageJ, ggplot2] -> stage not stated [QuPath]

### Recognition and control of neutrophil extracellular trap formation by MICL. (Nature 2024)

- DOI: 10.1038/s41586-024-07820-3 | PMCID: PMC11390483 | PMID: 39143217
- Evidence: Fluorescence quantification was conducted by segmenting the DAPI channel using QuPath software (version 0.4.3) with the Cellpose extension ( https://github.com/BIOP/qupath-extension-cellpose ).
- Full pipeline: quantification [Cellpose, QuPath]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Quantification of metastatic foci and lesion area H&E sections were imaged on the Leica DMi8 inverted microscope, equipped with a FLEXACAM C1 12 MP CMOS camera and analysed using QuPath software 81 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Version used: **0.2.3**
- Evidence: Slides were scanned with an Aperio System and analysed with Aperio Image Scope v.12.4.0 software (Leica) and QuPath v.0.2.3 (ref.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **0.2.2**
- Evidence: Whole-slide images of tumours that met inclusion criteria (cellularity of more than 50% and DEN1 signature of more than 80%) were annotated in QuPath (v0.2.2) 88 using the polygon tool to include neoplastic tissue and excluded adjacent parenchyma, cyst cavities, processing artefacts and white space.
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### A multimodal generative AI copilot for human pathology. (Nature 2024)

- DOI: 10.1038/s41586-024-07618-3 | PMCID: PMC11464372 | PMID: 38866050
- Evidence: To evaluate PathChat, we curated PathQABench using representative high-resolution ROI images hand-selected by a board-certified pathologist from 105 H&E WSI cases using the open-source QuPath digital viewer 67 .
- Full pipeline: machine learning [PyTorch v2.0.1] -> stage not stated [Matplotlib v3.7.1, QuPath, seaborn v0.12.2]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Version used: **0.3.0**
- Evidence: All image analysis was undertaken in QuPath (v0.3.0) 41 with StarDist nuclei detection extension 42 .
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **0.2.1**
- Evidence: QuPath v.0.2.1 image analysis software was used to measure areas of labyrinth zone and whole placenta.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **0.4.3**
- Evidence: Images were taken on a Hamamatsu Nanozoomer Slide Scanning system and an Olympus VS200 slide scanner, and processed using NDP View 2 software (Hamamatsu) and QuPath (v.0.4.3) 50 , respectively.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Version used: **0.3.2**
- Evidence: The slides were then scanned on the Leica AT2 system, and the images were analysed using QuPath v.0.3.2 ( https://qupath.github.io , University of Edinburgh, Scotland).
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **0.5.1**
- Evidence: Images were analysed using QuPath (v.0.5.1).
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Evidence: All post-acquisition processing was performed using QuPath 90 .
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Integration of hunger and hormonal state gates infant-directed aggression. (Nature 2025)

- DOI: 10.1038/s41586-025-09651-2 | PMCID: PMC12675289 | PMID: 41125886
- Evidence: Brain sections were imaged on a slide scanner, and FOS + cell densities were quantified between sections from Agg + and Agg − mice using QuPath software (see the section ‘Imaging’).
- Full pipeline: quantification [QuPath] -> registration [ImageJ] -> machine learning [scikit-learn] -> stage not stated [Python v3.7]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Version used: **0.4.2**
- Evidence: Stained slides were imaged on a NanoZoomer (Hamamatsu Photonics) slide scanner and analysed with QuPath (v.0.4.2) 39 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Ribonucleotide incorporation into mitochondrial DNA drives inflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09541-7 | PMCID: PMC12629987 | PMID: 40993386
- Version used: **0.4.4**
- Evidence: In brief, 2 µm formalin-fixed paraffin-embedded sections of kidney tissue were prepared, stained, digitalized using the Ventana DP 200 slide scanner (Roche Diagnostics) and analysed using QuPath (v.0.4.4) 49 .
- Full pipeline: quantification [ImageJ] -> visualisation [ImageJ] -> stage not stated [QuPath v0.4.4]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: 1e,f ) was semi-automated using QuPath open software for bioimage analysis (v.0.5.1-x64).
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### A neuronal architecture underlying autonomic dysreflexia. (Nature 2025)

- DOI: 10.1038/s41586-025-09487-w | PMCID: PMC12571909 | PMID: 40963010
- Version used: **0.4.3**
- Evidence: Images were generated using QuPath (v0.4.3). iDISCO+ Mice underwent a 90-min colorectal distension protocol (30 s inflate then 60 s deflate repeatedly) 14 and were perfused 9 , 47 30 min later with 0.1 M PBS followed by 4% PFA (in 0.1 M PBS).
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain, QuPath v0.4.3]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: The size and number of mammospheres were analysed using QuPath software.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Version used: **0.2.3**
- Evidence: We then used QuPath v0.2.3 to quantify the overlap of FISH and immunohistochemistry signals in the maximum projection images.
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: ROI annotations were drawn in QuPath.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Evidence: Further analysis was performed using QuPath.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **0.5.1**
- Evidence: Slide scans were imported into QuPath (v.0.5.1) 80 for quality control and stain vector normalization.
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Version used: **0.5.1**
- Evidence: To evaluate p21-positive cells, full virtual slide scans were loaded into QuPath 0.5.1 (ref.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Version used: **0.4.4**
- Evidence: Experienced pathologist analysed each tissue sample using image analysis software (QuPath v.0.4.4) 62 .
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: For ORO staining quantification, 2–10 images of each sample with a ×40 objective were taken and quantification was performed using QuPath software (v0.5.1).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: IHC analysis of tumour histology was carried out using QuPath software, with the investigator blinded to the tumour genotype.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Version used: **0.5.1**
- Evidence: Quantification was performed with QuPath v0.5.1.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### PLA2G15 is a BMP hydrolase and its targeting ameliorates lysosomal disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08942-y | PMCID: PMC12158761 | PMID: 40335701
- Evidence: Histomorphometric evaluation was conducted in QuPath 56 , quantitative pathology and bioimage analysis software, v.0.4.3.
- Full pipeline: stage not stated [AlphaFold, CellProfiler v4.2.7, ChimeraX, ImageJ v2.1.0, QuPath]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: Single-cell spatial transcriptomic analysis was performed by quantifying gene counts per cell using cell segmentation using QuPath software 75 .
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Aspirin prevents metastasis by limiting platelet TXA&lt;sub&gt;2&lt;/sub&gt; suppression of T cell immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-08626-7 | PMCID: PMC12018268 | PMID: 40044852
- Evidence: Slide images were taken using a Pannoramic digital slide scanner (3DHistech) and analysed using QuPath Software.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3, QuPath]

### A hypothalamic circuit underlying the dynamic control of social homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-08617-8 | PMCID: PMC12018270 | PMID: 40011768
- Version used: **0.3.2**
- Evidence: The number of cells marked by specific and overlapping genes was measured using QuPath v.0.3.2.
- Full pipeline: stage not stated [DeepLabCut, QuPath v0.3.2]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Version used: **0.5.1**
- Evidence: Cell detection and cell classifications were performed using QuPath v.0.5.1.
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### Intrinsic electrical activity drives small-cell lung cancer progression. (Nature 2025)

- DOI: 10.1038/s41586-024-08575-7 | PMCID: PMC11922742 | PMID: 39939778
- Version used: **0.5.0**
- Evidence: The number of MCT4- and SOX1-positive cells at the TMA was calculated using QuPath 0.5.0, and 3D visualization, rendering and videos have been generated using the Imaris software.
- Full pipeline: alignment/mapping [RSEM] -> machine learning [Cellpose, TrackMate] -> visualisation [QuPath v0.5.0] -> stage not stated [Enrichr, GSEA, ImageJ]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: P14 CD8 T cell distances for IMAP representation over time were quantified using a groovy script on QuPath ( https://github.com/Goldrathlab/Spatial-TRM-paper ).
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: Quantification of RNAscope and immunostaining Images were acquired using the VS 200 microscope and analysed with QuPath.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Version used: **0.2.3**
- Evidence: The number of TLSs were determined in at least three sections using QuPath (v.0.2.3; https://qupath.github.io/ ).
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Version used: **0.5.1**
- Evidence: All cell segmentations and cell-type annotations were performed using automated pipelines in QuPath 0.5.1.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### The oestrous cycle stage affects mammary tumour sensitivity to chemotherapy. (Nature 2025)

- DOI: 10.1038/s41586-024-08276-1 | PMCID: PMC11666466 | PMID: 39633046
- Version used: **0.4.4**
- Evidence: For determination of positive cells, IHC staining was quantified using QuPath 0.4.4 (GitHub) with atomized classifiers.
- Full pipeline: quantification [Fiji v1.49k, QuPath v0.4.4] -> dimensionality reduction/clustering [ImageJ] -> differential/statistical testing [R v4.4.2] -> machine learning [QuPath v0.4.4] -> stage not stated [ggplot2, tidyverse]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Tiles of 512 × 512 pixels in size were obtained using QuPath.
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Evidence: Subcellular quantification of individual puncta per 100 μm nucleus—identified by DAPI staining—was performed for each maximum intensity projected image using QuPath software (v0.5.1) 66 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Eosinophils drive intestinal remodelling and innate defence in reproduction. (Nature 2026)

- DOI: 10.1038/s41586-026-10531-6 | PMCID: PMC13233317 | PMID: 42129565
- Evidence: For each mouse, the entire duodenum mucosa was analysed for the quantification of the mucin area (PAS and Alcian Blue-positive) with the aid of QuPath software ( https://qupath.github.io ) 53 .
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Scanpy v1.8.2]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Evidence: Digital fluorescent micrographs were analysed using the Positive Cell Detection Pipeline in QuPath 55 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Total lobes and lesion areas were defined manually and measured using QuPath open-source software (v.0.6.0).
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### A spatial atlas of the healthy human liver from live donors. (Nature 2026)

- DOI: 10.1038/s41586-026-10377-y | PMCID: PMC13216088 | PMID: 41986723
- Evidence: Single-nucleus segmentation was performed on the H&E image using the Stardist algorithm 63 implemented within QuPath, utilizing the pre-trained H&E model he_heavy_augment.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> machine learning [QuPath] -> visualisation [Scanpy v1.10.0] -> stage not stated [AnnData, Cellpose, GSEA]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **0.6.0**
- Evidence: Slides were scanned on the GeoMx Digital Spatial Profiler (Nanostring) with a ×20 0.45 numerical aperture objective and analysed using the QuPath (v.0.6.0) Instanseg extension 69 .
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Quantification of GPC5 + cells was performed in QuPath using automated cell segmentation within defined regions of interest (syncytial aggregates or membrane), with manual verification.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Scanned images were analysed using QuPath 110 (v.0.5.1) In situ hybridization (RNAscope) RNAscope was performed using RNAscope 2.5 HD Detection Reagent Red (322360, Advanced Cell Diagnostics) according to the manufacturer’s protocol.
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Evidence: Immunohistochemistry sections were scanned with a 3DHISTECH Laminar Scanner (Perkin Elmer) and quantification was done with QuPath 90 .
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **0.5.1**
- Evidence: All stained slides were scanned with the Aperio AT2 DX System (Leica) and analysed by macro-based analysis by ImageJ (1.54g) or QuPath (v.0.5.1).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Tumour-brain crosstalk restrains cancer immunity via a sensory-sympathetic axis. (Nature 2026)

- DOI: 10.1038/s41586-025-10028-8 | PMCID: PMC12935554 | PMID: 41639447
- Evidence: Tumour burden was assessed by calculating the percentage of tumour area to the total lung tissue area using the QuPath software ( https://qupath.github.io/ ); all five lobes were analysed for each mouse.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [GSEA, ImageJ, QuPath]

### Intestinal macrophages modulate synucleinopathy along the gut-brain axis. (Nature 2026)

- DOI: 10.1038/s41586-025-09984-y | PMCID: PMC12960212 | PMID: 41606336
- Evidence: All images were processed and analysed with Fiji (National Institutes of Health, NIH) and QuPath 51 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, R v4.0, SciPy, Seurat v4.3]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Evidence: Images were analysed using NIS Elements (Nikon), ImageJ (v.1.54f, National Institutes of Health), ZEN (ZEN lite, v.3.9.101, ZEISS) and QuPath-0.5.0-x64.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Version used: **0.5.1**
- Evidence: Acquired images were white-balanced and zooms and crops of regions of interest were obtained using QuPath (0.5.1) 52 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Version used: **0.6.0**
- Evidence: QuPath v.0.6.0 was used to quantify the percentages of IL-11 mNG fibroblasts in whole-colon Swiss rolls from Il11 mNG mice subjected to chronic DSS.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Version used: **0.6.0**
- Evidence: Digitized slides were further processed using QuPath (v.0.6.0) 53 .
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Decay of driver mutations shapes the landscape of intestinal transformation. (Nature 2026)

- DOI: 10.1038/s41586-025-09762-w | PMCID: PMC12804087 | PMID: 41339549
- Evidence: Immunohistochemistry and RNAscope image analysis and quantification were performed using QuPath 101 .
- Full pipeline: alignment/mapping [BWA v0.7.17, R] -> quantification [QuPath] -> visualisation [ggplot2] -> stage not stated [VEP]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **0.5.1**
- Evidence: For quantitation of proliferation and apoptosis, six regions of interest were chosen randomly on the whole slide image using QuPath (v.0.5.1) 66 .
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Evidence: Images analysis was carried out using QuPath image analysis software.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Evidence: The method was implemented in QuPath and the resulting score can range between 0 (no expression) and 300 (maximum expression).
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Cell segmentation was performed in QuPath software (v.0.5.0) using DAPI for nuclear detection and expansion of cell boundaries by 5 µm to approximate full cell outlines.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Version used: **0.5**
- Evidence: Quantification of AP Red signal intensity was performed using QuPath (v.0.5) with uniform thresholding parameters across all samples.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Targeting FSP1 triggers ferroptosis in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09710-8 | PMCID: PMC12779550 | PMID: 41193800
- Evidence: Tumour burden was quantified by H&E staining and analysed using QuPath software as a measurement of total tumour area/total lung lobe area.
- Full pipeline: quantification [QuPath]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **0.6**
- Evidence: Masson’s-trichrome-positive staining was quantified using QuPath (v.0.6) 54 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Unraveling the hidden role of a uORF-encoded peptide as a kinase inhibitor of PKCs. (PNAS 2021)

- DOI: 10.1073/pnas.2018899118 | PMCID: PMC8501901 | PMID: 34593629
- Evidence: Images were captured by a PANNORAMIC MIDI scanner (3DHISTECH) and analyzed by QuPath software (0.2.1).
- Full pipeline: normalisation [ImageJ] -> stage not stated [QuPath]

### STING activation promotes robust immune response and NK cell-mediated tumor regression in glioblastoma models. (PNAS 2022)

- DOI: 10.1073/pnas.2111003119 | PMCID: PMC9282249 | PMID: 35787058
- Evidence: IHC staining was quantified in QuPath software (0.2.0-m4).
- Full pipeline: alignment/mapping [STAR] -> quantification [QuPath] -> differential/statistical testing [DESeq2, R, ggplot2] -> stage not stated [Enrichr, ImageJ]

### Host protease activity classifies pneumonia etiology. (PNAS 2022)

- DOI: 10.1073/pnas.2121778119 | PMCID: PMC9231472 | PMID: 35696579
- Evidence: Counts were obtained using QuPath, and stain-positive cells were identified via manually set thresholds.
- Full pipeline: dimensionality reduction/clustering [R] -> machine learning [Python] -> stage not stated [QuPath]

### Radioresistant cells initiate lymphocyte-dependent lung inflammation and IFNγ-dependent mortality in STING gain-of-function mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202327119 | PMCID: PMC9231608 | PMID: 35696583
- Evidence: Whole slide images were then analyzed in QuPath ( 56 ) using trained pixel classifiers, namely, one trained to identify tissue broadly and another trained to specifically identify immune aggregates.
- Full pipeline: alignment/mapping [DESeq2] -> differential/statistical testing [DESeq2] -> machine learning [QuPath] -> visualisation [DESeq2]

### A predictive microfluidic model of human glioblastoma to assess trafficking of blood-brain barrier-penetrant nanoparticles. (PNAS 2022)

- DOI: 10.1073/pnas.2118697119 | PMCID: PMC9191661 | PMID: 35648828
- Evidence: Quantification of CC3 staining was performed in QuPath version (v)0.2.3 (Queen’s University, Belfast) using QuPath’s build-in “Positive cell detection” ( 88 ) with three ROIs of the same size manually placed per tumor section.
- Full pipeline: quantification [ImageJ, QuPath]

### MITF deficiency accelerates GNAQ-driven uveal melanoma. (PNAS 2022)

- DOI: 10.1073/pnas.2107006119 | PMCID: PMC9172632 | PMID: 35512098
- Evidence: Quantification using QuPath software determined that the average percentage of phospho-ERK–positive tumor cells in Qpm+ tumors ( n = 4) was 42.93% ± 9.95% ( SI Appendix , Fig.
- Full pipeline: quantification [QuPath] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2 v1.30.1, R v4.0.3] -> differential/statistical testing [Cytoscape] -> visualisation [GSEA]

### Tumor FAK orchestrates immunosuppression in ovarian cancer via the CD155/TIGIT axis. (PNAS 2022)

- DOI: 10.1073/pnas.2117065119 | PMCID: PMC9169934 | PMID: 35467979
- Version used: **0.2.3**
- Evidence: QuPath (0.2.3) ( 50 ) was used for image analyses.
- Full pipeline: stage not stated [QuPath v0.2.3]

### FKBP52 and FKBP51 differentially regulate the stability of estrogen receptor in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2110256119 | PMCID: PMC9169630 | PMID: 35394865
- Version used: **0.3.1**
- Evidence: The percentage of Ki-67–positive cells was determined using the function of “Positive cell detection” in QuPath, version 0.3.1, software ( 64 ).
- Full pipeline: stage not stated [GSEA, QuPath v0.3.1]

### Differential effects of early or late exposure to prenatal maternal immune activation on mouse embryonic neurodevelopment. (PNAS 2022)

- DOI: 10.1073/pnas.2114545119 | PMCID: PMC8944668 | PMID: 35286203
- Version used: **0.2.0**
- Evidence: Images from the all four treatment groups were analyzed blind to the experimental conditions by using QuPath (v0.2.0-m3) software ( 78 ).
- Full pipeline: differential/statistical testing [R v3.5.1, lme4] -> stage not stated [ANTs, QuPath v0.2.0]

### Gene expression in the primate orbitofrontal cortex related to anxious temperament. (PNAS 2023)

- DOI: 10.1073/pnas.2305775120 | PMCID: PMC10710052 | PMID: 38011550
- Evidence: Cell numbers and probe detections were collected using QuPath software v0.4.3.
- Full pipeline: alignment/mapping [Python v2.7] -> stage not stated [CellProfiler v4.2.1, ImageJ v1.53s, QuPath, Scanpy, limma, scDblFinder]

### Peripheral blood TCR clonotype diversity as an age-associated marker of breast cancer progression. (PNAS 2023)

- DOI: 10.1073/pnas.2316763120 | PMCID: PMC10710020 | PMID: 38011567
- Evidence: Images were captured by the Nikon Ti/E inverted microscope and analyzed with QuPath.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [survival (R)] -> stage not stated [DESeq2, GSEA, QuPath, R v4.3]

### Transient inhibition of lysosomal functions potentiates nucleic acid vaccines. (PNAS 2023)

- DOI: 10.1073/pnas.2306465120 | PMCID: PMC10622924 | PMID: 37871214
- Evidence: Slides were imaged using an Andor Dragonfly Spinning Disk Confocal Microscope; the images were analyzed using Image J or QuPath software.
- Full pipeline: stage not stated [QuPath]

### Vestibular CCK signaling drives motion sickness-like behavior in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2304933120 | PMCID: PMC10622874 | PMID: 37847729
- Evidence: All in situ hybridization assays were imaged using a confocal (Leica SP5) or epifluorescence (Nikon Eclipse 90i) microscope and analyzed in ImageJ (Fiji v1.0) or QuPath open-source software ( 74 ).
- Full pipeline: stage not stated [ImageJ, QuPath]

### Steroid receptor coactivator 3 is a key modulator of regulatory T cell-mediated tumor evasion. (PNAS 2023)

- DOI: 10.1073/pnas.2221707120 | PMCID: PMC10266015 | PMID: 37253006
- Evidence: The QuPath program was used to quantify IHC staining results.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, MACS2]

### A backpack-based myeloid cell therapy for multiple sclerosis. (PNAS 2023)

- DOI: 10.1073/pnas.2221535120 | PMCID: PMC10151518 | PMID: 37075071
- Version used: **0.3.2**
- Evidence: Immune cell infiltration was measured using QuPath v0.3.2 ( 54 ).
- Full pipeline: stage not stated [QuPath v0.3.2]

### Molecular profiling of the stroke-induced alterations in the cerebral microvasculature reveals promising therapeutic candidates. (PNAS 2023)

- DOI: 10.1073/pnas.2205786120 | PMCID: PMC10120001 | PMID: 37058487
- Evidence: QuPath software was used to quantify the number of probes (transcripts) per unit of Glut1 positive vessel area in each ROI.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [GSEA]

### Metastasis from the tumor interior and necrotic core formation are regulated by breast cancer-derived angiopoietin-like 7. (PNAS 2023)

- DOI: 10.1073/pnas.2214888120 | PMCID: PMC10013750 | PMID: 36853945
- Evidence: QuPath quantification of RNA ISH.
- Full pipeline: quantification [QuPath] -> stage not stated [Metascape]

### CRISPR metabolic screen identifies ATM and KEAP1 as targetable genetic vulnerabilities in solid tumors. (PNAS 2023)

- DOI: 10.1073/pnas.2212072120 | PMCID: PMC9963842 | PMID: 36724254
- Evidence: Tumor burden was calculated by quantifying the area of tumor nodules in lung region using QuPath software.
- Full pipeline: quantification [QuPath]

### Goblet cell differentiation subgroups in colorectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2414213121 | PMCID: PMC11513979 | PMID: 39401352
- Evidence: Immunofluorescence images were visualised using Fiji/ImageJ ( https://imagej.net/software/fiji/ ) and QuPath ( https://qupath.github.io/ ) software.
- Full pipeline: visualisation [Fiji, ImageJ, QuPath] -> stage not stated [CellProfiler v3.0]

### Transcriptional repression by HDAC3 mediates T cell exclusion from &lt;i&gt;Kras&lt;/i&gt; mutant lung tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2317694121 | PMCID: PMC11494357 | PMID: 39388266
- Evidence: Stained slides were scanned using a Perkin Elmer Slide Scanner for downstream analysis using Panoramic Viewer software, Inform v2.1 image analysis software, or QuPath software.
- Full pipeline: alignment/mapping [HOMER, STAR] -> stage not stated [Enrichr, GSEA, QuPath]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Version used: **0.5.1**
- Evidence: Image quantification of positive ASCL1 cells or HMGCS2 positive cells was done with QuPath v0.5.1 software.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### An arginine-rich nuclear localization signal (ArgiNLS) strategy for streamlined image segmentation of single cells. (PNAS 2024)

- DOI: 10.1073/pnas.2320250121 | PMCID: PMC11317604 | PMID: 39074275
- Evidence: ML classifiers for ArgiNLS- and SV40nls-EGFP labels were created using random forest classification with QuPath ( 84 ) software applied to composite TIF images ( SI Appendix , Supporting Information Methods ).
- Full pipeline: quantification [ImageJ] -> machine learning [QuPath, ilastik]

### <i>Vibrio</i> MARTX toxin processing and degradation of cellular Rab GTPases by the cytotoxic effector Makes Caterpillars Floppy. (PNAS 2024)

- DOI: 10.1073/pnas.2316143121 | PMCID: PMC11194500 | PMID: 38861595
- Evidence: Images of the distal, proximal, and central portions of each small intestine were taken on an EVOS imaging system at 20× magnification and Rab1B signal intensity quantified by color deconvolution using QuPath v0 4.4.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [QuPath] -> dimensionality reduction/clustering [ChimeraX v1.5, ColabFold v1.5.1] -> stage not stated [AlphaFold]

### β-catenin turnover is regulated by Nek10-mediated tyrosine phosphorylation in A549 lung adenocarcinoma cells. (PNAS 2024)

- DOI: 10.1073/pnas.2300606121 | PMCID: PMC11087748 | PMID: 38683979
- Evidence: Lung metastasis area was quantified by semiautomated digital analysis using QuPath pathology and bioimage analysis software ( 27 ).
- Full pipeline: quantification [ImageJ, QuPath]

### Proteasome stress activates YAP/TAZ through the RAP2-MAP4Ks-LATS1/2 pathway and its therapeutic implications in solid tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2517376122 | PMCID: PMC12745813 | PMID: 41410760
- Evidence: H-scores were quantified using QuPath.
- Full pipeline: quantification [QuPath]

### Medial entorhinal VIP-expressing interneurons receive input from the thalamic anterior dorsal nucleus and are critical for spatial memory. (PNAS 2025)

- DOI: 10.1073/pnas.2425024122 | PMCID: PMC12745809 | PMID: 41397139
- Evidence: Virtual Slide Images (.vsi) files acquired from the slide scanner were opened in FIJI using the BIOP VSI Reader (EPFL, Lausanne, Switzerland) and exported as individual TIFF files for further analysis in FIJI (Image J version 2.1.0) and QuPath (Software version 0.4.3.1).
- Full pipeline: stage not stated [QuPath]

### The immunoproteasome regulates ILC2 responses by modulating mitochondrial capacity. (PNAS 2025)

- DOI: 10.1073/pnas.2518190122 | PMCID: PMC12663963 | PMID: 41264257
- Evidence: After 3 wk of HDM injections, the lung was harvested and lung damages were evaluated by determining cell number (using QuPath), alveolar and tissue areas (using QuPath), epithelial thickness (using ImageJ), and inflammation score, described previously ( 117 ), estimated by a blinded observer.
- Full pipeline: read trimming [fastp] -> quantification [ImageJ] -> differential/statistical testing [R, edgeR] -> stage not stated [QuPath]

### Machine-learning models based on histological images from healthy donors identify imageQTLs and predict chronological age. (PNAS 2025)

- DOI: 10.1073/pnas.2423469122 | PMCID: PMC12646272 | PMID: 41218125
- Version used: **0.4.3**
- Evidence: QuPath v0.4.3 was used to extract nucleus features from GTEx WSIs.
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [PLINK v2.0] -> stage not stated [DESeq2, GSEA, QuPath v0.4.3]

### Synovial MS4A4A correlates with inflammation and counteracts response to corticosteroids in arthritis. (PNAS 2025)

- DOI: 10.1073/pnas.2504529122 | PMCID: PMC12452939 | PMID: 40924449
- Evidence: The percentage of MS4A4A, NE, FCGR3A, Ly6G, and Iba1-positive cells in the synovium was determined using quantitative digital image analyses (QuPath software) ( 58 ).
- Full pipeline: stage not stated [QuPath]

### Therapeutic CD8&lt;sup&gt;+&lt;/sup&gt; T cell tissue retention and immunomodulation during ART interruption fail to prevent SIV rebound. (PNAS 2025)

- DOI: 10.1073/pnas.2501037122 | PMCID: PMC12377730 | PMID: 40811471
- Evidence: Whole tissue slides were scanned using the Akoya Fusion microscope at 40X and were analyzed using the QuPath software.
- Full pipeline: stage not stated [QuPath, StarDist]

### A recurrent de novo damaging variant in &lt;i&gt;EMP2&lt;/i&gt; causes progressive symmetric erythrokeratoderma. (PNAS 2025)

- DOI: 10.1073/pnas.2509896122 | PMCID: PMC12358830 | PMID: 40758889
- Evidence: For quantification of Ki67+ cells, QuPath was used for nuclei detection to count cells, and Prism version 10.0.0 was used for statistical analysis.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [QuPath] -> dimensionality reduction/clustering [Monocle, Seurat, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ANNOVAR]

### Effects of the gut microbiota on placental angiogenesis and intrauterine growth in gnotobiotic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426341122 | PMCID: PMC12318179 | PMID: 40711921
- Version used: **0.4.4**
- Evidence: LZ/JZ areas and vascular measurements were performed using QuPath v0.4.4.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, lme4] -> stage not stated [QuPath v0.4.4]

### Neuronal ALKAL2 and its ALK receptor contribute to the development of colitis-associated colorectal cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500632122 | PMCID: PMC12184428 | PMID: 40493183
- Evidence: RNAscope quantification was performed using QuPath software, following the recommendations provided by the ACD manufacturer.
- Full pipeline: quantification [QuPath]

### Dmrt2 and Hmx2 direct intercalated cell diversity in the mammalian kidney through antagonistic and supporting regulatory processes. (PNAS 2025)

- DOI: 10.1073/pnas.2418471122 | PMCID: PMC12107187 | PMID: 40354537
- Evidence: QuPath was used to quantify cells with positive signal (puncta) for Foxi1, Dmrt2, Hmx2, Slc4a1, or Slc26a4 after RNAscope detection of transcripts.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Monocle, Seurat]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Evidence: Quantification was done using the image processing software QuPath and ImageJ.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### O-GalNAc glycans are enriched in neuronal tracts and regulate nodes of Ranvier. (PNAS 2025)

- DOI: 10.1073/pnas.2418949122 | PMCID: PMC11892645 | PMID: 39999163
- Version used: **0.3.2**
- Evidence: Images analysis was then performed using ImageJ (v1.53t) or QuPath (v0.3.2) software.
- Full pipeline: visualisation [FUMA] -> stage not stated [ImageJ v1.53t, QuPath v0.3.2]

### A clinically relevant model and method to study necrosis as a driving force in glioma restructuring and progression. (PNAS 2025)

- DOI: 10.1073/pnas.2416024122 | PMCID: PMC11848380 | PMID: 39946540
- Evidence: All whole-slide images were scanned, and digital images were analyzed using QuPath software (version 0.5.1) to assess tumor size, extent necrosis, and thrombotic events within glioma regions containing necrosis.
- Full pipeline: stage not stated [QuPath]

### Fasting primes small intestinal regeneration after damage via a microbiome-metabolite-chromatin axis. (PNAS 2026)

- DOI: 10.1073/pnas.2529215123 | PMCID: PMC13320697 | PMID: 42335240
- Evidence: Positive cells were counted using QuPath ( 4 ) and statistically analyzed using GraphPad Prism 10.
- Full pipeline: dimensionality reduction/clustering [MACS2 v2.2.9.1, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ArchR v1.0.2, GSEA, HOMER, R v1.0.2]

### 15-PGDH inhibition promotes muscle repair and strength recovery during GLP-1 receptor agonist-induced weight loss. (PNAS 2026)

- DOI: 10.1073/pnas.2606533123 | PMCID: PMC13250539 | PMID: 42228536
- Evidence: Digital images were captured with an Aperio AT2 (Leica) and QuPath software was used to extract the images.
- Full pipeline: stage not stated [QuPath]

### Three-dimensional high-content imaging of unstained soft tissue with subcellular resolution using a laboratory-based X-ray microscope. (PNAS 2026)

- DOI: 10.1073/pnas.2525239123 | PMCID: PMC13012051 | PMID: 41843669
- Version used: **0.5.1**
- Evidence: Nuclei in the H&E histology images were segmented and their size quantified using the function Cell detection of the commercially available software QuPath (v.
- Full pipeline: quantification [QuPath v0.5.1]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Version used: **0.5.1**
- Evidence: Images were acquired using a Zeiss 980 Confocal Microscope or Olympus VS200 Slide Scanner and analyzed using QuPath (v0.5.1).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Lipid nanoparticle GM-CSF replacement for autoimmune pulmonary alveolar proteinosis. (PNAS 2026)

- DOI: 10.1073/pnas.2511483123 | PMCID: PMC12913010 | PMID: 41671176
- Evidence: The images were acquired using an inverted fluorescence microscope and analyzed using QuPath software (v0.5.1).
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, scDblFinder]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: QuPath software was utilized for IF stain analysis.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Sleep loss induces cholesterol-associated myelin dysfunction. (PNAS 2026)

- DOI: 10.1073/pnas.2523438123 | PMCID: PMC12846829 | PMID: 41557795
- Evidence: Images were acquired using epifluorescence or confocal microscopy, and quantitative morphometry was performed with QuPath and Fiji software.
- Full pipeline: normalisation [ANTs] -> dimensionality reduction/clustering [ANTs] -> differential/statistical testing [ANTs] -> stage not stated [QuPath]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Evidence: Cell detection and classification was carried out using QuPath software v0.5.0 ( 71 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Evidence: Tissues were then annotated, mast cells counted in QuPath and classified as normal or degranulated based on 1) extent of granules exhibiting fusion with the cell membrane 2) granules identified immediately proximally to the cell of interest, and/or 3) alterations in staining/extrusion of the cell.
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

### Myelin sheaths in the central nervous system can withstand damage and dynamically remodel. (Science 2026)

- DOI: 10.1126/science.adr4661 | PMCID: PMC7618902 | PMID: 41678629
- Version used: **0.4.4**
- Evidence: Human post-mortem brain tissue quantification Analysis was done using QuPath version 0.4.4 and Fiji ImageJ 64-bit version 2.14.0/1.54f software.
- Full pipeline: quantification [Fiji, QuPath v0.4.4] -> stage not stated [ImageJ v1.54p]

