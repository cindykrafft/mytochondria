# SLEAP

- **Category:** neuro-tools
- **Papers in survey:** 10
- **Journals:** Nature (6), PNAS (3), Science (1)
- **Years:** 2023 (1), 2024 (3), 2025 (5), 2026 (1)
- **Versions named:** 1.3.3 (1), 1.3.0 (1)
- **Pipeline stages it appears in:** machine learning (2), structure determination (1), quantification (1)

## Papers

### Flexible circuit mechanisms for context-dependent song sequencing. (Nature 2023)

- DOI: 10.1038/s41586-023-06632-1 | PMCID: PMC10600009 | PMID: 37821705
- Evidence: Tracking Male and female poses (locations of head, thorax, and left and right wing tip) were automatically estimated and tracked, and manually proofread for all videos using SLEAP 17 ( sleap.ai ).
- Full pipeline: differential/statistical testing [Brian2] -> simulation/modelling [Brian2] -> machine learning [CaImAn, PyTorch] -> stage not stated [Python v2.7, SLEAP]

### The mechanism for directional hearing in fish. (Nature 2024)

- DOI: 10.1038/s41586-024-07507-9 | PMCID: PMC11222163 | PMID: 38898274
- Evidence: Behavioural analysis Tracking Pose tracking of D. cerebrum ’s swimming behaviour was carried out with SLEAP 75 .
- Full pipeline: stage not stated [ImageJ v1.5, Python, SLEAP, SciPy]

### Descending networks transform command signals into population motor control. (Nature 2024)

- DOI: 10.1038/s41586-024-07523-9 | PMCID: PMC11186778 | PMID: 38839968
- Version used: **1.3.0**
- Evidence: 1d ) using SLEAP (v1.3.0) 73 .
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> stage not stated [NetworkX, SLEAP v1.3.0]

### Mapping model units to visual neurons reveals population code for social behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07451-8 | PMCID: PMC11136655 | PMID: 38778103
- Evidence: ...16 18 24 16 17 75 459 Joint positions for the male and female for every frame were tracked with a DNN trained for multi-animal pose estimation called SLEAP 51 .
- Full pipeline: machine learning [SLEAP] -> stage not stated [Keras, TensorFlow]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: ...ng (CaImAn 7 and Suite2P 8 ), Neuropixels recordings (KiloSort 9 and MountainSort 10 ), label-free behavioural tracking (DeepLabCut 11 , MoSeq 12 and SLEAP 13 ) and spatial transcriptomics (Giotto 14 and Squidpy 15 ), the goal of NEURD is to make ‘big neuroscience data’ (in this case, large-scale electron microscopy reconstructions) accessible to a larger community.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### A brain reward circuit inhibited by next-generation weight-loss drugs in mice. (Nature 2026)

- DOI: 10.1038/s41586-026-10444-4 | PMCID: PMC13293854 | PMID: 42092139
- Version used: **1.3.3**
- Evidence: Machine-learning-assisted behaviour classification Mouse pose tracking was performed using SLEAP (v.1.3.3) 24 , 25 .
- Full pipeline: normalisation [NetworkX] -> visualisation [NetworkX] -> stage not stated [ImageJ, OpenCV, SLEAP v1.3.3]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Evidence: For data analysis, video footage (20 frames/s) of X. umbellata pulsation was processed using SLEAP ( 97 ).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### Time-of-day modulation in mosquito response persistence to carbon dioxide is controlled by Pigment-Dispersing Factor. (PNAS 2025)

- DOI: 10.1073/pnas.2520826122 | PMCID: PMC12646304 | PMID: 41218121
- Evidence: SLEAP was used to track animal activity and identity ( 75 ).
- Full pipeline: stage not stated [R v4.2.3, SLEAP]

### The cingulate cortex facilitates auditory perception under challenging listening conditions. (PNAS 2025)

- DOI: 10.1073/pnas.2412453122 | PMCID: PMC12002281 | PMID: 40168120
- Evidence: Animal position was quantified using SLEAP, a framework for pose tracking via deep learning ( 36 ).
- Full pipeline: quantification [SLEAP] -> machine learning [SLEAP]

### Hedonic eating is controlled by dopamine neurons that oppose GLP-1R satiety. (Science 2025)

- DOI: 10.1126/science.adt0773 | PMCID: PMC12009138 | PMID: 40146831
- Evidence: To calculate the body length, we analyzed video tracking data by identifying key anatomical points, including the mouth and tail-base, within the cage using SLEAP (Social LEAP Estimates Animal Poses; www.sleap.ai ).
- Full pipeline: stage not stated [R, SLEAP, emmeans]

