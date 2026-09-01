# clusterProfiler

- **Category:** genomics
- **Papers in survey:** 244
- **Journals:** PNAS (120), Nature (95), Cell (20), Science (9)
- **Years:** 2021 (12), 2022 (37), 2023 (40), 2024 (44), 2025 (70), 2026 (41)
- **Versions named:** 4.10.1 (6), 4.6.2 (6), 3.14.3 (5), 4.2.2 (5), 4.0.5 (4), 4.12.0 (3), 4.14.6 (3), 4.8.3 (3), 4.6.0 (3), 4.0 (3)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (244), differential/statistical testing (55), visualisation (9), alignment/mapping (3), normalisation (3), simulation/modelling (2), quantification (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **3.14.3**
- Evidence: ...oject.org/web/packages/dplyr/index.html R package uwot version 0.1.8 Melville, 2020 https://cran.r-project.org/web/packages/uwot/index.html R package clusterProfiler version 3.14.3 Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html R package ggpubr version 0.4.0 Kassambara, 2020 https://cran.r-project.org/web/packages/ggpubr/index.html R package tidyr version ...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **3.15.4**
- Evidence: ...c/html/tximport.html R Package: DESeq2 (version 1.27.32) Love et al. , 2014 http://bioconductor.org/packages/release/bioc/html/DESeq2.html R Package: clusterProfiler (version 3.15.4) Yu et al. , 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html R Package: ChIPpeakAnno (version 3.22.0) Zhu et al. , 2010 https://www.bioconductor.org/packages/release/bioc/html/ChIPpeakAnno...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...apt Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ Limma Ritchie et al., 2015 https://bioconductor.org/packages/release/bioc/html/limma.html clusterProfiler Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html Resource availability Lead contact Further information and requests for reagents may be directed to and will be fulfilled by Lead Contact Ivan Ma...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.053 | PMCID: PMC7857060 | PMID: 33657410
- Evidence: Based on these genes, enriched GO terms were then acquired for each group of cells using R package clusterProfiler ( Yu et al., 2012 ) following the default parameters.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [SCENIC v1.1.2, Scanpy v1.4.6, Seurat v2.3.0, kallisto, scDblFinder]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Version used: **3.16.1**
- Evidence: ...n.r-project.org/web/packages/WGCNA/index.html STRING Database version 11.0 Szklarczyk et al., 2019 ; STRING Database https://string-db.org/ R package clusterProfiler version 3.16.1 R Bioconductor; Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html R package ggplot2 version 3.3.2 R CRAN https://cran.r-project.org/web/packages/ggplot2/index.html R package pheatm...
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 103 https://github.com/chanzuckerberg/cellxgene clusterProfiler (version: 3.18.1) Yuetal.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Mild respiratory COVID can cause multi-lineage neural cell and myelin dysregulation. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.008 | PMCID: PMC9189143 | PMID: 35768006
- Evidence: (2021) https://doi.org/10.1101/2021.11.28.470236 clusterProfiler package (v4.0.5) Wu et al.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.1.0, UMAP, clusterProfiler] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [ImageJ, R v4.1.1]

### Disrupting autorepression circuitry generates "open-loop lethality" to yield escape-resistant antiviral agents. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.022 | PMCID: PMC9097017 | PMID: 35561685
- Evidence: Enrichment analyses was performed to identify gene ontology (GO) terms for the clusters that had more than 100 genes with available Entrez IDs using the enrichGO function from the clusterProfiler package to search for biological process sub-ontologies and assessed the significance of enrichment of a GO term relative to a background set of all the genes detected ( Yu et al., 2012 ).
- Full pipeline: alignment/mapping [kallisto] -> quantification [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Version used: **3.19.0**
- Evidence: R packages used for GSEA were AnnotationDbi (1.52.0) and org.Hs.eg.db, (3.12.0), clusterProfiler (3.19.0), msigdbr (7.2.1), for C2 curated datasets.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: 67 https://guangchuangyu.github.io/software/clusterProfiler/ SynaptosomesMacro Paget-Blanc et al.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Version used: **4.4.1**
- Evidence: The over-representation analysis was performed using the enricher function from R package clusterProfiler (version 4.4.1) 39 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: 105 https://github.com/varemo/piano clusterProfiler Väremo et al.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: 96 https://bioconductor.org/packages/3.14/bioc/html/limma.html clusterProfiler Yu et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### SARS-CoV-2 replication in airway epithelia requires motile cilia and microvillar reprogramming. (Cell 2023)

- DOI: 10.1016/j.cell.2022.11.030 | PMCID: PMC9715480 | PMID: 36580912
- Evidence: GO ORA was conducted using the enrichGO function from the clusterProfiler package from Bioconductor 85 and the database org.Hs.eg.db package from Bioconductor (Marc Carlson (2020). org.Hs.eg.db: Genome wide annotation for Human.
- Full pipeline: normalisation [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, GSEA] -> stage not stated [ImageJ, MACS2, R]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 84 https://ggplot2.tidyverse.org/ clusterProfiler R package Yu et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### CSF proteomics identifies early changes in autosomal dominant Alzheimer's disease. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.049 | PMCID: PMC11531390 | PMID: 39332414
- Version used: **4.0**
- Evidence: ...maDataIO Biobase 2.42.0 Open-source https://www.bioconductor.org/packages/release/bioc/html/Biobase.html UniProt Open-source https://www.uniprot.org/ clusterProfiler 4.0 Yu et al.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.0] -> simulation/modelling [GSVA] -> visualisation [ggplot2] -> stage not stated [R v4.1.3, WGCNA]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: The Gene Set Enrichment Analysis (GSEA) was carried out to examine any over-representation of the sorted AHNAK-KD signature in the AHNAK-centered network neighborhoods (up to 3-layers in the MSBB MEGENA proteomics network) using the R package clusterProfiler.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### Serotonin transporter inhibits antitumor immunity through regulating the intratumoral serotonin axis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.032 | PMCID: PMC12255530 | PMID: 40403728
- Evidence: For gene set enrichment analysis (GSEA), the clusterProfiler packages were used to calculate the enrichment scores for each cluster in the signature gene list (GEO: GSE122713 ).
- Full pipeline: quantification [R, Seurat v4.0.0] -> dimensionality reduction/clustering [GSEA, R, Seurat v4.0.0, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2, velocyto]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: Annotation of genomic features: The distribution of PHGDH peaks in genomic features was obtained from the anotatePeak function in the ‘clusterProfiler‘ R package, based on the GENCODE V36.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### Therapeutic potential of allosteric HECT E3 ligase inhibition. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.001 | PMCID: PMC12087876 | PMID: 40179885
- Evidence: 2.4 Thermo Fisher Scientific N/A clusterProfiler Mund et al.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [AlphaFold, PyMOL]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Version used: **3.18.1**
- Evidence: Gene Ontology enrichment analysis was performed using the R package clusterProfiler (v.3.18.1).
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Pathway enrichment analysis was performed using the clusterProfiler R package 54 using the top 100 genes for each cell cluster/group as defined by the sortGenes function from the genesorteR package.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: The DEGs of each cell cluster from mouse and monkey were used for GO enrichment and analysed by the clusterProfiler R package 55 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### The pupal moulting fluid has evolved social functions in ants. (Nature 2022)

- DOI: 10.1038/s41586-022-05480-9 | PMCID: PMC9750870 | PMID: 36450990
- Evidence: The list of proteins identified in the pupal fluid was evaluated for functional enrichment in these GO terms, P -values were adjusted with an FDR cut-off of 0.05, and the network plots were visualized using the clusterProfiler package 37 .
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R v3.6.3, clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [ImageJ]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Evidence: GO enrichment analysis for differentially expressed genes was implemented with the clusterProfiler R package (v3.14.3), using the human genome annotation record in the org.Hs.eg.db R package (v3.10.0) and a Benjamini–Hochberg-adjusted P value of 0.05 as the cut-off.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### Spatial profiling of chromatin accessibility in mouse and human tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05094-1 | PMCID: PMC9452302 | PMID: 35978191
- Evidence: The enrichGO function in the clusterProfiler package was used for GO enrichment analysis (qvalueCutoff = 0.05) 56 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [Python, Seurat] -> stage not stated [ArchR, Snakemake]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: ...brain. d , Top Gene Ontology biological process terms associated with genes nearest to brain-specific or shared (≥4 other tissues) ERα CUT&RUN peaks (clusterProfiler, P adj < 0.1). e , Combined sex E2 versus vehicle RNA-seq in BNSTp Esr1 + cells; light grey and red dots (DESeq2, P adj < 0.1), dark grey and red dots (DESeq2, P < 0.01), purple dots (validated by in situ hybridization (ISH)).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: GO enrichment We performed GO enrichment analysis using R package clusterProfiler 100 , 101 .
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: The significant pathways were obtained by running a hypergeometric test using clusterProfiler listing the pathways with a varied range of FDRs.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Glioma synapses recruit mechanisms of adaptive plasticity. (Nature 2023)

- DOI: 10.1038/s41586-023-06678-1 | PMCID: PMC10632140 | PMID: 37914930
- Evidence: 4e,f,g ) was computed for the positively correlated genes in each state (145, 138 and 97 genes with Pearson correlation coefficient greater than 0.25 for the AC-like, OC-like and OPC-like states, respectively) using the function enrichGo (package clusterProfiler).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [ImageJ v2.1.0, RSEM, featureCounts, kallisto] -> normalisation [RSEM] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.36.0] -> visualisation [ImageJ v2.1.0] -> stage not stated [R v4.1.1]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Evidence: To perform gene ontology analysis, we used the function ‘enrichGO’ from the R package clusterProfiler 66 with ‘pAdjustMethod = ′fdr′’.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: Pathway enrichment was performed on genes associated with differential peaks using the enrichGO function in the Bioconductor package clusterProfiler and similar pathways were merged in R using the ‘simplify’ function with a similarity cut-off of 0.7.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Version used: **3.18.1**
- Evidence: A heat map of the resulting data matrix annotated by Gene Ontology (GO) terms was constructed for preliminary interpretation by first clustering the genes and then running enrichment analysis using clusterProfiler (v.3.18.1) to select the most significant GO terms associated with said clusters (our script also allowed us to use WikiPathways and KEGG).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### A druggable copper-signalling pathway that drives inflammation. (Nature 2023)

- DOI: 10.1038/s41586-023-06017-4 | PMCID: PMC10131557 | PMID: 37100912
- Evidence: Enrichment analysis from differentially expressed genes has been performed using the enrichGO function from clusterProfiler package v3.16.1.
- Full pipeline: quality control [Nextflow] -> normalisation [R, deepTools, edgeR v3.30.3] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, limma]

### Spatial epigenome-transcriptome co-profiling of mammalian tissues. (Nature 2023)

- DOI: 10.1038/s41586-023-05795-1 | PMCID: PMC10076218 | PMID: 36922587
- Version used: **4.2**
- Evidence: GO enrichment analysis was conducted with the ‘enrichGO’ function (qvalueCutoff = 0.05) in the clusterProfiler v.4.2 package 25 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.2] -> visualisation [ArchR v1.0.1, Seurat v4.1] -> stage not stated [Monocle, Signac v1.8]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: The Gene Ontology term enrichment analysis was performed using Enrichr online tool ( https://maayanlab.cloud/Enrichr/ ), STRING ( https://string-db.org ) and clusterProfiler 57 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Evidence: GO enrichment analysis was performed using the WEB-based Gene Set Analysis Toolkit” (WebGestalt) and the R package clusterProfiler.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Version used: **3.14.3**
- Evidence: Bioinformatics analysis Gene set enrichment analysis The enrichment analysis for chromosomal gene distributions was done in R v3.6.3 with the GSEA function of clusterProfiler v3.14.3 53 was used with maxGSSize = 20000 and nPerm = 20000.
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Gene set enrichment analysis was performed in R using the GSEA function of the clusterProfiler package (version 4.4.4) 65 .
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: Over-representation for ‘RAS-late genes’ was analysed using the clusterProfiler R package (v.3.16.0).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Version used: **3.18.1**
- Evidence: Finally, with the full list of rank statistics calculated for all genes tested, we used the function GSEA (parameters: pvalueCutoff=0.5; package: clusterProfiler v.3.18.1) to obtain the normalized enrichment score of Hallmark pathways (package: msigdbr 7.5.1) from the MSigDB 64 .
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Evidence: Gene Ontology and feature annotation Gene Ontology has been realized using R packages for Gene Ontology clusterProfiler, the annotation DB org.Hs.eg.db and msigdbr.
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: Gene-centric enrichment analysis was performed using the clusterProfiler package, accessing the MsigDB C5 database.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: We checked the Gene Ontology terms of the top 500 genes that were most positively or negatively correlated to absorption probabilities using the clusterProfiler R package 60 .
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Early intermittent hyperlipidaemia alters tissue macrophages to fuel atherosclerosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07993-x | PMCID: PMC11464399 | PMID: 39231480
- Version used: **4.4.4**
- Evidence: GO and KEGG pathway analysis were performed using R package clusterProfiler (v.4.4.4) 54 , 55 on the significant DEGs ( n = 746); all identified pathways are listed in Supplementary Table 2 , with ten selected pathways plotted in Fig.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.4.4] -> visualisation [clusterProfiler v4.4.4] -> stage not stated [DESeq2 v1.36.0, R, Seurat v5.0.0]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: The results from the differential gene expression analysis were used for gene set enrichment analysis of Hallmark pathways using clusterProfiler 66 . scRNA-seq experiments Cryopreserved PBMCs obtained at baseline and after 3 months of testosterone treatment were thawed in thawing medium (RPMI 1640 HyClone supplemented with 10% FBS, 1% penicillin-streptomycin and Benzonase-nuclease (Sigma-Aldrich))...
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Evidence: Significantly downregulated genes between the 5B8 and IgG2b treated group ( P < 0.05) were on clusterProfiler to determine significantly downregulated pathways using the enrichGO function.
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Evidence: Gene-set enrichment analysis 68 , 69 was performed on each T cell subsets with the GSEA function of clusterProfiler 70 in R.
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Evidence: R packages used were limma ( https://bioconductor.org/packages/limma ), MSnbase ( https://bioconductor.org/packages/MSnbase ), tidyverse ( https://tidyverse.tidyverse.org ), biobroom ( https://bioconductor.org/packages/biobroom ), ggrepel ( https://cran.r-project.org/web/packages/ggrepel/vignettes/ggrepel.html ) and ClusterProfiler ( https://bioconductor.org/packages/clusterProfiler/ ).
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### Single-cell nascent RNA sequencing unveils coordinated global transcription. (Nature 2024)

- DOI: 10.1038/s41586-024-07517-7 | PMCID: PMC11222150 | PMID: 38839954
- Evidence: A network of pairwise co-transcribed genes was created using the Leiden algorithm, and the modules were selected for gene ontology analyses using the clusterProfiler R package.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Cutadapt] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Seurat]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: GO analysis was performed using the clusterProfiler 49 R package v4.8.3.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Version used: **4.6.2**
- Evidence: Pathway analysis of the differential genes and grouped genes in the heat map was performed using QIAGEN Ingenuity Pathway Analysis 2022 Winter Release and clusterProfiler v.4.6.2.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Evidence: The ORA was performed using the ‘enrich_GO’ function (parameters: keyType = “ENTREZID”, OrgDb = org.Mm.eg.db, ont = “ALL”, pAdjustMethod = “BH”, qvalueCutoff = 0.1) of the clusterProfiler package 58 (v.3.16.1).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Version used: **4.6.0**
- Evidence: Gene Ontology analysis was performed on all genes with a spatial variation Z score above 7.0 using EnrichGO from clusterProfiler v.4.6.0 (using the default parameters) and using annotations from org.Hs.eg.db v.3.16.0 (Supplementary Table 3 ) under the biological process ontology.
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Dictionary of immune responses to cytokines at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-023-06816-9 | PMCID: PMC10781646 | PMID: 38057668
- Version used: **4.2.1**
- Evidence: The top 30 genes with the highest weights for each GP were used to identify enriched biological processes using clusterProfiler (v.4.2.1) 46 on the Hallmark gene sets from the MSigDB database 47 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.1] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Version used: **4.6.0**
- Evidence: Ontology analysis was performed on differential protein abundance data generated by MSqROB using clusterProfiler (v4.6.0) 57 gene set enrichment analysis, applying Benjamini–Hochberg correction and grouping proteins by ‘Reactome pathway’ annotations (v.65) 58 . scRNA-seq library preparation and data processing Single-cell suspensions of human breast cells were generated as described above and scRN...
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Version used: **4.0**
- Evidence: GO enrichment analysis To relate various gene modules to known biological processes, we performed gene set enrichment analyses using the R package clusterProfiler 4.0 (RRID: SCR_016884 ) 89 and g:Profiler (RRID: SCR_006809 ) 90 .
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Evidence: The analysis was performed using the function enrichGO() from the R package clusterProfiler 99 with minGSSize set to 20 and maxGSSize set to 200.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Evidence: Gene set enrichment for gene ontology (GO) terms labelled BP (for Biological Process) was performed in R with the clusterProfiler package (v.4.0.0) 58 , using the function compareCluster with extra arguments fun = ‘enrichGO’, OrgDb = ‘org.Hs.eg.db’, keyType = ‘SYMBOL’ and ont = ‘BP’.
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### Spatial joint profiling of DNA methylome and transcriptome in tissues. (Nature 2025)

- DOI: 10.1038/s41586-025-09478-x | PMCID: PMC12571926 | PMID: 40903587
- Evidence: GO enrichment analysis was conducted using the enrichGO function from clusterProfiler package 64 (v.4.2).
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [Python, R, UMAP, clusterProfiler, pheatmap] -> visualisation [Python] -> stage not stated [HOMER, Seurat]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Pathway was analysed using clusterProfiler 79 .
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Evidence: Gene set enrichment or pathway analysis were performed using clusterProfiler 69 and Camera 70 against the Gene Ontology database, KEGG database and HALLMARK C2 and C7 gene sets in the MSigDB (v7.5). scRNA-seq Peritoneal B cells (CD19 + CD3 − 7AAD − ) from three 8-week-old mice, B-1Ps (Lin − CD93 + IgM − CD19 + B220 low/−) from embryonic day 18.5 fetal livers (three fetal livers were pooled togethe...
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Version used: **4.8.3**
- Evidence: For HALLMARK pathway enrichment analysis, differentially expressed genes were tested if over-represented against the HALLMARK pathways from the MSigDB using R packages msigdbr (v.7.5.1) and clusterProfiler (v.4.8.3).
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: We applied the enricher function from the R package clusterProfiler 66 on each cluster for enrichment analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Version used: **4.10.0**
- Evidence: The significant (adjusted P < 0.05) cluster marker genes were subjected to GO enrichment analysis performed with the clusterProfiler v.4.10.0 package 73 .
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: GSEA was done using the clusterProfiler R package (v.4.0.5) 62 and the Benjamini–Hochberg method was used to calculate the adjusted P values.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Version used: **4.4.4**
- Evidence: Gene Ontology and gene set enrichment analysis Over-representation and gene set enrichment analysis were conducted using clusterProfiler (v4.4.4).
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Version used: **4.2.2**
- Evidence: The session used the following libraries: DESeq2 (1.34.0), png (0.1-7), apeglm (1.16.0), reshape2 (1.4.4), magrittr (2.0), edgeR (3.36.0), Matrix.utils (0.9.8), enrichplot (1.14.1), ggpubr (0.4.0), GO.db (3.14.0), clusterProfiler (4.2.2), genesorteR (0.4.3), RColorBrewer (1.1-2), slingshot (2.2.0), TrajectoryUtils (1.2.0), princurve (2.1.6), scRNAseq (2.8.0), pathview (1.34.0), limma (3.50.0), dyn...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **4.12.6**
- Evidence: We then used the R package clusterProfiler (v.4.12.6) 79 to carry out an overrepresentation analysis of the differentially expressed genes based on KEGG annotations.
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Version used: **4.6.2**
- Evidence: A ranked list of coding genes was generated based on the Wald statistic in DESeq2, and subsequently processed by GSEA 55 using the R package clusterProfiler (v.4.6.2) 56 against the Hallmark gene sets from Molecular Signature Database (MSigDB) 57 to identify significantly enriched pathways.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: Each set of DEGs was subjected to an over-representation analysis to identify enriched GO terms, HALLMARK pathways and KEGG pathways using the respective functions in clusterProfiler 66 .
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Bar colour denotes −log 10 -adjusted P value, calculated by gseGO in the clusterProfiler package. f , Glycolysis (left) and hypoxia (right) signatures in LOY SCR ( n = 73,576) versus WTY SCR ( n = 83,453) epithelial cells.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: Subsequently, we conducted cell-type-aware immune response enrichment analysis using the hypergeometric test (FDR < 0.05) through the enricher function in the clusterProfiler R package 71 .
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Evidence: 155 , and was performed using the clusterProfiler R package (RRID:SCR_016884) with brain-expressed genes as background.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: Enriched pathways per cluster were generated using the enrichGO function of the clusterProfiler Bioconductor R package 73 or the Enrichr gene list enrichment analysis tool 74 , using the marker genes identified per cluster from the FindMarkers() function.
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Version used: **4.9.2**
- Evidence: The GSEA dot plot was generated by plotting key pathways from the GSEA results using the dotplot function from clusterProfiler 4.9.2 package.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: We then used msigdbr and clusterProfiler R packages to identify chromosomal loci of the differentially expressed genes.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Version used: **4.6.2**
- Evidence: Gene Ontology (GO) enrichment analysis of these genes was performed in the R package clusterProfiler (v.4.6.2), with P ≤ 0.05 as the threshold for significance.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Evidence: Analysis also included the following R packages: coloc v.5.2.2 ( https://rdrr.io/cran/coloc/man/coloc.abf.html ), ClusterProfiler64 v.4.8.2 ( https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html ), susieR package62 v.0.12.27, R v.4.2.163 ( https://cran.r-project.org/web/packages/susieR/index.html ).
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### Spatially resolved mapping of cells associated with human complex traits. (Nature 2025)

- DOI: 10.1038/s41586-025-08757-x | PMCID: PMC12095064 | PMID: 40108460
- Evidence: The module score of these 417 drug targets genes for individual spots was computed using the AddModuleScore function in the Seurat (V4.4.0) R package with the default settings 83 , 84 GO term enrichment We performed GO term enrichment analysis using the clusterProfiler 85 (V3.18) R package with the default settings.
- Full pipeline: alignment/mapping [R] -> variant calling [GCTA] -> normalisation [Scanpy] -> dimensionality reduction/clustering [PLINK, Seurat, clusterProfiler] -> differential/statistical testing [MAGMA] -> simulation/modelling [PLINK] -> stage not stated [LDSC]

### Drivers of avian genomic change revealed by evolutionary rate decomposition. (Nature 2025)

- DOI: 10.1038/s41586-025-08777-7 | PMCID: PMC12119353 | PMID: 40108459
- Evidence: Gene identities were inferred using the best blastn match 85 and used as input for testing enrichment of KEGG terms using clusterProfiler 86 .
- Full pipeline: dimensionality reduction/clustering [BLAST, clusterProfiler] -> differential/statistical testing [brms] -> structure determination [phytools] -> visualisation [phytools] -> stage not stated [IQ-TREE v2.1.2, R]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Evidence: Gene Ontology over-representation analysis was performed using the clusterProfiler 79 package (v.3.16.1).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Evidence: The resulting moderated t- statistics of each gene were ranked and used as the input for gene set enrichment analysis (GSEA) using the R package clusterProfiler 65 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: GO enrichment analysis was performed for these candidates for each TF using the enrichGO function of clusterProfiler with org.At.tair.db annotation.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: Gene set enrichment analysis was performed with clusterProfiler 61 (v4.10.1) using msigdbr (v7.5.1) on all human gene sets.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **3.14.3**
- Evidence: Gene Ontology enrichment analysis was performed using clusterProfiler (v3.14.3), and circus-plots were generated using circlise (v0.4.8).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Version used: **4.4.4**
- Evidence: Differential gene expression analysis on raw counts was performed using DESeq2, over-representation analysis with clusterProfiler v.4.4.4 and gene set enrichment analysis with fgsea v.1.22.0.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Endogenous self-peptides guard immune privilege of the central nervous system. (Nature 2025)

- DOI: 10.1038/s41586-024-08279-y | PMCID: PMC11666455 | PMID: 39476864
- Evidence: For each gene set, genes were separated into up- and downregulated and separately 48 the enrichGO function from the clusterProfiler package was used with a gene set size set between 10 and 500 genes and P values adjusted using Benjamini–Hochberg correction 49 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR, limma] -> stage not stated [Seurat]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **4.12.0**
- Evidence: Functional enrichment of genes upregulated during early embryogenesis (≤E10) and downregulated afterwards, or vice versa, was performed using Fisher’s exact test for GO Biological Process ontology with enrichGO function from clusterProfiler (v4.12.0) package 259 , using all genes expressed in this dataset as background.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Version used: **4.14.6**
- Evidence: Biological pathways associated with SE consensus markers To identify biological pathways associated with SE consensus markers, we performed overlap analysis using the enricher function from the clusterProfiler (v.4.14.6) R package 84 .
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **4.14.6**
- Evidence: Statistically overrepresented GO terms and pathways were identified using clusterProfiler (v.4.14.6) 65 and the PANTHER database 66 . scRNA-seq data of CD45-sorted immune cells were mapped to the mouse reference mm10 (v.1.2.0) using 10x Genomics Cell Range (v.7.2.0).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### Dynamics of genetic and somatic trade-offs in ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10407-9 | PMCID: PMC13253337 | PMID: 42020758
- Evidence: For each locus we tested set over-representation against our filtered whole-genome background ( n = 18,830) using clusterProfiler for Gene Ontology (Biological Process, Molecular Function, Cellular Component), KEGG pathways and Reactome pathways.
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.3.4.1] -> variant calling [BCFtools, R v4.0] -> dimensionality reduction/clustering [PLINK, TwoSampleMR v0.6.2, clusterProfiler] -> stage not stated [SAMtools v1.6]

### H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; repurposes plant O&lt;sub&gt;2&lt;/sub&gt; sensing to regulate post-hypoxia responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10366-1 | PMCID: PMC13216066 | PMID: 42020755
- Evidence: Gene ontology enrichment analysis of the differentially expressed genes was conducted using clusterProfiler 77 (v.4.10.1).
- Full pipeline: quality control [FastQC, featureCounts] -> alignment/mapping [FastQC, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR] -> stage not stated [ImageJ, R v4.3.1]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **4.14.0**
- Evidence: Pre-rank gene set enrichment analysis was performed for each comparison using clusterProfiler (v.4.14.0) 85 , incorporating gene ontologies for biological processes, molecular functionality and cellular components.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **4.8.3**
- Evidence: Library preparation (directional messenger RNA; poly-A enrichment) and sequencing (NovaSeq X Plus Series PE150) were performed at Novogene and data were analysed with DESeq2 (v.1.38.3) and clusterProfiler (v.4.8.3) with method fgsea (v.1.24.0).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **4.12.6**
- Evidence: GO enrichment analysis GO enrichment analysis was performed using the clusterProfiler (v.4.12.6) 124 on a given gene list.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Expansion of outer cortical CUX2 neurons requires adaptations for DNA repair. (Nature 2026)

- DOI: 10.1038/s41586-026-10290-4 | PMCID: PMC13190340 | PMID: 41922774
- Evidence: Pathway and gene ontology enrichment analyses were done using the clusterProfiler R package (v.4.14.6), restricted to the biological process category and the top ten activated and suppressed pathways.
- Full pipeline: variant calling [UMAP] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [R, Scanpy v1.8.1, UMAP, clusterProfiler]

### Thymic health and immunotherapy outcomes in patients with cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10243-x | PMCID: PMC13102699 | PMID: 41851467
- Evidence: Enrichment score was calculated using the clusterProfiler package (v.4.2.0), using pathways that included at least ten genes.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> stage not stated [STRING db]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Evidence: To identify biological terms that are over-represented in a specific gene set, we performed GO and GSEA analysis using the enrichGO and gseGO functions, respectively, from the clusterProfiler package (v.4.6.2) 59 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Evidence: We used the enrichGO function from the clusterProfiler 89 package (v.4.10.0) to determine the overrepresentation of Gene Ontology (GO) terms across Biological Process, Molecular Function and Cellular Component 90 .
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **1.38.3**
- Evidence: Upregulated genes of St.3, St.4, St.14 and St.31 were used for enrichment analysis using the enricher function of clusterProfiler v.1.38.3 (ref.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Version used: **4.10.1**
- Evidence: Gene Ontology analyses Gene Ontology analyses were performed using clusterProfiler v.4.10.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Evidence: Functional enrichment analysis Functional enrichment was performed separately for each gene module using over-representation analysis with the clusterProfiler R package v.4.12.6 (ref.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### In vivo base editing of Chd3 rescues behavioural abnormalities in mice. (Nature 2026)

- DOI: 10.1038/s41586-026-10113-6 | PMCID: PMC12999480 | PMID: 41708849
- Evidence: Gene ontology enrichment and KEGG analysis of differentially expressed genes was implemented by the clusterProfiler R package, in which gene length bias was corrected 51 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> stage not stated [GSEA]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Version used: **4.0.5**
- Evidence: Pathway enrichment analysis The enriched functional terms in this study were analysed by the R package clusterProfiler v.4.0.5.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **4.0.5**
- Evidence: Module gene-ontology term enrichment was performed using clusterProfiler (v.4.0.5) 128 with default parameters.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: Pathway enrichment analyses were performed using the same ExWAS gene set via the clusterProfiler R package 69 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Version used: **4.12.0**
- Evidence: Genes were ranked by surprisal analysis scores and analysed separately for association with modules 1 and 2 using the R package clusterProfiler (v.4.12.0) 69 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: Gene set enrichment analysis (GSEA) was conducted using the clusterProfiler package, leveraging gseKEGG, gseGO and gsePathway for pathway enrichment analysis 75 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: The clusterProfiler package (v.4.10.0) was used to perform GSEA and ORA 55 .
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: We utilized enrichGO and enricher functions in clusterProfiler 90 package in R for the analysis.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: Differentially expressed genes were ranked by log 2 (fold change expression) and used for gene set enrichment analysis (GSEA) on the Hallmark gene set from msigdbr (v.7.5.1), a previously published GR-activity signature 16 or a newly developed PR-activity signature 17 (Extended Data Table 3 ), using clusterProfiler 57 (v.3.18.1), (pvalueCutoff = 0.05, pAdjustMethod = “BH”).
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Version used: **3.14.3**
- Evidence: GSEA was based on clusterProfiler (v.3.14.3) R package 73 . log 2 (fold change) was calculated between the mature M cells and enterocytes.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Pathway enrichment analysis Gene Ontology (GO) and Reactome pathway enrichment analyses for both scRNA-seq and ST data were conducted using the clusterProfiler R package 73 (v.4.12.6).
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: These annotations were used to test enrichment using over-representation analysis (ORA) of sets of genes associated with expression level categories with the R package clusterProfiler 66 (v.4.6) and a Benjamini–Hochberg FDR correction P value cut-off of 0.05.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Defective cytokinin signaling reprograms lipid and flavonoid gene-to-metabolite networks to mitigate high salinity in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2105021118 | PMCID: PMC8640937 | PMID: 34815339
- Evidence: The Arabidopsis Genome Initiative (AGI) of the DEGs were mapped into the Arabidopsis “ath” KEGG reference database using the “clusterProfiler” and “pathview” packages in R v3.5.1 ( 93 ) to identify the key metabolic pathways associated with the identified DEGs.
- Full pipeline: alignment/mapping [clusterProfiler] -> variant calling [ggplot2] -> dimensionality reduction/clustering [R v3.5, clusterProfiler] -> visualisation [Cytoscape, igraph]

### Single-cell sequencing reveals suppressive transcriptional programs regulated by MIS/AMH in neonatal ovaries. (PNAS 2021)

- DOI: 10.1073/pnas.2100920118 | PMCID: PMC8157966 | PMID: 33980714
- Evidence: Differentially expressed genes with at least twofold changes between the MIS-treated granulosa cells and controls were used as input for Gene Ontology Enrichment Analysis by clusterProfiler ( 50 ).
- Full pipeline: read trimming [R, Seurat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [CellPhoneDB, CellProfiler]

### TBK1 recruitment to STING activates both IRF3 and NF-κB that mediate immune defense against tumors and viral infections. (PNAS 2021)

- DOI: 10.1073/pnas.2100225118 | PMCID: PMC8040795 | PMID: 33785602
- Evidence: The KEGG pathway enrichment analysis was done using the R package clusterProfiler ( 64 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [R v4.0.2, ggplot2]

### High-salt diet suppresses autoimmune demyelination by regulating the blood-brain barrier permeability. (PNAS 2021)

- DOI: 10.1073/pnas.2025944118 | PMCID: PMC7999868 | PMID: 33723078
- Version used: **3.14.3**
- Evidence: For both mRNA-seq and proteomics data, overrepresented gene ontology (GO) gene sets (the “Biological Process” category) among differentially expressed genes or proteins were detected using clusterProfiler (version 3.14.3) ( 36 ) and filtered by semantic similarity (using an information content-based method by Schlicker et al.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [DESeq2 v1.26.1, kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.1, clusterProfiler v3.14.3, limma] -> visualisation [pheatmap, tidyverse]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Evidence: The list of differentially expressed genes detected by DESeq2 (basemean > 5 and fold-change < 0.25, or basemean > 5 and fold-change > 4) were used for GO enrichment analysis by clusterProfiler package ( 41 ).
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### Inflammatory response to retrotransposons drives tumor drug resistance that can be prevented by reverse transcriptase inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2213146119 | PMCID: PMC9894111 | PMID: 36449545
- Evidence: Kyoto Encyclopedia of Genes and Genomes (KEGG) enrichment was performed with R clusterProfiler package software ( 54 ) and presented as dot plots, with the dot size representing gene count enriched in the pathway, and the dot color showing the enrichment significance.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [featureCounts]

### Conservation at the uterine-placental interface. (PNAS 2022)

- DOI: 10.1073/pnas.2210633119 | PMCID: PMC9565169 | PMID: 36191208
- Version used: **3.16.1**
- Evidence: To explore gene set functions, we carried out GO enrichment analysis using the R package clusterProfiler (version 3.16.1) ( 50 ).
- Full pipeline: quality control [R, Seurat v4.1.0] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v3.16.1] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, MACS2]

### FGFR redundancy limits the efficacy of FGFR4-selective inhibitors in hepatocellular carcinoma. (PNAS 2022)

- DOI: 10.1073/pnas.2208844119 | PMCID: PMC9546626 | PMID: 36179047
- Evidence: Gene ontology analysis of differentially expressed genes was performed with clusterProfiler ( 40 ).
- Full pipeline: alignment/mapping [DESeq2] -> quantification [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [pheatmap]

### Ectopic expression of meiotic cohesin generates chromosome instability in cancer cell line. (PNAS 2022)

- DOI: 10.1073/pnas.2204071119 | PMCID: PMC9549395 | PMID: 36179046
- Evidence: For GO analysis/clustering and pathway mapping, ClusterProfiler ( https://guangchuangyu.github.io/software/clusterProfiler ) and KEGG portal ( https://genome.jgi.doe.gov/portal/ ) were used.
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, clusterProfiler] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [BEDTools, MACS2 v2.2, RepeatMasker]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Evidence: The clusterProfiler package ( 95 ) in R was used for KEGG pathway category analysis.
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Monosomy X in isogenic human iPSC-derived trophoblast model impacts expression modules preserved in human placenta. (PNAS 2022)

- DOI: 10.1073/pnas.2211073119 | PMCID: PMC9546589 | PMID: 36161909
- Evidence: GSEA using clusterProfiler ( 111 ) was performed on all genes ranked by DESeq2’s Wald statistic in three separate conditions, as well as the average of their quantile-normalized Wald scores to ensure equal weighting.
- Full pipeline: normalisation [GSEA, clusterProfiler] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler] -> stage not stated [WGCNA]

### Uridylation and the SKI complex orchestrate the Calvin cycle of photosynthesis through RNA surveillance of <i>TKL1</i> in Arabidopsis. (PNAS 2022)

- DOI: 10.1073/pnas.2205842119 | PMCID: PMC9499578 | PMID: 36095196
- Evidence: Gene Ontology term and Kyoto Encyclopedia of Genes and Genomes pathway enrichment analyses were performed using the R package clusterProfiler. sRNA Library Construction and Sequencing.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: We used clusterProfiler for gene ontology enrichment analysis ( 67 ).
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### Tumor-polarized GPX3&lt;sup&gt;+&lt;/sup&gt; AT2 lung epithelial cells promote premetastatic niche formation. (PNAS 2022)

- DOI: 10.1073/pnas.2201899119 | PMCID: PMC9371733 | PMID: 35914155
- Version used: **3.14.0**
- Evidence: Gene Ontology, Kyoto encyclopedia of genes and genomes (KEGG), and GSEA pathway enrichment analyses of differentially expressed genes (DEGs) were performed by clusterProfiler (v 3.14.0) package.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Monocle, clusterProfiler v3.14.0] -> differential/statistical testing [GSEA, clusterProfiler v3.14.0] -> stage not stated [Seurat v3.0.2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Evidence: To find pathways enriched in the ZR FUS shared and Sox9-specific sites, Kyoto Encyclopedia of Genes and Genomes enrichment analysis was performed using clusterProfiler, with a P value cutoff of 0.05 ( 46 ).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### The global succinylation of SARS-CoV-2-infected host cells reveals drug targets. (PNAS 2022)

- DOI: 10.1073/pnas.2123065119 | PMCID: PMC9335334 | PMID: 35858407
- Evidence: We performed enrichment analysis of gene ontology and Kyoto Encyclopedia of Genes and Genomes pathways via ClueGo ( 49 ) or clusterProfiler package in R (4.0.4) with default parameters ( 50 ).
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [R v4.0.4, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Version used: **4.0.0**
- Evidence: Enriched GO terms were identified using the packages clusterProfiler (v.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### Nuclear speckle integrity and function require TAO2 kinase. (PNAS 2022)

- DOI: 10.1073/pnas.2206046119 | PMCID: PMC9231605 | PMID: 35704758
- Evidence: Gene set enrichment analysis of the KEGG database was performed using the clusterProfiler package ( 49 ).
- Full pipeline: quality control [STAR] -> read trimming [STAR, Trimmomatic] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor v3.11, R v4.0.2]

### Caspase-4/11 exacerbates disease severity in SARS-CoV-2 infection by promoting inflammation and immunothrombosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202012119 | PMCID: PMC9173818 | PMID: 35588457
- Evidence: Functional enrichment was performed with Ingenuity Pathway Analysis (Qiagen) to enrich for IPA Canonical Pathways, “clusterProfiler” to generate enrichment maps ( 55 ), and EnrichR ( 59 ).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [limma] -> visualisation [DESeq2] -> stage not stated [ComplexHeatmap]

### MoSBi: Automated signature mining for molecular stratification and subtyping. (PNAS 2022)

- DOI: 10.1073/pnas.2118210119 | PMCID: PMC9169782 | PMID: 35412913
- Evidence: Gene set/pathway enrichment was performed using the “clusterProfiler” R package using the “enrichGO” (biological process enrichment) and “enrichKEGG” functions.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [Cytoscape, Docker, R]

### Hemogenic and aortic endothelium arise from a common hemogenic angioblast precursor and are specified by the Etv2 dosage. (PNAS 2022)

- DOI: 10.1073/pnas.2119051119 | PMCID: PMC9060440 | PMID: 35333649
- Evidence: GO analysis was performed with the clusterProfiler package (v.3.16.1) using the top 100 marker genes.
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, R v4.0.2, Seurat]

### A vasculature niche orchestrates stromal cell phenotype through PDGF signaling: Importance in human fibrotic disease. (PNAS 2022)

- DOI: 10.1073/pnas.2120336119 | PMCID: PMC9060460 | PMID: 35320046
- Evidence: GO enrichment of cluster markers and differentially expressed genes was performed using the R package clusterProfiler ( 38 ) with a Benjamini–Hochberg (BH) multiple testing adjustment and a false-discovery rate (FDR) cutoff of 0.1, using all expressed genes expressed in >3 cells as background.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [CellPhoneDB, R, Seurat]

### Phosphonate production by marine microbes: Exploring new sources and potential function. (PNAS 2022)

- DOI: 10.1073/pnas.2113386119 | PMCID: PMC8931226 | PMID: 35254902
- Version used: **3.8**
- Evidence: Significant enrichment of Kyoto Encyclopedia of Genes and Genomes pathways was determined using the hypergeometric test ( 110 ) implemented in clusterProfiler version 3.8 ( 111 ).
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler v3.8] -> stage not stated [HMMER v3.1b, eggNOG v4.5.1]

### The life history of &lt;i&gt;Drosophila&lt;/i&gt; sperm involves molecular continuity between male and female reproductive tracts. (PNAS 2022)

- DOI: 10.1073/pnas.2119899119 | PMCID: PMC8931355 | PMID: 35254899
- Version used: **4.0**
- Evidence: Functional enrichment was examined using clusterProfiler version 4.0 ( 81 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.0]

### Engineering and functional analysis of yeast with a monotypic 40S ribosome subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2114445119 | PMCID: PMC8833219 | PMID: 35105807
- Evidence: GO enrichment analysis of differentially expressed gene was implemented by the clusterProfiler R package.
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> variant calling [GATK v3.5, SnpEff] -> registration [GATK v3.5] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [Picard]

### TRIM14 inhibits OPTN-mediated autophagic degradation of KDM4D to epigenetically regulate inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2113454119 | PMCID: PMC8851536 | PMID: 35145029
- Version used: **4.0.5**
- Evidence: Enrichment analysis was performed by clusterProfiler (v4.0.5).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5] -> dimensionality reduction/clustering [clusterProfiler v4.0.5] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.6, Picard]

### A distinct role of STING in regulating glucose homeostasis through insulin sensitivity and insulin secretion. (PNAS 2022)

- DOI: 10.1073/pnas.2101848119 | PMCID: PMC8851542 | PMID: 35145023
- Evidence: GO and pathway grouping and enrichment studies were performed by clusterProfiler (V3.16.1) ( 49 ), and pathway visualization was conducted using pathview (v1.28.1) ( 50 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1] -> alignment/mapping [Bowtie2 v2.3.5.1] -> quantification [HOMER v4.11.1] -> normalisation [HOMER v4.11.1] -> dimensionality reduction/clustering [clusterProfiler, pheatmap v1.0.12] -> visualisation [clusterProfiler, pheatmap v1.0.12]

### The m<sup>6</sup>A reader YTHDC2 is essential for escape from KSHV SOX-induced RNA decay. (PNAS 2022)

- DOI: 10.1073/pnas.2116662119 | PMCID: PMC8872733 | PMID: 35177478
- Evidence: ( D ) Heat map of the most significant m 6 A-enriched functional pathways in latent and lytic cells calculated through an enrichment analysis preformed using the R package clusterProfiler.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [HOMER]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway enrichment analysis using the R Bioconductor clusterProfiler package ( 48 ) with a Benjamini–Hochberg adjusted P value cutoff of 0.05 for the genes that were cobound by BRD4, LSD1, and MTA3 revealed that the BRD4/LSD1/NuRD complex–directed super-enhancers influence several prominent cellular signaling pathways, including autophagy, Hippo, and ...
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Evidence: Gene set enrichment analyses were performed with the clusterProfiler Bioconductor package ( 57 ), using the hypergeometric test to assess enrichment of marginally significant DEGs (at P < 0.005) that were stratified by case–control directionality, against a background of all expressed genes that had Entrez gene IDs.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### Convergent evolution of venom gland transcriptomes across Metazoa. (PNAS 2022)

- DOI: 10.1073/pnas.2111392119 | PMCID: PMC8740685 | PMID: 34983844
- Evidence: KEGG pathway and GO enrichment analyses of all isa modules were performed with clusterProfiler ( 49 ) based on human gene annotation after converting the OrthoDB ClusterId to NCBI EntrezId using the OG2gene file at the Metazoa node obtained from the OrthoDB data page.
- Full pipeline: quality control [kallisto] -> read trimming [kallisto] -> alignment/mapping [RAxML] -> quantification [kallisto] -> normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [Bioconductor, InterProScan]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: GO enrichment analysis was carried out using the clusterProfiler package in R and AgriGO ( http://bioinfo.cau.edu.cn/agriGO/ ).
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### Transcriptional signatures of early-life stress and antidepressant treatment efficacy. (PNAS 2023)

- DOI: 10.1073/pnas.2305776120 | PMCID: PMC10710023 | PMID: 38011563
- Evidence: Gene ontology analysis utilized “clusterProfiler,” “org.Hs.eg.db,” and “org.Mm.eg.db” packages ( 66 , 67 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, limma]

### Microbiota configuration determines nutritional immune optimization. (PNAS 2023)

- DOI: 10.1073/pnas.2304905120 | PMCID: PMC10710091 | PMID: 38011570
- Evidence: Fold changes with associated genes were ranked for GSEA testing using the clusterProfiler package ( https://www.sciencedirect.com/science/article/pii/S2666675821000667 ).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Bowtie2 v2.4.2, HOMER, HUMAnN v3.0, QIIME 2 v2020.2]

### Substances in the mandibular glands mediate queen effects on larval development and colony organization in an annual bumble bee. (PNAS 2023)

- DOI: 10.1073/pnas.2302071120 | PMCID: PMC10636365 | PMID: 37903277
- Evidence: We analyzed the proteins that are significantly more abundant in the queen regurgitate produced by a t -test with permutation-based FDR correction ( P < 0.1) using the clusterProfiler package ( 68 ) in R version 4.2.2.
- Full pipeline: dimensionality reduction/clustering [R v4.2.2, clusterProfiler] -> differential/statistical testing [R v4.2.2, clusterProfiler]

### Hemispheric asymmetry in cortical thinning reflects intrinsic organization of the neurotransmitter systems and homotopic functional connectivity. (PNAS 2023)

- DOI: 10.1073/pnas.2306990120 | PMCID: PMC10589642 | PMID: 37831741
- Evidence: We then conducted GO enrichment analysis on these two gene lists using the "clusterProfiler" R package ( 47 ).
- Full pipeline: quality control [FSL, MRIQC v0.15.0, fMRIPrep v1.3.2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R v4.2.2] -> stage not stated [FreeSurfer v6.0.0]

### Downregulation of apoptotic repressor <i>AVEN</i> exacerbates cardiac injury after myocardial infarction. (PNAS 2023)

- DOI: 10.1073/pnas.2302482120 | PMCID: PMC10589712 | PMID: 37816050
- Evidence: The enrichment analysis was performed by clusterProfiler ( 53 ).
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Version used: **4.2.2**
- Evidence: Then, clusterProfiler (v4.2.2) and org.Mm.eg.db (v3.14.0) were used to translate biological IDs.
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus. (PNAS 2023)

- DOI: 10.1073/pnas.2310163120 | PMCID: PMC10515167 | PMID: 37703282
- Evidence: GO enrichment analysis was performed using R package, clusterProfiler, with TAIR10 annotation as the background.
- Full pipeline: quality control [R, Seurat v4.1.0] -> alignment/mapping [STAR] -> normalisation [R, Seurat v4.1.0] -> dimensionality reduction/clustering [R, Seurat v4.1.0, UMAP, clusterProfiler] -> stage not stated [Monocle, velocyto]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: Gene set enrichment analyses (GSEAs) were performed on lists of differentially expressed genes (DEGs) for GO BP term enrichment without cutoffs using clusterProfiler ( 41 ) and fold change calculations from DESeq2.
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### Nasal administration of anti-CD3 monoclonal antibody ameliorates disease in a mouse model of Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2309221120 | PMCID: PMC10500187 | PMID: 37669383
- Version used: **4.6.2**
- Evidence: Statistically significant up- and down-regulated genes were separated, and R package clusterProfiler (v4.6.2)’s enrichGO function was used for pathway analysis.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler v4.6.2] -> differential/statistical testing [R, clusterProfiler v4.6.2] -> stage not stated [ImageJ]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Evidence: For the enrichment analysis, hallmark gene sets ( 56 ) were used in a gene set enrichment analysis using clusterProfiler R package v4.8.0 ( 57 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### Activin E-ACVR1C cross talk controls energy storage via suppression of adipose lipolysis in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2309967120 | PMCID: PMC10410708 | PMID: 37523551
- Evidence: Pathway enrichment analysis was performed using the clusterProfiler package ( 55 ).
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2]

### MicroRNA-335-5p suppresses voltage-gated sodium channel expression and may be a target for seizure control. (PNAS 2023)

- DOI: 10.1073/pnas.2216658120 | PMCID: PMC10372546 | PMID: 37463203
- Evidence: Pathway enrichment analysis of the remaining 267 MTIs ( Dataset S3 ) was performed using the ReactomePA ( 74 ) and clusterProfiler ( 75 ) packages, with an adjusted p-value (Benjamini–Hochberg) <0.05 considered significant ( Dataset S4 ).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [ComplexHeatmap, DESeq2, R, tidyverse]

### Sex-specific and opposed effects of FKBP51 in glutamatergic and GABAergic neurons: Implications for stress susceptibility and resilience. (PNAS 2023)

- DOI: 10.1073/pnas.2300722120 | PMCID: PMC10266018 | PMID: 37252963
- Evidence: GO enrichment analysis of DEGs was implemented by the clusterProfiler R package.
- Full pipeline: variant calling [SPM] -> dimensionality reduction/clustering [R, clusterProfiler]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Version used: **4.2.2**
- Evidence: Gene Ontology (GO) ( 58 ) and Kyoto Encyclopedia of Genes and Genomes (KEGG) ( 59 ) enrichment analyses were performed with the R package clusterProfiler version 4.2.2 ( 60 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Consequences of poly(ethylene oxide) and poloxamer P188 on transcription in healthy and stressed myoblasts. (PNAS 2023)

- DOI: 10.1073/pnas.2219885120 | PMCID: PMC10161009 | PMID: 37094151
- Evidence: Gene set enrichment analysis was accomplished through the clusterProfiler package with the genome specified as org.Mm.eg.db ( 64 – 67 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [GSEA, STRING db]

### Identification of hidden associations among eukaryotic genes through statistical analysis of coevolutionary transitions. (PNAS 2023)

- DOI: 10.1073/pnas.2218329120 | PMCID: PMC10120013 | PMID: 37043529
- Evidence: The enrichment analysis was performed with the GSEA function of the clusterProfiler R library ( 65 ).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Python, RAxML v8.2.12]

### Phosphatidylserine-positive extracellular vesicles boost effector CD8<sup>+</sup> T cell responses during viral infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210047120 | PMCID: PMC10120060 | PMID: 37040405
- Evidence: GSEA were conducted with “clusterProfiler” (version 3.18.1) on the statistic reported by DEseq2.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler]

### Mutant β<sub>1</sub>-adrenergic receptor improves REM sleep and ameliorates tau accumulation in a mouse model of tauopathy. (PNAS 2023)

- DOI: 10.1073/pnas.2221686120 | PMCID: PMC10104526 | PMID: 37014857
- Evidence: GO enrichment analysis of DEGs was performed using the clusterProfiler R package (version 3.8.1), and GO terms with adjusted P values < 0.05 were considered significantly enriched by DEGs.
- Full pipeline: quantification [featureCounts v1.5.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### E2F regulation of the <i>Phosphoglycerate kinase</i> gene is functionally important in <i>Drosophila</i> development. (PNAS 2023)

- DOI: 10.1073/pnas.2220770120 | PMCID: PMC10104548 | PMID: 37011211
- Evidence: A gene set enrichment analysis was performed using clusterProfiler ( 35 ) to determine the overrepresentation of gene ontology terms among the 513 regions that showed a significant reduction in chromatin accessibility in Pgk ΔE2F mutants.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler]

### Neuron-specific transcriptomic signatures indicate neuroinflammation and altered neuronal activity in ASD temporal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2206758120 | PMCID: PMC10013873 | PMID: 36862688
- Evidence: Gene ontology (GO) enrichment was performed using the gProfileR R package ( 80 ) and the fGSEA algorithm as implemented in the clusterProfiler R package ( 81 ).
- Full pipeline: quantification [featureCounts v1.6.4] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [DESeq2 v1.22.2, GSEA, WGCNA]

### Time of day determines postexercise metabolism in mouse adipose tissue. (PNAS 2023)

- DOI: 10.1073/pnas.2218510120 | PMCID: PMC9974500 | PMID: 36780527
- Evidence: Gene ontology (GO) enrichment analysis was performed utilizing clusterProfiler and molecular function GO terms, with all detected genes serving as background.
- Full pipeline: alignment/mapping [featureCounts v1.6.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [R]

### Epigenetic function during heroin self-administration controls future relapse-associated behavior in a cell type-specific manner. (PNAS 2023)

- DOI: 10.1073/pnas.2210953120 | PMCID: PMC9963300 | PMID: 36745812
- Evidence: The package clusterProfiler was used for the gene ontology analysis ( 49 ).
- Full pipeline: variant calling [limma] -> dimensionality reduction/clustering [ImageJ, clusterProfiler] -> differential/statistical testing [limma]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: Gene ontology over-representation and gene set enrichment analysis (GSEA) were conducted using the clusterProfiler package ( 29 ) with a GO level of 3 and fgsea package ( 30 ) with the Reactome database, respectively.
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Sec22b is a critical and nonredundant regulator of plasma cell maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2213056120 | PMCID: PMC9926242 | PMID: 36595686
- Evidence: GSEA was performed by the clusterProfiler::GSEA function using the fgsea algorithm.
- Full pipeline: read trimming [Bioconductor, edgeR] -> alignment/mapping [Bioconductor, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [GSEA, clusterProfiler, fgsea] -> differential/statistical testing [Bioconductor, R, edgeR, limma]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: GO analysis was performed using significantly up- or down-regulated genes and the enrichGO function from the clusterProfiler package with biological process ontologies, and top 20 genes ordered by gene ratio were plotted.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Accelerated cell-type-specific regulatory evolution of the human brain. (PNAS 2024)

- DOI: 10.1073/pnas.2411918121 | PMCID: PMC11670112 | PMID: 39680759
- Evidence: We used the package clusterProfiler and the function enrichGO() to enrich GO terms for each list of genes.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [Seurat]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: Pathway analysis/GSEA was performed using clusterProfiler (60) or fgsea.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### A comprehensive transcriptome characterization of individual nuclear receptor pathways in the human small intestine. (PNAS 2024)

- DOI: 10.1073/pnas.2411189121 | PMCID: PMC11551338 | PMID: 39475639
- Evidence: Volcano plots were generated with the R package EnhancedVolcano and GO term analysis was performed using R package clusterProfiler ( 74 , 75 ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [pheatmap]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: Gene set enrichment analysis (GSEA) ( 55 ), focused on Gene Ontology ( 56 ), was conducted using the R 4.3.1 Bioconductor package clusterProfiler ( 57 ) to elucidate whole transcriptomic patterns between groups.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Evidence: ( A ) Core pathway enrichment with identified putative immune evasion genes for each model using clusterProfiler.
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: To assess the enrichment of GO terms and KEGG pathways, we carried out a hypergeometric test using the R package clusterProfiler ( 48 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Evidence: Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway enrichment analyses were performed in R with the package “clusterProfiler” ( 90 , 91 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### Mitochondrial antioxidants abate SARS-COV-2 pathology in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2321972121 | PMCID: PMC11287122 | PMID: 39008677
- Evidence: GO data were generated using “clusterProfiler” (version 4.6.2), “AnnotationDbi” (version 1.60.1), and “org.Mm.eg.db” (version 3.16.0) packages in R.
- Full pipeline: quantification [DESeq2, R v4.2.2] -> normalisation [DESeq2, R v4.2.2] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ComplexHeatmap, GSEA v4.3.2, ggplot2]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: PANTHER Classification System ( 52 ) and clusterProfiler ( 53 ) were used for GO analysis.
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### Transfection of entomopathogenic <i>Metarhizium</i> species with a mycovirus confers hypervirulence against two lepidopteran pests. (PNAS 2024)

- DOI: 10.1073/pnas.2320572121 | PMCID: PMC11214047 | PMID: 38885380
- Evidence: A gene ontology (GO) enrichment analysis of the DEGs was implemented using the R package clusterProfiler ( http://bioconductor.org/packages/release/bioc/html/clusterProfiler.html ), in which gene length bias was corrected ( 66 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [ggplot2] -> quantification [ggplot2] -> dimensionality reduction/clustering [clusterProfiler, ggplot2] -> stage not stated [BLAST, DESeq2, R, pheatmap]

### Single-tissue proteomics in <i>Caenorhabditis elegans</i> reveals proteins resident in intestinal lysosome-related organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2322588121 | PMCID: PMC11194598 | PMID: 38861598
- Evidence: For GO enrichment analysis, overrepresentation analysis (ORA) was performed to identify the biological process using the clusterProfiler R package ( 104 ).
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, R, clusterProfiler] -> stage not stated [ggplot2]

### Decoding transcriptomic signatures of cysteine string protein alpha-mediated synapse maintenance. (PNAS 2024)

- DOI: 10.1073/pnas.2320064121 | PMCID: PMC11181078 | PMID: 38833477
- Evidence: Gene-set enrichment analysis was performed using the function enrichGO from the R package clusterProfiler.
- Full pipeline: dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP, clusterProfiler] -> visualisation [UMAP]

### TMPRSS2-mediated SARS-CoV-2 uptake boosts innate immune activation, enhances cytopathology, and drives convergent virus evolution. (PNAS 2024)

- DOI: 10.1073/pnas.2407437121 | PMCID: PMC11161796 | PMID: 38814864
- Evidence: KEGG pathway analyses were performed with clusterProfiler ( 43 ) and Pathview packages in R.
- Full pipeline: read trimming [fastp] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R]

### Transgenerational increases in DNA methylation in Arabidopsis plants defective in active DNA demethylation. (PNAS 2024)

- DOI: 10.1073/pnas.2320468121 | PMCID: PMC11145202 | PMID: 38768356
- Evidence: Functional analysis of CG- DMR-associated genes was performed using clusterProfiler ( 21 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [R]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: GSEA was conducted using the R package “clusterProfiler” (v.3.12.0) for the gene list ranked by fold changes [log 2 (fold change)] ( 29 ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### APOBEC2 safeguards skeletal muscle cell fate through binding chromatin and regulating transcription of non-muscle genes during myoblast differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2312330121 | PMCID: PMC11047093 | PMID: 38625936
- Evidence: Analysis and plots were done using compareCluster function of clusterProfiler package.
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [ImageJ, R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, MACS2]

### A region of suppressed recombination misleads neoavian phylogenomics. (PNAS 2024)

- DOI: 10.1073/pnas.2319506121 | PMCID: PMC11009670 | PMID: 38557186
- Version used: **4.6.2**
- Evidence: By obtaining the Gene Ontology (GO) annotation information from the gprofiler_full_ggallus.name.gmt database (Version 2023-07-27) ( 70 ), we applied the enrichGO function of the R package clusterProfiler (version 4.6.2) ( 71 ) to explore any possible biological implications of the outlier genes.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> dimensionality reduction/clustering [R, clusterProfiler v4.6.2]

### Normalizing granuloma vasculature and matrix improves drug delivery and reduces bacterial burden in tuberculosis-infected rabbits. (PNAS 2024)

- DOI: 10.1073/pnas.2321336121 | PMCID: PMC10998582 | PMID: 38530888
- Version used: **4.10.0**
- Evidence: Due to unsupported ontologies/pathways for O. cuniculus , we performed GSEA (clusterProfiler v.4.10.0) by converting rabbit ensemble gene IDs to human orthologs using BioMart database (biomaRt v.2.58.0) and excluding genes for which duplicate matches, or no matches were found.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> normalisation [DESeq2 v1.42.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.0] -> stage not stated [ImageJ]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: The functional enrichment analysis employed the systemPipeR ( 39 ) and clusterProfiler ( 40 ) packages.
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### Viral afterlife: SARS-CoV-2 as a reservoir of immunomimetic peptides that reassemble into proinflammatory supramolecular complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2300644120 | PMCID: PMC10861912 | PMID: 38306481
- Version used: **4.2.2**
- Evidence: KEGG pathway analysis is performed with significant differentially expressed genes (adjusted P -value < 0.05) using clusterProfiler (version 4.2.2) ( 78 – 80 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.34.0, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.34.0, clusterProfiler v4.2.2] -> visualisation [ChimeraX]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Version used: **4.6.0**
- Evidence: For functional analysis of cluster-specific genes, an R package clusterProfiler (v4.6.0) ( 117 ) was used.
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: We performed statistical analysis and visualization of these pathways using the compareCluster() function from the R package “clusterProfiler”, by applying an over-representation analysis (ORA) method.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Cortical &lt;i&gt;miR-709&lt;/i&gt; links glutamatergic signaling to NREM sleep EEG slow waves in an activity-dependent manner. (PNAS 2024)

- DOI: 10.1073/pnas.2220532121 | PMCID: PMC10801902 | PMID: 38207077
- Version used: **4.8.1**
- Evidence: The pathway enrichment barplots were created using the enrichGO function of the clusterProfiler 4.8.1 R package ( 106 ) and using separately all up- ( 75 ) and downregulated ( 33 ) genes (also see SI Appendix , Supporting Methods for details).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [Bioconductor, R, limma] -> stage not stated [WGCNA]

### Disruption of DNA methylation-mediated cranial neural crest proliferation and differentiation causes orofacial clefts in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2317668121 | PMCID: PMC10801837 | PMID: 38194455
- Evidence: Gene ontological analyses were performed using R package clusterProfiler ( 79 ), using an FDR threshold of 0.05 to determine significant enrichment of biological processes.
- Full pipeline: quality control [FastQC] -> read trimming [RSEM v1.3.1, STAR v2.7.0] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.0] -> variant calling [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Version used: **4.14.6**
- Evidence: Gene ontology over-representation analysis was performed on the concordantly up-/downregulated genes between CBP/p300 inhibitor treatments and pan T antigen knockdown in CVG-1 cells using clusterProfiler v.4.14.6; overrepresented terms were visualized in descending order of gene ratio, i.e., number of genes in the query gene set found in a particular GO biological process term divided by the total...
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### Ace2 safeguards embryonic hematopoietic stem and progenitor cell production by restraining Nlrp3-mediated pyroptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2515641122 | PMCID: PMC12704739 | PMID: 41348733
- Version used: **4.6.1**
- Evidence: KEGG enrichment analyses were performed using the enrichment analysis tool clusterProfiler(version 4.6.1) ( 69 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.1.0] -> quantification [StringTie v1.3.3b] -> dimensionality reduction/clustering [clusterProfiler v4.6.1] -> differential/statistical testing [DESeq2 v1.10.1, R v3.2.3] -> stage not stated [GSEA, ImageJ]

### Brain-wide mapping of developmental trajectories of cerebellar efferent projections. (PNAS 2025)

- DOI: 10.1073/pnas.2521091122 | PMCID: PMC12685143 | PMID: 41289407
- Evidence: Pseudobulk differential expression and gene set enrichment analyses were performed using DESeq2 and clusterProfiler.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Version used: **3.12.0**
- Evidence: GO enrichment was analyzed with the R packages AnnotationForge (v1.26.0) ( 76 ) and clusterProfiler (v3.12.0) ( 77 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Evidence: KEGG and GO Enrichment analysis was done using the clusterProfiler ( 94 ) (v3.16.0) R package.
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: Further analysis and visualization were performed in R including clusterProfiler and GOplot packages for Gene ontology enrichment analysis ( 96 , 102 , 103 ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Version used: **4.2.0**
- Evidence: Pathway/GO analysis on the differentially expressed genes was performed using clusterProfiler (version 4.2.0) in R ( 21 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Evidence: To identify overrepresented biological processes and molecular functions among the GO terms for large versus miniature species, we performed enrichment analysis with the “enrichGO” function in the R package clusterProfiler ( 92 ) using the zebrafish ( Danio rerio ) annotation database, a P -value and q-value cutoff of 0.05, and the Benjamini–Hochberg multiple testing correction.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Joint disruption of &lt;i&gt;Ret&lt;/i&gt; and &lt;i&gt;Ednrb&lt;/i&gt; transcription shifts cell fate trajectories in the enteric nervous system in Hirschsprung disease. (PNAS 2025)

- DOI: 10.1073/pnas.2507062122 | PMCID: PMC12582274 | PMID: 41118220
- Evidence: ( E ) GO analysis of genes with statistically significant ( P adj < 0.05) gene expression alterations from Ret and Ednrb interactions using the clusterProfiler package; only the top 4 terms are plotted for each significant gene class ( x -axis).
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [clusterProfiler] -> stage not stated [Seurat]

### TMEM16F phospholipid scramblase regulates tumorigenesis by modulating the tumor immune microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2513910122 | PMCID: PMC12557541 | PMID: 41100671
- Version used: **4.10.1**
- Evidence: For KEGG analyses of the DEGs, the clusterProfiler (v4.10.1) package was employed.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> visualisation [UMAP] -> stage not stated [ImageJ, Seurat v4.3.0]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Gene Set Enrichment Analysis (GSEA) was performed using clusterProfiler ( 36 ) (v4.12.0), with gene sets from the Molecular Signatures Database ( 37 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: Gene Ontology enrichment was performed on the DE genes with the following script: # Load necessary libraries while suppressing warnings and messages library(clusterProfiler), library(matrixStats), library(gplots), library(RColorBrewer), library(sqldf), library(hopach), library(edgeR), library(limma), library(GOstats), library(GO.db), library(org.Hs.eg.db), library(org.Mm.eg.db), library(data.table...
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Evidence: Differentially expressed genes have been ranked by log2(FoldChange expression) and used for GSEAs on the hallmark gene set (H) from msigdbr (v7.5.1) using clusterProfiler [v3.18.1 ( 64 )], [ P valueCutoff = 0.05, pAdjustMethod = “BH”].
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Evidence: For each species, genes in shared, Epithemia -specific orthogroups were used for enrichment tests against a gene universe of functionally annotated genes with p-value cutoff 0.1. clusterProfiler ( 116 ) was used for tests of significance.
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### Lysosomal glucocerebrosidase is needed for ciliary Hedgehog signaling: A convergent pathway contributing to Parkinson's disease. (PNAS 2025)

- DOI: 10.1073/pnas.2504774122 | PMCID: PMC12337309 | PMID: 40737317
- Evidence: For Gene Ontology (GO) ( 47 , 48 ) enrichment analysis of differentially expressed genes, the clusterProfiler R package ( 49 ) was used.
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [CellProfiler]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: DEGs were identified using GO and KEGG pathway enrichment analyses were performed using the clusterProfiler R package, with GO analysis covering biological processes (BP), molecular functions (MF), and cellular components (CC).
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: GO term enrichment analyses were performed using clusterProfiler and gene set enrichment analysis ( 72 , 73 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: The DEG profiles were then used to predict associated Gene Ontology Terms using the Gene Set Enrichment Analysis analysis in the R package clusterProfiler ( 57 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **4.12.3**
- Evidence: Enriched IPR terms were determined using the R package clusterProfiler v4.12.3, the DEGs with a log2FC threshold of |1| as foreground and genes subjected DEG analysis (i.e., genes that were retained after removing the low counts) as background.
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: GO enrichment analysis was performed by using Metascape ( 73 ) or R package clusterProfiler ( 74 ) (Version 3.18.1).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Convergent expansions of keystone gene families drive metabolic innovation in Saccharomycotina yeasts. (PNAS 2025)

- DOI: 10.1073/pnas.2500165122 | PMCID: PMC12167968 | PMID: 40460114
- Evidence: Enrichment analysis was performed using the enrichKEGG() function in the R package clusterProfiler ( 55 ) v4.10.
- Full pipeline: alignment/mapping [IQ-TREE] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [InterProScan, OrthoFinder]

### Pathophysiologically relevant bisphenol S exposure accelerates aging by disrupting brown adipose tissue-regulated energy metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2420437122 | PMCID: PMC12167992 | PMID: 40455996
- Evidence: GO and KEGG pathway analyses were performed with the clusterProfiler R package.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> visualisation [GSEA]

### The SIK3-N783Y mutation is associated with the human natural short sleep trait. (PNAS 2025)

- DOI: 10.1073/pnas.2500356122 | PMCID: PMC12088394 | PMID: 40324078
- Evidence: GO enrichment analysis was performed using the clusterProfiler R package (v4.14.4, RRID: SCR_016884), focusing on BP and CC.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> machine learning [SnpEff] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Cytoscape, ImageJ]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Version used: **4.6.2**
- Evidence: KEGG enrichment analysis was conducted using clusterProfiler v4.6.2.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Evidence: Gene-ontology analysis was performed with the clusterProfiler R package ( https://yulab-smu.top/biomedical-knowledge-mining-book ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### Cell type and region-specific transcriptional changes in the endometrium of women with RIF identify potential treatment targets. (PNAS 2025)

- DOI: 10.1073/pnas.2421254122 | PMCID: PMC11929460 | PMID: 40063812
- Version used: **4.10.1**
- Evidence: Altered pathways and gene ontology (GO) biological processes were identified with Gene Set Enrichment Analysis (GSEA) using either GO biological process annotations or KEGG pathways ( 33 , 34 ), implemented in clusterProfiler (v 4.10.1) ( 35 ) using a minimum and maximum gene set size of 10 and 500, respectively.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.1] -> differential/statistical testing [lme4 v1.1] -> stage not stated [R, Seurat v5.0.3]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Evidence: Differentially expressed genes with adjusted P -values less than 0.05 were used as input for GO enrichment analysis by the clusterProfiler package ( 60 ), and the Enrichplot package was used for the visualization of Functional Enrichment Results ( 61 ).
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### Exome sequencing identifies genes for socioeconomic status in 350,770 individuals. (PNAS 2025)

- DOI: 10.1073/pnas.2414018122 | PMCID: PMC11745334 | PMID: 39772748
- Evidence: GO pathways enrichment analysis was performed by R package clusterProfiler ( 73 ).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ANNOVAR, FUMA, PLINK v2.0, SAIGE, Seurat, SnpEff]

### Gonadal sex and temperature independently influence germ cell differentiation and meiotic progression in &lt;i&gt;Trachemys scripta&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2413191121 | PMCID: PMC11725912 | PMID: 39793067
- Evidence: Gene Ontology analyses were done using terms associated with mouse orthologs with ClusterProfiler ( https://bioconductor.org/packages/ clusterProfiler ).
- Full pipeline: dimensionality reduction/clustering [Scanpy, UMAP, clusterProfiler]

### Genome-wide association mapping and targeted loss of function studies identify &lt;i&gt;Shroom3&lt;/i&gt; as a driver of hyperpolyploidy and ventricular dilation. (PNAS 2026)

- DOI: 10.1073/pnas.2522068123 | PMCID: PMC13229193 | PMID: 42189988
- Evidence: Terms are sorted by the normalized enrichment score calculated by clusterProfiler.
- Full pipeline: alignment/mapping [GEMMA] -> normalisation [clusterProfiler] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: GO analysis of gene lists was performed using clusterProfiler with a background set of all genes expressed in at least one of the sampled tissues ( 73 ).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Functional dissection of &lt;i&gt;SPOP&lt;/i&gt; at the amino acid level reveals a comprehensive functional landscape of variants during tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523210123 | PMCID: PMC13167761 | PMID: 42090249
- Evidence: Gene Ontology enrichment analysis utilized the clusterProfiler package ( 55 ).
- Full pipeline: read trimming [Cutadapt, minimap2] -> alignment/mapping [STAR, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> visualisation [PyMOL] -> stage not stated [DESeq2, GATK, R]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Evidence: Hallmark gene sets were retrieved using the msigdbr package (v 25.1.1) and enrichment analysis was performed using clusterProfiler package (v 4.10.1).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### Mild SARS-CoV-2 maternal infection in mice induces transient offspring neurodevelopmental aberrance. (PNAS 2026)

- DOI: 10.1073/pnas.2518294123 | PMCID: PMC13012083 | PMID: 41849379
- Version used: **4.10.0**
- Evidence: Gene symbols were converted between Ensembl IDs and Entrez IDs using the AnnotationDbi library (version 1.64.1) and bitr function (provided by clusterProfiler version 4.10.0).
- Full pipeline: quality control [FastQC v0.11.9] -> dimensionality reduction/clustering [clusterProfiler v4.10.0] -> differential/statistical testing [limma v3.58.1] -> visualisation [ggplot2 v3.5.2] -> stage not stated [R v4.3.2]

### The Nemp1-Nesprin complex mediates cellular responses to matrix mechanics. (PNAS 2026)

- DOI: 10.1073/pnas.2521253123 | PMCID: PMC12956887 | PMID: 41730104
- Version used: **4.10.1**
- Evidence: Furthermore, functional enrichment analysis was conducted to identify Gene Ontology (GO) terms and pathways significantly associated with differentially expressed genes ( P -value <0.05) were performed using clusterProfiler 4.10.1 [4].
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [Salmon v1.8.0] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [R, clusterProfiler v4.10.1, edgeR] -> visualisation [pheatmap v1.0.12]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Evidence: Functional enrichment was performed using GO and KEGG pathway analyses via the clusterProfiler R package v4.9.3 ( 63 ).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Evidence: Gene set enrichment and overrepresentation analysis was performed using clusterProfiler R package.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### Acclimation to high and low diurnal light is flexible in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2523996123 | PMCID: PMC12773772 | PMID: 41481448
- Version used: **4.12.0**
- Evidence: Each cluster of genes was tested for GO term enrichment using the enricher function from the R package clusterProfiler (v4.12.0) with pvalueCutoff = 0.05 and pAdjustMethod = “BH.” Representative enriched GO terms are displayed.
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [R, clusterProfiler v4.12.0] -> differential/statistical testing [clusterProfiler v4.12.0] -> stage not stated [ggplot2 v3.5.1]

### Dietary folic acid prevents peripheral neuropathy in mouse models of neural tube defects and type 2 diabetes. (PNAS 2026)

- DOI: 10.1073/pnas.2528095123 | PMCID: PMC12773702 | PMID: 41481435
- Version used: **4.8.1**
- Evidence: Functional enrichment analysis of the up- and down-regulated genes was performed using the R package clusterProfiler v4.8.1 using the GO biological processes (BP) terms ( 68 ).
- Full pipeline: read trimming [fastp v0.20, kallisto v0.46.1] -> alignment/mapping [kallisto v0.46.1] -> quantification [kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [R v3.42.2, edgeR v3.42.2] -> stage not stated [ImageJ]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Evidence: Gene Ontology analysis plots were generated with the R package “clusterProfiler.” To generate gene sets for GSEA, we selected the top 200 genes up-regulated in Ly49 + CD8 + T cells compared with Ly49 – CD8 + T cells in EAE mice ( 7 ) and the previously reported CD4 + T reg signature genes identified in mice ( 17 ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Version used: **4.10.1**
- Evidence: The top 200 significantly ranked genes underwent Gene Ontology enrichment analysis via clusterProfiler v4.10.1 using default parameters ( 87 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Evidence: GO enrichment of the differentially expressed genes between cluster 0,1 versus cluster 2 (with average Log2 fold change >1 or <−1 and adjusted p value <0.05) was performed using the clusterProfiler R package ( 98 ) based on the hallmark gene set from the Molecular Signatures Database (MSigDB)( 99 ), with pathway p value cutoff of 0.5 and q value cutoff of 1 after p value adjustment using Benjamini...
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

### Silencing mitochondrial gene expression in living cells. (Science 2025)

- DOI: 10.1126/science.adr3498 | PMCID: PMC7618265 | PMID: 40403134
- Version used: **4.8.3**
- Evidence: For Gene Ontology (GO) term enrichment analysis, the clusterProfiler (version 4.8.3) ( 46 ) package was used, with annotations from org.Hs.eg.db (version 3.17.0), focusing on Biological Processes (BP) and Molecular Functions (MF).
- Full pipeline: quantification [ImageJ v1.47] -> normalisation [limma v3.56.2] -> dimensionality reduction/clustering [clusterProfiler v4.8.3, limma v3.56.2] -> differential/statistical testing [DESeq2 v1.40.2, ImageJ v1.47, limma v3.56.2] -> stage not stated [Bioconductor, R v4.3.0, ggplot2]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Version used: **4.2.2**
- Evidence: Enrichment of genomic functions and cellular processes was done using the gseGO() function, as part of the R package, clusterProfiler (v4.2.2) ( Supplementary Table 2 ).
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Genes were ranked by log 2 fold change, and GSEA was performed using the clusterProfiler R package ( 94 ) (v4.10) with custom TERM2GENE mappings.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: Enrichment analysis: To perform overrepresentation analysis for significantly differentially expressed genes between either young (80 days) versus old (≥210 days) or short-lived versus long-lived trajectory (all 150 days old), we used GO enrichment analysis using the enrichGO function in the clusterProfiler package (version 4.4.4) ( data S2 ).
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Version used: **4.10.1**
- Evidence: Gene set enrichment analysis was conducted using clusterProfiler (4.10.1).
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **4.0.5**
- Evidence: For gene ontology enrichment analysis, we used the R package clusterProfiler (v4.0.5) to query the database org.Hs.eg.db_3.13.0.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

