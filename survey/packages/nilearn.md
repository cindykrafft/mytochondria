# Nilearn

- **Category:** neuroimaging
- **Papers in survey:** 14
- **Journals:** PNAS (11), Nature (2), Science (1)
- **Years:** 2021 (3), 2022 (1), 2023 (2), 2024 (3), 2025 (5)
- **Versions named:** 0.4.2 (1), 0.5.2 (1), 0.6.2 (1)
- **Pipeline stages it appears in:** differential/statistical testing (1)

## Papers

### Geometric constraints on human brain function. (Nature 2023)

- DOI: 10.1038/s41586-023-06098-1 | PMCID: PMC10266981 | PMID: 37258669
- Evidence: We used the python module Nilearn 86 to retrieve activation maps from NeuroVault that were unthresholded and with a modality tag of fMRI-BOLD.
- Full pipeline: stage not stated [FSL, FreeSurfer, Nilearn]

### A foundation model to predict and capture human cognition. (Nature 2025)

- DOI: 10.1038/s41586-025-09215-4 | PMCID: PMC12390832 | PMID: 40604288
- Evidence: The GLMs were built using nilearn 66 .
- Full pipeline: stage not stated [Nilearn, fMRIPrep v24.0]

### Temporal self-compression: Behavioral and neural evidence that past and future selves are compressed as they move away from the present. (PNAS 2021)

- DOI: 10.1073/pnas.2101403118 | PMCID: PMC8670431 | PMID: 34848536
- Evidence: Multivariate analyses were all conducted using Python packages, including nltools 0.3.14 ( 95 ) and nilearn ( 96 ).
- Full pipeline: registration [AFNI, FreeSurfer] -> stage not stated [FSL v5.0.9, Nilearn, Nipype v1.2.0, R, fMRIPrep v1.4.0, lme4]

### Divisive normalization unifies disparate response signatures throughout the human visual hierarchy. (PNAS 2021)

- DOI: 10.1073/pnas.2108713118 | PMCID: PMC8609633 | PMID: 34772812
- Version used: **0.6.2**
- Evidence: Many internal operations of fMRIPrep use Nilearn 0.6.2 (ref.
- Full pipeline: registration [AFNI, fMRIPrep] -> structure determination [FreeSurfer v7.1] -> stage not stated [FSL v5.0.9, Nilearn v0.6.2, PsychoPy]

### Attention, awareness, and the right temporoparietal junction. (PNAS 2021)

- DOI: 10.1073/pnas.2026099118 | PMCID: PMC8237657 | PMID: 34161276
- Evidence: Many internal operations of FMRIPREP use Nilearn ( 43 ) (RRID: SCR_001362 ), principally within the BOLD-processing workflow.
- Full pipeline: normalisation [ANTs] -> registration [AFNI, ANTs] -> stage not stated [FSL, Nilearn, Nipype, fMRIPrep v1.2.3]

### The neural signature of the decision value of future pain. (PNAS 2022)

- DOI: 10.1073/pnas.2119931119 | PMCID: PMC9191656 | PMID: 35658082
- Evidence: We first created general linear models (GLMs) at the participant level using the nilearn GLM module to estimate the BOLD response to various task events.
- Full pipeline: differential/statistical testing [Nilearn] -> machine learning [scikit-learn] -> stage not stated [fMRIPrep v20.1.1]

### Rats respond to aversive emotional arousal of human handlers with the activation of the basolateral and central amygdala. (PNAS 2023)

- DOI: 10.1073/pnas.2302655120 | PMCID: PMC10655214 | PMID: 37934822
- Version used: **0.5.2**
- Evidence: We performed preprocessing on the fMRI data using fMRIPrep 1.4.0 software ( 54 , 55 ), which is based on Nipype 1.2.0 ( 56 , 57 ) and Nilearn 0.5.2 ( 58 ).
- Full pipeline: registration [AFNI, FSL v5.0.9] -> differential/statistical testing [SciPy] -> stage not stated [ANTs v2.2.0, ImageJ, Nilearn v0.5.2, Nipype v1.2.0, fMRIPrep v1.4.0]

### Deciphering the neural responses to a naturalistic persuasive message. (PNAS 2024)

- DOI: 10.1073/pnas.2401317121 | PMCID: PMC11513929 | PMID: 39413130
- Evidence: After preprocessing with fMRIprep, we further denoised the data using nilearn ( 93 ).
- Full pipeline: stage not stated [Nilearn, PsychoPy, Python, dcm2niix, fMRIPrep]

### Diverging neural dynamics for syntactic structure building in naturalistic speaking and listening. (PNAS 2024)

- DOI: 10.1073/pnas.2310766121 | PMCID: PMC10945772 | PMID: 38442171
- Evidence: Each word-by-word predictor was mean-centered (except for the word rate predictor, and the sentence-onset and -offset predictors) and convolved with the canonical hemodynamic response function following SPM’s double gamma function as computed in nilearn .
- Full pipeline: differential/statistical testing [R v4.0.3, lme4] -> stage not stated [FreeSurfer, Nilearn, Python, TensorFlow, emmeans]

### The central renin-angiotensin system: A genetic pathway, functional decoding, and selective target engagement characterization in humans. (PNAS 2024)

- DOI: 10.1073/pnas.2306936121 | PMCID: PMC10895353 | PMID: 38349873
- Evidence: Many internal operations of fMRIPrep using Nilearn ( 110 ), mostly within the functional processing workflow.
- Full pipeline: alignment/mapping [SPM] -> registration [FSL] -> differential/statistical testing [SPM] -> stage not stated [Nilearn, Nipype v1.5.1, fMRIPrep v20.2.1]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Evidence: First-level individual analysis of fMRI data was performed using the Nilearn package in Python ( 104 ).
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Version used: **0.4.2**
- Evidence: Many internal operations of fMRIPrep use Nilearn 0.4.2 mostly within the functional processing workflow.
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### Brain aging shows nonlinear transitions, suggesting a midlife "critical window" for metabolic intervention. (PNAS 2025)

- DOI: 10.1073/pnas.2416433122 | PMCID: PMC11912423 | PMID: 40030017
- Evidence: Mayo, Cam-CAN, and the metabolic intervention datasets were preprocessed with fMRIprep ( 83 ), combined with image processing methods from SPM (SPM12, UCL) and the nilearn python library ( 84 ).
- Full pipeline: stage not stated [Nilearn, SPM, SciPy, fMRIPrep]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Software libraries used for plotting anatomy include Pysurfer and nilearn.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

