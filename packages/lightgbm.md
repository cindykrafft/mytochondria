# LightGBM

- **Category:** general
- **Papers in survey:** 10
- **Journals:** PNAS (7), Nature (3)
- **Years:** 2021 (2), 2022 (1), 2024 (2), 2025 (3), 2026 (2)
- **Pipeline stages it appears in:** differential/statistical testing (5), machine learning (2)

## Papers

### Machine learning and phone data can improve targeting of humanitarian aid. (Nature 2022)

- DOI: 10.1038/s41586-022-04484-9 | PMCID: PMC8967719 | PMID: 35296856
- Evidence: Specifically, we train a gradient boosting regressor with Microsoft’s LightGBM for the two matched survey-CDR datasets separately.
- Full pipeline: stage not stated [LightGBM]

### Accurate predictions on small data with a tabular foundation model. (Nature 2025)

- DOI: 10.1038/s41586-024-08328-6 | PMCID: PMC11711098 | PMID: 39780007
- Evidence: We compared TabPFN against state-of-the-art baselines, including tree-based methods (random forest 38 , XGBoost (XGB) 7 , CatBoost 9 , LightGBM 8 ), linear models, support vector machines (SVMs) 39 and MLPs 34 .
- Full pipeline: normalisation [NumPy] -> differential/statistical testing [LightGBM, XGBoost]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Supervised machine learning models Multiple regression algorithms were initially utilized for development of the relative rodent multi-tissue chronological clock, including elastic net, BR, SVM, random forest, KNN and LightGBM.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Global monitoring of the impact of the COVID-19 pandemic through online surveys sampled from the Facebook user base. (PNAS 2021)

- DOI: 10.1073/pnas.2111455118 | PMCID: PMC8713788 | PMID: 34903657
- Evidence: Four base-modeling methods (Logistic Regression, Gaussian Naive Bayes, Support Vector Machine, and Light Gradient Boosting Machine) were compared to identify the Light Gradient Boosting Machine (LightGBM) as the highest performing at a moderate time cost.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap v2.3.4, R v3.6] -> differential/statistical testing [LightGBM] -> visualisation [ComplexHeatmap v2.3.4, Python v3.8, R v3.6]

### Interpreting machine learning models to investigate circadian regulation and facilitate exploration of clock function. (PNAS 2021)

- DOI: 10.1073/pnas.2103070118 | PMCID: PMC8364196 | PMID: 34353905
- Evidence: The following classifiers were tested: Logistic Regression, Gaussian process, Random Forest, XGBoost, LightGBM, Support Vector Machine (linear kernel), Decision Tree, and K nearest neighbors.
- Full pipeline: differential/statistical testing [LightGBM, XGBoost] -> machine learning [LightGBM, TensorFlow v2.0.0, XGBoost] -> stage not stated [Jupyter, WGCNA]

### Reducing the uncertainty in estimating soil microbial-derived carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2401916121 | PMCID: PMC11363314 | PMID: 39172788
- Evidence: Hence, we selected six representative tree ensemble methods, including Random Forest ( 37 ), extreme gradient boosting model-XGBoost ( 38 ), light gradient boosting machine model-LightGBM ( 39 ), category gradient boosting decision trees model-CatBoost ( 40 ), Deep Forest ( 41 ), and Auto-Sklearn ( 42 ).
- Full pipeline: stage not stated [LightGBM, XGBoost]

### Interpreting chemisorption strength with AutoML-based feature deletion experiments. (PNAS 2024)

- DOI: 10.1073/pnas.2320232121 | PMCID: PMC10962981 | PMID: 38478684
- Evidence: In this work, Autogluon conducts exhaustive testing across a diverse range of models and configurations, encompassing neural networks, LightGBM and CatBoost boosted trees, Random Forests, and Extremely Randomized Trees, leading to the creation of thousands of distinct models with varying structures and hyperparameter settings.
- Full pipeline: machine learning [LightGBM, XGBoost]

### Evaluating large language models in biomedical data science challenges through a classroom experiment. (PNAS 2025)

- DOI: 10.1073/pnas.2521062122 | PMCID: PMC12718336 | PMID: 41380002
- Evidence: On average, gradient boosting appears more than once per submission, as each submission may include multiple software packages implementing different variants, such as XGBoost ( 27 ), CatBoost ( 28 ), and LightGBM ( 29 ).
- Full pipeline: stage not stated [LightGBM, XGBoost]

### Improving outbreak forecasts through model augmentation. (PNAS 2025)

- DOI: 10.1073/pnas.2508575122 | PMCID: PMC12582271 | PMID: 41134625
- Evidence: Epimodulation substantially improves the performance of ARIMA, Holt-Winters, Spline, Prophet, and LightGBM models in retrospective forecasts of COVID-19 hospital admissions from September 15, 2020, to August 15, 2023, a period spanning six epidemic waves in the United States ( Fig.
- Full pipeline: stage not stated [LightGBM, R]

### Unveiling the glymphatic system's role in brain aging: A comprehensive biomarker and modifiable intervention target. (PNAS 2026)

- DOI: 10.1073/pnas.2516601123 | PMCID: PMC13142974 | PMID: 42044335
- Evidence: DTI-ALPS, diffusion tensor imaging along perivascular spaces; ADNI, Alzheimer’s Disease Neuroimaging Initiative; TALENT, Tongji cerebrAl smalL vEssel disease and agiNg cohort; XGBoost, eXtreme Gradient Boosting; CatBoost, Categorical Boosting; LightGBM, Light Gradient Boosting Machine; SVR, Support Vector Regression; SHAP, SHapley Additive exPlanations; BAG, Brain age gap; CVS, Cardiovascular syst...
- Full pipeline: quality control [PLINK] -> alignment/mapping [ANNOVAR] -> variant calling [PLINK] -> differential/statistical testing [FUMA, LightGBM, Metascape] -> machine learning [XGBoost]

