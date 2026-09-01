# emcee

- **Category:** physical
- **Papers in survey:** 28
- **Journals:** Nature (24), PNAS (4)
- **Years:** 2022 (4), 2023 (10), 2024 (8), 2025 (5), 2026 (1)
- **Pipeline stages it appears in:** simulation/modelling (16), differential/statistical testing (2), quantification (1)

## Papers

### A nearby long gamma-ray burst from a merger of compact objects. (Nature 2022)

- DOI: 10.1038/s41586-022-05327-3 | PMCID: PMC9729102 | PMID: 36477127
- Evidence: We performed Bayesian parameter estimation with emcee 64 and nine free parameters: n , p , E K,iso , θ c , θ v , an outer jet truncation angle θ w , shock microphysical parameters ε e and ε B , and the participation fraction ξ N .
- Full pipeline: differential/statistical testing [emcee] -> stage not stated [SExtractor]

### Radiation-driven acceleration in the expanding WR140 dust shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05155-5 | PMCID: PMC9556302 | PMID: 36224416
- Evidence: This research made use of NASA’s Astrophysics Data System; the emcee package 30 ; NUMPY 31 ; MATPLOTLIB 32 ; and Astropy, a community-developed core Python package for Astronomy 33 .
- Full pipeline: stage not stated [Astropy, emcee]

### Solar flare accelerates nearly all electrons in a large coronal volume. (Nature 2022)

- DOI: 10.1038/s41586-022-04728-8 | PMCID: PMC9217745 | PMID: 35676480
- Evidence: Here we use the Markov chain Monte Carlo (MCMC) simulations, implemented by an open-source Python package emcee 26 , to derive statistical distributions of the model fit parameters to quantify the confidence of this finding.
- Full pipeline: quantification [emcee] -> differential/statistical testing [emcee] -> simulation/modelling [emcee]

### First observation of &lt;sup&gt;28&lt;/sup&gt;O. (Nature 2023)

- DOI: 10.1038/s41586-023-06352-6 | PMCID: PMC10630140 | PMID: 37648757
- Evidence: We sample the posterior using the affine invariant Markov chain Monte Carlo (MCMC) ensemble sampler emcee 102 and the resulting distribution is shown in the upper-right triangle of Extended Data Fig.
- Full pipeline: simulation/modelling [Geant4, emcee]

### No thick carbon dioxide atmosphere on the rocky exoplanet TRAPPIST-1 c. (Nature 2023)

- DOI: 10.1038/s41586-023-06232-z | PMCID: PMC10447244 | PMID: 37337068
- Evidence: Data analysis SZ We fitted the eclipse light curve using the open-source Python MCMC sampling routine emcee 35 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, dynesty, emcee]

### A broadband thermal emission spectrum of the ultra-hot Jupiter WASP-18b. (Nature 2023)

- DOI: 10.1038/s41586-023-06230-1 | PMCID: PMC10412449 | PMID: 37257843
- Evidence: Light-curve fits are performed using the affine-invariant Markov chain Monte Carlo (MCMC) ensemble sampler emcee 82 , using 20,000 steps and four walkers per free parameter.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [emcee] -> stage not stated [MOM6, dynesty, scikit-image]

### Early Release Science of the exoplanet WASP-39b with JWST NIRCam. (Nature 2023)

- DOI: 10.1038/s41586-022-05590-4 | PMCID: PMC9946836 | PMID: 36623551
- Evidence: For all fits, the parameters were estimated with a Markov chain Monte Carlo fit, using either the emcee Python package 60 (for fits performed with Eureka!), the pymc3 Python package 61 (implemented through the Exoplanet code 62 , 63 , for fits performed with chromatic-fitting or tshirt) or the CONAN Python package 57 , 58 (for fits performed with HANSOLO).
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Jupyter, PyMC, PyMC3]

### Early Release Science of the exoplanet WASP-39b with JWST NIRISS. (Nature 2023)

- DOI: 10.1038/s41586-022-05674-1 | PMCID: PMC9946829 | PMID: 36623550
- Evidence: We fit the light curves using the Markov chain Monte Carlo (MCMC) ensemble sampler emcee 75 for 1,000 steps using four walkers per free parameter.
- Full pipeline: normalisation [SciPy] -> differential/statistical testing [dynesty] -> simulation/modelling [emcee] -> stage not stated [Astropy, PyMC, PyMC3, Python]

### Early Release Science of the exoplanet WASP-39b with JWST NIRSpec PRISM. (Nature 2023)

- DOI: 10.1038/s41586-022-05677-y | PMCID: PMC9946832 | PMID: 36623548
- Evidence: We fit this white light curve using the Markov chain Monte Carlo sampler emcee 32 within the least-squares minimization framework of lmfit.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy]

### Early Release Science of the exoplanet WASP-39b with JWST NIRSpec G395H. (Nature 2023)

- DOI: 10.1038/s41586-022-05591-3 | PMCID: PMC9946835 | PMID: 36623549
- Evidence: We fitted our broadband light curve with a transit + systematics model using a Gaussian process (GP) 63 , 64 , implemented through george 65 , and a Markov chain Monte Carlo method, implemented through emcee 66 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy, dynesty]

### Identification of carbon dioxide in an exoplanet atmosphere. (Nature 2023)

- DOI: 10.1038/s41586-022-05269-w | PMCID: PMC9946830 | PMID: 36055338
- Evidence: We used the Markov chain Monte Carlo sampling routine emcee 63 to find the best-fit parameters and measure the posterior distribution.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Quasi-periodic X-ray eruptions years after a nearby tidal disruption event. (Nature 2024)

- DOI: 10.1038/s41586-024-08023-6 | PMCID: PMC11499261 | PMID: 39385028
- Evidence: The fit was performed using Markov chain Monte Carlo techniques, using the emcee formalism 74 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy]

### A temperate super-Jupiter imaged with JWST in the mid-infrared. (Nature 2024)

- DOI: 10.1038/s41586-024-07837-8 | PMCID: PMC11424479 | PMID: 39048015
- Evidence: We sampled the posterior with a Monte Carlo Markov chain (using emcee; ref.
- Full pipeline: simulation/modelling [emcee]

### Fast-moving stars around an intermediate-mass black hole in ω Centauri. (Nature 2024)

- DOI: 10.1038/s41586-024-07511-z | PMCID: PMC11236702 | PMID: 38987499
- Evidence: The posterior was sampled using a Markov chain Monte Carlo (MCMC) ensemble sampler implemented using the package emcee 61 using recommended burn-in and autocorrelation corrections.
- Full pipeline: simulation/modelling [emcee]

### Bound star clusters observed in a lensed galaxy 460 Myr after the Big Bang. (Nature 2024)

- DOI: 10.1038/s41586-024-07703-7 | PMCID: PMC11324512 | PMID: 38914113
- Evidence: The source plane model parameters are first optimized using a downhill simplex algorithm, then sampled using an MCMC with the Python package emcee 47 .
- Full pipeline: stage not stated [emcee]

### A warm Neptune's methane reveals core mass and vigorous atmospheric mixing. (Nature 2024)

- DOI: 10.1038/s41586-024-07395-z | PMCID: PMC11208151 | PMID: 38768633
- Evidence: Moreover, these codes made use ExoTiC-LD 117 ( https://exotic-ld.readthedocs.io/en/latest/ ) and Emcee ( https://emcee.readthedocs.io/en/stable/ ) 118 , which use the Python libraries scipy 119 , numpy 120 , astropy 121 and matplotlib 122 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty, emcee]

### Methane emission from a cool brown dwarf. (Nature 2024)

- DOI: 10.1038/s41586-024-07190-w | PMCID: PMC11023930 | PMID: 38632480
- Evidence: In this work, we coupled the forward model to the emcee sampler 66 , which is the same method used in refs.
- Full pipeline: stage not stated [emcee]

### A dynamical measure of the black hole mass in a quasar 11 billion years ago. (Nature 2024)

- DOI: 10.1038/s41586-024-07053-4 | PMCID: PMC11636685 | PMID: 38286342
- Evidence: We use the emcee package 47 to perform Markov chain Monte Carlo sampling to fit for ( x i , y i ) of the central ten spectral channels across the Hα line and sample the posterior.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Sulfur dioxide in the mid-infrared transmission spectrum of WASP-39b. (Nature 2024)

- DOI: 10.1038/s41586-024-07040-9 | PMCID: PMC10901732 | PMID: 38232945
- Evidence: In all light-curve fits, we used Markov chain Monte Carlo implemented using emcee 43 .
- Full pipeline: differential/statistical testing [dynesty] -> simulation/modelling [dynesty, emcee] -> stage not stated [PyMC, PyMC3]

### Titan's strong tidal dissipation precludes a subsurface ocean. (Nature 2025)

- DOI: 10.1038/s41586-025-09818-x | PMCID: PMC12711566 | PMID: 41407902
- Evidence: To validate the results obtained with the Metropolis–Hastings sampler, we also ran a separate analysis using the affine-invariant ensemble sampler provided by the open-source library emcee 65 , with the same parameter space.
- Full pipeline: stage not stated [emcee]

### Calving-driven fjord dynamics resolved by seafloor fibre sensing. (Nature 2025)

- DOI: 10.1038/s41586-025-09347-7 | PMCID: PMC12350177 | PMID: 40804151
- Evidence: We now initialize a Markov-chain Monte-Carlo sampler with 64 walkers for each inversion parameter, randomly distributed around the initial cable location using the affine invariant Markov-chain Monte-Carlo (MCMC) ensemble sampler emcee 57 for maximizing the logarithmic probability function from (6).
- Full pipeline: stage not stated [Jupyter, emcee]

### One-third of Sun-like stars are born with misaligned planet-forming disks. (Nature 2025)

- DOI: 10.1038/s41586-025-09324-0 | PMCID: PMC12350154 | PMID: 40770103
- Evidence: In the context of HBM, the model parameters are hyperparameters with posterior distributions determined with the affine-invariant Markov chain Monte Carlo (MCMC) sampler emcee 99 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, Python, SciPy]

### Io's tidal response precludes a shallow magma ocean. (Nature 2025)

- DOI: 10.1038/s41586-024-08442-5 | PMCID: PMC11798835 | PMID: 39667409
- Evidence: A large parameter space is explored using the affine invariant ensemble sampler implemented in the open-source library, emcee 81 .
- Full pipeline: stage not stated [emcee]

### Little red dots as young supermassive black holes in dense ionized cocoons. (Nature 2026)

- DOI: 10.1038/s41586-025-09900-4 | PMCID: PMC12804088 | PMID: 41535486
- Evidence: 65 ), except objects A and D, which were fitted using the Ensemble sampler emcee v.
- Full pipeline: simulation/modelling [PyMC v5.17.0] -> stage not stated [emcee]

### <i>Mycobacterium tuberculosis</i> DNA repair helicase UvrD1 is activated by redox-dependent dimerization via a 2B domain cysteine. (PNAS 2022)

- DOI: 10.1073/pnas.2114501119 | PMCID: PMC8872793 | PMID: 35173050
- Evidence: Python 3 was installed via Anaconda along with modules such as numpy, scipy, matpotlib, lmfit, emcee, corner, os, and pandas, and then the globalfit model was used to fit the data for unwinding using the n-step unwinding model and translocation using a two-step dissociation model ( 64 ).
- Full pipeline: stage not stated [Conda, NumPy, Python, SciPy, emcee]

### The orbital eccentricity distribution of planets orbiting M dwarfs. (PNAS 2023)

- DOI: 10.1073/pnas.2217398120 | PMCID: PMC10265968 | PMID: 37252955
- Evidence: We use a Markov Chain Monte Carlo (MCMC) analysis with the Python package emcee ( 44 ).
- Full pipeline: simulation/modelling [emcee]

### Entropic control of the free-energy landscape of an archetypal biomolecular machine. (PNAS 2023)

- DOI: 10.1073/pnas.2220591120 | PMCID: PMC10214133 | PMID: 37186858
- Evidence: The posterior probability distribution for each RC dataset, defined here as the product of the above likelihood and prior distributions (assuming the evidence is a constant, since only a single model is used) ( 53 ), was sampled using an affine-invariant Markov chain Monte Carlo (MCMC) method, emcee ( 54 , 55 ).
- Full pipeline: simulation/modelling [emcee]

### A precise metallicity and carbon-to-oxygen ratio for a warm giant exoplanet from its panchromatic JWST emission spectrum. (PNAS 2025)

- DOI: 10.1073/pnas.2416193122 | PMCID: PMC12501160 | PMID: 40982673
- Evidence: To perform the MCMC runs, we used the emcee Python package ( 53 ) using 12 walkers with a 2,000-step burn-in and then a 4,000-step production run for each spectral channel.
- Full pipeline: quantification [dynesty] -> stage not stated [SciPy, emcee]

