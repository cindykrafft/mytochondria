# FieldTrip

- **Category:** neuroimaging
- **Papers in survey:** 42
- **Journals:** PNAS (36), Nature (5), Cell (1)
- **Years:** 2021 (9), 2022 (8), 2023 (5), 2024 (10), 2025 (8), 2026 (2)
- **Versions named:** 3.5 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), differential/statistical testing (2), simulation/modelling (1), visualisation (1), dimensionality reduction/clustering (1), machine learning (1), structure determination (1)

## Papers

### Impaired neural replay of inferred relationships in schizophrenia. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.012 | PMCID: PMC8357425 | PMID: 34197734
- Evidence: MEG pre-processing, time-frequency analysis and source reconstruction was performed using MATLAB in conjunction with functions from the Statistical Parametric Mapping 12 (SPM12, https://www.fil.ion.ucl.ac.uk/spm/software/spm12/ ) toolbox, FieldTrip ( https://www.fieldtriptoolbox.org/ ), the OHBA Software Library (OSL, including OAT, https://ohba-analysis.github.io/osl-docs/ ) and FMRIB Software Li...
- Full pipeline: alignment/mapping [FieldTrip, SPM] -> differential/statistical testing [FieldTrip, SPM] -> structure determination [FieldTrip, SPM] -> stage not stated [FSL]

### An orexigenic subnetwork within the human hippocampus. (Nature 2023)

- DOI: 10.1038/s41586-023-06459-w | PMCID: PMC10499606 | PMID: 37648849
- Evidence: Task data preprocessing and analyses Electrophysiological data were downsampled to 1,000 Hz, notch filtered for 60 Hz and 2nd–3rd harmonics, and Laplacian rereferenced in FieldTrip as previously described 12 , 68 .
- Full pipeline: alignment/mapping [SPM] -> normalisation [ANTs v2.1.0] -> registration [ANTs v2.1.0] -> differential/statistical testing [SPM] -> stage not stated [FSL, FieldTrip, Python v3.6, fMRIPrep v1.2.3]

### Single-neuron representations of odours in the human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08016-5 | PMCID: PMC11485236 | PMID: 39385026
- Evidence: Electrode localization was performed based on co-registered CTs and MRIs using the LeGUI software package (v.1.2) 65 and electrode locations were visualized using Fieldtrip (v.213bc8bcb) 66 and the ‘plot_ecog’ function ( https://github.com/s-michelmann/moment-by-moment-tracking/blob/master/plot_ecog.m ).
- Full pipeline: visualisation [FieldTrip]

### Control of working memory by phase-amplitude coupling of human hippocampal neurons. (Nature 2024)

- DOI: 10.1038/s41586-024-07309-z | PMCID: PMC11078732 | PMID: 38632400
- Evidence: The 3D plot was generated using FieldTrip (v.20200409) and the Brainnetome Atlas 58 .
- Full pipeline: stage not stated [EEGLAB v2019.1, FieldTrip, FreeSurfer, Python]

### Single-neuronal elements of speech production in humans. (Nature 2024)

- DOI: 10.1038/s41586-023-06982-w | PMCID: PMC10866697 | PMID: 38297120
- Evidence: The MNI transformation of these coordinates was then carried out to register the locations in MNI space with Fieldtrip toolbox (v.20230602; https://www.fieldtriptoolbox.org/ ; Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [Kilosort v1.0, scikit-learn] -> structure determination [FreeSurfer v7.4.1] -> stage not stated [FieldTrip, statsmodels v0.13.5]

### Parkinson's disease as a somato-cognitive action network disorder. (Nature 2026)

- DOI: 10.1038/s41586-025-10059-1 | PMCID: PMC13017517 | PMID: 41639440
- Evidence: Using the volume conductor model, the potential distribution stemming from DBS was simulated through the integration of the FieldTrip-SimBio pipeline.
- Full pipeline: normalisation [ANTs, FSL] -> registration [FSL, FreeSurfer v6.0.0] -> simulation/modelling [FieldTrip] -> stage not stated [Connectome Workbench v1.5]

### The hippocampus as the switchboard between perception and memory. (PNAS 2021)

- DOI: 10.1073/pnas.2114171118 | PMCID: PMC8685930 | PMID: 34880133
- Evidence: All EEG data processing was performed in MATLAB using FieldTrip ( 66 ).
- Full pipeline: stage not stated [FieldTrip]

### Visual exposure enhances stimulus encoding and persistence in primary cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2105276118 | PMCID: PMC8639370 | PMID: 34663727
- Evidence: The Fieldtrip toolbox ( 65 ) was used for laminar analysis ( SI Appendix , Fig.
- Full pipeline: stage not stated [FieldTrip, Python]

### The human olfactory bulb processes odor valence representation and cues motor avoidance behavior. (PNAS 2021)

- DOI: 10.1073/pnas.2101209118 | PMCID: PMC8545486 | PMID: 34645711
- Evidence: The maximum projection of the dipoles’ time course over three principal axes was computed to serve as OB activity. eLORETA analysis was carried out in the open-source Fieldtrip toolbox 2018 within MATLAB R2019b ( 81 ).
- Full pipeline: stage not stated [FieldTrip]

### Increasing and decreasing interregional brain coupling increases and decreases oscillatory activity in the human brain. (PNAS 2021)

- DOI: 10.1073/pnas.2100652118 | PMCID: PMC8449322 | PMID: 34507986
- Evidence: Offline EEG analysis was performed using FieldTrip ( 33 ).
- Full pipeline: stage not stated [FieldTrip]

### Spontaneous activity competes with externally evoked responses in sensory cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2023286118 | PMCID: PMC8237647 | PMID: 34155142
- Evidence: For time-frequency representation, we transformed the LFP data from the time domain to the frequency domain by convolving it with complex Morlet wavelets seven cycles wide in each frequency using the Fieldtrip toolbox ( 68 ) for Matlab (Mathworks, version R2018a).
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [FieldTrip]

### Neural indicators of articulator-specific sensorimotor influences on infant speech perception. (PNAS 2021)

- DOI: 10.1073/pnas.2025043118 | PMCID: PMC8157983 | PMID: 33980713
- Evidence: We also tested for an interaction of Condition by Phonetic contrast; to conduct this analysis in Fieldtrip, we calculated the difference between the standard and deviant trials, and compared this difference in a paired t test between the /ba/-/ɗa/ and the /ɗa/-/ɖa/ contrasts.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, brms]

### Volitional learning promotes theta phase coding in the human hippocampus. (PNAS 2021)

- DOI: 10.1073/pnas.2021238118 | PMCID: PMC7958181 | PMID: 33674388
- Evidence: Using the FieldTrip toolbox ( 55 ), we decomposed the signal during the whole experiment via complex Morlet wavelets with a variable number of cycles, linearly increasing between 3 cycles (at 1 Hz) to 6 cycles (at 29 Hz) in 29 steps for the low-frequency range, and from 6 cycles (at 30 Hz) to 12 cycles (at 150 Hz) in 25 steps for the high-frequency range.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, FreeSurfer]

### Cerebellar Purkinje cells can differentially modulate coherence between sensory and motor cortex depending on region and behavior. (PNAS 2021)

- DOI: 10.1073/pnas.2015292118 | PMCID: PMC7812746 | PMID: 33443203
- Evidence: Phase-coherence analysis was computed using the FieldTrip toolbox ( SI Appendix , Supplementary Methods ).
- Full pipeline: stage not stated [FieldTrip]

### Shaping overnight consolidation via slow-oscillation closed-loop targeted memory reactivation. (PNAS 2022)

- DOI: 10.1073/pnas.2123428119 | PMCID: PMC9636934 | PMID: 36279449
- Evidence: All data analyses were performed in MATLAB (Version 2018b) and with the Fieldtrip toolbox.
- Full pipeline: stage not stated [FieldTrip]

### Sleep deprivation and hippocampal ripple disruption after one-session learning eliminate memory expression the next day. (PNAS 2022)

- DOI: 10.1073/pnas.2123424119 | PMCID: PMC9636927 | PMID: 36279444
- Evidence: All data analysis was performed with custom scripts ( 48 ) and standard scripts from the community (e.g., Fieldtrip ( 49 ), FMA Toolbox); for the other analyses and more details, please see SI Appendix , SI Methods .
- Full pipeline: stage not stated [FieldTrip]

### Temporal scaling of human scalp-recorded potentials. (PNAS 2022)

- DOI: 10.1073/pnas.2214638119 | PMCID: PMC9618087 | PMID: 36256817
- Evidence: For each electrode, we defined a cluster by identifying neighboring electrodes according to a template available in the FieldTrip toolbox ( 61 ).
- Full pipeline: dimensionality reduction/clustering [FieldTrip] -> stage not stated [EEGLAB]

### A hierarchy of linguistic predictions during natural language comprehension. (PNAS 2022)

- DOI: 10.1073/pnas.2201968119 | PMCID: PMC9371745 | PMID: 35921434
- Evidence: To estimate the source time series from the MEG data, we used linearly constrained minimum variance beam forming, performed separately for each session, using Fieldtrip’s ft _ sourceanalysis routine.
- Full pipeline: alignment/mapping [Connectome Workbench, FreeSurfer] -> structure determination [Connectome Workbench, FreeSurfer] -> machine learning [FieldTrip] -> stage not stated [FSL]

### Cardiac sympathetic-vagal activity initiates a functional brain-body response to emotional arousal. (PNAS 2022)

- DOI: 10.1073/pnas.2119599119 | PMCID: PMC9173754 | PMID: 35588453
- Evidence: The process was performed using MATLAB R2018b (MathWorks) and Fieldtrip Toolbox ( 35 ).
- Full pipeline: stage not stated [FieldTrip]

### Optimal deep brain stimulation sites and networks for cervical vs. generalized dystonia. (PNAS 2022)

- DOI: 10.1073/pnas.2114985119 | PMCID: PMC9168456 | PMID: 35357970
- Evidence: Electric fields (E-fields) were estimated in native space based on the long-term DBS settings applied using an adaptation of the SimBio/FieldTrip pipeline ( 32 ), as implemented in Lead-DBS ( 20 ).
- Full pipeline: normalisation [ANTs] -> stage not stated [FieldTrip]

### Temporal-spectral signaling of sensory information and expectations in the cerebral processing of pain. (PNAS 2022)

- DOI: 10.1073/pnas.2116616119 | PMCID: PMC8740684 | PMID: 34983852
- Evidence: Finally, data were exported to Matlab (version R2019b, Mathworks), and further analyses were performed using FieldTrip [version 20200128 ( 78 )].
- Full pipeline: stage not stated [FieldTrip, R]

### Transcranial stimulation of alpha oscillations up-regulates the default mode network. (PNAS 2022)

- DOI: 10.1073/pnas.2110868119 | PMCID: PMC8740757 | PMID: 34969856
- Evidence: Source-level analysis of alpha activity was performed using the Fieldtrip toolbox implemented in the Statistical Parametric Mapping Software, 12th Edition (SPM12 ) ( 55 ) , with the head model defined by each participant’s T1 scan.
- Full pipeline: alignment/mapping [FieldTrip, SPM] -> differential/statistical testing [FieldTrip, SPM]

### Causal evidence for a coordinated temporal interplay within the language network. (PNAS 2023)

- DOI: 10.1073/pnas.2306279120 | PMCID: PMC10666120 | PMID: 37963247
- Evidence: EEG data were preprocessed offline using the FieldTrip toolbox ( 139 ) in Matlab (The Mathworks, USA).
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [EEGLAB, FieldTrip, emmeans]

### Subspace partitioning in the human prefrontal cortex resolves cognitive interference. (PNAS 2023)

- DOI: 10.1073/pnas.2220523120 | PMCID: PMC10334727 | PMID: 37399398
- Evidence: 3D electrode coordinates were determined using the Fieldtrip toolbox ( 51 ) on the CT scan.
- Full pipeline: stage not stated [FieldTrip, FreeSurfer v5.3.0]

### Neural representations of the content and production of human vocalization. (PNAS 2023)

- DOI: 10.1073/pnas.2219310120 | PMCID: PMC10265962 | PMID: 37253014
- Evidence: All analyses were performed using the Fieldtrip toolbox ( 46 ) and custom code in MATLAB.
- Full pipeline: stage not stated [FieldTrip]

### Human brain effects of DMT assessed via EEG-fMRI. (PNAS 2023)

- DOI: 10.1073/pnas.2218949120 | PMCID: PMC10068756 | PMID: 36940333
- Evidence: The following preprocessing steps were performed using the Fieldtrip software ( 79 ): The data were demeaned, band-pass filtered at 1 to 45 Hz, and epoched in separate 2-s trials.
- Full pipeline: normalisation [ANTs, FSL] -> registration [AFNI, ANTs, FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Breathing orchestrates synchronization of sleep oscillations in the human hippocampus. (PNAS 2024)

- DOI: 10.1073/pnas.2405395121 | PMCID: PMC11670218 | PMID: 39680758
- Evidence: Data analyses were conducted in MATLAB (MathWorks Inc.) (RRID:SCR_001622) using custom code and functions from the FieldTrip toolbox ( 94 ) ( RRID :SCR_004849) and the CircStat toolbox ( 95 ).
- Full pipeline: registration [FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Differential neural mechanisms underlie cortical gating of visual spatial attention mediated by alpha-band oscillations. (PNAS 2024)

- DOI: 10.1073/pnas.2313304121 | PMCID: PMC11551340 | PMID: 39471220
- Evidence: All analyses were performed offline using EEGLAB ( 69 ), FieldTrip ( 70 ), and customized scripts written in MATLAB.
- Full pipeline: alignment/mapping [SPM] -> structure determination [SPM] -> stage not stated [EEGLAB, FieldTrip]

### Adolescent alcohol consumption predicted by differences in electrophysiological functional connectivity and neuroanatomy. (PNAS 2024)

- DOI: 10.1073/pnas.2320805121 | PMCID: PMC11494299 | PMID: 39378092
- Evidence: Afterward, Fieldtrip software ( 30 ) was used on Matlab R2020b to automatically detect artifacts in the signal that were visually confirmed by an MEG expert.
- Full pipeline: stage not stated [FieldTrip, FreeSurfer]

### Entrainment echoes in the cerebellum. (PNAS 2024)

- DOI: 10.1073/pnas.2411167121 | PMCID: PMC11348099 | PMID: 39136991
- Evidence: MEG data were further processed using the FieldTrip software ( 55 ) as well as custom-built scripts, both implemented in MATLAB (The MathWorks, Inc.).
- Full pipeline: stage not stated [FieldTrip]

### Beta and theta oscillations track effort and previous reward in the human basal ganglia and prefrontal cortex during decision making. (PNAS 2024)

- DOI: 10.1073/pnas.2322869121 | PMCID: PMC11295073 | PMID: 39047043
- Evidence: Preprocessing, temporal alignment of behavioral and neural data, and analyses of behavioral and neural data used the Fieldtrip toolbox ( 110 ) and custom code (MATLAB, MathWorks).
- Full pipeline: alignment/mapping [FieldTrip] -> structure determination [FreeSurfer]

### Information structure in Makhuwa: Electrophysiological evidence for a universal processing account. (PNAS 2024)

- DOI: 10.1073/pnas.2315438121 | PMCID: PMC11287159 | PMID: 39028693
- Evidence: All EEG data processing was carried out using the FieldTrip toolbox ( 23 ) running in Matlab (R2020b; Mathworks, Inc.).
- Full pipeline: stage not stated [FieldTrip]

### Dynamic brain communication underwriting face pareidolia. (PNAS 2024)

- DOI: 10.1073/pnas.2401196121 | PMCID: PMC11032489 | PMID: 38588422
- Evidence: MEG data analysis was conducted with in-house MATLAB scripts (version, MATLAB 2020a; The MathWorks Inc., Natick, MA) and the Fieldtrip toolbox [version, fieldtrip-20201229; ( 64 )].
- Full pipeline: stage not stated [FieldTrip]

### Neural synchrony links sensorimotor cortices in a network for facial motor control. (PNAS 2025)

- DOI: 10.1073/pnas.2512604122 | PMCID: PMC12772211 | PMID: 41433067
- Evidence: We measured functional connectivity between the pairs of recorded areas by computing the PPC measurement as implemented in Fieldtrip ( 25 , 65 ).
- Full pipeline: stage not stated [FieldTrip]

### Cortical tracking of sign language: The role of language knowledge in tracking of different articulators. (PNAS 2025)

- DOI: 10.1073/pnas.2512665122 | PMCID: PMC12745750 | PMID: 41397120
- Evidence: Subsequent analyses were performed using MatlabR2012b (Mathworks, Natick, MA) and Fieldtrip toolbox ( 29 ).
- Full pipeline: normalisation [SPM] -> stage not stated [FieldTrip, FreeSurfer]

### Interoception vs. Exteroception: Cardiac interoception competes with tactile perception, yet also facilitates self-relevance encoding. (PNAS 2025)

- DOI: 10.1073/pnas.2516229122 | PMCID: PMC12704728 | PMID: 41329741
- Evidence: Offline preprocessing and analysis of behavioral, physiological, and neural data was done using the Fieldtrip toolbox implemented in Matlab ( 58 ) and additional custom-built Matlab code.
- Full pipeline: structure determination [Brainstorm] -> stage not stated [FieldTrip, Psychtoolbox]

### Cardiac signals inform auditory regularity processing in the absence of consciousness. (PNAS 2025)

- DOI: 10.1073/pnas.2505454122 | PMCID: PMC12107109 | PMID: 40354541
- Evidence: Data were analyzed in MATLAB (R2019b, The MathWorks, Natick, MA) using open-source toolboxes EEGLAB [13.4.4b, ( 53 )], Fieldtrip [20201205, ( 54 )] and custom-made scripts.
- Full pipeline: stage not stated [EEGLAB, FieldTrip]

### Temporal autocorrelation is predictive of age-An extensive MEG time-series analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411098122 | PMCID: PMC11873822 | PMID: 39977317
- Version used: **3.5**
- Evidence: Leadfields and individual head models were computed using the “single shell” method implemented in Fieldtrip.
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer v6.0.0, SUMA] -> stage not stated [FieldTrip v3.5]

### Precision data-driven modeling of cortical dynamics reveals person-specific mechanisms underpinning brain electrophysiology. (PNAS 2025)

- DOI: 10.1073/pnas.2409577121 | PMCID: PMC11761305 | PMID: 39823302
- Evidence: We reduced the 3d forward model to a single dipole direction per vertex by assuming that dipoles are oriented normal to the cortical surface (as calculated in FieldTrip using the vertex cross-product method).
- Full pipeline: stage not stated [FieldTrip]

### Engaging dystonia networks with subthalamic stimulation. (PNAS 2025)

- DOI: 10.1073/pnas.2417617122 | PMCID: PMC11745339 | PMID: 39773021
- Evidence: Finally, based on clinical stimulation protocols and electrode localizations, distributions of the induced electric fields were computed using the SimBio/FieldTrip pipeline ( https://www.mrt.uni-jena.de/simbio/ ; http://fieldtriptoolbox.org/ ) ( 39 ) to solve the static formulation of Maxwell’s equations using the Finite Element Method.
- Full pipeline: normalisation [ANTs] -> stage not stated [FieldTrip]

### Human brain dynamics are shaped by rare long-range connections over and above cortical geometry. (PNAS 2025)

- DOI: 10.1073/pnas.2415102122 | PMCID: PMC11725837 | PMID: 39752525
- Evidence: A custom MATLAB script, utilizing the “ft_read_cifti” function from the Fieldtrip toolbox, was employed to extract the average time series of all grayordinates in each region defined by the Glasser360 parcellations (180 regions per hemisphere) in the HCP CIFTI grayordinates standard space.
- Full pipeline: stage not stated [Connectome Workbench, FSL, FieldTrip, FreeSurfer]

### Human hippocampal theta-gamma coupling coordinates sequential planning during navigation. (PNAS 2026)

- DOI: 10.1073/pnas.2513547123 | PMCID: PMC12956831 | PMID: 41758661
- Evidence: MEG data were preprocessed using SPM12 ( 44 ), Fieldtrip ( 45 ), and custom MATLAB code.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, SPM]

