# Psychtoolbox

- **Category:** neuro-tools
- **Papers in survey:** 41
- **Journals:** PNAS (24), Nature (15), Cell (2)
- **Years:** 2021 (1), 2022 (2), 2023 (7), 2024 (14), 2025 (15), 2026 (2)
- **Versions named:** 3.0.9 (1), 3.0.18 (1), 3.0.16 (1), 3.0.11 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (1), visualisation (1), differential/statistical testing (1)

## Papers

### Fine-grained descending control of steering in walking Drosophila. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.033 | PMCID: PMC12778575 | PMID: 39293446
- Evidence: ...10.5281/zenodo.12775493 MATLAB 2018a, 2020b, and 2021b MathWorks RRID: SCR_001622 R version 4.2.2 R Project for Statistical Computing RRID:SCR_001905 Psychtoolbox-3 refs 114 , 115 http://psychtoolbox.org/ Other matte black spray paint Grainger Tough Guy 4WGC1 302 stainless steel foil with etched teardrop-shaped hole Etchit github.com/wilson-lab/design-files UV-cured glue Henkel Adhesives Loctite A...
- Full pipeline: differential/statistical testing [Psychtoolbox, R v4.2.2]

### Imaging high-frequency voltage dynamics in multiple neuron classes of behaving mammals. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.028 | PMCID: PMC12616578 | PMID: 40675148
- Evidence: We used custom software developed with the Psychtoolbox in MATLAB (MathWorks) to display drifting gratings (sine waves of 1 Hz temporal frequency, 0.033 cycle per degree of spatial frequency and 100% contrast, oriented at 315° to horizontal).
- Full pipeline: dimensionality reduction/clustering [DeepLabCut v2.2.1] -> machine learning [DeepLabCut v2.2.1] -> stage not stated [Psychtoolbox]

### Brain-phenotype models fail for individuals who defy sample stereotypes. (Nature 2022)

- DOI: 10.1038/s41586-022-05118-w | PMCID: PMC9433326 | PMID: 36002572
- Evidence: Tasks were presented using Psychtoolbox-3 77 .
- Full pipeline: registration [FSL, SPM] -> stage not stated [Psychtoolbox]

### A single photoreceptor splits perception and entrainment by cotransmission. (Nature 2023)

- DOI: 10.1038/s41586-023-06681-6 | PMCID: PMC10651484 | PMID: 37880372
- Evidence: Visual stimuli were presented through a DMD projector (DLP4710EVM-LC, Texas Instruments) controlled by Psychtoolbox 3.
- Full pipeline: visualisation [ImageJ] -> stage not stated [Psychtoolbox]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: Visual stimuli were coded with Psychtoolbox (MATLAB, MathWorks), presented on a 27 inch monitor, and consisted of a spherically corrected bar 12.5° in width moving at 10° s −1 horizontally or vertically in either direction.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### Intermittent rate coding and cue-specific ensembles support working memory. (Nature 2024)

- DOI: 10.1038/s41586-024-08139-9 | PMCID: PMC11634780 | PMID: 39506106
- Evidence: Behavioural task Stimuli were presented on a VIEWPixx3D monitor positioned at a viewing distance of 60 cm using Psychtoolbox and MATLAB (v.R2022a, MathWorks).
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [Psychtoolbox]

### Dynamic interface printing. (Nature 2024)

- DOI: 10.1038/s41586-024-08077-6 | PMCID: PMC11525192 | PMID: 39478212
- Evidence: The image stack was further corrected using the convex-slicing algorithm to produce a secondary optimized image stack, with the sequence being sent to the projector over HDMI using Psychtoolbox-3 (ref.
- Full pipeline: stage not stated [ImageJ, Psychtoolbox]

### Connectomic reconstruction predicts visual features used for navigation. (Nature 2024)

- DOI: 10.1038/s41586-024-07967-z | PMCID: PMC11446847 | PMID: 39358517
- Evidence: Visual stimuli were drawn and displayed by Psychtoolbox-3.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Psychtoolbox, SciPy]

### Calcium-permeable AMPA receptors govern PV neuron feature selectivity. (Nature 2024)

- DOI: 10.1038/s41586-024-08027-2 | PMCID: PMC11560848 | PMID: 39358515
- Evidence: Six orientation gratings spaced at 30° were presented drifting in both directions orthogonal to the gratings (total of 12 directions) in a pseudo-randomized order to characterize sensory tuning using Psychtoolbox-3 (ref.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> stage not stated [DESeq2, ImageJ, Psychtoolbox, SciPy]

### Flexible perceptual encoding by discrete gamma events. (Nature 2025)

- DOI: 10.1038/s41586-025-09604-9 | PMCID: PMC12657229 | PMID: 41062693
- Evidence: Visual stimulation and behavioural hardware Visual stimuli were generated using the Psychtoolbox MATLAB extension 70 and displayed on a 17″ × 9.5″ monitor situated 20 cm in front of the animal (visual detection task) or 15 cm from the right eye (all other behavioural tasks; passive visual stimulation).
- Full pipeline: dimensionality reduction/clustering [NumPy v1.11.3, UMAP] -> stage not stated [Psychtoolbox]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: We programmed visual stimuli with Psychtoolbox-3 for Matlab 61 , 62 and displayed them on an LCD monitor from above the arena.
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### The dynamics and geometry of choice in the premotor cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-09199-1 | PMCID: PMC12408350 | PMID: 40562938
- Version used: **3.0.9**
- Evidence: This system communicated with a separate computer running Psychtoolbox (v3.0.9) on MATLAB R2012b for stimulus display.
- Full pipeline: stage not stated [Brian2, Psychtoolbox v3.0.9, SciPy]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: Looming visual stimuli were generated using Psychtoolbox as previously mentioned.
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Evidence: Data acquisition Behavioural data acquisition The task was run on Matlab (PKU: R2018b; DCCN, UB and Yale: R2019b; Harvard: R2020b; NYU: R2020a, and WU: 2021a) using Psychtoolbox (v3) 66 .
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Foundation model of neural activity predicts response to new stimulus types. (Nature 2025)

- DOI: 10.1038/s41586-025-08829-y | PMCID: PMC11981942 | PMID: 40205215
- Evidence: Monitor positioning and calibration Visual stimuli were presented with Psychtoolbox in MATLAB to the left eye with a 31.0 × 55.2 cm (height × width) monitor (ASUS PB258Q) with a resolution of 1,080 × 1,920 pixels positioned 15 cm away from the eye.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut] -> visualisation [UMAP] -> stage not stated [Psychtoolbox]

### Basis functions for complex social decisions in dorsomedial frontal cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08705-9 | PMCID: PMC12074988 | PMID: 40074892
- Evidence: The behavioural pre-experiment that took place before scanning and the fMRI experiment were programmed in Matlab using Psychtoolbox-3 (ref.
- Full pipeline: stage not stated [FSL, Psychtoolbox, jsPsych]

### Building compositional tasks with shared neural subspaces. (Nature 2026)

- DOI: 10.1038/s41586-025-09805-2 | PMCID: PMC12872450 | PMID: 41299181
- Evidence: The stimuli were rendered as three-dimensional models using POV-Ray and MATLAB (MathWorks) and displayed using Psychtoolbox on a Dell U2413 LCD monitor positioned 58 cm from the animal.
- Full pipeline: dimensionality reduction/clustering [Psychtoolbox] -> visualisation [Psychtoolbox]

### How multisensory neurons solve causal inference. (PNAS 2021)

- DOI: 10.1073/pnas.2106235118 | PMCID: PMC8364184 | PMID: 34349023
- Version used: **3.0.11**
- Evidence: Image translation, motion-in-depth, and rotation were performed in MATAB using Psychtoolbox version 3.0.11 subpixel rendering extensions ( 41 , 42 ) ( http://psychtoolbox.org/ ).
- Full pipeline: stage not stated [Psychtoolbox v3.0.11, Python v3.6.4, TensorFlow]

### Unlocking adults' implicit statistical learning by cognitive depletion. (PNAS 2022)

- DOI: 10.1073/pnas.2026011119 | PMCID: PMC8764693 | PMID: 34983868
- Evidence: The task was run in Matlab2016b/Psychtoolbox on a Dell laptop (refresh rate, 60 Hz).
- Full pipeline: stage not stated [EEGLAB, Psychtoolbox, R, afex, emmeans, lme4]

### The perception of auditory motion in sighted and early blind individuals. (PNAS 2023)

- DOI: 10.1073/pnas.2310156120 | PMCID: PMC10710053 | PMID: 38015842
- Evidence: The stimuli were generated and presented using MATLAB and Psychtoolbox ( 69 ).
- Full pipeline: stage not stated [Psychtoolbox]

### Different roles of response covariability and its attentional modulation in the sensory cortex and posterior parietal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2216942120 | PMCID: PMC10589615 | PMID: 37812698
- Evidence: The grating stimulus was generated via the Psychtoolbox ( http://psychtoolbox.org/ ) and MATLAB (MathWorks, Natick, MA, USA) using a Mac Pro (Late 2013).
- Full pipeline: stage not stated [FreeSurfer, Psychtoolbox, SUMA]

### Acetylcholine and noradrenaline enhance foraging optimality in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2305596120 | PMCID: PMC10483619 | PMID: 37639601
- Evidence: The task was run in Psychtoolbox ( 108 ) and adopted from Le Heron et al.
- Full pipeline: differential/statistical testing [brms, emmeans] -> stage not stated [Psychtoolbox]

### Deriving the number of salience maps an observer has from the number and quality of concurrent centroid judgments. (PNAS 2023)

- DOI: 10.1073/pnas.2301707120 | PMCID: PMC10214162 | PMID: 37186842
- Evidence: The experiment was conducted on an iMac intel computer installed with MATLAB 2018b and Psychtoolbox-3 software.
- Full pipeline: stage not stated [Psychtoolbox]

### Confidence of probabilistic predictions modulates the cortical response to pain. (PNAS 2023)

- DOI: 10.1073/pnas.2212252120 | PMCID: PMC9942789 | PMID: 36669115
- Evidence: The synchronization of the stimuli, triggers on the EEG, and behavioral questions was performed with the Data Acquisition Toolbox and Psychtoolbox running on Matlab.
- Full pipeline: stage not stated [Psychtoolbox]

### What can the eye see with melanopsin? (PNAS 2024)

- DOI: 10.1073/pnas.2411151121 | PMCID: PMC11621463 | PMID: 39570305
- Evidence: Stimuli are generated on a controlling computer in MATLAB using a combination of Psychtoolbox ( 40 ) and custom developed OpenGL graphics shaders.
- Full pipeline: stage not stated [Psychtoolbox]

### Leader-follower dynamics during early social interactions matter for infant word learning. (PNAS 2024)

- DOI: 10.1073/pnas.2321008121 | PMCID: PMC11420154 | PMID: 39254996
- Evidence: At the same time, audio recordings were started at the beginning of each trial and stopped at the end of each trial with the same MATLAB script using the audio functions of the Psychtoolbox package.
- Full pipeline: normalisation [Python] -> stage not stated [EEGLAB, Psychtoolbox]

### The neural basis of swap errors in working memory. (PNAS 2024)

- DOI: 10.1073/pnas.2401032121 | PMCID: PMC11331092 | PMID: 39102534
- Evidence: The behavioral task was implemented in Psychtoolbox and MATLAB (Mathworks) and it was displayed on a Dell U2413 liquid crystal display (LCD) monitor, which the monkeys viewed at a distance of 58 cm.
- Full pipeline: stage not stated [Psychtoolbox, Stan, scikit-learn]

### Spontaneous eye movements reflect the representational geometries of conceptual spaces. (PNAS 2024)

- DOI: 10.1073/pnas.2403858121 | PMCID: PMC11046636 | PMID: 38635638
- Evidence: Participants’ voice was recorded using custom Psychtoolbox functions in the MATLAB environment, via the built-in microphone of the earphones used to present sounds.
- Full pipeline: stage not stated [Psychtoolbox]

### How small changes to one eye's retinal image can transform the perceived shape of a very familiar object. (PNAS 2024)

- DOI: 10.1073/pnas.2400086121 | PMCID: PMC11046684 | PMID: 38621132
- Version used: **3.0.18**
- Evidence: All stimuli were presented with Psychtoolbox version 3.0.18 in MATLAB (MATLAB R2022a; The MathWorks, Natick, MA).
- Full pipeline: stage not stated [Psychtoolbox v3.0.18]

### Brain decoding of spontaneous thought: Predictive modeling of self-relevance and valence using personal narratives. (PNAS 2024)

- DOI: 10.1073/pnas.2401959121 | PMCID: PMC10998624 | PMID: 38547065
- Version used: **3.0.16**
- Evidence: We used MATLAB (MathWorks) and Psychtoolbox (version 3.0.16, http://psychtoolbox.org/ ) for stimuli presentation and behavioral data acquisition.
- Full pipeline: stage not stated [Psychtoolbox v3.0.16]

### The reach of reactivation: Effects of consciously triggered versus unconsciously triggered reactivation of associative memory. (PNAS 2024)

- DOI: 10.1073/pnas.2313604121 | PMCID: PMC10927514 | PMID: 38408248
- Evidence: Stimuli were presented on a 20.75 × 11.67 inch Dell P2417H screen, controlled by Matlab2020b code using the Psychtoolbox-3 toolbox ( 49 ).
- Full pipeline: stage not stated [Psychtoolbox]

### Sleep shapes the associative structure underlying pattern completion in multielement event memory. (PNAS 2024)

- DOI: 10.1073/pnas.2314423121 | PMCID: PMC10907255 | PMID: 38377208
- Evidence: Behavioral data were acquired using MATLAB/Psychtoolbox (RRID:SCR_002881; refs.
- Full pipeline: differential/statistical testing [R] -> stage not stated [Psychtoolbox]

### Inactivation of face-selective neurons alters eye movements when free viewing faces. (PNAS 2024)

- DOI: 10.1073/pnas.2309906121 | PMCID: PMC10801883 | PMID: 38198528
- Evidence: The images were displayed using Psychtoolbox ( 66 , 67 ) and the PLDAPS toolbox ( 68 ) in MATLAB (MathWorks, version R2018b).
- Full pipeline: stage not stated [AFNI, Psychtoolbox]

### Interoception vs. Exteroception: Cardiac interoception competes with tactile perception, yet also facilitates self-relevance encoding. (PNAS 2025)

- DOI: 10.1073/pnas.2516229122 | PMCID: PMC12704728 | PMID: 41329741
- Evidence: The task was presented with Matlab 2017b ( 52 ) using the Psychtoolbox ( 53 ), running on a MacBook Air stimulation laptop.
- Full pipeline: structure determination [Brainstorm] -> stage not stated [FieldTrip, Psychtoolbox]

### Automaticity speeds the retrieval of instances from the human hippocampus. (PNAS 2025)

- DOI: 10.1073/pnas.2518523122 | PMCID: PMC12595489 | PMID: 41166430
- Evidence: The experimental script for stimulus presentation and behavioral data collection was written in Psychtoolbox ( 44 ) on MATLAB (version 2021b; The MathWorks Inc., Natick, MA).
- Full pipeline: stage not stated [EEGLAB, FreeSurfer v6.0.0, Psychtoolbox]

### Micro-offline gains do not reflect offline learning during early motor skill acquisition in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2509233122 | PMCID: PMC12595466 | PMID: 41150724
- Evidence: Stimuli for Experiments 1 and 3-5 were presented using MATLAB (R2021b, The MathWorks, Inc., Natick, Massachusetts, United States) and Psychtoolbox ( 48 ), whereas Experiment 2 (the online study) was programmed in PscyhoPy ( 49 ) and conducted on Pavlovia ( www.pavlovia.org ), with participants recruited via Prolific ( www.prolific.com ).
- Full pipeline: stage not stated [Psychtoolbox]

### Motor expertise modulates cortical activation during imagery of simple and complex actions. (PNAS 2025)

- DOI: 10.1073/pnas.2515027122 | PMCID: PMC12501113 | PMID: 40982676
- Evidence: Participants in each experiment completed three MI conditions using a block design implemented in MATLAB (2020b) with Psychtoolbox.
- Full pipeline: stage not stated [Psychtoolbox]

### A hierarchy of processing complexity and timescales for natural sounds in the human auditory cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2412243122 | PMCID: PMC12067213 | PMID: 40294254
- Evidence: The experiment was run using Psychtoolbox-3 and custom MATLAB code.
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox]

### Broken time-reversal symmetry in visual motion detection. (PNAS 2025)

- DOI: 10.1073/pnas.2410768122 | PMCID: PMC11912477 | PMID: 40048271
- Evidence: Stimuli were presented using custom code written in Psychtoolbox ( 52 – 54 ) running on MATLAB (Natick, MA) and the turning response was summarized for each fly by averaging its turning over the stimulus presentation period.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Psychtoolbox]

### The origin of color categories. (PNAS 2025)

- DOI: 10.1073/pnas.2400273121 | PMCID: PMC11725794 | PMID: 39793082
- Evidence: The experiment was controlled with custom software written in MATLAB and Psychtoolbox ( 60 ).
- Full pipeline: stage not stated [Psychtoolbox]

### Individual differences in speech monitoring: Functional and structural correlates of delayed auditory feedback. (PNAS 2026)

- DOI: 10.1073/pnas.2530123123 | PMCID: PMC13321129 | PMID: 42330290
- Evidence: Stimulus presentation was executed using MATLAB Psychtoolbox-3 running on an HP Intel Core i7 laptop with a Windows 10 operating system.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox, SPM, fMRIPrep v23.1.0]

