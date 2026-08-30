# dynesty

- **Category:** physical
- **Papers in survey:** 18
- **Journals:** Nature (16), PNAS (2)
- **Years:** 2023 (9), 2024 (5), 2025 (3), 2026 (1)
- **Pipeline stages it appears in:** differential/statistical testing (5), simulation/modelling (1), quantification (1)

## Papers

### Water in the terrestrial planet-forming zone of the PDS 70 disk. (Nature 2023)

- DOI: 10.1038/s41586-023-06317-9 | PMCID: PMC10432267 | PMID: 37488359
- Evidence: We use the MultiNest Bayesian fitting algorithm 62 and the PyMultiNest package 63 to find the best-fit parameters.
- Full pipeline: differential/statistical testing [dynesty] -> visualisation [Matplotlib v3.5.1] -> stage not stated [SciPy]

### Carbonaceous dust grains seen in the first billion years of cosmic time. (Nature 2023)

- DOI: 10.1038/s41586-023-06413-w | PMCID: PMC10499605 | PMID: 37467786
- Evidence: We then performed several Bayesian power-law fitting procedures to the rest-frame UV continuum with a Python implementation 55 of the MultiNest 56 nested sampling algorithm.
- Full pipeline: differential/statistical testing [dynesty]

### No thick carbon dioxide atmosphere on the rocky exoplanet TRAPPIST-1 c. (Nature 2023)

- DOI: 10.1038/s41586-023-06232-z | PMCID: PMC10447244 | PMID: 37337068
- Evidence: 9 , jwst 32 , emcee 35 , trafit 41 – 43 , dynesty 84 , 85 , SMART 60 , VPL Climate 3 , 58 , 59 , DISORT 56 , 57 and IRAF/DAOPHOT 33 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, dynesty, emcee]

### A broadband thermal emission spectrum of the ultra-hot Jupiter WASP-18b. (Nature 2023)

- DOI: 10.1038/s41586-023-06230-1 | PMCID: PMC10412449 | PMID: 37257843
- Evidence: The PyMultiNest 103 routine is used to sample the 1D-RCTE spectra through interpolation (and subsequent binning to the data wavelength bins) to obtain posterior probability constraints on the above parameters.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [emcee] -> stage not stated [MOM6, dynesty, scikit-image]

### A massive quiescent galaxy at redshift 4.658. (Nature 2023)

- DOI: 10.1038/s41586-023-06158-6 | PMCID: PMC10371866 | PMID: 37216978
- Evidence: We fitted our model to the data using the MultiNest nested sampling algorithm 49 – 51 .
- Full pipeline: stage not stated [dynesty]

### Forming intracluster gas in a galaxy protocluster at a redshift of 2.16. (Nature 2023)

- DOI: 10.1038/s41586-023-05761-x | PMCID: PMC10060161 | PMID: 36991192
- Evidence: We specifically exploit the implementation provided in the dynesty (ref.
- Full pipeline: stage not stated [dynesty]

### Early Release Science of the exoplanet WASP-39b with JWST NIRISS. (Nature 2023)

- DOI: 10.1038/s41586-022-05674-1 | PMCID: PMC9946829 | PMID: 36623550
- Evidence: We compare the observations to these models in a Bayesian inference framework using the nested sampling algorithm MultiNest 108 through its Python implementation PyMultiNest 109 and obtain an optimal set of M/H, C/O ratio, K/O ratio and f through nearest-neighbour search in the grid.
- Full pipeline: normalisation [SciPy] -> differential/statistical testing [dynesty] -> simulation/modelling [emcee] -> stage not stated [Astropy, PyMC, PyMC3, Python]

### Early Release Science of the exoplanet WASP-39b with JWST NIRSpec G395H. (Nature 2023)

- DOI: 10.1038/s41586-022-05591-3 | PMCID: PMC9946835 | PMID: 36623549
- Evidence: Fitting pipeline 4: transitspectroscopy We fit the broadband and spectroscopic light curves produced from the transitspectroscopy stellar spectra, running juliet 68 in parallel with the light-curve-fitting module of the transitspectroscopy pipeline 48 with dynamic nested sampling through dynesty 69 and analytical transit models computed using batman.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy, dynesty]

### Identification of carbon dioxide in an exoplanet atmosphere. (Nature 2023)

- DOI: 10.1038/s41586-022-05269-w | PMCID: PMC9946830 | PMID: 36055338
- Evidence: ...xoTiC-ISM ), ExoTiC-LD 60 ( https://exotic-ld.readthedocs.io/en/latest/ ), Emcee 63 ( https://emcee.readthedocs.io/en/stable/ ), DYNESTY 74 ( https://dynesty.readthedocs.io/en/stable/index.html ) and chromatic ( https://zkbt.github.io/chromatic/ ), each of which use the standard Python libraries scipy 98 , numpy 99 , astropy 100 , 101 and matplotlib 102 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### A warm Neptune's methane reveals core mass and vigorous atmospheric mixing. (Nature 2024)

- DOI: 10.1038/s41586-024-07395-z | PMCID: PMC11208151 | PMID: 38768633
- Evidence: It couples a correlated-k 59 radiative transfer scheme with the PyMultiNest 70 – 72 , 94 Nested Sampling algorithm 95 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty, emcee]

### Star formation shut down by multiphase gas outflow in a galaxy at a redshift of 2.45. (Nature 2024)

- DOI: 10.1038/s41586-024-07412-1 | PMCID: PMC11153157 | PMID: 38648852
- Evidence: The model has a total of 25 free parameters, and to fully explore the posterior distribution we use the nested sampling package dynesty 50 .
- Full pipeline: stage not stated [Astropy, dynesty]

### A dynamical measure of the black hole mass in a quasar 11 billion years ago. (Nature 2024)

- DOI: 10.1038/s41586-024-07053-4 | PMCID: PMC11636685 | PMID: 38286342
- Evidence: We used the dynesty package 51 (v2.1), which performs dynamic nested sampling 52 to sample the potentially complicated posterior.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Sulfur dioxide in the mid-infrared transmission spectrum of WASP-39b. (Nature 2024)

- DOI: 10.1038/s41586-024-07040-9 | PMCID: PMC10901732 | PMID: 38232945
- Evidence: ARCiS ARCiS (ARtful modelling Code for exoplanet Science) is an atmospheric modelling and Bayesian retrieval package 78 , 79 , which uses the MultiNest 80 Monte Carlo nested sampling algorithm to sample a parameter space for the region of maximum likelihood.
- Full pipeline: differential/statistical testing [dynesty] -> simulation/modelling [dynesty, emcee] -> stage not stated [PyMC, PyMC3]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Evidence: Here we used a nested sampling approach using the dynesty package 91 – 93 .
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### Witnessing the onset of reionization through Lyman-α emission at redshift 13. (Nature 2025)

- DOI: 10.1038/s41586-025-08779-5 | PMCID: PMC11946913 | PMID: 40140594
- Evidence: We used the PyMultiNest 100 implementation of the multimodal nested-sampling algorithm MultiNest 101 to perform a Bayesian fitting routine to the sigma-clipped PRISM spectrum and corresponding covariance matrix (see Supplementary information ) from 1.609 μm up to 2.897 μm (127 wavelength bins), or 1,150 Å ≲ λ emit ≲ 2,000 Å at z = 13.
- Full pipeline: differential/statistical testing [dynesty]

### Aerosols and hydrocarbons in the atmosphere of a white dwarf planet. (Nature 2026)

- DOI: 10.1038/s41586-026-10514-7 | PMCID: PMC13322981 | PMID: 42387166
- Evidence: Our retrieval model is thus defined by 25 free parameters, which we fit using MultiNest’s 42 – 44 Python wrapper PyMultiNest 45 with 1,000 live points.
- Full pipeline: stage not stated [dynesty]

### Using JADES NIRCam photometry to investigate the dependence of stellar mass inferences on the IMF in the early universe. (PNAS 2024)

- DOI: 10.1073/pnas.2317375121 | PMCID: PMC11494360 | PMID: 39378084
- Evidence: The posterior distributions are sampled using the dynamic nested sampling code dynesty, ref.
- Full pipeline: stage not stated [dynesty]

### A precise metallicity and carbon-to-oxygen ratio for a warm giant exoplanet from its panchromatic JWST emission spectrum. (PNAS 2025)

- DOI: 10.1073/pnas.2416193122 | PMCID: PMC12501160 | PMID: 40982673
- Evidence: We estimate WASP-80 b’s atmosphere parameters using nested sampling with PyMultiNest ( 61 ) and 500 live points (parameter combinations) over the full model grid [T day , T int , [M/H], C/O, and log 10 (K zz )], with the addition of a vertically uniform gray cloud opacity ( κ cld , effectively an abundance weighted gray cross-section), and a dilution factor ( A ) multiplying the planetary flux spe...
- Full pipeline: quantification [dynesty] -> stage not stated [SciPy, emcee]

