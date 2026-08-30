# EEGLAB

- **Category:** neuroimaging
- **Papers in survey:** 22
- **Journals:** PNAS (20), Nature (1), Cell (1)
- **Years:** 2021 (3), 2022 (5), 2023 (3), 2024 (3), 2025 (6), 2026 (2)
- **Versions named:** 2019.1 (1), 2021.0 (1), 13.6.5b (1)

## Papers

### From structure to clinic: Design of a muscarinic M1 receptor agonist with potential to treatment of Alzheimer's disease. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.001 | PMCID: PMC7616177 | PMID: 34822784
- Evidence: Non-human primate qEEG measurments Data was analyzed using existing, customized MATLAB scripts with the EEGLAB toolbox.
- Full pipeline: normalisation [CCP4] -> stage not stated [EEGLAB, ImageJ, PyMOL]

### Control of working memory by phase-amplitude coupling of human hippocampal neurons. (Nature 2024)

- DOI: 10.1038/s41586-024-07309-z | PMCID: PMC11078732 | PMID: 38632400
- Version used: **2019.1**
- Evidence: We then filtered (using pop_eegfiltnew.m from EEGLAB, v.2019.1) 66 each trial separately within the respective frequency bands of interest (see below for more details).
- Full pipeline: stage not stated [EEGLAB v2019.1, FieldTrip, FreeSurfer, Python]

### Neural indicators of articulator-specific sensorimotor influences on infant speech perception. (PNAS 2021)

- DOI: 10.1073/pnas.2025043118 | PMCID: PMC8157983 | PMID: 33980713
- Evidence: EEG preprocessing analyses were conducted using functions from EEGLAB ( 46 ).
- Full pipeline: stage not stated [EEGLAB, FieldTrip, brms]

### Volitional learning promotes theta phase coding in the human hippocampus. (PNAS 2021)

- DOI: 10.1073/pnas.2021238118 | PMCID: PMC7958181 | PMID: 33674388
- Evidence: After artifact rejection, we band-pass filtered the signal at the selected electrodes from 1 to 200 Hz using a Hamming-windowed sinc finite impulse response filter (eegfiltnew.m from the EEGLAB toolbox) ( 54 ), and rereferenced the data to bipolar references before performing subsequent analyses.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, FreeSurfer]

### Temporal scaling of human scalp-recorded potentials. (PNAS 2022)

- DOI: 10.1073/pnas.2214638119 | PMCID: PMC9618087 | PMID: 36256817
- Evidence: For all three timing tasks, EEG was preprocessed in MATLAB 2020b (Mathworks, Natick, USA) using EEGLAB ( 57 ).
- Full pipeline: dimensionality reduction/clustering [FieldTrip] -> stage not stated [EEGLAB]

### How musical rhythm training improves short-term memory for faces. (PNAS 2022)

- DOI: 10.1073/pnas.2201655119 | PMCID: PMC9564217 | PMID: 36191231
- Evidence: EEGLAB functions ( 117 ) were used for ICA (binica), spherical interpolation (pop_interp), and plotting topographies (topoplot).
- Full pipeline: stage not stated [EEGLAB]

### Spatiotemporal dynamics of odor representations in the human brain revealed by EEG decoding. (PNAS 2022)

- DOI: 10.1073/pnas.2114966119 | PMCID: PMC9173780 | PMID: 35584113
- Version used: **13.6.5b**
- Evidence: EEG data were analyzed using EEGLAB (version 13.6.5b)—an open-source toolbox for EEG data analysis ( 63 )—and custom-written MATLAB scripts unless otherwise stated.
- Full pipeline: stage not stated [EEGLAB v13.6.5b]

### Consciousness is supported by near-critical slow cortical electrodynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2024455119 | PMCID: PMC8851554 | PMID: 35145021
- Evidence: We then low-pass filtered all signals using EEGLAB’s two-way least-squares finite impulse response low-pass filtering, where the filter order was set to 3 × sampling rate lowpass frequency cutoff (the default of EEGLAB).
- Full pipeline: stage not stated [EEGLAB]

### Unlocking adults' implicit statistical learning by cognitive depletion. (PNAS 2022)

- DOI: 10.1073/pnas.2026011119 | PMCID: PMC8764693 | PMID: 34983868
- Evidence: The EEG data analyses were performed using EEGLAB, which is an open-source toolbox operated in the MATLAB environment ( 60 ).
- Full pipeline: stage not stated [EEGLAB, Psychtoolbox, R, afex, emmeans, lme4]

### Causal evidence for a coordinated temporal interplay within the language network. (PNAS 2023)

- DOI: 10.1073/pnas.2306279120 | PMCID: PMC10666120 | PMID: 37963247
- Evidence: Offline EEG preprocessing was performed using a combination of EEGLAB ( 142 ), the TMS-EEG signal analyzer (TESA) toolbox ( 143 ), and FieldTrip ( 139 ) in the Matlab environment (The Mathworks, USA).
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [EEGLAB, FieldTrip, emmeans]

### Architectural experience influences the processing of others' body expressions. (PNAS 2023)

- DOI: 10.1073/pnas.2302215120 | PMCID: PMC10576150 | PMID: 37782807
- Version used: **2021.0**
- Evidence: EEG data were imported into MATLAB to perform the following analysis with EEGLAB v2021.0 ( 55 ).
- Full pipeline: stage not stated [EEGLAB v2021.0]

### Distinct early and late neural mechanisms regulate feature-specific sensory adaptation in the human visual system. (PNAS 2023)

- DOI: 10.1073/pnas.2216192120 | PMCID: PMC9963156 | PMID: 36724257
- Evidence: Offline EEG preprocessing was performed using EEGLAB in accordance with best practice procedures ( 40 , 41 ).
- Full pipeline: stage not stated [EEGLAB]

### Differential neural mechanisms underlie cortical gating of visual spatial attention mediated by alpha-band oscillations. (PNAS 2024)

- DOI: 10.1073/pnas.2313304121 | PMCID: PMC11551340 | PMID: 39471220
- Evidence: All analyses were performed offline using EEGLAB ( 69 ), FieldTrip ( 70 ), and customized scripts written in MATLAB.
- Full pipeline: alignment/mapping [SPM] -> structure determination [SPM] -> stage not stated [EEGLAB, FieldTrip]

### Leader-follower dynamics during early social interactions matter for infant word learning. (PNAS 2024)

- DOI: 10.1073/pnas.2321008121 | PMCID: PMC11420154 | PMID: 39254996
- Evidence: First, EEG data were high-pass filtered at 1 Hz (FIR filter with a Hamming window applied), and line noise was removed using the EEGLAB function clean_line.m before applying a low-pass filter with a cutoff frequency of 30 Hz.
- Full pipeline: normalisation [Python] -> stage not stated [EEGLAB, Psychtoolbox]

### Automaticity speeds the retrieval of instances from the human hippocampus. (PNAS 2025)

- DOI: 10.1073/pnas.2518523122 | PMCID: PMC12595489 | PMID: 41166430
- Evidence: The offline preprocessing was performed in MATLAB 2021b (MathWorks Inc), using EEGLAB ( 45 ), along with in-house MATLAB code.
- Full pipeline: stage not stated [EEGLAB, FreeSurfer v6.0.0, Psychtoolbox]

### Distinct timescales dissociate spontaneous thought dimensions. (PNAS 2025)

- DOI: 10.1073/pnas.2427088122 | PMCID: PMC12478187 | PMID: 40961141
- Evidence: Data were processed in EEGLAB ( 34 ): rereferenced to the average, filtered (1 to 50 Hz), and cleaned using ICA.
- Full pipeline: stage not stated [EEGLAB, R]

### Characterizing a highly excited and sustained brain response activity during gaming: P300-CE. (PNAS 2025)

- DOI: 10.1073/pnas.2502135122 | PMCID: PMC12318198 | PMID: 40690665
- Evidence: EEG data preprocessing and analysis were conducted using MATLAB (MathWorks, R2021a) and EEGLAB toolbox ( 35 ).
- Full pipeline: stage not stated [EEGLAB, PsychoPy]

### Task difficulty modulates the effect of mind wandering on phase dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2416387122 | PMCID: PMC12146758 | PMID: 40445764
- Evidence: EEG data were collected using 64 electrodes and preprocessed with EEGLAB ( 60 ), including rereferencing, bandpass filtering, and epoch extraction (1,500 ms for Experiments 1 and 2, 2,200 ms for Experiments 3 and 4).
- Full pipeline: stage not stated [EEGLAB]

### Cardiac signals inform auditory regularity processing in the absence of consciousness. (PNAS 2025)

- DOI: 10.1073/pnas.2505454122 | PMCID: PMC12107109 | PMID: 40354541
- Evidence: Data were analyzed in MATLAB (R2019b, The MathWorks, Natick, MA) using open-source toolboxes EEGLAB [13.4.4b, ( 53 )], Fieldtrip [20201205, ( 54 )] and custom-made scripts.
- Full pipeline: stage not stated [EEGLAB, FieldTrip]

### Infant EEG microstate dynamics relate to fine-grained patterns of infant attention during naturalistic play with caregivers. (PNAS 2025)

- DOI: 10.1073/pnas.2414636122 | PMCID: PMC11929394 | PMID: 40080640
- Evidence: Preprocessing was performed with EEGLAB ( 75 ) in MATLAB (MathWorks, Natick, MA).
- Full pipeline: stage not stated [EEGLAB]

### Cognition does not automatically influence perception: Evidence from neural encoding of colors belonging to different categories. (PNAS 2026)

- DOI: 10.1073/pnas.2538139123 | PMCID: PMC13273331 | PMID: 42263133
- Evidence: Data from both sites were analyzed in Matlab (Mathworks) using the EEGLAB toolbox ( 55 ).
- Full pipeline: differential/statistical testing [R v4.3, emmeans v1.10, lme4 v3.1] -> stage not stated [EEGLAB]

### Human hippocampal theta-gamma coupling coordinates sequential planning during navigation. (PNAS 2026)

- DOI: 10.1073/pnas.2513547123 | PMCID: PMC12956831 | PMID: 41758661
- Evidence: Physiological artifacts related to eye blinks and lateral eye movements were identified and removed using independent components analysis implemented in Fieldtrip and EEGLAB ( 46 ).
- Full pipeline: stage not stated [EEGLAB, FieldTrip, SPM]

