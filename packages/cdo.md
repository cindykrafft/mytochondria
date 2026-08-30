# CDO

- **Category:** physical
- **Papers in survey:** 5
- **Journals:** PNAS (5)
- **Years:** 2021 (2), 2022 (1), 2024 (1), 2025 (1)
- **Versions named:** 1.9.9r (1)

## Papers

### COVID-19 lockdowns drive decline in active fires in southeastern United States. (PNAS 2021)

- DOI: 10.1073/pnas.2105666118 | PMCID: PMC8639348 | PMID: 34663728
- Version used: **1.9.9r**
- Evidence: We used Climate Data Operators (1.9.9rc2) to carry out the calculation.
- Full pipeline: differential/statistical testing [R v3.6.0] -> stage not stated [CDO v1.9.9r]

### Temperature and population density influence SARS-CoV-2 transmission in the absence of nonpharmaceutical interventions. (PNAS 2021)

- DOI: 10.1073/pnas.2019284118 | PMCID: PMC8237566 | PMID: 34103391
- Evidence: We used the Climate Data Operators program ( 55 ) to compute daily means for each of our climate variables.
- Full pipeline: stage not stated [CDO]

### Evidence that Pacific tuna mercury levels are driven by marine methylmercury production and anthropogenic inputs. (PNAS 2022)

- DOI: 10.1073/pnas.2113032119 | PMCID: PMC8764691 | PMID: 34983875
- Evidence: All outputs on the NEMO curvilinear, tripolar grid were regridded onto a regular 1° × 1° horizontal grid prior to data extraction using the remap function in Climate Data Operators ( 66 ).
- Full pipeline: differential/statistical testing [R v3.6] -> stage not stated [CDO]

### Observed carbon decoupling of subnational production insufficient for net-zero goal by 2050. (PNAS 2024)

- DOI: 10.1073/pnas.2411419121 | PMCID: PMC11551423 | PMID: 39467137
- Evidence: We use the Climate Data Operators provided from the Max-Planch-Institute for Meteorology ( 47 ) and the shapefiles provided by the DOSE dataset ( 29 ) to aggregate the emissions data from grid cells to the respective subnational level described in the economic data section.
- Full pipeline: stage not stated [CDO]

### Eukaryotic phytoplankton drive a decrease in primary production in response to elevated CO&lt;sub&gt;2&lt;/sub&gt; in the tropical and subtropical oceans. (PNAS 2025)

- DOI: 10.1073/pnas.2423680122 | PMCID: PMC11929437 | PMID: 40063804
- Evidence: The products of the climatology Chl- a and the carbon-based primary production were corrected to the same resolution and calculated each grid cell area using Climate Data Operators (CDO, Version 2.3.0) ( 80 ).
- Full pipeline: quality control [DADA2, QIIME 2, R] -> stage not stated [CDO, vegan]

