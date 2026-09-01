# CONN toolbox

- **Category:** neuroimaging
- **Papers in survey:** 7
- **Journals:** PNAS (7)
- **Years:** 2021 (2), 2022 (2), 2025 (1), 2026 (2)
- **Pipeline stages it appears in:** alignment/mapping (1), differential/statistical testing (1), normalisation (1)

## Papers

### Dopaminergic brainstem disconnection is common to pharmacological and pathological consciousness perturbation. (PNAS 2021)

- DOI: 10.1073/pnas.2026289118 | PMCID: PMC8325270 | PMID: 34301891
- Evidence: Preprocessing for all scans was performed using the CONN functional connectivity toolbox [19c ( 60 )], running in MATLAB (2018b, MathWorks, Inc.).
- Full pipeline: differential/statistical testing [ggplot2] -> stage not stated [CONN toolbox]

### The impact of a lack of mathematical education on brain development and future attainment. (PNAS 2021)

- DOI: 10.1073/pnas.2013155118 | PMCID: PMC8214709 | PMID: 34099561
- Evidence: Resting fMRI data were preprocessed and analyzed using the CONN toolbox ( http://www.nitrc.org/projects/conn , RRID: SCR_009550 ) ( 93 ) in SPM12 (Wellcome Department of Imaging Neuroscience, Institute of Neurology, London, UK) and the default MNI-space direct normalization preprocessing pipeline.
- Full pipeline: quantification [SPM] -> normalisation [CONN toolbox]

### The effect of learning to drum on behavior and brain function in autistic adolescents. (PNAS 2022)

- DOI: 10.1073/pnas.2106244119 | PMCID: PMC9191342 | PMID: 35639696
- Evidence: Statistical Parametric Mapping (SPM12) and the CONN functional connectivity toolbox Version 18b ( https://www.nitrc.org/projects/conn ) ( 108 ) were used to preprocess and analyze the anatomical and functional data.
- Full pipeline: alignment/mapping [CONN toolbox, SPM] -> differential/statistical testing [CONN toolbox, SPM]

### Diffusion MRI-guided theta burst stimulation enhances memory and functional connectivity along the inferior longitudinal fasciculus in mild cognitive impairment. (PNAS 2022)

- DOI: 10.1073/pnas.2113778119 | PMCID: PMC9173759 | PMID: 35594397
- Evidence: The rs-fMRI data were acquired immediately before and after each TBS session for functional connectivity analysis, which was performed by CONN toolbox ( https://www.nitrc.org/projects/conn ) ( 91 ).
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs, CONN toolbox, FSL, FreeSurfer, MRtrix3]

### Memory control deficits in the sleep-deprived human brain. (PNAS 2025)

- DOI: 10.1073/pnas.2400743122 | PMCID: PMC11725914 | PMID: 39739795
- Evidence: RS fMRI data were analyzed using the CONN functional connectivity toolbox version 21.a [ https://web.conn-toolbox.org/ ; ( 71 )], implemented with SPM version 12 ( https://www.fil.ion.ucl.ac.uk/spm/ ) and MATLAB version 2019a.
- Full pipeline: stage not stated [CONN toolbox, FSL v5.0, R]

### Contributions of the basolateral amygdala and nucleus accumbens to sustaining not just initiating cognitive effort. (PNAS 2026)

- DOI: 10.1073/pnas.2601231123 | PMCID: PMC13167750 | PMID: 42090260
- Evidence: To examine functional coupling, we performed a gPPI analysis ( 46 , 79 ) and a background functional coupling analysis implemented by the CONN toolbox (release 22.a) ( 80 , 81 ).
- Full pipeline: stage not stated [CONN toolbox, PsychoPy, SPM, afex]

### Incentive valence differentially engages open- and closed-loop basal ganglia circuits during movement initiation. (PNAS 2026)

- DOI: 10.1073/pnas.2537314123 | PMCID: PMC13167725 | PMID: 42090262
- Evidence: Functional connectivity was computed using the CONN toolbox (v22.a).
- Full pipeline: stage not stated [ANTs, CONN toolbox, FSL]

