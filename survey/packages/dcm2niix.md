# dcm2niix

- **Category:** neuroimaging
- **Papers in survey:** 4
- **Journals:** Nature (2), PNAS (2)
- **Years:** 2024 (1), 2025 (2), 2026 (1)

## Papers

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Evidence: This includes converting DICOM data to NIfTI using dcm2niix 88 and creating event files using custom Python codes.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Population-scale repeat expansions elucidate disease risk and brain atrophy. (Nature 2026)

- DOI: 10.1038/s41586-026-10345-6 | PMCID: PMC13190288 | PMID: 41951733
- Evidence: In brief, the raw .zip files were accessed from the UKB Research Access Platform and converted to NIfTI using dcm2niix 70 .
- Full pipeline: variant calling [R, REGENIE v3.2] -> registration [FSL v6.0.7.8] -> differential/statistical testing [REGENIE v3.2] -> stage not stated [FreeSurfer v7.3.2, PLINK, dcm2niix]

### Deciphering the neural responses to a naturalistic persuasive message. (PNAS 2024)

- DOI: 10.1073/pnas.2401317121 | PMCID: PMC11513929 | PMID: 39413130
- Evidence: First, we transformed the raw DICOM files to NIFTI files using the dcm2niix [( 91 ); https://github.com/rordenlab/dcm2niix ].
- Full pipeline: stage not stated [Nilearn, PsychoPy, Python, dcm2niix, fMRIPrep]

### Shared disbelief and shared belief: Belief and disbelief as drivers of interpersonal neural synchronization during narrative processing. (PNAS 2025)

- DOI: 10.1073/pnas.2422396122 | PMCID: PMC12167953 | PMID: 40472031
- Evidence: The raw DICOM files were first converted to nifty files using the dcm2nii tool.
- Full pipeline: registration [FSL v5.0] -> stage not stated [dcm2niix]

