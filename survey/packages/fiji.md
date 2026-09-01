# Fiji

- **Category:** imaging
- **Papers in survey:** 198
- **Journals:** PNAS (108), Nature (75), Cell (11), Science (4)
- **Years:** 2021 (24), 2022 (32), 2023 (37), 2024 (38), 2025 (39), 2026 (28)
- **Versions named:** 2.1.0 (3), 2.9.0 (3), 2.0.0 (3), 1.52p (3), 2.3.0 (2), 1.53c (2), 1.54f (2), 2.14.0 (2), 1.8.0 (2), 1.53e (1)
- **Pipeline stages it appears in:** quantification (34), visualisation (10), dimensionality reduction/clustering (5), differential/statistical testing (3), normalisation (2), registration (2), simulation/modelling (1), alignment/mapping (1)

## Papers

### Microglia jointly degrade fibrillar alpha-synuclein cargo by distribution through tunneling nanotubes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.007 | PMCID: PMC8527836 | PMID: 34555357
- Evidence: Henneberger N/A Software and Algorithms CellProfiler Broad Institute of Harvard and MIT v3.1.8 FACSDIVA™ software Becton Dickinson N/A Fiji ImageJ Wayne Rusband v2.0.0-rc-69/1.52n FlowJo FlowJo, LLC v3.05470 ggplot2 CRAN v3.2.1 Graph Pad Prism GraphPad Software Inc. v7.0e and v8.0 Image Studio, v5.2 LI-COR Biosciences N/A Imaris Bitplane by Oxford Instruments plc v9.2.1 NIS-elements Nikon AR 4.20....
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> dimensionality reduction/clustering [Cytoscape] -> stage not stated [CellProfiler, Fiji, ImageJ, ggplot2, tidyverse]

### Parasitic modulation of host development by ubiquitin-independent protein degradation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.029 | PMCID: PMC8525514 | PMID: 34536345
- Evidence: ... constructs listed in Table S5 ) Berrow et al., 2007 N/A Software and algorithms Prism 7 Graphpad https://www.graphpad.com/scientific-software/prism/ Fiji ImageJ https://imagej.net/software/fiji/ Phylogeny.fr ( Dereeper et al., 2008 ) http://www.phylogeny.fr/index.cgi Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fu...
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> stage not stated [Fiji, ImageJ]

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Evidence: ...ombinase Expression Vector Thermo Fisher Scientific Cat#V600520 pcDNA5 FRT/TO Vector Kit Thermo Fisher Scientific Cat#V652020 Software and algorithms Fiji/ImageJ Rueden et al., 2017 https://imagej.nih.gov/ij/ GraphPad Prism 5 GraphPad Software https://www.graphpad.com/scientific-software/prism/ R v 4.0.3 The R Project for Statistical Computing https://www.r-project.org/ Python v 3.7 Python Softwar...
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Evidence: ...n Cat#: 12536017 Software and algorithms GraphPad Prism 9.0 GraphPad Software, Inc https://www.graphpad.com/ FlowJo FlowJo 10 https://www.flowjo.com/ Fiji/ImageJ Open Source https://imagej.net/Fiji BioRender BioRender https://biorender.com/ TrimGalore (version 0.5.0) Martin, 2011 https://github.com/FelixKrueger/TrimGalore kallisto (version 0.44.0) Bray et al. , 2016 https://pachterlab.github.io/ka...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### The molecular basis for sarcomere organization in vertebrate skeletal muscle. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.047 | PMCID: PMC8054911 | PMID: 33765442
- Evidence: ...ki/doku.php?id=gpu_isac SPHIRE Moriya et al., 2017 https://sphire.mpg.de/ TrackMate plug-in in Fiji Tinevez et al., 2017 https://imagej.net/TrackMate Fiji (ImageJ) Schindelin et al., 2012 ; Schneider et al., 2012 https://imagej.net/Fiji TEMPy Farabella et al., 2015 http://tempy.ismb.lon.ac.uk/ SWISS-MODEL Bertoni et al., 2017 ; Bienert et al., 2017 ; Guex et al., 2009 ; Studer et al., 2020 ; Water...
- Full pipeline: visualisation [R] -> stage not stated [EMAN2, Fiji, IMOD, ImageJ, RELION, TrackMate]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **2.0.0**
- Evidence: ...sue Optimization, Rev A) was performed with imaging of fluorescence footprint on InCell 6000 Analyzer (GE Healthcare) and image analysis performed in Fiji (ImageJ v2.0.0) identifying 18 minutes as optimum permeabilization time.
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A serotonergic axon-cilium synapse drives nuclear signaling to alter chromatin accessibility. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.026 | PMCID: PMC9789380 | PMID: 36055200
- Evidence: GRAB-HTR6-cilia with optogenetic stimulation The 4D stacks (xyzt) were projected onto single planes (xyt) by maximum intensity projection in Fiji/ImageJ.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python] -> simulation/modelling [ImageJ] -> stage not stated [Conda, Fiji, PHENIX]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: The whole-body tiled stacks were initially stitched utilizing Fiji/ImageJ to obtain stitching on the xy-axis ( http://discotechnologies.org/SHANEL/manual_stitching.py ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Ricca's factors as mobile proteinaceous effectors of electrical signaling. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.006 | PMCID: PMC10098372 | PMID: 36870332
- Evidence: ...N/A TGG1-Glu420Ala-StrepII-9×His This paper N/A TGG1-StrepII-9×His This paper N/A Software and algorithms ChemDraw v20.0 PerkinElmer RRID: SCR_016768 Fiji (ImageJ) Schneider et al.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 5 N/A Software and algorithms Fiji (ImageJ) Schindelin et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Mapping cellular targets of covalent cancer drugs in the entire mammalian body. (Cell 2026)

- DOI: 10.1016/j.cell.2025.11.030 | PMCID: PMC12875305 | PMID: 41435821
- Evidence: For hemisphere coronal and transverse views, TIFF files were imported as image sequences and then resliced by Fiji ImageJ.
- Full pipeline: visualisation [ImageJ] -> stage not stated [Fiji]

### Cold-induced Arabidopsis FRIGIDA nuclear condensates for FLC repression. (Nature 2021)

- DOI: 10.1038/s41586-021-04062-5 | PMCID: PMC8612926 | PMID: 34732891
- Evidence: A binary image of just the spots was then created through threshold in Fiji (ImageJ) and the spot area was subsequently measured by Analyze Particles in Fiji (ImageJ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Cellular anatomy of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03970-w | PMCID: PMC8494646 | PMID: 34616071
- Evidence: Then, we placed fiduciary landmarks on both data and CCFv3 sections for warping conducted using moving least squares in Fiji/ImageJ.
- Full pipeline: alignment/mapping [Python v3.7] -> stage not stated [Fiji, ImageJ]

### Genetic dissection of the glutamatergic neuron system in cerebral cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03955-9 | PMCID: PMC8494647 | PMID: 34616069
- Evidence: ...EGFP or EYFP was filtered by applying a square root transformation, histogram matching to the original image, and median and Gaussian filtering using Fiji/ImageJ software 50 so as to maximize signal detection while minimizing background auto-fluorescence, as described before 51 .
- Full pipeline: stage not stated [Fiji, ImageJ]

### Centromeres are dismantled by foundational meiotic proteins Spo11 and Rec8. (Nature 2021)

- DOI: 10.1038/s41586-021-03279-8 | PMCID: PMC8843027 | PMID: 33658710
- Evidence: Semi-automated quantitation of KT loss We developed a Fiji/ImageJ macro to score for the presence of CenpA signal on either side of a CenpB bar.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: DM intensities relative to the endogenous DHFR on chromosome 5 were determined using the ROI feature in Fiji (ImageJ) 35 by averaging the intensities of the brightest four single DM dots in each spread and subtraction of similarly sized adjacent background regions, divided by the average intensity of the endogenous DHFR signals within the same spread (with background subtracted).
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Medin co-aggregates with vascular amyloid-β in Alzheimer's disease. (Nature 2022)

- DOI: 10.1038/s41586-022-05440-3 | PMCID: PMC9712113 | PMID: 36385530
- Version used: **2.3**
- Evidence: Densitometric values of single protein bands (amyloid-β, APP, CTF-β, GAPDH, α-SMA, β-actin; PDGFR-β, full-length MFG-E8) or fragments or aggregates (6B3, 1–80 kDa) were analysed with the software package Aida (Stella 3200, Raytest) or Fiji/ImageJ (v.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Fiji v2.3, ImageJ v2.3, SCENIC, WGCNA]

### Maturation and circuit integration of transplanted human cortical organoids. (Nature 2022)

- DOI: 10.1038/s41586-022-05277-w | PMCID: PMC9556304 | PMID: 36224417
- Version used: **2.1.0**
- Evidence: The files were next loaded into Fiji (ImageJ, version 2.1.0; NIH) plugin SimpleNeuriteTracer 41 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Fiji v2.1.0, ImageJ, R v4.1.2, Seurat v4.1.1, edgeR v3.36.0, scDblFinder]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: Imaging data were analysed using Fiji (ImageJ) software (NIH). scRNA-seq and analysis Relating to the dataset introduced in Fig.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Nuclear chromosome locations dictate segregation error frequencies. (Nature 2022)

- DOI: 10.1038/s41586-022-04938-0 | PMCID: PMC9300461 | PMID: 35831506
- Version used: **2.0.0**
- Evidence: Image analysis and quantification was done using Fiji ImageJ (v.2.0.0).
- Full pipeline: read trimming [Bowtie2 v2.3.4, Cutadapt v1.16] -> alignment/mapping [Bowtie2 v2.3.4, Cutadapt v1.16] -> quantification [Fiji v2.0.0, ImageJ v2.0.0]

### MCM complexes are barriers that restrict cohesin-mediated loop extrusion. (Nature 2022)

- DOI: 10.1038/s41586-022-04730-0 | PMCID: PMC9159944 | PMID: 35585235
- Evidence: Image analysis was performed in Fiji/ImageJ.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ, NumPy, Python, SciPy, ggplot2]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: The number of Nfix + , GFP + and Nfix + GFP + cells was quantified using Fiji/ImageJ from the centre three optical slices by an investigator blinded to condition.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### A multidimensional coding architecture of the vagal interoceptive system. (Nature 2022)

- DOI: 10.1038/s41586-022-04515-5 | PMCID: PMC8967724 | PMID: 35296859
- Evidence: Area innervated by vagal afferents retrogradely labelled from various visceral organs at different Bregma levels (−7.20, −7.32, −7.48, −7.56, −7.76, −7.92, −8.0 mm) were measured using Fiji (ImageJ) ( Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [R, Seurat, UMAP, pheatmap] -> stage not stated [CellPhoneDB, Fiji, ImageJ]

### Altered TMPRSS2 usage by SARS-CoV-2 Omicron impacts infectivity and fusogenicity. (Nature 2022)

- DOI: 10.1038/s41586-022-04474-x | PMCID: PMC8942856 | PMID: 35104837
- Evidence: For distance analysis, the two-dimensional coordinates of the centroids of spike proteins were calculated using the Analyze Particles module of Fiji (ImageJ).
- Full pipeline: read trimming [Bowtie2 v2.3.4.3] -> alignment/mapping [Bowtie2 v2.3.4.3] -> dimensionality reduction/clustering [Fiji] -> visualisation [ChimeraX v1.3] -> stage not stated [GROMACS, ImageJ, Pangolin, Scanpy v1.7.1]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Version used: **1.53k**
- Evidence: Maximum-intensity projections of the lattice videos were generated using Fiji (ImageJ 1.53k).
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### Stress granules plug and stabilize damaged endolysosomal membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06726-w | PMCID: PMC10686833 | PMID: 37968398
- Evidence: Stress granules and GAL-3 puncta analysis Analysis was done in Fiji/ImageJ using the sequence Image>Adjust>Threshold and then puncta or area in the segmented image was determined using the menu command Analyze>Analyze particles.
- Full pipeline: dimensionality reduction/clustering [Python] -> stage not stated [Fiji, ImageJ, MACS2, PHENIX, R v3.0]

### Assembloid CRISPR screens reveal impact of disease genes in human neurodevelopment. (Nature 2023)

- DOI: 10.1038/s41586-023-06564-w | PMCID: PMC10567561 | PMID: 37758944
- Version used: **1.0**
- Evidence: Images were analysed with Imaris (Oxford Instruments, v.9.7.0) and Fiji (ImageJ, v.1.0 and v.1.53f51).
- Full pipeline: normalisation [ComplexHeatmap, R, Seurat] -> visualisation [ComplexHeatmap] -> stage not stated [Fiji v1.0, ImageJ v1.0, ggplot2]

### A microscale soft ionic power source modulates neuronal network activity. (Nature 2023)

- DOI: 10.1038/s41586-023-06295-y | PMCID: PMC10468398 | PMID: 37648756
- Evidence: Images were processed using the Leica Application Suite X and Fiji (ImageJ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: A line along the pia was drawn manually in Fiji ImageJ for each image.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### A rise-to-threshold process for a relative-value decision. (Nature 2023)

- DOI: 10.1038/s41586-023-06271-6 | PMCID: PMC10356611 | PMID: 37407812
- Evidence: Images were analysed using Fiji (ImageJ).
- Full pipeline: registration [CaImAn] -> stage not stated [DeepLabCut, Fiji, ImageJ]

### Phase separation of FSP1 promotes ferroptosis. (Nature 2023)

- DOI: 10.1038/s41586-023-06255-6 | PMCID: PMC10338336 | PMID: 37380771
- Evidence: Average sizes of condensates were calculated by Fiji/ImageJ. d .
- Full pipeline: visualisation [CellProfiler v4.1.3] -> stage not stated [AlphaFold, ColabFold, Fiji, ImageJ]

### Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor. (Nature 2023)

- DOI: 10.1038/s41586-023-06179-1 | PMCID: PMC7614784 | PMID: 37344587
- Evidence: Percentage ATP hydrolysis was calculated using Fiji (ImageJ).
- Full pipeline: alignment/mapping [ChimeraX] -> machine learning [RELION v3.1] -> stage not stated [AlphaFold, Fiji, ImageJ, PHENIX, Topaz]

### Class B1 GPCR activation by an intracellular agonist. (Nature 2023)

- DOI: 10.1038/s41586-023-06169-3 | PMCID: PMC10307627 | PMID: 37286611
- Evidence: The co-localization index for individual cells in each stimulation condition was calculated using Fiji (ImageJ).
- Full pipeline: registration [RELION] -> simulation/modelling [MDTraj v1.9.8, NAMD v2.13, seaborn] -> visualisation [MDTraj v1.9.8, seaborn] -> stage not stated [Fiji, ImageJ, VMD v1.9.3]

### A median fin derived from the lateral plate mesoderm and the origin of paired fins. (Nature 2023)

- DOI: 10.1038/s41586-023-06100-w | PMCID: PMC10266977 | PMID: 37225983
- Version used: **1.52p**
- Evidence: Microscopy images (fluorescence and bright field) were analysed by ZEN Blue v.3.6 (Zeiss), Fiji (ImageJ v.1.52p) and IMARIS v.9.9.1 (Oxford Instruments).
- Full pipeline: stage not stated [Fiji v1.52p, ImageJ v1.52p]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: Colocalization analysis was conducted using the Fiji/ImageJ Coloc2 plugin.
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### The cellular coding of temperature in the mammalian cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05705-5 | PMCID: PMC9946826 | PMID: 36755097
- Evidence: Images were acquired with a Zeiss microscope (AX10) using a 5× objective and processed using Fiji (ImageJ, NIH, USA).
- Full pipeline: registration [Python, Suite2p] -> stage not stated [Fiji, ImageJ, Kilosort]

### Microglia regulate central nervous system myelin growth and integrity. (Nature 2023)

- DOI: 10.1038/s41586-022-05534-y | PMCID: PMC9812791 | PMID: 36517604
- Evidence: Cell counts were calculated from a measured area based on assumption of circularity using Fiji/ImageJ (Fiji.sc), with three regions of interest quantified per section.
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [QuPath v0.3.0, ggplot2 v3.3.5]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: Adipocyte size quantification Images of ingAT and epiAT were taken with 3DHISTECH Slide Viewer 2 and then analysed with Adiposoft 69 using Fiji ImageJ 70 .
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: For registration, we used BigWarp 71 , which was packaged in the Fiji/ImageJ software application.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: Images were processed using Fiji ImageJ (v.154f) software 127 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: Blot intensities were quantified with Fiji (ImageJ) Analyse-Gel module.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Evidence: Fibrinogen immunoreactivity was quantified using Fiji (ImageJ) as described previously 70 .
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Evidence: Images were processed using Fiji ImageJ.
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### Adenosine signalling to astrocytes coordinates brain metabolism and function. (Nature 2024)

- DOI: 10.1038/s41586-024-07611-w | PMCID: PMC11291286 | PMID: 38961289
- Evidence: Data analysis Imaging data were acquired using IQ3 software (v6.3; Andor, Oxford Instruments) or Olympus FluoView software (v4; Olympus) and analysed using Fiji (ImageJ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ, R v4.2.2, Seurat, UMAP] -> stage not stated [Fiji]

### Antisense oligonucleotide therapeutic approach for Timothy syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07310-6 | PMCID: PMC11043036 | PMID: 38658687
- Version used: **2.1.0**
- Evidence: Mean grey values were collected from ROIs delineating Calbryte + somas (visualized by standard deviation projection of the entire time series) with Fiji (ImageJ v.2.1.0, NIH).
- Full pipeline: visualisation [Fiji v2.1.0] -> stage not stated [ImageJ]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **2.14.0**
- Evidence: The acquired images were composed, edited and analysed using Fiji (ImageJ, v.2.14.0/1,54f).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### Network-level encoding of local neurotransmitters in cortical astrocytes. (Nature 2024)

- DOI: 10.1038/s41586-024-07311-5 | PMCID: PMC11062919 | PMID: 38632406
- Evidence: To quantify loss of Cx43 in RFP + and RFP − astrocytes, Fiji (ImageJ) was used.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [statsmodels v0.12.2] -> stage not stated [SciPy v1.6.2]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Evidence: All analyses were performed with Fiji/ImageJ.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: Image analysis to quantify AT8 or caspase-3 positivity in hiPS cell-derived neuron stains was performed using custom macros written in the open-source Fiji (ImageJ) software.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### A vagal reflex evoked by airway closure. (Nature 2024)

- DOI: 10.1038/s41586-024-07144-2 | PMCID: PMC10972749 | PMID: 38448588
- Version used: **1.52p**
- Evidence: Two-channel images were motion-corrected using the ‘Image Stabilizer’ plugin in Fiji ImageJ (v.1.52p).
- Full pipeline: quality control [R v4.1.3, Seurat v4.1.1] -> alignment/mapping [R v4.1.3, Seurat v4.1.1] -> normalisation [R v4.1.3, Seurat v4.1.1] -> dimensionality reduction/clustering [R v4.1.3, Seurat v4.1.1, UMAP] -> differential/statistical testing [Enrichr, R v4.1.3, Seurat v4.1.1] -> stage not stated [Fiji v1.52p, ImageJ v1.52p]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Version used: **1.53c**
- Evidence: Images were analysed using the open-source software Fiji (ImageJ, v.1.53c).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Modelling post-implantation human development to yolk sac blood emergence. (Nature 2024)

- DOI: 10.1038/s41586-023-06914-8 | PMCID: PMC10849971 | PMID: 38092041
- Evidence: Image acquisition and processing Images were acquired using the EVOS M700 automated scanning microscope (M7000 Software Revision v.2.0.2094.0), Leica SP8 confocal microscope (Leica Application Suite X v.3.7.4), Sartorius Incucyte S3 Live Cell Imaging System (software v.v2019B) or Nikon A1 confocal microscope, and processed using Fiji/ImageJ software (National Institutes of Health, NIH) 63 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Enrichr, Fiji, ImageJ, Seurat]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: Images stained for CD11B (microglia marker) were normalized to 0.35% pixel saturation to standardize microglia segmentation (outlining) in Fiji/ImageJ 73 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### SARS-CoV-2 mRNA vaccines sensitize tumours to immune checkpoint blockade. (Nature 2025)

- DOI: 10.1038/s41586-025-09655-y | PMCID: PMC12611756 | PMID: 41125896
- Evidence: Image processing was performed using Fiji ImageJ software (NIH) and Imaris (Oxford Instruments).
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Fiji, ImageJ, R]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Version used: **2.1.0**
- Evidence: All images were acquired with Zen 3.4 and analysed using Fiji ImageJ 2.1.0.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### DNA2 enables growth by restricting recombination-restarted replication. (Nature 2025)

- DOI: 10.1038/s41586-025-09470-5 | PMCID: PMC12545200 | PMID: 40903580
- Evidence: Bright-field microscopy images of logarithmically growing cells were taken using a Nikon Eclipse E400 microscope with ×10 magnification to determine the cell length using Fiji (ImageJ; v.1.53t) 68 .
- Full pipeline: stage not stated [Fiji, ImageJ]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Version used: **1.54f**
- Evidence: Images were acquired on an automated Nikon Eclipse Ti2 microscope fitted with the Yokogawa spinning-disk field-scanning confocal system and Photometrics PRIME 95B sCMOS camera, using a ×20 objective. z stack images were deconvolved using Nikon NIS-Elements AR5.20.01 software and processed with Fiji/ImageJ (1.54f, 64 bit).
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Patterned invagination prevents mechanical instability during gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09480-3 | PMCID: PMC12527948 | PMID: 40903575
- Version used: **2.16.0**
- Evidence: Image processing and visualization We converted the raw light-sheet imaging datasets into individual TIFF stacks for downstream processing using a custom macro (ProcessZ1Coverslip.ijm) in Fiji/ImageJ (v2.16.0/1.54p) with Java (v1.8.0_172) 41 , 42 .
- Full pipeline: differential/statistical testing [Jupyter, Python v3.10.7, R v4.2.1] -> visualisation [Fiji v2.16.0, ImageJ v2.16.0] -> stage not stated [ilastik v1.3.3b]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Lesion sizes were calculated in Fiji (ImageJ version 1) by tracing the fibroblast–astrocyte border (using ER-TR7 and/or GFAP).
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Evidence: For mouse tissue confocal microscopy, three representative images per biological replicate ( n = 5) were acquired and quantified in Fiji (ImageJ) with BioVoxxel Toolbox for Voronoi segmentation.
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Version used: **2.9.0**
- Evidence: For analysis of the Aβ plaque burden, pictures of Aβ immunoreactivity (using the rabbit anti-Aβ monoclonal antibody, clone D54D2, Cell Signaling, 8243, dilution 1:250) in the hippocampus were processed using a macro developed for use with Fiji/ImageJ 2.9.0.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: To visualize the wound, adjacent positions were stitched using the Stitching plugin from Fiji ImageJ.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Version used: **2.0.0**
- Evidence: Data were processed with Fiji/ImageJ (v.2.0.0, NIH) as follows: images were converted to 8-bit, each brain was manually encircled and its area was recorded.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Serotonin and neurotensin inputs in the vCA1 dictate opposing social valence. (Nature 2025)

- DOI: 10.1038/s41586-025-08809-2 | PMCID: PMC12137126 | PMID: 40307550
- Version used: **1.52p**
- Evidence: A Fiji (ImageJ v.1.52p) macro was used for automated image analysis, which was performed blinded.
- Full pipeline: stage not stated [Fiji v1.52p, ImageJ v1.52p]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Quantification was performed using Fiji (ImageJ) 54 (Extended Data Fig.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Version used: **2.9.0**
- Evidence: The data were quantified using Fiji ImageJ v.2.9.0.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### The conserved HIV-1 spacer peptide 2 triggers matrix lattice maturation. (Nature 2025)

- DOI: 10.1038/s41586-025-08624-9 | PMCID: PMC11964938 | PMID: 40011770
- Version used: **1.54f**
- Evidence: 4e–h , greyscales were made similar using Fiji (ImageJ v1.54f).
- Full pipeline: structure determination [PHENIX] -> visualisation [RELION] -> stage not stated [AlphaFold v2.2.0, ChimeraX v1.3, Clustal Omega, Fiji v1.54f, ImageJ v1.54f]

### Mis-splicing of a neuronal microexon promotes CPEB4 aggregation in ASD. (Nature 2025)

- DOI: 10.1038/s41586-024-08289-w | PMCID: PMC11711090 | PMID: 39633052
- Evidence: NIS Elements AR (v.5.30.05) software was used for acquisition, and Fiji/ImageJ software was used to adjust images for visualization. mEGFP–CPEB4 neuronal stimulation with NMDA Primary striatal neurons from mEGFP–CPEB4 mice were imaged at 14–21 days of differentiation, and where specified, neuron stimulation was induced by the addition of 20 µM NMDA (Tocris, 0114), a selective NMDA receptor agonist...
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj, OpenMM v7.5] -> visualisation [Fiji, ImageJ] -> stage not stated [VMD]

### The oestrous cycle stage affects mammary tumour sensitivity to chemotherapy. (Nature 2025)

- DOI: 10.1038/s41586-024-08276-1 | PMCID: PMC11666466 | PMID: 39633046
- Version used: **1.49k**
- Evidence: For determination of positive cells, staining was quantified using Fiji/ImageJ v.1.49k and Excel 2016.
- Full pipeline: quantification [Fiji v1.49k, QuPath v0.4.4] -> dimensionality reduction/clustering [ImageJ] -> differential/statistical testing [R v4.4.2] -> machine learning [QuPath v0.4.4] -> stage not stated [ggplot2, tidyverse]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Buds per organoid and the percentage of budding organoids were estimated from day 6/7 images which were counted manually using Fiji/ImageJ (NIH).
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### HIV-1 signalling remodels nuclear pores to licence infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10453-3 | PMCID: PMC13293875 | PMID: 42092137
- Evidence: HIV-1 GFP–CA + target T cells were manually scored for GFP–CA cellular localization using Fiji ImageJ’s plot profile function.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [CellProfiler, Fiji, ImageJ]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: Raw images were exported from Nikon NIS-Elements software (v.5.41.02), split into individual channels using Fiji ImageJ software, and saved as .tif files.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Confocal images were processed and analysed using Fiji (ImageJ).
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Version used: **2.3.0**
- Evidence: Quantifications were performed using Fiji/ImageJ (v.2.3.0/1.53q) as previously described 5 .
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### Structural basis of supercoiling-induced CRISPR-Cas9 off-target activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10255-7 | PMCID: PMC13171457 | PMID: 41882360
- Evidence: Gels were analysed on Fiji (ImageJ), and intensities for SC, linear and background bands were measured.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, RELION] -> stage not stated [AlphaFold, Fiji, ImageJ, Topaz]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Raw images were processed using Fiji/ImageJ 111 , using functions for background subtraction (25 px) and despeckling.
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### A membrane-bound nuclease directly cleaves phage DNA during genome injection. (Nature 2026)

- DOI: 10.1038/s41586-026-10207-1 | PMCID: PMC13190303 | PMID: 41741653
- Evidence: Image analysis was done using Fiji (ImageJ).
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> stage not stated [Fiji, HMMER, ImageJ]

### CLCC1 governs ER bilayer equilibration to maintain lipid homeostasis. (Nature 2026)

- DOI: 10.1038/s41586-026-10161-y | PMCID: PMC13061606 | PMID: 41741642
- Evidence: Images were acquired on the ZEISS 900 confocal microscope with Airyscan2 (Carl Zeiss) controlled by ZEISS ZEN v.3.2 (blue edition) and processed with Fiji (ImageJ distribution, v.2.1.0; based on ImageJ, NIH; https://imagej.net/software/fiji/ ).
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [R] -> structure determination [IMOD] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX v1.7.1, Fiji, ImageJ]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Version used: **1.53e**
- Evidence: Immunoblots were visualized on a LI-COR imager (LI-COR Biosciences) running Odyssey v.3.0, and Fiji/ImageJ v.1.53e (NIH) was used for quantification of protein levels.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Version used: **1.53c**
- Evidence: Images were quantified using Fiji ImageJ (v.1.53c) without blinding.
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### Vagal blood volume receptors compensate for haemorrhage and posture change. (Nature 2026)

- DOI: 10.1038/s41586-025-10010-4 | PMCID: PMC13017543 | PMID: 41606321
- Evidence: Two-channel images were processed, analysed and classified as previously described using Fiji ImageJ and Microsoft Excel 18 .
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ, ilastik, scikit-image]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Evidence: The lengths of red (CldU) or green (IdU) labelled patches were measured using Fiji ImageJ (National Institutes of Health).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Albumin orchestrates a natural host defence mechanism against mucormycosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09882-3 | PMCID: PMC12804082 | PMID: 41501454
- Evidence: Certain images were acquired with a Leica TCS SP8 confocal microscope with a ×63 lens and analysed with the use of Fiji/ImageJ.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> differential/statistical testing [R v4.3.1] -> visualisation [R v4.3.1] -> stage not stated [Fiji, GSEA, ImageJ, pheatmap]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **2.1.1**
- Evidence: Representative images of microscopy experiments were prepared using Fiji (ImageJ, v.2.1.1/1.53i).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Images were further processed using Fiji/ImageJ software (v1.53t) 65 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### SIGLEC12 mediates plasma membrane rupture during necroptotic cell death. (Nature 2026)

- DOI: 10.1038/s41586-025-09741-1 | PMCID: PMC12779560 | PMID: 41225007
- Evidence: Images were analysed using Fiji/ImageJ.
- Full pipeline: quality control [FastQC v0.11.2] -> alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [Fiji, ImageJ]

### In vivo visualization of butterfly scale cell morphogenesis in <i>Vanessa cardui</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2112009118 | PMCID: PMC8670486 | PMID: 34845021
- Evidence: The color representations of 3D amplitude data are based on the Temporal-Color Code plugin by Kota Miura for Fiji/ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Direct imaging of intraflagellar-transport turnarounds reveals that motors detach, diffuse, and reattach to opposite-direction trains. (PNAS 2021)

- DOI: 10.1073/pnas.2115089118 | PMCID: PMC8609318 | PMID: 34732580
- Evidence: To further characterize and quantify the diffusion behavior, we extracted single-molecule trajectories from the original image sequences of all three IFT motors with single-particle tracking using the Fiji/ImageJ ( 35 ) plugin Trackmate ( 32 ).
- Full pipeline: quantification [Fiji, ImageJ] -> simulation/modelling [Fiji, ImageJ]

### Dim light in the evening causes coordinated realignment of circadian rhythms, sleep, and short-term memory. (PNAS 2021)

- DOI: 10.1073/pnas.2101591118 | PMCID: PMC8488663 | PMID: 34556572
- Evidence: Identical settings were used to acquire images of each region from the four different conditions, and cFos-immunoreactive nuclei were quantified in Fiji ImageJ ( 115 ).
- Full pipeline: quantification [Fiji, ImageJ] -> stage not stated [R]

### Morphological cell profiling of SARS-CoV-2 infection identifies drug repurposing candidates for COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2105815118 | PMCID: PMC8433531 | PMID: 34413211
- Evidence: Representative image was acquired on a Yokogawa CQ1 high-content imager with a 60× lens and visualized with Fiji ImageJ.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ] -> stage not stated [CellProfiler, scikit-learn]

### Wild-type GBA1 increases the α-synuclein tetramer-monomer ratio, reduces lipid-rich aggregates, and attenuates motor and cognitive deficits in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2103425118 | PMCID: PMC8346893 | PMID: 34326260
- Evidence: Image analyses were done using Fiji ImageJ Software (NIH).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Microscopic origins of the crystallographically preferred growth in evaporation-induced colloidal crystals. (PNAS 2021)

- DOI: 10.1073/pnas.2107588118 | PMCID: PMC8364128 | PMID: 34341109
- Evidence: The collected 3D stacks of tomography images were first aligned by using Fiji/ImageJ (NIH).
- Full pipeline: alignment/mapping [Fiji, ImageJ]

### A phage mechanism for selective nicking of dUMP-containing DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2026354118 | PMCID: PMC8201957 | PMID: 34074772
- Evidence: The captured images were processed further using Fiji ImageJ suite ( 23 ).
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [GATK v3.7] -> variant calling [Cutadapt] -> stage not stated [Fiji, ImageJ, VEP]

### Disrupted osteocyte connectivity and pericellular fluid flow in bone with aging and defective TGF-β signaling. (PNAS 2021)

- DOI: 10.1073/pnas.2023999118 | PMCID: PMC8237574 | PMID: 34161267
- Evidence: Femurs from male young (2 mo, n = 3) and aged (35 to 37 mo, n = 5) C57BL/6 mice (Buck Institute) and male young (2 mo) TβRII ocy−/− mice and their TβRII ctrl littermates ( n = 4 to 5 each) were prepared for histological examination via silver nitrate staining as described elsewhere ( 9 , 49 , 57 ) and two-dimensional (2D) canalicular length quantified utilizing Fiji/ImageJ ( 60 ).
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [Fiji, ImageJ]

### Resetting proteostasis with ISRIB promotes epithelial differentiation to attenuate pulmonary fibrosis. (PNAS 2021)

- DOI: 10.1073/pnas.2101100118 | PMCID: PMC8157939 | PMID: 33972447
- Version used: **1.8.0**
- Evidence: Apoptotic AT2 cells (TUNEL+/pro-SPC+) were counted using Fiji (ImageJ, v.1.8.0).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> alignment/mapping [FastQC, Trimmomatic v0.36] -> differential/statistical testing [edgeR v3.28.0] -> stage not stated [Fiji v1.8.0, HTSeq v0.11.2, ImageJ v1.8.0]

### Transcriptional profiling reveals signatures of latent developmental potential in <i>Arabidopsis</i> stomatal lineage ground cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021682118 | PMCID: PMC8092560 | PMID: 33875598
- Evidence: Z- stacks through the epidermis were generated and analyzed by Leica LAS and by Fiji (ImageJ, NIH).
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [Bowtie2, DESeq2] -> stage not stated [Fiji, ImageJ]

### Presynaptic α&lt;sub&gt;2&lt;/sub&gt;δ subunits are key organizers of glutamatergic synapses. (PNAS 2021)

- DOI: 10.1073/pnas.1920827118 | PMCID: PMC8040823 | PMID: 33782113
- Evidence: ( A ) Putative synaptic varicosities from neurons cotransfected with SynGCaMP6f and mCherry were selected in Fiji/ImageJ using the ROI tool (yellow circles).
- Full pipeline: quantification [ImageJ] -> stage not stated [Fiji]

### <i>Drosophila</i> Fezf functions as a transcriptional repressor to direct layer-specific synaptic connectivity in the fly visual system. (PNAS 2021)

- DOI: 10.1073/pnas.2025530118 | PMCID: PMC8020669 | PMID: 33766917
- Evidence: Fluorescence images were acquired using Zeiss LSM 800 Confocal Microscope and processed with Fiji ImageJ imaging software.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2, MACS2 v2.1.1] -> stage not stated [Fiji, ImageJ]

### SOX9-COL9A3-dependent regulation of choroid plexus epithelial polarity governs blood-cerebrospinal fluid barrier integrity. (PNAS 2021)

- DOI: 10.1073/pnas.2009568118 | PMCID: PMC8017668 | PMID: 33526661
- Version used: **1.43**
- Evidence: Fluorescence intensity and Golgi orientation were analyzed using Fiji/ImageJ version 1.43.
- Full pipeline: stage not stated [Fiji v1.43, ImageJ v1.43]

### KIF2A deficiency causes early-onset neurodegeneration. (PNAS 2022)

- DOI: 10.1073/pnas.2209714119 | PMCID: PMC9674219 | PMID: 36343267
- Evidence: To quantify fluorescence, we analyzed an area of 350 µm width per 1,150 µm height in Fiji (ImageJ).
- Full pipeline: quantification [Fiji, ImageJ]

### Neuronal signature of spatial decision-making during navigation by freely moving rats by using calcium imaging. (PNAS 2022)

- DOI: 10.1073/pnas.2212152119 | PMCID: PMC9636941 | PMID: 36279456
- Version used: **2.1**
- Evidence: Confocal and microscope images were open and processed with Fiji/ImageJ v2.1 (NIH); linear transformation of brightness and contrast was applied uniformly and equally to all compared images or channels.
- Full pipeline: machine learning [CaImAn] -> stage not stated [Fiji v2.1, ImageJ v2.1, Python]

### Disruption of proteostasis causes IRE1 mediated reprogramming of alveolar epithelial cells. (PNAS 2022)

- DOI: 10.1073/pnas.2123187119 | PMCID: PMC9618079 | PMID: 36252035
- Version used: **1.8.0**
- Evidence: Images were analyzed on Fiji (ImageJ, v.1.8.0) with quantification methods detailed in the SI Appendix .
- Full pipeline: quantification [Fiji v1.8.0, ImageJ v1.8.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [MACS2]

### Tetraspanin-5-mediated MHC class I clustering is required for optimal CD8 T cell activation. (PNAS 2022)

- DOI: 10.1073/pnas.2122188119 | PMCID: PMC9586303 | PMID: 36215490
- Evidence: Images were further processed using Fiji/ImageJ software ( 79 ) followed by a custom pipeline designed to analyze MHC I clusters at the PM (Cell Profiler, Broad Institute) ( 80 ).
- Full pipeline: dimensionality reduction/clustering [Fiji, ImageJ]

### Mechanical coupling of supracellular stress amplification and tissue fluidization during exit from quiescence. (PNAS 2022)

- DOI: 10.1073/pnas.2201328119 | PMCID: PMC9371707 | PMID: 35914175
- Evidence: Subsequently, all images in a time series were subjected to image registration using the descriptor-based series registration plugin in Fiji ImageJ ( 59 ).
- Full pipeline: registration [Fiji, ImageJ] -> machine learning [StarDist]

### Wnt signaling regulates hepatocyte cell division by a transcriptional repressor cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2203849119 | PMCID: PMC9335208 | PMID: 35867815
- Evidence: Hepatocyte nuclei were detected automatically with the “analyze particles” feature of Fiji (ImageJ) software to encircle GFP- or HNF4α-positive nuclei and selected regions were validated or corrected manually when necessary.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [Fiji, ImageJ, MACS2]

### Competition between growth and shear stress drives intermittency in preferential flow paths in porous medium biofilms. (PNAS 2022)

- DOI: 10.1073/pnas.2122202119 | PMCID: PMC9335220 | PMID: 35858419
- Evidence: To obtain an image of the entire porous domain, images of the array of positions were stitched using Fiji ImageJ ( 63 ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Fast, strong, and reversible adhesives with dynamic covalent bonds for potential use in wound dressing. (PNAS 2022)

- DOI: 10.1073/pnas.2203074119 | PMCID: PMC9304023 | PMID: 35858303
- Evidence: (The contact region diameter was measured by Fiji ImageJ.) In order to quantify the results shown in Fig.
- Full pipeline: quantification [Fiji, ImageJ]

### An immature, dedifferentiated, and lineage-deconstrained cone precursor origin of N-Myc-initiated retinoblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2200721119 | PMCID: PMC9282279 | PMID: 35867756
- Evidence: The Weka plugin ( 21 ) was obtained via Fiji/ImageJ and used to train the segmentation algorithm with randomly chosen DAPI-stained confocal images.
- Full pipeline: stage not stated [Fiji, ImageJ]

### A long noncoding RNA influences the choice of the X chromosome to be inactivated. (PNAS 2022)

- DOI: 10.1073/pnas.2118182119 | PMCID: PMC9282422 | PMID: 35787055
- Evidence: Z-stacks were captured on a Leica SP5 confocal microscope (Leica Microsystems, Germany) and images were prepared with Fiji/ImageJ software.
- Full pipeline: read trimming [Trimmomatic v0.36.6] -> alignment/mapping [Bowtie2 v2.3.4.2] -> stage not stated [Fiji, ImageJ, SAMtools v1.1.2]

### Ablation of lysophosphatidic acid receptor 1 attenuates hypertrophic cardiomyopathy in a mouse model. (PNAS 2022)

- DOI: 10.1073/pnas.2204174119 | PMCID: PMC9282378 | PMID: 35787042
- Evidence: Visualization and background removal (rolling ball radius) were done using Fiji/ImageJ.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ, UMAP] -> stage not stated [R v4.0, Seurat v3.1, scDblFinder]

### Two light sensors decode moonlight versus sunlight to adjust a plastic circadian/circalunidian clock to moon phase. (PNAS 2022)

- DOI: 10.1073/pnas.2115725119 | PMCID: PMC9295771 | PMID: 35622889
- Evidence: Image analysis was performed using the software Fiji/ImageJ ( 53 ).
- Full pipeline: stage not stated [Cellpose, Fiji, ImageJ]

### K<sub>v</sub>1.1 preserves the neural stem cell pool and facilitates neuron maturation during adult hippocampal neurogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2118240119 | PMCID: PMC9295736 | PMID: 35613055
- Evidence: Images were processed and analyzed using Fiji (ImageJ, NIH).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Mast cell infiltration of the choroid and protease release are early events in age-related macular degeneration associated with genetic risk at both chromosomes 1q32 and 10q26. (PNAS 2022)

- DOI: 10.1073/pnas.2118510119 | PMCID: PMC9171765 | PMID: 35561216
- Evidence: Images were then processed and analyzed using Fiji ImageJ ( https://imagej.net/Fiji/Downloads ).
- Full pipeline: quantification [CellProfiler] -> normalisation [R] -> differential/statistical testing [R, afex] -> stage not stated [Fiji, ImageJ]

### Targeted ubiquitination of sensory neuron calcium channels reduces the development of neuropathic pain. (PNAS 2022)

- DOI: 10.1073/pnas.2118129119 | PMCID: PMC9171802 | PMID: 35561213
- Evidence: Image analysis was done with the Fiji ImageJ program.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Single molecule tracking of bacterial cell surface cytochromes reveals dynamics that impact long-distance electron transport. (PNAS 2022)

- DOI: 10.1073/pnas.2119964119 | PMCID: PMC9171617 | PMID: 35503913
- Evidence: First, Fiji (ImageJ) software was used to convert the time-lapse microscopy data to TIFF image sequence files that could be opened by SLIMfast in MATLAB.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Sensitivity of <i>VHL</i> mutant kidney cancers to HIF2 inhibitors does not require an intact p53 pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2120403119 | PMCID: PMC9168943 | PMID: 35357972
- Evidence: Colonies were quantified with Fiji ImageJ ( 44 ).
- Full pipeline: quantification [Fiji, ImageJ]

### Cell size and polarization determine cytokinesis furrow ingression dynamics in mouse embryos. (PNAS 2022)

- DOI: 10.1073/pnas.2119381119 | PMCID: PMC8944651 | PMID: 35294282
- Evidence: All fluorescence intensity measurements were performed using Fiji/ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ]

### A dialogue-like cell communication mechanism is conserved in filamentous ascomycete fungi and mediates interspecies interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2112518119 | PMCID: PMC8944665 | PMID: 35286209
- Evidence: Simple image analyses were performed with Fiji (ImageJ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Abolishing the prelamin A ZMPSTE24 cleavage site leads to progeroid phenotypes with near-normal longevity in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2118695119 | PMCID: PMC8892526 | PMID: 35197292
- Evidence: For quantification, films were scanned with a digital scanner and the band signal intensities were quantified using Fiji ImageJ ( https://imagej.net/software/fiji/ ) and analyzed using Excel (Microsoft).
- Full pipeline: quantification [Fiji, ImageJ]

### ER-phagy requires the assembly of actin at sites of contact between the cortical ER and endocytic pits. (PNAS 2022)

- DOI: 10.1073/pnas.2117554119 | PMCID: PMC8833162 | PMID: 35101986
- Evidence: Acquired images were further processed with Open Lab (Improvision), Fiji ImageJ, or Photoshop CS4 (Adobe) software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### THESEUS1 modulates cell wall stiffness and abscisic acid production in <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2119258119 | PMCID: PMC8740707 | PMID: 34949719
- Evidence: Images obtained from Leica TCS SP8 (Leica Microsystems) were processed in Fiji (ImageJ), and images obtained from LSM 800 (Carl Zeiss) were processed as single plane maximum intensity projections of three optical sections in Zen Blue 3.3 software (Carl Zeiss).
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [Fiji, ImageJ]

### Adaptive DNA amplification of synthetic gene circuit opens a way to overcome cancer chemoresistance. (PNAS 2023)

- DOI: 10.1073/pnas.2303114120 | PMCID: PMC10710087 | PMID: 38019857
- Evidence: We used Nikon Elements AR v4.40.00 (Build 1084) to collect and analyze imaging data, in addition to Fiji (ImageJ) and the Image Processing Toolbox in MATLAB (MathWorks, Inc.).
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.6.1d] -> quantification [featureCounts] -> stage not stated [Fiji, ImageJ, R v4.1, fastp v0.20.1]

### rDNA magnification is a unique feature of germline stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2314440120 | PMCID: PMC10666004 | PMID: 37967216
- Evidence: Samples were imaged using a Leica Stellaris 8 confocal microscope with 63× oil-immersion objectives and processed using Fiji (ImageJ) software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### IL-38 regulates intestinal stem cell homeostasis by inducing WNT signaling and beneficial IL-1β secretion. (PNAS 2023)

- DOI: 10.1073/pnas.2306476120 | PMCID: PMC10636342 | PMID: 37906644
- Evidence: Organoid size was measured using Fiji (ImageJ) software in pixel 2 ; every measurement was normalized with the average of the control group for each experiment.
- Full pipeline: normalisation [Fiji, ImageJ]

### Cereblon influences the timing of muscle differentiation in <i>Ciona</i> tadpoles. (PNAS 2023)

- DOI: 10.1073/pnas.2309989120 | PMCID: PMC10614628 | PMID: 37856545
- Evidence: Fluorescence intensity measurements were determined on z-stack confocal images using custom scripts in Fiji (ImageJ) ( 70 ).
- Full pipeline: differential/statistical testing [R] -> visualisation [ComplexHeatmap v2.10.0] -> stage not stated [Fiji, ImageJ, Seurat v4.3.0]

### Molecular mechanisms controlling the biogenesis of the TGF-β signal Vg1. (PNAS 2023)

- DOI: 10.1073/pnas.2307203120 | PMCID: PMC10614602 | PMID: 37844219
- Evidence: All images were processed in Fiji/ImageJ ( 77 ).
- Full pipeline: stage not stated [AlphaFold, Fiji, ImageJ]

### LST-1 is a bifunctional regulator that feeds back on Notch-dependent transcription to regulate <i>C. elegans</i> germline stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2309964120 | PMCID: PMC10523584 | PMID: 37729202
- Evidence: Immunostaining quantitation for cytoplasmic proteins was performed using Fiji/ImageJ following previously described protocols ( 15 ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### <i>Coxiella</i> co-opts the Glutathione Peroxidase 4 to protect the host cell from oxidative stress-induced cell death. (PNAS 2023)

- DOI: 10.1073/pnas.2308752120 | PMCID: PMC10483631 | PMID: 37639588
- Evidence: Image analyses were performed using Fiji ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ]

### TRPML3/BK complex promotes autophagy and bacterial clearance by providing a positive feedback regulation of mTOR via PI3P. (PNAS 2023)

- DOI: 10.1073/pnas.2215777120 | PMCID: PMC10450854 | PMID: 37585464
- Evidence: The number of LC3 and ATG16L1 fluorescent puncta per cell was counted using Fiji ImageJ, and more than 20 cells from at least three experiments were used for statistics.
- Full pipeline: differential/statistical testing [Fiji, ImageJ]

### Surface-induced phase separation of reconstituted nascent integrin clusters on lipid membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2301881120 | PMCID: PMC10400992 | PMID: 37494400
- Evidence: Fiji/ImageJ was used to analyze the density and size of β 1 clusters ( 50 ).
- Full pipeline: dimensionality reduction/clustering [Fiji, ImageJ]

### Inactive PARP1 causes embryonic lethality and genome instability in a dominant-negative manner. (PNAS 2023)

- DOI: 10.1073/pnas.2301972120 | PMCID: PMC10401025 | PMID: 37487079
- Evidence: All images’ analyses were carried out with Fiji ImageJ software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Geometrical control of interface patterning underlies active matter invasion. (PNAS 2023)

- DOI: 10.1073/pnas.2219708120 | PMCID: PMC10372614 | PMID: 37459530
- Evidence: Images were processed using open-source Fiji (ImageJ) software ( https://fiji.sc/ ) and custom-written programs in MATLAB (The MathWorks, Inc.).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Lipopolysaccharide-induced sepsis impairs M2R-GIRK signaling in the mouse sinoatrial node. (PNAS 2023)

- DOI: 10.1073/pnas.2210152120 | PMCID: PMC10334783 | PMID: 37406102
- Version used: **1.53t**
- Evidence: Quantitative fluorescence analysis was performed with the ImageJ-based open-source software package Fiji (ImageJ 1.53t) ( 42 ).
- Full pipeline: differential/statistical testing [R v4.1.0] -> stage not stated [Fiji v1.53t, ImageJ v1.53t]

### EMT activates exocytotic Rabs to coordinate invasion and immunosuppression in lung cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2220276120 | PMCID: PMC10334751 | PMID: 37406091
- Evidence: For fixed cell imaging, the raw images were processed and fluorescent intensity was analyzed in Fiji/ImageJ ( https://imagej.nih.gov/ij/download.html ).
- Full pipeline: stage not stated [Fiji, ImageJ, MACS2]

### A functional logic for neurotransmitter corelease in the cholinergic forebrain pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2218830120 | PMCID: PMC10334726 | PMID: 37399414
- Evidence: Image analysis and processing were done with Fiji/ImageJ software ( 37 ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Long noncoding RNA MALAT1 is dynamically regulated in leader cells during collective cancer invasion. (PNAS 2023)

- DOI: 10.1073/pnas.2305410120 | PMCID: PMC10319025 | PMID: 37364126
- Evidence: The distance between the two leading edges (wound width) was measured by Fiji ImageJ, and the migration rate was calculated by the difference of the initial and final wound width divided by migration time.
- Full pipeline: stage not stated [Fiji, ImageJ, TrackMate]

### The retrotransposon R2 maintains <i>Drosophila</i> ribosomal DNA repeats. (PNAS 2023)

- DOI: 10.1073/pnas.2221613120 | PMCID: PMC10266012 | PMID: 37252996
- Evidence: Images were taken with a Leica Stellaris 8 confocal microscope with 63× oil-immersion objectives and processed using Fiji (ImageJ) software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Discovery of phosphorylated lantibiotics with proimmune activity that regulate the oral microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2219392120 | PMCID: PMC10235938 | PMID: 37216534
- Evidence: The mean intensity of pixels for green (Syto-9; live) and red (PI; dead) signals was measured within biofilm areas of each image, with the slices containing the highest respective signal intensity using custom Fiji (ImageJ) ( 72 ).
- Full pipeline: alignment/mapping [Cytoscape v3.9.1] -> visualisation [Cytoscape v3.9.1] -> stage not stated [Fiji, ImageJ]

### Direct tests of cytochrome <i>c</i> and <i>c</i><sub>1</sub> functions in the electron transport chain of malaria parasites. (PNAS 2023)

- DOI: 10.1073/pnas.2301047120 | PMCID: PMC10175771 | PMID: 37126705
- Evidence: Fiji/ImageJ was used to process and analyze images.
- Full pipeline: alignment/mapping [PyMOL v2.0] -> visualisation [PyMOL v2.0] -> stage not stated [Fiji, ImageJ, PHENIX]

### STAT2 hinders STING intracellular trafficking and reshapes its activation in response to DNA damage. (PNAS 2023)

- DOI: 10.1073/pnas.2216953120 | PMCID: PMC10120020 | PMID: 37036972
- Evidence: Fiji (ImageJ) software Co-localization plugin was utilized to identify protein colocalization, and Pearson’s colocalization coefficient was determined using Fiji software (ImageJ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Regressive changes in sizes of somatosensory cuneate nucleus after sensory loss in primates. (PNAS 2023)

- DOI: 10.1073/pnas.2222076120 | PMCID: PMC10242712 | PMID: 36877853
- Evidence: The outlined Cu images were then saved as a PNG file at 300 dpi for further Fiji/ImageJ analysis.
- Full pipeline: stage not stated [Fiji, ImageJ]

### SUMO/deSUMOylation of the BRI1 brassinosteroid receptor modulates plant growth responses to temperature. (PNAS 2023)

- DOI: 10.1073/pnas.2217255120 | PMCID: PMC9942830 | PMID: 36652487
- Evidence: Plates were scanned and hypocotyls measured using Fiji ImageJ software.
- Full pipeline: stage not stated [Fiji, ImageJ, MACS2]

### Robotic data acquisition with deep learning enables cell image-based prediction of transcriptomic phenotypes. (PNAS 2023)

- DOI: 10.1073/pnas.2210283120 | PMCID: PMC9910600 | PMID: 36577074
- Evidence: As a comparison, we also classified these cells into three clusters based on their morphological and dynamical features ( Datasets S7–S9 ), which were extracted from the cell images by three representative and well-used conventional image analysis software programs ( 17 ): NIS-Elements ( 18 ), CellProfiler 4 ( 17 ), and TrackMate 7 ( 19 ) in Fiji (ImageJ) ( 20 ) ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [CellProfiler, Fiji, ImageJ, TrackMate]

### Mec1 regulates PAS recruitment of Atg13 via direct binding with Atg13 during glucose starvation-induced autophagy. (PNAS 2023)

- DOI: 10.1073/pnas.2215126120 | PMCID: PMC9910460 | PMID: 36574691
- Evidence: All the images were processed using Fiji ImageJ software and its plugins.
- Full pipeline: simulation/modelling [AlphaFold] -> stage not stated [Fiji, ImageJ]

### Actin polymerization counteracts prewetting of N-WASP on supported lipid bilayers. (PNAS 2024)

- DOI: 10.1073/pnas.2407497121 | PMCID: PMC11648614 | PMID: 39630867
- Version used: **2.9.0**
- Evidence: Images were processed using Fiji/ImageJ 2.9.0.
- Full pipeline: stage not stated [Fiji v2.9.0, ImageJ v2.9.0, ilastik]

### Early disruption of the CREB pathway drives dendritic morphological alterations in FTD/ALS cortical neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2406998121 | PMCID: PMC11626127 | PMID: 39589881
- Evidence: All image analyses were performed using Fiji/ImageJ software ( 85 ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Microtubule poleward flux as a target for modifying chromosome segregation errors. (PNAS 2024)

- DOI: 10.1073/pnas.2405015121 | PMCID: PMC11588092 | PMID: 39541344
- Evidence: Image analysis and measurements were performed in Fiji/ImageJ (NIH).
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ]

### Goblet cell differentiation subgroups in colorectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2414213121 | PMCID: PMC11513979 | PMID: 39401352
- Evidence: Immunofluorescence images were visualised using Fiji/ImageJ ( https://imagej.net/software/fiji/ ) and QuPath ( https://qupath.github.io/ ) software.
- Full pipeline: visualisation [Fiji, ImageJ, QuPath] -> stage not stated [CellProfiler v3.0]

### Paraneoplastic renal dysfunction in fly cancer models driven by inflammatory activation of stem cells. (PNAS 2024)

- DOI: 10.1073/pnas.2405860121 | PMCID: PMC11494367 | PMID: 39392665
- Evidence: ... Stock Center Flybase ID: FBst0091417 UAS-pvf1 RNAi (validated in PMID:32901612) Bloomington Drosophila Stock Center Flybase ID: FBst0039038 Software Fiji ImageJ http://fiji.sc/ Illustrator Adobe https://www.adobe.com/products/illustrator.html Photoshop Adobe https://www.adobe.com/products/photoshopfamily.html Acrobat Adobe https://www.acrobat.adobe.com/us/en/acrobat.html Excel Microsoft https://p...
- Full pipeline: stage not stated [Fiji, ImageJ]

### Mechanically adaptive and deployable intracortical probes enable long-term neural electrophysiological recordings. (PNAS 2024)

- DOI: 10.1073/pnas.2403380121 | PMCID: PMC11459173 | PMID: 39331412
- Evidence: Fluorescence intensity was quantitatively analyzed using Fiji ImageJ software, enabling detailed examination of glial activation and neuron density in response to the implanted neural probes.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Septo-dentate gyrus cholinergic circuits modulate function and morphogenesis of adult neural stem cells through granule cell intermediaries. (PNAS 2024)

- DOI: 10.1073/pnas.2405117121 | PMCID: PMC11459179 | PMID: 39312657
- Evidence: Imaging analysis was performed using Fiji/ImageJ and Imaris.
- Full pipeline: dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> differential/statistical testing [R v4.1] -> simulation/modelling [Slingshot] -> structure determination [Seurat] -> stage not stated [Fiji, ImageJ]

### Nucleated synthetic cells with genetically driven intercompartment communication. (PNAS 2024)

- DOI: 10.1073/pnas.2404790121 | PMCID: PMC11388312 | PMID: 39186653
- Evidence: Image processing was performed with Fiji (ImageJ), and graphs were plotted and analyzed with Prism (GraphPad Software).
- Full pipeline: visualisation [Fiji, ImageJ]

### A PIKfyve modulator combined with an integrated stress response inhibitor to treat lysosomal storage diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2320257121 | PMCID: PMC11348278 | PMID: 39150784
- Evidence: Nuclear localization was quantified using Fiji (ImageJ).
- Full pipeline: quantification [DESeq2, Fiji, ImageJ] -> differential/statistical testing [DESeq2]

### MAVS Cys508 palmitoylation promotes its aggregation on the mitochondrial outer membrane and antiviral innate immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2403392121 | PMCID: PMC11348129 | PMID: 39141356
- Evidence: The images were processed by Fiji ImageJ.
- Full pipeline: quantification [CellProfiler, ImageJ] -> visualisation [Matplotlib, SciPy] -> stage not stated [Fiji]

### A transient radial cortical microtubule array primes cell division in <i>Arabidopsis</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2320470121 | PMCID: PMC11260093 | PMID: 38990951
- Evidence: All the processing of the images was done on the Fiji (ImageJ) software.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Fiji, ImageJ]

### Advanced surface passivation for high-sensitivity studies of biomolecular condensates. (PNAS 2024)

- DOI: 10.1073/pnas.2403013121 | PMCID: PMC11145189 | PMID: 38781207
- Evidence: These image stacks were then processed using Fiji/ImageJ software to generate orthogonal (y-z) views of the condensates.
- Full pipeline: stage not stated [Fiji, ImageJ, TrackMate]

### Dark continuous noise from mutant G90D-rhodopsin predominantly underlies congenital stationary night blindness. (PNAS 2024)

- DOI: 10.1073/pnas.2404763121 | PMCID: PMC11127052 | PMID: 38743626
- Evidence: The intensity of the uncut and cut fragments was quantified using Fiji (ImageJ), and the results show 56 ± 4% (mean ± SD, N = 5 retinae) of the transcript belonging to G90D in Rho G90D/WT retinae, a value close to 50% transcript derived from one allele.
- Full pipeline: quantification [Fiji, ImageJ]

### Monocyte to macrophage differentiation and changes in cellular redox homeostasis promote cell type-specific HIV latency reactivation. (PNAS 2024)

- DOI: 10.1073/pnas.2313823121 | PMCID: PMC11087762 | PMID: 38683980
- Evidence: Fiji/ImageJ was used to define regions of interest (ROIs) based on phase contrast outlines of cells for quantification of cell number, morphology, and GFP intensity.
- Full pipeline: quantification [Fiji, ImageJ]

### Structural and functional reorganization of inhibitory synapses by activity-dependent cleavage of neuroligin-2. (PNAS 2024)

- DOI: 10.1073/pnas.2314541121 | PMCID: PMC11067042 | PMID: 38657049
- Evidence: The data analysis software used for all data processing was Fiji ImageJ, MATLAB2018b, Clampfit 10.7, and IgoPro software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Elimination of virus-like particles reduces protein aggregation and extends replicative lifespan in <i>Saccharomyces cerevisiae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313538121 | PMCID: PMC10998562 | PMID: 38527193
- Evidence: Images were acquired with Z-stacks except where indicated and manually quantified with the help of the CellCounter Plugin in Fiji (ImageJ).
- Full pipeline: alignment/mapping [IMOD] -> quantification [Fiji, ImageJ] -> structure determination [IMOD] -> visualisation [IMOD]

### The early macrophage response to pathogens requires dynamic regulation of the nuclear paraspeckle. (PNAS 2024)

- DOI: 10.1073/pnas.2312587121 | PMCID: PMC10907238 | PMID: 38381785
- Evidence: RNA and protein colocalization was measured using Coloc 2 plugin in Fiji (ImageJ) software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### The spindle protein CKAP2 regulates microtubule dynamics and ensures faithful chromosome segregation. (PNAS 2024)

- DOI: 10.1073/pnas.2318782121 | PMCID: PMC10907244 | PMID: 38381793
- Evidence: All images were processed and analyzed using Fiji (ImageJ).
- Full pipeline: stage not stated [Fiji, ImageJ, PHENIX]

### Design of universal Ebola virus vaccine candidates via immunofocusing. (PNAS 2024)

- DOI: 10.1073/pnas.2316960121 | PMCID: PMC10873634 | PMID: 38319964
- Version used: **2.3.0**
- Evidence: Imaging was acquired on a chemiluminescence imager (GE Amersham Imager 600) and analyzed with Fiji (ImageJ v2.3.0).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CellProfiler, Fiji v2.3.0, ImageJ v2.3.0, PyMOL]

### De novo design of modular protein hydrogels with programmable intra- and extracellular viscoelasticity. (PNAS 2024)

- DOI: 10.1073/pnas.2309457121 | PMCID: PMC10861882 | PMID: 38289949
- Evidence: FRAP analysis began by using the Fast4DReg plugin in Fiji (ImageJ) ( https://github.com/guijacquemet/Fast4DReg ) to correct for drift in the collected images.
- Full pipeline: stage not stated [CellProfiler v4.0, Fiji, ImageJ]

### SAGA1 and SAGA2 promote starch formation around proto-pyrenoids in Arabidopsis chloroplasts. (PNAS 2024)

- DOI: 10.1073/pnas.2311013121 | PMCID: PMC10823261 | PMID: 38241434
- Evidence: Starch area analysis was carried out by measurement of TEM images using Fiji (ImageJ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Local and dynamic regulation of neuronal glycolysis in vivo. (PNAS 2024)

- DOI: 10.1073/pnas.2314699121 | PMCID: PMC10801914 | PMID: 38198527
- Evidence: All images were processed using Fiji/ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Spartin-mediated lipid transfer facilitates lipid droplet turnover. (PNAS 2024)

- DOI: 10.1073/pnas.2314093121 | PMCID: PMC10801920 | PMID: 38190532
- Evidence: Images were acquired using Nikon Elements and analyzed in Fiji (ImageJ).
- Full pipeline: stage not stated [AlphaFold, Fiji, ImageJ]

### Galectin-9 binding to HLA-DR in dendritic cells controls immune synapse formation and T cell proliferation. (PNAS 2025)

- DOI: 10.1073/pnas.2501381122 | PMCID: PMC12718305 | PMID: 41359845
- Evidence: Imaging was performed using both Leica DMI6000 and Zeiss LSM900 microscopes, and fluorescence analysis was conducted in Fiji ImageJ using custom macros and statistical tools like Mander’s and Pearson’s coefficients.
- Full pipeline: alignment/mapping [STAR] -> normalisation [DESeq2, R] -> differential/statistical testing [Fiji, ImageJ] -> stage not stated [GSEA, fgsea]

### Nonionic signaling rapidly remodels postsynaptic DLG to induce retrograde homeostatic plasticity. (PNAS 2025)

- DOI: 10.1073/pnas.2502997122 | PMCID: PMC12684909 | PMID: 41296724
- Evidence: For analysis, manual ROIs were drawn over individual boutons in Fiji (ImageJ) to measure fluorescence intensity and calculate ΔF/F 0 , where baseline fluorescence (F 0 ) was recorded before stimulation.
- Full pipeline: quantification [ImageJ] -> stage not stated [Fiji]

### Erythroid precursors regulate local oxygen tension and repair outcomes in the bone marrow niche. (PNAS 2025)

- DOI: 10.1073/pnas.2522548122 | PMCID: PMC12646327 | PMID: 41218120
- Evidence: Images were taken with an AxioScan and image quantification was performed using the Fiji/ImageJ software.
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA v4.3.3, Seurat v4.0]

### A cytoplasmic motif in HLA-E that drives clathrin-mediated endocytosis and VCP-associated postendocytic trafficking. (PNAS 2025)

- DOI: 10.1073/pnas.2514956122 | PMCID: PMC12582296 | PMID: 41134633
- Evidence: Image analysis, including colocalization quantification, was performed in Fiji/ImageJ using the Coloc2 plug-in.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [STRING db] -> stage not stated [Cytoscape v3.10.1, PHENIX]

### Invasin-functionalized PIC hydrogels enable long-term 3D culture of epithelial organoids. (PNAS 2025)

- DOI: 10.1073/pnas.2507500122 | PMCID: PMC12557532 | PMID: 41091766
- Evidence: Organoids were segmented and tracked over time using Fiji (ImageJ) software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Ectopic transcription due to inherited histone methylation may interfere with the ongoing function of differentiated neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2513137122 | PMCID: PMC12501177 | PMID: 40991443
- Evidence: The resulting images were adjusted for brightness/contrast and channels were merged into a composite using Fiji/ImageJ ( 59 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ]

### Spatiotemporal distribution of the glycoprotein pherophorin II reveals stochastic geometry of the growing ECM of &lt;i&gt;Volvox carteri&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2425759122 | PMCID: PMC12377771 | PMID: 40794838
- Version used: **1.51w**
- Evidence: Image processing and analysis used Fiji (ImageJ 1.51w) ( 77 ).
- Full pipeline: stage not stated [Fiji v1.51w, ImageJ v1.51w]

### A genetically defined pontine nucleus essential for ingestion in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2411174122 | PMCID: PMC12305073 | PMID: 40663610
- Evidence: For three sections per animal, across three animals, Fiji/ImageJ was used to draw regions of interest around subdivisions of Mo5 (Mo5 proper and Acc5), Mo7 (medial, middle, and lateral), and Mo12 (dorsal and ventral) using ChAT expression as cytoarchitectonic guide.
- Full pipeline: differential/statistical testing [NumPy] -> machine learning [DeepLabCut v2.3.8] -> stage not stated [Fiji, ImageJ, Python, SciPy]

### Monensin suppresses EMT-driven cancer cell motility by inducing Golgi pH-dependent exocytosis of GOLIM4. (PNAS 2025)

- DOI: 10.1073/pnas.2501347122 | PMCID: PMC12280883 | PMID: 40632561
- Version used: **1.51**
- Evidence: Image analysis was performed using Fiji (ImageJ version 1.51 s, NIH), Huygens Professional, or NIS-Elements.
- Full pipeline: stage not stated [Fiji v1.51, ImageJ v1.51]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Evidence: Confocal Z-Stacks were analyzed and processed in Fiji (ImageJ, NIH, Bethesda) and/or Imaris (BitPlane, Belfast, UK).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Behavioral resilience via dynamic circuit firing homeostasis. (PNAS 2025)

- DOI: 10.1073/pnas.2421386122 | PMCID: PMC12067288 | PMID: 40299703
- Evidence: To display synaptic sites at terminal boutons, images were imported into Fiji ImageJ (NIH), and the maximum intensity frame for the Brp channel was selected.
- Full pipeline: stage not stated [Fiji, ImageJ, Python]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Evidence: The area and number of lesions were quantified using the image processing software Fiji ImageJ ( 29 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### Structural basis for immune cell binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; via the trimeric autotransporter adhesin CbpF. (PNAS 2025)

- DOI: 10.1073/pnas.2418155122 | PMCID: PMC12012533 | PMID: 40198705
- Evidence: Image analysis was performed using Fiji/ImageJ ( 49 ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot v0.9.8.7, PHENIX] -> visualisation [R] -> stage not stated [AlphaFold, Fiji, ImageJ, UCSF Chimera]

### Reconfigurable homochiral colloidal clusters assembled under orthogonally applied electric and magnetic fields. (PNAS 2025)

- DOI: 10.1073/pnas.2418006122 | PMCID: PMC12002283 | PMID: 40168128
- Evidence: Images were analyzed using Fiji ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Intravital imaging of translocated bacteria via fluorogenic labeling of gut microbiota in situ. (PNAS 2025)

- DOI: 10.1073/pnas.2415845122 | PMCID: PMC12002288 | PMID: 40153461
- Version used: **2.14.0**
- Evidence: Data were further processed using Fiji ImageJ (2.14.0).
- Full pipeline: stage not stated [Fiji v2.14.0, ImageJ v2.14.0]

### The PVD neuron has male-specific structure and mating function in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421376122 | PMCID: PMC12002248 | PMID: 40138342
- Evidence: Analysis of male tail rays for neuron presence was manually evaluated using Fiji (ImageJ, NIH) by merging DIC and fluorescent channels and following the fluorescent signal through the Z-series in three dimensions.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Xylem embolism refilling revealed in stems of a weedy grass. (PNAS 2025)

- DOI: 10.1073/pnas.2420618122 | PMCID: PMC12002171 | PMID: 40112095
- Evidence: Images were captured every 5 min, and the resulting stack of images was analyzed in Fiji/ImageJ ( 50 ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### Dynamic investigation of hypoxia-induced L-lactylation. (PNAS 2025)

- DOI: 10.1073/pnas.2404899122 | PMCID: PMC11912421 | PMID: 40030031
- Evidence: All image analysis was performed using Fiji ImageJ.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Fiji, ImageJ, MACS2]

### Laser ablation microscopy reveals apical notch, apical dominance, and meristem regeneration dynamics in &lt;i&gt;Marchantia polymorpha&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2600460123 | PMCID: PMC13320805 | PMID: 42330275
- Evidence: Images were processed using LasX, ZEN Blue, and Fiji/ImageJ software packages.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Fiji, ImageJ]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: Western blots were quantified in Fiji (ImageJ).
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### ERK builds a population of short-lived nascent adhesions that produce persistent edge protrusion and cell migration. (PNAS 2026)

- DOI: 10.1073/pnas.2525452123 | PMCID: PMC13271172 | PMID: 42296347
- Evidence: Blots were imaged using an Odyssey CLx imaging system (LI-COR) and quantified in Fiji/ImageJ.
- Full pipeline: quantification [Fiji, ImageJ] -> stage not stated [Cellpose]

### Heterotypic intercellular adhesion tunes efficiency of cell-on-cell migration. (PNAS 2026)

- DOI: 10.1073/pnas.2524496123 | PMCID: PMC13273321 | PMID: 42284330
- Evidence: Live cell tracking was performed using the built-in Mastodon plugin in Fiji/ImageJ ( 72 ).
- Full pipeline: stage not stated [Fiji, ImageJ]

### A fungal natural product that inhibits plant cellulose biosynthesis by disrupting cellulose synthase complexes. (PNAS 2026)

- DOI: 10.1073/pnas.2602575123 | PMCID: PMC13273347 | PMID: 42263129
- Evidence: Image analysis was performed using Fiji/ImageJ software.
- Full pipeline: stage not stated [Fiji, ImageJ]

### Germline-targeted baboon apolipoprotein L-1 protects mice against African trypanosomes. (PNAS 2026)

- DOI: 10.1073/pnas.2525773123 | PMCID: PMC13037889 | PMID: 41894328
- Evidence: The band intensities compared to a serially diluted sample of rAPOL1 via pixel counts using Fiji/ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ]

### The audience shapes the information content of the honey bee waggle dance. (PNAS 2026)

- DOI: 10.1073/pnas.2518687123 | PMCID: PMC13056074 | PMID: 41871274
- Version used: **1.50i**
- Evidence: We used Tracker (v4.91) or Fiji ImageJ (v1.50i) software (see also control analysis 1, below), and the researchers making the measurements were blind to the treatment phase and the colony origin of the observed bee.
- Full pipeline: stage not stated [Fiji v1.50i, ImageJ v1.50i]

### GSK-3β coordinates axonal microtubule organization through Shot and Tau. (PNAS 2026)

- DOI: 10.1073/pnas.2516746123 | PMCID: PMC12933142 | PMID: 41701831
- Evidence: Analysis was automated using Fiji/ImageJ macros: axondisorg_table or axon-disorganization-from-rois ( https://github.com/avmann ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold, ColabFold] -> visualisation [ChimeraX] -> stage not stated [Fiji, ImageJ]

### Acquired motility of &lt;i&gt;Babesia microti&lt;/i&gt;-infected red blood cells. (PNAS 2026)

- DOI: 10.1073/pnas.2509776123 | PMCID: PMC12912998 | PMID: 41628349
- Evidence: Image analyses were completed in Fiji ImageJ as follows i) Cell count was performed using “Plugins–Analyze–Cell Counter.” ii) Signal (e.g., grayscale, fluorescence) intensity and morphology (including size and shape) analyses were performed using “Analyze–Measure.” “Set Measurements” for intensity analysis included “Mean gray value, SD, and Min & max gray value”.
- Full pipeline: stage not stated [Fiji, ImageJ]

### The membrane skeleton is constitutively remodeled in neurons by calcium signaling. (Science 2025)

- DOI: 10.1126/science.adn6712 | PMCID: PMC12333566 | PMID: 40773558
- Evidence: We visually identified and marked regions of the axon in which the MPS undergoes at least one degradation and reformation cycle during the first 15 frames of imaging at 15-sec time resolution, corresponding to 225-sec total imaging time, using Fiji/ImageJ.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Fiji, ImageJ]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: Gels were analysed in Fiji (ImageJ) and relative protection was calculated in Excel (Microsoft), plotted and analysed in Prism (GraphPad).
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Myelin sheaths in the central nervous system can withstand damage and dynamically remodel. (Science 2026)

- DOI: 10.1126/science.adr4661 | PMCID: PMC7618902 | PMID: 41678629
- Evidence: Human post-mortem brain tissue quantification Analysis was done using QuPath version 0.4.4 and Fiji ImageJ 64-bit version 2.14.0/1.54f software.
- Full pipeline: quantification [Fiji, QuPath v0.4.4] -> stage not stated [ImageJ v1.54p]

### Blocking RAN translation without altering repeat RNAs rescues &lt;i&gt;C9ORF72&lt;/i&gt;-related ALS and FTD phenotypes. (Science 2026)

- DOI: 10.1126/science.adv2600 | PMCID: PMC13107528 | PMID: 41643021
- Evidence: Automatic quantifications were performed using a custom Fiji/ImageJ-based plugin (National Institutes of Health, version 1.53c) ( 43 ). hNIL motor neurons survival assay Because the PiggyBac hNIL plasmid includes a nuclear BFP2, successfully nucleofected cells displayed blue, fluorescent nuclei, allowing us to count them over time. hNIL motor neurons at day 3 of differentiation were seeded in a po...
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> quantification [CellProfiler, Fiji, ImageJ] -> differential/statistical testing [DESeq2, R v4.2.1]

