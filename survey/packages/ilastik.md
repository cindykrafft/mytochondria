# ilastik

- **Category:** imaging
- **Papers in survey:** 55
- **Journals:** PNAS (27), Nature (21), Cell (6), Science (1)
- **Years:** 2021 (7), 2022 (12), 2023 (9), 2024 (9), 2025 (14), 2026 (4)
- **Versions named:** 1.3.3 (7), 1.3.2 (3), 1.3.3b (1), 1.3.3p (1), 1.4.1r (1), 1.1.5 (1)
- **Pipeline stages it appears in:** machine learning (14), quantification (8), dimensionality reduction/clustering (3), registration (1), normalisation (1), visualisation (1), alignment/mapping (1), structure determination (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **1.3.2**
- Evidence: Cell segmentation and single-cell feature extraction Segmentation was performed in a two-step process, a signal-classification step using Ilastik 1.3.2 ( Berg et al., 2019 ) followed by an object-recognition step using CellProfiler 3.1.8 ( Carpenter et al., 2006 ), as described elsewhere ( Schapiro et al., 2017 ).
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ...uperElastix/elastix ElastixWrapper Tischer, 2019 https://github.com/embl-cba/elastixWrapper ImageJ Schindelin et al., 2012 https://imagej.nih.gov/ij/ Ilastik Berg et al., 2019 https://www.ilastik.org/ Python Louvain N/A https://github.com/taynaud/python-louvain UMAP McInnes et al., 2018 https://umap-learn.readthedocs.io/en/latest/ scikit-image van der Walt et al., 2014 https://scikit-image.org/ sc...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Functional diversity for body actions in the mesencephalic locomotor region. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.002 | PMCID: PMC8382160 | PMID: 34302739
- Version used: **1.1.5**
- Evidence: The machine learning software Ilastik (version 1.1.5) was used to track the position of mice in the open field.
- Full pipeline: differential/statistical testing [R, scikit-learn] -> visualisation [seaborn] -> stage not stated [DeepLabCut, Python v3.7, SciPy, ilastik v1.1.5]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ...eneontology.org/ GraphPad Prism 9 GraphPad https://www.graphpad.com/ Harmony ( Korsunsky et al., 2019 ) https://www.github.com/immunogenomics/harmony Ilastik ( Berg et al., 2019 ) https://www.ilastik.org/ ImageJ ( Schneider et al., 2012 ) https://imagej.nih.gov/ij Qi-Tissue Quantitative Imagining Systems https://www.qi-tissue.com genexyz Polylux Resolve Biosciences Single-Cell Signature Explorer a...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: We trained a random forest pixel classifier (Ilastik 115 with default settings) on 3 images of the green channel (LysM-eGFP) and used that for subsequent classification of the LysM-eGFP channel of each image stack.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 48 https://gsea-msigdb.github.io/gseapreranked-gpmodule/v6/index.html Ilastik Berg et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Actin cables and comet tails organize mitochondrial networks in mitosis. (Nature 2021)

- DOI: 10.1038/s41586-021-03309-5 | PMCID: PMC7990722 | PMID: 33658713
- Evidence: 2D Mitochondrial mass distribution analysis: Binary segmentations of metaphase mitochondria (Mito-dsRed2) after DMSO, CytoD, NT siRNA, Myo19 siRNA (Extended Data Figure 5) or Arp3 siRNA-treatment (Extended Data Figure 9) were generated using the pixel classification workflow in ilastik 43 .
- Full pipeline: simulation/modelling [TrackMate] -> stage not stated [ImageJ, ilastik]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Version used: **1.3.3**
- Evidence: For the calculation of tissue flows, osteoblast nuclei (equalized H2A-mCherry marker, hyposquamal layer) were segmented and then tracked using Ilastik 1.3.3 software 43 .
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: 7g,h, nuclear segmentation was performed in Ilastik 71 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: An Ilastik classifier was then trained and used to classify the signal for each channel (405, 488, 561 and 647 nm) of each FISH round into foreground and background.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Spatial predictors of immunotherapy response in triple-negative breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06498-3 | PMCID: PMC10533410 | PMID: 37674077
- Evidence: To identify regions of contiguous epithelium, we labelled pixels as epithelial based on their expression of cytokeratins and used a random-forest pixel classifier (Ilastik 43 ) to assign all remaining pixels a probability of belonging to an epithelial region.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> quantification [Bioconductor] -> differential/statistical testing [R] -> machine learning [ilastik] -> stage not stated [CellProfiler]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: SMAD nuclear fluorescence intensity quantification Nuclear segmentation masks of the epiblast-like compartment of the hEE were generated using Ilastik software (Ilastik-1.4.0).
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Fast and sensitive GCaMP calcium indicators for imaging neural populations. (Nature 2023)

- DOI: 10.1038/s41586-023-05828-9 | PMCID: PMC10060165 | PMID: 36922596
- Evidence: The Ilastik toolkit 54 was used to segment cell bodies in the reference images.
- Full pipeline: structure determination [REFMAC] -> stage not stated [CaImAn, PyMOL, Python, Suite2p, ilastik]

### Cardiogenic control of affective behavioural state. (Nature 2023)

- DOI: 10.1038/s41586-023-05748-8 | PMCID: PMC9995271 | PMID: 36859543
- Evidence: For automated whole-brain registration and cell-segmentation analysis, images were loaded onto Arivis Vision4D software, and neurons were segmented using a built-in supervised pixel-based classifier package based on Ilastik 63 (‘Trainable Segmenter’).
- Full pipeline: registration [ilastik] -> machine learning [ilastik] -> stage not stated [Kilosort v2.5]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: Data were normalized using semi-automated background removal in ilastik 60 (v.1.3.3), to control for variations in the signal-to-noise ratio between FFPE sections as described previously 61 .
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Version used: **1.3.3**
- Evidence: Liver ORO and CD protein signal was quantified using CellProfiler (v.4.2.6) 61 after pixel classification using ilastik (v.1.3.3) 66 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Evidence: Wide-field image quantification was done using trained ilastik 66 algorithms to segment the pixels (positive vs background) of TDP-43–HA, TDP-43 p403/404 and DAPI staining.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: RNA-ISH colocalization analysis Colocalization analysis was performed by first identifying the expressed genes on raw images through the utilization of a pixel classifier trained with the software ilastik 94 .
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Marcus kinetics control singlet and triplet oxygen evolving from superoxide. (Nature 2025)

- DOI: 10.1038/s41586-025-09587-7 | PMCID: PMC12527928 | PMID: 41044415
- Evidence: The images were analysed using the ilastik pixel classification and object classification workflows ( https://www.ilastik.org/ ), resulting in a histogram of particle sizes (Extended Data Fig.
- Full pipeline: stage not stated [ilastik]

### Patterned invagination prevents mechanical instability during gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09480-3 | PMCID: PMC12527948 | PMID: 40903575
- Version used: **1.3.3b**
- Evidence: Then, we created cartographic projections of the lateral recordings using the ImSAnE toolbox (v3a7be24) 45 by loading the restored data in MATLAB (R2015b) 46 , segmenting the epithelial surface using ilastik (v1.3.3b2) 47 , and generating 3D cartographic projections of lateral views following a workflow established for fly embryos 48 .
- Full pipeline: differential/statistical testing [Jupyter, Python v3.10.7, R v4.2.1] -> visualisation [Fiji v2.16.0, ImageJ v2.16.0] -> stage not stated [ilastik v1.3.3b]

### Quantitative imaging of lipid transport in mammalian cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09432-x | PMCID: PMC12507682 | PMID: 40836094
- Evidence: Segmented probability maps were generated for every organelle marker using the pixel classifier approach of the Ilastik software package 31 .
- Full pipeline: machine learning [ilastik]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: 3 , the light-sheet movies were segmented using Ilastik and post-processed, as above, and scikit-images regionprops functions were used to assess the volumes and the major axis length.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Version used: **1.3.3p**
- Evidence: The acquired images were processed and analysed using FIJI (v.2.14.0) 70 , ilastik (v.1.3.3post3) 71 and CellProfiler (v.4.2.1) 72 as described previously 69 .
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Evidence: For the co-localization analysis of ZorB–HT with either ZorC–mNG or ZorD–mNG, ZorB focus detection was performed using ilastik 64 .
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: All imaging data were examined, processed and quantified using Fiji, Ilastik and Cell Profiler.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Vagal blood volume receptors compensate for haemorrhage and posture change. (Nature 2026)

- DOI: 10.1038/s41586-025-10010-4 | PMCID: PMC13017543 | PMID: 41606321
- Evidence: Nerve fibres were assigned by image segmentation using Ilastik (Ilastik, Pixel Classification) and smoothened (Otsu’s method).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ, ilastik, scikit-image]

### Holistic motor control of zebra finch song syllable sequences. (Nature 2026)

- DOI: 10.1038/s41586-025-10069-z | PMCID: PMC13043288 | PMID: 41606337
- Version used: **1.3.3**
- Evidence: For segmentation, a selected portion of signals of interest in the downsampled contrast adjusted images of the tissue was visually identified, annotated and used to train a random forest classifier for segmentation in ilastik (v.1.3.3) (refs.
- Full pipeline: machine learning [ilastik v1.3.3] -> stage not stated [ImageJ]

### Three-dimensional virtual histology of the human hippocampus based on phase-contrast computed tomography. (PNAS 2021)

- DOI: 10.1073/pnas.2113835118 | PMCID: PMC8640721 | PMID: 34819378
- Evidence: The CB data were segmented with the interactive software package Ilastik ( 26 ) and a further manual optimization based on image filters and object removal based on visual control.
- Full pipeline: stage not stated [ilastik]

### ALS- and FTD-associated missense mutations in TBK1 differentially disrupt mitophagy. (PNAS 2021)

- DOI: 10.1073/pnas.2025053118 | PMCID: PMC8214690 | PMID: 34099552
- Evidence: Confocal microscopy was performed on an UltraView Vox spinning disk confocal system and images were deconvolved with Huygens Professional Software, then analyzed with ImageJ/FIJI, Ilastik, and CellProfiler software ( 56 – 58 ).
- Full pipeline: stage not stated [CellProfiler, ImageJ, ilastik]

### Gene delivery available in molluscan cells by strong promoter discovered from bivalve-infectious virus. (PNAS 2022)

- DOI: 10.1073/pnas.2209910119 | PMCID: PMC9661190 | PMID: 36322729
- Version used: **1.3.3**
- Evidence: An area of 0.77 cm 2 of autofluorescence emitted from adherent cells was photographed from each well and run through ilastik (1.3.3) Pixel Classification + Object Classification pipeline ( 74 ) for cell counting by supervised machine learning.
- Full pipeline: visualisation [R v4.1.2] -> stage not stated [ilastik v1.3.3]

### A quantitative and spatial analysis of cell cycle regulators during the fission yeast cycle. (PNAS 2022)

- DOI: 10.1073/pnas.2206172119 | PMCID: PMC9457408 | PMID: 36037351
- Evidence: The machine learning tool Ilastik ( 39 ) was trained and used to segment maximum projection mCherry images to create nuclear masks.
- Full pipeline: machine learning [ilastik]

### Bridging scales in a multiscale pattern-forming system. (PNAS 2022)

- DOI: 10.1073/pnas.2206888119 | PMCID: PMC9388104 | PMID: 35960842
- Evidence: We used the pixel classifier provided by the software ilastik ( 35 ).
- Full pipeline: machine learning [ilastik] -> stage not stated [ImageJ v1.52j]

### Dystrophin missense mutations alter focal adhesion tension and mechanotransduction. (PNAS 2022)

- DOI: 10.1073/pnas.2205536119 | PMCID: PMC9231619 | PMID: 35700360
- Version used: **1.3.2**
- Evidence: Stacked images were aligned using the Linear Stack with Alignment with an SIFT plugin and then analyzed using the BRET-Analyzer plugin ( 62 ). mNeonGreen images were used to generate FA masks using a machine learning tool, Ilastik (version 1.3.2).
- Full pipeline: alignment/mapping [ilastik v1.3.2] -> stage not stated [ImageJ v1.53h]

### Dynamics of <i>Drosophila</i> endoderm specification. (PNAS 2022)

- DOI: 10.1073/pnas.2112892119 | PMCID: PMC9169638 | PMID: 35412853
- Evidence: Image segmentation was performed for each two-dimensional (2D) slice of a movie using ilastik (41).
- Full pipeline: dimensionality reduction/clustering [ilastik] -> differential/statistical testing [PyMC, PyMC3] -> machine learning [scikit-learn]

### A role for endoplasmic reticulum dynamics in the cellular distribution of microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2104309119 | PMCID: PMC9169640 | PMID: 35377783
- Evidence: The ER segmentation was performed using a random forest pixel classifier in Ilastik.
- Full pipeline: machine learning [ilastik] -> stage not stated [CellProfiler]

### Mitochondrial dysfunction and oxidative stress contribute to cognitive and motor impairment in FOXP1 syndrome. (PNAS 2022)

- DOI: 10.1073/pnas.2112852119 | PMCID: PMC8872729 | PMID: 35165191
- Evidence: The total number of lysosomes was obtained by Ilastik segmentation and further arivis Vision4D (v3.4) three-dimensional (3D) reconstruction.
- Full pipeline: dimensionality reduction/clustering [ilastik] -> structure determination [ilastik] -> stage not stated [ImageJ]

### In situ proximity labeling identifies Lewy pathology molecular interactions in the human brain. (PNAS 2022)

- DOI: 10.1073/pnas.2114405119 | PMCID: PMC8812572 | PMID: 35082147
- Version used: **1.3.2**
- Evidence: Image quantification was performed using a random forest machine learning pixel classifier using ilastik (v.1.3.2), trained on representative images.
- Full pipeline: quantification [CellProfiler v3.1.5, ilastik v1.3.2] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Cytoscape] -> machine learning [ilastik v1.3.2] -> visualisation [Cytoscape] -> stage not stated [R v4.0.3]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Version used: **1.3.3**
- Evidence: Tagged image format (TIF) images were processed and converted to simple segmentation images using the Ilastik 1.3.3 (interactive machine learning for [bio]image analysis) tool ( 73 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Minorities drive growth resumption in cross-feeding microbial communities. (PNAS 2023)

- DOI: 10.1073/pnas.2301398120 | PMCID: PMC10636363 | PMID: 37903278
- Evidence: All image analysis was performed using MATLAB (version 2017b and newer), Vanellus software (DJ Kiviet, http://kiviet.com/research/vanellus.php ), and Ilastik-1.3.3post2-OSX ( https://www.ilastik.org/ ).
- Full pipeline: stage not stated [ilastik]

### Two-fluid dynamics and micron-thin boundary layers shape cytoplasmic flows in early <i>Drosophila</i> embryos. (PNAS 2023)

- DOI: 10.1073/pnas.2302879120 | PMCID: PMC10622894 | PMID: 37878715
- Version used: **1.3.3**
- Evidence: The nuclear segmentation masks of the Drosophila embryos were generated with Ilastik 1.3.3 software ( 56 ) by using the Pixel Classification pipeline.
- Full pipeline: stage not stated [ilastik v1.3.3]

### In situ architecture and membrane fusion of SARS-CoV-2 Delta variant. (PNAS 2023)

- DOI: 10.1073/pnas.2213332120 | PMCID: PMC10160983 | PMID: 37094167
- Evidence: Particle identification was carried out using ilastik ( 44 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, PHENIX] -> stage not stated [Coot, MotionCor2, RELION, ilastik]

### Actin polymerization counteracts prewetting of N-WASP on supported lipid bilayers. (PNAS 2024)

- DOI: 10.1073/pnas.2407497121 | PMCID: PMC11648614 | PMID: 39630867
- Evidence: For the phase diagram of surface condensates on SLBs the condensed area fraction (A in over total area A total in the field of view) was measured by segmentation of condensates in Ilastik (see below).
- Full pipeline: stage not stated [Fiji v2.9.0, ImageJ v2.9.0, ilastik]

### The endoplasmic reticulum as an active liquid network. (PNAS 2024)

- DOI: 10.1073/pnas.2409755121 | PMCID: PMC11494354 | PMID: 39392663
- Evidence: The machine learning segmentation toolkit ilastik ( 75 ) is used to segment ER network structures and identify polygons in live-cell images.
- Full pipeline: stage not stated [ilastik]

### An arginine-rich nuclear localization signal (ArgiNLS) strategy for streamlined image segmentation of single cells. (PNAS 2024)

- DOI: 10.1073/pnas.2320250121 | PMCID: PMC11317604 | PMID: 39074275
- Evidence: We therefore trained separate ML classifiers using ilastik software (61) to achieve optimal single-cell classification performance, separately for each tag ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> machine learning [QuPath, ilastik]

### Intracellular C3 protects β-cells from IL-1β-driven cytotoxicity via interaction with Fyn-related kinase. (PNAS 2024)

- DOI: 10.1073/pnas.2312621121 | PMCID: PMC10895342 | PMID: 38346191
- Evidence: Images were analyzed using Ilastik and ImageJ software.
- Full pipeline: stage not stated [ImageJ, STRING db, ilastik]

### Genome integrity relies on rapid recycling of DNA Pol III in bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2511725122 | PMCID: PMC12663971 | PMID: 41264243
- Evidence: This cell mask was created using ilastik and Cellpose ( 58 , 59 ).
- Full pipeline: stage not stated [Cellpose, ilastik]

### A model for boundary-driven tissue morphogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2505160122 | PMCID: PMC12478147 | PMID: 40966291
- Evidence: ( C ) After image fusion and deconvolution ( Materials and Methods and SI Appendix ), images are processed using a pixel classifier (ilastik, 53 ) to improve nuclear detection.
- Full pipeline: machine learning [ilastik] -> stage not stated [TrackMate]

### A thermodynamic perspective on mammalian neural crest ingression. (PNAS 2025)

- DOI: 10.1073/pnas.2504185122 | PMCID: PMC12435306 | PMID: 40906808
- Evidence: We used Ilastik ( 88 ), a machine learning segmentation program, to segment the neural crest in 3D.
- Full pipeline: stage not stated [ilastik]

### Concerted transport and phosphorylation of diacylglycerol at ER-PM contact sites regulate phospholipid dynamics during stress. (PNAS 2025)

- DOI: 10.1073/pnas.2421334122 | PMCID: PMC12167946 | PMID: 40455983
- Evidence: Confocal images of the cortical plane of transiently coexpressed proteins in N. benthamiana leaves were segmented in ER and ER–PM CS in a semiautomatic way, using the interactive machine learning tool ilastik ( 45 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Clustal Omega, Cufflinks v2.2.1, R] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [AlphaFold, ilastik]

### A conserved ARF-DNA interface underlies auxin-triggered transcriptional response. (PNAS 2025)

- DOI: 10.1073/pnas.2501915122 | PMCID: PMC12002309 | PMID: 40168121
- Version used: **1.3.3**
- Evidence: To quantify thallus growth area, pictures were resized to 2,000 × 2,000 pixels with ImageMagick (version 7.1.1-21), followed by pixel classification and object quantification of projected area of single gemmalings with Ilastik (version 1.3.3) ( 45 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [featureCounts] -> quantification [ilastik v1.3.3] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, HMMER, PyMOL]

### Bacterial motility depends on a critical flagellum length and energy-optimized assembly. (PNAS 2025)

- DOI: 10.1073/pnas.2413488122 | PMCID: PMC11929379 | PMID: 40067900
- Evidence: Image analysis and tracking of cells was performed using ilastik ( 45 ) and Fiji ( 46 ) equipped with TrackMate ( 47 ).
- Full pipeline: stage not stated [ImageJ, TrackMate, ilastik]

### Spatial population dynamics of bacterial colonies with social antibiotic resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2417065122 | PMCID: PMC11848446 | PMID: 39937854
- Evidence: For image analysis, tile assembly, maximum intensity projection and intensity adjustment were conducted in FIJI/ImageJ ( 105 , 106 ), segmentation in ilastik ( 107 ) and composition and patch size (radially averaged autocorrelation functions of green signal) quantification in MATLAB (Mathworks).
- Full pipeline: quantification [ImageJ, ilastik]

### A carnitine transporter at the blood-brain barrier modulates sleep via glial lipid metabolism in <i>Drosophila</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2421178122 | PMCID: PMC11789159 | PMID: 39847335
- Evidence: Ilastik ( https://www.ilastik.org/ ) software was used to process raw images to remove off-target signals which were excluded from the analysis.
- Full pipeline: quantification [ImageJ] -> stage not stated [ilastik]

### Collectin-11 regulates osteoclastogenesis and bone maintenance via a complement-dependent mechanism. (PNAS 2026)

- DOI: 10.1073/pnas.2511950123 | PMCID: PMC12974412 | PMID: 41774788
- Version used: **1.4.1r**
- Evidence: ImageJ (NIH) software ( 9 , 35 ) in conjunction with Ilastik 1.4.1rc2 software was used to generate pixel-based segmentation images of TRAP-stained OCLs and calculate the area of OCLs in microscopic images—see SI Appendix , Fig.
- Full pipeline: stage not stated [ImageJ, ilastik v1.4.1r]

### Ciliopathy patient variants reveal organelle-specific functions for TUBB4B in axonemal microtubules. (Science 2024)

- DOI: 10.1126/science.adf5489 | PMCID: PMC7616230 | PMID: 38662826
- Evidence: Staining colocalization between positive FLAG and positive α-tubulin from a given cell area (ROI) was quantified using machine learning of Ilastik software( 65 ), percentages of staining colocalization were generated using JACoP plugin on ImageJ software( 66 ) and plotted using GraphPad software.
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ, Seurat, ilastik] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [ChimeraX, IMOD, PHENIX, RELION] -> visualisation [ImageJ, ilastik] -> stage not stated [VEP]

