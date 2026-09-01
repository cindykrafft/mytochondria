# Keras

- **Category:** general
- **Papers in survey:** 31
- **Journals:** PNAS (16), Nature (13), Cell (2)
- **Years:** 2021 (5), 2022 (4), 2023 (10), 2024 (5), 2025 (6), 2026 (1)
- **Versions named:** 2.3.1 (2), 2.2.4 (1)
- **Pipeline stages it appears in:** machine learning (13), simulation/modelling (1)

## Papers

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **2.2.4**
- Evidence: ...st+ CD-HIT v4.7 Li and Godzik, 2006 https://github.com/weizhongli/cdhit/wiki TensorFlow v1.10.0 Abadi et al., 2016 https://www.tensorflow.org/install Keras v2.2.4 – https://keras.io/ checkV v0.7.0 Nayfach et al., 2020 https://bitbucket.org/berkeleylab/checkv/src/master/ MCL v14-137 van Dongen, 2000 https://www.micans.org/mcl/index.html?sec_software HMMER v3.1b2 Eddy, 1998 http://hmmer.org/ CrisprC...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Evidence: Keras libraries (2.4.3) from Tensorflow (v2.5) were used to build the long-short-term-memory recurrent neural networks (RNN) models.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Swarm Learning for decentralized and confidential clinical machine learning. (Nature 2021)

- DOI: 10.1038/s41586-021-03583-3 | PMCID: PMC8189907 | PMID: 34040261
- Version used: **2.3.1**
- Evidence: To preprocess the data, we used Keras (v.2.3.1) real-time data augmentation and generation APIs (keras.preprocessing.image.ImageDataGenerator and flow_from_dataframe).
- Full pipeline: alignment/mapping [kallisto v0.43.1] -> normalisation [DESeq2 v1.22.2, R] -> machine learning [Docker] -> stage not stated [Keras v2.3.1, TensorFlow v2.2.0, scikit-learn]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: All of these analyses were carried out in Python using packages from Sci-kit learn 70 , TensorFlow 71 and Keras 72 libraries.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### A compute-in-memory chip based on resistive random-access memory. (Nature 2022)

- DOI: 10.1038/s41586-022-04992-8 | PMCID: PMC9385482 | PMID: 35978128
- Evidence: The model is trained using the Keras framework.
- Full pipeline: machine learning [Keras, PyTorch]

### A foundation model for generalizable disease detection from retinal images. (Nature 2023)

- DOI: 10.1038/s41586-023-06555-x | PMCID: PMC10550819 | PMID: 37704728
- Evidence: Furthermore, a Keras version implemented by Y.K. is available at https://github.com/uw-biomedical-ml/RETFound_MAE .
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.19.5, SciPy v1.5.4, seaborn v0.12.0] -> stage not stated [Keras, PyTorch]

### Wake-like skin patterning and neural activity during octopus sleep. (Nature 2023)

- DOI: 10.1038/s41586-023-06203-4 | PMCID: PMC10322707 | PMID: 37380770
- Evidence: 62 ) network pretrained on the ImageNet 63 database, using the Keras 64 platform (included in TensorFlow v.2.0).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> machine learning [Keras, TensorFlow v2.0] -> stage not stated [Python v3.6, scikit-image]

### The dynamics of pattern matching in camouflaging cuttlefish. (Nature 2023)

- DOI: 10.1038/s41586-023-06259-2 | PMCID: PMC10322717 | PMID: 37380772
- Evidence: 1 – 3 ) was the max-pooled fifth layer activations (conv5_1) of the VGG-19 neural network with weights pretrained with the ImageNet dataset in an object-recognition task, accessed through the Keras platform 42 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [Keras, OpenCV] -> visualisation [R, UMAP] -> stage not stated [PsychoPy, Scanpy]

### Single-cell spatial landscapes of the lung tumour immune microenvironment. (Nature 2023)

- DOI: 10.1038/s41586-022-05672-3 | PMCID: PMC9931585 | PMID: 36725934
- Evidence: We used the TensorFlow (version 2.8.0) framework alongside Keras, which now acts as an interface for the TensorFlow library.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> machine learning [Python v3.7.12] -> stage not stated [Keras, TensorFlow v2.8.0]

### Mapping model units to visual neurons reveals population code for social behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07451-8 | PMCID: PMC11136655 | PMID: 38778103
- Evidence: The model instantiation and optimization was coded in Keras ( https://keras.io/ ) on top of Tensorflow 57 ; we used the default random initialization parameters to initialize weights.
- Full pipeline: machine learning [SLEAP] -> stage not stated [Keras, TensorFlow]

### Avoiding fusion plasma tearing instability with deep reinforcement learning. (Nature 2024)

- DOI: 10.1038/s41586-024-07024-9 | PMCID: PMC10881383 | PMID: 38383624
- Evidence: The tearing-avoidance controller, another DNN model, is trained using the deep deterministic policy gradient 56 method, which is implemented using Keras-RL ( https://keras.io/ ) 57 .
- Full pipeline: machine learning [Keras]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Version used: **2.3.1**
- Evidence: The software used for this methodology was as follows: Python (v.3), Keras (v.2.3.1), tensorflow (v.2.1.0), scikit-learn (v.0.21.3), deeplift (v.0.6.10.0) and biopython (v.1.76).
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Targeted design of synthetic enhancers for selected tissues in the Drosophila embryo. (Nature 2024)

- DOI: 10.1038/s41586-023-06905-9 | PMCID: PMC10830412 | PMID: 38086418
- Evidence: The models were implemented and trained in Keras ( https://keras.io/ ) from TensorFlow v.1.14.0 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Keras, TensorFlow v1.14.0] -> visualisation [R, UMAP] -> stage not stated [BEDTools, MACS2, ggplot2 v3.2.1]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: To overcome this limitation, we re-trained the 50-layer ResNet 81 implemented in Keras ( https://keras.io ; v.2.8.0) for TensorFlow ( https://www.tensorflow.org ; v.2.8.0) from the Python package Cellfinder 80 to classify candidate FOS + cells in our high-resolution light-sheet microscopy imaging dataset as true FOS + cells or artefacts.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: The model was implemented using Keras 61 , trained with mean-square error as loss function and optimized using the Adam optimizer 62 with default parameters.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Functional connectome fingerprinting using shallow feedforward neural networks. (PNAS 2021)

- DOI: 10.1073/pnas.2021852118 | PMCID: PMC8053937 | PMID: 33827923
- Evidence: Training, testing, and validation of the models were performed with Keras and TensorFlow.
- Full pipeline: machine learning [Keras, TensorFlow]

### An ecologically motivated image dataset for deep learning yields better models of human vision. (PNAS 2021)

- DOI: 10.1073/pnas.2011417118 | PMCID: PMC7923360 | PMID: 33593900
- Evidence: DenseNet and VGG19 were obtained via Keras applications.
- Full pipeline: stage not stated [Keras]

### Genome-wide detection of cytosine methylation by single molecule real-time sequencing. (PNAS 2021)

- DOI: 10.1073/pnas.2019768118 | PMCID: PMC7865158 | PMID: 33495335
- Evidence: The program for the CNN model was implemented on the basis of the Keras deep learning framework ( https://keras.io/ ).
- Full pipeline: alignment/mapping [BWA] -> machine learning [Keras]

### Accurate prediction of ice nucleation from room temperature water. (PNAS 2022)

- DOI: 10.1073/pnas.2205347119 | PMCID: PMC9351478 | PMID: 35878028
- Evidence: Convolutional neural networks (CNNs) were used in this study and were built using the Python libraries Keras, which is freely available at ( https://keras.io ), and Tensorflow ( 71 ).
- Full pipeline: machine learning [Keras, TensorFlow] -> stage not stated [AlphaFold]

### Neural functional theory for inhomogeneous fluids: Fundamentals and applications. (PNAS 2023)

- DOI: 10.1073/pnas.2312484120 | PMCID: PMC10723051 | PMID: 38060556
- Evidence: The machine learning routines are implemented in Keras/Tensorflow ( 43 ) and we use the standard Adam ( 47 ) optimizer for the adjustment of the network parameters in order to fit c 1 ⋆ ( x ; [ ρ ] ) against the simulation reference c 1 ( x ) .
- Full pipeline: simulation/modelling [Keras, TensorFlow] -> stage not stated [Picard]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: The LSTM model was written and executed with Keras ( 83 ), an open-source python neural-network library running on top of TensorFlow( 84 ) (v1.x; Google).
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Development potential of nanoenabled agriculture projected using machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2301885120 | PMCID: PMC10288598 | PMID: 37314934
- Evidence: TensorFlow Keras was used in Python 3.8 to build a two-layer connected ANN model.
- Full pipeline: stage not stated [Keras, Python v3.8, R v4.0, TensorFlow, igraph, scikit-learn]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: For transfer learning, these single-cell crops were then resized to 299 × 299 images, and each channel was repeated three times to generate 299 × 299 × 3 images of the size required to extract features using the Xception network model ( 60 ) provided by Keras.
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. (PNAS 2023)

- DOI: 10.1073/pnas.2216399120 | PMCID: PMC9992854 | PMID: 36802420
- Evidence: All models are implemented in Keras ( 56 ) with a Tensorflow backend ( 57 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, Keras, TensorFlow]

### Decoding the metabolic response of <i>Escherichia coli</i> for sensing trace heavy metals in water. (PNAS 2023)

- DOI: 10.1073/pnas.2210061120 | PMCID: PMC9963153 | PMID: 36745806
- Evidence: The 1D CNN model architecture utilizes Keras framework with Tensorflow backend.
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> machine learning [scikit-learn] -> stage not stated [Keras, Python v3.6, TensorFlow]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Evidence: All models were constructed in Python 3 using Keras 2 with a Tensorflow backend.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### Mineral dissolution by dimeric complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2504109122 | PMCID: PMC12541406 | PMID: 41052339
- Evidence: S14 , and the model training was carried out using TensorFlow and Keras.
- Full pipeline: simulation/modelling [PLUMED] -> machine learning [Jupyter, Keras, Python, TensorFlow] -> stage not stated [ImageJ]

### Structure in conversation: Evidence for the vocabulary, semantics, and syntax of prosody. (PNAS 2025)

- DOI: 10.1073/pnas.2403262122 | PMCID: PMC12054737 | PMID: 40258156
- Evidence: The Keras software package was used to construct and train the AE ( 104 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [Keras]

### Advancing forecasting capabilities: A contrastive learning model for forecasting tropical cyclone rapid intensification. (PNAS 2025)

- DOI: 10.1073/pnas.2415501122 | PMCID: PMC11789009 | PMID: 39835899
- Evidence: Tensorflow and Keras were used to build and train the RITCF-contrastive model.
- Full pipeline: stage not stated [Keras, TensorFlow, WRF]

### Decoding the elite soccer player's psychological profile. (PNAS 2025)

- DOI: 10.1073/pnas.2415126122 | PMCID: PMC11760505 | PMID: 39808661
- Evidence: The ANN architecture was constructed using the TensorFlow and Keras frameworks in Python.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Keras, Python, TensorFlow]

### Two-dimensional NMR from a single pulse: Reconstructing heteronuclear 2D spectra via off-resonance decoupling and deep neural networks. (PNAS 2026)

- DOI: 10.1073/pnas.2527937123 | PMCID: PMC13123836 | PMID: 42012953
- Evidence: Keras ( 56 ) and Tensorflow ( 57 ) were used to both train the DNN and to construct 1 H– 13 C correlation maps from the off-resonance datasets using the trained DNN.
- Full pipeline: machine learning [Keras, TensorFlow]

