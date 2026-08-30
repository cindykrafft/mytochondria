# GSEA

- **Category:** genomics
- **Papers in survey:** 720
- **Journals:** PNAS (469), Nature (199), Cell (35), Science (16), NEJM (1)
- **Years:** 2021 (47), 2022 (105), 2023 (133), 2024 (158), 2025 (200), 2026 (77)
- **Versions named:** 4.3.2 (7), 4.0.3 (6), 4.1.0 (6), 4.2.3 (3), 2.2.3 (2), 4.3.3 (1), 2.0 (1), 3.0 (1)
- **Pipeline stages it appears in:** differential/statistical testing (134), dimensionality reduction/clustering (66), normalisation (26), quantification (13), visualisation (9), alignment/mapping (3), quality control (2), machine learning (1), variant calling (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: The full differential expression, GSEA tables, and their respective statistics generated through g:Profiler are available in Tables S6 and S7 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **2.0**
- Evidence: ...GT ∗ G ∗ C Software and algorithms MaxQuant 1.6.10.43 Cox and Mann, 2008 https://www.maxquant.org/ R 3.6 R Core Team, 2019 https://www.r-project.org/ GSEA 2.0 Subramanian et al., 2005 https://www.gsea-msigdb.org/gsea/index.jsp R version 3.6.3 R Core Team, 2020 https://cran.r-project.org/ R package Seurat version 3.2.2 Stuart et al., 2019 https://cran.r-project.org/web/packages/Seurat/index.html R ...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### The interferon landscape along the respiratory tract impacts the severity of COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.016 | PMCID: PMC8373821 | PMID: 34492226
- Evidence: ...oftware and algorithms Transcriptome Analysis Console (TAC) software with ampliSeqRNA plugin ThermoFisher N/A CIBERSORTx Newman et al., 2019 N/A Fast Gene Set Enrichment Analysis package (fGSEA) Korotkevich et al., 2021 N/A ComplexHeatmap package Gu et al., 2016 N/A Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulf...
- Full pipeline: stage not stated [ComplexHeatmap, GSEA, MACS2]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Evidence: Gene set enrichment analysis (GSEA) was completed using the R package fgsea over genes ranked by average log foldchange expression between each group, including all genes with an average expression > 0.5 UMI within each respective cell type ( Korotkevich et al., 2021 ).
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Secreted gelsolin inhibits DNGR-1-dependent cross-presentation and cancer immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.021 | PMCID: PMC8320529 | PMID: 34081922
- Version used: **2.2.3**
- Evidence: The Wald’s statistic was used to rank genes using Preranked GSEA (version 2.2.3) ( Subramanian et al., 2005 ) and statistically significant pathways identified from the c2 pathway genesets [MSigdb] ( Liberzon et al., 2011 ).
- Full pipeline: differential/statistical testing [GSEA v2.2.3]

### Characterizing genetic intra-tumor heterogeneity across 2,658 human cancer genomes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.009 | PMCID: PMC8054914 | PMID: 33831375
- Evidence: We used a GSEA-like test to see if any of the 43 SRB loci were enriched for clonal or subclonal SVs.
- Full pipeline: quantification [SAMtools] -> stage not stated [GSEA, IMPUTE2, Mutect2, R, fgsea]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **3.0**
- Evidence: ...ackages/NMF/index.html R Package: ReactomePA (version 1.31.0) Yu and He, 2016 https://www.bioconductor.org/packages/release/bioc/html/ReactomePA.html GSEA (version 3.0) Subramanian et al., 2005 https://www.gsea-msigdb.org/gsea/index.jsp ssGSEA (version 1.0) Wang et al., 2017 https://secure.jbs.elsevierhealth.com/action/getSharedSiteSession?redirect=https%3A%2F%2Fwww.cell.com%2Fcancer-cell%2Ffullte...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: GSEA analysis for gene signatures in TPT treated hamsters We identified TOP1 inhibitor gene signatures from TPT-treated Syrian hamsters infected with SARS-CoV-2.
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: (D) Heatmap of REACTOME_Fatty acid metabolism LE genes from the GSEA analysis of DSM association in CD56 dim CD16 hi NK cells at T0 (see Figure 3 B).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Multi-organ proteomic landscape of COVID-19 autopsies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.004 | PMCID: PMC7794601 | PMID: 33503446
- Evidence: The immunological proteins were mapped against GSEA-immunologic gene sets in Metascape platform with our differentially expressed proteins and then the enriched pathways were distinguished by IPA analysis.
- Full pipeline: alignment/mapping [GSEA] -> differential/statistical testing [GSEA] -> stage not stated [Cytoscape, Metascape, R v3.6.1]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Version used: **4.1.0**
- Evidence: ....0 Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html VennDiagram v1.6.20 CRAN https://rdrr.io/cran/VennDiagram/ GSEA 4.1.0 Subramanian et al., 2005 and Mootha et al., 2003 https://www.gsea-msigdb.org/gsea/login.jsp;jsessionid=94213B4581121AA02E710A5BE27FBE9F CellRanger v3.1.0 10x Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/dow...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.030 | PMCID: PMC7584921 | PMID: 33147445
- Evidence: Gene Set Enrichment Analysis for SARS-CoV-2 Pooled CRISPR Screen, Affinity Proteomics Enriched CRISPR Screen Genes for Each Viral Gene, and Gene Ontology (GO) Analyses of SARS-CoV-2, ZIKV, and IAV Pooled CRISPR Screens, Related to Figures 2, 3, and S2 Table S3.
- Full pipeline: read trimming [Cutadapt v1.13] -> alignment/mapping [STAR] -> stage not stated [DESeq2, GSEA, R, Seurat, fgsea]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: Gene Set Enrichment analysis (GSEA) was carried out using R package Cluster Profiler (v3.18.1; Yu et al., 2012 ) and gene lists ranked using the Wald statistic.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: A summary of other processes that may be affected at the early and late stages of the infection is shown in GSEA plots for 1 and 10 dpi ( Figure S3 ), and all the significant transcriptional changes are listed in Table S1 .
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: Pathway Analysis Gene-set enrichment analysis GSEA of differentially expressed genes were performed using the FGSEA algorithm ( Korotkevich et al., 2021 ).
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: Gene Set Enrichment Analysis (GSEA) The log 2 -fold change of differentially expressed genes (with high counts, i.e., “baseMean” > 100) from DESeq2 was used to define the ranked gene list used for GSEA.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: ECM Gene Analysis To analyze ECM components by gene expression, an ECM gene signature (GO ECM structural constituent, GO:0030021) was downloaded from the GSEA website ( www.gsea-msigdb.org ) and used to compare MIBI-identified samples with the top and bottom quartiles of cancer-associated fibroblast density in the stroma.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: Gene set enrichment analysis (GSEA) 87 for Gene Ontology terms 88 and KEGG pathways 89 was performed with clusterprofiler.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: The ensemble ID targeting multiple genes was collapsed (average) and a final gene data matrix was used for a modular repertoire analysis as previously described 82 , 83 or for gene set enrichment analysis (GSEA: fgsea) with hallmark gene sets ( http://www.gsea-msigdb.org/ ).
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Mechanopathology of biofilm-like Mycobacterium tuberculosis cords. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.016 | PMCID: PMC10642369 | PMID: 37865090
- Evidence: ...nder Foundation RRID: SCR_008606 MATLAB 2018b MathWorks RRID: SCR_001622 Molecular Signatures Database UC San Diego, Broad Institute RRID: SCR_016863 Gene Set Enrichment Analysis (GSEA) UC San Diego, Broad Institute RRID: SCR_003199 R Project for Scientific Computing Free Software Foundation RRID: SCR_001905 Star PMID: 23104886 RRID: SCR_004463 FastQC Baraham Institute RRID: SCR_014583 Bioconducto...
- Full pipeline: quality control [Bioconductor, FastQC, GSEA, STAR v2.7.10b] -> alignment/mapping [STAR v2.7.10b] -> quantification [R, edgeR] -> stage not stated [ImageJ, MACS2]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Evidence: .../A Bioconductor v.3.8 Bioconductor https://www.bioconductor.org/ Biorender Biorender https://biorender.com/ Flowjo v10.6.2 BD https://www.flowjo.com/ GSEA Broad institute https://www.gsea-msigdb.org/ ImageJ v2.1.0/1.53c NIH https://imagej.nih.gov/ij/ Kallisto v.0.46.0 Pachter Lab https://pachterlab.github.io/kallisto/ Olympic cellSens imaging software Olympus LS https://www.olympus-lifescience.com...
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Gene set enrichment analysis (GSEA) Enrichment of Gene ontology (GO) terms for biological processes were analysed using GProfiler 109 and Enrichr.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Evidence: GSEA analysis reveals lipid antigen processing and presentation (P<1.96E-13) and cellular response to interferon (P<2.74E-5) as the two most highly enriched pathways ( Figure 3E , see Methods ).
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Version used: **4.2.3**
- Evidence: 84 https://bioconductor.org/packages/edgeR/ GSEA 4.2.3 Barnden et al.
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### SARS-CoV-2 replication in airway epithelia requires motile cilia and microvillar reprogramming. (Cell 2023)

- DOI: 10.1016/j.cell.2022.11.030 | PMCID: PMC9715480 | PMID: 36580912
- Evidence: 50 Using kinase set enrichment analysis (KSEA), 51 , 52 we assigned an enrichment score (ES) (weighted Kolmogorov-Smirnov statistic) to each kinase to reflect its activity in a manner analogous to that of gene set enrichment analysis (GSEA).
- Full pipeline: normalisation [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, GSEA] -> stage not stated [ImageJ, MACS2, R]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: 86 https://git.bioconductor.org/packages/clusterProfiler Gene Set Enrichment Analysis (GSEA) Subramanian et al.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### Thyroid hormone remodels cortex to coordinate body-wide metabolism and exploration. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.041 | PMCID: PMC11455614 | PMID: 39178853
- Evidence: Gene set enrichment analysis (GSEA) of astrocyte TRGs ( Table S2 ) revealed an over-representation of genes associated with synapse formation and maintenance, including astrocyte-expressed genes that regulate synaptic glutamate release and clearance ( Figure S4C ).
- Full pipeline: read trimming [Seurat] -> alignment/mapping [Seurat] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, R v4.2.2] -> stage not stated [GSEA, PyTorch]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Evidence: Gene set enrichment analysis (GSEA) was assessed with the GAGE package, 101 which uses the average of the absolute values of the per gene test statistics to account for both up- and down-regulation of the curated pathways.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Evidence: TF knockout GO enrichment GO enrichment analysis for each TF-KO was performed using Gene Set Enrichment Analysis (GSEA) implemented in ClusterProfiler R package 152 after ranking genes based on significance of enrichment defined as: -log 10 (P-value)*Fold Change ( Figure 6F ; Tables S6A – S6C ).
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Distinct components of mRNA vaccines cooperate to instruct efficient germinal center responses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.023 | PMCID: PMC12878702 | PMID: 41406961
- Evidence: GSEA was performed by contrasting pseudo-bulk counts of biotin-positive and -negative cells with DESeq2 and testing genes ranked by −log10 p-value (signed by log fold change) for enrichment of a previously published LIPSTIC signature 34 with the R package fgsea.
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [GSEA, R, fgsea] -> stage not stated [Seurat]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Evidence: 125 DEP and Gene Set Enrichment Analysis (GSEA) analysis of the human iPSC-derived AHNAK -knockdown (KD) astrocytes The expression of the above-quantified proteins were log2-transformed and normalized by median centering.
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### RNA Pol II inhibition activates cell death independently from the loss of transcription. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.034 | PMCID: PMC12406974 | PMID: 40818455
- Evidence: To identify if fast or slow decaying mRNAs are preferentially enriched at the extreme ends of our chemo-genetic profiling data, GSEA was run with a pre-ranked list of the relative death rate scores.
- Full pipeline: quality control [FastQC] -> quantification [FastQC, kallisto] -> normalisation [DESeq2] -> differential/statistical testing [FastQC] -> stage not stated [GSEA]

### Molecular and neural control of social hierarchy by a forebrain-thalamocortical circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.024 | PMCID: PMC12458795 | PMID: 40795854
- Evidence: To determine the effect of social status on gene set enrichment, we used gene set enrichment analysis (GSEA), a technique designed to detect modest but coordinated changes in the expression of groups of functionally related genes that are defined a priori 42 , 43 .
- Full pipeline: normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, GSEA, R, Seurat v2.3.4]

### Serotonin transporter inhibits antitumor immunity through regulating the intratumoral serotonin axis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.032 | PMCID: PMC12255530 | PMID: 40403728
- Evidence: For gene set enrichment analysis (GSEA), the clusterProfiler packages were used to calculate the enrichment scores for each cluster in the signature gene list (GEO: GSE122713 ).
- Full pipeline: quantification [R, Seurat v4.0.0] -> dimensionality reduction/clustering [GSEA, R, Seurat v4.0.0, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2, velocyto]

### Citrate clearance is a major function of aconitase 2 in the canonical TCA cycle. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.028 | PMCID: PMC13045649 | PMID: 41763199
- Evidence: Genes were ranked by log 2 fold change of the comparisons indicated in each figure legend and gene set enrichment analysis (GSEA) was performed using fgsea (version 1.32.4) in R with Reactome gene sets using the msigdbr function or with custom kidney injury-related gene sets.
- Full pipeline: differential/statistical testing [DESeq2 v1.46.0] -> stage not stated [GSEA, R v4.3.2, featureCounts, fgsea, ggplot2 v3.5.2]

### A Microbiota-Directed Food Intervention for Undernourished Children. (NEJM 2021)

- DOI: 10.1056/nejmoa2023294 | PMCID: PMC7993600 | PMID: 33826814
- Evidence: Changes in plasma protein abundances were analyzed using an Empirical Bayes linear model framework [limma( 12 )] and gene set enrichment analysis [GSEA( 13 )], a method for quantifying whether a rank-ordered list of features (e.g., proteins ranked by their changes in abundances after a treatment or by correlation coefficient) are enriched for a subset of features of interest (e.g., a biological pa...
- Full pipeline: quantification [GSEA, limma] -> differential/statistical testing [GSEA, limma]

### NASH limits anti-tumour surveillance in immunotherapy-treated HCC. (Nature 2021)

- DOI: 10.1038/s41586-021-03362-0 | PMCID: PMC8046670 | PMID: 33762733
- Evidence: GSEA was performed using ClusterProfiler (3.18) 44 and gene sets obtained from WikiPathway ( https://www.wikipathways.org/ ) and MSigDB ( https://broadinstitute.org/msigdb ) 45 – 47 .
- Full pipeline: quality control [Seurat] -> alignment/mapping [velocyto v0.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2 v1.28.1] -> stage not stated [R v3.4, scVelo v0.2.2]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Gene Set Enrichment Analysis Differential expression analysis was performed with DESeq2.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Lipid signalling enforces functional specialization of T<sub>reg</sub> cells in tumours. (Nature 2021)

- DOI: 10.1038/s41586-021-03235-6 | PMCID: PMC8168716 | PMID: 33627871
- Evidence: Gene expression profiling, gene set enrichment analysis (GSEA) and Ingenuity pathway analysis (IPA) Microarray analyses (Affymetrix Mouse Clariom S Assay) of total RNA collected in individual batches from the following T reg cell samples were performed: (a) T reg cells from tumours or PLNs of Foxp3 Cre Scap +/+ or +/fl ( n = 4 biological replicates) or Foxp3 Cre Scap fl/fl ( n = 3 biological repli...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, limma v3.34.9] -> visualisation [UMAP] -> stage not stated [GSEA, Seurat, ggplot2 v2.2.1]

### SARS-CoV-2 infection is effectively treated and prevented by EIDD-2801. (Nature 2021)

- DOI: 10.1038/s41586-021-03312-w | PMCID: PMC7979515 | PMID: 33561864
- Evidence: Graphs and summary tables were built in R using ggplot; gene set enrichment was performed using GSEA and GO analysis (tidyverse 1.3.0; PCATools 1.2.0; Sqldf 0.4–11; na.tools 0.3.1; ggbiplot 0.55; ggplot2 3.3.1; dplyr 0.8.4).
- Full pipeline: alignment/mapping [STAR v2.7.5a] -> quantification [STAR v2.7.5a] -> normalisation [DESeq2, R v3.6.3] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [GSEA, ImageJ, ggplot2 v3.3.1, tidyverse v1.3.0]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Gene set enrichment analysis (GSEA): GSEA 72 was performed using the GSEA-Preranked tool for conducting gene set enrichment analysis of data derived from RNA-seq experiments (version 2.07) against signatures in the MSigDB database ( http://software.broadinstitute.org/gsea/msigdb ), signatures derived herein, and published expression signatures derived from human 23 , 73 or organoid samples 17 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: The functional enrichment analyses were implemented by GSEA ( gsea-msigdb.org/gsea , 4.0.0) 63 and the Bioconductor package GeneAnswers ( bioconductor.org/packages/release/bioc/html/GeneAnswers , 2.32.0).
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### IgA transcytosis and antigen recognition govern ovarian cancer immunity. (Nature 2021)

- DOI: 10.1038/s41586-020-03144-0 | PMCID: PMC7969354 | PMID: 33536615
- Evidence: The preranked gene list was used to perform preranked GSEA 28 (v.4.0.2) to assess enrichment of hallmarks, curated gene sets and Gene Ontology 29 terms in MSigDB 28 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, HTSeq, STAR] -> normalisation [HTSeq] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [GSEA, R v3.6.1]

### Dynamic regulation of T<sub>FH</sub> selection during the germinal centre reaction. (Nature 2021)

- DOI: 10.1038/s41586-021-03187-x | PMCID: PMC7979475 | PMID: 33536617
- Evidence: Increased TCR signaling enforces proliferation supported by a switch in metabolic status. a, Gene Set Enrichment Analysis and the rank-ordered gene lists found upregulated in αDEC205-HIGH versus non boosted or b, αDEC205-HIGH versus αDEC205-LOW groups.
- Full pipeline: quantification [DESeq2 v1.24.0, R] -> differential/statistical testing [DESeq2 v1.24.0, R, Seurat v3.1.2, kallisto v0.46] -> stage not stated [GSEA]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Evidence: Gene Set Enrichment Analysis 36 , 37 (GSEA - Supplementary Table 1 ) was used to define the enriched gene set for the pre-ranked homo sapiens homologs list by Wald statistics.
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### Histone H1 loss drives lymphoma by disrupting 3D chromatin architecture. (Nature 2021)

- DOI: 10.1038/s41586-020-3017-y | PMCID: PMC7855728 | PMID: 33299181
- Evidence: ... based on genes in the top 90 th percentile variability. b , FPKM expression of NSD2 from human and mouse naïve B and GCB cells RNA-seq profiles. c , GSEA analysis of genes linked to NSD2 gain-of-function mutation in three cell lines (RCHACV, SEM, RPMI) against ranked murine H1c −/− /e −/− GC B cell expression changes. d , Boxplot of log2 relative gene expression normalized to average expression v...
- Full pipeline: quantification [GSEA] -> normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Arterialization requires the timely suppression of cell growth. (Nature 2021)

- DOI: 10.1038/s41586-020-3018-x | PMCID: PMC7116692 | PMID: 33299176
- Evidence: Complementary enrichment analyses with GSEA 38 were performed for each contrast, using the whole collection of genes detected as expressed (12,872 genes) to identify gene sets that had a tendency to be more expressed in either of the conditions being compared.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5] -> alignment/mapping [RSEM v1.2.30] -> normalisation [limma v3.32.10] -> differential/statistical testing [limma v3.32.10] -> stage not stated [GSEA, ImageJ]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: We used GSEA-preranked to test for an enrichment of ECM genes in the phenotypes using fgsea R package (v.1.14.0) 79 , with MatrisomeDB gene set collection 5 .
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Identification of SARS-CoV-2 inhibitors using lung and colonic organoids. (Nature 2021)

- DOI: 10.1038/s41586-020-2901-9 | PMCID: PMC8034380 | PMID: 33116299
- Evidence: Gene set enrichment analysis (GSEA) revealed over-represented pathway networks including rheumatoid arthritis, TNF signaling, IL-17 signaling, and cytokine-cytokine receptor interaction ( Fig.
- Full pipeline: quality control [R, edgeR] -> alignment/mapping [Bowtie2] -> quantification [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, edgeR] -> machine learning [UMAP] -> visualisation [Bowtie2] -> stage not stated [GSEA, Seurat v3.1.0]

### A plant-derived natural photosynthetic system for improving cell anabolism. (Nature 2022)

- DOI: 10.1038/s41586-022-05499-y | PMCID: PMC9750875 | PMID: 36477541
- Evidence: To determine the level of metabolic pathway enrichment, we used gene set enrichment analysis (GSEA) to compare the pathways between different groups 53 .
- Full pipeline: stage not stated [DESeq2, GSEA]

### Effect of the intratumoral microbiota on spatial and cellular heterogeneity in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05435-0 | PMCID: PMC9684076 | PMID: 36385528
- Evidence: 5 Differential gene expression and GSEA analysis comparing distinct CRC single-cell groups on the basis of bacteria association. a , GSEA analysis indicating the signalling pathways that are differentially regulated in HCT116 cells co-incubated with Fusobacterium nucleatum at MOI = 500 for 3 h between different single-cell groups as follow: Top: Total F. nucleatum -associated cells (Total Fuso+ ) ...
- Full pipeline: alignment/mapping [GATK, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Evidence: Functional enrichment was computed through the Gene Set Enrichment Analysis implementation in 94 with genes ordered by fold change.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Evidence: To perform gene set enrichment analysis 89 all remaining genes were ordered by DESeq2’s test statistic, and enrichment of Gene Ontology annotations, KEGG pathways and Hallmark pathways was tested for (FDR < 0.05) using gseGO, gseKEGG and GSEA, respectively, from ClusterProfiler 65 .
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### Collagenolysis-dependent DDR1 signalling dictates pancreatic cancer outcome. (Nature 2022)

- DOI: 10.1038/s41586-022-05169-z | PMCID: PMC9588640 | PMID: 36198801
- Evidence: Pathway analyses were performed using the Molecular Signature Database of GSEA. scRNA-seq analysis Samples from five primary tumours from patients with PDAC and one PDAC liver metastasis were obtained 33 and analysed separately to better identify cell heterogeneity and clusters.
- Full pipeline: quality control [R v4.0.2, Seurat] -> alignment/mapping [STAR] -> quantification [HOMER v4.11] -> dimensionality reduction/clustering [GSEA]

### Long-primed germinal centres with enduring affinity maturation and clonal migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05216-9 | PMCID: PMC9491273 | PMID: 36131022
- Evidence: Gene set enrichment analysis (GSEA) was conducted using the package fgsea in R 44 , 45 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [UCSF Chimera v1.13] -> visualisation [UCSF Chimera v1.13] -> stage not stated [GSEA, RELION v3.0, Seurat, fgsea]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: In accordance with the in vitro data, gene set enrichment analysis (GSEA) showed that infused CAR + cells with attenuated PD1 expression had a higher proliferation and immune response capability in vivo (Fig.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### RASA2 ablation in T cells boosts antigen sensitivity and long-term function. (Nature 2022)

- DOI: 10.1038/s41586-022-05126-w | PMCID: PMC9433322 | PMID: 36002574
- Evidence: For the quality metric of screens by dropout analysis of essential genes, we used essential genes as determined by DepMap 19 and GSEA for gene-level log 2 fold change.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [DESeq2, Seurat, fgsea] -> stage not stated [GSEA, ImageJ v1.52q, R]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: Gene set enrichment analysis was performed using Gene Set Enrichment Analysis (GSEA) software (v.4.0.3) 58 .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Evidence: We carried out Gene Set Enrichment Analysis in R using the ClusterProfiler package 58 v.3.14.3 and msigdbr v.7.1.1 using default settings with all the gene expression changes.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: For gene set enrichment analysis (GSEA), the msigdbr R package (version 7.4.1) was used to download the hallmark gene set from the Molecular Signatures Database.
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Brown-fat-mediated tumour suppression by cold-altered global metabolism. (Nature 2022)

- DOI: 10.1038/s41586-022-05030-3 | PMCID: PMC9365697 | PMID: 35922508
- Version used: **4.1.0**
- Evidence: GSEA was performed with GSEA (v.4.1.0) using the GSEAPreranked tool, whereby genes were preranked on the basis of their P values and fold changes.
- Full pipeline: alignment/mapping [featureCounts v2.0.0] -> differential/statistical testing [DESeq2 v1.30.0, GSEA v4.1.0] -> stage not stated [ImageJ]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: Next, we estimated TF activities for each cell using Viper 74 , a GSEA-like approach, as implemented in the Dorothea R package and tutorial 75 .
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Version used: **4.0.3**
- Evidence: The GSEA algorithm was used to compute the normalized enrichment score and statistical significance for Molecular Signatures Database (MSigDB) hallmark, C2, C5 and C6 collection terms and gene set permutations were performed 1,000 times for each analysis by GSEA v.4.0.3 software.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Intermittent PI3Kδ inhibition sustains anti-tumour immunity and curbs irAEs. (Nature 2022)

- DOI: 10.1038/s41586-022-04685-2 | PMCID: PMC9132770 | PMID: 35508656
- Evidence: Gene Set Enrichment Analysis (GSEA) scores were estimated with fgsea (v1.10.1) in R using signal-to-noise ratio as the metric (minSize = 3 and maxSize = 500).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [GSEA, MACS2, Seurat v3.1.5, fgsea v1.10.1]

### CCNE1 amplification is synthetic lethal with PKMYT1 kinase inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-04638-9 | PMCID: PMC9046089 | PMID: 35444283
- Evidence: GSEA 62 was performed to identify the enrichment of genes co-regulated by MMB–FOXM1 in the FT282-hTERT TP53 R175H CCNE1 C3 and C4 clones compared to parental wild-type cells.
- Full pipeline: quality control [FastQC v0.11.9] -> stage not stated [GSEA, ImageJ v2.0.0, edgeR v3.30.3]

### Genetic instability from a single S phase after whole-genome duplication. (Nature 2022)

- DOI: 10.1038/s41586-022-04578-4 | PMCID: PMC8986533 | PMID: 35355016
- Evidence: GSEA with TCGA PanCancer data GSEA was performed using GSEA software v.4.2.1 50 , 51 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.4] -> normalisation [RSEM] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Tryptophan depletion results in tryptophan-to-phenylalanine substitutants. (Nature 2022)

- DOI: 10.1038/s41586-022-04499-2 | PMCID: PMC8942854 | PMID: 35264796
- Evidence: ER, endoplasmic reticulum. d , GSEA plot depicting the enrichment of T cell activation signature stratified against the difference in the number of substitutants in the W>F high class versus the W>F low class.
- Full pipeline: stage not stated [Coot, GSEA]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: Gene set enrichment analysis Gene set enrichment analysis (GSEA) 11 , 41 was done with the fast GSEA algorithm 42 using Bioconductor’s fgsea package 43 .
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Evidence: For gene enrichment analysis (GSEA), we first defined ERG and FOXA1 gene signatures from VCaP or LNCaP cells treated with control siRNA or siRNA targeting ERG 38 or FOXA1 (generated in this study) containing 250 significantly downregulated genes.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: As input to this gene set enrichment analysis (GSEA) method, the annotated gene sets provided within the MSigDB version 6.1 were used 22 , 77 (Fig.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### The molecular cytoarchitecture of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06818-7 | PMCID: PMC10719111 | PMID: 38092915
- Evidence: Transcription factor enrichment To identify the transcription factors selectively enriched for telencephalic excitatory or inhibitory populations, we performed gene set enrichment analysis (GSEA) on a ranked gene list against a curated transcription factor gene set.
- Full pipeline: normalisation [Seurat] -> registration [PyTorch] -> dimensionality reduction/clustering [Scanpy] -> visualisation [ComplexHeatmap] -> stage not stated [GSEA, MAGMA v1.10, R, Rcpp, fgsea v1.20.0, igraph v1.2.7]

### Trans-vaccenic acid reprograms CD8&lt;sup&gt;+&lt;/sup&gt; T cells and anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06749-3 | PMCID: PMC10686835 | PMID: 37993715
- Evidence: ...regulated genes ( upper ) and down-regulated genes ( lower ) by RNA-seq analysis of CD8 + T cells treated with TVA comparing to control ( n = 3). h , GSEA of upregulated MYC targets V1 ( left ) and MYC target V2 ( right ) induced by TVA treatment in CD8 + T cells.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Cytoscape] -> visualisation [Cytoscape] -> stage not stated [DADA2, GSEA]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: Pre-ranked GSEA and Fisher’s exact test For scRNA-seq analysis, nonparametric two-tailed Wilcoxon rank-sum test was used to compare the gene expression of cells between two genotypes (sg Ikzf1 compared with sgNTC, sg Ets1 compared with sgNTC or sg Rbpj compared with sgNTC) and then genes in each comparison were ranked based on their log 2 (FC) values.
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Embryo-scale reverse genetics at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06720-2 | PMCID: PMC10665197 | PMID: 37968389
- Evidence: Gene-set enrichment analyses After differential expression testing, genes that had significant coefficients ( q < 0.05) were used for gene-set enrichment analysis (GSEA) with the g:Profiler2 R package (v.0.2.1) 70 .
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Monocle v1.3.1, UMAP] -> differential/statistical testing [GSEA, R] -> stage not stated [ImageJ, fgsea v1.26.0]

### Apoptotic stress causes mtDNA release during senescence and drives the SASP. (Nature 2023)

- DOI: 10.1038/s41586-023-06621-4 | PMCID: PMC10584674 | PMID: 37821702
- Evidence: Gene Ontology analysis was performed using Gene Set enrichment Analysis (GSEA) and Ingenuity Pathway Analysis (IPA) software.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [Cufflinks, FastQC, STAR] -> quantification [Cufflinks, DESeq2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Evidence: GSEA was performed using GSEAPreranked 18 , 55 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Evidence: 10g ), the list of expressed genes ranked by higher to lower LFC value was used as input to the R package fgsea (v.3.17) 59 to run GSEA using the mouse GO:BP dataset.
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: The identified gene candidates for each cluster were interrogated for statistically significant gene ontologies using GSEA 69 ( http://software.broadinstitute.org/gsea/index.jsp ).
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: After removing scores of zero and rescaling correlation values to the range [−1,1], we use these scores as input to gene set enrichment analysis (GSEA), along with cell-type-specific GMT files (provided in Supplementary Table 7 ), to assign pathways to these major axes of biological variation.
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Version used: **2.2.3**
- Evidence: Gene Set Enrichment analysis (GSEA, version 2.2.3) 55 was performed for each pairwise comparison using gene lists ranked using the Wald statistic.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Evidence: A ranked DEG list was generated based on Wald statistics from DESeq2 results, and GSEA was performed using hallmark gene sets 66 , 67 .
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Evidence: For the human genes in our filtered gene set ( n = 12,655), we defined as ISGs ( n = 174) those genes included in the union of GSEA’s hallmark ( https://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp?collection=H ) IFNα response and IFNγ response gene sets, but excluded those from the inflammatory response set.
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Gene set enrichment analyses (GSEA) To compute gene set enrichments for aPT and aTAL, conserved genes differentially expressed in the adaptive over reference states were identified as indicated above.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Mast cells link immune sensing to antigen-avoidance behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06188-0 | PMCID: PMC10432277 | PMID: 37438525
- Evidence: Gene set enrichment analysis (GSEA) for each experimental group was performed on the complete dataset ranked with lfcshrink using ClusterProfiler 73 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [DESeq2]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Evidence: The pre-ranked gene set enrichment analysis (GSEA) was performed as previously described 65 against gene sets from KEGG, BIOCARTA, PID, REACTOME, C7 immunological, GO and HALLMARK collections from the Molecular Signatures Database (mSigDB) ( https://www.broadinstitute.org/gsea/msigdb/ , version 7.4) and signatures curated from published papers, as follows.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: A GSEA was performed on normalized gene counts from control and lamin-B2-overexpressing TP53 -knockout hTERT RPE-1 cells treated with reversine or DMSO (Extended Data Fig.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Gene set enrichment analysis was performed on the log-transformed fold change given by the differential expression contrasts using the GSEA function from ClusterProfiler on the Hallmark Gene Set Collection 38 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Deterministic evolution and stringent selection during preneoplasia. (Nature 2023)

- DOI: 10.1038/s41586-023-06102-8 | PMCID: PMC10247377 | PMID: 37258665
- Evidence: Supplementary Table 6 scRNA sequencing results including quality control metrics, top differentially expressed genes and GSEA results.
- Full pipeline: quality control [GSEA] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP]

### Uridine-derived ribose fuels glucose-restricted pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06073-w | PMCID: PMC10232363 | PMID: 37198494
- Version used: **4.0.3**
- Evidence: Pathway analyses Pathway analyses were performed using DAVID functional annotation platform ( https://david.ncifcrf.gov/ , version 6.8) or gene set enrichment analysis (GSEA, version 4.0.3) with GSEAPreranked option.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5.2, limma] -> visualisation [ComplexHeatmap, ggplot2 v3.3.5, tidyverse v0.8.3] -> stage not stated [GSEA v4.0.3]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Evidence: In addition, we performed GSEA to study the gene sets enriched in the E2-induced HTGTS breakpoint hotspots.
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### Mitotic clustering of pulverized chromosomes from micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-05974-0 | PMCID: PMC10307639 | PMID: 37165191
- Version used: **4.3.2**
- Evidence: Gene Set Enrichment Analysis (GSEA, v.4.3.2) 55 was performed using the weighted enrichment statistic on normalized gene counts computed using DESeq2 56 .
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> quantification [ImageJ] -> normalisation [DESeq2, GSEA v4.3.2, HTSeq v0.6.1p] -> differential/statistical testing [DESeq2, GSEA v4.3.2] -> stage not stated [BEDTools]

### Dedifferentiation maintains melanocyte stem cells in a dynamic niche. (Nature 2023)

- DOI: 10.1038/s41586-023-05960-6 | PMCID: PMC10132989 | PMID: 37076619
- Evidence: The pre-ranked gene list as queried for its enrichment in two annotated gene sets acquired from The Molecular Signature Database (MSigDB)—GOBP_DENDRITE_DEVELOPMENT and GOBP_DENDRITE_MORPHOGENESIS—using the preranked gene set enrichment analysis (GSEA) analysis tool 61 , 62 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> structure determination [ImageJ] -> visualisation [Seurat] -> stage not stated [GSEA]

### Ageing-associated changes in transcriptional elongation influence longevity. (Nature 2023)

- DOI: 10.1038/s41586-023-05922-y | PMCID: PMC10132977 | PMID: 37046086
- Evidence: For the differential analysis of transcriptional elongation regulators, we downloaded the list of positive and negative regulators from the GSEA/MSigDB 71 .
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.5.1b, Trimmomatic] -> quantification [StringTie] -> differential/statistical testing [DESeq2 v1.8.2, GSEA] -> stage not stated [kallisto v0.42.5]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: The t -statistic generated by limma was used as input for GSEA for MSigDB hallmark gene sets 14 using the R package fgsea (v.1.10.1) 71 with default parameters.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Evidence: Scale bars 100 μm (B,F,E) Extended Data Figure 5 A-B) Significantly enriched GSEA pathways upregulated in T-PM lung epithelial cells compared to T control mice (A), in ET-PM lung epithelial cells compared to ET control mice (B).
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: Enrichment analysis of features in the MEFISTO model Gene set enrichment analysis for gene features was performed based on the C5 category and the Biological Process subcategory from the MSigDB database ( https://www.gsea-msigdb.org/gsea/msigdb ) using GSEA functionality implemented in MOFA2 (run_enrichment command, MOFA2 version 1.3.5).
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Fumarate induces vesicular release of mtDNA to drive innate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-05770-w | PMCID: PMC10017517 | PMID: 36890229
- Evidence: GSEA was performed using the GSEA software from Broad Institute.
- Full pipeline: read trimming [Cutadapt v1.10.0] -> alignment/mapping [Cutadapt v1.10.0, STAR v2.6.0c] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2 v1.18.1] -> stage not stated [GSEA, ImageJ]

### Macrophage fumarate hydratase restrains mtRNA-mediated interferon production. (Nature 2023)

- DOI: 10.1038/s41586-023-05720-6 | PMCID: PMC10411300 | PMID: 36890227
- Evidence: Geneset enrichment analysis (GSEA) identified an expected suppression in genes associated with metabolism, but FHIN1 also decreased expression of inflammatory pathways, including IL-1 and IL-10 signalling ( Fig.
- Full pipeline: stage not stated [GSEA]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: ( h ) Gene set enrichment analysis (GSEA) of downregulated genes in DPY30–mAID cells in response to 2 h Auxin treatment.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Evidence: The gene set enrichment analysis (GSEA) of the Reactome pathway Autophagy (R-HSA-9612973) was performed using fgsea (v.4.1) 49 . qPCR Total RNA was extracted from cell lines using Trizol Reagent (Invitrogen,15596018) and the total RNA extraction kit (Qiagen, 74004/74104) according to the manufacturer’s protocol.
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Green points are significant only in pups. n , Top ten enriched pathways in adults and pups from a GSEA of genes matched to the closest DA peaks.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Evidence: Bioinformatics analysis Gene set enrichment analysis The enrichment analysis for chromosomal gene distributions was done in R v3.6.3 with the GSEA function of clusterProfiler v3.14.3 53 was used with maxGSSize = 20000 and nPerm = 20000.
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **4.0.3**
- Evidence: GSEA The RPKM matrix after the removal of low-count genes (edgeR (v.3.30.0) 64 ) was used as an input for the GSEA (v.4.0.3) software 71 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: For gene-set enrichment analysis (GSEA), differentially expressed genes were pre-ranked in decreasing order by the negative logarithm of their P value, multiplied for the sign of their average logFC (in R, ‘- log(p_val)*sign(avg_log2FC)’).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: Putative enhancers farther away than 20,000 from a TSS or gene body were not linked to any gene and were discarded from downstream GSEA.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Gene set enrichment analysis was performed in R using the GSEA function of the clusterProfiler package (version 4.4.4) 65 .
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: Gene set enrichment analysis GSEA was carried out on all 6,495 C2 curated gene sets from the Molecular Signatures Database (MSigDB, http://www.broadinstitute.org/msigdb ) using the ‘fgsea’ R package (v.1.22 RRID: SCR_020938 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: Spot-depth GSEA pathway enrichment analysis To summarize biological programs enriched in the centre and periphery of tumour microregions across sections, we first obtained the cohort-level average layer correlation coefficient.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: 63 ) and GSEA with the clusterProfiler package (MsigDB H, C2 or C5 database) within the R environment.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: The ranked genes were used for GSEA using the fgsea package in R.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: Differentially regulated pathways were identified using gene set enrichment analysis from the GSEA (Broad Institute) package based on signatures from MSigDB (MSigDB_Hallmark_2020) 121 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: For a – c , scale bars, 40 μm. d , GSEA enrichment analysis between genes upregulated (upDEGs) after Pspc1 depletion and upregulated DEGs after Tet2 KO in mES cells.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: Among the significant ligand–receptors ( P < 0.001), we selected ligands or receptors identified in HSC/MPPs and used to communicate with vascular endothelial cells, and performed gene set enrichment analysis (GSEA) on those using EnrichR.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Evidence: GSEA was conducted with the fgsea package v.1.30.0 by projecting the fold-change ranking onto the following MSigDB genesets ( http://www.gsea-msigdb.org/gsea/msigdb/ ): H (Hallmark), C2 CP (Curated canonical pathways), C3 (Regulatory targets) and C5 (Gene ontologies).
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Version used: **4.2.3**
- Evidence: GSEA was performed using GSEA v.4.2.3 with 1,000 times permutation and collapsing mouse genes to the chip platform Mouse_Gene_Symbol_Remapping_Human_Orthologs_MSigDB.v7.5.1.chip.
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Evidence: Gene-set enrichment analysis 68 , 69 was performed on each T cell subsets with the GSEA function of clusterProfiler 70 in R.
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Evidence: Gene set enrichment analysis (GSEA) on differentially expressed genes was performed using GSEA software (v.4.3.2) 79 , 80 , and run with the MSigDB 2022 mouse database.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: Pathway analyses GSEA 106 (v.4.2.3 desktop) and MSigDB 107 , 108 (v.7.4) were used in pathway analyses, with the following settings: filter ‘geneset min=15 max=200’.
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: GSEA was performed using the Bioconductor package fgsea with the default parameters on genes ranked by log[fold change] 91 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07752-y | PMCID: PMC11291290 | PMID: 39048822
- Evidence: We used GSEA to ascertain the significance of enrichment for the gene signature associated with cluster 3.
- Full pipeline: normalisation [DESeq2 v1.30.1, limma] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [limma] -> stage not stated [R, Seurat, fgsea]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: RNA-seq data were analysed using GSEA.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Pathway enrichment analysis was carried out using the GSEA 31 pre-ranked method using the GSEApy 76 ( https://github.com/zqfang/GSEApy ), which enables the analysis of up- and downregulated genes simultaneously.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Plasmacytoid dendritic cells control homeostasis of megakaryopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07671-y | PMCID: PMC11254756 | PMID: 38987596
- Evidence: GSEA To prepare the data for gene set enrichment analysis (GSEA), DESeq2 (v.1.30.0) analysis was performed using Galaxy with the default parameters 71 , 72 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [Monocle] -> stage not stated [DESeq2 v1.30.0, GSEA, Seurat]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: Gene set enrichment and pathway analyses We performed GSEA on gut, skin and lung tissue-resident memory T cell dataset 69 as follows: first, we downloaded raw microarray data pertaining from the GEO database (accession ID: GSE47045 , tissue-resident memory T cells: gut, lung and skin versus tissue effector-memory cells (spleen)) and extracted DEGs from each comparison using Limma R package v.3.58....
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: GSEA pathway enrichment is calculated for pre-flight, post-flight (R+1), and recovery time intervals.
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: GSEA GSEA was performed using fGSEA 78 in R with differentially expressed gene lists ranked by t -statistic.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### MYCT1 controls environmental sensing in human haematopoietic stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07478-x | PMCID: PMC11168926 | PMID: 38839950
- Evidence: 18 , as well as the genes included in the curated HSC cell type signature gene sets from the GSEA database 33 (datasets from ref.
- Full pipeline: quantification [Bioconductor] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> stage not stated [AlphaFold, GSEA, R, Seurat v3.1.2]

### Natural proteome diversity links aneuploidy tolerance to protein turnover. (Nature 2024)

- DOI: 10.1038/s41586-024-07442-9 | PMCID: PMC11153158 | PMID: 38778096
- Evidence: KEGG-pathway GSEA of these median relative expression values was performed with WebGestalt 2019 using the default settings (accessed December 2021) 82 .
- Full pipeline: read trimming [edgeR] -> quantification [R, edgeR] -> normalisation [edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold, GSEA, STRING db, data.table]

### Acquisition of epithelial plasticity in human chronic liver disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07465-2 | PMCID: PMC11153150 | PMID: 38778114
- Evidence: GSEA of differentially expressed genes was carried out using gprofiler2 (v.0.2.0) 70 using all genes detected in the compared cell groups as the background set.
- Full pipeline: quality control [Seurat v4.0.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [velocyto v0.17.17]

### Temporal dynamics of the multi-omic response to endurance exercise training. (Nature 2024)

- DOI: 10.1038/s41586-023-06877-w | PMCID: PMC11062907 | PMID: 38693412
- Evidence: In agreement with this hypothesis, gene set enrichment analysis (GSEA) of extracellular matrix proteins revealed a negative enrichment in response to endurance training, showing decreased abundance of proteins such as basement membrane proteins (Extended Data Fig.
- Full pipeline: quantification [GSEA] -> differential/statistical testing [GSEA] -> machine learning [GSEA] -> stage not stated [R]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Evidence: Moreover, gene set enrichment analysis (GSEA) revealed that PGE 2 induced specific transcriptional changes in RA CD8 + T cells related to mitochondrial and lipid metabolism (Fig.
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### Discovery of WRN inhibitor HRO761 with synthetic lethality in MSI cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07350-y | PMCID: PMC11078746 | PMID: 38658754
- Evidence: RNA-seq and GSEA RNA was extracted as described above with the only change than an on-column DNA digest was performed according to the manufacturer’s instructions (RNase-free DNase Set, 79254).
- Full pipeline: normalisation [R, fgsea] -> differential/statistical testing [DESeq2, R, fgsea] -> stage not stated [GSEA, PHENIX, SciPy]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Evidence: To evaluate the enrichment of the in vivo AKP gene expression program across samples, the enrichment scores for both the upregulated and downregulated signatures were calculated using single-sample GSEA (ssGSEA) 48 .
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **4.3.2**
- Evidence: DEGs obtained from comparing the groups ‘anti-CD3/CD28 +IL-2’ and ‘PGE 2 -treated + anti-CD3/CD28 +IL-2’ were ordered based on their log 2 fold change values and subjected to GSEA using GSEA (v.4.3.2) probing for hallmark genes from mh.all.v2023.1.Mm (MSigDB).
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: Data show FOXO1 OE epigenetic signature scores for patients with durable (patient 52, n = 616 cells; patient 54, n = 2,959 cells) and short (patient 38, n = 2,093 cells; patient 66, n = 2,355 cells) CAR T cell persistence. h , GSEA using FOXO1 OE DEGs and DEGs derived from CD39 − CD69 − TILs from adult patients with melanoma 8 .
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: To perform diffexp analyses and GSEA between individual groups within each cluster, the to_psuedobulk function from Libra was used to pull out pseudobulk count matrix of each replicate pool and clusters.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: GSEA For GSEA 9 , 86 of latent factors inferred by PEER, the C5 Gene Ontology collection (v.7.2) 87 , 88 from the Molecular Signatures Database 89 , 90 was merged with the SynGO (release 20210225) 91 biological process (BP) and cell component (CC) gene lists.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Version used: **4.3.2**
- Evidence: Gene set enrichment analysis (GSEA) was performed on unfiltered DESeq2 normalized count data using the DESeq2 package (v.1.40.2) 68 and GSEA v.4.3.2 software 69 , 70 in conjunction with MSigDB (v.2023.1).
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: Gene set enrichment analysis 54 was performed using GSEA software (v4.1.0) ( http://www.broadinstitute.org/gsea ) with 1,000 permutations.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Evidence: The GSEA was done according to a previously published method 51 .
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Matrix viscoelasticity promotes liver cancer progression in the pre-cirrhotic liver. (Nature 2024)

- DOI: 10.1038/s41586-023-06991-9 | PMCID: PMC10866704 | PMID: 38297127
- Evidence: GSEA was conducted using the preranked GSEA method within the KEGG databases with the online tool g:Profiler ( https://biit.cs.ut.ee/gprofiler/gost ).
- Full pipeline: stage not stated [GSEA, ImageJ v1.53t]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: GSEA 74 was performed on d50 versus d25 and d100 versus d50 pairwise comparisons to test enrichment in KEGG pathways or gene sets from MSigDB using the following parameters: FDR ≤ 5%, minimum gene-set size=15, maximum gene-set size=500, number of permutations = 1000.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Evidence: GSEA and data visualization Gene set enrichment methods were applied using GSEA and over-representation analysis (ORA).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Mucosal boosting enhances vaccine protection against SARS-CoV-2 in macaques. (Nature 2024)

- DOI: 10.1038/s41586-023-06951-3 | PMCID: PMC10849944 | PMID: 38096903
- Evidence: GSEA throughout the study was performed to assess enrichment in pathways.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.9a] -> quantification [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [GSEA]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: The t -statistics produced using this method can also be used as a ranking factor for input into GSEA.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **4.2.3**
- Evidence: Gene expression data were further analysed using Gene Set Enrichment Analysis (GSEA 4.2.3 software; number of permutations = 1,000) using the DAM gene set from Keren-Shaul et al.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: For Gene Set Enrichment Analysis (GSEA), genes were ranked by −log 10 ( P value) × sign(log 2 (fold change)) from DESeq2 results, and enrichment was run using the fgsea R package (v.1.28.0).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: Labeled dots represent statistically significant genes involved in apoptosis according to GSEA curated gene sets 25 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Evidence: Gene set enrichment analysis was performed with a publicly available Snakemake workflow (v.0.1.1) 67 using GSEA ( https://www.genepattern.org/modules/docs/GSEAPreranked/1 ) with the prerank function from the GSEApy 1.0.3 package 68 . ‘GO biological process sets’ gene sets were selected ( http://www.broadinstitute.org/gsea/msigdb ).
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Version used: **4.0.3**
- Evidence: Gene set enrichment analysis For the RNA-seq dataset of Spp1 and Itgb3 WT and knockout organoids, GSEA (v.4.0.3) analysis was performed using the rlog-transformed counts, with the following settings applied: number of permutations = 1000, permutation type = gene set, enrichment statistics = weighted, metric for ranking genes = Signal2Noise.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Multi-omics GSEA All omics were analysed and visualized in R (Statistical Computing, v.4.1.0).
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: Gene set enrichment analyses GSEA was performed using human homologues of normal tuft, basal, NE and ionocyte cell signatures, previously established from mouse and/or human scRNA-seq datasets 10 , as described above in the scRNA-seq-related methods and included in Supplementary Table 2 .
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Evidence: Statistics for GO were generated with GSEA and single-tailed hypergeometric test with Benjamini–Hochberg multiple hypothesis correction. hdWGCNA and Celda Modules were compared against each other for further validation.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Evidence: GSEA was conducted using the fgsea 65 (v.1.28.0) and genekitr 66 (v.1.2.5) packages, exploring GO, KEGG, REACTOME, Hallmarks, Biocarta and WikiPathways databases.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: Gene set enrichment analysis (GSEA) revealed that IFNα response, IFNγ response and TNF signalling through NF-κB were the most significantly enriched pathways in patients P1 and P2 (Fig.
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Fast GSEA (fGSEA; R implementation 59 ) with 10,000 permutations tested enrichment of WikiPathways gene sets (Supplementary Table 3 ) among differentially expressed genes.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: GSEA was performed using the fgsea 74 R package (v.1.26) with Gene Ontology biological process pathway sets from MSigDB 75 .
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Evidence: (c) Dot plot presentation of Hallmark gene sets according to GSEA for differentially expressed genes in TCF1 WT LEF1 WT and TCF1 Δ LEF1 Δ B-1a cells.
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Evidence: Pathway analysis Pathway analysis was performed using Metascape 52 or the GSEA GUI tool (v.4.3.3).
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Evidence: GSEA To identify differentially expressed gene sets associated with sensitivity and resistance to CIRc-001 across the Horizon Discovery OncoSignature cell line panel, and to CIRc-004 across the SCLC panel (Fig.
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: This 46-gene PNI/nerve injury signature was first tested on our anti-PD-1 neoadjuvant cSCC clinical trial bulk RNA-seq data using GSEA.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Excised DNA circles from V(D)J recombination promote relapsed leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-09372-6 | PMCID: PMC12443594 | PMID: 40770098
- Evidence: Identification of differentially expressed genes and GSEA analysis RNA-seq data of patients at diagnosis were downloaded from the TARGET database (dbGaP Sub-study ID: phs000464; Fig.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [Python]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: GSEA was done using the clusterProfiler R package (v.4.0.5) 62 and the Benjamini–Hochberg method was used to calculate the adjusted P values.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### Precisely defining disease variant effects in CRISPR-edited single cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09313-3 | PMCID: PMC12488502 | PMID: 40702188
- Evidence: Gene-set enrichment analysis (GSEA) of these genes identified an enrichment for T helper 1 cell (T H 1 cell) and activation pathways (Extended Data Fig.
- Full pipeline: alignment/mapping [kallisto] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> stage not stated [GSEA, R, lme4]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: In parallel, we also performed differential expression analysis using a pseudobulked generalized linear mixed model (DREAMLET 82 ), accounting for random patient and fixed tumour-site effects, and performed gene-set enrichment analysis (GSEA) with the same set of pathways.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: GSEA 77 using X p values of peptides was used to evaluate the phosphorylation levels in proteins of the mTOR signalling pathway among conditions (that is, cells stimulated with ImP versus unstimulated).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Rewiring endogenous genes in CAR T cells for tumour-restricted payload delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09212-7 | PMCID: PMC12328239 | PMID: 40604285
- Evidence: Unbiased GSEA was used on a preranked list of differentially expressed genes identified by RNA-seq analysis.
- Full pipeline: quality control [Cutadapt v2.1] -> read trimming [edgeR v3.8.5] -> alignment/mapping [HISAT2] -> normalisation [edgeR v3.8.5] -> dimensionality reduction/clustering [Seurat] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Evidence: A ranked list of coding genes was generated based on the Wald statistic in DESeq2, and subsequently processed by GSEA 55 using the R package clusterProfiler (v.4.6.2) 56 against the Hallmark gene sets from Molecular Signature Database (MSigDB) 57 to identify significantly enriched pathways.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Nerve-to-cancer transfer of mitochondria during cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09176-8 | PMCID: PMC12328229 | PMID: 40562940
- Evidence: (C) Gene Set Enrichment Analysis (GSEA) revealed significant downregulation of metabolic pathways, with the tricarboxylic acid (TCA) cycle being the most impacted in cancer cells derived from denervated tumors.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Python, SAMtools] -> quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Python] -> stage not stated [GSEA]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: Gene set enrichment analysis (GSEA) 60 was done using the GSEA-Preranked tool (v.2.07).
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: GSEA was done using previously published signatures, described in supplementary Table 8 , and expression was obtained after DEseq2 normalization.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Based on single-sample GSEA (ssGSEA) 48 conducted with the GSVA 49 R package (v.1.44.5), we observed that patients with low levels of YchrS exhibited characteristics similar to those of people with LOY DNA , whereas those with high YchrS levels resembled people with an intact Y chromosome (WTY DNA ).
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: Figure 5e was prepared using GSEA of upregulated and downregulated pathways in CREM KO versus WT CAR70–IL-15 NK cells as assessed by bulk RNA-seq.
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: This was performed by calculating the single-sample GSEA score using GSVA in R and selecting the samples above the third, second or first quantile for the respective category.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Evidence: GSEA for bulk RNA-seq data was performed using the R package fgsea (1.22.0). scRNA-seq For the scRNA-seq, hepatocytes from wild-type mice, cholangiocytes from a Rosa26 -nTnG mouse and portal mesenchyme from a PDGFRα-H2B-GFP mouse sorted for SCA1 + cells were used.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Evidence: To assess the significantly upregulated DC maturation pathways, gene set enrichment analysis (GSEA) was performed on the Stat3 −/− versus Stat3 +/+ differentially expressed genes in R using the gseGO function.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: IFNγ gene signature 2 GSEA Hallmark interferon gamma response gene set was retrieved online ( https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ ; 200 genes).
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Evidence: GSEA, gene set enrichment analysis. k – m , Schematic ( k ), immunoblot ( l ) and quantification ( m ) of the indicated proteins (Extended Data Fig.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Native nucleosomes intrinsically encode genome organization principles. (Nature 2025)

- DOI: 10.1038/s41586-025-08971-7 | PMCID: PMC12240700 | PMID: 40335690
- Evidence: ... score). e , Condensability over gene units averaged over genes belonging to five quantiles of gene expression. f , g , Gene set enrichment analysis (GSEA) of polyamine-deficient conditions Odc KO ( f ) and +DFMO ( g ) compared with the wild type.
- Full pipeline: alignment/mapping [Bowtie2, Python] -> simulation/modelling [OpenMM] -> stage not stated [GSEA, Jupyter, scikit-learn]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Evidence: For pathway-level analysis, gene lists were either submitted to EnrichR 72 – 74 or GSEA 75 , 76 (4.3.3) was used.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08885-4 | PMCID: PMC12158776 | PMID: 40240610
- Evidence: GSEA was conducted using WebGestalt 2024 against the indicated databases, with an FDR of <0.05 considered significant 50 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, scikit-learn] -> differential/statistical testing [GSEA, limma] -> stage not stated [Cellpose v2.0, STRING db]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **4.3.2**
- Evidence: For GSEA, the preprocessed expression dataset and gene sets were input into GSEA (v.4.3.2), and gene sets were ranked based on their enrichment scores calculated using the two-tailed Kolmogorov–Smirnov test.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### TGFβ links EBV to multisystem inflammatory syndrome in children. (Nature 2025)

- DOI: 10.1038/s41586-025-08697-6 | PMCID: PMC12003184 | PMID: 40074901
- Evidence: Gene set enrichment analysis GSEA was performed as previously described 57 for each individual cell based on the difference to the mean of log-normalized expression values of monocytes, B cells including plasmablasts, or T cells manually selected using cloupe (version 6.3.0) in the analysed set as pre-ranked list and 1,000 randomizations 66 , 67 .
- Full pipeline: normalisation [GSEA, R v4.1.2, Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, pheatmap]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Version used: **4.3.2**
- Evidence: GSEA GSEA was performed using GSEA v.4.3.2 software ( https://www.gsea-msigdb.org/gsea/downloads.jsp ).
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Aspirin prevents metastasis by limiting platelet TXA&lt;sub&gt;2&lt;/sub&gt; suppression of T cell immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-08626-7 | PMCID: PMC12018268 | PMID: 40044852
- Evidence: 4a (14,025 genes; Supplementary Table 3 ) was subject to single-sample Gene Set Enrichment Analysis (ssGSEA) analysis 62 . ssGSEA was used to test the relative enrichment of each gene set comprising the MsigDB C7 Immunologic signature gene sets in the total expressed gene transcriptional profile of each replicate sample. ssGSEA first calculates for each sample the differential expression of each e...
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3, QuPath]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Evidence: CloneTrack clones in the expansion phase overexpressed genes characteristic of proliferating cells ( MKI67 and others by Gene Set Enrichment Analysis ( Methods ); proliferative state) relative to all other phases, whereas effector genes ( GZMB , GZMH , NKG7 , PRF1 and JUN family genes; effector state) were modulated in the contraction phase (Fig.
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### Tumour-wide RNA splicing aberrations generate actionable public neoantigens. (Nature 2025)

- DOI: 10.1038/s41586-024-08552-0 | PMCID: PMC11903331 | PMID: 39972144
- Evidence: Pre-ranked gene set enrichment analysis (GSEA) was carried out by ranking genes with the product of their fold-change sign and the −log 10 [adjusted P value].
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, R, RSEM] -> differential/statistical testing [DESeq2, GSEA, R] -> stage not stated [AlphaFold v2.3.2, Picard]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Evidence: GSEA was performed using GSEA_4.0.3 (Broad Institute).
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### Intrinsic electrical activity drives small-cell lung cancer progression. (Nature 2025)

- DOI: 10.1038/s41586-024-08575-7 | PMCID: PMC11922742 | PMID: 39939778
- Evidence: GSEA was carried out using the pre-ranked mode with default settings 82 .
- Full pipeline: alignment/mapping [RSEM] -> machine learning [Cellpose, TrackMate] -> visualisation [QuPath v0.5.0] -> stage not stated [Enrichr, GSEA, ImageJ]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Evidence: The resulting moderated t- statistics of each gene were ranked and used as the input for gene set enrichment analysis (GSEA) using the R package clusterProfiler 65 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: Gene set enrichment analysis (GSEA) revealed that the cells from cluster 2 showed an enrichment of exhaustion gene signatures, whereas those in cluster 1 showed an enrichment of the corresponding gene signatures derived from cells from an acute infection (Fig.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: Pre-ranked gene-set enrichment analysis (GSEA 34 ; https://www.gsea-msigdb.org/gsea ) was then performed, using the R package fgsea 35 (v1.20.0; https://github.com/ctlab/fgsea ; multilevel implementation with 10000 initial permutations and no lower bound for p-value estimation), for each of the 3 comparisons of interest, based on the ranking metric TRM, and considering a collection of 3065 mouse g...
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: Pathway enrichment analysis using the MSigDB 2020 Hallmark gene set with gene set enrichment analysis (GSEA; https://www.gsea-msigdb.org/gsea/index.jsp ) indicated mTOR complex 1 (mTORC1) signalling as one of the top three downregulated pathways (Extended Data Fig.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Evidence: The Ingenuity enrichment statistics for this pathway were determined using Fischer’s Exact Test p-value with Benjamin–Hochberg correction, 4.93E-08; Z score, 2,722. b-e , RANK–RANKL-induced changes of the NF-κB, anti-apoptotic, BMP, and ERK/MAPK pathways as assessed by Gene set enrichment analysis (GSEA) enrichment plots (top panels).
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Evidence: Depth-normalized counts for pseudobulk and GSEA functional analyses of this experiment were generated using cellranger aggr.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Evidence: 3g ); and (2) GSEA of relevant cell type gene sets from the literature ( Supplementary Table 2 ), based on differentially expressed genes (DEGs) in each cluster compared with the rest, computed using the R package MAST (v.1.16.0) 62 .
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: GSEA 253 was applied to pre-ranked gene lists.
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Evidence: GSEA was performed using clusterProfiler (v.4.14.6) with genome-wide annotation for mouse org.Mm.eg.db (v.3.20.0) and the Molecular Signatures Database 71 R implementation msigdbr (v.10.0.1) 72 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: ... following electroporation with GeCas12a2 against the indicated targets in HeLa-GFP cells. h , Enrichment scores from a gene set enrichment analysis (GSEA) for cells treated with nigericin or GeCas12a2 RNPs targeting the GFP transcript compared with negative controls in HeLa-GFP cells.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Postprandial lipid metabolism durably enhances T cell immunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10432-8 | PMCID: PMC13293855 | PMID: 42056521
- Evidence: Representative FACS plot (upper) and bar graph of gMFI of dyes were shown (lower) (n = 4). j , GSEA analysis using MSigDB C7 database selected for CD8 + T cell subset. k , Tabulated data of DE peaks from ATAC-Seq on naïve ex vivo fasted and fed CD8 + T cells and their 24 hr TCR activated cells (n = 3 mice). l-m , Human ex vivo pre- and post-CD8 + T cells were subjected to bulk RNA –sequencing (n =...
- Full pipeline: stage not stated [GSEA]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: Pathway enrichment was performed using GSEApy (GSEA or over-representation analysis with Fisher’s exact test and Benjamini–Hochberg correction).
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Netrin1 blockade alleviates resistance to chemotherapy in pancreatic cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10436-4 | PMCID: PMC13275303 | PMID: 42020751
- Evidence: GSEA was performed to identify biological pathways and functions enriched in the DEGs between experimental groups (for example, pre- versus post-treatment, or PR versus SD, according to the RECIST 1.1 classification).
- Full pipeline: quality control [MultiQC v1.23] -> read trimming [Trim Galore] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, tidyverse] -> stage not stated [Bioconductor, GSEA, R v4.3]

### A spatial atlas of the healthy human liver from live donors. (Nature 2026)

- DOI: 10.1038/s41586-026-10377-y | PMCID: PMC13216088 | PMID: 41986723
- Evidence: GSEA 29 was performed using version 3.0 with default parameters using the gene sets Hallmark and KEGG.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> machine learning [QuPath] -> visualisation [Scanpy v1.10.0] -> stage not stated [AnnData, Cellpose, GSEA]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: For gene set enrichment analysis (GSEA), two methods were applied: preranked GSEA (fgsea 67 v.1.24.0) and single-sample GSEA (ssGSEA 68 implemented in GSVA v.1.46.0).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: P values, Wilcoxon rank-sum test (two-tailed) after Benjamini–Hochberg correction. k , In vitro decidualized HuFs recapitulated the DSC4 transcriptomic signatures (left), manifested by CNR1 (right). l , Gene set enrichment analysis (GSEA) of DSC3 versus DSC4 responses to mAEA after in vitro decidualization. mAEA induces pro-apoptotic genes in DSC3, which were repressed in DSC4.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Version used: **4.3.2**
- Evidence: GSEA was performed using the GSEA v.4.3.2 software provided by the Broad Institute 85 , using the non-preranked whole DRG genome and Hallmark_MSigDB gene sets.
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Evidence: GSEA was done using the GSEA desktop v.4.3.3 (ref.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: Single-cell GSEA was performed using ssGSEA ( https://rpubs.com/pranali018/SSGSEA ).
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: We performed GSEA with DEGs from a putative recent GC emigrant cluster using the fgsea package v.1.24.0.
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Evidence: First, we performed GO analysis to identify over-represented biological processes in each metaprogram as described in section: GO and gene set enrichment (GSEA) analysis.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: 2g was executed using SynGo 79 , using the ‘brain expressed’ background Gene Set Enrichment Analysis setting of ‘min. gene count per term’ set to five and considering the function (biological processes) readout.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: Data were analysed using one-way ANOVA with Tukey’s multiple-comparisons test. g , Gene set enrichment analysis (GSEA) of hallmark pathways in subpopulations of myeloid cells between shCtr and sh Lcn2 tumours from e .
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Evidence: Differential gene expression analysis, GSEA and variant allele frequency calculation Whole-exome sequencing and RNA-seq data for P12 and P13 from post-treatment samples were analysed using the bioinformatics software pipeline.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### In vivo base editing of Chd3 rescues behavioural abnormalities in mice. (Nature 2026)

- DOI: 10.1038/s41586-026-10113-6 | PMCID: PMC12999480 | PMID: 41708849
- Evidence: ...E) mice versus Chd3 +/+ (NT-TeABE) (downregulated) ( c ) and Chd3 hR1025W/+ (TeABE) mice versus Chd3 hR1025W/+ (NT-TeABE) (upregulated) ( f ). d, g , Gene Set Enrichment Analysis (GSEA) plots showing enrichment scores for the neuroactive ligand-receptor interaction gene set in c and f .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> stage not stated [GSEA]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: For GSEA, the genes were first ranked by the mean edge weight in corresponding samples and H, C5, C6 and C7 collections from the Molecular Signatures Database were used for annotation.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: Differentially enriched Gene Ontology (GO) biological pathways were identified using EnrichR ( https://maayanlab.cloud/Enrichr/ ) and Gene Set Enrichment Analysis (GSEA).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: For more details on ssGSEA, see the original references 27 , 96 and the documentation of the single-sample GSEA module in GenePattern ( www.genepattern.org/modules/docs/ssGSEAProjection/4/ ).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Tumour-brain crosstalk restrains cancer immunity via a sensory-sympathetic axis. (Nature 2026)

- DOI: 10.1038/s41586-025-10028-8 | PMCID: PMC12935554 | PMID: 41639447
- Evidence: The combination of VSN and sympathetic nerve signature genes were translated to human gene symbols (Ensembl) and were used to score individual TCGA tumour expression profiles through single-sample Gene Set Enrichment Analysis (ssGSEA), implemented via GenePattern ( https://cloud.genepattern.org/gp/pages/index.jsf ).
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [GSEA, ImageJ, QuPath]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: GSEA was run on metafor analysis output to determine enriched pathways using the fgsea package (v.1.3.0).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Polyamine-dependent metabolic shielding regulates alternative splicing. (Nature 2026)

- DOI: 10.1038/s41586-025-09965-1 | PMCID: PMC12999471 | PMID: 41535471
- Evidence: ...perturbations consistent with AMD1 silencing in DU145 cells, using EventPointer pipeline with Fisher, Poisson binomial, gene set enrichment analysis (GSEA) and Wilcoxon tests.
- Full pipeline: stage not stated [AlphaFold, GSEA]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Evidence: GSEA of the gene modules GSEA was performed using MSigDB (v.7.5.1) pathways and custom gene sets derived from the existing literature 33 , 68 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Derivation of GSEA scores ssGSEA scores were calculated from transcriptome profiles for each subject using the ssGSEA module (v.10.1.0) implemented in GenePattern 90 .
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Albumin orchestrates a natural host defence mechanism against mucormycosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09882-3 | PMCID: PMC12804082 | PMID: 41501454
- Evidence: RNA-seq enrichment analysis The GO enrichment analysis performed using the gene set enrichment analysis (GSEA) 71 method as previously implemented by the web-based application FungiFun3 ( https://fungifun3.hki-jena.de/ ) 72 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> differential/statistical testing [R v4.3.1] -> visualisation [R v4.3.1] -> stage not stated [Fiji, GSEA, ImageJ, pheatmap]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: Integrating spatially informed interaction analysis with single-sample Gene Set Enrichment Analysis (ssGSEA) of peripheral blood-circulating T cells revealed age-linked attenuation of Notch1/3 and IL-7 signalling (Fig.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: Gene set enrichment analysis (GSEA) was conducted using the clusterProfiler package, leveraging gseKEGG, gseGO and gsePathway for pathway enrichment analysis 75 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: Pathway analysis Gene-set enrichment analysis (GSEA) was performed to determine which predefined sets of genes were significantly enriched across the plasticity paradigms 54 .
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Genes colored in red are also upregulated by BBP. i , Gene Set Enrichment Analysis of the upregulated genes upon BPA exposure. j , Gene Set Enrichment Analysis of the upregulated genes upon BBP exposure. k , Dot plot showing the variance-scaled, log-transformed expression of the genes (x-axis) which are upregulated by both BPA and BBP in non-ciliated cells (y-axis) in in vivo fetal uterine epithel...
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: Differentially expressed genes were ranked by log 2 (fold change expression) and used for gene set enrichment analysis (GSEA) on the Hallmark gene set from msigdbr (v.7.5.1), a previously published GR-activity signature 16 or a newly developed PR-activity signature 17 (Extended Data Table 3 ), using clusterProfiler 57 (v.3.18.1), (pvalueCutoff = 0.05, pAdjustMethod = “BH”).
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Evidence: GSEA was based on clusterProfiler (v.3.14.3) R package 73 . log 2 (fold change) was calculated between the mature M cells and enterocytes.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: We used two different sources for the functional signatures: (1) previous publications, for which we provide the whole list of genes reported and used in Supplementary Table 2 ; and (2) public databases such as gene ontology (GO) and gene set enrichment analysis (GSEA).
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Evidence: The x-axis represents log 2 fold-change in gene expression, while the y-axis represents the -log 10 (q-value). b , Gene Set Enrichment Analysis results showing pathways enriched in luminal B breast cancer cases with these SVs.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Evidence: ...mples were created by averaging the expression of each gene in each individual sample from snRNA-seq data, processed by gene set enrichment analysis (GSEA) with normalized enrichment scores and nominal P values determined by 1,000 permutations of gene labels using permutation tests.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Evidence: We also used the UniProt database ( https://www.uniprot.org ); gene sets for GSEA ( https://www.gsea-msigdb.org/gsea/index.jsp ); human genome reference GRCh38 and human V(D)J reference ( https://www.10xgenomics.com/support/software/cell-ranger/downloads ); and reprocessed data from GEO ( GSE221553 ) 31 .
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: BrdU (red), GLUL (yellow) and DNA (blue) are shown. k – m , Spatial transcriptomics gene set enrichment analysis (GSEA) for MAPK upregulated genes ( k ), MAPK downregulated genes ( l ) and translation reactome pathway ( m ); MAPK GSEA is from a day 10 Braf V600E -mutated liver.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Evidence: To detect enrichment of PB-T RM gene signature, we performed GSEA using the differential expression results with the fgsea (v.1.30.0) library in R (v.4.4.1) 48 .
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Bach1 derepression is neuroprotective in a mouse model of Parkinson's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2111643118 | PMCID: PMC8694049 | PMID: 34737234
- Evidence: The obtained Bach1-ARE and Bach1-non-ARE gene signatures were used to evaluate the enrichment of gene sets using gene set enrichment analysis [GSEA ( 28 )].
- Full pipeline: stage not stated [GSEA]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: GSEA software from the Broad Institute ( 75 , 76 ) was used to perform GSEA.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Evidence: Custom gene set for GSEA analysis was built from curated gene lists available from Molecular Signature Database ( http://www.gsea-msigdb.org/gsea/index.jsp ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Critical regulation of follicular helper T cell differentiation and function by Gα<sub>13</sub> signaling. (PNAS 2021)

- DOI: 10.1073/pnas.2108376118 | PMCID: PMC8639339 | PMID: 34663730
- Evidence: Gene set enrichment analysis (GSEA) of Tfh cells compared to non-Tfh cells yielded a positive correlation with genes signatures associated with RhoA and RhoGTPase effectors, suggesting that RhoA activation is positively correlated with human Tfh cell lineage program ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Evidence: GSEA was carried out using signal-to-noise as the ranking metric and with the “weighted” scoring scheme.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### Engineered SARS-CoV-2 receptor binding domain improves manufacturability in yeast and immunogenicity in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2106845118 | PMCID: PMC8463846 | PMID: 34493582
- Version used: **4.1.0**
- Evidence: Gene set enrichment analysis (GSEA) was performed with GSEA 4.1.0 using Wald statistics calculated by DESeq2 ( 62 ) and gene sets from yeast GO Slim ( 63 ).
- Full pipeline: differential/statistical testing [DESeq2, GSEA v4.1.0] -> stage not stated [ImageJ, edgeR v3.26.8]

### Functional succinate dehydrogenase deficiency is a common adverse feature of clear cell renal cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2106947118 | PMCID: PMC8488664 | PMID: 34551979
- Evidence: S9 ) The GSEA platform ( 47 , 48 ) was used for Pathway Enrichment Analysis. ccRCC KIRC data were downloaded from TCGA.
- Full pipeline: stage not stated [GSEA, ImageJ]

### The p53 transcriptional response across tumor types reveals core and senescence-specific signatures modulated by long noncoding RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2025539118 | PMCID: PMC8346867 | PMID: 34326251
- Evidence: Gene sets from the Molecular Signature Database were downloaded from the GSEA ( 46 ) webpage ( https://www.gsea-msigdb.org/gsea ) ( 47 ).
- Full pipeline: alignment/mapping [StringTie, TopHat] -> normalisation [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Evidence: Indeed, gene set enrichment analysis (GSEA) revealed significant overlap of repressed genes between the pharmacologic (iBRD9 and dBRD9) and genetic loss-of-function models, with the majority of dBRD9-repressed genes expressed at lower levels in KO BMDMs ( Fig.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Targeting Axl favors an antitumorigenic microenvironment that enhances immunotherapy responses by decreasing Hif-1α levels. (PNAS 2021)

- DOI: 10.1073/pnas.2023868118 | PMCID: PMC8307381 | PMID: 34266948
- Evidence: Transcriptomic analyses of the Axl -null tumors 5 wks after tumor onset suggested a dampening of “hypoxia” and “angiogenesis” and an enhancement of “activation of immune response” by gene set enrichment analyses (GSEA) ( Fig.
- Full pipeline: stage not stated [GSEA]

### Single-cell analyses of renal cell cancers reveal insights into tumor microenvironment, cell of origin, and therapy response. (PNAS 2021)

- DOI: 10.1073/pnas.2103240118 | PMCID: PMC8214680 | PMID: 34099557
- Evidence: ( A ) Pathway enrichments identified by GSEA of single-cell (SC) data for ccRCC tumor epithelial cells vs. the P-CO PT-B cells (first column) or the common PT-A cell population (second column).
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [GSEA]

### LRRC8A-containing chloride channel is crucial for cell volume recovery and survival under hypertonic conditions. (PNAS 2021)

- DOI: 10.1073/pnas.2025013118 | PMCID: PMC8201826 | PMID: 34083438
- Evidence: Genes were then ranked by RRA, and a gene set enrichment analysis (GSEA) ( 57 ) was performed against the entire Kyoto Encyclopedia of Genes and Genomes (KEGG) database ( SI Appendix , Table S3 ).
- Full pipeline: differential/statistical testing [ggplot2 v3.1.0] -> visualisation [ggplot2 v3.1.0] -> stage not stated [GSEA]

### AGO2 promotes tumor progression in KRAS-driven mouse models of non-small cell lung cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2026104118 | PMCID: PMC8157917 | PMID: 33972443
- Evidence: To determine whether Ago2 ablation reduced KRAS-dependent gene expression in the same lesions, we subjected nodule isolates to RNA sequencing (RNA-seq), then performed gene set enrichment analysis (GSEA) employing signatures defined in KRAS-driven mouse lung cancer ( 37 ).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> differential/statistical testing [fgsea, limma] -> stage not stated [GSEA]

### Establishment of bovine expanded potential stem cells. (PNAS 2021)

- DOI: 10.1073/pnas.2018505118 | PMCID: PMC8053967 | PMID: 33833056
- Evidence: In comparison to bovine fibroblasts, bEPSCs had significantly higher expression of genes functioning in cell cycle and oxidative phosphorylation in Gene Set Enrichment Analysis (GSEA) ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### TAp73 represses NF-κB-mediated recruitment of tumor-associated macrophages in breast cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2017089118 | PMCID: PMC7958209 | PMID: 33649219
- Evidence: ( E ) An enrichment map generated from GSEA results and visualized by Cytoscape EnrichmentMap and AutoAnnotate application, showing biological pathways enriched in TAp73 low versus TAp73 high.
- Full pipeline: visualisation [Cytoscape, GSEA]

### IDO1 scavenges reactive oxygen species in myeloid-derived suppressor cells to prevent graft-versus-host disease. (PNAS 2021)

- DOI: 10.1073/pnas.2011170118 | PMCID: PMC7958359 | PMID: 33649207
- Evidence: ( D ) GSEA enrichment plots for classifying significant genes of IDO-KO GVHD hosts in terms of free radical scavenging function.
- Full pipeline: stage not stated [GSEA]

### Aryl hydrocarbon receptor is essential for the pathogenesis of pulmonary arterial hypertension. (PNAS 2021)

- DOI: 10.1073/pnas.2023899118 | PMCID: PMC7980441 | PMID: 33836606
- Evidence: Gene set enrichment analysis (GSEA) revealed that genes involved in chemokine secretion were enriched in Ahr +/+ SuHx rats ( Fig.
- Full pipeline: stage not stated [GSEA]

### Activation of NF-κB and p300/CBP potentiates cancer chemoimmunotherapy through induction of MHC-I antigen presentation. (PNAS 2021)

- DOI: 10.1073/pnas.2025840118 | PMCID: PMC7923353 | PMID: 33602823
- Evidence: ( B ) Gene set enrichment analysis (GSEA) was applied to expression profiles specific to each treatment group relative to Ctrl.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### CD20 as a gatekeeper of the resting state of human B cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021342118 | PMCID: PMC7896350 | PMID: 33563755
- Evidence: For this, we analyzed the transcriptome profile of B cells from CLL patients ( 27 ) that have relapsed after a combined RTX treatment (RTX ± fludarabine) for the expression of PC-specific genes in a gene set enrichment analysis (GSEA) and compared this gene set with Ramos WT and CD20KO-L cells ( Fig.
- Full pipeline: normalisation [fgsea] -> differential/statistical testing [R, limma] -> stage not stated [CellProfiler v3.0.0, GSEA]

### OCT4 induces embryonic pluripotency via STAT3 signaling and metabolic mechanisms. (PNAS 2021)

- DOI: 10.1073/pnas.2008890118 | PMCID: PMC7826362 | PMID: 33452132
- Evidence: We further validated this result with Gene Set Enrichment Analysis by comparing the rank of differentially expressed genes between E4.5 EPI (PrE)/E4.0 TE and E4.5 EPI (PrE)/E4.5 MUT ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> variant calling [WGCNA] -> quantification [Bioconductor, HTSeq] -> dimensionality reduction/clustering [Bioconductor, WGCNA] -> differential/statistical testing [GSEA, R]

### Permissive selection followed by affinity-based proliferation of GC light zone B cells dictates cell fate and ensures clonal breadth. (PNAS 2021)

- DOI: 10.1073/pnas.2016425118 | PMCID: PMC7812803 | PMID: 33419925
- Evidence: To investigate distinctive biological features of the clusters, we performed Gene Set Enrichment Analysis (GSEA).
- Full pipeline: dimensionality reduction/clustering [GSEA]

### Synthetical lethality of Werner helicase and mismatch repair deficiency is mediated by p53 and PUMA in colon cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2211775119 | PMCID: PMC9907101 | PMID: 36508676
- Evidence: Gene Set Enrichment Analysis (GSEA) revealed that p53 and apoptosis pathways are among the most significantly activated pathways by WRN KD ( Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [GSEA]

### PROX1 transcription factor controls rhabdomyosarcoma growth, stemness, myogenic properties and therapeutic targets. (PNAS 2022)

- DOI: 10.1073/pnas.2116220119 | PMCID: PMC9894179 | PMID: 36459642
- Evidence: ...dels, histology and immunohistochemistry, RNA extraction and quantitative real time PCR, protein extraction and Western blotting analysis, RNAseq and GSEA, drug sensitivity and resistance testing (DSRT), and statistical analyses are also included in the SI Appendix for Materials and Methods .
- Full pipeline: differential/statistical testing [GSEA]

### Deletion of <i>Jazf1</i> gene causes early growth retardation and insulin resistance in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2213628119 | PMCID: PMC9894197 | PMID: 36442127
- Evidence: RNA-Seq and Gene Set Enrichment Analysis (GSEA).
- Full pipeline: stage not stated [GSEA, ImageJ]

### EBF1 is continuously required for stabilizing local chromatin accessibility in pro-B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2210595119 | PMCID: PMC9860308 | PMID: 36409886
- Evidence: ( H ) Gene set enrichment analysis (GSEA) of genes upregulated after 24 h of EBF1 expression ( 12 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA, featureCounts]

### Sequestration of a dual function DNA-binding protein by <i>Vibrio cholerae</i> CRP. (PNAS 2022)

- DOI: 10.1073/pnas.2210115119 | PMCID: PMC9674212 | PMID: 36343262
- Evidence: Transcriptomic data were subjected to GO analysis using the GSEA-PRO v3 online tool ( gseapro.molgenrug.nl/ ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> stage not stated [GSEA, ImageJ]

### Superenhancer drives a tumor-specific splicing variant of MARCO to promote triple-negative breast cancer progression. (PNAS 2022)

- DOI: 10.1073/pnas.2207201119 | PMCID: PMC9674263 | PMID: 36343244
- Evidence: ( H ) GSEA plots showing the enrichment of metastasis- and progenitor-related gene sets in high-TST-burden patients compared to low patients.
- Full pipeline: stage not stated [GSEA]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: Gene Set Enrichment Analysis (GSEA) ( 51 ) of the RNA-seq data re-emphasized the role of Pi3k/Akt/mTOR signaling by identifying the activation of mTORC1 in these tumors ( Fig.
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Combination of common mtDNA variants results in mitochondrial dysfunction and a connective tissue dysregulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212417119 | PMCID: PMC9659340 | PMID: 36322731
- Evidence: Pathway enrichment was performed on control vs. treatment samples using gene set enrichment analysis (GSEA) ( 48 , 49 ) version 4.1.0 using a weighted scoring scheme and Hallmark and C2 CP gene sets.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [R, limma] -> stage not stated [GSEA]

### Up-regulation of BTN3A1 on CD14<sup>+</sup> cells promotes Vγ9Vδ2 T cell activation in psoriasis. (PNAS 2022)

- DOI: 10.1073/pnas.2117523119 | PMCID: PMC9636952 | PMID: 36288286
- Evidence: Deep analysis was further performed based on DEGs of protein coding genes (fold change >1.5, P < 0.05), including GO analysis using DAVID and GSEA (Broad Institute).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Inhibition of FOXP3 by stapled alpha-helical peptides dampens regulatory T cell function. (PNAS 2022)

- DOI: 10.1073/pnas.2209044119 | PMCID: PMC9586281 | PMID: 36227917
- Evidence: Gene set enrichment analysis (GSEA) found that Treg cells from SAH(229–259) C -treated animals had expression profiles that mirrored murine Foxp3- deficient hybridomas ( 56 ) ( Fig.
- Full pipeline: stage not stated [GSEA]

### LYL1 facilitates AETFC assembly and gene activation by recruiting CARM1 in t(8;21) AML. (PNAS 2022)

- DOI: 10.1073/pnas.2213718119 | PMCID: PMC9586329 | PMID: 36215477
- Evidence: Gene set enrichment analysis (GSEA) of the RNA-seq data (shLYL1 vs. shNC) showed that genes directly activated by AE are significantly down-regulated in the LYL1 knockdown (KD) group ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Attenuation of relapsing fever neuroborreliosis in mice by IL-17A blockade. (PNAS 2022)

- DOI: 10.1073/pnas.2205460119 | PMCID: PMC9586318 | PMID: 36215473
- Evidence: Gene Set Enrichment Analysis (GSEA) confirmed significant enrichment of genes related to the IL-17 signaling pathway ( Fig.
- Full pipeline: stage not stated [GSEA]

### Ovarian cancer cell fate regulation by the dynamics between saturated and unsaturated fatty acids. (PNAS 2022)

- DOI: 10.1073/pnas.2203480119 | PMCID: PMC9564215 | PMID: 36197994
- Evidence: ( F ) Enrichment plots generated by Gene Set Enrichment Analysis of gene expression (RNA-seq normalized counts) in OVCAR-5 shSCD vs. shCtrl using Hallmark and C2 gene sets from Molecular Signatures Database.
- Full pipeline: normalisation [GSEA] -> differential/statistical testing [ImageJ, edgeR] -> stage not stated [RSEM]

### Monosomy X in isogenic human iPSC-derived trophoblast model impacts expression modules preserved in human placenta. (PNAS 2022)

- DOI: 10.1073/pnas.2211073119 | PMCID: PMC9546589 | PMID: 36161909
- Evidence: GSEA using clusterProfiler ( 111 ) was performed on all genes ranked by DESeq2’s Wald statistic in three separate conditions, as well as the average of their quantile-normalized Wald scores to ensure equal weighting.
- Full pipeline: normalisation [GSEA, clusterProfiler] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler] -> stage not stated [WGCNA]

### TGFB2-AS1 inhibits triple-negative breast cancer progression via interaction with SMARCA4 and regulating its targets <i>TGFB2</i> and <i>SOX2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2117988119 | PMCID: PMC9522332 | PMID: 36126099
- Evidence: ( E ) GSEA of microarray profiles from MDA-231 with TGFB2-AS1 knockdown matching with TGFβ activated gene set.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5] -> stage not stated [GSEA, Galaxy, MACS2 v2.1.2]

### Monocytes maintain central nervous system homeostasis following helminth-induced inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2201645119 | PMCID: PMC9478671 | PMID: 36070344
- Version used: **4.0.3**
- Evidence: Up-regulated and down-regulated genes were analyzed through GSEA (v4.0.3) to identify enriched pathways.
- Full pipeline: stage not stated [GSEA v4.0.3, ImageJ v1.52a, Seurat]

### Hippo signaling cofactor, WWTR1, at the crossroads of human trophoblast progenitor self-renewal and differentiation. (PNAS 2022)

- DOI: 10.1073/pnas.2204069119 | PMCID: PMC9457323 | PMID: 36037374
- Evidence: Unbiased gene set enrichment analysis (GSEA) of RNA-seq data showed that loss of WWTR1 in human TSCs down-regulated transcription of various genes in the Wingless/Integrate (WNT) signaling pathway ( Fig.
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA, MACS2]

### Comparative genomics of mortal and immortal cnidarians unveils novel keys behind rejuvenation. (PNAS 2022)

- DOI: 10.1073/pnas.2118763119 | PMCID: PMC9459311 | PMID: 36037356
- Evidence: GSEA was performed with the fgsea ( 48 ) package, after adapting the human Molecular Signatures Database (MSigDB) ( 49 ) to the genome of T. dohrnii .
- Full pipeline: alignment/mapping [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [AlphaFold v2.1.2, BUSCO, ChimeraX, GSEA, fgsea]

### 3D chromatin remodeling potentiates transcriptional programs driving cell invasion. (PNAS 2022)

- DOI: 10.1073/pnas.2203452119 | PMCID: PMC9457068 | PMID: 36037342
- Evidence: See SI Appendix , Materials and Methods for detailed data processing, analysis, full GSEA gene pathway names, and the quantitative real-time PCR protocol.
- Full pipeline: quality control [R] -> stage not stated [DESeq2, GSEA, ImageJ, MACS2]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### Chromatin structure undergoes global and local reorganization during murine dendritic cell development and activation. (PNAS 2022)

- DOI: 10.1073/pnas.2207009119 | PMCID: PMC9407307 | PMID: 35969760
- Evidence: ( F ) GSEA comparing WT CDPs with Irf8 −/− CDPs for genes included in the 942 genomic regions analyzed in E .
- Full pipeline: stage not stated [GSEA]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Evidence: GSEA was performed with ranked ratios of gene expression in CD4 + T cells or CD8 + T cells from normal-appearing brain vs. blood, GBM vs. blood, and GBM vs. normal-appearing brain.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### Early B cell factor 4 modulates FAS-mediated apoptosis and promotes cytotoxic function in human immune cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208522119 | PMCID: PMC9388157 | PMID: 35939714
- Evidence: ( B ) GSEA of mRNA-seq data from empty vector vs.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Tcf-1 promotes genomic instability and T cell transformation in response to aberrant β-catenin activation. (PNAS 2022)

- DOI: 10.1073/pnas.2201493119 | PMCID: PMC9371646 | PMID: 35921443
- Evidence: ( E ) GSEA/MSigDB of cluster 1 gene expression showing significant signatures (normalized enrichment score (NES) > 1 Faulse Discovery Rate (FDR) < 0.2) with relevant genome maintenance programs labeled and highlighted in red.
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA] -> stage not stated [HOMER, Metascape]

### Inhibition of CDK8/19 Mediator kinase potentiates HER2-targeting drugs and bypasses resistance to these agents in vitro and in vivo. (PNAS 2022)

- DOI: 10.1073/pnas.2201073119 | PMCID: PMC9371674 | PMID: 35914167
- Evidence: We have used gene set enrichment analysis (GSEA) ( 31 ) to determine which of the 50 hallmark pathways were differentially affected by lapatinib alone and by lapatinib + senexin B combination.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [GSEA] -> stage not stated [edgeR]

### Tumor-polarized GPX3&lt;sup&gt;+&lt;/sup&gt; AT2 lung epithelial cells promote premetastatic niche formation. (PNAS 2022)

- DOI: 10.1073/pnas.2201899119 | PMCID: PMC9371733 | PMID: 35914155
- Evidence: Gene Ontology, Kyoto encyclopedia of genes and genomes (KEGG), and GSEA pathway enrichment analyses of differentially expressed genes (DEGs) were performed by clusterProfiler (v 3.14.0) package.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Monocle, clusterProfiler v3.14.0] -> differential/statistical testing [GSEA, clusterProfiler v3.14.0] -> stage not stated [Seurat v3.0.2]

### CFI-402257, a TTK inhibitor, effectively suppresses hepatocellular carcinoma. (PNAS 2022)

- DOI: 10.1073/pnas.2119514119 | PMCID: PMC9371652 | PMID: 35914158
- Evidence: Lower : GSEA of SASP expression data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### ZAP isoforms regulate unfolded protein response and epithelial- mesenchymal transition. (PNAS 2022)

- DOI: 10.1073/pnas.2121453119 | PMCID: PMC9351355 | PMID: 35881805
- Evidence: Gene Set Enrichment Analysis (GSEA) for Gene Ontology Cellular Component (GOCC) using the expression of all of the genes showed that compared to the ZAPL-KO cells, the ZAPS-KO cells up-regulated genes in ribosome-related terms (cytoplasmic ribosome and polysome) and nuclear component terms (chromosomal telomeric region and DNA package complex), while down-regulated genes in secretory and membrane ...
- Full pipeline: stage not stated [GSEA]

### EBNA2-EBF1 complexes promote MYC expression and metabolic processes driving S-phase progression of Epstein-Barr virus-infected B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2200512119 | PMCID: PMC9335265 | PMID: 35857872
- Evidence: Next, we performed a gene set enrichment analysis (GSEA) with DE, protein-coding genes (FDR < 0.01) to identify cellular processes affected in EBVΔα1-infected B cells at each time point.
- Full pipeline: differential/statistical testing [DESeq2, GSEA]

### Inhibitors of eIF4G1-eIF1 uncover its regulatory role of ER/UPR stress-response genes independent of eIF2α-phosphorylation. (PNAS 2022)

- DOI: 10.1073/pnas.2120339119 | PMCID: PMC9335335 | PMID: 35857873
- Evidence: Likewise, using Gene Set Enrichment Analysis, we found a substantial overlap of affected pathways among the up-regulated gene sets of both drugs, including UPR, UV response, apoptosis, mTORC signaling, tumor necrosis factor-α signaling, and G2/M checkpoint ( Fig.
- Full pipeline: stage not stated [GSEA]

### Splice factor polypyrimidine tract-binding protein 1 (Ptbp1) primes endothelial inflammation in atherogenic disturbed flow conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2122227119 | PMCID: PMC9335344 | PMID: 35858420
- Evidence: Statistical analysis was performed as follows: ( A ) Kruskal–Wallis and Dunn’s post hoc analysis, ( B ) Mann–Whitney test, ( C ) Kolmogorov—Smirnov analysis integrated into the GSEA work flow, and ( G and H ) Wilcoxon rank test, comparing gene expression levels in EC4 to EC5 and EC6 to EC7, * P < 0.05, ** P < 0.01, **** P < 0.0001.
- Full pipeline: differential/statistical testing [GSEA, Scanpy]

### Nuclear-localized, iron-bound superoxide dismutase-2 antagonizes epithelial lineage programs to promote stemness of breast cancer cells via a histone demethylase activity. (PNAS 2022)

- DOI: 10.1073/pnas.2110348119 | PMCID: PMC9303987 | PMID: 35858297
- Evidence: In fact, gene set enrichment analysis (GSEA) of Hallmark genes showed up-regulation of genes associated with EMT ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [edgeR] -> stage not stated [Cytoscape, GSEA, STRING db]

### Specialization of the photoreceptor transcriptome by &lt;i&gt;Srrm3&lt;/i&gt;-dependent microexons is required for outer segment maintenance and vision. (PNAS 2022)

- DOI: 10.1073/pnas.2117090119 | PMCID: PMC9303857 | PMID: 35858306
- Evidence: Moreover, differential gene-expression analyses at each time point revealed much fewer down-regulated genes [−log 2 FC(MUT/WT) < 1.5] in MUT eyes at 48, 60, and 72 hpf than at 5 dpf ( Dataset S8 ), and gene set enrichment analysis (GSEA) showed no enrichment for PR-related categories among those genes ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Id3 expression identifies CD4&lt;sup&gt;+&lt;/sup&gt; memory Th1 cells. (PNAS 2022)

- DOI: 10.1073/pnas.2204254119 | PMCID: PMC9303986 | PMID: 35858332
- Evidence: Furthermore, gene set enrichment analysis (GSEA) indicated that the Tcm precursor (Tcmp) signature recently defined by Ciucci et al.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Seurat v3.5.1]

### EBF1 promotes triple-negative breast cancer progression by surveillance of the HIF1α pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2119518119 | PMCID: PMC9282371 | PMID: 35867755
- Evidence: Moreover, Gene Set Enrichment Analysis (GSEA) revealed that the EBF1 gene expression profile was negatively associated with the hallmark “hypoxia” ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### RNA m&lt;sup&gt;1&lt;/sup&gt;A methylation regulates glycolysis of cancer cells through modulating ATP5D. (PNAS 2022)

- DOI: 10.1073/pnas.2119038119 | PMCID: PMC9282374 | PMID: 35867754
- Evidence: Gene Set Enrichment Analysis found that the epithelial mesenchymal transition ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Differentiation and homeostasis of effector Treg cells are regulated by inositol polyphosphates modulating Ca&lt;sup&gt;2+&lt;/sup&gt; influx. (PNAS 2022)

- DOI: 10.1073/pnas.2121520119 | PMCID: PMC9271192 | PMID: 35776543
- Evidence: Gene set enrichment analysis (GSEA) revealed that common Treg signature genes ( 35 ) were underrepresented in IPMK-deficient Treg cells ( Fig.
- Full pipeline: stage not stated [GSEA]

### Activating STING1-dependent immune signaling in <i>TP53</i> mutant and wild-type acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2123227119 | PMCID: PMC9271208 | PMID: 35759659
- Evidence: ( A and B ) Gene set enrichment analysis (GSEA) of Hallmarks pathway for TP53 status (mutant ([MT] vs.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [ggpubr] -> stage not stated [GSEA, R, STRING db, fgsea]

### Screening membraneless organelle participants with machine-learning models that integrate multimodal features. (PNAS 2022)

- DOI: 10.1073/pnas.2115369119 | PMCID: PMC9214545 | PMID: 35687670
- Evidence: Finding Enriched Pathways with GSEA.
- Full pipeline: stage not stated [GSEA, InterProScan, XGBoost]

### Rhabdomyosarcomas are oncogene addicted to the activation of AVIL. (PNAS 2022)

- DOI: 10.1073/pnas.2118048119 | PMCID: PMC9214494 | PMID: 37146302
- Evidence: Indeed, gene set enrichment analysis (GSEA) analyses revealed the enrichment of PAX-FOXO1 gene expression signature that defines molecular classes and determines the prognosis of alveolar rhabdomyosarcomas ( 15 ), as well as a gene set found in mouse MSC cells expressing PAX-FOXO1 fusion ( 16 ) ( Fig.
- Full pipeline: stage not stated [GSEA]

### GPR174 signals via G&lt;i&gt;α&lt;/i&gt;s to control a CD86-containing gene expression program in B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2201794119 | PMCID: PMC9191659 | PMID: 35639700
- Evidence: DESeq2 was used for the gene differential expression analysis and with GSEA software.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [MACS2, pheatmap]

### A brain-enriched lncRNA shields cancer cells from immune-mediated killing for metastatic colonization in the brain. (PNAS 2022)

- DOI: 10.1073/pnas.2200230119 | PMCID: PMC9295751 | PMID: 35617432
- Evidence: Further Gene Set Enrichment Analysis (GSEA) of the RNA-seq data revealed that depletion of BMOR in 231-BM cells versus the control down-regulated several immune response pathways important for inducing the cytotoxicity of cancer cells, such as the interferon (IFN) response, such as IFN-α and IFN-γ response, and tumor necrosis factor (TNF) signaling, such as the TNF-α signaling via nuclear factor κ...
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA]

### Zinc finger protein 280C contributes to colorectal tumorigenesis by maintaining epigenetic repression at H3K27me3-marked loci. (PNAS 2022)

- DOI: 10.1073/pnas.2120633119 | PMCID: PMC9295756 | PMID: 35605119
- Evidence: RNA Sequencing and Gene Set Enrichment Analysis.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, MACS2 v2.1.6] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> visualisation [deepTools v3.1.3] -> stage not stated [GSEA]

### Single-cell transcriptomic classification of rabies-infected cortical neurons. (PNAS 2022)

- DOI: 10.1073/pnas.2203677119 | PMCID: PMC9295789 | PMID: 35609197
- Evidence: DE Analysis and GSEA.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ImageJ, R v4.1.1, Seurat v4.0, scDblFinder]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Single-sample GSEA (ssGSEA) was used to quantify the activity of gene sets compared to genes outside the gene set within a sample using the GSVA R package.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### MITF deficiency accelerates GNAQ-driven uveal melanoma. (PNAS 2022)

- DOI: 10.1073/pnas.2107006119 | PMCID: PMC9172632 | PMID: 35512098
- Evidence: Total peptide and phospho-peptide sample preparation, liquid chromatography-tandem mass spectrometry, and GSEA methods and visualization are described in SI Appendix , Supplemental Materials and Methods .
- Full pipeline: quantification [QuPath] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2 v1.30.1, R v4.0.3] -> differential/statistical testing [Cytoscape] -> visualisation [GSEA]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: Pathway enrichment was performed using Gene Set Enrichment Analysis (GSEA) version 4.1.0 using a weighted scoring scheme and Hallmark and C2 CP gene sets.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Evidence: Network Analysis and GSEA.
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### A preclinical platform for assessing antitumor effects and systemic toxicities of cancer drug targets. (PNAS 2022)

- DOI: 10.1073/pnas.2110557119 | PMCID: PMC9169916 | PMID: 35442775
- Evidence: GSEA.
- Full pipeline: read trimming [Trimmomatic] -> quantification [ImageJ] -> stage not stated [GSEA]

### Hereditary retinoblastoma iPSC model reveals aberrant spliceosome function driving bone malignancies. (PNAS 2022)

- DOI: 10.1073/pnas.2117857119 | PMCID: PMC9169787 | PMID: 35412907
- Evidence: Gene set enrichment analysis (GSEA) of transcription factor targets and oncogenic signatures identified E2F chromatin immunoprecipitation (ChIP) targets and a pRB/E2F–associated oncogenic signature as enriched in RB OBs ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Elucidation of CKAP4-remodeled cell mechanics in driving metastasis of bladder cancer through aptamer-based target discovery. (PNAS 2022)

- DOI: 10.1073/pnas.2110500119 | PMCID: PMC9169774 | PMID: 35412892
- Evidence: ( I ) Association of CKAP4 level with hallmark protein secretion from GSEA database ( P = 8.6 × 10 9 ; Pearson correlation test).
- Full pipeline: stage not stated [GSEA]

### FKBP52 and FKBP51 differentially regulate the stability of estrogen receptor in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2110256119 | PMCID: PMC9169630 | PMID: 35394865
- Evidence: Gene set enrichment analysis (GSEA) revealed that the sets of genes down-regulated and up-regulated in response to E2 exposure were positively and negatively enriched, respectively, in FKBP52-depleted cells ( Fig.
- Full pipeline: stage not stated [GSEA, QuPath v0.3.1]

### Parkinson's disease and multiple system atrophy patient iPSC-derived oligodendrocytes exhibit alpha-synuclein-induced changes in maturation and immune reactive properties. (PNAS 2022)

- DOI: 10.1073/pnas.2111405119 | PMCID: PMC8944747 | PMID: 35294277
- Evidence: ( G ) GSEA reveals groups of genes enriched or depleted in aSYN p.A53T O4 + OLCs.
- Full pipeline: differential/statistical testing [ggplot2 v3.3.0] -> stage not stated [ComplexHeatmap v2.4.3, Cytoscape, GSEA]

### Intermittent treatment of BRAF<sup>V600E</sup> melanoma cells delays resistance by adaptive resensitization to drug rechallenge. (PNAS 2022)

- DOI: 10.1073/pnas.2113535119 | PMCID: PMC8944661 | PMID: 35290123
- Evidence: ( A ) Gene set enrichment analysis (GSEA) was performed on genes associated with PC1 and PC2.
- Full pipeline: stage not stated [GSEA]

### pH-degradable, bisphosphonate-loaded nanogels attenuate liver fibrosis by repolarization of M2-type macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2122310119 | PMCID: PMC8944276 | PMID: 35290110
- Evidence: ( E ) GSEA of differentially expressed genes in AL/NP-treated livers, compared with CCl 4 fibrotic control livers, identified highly enriched genes in gene sets related to M1- vs.
- Full pipeline: differential/statistical testing [GSEA]

### A PRC2-Kdm5b axis sustains tumorigenicity of acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2122940119 | PMCID: PMC8892512 | PMID: 35217626
- Evidence: Gene set enrichment analysis (GSEA) showed the blockade of PRC2’s enzymatic activity by either inhibitor to be correlated with up-regulation of transcripts repressed by PRC2 or those related either to leukocyte differentiation or apoptosis ( Fig.
- Full pipeline: stage not stated [GSEA]

### Landscape of surfaceome and endocytome in human glioma is divergent and depends on cellular spatial organization. (PNAS 2022)

- DOI: 10.1073/pnas.2114456119 | PMCID: PMC8892282 | PMID: 35217608
- Evidence: Methods Detailed descriptions of the mouse GBM model, Western blotting, ligand uptake, biotinylation of PBMCs and CD14 + magnetic cell separation sorting, Incucyte cytotox assay, and GSEA and pathway analysis of LC-MS/MS data are listed in SI Appendix .
- Full pipeline: dimensionality reduction/clustering [R v4.0.4, ggplot2, pheatmap] -> visualisation [R v4.0.4, ggplot2, pheatmap] -> stage not stated [GSEA]

### NOXA expression drives synthetic lethality to RUNX1 inhibition in pancreatic cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2105691119 | PMCID: PMC8892327 | PMID: 35197278
- Evidence: ( H ) Gene set enrichment analysis (GSEA) of dataset, described in ( 52 ).
- Full pipeline: stage not stated [GSEA]

### Developmentally distinct CD4<sup>+</sup> T<sub>reg</sub> lineages shape the CD8<sup>+</sup> T cell response to acute <i>Listeria</i> infection. (PNAS 2022)

- DOI: 10.1073/pnas.2113329119 | PMCID: PMC8915796 | PMID: 35239442
- Evidence: Gene set enrichment analysis (GSEA) of gene clusters 1 to 3 (C1-3) revealed that C2, highly expressed before infection, was largely down-regulated from days 1 to 3 postinfection only to be partially up-regulated as part of the subsequent day 7 signature.
- Full pipeline: dimensionality reduction/clustering [GSEA]

### BEND3 safeguards pluripotency by repressing differentiation-associated genes. (PNAS 2022)

- DOI: 10.1073/pnas.2107406119 | PMCID: PMC8892337 | PMID: 35217604
- Evidence: ( D and E ) Gene set enrichment analysis (GSEA) and heatmap showing the expression of developmental genes present in 4,495 DE genes of the BEND3 RNA-seq data.
- Full pipeline: stage not stated [GSEA]

### Specialized interferon action in COVID-19. (PNAS 2022)

- DOI: 10.1073/pnas.2116730119 | PMCID: PMC8931386 | PMID: 35217532
- Evidence: Gene set enrichment analysis (GSEA) identified the Hallmark Interferon Alpha and Gamma Response gene sets as the most significant positively enriched signatures in COVID-19 patients ( Fig.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### LINE-1 expression in cancer correlates with p53 mutation, copy number alteration, and S phase checkpoint. (PNAS 2022)

- DOI: 10.1073/pnas.2115999119 | PMCID: PMC8872788 | PMID: 35169076
- Evidence: For GSEA, Spearman correlations were calculated between our LINE-1 ORF1p quantification and the log normalized quantification for each identified protein identified in at least half of the samples.
- Full pipeline: quantification [GSEA] -> normalisation [GSEA]

### CCR8-targeted specific depletion of clonally expanded Treg cells in tumor tissues evokes potent tumor immunity with long-lasting memory. (PNAS 2022)

- DOI: 10.1073/pnas.2114282119 | PMCID: PMC8851483 | PMID: 35140181
- Evidence: Gene set enrichment analysis (GSEA) of L-group 2 vs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Intravesical delivery of <i>KDM6A</i>-mRNA via mucoadhesive nanoparticles inhibits the metastasis of bladder cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2112696119 | PMCID: PMC8851555 | PMID: 35131941
- Evidence: Moreover, the results confirmed by the gene set enrichment analysis (GSEA) also demonstrated that both the focal adhesion signaling pathway (*** P < 0.001) and the CAMs signaling pathway (* P < 0.05) were significantly up-regulated in Kdm6a -null KU19-19 cells compared to those in Kdm6a -wild-type RT-4 cells ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### LINEAGE: Label-free identification of endogenous informative single-cell mitochondrial RNA mutation for lineage analysis. (PNAS 2022)

- DOI: 10.1073/pnas.2119767119 | PMCID: PMC8812554 | PMID: 35086932
- Evidence: Many of these genes were enriched in gene ontology (GO) term “GO_CC: MITOCHONDRION” with Gene Set Enrichment Analysis ( Fig.
- Full pipeline: alignment/mapping [Python, SAMtools v1.9] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [GSEA, Seurat]

### Sirt6 regulates lifespan in <i>Drosophila melanogaster</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2111176119 | PMCID: PMC8812521 | PMID: 35091469
- Evidence: GSEA ( 32 ) was performed using normalized count data.
- Full pipeline: quantification [DESeq2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2]

### Redox signaling by glutathione peroxidase 2 links vascular modulation to metabolic plasticity of breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2107266119 | PMCID: PMC8872779 | PMID: 35193955
- Evidence: ...zation, integration and clustering, cluster comparison and visualization, differential gene expression, IPA, TCGA data mining, Kaplan–Meier analysis, GSEA, and statistical analysis are described in SI Appendix .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [GSEA, UMAP]

### Genetic analysis of cancer drivers reveals cohesin and CTCF as suppressors of PD-L1. (PNAS 2022)

- DOI: 10.1073/pnas.2120540119 | PMCID: PMC8851563 | PMID: 35149558
- Evidence: Raw read counts were analyzed using DESeq2 ( 42 ) GSEA.
- Full pipeline: alignment/mapping [R, STAR v2.4.2a, featureCounts] -> quantification [DESeq2, GSEA, R, featureCounts]

### miR-182 targeting reprograms tumor-associated macrophages and limits breast cancer progression. (PNAS 2022)

- DOI: 10.1073/pnas.2114006119 | PMCID: PMC8833194 | PMID: 35105806
- Evidence: Transcriptomic Sequencing and GSEA Analyses.
- Full pipeline: stage not stated [GSEA]

### Executioner caspases 3 and 7 are dispensable for intestinal epithelium turnover and homeostasis at steady state. (PNAS 2022)

- DOI: 10.1073/pnas.2024508119 | PMCID: PMC8832966 | PMID: 35105800
- Evidence: ( G ) Gene set enrichment analyses (GSEA) for the indicated signatures.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### BRD9 regulates interferon-stimulated genes during macrophage activation via cooperation with BET protein BRD4. (PNAS 2022)

- DOI: 10.1073/pnas.2110812119 | PMCID: PMC8740701 | PMID: 34983841
- Evidence: GSEA was performed on DEGs against HALLMARK gene sets (GSEA homepage [ http://www.gsea-msigdb.org/ ], 2004 to 2017).
- Full pipeline: alignment/mapping [STAR] -> quantification [HOMER] -> stage not stated [GSEA]

### Pathogenic TNF-α drives peripheral nerve inflammation in an Aire-deficient model of autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2114406119 | PMCID: PMC8795502 | PMID: 35058362
- Evidence: ( D ) GSEA plots with murine hallmark signature datasets from MSigDB (adjusted P < 0.05, normalized enrichment score < 7).
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellChat, Seurat]

### Early antitumor activity of oral Langerhans cells is compromised by a carcinogen. (PNAS 2022)

- DOI: 10.1073/pnas.2118424119 | PMCID: PMC8784117 | PMID: 35012988
- Evidence: In agreement with the rapid DNA damage induced by the carcinogen, the analysis of gene set enrichment analysis (GSEA) revealed that cellular pathways involved in the cell cycle, DNA repair, and apoptosis, were up-regulated in epithelial cells treated with 4NQO for 1 wk and to a lesser extent for 3 wk ( Fig.
- Full pipeline: stage not stated [GSEA]

### STIM1 is a core trigger of airway smooth muscle remodeling and hyperresponsiveness in asthma. (PNAS 2022)

- DOI: 10.1073/pnas.2114557118 | PMCID: PMC8740694 | PMID: 34949717
- Evidence: Through gene set enrichment analysis (GSEA) using the reactome gene sets, numerous enriched pathways were revealed between shScramble and shSTIM1 HASMCs.
- Full pipeline: stage not stated [GSEA]

### Inhibition of EZH2 transactivation function sensitizes solid tumors to genotoxic stress. (PNAS 2022)

- DOI: 10.1073/pnas.2105898119 | PMCID: PMC8784159 | PMID: 35031563
- Evidence: ( B ) Gene set enrichment analysis (GSEA) of genes with positive Δβ, defined as [β (GSK126) − β (DMSO)], in abl cells.
- Full pipeline: stage not stated [GSEA]

### XP-524 is a dual-BET/EP300 inhibitor that represses oncogenic KRAS and potentiates immune checkpoint inhibition in pancreatic cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2116764119 | PMCID: PMC8795568 | PMID: 35064087
- Evidence: Post hoc gene set enrichment analysis (GSEA) suggested that XP-524 most significantly suppresses oncogenic KRAS signaling, as well as several associated cellular processes, including the MAPK pathway and cell cycle progression ( Fig.
- Full pipeline: stage not stated [GSEA]

### p53 deficient breast cancer cells reprogram preadipocytes toward tumor-protective immunomodulatory cells. (PNAS 2023)

- DOI: 10.1073/pnas.2311460120 | PMCID: PMC10756271 | PMID: 38127986
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: quantification [ImageJ] -> normalisation [RSEM] -> machine learning [MACS2] -> stage not stated [GSEA, Metascape, R v4.0.2]

### Genomic loci influence patterns of structural covariance in the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2300842120 | PMCID: PMC10756284 | PMID: 38127979
- Evidence: Gene Set Enrichment Analysis Highlights Pathways That Shape Patterns of Structural Covariance.
- Full pipeline: differential/statistical testing [FUMA, MAGMA, PLINK] -> stage not stated [GCTA, GSEA, LDSC]

### Tiam1 methylation by NSD2 promotes Rac1 signaling activation and colon cancer metastasis. (PNAS 2023)

- DOI: 10.1073/pnas.2305684120 | PMCID: PMC10756287 | PMID: 38113258
- Evidence: The results, which are presented in Dataset S1 , revealed that NSD2 KD was associated with downregulation of the Rac1 signaling pathway, as demonstrated by Gene Set Enrichment Analysis ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### SERS analysis of cancer cell-secreted purines reveals a unique paracrine crosstalk in MTAP-deficient tumors. (PNAS 2023)

- DOI: 10.1073/pnas.2311674120 | PMCID: PMC10756296 | PMID: 38109528
- Evidence: Furthermore, the Gene Set Enrichment Analysis (GSEA) results shown in Fig.
- Full pipeline: stage not stated [GSEA]

### PARP7-mediated ADP-ribosylation of FRA1 promotes cancer cell growth by repressing IRF1- and IRF3-dependent apoptosis. (PNAS 2023)

- DOI: 10.1073/pnas.2309047120 | PMCID: PMC10710093 | PMID: 38011562
- Evidence: To gain additional functional insight, we performed a GSEA-based pathway analysis of genes differentially expressed after FRA1 knockdown and RBN-2397 treatment and observed an enrichment of TNFα signaling, NA-sensing, apoptosis, and cell cycle genes, respectively ( Fig.
- Full pipeline: differential/statistical testing [GSEA]

### Peripheral blood TCR clonotype diversity as an age-associated marker of breast cancer progression. (PNAS 2023)

- DOI: 10.1073/pnas.2316763120 | PMCID: PMC10710020 | PMID: 38011567
- Evidence: Pre-ranked GSEA was performed using the FGSEA package (v1.24.0), while the DESeq2 package (v1.38.3) was used for the pre-ranking of gene expression.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [survival (R)] -> stage not stated [DESeq2, GSEA, QuPath, R v4.3]

### Microbiota configuration determines nutritional immune optimization. (PNAS 2023)

- DOI: 10.1073/pnas.2304905120 | PMCID: PMC10710091 | PMID: 38011570
- Evidence: Fold changes with associated genes were ranked for GSEA testing using the clusterProfiler package ( https://www.sciencedirect.com/science/article/pii/S2666675821000667 ).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Bowtie2 v2.4.2, HOMER, HUMAnN v3.0, QIIME 2 v2020.2]

### NMDAR antagonists suppress tumor progression by regulating tumor-associated macrophages. (PNAS 2023)

- DOI: 10.1073/pnas.2302126120 | PMCID: PMC10666127 | PMID: 37967215
- Evidence: Gene set enrichment analysis (GSEA) in NK, CD4 + and CD8 + T cells indicated that KEGG pathways representing positive regulation of cell proliferation, cell activation and cell-mediated cytotoxicity were enriched and upregulated, while cell apoptosis, metabolism such as OXPHOS and ferroptosis pathways were downregulated by MK-801 treatment ( Fig.
- Full pipeline: stage not stated [GSEA]

### The adaptive antioxidant response during fasting-induced muscle atrophy is oppositely regulated by ZEB1 and ZEB2. (PNAS 2023)

- DOI: 10.1073/pnas.2301120120 | PMCID: PMC10655555 | PMID: 37948583
- Evidence: ( B ) GSEA plots for gene signatures of glycolysis, OxPhos, and muscle atrophy in fasted Zeb1 ΔSKM mice versus fasted Zeb2 ΔSKM mice.
- Full pipeline: stage not stated [GSEA, ImageJ]

### A pan-cancer analysis implicates human &lt;i&gt;NKIRAS1&lt;/i&gt; as a tumor-suppressor gene. (PNAS 2023)

- DOI: 10.1073/pnas.2312595120 | PMCID: PMC10655574 | PMID: 37931099
- Evidence: Gene set enrichment was assessed by GSEA ( 32 , 33 ).
- Full pipeline: stage not stated [GSEA]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Evidence: ( I ) Gene set enrichment analysis (GSEA) showing up-regulated and down-regulated functions and gene sets in DKO LSKs vs.
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### Targeting MFGE8 secreted by cancer-associated fibroblasts blocks angiogenesis and metastasis in esophageal squamous cell carcinoma. (PNAS 2023)

- DOI: 10.1073/pnas.2307914120 | PMCID: PMC10589644 | PMID: 37816055
- Evidence: We then performed gene set enrichment analysis (GSEA) on the TCGA database using samples from 25 patients (1/4) with high MFGE8 expression and 25 patients with low MFGE8 expression, with a significance threshold of P <0.05 and q < 0.25.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Normal and Sjogren's syndrome models of the murine lacrimal gland studied at single-cell resolution. (PNAS 2023)

- DOI: 10.1073/pnas.2311983120 | PMCID: PMC10589653 | PMID: 37812717
- Evidence: Gene Set Enrichment Analysis (GSEA; 48 ) for each of these cell types, based on a comparison of MRL/lpr female vs.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### A snoRNA-tRNA modification network governs codon-biased cellular states. (PNAS 2023)

- DOI: 10.1073/pnas.2312126120 | PMCID: PMC10576143 | PMID: 37792516
- Evidence: WT were median-normalized and tested for gene set enrichment using gene set enrichment analysis (GSEA) and MSigDB c5.all collection.
- Full pipeline: normalisation [GSEA]

### Nuclear VCP drives colorectal cancer progression by promoting fatty acid oxidation. (PNAS 2023)

- DOI: 10.1073/pnas.2221653120 | PMCID: PMC10576098 | PMID: 37788309
- Evidence: Gene set enrichment analysis (GSEA) between experimental groups revealed significant upregulation of genes that regulate fatty acid metabolism and fatty acid β-oxidation processes in cells undergoing VCP overexpression ( Fig.
- Full pipeline: stage not stated [GSEA]

### A deregulated m<sup>6</sup>A writer complex axis driven by BRD4 confers an epitranscriptomic vulnerability in combined DNA repair-targeted therapy. (PNAS 2023)

- DOI: 10.1073/pnas.2304534120 | PMCID: PMC10576145 | PMID: 37782793
- Evidence: ( K ) GSEA of m 6 A positively regulated ( Upper ) and m 6 A negatively regulated gene sets ( Lower ) from Fig.
- Full pipeline: stage not stated [GSEA]

### Characteristics and anatomic location of PD-1<sup>+</sup>TCF1<sup>+</sup> stem-like CD8 T cells in chronic viral infection and cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2221985120 | PMCID: PMC10576122 | PMID: 37782797
- Evidence: ( C ) GSEA for identifying specific gene signatures of two murine CD8 TIL subsets compared to gene signatures of LCMV stem-like and exhausted CD8 T cells.
- Full pipeline: stage not stated [Cytoscape, GSEA]

### Divergent roles for STAT4 in shaping differentiation of cytotoxic ILC1 and NK cells during gut inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2306761120 | PMCID: PMC10556635 | PMID: 37756335
- Evidence: To corroborate this hypothesis, we performed Gene Set Enrichment Analysis (GSEA), showing that genes associated with high-density p300 load (established in ref.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### A TIAM1-TRIM28 complex mediates epigenetic silencing of protocadherins to promote migration of lung cancer cells. (PNAS 2023)

- DOI: 10.1073/pnas.2300489120 | PMCID: PMC10556593 | PMID: 37748077
- Evidence: ( B ) GSEA showing that cell–cell adhesion genes are positively correlated with TIAM1 knockdown in H441 cells.
- Full pipeline: stage not stated [GSEA, MACS2]

### Causal ALS genes impact the MHC class II antigen presentation pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2305756120 | PMCID: PMC10523463 | PMID: 37722062
- Evidence: Whole-Cell Proteomics and GSEA.
- Full pipeline: stage not stated [GSEA]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Evidence: The nominal P value of all GSEA plots in Figs.
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### Serine starvation silences estrogen receptor signaling through histone hypoacetylation. (PNAS 2023)

- DOI: 10.1073/pnas.2302489120 | PMCID: PMC10515173 | PMID: 37695911
- Evidence: Comparative Gene Set Enrichment Analysis (GSEA) of expression data taken from both the ER − MDA-MB-231 and the ER + MCF7 cell lines cultured in complete vs. serine-free media confirmed an enrichment of genes belonging to the Late Estrogen Response pathway ( Fig.
- Full pipeline: stage not stated [Enrichr, GSEA]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: Gene set enrichment analysis (GSEA) ( 40 , 41 ) of these genes revealed strong enrichment of genes involved in the canonical Wnt signaling pathway ( Rps12, Nrarp, Aes, and Sox2 ), phagocytosis ( Pik3ca and Appl2 ), regulation of neuronal synaptic plasticity ( Cntn2 and Syngap1 ), Ras protein signal transduction ( Plce1, Map4 k4, Abl2, Syngap1, and Gpsm2 ), and neuron projection morphogenesis ( Map...
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### Systems-level temporal immune-metabolic profile in Crimean-Congo hemorrhagic fever virus infection. (PNAS 2023)

- DOI: 10.1073/pnas.2304722120 | PMCID: PMC10500270 | PMID: 37669378
- Evidence: The gene set enrichment analysis (GSEA) of the four modules identified a distinct pattern of innate and adaptive immunity and metabolic processes ( Fig.
- Full pipeline: normalisation [R, limma v3.50.0] -> differential/statistical testing [R, limma v3.50.0] -> stage not stated [Bioconductor, DESeq2 v1.26.0, GSEA]

### Myo-differentiation reporter screen reveals NF-Y as an activator of PAX3-FOXO1 in rhabdomyosarcoma. (PNAS 2023)

- DOI: 10.1073/pnas.2303859120 | PMCID: PMC10483665 | PMID: 37639593
- Evidence: ( E ) GSEA plot demonstrating strong correlation between genes up-regulated following PAX3–FOXO1 knockout and the hallmark myogenesis gene set.
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA]

### CD45 alleviates airway inflammation and lung fibrosis by limiting expansion and activation of ILC2s. (PNAS 2023)

- DOI: 10.1073/pnas.2215941120 | PMCID: PMC10483638 | PMID: 37639581
- Evidence: Gene set enrichment analysis (GSEA) (Broad Institute) and enrichment analysis using Metascape ( 67 ) were performed.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Metascape]

### The spread of interferon-γ in melanomas is highly spatially confined, driving nongenetic variability in tumor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2304190120 | PMCID: PMC10468618 | PMID: 37603742
- Evidence: Moran’s I autocorrelation was also used to rank all genes, and gene set enrichment analysis (GSEA) was performed on the top 2,500 most spatially autocorrelated genes using the gseapy package functions prerank and enrichment_map for the top 10 most enriched gene sets.
- Full pipeline: stage not stated [GSEA, Python]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Evidence: Gene set enrichment analysis (GSEA) identified several cell cycle-associated gene sets including mitotic cell cycle processes, cell division, DNA replication, and regulation of cell cycle as top-scoring GO Biological Processes (BP) (hypergeometric test, q < 0.05; Dataset S7D ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### Triple-negative breast tumors are dependent on mutant p53 for growth and survival. (PNAS 2023)

- DOI: 10.1073/pnas.2308807120 | PMCID: PMC10450424 | PMID: 37579145
- Evidence: Differential gene expression was further analyzed with several pathway enrichment tools, such as GSEA ( 34 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA]

### XCR1 expression distinguishes human conventional dendritic cell type 1 with full effector functions from their immediate precursors. (PNAS 2023)

- DOI: 10.1073/pnas.2300343120 | PMCID: PMC10438835 | PMID: 37566635
- Evidence: ( C ) Gene expression values in ( B ) were analyzed by Gene Set Enrichment Analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [GSEA, MACS2, Seurat]

### CD47 promotes peripheral T cell survival by preventing dendritic cell-mediated T cell necroptosis. (PNAS 2023)

- DOI: 10.1073/pnas.2304943120 | PMCID: PMC10440595 | PMID: 37549290
- Evidence: ( D ) GSEA of pairwise comparisons of T cells between Cd47 ΔT and Cd47 f/f mice.
- Full pipeline: stage not stated [GSEA]

### SETD7 functions as a transcription repressor in prostate cancer via methylating FOXA1. (PNAS 2023)

- DOI: 10.1073/pnas.2220472120 | PMCID: PMC10438836 | PMID: 37549269
- Evidence: Gene Set Enrichment Analysis (GSEA) was conducted for hallmark gene sets and PCa-specific signatures, including FOXA1 targets and AR targets ( 11 , 41 ).
- Full pipeline: alignment/mapping [MACS2 v2.1.4, R] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [R]

### SEC61G assists <i>EGFR</i>-amplified glioblastoma to evade immune elimination. (PNAS 2023)

- DOI: 10.1073/pnas.2303400120 | PMCID: PMC10410745 | PMID: 37523556
- Evidence: ( I ) GSEA shows the correlation between SEC61G expression and the levels of total T cells or activated CD8 + T cells in GBM.
- Full pipeline: quantification [ImageJ] -> stage not stated [GSEA]

### Noncanonical HPV carcinogenesis drives radiosensitization of head and neck tumors. (PNAS 2023)

- DOI: 10.1073/pnas.2216532120 | PMCID: PMC10410762 | PMID: 37523561
- Evidence: ( H ) Barplot displaying GSEA-based adjusted P value representing the enrichment of each WGCNA module for probe–gene correlation.
- Full pipeline: variant calling [VarScan] -> differential/statistical testing [GSEA, WGCNA] -> stage not stated [CNVkit, R]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: GSEA ( 45 , 46 ) was performed using GSEA_4.1.0.
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### Functional interrogation of lymphocyte subsets in alopecia areata using single-cell RNA sequencing. (PNAS 2023)

- DOI: 10.1073/pnas.2305764120 | PMCID: PMC10629527 | PMID: 37428932
- Evidence: Gene set enrichment analysis (GSEA) of statistically significant differentially expressed genes also showed enrichment of gene ontology (GO) terms involving T cell immunity and cytotoxicity ( Fig.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA]

### Aberrant LYZ expression in tumor cells serves as the potential biomarker and target for HCC and promotes tumor progression via csGRP78. (PNAS 2023)

- DOI: 10.1073/pnas.2215744120 | PMCID: PMC10629575 | PMID: 37428911
- Evidence: Further, gene set enrichment analysis (GSEA) revealed that proliferation and metastasis-associated pathways were markedly enriched in LYZ-high HCCs ( Fig.
- Full pipeline: stage not stated [GSEA]

### NOS inhibition reverses TLR2-induced chondrocyte dysfunction and attenuates age-related osteoarthritis. (PNAS 2023)

- DOI: 10.1073/pnas.2207993120 | PMCID: PMC10629581 | PMID: 37428931
- Evidence: Functional enrichment analysis (GSEA) of the 26 mitochondroid genes that were downregulated by P3C4 and then restored by L-NAME addition revealed that these genes were involved in hypoxia response, the generation of precursor metabolites and energy, and ADP metabolic processes ( Fig.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [featureCounts] -> stage not stated [GSEA, MACS2]

### Pharmacological YAP activation promotes regenerative repair of cutaneous wounds. (PNAS 2023)

- DOI: 10.1073/pnas.2305085120 | PMCID: PMC10334740 | PMID: 37399395
- Evidence: RNA-sequencing experiments with PY-60 (10 µM, 24 h) additionally indicated that compound treatment induced a robust and selective YAP-driven transcriptional program in HEKa cells, as gene set enrichment analysis (GSEA) of core YAP target genes and YAP occupied loci indicated a robust enrichment in PY-60-treated samples ( Fig.
- Full pipeline: stage not stated [GSEA]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: The Wald statistic was used to rank all genes, and this ordered list was used as input for gene set enrichment analysis (GSEA) ( 66 ).
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Trophoblast PR-SET7 dysfunction induces viral mimicry response and necroptosis associated with recurrent miscarriage. (PNAS 2023)

- DOI: 10.1073/pnas.2216206120 | PMCID: PMC10288560 | PMID: 37307441
- Evidence: Gene Set Enrichment Analysis (GSEA) revealed significant enrichment of genes involved in apoptosis and the p53 pathway ( Fig.
- Full pipeline: stage not stated [GSEA]

### Tumor cell-derived spermidine is an oncometabolite that suppresses TCR clustering for intratumoral CD8<sup>+</sup> T cell activation. (PNAS 2023)

- DOI: 10.1073/pnas.2305245120 | PMCID: PMC10268234 | PMID: 37276392
- Evidence: Gene set enrichment analysis (GSEA) showed that spermidine treatment resulted in suppression of the genes involved in DNA replication and cell cycle ( Fig.
- Full pipeline: stage not stated [GSEA]

### Steroid receptor coactivator 3 is a key modulator of regulatory T cell-mediated tumor evasion. (PNAS 2023)

- DOI: 10.1073/pnas.2221707120 | PMCID: PMC10266015 | PMID: 37253006
- Evidence: The cellular pathways associated with SRC-3 KO Treg cells were analyzed with DAVID and GSEA programs.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, MACS2]

### Ablation of ZC3H11A causes early embryonic lethality and dysregulation of metabolic processes. (PNAS 2023)

- DOI: 10.1073/pnas.2216799120 | PMCID: PMC10266022 | PMID: 37252988
- Evidence: Hallmark gene set enrichment analysis (GSEA) using all DE genes in KO embryos revealed a significant depletion (FDR < 0.05) of genes involved in glycolysis, fatty acid metabolism pathways, and epithelial–mesenchymal transition (EMT) processes ( Fig.
- Full pipeline: differential/statistical testing [GSEA]

### The KEAP1-NRF2 pathway regulates TFEB/TFE3-dependent lysosomal biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2217425120 | PMCID: PMC10235939 | PMID: 37216554
- Evidence: GSEA confirmed enrichment of signatures associated with NRF2 activation ( Fig.
- Full pipeline: stage not stated [GSEA, HOMER]

### EGR4 is critical for cell-fate determination and phenotypic maintenance of geniculate ganglion neurons underlying sweet and umami taste. (PNAS 2023)

- DOI: 10.1073/pnas.2217595120 | PMCID: PMC10235952 | PMID: 37216536
- Evidence: A ranked gene list was generated based on the differential gene expression analysis, and the list was used for gene set enrichment analysis with GSEA ( https://www.gsea-msigdb.org/gsea/index.jsp ).
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.5] -> differential/statistical testing [GSEA, edgeR v3.12.1] -> stage not stated [ImageJ]

### Aneuploidy effects on human gene expression across three cell types. (PNAS 2023)

- DOI: 10.1073/pnas.2218478120 | PMCID: PMC10214149 | PMID: 37192167
- Evidence: We verified the enrichment of neuronal marker gene sets in each iN sample using gene set enrichment analysis (GSEA) provided by Clusterprofiler ( 44 ) ( SI Appendix , Text S2.3 and Fig.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [DESeq2, FastQC, Trimmomatic] -> quantification [FastQC, Trimmomatic] -> dimensionality reduction/clustering [GSEA] -> stage not stated [R v4.1.0]

### Harnessing endogenous transcription factors directly by small molecules for chemically induced pluripotency inception. (PNAS 2023)

- DOI: 10.1073/pnas.2215155120 | PMCID: PMC10214147 | PMID: 37192170
- Evidence: Gene set enrichment analysis (GSEA) results further suggested the upregulation of ribosome, spliceosome, DNA repair, pyrimidine metabolism, and downregulation of lysosome, cytokine–cytokine receptor interaction, and Hedgehog signaling pathway ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### S-lactoyl modification of KEAP1 by a reactive glycolytic metabolite activates NRF2 signaling. (PNAS 2023)

- DOI: 10.1073/pnas.2300763120 | PMCID: PMC10193962 | PMID: 37155889
- Evidence: Additionally, when IMR32 cells were evaluated for transcriptome-wide changes by RNA sequencing, sAKZ692 treatment (20 µM) was found to induce a selective and robust NRF2 transcriptional profile as assessed by gene set enrichment analysis (GSEA) using commonly used NRF2 gene sets ( Fig.
- Full pipeline: stage not stated [GSEA]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: Perform GSEA of NFIA’s target genes.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### TRAF4-mediated nonproteolytic ubiquitination of androgen receptor promotes castration-resistant prostate cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2218229120 | PMCID: PMC10193960 | PMID: 37155905
- Evidence: ( A ) Gene set enrichment analysis (GSEA) of the genes associated with TRAF4 overexpression in LNCaP cells under androgen-deprived culture condition.
- Full pipeline: normalisation [HOMER] -> stage not stated [BEDTools, GSEA, MACS2 v2.1.0]

### The PRAK-NRF2 axis promotes the differentiation of Th17 cells by mediating the redox homeostasis and glycolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2212613120 | PMCID: PMC10175746 | PMID: 37126714
- Evidence: Gene ontology (GO) analysis and Gene set enrichment analysis (GSEA) both revealed that glycolysis, which is highly elevated during Th17-polarizaiton, was dramatically downregulated in the Prak KO Th17 cells ( Fig.
- Full pipeline: stage not stated [GSEA]

### Targeting SWI/SNF ATPases in H3.3K27M diffuse intrinsic pontine gliomas. (PNAS 2023)

- DOI: 10.1073/pnas.2221175120 | PMCID: PMC10161095 | PMID: 37094128
- Evidence: Sorting of differentially expressed genes was performed by using the empirical Bayes hierarchical models (EBSeq), and significantly up-regulated and down-regulated pathways were determined by the Molecular Signatures Database (MSigDB) in GSEA software ( https://www.gsea-msigdb.org/gsea/msigdb/ ).
- Full pipeline: alignment/mapping [RSEM] -> normalisation [MACS2 v3.0.0] -> differential/statistical testing [GSEA]

### Consequences of poly(ethylene oxide) and poloxamer P188 on transcription in healthy and stressed myoblasts. (PNAS 2023)

- DOI: 10.1073/pnas.2219885120 | PMCID: PMC10161009 | PMID: 37094151
- Evidence: Network and Gene Set Enrichment Analysis.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [GSEA, STRING db]

### High fried food consumption impacts anxiety and depression due to lipid metabolism disturbance and neuroinflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2221097120 | PMCID: PMC10160962 | PMID: 37094155
- Evidence: Moreover, we performed pathway enrichment analysis by employing gene set enrichment analysis (GSEA) algorithm to identify biological pathways affected by chronic exposure to acrylamide.
- Full pipeline: stage not stated [GSEA]

### Reprogramming by drug-like molecules leads to regeneration of cochlear hair cell-like cells in adult mice. (PNAS 2023)

- DOI: 10.1073/pnas.2215253120 | PMCID: PMC10151514 | PMID: 37068229
- Evidence: By Gene Set Enrichment Analysis ( 33 , 34 ), we identified genes prominently enriched under Myc/Notch1 co-activation in the pathways including MYC targets and NOTCH signaling, E2F targets, G2M checkpoint, oxidative phosphorylation, and mTORC1 ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat v3.2, UMAP] -> simulation/modelling [Monocle] -> stage not stated [GSEA]

### Molecular profiling of the stroke-induced alterations in the cerebral microvasculature reveals promising therapeutic candidates. (PNAS 2023)

- DOI: 10.1073/pnas.2205786120 | PMCID: PMC10120001 | PMID: 37058487
- Evidence: In another examination to further investigate which biological pathways were differentially enriched in sham or tMCAO microvessels, we performed gene set enrichment analyses (GSEA) of the gene counts per million from each sample of sham and tMCAO microvessels using the Molecular Signature Data Base (MsigDB) platform ( 33 ) and the built-in pathway-specific data bases: Pathway Interaction Database ...
- Full pipeline: quantification [QuPath] -> differential/statistical testing [GSEA]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: ( E ) Normalized enrichment score (NES) computed via GSEA for ISGs (genes significantly enriched in nontargeting control cells with transfected hairpin RNA relative to unstimulated nontargeting control cells).
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### Pleiotropic role of TRAF7 in skull-base meningiomas and congenital heart disease. (PNAS 2023)

- DOI: 10.1073/pnas.2214997120 | PMCID: PMC10120005 | PMID: 37043537
- Evidence: Gene set enrichment analysis (GSEA) indicating the enrichment of cilia-related genes (obtained from CiliaCarta Database) within the genes that show positive ( Left ) or negative ( Right ) association with Traf7 expression in knn-DREMI analysis.
- Full pipeline: stage not stated [GSEA]

### Identification of hidden associations among eukaryotic genes through statistical analysis of coevolutionary transitions. (PNAS 2023)

- DOI: 10.1073/pnas.2218329120 | PMCID: PMC10120013 | PMID: 37043529
- Evidence: The enrichment analysis was performed with the GSEA function of the clusterProfiler R library ( 65 ).
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Python, RAxML v8.2.12]

### Tumor progression is independent of tumor-associated macrophages in cell lineage-based mouse models of glioblastoma. (PNAS 2023)

- DOI: 10.1073/pnas.2222084120 | PMCID: PMC10120014 | PMID: 37040416
- Evidence: GSEA analysis.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, fgsea]

### Phosphatidylserine-positive extracellular vesicles boost effector CD8<sup>+</sup> T cell responses during viral infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210047120 | PMCID: PMC10120060 | PMID: 37040405
- Evidence: GSEA were conducted with “clusterProfiler” (version 3.18.1) on the statistic reported by DEseq2.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler]

### Interrogating bromodomain inhibitor resistance in KMT2A-rearranged leukemia through combinatorial CRISPR screens. (PNAS 2023)

- DOI: 10.1073/pnas.2220134120 | PMCID: PMC10120025 | PMID: 37036970
- Evidence: The log 2 (fold change) values of all genes from the whole-transcriptome comparison were uploaded for GSEA.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [RSEM] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GATK v4.1.2.0, GSEA]

### GINS4 suppresses ferroptosis by antagonizing p53 acetylation with Snail. (PNAS 2023)

- DOI: 10.1073/pnas.2219585120 | PMCID: PMC10104543 | PMID: 37018198
- Evidence: GSEA results showed that DNA replication and cell cycle pathways were significantly enriched in both datasets.
- Full pipeline: stage not stated [GSEA]

### The expansion of agriculture has shaped the recent evolutionary history of a specialized squash pollinator. (PNAS 2023)

- DOI: 10.1073/pnas.2208116120 | PMCID: PMC10104555 | PMID: 37011184
- Evidence: Gene Set Enrichment Analysis and Nonsynonymous Substitutions.
- Full pipeline: alignment/mapping [AUGUSTUS] -> variant calling [GATK] -> stage not stated [BUSCO v4.0.6, GSEA, R]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Evidence: Hallmark pathway analysis, obtained by Gene Set Enrichment Analysis, revealed that TS-CAR Tregs upregulated pathways linked to metabolism, including MYC and MTORC1 signaling, glycolysis, oxidative phosphorylation, cholesterol homeostasis, fatty acid metabolism, and adipogenesis ( Fig.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### circNEIL3 inhibits tumor metastasis through recruiting the E3 ubiquitin ligase Nedd4L to degrade YBX1. (PNAS 2023)

- DOI: 10.1073/pnas.2215132120 | PMCID: PMC10068820 | PMID: 36961927
- Evidence: ( G ) Gene Set Enrichment Analysis showing the correlation of YBX1 protein abundance with cellular adhesion and metastatic pathways in breast cancer and lung adenocarcinoma samples.
- Full pipeline: quantification [GSEA]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Evidence: Gene set enrichment analysis (GSEA) of the top 500 genes linked to cobound, H3K4me1 + E/SEs ( Methods ) revealed a significant overrepresentation of programs related to BCR signaling, cytokines and chemokines stimulation, G-protein signaling, and transcription factors of relevance to the GC reaction (e.g.
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### Neuron-specific transcriptomic signatures indicate neuroinflammation and altered neuronal activity in ASD temporal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2206758120 | PMCID: PMC10013873 | PMID: 36862688
- Evidence: Gene set enrichment analysis (GSEA) indicated that genes with significant diagnosis-by-age interaction were enriched in immune/inflammation pathways and synaptic-related pathways.
- Full pipeline: quantification [featureCounts v1.6.4] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [DESeq2 v1.22.2, GSEA, WGCNA]

### Mouse models of human multiple myeloma subgroups. (PNAS 2023)

- DOI: 10.1073/pnas.2219439120 | PMCID: PMC10013859 | PMID: 36853944
- Evidence: We then employed gene set enrichment analysis (GSEA) using the tmod algorithm ( 39 ) to determine whether human MM signature genes are enriched in double-mutant mouse plasma cells.
- Full pipeline: stage not stated [GSEA]

### Defining and targeting tumor-associated macrophages in malignant mesothelioma. (PNAS 2023)

- DOI: 10.1073/pnas.2210836120 | PMCID: PMC9992826 | PMID: 36821580
- Evidence: ( C ) GSEA was performed to show the SPM-specific genes involved in top 10 hallmark gene sets of up- or downregulated genes (>twofold change; P < 0.05).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Liver X receptor controls follicular helper T cell differentiation via repression of TCF-1. (PNAS 2023)

- DOI: 10.1073/pnas.2213793120 | PMCID: PMC9992818 | PMID: 36802434
- Evidence: In addition, gene set enrichment analysis (GSEA) revealed that Nr1h2 −/− Tfh cells were enriched for genes involved in the BCL6-high Tfh program, indicating that GC Tfh transcriptome is up-regulated in the absence of LXRβ ( SI Appendix, Fig.
- Full pipeline: stage not stated [GSEA]

### Type III interferon drives thymic B cell activation and regulatory T cell generation. (PNAS 2023)

- DOI: 10.1073/pnas.2220120120 | PMCID: PMC9992806 | PMID: 36802427
- Evidence: GSEA was performed using Limma to generate a preranked list based on t-value and then analyzed using the GSEA-Broad Institute website application ( https://www.gsea-msigdb.org/gsea/index.jsp ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R v4.0.0, Seurat, edgeR v3.24.3, ggplot2, pheatmap]

### ALK fusion NSCLC oncogenes promote survival and inhibit NK cell responses via <i>SERPINB4</i> expression. (PNAS 2023)

- DOI: 10.1073/pnas.2216479120 | PMCID: PMC9974509 | PMID: 36791109
- Evidence: These genes were strongly enriched for Tumor Necrosis Factor-Alpha (TNF-α) signaling via NF-κB ( P adj = 4.5e−14) and Interleukin-2 (IL2)-Signal transducer and activator of transcription 5 (STAT5) signaling ( P adj = 2.0e−07) as observed from a Hallmark gene set enrichment analysis (GSEA) ( Fig.
- Full pipeline: stage not stated [GSEA]

### Reduction of embryonic <i>E93</i> expression as a hypothetical driver of the evolution of insect metamorphosis. (PNAS 2023)

- DOI: 10.1073/pnas.2216640120 | PMCID: PMC9963766 | PMID: 36745781
- Evidence: ( C ) GSEA showing the top significantly enriched Gene Ontology (GO) terms of biological processes down-regulated after depleting E93 in early embryos.
- Full pipeline: stage not stated [GSEA]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: Gene ontology over-representation and gene set enrichment analysis (GSEA) were conducted using the clusterProfiler package ( 29 ) with a GO level of 3 and fgsea package ( 30 ) with the Reactome database, respectively.
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Distinct and opposite effects of leukemogenic <i>Idh</i> and <i>Tet2</i> mutations in hematopoietic stem and progenitor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2208176120 | PMCID: PMC9942850 | PMID: 36652477
- Evidence: In agreement with our flow cytometry analyses, Gene Set Enrichment Analysis (GSEA) indicated that Idh2 R172K and Tet2 −/− cells downregulated markers of hematopoietic progenitor differentiation and proliferation but showed opposite alterations of genes associated with HSCs and early progenitors ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [SCENIC, Seurat, Slingshot] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, MACS2]

### HER2-driven breast cancer suppression by the JNK signaling pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2218373120 | PMCID: PMC9942916 | PMID: 36656864
- Evidence: Gene set enrichment analysis (GSEA) of DE genes caused by JNK deficiency under control conditions reported hallmarks of apical junctions, KRAS signaling, and breast cancer pathways ( Fig.
- Full pipeline: stage not stated [GSEA]

### ATOH8 binds SMAD3 to induce cellular senescence and prevent Ras-driven malignant transformation. (PNAS 2023)

- DOI: 10.1073/pnas.2208927120 | PMCID: PMC9934021 | PMID: 36626550
- Evidence: ( E and F ) Gene Set Enrichment Analysis (GSEA) of the correlation between ATOH8 and 122 down-regulated target genes and 23 cell cycle–promoting genes using the TCGA lung cancer database.
- Full pipeline: stage not stated [GSEA]

### OGT controls mammalian cell viability by regulating the proteasome/mTOR/ mitochondrial axis. (PNAS 2023)

- DOI: 10.1073/pnas.2218332120 | PMCID: PMC9934350 | PMID: 36626549
- Evidence: ( F ) Leading edge analysis for proteome level-GSEA of proteins involved in the PI3K–AKT–MTOR pathway.
- Full pipeline: visualisation [Metascape] -> stage not stated [GSEA]

### Sec22b is a critical and nonredundant regulator of plasma cell maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2213056120 | PMCID: PMC9926242 | PMID: 36595686
- Evidence: GSEA was performed by the clusterProfiler::GSEA function using the fgsea algorithm.
- Full pipeline: read trimming [Bioconductor, edgeR] -> alignment/mapping [Bioconductor, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [GSEA, clusterProfiler, fgsea] -> differential/statistical testing [Bioconductor, R, edgeR, limma]

### Atf7ip and Setdb1 interaction orchestrates the hematopoietic stem and progenitor cell state with diverse lineage differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2209062120 | PMCID: PMC9910619 | PMID: 36577070
- Evidence: Gene set enrichment analysis (GSEA) revealed that categories in "mitotic cell cycle", "DNA replication", were identified in the down-regulated setdb1b −/− dataset, whereas biological processes in "immune system process", "inflammatory response", were found in the up-regulated setdb1b −/− transcriptome ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Bioprosthetic heart valve structural degeneration associated with metabolic syndrome: Mitigation with polyoxazoline modification. (PNAS 2023)

- DOI: 10.1073/pnas.2219054120 | PMCID: PMC9910464 | PMID: 36574676
- Evidence: Gene Set Enrichment Analysis (GSEA) in Clinical BHV Explants from Patients with and without MetS.
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [Cytoscape v3.9.1] -> visualisation [Bioconductor, Cytoscape v3.9.1] -> stage not stated [GSEA]

### Structure-based discovery of potent WD repeat domain 5 inhibitors that demonstrate efficacy and safety in preclinical animal models. (PNAS 2023)

- DOI: 10.1073/pnas.2211297120 | PMCID: PMC9910433 | PMID: 36574664
- Evidence: These categories and the similarities between C16 and 10 are further reinforced by Gene Set Enrichment Analysis ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Inhibiting androgen receptor splice variants with cysteine-selective irreversible covalent inhibitors to treat prostate cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2211832120 | PMCID: PMC9910435 | PMID: 36577061
- Evidence: Heatmap ( C ) and GSEA plot and the corresponding heatmap for the hallmark apoptosis pathway ( D ) are shown.
- Full pipeline: stage not stated [GSEA]

### Enhanced pathogenicity of Th17 cells due to natalizumab treatment: Implications for MS disease rebound. (PNAS 2023)

- DOI: 10.1073/pnas.2209944120 | PMCID: PMC9910615 | PMID: 36574650
- Evidence: The GSEA was done using the R-package fgsea ( 52 ).
- Full pipeline: stage not stated [GSEA, fgsea, tidyverse]

### Breast cancer patient-derived whole-tumor cell culture model for efficient drug profiling and treatment response prediction. (PNAS 2023)

- DOI: 10.1073/pnas.2209856120 | PMCID: PMC9910599 | PMID: 36574653
- Evidence: Furthermore, the gene-set enrichment analysis (GSEA) identified a high degree of agreement among the signaling pathways between the two treatment groups (using either the Hallmarks or the Canonical pathways gene-set collection), indicating that there is no significant difference in the molecular pathways induced by 4OHT and EDF treatment ( Fig.
- Full pipeline: alignment/mapping [GATK] -> stage not stated [GSEA, SnpEff]

### Interplay between Netrin-1 and Norrin controls arteriovenous zonation of blood-retina barrier integrity. (PNAS 2024)

- DOI: 10.1073/pnas.2408674121 | PMCID: PMC11670198 | PMID: 39693351
- Evidence: Gene set enrichment analysis (GSEA) revealed downregulation of both BBB and BRB enriched genes and downregulation of WNT/β-catenin signaling target genes in Ntn1iKO and Unc5biECKO ECs ( 44 ) ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: Gene Set Enrichment Analysis From Mouse Retina RNA-Seq.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Engineering bacteria for cancer immunotherapy by inhibiting IDO activity and reprogramming CD8+ T cell response. (PNAS 2024)

- DOI: 10.1073/pnas.2412070121 | PMCID: PMC11670085 | PMID: 39693352
- Evidence: ( L and M ) GSEA plot comparing Untreated with L-Trp CB-conditioned CD8 + T cells for immune effector processes, natural killer cell–mediated immunity and mTORC1 signaling.
- Full pipeline: stage not stated [GSEA]

### Complement C3d enables cell-mediated immunity capable of distinguishing spontaneously transformed from nontransformed cells. (PNAS 2024)

- DOI: 10.1073/pnas.2405824121 | PMCID: PMC11670236 | PMID: 39693340
- Evidence: ( D ) GSEA pathway analysis of differentially expressed genes in various bone marrow cell populations.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [Seurat, pheatmap]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: GSEA was performed with GSEA software ( 62 ).
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Cold-blooded vertebrate utilizes behavioral fever to alleviate T cell apoptosis and optimize antimicrobial immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2408969121 | PMCID: PMC11670090 | PMID: 39680767
- Evidence: This was further confirmed by the RNAseq and gene set enrichment analysis (GSEA) results, which revealed that infected tilapia that did and did not develop behavioral fever showed no significant differences in T cell activation, regulation of T cell activation and T cell receptor signaling pathway ( SI Appendix , Fig.
- Full pipeline: stage not stated [Cytoscape, GSEA]

### Increased perfluorooctanoic acid accumulation facilitates the migration and invasion of lung cancer cells via remodeling cell mechanics. (PNAS 2024)

- DOI: 10.1073/pnas.2408575121 | PMCID: PMC11665856 | PMID: 39665760
- Evidence: Gene set enrichment analysis (GSEA) revealed that PFOA significantly elevated gene expression in pathways related to focal adhesion, regulation of the actin cytoskeleton, ECM–receptor interaction, and the phosphatidylinositol 3-kinase (PI3K)-Akt signaling pathway ( Fig.
- Full pipeline: differential/statistical testing [R] -> visualisation [ggplot2] -> stage not stated [GSEA]

### Targeting DTX2/UFD1-mediated FTO degradation to regulate antitumor immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2407910121 | PMCID: PMC11665913 | PMID: 39661064
- Evidence: GSEA and heatmaps of significant genes were generated using WebGestalt.
- Full pipeline: stage not stated [GSEA, Metascape]

### Transcriptional reprogramming primes CD8+ T cells toward exhaustion in Myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2024)

- DOI: 10.1073/pnas.2415119121 | PMCID: PMC11648872 | PMID: 39621903
- Evidence: ( D ) GSEA dot plot of γδT cells against hallmark pathways from Molecular Signature Database.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, GSEA]

### Lethal COVID-19 associates with RAAS-induced inflammation for multiple organ damage including mediastinal lymph nodes. (PNAS 2024)

- DOI: 10.1073/pnas.2401968121 | PMCID: PMC11626201 | PMID: 39602262
- Evidence: 1 D ) and with induction of the IFNα gene set enrichment analysis (GSEA) pathway ( Fig.
- Full pipeline: stage not stated [GSEA, ImageJ]

### PGC-1α drives small cell neuroendocrine cancer progression toward an ASCL1-expressing subtype with increased mitochondrial capacity. (PNAS 2024)

- DOI: 10.1073/pnas.2416882121 | PMCID: PMC11626175 | PMID: 39589879
- Evidence: ( Right ) Gene set enrichment analysis (GSEA) of differentially expressed genes in pre- versus post ADT-treated tumors.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [HOMER]

### In situ licensing of mesenchymal stem cell immunomodulatory function via BMP-2 induced developmental process. (PNAS 2024)

- DOI: 10.1073/pnas.2410579121 | PMCID: PMC11621467 | PMID: 39565311
- Evidence: Furthermore, Gene-set enrichment analysis (GSEA) indicated downregulation of immune and inflammatory response signature genes in HMSCs, whereas these genes were upregulated in IBMSCs ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA, R]

### CD2 expressing innate lymphoid and T cells are critical effectors of immunopathogenesis in hidradenitis suppurativa. (PNAS 2024)

- DOI: 10.1073/pnas.2409274121 | PMCID: PMC11621750 | PMID: 39560648
- Evidence: Next, we performed Gene Set Enrichment Analysis to identify the enrichment of hallmarks and canonical pathways in all scRNAseq clusters.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.0, UMAP]

### Small-molecule disruption of androgen receptor-dependent chromatin clusters. (PNAS 2024)

- DOI: 10.1073/pnas.2406239121 | PMCID: PMC11621760 | PMID: 39560645
- Evidence: ( D ) RNA-sequencing data for a panel of PCa models treated with BG-15n represented as GSEA normalized enrichment scores (NES) for the Hallmark Androgen Response pathway.
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [GSEA]

### Loss of XIST lncRNA unlocks stemness and cellular plasticity in ovarian cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2418096121 | PMCID: PMC11588085 | PMID: 39546568
- Evidence: ( C ) Bubble map of pathways enriched in OVCAR3-KRAB in XIST KD after GSEA.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Augmenting antitumor efficacy of Th17-derived Th1 cells through IFN-γ-induced type I interferon response network via IRF7. (PNAS 2024)

- DOI: 10.1073/pnas.2412120121 | PMCID: PMC11588128 | PMID: 39541355
- Evidence: Genes regulating positive leukocyte apoptotic processes were intermediately enriched by gene set enrichment analysis (GSEA) of in vitro-cultured Th 17 1 cells compared to Th1 and Th17 cells ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA, GSVA]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: Pathway analysis/GSEA was performed using clusterProfiler (60) or fgsea.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Mediator kinase inhibitors suppress triple-negative breast cancer growth and extend tumor suppression by mTOR and AKT inhibitors. (PNAS 2024)

- DOI: 10.1073/pnas.2414501121 | PMCID: PMC11588072 | PMID: 39541354
- Evidence: Gene Set Enrichment Analysis (GSEA) of 50 hallmark pathways in tumor cells revealed the pathways that were differentially affected in different treatment arms ( Fig.
- Full pipeline: differential/statistical testing [GSEA]

### Implantable 3D printed hydrogels with intrinsic channels for liver tissue engineering. (PNAS 2024)

- DOI: 10.1073/pnas.2403322121 | PMCID: PMC11588097 | PMID: 39531491
- Evidence: Relative gene expression analysis and GSEA were determined using the DEseq2 and GSEA module of GenePattern ( 37 ).
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> stage not stated [GSEA]

### DeSide: A unified deep learning approach for cellular deconvolution of tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2407096121 | PMCID: PMC11573681 | PMID: 39514318
- Evidence: The gene sets used in this work were downloaded from GSEA ( https://www.gsea-msigdb.org/gsea/msigdb/human/collections.jsp#C2 ) ( 57 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, Python, TensorFlow]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: Gene-wise correlation coefficients were exported for GSEA.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### Deficiency of &lt;i&gt;DDX3X&lt;/i&gt; results in neurogenesis defects and abnormal behaviors via dysfunction of the Notch signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2404173121 | PMCID: PMC11551356 | PMID: 39471229
- Evidence: To assess the functional changes of these neuronal clusters, we performed gene set enrichment analyses (GSEA) based on the gene rank of the expressional fold change.
- Full pipeline: dimensionality reduction/clustering [GSEA] -> stage not stated [Seurat]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: Gene set enrichment analysis (GSEA) ( 55 ), focused on Gene Ontology ( 56 ), was conducted using the R 4.3.1 Bioconductor package clusterProfiler ( 57 ) to elucidate whole transcriptomic patterns between groups.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### WDR20 prevents hepatocellular carcinoma senescence by orchestrating the simultaneous USP12/46-mediated deubiquitination of c-Myc. (PNAS 2024)

- DOI: 10.1073/pnas.2407904121 | PMCID: PMC11536108 | PMID: 39432777
- Evidence: The GSEA pathway analysis also revealed the cellular senescence pathway activation following WDR20 silencing ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Evidence: Gene set enrichment analysis (GSEA) was performed using the prerank tool in GSEApy.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Maternal NO&lt;sub&gt;2&lt;/sub&gt; exposure and fetal growth restriction: Hypoxia transmission and lncRNAs-proinflammation-mediated abnormal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2409597121 | PMCID: PMC11536148 | PMID: 39432779
- Evidence: The gene set enrichment analysis (GSEA) (|NES| > 1.5, q < 0.05, Fig.
- Full pipeline: stage not stated [GSEA]

### Nuclear p62 condensates stabilize the promyelocytic leukemia nuclear bodies by sequestering their ubiquitin ligase RNF4. (PNAS 2024)

- DOI: 10.1073/pnas.2414377121 | PMCID: PMC11513912 | PMID: 39418304
- Evidence: Gene set enrichment analysis (GSEA) which was performed to obtain common pathways using protein logFC/se values, revealed 27 positively and 4 negatively correlated biological processes ( SI Appendix , Table S1 ).
- Full pipeline: stage not stated [GSEA]

### Abortive infection of bat fibroblasts with SARS-CoV-2. (PNAS 2024)

- DOI: 10.1073/pnas.2406773121 | PMCID: PMC11513954 | PMID: 39401365
- Evidence: Differential expression analysis was performed using DESeq2 ( 40 ), and we found gene sets enriched in genes changing upon infection using the GSEA tool ( 41 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, GSEA]

### TRIM21 induces selective autophagic degradation of c-Myc and sensitizes regorafenib therapy in colorectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406936121 | PMCID: PMC11494295 | PMID: 39388269
- Evidence: Consistently, gene set enrichment analysis (GSEA) of the The Cancer Genome Atlas-Colon Adenocarcinoma dataset revealed significant enrichment of genes down-regulated by MYC in patients with high TRIM21 expression ( SI Appendix , Fig.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [GSEA]

### Transcriptional repression by HDAC3 mediates T cell exclusion from &lt;i&gt;Kras&lt;/i&gt; mutant lung tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2317694121 | PMCID: PMC11494357 | PMID: 39388266
- Evidence: Gene set enrichment analysis (GSEA) confirmed that the expression of “SASP Fridman Senescence” and “TNFα Signaling via NF-κB” gene sets were enriched upon HDAC3 inactivation ( Fig.
- Full pipeline: alignment/mapping [HOMER, STAR] -> stage not stated [Enrichr, GSEA, QuPath]

### Targeting the MAtrix REgulating MOtif abolishes several hallmarks of cancer, triggering antitumor immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2404485121 | PMCID: PMC11494334 | PMID: 39382998
- Evidence: GSEA was performed with the GSEA tool (v4.3.2) ( 51 , 52 ) using either mouse hallmark gene set collection (MH) alone ( 53 ) or all curated mouse gene sets collection (M2) available at MSigDB.
- Full pipeline: quality control [FastQC] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, ImageJ]

### Functional inversion of circadian regulator REV-ERBα leads to tumorigenic gene reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2411321121 | PMCID: PMC11494309 | PMID: 39383000
- Evidence: GSEA analysis also showed that pathways of MAPK and PI3K-Akt signaling, KRAS signaling, and cell cycle were highly enriched ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### An engineered model of metastatic colonization of human bone marrow reveals breast cancer cell remodeling of the hematopoietic niche. (PNAS 2024)

- DOI: 10.1073/pnas.2405257121 | PMCID: PMC11494322 | PMID: 39374382
- Evidence: By performing gene set enrichment analysis (GSEA), we identified a number of significantly upregulated pathways associated with cancer cells cultured in ME tissues as compared to those in the OB group.
- Full pipeline: stage not stated [GSEA]

### Toward a CRISPR-based mouse model of &lt;i&gt;Vhl&lt;/i&gt;-deficient clear cell kidney cancer: Initial experience and lessons learned. (PNAS 2024)

- DOI: 10.1073/pnas.2408549121 | PMCID: PMC11474080 | PMID: 39365820
- Evidence: ( D ) GSEA showing significantly up-or down-regulated pathways in Cre-less AAV model kidney tumor vs normal mouse kidney and TCGA ccRCC vs normal human kidney.
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1] -> visualisation [ImageJ v1.53] -> stage not stated [GSEA]

### Calcineurin-mediated dephosphorylation stabilizes E2F1 protein by suppressing binding of the FBXW7 ubiquitin ligase subunit. (PNAS 2024)

- DOI: 10.1073/pnas.2414618121 | PMCID: PMC11474076 | PMID: 39361641
- Evidence: Gene set enrichment analysis (GSEA) of RNA-seq data previously obtained from calcineurin Aα–depleted and control MCF7 cells (DRA011729) revealed that the expression of E2F target genes was down-regulated by calcineurin depletion ( Fig.
- Full pipeline: stage not stated [GSEA]

### Proteomic and phosphoproteomic landscape of localized prostate cancer unveils distinct molecular subtypes and insights into precision therapeutics. (PNAS 2024)

- DOI: 10.1073/pnas.2402741121 | PMCID: PMC11459144 | PMID: 39320917
- Evidence: ( F ) GSEA to identify cancer hallmark with activity either higher (red bars) or lower (blue bars) in prostate tumor samples.
- Full pipeline: differential/statistical testing [R, limma] -> stage not stated [GSEA]

### A sensitive assay for measuring whole-blood responses to type I IFNs. (PNAS 2024)

- DOI: 10.1073/pnas.2402983121 | PMCID: PMC11459193 | PMID: 39312669
- Evidence: The ensemble ID targeting multiple genes was collapsed (average) and a final gene data matrix was used for a modular repertoire analysis, as previously described ( 103 ) or for geneset enrichment analysis (GSEA: fgsea) with hallmark gene sets ( http://www.gsea-msigdb.org/ ). scRNAseq.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, fgsea]

### A molecular switch from tumor suppressor to oncogene in ER+ve breast cancer: Role of androgen receptor, JAK-STAT, and lineage plasticity. (PNAS 2024)

- DOI: 10.1073/pnas.2406837121 | PMCID: PMC11459127 | PMID: 39312663
- Evidence: Paired t test analysis followed by Gene Set Enrichment Analysis (GSEA) showed that pathways associated with worse prognosis and tumor progression, including HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION, HALLMARK_PI3K_AKT_MTOR_SIGNALING, HALLMARK_MTORC1_SIGNALING, were represented by the genes down-regulated in AR-high cells or genes higher in AR-low cells ( SI Appendix , Figs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Genetic variation drives cancer cell adaptation to ECM stiffness. (PNAS 2024)

- DOI: 10.1073/pnas.2403062121 | PMCID: PMC11441511 | PMID: 39302966
- Version used: **4.1.0**
- Evidence: Oncogenic gene signatures were identified using GSEA v4.1.0 and the C6 MSigDB collection.
- Full pipeline: read trimming [Bismark] -> alignment/mapping [Bismark] -> differential/statistical testing [R v4.1.3, edgeR] -> stage not stated [GSEA v4.1.0, ImageJ, Trim Galore]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Evidence: ( E ) GSEA of Reactome pathways with differentially expressed genes (from D with fold change > 2) in Mga KO 4T1 cells compared with WT control cells with IFN-γ stimulation.
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### Phenoxyacetic acid enhances nodulation symbiosis during the rapid growth stage of soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2322217121 | PMCID: PMC11406252 | PMID: 39240965
- Evidence: To further investigate potential mechanisms underlying POA-mediated nodulation, we used Gene Set Enrichment Analysis (GSEA) to predict pathways downstream of POA and found that POA initiates the negative regulation of the ethylene-active signaling pathway ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Oncofetal IGF2BP3-mediated control of microRNA structural diversity in the malignancy of early-stage lung adenocarcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2407016121 | PMCID: PMC11388381 | PMID: 39196622
- Evidence: Gene set enrichment analysis (GSEA) revealed that cell cycle, epithelial–mesenchymal transition (EMT), and immune response pathways were the most variable gene sets between the D-score high and low samples ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### &lt;i&gt;RAD21&lt;/i&gt; promotes oncogenesis and lethal progression of prostate cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2405543121 | PMCID: PMC11388324 | PMID: 39190349
- Evidence: RNA Isolation, Sequencing, and GSEA.
- Full pipeline: stage not stated [GSEA, ImageJ]

### Type I interferon signaling pathway enhances immune-checkpoint inhibition in KRAS mutant lung tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2402913121 | PMCID: PMC11388366 | PMID: 39186651
- Evidence: Gene set enrichment analysis (GSEA) of the transcriptomic data revealed enrichment of pathways related with the three aspects of transcriptional heterogeneity in lung adenomas ( SI Appendix, Fig.
- Full pipeline: stage not stated [GSEA]

### Lipid-associated macrophages' promotion of fibrosis resolution during MASH regression requires TREM2. (PNAS 2024)

- DOI: 10.1073/pnas.2405746121 | PMCID: PMC11363294 | PMID: 39172787
- Evidence: These correlation values were then used in a gene set enrichment analysis (GSEA) to identify pathways enriched with genes that are positively or negatively correlated with Trem2 expression ( Fig.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Polyomavirus ALTOs, but not MTs, downregulate viral early gene expression by activating the NF-κB pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2403133121 | PMCID: PMC11348336 | PMID: 39141346
- Evidence: RNA Sequencing and Gene Set Enrichment Analysis.
- Full pipeline: alignment/mapping [Clustal Omega, STAR] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [GSEA]

### Zfp697 is an RNA-binding protein that regulates skeletal muscle inflammation and remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2319724121 | PMCID: PMC11348326 | PMID: 39141348
- Evidence: Gene set enrichment analysis (GSEA) of “unloading vs. control” and “reloading vs. unloading”, performed with hallmark gene sets ( 11 ), revealed in common between both groups a repression of oxidative metabolism and myogenesis-related pathways and an induction on unfolded protein response ( Fig.
- Full pipeline: stage not stated [GSEA]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: ( B ) Dotplot showing GSEA results from the four tumor epithelial clusters calculated by ClusterProfiler().
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Phase separation of PML/RARα and BRD4 coassembled microspeckles governs transcriptional dysregulation in acute promyelocytic leukemia. (PNAS 2024)

- DOI: 10.1073/pnas.2406519121 | PMCID: PMC11348160 | PMID: 39136995
- Evidence: ( H ) GSEA showing the enrichment of BP genes among genes most likely targeted by SEs with PML/RARα and BRD4 cobinding.
- Full pipeline: stage not stated [GSEA, ImageJ v2.1.0]

### IL-1 receptor antagonism reveals a yin-yang relationship between NFκB and interferon signaling in chronic lymphocytic leukemia. (PNAS 2024)

- DOI: 10.1073/pnas.2405644121 | PMCID: PMC11331101 | PMID: 39121163
- Evidence: Gene Set Enrichment Analysis (GSEA).
- Full pipeline: stage not stated [GSEA]

### Oxysterol binding protein regulates the resolution of TLR-induced cytokine production in macrophages. (PNAS 2024)

- DOI: 10.1073/pnas.2406492121 | PMCID: PMC11331125 | PMID: 39361877
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: quality control [FastQC v0.11.5] -> quantification [ImageJ, limma] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [R, edgeR v3.26.8, limma] -> stage not stated [GSEA, MACS2 v2.1.0, featureCounts]

### Prostate cancer-induced endothelial-cell-to-osteoblast transition drives immunosuppression in the bone-tumor microenvironment through Wnt pathway-induced M2 macrophage polarization. (PNAS 2024)

- DOI: 10.1073/pnas.2402903121 | PMCID: PMC11331113 | PMID: 39102549
- Evidence: 1 A , gene set enrichment analysis (GSEA) of GSE241343 RNAseq data demonstrated enrichment of an M2-like macrophage signature in MycCaP-BMP4 tumors compared with MycCaP tumors ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [GSEA]

### Reconstruction of single-cell lineage trajectories and identification of diversity in fates during the epithelial-to-mesenchymal transition. (PNAS 2024)

- DOI: 10.1073/pnas.2406842121 | PMCID: PMC11317558 | PMID: 39093947
- Evidence: We performed single-sample Gene Set Enrichment Analysis (ssGSEA) on all gene sets using GSEAPY (v1.0.4), a Python package 8686 ( 74 ).
- Full pipeline: stage not stated [GSEA]

### Unraveling clonal CD8 T cell expansion and identification of essential factors in γ-herpesvirus-induced lymphomagenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2404536121 | PMCID: PMC11317613 | PMID: 39088396
- Evidence: Gene-set enrichment analysis (GSEA) further revealed significant phenotypic changes in CD8 + T cells during MCF ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [Seurat, UMAP] -> stage not stated [GSEA]

### USP11 promotes prostate cancer progression by up-regulating AR and c-Myc activity. (PNAS 2024)

- DOI: 10.1073/pnas.2403331121 | PMCID: PMC11295044 | PMID: 39052835
- Evidence: To confirm these results, we performed GSEA analysis of differentially expressed genes (DEGs) after USP11 KD and observed enrichment of AR or MYC target genes ( Fig.
- Full pipeline: quantification [pheatmap] -> differential/statistical testing [GSEA] -> stage not stated [Enrichr]

### HLA-C expression in extravillous trophoblasts is determined by an ELF3-NLRP2/NLRP7 regulatory axis. (PNAS 2024)

- DOI: 10.1073/pnas.2404229121 | PMCID: PMC11295039 | PMID: 39052836
- Evidence: ( E ) GSEA plot of the most significant pathways enriched by the significantly differentially expressed genes (DEGs) in NLRP7 −/− cells.
- Full pipeline: differential/statistical testing [GSEA]

### A therapy for suppressing canonical and noncanonical SARS-CoV-2 viral entry and an intrinsic intrapulmonary inflammatory response. (PNAS 2024)

- DOI: 10.1073/pnas.2408109121 | PMCID: PMC11287264 | PMID: 39028694
- Evidence: Gene set enrichment analysis (GSEA), using Kyoto Encyclopedia of Genes and Genomes (KEGG), of the mock vs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Metascape]

### Mitochondrial antioxidants abate SARS-COV-2 pathology in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2321972121 | PMCID: PMC11287122 | PMID: 39008677
- Version used: **4.3.2**
- Evidence: Gene Set Enrichment Analysis (GSEA) was performed using GSEA 4.3.2.
- Full pipeline: quantification [DESeq2, R v4.2.2] -> normalisation [DESeq2, R v4.2.2] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ComplexHeatmap, GSEA v4.3.2, ggplot2]

### Intratumoral NKT cell accumulation promotes antitumor immunity in pancreatic cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2403917121 | PMCID: PMC11260137 | PMID: 38980903
- Evidence: GSEA.
- Full pipeline: quality control [FastQC, RSEM] -> stage not stated [GSEA, ImageJ, MACS2]

### Single-cell analysis of treatment-resistant prostate cancer: Implications of cell state changes for cell surface antigen-targeted therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322203121 | PMCID: PMC11252802 | PMID: 38968122
- Evidence: These latter cells were enriched for stem cell programs and the AP–1 pathway based on GSEA ( Dataset S7 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, SCENIC]

### NRF2 is a spatiotemporal metabolic hub essential for the polyfunctionality of Th2 cells. (PNAS 2024)

- DOI: 10.1073/pnas.2319994121 | PMCID: PMC11252815 | PMID: 38959032
- Evidence: Hallmark pathway ( D ) and GSEA ( E ) of cluster 2.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP] -> stage not stated [Scanpy]

### Nonviral CRISPR/Cas9 mutagenesis for streamlined generation of mouse lung cancer models. (PNAS 2024)

- DOI: 10.1073/pnas.2322917121 | PMCID: PMC11252735 | PMID: 38959035
- Evidence: To further demonstrate that in vivo gene editing-generated tumors are SCLC, we performed gene set enrichment analysis (GSEA) using reported signatures from mouse and human SCLC.
- Full pipeline: stage not stated [GSEA]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: Single-Cell Differential Gene Expression Analysis and GSEA.
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### The epithelial <i>C15ORF48/miR-147-NDUFA4</i> axis is an essential regulator of gut inflammation, energy metabolism, and the microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2315944121 | PMCID: PMC11228508 | PMID: 38917002
- Evidence: ( A ) GSEA pathway enrichment analysis of up-regulated genes (fold change >1.5; P < 0.05; RPKM > 1) in unchallenged C15ORF48/miR-147 −/− (KO) colonocytes.
- Full pipeline: quantification [GSEA] -> stage not stated [PyMOL]

### A druggable cascade links methionine metabolism to epigenomic reprogramming in squamous cell carcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2320835121 | PMCID: PMC11214090 | PMID: 38900797
- Evidence: Using differentially expressed genes between control and knockdown groups, we performed gene set enrichment analysis (GSEA) against 6,449 public gene-sets in an unbiased manner ( 38 ).
- Full pipeline: differential/statistical testing [GSEA]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: Gene Set Enrichment Analysis (GSEA) results suggested that MOZ inhibition in MOZ-TIF2 LSK cells turns on a hematopoietic differentiation program, as differentially expressed genes were enriched in gene sets involved in myeloid development and mature hematopoietic cells ( Fig.
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### AMBRA1 levels predict resistance to MAPK inhibitors in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2400566121 | PMCID: PMC11194594 | PMID: 38870061
- Evidence: Gene Set Enrichment Analysis (GSEA) indicated a significant enrichment for “Undifferentiated” and NCSC-like gene sets ( 37 ) in the AMBRA1 LOW groups, while the “Melanocytic” gene set ( 37 ) was enriched in the AMBRA1 HIGH groups ( Fig.
- Full pipeline: normalisation [RSEM] -> stage not stated [GSEA, ImageJ v1.52]

### Protective function and differentiation cues of brain-resident CD8+ T cells during surveillance of latent <i>Toxoplasma gondii</i> infection. (PNAS 2024)

- DOI: 10.1073/pnas.2403054121 | PMCID: PMC11181119 | PMID: 38838017
- Evidence: ( C ) GSEA using tissue-resident T cell gene signatures (from refs.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### EHMT2-mediated transcriptional reprogramming drives neuroendocrine transformation in non-small cell lung cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2317790121 | PMCID: PMC11161775 | PMID: 38814866
- Evidence: Gene Set Enrichment Analysis (GSEA) on paired cell lines indicated that SCLC-related gene expression was significantly enriched in T-PC9 and T-H1650 ( Fig.
- Full pipeline: stage not stated [GSEA]

### Long noncoding RNA LIRIL2R modulates FOXP3 levels and suppressive function of human CD4<sup>+</sup> regulatory T cells by regulating IL2RA. (PNAS 2024)

- DOI: 10.1073/pnas.2315363121 | PMCID: PMC11161746 | PMID: 38805281
- Evidence: Analysis of TF Binding Sites, Pathway Analysis, and GSEA.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9, kallisto] -> differential/statistical testing [R, limma v3.42.2] -> stage not stated [GSEA]

### SUMO-specific protease 1 regulates germinal center B cell response through deSUMOylation of PAX5. (PNAS 2024)

- DOI: 10.1073/pnas.2314619121 | PMCID: PMC11145296 | PMID: 38776375
- Evidence: GSEA from Broad Institute was used following the instruction.
- Full pipeline: alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Evidence: ( E ) GSEA analysis utilizing HALLMARK collection, normalized enrichment score (NES), and adjusted P -values (padj) are indicated.
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### Astrocyte-to-microglia communication via Sema4B-Plexin-B2 modulates injury-induced reactivity of microglia. (PNAS 2024)

- DOI: 10.1073/pnas.2400648121 | PMCID: PMC11145257 | PMID: 38781210
- Evidence: ( F ) Gene Set Enrichment Analysis (GSEA) showing significantly dysregulated canonical pathways in the Sema4B −/− immune fraction.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### Interferon signaling in the nasal epithelium distinguishes among lethal and common cold coronaviruses and mediates viral clearance. (PNAS 2024)

- DOI: 10.1073/pnas.2402540121 | PMCID: PMC11127059 | PMID: 38758698
- Evidence: Genes with significant up- or downregulation were assessed using DESeq2 followed by Gene Set Enrichment Analysis (GSEA) ( 45 , 46 ).
- Full pipeline: stage not stated [DESeq2, GSEA]

### Macrophage transplantation rescues RNASET2-deficient leukodystrophy by replacing deficient microglia in a zebrafish model. (PNAS 2024)

- DOI: 10.1073/pnas.2321496121 | PMCID: PMC11126979 | PMID: 38753517
- Evidence: For GSEA, genes were ranked according to their Wald statistic results from the differential expression analysis.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [R v4.3, fgsea v1.28.0, ggplot2 v3.4.4] -> stage not stated [HTSeq v2.0]

### Simultaneous targeting of peripheral and brain tumors with a therapeutic nanoparticle to disrupt metabolic adaptability at both sites. (PNAS 2024)

- DOI: 10.1073/pnas.2318119121 | PMCID: PMC11098113 | PMID: 38709930
- Evidence: Gene set enrichment analysis (GSEA) on the genes involved in the NER pathway of Kyoto encyclopedia of genes and genomes (KEGG) databases revealed enrichment scores (ES) of less than zero (ES < 0) for T-Platin-M-NP group vs. cisplatin group and T-Platin-M-NP group vs. control group which suggest that NER-related genes are down-regulated with T-Platin-M-NP treatment ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Cancer-stromal cell interactions in breast cancer brain metastases induce glycocalyx-mediated resistance to HER2-targeting therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322688121 | PMCID: PMC11098130 | PMID: 38709925
- Evidence: GSEA was performed using the Broad GSEA Application (GSEA Java; v4.1.0) with Hallmark gene sets v7.4 ( 26 , 27 ).
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v1.18.1] -> normalisation [edgeR] -> differential/statistical testing [DESeq2 v1.18.1, MACS2 v2.1.1.20160309] -> stage not stated [GSEA, GSVA]

### OTUB2 silencing promotes ovarian cancer via mitochondrial metabolic reprogramming and can be synthetically targeted by CA9 inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2315348121 | PMCID: PMC11087800 | PMID: 38701117
- Evidence: The results of gene set enrichment analysis (GSEA) indicated that overexpression of either OTUB2 or SNX29P2 suppresses the glycolysis pathway and enhances OXPHOS activity ( Fig.
- Full pipeline: stage not stated [GSEA]

### Species-wide quantitative transcriptomes and proteomes reveal distinct genetic control of gene expression variation in yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2319211121 | PMCID: PMC11087752 | PMID: 38696467
- Evidence: Based on the CV, we performed a functional exploration by gene set enrichment analysis (GSEA) ( 75 ) using the fgsea R package ( 76 ) for the gene ontology annotation ( 77 , 78 ) to detect cellular pathways with a conserved regulation across the population.
- Full pipeline: quantification [R, WGCNA] -> normalisation [WGCNA] -> stage not stated [GSEA, fgsea]

### TRAF3 loss-of-function reveals the noncanonical NF-κB pathway as a therapeutic target in diffuse large B cell lymphoma. (PNAS 2024)

- DOI: 10.1073/pnas.2320421121 | PMCID: PMC11067025 | PMID: 38662551
- Version used: **4.1.0**
- Evidence: Preranked gene-set enrichment analysis (GSEA v4.1.0, https://www.gsea-msigdb.org/gsea/index.jsp ) was performed using the log 2 FC between TRAF3 _del vs.
- Full pipeline: stage not stated [DESeq2 v1.26.0, GSEA v4.1.0, limma]

### Liver cancer development driven by the AP-1/c-Jun~Fra-2 dimer through c-Myc. (PNAS 2024)

- DOI: 10.1073/pnas.2404188121 | PMCID: PMC11067056 | PMID: 38657045
- Evidence: Gene set enrichment analysis [GSEA ( 31 )] revealed enrichment in MSigDB Hallmarks gene sets related to cell cycle, p53 pathway, cell death, and hypoxia in the 3 mutant groups, when compared to their respective control littermates ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: GSEA was conducted using the R package “clusterProfiler” (v.3.12.0) for the gene list ranked by fold changes [log 2 (fold change)] ( 29 ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Autoimmunity against melanoma differentiation-associated gene 5 induces interstitial lung disease mimicking dermatomyositis in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2313070121 | PMCID: PMC11032490 | PMID: 38588434
- Evidence: Gene set enrichment analysis (GSEA) showed R-MMU-6798695: Neutrophil degranulation, and GO:0045321: leukocyte activation ( Fig.
- Full pipeline: differential/statistical testing [Metascape] -> stage not stated [GSEA, MACS2]

### The MUC1-HIF-1α signaling axis regulates pancreatic cancer pathogenesis through polyamine metabolism remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2315509121 | PMCID: PMC10998584 | PMID: 38547055
- Evidence: GSEA pathway enrichment analysis revealed 11 negatively enriched pathways with SAT1 loss ( Fig.
- Full pipeline: alignment/mapping [DESeq2, R, TopHat] -> differential/statistical testing [DESeq2, R, TopHat] -> stage not stated [GSEA, ImageJ]

### Normalizing granuloma vasculature and matrix improves drug delivery and reduces bacterial burden in tuberculosis-infected rabbits. (PNAS 2024)

- DOI: 10.1073/pnas.2321336121 | PMCID: PMC10998582 | PMID: 38530888
- Evidence: Due to unsupported ontologies/pathways for O. cuniculus , we performed GSEA (clusterProfiler v.4.10.0) by converting rabbit ensemble gene IDs to human orthologs using BioMart database (biomaRt v.2.58.0) and excluding genes for which duplicate matches, or no matches were found.
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> normalisation [DESeq2 v1.42.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.0] -> stage not stated [ImageJ]

### Improved RNA stability estimation through Bayesian modeling reveals most <i>Salmonella</i> transcripts have subminute half-lives. (PNAS 2024)

- DOI: 10.1073/pnas.2308814121 | PMCID: PMC10998600 | PMID: 38527194
- Evidence: To investigate the physiological consequences of RBP deletion, we identified pathways enriched in differentially stabilized and differentially expressed transcripts in the proQ and cspC/E deletion strains with the GSEA algorithm ( 50 ) ( Fig.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [Cutadapt v4.1, HTSeq] -> quantification [HTSeq] -> normalisation [Stan] -> differential/statistical testing [GSEA, Stan] -> simulation/modelling [Stan] -> stage not stated [R, edgeR, limma]

### IL7 increases targeted lipid nanoparticle-mediated mRNA expression in T cells in vitro and in vivo by enhancing T cell protein translation. (PNAS 2024)

- DOI: 10.1073/pnas.2319856121 | PMCID: PMC10990120 | PMID: 38513098
- Evidence: GSEA ( 21 ) was performed using lists of DEG.
- Full pipeline: alignment/mapping [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: ( B ) Gene signatures that are significantly enriched in hA3G-knockdown ATL cells (ATL-55T+), based on GSEA analysis with RNA-seq.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Isotype switching in human memory B cells sets intrinsic antigen-affinity thresholds that dictate antigen-driven fates. (PNAS 2024)

- DOI: 10.1073/pnas.2313672121 | PMCID: PMC10990115 | PMID: 38502693
- Evidence: GSEA was run with a custom function based on the fgseaMultilevel function from the fgsea package ( https://github.com/TranLab/ModuleLists ) that includes MSigDB gene collections as well as blood transcription modules ( 63 ) and other gene sets relevant to immunology and blood transcriptomics ( 64 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, GSEA, R, fgsea]

### SRF transcriptionally regulates the oligodendrocyte cytoskeleton during CNS myelination. (PNAS 2024)

- DOI: 10.1073/pnas.2307250121 | PMCID: PMC10962977 | PMID: 38483990
- Evidence: As expected, Gene Set Enrichment Analysis (GSEA) of SRF-KO OPC genes identified depletion of pathways associated with “Transcription regulation” and “Cell cycle” ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Endogenous retrovirus HERVH-derived lncRNA <i>UCA1</i> controls human trophoblast development. (PNAS 2024)

- DOI: 10.1073/pnas.2318176121 | PMCID: PMC10962953 | PMID: 38483994
- Evidence: Correspondingly, the gene set enrichment analysis (GSEA) also confirmed that the type I interferon signaling was increased during STB induction from hTSCs overexpressing UCA1 ( Fig.
- Full pipeline: dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [WGCNA] -> stage not stated [GSEA]

### Epidermal growth factor receptor (EGFR) is a target of the tumor-suppressor E3 ligase FBXW7. (PNAS 2024)

- DOI: 10.1073/pnas.2309902121 | PMCID: PMC10962967 | PMID: 38483988
- Evidence: RNA Sequencing Analysis and GSEA.
- Full pipeline: alignment/mapping [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### RN7SL1 may be translated under oncogenic conditions. (PNAS 2024)

- DOI: 10.1073/pnas.2312322121 | PMCID: PMC10962956 | PMID: 38478683
- Evidence: To characterize gene expression in GFP-positive cells, Gene Set Enrichment Analysis (GSEA) was performed by using Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway.
- Full pipeline: stage not stated [GSEA]

### Sustained AhR activity programs memory fate of early effector CD8<sup>+</sup> T cells. (PNAS 2024)

- DOI: 10.1073/pnas.2317658121 | PMCID: PMC10945852 | PMID: 38437537
- Evidence: Gene set enrichment analysis (GSEA) based on the previously identified AhR activation gene signature ( 44 ) showed that genes transactivated by AhR were enriched in IL-2 + T cells ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Pathogenic GATA2 genetic variants utilize an obligate enhancer mechanism to distort a multilineage differentiation program. (PNAS 2024)

- DOI: 10.1073/pnas.2317147121 | PMCID: PMC10927522 | PMID: 38422019
- Evidence: GSEA analysis revealed that GATA2-activated genes in −77 −/− cells conform to a hallmark mast cell signature ( Dataset Table S1 , P = 0.0029).
- Full pipeline: quantification [RSEM] -> stage not stated [GSEA]

### Hippo cooperates with p53 to maintain foregut homeostasis and suppress the malignant transformation of foregut basal progenitor cells. (PNAS 2024)

- DOI: 10.1073/pnas.2320559121 | PMCID: PMC10927585 | PMID: 38408237
- Evidence: ...ageal epithelium, RNA and protein isolation, western blot analysis, RNA sequencing, differential gene expression, Gene Ontology enrichment, KEGG, and GSEA analysis, and quantification and statistical analysis can be found in SI Appendix .
- Full pipeline: quantification [GSEA] -> differential/statistical testing [GSEA]

### Enhancing chimeric antigen receptor T cell therapy by modulating the p53 signaling network with Δ133p53α. (PNAS 2024)

- DOI: 10.1073/pnas.2317735121 | PMCID: PMC10927528 | PMID: 38408246
- Evidence: ( D ) Summary of results for GSEA of all Hallmark and GO Biological Process gene sets.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### IL-27 regulates the differentiation of follicular helper NKT cells via metabolic adaptation of mitochondria. (PNAS 2024)

- DOI: 10.1073/pnas.2313964121 | PMCID: PMC10907256 | PMID: 38394242
- Evidence: GSEA was performed to determine the statistical significance of the enrichment of known transcriptional signatures in a ranked list of genes ( 49 , 50 ).
- Full pipeline: read trimming [fastp] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ, MACS2]

### Methyltransferase Setd2 prevents T cell-mediated autoimmune diseases via phospholipid remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2314561121 | PMCID: PMC10895270 | PMID: 38359295
- Evidence: ( G ) GSEA analysis of enrichment in IL-17 signaling pathway-related genes from Th0 cells.
- Full pipeline: stage not stated [GSEA]

### Cysteine induces mitochondrial reductive stress in glioblastoma through hydrogen peroxide production. (PNAS 2024)

- DOI: 10.1073/pnas.2317343121 | PMCID: PMC10895255 | PMID: 38359293
- Evidence: Single Sample Gene Set Enrichment Analysis (ssGSEA) was applied to score the metabolic signature in each tumor sample using their RNAseq expression profiles ( 69 ). ssGSEA was implemented using the “gsva” package (v1.30.0) in R.
- Full pipeline: stage not stated [GSEA]

### Tumor circadian clock strength influences metastatic potential and predicts patient prognosis in luminal A breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2311854121 | PMCID: PMC10873596 | PMID: 38319971
- Evidence: Transcripts significantly cycling in either luminal A or noncancerous samples (BHq < 0.05) were ranked by the log fold change in amplitude and analyzed by GSEA.
- Full pipeline: stage not stated [GSEA]

### RNF20 contributes to epigenetic immunosuppression through CDK9-dependent LSD1 stabilization. (PNAS 2024)

- DOI: 10.1073/pnas.2307150121 | PMCID: PMC10873621 | PMID: 38315842
- Evidence: These findings were further corroborated by GSEA ( Fig.
- Full pipeline: stage not stated [GSEA]

### TM4SF19 controls GABP-dependent <i>YAP</i> transcription in head and neck cancer under oxidative stress conditions. (PNAS 2024)

- DOI: 10.1073/pnas.2314346121 | PMCID: PMC10873613 | PMID: 38315837
- Evidence: ( H ) GSEA data of YAP/TEAD direct target gene expressions in TM4SF19 knockdown YD10B cells compared to those with control.
- Full pipeline: normalisation [RSEM] -> stage not stated [GSEA, ImageJ]

### Effective treatment of optic neuropathies by intraocular delivery of MSC-sEVs through augmenting the G-CSF-macrophage pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2305947121 | PMCID: PMC10861878 | PMID: 38289952
- Evidence: Gene set enrichment analysis (GSEA) confirmed the significantly positively enriched terms “lysosome”, “apoptotic cell clearance”, and “lipid catabolic process” in the Mo/MΦ2 cluster ( Fig.
- Full pipeline: dimensionality reduction/clustering [CellChat, GSEA, UMAP] -> visualisation [UMAP]

### Single-cell analysis of refractory anti-SRP necrotizing myopathy treated with anti-BCMA CAR-T cell therapy. (PNAS 2024)

- DOI: 10.1073/pnas.2315990121 | PMCID: PMC10861907 | PMID: 38289960
- Evidence: ( E ) Heatmap showing single-sample gene set enrichment analysis (GSEA) scores of indicated signatures in CD4 + T cells, CD8 + T cells, NK cells, and myeloid cells of patient with IMNM at baseline, at 1 mo, at 3 mo, at 6 mo, at 9 mo, at 12 mo, at 15 mo, and at 18 mo post-infusion.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSVA] -> stage not stated [GSEA]

### Pharmacological modulation of RB1 activity mitigates resistance to neoadjuvant chemotherapy in locally advanced rectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2304619121 | PMCID: PMC10861914 | PMID: 38289962
- Evidence: In addition, Gene Set Enrichment Analysis (GSEA) in the Hallmark gene sets identified significant upregulation of cell cycle–related pathways in the nonresponder group, including MYC targets, E2F targets, G2/M checkpoint genes, and DNA repair pathway ( Fig.
- Full pipeline: stage not stated [GSEA, HOMER]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; proteases trigger eosinophil-mediated skin inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2309243121 | PMCID: PMC10861893 | PMID: 38289950
- Evidence: ( D ) GSEA of significant DEGs with gene sets (adjusted P -value < 0.05) from the KEGG.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [GSEA]

### Single-cell RNA sequencing unveils unique transcriptomic signatures of endothelial cells and role of ENO1 in response to disturbed flow. (PNAS 2024)

- DOI: 10.1073/pnas.2318904121 | PMCID: PMC10835041 | PMID: 38261622
- Evidence: ( F ) GSEA plots showing that the enrichment of gene sets with response to hypoxia, inflammatory response, response to cytokine, response to ROS regulation of cell proliferation, as well as cell cycle, are significantly enriched in DS-clusters.
- Full pipeline: normalisation [Seurat v4.0.2] -> dimensionality reduction/clustering [GSEA, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0.2]

### Dancr-BRG1 regulates Nfatc1 transcription and Pgc1β-dependent metabolic shifts in osteoclastogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2313656121 | PMCID: PMC10835043 | PMID: 38252822
- Evidence: To further investigate this phenomenon, we conducted Gene Set Enrichment Analysis (GSEA) of TCA cycle and oxidative phosphorylation (OXPHOS) using RNA-seq data, which revealed that Dancr-KO dramatically promoted these two biological processes ( Fig.
- Full pipeline: stage not stated [GSEA]

### The exostosin glycosyltransferase 1/STAT3 axis is a driver of breast cancer aggressiveness. (PNAS 2024)

- DOI: 10.1073/pnas.2316733121 | PMCID: PMC10801894 | PMID: 38215181
- Evidence: For gene set enrichment analysis (GSEA), Spearman’s rank correlation coefficient between the gene of interest and the whole genome was computed, downloaded, and subjected to GSEA and visualization of the result using the R package ClusterProfiler ( 62 ) and Enrichplot.
- Full pipeline: dimensionality reduction/clustering [GSEA, R] -> visualisation [GSEA, R] -> stage not stated [Matplotlib]

### ALK signaling primes the DNA damage response sensitizing ALK-driven neuroblastoma to therapeutic ATR inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2315242121 | PMCID: PMC10769851 | PMID: 38154064
- Evidence: ( F and G ) Hallmark GSEA showing normalized enrichment scores and corresponding FDR values with running score plot (panel G ) shown for E2F targets, the most strongly enriched gene set.
- Full pipeline: normalisation [GSEA] -> differential/statistical testing [GSEA, R]

### Cystathionine γ-lyase is a major regulator of cognitive function through neurotrophin signaling and neurogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2528478122 | PMCID: PMC12772173 | PMID: 41452980
- Evidence: We further filtered proteins by P -value of less than or equal to 0.05 and a fold difference of at least 1.2 fold, and then compared the up- and downregulated signatures with a public human postmortem hippocampal AD gene expression dataset ( GSE36980 ) and performed GSEA.
- Full pipeline: stage not stated [GSEA]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Evidence: ( E ) GSEA using GO Biological Process terms on CVG-1 DEGs from A-485 ( Top panel) and dCBP-1 ( Lower panel) treatment.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### Dysregulated NAMPT signaling underlines the immune-suppressive microenvironment in venous leg ulcers. (PNAS 2025)

- DOI: 10.1073/pnas.2512142122 | PMCID: PMC12772187 | PMID: 41439711
- Evidence: ( E ) Gene set enrichment analysis (GSEA) plot for Hallmark signaling pathways enriched in NS and VLU fibroblasts.
- Full pipeline: dimensionality reduction/clustering [CellChat, UMAP] -> stage not stated [GSEA]

### A PSAT1 buff of YBX1 transcriptionally sustains HLA-E-mediated evasion of NK immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2505658122 | PMCID: PMC12772220 | PMID: 41428871
- Evidence: ( B–E ) Gene Ontology (GO) and Gene Set Enrichment Analysis (GSEA) revealed enriched immune-related processes in PSAT1-knockdown LNCaP cells, including significant activation of the NK-cell-mediated innate immune response.
- Full pipeline: stage not stated [GSEA]

### Antibiotic-induced microbiota depletion impairs the proregenerative response to a biological scaffold. (PNAS 2025)

- DOI: 10.1073/pnas.2510841122 | PMCID: PMC12772165 | PMID: 41428865
- Evidence: GSEA was performed with fgsea v1.28.0, ranking results by the product of logFC and −log10(padj), using REACTOME and HALLMARK pathways.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.42.0] -> stage not stated [GSEA, fgsea v1.28.0]

### Convergent mutation trajectories convert functional self-tolerance in IGHV4-34 B cells to genetic tolerance encoded in the antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2522257122 | PMCID: PMC12745689 | PMID: 41410768
- Evidence: GSEA, ( 75 ) was performed on Hallmark (mh) and Cell Signature (m8) ontologies, and terms with FWER < 0.05 were defined as significantly enriched.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [GSEA]

### Dual-targeted ping-pong CAR T cells: Leveraging peripheral expansion to improve solid tumor immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2518996122 | PMCID: PMC12745717 | PMID: 41397127
- Evidence: ( I ) Gene Set Enrichment Analysis (GSEA) of differentially expressed genes performed using the fGSEA package.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Bioconductor, GSVA, R, ggplot2]

### Glomerular endothelial cells eliminate nicotinamide adenine dinucleotide to instruct CD103&lt;sup&gt;+&lt;/sup&gt; T cells in human lupus nephritis. (PNAS 2025)

- DOI: 10.1073/pnas.2507422122 | PMCID: PMC12718392 | PMID: 41385546
- Evidence: To investigate metabolic changes in CD103 + T cells, we performed GSEA on single-cell renal data from LN patients, comparing CD4 + CD103 + versus CD4 + CD103 − T cells.
- Full pipeline: stage not stated [GSEA]

### TAPT1 interacts with SUCO to maintain the homeostasis of newly synthesized proteins and brain development in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2501361122 | PMCID: PMC12718307 | PMID: 41379998
- Evidence: GSEA and Enrichment of GO terms were performed by R package “ClusterProfiler” (v4.7.1.003) ( 57 ).
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [GSEA] -> stage not stated [ImageJ]

### Intracellular &lt;i&gt;Acinetobacter baumannii&lt;/i&gt; acts as a transient reservoir in lung infection via a "persist and resist" strategy. (PNAS 2025)

- DOI: 10.1073/pnas.2511369122 | PMCID: PMC12718349 | PMID: 41364768
- Evidence: GSEA.
- Full pipeline: visualisation [R, ggplot2] -> stage not stated [GSEA]

### Galectin-9 binding to HLA-DR in dendritic cells controls immune synapse formation and T cell proliferation. (PNAS 2025)

- DOI: 10.1073/pnas.2501381122 | PMCID: PMC12718305 | PMID: 41359845
- Evidence: For Gene Set Enrichment Analysis, fold changes per gene were determined by calculating the ratio between control and knockdown animals for each biological replicate separately.
- Full pipeline: alignment/mapping [STAR] -> normalisation [DESeq2, R] -> differential/statistical testing [Fiji, ImageJ] -> stage not stated [GSEA, fgsea]

### Ace2 safeguards embryonic hematopoietic stem and progenitor cell production by restraining Nlrp3-mediated pyroptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2515641122 | PMCID: PMC12704739 | PMID: 41348733
- Evidence: GSEA.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.1.0] -> quantification [StringTie v1.3.3b] -> dimensionality reduction/clustering [clusterProfiler v4.6.1] -> differential/statistical testing [DESeq2 v1.10.1, R v3.2.3] -> stage not stated [GSEA, ImageJ]

### Prostaglandin E&lt;sub&gt;2&lt;/sub&gt;-EP2/EP4 signaling induces the tumor-infiltrating Treg phenotype for tumor growth. (PNAS 2025)

- DOI: 10.1073/pnas.2424251122 | PMCID: PMC12704795 | PMID: 41343674
- Evidence: To examine this, we carried out gene set enrichment analysis (GSEA) with their TI-Treg signature genes as the gene set and also mapped the genes of the TI-Treg signature in the volcano plot of EP4 agonist-induced genes.
- Full pipeline: alignment/mapping [GSEA] -> dimensionality reduction/clustering [UMAP]

### Oxidative pentose phosphate pathway is required for T cell activation and antitumor immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2516288122 | PMCID: PMC12704759 | PMID: 41337482
- Evidence: RNA Sequencing (RNA-seq), Differential Expression, and Gene Set Enrichment Analysis.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Evidence: For the gene set enrichment analysis (GSEA) results from DESeq2 analysis were used for a metric construction as follows: log2fc* − log10( P value).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### Glycoside hydrolase-mediated glucomannan catabolism in &lt;i&gt;Segatella copri&lt;/i&gt;, a target of microbiota-directed foods for malnourished children. (PNAS 2025)

- DOI: 10.1073/pnas.2521522122 | PMCID: PMC12704710 | PMID: 41329729
- Evidence: Each set of vertical bars correspondi to the gene in a significantly upregulated PUL (q < 0.05, GSEA).
- Full pipeline: quality control [DESeq2, kallisto] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [AlphaFold, GSEA, fgsea]

### Brain-wide mapping of developmental trajectories of cerebellar efferent projections. (PNAS 2025)

- DOI: 10.1073/pnas.2521091122 | PMCID: PMC12685143 | PMID: 41289407
- Evidence: To examine the temporal dynamics of molecular maturation, we performed Gene Set Enrichment Analysis (GSEA) on Differential Expression (DE) results across embryonic and early postnatal time points.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler]

### <i>Lrig1</i>-expressing quiescent stem cells maintain vocal fold mucosal homeostasis via <i>Notch</i> signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2513590122 | PMCID: PMC12685045 | PMID: 41289377
- Evidence: Gene set enrichment analysis (GSEA) confirmed that silencing of cell type–specific genes in Lrig1 + cells is accompanied by the activation of a global transcriptional program related to RNA metabolism, epigenetic regulation and protein ubiquitination ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### USP1-TRAF2 axis-regulated mortalin stability mediates chemoresistance by disrupting calcium transport in peripheral T-cell lymphoma. (PNAS 2025)

- DOI: 10.1073/pnas.2504195122 | PMCID: PMC12685112 | PMID: 41289404
- Evidence: We previously observed elevated cytoplasmic calcium due to mortalin downregulation, and gene set enrichment analysis (GSEA) indicated significant activation of the calcium signaling pathway post–doxorubicin treatment ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Drug repurposing screen identifies an HRI activating compound that promotes adaptive mitochondrial remodeling in MFN2-deficient cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517552122 | PMCID: PMC12685026 | PMID: 41289394
- Evidence: Further supporting this idea, geneset enrichment analysis (GSEA) showed increased expression of UPR and mTOR genesets—two genesets that include many ISR target genes—in HEK293T cells treated with MBX or PGL ( Fig.
- Full pipeline: stage not stated [GSEA]

### Using gnotobiotic mice to decipher effects of gut microbiome repair in undernourished children on tuft and goblet cell function. (PNAS 2025)

- DOI: 10.1073/pnas.2523178122 | PMCID: PMC12685025 | PMID: 41289388
- Evidence: ( B ) Lollipop plot illustrating the normalized enrichment score (NES) for mcSEED metabolic pathways with significantly altered expression from microbial RNA-seq data, as identified from GSEA.
- Full pipeline: normalisation [GSEA]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: Visualization was generated with ggplot2 package, heatmaps were created with ComplexHeatmap package ( 63 ), volcano plots with the EnhancedVolcano Package ( 64 ) and GSEA with decoupleR ( 27 ).
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### Engineering a spatiotemporal macrophage circuit via STING phase separation to override immune suppression in pancreatic cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2504718122 | PMCID: PMC12664005 | PMID: 41264244
- Evidence: ( F ) Gene Ontology biological process (GO BP) enrichment was assessed by GSEA, with genes ordered according to log 2 FC values comparing each TAM subset to the remaining TAMs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, GSEA]

### The liver talks back: NPY orchestrates attraction of cancer cells and CHK2-dependent clonogenicity in the metastatic niche. (PNAS 2025)

- DOI: 10.1073/pnas.2518418122 | PMCID: PMC12663930 | PMID: 41252148
- Evidence: RNA sequencing (RNA-seq), differential gene expression (DGEA), and gene set enrichment analysis (GSEA) of metastatic liver tissue (MET) confirmed induction of metastatic melanoma-related signatures as defined in humans ( 23 ) and mice ( 24 ).
- Full pipeline: differential/statistical testing [DESeq2, GSEA]

### An adipo-osteoprogenitor population in the endosteal niche contributes to bone and fat formation in adult mouse bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2502436122 | PMCID: PMC12663985 | PMID: 41248279
- Evidence: GSEA with MsigDB gene sets was performed to identify pathways with significant differences across cell clusters.
- Full pipeline: quality control [Seurat v4.1.1, UMAP] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.1.1, UMAP]

### Machine-learning models based on histological images from healthy donors identify imageQTLs and predict chronological age. (PNAS 2025)

- DOI: 10.1073/pnas.2423469122 | PMCID: PMC12646272 | PMID: 41218125
- Evidence: Additionally, we performed GSEA using the internal champ.GSEA function.
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [PLINK v2.0] -> stage not stated [DESeq2, GSEA, QuPath v0.4.3]

### Erythroid precursors regulate local oxygen tension and repair outcomes in the bone marrow niche. (PNAS 2025)

- DOI: 10.1073/pnas.2522548122 | PMCID: PMC12646327 | PMID: 41218120
- Version used: **4.3.3**
- Evidence: For GSEA, a preranked list of genes was generated based on fold changes between comparisons and analyzed using GSEA v4.3.3.
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA v4.3.3, Seurat v4.0]

### Forward genetic screening in engineered colorectal cancer organoids identifies regulators of metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2510910122 | PMCID: PMC12646219 | PMID: 41218116
- Evidence: Gene set enrichment analysis (GSEA) indicated that sgBcl2l13 carcinoma cells downregulated the interferon alpha and gamma (IFN-α/IFN-γ) response gene signatures and upregulated the hypoxia response ( SI Appendix , Fig.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Seurat]

### METTL3-dependent m6A RNA methylation suppresses aberrant mammary epithelial differentiation and neoplastic transformation. (PNAS 2025)

- DOI: 10.1073/pnas.2514643122 | PMCID: PMC12646209 | PMID: 41218124
- Evidence: ( F ) GSEA reveals the luminal and invasive breast cancer signature genes are significantly enriched in MCF10A cells depleted of METTL3 versus control.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### cGAS-agonistic spherical nucleic acids reprogram the glioblastoma immune microenvironment and promote antitumor immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2409557122 | PMCID: PMC12626011 | PMID: 41183206
- Evidence: ( L ) Top 5 Kyoto Encyclopedia of Genes and Genomes-enriched pathways identified by gene set enrichment analysis (GSEA), with a false discovery rate (FDR) < 25% of the t statistic, sorted by normalized enrichment scores (NES).
- Full pipeline: normalisation [GSEA] -> differential/statistical testing [GSEA]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: GSEA.
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### p53 regulates the expression of histone modifiers to restrict stemness and maintain differentiated luminal identity in breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2522646122 | PMCID: PMC12595495 | PMID: 41160600
- Evidence: Genes were ranked according to fold change following treatment and compared to the CREIGHTON_ENDOCRINE_THERAPY_RESISTANCE_1 gene signature (MSigDB) ( 59 ) by GSEA ( Dataset S7 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ggplot2, survival (R), tidyverse]

### Nanomaterial-induced mitochondrial biogenesis enhances intercellular mitochondrial transfer efficiency. (PNAS 2025)

- DOI: 10.1073/pnas.2505237122 | PMCID: PMC12582283 | PMID: 41134634
- Evidence: To delve deeper into this finding, we employed Gene Set Enrichment Analysis (GSEA) on smooth muscle cells (SMCs) post MitoFactory-transfer.
- Full pipeline: stage not stated [GSEA]

### Disrupted developmental signaling induces novel transcriptional states. (PNAS 2025)

- DOI: 10.1073/pnas.2418351122 | PMCID: PMC12582265 | PMID: 41118206
- Evidence: Differential Expression and Gene Set Enrichment Analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA]

### HIF2α negatively regulates MYCN protein levels and promotes a low-risk noradrenergic phenotype in neuroblastoma. (PNAS 2025)

- DOI: 10.1073/pnas.2516922122 | PMCID: PMC12582314 | PMID: 41118218
- Evidence: Eight clusters were defined by differentially expressed genes and gene set enrichment analysis (GSEA).
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2, FastQC, GSEA] -> visualisation [UMAP] -> stage not stated [R, Scanpy, Seurat]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: Gene set enrichment analysis (GSEA) ( 31 ) was performed using ClusterProfiler ( 32 ) in R version 4.1.2 using gene sets obtained from MSigDB ( 33 ) or published studies [i.e., Wang and Balk androgen response gene sets ( 34 , 35 )].
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Precise gene editing of pathogenic Lamin A mutations corrects cardiac disease. (PNAS 2025)

- DOI: 10.1073/pnas.2515267122 | PMCID: PMC12582316 | PMID: 41082656
- Evidence: ( I ) Gene Set Enrichment Analysis (GSEA) bar plot showing the enriched (up) and underrepresented (down) mouse hallmark gene sets in R249Q/R249Q +AAV9 sgRNA3 compared to R249Q/R249Q +AAV9 control mice. ns = nonsignificant; * P < 0.05; ** P < 0.01.
- Full pipeline: stage not stated [GSEA]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Genome Ontology and GSEA were completed using WebGestaltR package (v1.0.0) ( 59 ) and GSEA package (v4.3.2) on database (v2022.1.Hs) ( 60 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: ( E ) GSEA plot showing enrichment of the Th1/Th2 pathway in control compared to PKA-KO cells.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Autoimmunity-associated DIORA1 binds the MRCK family of serine/threonine kinases and controls cell motility. (PNAS 2025)

- DOI: 10.1073/pnas.2426917122 | PMCID: PMC12519202 | PMID: 41042840
- Evidence: Transcriptomic data were processed using standard pipelines and analyzed with DESeq2 and gene set enrichment tools, including GSEA and overrepresentation analysis using HALLMARK gene sets.
- Full pipeline: visualisation [STRING db] -> stage not stated [AlphaFold, DESeq2, GSEA, UCSF Chimera]

### Activation of epigenetic reprogramming via crotonylation overcomes resistance to EGFR-TKI therapy in lung cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2509255122 | PMCID: PMC12519144 | PMID: 41026825
- Evidence: ( I ) GSEA shows enrichment of genes upregulated in the PI3K/AKT signaling pathway in HCC827/Er cells compared to HCC827 cells.
- Full pipeline: stage not stated [GSEA]

### Biliverdin reductase A is a major determinant of protective NRF2 signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2513120122 | PMCID: PMC12519219 | PMID: 41026820
- Evidence: Further Gene Set Enrichment Analysis (GSEA) of BVR-NRF2 ChIP sets highlighted genes implicated in inflammatory pathways, heme metabolism, and redox signaling ( Fig.
- Full pipeline: stage not stated [GSEA]

### CRISPR screens identify the ATPase VCP as a druggable therapeutic vulnerability in cholangiocarcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2519568122 | PMCID: PMC12501119 | PMID: 40991439
- Evidence: Gene Set Enrichment Analysis (GSEA) revealed significant activation of cellular senescence pathways in both cell lines after prolonged CB-5339 exposure, with senescence-associated signatures markedly enriched (RBE: NES = 2.20, FDR = 1.07 × 10 −5 ; HuCCT1: NES = 1.60, FDR = 0.04) ( Fig.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Muscle-specific increased expression of &lt;i&gt;JAG1&lt;/i&gt; improves the skeletal muscle phenotype in dystrophin-deficient mice. (PNAS 2025)

- DOI: 10.1073/pnas.2506437122 | PMCID: PMC12501121 | PMID: 40986346
- Evidence: ( E and F ) Top enriched Gene Ontology terms from GSEA.
- Full pipeline: visualisation [R v4.3.3, ggplot2] -> stage not stated [GSEA, ImageJ]

### A TGF-βR/IL-2R immunomodulatory fusion protein transforms immunosuppression into T cell activation to enhance adoptive T cell therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2516951122 | PMCID: PMC12501114 | PMID: 40986340
- Version used: **4.1.0**
- Evidence: GSEA ( 55 ) was performed with GSEA (v4.1.0); log2 fold changes were calculated with a +1 pseudocount to account for zero-count genes and avoid infinite values.
- Full pipeline: alignment/mapping [Python, Scanpy] -> stage not stated [GSEA v4.1.0, scDblFinder]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Gene Set Enrichment Analysis (GSEA) was performed using clusterProfiler ( 36 ) (v4.12.0), with gene sets from the Molecular Signatures Database ( 37 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: ( C ) Gene Set Enrichment Analysis of differentially expressed genes in ( B ).
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Tubular ACSM3 deficiency impairs medium-chain fatty acid metabolism and aggravates kidney fibrosis. (PNAS 2025)

- DOI: 10.1073/pnas.2505752122 | PMCID: PMC12478119 | PMID: 40953271
- Evidence: Gene Set Enrichment Analysis showed that the downregulated genes were mainly enriched into metabolic pathways, and with a significant decrease in lipid metabolism related genes ( Fig.
- Full pipeline: stage not stated [GSEA, ImageJ]

### Replication stress-induced nuclear hypertrophy alters chromatin topology and impacts cancer cell fitness. (PNAS 2025)

- DOI: 10.1073/pnas.2424709122 | PMCID: PMC12452916 | PMID: 40928878
- Evidence: The results of the GSEA and GOBP analyses for the screen data are available in Dataset S2 .
- Full pipeline: quantification [CellProfiler v4.2.1] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Single-cell transcriptome combined with genetic tracing reveals a roadmap of fibrosis formation during proliferative vitreoretinopathy. (PNAS 2025)

- DOI: 10.1073/pnas.2424487122 | PMCID: PMC12452882 | PMID: 40920930
- Evidence: Gene set enrichment analysis (GSEA) further showed PVR MGCs were enriched in metabolic processes, whereas normal control MGCs were associated with physiological functions ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Monocle, Slingshot] -> visualisation [UMAP] -> stage not stated [Cellpose, GSEA]

### Restoring mitochondrial quantity and quality to reverse the Warburg effect and drive neuroblastoma differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2502483122 | PMCID: PMC12435223 | PMID: 40911595
- Evidence: Further analysis of gene set enrichment (GSEA) revealed positive enrichment of pathways related to neuronal differentiation and development, including “anterior–posterior pattern specification,” “regulation of axonogenesis,” “neuron maturation,” and “regulation of neurogenesis” in the RA + NEN group ( Fig.
- Full pipeline: stage not stated [GSEA]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Evidence: Preranked GSEA was performed for each contrast and/or correlation against gene sets extracted from the MSigDB (BROAD Institute) ( 44 ), and CHEA ( 45 , 46 ) databases.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### Inflammation awakens dormant cancer cells by modulating the epithelial-mesenchymal phenotypic state. (PNAS 2025)

- DOI: 10.1073/pnas.2515009122 | PMCID: PMC12435312 | PMID: 40901881
- Evidence: ( C ) Gene Set Enrichment Analysis (GSEA) was conducted to compare the awakened Sum159low-1 cells induced by bleomycin with Sum159low-1 cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Therapeutic restoration of mitochondria-endoplasmic reticulum cross talk for osteoarthritis. (PNAS 2025)

- DOI: 10.1073/pnas.2426992122 | PMCID: PMC12435279 | PMID: 40892916
- Evidence: Gene set enrichment analysis (GSEA) revealed upregulation of pathways related to MMP activation, whereas pathways associated with extracellular matrix receptor interactions were downregulated after MFN2 knockout ( Fig.
- Full pipeline: stage not stated [GSEA]

### Lysosomal reduced thiols are essential for mouse embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2427125122 | PMCID: PMC12435214 | PMID: 40892915
- Evidence: GSEA was carried out using WEB-based Gene SeT AnaLysis Toolkit (WebGestalt) ( 39 ), with signed significance scores (−log 10 adjusted P -value multiplied by the sign of the log 2 ‚ fold change) used as the ranking metric.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Tumor-expressed GPNMB orchestrates Siglec-9&lt;sup&gt;+&lt;/sup&gt; TAM polarization and EMT to promote metastasis in triple-negative breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2503081122 | PMCID: PMC12435292 | PMID: 40892920
- Evidence: GSEA further confirmed activation of NF-κB, CEBPB, ETS1, SP1, STAT3, MAPK , and BHLHE40 regulons ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [AlphaFold] -> machine learning [UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina, GSEA, R v4.3.0]

### Patient stratification reveals the molecular basis of disease co-occurrences. (PNAS 2025)

- DOI: 10.1073/pnas.2421060122 | PMCID: PMC12415287 | PMID: 40880536
- Evidence: In order to better characterize the molecular processes underlying the analyzed diseases, we performed Gene Set Enrichment Analyses (GSEA) ( 20 ) on the ranked lists of genes derived from differential expression—log Fold Change (logFC)—using annotations from Reactome ( 21 ), Kyoto Encyclopedia of Genes and Genomes ( 22 ) and Gene Ontology ( 23 ).
- Full pipeline: quality control [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [GSEA, limma]

### CRISPR with Transcriptional Readout reveals influenza transcription is modulated by NELF and can precipitate an interferon response. (PNAS 2025)

- DOI: 10.1073/pnas.2515564122 | PMCID: PMC12415228 | PMID: 40864651
- Evidence: To quantitatively characterize these associations, we performed gene set enrichment analysis (GSEA), for a larger set of RIG-I associated genes (the initial core set is too small for GSEA), and those genes identified as required for infection by a prior CRISPR screen ( Fig.
- Full pipeline: stage not stated [GSEA, Python]

### Seeding of visceral adipose tissue with perinatally generated regulatory T cells shapes the metabolic tenor in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2518203122 | PMCID: PMC12415289 | PMID: 40857317
- Evidence: For pathway and signature analyses, Gene Set Enrichment Analysis (GSEA) was performed with p-value adjustment using the Benjamini–Hochberg method.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [R]

### Protein functional site annotation using local structure embeddings. (PNAS 2025)

- DOI: 10.1073/pnas.2513219122 | PMCID: PMC12403137 | PMID: 40833413
- Evidence: We use the same increment and decrement formulas as in GSEA ( 49 ) to compute S , and the ES is similarly calculated as a weighted Kolmogorov–Smirnov statistic using the maximum deviation of S from zero.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [AlphaFold, BLAST]

### Macrophage TBK1 signaling drives the development and outgrowth of breast cancer brain metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2420793122 | PMCID: PMC12403136 | PMID: 40833415
- Evidence: ...fluorescence and immunohistochemistry, H&E staining, and generation of brain metastasis mouse models), patient samples, bioinformatic analyses (e.g., GSEA, scRNA-seq, and survival analysis of human BCBM samples), and statistical analysis are provided in the SI Appendix , SI Materials and Methods .
- Full pipeline: differential/statistical testing [GSEA]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: Gene Set Enrichment Analysis for ZNF93 KD was done using the GSEA web interface ( 61 , 62 ).
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Evidence: GSEA enrichment plots have been generated using the plot.gsea function from Rseb package [v0.3.2 ( 65 )].
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### Evaluating plant growth-defense trade-offs by modeling the interaction between primary and secondary metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2502160122 | PMCID: PMC12358851 | PMID: 40773226
- Evidence: MapMan-defined pathways ( 59 , 60 ) enriched with differentially regulated genes were calculated using Gene Set Enrichment Analysis ( 61 ) (BH-corrected P -value < 0.05).
- Full pipeline: differential/statistical testing [GSEA]

### Effects of the gut microbiota on placental angiogenesis and intrauterine growth in gnotobiotic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426341122 | PMCID: PMC12318179 | PMID: 40711921
- Evidence: Gene set enrichment analysis (GSEA) of Gene Ontology Biological Processes (GO-BPs) was performed with a focus on the leading edge differentially expressed transcripts ( Materials and Methods ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, lme4] -> stage not stated [QuPath v0.4.4]

### Cell-type-informed genotyping of mosaic focal epilepsies reveals cell-autonomous and non-cell-autonomous disease-associated transcriptional programs. (PNAS 2025)

- DOI: 10.1073/pnas.2509622122 | PMCID: PMC12305027 | PMID: 40674414
- Evidence: Differential gene expression (DGE) and gene set enrichment analyses (GSEA) characterized cell-type-associated changes in transcriptional programs between cases and controls ( SI Appendix , Fig.
- Full pipeline: normalisation [Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [CellChat, fgsea v1.28.0]

### Deletion of p63 exon 13 in mice reveals C-terminal isoform-specific functions in epithelial development. (PNAS 2025)

- DOI: 10.1073/pnas.2503866122 | PMCID: PMC12304987 | PMID: 40674423
- Evidence: Gene set enrichment analysis via Mouse Reactome pathway collection (GSEA mReactome) revealed that the most significantly altered pathways in p63 +/+ cells were associated with translation, whereas genes enriched in p63 Δ13/Δ13 keratinocytes were associated with ECM organization and adhesion ( Fig.
- Full pipeline: stage not stated [GSEA]

### mtKO: A dedicated guide RNA library for mitochondria research. (PNAS 2025)

- DOI: 10.1073/pnas.2502285122 | PMCID: PMC12304920 | PMID: 40674424
- Evidence: ( B ) GSEA on the significantly depleted pathways.
- Full pipeline: stage not stated [GSEA]

### In vivo generation of CAR macrophages via the enucleated mesenchymal stem cell delivery system for glioblastoma therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426724122 | PMCID: PMC12304911 | PMID: 40658861
- Evidence: ( N ) GSEA of the regulation of inflammatory response pathway reveals its relative enrichment in CAR + M compared to control.
- Full pipeline: stage not stated [GSEA]

### CDKN1B (p27/kip1) enhances drug-tolerant persister CTCs by restricting polyploidy following mitotic inhibitors. (PNAS 2025)

- DOI: 10.1073/pnas.2507203122 | PMCID: PMC12280942 | PMID: 40623195
- Evidence: GSEA of genes differentially expressed following DTX treatment in the per pro cells shows strong suppression of proliferation (E2F targets, G2/M checkpoint genes, mTORC1 signaling; BRx-82 FDRs from 4.07 × 10 −29 to 4.76 × 10 −7 ; Brx-142 FDRs from 9.03 × 10 −79 to 2.64 × 10 −14 ; Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### TEAD-targeting small molecules induce a cofactor switch to regulate the Hippo pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2425984122 | PMCID: PMC12260418 | PMID: 40608666
- Evidence: ( I ) Enriched Hallmark gene sets determined by GSEA of RNA-seq from 24-h Compound 2 treatment or WT VGLL4 overexpression.
- Full pipeline: stage not stated [GSEA, HOMER]

### Gelated microvesicle-mediated delivery of mesenchymal stem cell mitochondria for the treatment of myocardial infarction. (PNAS 2025)

- DOI: 10.1073/pnas.2424529122 | PMCID: PMC12260566 | PMID: 40591606
- Evidence: ( D ) Gene set enrichment analysis (GSEA) of target pathways of MI model rats.
- Full pipeline: stage not stated [GSEA, ImageJ]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### Fine structural design of 3βHSD1 inhibitors for prostate cancer therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2422267122 | PMCID: PMC12232669 | PMID: 40560608
- Evidence: Consistently, gene set enrichment analysis (GSEA) showed that HEAL-116 specifically antagonized the biological effect of DHEA ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, GSEA]

### Setdb1 ablation in macrophages attenuates fibrosis in heart allografts. (PNAS 2025)

- DOI: 10.1073/pnas.2424534122 | PMCID: PMC12232555 | PMID: 40553495
- Evidence: Gene set enrichment analysis (GSEA) showed that these macrophages highly expressed genes associated with histone methylation, such as SET domain bifurcated histone lysine methyltransferase 1 (Setdb1), SET domain containing 2 (Setd2) and histone-lysine N-methyltransferase 2 (KMT2) members.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, PyMOL]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles suppress IFNε-mediated responses driven by its intracellular bacterial symbiont &lt;i&gt;Mycoplasma hominis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2508297122 | PMCID: PMC12232435 | PMID: 40560611
- Evidence: GSEA was performed using the BubbleGUM package as previously described ( 91 ).
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [GSEA]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: Differentially expressed genes (log2 Fold change < −0.5 or > 0.5, FDR< 0.05) were further analyzed using GSEA by GSEA software ( 60 ) or KEGG enrichment analysis ( 61 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Bone morphogenetic protein-9 controls pulmonary vascular growth and remodeling. (PNAS 2025)

- DOI: 10.1073/pnas.2410229122 | PMCID: PMC12232436 | PMID: 40549904
- Evidence: ( D ) Gene set enrichment analysis (GSEA) between ALK1 high vs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat, UMAP] -> stage not stated [GSEA]

### Tumor-promoting UBR4 coordinates impaired mitophagy-associated senescence and lung adenocarcinoma pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2425015122 | PMCID: PMC12207436 | PMID: 40531870
- Evidence: To better understand the functional signatures of UBR4 in LUAD, we performed gene set enrichment analysis (GSEA) using hallmark and gene ontology (GO) gene sets.
- Full pipeline: differential/statistical testing [ImageJ] -> stage not stated [GSEA]

### Sp140L functions as a herpesvirus restriction factor suppressing viral transcription and activating interferon-stimulated genes. (PNAS 2025)

- DOI: 10.1073/pnas.2426339122 | PMCID: PMC12207491 | PMID: 40526717
- Evidence: We first pooled all time points for each WT and LPKO scRNAseq dataset into a “pseudobulk” dataset and performed gene set enrichment analysis (GSEA) to identify differentially regulated pathways between WT and LPKO infection.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [AlphaFold]

### Antlers on does: An unexpected role of macrophages in deer biology. (PNAS 2025)

- DOI: 10.1073/pnas.2424448122 | PMCID: PMC12184406 | PMID: 40512783
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: alignment/mapping [DESeq2, HISAT2, StringTie] -> quantification [ImageJ] -> normalisation [ImageJ] -> differential/statistical testing [DESeq2, HISAT2, StringTie] -> stage not stated [GSEA, Seurat]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: The DEG profiles were then used to predict associated Gene Ontology Terms using the Gene Set Enrichment Analysis analysis in the R package clusterProfiler ( 57 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: In addition, RNA-Sequencing (RNA-seq)/gene set enrichment analysis (GSEA) revealed strong similarities between 6137J and the PRN;Cdk12KO lines ( SI Appendix , Fig.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### Reproductive state controls transcription in the murine liver, with implications for breast cancer liver metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2420174122 | PMCID: PMC12184434 | PMID: 40498462
- Evidence: Additional details regarding RNAseq analysis methods STRING & PANTHER, GSEA, ssGSEA, and Regulon analysis, are detailed and a full list of the pathways used in each analysis can be found in SI Appendix , Table S2 .
- Full pipeline: stage not stated [GSEA]

### Ligand-specific regulation of a binary enhancer code dictating cellular senescence. (PNAS 2025)

- DOI: 10.1073/pnas.2506321122 | PMCID: PMC12184664 | PMID: 40493192
- Evidence: ( C ) Gene Set Enrichment Analysis (GSEA) plot of enrichment score ( 45 ) for aforementioned gene set over background dataset of 14,493 genes detectibly expressed in BJ fibroblasts.
- Full pipeline: alignment/mapping [HOMER] -> stage not stated [GSEA, Metascape]

### Feedback regulation between histone lactylation and ALKBH3-mediated glycolysis regulates age-related macular degeneration pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2416046122 | PMCID: PMC12184506 | PMID: 40493193
- Evidence: Both GSEA and GO analyses of the RNA-Seq data revealed the enrichment of glycolysis in fRPE cells overexpressing ALKBH3 compared to control cells ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### A proteomic signature of healthspan. (PNAS 2025)

- DOI: 10.1073/pnas.2414086122 | PMCID: PMC12168021 | PMID: 40478878
- Evidence: Gene Set Enrichment Analysis of Proteins Associated with HPS (Test Sample, n = 12,935).
- Full pipeline: alignment/mapping [FUMA v1.5.2] -> differential/statistical testing [FUMA v1.5.2] -> stage not stated [GSEA, R]

### Light at night negatively affects mood in diurnal primate-like tree shrews via a visual pathway related to the perihabenular nucleus. (PNAS 2025)

- DOI: 10.1073/pnas.2411280122 | PMCID: PMC12167994 | PMID: 40478874
- Evidence: Gene Set Enrichment Analysis.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA]

### Creb5 controls its own expression and directly induces the joint interzone regulatory program. (PNAS 2025)

- DOI: 10.1073/pnas.2501830122 | PMCID: PMC12168028 | PMID: 40472036
- Evidence: Gene Set Enrichment Analysis of the DEGs that were more highly expressed in Creb5+Sox9+ cells relative to Creb5-Sox9+ cells, indicated that these 1,620 DEGs were enriched in Gene Ontology terms that promote cell adhesion or ERK signaling pathways ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### Pathophysiologically relevant bisphenol S exposure accelerates aging by disrupting brown adipose tissue-regulated energy metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2420437122 | PMCID: PMC12167992 | PMID: 40455996
- Evidence: Additionally, GSEA was applied to evaluate differences in biological pathways, with results visualized using the enrichplot package when P < 0.05.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> visualisation [GSEA]

### Disrupted diencephalon development and neuropeptidergic pathways in zebrafish with autism-risk mutations. (PNAS 2025)

- DOI: 10.1073/pnas.2402557122 | PMCID: PMC12167956 | PMID: 40460132
- Evidence: Cellular differences in these lines were predicted using gene set enrichment analysis (GSEA) with published single-cell sequencing data (scRNA-seq) from a similar age and tissue ( 29 ).
- Full pipeline: stage not stated [GSEA]

### Epithelial Regnase-1 inhibits colorectal tumor growth by regulating IL-17 signaling via degradation of <i>NFKBIZ</i> mRNA. (PNAS 2025)

- DOI: 10.1073/pnas.2500820122 | PMCID: PMC12168022 | PMID: 40460118
- Evidence: Gene set enrichment analysis (GSEA) using Mouse MSigDB (M2: CP, Reactome) ( Fig.
- Full pipeline: stage not stated [GSEA]

### Nanoimmunomodulation of the Aβ-STING feedback machinery in microglia for Alzheimer's disease treatment. (PNAS 2025)

- DOI: 10.1073/pnas.2427257122 | PMCID: PMC12146763 | PMID: 40434641
- Evidence: ( A ) GSEA on DNA cytosolic sensing and IFN α/β signaling pathways in the brains of AD patients versus healthy individuals.
- Full pipeline: stage not stated [GSEA]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: ( Q ) Gene set enrichment analysis (GSEA) based on the genes ranked by the relationship with TFF3+MC4 score.
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### BRD9 functions as an HIV-1 latency regulatory factor. (PNAS 2025)

- DOI: 10.1073/pnas.2418467122 | PMCID: PMC12130862 | PMID: 40402245
- Evidence: For example, the chromosome segregation pathway was significantly enriched and we performed Gene Set Enrichment Analysis to illustrate the enrichment.
- Full pipeline: quality control [Bowtie2, FastQC] -> alignment/mapping [Bowtie2, FastQC] -> stage not stated [GSEA]

### Phase separation of RXRγ drives tumor chemoresistance and represents a therapeutic target for small-cell lung cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2421199122 | PMCID: PMC12130815 | PMID: 40392852
- Evidence: Further examination by gene-set enrichment analysis (GSEA) revealed that genes involved in cell junction, stemness, and neuronal function were significantly altered by RXRγ inhibition ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Mutant &lt;i&gt;IDH1&lt;/i&gt; cooperates with &lt;i&gt;NPM1c&lt;/i&gt; or &lt;i&gt;FLT3&lt;/i&gt;&lt;sup&gt;ITD&lt;/sup&gt; to drive distinct myeloid diseases and molecular outcomes. (PNAS 2025)

- DOI: 10.1073/pnas.2415779122 | PMCID: PMC12107087 | PMID: 40377995
- Evidence: By Gene Set Enrichment Analysis (GSEA), the top upregulated pathways in Idh1 R132 ; Npm1c cKit + cells (compared to WT) included gene sets related to the immune system, especially interferon α/γ responses ( Fig.
- Full pipeline: differential/statistical testing [DESeq2, GSVA] -> stage not stated [GSEA]

### Thymic Bmi-1 hampers γδT17 generation and its derived RORγt-IL-17A signaling to delay cardiac aging. (PNAS 2025)

- DOI: 10.1073/pnas.2414717122 | PMCID: PMC12107095 | PMID: 40366697
- Evidence: ( D ) GSEA of PRC2 methylate histones and DNA and Notch signaling pathway.
- Full pipeline: stage not stated [GSEA]

### CaMK modulates sensory neural activity to control longevity and proteostasis. (PNAS 2025)

- DOI: 10.1073/pnas.2423428122 | PMCID: PMC12107105 | PMID: 40359038
- Evidence: S5 A , C , and E ), and gene set enrichment analysis (GSEA) ( SI Appendix, Fig.
- Full pipeline: stage not stated [GSEA]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Evidence: Gene set enrichment analysis (GSEA) comparing each time point with the baseline before vaccination in all APC populations using all expressed genes confirmed the common enrichment of ISGs on days 3 and 7 after vaccination ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### Intercellular contractile force attenuates chemosensitivity through Notch-MVP-mediated nuclear drug export. (PNAS 2025)

- DOI: 10.1073/pnas.2417626122 | PMCID: PMC12088414 | PMID: 40333760
- Evidence: ( B ) GSEA analysis of the RNA-sequencing data of patient samples in the GEO database GSE34138 .
- Full pipeline: stage not stated [GSEA]

### De novo DUOX2 expression in neutrophil subsets shapes the pathogenesis of intestinal disease. (PNAS 2025)

- DOI: 10.1073/pnas.2421747122 | PMCID: PMC12088431 | PMID: 40327691
- Evidence: ( L ) GSEA performed in enrichr on highly enriched proteins in colPMNs (encircled in K ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Understanding TAK1 deficiency in microglia: Dual mechanisms for photoreceptor protection in a mouse model of retinitis pigmentosa. (PNAS 2025)

- DOI: 10.1073/pnas.2423134122 | PMCID: PMC12067235 | PMID: 40314985
- Evidence: ( F ) Gene set enrichment analysis (GSEA) of genes related to “KEGG_PATHWAY_OF_APOPTOSIS.” ( G ) KEGG network analysis of DEGs.
- Full pipeline: stage not stated [GSEA]

### Genomic analysis of progenitors in viral infection implicates glucocorticoids as suppressors of plasmacytoid dendritic cell generation. (PNAS 2025)

- DOI: 10.1073/pnas.2410092122 | PMCID: PMC12067256 | PMID: 40294270
- Evidence: Subsequent gene set enrichment analysis (GSEA) validated these findings by showing that genes that were significantly downregulated in Lin − c-kit int/lo Flt3 + progenitors from infected mice were enriched for the pre-pDC-primed signature ( Fig.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### B cell-derived acetylcholine mitigates skin inflammation in mice through α9 nicotinic acetylcholine receptor-mediated signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2501960122 | PMCID: PMC12054817 | PMID: 40267137
- Evidence: For GSEA, WebGestalt software was used ( www.webgestalt.org ).
- Full pipeline: stage not stated [GSEA, ImageJ]

### MOB1 deletion in murine mature adipocytes ameliorates obesity and diabetes. (PNAS 2025)

- DOI: 10.1073/pnas.2424741122 | PMCID: PMC12054810 | PMID: 40258148
- Evidence: These results were confirmed by GSEA enrichment plotting ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA, ImageJ]

### Semaphorin 6A phase separation sustains a histone lactylation-dependent lactate buildup in pathological angiogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2423677122 | PMCID: PMC12036978 | PMID: 40244673
- Evidence: Gene set enrichment analysis (GSEA) of H3K9la/H3K18la-binding genes showed more significant enrichment in the “protein methylation” pathway in OIR ECs ( Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [GSEA]

### MFRP is a molecular hub that organizes the apical membrane of RPE cells by engaging in interactions with specific proteins and lipids. (PNAS 2025)

- DOI: 10.1073/pnas.2425523122 | PMCID: PMC12036977 | PMID: 40249779
- Evidence: Further characterization of the transcriptomic data through gene-set enrichment analysis (GSEA) revealed that most relevant gene-set-phenotype associations corresponded to two major categories: gene ontology (GO)-term biological processes, or biological pathways.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### SNX10 deficiency impairs sensitivity to anti-HER2 antibody-drug conjugates via altering HER2 trafficking in HER2-positive breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2417586122 | PMCID: PMC12037019 | PMID: 40228127
- Evidence: ( F – I ) GSEA enrichment plot of vesicle-related GO pathways and GO pathway enrichment of the differentially expressed genes (DEGs) in PDOs ( F and G ) and in the T-DM1/P subgroup in the I-SPY2 clinical trial ( H and I ).
- Full pipeline: differential/statistical testing [GSEA] -> visualisation [GSVA]

### FAO-fueled OXPHOS and NRF2-mediated stress resilience in MICs drive lymph node metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2411241122 | PMCID: PMC12012528 | PMID: 40215279
- Evidence: ( A ) GSEA plots illustrating upregulation of the OXPHOS pathway in MIC cluster.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [UMAP]

### Perturbing nuclear glycosylation in the mouse preimplantation embryo slows down embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2410520122 | PMCID: PMC12012502 | PMID: 40203037
- Evidence: ( D ) GSEA of gene expression changes in E7 epiblasts derived from Btgh-injected embryos vs. dBtgh-injected controls.
- Full pipeline: read trimming [STAR v2.7.8a] -> alignment/mapping [STAR v2.7.8a] -> normalisation [DESeq2, deepTools v3.0.2] -> stage not stated [GSEA, ImageJ, featureCounts]

### Inactivation of microglial LXRβ in early postnatal mice impairs microglia homeostasis and causes long-lasting cognitive dysfunction. (PNAS 2025)

- DOI: 10.1073/pnas.2410698122 | PMCID: PMC12012545 | PMID: 40208947
- Evidence: ( N and O ) GSEA revealed that deletion of LXRβ in microglia positively regulated the phagocytosis gene set, such as the regulation of phagocytosis ( N ) and phagocytic vesicle membrane ( O ).
- Full pipeline: stage not stated [GSEA]

### The Hippo pathway and p27&lt;sup&gt;Kip1&lt;/sup&gt; cooperate to suppress mitotic regeneration in the organ of Corti and the retina. (PNAS 2025)

- DOI: 10.1073/pnas.2411313122 | PMCID: PMC12002246 | PMID: 40178894
- Evidence: ( D ) The heatmap generated with GSEA demonstrates the relative expression levels of positive regulators of cell cycle (GO:0045787) differentially expressed after LKI treatment (|Log(FoldChange)| > 1.5; FDR < 0.05; N = 3 samples for each condition).
- Full pipeline: differential/statistical testing [GSEA]

### DDX54 downregulation enhances anti-PD1 therapy in immune-desert lung tumors with high tumor mutational burden. (PNAS 2025)

- DOI: 10.1073/pnas.2412310122 | PMCID: PMC12002276 | PMID: 40172969
- Evidence: By gene set enrichment analysis (GSEA), we found that immune-desert samples with TMB-H are associated with multiple immune suppressive pathways and signatures such as WNT3A and MYC pathway, epithelial–mesenchymal transition (EMT), and cancer-associate stemness ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Therapeutic targeting of the NOTCH1 and neddylation pathways in T cell acute lymphoblastic leukemia. (PNAS 2025)

- DOI: 10.1073/pnas.2426742122 | PMCID: PMC12002235 | PMID: 40163723
- Evidence: ( J ) GSEA of the top differentially expressed genes in CompE-treated LS174T cells in ( F ) vs. top 300 upregulated genes in DBZ-treated Lgr5-EGFP High mouse intestinal stem cells in ( I ).
- Full pipeline: differential/statistical testing [GSEA]

### Signaling networks in cancer stromal senescent cells establish malignant microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2412818122 | PMCID: PMC12002233 | PMID: 40168129
- Evidence: Gene ontology (GO) and gene set enrichment analysis (GSEA) revealed up-regulation of Th17 activation, SHH, and TNF-α signaling pathways ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### ETV5 reduces androgen receptor expression and induces neural stem-like properties during neuroendocrine prostate cancer development. (PNAS 2025)

- DOI: 10.1073/pnas.2420313122 | PMCID: PMC11962414 | PMID: 40117308
- Evidence: ( E ) GSEA of NEPC signatures in ETV5 -high 10% and ETV5 -low 10% samples from public datasets, including MSK 2014, SU2C/PCF 2015, SU2C/PCF 2019, and FHCRC 2016.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Version used: **4.0.3**
- Evidence: GSEA (version 4.0.3) was performed as previously described ( 72 ).
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### Dual mRNA nanoparticles strategy for enhanced pancreatic cancer treatment and β-elemene combination therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2418306122 | PMCID: PMC11929461 | PMID: 40067898
- Evidence: In addition, the transcriptome was interrogated for immune signatures through gene set enrichment analysis (GSEA), and pathways associated with the antigen processing and presentation, humoral immune response, and response to interferon-gamma emerged as significantly enriched in the contrast NVs mRNA@LNPs + anti-PD-1 mRNA@LPNPs versus empty NPs group ( Fig.
- Full pipeline: stage not stated [GSEA, GSVA]

### Cell type and region-specific transcriptional changes in the endometrium of women with RIF identify potential treatment targets. (PNAS 2025)

- DOI: 10.1073/pnas.2421254122 | PMCID: PMC11929460 | PMID: 40063812
- Evidence: Altered pathways and gene ontology (GO) biological processes were identified with Gene Set Enrichment Analysis (GSEA) using either GO biological process annotations or KEGG pathways ( 33 , 34 ), implemented in clusterProfiler (v 4.10.1) ( 35 ) using a minimum and maximum gene set size of 10 and 500, respectively.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.1] -> differential/statistical testing [lme4 v1.1] -> stage not stated [R, Seurat v5.0.3]

### The NAE1-mediated neddylation operates as an essential post-translational modification checkpoint for effector CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424061122 | PMCID: PMC11912420 | PMID: 40030035
- Evidence: GSEA was done on GSEA desktop software v4.3.3 on classic preranked mode.
- Full pipeline: read trimming [HISAT2, SAMtools, Trim Galore v0.6.10] -> alignment/mapping [HISAT2, SAMtools, Trim Galore v0.6.10] -> stage not stated [DESeq2, GSEA, pheatmap]

### Erythroid progenitor cell-mediated spleen-tumor interaction deteriorates cancer immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2417473122 | PMCID: PMC11892600 | PMID: 40014568
- Evidence: We used a human gene set (Descartes fetal spleen erythroblasts) from the gene set enrichment analysis (GSEA) database ( 28 ) and selected the erythrocyte-related genes, enriched in intratumoral CD45 + EPCs, as EPC signatures (including EPOR , TFRC , GYPA , HMBS , IL1RL1 , LONRF3 , MINPP1 , PCLAF , PPM1H , SLC25A15 , and SLC29A1 ).
- Full pipeline: stage not stated [GSEA]

### Identification of AK4 and RHOC as potential oncogenes addicted by adult T cell leukemia. (PNAS 2025)

- DOI: 10.1073/pnas.2416412122 | PMCID: PMC11874535 | PMID: 39982744
- Evidence: Gene set enrichment analysis (GSEA) indicates that AK4 and RHOC are both deeply implicated in the activation of key pathways including MYC targets, oxidative phosphorylation, mTORC1 signaling, and fatty acid metabolism ( Fig.
- Full pipeline: stage not stated [GSEA]

### Metabolomic insights into pathogenesis and therapeutic potential in adult acute lymphoblastic leukemia. (PNAS 2025)

- DOI: 10.1073/pnas.2423169122 | PMCID: PMC11848409 | PMID: 39946534
- Evidence: Besides, pathway enrichment analysis of the poorer prognosis BC3 group revealed upregulated metabolic reprogramming, consistent with the GSEA results ( SI Appendix, Fig.
- Full pipeline: stage not stated [GSEA, GSVA]

### Osteocyte connexin hemichannels and prostaglandin E&lt;sub&gt;2&lt;/sub&gt; release dictate bone marrow mesenchymal stromal cell commitment. (PNAS 2025)

- DOI: 10.1073/pnas.2412144122 | PMCID: PMC11848350 | PMID: 39937859
- Evidence: ( D ) Featured changed pathways generated by GSEA.
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [Monocle, UMAP] -> stage not stated [GSEA]

### Clear cell renal carcinoma essentially requires CDKL3 for oncogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2415244122 | PMCID: PMC11848426 | PMID: 39937856
- Evidence: In-depth Gene Set Enrichment Analysis (GSEA) further revealed that CDKL3 expression has significantly positive correlation with the activation of PI3K-Akt-mTOR signaling cascade ( Fig.
- Full pipeline: stage not stated [GSEA]

### Identification of FSH-regulated and estrous stage-specific transcriptional networks in mouse ovaries. (PNAS 2025)

- DOI: 10.1073/pnas.2411977122 | PMCID: PMC11848299 | PMID: 39928863
- Evidence: Pathway analysis was performed using GSEA ( 16 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Extrinsic induction of apoptosis and tumor suppression via the p53-Reprimo-Hippo-YAP/TAZ-p73 pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2413126122 | PMCID: PMC11831151 | PMID: 39913207
- Evidence: GSEA plots revealed that genes upregulated by TNF-α were also upregulated in rReprimo-treated HeLa cells ( Fig.
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, HISAT2 v2.1.0] -> stage not stated [GSEA]

### Uterine organoids reveal insights into epithelial specification and plasticity in development and disease. (PNAS 2025)

- DOI: 10.1073/pnas.2422694122 | PMCID: PMC11804710 | PMID: 39883834
- Evidence: To gain insights into how the mesenchyme regulates epithelial cell differentiation, we performed gene set enrichment analysis (GSEA) using integrated scRNA-seq datasets encompassing PNDs 1, 3, and 5 mesenchyme or epithelium ( 27 , 35 ) ( GSE229790 , PRJNA1046685) ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [CellChat, GSEA]

### CBX2 suppresses interferon signaling to diminish tumor immunogenicity via a noncanonical corepressor complex. (PNAS 2025)

- DOI: 10.1073/pnas.2417529122 | PMCID: PMC11804501 | PMID: 39883845
- Evidence: Consistent with our observations in the mouse models, Gene Set Enrichment Analysis (GSEA) of Gene Ontology (GO) terms applied to transcriptional data from skin cutaneous melanoma (SKCM) patient samples in The Cancer Genome Atlas (TCGA) also reveal that antitumor immune signaling pathways, such as T cell-mediated cytotoxicity and antigen presentation, are enriched in the CBX2 low expression group (...
- Full pipeline: stage not stated [GSEA]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Evidence: GSEAs were performed using GSEA software ( 62 ).
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### Complement C3 of tumor-derived extracellular vesicles promotes metastasis of RCC via recruitment of immunosuppressive myeloid cells. (PNAS 2025)

- DOI: 10.1073/pnas.2420005122 | PMCID: PMC11789090 | PMID: 39847320
- Evidence: Additionally, we performed gene set enrichment analysis (GSEA) of upregulated pathways within ACHN EVs, which uncovered the complement cascade and other pathways involved in EV-mediated premetastatic niches formation ( SI Appendix, Fig.
- Full pipeline: stage not stated [GSEA]

### ADARp110 promotes hepatocellular carcinoma progression via stabilization of CD24 mRNA. (PNAS 2025)

- DOI: 10.1073/pnas.2409724122 | PMCID: PMC11761664 | PMID: 39808660
- Evidence: To explore other possible mechanisms promoting HCC progression, we performed Gene Set Enrichment Analysis (GSEA) using transcriptional data and noticed a marked downregulation of reactivate oxygen species pathway signature concurrent with both ADAR and CD24 expression ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### The cGAS-STING, p38 MAPK, and p53 pathways link genome instability to accelerated cellular senescence in ATM-deficient murine lung fibroblasts. (PNAS 2025)

- DOI: 10.1073/pnas.2419196122 | PMCID: PMC11745328 | PMID: 39772747
- Evidence: ( A ) GSEA plots for hallmark interferon gene sets when global gene expression was compared between Atm −/− and WT cells at P2 ( Upper ) and P8 ( Lower ).
- Full pipeline: stage not stated [GSEA]

### PKM2 controls cochlear development through lactate-dependent transcriptional regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2410829122 | PMCID: PMC11745320 | PMID: 39773029
- Evidence: Gene set enrichment analysis (GSEA) revealed that canonical glycolysis accompanied by the NADH regeneration process was strongly enriched in the organoid group, while genes related to the mitochondrial respiratory chain complex were strongly downregulated ( Fig.
- Full pipeline: stage not stated [GSEA]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: Genes were ranked based on fold change from the DESeq2 analysis, and these rankings were applied in GSEA using the classic statistical approach.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### <i>Salmonella</i> infection accelerates postnatal maturation of the intestinal epithelium. (PNAS 2025)

- DOI: 10.1073/pnas.2403344122 | PMCID: PMC11725846 | PMID: 39793046
- Evidence: Further details about the generation and bioinformatic analysis of these samples, including the generation of PCA plots and gene set enrichment analysis (GSEA), are provided in SI Appendix , Materials and Methods .
- Full pipeline: dimensionality reduction/clustering [GSEA] -> differential/statistical testing [DESeq2]

### ANAC044 orchestrates mitochondrial stress signaling to trigger iron-induced stem cell death in root meristems. (PNAS 2025)

- DOI: 10.1073/pnas.2411579122 | PMCID: PMC11725852 | PMID: 39793035
- Evidence: To test high Fe and GSNOR -dependent gene enrichment in an orthogonal manner, we conducted a Gene Set Enrichment Analysis (GSEA) using all genes.
- Full pipeline: alignment/mapping [HTSeq v0.6.0, R v2.6.1, STAR v2.6.1] -> quantification [HTSeq v0.6.0, R v2.6.1, STAR v2.6.1] -> stage not stated [GSEA]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Evidence: ( F ) Gene Set Enrichment Analysis plots of selected autophagy gene sets (core autophagy genes) that are differentially expressed in Resistant (SHP099 28 d) vs Sensitive (SHP099 5 d) NP mutant MPNST allografts (n = 3 replicates per condition, * P <0.01, FDR q = 0.06, NES = 1.33) and ( G ) Resistant (SHP099 28 d) versus Sensitive (SHP099 5 d) NF1-MPNST PDX#2 samples (n = 3 replicates per condition,...
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### Oncogenic IDH1<sup>mut</sup> drives robust loss of histone acetylation and increases chromatin heterogeneity. (PNAS 2025)

- DOI: 10.1073/pnas.2403862122 | PMCID: PMC11725805 | PMID: 39793065
- Evidence: ( B ) Gene set enrichment analysis (GSEA) of expression differences between control and mutant-IDH1 expressing cells (7d).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Collagen-producing eye cell atlas reveals distinct fibroblast fates in early injury vs. fibrotic subretinal disease. (PNAS 2026)

- DOI: 10.1073/pnas.2519056123 | PMCID: PMC13320955 | PMID: 42361041
- Evidence: GSEA was performed via gseapy (GO_Biological_Process_2021) and GSEA Preranked software.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Scanpy v1.9.6]

### Fasting primes small intestinal regeneration after damage via a microbiome-metabolite-chromatin axis. (PNAS 2026)

- DOI: 10.1073/pnas.2529215123 | PMCID: PMC13320697 | PMID: 42335240
- Evidence: ( D ) Top 10 MSigDB GSEA pathways based on H3K27ac proximal promoter peaks overlapping with publicly available HiChIP and inhouse ChIP seq data in Fast (−Tetra) condition.
- Full pipeline: dimensionality reduction/clustering [MACS2 v2.2.9.1, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ArchR v1.0.2, GSEA, HOMER, R v1.0.2]

### APOBEC2 deficiency disrupts hematopoietic lineage commitment, resulting in emergence of dual identity lymphocytes in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2531122123 | PMCID: PMC13250534 | PMID: 42247564
- Evidence: Pathway enrichment analysis (PEA) and gene set enrichment analysis (GSEA) further revealed an enrichment of B cell identity programs and antigen presentation pathways within these A2 −/− derived T cell populations ( SI Appendix , Fig.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, scDblFinder]

### mRNA-laden LNP-enabled in situ CAR-macrophage alleviates liver fibrosis via inhibiting activated HSCs and modulating the immune microenvironment. (PNAS 2026)

- DOI: 10.1073/pnas.2534673123 | PMCID: PMC13229182 | PMID: 42213756
- Evidence: Compared with the Fibrosis group, the LNP group promoted proliferation-related biological processes in Heps, as indicated by GSEA of GO terms ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Genome-wide association mapping and targeted loss of function studies identify &lt;i&gt;Shroom3&lt;/i&gt; as a driver of hyperpolyploidy and ventricular dilation. (PNAS 2026)

- DOI: 10.1073/pnas.2522068123 | PMCID: PMC13229193 | PMID: 42189988
- Evidence: Gene clusters are annotated with enriched terms from DAVID ( I ) Top 10 terms from gene set enrichment analysis (GSEA) with biased expression in Shroom3 1073S (red) or Shroom3 1073G (blue).
- Full pipeline: alignment/mapping [GEMMA] -> normalisation [clusterProfiler] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ]

### Epstein-Barr virus (EBV) infection causes human germinal center B cell-derived lymphomas in the absence of EBNA2 expression. (PNAS 2026)

- DOI: 10.1073/pnas.2525164123 | PMCID: PMC13229203 | PMID: 42189985
- Evidence: Interestingly, GSEA of the RNA-seq results suggested that LMP2A-high tumors have signatures consistent with increased expression of genes not normally expressed in B cells.
- Full pipeline: stage not stated [GSEA]

### Light-controlled disruption of cancer cell dormancy via photoswitchable stress hormone receptor degraders. (PNAS 2026)

- DOI: 10.1073/pnas.2528760123 | PMCID: PMC13214037 | PMID: 42166243
- Evidence: ( G ) Gene Set Enrichment Analysis (GSEA) using Hallmark gene sets from MSigDB, highlighting transcriptional differences between E- isomer + DEX and Z- isomer + DEX treatments.
- Full pipeline: quantification [R] -> normalisation [edgeR] -> differential/statistical testing [R] -> stage not stated [GSEA]

### Spatially tunable multiomic sequencing using light-driven combinatorial barcoding of molecules in tissues. (PNAS 2026)

- DOI: 10.1073/pnas.2527896123 | PMCID: PMC13214022 | PMID: 42150070
- Evidence: ( D ) Gene Set Enrichment Analysis.
- Full pipeline: stage not stated [GSEA]

### NAT10/ac&lt;sup&gt;4&lt;/sup&gt;C drives intrahepatic cholangiocarcinoma by suppressing transposable elements via chromatin remodeling. (PNAS 2026)

- DOI: 10.1073/pnas.2532263123 | PMCID: PMC13187814 | PMID: 42133812
- Evidence: ( G ) Gene sets enrichment analysis (GSEA) of innate immune related hallmarks in si- CHAF1A vs. si-Ctrl cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, GSEA]

### ATP2B1 expression identifies human hematopoietic stem cells with superior repopulation and self-renewal. (PNAS 2026)

- DOI: 10.1073/pnas.2604380123 | PMCID: PMC13167729 | PMID: 42085155
- Evidence: ( C ) GSEA results depicting enrichment of stem cell signatures across CD49f + ATP2B1 + , CD49f + ATP2B1 – and CD49f – ATP2B1 – HSC.
- Full pipeline: stage not stated [GSEA, HOMER, ImageJ]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Evidence: Spearman correlation coefficients between FOSL2 (FRA2) expression and all detected genes across the cohort was computed and the ranked correlation list was used as input for Gene Set Enrichment Analysis (GSEA) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### Suppression rather than activation of the integrated stress response (GCN2-ATF4) pathway extends lifespan in the fly. (PNAS 2026)

- DOI: 10.1073/pnas.2518812123 | PMCID: PMC13142962 | PMID: 42048457
- Evidence: Gene set enrichment analysis (GSEA; 116 ) was performed to identify biological pathways and processes associated with the differential gene expression profile.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [GSEA, edgeR] -> stage not stated [R, minimap2 v2.24]

### Type I interferons induced upon respiratory viral infection impair lung metastatic initiation. (PNAS 2026)

- DOI: 10.1073/pnas.2412919123 | PMCID: PMC13099621 | PMID: 41996163
- Evidence: Consistent with this finding, GSEA analysis indicated that cancer cells in IFN-α pre-exposed lungs display a reduction in pathways linked to cell cycle and DNA replication, ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, GSEA]

### FABP7 controls radial glial scaffold stability during human cortical development. (PNAS 2026)

- DOI: 10.1073/pnas.2523130123 | PMCID: PMC13099611 | PMID: 41984827
- Evidence: GSEA of RG-specific DEGs further confirmed enrichment of neurodevelopmental diseases such as ASD ( SI Appendix , Table S6 ), ID, and epileptic encephalopathy, whereas psychiatric disorders such as depression showed no significant association ( SI Appendix , Fig.
- Full pipeline: normalisation [Seurat v4.4.0, edgeR v3.40.2] -> dimensionality reduction/clustering [Seurat v4.4.0, UMAP, edgeR v3.40.2] -> differential/statistical testing [Seurat v4.4.0, edgeR v3.40.2] -> visualisation [UMAP] -> stage not stated [GSEA, WGCNA]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Evidence: GSEA enrichment plots of EMT-related pathways.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### Use of a cytochrome P450 humanized mouse model to refine schistosomiasis drug discovery. (PNAS 2026)

- DOI: 10.1073/pnas.2600197123 | PMCID: PMC13079396 | PMID: 41961851
- Evidence: Gene set enrichment analyses (GSEA) revealed a top 20 list of shared Gene Ontology (GO) Biological Processes (BP) and Molecular Function (MF) terms that were significantly over-represented upon infection ( q < 0.05) in both 8HUM and WT mice ( Fig.
- Full pipeline: stage not stated [GSEA]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: ( D ) GSEA plots of promoter and enhancer EWS-FLI1 10xGGAA signatures in transcriptomes from STAG2 knockdown, STAG2 knockout, and EWS-FLI1 knockdown conditions compared with their respective controls (n = 2 biological replicates, GSEA enrichment test).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### Fibro-adipogenic progenitor cells from murine SMA muscles are intrinsically adipogenic. (PNAS 2026)

- DOI: 10.1073/pnas.2525423123 | PMCID: PMC13037897 | PMID: 41886383
- Evidence: Volcano plots, heatmaps, and GSEA edgeplots were generated using R packages.
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ, fastp]

### PHGDH phosphorylation mediated by WNK1 serves as a dual marker of metabolic vulnerability and responsiveness to oxaliplatin treatment. (PNAS 2026)

- DOI: 10.1073/pnas.2525213123 | PMCID: PMC13037954 | PMID: 41880577
- Evidence: Consistently, Gene Set Enrichment Analysis (GSEA) demonstrated a significant enrichment of serine metabolism–related gene signatures in gastric cancer tissues compared with normal controls ( SI Appendix , Fig.
- Full pipeline: stage not stated [GSEA]

### GFAP&lt;sup&gt;+&lt;/sup&gt; FOXF2&lt;sup&gt;+&lt;/sup&gt; ependymal cells promote blood-brain barrier repair via DLL4-NOTCH signaling after neural injury. (PNAS 2026)

- DOI: 10.1073/pnas.2520352123 | PMCID: PMC13037844 | PMID: 41875155
- Evidence: ( K ) GSEA enrichment analysis identifying core genes that regulate angiogenesis pathways in cluster 7 (C7).
- Full pipeline: dimensionality reduction/clustering [GSEA, Seurat, UMAP] -> visualisation [Seurat, UMAP]

### KLF2 overrides the resident memory CD8 T cell differentiation program, in opposition to KLF3. (PNAS 2026)

- DOI: 10.1073/pnas.2533700123 | PMCID: PMC13037849 | PMID: 41871244
- Evidence: ( C and D ) shows the result of GSEA, in which genes that were differentially expressed in the Klf2 -Cr vs.
- Full pipeline: quality control [FastQC v0.12.1, featureCounts v2.0.6] -> read trimming [FastQC v0.12.1, featureCounts v2.0.6] -> alignment/mapping [FastQC v0.12.1, featureCounts v2.0.6] -> differential/statistical testing [GSEA] -> stage not stated [HOMER v4.9.1, deepTools v3.3.0]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Evidence: GSEA.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Evidence: ( L ) GSEA of cellular senescence-related pathways following H327ac knockdown.
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### Reactivation of the silenced &lt;i&gt;BASP1&lt;/i&gt; gene suppresses oncogenic WNT signaling in human colorectal cancer cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524159123 | PMCID: PMC12974518 | PMID: 41785318
- Evidence: Gene set enrichment analysis (GSEA) also showed downregulation of multiple genes associated with WNT signaling in SW480-gRNA-B-all ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R, ggplot2] -> visualisation [R, ggplot2] -> stage not stated [GSEA]

### Phenotypic CRISPR screens identify NLRX1 as an essential activator of the human mitochondrial permeability transition. (PNAS 2026)

- DOI: 10.1073/pnas.2535298123 | PMCID: PMC12956895 | PMID: 41739553
- Evidence: We evaluated the positive RRA hits by Gene Set Enrichment Analysis (GSEA) using the Comprehensive Resource of Mammalian Protein Complexes (CORUM; Protein Complexes), Gene Ontology (GO) Biological Processes, the Kyoto Encyclopedia of Genes and Genomes (KEGG), and the Reactome ( 111 ).
- Full pipeline: stage not stated [ANTs, GSEA, ImageJ]

### Differential disease tolerance mediates sex-biased illness severity in sepsis. (PNAS 2026)

- DOI: 10.1073/pnas.2522764123 | PMCID: PMC12956862 | PMID: 41734079
- Evidence: KEGG pathway enrichment analysis was conducted using cluterProfiler (v4.16.0), and GSEA was conducted using fgsea (v1.34.0).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [GSEA, MACS2, R v4.5.0, fgsea v1.34.0]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: GO and GSEA.
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Gene Set Enrichment Analysis (GSEA) of significantly downregulated genes following Mertk inhibitor treatment revealed significant enrichment in pathways related to ECM organization, and cytokine signaling, while the upregulated genes were enriched in pathways associated with neuronal systems and GPCR signaling ( Fig.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Lack of synergy between AR-targeted therapies and PARP inhibitors in homologous recombination-proficient prostate cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2515790122 | PMCID: PMC12867744 | PMID: 41591905
- Evidence: GSEA of this gene sets did not reveal any specific pathway enriched in this cluster of genes.
- Full pipeline: quality control [Cufflinks, DESeq2, STAR] -> alignment/mapping [Cufflinks, DESeq2, STAR] -> quantification [CellProfiler, Cufflinks, DESeq2, STAR] -> normalisation [Cufflinks, DESeq2, STAR] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [Cufflinks, DESeq2, STAR]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Evidence: In human iNs, gene set enrichment analysis (GSEA) identified hypoxia response as the most strongly activated pathway ( Fig.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### Circular RNA-based therapy targeting metabolic vulnerability of fatty acid synthesis overcomes castration-resistant prostate cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2504904123 | PMCID: PMC12773704 | PMID: 41468427
- Evidence: Moreover, gene set enrichment analysis (GSEA) showed that gene sets were cell-cycle related, concordant with its inhibition of cell proliferation ( SI Appendix, Fig.
- Full pipeline: stage not stated [GSEA]

### Ebola virus matrix protein VP40 triggers inflammatory responses linked to the ebolavirus virulence. (PNAS 2026)

- DOI: 10.1073/pnas.2508194123 | PMCID: PMC12773709 | PMID: 41461033
- Evidence: Gene set enrichment analysis (GSEA) utilizing the Hallmark gene sets demonstrated pathways related to inflammation, such as TNFα Signaling via NFκB, were enriched in both EBOV and RESTV infections, however a greater number of genes were enriched in response to EBOV infection ( Fig.
- Full pipeline: stage not stated [GSEA]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: B cell activation scoring Gene Ontology B Cell Activation gene list was downloaded from Gene Set Enrichment Analysis website ( http://www.gsea-msigdb.org/gsea/msigdb/genesets.jsp ).
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Evidence: Gene Ontology analysis plots were generated with the R package “clusterProfiler.” To generate gene sets for GSEA, we selected the top 200 genes up-regulated in Ly49 + CD8 + T cells compared with Ly49 – CD8 + T cells in EAE mice ( 7 ) and the previously reported CD4 + T reg signature genes identified in mice ( 17 ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Evidence: Gene Set Enrichment Analysis (GSEA) GSEA pre-ranked analysis was performed using DEGs between Vγ2/3/4 CD103 + (positive values) and CD103 neg (negative values) with several published datasets ( Fig.
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### MEG3 activates necroptosis in human neuron xenografts modeling Alzheimer's disease. (Science 2023)

- DOI: 10.1126/science.abp9556 | PMCID: PMC7615236 | PMID: 37708272
- Evidence: We found a prominent enrichment using GSEA (gene set enrichment analysis) between previously published AD datasets ( table S3 ), including the ROSMAP (Religious Orders Study and Rush Memory and Aging Project) cohort ( 20 ), and our data in transplanted neurons at 6 and 18 months after transplantation [adjusted P value ( P adj ) < 0.05] but not at 2 months ( fig.
- Full pipeline: differential/statistical testing [GSEA]

### Epigenetic plasticity cooperates with cell-cell interactions to direct pancreatic tumorigenesis. (Science 2023)

- DOI: 10.1126/science.add5327 | PMCID: PMC10316746 | PMID: 37167403
- Evidence: To expose potential unifying features of distinct plastic cell-states, we used gene set enrichment analysis (GSEA) ( 48 ) to identify gene signatures within populations displaying high plasticity scores ( Table S4 ).
- Full pipeline: quality control [ArchR] -> normalisation [ArchR] -> visualisation [Python] -> stage not stated [GSEA]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: GSEA was conducted with the fgsea package, by projecting the ranking of fold-change in expression onto the Hallmark gene sets ( 71 ).
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Specific tRNAs promote mRNA decay by recruiting the CCR4-NOT complex to translating ribosomes. (Science 2024)

- DOI: 10.1126/science.adq8587 | PMCID: PMC11583848 | PMID: 39571015
- Evidence: Gene set enrichment analysis (GSEA) ( 35 ) of mRNA decay rate data from HEK293T and Jurkat cells, as well as steady-state mRNA levels from Cnot3 knockout pro-B cells, revealed that genesets containing mitochondrial ribosomal proteins were highly upregulated upon CNOT3 depletion and were the only significantly upregulated genesets detected in all three datasets ( Fig.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [GSEA, RELION v4.0]

### The transcription factor ZEB2 drives the formation of age-associated B cells. (Science 2024)

- DOI: 10.1126/science.adf8531 | PMCID: PMC7616037 | PMID: 38271512
- Evidence: Gene set enrichment analysis (GSEA) revealed that Zeb2 -deficient B cells lacked expression of the “ABC upregulated” gene set while it was enriched in the “ABC downregulated” gene set from the public dataset GSE99480 ( 8 ) ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: GSEA analysis and corresponding heatmaps and figures were created using R package fgsea (vfgsea_1.24.0), ComplexHeatmap, and ggplot2 for signatures from MSigDB’s hallmark MTORC1 and custom AR signatures based on our data ( 53 – 55 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: Gene set enrichment analysis (GSEA) revealed that gene ontology terms related to spermatogenesis were deregulated in these mutants ( Fig.
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Distinct myeloid-derived suppressor cell populations in human glioblastoma. (Science 2025)

- DOI: 10.1126/science.abm5214 | PMCID: PMC12836367 | PMID: 39818911
- Evidence: IDH-WT glioblastoma MDSCs exhibit robust catabolic and anabolic metabolism Given the substantial shifts in pseudotemporal expression of genes associated with metabolic pathways as cells transition between different myeloid cellular states, we performed gene set enrichment analysis (GSEA) to further characterize pathways representative of functional states of the MDSC populations.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R, SCENIC, velocyto]

### Microglia Rank signaling regulates GnRH neuronal function and the hypothalamic-pituitary-gonadal axis. (Science 2026)

- DOI: 10.1126/science.aeb6999 | PMCID: PMC7619046 | PMID: 41818388
- Evidence: Gene Set Enrichment Analysis Gene Set Enrichment Analysis (GSEA) was used to interpret gene expression data through GSEA Preranked ( 103 ) on a preranked gene list sorted according to log2FC resulting from previous DEA.
- Full pipeline: quality control [FastQC, STAR v2.7.1] -> alignment/mapping [FastQC, GATK, STAR v2.7.1] -> normalisation [FastQC, STAR v2.7.1] -> dimensionality reduction/clustering [FastQC, ImageJ, STAR v2.7.1, UMAP] -> stage not stated [GSEA, Seurat]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: Geneset enrichment analysis (GSEA) was conducted with the fgsea package in R.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: To investigate whether genes associated with memory domains showed coordinated transcriptional changes upon rechallenge, we performed GSEA ( 93 ) using bulk RNA-seq data from Y1 PIMQ + TPA versus Y1 naïve + TPA conditions.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Overcoming T cell tolerance to tumor self-antigens through catch-bond engineering. (Science 2026)

- DOI: 10.1126/science.adx3162 | PMCID: PMC13004167 | PMID: 41855322
- Evidence: Comparisons of the differences of upregulated pathways using Gene Set Enrichment Analysis (GSEA) revealed the upregulation of genes involved in cell cycle, i.e., G2M checkpoint and E2F targets, in the TCR catch bond-engineered TILs compared to TILs with the wild-type TCR ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Evidence: Ribo-seq data was generated in CD34 + CD45RA − CD90 + human HSCs, as previously reported ( 36 ); raw counts of ribosome protected fragments (RPFs) were normalized to transcript length, and the mean log-normalized RPKM (reads per kilobase per million mapped reads) across three replicates was ranked, followed by GSEA using the fGSEA package.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

