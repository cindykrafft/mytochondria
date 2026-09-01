# afex

- **Category:** general
- **Papers in survey:** 8
- **Journals:** PNAS (6), Nature (2)
- **Years:** 2022 (2), 2023 (1), 2025 (3), 2026 (2)
- **Versions named:** 0.28 (1), 1.2.1 (1)
- **Pipeline stages it appears in:** differential/statistical testing (3)

## Papers

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Version used: **0.28**
- Evidence: The ANOVA tests were computed using the afex package (afex v.0.28-1) 65 .
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### Vicarious body maps bridge vision and touch in the human brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09796-0 | PMCID: PMC12872459 | PMID: 41299177
- Evidence: ...ment} d z = t N The within-participant differences in topographic connectivity scores were analysed using repeated-measures ANOVA, implemented in the afex package in the R programming language 63 .
- Full pipeline: stage not stated [Connectome Workbench, Python, R, afex, emmeans]

### Mast cell infiltration of the choroid and protease release are early events in age-related macular degeneration associated with genetic risk at both chromosomes 1q32 and 10q26. (PNAS 2022)

- DOI: 10.1073/pnas.2118510119 | PMCID: PMC9171765 | PMID: 35561216
- Evidence: Data were analyzed with a Poisson generalized linear mixed effects model with donor as a random effect using R package “afex” version 0.28-1, function “mixed.” P values were computed based on 1,000 samples of parametric bootstrap.
- Full pipeline: quantification [CellProfiler] -> normalisation [R] -> differential/statistical testing [R, afex] -> stage not stated [Fiji, ImageJ]

### Unlocking adults' implicit statistical learning by cognitive depletion. (PNAS 2022)

- DOI: 10.1073/pnas.2026011119 | PMCID: PMC8764693 | PMID: 34983868
- Evidence: These analyses were performed using the lme4 package ( 61 ) and the afex package ( 62 ) in R (R Development Core Team, 2011).
- Full pipeline: stage not stated [EEGLAB, Psychtoolbox, R, afex, emmeans, lme4]

### Elevated CO<sub>2</sub> alters relative belowground carbon investment for nutrient acquisition in a mature temperate forest. (PNAS 2025)

- DOI: 10.1073/pnas.2503595122 | PMCID: PMC12304975 | PMID: 40663611
- Evidence: To evaluate the effect of eCO 2 on exudate, root morphology and nutrient content, and ECM biomass production, we used linear mixed effect models [ mixed function in the package afex ( 58 )], comparing a full model with CO 2 treatment as a fixed effect, and date and array as random effects, with a null model including with date and array and random effects only by one-way ANOVA.
- Full pipeline: dimensionality reduction/clustering [vegan] -> differential/statistical testing [R v4.4, afex] -> visualisation [R v4.4, vegan]

### Winters restrict a climate change-driven butterfly range expansion despite rapid evolution of seasonal timing traits. (PNAS 2025)

- DOI: 10.1073/pnas.2418392122 | PMCID: PMC12232556 | PMID: 40549916
- Version used: **1.2.1**
- Evidence: For statistical tests, we used the package car 3.1.1 ( 74 ), except for likelihood ratio tests—which we did with anova in base R and the package afex 1.2.1 ( 75 )—and post hoc tests, which we did with emmeans 1.8.5 ( 76 ).
- Full pipeline: differential/statistical testing [afex v1.2.1, emmeans v1.8.5] -> stage not stated [R, lme4 v1.1.32]

### Large language models show amplified cognitive biases in moral decision-making. (PNAS 2025)

- DOI: 10.1073/pnas.2412015122 | PMCID: PMC12207438 | PMID: 40540596
- Evidence: We used the afex package ( 113 ) in R with effect contrast coding, which is the default in this package.
- Full pipeline: stage not stated [afex]

### Contributions of the basolateral amygdala and nucleus accumbens to sustaining not just initiating cognitive effort. (PNAS 2026)

- DOI: 10.1073/pnas.2601231123 | PMCID: PMC13167750 | PMID: 42090260
- Evidence: Repeated-measures ANOVA tested for mean differences in accuracy and reaction between high vs. low value and cognitive effort conditions using the “afex” package ( 67 ). fMRI Acquisition. fMRI data were acquired at the Stanford Center for Cognitive and Neurobiological Imaging using a 3.0T General Electric Discovery MR750 FMRI scanner equipped with a Nova 32-channel head coil.
- Full pipeline: stage not stated [CONN toolbox, PsychoPy, SPM, afex]

