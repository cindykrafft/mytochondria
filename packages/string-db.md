# STRING db

- **Category:** genomics
- **Papers in survey:** 90
- **Journals:** PNAS (57), Nature (25), Cell (6), Science (2)
- **Years:** 2021 (4), 2022 (11), 2023 (17), 2024 (20), 2025 (25), 2026 (13)
- **Versions named:** 11.5 (3), 12.0 (2), 81.7 (1)
- **Pipeline stages it appears in:** visualisation (6), dimensionality reduction/clustering (5), differential/statistical testing (5)

## Papers

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: In order to visualize morphogen pathway interactions and their modules, we downloaded high confidence interactions from STRING database ( Szklarczyk et al., 2019 ) (version 11.0) for the morphogens.
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Genome-Scale Identification of SARS-CoV-2 and Pan-coronavirus Host Factor Networks. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.006 | PMCID: PMC7796900 | PMID: 33382968
- Evidence: For construction of the network in Figure 3 , significant CRISPR hits from any virus were searched using the STRING database ( https://string-db.org ; Szklarczyk et al., 2019 ) using default parameters and imported into Cytoscape ( Shannon et al., 2003 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [Cytoscape, STRING db, Seurat]

### The proteomic landscape of synaptic diversity across brain regions and cell types. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.028 | PMCID: PMC10686415 | PMID: 37918396
- Evidence: 34 http://mips.helmholtz-muenchen.de/corum/ STRING database Szklarczyk et al.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Cytoscape, R v4.2, STRING db, WGCNA]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Version used: **11.5**
- Evidence: We used the STRING database v11.5 71 to identify known and predicted protein–protein interactions among this set of 75 genes.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### Molecular and cellular mechanisms of teneurin signaling in synaptic partner matching. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.022 | PMCID: PMC11833509 | PMID: 38996528
- Evidence: Functional enrichment analyses, including Gene Ontology, protein domain (SMART), reactome pathway, and local network cluster, were performed on these gene sets using the STRING database.
- Full pipeline: quantification [R] -> dimensionality reduction/clustering [STRING db] -> differential/statistical testing [limma] -> visualisation [R] -> stage not stated [ImageJ]

### The essential host genome for Cryptosporidium survival exposes metabolic dependencies that can be leveraged for treatment. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.001 | PMCID: PMC7618951 | PMID: 40706591
- Version used: **12.0**
- Evidence: We functionally characterised these genes using the STRING database (v 12.0), and discovered a majority belonged to critical cellular components such as the ribosome, proteasome, and cell cycle regulators ( Figures S1M and S1N ).
- Full pipeline: quality control [FastQC, ImageJ v2.1.0, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [PHENIX, STRING db v12.0]

### Chaperone-mediated autophagy sustains haematopoietic stem-cell function. (Nature 2021)

- DOI: 10.1038/s41586-020-03129-z | PMCID: PMC8428053 | PMID: 33442062
- Evidence: Allocation of proteins to functional groups was done using the IPA software (Ingenuity Systems) and STRING database ( https://string-db.org/ ).
- Full pipeline: stage not stated [STRING db]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: This method identified three main groups of TFs, each of which was analysed with STRINGdb 105 to identify significantly overrepresented pathways.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Evidence: The STRINGdb R package v.2.6.1 (ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: Protein–protein interaction networks were generated using the STRING database 74 .
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Evidence: External data sources URLs for external data used are as follows: the GWAS catalogue ( https://www.ebi.ac.uk/gwas/ ), the GTEx project ( https://gtexportal.org/home/ ), the Human Protein Atlas ( https://www.proteinatlas.org/ ), STRING database ( https://string-db.org/ ; file name: 9606.protein.actions.v11.txt.gz) and UniProt ( https://www.uniprot.org/ ).
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: STRING database interactions were filtered to include affinity purification–MS validations.
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: A gene interaction network was first built by querying the STRING database with GATA2 target genes, then pruned to only keep genes reported as associated with GATA2.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Evidence: STRING was used to identify putative biological processes by searching for interactions on the basis of the closest-related genes for fungi found in the STRING database 46 .
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Membrane prewetting by condensates promotes tight-junction belt formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07726-0 | PMCID: PMC11324514 | PMID: 39112699
- Version used: **11.5**
- Evidence: The interactome was created in Cytoscape (v.3.9.0) using the STRING database (v.11.5).
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [R] -> stage not stated [Cellpose, Cytoscape v3.9.0, Jupyter v7.3.10, STRING db v11.5, ggplot2]

### NBS1 lactylation is required for efficient DNA repair and chemotherapy resistance. (Nature 2024)

- DOI: 10.1038/s41586-024-07620-9 | PMCID: PMC11254748 | PMID: 38961290
- Evidence: ...des and proteins in lactylation proteome. c , Protein-protein interaction network analysis of the DNA damage repair-related Kla proteins based on the STRING database. d , Dose-response curves for cisplatin in AGS-P and AGS-sh-NBS1 cells treated with or without lactate (20 mM) (Left).
- Full pipeline: quantification [ImageJ] -> stage not stated [STRING db]

### Natural proteome diversity links aneuploidy tolerance to protein turnover. (Nature 2024)

- DOI: 10.1038/s41586-024-07442-9 | PMCID: PMC11153158 | PMID: 38778096
- Evidence: For assessment of the protein properties on attenuation, the following sources were used: macromolecular-complex membership: Complex Portal of the EBI (accessed December 2020) 73 ; protein–protein interactions (PPIs): STRING database (accessed November 2022) 74 ; prediction of protein disorder and linear interacting peptides by AlphaFold, MobiDB and anchor: MobiDB (accessed October 2022) 75 ; GC c...
- Full pipeline: read trimming [edgeR] -> quantification [R, edgeR] -> normalisation [edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold, GSEA, STRING db, data.table]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Edges represent putative interactions from the STRING database. g , Bar graphs show the functional enrichment analysis of all 78 proteins using ‘Biological process’, “Cellular component”, and “Molecular function” terms from Enrichr.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **11.5**
- Evidence: Moreover, the mouse protein–protein interaction (PPI) network was integrated from the STRING database (v.11.5) 60 , with a focus on interactions having a combined score above 900.
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08885-4 | PMCID: PMC12158776 | PMID: 40240610
- Evidence: Interaction networks were calculated with STRING database at standard settings 51 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, scikit-learn] -> differential/statistical testing [GSEA, limma] -> stage not stated [Cellpose v2.0, STRING db]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Evidence: ...uent panels (cosine similarity function). b) Distribution of similarities shown for protein pairs with a ‘high-confidence interaction’ denoted in the STRING database (green) in comparison to all other protein pairs (grey). c) Similar to (b) but for protein pairs in the same CORUM complex. d) Similar to (b) but for protein pairs that yield highly similar transcriptional profiles (top 1% pairs) when...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Evidence: PPI networks were constructed using STRINGdb (v.12) 51 , with a confidence threshold greater than 0.7.
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Evidence: Protein–protein interaction networks were constructed using STRINGdb (v.12) 56 , with a confidence threshold of >0.7, and the resulting networks were imported and visualized using Cytoscape (v.3.9.0).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: In-community edges are marked by reduced saturation. b , Benchmark of concordance of inferred TF–TF interactions using different methods with physical interactions from the STRING database.
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: Visualization was performed in Cytoscape with additional connections included from the STRING database 65 .
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Evidence: Clustering was performed using MCL clustering in the STRING database, and top functional annotations were extracted from STRING. b , Histogram showing expression distributions of candidate Vemurafenib-resistant genes in wild-type A375 cells.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Evidence: Bioinformatics TF interaction networks were generated using STRING database 82 , with the default setting of medium confidence.
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### Thymic health and immunotherapy outcomes in patients with cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10243-x | PMCID: PMC13102699 | PMID: 41851467
- Evidence: Enrichment analysis used the STRINGdb package (v.2.6.0), with proteins from the filtered Olink panel as background.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> stage not stated [STRING db]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **12.0**
- Evidence: Protein–protein association data was obtained from the STRING database (v.12.0) and integrated to analyse both functional and physical interactions using curated datasets and high-throughput experimental evidence.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Evidence: Functional interactions and protein-protein interactions for high confidence candidate regulators were identified using the STRING database using STRING v.12.0 40 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: The predicted functional interaction network of CCN1 was generated using the STRING database 53 (Extended Data Fig.
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### A membrane protein display platform for receptor interactome discovery. (PNAS 2021)

- DOI: 10.1073/pnas.2025451118 | PMCID: PMC8488672 | PMID: 34531301
- Evidence: Protein specific information was retrieved from the STRING database ( https://string-db.org/ ).
- Full pipeline: stage not stated [STRING db]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Evidence: PPI enrichment analysis was performed using STRING database ( 36 ) with the options of “version = 11, species = 9,606, score_threshold = 700”.
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### Integrated gene analyses of de novo variants from 46,612 trios with autism and developmental disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2203491119 | PMCID: PMC9674258 | PMID: 36350923
- Evidence: The PPI network was assessed using the STRING database with default settings and imported into Cytoscape for downstream analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [R v3.6.2] -> stage not stated [Cytoscape, GATK, STRING db, freebayes]

### Cooperation loci are more pleiotropic than private loci in the bacterium <i>Pseudomonas aeruginosa</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214827119 | PMCID: PMC9564939 | PMID: 36191234
- Evidence: As measures of pleiotropy, I used the number of protein interactions contained in the STRING database ( 13 ), the number of biological process Gene Ontology (GO) terms ( 14 ), and gene expression pleiotropy for each locus with available data ( Fig.
- Full pipeline: stage not stated [STRING db]

### Active forgetting requires Sickie function in a dedicated dopamine circuit in <i>Drosophila</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2204229119 | PMCID: PMC9499536 | PMID: 36095217
- Evidence: ( C ) Top five biological processes (gene ontology) associated with the 215 MS candidates predicted by the STRING database. “Strength” denotes the ratio between the number of proteins in the network that are annotated with a term and the number of proteins that the database expected to be annotated with this term in a random network of the same size.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [STRING db, Slingshot]

### Nuclear-localized, iron-bound superoxide dismutase-2 antagonizes epithelial lineage programs to promote stemness of breast cancer cells via a histone demethylase activity. (PNAS 2022)

- DOI: 10.1073/pnas.2110348119 | PMCID: PMC9303987 | PMID: 35858297
- Evidence: ( F ) Protein–protein interaction network analysis of NLS-SOD2 up-regulated genes based on STRING database. n = 4.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [edgeR] -> stage not stated [Cytoscape, GSEA, STRING db]

### Activating STING1-dependent immune signaling in <i>TP53</i> mutant and wild-type acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2123227119 | PMCID: PMC9271208 | PMID: 35759659
- Evidence: To examine the connection between immune signaling and HR in AML, we used the STRING database and computational tool ( 46 ) to perform network analysis for known protein interactions between targets of interest.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [ggpubr] -> stage not stated [GSEA, R, STRING db, fgsea]

### Integrated screens uncover a cell surface tumor suppressor gene <i>KIRREL</i> involved in Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2121779119 | PMCID: PMC9231494 | PMID: 35704761
- Evidence: The curated KIRREL -related genes from ( D ) (correlation factor > 0.3 or < −0.3) were constructed into one network using the STRING database ( https://string-db.org/ ).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.3a] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [STRING db]

### Protective role of chaperone-mediated autophagy against atherosclerosis. (PNAS 2022)

- DOI: 10.1073/pnas.2121133119 | PMCID: PMC9168839 | PMID: 35363568
- Evidence: Gene set enrichment analysis (with the STRING database) further showed up-regulation of nodes related to cell migration, proliferation, differentiation, and response to lipids ( SI Appendix , Fig.
- Full pipeline: stage not stated [STRING db]

### Proteome-wide cellular thermal shift assay reveals unexpected cross-talk between brassinosteroid and auxin signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2118220119 | PMCID: PMC8931322 | PMID: 35254915
- Evidence: S6 ) according to the STRING database ( 29 ).
- Full pipeline: stage not stated [STRING db]

### Multiomic prediction of therapeutic targets for human diseases associated with protein phase separation. (PNAS 2023)

- DOI: 10.1073/pnas.2300215120 | PMCID: PMC10556643 | PMID: 37774095
- Evidence: Interactions in the STRING database that documents disease-related physical interactions ( 79 ) (with confidence score ≥ 700) were used to calculate Hill-transformed ( 80 ) betweenness centrality ( 81 , 82 ) scores for each PPS-prone disease-associated proteins in the significantly differentially expressed pathways identified above.
- Full pipeline: differential/statistical testing [STRING db] -> stage not stated [PHENIX]

### Contrastive learning in protein language space predicts interactions between drugs and protein targets. (PNAS 2023)

- DOI: 10.1073/pnas.2220778120 | PMCID: PMC10268324 | PMID: 37289807
- Evidence: Human protein sequences were taken from the STRING database and processed following ref.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [PyTorch v1.11, STRING db]

### The role of genetic selection and climatic factors in the dispersal of anatomically modern humans out of Africa. (PNAS 2023)

- DOI: 10.1073/pnas.2213061120 | PMCID: PMC10235988 | PMID: 37220274
- Evidence: Evaluation of coherent biological functionality among the candidate gene sets was performed using standard enrichment tests of predefined functional and biomedical annotations on the STRING database ( 64 ) ( SI Appendix , section 3.8 ).
- Full pipeline: stage not stated [STRING db]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: The protein interaction network of related differentially expressed genes was analyzed using the STRING database V11.5 ( 55 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Consequences of poly(ethylene oxide) and poloxamer P188 on transcription in healthy and stressed myoblasts. (PNAS 2023)

- DOI: 10.1073/pnas.2219885120 | PMCID: PMC10161009 | PMID: 37094151
- Evidence: To assess connectivity of the network, the 192 genes in the STRING database that exhibited ≥twofold modulation in expression upon short-term exposure to osmotic stress were evaluated in STRING.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [GSEA, STRING db]

### Cross-linking mass spectrometry discovers, evaluates, and corroborates structures and protein-protein interactions in the human cell. (PNAS 2023)

- DOI: 10.1073/pnas.2219418120 | PMCID: PMC10151615 | PMID: 37071682
- Evidence: Second, 191 of the remaining novel PPIs were predicted with at least medium confidence by the STRING database (combined score of at least 0.4) ( 43 ), which integrates information across multiple lines of evidence including known interactions curated for homologous protein pairs, gene and protein coexpression, and literature text-mining.
- Full pipeline: differential/statistical testing [AlphaFold] -> stage not stated [STRING db]

### Loss of regulation of protein synthesis and turnover underpins an attenuated stress response in senescent human mesenchymal stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2210745120 | PMCID: PMC10083568 | PMID: 36989307
- Evidence: Using the highest-confidence PPI data taken from the STRING database ( 33 ), we performed modularity analysis ( 34 ) on the Brehme et al. chaperome to subdivide it into deeply interconnected modules ( SI Appendix , Fig.
- Full pipeline: stage not stated [STRING db]

### Single-nuclei RNA sequencing (snRNA-seq) uncovers trophoblast cell types and lineages in the mature bovine placenta. (PNAS 2023)

- DOI: 10.1073/pnas.2221526120 | PMCID: PMC10041116 | PMID: 36913592
- Evidence: Previously described interactions between transcription factors were also queried in the STRING database ( 45 ) and all transcription factors had at least one known interaction with another transcription factor that were derived from curated databases and/or experimentally determined ( SI Appendix , Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, Slingshot] -> stage not stated [STRING db]

### Larger cerebral cortex is genetically correlated with greater frontal area and dorsal thickness. (PNAS 2023)

- DOI: 10.1073/pnas.2214834120 | PMCID: PMC10089183 | PMID: 36893272
- Evidence: We harnessed data from a protein–protein interaction network or “interactome” present in the STRING database ( 21 ) and define genetic modules based on the premise that protein products of genes that are associated with a particular trait tend to interact with each other and converge on related biological and functional networks, rather than being randomly spread throughout the interactome ( 20 , ...
- Full pipeline: quality control [PLINK] -> alignment/mapping [MAGMA] -> dimensionality reduction/clustering [GCTA] -> differential/statistical testing [GCTA] -> visualisation [Cytoscape] -> stage not stated [FUMA, FreeSurfer v5.3, LDSC, STRING db]

### The SET oncoprotein promotes estrogen-induced transcription by facilitating establishment of active chromatin. (PNAS 2023)

- DOI: 10.1073/pnas.2206878120 | PMCID: PMC9974495 | PMID: 36791099
- Evidence: The STRING database, which includes known and predicted protein–protein interactions, suggests that SET can interact with several members of the condensin complex, including SMC2, SMC4, NCAPG, and NCAPH2 ( SI Appendix , Fig.
- Full pipeline: stage not stated [STRING db]

### Multimodal epigenetic changes and altered NEUROD1 chromatin binding in the mouse hippocampus underlie FOXG1 syndrome. (PNAS 2023)

- DOI: 10.1073/pnas.2122467120 | PMCID: PMC9926245 | PMID: 36598943
- Evidence: STRING database ( 49 ) was used to explore known and predicted protein–protein interactions of FOXG1 in Mus musculus .
- Full pipeline: stage not stated [Python, STRING db]

### Machine learning reveals the transcriptional regulatory network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC 7942. (PNAS 2024)

- DOI: 10.1073/pnas.2410492121 | PMCID: PMC11420160 | PMID: 39269777
- Evidence: In fact, Synpcc7942_1090 clusters with photosystem proteins by the predictions of the STRING database and Synpcc7942_0551 with photosystem proteins, RNA polymerase, and sigma factors ( 32 ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore, featureCounts] -> read trimming [FastQC, Trim Galore] -> quantification [MultiQC, featureCounts] -> dimensionality reduction/clustering [STRING db] -> stage not stated [scikit-learn]

### Structural color in the bacterial domain: The ecogenomics of a 2-dimensional optical phenotype. (PNAS 2024)

- DOI: 10.1073/pnas.2309757121 | PMCID: PMC11260094 | PMID: 38990940
- Evidence: To predict functional associations between the genes, most of which were annotated as hypothetical proteins, we uploaded the protein sequences of the orthologs selected by the pan-GWAS approach to the STRING database, which integrates diverse sources of evidence for functional interactions between proteins ( 30 ).
- Full pipeline: stage not stated [STRING db]

### MACSPI enables tissue-selective proteomic and interactomic analyses in multicellular organisms. (PNAS 2024)

- DOI: 10.1073/pnas.2319060121 | PMCID: PMC11126916 | PMID: 38753516
- Version used: **81.7**
- Evidence: In fact, based on the information in the STRING database, 81.7% of proteins in our PPI network interact with HSP90 either directly or indirectly through binding partners ( SI Appendix , Fig.
- Full pipeline: stage not stated [STRING db v81.7]

### Synergistic induction of blood-brain barrier properties. (PNAS 2024)

- DOI: 10.1073/pnas.2316006121 | PMCID: PMC11126970 | PMID: 38748577
- Evidence: Bioinformatic analyses using the STRING database revealed a network of interactions between the effector transcription factors of cAMP, Wnt, and TGF-β pathways, with β-catenin taking center stage ( Fig.
- Full pipeline: stage not stated [STRING db]

### SRSF1 interactome determined by proximity labeling reveals direct interaction with spliceosomal RNA helicase DDX23. (PNAS 2024)

- DOI: 10.1073/pnas.2322974121 | PMCID: PMC11126954 | PMID: 38743621
- Evidence: ( H ) Protein-network visualization generated with Cytoscape and STRING database, derived from the 190 proteins in common between BS and SB datasets.
- Full pipeline: visualisation [Cytoscape, STRING db] -> stage not stated [AlphaFold]

### ZEPPI: Proteome-scale sequence-based evaluation of protein-protein interaction models. (PNAS 2024)

- DOI: 10.1073/pnas.2400260121 | PMCID: PMC11127014 | PMID: 38743624
- Evidence: Note that Interactome3D also includes homology-modeled PPIs and the STRING database has many inferred PPIs, which are not determined by direct physical interaction experiments but inferred by other methods such as gene-related methods or species PPI transfer.
- Full pipeline: alignment/mapping [RoseTTAFold] -> stage not stated [AlphaFold, STRING db]

### Activation of ERβ hijacks the splicing machinery to trigger R-loop formation in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2306814121 | PMCID: PMC10990146 | PMID: 38513102
- Evidence: Furthermore, we obtained the protein–protein interaction (PPI) networks from the STRING database ( 23 ) and found that U2 small nuclear RNA auxiliary factor 1 (U2AF1) was one of the core proteins involved in RNA splicing pathway, which had the strongest interactions with proteins of this pathway ( Fig.
- Full pipeline: visualisation [Cytoscape] -> stage not stated [ImageJ, STRING db]

### Dual topologies of myotomal collagen XV and Tenascin C act in concert to guide and shape developing motor axons. (PNAS 2024)

- DOI: 10.1073/pnas.2314588121 | PMCID: PMC10990108 | PMID: 38502691
- Evidence: ( B ) Protein–protein interaction network analysis of the total core matrisome genes expressed by SMPs with STRING database.
- Full pipeline: alignment/mapping [UMAP] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [STRING db]

### Mutations of the circadian clock genes &lt;i&gt;Cry&lt;/i&gt;, &lt;i&gt;Per,&lt;/i&gt; or &lt;i&gt;Bmal1&lt;/i&gt; have different effects on the transcribed and nontranscribed strands of cycling genes. (PNAS 2024)

- DOI: 10.1073/pnas.2316731121 | PMCID: PMC10895256 | PMID: 38359290
- Evidence: Guided by the protein–protein interaction network in the STRING database ( 45 ), we constructed a network ( Fig.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2] -> stage not stated [STRING db]

### KAT8-catalyzed lactylation promotes eEF1A2-mediated protein synthesis and colorectal carcinogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2314128121 | PMCID: PMC10895275 | PMID: 38359291
- Evidence: ( E ) Protein–protein interaction network of differentially lactylated proteins between CRC tumor and adjacent normal tissues based on the STRING database.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [STRING db] -> stage not stated [AlphaFold]

### Intracellular C3 protects β-cells from IL-1β-driven cytotoxicity via interaction with Fyn-related kinase. (PNAS 2024)

- DOI: 10.1073/pnas.2312621121 | PMCID: PMC10895342 | PMID: 38346191
- Evidence: Searching the STRING database for FRK predicted functional partners also revealed C3 ( Fig.
- Full pipeline: stage not stated [ImageJ, STRING db, ilastik]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: To construct the protein–protein interaction network, we used protein network data from the STRING database with the file name “9606.protein.physical.links.detailed.v11.5.txt”.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### A conserved hub protein required for peptidoglycan remodeling and cell division in &lt;i&gt;Acinetobacter baumannii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2529815122 | PMCID: PMC12772221 | PMID: 41428879
- Evidence: The STRING database ( 72 ) revealed that wthA had synteny with lolB that was widespread in γ- and β-Proteobacteria as well as Bacteroidota.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [STRING db]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Evidence: To identify functional relationships between upregulated genes following miRNA inhibition, protein–protein interaction networks were constructed using the STRING database [v12.0; ( 44 )].
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### A cytoplasmic motif in HLA-E that drives clathrin-mediated endocytosis and VCP-associated postendocytic trafficking. (PNAS 2025)

- DOI: 10.1073/pnas.2514956122 | PMCID: PMC12582296 | PMID: 41134633
- Evidence: ( D ) Protein–protein interaction networks from the STRING database (confidence cutoff 0.9) for proteins most significantly enriched in HLA-E-APEX2 (red) or HLA-A3-APEX2 (blue) experiments (FDR < 0.05 and FC ≥ 1).
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [STRING db] -> stage not stated [Cytoscape v3.10.1, PHENIX]

### Autoimmunity-associated DIORA1 binds the MRCK family of serine/threonine kinases and controls cell motility. (PNAS 2025)

- DOI: 10.1073/pnas.2426917122 | PMCID: PMC12519202 | PMID: 41042840
- Evidence: To visualize the DIORA1 interaction network, an unadjusted STRINGdb ( 16 ) interaction map was generated using DIORA1 and the BioID hits MRCKA, MRCKB, CEP55, and WASHC5 as seed proteins ( SI Appendix , Fig.
- Full pipeline: visualisation [STRING db] -> stage not stated [AlphaFold, DESeq2, GSEA, UCSF Chimera]

### Blood-labyrinth barrier damage mediated by granzymes from cytotoxic lymphocytes results in hearing loss in systemic lupus erythematosus. (PNAS 2025)

- DOI: 10.1073/pnas.2423240122 | PMCID: PMC12377648 | PMID: 40794837
- Evidence: Using DEGs with a log fold change (logFC) > 0.75, we constructed a protein–protein association network based on the STRING database ( 35 ) and identified the hub genes using maximal clique centrality (MCC), a network scoring method in Cytoscape ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cytoscape, GSVA, STRING db]

### Split-YFP-coupled interaction-dependent TurboID identifies new functions of basal cell polarity in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2502445122 | PMCID: PMC12358837 | PMID: 40768356
- Evidence: ( F ) Markov clustering of the 49 enriched proteins based on protein–protein interaction scores from the STRING database.
- Full pipeline: dimensionality reduction/clustering [STRING db] -> stage not stated [ImageJ, tidyverse]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: Protein interaction networks were generated using the STRING database ( https://string-db.org ).
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### The pathogenic factor of ZC4H2-associated rare disorder is a postsynaptic regulator for synaptic activity and cognitive function. (PNAS 2025)

- DOI: 10.1073/pnas.2426375122 | PMCID: PMC12280958 | PMID: 40632560
- Evidence: To further examine functional associations, protein–protein interaction networks were constructed using the STRING database ( 29 ).
- Full pipeline: stage not stated [STRING db]

### Human milk IgA promotes normal immune development by limiting Th17-inducing <i>Erysipelatoclostridium ramosum</i> in the infant gut. (PNAS 2025)

- DOI: 10.1073/pnas.2501030122 | PMCID: PMC12280908 | PMID: 40623174
- Evidence: For KEGG (Kyoto Encyclopedia of Genes and Genomes) enrichment analysis, the functional enrichment analysis tool in the STRING database ( https://string-db.org/ ) was used.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> quantification [DESeq2, FastQC, R] -> differential/statistical testing [DESeq2, FastQC, R] -> stage not stated [STRING db]

### A transcriptomic, proteomic, and functional genetic atlas dissects neurofibromin function in the peripheral nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2506823122 | PMCID: PMC12260521 | PMID: 40587782
- Evidence: Visualization was performed in Cytoscape with additional connections included from the STRING database ( 42 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> visualisation [Cytoscape, STRING db]

### Metabolic control of glycosylation forms for establishing glycan-dependent protein interaction networks. (PNAS 2025)

- DOI: 10.1073/pnas.2422936122 | PMCID: PMC12207472 | PMID: 40531880
- Evidence: Examining the overlap between our network and the established database, over 46% of interactions (72 out of 156) from our platform were found on the STRING database with high confidence scores, 43 out of 156 interactions were recorded in the BioGRID database ( 32 , 33 ).
- Full pipeline: dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.9.1] -> stage not stated [AlphaFold, ComplexHeatmap, STRING db]

### Bias-aware training and evaluation of link prediction algorithms in network biology. (PNAS 2025)

- DOI: 10.1073/pnas.2416646122 | PMCID: PMC12184500 | PMID: 40493194
- Evidence: Subsequently, we extend our analysis to various networks from the STRING database ( 45 ), demonstrating that our findings generalize across different databases and evidence types for PPIs.
- Full pipeline: stage not stated [STRING db]

### ID3 enhances PD-L1 expression by restructuring MYC to promote colorectal cancer immune evasion. (PNAS 2025)

- DOI: 10.1073/pnas.2423490122 | PMCID: PMC12012548 | PMID: 40208940
- Evidence: Even so, the STRING database suggested a potential interaction between ID3, MYC, and PD-L1 ( Fig.
- Full pipeline: stage not stated [AlphaFold, STRING db]

### RGMb drives macrophage infiltration to aggravate kidney disease. (PNAS 2025)

- DOI: 10.1073/pnas.2418739122 | PMCID: PMC11929492 | PMID: 40080642
- Evidence: We performed RGMb binding protein prediction by STRING database and found that TAB1 is one of the potential RGMb binding proteins ( SI Appendix , Fig.
- Full pipeline: stage not stated [STRING db]

### A bacterial effector manipulates host lysosomal protease activity-dependent plasticity in cell death modalities to facilitate infection. (PNAS 2025)

- DOI: 10.1073/pnas.2406715122 | PMCID: PMC11874418 | PMID: 39964716
- Evidence: Lines indicate interactions between proteins inferred from STRING database.
- Full pipeline: stage not stated [STRING db]

### Targeting EPHB2/ABL1 restores antitumor immunity in preclinical models of ependymoma. (PNAS 2025)

- DOI: 10.1073/pnas.2319474122 | PMCID: PMC11789170 | PMID: 39841145
- Evidence: S1 C , where we reconstituted the network of DEGs by the STRING database, those kinases formed several clusters, including Cyclin-dependent kinases (CDKs), Src kinase family, EphB-Abl signaling pathway, mitogen-activated protein kinases (MAPKs), erb-b2 receptor tyrosine kinase 2, and RIP kinases.
- Full pipeline: quantification [HTSeq] -> dimensionality reduction/clustering [R, STRING db, pheatmap] -> stage not stated [Bioconductor, DESeq2, Seurat]

### The single-stranded DNA-binding factor SUB1/PC4 alleviates replication stress at telomeres and is a vulnerability of ALT cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2419712122 | PMCID: PMC11745411 | PMID: 39772744
- Evidence: ( E ) Interactome of top 100 SUB1/PC4 codependent genes created using STRINGdb [medium confidence setting (0.4)] and Cytoscape for network formatting.
- Full pipeline: stage not stated [CellProfiler, Cytoscape, ImageJ, STRING db]

### Linear-time prediction of proteome-scale microbial protein interactions. (PNAS 2026)

- DOI: 10.1073/pnas.2610619123 | PMCID: PMC13291599 | PMID: 42308045
- Evidence: To determine a decision boundary for proteome-scale PPI screening, we create a dataset consisting of the 650 positive E. coli PPI benchmark pairs, and randomly sampled negative pairs from the E. coli proteome at a 1:100 positive-to-negative ratio, excluding any pairs with documented physical interaction in STRING database.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [PyTorch] -> visualisation [UMAP] -> stage not stated [AlphaFold, BLAST, STRING db]

### Experimental evolution of cellular miniaturization reveals a putative mechanism for cell size evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2531280123 | PMCID: PMC13273275 | PMID: 42284327
- Evidence: Gray lines indicate known genetic and physical interactions [STRING database ( 64 )].
- Full pipeline: stage not stated [Cytoscape, STRING db]

### Active zone plasticity couples sleep need to presynaptic hypophosphorylation. (PNAS 2026)

- DOI: 10.1073/pnas.2524065123 | PMCID: PMC13273273 | PMID: 42258713
- Evidence: Then the predicted kinase–substrate relationships were filtered with protein–protein interaction information from STRING database ( https://version-11-5.string-db.org/ ).
- Full pipeline: stage not stated [AlphaFold, ImageJ, Metascape, PyMOL, STRING db]

### ProteomeLM: A proteome-scale language model enables accurate and rapid prediction of protein-protein interactions and gene essentiality across taxa. (PNAS 2026)

- DOI: 10.1073/pnas.2524201123 | PMCID: PMC13214046 | PMID: 42160340
- Evidence: Specifically, we use the D-SCRIPT dataset ( 27 ), which is derived from the STRING database ( 69 ), and focuses exclusively on experimentally validated physical interactions.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold, STRING db]

### Proteome-wide prediction of interactions between structured domains and peptide motifs reveals functionally coherent subnetworks. (PNAS 2026)

- DOI: 10.1073/pnas.2527957123 | PMCID: PMC13080015 | PMID: 41941631
- Evidence: ...h at least two literature references. • STRING-Physical (2024) ( 34 ): Experimentally supported physical and co-complex interactions derived from the STRING database. • APID Level 2 (2025) ( 32 ): PPIs observed using at least one binary experimental method. • BioGRID-MV-Physical (2025) ( 33 ): Curated physical interactions derived from both high-throughput and low-throughput studies, supported by ...
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [AlphaFold, HMMER, Python, R, STRING db, scikit-learn]

### Pharmaco-behavioral profiling identifies suppressors of autism gene-associated phenotypes in zebrafish. (PNAS 2026)

- DOI: 10.1073/pnas.2518846123 | PMCID: PMC13012064 | PMID: 41838920
- Evidence: To this end, we examined PPI networks among the strongest anticorrelating drug targets for each mutant (correlation < −0.5, P < 0.05, t-statistic) using the STRING database ( 29 ).
- Full pipeline: differential/statistical testing [STRING db] -> visualisation [Cytoscape]

### Global analysis of protein degradation reveals instability of diverse regulators in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2515265123 | PMCID: PMC12974527 | PMID: 41774798
- Evidence: Protein–protein interaction and functional enrichment analysis of the 364 annotated substrates were performed on the STRING database server ( 98 ).
- Full pipeline: quantification [limma] -> normalisation [limma] -> differential/statistical testing [XGBoost, limma] -> machine learning [XGBoost] -> stage not stated [AlphaFold, R, STRING db]

### In silico protein interaction screening uncovers DONSON's role in replication initiation. (Science 2023)

- DOI: 10.1126/science.adi3448 | PMCID: PMC10801813 | PMID: 37590370
- Evidence: To identify proteins previously associated with human DONSON, we queried the STRING database through its REST API on 19 July, 2023.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, STRING db]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Evidence: We found that the products of these pathoadaptive genes were tightly interconnected, with more protein-protein interactions than expected by chance ( STRING database ( 56 ); p < 1 x 10 -16 ; Figure 4C ; Figure S12 ), indicating their likely coordinated functional roles.
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

