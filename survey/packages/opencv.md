# OpenCV

- **Category:** imaging
- **Papers in survey:** 45
- **Journals:** PNAS (24), Nature (20), Science (1)
- **Years:** 2022 (3), 2023 (7), 2024 (10), 2025 (19), 2026 (6)
- **Versions named:** 4.9.0 (1), 4.5.1.48 (1)
- **Pipeline stages it appears in:** machine learning (5), differential/statistical testing (1), quantification (1), alignment/mapping (1), registration (1), visualisation (1), normalisation (1), simulation/modelling (1)

## Papers

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: The code was written in Python and used the OpenCV and OpenSlide library.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Diverse organic-mineral associations in Jezero crater, Mars. (Nature 2023)

- DOI: 10.1038/s41586-023-06143-z | PMCID: PMC10371864 | PMID: 37438522
- Evidence: The script uses the OpenCV library built in classes to implement BRISK keypoint detection and a FLANN-based matcher to match keypoints to generate the overlays.
- Full pipeline: stage not stated [OpenCV, Python, SciPy]

### The dynamics of pattern matching in camouflaging cuttlefish. (Nature 2023)

- DOI: 10.1038/s41586-023-06259-2 | PMCID: PMC10322717 | PMID: 37380772
- Evidence: The inputs to the neural network were preprocessed as follows: cuttlefish images were converted into 8-bit greyscale and histogram-equalized using OpenCV 4 (ref.
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [Keras, OpenCV] -> visualisation [R, UMAP] -> stage not stated [PsychoPy, Scanpy]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: Next, the location of the mouse was identified by finding the centroid of the contour with the largest area using the OpenCV findcontours function.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### Chemical reservoir computation in a self-organizing reaction network. (Nature 2024)

- DOI: 10.1038/s41586-024-07567-x | PMCID: PMC11254755 | PMID: 38926572
- Evidence: Images were adapted to plots using OpenCV-Python 50 .
- Full pipeline: stage not stated [OpenCV, Python, scikit-learn]

### Life-cycle-coupled evolution of mitosis in close relatives of animals. (Nature 2024)

- DOI: 10.1038/s41586-024-07430-z | PMCID: PMC11153136 | PMID: 38778110
- Evidence: The tracing of bundles and twist calculations were previously written in Python programming language using PyCharm IDE, with external libraries such as NumPy, scikit-image, Matplotlib, PIL, OpenCV and SciPy.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [HMMER v3.3.2, ImageJ, Matplotlib, NumPy, OpenCV, Python, SciPy, scikit-image]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Evidence: For transcript detection, the OpenCV function adaptiveThreshold was used with a block size of 41 pixels, and a subtracted constant ranging from −80 to −70 among our replicate smFISH experiments.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Online images amplify gender bias. (Nature 2024)

- DOI: 10.1038/s41586-024-07068-x | PMCID: PMC10901730 | PMID: 38355800
- Evidence: Third, we used Python’s OpenCV—a popular open-source deep learning framework—to extract the faces from each image; this algorithm automatically isolates each face and extracts a square including the entire face and minimal surrounding context.
- Full pipeline: machine learning [OpenCV]

### Glasses-free 3D display with ultrawide viewing range using deep learning. (Nature 2025)

- DOI: 10.1038/s41586-025-09752-y | PMCID: PMC12675290 | PMID: 41299166
- Evidence: For the binocular localization part, we use the lightweight face detector 61 built in OpenCV to obtain each eye position.
- Full pipeline: visualisation [Matplotlib] -> stage not stated [OpenCV]

### Slipknot-gauged mechanical transmission and robotic operation. (Nature 2025)

- DOI: 10.1038/s41586-025-09673-w | PMCID: PMC12657242 | PMID: 41299050
- Evidence: For the open slipknot detection, the function Detector(·) was realized by implementing template matching using the scale-invariant feature transform operator from OpenCV.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [OpenCV]

### Age and gender distortion in online media and large language models. (Nature 2025)

- DOI: 10.1038/s41586-025-09581-z | PMCID: PMC12571887 | PMID: 41062689
- Evidence: Next, we applied the OpenCV deep learning module in Python to automatically extract the face from each image.
- Full pipeline: machine learning [OpenCV, Python]

### Network synchrony creates neural filters promoting quiescence in Drosophila. (Nature 2025)

- DOI: 10.1038/s41586-025-09376-2 | PMCID: PMC12527942 | PMID: 40836080
- Version used: **4.9.0**
- Evidence: 5e was quantified using Python (3.11.0) and OpenCV (4.9.0) as previously described 21 .
- Full pipeline: quantification [OpenCV v4.9.0] -> stage not stated [Python]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: 3 ), all images were first corrected for camera distortion using the remap function of OpenCV 85 by linear interpolation based on a reference image of a micrometre-scale microgrid captured with the respective microscope objective.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Evidence: The ISH image was morphed to match its in vivo counterpart using these coordinates with a custom Python script that builds on the OpenCV library 3 .
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: To align histology images with Xenium spatial coordinates, we used an OpenCV Oriented FAST and Rotated BRIEF 47 object to detect key points in the DAPI channel of both histology and Xenium images.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: Next, the array was blurred using the cv2.GaussianBlur function in OpenCV with ksize=(5,5).
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Efficient robot navigation inspired by honeybee learning flights. (Nature 2026)

- DOI: 10.1038/s41586-026-10461-3 | PMCID: PMC13216067 | PMID: 42129549
- Evidence: Second, this region is unwrapped into a rectangular panorama through a linear–polar transformation, implemented with the linearPolar function from the OpenCV library.
- Full pipeline: stage not stated [Docker, OpenCV]

### A brain reward circuit inhibited by next-generation weight-loss drugs in mice. (Nature 2026)

- DOI: 10.1038/s41586-026-10444-4 | PMCID: PMC13293854 | PMID: 42092139
- Evidence: Behaviour localization and categorization The locations of the food hopper, water spout and shelter were identified using OpenCV (2024), and corresponding regions of interest were defined.
- Full pipeline: normalisation [NetworkX] -> visualisation [NetworkX] -> stage not stated [ImageJ, OpenCV, SLEAP v1.3.3]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: We resized to defined length L with the resize() method in OpenCV image package ( https://pypi.org/project/opencv-python/ ).
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### In vitro reconstitution of calcium-dependent recruitment of the human ESCRT machinery in lysosomal membrane repair. (PNAS 2022)

- DOI: 10.1073/pnas.2205590119 | PMCID: PMC9436306 | PMID: 35994655
- Evidence: Subsequently, we adjusted the image contrast to sparse out the image pixel values (using the equalize bar chart from OpenCV) before generating a binary mask (using threshold_otsu from scikit-image, which minimizes the intragroup pixel value variance).
- Full pipeline: stage not stated [ImageJ, OpenCV, Python, scikit-image]

### Random encounters and amoeba locomotion drive the predation of &lt;i&gt;Listeria monocytogenes&lt;/i&gt; by &lt;i&gt;Acanthamoeba castellanii&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122659119 | PMCID: PMC9371647 | PMID: 35914149
- Evidence: Prior to tracking of the Listeria cells with Trackpy ( 53 ), two dynamic masks (an Acanthamoeba mask and an interaction mask for each individual frame) were created for each region of interest using mathematical operations from the OpenCV ( 55 ) and SciPy ( 56 ) modules ( Fig.
- Full pipeline: stage not stated [ImageJ, OpenCV, Python, SciPy]

### Programmable self-organization of heterogeneous microrobot collectives. (PNAS 2023)

- DOI: 10.1073/pnas.2221913120 | PMCID: PMC10268276 | PMID: 37276400
- Evidence: A Python script was developed using the OpenCV library to process the experimental videos and extract the positions of the microrobots.
- Full pipeline: stage not stated [OpenCV, Python]

### Cellular segregation in cocultures is driven by differential adhesion and contractility on distinct timescales. (PNAS 2023)

- DOI: 10.1073/pnas.2213186120 | PMCID: PMC10104523 | PMID: 37011207
- Evidence: Cell positions and areas were obtained using OpenCV as described by Skamrahl et al.
- Full pipeline: dimensionality reduction/clustering [scikit-image] -> stage not stated [Cellpose v1.0, OpenCV, Python]

### Collective magnetotaxis of microbial holobionts is optimized by the three-dimensional organization and magnetic properties of ectosymbionts. (PNAS 2023)

- DOI: 10.1073/pnas.2216975120 | PMCID: PMC10013862 | PMID: 36848579
- Evidence: The trajectories and U-turn of 22 MHB were extracted and smoothed by a tracking script written in python and based on the OpenCV object tracking algorithms with the Channel and Spatial Reliability (CSR) tracker.
- Full pipeline: simulation/modelling [OpenCV] -> structure determination [IMOD] -> stage not stated [ImageJ]

### 3D electron microscopy for analyzing nanoparticles in the tumor endothelium. (PNAS 2024)

- DOI: 10.1073/pnas.2406331121 | PMCID: PMC11665908 | PMID: 39665759
- Evidence: Contrast Limited Adaptive histogram equalization (CLAHE) was then applied via OpenCV ( 33 ) to increase contrast across the image stack.
- Full pipeline: alignment/mapping [Python] -> stage not stated [ImageJ, OpenCV, scikit-learn]

### Emergent behaviors of buckling-driven elasto-active structures. (PNAS 2024)

- DOI: 10.1073/pnas.2410654121 | PMCID: PMC11551342 | PMID: 39471217
- Evidence: With Python’s Open Source Computer Vision (OpenCV) package ( 30 ), we postprocess the recorded videos by tracking the attached markers’ position data ( x , y , t ) with time.
- Full pipeline: stage not stated [OpenCV]

### Can names shape facial appearance? (PNAS 2024)

- DOI: 10.1073/pnas.2405334121 | PMCID: PMC11287245 | PMID: 39008667
- Evidence: Initially, OpenCV’s deep learning face detector, which is based on the single shot detector (SSD) framework with a ResNet base network, was employed to crop faces from the images.
- Full pipeline: machine learning [OpenCV]

### Metastable precipitation and ion-extractant transport in liquid-liquid separations of trivalent elements. (PNAS 2024)

- DOI: 10.1073/pnas.2315584121 | PMCID: PMC10990121 | PMID: 38507453
- Evidence: The video was converted into individual frames in RGB format with the OpenCV python library ( https://pypi.org/project/opencv-python/ ).
- Full pipeline: stage not stated [OpenCV]

### Predation without direction selectivity. (PNAS 2024)

- DOI: 10.1073/pnas.2317218121 | PMCID: PMC10962952 | PMID: 38483997
- Evidence: Custom software (OpenCV, Python) was used to extrapolate the mouse’s position relative to the cricket, as previously described ( 34 ).
- Full pipeline: stage not stated [DeepLabCut, OpenCV, PsychoPy]

### Mechanism and cellular function of direct membrane binding by the ESCRT and ERES-associated Ca<sup>2+</sup>-sensor ALG-2. (PNAS 2024)

- DOI: 10.1073/pnas.2318046121 | PMCID: PMC10907313 | PMID: 38386713
- Evidence: Subsequently, we adjusted the image contrast to sparse out the image pixel values (using Equalize Bar chart from OpenCV) before generating a binary mask (using threshold_otsu from scikit-image, which minimizes the intra-group pixel value variance).
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis v2.0] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, ImageJ, OpenCV, PyMOL, Python, scikit-image]

### Engineered calcium-regulated affinity protein for efficient internalization and lysosomal toxin delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2509081122 | PMCID: PMC12685030 | PMID: 41289384
- Evidence: Image processing was performed in Fiji for background subtraction and in Python (OpenCV, SciPy, NumPy, scikit-image) for analysis.
- Full pipeline: structure determination [ChimeraX v1.9, PHENIX v1.21.2] -> visualisation [ChimeraX v1.9, PHENIX v1.21.2] -> stage not stated [AlphaFold, NumPy, OpenCV, Python, SciPy, scikit-image]

### On the scale of heterogeneity in composite electrodes of batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2520136122 | PMCID: PMC12582338 | PMID: 41129219
- Evidence: Image analysis is performed using the open-source library, OpenCV, to identify NMC particles in the images and calculate their average pixel intensity values.
- Full pipeline: alignment/mapping [scikit-image] -> dimensionality reduction/clustering [SciPy] -> structure determination [scikit-image] -> visualisation [Matplotlib, NumPy] -> stage not stated [OpenCV, Python]

### From propulsion to suction: Unraveling thrust reversal in propellers at intermediate Reynolds numbers. (PNAS 2025)

- DOI: 10.1073/pnas.2504153122 | PMCID: PMC12519195 | PMID: 41037635
- Evidence: Rotation angles were extracted using OpenCV-based tracking, and water tunnel experiments confirmed consistent speeds between fixed and free-motion conditions ( SI Appendix , Fig.
- Full pipeline: stage not stated [OpenCV]

### Electrokinetic propulsion for electronically integrated microscopic robots. (PNAS 2025)

- DOI: 10.1073/pnas.2500526122 | PMCID: PMC12305017 | PMID: 40663604
- Evidence: Images from a USB camera (Basler Ace2 USB Camera) are sent to a Python script where robot positions and engine locations are determined by using adaptive thresholding in OpenCV ( 52 ) to extract contours.
- Full pipeline: stage not stated [ImageJ, OpenCV, Python]

### A quantitative imaging framework for lithium morphology: Linking deposition uniformity to cycle stability in lithium metal batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2502518122 | PMCID: PMC12305041 | PMID: 40663608
- Evidence: Images were binarized in Python using OpenCV’s cv2.THRESH_BINARY method by retaining a fixed percentage of the brightest pixels in each image to account for contrast variations.
- Full pipeline: stage not stated [OpenCV, Python]

### Equilibrium-gated pattern formation: How molecular dissociation thermodynamics drive emergent behavior in dissipative polymeric systems. (PNAS 2025)

- DOI: 10.1073/pnas.2503176122 | PMCID: PMC12184403 | PMID: 40493201
- Evidence: Front speed measurements were determined from video recordings using either the open-source physics software package Tracker® or a custom-built Python algorithm based on the OpenCV library.
- Full pipeline: stage not stated [OpenCV]

### Near-zero photon bioimaging by fusing deep learning and ultralow-light microscopy. (PNAS 2025)

- DOI: 10.1073/pnas.2412261122 | PMCID: PMC12130841 | PMID: 40388622
- Evidence: This step was completed on a supercomputer ( 49 ) using Python and the OpenCV package ( see online source code ).
- Full pipeline: stage not stated [ImageJ, OpenCV]

### The world through infant eyes: Evidence for the early emergence of the cardinal orientation bias. (PNAS 2025)

- DOI: 10.1073/pnas.2421277122 | PMCID: PMC12037014 | PMID: 40228134
- Evidence: We then converted to gray-scale using the ITU-R 601-2 luma transform via the OpenCV Python library ( 63 ) and normalized the pixel intensities to values between zero and one.
- Full pipeline: normalisation [OpenCV]

### Pulsatile flow induces chromatin interaction with lamin-associated proteins to enrich H3K9 methylation in endothelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424566122 | PMCID: PMC11962468 | PMID: 40117319
- Evidence: The nuclear morphology assay was analyzed using python 3.5 with open source image analysis libraries OpenCV, Scikit-Image, and pillow.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [HOMER, ImageJ, MACS2, OpenCV]

### Triggering and modulation of a complex behavior by a single peptidergic command neuron in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420452122 | PMCID: PMC11929487 | PMID: 40085652
- Evidence: Wandering larvae filmed in the pupariation monitor device ( 17 ) under white or blue light were evaluated for the occurrence of GSB using custom written python scripts available at https://github.com/AndresGarelli/Larva_Tracking_OpenCV .
- Full pipeline: stage not stated [ImageJ, OpenCV]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Version used: **4.5.1.48**
- Evidence: The largest continuous stained area was segmented with an automated script in Python3.7 using OpenCV (v4.5.1.48; SI Appendix , Fig.
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: Pairwise optical flow was computed with OpenCV’s calcOpticalFlowFarneback (pyr_scale = 0.5, levels = 3, winsize = 15, iterations = 3, poly_n = 5, poly_sigma = 1.2, flags = 0).
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: It was implemented in Python, utilizing OpenCV, PIL, Tkinter/CustomTkinter, Matplotlib, NumPy, and Pandas for image processing, visualization, and data management, and with aicspylibczi for handling czi files.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: First, we used feature registration algorithm implemented in Python via OpenCV-contrib library (version 4.3.0) ( 73 ) to compute an affine transformation of DAPI channel from cycle r>1 (moving image) with respect to DAPI channel from the first cycle r=1 (reference image).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

