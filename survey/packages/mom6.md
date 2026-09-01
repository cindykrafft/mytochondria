# MOM6

- **Category:** physical
- **Papers in survey:** 17
- **Journals:** PNAS (14), Nature (3)
- **Years:** 2021 (3), 2022 (2), 2023 (3), 2024 (5), 2025 (3), 2026 (1)
- **Pipeline stages it appears in:** simulation/modelling (8), dimensionality reduction/clustering (2), machine learning (1)

## Papers

### A broadband thermal emission spectrum of the ultra-hot Jupiter WASP-18b. (Nature 2023)

- DOI: 10.1038/s41586-023-06230-1 | PMCID: PMC10412449 | PMID: 37257843
- Evidence: We use the SPARC/MITgcm 53 to model the 3D atmospheric structure of WASP-18b.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [emcee] -> stage not stated [MOM6, dynesty, scikit-image]

### Inhomogeneous terminators on the exoplanet WASP-39 b. (Nature 2024)

- DOI: 10.1038/s41586-024-07768-4 | PMCID: PMC11357994 | PMID: 39009005
- Evidence: We used one-dimensional (1D) pressure–temperature profiles as input, extracted from a cloud-free GCM simulation of WASP-39 b using ExpeRT/MITgcm 62 .
- Full pipeline: dimensionality reduction/clustering [MOM6] -> simulation/modelling [MOM6]

### Wide-swath satellite altimetry unveils global submesoscale ocean dynamics. (Nature 2025)

- DOI: 10.1038/s41586-025-08722-8 | PMCID: PMC12003163 | PMID: 40240853
- Evidence: Simulated SSH data from the MITgcm LLC4320 data are available at 10.5067/KARIN-2MES1.
- Full pipeline: simulation/modelling [MOM6] -> stage not stated [Matplotlib]

### Plastic waste release caused by COVID-19 and its fate in the global ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2111530118 | PMCID: PMC8617455 | PMID: 34751160
- Evidence: We simulate the transport and fate of the 25,900 ± 3,800 tons of pandemic-associated plastic waste by the Nanjing University MITgcm-Plastic model (NJU-MP) to evaluate its impact on the marine environment.
- Full pipeline: simulation/modelling [MOM6]

### On the effects of the ocean on atmospheric CFC-11 lifetimes and emissions. (PNAS 2021)

- DOI: 10.1073/pnas.2021528118 | PMCID: PMC8000270 | PMID: 33723065
- Evidence: MITgcm Model.
- Full pipeline: stage not stated [MOM6]

### Ocean melting of the Zachariae Isstrøm and Nioghalvfjerdsfjorden glaciers, northeast Greenland. (PNAS 2021)

- DOI: 10.1073/pnas.2015483118 | PMCID: PMC7812800 | PMID: 33372140
- Evidence: Grounded ice undercutting, q m , is calculated based on high-resolution (1 m), three-dimensional simulations of a melt plume using the MITgcm ocean model with varying water depth, b , subglacial discharge, q s g , and thermal forcing, T F , as q m = (0.0003 b q s g 0.33 + 0.15) T F 1.18 ( 19 ).
- Full pipeline: dimensionality reduction/clustering [MOM6] -> simulation/modelling [MOM6]

### A nutrient relay sustains subtropical ocean productivity. (PNAS 2022)

- DOI: 10.1073/pnas.2206504119 | PMCID: PMC9565266 | PMID: 36191202
- Evidence: 49 , which includes the global ocean circulation based on the Massachusetts Institute of Technology general circulation model (MITgcm) ( 50 ), coupled to the Darwin biogeochemical and ecological model ( 51 – 54 ).
- Full pipeline: stage not stated [MOM6]

### Trophic interactions with heterotrophic bacteria limit the range of &lt;i&gt;Prochlorococcus&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2110993118 | PMCID: PMC8764666 | PMID: 34983874
- Evidence: The biogeochemical and biological tracers are transported and mixed by the Massachusetts Institute of Technology (MIT) general circulation model (MITgcm) ( 71 ), constrained to be consistent with altimetric and hydrographic observations ( 72 ).
- Full pipeline: machine learning [MOM6]

### Ice and ocean constraints on early human migrations into North America along the Pacific coast. (PNAS 2023)

- DOI: 10.1073/pnas.2208738120 | PMCID: PMC9963817 | PMID: 36745804
- Evidence: Numerical model simulations were performed using the Massachusetts Institute of Technology General Circulation Model (MITgcm) ( 88 ) for the high-resolution ocean current simulations ( Fig.
- Full pipeline: simulation/modelling [MOM6]

### Climate-driven changes of global marine mercury cycles in 2100. (PNAS 2023)

- DOI: 10.1073/pnas.2202488120 | PMCID: PMC9926249 | PMID: 36595667
- Evidence: Methods MITgcm-Hg.
- Full pipeline: stage not stated [MOM6]

### Unexpected anthropogenic emission decreases explain recent atmospheric mercury concentration declines. (PNAS 2024)

- DOI: 10.1073/pnas.2401950121 | PMCID: PMC11494326 | PMID: 39378086
- Evidence: Legacy reemissions of Hg from the ocean are calculated online (depending on temperature and wind speed) through an air–sea exchange parametrization ( 83 ), with concentrations of Hg in the surface ocean taken from a previous ocean general circulation model (MITgcm) simulation ( 42 ).
- Full pipeline: simulation/modelling [MOM6] -> stage not stated [R, lme4]

### Global fishing patterns amplify human exposures to methylmercury. (PNAS 2024)

- DOI: 10.1073/pnas.2405898121 | PMCID: PMC11459155 | PMID: 39312660
- Evidence: Seawater MeHg concentrations were from prior work using the Massachusetts Institute of Technology general circulation model (MITgcm) ( 19 ).
- Full pipeline: stage not stated [MOM6]

### On the role of seamounts in upwelling deep-ocean waters through turbulent mixing. (PNAS 2024)

- DOI: 10.1073/pnas.2322163121 | PMCID: PMC11228523 | PMID: 38917014
- Evidence: Average flow speeds at the mid-heights of seamounts in the KW11 census are calculated from the LLC4320 model, a global, full-depth ocean and sea ice simulation carried out using the Massachusetts Institute of Technology general circulation model (MITgcm).
- Full pipeline: simulation/modelling [MOM6]

### The effect of reef morphology on coral recruitment at multiple spatial scales. (PNAS 2024)

- DOI: 10.1073/pnas.2311661121 | PMCID: PMC10823213 | PMID: 38190515
- Evidence: We then displaced larvae via advection and random diffusion starting on expected spawning dates ( SI Appendix , Table S1 ) using a regional nest of the Massachusetts Institute of Technology general circulation model [MITgcm; ( 21 )].
- Full pipeline: read trimming [R] -> stage not stated [MOM6]

### Contrasting melt regime in the Ice Grounding Zone of Thwaites Glacier, West Antarctica. (PNAS 2025)

- DOI: 10.1073/pnas.2512626122 | PMCID: PMC12685041 | PMID: 41248314
- Evidence: The MITgcm ocean model is a finite-volume method that solves the Boussinesq hydrostatic form of the Navier–Stokes equations on an Arakawa C-grid for an incompressible fluid ( 45 ).
- Full pipeline: stage not stated [MOM6]

### A universal wind-wave-bubble formulation for air-sea gas exchange and its impact on oxygen fluxes. (PNAS 2025)

- DOI: 10.1073/pnas.2419319122 | PMCID: PMC12478149 | PMID: 40956887
- Evidence: We use the ocean circulation model from the Geophysical Fluid Dynamics Laboratory (GFDL) ( 8 ) global ocean model (Modular Ocean Model, MOM6) ( 56 ) coupled with sea ice and biogeochemistry (COBALTv2) ( 9 ).
- Full pipeline: stage not stated [MOM6]

### Large declines in organofluorine contamination indicated by subarctic marine mammal tissues. (PNAS 2026)

- DOI: 10.1073/pnas.2524513123 | PMCID: PMC12867700 | PMID: 41587316
- Evidence: Seawater C8 PFSA (PFOS) concentrations were simulated in the North Atlantic Ocean using the MITgcm general circulation model, following an adaptation of the model developed by Zhang et al.
- Full pipeline: differential/statistical testing [R v4.2.2] -> simulation/modelling [MOM6]

