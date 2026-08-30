# TensorFlow

- **Category:** general
- **Papers in survey:** 90
- **Journals:** PNAS (57), Nature (27), Science (3), Cell (3)
- **Years:** 2021 (15), 2022 (12), 2023 (28), 2024 (16), 2025 (16), 2026 (3)
- **Versions named:** 2.0 (3), 1.10.0 (2), 2.7.0 (2), 2.18.0 (1), 1.14.0 (1), 1.12 (1), 2.6.0 (1), 2.8.0 (1), 2.2.0 (1), 2.9.1 (1)
- **Pipeline stages it appears in:** machine learning (45), simulation/modelling (2), differential/statistical testing (1), normalisation (1), dimensionality reduction/clustering (1)

## Papers

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **1.10.0**
- Evidence: ... Altschul et al., 1990 + ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+ CD-HIT v4.7 Li and Godzik, 2006 https://github.com/weizhongli/cdhit/wiki TensorFlow v1.10.0 Abadi et al., 2016 https://www.tensorflow.org/install Keras v2.2.4 – https://keras.io/ checkV v0.7.0 Nayfach et al., 2020 https://bitbucket.org/berkeleylab/checkv/src/master/ MCL v14-137 van Dongen, 2000 https://www.micans.org/mcl/...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Version used: **2.5**
- Evidence: Keras libraries (2.4.3) from Tensorflow (v2.5) were used to build the long-short-term-memory recurrent neural networks (RNN) models.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Design principles of cell-state-specific enhancers in hematopoiesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.017 | PMCID: PMC12173716 | PMID: 40345201
- Evidence: Deep learning-based analysis Our deep model, implemented in Tensorflow, follows a relatively simple architecture of four convolutional layers stacked on top of three fully connected layers.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ArchR] -> machine learning [TensorFlow] -> stage not stated [R, ggplot2, kallisto, pheatmap]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Version used: **2.0**
- Evidence: The training and testing processes were conducted via TensorFlow 2.0 66 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Skilful precipitation nowcasting using deep generative models of radar. (Nature 2021)

- DOI: 10.1038/s41586-021-03854-z | PMCID: PMC8481123 | PMID: 34588668
- Evidence: Code availability We rely on several open-source code frameworks including Iris (scitools-iris.readthedocs.io), Cartopy (scitools.org.uk/cartopy), TensorFlow ( www.tensorflow.org ), and Colab (colab.sandbox.google.com).
- Full pipeline: stage not stated [Cartopy, TensorFlow]

### Highly accurate protein structure prediction with AlphaFold. (Nature 2021)

- DOI: 10.1038/s41586-021-03819-2 | PMCID: PMC8371605 | PMID: 34265844
- Evidence: For neural network construction, running and other analyses, we used TensorFlow 70 , Sonnet 71 , NumPy 72 , Python 73 and Colab 74 .
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [OpenMM v7.3.1] -> machine learning [HMMER, NumPy, OpenMM v7.3.1, Python, TensorFlow]

### Swarm Learning for decentralized and confidential clinical machine learning. (Nature 2021)

- DOI: 10.1038/s41586-021-03583-3 | PMCID: PMC8189907 | PMID: 34040261
- Version used: **2.2.0**
- Evidence: To run the experiments, we used Python version 3.6.9 with Keras version 2.3.1 and TensorFlow version 2.2.0-rc2.
- Full pipeline: alignment/mapping [kallisto v0.43.1] -> normalisation [DESeq2 v1.22.2, R] -> machine learning [Docker] -> stage not stated [Keras v2.3.1, TensorFlow v2.2.0, scikit-learn]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: For training, the weights were initialized using the default initialization in TensorFlow 62 .
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: All of these analyses were carried out in Python using packages from Sci-kit learn 70 , TensorFlow 71 and Keras 72 libraries.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Scaling deep learning for materials discovery. (Nature 2023)

- DOI: 10.1038/s41586-023-06735-9 | PMCID: PMC10700131 | PMID: 38030720
- Evidence: We also make great of use functionality written in JAX MD for processing crystal structures 63 , as well as TensorFlow for parallelized data input 64 .
- Full pipeline: stage not stated [TensorFlow]

### All-analog photoelectronic chip for high-speed vision tasks. (Nature 2023)

- DOI: 10.1038/s41586-023-06558-8 | PMCID: PMC10620079 | PMID: 37880362
- Evidence: Training of ACCEL For the training of ACCEL, we model the complete analog physical process in both OAC and EAC jointly with Tensorflow, including the modulation and light diffraction in OAC, the nonlinearity using photoelectronic conversion and the equivalent matrix multiplication in EAC.
- Full pipeline: machine learning [TensorFlow]

### Champion-level drone racing using deep reinforcement learning. (Nature 2023)

- DOI: 10.1038/s41586-023-06419-4 | PMCID: PMC10468397 | PMID: 37648758
- Evidence: The training environment is implemented using TensorFlow Agents 51 .
- Full pipeline: machine learning [TensorFlow]

### A high-performance speech neuroprosthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-06377-x | PMCID: PMC10468393 | PMID: 37612500
- Evidence: The RNN is a five-layer, gated recurrent-unit architecture trained using TensorFlow 2.
- Full pipeline: machine learning [TensorFlow]

### An analog-AI chip for energy-efficient speech recognition and transcription. (Nature 2023)

- DOI: 10.1038/s41586-023-06337-5 | PMCID: PMC10447234 | PMID: 37612392
- Evidence: For model size: B, 1 billion; M, 1 million. b , Inference models are trained using popular frameworks such as PyTorch or TensorFlow.
- Full pipeline: machine learning [PyTorch, TensorFlow]

### Wake-like skin patterning and neural activity during octopus sleep. (Nature 2023)

- DOI: 10.1038/s41586-023-06203-4 | PMCID: PMC10322707 | PMID: 37380770
- Version used: **2.0**
- Evidence: 62 ) network pretrained on the ImageNet 63 database, using the Keras 64 platform (included in TensorFlow v.2.0).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> machine learning [Keras, TensorFlow v2.0] -> stage not stated [Python v3.6, scikit-image]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: A TensorFlow U-net model adapted from https://github.com/zhixuhao/unet was trained on a dataset of 595 paired images with masks (70% training and 30% validation) for 7 epochs until the model began to overfit as indicated by the training accuracy exceeding the validation accuracy without improving loss.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### De novo design of protein interactions with learned surface fingerprints. (Nature 2023)

- DOI: 10.1038/s41586-023-05993-x | PMCID: PMC10131520 | PMID: 37100904
- Version used: **1.12**
- Evidence: MaSIF-site was implemented in Tensorflow (v.1.12) 59 , and trained for 40 h on a single-GPU machine, which allowed for 43 epochs.
- Full pipeline: alignment/mapping [AlphaFold] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> structure determination [Coot v0.9.5] -> machine learning [TensorFlow v1.12] -> visualisation [ChimeraX] -> stage not stated [PHENIX v1.20.1, UCSF Chimera]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **2.6.0**
- Evidence: Classifier to predict seeding and non-seeding tumour regions We built the machine-learning framework in Python using Tensorflow (v.2.6.0) 104 and sklearn (v.0.0) 105 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: ...a 1 0 a 2 a 3 T The free parameters a 1 , a 2 , a 3 , σ 1 (2) , σ 2 (2) and l are estimated using maximum likelihood and automatic differentiation in Tensorflow 60 , 61 using the BFGS algorithm.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Single-cell spatial landscapes of the lung tumour immune microenvironment. (Nature 2023)

- DOI: 10.1038/s41586-022-05672-3 | PMCID: PMC9931585 | PMID: 36725934
- Version used: **2.8.0**
- Evidence: We used the TensorFlow (version 2.8.0) framework alongside Keras, which now acts as an interface for the TensorFlow library.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> machine learning [Python v3.7.12] -> stage not stated [Keras, TensorFlow v2.8.0]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: The network was designed using TensorFlow to process images in <33 ms, the time between frame captures on the Microsoft Kinect V2 61 .
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Evidence: We performed tracking of the mice in the video data using DeepLabCut 61 (version 2.0), a Python package for marker-less pose estimation based in the TensorFlow machine learning library.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Bendable non-silicon RISC-V microprocessor. (Nature 2024)

- DOI: 10.1038/s41586-024-07976-y | PMCID: PMC11464375 | PMID: 39322672
- Evidence: To test our accelerator, we developed a Tiny Machine Learning (TinyML) model using Tensorflow 28 to perform ECG anomaly detection using the ECG5000 time series classification dataset 29 .
- Full pipeline: stage not stated [Python, TensorFlow]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: (3) We used TensorFlow 110 (v.2.3.1) to construct the supervised machine learning model with a 50-layer residual network architecture (ResNet50-1D), of which the 4 stacked blocks were composed of 48 convolutional layers, 1 max pool and 1 average pool layer.
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Evidence: For segmentation of epithelioid nuclei, a pre-trained StarDist 89 model (he_heavy_augment.zip) was downloaded from https://github.com/stardist/stardist-imagej/tree/master/src/main/resources/models/2D , and an inference instance was deployed using Groovy across the tiles in QuPath, built from source with Tensorflow 90 , with a minimum detection threshold of 0.5.
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Mapping model units to visual neurons reveals population code for social behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07451-8 | PMCID: PMC11136655 | PMID: 38778103
- Evidence: The model instantiation and optimization was coded in Keras ( https://keras.io/ ) on top of Tensorflow 57 ; we used the default random initialization parameters to initialize weights.
- Full pipeline: machine learning [SLEAP] -> stage not stated [Keras, TensorFlow]

### Targeted design of synthetic enhancers for selected tissues in the Drosophila embryo. (Nature 2024)

- DOI: 10.1038/s41586-023-06905-9 | PMCID: PMC10830412 | PMID: 38086418
- Version used: **1.14.0**
- Evidence: The models were implemented and trained in Keras ( https://keras.io/ ) from TensorFlow v.1.14.0 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Keras, TensorFlow v1.14.0] -> visualisation [R, UMAP] -> stage not stated [BEDTools, MACS2, ggplot2 v3.2.1]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: We used GEE’s TensorFlow output format and ‘kernelSize’ argument to generate tiles that overlapped their neighbours by 300 km (double the largest neighbourhood size in our asynchrony calculations), to allow asynchrony to be calculated independently and in parallel.
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: To overcome this limitation, we re-trained the 50-layer ResNet 81 implemented in Keras ( https://keras.io ; v.2.8.0) for TensorFlow ( https://www.tensorflow.org ; v.2.8.0) from the Python package Cellfinder 80 to classify candidate FOS + cells in our high-resolution light-sheet microscopy imaging dataset as true FOS + cells or artefacts.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Version used: **2.18.0**
- Evidence: For datasets with poorly defined morphology, crypt–villus axis values for each cell were predicted using a TensorFlow v2.18.0 ( https://www.tensorflow.org/ ) deep neural network trained on a feature space comprising a decomposition of latent factors for epithelial and stromal transcriptional neighbourhoods.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Neural networks to learn protein sequence-function relationships from deep mutational scanning data. (PNAS 2021)

- DOI: 10.1073/pnas.2104878118 | PMCID: PMC8640744 | PMID: 34815338
- Evidence: We used Python v3.6 and TensorFlow ( 58 ) v1.14 to implement the models.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [NetworkX, TensorFlow]

### Deep learning for early warning signals of tipping points. (PNAS 2021)

- DOI: 10.1073/pnas.2106140118 | PMCID: PMC8488604 | PMID: 34544867
- Version used: **2.0**
- Evidence: The code was written using TensorFlow 2.0 in Anaconda 2020.02.
- Full pipeline: simulation/modelling [SciPy] -> stage not stated [Conda v2020.02, TensorFlow v2.0]

### How multisensory neurons solve causal inference. (PNAS 2021)

- DOI: 10.1073/pnas.2106235118 | PMCID: PMC8364184 | PMID: 34349023
- Evidence: All the networks described in the study were implemented in Python version 3.6.4 ( https://python.org ) using TensorFlow ( http://www.tensorflow.org ), a library for efficient optimization of mathematical expressions.
- Full pipeline: stage not stated [Psychtoolbox v3.0.11, Python v3.6.4, TensorFlow]

### Interpreting machine learning models to investigate circadian regulation and facilitate exploration of clock function. (PNAS 2021)

- DOI: 10.1073/pnas.2103070118 | PMCID: PMC8364196 | PMID: 34353905
- Version used: **2.0.0**
- Evidence: We developed an ML-based pipeline to predict the circadian time (phase) at any single, transcriptomic sampling timepoint using gene expression data from a set of marker genes using an artificial neural network in TensorFlow (version 2.0.0) ( 82 ).
- Full pipeline: differential/statistical testing [LightGBM, XGBoost] -> machine learning [LightGBM, TensorFlow v2.0.0, XGBoost] -> stage not stated [Jupyter, WGCNA]

### The attention schema theory in a neural network agent: Controlling visuospatial attention using a descriptive model of attention. (PNAS 2021)

- DOI: 10.1073/pnas.2102421118 | PMCID: PMC8379943 | PMID: 34385306
- Evidence: We used a deep Q-learning agent implemented through the TF-Agents library for Python ( 33 ), which allows for computationally efficient training of reinforcement learning models using TensorFlow ( 34 ).
- Full pipeline: machine learning [TensorFlow]

### Automated, multiparametric monitoring of respiratory biomarkers and vital signs in clinical and home settings for COVID-19 patients. (PNAS 2021)

- DOI: 10.1073/pnas.2026610118 | PMCID: PMC8126790 | PMID: 33893178
- Evidence: All analysis used Python 3.0 with SciPy, PyWavelets, and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Functional connectome fingerprinting using shallow feedforward neural networks. (PNAS 2021)

- DOI: 10.1073/pnas.2021852118 | PMCID: PMC8053937 | PMID: 33827923
- Evidence: Training, testing, and validation of the models were performed with Keras and TensorFlow.
- Full pipeline: machine learning [Keras, TensorFlow]

### Public data from three US states provide new insights into well integrity. (PNAS 2021)

- DOI: 10.1073/pnas.2013894118 | PMCID: PMC8040654 | PMID: 33753556
- Evidence: New Mexico integrity testing records were identified by downloading 643,647 documents of unknown types and classifying them using a retrained image classification neural network developed in the open-source machine learning library TensorFlow ( 41 ).
- Full pipeline: machine learning [TensorFlow]

### Density estimation using deep generative neural networks. (PNAS 2021)

- DOI: 10.1073/pnas.2101344118 | PMCID: PMC8054014 | PMID: 33833061
- Evidence: The neural networks in Roundtrip model were implemented with TensorFlow ( 26 ).
- Full pipeline: machine learning [TensorFlow] -> stage not stated [scikit-learn]

### Artificial intelligence velocimetry and microaneurysm-on-a-chip for three-dimensional analysis of blood flow in physiology and disease. (PNAS 2021)

- DOI: 10.1073/pnas.2100697118 | PMCID: PMC8020788 | PMID: 33762307
- Evidence: The governing equations are encoded in the network, where the derivatives are computed via automatic differentiation in the TensorFlow code [Google ( 46 )].
- Full pipeline: stage not stated [TensorFlow]

### Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT. (PNAS 2022)

- DOI: 10.1073/pnas.2214414119 | PMCID: PMC9894175 | PMID: 36459654
- Evidence: Network Architecture. scVAEIT is implemented using the Tensorflow ( 31 ) (version 2.4.1) Python library. scVAEIT consists of three main branches, the mask encoder, the main encoder and the main decoder.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat, TensorFlow]

### Dynamics of plosive consonants via imaging, computations, and soft electronics. (PNAS 2022)

- DOI: 10.1073/pnas.2214164119 | PMCID: PMC9674252 | PMID: 36343234
- Evidence: All analyses used Python 3.0 with SciPy and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Melting temperature prediction using a graph neural network model: From ancient minerals to new materials. (PNAS 2022)

- DOI: 10.1073/pnas.2209630119 | PMCID: PMC9457469 | PMID: 36044552
- Evidence: The machine learning model combines the Graph Neural Network (GNN) ( 21 ) and residual neural network (ResNet) ( 22 ) architectures within the Tensorflow ( 23 ) framework ( Fig.
- Full pipeline: machine learning [TensorFlow] -> stage not stated [XGBoost]

### A photo-switchable assay system for dendrite degeneration and repair in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2204577119 | PMCID: PMC9407391 | PMID: 35969739
- Evidence: The code used for deep learning–based automatic dendrite structure prediction is written in Python/TensorFlow.
- Full pipeline: machine learning [Python, TensorFlow]

### Revisiting [Formula: see text]-wavelet compressed-sensing MRI in the era of deep learning. (PNAS 2022)

- DOI: 10.1073/pnas.2201062119 | PMCID: PMC9388129 | PMID: 35939712
- Evidence: Supervised training was performed with a normalized ℓ 1 - ℓ 2 loss in k space ( 3 , 7 ), using TensorFlow in Python.
- Full pipeline: normalisation [Python, TensorFlow] -> machine learning [Python, TensorFlow]

### Accurate prediction of ice nucleation from room temperature water. (PNAS 2022)

- DOI: 10.1073/pnas.2205347119 | PMCID: PMC9351478 | PMID: 35878028
- Evidence: Convolutional neural networks (CNNs) were used in this study and were built using the Python libraries Keras, which is freely available at ( https://keras.io ), and Tensorflow ( 71 ).
- Full pipeline: machine learning [Keras, TensorFlow] -> stage not stated [AlphaFold]

### Deep learning of dynamically responsive chemical Hamiltonians with semiempirical quantum mechanics. (PNAS 2022)

- DOI: 10.1073/pnas.2120333119 | PMCID: PMC9271210 | PMID: 35776544
- Evidence: NN architectures of this type include hierarchical interacting-particle neural network (HIPNN) ( 8 ), MoleculeNet ( 9 ), TensorMol (Tensorflow Molecules) (10), DPMD (Deep Potential Molecular Dynamics) ( 11 ), SchNet ( 12 – 14 ), ANI-1 (Accurate NeurAl Network Engine for Molecular Energies) ( 15 – 18 ), and PhysNet ( 19 ), etc.
- Full pipeline: simulation/modelling [TensorFlow] -> machine learning [TensorFlow] -> stage not stated [PyTorch, RDKit, SciPy]

### Digital rheometer twins: Learning the hidden rheology of complex fluids through rheology-informed graph neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2202234119 | PMCID: PMC9171907 | PMID: 35544690
- Evidence: The backend of ADCME is TensorFlow, a high-performance deep learning framework that offers parallel processing and automatic differentiation based on computational graphs, in which a value is represented as an edge, and a node represents a function.
- Full pipeline: machine learning [TensorFlow]

### Single-molecule fluorescence imaging and deep learning reveal highly heterogeneous aggregation of amyloid-β 42. (PNAS 2022)

- DOI: 10.1073/pnas.2116736119 | PMCID: PMC8944908 | PMID: 35290118
- Version used: **1.14**
- Evidence: The neural network was trained using TensorFlow 1.14 with a Tesla P100 GPU of NIH HPC Biowulf cluster.
- Full pipeline: dimensionality reduction/clustering [TensorFlow v1.14] -> machine learning [TensorFlow v1.14]

### Neural functional theory for inhomogeneous fluids: Fundamentals and applications. (PNAS 2023)

- DOI: 10.1073/pnas.2312484120 | PMCID: PMC10723051 | PMID: 38060556
- Evidence: The machine learning routines are implemented in Keras/Tensorflow ( 43 ) and we use the standard Adam ( 47 ) optimizer for the adjustment of the network parameters in order to fit c 1 ⋆ ( x ; [ ρ ] ) against the simulation reference c 1 ( x ) .
- Full pipeline: simulation/modelling [Keras, TensorFlow] -> stage not stated [Picard]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: The LSTM model was written and executed with Keras ( 83 ), an open-source python neural-network library running on top of TensorFlow( 84 ) (v1.x; Google).
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Automated crystal system identification from electron diffraction patterns using multiview opinion fusion machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2309240120 | PMCID: PMC10655557 | PMID: 37943836
- Evidence: The CNN was trained with a batch size of 32 and 10 epochs under the framework of Tensorflow.
- Full pipeline: machine learning [TensorFlow]

### Deciphering RNA splicing logic with interpretable machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2221165120 | PMCID: PMC10576025 | PMID: 37796983
- Version used: **2.6**
- Evidence: The model was implemented in Python 3.8 ( 48 ) using Tensorflow 2.6 ( 49 ) and Numpy 1.20 ( 50 ).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [NumPy v1.20, Python v3.8, TensorFlow v2.6]

### Prediction and design of protease enzyme specificity using a structure-aware graph convolutional network. (PNAS 2023)

- DOI: 10.1073/pnas.2303590120 | PMCID: PMC10523478 | PMID: 37729196
- Version used: **1.13.1**
- Evidence: We used the Scikit-learn 0.20.1 ( 66 ) to implement logistic regression (lg), random forest (rf), decision tree (dt), SVM classification, and Tensorflow 1.13.1 ( 67 ) for ANN.
- Full pipeline: differential/statistical testing [TensorFlow v1.13.1, scikit-learn v0.20.1] -> machine learning [PyTorch]

### Physics-supervised deep learning-based optimization (PSDLO) with accuracy and efficiency. (PNAS 2023)

- DOI: 10.1073/pnas.2309062120 | PMCID: PMC10466106 | PMID: 37603744
- Version used: **2.11.0**
- Evidence: We used the TensorFlow (v2.11.0) framework to implement our NN model.
- Full pipeline: stage not stated [TensorFlow v2.11.0]

### Development potential of nanoenabled agriculture projected using machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2301885120 | PMCID: PMC10288598 | PMID: 37314934
- Evidence: TensorFlow Keras was used in Python 3.8 to build a two-layer connected ANN model.
- Full pipeline: stage not stated [Keras, Python v3.8, R v4.0, TensorFlow, igraph, scikit-learn]

### 3D surface reconstruction of cellular cryo-soft X-ray microscopy tomograms using semisupervised deep learning. (PNAS 2023)

- DOI: 10.1073/pnas.2209938120 | PMCID: PMC10268598 | PMID: 37276395
- Evidence: We have implemented the entire data preparation and augmentation pipeline using the TensorFlow ( 66 ) Dataset API, which benefits from automated GPU processing, hence offering uninterrupted training of the network while augmented data are prepared on-the-fly.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> machine learning [TensorFlow] -> stage not stated [SciPy]

### Implicit learning of convective organization explains precipitation stochasticity. (PNAS 2023)

- DOI: 10.1073/pnas.2216158120 | PMCID: PMC10193982 | PMID: 37155849
- Evidence: Both networks are implemented using the Tensorflow library version 2.9 ( 35 ), and the hyperparameters are tuned using the Sherpa hyperparameter tuning library ( 36 ).
- Full pipeline: stage not stated [TensorFlow]

### Triadic influence as a proxy for compatibility in social relationships. (PNAS 2023)

- DOI: 10.1073/pnas.2215041120 | PMCID: PMC10068781 | PMID: 36947512
- Evidence: The artificial neural network was implemented in the standard library TensorFlow ( 50 ) with one input layer of 128 neurons and 3 hidden layers—the sizes of the network layers are 128, 64, 32, and 8—and we use the ReLu activation function.
- Full pipeline: machine learning [TensorFlow]

### Closed-loop network of skin-interfaced wireless devices for quantifying vocal fatigue and providing user feedback. (PNAS 2023)

- DOI: 10.1073/pnas.2219394120 | PMCID: PMC9992836 | PMID: 36802437
- Evidence: All analyses used Python 3.0 with SciPy and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. (PNAS 2023)

- DOI: 10.1073/pnas.2216399120 | PMCID: PMC9992854 | PMID: 36802420
- Evidence: All models are implemented in Keras ( 56 ) with a Tensorflow backend ( 57 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, Keras, TensorFlow]

### Decoding the metabolic response of <i>Escherichia coli</i> for sensing trace heavy metals in water. (PNAS 2023)

- DOI: 10.1073/pnas.2210061120 | PMCID: PMC9963153 | PMID: 36745806
- Evidence: The 1D CNN model architecture utilizes Keras framework with Tensorflow backend.
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> machine learning [scikit-learn] -> stage not stated [Keras, Python v3.6, TensorFlow]

### Data-driven predictions of the time remaining until critical global warming thresholds are reached. (PNAS 2023)

- DOI: 10.1073/pnas.2207183120 | PMCID: PMC9963891 | PMID: 36716375
- Version used: **2.7.0**
- Evidence: The model is coded and trained using Tensorflow 2.7.0, and Tensorflow-Probability 0.15.0.
- Full pipeline: machine learning [TensorFlow v2.7.0] -> stage not stated [SciPy]

### Propagating spatiotemporal activity patterns across macaque motor cortex carry kinematic information. (PNAS 2023)

- DOI: 10.1073/pnas.2212227120 | PMCID: PMC9942811 | PMID: 36652475
- Evidence: To denoise the signal, we used a variant of autoencoders called the contractive autoencoder ( 8 ) (implemented in Tensorflow with adaptions from https://github.com/zaouk/contractive_autoencoders ).
- Full pipeline: stage not stated [TensorFlow]

### Anatomically interpretable deep learning of brain age captures domain-specific cognitive impairment. (PNAS 2023)

- DOI: 10.1073/pnas.2214634120 | PMCID: PMC9926270 | PMID: 36595679
- Version used: **2.7.0**
- Evidence: The DL architecture was implemented in Python 3.6 using TensorFlow 2.7.0 and executed on a computer with an Intel Core i7 processor (2.2 GHz clock speed) with 16 GB of RAM and a 12 GB NVIDIA Tesla K80 graphical processing unit.
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [Python v3.6, TensorFlow v2.7.0]

### DeSide: A unified deep learning approach for cellular deconvolution of tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2407096121 | PMCID: PMC11573681 | PMID: 39514318
- Evidence: Supplementary Material Appendix 01 (PDF) Dataset S01 (XLSX) Dataset S02 (XLSX) Dataset S03 (XLSX) Dataset S04 (XLSX) Dataset S05 (XLSX) Dataset S06 (XLSX) Dataset S07 (XLSX) Dataset S08 (XLSX) Dataset S09 (XLSX) Data, Materials, and Software Availability DeSide is implemented in Python using the TensorFlow library for constructing the DNN model.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, Python, TensorFlow]

### Hyperspectral unmixing for Raman spectroscopy via physics-constrained autoencoders. (PNAS 2024)

- DOI: 10.1073/pnas.2407439121 | PMCID: PMC11551349 | PMID: 39471214
- Evidence: We conducted our analyses in Python, using TensorFlow ( 110 ) for autoencoder model development and training, and the RamanSPy package ( 83 ) for unmixing with conventional methods, data loading and management, preprocessing, and plotting.
- Full pipeline: machine learning [TensorFlow] -> stage not stated [Python]

### The topology and geometry of neural representations. (PNAS 2024)

- DOI: 10.1073/pnas.2317881121 | PMCID: PMC11494346 | PMID: 39374397
- Version used: **1.3.0**
- Evidence: 39 , we trained the DNNs on the complete CIFAR-10 image dataset (both training and test sets), which comprises 10 distinct object categories, each represented by 5,000 training and 1,000 test images, implemented with TensorFlow (version 1.3.0) and Python 3.5.4.
- Full pipeline: machine learning [Python v3.5.4, TensorFlow v1.3.0]

### Stochastic machine learning via sigma profiles to build a digital chemical space. (PNAS 2024)

- DOI: 10.1073/pnas.2404676121 | PMCID: PMC11295021 | PMID: 39042681
- Evidence: 2.5.2) ( 35 ) and TensorFlow (V.
- Full pipeline: stage not stated [TensorFlow]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Evidence: All models were constructed in Python 3 using Keras 2 with a Tensorflow backend.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### Diverging neural dynamics for syntactic structure building in naturalistic speaking and listening. (PNAS 2024)

- DOI: 10.1073/pnas.2310766121 | PMCID: PMC10945772 | PMID: 38442171
- Evidence: We used GPT-2 XL via the TensorFlow implementation provided by HuggingFace’s Transformers package ( 86 ).
- Full pipeline: differential/statistical testing [R v4.0.3, lme4] -> stage not stated [FreeSurfer, Nilearn, Python, TensorFlow, emmeans]

### Hormonal basis of sex differences in anesthetic sensitivity. (PNAS 2024)

- DOI: 10.1073/pnas.2312913120 | PMCID: PMC10801881 | PMID: 38190526
- Evidence: Automated cell detection was performed using a custom convolutional neural network through the Tensorflow python package.
- Full pipeline: machine learning [TensorFlow]

### Impossibility theorems for feature attribution. (PNAS 2024)

- DOI: 10.1073/pnas.2304406120 | PMCID: PMC10786278 | PMID: 38181057
- Evidence: We compute ∇ f exactly using TensorFlow ( 21 ).
- Full pipeline: stage not stated [TensorFlow]

### StratoLAMP: Label-free, multiplex digital loop-mediated isothermal amplification based on visual stratification of precipitate. (PNAS 2024)

- DOI: 10.1073/pnas.2314030121 | PMCID: PMC10786297 | PMID: 38165933
- Evidence: Mask R-CNN for TensorFlow 2 was adopted as the algorithm for droplet segmentation and classification, with ResNet-50 serving as the backbone.
- Full pipeline: stage not stated [ImageJ, TensorFlow]

### Adaptable microplastic classification using similarity learning on µFTIR spectra collected from µFTIR focal plane array imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2509745122 | PMCID: PMC12557549 | PMID: 41086209
- Version used: **2.10.1**
- Evidence: The similarity and CNN models used in this study were constructed in Python using a combination of Tensorflow (v 2.10.1) and the Tensorflow Similarity package (v 0.17.1).
- Full pipeline: stage not stated [Python, TensorFlow v2.10.1, scikit-learn v1.3.2]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Evidence: Molecular structural features, including the number of hydrogen bonds, distances of hydrogen bonds, SASA, and RSA, were integrated by the graph neural network (GNN) using the deep learning library TensorFlow ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### Mineral dissolution by dimeric complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2504109122 | PMCID: PMC12541406 | PMID: 41052339
- Evidence: S14 , and the model training was carried out using TensorFlow and Keras.
- Full pipeline: simulation/modelling [PLUMED] -> machine learning [Jupyter, Keras, Python, TensorFlow] -> stage not stated [ImageJ]

### The principles behind equivariant neural networks for physics and chemistry. (PNAS 2025)

- DOI: 10.1073/pnas.2415656122 | PMCID: PMC12541325 | PMID: 41052329
- Evidence: Modern neural network libraries such as PyTorch ( 10 ), TensorFlow ( 11 ) and JAX ( 12 ) operate similarly to compilers in the sense that they translate code written in a language like Python into a computation graph.
- Full pipeline: machine learning [PyTorch, TensorFlow]

### Sensory population activity reveals downstream confidence computations in the primate visual system. (PNAS 2025)

- DOI: 10.1073/pnas.2426441122 | PMCID: PMC12232640 | PMID: 40560622
- Evidence: We implemented networks within the TensorFlow framework using the AdamW optimizer with an objective to minimize binary cross-entropy.
- Full pipeline: stage not stated [Kilosort, TensorFlow]

### Multistage nucleation pathway in LiF molten salt mirrors the crystal-melt interface structure. (PNAS 2025)

- DOI: 10.1073/pnas.2425702122 | PMCID: PMC12207450 | PMID: 40540599
- Evidence: The training of the NN model was implemented in the TensorFlow package ( 99 ).
- Full pipeline: simulation/modelling [LAMMPS] -> machine learning [TensorFlow]

### Deep learning to quantify the pace of brain aging in relation to neurocognitive changes. (PNAS 2025)

- DOI: 10.1073/pnas.2413442122 | PMCID: PMC11912385 | PMID: 39993207
- Version used: **2.12.0**
- Evidence: The model was implemented using Python 3.8 and TensorFlow 2.12.0 on a computer with an Intel Core i7 processor, a clock speed of 2.2 GHz, 16 GB of RAM, and a 32 GB NVIDIA V100 graphical processing unit (GPU) for training and evaluation.
- Full pipeline: structure determination [FreeSurfer] -> machine learning [Python v3.8, TensorFlow v2.12.0]

### Control of flow behavior in complex fluids using automatic differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2403644122 | PMCID: PMC11874484 | PMID: 39964722
- Evidence: Yet, it is straightforward to implement AD in numerical solvers for fluid mechanics and can be carried out in open-source machine learning libraries such as JAX ( 10 ), TensorFlow ( 11 ) and PyTorch ( 12 ).
- Full pipeline: stage not stated [PyTorch, TensorFlow]

### Toward equitable major histocompatibility complex binding predictions. (PNAS 2025)

- DOI: 10.1073/pnas.2405106122 | PMCID: PMC11874272 | PMID: 39964728
- Evidence: Each MHCGlobe neural network was trained using RMSprop gradient descent optimization within the TensorFlow ( https://www.tensorflow.org/ ) training functions.
- Full pipeline: machine learning [TensorFlow, scikit-learn]

### Advancing forecasting capabilities: A contrastive learning model for forecasting tropical cyclone rapid intensification. (PNAS 2025)

- DOI: 10.1073/pnas.2415501122 | PMCID: PMC11789009 | PMID: 39835899
- Evidence: Tensorflow and Keras were used to build and train the RITCF-contrastive model.
- Full pipeline: stage not stated [Keras, TensorFlow, WRF]

### Random noise promotes slow heterogeneous synaptic dynamics important for robust working memory computation. (PNAS 2025)

- DOI: 10.1073/pnas.2316745122 | PMCID: PMC11760912 | PMID: 39819216
- Version used: **1.10.0**
- Evidence: All the models were implemented with TensorFlow 1.10.0 and trained on NVIDIA GPUs (Quadro P4000 and Quadro RTX 4000).
- Full pipeline: machine learning [TensorFlow v1.10.0]

### Decoding the elite soccer player's psychological profile. (PNAS 2025)

- DOI: 10.1073/pnas.2415126122 | PMCID: PMC11760505 | PMID: 39808661
- Evidence: The ANN architecture was constructed using the TensorFlow and Keras frameworks in Python.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Keras, Python, TensorFlow]

### Two-dimensional NMR from a single pulse: Reconstructing heteronuclear 2D spectra via off-resonance decoupling and deep neural networks. (PNAS 2026)

- DOI: 10.1073/pnas.2527937123 | PMCID: PMC13123836 | PMID: 42012953
- Evidence: Keras ( 56 ) and Tensorflow ( 57 ) were used to both train the DNN and to construct 1 H– 13 C correlation maps from the off-resonance datasets using the trained DNN.
- Full pipeline: machine learning [Keras, TensorFlow]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: Automated cell detection was performed by LCT using a custom convolutional neural network created with the Tensorflow python package (Google).
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: The Adam optimizer (learning rate 0.001) is used with deterministic behavior enforced by fixing Python, Numpy, TensorFlow and random-seed states.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **2.9.1**
- Evidence: The model architecture was implemented in TensorFlow (v2.9.1).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

