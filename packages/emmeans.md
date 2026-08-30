# emmeans

- **Category:** general
- **Papers in survey:** 114
- **Journals:** PNAS (88), Nature (23), Science (2), Cell (1)
- **Years:** 2021 (7), 2022 (13), 2023 (21), 2024 (17), 2025 (42), 2026 (14)
- **Versions named:** 1.10.6 (2), 1.5.2 (1), 1.10 (1), 1.10.3 (1), 1.8.5 (1), 1.10.2 (1), 1.7.4 (1), 1.8.8 (1), 1.7.3 (1), 1.4.6 (1)
- **Pipeline stages it appears in:** differential/statistical testing (39), variant calling (3), normalisation (1), quantification (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: We estimated differences between tumor types within each tissue compartment using emmeans.
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Logged tropical forests have amplified and diverse ecosystem energetics. (Nature 2022)

- DOI: 10.1038/s41586-022-05523-1 | PMCID: PMC9771799 | PMID: 36517596
- Evidence: Pairwise post hoc comparison of the habitats, with Tukey adjustment, was carried out using the emmeans package 52 .
- Full pipeline: stage not stated [R, emmeans]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: We fitted the model using the multinom function of the nnet package and estimated the growth advantage using the package emmeans in R.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### Cancer risk across mammals. (Nature 2022)

- DOI: 10.1038/s41586-021-04224-5 | PMCID: PMC8755536 | PMID: 34937938
- Evidence: Pairwise order differences were assessed using the R package emmeans 46 .
- Full pipeline: stage not stated [R, emmeans, phytools]

### The illusion of moral decline. (Nature 2023)

- DOI: 10.1038/s41586-023-06137-x | PMCID: PMC10284688 | PMID: 37286595
- Evidence: Analysis To analyse the data, we fit a linear mixed effects model using the lme4 package in R 30 , extracted P values using the lmerTest package 31 and calculated planned contrasts using the emmeans package 32 , using a Holm–Bonferroni correction for multiple comparisons.
- Full pipeline: differential/statistical testing [emmeans, lme4]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Version used: **1.5.2**
- Evidence: For the proportion data shown in this paper, GLM with logit link function (R v4.0.2 and emmeans v1.5.2 ( https://cran.r-project.org/web/packages/emmeans/index.html )) and ordinary ANOVA with arcsine transformed value (arcsine transformation equation: Y = arcsin(√( Y / n )) × 180/π) were both applied to confirm the significance of the observations, and the full statistic results are shown in the Su...
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: We used the emmeans package in R to assess the significance of the regression contrasts and used p.adjust with the fdr method to adjust P values.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Genetic determinants of micronucleus formation in vivo. (Nature 2024)

- DOI: 10.1038/s41586-023-07009-0 | PMCID: PMC10917660 | PMID: 38355793
- Evidence: The genotype effect and associated error were estimated as a marginal mean using the emmeans package (R; v.1.4.4).
- Full pipeline: variant calling [emmeans] -> differential/statistical testing [R v3.18] -> stage not stated [ImageJ v1.53a, MAGMA]

### Pesticide use negatively affects bumble bees across European landscapes. (Nature 2024)

- DOI: 10.1038/s41586-023-06773-3 | PMCID: PMC11006599 | PMID: 38030722
- Evidence: We estimated marginal means with the emmeans package 67 .
- Full pipeline: stage not stated [emmeans, lme4]

### Amygdala-liver signalling orchestrates glycaemic responses to stress. (Nature 2025)

- DOI: 10.1038/s41586-025-09420-1 | PMCID: PMC12527908 | PMID: 40903586
- Evidence: Analyses in R were performed with R 3.6 using the lme4, lmerTest, emmeans, and car packages 61 , 62 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.4.2, emmeans, lme4]

### Engineered yeast provides rare but essential pollen sterols for honeybees. (Nature 2025)

- DOI: 10.1038/s41586-025-09431-y | PMCID: PMC12507675 | PMID: 40836088
- Evidence: Post hoc analysis was performed using the car 52 and emmeans 53 packages with Tukey adjustments for family-wise error rates.
- Full pipeline: stage not stated [ImageJ, emmeans]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: ...ge of transmitter-positive neurons that co-express FOS) or species (percentage of neurons that co-express a given transmitter, enrichment ratio) with emmeans {emmeans} and contrast {emmeans}.
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **1.10.6**
- Evidence: The package emmeans (v.1.10.6) was used to extract estimates of marginal means and contrasts from the model.
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: Pairwise post-hoc comparisons of the fixed effects were conducted using t -tests with Bonferroni adjustments, implemented through the R package ‘emmeans’ 65 .
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Global evolution of inflammatory bowel disease across epidemiologic stages. (Nature 2025)

- DOI: 10.1038/s41586-025-08940-0 | PMCID: PMC12158780 | PMID: 40307548
- Evidence: Negative binomial regression models followed by post hoc comparisons of estimated marginal means using the emmeans 68 package in R with Tukey adjustment for multiple comparisons were used to evaluate significant differences in CR between stage 1, stage 2 and stage 3 in each of the following: CD incidence, UC incidence, CD prevalence and UC prevalence.
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [ggplot2]

### Goal-specific hippocampal inhibition gates learning. (Nature 2025)

- DOI: 10.1038/s41586-025-08868-5 | PMCID: PMC12222015 | PMID: 40205046
- Evidence: The emmeans package (v.1.8.9; https://cran.r-project.org/web/packages/emmeans/index.html ) was used to adjust P values for multiple comparisons.
- Full pipeline: differential/statistical testing [R v4.2.2, emmeans, lme4]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: The coefficient estimates and the corresponding significance tests are computed for the fitted GLMM using the emtrends function from the emmeans R package.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### The global human impact on biodiversity. (Nature 2025)

- DOI: 10.1038/s41586-025-08752-2 | PMCID: PMC12058524 | PMID: 40140566
- Evidence: Mixed models were fitted using the glmmTMB package 59 and marginal means estimated using the emmeans package 60 .
- Full pipeline: stage not stated [emmeans]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: The multiple linear regression analyses were performed using the emmeans package in R (v.4.3.3).
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Dopaminergic mechanisms of dynamical social specialization. (Nature 2026)

- DOI: 10.1038/s41586-026-10301-4 | PMCID: PMC13233320 | PMID: 41922757
- Evidence: To compare predicted responses at zero distance (intercepts), marginal means were extracted with the emmeans package and pairwise contrasts performed with Tukey correction.
- Full pipeline: visualisation [ImageJ] -> stage not stated [emmeans]

### Rising atmospheric CO&lt;sub&gt;2&lt;/sub&gt; reduces nitrogen availability in boreal forests. (Nature 2026)

- DOI: 10.1038/s41586-025-10039-5 | PMCID: PMC12916481 | PMID: 41709006
- Evidence: We modelled δ 15 N as a function of the significant and non-significant scaled variables (emmeans function) and estimated the slopes of significant model variables (emtrends function) using the emmeans package 85 .
- Full pipeline: normalisation [emmeans] -> stage not stated [R, ggplot2]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Mixed models were fitted using the glmmTMB package 50 , and marginal means were estimated using the emmeans package 51 .
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Vicarious body maps bridge vision and touch in the human brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09796-0 | PMCID: PMC12872459 | PMID: 41299177
- Evidence: This was implemented using the emmeans R package 64 .
- Full pipeline: stage not stated [Connectome Workbench, Python, R, afex, emmeans]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Evidence: The emmeans R package (v.1.11.0) was used to calculate the AME and CIs between groups.
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Plant biodiversity and the regeneration of soil fertility. (PNAS 2021)

- DOI: 10.1073/pnas.2111321118 | PMCID: PMC8670497 | PMID: 34845020
- Evidence: Differences among means were compared using least-squares means (R package emmeans) followed by a Tukey correction using the Satterthwaite estimation of the degrees of freedom.
- Full pipeline: stage not stated [R v4.1.1, emmeans]

### Evolutionary change in the construction of the nursery environment when parents are prevented from caring for their young directly. (PNAS 2021)

- DOI: 10.1073/pnas.2102450118 | PMCID: PMC8640939 | PMID: 34819363
- Evidence: Post hoc comparisons were performed with the package “emmeans” version 1.6.3 in R ( 41 ).
- Full pipeline: differential/statistical testing [R v4.1.1, lme4] -> stage not stated [ImageJ v1.49v, emmeans]

### Soil chemistry determines whether defensive plant secondary metabolites promote or suppress herbivore growth. (PNAS 2021)

- DOI: 10.1073/pnas.2109602118 | PMCID: PMC8639379 | PMID: 34675080
- Evidence: All statistical analyses were conducted with R 3.4.4 (R Foundation for Statistical Computing) using the packages “car,” “emmeans,” and “RVAideMemoire” ( 77 – 80 ).
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [R]

### Human variation in gingival inflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2012578118 | PMCID: PMC8271746 | PMID: 34193520
- Evidence: Fixed-effects comparisons between test and control sides, and over-time changes within each group, were performed and post hoc false-discovery rate (FDR) ( 66 ) corrected pairwise comparisons were reported using the emmeans() function in the “ emmeans” package in R ( 67 ).
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [DADA2, QIIME 2 v2018.2, R, phyloseq]

### Identification of a micropeptide and multiple secondary cell genes that modulate &lt;i&gt;Drosophila&lt;/i&gt; male reproductive success. (PNAS 2021)

- DOI: 10.1073/pnas.2001897118 | PMCID: PMC8053986 | PMID: 33876742
- Evidence: We performed a statistical test in R using the packages lme4 and emmeans ( 73 – 75 ).
- Full pipeline: differential/statistical testing [emmeans, lme4]

### A narrow ear canal reduces sound velocity to create additional acoustic inputs in a microscale insect ear. (PNAS 2021)

- DOI: 10.1073/pnas.2017281118 | PMCID: PMC7958352 | PMID: 33658360
- Evidence: Post hoc testing was carried out using estimated marginal means from the emmeans package ( 46 ).
- Full pipeline: differential/statistical testing [R v4.0, lme4] -> stage not stated [emmeans]

### NETfacts: An integrated intervention at the individual and collective level to treat communities affected by organized violence. (PNAS 2022)

- DOI: 10.1073/pnas.2204698119 | PMCID: PMC9636916 | PMID: 36306329
- Version used: **1.4.6**
- Evidence: Significance tests were assessed by likelihood ratio tests ( 68 ), and post hoc tests were conducted with emmeans 1.4.6 ( 69 ).
- Full pipeline: differential/statistical testing [R v4.0] -> stage not stated [emmeans v1.4.6, lavaan v0.6, lme4 v1.1]

### Organellar transcripts dominate the cellular mRNA pool across plants of varying ploidy levels. (PNAS 2022)

- DOI: 10.1073/pnas.2204187119 | PMCID: PMC9335225 | PMID: 35858449
- Evidence: Post hoc comparisons between species pairs were conducted with the emmeans function, using a Holm procedure for the Bonferroni correction to account for multiple pairwise comparisons.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R v3.5, emmeans] -> visualisation [ggplot2] -> stage not stated [lme4]

### Motor learning without movement. (PNAS 2022)

- DOI: 10.1073/pnas.2204379119 | PMCID: PMC9335319 | PMID: 35858450
- Evidence: Statistical tests were conducted in R (version 4.0.3): packages rstatix ( 71 ), coin ( 72 ), MuMIn ( 73 ), lmerTest ( 74 ), lme4 ( 75 ), r2glmm ( 76 ), emmeans ( 77 ), effsize ( 78 ), effectsize ( 79 ), magrittr ( 80 ), ggplot2 ( 81 ), ggpubr ( 82 ), and ggeffects ( 83 ).
- Full pipeline: differential/statistical testing [R v4.0.3, emmeans, ggplot2, ggpubr, lme4] -> stage not stated [Python v3.8.5]

### Animal soundscapes reveal key markers of Amazon forest degradation from fire and logging. (PNAS 2022)

- DOI: 10.1073/pnas.2102878119 | PMCID: PMC9170030 | PMID: 35471905
- Evidence: Then, to evaluate effect size, standardized mean difference was calculated (Cohen’s D) using the R package “emmeans” for each frequency band to assess pairwise differences between levels for the two models, and the sum of all the pairwise effect sizes was assessed to estimate the frequency bin of maximum change in each case.
- Full pipeline: stage not stated [R, emmeans, igraph]

### Rhesus monkeys have an interoceptive sense of their beating hearts. (PNAS 2022)

- DOI: 10.1073/pnas.2119868119 | PMCID: PMC9169786 | PMID: 35412910
- Evidence: Post hoc comparisons to determine differences in looking times across trial types were carried out using the package emmeans ( 73 ).
- Full pipeline: differential/statistical testing [R v4.0.4] -> stage not stated [emmeans, lme4]

### Disruption of the circadian clock component BMAL1 elicits an endocrine adaption impacting on insulin sensitivity and liver disease. (PNAS 2022)

- DOI: 10.1073/pnas.2200083119 | PMCID: PMC8916004 | PMID: 35238641
- Evidence: Longitudinal data that have been acquired over several weeks were analyzed using a linear model, and pairwise comparisons were computed using the CRAN package emmeans for each time point.
- Full pipeline: differential/statistical testing [emmeans]

### Biome boundary maintained by intense belowground resource competition in world's thinnest-rooted plant community. (PNAS 2022)

- DOI: 10.1073/pnas.2117514119 | PMCID: PMC8892519 | PMID: 35165205
- Evidence: S1 B and C ) using linear regression (lm; R package stats) followed by pairwise contrast analysis (emmeans; R package emmeans).
- Full pipeline: differential/statistical testing [R, emmeans, lme4]

### Extra-pair paternity explains cooperation in a bird species. (PNAS 2022)

- DOI: 10.1073/pnas.2112004119 | PMCID: PMC8820227 | PMID: 35042830
- Evidence: R package emmeans ( 48 ) was used to perform post hoc tests to compare estimated marginal means of experiment groups.
- Full pipeline: differential/statistical testing [R v3.5, lme4] -> stage not stated [emmeans]

### Loss of glucose 6-phosphate dehydrogenase function increases oxidative stress and glutaminolysis in metastasizing melanoma cells. (PNAS 2022)

- DOI: 10.1073/pnas.2120617119 | PMCID: PMC8833200 | PMID: 35110412
- Evidence: All statistical analyses were performed using Graphpad Prism 9.2.0 or R 4.0.2 with the stats, fBasics, car, lme4, emmeans, and nparLD packages.
- Full pipeline: differential/statistical testing [R v4.0, emmeans, lme4]

### Unlocking adults' implicit statistical learning by cognitive depletion. (PNAS 2022)

- DOI: 10.1073/pnas.2026011119 | PMCID: PMC8764693 | PMID: 34983868
- Evidence: Cohen’s d effect sizes on the model’s estimates are calculated with the eff_size function from the emmeans package ( 64 ).
- Full pipeline: stage not stated [EEGLAB, Psychtoolbox, R, afex, emmeans, lme4]

### Radiation and temperature drive diurnal variation of aerobic methane emissions from Scots pine canopy. (PNAS 2023)

- DOI: 10.1073/pnas.2308516120 | PMCID: PMC10756279 | PMID: 38127980
- Evidence: Differences between time-of-day groups were tested using estimated marginal means ( emmeans package version 1.8.8).
- Full pipeline: differential/statistical testing [R v4.2.1, lme4 v1.1] -> stage not stated [HMMER, emmeans]

### Hippocampal contributions to novel spatial learning are both age-related and age-invariant. (PNAS 2023)

- DOI: 10.1073/pnas.2307884120 | PMCID: PMC10723126 | PMID: 38055735
- Evidence: Post hoc tests based on the three way interactions were done using the emmeans package.
- Full pipeline: normalisation [ANTs v2.3.5] -> simulation/modelling [brms] -> stage not stated [FSL, PsychoPy, R v4.2, emmeans, lme4]

### Causal evidence for a coordinated temporal interplay within the language network. (PNAS 2023)

- DOI: 10.1073/pnas.2306279120 | PMCID: PMC10666120 | PMID: 37963247
- Evidence: We used the package emmeans ( 156 ) for pairwise follow-up comparisons to further explore significant interactions.
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [EEGLAB, FieldTrip, emmeans]

### Bacterial tolerance to host-exuded specialized metabolites structures the maize root microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2310134120 | PMCID: PMC10622871 | PMID: 37878725
- Evidence: The following further R packages were used: Tidyverse ( 80 ), Broom ( 81 ), DECIPHER ( 82 ), DESeq2 ( 83 ), emmeans ( 84 ), ggthemes ( 85 ), multcomp ( 86 ), phyloseq ( 87 ), phytools ( 88 ), and vegan ( 89 ) in combination with some custom functions.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> stage not stated [DESeq2, R, RAxML v8.2.12, emmeans, phyloseq, phytools]

### Frugivore-mediated seed dispersal in fragmented landscapes: Compositional and functional turnover from forest to matrix. (PNAS 2023)

- DOI: 10.1073/pnas.2302440120 | PMCID: PMC10622928 | PMID: 37871198
- Version used: **1.7.3**
- Evidence: We used the R package emmeans v.1.7.3 to obtain estimated marginal means from the GLMMs for forest and matrix on the original scale.
- Full pipeline: stage not stated [QGIS v3.26.1, R, emmeans v1.7.3]

### Trehalose-6-phosphate signaling regulates lateral root formation in Arabidopsis thaliana. (PNAS 2023)

- DOI: 10.1073/pnas.2302996120 | PMCID: PMC10556606 | PMID: 37748053
- Evidence: Where applicable, post hoc Tukey and Dunnett’s tests were set up using the “emmeans” package ( 54 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [ImageJ, emmeans]

### Acetylcholine and noradrenaline enhance foraging optimality in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2305596120 | PMCID: PMC10483619 | PMID: 37639601
- Evidence: Post hoc contrasts were performed with functions hypothesis() and emmeans() from R-packages brms and emmeans , respectively ( 110 , 112 ).
- Full pipeline: differential/statistical testing [brms, emmeans] -> stage not stated [Psychtoolbox]

### How exceptional are the classic adaptive radiations of passerine birds? (PNAS 2023)

- DOI: 10.1073/pnas.1813976120 | PMCID: PMC10469319 | PMID: 37624752
- Evidence: We compared marginal means for size and shape disparity among the distributional categories using the function “emmeans” in the package “emmeans” ( 58 ).
- Full pipeline: stage not stated [R, emmeans]

### A persistent major mutation in canonical jasmonate signaling is embedded in an herbivory-elicited gene network. (PNAS 2023)

- DOI: 10.1073/pnas.2308500120 | PMCID: PMC10466192 | PMID: 37607232
- Evidence: The values are the differences in the slopes of regression lines calculated with the emmeans package in R and are listed in SI Appendix , Table S3 ; an asterisk denotes significant differences.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [emmeans]

### Evolutionary predictors of the specific colors of birds. (PNAS 2023)

- DOI: 10.1073/pnas.2217692120 | PMCID: PMC10450850 | PMID: 37579151
- Evidence: We then combined these into an overall effect by: 1) calculating the posterior distribution of each predicted slope in the original scale of the variable using the function “emtrends” from the R package emmeans ( 100 ) and 2) using these posterior distributions to compute a mean effect and its uncertainty (95% credible intervals).
- Full pipeline: differential/statistical testing [brms] -> stage not stated [R, emmeans]

### Climate change-induced stress disrupts ectomycorrhizal interaction networks at the boreal-temperate ecotone. (PNAS 2023)

- DOI: 10.1073/pnas.2221619120 | PMCID: PMC10450648 | PMID: 37579148
- Evidence: When main effects were significant, post hoc Dunnett’s tests were used to compare the relative abundance of each specific functional grouping in each treatment compared to the control (ambient temperature and precipitation) with the ‘emmeans’ package (version 1.6.0).
- Full pipeline: quantification [emmeans] -> differential/statistical testing [R v4.1.0] -> visualisation [igraph]

### Adaptive structural and functional evolution of the placenta protects fetal growth in high-elevation deer mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218049120 | PMCID: PMC10288601 | PMID: 37307471
- Evidence: We assessed the significance of fixed effects and interactions within models using type III sum of squares in the car package ( 92 ), and we performed post hoc tests within emmeans and lmerTest packages ( 93 , 94 ) using a Benjamini–Hochberg correction for multiple comparisons.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [ImageJ v2.0.0, featureCounts] -> stage not stated [R v4.0, WGCNA, emmeans, lme4]

### Unraveling female communication through scent marks in the Norway rat. (PNAS 2023)

- DOI: 10.1073/pnas.2300794120 | PMCID: PMC10288631 | PMID: 37307448
- Evidence: Analyses were carried out using R version 4.2.0 ( 78 ) with the lme4 ( 79 ) and emmeans ( 80 ) packages for mixed-effects models and IBM SPSS version 27 (IBM Ltd.) for repeated-measures ANOVAs.
- Full pipeline: differential/statistical testing [R v4.2.0, emmeans, lme4]

### Decomposition decreases molecular diversity and ecosystem similarity of soil organic matter. (PNAS 2023)

- DOI: 10.1073/pnas.2303335120 | PMCID: PMC10288640 | PMID: 37307452
- Evidence: Variable means were contrasted using estimated marginal means with a Bonferroni correction factor using the emmeans R package ( 73 ) and compact letter displays.
- Full pipeline: differential/statistical testing [R, emmeans] -> stage not stated [vegan]

### Experimentally simulating the evolution-to-ecology connection: Divergent predator morphologies alter natural food webs. (PNAS 2023)

- DOI: 10.1073/pnas.2221691120 | PMCID: PMC10268251 | PMID: 37276393
- Evidence: Post-hoc t tests used a similar approach and were performed using the “lmerTest” ( 53 ) and “emmeans” packages ( 54 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [emmeans, lme4]

### Evolution of acoustic signals associated with cooperative parental behavior in a poison frog. (PNAS 2023)

- DOI: 10.1073/pnas.2218956120 | PMCID: PMC10151463 | PMID: 37071680
- Evidence: Model testing was carried out using the packages “lmerTest” ( 46 ) and “emmeans” ( 47 ), with reproductive stage specified as a covariate and individual ID specified as a random effect in all models.
- Full pipeline: stage not stated [R, emmeans, lme4]

### Increased dominance of heat-tolerant symbionts creates resilient coral reefs in near-term ocean warming. (PNAS 2023)

- DOI: 10.1073/pnas.2202388120 | PMCID: PMC9974440 | PMID: 36780524
- Evidence: Tukey’s comparisons among species and years were performed using emmeans and multcomp v1.4 ( SI Appendix , Tables S6 and S7 ).
- Full pipeline: quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [R v3.6, emmeans]

### Adaptive control is reversed between hands after left hemisphere stroke and lost following right hemisphere stroke. (PNAS 2023)

- DOI: 10.1073/pnas.2212726120 | PMCID: PMC9963612 | PMID: 36716370
- Evidence: Estimated marginal means were compared between groups using the emmeans package (v.
- Full pipeline: stage not stated [R v4.0.2, emmeans]

### Diverse mating consequences of the evolutionary breakdown of the sexual polymorphism heterostyly. (PNAS 2023)

- DOI: 10.1073/pnas.2214492120 | PMCID: PMC9926269 | PMID: 36595698
- Evidence: Comparisons among marginal factor means involved Tukey’s test for main effects and the Dunn–Šidák procedure for nested effects and interactions ( 81 ) and were conducted using the R emmeans package version 1.6.3.
- Full pipeline: stage not stated [R v4.1.1, emmeans]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: Then, statistical analysis was performed for the fitted model using the function ANOVA in the R package “car” ( 78 ), followed by multiple pairwise comparisons using the R package “emmeans” ( 79 ), which uses the Tukey method for P value adjustment.
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Intensive leaf cooling promotes tree survival during a record heatwave. (PNAS 2024)

- DOI: 10.1073/pnas.2408583121 | PMCID: PMC11513916 | PMID: 39401366
- Evidence: Linear mixed effects models were employed to analyze changes in the dependent variables g sw , T crit , F v /F m , thermal safety margin, and leaf water potential, using the packages “lmerTest” ( 67 ) and “emmeans” ( 68 ).
- Full pipeline: differential/statistical testing [emmeans, lme4] -> stage not stated [R]

### Presaccadic preview shapes postsaccadic processing more where perception is poor. (PNAS 2024)

- DOI: 10.1073/pnas.2411293121 | PMCID: PMC11406264 | PMID: 39236235
- Version used: **1.7.4**
- Evidence: Post hoc tests for any significant effects were run with the package emmeans (version 1.7.4-1 in R).
- Full pipeline: stage not stated [emmeans v1.7.4]

### Parallel ecological and evolutionary responses to selection in a natural bacterial community. (PNAS 2024)

- DOI: 10.1073/pnas.2403577121 | PMCID: PMC11388356 | PMID: 39190353
- Evidence: In general, models were compared by sequentially deleting terms and comparing model fits using F-tests or χ 2 -tests (where appropriate), after which pairwise contrasts were computed using the “emmeans” packages ( 87 ), with α < 0.05.
- Full pipeline: quantification [DESeq2, R] -> stage not stated [emmeans, ggplot2, lme4, vegan]

### Maternal manipulation of offspring size can trigger the evolution of eusociality in promiscuous species. (PNAS 2024)

- DOI: 10.1073/pnas.2402179121 | PMCID: PMC11331107 | PMID: 39110731
- Version used: **1.8.8**
- Evidence: 3 , we derived probabilities of direction (pd), which represents the posterior probability that an effect occurs in a particular direction, from Bayesian models implemented with the brms v2.20.4 ( 82 – 84 ) package in combination with the MCMC sampler of cmdstanr ( 85 ) and posterior means with the emmeans v1.8.8 ( 86 ) package (details in SI Appendix ).
- Full pipeline: differential/statistical testing [brms v2.20.4, emmeans v1.8.8] -> stage not stated [R v4.2, tidyverse v2.0.0]

### Flexible oviposition behavior enabled the evolution of terrestrial reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2312371121 | PMCID: PMC11295038 | PMID: 39042675
- Evidence: Post hoc comparisons of species or populations were conducted with the emmeans package ( 52 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2] -> stage not stated [ImageJ, RAxML v1.0.3, emmeans, lme4, phytools]

### The integral role of de novo lipogenesis in the preparation for seasonal dormancy. (PNAS 2024)

- DOI: 10.1073/pnas.2406194121 | PMCID: PMC11260141 | PMID: 38990942
- Evidence: The estimated marginal means were calculated using the R package “emmeans” (v1.8).
- Full pipeline: quantification [R] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [BLAST, emmeans]

### Hemispheric functional organization, as revealed by naturalistic neuroimaging, in pediatric epilepsy patients with cortical resections. (PNAS 2024)

- DOI: 10.1073/pnas.2317458121 | PMCID: PMC11252739 | PMID: 38950362
- Evidence: We then conducted planned comparisons on the EMMs from the model, extracted with the R function emmeans ( 63 ), to further probe the two-way interactions of the within- and between-edge types across group by calculating the difference between each patient group and the matched hemisphere of the controls for each edge type separately.
- Full pipeline: differential/statistical testing [R, lme4] -> structure determination [FreeSurfer] -> stage not stated [AFNI v21.1.10, emmeans]

### Puppy whines mediate maternal behavior in domestic dogs. (PNAS 2024)

- DOI: 10.1073/pnas.2316818121 | PMCID: PMC11145252 | PMID: 38768360
- Evidence: When the effect of an interaction was statistically significant, we conducted post hoc tests to assess the relationship between f o manipulations and behavioral responses when variants were derived from own and stranger puppies [emtrends( ) function from emmeans R package ( 64 )].
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [R, lme4]

### Evolutionarily conserved neural responses to affective touch in monkeys transcend consciousness and change with age. (PNAS 2024)

- DOI: 10.1073/pnas.2322157121 | PMCID: PMC11067024 | PMID: 38648473
- Evidence: Post hoc tests to assess interactions were conducted on the EMMs using the emmeans package ( 114 ).
- Full pipeline: stage not stated [AFNI, CIVET, Python, R v4.3.1, emmeans, lme4]

### Costs of being a diet generalist for the protist predator <i>Dictyostelium discoideum</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313203121 | PMCID: PMC10998602 | PMID: 38530891
- Evidence: We used the “ emmeans ” package to calculate estimated effect sizes (Cohen’s d, a standardized measure) and 95% CIs for relevant contrasts ( 81 ).
- Full pipeline: differential/statistical testing [R v4.2.1] -> stage not stated [emmeans]

### The circadian molecular clock in the suprachiasmatic nucleus is necessary but not sufficient for fear entrainment. (PNAS 2024)

- DOI: 10.1073/pnas.2316841121 | PMCID: PMC10990155 | PMID: 38502706
- Evidence: Post hoc Tukey comparisons within groups were performed using the emmeans package ( 30 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [ImageJ, emmeans]

### Diverging neural dynamics for syntactic structure building in naturalistic speaking and listening. (PNAS 2024)

- DOI: 10.1073/pnas.2310766121 | PMCID: PMC10945772 | PMID: 38442171
- Evidence: We computed the contribution of factors to the models using car [version 3.0-10 ( 91 )], and pairwise comparisons with the package emmeans [version 1.6.1 ( 92 )].
- Full pipeline: differential/statistical testing [R v4.0.3, lme4] -> stage not stated [FreeSurfer, Nilearn, Python, TensorFlow, emmeans]

### Evolved birth physiology meets modern birth practice: Sustained effects of planned cesarean delivery on child hair cortisol in Brazil. (PNAS 2025)

- DOI: 10.1073/pnas.2519365122 | PMCID: PMC12718353 | PMID: 41359854
- Evidence: Pairwise contrasts of log hair cortisol by birth mode were calculated via the emmeans package (version 1.11.1) ( 45 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.5.0, emmeans]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Evidence: Effect sizes, their CI and P values of contrasts between groups were determined with the emmeans package (v1.11.1).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### An AINTEGUMENTA phosphoswitch controls bilateral stem cell activity during secondary growth. (PNAS 2025)

- DOI: 10.1073/pnas.2510538122 | PMCID: PMC12663975 | PMID: 41264254
- Evidence: Inference from the models was done with the emmeans package (version 1.5.5-1) and P -values for the pairwise contrasts were adjusted using the Holm–Bonferroni method.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> quantification [R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3, emmeans] -> stage not stated [Galaxy, ggplot2 v3.4.3]

### General laws of biodiversity: Climatic niches predict plant range size and ecological dominance globally. (PNAS 2025)

- DOI: 10.1073/pnas.2517585122 | PMCID: PMC12646267 | PMID: 41218123
- Evidence: We compared the slopes of each model across the grouping variable using a Tukey test, available in the function emtrends of the R package emmeans ( 83 ).
- Full pipeline: stage not stated [R, emmeans, lme4]

### Elevated virus infection of honey bee queens reduces methyl oleate production and destabilizes colony-level social structure. (PNAS 2025)

- DOI: 10.1073/pnas.2518975122 | PMCID: PMC12557728 | PMID: 41086214
- Evidence: In all cases, we used tools within the DHARMa ( 79 ) package to confirm appropriateness of residual distributions, and post hoc testing was conducted using emmeans ( 80 ) with the Tukey P value adjustment method applied.
- Full pipeline: quantification [limma] -> differential/statistical testing [emmeans] -> stage not stated [R v4.3.0]

### Transpupillary in vivo two-photon imaging reveals enhanced surveillance of retinal microglia in diabetic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426241122 | PMCID: PMC12541322 | PMID: 41060759
- Evidence: All statistical analyses were performed using Excel software (Microsoft, Redmond, WA), MATLAB using built-in functions, and R (version 4.4.2; using the “tidyverse”, “multcomp”, “rstatix”, “nlme”, “emmeans”, and “PMCMRplus” packages).
- Full pipeline: differential/statistical testing [R v4.4.2, emmeans, tidyverse] -> stage not stated [ImageJ v1.54f]

### Experimentally enhancing dispersal reveals the outsized importance of transient dynamics in a fluctuating environment. (PNAS 2025)

- DOI: 10.1073/pnas.2422454122 | PMCID: PMC12452863 | PMID: 40928877
- Evidence: Fourth, post hoc Tukey pairwise comparisons were conducted using the “emmeans” package only when predictors in our ANOVAs were statistically significant ( 42 ) and were always made to the control plot unless otherwise indicated.
- Full pipeline: differential/statistical testing [R v4.3.2, emmeans]

### Female membrane proteins regulate postmating ovulation in &lt;i&gt;Drosophila melanogaster&lt;/i&gt; by ovulin-dependent and -independent pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2508783122 | PMCID: PMC12452909 | PMID: 40920921
- Evidence: The package emmeans was then used to select relevant pairwise comparisons, and P -values were adjusted for multiple comparisons using the Holm–Bonferroni correction.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> variant calling [lme4] -> differential/statistical testing [emmeans, lme4] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.5.5]

### Asymmetric development and function of paired sperm-storage organs in &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2512096122 | PMCID: PMC12403100 | PMID: 40828028
- Version used: **1.10.6**
- Evidence: Statistical analysis was performed in R v4.4.1 with the following packages: tidyverse v2.0.0, lme4 v1.1–35.5, and emmeans v1.10.6.
- Full pipeline: differential/statistical testing [R v4.4, emmeans v1.10.6, lme4 v1.1, tidyverse v2.0.0]

### Evolution of developmental bias explains divergent patterns of phenotypic evolution in two nematode clades. (PNAS 2025)

- DOI: 10.1073/pnas.2507529122 | PMCID: PMC12403097 | PMID: 40828025
- Version used: **1.10.3**
- Evidence: To estimate mutational effects on the directional changes in the trait means of RMLs in respect to their ancestors, we estimated marginal means of the fixed effect Treatment (control Vs mutation) using the R package emmeans (v.
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MAFFT v7.49] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.2.2, emmeans v1.10.3, ggplot2 v3.5.1]

### Indigenous territories and protected areas are crucial for ecosystem connectivity in the Amazon basin. (PNAS 2025)

- DOI: 10.1073/pnas.2418189122 | PMCID: PMC12337320 | PMID: 40720645
- Evidence: Post hoc comparisons among levels of the predictor variables were performed using the “contrast” and “regrid” functions of the “emmeans” v.1. package ( 108 ) and were represented with letters on the plot to indicate significant differences among the levels of ITPA categories.
- Full pipeline: visualisation [ggplot2 v3.5.1, tidyverse v1.3.1] -> stage not stated [QGIS, emmeans, lme4]

### Larval diapause slows adult epigenetic aging in an insect model, &lt;i&gt;Nasonia vitripennis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2513020122 | PMCID: PMC12337301 | PMID: 40720640
- Evidence: Curiously, at day 6 posteclosion, adults that have passed through diapause as larvae were epigenetically older than age-matched controls by an estimated 2.8 d (diapaused: 11.32 d vs. control: 8.53 d, t = −3.22, d.f. = 36, P = 0.0027, emmeans post hoc).
- Full pipeline: stage not stated [emmeans]

### Static allometries of caste-associated traits vary with genotype but not environment in the clonal raider ant. (PNAS 2025)

- DOI: 10.1073/pnas.2501716122 | PMCID: PMC12318203 | PMID: 40694330
- Evidence: Post hoc Tukey’s tests comparing genotypes in their average body sizes and static allometries were performed using the package emmeans .
- Full pipeline: variant calling [emmeans] -> stage not stated [ImageJ]

### Human land use promotes range expansion of soil protists from temperate to subtropical regions in China. (PNAS 2025)

- DOI: 10.1073/pnas.2413220122 | PMCID: PMC12318147 | PMID: 40694336
- Evidence: To facilitate comparison of the magnitude of biological homogenization between spatial scales and land-use types, effect sizes of human land-use systems on community distance were estimated based on linear mixed effects models and given as Cohen’s D (“eff_size” in the “emmeans” package) ( 61 ).
- Full pipeline: differential/statistical testing [R v3.6.2, emmeans, lme4] -> stage not stated [QIIME 2 v1.90, vegan]

### HIF1α mediates circadian regulation of skeletal muscle metabolism and substrate preference in response to time-of-day exercise. (PNAS 2025)

- DOI: 10.1073/pnas.2504080122 | PMCID: PMC12280960 | PMID: 40627397
- Evidence: Where significant, post hoc testing was conducted using “emmeans” ( 43 ).
- Full pipeline: alignment/mapping [STAR, featureCounts] -> quantification [Python] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [emmeans]

### Divergent oxygen trends in ice-covered lakes driven by ice-cover decline and ecological memory. (PNAS 2025)

- DOI: 10.1073/pnas.2426140122 | PMCID: PMC12260399 | PMID: 40601624
- Evidence: We compared trends within each class category using ANOVA (lmerTest), followed by a post hoc Tukey’s HSD test using the “emmeans” R package ( 80 ).
- Full pipeline: stage not stated [R v4.2, emmeans, lme4]

### Contribution of glutamatergic projections to neurons in the nonhuman primate substantia nigra pars reticulata for reactive inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2427032122 | PMCID: PMC12232709 | PMID: 40569385
- Evidence: For LMM and GLMM analyses, we used the lme4 ( 66 ), pbkrtest ( 67 ), emmeans ( 68 ), and brms ( 69 ) packages in RStudio.
- Full pipeline: stage not stated [brms, emmeans, lme4]

### Winters restrict a climate change-driven butterfly range expansion despite rapid evolution of seasonal timing traits. (PNAS 2025)

- DOI: 10.1073/pnas.2418392122 | PMCID: PMC12232556 | PMID: 40549916
- Version used: **1.8.5**
- Evidence: For statistical tests, we used the package car 3.1.1 ( 74 ), except for likelihood ratio tests—which we did with anova in base R and the package afex 1.2.1 ( 75 )—and post hoc tests, which we did with emmeans 1.8.5 ( 76 ).
- Full pipeline: differential/statistical testing [afex v1.2.1, emmeans v1.8.5] -> stage not stated [R, lme4 v1.1.32]

### Model-based algorithms shape automatic evaluative processing. (PNAS 2025)

- DOI: 10.1073/pnas.2417068122 | PMCID: PMC12207468 | PMID: 40540594
- Evidence: Analyses were conducted using standard linear models, with planned comparisons implemented using the emmeans package ( 77 ) and accompanying Bayes Factors calculated using the BayesFactor package ( 78 ).
- Full pipeline: differential/statistical testing [R, emmeans]

### Longitudinal sequencing reveals polygenic and epistatic nature of genomic response to selection. (PNAS 2025)

- DOI: 10.1073/pnas.2410452122 | PMCID: PMC12207516 | PMID: 40531879
- Evidence: This was done using the emtrends function in the R package emmeans ( 55 ).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA, Picard] -> variant calling [DESeq2] -> dimensionality reduction/clustering [PLINK] -> stage not stated [R, emmeans]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Evidence: We tested whether ancestry cohort significantly explained variation in the summary statistics using one-way ANOVA, followed by Tukey’s tests, performed using the multcomp ( 65 ) and emmeans ( 66 ) packages, to determine which levels of the variables explained the variation.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: When there was a significant main effect, we performed pairwise comparisons (emmeans::emmeans in R) ( 44 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### Hygrometrically controlled programmed cell death drives anther opening and pollen release. (PNAS 2025)

- DOI: 10.1073/pnas.2420132122 | PMCID: PMC12107150 | PMID: 40377996
- Evidence: Differences between individual variants were estimated by emmeans function from package emmeans.
- Full pipeline: quantification [kallisto v0.48.0] -> differential/statistical testing [R] -> stage not stated [emmeans]

### Linked nitrogen and carbon dynamics reveal distinct pools and patterns in a deep, weathered bedrock rhizosphere. (PNAS 2025)

- DOI: 10.1073/pnas.2400452122 | PMCID: PMC12087964 | PMID: 40343996
- Evidence: Pairwise comparisons were conducted using the emmeans ( 69 ) package in R for post hoc Tukey comparison of seasonal differences in TDN within water year and the r.squaredGLMM command from MuMIn package was used to calculate marginal and conditional R 2 for all models ( 70 ).
- Full pipeline: stage not stated [R v4.2.2, emmeans, lme4]

### Improved synapsis dynamics accompany meiotic stability in &lt;i&gt;Arabidopsis arenosa&lt;/i&gt; autotetraploids. (PNAS 2025)

- DOI: 10.1073/pnas.2420115122 | PMCID: PMC12088413 | PMID: 40333759
- Evidence: For the best fit GLMM, we estimated means, CI, medians, SE, and P -values using the emmeans R package ( 78 ) with Holm–Bonferroni correction, based on Wald’s tests performed by glmmTMB.
- Full pipeline: differential/statistical testing [emmeans, ggplot2] -> stage not stated [ImageJ, R]

### Evolutionary feedbacks for &lt;i&gt;Drosophila&lt;/i&gt; aggression revealed through experimental evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2419068122 | PMCID: PMC12054797 | PMID: 40273109
- Evidence: These computations were implemented in the emmeans package ( 67 ).
- Full pipeline: stage not stated [emmeans]

### Pathogen growth and virulence dynamics drive the host evolution against coinfections. (PNAS 2025)

- DOI: 10.1073/pnas.2412124122 | PMCID: PMC12054814 | PMID: 40267133
- Evidence: Moreover, to understand the contrast between diverging evolutionary trends across generations from different selection regimes, we used a generalized linear model fitted to Gaussian distribution followed by performing pairwise comparisons using “emmeans”.
- Full pipeline: differential/statistical testing [DESeq2, emmeans]

### microRNA-218-5p coordinates scaling of excitatory and inhibitory synapses during homeostatic synaptic plasticity. (PNAS 2025)

- DOI: 10.1073/pnas.2500880122 | PMCID: PMC12002172 | PMID: 40172961
- Evidence: Post hoc analysis was used using the emmeans R-package using Dunn’s test against a reference control.
- Full pipeline: alignment/mapping [edgeR] -> normalisation [edgeR, lme4] -> differential/statistical testing [R v4.0, edgeR] -> stage not stated [emmeans]

### Tetrapod species-area relationships across the Cretaceous-Paleogene mass extinction. (PNAS 2025)

- DOI: 10.1073/pnas.2419052122 | PMCID: PMC12002258 | PMID: 40131953
- Evidence: We tested for differences in slopes of successive bins using an interaction with covariates analysis implemented via the function “emtrends()” in the R package “emmeans.” 3.6.
- Full pipeline: stage not stated [R, emmeans]

### eDNA confirms lower trophic interactions help to modulate population outbreaks of the notorious crown-of-thorns sea star. (PNAS 2025)

- DOI: 10.1073/pnas.2424560122 | PMCID: PMC11929471 | PMID: 40063810
- Evidence: Significant results were explored by the Tukey method using emmeans ( 75 ).
- Full pipeline: differential/statistical testing [JAGS, R v4.1, Stan] -> simulation/modelling [JAGS, Stan] -> stage not stated [emmeans]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Version used: **1.10.2**
- Evidence: The emtrends function [emmeans v1.10.2 package ( 110 )] was used to test directionality and obtain CI within interacting predictors.
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Cognition does not automatically influence perception: Evidence from neural encoding of colors belonging to different categories. (PNAS 2026)

- DOI: 10.1073/pnas.2538139123 | PMCID: PMC13273331 | PMID: 42263133
- Version used: **1.10**
- Evidence: Other statistical analyses were implemented in R 4.3.1 ( 59 ) using the following packages: lmerTest 3.1-3 ( 60 ), emmeans 1.10 ( 61 ), DHARMa 0.4.6 ( 62 ), simr 1.0.7 ( 63 ), and BayesFactor 0.9.12 ( 64 ).
- Full pipeline: differential/statistical testing [R v4.3, emmeans v1.10, lme4 v3.1] -> stage not stated [EEGLAB]

### Mating-dependent lifespan cost of sterol depletion in male &lt;i&gt;Drosophila melanogaster&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2533735123 | PMCID: PMC13250600 | PMID: 42228537
- Evidence: Estimates were then bias-adjusted using the package emmeans ( 43 ).
- Full pipeline: differential/statistical testing [lme4] -> visualisation [ggplot2, tidyverse] -> stage not stated [emmeans]

### Persistent trade-offs balance competition and colonization across centuries. (PNAS 2026)

- DOI: 10.1073/pnas.2534310123 | PMCID: PMC13250502 | PMID: 42228529
- Evidence: Pairwise comparisons between WT and mutant strains were performed using the emmeans() function from the emmeans package.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [DESeq2, IQ-TREE v2.1.4, R, emmeans]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: The analysis was implemented in R, using the dplyr and emmeans packages to compute genotype means, mean differences, SE, CI, and P -values, ensuring statistical inference.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Evidence: We used the emmeans package (v.
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

### Sender-receiver subdivisions of the default mode network in perceptual and memory-guided cognition. (PNAS 2026)

- DOI: 10.1073/pnas.2528851123 | PMCID: PMC13079981 | PMID: 41945445
- Evidence: 6 ) were obtained with the emmeans package [1.8.5; ( 66 )].
- Full pipeline: alignment/mapping [SPM] -> differential/statistical testing [SPM] -> stage not stated [FSL v6.0, emmeans, lme4]

### DNA methylation in invertebrate genomes and cell lineage plasticity. (PNAS 2026)

- DOI: 10.1073/pnas.2510416123 | PMCID: PMC13012060 | PMID: 41790947
- Evidence: Estimated marginal means and pairwise contrasts were computed with emmeans ( 96 ) ( SI Appendix , Table S4 ).
- Full pipeline: quality control [Bismark v0.24.0, Trim Galore v0.6.10] -> read trimming [Bismark v0.24.0, Trim Galore v0.6.10] -> alignment/mapping [Bismark v0.24.0, Trim Galore v0.6.10] -> stage not stated [R v4.5, emmeans, phytools]

### Decadal extreme drought reduces alpine subsoil carbon stocks. (PNAS 2026)

- DOI: 10.1073/pnas.2517468123 | PMCID: PMC12933107 | PMID: 41719334
- Evidence: For significant treatment effects ( P < 0.05), we performed post hoc pairwise comparisons using estimated marginal means with Tukey’s HSD adjustment for multiple comparisons (emmeans package in R).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [emmeans]

### Oxidizing pollutants can disrupt nestmate recognition in ants. (PNAS 2026)

- DOI: 10.1073/pnas.2520139123 | PMCID: PMC12890811 | PMID: 41628329
- Evidence: The global effect of Treatment was tested with likelihood-ratio tests (function drop1 ), followed by post hoc pairwise comparisons between all levels of Treatment using the emmeans package, with Holm adjustment for multiple comparisons.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [emmeans]

### SPL13 controls a root apical meristem phase change by triggering oriented cell divisions. (Science 2024)

- DOI: 10.1126/science.ado4298 | PMCID: PMC7616863 | PMID: 39541454
- Evidence: Inference from the models was done with the emmeans package (version 1.5.5-1) and p-values for the pairwise contrasts were adjusted using the Holm-Bonferroni method.
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [R v3.5.1, edgeR, ggplot2 v3.4.3]

### Hedonic eating is controlled by dopamine neurons that oppose GLP-1R satiety. (Science 2025)

- DOI: 10.1126/science.adt0773 | PMCID: PMC12009138 | PMID: 40146831
- Evidence: Post-hoc pairwise comparisons between treatment conditions were conducted within each time bin using estimated marginal means (EMMs) derived from the full model via the emmeans package in R ( https://cran.r-project.org/web/packages/emmeans/index.html ).
- Full pipeline: stage not stated [R, SLEAP, emmeans]

