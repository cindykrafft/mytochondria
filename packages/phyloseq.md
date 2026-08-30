# phyloseq

- **Category:** microbiome
- **Papers in survey:** 31
- **Journals:** PNAS (17), Nature (11), Cell (3)
- **Years:** 2021 (4), 2022 (4), 2023 (10), 2024 (5), 2025 (5), 2026 (3)
- **Versions named:** 1.20 (1), 1.28.0 (1), 1.46 (1), 1.32.0 (1), 1.34.0 (1)
- **Pipeline stages it appears in:** visualisation (5), quantification (4), differential/statistical testing (3), dimensionality reduction/clustering (1)

## Papers

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **1.34.0**
- Evidence: ...ps://qiime2.org/ ITSx version 1.1b1 ( Bengtsson-Palme and Ryberg, 2013 https://microbiology.se/software/itsx/ R version 4.03 R CRAN www.r-project.org phyloseq 1.34.0 McMurdie and Holmes, 2013 https://bioconductor.org/packages/release/bioc/html/phyloseq.html caret 6.0-90 Kuhn, 2008 https://topepo.github.io/caret/ PRROC 1.3.1 Grau et al., 2015 https://cran.r-project.org/web/packages/PRROC/index.html...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: ...38/nmeth.3869 https://doi.org/10.18129/B9.bioc.dada2 Phlyoseq v1.30.090 https://doi.org/10.1371/journal.pone.0061217 https://doi.org/10.18129/B9.bioc.phyloseq eggNOG 5.0 https://doi.org/10.1093/nar/gky1085 https://github.com/eggnogdb/eggnog-mapper MUSCLE v5.1 https://doi.org/10.1038/s41467-022-34630-w https://www.drive5.com/muscle/ raxmlGUI 2.0 https://doi.org/10.1111/2041-210X.13512 https://anton...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Cervicovaginal microbiome and natural history of Chlamydia trachomatis in adolescents and young women. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.011 | PMCID: PMC12035847 | PMID: 39818212
- Evidence: In terms of microbial measures, α-diversity (i.e., Chao1 and Shannon indices) and β-diversity (Jensen Shannon divergence (JSD) distance) were calculated using the phyloseq package 48 in R.
- Full pipeline: quantification [DADA2] -> dimensionality reduction/clustering [DADA2] -> differential/statistical testing [DADA2, R, vegan] -> machine learning [DADA2] -> stage not stated [ggplot2, phyloseq]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: Relative abundances of bacterial OTUs were visualized with phyloseq 64 .
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Profiling the human intestinal environment under physiological conditions. (Nature 2023)

- DOI: 10.1038/s41586-023-05989-7 | PMCID: PMC10191855 | PMID: 37165188
- Evidence: Shannon diversity was calculated using the phyloseq::estimate_richness function, which is a wrapper for the vegan::diversity function 48 , 49 .
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DADA2, DESeq2, R, limma v3.48.3] -> stage not stated [Bowtie2 v2.4.1, HMMER, phyloseq]

### The dietary sweetener sucralose is a negative modulator of T cell-mediated responses. (Nature 2023)

- DOI: 10.1038/s41586-023-05801-6 | PMCID: PMC10033444 | PMID: 36922598
- Evidence: 45 ) with the phyloseq package 46 aggregating the count data to the genus level.
- Full pipeline: read trimming [Cutadapt v2.10, DADA2 v1.18] -> alignment/mapping [Cutadapt v2.10, RSEM v1.3.1] -> stage not stated [DESeq2 v1.30, R v4.0, STAR v2.7.6, phyloseq]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Evidence: Data were summarized as metagenomics operational taxonomic units (OTUs) into biom format and analysed with phyloseq and LEfSe (refs.
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **1.28.0**
- Evidence: A principal component analysis plot on Aitchison distance was produced with the ordinate and plot_ordination function in phyloseq (v1.28.0) 126 , using one randomly selected sample per individual ( n = 4,840 gut samples, n = 2,069 oral samples).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Airborne DNA reveals predictable spatial and seasonal dynamics of fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-07658-9 | PMCID: PMC11269176 | PMID: 38987593
- Evidence: We then computed the site-to-site community distance matrix using either the Bray–Curtis dissimilarity index (using the vegdist function of the R package vegan 70 ) or, alternatively, the unifrac distance (using the UniFrac function of the R package phyloseq 71 ) that accounted for taxonomic relatedness among the taxa.
- Full pipeline: read trimming [Cutadapt v4.2] -> differential/statistical testing [lme4] -> stage not stated [DADA2 v1.18.0, R, phyloseq]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Evidence: Microbial communities were further analysed using the microbiome 74 and phyloseq 75 packages.
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Microbial metabolite drives ageing-related clonal haematopoiesis via ALPK1. (Nature 2025)

- DOI: 10.1038/s41586-025-08938-8 | PMCID: PMC12137129 | PMID: 40269158
- Evidence: Microbiome communities in comparison groups were analysed using the R package phyloseq ( https://joey711.github.io/phyloseq/ ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [HISAT2] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, FastQC v0.11.8, R] -> stage not stated [MACS2, ggplot2, phyloseq]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Version used: **1.20**
- Evidence: Further analyses were performed using the phyloseq v.1.20 package in R Studio v.1.3.1093 ( https://bioconductor.org/packages/release/bioc/html/phyloseq.html ).
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: To illustrate the relative abundance of the most abundant phyla and families across core, indicator and specific ASVs, we computed ridgeline plots using ggridges 79 (v.0.5.4) and agglomerated ASVs at the genus level using tax_glom in the phyloseq 80 package (v.1.41.1).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Evidence: Downstream analysis was performed in R v.4.1.0 using tidyverse, phyloseq and vegan packages 75 .
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### An ancient antimicrobial protein co-opted by a fungal plant pathogen for in planta mycobiome manipulation. (PNAS 2021)

- DOI: 10.1073/pnas.2110968118 | PMCID: PMC8670511 | PMID: 34853168
- Evidence: The generated taxonomy table and abundance table were subsequently transformed into a phyloseq ( 66 ) object (version 1.30.0) in R (version 3.6.1) to facilitate analysis of the microbiomes.
- Full pipeline: alignment/mapping [HMMER, SAMtools] -> quantification [ImageJ, R v3.6.1, phyloseq] -> differential/statistical testing [DESeq2] -> visualisation [HMMER]

### No evidence for colonization of oral bacteria in the distal gut in healthy adults. (PNAS 2021)

- DOI: 10.1073/pnas.2114152118 | PMCID: PMC8594488 | PMID: 34610963
- Evidence: The ASV table was merged with relevant metadata into a phyloseq object for downstream analysis in R ( SI Appendix ).
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [BLAST] -> differential/statistical testing [R v3.4] -> stage not stated [DADA2, phyloseq]

### Human variation in gingival inflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2012578118 | PMCID: PMC8271746 | PMID: 34193520
- Evidence: Data were integrated into a single object using the “phyloseq” R package ( 63 ) and further analyzed ( SI Appendix , Supplementary Materials and Methods ).
- Full pipeline: differential/statistical testing [emmeans] -> stage not stated [DADA2, QIIME 2 v2018.2, R, phyloseq]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: The output of the DADA2 pipeline (feature table of amplicon sequence variants) was processed for alpha and beta diversity analysis using the phyloseq ( 50 ) and microbiomeSeq ( http://www.github.com/umerijaz/microbiomeSeq ) packages in R.
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Geological activity shapes the microbiome in deep-subsurface aquifers by advection. (PNAS 2022)

- DOI: 10.1073/pnas.2113985119 | PMCID: PMC9231496 | PMID: 35696589
- Evidence: Bioinformatics packages in R, including Dada2 ( 60 ) and phyloseq ( 61 ), were used to analyze the sequencing data.
- Full pipeline: read trimming [Cutadapt] -> quantification [R] -> stage not stated [phyloseq]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: All statistical analyses were performed and visualized in R ( http://www.R-project.org ) using the ggplot2 ( 80 ), genoPlotR ( 81 ), phyloseq ( 82 ), dunn.test ( 83 ), and vegan ( 84 ) packages.
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Integrated genomic and functional analyses of human skin-associated &lt;i&gt;Staphylococcus&lt;/i&gt; reveal extensive inter- and intra-species diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2310585120 | PMCID: PMC10666031 | PMID: 37956283
- Evidence: 16S rRNA amplicon (V1–V3) sequencing data were processed using the DADA2 pipeline version v1.2.0 ( 49 ) and downstream community analysis was carried out using phyloseq ( 50 ) in RStudio (R v4.2.0).
- Full pipeline: alignment/mapping [RAxML v1.1.0] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [DADA2, R v4.2, eggNOG, phyloseq]

### Bacterial tolerance to host-exuded specialized metabolites structures the maize root microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2310134120 | PMCID: PMC10622871 | PMID: 37878725
- Evidence: The following further R packages were used: Tidyverse ( 80 ), Broom ( 81 ), DECIPHER ( 82 ), DESeq2 ( 83 ), emmeans ( 84 ), ggthemes ( 85 ), multcomp ( 86 ), phyloseq ( 87 ), phytools ( 88 ), and vegan ( 89 ) in combination with some custom functions.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> stage not stated [DESeq2, R, RAxML v8.2.12, emmeans, phyloseq, phytools]

### Cooperation and cheating orchestrate Vibrio assemblages and polymicrobial synergy in oysters infected with OsHV-1 virus. (PNAS 2023)

- DOI: 10.1073/pnas.2305195120 | PMCID: PMC10556616 | PMID: 37751557
- Evidence: Original R statistic scripts for metagenomics analyses and the phyloseq table are available https://doi.org/10.5281/zenodo.7599486 .
- Full pipeline: quantification [DESeq2 v1.36.0] -> differential/statistical testing [phyloseq] -> structure determination [RAxML] -> stage not stated [DADA2 v1.14, QIIME 2]

### Ecoevolutionary processes structure milk microbiomes across the mammalian tree of life. (PNAS 2023)

- DOI: 10.1073/pnas.2218900120 | PMCID: PMC10334807 | PMID: 37399384
- Evidence: We built a phylogenetic tree using FastTree ( 63 ) in QIIME2 ( 64 ), and combined data files for further analysis using the phyloseq package ( 65 ).
- Full pipeline: stage not stated [QIIME 2, R v4.0.3, lavaan, phyloseq]

### Diversity of plant DNA in stool is linked to dietary quality, age, and household income. (PNAS 2023)

- DOI: 10.1073/pnas.2304441120 | PMCID: PMC10319039 | PMID: 37368926
- Version used: **1.32.0**
- Evidence: ASV count tables, taxonomic assignments, and metadata were organized using phyloseq v1.32.0 ( 74 ).
- Full pipeline: read trimming [QIIME 2] -> stage not stated [Cutadapt v3.4, DADA2 v1.10.0, phyloseq v1.32.0]

### &lt;i&gt;Trachymyrmex septentrionalis&lt;/i&gt; ants promote fungus garden hygiene using &lt;i&gt;Trichoderma&lt;/i&gt;-derived metabolite cues. (PNAS 2023)

- DOI: 10.1073/pnas.2219373120 | PMCID: PMC10288546 | PMID: 37319116
- Evidence: ASVs not classified at the phylum level (n = 20) were removed using Phyloseq’s subset_taxa() command and ASVs that were not present at ≥1% abundance in at least one sample (n = 381) were assigned as “Other” using the metagMisc v.0.04 ( https://github.com/vmikk/metagMisc ) command phyloseq_filter_sample_wise_abund_trim().
- Full pipeline: read trimming [DADA2 v1.16.0, Trimmomatic v0.39] -> quantification [phyloseq]

### Manipulating a host-native microbial strain compensates for low microbial diversity by increasing weight gain in a wild bird population. (PNAS 2024)

- DOI: 10.1073/pnas.2402352121 | PMCID: PMC11513901 | PMID: 39401350
- Evidence: Shannon and Chao1 diversity were estimated with phyloseq’s estimate_richness function.
- Full pipeline: visualisation [vegan] -> stage not stated [Bioconductor, DADA2, R, lme4, phyloseq]

### Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2303439121 | PMCID: PMC11317588 | PMID: 39093948
- Evidence: Subsequent processing, visualization, and statistical tests of sequence data were performed in R version 3.6.0 (R Core Team, 2020), primarily within the phyloseq package ( 42 ).
- Full pipeline: quantification [ImageJ v2.0.0] -> dimensionality reduction/clustering [vegan] -> differential/statistical testing [DESeq2, R v3.6.0, phyloseq, vegan] -> visualisation [Cytoscape, R v3.6.0, igraph, phyloseq] -> stage not stated [DADA2]

### Intergenerational protective anti-gut commensal immunoglobulin G originates in early life. (PNAS 2024)

- DOI: 10.1073/pnas.2309994121 | PMCID: PMC10990157 | PMID: 38517976
- Evidence: Taxonomic assignment and data visualization was performed in R v4.0.3 with phyloseq package v1.38.0 ( 49 ).
- Full pipeline: read trimming [Bowtie2 v2.4.1, MAFFT v7.475] -> alignment/mapping [Bowtie2 v2.4.1, MAFFT v7.475] -> dimensionality reduction/clustering [Docker] -> visualisation [R v4.0, phyloseq] -> stage not stated [BLAST, RAxML]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Version used: **1.46**
- Evidence: We imported the obtained ASV table and corresponding taxa table into phyloseq v 1.46 for downstream analyses and visualizations.
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

### Plant diversity influences plant volatile emission with varying effects at the species and community levels. (PNAS 2026)

- DOI: 10.1073/pnas.2518326123 | PMCID: PMC12818445 | PMID: 41538247
- Evidence: AMF diversity (Shannon diversity) was estimated with phyloseq ( 77 ) on rarefied data (2400 reads per sample).
- Full pipeline: differential/statistical testing [R v4.5.1, lme4, tidyverse] -> visualisation [ComplexHeatmap, R v4.5.1, ggplot2, pheatmap, tidyverse] -> stage not stated [mothur, phyloseq]

