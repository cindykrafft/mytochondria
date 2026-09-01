# QSIPrep

- **Category:** neuroimaging
- **Papers in survey:** 2
- **Journals:** PNAS (2)
- **Years:** 2025 (2)
- **Pipeline stages it appears in:** registration (1)

## Papers

### Full interhemispheric integration sustained by a fraction of posterior callosal fibers. (PNAS 2025)

- DOI: 10.1073/pnas.2520190122 | PMCID: PMC12582319 | PMID: 41118210
- Evidence: Image coregistration parameters were subsequently estimated between an N3 bias-corrected mean BOLD reference and the skull-stripped T 1 image via antsRegistration (including both linear and nonlinear transformations to minimize residual signal deformations, cf. “SyN distortion correction” as implemented by the widely used fMRIPrep and QSIPrep pipelines).
- Full pipeline: alignment/mapping [ANTs, SPM] -> normalisation [ANTs, SPM] -> registration [QSIPrep, fMRIPrep] -> differential/statistical testing [ANTs, SPM] -> stage not stated [FSL]

### Connectional axis of individual functional variability: Patterns, structural correlates, and relevance for development and cognition. (PNAS 2025)

- DOI: 10.1073/pnas.2420228122 | PMCID: PMC11962465 | PMID: 40100626
- Evidence: Diffusion MRI data were preprocessed using Mrtrix3 ( 70 ) and QSIPrep ( 71 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [QSIPrep]

