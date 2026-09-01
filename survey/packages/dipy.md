# DIPY

- **Category:** neuroimaging
- **Papers in survey:** 4
- **Journals:** PNAS (3), Nature (1)
- **Years:** 2021 (1), 2023 (3)
- **Pipeline stages it appears in:** registration (1), machine learning (1)

## Papers

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: We then performed an affine registration using the scikit-image 54 library, followed by intensity-based nonlinear registration using the SyN 55 algorithm from the DIPY 56 library.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Modular origins of high-amplitude cofluctuations in fine-scale functional connectivity dynamics. (PNAS 2021)

- DOI: 10.1073/pnas.2109380118 | PMCID: PMC8609635 | PMID: 34750261
- Evidence: The Dipy toolbox (version 1.1) ( 75 ) was used to fit a multishell, multitissue constrained spherical deconvolution ( 76 ) to the diffusion data with a spherical harmonics order of 8, using tissue maps estimated with FSL’s fast ( 77 ).
- Full pipeline: machine learning [DIPY] -> stage not stated [FSL]

### Early path dominance as a principle for neurodevelopment. (PNAS 2023)

- DOI: 10.1073/pnas.2218007120 | PMCID: PMC10120000 | PMID: 37053187
- Evidence: Connectivity matrices are calculated using the Diffusion Imaging in Python (DIPY) software ( 54 ).
- Full pipeline: stage not stated [DIPY, Python]

### Neuronal activity-induced, equilibrative nucleoside transporter-dependent, somatodendritic adenosine release revealed by a GRAB sensor. (PNAS 2023)

- DOI: 10.1073/pnas.2212387120 | PMCID: PMC10083574 | PMID: 36996110
- Evidence: ( I and J ) Traces ( H ) and group summary ( J ) of Ado1.0 ( Upper panels, green) and R ncp -iGlu ( Bottom panels, red) ΔF/F 0 in response to high K + before (control), during, and after (wash) application of NBTI (5 μM) and DIPY (10 μM); n = 7 coverslips each.
- Full pipeline: stage not stated [DIPY, ImageJ, PHENIX]

