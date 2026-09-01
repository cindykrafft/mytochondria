# Astropy

- **Category:** physical
- **Papers in survey:** 16
- **Journals:** Nature (14), PNAS (1), Cell (1)
- **Years:** 2021 (2), 2022 (2), 2023 (5), 2024 (4), 2025 (3)
- **Versions named:** 2.0.2 (1)

## Papers

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Version used: **2.0.2**
- Evidence: We then used the Rayleigh test (astropy 2.0.2) to assess modulation significance.
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### Measuring the density structure of an accretion hot spot. (Nature 2021)

- DOI: 10.1038/s41586-021-03751-5 | PMCID: PMC8410598 | PMID: 34471274
- Evidence: To measure the period in the light curves, we use the Astropy Lomb–Scargle periodogram function 43 – 45 .
- Full pipeline: stage not stated [Astropy]

### Radiation-driven acceleration in the expanding WR140 dust shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05155-5 | PMCID: PMC9556302 | PMID: 36224416
- Evidence: This research made use of NASA’s Astrophysics Data System; the emcee package 30 ; NUMPY 31 ; MATPLOTLIB 32 ; and Astropy, a community-developed core Python package for Astronomy 33 .
- Full pipeline: stage not stated [Astropy, emcee]

### Observations of a Magellanic Corona. (Nature 2022)

- DOI: 10.1038/s41586-022-05090-5 | PMCID: PMC9519455 | PMID: 36171382
- Evidence: Furthermore, the following software was used in this work: Astropy 62 , 63 , calcos 33 , cartopy 64 , lmfit 37 , SciPy 65 , VoigtFit 36 , Cloudy 45 and Pingouin 66 .
- Full pipeline: normalisation [Cloudy] -> stage not stated [Astropy, SciPy]

### A Milky Way-like barred spiral galaxy at a redshift of 3. (Nature 2023)

- DOI: 10.1038/s41586-023-06636-x | PMCID: PMC10651483 | PMID: 37938777
- Evidence: Finally, we combined all PSF-convolved images using the ccdproc.combine v.2.4.0 astropy image reduction package 38 .
- Full pipeline: stage not stated [Astropy]

### No thick carbon dioxide atmosphere on the rocky exoplanet TRAPPIST-1 c. (Nature 2023)

- DOI: 10.1038/s41586-023-06232-z | PMCID: PMC10447244 | PMID: 37337068
- Evidence: Code availability We used the following codes, resources and Python packages to reduce, analyse and interpret our JWST observations of TRAPPIST-1 c: numpy 81 , matplotlib 82 , astropy 83 , batman 36 , Eureka!
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, dynesty, emcee]

### Resolved imaging confirms a radiation belt around an ultracool dwarf. (Nature 2023)

- DOI: 10.1038/s41586-023-06138-w | PMCID: PMC10338340 | PMID: 37187211
- Evidence: This work also made use of Astropy ( www.astropy.org ), a publicly available community-developed core Python package of tools and resources for astronomy 82 – 85 .
- Full pipeline: stage not stated [Astropy]

### Early Release Science of the exoplanet WASP-39b with JWST NIRISS. (Nature 2023)

- DOI: 10.1038/s41586-022-05674-1 | PMCID: PMC9946829 | PMID: 36623550
- Evidence: This research made use of ccdproc, an Astropy package for image reduction 53 .
- Full pipeline: normalisation [SciPy] -> differential/statistical testing [dynesty] -> simulation/modelling [emcee] -> stage not stated [Astropy, PyMC, PyMC3, Python]

### Identification of carbon dioxide in an exoplanet atmosphere. (Nature 2023)

- DOI: 10.1038/s41586-022-05269-w | PMCID: PMC9946830 | PMID: 36055338
- Evidence: ....io/en/stable/index.html ) and chromatic ( https://zkbt.github.io/chromatic/ ), each of which use the standard Python libraries scipy 98 , numpy 99 , astropy 100 , 101 and matplotlib 102 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### A warm Neptune's methane reveals core mass and vigorous atmospheric mixing. (Nature 2024)

- DOI: 10.1038/s41586-024-07395-z | PMCID: PMC11208151 | PMID: 38768633
- Evidence: Moreover, these codes made use ExoTiC-LD 117 ( https://exotic-ld.readthedocs.io/en/latest/ ) and Emcee ( https://emcee.readthedocs.io/en/stable/ ) 118 , which use the Python libraries scipy 119 , numpy 120 , astropy 121 and matplotlib 122 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty, emcee]

### Star formation shut down by multiphase gas outflow in a galaxy at a redshift of 2.45. (Nature 2024)

- DOI: 10.1038/s41586-024-07412-1 | PMCID: PMC11153157 | PMID: 38648852
- Evidence: Code availability We used publicly available code including the JWST data reduction pipeline ( https://github.com/spacetelescope/jwst ), Prospector 39 , Forcepho (B.D.J. et al., manuscript in preparation; https://github.com/bd-j/forcepho ), dynesty 50 , astropy 85 , pyneb 61 , linetools 86 and specutils 87 .
- Full pipeline: stage not stated [Astropy, dynesty]

### A dynamical measure of the black hole mass in a quasar 11 billion years ago. (Nature 2024)

- DOI: 10.1038/s41586-024-07053-4 | PMCID: PMC11636685 | PMID: 38286342
- Evidence: To avoid large outliers influencing the fit, we used the FittingWithOutlierRemoval function in the astropy.modeling module 45 to iteratively perform fits and at each step remove all channels more than 3 σ away from the previous best fit.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### One-third of Sun-like stars are born with misaligned planet-forming disks. (Nature 2025)

- DOI: 10.1038/s41586-025-09324-0 | PMCID: PMC12350154 | PMID: 40770103
- Evidence: 97 ), Lightkurve 68 , Astropy 102 , NumPy 103 , SciPy 104 and Matplotlib 105 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, Python, SciPy]

### Evidence for a sub-Jovian planet in the young TWA 7 disk. (Nature 2025)

- DOI: 10.1038/s41586-025-09150-4 | PMCID: PMC12221965 | PMID: 40562924
- Evidence: We used various functions of the following software packages to perform the analysis and create the figures: numpy, astropy, scipy, matplotlib and photutils.
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: We then used sigma clipping (function, astropy.stats.sigma_clipped_stats; sigma=3.0, maxiters=10, cenfunc=‘median’, stdfunc=‘mad_std’) to estimate the mean background signal level for this subvolume, μ bg , and set the watershed-detection threshold for each sample to 10* μ bg .
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: All plots were generated using Matplotlib ( 58 ), Seaborn ( https://seaborn.pydata.org ) adjustText ( https://github.com/Phlya/adjustText ), mpl-scatter-density ( https://github.com/astrofrog/mpl-scatter-density ), Astropy ( 59 , 60 ), and Scanpy ( 50 ) libraries under Python 3.7.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

