# SUMA

- **Category:** neuroimaging
- **Papers in survey:** 6
- **Journals:** PNAS (6)
- **Years:** 2021 (1), 2022 (1), 2023 (1), 2025 (3)
- **Pipeline stages it appears in:** structure determination (1), normalisation (1)

## Papers

### Shared neural codes for visual and semantic information about familiar faces in a common representational space. (PNAS 2021)

- DOI: 10.1073/pnas.2110474118 | PMCID: PMC8609335 | PMID: 34732577
- Evidence: Other categories” in SUMA ( 45 ).
- Full pipeline: stage not stated [AFNI, Python, SUMA, fMRIPrep v1.0.3]

### Brain-wide functional connectivity of face patch neurons during rest. (PNAS 2022)

- DOI: 10.1073/pnas.2206559119 | PMCID: PMC9457296 | PMID: 36044550
- Evidence: For the sake of clarity, we therefore inverted the sign of modulation throughout the article. fMRI Data Processing. fMRI data were analyzed using the AFNI/SUMA software package ( 61 ) and custom-written MATLAB code (MathWorks, Natick, MA).
- Full pipeline: stage not stated [AFNI, SUMA]

### Different roles of response covariability and its attentional modulation in the sensory cortex and posterior parietal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2216942120 | PMCID: PMC10589615 | PMID: 37812698
- Evidence: SUMA and custom Python/MATLAB codes were used to generate equi-volume surfaces ( https://github.com/herrlich10/mripy ).
- Full pipeline: stage not stated [FreeSurfer, Psychtoolbox, SUMA]

### Dynamic neuroplasticity of language networks: The intersection of bilingualism and epilepsy. (PNAS 2025)

- DOI: 10.1073/pnas.2422742122 | PMCID: PMC12304909 | PMID: 40658859
- Evidence: Image Processing. fMRI data processing was carried out using AFNI ( 52 ) and SUMA ( 53 ).
- Full pipeline: stage not stated [AFNI, SUMA]

### Temporal autocorrelation is predictive of age-An extensive MEG time-series analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411098122 | PMCID: PMC11873822 | PMID: 39977317
- Evidence: T1- and T2-weighted images were reconstructed using FreeSurfer 6.0.0 ( https://surfer.nmr.mgh.harvard.edu/ ) and MEG sensor data further projected to individual cortical surfaces derived from SUMA ( 65 ).
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer v6.0.0, SUMA] -> stage not stated [FieldTrip v3.5]

### Expansion of a conserved architecture drives the evolution of the primate visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421585122 | PMCID: PMC11761675 | PMID: 39805017
- Evidence: Analysis of Functional NeuroImages (AFNI; RRID:nif-0000-00259; Cox, 1996), SUMA ( 116 ), Freesurfer (FreeSurfer, RRID:nif-0000-00304) ( 117 , 118 ), FSL ( 119 ) (FSL, RRID:birnlex_2067), Advanced Normalization Tools ( 120 ) (ANTs), and MATLAB (MATLAB, RRID:nlx_153890) were used for additional data processing.
- Full pipeline: normalisation [AFNI, ANTs, FSL, SUMA] -> structure determination [FreeSurfer]

