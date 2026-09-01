# MRIQC

- **Category:** neuroimaging
- **Papers in survey:** 3
- **Journals:** PNAS (2), Nature (1)
- **Years:** 2023 (1), 2025 (2)
- **Versions named:** 0.16.1 (1), 0.15.1 (1), 0.15.0 (1)
- **Pipeline stages it appears in:** quality control (3)

## Papers

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **0.16.1**
- Evidence: Subsequently, MRI data quality control was performed using MRIQC (0.16.1) 89 and custom scripts for data rejection.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Hemispheric asymmetry in cortical thinning reflects intrinsic organization of the neurotransmitter systems and homotopic functional connectivity. (PNAS 2023)

- DOI: 10.1073/pnas.2306990120 | PMCID: PMC10589642 | PMID: 37831741
- Version used: **0.15.0**
- Evidence: Quality control, preprocessing of anatomical and functional data were performed, respectively, with MRIQC 0.15.0 ( 41 ), fMRIPrep 1.3.2 ( 42 ), and FSL_regfilt 5.0.9.
- Full pipeline: quality control [FSL, MRIQC v0.15.0, fMRIPrep v1.3.2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R v4.2.2] -> stage not stated [FreeSurfer v6.0.0]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Version used: **0.15.1**
- Evidence: The quality of the fMRI data was first assessed using MRIQC version 0.15.1 ( 101 ).
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

