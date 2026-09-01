# NiBabel

- **Category:** neuroimaging
- **Papers in survey:** 4
- **Journals:** PNAS (2), Nature (1), Cell (1)
- **Years:** 2023 (1), 2024 (1), 2025 (2)
- **Versions named:** 3.2.2 (1), 3.2.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (1), differential/statistical testing (1)

## Papers

### Stimulant medications affect arousal and reward, not attention networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.039 | PMCID: PMC12834599 | PMID: 41448140
- Evidence: 176 Processing dependencies included FSL, 177 FreeSurfer, 178 and NiBabel.
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [FSL, FreeSurfer, NiBabel]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **3.2.2**
- Evidence: Analysis-specific functional preprocessing Additional, analysis-specific, fMRI data preprocessing was performed using FSL 6.0.2 (FMRIB Software Library) 94 , Statistical Parametric Mapping (SPM 12) software 95 , and custom Python scripts (using NiBabel (3.2.2) 96 and SciPy (1.8.0) 97 after the above-outlined general preprocessing.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: Volumetric segmentation and analysis were performed using the NumPy, ANTsPy , and NiBabel packages in Python (Python 3.7).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Version used: **3.2.0**
- Evidence: These and the diameter of the respective closest vessel segment for each hippocampal GM voxel were then stored as NIfTI volumes using nibabel v3.2.0 ( 109 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

