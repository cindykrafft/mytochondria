# Suite2p

- **Category:** neuro-tools
- **Papers in survey:** 32
- **Journals:** Nature (19), PNAS (10), Cell (2), Science (1)
- **Years:** 2022 (7), 2023 (5), 2024 (5), 2025 (11), 2026 (4)
- **Pipeline stages it appears in:** registration (10), alignment/mapping (3)

## Papers

### Large-scale two-photon calcium imaging in freely moving mice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.02.017 | PMCID: PMC8970296 | PMID: 35305313
- Evidence: ..., 2012 https://imagej.nih.gov/ij/ ScanImage 2021 (matlab) Vidrio Technologies; Pologruto et al., 2003 https://vidriotechnologies.com/scanimage-v2021/ Suite2p (python) Pachitariu et al., 2017 https://github.com/MouseLand/suite2p ROIMatchPub Adam Ranson https://github.com/ransona/ROIMatchPub DeepLabCut (python) Mathis et al., 2018 ; Nath et al., 2019 https://github.com/DeepLabCut/DeepLabCut CIAtah(M...
- Full pipeline: stage not stated [DeepLabCut, ImageJ, Suite2p]

### Cholinergic neuronal activity promotes diffuse midline glioma growth through muscarinic signaling. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.031 | PMCID: PMC12396346 | PMID: 40541184
- Evidence: Imaging data was registered using suite2p before the mean fluorescence image was computed.
- Full pipeline: stage not stated [ImageJ, Suite2p]

### Entorhinal cortex directs learning-related changes in CA1 representations. (Nature 2022)

- DOI: 10.1038/s41586-022-05378-6 | PMCID: PMC9668747 | PMID: 36323779
- Evidence: All axonal regions of interest (ROIs), as identified by Suite2p in the image from a .
- Full pipeline: stage not stated [ImageJ v2.0.0, Suite2p]

### Fos ensembles encode and shape stable spatial maps in the hippocampus. (Nature 2022)

- DOI: 10.1038/s41586-022-05113-1 | PMCID: PMC9452297 | PMID: 36002569
- Evidence: Fluorescence source extraction and classification After motion correction, spatial footprints of fluorescence sources in calcium movies were identified using Suite2p 66 (Python version, https://github.com/MouseLand/suite2p ).
- Full pipeline: alignment/mapping [Cellpose] -> registration [Suite2p]

### Cortical feedback loops bind distributed representations of working memory. (Nature 2022)

- DOI: 10.1038/s41586-022-05014-3 | PMCID: PMC9365695 | PMID: 35896749
- Evidence: The imaging data were registered and pre-processed using a modified Suite2p pipeline 76 .
- Full pipeline: stage not stated [CaImAn, Suite2p]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: First, the built-in Suite2p classification algorithm iscell was applied using the default parameters.
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: Raw fluorescence from sources was extracted with Suite2p 54 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### Cortico-cortical feedback engages active dendrites in visual cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06007-6 | PMCID: PMC10244179 | PMID: 37138089
- Evidence: Calcium imaging data preprocessing Two-photon calcium imaging data were motion-corrected, segmented and fluorescence-deconvolved where indicated using Suite2p 72 in all experiments except for all-optical spine mapping, in which ImageJ was used for online ROI selection.
- Full pipeline: alignment/mapping [Suite2p] -> stage not stated [ImageJ]

### Fast and sensitive GCaMP calcium indicators for imaging neural populations. (Nature 2023)

- DOI: 10.1038/s41586-023-05828-9 | PMCID: PMC10060165 | PMID: 36922596
- Evidence: The movies recorded during loose-seal recordings were motion-corrected and segmented with the Python implementation of Suite2p ( github.com/MouseLand/suite2p ) 67 .
- Full pipeline: structure determination [REFMAC] -> stage not stated [CaImAn, PyMOL, Python, Suite2p, ilastik]

### The cellular coding of temperature in the mammalian cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05705-5 | PMCID: PMC9946826 | PMID: 36755097
- Evidence: Two-photon analysis Motion correction of data, identification of putative neurons and calculation of Δ F / F was carried out using the Suite2p package (v0.9.3) in Python 42 .
- Full pipeline: registration [Python, Suite2p] -> stage not stated [Fiji, ImageJ, Kilosort]

### Volatile working memory representations crystallize with practice. (Nature 2024)

- DOI: 10.1038/s41586-024-07425-w | PMCID: PMC11136659 | PMID: 38750359
- Evidence: Code availability Calcium imaging data analysis ( https://github.com/MouseLand/suite2p , https://github.com/flatironinstitute/NoRMCorre and https://github.com/zivlab/CellReg ), electrophysiology data analysis ( https://github.com/MouseLand/Kilosort and https://github.com/cortex-lab/phy ), animal paw tracking ( https://github.com/DeepLabCut/DeepLabCut ) and decoding analysis ( https://github.com/be...
- Full pipeline: stage not stated [DeepLabCut, Kilosort, Suite2p]

### Multisensory gamma stimulation promotes glymphatic clearance of amyloid. (Nature 2024)

- DOI: 10.1038/s41586-024-07132-6 | PMCID: PMC10917684 | PMID: 38418876
- Evidence: To avoid subtle xy changes in motion, we used the phase correlation rigid registration method implemented in suite2p, using the microglia channel to align the vascular channel.
- Full pipeline: alignment/mapping [Suite2p] -> quantification [ImageJ] -> normalisation [ImageJ] -> registration [Suite2p] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [Seurat v4.0.3, scDblFinder]

### Minute-scale oscillatory sequences in medial entorhinal cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06864-1 | PMCID: PMC10781645 | PMID: 38123682
- Evidence: Analysis of imaging time series Imaging time series data were analysed using the Suite2p 59 Python library ( https://github.com/MouseLand/suite2p ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, Suite2p]

### Unsupervised pretraining in biological neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09180-y | PMCID: PMC12367527 | PMID: 40533561
- Evidence: Processing of calcium imaging data Calcium imaging data were processed using Suite2p 32 , available on GitHub ( www.github.com/MouseLand/suite2p ).
- Full pipeline: visualisation [Matplotlib] -> stage not stated [NumPy, Python, SciPy, Suite2p, scikit-learn]

### Brain-wide presynaptic networks of functionally distinct cortical neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-08631-w | PMCID: PMC12043506 | PMID: 40011781
- Evidence: Processing of two-photon calcium images Two-photon Ca 2+ images were processed using Suite2p 78 , in Python, with default parameters, unless otherwise indicated.
- Full pipeline: stage not stated [Python, Suite2p]

### Learning produces an orthogonalized state machine in the hippocampus. (Nature 2025)

- DOI: 10.1038/s41586-024-08548-w | PMCID: PMC11964937 | PMID: 39939774
- Evidence: Calcium imaging data were saved into tiff files and were processed using the Suite2p toolbox ( https://www.suite2p.org/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Suite2p]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: Analysis of two-photon imaging data Suite2p 77 was used for motion correction, ROI detection, ROI classification, and signal extraction (time constant tau = 7 s, diameter = 4 pixels).
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### A combinatorial neural code for long-term motor memory. (Nature 2025)

- DOI: 10.1038/s41586-024-08193-3 | PMCID: PMC11735397 | PMID: 39537930
- Evidence: Preprocessing of two-photon imaging data Imaging data were preprocessed using Suite2p package 70 to perform motion correction and extract raw fluorescence signals ( F ) from automatically identified regions of interest (ROIs).
- Full pipeline: registration [Suite2p] -> stage not stated [DeepLabCut]

### Vectorized instructive signals in cortical dendrites. (Nature 2026)

- DOI: 10.1038/s41586-026-10190-7 | PMCID: PMC13112360 | PMID: 41741650
- Evidence: Offline image analysis and signal extraction To correct for brain motion after image acquisition, as well as to automatically detect ROIs, we used the Suite2p pipeline 69 .
- Full pipeline: stage not stated [Suite2p]

### Plastic landmark anchoring in zebrafish compass neurons. (Nature 2026)

- DOI: 10.1038/s41586-025-09888-x | PMCID: PMC12916487 | PMID: 41501455
- Evidence: Imaging data preprocessing All imaging data were pre-processed using the suite2p package 51 .
- Full pipeline: differential/statistical testing [scikit-learn v1.1.2] -> stage not stated [SciPy, Suite2p]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: Analysis Image processing Scanbox.sbx files were converted to tiff format and motion-corrected and segmented using Suite2p in Python ( https://github.com/MouseLand/suite2p ).
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Dynamic processing of hunger and thirst by common mesolimbic neural ensembles. (PNAS 2022)

- DOI: 10.1073/pnas.2211688119 | PMCID: PMC9618039 | PMID: 36252036
- Evidence: For two-photon imaging experiments, behavioral data, and imaging data were analyzed using the Suite2p pipeline ( 38 ) and custom Python scripts.
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [Python, Suite2p]

### Functional network topography of the medial entorhinal cortex. (PNAS 2022)

- DOI: 10.1073/pnas.2121655119 | PMCID: PMC8851479 | PMID: 35135885
- Evidence: Numbers indicate Suite2p cell IDs.
- Full pipeline: stage not stated [Suite2p]

### Experience-dependent functional plasticity and visual response selectivity of surviving subplate neurons in the mouse visual cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2217011120 | PMCID: PMC9992851 | PMID: 36812195
- Evidence: Registration and cell detection were performed using Suite2p ( 52 ).
- Full pipeline: registration [Suite2p] -> stage not stated [PsychoPy]

### Cellular-resolution optogenetics reveals attenuation-by-suppression in visual cortical neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2318837121 | PMCID: PMC11551350 | PMID: 39485801
- Evidence: We used the CaImAn toolbox ( 80 ) for motion correction and Suite2p ( 81 ) for cell segmentation to allow manual selection of cell masks.
- Full pipeline: registration [CaImAn, Suite2p]

### Revisiting the high-dimensional geometry of population responses in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2506535122 | PMCID: PMC12625980 | PMID: 41191501
- Evidence: Calcium movie data were processed using the Suite2p toolbox to estimate spike rates of neurons.
- Full pipeline: stage not stated [SciPy, Suite2p]

### Microglia-to-neuron signaling links &lt;i&gt;APOE4&lt;/i&gt; and inflammation to enhanced neuronal lipid metabolism and network activity. (PNAS 2025)

- DOI: 10.1073/pnas.2516103122 | PMCID: PMC12452947 | PMID: 40920927
- Evidence: To analyze neuronal calcium activity, we first used the analysis pipeline Suite2p ( https://github.com/MouseLand/suite2p ) to identify cell regions of interest (ROIs) and extract fluorescent signals.
- Full pipeline: stage not stated [Suite2p]

### Patchy harmonic functional connectivity of the mouse auditory cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2510012122 | PMCID: PMC12260567 | PMID: 40587804
- Evidence: After the imaging session, raw recordings were processed through the Suite2p package ( 65 ) to extract the calcium traces.
- Full pipeline: stage not stated [Suite2p]

### Increased excitatory synapse size in hippocampal place cells compared to silent cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505322122 | PMCID: PMC12167973 | PMID: 40472030
- Evidence: Motion correction, region of interest (ROI) detection, fluorescent trace extraction, and spike deconvolution were performed with the software Suite2p ( 41 ).
- Full pipeline: registration [Suite2p] -> stage not stated [Cellpose, ImageJ, Python, SciPy]

### The visuomotor transformations underlying target-directed behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2416215122 | PMCID: PMC12002292 | PMID: 40127271
- Evidence: We used suite2p ( 43 ) to motion correct and segment cell bodies, identifying a total of 188,272 cell bodies within our dataset of 7 fish, and mapped the cell bodies onto the mapZebrain atlas ( 44 ).
- Full pipeline: alignment/mapping [Suite2p] -> registration [Suite2p]

### Place cells in CA1 lack topographical organization of firing locations. (PNAS 2026)

- DOI: 10.1073/pnas.2528601123 | PMCID: PMC12933062 | PMID: 41706904
- Evidence: Motion correction, ROI extraction, calculation of signal traces and deconvolution were performed by the Python based version of suite2p ( 57 ).
- Full pipeline: registration [Suite2p] -> stage not stated [DeepLabCut]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: For two-photon imaging experiments, behavioral and imaging data were analyzed using the Suite2p pipeline ( 94 ) and custom Python scripts.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

