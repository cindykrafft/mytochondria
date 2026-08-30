# CellProfiler

- **Category:** imaging
- **Papers in survey:** 124
- **Journals:** PNAS (71), Nature (35), Cell (11), Science (7)
- **Years:** 2021 (17), 2022 (15), 2023 (18), 2024 (31), 2025 (25), 2026 (18)
- **Versions named:** 4.2.1 (8), 4.2.5 (3), 4.2.7 (2), 3.1.9 (2), 4.0.7 (2), 4.2.4 (2), 3.1.8 (2), 4.2.6 (1), 4.1.3 (1), 3.0 (1)
- **Pipeline stages it appears in:** quantification (34), visualisation (3), normalisation (2), variant calling (1), dimensionality reduction/clustering (1), differential/statistical testing (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **3.1.8**
- Evidence: Cell segmentation and single-cell feature extraction Segmentation was performed in a two-step process, a signal-classification step using Ilastik 1.3.2 ( Berg et al., 2019 ) followed by an object-recognition step using CellProfiler 3.1.8 ( Carpenter et al., 2006 ), as described elsewhere ( Schapiro et al., 2017 ).
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Microglia jointly degrade fibrillar alpha-synuclein cargo by distribution through tunneling nanotubes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.007 | PMCID: PMC8527836 | PMID: 34555357
- Evidence: Henneberger N/A Software and Algorithms CellProfiler Broad Institute of Harvard and MIT v3.1.8 FACSDIVA™ software Becton Dickinson N/A Fiji ImageJ Wayne Rusband v2.0.0-rc-69/1.52n FlowJo FlowJo, LLC v3.05470 ggplot2 CRAN v3.2.1 Graph Pad Prism GraphPad Software Inc. v7.0e and v8.0 Image Studio, v5.2 LI-COR Biosciences N/A Imaris Bitplane by Oxford Instruments plc v9.2.1 NIS-elements Nikon AR 4.20....
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> dimensionality reduction/clustering [Cytoscape] -> stage not stated [CellProfiler, Fiji, ImageJ, ggplot2, tidyverse]

### Kinase-mediated RAS signaling via membraneless cytoplasmic protein granules. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.031 | PMCID: PMC8127962 | PMID: 33848463
- Evidence: ...ps://www.graphpad.com ImageJ Schneider et al., 2012 https://imagej.nih.gov/ij Micro-Manager software Edelstein et al., 2010 https://micro-manager.org CellProfiler software CellProfiler https://cellprofiler.org MATLAB software Mathworks https://www.mathworks.com/products/matlab.html Resource availability Lead contact Further information and requests for resources should be directed to and will be f...
- Full pipeline: visualisation [ChimeraX] -> stage not stated [CellProfiler, ImageJ]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: For quantitation of all PLAs, the number of PLA puncta was counted across maximum intensity projections of raw files of each stack using CellProfiler ( McQuin et al., 2018 ) and then normalized to the number of DAPI-positive nuclei in that field of view.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### Compromised SARS-CoV-2-specific placental antibody transfer. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.027 | PMCID: PMC7755577 | PMID: 33476549
- Evidence: ...d Prism GraphPad https://www.graphpad.com/scientific-software/prism/ Intellicyt ForeCyt Software Sartorious https://intellicyt.com/products/software/ CellProfiler software Broad Institute https://cellprofiler.org/ R programming language Version 3.6.1 https://www.r-project.org/ GlycanAssure software ThermoFisher Scientific https://www.thermofisher.com/us/en/home/life-science/bioproduction/contamina...
- Full pipeline: differential/statistical testing [Cytoscape v3.8.0] -> stage not stated [Bioconductor, CellProfiler, R v4.0.0]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Version used: **2.2.0**
- Evidence: ...1 Schneider et al., 2012 https://doi.org/10.1038/nmeth.2089 ImageJ (Fiji), version 1.53f51 Schindelin et al., 2012 https://doi.org/10.1038/nmeth.2019 CellProfiler, version 2.2.0 CellProfiler, USA https://cellprofiler.org RStudio, version 1.4.1106 RStudio, USA https://www.rstudio.com/ DEP-LFQ package for R, BiocManager 1.30.16 CRAN repositories https://bioconductor.org/packages/devel/bioc/vignettes...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: Image segmentation was performed using a CellProfiler 152 pipeline with the following steps: 1) IdentifyPrimaryObjects, 2) MeasureObjectSizeShape, 3) MeasureObjectIntensity, 4) ConvertObjectsToImage, 5) TrackObjects, 6) SaveImages, 7) ExportToSpreadsheet.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 91 https://bioconductor.org/packages/release/bioc/html/scran.html ggscatter Alboukadel Kassambara https://doi.org/10.32614/CRAN.package.ggpubr Zen Black software v2.3 Zeiss https://www.zeiss.com/microscopy/en/products/software/zeiss-zen.html Zen Blue software v2.3 Zeiss https://www.zeiss.com/microscopy/en/products/software/zeiss-zen.html CellProfiler software v4.2.1 Carpenter et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Version used: **4.2.5**
- Evidence: 130 RRID: SCR_002285 CellProfiler v4.2.5 Stirling et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Molecular and neural control of social hierarchy by a forebrain-thalamocortical circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.024 | PMCID: PMC12458795 | PMID: 40795854
- Evidence: A CellProfiler pipeline 79 was created to measure RNA signal of candidate genes within Necab1 + and Necab1 − cells.
- Full pipeline: normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, GSEA, R, Seurat v2.3.4]

### Brain endothelial gap junction coupling enables rapid vasodilation propagation during neurovascular coupling. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.030 | PMCID: PMC12337775 | PMID: 40675149
- Version used: **4.2.4**
- Evidence: For optogenetic experiments, an image of mScarlet signal – acquired and transformed alongside the SMA + arterial network – was binarized using CellProfiler 4.2.4 (ref.
- Full pipeline: quantification [ImageJ, Python] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.2.4]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Evidence: CellProfiler (Broad Institute, v3.1.9) was used to quantitate the number of puncta per cell and the size (area) of each individual punctum from image projections.
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: Image processing and quality filtering Cell detection and single-cell image analysis was performed using CellProfiler (v.2) 77 .
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### Spatial predictors of immunotherapy response in triple-negative breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06498-3 | PMCID: PMC10533410 | PMID: 37674077
- Evidence: Whole-cell image masks were used for downstream measurements (single-cell proteomic profiles and size) using CellProfiler 44 .
- Full pipeline: alignment/mapping [STAR v2.5.2] -> quantification [Bioconductor] -> differential/statistical testing [R] -> machine learning [ilastik] -> stage not stated [CellProfiler]

### Phase separation of FSP1 promotes ferroptosis. (Nature 2023)

- DOI: 10.1038/s41586-023-06255-6 | PMCID: PMC10338336 | PMID: 37380771
- Version used: **4.1.3**
- Evidence: The imaging software ImageJ/Fiji was used for visualization, and CellProfiler (v.4.1.3, Broad Institute) was used to count the condensates in each cell.
- Full pipeline: visualisation [CellProfiler v4.1.3] -> stage not stated [AlphaFold, ColabFold, Fiji, ImageJ]

### RHOJ controls EMT-associated resistance to chemotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05838-7 | PMCID: PMC10076223 | PMID: 36949199
- Version used: **3.1.9**
- Evidence: EdU intensity was assessed in at least 250 EdU-positive nuclei per condition per experiment using CellProfiler (v.3.1.9).
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [limma] -> normalisation [HTSeq] -> differential/statistical testing [limma] -> stage not stated [CellProfiler v3.1.9, ImageJ]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Version used: **4.2.1**
- Evidence: Then, 48 h after transfection, nuclei were stained with Hoechst (1 μg ml −1 ), images were taken using the Revolve fluorescence microscope and analysed with CellProfiler v.4.2.1 using a customized pipeline.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: Cell segmentation masks were created for all cells in ilastik and CellProfiler 62 (v.2.2.0).
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Multiple pathways for SARS-CoV-2 resistance to nirmatrelvir. (Nature 2023)

- DOI: 10.1038/s41586-022-05514-2 | PMCID: PMC9849135 | PMID: 36351451
- Version used: **4.0.7**
- Evidence: Cells were then imaged for DAPI and green fluorescent protein using IN Cell 2000 (GE) and analysed with CellProfiler v.4.0.7 (ref.
- Full pipeline: dimensionality reduction/clustering [SciPy, seaborn] -> stage not stated [CellProfiler v4.0.7, Nextflow, Pangolin v4.0.6]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Version used: **4.2.1**
- Evidence: Image analysis and quantification were performed using the open-source software CellProfiler (v.4.2.1).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Version used: **4.2.5**
- Evidence: Cell videos were analysed using CellProfiler v.4.2.5.
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Evidence: Cells labelled by tdTomato, GFP or both tdTomato and GFP, or DAPI only, were counted using the cell counter in ImageJ or CellProfiler.
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **4.2.1**
- Evidence: Automated image analysis Immunofluorescence images were quantified using CellProfiler (v.4.2.1) automated image-processing software 62 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Version used: **4.2.6**
- Evidence: Quantification of the immunofluorescence signal was performed using CellProfiler (v.4.2.6) 61 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### The CRL5-SPSB3 ubiquitin ligase targets nuclear cGAS for degradation. (Nature 2024)

- DOI: 10.1038/s41586-024-07112-w | PMCID: PMC10972748 | PMID: 38418882
- Evidence: Analysis of nuclear cGAS–GFP levels was performed using the CellProfiler software.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ChimeraX]

### Modelling post-implantation human development to yolk sac blood emergence. (Nature 2024)

- DOI: 10.1038/s41586-023-06914-8 | PMCID: PMC10849971 | PMID: 38092041
- Evidence: The resulting images were evaluated by using a custom pipeline in CellProfiler 65 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Enrichr, Fiji, ImageJ, Seurat]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: For PU.1 immunofluorescence quantification by CellProfiler (Figs.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **4.2.1**
- Evidence: Cell segmentation masks were generated from the normalized images using CellProfiler (v4.2.1).
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### LRP8 is a receptor for tick-borne encephalitis virus. (Nature 2025)

- DOI: 10.1038/s41586-025-09500-2 | PMCID: PMC13221092 | PMID: 40993380
- Evidence: Images were processed in Photoshop (Adobe Systems) and analyzed using a custom analysis pipeline in CellProfiler 52 .
- Full pipeline: stage not stated [CellProfiler, ImageJ]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Evidence: Segmentation of nuclear speckles was performed using CellProfiler using the Otsu thresholding algorithm, and nucleoplasms were considered all non-speckle regions of the nucleus.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: Quantification via CellProfiler of KI67 positivity per organoid per genotype (bottom).
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Image analysis Images were analysed using CellProfiler 70 , TrackMate 71 and MATLAB v.R2021b and R2023b (MathWorks).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Evidence: Quantitative image analysis All quantitative imaging measurements were performed using CellProfiler 73 v.4.2.6.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### PLA2G15 is a BMP hydrolase and its targeting ameliorates lysosomal disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08942-y | PMCID: PMC12158761 | PMID: 40335701
- Version used: **4.2.7**
- Evidence: The images were analysed using ImageJ v.2.1.0 and CellProfiler v.4.2.7.
- Full pipeline: stage not stated [AlphaFold, CellProfiler v4.2.7, ChimeraX, ImageJ v2.1.0, QuPath]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Version used: **4.2.1**
- Evidence: The acquired images were processed and analysed using FIJI (v.2.14.0) 70 , ilastik (v.1.3.3post3) 71 and CellProfiler (v.4.2.1) 72 as described previously 69 .
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **4.2.5**
- Evidence: PROX1 expression was quantified using the CellProfiler (v.4.2.5) software 85 .
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### HIV-1 signalling remodels nuclear pores to licence infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10453-3 | PMCID: PMC13293875 | PMID: 42092137
- Evidence: Cell profiler pipelines are available online ( https://github.com/MattVXWhelan/Mesner_Whelan_et_al/blob/main/CellProfiler_Analysis ).
- Full pipeline: differential/statistical testing [limma] -> stage not stated [CellProfiler, Fiji, ImageJ]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: DAPI and 53BP1 channel images were then loaded into a custom CellProfiler pipeline to quantify the number of 53BP1 foci per cell.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: Images were collected on an EVOS FL upright microscope and analysed for fluorescence using a custom CellProfiler pipeline (v.4.2.8; available at GitHub: https://github.com/RowitchLab/Code_for_Cux2_Atf4_paper ).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Synthetic circuits for cell ratio control. (Nature 2026)

- DOI: 10.1038/s41586-026-10259-3 | PMCID: PMC13171440 | PMID: 41851453
- Version used: **4.2.1**
- Evidence: Enhanced images were then segmented in CellProfiler (v.4.2.1) by splitting RGB channels and identifying primary objects with diameters of 10–160 pixels using adaptive Otsu thresholding in three-class mode.
- Full pipeline: quantification [ImageJ v1.54g] -> simulation/modelling [Python v3.8.5] -> stage not stated [CellProfiler v4.2.1]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: To assess AAV infection, stitched images of four fields were acquired with a Plan Apo 10× DIC L objective, and the percentage of Ribo-STAMP over NeuN-positive neurons was assessed with CellProfiler.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: Cellular segmentation was performed with CellProfiler using the Cellpose 2.0 TissueNet segmentation model.
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Fibroblastic reticular cells direct the initiation of T cell responses via CD44. (Nature 2026)

- DOI: 10.1038/s41586-025-09988-8 | PMCID: PMC12999478 | PMID: 41565815
- Evidence: Data analysis was performed using Image Data Exploration and Analysis Software (IDEAS) and rank-weighted co-localization was analysed using the co-localization pipeline in CellProfiler. vCD44BP impact on adjuvant-induced LN expansion, immunization and influenza infection Montanide adjuvant (Seppic) (25% diluted in PBS) was administered by subcutaneous injection in the neck scruff of mice.
- Full pipeline: normalisation [CCP4] -> structure determination [Coot] -> stage not stated [CellProfiler, ImageJ, PHENIX, PyMOL]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: To quantify the PNN around parvalbumin-expressing (PV) cells, a custom ROI detection pipeline was developed in CellProfiler.
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Version used: **4.2.7**
- Evidence: Analysis of IF–DNA-FISH of knockout mitotic cells We first created a CellProfiler (v.4.2.7) 84 analysis pipeline to quantify protein expression levels after targeted knockdown.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### Secretome translation shaped by lysosomes and lunapark-marked ER junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-09718-0 | PMCID: PMC12727531 | PMID: 41193816
- Evidence: The labelled cells were mounted using VECTASHIELD antifade with DAPI (Vectorlabs), imaged using Zeiss 980 AiryScan, and quantified using CellProfiler.
- Full pipeline: read trimming [Cutadapt v2.10, STAR v2.7.5c] -> alignment/mapping [Cutadapt v2.10, STAR v2.7.5c] -> quantification [CellProfiler] -> stage not stated [DESeq2, ImageJ, TrackMate]

### Morphological cell profiling of SARS-CoV-2 infection identifies drug repurposing candidates for COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2105815118 | PMCID: PMC8433531 | PMID: 34413211
- Evidence: The open source CellProfiler software ( 10 ) was used in an Ubuntu Linux-based distributed Amazon AWS cloud implementation for segmentation, feature extraction, and infection scoring, and results were written to an Amazon RDS relational database using MySQL.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ] -> stage not stated [CellProfiler, scikit-learn]

### Natural variation identifies SNI1, the SMC5/6 component, as a modifier of meiotic crossover in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2021970118 | PMCID: PMC8379953 | PMID: 34385313
- Evidence: The CellProfiler program was used to identify seed boundaries in micrographs and to assign a dsRed and eGFP fluorescence intensity value to each seed object ( 37 , 82 ).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [CellProfiler]

### Restriction of SARS-CoV-2 replication by targeting programmed -1 ribosomal frameshifting. (PNAS 2021)

- DOI: 10.1073/pnas.2023051118 | PMCID: PMC8256030 | PMID: 34185680
- Evidence: Cell nuclei, mCherry, and GFP signals are imaged using an automated fluorescent microscope (InCell 2200; GE) with a 20× objective, and the acquired images are quantified using the CellProfiler image analysis package.
- Full pipeline: quantification [CellProfiler]

### ALS- and FTD-associated missense mutations in TBK1 differentially disrupt mitophagy. (PNAS 2021)

- DOI: 10.1073/pnas.2025053118 | PMCID: PMC8214690 | PMID: 34099552
- Evidence: Confocal microscopy was performed on an UltraView Vox spinning disk confocal system and images were deconvolved with Huygens Professional Software, then analyzed with ImageJ/FIJI, Ilastik, and CellProfiler software ( 56 – 58 ).
- Full pipeline: stage not stated [CellProfiler, ImageJ, ilastik]

### Single-cell sequencing reveals suppressive transcriptional programs regulated by MIS/AMH in neonatal ovaries. (PNAS 2021)

- DOI: 10.1073/pnas.2100920118 | PMCID: PMC8157966 | PMID: 33980714
- Evidence: CellProfiler Software was used for automated cell counts.
- Full pipeline: read trimming [R, Seurat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [CellPhoneDB, CellProfiler]

### ORF10-Cullin-2-ZYG11B complex is not required for SARS-CoV-2 infection. (PNAS 2021)

- DOI: 10.1073/pnas.2023157118 | PMCID: PMC8092598 | PMID: 33827988
- Evidence: Samples were imaged on a Cytation 1 Cell Imaging Multi-Mode Reader (BioTek) and were evaluated using CellProfiler ( 34 ).
- Full pipeline: stage not stated [CellProfiler, R v4.0.2]

### Pathogenic LRRK2 regulates ciliation probability upstream of tau tubulin kinase 2 via Rab10 and RILPL1 proteins. (PNAS 2021)

- DOI: 10.1073/pnas.2005894118 | PMCID: PMC7958464 | PMID: 33653948
- Evidence: Cilium length was measured using CellProfiler ( 24 ).
- Full pipeline: stage not stated [CellProfiler]

### Visualizing active viral infection reveals diverse cell fates in synchronized algal bloom demise. (PNAS 2021)

- DOI: 10.1073/pnas.2021586118 | PMCID: PMC7980383 | PMID: 33707211
- Evidence: To estimate the fraction of infected cells, we used CellProfiler ( 59 ) using the PercentPositive pipeline separately for each probe after a maximum projection and background subtraction for each channel separately ( SI Appendix , Fig.
- Full pipeline: stage not stated [CellProfiler]

### GRK5 is a regulator of fibroblast activation and cardiac fibrosis. (PNAS 2021)

- DOI: 10.1073/pnas.2012854118 | PMCID: PMC7865138 | PMID: 33500351
- Evidence: Images were quantified using CellProfiler, a cell image analysis software, capable of determining fibrotic area in an unbiased manner ( 24 ).
- Full pipeline: quantification [CellProfiler] -> normalisation [ImageJ]

### CD20 as a gatekeeper of the resting state of human B cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021342118 | PMCID: PMC7896350 | PMID: 33563755
- Version used: **3.0.0**
- Evidence: All microscope images were acquired using Leica DMi8 microscope equipped with a 63× oil immersion objective lens and analyzed with CellProfiler 3.0.0 and Prism software (GraphPad).
- Full pipeline: normalisation [fgsea] -> differential/statistical testing [R, limma] -> stage not stated [CellProfiler v3.0.0, GSEA]

### <i>Drosophila</i> Sex Peptide controls the assembly of lipid microcarriers in seminal fluid. (PNAS 2021)

- DOI: 10.1073/pnas.2019622118 | PMCID: PMC7865141 | PMID: 33495334
- Evidence: Microcarrier image analysis was performed using the open‐access CellProfiler Software version 2.2.0.
- Full pipeline: differential/statistical testing [R] -> stage not stated [CellProfiler]

### Targeting transcriptional regulation of SARS-CoV-2 entry factors <i>ACE2</i> and <i>TMPRSS2</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2021450118 | PMCID: PMC7817128 | PMID: 33310900
- Evidence: Images were analyzed using CellProfiler to quantify the percentage of infected cells at the well level ( 43 ).
- Full pipeline: quantification [CellProfiler] -> normalisation [Seurat]

### Input integration by the circadian clock exhibits nonadditivity and fold-change detection. (PNAS 2022)

- DOI: 10.1073/pnas.2209933119 | PMCID: PMC9636907 | PMID: 36279450
- Version used: **3.1.9**
- Evidence: A CellProfiler (version 3.1.9, Broad Institute ( 67 )) pipeline was used for illumination correction, nuclei segmentation, tracking, and fluorescence quantifications.
- Full pipeline: quantification [CellProfiler v3.1.9]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: Image analysis was performed with CellProfiler-3 software ( http://www.cellprofiler.org ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### A ribavirin-induced ORF2 single-nucleotide variant produces defective hepatitis E virus particles with immune decoy function. (PNAS 2022)

- DOI: 10.1073/pnas.2202653119 | PMCID: PMC9407633 | PMID: 35969792
- Evidence: Images were taken using a Keyence microscope with 4× magnification and processed using CellProfiler.
- Full pipeline: stage not stated [CellProfiler]

### WNK1 collaborates with TGF-β in endothelial cell junction turnover and angiogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2203743119 | PMCID: PMC9335306 | PMID: 35867836
- Evidence: Subsequently, CellProfiler ( 77 ) was used to extract features (i.e., number of sprouted cells and cord lengths) from the masked images.
- Full pipeline: stage not stated [CellProfiler, ImageJ]

### A mechanism of self-lipid endocytosis mediated by the receptor Mincle. (PNAS 2022)

- DOI: 10.1073/pnas.2120489119 | PMCID: PMC9335232 | PMID: 35867828
- Version used: **3.1.8**
- Evidence: Quantification of fluorescent GM3 uptake by endothelial cells was performed using CellProfiler 3.1.8 ( 41 ).
- Full pipeline: quantification [CellProfiler v3.1.8] -> stage not stated [MACS2]

### SRS-FISH: A high-throughput platform linking microbiome metabolism to identity at the single-cell level. (PNAS 2022)

- DOI: 10.1073/pnas.2203519119 | PMCID: PMC9245642 | PMID: 35727976
- Evidence: All imaging and statistical analyses were performed with CellProfiler and MATLAB (The MathWorks).
- Full pipeline: differential/statistical testing [CellProfiler]

### Mast cell infiltration of the choroid and protease release are early events in age-related macular degeneration associated with genetic risk at both chromosomes 1q32 and 10q26. (PNAS 2022)

- DOI: 10.1073/pnas.2118510119 | PMCID: PMC9171765 | PMID: 35561216
- Evidence: An analysis pipeline was developed for the quantification of mast cells using CellProfiler software 3.1.9 ( https://cellprofiler.org/ ) to automate the quantitation of the number of MC T - or MC TC -stained cells in submacular sections.
- Full pipeline: quantification [CellProfiler] -> normalisation [R] -> differential/statistical testing [R, afex] -> stage not stated [Fiji, ImageJ]

### A role for endoplasmic reticulum dynamics in the cellular distribution of microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2104309119 | PMCID: PMC9169640 | PMID: 35377783
- Evidence: Image analysis was performed using CellProfiler (CP), with inbuilt CP modules, or custom MATLAB-based modules.
- Full pipeline: machine learning [ilastik] -> stage not stated [CellProfiler]

### Triglyceride breakdown from lipid droplets regulates the inflammatory response in macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2114739119 | PMCID: PMC8944848 | PMID: 35302892
- Evidence: Images were processed and analyzed for LDs with CellProfiler software ( 43 ).
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> visualisation [ggplot2] -> stage not stated [CellProfiler]

### Social reactivation of fear engrams enhances memory recall. (PNAS 2022)

- DOI: 10.1073/pnas.2114230119 | PMCID: PMC8944571 | PMID: 35286206
- Evidence: CellProfiler.
- Full pipeline: stage not stated [CellProfiler]

### In situ proximity labeling identifies Lewy pathology molecular interactions in the human brain. (PNAS 2022)

- DOI: 10.1073/pnas.2114405119 | PMCID: PMC8812572 | PMID: 35082147
- Version used: **3.1.5**
- Evidence: A custom CellProfiler (v.3.1.5) pipeline was then used to quantify pixels representing positive stain (90% confidence score).
- Full pipeline: quantification [CellProfiler v3.1.5, ilastik v1.3.2] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Cytoscape] -> machine learning [ilastik v1.3.2] -> visualisation [Cytoscape] -> stage not stated [R v4.0.3]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Version used: **4.07**
- Evidence: The simple segmentation images were analyzed for GFP area in CellProfiler 4.07 (cell image analysis software) ( 74 ) and exported into Microsoft Excel.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Integrin α&lt;sub&gt;5&lt;/sub&gt;β&lt;sub&gt;1&lt;/sub&gt; contributes to cell fusion and inflammation mediated by SARS-CoV-2 spike via RGD-independent interaction. (PNAS 2023)

- DOI: 10.1073/pnas.2311913120 | PMCID: PMC10723138 | PMID: 38060559
- Evidence: The mean or total EGFP area was measured using CellProfiler software.
- Full pipeline: stage not stated [CellProfiler]

### Gene expression in the primate orbitofrontal cortex related to anxious temperament. (PNAS 2023)

- DOI: 10.1073/pnas.2305775120 | PMCID: PMC10710052 | PMID: 38011550
- Version used: **4.2.1**
- Evidence: Images were preprocessed using ImageJ version 1.53s and CellProfiler version 4.2.1.
- Full pipeline: alignment/mapping [Python v2.7] -> stage not stated [CellProfiler v4.2.1, ImageJ v1.53s, QuPath, Scanpy, limma, scDblFinder]

### Localization of PPM1H phosphatase tunes Parkinson's disease-linked LRRK2 kinase-mediated Rab GTPase phosphorylation and ciliogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2315171120 | PMCID: PMC10622911 | PMID: 37889931
- Evidence: Images were converted to maximum intensity projections using Fiji ( https://fiji.sc/ ) and analyzed using CellProfiler software ( 22 , 23 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [CellProfiler, ChimeraX]

### Phase separation underlies signaling activation of oncogenic NTRK fusions. (PNAS 2023)

- DOI: 10.1073/pnas.2219589120 | PMCID: PMC10589674 | PMID: 37812694
- Evidence: For analysis of Pearson’s correlation coefficient, CellProfiler and Coloc2 of Fiji were used.
- Full pipeline: stage not stated [CellProfiler, PyMOL]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Evidence: Confocal stack images were acquired on the Nikon Eclipse Ti confocal microscope with a 40× oil objective and type A immersion oil and quantified using a custom CellProfiler ( 86 , 87 ) workflow.
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### Optogenetic clustering and membrane translocation of the BcLOV4 photoreceptor. (PNAS 2023)

- DOI: 10.1073/pnas.2221615120 | PMCID: PMC10410727 | PMID: 37527339
- Evidence: Segmentation images were imported to CellProfiler along with the corresponding images of BcLOV-mCherry variants.
- Full pipeline: stage not stated [CellProfiler, ImageJ, R v4.2.2, ggplot2, tidyverse]

### Geometry-mediated bridging drives nonadhesive stripe wound healing. (PNAS 2023)

- DOI: 10.1073/pnas.2221040120 | PMCID: PMC10161107 | PMID: 37098071
- Evidence: Nuclei area, cell area, and nuclei offset were obtained by CellProfiler.
- Full pipeline: alignment/mapping [ImageJ] -> simulation/modelling [ImageJ] -> stage not stated [CellProfiler, StarDist]

### State- and stimulus-specific dynamics of SMAD signaling determine fate decisions in individual cells. (PNAS 2023)

- DOI: 10.1073/pnas.2210891120 | PMCID: PMC10013741 | PMID: 36857347
- Evidence: Cells were tracked throughout the duration of the experiment using custom-written MATLAB (MathWorks) scripts based on code developed by the Alon lab ( 24 ) and the CellProfiler project ( 25 ) as previously described ( 15 ).
- Full pipeline: stage not stated [CellProfiler, SciPy]

### Rab3 mediates a pathway for endocytic sorting and plasma membrane recycling of ordered microdomains. (PNAS 2023)

- DOI: 10.1073/pnas.2207461120 | PMCID: PMC10013782 | PMID: 36848577
- Evidence: The images were then analyzed with CellProfiler ( 84 ) to determine the fluorescence of the probe in the whole cell and at the PM.
- Full pipeline: stage not stated [CellProfiler, ImageJ]

### Mammalian telomeric RNA (TERRA) can be translated to produce valine-arginine and glycine-leucine dipeptide repeat proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2221529120 | PMCID: PMC9992779 | PMID: 36812212
- Evidence: To analyze the data, we set the threshold to discriminate the positive signals from the negative signals using CellProfiler software ( 55 ).
- Full pipeline: stage not stated [CellProfiler, ImageJ]

### Robotic data acquisition with deep learning enables cell image-based prediction of transcriptomic phenotypes. (PNAS 2023)

- DOI: 10.1073/pnas.2210283120 | PMCID: PMC9910600 | PMID: 36577074
- Evidence: As a comparison, we also classified these cells into three clusters based on their morphological and dynamical features ( Datasets S7–S9 ), which were extracted from the cell images by three representative and well-used conventional image analysis software programs ( 17 ): NIS-Elements ( 18 ), CellProfiler 4 ( 17 ), and TrackMate 7 ( 19 ) in Fiji (ImageJ) ( 20 ) ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [CellProfiler, Fiji, ImageJ, TrackMate]

### Artificial dynamic structure ensemble-guided rational design of a universal RNA aptamer-based sensing tag. (PNAS 2024)

- DOI: 10.1073/pnas.2414793121 | PMCID: PMC11670126 | PMID: 39705306
- Version used: **4.2.4**
- Evidence: All cell segmentation, fluorescence measurements, and the number of foci per nucleus were determined with CellProfiler 4.2.4 ( 55 ).
- Full pipeline: stage not stated [CellProfiler v4.2.4, ImageJ, StarDist]

### Modeling extrahepatic hepatitis E virus infection in induced human primary neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2411434121 | PMCID: PMC11588080 | PMID: 39546567
- Evidence: A CellProfiler pipeline was employed to ascertain the presence and length of neurites via β-III-tubulin immunofluorescence staining and the HEV infection status of cells by immunofluorescence staining of the capsid protein.
- Full pipeline: differential/statistical testing [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> visualisation [ComplexHeatmap, Seurat, ggplot2, tidyverse] -> stage not stated [CellProfiler, ImageJ]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: MRG and dsRNA quantification was performed using an automated pipeline on CellProfiler software.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### Identification and characterization of the lipoprotein &lt;i&gt;N&lt;/i&gt;-acyltransferase in &lt;i&gt;Bacteroides&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2410909121 | PMCID: PMC11573676 | PMID: 39495918
- Evidence: Bacterial cells were segmented using Otsu two-class thresholding with CellProfiler using the CellMask Deep Red channel and intensity and size/shape features were tabulated for the Alexa Fluor 488 and CellMask Deep Red channels ( 76 ).
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CellProfiler, eggNOG]

### Facilitating and restraining virus infection using cell-attachable soluble viral receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2414583121 | PMCID: PMC11551432 | PMID: 39480852
- Evidence: The GFP-positive cell areas were calculated using CellProfiler software and presented as a percentage of ACE2 WT level.
- Full pipeline: stage not stated [AlphaFold, CellProfiler]

### Intrinsically disordered region amplifies membrane remodeling to augment selective ER-phagy. (PNAS 2024)

- DOI: 10.1073/pnas.2408071121 | PMCID: PMC11536123 | PMID: 39453744
- Evidence: Representative images were obtained from duplicate IF experiments and analyzed for ER-associated FAM134B-induced punctate structures using the CellProfiler ( 69 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, CellProfiler, MDAnalysis]

### Goblet cell differentiation subgroups in colorectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2414213121 | PMCID: PMC11513979 | PMID: 39401352
- Version used: **3.0**
- Evidence: The nuclei, labeled with DAPI, were counted via CellProfiler 3.0, while the number of cells staining for MUC2 and TFF3 was counted manually. *** P ≤ 0.001, “NS” ( P > 0.05) indicates a nonsignificant comparison.
- Full pipeline: visualisation [Fiji, ImageJ, QuPath] -> stage not stated [CellProfiler v3.0]

### Poly ADP-ribose signaling is dysregulated in Huntington disease. (PNAS 2024)

- DOI: 10.1073/pnas.2318098121 | PMCID: PMC11459172 | PMID: 39331414
- Evidence: Nuclei were identified as primary objects in CellProfiler ( 95 ) using the Hoechst staining, then pixel intensity of the RADD and PAR staining within nuclei was calculated and the mean intensity recorded for each image.
- Full pipeline: quantification [ImageJ] -> stage not stated [CellProfiler]

### Abortive and productive infection of CNS cell types following in vivo delivery of VSV. (PNAS 2024)

- DOI: 10.1073/pnas.2406421121 | PMCID: PMC11363278 | PMID: 39159381
- Evidence: Image Processing and Semiautomated Quantification with CellProfiler.
- Full pipeline: quantification [CellProfiler] -> stage not stated [ImageJ]

### Circadian period is compensated for repressor protein turnover rates in single cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404738121 | PMCID: PMC11348271 | PMID: 39141353
- Evidence: Cell tracking was performed automatically using CellProfiler.
- Full pipeline: quality control [Python] -> stage not stated [CellProfiler, SciPy]

### MAVS Cys508 palmitoylation promotes its aggregation on the mitochondrial outer membrane and antiviral innate immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2403392121 | PMCID: PMC11348129 | PMID: 39141356
- Evidence: Image quantification was performed using CellProfiler [v4.1.3 (1)] ( 57 ).
- Full pipeline: quantification [CellProfiler, ImageJ] -> visualisation [Matplotlib, SciPy] -> stage not stated [Fiji]

### Loss of primary cilia and dopaminergic neuroprotection in pathogenic LRRK2-driven and idiopathic Parkinson's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2402206121 | PMCID: PMC11317616 | PMID: 39088390
- Evidence: All image visualizations and analyses were performed using Fiji ( 60 ) and CellProfiler ( 61 ).
- Full pipeline: dimensionality reduction/clustering [scDblFinder] -> visualisation [CellProfiler] -> stage not stated [Seurat]

### The multifunction <i>Coxiella</i> effector Vice stimulates macropinocytosis and interferes with the ESCRT machinery. (PNAS 2024)

- DOI: 10.1073/pnas.2315481121 | PMCID: PMC11194487 | PMID: 38870060
- Evidence: (Scale bars: 10 µm.) ( H ) The median size of LAMP1-positive compartments in U2OS cells expressing either HA-tag alone or HA-Vice was measured using CellProfiler.
- Full pipeline: normalisation [ImageJ] -> stage not stated [CellProfiler]

### Structural insights reveal interplay between LAG-3 homodimerization, ligand binding, and function. (PNAS 2024)

- DOI: 10.1073/pnas.2310866121 | PMCID: PMC10962948 | PMID: 38483996
- Evidence: Images were quantified for total GFP fluorescence intensity using CellProfiler.
- Full pipeline: quantification [CellProfiler] -> stage not stated [AlphaFold]

### Design of universal Ebola virus vaccine candidates via immunofocusing. (PNAS 2024)

- DOI: 10.1073/pnas.2316960121 | PMCID: PMC10873634 | PMID: 38319964
- Evidence: Infected and total cells were counted using a customized pipeline in CellProfiler (Broad Institute, available upon request).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CellProfiler, Fiji v2.3.0, ImageJ v2.3.0, PyMOL]

### De novo design of modular protein hydrogels with programmable intra- and extracellular viscoelasticity. (PNAS 2024)

- DOI: 10.1073/pnas.2309457121 | PMCID: PMC10861882 | PMID: 38289949
- Version used: **4.0**
- Evidence: Viable and nonviable cells were counted using CellProfiler 4.0.
- Full pipeline: stage not stated [CellProfiler v4.0, Fiji, ImageJ]

### Logic-based mechanistic machine learning on high-content images reveals how drugs differentially regulate cardiac fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2303513121 | PMCID: PMC10835125 | PMID: 38266046
- Evidence: To quantify αSMA expression, an automated image analysis pipeline was employed in CellProfiler (Broad Institute) ( 22 ).
- Full pipeline: quantification [CellProfiler] -> differential/statistical testing [Python v3.8.5, statsmodels]

### Self-organized BMP signaling dynamics underlie the development and evolution of digit segmentation patterns in birds and mammals. (PNAS 2024)

- DOI: 10.1073/pnas.2304470121 | PMCID: PMC10786279 | PMID: 38175868
- Evidence: We quantified NOG FISH signals and protein marker expression using CellProfiler ( 82 ), and binarized cells into marker “ON/OFF” states using the R package segmented ( 83 ).
- Full pipeline: quantification [CellProfiler, R] -> visualisation [Seurat v3.1.4, Slingshot]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Evidence: Nuclear morphology was analyzed using a CellProfiler pipeline (code available on GitHub via the links provided below) to quantify nuclear area and perimeter.
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### Replication stress-induced nuclear hypertrophy alters chromatin topology and impacts cancer cell fitness. (PNAS 2025)

- DOI: 10.1073/pnas.2424709122 | PMCID: PMC12452916 | PMID: 40928878
- Version used: **4.2.1**
- Evidence: Nuclear segmentation and signal quantification were carried out using CellProfiler 4.2.1.
- Full pipeline: quantification [CellProfiler v4.2.1] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Lysosomal glucocerebrosidase is needed for ciliary Hedgehog signaling: A convergent pathway contributing to Parkinson's disease. (PNAS 2025)

- DOI: 10.1073/pnas.2504774122 | PMCID: PMC12337309 | PMID: 40737317
- Evidence: The images were acquired using ZEN 3.4 (blue edition) software, and visualizations and analyses were performed using Fiji ( 50 ) and CellProfiler ( 51 ).
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [CellProfiler]

### Histone variant H2A.W7 represses meiotic crossover formation in &lt;i&gt;Arabidopsis&lt;/i&gt; heterochromatin. (PNAS 2025)

- DOI: 10.1073/pnas.2414166122 | PMCID: PMC12146724 | PMID: 40440068
- Evidence: Seed images were captured with a Leica M165 FC microscope and analyzed with CellProfiler.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [CellProfiler]

### Antigen mobility regulates the dynamics and precision of antigen capture in the B cell immune synapse. (PNAS 2025)

- DOI: 10.1073/pnas.2422528122 | PMCID: PMC12107191 | PMID: 40354540
- Evidence: The ImageJ/Fiji, CellProfiler, Icy, and Python scripts used for image analysis are available on GitHub ( https://github.com/SpillaneLab ) ( 85 ).
- Full pipeline: stage not stated [CellProfiler, ImageJ, Python]

### Acute chromatin decompaction stiffens the nucleus as revealed by nanopillar-induced nuclear deformation in cells. (PNAS 2025)

- DOI: 10.1073/pnas.2416659122 | PMCID: PMC12088434 | PMID: 40343993
- Evidence: H3K27me3 foci analysis follows the methodology provided by McQuin et al. for CellProfiler ( 57 ).
- Full pipeline: stage not stated [CellProfiler, ggplot2]

### The histone variant H2A.W restricts heterochromatic crossovers in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2413698122 | PMCID: PMC12002335 | PMID: 40184177
- Evidence: Approximately 1,000 to 1,500 seeds from the individual seed-based FTL hemizygous plant Columbia-0 Traffic Line 3.9 ( CTL3.9 ) can be automatically scored to measure crossover frequency (cM) by analyzing the frequency of each type of fluorescent seed using CellProfiler ( Fig.
- Full pipeline: stage not stated [CellProfiler]

### Logic-based machine learning predicts how escitalopram attenuates cardiomyocyte hypertrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2420499122 | PMCID: PMC11912418 | PMID: 40035765
- Evidence: These images were processed using CellProfiler ( 31 ) using a cellular segmentation algorithm developed previously and validated to within 5% of two independent manual segmentations ( 32 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [CellProfiler, Cytoscape]

### EGFR-induced lncRNA &lt;i&gt;TRIDENT&lt;/i&gt; promotes drug resistance in non-small cell lung cancer via phospho-TRIM28-mediated DNA damage repair. (PNAS 2025)

- DOI: 10.1073/pnas.2415389122 | PMCID: PMC11912419 | PMID: 40030013
- Evidence: (Scale bar, 10 μm.) ( B ) Quantification of the average number of γH2AX foci per nuclei calculated using CellProfiler.
- Full pipeline: quantification [CellProfiler]

### Endogenous LRRK2 and PINK1 function in a convergent neuroprotective ciliogenesis pathway in the brain. (PNAS 2025)

- DOI: 10.1073/pnas.2412029122 | PMCID: PMC11804522 | PMID: 39874296
- Evidence: The fraction of PPM1H on mitochondria was quantified by measuring the fraction of PPM1H-mApple labeled pixels that coincide with GFP-Mito labeled pixels after image segmentation using CellProfiler as detailed in 10.17504/protocols.io.j8nlk8qk6l5r/v1 .
- Full pipeline: quantification [CellProfiler]

### The single-stranded DNA-binding factor SUB1/PC4 alleviates replication stress at telomeres and is a vulnerability of ALT cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2419712122 | PMCID: PMC11745411 | PMID: 39772744
- Evidence: Telomeric SUB1 foci were automatically counted using CellProfiler.
- Full pipeline: stage not stated [CellProfiler, Cytoscape, ImageJ, STRING db]

### Reconstructing EBV reactivation and DNA damage response kinetics in morphologic pseudotime. (PNAS 2026)

- DOI: 10.1073/pnas.2609598123 | PMCID: PMC13250554 | PMID: 42234528
- Evidence: ( B ) Representative CellProfiler segmentation of nuclei, cytoplasm, and whole cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Seurat]

### HPV16 E6 oncoprotein promotes microhomology-mediated viral integration by increasing PolΘ protein expression. (PNAS 2026)

- DOI: 10.1073/pnas.2532479123 | PMCID: PMC12974484 | PMID: 41785316
- Evidence: Foci quantification was performed using CellProfiler software (version 4.2.6).
- Full pipeline: quantification [CellProfiler, ImageJ]

### Lack of synergy between AR-targeted therapies and PARP inhibitors in homologous recombination-proficient prostate cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2515790122 | PMCID: PMC12867744 | PMID: 41591905
- Evidence: Images were acquired using a Zeiss Axio Observer microscope with a 63× objective, and foci quantification was performed using CellProfiler software.
- Full pipeline: quality control [Cufflinks, DESeq2, STAR] -> alignment/mapping [Cufflinks, DESeq2, STAR] -> quantification [CellProfiler, Cufflinks, DESeq2, STAR] -> normalisation [Cufflinks, DESeq2, STAR] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [Cufflinks, DESeq2, STAR]

### The EPS-I exopolysaccharide transforms &lt;i&gt;Ralstonia&lt;/i&gt; wilt pathogen biofilms into viscoelastic fluids for rapid dissemination in planta. (PNAS 2026)

- DOI: 10.1073/pnas.2512757123 | PMCID: PMC12846841 | PMID: 41570073
- Evidence: We used CellProfiler to quantify the area of individual colonies ( 55 ), which demonstrated that wild-type RSSC colonies occupy roughly double the area compared to ∆ epsB colonies ( Fig.
- Full pipeline: quantification [CellProfiler] -> dimensionality reduction/clustering [BLAST]

### Functionally heterogeneous intratumoral CD4&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; double-positive T cells can give rise to single-positive T cells. (PNAS 2026)

- DOI: 10.1073/pnas.2506168123 | PMCID: PMC12849695 | PMID: 41557789
- Evidence: Cell segmentation was performed using CellProfiler (Broad Institute), with DAPI-stained nuclei as primary objects.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Monocle, Scanpy]

### A pothole-filling strategy for selective targeting of rCUG-repeats associated with myotonic dystrophy type 1. (PNAS 2026)

- DOI: 10.1073/pnas.2507065123 | PMCID: PMC12799113 | PMID: 41512040
- Evidence: Image analysis was performed using custom software developed in MATLAB and CellProfiler, with histograms generated in OriginLab.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS] -> stage not stated [CellProfiler]

### Polyserine domains are toxic and exacerbate tau pathology in mice. (PNAS 2026)

- DOI: 10.1073/pnas.2527425122 | PMCID: PMC12773705 | PMID: 41481461
- Evidence: Quantification of Iba1-positive area of the cerebellum or p-tau-positive area of the hippocampus was performed with a CellProfiler pipeline.
- Full pipeline: quantification [CellProfiler]

### Creation of de novo cryptic splicing for ALS and FTD precision medicine. (Science 2024)

- DOI: 10.1126/science.adk2539 | PMCID: PMC7616720 | PMID: 39361759
- Evidence: Images were then analyzed using CellProfiler ( 31 ): briefly, red objects were identified using an adaptive threshold (“Robust Background” method), then the total intensity of red signal within these objects was calculated.
- Full pipeline: alignment/mapping [STAR v2.7.0f, minimap2 v2.1] -> quantification [ImageJ, STAR v2.7.0f] -> stage not stated [BEDTools, CellProfiler, R, Snakemake v5.5.4]

### Transcripts of repetitive DNA elements signal to block phagocytosis of hematopoietic stem cells. (Science 2024)

- DOI: 10.1126/science.adn1629 | PMCID: PMC12012832 | PMID: 39264994
- Evidence: Data were analyzed using the CellProfiler and R-Sight HTS software.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [CellProfiler, Metascape, R]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Evidence: Supplementary Material Supplement Table S2 MDAR Checklist Acknowledgments We thank Will Allen, Ken Chan, Yi Chen, Keith Joung, Gayathri Muthukumar, Alice Referemat, Jaspreet Sandhu, Fyodor Urnov, Alisa White, Katie Yost, Pu Zheng, the CellProfiler team at the Broad Institute, and members of the Weissman, Vallabh/Minikel, and Liu labs for useful advice and discussion.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Native architecture of a human GBP1 defense complex for cell-autonomous immunity to infection. (Science 2024)

- DOI: 10.1126/science.abm9903 | PMCID: PMC12091997 | PMID: 38422126
- Evidence: All images were subjected to processing to widefield image, de-convolution, and maximum intensity projection for semiautomatic analysis in CellProfiler (Broad Institute, Open Scholar, 2021).
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [EMAN2, UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ImageJ]

### PIEZO channels link mechanical forces to uterine contractions in parturition. (Science 2025)

- DOI: 10.1126/science.ady3045 | PMCID: PMC12807505 | PMID: 41231991
- Evidence: Transcript quantification in RNAscope Maximum z-projection images were used for RNAscope quantification using CellProfiler ( 77 ).
- Full pipeline: alignment/mapping [Seurat] -> quantification [CellProfiler] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy, edgeR] -> visualisation [UMAP] -> stage not stated [scDblFinder]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Version used: **4.0.7**
- Evidence: CellProfiler (v4.0.7) (Broad Institute, US-MA) was used to quantitatively analyze platelet-tumor cell interaction.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Blocking RAN translation without altering repeat RNAs rescues &lt;i&gt;C9ORF72&lt;/i&gt;-related ALS and FTD phenotypes. (Science 2026)

- DOI: 10.1126/science.adv2600 | PMCID: PMC13107528 | PMID: 41643021
- Evidence: To quantify mislocalized Mab414 foci, CellProfiler was used.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> quantification [CellProfiler, Fiji, ImageJ] -> differential/statistical testing [DESeq2, R v4.2.1]

