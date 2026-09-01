# MNE-Python

- **Category:** neuroimaging
- **Papers in survey:** 9
- **Journals:** PNAS (6), Nature (3)
- **Years:** 2022 (2), 2023 (2), 2024 (2), 2025 (3)
- **Versions named:** 0.22.0 (2), 0.24 (1), 0.23.0 (1)

## Papers

### Walking naturally after spinal cord injury using a brain-spine interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06094-5 | PMCID: PMC10232367 | PMID: 37225984
- Evidence: Stereotypical artefacts (cardiac, ocular) were identified by independent components analysis using MNE-Python software 45 and rejected on visual screening (Infomax method, calculated separately for magnetometers and gradiometers using 64 components).
- Full pipeline: stage not stated [MNE-Python]

### Large-scale single-neuron speech sound encoding across the depth of human cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06839-2 | PMCID: PMC10866713 | PMID: 38093008
- Version used: **0.22.0**
- Evidence: We used an alpha regularization parameter of 500 using the ‘ReceptiveField’ function implemented in mne-python v.0.22.0.
- Full pipeline: registration [Kilosort v2.5] -> stage not stated [MNE-Python v0.22.0, PyTorch]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **0.24**
- Evidence: The results of the optimization phase and the preregistered replication phase were compared and deemed to be largely compatible, with some minor exceptions (section 4 of Supplementary Information ). iEEG preprocessing Data were converted to BIDS 67 and preprocessed using MNE-Python (v0.24) 68 , and custom-written functions in Python and Matlab.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Deep neural networks constrained by neural mass models improve electrophysiological source imaging of spatiotemporal brain dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2201128119 | PMCID: PMC9351497 | PMID: 35881787
- Version used: **0.22.0**
- Evidence: The data analysis results for sLORETA and unit–noise–gain minimum variance Beamformer were calculated using MNE-Python (version 0.22.0) ( 41 ); CMEM was calculated using the BrainEntropy plug-in (version 2.7.3) in Brainstorm, and FAST-IRES was calculated using the published code. * Otsu’s ( 74 ) method was used to find the extent of the imaging solution when calculating the precision and recall fo...
- Full pipeline: machine learning [PyTorch] -> stage not stated [FreeSurfer, MNE-Python v0.22.0, Python v0.22.0]

### Enhancement of speech-in-noise comprehension through vibrotactile stimulation at the syllabic rate. (PNAS 2022)

- DOI: 10.1073/pnas.2117000119 | PMCID: PMC9060510 | PMID: 35312362
- Evidence: EEG preprocessing analysis were carried out by using the MNE Python package ( 60 ).
- Full pipeline: stage not stated [MNE-Python]

### Neural tracking measures of speech intelligibility: Manipulating intelligibility while keeping acoustics unchanged. (PNAS 2023)

- DOI: 10.1073/pnas.2309166120 | PMCID: PMC10710032 | PMID: 38032934
- Version used: **0.23.0**
- Evidence: All data analyses were performed in mne-python 0.23.0 ( 47 , 48 ) and Eelbrain 0.36 ( 49 ).
- Full pipeline: normalisation [FreeSurfer] -> differential/statistical testing [R v4.0] -> stage not stated [MNE-Python v0.23.0, lme4 v1.1]

### Aversive memories can be weakened during human sleep via the reactivation of positive interfering memories. (PNAS 2024)

- DOI: 10.1073/pnas.2400678121 | PMCID: PMC11295023 | PMID: 39052838
- Evidence: All EEG processing steps were carried out using MNE-Python [v1.5.1, ( 82 )] and Python 3.8.
- Full pipeline: differential/statistical testing [Docker] -> stage not stated [MNE-Python, Python v3.8]

### From retinotopic to ordinal coding: Dissecting the cortical stages of visual word recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2507291122 | PMCID: PMC12582272 | PMID: 41118216
- Evidence: To remove environmental noise and artifacts related to head movements, Maxwell filtering was applied using the MaxFilter tool in MNE-Python.
- Full pipeline: normalisation [Python] -> differential/statistical testing [Python] -> stage not stated [FSL, MNE-Python, PyTorch, SPM]

### Differential representations of spatial location by aperiodic and alpha oscillatory activity in working memory. (PNAS 2025)

- DOI: 10.1073/pnas.2506418122 | PMCID: PMC12318205 | PMID: 40705421
- Evidence: To estimate an aperiodic-adjusted instantaneous measure of alpha power, we first computed sliding-window power spectra for each trial using multitapers in MNE-Python ( 35 ) with time windows of 1 s ( Fig.
- Full pipeline: stage not stated [MNE-Python]

