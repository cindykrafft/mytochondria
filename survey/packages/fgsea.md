# fgsea

- **Category:** genomics
- **Papers in survey:** 122
- **Journals:** Nature (68), PNAS (38), Cell (12), Science (4)
- **Years:** 2021 (11), 2022 (16), 2023 (19), 2024 (26), 2025 (32), 2026 (18)
- **Versions named:** 1.30.0 (4), 1.28.0 (4), 1.20.0 (3), 1.22.0 (3), 1.26.0 (3), 1.10.1 (2), 1.25.1 (1), 3.17 (1), 4.1 (1), 1.18.0 (1)
- **Pipeline stages it appears in:** differential/statistical testing (21), dimensionality reduction/clustering (7), normalisation (6), visualisation (2), quality control (1), variant calling (1)

## Papers

### Visualizing in deceased COVID-19 patients how SARS-CoV-2 attacks the respiratory and olfactory mucosae but spares the olfactory bulb. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.027 | PMCID: PMC8564600 | PMID: 34798069
- Evidence: ...ACTOME_OLFACTORY_SIGNALING_PATHWAY gene set https://www.gsea-msigdb.org/gsea/msigdb/cards/REACTOME_OLFACTORY_SIGNALING_PATHWAY Systematic name: M4072 fgsea Bioconductor package https://bioconductor.org/packages/release/bioc/html/fgsea.html v1.17.0 org.Hs.eg.db Bioconductor database https://bioconductor.org/packages/release/data/annotation/html/org.Hs.eg.db.html v3.12.0 Other GeoMx Digital Spatial ...
- Full pipeline: stage not stated [Bioconductor, R v4.1, fgsea]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Version used: **1.16.0**
- Evidence: ...tps://CRAN.R-project.org/package=ggplot2 R package – ComplexHeatmap v2.7.3 Bioconductor https://bioconductor.org/packages/ComplexHeatmap/ R package – fgsea v1.16.0 Bioconductor https://bioconductor.org/packages/fgsea/ Python Programming Language v3.8.3 Python https://www.python.org Python package scVelo v0.3.0 Bergen et al., 2020 https://scvelo.readthedocs.io/ CellBender Fleming et al., 2019 https...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Characterizing genetic intra-tumor heterogeneity across 2,658 human cancer genomes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.009 | PMCID: PMC8054914 | PMID: 33831375
- Evidence: Using the fgsea package in R ( Sergushichev, 2016 ), we computed an enrichment score for hits across the ranking for each SRB locus.
- Full pipeline: quantification [SAMtools] -> stage not stated [GSEA, IMPUTE2, Mutect2, R, fgsea]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...scovery D-001810-10-20 ON-TARGETplus Human TOP1 siRNA Horizon Discovery L-005278-00-0005 qPCR primers This Study STAR Methods Software and algorithms fgsea Korotkevich et al., 2019 https://bioconductor.org/packages/release/bioc/html/fgsea.html DoubletFinder McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder Seurat Stuart et al., 2019 https://satijalab.org/seurat/ DESeq2 Lov...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: ... https://bioconductor.org/packages/release/bioc/html/edgeR.html FGSEA (1.10.1) Sergushichev, 2016 https://bioconductor.org/packages/release/bioc/html/fgsea.html lme4 (1.1-23) Bates et al., 2015 https://cran.r-project.org/web/packages/lme4/index.html lmerTest Kuznetsova et al., 2017 https://cran.r-project.org/web/packages/lmerTest/index.html plsRglm (1.2.5) Bertrand and Maumy-Bertrand, 2019 https:/...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.030 | PMCID: PMC7584921 | PMID: 33147445
- Evidence: Gene Set Enrichment Analyses were performed using the fgsea package with Gene Ontology for biological processes (c5.bp.v7.1.symbols) ( Korotkevich et al., 2019 ).
- Full pipeline: read trimming [Cutadapt v1.13] -> alignment/mapping [STAR] -> stage not stated [DESeq2, GSEA, R, Seurat, fgsea]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ... Fastcluster ( Mulner, 2013 ) v1.1.25 FastQC ( Andrews, 2010 ) v0.11.9 https://github.com/s-andrews/FastQC featureCounts ( Liao et al., 2014 ) v1.6.4 fgsea ( Korotkevich et al., 2021 ) https://bioconductor.org/packages/release/bioc/html/fgsea.html FlowJo BD Biosciences v10.6 https://www.flowjo.com Fragpipe ( Yu et al., 2021 ) v13.0 GATK variant calling ( Van der Auwera and O’Connor, 2020 ) v4.1.7....
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: GSEA was performed with the R package “fgsea” v.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: The ensemble ID targeting multiple genes was collapsed (average) and a final gene data matrix was used for a modular repertoire analysis as previously described 82 , 83 or for gene set enrichment analysis (GSEA: fgsea) with hallmark gene sets ( http://www.gsea-msigdb.org/ ).
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 44 https://bioconductor.org/packages/release/bioc/html/fgsea.html Fiji-Imagej Schneider et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Distinct components of mRNA vaccines cooperate to instruct efficient germinal center responses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.023 | PMCID: PMC12878702 | PMID: 41406961
- Evidence: GSEA was performed by contrasting pseudo-bulk counts of biotin-positive and -negative cells with DESeq2 and testing genes ranked by −log10 p-value (signed by log fold change) for enrichment of a previously published LIPSTIC signature 34 with the R package fgsea.
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [GSEA, R, fgsea] -> stage not stated [Seurat]

### Citrate clearance is a major function of aconitase 2 in the canonical TCA cycle. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.028 | PMCID: PMC13045649 | PMID: 41763199
- Evidence: Genes were ranked by their Pearson correlation coefficient ( r ) and gene set enrichment analysis was performed using the ranked list with the fgsea package 98 (version 1.28.0) and Hallmark and Reactome gene sets using the msigdbr package (version 7.5.1) in R (version 4.3.2).
- Full pipeline: differential/statistical testing [DESeq2 v1.46.0] -> stage not stated [GSEA, R v4.3.2, featureCounts, fgsea, ggplot2 v3.5.2]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Fast Gene Set Enrichment Analysis was performed using R package ‘fgsea’ (nperm = 2000) 62 with the msigdb h.all.v6.2.symbols cancer hallmark gene sets 20 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: We used GSEA-preranked to test for an enrichment of ECM genes in the phenotypes using fgsea R package (v.1.14.0) 79 , with MatrisomeDB gene set collection 5 .
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### The neurons that restore walking after paralysis. (Nature 2022)

- DOI: 10.1038/s41586-022-05385-7 | PMCID: PMC9668750 | PMID: 36352232
- Evidence: 79 , by applying fgsea 80 to the signed −log 10 P values estimated by the GLMMs, and compared the normalized enrichment scores estimated by fgsea between acute and chronic perturbations.
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat, velocyto] -> normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.3, fgsea] -> simulation/modelling [Python v2.7] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain]

### Long-primed germinal centres with enduring affinity maturation and clonal migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05216-9 | PMCID: PMC9491273 | PMID: 36131022
- Evidence: Gene set enrichment analysis (GSEA) was conducted using the package fgsea in R 44 , 45 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [UCSF Chimera v1.13] -> visualisation [UCSF Chimera v1.13] -> stage not stated [GSEA, RELION v3.0, Seurat, fgsea]

### RASA2 ablation in T cells boosts antigen sensitivity and long-term function. (Nature 2022)

- DOI: 10.1038/s41586-022-05126-w | PMCID: PMC9433322 | PMID: 36002574
- Evidence: The R package fgsea 58 v1.18.0 was used to perform GSEA, with gene ranking based on DESeq2 test statistic and MSigDB v7.2 hallmark gene sets 59 as the reference gene lists.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [DESeq2, Seurat, fgsea] -> stage not stated [GSEA, ImageJ v1.52q, R]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: The plotEnrichment() function from the fgsea R package (version 1.16.0) was used to create GSEA enrichment plots.
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Evidence: 57 ), and subsequent gene set enrichment analysis was performed using the fgsea (ref.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### Intermittent PI3Kδ inhibition sustains anti-tumour immunity and curbs irAEs. (Nature 2022)

- DOI: 10.1038/s41586-022-04685-2 | PMCID: PMC9132770 | PMID: 35508656
- Version used: **1.10.1**
- Evidence: Gene Set Enrichment Analysis (GSEA) scores were estimated with fgsea (v1.10.1) in R using signal-to-noise ratio as the metric (minSize = 3 and maxSize = 500).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [GSEA, MACS2, Seurat v3.1.5, fgsea v1.10.1]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: Gene set enrichment analysis Gene set enrichment analysis (GSEA) 11 , 41 was done with the fast GSEA algorithm 42 using Bioconductor’s fgsea package 43 .
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Evidence: These gene signatures were used to perform a fast pre-ranked GSEA using fgsea bioconductor package 39 in R.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Signature of long-lived memory CD8<sup>+</sup> T cells in acute SARS-CoV-2 infection. (Nature 2022)

- DOI: 10.1038/s41586-021-04280-x | PMCID: PMC8810382 | PMID: 34875673
- Evidence: Gene set enrichment analysis 40 was performed on this pre-ranked list using the R package FGSEA ( https://github.com/ctlab/fgsea/ ) 41 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R v4.1.0, Seurat v4.0.3, fgsea]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Version used: **1.20.0**
- Evidence: We used the R package fgsea v.1.20.0 (ref.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Embryo-scale reverse genetics at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06720-2 | PMCID: PMC10665197 | PMID: 37968389
- Version used: **1.26.0**
- Evidence: We performed GSEA using the msigdbr ( https://davislaboratory.github.io/msigdb ) and fgsea (v.1.26.0) R packages 71 and the MSigDB ‘Hallmarks’ database via the msigdbR package (v.7.5.1) 72 , which summarizes 50 well-defined biological states and processes.
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Monocle v1.3.1, UMAP] -> differential/statistical testing [GSEA, R] -> stage not stated [ImageJ, fgsea v1.26.0]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: We further performed over-representation analysis using hypergeometric test from the fgsea R package.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Version used: **3.17**
- Evidence: 10g ), the list of expressed genes ranked by higher to lower LFC value was used as input to the R package fgsea (v.3.17) 59 to run GSEA using the mouse GO:BP dataset.
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Evidence: Pathway enrichment analyses We performed functional assessments of the effects of cellular composition variability on differences in gene expression between donors in the basal state and in response to each virus, using the fgsea R package (v.1.18.1) 83 and the default options.
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Gene set ontologies from the Molecular Signatures Database (MSigDB) were downloaded from https://gsea-msigdb.org and pathway enrichments were computed using fgsea 72 and gage 73 , retaining only Gene Ontology terms that were significant ( P < 0.05) for both.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **1.10.1**
- Evidence: The t -statistic generated by limma was used as input for GSEA for MSigDB hallmark gene sets 14 using the R package fgsea (v.1.10.1) 71 with default parameters.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Version used: **4.1**
- Evidence: The gene set enrichment analysis (GSEA) of the Reactome pathway Autophagy (R-HSA-9612973) was performed using fgsea (v.4.1) 49 . qPCR Total RNA was extracted from cell lines using Trizol Reagent (Invitrogen,15596018) and the total RNA extraction kit (Qiagen, 74004/74104) according to the manufacturer’s protocol.
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Version used: **1.18.0**
- Evidence: GSEAs GSEAs were performed using the R package fgsea (v.1.18.0) with the following parameters: minSize = 15, maxSize = 500, nperm = 100000.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: GSEA was performed on this pre-ranked list using the R package FGSEA ( https://github.com/ctlab/fgsea/ ) with default parameters and the GO Biological Process database, made accessible in R by the package msigdbr ( https://github.com/cran/msigdbr ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: Gene set enrichment analysis GSEA was carried out on all 6,495 C2 curated gene sets from the Molecular Signatures Database (MSigDB, http://www.broadinstitute.org/msigdb ) using the ‘fgsea’ R package (v.1.22 RRID: SCR_020938 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: The ranked genes were used for GSEA using the fgsea package in R.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Evidence: GSEA was conducted with the fgsea package v.1.30.0 by projecting the fold-change ranking onto the following MSigDB genesets ( http://www.gsea-msigdb.org/gsea/msigdb/ ): H (Hallmark), C2 CP (Curated canonical pathways), C3 (Regulatory targets) and C5 (Gene ontologies).
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Gene set enrichment and pathway analysis Rank-based gene set enrichment analysis and generating the associated random-walk plots were performed using the fgsea R package 56 .
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: GSEA was performed using the Bioconductor package fgsea with the default parameters on genes ranked by log[fold change] 91 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07752-y | PMCID: PMC11291290 | PMID: 39048822
- Evidence: The average log 2 fold change values were used as an input in GSEA implemented in the fgsea R package (v1.16.0).
- Full pipeline: normalisation [DESeq2 v1.30.1, limma] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [limma] -> stage not stated [R, Seurat, fgsea]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Version used: **1.22.0**
- Evidence: Gene set enrichment analysis was carried out using the fgsea v.1.22.0 R package for MSigDB Hallmark (msigdbr v.7.5.1) and MitoCarta v3.0 gene sets with 100,000 iterations.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### Discovery of WRN inhibitor HRO761 with synthetic lethality in MSI cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07350-y | PMCID: PMC11078746 | PMID: 38658754
- Evidence: In particular, we used the R package fgsea 52 (v.1.25.1) to estimate normalized enrichment statistics and associated P values, for each gene set in the Hallmark Collection (h.all.v6.2.symbols.gmt) from the Molecular Signatures Database 53 with nperm = 10,000.
- Full pipeline: normalisation [R, fgsea] -> differential/statistical testing [DESeq2, R, fgsea] -> stage not stated [GSEA, PHENIX, SciPy]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: Gene set enrichment analysis The fgsea R package 64 (v1.4.0) was used for gene set enrichment.
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: Unbiased gene set enrichment analysis was performed using fgsea package on differential expressed genes pre-ranked by fold change with 1,000 permutations (nominal P value cut-off <0.05) 53 .
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Version used: **1.26.0**
- Evidence: Gene set enrichment analysis was performed on differential expression analysis results using msigdbr (v7.5.1) and fgsea (v1.26.0).
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Version used: **1.20.0**
- Evidence: Gene set enrichment analysis was run on each cluster comparing samples with different condition against the Gene Ontology database using R package fgsea v1.20.0.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### Anti-TIGIT antibody improves PD-L1 blockade through myeloid and T&lt;sub&gt;reg&lt;/sub&gt; cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07121-9 | PMCID: PMC11139643 | PMID: 38418879
- Evidence: The moderated t -statistics from limma DEG tests were used as a preranked gene list input for pathway enrichment analysis, which was performed using the fgsea R package (v.1.14.0) 59 .
- Full pipeline: alignment/mapping [Bioconductor, R] -> quantification [Bioconductor, R] -> normalisation [Harmony v1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [fgsea] -> stage not stated [Seurat]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: For gene set enrichment analysis, pathways enriched in the ranked DEGs were identified against the mouse Molecular Signatures Database (MSigDB) 97 pathway collection ( P adj < 0.25) using the fgsea package in R, and the most biologically informative lists are shown. scRNA-seq analysis The CRC dataset ( GSE146409 ) 98 contained three patients with colorectal liver metastasis and a non-tumour indivi...
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Evidence: In detail, GSEA was performed by using gene sets published on the MsigDB (Reactome, KEGG, Biocarta and Hallmarks) 54 and from a published study 55 (ATF4) using the packages fgsea 56 (v.1.16.0) and GSEABase 57 (v.1.52.1).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: ...tial expression analysis; (2) defined gene sets as groups of these ranked transcripts assigned to the same metabolic pathway; and (3) performed GSEA (fgsea 61 , v.3.14).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: For Gene Set Enrichment Analysis (GSEA), genes were ranked by −log 10 ( P value) × sign(log 2 (fold change)) from DESeq2 results, and enrichment was run using the fgsea R package (v.1.28.0).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Evidence: We used the fora function from the fgsea R package v.1.27.0 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Gene set enrichment was performed using fgsea ( https://bioconductor.org/packages/release/bioc/html/fgsea.html ) using as input gene or protein list rank by relative changes (log 2 -transformed fold change of comparison).
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Evidence: GSEA was conducted using the fgsea 65 (v.1.28.0) and genekitr 66 (v.1.2.5) packages, exploring GO, KEGG, REACTOME, Hallmarks, Biocarta and WikiPathways databases.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: GSEA was performed using the fgsea 74 R package (v.1.26) with Gene Ontology biological process pathway sets from MSigDB 75 .
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: The R package fgsea 67 was used for GO term enrichment analysis on the log 2 -transformed fold change values from each group.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Precisely defining disease variant effects in CRISPR-edited single cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09313-3 | PMCID: PMC12488502 | PMID: 40702188
- Evidence: Gene set enrichment analysis We performed gene set enrichment using fgsea on the results from the linear models predicting differentially expressed genes associated with dosage in the CD45 experiment and polarization status in the IL2RA experiment.
- Full pipeline: alignment/mapping [kallisto] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> stage not stated [GSEA, R, lme4]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Genes were ranked according to log fold changes, and resulting ranks were used as input for the fgsea R package along with the Hallmark gene sets from the Molecular Signature Data Base (MSigDB; https://www.gsea-msigdb.org/gsea/msigdb ).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: Differential enrichment of gene sets between conditions was performed using gsea (fgsea package (v.1.28.0) 76 ).
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Version used: **1.22.0**
- Evidence: GSEA for bulk RNA-seq data was performed using the R package fgsea (1.22.0). scRNA-seq For the scRNA-seq, hepatocytes from wild-type mice, cholangiocytes from a Rosa26 -nTnG mouse and portal mesenchyme from a PDGFRα-H2B-GFP mouse sorted for SCA1 + cells were used.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### Targeting the SHOC2-RAS interaction in RAS-mutant cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-08931-1 | PMCID: PMC12137120 | PMID: 40335703
- Evidence: Pre-ranked gene-set enrichment analysis was performed for each contrast using the R package fgsea with signed P -values (sign(log 2 (FC)) × –log 10 ( P -value)) as ranks.
- Full pipeline: differential/statistical testing [DESeq2, edgeR] -> stage not stated [Picard, R, fgsea, ggplot2 v3.3.6, ggpubr v0.4.0]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Enrichment of the Hallmark and Reactome gene sets downloaded from MSigDB 68 were examined using fgsea 69 with genes ranked by logFC estimated from limma as input.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Evidence: Gene set enrichment analysis was carried out using the fgsea R package v.1.22.0 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: Gene set enrichment analysis was performed using the ‘fgsea’ R package (v1.20.0) 65 with the Hallmark pathways database provided by the ‘msigdbr’ R package (v7.5.1) 66 .
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Synthetic lethality of mRNA quality control complexes in cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08398-6 | PMCID: PMC11864970 | PMID: 39910291
- Evidence: Gene set enrichment analyses were performed using the fgsea package.
- Full pipeline: normalisation [featureCounts, limma] -> visualisation [PyMOL v1.7.6.6] -> stage not stated [fgsea]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: Pre-ranked gene-set enrichment analysis (GSEA 34 ; https://www.gsea-msigdb.org/gsea ) was then performed, using the R package fgsea 35 (v1.20.0; https://github.com/ctlab/fgsea ; multilevel implementation with 10000 initial permutations and no lower bound for p-value estimation), for each of the 3 comparisons of interest, based on the ranking metric TRM, and considering a collection of 3065 mouse g...
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Engineered extrachromosomal oncogene amplifications promote tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08318-8 | PMCID: PMC11754114 | PMID: 39695225
- Evidence: Enrichment was calculated using the fgsea R package.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, R, STAR] -> quantification [MACS2 v3.0.0b, deepTools v3.5.3] -> differential/statistical testing [DESeq2, R, STAR] -> stage not stated [CNVkit v0.9.10, fgsea]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Version used: **1.22.0**
- Evidence: Differential gene expression analysis on raw counts was performed using DESeq2, over-representation analysis with clusterProfiler v.4.4.4 and gene set enrichment analysis with fgsea v.1.22.0.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **1.30.0**
- Evidence: GSEA was implemented using the fgsea (v1.30.0) package against curated gene sets from the MSigDB, including the Reactome, KEGG and Hallmark collections.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Version used: **1.25.1**
- Evidence: Finally, we subjected the resulting SE-specific ranked lists to fgsea (v.1.25.1) 114 , testing the enrichments of SE-specific consensus genes (Extended Data Fig.
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Evidence: GSEA was performed using the fgsea package with pre-ranked gene lists from the MsigDBR package, including Hallmark, KEGG, Reactome, WIKIPATHWAYS and a customized set of ontologies found from the literature.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **1.30.0**
- Evidence: We used the R package fgsea (v.1.30.0) 71 to calculate the normalized enrichment statistics for each gene set in the Hallmark Collection from the Molecular Signatures Database 72 . qPCR of incorporated dsODN for off-target double-strand-break detection Detection of dsDNA breaks by qPCR of integrated donor oligos (dsODN) is adapted from the GUIDE-Seq method as described previously 73 .
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: For gene set enrichment analysis (GSEA), two methods were applied: preranked GSEA (fgsea 67 v.1.24.0) and single-sample GSEA (ssGSEA 68 implemented in GSVA v.1.46.0).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: GSEA was performed using the javaGSEA application (v4.2.3) 53 and FGSEA R package (v1.34.2; http://bioconductor.org/packages/fgsea/ ).
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: We performed GSEA with DEGs from a putative recent GC emigrant cluster using the fgsea package v.1.24.0.
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Evidence: Gene set enrichment analysis 47 was performed using the log 2 FC ranking of differentially expressed genes using fgsea.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Dynamic antigen expression and cytotoxic T cell resistance in HIV reservoir clones. (Nature 2026)

- DOI: 10.1038/s41586-026-10298-w | PMCID: PMC13190302 | PMID: 41735521
- Evidence: Gene set enrichment analysis was performed using fgsea::fgseaMultilevel() with genes ranked by DESeq2 Wald statistic.
- Full pipeline: normalisation [Seurat v5.1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> visualisation [limma] -> stage not stated [MACS2]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Version used: **1.20.0**
- Evidence: GSEA was performed using fgsea 1.20.0 46 R package on MSigDB v.7.5.1 47 KEGG canonical pathways.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: GSEA was run on metafor analysis output to determine enriched pathways using the fgsea package (v.1.3.0).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Version used: **1.28.0**
- Evidence: All over-representation and gene set enrichment analyses shown were performed with fgsea v.1.28.0.
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **1.30.0**
- Evidence: To detect enrichment of PB-T RM gene signature, we performed GSEA using the differential expression results with the fgsea (v.1.30.0) library in R (v.4.4.1) 48 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### AGO2 promotes tumor progression in KRAS-driven mouse models of non-small cell lung cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2026104118 | PMCID: PMC8157917 | PMID: 33972443
- Evidence: Finally, the fgsea package was used to perform gene set analysis using estimated log-fold change from differential analysis as input.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> differential/statistical testing [fgsea, limma] -> stage not stated [GSEA]

### Identification of EMT signaling cross-talk and gene regulatory networks by single-cell RNA sequencing. (PNAS 2021)

- DOI: 10.1073/pnas.2102050118 | PMCID: PMC8126782 | PMID: 33941680
- Evidence: For miRNA enrichment analysis, miRNAs and their target genes were obtained from the miR database mirWalk2.0 ( 34 ). miRNA enrichment was inferred based on the miRNA target expression in scRNA-seq data using the fgsea package (v1.16.0).
- Full pipeline: quality control [R, Seurat v3.1.0] -> normalisation [R, Seurat v3.1.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, Seurat v3.1.0, UMAP] -> stage not stated [GSVA, fgsea]

### CD20 as a gatekeeper of the resting state of human B cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021342118 | PMCID: PMC7896350 | PMID: 33563755
- Evidence: After RMA normalization, single-sample enrichment of PC differentiation up-regulated genes was performed using the fgsea R package ( 47 ) on the ranked after vs. before relapse log FC.
- Full pipeline: normalisation [fgsea] -> differential/statistical testing [R, limma] -> stage not stated [CellProfiler v3.0.0, GSEA]

### Biosensors for inflammation as a strategy to engineer regulatory T cells for cell therapy. (PNAS 2022)

- DOI: 10.1073/pnas.2208436119 | PMCID: PMC9546553 | PMID: 36161919
- Evidence: Gene set enrichment analysis was performed using fgsea .
- Full pipeline: quality control [DESeq2] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [fgsea, ggplot2]

### Comparative genomics of mortal and immortal cnidarians unveils novel keys behind rejuvenation. (PNAS 2022)

- DOI: 10.1073/pnas.2118763119 | PMCID: PMC9459311 | PMID: 36037356
- Evidence: GSEA was performed with the fgsea ( 48 ) package, after adapting the human Molecular Signatures Database (MSigDB) ( 49 ) to the genome of T. dohrnii .
- Full pipeline: alignment/mapping [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [AlphaFold v2.1.2, BUSCO, ChimeraX, GSEA, fgsea]

### Activating STING1-dependent immune signaling in <i>TP53</i> mutant and wild-type acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2123227119 | PMCID: PMC9271208 | PMID: 35759659
- Evidence: Microarray derived log2 fold change values were preranked prior to running fgsea ( 79 ) using Hallmarks pathways as contained in MSigDB ( 80 ).
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [ggpubr] -> stage not stated [GSEA, R, STRING db, fgsea]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: Using the ranked covariate output, fGSEA (fast preranked gene set enrichment analysis) analysis was performed using the R package fgsea.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### Hatching is modulated by microRNA-378a-3p derived from extracellular vesicles secreted by blastocysts. (PNAS 2022)

- DOI: 10.1073/pnas.2122708119 | PMCID: PMC8944274 | PMID: 35298333
- Evidence: To gain further biological insight into these results, a classical overrepresentation analysis based on a hypergeometric test was applied in the R package fgsea ( 83 ).
- Full pipeline: differential/statistical testing [DESeq2, R v4.0.3] -> stage not stated [fgsea]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: GSEA was performed using the R package ‘fgsea’ using a concatenation of all three gene ontology databases (GO:BP, GO:MF, GO:CC) downloaded from MSigDB ( http://www.gsea-msigdb.org ).
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: RNA-seq analyses were performed using Seq2Pathway, fgsea, tidyverse, and dplyr software packages.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Tumor progression is independent of tumor-associated macrophages in cell lineage-based mouse models of glioblastoma. (PNAS 2023)

- DOI: 10.1073/pnas.2222084120 | PMCID: PMC10120014 | PMID: 37040416
- Evidence: The R package fgsea was used for this analysis.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, fgsea]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Version used: **1.8.0**
- Evidence: The Gene Set Enrichment Analysis was performed with fgsea (v1.8.0) and Hallmark gene sets from MSigDB (v6.2).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: Gene ontology over-representation and gene set enrichment analysis (GSEA) were conducted using the clusterProfiler package ( 29 ) with a GO level of 3 and fgsea package ( 30 ) with the Reactome database, respectively.
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Sec22b is a critical and nonredundant regulator of plasma cell maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2213056120 | PMCID: PMC9926242 | PMID: 36595686
- Evidence: GSEA was performed by the clusterProfiler::GSEA function using the fgsea algorithm.
- Full pipeline: read trimming [Bioconductor, edgeR] -> alignment/mapping [Bioconductor, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [GSEA, clusterProfiler, fgsea] -> differential/statistical testing [Bioconductor, R, edgeR, limma]

### Enhanced pathogenicity of Th17 cells due to natalizumab treatment: Implications for MS disease rebound. (PNAS 2023)

- DOI: 10.1073/pnas.2209944120 | PMCID: PMC9910615 | PMID: 36574650
- Evidence: The GSEA was done using the R-package fgsea ( 52 ).
- Full pipeline: stage not stated [GSEA, fgsea, tidyverse]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: Pathway analysis/GSEA was performed using clusterProfiler (60) or fgsea.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### A sensitive assay for measuring whole-blood responses to type I IFNs. (PNAS 2024)

- DOI: 10.1073/pnas.2402983121 | PMCID: PMC11459193 | PMID: 39312669
- Evidence: The ensemble ID targeting multiple genes was collapsed (average) and a final gene data matrix was used for a modular repertoire analysis, as previously described ( 103 ) or for geneset enrichment analysis (GSEA: fgsea) with hallmark gene sets ( http://www.gsea-msigdb.org/ ). scRNAseq.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, fgsea]

### Alloreactive memory CD4 T cells promote transplant rejection by engaging DCs to induce innate inflammation and CD8 T cell priming. (PNAS 2024)

- DOI: 10.1073/pnas.2401658121 | PMCID: PMC11348247 | PMID: 39136987
- Evidence: The fgsea R package ( 10.1101/060012 ) was used for further gene enrichment analysis using the Hallmark geneset.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2, limma] -> differential/statistical testing [DESeq2, R] -> visualisation [limma] -> stage not stated [fgsea]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: The R package fgsea (Version 1.27.0) ( 53 ) provided the over-representation analysis (ORA) hypergeometric test used to determine overenrichment of genes represented in the list of peaks with increased accessibility in each experimental treatment compared to a second background, “gene universe” list of all consensus peaks detected, similarly filtered as in step one to include only one instance of ...
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: For GSEA, we applied fgsea package, implemented in R, to the sorted gene fold-changes generated by FindMarkers function from Seurat.
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Evidence: Differential expression analysis was carried out with DeSeq2 (v1.34.0) ( 56 ) Differentially expressed genes (adjusted P value < 0.1) were subjected to gene set enrichment analysis using the fgsea package (version 1.16.0).
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### Macrophage transplantation rescues RNASET2-deficient leukodystrophy by replacing deficient microglia in a zebrafish model. (PNAS 2024)

- DOI: 10.1073/pnas.2321496121 | PMCID: PMC11126979 | PMID: 38753517
- Version used: **1.28.0**
- Evidence: The ranked list of genes was then used for a GSEA using the package fgsea v1.28.0 and the results were plotted using the package ggplot2 v3.4.4. in R v4.3.2.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [R v4.3, fgsea v1.28.0, ggplot2 v3.4.4] -> stage not stated [HTSeq v2.0]

### Species-wide quantitative transcriptomes and proteomes reveal distinct genetic control of gene expression variation in yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2319211121 | PMCID: PMC11087752 | PMID: 38696467
- Evidence: Based on the CV, we performed a functional exploration by gene set enrichment analysis (GSEA) ( 75 ) using the fgsea R package ( 76 ) for the gene ontology annotation ( 77 , 78 ) to detect cellular pathways with a conserved regulation across the population.
- Full pipeline: quantification [R, WGCNA] -> normalisation [WGCNA] -> stage not stated [GSEA, fgsea]

### Isotype switching in human memory B cells sets intrinsic antigen-affinity thresholds that dictate antigen-driven fates. (PNAS 2024)

- DOI: 10.1073/pnas.2313672121 | PMCID: PMC10990115 | PMID: 38502693
- Evidence: GSEA was run with a custom function based on the fgseaMultilevel function from the fgsea package ( https://github.com/TranLab/ModuleLists ) that includes MSigDB gene collections as well as blood transcription modules ( 63 ) and other gene sets relevant to immunology and blood transcriptomics ( 64 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, GSEA, R, fgsea]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Version used: **1.26.0**
- Evidence: Gene set enrichment analysis between conditions was performed by fgsea v.1.26.0 on hallmark gene signature obtained from Molecular Signature Database and tumor transcriptional metaprograms from Gavish et al.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### Antibiotic-induced microbiota depletion impairs the proregenerative response to a biological scaffold. (PNAS 2025)

- DOI: 10.1073/pnas.2510841122 | PMCID: PMC12772165 | PMID: 41428865
- Version used: **1.28.0**
- Evidence: GSEA was performed with fgsea v1.28.0, ranking results by the product of logFC and −log10(padj), using REACTOME and HALLMARK pathways.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.42.0] -> stage not stated [GSEA, fgsea v1.28.0]

### Galectin-9 binding to HLA-DR in dendritic cells controls immune synapse formation and T cell proliferation. (PNAS 2025)

- DOI: 10.1073/pnas.2501381122 | PMCID: PMC12718305 | PMID: 41359845
- Evidence: The average fold change was then used as input for the R package fgsea ( 57 ).
- Full pipeline: alignment/mapping [STAR] -> normalisation [DESeq2, R] -> differential/statistical testing [Fiji, ImageJ] -> stage not stated [GSEA, fgsea]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: Gene set enrichment analysis was performed using the fgsea package ( 63 ) in R to identify significantly enriched gene sets.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Glycoside hydrolase-mediated glucomannan catabolism in &lt;i&gt;Segatella copri&lt;/i&gt;, a target of microbiota-directed foods for malnourished children. (PNAS 2025)

- DOI: 10.1073/pnas.2521522122 | PMCID: PMC12704710 | PMID: 41329729
- Evidence: 38 ) or gene sets (fgsea, ref.
- Full pipeline: quality control [DESeq2, kallisto] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [AlphaFold, GSEA, fgsea]

### Cell-type-informed genotyping of mosaic focal epilepsies reveals cell-autonomous and non-cell-autonomous disease-associated transcriptional programs. (PNAS 2025)

- DOI: 10.1073/pnas.2509622122 | PMCID: PMC12305027 | PMID: 40674414
- Version used: **1.28.0**
- Evidence: Gene set enrichment analysis was performed with fgsea (v1.28.0) ( 35 ), with genes ranked in descending order by average log2 fold-change.
- Full pipeline: normalisation [Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [CellChat, fgsea v1.28.0]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: We performed gene set enrichment analysis using the H hallmark gene sets and the R package fgsea.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: Enrichment of Hallmark gene sets downloaded from MSigDB ( 30 ) was examined with fgsea ( 31 ) using genes ranked by logFC estimated from limma as input.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### Shared host genetic landscape of respiratory viral infection. (PNAS 2025)

- DOI: 10.1073/pnas.2414202122 | PMCID: PMC12107129 | PMID: 40372436
- Evidence: These normalized scores were also used to profile the functional annotation of highly ranked proviral genes in each screen via gene set enrichment analysis (R:4.1.0, fgsea:1.20.0) using the KEGG (msigdbr:7.5.1) and CORUM annotation (28.11.2022 Corum 4.1 release).
- Full pipeline: normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Murine gut microbiota dysbiosis via enteric infection modulates the foreign body response to a distal biomaterial implant. (PNAS 2025)

- DOI: 10.1073/pnas.2422169122 | PMCID: PMC12107164 | PMID: 40354538
- Evidence: Rank based gene set enrichment analysis for the REACTOME pathways gene sets were performed using the fgsea package ( 83 ), where differential gene expression results were ranked by logFC*-log10( P adj ).
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, fgsea]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Evidence: Analysis was performed using DESeq2 (v1.34.0), fgsea, and ranked gene lists.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Version used: **1.30.0**
- Evidence: Gene set enrichment analysis was performed with the R package fgsea (v1.30.0) and the gene sets were imported with msigdbr (v7.5.1).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Fast gene set enrichment analysis (fgsea) ( 53 ) was applied to the ranked gene lists to compute normalized enrichment scores (NES) and adjusted p-values (Benjamini–Hochberg) for MSigDB Hallmark gene sets (H) ( 54 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### Differential disease tolerance mediates sex-biased illness severity in sepsis. (PNAS 2026)

- DOI: 10.1073/pnas.2522764123 | PMCID: PMC12956862 | PMID: 41734079
- Version used: **1.34.0**
- Evidence: KEGG pathway enrichment analysis was conducted using cluterProfiler (v4.16.0), and GSEA was conducted using fgsea (v1.34.0).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [GSEA, MACS2, R v4.5.0, fgsea v1.34.0]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: GSEA was conducted with the fgsea package, by projecting the ranking of fold-change in expression onto the Hallmark gene sets ( 71 ).
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: GSEA analysis and corresponding heatmaps and figures were created using R package fgsea (vfgsea_1.24.0), ComplexHeatmap, and ggplot2 for signatures from MSigDB’s hallmark MTORC1 and custom AR signatures based on our data ( 53 – 55 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: Geneset enrichment analysis (GSEA) was conducted with the fgsea package in R.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Evidence: Gene set enrichment analysis was performed using the fGSEA package ( https://github.com/ctlab/fgsea/ ) using the 2024 Hallmark gene sets.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

