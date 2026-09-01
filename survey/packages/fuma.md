# FUMA

- **Category:** statgen
- **Papers in survey:** 18
- **Journals:** PNAS (11), Nature (5), Science (1), Cell (1)
- **Years:** 2021 (1), 2022 (2), 2023 (3), 2024 (3), 2025 (6), 2026 (3)
- **Versions named:** 1.6.3 (1), 1.5.6 (1), 1.5.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (6), differential/statistical testing (4), visualisation (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: ...NK 1.9 Purcell et al., 2007 https://www.cog-genomics.org/plink/1.9/ COJO in GCTA Yang et al., 2011 , 2012 https://cnsgenomics.com/software/gcta/#COJO FUMA Watanabe et al., 2017 https://fuma.ctglab.nl LDHub Zheng et al., 2017 https://github.com/bulik/ldsc PRsice2 Choi and O’Reilly, 2019 ; Choi et al., 2020 https://www.prsice.info LDpred Vilhjálmsson et al., 2015 https://github.com/bvilhjal/ldpred L...
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: FUMA SNP2GENE was then used to identify the nearest genes to each locus on the basis of the linkage disequilibrium calculated using the 1000 Genomes EUR populations, and explore previously reported associations in the GWAS catalogue 40 , 71 (Supplementary Table 7 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Evidence: FUMA, a web-based platform for GWAS analysis 76 , was used to identify high-correlation SNPs with an LD r 2 ≥ 0.8 with lead SNPs.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.5.6**
- Evidence: 22 were uploaded to the FUMA (v.1.5.6) 108 web server ( https://fuma.ctglab.nl ).
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Evidence: To identify risk loci and their lead variants, we performed LD clumping using the Functional Mapping and Annotation of Genome-Wide Association Studies (FUMA) 49 .
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Version used: **1.6.3**
- Evidence: Genome-wide significance was defined as P < 5 × 10 −8 , and independent risk loci were defined in FUMA (v1.6.3) 48 , based on 1000Gv3 (EUR population; r 2 threshold of 0.6) lead SNPs (merging distance of 250 kb).
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Using neuroimaging genomics to investigate the evolution of human brain structure. (PNAS 2022)

- DOI: 10.1073/pnas.2200638119 | PMCID: PMC9546597 | PMID: 36161899
- Evidence: The GWAS results for left pars triangularis were annotated using Functional Mapping and Annotation of Genome-Wide Association Studies (FUMA; https://fuma.ctglab.nl ; version 1.3.6a) ( 64 ).
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [LDSC] -> stage not stated [FreeSurfer, PLINK, R, ggplot2]

### Genome-wide analyses of individual differences in quantitatively assessed reading- and language-related skills in up to 34,000 people. (PNAS 2022)

- DOI: 10.1073/pnas.2202764119 | PMCID: PMC9436320 | PMID: 35998220
- Evidence: Next, we used MAGMA gene property analysis ( 22 ) to study whether the multivariate GenLang GWAS results were enriched in a specific tissue or brain cell type using tissue-specific and cell type–specific gene expression data in Functional Mapping and Annotation (FUMA) ( 42 , 43 ).
- Full pipeline: alignment/mapping [FUMA] -> stage not stated [LDSC, MAGMA]

### Genomic loci influence patterns of structural covariance in the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2300842120 | PMCID: PMC10756284 | PMID: 38127979
- Evidence: Based on these gene-level P -values, we performed hypothesis-free gene set pathway analysis using MAGMA ( 16 ) ( Method 4E ): a more stringent correction for multiple comparisons was performed than the prioritized gene set enrichment analysis using GENE2FUN from FUMA ( Method 4F and Fig.
- Full pipeline: differential/statistical testing [FUMA, MAGMA, PLINK] -> stage not stated [GCTA, GSEA, LDSC]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: Functional Follow-Up with FUMA.
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### Machine-learning models based on histological images from healthy donors identify imageQTLs and predict chronological age. (PNAS 2025)

- DOI: 10.1073/pnas.2423469122 | PMCID: PMC12646272 | PMID: 41218125
- Evidence: A genome-wide significance threshold of P -value < 5e-8 was applied, and significant SNPs were annotated using Functional Mapping and Annotation of Genome-Wide Association Studies (FUMA) v1.5.2 ( Dataset S3 ) ( 49 ).
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [PLINK v2.0] -> stage not stated [DESeq2, GSEA, QuPath v0.4.3]

### Life without sex: Large-scale study links sexlessness to physical, cognitive, and personality traits, socioecological factors, and DNA. (PNAS 2025)

- DOI: 10.1073/pnas.2418257122 | PMCID: PMC12478097 | PMID: 40956885
- Evidence: We used the GWAS summary statistics to compute gene-based P -value in MAGMA ( 36 ) for 18,714 protein-coding genes using FUMA ( 37 ).
- Full pipeline: differential/statistical testing [FUMA, LDSC, MAGMA] -> stage not stated [R]

### A proteomic signature of healthspan. (PNAS 2025)

- DOI: 10.1073/pnas.2414086122 | PMCID: PMC12168021 | PMID: 40478878
- Version used: **1.5.2**
- Evidence: Proteins significant at the Bonferroni-corrected level were entered into the gene set analysis implemented in the FUnctional Mapping and Annotation (FUMA version 1.5.2) of Genome-Wide Association Studies.
- Full pipeline: alignment/mapping [FUMA v1.5.2] -> differential/statistical testing [FUMA v1.5.2] -> stage not stated [GSEA, R]

### O-GalNAc glycans are enriched in neuronal tracts and regulate nodes of Ranvier. (PNAS 2025)

- DOI: 10.1073/pnas.2418949122 | PMCID: PMC11892645 | PMID: 39999163
- Evidence: Gene set enrichment analysis and figures were generated using the FUMA GWAS GENE2FUNC online tool ( 75 ) on January 9, 2024, with adjusted P -value threshold set at <0.05.
- Full pipeline: visualisation [FUMA] -> stage not stated [ImageJ v1.53t, QuPath v0.3.2]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Evidence: Enrichment analysis of tissue types was performed by FUMA ( 74 ).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Unveiling the glymphatic system's role in brain aging: A comprehensive biomarker and modifiable intervention target. (PNAS 2026)

- DOI: 10.1073/pnas.2516601123 | PMCID: PMC13142974 | PMID: 42044335
- Evidence: Genome-wide significant SNPs ( P < 5 × 10 −8 , linkage disequilibrium r 2 < 0.6) were identified, and candidate variants were annotated with r 2 ≥ 0.6, GWAS P value < 1 × 10 −5 , and MAF >0.001 in FUMA ( https://fuma.ctglab.nl/ ) ( 66 ).
- Full pipeline: quality control [PLINK] -> alignment/mapping [ANNOVAR] -> variant calling [PLINK] -> differential/statistical testing [FUMA, LightGBM, Metascape] -> machine learning [XGBoost]

### The persistence and loss of hard selective sweeps amid admixture in ancient Eurasians. (PNAS 2026)

- DOI: 10.1073/pnas.2528672123 | PMCID: PMC13123867 | PMID: 42008668
- Evidence: We next performed an enrichment analysis for previously identified genome-wide association study (GWAS) annotations on the set of mapped genes using Functional Mapping and Annotation of Genome-Wide Association Studies (FUMA) ( 66 ).
- Full pipeline: alignment/mapping [FUMA] -> stage not stated [VEP]

### Diversity and scale: Genetic architecture of 2068 traits in the VA Million Veteran Program. (Science 2024)

- DOI: 10.1126/science.adj1182 | PMCID: PMC12857194 | PMID: 39024449
- Evidence: We determined genomic loci and lead variant via LD clumping in Plink 1.9 ( 51 ) using a two-tiered approach similar to that previously described in FUMA ( 52 ).
- Full pipeline: stage not stated [FUMA, LDSC, SAIGE, VEP]

