# QGIS

- **Category:** physical
- **Papers in survey:** 67
- **Journals:** PNAS (42), Nature (25)
- **Years:** 2021 (5), 2022 (13), 2023 (18), 2024 (10), 2025 (14), 2026 (7)
- **Versions named:** 3.16 (3), 3.22 (2), 3.18 (2), 3.14 (2), 3.28.6 (1), 3.40 (1), 3.40.6 (1), 3.32.3 (1), 3.30 (1), 3.12.263 (1)
- **Pipeline stages it appears in:** alignment/mapping (6), visualisation (5), differential/statistical testing (5), machine learning (2), dimensionality reduction/clustering (2), simulation/modelling (1), quantification (1)

## Papers

### Dairying enabled Early Bronze Age Yamnaya steppe expansions. (Nature 2021)

- DOI: 10.1038/s41586-021-03798-4 | PMCID: PMC8550948 | PMID: 34526723
- Version used: **3.12**
- Evidence: Base maps were created using QGIS 3.12 ( https://qgis.org/en/site/ ), and use Natural Earth vector map data from https://www.naturalearthdata.com/downloads/ .
- Full pipeline: stage not stated [QGIS v3.12]

### Genome of a middle Holocene hunter-gatherer from Wallacea. (Nature 2021)

- DOI: 10.1038/s41586-021-03823-6 | PMCID: PMC8387238 | PMID: 34433944
- Evidence: 1a, b were created in ArcGIS (QGIS) from Shuttle Radar Topography Mission (SRTM 1) Arc-Second Global data courtesy of the US Geological Survey.
- Full pipeline: read trimming [BWA, SAMtools v1.3] -> alignment/mapping [BWA] -> variant calling [SAMtools v1.3] -> differential/statistical testing [ggplot2 v3.3.3] -> visualisation [ggplot2 v3.3.3] -> stage not stated [PLINK v1.9, QGIS]

### Global hotspots of salt marsh change and carbon emissions. (Nature 2022)

- DOI: 10.1038/s41586-022-05355-z | PMCID: PMC9771810 | PMID: 36450979
- Version used: **3.12.263**
- Evidence: We imported the processed HURDAT2 data as a delimited text layer into QGIS 3.12.263, creating a buffer surrounding each point based on the hurricane diameter 77 .
- Full pipeline: stage not stated [Python v3.8.10, QGIS v3.12.263, R v3.6, ggplot2, tidyverse]

### Social capital I: measurement and associations with economic mobility. (Nature 2022)

- DOI: 10.1038/s41586-022-04996-4 | PMCID: PMC9352590 | PMID: 35915342
- Evidence: Maps were made with the QGIS software package.
- Full pipeline: stage not stated [QGIS]

### Post-extinction recovery of the Phanerozoic oceans and biodiversity hotspots. (Nature 2022)

- DOI: 10.1038/s41586-022-04932-6 | PMCID: PMC9300466 | PMID: 35831505
- Version used: **3.22.0**
- Evidence: Finally, we spatially overlap the hexagons and 0.5° × 0.5° square grid to match the map of the palaeo analysis and extract the value of the diversity index per coastal grid in QGIS v.3.22.0.
- Full pipeline: stage not stated [QGIS v3.22.0]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Version used: **3.22.1**
- Evidence: The map was created using QGIS v.3.22.1 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Native diversity buffers against severity of non-native tree invasions. (Nature 2023)

- DOI: 10.1038/s41586-023-06440-7 | PMCID: PMC10533391 | PMID: 37612513
- Evidence: 3.9.7), Google Earth Engine (earthengine-api 0.1.306), QGIS-LTR (v.
- Full pipeline: visualisation [ggplot2, lme4] -> stage not stated [QGIS, R, tidyverse]

### Extensive pedigrees reveal the social organization of a Neolithic community. (Nature 2023)

- DOI: 10.1038/s41586-023-06350-8 | PMCID: PMC10432279 | PMID: 37495691
- Version used: **3.30**
- Evidence: 1 was created using the Free and Open Source QGIS (v3.30) under the Sharealike license ( https://creativecommons.org/licenses/by-sa/3.0/ ).
- Full pipeline: quality control [ANGSD] -> read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [QGIS v3.30]

### Rift-induced disruption of cratonic keels drives kimberlite volcanism. (Nature 2023)

- DOI: 10.1038/s41586-023-06193-3 | PMCID: PMC10727985 | PMID: 37495695
- Version used: **3.16**
- Evidence: We performed this analysis using open-source GIS software QGIS (v.
- Full pipeline: stage not stated [QGIS v3.16, R]

### Northwest African Neolithic initiated by migrants from Iberia and Levant. (Nature 2023)

- DOI: 10.1038/s41586-023-06166-6 | PMCID: PMC10266975 | PMID: 37286608
- Evidence: The map was generated using the open source QGIS Geographic Information System, http://qgis.osgeo.org . b , Chronological representation of the investigated archaeological time periods of northwestern Africa, with each site’s radiocarbon-dated timeline indicated. c , Enlarged view of a PCA plot (Supplementary Fig.
- Full pipeline: variant calling [GATK v3.5.0] -> registration [GATK v3.5.0] -> dimensionality reduction/clustering [ADMIXTURE, QGIS] -> stage not stated [BCFtools, PLINK v1.9, SAMtools]

### Suppressed basal melting in the eastern Thwaites Glacier grounding zone. (Nature 2023)

- DOI: 10.1038/s41586-022-05586-0 | PMCID: PMC9931584 | PMID: 36792735
- Evidence: Figure 1 was created with the QGIS Geographic Information System.
- Full pipeline: stage not stated [QGIS]

### Less extreme and earlier outbursts of ice-dammed lakes since 1900. (Nature 2023)

- DOI: 10.1038/s41586-022-05642-9 | PMCID: PMC9946834 | PMID: 36792828
- Evidence: Hence, we manually digitized the extents of the lakes from satellite images in QGIS V3.16 software.
- Full pipeline: differential/statistical testing [Stan, brms] -> stage not stated [QGIS]

### Heterogeneous melting near the Thwaites Glacier grounding line. (Nature 2023)

- DOI: 10.1038/s41586-022-05691-0 | PMCID: PMC9931587 | PMID: 36792738
- Evidence: 12 ) demonstrate notable GL retreat over the past two decades (QGIS map: Landsat 8, 15 m pixel −1 , band 8 image LC08_L1GT_003113_20200131_20200211_01_T2_B8, 31 January 2020; the red box denotes the study region). b , c , Warm water is delivered close to the ice base (upper grey regions), shown by contours of thermal driving (degrees above in situ freezing point).
- Full pipeline: stage not stated [QGIS]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **3.32.3**
- Evidence: 6b were generated using QGIS (v3.32.3).
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Coevolution of craton margins and interiors during continental break-up. (Nature 2024)

- DOI: 10.1038/s41586-024-07717-1 | PMCID: PMC11306106 | PMID: 39112622
- Version used: **3.16**
- Evidence: To achieve this, we use the open-source geographic information system applications QGIS (v3.16; https://www.qgis.org/ ) and GRASS ( https://grass.osgeo.org/ ).
- Full pipeline: stage not stated [QGIS v3.16, R]

### Homo sapiens reached the higher latitudes of Europe by 45,000 years ago. (Nature 2024)

- DOI: 10.1038/s41586-023-06923-7 | PMCID: PMC10849966 | PMID: 38297117
- Evidence: The map was created in QGIS 39 on the basis of Shuttle Radar Topography Mission data V4 ( http://srtm.csi.cgiar.org ) 40 . c , d , Blade fragments (16/116-159048 and 16/116-151453), layer 8. e , Quartzite flake (16/116-159051) from surface retouch, layer 8. f , Jerzmanowice blade point, layer X (Museum Burg Ranis, IV 1328). g , Bifacial leaf point (Museum Burg Ranis IV 1319), layer X. a , Adapted ...
- Full pipeline: alignment/mapping [BWA] -> registration [MAFFT v7.453] -> structure determination [MAFFT v7.453] -> stage not stated [BEAST v2.6.6, QGIS, R v4.1, SAMtools]

### Healthy forests safeguard traditional wild meat food systems in Amazonia. (Nature 2025)

- DOI: 10.1038/s41586-025-09743-z | PMCID: PMC12711560 | PMID: 41299169
- Evidence: Maps were produced in QGIS ( https://qgis.org/en/site/ ), with the final edition in Inkscape ( https://inkscape.org ) and GIMP ( https://www.gimp.org ).
- Full pipeline: stage not stated [QGIS]

### Global hotspots of mycorrhizal fungal richness are poorly protected. (Nature 2025)

- DOI: 10.1038/s41586-025-09277-4 | PMCID: PMC12422971 | PMID: 40702191
- Version used: **3.40**
- Evidence: We created 1-km 2 resolution sampling intensity layers for the SSU and ITS training datasets using kernel density interpolation from sample coordinates with a 5° radius and uniform decay rate in QGIS (v.3.40).
- Full pipeline: machine learning [QGIS v3.40] -> stage not stated [R]

### Ancient DNA reveals the prehistory of the Uralic and Yeniseian peoples. (Nature 2025)

- DOI: 10.1038/s41586-025-09189-3 | PMCID: PMC12342343 | PMID: 40604287
- Version used: **3.40.6**
- Evidence: All maps in the main text and in the Supplementary Information were created using ArcGIS 10.6.1 and QGIS 3.40.6.
- Full pipeline: variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [ANGSD v0.923, QGIS v3.40.6, R]

### Major expansion in the human niche preceded out of Africa dispersal. (Nature 2025)

- DOI: 10.1038/s41586-025-09154-0 | PMCID: PMC12328235 | PMID: 40533559
- Version used: **3.22**
- Evidence: 1 was originally developed on QGIS 3.22 Białowieża with WGS 84 projection.
- Full pipeline: stage not stated [CESM, QGIS v3.22, R]

### The Ronne Ice Shelf survived the last interglacial. (Nature 2025)

- DOI: 10.1038/s41586-024-08394-w | PMCID: PMC11798827 | PMID: 39880946
- Evidence: Maps in a and b were generated using QGIS with the Quantarctica mapping environment 43 , under a Creative Commons licence CC BY 4.0 .
- Full pipeline: alignment/mapping [QGIS] -> stage not stated [WRF]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Evidence: C. cor and human population distribution data in Kenya GPS points from all the study areas in Kenya where bats were surveyed were uploaded onto QGIS (2025, https://www.qgis.org ).
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### Observing the tidal pulse of rivers from wide-swath satellite altimetry. (Nature 2026)

- DOI: 10.1038/s41586-026-10287-z | PMCID: PMC13061602 | PMID: 41851459
- Evidence: Figures were plotted with QGIS and Matplotlib.
- Full pipeline: visualisation [Matplotlib, QGIS] -> stage not stated [Python]

### Sea level much higher than assumed in most coastal hazard assessments. (Nature 2026)

- DOI: 10.1038/s41586-026-10196-1 | PMCID: PMC13083249 | PMID: 41781624
- Version used: **3.28.6**
- Evidence: The results were visualized using QGIS v.3.28.6 and shapefiles from ref.
- Full pipeline: visualisation [QGIS v3.28.6] -> stage not stated [VMD]

### Protected area management has significant spillover effects on vegetation. (Nature 2026)

- DOI: 10.1038/s41586-025-09837-8 | PMCID: PMC12916312 | PMID: 41372406
- Evidence: To create sampling points, I first used the ‘random points in polygons’ command in QGIS (not to be confused with the ‘inside polygons’ command) with the option of 50 points per polygon and a minimum spacing of 300 m to generate random points inside each of the CAPAD polygons.
- Full pipeline: stage not stated [QGIS, R, vegan]

### Global and country-level estimates of human population at high altitude. (PNAS 2021)

- DOI: 10.1073/pnas.2102463118 | PMCID: PMC8106311 | PMID: 33903258
- Version used: **3.4.0**
- Evidence: Materials and Methods Population estimates were calculated using QGIS 3.4.0-Madeira software.
- Full pipeline: stage not stated [QGIS v3.4.0]

### Declining greenness in Arctic-boreal lakes. (PNAS 2021)

- DOI: 10.1073/pnas.2021219118 | PMCID: PMC8053985 | PMID: 33876758
- Evidence: Satellite remote sensing analyses were performed in Google Earth Engine ( 125 ); statistics were calculated in Python ( 126 ) using a suite of packages and spatial joins were conducted in QGIS ( 127 ).
- Full pipeline: differential/statistical testing [Python, QGIS] -> stage not stated [SciPy]

### Higher airborne pollen concentrations correlated with increased SARS-CoV-2 infection rates, as evidenced from 31 countries across the globe. (PNAS 2021)

- DOI: 10.1073/pnas.2019034118 | PMCID: PMC7999946 | PMID: 33798095
- Version used: **2.4.0**
- Evidence: Maps were created per occasion using QGIS 2.4.0 ( https://qgis.org/en/site ).
- Full pipeline: stage not stated [QGIS v2.4.0, R]

### Sea ice fluctuations in the Baffin Bay and the Labrador Sea during glacial abrupt climate changes. (PNAS 2022)

- DOI: 10.1073/pnas.2203468119 | PMCID: PMC9636944 | PMID: 36279448
- Version used: **3.10.10**
- Evidence: The map was produced with QGIS ( v3.10.10 ).
- Full pipeline: stage not stated [QGIS v3.10.10]

### Bending the curve: Simple but massive conservation action leads to landscape-scale recovery of amphibians. (PNAS 2022)

- DOI: 10.1073/pnas.2123070119 | PMCID: PMC9586276 | PMID: 36215493
- Version used: **3.16**
- Evidence: The surroundings of each site were characterized by the percent area of forest within a circular buffer of radius 100 m and the area of large (width ≥6 m) roads within a circular buffer of radius 1 km, extracted from the swissTLM3D vector data (swissTLM3D, SwissTopo [5704000000]) in QGIS v.3.16 ( https://qgis.org/en/site/ ).
- Full pipeline: stage not stated [JAGS, QGIS v3.16, R v4.0.3]

### Rats and the city: Implications of urbanization on zoonotic disease risk in Southeast Asia. (PNAS 2022)

- DOI: 10.1073/pnas.2112341119 | PMCID: PMC9522346 | PMID: 36122224
- Version used: **3.2.3**
- Evidence: We used the Semi-Automatic Classification Plugin v6.2.9 in QGIS v3.2.3 to transform the digital numbers for LANDSAT 8 data into reflectance values ( 51 , 52 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8] -> stage not stated [QGIS v3.2.3, R, igraph]

### Male mastodon landscape use changed with maturation (late Pleistocene, North America). (PNAS 2022)

- DOI: 10.1073/pnas.2118329119 | PMCID: PMC9231495 | PMID: 35696566
- Version used: **3.4**
- Evidence: All analyses and modeling were scripted in R version 3.5.1 ( 61 ) and QGIS version 3.4.
- Full pipeline: stage not stated [QGIS v3.4, R v3.5.1]

### Accelerating ethics, empathy, and equity in geographic information science. (PNAS 2022)

- DOI: 10.1073/pnas.2119967119 | PMCID: PMC9171629 | PMID: 35507875
- Evidence: 114 ), and in response communities developed packages like QGIS ( 115 ) and R spatial ( 116 ).
- Full pipeline: stage not stated [QGIS]

### Land management explains major trends in forest structure and composition over the last millennium in California's Klamath Mountains. (PNAS 2022)

- DOI: 10.1073/pnas.2116264119 | PMCID: PMC8944927 | PMID: 35286202
- Version used: **3.14**
- Evidence: In QGIS version 3.14 ( 79 ), lake boundaries ( 80 ) and harvest records ( 42 ) were obtained and plotted.
- Full pipeline: visualisation [QGIS v3.14, R]

### Discovering disease-causing pathogens in resource-scarce Southeast Asia using a global metagenomic pathogen monitoring system. (PNAS 2022)

- DOI: 10.1073/pnas.2115285119 | PMCID: PMC8931249 | PMID: 35238677
- Version used: **3.16.5**
- Evidence: To summarize and quantify land-cover types, we created 1-km buffers around the geographic coordinates for participant villages and extracted land cover characteristics for each participant using the Zonal Histogram function in QGIS (v3.16.5: https://qgis.org ).
- Full pipeline: quantification [QGIS v3.16.5]

### Diverse methylotrophic methanogenic archaea cause high methane emissions from seagrass meadows. (PNAS 2022)

- DOI: 10.1073/pnas.2106628119 | PMCID: PMC8892325 | PMID: 35165204
- Evidence: ( 38 ) using the quantum geographic information system (QGIS; version 3.14).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [MAFFT] -> stage not stated [HMMER, IQ-TREE, QGIS, SPAdes]

### Multiple spillovers from humans and onward transmission of SARS-CoV-2 in white-tailed deer. (PNAS 2022)

- DOI: 10.1073/pnas.2121644119 | PMCID: PMC8833191 | PMID: 35078920
- Evidence: QGIS (geographic information system) mapping software version 3.16.10 was used to visually portray the geographic location of the white-tailed deer sampled ( 54 ).
- Full pipeline: read trimming [SAMtools v1.11] -> alignment/mapping [QGIS, RAxML] -> variant calling [SAMtools v1.11] -> stage not stated [Pangolin v3.1.11]

### Frugivore-mediated seed dispersal in fragmented landscapes: Compositional and functional turnover from forest to matrix. (PNAS 2023)

- DOI: 10.1073/pnas.2302440120 | PMCID: PMC10622928 | PMID: 37871198
- Version used: **3.26.1**
- Evidence: ... natural and artificial perching sites for birds) in the surrounding agricultural matrix ( n = 20 to 34 in each landscape); landscape map produced in QGIS v.3.26.1 (QGIS Development Team 2022) by digitizing satellite images.
- Full pipeline: stage not stated [QGIS v3.26.1, R, emmeans v1.7.3]

### The impact of farming on prehistoric culinary practices throughout Northern Europe. (PNAS 2023)

- DOI: 10.1073/pnas.2310138120 | PMCID: PMC10614617 | PMID: 37844237
- Version used: **3.28.2**
- Evidence: Mapping was undertaken with QGIS (version 3.28.2-Firenze) using Natural Earth.
- Full pipeline: alignment/mapping [QGIS v3.28.2]

### Avoiding an unjust transition to sustainability: An equity metric for spatial conservation planning. (PNAS 2023)

- DOI: 10.1073/pnas.2216693120 | PMCID: PMC10614950 | PMID: 37844239
- Evidence: We used R software ( 91 ) for data processing, statistical tests, and the creation of plots, and we used QGIS ( 92 ) for partitioning data into regions, obtaining population and calorie counts, and creating maps.
- Full pipeline: differential/statistical testing [QGIS]

### The global biogeography and environmental drivers of fairy circles. (PNAS 2023)

- DOI: 10.1073/pnas.2304032120 | PMCID: PMC10556617 | PMID: 37748063
- Version used: **3.14**
- Evidence: The perimeter of each FC was drawn, and we calculated the area (in m 2 ) of each FC with a Geographic Information System (QGIS, v.3.14 QGIS Development Team, 2021) ( 74 ).
- Full pipeline: stage not stated [QGIS v3.14, R]

### Reductions in home-range size and social interactions among dehorned black rhinoceroses (<i>Diceros bicornis</i>). (PNAS 2023)

- DOI: 10.1073/pnas.2301727120 | PMCID: PMC10288626 | PMID: 37307460
- Evidence: Reserve boundary shapefiles were projected in QGIS and intersected with location data to exclude incorrect GPS coordinates.
- Full pipeline: stage not stated [QGIS, igraph]

### Ecological barriers mediate spatiotemporal shifts of bird communities at a continental scale. (PNAS 2023)

- DOI: 10.1073/pnas.2213330120 | PMCID: PMC10266007 | PMID: 37252949
- Evidence: For all data processing and statistical analyses, we used QGIS ( 59 ) and R software (version 4.2.0 vigorous calisthenics; 60 ).
- Full pipeline: differential/statistical testing [QGIS] -> stage not stated [R]

### The effect of climate change on avian offspring production: A global meta-analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2208389120 | PMCID: PMC10175715 | PMID: 37126701
- Evidence: 51 using QGIS software (version 3.22.11).
- Full pipeline: stage not stated [QGIS, R v4.2.2, metafor]

### White-tailed deer (<i>Odocoileus virginianus</i>) may serve as a wildlife reservoir for nearly extinct SARS-CoV-2 variants of concern. (PNAS 2023)

- DOI: 10.1073/pnas.2215067120 | PMCID: PMC9963525 | PMID: 36719912
- Evidence: The spatial clusters were visualized in QGIS (geographic information system) mapping software version 3.16.16 ( 43 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.453, QGIS] -> dimensionality reduction/clustering [QGIS] -> visualisation [IQ-TREE, QGIS] -> stage not stated [Nextstrain, Pangolin v4.0.6]

### Three decades of increasing fish biodiversity across the northeast Atlantic and the Arctic Ocean. (PNAS 2023)

- DOI: 10.1073/pnas.2120869120 | PMCID: PMC9942854 | PMID: 36656855
- Evidence: The shapefiles for the ocean and land were obtained from the Marine Regions database ( 56 ) and maps were created using QGIS software ( 57 ).
- Full pipeline: stage not stated [QGIS, R]

### Isotopic and DNA analyses reveal multiscale PPNB mobility and migration across Southeastern Anatolia and the Southern Levant. (PNAS 2023)

- DOI: 10.1073/pnas.2210611120 | PMCID: PMC9942848 | PMID: 36649412
- Version used: **3.16.6**
- Evidence: Statistical analysis was carried out using JMP 11.0 and R 3.63; map illustration was carried out with QGIS 3.16.6.
- Full pipeline: differential/statistical testing [QGIS v3.16.6, R v3.63]

### Mapping the connectivity-conflict interface to inform conservation. (PNAS 2023)

- DOI: 10.1073/pnas.2211482119 | PMCID: PMC9910505 | PMID: 36574696
- Evidence: We used Quantum Geographic Information System (QGIS) v.
- Full pipeline: stage not stated [QGIS, R]

### Principal role of fungi in soil carbon stabilization during early pedogenesis in the high Arctic. (PNAS 2024)

- DOI: 10.1073/pnas.2402689121 | PMCID: PMC11252988 | PMID: 38954550
- Version used: **3.18**
- Evidence: 1 A ) was created using QGIS 3.18 and published estimates of soil age ( 77 ), according to geographical data from the Norwegian Polar Institute.
- Full pipeline: differential/statistical testing [R v4.3.1] -> stage not stated [BLAST, QGIS v3.18]

### Private management of African protected areas improves wildlife and tourism outcomes but with security concerns in conflict regions. (PNAS 2024)

- DOI: 10.1073/pnas.2401814121 | PMCID: PMC11260162 | PMID: 38950358
- Evidence: First, we used Quantum Geographic Information System (QGIS) to manually select all polygons from each of the World Database of Protected Areas’ (WDPA) shapefiles that overlapped with the boundaries of AP’s anchor areas.
- Full pipeline: stage not stated [QGIS, R]

### The length and spacing of river tributaries. (PNAS 2024)

- DOI: 10.1073/pnas.2313899121 | PMCID: PMC11009638 | PMID: 38573963
- Evidence: 10 ), by converting the LSDTopoTools-generated basin outlines polygons to points in QGIS and summing the distance between points ( 47 ).
- Full pipeline: stage not stated [QGIS]

### The dawn of the tropical Atlantic invasion into the Mediterranean Sea. (PNAS 2024)

- DOI: 10.1073/pnas.2320687121 | PMCID: PMC11009679 | PMID: 38557179
- Evidence: We downloaded GBIF modern occurrence data for them and cleaned occurrences manually in QGIS by removing unlikely records, including those on land or clearly outside a species known range.
- Full pipeline: differential/statistical testing [R] -> simulation/modelling [CESM] -> stage not stated [QGIS]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Evidence: The remaining points were manually curated in QGIS ( https://docs.qgis.org/3.22/en/docs/user_manual/index.html ).
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### Mechanistic links between physiology and spectral reflectance enable previsual detection of oak wilt and drought stress. (PNAS 2024)

- DOI: 10.1073/pnas.2316164121 | PMCID: PMC10873599 | PMID: 38315867
- Evidence: We used QGIS ( 60 ) and the RGB images of the UAV to manually trace canopies of each tree avoiding empty spaces in each flight date and convert them to polygons.
- Full pipeline: normalisation [R v3.5] -> stage not stated [ImageJ, QGIS]

### A recent gibbon ape leukemia virus germline integration in a rodent from New Guinea. (PNAS 2024)

- DOI: 10.1073/pnas.2220392121 | PMCID: PMC10861895 | PMID: 38305758
- Version used: **3.16.10**
- Evidence: Map created using the free and open source QGIS version 3.16.10-Hannover.
- Full pipeline: read trimming [Cutadapt v1.15, Picard v1.4, Trimmomatic v0.27] -> alignment/mapping [PyMOL v2.4] -> differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7] -> stage not stated [QGIS v3.16.10, RAxML v8.2.11]

### A speleothem record from the Fertile Crescent covering the last deglaciation better contextualizes neolithization. (PNAS 2025)

- DOI: 10.1073/pnas.2502092122 | PMCID: PMC12718302 | PMID: 41325542
- Version used: **3.34.11**
- Evidence: The maps were designed using QGIS 3.34.11; plugin https://nextgis.com/blog/quickmapservices/ .
- Full pipeline: simulation/modelling [CESM v1.3] -> stage not stated [QGIS v3.34.11]

### Causes and consequences of disordered hyperuniformity in global drylands. (PNAS 2025)

- DOI: 10.1073/pnas.2504496122 | PMCID: PMC12541334 | PMID: 41055984
- Version used: **3.18**
- Evidence: The image analyses were conducted in QGIS 3.18 and MATLAB 2021a.
- Full pipeline: stage not stated [QGIS v3.18]

### Landscape changes elevate the risk of avian influenza virus diversification and emergence in the East Asian-Australasian Flyway. (PNAS 2025)

- DOI: 10.1073/pnas.2503427122 | PMCID: PMC12403075 | PMID: 40825116
- Version used: **3.22**
- Evidence: In this study, the remote sensing data were processed in an open-source geographic information system (QGIS version 3.22) ( 78 ), the IBM was built and simulated in an agent-based modeling platform (NetLogo version 6.1.1) ( 71 ), and the data were processed and analyzed with a statistical language (R version 4.4.1) ( 79 ).
- Full pipeline: differential/statistical testing [QGIS v3.22, R v4.4.1] -> simulation/modelling [QGIS v3.22, R v4.4.1]

### Indigenous territories and protected areas are crucial for ecosystem connectivity in the Amazon basin. (PNAS 2025)

- DOI: 10.1073/pnas.2418189122 | PMCID: PMC12337320 | PMID: 40720645
- Evidence: Maps were produced with QGIS software ( 115 ).
- Full pipeline: visualisation [ggplot2 v3.5.1, tidyverse v1.3.1] -> stage not stated [QGIS, emmeans, lme4]

### The importance of small-island populations for the long-term survival of endangered large-bodied insular mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422690122 | PMCID: PMC12232422 | PMID: 40553499
- Evidence: Ensemble distribution models ( 21 ) were generated and analyzed in R ( 34 ) and QGIS ( 35 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [ANGSD, QGIS, R, VEP]

### Resilience of deep aquifer microbial communities to seasonal hydrological fluctuations. (PNAS 2025)

- DOI: 10.1073/pnas.2422608122 | PMCID: PMC12167999 | PMID: 40478876
- Version used: **3.32.0**
- Evidence: Maps were generated by QGIS (v3.32.0).
- Full pipeline: stage not stated [QGIS v3.32.0]

### Unbalanced social-ecological acceleration led to state formation failure in early medieval Poland. (PNAS 2025)

- DOI: 10.1073/pnas.2409056122 | PMCID: PMC12067273 | PMID: 40258139
- Evidence: For plotting the resulting graphs on maps, the QGIS Geographic Information System, version: 3.4.5-Madeira ( 78 ) and the mapping resources the Environmental Systems Research Institute have been used.
- Full pipeline: alignment/mapping [QGIS]

### Kuznets' tides: An archaeological perspective on the long-term dynamics of sustainable development. (PNAS 2025)

- DOI: 10.1073/pnas.2400603121 | PMCID: PMC12037042 | PMID: 40228132
- Version used: **3.32**
- Evidence: The map was prepared using QGIS 3.32 and a basemap from naturalearth.com projected using the Eckert IV coordinate reference system.
- Full pipeline: stage not stated [QGIS v3.32]

### Urban highways are barriers to social ties. (PNAS 2025)

- DOI: 10.1073/pnas.2408937122 | PMCID: PMC11912457 | PMID: 40035764
- Evidence: The network geometries are further simplified with OSMnx, and for the case studies, manually in the open-source geographic information system (GIS) software QGIS (see SI Appendix , section C for details on OSM queries and simplification).
- Full pipeline: stage not stated [QGIS]

### Underwater cultural heritage and extreme events: Storm impacts under climate change. (PNAS 2026)

- DOI: 10.1073/pnas.2523844123 | PMCID: PMC13012099 | PMID: 41838914
- Version used: **3.40.1**
- Evidence: To support data visualization, a world seabed sediment map of continental shelf areas was created with the software QGIS 3.40.1-Bratislava.
- Full pipeline: visualisation [QGIS v3.40.1]

### Rapid ice-marginal lake growth in Alaska driven by glacier retreat through bed overdeepenings. (PNAS 2026)

- DOI: 10.1073/pnas.2513289123 | PMCID: PMC13012058 | PMID: 41802086
- Evidence: Using Sentinel-2 optical imagery from 1 May to 30 September 2018 and 1 May to 30 September 2024, we manually mapped lake extents at 1:10,000 scale for these 2 y ( 48 ) in the open-source QGIS software program version 3.36.3-Maidenhead ( 49 ).
- Full pipeline: alignment/mapping [QGIS]

### From data to decisions: Toward a Biodiversity Monitoring Standards Framework. (PNAS 2026)

- DOI: 10.1073/pnas.2519347123 | PMCID: PMC12974509 | PMID: 41779789
- Evidence: This also involves the promotion of free and open-source analytical software [Open Source Initiative (2007); e.g., software libraries, QGIS, platform for biodiversity analytics such as BON in a Box] and provision of training, although methods could be documented such that they can be implemented independently of specific software choices.
- Full pipeline: machine learning [QGIS] -> stage not stated [Docker]

