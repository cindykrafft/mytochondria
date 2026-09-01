# Cytoscape

- **Category:** genomics
- **Papers in survey:** 178
- **Journals:** PNAS (111), Nature (41), Cell (22), Science (4)
- **Years:** 2021 (18), 2022 (38), 2023 (35), 2024 (28), 2025 (51), 2026 (8)
- **Versions named:** 3.9.1 (18), 3.7.2 (7), 3.7.1 (6), 3.10.1 (5), 3.8.0 (5), 3.8.2 (4), 3.9.0 (3), 3.8.1 (3), 3.10.0 (2), 3.8 (2)
- **Pipeline stages it appears in:** visualisation (92), dimensionality reduction/clustering (16), differential/statistical testing (12), alignment/mapping (2), normalisation (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: This regulon-regulon target network (along with its cluster labels and average enrichment per regulon) was exported as a weighted adjacency matrix for visualization in Cytoscape ( Shannon, 2003 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Microglia jointly degrade fibrillar alpha-synuclein cargo by distribution through tunneling nanotubes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.007 | PMCID: PMC8527836 | PMID: 34555357
- Evidence: Clusters were defined by the Cytoscape tool Wordcloud.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> dimensionality reduction/clustering [Cytoscape] -> stage not stated [CellProfiler, Fiji, ImageJ, ggplot2, tidyverse]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Version used: **3.8.1**
- Evidence: ...C CVCL-7927 VeroE6 ATCC CRL-1586 Oligonucleotides See Table S1 for ChIRP-MS Oligos N/A N/A Software and Algorithms R https://www.r-project.org/ R 3.6 Cytoscape https://cytoscape.org/ Cytoscape 3.8.1 Differential Enrichment analysis of Proteomics Data (DEP) https://rdrr.io/bioc/DEP/man/DEP.html DEP 1.10.0 DESeq2 https://bioconductor.org/packages/release/bioc/html/DESeq2.html DESeq2 1.28.1 DAVID Bio...
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Multi-organ proteomic landscape of COVID-19 autopsies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.004 | PMCID: PMC7794601 | PMID: 33503446
- Evidence: These 179 proteins formed 447 interactions according to String ( Szklarczyk et al., 2019 ) and Cytoscape ( Shannon et al., 2003 ) in our data ( Figure S5 ).
- Full pipeline: alignment/mapping [GSEA] -> differential/statistical testing [GSEA] -> stage not stated [Cytoscape, Metascape, R v3.6.1]

### Compromised SARS-CoV-2-specific placental antibody transfer. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.027 | PMCID: PMC7755577 | PMID: 33476549
- Version used: **3.8.0**
- Evidence: Correlations with coefficients > 0.75 and p value < 0.05 were inputted into Cytoscape (version 3.8.0) to produce correlation networks.
- Full pipeline: differential/statistical testing [Cytoscape v3.8.0] -> stage not stated [Bioconductor, CellProfiler, R v4.0.0]

### Genome-Scale Identification of SARS-CoV-2 and Pan-coronavirus Host Factor Networks. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.006 | PMCID: PMC7796900 | PMID: 33382968
- Evidence: ...entific-software/prism/ Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout (MAGeCK) Li et al., 2014 https://sourceforge.net/p/mageck/wiki/Home/ Cytoscape Shannon et al., 2003 https://cytoscape.org/ Seurat Stuart et al., 2019 https://satijalab.org/seurat/ Other Revolve inverted microscope ECHO https://discover-echo.com/revolve Resource Availability Lead Contact Further information and request...
- Full pipeline: differential/statistical testing [R] -> stage not stated [Cytoscape, STRING db, Seurat]

### Genetic Screens Identify Host Factors for SARS-CoV-2 and Common Cold Coronaviruses. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.004 | PMCID: PMC7723770 | PMID: 33333024
- Version used: **3.8.0**
- Evidence: .../mageck/wiki/Home R 3.6.0 R https://www.r-project.org FlowJo 10.6.1 FlowJo LLC N/A ChemiDoc MP Imaging System Bio-Rad N/A MATLAB R2020a MathWorks N/A Cytoscape 3.8.0 Cytoscape https://cytoscape.org GraphPad Prism 8 GraphPad N/A Sequencher 5.1 Gene Codes N/A CFX Maestro™ Software Bio-Rad Cat #12004110 Resource Availability Lead Contact Further information and requests for resources and reagents sho...
- Full pipeline: stage not stated [Cytoscape v3.8.0, R v3.6]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **3.8.1**
- Evidence: ...tor.org/packages/release/bioc/html/snm.html MATLAB version 2019b with the Statistics and Machine Learning Toolbox MathWorks https://www.mathworks.com Cytoscape 3.8.1 Shannon et al., 2003 https://cytoscape.org/ UNITE database (version 8, dynamic, sh_taxonomy_qiime_ver8_dynamic_04.02.2020.txt) Nilsson et al., 2019 https://unite.ut.ee/repository.php scikit-bio 0.5.6 N/A https://github.com/biocore/sci...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Evidence: Escape Networks Network plots were generated using the igraph package ( Csardi and Nepusz, 2006 ) and Cytoscape software 3.8.2 ( Shannon et al., 2003 ) with edges drawn between every pair of two amino acid sequences from ED 1 and 2, when the pair of sequences share a common mutation on amino acid level.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ...nder ( Kalyaanamoorthy et al., 2017 ) N/A iTOL https://itol.embl.de ( Letunic and Bork, 2021 ) v6 Diamond blastp ( Buchfink et al., 2021 ) v2.0.7.145 Cytoscape ( Shannon et al., 2003 ) v3.7.1 R (phylogeny) https://www.r-project.org/ v4.0.3 Phylogram ( Wilkinson and Davy, 2018 ) v2.1.0 Dendextend ( Galili, 2015 ) v1.15.1 R (statistics) https://www.r-project.org/ v4.1.0 BBmap (BBtools) ( Bushnell et...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...g.stats.ox.ac.uk/webapps/covabdab/ CyTOF Software v7.0 http://www.fluidigm.com/products-services/software CytoNorm ( Van Gassen et al., 2020 ) v0.0.5 Cytoscape ( Shannon et al., 2003 ) v3.8.0 Cytosplore ( van Unen et al., 2017 ) https://www.cytosplore.org/ demuxlet ( Kang et al., 2018 ) v2 https://github.com/statgen/demuxlet diffcyt ( Weber et al., 2019 ) v1.8.8 edgeR ( Robinson et al., 2010 ) v3....
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: ...Johnson, 2021 ) v0.2.10 https://akoyabio.github.io/phenoptrReports Prism (software) https://www.graphpad.com v9 FlowJo https://www.flowjo.com v10.6.1 Cytoscape https://www.cytoscape.org v3.7.1 ( Shannon et al., 2003 ) iRegulon ( Janky et al., 2014 ) v1.3 inForm Akoya Biosciences v2.4.8 BioRad CFX Maestro 1.0 Version 4.0.2325.0418 BioRad 2017 12004110 ZEN 3.0 black edition Carl Zeiss AG v3.0 Resour...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Limb development genes underlie variation in human fingerprint patterns. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.008 | PMCID: PMC8740935 | PMID: 34995520
- Evidence: ...ics ACCO1394 Medland et al., 2007 https://www.smiths.com/news-and-media/2005/07/smiths-heimann-biometrics-and-cross-match-technologies-to-join-forces Cytoscape Kohl et al., 2011 https://apps.cytoscape.org/ Resource availability Lead contact Further information and requests for resources should be directed to and will be fulfilled by the Lead Contact, Sijia Wang ( wangsijia@picb.ac.cn ).
- Full pipeline: stage not stated [Cytoscape, GCTA, IMPUTE2, ImageJ, PLINK v1.9, R v3.6, SHAPEIT]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: 59 https://msstats.org/ WGCNA Langfelder and Horvath 33 https://horvath.genetics.ucla.edu/html/CoexpressionNetwork/Rpackages/WGCNA/ Cytoscape Shannon et al.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### Apoptotic cell fragments locally activate tingible body macrophages in the germinal center. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.004 | PMCID: PMC7614509 | PMID: 36868219
- Version used: **3.9.1**
- Evidence: 85 https://www.gsea-msigdb.org/gsea M5.all.v0.3.symbols.gmt msigDB https://www.gsea-msigdb.org/gsea/msigdb Cytoscape 3.9.1 Stoeckius et al.
- Full pipeline: simulation/modelling [ggplot2] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, GSEA v4.2.3, ImageJ, Python v3.9, QuPath, R v4.1, Seurat, edgeR]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: 105 The Corona virus disease-related genes were then illustrated with Cytoscape (Version 3.8.2) 111 using the STRING protein query with a 0.8 confidence score cutoff.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### An atlas of human vector-borne microbe interactions reveals pathogenicity mechanisms. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.023 | PMCID: PMC11959484 | PMID: 38876107
- Evidence: The interactions with proteins enriched by two or more pathogen samples were also visualized using Cytoscape 117 .
- Full pipeline: dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [R]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Version used: **3.10.1**
- Evidence: 114 http://revigo.irb.hr/ Cytoscape v3.10.1 Shannon et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Multiscale proteomic modeling reveals protein networks driving Alzheimer's disease pathogenesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.038 | PMCID: PMC12851831 | PMID: 41005309
- Version used: **3.7.2**
- Evidence: Lastly, the AHNAK signaling map was visualized in Cytoscape (version 3.7.2).
- Full pipeline: quantification [GSEA, featureCounts v1.4.4] -> normalisation [GSEA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma] -> visualisation [Cytoscape v3.7.2] -> stage not stated [Bioconductor, R, Scanpy, Seurat, WGCNA]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: The resulting TF enrichment network was visualized in Cytoscape, revealing functional TF clusters with coordinated activity.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Encoding and decoding selectivity and promiscuity in the human chemokine-GPCR interaction network. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.046 | PMCID: PMC12435897 | PMID: 40273912
- Evidence: The chemokine-GPCR network representations were generated with Cytoscape.
- Full pipeline: alignment/mapping [ANNOVAR, MUSCLE, R] -> stage not stated [Cytoscape, PyMOL, TopHat]

### Global genetic interaction network of a human cell maps conserved principles and informs functional interpretation of gene co-essentiality profiles. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.044 | PMCID: PMC13281610 | PMID: 42049019
- Evidence: The core network was visualized using the “yFiles Organic” network layout in Cytoscape ( Data S10 ).
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, STAR] -> variant calling [GATK] -> visualisation [Cytoscape] -> stage not stated [ANNOVAR, R, SciPy]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Version used: **3.4.0**
- Evidence: Pathway Analysis Pathways ( Extended Data Fig.8h ) were obtained from REACTOME 62 , 63 . mRNA classes were mapped on pathways with Cytoscape 3.4.0.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### Discovery, structure and mechanism of a tetraether lipid synthase. (Nature 2022)

- DOI: 10.1038/s41586-022-05120-2 | PMCID: PMC9433317 | PMID: 35882349
- Evidence: All networks were visualized and edited in Cytoscape 62 .
- Full pipeline: structure determination [Coot] -> visualisation [Cytoscape, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Trans-vaccenic acid reprograms CD8&lt;sup&gt;+&lt;/sup&gt; T cells and anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06749-3 | PMCID: PMC10686835 | PMID: 37993715
- Evidence: The list of differentially expressed gene bodies was then submitted for GO enrichment and visualization, which was performed via the Gene Ontology project 18 , 19 and REVIGO 46 and Cytoscape 47 , respectively.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Cytoscape] -> visualisation [Cytoscape] -> stage not stated [DADA2, GSEA]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: Cytoscape software (v.3.7.2) was then used to visualize both intramodular and intermodular connectivity (edges), especially through the central hub TFs (nodes).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### The social and structural architecture of the yeast protein interactome. (Nature 2023)

- DOI: 10.1038/s41586-023-06739-5 | PMCID: PMC10700138 | PMID: 37968396
- Evidence: Networks were created and exported into Cytoscape 56 for further analysis and visualization strategies.
- Full pipeline: visualisation [ChimeraX v1.4, Cytoscape, Matplotlib, NumPy v1.20.3] -> stage not stated [AlphaFold, NetworkX v2.6.2, Python]

### Dopaminergic systems create reward seeking despite adverse consequences. (Nature 2023)

- DOI: 10.1038/s41586-023-06671-8 | PMCID: PMC10632144 | PMID: 37880370
- Version used: **3.9.1**
- Evidence: The connectivity map displaying the input network was generated using Cytoscape v3.9.1.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [ComplexHeatmap v1.10.2, Cytoscape v3.9.1]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **3.7.1**
- Evidence: ...k/impute/impute_v2.html ), dbSNP (v140, https://www.ncbi.nlm.nih.gov/SNP ), BiNGO (v3.0.3, https://www.psb.ugent.be/cbd/papers/BiNGO/Download.html ), Cytoscape (v3.7.1, https://cytoscape.org/download.html ), COLOC (v5.1.0.1, https://github.com/chr1swallace/coloc ).
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Version used: **3.7.0**
- Evidence: The networks were visualized using Cytoscape (v.3.7.0) 67 .
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: These factors were then plotted in relation to each other in Cytoscape.
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### A cytosolic surveillance mechanism activates the mitochondrial UPR. (Nature 2023)

- DOI: 10.1038/s41586-023-06142-0 | PMCID: PMC10284689 | PMID: 37286597
- Version used: **3.7.1**
- Evidence: GO enrichments were visualized with the EnrichmentMap (v.3.3.2) plug-in in Cytoscape (v.3.7.1).
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.7.1] -> stage not stated [DESeq2 v1.18.1, ImageJ v1.53, ggplot2 v3.3.3]

### Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer. (Nature 2023)

- DOI: 10.1038/s41586-023-05945-5 | PMCID: PMC10232371 | PMID: 37259003
- Version used: **3.9.1**
- Evidence: The resulting sequence similarity network of 696 nodes and 241,853 edges was then constructed and explored using the organic layout through Cytoscape (v3.9.1) 43 and visualized in R (v4.1.0) 44 .
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> structure determination [Coot] -> visualisation [Cytoscape v3.9.1, PyMOL, R v4.1.0] -> stage not stated [IQ-TREE v2.2.0.3]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Version used: **3.8**
- Evidence: Protein–protein interaction analysis Network figures were created using Cytoscape (v.3.8), with nodes corresponding to the gene name for proteins identified in the proteomic analysis.
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **3.8.2**
- Evidence: Random subsets consisting of the nodes and edges of 30% of the transcripts were fed into Cytoscape (v.3.8.2) 103 for network visualization (Supplementary Fig.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **3.7.2**
- Evidence: Network representation and clustering of GSEA results were performed using EnrichmentMap (v.3.2.1) 73 and AutoAnnotate (v.1.3.2) 74 for Cytoscape (v.3.7.2) 75 with the Jaccard coefficient set to 0.25.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Neuronal parts list and wiring diagram for a visual system. (Nature 2024)

- DOI: 10.1038/s41586-024-07981-1 | PMCID: PMC11446827 | PMID: 39358525
- Evidence: Layout We used Cytoscape 81 to draw the wiring diagrams.
- Full pipeline: stage not stated [Cytoscape]

### Neural circuit mechanisms underlying context-specific halting in Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07854-7 | PMCID: PMC11446846 | PMID: 39358520
- Evidence: Cytoscape 75 (v.3.10.0) was used to create all the wiring diagrams shown in this study.
- Full pipeline: dimensionality reduction/clustering [DeepLabCut v2.2.3] -> structure determination [DeepLabCut v2.2.3] -> stage not stated [Cytoscape, ImageJ, Python]

### Fibrin drives thromboinflammation and neuropathology in COVID-19. (Nature 2024)

- DOI: 10.1038/s41586-024-07873-4 | PMCID: PMC11424477 | PMID: 39198643
- Version used: **3.7.2**
- Evidence: The fibrin NK suppression network was generated using Cytoscape (v.3.7.2) 72 .
- Full pipeline: alignment/mapping [UCSF Chimera] -> quantification [Fiji] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [GSEA v4.2.3, edgeR, lme4 v1.1] -> stage not stated [Cytoscape v3.7.2, ImageJ v1.50, Jupyter, Python, scikit-image]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Version used: **3.9.0**
- Evidence: The interactome was created in Cytoscape (v.3.9.0) using the STRING database (v.11.5).
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Version used: **3.7.1**
- Evidence: Transcription factor networks were generated and visualized in Cytoscape v.3.7.1 (ref.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Evidence: Cytoscape 53 was used to perform network data integration and visualization.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Network of large pedigrees reveals social practices of Avar communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07312-4 | PMCID: PMC11078744 | PMID: 38658749
- Version used: **3.9.1**
- Evidence: We used Cytoscape v.3.9.1 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [BCFtools v1.3, Cytoscape v3.9.1, Picard, igraph]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **3.8.0**
- Evidence: On the same regulons, we constructed a regulatory network with the top 100 non-redundant edges of the network by importance score, and visualized the edges, transcription factors and target genes using Cytoscape (v.3.8.0) 70 .
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Version used: **3.8**
- Evidence: Protein networks and protein–protein interaction analysis Network figures were created using Cytoscape (v.3.8) with nodes corresponding to the gene name for proteins identified in the proteomic analysis.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Version used: **3.9.1**
- Evidence: 5g was created using yFiles Hierarchical layout in Cytoscape v3.9.1.
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### Stress response silencing by an E3 ligase mutated in neurodegeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06985-7 | PMCID: PMC10881396 | PMID: 38297121
- Evidence: To identify pathways enriched in the candidate genes, we took genes in the 5% top CasTLE score with a negative CasTLE Effect and ran Gene Ontology enrichment analysis (Cytoscape, ClueGO v.3.7.1).
- Full pipeline: alignment/mapping [kallisto v0.48.0] -> quantification [kallisto v0.48.0] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, Cytoscape, Galaxy v2.11.40.7]

### Nanobody-based recombinant antivenom for cobra, mamba and rinkhals bites. (Nature 2025)

- DOI: 10.1038/s41586-025-09661-0 | PMCID: PMC12629983 | PMID: 41162699
- Evidence: The obtained SSN was visualized with Cytoscape.
- Full pipeline: structure determination [PHENIX] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, PyMOL]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Version used: **2.9.0**
- Evidence: The network was visualized using Cytoscape (v2.9.0).
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Version used: **3.9.1**
- Evidence: Protein–metabolite edges were visualized with Cytoscape v.3.9.1 80 .
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: Generation of eGRNs The regulatory network output, with its transcription factors (eRegulons) and the targeted genes with enriched motifs, generated from the SCENIC+ analysis was imported into Cytoscape 70 for visualization (Supplementary Fig.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Deciphering phenylalanine-derived salicylic acid biosynthesis in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09280-9 | PMCID: PMC12408371 | PMID: 40702180
- Evidence: These genes were visualized around OsCNL1 using the Cytoscape software (v.3.7.2), with their distance to OsCNL1 reflecting the strength of co-expression.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> visualisation [Cytoscape] -> stage not stated [IQ-TREE, ImageJ v1.42q]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Version used: **3.10.1**
- Evidence: The core component of the network (that is, biggest module) was visualized using Cytoscape v3.10.1 (RRID:SCR_003032), and protein communities were detected by unsupervised edge-betweenness analysis (Fig.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **3.10.0**
- Evidence: Moreover, the R package KEGGREST (v.1.36.0) was used to extract KEGG pathway annotations, and Cytoscape (v.3.10.0) was used to construct network plots for the identified KEGG pathways.
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: ...hi Square test results Supplementary Table 7 Numeric data Supplementary Table 8 Sequences used in enSERT enhancer–reporter assay Supplementary Data 1 Cytoscape file showing interaction landscape of pioneer factors.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Evidence: Cell map toolkit and portal To enable interactive exploration of the human cell map, we developed the companion Multiscale Integrated Cell visualization portal (available at http://musicmaps.ai/u2os-cellmap/ ), which combines a high-performance graphical web interface with the general analysis functionality of the widely used Cytoscape application 49 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **3.5.10**
- Evidence: The resulting networks were imported and visualized using Cytoscape (v.3.5.10).
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **3.9.0**
- Evidence: Protein–protein interaction networks were constructed using STRINGdb (v.12) 56 , with a confidence threshold of >0.7, and the resulting networks were imported and visualized using Cytoscape (v.3.9.0).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: Network diagrams were graphed by Cytoscape 59 (v.3.10.1) and bubble plots were graphed by gglot2 package.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Version used: **3.9.1**
- Evidence: We used Cytoscape v3.9.1 ( https://cytoscape.org/ ) to visualize the graph.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: Apoptosis pathway visualization was performed using Cytoscape 60 (v3.8.2).
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Interactions with absolute coefficients exceeding 0.1 were visualized using Cytoscape 69 , and all identified regulatory interactions were included in our downstream analyses.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Chemical capture of diazo metabolites reveals biosynthetic hydrazone oxidation. (Nature 2026)

- DOI: 10.1038/s41586-025-10079-x | PMCID: PMC13061610 | PMID: 41639443
- Evidence: Results were visualized with Cytoscape 65 .
- Full pipeline: visualisation [Cytoscape] -> stage not stated [AlphaFold, BLAST, InterProScan, Prokka]

### Defective cytokinin signaling reprograms lipid and flavonoid gene-to-metabolite networks to mitigate high salinity in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2105021118 | PMCID: PMC8640937 | PMID: 34815339
- Evidence: A subnetwork of DEGs in a [( ahp2,3,5 -C + arr1,10,12 -C + ahp2,3,5 -S + arr1,10,12 -S)/4 − (WT-C + WT-S)/2] comparison was then obtained using igraph ( https://igraph.org ) and plotted using Cytoscape ( 99 ).
- Full pipeline: alignment/mapping [clusterProfiler] -> variant calling [ggplot2] -> dimensionality reduction/clustering [R v3.5, clusterProfiler] -> visualisation [Cytoscape, igraph]

### Functional genomics and metabolomics advance the ethnobotany of the Samoan traditional medicine "matalafi". (PNAS 2021)

- DOI: 10.1073/pnas.2100880118 | PMCID: PMC8609454 | PMID: 34725148
- Version used: **3.7.1**
- Evidence: Molecular networks were visualized with Cytoscape 3.7.1 ( 70 ).
- Full pipeline: visualisation [Cytoscape v3.7.1]

### Continuous variable responses and signal gating form kinetic bases for pulsatile insulin signaling and emergence of resistance. (PNAS 2021)

- DOI: 10.1073/pnas.2102560118 | PMCID: PMC8522282 | PMID: 34615716
- Evidence: Data Availability Cytoscape file data have been deposited in Network Data Exchange (NDEx).
- Full pipeline: stage not stated [Cytoscape]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: 2 B ) (download Cytoscape file from https://zenodo.org/record/4498884 ) ( 56 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### Genetic basis of variation in cocaine and methamphetamine consumption in outbred populations of <i>Drosophila melanogaster</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2104131118 | PMCID: PMC8201854 | PMID: 34074789
- Version used: **3.8.0**
- Evidence: All networks were visualized using Cytoscape 3.8.0.
- Full pipeline: alignment/mapping [GATK v2.4, Picard] -> registration [GATK v2.4, Picard] -> visualisation [Cytoscape v3.8.0]

### SIK2 orchestrates actin-dependent host response upon &lt;i&gt;Salmonella&lt;/i&gt; infection. (PNAS 2021)

- DOI: 10.1073/pnas.2024144118 | PMCID: PMC8126862 | PMID: 33947818
- Evidence: Identified genes were analyzed with Cytoscape with plugins for ReactomeFI, STRING, and OmicsVisualizer.
- Full pipeline: visualisation [Cytoscape]

### Anaerobic gut fungi are an untapped reservoir of natural products. (PNAS 2021)

- DOI: 10.1073/pnas.2019855118 | PMCID: PMC8106346 | PMID: 33906945
- Evidence: 6 and SI Appendix , Dataset S9 in GRAPHML format for visualization in Cytoscape ( 87 ).
- Full pipeline: alignment/mapping [AUGUSTUS, MAFFT] -> dimensionality reduction/clustering [BLAST] -> visualisation [Cytoscape] -> stage not stated [OrthoFinder, RAxML]

### TAp73 represses NF-κB-mediated recruitment of tumor-associated macrophages in breast cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2017089118 | PMCID: PMC7958209 | PMID: 33649219
- Evidence: ( E ) An enrichment map generated from GSEA results and visualized by Cytoscape EnrichmentMap and AutoAnnotate application, showing biological pathways enriched in TAp73 low versus TAp73 high.
- Full pipeline: visualisation [Cytoscape, GSEA]

### Primate innate immune responses to bacterial and viral pathogens reveals an evolutionary trade-off between strength and specificity. (PNAS 2021)

- DOI: 10.1073/pnas.2015855118 | PMCID: PMC8020666 | PMID: 33771921
- Version used: **3.7.2**
- Evidence: We conducted the functional characterization using GO enrichment implemented in the CluGO application (2.5.5) of Cytoscape (version 3.7.2) ( 60 ).
- Full pipeline: read trimming [Trim Galore v0.2.7] -> alignment/mapping [HTSeq] -> normalisation [limma] -> differential/statistical testing [R v3.6.2, limma] -> stage not stated [Cytoscape v3.7.2]

### Microbial dynamics of elevated carbon flux in the open ocean's abyss. (PNAS 2021)

- DOI: 10.1073/pnas.2018269118 | PMCID: PMC7848738 | PMID: 33479184
- Evidence: Visualization of the resulting modules and their correlation with carbon flux was performed using Cytoscape ( 80 ).
- Full pipeline: read trimming [SPAdes] -> alignment/mapping [SPAdes] -> structure determination [SPAdes, ggplot2, pheatmap] -> visualisation [Cytoscape, ggplot2, pheatmap] -> stage not stated [BWA v0.7.15, R, WGCNA]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Version used: **3.8.0**
- Evidence: The resulting network file was visualized and analyzed using Cytoscape v3.8.0 ( 117 ).
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### High-throughput functional annotation of natural products by integrated activity profiling. (PNAS 2022)

- DOI: 10.1073/pnas.2208458119 | PMCID: PMC9894231 | PMID: 36449542
- Evidence: Networks were visualized in Cytoscape ( 49 ) with edge lengths drawn using the Allegro Spring-Electric layout.
- Full pipeline: visualisation [Cytoscape] -> stage not stated [R]

### Integrated gene analyses of de novo variants from 46,612 trios with autism and developmental disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2203491119 | PMCID: PMC9674258 | PMID: 36350923
- Evidence: The PPI network was assessed using the STRING database with default settings and imported into Cytoscape for downstream analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [R v3.6.2] -> stage not stated [Cytoscape, GATK, STRING db, freebayes]

### Combination of common mtDNA variants results in mitochondrial dysfunction and a connective tissue dysregulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212417119 | PMCID: PMC9659340 | PMID: 36322731
- Evidence: ( A ) Cluster analysis from GSEA of RNAseq in mutant versus control cybrids using Cytoscape.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [R, limma] -> stage not stated [GSEA]

### Novel biochemical, structural, and systems insights into inflammatory signaling revealed by contextual interaction proteomics. (PNAS 2022)

- DOI: 10.1073/pnas.2117175119 | PMCID: PMC9546619 | PMID: 36179048
- Version used: **3.6.0**
- Evidence: S2 E , were generated using Cytoscape (v3.6.0) ( 44 ).
- Full pipeline: stage not stated [Cytoscape v3.6.0]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Version used: **3.8.2**
- Evidence: These results were visualized using Cytoscape (v3.8.2) software ( 96 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Super-enhancers conserved within placental mammals maintain stem cell pluripotency. (PNAS 2022)

- DOI: 10.1073/pnas.2204716119 | PMCID: PMC9546576 | PMID: 36161929
- Evidence: Protein–protein interaction analysis using Cytoscape revealed that complex interactions are likely to present among these 30 transcription factors ( Fig.
- Full pipeline: stage not stated [Cytoscape]

### Active forgetting requires Sickie function in a dedicated dopamine circuit in <i>Drosophila</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2204229119 | PMCID: PMC9499536 | PMID: 36095217
- Evidence: Markov clustering was performed with protein–protein interaction scores from the STRING database in Cytoscape.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [STRING db, Slingshot]

### A common vesicle proteome drives fungal biofilm development. (PNAS 2022)

- DOI: 10.1073/pnas.2211424119 | PMCID: PMC9501958 | PMID: 36095193
- Evidence: The obtained phenotypic outcomes were organized into visual Candida biofilm phenotypic networks using the Cytoscape platform ( 85 ).
- Full pipeline: stage not stated [Cytoscape]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: StringDB ( 48 ) and Cytoscape ( 49 ) were used in conjunction to generate an organically clustered interactome of functionally associated genes (StringDB, confidence >0.4).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Version used: **3.4.0**
- Evidence: By using Cytoscape version 3.4.0 ( 36 ), the highly connected genes of specific modules at each developmental stage were visually identified.
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### Distinct evolutionary trajectories of SARS-CoV-2-interacting proteins in bats and primates identify important host determinants of COVID-19. (PNAS 2022)

- DOI: 10.1073/pnas.2206610119 | PMCID: PMC9436378 | PMID: 35947637
- Evidence: Interactors of RIPK1 were retrieved using the Reactome Cytoscape Plugin ( 82 ).
- Full pipeline: stage not stated [BLAST, Cytoscape, Picard]

### Nuclear-localized, iron-bound superoxide dismutase-2 antagonizes epithelial lineage programs to promote stemness of breast cancer cells via a histone demethylase activity. (PNAS 2022)

- DOI: 10.1073/pnas.2110348119 | PMCID: PMC9303987 | PMID: 35858297
- Evidence: STRING network was generated using the list of DEGs uploaded to Cytoscape 3 against reference species ( Homo sapiens ) with confidence cutoff of 0.8 and zero additional interactions.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [edgeR] -> stage not stated [Cytoscape, GSEA, STRING db]

### Sequential rescue and repair of stalled and damaged ribosome by bacterial PrfH and RtcB. (PNAS 2022)

- DOI: 10.1073/pnas.2202464119 | PMCID: PMC9304027 | PMID: 35858322
- Evidence: The SSN file with 100% identification (e.g., 100% representative node) was displayed with Cytoscape ( 47 ) to produce the initial SSN.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [Cytoscape, MotionCor2]

### Blood-based untargeted metabolomics in relapsing-remitting multiple sclerosis revealed the testable therapeutic target. (PNAS 2022)

- DOI: 10.1073/pnas.2123265119 | PMCID: PMC9231486 | PMID: 35700359
- Evidence: Further, to identify and visualize the enriched metabolic pathways from dysregulated metabolites in RRMS, we employed Metscape, a plug-in for Cytoscape ( 16 ).
- Full pipeline: differential/statistical testing [Bioconductor, R] -> visualisation [Cytoscape]

### Vagus nerve stimulation promotes resolution of inflammation by a mechanism that involves Alox15 and requires the α7nAChR subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2023285119 | PMCID: PMC9295760 | PMID: 35622894
- Evidence: After normalizing concentrations (expressed as fold change from sham-treated mice), LM profiles were subjected to interaction network pathway analysis using Cytoscape ( https://cytoscape.org/ ).
- Full pipeline: normalisation [Cytoscape] -> differential/statistical testing [R, ggplot2] -> visualisation [R, ggplot2]

### MITF deficiency accelerates GNAQ-driven uveal melanoma. (PNAS 2022)

- DOI: 10.1073/pnas.2107006119 | PMCID: PMC9172632 | PMID: 35512098
- Evidence: ( B ) Cytoscape enrichment map shows GSEA c2cp_Reactome data sets that were significantly enriched (false discovery rate [FDR] q value < 0.05) in Qpm− (red) versus Qpm+ (blue).
- Full pipeline: quantification [QuPath] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2 v1.30.1, R v4.0.3] -> differential/statistical testing [Cytoscape] -> visualisation [GSEA]

### Genomewide CRISPR knockout screen identified PLAC8 as an essential factor for SADS-CoVs infection. (PNAS 2022)

- DOI: 10.1073/pnas.2118126119 | PMCID: PMC9170153 | PMID: 35476513
- Evidence: ( D ) Cytoscape EnrichmentMap of significantly enriched GO pathways as determined by g:Profiler.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [STAR v2.7.7a] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [R v4.0.3] -> stage not stated [Cytoscape, SAMtools v1.12, featureCounts]

### MoSBi: Automated signature mining for molecular stratification and subtyping. (PNAS 2022)

- DOI: 10.1073/pnas.2118210119 | PMCID: PMC9169782 | PMID: 35412913
- Evidence: Networks can be exported as graphML for compatibility with tools such as Cytoscape ( 42 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [Cytoscape, Docker, R]

### SARS-CoV-2 infection of airway cells causes intense viral and cell shedding, two spreading mechanisms affected by IL-13. (PNAS 2022)

- DOI: 10.1073/pnas.2119680119 | PMCID: PMC9169748 | PMID: 35353667
- Evidence: Gene set enrichment analysis was performed using GO gene sets, and related sets were visualized using Cytoscape.
- Full pipeline: quantification [ImageJ] -> visualisation [Cytoscape]

### Biochemical and structural characterization of an aromatic ring-hydroxylating dioxygenase for terephthalic acid catabolism. (PNAS 2022)

- DOI: 10.1073/pnas.2121426119 | PMCID: PMC9060491 | PMID: 35312352
- Evidence: An SSN of the family of proteins that the catalytic domain of TPADO belongs to (PF00848) was generated with EFI-EST web tools and visualized in Cytoscape.
- Full pipeline: visualisation [Cytoscape, PyMOL]

### Parkinson's disease and multiple system atrophy patient iPSC-derived oligodendrocytes exhibit alpha-synuclein-induced changes in maturation and immune reactive properties. (PNAS 2022)

- DOI: 10.1073/pnas.2111405119 | PMCID: PMC8944747 | PMID: 35294277
- Evidence: ( H ) Network analysis using Cytoscape for genes down-regulated in aSYN p.A53T O4 + OLCs allows identification of subnetworks, including the subnetwork “myelination.” ( I ) Representative images of adherent cultures stained for myelin binding protein (MBP).
- Full pipeline: differential/statistical testing [ggplot2 v3.3.0] -> stage not stated [ComplexHeatmap v2.4.3, Cytoscape, GSEA]

### Gain of gene regulatory network interconnectivity at the origin of vertebrates. (PNAS 2022)

- DOI: 10.1073/pnas.2114802119 | PMCID: PMC8931241 | PMID: 35263228
- Evidence: Cytoscape ( 31 ) networks were generated to better represent the connectivity of responsive genes.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq, STAR v2.5.3a, kallisto] -> differential/statistical testing [DESeq2 v1.18.0, R v3.4] -> stage not stated [Cytoscape]

### A multiomic study uncovers a bZIP23-PER1A-mediated detoxification pathway to enhance seed vigor in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2026355119 | PMCID: PMC8892333 | PMID: 35217598
- Version used: **3.6**
- Evidence: Metabolite–metabolite interaction network was predicted using MetaboAnalyst web service ( https://www.metaboanalyst.ca ) and visualized using Cytoscape 3.6.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [Cytoscape v3.6] -> stage not stated [R, featureCounts]

### Network modeling predicts personalized gene expression and drug responses in valve myofibroblasts cultured with patient sera. (PNAS 2022)

- DOI: 10.1073/pnas.2117323119 | PMCID: PMC8872767 | PMID: 35181609
- Evidence: All visualizations of network topology were constructed using Cytoscape ( 29 , 62 , 63 ).
- Full pipeline: visualisation [Cytoscape] -> stage not stated [NumPy]

### Distinguishing the molecular diversity, nutrient content, and energetic potential of exometabolomes produced by macroalgae and reef-building corals. (PNAS 2022)

- DOI: 10.1073/pnas.2110283119 | PMCID: PMC8812564 | PMID: 35101918
- Version used: **3.7**
- Evidence: Molecular networks were visualized in Cytoscape 3.7 ( 75 ).
- Full pipeline: differential/statistical testing [vegan] -> visualisation [Cytoscape v3.7]

### In situ proximity labeling identifies Lewy pathology molecular interactions in the human brain. (PNAS 2022)

- DOI: 10.1073/pnas.2114405119 | PMCID: PMC8812572 | PMID: 35082147
- Evidence: P value < 0.05) clustered into nodes representing similar pathways were visualized using Cytoscape and Enrichmentmap.
- Full pipeline: quantification [CellProfiler v3.1.5, ilastik v1.3.2] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Cytoscape] -> machine learning [ilastik v1.3.2] -> visualisation [Cytoscape] -> stage not stated [R v4.0.3]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: GO categories enrichment analysis was carried out for the list of up-regulated both_n genes and the list of down-regulated both_n genes using Bingo ( 24 ) in Cytoscape ( 67 ), with a false discovery rate (FDR)-adjusted P value cutoff of 0.05 and the list of genes in our tx2gene file as the universe.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Metabolomic selection for enhanced fruit flavor. (PNAS 2022)

- DOI: 10.1073/pnas.2115865119 | PMCID: PMC8860002 | PMID: 35131943
- Version used: **3.7.1**
- Evidence: The process assumed an unsigned network and the network was visualized and represented using Cytoscape 3.7.1 ( 52 ).
- Full pipeline: differential/statistical testing [XGBoost] -> machine learning [XGBoost] -> visualisation [Cytoscape v3.7.1] -> stage not stated [R, WGCNA]

### Differential interferon-α subtype induced immune signatures are associated with suppression of SARS-CoV-2 infection. (PNAS 2022)

- DOI: 10.1073/pnas.2111600119 | PMCID: PMC8872780 | PMID: 35131898
- Version used: **3.8.2**
- Evidence: Data visualization was done using R and Cytoscape (v.3.8.2).
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [Pangolin]

### Spatiotemporal analysis identifies ABF2 and ABF3 as key hubs of endodermal response to nitrate. (PNAS 2022)

- DOI: 10.1073/pnas.2107879119 | PMCID: PMC8794810 | PMID: 35046022
- Evidence: The resulting network was visualized using Cytoscape ( 77 ).
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEDTools, ImageJ, MACS2, R]

### USP16 is an ISG15 cross-reactive deubiquitinase that targets pro-ISG15 and ISGylated proteins involved in metabolism. (PNAS 2023)

- DOI: 10.1073/pnas.2315163120 | PMCID: PMC10722975 | PMID: 38055744
- Evidence: Cytoscape software was used to visualize the interaction network.
- Full pipeline: visualisation [Cytoscape]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Version used: **3.7.1**
- Evidence: The network graph of 350 genes was visualized with a radial plot using yFiles Layout Algorithms (version 1.1.2) and Cytoscape (version 3.7.1) ( http://www.cytoscape.org/ ).
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Massive intein content in &lt;i&gt;Anaeramoeba&lt;/i&gt; reveals aspects of intein mobility in eukaryotes. (PNAS 2023)

- DOI: 10.1073/pnas.2306381120 | PMCID: PMC10710043 | PMID: 38019867
- Evidence: The resulting network was visualized and edited with Cytoscape ( 57 ).
- Full pipeline: alignment/mapping [IQ-TREE, MUSCLE] -> structure determination [IQ-TREE] -> visualisation [Cytoscape] -> stage not stated [BLAST]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **3.9.1**
- Evidence: Finally, correlation networks between HERVs and selected genes have been generated by Cytoscape (v3.9.1) ( 47 ) for both CLL forms.
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Characteristics and anatomic location of PD-1<sup>+</sup>TCF1<sup>+</sup> stem-like CD8 T cells in chronic viral infection and cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2221985120 | PMCID: PMC10576122 | PMID: 37782797
- Evidence: ( D ) Cytoscape network analysis for identifying enriched Reactome pathways in each CD8 T cell subset.
- Full pipeline: stage not stated [Cytoscape, GSEA]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Evidence: The network map was created with Cytoscape based on the GSEA output of the GO analysis.
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### The mRNA stability factor Khd4 defines a specific mRNA regulon for membrane trafficking in the pathogen <i>Ustilago maydis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2301731120 | PMCID: PMC10450656 | PMID: 37590419
- Evidence: The GO term enrichment analysis was carried out using the R package gProfiler2 and visualized with the Cytoscape plugin, EnrichmentMap ( 77 , 78 ).
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape, R]

### The structural basis of hyperpromiscuity in a core combinatorial network of type II toxin-antitoxin and related phage defense systems. (PNAS 2023)

- DOI: 10.1073/pnas.2305393120 | PMCID: PMC10440598 | PMID: 37556498
- Version used: **3.5.0**
- Evidence: 5 ( 76 ) and with resulting networks visualized with Cytoscape v.
- Full pipeline: visualisation [Cytoscape v3.5.0] -> stage not stated [AlphaFold, Python]

### Pumping iron: A multi-omics analysis of two extremophilic algae reveals iron economy management. (PNAS 2023)

- DOI: 10.1073/pnas.2305495120 | PMCID: PMC10372677 | PMID: 37459532
- Version used: **3.4**
- Evidence: The networks were created in Cytoscape (v3.4) with the BLAST2SimilarityGraph plug-in and the yFiles Organic layout engine provided with Cytoscape.
- Full pipeline: alignment/mapping [BLAST] -> visualisation [PyMOL v1.7.4] -> stage not stated [ColabFold, Cytoscape v3.4, OrthoFinder v2.5.2]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: Logistic regression was applied to the binarized AUC scores to identify regulons with statistically significant changes in their activity after transplantation and Cytoscape ( 70 ) was used to visualize the regulons.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Discovery of phosphorylated lantibiotics with proimmune activity that regulate the oral microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2219392120 | PMCID: PMC10235938 | PMID: 37216534
- Version used: **3.9.1**
- Evidence: ( A ) Sequence similarity network (SSN) of the lanthionine dehydratase enzyme (SrnM-10) of strain S. salivarius SALI-10 in different bacterial phyla generated using the Enzyme Similarity Tool-Enzyme Function Initiative (EST-EFI, https://efi.igb.illinois.edu/efi-est/ ) and visualized in Cytoscape (v.3.9.1) with an alignment score threshold of 120 (∼30% sequence identity).
- Full pipeline: alignment/mapping [Cytoscape v3.9.1] -> visualisation [Cytoscape v3.9.1] -> stage not stated [Fiji, ImageJ]

### Architecture and genomic arrangement of the MurE-MurF bacterial cell wall biosynthesis complex. (PNAS 2023)

- DOI: 10.1073/pnas.2219540120 | PMCID: PMC10214165 | PMID: 37186837
- Evidence: Regarding the study of the distribution of major types of Mur chimeras in bacteria, SSN were generated for each type of Mur chimera using EFI-EST web [efi.igb.illinois.edu/efi-est/; ( 36 )] and were further analyzed using Cytoscape ( 37 ).
- Full pipeline: stage not stated [AlphaFold, Cytoscape]

### Branched germline cysts and female-specific cyst fragmentation facilitate oocyte determination in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2219683120 | PMCID: PMC10194012 | PMID: 37155904
- Evidence: Adjacency matrices describing the connectivity of the cells in cysts were created using Cytoscape, all remaining adjacency matrices were created manually.
- Full pipeline: stage not stated [Cytoscape]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Evidence: Data, Materials, and Software Availability Supplementary raw data are available at https://doi.org/10.6084/m9.figshare.21581355.v3 ( 39 ) and comprise: 1) AlphaFold structural predictions (.pdb) of MCP genes; 2) all MCP genes confirmed by HHpred or Alphafold (Fasta format); 3) Cytoscape network of MCP genes used in Fig.
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: Visualization of results was done through Cytoscape ( 24 ), and functional profiling was completed with g:Profiler ( 23 ) ( Fig.
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Version used: **3.7.2**
- Evidence: GO term enrichment analyses were performed using the App ClueGO v2.5.3 in Cytoscape 3.7.2 ( 75 ), with GO Term Fusion enabled to collapse terms containing very similar gene lists and using a custom background corresponding to expressed genes in the corresponding species as obtained from RNA-seq results of the corresponding input samples of the meRIP experiments.
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Characterization of a unique polysaccharide monooxygenase from the plant pathogen <i>Magnaporthe oryzae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2215426120 | PMCID: PMC9974505 | PMID: 36791100
- Evidence: The clusters of sequences were visualized in Cytoscape ( 83 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, Cytoscape] -> visualisation [Clustal Omega, Cytoscape] -> stage not stated [AlphaFold, ColabFold, ImageJ, R]

### Mitochondrial control of microglial phagocytosis by the translocator protein and hexokinase 2 in Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2209177120 | PMCID: PMC9974442 | PMID: 36787364
- Evidence: Network and functional enrichment analysis of identified candidate interactors was carried out using Cytoscape ( 72 ), InTact ( 73 ), and StringApp plugins version 3.8 ( 74 ).
- Full pipeline: differential/statistical testing [Bioconductor, R] -> stage not stated [Cytoscape]

### Bioprosthetic heart valve structural degeneration associated with metabolic syndrome: Mitigation with polyoxazoline modification. (PNAS 2023)

- DOI: 10.1073/pnas.2219054120 | PMCID: PMC9910464 | PMID: 36574676
- Version used: **3.9.1**
- Evidence: Protein–protein interaction and functional enrichment analysis were carried out via open-source bioinformatics software with filtered proteins (significance, P < 0.05 [permutation-based FDR correction] and 0.58 log2FC), using string-db v11.5 ( www.string-db.org ), ( 55 , 56 ) and visualized with Cytoscape v3.9.1 ( www.cytoscape.org ) ( 57 ) and DisGeNET app ( www.disgenet.org ) ( 58 ).
- Full pipeline: dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [Cytoscape v3.9.1] -> visualisation [Bioconductor, Cytoscape v3.9.1] -> stage not stated [GSEA]

### Cold-blooded vertebrate utilizes behavioral fever to alleviate T cell apoptosis and optimize antimicrobial immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2408969121 | PMCID: PMC11670090 | PMID: 39680767
- Evidence: ( B ) Interaction network of immune-related genes constructed by Cytoscape software, n = 4.
- Full pipeline: stage not stated [Cytoscape, GSEA]

### YkuR functions as a protein deacetylase in &lt;i&gt;Streptococcus mutans&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407820121 | PMCID: PMC11474102 | PMID: 39356671
- Version used: **3.10.1**
- Evidence: Subsequently, we characterized 21 highly interconnected networks using combining cluster analysis of the molecular complex detection (MCODE) module in Cytoscape v3.10.1 ( Dataset S4 ).
- Full pipeline: dimensionality reduction/clustering [Cytoscape v3.10.1]

### Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2303439121 | PMCID: PMC11317588 | PMID: 39093948
- Evidence: We used the igraph package ( 51 ) for correlation calculations, network construction, and topology analysis, and Cytoscape ( 52 ) for visualization.
- Full pipeline: quantification [ImageJ v2.0.0] -> dimensionality reduction/clustering [vegan] -> differential/statistical testing [DESeq2, R v3.6.0, phyloseq, vegan] -> visualisation [Cytoscape, R v3.6.0, igraph, phyloseq] -> stage not stated [DADA2]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Version used: **3.7.2**
- Evidence: Modules of interest were exported to Cytoscape v3.7.2 ( 97 ) for visualization, and NetworkAnalyzer ( 98 ) was used to calculate network topological parameters.
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### Nitrogen and sulfur for phosphorus: Lipidome adaptation of anaerobic sulfate-reducing bacteria in phosphorus-deprived conditions. (PNAS 2024)

- DOI: 10.1073/pnas.2400711121 | PMCID: PMC11181052 | PMID: 38833476
- Version used: **3.9.1**
- Evidence: The resulting molecular networks were visualized using Cytoscape version 3.9.1 ( 71 , 72 ).
- Full pipeline: visualisation [Cytoscape v3.9.1] -> stage not stated [ggplot2, pheatmap]

### ZmPILS6 is an auxin efflux carrier required for maize root morphogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2313216121 | PMCID: PMC11145266 | PMID: 38781209
- Version used: **3.9.1**
- Evidence: Visualization of the ZmPILS6 coexpression network ( Dataset S6 ) was visualized in Cytoscape version 3.9.1 using the organic layout.
- Full pipeline: variant calling [R] -> dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.9.1, R] -> stage not stated [ImageJ, WGCNA]

### SRSF1 interactome determined by proximity labeling reveals direct interaction with spliceosomal RNA helicase DDX23. (PNAS 2024)

- DOI: 10.1073/pnas.2322974121 | PMCID: PMC11126954 | PMID: 38743621
- Evidence: ( H ) Protein-network visualization generated with Cytoscape and STRING database, derived from the 190 proteins in common between BS and SB datasets.
- Full pipeline: visualisation [Cytoscape, STRING db] -> stage not stated [AlphaFold]

### Identification of secretory autophagy as a mechanism modulating activity-induced synaptic remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2315958121 | PMCID: PMC11032469 | PMID: 38588427
- Evidence: Cytoscape was used to display functional pathway analysis results.
- Full pipeline: stage not stated [Cytoscape]

### Activation of ERβ hijacks the splicing machinery to trigger R-loop formation in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2306814121 | PMCID: PMC10990146 | PMID: 38513102
- Evidence: ( D ) GO modules for the BP in the MDA-MB-231 cell line were visualized using EnrichmentMap in Cytoscape.
- Full pipeline: visualisation [Cytoscape] -> stage not stated [ImageJ, STRING db]

### Dinickel enzyme evolved to metabolize the pharmaceutical metformin and its implications for wastewater and human microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2312652121 | PMCID: PMC10927577 | PMID: 38408229
- Evidence: Cytoscape was used to visualize the clustering in the SSN and identify the clusters containing MfmA and MfmB sequences ( 67 ).
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> structure determination [CCP4] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, AutoDock Vina]

### A macrophage-collagen fragment axis mediates subcutaneous adipose tissue remodeling in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2313185121 | PMCID: PMC10861897 | PMID: 38300872
- Evidence: Analysis was done in Cytoscape with GO:Biological process database.
- Full pipeline: stage not stated [Cytoscape, ImageJ]

### Viruses traverse the human proteome through peptide interfaces that can be biomimetically leveraged for drug discovery. (PNAS 2024)

- DOI: 10.1073/pnas.2308776121 | PMCID: PMC10835127 | PMID: 38252831
- Evidence: Networks are visualized with Cytoscape ( 45 ) using a force-directed layout.
- Full pipeline: differential/statistical testing [R] -> visualisation [Cytoscape] -> stage not stated [igraph]

### BRCA1 and ELK-1 regulate neural progenitor cell fate in the optic tectum in response to visual experience in <i>Xenopus laevis</i> tadpoles. (PNAS 2024)

- DOI: 10.1073/pnas.2316542121 | PMCID: PMC10801852 | PMID: 38198524
- Evidence: We used STRING and Cytoscape to identify protein–protein interaction networks among DE transcripts.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, Cufflinks, Cytoscape, ImageJ]

### Native metabolomics identifies pteridines as CutA ligands and modulators of copper binding. (PNAS 2025)

- DOI: 10.1073/pnas.2509468122 | PMCID: PMC12685090 | PMID: 41289401
- Evidence: Feature-based molecular networking results were screened and visualized in Cytoscape ( 72 ), and statistical analyses were carried out using the Statistical Analysis of Feature-Based Molecular Networking script ( 73 ) or the associated web application ( https://fbmn-statsguide.gnps2.org ).
- Full pipeline: differential/statistical testing [Cytoscape, Python] -> visualisation [ChimeraX, Cytoscape]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Version used: **3.9.0**
- Evidence: Coexpression of relevant genes was visualized in Cytoscape (v3.9.0) ( 95 ).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### A cytoplasmic motif in HLA-E that drives clathrin-mediated endocytosis and VCP-associated postendocytic trafficking. (PNAS 2025)

- DOI: 10.1073/pnas.2514956122 | PMCID: PMC12582296 | PMID: 41134633
- Version used: **3.10.1**
- Evidence: PPI networks were constructed based on these parameters using Cytoscape 3.10.1 and were finalized in Adobe Illustrator.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [STRING db] -> stage not stated [Cytoscape v3.10.1, PHENIX]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Evidence: Transporters with the top 15 highest and bottom 15 lowest correlation values were connected to corresponding compounds and visualized in the network using Cytoscape ( 45 ).
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### Single-cell sequencing uncovers sensory neuron-mediated CGRP signaling as a driver of sarcoma progression. (PNAS 2025)

- DOI: 10.1073/pnas.2500161122 | PMCID: PMC12582254 | PMID: 41118222
- Evidence: Network of enriched GO terms and Reactome pathways generated with g:Profiler and EnrichmentMap using Cytoscape among ( D ), tumor cells implanted in TrkA WT mice, and ( E ) TME cells from TrkA WT mice.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [CellChat, Cytoscape]

### Gene age shapes functional and evolutionary properties of the &lt;i&gt;Drosophila&lt;/i&gt; seminal fluid proteome. (PNAS 2025)

- DOI: 10.1073/pnas.2505490122 | PMCID: PMC12541329 | PMID: 41055975
- Version used: **3.10**
- Evidence: The PPI network was visualized with Cytoscape v3.10 ( 55 ).
- Full pipeline: visualisation [Cytoscape v3.10] -> stage not stated [R]

### Combined pesticide pollution enhances the dissemination of the phage-encoded antibiotic resistome in the soil under nitrogen deposition. (PNAS 2025)

- DOI: 10.1073/pnas.2516722122 | PMCID: PMC12519213 | PMID: 41042849
- Version used: **3.10.0**
- Evidence: Viral shared networks constructed by vConTACT3 were visualized using Cytoscape (v3.10.0) ( 91 ).
- Full pipeline: read trimming [fastp v0.22.08] -> alignment/mapping [BLAST] -> visualisation [Cytoscape v3.10.0] -> stage not stated [HMMER v3.1b, R v4.0.3, eggNOG, vegan]

### 12/15-lipoxygenase orchestrates murine wound healing via PPARγ-activating oxylipins acting holistically to dampen inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2502640122 | PMCID: PMC12435204 | PMID: 40906806
- Evidence: Genes that were found to be significantly differentially expressed at Day 7 were analyzed in Cytoscape, using their expression levels for the entire time-course, with correlation [r] > 0.8 shown.
- Full pipeline: differential/statistical testing [Cytoscape]

### Blood-labyrinth barrier damage mediated by granzymes from cytotoxic lymphocytes results in hearing loss in systemic lupus erythematosus. (PNAS 2025)

- DOI: 10.1073/pnas.2423240122 | PMCID: PMC12377648 | PMID: 40794837
- Evidence: Using DEGs with a log fold change (logFC) > 0.75, we constructed a protein–protein association network based on the STRING database ( 35 ) and identified the hub genes using maximal clique centrality (MCC), a network scoring method in Cytoscape ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cytoscape, GSVA, STRING db]

### C11orf54 catalyzes L-xylulose formation in human metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2506597122 | PMCID: PMC12337341 | PMID: 40737316
- Version used: **3.9.1**
- Evidence: Cytoscape 3.9.1 was used to generate protein interaction networks.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.3] -> visualisation [Clustal Omega v1.2.3] -> stage not stated [AutoDock Vina v1.2.5, Cytoscape v3.9.1, PyMOL v2.5.0]

### Ciprofloxacin-driven purifying selection on viral genomes accelerates soil N&lt;sub&gt;2&lt;/sub&gt;O production. (PNAS 2025)

- DOI: 10.1073/pnas.2503199122 | PMCID: PMC12304974 | PMID: 40668828
- Version used: **3.7.2**
- Evidence: Virus–MAG networks were visualized using Cytoscape v3.7.2.
- Full pipeline: read trimming [fastp] -> visualisation [Cytoscape v3.7.2] -> stage not stated [BLAST v2.12.0, R v4.3.1, eggNOG, ggplot2, pheatmap]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Version used: **3.9.1**
- Evidence: We used the ClueGO (v.2.5.9) Cytoscape (v.3.9.1) module to explore the enrichment of ontology terms for which the response to DENV infection significantly correlated with ancestry.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### Identification of a VPS29 isoform with restricted association to Retriever and Retromer accessory proteins through autoinhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2501111122 | PMCID: PMC12260524 | PMID: 40587794
- Version used: **3.3**
- Evidence: Protein–protein interaction network analysis was performed using Metascape 3.5 ( 81 ) and visualized using Cytoscape 3.3 software with the Enrichment Map plug-in ( 82 ).
- Full pipeline: alignment/mapping [ChimeraX v1.6.1, PyMOL] -> differential/statistical testing [R] -> machine learning [AlphaFold, ColabFold] -> visualisation [ChimeraX v1.6.1, Cytoscape v3.3, Metascape v3.5, PyMOL] -> stage not stated [IQ-TREE v2.2.5]

### A transcriptomic, proteomic, and functional genetic atlas dissects neurofibromin function in the peripheral nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2506823122 | PMCID: PMC12260521 | PMID: 40587782
- Evidence: Visualization was performed in Cytoscape with additional connections included from the STRING database ( 42 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> visualisation [Cytoscape, STRING db]

### Metabolic control of glycosylation forms for establishing glycan-dependent protein interaction networks. (PNAS 2025)

- DOI: 10.1073/pnas.2422936122 | PMCID: PMC12207472 | PMID: 40531880
- Version used: **3.9.1**
- Evidence: The total interaction network and all subnetworks were visualized using Cytoscape (v.3.9.1) ( 43 ).
- Full pipeline: dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.9.1] -> stage not stated [AlphaFold, ComplexHeatmap, STRING db]

### The oncogene SLC35F2 is a high-specificity transporter for the micronutrients queuine and queuosine. (PNAS 2025)

- DOI: 10.1073/pnas.2425364122 | PMCID: PMC12207525 | PMID: 40526720
- Version used: **3.10.1**
- Evidence: SSNs were generated using the Enzyme Function Initiative (EFI) analytic suite ( 57 ) and visualized using Cytoscape (3.10.1) ( 58 ).
- Full pipeline: read trimming [MUSCLE v5.2] -> alignment/mapping [AlphaFold, MUSCLE v5.2] -> quantification [ImageJ] -> visualisation [Cytoscape v3.10.1]

### Enzymatic carbon-fluorine bond cleavage by human gut microbes. (PNAS 2025)

- DOI: 10.1073/pnas.2504122122 | PMCID: PMC12184663 | PMID: 40512801
- Evidence: We visualized the 95% amino acid identity representative network using Cytoscape ( 66 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R] -> simulation/modelling [AlphaFold, GROMACS] -> visualisation [Cytoscape] -> stage not stated [ColabFold, IQ-TREE]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: The TFs with significant variability were identified by chromVAR from JASPAR database, and their interaction networks were constructed via STRING website and visualized in Cytoscape ( 68 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Identification of the lydiamycin biosynthetic gene cluster in a plant pathogen guides structural revision and identification of molecular target. (PNAS 2025)

- DOI: 10.1073/pnas.2424388122 | PMCID: PMC12130866 | PMID: 40388608
- Version used: **3.8.2**
- Evidence: The resulting samples were subjected to LC–MS/MS analysis using a Waters Acquity UHPLC coupled to a Q-Exactive Orbitrap Mass Spectrometer (Thermo). mzML format data were used to create molecular networks with GNPS ( 83 ), which were visualized using Cytoscape 3.8.2 ( 84 ).
- Full pipeline: alignment/mapping [ChimeraX v1.5, Clustal Omega, RAxML] -> visualisation [Cytoscape v3.8.2] -> stage not stated [ColabFold v1.2]

### The SIK3-N783Y mutation is associated with the human natural short sleep trait. (PNAS 2025)

- DOI: 10.1073/pnas.2500356122 | PMCID: PMC12088394 | PMID: 40324078
- Evidence: Network analysis was performed in Cytoscape ( 45 ) (v3.10.3) using SIGNOR App( 29 ) (v1.2).
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> machine learning [SnpEff] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Cytoscape, ImageJ]

### Bacterial extracellular vesicles target different bacterial species, impairing cell division and diminishing their pathogenicity. (PNAS 2025)

- DOI: 10.1073/pnas.2416652122 | PMCID: PMC12067206 | PMID: 40299696
- Evidence: To analyze the overrepresentation of a functional class of DEGs, we performed gene ontology (GO) functional enrichment analysis using Cytoscape plug-in ClueGO v2.5.10 ( 60 ) with a custom annotation database as a reference dataset.
- Full pipeline: differential/statistical testing [R, edgeR] -> stage not stated [Cytoscape, ImageJ]

### A disease-specific convergence of host and Epstein-Barr virus genetics in multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418783122 | PMCID: PMC12002260 | PMID: 40184175
- Version used: **3.9.1**
- Evidence: The resultant network was imported in Cytoscape v.3.9.1 ( 72 ).
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [Cytoscape v3.9.1, R v1.1.456, VEP]

### Modulation of host gene expression by the zinc finger antiviral protein. (PNAS 2025)

- DOI: 10.1073/pnas.2420819122 | PMCID: PMC12002351 | PMID: 40146858
- Evidence: Network plots were produced using Cytoscape ( 51 ).
- Full pipeline: alignment/mapping [DESeq2, STAR] -> differential/statistical testing [DESeq2, STAR] -> visualisation [ggplot2] -> stage not stated [Cytoscape]

### An atlas of protein phosphorylation dynamics during interferon signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2412990122 | PMCID: PMC12002234 | PMID: 40138345
- Version used: **3.9**
- Evidence: Protein networks were created with STRING ( 18 ) and annotated in Cytoscape 3.9 ( 55 ).
- Full pipeline: stage not stated [Cytoscape v3.9]

### Comprehensive mutant chemotyping reveals embedding of a lineage-specific biosynthetic gene cluster in wider plant metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2417588122 | PMCID: PMC11962460 | PMID: 40106352
- Version used: **3.5.1**
- Evidence: Network data were visualized and cropped in Cytoscape v3.5.1 ( 45 ) ( http://www.cytoscape.org/ ) to select the avenacin-related cluster and to remove nodes with the same molecular weights (isomers).
- Full pipeline: dimensionality reduction/clustering [Cytoscape v3.5.1] -> visualisation [Cytoscape v3.5.1]

### Logic-based machine learning predicts how escitalopram attenuates cardiomyocyte hypertrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2420499122 | PMCID: PMC11912418 | PMID: 40035765
- Evidence: LogiRx identified top scoring directed pathways from drug targets to the hypertrophy signaling network nodes through OmniPath directed interactions ( 22 , 23 ) using the PathLinker algorithm ( 24 , 25 ) in Cytoscape ( 26 ) ( Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [CellProfiler, Cytoscape]

### Ancient genomes reveal trans-Eurasian connections between the European Huns and the Xiongnu Empire. (PNAS 2025)

- DOI: 10.1073/pnas.2418485122 | PMCID: PMC11892651 | PMID: 39993190
- Version used: **3.9.1**
- Evidence: We used Cytoscape v3.9.1 ( 103 ) to plot the networks of pairwise IBD relations.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [Cytoscape v3.9.1, Picard]

### Extensive location bias of the GPCR-dependent translatome via site-selective activation of mTOR. (PNAS 2025)

- DOI: 10.1073/pnas.2414738122 | PMCID: PMC11874449 | PMID: 39964727
- Evidence: Protein interaction matrices were generated by String-DB ( 52 ) and analyzed in Cytoscape ( 53 ).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v3.16] -> stage not stated [Cytoscape, R]

### Ancient origin and high diversity of zymocin-like killer toxins in the budding yeast subphylum. (PNAS 2025)

- DOI: 10.1073/pnas.2419860122 | PMCID: PMC11848437 | PMID: 39928860
- Evidence: 6 ) was done using Cytoscape ( 43 ).
- Full pipeline: read trimming [SPAdes v3.14] -> alignment/mapping [STAR] -> stage not stated [Cytoscape]

### Natural variations in <i>TT8</i> and its neighboring <i>STK</i> confer yellow seed with elevated oil content in <i>Brassica juncea</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2417264122 | PMCID: PMC11804580 | PMID: 39883846
- Evidence: Network visualization for each module was carried out using the Cytoscape software version 3.6 ( 95 ).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12] -> differential/statistical testing [GEMMA] -> visualisation [Cytoscape] -> stage not stated [BUSCO, R, VCFtools, WGCNA, minimap2 v2.17]

### Epstein-Barr virus BALF0/1 subverts the Caveolin and ERAD pathways to target B cell receptor complexes for degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2400167122 | PMCID: PMC11789056 | PMID: 39847318
- Version used: **3.8.1**
- Evidence: Cytoscape version 3.8.1 was used to construct protein–protein interaction networks.
- Full pipeline: stage not stated [AlphaFold, Cytoscape v3.8.1, ImageJ]

### The single-stranded DNA-binding factor SUB1/PC4 alleviates replication stress at telomeres and is a vulnerability of ALT cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2419712122 | PMCID: PMC11745411 | PMID: 39772744
- Evidence: ( E ) Interactome of top 100 SUB1/PC4 codependent genes created using STRINGdb [medium confidence setting (0.4)] and Cytoscape for network formatting.
- Full pipeline: stage not stated [CellProfiler, Cytoscape, ImageJ, STRING db]

### Electron transfer in polysaccharide monooxygenase catalysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411229121 | PMCID: PMC11725913 | PMID: 39793048
- Evidence: The clusters of sequences were visualized using Cytoscape ( 43 ).
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, Clustal Omega]

### Experimental evolution of cellular miniaturization reveals a putative mechanism for cell size evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2531280123 | PMCID: PMC13273275 | PMID: 42284327
- Evidence: ( C ) Interaction network of mutations detected in S1–S3 evolved populations curated in Cytoscape ( 63 ).
- Full pipeline: stage not stated [Cytoscape, STRING db]

### Impact of sex chromosomes and gonad type in stress susceptibility in corticostriatal brain regions. (PNAS 2026)

- DOI: 10.1073/pnas.2531920123 | PMCID: PMC13229181 | PMID: 42189975
- Version used: **3.10.3**
- Evidence: Pathway overrepresentation through Metascape was used to identify biological processes that were most impacted by stress exposure, with all expressed transcripts used as the background reference set ( 75 ) and networks were visualized using Cytoscape 3.10.3.
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.10.3, Metascape] -> stage not stated [Bioconductor, WGCNA]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: The network was clustered using the k-means algorithm into three distinct clusters: BLOC and HPS complexes (green), Rab and VPS proteins (red), and AP complexes (blue) and visualized using Cytoscape ( 71 ).
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Proteome-wide prediction of interactions between structured domains and peptide motifs reveals functionally coherent subnetworks. (PNAS 2026)

- DOI: 10.1073/pnas.2527957123 | PMCID: PMC13080015 | PMID: 41941631
- Evidence: The GLay community clustering algorithm ( 43 ) as implemented in Cytoscape ( 42 ) was used to cluster the network obtained from the PrePPI-SLiM human predictions with FPR ≤ 0.001.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [AlphaFold, HMMER, Python, R, STRING db, scikit-learn]

### Pharmaco-behavioral profiling identifies suppressors of autism gene-associated phenotypes in zebrafish. (PNAS 2026)

- DOI: 10.1073/pnas.2518846123 | PMCID: PMC13012064 | PMID: 41838920
- Evidence: ( E ) Rescued DEGs in scn1lab Δ44/Δ44 (green) and dyrk1aa Δ77/Δ77 dyrk1ab Δ8/Δ8 (magenta) mutants and LEVO targets (cyan) in the fatty acid metabolic process pathway (GO: 0006631), visualized using Cytoscape ( 37 ).
- Full pipeline: differential/statistical testing [STRING db] -> visualisation [Cytoscape]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: We used the Cytoscape software (v3.9.1) to visualize clusters.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Version used: **3.9.1**
- Evidence: The network was visualized using Cytoscape v.3.9.1 organic layout ( 91 ).
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Evidence: We then identified potential transmission events as isolates from the same clone sampled from different patients that differed by 26 SNPs or fewer, visualised using Cytoscape.
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

### Comparative connectomics of two distantly related nematode species reveals patterns of nervous system evolution. (Science 2025)

- DOI: 10.1126/science.adx2143 | PMCID: PMC12330220 | PMID: 40743352
- Evidence: Display layouts of complete networks were made using Cytoscape ( 43 ).
- Full pipeline: quantification [SciPy] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Cytoscape]

