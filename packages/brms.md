# brms

- **Category:** general
- **Papers in survey:** 70
- **Journals:** PNAS (53), Nature (14), Cell (2), Science (1)
- **Years:** 2021 (8), 2022 (9), 2023 (15), 2024 (13), 2025 (22), 2026 (3)
- **Versions named:** 2.20.3 (1), 2.20.4 (1), 2.14.4 (1), 2.13.5 (1)
- **Pipeline stages it appears in:** differential/statistical testing (47), simulation/modelling (3), normalisation (1), dimensionality reduction/clustering (1)

## Papers

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ....1 IQ-TREE 2 Minh et al., 2020 Version 2.0.6 lubridate https://github.com/tidyverse/lubridate Version 1.7.4 ape Paradis and Schliep, 2019 Version 5.3 brms Bürkner, 2018 Version 2.13.5 drc https://cran.r-project.org/web/packages/drc/drc.pdf Version 3.0-1 entropy https://cran.r-project.org/web/packages/entropy/ Version 1.2.1 RcppRoll https://cran.r-project.org/web/packages/RcppRoll/index.html Versio...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Evaluating the Effects of SARS-CoV-2 Spike Mutation D614G on Transmissibility and Pathogenicity. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.020 | PMCID: PMC7674007 | PMID: 33275900
- Version used: **2.13.5**
- Evidence: 5.3, brms v.
- Full pipeline: differential/statistical testing [R v3.6] -> stage not stated [BEAST, IQ-TREE, Nextflow, brms v2.13.5]

### Transgenic ferret models define pulmonary ionocyte diversity and function. (Nature 2023)

- DOI: 10.1038/s41586-023-06549-9 | PMCID: PMC10533402 | PMID: 37730992
- Evidence: Testing for differences in cell-type proportions To assess the significance of changes in the fraction of cells under different conditions, we used Bayesian negative binomial regression, estimated using the R package ‘brms’.
- Full pipeline: alignment/mapping [kallisto] -> variant calling [UMAP] -> quantification [R, Seurat] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [brms] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2]

### The recovery of European freshwater biodiversity has come to a halt. (Nature 2023)

- DOI: 10.1038/s41586-023-06400-1 | PMCID: PMC10432276 | PMID: 37558875
- Evidence: Trend values in precipitation and maximum temperature over the period covered by each time series were calculated using Bayesian models fitted using the R package brms 80 .
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Global hotspots of traded phylogenetic and functional diversity. (Nature 2023)

- DOI: 10.1038/s41586-023-06371-3 | PMCID: PMC10412452 | PMID: 37495700
- Evidence: We fit models using a Bernoulli distribution (logit link function) using the package brms 65 , 66 .
- Full pipeline: stage not stated [R, brms, phytools]

### Less extreme and earlier outbursts of ice-dammed lakes since 1900. (Nature 2023)

- DOI: 10.1038/s41586-022-05642-9 | PMCID: PMC9946834 | PMID: 36792828
- Evidence: We numerically approximate the posterior distribution using a Hamiltonian sampling algorithm implemented in Stan 73 that is called via the software package brms 74 within the statistical programming language R 75 .
- Full pipeline: differential/statistical testing [Stan, brms] -> stage not stated [QGIS]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: We implemented support for all generalized linear models provided by the stats R package, regularized linear models provided by the glmnet R package 69 , Bayesian regression models implemented through the brms R package 70 , gradient boosting regression through the xgboost R package 70 , 71 , as well as bagging and Bayesian ridge models through scikit-learn 72 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Continental-scale nutrient and contaminant delivery by Pacific salmon. (Nature 2024)

- DOI: 10.1038/s41586-024-07980-2 | PMCID: PMC11499284 | PMID: 39385021
- Evidence: Model fitting We fit models in R using the package brms 85 .
- Full pipeline: stage not stated [brms]

### Human degradation of tropical moist forests is greater than previously estimated. (Nature 2024)

- DOI: 10.1038/s41586-024-07629-0 | PMCID: PMC11254752 | PMID: 38961293
- Evidence: We fitted the models using the programming language Stan via the brms package in the R software for statistical computing 71 .
- Full pipeline: differential/statistical testing [brms]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **2.20.3**
- Evidence: Chains were sampled using the NUTS (No-U-Turn Sampler) algorithm in Stan ( https://mc-stan.org/ ) with the brms (v.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### A cryptic role for reciprocal helping in a cooperatively breeding bird. (Nature 2025)

- DOI: 10.1038/s41586-025-08958-4 | PMCID: PMC12158779 | PMID: 40335688
- Evidence: To estimate this relationship, we fitted a Bayesian negative binomial multilevel model (using the brms R package 68 with default priors) with total seconds of provisioning time by a visitor to a nest as the response variable, log-transformed total minutes of sampling time each day as the offset term, scaled minutes of nest attendance as the fixed effect, and nest and helper as random intercepts.
- Full pipeline: normalisation [R, brms] -> differential/statistical testing [R, brms] -> stage not stated [vegan]

### Plant diversity dynamics over space and time in a warming Arctic. (Nature 2025)

- DOI: 10.1038/s41586-025-08946-8 | PMCID: PMC12176628 | PMID: 40307554
- Evidence: Bayesian models were fitted using the brms package v.2.17 88 and ran for as many iterations as necessary to achieve convergence (2,000–3,000 iterations over four chains), which was assessed through examination of the Rhat term and trace plots.
- Full pipeline: differential/statistical testing [brms]

### Drivers of avian genomic change revealed by evolutionary rate decomposition. (Nature 2025)

- DOI: 10.1038/s41586-025-08777-7 | PMCID: PMC12119353 | PMID: 40108459
- Evidence: Using a Bayesian mixed-effects linear modelling framework, parameter inference was performed via the no U-turn sampler 66 , 67 as implemented in the package brms 68 .
- Full pipeline: dimensionality reduction/clustering [BLAST, clusterProfiler] -> differential/statistical testing [brms] -> structure determination [phytools] -> visualisation [phytools] -> stage not stated [IQ-TREE v2.1.2, R]

### Vulnerability of amphibians to global warming. (Nature 2025)

- DOI: 10.1038/s41586-025-08665-0 | PMCID: PMC11946914 | PMID: 40044855
- Evidence: While better methods exist to model phylogenetic patterns, generalized additive linear models do not allow for phylogenetic correlation matrices, and other functions such as brms 106 surpassed our computational time and memory limits.
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [R, brms] -> visualisation [ggplot2] -> stage not stated [lme4 v1.1, metafor]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Evidence: To implement Bayesian sampling for these analyses, we used brms 106 , a package that enables coding models in R for implementation in the stan statistical language 107 .
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Technology mediation in child sexual exploitation and abuse in Africa and Asia. (Nature 2026)

- DOI: 10.1038/s41586-026-10525-4 | PMCID: PMC13253325 | PMID: 42203864
- Evidence: All other parameters retained brms default priors: a Student- t (3, 0, 2.5) prior for the intercept, half-Student- t (3, 0, 2.5) priors for random effect standard deviations and an LKJ(1) prior for the random effects correlation matrix 93 , 94 .
- Full pipeline: differential/statistical testing [R] -> stage not stated [brms, ggplot2]

### The (minimal) persuasive advantage of political video over text. (PNAS 2021)

- DOI: 10.1073/pnas.2114388118 | PMCID: PMC8617416 | PMID: 34782473
- Evidence: To test our main hypotheses, we fit a series of Bayesian multilevel linear regression models using the brms package in R ( 58 , 59 ).
- Full pipeline: differential/statistical testing [R, brms]

### Anthropogenic pressures and life history predict trajectories of seagrass meadow extent at a global scale. (PNAS 2021)

- DOI: 10.1073/pnas.2110802118 | PMCID: PMC8609331 | PMID: 34725160
- Evidence: We fit models using the brms package ( 79 ) from R ( 80 ).
- Full pipeline: stage not stated [brms]

### Monitoring the COVID-19 epidemic with nationwide telecommunication data. (PNAS 2021)

- DOI: 10.1073/pnas.2100664118 | PMCID: PMC8256040 | PMID: 34162708
- Evidence: The software used for estimation is the R package brms ( 60 , 61 ) version 2.11.1 built upon the statistical modeling platform Stan ( 62 ).
- Full pipeline: differential/statistical testing [R, brms] -> simulation/modelling [Stan v2.19.2]

### Global abundance estimates for 9,700 bird species. (PNAS 2021)

- DOI: 10.1073/pnas.2023170118 | PMCID: PMC8166167 | PMID: 34001610
- Evidence: We then fit a Bayesian mixed-effects random slope model using the R package brms ( 71 , 72 ), which is a wrapper to fit Bayesian models in stan ( 73 ) via rstan ( 74 ).
- Full pipeline: differential/statistical testing [R, brms] -> stage not stated [phytools]

### Neural indicators of articulator-specific sensorimotor influences on infant speech perception. (PNAS 2021)

- DOI: 10.1073/pnas.2025043118 | PMCID: PMC8157983 | PMID: 33980713
- Evidence: Model fit was implemented using the package brms ( 49 ) v2.12 within the R computing environment.
- Full pipeline: stage not stated [EEGLAB, FieldTrip, brms]

### Human disturbance compresses the spatiotemporal niche. (PNAS 2022)

- DOI: 10.1073/pnas.2206339119 | PMCID: PMC9907093 | PMID: 36534801
- Evidence: We ran the pair and network models in the R package brms ( 76 , 77 ) using three Markov chain Monte Carlo (MCMC) chains run for 4,000 iterations, discarding the initial 2,000 iterations as warmup.
- Full pipeline: simulation/modelling [brms] -> stage not stated [R]

### Noninvasive detection of any-stage cancer using free glycosaminoglycans. (PNAS 2022)

- DOI: 10.1073/pnas.2115328119 | PMCID: PMC9897435 | PMID: 36469776
- Version used: **2.14.4**
- Evidence: Bayesian estimation was carried out using the brms (2.14.4) ( 36 , 37 ) and tidybayes (2.3.1) packages in R (4.0.4).
- Full pipeline: differential/statistical testing [R v4.0.4, brms v2.14.4] -> stage not stated [rstanarm]

### Within-individual changes reveal increasing social selectivity with age in rhesus macaques. (PNAS 2022)

- DOI: 10.1073/pnas.2209180119 | PMCID: PMC9894112 | PMID: 36445967
- Evidence: We conducted all analyses using R version 4.1.0 ( 58 ) and fitted all models in the Bayesian software STAN ( 59 ) using the brms package (version 2.15.0; ( 60 )).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R v1.8.5]

### A resource-rational model of human processing of recursive linguistic structure. (PNAS 2022)

- DOI: 10.1073/pnas.2122602119 | PMCID: PMC9618130 | PMID: 36260742
- Evidence: We then analyzed log-transformed reading times on the final verb using Bayesian mixed-effects models implemented in Stan ( 71 ) using brms ( 72 ).
- Full pipeline: differential/statistical testing [Stan, brms]

### Systemic racism alters wildlife genetic diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2102860119 | PMCID: PMC9618126 | PMID: 36256811
- Evidence: To test for the effects of residential racial segregation (% White residents in neighborhood) on the genetic diversity of wild populations we used Bayesian linear mixed models implemented in the brms package ( 24 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Factors influencing terrestriality in primates of the Americas and Madagascar. (PNAS 2022)

- DOI: 10.1073/pnas.2121105119 | PMCID: PMC9586308 | PMID: 36215474
- Evidence: We fitted the models in R v3.6.3 ( 118 ) using the ‘brms’ package ( 126 ), for model fitting, ‘bayestestR’ ( 125 ) for Bayesian summary statistics, and ‘ape’ ( 127 ) and ‘phytools’ ( 128 ) for handling the phylogenetic data.
- Full pipeline: differential/statistical testing [brms, phytools] -> stage not stated [R v3.6]

### Linguistic measures of psychological distance track symptom levels and treatment outcomes in a large set of psychotherapy transcripts. (PNAS 2022)

- DOI: 10.1073/pnas.2114737119 | PMCID: PMC9060508 | PMID: 35316132
- Evidence: Bayesian analyses were conducted using the brms package ( 85 , 86 ).
- Full pipeline: differential/statistical testing [R, brms, lme4]

### A global analysis of tree pests and emerging pest threats. (PNAS 2022)

- DOI: 10.1073/pnas.2113298119 | PMCID: PMC9060442 | PMID: 35312373
- Evidence: The model was fit in Stan ( 49 ) and called with the brms package ( 50 ) in R.
- Full pipeline: stage not stated [Stan, brms]

### Children across societies enforce conventional norms but in culturally variable ways. (PNAS 2022)

- DOI: 10.1073/pnas.2112521118 | PMCID: PMC8740750 | PMID: 34969840
- Evidence: We analyzed all data in R ( 56 ) and implemented Bayesian multilevel models using the brms package ( 57 , 58 ) and the package’s default priors.
- Full pipeline: differential/statistical testing [R, brms]

### Hippocampal contributions to novel spatial learning are both age-related and age-invariant. (PNAS 2023)

- DOI: 10.1073/pnas.2307884120 | PMCID: PMC10723126 | PMID: 38055735
- Evidence: We utilized the brms package ( 52 ) in R 4.2.2, employing 10 Markov chain Monte Carlo chains with 6,000 iterations per chain, resulting in a total of 20,000 posterior iterations for coefficient estimation.
- Full pipeline: normalisation [ANTs v2.3.5] -> simulation/modelling [brms] -> stage not stated [FSL, PsychoPy, R v4.2, emmeans, lme4]

### Increased homozygosity due to endogamy results in fitness consequences in a human population. (PNAS 2023)

- DOI: 10.1073/pnas.2309552120 | PMCID: PMC10614605 | PMID: 37847737
- Evidence: To assess the effects of F ROH on fertility, we performed a Bayesian Poisson regression in R, fitted using the brms() package ( 64 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [PLINK]

### Acetylcholine and noradrenaline enhance foraging optimality in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2305596120 | PMCID: PMC10483619 | PMID: 37639601
- Evidence: Bayesian hierarchical linear mixed-effects models were constructed using the package brms ( 110 ).
- Full pipeline: differential/statistical testing [brms, emmeans] -> stage not stated [Psychtoolbox]

### Evolutionary predictors of the specific colors of birds. (PNAS 2023)

- DOI: 10.1073/pnas.2217692120 | PMCID: PMC10450850 | PMID: 37579151
- Evidence: Models were implemented using a hierarchical Bayesian approach with the R package “brms” (v 2.16.3) ( 97 ), an R interface with STAN ( 98 ), used to fit the models.
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R, emmeans]

### Emotional (in)stability: Neuroticism is associated with increased variability in negative emotion after all. (PNAS 2023)

- DOI: 10.1073/pnas.2212154120 | PMCID: PMC10266024 | PMID: 37253012
- Evidence: We used brms ( 15 ), which implements Bayesian multilevel models using an R interface to the probabilistic programming language Stan ( 31 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Do some languages sound more beautiful than others? (PNAS 2023)

- DOI: 10.1073/pnas.2218367120 | PMCID: PMC10151606 | PMID: 37068255
- Evidence: Unaggregated responses were analyzed using Bayesian multilevel models fit with the R package brms ( 37 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Conservation successes and challenges for wide-ranging sharks and rays. (PNAS 2023)

- DOI: 10.1073/pnas.2216891120 | PMCID: PMC9945978 | PMID: 36689654
- Evidence: All models were implemented in the R statistical language v.4.1.0 ( 83 ) using the brms package v.2.16.2 ( 86 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Mapping the number of female sex workers in countries across sub-Saharan Africa. (PNAS 2023)

- DOI: 10.1073/pnas.2200633120 | PMCID: PMC9926247 | PMID: 36595685
- Evidence: The model was fitted using the RStan ( 37 ) and brms ( 38 , 39 ) packages.
- Full pipeline: stage not stated [R, Stan, brms]

### Burkitt lymphoma risk shows geographic and temporal associations with <i>Plasmodium falciparum</i> infections in Uganda, Tanzania, and Kenya. (PNAS 2023)

- DOI: 10.1073/pnas.2211055120 | PMCID: PMC9926229 | PMID: 36595676
- Evidence: All models were fitted using the “brms” package for Bayesian hierarchical regression modeling for R 4.0.0, using default priors for both regression and variance parameters ( 57 , 58 ).
- Full pipeline: differential/statistical testing [R v4.0, brms]

### Sex and age differences in "theory of mind" across 57 countries using the English version of the "Reading the Mind in the Eyes" Test. (PNAS 2023)

- DOI: 10.1073/pnas.2022385119 | PMCID: PMC9910622 | PMID: 36584298
- Evidence: This was conducted using the brms package in R version 4.1.2.
- Full pipeline: stage not stated [R v4.1.2, brms]

### Susceptibility to online misinformation: A systematic meta-analysis of demographic and psychological factors. (PNAS 2024)

- DOI: 10.1073/pnas.2409329121 | PMCID: PMC11588074 | PMID: 39531500
- Evidence: We used a Bayesian generalized linear mixed-effects model (GLMM) with the R package brms ( 89 ) assuming a Bernoulli-distributed response with a probit link function.
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Path dependence, stigmergy, and memetic reification in the formation of the 27 Club myth. (PNAS 2024)

- DOI: 10.1073/pnas.2413373121 | PMCID: PMC11573623 | PMID: 39495913
- Evidence: Bayesian models were estimated using the brms package in R ( 13 ), with more information available in the SI Appendix .
- Full pipeline: differential/statistical testing [R, brms]

### The persistent DDT footprint of ocean disposal, and ecological controls on bioaccumulation in fishes. (PNAS 2024)

- DOI: 10.1073/pnas.2401500121 | PMCID: PMC11551384 | PMID: 39467121
- Evidence: Parameter estimates were obtained using the “brms” R package ( 105 ), which makes use of Stan ( 106 ) to implement a Hamiltonian Monte Carlo Sampler and its extension the No-U-Turn Sampler ( 107 ).
- Full pipeline: differential/statistical testing [R] -> simulation/modelling [brms]

### Microevolutionary change in wild stickleback: Using integrative time-series data to infer responses to selection. (PNAS 2024)

- DOI: 10.1073/pnas.2410324121 | PMCID: PMC11406292 | PMID: 39231210
- Evidence: All models were fit using Stan via the brms package in R statistical environment (version 4.1.2) ( 69 ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> differential/statistical testing [R, Stan, brms] -> stage not stated [ImageJ]

### A quantitative model of temperature-dependent diapause progression. (PNAS 2024)

- DOI: 10.1073/pnas.2407057121 | PMCID: PMC11388385 | PMID: 39196619
- Evidence: We performed all modeling using Bayesian methods in Stan ( 57 ), via the package brms ( 58 ) in R [version 4.1.3; R Core Team ( 59 )].
- Full pipeline: differential/statistical testing [R, Stan, brms] -> stage not stated [tidyverse]

### Maternal manipulation of offspring size can trigger the evolution of eusociality in promiscuous species. (PNAS 2024)

- DOI: 10.1073/pnas.2402179121 | PMCID: PMC11331107 | PMID: 39110731
- Version used: **2.20.4**
- Evidence: 3 , we derived probabilities of direction (pd), which represents the posterior probability that an effect occurs in a particular direction, from Bayesian models implemented with the brms v2.20.4 ( 82 – 84 ) package in combination with the MCMC sampler of cmdstanr ( 85 ) and posterior means with the emmeans v1.8.8 ( 86 ) package (details in SI Appendix ).
- Full pipeline: differential/statistical testing [brms v2.20.4, emmeans v1.8.8] -> stage not stated [R v4.2, tidyverse v2.0.0]

### Interaction structure constrains the emergence of conventions in group communication. (PNAS 2024)

- DOI: 10.1073/pnas.2403888121 | PMCID: PMC11252989 | PMID: 38968102
- Evidence: We fit all regression models in brms ( 49 ) with weakly regularizing priors.
- Full pipeline: differential/statistical testing [brms]

### Shifting fire regimes cause continent-wide transformation of threatened species habitat. (PNAS 2024)

- DOI: 10.1073/pnas.2316417121 | PMCID: PMC11067043 | PMID: 38648477
- Evidence: We then fitted Bayesian mixed effects models using the brms package ( 60 ) in program R ( 61 ) to determine whether the change coefficients of each fire metric for reserves could be predicted by reserve area (AREA), protected area status (PA), HFI, NDVI, annual rainfall change coefficient (RAIN_CHANGE), elevation (ELEV), initial proportion unburnt (INIT), and mean annual proportion of reserve burn...
- Full pipeline: differential/statistical testing [brms]

### Macroscale controls determine the recovery of river ecosystem productivity following flood disturbances. (PNAS 2024)

- DOI: 10.1073/pnas.2307065121 | PMCID: PMC10835108 | PMID: 38266048
- Evidence: We fit the model in a Bayesian framework using the brms package ( 85 ), with four chains run for 2,000 iterations including 1,000 warm-up iterations (i.e., 4,000 total iterations per model fit) and a maximum tree depth of 12.
- Full pipeline: differential/statistical testing [brms] -> visualisation [tidyverse] -> stage not stated [R]

### Primate social organization evolved from a flexible pair-living ancestor. (PNAS 2024)

- DOI: 10.1073/pnas.2215401120 | PMCID: PMC10769843 | PMID: 38154063
- Evidence: All models were estimated in the Stan statistical programming language ( 60 ) using R (R Core Team 2020) and the brms package ( 66 ).
- Full pipeline: differential/statistical testing [R, brms]

### A species' response to spatial climatic variation does not predict its response to climate change. (PNAS 2024)

- DOI: 10.1073/pnas.2304404120 | PMCID: PMC10769845 | PMID: 38109562
- Evidence: Hence, we implemented the growth model in a Bayesian framework, using minimally informative priors, in the “brms” package in R 3.3.0 ( 99 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R v3.6]

### Oxytocin varies across the life course in a sex-specific way in a human subsistence population. (PNAS 2025)

- DOI: 10.1073/pnas.2509977122 | PMCID: PMC12745800 | PMID: 41397140
- Evidence: We investigated age- and sex-related differences in OT throughout the life course using generalized linear multilevel models (GLMMs) and the brms package in R ( 78 ).
- Full pipeline: stage not stated [R v4.5.1, brms]

### Dried fish provide widespread access to critical nutrients across Africa. (PNAS 2025)

- DOI: 10.1073/pnas.2426844122 | PMCID: PMC12501148 | PMID: 40982677
- Evidence: Models were fitted using brms ( 122 ) and Stan ( 123 ) in R 4.3.3. [1] γ i = country a + cluster b + β 1 prox marine i * β 2 prox inland i + β 3 prox urban i + β 4 hh size i + β 5 hh wealth i + β 6 rural i .
- Full pipeline: dimensionality reduction/clustering [R v4.3, brms]

### Historical and experimental evidence that inherent properties are overweighted in early scientific explanation. (PNAS 2025)

- DOI: 10.1073/pnas.2424725122 | PMCID: PMC12478141 | PMID: 40971388
- Evidence: In Studies 2 to 5, we performed Bayesian data analysis using the R package brms ( 76 ).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R]

### Chants across seven traditions share acoustic traits that enhance subjective relaxation. (PNAS 2025)

- DOI: 10.1073/pnas.2506480122 | PMCID: PMC12415189 | PMID: 40854128
- Evidence: All mixed model analyses were conducted in R using the brms package ( 81 ) with mildly informative conservative priors.
- Full pipeline: stage not stated [R, brms]

### Decoding memory function through naturalistic gaze patterns. (PNAS 2025)

- DOI: 10.1073/pnas.2505879122 | PMCID: PMC12377732 | PMID: 40789026
- Evidence: To elucidate the relationship between group status and idiosyncratic gaze similarity, we used Bayesian multilevel modeling ( brms package) to model a linear effect of group based on presumed memory function (YA > HOA > AR > MCI > Amnesia).
- Full pipeline: differential/statistical testing [brms]

### Semantic change in adults is not primarily a generational phenomenon. (PNAS 2025)

- DOI: 10.1073/pnas.2426815122 | PMCID: PMC12337318 | PMID: 40720652
- Evidence: We implement our Bayesian meta-analysis model in R using the brms front-end ( 90 ) to Stan ( 91 ).
- Full pipeline: differential/statistical testing [brms]

### Translocations contribute to population rescue in an imperiled woodpecker. (PNAS 2025)

- DOI: 10.1073/pnas.2410946122 | PMCID: PMC12337267 | PMID: 40720647
- Evidence: Second, we fit a series of Bayesian regression models with stan ( 55 ) and brms ( 56 ) to examine whether translocated birds showed differences in lifetime reproductive success (total fledglings produced over an individual’s life) compared to birds with no translocation ancestry ( SI Appendix , Tables S2 and S3 ).
- Full pipeline: differential/statistical testing [brms]

### Contribution of glutamatergic projections to neurons in the nonhuman primate substantia nigra pars reticulata for reactive inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2427032122 | PMCID: PMC12232709 | PMID: 40569385
- Evidence: For LMM and GLMM analyses, we used the lme4 ( 66 ), pbkrtest ( 67 ), emmeans ( 68 ), and brms ( 69 ) packages in RStudio.
- Full pipeline: stage not stated [brms, emmeans, lme4]

### Conserving the beauty of the world's reef fish assemblages. (PNAS 2025)

- DOI: 10.1073/pnas.2415931122 | PMCID: PMC12207427 | PMID: 40531873
- Evidence: All models were built using the R package brms ( 60 ) and were run with four chains of 4,000 iterations.
- Full pipeline: stage not stated [R, brms]

### Cave records reveal recent origin of North America's deepest canyon. (PNAS 2025)

- DOI: 10.1073/pnas.2413069122 | PMCID: PMC12130896 | PMID: 40388611
- Evidence: For model (7), we used the default priors implemented in the R package brms, i.e an Inverse Gamma(8, 3) prior to cater to a length-scale parameter of the Gaussian Process that would more smoothly cover the time interval of our study, and a Student-t (3, 0, 2.5) prior on the variance; again, we forced the regression line through the origin.
- Full pipeline: differential/statistical testing [R, brms]

### Group traits moderate the relationship between individual social traits and fitness in gorillas. (PNAS 2025)

- DOI: 10.1073/pnas.2421539122 | PMCID: PMC12107160 | PMID: 40324072
- Evidence: All models were run as Bayesian multilevel models in the brms R package ( 98 ) using R version 4.3.1.
- Full pipeline: differential/statistical testing [R, brms] -> stage not stated [igraph]

### Global subnational estimates of migration of scientists reveal large disparities in internal and international flows. (PNAS 2025)

- DOI: 10.1073/pnas.2424521122 | PMCID: PMC12012457 | PMID: 40215276
- Evidence: The model was fitted using the brms R package ( 46 , 47 ).
- Full pipeline: stage not stated [R, brms]

### Indigenous Knowledge as a sole data source in habitat selection functions. (PNAS 2025)

- DOI: 10.1073/pnas.2411946122 | PMCID: PMC12012537 | PMID: 40198704
- Evidence: All analysis was completed in R (R Core Team 2023) and beta regression was completed using a Bayesian approach and the R package brms ( 69 ), with flat priors over the entire real line.
- Full pipeline: differential/statistical testing [R, brms]

### Quirks of cognition explain why we dramatically overestimate the size of minority groups. (PNAS 2025)

- DOI: 10.1073/pnas.2413064122 | PMCID: PMC12002232 | PMID: 40163733
- Evidence: All models were fit using the brms package in R .
- Full pipeline: stage not stated [brms]

### Belief in belief: Even atheists in secular countries show intuitive preferences favoring religious belief. (PNAS 2025)

- DOI: 10.1073/pnas.2404720122 | PMCID: PMC12002237 | PMID: 40146854
- Evidence: Models used the brms package in R ( 45 ), including its in-built Bayes factor model comparison functions.
- Full pipeline: stage not stated [R, brms]

### The population dynamics of clustered consumer-resource spatial patterns: Insights from the demographics of a Turing mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2407991121 | PMCID: PMC11761679 | PMID: 39823299
- Evidence: To analyze the trends in the Phoridae dynamics across the ages of Azteca nests, we used Bayesian multilevel models implemented in the brms R package ( 46 ).
- Full pipeline: differential/statistical testing [R, brms]

### An inverse correlation between structural linguistic and human genetic diversity. (PNAS 2026)

- DOI: 10.1073/pnas.2526762123 | PMCID: PMC13142977 | PMID: 42066044
- Evidence: For each feature, all available languages were modeled in a GAMM implemented using the brms ( 81 ) interface to Stan ( 82 , 83 ) in R ( 84 ).
- Full pipeline: variant calling [PLINK v1.9] -> stage not stated [R, Stan, brms]

### Kava consumption and the rise of sociopolitical complexity in Oceania. (PNAS 2026)

- DOI: 10.1073/pnas.2521658123 | PMCID: PMC12956823 | PMID: 41730102
- Evidence: We ran Bayesian regression models using the R package brms ( 41 ).
- Full pipeline: differential/statistical testing [R, brms]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Evidence: Bayesian analysis of age–viral load associations We estimated associations of viral load and age with a thin-plate spline regression using the brms package ( 58 , 59 ) in R ( 60 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

