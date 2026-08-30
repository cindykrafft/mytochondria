# limma

- **Category:** genomics
- **Papers in survey:** 234
- **Journals:** Nature (115), PNAS (97), Cell (17), Science (4), NEJM (1)
- **Years:** 2021 (22), 2022 (31), 2023 (46), 2024 (36), 2025 (65), 2026 (34)
- **Versions named:** 3.46.0 (6), 3.58.1 (5), 3.34.9 (3), 3.48.3 (3), 3.62.2 (2), 3.60.6 (2), 3.54.2 (2), 3.38.3 (2), 3.60.2 (2), 3.50.0 (2)
- **Pipeline stages it appears in:** differential/statistical testing (143), normalisation (62), quantification (15), dimensionality reduction/clustering (12), visualisation (5), read trimming (3), alignment/mapping (3), variant calling (2), simulation/modelling (2), quality control (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: Differential abundance was performed using a within-individual paired sample design in limma in R ( Ritchie et al., 2015 ).
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **3.43.11**
- Evidence: DMLs and DMRs were identified via the R Package DMRCate (version 2.2.3) using limma (version 3.43.11) ( Peters et al., 2015 ; Ritchie et al., 2015 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...ad NA Cutadapt Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ Limma Ritchie et al., 2015 https://bioconductor.org/packages/release/bioc/html/limma.html clusterProfiler Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html Resource availability Lead contact Further information and requests for reagents may be directed to and will be fulfilled by Lead Cont...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Human neutralizing antibodies against SARS-CoV-2 require intact Fc effector functions for optimal therapeutic protection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.026 | PMCID: PMC7879018 | PMID: 33691139
- Evidence: ...sm GraphPad v 9.0.0 Biorender biorender.com N/A flexiWare SCIREQ Inc. v8.1.3 STAR program Dobin et al., 2013 v 2.5.1a EdgeR Robinson et al., 2010 N/A limma Ritchie et al., 2015 N/A RSeQC Liao et al., 2014 v2.6.2 Nanozoomer Digital Pathology Hamamatsu v2 Recombinant DNA Plasmid: rCOV2-2050 in pTwist-mCis_hG1 Zost et al., 2020b N/A Plasmid: rCOV2-2050 in pTwist-mCis_hG1 LALA-PG This study N/A Plasmi...
- Full pipeline: quality control [edgeR, limma] -> read trimming [R] -> normalisation [R]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: ...ges/release/bioc/html/flowWorkspace.html Limma (versions 3.40.2, 3.42.2) Ritchie et al., 2015 https://www.bioconductor.org/packages/release/bioc/html/limma.html Tidyverse (1.2.1, 1.3.0) ( Wickham, 2019 ) https://www.tidyverse.org ComplexHeatmap (2.2.0) Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html edgeR (3.26.8, 3.28.1) McCarthy et al., 2012 https://biocon...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Evidence: The differential analysis used the proteusLabelFree package (Version 0.1.6; Gierlinski et al., 2018 ) which is based on limma ( Smyth, 2004 ).
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: ...M-BC 1.4.0 Lin and Peddada, 2020 https://github.com/FrederickHuangLin/ANCOMBC decontam 1.14.0 Davis et al., 2018 https://github.com/benjjneb/decontam limma-voom 3.50.0 Law et al., 2014 https://bioconductor.org/packages/release/bioc/html/limma.html snm 1.42.0 Mecham et al., 2010 https://www.bioconductor.org/packages/release/bioc/html/snm.html MATLAB version 2019b with the Statistics and Machine Lea...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...ctrepo.com/project/scikit-tda-kepler-mapper-python-data-validation Limma ( Ritchie et al., 2015 ) https://bioconductor.org/packages/release/bioc/html/limma.html MATLAB https://uk.mathworks.com/help/matlab/ Matplotlib ( Hunter, 2007 ) https://matplotlib.org/ MSFragger ( Kong et al., 2017 ) v3.0 MSigDB ( Subramanian et al., 2005 ) https://www.gsea-msigdb.org/gsea/msigdb/index.jsp Pandas v1.2.4 https...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Evidence: Differentially expressed genes were identified with linear modeling using limma (FDR ≤0.05; absolute logFC ≥1) after correcting for multiple testing using Benjamini-Hochberg.
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### Arginine reprograms metabolism in liver cancer via RBM39. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.011 | PMCID: PMC10642370 | PMID: 37804830
- Evidence: The function <limma_ASE> was used with default settings to generate statistics for differential ASE (Alternative Splice Elements) analysis with a stringent cut-off (-Log 10 p = 4).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ, R] -> normalisation [RSEM] -> differential/statistical testing [STAR, limma]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: Raw TMT reporter ion signals (signal_sum columns) were first cleaned for batch effects using limma 105 and further normalized using vsn (variance stabilization normalization 106 ).
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: 105 https://bioconductor.org/packages/clusterProfiler/ topGO R package Alexa and Rahnenfuhrer 106 https://bioconductor.org/packages/topGO/ limma R package Ritchie et al.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: 95 https://bioconductor.org/packages/release/bioc/html/vsn.html limma Ritchie et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Molecular and cellular mechanisms of teneurin signaling in synaptic partner matching. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.022 | PMCID: PMC11833509 | PMID: 38996528
- Evidence: The linear model along with the associated moderated t-test and BH-FDR correction were implemented using the limma library 131 in R.
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [STRING db] -> differential/statistical testing [limma] -> visualisation [R] -> stage not stated [ImageJ]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 50 https://bioconductor.org/packages/release/bioc/html/limma.html pheatmap R Kolde 51 https://www.rdocumentation.org/packages/pheatmap/versions/1.0.12/topics/pheatmap Prism 10 GraphPad software https://www.graphpad.com/scientific-software/prism RSEM tool Li and Dewey 52 https://deweylab.github.io/RSEM/ scVelo Bergen et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: Next, we interrogated the differential expression of proteins between any two of the three groups using the moderated t-test implemented in the limma package.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **3.60.6**
- Evidence: 223 https://itol.embl.de/ limma (v3.60.6) Ritchie et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### A Microbiota-Directed Food Intervention for Undernourished Children. (NEJM 2021)

- DOI: 10.1056/nejmoa2023294 | PMCID: PMC7993600 | PMID: 33826814
- Evidence: Changes in plasma protein abundances were analyzed using an Empirical Bayes linear model framework [limma( 12 )] and gene set enrichment analysis [GSEA( 13 )], a method for quantifying whether a rank-ordered list of features (e.g., proteins ranked by their changes in abundances after a treatment or by correlation coefficient) are enriched for a subset of features of interest (e.g., a biological pa...
- Full pipeline: quantification [GSEA, limma] -> differential/statistical testing [GSEA, limma]

### Spatially resolved cell atlas of the mouse primary motor cortex by MERFISH. (Nature 2021)

- DOI: 10.1038/s41586-021-03705-x | PMCID: PMC8494645 | PMID: 34616063
- Evidence: P values were calculated using the analysis of variance (ANOVA) test in limma 47 on log-transformed data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Scanpy, scDblFinder]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **3.38.3**
- Evidence: The clustering pipeline is implemented in the R package scrattch.hicat v0.0.22 (RRID SCR_018099), with marker genes defined using the limma v3.38.3 package; the clustering method is provided by the ‘run_consensus_clust’ function ( https://github.com/AllenInstitute/scrattch.hicat ).
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: The DGE test was performed using a linear model implemented in the package limma 73 (v.3.46.0), using 10% FDR, and aggregating expression profiles by sample(implemented in the function findNhoodGroupMarkers of the miloR package, with option aggregateSamples = TRUE).
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Lipid signalling enforces functional specialization of T<sub>reg</sub> cells in tumours. (Nature 2021)

- DOI: 10.1038/s41586-021-03235-6 | PMCID: PMC8168716 | PMID: 33627871
- Version used: **3.34.9**
- Evidence: For microarray analyses 43 , the expression signals were summarized using the robust multi-array average algorithm (Affymetrix Expression Console v1.1), followed by differential expression (DE) analysis performed using R package limma v.3.34.9.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, limma v3.34.9] -> visualisation [UMAP] -> stage not stated [GSEA, Seurat, ggplot2 v2.2.1]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Differential expression analysis was then applied using limma package 74 to define differentially expressed genes (DEGs) between PDAC vs normal samples, using > 2-fold change and adjusted p-value < 0.05 cut-off.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Evidence: The limma-voom R package was used to normalize gene expression levels and perform differential expression analysis.
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Arterialization requires the timely suppression of cell growth. (Nature 2021)

- DOI: 10.1038/s41586-020-3018-x | PMCID: PMC7116692 | PMID: 33299176
- Version used: **3.32.10**
- Evidence: Expression count matrices were then processed with an analysis pipeline that used the bioconductor package limma v.3.32.10 37 for normalization (using the TMM method) and differential expression testing; matrix processing considered only genes expressed with at least 1 count per million (CPM) in at least as many samples as the condition with the least number of replicates.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5] -> alignment/mapping [RSEM v1.2.30] -> normalisation [limma v3.32.10] -> differential/statistical testing [limma v3.32.10] -> stage not stated [GSEA, ImageJ]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Evidence: Differential expression analysis of Emp1-high vs -low data was performed using a linear model with empirical shrinkage (limma R package) 58 , taking into account the paired data setting.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: The counts for the remaining genes (24,836) and transcripts (99,819) passing these filters were normalized using the limma-trend approach in the limma 53 R package.
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### Antibody targeting of E3 ubiquitin ligases for receptor degradation. (Nature 2022)

- DOI: 10.1038/s41586-022-05235-6 | PMCID: PMC9534761 | PMID: 36131013
- Evidence: Subsequently, differential expression analysis on the normalized count data was performed using the limma R package 27 .
- Full pipeline: quantification [Bioconductor, R] -> normalisation [R, limma] -> differential/statistical testing [Bioconductor, limma]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: Read counts were converted to log 2 -CPM, quantile normalized and precision weighted with the voom function of the limma package 53 , 54 after accounting for batch effects.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Truncated FGFR2 is a clinically actionable oncogene in multiple cancers. (Nature 2022)

- DOI: 10.1038/s41586-022-05066-5 | PMCID: PMC9436779 | PMID: 35948633
- Version used: **3.52.1**
- Evidence: The R package limma (v.3.52.1) 81 was used to perform differential expression analysis on class 1 phosphosite intensity data.
- Full pipeline: read trimming [edgeR v3.26.6] -> alignment/mapping [BWA v0.7.5a, STAR v2.7.2] -> quantification [RSEM v1.3.0, edgeR v3.26.6, featureCounts v1.6.2] -> normalisation [edgeR v3.26.6] -> differential/statistical testing [R, limma v3.52.1]

### Mechanism of mitoribosomal small subunit biogenesis and preinitiation. (Nature 2022)

- DOI: 10.1038/s41586-022-04795-x | PMCID: PMC9200640 | PMID: 35676484
- Version used: **3.34.9**
- Evidence: Differential expression analysis was performed using limma, version 3.34.9 (ref.
- Full pipeline: registration [RELION v3.0] -> differential/statistical testing [limma v3.34.9] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4 v7.0, ChimeraX v0.91]

### TLR7 gain-of-function genetic variation causes human lupus. (Nature 2022)

- DOI: 10.1038/s41586-022-04642-z | PMCID: PMC9095492 | PMID: 35477763
- Evidence: Sequencing was performed using the NextSeq500 platform and analysis was conducted using the following R packages: limma, edgeR and enhanced volcano 49 .
- Full pipeline: dimensionality reduction/clustering [Seurat v4.0.1] -> differential/statistical testing [R, Seurat v4.0.1] -> visualisation [Seurat v4.0.1] -> stage not stated [edgeR, limma]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: Significant immune features between all twins with MS and unaffected twin siblings were extracted using the moderated limma-trend method implemented in diffcyt, applying a false discovery correction according to the Benjamini–Hochberg approach 57 .
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Evidence: Finally, we removed the effect of sequencing batch on estimated logCPM values with TMM normalization for the discovery cohort using the limma-voom function, removeBatchEffect. log 2 -transformed fold change and CV estimation We define log 2 -transformed fold-change (﻿log 2 (FC)) as the difference between the median gene level (logCPM; see ‘Bioinformatic processing’) between preeclampsia and normot...
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### The cGAS-STING pathway drives type I IFN immunopathology in COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04421-w | PMCID: PMC8891013 | PMID: 35045565
- Version used: **3.40.6**
- Evidence: Differential protein expression analysis was performed using the R bioconductor package limma (v.3.40.6, 2020-02-29) 55 , followed by the Benjamini–Hochberg multiple-testing method 56 .
- Full pipeline: quantification [ImageJ] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [limma v3.40.6] -> stage not stated [Bioconductor]

### A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06812-z | PMCID: PMC10719114 | PMID: 38092916
- Evidence: In our original scrattch.hicat package, we applied limma package 133 to perform this analysis.
- Full pipeline: quantification [UMAP] -> normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [Cellpose, Jupyter, WGCNA, limma, scDblFinder]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **3.48.3**
- Evidence: Differential expression analysis of genes was performed using the lmFit method implemented in the R package limma (v.3.48.3) 79 .
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Evidence: Differential expression was performed on adjusted counts between vehicle-treated and drug-treated samples using the limma method, with dose as the continuous covariate and blocking on donor.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### A spatially resolved timeline of the human maternal-fetal interface. (Nature 2023)

- DOI: 10.1038/s41586-023-06298-9 | PMCID: PMC10356615 | PMID: 37468587
- Evidence: DEGs in EVTs DEGs between intravascular and interstitial EVTs were identified using the Bioconductor package limma 65 (linear models for microarray data) after consulting with the NanoString statistics team.
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [limma, scikit-learn] -> stage not stated [ImageJ, Jupyter, Python, QuPath v0.4.0, R]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: Enrichment of KEGG pathways in these clusters of genes was determined using the limma function kegga 88 , and the resulting unadjusted P values are plotted in Extended Data Fig.
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **3.46.0**
- Evidence: For microarray analysis, the gene expression probe signals were quantile-normalized and summarized by the RMA algorithm by Affymetrix Expression Console (version 1.4.1), then the differential gene expression analysis was performed by R package limma (version 3.46.0).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Outer membrane utilisomes mediate glycan uptake in gut Bacteroidetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06146-w | PMCID: PMC7618045 | PMID: 37286596
- Evidence: Statistical analysis was performed using limma 43 and the Benjamini-Hochberg correction for multiple hypothesis testing was implemented.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, CCP4, ChimeraX, PHENIX, R v4.1.1, RELION]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: The count data matrix was then processed by using limma and edgeR in R/Bioconductor, as described.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Version used: **3.46.0**
- Evidence: Differential expression analyses were conducted using limma (v.3.46.0) 37 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Uridine-derived ribose fuels glucose-restricted pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06073-w | PMCID: PMC10232363 | PMID: 37198494
- Evidence: Differential gene expression between PDA and non-tumours were performed in R using the limma package (version 3.38.3).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5.2, limma] -> visualisation [ComplexHeatmap, ggplot2 v3.3.5, tidyverse v0.8.3] -> stage not stated [GSEA v4.0.3]

### Profiling the human intestinal environment under physiological conditions. (Nature 2023)

- DOI: 10.1038/s41586-023-05989-7 | PMCID: PMC10191855 | PMID: 37165188
- Version used: **3.48.3**
- Evidence: Statistical analysis was performed with limma (v.3.48.3) and a moderated t -test with FDR adjustment for multiple-hypothesis testing.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DADA2, DESeq2, R, limma v3.48.3] -> stage not stated [Bowtie2 v2.4.1, HMMER, phyloseq]

### A druggable copper-signalling pathway that drives inflammation. (Nature 2023)

- DOI: 10.1038/s41586-023-06017-4 | PMCID: PMC10131557 | PMID: 37100912
- Evidence: Differential expression was assessed with the limma/voom framework (v 3.44.3) 79 .
- Full pipeline: quality control [Nextflow] -> normalisation [R, deepTools, edgeR v3.30.3] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, limma]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Version used: **3.54**
- Evidence: Statistical analysis of differentially expressed proteins was done using the Bioconductor package limma (v.3.54).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **3.50.3**
- Evidence: Transcriptional data analyses Gene level transcription analysis used edgeR (v3.36.0) 47 and limma (v3.50.3) 48 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: Expression differences were performed at the region level through the limma-voom analytical pipeline, taking tumour as a blocking factor, by performing within-tumour expression correlations and including them within the voom model estimate using the duplicateCorrelation() function.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Version used: **3.46.0**
- Evidence: Differential gene expression analysis Differential gene expression analysis was performed with limma (limma version 3.46.0, edgeR version 3.32.1) with “cell_or_nucleus” covariate (scRNA-seq or snRNA-seq (including multiome snRNA-seq) origin of each droplet) backwards along the trajectory that was derived using stOrder approach, namely for the following 6 comparisons: VCT-CCC vs VCT (VCT and VCT-p ...
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### RHOJ controls EMT-associated resistance to chemotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05838-7 | PMCID: PMC10076223 | PMID: 36949199
- Evidence: To compare protein abundance between pairs of sample groups (RhoJHAuntreatedIP versus EVuntreatedIP, RhoJHAtreated12hchemoIP versus EVtreated12hchemoIP sample groups), statistical testing for differences between two group means was performed, using the package limma 65 .
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [limma] -> normalisation [HTSeq] -> differential/statistical testing [limma] -> stage not stated [CellProfiler v3.1.9, ImageJ]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: A protein was considered to be an interactor if in one or both comparisons its levels were statistically significantly different ( Q ≤ 0.05, limma test, with P values adjusted by the Storey method) and at least twice higher in IP reactions than in the corresponding IG control (Supplementary Table 3 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: The R (3.6.1) package EdgeR 61 (edgeR_3.28.1;limma_3.42.2) was used to identify proteins significantly enriched in NPAS4 or TIP60 immunoprecipitate samples relative to wild-type samples that did not express Flag-tagged proteins.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: We found that B2M was among the most significantly downregulated genes in B2M MUT cancers (two-sided limma-voom-based regression, P = 3.5 × 10 −4 , Benjamini–Hochberg false-discovery rate (FDR)-adjusted P = 0.12, adjusted for tumour type; Fig.
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: The resulting count matrix was then further analysed using the limma package for R (v.4.1.1).
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Evidence: Gene Ontology analysis Enriched terms in the Gene Ontology 32 analyses of genes with conserved and diverged expression trajectories were identified using the goana function of the limma R package, v.3.40.6 (default parameters).
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: For P values, limma’s 84 rankSumTestWithCorrelation (the default for Seurat’s FindMarkers; two-sided Wilcoxon–Mann–Whitney) was used with downsampled, log-transformed single-cell data as input.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: As a result, our analyses were performed by first computing cell-type-specific pseudobulk profiles for each sample and then analysing pseudobulk RNA-seq profiles using limma 62 .
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Evidence: Potential batch effects were removed using the limma package.
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07752-y | PMCID: PMC11291290 | PMID: 39048822
- Evidence: Subsequently, we conducted a rigorous analysis of differential gene expression using the limma package on normalized count data obtained from publicly available datasets.
- Full pipeline: normalisation [DESeq2 v1.30.1, limma] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [limma] -> stage not stated [R, Seurat, fgsea]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: The ‘limma’ R package was applied to the plasma proteomic, EVP proteomic and metabolite data (v3.52).
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Differential expression analysis was performed in R using limma 77 with voom transformation and including donor as a covariate.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### GLP-1-directed NMDA receptor antagonism for obesity treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07419-8 | PMCID: PMC11136670 | PMID: 38750368
- Version used: **3.54.2**
- Evidence: For differential expression analysis, the R package limma (v.3.54.2) was used to identify differentially expressed proteins.
- Full pipeline: differential/statistical testing [DESeq2 v1.30.1, R, limma v3.54.2] -> stage not stated [LDSC, MAGMA]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Version used: **3.54.0**
- Evidence: Differential expression analyses were performed using the limma (v3.54.0).
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: The enrichment of BMP2-induced peaks over constitutive peaks was analysed by using default settings in the voom–limma analysis software packages 63 .
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: To correct for batch effects by donor, the removeBatchEffect function in the limma package was used.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### CGRP sensory neurons promote tissue healing via neutrophils and macrophages. (Nature 2024)

- DOI: 10.1038/s41586-024-07237-y | PMCID: PMC11023938 | PMID: 38538784
- Evidence: Differential gene expression analysis was performed using limma/voom 68 in Degust and genes with a FDR-adjusted P value < 0.05 were considered significantly upregulated or downregulated.
- Full pipeline: quality control [featureCounts] -> alignment/mapping [STAR] -> quantification [featureCounts] -> differential/statistical testing [limma]

### Decoding chromatin states by proteomic profiling of nucleosome readers. (Nature 2024)

- DOI: 10.1038/s41586-024-07141-5 | PMCID: PMC10954555 | PMID: 38448585
- Evidence: We used limma 60 to estimate the log 2 [FC] values between H3K4me3 and controls (H3 and H4), H3K4me1 and controls, and H3K4me3 and H3K4me1.
- Full pipeline: stage not stated [limma]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Differential protein expression and enrichment analysis was performed with the Bioconductor R package limma ( https://bioconductor.org/packages/release/bioc/html/limma.html ).
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Anti-TIGIT antibody improves PD-L1 blockade through myeloid and T&lt;sub&gt;reg&lt;/sub&gt; cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07121-9 | PMCID: PMC11139643 | PMID: 38418879
- Evidence: Low-quality protein levels were filtered on the basis of Q -values (cut-off, 0.01) and the batch-effect corrected using combat as described previously 44 . limma 45 was used to test for differences in log-scaled protein levels.
- Full pipeline: alignment/mapping [Bioconductor, R] -> quantification [Bioconductor, R] -> normalisation [Harmony v1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [fgsea] -> stage not stated [Seurat]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: For comparison of each IAA-treated condition to the mock-treated condition, statistical testing was conducted with limma, whereby differentially expressed proteins were selected using a log 2 [FC] cutoff of 1 and a P -value cutoff of 0.01, allowing one to reach a false discovery rate inferior to 5% according to the Benjamini–Hochberg estimator.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: For differential expression on the basis of carrier status, limma-voom 109 was run on donor-level pseudobulks with batch as a blocking factor and AD status as a grouping variable.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: We applied the limma package (implemented in scrattch.bigcat package) to perform this analysis.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### SARS-CoV-2 mRNA vaccines sensitize tumours to immune checkpoint blockade. (Nature 2025)

- DOI: 10.1038/s41586-025-09655-y | PMCID: PMC12611756 | PMID: 41125896
- Evidence: Statistical analysis was performed using R, in which we evaluated significance using a linear model with fixed effects based on the time from vaccine and controlling for patient ID (paired), including accommodation of biological variance between the baselines using the limma package’s duplicateCorrelation function.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Fiji, ImageJ, R]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Version used: **3.46.0**
- Evidence: Differential expression and gene set enrichment analysis Differential expression analysis was performed on the quality-controlled, filtered and normalized transcript counts using limma (3.46.0) 65 to fit a linear model for detecting statistically significant transcripts in RHOG -knockout compared with standard CAR T cells.
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Differential expression analysis between MYCN amplification status was performed using the Bioconductor package limma 66 (v.3.40.6).
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Differential expression analysis (edgeR, limma-voom) retained protein-coding genes expressed at ≥1 CPM in ≥1 sample, normalized counts and used linear modelling with empirical Bayes moderation with contrasts based on experimental conditions (treatment/genotype). fGSEA (10,000 permutations) of WikiPathways gene sets (Supplementary Table 3 ) was performed using ranked differentially expressed genes ...
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Version used: **3.58.1**
- Evidence: For RNA-seq DEG analysis, limma (v.3.58.1)/EdgeR (v.4.0.16) with a generalized linear model (GLM) F test was used, and the Benjamini–Hochberg procedure was used to adjust P values accounting for multiple testing.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Evidence: Differential expression analyses were performed with voom-limma 65 , after removal of lowly expressed genes and normalized using the trimmed mean of M -values method 66 , 67 .
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Evidence: 11g was performed using the top 500 genes with the largest s.d. of log-transformed FPKM (fragments per kilobase of transcript per million mapped fragments) values and these genes were subjected to PCA using the removeBatchEffect function in the limma package (v.3.58.1) and prcomp function of R software (v.4.3.3).
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Evidence: We performed differential gene expression analysis using the limma-trend pipeline v.3.50.1 (Supplementary Table 22 ).
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: Differential expression analysis was done using limma 72 with the voom method followed by GSEA as described above.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Version used: **3.52.3**
- Evidence: Differential expression analysis for microarray data was performed using limma (v3.52.3).
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **3.46.0**
- Evidence: The session used the following libraries: limma (3.46.0), edgeR (3.32.1), tximport (1.18.0), edgeR (3.32.1), sva (3.38.0), RColorBrewer (1.1-2), pheatmap (1.0.12), biomaRt (2.46.3), ggplot2 (3.3.3), gplots (3.1.1), ggfortify (0.4.11), NMF (0.23.0), cluster (2.1.1), fpc (2.2-9), plyr (1.8.6), dplyr (1.0.5), pvclust (2.2-0), ggrepel (0.9.1), amap (0.8-18), gProfileR (0.7.0), xtable (1.8-4), ggpubr (...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Evidence: Differential expression of genes between samples was assessed with voom 64 and limma with treat(., lfc = log2(1.2), robust = TRUE) 65 , 66 to generate the t -statistic.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Version used: **3.60.6**
- Evidence: Bulk RNA-seq analysis was performed using the edgeR (v.4.2.2) and limma (v.3.60.6) package workflows.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Evidence: Differential expression analysis was performed using GEO2R, with limma precision weights applied and the remaining options set to default 66 .
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Differential analysis was done using limma-voom 64 , 65 after TMM normalization 66 of gene level counts with calcNormFactors of edgeR 67 .
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **3.36.0**
- Evidence: For THP-1 RNA-seq analysis, RNA-seq analysis was conducted using the EdgeR (3.50.3) limma (3.36.0) workflow.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08885-4 | PMCID: PMC12158776 | PMID: 40240610
- Evidence: Statistical analyses were performed on proteins with at least 30% data completeness across samples, assuming normality using the limma package v.3.60.3 with two-sided moderated t -tests and ‘fdr’ as a multiple testing correction method.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, scikit-learn] -> differential/statistical testing [GSEA, limma] -> stage not stated [Cellpose v2.0, STRING db]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Evidence: These group comparisons (contrasts) were evaluated with a moderated Wald test with pooled variance (as implemented in the limma R package 77 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: Pairwise differentially expressed genes were identified as previously described 6 using the limma package 69 and selecting genes with at least a twofold change in expression and an adjusted P value of less than 0.01.
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### The P-loop NTPase RUVBL2 is a conserved clock component across eukaryotes. (Nature 2025)

- DOI: 10.1038/s41586-025-08797-3 | PMCID: PMC12178907 | PMID: 40140583
- Evidence: The differential analysis was done using the limma package (v.3.54.2) 58 , and the resulting volcano plots were created in R using ggplot2 (v.3.4.2). siRNA assay U2OS cells with the Per2-dLuc reporter were seeded at 8 × 10 5 cells in 35-mm dishes.
- Full pipeline: differential/statistical testing [ggplot2 v3.4.2, limma] -> stage not stated [ImageJ v1.53c]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **3.34.9**
- Evidence: The expression signals were analysed using Affymetrix Expression Console (v.1.4.1), followed by differential expression analysis performed using R package limma (v.3.34.9).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Each cell type was subset across all ages, then sample-pseudobulked ( n = 4 samples per age, except n = 2 at E16) and passed to the limma-voom pipeline 81 from the edgeR (RRID:SCR_012802) package 82 for differential expression analysis testing.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Evidence: Analysis of differentially expressed proteins Differentially expressed proteins were identified using an empirical Bayes-moderated t -test to compare treatment groups with the limma R package (v.3.54.2) 50 .
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Evidence: The protein ratio was calculated using the PD2.5 pairwise ratio-based algorithm and an empirical Bayes-moderated t -test was used to compare treatment groups using the limma R package (v.3.54.2) 55 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Version used: **3.58.1**
- Evidence: ...pbapply v.1.7-2, Matrix v.1.6-1.1, scUtils v.0.0.1, magrittr v.2.0.3, igraph v.1.5.1, treeio v.1.26.0, ggh4x v.0.2.6, scales v.1.2.1, edgeR v.4.0.16, limma v.3.58.1, ggtree v.3.10.1, lubridate v.1.9.3, forcats v.1.0.0, stringr v.1.5.0, dplyr v.1.1.3, purrr v.1.0.2, readr v.2.1.4, tidyr v.1.3.0, tibble v.3.2.1, ggplot2 v.3.4.4, tidyverse v.2.0.0, SeuratObject v.4.1.4, Seurat v.4.4.0, RcppAnnoy v.0....
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Synthetic lethality of mRNA quality control complexes in cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08398-6 | PMCID: PMC11864970 | PMID: 39910291
- Evidence: Counts were calculated using featureCounts from subread package and subsequently adjusted with TMM normalization and limma-voom transformation.
- Full pipeline: normalisation [featureCounts, limma] -> visualisation [PyMOL v1.7.6.6] -> stage not stated [fgsea]

### C-terminal amides mark proteins for degradation via SCF-FBXO31. (Nature 2025)

- DOI: 10.1038/s41586-024-08475-w | PMCID: PMC11821526 | PMID: 39880951
- Version used: **3.58.1**
- Evidence: Common contaminants 67 were removed and enrichment of interactors was calculated using limma v.3.58.1, by fitting a linear model to normalized spectral counts for each sample plus one pseudocount followed by empirical bayes moderation and Benjamini–Hochberg correction of P values for multiple-hypothesis testing.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [limma v3.58.1] -> differential/statistical testing [DESeq2, limma v3.58.1] -> visualisation [ChimeraX]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **3.18**
- Evidence: Filtration and statistical analysis were performed in the R programming by Biogenity using limma v.3.18 (ref.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **3.58.1**
- Evidence: Cell-type proportion analysis The investigation of variations in cell-type proportions across different age groups and brain regions was conducted using a linear model approach implemented in the R packages speckle (v.1.2.0) 56 and limma (v.3.58.1) 57 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: The resulting count data were subjected to TMM normalization using the function calcNormFactors in the package edgeR, followed by log transformation by the function voomWithQualityWeights in the package limma.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: Mean-variance trend was estimated with limma’s (v.3.50.3) voom function.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: Differential expression analysis was performed based on the provided RMA-normalized expression levels for these probes, using the R package limma 52 (v3.50.1) ( https://bioinf.wehi.edu.au/limma ), and comparing expression levels in 16 Lung samples vs 20 samples from all other metastatic sites available in the data set (5 Liver, 8 Bone, and 7 Brain samples, all considered together).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Neutralizing GDF-15 can overcome anti-PD-1 and anti-PD-L1 resistance in solid tumours. (Nature 2025)

- DOI: 10.1038/s41586-024-08305-z | PMCID: PMC11779642 | PMID: 39663448
- Evidence: Differential gene expression analyses were performed using the R/Bioconductor package limma (linear models for microarray and RNA-sequencing data) between visugromab treatment (day 14) and pretreatment (baseline) by applying a paired moderated t -test.
- Full pipeline: quantification [R] -> differential/statistical testing [Bioconductor, limma]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: To evaluate intragroup variability, module expression for each sample was calculated as the mean expression of all scaled log-transformed normalized counts (given by the edgeR cpm function, corrected for the percentage of ribosomal RNA using the limma function removeBatchEffect after log-transformation).
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Endogenous self-peptides guard immune privilege of the central nervous system. (Nature 2025)

- DOI: 10.1038/s41586-024-08279-y | PMCID: PMC11666455 | PMID: 39476864
- Evidence: After filtering, limma and edgeR were used to build a model and conduct differential expression testing with the lmFit, contrasts.fit and eBayes functions.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR, limma] -> stage not stated [Seurat]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Gene-level statistics were obtained using dataset-appropriate models: limma 254 (v3.60.0) for intervention and disease datasets, edgeR 240 (v4.2.0) for ITP cohort analyses, and linear mixed-effects models for aggregated meta-dataset signatures, as described in the corresponding sections.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: The original gene alias names were converted to the updated gene symbols using the function ‘alias2Symbol’ of limma 78 (v.3.50.3).
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### HIV-1 signalling remodels nuclear pores to licence infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10453-3 | PMCID: PMC13293875 | PMID: 42092137
- Evidence: Differential expression analysis was performed using the limma package (v.3.50.1) with donor as a blocking factor.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [CellProfiler, Fiji, ImageJ]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Evidence: Differential gene expression analysis was performed using the limma package.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: Differential expression was assessed using Wilcoxon or limma with Benjamini–Hochberg correction.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Template-driven scaffolding of SCF&lt;sup&gt;FBXO42&lt;/sup&gt; regulates PP2A degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10368-z | PMCID: PMC13233325 | PMID: 41986709
- Evidence: We performed a differential abundance analysis at the sgRNA level using the popular limma-voom approach 53 .
- Full pipeline: quantification [limma] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, Coot, PHENIX, R]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: Proteins were ranked based on the log-transformed fold change estimated by limma, with no log fold change threshold applied.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: DEG analyses DEGs for Cux2 cre Atf4 fl mice were determined in Omics playground 63 (v.2.8.19) by performing t -tests (standard, Welch) and limma (no trend, trend, voom), edgeR (QLF, LRT) and DESeq2 (Wald, LRT) tests and taking the highest q value for tests with cutoffs of a false-discovery rate (FDR) of 0.05 and a log 2 -transformed FC of 0.1.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Evidence: The normalization and batch effect correction were performed using the limma package v.3.34.5.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: Differential statistics of the interaction probabilities was computed using limma in R 63 .
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **3.5.4**
- Evidence: Next, the duplicate correlation (dupcor()) function of limma (v.3.5.4) 75 was used to compute the correlation of technical replicates for matching reference samples across batches.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Dynamic antigen expression and cytotoxic T cell resistance in HIV reservoir clones. (Nature 2026)

- DOI: 10.1038/s41586-026-10298-w | PMCID: PMC13190302 | PMID: 41735521
- Evidence: For visualization, batch effects were removed from VST-transformed data using limma::removeBatchEffect().
- Full pipeline: normalisation [Seurat v5.1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> visualisation [limma] -> stage not stated [MACS2]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Version used: **3.64.1**
- Evidence: The acral:cutaneous (A:C) ratio was calculated for each of the 77 primary acral tumours using the method described above after batch correction (limma v.3.64.1, ref.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: Batch effect was removed using limma 78 .
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### Pre-assembly of biomolecular condensate seeds drives RSV replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10071-5 | PMCID: PMC13043309 | PMID: 41606345
- Version used: **3.52.4**
- Evidence: R-package limma (v3.52.4) 84 was used for statistical analysis for protein intensities, applying a moderated t -test, with P values adjusted for multiple testing using Benjamini–Hochberg methodology.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [limma v3.52.4] -> stage not stated [napari]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Evidence: Significant changes between the relative protein abundance of the experimental samples to the control samples were assessed by two-sided moderated t -test as implemented in the limma package (v.3.54.2) 81 (Supplementary Table 7 ).
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Oral 4'-fluorouridine rescues nonhuman primates from advanced Lassa fever. (Nature 2026)

- DOI: 10.1038/s41586-025-09906-y | PMCID: PMC12935548 | PMID: 41501462
- Version used: **3.62.1**
- Evidence: Thresholded count matrices were exported from nSolver and analysed with limma v.3.62.1 (edgeR v.4.4.1) in R v.4.4.2 58 , 60 ; scripts are available on GitHub ( https://github.com/geisbert-lab/lasv-togo-4fiu ).
- Full pipeline: stage not stated [edgeR v4.4.1, limma v3.62.1]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: 2a,b , batch correction was performed on the VST-transformed values using limma’s removeBatchEffect, with sample material type (tissue versus organoid) treated as the batch variable 73 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: Log-normalized counts of cells were used as input to the limma-trend pipeline 91 , while accounting for gel bead-in-emulsion (GEM) group (batch effect), number of genes expressed and the percentage of mitochondrial gene expression as covariates.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **3.62.2**
- Evidence: Significance ( P values) was assessed using the limma (v.3.62.2) linear modelling framework with an empirical Bayes approach, based on log 2 -transformed normalized enrichment values.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **3.32.2**
- Evidence: The processing of the counts and differential expression analysis was performed using limma (v.3.32.2) 58 and EdgeR (v.3.20.1) 59 ) which were also used to perform pairwise differential expression analyses.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Version used: **3.1**
- Evidence: Differential expression analysis was performed on baseline samples between viraemic controllers ( n = 6) and non-controllers ( n = 3) using lmfit through limma (v.3.1) 67 .
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Evidence: Integration of CUT&Tag and VIPER analysis of snRNA-seq data Histone mark count matrices were processed using limma ‘voom’ (v.3.54.2).
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Version used: **3.60.3**
- Evidence: Differential expression analysis was performed using limma (v.3.60.3).
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### AGO2 promotes tumor progression in KRAS-driven mouse models of non-small cell lung cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2026104118 | PMCID: PMC8157917 | PMID: 33972443
- Evidence: Differential analysis between biallelic knockout and wild type was performed on voom-transformed count data ( 56 ) using the limma ( 57 ) package.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> differential/statistical testing [fgsea, limma] -> stage not stated [GSEA]

### Small noncoding RNA profiling across cellular and biofluid compartments and their implications for multiple sclerosis immunopathology. (PNAS 2021)

- DOI: 10.1073/pnas.2011574118 | PMCID: PMC8092379 | PMID: 33879606
- Evidence: Differential expression analysis was performed utilizing the limma package.
- Full pipeline: alignment/mapping [Trim Galore, featureCounts] -> differential/statistical testing [DESeq2, limma] -> stage not stated [BEDTools]

### Primate innate immune responses to bacterial and viral pathogens reveals an evolutionary trade-off between strength and specificity. (PNAS 2021)

- DOI: 10.1073/pnas.2015855118 | PMCID: PMC8020666 | PMID: 33771921
- Evidence: We normalized the resulting read-count matrix using the function voom from the R-package limma to allow using linear models by limma package ( 57 ).
- Full pipeline: read trimming [Trim Galore v0.2.7] -> alignment/mapping [HTSeq] -> normalisation [limma] -> differential/statistical testing [R v3.6.2, limma] -> stage not stated [Cytoscape v3.7.2]

### High-salt diet suppresses autoimmune demyelination by regulating the blood-brain barrier permeability. (PNAS 2021)

- DOI: 10.1073/pnas.2025944118 | PMCID: PMC7999868 | PMID: 33723078
- Evidence: For differential expression analysis, the groups of interest were contrasted using a differential enrichment test based on protein-wise linear models and empirical Bayes statistics originally implemented in the limma package ( 32 ).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [DESeq2 v1.26.1, kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.1, clusterProfiler v3.14.3, limma] -> visualisation [pheatmap, tidyverse]

### Single-cell atlas of developing murine adrenal gland reveals relation of Schwann cell precursor signature to neuroblastoma phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2022350118 | PMCID: PMC7865168 | PMID: 33500353
- Evidence: For both datasets, the normalized log2 data were quantile normalized using the R package limma ( 57 ).
- Full pipeline: normalisation [R, Seurat, limma] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [featureCounts v1.5.2]

### Placental genomic risk scores and early neurodevelopmental outcomes. (PNAS 2021)

- DOI: 10.1073/pnas.2019789118 | PMCID: PMC7896349 | PMID: 33558239
- Evidence: We used the function eBayes in the R package limma ( 92 ) to attribute a moderated t statistic to each gene related to differential expression (using the covariates provided by each reporting group); then, we applied the geneSetTest function on the moderated t statistics (results are reported in SI Appendix , Table S13 ) testing whether the selected sets of genes (that is, the genes in the GWAS lo...
- Full pipeline: quality control [PLINK v1.07] -> alignment/mapping [SPM] -> differential/statistical testing [SPM, limma] -> stage not stated [R]

### CD20 as a gatekeeper of the resting state of human B cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021342118 | PMCID: PMC7896350 | PMID: 33563755
- Evidence: Differential gene expression was determined using the limma R package ( 46 ) for P value and FDR calculation (technical replicates of Ramos WT, n = 3; biological replicates of independently generated CD20KO cell lines: KO-I, n = 4, and KO-L, n = 5).
- Full pipeline: normalisation [fgsea] -> differential/statistical testing [R, limma] -> stage not stated [CellProfiler v3.0.0, GSEA]

### The harsh microenvironment in early breast cancer selects for a Warburg phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2011342118 | PMCID: PMC7826394 | PMID: 33452133
- Evidence: Association of gene expression with continuous measure of LPR was completed with linear regression models using the limma package ( 21 ).
- Full pipeline: read trimming [R] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Cutadapt, Enrichr]

### Age-related brain atrophy is not a homogenous process: Different functional brain networks associate differentially with aging and blood factors. (PNAS 2022)

- DOI: 10.1073/pnas.2207181119 | PMCID: PMC9894212 | PMID: 36459652
- Evidence: To remove the unwanted batch effects associated with technical variables, we used the “removeBatchEffect” function from the limma ( 77 ) package, with participant age and sex accounted for as experimental design parameters.
- Full pipeline: normalisation [limma] -> registration [SPM] -> stage not stated [R]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: For the comparisons involving tumor samples, we applied the R limma package voom transformation to the RNA-seq data and then fit the mixed model by treating the groups of interest as a fixed effect and sample identification as a random effect as we estimated the correlation between the duplicated samples that were sequenced more than once ( 77 , 78 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Combination of common mtDNA variants results in mitochondrial dysfunction and a connective tissue dysregulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212417119 | PMCID: PMC9659340 | PMID: 36322731
- Evidence: The voom procedure ( 46 ) was used to normalize the RSEM generated expected counts followed by differential expression testing using R package limma ( 47 ) to obtain P values and LogFC.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [R, limma] -> stage not stated [GSEA]

### Socioeconomic inequalities in molecular risk for chronic diseases observed in young adulthood. (PNAS 2022)

- DOI: 10.1073/pnas.2103088119 | PMCID: PMC9621370 | PMID: 36252037
- Evidence: The omnibus P values were calculated as the minimum (across all genes in the disease sets) FDR-corrected P value derived from a whole-genome (limma) linear regression for the association between SES and each gene in the signature with full controls.
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R, limma] -> stage not stated [Bioconductor]

### Blockade of the protease ADAM17 ameliorates experimental pancreatitis. (PNAS 2022)

- DOI: 10.1073/pnas.2213744119 | PMCID: PMC9586293 | PMID: 36215509
- Version used: **3.50.0**
- Evidence: Differential gene expression analyses were performed using the limma (v3.50.0) package ( 29 ).
- Full pipeline: alignment/mapping [R v4.1.2] -> differential/statistical testing [limma v3.50.0] -> stage not stated [edgeR, pheatmap]

### Comparative genomics of mortal and immortal cnidarians unveils novel keys behind rejuvenation. (PNAS 2022)

- DOI: 10.1073/pnas.2118763119 | PMCID: PMC9459311 | PMID: 36037356
- Evidence: STAR ( 44 ) was used for aligning RNA sequences of each sample to the assembled T. dohrnii genome and edgeR ( 45 ) and limma ( 46 ) for modeling differential expression between stages, after applying voom ( 47 ) transformation to consider library size variability.
- Full pipeline: alignment/mapping [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [AlphaFold v2.1.2, BUSCO, ChimeraX, GSEA, fgsea]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; induces a muted host response in human blood that blunts the recruitment of neutrophils. (PNAS 2022)

- DOI: 10.1073/pnas.2123017119 | PMCID: PMC9351360 | PMID: 35881802
- Evidence: Clinical cohort analysis was performed via R package limma ( 64 ).
- Full pipeline: alignment/mapping [Bowtie2 v3.1, HTSeq] -> differential/statistical testing [DESeq2, R v3.5.1] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [limma]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Evidence: For differential analysis, we used the moderated t test as implemented in the R package limma, and multiple-hypothesis testing correction was performed with the Benjamini–Hochberg procedure.
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### Genetic and structural basis of the human anti-α-galactosyl antibody response. (PNAS 2022)

- DOI: 10.1073/pnas.2123212119 | PMCID: PMC9282431 | PMID: 35867757
- Evidence: Cohort level differences in V-region usage between α-gal + and α-gal − B cells were tested in patients and controls separately, and then between patients and controls (interaction test) by transforming counts and testing for differential usage using limma voom ( 70 ).
- Full pipeline: normalisation [CCP4] -> differential/statistical testing [limma] -> structure determination [PHENIX] -> machine learning [PHENIX]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Evidence: Counts and tpm matrices were first quantile normalized (limma R package, v.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### DNA methylation signatures in airway cells from adult children of asthmatic mothers reflect subtypes of severe asthma. (PNAS 2022)

- DOI: 10.1073/pnas.2116467119 | PMCID: PMC9214527 | PMID: 35666868
- Evidence: Differential methylation analysis was performed using a linear model in limma ( 42 ), corrected for age, gender, current smoking status, and the first three ancestry PCs.
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [WGCNA, limma] -> visualisation [pheatmap] -> stage not stated [R]

### Caspase-4/11 exacerbates disease severity in SARS-CoV-2 infection by promoting inflammation and immunothrombosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202012119 | PMCID: PMC9173818 | PMID: 35588457
- Evidence: Data were normalized using “voom,” and statistical analysis for differential expression was performed with “limma” ( 58 ).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [limma] -> visualisation [DESeq2] -> stage not stated [ComplexHeatmap]

### Induction of human trophoblast stem-like cells from primed pluripotent stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2115709119 | PMCID: PMC9171790 | PMID: 35537047
- Version used: **3.48.3**
- Evidence: Differentially expressed genes were obtained by using limma (v3.48.3) ( 50 ) with selection criteria of p-adjusted value < 0.01 and fold change > 2.
- Full pipeline: alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.32.0, R] -> normalisation [DESeq2 v1.32.0, R] -> differential/statistical testing [limma v3.48.3]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: The voom procedure was used to normalize the RSEM-generated expected counts followed by differential expression testing using R package limma to obtain P values and LogFC.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### A saturation mutagenesis screen uncovers resistant and sensitizing secondary <i>KRAS</i> mutations to clinical KRAS<sup>G12C</sup> inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2120512119 | PMCID: PMC9170150 | PMID: 35471904
- Evidence: We used limma-voom to perform a statistical differential analysis of the sequencing counts data ( 17 ).
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Bioconductor, PHENIX]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Evidence: The R package limma was used to fit the counts data to a model based on groups.
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### Layered evolution of gene expression in "superfast" muscles for courtship. (PNAS 2022)

- DOI: 10.1073/pnas.2119671119 | PMCID: PMC9168950 | PMID: 35363565
- Evidence: We analyzed changes in pairwise differential gene expression using R ( 51 ) with the limma and voom packages ( 52 , 53 ).
- Full pipeline: alignment/mapping [BCFtools, BWA, RAxML, STAR v2.7.3a] -> differential/statistical testing [limma] -> stage not stated [featureCounts v2.0.1]

### Natural disaster and immunological aging in a nonhuman primate. (PNAS 2022)

- DOI: 10.1073/pnas.2121663119 | PMCID: PMC8872742 | PMID: 35131902
- Evidence: Read counts were normalized using the voom function from the limma package in the R environment ( 76 ), which normalizes counts overall to account for between-sample variation by estimating the mean-variance relationship of the log-counts among all samples.
- Full pipeline: alignment/mapping [ANGSD, kallisto] -> quantification [limma] -> normalisation [limma] -> differential/statistical testing [R v4.0.2] -> stage not stated [HOMER, Seurat]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Evidence: We used linear mixed-effects modeling, treating each subclone line as a random intercept, using the limma voom approach ( 22 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### Transcriptional signatures of early-life stress and antidepressant treatment efficacy. (PNAS 2023)

- DOI: 10.1073/pnas.2305776120 | PMCID: PMC10710023 | PMID: 38011563
- Evidence: RNA-seq analyses for these datasets utilized the R packages “DESeq2,” “removeBatchEffect,” and “limma” ( 63 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, limma]

### Gene expression in the primate orbitofrontal cortex related to anxious temperament. (PNAS 2023)

- DOI: 10.1073/pnas.2305775120 | PMCID: PMC10710052 | PMID: 38011550
- Evidence: Analyses were performed in a custom pipeline written in python 2.7, as well as in limma ( 26 ).
- Full pipeline: alignment/mapping [Python v2.7] -> stage not stated [CellProfiler v4.2.1, ImageJ v1.53s, QuPath, Scanpy, limma, scDblFinder]

### TGF-β broadly modifies rather than specifically suppresses reactivated memory CD8 T cells in a dose-dependent manner. (PNAS 2023)

- DOI: 10.1073/pnas.2313228120 | PMCID: PMC10691214 | PMID: 37988468
- Evidence: Reads overlapping peaks were enumerated with getCounts function from chromVAR and normalized and log2-transformed with voom from R package limma ( 63 , 64 ).
- Full pipeline: normalisation [limma] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2, R]

### Dysregulated CD200-CD200R signaling in early diabetes modulates microglia-mediated retinopathy. (PNAS 2023)

- DOI: 10.1073/pnas.2308214120 | PMCID: PMC10636339 | PMID: 37903272
- Evidence: We then performed a standard EdgeR-limma pipeline analysis on all samples (n = 10) and compiled differentially expressed genes (DEG; >|1.5|FC; FDR < 0.05) for each diabetic condition compared to control.
- Full pipeline: differential/statistical testing [edgeR, limma]

### Engineered bone marrow as a clinically relevant ex vivo model for primary bone cancer research and drug screening. (PNAS 2023)

- DOI: 10.1073/pnas.2302101120 | PMCID: PMC10523456 | PMID: 37729195
- Evidence: Differentially expressed genes were then identified using limma after voom normalization ( 68 ).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [limma]

### Systems-level temporal immune-metabolic profile in Crimean-Congo hemorrhagic fever virus infection. (PNAS 2023)

- DOI: 10.1073/pnas.2304722120 | PMCID: PMC10500270 | PMID: 37669378
- Version used: **3.50.0**
- Evidence: The data were normalized using R package NormalyzerDE v1.12.0 ( 25 ), and differential expression analysis was performed using R package limma v3.50.0.
- Full pipeline: normalisation [R, limma v3.50.0] -> differential/statistical testing [R, limma v3.50.0] -> stage not stated [Bioconductor, DESeq2 v1.26.0, GSEA]

### Impaired age-associated mitochondrial translation is mitigated by exercise and PGC-1α. (PNAS 2023)

- DOI: 10.1073/pnas.2302360120 | PMCID: PMC10483666 | PMID: 37639610
- Evidence: Acquired reporter ion intensities were employed for automated quantification and statistical analysis using SafeQuant v2.3 and limma.
- Full pipeline: quantification [ImageJ v1.52a, limma] -> differential/statistical testing [edgeR, limma]

### sccomp: Robust differential composition and variability analysis for single-cell data. (PNAS 2023)

- DOI: 10.1073/pnas.2203828120 | PMCID: PMC10438834 | PMID: 37549298
- Evidence: ( 14 ) propeller 2021 Logit-linear + limma ● ● ● Phipson et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> machine learning [R] -> stage not stated [Seurat, Stan, limma, tidyverse]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Evidence: Heteroscedasticity and sample-level variation were removed from the data by applying the limma ( 46 ) (v3.15) voomWithQualityWeights function ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Differential expression was identified with robust paired moderated t tests using limma ( 97 ).
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Computational drug discovery for castration-resistant prostate cancers through in vitro drug response modeling. (PNAS 2023)

- DOI: 10.1073/pnas.2218522120 | PMCID: PMC10151558 | PMID: 37068243
- Evidence: The R package limma ( 70 ) was used to carry out differential expression analysis between the two cell lines; a threshold of 0.05 for adjusted P -values was chosen to select DE genes.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [limma] -> stage not stated [ImageJ, R v4.0.3]

### Optimal generation of hepatic tissue-resident memory CD4 T cells requires IL-1 and IL-2. (PNAS 2023)

- DOI: 10.1073/pnas.2214699120 | PMCID: PMC10120061 | PMID: 37040404
- Evidence: ( C ) Volcano plot of a selection of differentially expressed chemokines and receptors and cytokines and receptors of liver TRM vs. liver TEM. n = 6; differential gene expression calculated by limma in R.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [MACS2]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Version used: **3.38.3**
- Evidence: In R, raw count matrices were generated using HTSeq (v0.11.2), then scale factors were calculated to take into account differences in library sizes using edgeR (v3.24.3), and normalization was performed using limma (v3.38.3) as in (Law et al., 2016).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Lysosome-targeted multifunctional lipid probes reveal the sterol transporter NPC1 as a sphingosine interactor. (PNAS 2023)

- DOI: 10.1073/pnas.2213886120 | PMCID: PMC10089177 | PMID: 36893262
- Evidence: The raw TMT reporter ion signals were first cleaned for batch effects using limma ( 63 ) and further normalized using variance stabilization normalization ( 64 ).
- Full pipeline: normalisation [limma] -> stage not stated [ImageJ v2.1.0]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Evidence: Log 2 CPM values were determined using the limma package v3.50.3, normalizing by the trimmed mean of M-values method.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Epigenetic function during heroin self-administration controls future relapse-associated behavior in a cell type-specific manner. (PNAS 2023)

- DOI: 10.1073/pnas.2210953120 | PMCID: PMC9963300 | PMID: 36745812
- Evidence: Differential expression analysis was performed using limma ( 48 ) accounting for technical and biological confounding factors as follows: Gene expression ~ Genotype + Batch + Sex.
- Full pipeline: variant calling [limma] -> dimensionality reduction/clustering [ImageJ, clusterProfiler] -> differential/statistical testing [limma]

### A virus-induced circular RNA maintains latent infection of Kaposi's sarcoma herpesvirus. (PNAS 2023)

- DOI: 10.1073/pnas.2212864120 | PMCID: PMC9963958 | PMID: 36724259
- Evidence: Significances were computed when n is 2 or more with limma. * P -value < 0.05.
- Full pipeline: stage not stated [limma]

### Sec22b is a critical and nonredundant regulator of plasma cell maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2213056120 | PMCID: PMC9926242 | PMID: 36595686
- Evidence: Differential expression analysis was performed using the Bioconductor limma package and the voom transformation.
- Full pipeline: read trimming [Bioconductor, edgeR] -> alignment/mapping [Bioconductor, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [GSEA, clusterProfiler, fgsea] -> differential/statistical testing [Bioconductor, R, edgeR, limma]

### Natural selection of immune and metabolic genes associated with health in two lowland Bolivian populations. (PNAS 2023)

- DOI: 10.1073/pnas.2207544120 | PMCID: PMC9910614 | PMID: 36574663
- Evidence: We then filtered for expressed, protein-coding genes, normalized the data with the R package limma ( 99 ) and corrected for known technical effects.
- Full pipeline: alignment/mapping [R] -> variant calling [GEMMA] -> normalisation [limma] -> stage not stated [ADMIXTURE, GCTA, VCFtools]

### Epithelial tubule interconnection driven by HGF-Met signaling in the kidney. (PNAS 2024)

- DOI: 10.1073/pnas.2416887121 | PMCID: PMC11670081 | PMID: 39705305
- Evidence: Corrected log-normalized expression counts were obtained by calling the removeBatch Effect from the limma (25605792) Bioconductor package with a design formula including G1 and G2M cell cycle phase scores as covariates.
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, ImageJ]

### Large-scale CRISPR/Cas9 deletions within the WFDC gene cluster uncover gene functionality and critical roles in mammalian reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2413195121 | PMCID: PMC11665854 | PMID: 39665756
- Evidence: Missing values were imputed, and differential analysis was performed using the moderated t test and log2 fold changes in the R package limma, with multiple-hypothesis testing corrected by the Benjamini–Hochberg procedure.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R, limma]

### Natural variation in age-related dopamine neuron degeneration is glutathione dependent and linked to life span. (PNAS 2024)

- DOI: 10.1073/pnas.2403450121 | PMCID: PMC11494315 | PMID: 39388265
- Evidence: This was applied to the normalized and imputed metabolomic data using the Bioconductor limma package ( 98 ).
- Full pipeline: normalisation [Bioconductor, limma] -> stage not stated [ImageJ]

### TRIM21 induces selective autophagic degradation of c-Myc and sensitizes regorafenib therapy in colorectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406936121 | PMCID: PMC11494295 | PMID: 39388269
- Evidence: We identified the top 3,000 differentially expressed genes ranked according to B-statistics of the limma method ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [GSEA]

### Proteomic and phosphoproteomic landscape of localized prostate cancer unveils distinct molecular subtypes and insights into precision therapeutics. (PNAS 2024)

- DOI: 10.1073/pnas.2402741121 | PMCID: PMC11459144 | PMID: 39320917
- Evidence: We compared the levels of phosphorylated sites between tumor and normal tissues within each proteomic subtype by using a simple linear model and moderated t-statistics implemented in the R package limma ( 37 ) (version 3.46.15).
- Full pipeline: differential/statistical testing [R, limma] -> stage not stated [GSEA]

### FicD sensitizes cellular response to glucose fluctuations in mouse embryonic fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2400781121 | PMCID: PMC11420183 | PMID: 39259589
- Evidence: To ensure this loss of response was not an artifact of our RNA seq analysis with EdgeR, we compared the EdgeR-defined DEGs to those defined by additional methods (DESeq2, NOISeq, and limma).
- Full pipeline: stage not stated [DESeq2, edgeR, limma]

### Alloreactive memory CD4 T cells promote transplant rejection by engaging DCs to induce innate inflammation and CD8 T cell priming. (PNAS 2024)

- DOI: 10.1073/pnas.2401658121 | PMCID: PMC11348247 | PMID: 39136987
- Evidence: For PCA and heatmap visualization, batch effects were removed using the removeBatchEffect() function from the limma R package ( https://doi.org/10.1093/nar/gkv007 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2, limma] -> differential/statistical testing [DESeq2, R] -> visualisation [limma] -> stage not stated [fgsea]

### Oxysterol binding protein regulates the resolution of TLR-induced cytokine production in macrophages. (PNAS 2024)

- DOI: 10.1073/pnas.2406492121 | PMCID: PMC11331125 | PMID: 39361877
- Evidence: Statistical analysis of differential lipid abundance was performed using the limma package ( 56 ) in R on the log 2 -transformed concentration measurements.
- Full pipeline: quality control [FastQC v0.11.5] -> quantification [ImageJ, limma] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [R, edgeR v3.26.8, limma] -> stage not stated [GSEA, MACS2 v2.1.0, featureCounts]

### IFIH1 (MDA5) is required for innate immune detection of intron-containing RNA expressed from the HIV-1 provirus. (PNAS 2024)

- DOI: 10.1073/pnas.2404349121 | PMCID: PMC11260138 | PMID: 38985764
- Version used: **3.46.0**
- Evidence: DESeq2’s rlog variance stabilization transformation was applied to the gene counts, and the donor effect was removed using limma (v3.46.0) software removeBatchEffect function prior to generating the heatmap and PCA plots.
- Full pipeline: alignment/mapping [RSEM v1.3.1] -> quantification [RSEM v1.3.1] -> dimensionality reduction/clustering [limma v3.46.0] -> differential/statistical testing [DESeq2 v1.30.1]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: To format counts for modeling of differential accessibility in limma, we created a DGElist object and applied calcnormFactors with edgeR (Version 3.34.1) ( 51 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### Psychosocial experiences are associated with human brain mitochondrial biology. (PNAS 2024)

- DOI: 10.1073/pnas.2317673121 | PMCID: PMC11228499 | PMID: 38889126
- Version used: **3.44.3**
- Evidence: Pseudo-bulk UMI counts normalization was done by using the trimmed mean of M-values (TMM) method of edgeR, and log2 of counts per million174 mapped reads (CPM) were calculated using the voom function of limma (version 3.44.3).
- Full pipeline: read trimming [edgeR, limma v3.44.3] -> alignment/mapping [edgeR, limma v3.44.3] -> normalisation [edgeR, limma v3.44.3] -> differential/statistical testing [R v4.0.4] -> stage not stated [Bioconductor]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles up-regulate and directly transfer adherence factors promoting host cell colonization. (PNAS 2024)

- DOI: 10.1073/pnas.2401159121 | PMCID: PMC11194581 | PMID: 38865261
- Evidence: Normalized filtered data were variance-stabilized using the voom function in limma ( 76 ), and differentially expressed genes were identified with linear modeling using limma (FDR ≤ 0.05; absolute logFC ≥ 0.8) after correcting for multiple testing using the Benjamini–Hochberg procedure.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [Galaxy]

### Long noncoding RNA LIRIL2R modulates FOXP3 levels and suppressive function of human CD4<sup>+</sup> regulatory T cells by regulating IL2RA. (PNAS 2024)

- DOI: 10.1073/pnas.2315363121 | PMCID: PMC11161746 | PMID: 38805281
- Version used: **3.42.2**
- Evidence: Differentially accessible regions were identified using limma (v3.42.2) R package ( 65 ) with |logFC| > 1 and a P -value < 0.01.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9, kallisto] -> differential/statistical testing [R, limma v3.42.2] -> stage not stated [GSEA]

### TRAF3 loss-of-function reveals the noncanonical NF-κB pathway as a therapeutic target in diffuse large B cell lymphoma. (PNAS 2024)

- DOI: 10.1073/pnas.2320421121 | PMCID: PMC11067025 | PMID: 38662551
- Evidence: DGEA between NFKB2-positive and NFKB2-negative DLBCL samples was performed using limma.
- Full pipeline: stage not stated [DESeq2 v1.26.0, GSEA v4.1.0, limma]

### A survey of chromosomal instability measures across mechanistic models. (PNAS 2024)

- DOI: 10.1073/pnas.2309621121 | PMCID: PMC11032477 | PMID: 38588415
- Version used: **3.46**
- Evidence: Linear modeling and differential expression analysis were performed in limma (v3.46) ( 72 , 73 ).
- Full pipeline: quantification [R] -> normalisation [R] -> differential/statistical testing [limma v3.46]

### Improved RNA stability estimation through Bayesian modeling reveals most <i>Salmonella</i> transcripts have subminute half-lives. (PNAS 2024)

- DOI: 10.1073/pnas.2308814121 | PMCID: PMC10998600 | PMID: 38527194
- Evidence: This is similar to the idea of variance shrinkage through empirical Bayes methods implemented in edgeR ( 26 ) and limma ( 79 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [Cutadapt v4.1, HTSeq] -> quantification [HTSeq] -> normalisation [Stan] -> differential/statistical testing [GSEA, Stan] -> simulation/modelling [Stan] -> stage not stated [R, edgeR, limma]

### Principled and interpretable alignability testing and integration of single-cell data. (PNAS 2024)

- DOI: 10.1073/pnas.2313719121 | PMCID: PMC10927515 | PMID: 38416677
- Evidence: Other methods such as limma ( 25 ) and MAST ( 26 ) consider linear batch correction, whose focus is restricted to differential testing and does not account for possible covariance shifts.
- Full pipeline: normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Seurat]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: To conduct the co-occurrence analysis, we employed the VennCounts() function from the R package “limma” to calculate the number of overlapping genes between gene groups.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Cortical &lt;i&gt;miR-709&lt;/i&gt; links glutamatergic signaling to NREM sleep EEG slow waves in an activity-dependent manner. (PNAS 2024)

- DOI: 10.1073/pnas.2220532121 | PMCID: PMC10801902 | PMID: 38207077
- Evidence: Statistical analysis was performed with the R Bioconductor package limma by fitting a linear model and computing moderated t tests, comparing miRNA expression levels in the SD vs. the control group.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [Bioconductor, R, limma] -> stage not stated [WGCNA]

### Neural crest cell recruitment and reprogramming as central drivers of embryonic limb regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2519994122 | PMCID: PMC12772167 | PMID: 41433066
- Evidence: Differential gene expression analysis was performed by building a linear model using limma package.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Seurat]

### Convergent mutation trajectories convert functional self-tolerance in IGHV4-34 B cells to genetic tolerance encoded in the antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2522257122 | PMCID: PMC12745689 | PMID: 41410768
- Evidence: Differentially expressed genes between Pre589+ and Pre589− B2 cells were determined using limma ( 74 ) on log transcription quotients from Sanity.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [GSEA]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Evidence: Differential expression analysis was performed using voom ( 57 ) and limma ( 58 , 59 ).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### Elevated virus infection of honey bee queens reduces methyl oleate production and destabilizes colony-level social structure. (PNAS 2025)

- DOI: 10.1073/pnas.2518975122 | PMCID: PMC12557728 | PMID: 41086214
- Evidence: We used tools within the limma package ( 86 ), which enables empirical Bayes variance estimation, to identify significant relationships between lipid compound abundances and total virus load (continuous predictor) for both the cage trial (final n = 27) and field sample data (n = 29, down from 32 due to three instances of queen rejection, supersedure, or mishandling).
- Full pipeline: quantification [limma] -> differential/statistical testing [emmeans] -> stage not stated [R v4.3.0]

### Targeting the 3D genome by anthracyclines for chemotherapeutic effects. (PNAS 2025)

- DOI: 10.1073/pnas.2500704122 | PMCID: PMC12519215 | PMID: 41042842
- Evidence: Differential peaks between groups were assessed by limma eBayes, with FDR < 0.05 defining significance.
- Full pipeline: differential/statistical testing [DESeq2, limma] -> stage not stated [HOMER]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Gene expression data were normalized using the TMM method in edgeR ( 34 ) (v4.2.0), and DEGs were identified using limma-voom ( 35 ) (v3.60.0).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: We then calculated a contrast matrix and corrected for Poisson count noise using the makeContrast and voom functions of the R package limma ( 78 ), respectively.
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### Patient stratification reveals the molecular basis of disease co-occurrences. (PNAS 2025)

- DOI: 10.1073/pnas.2421060122 | PMCID: PMC12415287 | PMID: 40880536
- Evidence: After performing batch effect identification, we used the limma pipeline ( 17 ) for differential expression analysis.
- Full pipeline: quality control [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [GSEA, limma]

### Evolutionarily conserved grammar rules viral factories of amoeba-infecting members of the hyperdiverse &lt;i&gt;Nucleocytoviricota&lt;/i&gt; phylum. (PNAS 2025)

- DOI: 10.1073/pnas.2515074122 | PMCID: PMC12415211 | PMID: 40864652
- Evidence: The volcano plots represent the −log10 (limma P -value) on the y axis plotted against the log2(FoldChange bait vs. control) on the x axis for each quantified protein ( Upper panel: OLS1-GFP vs.
- Full pipeline: quantification [limma] -> dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> visualisation [limma] -> stage not stated [HMMER v3.3.2, ImageJ]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: ...ages library(clusterProfiler), library(matrixStats), library(gplots), library(RColorBrewer), library(sqldf), library(hopach), library(edgeR), library(limma), library(GOstats), library(GO.db), library(org.Hs.eg.db), library(org.Mm.eg.db), library(data.table), library(circlize), library(gridExtra), library(ggplot2), library(dplyr)})) # Set new working directory setwd(“”) # Load significant genes dat...
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: Expression estimates were fitted to a nested linear model using the lmFit and eBayes functions in the limma package.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### PLAA/UFD-3 regulates P-bodies through its intrinsic disordered domain. (PNAS 2025)

- DOI: 10.1073/pnas.2427250122 | PMCID: PMC12232612 | PMID: 40560612
- Evidence: The raw data without further normalization or imputation were analyzed using an empirical Bayes test based on the limma R package, using function limma::eBayes().
- Full pipeline: normalisation [limma] -> stage not stated [Python, R v4.2.2]

### Testicular somatic and germ cell maturation during rhesus macaque development. (PNAS 2025)

- DOI: 10.1073/pnas.2419995122 | PMCID: PMC12232671 | PMID: 40569389
- Evidence: To identify DEGs of 2-fold or greater between the groups, the limma package with empirical Bayes moderation was used ( 23 ) with a false discovery rate (FDR) adjustment of p <0.05 for statistical significance ( Dataset S1A ).
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle]

### The RRM domain-containing protein Rbp3 interacts with ribosomes and the 3' ends of mRNAs encoding photosynthesis proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2506275122 | PMCID: PMC12232666 | PMID: 40553498
- Evidence: Raw data were normexp background corrected ( 87 ) and quantile normalized using the limma R package ( 88 ).
- Full pipeline: alignment/mapping [DESeq2] -> normalisation [R, limma] -> stage not stated [AlphaFold]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles suppress IFNε-mediated responses driven by its intracellular bacterial symbiont &lt;i&gt;Mycoplasma hominis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2508297122 | PMCID: PMC12232435 | PMID: 40560611
- Evidence: Normalized filtered data were variance stabilized using the voom function in limma ( 90 ), and differentially expressed genes were identified with linear modeling using limma (FDR ≤ 0.05; absolute Log 2 FC ≥ 1) after correcting for multiple testing using Benjamini–Hochberg.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [GSEA]

### Single Antisense Oligonucleotides Correct Diverse Splicing Mutations in Hotspot Exons. (PNAS 2025)

- DOI: 10.1073/pnas.2425659122 | PMCID: PMC12207475 | PMID: 40523177
- Evidence: To estimate the MaPSy splicing score using three replicates, log fold change (FC) estimates from mpralm ( 49 ), a variation of the limma-voom framework for allelic differential expression in massively parallel reporter assays ( 50 , 51 ), were utilized.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [SAMtools, VEP]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: Differential analysis was performed using the limma-voom procedure ( 26 , 27 ) after TMM-normalization ( 28 ) of gene-level counts with calcNormFactors of edgeR ( 29 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### HCK regulates NLRP12-mediated PANoptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2422079122 | PMCID: PMC12130821 | PMID: 40408404
- Version used: **3.60.2**
- Evidence: For differential gene expression analysis, we employed the limma v3.60.2 package ( 69 ).
- Full pipeline: differential/statistical testing [limma v3.60.2] -> simulation/modelling [R] -> visualisation [ChimeraX v1.8, R] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.8]

### Transcriptomic and proteomic ramifications of segmental amplification in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2422424122 | PMCID: PMC12107188 | PMID: 40372434
- Evidence: Differential expression analysis was performed in R v4.3.1/RStudio (Posit team; Boston, MA) with the following Bioconductor/R packages: edgeR ( 66 , 67 ), limma ( 68 ), glimma, gplots, RcolorBrewer, and Nonnegative Matrix Factorization.
- Full pipeline: differential/statistical testing [Bioconductor, R v4.3, edgeR, limma]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Version used: **3.54.2**
- Evidence: To address donor-related batch effects, the removeBatchEffect function in limma v3.54.2 was applied to the gene expression data.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Protein Phosphatase 1 Regulatory Subunit 3C integrates cholesterol metabolism and isocitrate dehydrogenase in chondrocytes and neoplasia. (PNAS 2025)

- DOI: 10.1073/pnas.2501519122 | PMCID: PMC12037013 | PMID: 40232792
- Version used: **3.60.2**
- Evidence: TMM normalization and differential gene expression analysis were performed using the R packages edgeR (v4.2.2) and limma (v3.60.2), respectively.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> quantification [Fiji, ImageJ, QuPath, featureCounts v1.5.0] -> normalisation [edgeR v4.2.2, limma v3.60.2] -> differential/statistical testing [edgeR v4.2.2, limma v3.60.2] -> stage not stated [R, fgsea v1.30.0, survival (R)]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Evidence: Statistical testing was conducted with limma, whereby differentially expressed proteins were selected using a log 2 FC cut-off of 1 and a P -value cut-off of 0.00776, allowing to reach a FDR inferior to 1% according to the Benjamini–Hochberg estimator.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: Differential expression analysis was performed on the batch-corrected 23 controls and 27 MASLD samples using limma voom (PMID: 24485249).
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### TGFb signaling instructs a conserved fibrosis-associated cell state marked by LRRC15. (PNAS 2026)

- DOI: 10.1073/pnas.2536550123 | PMCID: PMC13214008 | PMID: 42160341
- Version used: **3.56.1**
- Evidence: Pairwise differential expression analysis between treatment conditions was performed using the limma+voom method provided by the limma v3.56.1 R package ( 47 ).
- Full pipeline: normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.56.1] -> simulation/modelling [Slingshot]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: Variation associated with biological replicates was removed using limma:removeBatchEffect ) ( 69 ).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Evidence: ... 2) normalization (signal space transformation robust multiple-array average); 3) differentially expression analysis employing the eBayes method from limma R package included in TAC software.
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Differential gene expression was performed using the R Bioconductor package limma ( 49 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### Toward the simultaneous detection of multiple diseases with a highly cost-effective cell-free DNA methylome test. (PNAS 2026)

- DOI: 10.1073/pnas.2518347123 | PMCID: PMC13080018 | PMID: 41941615
- Evidence: The popular empirical Bayes method, which moderates the SE of the estimated log-fold changes ( 30 ) (R package limma) was used to identify those target regions that can differentiate between one cancer type and all others (one-vs-rest) and between any two pairs of cancer types (one-vs-one).
- Full pipeline: stage not stated [R, limma]

### Mild SARS-CoV-2 maternal infection in mice induces transient offspring neurodevelopmental aberrance. (PNAS 2026)

- DOI: 10.1073/pnas.2518294123 | PMCID: PMC13012083 | PMID: 41849379
- Version used: **3.58.1**
- Evidence: Differential expression analysis was performed using R package limma (version 3.58.1).
- Full pipeline: quality control [FastQC v0.11.9] -> dimensionality reduction/clustering [clusterProfiler v4.10.0] -> differential/statistical testing [limma v3.58.1] -> visualisation [ggplot2 v3.5.2] -> stage not stated [R v4.3.2]

### Global analysis of protein degradation reveals instability of diverse regulators in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2515265123 | PMCID: PMC12974527 | PMID: 41774798
- Evidence: All normalization and differential abundance analysis was conducted with the R package limma ( 100 ).
- Full pipeline: quantification [limma] -> normalisation [limma] -> differential/statistical testing [XGBoost, limma] -> machine learning [XGBoost] -> stage not stated [AlphaFold, R, STRING db]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Version used: **3.62.2**
- Evidence: For PCA, gene counts were downsampled to the same library size and batch effects were regressed out using removeBatchEffects function in limma (v.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### CHAMP1 complex promotes heterochromatin assembly and reduces replication stress. (PNAS 2026)

- DOI: 10.1073/pnas.2525144122 | PMCID: PMC12773717 | PMID: 41481470
- Evidence: The associations between mRNA expression of CCNE and that of every other gene were assessed using the robust linear regressions on the log 2 (TPM+1) mRNA expression values, as computed by the limma ( 59 ) package in R, with robust empirical Bayes moderation and lineage correction.
- Full pipeline: quantification [ImageJ, limma] -> differential/statistical testing [R, ggplot2, limma] -> visualisation [ImageJ, survival (R) v0.5.0]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Differential expression analysis was performed using limma-trend with empirical Bayes moderation.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Mitochondria protect against an intracellular pathogen by restricting access to folate. (Science 2025)

- DOI: 10.1126/science.adr6326 | PMCID: PMC12483063 | PMID: 40811546
- Evidence: Differential expression analysis was performed using limma, in R ( 58 ).
- Full pipeline: differential/statistical testing [limma] -> visualisation [R, tidyverse]

### Silencing mitochondrial gene expression in living cells. (Science 2025)

- DOI: 10.1126/science.adr3498 | PMCID: PMC7618265 | PMID: 40403134
- Version used: **3.56.2**
- Evidence: Batch correction was applied using limma (version 3.56.2) ( 45 ) to account for variability between replicates performed on different days with different reagent batches (batch1: replicate 1 and 2; batch 2: replicate 3 and 4) to improve clustering and reliability of differential expression results.
- Full pipeline: quantification [ImageJ v1.47] -> normalisation [limma v3.56.2] -> dimensionality reduction/clustering [clusterProfiler v4.8.3, limma v3.56.2] -> differential/statistical testing [DESeq2 v1.40.2, ImageJ v1.47, limma v3.56.2] -> stage not stated [Bioconductor, R v4.3.0, ggplot2]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: Principal component analysis (PCA) plots were generated using the top 500 most variable genes, applying the vst() function and limma::removeBatchEffect() to remove batch effects for PCA visualization.
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

