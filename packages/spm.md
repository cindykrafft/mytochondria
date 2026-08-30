# SPM

- **Category:** neuroimaging
- **Papers in survey:** 76
- **Journals:** PNAS (65), Nature (8), Cell (3)
- **Years:** 2021 (8), 2022 (14), 2023 (13), 2024 (17), 2025 (19), 2026 (5)
- **Pipeline stages it appears in:** differential/statistical testing (35), alignment/mapping (29), normalisation (9), registration (7), structure determination (4), dimensionality reduction/clustering (1), visualisation (1), variant calling (1), simulation/modelling (1), quantification (1)

## Papers

### Impaired neural replay of inferred relationships in schizophrenia. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.012 | PMCID: PMC8357425 | PMID: 34197734
- Evidence: MEG pre-processing, time-frequency analysis and source reconstruction was performed using MATLAB in conjunction with functions from the Statistical Parametric Mapping 12 (SPM12, https://www.fil.ion.ucl.ac.uk/spm/software/spm12/ ) toolbox, FieldTrip ( https://www.fieldtriptoolbox.org/ ), the OHBA Software Library (OSL, including OAT, https://ohba-analysis.github.io/osl-docs/ ) and FMRIB Software Li...
- Full pipeline: alignment/mapping [FieldTrip, SPM] -> differential/statistical testing [FieldTrip, SPM] -> structure determination [FieldTrip, SPM] -> stage not stated [FSL]

### Generative replay underlies compositional inference in the hippocampal-prefrontal circuit. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.004 | PMCID: PMC10914680 | PMID: 37804832
- Evidence: Pre-processing All pre-processing steps and subsequent imaging analyses were performed with SPM12 (Wellcome Trust Centre for Neuroimaging, http://www.fil.ion.ucl.ac.uk/spm ).
- Full pipeline: stage not stated [SPM]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Voxels with p < 0.05 (t value threshold 1.78, uncorrected for multiple comparisons) are projected on the SPM12 skull surface template.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Brain-phenotype models fail for individuals who defy sample stereotypes. (Nature 2022)

- DOI: 10.1038/s41586-022-05118-w | PMCID: PMC9433326 | PMID: 36002572
- Evidence: Motion correction was performed in SPM12 107 .
- Full pipeline: registration [FSL, SPM] -> stage not stated [Psychtoolbox]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: This software uses SPM12 ( https://www.fil.ion.ucl.ac.uk/spm/software/spm12/ ) to perform tissue segmentation and normalization of individual scans to Montreal Neurological Institute (MNI) template space.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### An orexigenic subnetwork within the human hippocampus. (Nature 2023)

- DOI: 10.1038/s41586-023-06459-w | PMCID: PMC10499606 | PMID: 37648849
- Evidence: ...lysis rsRC analysis was performed on the binge-eating-prone cohort’s preprocessed resting-state fMRI data using DPABI/DPARSF v.4.3, which is based on Statistical Parametric Mapping (SPM, v.12, https://www.fil.ion.ucl.ac.uk/spm ) 77 .
- Full pipeline: alignment/mapping [SPM] -> normalisation [ANTs v2.1.0] -> registration [ANTs v2.1.0] -> differential/statistical testing [SPM] -> stage not stated [FSL, FieldTrip, Python v3.6, fMRIPrep v1.2.3]

### Human hippocampal and entorhinal neurons encode the temporal structure of experience. (Nature 2024)

- DOI: 10.1038/s41586-024-07973-1 | PMCID: PMC11540853 | PMID: 39322671
- Evidence: Second, the MRI image was: (1) segmented into the grey matter, white matter, and cerebrospinal fluid probability maps; (2) resampled (1 × 1 × 1 mm voxel size); and (3) normalized to the 152 T1-weighted MNI template using the nonlinear transformation algorithm implemented in the Statistical Parametric Mapping toolbox (SPM12, Wellcome Department of Cognitive Neurology, London, UK).
- Full pipeline: alignment/mapping [SPM] -> normalisation [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL]

### Semantic encoding during language comprehension at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07643-2 | PMCID: PMC11254762 | PMID: 38961302
- Evidence: Recording locations were then confirmed using SPM12 software and were visualized on a standard three-dimensional rendered brain (spm152).
- Full pipeline: dimensionality reduction/clustering [SPM] -> visualisation [SPM] -> stage not stated [Kilosort, Python]

### Cocaine chemogenetics blunts drug-seeking by synthetic physiology. (Nature 2025)

- DOI: 10.1038/s41586-025-09427-8 | PMCID: PMC12527922 | PMID: 40866713
- Evidence: All statistical parametric mapping (SPM) analyses were performed using MATLAB R2016 (MathWorks) and SPM12 (University College London) 62 .
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [PyMOL]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Evidence: Analysis-specific functional preprocessing Additional, analysis-specific, fMRI data preprocessing was performed using FSL 6.0.2 (FMRIB Software Library) 94 , Statistical Parametric Mapping (SPM 12) software 95 , and custom Python scripts (using NiBabel (3.2.2) 96 and SciPy (1.8.0) 97 after the above-outlined general preprocessing.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Phase I trial of hES cell-derived dopaminergic neurons for Parkinson's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08845-y | PMCID: PMC12095069 | PMID: 40240592
- Evidence: Mean image derivation in the standard brain space 18 F-DOPA PET images for each participant were realigned across individual time frames and then registered together to the high-resolution T1 structural MRI scan (see below) using SPM12 software ( https://www.fil.ion.ucl.ac.uk/spm ).
- Full pipeline: registration [SPM] -> stage not stated [FSL]

### The middle cingulate cortex and dorso-central insula: A mirror circuit encoding observation and execution of vitality forms. (PNAS 2021)

- DOI: 10.1073/pnas.2111358118 | PMCID: PMC8612212 | PMID: 34716272
- Evidence: In the first level, the fMRI BOLD signal of each participant was modeled using two general linear models (GLMs), and analysis was carried out using SPM12 software (the Wellcome Department of Imaging Neuroscience).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [FSL]

### Testing models at the neural level reveals how the brain computes subjective value. (PNAS 2021)

- DOI: 10.1073/pnas.2106237118 | PMCID: PMC8639327 | PMID: 34686596
- Evidence: Using statistical parametric mapping (SPM12; Functional Imaging Laboratory, University College London) we performed slice timing correction, spatial realignment, normalization to the standard echo-planar imaging template and spatial smoothing using an isometric Gaussian kernel with a full-width at half-maximum (FWHM) of 10 mm.
- Full pipeline: alignment/mapping [SPM] -> normalisation [SPM] -> registration [SPM] -> differential/statistical testing [R, SPM]

### Altered effective connectivity in sensorimotor cortices is a signature of severity and clinical course in depression. (PNAS 2021)

- DOI: 10.1073/pnas.2105730118 | PMCID: PMC8501855 | PMID: 34593640
- Evidence: The preprocessing and statistical analysis of fMRI data were executed with the SPM12 v7771 toolbox (Statistical Parametric Mapping, https://www.fil.ion.ucl.ac.uk/spm ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM]

### Shifting gradients of macroscale cortical organization mark the transition from childhood to adolescence. (PNAS 2021)

- DOI: 10.1073/pnas.2024448118 | PMCID: PMC8285909 | PMID: 34260385
- Evidence: The CCS pipeline is designed for preprocessing multimodal MRI datasets and integrating several publicly available software such as Statistical Parametric Mapping (SPM; ref.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [AFNI, FSL, FreeSurfer]

### The impact of a lack of mathematical education on brain development and future attainment. (PNAS 2021)

- DOI: 10.1073/pnas.2013155118 | PMCID: PMC8214709 | PMID: 34099561
- Evidence: To quantify the structural properties, we segmented the images into different tissue classes including gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF) using the SPM12 segmentation facility.
- Full pipeline: quantification [SPM] -> normalisation [CONN toolbox]

### Placental genomic risk scores and early neurodevelopmental outcomes. (PNAS 2021)

- DOI: 10.1073/pnas.2019789118 | PMCID: PMC7896349 | PMID: 33558239
- Evidence: Global and regional gray matter volumes were examined with VBM ( 81 ), using the VBM toolbox ( http://dbm.neuro.uni-jena.de/vbm8/VBM8-Manual.pdf ) implemented in Statistical Parametric Mapping software (SPM12; https://www.fil.ion.ucl.ac.uk/spm/ ).
- Full pipeline: quality control [PLINK v1.07] -> alignment/mapping [SPM] -> differential/statistical testing [SPM, limma] -> stage not stated [R]

### A link between synaptic plasticity and reorganization of brain activity in Parkinson's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2013962118 | PMCID: PMC7826364 | PMID: 33431672
- Evidence: The fMRI data were analyzed using the Statistical Parametric Mapping 12 (SPM version 12) (Wellcome Centre for Human Neuroimaging, Functional Imaging Laboratory, University College London).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM]

### Age-related brain atrophy is not a homogenous process: Different functional brain networks associate differentially with aging and blood factors. (PNAS 2022)

- DOI: 10.1073/pnas.2207181119 | PMCID: PMC9894212 | PMID: 36459652
- Evidence: Tissue segmentation was achieved using SPM12’s unified segmentation procedure, and each participant’s gray matter segmentation was warped using the DARTEL (Diffeomorphic Anatomical Registration using Exponentiated Lie algebra) to create a study-specific template ( 29 ) ( 68 ).
- Full pipeline: normalisation [limma] -> registration [SPM] -> stage not stated [R]

### Neurocomputational evidence that conflicting prosocial motives guide distributive justice. (PNAS 2022)

- DOI: 10.1073/pnas.2209078119 | PMCID: PMC9897457 | PMID: 36445964
- Evidence: We used Statistical Parametric Mapping software SPM12 (Wellcome Trust Department of Cognitive Neurology, London, UK) which was run-through MATLAB (MathWorks) to preprocess the fMRI images, perform GLM analyses and PPI analyses.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM]

### A tool for monitoring cell type-specific focused ultrasound neuromodulation and control of chronic epilepsy. (PNAS 2022)

- DOI: 10.1073/pnas.2206828119 | PMCID: PMC9674244 | PMID: 36343238
- Evidence: Voxel-wise changes in uptake were assessed relative to global uptake between the stimulated and nonstimulated hemispheres in Statistical Parametric Mapping 12.
- Full pipeline: alignment/mapping [SPM] -> quantification [Python, SciPy] -> differential/statistical testing [NumPy, SPM]

### Electrophysiological markers of memory consolidation in the human brain when memories are reactivated during sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2123430119 | PMCID: PMC9636913 | PMID: 36279460
- Evidence: CT scans were registered to MRI scans using the mutual information method through the Statistical Parametric Mapping toolbox in MATLAB ( 75 ), and cortical reconstruction and volumetric segmentation was performed with Freesurfer ( 76 ).
- Full pipeline: alignment/mapping [FreeSurfer, SPM] -> differential/statistical testing [FreeSurfer, SPM] -> structure determination [FreeSurfer, SPM]

### Language and developmental plasticity after perinatal stroke. (PNAS 2022)

- DOI: 10.1073/pnas.2207293119 | PMCID: PMC9586296 | PMID: 36215488
- Evidence: MRI data were analyzed with SPM12 using default settings except where specifically mentioned, with statistical analyses in Excel and SPSS (v.27.0.1.0).
- Full pipeline: dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM]

### Mind blanking is a distinct mental state linked to a recurrent brain profile of globally positive connectivity during ongoing mentation. (PNAS 2022)

- DOI: 10.1073/pnas.2200511119 | PMCID: PMC9564098 | PMID: 36194631
- Evidence: Preprocessing and denoising were performed via a locally developed pipeline written in Python [nipype package ( 48 )] encompassing toolboxes from Statistical Parametric Mapping 12 ( 49 ), FSL 6.0 ( 50 ), AFNI ( 51 ), and ART ( http://web.mit.edu/swg/software.htm ).
- Full pipeline: alignment/mapping [AFNI, FSL v6.0, Nipype, SPM] -> differential/statistical testing [AFNI, FSL v6.0, Nipype, SPM] -> machine learning [scikit-learn] -> stage not stated [Python]

### Human cerebellum and corticocerebellar connections involved in emotional memory enhancement. (PNAS 2022)

- DOI: 10.1073/pnas.2204900119 | PMCID: PMC9564100 | PMID: 36191198
- Evidence: We used the statistical parametric mapping (SPM) software SPM12 version 6685 (Wellcome Trust Centre for Neuroimaging, London, UK; https://www.fil.ion.ucl.ac.uk/spm/ ) implemented in Matlab R2016a.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> visualisation [R] -> stage not stated [FreeSurfer v4.5]

### Breakdown of utilitarian moral judgement after basolateral amygdala damage. (PNAS 2022)

- DOI: 10.1073/pnas.2119072119 | PMCID: PMC9351380 | PMID: 35878039
- Evidence: In this method, which is implemented in the SPM8 anatomy toolbox ( https://www.fz-juelich.de/inm/inm-1/spm_anatomy_toolbox ), a volume of interest is superimposed onto a cytoarchitectonic probability map of the medial-temporal lobe ( 57 ).
- Full pipeline: stage not stated [SPM]

### Comparing human and chimpanzee temporal lobe neuroanatomy reveals modifications to human language hubs beyond the frontotemporal arcuate fasciculus. (PNAS 2022)

- DOI: 10.1073/pnas.2118295119 | PMCID: PMC9282369 | PMID: 35787056
- Evidence: DWI images were preprocessed to realign and correct for eddy current (using Statistical Parametric Mapping software - SPM12) and for artifacts from head and/or cardiac motion using robust tensor modeling [Donders Institute Diffusion Imaging toolbox ( 83 )].
- Full pipeline: alignment/mapping [SPM] -> registration [FSL v5.0.10, SPM] -> differential/statistical testing [SPM] -> stage not stated [R, tidyverse]

### The effect of learning to drum on behavior and brain function in autistic adolescents. (PNAS 2022)

- DOI: 10.1073/pnas.2106244119 | PMCID: PMC9191342 | PMID: 35639696
- Evidence: Statistical Parametric Mapping (SPM12) and the CONN functional connectivity toolbox Version 18b ( https://www.nitrc.org/projects/conn ) ( 108 ) were used to preprocess and analyze the anatomical and functional data.
- Full pipeline: alignment/mapping [CONN toolbox, SPM] -> differential/statistical testing [CONN toolbox, SPM]

### Mitigating climate disruption in time: A self-consistent approach for avoiding both near-term and long-term global warming. (PNAS 2022)

- DOI: 10.1073/pnas.2123536119 | PMCID: PMC9295773 | PMID: 35605122
- Evidence: Historical curve (past simulated warming) is from figure SPM8.a ( 47 , 64 ).
- Full pipeline: simulation/modelling [SPM]

### Neural representations of others' traits predict social decisions. (PNAS 2022)

- DOI: 10.1073/pnas.2116944119 | PMCID: PMC9295729 | PMID: 35605117
- Evidence: We first estimated voxel-wise response patterns evoked by each recipient in each scanning run using a generalized linear model (GLM) implemented in SPM12 software.
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, SPM] -> stage not stated [Python]

### Transcranial stimulation of alpha oscillations up-regulates the default mode network. (PNAS 2022)

- DOI: 10.1073/pnas.2110868119 | PMCID: PMC8740757 | PMID: 34969856
- Evidence: Source-level analysis of alpha activity was performed using the Fieldtrip toolbox implemented in the Statistical Parametric Mapping Software, 12th Edition (SPM12 ) ( 55 ) , with the head model defined by each participant’s T1 scan.
- Full pipeline: alignment/mapping [FieldTrip, SPM] -> differential/statistical testing [FieldTrip, SPM]

### Increased cortical inhibition following brief motor memory reactivation supports reconsolidation and overnight offline learning gains. (PNAS 2023)

- DOI: 10.1073/pnas.2303985120 | PMCID: PMC10756311 | PMID: 38113264
- Evidence: SPM12 (Wellcome Center for Human Neuroimaging, UCL, UK, http://www.fil.ion.ucl.ac.uk/spm ) was used to segment the T1-weighted anatomical images into gray matter (GM), white matter (WM), and cerebrospinal fluid (CSF) images.
- Full pipeline: differential/statistical testing [R v4.1] -> visualisation [R v4.1] -> stage not stated [SPM, lme4]

### Whole-brain, gray, and white matter time-locked functional signal changes with simple tasks and model-free analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2219666120 | PMCID: PMC10589709 | PMID: 37824529
- Evidence: 1 , fMRI) using the statistical parametric mapping software package SPM12 ( www.fil.ion.ucl.ac.uk/spm/software ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL, FreeSurfer]

### Neural evidence of switch processes during semantic and phonetic foraging in human memory. (PNAS 2023)

- DOI: 10.1073/pnas.2312462120 | PMCID: PMC10589708 | PMID: 37824523
- Evidence: Whole brain T1-weighted anatomical scans and four 8.5-min functional scans (repetition time: 2,000 ms) were collected on a Siemens 3T MRI system (Magnetom, Prisma Fit) with a 64-channel coil. fMRI data were processed using Statistical Parametric Mapping (SPM) version 12 (Wellcome Imaging Department, University College, London, UK).
- Full pipeline: alignment/mapping [SPM] -> dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM] -> stage not stated [Python v2.7]

### Enhanced amygdala-cingulate connectivity associates with better mood in both healthy and depressive individuals after sleep deprivation. (PNAS 2023)

- DOI: 10.1073/pnas.2214505120 | PMCID: PMC10293819 | PMID: 37339227
- Evidence: Imaging data preprocessing was performed using the Statistical Parametric Mapping software (SPM 12, Wellcome Department of Cognitive Neurology, UK) and the DPABI V6.2 toolbox ( 57 ) implemented in Matlab 2021a (Math Works, Natick, MA, USA).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM]

### Sex-specific and opposed effects of FKBP51 in glutamatergic and GABAergic neurons: Implications for stress susceptibility and resilience. (PNAS 2023)

- DOI: 10.1073/pnas.2300722120 | PMCID: PMC10266018 | PMID: 37252963
- Evidence: Smoothed Jacobian deformation fields were compared in SPM12 in an independent two-factorial model (genotype × sex) for Fkbp5 Dlx and Fkbp5 Nex mice vs. their Fkbp5 lox/lox controls, respectively.
- Full pipeline: variant calling [SPM] -> dimensionality reduction/clustering [R, clusterProfiler]

### Re-cognizing the new self: The neurocognitive plasticity of self-processing following facial transplantation. (PNAS 2023)

- DOI: 10.1073/pnas.2211966120 | PMCID: PMC10083597 | PMID: 36972456
- Evidence: SPM12 ( www.fil.ion.ucl.ac.uk ) implemented in MATLAB (v 2018a, The MathWorks, Natick, MA) was used for data preprocessing and statistical analyses.
- Full pipeline: differential/statistical testing [SPM]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Evidence: Individual voxel BOLD activation on each study trial was estimated with a general linear model (GLM) as implemented in SPM12 ( 136 ) †† using the least squares-single approach described in ref.
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Evaluating the impact of short educational videos on the cortical networks for mathematics. (PNAS 2023)

- DOI: 10.1073/pnas.2213430120 | PMCID: PMC9963232 | PMID: 36730198
- Evidence: Using SPM12 software, functional images were first realigned, normalized to the standard Montreal Neurological Institute brain space, resampled to 1.5-mm voxel size, and spatially smoothed with an isotropic Gaussian filter of 2 mm FWHM.
- Full pipeline: normalisation [SPM] -> registration [SPM]

### Spontaneous cortical dynamics from the first years to the golden years. (PNAS 2023)

- DOI: 10.1073/pnas.2212776120 | PMCID: PMC9942851 | PMID: 36652485
- Evidence: Whole-brain PSD maps per canonical band were analyzed in SPM12 to examine spatially specific effects of age and sex, and their interactions.
- Full pipeline: stage not stated [SPM, ggplot2]

### Cortisol awakening response prompts dynamic reconfiguration of brain networks in emotional and executive functioning. (PNAS 2024)

- DOI: 10.1073/pnas.2405850121 | PMCID: PMC11670246 | PMID: 39680766
- Evidence: Image preprocessing was performed using Statistical Parametric Mapping (SPM12, http://www.fil.ion.ucl.ac.uk/spm ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM]

### Intracortical recordings reveal the neuronal selectivity for bodies and body parts in the human visual cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2408871121 | PMCID: PMC11665852 | PMID: 39652751
- Evidence: For imaging preprocessing, we utilized SPM12 software (Wellcome Department of Cognitive Neurology, London, UK) running on MATLAB (Mathworks, Natick, MA).
- Full pipeline: stage not stated [FreeSurfer, Python, SPM, scikit-learn]

### Neural responses to social rejection reflect dissociable learning about relational value and reward. (PNAS 2024)

- DOI: 10.1073/pnas.2400022121 | PMCID: PMC11626180 | PMID: 39589878
- Evidence: For univariate analyses, data were additionally smoothed with an 8 mm kernel using SPM12 software.
- Full pipeline: stage not stated [SPM]

### Differential neural mechanisms underlie cortical gating of visual spatial attention mediated by alpha-band oscillations. (PNAS 2024)

- DOI: 10.1073/pnas.2313304121 | PMCID: PMC11551340 | PMID: 39471220
- Evidence: We reconstructed electrode locations by aligning a postoperative CT scan image of the implanted electrodes with a preoperative high-resolution structural MRI using SPM8 ( 67 ).
- Full pipeline: alignment/mapping [SPM] -> structure determination [SPM] -> stage not stated [EEGLAB, FieldTrip]

### Tipping the balance between fairness and efficiency through temporoparietal stimulation. (PNAS 2024)

- DOI: 10.1073/pnas.2409395121 | PMCID: PMC11494363 | PMID: 39388264
- Evidence: We analyzed the neuroimaging data with SPM12 in Matlab ( www.fil.ion.ucl.ac.uk/spm ).
- Full pipeline: differential/statistical testing [JAGS] -> stage not stated [R v4.0.0, SPM, lme4]

### Auditory cortical regions show resting-state functional connectivity with the default mode-like network in echolocating bats. (PNAS 2024)

- DOI: 10.1073/pnas.2306029121 | PMCID: PMC11228507 | PMID: 38913894
- Evidence: ( Top ) Sagittal, coronal, and axial views of a T-score map resulting from a voxel-wise comparison of BOLD signal elicited by 50 blocks of auditory stimulation (ultrasonic noise ripples) contrasted against 50 blocks of silence (SPM12) in our nine-bat population (T max = 5.57).
- Full pipeline: stage not stated [SPM]

### Characteristic BOLD signals are detectable in white matter of the spinal cord at rest and after a stimulus. (PNAS 2024)

- DOI: 10.1073/pnas.2316117121 | PMCID: PMC11145258 | PMID: 38776372
- Evidence: Analyses were performed on the spinal cords of 11 monkeys (61 runs) with a left dominant hand using GLM in SPM12 software ( 54 ).
- Full pipeline: stage not stated [FSL, SPM]

### Subthalamic nucleus-language network connectivity predicts dopaminergic modulation of speech function in Parkinson's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2316149121 | PMCID: PMC11145286 | PMID: 38768342
- Evidence: A standard preprocessing pipeline was implemented using SPM12 software package ( https://www.fil.ion.ucl.ac.uk/spm/software/spm12/ ), as well as in-house programs in MATLAB (MathWorks).
- Full pipeline: machine learning [scikit-learn] -> stage not stated [SPM]

### Body mass index-dependent shifts along large-scale gradients in human cortical organization explain dietary regulatory success. (PNAS 2024)

- DOI: 10.1073/pnas.2314224121 | PMCID: PMC11067012 | PMID: 38648482
- Evidence: We focus our analysis on voxels shared across these three established gradients (92,130 voxels) using SPM12’s conjunction function ( http://www.fil.ion.ucl.ac.uk/spm ) (Cortical Gradient Map 1 ∩ Cortical Gradient Map 2 ∩ Cortical Gradient Map 3).
- Full pipeline: stage not stated [SPM, fMRIPrep]

### Causal functional maps of brain rhythms in working memory. (PNAS 2024)

- DOI: 10.1073/pnas.2318528121 | PMCID: PMC10998564 | PMID: 38536752
- Evidence: The framework uses SPM12 and CAT12 to perform automatic tissue segmentations and surface reconstruction ( 96 , 97 ).
- Full pipeline: normalisation [FreeSurfer] -> structure determination [SPM] -> stage not stated [R v4.3]

### Changes in spatial self-consciousness elicit grid cell-like representation in the entorhinal cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2315758121 | PMCID: PMC10962966 | PMID: 38489383
- Evidence: The functional images were preprocessed using SPM12.
- Full pipeline: differential/statistical testing [lme4 v1.1.26] -> stage not stated [FreeSurfer v6.0.0, R, SPM]

### Onscreen presence of instructors in video lectures affects learners' neural synchrony and visual attention during multimedia learning. (PNAS 2024)

- DOI: 10.1073/pnas.2309054121 | PMCID: PMC10963011 | PMID: 38466840
- Evidence: The fMRI data preprocessing was conducted using the software SPM12 (Wellcome Centre for Human Neuroimaging; https://www.fil.ion.ucl.ac.uk/spm/software/spm12/ ).
- Full pipeline: visualisation [BrainNet Viewer] -> stage not stated [SPM]

### Live music stimulates the affective brain and emotionally entrains listeners in real time. (PNAS 2024)

- DOI: 10.1073/pnas.2316306121 | PMCID: PMC10927510 | PMID: 38408255
- Evidence: Offline Functional Brain Data analysis. fMRI analyses were performed using Statistical Parametric Mapping (SPM12, version 7771; fil.ion.ucl.ac.uk/spm ).
- Full pipeline: alignment/mapping [SPM] -> dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM]

### The social transmission of empathy relies on observational reinforcement learning. (PNAS 2024)

- DOI: 10.1073/pnas.2313073121 | PMCID: PMC10907261 | PMID: 38381794
- Evidence: Preprocessing, first-level, and second level analysis . fMRI data were analyzed using SPM12 ( https://www.fil.ion.ucl.ac.uk/spm/ ) using a standard preprocessing pipeline (see SI Appendix , Supplementary Methods, fMRI analyses , for further details).
- Full pipeline: stage not stated [SPM, lme4]

### The central renin-angiotensin system: A genetic pathway, functional decoding, and selective target engagement characterization in humans. (PNAS 2024)

- DOI: 10.1073/pnas.2306936121 | PMCID: PMC10895353 | PMID: 38349873
- Evidence: We subsequently conducted voxel-wise analysis on the level of the whole (left) brain using statistical parametric mapping software (SPM12, Welcome Department of Imaging Neuroscience, London, UK).
- Full pipeline: alignment/mapping [SPM] -> registration [FSL] -> differential/statistical testing [SPM] -> stage not stated [Nilearn, Nipype v1.5.1, fMRIPrep v20.2.1]

### Hormonal mechanisms of women's risk in the face of traumatic stress. (PNAS 2025)

- DOI: 10.1073/pnas.2524903122 | PMCID: PMC12745815 | PMID: 41397126
- Evidence: Fearful and neutral face conditions were modeled in SPM12 using a blocked design, convolving the hemodynamic response function with 8-s blocks.
- Full pipeline: differential/statistical testing [R v4.3.0, lme4] -> stage not stated [SPM, fMRIPrep v20.2.3]

### Cortical tracking of sign language: The role of language knowledge in tracking of different articulators. (PNAS 2025)

- DOI: 10.1073/pnas.2512665122 | PMCID: PMC12745750 | PMID: 41397120
- Evidence: Finally, we applied a nonlinear transformation, computed using the spatial normalization algorithm implemented in SPM8 (Wellcome Department of Cognitive Neurology, London, UK), from each individual MRI to the standard Montreal Neurological Institute (MNI) brain and subsequently applied it to every individual brain coherence map.
- Full pipeline: normalisation [SPM] -> stage not stated [FieldTrip, FreeSurfer]

### Full interhemispheric integration sustained by a fraction of posterior callosal fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2520190122 | PMCID: PMC12582319 | PMID: 41118210
- Evidence: Initial preprocessing relied on functions from the Statistical Parametric Mapping 12 software (SPM12, Wellcome Trust Centre for Neuroimaging, London) in Matlab and Advanced Normalization Tools (ANTs) ( 64 ).
- Full pipeline: alignment/mapping [ANTs, SPM] -> normalisation [ANTs, SPM] -> registration [QSIPrep, fMRIPrep] -> differential/statistical testing [ANTs, SPM] -> stage not stated [FSL]

### From retinotopic to ordinal coding: Dissecting the cortical stages of visual word recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2507291122 | PMCID: PMC12582272 | PMID: 41118216
- Evidence: This distortion-corrected data was further processed using the SPM12 toolbox ( https://www.fil.ion.ucl.ac.uk/spm/software/spm12 ).
- Full pipeline: normalisation [Python] -> differential/statistical testing [Python] -> stage not stated [FSL, MNE-Python, PyTorch, SPM]

### Disentangling metabolic and neurovascular timescales supporting cognitive processes. (PNAS 2025)

- DOI: 10.1073/pnas.2506513122 | PMCID: PMC12501135 | PMID: 40982680
- Evidence: This involved coregistering the single voxel to the subject’s anatomical image with SPM12 and segmenting it into tissue types.
- Full pipeline: registration [FSL] -> stage not stated [SPM]

### Action-type mapping principles extend beyond evolutionarily conserved actions, even in people born without hands. (PNAS 2025)

- DOI: 10.1073/pnas.2503188122 | PMCID: PMC12402994 | PMID: 40828021
- Evidence: GLM beta estimates were obtained for each trial using SPM12.
- Full pipeline: stage not stated [SPM]

### Striatal and cerebellar interactions during reward-based motor performance. (PNAS 2025)

- DOI: 10.1073/pnas.2503373122 | PMCID: PMC12358918 | PMID: 40763015
- Evidence: Imaging data were preprocessed and analyzed using SPM12 (Wellcome Trust Centre for Neuroimaging, UCL, London, UK).
- Full pipeline: stage not stated [SPM]

### Optimistic people are all alike: Shared neural representations supporting episodic future thinking among optimistic individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2511101122 | PMCID: PMC12318172 | PMID: 40690674
- Evidence: We conducted data preprocessing and statistical analysis for Studies 1 and 2 using Statistical Parametric Mapping (SPM)-12 software (Wellcome Department of Imaging Neuroscience, London, UK).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [R, vegan]

### Predictive processes shape individual musical preferences. (PNAS 2025)

- DOI: 10.1073/pnas.2500494122 | PMCID: PMC12304940 | PMID: 40663615
- Evidence: Model fits were compared using Bayesian model comparison (spm_BMS function in SPM12) ( 64 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [R v4.0.2, lme4]

### A hierarchy of processing complexity and timescales for natural sounds in the human auditory cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2412243122 | PMCID: PMC12067213 | PMID: 40294254
- Evidence: Nonlinear MNI normalization was then performed in Brainstorm, which internally uses SPM12 for the procedure ( 71 ).Finally, the Julich Brain (v3.0) volumetric atlas ( 72 ) was imported for ROI analysis, using the MNI reverse field deformation to transform the atlas into the patient-specific spaces.
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox]

### Neural basis for individual differences in the attention-enhancing effects of methylphenidate. (PNAS 2025)

- DOI: 10.1073/pnas.2423785122 | PMCID: PMC12002349 | PMID: 40127280
- Evidence: We performed one regression for each PET measure, with the ALAN fMRI signal as the predictor and age as a covariate, over all striatal voxels, using the SPM12 toolbox in MATLAB.
- Full pipeline: differential/statistical testing [FSL, SPM] -> stage not stated [FreeSurfer v5.3.0, R]

### Constructed languages are processed by the same brain mechanisms as natural languages. (PNAS 2025)

- DOI: 10.1073/pnas.2313473122 | PMCID: PMC11962467 | PMID: 40096599
- Evidence: The first 10 s of each run were excluded to allow for steady-state magnetization. fMRI Data Preprocessing and First-Level Modeling. fMRI data were analyzed using SPM12 (release 7487), CONN EvLab module (release 19b), and other custom MATLAB scripts.
- Full pipeline: stage not stated [SPM]

### Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2408791122 | PMCID: PMC11912438 | PMID: 40053364
- Evidence: Then, the data were converted into Statistical Parametric Mapping (SPM) format, preprocessed and analyzed in MATLAB (MathWorks, Natick, MA, USA) using in-house codes and the Oxford Centre for Human Brain Activity (OHBA) Software Library (OSL) ( 84 ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM]

### The neural bases of the reach-grasp movement in humans: Quantitative evidence from brain lesions. (PNAS 2025)

- DOI: 10.1073/pnas.2419801122 | PMCID: PMC11912408 | PMID: 40042909
- Evidence: To do so, individual MR scans were normalized to the Montreal Neurological Institute (MNI) standard space using SPM12 software (Wellcome Trust Centre for Neuroimaging, London).
- Full pipeline: normalisation [SPM] -> stage not stated [R]

### Brain aging shows nonlinear transitions, suggesting a midlife "critical window" for metabolic intervention. (PNAS 2025)

- DOI: 10.1073/pnas.2416433122 | PMCID: PMC11912423 | PMID: 40030017
- Evidence: Mayo, Cam-CAN, and the metabolic intervention datasets were preprocessed with fMRIprep ( 83 ), combined with image processing methods from SPM (SPM12, UCL) and the nilearn python library ( 84 ).
- Full pipeline: stage not stated [Nilearn, SPM, SciPy, fMRIPrep]

### Temporal autocorrelation is predictive of age-An extensive MEG time-series analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411098122 | PMCID: PMC11873822 | PMID: 39977317
- Evidence: Each region was converted to surfaces and spatially normalized to Montreal Neurological Institute space (DARTEL; SPM12; https://filion.ucl.ac.uk/spm/software/spm12/ ) using CAT12 DARTEL template ( https://neuro.uni-jena.de/cat/ ), yielding 2,338 brain vertices for each participant as described elsewhere ( 66 ).
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer v6.0.0, SUMA] -> stage not stated [FieldTrip v3.5]

### Individual differences in speech monitoring: Functional and structural correlates of delayed auditory feedback. (PNAS 2026)

- DOI: 10.1073/pnas.2530123123 | PMCID: PMC13321129 | PMID: 42330290
- Evidence: First, we smoothed the preprocessed functional images in MNI space with an isotropic Gaussian kernel of 4 mm FWHM in SPM12 in MATLAB R2023b.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox, SPM, fMRIPrep v23.1.0]

### Reading ability in both deaf and hearing adults is linked to neural representations of abstract phonology derived from visual speech. (PNAS 2026)

- DOI: 10.1073/pnas.2535704123 | PMCID: PMC13229273 | PMID: 42190012
- Evidence: Data were analyzed with SPM12 ( http://www.fil.ion.ucl.ac.uk/spm/ ) with MATLAB.
- Full pipeline: stage not stated [SPM]

### Contributions of the basolateral amygdala and nucleus accumbens to sustaining not just initiating cognitive effort. (PNAS 2026)

- DOI: 10.1073/pnas.2601231123 | PMCID: PMC13167750 | PMID: 42090260
- Evidence: Functional data analysis was performed using SPM12 ( http://www.fil.ion.ucl.ac.uk/spm12 ).
- Full pipeline: stage not stated [CONN toolbox, PsychoPy, SPM, afex]

### Sender-receiver subdivisions of the default mode network in perceptual and memory-guided cognition. (PNAS 2026)

- DOI: 10.1073/pnas.2528851123 | PMCID: PMC13079981 | PMID: 41945445
- Evidence: Preprocessing was conducted in the CONN-fMRI functional connectivity toolbox (CONN), Version 18a ( 52 ), based on Statistical Parametric Mapping 12 ( http://www.fil.ion.ucl.ac.uk/spm/ ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL v6.0, emmeans, lme4]

### Human hippocampal theta-gamma coupling coordinates sequential planning during navigation. (PNAS 2026)

- DOI: 10.1073/pnas.2513547123 | PMCID: PMC12956831 | PMID: 41758661
- Evidence: MEG data were preprocessed using SPM12 ( 44 ), Fieldtrip ( 45 ), and custom MATLAB code.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, SPM]

