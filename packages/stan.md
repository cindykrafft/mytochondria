# Stan

- **Category:** general
- **Papers in survey:** 64
- **Journals:** PNAS (48), Nature (10), Cell (3), Science (2), Lancet (1)
- **Years:** 2021 (10), 2022 (9), 2023 (12), 2024 (17), 2025 (13), 2026 (3)
- **Versions named:** 2.28.1 (3), 2.26.11 (1), 2.23.0 (1), 2.33.1 (1), 2.32.5 (1), 2.26.13 (1), 2.19.2 (1), 2.19.3 (1)
- **Pipeline stages it appears in:** differential/statistical testing (29), simulation/modelling (14), normalisation (1)

## Papers

### Genome-wide gene expression tuning reveals diverse vulnerabilities of M. tuberculosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.033 | PMCID: PMC8382161 | PMID: 34297925
- Version used: **2.19.3**
- Evidence: ...0.1) Seabold and Perktold, 2010 https://www.statsmodels.org/stable/index.html Rstan (version 2.19.3) Stan Development Team, 2020 https://mc-stan.org/ Stan (version 2.19.3) Stan Development Team, 2021 https://mc-stan.org/ SpectroMine 1.0 Biognosys AG https://biognosys.com/software/spectromine/ Other Resource website that provides gene vulnerability data for M. tuberculosis and M. smegmatis This pap...
- Full pipeline: alignment/mapping [Python v2.7.18, SciPy v1.2.2] -> stage not stated [BLAST, Stan v2.19.3, statsmodels v0.10.1]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Version used: **2.28.1**
- Evidence: ...imAl v1.2 Capella-Gutiérrez et al., 2009 http://trimal.cgenomics.org RAxML v8.2.12 Stamatakis, 2014 https://cme.h-its.org/exelixis/web/software/raxml CmdStan v2.28.1 The Stan Development Team https://mc-stan.org CmdStanr v0.4.0 The Stan Development Team https://mc-stan.org/cmdstanr/ R v4.1.3 The R Foundation https://www.r-project.org/ Sequencher v5.1 software Gene Codes Corporation N/A In-house sc...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **2.28.1**
- Evidence: ... RAxML v8.2.12 ( Stamatakis, 2014 ) https://cme.h-its.org/exelixis/web/software/raxml BEAST2 v2.6.6 ( Bouckaert et al., 2014 ) https://www.beast2.org CmdStan v2.28.1 The Stan Development Team https://mc-stan.org CmdStanr v0.4.0 The Stan Development Team https://mc-stan.org/cmdstanr/ R v4.1.2 The R Foundation https://www.r-project.org/ Sequencher v5.1 software Gene Codes Corporation N/A In-house sc...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Global, regional, and national estimates and trends in stillbirths from 2000 to 2019: a systematic assessment. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)01112-0 | PMCID: PMC8417352 | PMID: 34454675
- Evidence: We used a Hamiltonian Monte Carlo algorithm implemented with the use of Stan 21 and R package RStan 22 to generate samples from the posterior distributions of stillbirth rate.
- Full pipeline: simulation/modelling [R, Stan]

### Attenuated fusogenicity and pathogenicity of SARS-CoV-2 Omicron variant. (Nature 2022)

- DOI: 10.1038/s41586-022-04462-1 | PMCID: PMC8942852 | PMID: 35104835
- Version used: **2.28.1**
- Evidence: Parameter estimation was performed by the framework of Bayesian statistical inference with Markov chain Monte Carlo (MCMC) methods implemented in CmdStan v.2.28.1 ( https://mc-stan.org ) with cmdstanr v.0.4.0 ( https://mc-stan.org/cmdstanr/ ).
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [fastp v0.21.0] -> variant calling [SAMtools v1.9] -> differential/statistical testing [Stan v2.28.1] -> simulation/modelling [Stan v2.28.1] -> stage not stated [BWA v0.7.17, ImageJ, R v3.6]

### Malaria protection due to sickle haemoglobin depends on parasite genotype. (Nature 2022)

- DOI: 10.1038/s41586-021-04288-3 | PMCID: PMC8810385 | PMID: 34883497
- Evidence: To reduce overfitting we used Stan 46 to fit the model assuming a mild regularising Gaussian prior with mean zero and standard deviation of 2 on the log-odds scale (that is, with 95% of mass between 1/50 and 50 on the relative risk scale) for each parameter, and between-parameter correlations set to 0.5.
- Full pipeline: alignment/mapping [MAFFT, STAR v2.7.3a, minimap2] -> variant calling [GATK] -> stage not stated [Stan]

### The burden and dynamics of hospital-acquired SARS-CoV-2 in England. (Nature 2023)

- DOI: 10.1038/s41586-023-06634-z | PMCID: PMC10620085 | PMID: 37853126
- Evidence: All analyses were performed in Stan 34 using the rstan package v.2.21.1 in R (ref.
- Full pipeline: stage not stated [R, Stan]

### Less extreme and earlier outbursts of ice-dammed lakes since 1900. (Nature 2023)

- DOI: 10.1038/s41586-022-05642-9 | PMCID: PMC9946834 | PMID: 36792828
- Evidence: We numerically approximate the posterior distribution using a Hamiltonian sampling algorithm implemented in Stan 73 that is called via the software package brms 74 within the statistical programming language R 75 .
- Full pipeline: differential/statistical testing [Stan, brms] -> stage not stated [QGIS]

### Insulin-regulated serine and lipid metabolism drive peripheral neuropathy. (Nature 2023)

- DOI: 10.1038/s41586-022-05637-6 | PMCID: PMC9891999 | PMID: 36697822
- Evidence: ...ta }_{j}+{z}_{i}{u}_{j}+\,\log ({{\rm{depth}}}_{i})$$\end{document} log ( η i j ) = x i β j + z i u j + log ( depth i ) We wrote this model using the Stan probabilistic programming language 62 and fit the model using BIRDMAn ( https://github.com/gibsramen/BIRDMAn ).
- Full pipeline: read trimming [fastp, minimap2 v2.17] -> alignment/mapping [Bowtie2 v2.4.2] -> quantification [ImageJ v1.53e] -> stage not stated [QIIME 2 v2020.11, Stan]

### Compensatory evolution in NusG improves fitness of drug-resistant M. tuberculosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07206-5 | PMCID: PMC10990936 | PMID: 38509362
- Evidence: ...= β max 1 + e − H ⋅ s − M The Bayesian vulnerability model was run for each condition independently, and samples for all the parameters were obtained using Stan running 4 independent chains with 1,000 warmup iterations and 3,000 samples each (for a total of 12,000 posterior samples for each parameter in the model after discarding warmup iterations).
- Full pipeline: variant calling [GATK v3.5, SAMtools v1.7] -> quantification [ImageJ] -> differential/statistical testing [Stan] -> stage not stated [RAxML v8.2.11, freebayes v1.3.1]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Evidence: This was done by separately fitting a β-mixture model with three components to each sample using Stan 89 and extracting the component mixture probability.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: Chains were sampled using the NUTS (No-U-Turn Sampler) algorithm in Stan ( https://mc-stan.org/ ) with the brms (v.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Evidence: The model was implemented in Stan, using the cmdstanr package 61 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Increase in wild animal consumption across Central Africa. (Nature 2026)

- DOI: 10.1038/s41586-026-10422-w | PMCID: PMC13216070 | PMID: 42056525
- Version used: **2.26.11**
- Evidence: Compiling, running and checking the model We coded our model in Stan 96 and run it in R (v.4.2.0) 76 , using four chains in parallel for 5,000 (4,000 warmup) iterations each using RStan (v.2.26.11) 77 .
- Full pipeline: stage not stated [R v4.2.0, Stan v2.26.11]

### Estimating SARS-CoV-2 infections from deaths, confirmed cases, tests, and random surveys. (PNAS 2021)

- DOI: 10.1073/pnas.2103272118 | PMCID: PMC8346866 | PMID: 34312227
- Evidence: We built the model in R and fit it with the RStan software package, which implements the No-U-Turn-Sampler for Bayesian inference ( 44 – 46 ).
- Full pipeline: differential/statistical testing [Stan]

### Socioeconomic development predicts a weaker contraceptive effect of breastfeeding. (PNAS 2021)

- DOI: 10.1073/pnas.2025348118 | PMCID: PMC8307660 | PMID: 34253613
- Evidence: The metaregression model was written in Stan ( 49 ).
- Full pipeline: differential/statistical testing [Stan] -> machine learning [R]

### Monitoring the COVID-19 epidemic with nationwide telecommunication data. (PNAS 2021)

- DOI: 10.1073/pnas.2100664118 | PMCID: PMC8256040 | PMID: 34162708
- Version used: **2.19.2**
- Evidence: Parameter estimates are obtained by Markov chain Monte Carlo sampling in Stan version 2.19.2, using the Hamiltonian Monte Carlo algorithm ( 63 , 64 ) and the No-U-Turn sampler (NUTS) ( 65 ).
- Full pipeline: differential/statistical testing [R, brms] -> simulation/modelling [Stan v2.19.2]

### Combat stress in a small-scale society suggests divergent evolutionary roots for posttraumatic stress disorder symptoms. (PNAS 2021)

- DOI: 10.1073/pnas.2020430118 | PMCID: PMC8054015 | PMID: 33876754
- Evidence: Models were fitted using RStan ( 82 ) and the leave-one-out (LOO) R package ( 83 ).
- Full pipeline: stage not stated [R, Stan]

### CD4 receptor diversity represents an ancient protection mechanism against primate lentiviruses. (PNAS 2021)

- DOI: 10.1073/pnas.2025914118 | PMCID: PMC8020793 | PMID: 33771926
- Evidence: The effects of the various alleles on the infectivity of each Env, as well as an overall allele effect, was estimated by Markov chain Monte Carlo sampling using Stan ( 89 ).
- Full pipeline: simulation/modelling [Stan]

### Bayesian estimation of SARS-CoV-2 prevalence in Indiana by random testing. (PNAS 2021)

- DOI: 10.1073/pnas.2013906118 | PMCID: PMC7865174 | PMID: 33441450
- Evidence: Bayesian inference was carried out using the package RStan ( 29 ).
- Full pipeline: differential/statistical testing [Stan] -> stage not stated [tidyverse]

### A resource-rational model of human processing of recursive linguistic structure. (PNAS 2022)

- DOI: 10.1073/pnas.2122602119 | PMCID: PMC9618130 | PMID: 36260742
- Evidence: We then analyzed log-transformed reading times on the final verb using Bayesian mixed-effects models implemented in Stan ( 71 ) using brms ( 72 ).
- Full pipeline: differential/statistical testing [Stan, brms]

### Multispecies coexistence in fragmented landscapes. (PNAS 2022)

- DOI: 10.1073/pnas.2201503119 | PMCID: PMC9477233 | PMID: 36067285
- Evidence: The parameters in the Bayesian model were fitted using Stan ( 52 ).
- Full pipeline: differential/statistical testing [Stan]

### Superstitious learning of abstract order from random reinforcement. (PNAS 2022)

- DOI: 10.1073/pnas.2202789119 | PMCID: PMC9436361 | PMID: 35998221
- Evidence: Both t and D were centered at zero to decrease the slope covariances before Bayesian multilevel model fitting performed in the Stan programming language using the MCMC method ( 28 ).
- Full pipeline: differential/statistical testing [Stan]

### Crosslinguistic word order variation reflects evolutionary pressures of dependency and information locality. (PNAS 2022)

- DOI: 10.1073/pnas.2122604119 | PMCID: PMC9214541 | PMID: 35675428
- Evidence: We conducted Bayesian inference for mixed effects analyses using Hamiltonian Monte Carlo in Stan ( 101 – 103 ).
- Full pipeline: differential/statistical testing [Stan] -> simulation/modelling [Stan]

### A global analysis of tree pests and emerging pest threats. (PNAS 2022)

- DOI: 10.1073/pnas.2113298119 | PMCID: PMC9060442 | PMID: 35312373
- Evidence: The model was fit in Stan ( 49 ) and called with the brms package ( 50 ) in R.
- Full pipeline: stage not stated [Stan, brms]

### Maternally derived antibody titer dynamics and risk of hospitalized infant dengue disease. (PNAS 2023)

- DOI: 10.1073/pnas.2308221120 | PMCID: PMC10576102 | PMID: 37774093
- Evidence: All model fitting was conducted in CmdStanR version 0.3.0.
- Full pipeline: stage not stated [Stan]

### The competition dynamics of approach and avoidance motivations following interpersonal transgression. (PNAS 2023)

- DOI: 10.1073/pnas.2302484120 | PMCID: PMC10556639 | PMID: 37769254
- Evidence: Parameters were estimated using Bayesian statistical inference method in RStan ( 57 ).
- Full pipeline: differential/statistical testing [Stan]

### Diversified farms bolster forest-bird populations despite ongoing declines in tropical forests. (PNAS 2023)

- DOI: 10.1073/pnas.2303937120 | PMCID: PMC10500279 | PMID: 37669369
- Evidence: The community trend model was developed and written in the probabilistic programming language Stan, and full Bayesian inference was carried out with MCMC sampling in the Stan language (SI stanModel).
- Full pipeline: differential/statistical testing [Stan]

### Diverse mathematical knowledge among indigenous Amazonians. (PNAS 2023)

- DOI: 10.1073/pnas.2215999120 | PMCID: PMC10469040 | PMID: 37603761
- Evidence: Knower levels were inferred using the Bayesian Data Analysis model described by Lee and Sarnecka ( 67 , 68 ) implemented in Stan ( 109 ) and R ( 108 ).
- Full pipeline: differential/statistical testing [Stan] -> stage not stated [R]

### sccomp: Robust differential composition and variability analysis for single-cell data. (PNAS 2023)

- DOI: 10.1073/pnas.2203828120 | PMCID: PMC10438834 | PMID: 37549298
- Evidence: This set of sampling statements and the data (Formulae 12 – 17 ) are provided to Stan ( 23 ) to sample from a joint posterior distribution of the model parameters.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> machine learning [R] -> stage not stated [Seurat, Stan, limma, tidyverse]

### Instructed motivational states bias reinforcement learning and memory formation. (PNAS 2023)

- DOI: 10.1073/pnas.2304881120 | PMCID: PMC10401012 | PMID: 37490530
- Evidence: All models were estimated using hierarchical Bayesian modeling in the RStan package ( 84 ) (version 2.21.0) in R (version 4.1.2) with data from sample 1.
- Full pipeline: differential/statistical testing [R v4.1.2, Stan] -> stage not stated [PsychoPy v2021.2.3]

### Demographic consequences of phenological asynchrony for North American songbirds. (PNAS 2023)

- DOI: 10.1073/pnas.2221961120 | PMCID: PMC10334763 | PMID: 37399376
- Evidence: We fit all models using the R package “rstan” to interface with Stan ( 91 ) in R ( 89 ).
- Full pipeline: differential/statistical testing [R, tidyverse] -> visualisation [tidyverse] -> stage not stated [Stan, phytools]

### Repetition learning is neither a continuous nor an implicit process. (PNAS 2023)

- DOI: 10.1073/pnas.2218042120 | PMCID: PMC10119999 | PMID: 37040406
- Evidence: The analytical models were programmed in Stan ( 65 ), and all analyses were carried out using R v4.2.1 ( 66 ) and the R package rstan v2.26.13 ( 67 ).
- Full pipeline: stage not stated [R v4.2, Stan]

### Mapping the number of female sex workers in countries across sub-Saharan Africa. (PNAS 2023)

- DOI: 10.1073/pnas.2200633120 | PMCID: PMC9926247 | PMID: 36595685
- Evidence: The model was fitted using the RStan ( 37 ) and brms ( 38 , 39 ) packages.
- Full pipeline: stage not stated [R, Stan, brms]

### Substitution patterns and price response for plant-based meat alternatives. (PNAS 2024)

- DOI: 10.1073/pnas.2319016121 | PMCID: PMC11648651 | PMID: 39621919
- Evidence: All analyses were performed in Stan and R.
- Full pipeline: stage not stated [Stan]

### Bridging theory and data: A computational workflow for cultural evolution. (PNAS 2024)

- DOI: 10.1073/pnas.2322887121 | PMCID: PMC11621747 | PMID: 39556723
- Evidence: Using the Stan probabilistic programming language ( 71 ), we sample from the joint posterior distribution of μ , θ ( Fig.
- Full pipeline: stage not stated [Stan]

### Predecisional information search adaptively reduces three types of uncertainty. (PNAS 2024)

- DOI: 10.1073/pnas.2311714121 | PMCID: PMC11588055 | PMID: 39546563
- Evidence: To obtain samples from the posterior distribution of the classification model, we used a no-U-turn sampler as implemented in Stan ( 77 ).
- Full pipeline: stage not stated [Stan]

### Water quality-fisheries tradeoffs in a changing climate underscore the need for adaptive ecosystem-based management. (PNAS 2024)

- DOI: 10.1073/pnas.2322595121 | PMCID: PMC11551330 | PMID: 39467116
- Evidence: We developed a Bayesian multiple linear regression model using the rstanarm package ( 165 ) in R ( 166 ) with Stan ( 167 ) to predict hypoxic area from the cumulative TP load and the spring air temperature ( SI Appendix ).
- Full pipeline: differential/statistical testing [R, Stan, rstanarm]

### Political organization and gender predict violence in the Andean archaeological record. (PNAS 2024)

- DOI: 10.1073/pnas.2410078121 | PMCID: PMC11536129 | PMID: 39432790
- Evidence: We use the Stan modeling language and the BRMS package in the R statistical computing environment to perform our computations using Hamiltonian Markov Cain Monte Carlo methods ( 99 , 100 ).
- Full pipeline: differential/statistical testing [R, Stan] -> simulation/modelling [Stan]

### Modeling the population-level impact of a third dose of MMR vaccine on a mumps outbreak at the University of Iowa. (PNAS 2024)

- DOI: 10.1073/pnas.2403808121 | PMCID: PMC11513962 | PMID: 39401354
- Evidence: To properly incorporate parameter uncertainty, we estimated model parameters using a Bayesian inference framework based on Hamiltonian Monte Carlo in Stan ( 25 ).
- Full pipeline: differential/statistical testing [Stan] -> simulation/modelling [Stan] -> stage not stated [R]

### Microevolutionary change in wild stickleback: Using integrative time-series data to infer responses to selection. (PNAS 2024)

- DOI: 10.1073/pnas.2410324121 | PMCID: PMC11406292 | PMID: 39231210
- Evidence: All models were fit using Stan via the brms package in R statistical environment (version 4.1.2) ( 69 ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> differential/statistical testing [R, Stan, brms] -> stage not stated [ImageJ]

### A quantitative model of temperature-dependent diapause progression. (PNAS 2024)

- DOI: 10.1073/pnas.2407057121 | PMCID: PMC11388385 | PMID: 39196619
- Evidence: We performed all modeling using Bayesian methods in Stan ( 57 ), via the package brms ( 58 ) in R [version 4.1.3; R Core Team ( 59 )].
- Full pipeline: differential/statistical testing [R, Stan, brms] -> stage not stated [tidyverse]

### The neural basis of swap errors in working memory. (PNAS 2024)

- DOI: 10.1073/pnas.2401032121 | PMCID: PMC11331092 | PMID: 39102534
- Evidence: As for the behavioral model, we fit this model using HMC in Stan.
- Full pipeline: stage not stated [Psychtoolbox, Stan, scikit-learn]

### Indigenous food production in a carbon economy. (PNAS 2024)

- DOI: 10.1073/pnas.2317686121 | PMCID: PMC11317563 | PMID: 39074272
- Version used: **2.32.5**
- Evidence: We used the R statistical computing environment (4.3.2) ( 53 ), Stan (2.32.2) ( 54 ), RStan (v2.32.5) ( 55 ), and the rethinking package (2.40) ( 56 ) for analysis.
- Full pipeline: differential/statistical testing [R, Stan v2.32.5]

### Multiple evolutionary pressures shape identical consonant avoidance in the world's languages. (PNAS 2024)

- DOI: 10.1073/pnas.2316677121 | PMCID: PMC11228491 | PMID: 38917001
- Version used: **2.26.13**
- Evidence: Models were fitted using RStan version 2.26.13 ( 100 ), running the No U-Turn Sampler (NUTS) over 4 chains for 2,000 iterations, with the first half discarded as burn-in.
- Full pipeline: stage not stated [Python, R, Stan v2.26.13, phytools]

### Inferring COVID-19 testing and vaccination behavior from New Jersey testing data. (PNAS 2024)

- DOI: 10.1073/pnas.2314357121 | PMCID: PMC11047110 | PMID: 38630720
- Evidence: Both these steps utilize an MCMC fitting procedure implemented in RStan ( 63 ).
- Full pipeline: stage not stated [Stan]

### Improved RNA stability estimation through Bayesian modeling reveals most <i>Salmonella</i> transcripts have subminute half-lives. (PNAS 2024)

- DOI: 10.1073/pnas.2308814121 | PMCID: PMC10998600 | PMID: 38527194
- Evidence: Subsequently, we fitted a Bayesian statistical model to the normalized data using Hamiltonian Monte Carlo with Stan ( 29 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [Cutadapt v4.1, HTSeq] -> quantification [HTSeq] -> normalisation [Stan] -> differential/statistical testing [GSEA, Stan] -> simulation/modelling [Stan] -> stage not stated [R, edgeR, limma]

### Women's subsistence strategies predict fertility across cultures, but context matters. (PNAS 2024)

- DOI: 10.1073/pnas.2318181121 | PMCID: PMC10907265 | PMID: 38346210
- Evidence: All analyses were run in R using the RStan package, which fits Bayesian mixed-effect models (accounting for population random effects) using Hamiltonian Markov chain Monte Carlo (MCMC), assessed using standard diagnostics (number of effective samples, the Gelman–Rubin diagnostic, and visual inspection of trace plots).
- Full pipeline: differential/statistical testing [Stan] -> simulation/modelling [Stan]

### Societal determinants of flood-induced displacement. (PNAS 2024)

- DOI: 10.1073/pnas.2206188120 | PMCID: PMC10801835 | PMID: 38190537
- Evidence: To this end, we rely on in-sample and out-of-sample prediction using NB regression with Bayesian inference via the Bayesian Regression Models using Stan (BRMS) package in R ( 89 ).
- Full pipeline: differential/statistical testing [R, Stan]

### Pollen nutrition structures bee and plant community interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2317228120 | PMCID: PMC10801918 | PMID: 38190523
- Evidence: We conducted Bayesian analyses using the R package “ rethinking” ( 94 ) which uses “ Stan” ( 95 ) and Hamilton MCMC to determine posterior distributions.
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [Stan] -> stage not stated [phytools]

### Complex multiannual cycles of &lt;i&gt;Mycoplasma pneumoniae&lt;/i&gt;: Persistence and the role of stochasticity. (PNAS 2025)

- DOI: 10.1073/pnas.2509184122 | PMCID: PMC12771566 | PMID: 41428876
- Evidence: Convergence was assessed based on the absence of diagnostic warnings from CmdStanPy ( 84 ), including the absence of divergent chains, no exceedances of tree-depth, sufficient E-BFMI ( > 0.3), and satisfactory R ^ ( < 1.05) and effective sample size (bulk ESS > 100 × # chains ) for all parameters.
- Full pipeline: stage not stated [Stan]

### China's post-zero-COVID Omicron wave: A Bayesian analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2514157122 | PMCID: PMC12685082 | PMID: 41289400
- Evidence: The model was fitted in a Bayesian framework using the No-U-Turn sampler via the RStan package ( 35 ).
- Full pipeline: differential/statistical testing [Stan]

### Morphological specializations of mosquito CO&lt;sub&gt;2&lt;/sub&gt;-sensing olfactory receptor neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2514666122 | PMCID: PMC12582328 | PMID: 41129220
- Evidence: Posterior distributions were estimated using MCMC sampling in Stan (Stan Development Team, 2024.
- Full pipeline: alignment/mapping [IMOD] -> machine learning [R] -> visualisation [tidyverse] -> stage not stated [ImageJ, SciPy, Stan]

### Data-driven equation discovery reveals nonlinear reinforcement learning in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2413441122 | PMCID: PMC12337339 | PMID: 40743390
- Evidence: To address this possibility, we next used the probabilistic programming language Stan ( 49 ) for individual-level model fitting, allowing us to assess the generalizability of the model and estimate participant-specific parameters.
- Full pipeline: stage not stated [Stan, jsPsych]

### The evolution of male-female dominance relations in primate societies. (PNAS 2025)

- DOI: 10.1073/pnas.2500405122 | PMCID: PMC12280975 | PMID: 40623178
- Evidence: We used functions of the package “rethinking” ( 53 ) to write the models to estimate associations between intersexual dominance and the respective predictor variables with Markov Chain Monte Carlo procedures in Stan ( 76 ).
- Full pipeline: differential/statistical testing [R v4.2.2, phytools] -> simulation/modelling [Stan, phytools]

### Forecasting range shifts of dioecious plants under climate change. (PNAS 2025)

- DOI: 10.1073/pnas.2422162122 | PMCID: PMC12130872 | PMID: 40392855
- Evidence: All models were fit using Stan ( 49 ) in R 4.3.1 ( 50 ).
- Full pipeline: stage not stated [R v4.3, Stan]

### Global warming drives a threefold increase in persistence and 1 &lt;sup&gt;°&lt;/sup&gt;C rise in intensity of marine heatwaves. (PNAS 2025)

- DOI: 10.1073/pnas.2413505122 | PMCID: PMC12037066 | PMID: 40228120
- Evidence: The statistical model has been implemented in Stan ( 33 ), a state-of-the-art probabilistic programming language that provides Bayesian statistical inference with MCMC sampling.
- Full pipeline: differential/statistical testing [Stan]

### Day-to-day fluctuations in motivation drive effort-based decision-making. (PNAS 2025)

- DOI: 10.1073/pnas.2417964122 | PMCID: PMC11962463 | PMID: 40096607
- Version used: **2.33.1**
- Evidence: Hierarchical generative modeling was conducted separately on a high-performance computer with R version 4.3.2 and models fitted in Stan version 2.33.1.
- Full pipeline: stage not stated [R v4.1.0, Stan v2.33.1]

### eDNA confirms lower trophic interactions help to modulate population outbreaks of the notorious crown-of-thorns sea star. (PNAS 2025)

- DOI: 10.1073/pnas.2424560122 | PMCID: PMC11929471 | PMID: 40063810
- Evidence: The Bayesian SEM was developed using the blavaan package, which relies on JAGS and Stan to estimate models via Markov Chain Monte Carlo simulation ( 77 ).
- Full pipeline: differential/statistical testing [JAGS, R v4.1, Stan] -> simulation/modelling [JAGS, Stan] -> stage not stated [emmeans]

### Automating the practice of science: Opportunities, challenges, and implications. (PNAS 2025)

- DOI: 10.1073/pnas.2401238121 | PMCID: PMC11804648 | PMID: 39869810
- Evidence: For example, modern statistical inference engines, like Stan, leverage techniques such as Markov Chain Monte Carlo (MCMC) for efficient sampling of model parameters ( 69 ).
- Full pipeline: differential/statistical testing [Stan] -> simulation/modelling [Stan] -> stage not stated [AlphaFold]

### An inverse correlation between structural linguistic and human genetic diversity. (PNAS 2026)

- DOI: 10.1073/pnas.2526762123 | PMCID: PMC13142977 | PMID: 42066044
- Evidence: As the response variable of our main models, again implemented in the brms ( 81 ) interface to Stan ( 82 , 83 ), we used the logit-transformed posterior mean entropies per grid cell [ logit ( H n i ) ] and the corresponding SD of these estimates [ sd ( logit ( H n i ) ] from the features of TLI (N = 333) and GBI (N = 196) separately, for each of the original and the jittered language coordinates.
- Full pipeline: variant calling [PLINK v1.9] -> stage not stated [R, Stan, brms]

### Dynamical modeling of individual sensory reactivity and habituation learning. (PNAS 2026)

- DOI: 10.1073/pnas.2524738123 | PMCID: PMC13037877 | PMID: 41894333
- Evidence: We fit the model described in the preceding section to individual fly data using Stan ( 59 ), a probabilistic programming framework that performs Bayesian modeling and inference via Hamiltonian Monte Carlo (HMC).
- Full pipeline: differential/statistical testing [Python v3.10, Stan] -> simulation/modelling [Stan]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Evidence: This analysis was implemented in Stan ( 72 ), as described in ( 97 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Age groups that sustain resurging COVID-19 epidemics in the United States. (Science 2021)

- DOI: 10.1126/science.abe8372 | PMCID: PMC8101272 | PMID: 33531384
- Version used: **2.23.0**
- Evidence: The contact-and-infection model was fit with CmdStan release 2.23.0 (22 April 2020), using an adaptive Hamiltonian Monte Carlo (HMC) sampler ( 42 ).
- Full pipeline: simulation/modelling [Stan v2.23.0]

