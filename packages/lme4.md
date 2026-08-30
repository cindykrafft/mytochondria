# lme4

- **Category:** general
- **Papers in survey:** 312
- **Journals:** PNAS (239), Nature (64), Science (5), Lancet (2), Cell (2)
- **Years:** 2021 (28), 2022 (61), 2023 (46), 2024 (73), 2025 (79), 2026 (25)
- **Versions named:** 1.1 (28), 3.1 (5), 1.1.27.1 (2), 1.1.26 (2), 1.1.35.3 (1), 1.1.32 (1), 3.1.3 (1)
- **Pipeline stages it appears in:** differential/statistical testing (165), quantification (9), normalisation (4), visualisation (4), dimensionality reduction/clustering (3), variant calling (3), simulation/modelling (2), machine learning (2), alignment/mapping (1)

## Papers

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Version used: **1.1**
- Evidence: ...oconductor.org/packages/release/bioc/html/edgeR.html FGSEA (1.10.1) Sergushichev, 2016 https://bioconductor.org/packages/release/bioc/html/fgsea.html lme4 (1.1-23) Bates et al., 2015 https://cran.r-project.org/web/packages/lme4/index.html lmerTest Kuznetsova et al., 2017 https://cran.r-project.org/web/packages/lmerTest/index.html plsRglm (1.2.5) Bertrand and Maumy-Bertrand, 2019 https://cran.r-pro...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: ... package) https://cran.r-project.org/web/packages/uwot/index.html v0.1.8 (CRAN) ComplexHeatmap (R package) ( Gu et al., 2016 ) v1.20.0 (Bioconductor) lme4 (R package) ( Nowicka et al., 2017 ) v1.1-21 (CRAN) multcomp (R package) ( Hothorn et al., 2008 ) v1.4-13 (CRAN) lsmeans (R package) ( Lenth, 2016 ) v2.30-0 (CRAN) phenoptr (R package) ( Johnson, 2021 ) v0.2.9 https://github.com/akoyabio/phenopt...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Patient care and clinical outcomes for patients with COVID-19 infection admitted to African high-care or intensive care units (ACCCOS): a multicentre, prospective, observational cohort study. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00441-4 | PMCID: PMC8137309 | PMID: 34022988
- Evidence: A three-level random-intercept mixed effects logistic regression was done on each of the five imputed datasets using the glmer function in the lme4 package 13 in R.
- Full pipeline: differential/statistical testing [lme4]

### Global variation in postoperative mortality and complications after cancer surgery: a multicentre, prospective cohort study in 82 countries. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00001-5 | PMCID: PMC7846817 | PMID: 33485461
- Evidence: All analyses were done using R (version 3.6.3), using the finalfit, tidyverse, and lme4.
- Full pipeline: stage not stated [R v3.6.3, lme4, tidyverse]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: The ‘glmer’ function in the lme4 package implemented on R was used to fit the model.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: We then fit a mixed effects linear model to these data in lme4 92 in which the chromosome number (1–9) was a random effect, to test the main effect of subgenome.
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: This regressed dataset was created with the ‘lmerTest’ 55 package in R through subtracting the effects of technical covariates and all biological covariates other than subject, diagnosis, and region from each gene, leaving only the random intercept, these three remaining biological covariate effects, and the residual.
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### Light competition drives herbivore and nutrient effects on plant diversity. (Nature 2022)

- DOI: 10.1038/s41586-022-05383-9 | PMCID: PMC9646529 | PMID: 36323777
- Evidence: We simplified the models using the anova() function for model comparison in the nlme and lme4 packages in R (ref.
- Full pipeline: stage not stated [R, lme4]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Evidence: The linear mixed-effects models were built with lmer from the lme4 R package v.1.1-28 (ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### Sufficient conditions for rapid range expansion of a boreal conifer. (Nature 2022)

- DOI: 10.1038/s41586-022-05093-2 | PMCID: PMC9385489 | PMID: 35948635
- Evidence: However, because both the relative solar elevation and snow depth vary with terrain, we used a linear mixed-effects model (lmer() in the lme4 R package 61 ) of height on shadow length (random factor of sample area with six levels), interpreting the fixed-effects intercept as the average snow depth (mean ± s.e. = 2.84 ± 0.14 m, t = 20.29) and the regression coefficient as the average tangent of sol...
- Full pipeline: alignment/mapping [R] -> differential/statistical testing [lme4]

### Clonal dynamics of haematopoiesis across the human lifespan. (Nature 2022)

- DOI: 10.1038/s41586-022-04786-y | PMCID: PMC9177428 | PMID: 35650442
- Evidence: Subsequently, linear mixed effects models were used to test for a linear relationship between age and number of SNVs or number of indels (function lmer, R package lme4).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R, lme4]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Evidence: Linear mixed effects models were analysed using lmerTest R package (3.1.3).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### Human mobility networks reveal increased segregation in large cities. (Nature 2023)

- DOI: 10.1038/s41586-023-06757-3 | PMCID: PMC10733138 | PMID: 38030732
- Evidence: ...emargin}{-69pt} \begin{document}$${\rm{Var}}\left({{\epsilon }}_{i}^{(1)}\right)$$\end{document} Var ϵ i ( 1 ) by fitting the mixed model using the R lme4 package, optimizing the restricted maximum-likelihood (REML) objective.
- Full pipeline: stage not stated [SciPy, lme4]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Version used: **1.1**
- Evidence: In the reanalysis of TwinsUK data, we fitted generalized linear mixed-effects models with age, sex, zygosity and BMI as fixed effects and sample collection year as a random effect using the function glmer of R package lme4 v.1.1-27.1 to estimate the associations between HOMA-IR and faecal carbohydrate metabolites (Extended Data Fig.
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### Native diversity buffers against severity of non-native tree invasions. (Nature 2023)

- DOI: 10.1038/s41586-023-06440-7 | PMCID: PMC10533391 | PMID: 37612513
- Evidence: 4.2.2) 115 using lme4 116 , lmerTest 117 , and betareg 118 , while visualizations for these models used ggplot2 119 ; tidyverse 95 was used throughout as well.
- Full pipeline: visualisation [ggplot2, lme4] -> stage not stated [QGIS, R, tidyverse]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Evidence: To quantify the experimental variation induced by the experimental run, library preparation and sequencing, and to remove unwanted batch effects, we first used the lmer function of the lme4 package (v.1.1-27.1) 75 to fit a linear model of the following form in each stimulation condition and for each lineage/cell type: 1 log ( 1 + C P M i ) = α + I I D i + L I B i + R U N i + F L O W i + ε i where ...
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### No evidence for magnetic field effects on the behaviour of Drosophila. (Nature 2023)

- DOI: 10.1038/s41586-023-06397-7 | PMCID: PMC10432270 | PMID: 37558871
- Evidence: ...usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\begin{array}{l}{\rm{fly.lme}}={\rm{lmerTest::lmer}}({\rm{Ycm}} \sim {\rm{Exposure}}\\ \,\times \,{\rm{condition}}+(1|{\rm{ID}})+(1|{\rm{trial}}/{\rm{frame}}),{\rm{data}}={\rm{df}},\\ \,{\rm{na.action}}={\rm{na.exclude}})\end{array}$$\end{document} fly.lme = lmerTest::lmer ( Ycm ~ Expo...
- Full pipeline: differential/statistical testing [R] -> stage not stated [lme4]

### The illusion of moral decline. (Nature 2023)

- DOI: 10.1038/s41586-023-06137-x | PMCID: PMC10284688 | PMID: 37286595
- Evidence: Analysis To analyse the data, we fit a linear mixed effects model using the lme4 package in R 30 , extracted P values using the lmerTest package 31 and calculated planned contrasts using the emmeans package 32 , using a Holm–Bonferroni correction for multiple comparisons.
- Full pipeline: differential/statistical testing [emmeans, lme4]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **3.1**
- Evidence: ...ons from 28 biological ctDNA low-shedders was calculated using the estimated marginal means (rstatix v0.7.1) 50 method, using a linear mixed-effects (lmerTest v3.1-3) 51 model to take into account the patient-tumour region associations, treating detection status as fixed effect and patient ID as random effect.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **3.1**
- Evidence: These were fitted using the package lmerTest (v.3.1-3) 63 in R, using the parent tumour from which the tumour region was derived as a random effect.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Antibodies against endogenous retroviruses promote lung cancer immunotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05771-9 | PMCID: PMC10115647 | PMID: 37046094
- Version used: **1.1.27.1**
- Evidence: The package lme4 (v.1.1.27.1) was used for linear mixed-effects models.
- Full pipeline: quantification [Salmon v0.12.0] -> differential/statistical testing [lme4 v1.1.27.1] -> stage not stated [QuPath v0.3, R, RepeatMasker, data.table v1.14.2, survival (R) v3.2.13, tidyverse v1.0.7]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Evidence: The BLUEs were computed with the lme4 package in R by first using the model: y ijk = µ + G i + E j + G i x E j + B jk + ε ijk Where y ijk is the score of accession i in environment j in block k , µ is the overall mean of the trait, G i is the effect of accession i , E j is the effect of environment j , G i × E j is the interaction effect between accession i and environment j , B jk is the effect o...
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Version used: **3.1**
- Evidence: 68 ), lmerTest 3.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### Clonal dynamics after allogeneic haematopoietic cell transplantation. (Nature 2024)

- DOI: 10.1038/s41586-024-08128-y | PMCID: PMC11602715 | PMID: 39478227
- Evidence: Using the lme function from the R package lme4, we performed a linear mixed-effects regression to estimate the impact of donor/recipient status on phylogenetic age.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [R]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: This analysis included investigating immune phenotypes using PAGA 75 (see below) and examining the effects of testosterone on immune cell composition using a mixed-effects model with the lme4 package.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Version used: **1.1**
- Evidence: The log-transformed odds ratio at each radius was estimated using generalized linear mixed-effects models, with the family argument set to binomial and implemented in glmer function in the lme4 (v.1.1-27) package in R 56 , in which the image source for the observations is modelled as a random effect.
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Multi-habitat landscapes are more diverse and stable with improved function. (Nature 2024)

- DOI: 10.1038/s41586-024-07825-y | PMCID: PMC11374697 | PMID: 39169178
- Evidence: Pollination experiment The effect of habitat numbers (one or three) on fruit weight and the proportion of Class 1 strawberries (a measure of fruit quality that is determined by pollination success) was assessed using a mixed effect model with site as a random effect and the landscape type (monad or triad) as a fixed effect, using the package lme4 (ref.
- Full pipeline: differential/statistical testing [R, lme4]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: Linear mixed-effects models were implemented using the R software packages lme4 111 and lmerTest 112 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Thresholds for adding degraded tropical forest to the conservation estate. (Nature 2024)

- DOI: 10.1038/s41586-024-07657-w | PMCID: PMC11269177 | PMID: 39020163
- Version used: **1.1**
- Evidence: Methods All data manipulation, data analysis and construction of figures were conducted in the R v.4.02 computing environment 46 , using the packages ape (v.5.0) 47 , betareg (v.3.1-4) 48 , dplyr (v.1.1.4) 49 , lme4 (v.1.1-35.1) 50 , lmtest (v.0.9-40) 51 , lubridate (v.1.9.3) 52 , MASS (v.7.3-60.0.1) 53 , openxlsx (v.4.2.5.2) 54 , paletteer (v.1.6.0) 55 , pastecs (v.1.4.2) 56 , png (v.0.1-8) 57 , ...
- Full pipeline: visualisation [ape (R) v5.0, lme4 v1.1, tidyverse v1.1.4]

### Airborne DNA reveals predictable spatial and seasonal dynamics of fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-07658-9 | PMCID: PMC11269176 | PMID: 38987593
- Evidence: Univariate analyses addressing how variations in DNA amount, species richness, spore size and trophic guild composition depend on climate, season and weather We fitted a series of mixed linear models with the R package lme4 (ref.
- Full pipeline: read trimming [Cutadapt v4.2] -> differential/statistical testing [lme4] -> stage not stated [DADA2 v1.18.0, R, phyloseq]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: The glmer function in the lme4 package implemented on R was used to fit the model.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### Global shortfalls in documented actions to conserve biodiversity. (Nature 2024)

- DOI: 10.1038/s41586-024-07498-7 | PMCID: PMC11168922 | PMID: 38839953
- Evidence: We used generalized linear models (GLMs) with a binomial error structure, fit using the glm function of the lme4 package 64 , to model both the proportion of species documented as receiving the appropriate type of conservation intervention, and the proportion of species with no documented interventions.
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [R v4.3.2, tidyverse]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Handling of geospatial and other data was conducted using the R packages lme4, matrixStats, Matrix, geojsonio, raster, rgeos, sf, sp, tmaptools, patchwork, leaflet, data.table, dplyr, haven, Hmisc, openxlsx, rgdal, scales, stringr, tidyr, tibble, xlsx, rfPermute, randomForest, forcats, and in python using the packages pandas, numpy, scipy, statsmodels, firthlogist, patsy and jupyter 68 – 97 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Frequent disturbances enhanced the resilience of past human populations. (Nature 2024)

- DOI: 10.1038/s41586-024-07354-8 | PMCID: PMC11111401 | PMID: 38693262
- Evidence: This analysis was performed using the cAIC4 and lme4 R packages 52 , 53 ; scripts are available at ref.
- Full pipeline: stage not stated [R, lme4]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.1**
- Evidence: Analyses also used the following packages: lme4 (v.1.1-31) 84 , minpack.lm (v.1.2-4) 85 .
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Mutualisms weaken the latitudinal diversity gradient among oceanic islands. (Nature 2024)

- DOI: 10.1038/s41586-024-07110-y | PMCID: PMC10937366 | PMID: 38418873
- Evidence: All analyses were done in R 3.4.1 58 , with linear mixed models constructed with the lme4 package 59 ; significance for these models was tested using lmerTest 60 , using Satterthwaite’s approximations for t -test and corresponding P values, with a P value of <0.05 used as the threshold for significance.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, ggplot2 v3.4.0, tidyverse v1.3.2]

### Rainforest transformation reallocates energy from green to brown food webs. (Nature 2024)

- DOI: 10.1038/s41586-024-07083-y | PMCID: PMC10917685 | PMID: 38355803
- Evidence: Statistical analyses To analyse the overall distribution of energy flux across animal groups and trophic functions, we first ran two mixed-effect models testing the effect of land-use system (rainforest, jungle rubber, rubber and oil palm), region (two regions included in the design) and either major animal group or trophic function on energy fluxes in food webs (the lme4 package) 82 .
- Full pipeline: differential/statistical testing [lme4]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: We subsequently fit linear mixed-effects models to the transformed abundances of each MAG across all 707 faecal samples (lme4 56 , v.1.1-27.1; lmerTest 57 , v.3.1-3).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### GDF15 linked to maternal risk of nausea and vomiting during pregnancy. (Nature 2024)

- DOI: 10.1038/s41586-023-06921-9 | PMCID: PMC10808057 | PMID: 38092039
- Evidence: Linear mixed models with random intercepts implemented in the LmerTest package ( https://cran.r-project.org/web/packages/lmerTest/index.html ) were used to characterize the effect of gestational age on relative abundance of natural-log transformed total circulating GDF15 measured by mass spectrometry.
- Full pipeline: alignment/mapping [GATK] -> variant calling [BCFtools, SAMtools] -> quantification [BCFtools, SAMtools, lme4] -> registration [Picard] -> stage not stated [PLINK v1.90b, R]

### Pesticide use negatively affects bumble bees across European landscapes. (Nature 2024)

- DOI: 10.1038/s41586-023-06773-3 | PMCID: PMC11006599 | PMID: 38030722
- Evidence: We constructed LMMs with the lme4 package 64 and GLMMs with the glmmTMB package 65 .
- Full pipeline: stage not stated [emmeans, lme4]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Version used: **1.1**
- Evidence: ...all experiments) with the factors time after inoculation, cyanophage type (WT or mutant) and their interaction, and replicate as random effects using lme4 (v.1.1-31) 68 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: Using lme4 package in R 59 , the design formula: NPX(bridged) ~ age group + CMV + sex, was applied, with comparisons on the age group factor.
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Version used: **3.1**
- Evidence: ...ore for all genes critical to the AVCM cell state (decreased in trisomic AVCM) and statistical tests were performed using linear mixed-effects model (lmerTest v3.1–3) with Benjamini-Hochberg multiple-testing correction applied to resultant p-values (stats v4.0.5).
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Somatic mutation and selection at population scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09584-w | PMCID: PMC12611758 | PMID: 41062696
- Evidence: Regression analyses To test for associations between epidemiological variables and rates of mutational signatures or driver mutation frequencies, we used mixed-effect regression models (lmer function in the lme4 R package 72 ) as described below.
- Full pipeline: alignment/mapping [MAFFT] -> variant calling [BEDTools, GATK] -> differential/statistical testing [lme4] -> stage not stated [BCFtools, R]

### Sperm sequencing reveals extensive positive selection in the male germline. (Nature 2025)

- DOI: 10.1038/s41586-025-09448-3 | PMCID: PMC12611766 | PMID: 41062690
- Evidence: For each tissue and mutation type for which a regression was performed, the model was constructed using the lmer function from the lme4 package 72 in R.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [Bioconductor, ggplot2 v3.4.4, lme4] -> visualisation [R] -> stage not stated [BCFtools, Nextflow]

### Polygenic and developmental profiles of autism differ by age at diagnosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09542-6 | PMCID: PMC12571882 | PMID: 41034588
- Version used: **1.1.27.1**
- Evidence: We also ran multiple linear mixed effects regression using the lme4 (v.1.1.27.1) package in R 99 , fitting a PGS by age interaction term to investigate whether the effects of PGS on SDQ change over time.
- Full pipeline: differential/statistical testing [PLINK, lme4 v1.1.27.1] -> stage not stated [GCTA, LDSC, lavaan v0.6]

### Amygdala-liver signalling orchestrates glycaemic responses to stress. (Nature 2025)

- DOI: 10.1038/s41586-025-09420-1 | PMCID: PMC12527908 | PMID: 40903586
- Evidence: Analyses in R were performed with R 3.6 using the lme4, lmerTest, emmeans, and car packages 61 , 62 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.4.2, emmeans, lme4]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: For testing statistical differences between two groups, we used a two-tailed unpaired Student’s t -test when the experimental design did not involve multiple batches (for example, different rounds of experiments); otherwise, we used the R packages lme4 and lmerTest to fit data into an LMM to account for potential random effects from different experimental rounds and clones.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: For the complete dataset, we then generated a mixed-effects linear model [response ~ (variable + species + stimulus + transmitter + brain region) 5 + section ID] using the R package lme {lme4}, and evaluated the model by contrasting stimulus (percentage of transmitter-positive neurons that co-express FOS) or species (percentage of neurons that co-express a given transmitter, enrichment ratio) with...
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Precisely defining disease variant effects in CRISPR-edited single cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09313-3 | PMCID: PMC12488502 | PMID: 40702188
- Evidence: The R package lme4 was used to model fixed effects using the glm.nb function, and the R package MASS was used to model random effects using the glmer.nb function.
- Full pipeline: alignment/mapping [kallisto] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> stage not stated [GSEA, R, lme4]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **1.1**
- Evidence: Statistical analysis was performed using generalized linear mixed models (lme4 v.1.1-35.5 package), with the animal identifier included as a random effect to account for non-independence owing to score replicates.
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Mapping the adaptive landscape of Batesian mimicry using 3D-printed stimuli. (Nature 2025)

- DOI: 10.1038/s41586-025-09216-3 | PMCID: PMC12367557 | PMID: 40604276
- Evidence: We used generalized linear models and generalized linear mixed models implemented in the package lme4 (ref.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.3.0]

### Rapid emergence of a maths gender gap in first grade. (Nature 2025)

- DOI: 10.1038/s41586-025-09126-4 | PMCID: PMC7618463 | PMID: 40500443
- Evidence: R packages used included rstatix, FactoMineR, dplyr, tidyverse, broom, ggplot2, jtools, LambertW, cohens_d, reshape2, lmerTest, knitr, rmarkdown, MatchIt, remotes, rcpp, glmertree, BayesFactor, mice and tableone, all for R v.4.3.2.
- Full pipeline: stage not stated [R, ggplot2, lme4, tidyverse]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: We modelled the data using the R package ‘lme4’ 63 assuming residuals followed a Gaussian distribution.
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Evidence: Linear mixed-effect model statistics were applied as implemented in the lme4 R package with a nested design to account for images acquired from the same culture well and same biological replicate.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **1.1**
- Evidence: A separate model for each treatment (apilimod or ESK981) comparison against DMSO was built using the R package lme4 (v.1.1-35.1) 84 .
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Goal-specific hippocampal inhibition gates learning. (Nature 2025)

- DOI: 10.1038/s41586-025-08868-5 | PMCID: PMC12222015 | PMID: 40205046
- Evidence: Statistical analysis For data with repeated samples from the same animal and day, we used LMM analysis in R (v.4.2.2) and lme4 package 67 (v.1.1.35.1) to evaluate significant differences while controlling for repeated measures from sessions or animals.
- Full pipeline: differential/statistical testing [R v4.2.2, emmeans, lme4]

### Timing and trajectory of BCR::ABL1-driven chronic myeloid leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-08817-2 | PMCID: PMC12018454 | PMID: 40205062
- Evidence: Mixed models Linear mixed models used for SNV burden and telomere analysis were implemented in the R package lme4 to estimate the impact of age and mutant status.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [R, lme4, metafor]

### Vulnerability of amphibians to global warming. (Nature 2025)

- DOI: 10.1038/s41586-025-08665-0 | PMCID: PMC11946914 | PMID: 40044855
- Version used: **1.1**
- Evidence: We therefore fitted Poisson and binomial models using lme4 (v.1.1-33) 107 and nested genus, species and observation as random terms.
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [R, brms] -> visualisation [ggplot2] -> stage not stated [lme4 v1.1, metafor]

### Clonal dynamics and somatic evolution of haematopoiesis in mouse. (Nature 2025)

- DOI: 10.1038/s41586-025-08625-8 | PMCID: PMC12074984 | PMID: 40044850
- Evidence: The signature-specific burdens per colony were estimated using a linear mixed model (R package lme4) with age as a random effect and mouse ID as grouping variable: \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$${{\rm{...
- Full pipeline: alignment/mapping [BWA] -> simulation/modelling [R] -> stage not stated [VEP, lme4]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Evidence: We undertook differential abundance analysis using a linear mixed effect model implemented in the lmerTest R package v.3.1-3 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Complete human recombination maps. (Nature 2025)

- DOI: 10.1038/s41586-024-08450-5 | PMCID: PMC11922761 | PMID: 39843742
- Evidence: This was done with the lmerTest 69 package in R 68 .
- Full pipeline: stage not stated [NumPy v1.24.2, SciPy v1.10.1, lme4, statsmodels v0.13.2]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **1.1.35.3**
- Evidence: Transcriptomic signatures of ageing, mortality and lifespan in the aggregated meta-dataset Scaled relative expression profiles from the aggregated meta-dataset were analysed using linear mixed-effects models implemented via lmer from lme4 (v1.1.35.3) and lmerTest (v3.1.3) packages 242 .
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: Group comparisons of fluorescence intensity data were assessed using a generalized linear model with a gamma distribution and log link function using the lme4 package 89 in R (v4.3.1).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### Somatic evolution following cancer treatment in normal tissue. (Nature 2026)

- DOI: 10.1038/s41586-025-09792-4 | PMCID: PMC13190248 | PMID: 41372419
- Evidence: Coverage and variance explained The relationship between coverage, VAF and number of mutations was assessed through a linear mixed-effects model using the R package lme4 followed by an anova test.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> differential/statistical testing [R, lme4] -> stage not stated [Nextflow, SAMtools v1.19.2]

### A place-based assessment of biodiversity intactness in sub-Saharan Africa. (Nature 2026)

- DOI: 10.1038/s41586-025-09781-7 | PMCID: PMC12727506 | PMID: 41339553
- Evidence: ...Class}/\mathrm{RG})\end{array}$$\end{document} Intactness index ~ IUCN category + range size scaled + ( 1 | Class / RG ) This model was run using the lme4 package in R.
- Full pipeline: normalisation [lme4]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Evidence: Statistical analyses Slope of HIV rebound modelling Linear mixed effects modelling was performed in R (v.4.3) using the lmerTest package (v.3.1; two-sided t -test with Satterthwaite’s approximation for d.f.) for viral rebound curves from the time of rebound to the time of peak viral load (as defined above: the highest viral load within the first 6 weeks after rebound) or the time of ART restart if...
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### Land-use change undermines the stability of avian functional diversity. (Nature 2026)

- DOI: 10.1038/s41586-025-09788-0 | PMCID: PMC12779574 | PMID: 41299180
- Evidence: All models were conducted using the lme4 package in R 102 .
- Full pipeline: stage not stated [R, lme4]

### Competitive dynamics underlie cognitive improvements during sleep. (PNAS 2021)

- DOI: 10.1073/pnas.2109339118 | PMCID: PMC8713802 | PMID: 34903651
- Evidence: All statistical analyses were performed in R 3.6.2 using the libraries lme4 and lsmeans.
- Full pipeline: differential/statistical testing [R v3.6, lme4]

### Temporal self-compression: Behavioral and neural evidence that past and future selves are compressed as they move away from the present. (PNAS 2021)

- DOI: 10.1073/pnas.2101403118 | PMCID: PMC8670431 | PMID: 34848536
- Evidence: For each study, linear mixed models using the R package lme4 were constructed to assess how time affected the trait ratings or dynamic circle overlap ( 82 ).
- Full pipeline: registration [AFNI, FreeSurfer] -> stage not stated [FSL v5.0.9, Nilearn, Nipype v1.2.0, R, fMRIPrep v1.4.0, lme4]

### Evolutionary change in the construction of the nursery environment when parents are prevented from caring for their young directly. (PNAS 2021)

- DOI: 10.1073/pnas.2102450118 | PMCID: PMC8640939 | PMID: 34819363
- Evidence: Mixed effects models were performed with the package “lme4” version 1.1-27.1 ( 40 ).
- Full pipeline: differential/statistical testing [R v4.1.1, lme4] -> stage not stated [ImageJ v1.49v, emmeans]

### Eighteen-month-old infants represent nonlocal syntactic dependencies. (PNAS 2021)

- DOI: 10.1073/pnas.2026469118 | PMCID: PMC8521675 | PMID: 34607945
- Evidence: For analyses across multiple age groups, we constructed linear mixed-effects models using the lme4 package in R ( 56 ).
- Full pipeline: differential/statistical testing [R, lme4]

### Follistatin mediates learning and synaptic plasticity via regulation of Asic4 expression in the hippocampus. (PNAS 2021)

- DOI: 10.1073/pnas.2109040118 | PMCID: PMC8488609 | PMID: 34544873
- Evidence: We fitted models by REML (Restricted maximum likelihood), using the lmer function from the R package lme4 ( 42 ).
- Full pipeline: alignment/mapping [HTSeq] -> stage not stated [R, lme4]

### What we talk about when we talk about colors. (PNAS 2021)

- DOI: 10.1073/pnas.2109237118 | PMCID: PMC8488626 | PMID: 34556580
- Version used: **1.1**
- Evidence: GLMM fits were performed in R (v3.6.3) using the lme4 (v1.1-21) package, with MLPE structure based on code from resistanceGA ( 70 ).
- Full pipeline: stage not stated [R v3.6.3, lme4 v1.1]

### National religiosity eases the psychological burden of poverty. (PNAS 2021)

- DOI: 10.1073/pnas.2103913118 | PMCID: PMC8488579 | PMID: 34544863
- Version used: **1.1**
- Evidence: We accounted for the nested data structure (persons nested in nations) by using linear mixed-effects models in R [mixed-effects model package lme4 version 1.1-23, models 1 through 3 ( 53 ); mixed-effects path model package lavaan version 0.6-7, model 4 ( 54 )].
- Full pipeline: differential/statistical testing [lavaan v0.6, lme4 v1.1]

### Trade-offs among transport, support, and storage in xylem from shrubs in a semiarid chaparral environment tested with structural equation modeling. (PNAS 2021)

- DOI: 10.1073/pnas.2104336118 | PMCID: PMC8379947 | PMID: 34389676
- Evidence: This was done using boxplots and violin plots (R package ggplot2) and by partitioning the variance of the measured traits among species nested within each site, across the different sites, and within each species (intraspecific; R package lme4 for mixed-effect models).
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.0.5, lavaan v0.6]

### Evidence and theory for lower rates of depression in larger US urban areas. (PNAS 2021)

- DOI: 10.1073/pnas.2022472118 | PMCID: PMC8346882 | PMID: 34315817
- Evidence: To do so, we ran logistic regressions with the R package lme4 ( 61 ) on each year of the BRFSS data using the individual participant-level survey responses.
- Full pipeline: differential/statistical testing [R, lme4]

### Social mindfulness and prosociality vary across the globe. (PNAS 2021)

- DOI: 10.1073/pnas.2023846118 | PMCID: PMC8536393 | PMID: 34426492
- Evidence: We standardized variables and ran all mixed models using R (package lme4) ( 60 ) with country (level 2) as the clustering variable.
- Full pipeline: dimensionality reduction/clustering [lme4]

### A large-scale study of stress, emotions, and blood pressure in daily life using a digital platform. (PNAS 2021)

- DOI: 10.1073/pnas.2105573118 | PMCID: PMC8346904 | PMID: 34326265
- Evidence: Given that check-ins were nested within individuals, we utilized multilevel modeling (i.e., mixed-effects models; lme4 package in RStudio 1.2.5019 and mixed models in SPSS version 27, further details in SI Appendix ) in which check-ins were nested within participants.
- Full pipeline: differential/statistical testing [lme4]

### Vocal learning and flexible rhythm pattern perception are linked: Evidence from songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2026130118 | PMCID: PMC8307534 | PMID: 34272278
- Evidence: Trials were binned in 10 ms increments starting at 75 ms IOI (20 bins), and the number of correct responses were analyzed with a binomial logistic regression using a generalized linear mixed model with tempo bin as a fixed effect and subject as a random effect, using the lme4 ( glmer) statistical package for R (version 3.6.2) within RStudio (version 1.2.5033).
- Full pipeline: differential/statistical testing [R v3.6.2, lme4]

### Sex-specific ornament evolution is a consistent feature of climatic adaptation across space and time in dragonflies. (PNAS 2021)

- DOI: 10.1073/pnas.2101458118 | PMCID: PMC8285952 | PMID: 34260398
- Evidence: We first used separate linear mixed-effects models to quantify each species’ relationship between climatic temperatures and male and female wing melanization (lme4) ( 44 ).
- Full pipeline: quantification [lme4] -> differential/statistical testing [lme4]

### Accelerated expansion of pathogenic mitochondrial DNA heteroplasmies in Huntington's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2014610118 | PMCID: PMC8325154 | PMID: 34301881
- Version used: **1.1**
- Evidence: The mixed-effects modeling and the significance level of the fixed effects were computed by using the lme4 (version 1.1) and lmerTest (version 3.0) R packages.
- Full pipeline: alignment/mapping [SAMtools v1.6, freebayes v1.1.0] -> registration [SAMtools v1.6, freebayes v1.1.0] -> differential/statistical testing [R v3.5.0, lme4 v1.1] -> stage not stated [ANNOVAR, Picard]

### Retrograde sulfur flow from glucosinolates to cysteine in <i>Arabidopsis thaliana</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2017890118 | PMCID: PMC8179156 | PMID: 34035165
- Evidence: The LMM analysis was performed in R using the lmer function in lme4 package using the following formula: value ∼ condition – 1 + ( 1 | batch ) , where “condition” includes sulfur concentrations, time points, genotypes, or their combinations, depending on the experimental setup.
- Full pipeline: variant calling [lme4] -> stage not stated [R v3.6]

### Environmental drivers of annual population fluctuations in a trans-Saharan insect migrant. (PNAS 2021)

- DOI: 10.1073/pnas.2102762118 | PMCID: PMC8256005 | PMID: 34155114
- Evidence: We fitted generalized linear mixed-effects models (GLMMs) to painted lady count data using the lme4 package ( 61 ) in the program R ( 62 ).
- Full pipeline: differential/statistical testing [lme4] -> simulation/modelling [WRF] -> stage not stated [R v3.5]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: Piglets were weighed every week for the first three diet phases and every 2 wk during the last two diet periods ( Dataset S2 ); the resulting dataset was analyzed by applying linear mixed-effects models built using R (v3.5) ( 45 ) and the lmerTest package (v3.1.2) ( 46 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Identification of a micropeptide and multiple secondary cell genes that modulate &lt;i&gt;Drosophila&lt;/i&gt; male reproductive success. (PNAS 2021)

- DOI: 10.1073/pnas.2001897118 | PMCID: PMC8053986 | PMID: 33876742
- Evidence: We performed a statistical test in R using the packages lme4 and emmeans ( 73 – 75 ).
- Full pipeline: differential/statistical testing [emmeans, lme4]

### A narrow ear canal reduces sound velocity to create additional acoustic inputs in a microscale insect ear. (PNAS 2021)

- DOI: 10.1073/pnas.2017281118 | PMCID: PMC7958352 | PMID: 33658360
- Evidence: Linear mixed effects models were run using lmerTest ( 45 ) in R 4.0.0 ( 45 ).
- Full pipeline: differential/statistical testing [R v4.0, lme4] -> stage not stated [emmeans]

### Evidence supporting a time-limited hippocampal role in retrieving autobiographical memories. (PNAS 2021)

- DOI: 10.1073/pnas.2023069118 | PMCID: PMC8000197 | PMID: 33723070
- Evidence: The average correlation of scene-selective voxels was compared across conditions for the left and right posterior hippocampus using the same LME modeling approach described previously, implemented in R using the lme4 ( 74 ) and lsmeans ( 75 ) packages.
- Full pipeline: stage not stated [AFNI, FreeSurfer v6.0, lme4]

### Sexually antagonistic coevolution between the sex chromosomes of <i>Drosophila melanogaster</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2003359118 | PMCID: PMC7923534 | PMID: 33602805
- Evidence: For statistical analysis after the 25 generations of experimental evolution we fitted linear mixed models (lme4) ( 43 ) with treatment nested within replicate populations to test the dependent variables: male reproductive fitness, egg-to-adult offspring survival, sperm competition, and sex ratio.
- Full pipeline: differential/statistical testing [R v3.4.4, lme4]

### Heat stress destabilizes symbiotic nutrient cycling in corals. (PNAS 2021)

- DOI: 10.1073/pnas.2022653118 | PMCID: PMC7865147 | PMID: 33500354
- Evidence: NanoSIMS measurements of relative 13 C and 15 N abundance in the host and symbiont tissue/cells were analyzed using linear mixed models with treatment as a fixed and colony as a random effect using the lme4 R package v.1.1-21 ( 98 ).
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [FastQC v0.11.5, Trimmomatic v0.39] -> alignment/mapping [Salmon v1.0.0] -> quantification [Salmon v1.0.0, lme4] -> differential/statistical testing [R, vegan v2.5] -> stage not stated [ImageJ]

### Sunlight exposure exerts immunomodulatory effects to reduce multiple sclerosis severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018457118 | PMCID: PMC7817192 | PMID: 33376202
- Evidence: Statistical analyses were conducted in R v3.6.0 using the packages stats , lme4 , glmmTMB , ordinal , and DHARMa .
- Full pipeline: quality control [PLINK v1.90] -> variant calling [PLINK v1.90] -> differential/statistical testing [R v3.6, lme4] -> visualisation [ggplot2] -> stage not stated [edgeR, kallisto]

### The Ruminant sorting mechanism protects teeth from abrasives. (PNAS 2022)

- DOI: 10.1073/pnas.2212447119 | PMCID: PMC9894168 | PMID: 36459638
- Evidence: Statistics were carried out in R ( 37 ) using the lmerTest package ( 38 ).
- Full pipeline: differential/statistical testing [R, lme4]

### The restart effect in social dilemmas shows humans are self-interested not altruistic. (PNAS 2022)

- DOI: 10.1073/pnas.2210082119 | PMCID: PMC9894210 | PMID: 36459646
- Evidence: We conducted analyses in RStudio ( 66 ), inputted the data with the zTree package ( 67 ), tested LMM significance with lmerTest ( 68 ), and made the data figures with ggplot2 ( 69 ).
- Full pipeline: stage not stated [ggplot2, lme4]

### Transposable elements drive intron gain in diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2209766119 | PMCID: PMC9860276 | PMID: 36417430
- Evidence: We then used the R package lme4 ( 54 ) to construct generalized linear model of the form: (proper_splices,missplices) ~ Introner + depth + length (proper_splices,missplices) ~ depth + length to correct for the depth and length of each intron.
- Full pipeline: alignment/mapping [MAFFT, SAMtools] -> differential/statistical testing [R, lme4] -> stage not stated [Python, RepeatMasker, phytools]

### Impact of cultural and genetic structure on food choices along the Silk Road. (PNAS 2022)

- DOI: 10.1073/pnas.2209311119 | PMCID: PMC9704696 | PMID: 36375050
- Evidence: Total variance of each distribution of cluster assignments was partitioned into “Between countries,” “Between cities,” “Within cities,” and “Among individuals.” In order to do so, we performed a linear mixed-effects analysis for each distribution of cluster assignments by using the function lmer implemented within the R package lme4 ( 73 ).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SciPy, lme4] -> differential/statistical testing [lme4] -> machine learning [ADMIXTURE] -> stage not stated [PLINK v1.9, R, vegan]

### Initial impressions of compatibility and mate value predict later dating and romantic interest. (PNAS 2022)

- DOI: 10.1073/pnas.2206925119 | PMCID: PMC9659375 | PMID: 36322750
- Evidence: All data analysis was done in R programming ( 45 ), using the glmer function (for logistic regression) and the lmer function (for continuous regression) from the lme4 package ( 46 ).
- Full pipeline: differential/statistical testing [lme4]

### NETfacts: An integrated intervention at the individual and collective level to treat communities affected by organized violence. (PNAS 2022)

- DOI: 10.1073/pnas.2204698119 | PMCID: PMC9636916 | PMID: 36306329
- Version used: **1.1**
- Evidence: To test our hypotheses regarding the effectiveness of NETfacts in comparison to NET only, we used separate GLMMs with lme4 1.1–27.1 for each response variable ( 67 ).
- Full pipeline: differential/statistical testing [R v4.0] -> stage not stated [emmeans v1.4.6, lavaan v0.6, lme4 v1.1]

### Aesthetic experience enhances first-person spatial representation. (PNAS 2022)

- DOI: 10.1073/pnas.2201540119 | PMCID: PMC9618070 | PMID: 36251990
- Evidence: These analyses were conducted in R, using the “glmer” and “lmer” functions from the lme4 package ( 62 ) to compute logistic and linear mixed effects models respectively, and the “Anova” function from the car package ( 63 ) to derive corresponding statistics (type II Wald χ 2 tests).
- Full pipeline: differential/statistical testing [lme4]

### An insect brain organizes numbers on a left-to-right mental number line. (PNAS 2022)

- DOI: 10.1073/pnas.2203584119 | PMCID: PMC9636979 | PMID: 36252101
- Evidence: We used R, version 4.1.2 ( 39 ), the psych package for descriptive statistics ( 40 ), and the packages lme4 ( 41 ) and lmerTest ( 42 ) for multilevel modeling.
- Full pipeline: differential/statistical testing [lme4]

### Sustainable pest control inspired by prey-predator ultrasound interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2211007119 | PMCID: PMC9618128 | PMID: 36215520
- Evidence: For S. exigua , we derived the mean and 95% confidence interval using a GLMM (gamma error distribution for spike latency and spike period; Poisson error distribution for spike numbers) with a random effect of individual ID, which was run in the “lme4” package ( 31 ) in R.
- Full pipeline: differential/statistical testing [R v4.0] -> stage not stated [lme4]

### Changing patterns of genetic differentiation in the slender wild oat, <i>Avena barbata</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121248119 | PMCID: PMC9546611 | PMID: 36161958
- Evidence: We analyzed the spatial pattern and temporal change in morphotype frequencies by GLMM with a binary (Logit) link function in the lme4 package of the R statistical programming language ( 54 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Brain dysfunction during warming is linked to oxygen limitation in larval zebrafish. (PNAS 2022)

- DOI: 10.1073/pnas.2207052119 | PMCID: PMC9522358 | PMID: 36122217
- Evidence: For responses recorded as repeated measures on individual fish, mixed models were created using the lmer function from the lme4 package, v.1.1–27.1, to account for fish identity as a random effect.
- Full pipeline: stage not stated [Python, lme4]

### Cross-modal and cross-language activation in bilinguals reveals lexical competition even when words or signs are unheard or unseen. (PNAS 2022)

- DOI: 10.1073/pnas.2203906119 | PMCID: PMC9457174 | PMID: 36037359
- Evidence: We analyzed the data using R ( 36 ) v4.0.3 with the VWPre package ( 37 ) v1.2.3 for preprocessing and the lme4 package ( 38 ) v1.1–25 for statistical analysis.
- Full pipeline: differential/statistical testing [lme4]

### Strategic intergroup alliances increase access to a contested resource in male bottlenose dolphins. (PNAS 2022)

- DOI: 10.1073/pnas.2121723119 | PMCID: PMC9457541 | PMID: 36037370
- Evidence: ...proportion data, where consortship rate was the response variable, and a generalized linear mixed-effect model with a Poisson family for count data ( lme4 package in R ( 68 )), where maximum consortship duration (in days) was the response variable.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, ggplot2]

### Exploring the associations between discrimination, coping, skin tone, and the psychosocial health of young adults of color. (PNAS 2022)

- DOI: 10.1073/pnas.2119587119 | PMCID: PMC9459310 | PMID: 36037339
- Evidence: Given that the data involved weekly diary assessments, longitudinal multilevel models were computed in R using the lme4 package ( 63 ) to examine whether within-person discrimination and between-person discrimination were associated with young adults’ psychosocial health.
- Full pipeline: stage not stated [lme4]

### Talking with strangers is surprisingly informative. (PNAS 2022)

- DOI: 10.1073/pnas.2206992119 | PMCID: PMC9407669 | PMID: 35972959
- Evidence: We used the R ( 20 ) packages lme4 ( 21 ) and lmerTest ( 22 ).
- Full pipeline: stage not stated [lme4]

### Sexual repurposing of juvenile aposematism in locusts. (PNAS 2022)

- DOI: 10.1073/pnas.2200759119 | PMCID: PMC9407653 | PMID: 35969777
- Evidence: ... ds YP ) and “trial” ( N = 8) were treated as fixed effects in the GLM; generalized linear mixed models (glmer and glmer.nb) were attempted using the lme4 package with trial as a random effect, but eight levels led to singularity within the model.
- Full pipeline: stage not stated [lme4]

### Two distinct ways to form long-term object recognition memory during sleep and wakefulness. (PNAS 2022)

- DOI: 10.1073/pnas.2203165119 | PMCID: PMC9407643 | PMID: 35969775
- Evidence: Statistical analyses were calculated in R (Version 1.3.1.1093) using the lme4 package (Version 1.1-23) and SPSS (Version 26.0, IBM).
- Full pipeline: differential/statistical testing [R, lme4]

### Insectivorous bats form mobile sensory networks to optimize prey localization: The case of the common noctule bat. (PNAS 2022)

- DOI: 10.1073/pnas.2203663119 | PMCID: PMC9388074 | PMID: 35939677
- Evidence: For the insect search-flight sequences (i.e., no area-restricted movement behavior; see Movement classification , above) where we found coefficients from the iSSA to be significant on the 0.1 level, we performed two linear mixed models [R package lme4 ( 50 )] to evaluate how bats changed their flight behavior (i.e., relative heading) and intraspecific distance in response to conspecifics that were...
- Full pipeline: stage not stated [R, lme4]

### Evolution of plasticity prevents postinvasion extinction of a native forb. (PNAS 2022)

- DOI: 10.1073/pnas.2118866119 | PMCID: PMC9371648 | PMID: 35914140
- Evidence: All mixed-effect models were developed using the lme4 ( 37 ) package of R ( 38 ), if not specified otherwise.
- Full pipeline: differential/statistical testing [lme4]

### Nonconcomitant host-to-host transmission of multipartite virus genome segments may lead to complete genome reconstitution. (PNAS 2022)

- DOI: 10.1073/pnas.2201453119 | PMCID: PMC9371732 | PMID: 35914138
- Evidence: We used the lme4 package in R to run these analyses.
- Full pipeline: stage not stated [lme4]

### Plant genetic effects on microbial hubs impact host fitness in repeated field trials. (PNAS 2022)

- DOI: 10.1073/pnas.2201285119 | PMCID: PMC9335298 | PMID: 35867817
- Evidence: Mixed models were fitted using the function lmer in the lme4 R package ( 57 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [Python] -> normalisation [Python] -> stage not stated [Prokka, R, SPAdes, igraph, lme4]

### Organellar transcripts dominate the cellular mRNA pool across plants of varying ploidy levels. (PNAS 2022)

- DOI: 10.1073/pnas.2204187119 | PMCID: PMC9335225 | PMID: 35858449
- Evidence: This model was fit with the lmer function (lme4 package) and evaluated with the Anova function (car package) using type III sums of squares.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R v3.5, emmeans] -> visualisation [ggplot2] -> stage not stated [lme4]

### Motor learning without movement. (PNAS 2022)

- DOI: 10.1073/pnas.2204379119 | PMCID: PMC9335319 | PMID: 35858450
- Evidence: Statistical tests were conducted in R (version 4.0.3): packages rstatix ( 71 ), coin ( 72 ), MuMIn ( 73 ), lmerTest ( 74 ), lme4 ( 75 ), r2glmm ( 76 ), emmeans ( 77 ), effsize ( 78 ), effectsize ( 79 ), magrittr ( 80 ), ggplot2 ( 81 ), ggpubr ( 82 ), and ggeffects ( 83 ).
- Full pipeline: differential/statistical testing [R v4.0.3, emmeans, ggplot2, ggpubr, lme4] -> stage not stated [Python v3.8.5]

### A comparison of political violence by left-wing, right-wing, and Islamist extremists in the United States and the world. (PNAS 2022)

- DOI: 10.1073/pnas.2122593119 | PMCID: PMC9335287 | PMID: 35858413
- Evidence: Because the outcome variable was dichotomous, we fit a generalized linear mixed-effects model implemented in lme4 ( 47 ).
- Full pipeline: differential/statistical testing [lme4]

### Sustained stoichiometric imbalance and its ecological consequences in a large oligotrophic lake. (PNAS 2022)

- DOI: 10.1073/pnas.2202268119 | PMCID: PMC9335326 | PMID: 35858403
- Evidence: We fit this model using lmer () in package lme4 in R.
- Full pipeline: stage not stated [R, lme4]

### Linking land-use and land-cover transitions to their ecological impact in the Amazon. (PNAS 2022)

- DOI: 10.1073/pnas.2202310119 | PMCID: PMC9271202 | PMID: 35759674
- Evidence: Then, we ran linear mixed models (LMMs) using the 'lmer' function from the lme4 package ( 65 ), with each ecological variable as the response variable, the land-use and land-cover classes (categorical variable with seven levels) as the explanatory variable, and clay content, elevation, and slope as covariates.
- Full pipeline: stage not stated [R v4.1.0, lme4]

### Early human B cell signatures of the primary antibody response to mRNA vaccination. (PNAS 2022)

- DOI: 10.1073/pnas.2204607119 | PMCID: PMC9282446 | PMID: 35759653
- Version used: **1.1.26**
- Evidence: The extent of temporal variation was assessed via a linear mixed effects model with the following formula in lme4 (1.1.26): Frequency ∼ timepoint + ( 1 | Subject _ ID ) Timepoint is a factor variable representing the discrete timepoints (v1D0, v1D7, etc.).
- Full pipeline: dimensionality reduction/clustering [R v4.0.2, UMAP] -> differential/statistical testing [lme4 v1.1.26] -> machine learning [ggplot2 v3.3.3]

### Long-term, climate-driven phenological shift in a tropical large carnivore. (PNAS 2022)

- DOI: 10.1073/pnas.2121667119 | PMCID: PMC9271205 | PMID: 35759658
- Evidence: Mixed-effects linear regression analyses were performed using the lme4 package ( 57 ); GAMMs were performed using the gamm4 package ( 58 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### White patients' physical responses to healthcare treatments are influenced by provider race and gender. (PNAS 2022)

- DOI: 10.1073/pnas.2007717119 | PMCID: PMC9271156 | PMID: 35749352
- Evidence: We used mixed-effects linear regression (package lmer and lmerTest , R version 3.3.1, https://www.R-project.org/ ) to examine changes in the size of patients’ allergic reaction to the skin prick test, in the 9-min period immediately after they received a placebo cream.
- Full pipeline: differential/statistical testing [R v3.3.1, lme4]

### Hot and dry conditions predict shorter nestling telomeres in an endangered songbird: Implications for population persistence. (PNAS 2022)

- DOI: 10.1073/pnas.2122944119 | PMCID: PMC9231487 | PMID: 35696588
- Evidence: To test for air temperature effects on early-life TL, we conducted linear mixed-effects models with restricted maximum likelihood estimates using lme4 package, version 1.1-19 ( 80 ).
- Full pipeline: differential/statistical testing [R v3.5.1, ggplot2, lme4]

### Fighting force and experience combine to determine contest success in a warlike mammal. (PNAS 2022)

- DOI: 10.1073/pnas.2119176119 | PMCID: PMC9231503 | PMID: 35700363
- Evidence: We built 12 global GLMMs (lme4 package) ( 74 ), each one representing a hypothesis for which properties influence contest success ( SI Appendix has all model forms).
- Full pipeline: differential/statistical testing [R, lme4]

### Global protected areas seem insufficient to safeguard half of the world's mammals from human-induced extinction. (PNAS 2022)

- DOI: 10.1073/pnas.2200118119 | PMCID: PMC9214487 | PMID: 35666869
- Evidence: We standardized the variables by subtracting the mean and dividing by the SD, and we used the dredge() function from the {lme4} package ( 75 ) in R version 3.6.0 ( 76 ) to fit all feasible component models (i.e., only including quadratic and cubic terms if the linear term was also present in the model) using maximum likelihood.
- Full pipeline: stage not stated [R v3.6.0, lme4]

### A global experiment on motivating social distancing during the COVID-19 pandemic. (PNAS 2022)

- DOI: 10.1073/pnas.2111091119 | PMCID: PMC9295806 | PMID: 35622891
- Version used: **1.1**
- Evidence: To account for the nested structure of the data, we used mixed effects models in the statistical package lme4 (version 1.1-21) ( 56 ).
- Full pipeline: differential/statistical testing [lme4 v1.1] -> stage not stated [R v1.3.1056]

### Fitness effects of plasmids shape the structure of bacteria-plasmid interaction networks. (PNAS 2022)

- DOI: 10.1073/pnas.2118361119 | PMCID: PMC9295774 | PMID: 35613058
- Evidence: We used the function glmer from the R package lme4 ( 45 ) to fit this model.
- Full pipeline: stage not stated [R, lme4]

### Long-term experimental evolution decouples size and production costs in <i>Escherichia coli</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2200713119 | PMCID: PMC9173777 | PMID: 35594402
- Evidence: Metabolic rates and growth models were calculated using R ( 49 ) and the packages nlme ( 50 ), lme4 ( 51 ), and plyr ( 52 ) for model fitting.
- Full pipeline: stage not stated [lme4]

### Higher tree diversity is linked to higher tree mortality. (PNAS 2022)

- DOI: 10.1073/pnas.2013171119 | PMCID: PMC9171344 | PMID: 35500110
- Evidence: Models were bootstrapped separately 100 times to estimate direct and indirect confidence bands using the bootMer function from the lme4 package ( 43 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [lme4]

### Species richness response to human pressure hides important assemblage transformations. (PNAS 2022)

- DOI: 10.1073/pnas.2107361119 | PMCID: PMC9171506 | PMID: 35500119
- Evidence: ( 28 ), I created an ecological model using a mixed generalized linear model [using the function glmer from the lme4 package ( 54 )], accounting for heterogeneity between studies.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Rhesus monkeys have an interoceptive sense of their beating hearts. (PNAS 2022)

- DOI: 10.1073/pnas.2119868119 | PMCID: PMC9169786 | PMID: 35412910
- Evidence: Looking time data were modeled using a generalized linear mixed model with a negative binomial distribution in the package lme4 ( 71 ).
- Full pipeline: differential/statistical testing [R v4.0.4] -> stage not stated [emmeans, lme4]

### Small mammal personalities generate context dependence in the seed dispersal mutualism. (PNAS 2022)

- DOI: 10.1073/pnas.2113870119 | PMCID: PMC9169644 | PMID: 35377818
- Evidence: To instead assess how personality traits may impact each interaction individually, we performed an additional analysis using mixed-effects models in the R package lme4 ( 65 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Interacting pest control and pollination services in coffee systems. (PNAS 2022)

- DOI: 10.1073/pnas.2119959119 | PMCID: PMC9169773 | PMID: 35377782
- Evidence: To analyze the effect of bird and bee exclosure treatments on fruit set, we used generalized linear mixed models (glmer function in R package lme4).
- Full pipeline: stage not stated [R, lme4]

### Linguistic measures of psychological distance track symptom levels and treatment outcomes in a large set of psychotherapy transcripts. (PNAS 2022)

- DOI: 10.1073/pnas.2114737119 | PMCID: PMC9060508 | PMID: 35316132
- Evidence: Mixed-effects models were conducted in lme4 ( 83 ), with P values calculated using the lmerTest package ( 84 ).
- Full pipeline: differential/statistical testing [R, brms, lme4]

### Differential effects of early or late exposure to prenatal maternal immune activation on mouse embryonic neurodevelopment. (PNAS 2022)

- DOI: 10.1073/pnas.2114545119 | PMCID: PMC8944668 | PMID: 35286203
- Evidence: To assess the effects of poly I:C exposure at different gestational timepoints on embryo neuroanatomy, we ran a whole-brain voxel-wise linear mixed-effects model [“mincLmer”; lme4_1.1-21 package ( 79 )] on the relative Jacobian determinant files using group and sex as fixed effects and number of pups per litter and cohort collection batch as random intercepts.
- Full pipeline: differential/statistical testing [R v3.5.1, lme4] -> stage not stated [ANTs, QuPath v0.2.0]

### Engineered nanoparticles enable deep proteomics studies at scale by leveraging tunable nano-bio interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2106053119 | PMCID: PMC8931255 | PMID: 35275789
- Evidence: To determine to what degree individual physicochemical properties correlate with protein abundances comparing profiles across the 157 protein groups, 10 NPs, and 45 subjects, we trained a linear mixed effects model (LMM; lme4) with ProteinIntensity = ZetaPotential + PolyDispersityIndex + HydrodynamicDiameter + ( 1 | Subject ) , setting RMFL = FALSE, which corresponds to a maximum likelihood estima...
- Full pipeline: quantification [lme4] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [R, igraph, lme4] -> machine learning [lme4] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold]

### Widespread misperceptions of long-term attitude change. (PNAS 2022)

- DOI: 10.1073/pnas.2107260119 | PMCID: PMC8931225 | PMID: 35254890
- Evidence: We tested this by fitting the following model using the lme4 package in R ( 36 ) and calculating P values using the lmerTest package ( 37 ): [1] ∣ estimated change ∣ − ∣ actual change ∣ ∼ intercept + participant random effects + item random effects .
- Full pipeline: differential/statistical testing [R, lme4]

### A variable refractory period increases collective performance in noisy environments. (PNAS 2022)

- DOI: 10.1073/pnas.2115103119 | PMCID: PMC8944924 | PMID: 35254873
- Evidence: We used a LMM ( lmer function of the lme4 package in R) to compare the time intervals between consecutive peaks of activity where the lure was active or not active in experimental sequences with sequence ID as a random factor (to account for the collection of multiple values of time intervals in each sequence).
- Full pipeline: simulation/modelling [R] -> stage not stated [lme4]

### Assessing the roles of nitrogen, biomass, and niche dimensionality as drivers of species loss in grassland communities. (PNAS 2022)

- DOI: 10.1073/pnas.2112010119 | PMCID: PMC8915794 | PMID: 35235460
- Evidence: All statistical analyses were performed in R version 4.1.1 using the packages MuMIn, lme4, lmerTest, and piecewiseSEM ( 57 – 60 ).
- Full pipeline: differential/statistical testing [R v4.1.1, lme4]

### Biome boundary maintained by intense belowground resource competition in world's thinnest-rooted plant community. (PNAS 2022)

- DOI: 10.1073/pnas.2117514119 | PMCID: PMC8892519 | PMID: 35165205
- Evidence: We used a linear mixed-effects model (lmer; R package lme4) to evaluate whether specific root length differs between highly seasonal and nonforested biomes (Fynbos, Grassland, Desert, and Mediterranean) vs. less seasonal forested biomes (Tropical, Subtropical, Temperate, Southern Afrotemperate, and Boreal forests).
- Full pipeline: differential/statistical testing [R, emmeans, lme4]

### Rodents monitor their error in self-generated duration on a single trial basis. (PNAS 2022)

- DOI: 10.1073/pnas.2108850119 | PMCID: PMC8892352 | PMID: 35193973
- Version used: **1.1**
- Evidence: 39 ) as implemented in R package lme4 (version 1.1–21), that is, for multiple per animal observations across sessions.
- Full pipeline: stage not stated [R, lme4 v1.1]

### Extra-pair paternity explains cooperation in a bird species. (PNAS 2022)

- DOI: 10.1073/pnas.2112004119 | PMCID: PMC8820227 | PMID: 35042830
- Evidence: To study the minimum approach distance of nest box A birds in all three experimental groups, generalized, linear mixed-effects model with gamma error structure as implemented in software R 3.5.0 ( 46 ) package lme4 ( 47 ) was used.
- Full pipeline: differential/statistical testing [R v3.5, lme4] -> stage not stated [emmeans]

### Loss of glucose 6-phosphate dehydrogenase function increases oxidative stress and glutaminolysis in metastasizing melanoma cells. (PNAS 2022)

- DOI: 10.1073/pnas.2120617119 | PMCID: PMC8833200 | PMID: 35110412
- Evidence: All statistical analyses were performed using Graphpad Prism 9.2.0 or R 4.0.2 with the stats, fBasics, car, lme4, emmeans, and nparLD packages.
- Full pipeline: differential/statistical testing [R v4.0, emmeans, lme4]

### Intersecting kinematic encoding and readout of intention in autism. (PNAS 2022)

- DOI: 10.1073/pnas.2114648119 | PMCID: PMC8812545 | PMID: 35101921
- Evidence: We performed model fitting using the R package lme4 ( 33 ).
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [PyTorch, R, lme4]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Evidence: We estimated the individual repeatability of the median log 2 ejaculate-to-soma coverage ratios of the selected windows (response variable) among the 15 ejaculate samples using a mixed-effect model with the “lmer” function in the “lme4” ( 40 ) package in R v4.0.3 ( 41 ) in which we fitted individual identity and ejaculate as random effects.
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### Unlocking adults' implicit statistical learning by cognitive depletion. (PNAS 2022)

- DOI: 10.1073/pnas.2026011119 | PMCID: PMC8764693 | PMID: 34983868
- Evidence: These analyses were performed using the lme4 package ( 61 ) and the afex package ( 62 ) in R (R Development Core Team, 2011).
- Full pipeline: stage not stated [EEGLAB, Psychtoolbox, R, afex, emmeans, lme4]

### Fast response times signal social connection in conversation. (PNAS 2022)

- DOI: 10.1073/pnas.2116915119 | PMCID: PMC8794835 | PMID: 35042815
- Evidence: For all reported analyses, we used lme4 ( 42 ) implemented in R ( 43 ) to perform linear mixed-effects regressions.
- Full pipeline: differential/statistical testing [R, lme4]

### Radiation and temperature drive diurnal variation of aerobic methane emissions from Scots pine canopy. (PNAS 2023)

- DOI: 10.1073/pnas.2308516120 | PMCID: PMC10756279 | PMID: 38127980
- Version used: **1.1**
- Evidence: In addition, we tested for differences between daytime and nighttime fluxes used mixed effects models with Shoot ID as a random effect (r packages lme4 v.
- Full pipeline: differential/statistical testing [R v4.2.1, lme4 v1.1] -> stage not stated [HMMER, emmeans]

### Increased cortical inhibition following brief motor memory reactivation supports reconsolidation and overnight offline learning gains. (PNAS 2023)

- DOI: 10.1073/pnas.2303985120 | PMCID: PMC10756311 | PMID: 38113264
- Evidence: Group-level repeated measures were analyzed with linear mixed models using the lme4 package implemented in R ( 45 ).
- Full pipeline: differential/statistical testing [R v4.1] -> visualisation [R v4.1] -> stage not stated [SPM, lme4]

### Bonobos and chimpanzees remember familiar conspecifics for decades. (PNAS 2023)

- DOI: 10.1073/pnas.2304903120 | PMCID: PMC10756267 | PMID: 38109542
- Evidence: For Model 1a and the Raw Difference Score Model 2b we fitted simple linear mixed models using the lmer function from the “lme4” package ( 69 ).
- Full pipeline: differential/statistical testing [R v4.0.2] -> stage not stated [lme4]

### Examining the role of dopamine in methylphenidate's effects on resting brain function. (PNAS 2023)

- DOI: 10.1073/pnas.2314596120 | PMCID: PMC10756194 | PMID: 38109535
- Evidence: The “lmer” function in the “lme4” R-package was utilized to perform these analyses.
- Full pipeline: differential/statistical testing [fMRIPrep] -> stage not stated [FreeSurfer, lme4]

### Hippocampal contributions to novel spatial learning are both age-related and age-invariant. (PNAS 2023)

- DOI: 10.1073/pnas.2307884120 | PMCID: PMC10723126 | PMID: 38055735
- Evidence: Specifically, in R 4.2.2, we first constructed the maximal model with all possible random slopes by using the lme4 package ( 51 ).
- Full pipeline: normalisation [ANTs v2.3.5] -> simulation/modelling [brms] -> stage not stated [FSL, PsychoPy, R v4.2, emmeans, lme4]

### Neural tracking measures of speech intelligibility: Manipulating intelligibility while keeping acoustics unchanged. (PNAS 2023)

- DOI: 10.1073/pnas.2309166120 | PMCID: PMC10710032 | PMID: 38032934
- Version used: **1.1**
- Evidence: For the LMEM analysis, the lme4 (version 1.1-30) ( 66 ), lmerTest (version 3.1-30) ( 67 ), and buildmer (version 2.4) ( 68 ) packages in R were used.
- Full pipeline: normalisation [FreeSurfer] -> differential/statistical testing [R v4.0] -> stage not stated [MNE-Python v0.23.0, lme4 v1.1]

### Causal evidence for a coordinated temporal interplay within the language network. (PNAS 2023)

- DOI: 10.1073/pnas.2306279120 | PMCID: PMC10666120 | PMID: 37963247
- Evidence: For each planned comparison, statistical analyses on reaction times and response accuracy were computed with generalized mixed-effects models fit by maximum likelihood (Laplace Approximation) using the function glmer from the lme4 package ( 146 ) in R ( 147 ) .
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [EEGLAB, FieldTrip, emmeans]

### Large language models show human-like content biases in transmission chain experiments. (PNAS 2023)

- DOI: 10.1073/pnas.2313790120 | PMCID: PMC10622889 | PMID: 37883432
- Evidence: Using the R package lme4, ( 12 ) the general formula can be written as: lmer ( proportion ∼ content + ( 1 | chain _ step ) + ( 1 | chain _ id ) ) .
- Full pipeline: stage not stated [R, lme4]

### Curiosity evolves as information unfolds. (PNAS 2023)

- DOI: 10.1073/pnas.2301974120 | PMCID: PMC10614840 | PMID: 37844235
- Evidence: We created linear and logistic mixed effects regression models with the lme4 package ( 55 ) and obtained P -values with the lmerTest package ( 56 ).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [Matplotlib, Python, seaborn] -> stage not stated [R v4.0]

### Fluctuating selection maintains distinct species phenotypes in an ecological community in the wild. (PNAS 2023)

- DOI: 10.1073/pnas.2222071120 | PMCID: PMC10589706 | PMID: 37812702
- Evidence: To account for temporal variability in selection among the five sampling periods, we also conducted a full general linear mixed model with sampling period as a random effect [i.e., (~1|sampling.period); Table 1 ] using the glmer function in the lme4 package in R ( 85 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [ImageJ, lme4]

### Space weather disrupts nocturnal bird migration. (PNAS 2023)

- DOI: 10.1073/pnas.2306317120 | PMCID: PMC10589677 | PMID: 37812699
- Evidence: We built our mixed-effect models using the “lmer” function (package lme4) ( 36 ) and included nonlinear splines using the “bs” function (package “splines”) ( 70 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.2.0, XGBoost]

### Associations between light exposure and sleep timing and sleepiness while awake in a sample of UK adults in everyday life. (PNAS 2023)

- DOI: 10.1073/pnas.2301608120 | PMCID: PMC10589638 | PMID: 37812713
- Version used: **1.1**
- Evidence: These and the following linear mixed models (LMMs) were computed using the lme4 (1.1 to 27.1), lmerTest (3.1 to 3), and lm.beta (1.6 to 2) packages in R and composed of individuals as a random effect.
- Full pipeline: stage not stated [R v4.0.4, lme4 v1.1]

### Environmental DNA reveals the genetic diversity and population structure of an invasive species in the Laurentian Great Lakes. (PNAS 2023)

- DOI: 10.1073/pnas.2307345120 | PMCID: PMC10500163 | PMID: 37669387
- Evidence: We tested the difference between mtDNA and nuDNA concentration in eDNA samples using a linear mixed model with the ‘lmer’ function in the lme4 package ( 52 ), with sample and site specified as nested random effects.
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.39] -> read trimming [FastQC v0.11.8, Trimmomatic v0.39] -> differential/statistical testing [R v4.1] -> stage not stated [DADA2, lme4]

### Urbanization and edge effects interact to drive mutualism breakdown and the rise of unstable pathogenic communities in forest soil. (PNAS 2023)

- DOI: 10.1073/pnas.2307519120 | PMCID: PMC10483667 | PMID: 37643216
- Evidence: ANOVA test for LMMs was run for values, standardized by the scale function in R, using the lme4 and lmerTest packages ( 99 , 100 ) in R.
- Full pipeline: quality control [R] -> stage not stated [igraph, lme4, vegan]

### Ants combine object affordance with latent learning to make efficient foraging decisions. (PNAS 2023)

- DOI: 10.1073/pnas.2302654120 | PMCID: PMC10468611 | PMID: 37603741
- Evidence: Analysis was carried out in R ( 66 ) (4.2.0) via RStudio 2022.07.0+548, using binomial linear mixed effect models in the package lme4 ( 67 ).
- Full pipeline: differential/statistical testing [R, lme4]

### An illusion of predictability in scientific results: Even experts confuse inferential uncertainty and outcome variability. (PNAS 2023)

- DOI: 10.1073/pnas.2302491120 | PMCID: PMC10438372 | PMID: 37556500
- Evidence: To analyze the calibration task for data scientists and faculty, we fit the following preregistered linear mixed effects model using the lme4 package in R: [1] | error | ∼ ( 1 | participant ) + psup + points where | error | is the absolute value between the true and guessed probability of superiority, psup refers to the true probability of superiority, and points is a binary indicator variable tha...
- Full pipeline: differential/statistical testing [lme4]

### Whole-soil-profile warming does not change microbial carbon use efficiency in surface and deep soils. (PNAS 2023)

- DOI: 10.1073/pnas.2302190120 | PMCID: PMC10410710 | PMID: 37523548
- Evidence: All statistical analyses were performed with R (version 4.1.3) using the lme4 ( 62 ), vegan ( 63 ), lavaan ( 64 ), psych ( 65 ), MuMIn ( 66 ), and rdacca.hp ( 67 ) packages.
- Full pipeline: differential/statistical testing [R v4.1.3, lavaan, lme4]

### A simple mechanism for collective decision-making in the absence of payoff information. (PNAS 2023)

- DOI: 10.1073/pnas.2216217120 | PMCID: PMC10629567 | PMID: 37428910
- Evidence: All data manipulation and statistical analyses were performed in R ( 73 ) (version 4.2.1) using the packages glmmTMB ( 74 ) (version 1.1.4), lme4 ( 75 ) (version 1.1-30), lmerTest ( 76 ) (version 3.1-3), DHARMa ( 77 ) (version 0.4.5), ggplot2 ( 78 ) (version 3.3.6), tidyr ( 79 ) (version 1.2.0), dplyr ( 80 ) (version 1.0.10), readr ( 81 ) (version 2.1.2), ggeffects ( 82 ) (version 1.1.3), survmine...
- Full pipeline: differential/statistical testing [ggplot2, lme4] -> stage not stated [R v4.2.1, data.table, survival (R), tidyverse]

### Adaptive structural and functional evolution of the placenta protects fetal growth in high-elevation deer mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218049120 | PMCID: PMC10288601 | PMID: 37307471
- Evidence: We assessed the significance of fixed effects and interactions within models using type III sum of squares in the car package ( 92 ), and we performed post hoc tests within emmeans and lmerTest packages ( 93 , 94 ) using a Benjamini–Hochberg correction for multiple comparisons.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [ImageJ v2.0.0, featureCounts] -> stage not stated [R v4.0, WGCNA, emmeans, lme4]

### Unraveling female communication through scent marks in the Norway rat. (PNAS 2023)

- DOI: 10.1073/pnas.2300794120 | PMCID: PMC10288631 | PMID: 37307448
- Evidence: Analyses were carried out using R version 4.2.0 ( 78 ) with the lme4 ( 79 ) and emmeans ( 80 ) packages for mixed-effects models and IBM SPSS version 27 (IBM Ltd.) for repeated-measures ANOVAs.
- Full pipeline: differential/statistical testing [R v4.2.0, emmeans, lme4]

### Experimentally simulating the evolution-to-ecology connection: Divergent predator morphologies alter natural food webs. (PNAS 2023)

- DOI: 10.1073/pnas.2221691120 | PMCID: PMC10268251 | PMID: 37276393
- Evidence: All analyses were conducted using R ( 51 ); linear mixed models and generalized linear mixed models were fit using functions in the “lme4” package ( 52 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [emmeans, lme4]

### Teachers recruit mentalizing regions to represent learners' beliefs. (PNAS 2023)

- DOI: 10.1073/pnas.2215015120 | PMCID: PMC10235937 | PMID: 37216526
- Evidence: In our key analysis, we used the lme4 and lmerTest packages in R to estimate a mixed-effects linear model that predicted learners’ posterior belief in the correct answer as a function of time (i.e., how many examples had been presented, coded as a continuous variable), teachers’ predictions about how likely students would be to answer correctly (ranging from 1 = no chance to 5 = certainly, and als...
- Full pipeline: differential/statistical testing [lme4]

### Body size predicts the rate of contemporary morphological change in birds. (PNAS 2023)

- DOI: 10.1073/pnas.2206971120 | PMCID: PMC10193942 | PMID: 37155909
- Evidence: For the Chicago dataset, we used three separate models to estimate changes in each of the three trait variables (tarsus length, bill length, and wing length) as a function of year, sex, and age as fixed effects, with random intercepts and slopes for the effect of year for each species using the lme4 package ( 44 ) in R ( 45 ).
- Full pipeline: stage not stated [R, lme4]

### Machine learning estimation of human body time using metabolomic profiling. (PNAS 2023)

- DOI: 10.1073/pnas.2212685120 | PMCID: PMC10161018 | PMID: 37094145
- Evidence: To test the significance of model improvement by increasing sample number, we ran a linear mixed-effects model to account for between-subjects variation, using the lme4 package (v1.1-30) in R, with the number of samples as a fixed effect (categorical factor) and subject ID as a random effect.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.2.1]

### Group augmentation underlies the evolution of complex sociality in the face of environmental instability. (PNAS 2023)

- DOI: 10.1073/pnas.2212211120 | PMCID: PMC10160950 | PMID: 37094171
- Evidence: All GLMs and GLMMs were fit using the package lme4 ( 110 ).
- Full pipeline: stage not stated [R, lme4]

### Evolution of acoustic signals associated with cooperative parental behavior in a poison frog. (PNAS 2023)

- DOI: 10.1073/pnas.2218956120 | PMCID: PMC10151463 | PMID: 37071680
- Evidence: Model testing was carried out using the packages “lmerTest” ( 46 ) and “emmeans” ( 47 ), with reproductive stage specified as a covariate and individual ID specified as a random effect in all models.
- Full pipeline: stage not stated [R, emmeans, lme4]

### Long-duration wind tunnel flights reveal exponential declines in protein catabolism over time in short- and long-distance migratory warblers. (PNAS 2023)

- DOI: 10.1073/pnas.2216016120 | PMCID: PMC10151508 | PMID: 37068245
- Evidence: We used the function “lmer” (lme4 package, version 1.1-17) and performed backward fixed-effects stepwise model selection on linear mixed-effects models with a α = 0.05 cutoff for fixed effects.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Identifying causal subsequent memory effects. (PNAS 2023)

- DOI: 10.1073/pnas.2120288120 | PMCID: PMC10068819 | PMID: 36952384
- Evidence: We estimate this model using maximum likelihood, as implemented in the R package lme4 ( 145 ).
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [AFNI, ANTs v2.2.0, FSL v5.0.9, FreeSurfer v6.0.1, Nipype v1.1.7, NumPy, R v4.0, fMRIPrep v1.2.6, lme4, tidyverse]

### Transcription factor bHLH121 regulates root cortical aerenchyma formation in maize. (PNAS 2023)

- DOI: 10.1073/pnas.2219668120 | PMCID: PMC10041174 | PMID: 36927156
- Evidence: A cross-year ANOVA of RCA was applied to analyze genotype, treatment, year, and environment for transposon mutant experiments using lmerTest ( 70 ).
- Full pipeline: alignment/mapping [MUSCLE] -> variant calling [R, lme4] -> differential/statistical testing [R] -> stage not stated [Bioconductor]

### A Toll pathway effector protects <i>Drosophila</i> specifically from distinct toxins secreted by a fungus or a bacterium. (PNAS 2023)

- DOI: 10.1073/pnas.2205140120 | PMCID: PMC10041126 | PMID: 36917667
- Evidence: Experiments measuring microbial loads (log2 values) were analyzed using linear models (lm) or linear mixed-effect models (lmer, package lme4) ( 50 ) in order to include the different factors of the experiment, such as the fly line or the treatment, and to include random factors, such as the experimental replicates.
- Full pipeline: differential/statistical testing [lme4]

### Demographic rates reveal the benefits of protected areas in a long-lived migratory bird. (PNAS 2023)

- DOI: 10.1073/pnas.2212035120 | PMCID: PMC10041063 | PMID: 36913571
- Evidence: Models were fitted using the “lme4” package ( 77 ) and the “bobyqa” optimizer.
- Full pipeline: differential/statistical testing [JAGS] -> simulation/modelling [JAGS] -> stage not stated [R, lme4]

### Increased dominance of heat-tolerant symbionts creates resilient coral reefs in near-term ocean warming. (PNAS 2023)

- DOI: 10.1073/pnas.2202388120 | PMCID: PMC9974440 | PMID: 36780524
- Evidence: The changes in symbiont abundance (bleaching) among different sampling times were estimated using mixed linear models with the lmerTest package ( 75 ) for R.
- Full pipeline: quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [R v3.6, emmeans]

### Restricted language access during childhood affects adult brain structure in selective language regions. (PNAS 2023)

- DOI: 10.1073/pnas.2215423120 | PMCID: PMC9963327 | PMID: 36745780
- Evidence: First, for each of the anatomical features, we aggregated the values across all language-relevant ROIs (sum of adjusted volume, average of thickness, sum of cortical area), and fitted linear models using AOA and hemisphere and their interaction as the target variables, and gender and age as covariates, using the lme4 package in R ( 95 ) and the lm function.
- Full pipeline: differential/statistical testing [R, lme4] -> structure determination [FreeSurfer]

### Sharing of misinformation is habitual, not just lazy or biased. (PNAS 2023)

- DOI: 10.1073/pnas.2216614120 | PMCID: PMC9942822 | PMID: 36649414
- Evidence: Specifically, we fit logistic mixed-effects models with functions from the lme4 package ( 34 ).
- Full pipeline: differential/statistical testing [lme4]

### The productive performance of intercropping. (PNAS 2023)

- DOI: 10.1073/pnas.2201886120 | PMCID: PMC9926256 | PMID: 36595678
- Evidence: Analyses were repeated with the function lmer of the more recent lme4 R package with identical outcomes.
- Full pipeline: differential/statistical testing [R] -> stage not stated [lme4]

### Rapid infant learning of syntactic-semantic links. (PNAS 2023)

- DOI: 10.1073/pnas.2209153119 | PMCID: PMC9910616 | PMID: 36574655
- Evidence: The analysis was computed using the lme4 package ( 48 ) in R3.4.4.
- Full pipeline: stage not stated [Python v3.5, lme4]

### Metabolites limiting predator growth wane with prey biodiversity. (PNAS 2024)

- DOI: 10.1073/pnas.2410210121 | PMCID: PMC11670093 | PMID: 39689178
- Evidence: To identify the predictors of nematode body size across different bacterial diversity levels, we performed multiple GLMMs using the “glmer” function from the lme4 package.
- Full pipeline: differential/statistical testing [ggplot2] -> stage not stated [lme4]

### Climate warming drives population trajectories of freshwater fish. (PNAS 2024)

- DOI: 10.1073/pnas.2410355121 | PMCID: PMC11665863 | PMID: 39652750
- Version used: **1.1**
- Evidence: The models were fitted using the “lmer” function in the R package lme4 v.1.1-35.3 ( 76 ), with the formula: water temperature ~ year + (1 | location).
- Full pipeline: quantification [R v0.3.5] -> differential/statistical testing [ggplot2 v3.5.1] -> stage not stated [lme4 v1.1]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: Linear mixed models were constructed for each response variable using the lme4 package in R (version 4.1.0) ( 104 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Urban environments increase generalization of hummingbird-plant networks across climate gradients. (PNAS 2024)

- DOI: 10.1073/pnas.2322347121 | PMCID: PMC11621834 | PMID: 39527750
- Evidence: Thus, we excluded both clades from these analyses, which were conducted using the lmer function from R-package lme4 ( 59 ).
- Full pipeline: stage not stated [lme4]

### Secondary thalamic dysfunction underlies abnormal large-scale neural dynamics in chronic stroke. (PNAS 2024)

- DOI: 10.1073/pnas.2409345121 | PMCID: PMC11573628 | PMID: 39503890
- Version used: **1.1**
- Evidence: We addressed this question with a linear mixed effects model (lme4 v1.1-34) ( 56 ), predicting regional MEG slowing scores as a function of the following fixed effects: ipsilesional thalamus degeneration (one value per patient), proximity to lesion (one value per region × patient), lesion volume (one value per patient), and the interaction between ipsilesional thalamus degeneration score and proxi...
- Full pipeline: registration [FSL] -> differential/statistical testing [lme4 v1.1] -> stage not stated [FreeSurfer]

### Meta-learning of human motor adaptation via the dorsal premotor cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2417543121 | PMCID: PMC11536165 | PMID: 39441634
- Evidence: All data processing and statistical analyses were performed in R version 4.3.2 with the lme4 ( 50 ) and lmerTest ( 51 ) packages.
- Full pipeline: differential/statistical testing [R v4.3.2, lme4] -> stage not stated [Python v3.7.9]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: The model was fitted using the R package “lme4” ( 77 ) with CFU counts as fixed effect and Bee nested within Experiment as random effects.
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Self-views converge during enjoyable conversations. (PNAS 2024)

- DOI: 10.1073/pnas.2321652121 | PMCID: PMC11513911 | PMID: 39401349
- Evidence: Linear mixed effects models were implemented using the lme4 package and were fit with maximum likelihood estimation; degrees of freedom and p-values were approximated using Satterthwaite’s method via the lmerTest package ( 63 , 64 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Asymmetric winter warming reduces microbial carbon use efficiency and growth more than symmetric year-round warming in alpine soils. (PNAS 2024)

- DOI: 10.1073/pnas.2401523121 | PMCID: PMC11513915 | PMID: 39401358
- Evidence: These analyses were performed using the “ piecewiseSEM ”, “ nlme ”, and “ lme4 ” packages ( 88 , 89 ).
- Full pipeline: dimensionality reduction/clustering [phytools] -> stage not stated [R, lme4]

### Intensive leaf cooling promotes tree survival during a record heatwave. (PNAS 2024)

- DOI: 10.1073/pnas.2408583121 | PMCID: PMC11513916 | PMID: 39401366
- Evidence: Linear mixed effects models were employed to analyze changes in the dependent variables g sw , T crit , F v /F m , thermal safety margin, and leaf water potential, using the packages “lmerTest” ( 67 ) and “emmeans” ( 68 ).
- Full pipeline: differential/statistical testing [emmeans, lme4] -> stage not stated [R]

### Manipulating a host-native microbial strain compensates for low microbial diversity by increasing weight gain in a wild bird population. (PNAS 2024)

- DOI: 10.1073/pnas.2402352121 | PMCID: PMC11513901 | PMID: 39401350
- Evidence: Linear mixed models were used to investigate the effect of treatment on alpha diversity across age groups, using the lme4 package ( 92 ).
- Full pipeline: visualisation [vegan] -> stage not stated [Bioconductor, DADA2, R, lme4, phyloseq]

### Tipping the balance between fairness and efficiency through temporoparietal stimulation. (PNAS 2024)

- DOI: 10.1073/pnas.2409395121 | PMCID: PMC11494363 | PMID: 39388264
- Evidence: We analyzed data with hierarchical general(-ized) linear mixed models (GLMMs) as implemented in the lme4 package ( 51 ) in R (version 4.0.0).
- Full pipeline: differential/statistical testing [JAGS] -> stage not stated [R v4.0.0, SPM, lme4]

### Unexpected anthropogenic emission decreases explain recent atmospheric mercury concentration declines. (PNAS 2024)

- DOI: 10.1073/pnas.2401950121 | PMCID: PMC11494326 | PMID: 39378086
- Evidence: We calculated these trends using LME modeling in the R package lme4 ( 74 ).
- Full pipeline: simulation/modelling [MOM6] -> stage not stated [R, lme4]

### Local adaptation, plasticity, and evolved resistance to hypoxic cold stress in high-altitude deer mice. (PNAS 2024)

- DOI: 10.1073/pnas.2412526121 | PMCID: PMC11474095 | PMID: 39352929
- Evidence: Statistical linear mixed-effects models were computed using the lmer function from the lme4 package in R, and the best-fitted model was chosen based on the lowest AIC value.
- Full pipeline: alignment/mapping [featureCounts v2.0.3] -> normalisation [edgeR] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [R, lme4] -> stage not stated [WGCNA]

### Male crickets in poor condition engage in less same-sex sexual behavior. (PNAS 2024)

- DOI: 10.1073/pnas.2408811121 | PMCID: PMC11459157 | PMID: 39312658
- Evidence: We used R version 4.3.1 ( 46 ) loaded with the packages lme4 ( 47 ), MASS ( 48 ), and car ( 49 ), for all analyses.
- Full pipeline: stage not stated [R v4.3.1, lme4]

### Naturalized species drive functional trait shifts in plant communities. (PNAS 2024)

- DOI: 10.1073/pnas.2403120121 | PMCID: PMC11459196 | PMID: 39298470
- Evidence: 4.0.0 and the following R packages: TNRS ( 73 ), lme4 ( 74 ), lmerTest ( 75 ), MuMIN ( 76 ), merTools ( 77 ), ggplot ( 78 ), and cowplot ( 79 ).
- Full pipeline: stage not stated [lme4]

### Childhood PM&lt;sub&gt;2.5&lt;/sub&gt; exposure and upward mobility in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2401882121 | PMCID: PMC11420190 | PMID: 39250663
- Evidence: 1 and 2 are fitted using the R packages lme4 ( 61 ) and npmlreg ( 62 ), respectively.
- Full pipeline: differential/statistical testing [R] -> stage not stated [lme4]

### Economic mobility and parents' opportunity hoarding. (PNAS 2024)

- DOI: 10.1073/pnas.2407230121 | PMCID: PMC11406285 | PMID: 39226344
- Evidence: The analyses in Study 1 were conducted using the “lme4” package in Rv4.3.2 ( 42 ).
- Full pipeline: stage not stated [lme4]

### Parallel ecological and evolutionary responses to selection in a natural bacterial community. (PNAS 2024)

- DOI: 10.1073/pnas.2403577121 | PMCID: PMC11388356 | PMID: 39190353
- Evidence: To test for the effect of copper on siderophore production in compost communities that had either evolved with or without SBW25, we initially used a LMM model (“ lmer ” function in “ lme4 ” package) ( 90 ) with copper × SBW25 presence as fixed explanatory variables, as well as their interaction.
- Full pipeline: quantification [DESeq2, R] -> stage not stated [emmeans, ggplot2, lme4, vegan]

### The consequences of AI training on human decision-making. (PNAS 2024)

- DOI: 10.1073/pnas.2408731121 | PMCID: PMC11331131 | PMID: 39106305
- Evidence: These models were estimated in R using lmerTest package, †† and the following Generalized Linear Model equation: accept ∼ partner ∗ offer ∗ training condition + ( 1 | participant ) Here, our dependent variable “accept” is binary ( 1 for acceptance, 0 for rejection).
- Full pipeline: differential/statistical testing [lme4] -> machine learning [lme4]

### Land conflicts from overlapping claims in Brazil's rural environmental registry. (PNAS 2024)

- DOI: 10.1073/pnas.2407357121 | PMCID: PMC11331109 | PMID: 39110724
- Evidence: Models were fit using the lme4 package ( 51 , 52 ) in R (v.4.3.1), and residuals were checked, showing no biases or heteroscedasticity.
- Full pipeline: stage not stated [R v4.3.1, lme4]

### Competing adaptations maintain nonadaptive variation in a wild cricket population. (PNAS 2024)

- DOI: 10.1073/pnas.2317879121 | PMCID: PMC11317585 | PMID: 39088392
- Evidence: Analysis of female mass across adulthood was performed using a linear mixed model using lme4 ( 57 ).
- Full pipeline: variant calling [VCFtools] -> stage not stated [R v4.0, lme4]

### Sex and mental health are related to subcortical brain microstructure. (PNAS 2024)

- DOI: 10.1073/pnas.2403212121 | PMCID: PMC11295051 | PMID: 39042688
- Evidence: Region-wise analysis used the linear mixed effects model (lmerTest) implemented in R 4.3.0, using all subjects, with family ID included as a random effect.
- Full pipeline: registration [FreeSurfer] -> differential/statistical testing [R v4.3, lme4]

### The physical soldier caste of an invasive, human-infecting flatworm is morphologically extreme and obligately sterile. (PNAS 2024)

- DOI: 10.1073/pnas.2400953121 | PMCID: PMC11295071 | PMID: 39042696
- Evidence: We used parametric bootstrapping from the bootMer function in the lme4 package ( 69 ) to obtain 95% CI considering only fixed-effects-associated error.
- Full pipeline: differential/statistical testing [R] -> stage not stated [ImageJ v1.53t, lme4]

### Flexible oviposition behavior enabled the evolution of terrestrial reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2312371121 | PMCID: PMC11295038 | PMID: 39042675
- Evidence: We analyzed the accumulation of mass over time for submerged egg masses with linear mixed models (LMMs) in the lme4 package ( 50 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2] -> stage not stated [ImageJ, RAxML v1.0.3, emmeans, lme4, phytools]

### Parallel vector memories in the brain of a bee as foundation for flexible navigation. (PNAS 2024)

- DOI: 10.1073/pnas.2402509121 | PMCID: PMC11287249 | PMID: 39008670
- Evidence: All statistical analyses were run on R (v4.0.2, R Core Development Team) with the autoimage, “car,” “circular,” “CircMLE,” ggplot2, “lme4,” “plotrix,” and “shape” plugins.
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [ImageJ v2.3.0]

### Relative decline in density of Northern Hemisphere tree species in warm and arid regions of their climate niches. (PNAS 2024)

- DOI: 10.1073/pnas.2314899121 | PMCID: PMC11252807 | PMID: 38954552
- Evidence: We also calculated species-level means and SD of changes in density by fitting a linear mixed model for each climatic region using lme4 R package ( 64 ).
- Full pipeline: differential/statistical testing [tidyverse] -> visualisation [tidyverse] -> stage not stated [R, lme4]

### Hemispheric functional organization, as revealed by naturalistic neuroimaging, in pediatric epilepsy patients with cortical resections. (PNAS 2024)

- DOI: 10.1073/pnas.2317458121 | PMCID: PMC11252739 | PMID: 38950362
- Evidence: For each level of organization across each atlas, we conducted mixed effects models on the LH and RH data separately, using the R package lme4 ( 60 ).
- Full pipeline: differential/statistical testing [R, lme4] -> structure determination [FreeSurfer] -> stage not stated [AFNI v21.1.10, emmeans]

### Nationwide law enforcement impact on the pet bird trade in China. (PNAS 2024)

- DOI: 10.1073/pnas.2321479121 | PMCID: PMC11194575 | PMID: 38857393
- Evidence: To robustly evaluate the impact of conservation enforcement, we analyzed whether national protection level and other variables are related to species abundance trends in the bird markets before and after the NSEA after accounting for possible confounding factors, by constructing the LMMs using the “lmer” function in the package “lmerTest” ( 59 ).
- Full pipeline: quantification [lme4] -> differential/statistical testing [R]

### Juvenile social play predicts adult reproductive success in male bottlenose dolphins. (PNAS 2024)

- DOI: 10.1073/pnas.2305948121 | PMCID: PMC11194510 | PMID: 38857400
- Evidence: We used linear mixed effects models [ lmer function in R package lme4 ( 87 )] to examine the development of male social bond strength and social activity budgets that largely consist of social play, from the early to late juvenile periods (N = 27 males) and late juvenile to early adult periods (N = 31 males).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2] -> stage not stated [R]

### Limited intraspecific variation in drought resistance along a pronounced tropical rainfall gradient. (PNAS 2024)

- DOI: 10.1073/pnas.2316971121 | PMCID: PMC11161779 | PMID: 38809703
- Evidence: Survival, growth, and traits models were fit using the lme4 package ( 55 ) and lmerTest package ( 56 ) in R version 4.1.2 ( 57 ).
- Full pipeline: stage not stated [R v4.1.2, lme4]

### Puppy whines mediate maternal behavior in domestic dogs. (PNAS 2024)

- DOI: 10.1073/pnas.2316818121 | PMCID: PMC11145252 | PMID: 38768360
- Evidence: Finally, to test whether within litters, interindividual variation in puppy body weight predicted interindividual puppy whine acoustics, we performed linear mixed models [fitted with lme4 R package ( 58 )] for each of our five selected acoustic variables.
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [R, lme4]

### Ripple effects of hospital team faultlines on patient outcomes (PNAS 2024)

- DOI: None | PMCID: PMC10666119 | PMID: None
- Evidence: For our GLMM, we treated the individual patient binary outcomes as a level-1 variable nested within hospital units and aggregated unit incivility as a level-2 variable using the lme4 package ( 34 ) in R ( 29 ).
- Full pipeline: dimensionality reduction/clustering [R] -> stage not stated [lavaan, lme4]

### Detecting inbreeding depression in structured populations. (PNAS 2024)

- DOI: 10.1073/pnas.2315780121 | PMCID: PMC11087799 | PMID: 38687793
- Evidence: Estimates for the LMs were obtained with the lm function of R, while estimates for the mixed models were obtained with the lmer function of the lme4 package or the lmm.aireml function of the gaston package if the model contained a GRM.
- Full pipeline: stage not stated [GCTA, PLINK, lme4]

### The thermoneutral zone in women takes an "arctic" shift compared to men. (PNAS 2024)

- DOI: 10.1073/pnas.2311116121 | PMCID: PMC11087792 | PMID: 38683977
- Version used: **3.1.3**
- Evidence: Exploratory outcomes measured at each T a , including T core , T sk, blood pressure, heart rate, EMG, and self-reported thermal comfort were assessed using linear mixed effect models with an interaction between T a and sex and a random intercept by participant (lmerTest v3.1.3 and lme4 v1.1.34 packages in R).
- Full pipeline: differential/statistical testing [lme4 v3.1.3] -> machine learning [ImageJ]

### Evolutionarily conserved neural responses to affective touch in monkeys transcend consciousness and change with age. (PNAS 2024)

- DOI: 10.1073/pnas.2322157121 | PMCID: PMC11067024 | PMID: 38648473
- Evidence: These models were implemented in R version 4.3.1 ( 112 ) using the lmer function from the package lme4 ( 113 ).
- Full pipeline: stage not stated [AFNI, CIVET, Python, R v4.3.1, emmeans, lme4]

### The evolutionary genomics of adaptation to stress in wild rhizobium bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2311127121 | PMCID: PMC10990125 | PMID: 38507447
- Version used: **1.1**
- Evidence: We analyzed Ni tolerance of Mesorhizobium isolates using linear models and linear mixed models implemented in the R package lme4 v.
- Full pipeline: quality control [Prokka v1.13.3] -> read trimming [MUSCLE] -> alignment/mapping [MAFFT v7.475, MUSCLE] -> differential/statistical testing [lme4 v1.1] -> visualisation [R] -> stage not stated [RAxML, SPAdes v3.14.1]

### The circadian molecular clock in the suprachiasmatic nucleus is necessary but not sufficient for fear entrainment. (PNAS 2024)

- DOI: 10.1073/pnas.2316841121 | PMCID: PMC10990155 | PMID: 38502706
- Evidence: Linear mixed-effects models (LMM) were used to analyze differences in the percent of locomotor and feeding activity at specific phases, and in FFT power across the protocol stages using the lme4 package for R ( 28 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [ImageJ, emmeans]

### Changes in spatial self-consciousness elicit grid cell-like representation in the entorhinal cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2315758121 | PMCID: PMC10962966 | PMID: 38489383
- Version used: **1.1.26**
- Evidence: To maximally utilize the data points, the R package for mixed-effects regressions (lme4, v1.1.26) was used to statistically assess the condition-wise difference ( SI Appendix , Table S1 ).
- Full pipeline: differential/statistical testing [lme4 v1.1.26] -> stage not stated [FreeSurfer v6.0.0, R, SPM]

### Using global remote camera data of a solitary species complex to evaluate the drivers of group formation. (PNAS 2024)

- DOI: 10.1073/pnas.2312252121 | PMCID: PMC10962950 | PMID: 38466845
- Evidence: Modeling was conducted in R version 4.3.1 using the function glmer in package lme4 ( 39 , 40 ).
- Full pipeline: stage not stated [R v4.3.1, lme4]

### The effects of mnemonic variability and spacing on memory over multiple timescales. (PNAS 2024)

- DOI: 10.1073/pnas.2311077121 | PMCID: PMC10962934 | PMID: 38470923
- Evidence: We used R packages including lme4, eemeans, rstatix, sjPlot, and ggplot2.
- Full pipeline: stage not stated [ggplot2, lme4]

### Learning shapes the development of migratory behavior. (PNAS 2024)

- DOI: 10.1073/pnas.2306389121 | PMCID: PMC10962998 | PMID: 38437530
- Evidence: The 95% CIs for all fixed effects included in the model were estimated using semiparametric bootstrapping (n = 1,000 simulations) using the bootMer function in the lme4 package (v 1.1-31) of R version 4.2.2 ( 62 ).
- Full pipeline: simulation/modelling [R v4.2.2, lme4]

### Diverging neural dynamics for syntactic structure building in naturalistic speaking and listening. (PNAS 2024)

- DOI: 10.1073/pnas.2310766121 | PMCID: PMC10945772 | PMID: 38442171
- Evidence: We ran a linear mixed-effects model with lme4 [version 1.1-26 ( 88 )] in R (version 4.0.3).
- Full pipeline: differential/statistical testing [R v4.0.3, lme4] -> stage not stated [FreeSurfer, Nilearn, Python, TensorFlow, emmeans]

### Fatigue and vigilance in medical experts detecting breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2309576121 | PMCID: PMC10945845 | PMID: 38437559
- Evidence: The analysis was performed using R software, with the multilevel models being fitted with the “lme4” package.
- Full pipeline: stage not stated [lme4]

### Decoupling of bird migration from the changing phenology of spring green-up. (PNAS 2024)

- DOI: 10.1073/pnas.2308433121 | PMCID: PMC10963019 | PMID: 38437528
- Evidence: We used the “lme4” ( 68 ) package in R ( 69 ) and coded this model separately for each species as: model = lmer (migration midpoint day j,k ~ mid-green-up day j,k * type j,k + latitude j + longitude j + (1|year k ) where indices j = pixel, and k = year ( Fig S4 ).
- Full pipeline: stage not stated [R, lme4]

### Pervasive mimicry in flight behavior among aposematic butterflies. (PNAS 2024)

- DOI: 10.1073/pnas.2300886121 | PMCID: PMC10945825 | PMID: 38408213
- Evidence: WBF and wing angles were modeled separately against mimicry ring, species and sex, using a linear mixed-effects model implemented in the “lme4” package ( 80 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [ImageJ, R]

### An evolutionary innovation for mating facilitates ecological niche expansion and buffers species against climate change. (PNAS 2024)

- DOI: 10.1073/pnas.2313371121 | PMCID: PMC10927580 | PMID: 38408245
- Evidence: We then compared mass loss between manipulated and control males using linear mixed-effects models [“ lme4 ” ( 50 )] ( SI Appendix ).
- Full pipeline: differential/statistical testing [lme4]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Evidence: We constructed GLM in lme4 ( 118 ) to evaluate predictors of species richness.
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### The social transmission of empathy relies on observational reinforcement learning. (PNAS 2024)

- DOI: 10.1073/pnas.2313073121 | PMCID: PMC10907261 | PMID: 38381794
- Evidence: We performed linear mixed models (LMM, “lme4”) in R v.4.1.1 (R Development Core Team, 2012) for the behavioral analyses on empathy ratings and prediction ratings as the dependent variables to investigate observational learning.
- Full pipeline: stage not stated [SPM, lme4]

### Self-organization as a mechanism of resilience in dryland ecosystems. (PNAS 2024)

- DOI: 10.1073/pnas.2305153121 | PMCID: PMC10861902 | PMID: 38300860
- Version used: **1.1**
- Evidence: These models were fitted using the R package lme4 v1.1-29 ( 42 ).
- Full pipeline: stage not stated [R, lme4 v1.1]

### Climate change drives migratory range shift via individual plasticity in shearwaters. (PNAS 2024)

- DOI: 10.1073/pnas.2312438121 | PMCID: PMC10861922 | PMID: 38285933
- Evidence: To investigate range shift further, we constructed linear mixed-effects models using the “lme4” package ( 60 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v3.4.3]

### Visual guidance fine-tunes probing movements of an insect appendage. (PNAS 2024)

- DOI: 10.1073/pnas.2306937121 | PMCID: PMC10861887 | PMID: 38285936
- Evidence: To statistically analyze the alignment of the head–thorax body axis direction, as well as the proboscis probing track direction on the flower with the pattern orientation, we used generalized linear mixed-effects model in R v4.1.2 (R Foundation for Statistical Computing) using the package “lme4” with the formula sector choice ∼ 1 | animalID .
- Full pipeline: alignment/mapping [R v4.1, lme4] -> differential/statistical testing [R v4.1, lme4] -> stage not stated [DeepLabCut]

### Social anxiety disorder-associated gut microbiota increases social fear. (PNAS 2024)

- DOI: 10.1073/pnas.2308706120 | PMCID: PMC10769841 | PMID: 38147649
- Evidence: To account for the nested donor structure, we used the linear mixed-effects modelling framework provided in the lme4 package in R ( 69 ), with the following model: feature ~ Treatment + (1|donor_ID).
- Full pipeline: differential/statistical testing [Python, SciPy v1.9.3, lme4] -> stage not stated [R v4.2.2, ggplot2]

### Hormonal mechanisms of women's risk in the face of traumatic stress. (PNAS 2025)

- DOI: 10.1073/pnas.2524903122 | PMCID: PMC12745815 | PMID: 41397126
- Evidence: The primary statistical tests were run in R version 4.3.0, using linear mixed effects models in the lme4 package.
- Full pipeline: differential/statistical testing [R v4.3.0, lme4] -> stage not stated [SPM, fMRIPrep v20.2.3]

### Evolved birth physiology meets modern birth practice: Sustained effects of planned cesarean delivery on child hair cortisol in Brazil. (PNAS 2025)

- DOI: 10.1073/pnas.2519365122 | PMCID: PMC12718353 | PMID: 41359854
- Evidence: To assess the association between birth mode and longitudinally measured cortisol, we fit a linear mixed-effects model using the lme4 package (version 1.1.37) ( 44 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.5.0, emmeans]

### Demographic responses of North Atlantic seabirds to seasonal ocean warming. (PNAS 2025)

- DOI: 10.1073/pnas.2507531122 | PMCID: PMC12718362 | PMID: 41359851
- Evidence: Models were fitted using “lme4” package version 1.1 to 27.1.
- Full pipeline: stage not stated [R, lme4]

### Mysterious illnesses have supernatural and ritualistic cures: Evidence from 3,655 century-old Irish folk cures. (PNAS 2025)

- DOI: 10.1073/pnas.2511006122 | PMCID: PMC12704799 | PMID: 41325525
- Evidence: Therefore, we ran mixed effects logistic regression models with the lme4 package ( 46 ) to test these hypotheses.
- Full pipeline: differential/statistical testing [R v4.1, lme4]

### Precipitation increase promotes soil organic carbon formation and stability via the mycorrhizal fungal pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2519072122 | PMCID: PMC12685053 | PMID: 41289393
- Evidence: To estimate the effects of Pi on plant, root, AMF, microbial, and soil variables, we employed linear mixed-effects models with Pi as a fixed effect and block as a random effect using the “lmer” function from the “lme4” package.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R, metafor, pheatmap, vegan]

### Cognitive correlates of human endurance. (PNAS 2025)

- DOI: 10.1073/pnas.2512055122 | PMCID: PMC12663999 | PMID: 41248292
- Evidence: We used linear mixed effect models (LMM) in R Version 4.2.0 (R CoreTeam 2020) with the lme4 package ( 90 ) to compare markers of effort and fatigability while taking into account repeated measures of the same individuals (treated as the random intercept).
- Full pipeline: differential/statistical testing [lme4]

### Morphological and genomic responses to hurricanes arise and persist during a biological invasion. (PNAS 2025)

- DOI: 10.1073/pnas.2517322122 | PMCID: PMC12663987 | PMID: 41248293
- Evidence: Therefore, we assessed the effect of hurricane history and genetic ancestry on A. sagrei morphology with a series of linear mixed models using the lmer() function in the lme4 package in R ( 54 ).
- Full pipeline: normalisation [ImageJ] -> stage not stated [GEMMA v0.94, R, lme4]

### General laws of biodiversity: Climatic niches predict plant range size and ecological dominance globally. (PNAS 2025)

- DOI: 10.1073/pnas.2517585122 | PMCID: PMC12646267 | PMID: 41218123
- Evidence: We performed GLMM using the R package lme4 ( 86 ).
- Full pipeline: stage not stated [R, emmeans, lme4]

### Testing whether connectivity stabilizes metacommunities and rescues declining diversity in a 25-y grassland study. (PNAS 2025)

- DOI: 10.1073/pnas.2520768122 | PMCID: PMC12646309 | PMID: 41213018
- Evidence: All statistical analyses were performed in R version 4.4.1 (2024-06-14) ( 56 ) using the “lme4,” “lmerTest,” “purr,” “car,” and “broom” packages with the “officer,” and “patchwork” further used for data visualization ( 57 – 63 ).
- Full pipeline: differential/statistical testing [R v4.4.1, lme4] -> visualisation [R v4.4.1, lme4]

### A species interaction kick-starts ecological speciation in allopatry. (PNAS 2025)

- DOI: 10.1073/pnas.2506625122 | PMCID: PMC12557528 | PMID: 41082661
- Evidence: Because the main LMM fitted with lmer() from the lme4 package resulted in singular fits, we used the blmer() function from the blme R- package ( 107 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [BCFtools, GATK, SAMtools, VCFtools, lme4]

### Smartphone use in a large US adult population: Temporal associations between objective measures of usage and mental well-being. (PNAS 2025)

- DOI: 10.1073/pnas.2427311122 | PMCID: PMC12582163 | PMID: 41082655
- Evidence: We used multilevel regression models R v.4.41 using the “lme4”package [v.
- Full pipeline: differential/statistical testing [lme4]

### Female membrane proteins regulate postmating ovulation in &lt;i&gt;Drosophila melanogaster&lt;/i&gt; by ovulin-dependent and -independent pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2508783122 | PMCID: PMC12452909 | PMID: 40920921
- Evidence: For ovulation assays using mates of control and ovulin-null males, data were analyzed in R using the package lme4 to construct a mixed effects logistic regression with female genotype and male genotype included as fixed effects and experimental replicate included as a random effect.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> variant calling [lme4] -> differential/statistical testing [emmeans, lme4] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.5.5]

### Joint models reveal human subcortical underpinnings of choice and learning behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2502269122 | PMCID: PMC12435315 | PMID: 40911596
- Evidence: We used the implementation in R packages “lme4” and “lmerTest” ( 122 , 123 ).
- Full pipeline: registration [ANTs] -> stage not stated [FSL, Nipype v1.5.1, fMRIPrep v20.2.0, lme4]

### Rising global temperatures reduce soil microbial diversity over the long term. (PNAS 2025)

- DOI: 10.1073/pnas.2426200122 | PMCID: PMC12415293 | PMID: 40854119
- Evidence: The analysis was conducted with the restricted maximum likelihood estimation with the lme4 package ( 67 ).
- Full pipeline: stage not stated [R, lme4, metafor]

### Hippocampal mismatch signals are based on episodic memories and not schematic knowledge. (PNAS 2025)

- DOI: 10.1073/pnas.2503535122 | PMCID: PMC12403140 | PMID: 40844765
- Evidence: Participants’ recall of all the video clips they watched inside the scanner was analyzed using logistic mixed effect models estimated with the lme4 ( 88 ) package available in R.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Aphid herbivory on macrophytes drives adaptive evolution in an aquatic community via indirect effects. (PNAS 2025)

- DOI: 10.1073/pnas.2502742122 | PMCID: PMC12403121 | PMID: 40838887
- Evidence: All linear mixed-effects models and generalized linear mixed-effects models were run using lme4 package (v 1.1-36).
- Full pipeline: quality control [BWA, SAMtools, Trim Galore v0.6.1] -> read trimming [BWA, SAMtools, Trim Galore v0.6.1] -> alignment/mapping [BWA, SAMtools, Trim Galore v0.6.1] -> differential/statistical testing [lme4]

### Asymmetric development and function of paired sperm-storage organs in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2512096122 | PMCID: PMC12403100 | PMID: 40828028
- Version used: **1.1**
- Evidence: Statistical analysis was performed in R v4.4.1 with the following packages: tidyverse v2.0.0, lme4 v1.1–35.5, and emmeans v1.10.6.
- Full pipeline: differential/statistical testing [R v4.4, emmeans v1.10.6, lme4 v1.1, tidyverse v2.0.0]

### Cognitive bridge between geometric and numerical learning in monkeys. (PNAS 2025)

- DOI: 10.1073/pnas.2502101122 | PMCID: PMC12403012 | PMID: 40825124
- Evidence: All data processing, analyses, and visualizations were performed in R using libraries dplyr , tidyr , ggplot2 , and lme4 .
- Full pipeline: visualisation [ggplot2, lme4, tidyverse]

### An information-theoretic foreshadowing of mathematicians' sudden insights. (PNAS 2025)

- DOI: 10.1073/pnas.2502791122 | PMCID: PMC12415256 | PMID: 40825142
- Evidence: All analyses were conducted in R using the lmerTest package.
- Full pipeline: stage not stated [lme4]

### Layer 1 NDNF interneurons form distinct subpopulations with opposite activation patterns during sleep in freely behaving mice. (PNAS 2025)

- DOI: 10.1073/pnas.2503139122 | PMCID: PMC12377762 | PMID: 40811472
- Evidence: Generalized linear mixed-effects model in R using the lme4 package and Satterthwaite approximation ( 54 ) was performed when repeated measurements were included and/or when replicates in one or multiple conditions were missing.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [lme4] -> visualisation [ImageJ] -> stage not stated [Python]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Evidence: ...alized linear mixed-effect model (GLMM) for the categorical trait petal-edge-shape with the functions lmer and glmer , respectively, in the R package lme4 ( 89 ) (for model details, see SI Appendix , Table S14 ).
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

### What people learn from punishment: A cognitive model. (PNAS 2025)

- DOI: 10.1073/pnas.2500730122 | PMCID: PMC12358846 | PMID: 40758880
- Evidence: Across studies 1 to 3, we modeled belief updates (posterior - prior) as the primary outcome using mixed-effects linear or logistic regressions (lme4/lmerTest) with maximal random-effects structures (pruned only if needed for convergence; 105 ). “I don’t know” responses were scored at each scale’s midpoint, and in some analyses, mild and harsh punishments were collapsed into “punish.” In study 4, w...
- Full pipeline: differential/statistical testing [lme4]

### Indigenous territories and protected areas are crucial for ecosystem connectivity in the Amazon basin. (PNAS 2025)

- DOI: 10.1073/pnas.2418189122 | PMCID: PMC12337320 | PMID: 40720645
- Evidence: The analysis was implemented using the “glmer.nb” function from the “lme4” v.12 package ( 107 ) in R.
- Full pipeline: visualisation [ggplot2 v3.5.1, tidyverse v1.3.1] -> stage not stated [QGIS, emmeans, lme4]

### Effects of the gut microbiota on placental angiogenesis and intrauterine growth in gnotobiotic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426341122 | PMCID: PMC12318179 | PMID: 40711921
- Evidence: Statistical significance was assigned to P -values < 0.05 using either nonparametric Wilcoxon test for maternal measurements and generalized linear mixed models for measurements involving multiple litter members to account for litter effects, using the lmerTest package in R.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, lme4] -> stage not stated [QuPath v0.4.4]

### Human land use promotes range expansion of soil protists from temperate to subtropical regions in China. (PNAS 2025)

- DOI: 10.1073/pnas.2413220122 | PMCID: PMC12318147 | PMID: 40694336
- Evidence: Linear mixed effects models were used to inspect whether community distances of total and different functional groups of protists in human land-use systems were lower than those in forests (biological homogenization impacts) with “city identity” included as random term (“lmer” in package “lme4”) ( 60 ).
- Full pipeline: differential/statistical testing [R v3.6.2, emmeans, lme4] -> stage not stated [QIIME 2 v1.90, vegan]

### Norms emerge through iterated learning. (PNAS 2025)

- DOI: 10.1073/pnas.2504178122 | PMCID: PMC12304962 | PMID: 40680030
- Evidence: The models were fitted using the lme4 package in R, specified as follows: Open response score ~ DV type * Generation + (1|Scenario) Judgment rating ~ Generation + (1|Scenario) The overall pattern of results was consistent across scenarios, so we report and discuss the combined results in the main text.
- Full pipeline: stage not stated [lme4]

### Mutualisms within light microhabitats are associated with sensory convergence in a mimetic butterfly community. (PNAS 2025)

- DOI: 10.1073/pnas.2422397122 | PMCID: PMC12305024 | PMID: 40663600
- Evidence: To test whether the visual environment varied along the transect according to topography, canopy openness, and height from the ground, linear mixed models were constructed using the function lmer in the lme4 package in R ( 59 , 60 ).
- Full pipeline: stage not stated [ImageJ, Python, R, lme4, phytools]

### Predictive processes shape individual musical preferences. (PNAS 2025)

- DOI: 10.1073/pnas.2500494122 | PMCID: PMC12304940 | PMID: 40663615
- Evidence: To test the contribution of IC and Entropy in participants’ choice in MUSICOS, we performed linear mixed modeling in R (version 4.0.2) ( https://www.npackd.org/p/r/4.0.2 ) and RStudio ( https://www.rstudio.com/ ) using the lme4 package ( 61 ) with participants’ choices as dependent variable.
- Full pipeline: differential/statistical testing [SPM] -> stage not stated [R v4.0.2, lme4]

### Dissociable glucocorticoid and noradrenergic effects on parochial cooperation and competition in intergroup conflict. (PNAS 2025)

- DOI: 10.1073/pnas.2502257122 | PMCID: PMC12304886 | PMID: 40658855
- Evidence: We ran separate LMEMs for the two dependent variables, “percentage of budget allocated to the within-group pool” and “percentage of budget allocated to the between-group pool”, using the lme4 package in R ( 47 ).
- Full pipeline: stage not stated [R, lme4]

### Divergent oxygen trends in ice-covered lakes driven by ice-cover decline and ecological memory. (PNAS 2025)

- DOI: 10.1073/pnas.2426140122 | PMCID: PMC12260399 | PMID: 40601624
- Evidence: HLMs were fitted using the “lme4” package in R ( 78 ), with year as fixed effect and random intercepts for each lake.
- Full pipeline: stage not stated [R v4.2, emmeans, lme4]

### The epigenetic impacts of pubertal acceleration following early caregiver disruptions. (PNAS 2025)

- DOI: 10.1073/pnas.2504216122 | PMCID: PMC12260577 | PMID: 40587802
- Evidence: Using the lme4 package, we first conducted generalized linear models (GLMs) to examine associations between disruptions in the caregiving environment and patterns of pubertal development, and subsequent associations between patterns of pubertal development and telomere erosion ( 55 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Contribution of glutamatergic projections to neurons in the nonhuman primate substantia nigra pars reticulata for reactive inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2427032122 | PMCID: PMC12232709 | PMID: 40569385
- Evidence: For LMM and GLMM analyses, we used the lme4 ( 66 ), pbkrtest ( 67 ), emmeans ( 68 ), and brms ( 69 ) packages in RStudio.
- Full pipeline: stage not stated [brms, emmeans, lme4]

### Winters restrict a climate change-driven butterfly range expansion despite rapid evolution of seasonal timing traits. (PNAS 2025)

- DOI: 10.1073/pnas.2418392122 | PMCID: PMC12232556 | PMID: 40549916
- Version used: **1.1.32**
- Evidence: We used R 4.2.2 ( 72 ) for analyses and the package lme4 1.1.32 ( 73 ) for fitting models.
- Full pipeline: differential/statistical testing [afex v1.2.1, emmeans v1.8.5] -> stage not stated [R, lme4 v1.1.32]

### Linking pregnancy- and birth-related risk factors to a multivariate fusion of child cortical structure. (PNAS 2025)

- DOI: 10.1073/pnas.2422281122 | PMCID: PMC12207422 | PMID: 40526716
- Evidence: Associations between the pregnancy- and birth-related dimensions and each of the CCs were tested by linear mixed-effects modeling using the “lmer” function from the lme4-package (version 1.1-29).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [FreeSurfer v7.1]

### Longitudinal trajectories of brain development from infancy to school age and their relationship with literacy development. (PNAS 2025)

- DOI: 10.1073/pnas.2414598122 | PMCID: PMC12184337 | PMID: 40493188
- Evidence: To generate longitudinal trajectories (i.e., growth curves), we next submitted cleaned, longitudinal structural and white matter organization estimates to linear mixed effects models using linear, logarithmic, and quadratic functions from the R “lme4” package ( 141 ).
- Full pipeline: dimensionality reduction/clustering [ANTs, FSL, R] -> differential/statistical testing [R, lme4] -> simulation/modelling [lme4] -> stage not stated [Docker v1.1.0, FreeSurfer v7.3, MRtrix3]

### Longitudinal associations between birth-to-six cortical growth and childhood neurocognitive function. (PNAS 2025)

- DOI: 10.1073/pnas.2418176122 | PMCID: PMC12146774 | PMID: 40424148
- Evidence: In order to assess when cortical thickness development was most predictive of later working memory, we then constructed piecewise hierarchical linear models (HLMs) of cortical thickness change over time using the lme4 package ( 55 ) in R.
- Full pipeline: alignment/mapping [FreeSurfer] -> registration [FreeSurfer] -> differential/statistical testing [FSL, lme4] -> stage not stated [fMRIPrep v20.0.7]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: All analyses were performed with the function lme4::lm or lme4::lmer in R ( 45 , 46 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### AI assistance improves people's ability to distinguish correct from incorrect eyewitness lineup identifications. (PNAS 2025)

- DOI: 10.1073/pnas.2503971122 | PMCID: PMC12130855 | PMID: 40388624
- Evidence: To investigate this question, we ran a mixed-effects model using the lme4 package ( 48 ) predicting reliance from the factors of AI-assistance and statement type, with random effects of participant and lineup.
- Full pipeline: differential/statistical testing [lme4]

### Linked nitrogen and carbon dynamics reveal distinct pools and patterns in a deep, weathered bedrock rhizosphere. (PNAS 2025)

- DOI: 10.1073/pnas.2400452122 | PMCID: PMC12087964 | PMID: 40343996
- Evidence: Using linear mixed models ( lme4 package) in R (v4.2.2), we explored the effects of season, depth and year (fixed effects), and Port ID (random effect) on TDN and NH 4 + concentrations in the VMS ( 66 , 67 ).
- Full pipeline: stage not stated [R v4.2.2, emmeans, lme4]

### Cryptic genetic variation in brain gene expression precedes the evolution of cannibalism in spadefoot toad tadpoles. (PNAS 2025)

- DOI: 10.1073/pnas.2418431122 | PMCID: PMC12088425 | PMID: 40294283
- Evidence: Second, we applied a generalized linear mixed-effect model fitted to a binomial distribution using the R packages lme4 ( 81 ) and lmerTest ( 82 ).
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [BUSCO, DESeq2, survival (R)]

### The Beholder's Share: Bridging art and neuroscience to study individual differences in subjective experience. (PNAS 2025)

- DOI: 10.1073/pnas.2413871122 | PMCID: PMC12012540 | PMID: 40193608
- Evidence: We used a linear modeling package made for the programming language R: lme4 ( 50 ).
- Full pipeline: registration [AFNI] -> differential/statistical testing [lme4] -> structure determination [FreeSurfer v6.0.1] -> stage not stated [ANTs v2.2.0, FSL v5.0.9, Nilearn v0.4.2, Nipype v1.1.1, fMRIPrep]

### A disease-specific convergence of host and Epstein-Barr virus genetics in multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418783122 | PMCID: PMC12002260 | PMID: 40184175
- Evidence: The mixed-effect multiple linear regression analyses were performed using the R program, Version 1.1.456 (function “lmer” from “lme4” package).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [Cytoscape v3.9.1, R v1.1.456, VEP]

### microRNA-218-5p coordinates scaling of excitatory and inhibitory synapses during homeostatic synaptic plasticity. (PNAS 2025)

- DOI: 10.1073/pnas.2500880122 | PMCID: PMC12002172 | PMID: 40172961
- Evidence: To correctly correct for batch effects, we implemented linear mixed models using the lmer-function from the R-packages lme4 and lmerTest.
- Full pipeline: alignment/mapping [edgeR] -> normalisation [edgeR, lme4] -> differential/statistical testing [R v4.0, edgeR] -> stage not stated [emmeans]

### Validating new limits for human thermoregulation. (PNAS 2025)

- DOI: 10.1073/pnas.2421281122 | PMCID: PMC12002229 | PMID: 40163728
- Evidence: The hourly rate of change in these variables was then compared between conditions using linear mixed effects models fit via the “lme4” package ( 59 ) with a fixed effect for condition and a random intercept for participant id to account for the crossover design.
- Full pipeline: differential/statistical testing [lme4] -> simulation/modelling [R] -> visualisation [ggplot2] -> stage not stated [survival (R)]

### A global estimate of multiecosystem photosynthesis losses under microplastic pollution. (PNAS 2025)

- DOI: 10.1073/pnas.2423957122 | PMCID: PMC11929485 | PMID: 40063820
- Evidence: The meta-analysis was conducted with RStudio in R version 4.0.3 with the “meta”, “metafor”, “lme4”, “nlme”, “ggplot2,” and “multcomp” packages.
- Full pipeline: stage not stated [Python v3.8.8, R v4.0.3, ggplot2, lme4, metafor, scikit-learn v1.2.2]

### Cell type and region-specific transcriptional changes in the endometrium of women with RIF identify potential treatment targets. (PNAS 2025)

- DOI: 10.1073/pnas.2421254122 | PMCID: PMC11929460 | PMID: 40063812
- Version used: **1.1**
- Evidence: DEGs between cell types and disease state were identified using a linear mixed effect model [package lme4 (v 1.1-35.2) ( 32 )] treating Patient ID as a random effect.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.1] -> differential/statistical testing [lme4 v1.1] -> stage not stated [R, Seurat v5.0.3]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Evidence: We performed linear mixed models, using the lme4 package in R ( 94 ) on populations from each range to extract variance components attributed to within- and among-population variation for each coverage window.
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Mycorrhiza increases plant diversity and soil carbon storage in grasslands. (PNAS 2025)

- DOI: 10.1073/pnas.2412556122 | PMCID: PMC11848320 | PMID: 39937867
- Version used: **1.1**
- Evidence: All statistical analyses except SEM were conducted in R, and the following packages: argicolae v.1.3-5, lme4 v.1.1-30, ggtext v.0.1.1, ggplot2 v.3.3.5, ggpubr v.0.4.0, tidyr v.1.1.4, and vegan v.2.5-7 were used.
- Full pipeline: differential/statistical testing [ggplot2 v3.3.5, ggpubr v0.4.0, lme4 v1.1, tidyverse v1.1.4]

### Interconnecting fragmented forests: Small and mobile birds are cornerstones in the plant-frugivore meta-network. (PNAS 2025)

- DOI: 10.1073/pnas.2415846122 | PMCID: PMC11848312 | PMID: 39946536
- Evidence: Linear mixed-effects models were fitted using the package “lme4” ( 79 ).
- Full pipeline: quantification [R] -> differential/statistical testing [lme4]

### Substrate and climate determine terrestrial litter decomposition. (PNAS 2025)

- DOI: 10.1073/pnas.2420664122 | PMCID: PMC11848321 | PMID: 39932997
- Evidence: These analyses were conducted by using piecewiseSEM ( 61 ), nlme, and lme4 ( 62 ) packages.
- Full pipeline: stage not stated [R, lme4]

### Growth decline in European beech associated with temperature-driven increase in reproductive allocation. (PNAS 2025)

- DOI: 10.1073/pnas.2423181122 | PMCID: PMC11804683 | PMID: 39874289
- Evidence: We used generalized linear mixed models (GLMMs) implemented via the “lme4” package ( 70 ) with plant ID and site ID as random intercept and year as random slope.
- Full pipeline: stage not stated [R, lme4]

### No gender differences in attraction to young partners: A study of 4500 blind dates. (PNAS 2025)

- DOI: 10.1073/pnas.2416984122 | PMCID: PMC11804577 | PMID: 39869809
- Evidence: Specifically, we used the code (1 | participant_ID) + (1 | partner_ID) + (1 | dyad_ID) in the lme4 package ( 27 ).
- Full pipeline: stage not stated [lme4]

### Floodplain forests drive fruit-eating fish diversity at the Amazon Basin-scale. (PNAS 2025)

- DOI: 10.1073/pnas.2414416122 | PMCID: PMC11761662 | PMID: 39805021
- Evidence: To examine the effects of floodplain ecosystem and landscape characteristics on frugivorous fish species-richness (response variable), we performed linear mixed effects models using the “lmer” function from the R package lme4 ( 80 ) with flooded forest area, forest tree diversity, biogeochemistry/water color, flood duration, elevation, and Strahler’s river order as explanatory fixed effects.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Increasing pesticide diversity impairs soil microbial functions. (PNAS 2025)

- DOI: 10.1073/pnas.2419917122 | PMCID: PMC11745395 | PMID: 39786931
- Evidence: To assess the effects of pesticide diversity on soil properties, microbial diversity, and network parameters, linear mixed-effects models were applied within each of the two N input levels (with and without N addition) using the R package “lme4” ( 104 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.2.3, eggNOG, igraph]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Evidence: To investigate variation in knockdown times by treatment, we used a linear mixed-effects model implemented using the “lme4” package in R ( 126 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### X*Y females exhibit steeper reproductive senescence in the African pygmy mouse. (PNAS 2025)

- DOI: 10.1073/pnas.2412609121 | PMCID: PMC11725917 | PMID: 39739810
- Evidence: Analyses were performed with the package lme4 ( 60 ).
- Full pipeline: stage not stated [R v4.2.2, lme4]

### Cognition does not automatically influence perception: Evidence from neural encoding of colors belonging to different categories. (PNAS 2026)

- DOI: 10.1073/pnas.2538139123 | PMCID: PMC13273331 | PMID: 42263133
- Version used: **3.1**
- Evidence: Other statistical analyses were implemented in R 4.3.1 ( 59 ) using the following packages: lmerTest 3.1-3 ( 60 ), emmeans 1.10 ( 61 ), DHARMa 0.4.6 ( 62 ), simr 1.0.7 ( 63 ), and BayesFactor 0.9.12 ( 64 ).
- Full pipeline: differential/statistical testing [R v4.3, emmeans v1.10, lme4 v3.1] -> stage not stated [EEGLAB]

### Mating-dependent lifespan cost of sterol depletion in male &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2533735123 | PMCID: PMC13250600 | PMID: 42228537
- Evidence: Generalized linear models (GLMs) and generalized linear mixed models (GLMMs) were fitted using stats ( 38 ) and lme4 ( 39 ).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2, tidyverse] -> stage not stated [emmeans]

### Persistent trade-offs balance competition and colonization across centuries. (PNAS 2026)

- DOI: 10.1073/pnas.2534310123 | PMCID: PMC13250502 | PMID: 42228529
- Evidence: To assess differences in bacterial growth across strains, we used linear mixed-effects models with batch as a random effect and strain as a fixed effect, using the lmer() function in the lme4 R package.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [DESeq2, IQ-TREE v2.1.4, R, emmeans]

### Semantic knowledge guides innovation and drives cultural evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2530750123 | PMCID: PMC13229230 | PMID: 42190014
- Evidence: The difference between these features, along with their interactions with the two experimental conditions (semantic vs nonsemantic and individual vs group), was entered into a generalized linear mixed-effects model (GLMM) with a binomial error distribution (i.e., logistic regression) using the lme4 package ( 70 ).
- Full pipeline: differential/statistical testing [R, lme4]

### A defined community of core gut microbiota members promotes cognitive performance in honey bees. (PNAS 2026)

- DOI: 10.1073/pnas.2608600123 | PMCID: PMC13214017 | PMID: 42160337
- Evidence: Generalized linear mixed models with a binomial error structure—logit-link function—[“glmer” function from the lme4 package ( 51 )] were used to assess the predictive value of the trials, gnotobiotic group and odor on responses to the CS.
- Full pipeline: normalisation [vegan] -> differential/statistical testing [vegan] -> stage not stated [lme4]

### When a bigger brain is better: The case of bee olfactory learning. (PNAS 2026)

- DOI: 10.1073/pnas.2514030123 | PMCID: PMC13123798 | PMID: 41973935
- Evidence: Learning, memory, and memory specificity scores were analyzed with generalized linear mixed-effects models (GLMM) (package lme4) with a binomial distribution error, and the same fixed and random effects.
- Full pipeline: differential/statistical testing [lme4]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: Analyses were done using the “lmerTest” package in R, v.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Sender-receiver subdivisions of the default mode network in perceptual and memory-guided cognition. (PNAS 2026)

- DOI: 10.1073/pnas.2528851123 | PMCID: PMC13079981 | PMID: 41945445
- Evidence: LMMs were fitted by restricted maximum-likelihood estimation in R [4.1.1; ( 62 )] using the lme4 package [(1.1.32; ( 63 )].
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL v6.0, emmeans, lme4]

### Building courage, strength, and knowledge: Mindfulness training reduces psychological threat and increases engagement in college physics. (PNAS 2026)

- DOI: 10.1073/pnas.2521857123 | PMCID: PMC13079943 | PMID: 41941630
- Evidence: Analyses for both momentary and longitudinal threat were conducted using R 4.4.1 ( 41 ) with lme4 ( 42 ) and r2mlm ( 43 ) packages.
- Full pipeline: machine learning [lavaan] -> stage not stated [R v4.4, lme4]

### The detection of episodic memory in others biases social choice. (PNAS 2026)

- DOI: 10.1073/pnas.2530482123 | PMCID: PMC13080019 | PMID: 41941618
- Evidence: All variables were standardized, and all mixed effect models were run with the lme4 package in R (version 1.1-35.5; 71 ).
- Full pipeline: differential/statistical testing [R v1.1, lme4]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: Next, we accounted for block effects with the Best Linear Unbiased Estimates (BLUEs) using the lme4 package (version 1.1-35.5) ( 57 ) in R (version 4.4.2) ( 58 ).
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Decadal extreme drought reduces alpine subsoil carbon stocks. (PNAS 2026)

- DOI: 10.1073/pnas.2517468123 | PMCID: PMC12933107 | PMID: 41719334
- Evidence: We used linear mixed-effects models in the lme4 and lmerTest packages to account for the hierarchical structure of the experimental design.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [emmeans]

### Grazer exclusion is associated with higher fast-cycling carbon pools but lower slow-cycling mineral-associated carbon across grasslands. (PNAS 2026)

- DOI: 10.1073/pnas.2512048123 | PMCID: PMC12890883 | PMID: 41628319
- Evidence: The SEMs were performed using the “piecewiseSEM” ( 80 ) and “lme4” ( 81 ) packages, with all regression models fitted using the lme function.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R]

### Oxidizing pollutants can disrupt nestmate recognition in ants. (PNAS 2026)

- DOI: 10.1073/pnas.2520139123 | PMCID: PMC12890811 | PMID: 41628329
- Evidence: 1 C ) were analyzed using a linear mixed-effects model with the lme4 package in RStudio v.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [emmeans]

### Distinct contributions of hippocampal pathways in learning regularities and exceptions revealed by functional footprints. (PNAS 2026)

- DOI: 10.1073/pnas.2503388123 | PMCID: PMC12818569 | PMID: 41543896
- Version used: **1.1**
- Evidence: We fitted 3 separate linear mixed effects models ( lme4 version 1.1-30, lmerTest version 3.1-3) ( 73 , 74 ), estimated using REML and optimx optimizer, to predict the early and late MSP and TSP footprint activations with early and late learning accuracies for each stimulus type.
- Full pipeline: normalisation [ANTs] -> registration [FSL] -> differential/statistical testing [R, lme4 v1.1] -> stage not stated [FreeSurfer, MRtrix3, Nipype v1.5.1, fMRIPrep v20.2.1]

### Plant diversity influences plant volatile emission with varying effects at the species and community levels. (PNAS 2026)

- DOI: 10.1073/pnas.2518326123 | PMCID: PMC12818445 | PMID: 41538247
- Evidence: Mixed-effects regression models were implemented using the lme4 , lmerTest , and glmmTMB packages ( 91 – 93 ), with model variance components extracted using MuMIn ( 94 ).
- Full pipeline: differential/statistical testing [R v4.5.1, lme4, tidyverse] -> visualisation [ComplexHeatmap, R v4.5.1, ggplot2, pheatmap, tidyverse] -> stage not stated [mothur, phyloseq]

### Food absence is a cue for metamorphosis in the solitary bee &lt;i&gt;Megachile rotundata&lt;/i&gt; through a conserved physiological mechanism. (PNAS 2026)

- DOI: 10.1073/pnas.2511035122 | PMCID: PMC12773758 | PMID: 41461034
- Evidence: We used a linear mixed model with lme4 ( 76 ) to determine which variables significantly contributed to an individual’s cluster designation.
- Full pipeline: dimensionality reduction/clustering [R v4.2.0, lme4]

### Hidden state inference requires abstract contextual representations in the ventral hippocampus. (Science 2024)

- DOI: 10.1126/science.adq5874 | PMCID: PMC7618349 | PMID: 39571013
- Evidence: Statistical analysis All statistics were calculated using the Python packages scipy, pingouin and statsmodels , and lme4 R package implemented in Python through rpy2.
- Full pipeline: differential/statistical testing [R, lme4, pingouin, scikit-learn, statsmodels] -> stage not stated [Python, SciPy]

### Transcripts of repetitive DNA elements signal to block phagocytosis of hematopoietic stem cells. (Science 2024)

- DOI: 10.1126/science.adn1629 | PMCID: PMC12012832 | PMID: 39264994
- Evidence: Linear mixed effects analysis was performed using the lme4 package (v.1.2-1).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [CellProfiler, Metascape, R]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Version used: **1.1**
- Evidence: Statistical models of somatic mutation burden We used linear mixed-effects (LME) models from the lme4 (v.1.1–27.1) R package ( 50 ) to investigate potential associations between somatic mutation burden and other covariates of interest.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Implementing the above model using the lme4 package (v.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **1.1**
- Evidence: For statistical inference, we applied linear mixed models using the R packages lme4 (v1.1-36) ( 120 ), lmerTest (v3.1-3)( 121 ), and pbkrtest (v.0.5-0.1) ( 122 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

