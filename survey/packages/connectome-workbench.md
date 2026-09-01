# Connectome Workbench

- **Category:** neuroimaging
- **Papers in survey:** 19
- **Journals:** PNAS (12), Nature (5), Science (1), Cell (1)
- **Years:** 2021 (1), 2022 (3), 2023 (2), 2024 (4), 2025 (7), 2026 (2)
- **Versions named:** 1.5 (3), 1.2.3 (2), 1.0 (1)
- **Pipeline stages it appears in:** alignment/mapping (5), visualisation (5), machine learning (1), structure determination (1)

## Papers

### Stimulant medications affect arousal and reward, not attention networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.039 | PMCID: PMC12834599 | PMID: 41448140
- Evidence: The RMS values were rendered on their corresponding cortical parcels using Connectome Workbench.
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [FSL, FreeSurfer, NiBabel]

### Reproducible brain-wide association studies require thousands of individuals. (Nature 2022)

- DOI: 10.1038/s41586-022-04492-9 | PMCID: PMC8991999 | PMID: 35296861
- Evidence: These surfaces were then combined with volumetric subcortical and cerebellar data into the CIFTI format using Connectome Workbench 59 , creating full brain time courses excluding non-grey matter tissue.
- Full pipeline: normalisation [FreeSurfer] -> stage not stated [ANTs, Connectome Workbench, FSL]

### A somato-cognitive action network alternates with effector regions in motor cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05964-2 | PMCID: PMC10172144 | PMID: 37076628
- Evidence: This eigenvectors file was mapped to the Conte69 surface template atlas 80 using the ribbon-constrained method in Connectome Workbench 81 , and the eigenvector time courses of all surface vertices were cross-correlated.
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [FSL] -> machine learning [Connectome Workbench] -> stage not stated [FreeSurfer, jsPsych]

### Frontostriatal salience network expansion in individuals in depression. (Nature 2024)

- DOI: 10.1038/s41586-024-07805-2 | PMCID: PMC11410656 | PMID: 39232159
- Evidence: ...tive (CIFTI) format and spatially smoothed with geodesic (for surface data) and Euclidean (for volumetric data) Gaussian kernels ( σ = 2.55 mm) using Connectome Workbench command line utilities 107 .
- Full pipeline: alignment/mapping [FSL] -> stage not stated [Connectome Workbench, FreeSurfer]

### Parkinson's disease as a somato-cognitive action network disorder. (Nature 2026)

- DOI: 10.1038/s41586-025-10059-1 | PMCID: PMC13017517 | PMID: 41639440
- Version used: **1.5**
- Evidence: Software packages incorporated into the above code for data analysis included: Python v.3.7 ( https://www.python.org ); MATLAB R2020b ( https://www.mathworks.com/ ); Connectome Workbench v.1.5 ( http://www.humanconnectome.org/software/connectome-workbench.html ); Freesurfer v.6.0.0 ( https://surfer.nmr.mgh.harvard.edu/ ); FSL v.6.0 ( https://fsl.fmrib.ox.ac.uk/fsl/fslwiki ); ANTs v.0.3.8 ( https:/...
- Full pipeline: normalisation [ANTs, FSL] -> registration [FSL, FreeSurfer v6.0.0] -> simulation/modelling [FieldTrip] -> stage not stated [Connectome Workbench v1.5]

### Vicarious body maps bridge vision and touch in the human brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09796-0 | PMCID: PMC12872459 | PMID: 41299177
- Evidence: Using Connectome Workbench commands, the cortex-wide single-trial β -estimates were nearest-neighbour resampled from fsaverage space to the same 59,000 vertex-per-hemisphere surface format as the HCP data.
- Full pipeline: stage not stated [Connectome Workbench, Python, R, afex, emmeans]

### Altered sense of self during seizures in the posteromedial cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2100522118 | PMCID: PMC8307613 | PMID: 34272280
- Evidence: This template allowed individual vertices to be selected for real-time visualization of the resulting correlation maps using the Connectome Workbench’s wb_view software.
- Full pipeline: visualisation [Connectome Workbench] -> stage not stated [AFNI v2016.09.04.1341, FreeSurfer]

### Sex differences in the functional topography of association networks in youth. (PNAS 2022)

- DOI: 10.1073/pnas.2110416119 | PMCID: PMC9388107 | PMID: 35939696
- Evidence: Connectome Workbench (version: 1.3.2) provided by the human connectome project ( https://www.humanconnectome.org/software/connectome-workbench ) ( 97 ) was used to visualize the brain surface.
- Full pipeline: visualisation [Connectome Workbench]

### A hierarchy of linguistic predictions during natural language comprehension. (PNAS 2022)

- DOI: 10.1073/pnas.2201968119 | PMCID: PMC9371745 | PMID: 35921434
- Evidence: Subject-specific cortical surfaces were reconstructed using Freesurfer, and postprocessing (down-sampling and surface-based alignment) of the reconstructed cortical surfaces was performed using the Connectome Workbench command-line tools (v 1.1.1).
- Full pipeline: alignment/mapping [Connectome Workbench, FreeSurfer] -> structure determination [Connectome Workbench, FreeSurfer] -> machine learning [FieldTrip] -> stage not stated [FSL]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: In addition, for both adult and fetal data, we generated maps of Gaussian (intrinsic) curvature using Connectome Workbench and FD, using the dilation method described by Madan et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Prenatal social disadvantage is associated with alterations in functional networks at birth. (PNAS 2024)

- DOI: 10.1073/pnas.2405448121 | PMCID: PMC11648631 | PMID: 39621900
- Version used: **1.2.3**
- Evidence: Volumetric resting-state BOLD timeseries were mapped to subject-specific surfaces using established procedures adapted from the Human Connectome Project as implemented in Connectome Workbench 1.2.3.
- Full pipeline: alignment/mapping [Connectome Workbench v1.2.3] -> stage not stated [FSL]

### A familiar face and person processing area in the human temporal pole. (PNAS 2024)

- DOI: 10.1073/pnas.2321346121 | PMCID: PMC11252731 | PMID: 38954551
- Version used: **1.5**
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: A detailed description of the unfolding algorithm can be found in the original work ( 36 ) and online documentation. ** All the surface-based output was generated within the GIfTI framework to allow easy manipulation, volume-to-surface mapping (see following sections) and visualization using Connectome Workbench ( 102 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Parallel systems for social and spatial cognition reaching the cortical apex. (PNAS 2025)

- DOI: 10.1073/pnas.2520067122 | PMCID: PMC12595413 | PMID: 41166425
- Version used: **1.5**
- Evidence: Data were preprocessed and analyzed using a custom pipeline, integrating software elements from multiple software packages: FSL (6.0.3), Freesurfer (7.1.1), AFNI, Connectome Workbench 1.5, tedana 0.0.10, and Multimodal Surface Matching (MSM).
- Full pipeline: stage not stated [AFNI, Connectome Workbench v1.5, FSL v6.0.3, FreeSurfer v7.1.1]

### Action-mode subnetworks for decision-making, action control, and feedback. (PNAS 2025)

- DOI: 10.1073/pnas.2502021122 | PMCID: PMC12260544 | PMID: 40587801
- Version used: **1.0**
- Evidence: For optimal comparison with fMRI data, these Freesurfer-derived surfaces were transformed into 32k fs_LR space, and the Julich atlas was sampled into this 32k fs_LR space using the enclosing voxel sampling procedure available in Connectome Workbench 1.0 ( 132 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [Connectome Workbench v1.0, FSL v6.0]

### Structure-function coupling in the first month of life: Associations with age and attention. (PNAS 2025)

- DOI: 10.1073/pnas.2412729122 | PMCID: PMC12168018 | PMID: 40455980
- Version used: **1.2.3**
- Evidence: Volumetric resting-state BOLD timeseries were mapped to subject-specific surfaces using established procedures adapted from the Human Connectome Project, which were implemented in Connectome Workbench 1.2.3.
- Full pipeline: alignment/mapping [Connectome Workbench v1.2.3] -> stage not stated [FSL]

### Specialization of the human hippocampal long axis revisited. (PNAS 2025)

- DOI: 10.1073/pnas.2422083122 | PMCID: PMC11760929 | PMID: 39808662
- Evidence: This correlation structure was then explored using Connectome Workbench’s wb_view software ( 71 , 72 ) by interactively choosing cerebral seed regions and visualizing the correlations from that seed region using the Jet look-up table (colorbar), excluding negative values.
- Full pipeline: differential/statistical testing [FSL v5.0.4] -> visualisation [Connectome Workbench] -> stage not stated [FreeSurfer]

### Human brain dynamics are shaped by rare long-range connections over and above cortical geometry. (PNAS 2025)

- DOI: 10.1073/pnas.2415102122 | PMCID: PMC11725837 | PMID: 39752525
- Evidence: In summary, the data underwent preprocessing using the HCP pipeline, which employs standardized methods with FSL (FMRIB Software Library), FreeSurfer, and Connectome Workbench software.
- Full pipeline: stage not stated [Connectome Workbench, FSL, FieldTrip, FreeSurfer]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Next, each participant’s cortical contacts were assigned to the nearest registered surface mesh vertices using wb_command in Connectome Workbench ( www.humanconnectome.org/software/workbench-command ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

