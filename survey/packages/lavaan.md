# lavaan

- **Category:** general
- **Papers in survey:** 21
- **Journals:** PNAS (20), Nature (1)
- **Years:** 2021 (3), 2022 (2), 2023 (4), 2024 (6), 2025 (3), 2026 (3)
- **Versions named:** 0.6 (4), 0.6.8 (1)
- **Pipeline stages it appears in:** differential/statistical testing (3), machine learning (1)

## Papers

### Polygenic and developmental profiles of autism differ by age at diagnosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09542-6 | PMCID: PMC12571882 | PMID: 41034588
- Version used: **0.6**
- Evidence: All latent growth curve models were fitted under the structural equation modelling framework using the lavaan (v.0.6-19) package in R 67 .
- Full pipeline: differential/statistical testing [PLINK, lme4 v1.1.27.1] -> stage not stated [GCTA, LDSC, lavaan v0.6]

### National religiosity eases the psychological burden of poverty. (PNAS 2021)

- DOI: 10.1073/pnas.2103913118 | PMCID: PMC8488579 | PMID: 34544863
- Version used: **0.6**
- Evidence: We accounted for the nested data structure (persons nested in nations) by using linear mixed-effects models in R [mixed-effects model package lme4 version 1.1-23, models 1 through 3 ( 53 ); mixed-effects path model package lavaan version 0.6-7, model 4 ( 54 )].
- Full pipeline: differential/statistical testing [lavaan v0.6, lme4 v1.1]

### Trade-offs among transport, support, and storage in xylem from shrubs in a semiarid chaparral environment tested with structural equation modeling. (PNAS 2021)

- DOI: 10.1073/pnas.2104336118 | PMCID: PMC8379947 | PMID: 34389676
- Version used: **0.6**
- Evidence: All SEM tests were run using R (R version 4.0.5) package lavaan 0.6 to 8 ( 43 ).
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.0.5, lavaan v0.6]

### Segregation, integration, and balance of large-scale resting brain networks configure different cognitive abilities. (PNAS 2021)

- DOI: 10.1073/pnas.2022288118 | PMCID: PMC8201916 | PMID: 34074762
- Evidence: SEM analysis was performed using the lavaan package in R ( 69 ).
- Full pipeline: simulation/modelling [BrainNet Viewer] -> visualisation [BrainNet Viewer] -> stage not stated [R, lavaan]

### NETfacts: An integrated intervention at the individual and collective level to treat communities affected by organized violence. (PNAS 2022)

- DOI: 10.1073/pnas.2204698119 | PMCID: PMC9636916 | PMID: 36306329
- Version used: **0.6**
- Evidence: Finally, to evaluate the longitudinal relationship between treatment and social outcomes on the prevalence of violence, we conducted a path analysis with lavaan 0.6–9 ( 70 ).
- Full pipeline: differential/statistical testing [R v4.0] -> stage not stated [emmeans v1.4.6, lavaan v0.6, lme4 v1.1]

### The evolution of insular woodiness. (PNAS 2022)

- DOI: 10.1073/pnas.2208629119 | PMCID: PMC9478640 | PMID: 36067289
- Version used: **0.6.8**
- Evidence: We fitted the structural equation models using the R package lavaan version 0.6.8 ( 79 ).
- Full pipeline: dimensionality reduction/clustering [phytools] -> stage not stated [R, lavaan v0.6.8]

### Exposure to automation explains religious declines. (PNAS 2023)

- DOI: 10.1073/pnas.2304748120 | PMCID: PMC10450436 | PMID: 37579178
- Evidence: ( B ) Estimates from a 5,000-sample bootstrapped mediation model, fit in lavaan for study 5, in which association with laws of nature fully explains why learning about AI reduces religiosity more than learning about science.
- Full pipeline: stage not stated [lavaan]

### Whole-soil-profile warming does not change microbial carbon use efficiency in surface and deep soils. (PNAS 2023)

- DOI: 10.1073/pnas.2302190120 | PMCID: PMC10410710 | PMID: 37523548
- Evidence: All statistical analyses were performed with R (version 4.1.3) using the lme4 ( 62 ), vegan ( 63 ), lavaan ( 64 ), psych ( 65 ), MuMIn ( 66 ), and rdacca.hp ( 67 ) packages.
- Full pipeline: differential/statistical testing [R v4.1.3, lavaan, lme4]

### Ecoevolutionary processes structure milk microbiomes across the mammalian tree of life. (PNAS 2023)

- DOI: 10.1073/pnas.2218900120 | PMCID: PMC10334807 | PMID: 37399384
- Evidence: We tested direct and indirect effects of quantitative dietary items (Elton Traits) on milk nutrient content and microbial structure with structural equation modeling (package lavaan) ( 76 ).
- Full pipeline: stage not stated [QIIME 2, R v4.0.3, lavaan, phyloseq]

### Elevated dementia risk, cognitive decline, and hippocampal atrophy in multisite chronic pain. (PNAS 2023)

- DOI: 10.1073/pnas.2215192120 | PMCID: PMC9992778 | PMID: 36802440
- Evidence: Mediation analyses were conducted in R 4.1.2 ( 82 ) with the “lavaan” package ( 88 ).
- Full pipeline: visualisation [ggplot2] -> stage not stated [FreeSurfer, R v4.1, lavaan]

### Ecological restoration enhances dryland carbon stock by reducing surface soil carbon loss due to wind erosion. (PNAS 2024)

- DOI: 10.1073/pnas.2416281121 | PMCID: PMC11573679 | PMID: 39514308
- Evidence: Therefore, we performed the “spdep,” “nlme,” and “lavaan” packages in R to construct spatial residuals.
- Full pipeline: stage not stated [R, lavaan, metafor]

### Impulsivity is a stable, measurable, and predictive psychological trait. (PNAS 2024)

- DOI: 10.1073/pnas.2321758121 | PMCID: PMC11181114 | PMID: 38830093
- Evidence: This model was estimated using the R package lavaan ( 56 ) with the weighted least-squares mean and variance estimator, using diagonally weighted least squares and computing robust SE, and all factors forced to be orthogonal, as defined by the standard bifactor model.
- Full pipeline: stage not stated [R, lavaan]

### A sociocultural approach to voting: Construing voting as a duty to others predicts political interest and engagement. (PNAS 2024)

- DOI: 10.1073/pnas.2215051121 | PMCID: PMC11145289 | PMID: 38768346
- Evidence: We next tested for mediation using the R package “lavaan” ( 55 ), with interdependent (vs. independent) language as the predictor, perceived duty to vote as the mediator, and political intentions as the outcome.
- Full pipeline: stage not stated [R, lavaan]

### The evolution of sex roles: The importance of ecology and social environment. (PNAS 2024)

- DOI: 10.1073/pnas.2321294121 | PMCID: PMC11145285 | PMID: 38771872
- Evidence: To corroborate the results of Fisher’s C-statistic, we calculated four additional widely used indices of model fit (TLI, CFI, RMSEA, SRMR) using the “lavaan” R package ( 123 ).
- Full pipeline: differential/statistical testing [R, lavaan] -> simulation/modelling [R] -> stage not stated [Python v3.10]

### Ripple effects of hospital team faultlines on patient outcomes (PNAS 2024)

- DOI: None | PMCID: PMC10666119 | PMID: None
- Evidence: We conducted these analyses using the lavaan (latent variable analysis) package in R ( 30 , 31 ).
- Full pipeline: dimensionality reduction/clustering [R] -> stage not stated [lavaan, lme4]

### Childhood maltreatment influences adult brain structure through its effects on immune, metabolic, and psychosocial factors. (PNAS 2024)

- DOI: 10.1073/pnas.2304704121 | PMCID: PMC11032474 | PMID: 38593073
- Evidence: Path coefficients were estimated using the “lavaan” package in R ( 113 ).
- Full pipeline: stage not stated [FreeSurfer, R v4.2.2, lavaan]

### Habenula-ventral tegmental area functional coupling and risk aversion in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2500815122 | PMCID: PMC12595472 | PMID: 41166429
- Evidence: All SEM was conducted in Latent Variable Analysis (lavaan) package v.0.6-17 using Maximum Likelihood estimation ( 44 ).
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [FSL, PsychoPy v2021.1.4, lavaan]

### Stability of general cognitive ability from infancy to adulthood: A combined twin and genomic investigation. (PNAS 2025)

- DOI: 10.1073/pnas.2426531122 | PMCID: PMC12130889 | PMID: 40388623
- Evidence: Phenotypic and PGS analyses were conducted using the lavaan package ( 80 ) and genetic analyses were conducted using the OpenMx package ( 81 ).
- Full pipeline: stage not stated [R v4.2.4, lavaan]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Evidence: SEM was conducted using the lavaan package ( 25 ).
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

### Building courage, strength, and knowledge: Mindfulness training reduces psychological threat and increases engagement in college physics. (PNAS 2026)

- DOI: 10.1073/pnas.2521857123 | PMCID: PMC13079943 | PMID: 41941630
- Evidence: Finally, we investigated whether reduced psychological threat served as an indirect effect variable between mindfulness training and physics engagement using SEM path analyses in lavaan ( 56 ).
- Full pipeline: machine learning [lavaan] -> stage not stated [R v4.4, lme4]

### Compounded effects on wetland greenhouse gas fluxes from climate change and water management along a saline to freshwater gradient. (PNAS 2026)

- DOI: 10.1073/pnas.2513685123 | PMCID: PMC12933060 | PMID: 41701819
- Evidence: We designed and tested the conceptual structural models using “lavaan” ( 104 ), based on the sample covariance matrix for standardized observed input variables, which included mean CO 2 and CH 4 flux as endogenous variables and management indicators as exogenous variables ( SI Appendix , Table S6 and Extended Methods ).
- Full pipeline: simulation/modelling [Python] -> machine learning [R] -> stage not stated [lavaan]

