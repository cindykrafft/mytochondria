# Metascape

- **Category:** genomics
- **Papers in survey:** 76
- **Journals:** PNAS (60), Nature (11), Cell (4), Science (1)
- **Years:** 2021 (4), 2022 (12), 2023 (14), 2024 (22), 2025 (16), 2026 (8)
- **Versions named:** 3.5 (2), 3.5.20230501 (2)
- **Pipeline stages it appears in:** differential/statistical testing (14), visualisation (5), quantification (2), dimensionality reduction/clustering (2), alignment/mapping (2), machine learning (1)

## Papers

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: ...0.6.1 Treestar RRID: SCR_008520 HOMER software version 4.11 http://homer.ucsd.edu/ RRID: SCR_010881 Imaris software version Bitplane RRID: SCR_007370 Metascape http://metascape.org/gp/index.html#/main/step1 RRID: SCR_016620 Prism software version 9 GraphPad RRID: SCR_002798 R version 4.05 http://www.r-project.org N/A Seurat package version 4.0 Hao et al., 2021 RRID: SCR_007322 STAR aligner version...
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### Multi-organ proteomic landscape of COVID-19 autopsies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.004 | PMCID: PMC7794601 | PMID: 33503446
- Evidence: ...html R version 3.6.1 R Project https://www.r-project.org Ingenuine pathway analysis (version 51963813) Krämer et al., 2014 https://www.qiagen.com/cn/ Metascape Zhou et al., 2019 https://metascape.org/gp/index.html#/main/step1 ClueGO 2.5.6 ( Bindea et al., 2009 ) https://cytoscape.org/ String Szklarczyk et al., 2019 https://string-db.org/ Other SOLAμ Thermo Fisher Scientific Cat # 62209-001 Resourc...
- Full pipeline: alignment/mapping [GSEA] -> differential/statistical testing [GSEA] -> stage not stated [Cytoscape, Metascape, R v3.6.1]

### Microglia maintain structural integrity during fetal brain morphogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.012 | PMCID: PMC10869139 | PMID: 38309258
- Version used: **3.5.20230501**
- Evidence: ...SCR_014199 Adobe Illustrator CS6 Adobe Systems RRID: SCR_010279 R software 4.2.2 GNU Project https://www.r-project.org/ ; RRID: SCR_001905 R package: Metascape 3.5.20230501 Metascape Team http://metascape.org/gp/index.html#/main/step1 ; RRID: SCR_016620 R package: Seurat 4.3.0.1 N/A https://satijalab.org/seurat/get_started.html ; RRID: SCR_016341 R package: Tidyverse 2.0.0 N/A https://CRAN.R-proje...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Bowtie2, ImageJ, Metascape v3.5.20230501, R, Seurat v4.3.0.1, ggplot2, tidyverse]

### Inflammation switches the chemoattractant requirements for naive lymphocyte entry into lymph nodes. (Cell 2025)

- DOI: 10.1016/j.cell.2024.11.031 | PMCID: PMC11845304 | PMID: 39708807
- Evidence: 66 Gene ontology and transcription factor regulation analysis on differentially accessible genes were performed through Metascape.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2 v1.4.2, Metascape] -> visualisation [UMAP] -> stage not stated [R v4.2.1, Seurat v4.3.0, deepTools v3.5.4]

### The role of somatosensory innervation of adipose tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05137-7 | PMCID: PMC9477745 | PMID: 36045288
- Evidence: Gene Ontology enrichment analysis was performed using Metascape 59 with the Gene Prioritization by Evidence Counting setting.
- Full pipeline: alignment/mapping [SAMtools v1.10, Salmon v1.5.1] -> quantification [ImageJ, Salmon v1.5.1] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [Metascape]

### Signalling by senescent melanocytes hyperactivates hair growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06172-8 | PMCID: PMC10284692 | PMID: 37344645
- Evidence: For gene ontology terms reported in Supplementary Tables 1 , 3 , 4 and 5 , analysis was done using Metascape.
- Full pipeline: alignment/mapping [RSEM v1.2.25, STAR v2.4.2a] -> quantification [RSEM v1.2.25] -> normalisation [RSEM v1.2.25] -> dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [edgeR v3.2.2] -> stage not stated [Metascape]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: For gene ontology analysis, the Metascape web application ( https://metascape.org/gp/index.html ) was used to infer enrichment of gene ontology terms 74 .
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Evidence: The obtained DEGs for each comparison were used as input in Metascape online tool 68 to perform functional enrichment analysis, with a Q value threshold set at 0.05 (Supplementary Table 11 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: Gene overlap and transcription factor target enrichment analysis was performed using Metascape 73 .
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Evidence: Metascape 49 was used to generate GO analyses for Fig.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Evidence: Pathway analysis Pathway analysis was performed using Metascape 52 or the GSEA GUI tool (v.4.3.3).
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: DEGs with FDR < 0.05 and |log 2 fold change| > 0.1 were used for Gene Ontology enrichment analyses using Metascape 78 v.3.5.20240101.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Glycocalyx dysregulation impairs blood-brain barrier in ageing and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08589-9 | PMCID: PMC11946907 | PMID: 40011765
- Evidence: Genes with FDR <0.05 were used for subsequent KEGG pathway enrichment and Metascape 43 analysis (Supplementary Data 5 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.32, Metascape] -> visualisation [DESeq2 v1.32] -> stage not stated [ImageJ, Seurat v4.1.1, SoupX v1.6.2, scDblFinder v2.0.4]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Evidence: Pathway analysis was performed using Metascape 52 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Cytosolic acetyl-coenzyme A is a signalling metabolite to control mitophagy. (Nature 2026)

- DOI: 10.1038/s41586-025-09745-x | PMCID: PMC12823391 | PMID: 41225001
- Evidence: GO biological processes enriched in the top 100 mitochondrial genes from the screen were analysed using the Metascape database 55 . qPCR analysis To quantify the mtDNA/nDNA ratio, genomic DNA was isolated from cells or tissues using the TIANamp Genomic DNA Kit (DP304-02, TIANGEN) according to the the manufacturer’s instructions, and qPCR was conducted to amplify the mitochondria genome ( MT-CYTB ,...
- Full pipeline: quantification [Metascape] -> stage not stated [R, ggplot2]

### Fever supports CD8<sup>+</sup> effector T cell responses by promoting mitochondrial translation. (PNAS 2021)

- DOI: 10.1073/pnas.2023752118 | PMCID: PMC8237659 | PMID: 34161266
- Evidence: Gene ontology analysis was performed using the Metascape online platform ( 41 ).
- Full pipeline: quality control [Galaxy, deepTools, featureCounts] -> read trimming [Galaxy, deepTools, featureCounts] -> alignment/mapping [DESeq2, Galaxy, R, deepTools, featureCounts] -> quantification [DESeq2, Galaxy, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [ImageJ, Metascape]

### The evolution of ancestral and species-specific adaptations in snowfinches at the Qinghai-Tibet Plateau. (PNAS 2021)

- DOI: 10.1073/pnas.2012398118 | PMCID: PMC8020664 | PMID: 33753478
- Evidence: We performed functional enrichment analyses using Metascape ( 63 ), which has integrated the latest GO annotation.
- Full pipeline: stage not stated [BUSCO, Metascape, R]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Evidence: GO representative analysis is done by Metascape ( 54 ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: Pathway analysis on the top 100 differentially expressed genes was performed using Metascape ( 69 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: GO enrichment analyses on temporal group genes were performed in Metascape ( 72 ).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Tcf-1 promotes genomic instability and T cell transformation in response to aberrant β-catenin activation. (PNAS 2022)

- DOI: 10.1073/pnas.2201493119 | PMCID: PMC9371646 | PMID: 35921443
- Evidence: ( B ) Pathway analysis of restored DEGs that were up-regulated (red) or down-regulated (DN, blue) in CAT versus Cre and CAT- Tcf7 Δ (Metascape, www.metascape.org ).
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA] -> stage not stated [HOMER, Metascape]

### Immune checkpoint inhibitors unleash pathogenic immune responses against the microbiota. (PNAS 2022)

- DOI: 10.1073/pnas.2200348119 | PMCID: PMC9245641 | PMID: 35727974
- Evidence: ( F ) Metascape pathway enrichment analysis for genes up-regulated in S. epi + anti–CTLA-4 in comparison to S. epidermidis + isotype.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [HOMER, Metascape]

### ESCPE-1 mediates retrograde endosomal sorting of the SARS-CoV-2 host factor Neuropilin-1. (PNAS 2022)

- DOI: 10.1073/pnas.2201980119 | PMCID: PMC9231623 | PMID: 35696571
- Evidence: Gene ontology analysis was performed using the PANTHER classification system ( 54 ) and Metascape ( 55 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [ImageJ, Metascape]

### A synthetic lethality screen reveals ING5 as a genetic dependency of catalytically dead Set1A/COMPASS in mouse embryonic stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2118385119 | PMCID: PMC9171609 | PMID: 35500115
- Evidence: GO analysis was carried out using the Metascape software.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [ImageJ, MACS2, Metascape]

### Agonists of prostaglandin E<sub>2</sub> receptors as potential first in class treatment for nephronophthisis and related ciliopathies. (PNAS 2022)

- DOI: 10.1073/pnas.2115960119 | PMCID: PMC9170064 | PMID: 35482924
- Evidence: ( Right ) Pertinent down- (light gray) or up-regulated (dark gray) pathways or relevant processes involving these genes were highlighted using Metascape.
- Full pipeline: alignment/mapping [R, featureCounts] -> quantification [ImageJ] -> stage not stated [Metascape, PHENIX]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: In addition, enrichment analysis was performed in Metascape ( 73 ) between non–exercise-trained mutant strains versus non–exercise-trained B6 control (including genes with adjusted P value < 0.05) and between exercise-trained versus non–exercise-trained within each strain (including genes with nominal P value < 0.05).
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### Sympatric speciation of the spiny mouse from Evolution Canyon in Israel substantiated genomically and methylomically. (PNAS 2022)

- DOI: 10.1073/pnas.2121822119 | PMCID: PMC9060526 | PMID: 35320043
- Evidence: GO enrichment was performed by Metascape.
- Full pipeline: stage not stated [Bismark, DELLY, GATK, Metascape, R, VCFtools]

### CD164 is a host factor for lymphocytic choriomeningitis virus entry. (PNAS 2022)

- DOI: 10.1073/pnas.2119676119 | PMCID: PMC8915965 | PMID: 35235462
- Evidence: To determine how LCMV binds to the cell surface in the absence of α-DG, we further mined our screen data to look for possible attachment factors by performing pathway analysis on the top 250 genes using Metascape ( Fig.
- Full pipeline: stage not stated [Metascape]

### p53 deficient breast cancer cells reprogram preadipocytes toward tumor-protective immunomodulatory cells. (PNAS 2023)

- DOI: 10.1073/pnas.2311460120 | PMCID: PMC10756271 | PMID: 38127986
- Evidence: Pathway enrichment analysis of downregulated and upregulated genes was performed using DAVID ( https://david.ncifcrf.gov ) ( 47 ) and Metascape ( https://metascape.org ) ( 48 ).
- Full pipeline: quantification [ImageJ] -> normalisation [RSEM] -> machine learning [MACS2] -> stage not stated [GSEA, Metascape, R v4.0.2]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Pathway analysis was performed with Metascape ( 48 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### A transcriptional program underlying the circannual rhythms of gonadal development in medaka. (PNAS 2023)

- DOI: 10.1073/pnas.2313514120 | PMCID: PMC10756274 | PMID: 38109538
- Version used: **3.5**
- Evidence: GO analyses of circannual genes and of DOGs in each season were performed using Metascape 3.5 ( 26 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5, RSEM v1.2.12] -> quantification [Bowtie2 v2.2.5, RSEM v1.2.12] -> stage not stated [BLAST, DIAMOND, Metascape v3.5, R v3.5]

### The human adenovirus E1B-55K oncoprotein coordinates cell transformation through regulation of DNA-bound host transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2310770120 | PMCID: PMC10622919 | PMID: 37883435
- Evidence: Through contextualization via Metascape pathway and process enrichment analyses, we captured the potential influences of E1B-55K on biological pathways ( Fig.
- Full pipeline: alignment/mapping [MACS2, R] -> stage not stated [HOMER, Metascape]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Evidence: In addition, the GO terms and KEGG functional enrichment of all genes corresponding to homozygous and putatively deleterious LOF mutations were retrieved using the Metascape website ( 103 ).
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### IL-6 trans-signaling in a humanized mouse model of scleroderma. (PNAS 2023)

- DOI: 10.1073/pnas.2306965120 | PMCID: PMC10500188 | PMID: 37669366
- Evidence: Pathway analysis of differentially expressed genes with adjusted P value of less than 0.05 was completed with Metascape ( 78 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### CD45 alleviates airway inflammation and lung fibrosis by limiting expansion and activation of ILC2s. (PNAS 2023)

- DOI: 10.1073/pnas.2215941120 | PMCID: PMC10483638 | PMID: 37639581
- Evidence: Gene set enrichment analysis (GSEA) (Broad Institute) and enrichment analysis using Metascape ( 67 ) were performed.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Metascape]

### Genome-wide kinase-MAM interactome screening reveals the role of CK2A1 in MAM Ca<sup>2+</sup> dynamics linked to DEE66. (PNAS 2023)

- DOI: 10.1073/pnas.2303402120 | PMCID: PMC10410754 | PMID: 37523531
- Evidence: ( C and D ) Metascape enrichment analysis of Gene Ontology Biological Process (GO-BP) and KEGG pathways, respectively, colored by the identities of the two lists (90 kinase candidates and putative MAM-resident proteins).
- Full pipeline: stage not stated [Metascape]

### Immunization with lytic polysaccharide monooxygenase CbpD induces protective immunity against <i>Pseudomonas aeruginosa</i> pneumonia. (PNAS 2023)

- DOI: 10.1073/pnas.2301538120 | PMCID: PMC10372616 | PMID: 37459522
- Evidence: The dark orange arc and purple lines reflect the regulated proteins shared in both datasets; light orange color represents regulated proteins unique to WT and ΔCbpD-infected vs. control mice; blue lines indicate the ontology term overlap among the significantly regulated proteins; plot generated with Metascape.
- Full pipeline: stage not stated [AlphaFold, Metascape]

### Metastasis from the tumor interior and necrotic core formation are regulated by breast cancer-derived angiopoietin-like 7. (PNAS 2023)

- DOI: 10.1073/pnas.2214888120 | PMCID: PMC10013750 | PMID: 36853945
- Evidence: ( F ) Metascape analysis of gene enrichment.
- Full pipeline: quantification [QuPath] -> stage not stated [Metascape]

### Self-renewing macrophages in dorsal root ganglia contribute to promote nerve regeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2215906120 | PMCID: PMC9963351 | PMID: 36763532
- Evidence: The data were subsequently analyzed for enrichment of KEGG pathways using Metascape ( 74 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Metascape, R]

### CITED2 is a conserved regulator of the uterine-placental interface. (PNAS 2023)

- DOI: 10.1073/pnas.2213622120 | PMCID: PMC9934066 | PMID: 36626551
- Evidence: Functional patterns of transcript expression were further analyzed using Metascape ( 64 ). scRNA-seq.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat] -> stage not stated [Metascape]

### OGT controls mammalian cell viability by regulating the proteasome/mTOR/ mitochondrial axis. (PNAS 2023)

- DOI: 10.1073/pnas.2218332120 | PMCID: PMC9934350 | PMID: 36626549
- Evidence: ( F ) Metascape visualization of the protein–protein interactome network of the 115 highly scored hits from the CRISPR screen.
- Full pipeline: visualisation [Metascape] -> stage not stated [GSEA]

### Targeting DTX2/UFD1-mediated FTO degradation to regulate antitumor immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2407910121 | PMCID: PMC11665913 | PMID: 39661064
- Evidence: GO and KEGG pathway enrichment analyses were conducted using Metascape, while gene expression correlation and overall survival analyses utilized PINA v3.0, UCSC Xena, and KM Plot.
- Full pipeline: stage not stated [GSEA, Metascape]

### Identification of FBLL1 as a neuron-specific RNA 2'-O-methyltransferase mediating neuronal differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2406961121 | PMCID: PMC11621510 | PMID: 39570315
- Evidence: Gene Ontology analysis using Metascape ( 35 ) revealed that proteins significantly more abundant in FBLL1-IP samples were associated with nervous system development ( Fig.
- Full pipeline: stage not stated [AlphaFold, Metascape]

### IFN-γ-induced Th1-Treg polarization in inflamed brains limits exacerbation of experimental autoimmune encephalomyelitis. (PNAS 2024)

- DOI: 10.1073/pnas.2401692121 | PMCID: PMC11621829 | PMID: 39560646
- Evidence: Metascape ( https://metascape.org ) was used for the Gene Ontology enrichment analysis of differentiallyexpressed genes (DEGs).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Metascape] -> stage not stated [MACS2, Seurat]

### Spatiotemporal transcriptomic map of glial cell response in a mouse model of acute brain ischemia. (PNAS 2024)

- DOI: 10.1073/pnas.2404203121 | PMCID: PMC11573666 | PMID: 39499634
- Evidence: Prepared with Metascape ( 32 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Metascape, Seurat]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Version used: **3.5.20230501**
- Evidence: GO Cellular Component terms enriched for these differentially expressed genes were identified using Metascape v3.5.20230501 ( https://metascape.org/ ) ( 77 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### TCA metabolism regulates DNA hypermethylation in LPS and &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;-induced immune tolerance. (PNAS 2024)

- DOI: 10.1073/pnas.2404841121 | PMCID: PMC11474056 | PMID: 39348545
- Evidence: Web-based pathway enrichment including Metascape (Metascape online pathway analysis portal ( https://metascape.org/gp/index.html#/main/step1 ) and Enrichr ( https://maayanlab.cloud/Enrichr/ ) was also used for broader search as they include multiple ontology resources.
- Full pipeline: stage not stated [Enrichr, Metascape]

### Alveolar macrophage function is impaired following inhalation of berry e-cigarette vapor. (PNAS 2024)

- DOI: 10.1073/pnas.2406294121 | PMCID: PMC11459156 | PMID: 39312670
- Evidence: Differentially expressed proteins with log 2 fold change values >1.5 and <−1.5 were analyzed using Metascape ( 65 ).
- Full pipeline: differential/statistical testing [Metascape] -> structure determination [AutoDock Vina v1.5.7] -> stage not stated [MACS2]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Evidence: Metascape ( 68 ) was used for GO enrichment analysis.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Qki5 safeguards spinal motor neuron function by defining the motor neuron-specific transcriptome via pre-mRNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2401531121 | PMCID: PMC11406248 | PMID: 39226364
- Evidence: To further elucidate the biologically relevant pathway of the Qki5 RNA targets, we first performed Metascape pathway analysis using a list of genes that have alternative splicing changes between siNC and siQk KD in mMNs (660 changed AS exons in siNC vs. siQk , cutoff: P < 0.01, FDR < 0.1, |DI| > 0.05, and reads per kilobase of exon per million mapped reads (RPKM) > 1) and hMNs (388 changed AS exon...
- Full pipeline: alignment/mapping [Metascape] -> quantification [Metascape, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### Zika virus NS5 protein inhibits type I interferon signaling via CRL3 E3 ubiquitin ligase-mediated degradation of STAT2. (PNAS 2024)

- DOI: 10.1073/pnas.2403235121 | PMCID: PMC11348293 | PMID: 39145933
- Evidence: ( F ) Bar plot of the gene ontology (GO) analysis depicting enriched GO terms for the top 20 hits, analyzed using the Metascape analysis webtool.
- Full pipeline: stage not stated [ImageJ, Metascape]

### A therapy for suppressing canonical and noncanonical SARS-CoV-2 viral entry and an intrinsic intrapulmonary inflammatory response. (PNAS 2024)

- DOI: 10.1073/pnas.2408109121 | PMCID: PMC11287264 | PMID: 39028694
- Evidence: S2 A and B ), as determined by correlating the signature genes to scRNAseq data in published datasets from fetal and adult human lung cells ( 20 – 27 ) and the gene annotation and analysis resource, Metascape ( 28 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Metascape]

### An HSF1-JMJD6-HSP feedback circuit promotes cell adaptation to proteotoxic stress. (PNAS 2024)

- DOI: 10.1073/pnas.2313370121 | PMCID: PMC11260097 | PMID: 38985769
- Evidence: WT cells were calculated using Metascape.
- Full pipeline: stage not stated [Metascape]

### Insulin receptor orchestrates kidney antibacterial defenses. (PNAS 2024)

- DOI: 10.1073/pnas.2400666121 | PMCID: PMC11260129 | PMID: 38976738
- Evidence: ( B ) Metascape TRRUST analysis identifies transcription factors regulating differential gene expression in IRKO ICs.
- Full pipeline: differential/statistical testing [Metascape] -> stage not stated [MACS2]

### Autoimmunity against melanoma differentiation-associated gene 5 induces interstitial lung disease mimicking dermatomyositis in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2313070121 | PMCID: PMC11032490 | PMID: 38588434
- Evidence: From given expression data, DEGs were defined as false discovery rate <0.05, and further understanding the functional classifications of DEGs, gene enrichment analysis was performed using Metascape ( https://metascape.org/gp/index.html ).
- Full pipeline: differential/statistical testing [Metascape] -> stage not stated [GSEA, MACS2]

### Activation of polyamine catabolism promotes glutamine metabolism and creates a targetable vulnerability in lung cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2319429121 | PMCID: PMC10990097 | PMID: 38513095
- Evidence: Functional enrichment analysis was performed using the Metascape online tool ( https://metascape.org/gp/index.html#/main/step1 ).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.4.2a] -> quantification [RSEM v1.3.3] -> differential/statistical testing [DESeq2, R] -> stage not stated [Metascape]

### The neuroimmune CGRP-RAMP1 axis tunes cutaneous adaptive immunity to the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2322574121 | PMCID: PMC10945812 | PMID: 38451947
- Evidence: Gene Ontology (GO) enrichment analysis for differentially expressed genes was performed using Metascape ( 73 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER, Metascape]

### Cellular and molecular organization of the Drosophila foregut. (PNAS 2024)

- DOI: 10.1073/pnas.2318760121 | PMCID: PMC10945768 | PMID: 38442150
- Evidence: Metascape analysis ( 49 ) showed the CA cluster preferentially expresses genes in additional pathways.
- Full pipeline: dimensionality reduction/clustering [Metascape, UMAP] -> stage not stated [Seurat]

### A predisposed motor bias shapes individuality in vocal learning. (PNAS 2024)

- DOI: 10.1073/pnas.2308837121 | PMCID: PMC10801888 | PMID: 38198530
- Evidence: GO analysis for individually-different genes in RAPNs was performed using Metascape ( https://metascape.org/gp/index.html ).
- Full pipeline: dimensionality reduction/clustering [UMAP, WGCNA] -> visualisation [UMAP] -> stage not stated [Metascape, R, Seurat]

### Maladaptive immunity to the microbiota promotes neuronal hyperinnervation and itch via IL-17A. (PNAS 2025)

- DOI: 10.1073/pnas.2525146122 | PMCID: PMC12772199 | PMID: 41428888
- Evidence: P < 0.05), and pathway enrichment via Metascape ( 96 , 98 , 99 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.44.0] -> visualisation [UMAP] -> stage not stated [Metascape, R v4.4, Seurat v4.4.0]

### MBNL loss of function in smooth muscle as a model for myotonic dystrophy associated gastrointestinal dysmotility. (PNAS 2025)

- DOI: 10.1073/pnas.2522788122 | PMCID: PMC12718393 | PMID: 41379996
- Evidence: Gene IDs of overlapping CEs were used for GO term analysis using Metascape ( 128 ).
- Full pipeline: quality control [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> alignment/mapping [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> variant calling [ImageJ] -> normalisation [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> stage not stated [Metascape]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Evidence: The functional role of significantly enriched proteins was determined by Metascape ( 32 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### Sirt6 prevents the age-related decline of H&lt;sub&gt;2&lt;/sub&gt;S through the control of one-carbon metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2514084122 | PMCID: PMC12646208 | PMID: 41218122
- Evidence: ( A ) Metascape pathways and ( B ) Proteomaps analyses of Sirt6-dependent acetylation sites.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [Metascape]

### Lipid raft proteomics identify endothelial myosin-9 (MYH9) as a regulator of low-density lipoprotein transcytosis and atherosclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2509315122 | PMCID: PMC12582289 | PMID: 41134623
- Evidence: The top 100 most positively correlated genes were submitted to Metascape ( 60 ) for pathway analysis using the default background for Homo sapiens .
- Full pipeline: read trimming [HISAT2] -> alignment/mapping [HISAT2] -> quantification [Cufflinks, ImageJ] -> stage not stated [Metascape]

### Identification of a VPS29 isoform with restricted association to Retriever and Retromer accessory proteins through autoinhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2501111122 | PMCID: PMC12260524 | PMID: 40587794
- Version used: **3.5**
- Evidence: Protein–protein interaction network analysis was performed using Metascape 3.5 ( 81 ) and visualized using Cytoscape 3.3 software with the Enrichment Map plug-in ( 82 ).
- Full pipeline: alignment/mapping [ChimeraX v1.6.1, PyMOL] -> differential/statistical testing [R] -> machine learning [AlphaFold, ColabFold] -> visualisation [ChimeraX v1.6.1, Cytoscape v3.3, Metascape v3.5, PyMOL] -> stage not stated [IQ-TREE v2.2.5]

### Ligand-specific regulation of a binary enhancer code dictating cellular senescence. (PNAS 2025)

- DOI: 10.1073/pnas.2506321122 | PMCID: PMC12184664 | PMID: 40493192
- Evidence: ( E ) Selected GO-terms from Metascape analysis of 252 RW GAINED genes.
- Full pipeline: alignment/mapping [HOMER] -> stage not stated [GSEA, Metascape]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: GO enrichment analysis was performed by using Metascape ( 73 ) or R package clusterProfiler ( 74 ) (Version 3.18.1).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Estrogen-related receptors regulate innate and adaptive muscle mitochondrial energetics through cooperative and distinct actions. (PNAS 2025)

- DOI: 10.1073/pnas.2426179122 | PMCID: PMC12107179 | PMID: 40354528
- Evidence: ChIP-Seq results were visualized on the UCSC genome browser, and gene ontology and pathway analysis was performed using Metascape ( metascape.org ).
- Full pipeline: alignment/mapping [HOMER] -> visualisation [Metascape]

### Phospholipid flippase ATP11A brokers uterine epithelial integrity and function. (PNAS 2025)

- DOI: 10.1073/pnas.2420617122 | PMCID: PMC12054786 | PMID: 40261925
- Evidence: Gene enrichment analyses were performed using Metascape ( 23 ).
- Full pipeline: quality control [R, Seurat v5.1.0] -> alignment/mapping [STAR v2.6.1a] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq, ImageJ v1.53, Metascape]

### Metabolism-weighted brain connectome reveals synaptic integration and vulnerability to neurodegeneration. (PNAS 2026)

- DOI: 10.1073/pnas.2531706123 | PMCID: PMC13321360 | PMID: 42330267
- Evidence: We used the Metascape ( http://metascape.org ) ( 34 ), an automated meta-analysis tool, for our gene enrichment analysis.
- Full pipeline: normalisation [ANTs, FSL, MRtrix3] -> registration [ANTs, FSL, MRtrix3] -> stage not stated [Enrichr, Metascape]

### Active zone plasticity couples sleep need to presynaptic hypophosphorylation. (PNAS 2026)

- DOI: 10.1073/pnas.2524065123 | PMCID: PMC13273273 | PMID: 42258713
- Evidence: Lists of significantly upregulated and downregulated proteins from proteomic and phospho-proteomic experiments were uploaded to Metascape ( https://metascape.org/ ) and enrichment analysis was performed for Gene Ontology (GO) Biological processes, Cellular components, and KEGG Pathway with a cut-off of P < 0.01, enrichment factor > 1.5, and number of hits > 2.
- Full pipeline: stage not stated [AlphaFold, ImageJ, Metascape, PyMOL, STRING db]

### Impact of sex chromosomes and gonad type in stress susceptibility in corticostriatal brain regions. (PNAS 2026)

- DOI: 10.1073/pnas.2531920123 | PMCID: PMC13229181 | PMID: 42189975
- Evidence: Pathway overrepresentation through Metascape was used to identify biological processes that were most impacted by stress exposure, with all expressed transcripts used as the background reference set ( 75 ) and networks were visualized using Cytoscape 3.10.3.
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.10.3, Metascape] -> stage not stated [Bioconductor, WGCNA]

### Unveiling the glymphatic system's role in brain aging: A comprehensive biomarker and modifiable intervention target. (PNAS 2026)

- DOI: 10.1073/pnas.2516601123 | PMCID: PMC13142974 | PMID: 42044335
- Evidence: Gene ontology (GO) enrichment analysis identified significant pathways (FDR-adjusted P < 0.05) through the Metascape web tool ( 63 ), with all human genes as the background.
- Full pipeline: quality control [PLINK] -> alignment/mapping [ANNOVAR] -> variant calling [PLINK] -> differential/statistical testing [FUMA, LightGBM, Metascape] -> machine learning [XGBoost]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: Metascape Analysis.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: GO analysis of DEGs was performed through Metascape ( https://metascape.org/ ) ( 47 ) and visualized with GraphPad Prism (Version 10.3.1).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Transcripts of repetitive DNA elements signal to block phagocytosis of hematopoietic stem cells. (Science 2024)

- DOI: 10.1126/science.adn1629 | PMCID: PMC12012832 | PMID: 39264994
- Evidence: Metascape ( 83 ) was used for pathway analysis.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [CellProfiler, Metascape, R]

