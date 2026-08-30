# AFNI

- **Category:** neuroimaging
- **Papers in survey:** 39
- **Journals:** PNAS (38), Nature (1)
- **Years:** 2021 (7), 2022 (9), 2023 (6), 2024 (8), 2025 (9)
- **Versions named:** 21.1.10 (1), 2016.09.04.1341 (1)
- **Pipeline stages it appears in:** registration (11), alignment/mapping (3), dimensionality reduction/clustering (3), normalisation (2), differential/statistical testing (2)

## Papers

### Cingulate dynamics track depression recovery with deep brain stimulation. (Nature 2023)

- DOI: 10.1038/s41586-023-06541-3 | PMCID: PMC10550829 | PMID: 37730990
- Evidence: All images were preprocessed using the FMRIB Software Library (FSL; http://www.fmrib.ox.ac.uk/fsl/ ) 57 (v.6.0) and Analysis of Functional NeuroImages (AFNI, http://afni.niml.nih.gov/afni/ ) software (v.23.1.06).
- Full pipeline: machine learning [PyTorch, scikit-learn v1.1.1] -> stage not stated [AFNI, FSL, Python v3.6]

### Temporal self-compression: Behavioral and neural evidence that past and future selves are compressed as they move away from the present. (PNAS 2021)

- DOI: 10.1073/pnas.2101403118 | PMCID: PMC8670431 | PMID: 34848536
- Evidence: BOLD runs were slice-time corrected using 3dTshift from Analysis of Functional NeuroImages (AFNI 20160207) (ref.
- Full pipeline: registration [AFNI, FreeSurfer] -> stage not stated [FSL v5.0.9, Nilearn, Nipype v1.2.0, R, fMRIPrep v1.4.0, lme4]

### Divisive normalization unifies disparate response signatures throughout the human visual hierarchy. (PNAS 2021)

- DOI: 10.1073/pnas.2108713118 | PMCID: PMC8609633 | PMID: 34772812
- Evidence: BOLD runs were slice-time-corrected by using 3dTshift from AFNI 20160207 (ref.
- Full pipeline: registration [AFNI, fMRIPrep] -> structure determination [FreeSurfer v7.1] -> stage not stated [FSL v5.0.9, Nilearn v0.6.2, PsychoPy]

### Shared neural codes for visual and semantic information about familiar faces in a common representational space. (PNAS 2021)

- DOI: 10.1073/pnas.2110474118 | PMCID: PMC8609335 | PMID: 34732577
- Evidence: This preprocessing step was performed as a single operation using 3dTProject in AFNI.
- Full pipeline: stage not stated [AFNI, Python, SUMA, fMRIPrep v1.0.3]

### Shifting gradients of macroscale cortical organization mark the transition from childhood to adolescence. (PNAS 2021)

- DOI: 10.1073/pnas.2024448118 | PMCID: PMC8285909 | PMID: 34260385
- Evidence: 94 ), Analysis of Functional NeuroImages (AFNI; ref.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [AFNI, FSL, FreeSurfer]

### Altered sense of self during seizures in the posteromedial cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2100522118 | PMCID: PMC8307613 | PMID: 34272280
- Version used: **2016.09.04.1341**
- Evidence: These signals were regressed out of native space–projected BOLD data (using 3dTproject; AFNI v2016.09.04.1341; Cox 1996; 2012), followed by bandpass filtering at 0.01 to 0.1 Hz (using 3dBandpass; AFNI v2016.09.04.1341; Cox 1996; 2012).
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [AFNI v2016.09.04.1341, FreeSurfer]

### Attention, awareness, and the right temporoparietal junction. (PNAS 2021)

- DOI: 10.1073/pnas.2026099118 | PMCID: PMC8237657 | PMID: 34161276
- Evidence: Functional data were slice time corrected using 3dTshift from Analysis of Functional Neuroimages (AFNI) version 16.2.07 ( 38 ) (RRID: SCR_005927 ) and motion corrected using mcflirt ( 39 ) (FSL version 5.0.9).
- Full pipeline: normalisation [ANTs] -> registration [AFNI, ANTs] -> stage not stated [FSL, Nilearn, Nipype, fMRIPrep v1.2.3]

### Evidence supporting a time-limited hippocampal role in retrieving autobiographical memories. (PNAS 2021)

- DOI: 10.1073/pnas.2023069118 | PMCID: PMC8000197 | PMID: 33723070
- Evidence: Scan acquisition parameters are described in SI Appendix , Supplementary Methods . fMRI data were preprocessed using AFNI ( 68 ) (RRID: SCR_005927) to reduce noise and facilitate across-subject comparisons.
- Full pipeline: stage not stated [AFNI, FreeSurfer v6.0, lme4]

### Compulsive drug-taking is associated with habenula-frontal cortex connectivity. (PNAS 2022)

- DOI: 10.1073/pnas.2208867119 | PMCID: PMC9897479 | PMID: 36469769
- Evidence: FSL ( https://fsl.fmrib.ox.ac.uk ) and Analysis of Functional NeuroImages (AFNI) ( 74 ) were used in fMRI data preprocessing, which included discarding the first four volumes, slice timing correction, motion correction, and spatial smoothing (blurred to a full width at half-maximum of 0.8 mm).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [AFNI, FSL]

### Neural event segmentation of continuous experience in human infants. (PNAS 2022)

- DOI: 10.1073/pnas.2200257119 | PMCID: PMC9618143 | PMID: 36252007
- Evidence: Analysis of Functional NeuroImages (AFNI)’s ( https://afni.nimh.nih.gov ) despiking algorithm was used to attenuate aberrant timepoints within voxels.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [ANTs] -> stage not stated [AFNI, FSL]

### Language and developmental plasticity after perinatal stroke. (PNAS 2022)

- DOI: 10.1073/pnas.2207293119 | PMCID: PMC9586296 | PMID: 36215488
- Evidence: Unless otherwise specified, all activation maps were thresholded at a single-voxel threshold of P < 0.001, combined with a cluster threshold of P < 0.05 as determined by AFNI’s 3dClustSim function ( 71 , 72 ).
- Full pipeline: dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM]

### Mind blanking is a distinct mental state linked to a recurrent brain profile of globally positive connectivity during ongoing mentation. (PNAS 2022)

- DOI: 10.1073/pnas.2200511119 | PMCID: PMC9564098 | PMID: 36194631
- Evidence: Preprocessing and denoising were performed via a locally developed pipeline written in Python [nipype package ( 48 )] encompassing toolboxes from Statistical Parametric Mapping 12 ( 49 ), FSL 6.0 ( 50 ), AFNI ( 51 ), and ART ( http://web.mit.edu/swg/software.htm ).
- Full pipeline: alignment/mapping [AFNI, FSL v6.0, Nipype, SPM] -> differential/statistical testing [AFNI, FSL v6.0, Nipype, SPM] -> machine learning [scikit-learn] -> stage not stated [Python]

### Hippocampus and temporal pole functional connectivity is associated with age and individual differences in autobiographical memory. (PNAS 2022)

- DOI: 10.1073/pnas.2203039119 | PMCID: PMC9564102 | PMID: 36191210
- Evidence: BOLD coefficient sets were subsequently extracted with AFNI 3dmaskave ( 92 – 94 ) by run and concatenated.
- Full pipeline: registration [FSL] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [AFNI]

### Brain-wide functional connectivity of face patch neurons during rest. (PNAS 2022)

- DOI: 10.1073/pnas.2206559119 | PMCID: PMC9457296 | PMID: 36044550
- Evidence: For the sake of clarity, we therefore inverted the sign of modulation throughout the article. fMRI Data Processing. fMRI data were analyzed using the AFNI/SUMA software package ( 61 ) and custom-written MATLAB code (MathWorks, Natick, MA).
- Full pipeline: stage not stated [AFNI, SUMA]

### Adolescent development of multiscale structural wiring and functional interactions in the human connectome. (PNAS 2022)

- DOI: 10.1073/pnas.2116673119 | PMCID: PMC9271154 | PMID: 35776541
- Evidence: T1-weighted data were processed using the fusion of neuroimaging preprocessing pipeline integrating AFNI, FSL, FreeSurfer, ANTs, and Workbench ( https://gitlab.com/by9433/funp ) ( 105 – 109 ), which is similar to the minimal preprocessing pipeline for the HCP ( 110 ).
- Full pipeline: stage not stated [AFNI, ANTs, FSL, FreeSurfer, MRtrix3]

### Multilevel atlas comparisons reveal divergent evolution of the primate brain. (PNAS 2022)

- DOI: 10.1073/pnas.2202491119 | PMCID: PMC9231627 | PMID: 35700361
- Evidence: Finally, using “3dhistog” from AFNI ( 32 ), we extracted the volume of each brain region for PGLS analysis.
- Full pipeline: stage not stated [AFNI, ANTs]

### Decoding the information structure underlying the neural representation of concepts. (PNAS 2022)

- DOI: 10.1073/pnas.2108091119 | PMCID: PMC8832989 | PMID: 35115397
- Evidence: The fMRI images were preprocessed (slice timing correction, motion correction, distortion correction, volume alignment, and scaling) using the software package Analysis of Functional NeuroImages (AFNI) ( 65 ).
- Full pipeline: alignment/mapping [AFNI] -> normalisation [AFNI] -> registration [AFNI]

### Rats respond to aversive emotional arousal of human handlers with the activation of the basolateral and central amygdala. (PNAS 2023)

- DOI: 10.1073/pnas.2302655120 | PMCID: PMC10655214 | PMID: 37934822
- Evidence: Slice-time correction was performed on the functional scanning runs using 3dTshift from AFNI 20160207 ( 66 ).
- Full pipeline: registration [AFNI, FSL v5.0.9] -> differential/statistical testing [SciPy] -> stage not stated [ANTs v2.2.0, ImageJ, Nilearn v0.5.2, Nipype v1.2.0, fMRIPrep v1.4.0]

### Neural evidence of switch processes during semantic and phonetic foraging in human memory. (PNAS 2023)

- DOI: 10.1073/pnas.2312462120 | PMCID: PMC10589708 | PMID: 37824523
- Evidence: 3dFWHMx and 3dClustSim in AFNI ( 99 ) were used to estimate activation significance thresholds of voxel-wise P < 0.001, cluster-corrected P < 0.05, k E = 78 (whole brain) or k E = 34 (cerebellar SUIT).
- Full pipeline: alignment/mapping [SPM] -> dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM] -> stage not stated [Python v2.7]

### Spatiotemporally distributed frontotemporal networks for sentence reading. (PNAS 2023)

- DOI: 10.1073/pnas.2300252120 | PMCID: PMC10151604 | PMID: 37068244
- Evidence: Following surgical implantation, electrodes were localized by coregistration of preoperative anatomical 3T MRI and postoperative computerized tomography scans in AFNI ( 79 ).
- Full pipeline: registration [AFNI] -> visualisation [FreeSurfer]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Evidence: A deformation field to correct for susceptibility distortions was estimated based on two echo-planar imaging (EPI) references with opposing phase-encoding directions, using 3dQwarp (AFNI 20160207, 126 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Human brain effects of DMT assessed via EEG-fMRI. (PNAS 2023)

- DOI: 10.1073/pnas.2218949120 | PMCID: PMC10068756 | PMID: 36940333
- Evidence: Preprocessing steps consisted of 1) despiking [3dDespike, Analysis of Functional NeuroImages (AFNI) ( 73 )]; 2) slice time correction [3dTshift, AFNI ( 73 )]; 3) motion correction [3dvolreg, AFNI ( 73 )] by registering each volume to the most similar volume, in the least squares sense, to all others (in-house code); 4) brain extraction [BET, FSL ( 74 )]; 5) rigid body registration to anatomical sc...
- Full pipeline: normalisation [ANTs, FSL] -> registration [AFNI, ANTs, FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Sculpting new visual categories into the human brain. (PNAS 2024)

- DOI: 10.1073/pnas.2410445121 | PMCID: PMC11648923 | PMID: 39625982
- Evidence: Images were preprocessed using custom AFNI ( 61 ), Freesurfer ( 25 ), and bash scripts.
- Full pipeline: stage not stated [AFNI, FreeSurfer]

### Human adolescent brain similarity development is different for paralimbic versus neocortical zones. (PNAS 2024)

- DOI: 10.1073/pnas.2314074121 | PMCID: PMC11331068 | PMID: 39121162
- Evidence: Briefly, this included ME-ICA to remove non-BOLD components ( 47 , 48 ); CSF regression using Analysis of Functional NeuroImages software [AFNI; ( 49 )]; parcellation into 360 bilateral cortical regions using the HCP template ( 44 ); band-pass filtering (frequency range 0.025 to 0.111 Hz); removal of 30 dropout regions, defined by a low Z score of mean signal intensity in at least one participant ...
- Full pipeline: differential/statistical testing [AFNI] -> stage not stated [FreeSurfer v5.3.0]

### A familiar face and person processing area in the human temporal pole. (PNAS 2024)

- DOI: 10.1073/pnas.2321346121 | PMCID: PMC11252731 | PMID: 38954551
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Hemispheric functional organization, as revealed by naturalistic neuroimaging, in pediatric epilepsy patients with cortical resections. (PNAS 2024)

- DOI: 10.1073/pnas.2317458121 | PMCID: PMC11252739 | PMID: 38950362
- Version used: **21.1.10**
- Evidence: All participant data were preprocessed through the same pipeline using AFNI (version 21.1.10) ( 54 ).
- Full pipeline: differential/statistical testing [R, lme4] -> structure determination [FreeSurfer] -> stage not stated [AFNI v21.1.10, emmeans]

### Evolutionarily conserved neural responses to affective touch in monkeys transcend consciousness and change with age. (PNAS 2024)

- DOI: 10.1073/pnas.2322157121 | PMCID: PMC11067024 | PMID: 38648473
- Evidence: Functional imaging data were processed with custom AFNI pipelines ( 105 , 106 ).
- Full pipeline: stage not stated [AFNI, CIVET, Python, R v4.3.1, emmeans, lme4]

### Subcallosal cingulate deep brain stimulation evokes two distinct cortical responses via differential white matter activation. (PNAS 2024)

- DOI: 10.1073/pnas.2314918121 | PMCID: PMC10998591 | PMID: 38527192
- Evidence: MR and CT images were processed using the FMRIB Software Library (FSL, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/ ) and the Analysis of Functional Neuroimages toolbox (AFNI, https://afni.nimh.nih.gov/ ) ( 44 , 45 ).
- Full pipeline: stage not stated [AFNI, Camino, FSL, Matplotlib v3.8.0, NumPy v1.24.4, SciPy v1.11.2, seaborn v0.12.2]

### Live music stimulates the affective brain and emotionally entrains listeners in real time. (PNAS 2024)

- DOI: 10.1073/pnas.2316306121 | PMCID: PMC10927510 | PMID: 38408255
- Evidence: We determined this cluster corrected threshold by using the 3DClustSim algorithm implemented in the AFNI software ( afni.nimh.nih.gov/afni ; version AFNI_18.3.01; including the new (spatial) autocorrelation function extension) and based on the estimated smoothness of the residual images.
- Full pipeline: alignment/mapping [SPM] -> dimensionality reduction/clustering [AFNI] -> differential/statistical testing [SPM]

### Inactivation of face-selective neurons alters eye movements when free viewing faces. (PNAS 2024)

- DOI: 10.1073/pnas.2309906121 | PMCID: PMC10801883 | PMID: 38198528
- Evidence: All EPI data were analyzed using Analysis of Functional NeuroImages (AFNI) software ( http://afni.nimh.nih.gov/afni ) ( 69 ).
- Full pipeline: stage not stated [AFNI, Psychtoolbox]

### Parallel systems for social and spatial cognition reaching the cortical apex. (PNAS 2025)

- DOI: 10.1073/pnas.2520067122 | PMCID: PMC12595413 | PMID: 41166425
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Evidence: To define outliers, we used the following IQMs: AFNI’s outlier ratio (aor), mean frame-wise displacement (fd_mean), intensity changes (DVARS_nstd), and global correlation (gcor).
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

### Orexin effect on physiological pulsations of the human brain. (PNAS 2025)

- DOI: 10.1073/pnas.2501578122 | PMCID: PMC12337265 | PMID: 40748959
- Evidence: Motion was corrected in four layers: 1) the raw MREG amplitude data were despiked with Analysis of Functional Neuroimages’ ( 73 ) (AFNI) tools, 2) FSL MCFLIRT was used to correct for bulk head motion, 3) each subjects’ MCLIRT motion correction data were used to exclude subjects with any absolute motion exceeding 1.5 mm (half the voxel size), relative motion over 0.5 mm, as well as the earlier impl...
- Full pipeline: registration [AFNI] -> stage not stated [FSL]

### Dynamic neuroplasticity of language networks: The intersection of bilingualism and epilepsy. (PNAS 2025)

- DOI: 10.1073/pnas.2422742122 | PMCID: PMC12304909 | PMID: 40658859
- Evidence: Image Processing. fMRI data processing was carried out using AFNI ( 52 ) and SUMA ( 53 ).
- Full pipeline: stage not stated [AFNI, SUMA]

### Genetic contributions to brain criticality and its relationship with human cognitive functions. (PNAS 2025)

- DOI: 10.1073/pnas.2417010122 | PMCID: PMC12232412 | PMID: 40549906
- Evidence: The signals of each ROI were then extracted using the 3dmaskdump function in AFNI ( 87 ).
- Full pipeline: stage not stated [AFNI, BrainNet Viewer]

### Early development of navigationally relevant location information in the retrosplenial complex. (PNAS 2025)

- DOI: 10.1073/pnas.2503569122 | PMCID: PMC12088441 | PMID: 40324094
- Evidence: Preprocessing was performed using AFNI (Analysis of Functional Neuroimages) ( 53 ) (version 20.3.02).
- Full pipeline: stage not stated [AFNI, FreeSurfer]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Evidence: BOLD runs were slice-time corrected using 3dTshift from AFNI.
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### Expectation-dependent stimulus selectivity in the ventral visual cortical pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2406684122 | PMCID: PMC12002251 | PMID: 40146852
- Evidence: We preprocessed raw image volumes through slice-by-slice motion- and slice-time correction (AFNI), which were aligned to MRI anatomical images and unwarped with JIP Analysis Toolkit ( https://www.nmr.mgh.harvard.edu/~jbm/jip/ ).
- Full pipeline: alignment/mapping [AFNI] -> registration [AFNI] -> stage not stated [FreeSurfer]

### Expansion of a conserved architecture drives the evolution of the primate visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421585122 | PMCID: PMC11761675 | PMID: 39805017
- Evidence: Analysis of Functional NeuroImages (AFNI; RRID:nif-0000-00259; Cox, 1996), SUMA ( 116 ), Freesurfer (FreeSurfer, RRID:nif-0000-00304) ( 117 , 118 ), FSL ( 119 ) (FSL, RRID:birnlex_2067), Advanced Normalization Tools ( 120 ) (ANTs), and MATLAB (MATLAB, RRID:nlx_153890) were used for additional data processing.
- Full pipeline: normalisation [AFNI, ANTs, FSL, SUMA] -> structure determination [FreeSurfer]

