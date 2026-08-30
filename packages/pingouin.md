# pingouin

- **Category:** general
- **Papers in survey:** 8
- **Journals:** PNAS (4), Nature (3), Science (1)
- **Years:** 2022 (1), 2023 (1), 2024 (2), 2025 (2), 2026 (2)
- **Versions named:** 0.5.4 (1)
- **Pipeline stages it appears in:** differential/statistical testing (4)

## Papers

### Dopaminergic action prediction errors serve as a value-free teaching signal. (Nature 2025)

- DOI: 10.1038/s41586-025-09008-9 | PMCID: PMC12310545 | PMID: 40369067
- Evidence: Mixed ANOVA was used from the pingouin package.
- Full pipeline: quantification [DeepLabCut] -> differential/statistical testing [Python, scikit-learn, statsmodels] -> stage not stated [SciPy, pingouin]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Version used: **0.5.4**
- Evidence: Software versions SCANPY (v. ≥1.9), pingouin (v.0.5.4), gseapy (v.1.1.1), numpy (v. ≥1.26), scipy (v. ≥1.12), scikit-learn (v. ≥1.13), leidenalg (v.0.10.2), matplotlib (v.3.8.4), Cellrank (v.2.0.7), Palantir (v.1.4.1), R (v.4.3.3), FIJI/ImageJ (v. >1.54) and GraphPad (v. >9.0) were used.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Evidence: Second, we calculated the partial Spearman’s correlation between each SGB and health markers, adjusting for sex, age and BMI, using the ‘pingouin’ Python package (v.0.5.4, https://github.com/raphaelvallat/pingouin ) (Extended Data Figs.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### In situ structural analysis reveals membrane shape transitions during autophagosome formation. (PNAS 2022)

- DOI: 10.1073/pnas.2209823119 | PMCID: PMC9522377 | PMID: 36122245
- Evidence: Statistical analyses were performed with the statistical analysis package in scipy 1.6.2 (scipy.stats) and the pingouin package (v.0.3.11, https://pingouin-stats.org/ ) ( 68 ), using the tests indicated in each respective analysis.
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> differential/statistical testing [SciPy v1.6.2, pingouin] -> structure determination [ChimeraX v1.2.5, IMOD v4.10.49] -> stage not stated [ImageJ v1.53, RELION v3.1.2]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Evidence: The linear regression was performed using the statsmodels package and the Pearson correlation coefficient was calculated using the pingouin package in Python.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: Statistical analyses were performed using the pingouin Python package ( 111 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Pulse timing dominates binaural hearing with cochlear implants. (PNAS 2025)

- DOI: 10.1073/pnas.2416697122 | PMCID: PMC12036976 | PMID: 40244669
- Evidence: 4 , we computed a two-way repeated measures ANOVA using the pingouin library ( https://pingouin-stats.org ).
- Full pipeline: stage not stated [pingouin, statsmodels]

### Hidden state inference requires abstract contextual representations in the ventral hippocampus. (Science 2024)

- DOI: 10.1126/science.adq5874 | PMCID: PMC7618349 | PMID: 39571013
- Evidence: Statistical analysis All statistics were calculated using the Python packages scipy, pingouin and statsmodels , and lme4 R package implemented in Python through rpy2.
- Full pipeline: differential/statistical testing [R, lme4, pingouin, scikit-learn, statsmodels] -> stage not stated [Python, SciPy]

