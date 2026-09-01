# Nipype

- **Category:** neuroimaging
- **Papers in survey:** 13
- **Journals:** PNAS (12), Nature (1)
- **Years:** 2021 (3), 2022 (1), 2023 (2), 2024 (3), 2025 (3), 2026 (1)
- **Versions named:** 1.5.1 (3), 1.6.1 (2), 1.2.0 (2), 1.1.1 (1), 1.1.7 (1)
- **Pipeline stages it appears in:** alignment/mapping (1), differential/statistical testing (1), normalisation (1)

## Papers

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **1.6.1**
- Evidence: All (f)MRI data were preprocessed using fMRIPrep (20.2.3) 90 , based on Nipype (1.6.1) 91 .
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Temporal self-compression: Behavioral and neural evidence that past and future selves are compressed as they move away from the present. (PNAS 2021)

- DOI: 10.1073/pnas.2101403118 | PMCID: PMC8670431 | PMID: 34848536
- Version used: **1.2.0**
- Evidence: 85 , 86 ; Research Resource Identifier [RRID]: SCR_016216), which is based on Nipype 1.2.0 (refs.
- Full pipeline: registration [AFNI, FreeSurfer] -> stage not stated [FSL v5.0.9, Nilearn, Nipype v1.2.0, R, fMRIPrep v1.4.0, lme4]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Evidence: Processing within the pipeline made use of the following Python libraries: Nipype ( 49 ), the Advanced Normalization Tools ( 50 ), the Insight Toolkit ( 51 ), Scikit-image ( 52 ), Scikit-learn ( 53 ), and SciPy ( 54 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Attention, awareness, and the right temporoparietal junction. (PNAS 2021)

- DOI: 10.1073/pnas.2026099118 | PMCID: PMC8237657 | PMID: 34161276
- Evidence: Results included in this manuscript come from preprocessing performed using fMRIPrep version 1.2.3 ( 32 ) (RRID: SCR_016216 ), a Nipype ( 33 ) (RRID: SCR_002502 ) based tool.
- Full pipeline: normalisation [ANTs] -> registration [AFNI, ANTs] -> stage not stated [FSL, Nilearn, Nipype, fMRIPrep v1.2.3]

### Mind blanking is a distinct mental state linked to a recurrent brain profile of globally positive connectivity during ongoing mentation. (PNAS 2022)

- DOI: 10.1073/pnas.2200511119 | PMCID: PMC9564098 | PMID: 36194631
- Evidence: Preprocessing and denoising were performed via a locally developed pipeline written in Python [nipype package ( 48 )] encompassing toolboxes from Statistical Parametric Mapping 12 ( 49 ), FSL 6.0 ( 50 ), AFNI ( 51 ), and ART ( http://web.mit.edu/swg/software.htm ).
- Full pipeline: alignment/mapping [AFNI, FSL v6.0, Nipype, SPM] -> differential/statistical testing [AFNI, FSL v6.0, Nipype, SPM] -> machine learning [scikit-learn] -> stage not stated [Python]

### Rats respond to aversive emotional arousal of human handlers with the activation of the basolateral and central amygdala. (PNAS 2023)

- DOI: 10.1073/pnas.2302655120 | PMCID: PMC10655214 | PMID: 37934822
- Version used: **1.2.0**
- Evidence: We performed preprocessing on the fMRI data using fMRIPrep 1.4.0 software ( 54 , 55 ), which is based on Nipype 1.2.0 ( 56 , 57 ) and Nilearn 0.5.2 ( 58 ).
- Full pipeline: registration [AFNI, FSL v5.0.9] -> differential/statistical testing [SciPy] -> stage not stated [ANTs v2.2.0, ImageJ, Nilearn v0.5.2, Nipype v1.2.0, fMRIPrep v1.4.0]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Version used: **1.1.7**
- Evidence: Results included in this manuscript come from preprocessing performed using fMRIPrep 1.2.6-1 ( 117 ), which is based on Nipype 1.1.7 ( 118 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Brain activity of professional investors signals future stock performance. (PNAS 2024)

- DOI: 10.1073/pnas.2307982121 | PMCID: PMC11032448 | PMID: 38593084
- Evidence: Finally, data of the remaining participants were preprocessed using the standard pipeline of fMRIprep version 20.2.0 ( 41 ), based on Nipype ( 42 ) ( SI Appendix , Appendix 2 ).
- Full pipeline: stage not stated [Nipype, Python, fMRIPrep v20.2.0]

### The dorsomedial prefrontal cortex prioritizes social learning during rest. (PNAS 2024)

- DOI: 10.1073/pnas.2309232121 | PMCID: PMC10962978 | PMID: 38466844
- Version used: **1.6.1**
- Evidence: Results included in this manuscript come from preprocessing performed using fMRIPrep 20.2.2 ( 85 ); RRID:SCR_016216), which is based on Nipype 1.6.1 ( 86 ); RRID:SCR_002502).
- Full pipeline: stage not stated [ANTs v2.3.3, FSL v5.0.9, FreeSurfer, Nipype v1.6.1, fMRIPrep v20.2.2]

### The central renin-angiotensin system: A genetic pathway, functional decoding, and selective target engagement characterization in humans. (PNAS 2024)

- DOI: 10.1073/pnas.2306936121 | PMCID: PMC10895353 | PMID: 38349873
- Version used: **1.5.1**
- Evidence: All MRI data were preprocessed using standardized workflows in fMRIPrep 20.2.1 ( 108 ), which is based on Nipype 1.5.1 ( 109 ). fMRIPrep is an automated pre-processing pipeline that flexibly employs tools from a variety of neuroimaging software packages.
- Full pipeline: alignment/mapping [SPM] -> registration [FSL] -> differential/statistical testing [SPM] -> stage not stated [Nilearn, Nipype v1.5.1, fMRIPrep v20.2.1]

### Joint models reveal human subcortical underpinnings of choice and learning behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2502269122 | PMCID: PMC12435315 | PMID: 40911596
- Version used: **1.5.1**
- Evidence: Results included in this manuscript come from preprocessing performed using fMRIPrep 20.2.0 ( 129 , 130 ); RRID:SCR_016216], which is based on Nipype 1.5.1 ( 131 , 132 ); RRID:SCR_002502].
- Full pipeline: registration [ANTs] -> stage not stated [FSL, Nipype v1.5.1, fMRIPrep v20.2.0, lme4]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Version used: **1.1.1**
- Evidence: Results included in this manuscript come from preprocessing performed using fMRIPprep 1.1.4 which is based on Nipype 1.1.1.
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### Distinct contributions of hippocampal pathways in learning regularities and exceptions revealed by functional footprints. (PNAS 2026)

- DOI: 10.1073/pnas.2503388123 | PMCID: PMC12818569 | PMID: 41543896
- Version used: **1.5.1**
- Evidence: Functional volumes were preprocessed with fMRIPrep version 20.2.1 ( 59 , 60 ), which is based on Nipype 1.5.1 ( 61 , 62 ).
- Full pipeline: normalisation [ANTs] -> registration [FSL] -> differential/statistical testing [R, lme4 v1.1] -> stage not stated [FreeSurfer, MRtrix3, Nipype v1.5.1, fMRIPrep v20.2.1]

