# MRtrix3

- **Category:** neuroimaging
- **Papers in survey:** 12
- **Journals:** PNAS (12)
- **Years:** 2021 (1), 2022 (4), 2023 (2), 2024 (1), 2025 (2), 2026 (2)
- **Pipeline stages it appears in:** normalisation (1), registration (1), machine learning (1)

## Papers

### Development of human white matter pathways in utero over the second and third trimester. (PNAS 2021)

- DOI: 10.1073/pnas.2023598118 | PMCID: PMC8157930 | PMID: 33972435
- Evidence: We then estimated ODFs for each subject in MRtrix3 ( https://www.mrtrix.org/ ).
- Full pipeline: stage not stated [MRtrix3]

### Morphological similarity of amygdala-ventral prefrontal pathways represents trait anxiety in younger and older adults. (PNAS 2022)

- DOI: 10.1073/pnas.2205162119 | PMCID: PMC9586323 | PMID: 36215497
- Evidence: Future studies should test if the association between tract morphology and behavior can be reproduced using other tractography pipelines, such as MRtrix3 that utilizes constrained spherical deconvolution ( 64 ), which has been shown to be more reliable than the traditional DTI measures ( 65 ), although technical prerequisites of this method, such as high angular resolution diffusion imaging data, ...
- Full pipeline: registration [ANTs] -> differential/statistical testing [R v4.0] -> structure determination [FreeSurfer] -> machine learning [MRtrix3] -> stage not stated [FSL]

### Adolescent development of multiscale structural wiring and functional interactions in the human connectome. (PNAS 2022)

- DOI: 10.1073/pnas.2116673119 | PMCID: PMC9271154 | PMID: 35776541
- Evidence: The diffusion MRI data were processed using MRtrix3 ( 23 ), including correction for susceptibility distortions, head motion, and eddy currents.
- Full pipeline: stage not stated [AFNI, ANTs, FSL, FreeSurfer, MRtrix3]

### Diffusion MRI-guided theta burst stimulation enhances memory and functional connectivity along the inferior longitudinal fasciculus in mild cognitive impairment. (PNAS 2022)

- DOI: 10.1073/pnas.2113778119 | PMCID: PMC9173759 | PMID: 35594397
- Evidence: Third, tractography analysis was performed on the preprocessed diffusion data using MRtrix ( https://github.com/MRtrix3 ) to generate a total of three white matter tractography maps from each of the ROIs for each participant.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [ANTs, CONN toolbox, FSL, FreeSurfer, MRtrix3]

### A diffusion MRI-based spatiotemporal continuum of the embryonic mouse brain for probing gene-neuroanatomy connections. (PNAS 2022)

- DOI: 10.1073/pnas.2111869119 | PMCID: PMC8851557 | PMID: 35165149
- Evidence: In order to resolve more-complex microstructural organizations, such as crossing fibers, we used the constraint spherical deconvolution method ( 77 ) to estimate the fiber orientation distributions in MRtrix ( http://www.mrtrix.org ).
- Full pipeline: stage not stated [MRtrix3]

### Human white matter myelinates faster in utero than ex utero. (PNAS 2023)

- DOI: 10.1073/pnas.2303491120 | PMCID: PMC10438384 | PMID: 37549280
- Evidence: DMRI tractography was performed in accordance with recent work ( 39 ), using MRtrix ( 75 , 76 ).
- Full pipeline: quantification [Python] -> stage not stated [FSL, MRtrix3]

### White matter plasticity following cataract surgery in congenitally blind patients. (PNAS 2023)

- DOI: 10.1073/pnas.2207025120 | PMCID: PMC10175850 | PMID: 37126677
- Evidence: In both samples, the visual pathways were derived through probabilistic tractography using MRtrix3 (Brain Institute, Melbourne, Australia) ( 76 – 85 ), while a whole-brain streamlines tracking (STT) tractography was used to extract late-visual and non-visual pathways.
- Full pipeline: stage not stated [MRtrix3]

### Evolutionary continuity and divergence of auditory dorsal and ventral pathways in primates revealed by ultra-high field diffusion MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2313831121 | PMCID: PMC10907247 | PMID: 38377216
- Evidence: The dMRI data of marmosets and macaque were denoised using the dwidenoise function implemented in MRtrix3 ( 94 ) and eddy current corrected using the eddy_correct function of FSL ( 95 ).
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [FSL, MRtrix3]

### Decreased hippocampal neurite density in late-middle-aged adults following prenatal exposure to higher levels of maternal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2420188122 | PMCID: PMC12595415 | PMID: 41144670
- Evidence: Diffusion-weighted scans were denoised using dwidenoise from MRtrix3 Version 3.0.2 ( 124 – 127 ).
- Full pipeline: stage not stated [FSL, FreeSurfer, MRtrix3, R v4.2.1, tidyverse]

### Longitudinal trajectories of brain development from infancy to school age and their relationship with literacy development. (PNAS 2025)

- DOI: 10.1073/pnas.2414598122 | PMCID: PMC12184337 | PMID: 40493188
- Evidence: Preprocessing and tractography for all diffusion-weighted image (DWI) data, regardless of age, were performed with MRtrix3 based on the pipeline established for the Developing Human Connectome Project ( 41 , 122 ).
- Full pipeline: dimensionality reduction/clustering [ANTs, FSL, R] -> differential/statistical testing [R, lme4] -> simulation/modelling [lme4] -> stage not stated [Docker v1.1.0, FreeSurfer v7.3, MRtrix3]

### Metabolism-weighted brain connectome reveals synaptic integration and vulnerability to neurodegeneration. (PNAS 2026)

- DOI: 10.1073/pnas.2531706123 | PMCID: PMC13321360 | PMID: 42330267
- Evidence: DWI preprocessing and probabilistic tractography were executed using MRtrix3 ( 54 ), FSL, and Advanced Normalization Tools (ANTs), incorporating denoising, eddy-current correction, motion correction (using FSL top-up), and bias-field correction (using ANTs).
- Full pipeline: normalisation [ANTs, FSL, MRtrix3] -> registration [ANTs, FSL, MRtrix3] -> stage not stated [Enrichr, Metascape]

### Distinct contributions of hippocampal pathways in learning regularities and exceptions revealed by functional footprints. (PNAS 2026)

- DOI: 10.1073/pnas.2503388123 | PMCID: PMC12818569 | PMID: 41543896
- Evidence: We first created participant-specific whole-brain tractographies using MRtrix3 ( 57 ).
- Full pipeline: normalisation [ANTs] -> registration [FSL] -> differential/statistical testing [R, lme4 v1.1] -> stage not stated [FreeSurfer, MRtrix3, Nipype v1.5.1, fMRIPrep v20.2.1]

