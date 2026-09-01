# ANTs

- **Category:** neuroimaging
- **Papers in survey:** 55
- **Journals:** PNAS (44), Nature (9), Science (1), Cell (1)
- **Years:** 2021 (3), 2022 (17), 2023 (10), 2024 (6), 2025 (12), 2026 (7)
- **Versions named:** 2.2.0 (3), 2.1 (1), 2.1.0 (1), 2.3.3 (1), 2.3.5 (1)
- **Pipeline stages it appears in:** normalisation (29), registration (15), alignment/mapping (9), dimensionality reduction/clustering (3), differential/statistical testing (2), visualisation (1)

## Papers

### A brainstem integrator for self-location memory and positional homeostasis in zebrafish. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.022 | PMCID: PMC11605990 | PMID: 36563666
- Evidence: We first registered all volumes to the volume recorded halfway through the experiment using ANTs.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: Image registration Image registration was performed using Advanced Normalization Tools (ANTs 51 ) running on the MPCDF Draco/Raven Garching computing cluster.
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### Reproducible brain-wide association studies require thousands of individuals. (Nature 2022)

- DOI: 10.1038/s41586-022-04492-9 | PMCID: PMC8991999 | PMID: 35296861
- Evidence: ANTs 56 DenoiseImage models scanner noise as a Rician distribution and attempts to remove such noise from the T1 and T2 anatomical images.
- Full pipeline: normalisation [FreeSurfer] -> stage not stated [ANTs, Connectome Workbench, FSL]

### An orexigenic subnetwork within the human hippocampus. (Nature 2023)

- DOI: 10.1038/s41586-023-06459-w | PMCID: PMC10499606 | PMID: 37648849
- Version used: **2.1.0**
- Evidence: Co-registration was performed using Advanced Normalization Tools (ANTs, v.2.1.0), and consisted of two successive steps of linear and nonlinear registration between the individual’s brain and the MNI brain.
- Full pipeline: alignment/mapping [SPM] -> normalisation [ANTs v2.1.0] -> registration [ANTs v2.1.0] -> differential/statistical testing [SPM] -> stage not stated [FSL, FieldTrip, Python v3.6, fMRIPrep v1.2.3]

### Wake-like skin patterning and neural activity during octopus sleep. (Nature 2023)

- DOI: 10.1038/s41586-023-06203-4 | PMCID: PMC10322707 | PMID: 37380770
- Evidence: 3D images of individual octopus brains were mapped to this reference atlas using the symmetric image normalization method (SyN) method implemented in the Advanced Normalization Tools (ANTs) library 56 .
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> machine learning [Keras, TensorFlow v2.0] -> stage not stated [Python v3.6, scikit-image]

### Abstract representations emerge in human hippocampal neurons during inference. (Nature 2024)

- DOI: 10.1038/s41586-024-07799-x | PMCID: PMC11338822 | PMID: 39143207
- Version used: **2.1**
- Evidence: Electrode locations were coregistered to the to the MNI152-aligned CIT168 probabilistic atlas 61 for standardized location reporting and visualization using Advanced Normalization Tools v.2.1 (refs.
- Full pipeline: alignment/mapping [ANTs v2.1] -> normalisation [ANTs v2.1] -> visualisation [ANTs v2.1]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Image alignment was performed using the Advanced Normalization Tools (ANTs) 82 .
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### A mouse brain stereotaxic topographic atlas with isotropic 1-μm resolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09211-8 | PMCID: PMC12422980 | PMID: 40604274
- Evidence: Using a 2D nonlinear registration method provided by the ANTs tool, we registered the immunohistochemical data onto the selected coronal plane.
- Full pipeline: registration [ANTs] -> stage not stated [ImageJ]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: HCR data were registered onto the standard brain as previously described 28 using Advanced Normalization Tools (ANTs) 71 .
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### Parkinson's disease as a somato-cognitive action network disorder. (Nature 2026)

- DOI: 10.1038/s41586-025-10059-1 | PMCID: PMC13017517 | PMID: 41639440
- Evidence: For MP2RAGE T1w images of the PIPD, TMS and MRgFUS dataset, the brain was first extracted from the uniform T1-weighted image using Advanced Normalized Tools (ANTs) 110 .
- Full pipeline: normalisation [ANTs, FSL] -> registration [FSL, FreeSurfer v6.0.0] -> simulation/modelling [FieldTrip] -> stage not stated [Connectome Workbench v1.5]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Evidence: Processing within the pipeline made use of the following Python libraries: Nipype ( 49 ), the Advanced Normalization Tools ( 50 ), the Insight Toolkit ( 51 ), Scikit-image ( 52 ), Scikit-learn ( 53 ), and SciPy ( 54 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Attention, awareness, and the right temporoparietal junction. (PNAS 2021)

- DOI: 10.1073/pnas.2026099118 | PMCID: PMC8237657 | PMID: 34161276
- Evidence: Spatial normalization to the ICBM 152 Nonlinear Asymmetrical template version 2009c ( 36 ) (RRID: SCR_008796 ) was performed through nonlinear registration with the antsRegistration tool of Advanced Normalization Tools (ANTs) version 2.2.0 using brain-extracted versions of both T1w volume and template.
- Full pipeline: normalisation [ANTs] -> registration [AFNI, ANTs] -> stage not stated [FSL, Nilearn, Nipype, fMRIPrep v1.2.3]

### Cellular-resolution gene expression profiling in the neonatal marmoset brain reveals dynamic species- and region-specific differences. (PNAS 2021)

- DOI: 10.1073/pnas.2020125118 | PMCID: PMC8106353 | PMID: 33903237
- Evidence: For final alignment with the MRI, we used the Advanced Normalization Tools (ANTS) image registration toolkit to align the 3D image stack with the 3D MRI image using a 3D deformable image transformation ( 39 , 40 ).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [ANTs] -> stage not stated [ImageJ]

### Compulsive drug-taking is associated with habenula-frontal cortex connectivity. (PNAS 2022)

- DOI: 10.1073/pnas.2208867119 | PMCID: PMC9897479 | PMID: 36469769
- Evidence: The fMRI images were aligned to their corresponding T2-weighted image and normalized to a 3D template aligned with a rat stereotaxic atlas ( 72 ) using Advanced Normalization Tools ( https://stnava.github.io/ANTs/ ).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [AFNI, FSL]

### Neural event segmentation of continuous experience in human infants. (PNAS 2022)

- DOI: 10.1073/pnas.2200257119 | PMCID: PMC9618143 | PMID: 36252007
- Evidence: In an additional exploratory analysis, we realigned participants’ anatomical data to the adult standard using Advanced Normalization Tools (ANTs) ( 73 ), a nonlinear alignment algorithm.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> registration [ANTs] -> stage not stated [AFNI, FSL]

### Morphological similarity of amygdala-ventral prefrontal pathways represents trait anxiety in younger and older adults. (PNAS 2022)

- DOI: 10.1073/pnas.2205162119 | PMCID: PMC9586323 | PMID: 36215497
- Evidence: A brain mask was created based on the FreeSurfer segmentation results, and diffeomorphic nonlinear registration of the ANTs SyN algorithm ( 73 ) was used to compute a spatial transformation between the individual’s T1-weighted image and the Montreal Neurological Institute (MNI) 152 1-mm standard space.
- Full pipeline: registration [ANTs] -> differential/statistical testing [R v4.0] -> structure determination [FreeSurfer] -> machine learning [MRtrix3] -> stage not stated [FSL]

### Hippocampal ripples signal contextually mediated episodic recall. (PNAS 2022)

- DOI: 10.1073/pnas.2201657119 | PMCID: PMC9546603 | PMID: 36161912
- Evidence: Structural MRI and computed tomography scans were coregistered by using Advanced Normalization Tools ( 28 ) to align the brain regions to the electrode montage.
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> differential/statistical testing [statsmodels]

### Structural basis and molecular mechanism of biased GPBAR signaling in regulating NSCLC cell growth via YAP activity. (PNAS 2022)

- DOI: 10.1073/pnas.2117054119 | PMCID: PMC9303995 | PMID: 35858343
- Evidence: We detected the expression of GPBAR in 28 NSCLC tissues paired with adjacent noncancerous tissues (ANTs) by IHC.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ANTs, CTFFIND]

### Adolescent development of multiscale structural wiring and functional interactions in the human connectome. (PNAS 2022)

- DOI: 10.1073/pnas.2116673119 | PMCID: PMC9271154 | PMID: 35776541
- Evidence: T1-weighted data were processed using the fusion of neuroimaging preprocessing pipeline integrating AFNI, FSL, FreeSurfer, ANTs, and Workbench ( https://gitlab.com/by9433/funp ) ( 105 – 109 ), which is similar to the minimal preprocessing pipeline for the HCP ( 110 ).
- Full pipeline: stage not stated [AFNI, ANTs, FSL, FreeSurfer, MRtrix3]

### Multilevel atlas comparisons reveal divergent evolution of the primate brain. (PNAS 2022)

- DOI: 10.1073/pnas.2202491119 | PMCID: PMC9231627 | PMID: 35700361
- Evidence: We thus used ANTs ( 50 ) with the original template provided by the atlas in order to segment the template in three components (white matter, gray matter, and cerebrospinal fluid).
- Full pipeline: stage not stated [AFNI, ANTs]

### Reversible modification of mitochondrial ADP/ATP translocases by paired <i>Legionella</i> effector proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2122872119 | PMCID: PMC9191684 | PMID: 35653564
- Evidence: In this study, we identified an L. pneumophila ART, Lpg0080, which ADP ribosylates an arginine residue in mitochondrial ADP/adenosine triphosphate (ATP) translocases (ANTs) and interferes with mitochondrial respiration.
- Full pipeline: stage not stated [ANTs, PHENIX, PyMOL]

### Diffusion MRI-guided theta burst stimulation enhances memory and functional connectivity along the inferior longitudinal fasciculus in mild cognitive impairment. (PNAS 2022)

- DOI: 10.1073/pnas.2113778119 | PMCID: PMC9173759 | PMID: 35594397
- Evidence: The final preprocessing step applied bias field correction to the dataset using the ANTs package ( 81 ).
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs, CONN toolbox, FSL, FreeSurfer, MRtrix3]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: The ANTs mediate the exchange of ATP and ADP from the mitochondria to the cytosol and vice versa.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### The effect of prolonged spaceflight on cerebrospinal fluid and perivascular spaces of astronauts and cosmonauts. (PNAS 2022)

- DOI: 10.1073/pnas.2120439119 | PMCID: PMC9169932 | PMID: 35412862
- Evidence: VSA was segmented with Advanced Normalization Tools.
- Full pipeline: normalisation [ANTs] -> stage not stated [FreeSurfer]

### Progesterone activates GPR126 to promote breast cancer development via the Gi pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2117004119 | PMCID: PMC9169622 | PMID: 35394864
- Evidence: We examined the expression of GPR126 in 14 fresh BC tissues paired with adjacent noncancerous tissues (ANTs) by Western blot.
- Full pipeline: quantification [ImageJ] -> stage not stated [ANTs]

### Optimal deep brain stimulation sites and networks for cervical vs. generalized dystonia. (PNAS 2022)

- DOI: 10.1073/pnas.2114985119 | PMCID: PMC9168456 | PMID: 35357970
- Evidence: In short, postoperative CT or MRI were linearly coregistered to preoperative MRI using advanced normalization tools [ https://stnava.github.io/ANTs/ ( 22 )].
- Full pipeline: normalisation [ANTs] -> stage not stated [FieldTrip]

### Differential effects of early or late exposure to prenatal maternal immune activation on mouse embryonic neurodevelopment. (PNAS 2022)

- DOI: 10.1073/pnas.2114545119 | PMCID: PMC8944668 | PMID: 35286203
- Evidence: Instructions for running the ANTs DBM analysis can be found on GitHub ( https://github.com/CoBrALab/twolevel_ants_dbm ), as can information on MRI preprocessing steps ( https://github.com/CoBrALab/documentation/wiki/Embryo-scan-preprocessing ).
- Full pipeline: differential/statistical testing [R v3.5.1, lme4] -> stage not stated [ANTs, QuPath v0.2.0]

### Hippocampal contributions to novel spatial learning are both age-related and age-invariant. (PNAS 2023)

- DOI: 10.1073/pnas.2307884120 | PMCID: PMC10723126 | PMID: 38055735
- Version used: **2.3.5**
- Evidence: Then, each subfield ROI was transformed into each participant’s native space using Advanced Normalization Tools (ANTs v2.3.5).
- Full pipeline: normalisation [ANTs v2.3.5] -> simulation/modelling [brms] -> stage not stated [FSL, PsychoPy, R v4.2, emmeans, lme4]

### Rats respond to aversive emotional arousal of human handlers with the activation of the basolateral and central amygdala. (PNAS 2023)

- DOI: 10.1073/pnas.2302655120 | PMCID: PMC10655214 | PMID: 37934822
- Version used: **2.2.0**
- Evidence: The preprocessing pipeline started by applying intensity nonuniformity correction to the anatomical images using N4BiasFieldCorrection ( 59 ) from ANTs 2.2.0 ( 60 ).
- Full pipeline: registration [AFNI, FSL v5.0.9] -> differential/statistical testing [SciPy] -> stage not stated [ANTs v2.2.0, ImageJ, Nilearn v0.5.2, Nipype v1.2.0, fMRIPrep v1.4.0]

### Intersubject similarity in neural representations underlies shared episodic memory content. (PNAS 2023)

- DOI: 10.1073/pnas.2308951120 | PMCID: PMC10466090 | PMID: 37603733
- Evidence: The single-item response estimation was conducted in the native space, which was then transformed to the MNI152 space using the antsApplyTransforms tool from the Advanced Normalization Tools ( 58 ).
- Full pipeline: alignment/mapping [BrainNet Viewer] -> normalisation [ANTs, fMRIPrep v1.4.1] -> registration [fMRIPrep v1.4.1] -> stage not stated [vegan]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: Volumetric segmentation and analysis were performed using the NumPy, ANTsPy , and NiBabel packages in Python (Python 3.7).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Merged magnetic resonance and light sheet microscopy of the whole mouse brain. (PNAS 2023)

- DOI: 10.1073/pnas.2218617120 | PMCID: PMC10151475 | PMID: 37068254
- Evidence: 2 using ANTs ( 34 ).
- Full pipeline: stage not stated [ANTs]

### Whole-brain mapping of histaminergic projections in mouse brain. (PNAS 2023)

- DOI: 10.1073/pnas.2216231120 | PMCID: PMC10083611 | PMID: 36976764
- Evidence: Finally, we registered these results by ANTs tools ( 87 ) and loaded the outline of the mouse brain and the results into Amira simultaneously to generate figures.
- Full pipeline: stage not stated [ANTs, ImageJ]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Version used: **2.2.0**
- Evidence: The T1w anatomical scans were corrected for intensity nonuniformity (INU) using N4BiasFieldCorrection (ANTs 2.2.0, 119 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Human brain effects of DMT assessed via EEG-fMRI. (PNAS 2023)

- DOI: 10.1073/pnas.2218949120 | PMCID: PMC10068756 | PMID: 36940333
- Evidence: ...in extraction [BET, FSL ( 74 )]; 5) rigid body registration to anatomical scans; 6) nonlinear registration to 2mm MNI brain [Symmetric Normalization, Advanced Normalization Tools (ANTS) ( 75 )]; 7) scrubbing—using an FD threshold of 0.4 and scrubbed volumes were replaced with the mean of the surrounding volumes.
- Full pipeline: normalisation [ANTs, FSL] -> registration [AFNI, ANTs, FSL] -> stage not stated [FieldTrip, FreeSurfer]

### eLemur: A cellular-resolution 3D atlas of the mouse lemur brain. (PNAS 2024)

- DOI: 10.1073/pnas.2413687121 | PMCID: PMC11648901 | PMID: 39630862
- Evidence: Tissue part in the histology images were aligned to the corresponding parts in the block face image via multiscale 2D rigid registration from Advanced Normalization Tools ( 69 ) in Python.
- Full pipeline: alignment/mapping [ANTs, Python] -> normalisation [ANTs, Python] -> registration [ANTs, Python] -> machine learning [Cellpose v2.0]

### BIFROST: A method for registering diverse imaging datasets of the &lt;i&gt;Drosophila&lt;/i&gt; brain. (PNAS 2024)

- DOI: 10.1073/pnas.2322687121 | PMCID: PMC11588091 | PMID: 39541350
- Evidence: Next, we added a nonlinear transformation step (SyN), the core nonlinear transformation embedded in the widely used registration pipeline ANTs.
- Full pipeline: alignment/mapping [scikit-image] -> registration [ANTs, ImageJ] -> visualisation [Jupyter] -> stage not stated [Snakemake]

### Modeling of brain efflux: Constraints of brain surfaces. (PNAS 2024)

- DOI: 10.1073/pnas.2318444121 | PMCID: PMC11032467 | PMID: 38598340
- Evidence: For each animal, both 3D-TrueFISP volumes acquired with four orthogonal phase encoding directions and DCE FLASH volumes were motion-corrected and spatially normalized with Advanced Normalization Tools (ANTs) (reference: B.
- Full pipeline: normalisation [ANTs]

### The dorsomedial prefrontal cortex prioritizes social learning during rest. (PNAS 2024)

- DOI: 10.1073/pnas.2309232121 | PMCID: PMC10962978 | PMID: 38466844
- Version used: **2.3.3**
- Evidence: The T1-weighted (T1w) image was corrected for intensity nonuniformity (INU) with N4BiasFieldCorrection ( 87 ), distributed with ANTs 2.3.3 ( 88 ), RRID:SCR_004757, and used as T1w-reference throughout the workflow.
- Full pipeline: stage not stated [ANTs v2.3.3, FSL v5.0.9, FreeSurfer, Nipype v1.6.1, fMRIPrep v20.2.2]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: The TSE runs were first resampled to 0.3 mm isotropic resolution and a minimally deformed average TSE template was created from the 0.3 mm TSE datasets using ANTs. ‡ This resampled 0.3 mm isotropic TSE template image was used for manual hippocampal segmentation and was defined as the final reference space for co-registering all other image modalities in the present study.
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Full interhemispheric integration sustained by a fraction of posterior callosal fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2520190122 | PMCID: PMC12582319 | PMID: 41118210
- Evidence: Initial preprocessing relied on functions from the Statistical Parametric Mapping 12 software (SPM12, Wellcome Trust Centre for Neuroimaging, London) in Matlab and Advanced Normalization Tools (ANTs) ( 64 ).
- Full pipeline: alignment/mapping [ANTs, SPM] -> normalisation [ANTs, SPM] -> registration [QSIPrep, fMRIPrep] -> differential/statistical testing [ANTs, SPM] -> stage not stated [FSL]

### Joint models reveal human subcortical underpinnings of choice and learning behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2502269122 | PMCID: PMC12435315 | PMID: 40911596
- Evidence: Prior to estimating R2 * and QSM, the GRE data were brought into MP2RAGE-space by coregistration of the first GRE echo (magnitude image) to the second inversion of the MP2RAGE, using a rigid transformation in ANTs.
- Full pipeline: registration [ANTs] -> stage not stated [FSL, Nipype v1.5.1, fMRIPrep v20.2.0, lme4]

### Interhemispheric resting-state functional connectivity correlates with spontaneous neural interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2505294122 | PMCID: PMC12403092 | PMID: 40825135
- Evidence: To create atlas-based subject-specific stimulus patterns, the Allen mouse brain atlas was coregistered to an anatomical MRI image (ANTs antsRegistrationSyN ), 2D-projected to the dorsal plane, and coregistered to an optical fluorescence image based on the position of fluorescent reference tubes.
- Full pipeline: registration [ANTs]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Evidence: Finally, using antsApplyTransforms (ANTs), images were normalized to the standard MNI152NLin2009cAsym template brain.
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

### Longitudinal trajectories of brain development from infancy to school age and their relationship with literacy development. (PNAS 2025)

- DOI: 10.1073/pnas.2414598122 | PMCID: PMC12184337 | PMID: 40493188
- Evidence: DWI data were first denoised using Marchenko–Pastur principal component analysis ( 123 – 125 ) and then corrected for susceptibility distortions, eddy currents, motion, and intensity inhomogeneity using FSL’s topup and eddy (with slice-to-volume correction) functions ( 126 – 130 ), and ANTs' N4 bias correction tool ( 131 ).
- Full pipeline: dimensionality reduction/clustering [ANTs, FSL, R] -> differential/statistical testing [R, lme4] -> simulation/modelling [lme4] -> stage not stated [Docker v1.1.0, FreeSurfer v7.3, MRtrix3]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Version used: **2.2.0**
- Evidence: The T1-weighted (T1w) image was corrected for intensity nonuniformity using N4BiasFieldCorrection ( 51 ) (ANTs 2.2.0) and used as T1w reference throughout the workflow.
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### Expansion of a conserved architecture drives the evolution of the primate visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421585122 | PMCID: PMC11761675 | PMID: 39805017
- Evidence: Analysis of Functional NeuroImages (AFNI; RRID:nif-0000-00259; Cox, 1996), SUMA ( 116 ), Freesurfer (FreeSurfer, RRID:nif-0000-00304) ( 117 , 118 ), FSL ( 119 ) (FSL, RRID:birnlex_2067), Advanced Normalization Tools ( 120 ) (ANTs), and MATLAB (MATLAB, RRID:nlx_153890) were used for additional data processing.
- Full pipeline: normalisation [AFNI, ANTs, FSL, SUMA] -> structure determination [FreeSurfer]

### Engaging dystonia networks with subthalamic stimulation. (PNAS 2025)

- DOI: 10.1073/pnas.2417617122 | PMCID: PMC11745339 | PMID: 39773021
- Evidence: Briefly, preoperative MRI and postoperative CT/MRI images were first coregistered and then nonlinearly warped to ICBM 2009b Nonlinear Asymmetric (“MNI”) space using advanced normalization tools (ANTs, https://stnava.github.io/ANTs/ ).
- Full pipeline: normalisation [ANTs] -> stage not stated [FieldTrip]

### Metabolism-weighted brain connectome reveals synaptic integration and vulnerability to neurodegeneration. (PNAS 2026)

- DOI: 10.1073/pnas.2531706123 | PMCID: PMC13321360 | PMID: 42330267
- Evidence: DWI preprocessing and probabilistic tractography were executed using MRtrix3 ( 54 ), FSL, and Advanced Normalization Tools (ANTs), incorporating denoising, eddy-current correction, motion correction (using FSL top-up), and bias-field correction (using ANTs).
- Full pipeline: normalisation [ANTs, FSL, MRtrix3] -> registration [ANTs, FSL, MRtrix3] -> stage not stated [Enrichr, Metascape]

### Individual differences in speech monitoring: Functional and structural correlates of delayed auditory feedback. (PNAS 2026)

- DOI: 10.1073/pnas.2530123123 | PMCID: PMC13321129 | PMID: 42330290
- Evidence: The anisotropic power (AP) maps ( 103 ) generated by StarTrack were used to normalize each participant’s DWI data and tractography to the common space of the ICBM 2009a nonlinear symmetric MNI template ( 104 ) using diffeomorphic registration in ANTs ( 105 , 106 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox, SPM, fMRIPrep v23.1.0]

### Incentive valence differentially engages open- and closed-loop basal ganglia circuits during movement initiation. (PNAS 2026)

- DOI: 10.1073/pnas.2537314123 | PMCID: PMC13167725 | PMID: 42090262
- Evidence: Multi-echo fMRI data were preprocessed using ANTs, FSL, and Tedana (v24.0.1).
- Full pipeline: stage not stated [ANTs, CONN toolbox, FSL]

### Phenotypic CRISPR screens identify NLRX1 as an essential activator of the human mitochondrial permeability transition. (PNAS 2026)

- DOI: 10.1073/pnas.2535298123 | PMCID: PMC12956895 | PMID: 41739553
- Evidence: These include the adenosine nucleotide translocases (ANTs) ( 76 , 77 ), the mitochondrial phosphate carrier (PiC) ( 78 ), the voltage-dependent anion channel (VDAC) ( 79 , 80 ), and F 0 F 1 ATP synthase ( 81 – 84 ).
- Full pipeline: stage not stated [ANTs, GSEA, ImageJ]

### Sleep loss induces cholesterol-associated myelin dysfunction. (PNAS 2026)

- DOI: 10.1073/pnas.2523438123 | PMCID: PMC12846829 | PMID: 41557795
- Evidence: FA and restricted fraction (RF) maps were generated (DTI and CHARMED model) and analyzed with tract-based spatial statistics (TBSS) using ANTs normalization and threshold-free cluster enhancement.
- Full pipeline: normalisation [ANTs] -> dimensionality reduction/clustering [ANTs] -> differential/statistical testing [ANTs] -> stage not stated [QuPath]

### Distinct contributions of hippocampal pathways in learning regularities and exceptions revealed by functional footprints. (PNAS 2026)

- DOI: 10.1073/pnas.2503388123 | PMCID: PMC12818569 | PMID: 41543896
- Evidence: All ROIs were registered to the BOLD space of participant-specific runs, using Advanced Normalization Tools (ANTs) ( 56 ).
- Full pipeline: normalisation [ANTs] -> registration [FSL] -> differential/statistical testing [R, lme4 v1.1] -> stage not stated [FreeSurfer, MRtrix3, Nipype v1.5.1, fMRIPrep v20.2.1]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: These and all other co-registration were performed using the Advanced Normalization Tools (ANTs) ( 86 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

