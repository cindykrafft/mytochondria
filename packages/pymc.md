# PyMC

- **Category:** general
- **Papers in survey:** 12
- **Journals:** Nature (8), PNAS (4)
- **Years:** 2022 (2), 2023 (3), 2024 (2), 2025 (2), 2026 (3)
- **Versions named:** 5.17.0 (1), 3.11.5 (1)
- **Pipeline stages it appears in:** simulation/modelling (4), differential/statistical testing (4)

## Papers

### Early Release Science of the exoplanet WASP-39b with JWST NIRCam. (Nature 2023)

- DOI: 10.1038/s41586-022-05590-4 | PMCID: PMC9946836 | PMID: 36623551
- Evidence: 55 , jwst 100 , chromatic, chromatic-fitting, PyMC3 61 , Exoplanet 62 , 63 , gCMCRT 101 , CONAN 57 , 58 , ExoTiC-LD 64 – 66 , LACOSMIC 59 , PICASO 77 , 78 , Virga 90 and VULCAN 33 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Jupyter, PyMC, PyMC3]

### Early Release Science of the exoplanet WASP-39b with JWST NIRISS. (Nature 2023)

- DOI: 10.1038/s41586-022-05674-1 | PMCID: PMC9946829 | PMID: 36623550
- Evidence: In this paper, we applied chromatic_fitting to the nirHiss reduction. chromatic_fitting uses the PyMC3 (NUTS) sampler 58 to fit the exoplanet transit model to the light curves.
- Full pipeline: normalisation [SciPy] -> differential/statistical testing [dynesty] -> simulation/modelling [emcee] -> stage not stated [Astropy, PyMC, PyMC3, Python]

### A hot-Jupiter progenitor on a super-eccentric retrograde orbit. (Nature 2024)

- DOI: 10.1038/s41586-024-07688-3 | PMCID: PMC11291287 | PMID: 39020171
- Evidence: 101 to fit the transits, and the orbital parameter posteriors are sampled using the PyMC3 Hamiltonian Monte Carlo package 102 .
- Full pipeline: simulation/modelling [PyMC, PyMC3]

### Sulfur dioxide in the mid-infrared transmission spectrum of WASP-39b. (Nature 2024)

- DOI: 10.1038/s41586-024-07040-9 | PMCID: PMC10901732 | PMID: 38232945
- Evidence: We then used PyMC3’s No-U-Turn Sampler 32 to sample our posterior.
- Full pipeline: differential/statistical testing [dynesty] -> simulation/modelling [dynesty, emcee] -> stage not stated [PyMC, PyMC3]

### Thermal asymmetry in the Moon's mantle inferred from monthly tidal response. (Nature 2025)

- DOI: 10.1038/s41586-025-08949-5 | PMCID: PMC12119328 | PMID: 40369068
- Evidence: Inversion procedure To constrain the structure of the lunar interior based on GL1800F, we carry out a Bayesian inversion using MCMC with a Metropolis–Hastings sampling algorithm using PyMC.
- Full pipeline: differential/statistical testing [PyMC]

### A prototype differential atom interferometer for fundamental physics. (Nature 2026)

- DOI: 10.1038/s41586-026-10617-1 | PMCID: PMC13275304 | PMID: 42310113
- Evidence: We use a No-U Turn Markov-chain Monte Carlo method implemented in the PyMC package 68 to sample from the posterior distribution of σ δ ϕ .
- Full pipeline: simulation/modelling [PyMC] -> stage not stated [Python]

### Little red dots as young supermassive black holes in dense ionized cocoons. (Nature 2026)

- DOI: 10.1038/s41586-025-09900-4 | PMCID: PMC12804088 | PMID: 41535486
- Version used: **5.17.0**
- Evidence: Emission line models All best-fit results in this paper were produced using the Monte Carlo Markov Chain (MCMC) NUTS sampler as part of the package PyMC v.
- Full pipeline: simulation/modelling [PyMC v5.17.0] -> stage not stated [emcee]

### A young progenitor for the most common planetary systems in the Galaxy. (Nature 2026)

- DOI: 10.1038/s41586-025-09840-z | PMCID: PMC12779570 | PMID: 41501195
- Evidence: We used PyMC3 44 , exoplanet ( https://docs.exoplanet.codes/en/stable/ ) 45 and starry 46 to fit the light curve, incorporating tailored models for correlated noise and instrumental systematics appropriate for each dataset.
- Full pipeline: simulation/modelling [SciPy] -> stage not stated [PyMC, PyMC3]

### Dynamics of <i>Drosophila</i> endoderm specification. (PNAS 2022)

- DOI: 10.1073/pnas.2112892119 | PMCID: PMC9169638 | PMID: 35412853
- Evidence: We utilized the PyMC3 package for Bayesian modeling ( 69 ) and ran three chains of the No-U-Turn sampling.
- Full pipeline: dimensionality reduction/clustering [ilastik] -> differential/statistical testing [PyMC, PyMC3] -> machine learning [scikit-learn]

### Dynamic gene expression and growth underlie cell-to-cell heterogeneity in <i>Escherichia coli</i> stress response. (PNAS 2022)

- DOI: 10.1073/pnas.2115032119 | PMCID: PMC9168488 | PMID: 35344432
- Evidence: Statistical inference was performed with PyMC3 ( 66 ), a Python package for probabilistic programming.
- Full pipeline: differential/statistical testing [PyMC, PyMC3]

### Digitizing chemical discovery with a Bayesian explorer for interpreting reactivity data. (PNAS 2023)

- DOI: 10.1073/pnas.2220045120 | PMCID: PMC10151610 | PMID: 37068251
- Evidence: Inference is carried out using Hamiltonian Monte Carlo, specifically using the No-U-turn sampler ( 34 ) algorithm for sampling as implemented in the NumPyro probabilistic programming package ( 33 , 58 ), early prototyping performed using the PyMC3 probabilistic programming package ( 59 ).
- Full pipeline: simulation/modelling [PyMC, PyMC3]

### High organofluorine concentrations in municipal wastewater affect downstream drinking water supplies for millions of Americans. (PNAS 2025)

- DOI: 10.1073/pnas.2417156122 | PMCID: PMC11761303 | PMID: 39761386
- Version used: **3.11.5**
- Evidence: 1 and using Bayesian linear regression implemented in PyMC3 version 3.11.5 ( 59 ) in Python version 3.9.7.
- Full pipeline: differential/statistical testing [PyMC v3.11.5, PyMC3 v3.11.5, Python v3.9.7]

