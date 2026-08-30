# cryoDRGN

- **Category:** structbio
- **Papers in survey:** 9
- **Journals:** PNAS (5), Nature (4)
- **Years:** 2022 (2), 2024 (4), 2025 (3)
- **Versions named:** 3.2.0 (1), 0.3.4 (1)
- **Pipeline stages it appears in:** machine learning (3), dimensionality reduction/clustering (2), structure determination (2), alignment/mapping (1)

## Papers

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: These segments and their assigned poses were then used for training of neural networks in cryoDRGN 69 to assess conformational variability.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Structure of the human TIP60-C histone exchange and acetyltransferase complex. (Nature 2024)

- DOI: 10.1038/s41586-024-08011-w | PMCID: PMC11578891 | PMID: 39260417
- Evidence: To analyse the heterogeneity in the cryo-EM map owing to the presence of the flexible TRRAP module (430 kDa), we used the neural-network-based cryoDRGN 43 and OPUS-DSD 44 reconstruction to map the particles on two principal components.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [cryoDRGN] -> structure determination [PHENIX, cryoDRGN] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Version used: **3.2.0**
- Evidence: Particles were then downsampled to 128 pixels and a cryoDRGN (v.3.2.0) 46 model was trained with 8 latent dimensions and 50 training iterations.
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### Structural dynamics of human fatty acid synthase in the condensing cycle. (Nature 2025)

- DOI: 10.1038/s41586-025-08782-w | PMCID: PMC12058526 | PMID: 39978408
- Evidence: The cryoDRGN models were trained with a latent dimension size of 8 and 25 epochs.
- Full pipeline: registration [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> machine learning [cryoDRGN] -> visualisation [UCSF Chimera] -> stage not stated [CTFFIND, Coot]

### Multistate structures of the MLL1-WRAD complex bound to H2B-ubiquitinated nucleosome. (PNAS 2022)

- DOI: 10.1073/pnas.2205691119 | PMCID: PMC9499523 | PMID: 36095189
- Evidence: We note that efforts to identify additional states using cryoDRGN ( 73 ) did not yield useful results.
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, RELION v3.0, VMD v1.9.3, cryoDRGN]

### Capturing a methanogenic carbon monoxide dehydrogenase/acetyl-CoA synthase complex via cryogenic electron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2410995121 | PMCID: PMC11474084 | PMID: 39361653
- Version used: **0.3.4**
- Evidence: Cryo-EM data processing was carried out using a combination of cryoSPARC v3.3.2 ( 65 ), pyem v0.5 ( 72 ), RELION v4.0 ( 66 ), and cryoDRGN v0.3.4 ( 67 , 68 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [AlphaFold] -> stage not stated [ChimeraX, RELION v4.0, cryoDRGN v0.3.4]

### Sec7 regulatory domains scaffold autoinhibited and active conformations. (PNAS 2024)

- DOI: 10.1073/pnas.2318615121 | PMCID: PMC10927569 | PMID: 38416685
- Evidence: For cryoDRGN analysis, we used TOPAZ to increase the likelihood of rare particles ( 68 ) (this did not improve resolution of the monomer) and aligned sorted particles on a monomer without subtraction for input into cryoDRGN ( 20 ).
- Full pipeline: alignment/mapping [cryoDRGN] -> structure determination [MotionCor2, PHENIX, RELION v3.1] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### Amortized template matching of molecular conformations from cryoelectron microscopy images using simulation-based inference. (PNAS 2025)

- DOI: 10.1073/pnas.2420158122 | PMCID: PMC12168013 | PMID: 40465628
- Evidence: CryoAI ( 27 ) and its implementation in cryoDRGN ( 28 ) use direct gradient-based optimization to amortize the particle poses while still requiring the direct estimation of a pose for each particle.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [PyTorch] -> stage not stated [cryoDRGN]

### Cryo-EM heterogeneity analysis using regularized covariance estimation and kernel regression. (PNAS 2025)

- DOI: 10.1073/pnas.2419140122 | PMCID: PMC11892586 | PMID: 40009640
- Evidence: For example, for a dataset of 300,000 images of size 256 2 , on one graphics processing unit (GPU), † RECOVAR computes 100 principal components in 4 h, where 3DVA takes 16 h to compute only 20 principal components, and Deep Reconstructing Generative Networks (cryoDRGN) takes 23 h to train a network.
- Full pipeline: dimensionality reduction/clustering [UMAP, cryoDRGN] -> structure determination [ChimeraX, UMAP, cryoDRGN] -> visualisation [UMAP] -> stage not stated [RELION]

