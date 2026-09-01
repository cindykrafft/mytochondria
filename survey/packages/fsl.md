# FSL

- **Category:** neuroimaging
- **Papers in survey:** 114
- **Journals:** PNAS (92), Nature (19), Cell (2), Science (1)
- **Years:** 2021 (9), 2022 (19), 2023 (22), 2024 (19), 2025 (33), 2026 (12)
- **Versions named:** 5.0.9 (6), 6.0 (3), 6.0.3 (3), 6.0.7.8 (2), 5.0 (2), 6.0.2 (1), 5.0.4 (1), 6.0.0 (1), 5.0.10 (1)
- **Pipeline stages it appears in:** registration (24), differential/statistical testing (13), normalisation (7), alignment/mapping (4), dimensionality reduction/clustering (3), simulation/modelling (1), machine learning (1), quality control (1)

## Papers

### Impaired neural replay of inferred relationships in schizophrenia. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.012 | PMCID: PMC8357425 | PMID: 34197734
- Evidence: ...lbox, FieldTrip ( https://www.fieldtriptoolbox.org/ ), the OHBA Software Library (OSL, including OAT, https://ohba-analysis.github.io/osl-docs/ ) and FMRIB Software Library (FSL, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/ ).
- Full pipeline: alignment/mapping [FieldTrip, SPM] -> differential/statistical testing [FieldTrip, SPM] -> structure determination [FieldTrip, SPM] -> stage not stated [FSL]

### Stimulant medications affect arousal and reward, not attention networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.039 | PMCID: PMC12834599 | PMID: 41448140
- Evidence: 176 Processing dependencies included FSL, 177 FreeSurfer, 178 and NiBabel.
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [FSL, FreeSurfer, NiBabel]

### Brain-phenotype models fail for individuals who defy sample stereotypes. (Nature 2022)

- DOI: 10.1038/s41586-022-05118-w | PMCID: PMC9433326 | PMID: 36002572
- Evidence: Structural scans were skull stripped using an optimized version of the FMRIB’s Software Library (FSL) 105 pipeline (optiBET) 106 .
- Full pipeline: registration [FSL, SPM] -> stage not stated [Psychtoolbox]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Evidence: At day 5, MDDCs were stimulated with 10 µg ml −1 of Akkermansia lipids, 100 ng ml −1 of Pam3CSK4, 100 ng ml −1 of FSL-1 or 100 ng ml −1 of LPS for 18 h or as indicated.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### Reproducible brain-wide association studies require thousands of individuals. (Nature 2022)

- DOI: 10.1038/s41586-022-04492-9 | PMCID: PMC8991999 | PMID: 35296861
- Evidence: This atlas transformation, mean field distortion correction, and resampling to 3 mm 3 atlas space were combined into a single interpolation using the FSL 58 applywarp tool.
- Full pipeline: normalisation [FreeSurfer] -> stage not stated [ANTs, Connectome Workbench, FSL]

### Normative spatiotemporal fetal brain maturation with satisfactory development at 2 years. (Nature 2023)

- DOI: 10.1038/s41586-023-06630-3 | PMCID: PMC10620088 | PMID: 37880365
- Evidence: We used non-parametric ‘Monte Carlo’ permutation testing as implemented in the FSL RANDOMISE method 69 , and applied threshold-free cluster enhancement to the statistical maps 70 , to enhance the brain areas that showed spatial contiguity.
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, statsmodels] -> simulation/modelling [FSL] -> stage not stated [Python v3.9.6, seaborn]

### Cingulate dynamics track depression recovery with deep brain stimulation. (Nature 2023)

- DOI: 10.1038/s41586-023-06541-3 | PMCID: PMC10550829 | PMID: 37730990
- Evidence: All images were preprocessed using the FMRIB Software Library (FSL; http://www.fmrib.ox.ac.uk/fsl/ ) 57 (v.6.0) and Analysis of Functional NeuroImages (AFNI, http://afni.niml.nih.gov/afni/ ) software (v.23.1.06).
- Full pipeline: machine learning [PyTorch, scikit-learn v1.1.1] -> stage not stated [AFNI, FSL, Python v3.6]

### An orexigenic subnetwork within the human hippocampus. (Nature 2023)

- DOI: 10.1038/s41586-023-06459-w | PMCID: PMC10499606 | PMID: 37648849
- Evidence: Whereas preprocessing was performed on the diffusion MRI data from the binge-eating-prone cohort to prepare the images for probabilistic tractography using the FSL suite 60 , 61 , the normative HCP diffusion MRI data had already been preprocessed (with the minimal preprocessing pipeline).
- Full pipeline: alignment/mapping [SPM] -> normalisation [ANTs v2.1.0] -> registration [ANTs v2.1.0] -> differential/statistical testing [SPM] -> stage not stated [FSL, FieldTrip, Python v3.6, fMRIPrep v1.2.3]

### Geometric constraints on human brain function. (Nature 2023)

- DOI: 10.1038/s41586-023-06098-1 | PMCID: PMC10266981 | PMID: 37258669
- Evidence: These connectome data were derived from minimally preprocessed dMRI data of 334 unrelated HCP subjects and constructed via the probabilistic tractography tool of FMRIB Software Library (FSL) 93 .
- Full pipeline: stage not stated [FSL, FreeSurfer, Nilearn]

### A somato-cognitive action network alternates with effector regions in motor cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05964-2 | PMCID: PMC10172144 | PMID: 37076628
- Evidence: To compute the overall degree of activation in response to each motion, data from each run was entered into a first-level analysis within FSL’s FEAT 98 in which each motion block was modelled as an event of duration 15.4 s, and the combined block waveform for each motion condition was convolved with a haemodynamic response function to form a separate regressor in a generalized linear model (GLM) a...
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [FSL] -> machine learning [Connectome Workbench] -> stage not stated [FreeSurfer, jsPsych]

### Human hippocampal and entorhinal neurons encode the temporal structure of experience. (Nature 2024)

- DOI: 10.1038/s41586-024-07973-1 | PMCID: PMC11540853 | PMID: 39322671
- Evidence: First, each participant’s MRI and CT images were co-registered using the FSL ‘flirt’ function.
- Full pipeline: alignment/mapping [SPM] -> normalisation [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL]

### Frontostriatal salience network expansion in individuals in depression. (Nature 2024)

- DOI: 10.1038/s41586-024-07805-2 | PMCID: PMC11410656 | PMID: 39232159
- Evidence: The resultant average SBR images were aligned, averaged, co-registered to the ACPC-aligned T1-weighted anatomical image and simultaneously corrected for spatial distortions using FSL topup and epi_reg programs.
- Full pipeline: alignment/mapping [FSL] -> stage not stated [Connectome Workbench, FreeSurfer]

### A probabilistic histological atlas of the human brain for MRI segmentation. (Nature 2025)

- DOI: 10.1038/s41586-025-09708-2 | PMCID: PMC12711564 | PMID: 41193801
- Evidence: Neuroimaging packages like FreeSurfer 4 , FSL 5 and SPM 6 enable large-scale studies with thousands of MRI scans.
- Full pipeline: stage not stated [FSL, FreeSurfer v7.0, PyTorch]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **6.0.2**
- Evidence: Analysis-specific functional preprocessing Additional, analysis-specific, fMRI data preprocessing was performed using FSL 6.0.2 (FMRIB Software Library) 94 , Statistical Parametric Mapping (SPM 12) software 95 , and custom Python scripts (using NiBabel (3.2.2) 96 and SciPy (1.8.0) 97 after the above-outlined general preprocessing.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Phase I trial of hES cell-derived dopaminergic neurons for Parkinson's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08845-y | PMCID: PMC12095069 | PMID: 40240592
- Evidence: Anatomical structures of the caudate nucleus and putamen were segmented in the MRI scan using an automated processing routine implemented with FSL software 48 ( https://fsl.fmrib.ox.ac.uk/fsl/docs/#/install/index ).
- Full pipeline: registration [SPM] -> stage not stated [FSL]

### Basis functions for complex social decisions in dorsomedial frontal cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08705-9 | PMCID: PMC12074988 | PMID: 40074892
- Evidence: The FMRIB Software Library (FSL) was used to analyse the imaging data 57 .
- Full pipeline: stage not stated [FSL, Psychtoolbox, jsPsych]

### Population-scale repeat expansions elucidate disease risk and brain atrophy. (Nature 2026)

- DOI: 10.1038/s41586-026-10345-6 | PMCID: PMC13190288 | PMID: 41951733
- Version used: **6.0.7.8**
- Evidence: The image was then brain-extracted 71 , rigidly transformed to MNI152 space using FLIRT 72 (FSL v.6.0.7.8) followed by a deformable registration to MNI152 space using FNIRT 73 .
- Full pipeline: variant calling [R, REGENIE v3.2] -> registration [FSL v6.0.7.8] -> differential/statistical testing [REGENIE v3.2] -> stage not stated [FreeSurfer v7.3.2, PLINK, dcm2niix]

### Rapid concerted switching of the neural code in the inferotemporal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10267-3 | PMCID: PMC13148990 | PMID: 41882367
- Evidence: Analysis of functional volumes was done using the FreeSurfer Functional Analysis Stream 57 and FSL 58 .
- Full pipeline: machine learning [PyTorch] -> stage not stated [FSL, FreeSurfer, Kilosort]

### Parkinson's disease as a somato-cognitive action network disorder. (Nature 2026)

- DOI: 10.1038/s41586-025-10059-1 | PMCID: PMC13017517 | PMID: 41639440
- Evidence: For the volumetric preprocessing pipeline, the preprocessed functional images in native space were normalized to a 2-mm spatial resolution volumetric template (the FSL version of the MNI ICBM152 non-linear template) using a co-registration matrix and volumetric non-linear registration with ANTs 110 .
- Full pipeline: normalisation [ANTs, FSL] -> registration [FSL, FreeSurfer v6.0.0] -> simulation/modelling [FieldTrip] -> stage not stated [Connectome Workbench v1.5]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Cells were then washed, trypsinized and seeded on to the labelled macrophages along with macrophage-activating ligand FSL-1 (1 ng ml −1 ; Invivogen, tlrl-fsl) overnight.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Evidence: At the clinic visit, participants were also fitted with wearable continuous glucose monitor CGM) devices (Abbott Freestyle Libre Pro (FSL)), visceral fat mass was measured using dual-energy X-ray absorptiometry scans following standard manufacturer’s recommendations (DXA; Hologic QDR 4500 plus) and fasting GlycA was measured using a high-throughput NMR metabolomics (Nightingale Health) 2016 panel.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Temporal self-compression: Behavioral and neural evidence that past and future selves are compressed as they move away from the present. (PNAS 2021)

- DOI: 10.1073/pnas.2101403118 | PMCID: PMC8670431 | PMID: 34848536
- Version used: **5.0.9**
- Evidence: Head–motion parameters with respect to the BOLD reference (transformation matrices and six corresponding rotation and translation parameters) are estimated before any spatiotemporal filtering using mcflirt (FMRIB Software Library 5.0.9) ( 90 ).
- Full pipeline: registration [AFNI, FreeSurfer] -> stage not stated [FSL v5.0.9, Nilearn, Nipype v1.2.0, R, fMRIPrep v1.4.0, lme4]

### The middle cingulate cortex and dorso-central insula: A mirror circuit encoding observation and execution of vitality forms. (PNAS 2021)

- DOI: 10.1073/pnas.2111358118 | PMCID: PMC8612212 | PMID: 34716272
- Evidence: Diffusion data were processed using the FMRIB Software Library (FSL) tools (version 5.0.9).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [FSL]

### Divisive normalization unifies disparate response signatures throughout the human visual hierarchy. (PNAS 2021)

- DOI: 10.1073/pnas.2108713118 | PMCID: PMC8609633 | PMID: 34772812
- Version used: **5.0.9**
- Evidence: 82 ; FSL 5.0.9).
- Full pipeline: registration [AFNI, fMRIPrep] -> structure determination [FreeSurfer v7.1] -> stage not stated [FSL v5.0.9, Nilearn v0.6.2, PsychoPy]

### Modular origins of high-amplitude cofluctuations in fine-scale functional connectivity dynamics. (PNAS 2021)

- DOI: 10.1073/pnas.2109380118 | PMCID: PMC8609635 | PMID: 34750261
- Evidence: FSL’s (FMRIB Software Library) dtifit was used to obtain scalar maps of fractional anisotropy, mean diffusivity, and mean kurtosis.
- Full pipeline: machine learning [DIPY] -> stage not stated [FSL]

### Shifting gradients of macroscale cortical organization mark the transition from childhood to adolescence. (PNAS 2021)

- DOI: 10.1073/pnas.2024448118 | PMCID: PMC8285909 | PMID: 34260385
- Evidence: 93 ), FMRIB Software Library (FSL; ref.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [AFNI, FSL, FreeSurfer]

### Dissociations between glucose metabolism and blood oxygenation in the human default mode network revealed by simultaneous PET-fMRI. (PNAS 2021)

- DOI: 10.1073/pnas.2021913118 | PMCID: PMC8271663 | PMID: 34193521
- Evidence: Higher-level analyses were performed using permutation testing with FMRIB Software Library (FSL) randomize ( 69 ) and 5,000 permutations.
- Full pipeline: differential/statistical testing [FSL]

### Attention, awareness, and the right temporoparietal junction. (PNAS 2021)

- DOI: 10.1073/pnas.2026099118 | PMCID: PMC8237657 | PMID: 34161276
- Evidence: Brain tissue segmentation of cerebrospinal fluid, white matter, and gray matter was performed on the brain-extracted T1w using fast ( 37 ) (Functional Magnetic Resonance Imaging of the Brain Software Library [FSL] version 5.0.9, RRID: SCR_002823 ).
- Full pipeline: normalisation [ANTs] -> registration [AFNI, ANTs] -> stage not stated [FSL, Nilearn, Nipype, fMRIPrep v1.2.3]

### Topographic connectivity reveals task-dependent retinotopic processing throughout the human brain. (PNAS 2021)

- DOI: 10.1073/pnas.2017032118 | PMCID: PMC7812773 | PMID: 33372144
- Evidence: Anatomical region of interest (ROI) definitions were taken from the multimodal parcellation atlas ( 41 ) for surface data and FMRIB Software Library’s Jülich histological atlas ( 42 ) for hippocampal ROIs in MNI volumetric space.
- Full pipeline: stage not stated [FSL, FreeSurfer, SciPy, statsmodels]

### Information flow across the cortical timescale hierarchy during narrative construction. (PNAS 2022)

- DOI: 10.1073/pnas.2209307119 | PMCID: PMC9907070 | PMID: 36508677
- Evidence: All participants provided informed, written consent, and the experimental protocol was approved by the institutional review board of Princeton University. fMRI Preprocessing. fMRI data were preprocessed using FSL ( https://fsl.fmrib.ox.ac.uk/ ), including slice time correction, motion correction, and high-pass filtering (140-s cutoff).
- Full pipeline: registration [FSL]

### Compulsive drug-taking is associated with habenula-frontal cortex connectivity. (PNAS 2022)

- DOI: 10.1073/pnas.2208867119 | PMCID: PMC9897479 | PMID: 36469769
- Evidence: FSL ( https://fsl.fmrib.ox.ac.uk ) and Analysis of Functional NeuroImages (AFNI) ( 74 ) were used in fMRI data preprocessing, which included discarding the first four volumes, slice timing correction, motion correction, and spatial smoothing (blurred to a full width at half-maximum of 0.8 mm).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [AFNI, FSL]

### Neural event segmentation of continuous experience in human infants. (PNAS 2022)

- DOI: 10.1073/pnas.2200257119 | PMCID: PMC9618143 | PMID: 36252007
- Evidence: Data from both age groups were preprocessed using a custom pipeline designed for awake infant fMRI ( 35 ), based on the FMRIB Software Library (FSL) FMRI Expert Analysis Tool (FEAT).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [ANTs] -> stage not stated [AFNI, FSL]

### Morphological similarity of amygdala-ventral prefrontal pathways represents trait anxiety in younger and older adults. (PNAS 2022)

- DOI: 10.1073/pnas.2205162119 | PMCID: PMC9586323 | PMID: 36215497
- Evidence: Preprocessing of diffusion-weighted images was done with FMRIB’s Diffusion Toolbox (FDT) of FSL (FMRIB software library v6.0, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/ ) in the following order ( 74 ).
- Full pipeline: registration [ANTs] -> differential/statistical testing [R v4.0] -> structure determination [FreeSurfer] -> machine learning [MRtrix3] -> stage not stated [FSL]

### Prenatal exposure to maternal social disadvantage and psychosocial stress and neonatal white matter connectivity at birth. (PNAS 2022)

- DOI: 10.1073/pnas.2204135119 | PMCID: PMC9586270 | PMID: 36219693
- Evidence: White matter tracts were defined using FA and FSL’s RGB V1 (primary vector) images.
- Full pipeline: stage not stated [FSL]

### Mind blanking is a distinct mental state linked to a recurrent brain profile of globally positive connectivity during ongoing mentation. (PNAS 2022)

- DOI: 10.1073/pnas.2200511119 | PMCID: PMC9564098 | PMID: 36194631
- Version used: **6.0**
- Evidence: Preprocessing and denoising were performed via a locally developed pipeline written in Python [nipype package ( 48 )] encompassing toolboxes from Statistical Parametric Mapping 12 ( 49 ), FSL 6.0 ( 50 ), AFNI ( 51 ), and ART ( http://web.mit.edu/swg/software.htm ).
- Full pipeline: alignment/mapping [AFNI, FSL v6.0, Nipype, SPM] -> differential/statistical testing [AFNI, FSL v6.0, Nipype, SPM] -> machine learning [scikit-learn] -> stage not stated [Python]

### Hippocampus and temporal pole functional connectivity is associated with age and individual differences in autobiographical memory. (PNAS 2022)

- DOI: 10.1073/pnas.2203039119 | PMCID: PMC9564102 | PMID: 36191210
- Evidence: T1-weighted images were skull stripped in FSL with the Brain Extraction Tool( 85 ) using default parameters.
- Full pipeline: registration [FSL] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [AFNI]

### An analysis of emotions and the prominence of positivity in #BlackLivesMatter tweets. (PNAS 2022)

- DOI: 10.1073/pnas.2205767119 | PMCID: PMC9436370 | PMID: 35998217
- Evidence: Emotion categories are drawn from Ekman’s taxonomy ( 20 ) and inferred over a dataset of 34.1 million tweets using a neural classification model with domain adaptation components (+TGT+FSL).
- Full pipeline: stage not stated [FSL]

### A hierarchy of linguistic predictions during natural language comprehension. (PNAS 2022)

- DOI: 10.1073/pnas.2201968119 | PMCID: PMC9371745 | PMID: 35921434
- Evidence: To create source models, FSL’s Brain Extraction Tool was used to strip nonbrain tissue.
- Full pipeline: alignment/mapping [Connectome Workbench, FreeSurfer] -> structure determination [Connectome Workbench, FreeSurfer] -> machine learning [FieldTrip] -> stage not stated [FSL]

### Comparing human and chimpanzee temporal lobe neuroanatomy reveals modifications to human language hubs beyond the frontotemporal arcuate fasciculus. (PNAS 2022)

- DOI: 10.1073/pnas.2118295119 | PMCID: PMC9282369 | PMID: 35787056
- Version used: **5.0.10**
- Evidence: MP2RAGE data were processed using the Oxford Center for Functional Magnetic Resonance Imaging of the Brain (FMRIB) software library (FSL 5.0.10; https://www.fmrib.ox.ac.uk/fsl ) and skull stripped with Brain Extraction Tool (BET).
- Full pipeline: alignment/mapping [SPM] -> registration [FSL v5.0.10, SPM] -> differential/statistical testing [SPM] -> stage not stated [R, tidyverse]

### Adolescent development of multiscale structural wiring and functional interactions in the human connectome. (PNAS 2022)

- DOI: 10.1073/pnas.2116673119 | PMCID: PMC9271154 | PMID: 35776541
- Evidence: T1-weighted data were processed using the fusion of neuroimaging preprocessing pipeline integrating AFNI, FSL, FreeSurfer, ANTs, and Workbench ( https://gitlab.com/by9433/funp ) ( 105 – 109 ), which is similar to the minimal preprocessing pipeline for the HCP ( 110 ).
- Full pipeline: stage not stated [AFNI, ANTs, FSL, FreeSurfer, MRtrix3]

### Dynamical differential covariance recovers directional network structure in multiscale neural systems. (PNAS 2022)

- DOI: 10.1073/pnas.2117234119 | PMCID: PMC9214501 | PMID: 35679342
- Evidence: For example, we calculated L1- and L2-regularized partial covariance matrices through the FMRIB (functional magnetic resonance imaging of the brain) software library (FSL) toolbox ( 38 ).
- Full pipeline: stage not stated [FSL]

### Variants of the guanine riboswitch class exhibit altered ligand specificities for xanthine, guanine, or 2'-deoxyguanosine. (PNAS 2022)

- DOI: 10.1073/pnas.2120246119 | PMCID: PMC9295807 | PMID: 35622895
- Evidence: FSL and called 92 PRT ( Fig.
- Full pipeline: stage not stated [FSL]

### Neural representations of others' traits predict social decisions. (PNAS 2022)

- DOI: 10.1073/pnas.2116944119 | PMCID: PMC9295729 | PMID: 35605117
- Evidence: For the population-level analysis, a cluster-level permutation test was conducted using the FSL randomise tool (whole-brain FWE- corrected TFCE P < 0.05; 4,999 iterations).
- Full pipeline: dimensionality reduction/clustering [FSL] -> differential/statistical testing [FSL, SPM] -> stage not stated [Python]

### Diffusion MRI-guided theta burst stimulation enhances memory and functional connectivity along the inferior longitudinal fasciculus in mild cognitive impairment. (PNAS 2022)

- DOI: 10.1073/pnas.2113778119 | PMCID: PMC9173759 | PMID: 35594397
- Evidence: We removed the Gibbs ringing artifacts ( 77 ) and used FMRIB Software Library (FSL) TOPUP to estimate and correct susceptibility-induced distortions using reverse encoded DWI data ( 78 ).
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs, CONN toolbox, FSL, FreeSurfer, MRtrix3]

### The photobiology of the human circadian clock. (PNAS 2022)

- DOI: 10.1073/pnas.2118803119 | PMCID: PMC9060497 | PMID: 35312355
- Version used: **6.0.3**
- Evidence: The fMRI data were preprocessed using FSL 6.0.3 (FMRIB Software Library, Oxford, UK) ( 50 ).
- Full pipeline: stage not stated [FSL v6.0.3]

### Hippocampal contributions to novel spatial learning are both age-related and age-invariant. (PNAS 2023)

- DOI: 10.1073/pnas.2307884120 | PMCID: PMC10723126 | PMID: 38055735
- Evidence: Image preprocessing was performed by using FEAT (FMRI Expert Analysis Tool), version 6.00, implemented in FSL (part of the FSL package; http://www.fmrib.ox.ac.uk/fsl ).
- Full pipeline: normalisation [ANTs v2.3.5] -> simulation/modelling [brms] -> stage not stated [FSL, PsychoPy, R v4.2, emmeans, lme4]

### The TLR2/TLR6 ligand FSL-1 mitigates radiation-induced hematopoietic injury in mice and nonhuman primates. (PNAS 2023)

- DOI: 10.1073/pnas.2122178120 | PMCID: PMC10723152 | PMID: 38051771
- Evidence: Twenty-six male rhesus macaques ( Macaca mulatta ; N = 20 irradiated and N = 6 nonirradiated controls) were studied, ranging in age (4.5 to 8 y) and in weight (5 to 15 kg), but matched between Vehicle- and FSL-1-treated groups.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R] -> stage not stated [FSL]

### Rats respond to aversive emotional arousal of human handlers with the activation of the basolateral and central amygdala. (PNAS 2023)

- DOI: 10.1073/pnas.2302655120 | PMCID: PMC10655214 | PMID: 37934822
- Version used: **5.0.9**
- Evidence: Additionally, we conducted skull-stripping on the anatomical reference using antsBrainExtraction from ANTs and segmentation using fast from FSL 5.0.9 ( 61 ).
- Full pipeline: registration [AFNI, FSL v5.0.9] -> differential/statistical testing [SciPy] -> stage not stated [ANTs v2.2.0, ImageJ, Nilearn v0.5.2, Nipype v1.2.0, fMRIPrep v1.4.0]

### Hemispheric asymmetry in cortical thinning reflects intrinsic organization of the neurotransmitter systems and homotopic functional connectivity. (PNAS 2023)

- DOI: 10.1073/pnas.2306990120 | PMCID: PMC10589642 | PMID: 37831741
- Evidence: Quality control, preprocessing of anatomical and functional data were performed, respectively, with MRIQC 0.15.0 ( 41 ), fMRIPrep 1.3.2 ( 42 ), and FSL_regfilt 5.0.9.
- Full pipeline: quality control [FSL, MRIQC v0.15.0, fMRIPrep v1.3.2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R v4.2.2] -> stage not stated [FreeSurfer v6.0.0]

### Whole-brain, gray, and white matter time-locked functional signal changes with simple tasks and model-free analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2219666120 | PMCID: PMC10589709 | PMID: 37824529
- Evidence: The diffusion data were preprocessed to correct for motion and eddy currents using the FSL software package ( 32 ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL, FreeSurfer]

### The adaptive stochasticity hypothesis: Modeling equifinality, multifinality, and adaptation to adversity. (PNAS 2023)

- DOI: 10.1073/pnas.2307508120 | PMCID: PMC10589678 | PMID: 37816058
- Evidence: We enforced a strict movement threshold of 1mm (estimated through FSL eddy during the diffusion sequence), which led to 29 scans being removed, leaving a final sample of 357 children.
- Full pipeline: stage not stated [FSL]

### Human white matter myelinates faster in utero than ex utero. (PNAS 2023)

- DOI: 10.1073/pnas.2303491120 | PMCID: PMC10438384 | PMID: 37549280
- Evidence: As a first quality assurance step, we removed all sessions that exceeded two standard deviations of the mean with regard to absolute motion and with regard to the amount of outlier slices replaced by FSL’s eddy tool during preprocessing.
- Full pipeline: quantification [Python] -> stage not stated [FSL, MRtrix3]

### Brain-to-brain mechanisms underlying pain empathy and social modulation of pain in the patient-clinician interaction. (PNAS 2023)

- DOI: 10.1073/pnas.2212910120 | PMCID: PMC10293846 | PMID: 37339198
- Version used: **6.0.0**
- Evidence: Individual fMRI datasets were preprocessed using tools from FMRIB’s Software Library (FSL, v6.0.0; www.fmrib.ox.ac.uk/fsl ) and included the following steps: slice-timing correction, motion correction (MCFLIRT) ( 90 ), correction of spatial inhomogeneity (TOPUP) ( 91 , 92 ), nonbrain tissue removal (BET) ( 93 ), spatial smoothing (full width at half maximum = 4 mm), temporal high-pass filtering (f...
- Full pipeline: registration [FSL v6.0.0, FreeSurfer v6.0.0] -> stage not stated [R]

### Brain imaging and neuropsychological assessment of individuals recovered from a mild to moderate SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217232120 | PMCID: PMC10235949 | PMID: 37220275
- Evidence: Normalized volumes of white matter hyperintensities (WMH load) were obtained by FSL’s Brain Intensity AbNormality Classification Algorithm (BIANCA) with LOCally Adaptive Threshold Estimation (LOCATE) ( 68 , 69 ).
- Full pipeline: normalisation [FSL] -> dimensionality reduction/clustering [Python v3.9.1] -> differential/statistical testing [Python v3.9.1] -> stage not stated [R, scikit-learn v1.0.2]

### Human and chimpanzee shared and divergent neurobiological systems for general and specific cognitive brain functions. (PNAS 2023)

- DOI: 10.1073/pnas.2218565120 | PMCID: PMC10235977 | PMID: 37216540
- Evidence: DWI images were preprocessed using FSL ( 112 ), including correction for eddy-current, motion, and susceptibility distortions (Supplementary Methods).
- Full pipeline: stage not stated [FSL, FreeSurfer]

### MWF of the corpus callosum is a robust measure of remyelination: Results from the ReBUILD trial. (PNAS 2023)

- DOI: 10.1073/pnas.2217635120 | PMCID: PMC10193980 | PMID: 37155847
- Evidence: MWF maps and FLAIR images were coregistered to the corresponding T 1 space, using linear and nonlinear transformations of FSL software library (FLIRT/FNIRT) ( 36 , 37 ).
- Full pipeline: stage not stated [FSL]

### Learning rules of engagement for social exchange within and between groups. (PNAS 2023)

- DOI: 10.1073/pnas.2218443120 | PMCID: PMC10175835 | PMID: 37126724
- Evidence: Following preprocessing ( SI Appendix , Section III.3 ), neuroimaging data were analyzed with FSL (Oxford Centre for Functional MRI of the Brain Software Library; www.fmrib.ox.ac.uk/fsl ).
- Full pipeline: stage not stated [FSL]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Version used: **5.0.9**
- Evidence: Brain tissue segmentation of cerebrospinal fluid (CSF), white matter (WM), and gray matter (GM) was performed on the brain-extracted T1w using fast (FSL 5.0.9, 125 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Human brain effects of DMT assessed via EEG-fMRI. (PNAS 2023)

- DOI: 10.1073/pnas.2218949120 | PMCID: PMC10068756 | PMID: 36940333
- Evidence: ...I ( 73 )] by registering each volume to the most similar volume, in the least squares sense, to all others (in-house code); 4) brain extraction [BET, FSL ( 74 )]; 5) rigid body registration to anatomical scans; 6) nonlinear registration to 2mm MNI brain [Symmetric Normalization, Advanced Normalization Tools (ANTS) ( 75 )]; 7) scrubbing—using an FD threshold of 0.4 and scrubbed volumes were replace...
- Full pipeline: normalisation [ANTs, FSL] -> registration [AFNI, ANTs, FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Propofol disrupts alpha dynamics in functionally distinct thalamocortical networks during loss of consciousness. (PNAS 2023)

- DOI: 10.1073/pnas.2207831120 | PMCID: PMC10089159 | PMID: 36897972
- Evidence: The data were further processed with FMRIB Software Library's (FSL's) BEDPOSTX (Bayesian Estimation of Diffusion Parameters Obtained using Sampling Techniques, modeling crossing X fibers) to model white matter fiber orientations and crossing fibers for probabilistic tractography.
- Full pipeline: registration [FreeSurfer] -> differential/statistical testing [FSL]

### Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. (PNAS 2023)

- DOI: 10.1073/pnas.2216399120 | PMCID: PMC9992854 | PMID: 36802420
- Evidence: Indeed, these scans present a remarkable white–gray matter contrast and can be easily analyzed with widespread neuroimaging packages, such as SPM ( 1 ), FSL ( 2 ), or FreeSurfer ( 3 ), to derive quantitative morphometric measurements.
- Full pipeline: stage not stated [FSL, FreeSurfer, Keras, TensorFlow]

### Brain aerobic glycolysis and resilience in Alzheimer disease. (PNAS 2023)

- DOI: 10.1073/pnas.2212256120 | PMCID: PMC9963219 | PMID: 36745794
- Evidence: Each FLAIR scan was first preprocessed with tools in FMRIB Software Library (FSL) for brain extraction ( 67 ), bias field correction ( 68 ), and rigid body registration ( 69 ) to an individual’s corresponding T1 image.
- Full pipeline: registration [FSL] -> stage not stated [FreeSurfer]

### Breathing orchestrates synchronization of sleep oscillations in the human hippocampus. (PNAS 2024)

- DOI: 10.1073/pnas.2405395121 | PMCID: PMC11670218 | PMID: 39680758
- Evidence: We used preoperative structural MRI scans and postoperative computed tomography (CT) scans to localize electrodes using FMRIB Software Library’s (FSL) registration tool flirt (RRID: SCR_002823) as described previously ( 88 , 89 ).
- Full pipeline: registration [FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Prenatal social disadvantage is associated with alterations in functional networks at birth. (PNAS 2024)

- DOI: 10.1073/pnas.2405448121 | PMCID: PMC11648631 | PMID: 39621900
- Evidence: Field distortion correction was performed, using the FSL TOPUP toolbox ( http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TOPUP ) and applied with FSL’s applytopup.
- Full pipeline: alignment/mapping [Connectome Workbench v1.2.3] -> stage not stated [FSL]

### Secondary thalamic dysfunction underlies abnormal large-scale neural dynamics in chronic stroke. (PNAS 2024)

- DOI: 10.1073/pnas.2409345121 | PMCID: PMC11573628 | PMID: 39503890
- Evidence: To fit diffusion tensors and thereby estimate MD, a brain mask was first extracted from the reference image using FSL’s ( 75 ) Brain Extraction Tool ( 76 ), then eddy was applied to the brain-masked diffusion-weighted images for outlier removal, motion correction, and eddy current correction [Eddy CUDA 9.1 ( 77 – 79 ); FWHM = 2, 16 degrees of freedom].
- Full pipeline: registration [FSL] -> differential/statistical testing [lme4 v1.1] -> stage not stated [FreeSurfer]

### V1 neurons are tuned to perceptual borders in natural scenes. (PNAS 2024)

- DOI: 10.1073/pnas.2221623121 | PMCID: PMC11572972 | PMID: 39495929
- Evidence: From the anatomical MRI, white matter was automatically segmented using the FMRIB’s Software Library (FSL) ( 52 ).
- Full pipeline: stage not stated [FSL]

### High-level cognition is supported by information-rich but compressible brain activity patterns. (PNAS 2024)

- DOI: 10.1073/pnas.2400082121 | PMCID: PMC11363287 | PMID: 39178232
- Evidence: Functional data were preprocessed and analyzed using FSL (Functional Magnetic Resonance Imaging of the Brain Software Library; www.fmrib.ox.ac.uk/fsl ), including correction for head motion and slice-acquisition time, spatial smoothing (6 mm full width half maximum Gaussian kernel), and high-pass temporal filtering (140 s period).
- Full pipeline: registration [FSL]

### Evidence of association between higher cardiorespiratory fitness and higher cerebral myelination in aging. (PNAS 2024)

- DOI: 10.1073/pnas.2402813121 | PMCID: PMC11363304 | PMID: 39159379
- Evidence: For each participant, using the FLIRT analysis as implemented in FSL software, all SPGR, bSSFP, or DAM images were linearly registered to the SPGR image obtained at FA of 8° and the respective derived transformation matrices were then applied to the original SPGR, bSSFP, or DAM images.
- Full pipeline: stage not stated [FSL]

### Callousness, exploitativeness, and tracking of cooperation incentives in the human default network. (PNAS 2024)

- DOI: 10.1073/pnas.2307221121 | PMCID: PMC11260090 | PMID: 38980906
- Evidence: Voxelwise general linear model analyses were conducted using FSL FEAT v6.0 via fmri.factory ( 67 ), an R package that streamlines model-based fMRI analyses.
- Full pipeline: differential/statistical testing [FSL, R] -> stage not stated [fMRIPrep v20.1.1]

### A familiar face and person processing area in the human temporal pole. (PNAS 2024)

- DOI: 10.1073/pnas.2321346121 | PMCID: PMC11252731 | PMID: 38954551
- Version used: **6.0.3**
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: BMDMs from Chat fl/fl and Chat fl/fl Lyz2 cre mice were treated with or without LPS, Pam3, or FSL-1 for 24 h, and then washed twice with PBS.
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Natural scenes reveal diverse representations of 2D and 3D body pose in the human brain. (PNAS 2024)

- DOI: 10.1073/pnas.2317707121 | PMCID: PMC11181088 | PMID: 38830105
- Evidence: These tools are based on a nonlinear mapping from each subject’s T1 to the MNI152 T1 template as determined using FSL’s fnirt utility.
- Full pipeline: alignment/mapping [FSL]

### Characteristic BOLD signals are detectable in white matter of the spinal cord at rest and after a stimulus. (PNAS 2024)

- DOI: 10.1073/pnas.2316117121 | PMCID: PMC11145258 | PMID: 38776372
- Evidence: The fMRI data were registered to a customized spinal cord template using FSL to perform group analysis ( 53 ).
- Full pipeline: stage not stated [FSL, SPM]

### Subcallosal cingulate deep brain stimulation evokes two distinct cortical responses via differential white matter activation. (PNAS 2024)

- DOI: 10.1073/pnas.2314918121 | PMCID: PMC10998591 | PMID: 38527192
- Evidence: MR and CT images were processed using the FMRIB Software Library (FSL, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/ ) and the Analysis of Functional Neuroimages toolbox (AFNI, https://afni.nimh.nih.gov/ ) ( 44 , 45 ).
- Full pipeline: stage not stated [AFNI, Camino, FSL, Matplotlib v3.8.0, NumPy v1.24.4, SciPy v1.11.2, seaborn v0.12.2]

### The dorsomedial prefrontal cortex prioritizes social learning during rest. (PNAS 2024)

- DOI: 10.1073/pnas.2309232121 | PMCID: PMC10962978 | PMID: 38466844
- Version used: **5.0.9**
- Evidence: Brain tissue segmentation of cerebrospinal fluid (CSF), white matter (WM) and gray matter (GM) was performed on the brain-extracted T1w using fast [FSL 5.0.9, RRID:SCR_002823, ( 89 )].
- Full pipeline: stage not stated [ANTs v2.3.3, FSL v5.0.9, FreeSurfer, Nipype v1.6.1, fMRIPrep v20.2.2]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: First, the blip-up and blip-down M 0 images were processed with FSL to estimate the phase-encoding distortion correction using FSL’s topup ( 41 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Evolutionary continuity and divergence of auditory dorsal and ventral pathways in primates revealed by ultra-high field diffusion MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2313831121 | PMCID: PMC10907247 | PMID: 38377216
- Evidence: The dMRI data of marmosets and macaque were denoised using the dwidenoise function implemented in MRtrix3 ( 94 ) and eddy current corrected using the eddy_correct function of FSL ( 95 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [FSL, MRtrix3]

### The central renin-angiotensin system: A genetic pathway, functional decoding, and selective target engagement characterization in humans. (PNAS 2024)

- DOI: 10.1073/pnas.2306936121 | PMCID: PMC10895353 | PMID: 38349873
- Evidence: Next, the resulting average brain was registered to the MNI stereotactic standard space using FSL linear registration and averaged so that each AT1R gene mRNA is represented in a single voxel-by-voxel brain map.
- Full pipeline: alignment/mapping [SPM] -> registration [FSL] -> differential/statistical testing [SPM] -> stage not stated [Nilearn, Nipype v1.5.1, fMRIPrep v20.2.1]

### Individuals who see the good in the bad engage distinctive default network coordination during post-encoding rest. (PNAS 2024)

- DOI: 10.1073/pnas.2306295121 | PMCID: PMC10769837 | PMID: 38150498
- Evidence: Functional and anatomical brain images were reoriented using SPM and skull-stripped using the Brain Extraction Tool in FSL.
- Full pipeline: registration [FSL]

### Creatine kinase imaging (CKI) for in vivo whole-brain mapping of creatine kinase reaction kinetics. (PNAS 2025)

- DOI: 10.1073/pnas.2505323122 | PMCID: PMC12664012 | PMID: 41264241
- Version used: **6.0.7.8**
- Evidence: All 1 H MR image processing and analysis were performed using FSL version 6.0.7.8 ( 70 ).
- Full pipeline: stage not stated [FSL v6.0.7.8]

### The synergy of methylphenidate- and reconsolidation-based extinction normalizes ventromedial prefrontal function in drug addiction. (PNAS 2025)

- DOI: 10.1073/pnas.2512310122 | PMCID: PMC12625820 | PMID: 41187084
- Evidence: All CS events (i.e., reminded CS+, nonreminded CS+, CS−) were sampled from their onset to offset (4 s) and convolved with a double-gamma hemodynamic response function to be included in the general linear model (GLM) along with their temporal derivatives using FSL’s FEAT [version 6.0.7.4 ( 55 )].
- Full pipeline: differential/statistical testing [FSL] -> stage not stated [fMRIPrep]

### Habenula-ventral tegmental area functional coupling and risk aversion in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2500815122 | PMCID: PMC12595472 | PMID: 41166429
- Evidence: Preprocessing was performed using tools from FMRIB Software Library (FSL) ( 93 ).
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [FSL, PsychoPy v2021.1.4, lavaan]

### Parallel systems for social and spatial cognition reaching the cortical apex. (PNAS 2025)

- DOI: 10.1073/pnas.2520067122 | PMCID: PMC12595413 | PMID: 41166425
- Version used: **6.0.3**
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### In vivo parcellation of the human superior colliculus from brain-wide probabilistic connectivity. (PNAS 2025)

- DOI: 10.1073/pnas.2518549122 | PMCID: PMC12595446 | PMID: 41166427
- Evidence: Probabilistic tractography was performed using FSL’s GPU-accelerated bedpostx and probtrackx (10,000 streamlines) seeded from SC ROIs.
- Full pipeline: stage not stated [FSL]

### Decreased hippocampal neurite density in late-middle-aged adults following prenatal exposure to higher levels of maternal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2420188122 | PMCID: PMC12595415 | PMID: 41144670
- Evidence: Susceptibility-induced distortions were then calculated using top-up from FSL Version 6.0.5.1 ( 128 , 129 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, MRtrix3, R v4.2.1, tidyverse]

### Full interhemispheric integration sustained by a fraction of posterior callosal fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2520190122 | PMCID: PMC12582319 | PMID: 41118210
- Evidence: ...ions that were transected by the surgery: These masks were specified in the fixed image space (i.e., the MNI152NLin6Asym template, as provided by the FMRIB Software Library, FSL) ( 66 , 67 ) because we lacked preoperative data for each patient, and CC segments were defined by the JHU-DTI white matter atlas ( 68 , 69 ) (also provided in FSL).
- Full pipeline: alignment/mapping [ANTs, SPM] -> normalisation [ANTs, SPM] -> registration [QSIPrep, fMRIPrep] -> differential/statistical testing [ANTs, SPM] -> stage not stated [FSL]

### From retinotopic to ordinal coding: Dissecting the cortical stages of visual word recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2507291122 | PMCID: PMC12582272 | PMID: 41118216
- Evidence: The raw functional data underwent distortion correction using FSL top-up ( https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/topup ).
- Full pipeline: normalisation [Python] -> differential/statistical testing [Python] -> stage not stated [FSL, MNE-Python, PyTorch, SPM]

### Fundamental features of social environments determine rate of social affiliation. (PNAS 2025)

- DOI: 10.1073/pnas.2506243122 | PMCID: PMC12557543 | PMID: 41086216
- Evidence: FMRI data were preprocessed and analyzed using FMRIB’s Software Library ( 50 ) (FSL), Python ( 51 ), and the package fslpy to interface with FSL ( 52 ).
- Full pipeline: stage not stated [FSL, R v4.3]

### Disentangling metabolic and neurovascular timescales supporting cognitive processes. (PNAS 2025)

- DOI: 10.1073/pnas.2506513122 | PMCID: PMC12501135 | PMID: 40982680
- Evidence: The preprocessing of resting-state and n-back fMRI conditions was implemented using an FSL-based automated pipeline ( https://github.com/tambalostefano/lnifmri_prep ) that included common steps: 1) slice timing correction; 2) T1-weighted image tissue segmentation; 3) geometric distortion and head motion correction; 4) coregistration of the T1-weighted image to the time series.
- Full pipeline: registration [FSL] -> stage not stated [SPM]

### Joint models reveal human subcortical underpinnings of choice and learning behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2502269122 | PMCID: PMC12435315 | PMID: 40911596
- Evidence: Run-level GLMs were estimated using FSL FEAT ( 144 ), and afterward the three run-level GLMs per participant were combined with a fixed effects analysis.
- Full pipeline: registration [ANTs] -> stage not stated [FSL, Nipype v1.5.1, fMRIPrep v20.2.0, lme4]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Evidence: First, fMRIPrep generated a reference volume and its skull-stripped version, which was used to estimate head motion using the mcflirt algorithm in FSL.
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

### Orexin effect on physiological pulsations of the human brain. (PNAS 2025)

- DOI: 10.1073/pnas.2501578122 | PMCID: PMC12337265 | PMID: 40748959
- Evidence: The Oxford Centre for Functional MRI of the brain (FMRIB) software library (FSL) ( 72 ) FEAT pipeline was used for MREG data preprocessing.
- Full pipeline: registration [AFNI] -> stage not stated [FSL]

### Trauma-predictive brain network connectivity adaptively responds to mild acute stress. (PNAS 2025)

- DOI: 10.1073/pnas.2505965122 | PMCID: PMC12327799 | PMID: 40737323
- Evidence: CPM and all experiments: Preprocessing. fMRI data were preprocessed using an identical pipeline in FSL ( 55 ).
- Full pipeline: stage not stated [FSL]

### Action-mode subnetworks for decision-making, action control, and feedback. (PNAS 2025)

- DOI: 10.1073/pnas.2502021122 | PMCID: PMC12260544 | PMID: 40587801
- Version used: **6.0**
- Evidence: FSL 6.0, https://fsl.fmrib.ox.ac.uk/fsl/fslwiki ( 139 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [Connectome Workbench v1.0, FSL v6.0]

### Longitudinal trajectories of brain development from infancy to school age and their relationship with literacy development. (PNAS 2025)

- DOI: 10.1073/pnas.2414598122 | PMCID: PMC12184337 | PMID: 40493188
- Evidence: DWI data were first denoised using Marchenko–Pastur principal component analysis ( 123 – 125 ) and then corrected for susceptibility distortions, eddy currents, motion, and intensity inhomogeneity using FSL’s topup and eddy (with slice-to-volume correction) functions ( 126 – 130 ), and ANTs' N4 bias correction tool ( 131 ).
- Full pipeline: dimensionality reduction/clustering [ANTs, FSL, R] -> differential/statistical testing [R, lme4] -> simulation/modelling [lme4] -> stage not stated [Docker v1.1.0, FreeSurfer v7.3, MRtrix3]

### Shared disbelief and shared belief: Belief and disbelief as drivers of interpersonal neural synchronization during narrative processing. (PNAS 2025)

- DOI: 10.1073/pnas.2422396122 | PMCID: PMC12167953 | PMID: 40472031
- Version used: **5.0**
- Evidence: The data for the two narratives were subjected to the following preprocessing steps, separately: 1) brain extraction for skull stripping the anatomical images using the FSL 5.0.
- Full pipeline: registration [FSL v5.0] -> stage not stated [dcm2niix]

### Structure-function coupling in the first month of life: Associations with age and attention. (PNAS 2025)

- DOI: 10.1073/pnas.2412729122 | PMCID: PMC12168018 | PMID: 40455980
- Evidence: Field distortion correction was calculated, using the FSL TOPUP toolbox ( https://fsl.fmrib.ox.ac.uk/fsl/ fslwiki/TOPUP), and distortion correction applied with applytopup ( 113 ).
- Full pipeline: alignment/mapping [Connectome Workbench v1.2.3] -> stage not stated [FSL]

### Longitudinal associations between birth-to-six cortical growth and childhood neurocognitive function. (PNAS 2025)

- DOI: 10.1073/pnas.2418176122 | PMCID: PMC12146774 | PMID: 40424148
- Evidence: A generalized linear model (GLM) was created using FSL ( 54 ) at the individual level that included 2-back, 0-back, and rest trials, as well as regressors of no interest for motion, global signal, white matter, and cerebrospinal fluid ( SI Appendix ).
- Full pipeline: alignment/mapping [FreeSurfer] -> registration [FreeSurfer] -> differential/statistical testing [FSL, lme4] -> stage not stated [fMRIPrep v20.0.7]

### Mapping global brain reconfigurations following local targeted manipulations. (PNAS 2025)

- DOI: 10.1073/pnas.2405706122 | PMCID: PMC12037044 | PMID: 40249780
- Evidence: Data processing [FSL software ( 85 )] included motion correction, regression of the volumes affected by motion and by sudden changes in BOLD signal intensity, skull stripping, bias field correction, slice timing correction, grand-mean intensity normalization, band pass filtering (0.01 to 0.1 Hz), registration to Allen Template using linear and nonlinear transformations and spatial smoothing with a...
- Full pipeline: normalisation [FSL] -> registration [FSL] -> differential/statistical testing [FSL]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Version used: **5.0.9**
- Evidence: Brain tissue segmentation of cerebrospinal fluid (CSF), white matter (WM), and gray matter (GM) was performed on the brain-extracted T1w using fast (FSL 5.0.9) ( 56 ).
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### Neural basis for individual differences in the attention-enhancing effects of methylphenidate. (PNAS 2025)

- DOI: 10.1073/pnas.2423785122 | PMCID: PMC12002349 | PMID: 40127280
- Evidence: First-level voxel-wise analyses were carried out with the general linear model in the FMRIB Software Library using the “FEAT” toolbox, estimating brain activation responses to the visual attention task for each fMRI run and subject ( 86 ).
- Full pipeline: differential/statistical testing [FSL, SPM] -> stage not stated [FreeSurfer v5.3.0, R]

### Protective role of parenthood on age-related brain function in mid- to late-life. (PNAS 2025)

- DOI: 10.1073/pnas.2411245122 | PMCID: PMC11892684 | PMID: 39999172
- Evidence: Briefly, each fMRI dataset was spatially normalized to MNI152 2-mm template space and FMRIB’s ICA-based classifier [FSL-FIX; ( 41 )] was trained on holdout set of participants and applied to the remaining participants to denoise the data.
- Full pipeline: normalisation [FSL, R] -> registration [FSL] -> machine learning [FSL]

### Specialization of the human hippocampal long axis revisited. (PNAS 2025)

- DOI: 10.1073/pnas.2422083122 | PMCID: PMC11760929 | PMID: 39808662
- Version used: **5.0.4**
- Evidence: Task MRI data were analyzed using run-specific general linear models (GLMs) implemented through FSL (version 5.0.4) first-level FEAT ( 74 ).
- Full pipeline: differential/statistical testing [FSL v5.0.4] -> visualisation [Connectome Workbench] -> stage not stated [FreeSurfer]

### Expansion of a conserved architecture drives the evolution of the primate visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421585122 | PMCID: PMC11761675 | PMID: 39805017
- Evidence: Analysis of Functional NeuroImages (AFNI; RRID:nif-0000-00259; Cox, 1996), SUMA ( 116 ), Freesurfer (FreeSurfer, RRID:nif-0000-00304) ( 117 , 118 ), FSL ( 119 ) (FSL, RRID:birnlex_2067), Advanced Normalization Tools ( 120 ) (ANTs), and MATLAB (MATLAB, RRID:nlx_153890) were used for additional data processing.
- Full pipeline: normalisation [AFNI, ANTs, FSL, SUMA] -> structure determination [FreeSurfer]

### Human brain dynamics are shaped by rare long-range connections over and above cortical geometry. (PNAS 2025)

- DOI: 10.1073/pnas.2415102122 | PMCID: PMC11725837 | PMID: 39752525
- Evidence: In summary, the data underwent preprocessing using the HCP pipeline, which employs standardized methods with FSL (FMRIB Software Library), FreeSurfer, and Connectome Workbench software.
- Full pipeline: stage not stated [Connectome Workbench, FSL, FieldTrip, FreeSurfer]

### Memory control deficits in the sleep-deprived human brain. (PNAS 2025)

- DOI: 10.1073/pnas.2400743122 | PMCID: PMC11725914 | PMID: 39739795
- Version used: **5.0**
- Evidence: Event-related fMRI data were analyzed using the FMRIB Software Library (FSL version 5.0; https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT/ ).
- Full pipeline: stage not stated [CONN toolbox, FSL v5.0, R]

### Metabolism-weighted brain connectome reveals synaptic integration and vulnerability to neurodegeneration. (PNAS 2026)

- DOI: 10.1073/pnas.2531706123 | PMCID: PMC13321360 | PMID: 42330267
- Evidence: DWI preprocessing and probabilistic tractography were executed using MRtrix3 ( 54 ), FSL, and Advanced Normalization Tools (ANTs), incorporating denoising, eddy-current correction, motion correction (using FSL top-up), and bias-field correction (using ANTs).
- Full pipeline: normalisation [ANTs, FSL, MRtrix3] -> registration [ANTs, FSL, MRtrix3] -> stage not stated [Enrichr, Metascape]

### Incentive valence differentially engages open- and closed-loop basal ganglia circuits during movement initiation. (PNAS 2026)

- DOI: 10.1073/pnas.2537314123 | PMCID: PMC13167725 | PMID: 42090262
- Evidence: Multi-echo fMRI data were preprocessed using ANTs, FSL, and Tedana (v24.0.1).
- Full pipeline: stage not stated [ANTs, CONN toolbox, FSL]

### Sender-receiver subdivisions of the default mode network in perceptual and memory-guided cognition. (PNAS 2026)

- DOI: 10.1073/pnas.2528851123 | PMCID: PMC13079981 | PMID: 41945445
- Version used: **6.0**
- Evidence: All functional and structural data were preprocessed using a standard pipeline and analyzed via the FMRIB (Functional Magnetic Resonance Imaging of the Brain) Software Library (FSL version 6.0, www.fmrib.ox.ac.uk/fsl ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL v6.0, emmeans, lme4]

### Sleep alters neurovascular and hydrodynamic coupling in the human brain. (PNAS 2026)

- DOI: 10.1073/pnas.2510731123 | PMCID: PMC13012097 | PMID: 41849399
- Evidence: Image preprocessing followed the standardized FSL (Functional MRI of the Brain’s software library) preprocessing pipeline ( 52 ).
- Full pipeline: stage not stated [FSL]

### Medullary and C3-C4 propriospinal pathways underlying mammalian forelimb movement control. (PNAS 2026)

- DOI: 10.1073/pnas.2518217123 | PMCID: PMC12867695 | PMID: 41604259
- Evidence: FSL software was employed for fMRI data analysis ( 86 ).
- Full pipeline: stage not stated [FSL]

### Distinct contributions of hippocampal pathways in learning regularities and exceptions revealed by functional footprints. (PNAS 2026)

- DOI: 10.1073/pnas.2503388123 | PMCID: PMC12818569 | PMID: 41543896
- Evidence: The fieldmap was then coregistered to the target EPI (echo-planar imaging) reference run and converted to a displacements field map (amenable to registration tools such as ANTs) with FSL’s fugue and other SDCflows tools.
- Full pipeline: normalisation [ANTs] -> registration [FSL] -> differential/statistical testing [R, lme4 v1.1] -> stage not stated [FreeSurfer, MRtrix3, Nipype v1.5.1, fMRIPrep v20.2.1]

### Primate-informed neural network for visual decision-making. (PNAS 2026)

- DOI: 10.1073/pnas.2426883123 | PMCID: PMC12799151 | PMID: 41512039
- Evidence: The fMRI data were preprocessed using FSL , including slice timing correction, motion correction, and field-map correction.
- Full pipeline: registration [FSL]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Probabilistic tractography was performed in FSL ( 88 ) using the probtrackx tool.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

