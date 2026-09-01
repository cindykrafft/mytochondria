# Cartopy

- **Category:** physical
- **Papers in survey:** 6
- **Journals:** Nature (6)
- **Years:** 2021 (1), 2023 (1), 2024 (2), 2025 (2)
- **Versions named:** 0.20.3 (1)
- **Pipeline stages it appears in:** visualisation (1)

## Papers

### Skilful precipitation nowcasting using deep generative models of radar. (Nature 2021)

- DOI: 10.1038/s41586-021-03854-z | PMCID: PMC8481123 | PMID: 34588668
- Evidence: Maps produced with Cartopy and SRTM elevation data 46 .
- Full pipeline: stage not stated [Cartopy, TensorFlow]

### Tropical deforestation causes large reductions in observed precipitation. (Nature 2023)

- DOI: 10.1038/s41586-022-05690-1 | PMCID: PMC9995269 | PMID: 36859548
- Evidence: Maps of the different regions generated using Cartopy and Natural Earth 51 .
- Full pipeline: stage not stated [Cartopy, seaborn, xarray]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Version used: **0.20.3**
- Evidence: Map produced using Cartopy (v.0.20.3, https://github.com/SciTools/cartopy/tree/v0.20.3 ), Natural Earth ( naturalearthdata.com ) and World Shaded Relief map (Esri). b , Temporal distribution of n = 36 malaria-positive ancient individuals.
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Satellite mapping reveals extensive industrial activity at sea. (Nature 2024)

- DOI: 10.1038/s41586-023-06825-8 | PMCID: PMC10764273 | PMID: 38172362
- Evidence: All maps were generated using Python ( https://www.python.org ) with the open-source visualization libraries PySeas ( https://github.com/GlobalFishingWatch/pyseas ), Matplotlib ( https://matplotlib.org ) and Cartopy ( https://scitools.org.uk/cartopy ).
- Full pipeline: machine learning [scikit-learn] -> visualisation [Cartopy, Matplotlib]

### A foundation model for the Earth system. (Nature 2025)

- DOI: 10.1038/s41586-025-09005-y | PMCID: PMC12119322 | PMID: 40399684
- Evidence: All of our plots were made using Matplotlib 77 and the geographical maps were produced using Cartopy 78 .
- Full pipeline: differential/statistical testing [WRF] -> stage not stated [Cartopy, Matplotlib]

### Impact of Amazonian deforestation on precipitation reverses between seasons. (Nature 2025)

- DOI: 10.1038/s41586-024-08570-y | PMCID: PMC11882456 | PMID: 40044888
- Evidence: Geographic data, including coastlines and boundaries, were sourced from open-access datasets (Natural Earth: www.naturalearthdata.com ) available in the Cartopy library of Python.
- Full pipeline: stage not stated [CESM, Cartopy, Python, WRF]

