# Enrichr

- **Category:** genomics
- **Papers in survey:** 110
- **Journals:** Nature (51), PNAS (48), Cell (8), Science (3)
- **Years:** 2021 (5), 2022 (18), 2023 (22), 2024 (27), 2025 (26), 2026 (12)
- **Versions named:** 2.1 (1)
- **Pipeline stages it appears in:** differential/statistical testing (20), dimensionality reduction/clustering (9), visualisation (3), normalisation (2), quantification (1)

## Papers

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: Comparison of different RNA-seq data KEGG and Encode TF analyses was performed using Enrichr ( Kuleshov et al., 2016 ).
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: To look for classes of functional behaviors among strong and weak perturbations, we used the gseapy implementation of the Enrichr algorithm to compute gene set enrichment p -values within the KEGG2021 pathway gene set (with the set of all targeted genes in the experiment as the background list).
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: 2019 ) https://github.com/saeyslab/nichenetr Enrichr ( Kuleshov et al., 2016 ) http://amp.pharm.mssm.edu/Enrichr/ FlowJo v10.6.1 FlowJo https://www.flowjo.com GeneOntology ( Ashburner et al., 2000 ) http://geneontology.org/ GraphPad Prism 9 GraphPad https://www.graphpad.com/ Harmony ( Korsunsky et al., 2019 ) https://www.github.com/immunogenomics/harmony Ilastik ( Berg et al., 2019 ) https://www.i...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Gene set enrichment analysis (GSEA) Enrichment of Gene ontology (GO) terms for biological processes were analysed using GProfiler 109 and Enrichr.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: Gene ontology and KEGG pathway analyses Gene ontology and KEGG pathways that are enriched within a group of genes were identified with the Enrichr tool (maayanlab.cloud/Enrichr/).
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 41 http://bioconductor.org/packages/release/bioc/html/edgeR.html Enrichr Kuleshov et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Pan-cancer proteogenomics characterization of tumor immunity. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.027 | PMCID: PMC10988632 | PMID: 38359819
- Evidence: Each cluster was submitted to Enrichr 126 and the most relevant enriched term was used to label the cluster.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, Enrichr] -> differential/statistical testing [GSVA, SciPy] -> machine learning [R] -> visualisation [GSVA] -> stage not stated [Cellpose, scikit-image]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: For GO term and pathway enrichment, we queried multiple databases available through the Enrichr platform ( https://maayanlab.cloud/Enrichr/#libraries ), including GO_Molecular_Function_2023, GO_Biological_Process_2023, GO_Cellular_Component_2023, WikiPathway_2023_Human, KEGG_2021_Human, and Reactome_2022.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: Gene Ontology enrichment We perform Gene Ontology enrichment analysis using the R package Enrichr (RRID:SCR_001575) 83 .
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### Post-translational control of beige fat biogenesis by PRDM16 stabilization. (Nature 2022)

- DOI: 10.1038/s41586-022-05067-4 | PMCID: PMC9433319 | PMID: 35978186
- Evidence: Gene Ontology analysis was performed using Enrichr 42 .
- Full pipeline: read trimming [edgeR, fastp v0.20.1] -> alignment/mapping [Bowtie2 v2.1.0, RSEM v1.2.15] -> quantification [Salmon v1.4.0] -> normalisation [edgeR] -> stage not stated [Enrichr]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: GO enrichment analysis We performed GO enrichment analysis using the Enrichr 85 module in GSEApy 86 .
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: 4d ) using Enrichr 36 .
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Version used: **2.1**
- Evidence: 11e ) was performed with the list of genes commonly dysregulated in individual perturbations and the deletion model using the R package Enrichr (v.2.1) 58 and the DisGeNET database 42 .
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Evidence: For cell-type gene set enrichment analysis of genes significantly associated with IR, annotated genes were analysed using Enrichr 60 , 61 and the Human Gene Atlas database 60 , and the results of cell types with P adj < 0.05 were selected.
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### Platelet factors attenuate inflammation and rescue cognition in ageing. (Nature 2023)

- DOI: 10.1038/s41586-023-06436-3 | PMCID: PMC10468395 | PMID: 37587343
- Evidence: GO term enrichment analysis was performed using Enrichr 52 (GO Biological Process 2018).
- Full pipeline: alignment/mapping [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> quantification [DESeq2, ImageJ, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> stage not stated [Enrichr, Seurat]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: GO pathway analysis for the astrocytic subcompartments was performed using Enrichr ( https://maayanlab.cloud/Enrichr/ ).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: Gene set enrichment analysis was performed using Enrichr 74 .
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: The Gene Ontology term enrichment analysis was performed using Enrichr online tool ( https://maayanlab.cloud/Enrichr/ ), STRING ( https://string-db.org ) and clusterProfiler 57 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Evidence: The resulting genes were analysed with Enrichr using Jensen Diseases 53 .
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: 65 ), specifically the LINCS_L1000_Chem_Pert_down dataset from Enrichr 66 , to evaluate the gene set overlap between upregulated DEGs in spatial subclones and downregulated genes after compound treatment.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: Gene set enrichment analysis was performed using the top 1,000 genes in each group ranked by scores (Supplementary Table 13 ) and the implementation of the Enrichr workflow 102 in the Python package GSEApy ( https://gseapy.readthedocs.io/ ; v.0.10.7) with Gene Ontology Biological Process (2021) as the query database (Supplementary Tables 14 , 15 ).
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: SNV enrichment analysis Enrichr refers to an integrative web-based search engine of various gene set libraries and methods to compute gene set enrichment with interactive visualization of the enrichment results 89 – 91 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### CRISPR-Cas9 screens reveal regulators of ageing in neural stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07972-2 | PMCID: PMC11525198 | PMID: 39358505
- Evidence: We performed gene set enrichment analysis by inputting gene lists into the EnrichR online portal ( https://maayanlab.cloud/Enrichr/ ) 89 , 90 , and then focusing on the ‘Ontologies’ tab with GO Biological Process (2018), Molecular function (2018) and Cellular components (2018), sorting the terms based on P value, which is computed by EnrichR using the Fisher exact test.
- Full pipeline: quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Enrichr]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Overlap-based pathway and gene ontology enrichment was performed using the web-based Enrichr platform 58 , 59 .
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Cell type composition was estimated for significantly up- and downregulated genes in Enrichr 93 using Tabula Muris 94 as a reference (odds ratio test). scRNA-seq Library preparation AKPS organoids were dissociated into single cells and incubated with 2 μg ml −1 rmPlexin B2 or vehicle in culture medium for 2 h at 37 °C.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Pathway enrichment The overrepresentation analysis for the pathway enrichment was performed by EnrichR 31 ( https://maayanlab.cloud/Enrichr ), which is based on Fisher’s exact test, and with custom R scripts utilizing the enrichR library on MSigDB Hallmark 2020 and other gene sets.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: Gene Ontology analysis on abundance standardized CVs was performed with Enrichr 41 , 42 using the default settings.
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: Enrichment analyses were carried out with Enrichr 69 or g:Profiler 70 with default parameters.
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Evidence: Gene Ontology and KEGG pathway analysis Genes were examined for enrichment of KEGG Pathway and GO Biological Process terms using the Enrichr web server 73 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### A vagal reflex evoked by airway closure. (Nature 2024)

- DOI: 10.1038/s41586-024-07144-2 | PMCID: PMC10972749 | PMID: 38448588
- Evidence: After differential expression analysis, gene ontology enrichment analysis used the top 50 most enriched genes ranked by significance ( P value) using Enrichr 61 ( https://maayanlab.cloud/Enrichr/ ).
- Full pipeline: quality control [R v4.1.3, Seurat v4.1.1] -> alignment/mapping [R v4.1.3, Seurat v4.1.1] -> normalisation [R v4.1.3, Seurat v4.1.1] -> dimensionality reduction/clustering [R v4.1.3, Seurat v4.1.1, UMAP] -> differential/statistical testing [Enrichr, R v4.1.3, Seurat v4.1.1] -> stage not stated [Fiji v1.52p, ImageJ v1.52p]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: The GO pathway analysis for the Crym -BioID2 interactome was done with Enrichr ( https://maayanlab.cloud/Enrichr/ ).
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Multisensory gamma stimulation promotes glymphatic clearance of amyloid. (Nature 2024)

- DOI: 10.1038/s41586-024-07132-6 | PMCID: PMC10917684 | PMID: 38418876
- Evidence: Enrichr was used to perform the Gene Ontology enrichment analysis 58 with P value < 0.05 as a cut-off.
- Full pipeline: alignment/mapping [Suite2p] -> quantification [ImageJ] -> normalisation [ImageJ] -> registration [Suite2p] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [Seurat v4.0.3, scDblFinder]

### Modelling post-implantation human development to yolk sac blood emergence. (Nature 2024)

- DOI: 10.1038/s41586-023-06914-8 | PMCID: PMC10849971 | PMID: 38092041
- Evidence: All marker genes with a log 2 fold change above 1 were used as an input to the Enrichr web server 68 , 69 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Enrichr, Fiji, ImageJ, Seurat]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Evidence: Gene Ontology biological process (GO_Biological_Process_2021) gene set enrichment analysis was performed using the Enrichr package (v.3.1) in R 82 – 84 on tumour cluster 2 enriched differentially expressed genes with log 2 [FC] < −0.5 and P adj < 0.05.
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: 94 ) analyses were performed using Enrichr 95 – 97 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Evidence: Gene set enrichment analysis for protein clusters was performed using Enrichr 72 – 74 .
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: Over-representation analysis was performed using the Enrichr R package 87 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Evidence: Pathways with enriched DEGs were generated using Enrichr ( https://maayanlab.cloud/Enrichr/# ) on the basis of the Reactome Pathway Database, Kyoto Encyclopedia of Genes and Genomes, GEO and Gene Ontology database.
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: ...ulk RNA-seq (bottom). h , Overlap between n = 1,184 PTSD snDEGs and n = 1,918 MDD snDEGs. i , Top biological process (BP) and molecular function (MF) Enrichr Gene Ontology terms for the n = 502 PTSD-specific DEGs from panel h . j , Log-normalized mean expression of significantly discordant genes ( CTNNA3 (top) and HSPA1A (bottom)) in each subtype for PTSD (blue) and MDD (orange).
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: Enriched pathways per cluster were generated using the enrichGO function of the clusterProfiler Bioconductor R package 73 or the Enrichr gene list enrichment analysis tool 74 , using the marker genes identified per cluster from the FindMarkers() function.
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Evidence: Statistical analysis was performed using one-way analysis of variance (ANOVA). g , Unbiased Enrichr analysis showing the top 10 downregulated pathways by population cluster in MSCs, and osteo-associated, arteriolar and sinusoidal endothelial populations.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Cell cycle duration determines oncogenic transformation capacity. (Nature 2025)

- DOI: 10.1038/s41586-025-08935-x | PMCID: PMC12119354 | PMID: 40307557
- Evidence: The Bioplanet terms enriched in the DEGs were also identified using the online tool Enrichr ( https://maayanlab.cloud/Enrichr/ ) 87 .
- Full pipeline: quality control [Scanpy, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Evidence: Gene set enrichment analyses were performed with the Enrichr online software 88 .
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Evidence: ...nline Mendelian Inheritance in Man (OMIM) database ( https://www.omim.org/ ), Human Pain Genetics Database ( https://humanpaingeneticsdb.ca/hpgdb/ ), Enrichr ( https://maayanlab.cloud/Enrichr/ ), Gene Ontology ( https://geneontology.org/ ), Reactome ( https://reactome.org/ ), Wikipathways ( https://www.wikipathways.org/ ), Open Targets ( https://platform.opentargets.org/downloads , v.23.09) and Bi...
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### Intrinsic electrical activity drives small-cell lung cancer progression. (Nature 2025)

- DOI: 10.1038/s41586-024-08575-7 | PMCID: PMC11922742 | PMID: 39939778
- Evidence: These eight genes were uploaded into Enrichr to perform a GSEA, selecting the ‘GO Biological Process 2023’ dataset as a refs.
- Full pipeline: alignment/mapping [RSEM] -> machine learning [Cellpose, TrackMate] -> visualisation [QuPath v0.5.0] -> stage not stated [Enrichr, GSEA, ImageJ]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Evidence: Cyclic genes were further assessed using ChEA in Enrichr ( https://maayanlab.cloud/Enrichr/ , (v.3.2)), which infers transcription factor regulation from integration of previous genome-wide chromatin immunoprecipitation (ChIP) analyses.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Evolution of myeloid-mediated immunotherapy resistance in prostate cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08290-3 | PMCID: PMC11779626 | PMID: 39633050
- Evidence: ...ing differentially expressed genes (adjusted P -value < 0.05, |log 2 FC| > 0.5) in SPP1 hi -TAMs versus other myeloid cells in humans and mice, using Enrichr with MSigDB Hallmark 2020 gene sets (blue dashed line at adjusted P = 0.05). b , c , Correlations between enrichment scores for hypoxia ( P < 0.001, R = 0.858) ( b ) or SPP1 hi -TAMs ( c ) and the adenosine signalling signature (sig) across p...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> stage not stated [ImageJ v2.14.0, MACS2]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Evidence: Sum aggregation on the depth-normalized UMI counts was followed by variance stabilizing transformation, selection of the 300 most variable genes, standardization, k -means clustering ( k = 3) and Enrichr analysis against the Reactome_2022 using Enrichr.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Over-represented KEGG pathways 66 and GO biological process terms 22 were identified using Enrichr (FDR < 0.05).
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: Pathway enrichment analysis using Enrichr To identify pathways enriched in niche-specific upregulated genes, we performed enrichment analysis using the gseapy Python package (v1.0.6) 66 .
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: These top ranked DEGs were included for the downstream gene ontology (GO) analysis using Enrichr 71 , and gene ontology terms with an FDR < 0.05 were considered statistically significant.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Evidence: Pathway enrichment in gene sets was performed with Enrichr 86 , 87 and Ingenuity Pathway Analysis Qiagen knowledge database (IPA; v.153384343) 88 with the whole list of expressed genes as background.
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: Differentially enriched pathways were identified using Enrichr ( https://maayanlab.cloud/Enrichr/ ) 77 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: Enrichr analysis Enrichr 57 permits the analysis of enriched pathways in a list of genes and was used to analyse the RNA sequencing data.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: Subsequently, GSEA was performed using the gseapy package, leveraging the Enrichr method 85 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Genes in each module were used as input into gene ontology (GO) using Enrichr (GO_Biological Process_2018 database).
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Evidence: GO analysis was performed by uploading these DEGs into the Enrichr software 68 to identify the most relevant cell types.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Evidence: For the RIPK2 dataset, protein interactions for each condition (RI-4, 1 h; RI-4, 4 h; and BafA1, 18 h) were used as the input for gene set enrichment analysis for GO molecular function (2023) terms using Enrichr.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: Enrichment analyses of the latter two (that is, pathway- and disease-related gene sets) were performed using Enrichr 63 .
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Recurrent rewiring of the adult hippocampal mossy fiber system by a single transcriptional regulator, Id2. (PNAS 2021)

- DOI: 10.1073/pnas.2108239118 | PMCID: PMC8501755 | PMID: 34599103
- Evidence: ( D ) Enrichr transcription factor-target enrichment analysis based on 285 up-regulated (red) and 848 down-regulated genes (blue) that were differentially expressed ( P < 0.05) between the AAV-EGFP or AAV-Id2 data sets.
- Full pipeline: differential/statistical testing [Enrichr]

### ZMYND8 preferentially binds phosphorylated EZH2 to promote a PRC2-dependent to -independent function switch in hypoxia-inducible factor-activated cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2019052118 | PMCID: PMC7923384 | PMID: 33593912
- Evidence: ( A – D ) Meta-analysis of down-regulated genes after ZMYND8 KO under hypoxia ( A and B ) or normoxia ( C and D ) by Enrichr ( http://amp.pharm.mssm.edu/Enrichr ).
- Full pipeline: stage not stated [Enrichr]

### The harsh microenvironment in early breast cancer selects for a Warburg phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2011342118 | PMCID: PMC7826394 | PMID: 33452133
- Evidence: Gene list enrichment was performed using oPOSSUM ( http://opossum.cisreg.ca/oPOSSUM3/ ) and Enrichr ( https://maayanlab.cloud/Enrichr/ ) ( 22 , 23 ).
- Full pipeline: read trimming [R] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Cutadapt, Enrichr]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: Pathway analysis was performed using Enrichr ( 71 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Hedgehog-interacting protein acts in the habenula to regulate nicotine intake. (PNAS 2022)

- DOI: 10.1073/pnas.2209870119 | PMCID: PMC9674224 | PMID: 36346845
- Evidence: KEGG, GO, and GWAS Catalog analyses of DEGs identified by scRNA-seq were performed using Enrichr ( https://maayanlab.cl oud/Enrichr/ ).
- Full pipeline: alignment/mapping [HTSeq, STAR, Scanpy] -> quantification [HTSeq] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Enrichr]

### Conservation at the uterine-placental interface. (PNAS 2022)

- DOI: 10.1073/pnas.2210633119 | PMCID: PMC9565169 | PMID: 36191208
- Evidence: Insights into the identities of other cell clusters were obtained by running cluster-associated transcripts through the Enrichr web tool using default parameters and the “Cell Types” results ( 46 ).
- Full pipeline: quality control [R, Seurat v4.1.0] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v3.16.1] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, MACS2]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Enrichr, Genomic Regions Enrichment of Annotations Tool, and Hypergeometric Optimization of Motif EnRichment use a binomial test to calculate significant enrichment in biological process or motif enrichment, respectively.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### NAD&lt;sup&gt;+&lt;/sup&gt; metabolism drives astrocyte proinflammatory reprogramming in central nervous system autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2211310119 | PMCID: PMC9436380 | PMID: 35994674
- Evidence: Chea and JASPAR-TRANSFAC databases were accessed through the online open-access Enrichr platform ( 58 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [DESeq2, R] -> normalisation [DESeq2, R] -> stage not stated [Enrichr]

### Balanced control of thermogenesis by nuclear receptor corepressors in brown adipose tissue. (PNAS 2022)

- DOI: 10.1073/pnas.2205276119 | PMCID: PMC9388101 | PMID: 35939699
- Evidence: GO analysis for RNA-seq was performed using Enrichr ( 63 ), with the top ranked KEGG or GO pathways selected by Enrichr combined score.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, edgeR, kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR, kallisto] -> differential/statistical testing [R v4.1, edgeR, kallisto] -> stage not stated [Enrichr, SAMtools]

### Inhibition of the angiotensin II type 2 receptor AT&lt;sub&gt;2&lt;/sub&gt;R is a novel therapeutic strategy for glioblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2116289119 | PMCID: PMC9371711 | PMID: 35917342
- Evidence: All the differentially expressed genes for each agent were subjected to pathway analysis (Kyoto Encyclopedia of Genes and Genomes year 2021) using Enrichr, and cancer-related pathways were curated ( SI Appendix , Tables S5 and S6 ) and matched to each other.
- Full pipeline: differential/statistical testing [Enrichr] -> stage not stated [ImageJ]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Evidence: GOs were determined by submitting genes associated with ChIP peaks at Enrichr, and significant GO terms with P values of <0.01 were selected for visualization using ggplot.
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### STING activation promotes robust immune response and NK cell-mediated tumor regression in glioblastoma models. (PNAS 2022)

- DOI: 10.1073/pnas.2111003119 | PMCID: PMC9282249 | PMID: 35787058
- Evidence: Gene enrichment analysis was performed with Enrichr ( 92 ) to investigate enriched pathways.
- Full pipeline: alignment/mapping [STAR] -> quantification [QuPath] -> differential/statistical testing [DESeq2, R, ggplot2] -> stage not stated [Enrichr, ImageJ]

### Chronic inflammatory arthritis drives systemic changes in circadian energy metabolism. (PNAS 2022)

- DOI: 10.1073/pnas.2112781119 | PMCID: PMC9170023 | PMID: 35482925
- Evidence: Pathway analysis of differentially expressed and rhythmic genes used the Enrichr web tool ( 42 , 43 ).
- Full pipeline: differential/statistical testing [Enrichr, R v3.30.3, edgeR v3.30.3]

### Extracellular vesicles from triple negative breast cancer promote pro-inflammatory macrophages associated with better clinical outcome. (PNAS 2022)

- DOI: 10.1073/pnas.2107394119 | PMCID: PMC9169908 | PMID: 35439048
- Evidence: The gene ontology analysis was performed using Enrichr ( https://maayanlab.cloud/Enrichr/ ) ( 72 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [UMAP, pheatmap] -> stage not stated [Enrichr, MACS2, R, Seurat]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: Functional enrichment analysis on top marker genes was performed using Enrichr using the gseapy package with the gene set GO_Biological_Processes_2021 ( 87 , 88 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### A DNA repair-independent role for alkyladenine DNA glycosylase in alkylation-induced unfolded protein response. (PNAS 2022)

- DOI: 10.1073/pnas.2111404119 | PMCID: PMC8892324 | PMID: 35197283
- Evidence: We next performed gene set enrichment analyses using libraries provided by the Enrichr database ( 25 , 26 ).
- Full pipeline: stage not stated [Bioconductor, Enrichr]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Gene sets were enriched for pathways using BioPlanet 2019 and ChIP-seq targets using ChIP enrichment analysis (ChEA) through Enrichr ( 61 – 63 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### Identification of alternative protein targets of glutamate-ureido-lysine associated with PSMA tracer uptake in prostate cancer cells. (PNAS 2022)

- DOI: 10.1073/pnas.2025710119 | PMCID: PMC8795759 | PMID: 35064078
- Evidence: DGE and KEA analyses were performed using BioJupies ( 51 ) and Enrichr ( 42 ) platforms.
- Full pipeline: stage not stated [Enrichr]

### Hyperactive Rac stimulates cannibalism of living target cells and enhances CAR-M-mediated cancer cell killing. (PNAS 2023)

- DOI: 10.1073/pnas.2310221120 | PMCID: PMC10756302 | PMID: 38109551
- Evidence: ( B ) Pathway enrichment analysis was performed in Enrichr (Ma’ayan laboratory) on upregulated genes with a fold change (FC) >3 and the Molecular Signatures Database (MSigDB) Hallmark 2020 output data were plotted.
- Full pipeline: visualisation [Enrichr]

### Serine starvation silences estrogen receptor signaling through histone hypoacetylation. (PNAS 2023)

- DOI: 10.1073/pnas.2302489120 | PMCID: PMC10515173 | PMID: 37695911
- Evidence: ( B ) Pathway analysis via Enrichr of genes that lost at least one H3K27ac peak in −Ser.
- Full pipeline: stage not stated [Enrichr, GSEA]

### TET3-mediated DNA oxidation is essential for intestinal epithelial cell response to stressors. (PNAS 2023)

- DOI: 10.1073/pnas.2221405120 | PMCID: PMC10500271 | PMID: 37669386
- Evidence: Gene ontology (GO) analysis by Enrichr cataloged the most significantly reduced pathways in Tet3 ΔIEC mice included type I interferon responses (e.g., Ifitm2, Ifitm3, Irf7, Ifit1, and Gbp2 ), Wnt and Notch signaling (e.g., Dll1, Dll4, Wnt3 , and Wnt9b ), antimicrobial response (e.g., Lyz1, Lyz2, Reg3b, and Reg3g ), and cellular stemness (e.g., Olfm4, Lgr4, Lgr5, and Sox9 ) ( Fig.
- Full pipeline: stage not stated [Enrichr]

### Astrocyte-targeting therapy rescues cognitive impairment caused by neuroinflammation via the Nrf2 pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2303809120 | PMCID: PMC10438385 | PMID: 37549281
- Evidence: Furthermore, previous ChEA Enrichr analyses revealed NFE2L2 /Nrf2 as overlapping signatures of astrocytes from both tauopathy MAPT P301S and β-amyloidopathy APP/PS1 models ( 22 ).
- Full pipeline: stage not stated [Enrichr]

### Resolvin D1 prevents injurious neutrophil swarming in transplanted lungs. (PNAS 2023)

- DOI: 10.1073/pnas.2302938120 | PMCID: PMC10400944 | PMID: 37487095
- Evidence: For pathway analysis, differentially down-regulated genes in RvD1-treated compared to vehicle-treated lungs were used if P < 0.05 and Log 2 FC > 0.58 and analyzed by MSigDB Hallmark 2020 Pathway analysis ( https://maayanlab.cloud/Enrichr ).
- Full pipeline: quality control [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Enrichr, ggpubr] -> stage not stated [Seurat v4.0.0]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: The final gene list and weights were input into the GSEA preranked method ( 64 ) to identify the statistically significant enriched pathways using the “KEGG_2021_Human” gene set from the Enrichr website ( 65 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### Rapid cancer cell perineural invasion utilizes amoeboid migration. (PNAS 2023)

- DOI: 10.1073/pnas.2210735120 | PMCID: PMC10151474 | PMID: 37075074
- Evidence: Data were analyzed using GO pathway enrichment analysis with a web-based tool ( https://amp.pharm.mssm.edu/Enrichr/ ) for using the KEGG 2019 dataset.
- Full pipeline: alignment/mapping [Bioconductor, HTSeq] -> normalisation [Bioconductor, HTSeq] -> differential/statistical testing [Bioconductor, HTSeq] -> stage not stated [Enrichr, ImageJ v1.52q]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: Enrichr P values for E and H are computed using the Fisher exact test and adjusted using the Benjamini–Hochberg procedure.
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### Cytoskeletal association of ATP citrate lyase controls the mechanodynamics of macropinocytosis. (PNAS 2023)

- DOI: 10.1073/pnas.2213272120 | PMCID: PMC9974455 | PMID: 36787367
- Evidence: ( A ) Gene ontology terms associated with BioID screen showing top actin-associated proteins among BirA-ACLY hits grouped by cellular component (Enrichr).
- Full pipeline: quantification [ImageJ v1.53q] -> stage not stated [Enrichr, PyMOL]

### Neighbor-specific gene expression revealed from physically interacting cells during mouse embryonic development. (PNAS 2023)

- DOI: 10.1073/pnas.2205371120 | PMCID: PMC9926237 | PMID: 36595695
- Evidence: We used Enrichr ( 40 ), an enrichment analysis tool, to investigate the enriched GO terms and KEGG pathways for each marker gene group.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, Enrichr, scDblFinder]

### ER-tethered stress sensor CREBH regulates mitochondrial unfolded protein response to maintain energy homeostasis. (PNAS 2024)

- DOI: 10.1073/pnas.2410486121 | PMCID: PMC11626163 | PMID: 39589874
- Evidence: GO and pathway analyses were conducted using Enrichr and SRplot.
- Full pipeline: stage not stated [Enrichr]

### AMBRA1 controls the translation of immune-specific genes in T lymphocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2416722121 | PMCID: PMC11536168 | PMID: 39436665
- Evidence: Up-regulated and down-regulated genes were input separately into Enrichr ( https://maayanlab.cloud/Enrichr/ ) ( 45 ).
- Full pipeline: quantification [HTSeq] -> normalisation [pheatmap] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, SAMtools, deepTools]

### Transcriptional repression by HDAC3 mediates T cell exclusion from &lt;i&gt;Kras&lt;/i&gt; mutant lung tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2317694121 | PMCID: PMC11494357 | PMID: 39388266
- Evidence: ( C ) Enrichr Pathways and Transcription Factor analysis of the 26 commonly up-regulated genes identified in Fig.
- Full pipeline: alignment/mapping [HOMER, STAR] -> stage not stated [Enrichr, GSEA, QuPath]

### TCA metabolism regulates DNA hypermethylation in LPS and &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;-induced immune tolerance. (PNAS 2024)

- DOI: 10.1073/pnas.2404841121 | PMCID: PMC11474056 | PMID: 39348545
- Evidence: Web-based pathway enrichment including Metascape (Metascape online pathway analysis portal ( https://metascape.org/gp/index.html#/main/step1 ) and Enrichr ( https://maayanlab.cloud/Enrichr/ ) was also used for broader search as they include multiple ontology resources.
- Full pipeline: stage not stated [Enrichr, Metascape]

### miR-96-5p expression is sufficient to induce and maintain the senescent cell fate in the absence of stress. (PNAS 2024)

- DOI: 10.1073/pnas.2321182121 | PMCID: PMC11459134 | PMID: 39325426
- Evidence: ...re s earch (ARCHS4), and T ranscriptional R egulatory R elationships U nravelled by S entence-Based T ext-Mining (TRRUST) tools available through the Enrichr portal ( 33 – 35 ).
- Full pipeline: quality control [FastQC, GATK] -> alignment/mapping [FastQC, GATK] -> differential/statistical testing [MACS2] -> stage not stated [Enrichr]

### The neocortical infrastructure for language involves region-specific patterns of laminar gene expression. (PNAS 2024)

- DOI: 10.1073/pnas.2401687121 | PMCID: PMC11348331 | PMID: 39133845
- Evidence: The list of genes with FDR-adjusted P < 0.01 was input to the software Enrichr ( 88 ) (as implemented at https://maayanlab.cloud/Enrichr/ ) for a descriptive Gene Ontology analysis.
- Full pipeline: quality control [Bioconductor] -> alignment/mapping [MAGMA, STAR v2.5.1b, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [ImageJ v1.53t, R]

### Huntingtin contains an ubiquitin-binding domain and regulates lysosomal targeting of mitochondrial and RNA-binding proteins. (PNAS 2024)

- DOI: 10.1073/pnas.2319091121 | PMCID: PMC11317567 | PMID: 39074279
- Evidence: Gene ontology pathways significantly altered by HTT KO were identified using Enrichr.
- Full pipeline: stage not stated [Enrichr]

### USP11 promotes prostate cancer progression by up-regulating AR and c-Myc activity. (PNAS 2024)

- DOI: 10.1073/pnas.2403331121 | PMCID: PMC11295044 | PMID: 39052835
- Evidence: ( B ) GO analysis of genes down-regulated after USP11 KD was performed using the Enrichr web server.
- Full pipeline: quantification [pheatmap] -> differential/statistical testing [GSEA] -> stage not stated [Enrichr]

### Mechanical stress during confined migration causes aberrant mitoses and c-MYC amplification. (PNAS 2024)

- DOI: 10.1073/pnas.2404551121 | PMCID: PMC11260125 | PMID: 38990945
- Evidence: ( B ) Enrichr analysis of the transcriptionally up-regulated (blue) and down-regulated (light-blue) pathways in U2OS cells migrated across constrictions. c-MYC targets appear as the top-ranked transcriptionally up-regulated genes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr]

### Dichotomous transactivation domains contribute to growth inhibitory and promotion functions of TAp73. (PNAS 2024)

- DOI: 10.1073/pnas.2318591121 | PMCID: PMC11127001 | PMID: 38739802
- Evidence: Functional classification of the genes using the IPA and Enrichr ( https://maayanlab.cloud/Enrichr/ ) ( 47 ) revealed that the top pathways regulated by TAp73β expression included cell-cycle, DNA replication, and the various DNA repair pathways ( Fig.
- Full pipeline: stage not stated [Enrichr]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: GO analysis was performed using the gProfileR R package ( 58 ) according to the authors’ tutorial and Enrichr and identified significant GO terms associated with the most differentially expressed genes.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Posttranscriptional control of the B cell receptor by HuR is essential for innate B cell maintenance and function. (PNAS 2025)

- DOI: 10.1073/pnas.2421149122 | PMCID: PMC12452923 | PMID: 40938701
- Evidence: Gene ontology enrichment analyses were performed using Enrichr and default settings. iCLIP analyses were performed using Flow ( https://app.flow.bio/ ) which integrates nf-core/clipseq v1.0 for iCLIP sequencing data analyses ( https://github.com/nf-core/clipseq ).
- Full pipeline: differential/statistical testing [DESeq2 v1.28.0] -> stage not stated [Enrichr]

### The WWP1-JARID1B axis sustains acute myeloid leukemia chemoresistance. (PNAS 2025)

- DOI: 10.1073/pnas.2421159122 | PMCID: PMC12280953 | PMID: 40627385
- Evidence: Functional enrichment was performed using Enrichr ( 52 ) and pathways were considered significant when showing an FDR < 0.05 Clinical Samples.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2, Enrichr] -> stage not stated [ggplot2]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Evidence: Ontology analyses were performed using Enrichr ( 63 ).
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### Generative prediction of causal gene sets responsible for complex traits. (PNAS 2025)

- DOI: 10.1073/pnas.2415071122 | PMCID: PMC12184495 | PMID: 40504147
- Evidence: Not all upstream transcription factors have transcriptional responses measured in our library, so we use the Enrichr gene set enrichment database to find them.
- Full pipeline: machine learning [SciPy] -> stage not stated [Enrichr, PyTorch]

### Induction of the ISR by AB5 subtilase cytotoxin drives type-I IFN expression in pDCs via STING activation. (PNAS 2025)

- DOI: 10.1073/pnas.2421258122 | PMCID: PMC12130819 | PMID: 40388626
- Evidence: Comparative analysis of differentially expressed genes (DEGs) and Gene Ontology (GO) pathways) using the Enrichr bioinformatic suite ( 25 ) in SubAB- and/or CL307-treated PBMCs showed that both treatments impacted gene expression with a variable efficiency among cell subsets ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Evidence: The functional enrichment analysis of ChIP-Seq peak-associated genes was performed using Enrichr (version of March 13th, 2022) ( 84 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: We used the tool EnrichR : https://maayanlab.cloud/Enrichr/ for GO analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### Metabolism-weighted brain connectome reveals synaptic integration and vulnerability to neurodegeneration. (PNAS 2026)

- DOI: 10.1073/pnas.2531706123 | PMCID: PMC13321360 | PMID: 42330267
- Evidence: We also did the enrichment analysis for the KEGG 2021 Human pathway separately using Enrichr ( 74 – 76 ) to find the relationship of our MwC map with disease pathways.
- Full pipeline: normalisation [ANTs, FSL, MRtrix3] -> registration [ANTs, FSL, MRtrix3] -> stage not stated [Enrichr, Metascape]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Enrichr ( 62 ) was used for pathway analysis with KEGG and/or Bioplanet pathways, using the entire set of expressed genes according to the scRNA-seq as a background set.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: Markers were submitted for gene set enrichment ranking and analysis using the Enrichr tool as implemented in the GSEApy (v1.0) package to query the Gene Ontology (GO) Biological Process database (GO_BP_2022) ( data S26 ).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Enrichr pathway analysis ( 28 ) of this gene set showed a significant enrichment of many cancer-associated pathways, including epithelial-mesenchymal transitions (EMT), hypoxia, glycolysis, and mTORC1 signaling ( fig.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Macrophage-derived oncostatin M repairs the lung epithelial barrier during inflammatory damage. (Science 2025)

- DOI: 10.1126/science.adi8828 | PMCID: PMC12541708 | PMID: 40638741
- Evidence: The resulting clusters were analyzed using MSigDB pathway enrichment in Enrichr.
- Full pipeline: dimensionality reduction/clustering [Enrichr, UMAP]

