# XGBoost

- **Category:** general
- **Papers in survey:** 65
- **Journals:** PNAS (43), Nature (18), Cell (4)
- **Years:** 2021 (4), 2022 (10), 2023 (10), 2024 (10), 2025 (19), 2026 (12)
- **Versions named:** 2.0.3 (1), 1.7.3 (1), 1.5.0.1 (1)
- **Pipeline stages it appears in:** machine learning (24), differential/statistical testing (18), dimensionality reduction/clustering (2), simulation/modelling (1), structure determination (1)

## Papers

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: All 11 biomarkers were inputted into the gradient boosted tree algorithm XGBoost (R package ‘xgboost’), a widely used machine learning algorithm effective for classification tasks.
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **1.5.0.1**
- Evidence: ...au et al., 2015 https://cran.r-project.org/web/packages/PRROC/index.html gbm 2.1.8 Ridgeway, 2007 https://cran.r-project.org/web/packages/gbm/gbm.pdf xgboost 1.5.0.1 Chen et al., 2015 https://xgboost.readthedocs.io/en/stable/R-package/xgboostPresentation.html randomForest 4.6-14 Liaw and Wiener, 2002 https://cran.r-project.org/web/packages/randomForest/randomForest.pdf ANCOM-BC 1.4.0 Lin and Pedda...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Evidence: Before fitting logistic regression models, selection for clinical variables was done using extreme gradient boosting (XGBoost)1 using R version 3.6.3 and libraries xgboost ( Chen and Guestrin, 2016 ) (version 1.3.2.1) and caret ( Kuhn, 2008 ) (version 6.0-86).
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### Perturb-Multimodal: A platform for pooled genetic screens with imaging and sequencing in intact mammalian tissue. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.022 | PMCID: PMC12324982 | PMID: 40513557
- Evidence: Data Processing Pipeline RCA-MERFISH gene expression was processed using a modified version of the MERlin pipeline, as previously described 110 , 113 , with the addition of a machine learning filtering step that used XGBoost to train a classifier to discriminate incorrectly decoded molecules that were assigned to blank barcodes and putatively correctly decoded molecules that were assigned to codin...
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose, XGBoost] -> stage not stated [AnnData, Scanpy]

### Regulatory genomic circuitry of human disease loci by integrative epigenomics. (Nature 2021)

- DOI: 10.1038/s41586-020-03145-z | PMCID: PMC7875769 | PMID: 33536621
- Evidence: Predictions were made by training an XGBoost classifier on the positive set of all valid links against their paired negative links, using precomputed correlations and distance to the transcription start site as features, and keeping all links with a probability above 5/7 (ref.
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [MACS2] -> machine learning [XGBoost] -> visualisation [R]

### An autonomous laboratory for the accelerated synthesis of novel materials. (Nature 2023)

- DOI: 10.1038/s41586-023-06734-w | PMCID: PMC10700133 | PMID: 38030721
- Evidence: For each set of recommended precursors, the most effective synthesis temperature is predicted using an XGBoost regressor trained in previous work 23 .
- Full pipeline: machine learning [XGBoost]

### Global methane emissions from rivers and streams. (Nature 2023)

- DOI: 10.1038/s41586-023-06344-6 | PMCID: PMC10511311 | PMID: 37587344
- Evidence: Random forest modelling We used random forest models to predict CH 4 concentrations and to understand the main drivers (but other machine-learning models such as XGBoost and a neural network were also explored; see Supplementary Information ).
- Full pipeline: machine learning [XGBoost] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4.0, tidyverse v1.0.7] -> stage not stated [R v0.3.2]

### Health system-scale language models are all-purpose prediction engines. (Nature 2023)

- DOI: 10.1038/s41586-023-06160-y | PMCID: PMC10338337 | PMID: 37286606
- Evidence: Structured baselines The structured baselines were (1) SAPS2/APACHE2 features + XGBoost for in-hospital mortality prediction, (2) LACE features + XGBoost for readmission prediction, (3) Lisbon Portugal features + XGBoost for binned LOS prediction and (4) claim form features + XGBoost for insurance denial prediction.
- Full pipeline: stage not stated [Matplotlib v3.5.2, Python v3.8.13, XGBoost, scikit-learn, seaborn v0.12.2]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: We implemented support for all generalized linear models provided by the stats R package, regularized linear models provided by the glmnet R package 69 , Bayesian regression models implemented through the brms R package 70 , gradient boosting regression through the xgboost R package 70 , 71 , as well as bagging and Bayesian ridge models through scikit-learn 72 .
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Digital measurement of SARS-CoV-2 transmission risk from 7 million contacts. (Nature 2024)

- DOI: 10.1038/s41586-023-06952-2 | PMCID: PMC10830410 | PMID: 38122820
- Evidence: Classifiers used included logistic regression, gradient-boosting machines 31 and extreme gradient-boosting XGBoost 32 with 10, 100 and 400 rounds.
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [XGBoost]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: Following the SCENIC+ approach, we inferred TF-to-gene relationships by combining XGBoost-based prediction of TF influence on gene expression.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Evidence: We used an extreme gradient boosting-based machine learning framework (XGBoost; Methods ) for its model explainability, streamlined implementation, and the relatively few training examples it requires.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### Data-driven de novo design of super-adhesive hydrogels. (Nature 2025)

- DOI: 10.1038/s41586-025-09269-4 | PMCID: PMC12328221 | PMID: 40770436
- Evidence: Non-linear models comprised k -nearest neighbours (KNN), kernel ridge regression (KRR), support vector regression (SVR), random forest regression (RFR), gradient boosting regression with XGBoost (XGB), extra trees regression (ETR) and Gaussian process (GP) with a Matérn kernel 32 , 34 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost] -> machine learning [UMAP] -> stage not stated [Python, scikit-learn v1.0.2]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Version used: **2.0.3**
- Evidence: ...analysis across gestational ages To evaluate the transcriptomic correspondence of EN-ET and EN-IT scSHC subclusters across different ages, we applied XGBoost (v.2.0.3) 41 , a distributed gradient-boosted decision-tree-based classification method.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: The annotated integrated dataset compilation was used as input for feature selection with XGBoost 67 .
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Accurate predictions on small data with a tabular foundation model. (Nature 2025)

- DOI: 10.1038/s41586-024-08328-6 | PMCID: PMC11711098 | PMID: 39780007
- Evidence: We compared TabPFN against state-of-the-art baselines, including tree-based methods (random forest 38 , XGBoost (XGB) 7 , CatBoost 9 , LightGBM 8 ), linear models, support vector machines (SVMs) 39 and MLPs 34 .
- Full pipeline: normalisation [NumPy] -> differential/statistical testing [LightGBM, XGBoost]

### An AI system to help scientists write expert-level empirical software. (Nature 2026)

- DOI: 10.1038/s41586-026-10658-6 | PMCID: PMC13293872 | PMID: 42156545
- Evidence: For each dataset, we used a search of 300 nodes, with the system permitted to use a broad suite of machine learning libraries, including scikit-learn, XGBoost and statsmodels.
- Full pipeline: stage not stated [NumPy, XGBoost, scikit-learn, statsmodels]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Evidence: Direct regression As our first approach in modelling HOMA-IR, we used gradient boosting machines; specifically, the XGBoost framework 48 , 49 .
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Evidence: XGBoost machine learning XGBoost machine learning models were developed to: (1) classify patients with CRC and healthy individuals, and detect early colorectal precancerous lesions (CRA); and (2) diagnose and grade patients with DLBCL at different stages.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Quantum spin resonance in engineered proteins for multimodal sensing. (Nature 2026)

- DOI: 10.1038/s41586-025-09971-3 | PMCID: PMC12851924 | PMID: 41565820
- Evidence: To perform the population decomposition, we trained a machine-learning classifier (XGBoost 67 ) on the dynamic data (that is, fluorescence versus time) used to generate Fig.
- Full pipeline: machine learning [XGBoost] -> stage not stated [NumPy v126.4, SciPy v1.15.1, scikit-image v0.20.0, scikit-learn v1.6.1]

### Predatory aggression evolved through adaptations to noradrenergic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-10009-x | PMCID: PMC12960248 | PMID: 41565818
- Evidence: Behavioural state classification Behavioural feature data with cluster labels found by embedding and clustering were used to train an XGBoost Classifier on the preprocessed data.
- Full pipeline: dimensionality reduction/clustering [UMAP, XGBoost] -> machine learning [UMAP, XGBoost] -> stage not stated [ImageJ, scikit-learn]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: To minimize overfitting when applying GeneBayes to LoF burden test estimates, we first performed feature selection using the BoostRFE function (boost recursive feature elimination) from the shap-hypetune package (see the URL in the Code availability section) to fit XGBoost 76 models on the sign and magnitude of γ ^ , the estimated effect size from LoF burden test summary statistics.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### A Bayesian neural network predicts the dissolution of compact planetary systems. (PNAS 2021)

- DOI: 10.1073/pnas.2026053118 | PMCID: PMC8501828 | PMID: 34599094
- Evidence: For the second, labeled “Modified Tamayo+20,” the model is an XGBoost ( 62 ) regression model (rather than classification) retrained on the same features as used in ref.
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [XGBoost]

### Interpreting machine learning models to investigate circadian regulation and facilitate exploration of clock function. (PNAS 2021)

- DOI: 10.1073/pnas.2103070118 | PMCID: PMC8364196 | PMID: 34353905
- Evidence: The following classifiers were tested: Logistic Regression, Gaussian process, Random Forest, XGBoost, LightGBM, Support Vector Machine (linear kernel), Decision Tree, and K nearest neighbors.
- Full pipeline: differential/statistical testing [LightGBM, XGBoost] -> machine learning [LightGBM, TensorFlow v2.0.0, XGBoost] -> stage not stated [Jupyter, WGCNA]

### Prevalence and drivers of abrupt vegetation shifts in global drylands. (PNAS 2022)

- DOI: 10.1073/pnas.2123393119 | PMCID: PMC9618119 | PMID: 36252001
- Evidence: We used xgboost algorithms in R to perform the RF algorithm ( 92 ).
- Full pipeline: stage not stated [R, XGBoost]

### Melting temperature prediction using a graph neural network model: From ancient minerals to new materials. (PNAS 2022)

- DOI: 10.1073/pnas.2209630119 | PMCID: PMC9457469 | PMID: 36044552
- Evidence: We benchmark our GNN model with XGBoost, one of the most popular gradient boosting methods.
- Full pipeline: machine learning [TensorFlow] -> stage not stated [XGBoost]

### Model-free prediction test with application to genomics data. (PNAS 2022)

- DOI: 10.1073/pnas.2205518119 | PMCID: PMC9407618 | PMID: 35969737
- Evidence: XGBoost tree ( 18 ) is implemented as the regression algorithm due to its fast computational speed and good flexibility to capture nonlinear relationships.
- Full pipeline: differential/statistical testing [XGBoost] -> stage not stated [Seurat]

### Screening membraneless organelle participants with machine-learning models that integrate multimodal features. (PNAS 2022)

- DOI: 10.1073/pnas.2115369119 | PMCID: PMC9214545 | PMID: 35687670
- Evidence: XGBoost classification model.
- Full pipeline: stage not stated [GSEA, InterProScan, XGBoost]

### Accurate virus identification with interpretable Raman signatures by machine learning. (PNAS 2022)

- DOI: 10.1073/pnas.2118836119 | PMCID: PMC9191668 | PMID: 35653572
- Evidence: To perform virus identification from Raman spectra, we compared the performances of several different ML models including XGBoost ( 19 ) and CNN.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [XGBoost]

### The 103,200-arm acceleration dataset in the UK Biobank revealed a landscape of human sleep phenotypes. (PNAS 2022)

- DOI: 10.1073/pnas.2116729119 | PMCID: PMC8944865 | PMID: 35302893
- Evidence: The original sleep/wake classification algorithm is a machine learning–based algorithm that uses XGBoost and the power spectrum of jerk (a derivative of acceleration) as its features ( 28 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [XGBoost]

### The dynamic trophic architecture of open-ocean protist communities revealed through machine-guided metatranscriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2100916119 | PMCID: PMC8851463 | PMID: 35145022
- Evidence: The features that impacted classification accuracy were determined for the Random Forest and XGBoost classifiers using an in-house version of the train-test MDA method ( 59 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> normalisation [Trimmomatic v0.36, kallisto] -> differential/statistical testing [DESeq2] -> machine learning [XGBoost] -> stage not stated [HMMER v3.1b]

### Metabolomic selection for enhanced fruit flavor. (PNAS 2022)

- DOI: 10.1073/pnas.2115865119 | PMCID: PMC8860002 | PMID: 35131943
- Evidence: ...multilayer perceptron neural network and a Bayesian neural network; decision tree-based models such as random forest, gradient boosting machines, and XGBoost; and models frequently used in genomic selection such as Bayes A, Bayes B, and Bayes Cπ.
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [XGBoost] -> visualisation [Cytoscape v3.7.1] -> stage not stated [R, WGCNA]

### Sparsity of higher-order landscape interactions enables learning and prediction for microbiomes. (PNAS 2023)

- DOI: 10.1073/pnas.2307313120 | PMCID: PMC10691334 | PMID: 37991947
- Evidence: Tree-based ensemble learners, like the random forest regressor and xgboost, are popular choices of supervised learning algorithms, especially when the predictors are not sure to be linearly related to the target variables.
- Full pipeline: stage not stated [Python, XGBoost, scikit-learn]

### Amazon deforestation causes strong regional warming. (PNAS 2023)

- DOI: 10.1073/pnas.2309123120 | PMCID: PMC10636322 | PMID: 37903256
- Evidence: We used a gradient-boosting decision tree algorithm (XGBoost) ( 65 ) as our model of choice, well suited to the regression problem with tabular data.
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [Jupyter] -> stage not stated [Python v3.9.7]

### Space weather disrupts nocturnal bird migration. (PNAS 2023)

- DOI: 10.1073/pnas.2306317120 | PMCID: PMC10589677 | PMID: 37812699
- Evidence: We residualized our response variables using MLT models (function “xgb.train,” package “xgboost”) ( 38 ) built with our weather, geographic, and temporal variables.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [R v4.2.0, XGBoost]

### Predicting substantive biomedical citations without full text. (PNAS 2023)

- DOI: 10.1073/pnas.2213697120 | PMCID: PMC10372685 | PMID: 37463199
- Evidence: Source code for the SPECTER and XGBoost libraries used in this study are available online ( 22 , 63 , 64 ).
- Full pipeline: stage not stated [XGBoost]

### Large-scale climate patterns offer preseasonal hints on the co-occurrence of heat wave and O<sub>3</sub> pollution in China. (PNAS 2023)

- DOI: 10.1073/pnas.2218274120 | PMCID: PMC10293814 | PMID: 37339212
- Evidence: This O 3 dataset was reconstructed with an eXtreme Gradient Boosting (XGBoost) model that integrated high-resolution meteorological data, satellite retrievals of trace gases, etc., and both crossvalidation and independent validation with historical observations of O 3 in China confirmed the accuracy.
- Full pipeline: structure determination [XGBoost] -> stage not stated [CESM]

### On the rise of fear speech in online social media. (PNAS 2023)

- DOI: 10.1073/pnas.2212270120 | PMCID: PMC10089164 | PMID: 36877833
- Evidence: We then use two one-vs-rest classifier–logistic regression (LR), support vector classifier (SVC) as well as XGBoost.
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [XGBoost]

### Reducing the uncertainty in estimating soil microbial-derived carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2401916121 | PMCID: PMC11363314 | PMID: 39172788
- Evidence: Hence, we selected six representative tree ensemble methods, including Random Forest ( 37 ), extreme gradient boosting model-XGBoost ( 38 ), light gradient boosting machine model-LightGBM ( 39 ), category gradient boosting decision trees model-CatBoost ( 40 ), Deep Forest ( 41 ), and Auto-Sklearn ( 42 ).
- Full pipeline: stage not stated [LightGBM, XGBoost]

### A potential role for RNA aminoacylation prior to its role in peptide synthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2410206121 | PMCID: PMC11363276 | PMID: 39178230
- Evidence: The sequencing data were additionally analyzed using the Python XGBoost package ( 54 ), the Python SHAP package ( 55 ), and the schemaball interaction network with a modified version of Oleg Komarov MATLAB code ( 56 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [XGBoost]

### Age-related behavioral resilience in smartphone touchscreen interaction dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2311865121 | PMCID: PMC11194488 | PMID: 38861610
- Evidence: From these 2,503 features, 250 features were selected using an iterative method that reduced the number of features based on the least significant features at each iteration using the Gini importance contribution method for XGBoost ( 53 ).
- Full pipeline: stage not stated [XGBoost]

### Machine learning enables identification of an alternative yeast galactose utilization pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2315314121 | PMCID: PMC11067038 | PMID: 38669185
- Version used: **1.7.3**
- Evidence: We trained a machine learning algorithm built by an XGBoost (1.7.3) ( 57 ) random forest classifier (XGBRFClassifier()) with the parameters “max_depth=12 and n_estimators = 100; all other parameters were in their default settings.
- Full pipeline: quantification [ggplot2 v3.4.2] -> machine learning [XGBoost v1.7.3, scikit-learn] -> visualisation [ggplot2 v3.4.2] -> stage not stated [HMMER, InterProScan]

### Cross-prediction-powered inference. (PNAS 2024)

- DOI: 10.1073/pnas.2322083121 | PMCID: PMC11009639 | PMID: 38568975
- Evidence: To illustrate the point that cross-prediction can be applied with any black-box model, we train gradient-boosted trees via XGBoost ( 57 ) to obtain the models f ( j ) .
- Full pipeline: stage not stated [AlphaFold, XGBoost]

### Positive effects of public breeding on US rice yields under future climate scenarios. (PNAS 2024)

- DOI: 10.1073/pnas.2309969121 | PMCID: PMC10990131 | PMID: 38498708
- Evidence: Ten machine learning models (CatBoost, GradientBoost, RandomForest, AdaBoost, XGBoost, LASSO, Elastic net, Bayesian Ridge, Support vector, and Stochastic Gradient Descent) were utilized to develop a two-layer meta learner ensemble model for rice yield prediction ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [XGBoost]

### Interpreting chemisorption strength with AutoML-based feature deletion experiments. (PNAS 2024)

- DOI: 10.1073/pnas.2320232121 | PMCID: PMC10962981 | PMID: 38478684
- Evidence: Among the models offered by Autogluon, three tree-based models, XGBoost, LightGBM, and CatBoost excelled, with average testing set MAEs of 0.29, 0.28, and 0.23 eV across five different training-testing sets, respectively.
- Full pipeline: machine learning [LightGBM, XGBoost]

### A comprehensive patient-specific prediction model for temporomandibular joint osteoarthritis progression. (PNAS 2024)

- DOI: 10.1073/pnas.2306132121 | PMCID: PMC10895339 | PMID: 38346188
- Evidence: ...NET), or the selection frequency of least absolute shrinkage and selection operator (denoted by Glmnet), or the eXtreme Gradient Boosting (denoted by XGBoost) feature selection methods yielded the highest ACC, AUC and F1 scores on the validation dataset, by average.
- Full pipeline: stage not stated [XGBoost]

### Development of prediction models to identify hotspots of schistosomiasis in endemic regions to guide mass drug administration. (PNAS 2024)

- DOI: 10.1073/pnas.2315463120 | PMCID: PMC10786280 | PMID: 38181058
- Evidence: We used the XGBoost package (version 1.7.6) to implement boosted trees models ( 56 ).
- Full pipeline: stage not stated [Python v3.9.7, XGBoost, scikit-learn]

### Evaluating large language models in biomedical data science challenges through a classroom experiment. (PNAS 2025)

- DOI: 10.1073/pnas.2521062122 | PMCID: PMC12718336 | PMID: 41380002
- Evidence: On average, gradient boosting appears more than once per submission, as each submission may include multiple software packages implementing different variants, such as XGBoost ( 27 ), CatBoost ( 28 ), and LightGBM ( 29 ).
- Full pipeline: stage not stated [LightGBM, XGBoost]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Evidence: Following creation of the GNN model, a gradient-boosting library, XGBoost, was added to simulate species’ thermal limits further.
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### Graph neural networks for predicting metal-ligand coordination of transition metal complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2415658122 | PMCID: PMC12541316 | PMID: 41052327
- Evidence: In addition to the models trained to predict number and identity of coordinating atoms, we trained a separate model to identify hemilabile ligands and determine whether our approach could outperform the XGBoost models introduced in prior work ( 29 ).
- Full pipeline: machine learning [XGBoost] -> stage not stated [NetworkX, Open Babel, RDKit]

### Generalized convolutional many-body distribution functional representations. (PNAS 2025)

- DOI: 10.1073/pnas.2415662122 | PMCID: PMC12541311 | PMID: 41052323
- Evidence: 4 where cMBDF based feature vectors are paired with an XGBoost regressor ( 35 ) for prediction of a few intensive molecular properties.
- Full pipeline: stage not stated [NumPy, PySCF, Python, SciPy, XGBoost]

### Riverine heat waves on the rise, outpacing air heat waves. (PNAS 2025)

- DOI: 10.1073/pnas.2503160122 | PMCID: PMC12501193 | PMID: 40982675
- Evidence: We used the R package “XGBoost” ( 76 ) for BRT model to identify influential drivers of riverine heat wave trends.
- Full pipeline: quantification [R] -> stage not stated [XGBoost]

### Identifying fish populations prone to abrupt shifts via dynamical footprint analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2505461122 | PMCID: PMC12403094 | PMID: 40825133
- Evidence: The BRT model was trained using the “train” function from the “caret” package, applying the “xgbTree” method to leverage the boosting capabilities of the “XGBoost” library.
- Full pipeline: machine learning [XGBoost] -> stage not stated [R]

### SpecTf: Transformers enable data-driven imaging spectroscopy cloud detection. (PNAS 2025)

- DOI: 10.1073/pnas.2502903122 | PMCID: PMC12260531 | PMID: 40608670
- Evidence: First, the GBT classification model was implemented using the Python XGBoost library ( 29 ).
- Full pipeline: stage not stated [PyTorch, XGBoost]

### Cross-species modeling of plant genomes at single-nucleotide resolution using a pretrained DNA language model. (PNAS 2025)

- DOI: 10.1073/pnas.2421738122 | PMCID: PMC12184517 | PMID: 40489624
- Evidence: For each task, the pretrained model weights were frozen, and XGBoost models (n_estimators = 1,000, max_depth = 6, learning_rate = 0.1) were trained using embeddings extracted from the last hidden state of the pretrained model.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [XGBoost] -> visualisation [UMAP] -> stage not stated [BEDTools, BUSCO, VEP]

### A skin-interfaced wireless wearable device and data analytics approach for sleep-stage and disorder detection. (PNAS 2025)

- DOI: 10.1073/pnas.2501220122 | PMCID: PMC12168010 | PMID: 40478868
- Evidence: ( F ) SHAP values of classifying WNR and WS stages using an XGBoost model.
- Full pipeline: differential/statistical testing [XGBoost] -> stage not stated [Singularity]

### Accurate identification and mechanistic evaluation of pathogenic missense variants with &lt;i&gt;Rhapsody-2&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418100122 | PMCID: PMC12067267 | PMID: 40314982
- Evidence: Complete or partial sets of descriptors were used in training Rhapsody-2 classifier or its variants, respectively, with XGBoost algorithm.
- Full pipeline: alignment/mapping [AlphaFold] -> machine learning [XGBoost]

### Prediction of carbon nanostructure mechanical properties and the role of defects using machine learning. (PNAS 2025)

- DOI: 10.1073/pnas.2415068122 | PMCID: PMC11912458 | PMID: 40030034
- Evidence: An interesting aspect of the results is that HS-GNN provides a suitable level of accuracy for in-distribution and out-of-distribution data, while XGBoost excels with evenly spread training data inside a distribution that can be relatively sparse.
- Full pipeline: machine learning [XGBoost]

### Fast Interpretable Greedy-Tree Sums. (PNAS 2025)

- DOI: 10.1073/pnas.2310151122 | PMCID: PMC11848335 | PMID: 39951504
- Evidence: We compare the prediction performance of FIGS and Bagging-FIGS to that of four other algorithms: random forest, XGBoost, and penalized iteratively reweighted least squares (PIRLS) on the log-likelihood of a generative additive model.
- Full pipeline: stage not stated [XGBoost]

### Transformations of the spatial activity manifold convey aversive information in CA3. (PNAS 2026)

- DOI: 10.1073/pnas.2517639123 | PMCID: PMC13273363 | PMID: 42284325
- Evidence: Decoding was performed using the package developed by the Kording Lab ( 28 ), specifically the Wiener, support vector regression (SVR), and extreme gradient boost (XGBoost) decoders.
- Full pipeline: differential/statistical testing [XGBoost] -> stage not stated [scikit-learn]

### Informal connections outweigh coauthorship ties in academic impact. (PNAS 2026)

- DOI: 10.1073/pnas.2511050123 | PMCID: PMC13142791 | PMID: 42044345
- Evidence: In SI Appendix , sections S15 and S16 we provide additional robustness tests using a classifier version of the random forest model, and two additional variations using XGBoost and Support Vector classifiers.
- Full pipeline: machine learning [XGBoost]

### Unveiling the glymphatic system's role in brain aging: A comprehensive biomarker and modifiable intervention target. (PNAS 2026)

- DOI: 10.1073/pnas.2516601123 | PMCID: PMC13142974 | PMID: 42044335
- Evidence: We employed XGBoost models to estimate an individual’s chronological age in a healthy population using 10-fold cross-validation.
- Full pipeline: quality control [PLINK] -> alignment/mapping [ANNOVAR] -> variant calling [PLINK] -> differential/statistical testing [FUMA, LightGBM, Metascape] -> machine learning [XGBoost]

### Coupled machine learning-ecosystem ensemble models substantially improve predictions of nitrous oxide (N&lt;sub&gt;2&lt;/sub&gt;O) fluxes from US croplands. (PNAS 2026)

- DOI: 10.1073/pnas.2524808123 | PMCID: PMC12974439 | PMID: 41779779
- Evidence: ...urn used as input data for an ensemble of four ML models [Random Forest ( 30 ), Gradient Boosting ( 31 ), Support-Vector Regression (SVR) ( 32 ), and XGBoost ( 33 )] blended by an SVR metalearner.
- Full pipeline: differential/statistical testing [XGBoost]

### Global analysis of protein degradation reveals instability of diverse regulators in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2515265123 | PMCID: PMC12974527 | PMID: 41774798
- Evidence: Four models were considered for this classification task: logistic regression with L1 regularization, random forest, artificial neural network (ANN), and gradient-boosted logistic regression with XGBoost ( 70 ).
- Full pipeline: quantification [limma] -> normalisation [limma] -> differential/statistical testing [XGBoost, limma] -> machine learning [XGBoost] -> stage not stated [AlphaFold, R, STRING db]

### Interpretable early warnings using machine learning in an online game-experiment. (PNAS 2026)

- DOI: 10.1073/pnas.2503493122 | PMCID: PMC12773730 | PMID: 41481444
- Evidence: We build our warning system by training gradient-boosted decision trees with XGBoost ( 62 ) to predict the time-to-transition, Δ ∗ = t ∗ − t .
- Full pipeline: machine learning [XGBoost]

