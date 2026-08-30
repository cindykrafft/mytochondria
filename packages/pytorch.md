# PyTorch

- **Category:** general
- **Papers in survey:** 129
- **Journals:** PNAS (72), Nature (53), Cell (3), Science (1)
- **Years:** 2021 (6), 2022 (16), 2023 (24), 2024 (26), 2025 (42), 2026 (15)
- **Versions named:** 2.0.1 (3), 1.12.1 (2), 2.2.0 (1), 2.1.1 (1), 2.1.2 (1), 2.21 (1), 1.13 (1), 1.12.0 (1), 1.7.1 (1), 2.0.0 (1)
- **Pipeline stages it appears in:** machine learning (55), simulation/modelling (5), normalisation (3), dimensionality reduction/clustering (2), differential/statistical testing (1), structure determination (1), registration (1), quantification (1)

## Papers

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: ...//rdrr.io/cran/pheatmap/ ggplot2 ( Wickham 2016 ) https://ggplot2.tidyverse.org Scanpy ( Wolf et al., 2018 ) https://scanpy.readthedocs.io/en/stable/ PyTorch N/A https://pytorch.org TotalVI ( Gayoso et al., 2021 ) https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html ScVI ( Lopez et al., 2018 ) https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html NicheNet ( Browaeys ...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Thyroid hormone remodels cortex to coordinate body-wide metabolism and exploration. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.041 | PMCID: PMC11455614 | PMID: 39178853
- Evidence: Parameters β , α , ζ , b were estimated using stochastic gradient descent optimization (learning rate of 0.1, 10000 iterations) and a negative log-likelihood loss function (custom Python code using PyTorch library).
- Full pipeline: read trimming [Seurat] -> alignment/mapping [Seurat] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, R v4.2.2] -> stage not stated [GSEA, PyTorch]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Version used: **2.5.1**
- Evidence: ...) Python https://www.python.org/ Bonsai (2.8.1) Bonsai Foundation https://bonsai-rx.org/ JAX (0.4.34) The JAX Authors https://docs.jax.dev/en/latest/ Pytorch (2.5.1) Pytorch Foundation https://pytorch.org/ Fiber localization based on allenCCF CortexLab https://github.com/cortex-lab/allenCCF Other Fibre Photometry System (FP3002) Neurophotometrics https://neurophotometrics.com/fp3002 Mono Fiber-opt...
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### RecA finds homologous DNA by reduced dimensionality search. (Nature 2021)

- DOI: 10.1038/s41586-021-03877-6 | PMCID: PMC8443446 | PMID: 34471288
- Version used: **1.7.1**
- Evidence: Pytorch 1.7.1 was used for the neural networks.
- Full pipeline: machine learning [PyTorch v1.7.1] -> visualisation [ImageJ] -> stage not stated [Python]

### A compute-in-memory chip based on resistive random-access memory. (Nature 2022)

- DOI: 10.1038/s41586-022-04992-8 | PMCID: PMC9385482 | PMID: 35978128
- Evidence: The model is trained using the PyTorch framework.
- Full pipeline: machine learning [Keras, PyTorch]

### Instantaneous tracking of earthquake growth with elastogravity signals. (Nature 2022)

- DOI: 10.1038/s41586-022-04672-7 | PMCID: PMC9177427 | PMID: 35545670
- Evidence: PEGSNet is built and trained using PyTorch 55 .
- Full pipeline: alignment/mapping [Matplotlib] -> machine learning [PyTorch] -> visualisation [Matplotlib]

### Deep physical neural networks trained with backpropagation. (Nature 2022)

- DOI: 10.1038/s41586-021-04223-6 | PMCID: PMC8791835 | PMID: 35082422
- Evidence: 2 – 4 , we used PAT to enable us to perform backpropagation on the physical apparatuses as automatic differentiation (autodiff) functions within PyTorch 54 (v1.6).
- Full pipeline: stage not stated [PyTorch]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Evidence: Gradients were estimated automatically using pytorch, and source code for our standard registration pipelines is available online at https://github.com/twardlab/emlddmm .
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Evidence: The models were implemented with Pytorch 76 and trained for ten epochs with the Adam optimizer, with a learning rate of 0.001.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### State estimation of a physical system with unknown governing equations. (Nature 2023)

- DOI: 10.1038/s41586-023-06574-8 | PMCID: PMC10567554 | PMID: 37821594
- Evidence: This is very similar to the batch-normalization 56 implementation provided in PyTorch 41 .
- Full pipeline: normalisation [PyTorch]

### Flexible circuit mechanisms for context-dependent song sequencing. (Nature 2023)

- DOI: 10.1038/s41586-023-06632-1 | PMCID: PMC10600009 | PMID: 37821705
- Evidence: The model was constructed and trained using the PyTorch library 54 .
- Full pipeline: differential/statistical testing [Brian2] -> simulation/modelling [Brian2] -> machine learning [CaImAn, PyTorch] -> stage not stated [Python v2.7, SLEAP]

### Ultra-fast deep-learned CNS tumour classification during surgery. (Nature 2023)

- DOI: 10.1038/s41586-023-06615-2 | PMCID: PMC10600004 | PMID: 37821699
- Evidence: For this purpose we use the L-BFGS algorithm implemented in PyTorch with learning rate 0.01 and a maximum of 500 iterations.
- Full pipeline: stage not stated [PyTorch, R]

### Cingulate dynamics track depression recovery with deep brain stimulation. (Nature 2023)

- DOI: 10.1038/s41586-023-06541-3 | PMCID: PMC10550829 | PMID: 37730990
- Evidence: LFP classification and inferring SDC Neural network models were used to classify LFP features using PyTorch 55 (v.1.11.0).
- Full pipeline: machine learning [PyTorch, scikit-learn v1.1.1] -> stage not stated [AFNI, FSL, Python v3.6]

### A foundation model for generalizable disease detection from retinal images. (Nature 2023)

- DOI: 10.1038/s41586-023-06555-x | PMCID: PMC10550819 | PMID: 37704728
- Evidence: Code availability The code used to train, fine-tune and evaluate RETFound from Y.Z. is available at https://github.com/rmaphoh/RETFound_MAE , which is based on PyTorch.
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.19.5, SciPy v1.5.4, seaborn v0.12.0] -> stage not stated [Keras, PyTorch]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Version used: **1.12.0**
- Evidence: We trained a neural network using PyTorch (v.1.12.0) 49 with these 68 moments as input, two linear hidden layers of size 32, a sigmoid output layer with a size of ten and with contrastive loss to reduce the output distance between equivalent pairs of central residues and increase the distance between non-equivalent pairs in a training set.
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### An analog-AI chip for energy-efficient speech recognition and transcription. (Nature 2023)

- DOI: 10.1038/s41586-023-06337-5 | PMCID: PMC10447234 | PMID: 37612392
- Evidence: For model size: B, 1 billion; M, 1 million. b , Inference models are trained using popular frameworks such as PyTorch or TensorFlow.
- Full pipeline: machine learning [PyTorch, TensorFlow]

### Skilful nowcasting of extreme precipitation with NowcastNet. (Nature 2023)

- DOI: 10.1038/s41586-023-06184-4 | PMCID: PMC10356617 | PMID: 37407824
- Evidence: Code availability We rely on PyTorch ( https://pytorch.org ) for deep model training and cartopy ( https://scitools.org.uk/cartopy ) for geospatial data processing.
- Full pipeline: machine learning [PyTorch]

### Accurate medium-range global weather forecasting with 3D neural networks. (Nature 2023)

- DOI: 10.1038/s41586-023-06185-3 | PMCID: PMC10356604 | PMID: 37407823
- Evidence: Code availability The code base of Pangu-Weather was established on PyTorch, a Python-based library for deep learning.
- Full pipeline: machine learning [PyTorch] -> visualisation [Matplotlib] -> stage not stated [NumPy, xarray]

### Learnable latent embeddings for joint behavioural and neural analysis. (Nature 2023)

- DOI: 10.1038/s41586-023-06031-6 | PMCID: PMC10172131 | PMID: 37138088
- Evidence: CEBRA API and example usage The Python implementation of CEBRA is written in PyTorch 55 and NumPy 56 and provides an application programming interface (API) that is fully compatible with scikit-learn 57 , a package commonly used for machine learning.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [NumPy, PyTorch, scikit-learn]

### Automated real-world data integration improves cancer outcome prediction. (Nature 2024)

- DOI: 10.1038/s41586-024-08167-5 | PMCID: PMC11655358 | PMID: 39506116
- Evidence: We used the PyTorch 46 implementation of RoBERTa and pretrained model weights from the HuggingFace library and model hub 47 .
- Full pipeline: machine learning [PyTorch]

### A broadband hyperspectral image sensor with high spatio-temporal resolution. (Nature 2024)

- DOI: 10.1038/s41586-024-08109-1 | PMCID: PMC11541218 | PMID: 39506154
- Evidence: We trained the model on the Pytorch platform with a single NVIDIA RTX 4090 GPU.
- Full pipeline: machine learning [PyTorch]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Evidence: Methods Training Malinois, a model of MPRA activity of CREs To enable systematic evaluation of parameters governing data preprocessing, model architecture and training, we developed tools for limited automatic machine learning in PyTorch ( https://github.com/sjgosai/boda2 ).
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### Connectome-constrained networks predict neural activity across the fly visual system. (Nature 2024)

- DOI: 10.1038/s41586-024-07939-3 | PMCID: PMC11525180 | PMID: 39261740
- Evidence: To model the hexagonal arrangement of photoreceptors in the fly retina, we developed a hexagonal convolutional neural network (CNN) in the widely used deep learning framework PyTorch 21 (ignoring neuronal superposition 70 ), which we used for simulation and optimization of the model.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [UMAP, scikit-learn] -> simulation/modelling [PyTorch] -> machine learning [PyTorch]

### Multi-pass, single-molecule nanopore reading of long protein strands. (Nature 2024)

- DOI: 10.1038/s41586-024-07935-7 | PMCID: PMC11410661 | PMID: 39261738
- Evidence: VR classification We used scikit-learn to develop and test classical machine learning models and Pytorch to develop and test convolutional neural-network models.
- Full pipeline: quantification [ImageJ] -> stage not stated [PyTorch, SciPy, scikit-learn]

### Brain-wide dynamics linking sensation to action during decision-making. (Nature 2024)

- DOI: 10.1038/s41586-024-07908-w | PMCID: PMC11499283 | PMID: 39261727
- Evidence: The outlier detection model was implemented using custom Python software using the NumPy, SciPy, and PyTorch libraries.
- Full pipeline: machine learning [DeepLabCut] -> stage not stated [Kilosort v2.0, NumPy, PyTorch, SciPy]

### Dopamine-mediated interactions between short- and long-term memory dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07819-w | PMCID: PMC11525173 | PMID: 39038490
- Evidence: 4h ), we used PyTorch 55 (v.1.7.1; www.pytorch.org ) to train computational classifiers that identified odours on the basis of patterns of activity in PPL1-DAN or MBON neural populations.
- Full pipeline: machine learning [PyTorch]

### Endoplasmic reticulum-plasma membrane contact gradients direct cell migration. (Nature 2024)

- DOI: 10.1038/s41586-024-07527-5 | PMCID: PMC11236710 | PMID: 38867038
- Evidence: Initial segmentations were manually performed on a few tomographic slices in DragonFly (v.2022.2) for training a neural network in DragonFly (v.2022.2) 55 or by using Tardis-Pytorch 56 on the deconvolved tomograms.
- Full pipeline: machine learning [PyTorch]

### A multimodal generative AI copilot for human pathology. (Nature 2024)

- DOI: 10.1038/s41586-024-07618-3 | PMCID: PMC11464372 | PMID: 38866050
- Version used: **2.0.1**
- Evidence: For all model training, we used eight 80 GB NVIDIA A100 GPUs configured for multi-GPU training using the popular open-source deep learning framework PyTorch (v.2.0.1, CUDA 11.8).
- Full pipeline: machine learning [PyTorch v2.0.1] -> stage not stated [Matplotlib v3.7.1, QuPath, seaborn v0.12.2]

### Low-latency automotive vision with event cameras. (Nature 2024)

- DOI: 10.1038/s41586-024-07409-w | PMCID: PMC11136662 | PMID: 38811712
- Evidence: We use the PyTorch Geometric 86 library, which is optimized for batch processing, and thus introduces data handling overhead.
- Full pipeline: stage not stated [PyTorch]

### Large-scale single-neuron speech sound encoding across the depth of human cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06839-2 | PMCID: PMC10866713 | PMID: 38093008
- Evidence: We used automatic differentiation in PyTorch 67 to compute this gradient for each of the jackknifed models on the test stimuli.
- Full pipeline: registration [Kilosort v2.5] -> stage not stated [MNE-Python v0.22.0, PyTorch]

### A probabilistic histological atlas of the human brain for MRI segmentation. (Nature 2025)

- DOI: 10.1038/s41586-025-09708-2 | PMCID: PMC12711564 | PMID: 41193801
- Evidence: The framework is implemented using the PyTorch package, which enables it to run on graphics processing units and curbs segmentation run times to about half an hour per hemisphere.
- Full pipeline: stage not stated [FSL, FreeSurfer v7.0, PyTorch]

### Learning the natural history of human disease with generative transformers. (Nature 2025)

- DOI: 10.1038/s41586-025-09529-3 | PMCID: PMC12589094 | PMID: 40963019
- Evidence: The transformer model is an encoder model based on the standard implementation provided in Python:pytorch (TransformerEncoder, TransformerEncoderLayer) with a context length of 128 tokens, an embedding size of 128, 2 multi-head attention blocks and a total of 2 sub-encoder layers, and the otherwise default parameters were used.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Jupyter, PyTorch, Python, scikit-learn]

### DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning. (Nature 2025)

- DOI: 10.1038/s41586-025-09422-z | PMCID: PMC12443585 | PMID: 40962978
- Evidence: Neural networks were developed with PyTorch 35 and the distributed framework is based on our internal framework HAI-LLM ( https://www.high-flyer.cn/en/blog/hai-llm ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [Matplotlib v3.5.2, NumPy v1.23.1]

### Analog optical computer for AI inference and combinatorial optimization. (Nature 2025)

- DOI: 10.1038/s41586-025-09430-z | PMCID: PMC12422976 | PMID: 40903585
- Evidence: The AOC-DT is implemented as a Pytorch module with the weight matrix W and bias terms b , as well as the gain β as trainable parameters.
- Full pipeline: stage not stated [PyTorch]

### Optical generative models. (Nature 2025)

- DOI: 10.1038/s41586-025-09446-5 | PMCID: PMC12390839 | PMID: 40866675
- Version used: **2.21**
- Evidence: All the models were trained and tested using PyTorch 2.21 57 with a single NVIDIA RTX 4090 graphics processing unit.
- Full pipeline: machine learning [PyTorch v2.21]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Evidence: This model was coded in PyTorch 70 and the maximum-likelihood solution was found running the Adam optimizer for 10,000 iterations and checking for convergence.
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Discovering cognitive strategies with tiny recurrent neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09142-4 | PMCID: PMC12390849 | PMID: 40604278
- Version used: **1.13**
- Evidence: Methods All data were analysed using Python 3.9 and PyTorch 1.13.
- Full pipeline: stage not stated [PyTorch v1.13, Python v3.9]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Version used: **1.12.1**
- Evidence: Network architecture and training We implemented deep-learning pipelines with Pytorch v.1.12.1 ( https://pytorch.org ) and used the Gunpowder framework v.1.2.2 ( https://github.com/funkelab/gunpowder ) to implement our data loading, augmentation, training and prediction pipeline that conveniently allowed processing of big datasets.
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Striatum supports fast learning but not memory recall. (Nature 2025)

- DOI: 10.1038/s41586-025-08969-1 | PMCID: PMC12244412 | PMID: 40335692
- Evidence: We used custom code wrapping PyTorch in Python to regress the behavioural condition on the input matrix.
- Full pipeline: stage not stated [DeepLabCut, PyTorch, Python, scikit-learn]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: All three layers were trained for 10 epochs, a batch size of 512, the categorical cross entropy loss function, and the Adam optimizer in PyTorch.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Evidence: The full loss function L is a weighted sum of the reconstruction and triplet losses: L = R + λ triplet T x + T y Model training Model parameters were trained with standard neural network learning procedures provided by Pytorch 74 v.2.0.1, based on backpropagation using the Adam stochastic gradient descent method 75 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### World and Human Action Models towards gameplay ideation. (Nature 2025)

- DOI: 10.1038/s41586-025-08600-3 | PMCID: PMC11839478 | PMID: 39972228
- Evidence: Modelling choices and hyperparameters Training We used PyTorch Lightning 66 and FSDP 67 for training.
- Full pipeline: machine learning [NumPy, PyTorch]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: The GET implementation is based on the PyTorch framework.
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Timely TGFβ signalling inhibition induces notochord. (Nature 2025)

- DOI: 10.1038/s41586-024-08332-w | PMCID: PMC11735409 | PMID: 39695233
- Evidence: 86 ), a pytorch-based computer vision library.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> stage not stated [PyTorch, R, Scanpy, scDblFinder]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: We trained a GNN model using PyTorch Geometric 108 to predict neighbourhood ageing from the features of a local cell graph.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Foundation models for fast, label-free detection of glioma infiltration. (Nature 2025)

- DOI: 10.1038/s41586-024-08169-3 | PMCID: PMC11711092 | PMID: 39537921
- Evidence: Our models were implemented in PyTorch Lightning (v.1.8.4).
- Full pipeline: machine learning [scikit-learn v1.4.1] -> stage not stated [PyTorch, R v3.6.3]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Version used: **2.2.0**
- Evidence: Liquid EcoTyper training The Liquid EcoTyper model was implemented and trained using PyTorch 2.2.0.
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Composable neural emulators accelerate thermoelectric generator design. (Nature 2026)

- DOI: 10.1038/s41586-026-10223-1 | PMCID: PMC13083250 | PMID: 41986625
- Evidence: All algorithms were implemented in Python (version 3.10) using the PyTorch module.
- Full pipeline: stage not stated [PyTorch, Python v3.10]

### General scales unlock AI evaluation with explanatory and predictive power. (Nature 2026)

- DOI: 10.1038/s41586-026-10303-2 | PMCID: PMC13043289 | PMID: 41922702
- Evidence: For implementation, the RF models were trained using the scikit-learn library 88 , whereas the fine-tuned LLaMA-3.1-8B was trained on the Transformers library 89 using the PyTorch backend running on Python 3.11.
- Full pipeline: machine learning [PyTorch, Python v3.11, scikit-learn]

### Rapid concerted switching of the neural code in the inferotemporal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10267-3 | PMCID: PMC13148990 | PMID: 41882367
- Evidence: To build a 60-dimension face feature space using a ResNet-50 model trained on the VGGFace2 dataset 36 , we used a PyTorch implementation of the VGGFace2 model available at https://github.com/cydonia999/VGGFace2-pytorch .
- Full pipeline: machine learning [PyTorch] -> stage not stated [FSL, FreeSurfer, Kilosort]

### Advancing operational global aerosol forecasting with machine learning. (Nature 2026)

- DOI: 10.1038/s41586-026-10234-y | PMCID: PMC12999505 | PMID: 41781617
- Evidence: The AI-GAMFS framework was implemented on the PyTorch platform.
- Full pipeline: stage not stated [PyTorch]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Sectional 3D image decompression for viewing, deep learning-based cell detection and classification, CMD-based cell population analysis and statistical analysis were implemented in Python (v.3.10 and v.3.12), with several open-source libraries, including NumPy, pandas, matplotlib, seaborn, scikit-learn, statsmodels, PyTorch, torchvision, albumentations, OpenCV, timm and ONNX Runtime.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Regulatory grammar in human promoters uncovered by MPRA-based deep learning. (Nature 2026)

- DOI: 10.1038/s41586-025-10093-z | PMCID: PMC13017510 | PMID: 41639451
- Version used: **2.1.1**
- Evidence: The model was implemented in PyTorch (v.2.1.1).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1] -> stage not stated [NumPy, PyTorch v2.1.1]

### Scalable and multiplexed recorders of gene regulation dynamics across weeks. (Nature 2026)

- DOI: 10.1038/s41586-026-10156-9 | PMCID: PMC13102694 | PMID: 41588170
- Evidence: For fibre segmentation, we used the U-Net backbone architecture from the PyTorch Connectomics library 55 to obtain instance segmentations from the structure monomer channel.
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [UMAP, scikit-image] -> simulation/modelling [AlphaFold, GROMACS v2021.1] -> stage not stated [ImageJ, PyTorch, napari]

### Language model-guided anticipation and discovery of mammalian metabolites. (Nature 2026)

- DOI: 10.1038/s41586-025-09969-x | PMCID: PMC12960238 | PMID: 41535467
- Evidence: LSTMs were implemented in PyTorch, adapting code from the REINVENT package 74 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [scikit-learn] -> stage not stated [PyTorch, RDKit]

### Comprehensive echocardiogram evaluation with view primed vision language AI. (Nature 2026)

- DOI: 10.1038/s41586-025-09850-x | PMCID: PMC12935550 | PMID: 41219498
- Version used: **2.1.2**
- Evidence: Computing hardware and software We used Python (v3.8.13), PyTorch (v2.1.2, CUDA 12.1; https://pytorch.org ) and TorchVision (v0.17.0) for all experiments and analyses in the study.
- Full pipeline: dimensionality reduction/clustering [SciPy v1.12.0] -> differential/statistical testing [SciPy v1.12.0, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [PyTorch v2.1.2]

### Computational prediction of the effect of amino acid changes on the binding affinity between SARS-CoV-2 spike RBD and human ACE2. (PNAS 2021)

- DOI: 10.1073/pnas.2106480118 | PMCID: PMC8594574 | PMID: 34588290
- Evidence: All codes were developed in Python using the PyTorch library.
- Full pipeline: stage not stated [PyTorch, Python]

### Exploring deep neural networks via layer-peeled model: Minority collapse in imbalanced training. (PNAS 2021)

- DOI: 10.1073/pnas.2103091118 | PMCID: PMC8639364 | PMID: 34675075
- Evidence: Another example is to take g 1 ( x ) = ( 1 − x ) q and g 2 ( x ) = x q for q > 1 , which can be implemented in most deep-learning libraries, such as PyTorch ( 49 ).
- Full pipeline: stage not stated [PyTorch]

### A self-exciting point process to study multicellular spatial signaling patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2026123118 | PMCID: PMC8364135 | PMID: 34362843
- Evidence: We maximize this likelihood using automatic differentiation from PyTorch ( 36 ).
- Full pipeline: stage not stated [PyTorch, TrackMate]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Version used: **1.2.0**
- Evidence: BABEL was implemented using the PyTorch (version 1.2.0) and Skorch (version 0.7.0) Python libraries.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Laboratory earthquake forecasting: A machine learning competition. (PNAS 2021)

- DOI: 10.1073/pnas.2011362118 | PMCID: PMC7865129 | PMID: 33495346
- Evidence: The features were used in a simple feed-forward neural net in the deep learning library pytorch.
- Full pipeline: machine learning [PyTorch]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Evidence: The Maximum Likelihood Estimation process was done using “PyTorch”.
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### Learning the relationship between nanoscale chemical patterning and hydrophobicity. (PNAS 2022)

- DOI: 10.1073/pnas.2200018119 | PMCID: PMC9860318 | PMID: 36409904
- Evidence: By exploring a number of fully connected feed-forward architectures, trained in PyTorch ( 53 ), we find that an ANN with a single hidden layer and 48 neurons possesses the lowest cross-validation error.
- Full pipeline: machine learning [PyTorch]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### Neural representational geometry underlies few-shot concept learning. (PNAS 2022)

- DOI: 10.1073/pnas.2200800119 | PMCID: PMC9618072 | PMID: 36251997
- Evidence: All DNNs studied throughout this work are standard architectures available in the PyTorch library ( 69 ) and are pretrained on the ImageNet1k dataset.
- Full pipeline: machine learning [PyTorch]

### Deep neural networks constrained by neural mass models improve electrophysiological source imaging of spatiotemporal brain dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2201128119 | PMCID: PMC9351497 | PMID: 35881787
- Evidence: The whole network was implemented in PyTorch and trained on one NVIDIA Telsa V100 graphics processing unit ( 73 ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [FreeSurfer, MNE-Python v0.22.0, Python v0.22.0]

### Deep learning of dynamically responsive chemical Hamiltonians with semiempirical quantum mechanics. (PNAS 2022)

- DOI: 10.1073/pnas.2120333119 | PMCID: PMC9271210 | PMID: 35776544
- Evidence: The SEQM module used here is implemented in the PYSEQM software package that utilizes Pytorch to interface with other ML packages ( 43 , 44 ).
- Full pipeline: simulation/modelling [TensorFlow] -> machine learning [TensorFlow] -> stage not stated [PyTorch, RDKit, SciPy]

### Interpretable modeling of genotype-phenotype landscapes with state-of-the-art predictive power. (PNAS 2022)

- DOI: 10.1073/pnas.2114021119 | PMCID: PMC9245639 | PMID: 35733251
- Evidence: We implemented LANTERN with the automatic differentiation library pytorch ( 53 ), with GP components of the model relying on gpytorch ( 54 ).
- Full pipeline: stage not stated [PyTorch]

### Simple, fast, and flexible framework for matrix completion with infinite width neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2115064119 | PMCID: PMC9169779 | PMID: 35412891
- Evidence: For training neural networks, we use the PyTorch library ( 50 ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, scikit-image]

### Implicit data crimes: Machine learning bias arising from misuse of public data. (PNAS 2022)

- DOI: 10.1073/pnas.2117203119 | PMCID: PMC9060447 | PMID: 35312366
- Evidence: We implemented MoDL using PyTorch ( 69 ).
- Full pipeline: stage not stated [PyTorch, Python]

### Intersecting kinematic encoding and readout of intention in autism. (PNAS 2022)

- DOI: 10.1073/pnas.2114648119 | PMCID: PMC8812545 | PMID: 35101921
- Evidence: The kinematic encoding and readout models were implemented using Python/PyTorch ( 36 ).
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [PyTorch, R, lme4]

### Ultrafast end-to-end protein structure prediction enables high-throughput exploration of uncharacterized proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2113348119 | PMCID: PMC8795500 | PMID: 35074909
- Evidence: Together with the dynamic computational graph construction used by PyTorch, this enables us to train the network with the iterations included.
- Full pipeline: stage not stated [AlphaFold, HMMER, PyTorch, RoseTTAFold]

### Surrogate gradients for analog neuromorphic computing. (PNAS 2022)

- DOI: 10.1073/pnas.2109194119 | PMCID: PMC8794842 | PMID: 35042792
- Evidence: Materials and Methods Software Environment Our training framework was based on PyTorch’s autodifferentiation library ( 29 ).
- Full pipeline: machine learning [PyTorch]

### Free energies at QM accuracy from force fields via multimap targeted estimation. (PNAS 2023)

- DOI: 10.1073/pnas.2304308120 | PMCID: PMC10655219 | PMID: 37931103
- Evidence: The code relies on PyTorch ( 89 ) to implement and train the normalizing flow maps and on ASE ( 90 ) to obtain potential energies and forces from external molecular simulation engines.
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [PLUMED v2.8.1, PyTorch]

### Gaming self-consistent field theory: Generative block polymer phase discovery. (PNAS 2023)

- DOI: 10.1073/pnas.2308698120 | PMCID: PMC10636330 | PMID: 37922326
- Evidence: The training of GAN was conducted using the open-source software package PyTorch ( 55 ).
- Full pipeline: machine learning [PyTorch]

### Prediction and design of protease enzyme specificity using a structure-aware graph convolutional network. (PNAS 2023)

- DOI: 10.1073/pnas.2303590120 | PMCID: PMC10523478 | PMID: 37729196
- Evidence: PGCN is trained on training datasets using PyTorch, and tested on validation sets for hyperparameter tuning.
- Full pipeline: differential/statistical testing [TensorFlow v1.13.1, scikit-learn v0.20.1] -> machine learning [PyTorch]

### Convergence in sympatric swallowtail butterflies reveals ecological interactions as a key driver of worldwide trait diversification. (PNAS 2023)

- DOI: 10.1073/pnas.2303060120 | PMCID: PMC10500277 | PMID: 37669385
- Evidence: The method was implemented in Python, mainly using the Pytorch library for machine learning, and the Lightly library for SimCLR-related augmentations, backbone, and loss function.
- Full pipeline: stage not stated [PyTorch, Python, R]

### A law of data separation in deep learning. (PNAS 2023)

- DOI: 10.1073/pnas.2221704120 | PMCID: PMC10483613 | PMID: 37639604
- Evidence: Footnotes This article is a PNAS Direct Submission. * For clarification, D 0 is calculated from the raw data, and D 1 is calculated from the data that have passed through the first layer but not the second layer. † See the architecture in https://github.com/kuangliu/pytorch-cifar/tree/master/models .
- Full pipeline: stage not stated [PyTorch]

### Lagrangian large eddy simulations via physics-informed machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2213638120 | PMCID: PMC10450849 | PMID: 37585463
- Evidence: The smoothing kernel NN [ 7 ] is constructed using PyTorch ( 66 ) open-source ML library.
- Full pipeline: stage not stated [PyTorch]

### NMDA-driven dendritic modulation enables multitask representation learning in hierarchical sensory processing pathways. (PNAS 2023)

- DOI: 10.1073/pnas.2300558120 | PMCID: PMC10410730 | PMID: 37523562
- Evidence: With a custom PyTorch ( 91 ) data sampler, we then ensured that the data for multitask learning was balanced across tasks and task-classes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [PyTorch]

### Modeling and design of heterogeneous hierarchical bioinspired spider web structures using deep learning and additive manufacturing. (PNAS 2023)

- DOI: 10.1073/pnas.2305273120 | PMCID: PMC10401013 | PMID: 37487072
- Evidence: All code ( 89 ) is developed in PyTorch ( 90 ).
- Full pipeline: stage not stated [PyTorch]

### Urban visual intelligence: Uncovering hidden city profiles with street view images. (PNAS 2023)

- DOI: 10.1073/pnas.2220417120 | PMCID: PMC10319000 | PMID: 37364096
- Evidence: The model is available at https://github.com/CSAILVision/semantic-segmentation-pytorch.
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [PyTorch]

### Contrastive learning in protein language space predicts interactions between drugs and protein targets. (PNAS 2023)

- DOI: 10.1073/pnas.2220778120 | PMCID: PMC10268324 | PMID: 37289807
- Version used: **1.11**
- Evidence: The model was implemented in PyTorch version 1.11.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [PyTorch v1.11, STRING db]

### Neural parameter calibration for large-scale multiagent models. (PNAS 2023)

- DOI: 10.1073/pnas.2216415120 | PMCID: PMC9963791 | PMID: 36763529
- Evidence: The neural core is implemented using pytorch § .
- Full pipeline: stage not stated [PyTorch]

### AI-boosted and motion-corrected, wireless near-infrared sensing system for continuously monitoring laryngeal muscles. (PNAS 2024)

- DOI: 10.1073/pnas.2410750121 | PMCID: PMC11665861 | PMID: 39652765
- Evidence: All the above-mentioned neural networks are built with the PyTorch package (version 2.0.0, based on CUDA 12.1 platform).
- Full pipeline: machine learning [PyTorch, Python v3.10.11]

### Automated determination of transport and depositional environments in sand and sandstones. (PNAS 2024)

- DOI: 10.1073/pnas.2407655121 | PMCID: PMC11459152 | PMID: 39284038
- Evidence: The model was trained using transfer learning of a pretrained ResNet-50 model ( 28 ) using Pytorch ( 59 ).
- Full pipeline: machine learning [PyTorch]

### Deep learning models map rapid plant species changes from citizen science and remote sensing data. (PNAS 2024)

- DOI: 10.1073/pnas.2318296121 | PMCID: PMC11406280 | PMID: 39236239
- Evidence: For comparison to previous work using CNNs to rank species presence from remote sensing imagery, we trained an Inception V3 architecture ( 34 ) ( Inception V3, SI Appendix , SM 3.2.4 and Table S4 ) with softmax cross-entropy loss using the official architecture implementation and initial weights from pytorch and using both the standard and auxiliary loss during training.
- Full pipeline: machine learning [PyTorch] -> stage not stated [NumPy, R]

### Riemannian geometry for efficient analysis of protein dynamics data. (PNAS 2024)

- DOI: 10.1073/pnas.2318951121 | PMCID: PMC11331106 | PMID: 39121160
- Evidence: Finally, all of the experiments are implemented using PyTorch in Python 3.8 and run on a 2 GHz Quad-Core Intel Core i5 with 16GB RAM.
- Full pipeline: stage not stated [PyTorch, Python v3.8]

### An all-atom protein generative model. (PNAS 2024)

- DOI: 10.1073/pnas.2311500121 | PMCID: PMC11228509 | PMID: 38916999
- Evidence: Supplementary Material Appendix 01 (PDF) Acknowledgments We would like to acknowledge Phil Wang for generous sharing of many useful PyTorch modules, other open-source code bases, Kilian Cavalotti for help with the Sherlock computing cluster, Christian Choe for providing monobody models, and Jiaming Song, Simon Kohl, Russ Bates, Rob Fergus, Jonas Adler, Sander Dieleman, Daniel Richman, Vishnu Saruk...
- Full pipeline: dimensionality reduction/clustering [PyTorch] -> machine learning [AlphaFold] -> stage not stated [PyMOL]

### Democratizing protein language models with parameter-efficient fine-tuning. (PNAS 2024)

- DOI: 10.1073/pnas.2405840121 | PMCID: PMC11214071 | PMID: 38900798
- Version used: **2.0.1**
- Evidence: All PEFT and FT models were implemented in PyTorch (v.2.0.1), using the HuggingFace implementations of ESM2 from the transformers package (v.4.32.1) and LoRA from the peft package (v.0.5.0).
- Full pipeline: stage not stated [AlphaFold, PyTorch v2.0.1, RoseTTAFold, scikit-learn v1.2.0]

### Optimal reaching subject to computational and physical constraints reveals structure of the sensorimotor control system. (PNAS 2024)

- DOI: 10.1073/pnas.2319313121 | PMCID: PMC10998569 | PMID: 38551834
- Evidence: The networks were constructed using the PyTorch framework and trained for 1,000 epochs with the Adam optimizer at a learning rate of 5 × 10 − 4 ( 43 ).
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> machine learning [PyTorch]

### Single-sequence protein structure prediction by integrating protein language models. (PNAS 2024)

- DOI: 10.1073/pnas.2308788121 | PMCID: PMC10990103 | PMID: 38507445
- Evidence: The model was implemented using PyTorch ( 21 ), and its distributed training on multi-GPUs was based on PyTorch Lightning ( 22 ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [AlphaFold]

### Increased methane emissions from oil and gas following the Soviet Union's collapse. (PNAS 2024)

- DOI: 10.1073/pnas.2314600121 | PMCID: PMC10963001 | PMID: 38470920
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability The deep learning model was implemented using PyTorch ( https://pytorch.org/ ).
- Full pipeline: machine learning [PyTorch]

### Machine learning to predict continuous protein properties from binary cell sorting data and map unseen sequence space. (PNAS 2024)

- DOI: 10.1073/pnas.2311726121 | PMCID: PMC10945751 | PMID: 38451939
- Evidence: PyTorch ( https://pytorch.org/ ) was used to train neural network models.
- Full pipeline: normalisation [scikit-learn] -> machine learning [PyTorch] -> stage not stated [MACS2, NumPy]

### Context-dependent design of induced-fit enzymes using deep learning generates well-expressed, thermally stable and active enzymes. (PNAS 2024)

- DOI: 10.1073/pnas.2313809121 | PMCID: PMC10945820 | PMID: 38437538
- Evidence: The implementation of the network was done in PyTorch ( 32 ) and PyTorch-Geometric ( 33 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyTorch]

### Homophily modulates double descent generalization in graph convolution networks. (PNAS 2024)

- DOI: 10.1073/pnas.2309504121 | PMCID: PMC10895367 | PMID: 38346190
- Evidence: This last model is used in the pytorch-geometric node classification tutorial. ‡ Fig.
- Full pipeline: stage not stated [PyTorch]

### Manifold fitting with CycleGAN. (PNAS 2024)

- DOI: 10.1073/pnas.2311436121 | PMCID: PMC10835067 | PMID: 38266050
- Evidence: Data, Materials, and Software Availability The PyTorch-based implementation, encompassing generators, discriminators, and manifold fitting sub-module of the model, along with the requisite code for data generation and comparison in simulations, is accessible via https://github.com/zhigang-yao/MFCGAN ( 37 ).
- Full pipeline: simulation/modelling [PyTorch]

### Accurate estimation of biological age and its application in disease prediction using a multimodal image Transformer system. (PNAS 2024)

- DOI: 10.1073/pnas.2308812120 | PMCID: PMC10801873 | PMID: 38190540
- Evidence: We used eight Telsa-A100 GPUs and trained the model for 500 epochs using Pytorch ( 47 ) library.
- Full pipeline: machine learning [PyTorch]

### Data-driven enhanced sampling of mechanistic pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2517169122 | PMCID: PMC12704791 | PMID: 41343671
- Evidence: All machine learning CVs were trained using the mlcolvar ( 53 ) module using PyTorch.
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.11.0] -> machine learning [PyTorch]

### Light-field deep learning enables high-throughput, scattering-mitigated calcium imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2510337122 | PMCID: PMC12685042 | PMID: 41289378
- Evidence: RL deconvolution was performed in Python 3 using PyTorch.
- Full pipeline: visualisation [napari] -> stage not stated [PyTorch, Python]

### Descattering and image restoration with a transformer-based neural network in deep tissue imaging. (PNAS 2025)

- DOI: 10.1073/pnas.2503576122 | PMCID: PMC12582269 | PMID: 41118214
- Evidence: This framework is implemented with Pytorch ( 57 ) version 1.9.0 and Python version 3.8.3 in the Microsoft Windows 10 operating system.
- Full pipeline: stage not stated [PyTorch, Python]

### From retinotopic to ordinal coding: Dissecting the cortical stages of visual word recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2507291122 | PMCID: PMC12582272 | PMID: 41118216
- Evidence: Pytorch libraries were used to train these networks with stochastic gradient descent on a categorical cross-entropy loss.
- Full pipeline: normalisation [Python] -> differential/statistical testing [Python] -> stage not stated [FSL, MNE-Python, PyTorch, SPM]

### The principles behind equivariant neural networks for physics and chemistry. (PNAS 2025)

- DOI: 10.1073/pnas.2415656122 | PMCID: PMC12541325 | PMID: 41052329
- Evidence: Modern neural network libraries such as PyTorch ( 10 ), TensorFlow ( 11 ) and JAX ( 12 ) operate similarly to compilers in the sense that they translate code written in a language like Python into a computation graph.
- Full pipeline: machine learning [PyTorch, TensorFlow]

### Manifold-constrained nucleus-level denoising diffusion model for structure-based drug design. (PNAS 2025)

- DOI: 10.1073/pnas.2415666122 | PMCID: PMC12541315 | PMID: 41052340
- Version used: **1.12.1**
- Evidence: All algorithms and models have been developed using Python 3.8.13, with PyTorch version 1.12.1 and PyTorch Geometric version 2.5.2, under CUDA 11.0.
- Full pipeline: simulation/modelling [AutoDock Vina] -> stage not stated [PyTorch v1.12.1, Python v3.8.13]

### STIM1 transmembrane helix dimerization captured by AI-guided transition path sampling. (PNAS 2025)

- DOI: 10.1073/pnas.2506516122 | PMCID: PMC12415195 | PMID: 40857319
- Evidence: Our neural network, implemented using pytorch ( 80 ), consisted of a pyramidal 5-layer Self-Normalizing Neural Network ( 81 ) in which the number of units per layer decreases from 77 in the input layer to 11 in the last, followed by a ResNet ( 82 , 83 ) consisting of 3 residual blocks, each with 4 layers and a width of 11 units per layer.
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [GROMACS v2020.6, MDAnalysis, MDTraj, NumPy, SciPy] -> machine learning [PyTorch]

### Efficient neural encoding as revealed by bilingualism. (PNAS 2025)

- DOI: 10.1073/pnas.2513768122 | PMCID: PMC12403110 | PMID: 40828024
- Evidence: We trained a neural network for speech recognition in a supervised manner, implemented in Python with the PyTorch package ( 58 ).
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [PyTorch, Python, scikit-learn]

### RNA polymerase III transcription-associated polyadenylation promotes the accumulation of noncoding retrotransposons during infection. (PNAS 2025)

- DOI: 10.1073/pnas.2507186122 | PMCID: PMC12358842 | PMID: 40768347
- Evidence: SAMBAR-Net is a binary CNN model implemented using PyTorch ( 98 ) to discriminate between expressed (RPKM≥10) from unexpressed (RPKM=0) B2 SINE genes in NIH3T3 cells using a one-hot encoded format as its input.
- Full pipeline: alignment/mapping [MACS2] -> quantification [PyTorch, RepeatMasker]

### Multiarea processing in body patches of the primate inferotemporal cortex implements inverse graphics. (PNAS 2025)

- DOI: 10.1073/pnas.2420287122 | PMCID: PMC12280979 | PMID: 40627399
- Evidence: All model training and testing were developed and performed in PyTorch ( 70 ).
- Full pipeline: machine learning [PyTorch]

### SpecTf: Transformers enable data-driven imaging spectroscopy cloud detection. (PNAS 2025)

- DOI: 10.1073/pnas.2502903122 | PMCID: PMC12260531 | PMID: 40608670
- Evidence: Second, the ANN model was implemented using the Pytorch library ( 30 ).
- Full pipeline: stage not stated [PyTorch, XGBoost]

### Generative prediction of causal gene sets responsible for complex traits. (PNAS 2025)

- DOI: 10.1073/pnas.2415071122 | PMCID: PMC12184495 | PMID: 40504147
- Evidence: We employ a conditional variational autoencoder in PyTorch, which is tailored for the analysis of genomic data and leverages class labels (baseline or variant) to impart enhanced interpretability and classification precision.
- Full pipeline: machine learning [SciPy] -> stage not stated [Enrichr, PyTorch]

### Amortized template matching of molecular conformations from cryoelectron microscopy images using simulation-based inference. (PNAS 2025)

- DOI: 10.1073/pnas.2420158122 | PMCID: PMC12168013 | PMID: 40465628
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability The code is available at GitHub ( https://github.com/flatironinstitute/cryoSBI ) and is based on LAMPE ( 63 ), a PyTorch implementation for simulation-based inference.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [PyTorch] -> stage not stated [cryoDRGN]

### Reversible molecular simulation for training classical and machine-learning force fields. (PNAS 2025)

- DOI: 10.1073/pnas.2426058122 | PMCID: PMC12146726 | PMID: 40434635
- Evidence: PythonCall.jl was used to call the PyTorch MACE.
- Full pipeline: stage not stated [MDAnalysis, OpenMM, PyTorch]

### Prevalence of simplex compression in adversarial deep neural networks. (PNAS 2025)

- DOI: 10.1073/pnas.2421593122 | PMCID: PMC12054840 | PMID: 40279388
- Evidence: We implement experiments using PyTorch ( 47 ) on an Ubuntu 64-bit Linux workstation having a 10-core Intel Xeon Silver CPU (2.20 GHz) and eight Nvidia GeForce RTX 4090 GPUs.
- Full pipeline: stage not stated [PyTorch]

### An integrated AI knowledge graph framework of bacterial enzymology and metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2425048122 | PMCID: PMC12012490 | PMID: 40193601
- Evidence: Separate encoders were used for each node type, with nodes represented as numeric features or labels encoded via multilayer perceptrons (MLPs) or embedding lookup tables (nn.Embedding from PyTorch), respectively ( 65 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HMMER, PyTorch, Python, SciPy]

### Linear Recursive Feature Machines provably recover low-rank matrices. (PNAS 2025)

- DOI: 10.1073/pnas.2411325122 | PMCID: PMC12002225 | PMID: 40153460
- Evidence: For deep linear diagonal networks, we used PyTorch ( 54 ).
- Full pipeline: machine learning [NumPy] -> stage not stated [PyTorch]

### Input-driven circuit reconfiguration in critical recurrent neural networks. (PNAS 2025)

- DOI: 10.1073/pnas.2418818122 | PMCID: PMC11912373 | PMID: 40053358
- Evidence: For example, in Python using PyTorch, where z is the state, I the input, and Ut the Fourier transform of the kernel U , all three torch.tensor()s of the same shape. where one would use fft2/ifft2 for two-dimensional tensor layers.
- Full pipeline: dimensionality reduction/clustering [PyTorch, Python]

### Broken time-reversal symmetry in visual motion detection. (PNAS 2025)

- DOI: 10.1073/pnas.2410768122 | PMCID: PMC11912477 | PMID: 40048271
- Evidence: Artificial neural networks were built and trained using Python and Pytorch ( 55 ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [Psychtoolbox]

### Learning-based inference of longitudinal image changes: Applications in embryo development, wound healing, and aging brain. (PNAS 2025)

- DOI: 10.1073/pnas.2411492122 | PMCID: PMC11873959 | PMID: 39977323
- Version used: **1.10.1**
- Evidence: We implemented our models using PyTorch (ver.
- Full pipeline: stage not stated [PyTorch v1.10.1]

### Control of flow behavior in complex fluids using automatic differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2403644122 | PMCID: PMC11874484 | PMID: 39964722
- Evidence: Yet, it is straightforward to implement AD in numerical solvers for fluid mechanics and can be carried out in open-source machine learning libraries such as JAX ( 10 ), TensorFlow ( 11 ) and PyTorch ( 12 ).
- Full pipeline: stage not stated [PyTorch, TensorFlow]

### A deep learning-enabled smart garment for accurate and versatile monitoring of sleep conditions in daily life. (PNAS 2025)

- DOI: 10.1073/pnas.2420498122 | PMCID: PMC11848432 | PMID: 39932995
- Version used: **2.0.1**
- Evidence: Network training was conducted using Python 3.8.13, Miniconda 3, and PyTorch 2.0.1 in a performance-optimized environment.
- Full pipeline: machine learning [Conda, PyTorch v2.0.1, Python v3.8.13]

### The functional role of oscillatory dynamics in neocortical circuits: A computational perspective. (PNAS 2025)

- DOI: 10.1073/pnas.2412830122 | PMCID: PMC11789028 | PMID: 39847330
- Version used: **1.9**
- Evidence: For GRU and LSTM networks, the default implementations in PyTorch 1.9 were used.
- Full pipeline: stage not stated [PyTorch v1.9]

### The perceptual primacy of feeling: Affectless visual machines explain a majority of variance in human visually evoked affect. (PNAS 2025)

- DOI: 10.1073/pnas.2306025121 | PMCID: PMC11789064 | PMID: 39847334
- Evidence: These models are sourced from six different repositories: the Torchvision (PyTorch) model zoo ( 114 ); the pytorch-image-models (timm) library ( 115 ); the Visual Self-Supervised Learning (Library) (self-supervised) model zoo ( 116 ); the Taskonomy (visualpriors) project ( 62 , 63 , 117 ); OpenAI’s CLIP repository ( 66 ); and FaceBook’s SLIP repository ( 70 ).
- Full pipeline: stage not stated [PyTorch]

### Learning the language of antibody hypervariability. (PNAS 2025)

- DOI: 10.1073/pnas.2418918121 | PMCID: PMC11725859 | PMID: 39793083
- Version used: **1.11.0**
- Evidence: Then, the embedding with reduced dimensions, outputted by the projection module is fed into two separate PyTorch (v1.11.0) Transformer Encoder modules, one each for a downstream similarity score prediction task (structure and function) ( 49 ).
- Full pipeline: stage not stated [AlphaFold, PyTorch v1.11.0]

### Linear-time prediction of proteome-scale microbial protein interactions. (PNAS 2026)

- DOI: 10.1073/pnas.2610619123 | PMCID: PMC13291599 | PMID: 42308045
- Evidence: FlashPPI was implemented in PyTorch and trained on 8 × NVIDIA H200 GPUs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [PyTorch] -> visualisation [UMAP] -> stage not stated [AlphaFold, BLAST, STRING db]

### Fast automated adjoints for spectral PDE solvers. (PNAS 2026)

- DOI: 10.1073/pnas.2530440123 | PMCID: PMC13080004 | PMID: 41961849
- Evidence: However, our implementation can still easily interface with external optimization libraries [e.g., Manopt ( 41 )] and integrators [e.g., PETSc ( 42 )], and allows combining sparse spectral solvers with machine learning frameworks [e.g., PyTorch ( 43 )], which inherently require differentiable simulators for training.
- Full pipeline: simulation/modelling [PyTorch] -> machine learning [PyTorch] -> stage not stated [OpenFOAM, Python, SciPy]

### Coalescence and translation: A language model for population genetics. (PNAS 2026)

- DOI: 10.1073/pnas.2518956123 | PMCID: PMC13079918 | PMID: 41961853
- Evidence: Models were implemented in PyTorch Lightning and trained with AdamW (base learning rate 3 × 10 − 4 ) with cosine annealing; datasets were stored in float16 for efficiency.
- Full pipeline: machine learning [PyTorch]

### Dual-encoder contrastive learning accelerates enzyme discovery. (PNAS 2026)

- DOI: 10.1073/pnas.2520070123 | PMCID: PMC13012038 | PMID: 41843673
- Version used: **2.0.0**
- Evidence: All models were trained using PyTorch v.
- Full pipeline: machine learning [PyTorch v2.0.0] -> stage not stated [RDKit]

### Data-driven superresolution imaging in disordered media. (PNAS 2026)

- DOI: 10.1073/pnas.2530449123 | PMCID: PMC12773735 | PMID: 41481440
- Evidence: The numerical experiments were coded using PyTorch.
- Full pipeline: stage not stated [PyTorch]

### Deploying synthetic coevolution and machine learning to engineer protein-protein interactions. (Science 2023)

- DOI: 10.1126/science.adh1720 | PMCID: PMC10403280 | PMID: 37499032
- Evidence: Our implementation uses the PyTorch V1.11 compiled with CUDA 10.2.
- Full pipeline: dimensionality reduction/clustering [igraph] -> visualisation [scikit-learn v1.2.2] -> stage not stated [AlphaFold, MACS2, PyTorch, RoseTTAFold]

