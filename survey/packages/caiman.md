# CaImAn

- **Category:** neuro-tools
- **Papers in survey:** 14
- **Journals:** Nature (9), PNAS (5)
- **Years:** 2022 (4), 2023 (3), 2024 (4), 2025 (3)
- **Pipeline stages it appears in:** machine learning (4), registration (2)

## Papers

### Cortical feedback loops bind distributed representations of working memory. (Nature 2022)

- DOI: 10.1038/s41586-022-05014-3 | PMCID: PMC9365695 | PMID: 35896749
- Evidence: The imaging data were pre-processed using modified CaImAn software 74 .
- Full pipeline: stage not stated [CaImAn, Suite2p]

### Flexible circuit mechanisms for context-dependent song sequencing. (Nature 2023)

- DOI: 10.1038/s41586-023-06632-1 | PMCID: PMC10600009 | PMID: 37821705
- Evidence: Dsx + TN1 somas were segmented by using the constrained non-negative matrix factorization algorithm to obtain temporal traces and spatial footprints of each soma as implemented in CaImAn 58 , 62 (the initial number and xyz location of all TN1 somas were manually pre-defined).
- Full pipeline: differential/statistical testing [Brian2] -> simulation/modelling [Brian2] -> machine learning [CaImAn, PyTorch] -> stage not stated [Python v2.7, SLEAP]

### A rise-to-threshold process for a relative-value decision. (Nature 2023)

- DOI: 10.1038/s41586-023-06271-6 | PMCID: PMC10356611 | PMID: 37407812
- Evidence: Two-photon imaging frames were motion corrected using either custom scripts from a previous study 66 or CaImAn 69 .
- Full pipeline: registration [CaImAn] -> stage not stated [DeepLabCut, Fiji, ImageJ]

### Fast and sensitive GCaMP calcium indicators for imaging neural populations. (Nature 2023)

- DOI: 10.1038/s41586-023-05828-9 | PMCID: PMC10060165 | PMID: 36922596
- Evidence: Movies were motion-corrected and converted to Δ F/F 0 traces using the Python implementation of CaImAn 69 .
- Full pipeline: structure determination [REFMAC] -> stage not stated [CaImAn, PyMOL, Python, Suite2p, ilastik]

### Kinetic features dictate sensorimotor alignment in the superior colliculus. (Nature 2024)

- DOI: 10.1038/s41586-024-07619-2 | PMCID: PMC11236723 | PMID: 38961292
- Evidence: Two-photon recordings were then registered and ROIs were determined manually and extracted using CaImAn 58 (Flatiron Institute) in Python.
- Full pipeline: stage not stated [CaImAn, DeepLabCut, PsychoPy, Python]

### Converting an allocentric goal into an egocentric steering signal. (Nature 2024)

- DOI: 10.1038/s41586-023-07006-3 | PMCID: PMC10881393 | PMID: 38326612
- Evidence: Processing of imaging data To correct for motion artefacts, we registered two-photon imaging frames using the CaImAn 64 Python package.
- Full pipeline: stage not stated [CaImAn, Python, SciPy]

### Alternative splicing of latrophilin-3 controls synapse formation. (Nature 2024)

- DOI: 10.1038/s41586-023-06913-9 | PMCID: PMC10830413 | PMID: 38233523
- Evidence: Time-lapsed videos of calcium imaging files were processed using the CaImAn package 46 to search for spiking somas and generate corresponding fluorescence intensity (Δ F / F ) over time.
- Full pipeline: alignment/mapping [STAR] -> quantification [scikit-image v0.20.0] -> stage not stated [CaImAn, DESeq2, HOMER, HTSeq, SciPy v1.10.1]

### Functional connectomics spanning multiple areas of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08790-w | PMCID: PMC11981939 | PMID: 40205214
- Evidence: Neurons were automatically segmented using constrained non-negative matrix factorization, then deconvolved to extract estimates of spiking activity, within the CaImAn pipeline 71 .
- Full pipeline: machine learning [CaImAn] -> visualisation [Matplotlib, NumPy] -> stage not stated [Python, SciPy]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: Similar to other open source software packages that have supported the widespread adoption of other complex data modalities such as calcium imaging (CaImAn 7 and Suite2P 8 ), Neuropixels recordings (KiloSort 9 and MountainSort 10 ), label-free behavioural tracking (DeepLabCut 11 , MoSeq 12 and SLEAP 13 ) and spatial transcriptomics (Giotto 14 and Squidpy 15 ), the goal of NEURD is to make ‘big neu...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### Neuronal signature of spatial decision-making during navigation by freely moving rats by using calcium imaging. (PNAS 2022)

- DOI: 10.1073/pnas.2212152119 | PMCID: PMC9636941 | PMID: 36279456
- Evidence: 1 D , Left ), recordings were processed to identify individual regions of interest (ROIs; Materials and Methods ) with the CaImAn constrained nonnegative matrix factorization-extended (CNMF-E) algorithm ( Fig.
- Full pipeline: machine learning [CaImAn] -> stage not stated [Fiji v2.1, ImageJ v2.1, Python]

### Ca2+ imaging of self and other in medial prefrontal cortex during social dominance interactions in a tube test. (PNAS 2022)

- DOI: 10.1073/pnas.2107942119 | PMCID: PMC9353509 | PMID: 35881809
- Evidence: Finally, event detection was computed using the OASIS package ( 29 ) (as found in CaImAn).
- Full pipeline: stage not stated [CaImAn, ImageJ]

### Real-time visualization of mRNA synthesis during memory formation in live mice. (PNAS 2022)

- DOI: 10.1073/pnas.2117076119 | PMCID: PMC9271212 | PMID: 35776545
- Evidence: ...f view in Arc mRNA and calcium images; 5) obtaining nuclear centroid coordinates using Imaris software (Bitplane); 6) calcium source extraction using CaImAn software ( 58 ), which is based on a constrained nonnegative matrix factorization algorithm by seeding the nuclear centroid locations as initial spatial components; and 7) matching the nuclei in Arc mRNA images and the spatial components detec...
- Full pipeline: machine learning [CaImAn] -> stage not stated [ImageJ]

### Cellular-resolution optogenetics reveals attenuation-by-suppression in visual cortical neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2318837121 | PMCID: PMC11551350 | PMID: 39485801
- Evidence: We used the CaImAn toolbox ( 80 ) for motion correction and Suite2p ( 81 ) for cell segmentation to allow manual selection of cell masks.
- Full pipeline: registration [CaImAn, Suite2p]

### Reactivation of memory-associated neurons induces downstream suppression of competing neuronal populations. (PNAS 2025)

- DOI: 10.1073/pnas.2410101122 | PMCID: PMC12002025 | PMID: 40168126
- Evidence: Trace extraction took place using a prepublished package, CaImAn ( 57 ).
- Full pipeline: stage not stated [CaImAn, ImageJ]

