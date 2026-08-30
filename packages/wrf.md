# WRF

- **Category:** physical
- **Papers in survey:** 16
- **Journals:** PNAS (13), Nature (3)
- **Years:** 2021 (1), 2022 (3), 2023 (1), 2024 (2), 2025 (9)
- **Versions named:** 4.3.1 (1)
- **Pipeline stages it appears in:** simulation/modelling (7), differential/statistical testing (1), normalisation (1), dimensionality reduction/clustering (1)

## Papers

### A foundation model for the Earth system. (Nature 2025)

- DOI: 10.1038/s41586-025-09005-y | PMCID: PMC12119322 | PMID: 40399684
- Evidence: These forecasts are produced by running various dynamical and statistical models, ranging from global ensembles such as the IFS to purpose-built tropical cyclone forecasting systems such as the Hurricane Weather Research and Forecasting model 35 .
- Full pipeline: differential/statistical testing [WRF] -> stage not stated [Cartopy, Matplotlib]

### Impact of Amazonian deforestation on precipitation reverses between seasons. (Nature 2025)

- DOI: 10.1038/s41586-024-08570-y | PMCID: PMC11882456 | PMID: 40044888
- Evidence: Methods Coupled land–atmosphere regional weather model The WRF model, developed by the National Center for Atmospheric Research 24 , is a fully coupled mesoscale model widely used for regional climate studies 4 , 26 , 51 .
- Full pipeline: stage not stated [CESM, Cartopy, Python, WRF]

### The Ronne Ice Shelf survived the last interglacial. (Nature 2025)

- DOI: 10.1038/s41586-024-08394-w | PMCID: PMC11798827 | PMID: 39880946
- Evidence: Water isotope modelling Estimates of the expected change in water isotopes across Antarctica owing to the atmospheric circulation changes associated with a reduced or collapsed WAIS are taken from a paper 32 that used the high-resolution Weather Research and Forecasting model with the addition of water isotope physics.
- Full pipeline: alignment/mapping [QGIS] -> stage not stated [WRF]

### Environmental drivers of annual population fluctuations in a trans-Saharan insect migrant. (PNAS 2021)

- DOI: 10.1073/pnas.2102762118 | PMCID: PMC8256005 | PMID: 34155114
- Evidence: The Weather Research and Forecasting (WRF) model (version 3.8, https://www.mmm.ucar.edu/wrf-model-general ) was used to produce a high-resolution atmospheric background for the trajectory calculations.
- Full pipeline: differential/statistical testing [lme4] -> simulation/modelling [WRF] -> stage not stated [R v3.5]

### Notable impact of wildfires in the western United States on weather hazards in the central United States. (PNAS 2022)

- DOI: 10.1073/pnas.2207329119 | PMCID: PMC9636965 | PMID: 36252100
- Evidence: To realistically simulate deep convective clouds and aerosols, we carried out high-resolution simulations by using the chemistry version of the Weather Research and Forecasting model (WRF-Chem) coupled with a spectral-bin microphysics scheme (SBM), which is a benchmark model for aerosol–cloud interaction studies ( 27 ).
- Full pipeline: simulation/modelling [WRF]

### A gap in nitrous oxide emission reporting complicates long-term climate mitigation. (PNAS 2022)

- DOI: 10.1073/pnas.2200354119 | PMCID: PMC9351463 | PMID: 35878021
- Evidence: ...x to minimize the differences between available atmospheric N 2 O observations and the prior flux convolved with an atmospheric transport matrix from Weather Research and Forecasting - Stochastic Time-Inverted Lagrangian Transport (WRF-STILT) ( 13 ).
- Full pipeline: stage not stated [WRF]

### Estimate of OH trends over one decade in North American cities. (PNAS 2022)

- DOI: 10.1073/pnas.2117399119 | PMCID: PMC9169711 | PMID: 35412909
- Evidence: We conduct a start-of-art chemical transport model simulation using Weather Research and Forecasting Model coupled with Chemistry (WRF-Chem) over North America.
- Full pipeline: simulation/modelling [WRF]

### Unveiling the underestimated direct emissions of nitrous acid (HONO). (PNAS 2023)

- DOI: 10.1073/pnas.2302048120 | PMCID: PMC10468620 | PMID: 37603738
- Evidence: The Weather Research and Forecasting model coupled with Chemistry (WRF-Chem) simulation revealed that incorporating direct HONO emissions led to a 1.5-fold increase in the average atmospheric HONO mixing ratio (in parts per billion by volume, ppbv) in the NCP.
- Full pipeline: simulation/modelling [WRF]

### Overlooked significance of iodic acid in new particle formation in the continental atmosphere. (PNAS 2024)

- DOI: 10.1073/pnas.2404595121 | PMCID: PMC11295062 | PMID: 39047040
- Evidence: Here, we investigate the role of IA in the process of SA–DMA nucleation from microscale mechanisms to macroscale impacts by combining quantum chemical calculations, atmospheric cluster dynamic simulations, and Weather Research and Forecasting model coupled with Chemistry (WRF-Chem) simulations.
- Full pipeline: dimensionality reduction/clustering [WRF] -> simulation/modelling [WRF]

### California's 2023 snow deluge: Contextualizing an extreme snow year against future climate change. (PNAS 2024)

- DOI: 10.1073/pnas.2320600121 | PMCID: PMC11098106 | PMID: 38684006
- Evidence: These bias-corrected GCMs were then used as forcing to the WRF model ( 73 ), run at a 9-km grid length across the western United States.
- Full pipeline: stage not stated [WRF]

### Strategy for coordinating near-term PM&lt;sub&gt;2.5&lt;/sub&gt;, ozone, and CO&lt;sub&gt;2&lt;/sub&gt; mitigation in China. (PNAS 2025)

- DOI: 10.1073/pnas.2513194122 | PMCID: PMC12646266 | PMID: 41213024
- Evidence: Validation against surface observation shows that our Weather Research and Forecasting Model (WRF)-CMAQ modeling system can reasonably capture the spatial-temporal patterns of PM 2.5 and O 3 concentrations over China ( SI Appendix , Table S5 ).
- Full pipeline: stage not stated [WRF]

### China's SO&lt;sub&gt;2&lt;/sub&gt; emission reductions enhance atmospheric ozone-driven sulfate aerosol production in East Asia. (PNAS 2025)

- DOI: 10.1073/pnas.2414064122 | PMCID: PMC12184437 | PMID: 40489614
- Evidence: To drive the CMAQ model, the meteorological fields were simulated using the Weather Research and Forecasting (WRF) model version 4.1.1 ( 47 ).
- Full pipeline: simulation/modelling [WRF]

### Prioritizing urban heat adaptation infrastructure based on multiple outcomes: Comfort, health, and energy. (PNAS 2025)

- DOI: 10.1073/pnas.2411144122 | PMCID: PMC12087966 | PMID: 40324090
- Evidence: The core of this methodology applies the Weather Research and Forecasting (WRF) mesoscale meteorological model with a state-of-the-art, multilayer urban canopy and building energy model BEP-BEM ( 42 – 44 ) to dynamically downscale outdoor climate, building energy use, and pollutant dispersion for contemporary and projected future extreme heat events.
- Full pipeline: stage not stated [CESM, WRF]

### Dynamical-generative downscaling of climate model ensembles. (PNAS 2025)

- DOI: 10.1073/pnas.2420288122 | PMCID: PMC12054837 | PMID: 40279391
- Evidence: The RCM used for dynamical downscaling is the Weather Research and Forecasting Model (WRF), in its version 4.1.3 ( 44 ).
- Full pipeline: normalisation [WRF]

### Advancing forecasting capabilities: A contrastive learning model for forecasting tropical cyclone rapid intensification. (PNAS 2025)

- DOI: 10.1073/pnas.2415501122 | PMCID: PMC11789009 | PMID: 39835899
- Evidence: Numerical models like the Hurricane Weather Research and Forecasting model (HWRF) have limited accuracy in RI TC forecasts.
- Full pipeline: stage not stated [Keras, TensorFlow, WRF]

### US Corn Belt enhances regional precipitation recycling. (PNAS 2025)

- DOI: 10.1073/pnas.2402656121 | PMCID: PMC11725895 | PMID: 39793051
- Version used: **4.3.1**
- Evidence: We conducted the high-resolution (4-km) coupled simulations using the Weather Research and Forecasting model (WRF, version 4.3.1; 17 ) with the Water Vapor Tracer (WVT; 23 ) scheme for three representative years, 2010 (wet year), 2011 (normal year), and 2012 (dry year), according to precipitation anomalies.
- Full pipeline: simulation/modelling [WRF v4.3.1]

