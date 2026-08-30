# JAGS

- **Category:** general
- **Papers in survey:** 20
- **Journals:** PNAS (18), Nature (1), Lancet (1)
- **Years:** 2021 (1), 2022 (4), 2023 (6), 2024 (3), 2025 (6)
- **Versions named:** 4.3 (1), 4.2.0 (1)
- **Pipeline stages it appears in:** differential/statistical testing (10), simulation/modelling (4), quantification (1)

## Papers

### Global, regional, and national prevalence estimates of physical or sexual, or both, intimate partner violence against women in 2018. (Lancet 2022)

- DOI: 10.1016/s0140-6736(21)02664-7 | PMCID: PMC8885817 | PMID: 35182472
- Evidence: The posterior distribution of the model variables were estimated using Markov chain Monte Carlo simulations in JAGS software version 4.6.
- Full pipeline: differential/statistical testing [R v4.0.4] -> simulation/modelling [JAGS]

### Functional evaluation and clinical classification of BRCA2 variants. (Nature 2025)

- DOI: 10.1038/s41586-024-08388-8 | PMCID: PMC11821525 | PMID: 39779857
- Evidence: The JAGS language 38 was used to specify and fit the VarCall model using a MCMC algorithm.
- Full pipeline: read trimming [Cutadapt v3.5] -> alignment/mapping [BWA v0.7.17, PyMOL] -> dimensionality reduction/clustering [PyMOL] -> stage not stated [JAGS]

### Climate variability and density-dependent population dynamics: Lessons from a simple High Arctic ecosystem. (PNAS 2021)

- DOI: 10.1073/pnas.2106635118 | PMCID: PMC8449336 | PMID: 34504000
- Version used: **4.2.0**
- Evidence: 1 – 3 ) was fitted in JAGS version 4.2.0 ( 65 ).
- Full pipeline: stage not stated [JAGS v4.2.0, R]

### Large-effect loci mediate rapid adaptation of salmon body size after river regulation. (PNAS 2022)

- DOI: 10.1073/pnas.2207634119 | PMCID: PMC9636922 | PMID: 36279467
- Evidence: 47 ) by using the Just Another Gibbs Sampler software (JAGS) and by including the “dinterval” function to ensure that x ( i , t ) | x ( i , t − 1 ) ranged between zero and one ( 48 ).
- Full pipeline: simulation/modelling [R] -> stage not stated [JAGS]

### Bending the curve: Simple but massive conservation action leads to landscape-scale recovery of amphibians. (PNAS 2022)

- DOI: 10.1073/pnas.2123070119 | PMCID: PMC9586276 | PMID: 36215493
- Evidence: Models were fitted in JAGS, run through R version 4.0.3 with package jagsUI (code in SI Appendix S5 ).
- Full pipeline: stage not stated [JAGS, QGIS v3.16, R v4.0.3]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Evidence: The JAGS-transformed values were log transformed.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### The role of tropical rainfall in driving range dynamics for a long-distance migratory bird. (PNAS 2023)

- DOI: 10.1073/pnas.2301055120 | PMCID: PMC10756294 | PMID: 38109531
- Evidence: We fit a hierarchical Poisson regression model using Markov chain Monte Carlo methods in Just Another Gibbs Sampler (JAGS) ( 55 ) implemented through R with package R2jags ( 56 ).
- Full pipeline: differential/statistical testing [JAGS] -> simulation/modelling [JAGS] -> stage not stated [R]

### An observation-based, reduced-form model for oxidation in the remote marine troposphere. (PNAS 2023)

- DOI: 10.1073/pnas.2209735120 | PMCID: PMC10451388 | PMID: 37579162
- Evidence: This approach was implemented in R using MCMC with the Just Another Gibbs Sampler (JAGS) packages rjags ( 103 , 104 ) and runjags ( 105 ).
- Full pipeline: stage not stated [JAGS]

### Fossil leaves reveal drivers of herbivore functional diversity during the Cenozoic. (PNAS 2023)

- DOI: 10.1073/pnas.2300514120 | PMCID: PMC10410718 | PMID: 37523540
- Version used: **4.3**
- Evidence: The Bayesian models were implemented in JAGS (version 4.3) and run in R via the rjags package (version 4-10) ( 69 ).
- Full pipeline: differential/statistical testing [JAGS v4.3] -> stage not stated [R v4.0.3]

### Demographic rates reveal the benefits of protected areas in a long-lived migratory bird. (PNAS 2023)

- DOI: 10.1073/pnas.2212035120 | PMCID: PMC10041063 | PMID: 36913571
- Evidence: All models were fitted within a Bayesian framework via Markov Chain Monte Carlo (MCMC) in JAGS (Just Another Gibbs Sampler, v.
- Full pipeline: differential/statistical testing [JAGS] -> simulation/modelling [JAGS] -> stage not stated [R, lme4]

### Intentional release of native species undermines ecological stability. (PNAS 2023)

- DOI: 10.1073/pnas.2218044120 | PMCID: PMC9963293 | PMID: 36749724
- Evidence: We fitted the models to the data using Just Another Gibbs Sampler (JAGS) version 4.1.0 through runjags package version 2.2.0-2 in R ( 78 ).
- Full pipeline: stage not stated [JAGS, R]

### Recent and future declines of a historically widespread pollinator linked to climate, land cover, and pesticides. (PNAS 2023)

- DOI: 10.1073/pnas.2211223120 | PMCID: PMC9945941 | PMID: 36689649
- Evidence: We wrote occupancy models in the JAGS language ( 70 ) and fit models using package NIMBLE ( 71 , 72 ).
- Full pipeline: differential/statistical testing [R v4.1] -> stage not stated [JAGS]

### Tipping the balance between fairness and efficiency through temporoparietal stimulation. (PNAS 2024)

- DOI: 10.1073/pnas.2409395121 | PMCID: PMC11494363 | PMID: 39388264
- Evidence: Parameters were estimated in a hierarchical Bayesian fashion with the dbern module in JAGS ( 52 ), assuming that individual parameters are normally distributed around a group-level parameter.
- Full pipeline: differential/statistical testing [JAGS] -> stage not stated [R v4.0.0, SPM, lme4]

### Impacts of fire and prospects for recovery in a tropical peat forest ecosystem. (PNAS 2024)

- DOI: 10.1073/pnas.2307216121 | PMCID: PMC11047076 | PMID: 38621126
- Evidence: All analyses conducted were specified within a Bayesian framework, implemented in rstan (hierarchical mixed-effects meta-analysis) and JAGS (all GLMMs and occupancy models) called through R version 4.0.2.
- Full pipeline: differential/statistical testing [JAGS, R v4.0.2]

### Climate change determines the sign of productivity trends in US forests. (PNAS 2024)

- DOI: 10.1073/pnas.2311132121 | PMCID: PMC10823222 | PMID: 38227667
- Evidence: These methods included the nonlinear mixed effects “ nlme ” function in R ( 77 ) and a hierarchical Bayesian approach in JAGS ( 78 ).
- Full pipeline: differential/statistical testing [JAGS] -> stage not stated [R v4.2.0]

### Conscious awareness, sensory integration, and evidence accumulation in bodily self-perception. (PNAS 2025)

- DOI: 10.1073/pnas.2503629122 | PMCID: PMC12704745 | PMID: 41337481
- Evidence: Perceptual awareness efficiency was quantified via Bayesian hierarchical modeling ( 52 ) using JAGS with three 10,000-iteration MCMC chains (1,000 burn-in).
- Full pipeline: quantification [JAGS] -> differential/statistical testing [JAGS] -> stage not stated [Docker, R]

### Seed dispersal disruption limits tropical forest regrowth. (PNAS 2025)

- DOI: 10.1073/pnas.2500951122 | PMCID: PMC12318199 | PMID: 40705429
- Evidence: In a Bayesian model implemented in JAGS, we fitted a saturating model of aboveground carbon ( μ ) over time in years ( t ) using the Monod equation ( 77 , 78 ). μ = α t β + t .
- Full pipeline: differential/statistical testing [JAGS]

### Thermal mismatch models derived from occurrence data predict pathogen prevalence in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2423706122 | PMCID: PMC12318235 | PMID: 40690669
- Evidence: We fitted the model to the data within a Bayesian framework using JAGS ( 75 ) called from R using the R package jagsUI ( 76 ).
- Full pipeline: differential/statistical testing [JAGS] -> stage not stated [R]

### eDNA confirms lower trophic interactions help to modulate population outbreaks of the notorious crown-of-thorns sea star. (PNAS 2025)

- DOI: 10.1073/pnas.2424560122 | PMCID: PMC11929471 | PMID: 40063810
- Evidence: The Bayesian SEM was developed using the blavaan package, which relies on JAGS and Stan to estimate models via Markov Chain Monte Carlo simulation ( 77 ).
- Full pipeline: differential/statistical testing [JAGS, R v4.1, Stan] -> simulation/modelling [JAGS, Stan] -> stage not stated [emmeans]

### Prey depletion, interspecific competition, and the energetics of hunting in endangered African wild dogs, &lt;i&gt;Lycaon pictus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2414772122 | PMCID: PMC11831116 | PMID: 39869818
- Evidence: R and JAGS code for the hierarchical distance sampling model are provided at the GitHub link in the Data, Materials, and Software Availability statement ( 86 ).
- Full pipeline: quantification [R] -> stage not stated [JAGS, tidyverse]

