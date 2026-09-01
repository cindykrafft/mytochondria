# FreeSurfer

- **Category:** neuroimaging
- **Papers in survey:** 116
- **Journals:** PNAS (96), Nature (18), Science (1), Cell (1)
- **Years:** 2021 (13), 2022 (14), 2023 (27), 2024 (26), 2025 (28), 2026 (8)
- **Versions named:** 6.0.0 (7), 7.1.1 (3), 7.1 (3), 6.0.1 (3), 5.3.0 (3), 5.3 (3), 6.0 (2), 7.3.2 (1), 7.0 (1), 6.1 (1)
- **Pipeline stages it appears in:** structure determination (23), registration (8), alignment/mapping (4), normalisation (3), dimensionality reduction/clustering (1), visualisation (1), differential/statistical testing (1)

## Papers

### Stimulant medications affect arousal and reward, not attention networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.039 | PMCID: PMC12834599 | PMID: 41448140
- Evidence: 176 Processing dependencies included FSL, 177 FreeSurfer, 178 and NiBabel.
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [FSL, FreeSurfer, NiBabel]

### Reproducible brain-wide association studies require thousands of individuals. (Nature 2022)

- DOI: 10.1038/s41586-022-04492-9 | PMCID: PMC8991999 | PMID: 35296861
- Evidence: (2) FreeSurfer 57 constructs cortical surfaces from the normalized anatomical data.
- Full pipeline: normalisation [FreeSurfer] -> stage not stated [ANTs, Connectome Workbench, FSL]

### SARS-CoV-2 is associated with changes in brain structure in UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04569-5 | PMCID: PMC9046077 | PMID: 35255491
- Evidence: Additional IDPs were created using subsegmentations of the hippocampus, amygdala and thalamus as implemented in FreeSurfer 68 – 71 .
- Full pipeline: stage not stated [FreeSurfer]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: Structural MRI processing Region of interest (ROI) labelling was implemented using the FreeSurfer 75 software package v.7 ( http://surfer.nmr.mgh.harvard.edu ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### Geometric constraints on human brain function. (Nature 2023)

- DOI: 10.1038/s41586-023-06098-1 | PMCID: PMC10266981 | PMID: 37258669
- Evidence: Specifically, we used a triangular surface mesh representation of the midthickness human cortical surface, comprising 32,492 vertices in each hemisphere, obtained from a downsampled, left–right symmetric version of the FreeSurfer’s fsaverage population-averaged template 77 ( https://github.com/ThomasYeoLab/CBIG/tree/master/data/templates/surface/fs_LR_32k ).
- Full pipeline: stage not stated [FSL, FreeSurfer, Nilearn]

### A somato-cognitive action network alternates with effector regions in motor cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05964-2 | PMCID: PMC10172144 | PMID: 37076628
- Evidence: Functional connectivity with adjacent postcentral gyrus In each adult human participant, we defined the pre- and postcentral gyri based on the individual-specific Brodmann areal parcellation produced by Freesurfer, which was deformed into fs_LR_32k space to match the functional data.
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [FSL] -> machine learning [Connectome Workbench] -> stage not stated [FreeSurfer, jsPsych]

### Study design features increase replicability in brain-wide association studies. (Nature 2024)

- DOI: 10.1038/s41586-024-08260-9 | PMCID: PMC11655360 | PMID: 39604734
- Version used: **6.1**
- Evidence: We filtered to the subset of cognitively normal participants whose data were processed using FreeSurfer (v6.1).
- Full pipeline: stage not stated [FreeSurfer v6.1, R]

### Frontostriatal salience network expansion in individuals in depression. (Nature 2024)

- DOI: 10.1038/s41586-024-07805-2 | PMCID: PMC11410656 | PMID: 39232159
- Evidence: Anatomical preprocessing and cortical surface generation Anatomical data were preprocessed and cortical surfaces generated using the Human Connectome Project (HCP) PreFreeSurfer, FreeSurfer and PostFreeSurfer pipelines (v.4.3).
- Full pipeline: alignment/mapping [FSL] -> stage not stated [Connectome Workbench, FreeSurfer]

### Psilocybin desynchronizes the human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07624-5 | PMCID: PMC11291293 | PMID: 39020167
- Evidence: Structural scans from different sessions were averaged together for the purposes of Freesurfer segmentation and nonlinear atlas registrations.
- Full pipeline: registration [FreeSurfer]

### Control of working memory by phase-amplitude coupling of human hippocampal neurons. (Nature 2024)

- DOI: 10.1038/s41586-024-07309-z | PMCID: PMC11078732 | PMID: 38632400
- Evidence: A pre-operative magnetic resonance imaging (MRI) image together with MRI or computed tomography post-operative images were used to localize the electrodes using Freesurfer as previously described 34 .
- Full pipeline: stage not stated [EEGLAB v2019.1, FieldTrip, FreeSurfer, Python]

### Single-neuronal elements of speech production in humans. (Nature 2024)

- DOI: 10.1038/s41586-023-06982-w | PMCID: PMC10866697 | PMID: 38297120
- Version used: **7.4.1**
- Evidence: ...raphy scans were coregistered by combination of ROSA software (Zimmer Biomet; v.3.1.6.276), Mango (v.4.1; https://mangoviewer.com/download.html ) and FreeSurfer (v.7.4.1; https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall ) to reconstruct the cortical surface and identify the cortical location from which Neuropixels recordings were obtained 77 – 81 .
- Full pipeline: dimensionality reduction/clustering [Kilosort v1.0, scikit-learn] -> structure determination [FreeSurfer v7.4.1] -> stage not stated [FieldTrip, statsmodels v0.13.5]

### A probabilistic histological atlas of the human brain for MRI segmentation. (Nature 2025)

- DOI: 10.1038/s41586-025-09708-2 | PMCID: PMC12711564 | PMID: 41193801
- Version used: **7.0**
- Evidence: Using FreeSurfer 7.0 as a silver standard, we computed Dice scores for our segmentations at the level of whole regions: that is, the level of granularity provided by FreeSurfer.
- Full pipeline: stage not stated [FSL, FreeSurfer v7.0, PyTorch]

### Longer scans boost prediction and cut costs in brain-wide association studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09250-1 | PMCID: PMC12367542 | PMID: 40670782
- Evidence: (7) Lastly, the data were projected onto FreeSurfer fsaverage6 surface space and smoothed using a 6 mm full-width half-maximum kernel.
- Full pipeline: stage not stated [FreeSurfer, Python v3.7]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Evidence: The FreeSurfer standard template was used (fsaverage) for participants lacking an anatomical scan ( n = 5). fMRI data acquisition MRI data were acquired using a 32-channel head coil on a 3 T Prisma scanner.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: 2d were generated using the Freesurfer software 57 .
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Population-scale repeat expansions elucidate disease risk and brain atrophy. (Nature 2026)

- DOI: 10.1038/s41586-026-10345-6 | PMCID: PMC13190288 | PMID: 41951733
- Version used: **7.3.2**
- Evidence: This final image was then segmented using FastSurfer 75 (v.2.3.0), and cortical thicknesses and other morphological traits were obtained using FreeSurfer (v.7.3.2).
- Full pipeline: variant calling [R, REGENIE v3.2] -> registration [FSL v6.0.7.8] -> differential/statistical testing [REGENIE v3.2] -> stage not stated [FreeSurfer v7.3.2, PLINK, dcm2niix]

### Rapid concerted switching of the neural code in the inferotemporal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10267-3 | PMCID: PMC13148990 | PMID: 41882367
- Evidence: Analysis of functional volumes was done using the FreeSurfer Functional Analysis Stream 57 and FSL 58 .
- Full pipeline: machine learning [PyTorch] -> stage not stated [FSL, FreeSurfer, Kilosort]

### Parkinson's disease as a somato-cognitive action network disorder. (Nature 2026)

- DOI: 10.1038/s41586-025-10059-1 | PMCID: PMC13017517 | PMID: 41639440
- Version used: **6.0.0**
- Evidence: The fMRI preprocessing sequence encompassed the following steps: (1) slice timing correction through stc_sess from the FreeSurfer v.6.0.0 software package ( http://surfer.nmr.mgh.harvard.edu ); (2) head motion correction using mc_sess from FreeSurfer ( https://surfer.nmr.mgh.harvard.edu/fswiki/mc-sess ); (3) linear detrending and bandpass filtering within the range of 0.01–0.08 Hz; and (4) regress...
- Full pipeline: normalisation [ANTs, FSL] -> registration [FSL, FreeSurfer v6.0.0] -> simulation/modelling [FieldTrip] -> stage not stated [Connectome Workbench v1.5]

### Shared and language-specific phonological processing in the human temporal lobe. (Nature 2026)

- DOI: 10.1038/s41586-025-09748-8 | PMCID: PMC12727522 | PMID: 41261133
- Evidence: FreeSurfer ( https://surfer.nmr.mgh.harvard.edu/ ) was used to create a three-dimensional model of the individual participant’s pial surfaces, run automatic parcellation to get individual anatomical labels and warp the individual participant surfaces into the cvs_avg35_inMNI152 average template.
- Full pipeline: dimensionality reduction/clustering [FreeSurfer]

### Temporal self-compression: Behavioral and neural evidence that past and future selves are compressed as they move away from the present. (PNAS 2021)

- DOI: 10.1073/pnas.2101403118 | PMCID: PMC8670431 | PMID: 34848536
- Evidence: The BOLD reference was then coregistered to the T1w reference using bbregister (FreeSurfer), which implements boundary-based registration ( 89 ).
- Full pipeline: registration [AFNI, FreeSurfer] -> stage not stated [FSL v5.0.9, Nilearn, Nipype v1.2.0, R, fMRIPrep v1.4.0, lme4]

### Handedness and its genetic influences are associated with structural asymmetries of the cerebral cortex in 31,864 individuals. (PNAS 2021)

- DOI: 10.1073/pnas.2113095118 | PMCID: PMC8617418 | PMID: 34785596
- Version used: **6.0**
- Evidence: We started from the Freesurfer 6.0 ( 76 ) “recon-all” cortical reconstructions generated by the UK Biobank imaging team (UK Biobank data field 20263, first imaging visit) but did not make use of image-derived phenotypes released by that team.
- Full pipeline: variant calling [GCTA] -> structure determination [FreeSurfer v6.0]

### Divisive normalization unifies disparate response signatures throughout the human visual hierarchy. (PNAS 2021)

- DOI: 10.1073/pnas.2108713118 | PMCID: PMC8609633 | PMID: 34772812
- Version used: **7.1**
- Evidence: Freesurfer 7.1 recon-all was used to obtain native cortical surface reconstructions for each participant.
- Full pipeline: registration [AFNI, fMRIPrep] -> structure determination [FreeSurfer v7.1] -> stage not stated [FSL v5.0.9, Nilearn v0.6.2, PsychoPy]

### Parallel hippocampal-parietal circuits for self- and goal-oriented processing. (PNAS 2021)

- DOI: 10.1073/pnas.2101743118 | PMCID: PMC8403906 | PMID: 34404728
- Version used: **5.3**
- Evidence: T1-weighted MRI data initially underwent automated segmentation using Freesurfer version 5.3 followed by manual editing of hippocampal results using ITK-SNAP software by a single highly-experienced rater (D.A.).
- Full pipeline: stage not stated [FreeSurfer v5.3]

### Shifting gradients of macroscale cortical organization mark the transition from childhood to adolescence. (PNAS 2021)

- DOI: 10.1073/pnas.2024448118 | PMCID: PMC8285909 | PMID: 34260385
- Evidence: 95 ), and FreeSurfer ( 96 ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [AFNI, FSL, FreeSurfer]

### Altered sense of self during seizures in the posteromedial cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2100522118 | PMCID: PMC8307613 | PMID: 34272280
- Evidence: The white matter and pial surfaces were calculated from the T1 anatomical template using FreeSurfer’s recon-all ( 52 ).
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [AFNI v2016.09.04.1341, FreeSurfer]

### Educational attainment does not influence brain aging. (PNAS 2021)

- DOI: 10.1073/pnas.2101644118 | PMCID: PMC8106299 | PMID: 33903255
- Version used: **7.1**
- Evidence: Materials and Methods MRIs were processed using FreeSurfer, version 7.1.
- Full pipeline: stage not stated [FreeSurfer v7.1]

### Heritability of individualized cortical network topography. (PNAS 2021)

- DOI: 10.1073/pnas.2016271118 | PMCID: PMC7936334 | PMID: 33622790
- Evidence: The heritability of individualized network size was estimated using SOLAR ( 49 ), covarying for age, sex, age 2 , age × sex, age 2 × sex, total surface area, and FreeSurfer-derived intracranial volume.
- Full pipeline: stage not stated [FreeSurfer]

### Evidence supporting a time-limited hippocampal role in retrieving autobiographical memories. (PNAS 2021)

- DOI: 10.1073/pnas.2023069118 | PMCID: PMC8000197 | PMID: 33723070
- Version used: **6.0**
- Evidence: Subject-specific hippocampal masks were generated with Freesurfer (version 6.0; RRID: SCR_001847), and each mask was manually segmented into anterior and posterior subregions using the uncal apex as a landmark of separation ( 27 ).
- Full pipeline: stage not stated [AFNI, FreeSurfer v6.0, lme4]

### Volitional learning promotes theta phase coding in the human hippocampus. (PNAS 2021)

- DOI: 10.1073/pnas.2021238118 | PMCID: PMC7958181 | PMID: 33674388
- Evidence: Electrode locations in native space were determined using FreeSurfer ( 52 ) and converted to Montreal Neurological Institute (MNI) coordinates using the pipeline described in ref.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, FreeSurfer]

### Hormone seasonality in medical records suggests circannual endocrine circuits. (PNAS 2021)

- DOI: 10.1073/pnas.2003926118 | PMCID: PMC7896322 | PMID: 33531344
- Evidence: ICV values for each subject were obtained from the FreeSurfer ( 59 ) datasheet supplied with the dataset.
- Full pipeline: stage not stated [FreeSurfer]

### Childhood self-control forecasts the pace of midlife aging and preparedness for old age. (PNAS 2021)

- DOI: 10.1073/pnas.2010211118 | PMCID: PMC7826388 | PMID: 33397808
- Version used: **5.3**
- Evidence: This method uses a stacked algorithm to predict chronological age from multiple measures of brain structure (cortical thickness, cortical surface area, and subcortical and global brain volumes) derived from Freesurfer v5.3.
- Full pipeline: stage not stated [FreeSurfer v5.3]

### Topographic connectivity reveals task-dependent retinotopic processing throughout the human brain. (PNAS 2021)

- DOI: 10.1073/pnas.2017032118 | PMCID: PMC7812773 | PMID: 33372144
- Evidence: Hippocampal subfield segmentation was performed using FreeSurfer, after which the individual subfields were warped to the functional data’s MNI space using the existing HCP warp fields with nearest-neighbor interpolation.
- Full pipeline: stage not stated [FSL, FreeSurfer, SciPy, statsmodels]

### Electrophysiological markers of memory consolidation in the human brain when memories are reactivated during sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2123430119 | PMCID: PMC9636913 | PMID: 36279460
- Evidence: CT scans were registered to MRI scans using the mutual information method through the Statistical Parametric Mapping toolbox in MATLAB ( 75 ), and cortical reconstruction and volumetric segmentation was performed with Freesurfer ( 76 ).
- Full pipeline: alignment/mapping [FreeSurfer, SPM] -> differential/statistical testing [FreeSurfer, SPM] -> structure determination [FreeSurfer, SPM]

### Metabolome-wide association study on &lt;i&gt;ABCA7&lt;/i&gt; indicates a role of ceramide metabolism in Alzheimer's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2206083119 | PMCID: PMC9618092 | PMID: 36269859
- Evidence: Regional cortical thickness and volumes were measured using the Freesurfer image analysis suite (version 5.0.3).
- Full pipeline: stage not stated [Bioconductor, FreeSurfer, PLINK]

### Morphological similarity of amygdala-ventral prefrontal pathways represents trait anxiety in younger and older adults. (PNAS 2022)

- DOI: 10.1073/pnas.2205162119 | PMCID: PMC9586323 | PMID: 36215497
- Evidence: Then, the masked image was used for cortical surface reconstruction using FreeSurfer’s recon-all ( 71 , 72 ).
- Full pipeline: registration [ANTs] -> differential/statistical testing [R v4.0] -> structure determination [FreeSurfer] -> machine learning [MRtrix3] -> stage not stated [FSL]

### Hippocampus and temporal pole functional connectivity is associated with age and individual differences in autobiographical memory. (PNAS 2022)

- DOI: 10.1073/pnas.2203039119 | PMCID: PMC9564102 | PMID: 36191210
- Version used: **6.0.1**
- Evidence: T1-weighted images were submitted to FreeSurfer version 6.0.1 ( 77 , 78 ) for cortical reconstruction and volumetric segmentation.
- Full pipeline: registration [FSL] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [AFNI]

### Human cerebellum and corticocerebellar connections involved in emotional memory enhancement. (PNAS 2022)

- DOI: 10.1073/pnas.2204900119 | PMCID: PMC9564100 | PMID: 36191198
- Version used: **4.5**
- Evidence: Each participant’s anatomical image was automatically segmented into cortical and subcortical structures using FreeSurfer version 4.5 ( 91 ).
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> visualisation [R] -> stage not stated [FreeSurfer v4.5]

### Using neuroimaging genomics to investigate the evolution of human brain structure. (PNAS 2022)

- DOI: 10.1073/pnas.2200638119 | PMCID: PMC9546597 | PMID: 36161899
- Evidence: This analysis was applied for 33 cortical regions segmented with FreeSurfer ( 22 ) and full cortical surface area.
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [LDSC] -> stage not stated [FreeSurfer, PLINK, R, ggplot2]

### A hierarchy of linguistic predictions during natural language comprehension. (PNAS 2022)

- DOI: 10.1073/pnas.2201968119 | PMCID: PMC9371745 | PMID: 35921434
- Evidence: Subject-specific cortical surfaces were reconstructed using Freesurfer, and postprocessing (down-sampling and surface-based alignment) of the reconstructed cortical surfaces was performed using the Connectome Workbench command-line tools (v 1.1.1).
- Full pipeline: alignment/mapping [Connectome Workbench, FreeSurfer] -> structure determination [Connectome Workbench, FreeSurfer] -> machine learning [FieldTrip] -> stage not stated [FSL]

### Deep neural networks constrained by neural mass models improve electrophysiological source imaging of spatiotemporal brain dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2201128119 | PMCID: PMC9351497 | PMID: 35881787
- Evidence: The cortical surface was segmented into 994 similarly sized regions in Freesurfer ( 64 ).
- Full pipeline: machine learning [PyTorch] -> stage not stated [FreeSurfer, MNE-Python v0.22.0, Python v0.22.0]

### Adolescent development of multiscale structural wiring and functional interactions in the human connectome. (PNAS 2022)

- DOI: 10.1073/pnas.2116673119 | PMCID: PMC9271154 | PMID: 35776541
- Evidence: T1-weighted data were processed using the fusion of neuroimaging preprocessing pipeline integrating AFNI, FSL, FreeSurfer, ANTs, and Workbench ( https://gitlab.com/by9433/funp ) ( 105 – 109 ), which is similar to the minimal preprocessing pipeline for the HCP ( 110 ).
- Full pipeline: stage not stated [AFNI, ANTs, FSL, FreeSurfer, MRtrix3]

### Multiscale neural signatures of major depressive, anxiety, and stress-related disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2204433119 | PMCID: PMC9191681 | PMID: 35648832
- Evidence: Structural images were processed using Freesurfer ( 67 , 68 ), while functional images were processed using FMRIB’s Multivariate Exploratory Linear Optimized Decomposition into Independent Components (MELODIC) and FSLnets tools ( 66 , 69 ).
- Full pipeline: stage not stated [FreeSurfer]

### Diffusion MRI-guided theta burst stimulation enhances memory and functional connectivity along the inferior longitudinal fasciculus in mild cognitive impairment. (PNAS 2022)

- DOI: 10.1073/pnas.2113778119 | PMCID: PMC9173759 | PMID: 35594397
- Evidence: Second, we used FreeSurfer ( https://surfer.nmr.mgh.harvard.edu ) for anatomical preprocessing and segmentation of hippocampal subfields.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs, CONN toolbox, FSL, FreeSurfer, MRtrix3]

### The effect of prolonged spaceflight on cerebrospinal fluid and perivascular spaces of astronauts and cosmonauts. (PNAS 2022)

- DOI: 10.1073/pnas.2120439119 | PMCID: PMC9169932 | PMID: 35412862
- Evidence: Preprocessing and LV segmentation were performed using FreeSurfer’s recon-all.
- Full pipeline: normalisation [ANTs] -> stage not stated [FreeSurfer]

### Examining the role of dopamine in methylphenidate's effects on resting brain function. (PNAS 2023)

- DOI: 10.1073/pnas.2314596120 | PMCID: PMC10756194 | PMID: 38109535
- Evidence: The analysis was conducted within a whole-brain mask and further explored within 360 cortical partitions, 19 subcortical partitions obtained from Freesurfer, as well as and 12 resting-state networks ( 34 ).
- Full pipeline: differential/statistical testing [fMRIPrep] -> stage not stated [FreeSurfer, lme4]

### Neural tracking measures of speech intelligibility: Manipulating intelligibility while keeping acoustics unchanged. (PNAS 2023)

- DOI: 10.1073/pnas.2309166120 | PMCID: PMC10710032 | PMID: 38032934
- Evidence: The digitized head shape and the marker coils locations were used to coregister the template FreeSurfer “fsaverage” ( 52 ) brain to each participant’s head shape using rotation, translation, and uniform scaling.
- Full pipeline: normalisation [FreeSurfer] -> differential/statistical testing [R v4.0] -> stage not stated [MNE-Python v0.23.0, lme4 v1.1]

### Hemispheric asymmetry in cortical thinning reflects intrinsic organization of the neurotransmitter systems and homotopic functional connectivity. (PNAS 2023)

- DOI: 10.1073/pnas.2306990120 | PMCID: PMC10589642 | PMID: 37831741
- Version used: **6.0.0**
- Evidence: Mean cortical thickness was extracted for each of the 68 regions (34 per hemisphere) in the Desikan–Killiany atlas ( 21 ) through the FreeSurfer (v6.0.0) implemented in the fMRIPrep pipeline.
- Full pipeline: quality control [FSL, MRIQC v0.15.0, fMRIPrep v1.3.2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R v4.2.2] -> stage not stated [FreeSurfer v6.0.0]

### Whole-brain, gray, and white matter time-locked functional signal changes with simple tasks and model-free analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2219666120 | PMCID: PMC10589709 | PMID: 37824529
- Evidence: FreeSurfer ( 33 ) was run on all T1-weighted images, and gray matter labels were extracted from the Destrieux ( 34 ) atlas parcellation, resulting in 164 gray matter labels ( Fig.
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL, FreeSurfer]

### Distributed feedforward and feedback cortical processing supports human speech production. (PNAS 2023)

- DOI: 10.1073/pnas.2300255120 | PMCID: PMC10589651 | PMID: 37819985
- Evidence: Based on the subject’s preoperative MRI, the automated FreeSurfer segmentation (Destrieux) was used for labeling within-subject anatomical locations of electrodes.
- Full pipeline: stage not stated [FreeSurfer]

### Different roles of response covariability and its attentional modulation in the sensory cortex and posterior parietal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2216942120 | PMCID: PMC10589615 | PMID: 37812698
- Evidence: Anatomical data were analyzed with FreeSurfer (CorTechs Inc, Charlestown, MA, USA) and custom MATLAB codes.
- Full pipeline: stage not stated [FreeSurfer, Psychtoolbox, SUMA]

### Functional modules for visual scene segmentation in macaque visual cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2221122120 | PMCID: PMC10410728 | PMID: 37523552
- Evidence: Offline Analysis. fMRI data were analyzed using FS-FAST and Freesurfer ( 35 ) as well as custom code written in Matlab.
- Full pipeline: stage not stated [FreeSurfer]

### Subspace partitioning in the human prefrontal cortex resolves cognitive interference. (PNAS 2023)

- DOI: 10.1073/pnas.2220523120 | PMCID: PMC10334727 | PMID: 37399398
- Version used: **5.3.0**
- Evidence: Then, we segmented the MRI using Freesurfer 5.3.0 ( 50 ) and coregistered the T1 to the CT.
- Full pipeline: stage not stated [FieldTrip, FreeSurfer v5.3.0]

### Brain-to-brain mechanisms underlying pain empathy and social modulation of pain in the patient-clinician interaction. (PNAS 2023)

- DOI: 10.1073/pnas.2212910120 | PMCID: PMC10293846 | PMID: 37339198
- Version used: **6.0.0**
- Evidence: The transformation matrix for registration between functional and high-resolution anatomical volumes was calculated using Boundary Based Registration [bbregister, Freesurfer, v6.0.0 ( 94 )].
- Full pipeline: registration [FSL v6.0.0, FreeSurfer v6.0.0] -> stage not stated [R]

### Human and chimpanzee shared and divergent neurobiological systems for general and specific cognitive brain functions. (PNAS 2023)

- DOI: 10.1073/pnas.2218565120 | PMCID: PMC10235977 | PMID: 37216540
- Evidence: For all of the datasets (i.e., all human and chimpanzee) the T1 image was processed using FreeSurfer ( 111 ), which involved tissue segmentation (see Supplementary Methods for details).
- Full pipeline: stage not stated [FSL, FreeSurfer]

### Country-level gender inequality is associated with structural differences in the brains of women and men. (PNAS 2023)

- DOI: 10.1073/pnas.2218782120 | PMCID: PMC10193926 | PMID: 37155867
- Evidence: Images were analyzed with FreeSurfer, focusing on cortical thickness and surface area from 68 regions of the Desikan–Killiany’s template and the two hemispheres, as well as the hippocampal volumes.
- Full pipeline: stage not stated [FreeSurfer]

### Spatiotemporally distributed frontotemporal networks for sentence reading. (PNAS 2023)

- DOI: 10.1073/pnas.2300252120 | PMCID: PMC10151604 | PMID: 37068244
- Evidence: Electrode positions were projected onto a cortical surface model generated in FreeSurfer ( 80 ) and displayed on the cortical surface model for visualization ( 75 ).
- Full pipeline: registration [AFNI] -> visualisation [FreeSurfer]

### Heterogeneity of depression across the socioeconomic spectrum. (PNAS 2023)

- DOI: 10.1073/pnas.2222069120 | PMCID: PMC10119997 | PMID: 37036974
- Evidence: Left and right amygdala volumes were calculated by the HCP using FreeSurfer pipeline (version 5.2).
- Full pipeline: stage not stated [FreeSurfer]

### Large-scale analysis of structural brain asymmetries in schizophrenia via the ENIGMA consortium. (PNAS 2023)

- DOI: 10.1073/pnas.2213880120 | PMCID: PMC10083554 | PMID: 36976765
- Evidence: For data from all sites, image processing and segmentation were performed using FreeSurfer (see SI Appendix , Table S2 for software versions) ( 57 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [FreeSurfer, ggplot2, metafor v3.0]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Version used: **6.0.1**
- Evidence: A T1w-reference map was computed (after INU-correction) using mri_robust_template (FreeSurfer 6.0.1, 120 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Human brain effects of DMT assessed via EEG-fMRI. (PNAS 2023)

- DOI: 10.1073/pnas.2218949120 | PMCID: PMC10068756 | PMID: 36940333
- Evidence: Specifically, the anatomical nuisance regressors were: a) ventricles [Freesurfer ( 76 ), eroded in 2 mm space], b) draining veins (DVs) [FSL’s CSF minus Freesurfer’s Ventricles, eroded in 1 mm space ( 74 , 76 )], and c) local white matter (WM) [FSL’s WM minus Freesurfer’s subcortical gray matter structures, eroded in 2 mm space ( 74 , 76 )].
- Full pipeline: normalisation [ANTs, FSL] -> registration [AFNI, ANTs, FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Propofol disrupts alpha dynamics in functionally distinct thalamocortical networks during loss of consciousness. (PNAS 2023)

- DOI: 10.1073/pnas.2207831120 | PMCID: PMC10089159 | PMID: 36897972
- Evidence: RAS coordinates were assigned for all intracranial channels by visual inspection of a maximal intensity projection of the CT, and then projected to the subjects’ individual MRI spaces using coregistration matrices produced using FreeSurfer.
- Full pipeline: registration [FreeSurfer] -> differential/statistical testing [FSL]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Version used: **5.3**
- Evidence: The standard “recon-all -all” processing pipeline of Freesurfer v5.3 was applied to perform automated surface-based morphometry segmentation ( 62 ).
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### Transcranial magnetic stimulation to frontal but not occipital cortex disrupts endogenous attention. (PNAS 2023)

- DOI: 10.1073/pnas.2219635120 | PMCID: PMC10013745 | PMID: 36853947
- Evidence: Each T1w scan was auto aligned to a template to ensure a similar slice prescription for all observers, and cortical surfaces were reconstructed using Freesurfer’s recon-all ( 82 ).
- Full pipeline: alignment/mapping [FreeSurfer] -> structure determination [FreeSurfer]

### Robust machine learning segmentation for large-scale analysis of heterogeneous clinical brain MRI datasets. (PNAS 2023)

- DOI: 10.1073/pnas.2216399120 | PMCID: PMC9992854 | PMID: 36802420
- Evidence: These segmentations contain labels for 31 brain structures, obtained manually (OASIS) or with FreeSurfer (HCP and ADNI) ( 45 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, Keras, TensorFlow]

### Elevated dementia risk, cognitive decline, and hippocampal atrophy in multisite chronic pain. (PNAS 2023)

- DOI: 10.1073/pnas.2215192120 | PMCID: PMC9992778 | PMID: 36802440
- Evidence: The 42 bilateral subfield hippocampal IDPs (field IDs, 26620 - 26663) were defined by the Freesurfer subsegmentation atlas ( 81 ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [FreeSurfer, R v4.1, lavaan]

### Restricted language access during childhood affects adult brain structure in selective language regions. (PNAS 2023)

- DOI: 10.1073/pnas.2215423120 | PMCID: PMC9963327 | PMID: 36745780
- Evidence: We used the recon-all function in FreeSurfer ( 38 ) to process the structural MRI images and to perform cortical reconstruction.
- Full pipeline: differential/statistical testing [R, lme4] -> structure determination [FreeSurfer]

### Brain aerobic glycolysis and resilience in Alzheimer disease. (PNAS 2023)

- DOI: 10.1073/pnas.2212256120 | PMCID: PMC9963219 | PMID: 36745794
- Evidence: Each individual’s GI, CMRGlc, CBF, and CMRO 2 images were partial volume corrected to regions defined by the Desikan–Killiany atlas and FreeSurfer subcortical parcellations.
- Full pipeline: registration [FSL] -> stage not stated [FreeSurfer]

### Anatomically interpretable deep learning of brain age captures domain-specific cognitive impairment. (PNAS 2023)

- DOI: 10.1073/pnas.2214634120 | PMCID: PMC9926270 | PMID: 36595679
- Evidence: For UKBB data, we used preprocessed images generated by a UKBB pipeline whose output included FreeSurfer reconstructions ( 61 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [Python v3.6, TensorFlow v2.7.0]

### Breathing orchestrates synchronization of sleep oscillations in the human hippocampus. (PNAS 2024)

- DOI: 10.1073/pnas.2405395121 | PMCID: PMC11670218 | PMID: 39680758
- Evidence: We also segmented subcortical areas of each individual’s anatomical image using the Freesurfer ( http://surfer.nmr.mgh.harvard.edu ; RRID:SCR_001847) subcortical segmentation tool.
- Full pipeline: registration [FSL] -> stage not stated [FieldTrip, FreeSurfer]

### Intracortical recordings reveal the neuronal selectivity for bodies and body parts in the human visual cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2408871121 | PMCID: PMC11665852 | PMID: 39652751
- Evidence: To generate cortical 3D renderings and for the high-resolution MNI atlas, we employed Freesurfer.
- Full pipeline: stage not stated [FreeSurfer, Python, SPM, scikit-learn]

### Sculpting new visual categories into the human brain. (PNAS 2024)

- DOI: 10.1073/pnas.2410445121 | PMCID: PMC11648923 | PMID: 39625982
- Evidence: Images were preprocessed using custom AFNI ( 61 ), Freesurfer ( 25 ), and bash scripts.
- Full pipeline: stage not stated [AFNI, FreeSurfer]

### Secondary thalamic dysfunction underlies abnormal large-scale neural dynamics in chronic stroke. (PNAS 2024)

- DOI: 10.1073/pnas.2409345121 | PMCID: PMC11573628 | PMID: 39503890
- Evidence: The spatial extents of the left and right thalami were first approximated by applying Freesurfer ( 85 ) (recon-all) to the T1 image.
- Full pipeline: registration [FSL] -> differential/statistical testing [lme4 v1.1] -> stage not stated [FreeSurfer]

### Adolescent alcohol consumption predicted by differences in electrophysiological functional connectivity and neuroanatomy. (PNAS 2024)

- DOI: 10.1073/pnas.2320805121 | PMCID: PMC11494299 | PMID: 39378092
- Evidence: MRI images from each participant were processed with FreeSurfer image analysis suite (version 5.3.0), which is documented and freely available for download online ( http://surfer.nmr.mgh.harvard.edu/ ).
- Full pipeline: stage not stated [FieldTrip, FreeSurfer]

### Repetition dynamically and rapidly increases cortical, but not hippocampal, offline reactivation. (PNAS 2024)

- DOI: 10.1073/pnas.2405929121 | PMCID: PMC11459139 | PMID: 39316058
- Evidence: ROIs included the hippocampus (HPC) and ventral temporal cortex (VTC) extracted from Freesurfer’s volumetric segmentation ( 41 ), as well as retrosplenial cortex (RSC) and medial prefrontal cortex (mPFC) converted from the Schaefer atlas ( 42 ).
- Full pipeline: stage not stated [FreeSurfer]

### COVID-19 lockdown effects on adolescent brain structure suggest accelerated maturation that is more pronounced in females than in males. (PNAS 2024)

- DOI: 10.1073/pnas.2403200121 | PMCID: PMC11420155 | PMID: 39250666
- Evidence: Cortical reconstruction, volumetric segmentation, and cortical parcellation were performed with the FreeSurfer image analysis suite (version 7, http://surfer.nmr.mgh.harvard.edu ) using the recon-all processing stream.
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [SciPy, scikit-learn]

### Depressive symptoms during the transition to adolescence: Left hippocampal volume as a marker of social context sensitivity. (PNAS 2024)

- DOI: 10.1073/pnas.2321965121 | PMCID: PMC11406239 | PMID: 39226358
- Evidence: All the structural MRI data were processed using FreeSurfer in line with the standard processing pipelines.
- Full pipeline: stage not stated [FreeSurfer]

### Human adolescent brain similarity development is different for paralimbic versus neocortical zones. (PNAS 2024)

- DOI: 10.1073/pnas.2314074121 | PMCID: PMC11331068 | PMID: 39121162
- Version used: **5.3.0**
- Evidence: We preprocessed the anatomical data using the recon-all command in Freesurfer v5.3.0 ( 43 ).
- Full pipeline: differential/statistical testing [AFNI] -> stage not stated [FreeSurfer v5.3.0]

### Sex and mental health are related to subcortical brain microstructure. (PNAS 2024)

- DOI: 10.1073/pnas.2403212121 | PMCID: PMC11295051 | PMID: 39042688
- Evidence: Subcortical regions were defined using FMRIB Image Registration and Segmentation Tool (FIRST) ( 59 ), while supratentorial volumes were derived using FreeSurfer ( 60 ).
- Full pipeline: registration [FreeSurfer] -> differential/statistical testing [R v4.3, lme4]

### Beta and theta oscillations track effort and previous reward in the human basal ganglia and prefrontal cortex during decision making. (PNAS 2024)

- DOI: 10.1073/pnas.2322869121 | PMCID: PMC11295073 | PMID: 39047043
- Evidence: To localize each ECoG contact in individual patients, we first used the preoperative T1 MRI to reconstruct the cortical surface using FreeSurfer ( 106 , 107 ).
- Full pipeline: alignment/mapping [FieldTrip] -> structure determination [FreeSurfer]

### A familiar face and person processing area in the human temporal pole. (PNAS 2024)

- DOI: 10.1073/pnas.2321346121 | PMCID: PMC11252731 | PMID: 38954551
- Version used: **7.1.1**
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Hemispheric functional organization, as revealed by naturalistic neuroimaging, in pediatric epilepsy patients with cortical resections. (PNAS 2024)

- DOI: 10.1073/pnas.2317458121 | PMCID: PMC11252739 | PMID: 38950362
- Evidence: For hemispherectomy patients, there was one additional preprocessing step: Before parcellation, we used the AFNI function lesion_align ( 33 ) to mirror the preserved hemisphere onto the lesioned hemisphere side to facilitate Freesurfer reconstruction ( 55 ), which is highly error-prone with a single hemisphere.
- Full pipeline: differential/statistical testing [R, lme4] -> structure determination [FreeSurfer] -> stage not stated [AFNI v21.1.10, emmeans]

### Impact of repeated blast exposure on active-duty United States Special Operations Forces. (PNAS 2024)

- DOI: 10.1073/pnas.2313568121 | PMCID: PMC11087753 | PMID: 38648470
- Version used: **7.3.0**
- Evidence: BOLD data were processed in the FreeSurfer 7.3.0 Functional Analysis Stream (FSFAST) ( 35 ) for B 0 distortion correction, motion correction, slice-timing correction, and temporal detrending.
- Full pipeline: registration [FreeSurfer v7.3.0]

### Childhood maltreatment influences adult brain structure through its effects on immune, metabolic, and psychosocial factors. (PNAS 2024)

- DOI: 10.1073/pnas.2304704121 | PMCID: PMC11032474 | PMID: 38593073
- Evidence: Downloaded 3D-MPRAGE T1-weighted images were preprocessed according to the Human Connectome Project (HCP) minimal Freesurfer pipeline ( 36 ).
- Full pipeline: stage not stated [FreeSurfer, R v4.2.2, lavaan]

### Causal functional maps of brain rhythms in working memory. (PNAS 2024)

- DOI: 10.1073/pnas.2318528121 | PMCID: PMC10998564 | PMID: 38536752
- Evidence: Finally, we transformed each head model into the normalized FreeSurfer Average (fsavg) space to allow for intersubject analysis.
- Full pipeline: normalisation [FreeSurfer] -> structure determination [SPM] -> stage not stated [R v4.3]

### Changes in spatial self-consciousness elicit grid cell-like representation in the entorhinal cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2315758121 | PMCID: PMC10962966 | PMID: 38489383
- Version used: **6.0.0**
- Evidence: EC ROI of each participant was defined using Freesurfer (v6.0.0) following previous studies ( 7 , 19 ).
- Full pipeline: differential/statistical testing [lme4 v1.1.26] -> stage not stated [FreeSurfer v6.0.0, R, SPM]

### The dorsomedial prefrontal cortex prioritizes social learning during rest. (PNAS 2024)

- DOI: 10.1073/pnas.2309232121 | PMCID: PMC10962978 | PMID: 38466844
- Evidence: Nongridded (surface) resamplings were performed using mri_vol2surf (FreeSurfer).
- Full pipeline: stage not stated [ANTs v2.3.3, FSL v5.0.9, FreeSurfer, Nipype v1.6.1, fMRIPrep v20.2.2]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Version used: **7.1.1**
- Evidence: The B 1 + -corrected MP2RAGE UNI images were then background denoised and pre-processed using presurfer § ( 91 ) and were processed using the recon-all pipeline for cortical segmentation and surface reconstruction in Freesurfer 7.1.1( 92 ). ¶ The cleaned hires-UNI, B 1 + corrected hires-UNI images and hires-T 1 maps were resampled to 0.3 mm isotropic resolution, averaged and used for further analy...
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Diverging neural dynamics for syntactic structure building in naturalistic speaking and listening. (PNAS 2024)

- DOI: 10.1073/pnas.2310766121 | PMCID: PMC10945772 | PMID: 38442171
- Evidence: BA44 and BA45 were extracted following Freesurfer’s label creation with the Destrieux Atlas ( 89 ) and resampled to functional space with bbregister.
- Full pipeline: differential/statistical testing [R v4.0.3, lme4] -> stage not stated [FreeSurfer, Nilearn, Python, TensorFlow, emmeans]

### Evolutionary continuity and divergence of auditory dorsal and ventral pathways in primates revealed by ultra-high field diffusion MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2313831121 | PMCID: PMC10907247 | PMID: 38377216
- Evidence: The 3D cortical surface of the brain was reconstructed using Freesurfer ( https://surfer.nmr.mgh.harvard.edu/ ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [FSL, MRtrix3]

### Cortical tracking of sign language: The role of language knowledge in tracking of different articulators. (PNAS 2025)

- DOI: 10.1073/pnas.2512665122 | PMCID: PMC12745750 | PMID: 41397120
- Evidence: We used the segmentation algorithms implemented in Freesurfer (Martinos Center of Biomedical Imaging, MQ) to segment MRI scans from each participant into scalp, skull, and brain components.
- Full pipeline: normalisation [SPM] -> stage not stated [FieldTrip, FreeSurfer]

### Parallel systems for social and spatial cognition reaching the cortical apex. (PNAS 2025)

- DOI: 10.1073/pnas.2520067122 | PMCID: PMC12595413 | PMID: 41166425
- Version used: **7.1.1**
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Automaticity speeds the retrieval of instances from the human hippocampus. (PNAS 2025)

- DOI: 10.1073/pnas.2518523122 | PMCID: PMC12595489 | PMID: 41166430
- Version used: **6.0.0**
- Evidence: To localize their precise positions in the brain, we first registered postoperative computed tomography (CT) images to preoperative T1-weighted MR images using FreeSurfer v6.0.0 ( 49 ), following the iElvis pipeline ( 50 ).
- Full pipeline: stage not stated [EEGLAB, FreeSurfer v6.0.0, Psychtoolbox]

### Decreased hippocampal neurite density in late-middle-aged adults following prenatal exposure to higher levels of maternal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2420188122 | PMCID: PMC12595415 | PMID: 41144670
- Evidence: Region-of-interest (ROI) masks were generated for the following subfields of the hippocampus using T1-weighted and high-resolution, T2-weighted structural scans with FreeSurfer Version 7.2.0: CA1, CA3, and CA4; the dentate gyrus; and the subiculum ( 122 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, MRtrix3, R v4.2.1, tidyverse]

### Familial transmission of neural representations for mental arithmetic across two generations. (PNAS 2025)

- DOI: 10.1073/pnas.2421528122 | PMCID: PMC12377651 | PMID: 40789033
- Evidence: Third, functional images were coregistered to the anatomical image using the bbregister algorithm in FreeSurfer.
- Full pipeline: quality control [MRIQC v0.15.1] -> normalisation [ANTs] -> registration [FSL] -> stage not stated [AFNI, FreeSurfer, Nilearn, PsychoPy, Python, fMRIPrep v20.2.5]

### Action-mode subnetworks for decision-making, action control, and feedback. (PNAS 2025)

- DOI: 10.1073/pnas.2502021122 | PMCID: PMC12260544 | PMID: 40587801
- Evidence: To map this atlas to the cortical surface, we downloaded an existing Freesurfer reconstruction of this brain from ( https://figshare.com/articles/dataset/FreeSurfer_reconstruction_of_the_MNI152_ICBM2009c_asymmetrical_non-linear_atlas/4223811 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [Connectome Workbench v1.0, FSL v6.0]

### The brain computes dynamic facial movements for emotion categorization using a third pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2423560122 | PMCID: PMC12207432 | PMID: 40526714
- Evidence: We reconstructed the time series of MEG sources on a 5 mm grid of boundary element model (BEM) surface (computed with Freesurfer and MNE software per participant, regularization parameter λ = 1/9).
- Full pipeline: structure determination [FreeSurfer]

### Linking pregnancy- and birth-related risk factors to a multivariate fusion of child cortical structure. (PNAS 2025)

- DOI: 10.1073/pnas.2422281122 | PMCID: PMC12207422 | PMID: 40526716
- Version used: **7.1**
- Evidence: We processed the T1-weighted images using FreeSurfer 7.1 ( https://surfer.nmr.mgh.harvard.edu/ ) ( 84 , 85 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [FreeSurfer v7.1]

### Longitudinal trajectories of brain development from infancy to school age and their relationship with literacy development. (PNAS 2025)

- DOI: 10.1073/pnas.2414598122 | PMCID: PMC12184337 | PMID: 40493188
- Version used: **7.3**
- Evidence: The standard, unmodified FreeSurfer v7.3 ( https://surfer.nmr.mgh.harvard.edu/ ) “recon” protocol was used for brains > 50 mo.
- Full pipeline: dimensionality reduction/clustering [ANTs, FSL, R] -> differential/statistical testing [R, lme4] -> simulation/modelling [lme4] -> stage not stated [Docker v1.1.0, FreeSurfer v7.3, MRtrix3]

### Longitudinal associations between birth-to-six cortical growth and childhood neurocognitive function. (PNAS 2025)

- DOI: 10.1073/pnas.2418176122 | PMCID: PMC12146774 | PMID: 40424148
- Evidence: Each participant’s brain at each timepoint was aligned to the early developmental atlas using Freesurfer ( 31 ) and then mapped to the Desikan–Killiany atlas to ensure correct registration at each ROI ( 50 , 51 ).
- Full pipeline: alignment/mapping [FreeSurfer] -> registration [FreeSurfer] -> differential/statistical testing [FSL, lme4] -> stage not stated [fMRIPrep v20.0.7]

### Early development of navigationally relevant location information in the retrosplenial complex. (PNAS 2025)

- DOI: 10.1073/pnas.2503569122 | PMCID: PMC12088441 | PMID: 40324094
- Evidence: For the hippocampus, we used FreeSurfer segmentation ( 54 ).
- Full pipeline: stage not stated [AFNI, FreeSurfer]

### A hierarchy of processing complexity and timescales for natural sounds in the human auditory cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2412243122 | PMCID: PMC12067213 | PMID: 40294254
- Evidence: For each patient, a cortical surface was reconstructed from a preoperative T1-weighted MRI using Freesurfer ( 69 ).
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Version used: **6.0.1**
- Evidence: Brain surfaces were reconstructed using recon-all ( 52 ) (FreeSurfer 6.0.1), and the brain mask estimated previously was refined with a custom variation of the method to reconcile ANTs-derived and FreeSurfer derived segmentations of the cortical gray-matter of Mindboggle ( 53 ).
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### Expectation-dependent stimulus selectivity in the ventral visual cortical pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2406684122 | PMCID: PMC12002251 | PMID: 40146852
- Evidence: To analyze the data, we used FreeSurfer and FS-FAST ( http://surfer.nmr.mgh.harvard.edu/ ) with custom Linux shell as well as custom MATLAB scripts for fMRI analysis.
- Full pipeline: alignment/mapping [AFNI] -> registration [AFNI] -> stage not stated [FreeSurfer]

### Neural basis for individual differences in the attention-enhancing effects of methylphenidate. (PNAS 2025)

- DOI: 10.1073/pnas.2423785122 | PMCID: PMC12002349 | PMID: 40127280
- Version used: **5.3.0**
- Evidence: FreeSurfer version 5.3.0 ( http://surfer.nmr.mgh.harvard.edu ) was used to automatically segment the anatomical MRI scans using the Desikan atlas ( 76 ), which provided bilateral nucleus accumbens, caudate, putamen, (which combined comprise the striatum) and cerebellum regions of interest.
- Full pipeline: differential/statistical testing [FSL, SPM] -> stage not stated [FreeSurfer v5.3.0, R]

### Brain-wide dynamic coactivation states code for hand movements in the resting state. (PNAS 2025)

- DOI: 10.1073/pnas.2415508122 | PMCID: PMC11929402 | PMID: 40073058
- Evidence: Structural and functional preprocessing was performed using the FreeSurfer and FS-FAST processing stream (surfer.nmr.mgh.harvard.edu), fully described in refs.
- Full pipeline: stage not stated [FreeSurfer]

### Deep learning to quantify the pace of brain aging in relation to neurocognitive changes. (PNAS 2025)

- DOI: 10.1073/pnas.2413442122 | PMCID: PMC11912385 | PMID: 39993207
- Evidence: For UKBB participants, we utilized T 1 -weighted MRIs preprocessed using the UKBB pipeline, which includes FreeSurfer (FS) reconstructions ( 36 ).
- Full pipeline: structure determination [FreeSurfer] -> machine learning [Python v3.8, TensorFlow v2.12.0]

### Temporal autocorrelation is predictive of age-An extensive MEG time-series analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411098122 | PMCID: PMC11873822 | PMID: 39977317
- Version used: **6.0.0**
- Evidence: T1- and T2-weighted images were reconstructed using FreeSurfer 6.0.0 ( https://surfer.nmr.mgh.harvard.edu/ ) and MEG sensor data further projected to individual cortical surfaces derived from SUMA ( 65 ).
- Full pipeline: normalisation [SPM] -> structure determination [FreeSurfer v6.0.0, SUMA] -> stage not stated [FieldTrip v3.5]

### Specialization of the human hippocampal long axis revisited. (PNAS 2025)

- DOI: 10.1073/pnas.2422083122 | PMCID: PMC11760929 | PMID: 39808662
- Evidence: For each fixation run, the mean BOLD signal was extracted within the Default Network A (DN-A) and Salience / Parietal Memory (SAL / PMN) networks on the cerebral surface and correlated with the BOLD signal within each voxel of each individual’s hippocampal boundaries as identified by the automated FreeSurfer parcellation ( 68 , 69 ).
- Full pipeline: differential/statistical testing [FSL v5.0.4] -> visualisation [Connectome Workbench] -> stage not stated [FreeSurfer]

### Expansion of a conserved architecture drives the evolution of the primate visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421585122 | PMCID: PMC11761675 | PMID: 39805017
- Evidence: Anatomical images underwent cortical surface reconstruction using Freesurfer.
- Full pipeline: normalisation [AFNI, ANTs, FSL, SUMA] -> structure determination [FreeSurfer]

### Human brain dynamics are shaped by rare long-range connections over and above cortical geometry. (PNAS 2025)

- DOI: 10.1073/pnas.2415102122 | PMCID: PMC11725837 | PMID: 39752525
- Evidence: In summary, the data underwent preprocessing using the HCP pipeline, which employs standardized methods with FSL (FMRIB Software Library), FreeSurfer, and Connectome Workbench software.
- Full pipeline: stage not stated [Connectome Workbench, FSL, FieldTrip, FreeSurfer]

### A detailed spatiotemporal atlas of the white matter tracts for the fetal brain. (PNAS 2025)

- DOI: 10.1073/pnas.2410341121 | PMCID: PMC11725871 | PMID: 39793058
- Evidence: ( 84 ) and made minor changes to reflect the differences between base parcellation protocols because Wassermann et al. used the FreeSurfer cortical parcellations for adults.
- Full pipeline: stage not stated [FreeSurfer]

### Individual differences in speech monitoring: Functional and structural correlates of delayed auditory feedback. (PNAS 2026)

- DOI: 10.1073/pnas.2530123123 | PMCID: PMC13321129 | PMID: 42330290
- Evidence: The template surface was first reconstructed in FreeSurfer ( https://surfer.nmr.mgh.harvard.edu ), producing pial and white matter boundary surfaces for each hemisphere.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> structure determination [FreeSurfer] -> stage not stated [Psychtoolbox, SPM, fMRIPrep v23.1.0]

### Empirical validation of race-neutral normative brain morphometry models across ethnoracially diverse populations. (PNAS 2026)

- DOI: 10.1073/pnas.2521055123 | PMCID: PMC13187733 | PMID: 42118844
- Evidence: Parcellated neuroimaging data—derived using the standard processing pipelines of the FreeSurfer image analysis suite ( https://surfer.nmr.mgh.harvard.edu/ ) applied to whole-brain T1-weighted structural MRI scans—were either generated by the research team or downloaded from publicly available repositories or obtained directly from the data owners.
- Full pipeline: stage not stated [FreeSurfer]

### Quantitative assessment of flow between cerebrospinal and interstitial fluid compartments in humans. (PNAS 2026)

- DOI: 10.1073/pnas.2526239123 | PMCID: PMC13142984 | PMID: 42054362
- Version used: **7.4**
- Evidence: From a standard T1 weighted image acquired at baseline before contrast injections, FreeSurfer [“recon-all-clinical”—a deep-learning based segmentation tool released with FreeSurfer 7.4 ( 53 , 54 )] was used to provide whole segmentations of the intracranial space.
- Full pipeline: stage not stated [FreeSurfer v7.4]

### Distinct contributions of hippocampal pathways in learning regularities and exceptions revealed by functional footprints. (PNAS 2026)

- DOI: 10.1073/pnas.2503388123 | PMCID: PMC12818569 | PMID: 41543896
- Evidence: Nongridded (surface) resamplings were performed using mri_vol2surf (FreeSurfer).
- Full pipeline: normalisation [ANTs] -> registration [FSL] -> differential/statistical testing [R, lme4 v1.1] -> stage not stated [FreeSurfer, MRtrix3, Nipype v1.5.1, fMRIPrep v20.2.1]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Version used: **6.0.0**
- Evidence: From the MRI scan, we extracted both the subcortical segmentation and cortical surface (FreeSurfer v6.0.0 recon-all command ( 66 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

