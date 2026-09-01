# metafor

- **Category:** general
- **Papers in survey:** 45
- **Journals:** PNAS (33), Nature (10), Lancet (2)
- **Years:** 2021 (1), 2022 (5), 2023 (10), 2024 (11), 2025 (14), 2026 (4)
- **Versions named:** 4.6 (2), 4.6.0 (1), 4.0.0 (1), 3.8 (1), 3.0 (1), 2.4 (1)
- **Pipeline stages it appears in:** differential/statistical testing (10)

## Papers

### Past SARS-CoV-2 infection protection against re-infection: a systematic review and meta-analysis. (Lancet 2023)

- DOI: 10.1016/s0140-6736(22)02465-5 | PMCID: PMC9998097 | PMID: 36930674
- Evidence: 27 Tidyverse, data.table, stringi, ggplot2, forestplot, formattable, crosswalk002, metafor, and mrbrt002 packages were used.
- Full pipeline: stage not stated [R v1.4.1103, data.table, ggplot2, metafor]

### Antivirals for post-exposure prophylaxis of influenza: a systematic review and network meta-analysis. (Lancet 2024)

- DOI: 10.1016/s0140-6736(24)01357-6 | PMCID: PMC11369964 | PMID: 39181596
- Evidence: We performed pairwise meta-analysis using the meta and metafor packages of R version 4.0.2.
- Full pipeline: stage not stated [R v4.0.2, metafor]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: Meta-analyses Meta-analyses to compare and aggregate effect sizes and confidence intervals from multiple cohorts were performed in R using the metafor 70 package with an inverse variance weighted fixed effects model.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### Biodiversity impacts of the 2019-2020 Australian megafires. (Nature 2024)

- DOI: 10.1038/s41586-024-08174-6 | PMCID: PMC11602714 | PMID: 39537920
- Evidence: Effect sizes for these datasets were calculated as the standardized mean change (mean-after minus mean-before) using change score standardization (SMCC, using SMCC option in escalc function of R package metafor) 63 – 65 , which accommodates the expected non-independence of repeated measures of the same sites 65 .
- Full pipeline: stage not stated [R, metafor]

### Environmental drivers of increased ecosystem respiration in a warming tundra. (Nature 2024)

- DOI: 10.1038/s41586-024-07274-7 | PMCID: PMC11062900 | PMID: 38632407
- Evidence: Modelling approach Meta-analysis To evaluate the effects of experimental warming on ER, we performed multivariate meta-analysis with the rma.mv function from the metafor R package 73 , using the Hedges’ SMD of the growing season average ER data as primary effect size (Fig.
- Full pipeline: stage not stated [R, ggplot2, metafor]

### Latitudinal patterns in stabilizing density dependence of forest communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07118-4 | PMCID: PMC10954553 | PMID: 38418889
- Evidence: Models were fitted with REML using the functions rma.mv() and rma() from the package metafor 70 (v.3.4-0) for the global and site-specific cases, respectively.
- Full pipeline: stage not stated [metafor]

### Timing and trajectory of BCR::ABL1-driven chronic myeloid leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-08817-2 | PMCID: PMC12018454 | PMID: 40205062
- Evidence: The cohort level analysis of mutational signatures and C>T at CpG representation for branch categories was carried out using a random effects meta-analysis using the rma function in the ‘metafor’ R package.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [R, lme4, metafor]

### Vulnerability of amphibians to global warming. (Nature 2025)

- DOI: 10.1038/s41586-025-08665-0 | PMCID: PMC11946914 | PMID: 40044855
- Evidence: Climate vulnerability analysis Using the imputed data, we fitted an individual meta-analytic model for each species to estimate the plasticity of imputed heat-tolerance limits (CT max ) to changes in operative body temperatures using the metafor package 98 (v.4.2-0).
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [R, brms] -> visualisation [ggplot2] -> stage not stated [lme4 v1.1, metafor]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **4.6**
- Evidence: ...ers were estimated using mixed-effects meta-analysis with restricted maximum likelihood (REML) criterion, implemented via the rma.uni function of the metafor (v4.6-0) package 239 , integrating study-level mean and standard error estimates of ln( A ) and r .
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Evidence: The resulting HRs and their associated standard errors were pooled across datasets within each cancer type, and across cancer types, using a nested random-effects meta-analysis implemented in the rma.mv function of the metafor R package 107 (v.4.8.0), with default parameters.
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: Meta-analyses across datasets were computed with the metafor R package 80 using a random-effects model and the DerSimonian–Laird estimator.
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **4.6.0**
- Evidence: To conduct meta-analyses on mutational differential gene expression, we used the metafor (v.4.6.0) package by fitting a fixed-effect model with the rma function for each time point 124 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Asymptomatic SARS-CoV-2 infection: A systematic review and meta-analysis. (PNAS 2021)

- DOI: 10.1073/pnas.2109229118 | PMCID: PMC8403749 | PMID: 34376550
- Evidence: Meta-analyses of sex-based and comorbidity-based differences in asymptomaticity were performed using the rma function from the R package metafor.
- Full pipeline: stage not stated [R, metafor]

### Complex agricultural landscapes host more biodiversity than simple ones: A global meta-analysis. (PNAS 2022)

- DOI: 10.1073/pnas.2203385119 | PMCID: PMC9499564 | PMID: 36095174
- Evidence: We used the metafor R package and a three-level meta-analytic random-effects model for dealing with effect size dependency since multiple effect sizes can come from the same article ( 108 – 111 ).
- Full pipeline: stage not stated [R, metafor]

### A quantitative synthesis of soil microbial effects on plant species coexistence. (PNAS 2022)

- DOI: 10.1073/pnas.2122088119 | PMCID: PMC9295794 | PMID: 35605114
- Evidence: 4 and 5 ) using metafor::rma.mv ( 93 ): rma . mv ( y ∼ EffectType , random = list ( ∼ EffectType ∣ Experiment _ ID , ∼ EffectType ∣ SpeciesPair _ Experiment _ ID ) , V = VarianceCovarianceMatrix , struct = “ UN ” ) The model included a fixed effect for the effect size type (stabilization/fitness differences).
- Full pipeline: stage not stated [metafor]

### Sublethal effects of parasitism on ruminants can have cascading consequences for ecosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2117381119 | PMCID: PMC9171767 | PMID: 35533278
- Evidence: Using the metafor package, we converted all directional r into Fisher’s Z ( Z r ) ( 97 ).
- Full pipeline: stage not stated [R, metafor]

### Emergent effects of global change on consumption depend on consumers and their resources in marine systems. (PNAS 2022)

- DOI: 10.1073/pnas.2108878119 | PMCID: PMC9173678 | PMID: 35446691
- Version used: **2.4**
- Evidence: All data manipulation and analyses were conducted using the statistical software, R (version 3.6.2) ( 60 ), with the associated packages tidyverse (version 1.3.0) ( 61 ) and metafor (version 2.4–0) ( 62 ).
- Full pipeline: differential/statistical testing [R v3.6.2, metafor v2.4, tidyverse v1.3.0]

### The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. (PNAS 2022)

- DOI: 10.1073/pnas.2107346118 | PMCID: PMC8740589 | PMID: 34983836
- Evidence: All analyses were conducted in R using the package metafor ( 80 ).
- Full pipeline: stage not stated [metafor]

### Similar photosynthetic but different yield responses of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; crops to elevated O&lt;sub&gt;3&lt;/sub&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2313591120 | PMCID: PMC10655586 | PMID: 37948586
- Version used: **3.8**
- Evidence: We calculated mean effect sizes of elevated [O 3 ] and their CIs using the rma.mv function of the R package metafor (version 3.8-1) ( 81 ) with studies nested in species or cultivars as random effects.
- Full pipeline: stage not stated [R, metafor v3.8]

### Changes in patterns of age-related network connectivity are associated with risk for schizophrenia. (PNAS 2023)

- DOI: 10.1073/pnas.2221533120 | PMCID: PMC10410767 | PMID: 37527347
- Evidence: To extract reproducible FNC × PRS associations across all cohorts, we performed a mixed-effect model meta-analysis derived from partial regressions between FNC and PRS across cohorts through the metafor R package ( 100 ).
- Full pipeline: differential/statistical testing [R, metafor]

### Restoring particulate and mineral-associated organic carbon through regenerative agriculture. (PNAS 2023)

- DOI: 10.1073/pnas.2217481120 | PMCID: PMC10214150 | PMID: 37186829
- Evidence: We estimated the effect size of SOC, MAOC, and POC for tillage treatment, cropping intensification, and ICL using the metafor package ( 63 ) in R ver 4.2.1.
- Full pipeline: stage not stated [R, metafor]

### Cultural threat perceptions predict violent extremism via need for cognitive closure. (PNAS 2023)

- DOI: 10.1073/pnas.2213874120 | PMCID: PMC10194010 | PMID: 37155886
- Evidence: First, we separately pooled all correlations between all variables in the model using the metafor package for R ( 85 ), and then we fitted a mediation model with a latent outcome to the matrix of pooled correlations using the metasem package for R ( 86 ).
- Full pipeline: stage not stated [metafor]

### The effect of climate change on avian offspring production: A global meta-analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2208389120 | PMCID: PMC10175715 | PMID: 37126701
- Evidence: 4 ) were run using R package “metafor”, version 3.4 ( 54 ).
- Full pipeline: stage not stated [QGIS, R v4.2.2, metafor]

### Large-scale analysis of structural brain asymmetries in schizophrenia via the ENIGMA consortium. (PNAS 2023)

- DOI: 10.1073/pnas.2213880120 | PMCID: PMC10083554 | PMID: 36976765
- Version used: **3.0**
- Evidence: S2–S4 ), effect sizes for diagnosis from each case–control dataset were meta-analyzed in a random-effects model fitted with a restricted maximum likelihood estimator, using the function “rma” in the R package metafor (v3.0-2) ( 66 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [FreeSurfer, ggplot2, metafor v3.0]

### Field interventions for climate change mitigation behaviors: A second-order meta-analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2214851120 | PMCID: PMC10068847 | PMID: 36943888
- Evidence: We used the “metafor” ( 85 ) package for creating the funnel and forest plots.
- Full pipeline: stage not stated [metafor]

### Trends in racial and ethnic discrimination in hiring in six Western countries. (PNAS 2023)

- DOI: 10.1073/pnas.2212875120 | PMCID: PMC9963383 | PMID: 36719918
- Evidence: We estimate the models using the “metafor” package in the R statistical language ( 63 ) with procedures from Pustejovsky and Tipton ( 55 ) to estimate the subgroup correlated effects models.
- Full pipeline: differential/statistical testing [metafor]

### Ecology and life history predict avian nest success in the global tropics. (PNAS 2024)

- DOI: 10.1073/pnas.2402652121 | PMCID: PMC11621757 | PMID: 39556725
- Evidence: To investigate whether our predictors are correlated with one another, which can affect the precision with which model parameters are estimated, we calculated variance inflation factors (VIFs) using the metafor R package.
- Full pipeline: stage not stated [R, metafor, phytools]

### Ecological restoration enhances dryland carbon stock by reducing surface soil carbon loss due to wind erosion. (PNAS 2024)

- DOI: 10.1073/pnas.2416281121 | PMCID: PMC11573679 | PMID: 39514308
- Evidence: We calculated the weighted response ratio (ln RR ++ ) and bias-corrected 95% bootstrap-CI using the “metafor” package in R ( 51 ).
- Full pipeline: stage not stated [R, lavaan, metafor]

### Rapid growth and the evolution of complete metamorphosis in insects. (PNAS 2024)

- DOI: 10.1073/pnas.2402980121 | PMCID: PMC11420152 | PMID: 39250668
- Evidence: The models were phylogenetic linear mixed-effects models ( 43 ) using the rma.mv function from the R package metafor ( 60 ) that incorporates sampling variance (the square of SE).
- Full pipeline: differential/statistical testing [metafor] -> stage not stated [R]

### Heterogeneity in effect size estimates. (PNAS 2024)

- DOI: 10.1073/pnas.2403490121 | PMCID: PMC11317577 | PMID: 39078672
- Evidence: Random effects meta-analyses were estimated using the metafor package (v-4.4.0) ( 109 ) in R (v-4.3.2) ( 110 ).
- Full pipeline: stage not stated [R, metafor]

### Significant shifts in latitudinal optima of North American birds. (PNAS 2024)

- DOI: 10.1073/pnas.2307525121 | PMCID: PMC11009622 | PMID: 38557189
- Evidence: We used the rma.mv function in the R package metafor ( 98 ) and included two random factors associated with individual species’ identities: One was an independent species effect, and the other explicitly incorporated phylogenetic correlations among species.
- Full pipeline: stage not stated [R, ape (R), metafor, phytools]

### Deforestation impacts soil biodiversity and ecosystem services worldwide. (PNAS 2024)

- DOI: 10.1073/pnas.2318475121 | PMCID: PMC10990143 | PMID: 38466879
- Evidence: The entire meta-regression and model selection analyses were conducted using glmulti ( 45 ) and metafor ( 46 ) packages in R (v.4.1.2).
- Full pipeline: differential/statistical testing [R v4.1.2, metafor] -> stage not stated [vegan]

### White Americans' preference for Black people in advertising has increased in the past 66 y: A meta-analysis. (PNAS 2024)

- DOI: 10.1073/pnas.2307505121 | PMCID: PMC10907232 | PMID: 38377190
- Evidence: All analyses were conducted in R using the package metafor ( 102 ). [2] E S ij = β 0 + ( ∑ k = 1 K β k E k , i j ) + ( ∑ l = 1 L β K + l S l , j ) + e ij + s j + a ij .
- Full pipeline: stage not stated [metafor]

### Climate sensitivity is widely but unevenly spread across zoonotic diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2422851122 | PMCID: PMC12718308 | PMID: 41364762
- Evidence: To each plot, we applied Egger’s regression test from the {metafor} package ( 91 ) to check for significant asymmetry, indicating potential publication bias.
- Full pipeline: differential/statistical testing [R, metafor]

### Precipitation increase promotes soil organic carbon formation and stability via the mycorrhizal fungal pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2519072122 | PMCID: PMC12685053 | PMID: 41289393
- Evidence: The effect size for each observation was calculated as the natural log of the response ratio (RR) using the escalc function in the R package “metafor”: [1] ln RR = ln ( X t / X c ) , where X t and X c represent the mean values of the variables under Pi and control conditions, respectively.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, metafor, pheatmap, vegan]

### Elevated risk of infectious diseases in adulthood after prenatal or early postnatal exposure to the Great Chinese Famine. (PNAS 2025)

- DOI: 10.1073/pnas.2513421122 | PMCID: PMC12685027 | PMID: 41284860
- Version used: **4.0.0**
- Evidence: All analyses were conducted using R 4.3.1, with packages tidyverse 2.0.0 ( 62 ) for data processing, INLA 23.04.24 ( 63 ) for fitting BAPC models, mgcv 1.8.42 ( 64 ) for fitting GAMs, metafor 4.0.0 ( 65 ) for fitting meta-regression models, foreach 1.5.2 ( 66 ) and doSNOW 1.0.20 ( 67 ) for parallel computation, and ggplot2 3.4.1 ( 68 ), tmap 3.3.3 ( 69 ), cowplot 1.1.1 ( 70 ), and ggsci 3.0.0 ( 71...
- Full pipeline: differential/statistical testing [R v4.3, ggplot2 v3.4.1, metafor v4.0.0, tidyverse v2.0.0] -> visualisation [ggplot2 v3.4.1]

### Overestimated natural biological nitrogen fixation translates to an exaggerated CO&lt;sub&gt;2&lt;/sub&gt; fertilization effect in Earth system models. (PNAS 2025)

- DOI: 10.1073/pnas.2514628122 | PMCID: PMC12685054 | PMID: 41284886
- Evidence: The weighted average and 95% CI of ln RR i for a given magnitude of CO 2 enrichment were calculated using the standard inverse-variance method and restricted maximum likelihood estimation using the R package “metafor” ( 58 ).
- Full pipeline: stage not stated [R, metafor]

### Small spaces have large impacts: Microsites determine plant litter decomposition rates in drylands. (PNAS 2025)

- DOI: 10.1073/pnas.2503852122 | PMCID: PMC12663943 | PMID: 41252155
- Evidence: We carried out meta-analyses using the metafor package ( 88 ) in R ( 89 ), calculating effect sizes from litter mass remaining as log response ratios in which we contrasted mass remaining for surface litter in open microsites with that of the previously defined microsite contrasts.
- Full pipeline: stage not stated [R, metafor]

### Meta-analysis finds large variation but no general patterns in the relationship between climate and parasitism in terrestrial animals. (PNAS 2025)

- DOI: 10.1073/pnas.2508970122 | PMCID: PMC12519196 | PMID: 41021800
- Evidence: We conducted analyses in R version 4.2.0 ( 64 ) using RStudio “Prairie Trillium” ( 65 ) the package “metafor” version 4.4.0 ( 66 ).
- Full pipeline: stage not stated [R v4.2.0, ggplot2, metafor]

### Rising global temperatures reduce soil microbial diversity over the long term. (PNAS 2025)

- DOI: 10.1073/pnas.2426200122 | PMCID: PMC12415293 | PMID: 40854119
- Evidence: Further, there is no publication bias in our meta-analysis models ( SI Appendix , Table S10 ) based on Egger’s test using metafor package ( 66 ).
- Full pipeline: stage not stated [R, lme4, metafor]

### Sustained benefits of long-term biochar application for food security and climate change mitigation. (PNAS 2025)

- DOI: 10.1073/pnas.2509237122 | PMCID: PMC12377759 | PMID: 40789038
- Evidence: The meta-analysis was conducted in R using the “rma.mv” function of the “metafor” package, which is designed for multivariate/multilevel meta-analysis and empowers the modeling of complex dependency structures in meta-analytic data.
- Full pipeline: stage not stated [R, metafor]

### A meta-analysis of the effectiveness of gratitude interventions on well-being across cultures. (PNAS 2025)

- DOI: 10.1073/pnas.2425193122 | PMCID: PMC12280877 | PMID: 40627390
- Version used: **4.6**
- Evidence: We conducted the meta-analysis in R using the following R packages: metafor (version 4.6-0) ( 70 ), weightr (version 2.0.2) ( 71 ), PublicationBias (version 2.4.0) ( 72 ), and glmulti (version 1.0.8) ( 73 ).
- Full pipeline: stage not stated [metafor v4.6]

### X and Y gene dosage effects are primary contributors to human sexual dimorphism: The case of height. (PNAS 2025)

- DOI: 10.1073/pnas.2503039122 | PMCID: PMC12146736 | PMID: 40388606
- Evidence: The results for each sex chromosome complement comparison for each ancestry group were then meta-analyzed across cohorts using a fixed-effects model in metafor ( 61 ).
- Full pipeline: stage not stated [metafor]

### Positive effects of species mixing on biodiversity of understory plant communities and soil health in forest plantations. (PNAS 2025)

- DOI: 10.1073/pnas.2418090122 | PMCID: PMC11929463 | PMID: 40080637
- Evidence: To evaluate the impact of species mixing on understory plant communities and soil in forest plantations, we applied a multilevel mixed-effects meta-analysis with the “rma.mv” function from the “metafor” package ( 82 ).
- Full pipeline: differential/statistical testing [metafor]

### A global estimate of multiecosystem photosynthesis losses under microplastic pollution. (PNAS 2025)

- DOI: 10.1073/pnas.2423957122 | PMCID: PMC11929485 | PMID: 40063820
- Evidence: The meta-analysis was conducted with RStudio in R version 4.0.3 with the “meta”, “metafor”, “lme4”, “nlme”, “ggplot2,” and “multcomp” packages.
- Full pipeline: stage not stated [Python v3.8.8, R v4.0.3, ggplot2, lme4, metafor, scikit-learn v1.2.2]

