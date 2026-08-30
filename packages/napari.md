# napari

- **Category:** imaging
- **Papers in survey:** 21
- **Journals:** Nature (11), PNAS (6), Cell (3), Science (1)
- **Years:** 2023 (2), 2024 (5), 2025 (8), 2026 (6)
- **Versions named:** 0.4.17 (1)
- **Pipeline stages it appears in:** visualisation (5), machine learning (1), quantification (1)

## Papers

### Synthetic Par polarity induces cytoskeleton asymmetry in unpolarized mammalian cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.034 | PMCID: PMC10765089 | PMID: 37774705
- Evidence: 55 https://napari.org/ Protein structure predictions Par6A AlphaFold2 https://alphafold.ebi.ac.uk/entry/Q9NPB6 * GG refers to the tricistronic His-PC-GBP-TM-VSVG-GBP + Flag iRFP670-Jupiter + PC-GFP-[protein of interest] ** TetOn refers to a bicistronic rtTA3 + Tet promoter driving the given ORF Resource Availability Lead contact Further information and requests for resources and reagents should be...
- Full pipeline: dimensionality reduction/clustering [ImageJ] -> stage not stated [AlphaFold, napari]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: ...enoCycler Fusion software v2.2.0 Akoya Biosciences https://www.akoyabio.com/phenocycler/ R R-project https://www.r-project.org/ Napari Napari https://napari.org/stable/ Other Matrigel-coated chamber slides ThermoFisher Scientific, Nunc-Labtek 171080 Superfrost Plus Micro Slides VWR 48311-703 Xenium slides 10x Genomics PN-3000941 10x Genomics’ gaskets from the single cell reagent kits 10x Genomics ...
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Nanoscale DNA tracing reveals the self-organization mechanism of mitotic chromosomes. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.028 | PMCID: PMC12127698 | PMID: 40132578
- Evidence: Mitotic and interphase cells were classified manually using napari.
- Full pipeline: quantification [NumPy] -> normalisation [SciPy] -> simulation/modelling [NumPy, OpenMM] -> machine learning [scikit-learn] -> stage not stated [Python, napari, scikit-image]

### The Smc5/6 complex is a DNA loop-extruding motor. (Nature 2023)

- DOI: 10.1038/s41586-023-05963-3 | PMCID: PMC10132971 | PMID: 37076626
- Evidence: Specifically, we utilized PyQtGraph ( https://github.com/pyqtgraph/pyqtgraph ) and napari ( https://github.com/Napari/napari ) 32 for visualization and export of images.
- Full pipeline: visualisation [napari] -> stage not stated [SciPy]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: 3D neighbourhoods were displayed using the open-source visualization tool Napari ( https://github.com/napari/napari ).
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Version used: **0.4.17**
- Evidence: Overlays of selected ETS2-target genes ( CXCL8 , S100A9 , CCL2 , CCL5 ) and fluorescent morphology markers were generated using napari (v.0.4.17, https://napari.org/stable/index.html ) on representative FOVs: FOV287 (PSC with involved duct), FOV294 (PSC background liver) and FOV55 (healthy liver).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: Cells that were imaged without occlusion or growth outside the field of view for the duration of 11 h were manually selected and exported in napari 60 using the napari-crop and napari-nd-cropper plugins.
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: Tissue localization of cell bodies with HCR signal Cell centroids in the HCR data were manually labelled using napari points layer tool 73 , by examination of HCR signal together with the nuclear labelling of the Tg(elavl3:H2b-GCaMP6s) .
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### In situ analysis reveals the TRiC duty cycle and PDCD5 as an open-state cofactor. (Nature 2025)

- DOI: 10.1038/s41586-024-08321-z | PMCID: PMC11754096 | PMID: 39663456
- Evidence: The above optimized setting produced distinguished peaks visualized in napari 55 (Extended Data Fig.
- Full pipeline: alignment/mapping [Clustal Omega, IMOD] -> structure determination [RELION] -> visualisation [ChimeraX, napari] -> stage not stated [AlphaFold]

### Genetically encoded assembly recorder temporally resolves cellular history. (Nature 2026)

- DOI: 10.1038/s41586-026-10323-y | PMCID: PMC13102709 | PMID: 41775935
- Evidence: Image processing and data analysis Python, MATLAB, ImageJ, Vision4D (arivis) and napari were used for image processing and/or visualization.
- Full pipeline: alignment/mapping [PyMOL] -> visualisation [ImageJ, napari]

### Pre-assembly of biomolecular condensate seeds drives RSV replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10071-5 | PMCID: PMC13043309 | PMID: 41606345
- Evidence: The napari-animation plugin was used to generate video output from the napari viewer to create supplementary videos ( https://napari.org/napari-animation/ ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [limma v3.52.4] -> stage not stated [napari]

### Scalable and multiplexed recorders of gene regulation dynamics across weeks. (Nature 2026)

- DOI: 10.1038/s41586-026-10156-9 | PMCID: PMC13102694 | PMID: 41588170
- Evidence: Software for image analysis Image analysis was performed in ImageJ (National Institutes of Health), napari 54 (napari contributors) and Python.
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [UMAP, scikit-image] -> simulation/modelling [AlphaFold, GROMACS v2021.1] -> stage not stated [ImageJ, PyTorch, napari]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: For analysis of microglia engulfment, images were analysed using pyclesperanto in the Napari viewer ( https://github.com/clEsperanto/napari_pyclesperanto_assistant ).
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Inhibitory PD-1 axis maintains high-avidity stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09440-x | PMCID: PMC12727512 | PMID: 41299179
- Evidence: Animation For animation of 3D imaging datasets, the napari-animation library was used and an animation script based on the instructions provided by the developers was made to generate keyframes specifying the camera positions and angles, image layer’s colourmap, adjustments of contrast/brightness, as well as clipping planes for animating transition between layers and for focusing on thin cross-sec...
- Full pipeline: quantification [seaborn] -> normalisation [Matplotlib, scikit-learn] -> dimensionality reduction/clustering [Matplotlib, scikit-learn] -> visualisation [Matplotlib, scikit-image, scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2, napari]

### An ankyrin G-binding motif mediates TRAAK periodic localization at axon initial segments of hippocampal pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2310120121 | PMCID: PMC11295008 | PMID: 39058579
- Evidence: AIS images were deconvolved using Huygens Professional version 22.04 (Scientific Volume Imaging, The Netherlands, http://svi.nl ) and image analysis was performed with the in-house developed K2 Napari Wave Breaker plugin version 0.1.4 for napari (DOI: 10.5281/zenodo.3555620 ) publicly available at https://github.com/SamKVs/napari-k2-WaveBreaker .
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Python v3.9] -> stage not stated [AlphaFold, ImageJ, NumPy, napari]

### TMEM16F exacerbates tau pathology and mediates phosphatidylserine exposure in phospho-tau-burdened neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2311831121 | PMCID: PMC11228522 | PMID: 38941274
- Evidence: Images were processed and analyzed with Slide Scope Virtual Scan, ImageJ software, and Python scikit and napari plugins.
- Full pipeline: stage not stated [ImageJ, Python, napari, scikit-image]

### Light-field deep learning enables high-throughput, scattering-mitigated calcium imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2510337122 | PMCID: PMC12685042 | PMID: 41289378
- Evidence: Volumes and videos were visualized and rendered with napari ( 93 ).
- Full pipeline: visualisation [napari] -> stage not stated [PyTorch, Python]

### A steady-state pool of calcium-dependent actin is maintained by Homer and controls epithelial mechanosensation. (PNAS 2025)

- DOI: 10.1073/pnas.2509784122 | PMCID: PMC12582288 | PMID: 41134626
- Evidence: Images were prepared for quantification using ImageJ/Fiji and a Napari package ( https://www.github.com/haesleinhuepf/devbio-napari ).
- Full pipeline: quantification [napari] -> normalisation [Matplotlib, NumPy, SciPy, seaborn, statsmodels] -> differential/statistical testing [R] -> stage not stated [ImageJ, scikit-image]

### In situ cryo-ET visualization of mitochondrial depolarization and mitophagic engulfment. (PNAS 2025)

- DOI: 10.1073/pnas.2511890122 | PMCID: PMC12337332 | PMID: 40743392
- Evidence: For subtomogram averaging and template match picking, ATP synthase and prohibitin complexes were manually picked using Napari ( https://www.napari-hub.org/ ) and imported into Relion 5 for particle extraction and downstream processing ( https://github.com/3dem/relion ) (RRID:SCR_016274) ( 91 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, RELION, napari]

### 3D epithelial cell topology tunes signaling range to promote precise patterning. (PNAS 2026)

- DOI: 10.1073/pnas.2522727123 | PMCID: PMC13167770 | PMID: 42090248
- Evidence: The projected and segmented images from the previous step were processed in napari to extract measurement tables using the regionprops plugin.
- Full pipeline: stage not stated [Cellpose, napari]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Evidence: To pick particles, a CRYOLO filament-picking model ( 47 ) was trained by manually selecting microtubules from 100 micrographs using the napari-boxmanager software.
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

