# DESeq2

- **Category:** genomics
- **Papers in survey:** 886
- **Journals:** PNAS (498), Nature (307), Cell (56), Science (24), NEJM (1)
- **Years:** 2021 (76), 2022 (142), 2023 (138), 2024 (198), 2025 (229), 2026 (103)
- **Versions named:** 1.30.1 (18), 1.26.0 (17), 1.32.0 (16), 1.34.0 (13), 1.36.0 (13), 1.40.2 (13), 1.24.0 (12), 1.38.3 (11), 1.18.1 (11), 1.44.0 (10)
- **Pipeline stages it appears in:** differential/statistical testing (586), normalisation (163), quantification (109), alignment/mapping (54), dimensionality reduction/clustering (38), visualisation (20), quality control (13), read trimming (8), variant calling (5), machine learning (1)

## Papers

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Evidence: The quantification matrix was then imported into R and analyzed via DESeq2.
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Version used: **1.20**
- Evidence: Normalization and statistical framework was performed using the DESeq2 v1.20 R package.
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Evidence: Salmon quantification output files were imported into R using tximport and counts normalized for visualization using the variance stabilizing transformation from DESeq2 ( Love et al., 2014 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Version used: **1.30.0**
- Evidence: ...or Statistical Computing 4.0.2 R Core Team https://www.r-project.org R package – Seurat v3.2.2 Github https://github.com/satijalab/seurat R package – DESeq2 v1.30.0 Bioconductor https://bioconductor.org/packages/DESeq2/ R package – Circlize v0.4.11 CRAN https://CRAN.R-project.org/package=circlize R package – ggplot2 v3.3.2 CRAN https://CRAN.R-project.org/package=ggplot2 R package – ComplexHeatmap ...
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: 1072534 Software and algorithms Galaxy platform Afgan et al., 2016 N/A Deeptools Ramírez et al., 2016 N/A STAR Dobin et al., 2013 N/A FeatureCounts Liao et al., 2014 N/A DESeq2 Love et al., 2014 N/A Morpheus Broad Institute N/A DAVID Huang et al., 2009 N/A Trimmomatic Bolger et al., 2014 N/A Bowtie2 Langmead and Salzberg, 2012 N/A SAM tools Li et al., 2009 N/A MACS2 Zhang et al., 2008 N/A Bedtools...
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: See Table S1 Yoshinobu et al., 2009 N/A Primers for xMLV, see Table S1 Yoshinobu et al., 2009 N/A Software and algorithms Cell Ranger software version 4.0.1 10X Genomics RRID: SCR_017344 DESeq2 package version 2.3.11 https://bioconductor.org/packages/release/bioc/html/DESeq2.html RRID: SCR_015687 FastQC software package version 0.11.5 Babraham Bioinformatics RRID: SCR_014583 Fiji image processing ...
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### Lipolysis drives expression of the constitutively active receptor GPR3 to induce adipose thermogenesis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.037 | PMCID: PMC8238500 | PMID: 34048700
- Evidence: ...Luc (CAMYEL) Jiang et al., 2007 N/A Software and algorithms STAR Dobin et al., 2013 N/A HOMER Heinz et al., 2010 N/A iRNA-seq Madsen et al., 2015 N/A DESeq2 Love et al., 2014 N/A Graphpad Prism 8.0 for statistical analysis GraphPad N/A Other Phenomaster home cage system TSE Systems N/A Constant climate chamber Memmert HPP750 Inveon multimodality PET/CT scanner Siemens N/A Echo-MRITM-4in1 body comp...
- Full pipeline: differential/statistical testing [DESeq2, HOMER]

### Splice site m<sup>6</sup>A methylation prevents binding of U2AF35 to inhibit RNA splicing. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.062 | PMCID: PMC8208822 | PMID: 33930289
- Evidence: ...e/ WebLogo http://weblogo.berkeley.edu/ R R Core Team, 2017 https://www.r-project.org Bowtie Langmead et al., 2009 http://bowtie-bio.sourceforge.net/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/DESeq2 Bioconductor Huber et al., 2015 https://www.bioconductor.org/ Salmon Patro et al., 2017 https://combine-lab.github.io/salmon/ MACS2 Zhang et al., 2008 https://github.com/macs3-project/...
- Full pipeline: stage not stated [Bioconductor, Cutadapt, DESeq2, MACS2, R]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **1.27.32**
- Evidence: ...ub.io/kallisto/ R Package: tximport (version 1.8.0) Soneson et al., 2015 https://bioconductor.org/packages/release/bioc/html/tximport.html R Package: DESeq2 (version 1.27.32) Love et al. , 2014 http://bioconductor.org/packages/release/bioc/html/DESeq2.html R Package: clusterProfiler (version 3.15.4) Yu et al. , 2012 https://bioconductor.org/packages/release/bioc/html/clusterProfiler.html R Package...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...tml DoubletFinder McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder Seurat Stuart et al., 2019 https://satijalab.org/seurat/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ChIP-seq Analysis pipeline This study https://github.com/MarioPujato/NextGenAligner bedtools Quinlan and Hall, 2010 https://github.com/arq5x/bedtools2/releases H...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Version used: **1.28.1**
- Evidence: ...ape https://cytoscape.org/ Cytoscape 3.8.1 Differential Enrichment analysis of Proteomics Data (DEP) https://rdrr.io/bioc/DEP/man/DEP.html DEP 1.10.0 DESeq2 https://bioconductor.org/packages/release/bioc/html/DESeq2.html DESeq2 1.28.1 DAVID Bioinformatics Resources https://david.ncifcrf.gov/ DAVID 6.8 Resource availability Lead contact Further information and requests for resources and reagents sh...
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Soluble ACE2-mediated cell entry of SARS-CoV-2 via interaction with proteins related to the renin-angiotensin system. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.053 | PMCID: PMC7923941 | PMID: 33713620
- Evidence: ...2 Langmead and Salzberg, 2012 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml HTSeq Anders et al., 2015 https://htseq.readthedocs.io/en/master/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html R Gu et al., 2016 ; Ito and Murphy, 2013 https://www.r-project.org/ UniProt Bairoch et al., 2005 https://www.uniprot.org/ Gene Ontology Ashburner et al., 2000 ht...
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> stage not stated [Bowtie2, Cutadapt, DESeq2, HTSeq]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: Expression counts were normalized using DESeq2 variance stabilizing transformation (vst) function and transcripts per kilobase million (TPM) values calculated using RSEM with default parameters ( Li and Dewey, 2011 ).
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: DESeq2 ( Love et al., 2014 )was then used to perform differential expression analyses, with zinbwave observational-level weights used in parameter estimation step, with the following non-default parameters: sfType = ”poscounts” and minmu = 1e-6.
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Version used: **1.24.0**
- Evidence: ...port.illumina.com/sequencing/sequencing_software/bcl2fastq-conversion-software.html STAR v2.7.3a Dobin et al., 2013 https://github.com/alexdobin/STAR DESeq2 v1.24.0 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ComplexHeatMap v2.0.0 Gu et al., 2016 https://bioconductor.org/packages/release/bioc/html/ComplexHeatmap.html VennDiagram v1.6.20 CRAN https://rdrr.io/cr...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.030 | PMCID: PMC7584921 | PMID: 33147445
- Evidence: ...2018 N/A FlowJo v10 BD Biosciences N/A GraphPad Prism 8 GraphPad N/A Cellranger v3.0.1 10x Genomics N/A Seurat R package v3.2 Stuart et al., 2019 N/A DESeq2 Love et al., 2014 N/A STRING tool Szklarczyk et al., 2019 N/A Resource Availability Lead Contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Neville Sanjana ( nev...
- Full pipeline: read trimming [Cutadapt v1.13] -> alignment/mapping [STAR] -> stage not stated [DESeq2, GSEA, R, Seurat, fgsea]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Version used: **1.32**
- Evidence: ...6/V5-DEST-HMGB1 Scott et al., 2011 Addgene Cat#31208 Software and Algorithms Bowtie2 v2.2.9 Langmead and Salzberg, 2012 N/A Cutadapt Martin, 2011 N/A DESeq2 v1.32 Love et al., 2014 N/A deeptools v3.1.3 Ramírez et al., 2016 N/A Flowjo 10.6.2 FLOWJO https://www.flowjo.com Graphpad Prism 8 Graphpad software https://www.graphpad.com/scientific-software/prism/ MACS2 Zhang et al., 2008 N/A PoolQ version...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: Differential gene expression was ascertained using the DESeq2 package ( Love et al., 2014 ).
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Post-gastrulation synthetic embryos generated ex utero from mouse naive ESCs. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.028 | PMCID: PMC9439721 | PMID: 35988542
- Evidence: ...tor.org/packages/release/bioc/html/AUCell.html UTAP Bioinformatics unit, Weizmann Institute of Science, Israel https://utap.readthedocs.io/en/latest/ DESeq2.0 Bioconductor project, USA https://bioconductor.org/packages/release/bioc/html/DESeq2.html IGV Broad Institute, USA https://software.broadinstitute.org/software/igv/ Other PVDF filter 0.22 μm Millipore SLGV033RS 35mm glass bottom dishes In Vi...
- Full pipeline: alignment/mapping [STAR v2.4.2a] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, R, Seurat, pheatmap]

### Disrupting autorepression circuitry generates "open-loop lethality" to yield escape-resistant antiviral agents. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.022 | PMCID: PMC9097017 | PMID: 35561685
- Evidence: Kallisto count function quantified transcript abundance for subsequent differential expression analysis with DESeq2 ( Love et al., 2014 ) in RStudio.
- Full pipeline: alignment/mapping [kallisto] -> quantification [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Version used: **1.28.0**
- Evidence: (2013) , Li and Dewey (2011) ( Dobin et al., 2013 ; Li and Dewey, 2011 ) N/A DESeq2 v1.28.0 ( Love et al., 2014 ) RRID: SCR_015687 R package Cluster Profiler v3.18.1 ( Yu et al., 2012 ) RRID: SCR_016884 Molecular Signatures database MSigDB, v7.2 RRID: SCR_016863 Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfille...
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### Cell surface fluctuations regulate early embryonic lineage sorting. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.022 | PMCID: PMC8896887 | PMID: 35196500
- Evidence: ...ucts/matlab.html Prism 7 Graphpad software, Inc https://www.graphpad.com/ htseq-count ( Anders et al., 2015 ) https://htseq.readthedocs.io/en/master/ DESeq2 ( Love et al., 2014 ) https://bioconductor.org/packages/release/bioc/html/DESeq2.html Sincell ( Juliá et al., 2015 ) http://bioconductor.org/packages/release/bioc/html/sincell.html FactoMineR ( Lê et al., 2008 ) http://factominer.free.fr/ R mo...
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Bioconductor] -> stage not stated [DESeq2, HTSeq, ImageJ]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: (2014) https://bioconductor.org/packages/release/bioc/html/DESeq2.html STAR Dobin et al.
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: The pseudobulk samples were then normalized according to the DESeq2 pipeline (( Love et al., 2014 ), v.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Raw reads were normalized with DESeq2 R package (version 1.30.0, Anders and Huber, 2010 ) and a paired t test was compared to the log2 ratio of group means to generate the volcano plot ( Table S3 ).
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: Peaks were called in each sample using MACS2 79 with default parameters, and differential accessibility/binding analysis was conducted using Bioconductor DESeq2 in RStudio.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### Early cellular mechanisms of type I interferon-driven susceptibility to tuberculosis. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.002 | PMCID: PMC10757650 | PMID: 38029747
- Evidence: The raw counts were used as input for DESeq2 111 analysis of differential gene expression.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR, Trimmomatic v0.36] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: We performed differential expression analysis with DESeq2 113 .
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: Library normalization and calculation of significant differential enrichment of RNA fragments in the two intervals was performed applying the DESeq2 101 approach using the Wald test statistic for calculating p values.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Differentially expressed genes between bones were obtained using the DESeq2 model.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Humanized mouse liver reveals endothelial control of essential hepatic metabolic functions. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.017 | PMCID: PMC10544749 | PMID: 37562401
- Evidence: Raw sequencing reads were aligned to the human–mouse combined genome with STAR ( https://doi.org/10.1093/bioinformatics/bts635 ), annotated and counted with HTSeq ( https://doi.org/10.1093/bioinformatics/btu638 ), normalized using DESeq2 ( https://doi.org/10.1186/s13059-014-0550-8 ) and graphed using the Broad Institute Morpheus web tool.
- Full pipeline: alignment/mapping [DESeq2, HTSeq, STAR] -> normalisation [DESeq2, HTSeq, STAR] -> stage not stated [Seurat v3.2]

### Engineering RNA export for measurement and manipulation of living cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.013 | PMCID: PMC10528933 | PMID: 37437570
- Version used: **1.30.1**
- Evidence: Differential expression of cellular RNA To characterize alterations to the cellular transcriptome due to RNA exporter expression, as shown in Figure S4D , differential expression analysis was performed using DESeq2 (1.30.1) 83 in R (4.0.5) comparing raw gene counts in cells transfected with and without RNA exporters.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.8a] -> quantification [SciPy v1.4.1] -> normalisation [scikit-image v0.19.2] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.5] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [PyMOL]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: A matrix containing sgRNA counts from all CEV-v1 screens (excluding C3649 and Pt5-C due to non-responsiveness to MDM2 / TP53 perturbations) was assembled and used as input for differential analysis by DESeq2.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Evidence: 89 http://bioconductor.org/packages/release/bioc/html/DEXSeq.html DESeq2 Love et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: The counting results were imported into DESeq2 object by tximport ( https://bioconductor.org/packages/release/bioc/html/tximport.html ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **1.10.1**
- Evidence: 103 The differential expression analysis was performed with DESeq2 v1.10.1.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Evidence: We considered a gene to be differentially expressed between two sets of conditions if the log 2 -fold-change between the two sets of conditions was greater than 1 (absolute value) and the adjusted p -value was below 0.05, according to the calculations made with the DESeq function of the DESeq2 package version 1.24.0 201 implemented in R.
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: ...s study pLCRIS_00558 Software and algorithms Custom code This study Zenodo: https://zenodo.org/records/12615731 Adobe Illustrator Adobe www.adobe.com DESeq2 https://doi.org/10.1186/s13059-014-0550-8 https://doi.org/10.18129/B9.bioc.DESeq2 QIIME I v1.9.188 https://doi.org/10.1038/s41587-019-0209-9 https://qiime2.org/ Dada2 v1.6.089 https://doi.org/10.1038/nmeth.3869 https://doi.org/10.18129/B9.bioc...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Version used: **3.14**
- Evidence: DESeq2 (version 3.14) and EdgeR (v.3.36.0) was used to assess the differential gene expression/binding between grouped samples.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### The germline coordinates mitokine signaling. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.010 | PMCID: PMC12261959 | PMID: 38959891
- Version used: **2.11.40.8**
- Evidence: Tools included Kallisto Quant v0.48.0+galaxy1 and DESeq2, v2.11.40.8+galaxy0 72 .
- Full pipeline: quantification [ImageJ] -> stage not stated [DESeq2 v2.11.40.8, kallisto]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Version used: **1.40.2**
- Evidence: 128 RRID: SCR_010881 DESeq2 v1.40.2 Love et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### An atlas of human vector-borne microbe interactions reveals pathogenicity mechanisms. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.023 | PMCID: PMC11959484 | PMID: 38876107
- Evidence: Significant differences in gene expression were then calculated by DESeq2, a 2-dimensional PCA was run, and a hierarchical clustering heatmap (with a threshold of ± 2-fold change in expression EGF/Fc at 37°C and p-value < 0.05) were all done using Partek Flow 10.0.23.0720 (Partek Incorporated).
- Full pipeline: dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [R]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Evidence: 102 https://bioconductor.org/packages/release/bioc/html/DESeq2.html FastQC v0.11.9 Andrew 103 http://www.bioinformatics.babraham.ac.uk/projects/fastqc MultiQC v1.8 Ewels et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Evidence: Differential expression analysis was performed with DESeq2 107 .
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: 89 N/A DESeq2 Love et al.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Evidence: 123 https://bioconductor.org/packages/release/bioc/html/DESeq2.html Other AuxPhos This paper Source code: https://github.com/WeijersLab/AuxPhos Webtool: https://weijerslab.shinyapps.io/AuxPhos MAFFT v7.505 Nakamura et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Distinct components of mRNA vaccines cooperate to instruct efficient germinal center responses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.023 | PMCID: PMC12878702 | PMID: 41406961
- Evidence: The PCA plot was generated using DESeq2 from pseudo-bulk counts aggregated by individual animals.
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [GSEA, R, fgsea] -> stage not stated [Seurat]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: ...ie2 https://doi.org/10.1038/nmeth.1923 https://github.com/BenLangmead/bowtie2 JASPAR https://doi.org/10.1093/nar/gkab1113 https://jaspar.genereg.net/ DESeq2 https://doi.org/10.1186/s13059-014-0550-8 http://www.bioconductor.org/packages/release/bioc/html/DESeq2.html bedtools https://doi.org/10.1093/bioinformatics/btq033 https://bedtools.readthedocs.io/en/latest/ Trim_galore Babraham Institute https...
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Evidence: 53 https://github.com/of erfrid/NQBMatlab/tre e/V16 DESeq2 Love et al.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### RNA Pol II inhibition activates cell death independently from the loss of transcription. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.034 | PMCID: PMC12406974 | PMID: 40818455
- Evidence: Counts were normalized to ERCC spike-ins using DESeq2, implemented with the function “estimateSizeFactors” with the option “controlGenes” set to the identities of the 92 ERCC transcripts.
- Full pipeline: quality control [FastQC] -> quantification [FastQC, kallisto] -> normalisation [DESeq2] -> differential/statistical testing [FastQC] -> stage not stated [GSEA]

### The essential host genome for Cryptosporidium survival exposes metabolic dependencies that can be leveraged for treatment. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.001 | PMCID: PMC7618951 | PMID: 40706591
- Evidence: RNA-seq data were analysed in R (v.4.4.1); data exploration, filtering, and differential gene expression analyses were performed using DESeq2 68 (v.1.46.0).
- Full pipeline: quality control [FastQC, ImageJ v2.1.0, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [PHENIX, STRING db v12.0]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Next, a DESeq2 62 object was created using the DESeqDataSetFromMatrix() function with design = ~ experiment, where experiment represents the replicates.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Version used: **1.36**
- Evidence: 84 ; RRID: N/A Bioconductor DESeq2 v1.36 Love et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Evidence: Samples displayed highly comparable recovery of spike-in reads, thus samples were normalized based on the DESeq2 size factors.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: 172 V3.2.26 BioRender BioRender.com N/A Bowtie2 Langmead and Salzberg 173 V2.5.4 BV-BRC platform UChicago V3.55.17 CFX Maestro Bio-Rad V2.3 COBRA MATLAB V2.13.3 DESeq2 Love et al.
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Citrate clearance is a major function of aconitase 2 in the canonical TCA cycle. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.028 | PMCID: PMC13045649 | PMID: 41763199
- Version used: **1.46.0**
- Evidence: Differentially expressed genes were determined using DESeq2 (version 1.46.0).
- Full pipeline: differential/statistical testing [DESeq2 v1.46.0] -> stage not stated [GSEA, R v4.3.2, featureCounts, fgsea, ggplot2 v3.5.2]

### The Genetic Architecture of Congenital Diarrhea and Enteropathy. (NEJM 2025)

- DOI: 10.1056/nejmoa2405333 | PMCID: PMC11968080 | PMID: 40174224
- Evidence: RNA was extracted and sequenced from pooled wildtype or variant zebrafish and differential expression analysis was carried out using the DESeq2 package in R.
- Full pipeline: differential/statistical testing [DESeq2]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: To calculate size factors, the TSS count matrix was processed through DESeqDataSetFromMatrix and estimateSizeFactors from the DESeq2 package 75 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### B cell-derived GABA elicits IL-10<sup>+</sup> macrophages to limit anti-tumour immunity. (Nature 2021)

- DOI: 10.1038/s41586-021-04082-1 | PMCID: PMC8599023 | PMID: 34732892
- Version used: **1.30.1**
- Evidence: The normalized number of molecules was calculated using DESeq2 (1.30.1).
- Full pipeline: alignment/mapping [STAR v2.5.4b] -> normalisation [DESeq2 v1.30.1]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: The differential expressed genes were identified using DESeq2 package 42 . eccDNA linearization EccDNA linearization was performed by sequential treatment of eccDNAs with the nickase fnCpf1 37 (Applied Biological Materials) and single strand DNA-specific nuclease.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Version used: **1.30.0**
- Evidence: To calculate the number of differentially expressed genes between each species pair for each cross-species cluster, we used a pseudobulk comparison method 74 from DESeq2 (v1.30.0).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### Swarm Learning for decentralized and confidential clinical machine learning. (Nature 2021)

- DOI: 10.1038/s41586-021-03583-3 | PMCID: PMC8189907 | PMID: 34040261
- Version used: **1.22.2**
- Evidence: The RNA-seq data (dataset A3) were normalized using the R package DESeq2 (v 1.22.2) with standard parameters.
- Full pipeline: alignment/mapping [kallisto v0.43.1] -> normalisation [DESeq2 v1.22.2, R] -> machine learning [Docker] -> stage not stated [Keras v2.3.1, TensorFlow v2.2.0, scikit-learn]

### NASH limits anti-tumour surveillance in immunotherapy-treated HCC. (Nature 2021)

- DOI: 10.1038/s41586-021-03362-0 | PMCID: PMC8046670 | PMID: 33762733
- Version used: **1.28.1**
- Evidence: Pairwise comparisons of CD4 + T cells versus CD4 + PD1 + T cells and CD8 + T cells versus CD8 + PD1 + T cells were performed using the results of differential expression analysis by DESeq2 (v1.28.1) 58 , setting CD4 + /CD8 + T cells as controls.
- Full pipeline: quality control [Seurat] -> alignment/mapping [velocyto v0.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2 v1.28.1] -> stage not stated [R v3.4, scVelo v0.2.2]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **1.26.0**
- Evidence: Samples were normalized for differences in sequencing depth by computing size factors and further variance stabilizing transformation with DESeq2 (v 1.26.0) 61 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Sulfur sequestration promotes multicellularity during nutrient limitation. (Nature 2021)

- DOI: 10.1038/s41586-021-03270-3 | PMCID: PMC7969356 | PMID: 33627869
- Evidence: Raw mapped reads were processed in R (Lucent Technologies) with DESeq2 52 to generate normalized read counts to visualize as heat maps using Morpheus (Broad Institute) and determine differentially expressed genes with greater than 2 fold change and lower than 0.1 adjusted P value, which were analysed for pathway enrichment using STRING.
- Full pipeline: read trimming [Seurat, UMAP, deepTools, featureCounts] -> alignment/mapping [DESeq2, R, Seurat, UMAP, deepTools, featureCounts] -> quantification [DESeq2, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R]

### SARS-CoV-2 infection is effectively treated and prevented by EIDD-2801. (Nature 2021)

- DOI: 10.1038/s41586-021-03312-w | PMCID: PMC7979515 | PMID: 33561864
- Evidence: RNA-sequencing data was normalized and interrogated for changes in gene expression using DESeq2 package (version 3.1.1) in R (version 3.6.3) 48 and statistical tests were two-sided.
- Full pipeline: alignment/mapping [STAR v2.7.5a] -> quantification [STAR v2.7.5a] -> normalisation [DESeq2, R v3.6.3] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [GSEA, ImageJ, ggplot2 v3.3.1, tidyverse v1.3.0]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: The resulting peak atlas was normalized using DESeq2 53 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: Differentially expressed genes (DEGs) were detected by DESeq2 package from Bioconductor ( bioconductor.org/packages/release/bioc/html/DESeq2 ) 62 using likelihood ratio test (LRT, adjusted P -value < 0.001) or Wald test.
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### IgA transcytosis and antigen recognition govern ovarian cancer immunity. (Nature 2021)

- DOI: 10.1038/s41586-020-03144-0 | PMCID: PMC7969354 | PMID: 33536615
- Version used: **1.30.0**
- Evidence: Differential expression analysis was performed using DESeq2 (v.1.30.0) 27 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, HTSeq, STAR] -> normalisation [HTSeq] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [GSEA, R v3.6.1]

### Dynamic regulation of T<sub>FH</sub> selection during the germinal centre reaction. (Nature 2021)

- DOI: 10.1038/s41586-021-03187-x | PMCID: PMC7979475 | PMID: 33536617
- Version used: **1.24.0**
- Evidence: Kallisto TPM values were converted to absolute counts using tximport (v1.12.3) R package and DESeq2 (v.1.24.0) was utilized for differential expression analysis.
- Full pipeline: quantification [DESeq2 v1.24.0, R] -> differential/statistical testing [DESeq2 v1.24.0, R, Seurat v3.1.2, kallisto v0.46] -> stage not stated [GSEA]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: The test for differential expression was conducted through a likelihood ratio test in DESeq2 86 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Control of osteoblast regeneration by a train of Erk activity waves. (Nature 2021)

- DOI: 10.1038/s41586-020-03085-8 | PMCID: PMC7864885 | PMID: 33408418
- Evidence: Bioconductor package DESeq2 35 (v 1.26.0) were employed for differential expression (DE) analysis.
- Full pipeline: read trimming [TopHat, Trim Galore v0.4.1] -> alignment/mapping [TopHat, Trim Galore v0.4.1] -> quantification [featureCounts] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> stage not stated [ilastik v1.3.3]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **1.26.0**
- Evidence: Bulk differential expression analysis: All analysis was performed using custom scripts in R version 3.6.3 using the DESeq2 version 1.26.0 framework 59 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Nociceptive nerves regulate haematopoietic stem cell mobilization. (Nature 2021)

- DOI: 10.1038/s41586-020-03057-y | PMCID: PMC7856173 | PMID: 33361809
- Evidence: Differential expression analysis between two groups was performed using the DESeq2 R package, which provide statistical routines for determining differential expression in digital gene expression data using a model based on the negative binomial distribution.
- Full pipeline: alignment/mapping [HTSeq v0.6.1] -> quantification [HTSeq v0.6.1] -> differential/statistical testing [DESeq2, R]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Evidence: Normalization for library size, log transformation, and differential expression analysis were performed with DESeq2 45 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### A plant-derived natural photosynthetic system for improving cell anabolism. (Nature 2022)

- DOI: 10.1038/s41586-022-05499-y | PMCID: PMC9750875 | PMID: 36477541
- Evidence: Compared with the IL-1β group, the IL-1β plus CM-NTU group showed upregulated expression of 351 genes and downregulated expression of 784 genes ( P -adjusted value by Wald test in DESeq2). d , Gene set enrichment analysis was performed to compare the gene sets involved in the TCA cycle, oxidative phosphorylation, glycolysis and ECM degradation between the IL-1β plus CM-NTU group and the IL-1β grou...
- Full pipeline: stage not stated [DESeq2, GSEA]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **1.24.0**
- Evidence: Differential gene expression analysis was performed on raw counts using DESeq2 (v.1.24.0) with a negative binomial distribution and Wald test for significance 57 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Version used: **1.30.1**
- Evidence: Genewise differential expression in the chemotherapy dataset between controls and Folfiri treatment was performed using the R package DESeq2 (v1.30.1) 54 .
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Nociceptor neurons affect cancer immunosurveillance. (Nature 2022)

- DOI: 10.1038/s41586-022-05374-w | PMCID: PMC9646485 | PMID: 36323780
- Version used: **1.18.1**
- Evidence: DESeq2 v.1.18.1 (ref.
- Full pipeline: read trimming [STAR v2.5.1b, Trimmomatic v0.35] -> alignment/mapping [STAR v2.5.1b, Trimmomatic v0.35, featureCounts] -> quantification [Bioconductor, RSEM] -> normalisation [Bioconductor, RSEM] -> dimensionality reduction/clustering [R] -> stage not stated [DESeq2 v1.18.1, ImageJ]

### Extracellular fluid viscosity enhances cell migration and cancer dissemination. (Nature 2022)

- DOI: 10.1038/s41586-022-05394-6 | PMCID: PMC9646524 | PMID: 36323783
- Evidence: The DESeq2.r package was used (in R, v.4.0) to normalize and compare the reads for each gene between the samples of interest, with respective P values for each gene per comparison and PCA score for each sample (Extended Data Fig.
- Full pipeline: alignment/mapping [HISAT2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Python v3.8, TrackMate]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: Changes in expression of genes associated with these sites were tested for using DESeq2 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Phenotypic plasticity and genetic control in colorectal cancer evolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05311-x | PMCID: PMC9684078 | PMID: 36289336
- Version used: **1.24.0**
- Evidence: Raw read counts uniquely assigned to these genes were converted into both transcripts per million (TPM) and variance stabilization transformed (VST) counts via DESeq2 v.1.24.0 (ref.
- Full pipeline: quantification [DESeq2 v1.24.0, GSVA] -> normalisation [Seurat v4.1.0] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, R, lme4] -> stage not stated [STRING db, ape (R) v5.6, phytools]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Evidence: For HEK293T cell ATAC-seq, genes with high, intermediate, low and no expression were defined by DESeq2 normalized basemean values from HEK293T cell RNA-seq data with under 2 basemean as non-expressing genes and the remaining genes binned into three groups for low, intermediate and high expression.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: DESeq2 (ref.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### The role of somatosensory innervation of adipose tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05137-7 | PMCID: PMC9477745 | PMID: 36045288
- Version used: **1.32.0**
- Evidence: Differential gene expression analysis and P -value calculation were performed by DESeq2 (v.1.32.0) 58 .
- Full pipeline: alignment/mapping [SAMtools v1.10, Salmon v1.5.1] -> quantification [ImageJ, Salmon v1.5.1] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [Metascape]

### RASA2 ablation in T cells boosts antigen sensitivity and long-term function. (Nature 2022)

- DOI: 10.1038/s41586-022-05126-w | PMCID: PMC9433322 | PMID: 36002574
- Evidence: Differential gene expression was performed using R package DESeq2 57 v1.32.0, controlling for donor variance.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [DESeq2, Seurat, fgsea] -> stage not stated [GSEA, ImageJ v1.52q, R]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Version used: **1.26.0**
- Evidence: Normalization and differential gene expression analysis was performed using DESeq2 (v.1.26.0).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Brown-fat-mediated tumour suppression by cold-altered global metabolism. (Nature 2022)

- DOI: 10.1038/s41586-022-05030-3 | PMCID: PMC9365697 | PMID: 35922508
- Version used: **1.30.0**
- Evidence: Differential expression analysis between three 30 °C and two 4 °C samples was performed using the R (v.4.0.3) package DESeq2 (v.1.30.0).
- Full pipeline: alignment/mapping [featureCounts v2.0.0] -> differential/statistical testing [DESeq2 v1.30.0, GSEA v4.1.0] -> stage not stated [ImageJ]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: The DESeq2 package in R was used to model expression counts and compute Wald test statistics 74 .
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Version used: **1.22.1**
- Evidence: Differential expression analyses DESeq2 (v1.22.1) 54 within R was used for read count normalization, and downstream differential expression analysis and visualization were performed within Qlucore Omics Explorer v3.3 (Qlucore).
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### A male steroid controls female sexual behaviour in the malaria mosquito. (Nature 2022)

- DOI: 10.1038/s41586-022-04908-6 | PMCID: PMC9352575 | PMID: 35794471
- Evidence: Calculation of normalized read counts and analysis of differential gene expression was performed using the DESeq2 package (version 1.28.1) in R (version 4.0.3).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, HTSeq v0.9.1, SAMtools v1.3.1] -> quantification [DESeq2, R v4.0.3] -> normalisation [DESeq2, R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3]

### Apoptotic brown adipocytes enhance energy expenditure via extracellular inosine. (Nature 2022)

- DOI: 10.1038/s41586-022-05041-0 | PMCID: PMC9452294 | PMID: 35790189
- Version used: **1.32.0**
- Evidence: Count data were homoscedastic normalized with respect to library size using the variance stabilizing transformation from DESeq2 (v.1.32.0, ref.
- Full pipeline: normalisation [DESeq2 v1.32.0] -> stage not stated [MACS2, featureCounts v2.0.1, ggpubr v0.4.0]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Evidence: For the comparison with DESeq2 52 , the input tables containing the replicates for the groups to compare were created by a custom perl script.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Potentiating adoptive cell therapy using synthetic IL-9 receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04801-2 | PMCID: PMC9283313 | PMID: 35676488
- Evidence: Differential expression analysis was performed using DESeq2 (ref.
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> quantification [HTSeq] -> normalisation [pheatmap] -> dimensionality reduction/clustering [edgeR] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [R, fgsea]

### The renal lineage factor PAX8 controls oncogenic signalling in kidney cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-04809-8 | PMCID: PMC9242860 | PMID: 35676472
- Evidence: TCGA ATAC-seq data, 410 human tumours, 562,709 pan-cancer peaks. ccRCCs compared to all other tumour types by DESeq2. e , Normalized DNA accessibility at E11:69419, TCGA ATAC-seq data. ccRCC (KIRC), N = 16; papillary RCC (KIRP), N = 34. f , Normalized DNAse hypersensitivity (DHS) signal for E11:69419, 733 samples from different cell types. g , Tumour-free survival of mice inoculated with 786-M1A c...
- Full pipeline: normalisation [DESeq2]

### Island-specific evolution of a sex-primed autosome in a sexual planarian. (Nature 2022)

- DOI: 10.1038/s41586-022-04757-3 | PMCID: PMC9177419 | PMID: 35650439
- Version used: **1.26.0**
- Evidence: Differential gene expression was analysed with DESeq2 (version 1.26.0) 55 .
- Full pipeline: variant calling [GATK v4.1.4.1] -> quantification [kallisto v0.44.0] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [ImageJ, RAxML v0.9.0, VCFtools v0.1.14]

### Neuropathic pain caused by miswiring and abnormal end organ targeting. (Nature 2022)

- DOI: 10.1038/s41586-022-04777-z | PMCID: PMC9159955 | PMID: 35614217
- Evidence: Differential gene expression analysis was performed using DESeq2 68 (v.1.28.1) and only genes having a false discovery rate (FDR) lower than 10% were considered as significant.
- Full pipeline: differential/statistical testing [DESeq2, R] -> stage not stated [ImageJ]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Differential peak calling for the MCF-7 CUT&RUN experiment was performed with DESeq2 ( P adj < 0.1) in DiffBind.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Intermittent PI3Kδ inhibition sustains anti-tumour immunity and curbs irAEs. (Nature 2022)

- DOI: 10.1038/s41586-022-04685-2 | PMCID: PMC9132770 | PMID: 35508656
- Version used: **1.24.0**
- Evidence: Differential expression analysis between the pre and post treatment, as well as between pre and post placebo, was performed using DESeq2 (v1.24.0).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [GSEA, MACS2, Seurat v3.1.5, fgsea v1.10.1]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Evidence: We used the DESeq2 package 100 in R (v.g3.5.3) to test for differential expression.
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Evidence: RNA-seq reads were mapped to the human (hg38) using STAR v2.7.3a following ENCODE standard options, read counts were generated using RSEM v1.3.1, and differential expression analysis was performed in R v4.0.2 using the DESeq2 package v1.28.1 40 .
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: For differential gene expression analysis, all samples were run in the same manner using the standard DESeq2 41 workflow without additional covariates, except for the Klim MNs dataset 9 , where we included the day of differentiation.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: Genes were ranked on the basis of their shrunken log-transformed fold change values and associated Wald test P values obtained from analysis of differential expression using Bioconductor’s DESeq2 (ref.
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Version used: **1.18.1**
- Evidence: Differential gene-expression analysis on raw counts and variance-stabilized transformation of count data for heatmap visualization were performed using DESeq2 v1.18.1.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Evidence: Differential expression analysis between conditions was performed on pseudobulk counts for each cell type in each sample using DESeq2 (ref.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: Tissue gene expression data were normalized using the DESeq2 (ref.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **1.26.0**
- Evidence: Bigwig files were created using deepTools bamCoverage (v.3.3.2) 62 , using a size factor calculated from DESeq2 (v.1.26.0) 63 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: Normalization of gene counts and differential analysis were performed using DESeq2 (v.5).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: To identify the DA OCRs, the raw nucleosome-free read was first normalized as counts per million followed by DA analysis by implementation of the negative binomial model in the DESeq2 R package 57 .
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Glioma synapses recruit mechanisms of adaptive plasticity. (Nature 2023)

- DOI: 10.1038/s41586-023-06678-1 | PMCID: PMC10632140 | PMID: 37914930
- Version used: **1.36.0**
- Evidence: Differential gene expression and log 2 fold change calculations were determined using the DESeq2 (v.1.36.0) package in R 65 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [ImageJ v2.1.0, RSEM, featureCounts, kallisto] -> normalisation [RSEM] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.36.0] -> visualisation [ImageJ v2.1.0] -> stage not stated [R v4.1.1]

### Targeting myeloid chemotaxis to reverse prostate cancer therapy resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06696-z | PMCID: PMC10686834 | PMID: 37844613
- Evidence: Differential gene expression between pre- and on-treatment samples was carried out using the HTG EdgeSeq Reveal DESeq2 analysis pipeline and R Software (v.4.2.3).
- Full pipeline: alignment/mapping [Cufflinks v2.2.1, TopHat v2.0.7] -> quantification [Cufflinks v2.2.1] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSVA v1.4, R]

### Apoptotic stress causes mtDNA release during senescence and drives the SASP. (Nature 2023)

- DOI: 10.1038/s41586-023-06621-4 | PMCID: PMC10584674 | PMID: 37821702
- Evidence: The read count matrix was then used for differential expression analysis with the linear modelling tool DESeq2.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [Cufflinks, FastQC, STAR] -> quantification [Cufflinks, DESeq2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Evidence: A variance stabilizing transformation was applied to the counts matrix, and differentially expressed genes were quantified using the DESeq2 R package 54 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Version used: **1.26.0**
- Evidence: Differential expression analysis was performed using DESeq2 (v.1.26.0), and only genes with FDR < 0.05 were considered as differentially expressed.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### Inhibition of fatty acid oxidation enables heart regeneration in adult mice. (Nature 2023)

- DOI: 10.1038/s41586-023-06585-5 | PMCID: PMC10584682 | PMID: 37758950
- Evidence: Differentially expressed genes were identified using DESeq2 version ≥ 1.14.0 (ref.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [FastQC v0.11.8, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Version used: **1.24.0**
- Evidence: Differential analysis was performed by DESeq2 (v.1.24.0) 58 .
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Evidence: Differential expression analysis was carried out with DESeq2 package (version 1.24.0) 53 within R version 3.6.0 54 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Platelet factors attenuate inflammation and rescue cognition in ageing. (Nature 2023)

- DOI: 10.1038/s41586-023-06436-3 | PMCID: PMC10468395 | PMID: 37587343
- Evidence: Alignment of RNA-seq reads to the mouse mm10 transcriptome was performed using STAR (v.2.7.3a) 50 using the ENCODE standard options, read counts were generated using RSEM (v.1.3.1) and differential expression analysis was performed in R (v.3.6.1) using the DESeq2 package (v.1.38.0) 51 (detailed pipeline v.2.0.1 and options are available at GitHub ( https://github.com/emc2cube/Bioinformatics/ )).
- Full pipeline: alignment/mapping [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> quantification [DESeq2, ImageJ, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> stage not stated [Enrichr, Seurat]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Evidence: Data normalization was performed using the DESeq2 Bioconductor package 64 and was rlog transformed to allow for visualization by PCA and heatmaps.
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Evidence: The DESeq2 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### cGAS-STING drives ageing-related inflammation and neurodegeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-06373-1 | PMCID: PMC10412454 | PMID: 37532932
- Version used: **1.38.2**
- Evidence: DEG analysis was performed using the R (v.4.2.2) package DESeq2 (v.1.38.2). scRNA-seq Nuclei from mouse brain were extracted by homogenizing mouse brain tissues in Nuclei EZ Lysis Buffer (Millipore Sigma) using a douncer.
- Full pipeline: alignment/mapping [HTSeq, STAR, featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.38.2, ImageJ, Seurat]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Evidence: Normalization was performed using the DESeq2 tool 63 in which counts were first scaled with respect to the library size for each sample followed by variance-stabilized normalization.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Evidence: RNA-seq analysis was performed with R (v.4.0.3) and the DESeq2 package (v.1.30.1). log 2 -Transformed transcripts per million were calculated, and we performed EMT score calculation as previously described 20 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### PLSCR1 is a cell-autonomous defence factor against SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06322-y | PMCID: PMC10371867 | PMID: 37438530
- Evidence: Differential gene expression was analysed with the R package DESeq2.
- Full pipeline: alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, R] -> simulation/modelling [AlphaFold, GROMACS v2021.3, Python] -> stage not stated [PyMOL, VMD]

### Mast cells link immune sensing to antigen-avoidance behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06188-0 | PMCID: PMC10432277 | PMID: 37438525
- Evidence: Count data normalization and differential expression analysis were performed using DESeq2 (ref.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [DESeq2]

### GDF15 promotes weight loss by enhancing energy expenditure in muscle. (Nature 2023)

- DOI: 10.1038/s41586-023-06249-4 | PMCID: PMC10322716 | PMID: 37380764
- Evidence: Salmon’s transcript-level quantification DESeq2 was used to detect DEGs 59 using the following threshold: for liver samples, |log 2 [fold change]| > 1, adjusted P < 0.05; for tibialis anterior muscle samples: |log 2 [fold change]| > 0.6, adjusted P < 0.1.
- Full pipeline: quality control [MultiQC, Trim Galore] -> read trimming [Trim Galore] -> quantification [DESeq2] -> stage not stated [R, TwoSampleMR]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: Gene sets were built using the FindMarkers function in Seurat with test.use = ‘DESeq2’ and otherwise default parameters.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Single-cell quantification of ribosome occupancy in early mouse development. (Nature 2023)

- DOI: 10.1038/s41586-023-06228-9 | PMCID: PMC10307641 | PMID: 37344592
- Evidence: For every pair of consecutive developmental stages, differential RNA expression and translation efficiency was determined using DESeq2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ, R v4.0, Seurat]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Version used: **1.18.1**
- Evidence: Differential expression analysis was performed using DESeq2 (v.1.18.1) 67 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: The log 2 -transformed fold change was computed using the DESeq2 package (v.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### A cytosolic surveillance mechanism activates the mitochondrial UPR. (Nature 2023)

- DOI: 10.1038/s41586-023-06142-0 | PMCID: PMC10284689 | PMID: 37286597
- Version used: **1.18.1**
- Evidence: Data were then variance stabilized via the rlog function as implemented in DESeq2 (v.1.18.1) 33 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.7.1] -> stage not stated [DESeq2 v1.18.1, ImageJ v1.53, ggplot2 v3.3.3]

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Version used: **1.26.0**
- Evidence: Gene raw counts of each sample were extracted using featureCounts (v.1.6.3) 71 from aligned profiles for differential gene expression analysis using DESeq2 (v.1.26.0) 72 and converted to TPM value for sample distance calculation and visualization, as well as for gene expression pattern analysis.
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Evidence: Differential expression was determined with DESeq2 (Figs.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: Read count information was generated using HTSeq and normalized using DESeq2.
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Profiling the human intestinal environment under physiological conditions. (Nature 2023)

- DOI: 10.1038/s41586-023-05989-7 | PMCID: PMC10191855 | PMID: 37165188
- Evidence: ...ASVs across n = 268 analysed samples; limma-voom was used to calculate differential expression after size factors were estimated and normalized using DESeq2; P < 0.05, Benjamini–Hochberg correction).
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DADA2, DESeq2, R, limma v3.48.3] -> stage not stated [Bowtie2 v2.4.1, HMMER, phyloseq]

### Mitotic clustering of pulverized chromosomes from micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-05974-0 | PMCID: PMC10307639 | PMID: 37165191
- Evidence: Gene Set Enrichment Analysis (GSEA, v.4.3.2) 55 was performed using the weighted enrichment statistic on normalized gene counts computed using DESeq2 56 .
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> quantification [ImageJ] -> normalisation [DESeq2, GSEA v4.3.2, HTSeq v0.6.1p] -> differential/statistical testing [DESeq2, GSEA v4.3.2] -> stage not stated [BEDTools]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Evidence: Differentially expression analysis was performed using DESeq2 70 using the apeglm parameter 71 to accurately calculate log-transformed fold changes and setting a false-discovery rate of 0.05.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### Reducing brassinosteroid signalling enhances grain yield in semi-dwarf wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06023-6 | PMCID: PMC10156601 | PMID: 37100915
- Evidence: The differentially expressed genes were analysed using the DESeq2 R package.
- Full pipeline: alignment/mapping [TopHat] -> differential/statistical testing [DESeq2, R] -> stage not stated [ImageJ, VCFtools v0.1.13]

### Ageing-associated changes in transcriptional elongation influence longevity. (Nature 2023)

- DOI: 10.1038/s41586-023-05922-y | PMCID: PMC10132977 | PMID: 37046086
- Version used: **1.8.2**
- Evidence: To determine differentially expressed genes, we used DESeq2 version 1.8.2 (ref.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.5.1b, Trimmomatic] -> quantification [StringTie] -> differential/statistical testing [DESeq2 v1.8.2, GSEA] -> stage not stated [kallisto v0.42.5]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **1.24.0**
- Evidence: Gene expression distance RSEM raw read counts were first normalized using the median of ratios method implemented in DESeq2 (v.1.24.0) 65 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: After this, we performed a differential gene expression analysis using the DESeq2 R library (v.1.30.1) 110 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Evidence: The “Mouse DGE Analysis” sheet features for each gene, metrics output from DESeq2 and the top 2 principal components from the PCA analysis.
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### The dietary sweetener sucralose is a negative modulator of T cell-mediated responses. (Nature 2023)

- DOI: 10.1038/s41586-023-05801-6 | PMCID: PMC10033444 | PMID: 36922598
- Version used: **1.30**
- Evidence: DESeq2 (v1.30 (ref.
- Full pipeline: read trimming [Cutadapt v2.10, DADA2 v1.18] -> alignment/mapping [Cutadapt v2.10, RSEM v1.3.1] -> stage not stated [DESeq2 v1.30, R v4.0, STAR v2.7.6, phyloseq]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: Differentially expressed genes between WGD and control were determined using DESeq2 (ref.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### Fumarate induces vesicular release of mtDNA to drive innate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-05770-w | PMCID: PMC10017517 | PMID: 36890229
- Version used: **1.18.1**
- Evidence: Differential expression analysis was carried out with DESeq2 (v.1.18.1) 30 .
- Full pipeline: read trimming [Cutadapt v1.10.0] -> alignment/mapping [Cutadapt v1.10.0, STAR v2.6.0c] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2 v1.18.1] -> stage not stated [GSEA, ImageJ]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: Differential gene expression calling was performed on raw read counts with ≥2 T>C conversions using DESeq2 with the default settings, and with size factors estimated on corresponding total mRNA reads for global normalization.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Evidence: Differential expression was assessed with DESeq2 (ref.
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: To identify inducible ATAC-seq and H3K27ac peaks, we conducted a differential expression analysis using DeSeq2 (v.DESeq2_1.26.0) 59 on regions that had non-zero counts in at least two of the samples.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Version used: **1.24.0**
- Evidence: Differential gene expression was performed on the raw gene counts with the R package, DESeq2 (v.1.24.0) 69 , using replicates to compute within-group dispersion.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **1.30.1**
- Evidence: For each species, the DESeq2 (v.1.30.1) package 100 was used to normalize read counts across developmental stages (Supplementary Tables 13 – 21 ) and adult tissues (Supplementary Tables 49 – 51 ) and to perform pairwise differential gene expression analyses between consecutive developmental stages.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: With the quantified raw count for all samples, DESeq2 (ref.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Evidence: Colour codes reflect the activity predicted based on analysis of differential expression (DESeq2), upstream regulators analysis (QIAGEN’s IPA) and motif enrichment analysis in RNA-seq and ATAC-seq data.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Version used: **1.32.0**
- Evidence: For isoform analysis, normalized gene expression counts were compared for samples with and without a repeat expansion using the DESeq2 (v1.32.0) package in R (v4.0.5).
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Undecaprenyl phosphate translocases confer conditional microbial fitness. (Nature 2023)

- DOI: 10.1038/s41586-022-05569-1 | PMCID: PMC9876793 | PMID: 36450355
- Version used: **1.30.1**
- Evidence: Read matrices were then analysed with DESeq2 (version 1.30.1) using default settings in R (version 4.0.3) to identify differentially expressed genes.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.3] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, ImageJ v1.53, InterProScan, featureCounts]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: Differential gene expression analysis Differential gene expression (DGE) analysis was performed using Scanpy rank gene groups function (Wilcoxon rank-sum test with default parameters) and/or by pseudobulking (decoupler 85 ) and DESeq2 (ref.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Exaptation of ancestral cell-identity networks enables C&lt;sub&gt;4&lt;/sub&gt; photosynthesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08204-3 | PMCID: PMC11618092 | PMID: 39567684
- Evidence: Next, we identified partitioned expression patterns between cell types using an ANCOVA model implemented in DESeq2 (adjusted P < 0.05).
- Full pipeline: dimensionality reduction/clustering [Seurat, Signac, UMAP] -> differential/statistical testing [OrthoFinder] -> stage not stated [DESeq2, MACS2]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: For each modality, the top 3,000 variable features (genes or peaks) between all samples were selected using the R package DESeq2 (ref.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Differential gene expression was performed using the DESeq2 package 64 .
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: Sample normalization was carried out using the median-ratios normalization method from DESeq2 R package (v.1.30.1, RRID: SCR_015687 ), and differential expression analysis used DESeq2.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Version used: **1.32.0**
- Evidence: DESeq2 (v.1.32.0) 95 was used to normalize the read counts and calculate the log 2 [FC], standard error and Wald-test P values.
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Version used: **1.20.0**
- Evidence: The gene hit counts table was used for expression analysis using DESeq2 v.1.20.0 (ref.
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### Selective utilization of glucose metabolism guides mammalian gastrulation. (Nature 2024)

- DOI: 10.1038/s41586-024-08044-1 | PMCID: PMC11499262 | PMID: 39415005
- Version used: **1.40.1**
- Evidence: Analysis of differential gene expression was performed using DESeq2 (v1.40.1).
- Full pipeline: normalisation [Seurat v4.3.0] -> differential/statistical testing [DESeq2 v1.40.1] -> simulation/modelling [Slingshot v2.8.0] -> visualisation [Slingshot v2.8.0] -> stage not stated [ImageJ]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: DESeq2 was used to normalize counts (mean-ratio method), calculate total reads and determine differentially expressed genes 62 .
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **1.24.0**
- Evidence: DESeq2 (R v.3.6.1, DESeq2 v.1.24.0) 108 was used for library size normalization after batch correction.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors. (Nature 2024)

- DOI: 10.1038/s41586-024-07943-7 | PMCID: PMC11560846 | PMID: 39385035
- Evidence: Raw RNA-seq data underwent normalization and transformation using the vsd function from DESeq2.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> normalisation [DESeq2, Harmony v0.1.1, R, Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Calcium-permeable AMPA receptors govern PV neuron feature selectivity. (Nature 2024)

- DOI: 10.1038/s41586-024-08027-2 | PMCID: PMC11560848 | PMID: 39358515
- Evidence: We used DESeq2 (ref.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> stage not stated [DESeq2, ImageJ, Psychtoolbox, SciPy]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: Reads were counted for each GENCODE annotated gene using HTSeq (v.0.12.4) 60 and for caRNAs using featureCounts 64 , and then differentially expressed genes were called using DESeq2 package in R 65 with P < 0.05.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: To ascertain whether Ts21 HSCs expressed genes enriched for non-local regulation, pseudobulk differential expression was performed (DESeq2) between disomic and Ts21 HSCs.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: The differential expression analysis was performed using DESeq2 65 version 1.28.1, and the P values were corrected by the Benjamini–Hochberg method to maintain the false discovery rate (FDR) below 5%.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Early intermittent hyperlipidaemia alters tissue macrophages to fuel atherosclerosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07993-x | PMCID: PMC11464399 | PMID: 39231480
- Version used: **1.36.0**
- Evidence: Counts extracted with htseq-counts were used to perform the DEG analysis using DESeq2 (v.1.36.0; R package, v.4.2.1; https://www.r-project.org/ ) 53 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.4.4] -> visualisation [clusterProfiler v4.4.4] -> stage not stated [DESeq2 v1.36.0, R, Seurat v5.0.0]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: The Kallisto outputs were then imported into R using the tximport package, and the effect of ‘visit’ on whole blood mRNA expression was assessed using DESeq2 (ref.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Version used: **1.40.2**
- Evidence: Pseudobulk differential expression analysis was conducted using DESeq2 (v.1.40.2) 69 , excluding all public datasets.
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Probing plant signal processing optogenetically by two channelrhodopsins. (Nature 2024)

- DOI: 10.1038/s41586-024-07884-1 | PMCID: PMC11424491 | PMID: 39198644
- Evidence: Normalization and DEG analysis were carried out employing the DIANE package using DESeq2 and default parameters 77 .
- Full pipeline: alignment/mapping [fastp, kallisto] -> normalisation [DESeq2] -> stage not stated [PyMOL, R, pheatmap]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Evidence: Bulk RNA sequencing For differential gene expression analysis in R, low detection genes (minimum average read count <10) were filtered before DESeq2 analysis (v.1.16.1) 72 .
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Mitochondrial complex I promotes kidney cancer metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07812-3 | PMCID: PMC11424252 | PMID: 39143213
- Version used: **1.14.1**
- Evidence: Differentially expressed genes were identified by DESeq2 v1.14.1.
- Full pipeline: alignment/mapping [STAR v2.7.3] -> differential/statistical testing [DESeq2 v1.14.1, edgeR] -> stage not stated [HTSeq v0.6.1, ImageJ, R, featureCounts]

### Growth of complete ammonia oxidizers on guanidine. (Nature 2024)

- DOI: 10.1038/s41586-024-07832-z | PMCID: PMC11410670 | PMID: 39143220
- Evidence: Differential transcription was evaluated by treating different timepoints as replicates and comparing treatments as factors using DESeq2 90 .
- Full pipeline: alignment/mapping [ImageJ v1.54f] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ImageJ v1.54f, PyMOL, phytools] -> stage not stated [AlphaFold, BEDTools, HMMER]

### ILC2-derived LIF licences progress from tissue to systemic immunity. (Nature 2024)

- DOI: 10.1038/s41586-024-07746-w | PMCID: PMC11338826 | PMID: 39112698
- Version used: **1.18.1**
- Evidence: Sequence data were trimmed to remove adaptors and sequences with a quality score below 30 using Trim Galore (v.0.50, Babraham Bioinformatics) and then aligned to the mouse genome (GRCm38) using STAR (v.2.6.0a); differential expression was calculated using DESeq2 (v.1.18.1).
- Full pipeline: read trimming [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [tidyverse]

### Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07752-y | PMCID: PMC11291290 | PMID: 39048822
- Version used: **1.30.1**
- Evidence: All samples were normalized by regularized log transformation (rlogTransformation function) and variance stabilizing transformation (vst function), which are accomplished in the DESeq2 (v1.30.1) package.
- Full pipeline: normalisation [DESeq2 v1.30.1, limma] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [limma] -> stage not stated [R, Seurat, fgsea]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: Bulk RNA-seq differential expression analysis Differential expression analysis of bulk RNA-seq data from the ROSMAP cohorts was performed using DESeq2 119 (plotted) and edgeR 118 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **1.38.3**
- Evidence: Differential expression analysis was done using DESeq2 (v.1.38.3) 64 .
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Symbolic recording of signalling and cis-regulatory element activity to DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07706-4 | PMCID: PMC11357993 | PMID: 39020177
- Evidence: Differential activity analysis for 98 synthetic ENGRAM recorders between different cells was performed using DESeq2 (ref.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.3] -> alignment/mapping [Cutadapt, STAR v2.7.3] -> differential/statistical testing [DESeq2, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Jupyter]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Evidence: Then, the TSS activity levels are assessed for each replicate and each experimental condition by first counting the raw read coverage across each TSS and all experiments and normalizing the dataset using DESeq2’s rlog variance stabilizing transform (v.1.38.3) 78 .
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: Raw reads were trimmed by TrimGalore v.0.4.0 (Babraham Bioinformatics), mapped to mm10 by TopHat v.2.0.13 and analysed by DESeq2.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Version used: **1.36.0**
- Evidence: Differentially expressed genes were identified using R v4.2.0 using the Bioconductor package DESeq2 v1.36.0 using the Wald test for comparisons.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: DESeq2 was utilized to identify the differentially expressed genes between different conditions 65 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Plasmacytoid dendritic cells control homeostasis of megakaryopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07671-y | PMCID: PMC11254756 | PMID: 38987596
- Version used: **1.30.0**
- Evidence: GSEA To prepare the data for gene set enrichment analysis (GSEA), DESeq2 (v.1.30.0) analysis was performed using Galaxy with the default parameters 71 , 72 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [Monocle] -> stage not stated [DESeq2 v1.30.0, GSEA, Seurat]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: We used DESeq2 R package v.2.1.28.1 (ref.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### dsRNA formation leads to preferential nuclear export and gene expression. (Nature 2024)

- DOI: 10.1038/s41586-024-07576-w | PMCID: PMC11236707 | PMID: 38898279
- Evidence: Data were processed in the R/Bioconductor environment ( www.bioconductor.org , R v.3.6.1) using the DESeq2 package 54 ; v.1.24.0).
- Full pipeline: read trimming [Cutadapt v2.1, TopHat v2.1.1] -> alignment/mapping [Cutadapt v2.1, TopHat v2.1.1] -> quantification [featureCounts] -> stage not stated [BEDTools, Bioconductor, DESeq2]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: Differential gene expression and gene ontology analysis We used DESeq2 (ref.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Version used: **1.36.0**
- Evidence: DESeq2 (v1.36.0) was applied to the Oxford Nanopore dRNA-seq and Ultima RNA-seq data.
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### MYCT1 controls environmental sensing in human haematopoietic stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07478-x | PMCID: PMC11168926 | PMID: 38839950
- Version used: **1.26.0**
- Evidence: To investigate the differences between control, MYCT1 KD and MYCT1 OE HSCs, cells with more than 1 count for HLF were selected (HLF + ), the differentially expressed genes between HLF + cells in the different samples (control, KD and OE) were obtained using the Seurat FindMarkers function using the DESeq2 (v.1.26.0) test.
- Full pipeline: quantification [Bioconductor] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> stage not stated [AlphaFold, GSEA, R, Seurat v3.1.2]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Evidence: Reads that uniquely aligned to exonic regions were counted with HTSeq (v.0.9.1) 65 with the union setting to produce a count matrix for differential expression analysis using the DESeq2 (ref.
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: The raw count gene expression data were used to carry out differential gene expression for all of the clusters and bulk using the DESeq2 package (Supplementary Table 2 ). sncRNA-seq library preparation A 10–50 ng quantity of total RNA from round spermatids (50 ng; n = 3 per group) and cauda spermatozoa (10 ng; n = 3 per group) from mice fed on HFD or LFD for 2 weeks or cauda spermatozoa from mice ...
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Adhesive anti-fibrotic interfaces on diverse organs. (Nature 2024)

- DOI: 10.1038/s41586-024-07426-9 | PMCID: PMC11168934 | PMID: 38778109
- Evidence: Differential gene expression analysis was carried out using DESeq2 (ref.
- Full pipeline: quality control [Cutadapt, FastQC] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ v2.1.0]

### GLP-1-directed NMDA receptor antagonism for obesity treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07419-8 | PMCID: PMC11136670 | PMID: 38750368
- Version used: **1.30.1**
- Evidence: For differential expression testing, the R package DESeq2 (v.1.30.1) was used to identify differentially expressed genes.
- Full pipeline: differential/statistical testing [DESeq2 v1.30.1, R, limma v3.54.2] -> stage not stated [LDSC, MAGMA]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **1.34.0**
- Evidence: Differential expression was performed by passing the raw counts into the DESeq2 (v.1.34.0) package 73 .
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Discovery of WRN inhibitor HRO761 with synthetic lethality in MSI cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07350-y | PMCID: PMC11078746 | PMID: 38658754
- Evidence: Differential gene expression analysis between two conditions (treatment and control) was performed using DESeq2 (ref.
- Full pipeline: normalisation [R, fgsea] -> differential/statistical testing [DESeq2, R, fgsea] -> stage not stated [GSEA, PHENIX, SciPy]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Evidence: Next, aligned reads were counted for each D. melanogaster transcript (dmel_r6.36 annotation) using the featureCounts function from the Rsubread R package (v.2.0.1, isPairedEnd = TRUE) and differential expression analysis was performed using the DESeq2 R package 69 (v.1.26.0, design = ~replicate + condition).
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **1.36**
- Evidence: For tumour antigen-specific CD8 + T cells in tdLNs, tumour-infiltrating stem-like CD8 + T cells and their naive counterparts, data from a previous study 3 were processed using the R package DESeq2 (v.1.36) 55 .
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Version used: **3.16**
- Evidence: Differential analysis of gene expression was performed using the DESeq2 v.3.16 package, with an absolute log 2 -transformed fold change ≥0.5 and false discovery rate (FDR) < 0.05.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **1.38.3**
- Evidence: Differential expression was calculated using DESeq2 (1.38.3) 33 with a design consisting of two covariates: pegRNA and epegRNA plasmid set nucleofected (set 1 or 2) and cell line (K562 PEmax parental or La-ko4).
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: Differential expression analysis was performed with DESeq2 (using the default settings) in the R environment 76 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Version used: **1.12**
- Evidence: Transcriptomes were analysed and compared using DESeq2 (v.1.12) 74 .
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Evidence: DEGs were identified using edgeR 70 and DESeq2 71 .
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: Differential enhancer peaks (±3 kilobases from transcription start site) were identified using DESeq2 with FC > 1 and adjusted P < 0.05.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### On the genetic basis of tail-loss evolution in humans and apes. (Nature 2024)

- DOI: 10.1038/s41586-024-07095-8 | PMCID: PMC10901737 | PMID: 38418917
- Version used: **1.40.2**
- Evidence: Differentially expressed genes were detected using DESeq2 (v.1.40.2) 60 , using its default two-sided Wald test with the cut-off of log 2 (fold expression change) > 0.5 and multiple test-adjusted P value < 0.05.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BEDTools v2.30.0, STAR v2.7.2a] -> differential/statistical testing [DESeq2 v1.40.2]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Version used: **1.30.0**
- Evidence: Read distribution was estimated using the negative binomial generalized log-linear model implemented in the R Bioconductor package DESeq2 v.1.30.0 (ref.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Evidence: Gene set enrichment analysis (GSEA) was performed on unfiltered DESeq2 normalized count data using the DESeq2 package (v.1.40.2) 68 and GSEA v.4.3.2 software 69 , 70 in conjunction with MSigDB (v.2023.1).
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### IL-10 constrains sphingolipid metabolism to limit inflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07098-5 | PMCID: PMC10954550 | PMID: 38383790
- Evidence: Subsequently, we employed DESeq2 70 v1.26.0 R package to identify significantly differential genes between naive and TLR2-activated (24 h) wild-type and Il10 -KO BMDMs.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HTSeq, Picard] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v4.3.0]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: Selected genes were subjected to the hierarchical clustering analysis using the iDEP.91 pipeline that contains the DESeq2 package 53 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **1.18.0**
- Evidence: Reads were counted using the R package GenomicAlignments (v.1.14.0) 48 (mode=‘Union’, inter.feature=FALSE) and only primary read alignments were retained. rlog-transformed values of the counts and differential expression values were calculated using DESeq2 (v.1.18.0) 49 .
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Evidence: Internally this pipeline uses TEtranscripts 23 , which estimates both gene and TE transcript abundance in RNA-seq data and conducts differential expression analysis on the resultant count tables, which is carried out by DESeq2 (ref.
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Evidence: These raw counts were then normalized and analysed for differential gene expression using the DESeq2 package (v.1.35.0) (ref.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: DESeq2 96 was applied to the gene counts table to identify differentially expressed genes (DEGs).
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Circulating myeloid-derived MMP8 in stress susceptibility and depression. (Nature 2024)

- DOI: 10.1038/s41586-023-07015-2 | PMCID: PMC10901735 | PMID: 38326622
- Version used: **1.26.0**
- Evidence: Differential expression analysis was done using DESeq2 v1.26.0 package 67 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, HTSeq v0.12.4, STAR v2.5] -> quantification [ImageJ, Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Differential gene expression across timepoints or treatments with epigenetic inhibitors was computed using versions 1.16 or 1.22.2 of DESeq2 respectively 73 .
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Stress response silencing by an E3 ligase mutated in neurodegeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06985-7 | PMCID: PMC10881396 | PMID: 38297121
- Evidence: Differential gene-expression analysis was performed using DESeq2 (ref.
- Full pipeline: alignment/mapping [kallisto v0.48.0] -> quantification [kallisto v0.48.0] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, Cytoscape, Galaxy v2.11.40.7]

### Alternative splicing of latrophilin-3 controls synapse formation. (Nature 2024)

- DOI: 10.1038/s41586-023-06913-9 | PMCID: PMC10830413 | PMID: 38233523
- Evidence: Gene counts from the high-throughput sequencing dataset were analysed using two-sided Wald test of DESeq2 for bulk RNA-seq datasets, and two-sided Wilcoxon rank-sum tests for the scRNA-seq dataset.
- Full pipeline: alignment/mapping [STAR] -> quantification [scikit-image v0.20.0] -> stage not stated [CaImAn, DESeq2, HOMER, HTSeq, SciPy v1.10.1]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Evidence: For differential gene expression analysis, the package DESeq2 was used ( bioconductor.org/packages/release/bioc/html/DESeq2.html ).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Emergence of replication timing during early mammalian development. (Nature 2024)

- DOI: 10.1038/s41586-023-06872-1 | PMCID: PMC10781638 | PMID: 38123678
- Version used: **1.34.0**
- Evidence: Differential genomic bins between conditions (for example, ATAC-seq following α-amanitin treatment) were called by DESeq2 (v.1.34.0) with an adjusted P value cutoff of 0.05.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.3.5] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [BEDTools, ImageJ v1.53k, R v4.0.0, SAMtools v1.9]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: RNA-seq data were analysed in R with the DESeq2 package 50 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Mucosal boosting enhances vaccine protection against SARS-CoV-2 in macaques. (Nature 2024)

- DOI: 10.1038/s41586-023-06951-3 | PMCID: PMC10849944 | PMID: 38096903
- Evidence: DESeq2 was used for normalization.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.9a] -> quantification [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [GSEA]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: We then returned to the unfiltered count output from kallisto, performed a variance-stabilizing transformation (VST, DESeq2 55 (v.1.34.0)) to control for heteroskedasticity, and filtered the dataset to the same 837 MAGs.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: Differential expression analysis was conducted using DESeq2 and default settings within the iDEP.96 web interface 48 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Prime editing-installed suppressor tRNAs for disease-agnostic genome editing. (Nature 2025)

- DOI: 10.1038/s41586-025-09732-2 | PMCID: PMC12675287 | PMID: 41261131
- Evidence: Fastq reads were trimmed of adapter sequences using Trim Galore, aligned to the human genome using STAR, and differential expression analysis was performed using DESeq2 and custom R scripts.
- Full pipeline: read trimming [Bowtie2, DESeq2, STAR, Trim Galore] -> alignment/mapping [Bioconductor, Bowtie2, DESeq2, STAR, Trim Galore] -> differential/statistical testing [DESeq2, STAR, Trim Galore]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Version used: **1.26.0**
- Evidence: Differentially expressed gene analysis was performed with DESeq2 (v1.26.0) with a multifactor design formula that accounted for treatment and participant ID.
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: The raw counts were processed through a VST procedure using the DESeq2 package 82 to obtain transformed values that were more suitable than the raw read counts for certain data mining tasks.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Version used: **1.42.0**
- Evidence: DEG analysis Differential gene expression analysis was performed using the DESeq2 (v.1.42.0) 60 package in R (v.4.3.2).
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Evidence: The filtered count matrix was normalized using median of ratios method 67 implemented in DESeq2 package 68 .
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Evidence: Several comparisons were conducted—between each time point in parasites from ds GFP -injected mosquitoes as well as between parasites from ds EcR - and ds GFP -injected mosquitoes of the same time point—using a Python wrapper for the DESeq2 package in R 58 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Version used: **1.38.3**
- Evidence: Differential expression was performed with DESeq2 (v1.38.3) and enrichment analysis was performed with enrichR (v3.2) using genes with adjusted P < 0.05. ssGSEA scores for curated signatures (Supplementary Table 2 ) were calculated using the GSVA (v1.46) package and gene sets consisting of individual genes were compared using log 2 (reads per million + 1) values instead.
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: Quality control Quality control was conducted using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), DESeq2 (ref.
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: For differential gene expression analysis, we used DESeq2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Differential expression analysis was performed using DESeq2 72 , using a GRCm38, release 101 genome and index.
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: Differential expression analysis was performed using DESeq2, with FDR-adjusted P < 0.05 as a threshold for differential expression.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Evidence: Differential expression analysis was conducted using DESeq2 in R 64 , with effect size shrinkage using the apeglm package 65 .
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: Differential gene expression analysis was conducted using DESeq2, and downstream heat-map visualization was performed using the R package pheatmap. scRNA-seq used in this study was performed with samples from two sources: human PBMCs and mouse kidney cells.
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### Programmable antisense oligomers for phage functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09499-6 | PMCID: PMC12571901 | PMID: 40931073
- Evidence: Two independent replicates were merged by geometrical averaging and P values were calculated by the Wald test (two-sided) using DESeq2.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, ImageJ v1.53]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Additional R packages used include Presto, DESeq2, dplyr, ply, ape, cowplot, Matrix, variancePartition, MAST, HGNChelper, openxlsx, RColorBrewer, gridExtra, ggpubr, ComplexHeatmap, tidyverse, tibble, biomaRt, data.table, glmGamPoi, SeuratWrappers, patchwork, magrittr, s2, gplots, stringr, ggnewscale, ggbreak, coin and dunn.test.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Microbial iron oxide respiration coupled to sulfide oxidation. (Nature 2025)

- DOI: 10.1038/s41586-025-09467-0 | PMCID: PMC12545173 | PMID: 40866705
- Version used: **3.19**
- Evidence: Counts tables were analysed using DESeq2 release 3.19 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.407, RAxML v8.2.12] -> structure determination [RAxML v8.2.12] -> visualisation [R v4.1] -> stage not stated [AlphaFold v2.3.2, AutoDock Vina v1.1.2, DESeq2 v3.19, HMMER, ImageJ, featureCounts]

### Maternal stress triggers early-life eczema through fetal mast cell programming. (Nature 2025)

- DOI: 10.1038/s41586-025-09419-8 | PMCID: PMC12488486 | PMID: 40866704
- Version used: **1.34.0**
- Evidence: Count matrix values were transformed using regularized log transformation implemented in DESeq2 (v.1.34.0) 70 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2 v1.34.0, ImageJ v2.16.0, Seurat, Signac v1.14.0]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Differential gene expression was analysed using DESeq2 (ref.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Version used: **1.44.0**
- Evidence: Differential expression analysis was performed using DESeq2 (v.1.44.0).
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Version used: **1.36.0**
- Evidence: Statistics for DEGs were calculated by DESeq2 (v.1.36.0) (Supplementary Tables 4 and 7 ).
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: Differentially expressed genes between WM and GM were then identified using DESeq2 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Version used: **1.48.1**
- Evidence: DESeq2 (v.1.48.1) was used for this analysis, and genes with FDR-adjusted P values < 0.05 were considered to be differentially regulated.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### Elementary 3D organization of active and silenced E. coli genome. (Nature 2025)

- DOI: 10.1038/s41586-025-09396-y | PMCID: PMC12460168 | PMID: 40804527
- Evidence: Differential gene expression analysis and data visualization were performed with the DESeq2 package 72 .
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [BEDTools, Conda, HOMER v4.11.1]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: Differential gene expression analysis was done using DESeq2 (ref.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Excised DNA circles from V(D)J recombination promote relapsed leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-09372-6 | PMCID: PMC12443594 | PMID: 40770098
- Evidence: Differentially expressed genes were identified using DESeq2 with |logFC| > 0.585 and FDR < 0.05.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [Python]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Differential gene expression analysis For RNA-seq, overall and timepoint-specific differential gene expression results were obtained using the DESeq2 package (v1.36.0) by modelling the additive and interaction effect of timepoint and Acly KO.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### A gut sense for a microbial pattern regulates feeding. (Nature 2025)

- DOI: 10.1038/s41586-025-09301-7 | PMCID: PMC12443592 | PMID: 40702192
- Evidence: Pairwise comparisons between genes from the PYY–GFP + and PYY–GFP − groups were made using DESeq2.
- Full pipeline: alignment/mapping [featureCounts] -> stage not stated [BigStitcher, DESeq2, ImageJ]

### Precisely defining disease variant effects in CRISPR-edited single cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09313-3 | PMCID: PMC12488502 | PMID: 40702188
- Evidence: To perform differential expression analysis between T reg and T H 1 samples, we ran DESeq2 with default parameters on the raw counts matrix.
- Full pipeline: alignment/mapping [kallisto] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> stage not stated [GSEA, R, lme4]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **1.38.3**
- Evidence: Using gene expression quantifications from short-read RNA-seq data, we performed differential expression analysis using DESeq2 (v.1.38.3) 116 between individuals who carried and did not carry each SV, supplemented with outlier expression analysis for singleton SVs ( Supplementary Methods ).
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Evidence: Lists of DESeq2-detected upregulated and downregulated genes (that is, the upregulated and downregulated gene signature of Ly6C Low neutrophils) were also analysed using gProgileR with the same settings.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Then, log-normalized data considering only genes with ≥20 counts in 3 samples were used for differential expression analysis, making all possible comparisons within the same cell type using the DESeq2 R package 73 .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Version used: **1.24.0**
- Evidence: This object was imported into DESeq2 v.1.24.0 (ref.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **1.44.0**
- Evidence: We then used DESeq2 (v.1.44.0) 78 to identify genes differentially expressed between each treatment and the unperturbed community (DMSO controls).
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Evidence: Differential expression was calculated in R by DESeq2 time course analysis with LRT and the top 200 most differentially expressed genes (log 2 [FC]) across WT meristem maturation were used for PCA of all meristem samples using Python scikit-learn PCA.transform 66 .
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Version used: **1.42.1**
- Evidence: Differential gene expression analyses were then performed using the R package DESeq2 (v.1.42.1) 54 , with raw count data as input.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Nerve-to-cancer transfer of mitochondria during cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09176-8 | PMCID: PMC12328229 | PMID: 40562940
- Evidence: Read counts were normalized with DESeq2’s median-of-ratios method, and genes with expression below 1.0 (geometric mean) were filtered out.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Python, SAMtools] -> quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Python] -> stage not stated [GSEA]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: Gene level counts were measured using HTSeq and compared using DESeq2.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: The gene expression was analysed by DESeq2 128 .
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Version used: **1.46.0**
- Evidence: ...g the FindMarkers function from Seurat (v5.2.1) 67 ; (3) Nebula (v1.5.3) 20 for correcting sample-specific effects with covariate correction; and (4) DESeq2 (v1.46.0) 21 with covariate correction.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: Transcriptomics analysis The raw transcriptome files were prepared for Kallisto import to DESeq2 using the genecode annotation M16 ( https://www.gencodegenes.org/mouse/release_M16.html ) to correct for library size based on the provided average transcript length.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: Differential gene expression analysis was performed using the DESeq2 package 58 in R ( http://cran.r-project.org/ ), comparing the experimental conditions.
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Version used: **1.38.3**
- Evidence: DEGs were called using DESeq2 v.1.38.3 with design ‘~batch + genotype + treatment + genotype:treatment’.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Classification of LOY based on transcriptome data We used the DESeq2 R package (v.1.42.1) to uncover Y chromosome gene expression differences between LOY DNA and WTY DNA 47 .
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: ATAC–seq peaks were analysed for differential enrichment between samples using DESeq2 (ref.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Version used: **1.36.0**
- Evidence: Differential gene expression analysis was performed using the R (4.2.0) package DESeq2 (1.36.0).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: Counts matrices were analyzed using DESeq2 48 to calculate the enrichment (fold-change) and false discovery rate for each transcript compared between input and IP samples.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Evidence: Differential expression analysis was performed on two anterior replicates and three posterior replicates using R v.4.1.2 and DESeq2 (ref.
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Unravelling cysteine-deficiency-associated rapid weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-08996-y | PMCID: PMC12267064 | PMID: 40399674
- Version used: **1.48**
- Evidence: The differential gene expression analysis and visualization were performed with DESeq2 version 1.48 using Wald test 66 , 67 .
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [DESeq2 v1.48, SciPy v1.1.0] -> visualisation [DESeq2 v1.48] -> stage not stated [HTSeq, Python, R]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: Resulting HTSeq 73 matrices from bulk transcriptome were processed in R Studio with DESeq2 74 .
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: The read counts were processed in R using the DESeq2 package (v1.36).
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Version used: **1.28.1**
- Evidence: Differential expression analysis was performed using DESeq2 v.1.28.1 with a P adj threshold of 0.05 within R v.4.0.2.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Targeting the SHOC2-RAS interaction in RAS-mutant cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-08931-1 | PMCID: PMC12137120 | PMID: 40335703
- Evidence: Differential sgRNA representation was calculated using the DESeq2 package 40 .
- Full pipeline: differential/statistical testing [DESeq2, edgeR] -> stage not stated [Picard, R, fgsea, ggplot2 v3.3.6, ggpubr v0.4.0]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: DESeq2 was used to compute differentially expressed genes using lfcShrink(type=“apeglm”) and filtered using adjusted P < 0.001 and log fold change (lfc) > 0.5 criteria to obtain a list of statistically significant altered gene expression.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: Gene expression levels in different lines or organs under different treatments or at different developmental stages (at least three biological replicates for each sample) were analysed using DESeq2 (ref.
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Microbial metabolite drives ageing-related clonal haematopoiesis via ALPK1. (Nature 2025)

- DOI: 10.1038/s41586-025-08938-8 | PMCID: PMC12137129 | PMID: 40269158
- Evidence: These counts were then normalized and used to test for differential expression using negative binomial generalized linear models implemented by the DESeq2 R package (v.1.30.1).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [HISAT2] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, FastQC v0.11.8, R] -> stage not stated [MACS2, ggplot2, phyloseq]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Evidence: Differential expression analysis was performed using the DESeq2 55 pipeline, with DEGs being identified based on a threshold of 1.5-fold change and an adjusted P < 0.05, as determined using the Benjamini–Hochberg method 56 .
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **1.34.0**
- Evidence: Differential analysis of gene expression was performed using DESeq2 (1.34.0).
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Version used: **1.22**
- Evidence: Differential expression analysis was performed with the DESeq2 (v.1.22) Bioconductor package 40 , using a likelihood ratio test for data from time-course experiments.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Stress dynamically modulates neuronal autophagy to gate depression onset. (Nature 2025)

- DOI: 10.1038/s41586-025-08807-4 | PMCID: PMC12058529 | PMID: 40205038
- Evidence: Genes differential expression analysis was performed by DESeq2 software.
- Full pipeline: quantification [StringTie] -> differential/statistical testing [DESeq2]

### Plasticity of the mammalian integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-08794-6 | PMCID: PMC12119373 | PMID: 40140574
- Evidence: 24 datasets The datasets were analysed using DESeq2 (ref.
- Full pipeline: quality control [FastQC v0.11.4] -> read trimming [R] -> alignment/mapping [Bioconductor, HTSeq, featureCounts] -> quantification [ImageJ] -> normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [ImageJ] -> stage not stated [DESeq2]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Evidence: To identify the differentially accessible open chromatin regions, the raw nucleosome-free read was first normalized as counts per million followed by differential accessibility analysis by implementation of the negative binomial model in the DESeq2 R package (v.1.43.5).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: To explore similarities and dissimilarities between samples, count data were normalized using the variance stabilizing transformation function from the DESeq2 package.
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: For downstream analyses, the raw counts were normalized using the ‘rlog’ function of the DESeq2 R package.
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Aspirin prevents metastasis by limiting platelet TXA&lt;sub&gt;2&lt;/sub&gt; suppression of T cell immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-08626-7 | PMCID: PMC12018268 | PMID: 40044852
- Evidence: Differential gene expression analysis was performed on all expressed genes (>20 detected reads) using DESeq2 56 , and differentially expressed genes were further analysed and visualized using R.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3, QuPath]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Plots were generated using the ggplot2 R package (RRID:SCR_014601). sexDEG analysis To determine DEGs between sexes, we performed sample-pseudobulk-based DESeq2 (RRID:SCR_015687) differential expression testing for each cell type.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### TIR1-produced cAMP as a second messenger in transcriptional auxin signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-08669-w | PMCID: PMC12018254 | PMID: 40044868
- Evidence: Differential expression analysis use the DESeq2 package 29 .
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Glycocalyx dysregulation impairs blood-brain barrier in ageing and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08589-9 | PMCID: PMC11946907 | PMID: 40011765
- Version used: **1.32**
- Evidence: Differential gene expression analysis and visualization were performed using DESeq2 (v1.32) (Supplementary Data 5 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.32, Metascape] -> visualisation [DESeq2 v1.32] -> stage not stated [ImageJ, Seurat v4.1.1, SoupX v1.6.2, scDblFinder v2.0.4]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **1.28.1**
- Evidence: Both human and mouse RNA-seq counts were normalized using VST from the DESeq2 (v.1.28.1 and v.1.44.0) package 66 and then centred within a sample.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Tumour-wide RNA splicing aberrations generate actionable public neoantigens. (Nature 2025)

- DOI: 10.1038/s41586-024-08552-0 | PMCID: PMC11903331 | PMID: 39972144
- Evidence: Gene set enrichment analysis Differential gene expression of TCGA, GTEx and UCSF GBM and LGG RNA-seq was performed and quantified using DESeq2 (ref.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, R, RSEM] -> differential/statistical testing [DESeq2, GSEA, R] -> stage not stated [AlphaFold v2.3.2, Picard]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Evidence: RSubread/FeatureCounts (v.2.12.2) was used to calculate read counts, while differential expression analysis was performed using DESeq2 72 , 73 , with adjusted P < 0.05 used as the significance cut-off.
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Version used: **1.32.0**
- Evidence: Differential expression analysis To identify DEGs between pancreas- and tumour-innervating neurons, we used DESeq2 (v.1.32.0) on pseudobulk libraries.
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### Transcriptional adaptation upregulates utrophin in Duchenne muscular dystrophy. (Nature 2025)

- DOI: 10.1038/s41586-024-08539-x | PMCID: PMC11903304 | PMID: 39939773
- Evidence: The processed reads were aligned to the GRCh38/Gencode v46 genome using STAR, and transcript abundance was estimated using HT-Seq, followed by DESeq2 for differential expression analysis in patient myotubes or IsoDE2 for HEK293T cells.
- Full pipeline: alignment/mapping [DESeq2, STAR] -> quantification [DESeq2, STAR] -> differential/statistical testing [DESeq2, STAR]

### SKI complex loss renders 9p21.3-deleted or MSI-H cancers dependent on PELO. (Nature 2025)

- DOI: 10.1038/s41586-024-08509-3 | PMCID: PMC11864980 | PMID: 39910293
- Evidence: ...ats, n = 23) indicated. b , Relative viability of KP4 cells with the indicated CRISPR knockout gRNAs ± DOX-induced PELO knockdown. c , q -values from DESeq2 Wald test for differential expression between RNA sequencing from KP4 FOCAD knockout cells ± DOX-induced PELO knockdown plotted against log 2 -transformed fold change.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [ImageJ v1.53k, Picard, RSEM, SciPy]

### C-terminal amides mark proteins for degradation via SCF-FBXO31. (Nature 2025)

- DOI: 10.1038/s41586-024-08475-w | PMCID: PMC11821526 | PMID: 39880951
- Evidence: Differential gene expression analysis was performed using DESeq2 78 (v.1.42.1) with the default parameters.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [limma v3.58.1] -> differential/statistical testing [DESeq2, limma v3.58.1] -> visualisation [ChimeraX]

### The maternal X chromosome affects cognition and brain ageing in female mice. (Nature 2025)

- DOI: 10.1038/s41586-024-08457-y | PMCID: PMC11798838 | PMID: 39843739
- Evidence: Downstream differential expression analysis was performed using DESeq2.
- Full pipeline: quality control [FastQC] -> read trimming [STAR] -> alignment/mapping [Bismark, STAR] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, featureCounts]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: To this end, we used DESeq2 to normalize the pseudo-bulk-by-gene RNA count matrix, and then rescaled per-gene values.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Version used: **10.1186**
- Evidence: Differential gene expression DEX analysis was performed by the R package DESeq2 (10.1186/gb-2010-11-10-r106) and principal components analysis was performed by the R package prcomp.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **3.18**
- Evidence: Differentially expressed genes (DEGs) were identified by pairwise comparisons using DESeq2 v.3.18 package in R.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: Differential expression analyses were performed by DESeq2 (ref.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Version used: **1.34.0**
- Evidence: Gene counts for all 4 matched polysomal/sub-polysomal sample pairs collected under all 4 conditions of interest (ASP shSCR, ASP shGRIN2D, ASP shDHPS, NoASP shSCR) were processed simultaneously within the DESeq2 (v1.34.0; https://bioconductor.org/packages/release/bioc/html/DESeq2.html ) framework 32 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Engineered extrachromosomal oncogene amplifications promote tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08318-8 | PMCID: PMC11754114 | PMID: 39695225
- Evidence: Reads were mapped to mm10 using the STAR aligner 52 , and differential gene expression was calculated using the DESeq2 R package 53 .
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, R, STAR] -> quantification [MACS2 v3.0.0b, deepTools v3.5.3] -> differential/statistical testing [DESeq2, R, STAR] -> stage not stated [CNVkit v0.9.10, fgsea]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Version used: **1.22.2**
- Evidence: Differential gene expression analysis was performed using the package DESeq2 (v.1.22.2) 86 with DESeqDataSetFromMatrix() followed by DESeq2().
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Version used: **1.32.0**
- Evidence: DESeq2 (v1.32.0) 51 was used to identify differentially expressed genes and proteins between each sgRNA and non-targeting control sample within each cell-type and stimulation condition, using donor information as a covariate.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **1.26.0**
- Evidence: The peak atlas was obtained by expanding the peak summit by ±500 bp, and differential peaks were identified using DESeq2 (v1.26.0).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Macrophages excite muscle spindles with glutamate to bolster locomotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08272-5 | PMCID: PMC11735391 | PMID: 39633045
- Evidence: RNA-seq analysis was run using the COMBINE laboratory’s Salmon-DESeq2 pipeline.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [DESeq2, ImageJ, ggplot2, scDblFinder]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Evidence: Differential gene expression analysis on raw counts was performed using DESeq2, over-representation analysis with clusterProfiler v.4.4.4 and gene set enrichment analysis with fgsea v.1.22.0.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **1.38.3**
- Evidence: The VST transformation was performed using the DESeq2 (v.1.38.3) package 72 .
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **2.11.40.8**
- Evidence: The mapped reads were assembled with FeatureCounts (v.2.0.8) 59 , and differential gene expression was analysed using DESeq2 (v.2.11.40.8) 60 based on read counts.
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **1.38.3**
- Evidence: Differential expression analysis was performed using DESeq2 (v1.38.3) 70 , with significant genes defined by an adjusted P value < 0.05.
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: The DEGs using a pseudo-bulk count matrix were identified by using the functions ‘DESeqDataSetFromMatrix ‘, ‘DESeq’ and ‘results’ of the package ‘DESeq2’ 63 with the default testing parameters, which performed a Wald test and adjusted P values by means of the Benjamini–Hochberg procedure.
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Eosinophils drive intestinal remodelling and innate defence in reproduction. (Nature 2026)

- DOI: 10.1038/s41586-026-10531-6 | PMCID: PMC13233317 | PMID: 42129565
- Evidence: Differentially expressed genes between nulliparous and lactating conditions for eosinophils were identified using DESeq2 with a pseudobulk approach 50 .
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Scanpy v1.8.2]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **1.46.0**
- Evidence: Differential expression analyses between castrated mice and sham-surgery mice were performed using DESeq2 (v.1.46.0) 63 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **1.44.0**
- Evidence: We used DESeq2 (v.1.44.0) 69 to normalize the read counts and perform differential expression analysis.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: We then used the DESeq2 package to perform differential expression for each annotated niche versus all other niches.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: The resulting feature count matrix, along with the Bakta annotation of the t4 isolate genome, were used to perform differential expression analysis with the DESeq2 (ref.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **1.44**
- Evidence: Differentially expressed genes were identified using the DESeq2 (v1.44) package.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **1.50.2**
- Evidence: Significantly upregulated DEGs with an FDR < 0.05 were identified using the DESeq2 (v.1.50.2) package 74 in R.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **1.38**
- Evidence: We used DESeq2 (v.1.38) 91 to identify genes that were differentially expressed dependent on the frequency of donor mitochondria.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **1.38.3**
- Evidence: Differential expression analysis at the gene and gene set level (ssGSEA/GSEA) was performed using DESeq2 (v.1.38.3).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Evidence: For gene filtering, genes with >5 read counts and in >5 samples were retained before performing differential gene expression analysis with DESeq2.
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### DNA damage burden causes selective CUX2 neuron loss in neuroinflammation. (Nature 2026)

- DOI: 10.1038/s41586-026-10310-3 | PMCID: PMC13190333 | PMID: 41922773
- Evidence: DEG analyses DEGs for Cux2 cre Atf4 fl mice were determined in Omics playground 63 (v.2.8.19) by performing t -tests (standard, Welch) and limma (no trend, trend, voom), edgeR (QLF, LRT) and DESeq2 (Wald, LRT) tests and taking the highest q value for tests with cutoffs of a false-discovery rate (FDR) of 0.05 and a log 2 -transformed FC of 0.1.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, ggplot2 v3.5.1] -> differential/statistical testing [DESeq2, Python, edgeR, limma] -> visualisation [ggplot2 v3.5.1] -> stage not stated [CellProfiler, ImageJ, NumPy, Seurat]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Evidence: Primary PFA-EPN and ST-EPN tissue samples were integrated and normalized with the DESeq2 pipeline, and log-transformed counts of AR were compared with a two-sided Student’s t -test. scRNA-seq analysis of mouse data Alignment of raw reads CellRanger (10X Genomics) pipelines (v.3.0.2 and v.5.0.1) were used to process the raw sequencing data for the mouse developing hindbrain and the FCG data, respec...
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Evidence: Genes with low expression (expression count summed over all samples of less than 10) were filtered out from the input matrix to DESeq2.
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Evidence: Enrichment in TF binding sites in sets of H3K27ac peaks We selected seven sets of ChIP–seq peaks: peaks annotated to differentially expressed genes between IT and ET neurons (DESeq2 P Adj < 0.05; one set for upregulated genes and another for downregulated genes), peaks differentially enriched between IT and ET neurons (as determined by DESeq2 with FC > 2 and P Adj < 0.1; one set for IT neuron-bias...
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### The E3 ubiquitin ligase mechanism specifying targeted microRNA degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10232-0 | PMCID: PMC13083262 | PMID: 41851464
- Version used: **1.38.3**
- Evidence: ... and 30 reads across all six lines (three knockouts and three controls) and normalized for sequencing depth using the estimateSizeFactors function of DESeq2 (v.1.38.3) 87 .
- Full pipeline: read trimming [Cutadapt v4.8] -> quantification [R] -> normalisation [DESeq2 v1.38.3] -> differential/statistical testing [R] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **1.34.0**
- Evidence: Differential expression analysis was performed with DESeq2 version 1.34.0 (ref.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: Read count normalization and differential gene expression were performed using DESeq2 with default parameters (v1.42.0) 52 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Evidence: Differential expression analysis was performed using DESeq2 (ref.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **1.32.0**
- Evidence: 68 ) in RStudio (v.4.2) using the following packages: ape (v.5.5), vegan (v.2.6.4), DESeq2 (v.1.32.0), matrixStats (v.0.61.0), cowplot (v.1.1.1), broom (v.0.7.8), dplyr (v.1.0.7), tidyr (v.1.1.3) and tidyverse (v.2.0.0).
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **1.44.0**
- Evidence: Differential analyses of ICS scores between groups of individuals were performed with the R package DESeq2 (v.1.44.0).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: The summarized data were then assessed by statistical models (one-way ANOVA with Tukey’s HSD and the Benjamini–Hochberg for multiple gene correction) or STAR, featureCounts and DESeq2.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Version used: **1.5**
- Evidence: Sequencing results were analysed using Partek Flow (Illumina) running DESeq2 v.1.5.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: The data were processed in R using the DESeq2 package (v.1.46.0) for read normalization and variance stabilizing transformation 74 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Dynamic antigen expression and cytotoxic T cell resistance in HIV reservoir clones. (Nature 2026)

- DOI: 10.1038/s41586-026-10298-w | PMCID: PMC13190302 | PMID: 41735521
- Evidence: Differential expression was performed using DESeq2 with ARC clone identity as a blocking factor.
- Full pipeline: normalisation [Seurat v5.1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> visualisation [limma] -> stage not stated [MACS2]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Version used: **1.39.3**
- Evidence: Differential transcription versus translation analysis after BDNF DESeq2 v.1.39.3 was used to calculate RNA log 2 FC and P values for the comparisons between the BDNF 15′ and no-treatment and BDNF 60′ and no-treatment conditions.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Version used: **1.48.1**
- Evidence: 75 ) on normalized and transformed expression data processed by the R package DESeq2 v.1.48.1 (ref.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Version used: **1.30**
- Evidence: Summarized counts were imported into DESeq2 (v.1.30) 44 for differential expression testing according to instructions on the package vignette, only considering genes that were covered by at least ten reads across all samples.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### In vivo base editing of Chd3 rescues behavioural abnormalities in mice. (Nature 2026)

- DOI: 10.1038/s41586-026-10113-6 | PMCID: PMC12999480 | PMID: 41708849
- Evidence: Differential expression analysis was performed using the DESeq2 R package (v.1.20.0) 50 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> stage not stated [GSEA]

### Agouti integrates environmental cues to regulate paternal behaviour. (Nature 2026)

- DOI: 10.1038/s41586-026-10123-4 | PMCID: PMC13019464 | PMID: 41708861
- Evidence: Pseudocounts were extracted using the AggregateExpression function in Seurat with subsequent application of the DESeq2 68 .
- Full pipeline: read trimming [R, scDblFinder] -> dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [DESeq2, Seurat]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: Differentially accessible regions were identified using DESeq2 (ref.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### Cleavage of mRNAs by a minority of pachytene piRNAs improves sperm fitness. (Nature 2026)

- DOI: 10.1038/s41586-026-10102-9 | PMCID: PMC13061629 | PMID: 41639461
- Version used: **1.18.1**
- Evidence: Differential expression analysis was performed using DESeq2 (v.1.18.1) 65 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.18.1]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **1.22.2**
- Evidence: Filtered estimated read counts from RSEM were used for differential expression comparisons using the Wald test implemented in the R Bioconductor package DESeq2 v.1.22.2 based on generalized linear model and negative binomial distribution 70 .
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Evidence: TiCoNE25 was used to cluster differentially expressed genes as determined by DESeq2.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### GlycoRNA complexed with heparan sulfate regulates VEGF-A signalling. (Nature 2026)

- DOI: 10.1038/s41586-025-10052-8 | PMCID: PMC12999495 | PMID: 41606331
- Version used: **1.42.1**
- Evidence: Deduplicated transcript-level UMI counts were used for differential analysis in DESeq2 (v1.42.1).
- Full pipeline: read trimming [Cutadapt v4.9, DESeq2 v1.42.1] -> alignment/mapping [Bowtie2 v2.5.4] -> differential/statistical testing [DESeq2 v1.42.1] -> stage not stated [ImageJ, Python, SciPy]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Evidence: Raw mapped reads were processed in R (Lucent Technologies) 66 , using DESeq2 (ref.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: DESeq2 was used to analyse the RNA sequencing data, with the raw gene counts used as input.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Evidence: DESeq2 was used to compare expression at the 3-day, 3-week and 3-month time points to control animals for each cluster.
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Differentially expressed genes were identified using the DESeq2 R package 73 .
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: DEGs were identified using DESeq2 (ref.
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Version used: **1.14.1**
- Evidence: Differential gene expression was carried using DESeq2 (v.1.14.1) using the HOMER getDiffExpression.pl script with default normalization and replicates used to compute within-group dispersion.
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: Gene expression differences, between the conditions, were determined using DESeq2 56 (v.1.22.2) with |log 2 (fold change)| > 1 and adjusted P value <0.05 cut-offs.
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### A direct role for a mitochondrial targeting sequence in signalling stress. (Nature 2026)

- DOI: 10.1038/s41586-025-09834-x | PMCID: PMC7618714 | PMID: 41372412
- Version used: **1.48.1**
- Evidence: Differential expression analysis was conducted using DESeq2 (v1.48.1) with default parameters.
- Full pipeline: quantification [R v4.4.1, featureCounts] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [AlphaFold, BLAST v2.14.0, ImageJ]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **1.30.1**
- Evidence: To identify genes whose expression significantly varies across conditions, we applied a Likelihood Ratio Test (LRT) using DESeq2 (v.1.30.1) 60 , allowing the detection of global effects of a factor without the need to specify individual contrasts.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **1.28.0**
- Evidence: For differential gene expression analysis Seurat (v.4.1.3) was used, with parameter test.use set to DESeq2 (v.1.28.0) in the ‘FindMarkers’ function.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **1.42.1**
- Evidence: All raw count matrices were normalized using DESeq2 (v1.42.1 or v1.48.0).
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Version used: **1.36**
- Evidence: Counts were normalized by applying the variance-stabilizing transformation function from DESeq2 (v1.36) 59 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: The DESeq2 package 63 was then used to normalize these counts and perform differential gene expression testing, again blocking for confounding variables.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Differential expression analysis was performed using DESeq2 with regularized log-transformed counts.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Secretome translation shaped by lysosomes and lunapark-marked ER junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-09718-0 | PMCID: PMC12727531 | PMID: 41193816
- Evidence: Gene counts were generated using the STARsolo algorithm and subsequently analysed using a version of DESeq2 on MatLab.
- Full pipeline: read trimming [Cutadapt v2.10, STAR v2.7.5c] -> alignment/mapping [Cutadapt v2.10, STAR v2.7.5c] -> quantification [CellProfiler] -> stage not stated [DESeq2, ImageJ, TrackMate]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: For gene-expression profiling, RNA-seq data from all oat lines were mapped to the GS7 transcriptome using Kallisto 68 , and differential gene-expression analysis was performed with DESeq2 69 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Adult mouse and human organoids derived from thyroid follicular cells and modeling of Graves' hyperthyroidism. (PNAS 2021)

- DOI: 10.1073/pnas.2117017118 | PMCID: PMC8713972 | PMID: 34916298
- Evidence: Expression data were analyzed using DESeq2 ( 52 ).
- Full pipeline: stage not stated [DESeq2]

### The cyclic dinucleotide 2'3'-cGAMP induces a broad antibacterial and antiviral response in the sea anemone &lt;i&gt;Nematostella vectensis&lt;/i&gt;. (PNAS 2021)

- DOI: 10.1073/pnas.2109022118 | PMCID: PMC8713801 | PMID: 34903650
- Evidence: Reads were mapped to the N. vectensis transcriptome (NCBI: GCF_000209225.1) using kallisto, and differential expression was analyzed in R with DESeq2.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Clustal Omega, DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto]

### Genetic studies of human-chimpanzee divergence using stem cell fusions. (PNAS 2021)

- DOI: 10.1073/pnas.2117557118 | PMCID: PMC8713981 | PMID: 34921118
- Evidence: DE analysis between diploids and autotetraploid iPSCs was performed with DESeq2 ( 57 ), and genes with an adjusted P < 0.05 and at least a twofold change in expression were called as significant ( SI Appendix , Supplemental Materials and Methods ).
- Full pipeline: stage not stated [DESeq2]

### An ancient antimicrobial protein co-opted by a fungal plant pathogen for in planta mycobiome manipulation. (PNAS 2021)

- DOI: 10.1073/pnas.2110968118 | PMCID: PMC8670511 | PMID: 34853168
- Evidence: The DESeq2 extension of phyloseq was used to identify differentially abundant microbial genera ( 68 ).
- Full pipeline: alignment/mapping [HMMER, SAMtools] -> quantification [ImageJ, R v3.6.1, phyloseq] -> differential/statistical testing [DESeq2] -> visualisation [HMMER]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: Differentially expressed genes and normalized gene read counts were obtained using DESeq2 ( 74 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Version used: **1.22.2**
- Evidence: Differential gene expression analysis was performed using DESeq2 (version 1.22.2) ( 64 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Monoclonal antibody-mediated neutralization of SARS-CoV-2 in an IRF9-deficient child. (PNAS 2021)

- DOI: 10.1073/pnas.2114390118 | PMCID: PMC8609338 | PMID: 34702736
- Evidence: The gene-level read counts were normalized and log 2 -transformed with DESeq2, to obtain the gene expression profile for all samples.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.2] -> quantification [DESeq2, STAR, featureCounts v2.0.2] -> normalisation [DESeq2]

### The translatome of neuronal cell bodies, dendrites, and axons. (PNAS 2021)

- DOI: 10.1073/pnas.2113929118 | PMCID: PMC8639352 | PMID: 34670838
- Version used: **1.30.1**
- Evidence: Raw counts were fed into DESeq2 version 1.30.1 and log fold change (LFC) shrinkage was used ( 18 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt] -> alignment/mapping [Bowtie2 v2.3.5.1, STAR v2.7.3, featureCounts v2.0.0] -> stage not stated [DESeq2 v1.30.1, Python]

### Low-bias ncRNA libraries using ordered two-template relay: Serial template jumping by a modified retroelement reverse transcriptase. (PNAS 2021)

- DOI: 10.1073/pnas.2107900118 | PMCID: PMC8594491 | PMID: 34649994
- Evidence: DESeq2 was used to normalize read counts for each set of replicates before conversion to log 2 CPM, and the distributions for combined replicates are presented as violin plots.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Evidence: The DESeq2 package ( 55 ) was used for differential gene expression analysis.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### Engineered SARS-CoV-2 receptor binding domain improves manufacturability in yeast and immunogenicity in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2106845118 | PMCID: PMC8463846 | PMID: 34493582
- Evidence: Gene set enrichment analysis (GSEA) was performed with GSEA 4.1.0 using Wald statistics calculated by DESeq2 ( 62 ) and gene sets from yeast GO Slim ( 63 ).
- Full pipeline: differential/statistical testing [DESeq2, GSEA v4.1.0] -> stage not stated [ImageJ, edgeR v3.26.8]

### Transposition and duplication of MADS-domain transcription factor genes in annual and perennial <i>Arabis</i> species modulates flowering. (PNAS 2021)

- DOI: 10.1073/pnas.2109204118 | PMCID: PMC8488671 | PMID: 34548402
- Evidence: Asterisks indicate significant differences calculated using DESeq2 of the fold changes versus the first time point.
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [BWA, MUSCLE] -> normalisation [R] -> stage not stated [DESeq2]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Evidence: This was done using tximport ( 50 ) to load the dataset into DESeq2 ( 50 ) for differential expression analysis using a threshold of Log2 fold change >2 and an adjusted P value of <0.05.
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Investigating lymphangiogenesis in vitro and in vivo using engineered human lymphatic vessel networks. (PNAS 2021)

- DOI: 10.1073/pnas.2101931118 | PMCID: PMC8346860 | PMID: 34326257
- Evidence: Normalization and differential expression analyses were conducted using DESeq2 R package version 1.28.1 ( 40 ).
- Full pipeline: alignment/mapping [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, R]

### The p53 transcriptional response across tumor types reveals core and senescence-specific signatures modulated by long noncoding RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2025539118 | PMCID: PMC8346867 | PMID: 34326251
- Evidence: To compare mRNA levels in different conditions, normalization factors were determined for each sample using a DESeq2-like normalization approach ( 45 ).
- Full pipeline: alignment/mapping [StringTie, TopHat] -> normalisation [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Evidence: Differential expression analysis between two conditions/groups (three biological replicates per condition) was performed using DESeq2 R package.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Evidence: ...–supplementary-alignments ignore.” The PCA was performed on the expression data using the normalization procedure rlog() implemented in the R package DESeq2 and the plotPCA() function [version 1.22.2 ( 33 )].
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: The analysis of the PCA loadings, together with DESeq2 and sparse Least Square Discriminant Analysis (sPLSDA), revealed the enrichment in the oral microbiomes of the Mesolithic foragers and Neolithic farmers from the Danube Gorges and Italy, as well as the chimpanzees, of the pathways Trans-envelope signaling system VreARI, Sigma54-dependent transcription related gene cluster and protein secretion...
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### The DME demethylase regulates sporophyte gene expression, cell proliferation, differentiation, and meristem resurrection. (PNAS 2021)

- DOI: 10.1073/pnas.2026806118 | PMCID: PMC8307533 | PMID: 34266952
- Evidence: We used DESeq2 ( 80 ) to find DEGs between dme -2 mutants and Ler wild type.
- Full pipeline: read trimming [HISAT2 v2.1.0, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0] -> visualisation [R, ggplot2] -> stage not stated [DESeq2, StringTie v2.1.3]

### Dynamic chromatin regulatory landscape of human CAR T cell exhaustion. (PNAS 2021)

- DOI: 10.1073/pnas.2104758118 | PMCID: PMC8325267 | PMID: 34285077
- Evidence: Differential peak calling was done with DESeq2 ( 62 ) using transcription start site-annotated peaks as control loci or consistent “housekeeping peaks.” Clustering was performed using the regularized-log transform values from DESeq2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [BEDTools, DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2, Picard, R]

### Fever supports CD8<sup>+</sup> effector T cell responses by promoting mitochondrial translation. (PNAS 2021)

- DOI: 10.1073/pnas.2023752118 | PMCID: PMC8237659 | PMID: 34161266
- Evidence: Raw mapped read counts were processed in R (Lucent Technologies) with DESeq2 ( 40 ) to determine differentially expressed genes and generate normalized read counts, which were visualized using Morpheus (Broad Institute).
- Full pipeline: quality control [Galaxy, deepTools, featureCounts] -> read trimming [Galaxy, deepTools, featureCounts] -> alignment/mapping [DESeq2, Galaxy, R, deepTools, featureCounts] -> quantification [DESeq2, Galaxy, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [ImageJ, Metascape]

### CRISPR-based targeting of DNA methylation in <i>Arabidopsis thaliana</i> by a bacterial CG-specific DNA methyltransferase. (PNAS 2021)

- DOI: 10.1073/pnas.2125016118 | PMCID: PMC8201958 | PMID: 34074795
- Evidence: Differential expression analysis was performed using the DESeq2 software package ( 31 ).
- Full pipeline: alignment/mapping [Bismark, HTSeq] -> normalisation [deepTools] -> differential/statistical testing [DESeq2]

### Molecular design of the γδT cell receptor ectodomain encodes biologically fit ligand recognition in the absence of mechanosensing. (PNAS 2021)

- DOI: 10.1073/pnas.2023050118 | PMCID: PMC8256041 | PMID: 34172580
- Version used: **1.6.3**
- Evidence: The read counts were quantified at the exon level using subRead featureCounts (v1.4.4) software ( 87 ) and differential expression testing was performed using DESeq2 (v1.6.3) software ( 88 ).
- Full pipeline: alignment/mapping [SAMtools, STAR] -> quantification [DESeq2 v1.6.3, featureCounts v1.4.4] -> differential/statistical testing [DESeq2 v1.6.3, featureCounts v1.4.4]

### Photosynthesis-independent production of reactive oxygen species in the rice bundle sheath during high light is mediated by NADPH oxidase. (PNAS 2021)

- DOI: 10.1073/pnas.2022702118 | PMCID: PMC8237631 | PMID: 34155141
- Evidence: Differential-expression analysis was performed using DESeq2 ( 72 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> quantification [ImageJ, Trimmomatic] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [ggplot2]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Version used: **1.22.2**
- Evidence: The differential gene expression analysis was performed with the package DESeq2 (version 1.22.2) ( 38 ) in R.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: We used the plotPCA function in the DESeq2 package ( 101 ) to carry out principal component analysis.
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### Small noncoding RNA profiling across cellular and biofluid compartments and their implications for multiple sclerosis immunopathology. (PNAS 2021)

- DOI: 10.1073/pnas.2011574118 | PMCID: PMC8092379 | PMID: 33879606
- Evidence: Differential expression analysis was performed with DESeq2.
- Full pipeline: alignment/mapping [Trim Galore, featureCounts] -> differential/statistical testing [DESeq2, limma] -> stage not stated [BEDTools]

### Transcriptional profiling reveals signatures of latent developmental potential in <i>Arabidopsis</i> stomatal lineage ground cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021682118 | PMCID: PMC8092560 | PMID: 33875598
- Evidence: S3 C ), counts were normalized via DESeq2 ( 46 ) using default settings and differentially expressed genes (19,707 genes) were obtained from all possible pairwise comparisons with a false-discovery rate (FDR) < 0.05, then clustered via FANNY ( 47 ) with k = 5 and a probability cutoff of 0.6.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [Bowtie2, DESeq2] -> stage not stated [Fiji, ImageJ]

### Use of NAD tagSeq II to identify growth phase-dependent alterations in <i>E. coli</i> RNA NAD<sup>+</sup> capping. (PNAS 2021)

- DOI: 10.1073/pnas.2026183118 | PMCID: PMC8040648 | PMID: 33782135
- Evidence: The DESeq2 package ( 41 ) was adopted to calculate the difference in NAD-RNA levels and total transcript levels between stationary and exponential phases.
- Full pipeline: alignment/mapping [minimap2] -> quantification [ImageJ] -> differential/statistical testing [R v3.5] -> stage not stated [DESeq2]

### Incipient genome erosion and metabolic streamlining for antibiotic production in a defensive symbiont. (PNAS 2021)

- DOI: 10.1073/pnas.2023047118 | PMCID: PMC8092579 | PMID: 33883280
- Version used: **1.20.0**
- Evidence: The differential expression analysis was done using DESeq2 (v1.20.0) ( 91 ).
- Full pipeline: quality control [Bowtie2 v2.3.2, StringTie v1.3.3] -> read trimming [Bowtie2 v2.3.2, StringTie v1.3.3] -> alignment/mapping [Bowtie2 v2.3.2, StringTie v1.3.3] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [BLAST, ggplot2, ggpubr]

### Brd4-bound enhancers drive cell-intrinsic sex differences in glioblastoma. (PNAS 2021)

- DOI: 10.1073/pnas.2017148118 | PMCID: PMC8072233 | PMID: 33850013
- Evidence: The differential enrichment of H3K27ac signals between male and female analysis was carried out with DiffBind using DESeq2 (method = DBA_DESEQ2) with libraries normalized to total library size.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, HTSeq v0.11.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Predicting transcriptional responses to cold stress across plant species. (PNAS 2021)

- DOI: 10.1073/pnas.2026330118 | PMCID: PMC7958178 | PMID: 33658387
- Evidence: Read counts were used to identify cold-responsive genes by comparing the expression of genes in treatment vs. control samples, with differentially expressed genes defined as having adjusted P value < 0.05 and absolute log2 of fold change ≥ 2 at any of the six time points using DESeq2 ( 47 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [HTSeq v0.6.1, MAFFT v7.149, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [BEAST v5.1, DESeq2] -> simulation/modelling [BEAST v5.1] -> stage not stated [R]

### High-salt diet suppresses autoimmune demyelination by regulating the blood-brain barrier permeability. (PNAS 2021)

- DOI: 10.1073/pnas.2025944118 | PMCID: PMC7999868 | PMID: 33723078
- Version used: **1.26.1**
- Evidence: Gene-level abundance estimates were imported to DESeq2 (version 1.26.1) ( 34 ) with tximport (version 1.14.2) ( 35 ) for differential expression analysis.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [DESeq2 v1.26.1, kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.1, clusterProfiler v3.14.3, limma] -> visualisation [pheatmap, tidyverse]

### The imprinted lncRNA <i>Peg13</i> regulates sexual preference and the sex-specific brain transcriptome in mice. (PNAS 2021)

- DOI: 10.1073/pnas.2022172118 | PMCID: PMC7958240 | PMID: 33658376
- Evidence: DESeq2 ( 19 ) was used to identify differentially expressed genes.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### <i>Drosophila</i> Fezf functions as a transcriptional repressor to direct layer-specific synaptic connectivity in the fly visual system. (PNAS 2021)

- DOI: 10.1073/pnas.2025530118 | PMCID: PMC8020669 | PMID: 33766917
- Evidence: Differential expression was performed at the gene level using the R Bioconductor package DESeq2 ( 39 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2, MACS2 v2.1.1] -> stage not stated [Fiji, ImageJ]

### Lipid droplets in mammalian eggs are utilized during embryonic diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2018362118 | PMCID: PMC7958255 | PMID: 33649221
- Evidence: In all cases, differential expression analysis was performed with DESeq2 ( 47 ).
- Full pipeline: quality control [FastQC, TopHat] -> read trimming [FastQC, TopHat] -> alignment/mapping [FastQC, HTSeq, TopHat, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Acetogenic bacteria utilize light-driven electrons as an energy source for autotrophic growth. (PNAS 2021)

- DOI: 10.1073/pnas.2020552118 | PMCID: PMC7936347 | PMID: 33619098
- Evidence: RNA-seq data were then normalized by DESeq2 to compare transcript levels under the growth conditions ( 32 ).
- Full pipeline: normalisation [DESeq2]

### <i>Lactobacillus</i> bile salt hydrolase substrate specificity governs bacterial fitness and host colonization. (PNAS 2021)

- DOI: 10.1073/pnas.2017709118 | PMCID: PMC8017965 | PMID: 33526676
- Evidence: Expression levels were calculated based on the normalized transcripts per million and differential expression was performed with DESeq2 in Geneious.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2]

### A conserved long noncoding RNA, GAPLINC, modulates the immune response during endotoxic shock. (PNAS 2021)

- DOI: 10.1073/pnas.2016648118 | PMCID: PMC7896317 | PMID: 33568531
- Evidence: Differential gene-expression analyses were conducted using DESeq2.
- Full pipeline: alignment/mapping [minimap2] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> stage not stated [SPAdes]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Evidence: Differentially expressed genes were detected using the DESeq2 package (v1.20.0).
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### Muscle injury causes long-term changes in stem-cell DNA methylation. (PNAS 2022)

- DOI: 10.1073/pnas.2212306119 | PMCID: PMC9907067 | PMID: 36534800
- Evidence: Only significant genes with a DESeq2 baseMean (mean across all samples) above 5, and an absolute log2FoldChange greater than 5/sqrt (baseMean) + 0.6, were considered as significant for comparisons to methylation data and enrichment analyses.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> differential/statistical testing [R] -> stage not stated [DESeq2, HOMER, HTSeq v0.6.0, ImageJ]

### Precise spatial structure impacts antimicrobial susceptibility of <i>S. aureus</i> in polymicrobial wound infections. (PNAS 2022)

- DOI: 10.1073/pnas.2212340119 | PMCID: PMC9907066 | PMID: 36520668
- Version used: **1.36.0**
- Evidence: Differential expression was determined with DESeq2 v1.36.0 ( 66 ) with betaPrior set to true.
- Full pipeline: read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0]

### Temporal changes in plasma membrane lipid content induce endocytosis to regulate developmental epithelial-to-mesenchymal transition. (PNAS 2022)

- DOI: 10.1073/pnas.2212879119 | PMCID: PMC9907157 | PMID: 36508654
- Evidence: Transcripts were then counted using featureCounts ( 83 ), and differential expression analysis between premigratory and migratory gene expression was carried out using DESeq2 ( 84 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, featureCounts]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Evidence: ( A ) Identification of DEGs between unsynchronized HeLa and synchronized HeLa by DESeq2 (FDR<0.05, log2(fold change)>1 or <−1).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Transgenerational transmission of aspartame-induced anxiety and changes in glutamate-GABA signaling and gene expression in the amygdala. (PNAS 2022)

- DOI: 10.1073/pnas.2213120119 | PMCID: PMC9894161 | PMID: 36459641
- Evidence: DESeq2 ( 80 ) was used to generate a Principle Component Analysis (PCA) plot and to determine statistically significant DEGs (a False Discovery Rate, FDR, of <0.05 was used).
- Full pipeline: dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2]

### Inflammatory response to retrotransposons drives tumor drug resistance that can be prevented by reverse transcriptase inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2213146119 | PMCID: PMC9894111 | PMID: 36449545
- Evidence: Normalized counts and differential expression (DE) of genes were obtained using DESeq2 ( 52 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [featureCounts]

### Transcriptional control of cone photoreceptor diversity by a thyroid hormone receptor. (PNAS 2022)

- DOI: 10.1073/pnas.2209884119 | PMCID: PMC9894165 | PMID: 36454759
- Evidence: TRβ2-regulated ATAC peaks were identified by differential analysis of control and KO samples using DESeq2 (q < 0.05; fold-change >1.5, except for Ccdc136 , >1.4).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [deepTools] -> differential/statistical testing [DESeq2, MACS2 v2.2.7.1, edgeR] -> visualisation [deepTools]

### The RNA polymerase of cytoplasmically replicating Zika virus binds with chromatin DNA in nuclei and regulates host gene transcription. (PNAS 2022)

- DOI: 10.1073/pnas.2205013119 | PMCID: PMC9894162 | PMID: 36442102
- Evidence: RNA-seq reads were mapped to the human genome (hg38) with TopHat2, and differential expression analysis was performed using DESeq2.
- Full pipeline: alignment/mapping [DESeq2, TopHat] -> differential/statistical testing [DESeq2, TopHat]

### Transcriptome-based molecular subtypes and differentiation hierarchies improve the classification framework of acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2211429119 | PMCID: PMC9894241 | PMID: 36442087
- Version used: **1.28.0**
- Evidence: Normalization of the counts matrix was simultaneously computed based on the R DESeq2 (v1.28.0) ( 44 ) transformation and the Transcripts Per Kilobase Million (TPM) value, which were used as the gene expression matrix for downstream analysis.
- Full pipeline: alignment/mapping [kallisto v0.46.2] -> quantification [DESeq2 v1.28.0] -> normalisation [DESeq2 v1.28.0] -> dimensionality reduction/clustering [ComplexHeatmap] -> machine learning [Python]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: Read counts for each gene were calculated using HTseq ( 64 ) and loaded into R ( http://www.R-project.org/ ) (R Development Core Team, 2015) where DESeq2 ( 65 ) (v.1.28.1, https://bioconductor.org/packages/release/bioc/html/DESeq2.html ) was used to perform differential expression analysis on genes with at least one count per sample with alpha set to 0.05.
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Anti-mesothelin immunotoxin induces mesothelioma eradication, anti-tumor immunity, and the development of tertiary lymphoid structures. (PNAS 2022)

- DOI: 10.1073/pnas.2214928119 | PMCID: PMC9860319 | PMID: 36409889
- Evidence: Downloaded gene counts were normalized and the fold change comparing the responders against non-responders was calculated by using DESeq2 ( 43 ).
- Full pipeline: normalisation [DESeq2]

### EBF1 is continuously required for stabilizing local chromatin accessibility in pro-B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2210595119 | PMCID: PMC9860308 | PMID: 36409886
- Evidence: The differential gene expression was analyzed using the DESeq2 package ( 50 ), for exons and introns separately.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA, featureCounts]

### Tissue-specific regulation of lipid polyester synthesis genes controlling oxygen permeation into <i>Lotus japonicus</i> nodules. (PNAS 2022)

- DOI: 10.1073/pnas.2206291119 | PMCID: PMC9704718 | PMID: 36375074
- Evidence: The DESeq2 package v.1.36.0 ( 57 ) within R was used for differential expression (DE) analysis.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [ImageJ] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, R] -> stage not stated [RAxML, ggpubr v0.4.0.999, pheatmap]

### Mapping prohormone processing by proteases in human enteroendocrine cells using genetically engineered organoid models. (PNAS 2022)

- DOI: 10.1073/pnas.2212057119 | PMCID: PMC9674236 | PMID: 36343264
- Evidence: Differential gene expression analysis was performed using the DESeq2 package ( 32 ).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [DESeq2] -> visualisation [R, Seurat] -> stage not stated [ImageJ]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Evidence: To determine the relative enrichment of vOTUs along the horizontal field transect, we performed a differential abundance analysis with DESeq2 ( 98 ), using vOTU nonnormalized count tables as input.
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### An unexpected role for leucyl aminopeptidase in UV tolerance revealed by a genome-wide fitness assessment in a model cyanobacterium. (PNAS 2022)

- DOI: 10.1073/pnas.2211789119 | PMCID: PMC9659335 | PMID: 36322730
- Evidence: Differential expression analysis was conducted using the following R packages: Rsamtool (R package version 1.30.0), GenomeInfoDb (R package version 1.14.0.), GenomicFeatures ( 61 ), GenomicAlignments, GenomicRanges ( 61 ), and DESeq2 ( 62 ).
- Full pipeline: differential/statistical testing [DESeq2, R]

### Up-regulation of BTN3A1 on CD14<sup>+</sup> cells promotes Vγ9Vδ2 T cell activation in psoriasis. (PNAS 2022)

- DOI: 10.1073/pnas.2117523119 | PMCID: PMC9636952 | PMID: 36288286
- Evidence: Differentially expressed genes (DEGs) between HCs and PV patients were identified by DESeq2 using two replicas in each condition.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### SWAP1-SFPS-RRC1 splicing factor complex modulates pre-mRNA splicing to promote photomorphogenesis in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214565119 | PMCID: PMC9636961 | PMID: 36282917
- Evidence: RNA-seq data were first analyzed using the DESeq2 package, and then enriched Gene Ontology (GO) terms were determined using the GeneCodis4 online tool.
- Full pipeline: stage not stated [DESeq2, ImageJ]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Evidence: Gene expression was quantified with HTSeq, followed by the variance-stabilizing transformation from DESeq2.
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Evidence: Three replicates from each species were counted, and the counts were processed by using DESeq2 ( 98 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### <i>Arabidopsis</i> AAR2, a conserved splicing factor in eukaryotes, acts in microRNA biogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2208415119 | PMCID: PMC9565372 | PMID: 36191209
- Evidence: Differentially accumulated small RNAs were analyzed using the R package DESeq2 ( 67 ).
- Full pipeline: alignment/mapping [featureCounts v1.64] -> differential/statistical testing [DESeq2, R, featureCounts v1.64]

### DNA polymerase epsilon interacts with SUVH2/9 to repress the expression of genes associated with meiotic DSB hotspot in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208441119 | PMCID: PMC9564942 | PMID: 36191225
- Version used: **1.30.1**
- Evidence: ...ultNmax 1 –outFilterMultimapNmax 50 –outFilterMismatchNoverLmax 0.1.” DE genes and TEs (fold change ≥2 and P < 0.01) were identified by the R package DESeq2 version 1.30.1 ( 69 ) based on the gene expression matrix quantified by featureCounts version 2.0.0 ( 70 ).
- Full pipeline: read trimming [Bismark v0.22.3, Cutadapt, STAR v2.7.9a] -> alignment/mapping [Bismark v0.22.3, Bowtie2, Cutadapt, STAR v2.7.9a] -> quantification [Bismark v0.22.3, Cutadapt, DESeq2 v1.30.1, R, STAR v2.7.9a, featureCounts v2.0.0] -> stage not stated [ImageJ v1.52]

### FGFR redundancy limits the efficacy of FGFR4-selective inhibitors in hepatocellular carcinoma. (PNAS 2022)

- DOI: 10.1073/pnas.2208844119 | PMCID: PMC9546626 | PMID: 36179047
- Evidence: Sequencing reads were aligned to the Homo sapiens GRCh38 reference transcriptome to obtain raw read counts, and the differential expression genes were analyzed using DESeq2 ( 39 ) followed by filtering for average FPKM greater than 5, log 2 -transformed fold changes greater than 1 and 1.5, and adjusted P values less than 0.05 and 0.01 for HuH-7 and JHH-7, respectively.
- Full pipeline: alignment/mapping [DESeq2] -> quantification [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [pheatmap]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Evidence: DESeq2 software ( 91 ) was used for the analysis of differentially expressed genes.
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Monosomy X in isogenic human iPSC-derived trophoblast model impacts expression modules preserved in human placenta. (PNAS 2022)

- DOI: 10.1073/pnas.2211073119 | PMCID: PMC9546589 | PMID: 36161909
- Evidence: For differential expression using DESeq2 ( 109 ), count tables were filtered for genes with sufficient expression.
- Full pipeline: normalisation [GSEA, clusterProfiler] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler] -> stage not stated [WGCNA]

### Biosensors for inflammation as a strategy to engineer regulatory T cells for cell therapy. (PNAS 2022)

- DOI: 10.1073/pnas.2208436119 | PMCID: PMC9546553 | PMID: 36161919
- Evidence: Quality control of the count matrix and differential expression gene calling was performed with DESeq2 .
- Full pipeline: quality control [DESeq2] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [fgsea, ggplot2]

### Sperm-inherited H3K27me3 epialleles are transmitted transgenerationally in &lt;i&gt;cis&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2209471119 | PMCID: PMC9546627 | PMID: 36161922
- Evidence: Significantly misexpressed genes were determined using the differential analysis program DESeq2 from 50 bp reads.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> normalisation [R] -> differential/statistical testing [DESeq2, TopHat]

### Cryptic specialized metabolites drive <i>Streptomyces</i> exploration and provide a competitive advantage during growth with other microbes. (PNAS 2022)

- DOI: 10.1073/pnas.2211052119 | PMCID: PMC9546628 | PMID: 36161918
- Evidence: Transcript level normalization and analyses of differential transcript levels were conducted using DESeq2 ( 62 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Opportunistic binding of EcR to open chromatin drives tissue-specific developmental responses. (PNAS 2022)

- DOI: 10.1073/pnas.2208935119 | PMCID: PMC9546573 | PMID: 36161884
- Evidence: DESeq2 was used to normalize counts and identify differentially expressed genes ( P adj < 0.05, absolute log 2 fold change >1).
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Arsenite toxicity is regulated by queuine availability and oxidation-induced reprogramming of the human tRNA epitranscriptome. (PNAS 2022)

- DOI: 10.1073/pnas.2123529119 | PMCID: PMC9499598 | PMID: 36095201
- Evidence: The differential gene expression (DGE) analysis was performed using DESeq2 with default parameters ( 62 ).
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [ImageJ]

### Miat and interacting protein Metadherin maintain a stem-like niche to promote medulloblastoma tumorigenesis and treatment resistance. (PNAS 2022)

- DOI: 10.1073/pnas.2203738119 | PMCID: PMC9478675 | PMID: 36067288
- Evidence: Transcript abundance estimation in transcripts per million (TPM) and differential expression analysis were performed using DESeq2 ( 63 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.3] -> quantification [DESeq2] -> differential/statistical testing [DESeq2]

### Truncated Tau caused by intron retention is enriched in Alzheimer's disease cortex and exhibits altered biochemical properties. (PNAS 2022)

- DOI: 10.1073/pnas.2204179119 | PMCID: PMC9477417 | PMID: 36067305
- Evidence: Generalized linear model from DESeq2 ( 48 ) was applied to measure the differential IR ratio between control subjects and AD patients, where P value <0.05 was considered significant.
- Full pipeline: normalisation [ggplot2, tidyverse] -> differential/statistical testing [DESeq2, featureCounts v2.0.1]

### SARS-CoV-2 variant spike and accessory gene mutations alter pathogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2204717119 | PMCID: PMC9477415 | PMID: 36040867
- Version used: **4.1.0**
- Evidence: Genes with a mean count of at least 10 reads in at least one condition were subjected to differential expression analysis with DESeq2 v4.1.0 followed by pathway analysis using Ingenuity Pathway Analysis (Qiagen) ( 19 ).
- Full pipeline: alignment/mapping [Cutadapt v3.4, STAR v2.7.8a] -> differential/statistical testing [DESeq2 v4.1.0, R v4.1.1]

### USP13 promotes deubiquitination of ZHX2 and tumorigenesis in kidney cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2119854119 | PMCID: PMC9457248 | PMID: 36037364
- Version used: **1.14.1**
- Evidence: Transcript abundance was then estimated using salmon (v0.11.3), and differential expression was detected using DESeq2 (v1.14.1) ( 45 ).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.14.1] -> differential/statistical testing [DESeq2 v1.14.1]

### 3D chromatin remodeling potentiates transcriptional programs driving cell invasion. (PNAS 2022)

- DOI: 10.1073/pnas.2203452119 | PMCID: PMC9457068 | PMID: 36037342
- Evidence: Using DESeq2 ( 26 ), we detected 2,976 and 2,893 genes that were significantly transcriptionally altered in CTCF +/− 1 and 2, respectively, compared to CTL [basemean > 100, absolute log2 fold-change (abs(log2FC)) >1, adjusted P < 0.05].
- Full pipeline: quality control [R] -> stage not stated [DESeq2, GSEA, ImageJ, MACS2]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Differential expression analysis was performed via DESeq2 ( 45 ) v1.24.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### NAD&lt;sup&gt;+&lt;/sup&gt; metabolism drives astrocyte proinflammatory reprogramming in central nervous system autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2211310119 | PMCID: PMC9436380 | PMID: 35994674
- Evidence: Raw read counts were normalized using the DESeq2 R package ( 82 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [DESeq2, R] -> normalisation [DESeq2, R] -> stage not stated [Enrichr]

### Isolation of a virus causing a chronic infection in the archaeal model organism &lt;i&gt;Haloferax volcanii&lt;/i&gt; reveals antiviral activities of a provirus. (PNAS 2022)

- DOI: 10.1073/pnas.2205037119 | PMCID: PMC9436352 | PMID: 35994644
- Evidence: Differential expression analyses were performed with R package DESeq2 ( 51 ) and plotted using ggplots2 ( 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BLAST] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [SPAdes v3.13.1]

### A temporal gradient of cytonuclear coordination of chaperonins and chaperones during RuBisCo biogenesis in allopolyploid plants. (PNAS 2022)

- DOI: 10.1073/pnas.2200106119 | PMCID: PMC9407610 | PMID: 35969751
- Evidence: This ratio was statistically tested for departures from equivalence using DESeq2 ( Materials and Methods ).
- Full pipeline: differential/statistical testing [DESeq2]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Version used: **1.32.0**
- Evidence: Data from RNA-seq were processed in R version 4.1.0 (2021-05-18) using DESeq2 (v1.32.0), openxlsx (v4.2.4), ggplot2 (v3.3.5), and dplyr (v1.0.7).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### Intestinal tissue-resident T cell activation depends on metabolite availability. (PNAS 2022)

- DOI: 10.1073/pnas.2202144119 | PMCID: PMC9411733 | PMID: 35969785
- Evidence: All normalizations and differential expression analyses were performed in R (version 3.1.0) together with the DESeq2 Bioconductor package and the Negative Binomial Distribution method.
- Full pipeline: read trimming [Cutadapt v1.1] -> alignment/mapping [TopHat] -> normalisation [Bioconductor, DESeq2, R v3.1.0] -> differential/statistical testing [Bioconductor, DESeq2, R v3.1.0]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; induces a muted host response in human blood that blunts the recruitment of neutrophils. (PNAS 2022)

- DOI: 10.1073/pnas.2123017119 | PMCID: PMC9351360 | PMID: 35881802
- Evidence: Differential expression analysis was performed in R (v3.5.1) using DESeq2 ( 62 ).
- Full pipeline: alignment/mapping [Bowtie2 v3.1, HTSeq] -> differential/statistical testing [DESeq2, R v3.5.1] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [limma]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Evidence: TM194 was performed using DESeq2 ( 57 ) R package.
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### LOCOM: A logistic regression model for testing differential abundance in compositional microbiome data with false discovery rate control. (PNAS 2022)

- DOI: 10.1073/pnas.2122788119 | PMCID: PMC9335309 | PMID: 35867822
- Evidence: WRENCH ( 6 ) is also a normalization approach that estimates group-specific compositional factors to bring the read counts of null taxa across groups to a similar level and employs differential expression analysis based on the negative binomial distribution (DESeq2) to detect differentially abundant taxa.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, vegan]

### EBNA2-EBF1 complexes promote MYC expression and metabolic processes driving S-phase progression of Epstein-Barr virus-infected B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2200512119 | PMCID: PMC9335265 | PMID: 35857872
- Evidence: Error bars indicate SD, and asterisks indicate FDR < 0.001 calculated by DESeq2. dpi, days postinfection.
- Full pipeline: differential/statistical testing [DESeq2, GSEA]

### Orchestrated translation specializes dinoflagellate metabolism three times per day. (PNAS 2022)

- DOI: 10.1073/pnas.2122335119 | PMCID: PMC9335273 | PMID: 35858433
- Evidence: A total of 3,324 significant (p adj < 0.05) differences (as determined by pairwise comparisons of time points using DESeq2) between triplicate samples at the three times are shown as a clustered heatmap, with transcriptome entries represented by horizontal lines and RPF read counts on a color scale ( B ).
- Full pipeline: read trimming [Trim Galore] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R]

### Seed DNA damage responses promote germination and growth in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2202172119 | PMCID: PMC9335332 | PMID: 35858436
- Evidence: Differentially expressed genes for each comparison were identified through the DESeq2 package ( 50 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [SAMtools] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **1.30.1**
- Evidence: DESeq2 (v1.30.1) ( 50 ) was used for normalization and differential gene expression analysis.
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### Therapeutic functions of astrocytes to treat α-synuclein pathology in Parkinson's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2110746119 | PMCID: PMC9304026 | PMID: 35858361
- Version used: **1.32**
- Evidence: Expression in RNA-seq data is represented by the read count (RC) normalized using DESeq2 (v1.32) with the relative log expression (RLE) method (inside box) and Log2[Astrocyte/control Ctx-NSC] (color intensities).
- Full pipeline: quantification [DESeq2 v1.32] -> normalisation [DESeq2 v1.32] -> stage not stated [ImageJ, MACS2]

### The global succinylation of SARS-CoV-2-infected host cells reveals drug targets. (PNAS 2022)

- DOI: 10.1073/pnas.2123065119 | PMCID: PMC9335334 | PMID: 35858407
- Evidence: All transcripts were normalized and differentially analyzed in DESeq2 ( 47 ).
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [R v4.0.4, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Evidence: ControlOE) was carried out with the DESeq2 package in R ( 77 ).
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### Voltage-gated sodium channel &lt;i&gt;scn8a&lt;/i&gt; is required for innervation and regeneration of amputated adult zebrafish fins. (PNAS 2022)

- DOI: 10.1073/pnas.2200342119 | PMCID: PMC9282381 | PMID: 35867745
- Evidence: Differentially regulated transcripts were identified using featureCounts and DESeq2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [ImageJ]

### STING activation promotes robust immune response and NK cell-mediated tumor regression in glioblastoma models. (PNAS 2022)

- DOI: 10.1073/pnas.2111003119 | PMCID: PMC9282249 | PMID: 35787058
- Evidence: Differential expression analysis was performed with DESeq2 in R ( 91 ), with an FDR-adjusted P value threshold of ≤0.1.
- Full pipeline: alignment/mapping [STAR] -> quantification [QuPath] -> differential/statistical testing [DESeq2, R, ggplot2] -> stage not stated [Enrichr, ImageJ]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Evidence: We used the R package DESeq2 ( 31 ) on raw counts for identifying genes differentially expressed during embryogenesis —separately in the E f and the E d series— and using hpf as the explanatory variable.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### Immune checkpoint inhibitors unleash pathogenic immune responses against the microbiota. (PNAS 2022)

- DOI: 10.1073/pnas.2200348119 | PMCID: PMC9245641 | PMID: 35727974
- Evidence: Differential gene expression was calculated using DESeq2 (with HOMER’s getDiffExpression.pl) and genes with a fold change greater than 2 and FDR smaller than 0.05 were considered differentially expressed.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [HOMER, Metascape]

### Metatranscriptomics captures dynamic shifts in mycorrhizal coordination in boreal forests. (PNAS 2022)

- DOI: 10.1073/pnas.2118852119 | PMCID: PMC9245616 | PMID: 35727987
- Evidence: Differential expression analysis and variance stabilization transformation were carried out with DESeq2 ( 114 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Trimmomatic] -> differential/statistical testing [DESeq2] -> stage not stated [eggNOG]

### Integrated screens uncover a cell surface tumor suppressor gene <i>KIRREL</i> involved in Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2121779119 | PMCID: PMC9231494 | PMID: 35704761
- Evidence: The raw read counts of retained genes were submitted for differential expression analysis by DESeq2 software.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.3a] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [STRING db]

### Nuclear speckle integrity and function require TAO2 kinase. (PNAS 2022)

- DOI: 10.1073/pnas.2206046119 | PMCID: PMC9231605 | PMID: 35704758
- Evidence: The DESeq2 package was used for differential expression analysis between control and TAO2 knockdown, with Benjamini–Hochberg correction (false discovery rate < 0.05) ( 48 ).
- Full pipeline: quality control [STAR] -> read trimming [STAR, Trimmomatic] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor v3.11, R v4.0.2]

### Radioresistant cells initiate lymphocyte-dependent lung inflammation and IFNγ-dependent mortality in STING gain-of-function mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202327119 | PMCID: PMC9231608 | PMID: 35696583
- Evidence: FASTA sequencing files were then analyzed using a standard RNAseq pipeline (DolphinNext) ( 57 ) to perform sequence alignment (STAR), differentially expressed gene identification (DESeq2), and data visualization (DEBrowser).
- Full pipeline: alignment/mapping [DESeq2] -> differential/statistical testing [DESeq2] -> machine learning [QuPath] -> visualisation [DESeq2]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **1.30.1**
- Evidence: Expression values were normalized using the “median-of-ratios” method (implemented in DESeq2 v1.30.1) ( 53 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### GPR174 signals via G&lt;i&gt;α&lt;/i&gt;s to control a CD86-containing gene expression program in B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2201794119 | PMCID: PMC9191659 | PMID: 35639700
- Evidence: DESeq2 was used for the gene differential expression analysis and with GSEA software.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [MACS2, pheatmap]

### Polycomb-mediated genome architecture enables long-range spreading of H3K27 methylation. (PNAS 2022)

- DOI: 10.1073/pnas.2201883119 | PMCID: PMC9295753 | PMID: 35617427
- Evidence: Log 2 fold changes (log 2 FCs) and P values (cutoff of absolute value log 2 FC > 1 and Benjamini–Hochberg–adjusted P value < 0.05 for significance) calculated in DESeq2 for each anchor point deletion clone ( n = 3 replicates) relative to others.
- Full pipeline: differential/statistical testing [DESeq2]

### Caspase-4/11 exacerbates disease severity in SARS-CoV-2 infection by promoting inflammation and immunothrombosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202012119 | PMCID: PMC9173818 | PMID: 35588457
- Evidence: For data visualization, DESeq2 rlog transformation was used for principal component analysis (PCA).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [limma] -> visualisation [DESeq2] -> stage not stated [ComplexHeatmap]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Evidence: Gene counts were then generated from transcript abundance using tximport , and differential gene expression analysis was performed with DESeq2 .
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Version used: **1.32.0**
- Evidence: We used R 4.1.0 and DESeq2 version 1.32.0 ( 79 ) to perform pairwise differential expression analyses of each timepoint comparing control animals to animals exposed to ascr#10.
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### APOBEC3A regulates transcription from interferon-stimulated response elements. (PNAS 2022)

- DOI: 10.1073/pnas.2011665119 | PMCID: PMC9171812 | PMID: 35549556
- Evidence: We performed differential expression analysis of genes using DESeq2 ( 58 ).
- Full pipeline: read trimming [fastp] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, Bioconductor, R v4.0]

### Induction of human trophoblast stem-like cells from primed pluripotent stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2115709119 | PMCID: PMC9171790 | PMID: 35537047
- Version used: **1.32.0**
- Evidence: The counts were quantified and normalized by median of ratio method using the R package DESeq2 (v1.32.0) ( 49 ).
- Full pipeline: alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.32.0, R] -> normalisation [DESeq2 v1.32.0, R] -> differential/statistical testing [limma v3.48.3]

### MITF deficiency accelerates GNAQ-driven uveal melanoma. (PNAS 2022)

- DOI: 10.1073/pnas.2107006119 | PMCID: PMC9172632 | PMID: 35512098
- Version used: **1.30.1**
- Evidence: A PCA was performed with R version 4.0.3 using plotPCA on the top 500 variable genes from DESeq2 version 1.30.1.
- Full pipeline: quantification [QuPath] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2 v1.30.1, R v4.0.3] -> differential/statistical testing [Cytoscape] -> visualisation [GSEA]

### Genomewide CRISPR knockout screen identified PLAC8 as an essential factor for SADS-CoVs infection. (PNAS 2022)

- DOI: 10.1073/pnas.2118126119 | PMCID: PMC9170153 | PMID: 35476513
- Version used: **1.30.1**
- Evidence: Differential expression analysis was performed using DESeq2 version 1.30.1 under the Variable design.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [STAR v2.7.7a] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [R v4.0.3] -> stage not stated [Cytoscape, SAMtools v1.12, featureCounts]

### Postmitotic G1 phase survivin drives mitogen-independent cell division of B lymphocytes. (PNAS 2022)

- DOI: 10.1073/pnas.2115567119 | PMCID: PMC9170024 | PMID: 35476510
- Evidence: Following RNA-seq differentially expressed genes were identified using DESeq2 with false discovery rate (FDR) ≤0.05 for phase I and ≤0.1 for phase II ( n = 2).
- Full pipeline: differential/statistical testing [DESeq2]

### An antagonistic pleiotropic gene regulates the reproduction and longevity tradeoff. (PNAS 2022)

- DOI: 10.1073/pnas.2120311119 | PMCID: PMC9170148 | PMID: 35482917
- Evidence: Transcriptome and translatome changes were calculated using the Bioconductor package DESeq2 with adjusted P ≤ 0.05.
- Full pipeline: alignment/mapping [HTSeq v0.9.1] -> quantification [HTSeq v0.9.1] -> stage not stated [Bioconductor, DESeq2, ImageJ]

### Brap regulates liver morphology and hepatocyte turnover via modulation of the Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2201859119 | PMCID: PMC9171358 | PMID: 35476518
- Evidence: Differential expression analysis was performed with DESeq2 ( 27 ), and genes were classified as significantly regulated if the adjusted P value was <0.05.
- Full pipeline: quality control [FastQC] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [R]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Evidence: Fold changes of differential expression were estimated through DESeq2 ( 58 , 59 , 60 ).
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### Extracellular vesicles from triple negative breast cancer promote pro-inflammatory macrophages associated with better clinical outcome. (PNAS 2022)

- DOI: 10.1073/pnas.2107394119 | PMCID: PMC9169908 | PMID: 35439048
- Version used: **1.22.2**
- Evidence: Differential gene expression analysis was performed using DESeq2 (v1.22.2) ( 71 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [UMAP, pheatmap] -> stage not stated [Enrichr, MACS2, R, Seurat]

### The CHARGE syndrome ortholog CHD-7 regulates TGF-β pathways in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2109508119 | PMCID: PMC9169646 | PMID: 35394881
- Version used: **1.20.0**
- Evidence: Finally, the DEGs were determined using DESeq2 (v1.20.0) with a cutoff of 0.05 on false discovery rate (FDR).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.5.4a] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [Bioconductor v3.7, R v3.5]

### Signaling from the RNA sensor RIG-I is regulated by ufmylation. (PNAS 2022)

- DOI: 10.1073/pnas.2119531119 | PMCID: PMC9169834 | PMID: 35394863
- Evidence: Normalization and differential expression was carried out using the DESeq2 ( 70 ) Bioconductor ( 71 ) package with the R statistical programming environment.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [HTSeq]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: Differential expression between clusters of one cell type and all other clusters was executed using a Wald test in DESeq2 with the design formula “∼donor + is.thiscelltype”, where the factor ‘is.thiscelltype’ is set to TRUE for pseudobulk populations from the cluster of interest and FALSE for other clusters ( 84 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### Prevention of the foreign body response to implantable medical devices by inflammasome inhibition. (PNAS 2022)

- DOI: 10.1073/pnas.2115857119 | PMCID: PMC8944905 | PMID: 35298334
- Evidence: Differential gene expression was performed with the DESeq2 package (v1.18.1, R v3.4.0) ( 54 ) and, with the same package, read counts were normalized on the estimated size factors.
- Full pipeline: quality control [MultiQC v0.9, featureCounts v1.5.0] -> alignment/mapping [MultiQC v0.9, STAR] -> quantification [DESeq2, HTSeq, R v3.4] -> normalisation [DESeq2, R v3.4] -> dimensionality reduction/clustering [MultiQC v0.9] -> differential/statistical testing [DESeq2, R v3.4] -> stage not stated [ImageJ]

### Hatching is modulated by microRNA-378a-3p derived from extracellular vesicles secreted by blastocysts. (PNAS 2022)

- DOI: 10.1073/pnas.2122708119 | PMCID: PMC8944274 | PMID: 35298333
- Evidence: Differential expression between blastocyst EVs (three replicates) and nonblastocyst EVs (two replicates) was statistically tested in R (R version 4.0.3) ( 80 ) with DESeq2 ( 81 ) via a custom written R script.
- Full pipeline: differential/statistical testing [DESeq2, R v4.0.3] -> stage not stated [fgsea]

### Genomic adaptations for arboreal locomotion in Asian flying treefrogs. (PNAS 2022)

- DOI: 10.1073/pnas.2116342119 | PMCID: PMC9060438 | PMID: 35286217
- Version used: **1.30.0**
- Evidence: Counts of each sample were calculated using featureCounts in the Rsubread package ( 60 ), and differential expression analysis used DESeq2 v1.30.0 ( 61 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> differential/statistical testing [DESeq2 v1.30.0, featureCounts] -> stage not stated [BUSCO]

### Gain of gene regulatory network interconnectivity at the origin of vertebrates. (PNAS 2022)

- DOI: 10.1073/pnas.2114802119 | PMCID: PMC8931241 | PMID: 35263228
- Version used: **1.18.0**
- Evidence: Using Bedtools ( 38 ), the number of reads per called peak and per sample in both treatment and control conditions was subsequently computed, and a differential analysis was performed using DESeq2 v1.18.0 in R 3.4.3 ( 39 ).
- Full pipeline: alignment/mapping [Bowtie2, HTSeq, STAR v2.5.3a, kallisto] -> differential/statistical testing [DESeq2 v1.18.0, R v3.4] -> stage not stated [Cytoscape]

### A multiomic study uncovers a bZIP23-PER1A-mediated detoxification pathway to enhance seed vigor in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2026355119 | PMCID: PMC8892333 | PMID: 35217598
- Evidence: Differential expression of transcript was analyzed between the unaged seeds of Kasalath and Jigeng88 rice and across all the aging times for each cultivar using the likelihood ratio test in the DESeq2 or quasi-likelihood method in the EdgeR.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [Cytoscape v3.6] -> stage not stated [R, featureCounts]

### Specialized interferon action in COVID-19. (PNAS 2022)

- DOI: 10.1073/pnas.2116730119 | PMCID: PMC8931386 | PMID: 35217532
- Evidence: DESeq2 analysis, adjusting for age and sex as covariates, identified 2,299 genes differentially expressed in the blood of COVID-19 patients ( Fig.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Leg length and bristle density, both necessary for water surface locomotion, are genetically correlated in water striders. (PNAS 2022)

- DOI: 10.1073/pnas.2119210119 | PMCID: PMC8892508 | PMID: 35193982
- Evidence: A dedicated R script has been written to obtain the differentially expressed genes from RSEM read counts using the DESeq2 package ( 61 ).
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [DESeq2, RSEM] -> differential/statistical testing [DESeq2] -> structure determination [MUSCLE] -> stage not stated [RAxML]

### The dynamic trophic architecture of open-ocean protist communities revealed through machine-guided metatranscriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2100916119 | PMCID: PMC8851463 | PMID: 35145022
- Evidence: Differentially transcribed genes were identified with R using DESeq2 ( 80 ) with an adjusted P value cutoff of 0.05.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> normalisation [Trimmomatic v0.36, kallisto] -> differential/statistical testing [DESeq2] -> machine learning [XGBoost] -> stage not stated [HMMER v3.1b]

### Sirt6 regulates lifespan in <i>Drosophila melanogaster</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2111176119 | PMCID: PMC8812521 | PMID: 35091469
- Evidence: Transcript abundance was quantified using Salmon ( 50 ), and differential expression was calculated using the DESeq2 function in DEBrowser ( 51 ) using default parameters.
- Full pipeline: quantification [DESeq2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: Correlations between the replicate samples were analyzed using DESeq2 ( 8 ) with a sample distance matrix.
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### Molecular parallelism in signaling function across different sexually selected ornaments in a warbler. (PNAS 2022)

- DOI: 10.1073/pnas.2120482119 | PMCID: PMC8872772 | PMID: 35165176
- Evidence: We estimated gene expression using the normalized counts (log10-transformed) produced by DESeq2 ( 51 ).
- Full pipeline: alignment/mapping [R, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.1.0, HISAT2 v2.1.0, ImageJ, SAMtools v1.7]

### Loss of TET reprograms Wnt signaling through impaired demethylation to promote lung cancer development. (PNAS 2022)

- DOI: 10.1073/pnas.2107599119 | PMCID: PMC8832965 | PMID: 35110400
- Evidence: DEG analysis was performed by using DESeq2 package with the raw count.
- Full pipeline: read trimming [Trim Galore v0.5.0] -> stage not stated [DESeq2, Picard v2.21.2, RepeatMasker, SAMtools v1.4]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: Differential expression (DE) analyses were conducted using DESeq2 ( 63 ) ( E. nindensis , E. tef , and O. thomaeum ) or edgeR ( 23 ) ( S. stapfianus and S. pyramidalis ), and resulting outputs were processed using Pandas 0.25.0 in Python 3.6.8.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Genetic analysis of cancer drivers reveals cohesin and CTCF as suppressors of PD-L1. (PNAS 2022)

- DOI: 10.1073/pnas.2120540119 | PMCID: PMC8851563 | PMID: 35149558
- Evidence: Raw read counts were analyzed using DESeq2 ( 42 ) GSEA.
- Full pipeline: alignment/mapping [R, STAR v2.4.2a, featureCounts] -> quantification [DESeq2, GSEA, R, featureCounts]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Differential expression analysis was performed with DESeq2 ( 57 ), and genes were classified as significantly regulated if adjusted P value <0.05.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### MRP5 and MRP9 play a concerted role in male reproduction and mitochondrial function. (PNAS 2022)

- DOI: 10.1073/pnas.2111617119 | PMCID: PMC8832985 | PMID: 35121660
- Version used: **1.12.3**
- Evidence: Differentially expressed genes were then identified via both manual export, sorting and fold change annotation, as well as processed via DESeq2, version 1.12.3, for more complex analysis.
- Full pipeline: quality control [FastQC v0.11.7] -> differential/statistical testing [Bioconductor v3.4, DESeq2 v1.12.3, R v3.6.1] -> stage not stated [HOMER]

### MadR mediates acyl CoA-dependent regulation of mycolic acid desaturation in mycobacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2111059119 | PMCID: PMC8872791 | PMID: 35165190
- Evidence: The tools included 1) RoundRobin (in-house), 2) RankProduct ( 51 ), 3) significance analysis of microarrays (SAM) ( 52 ), 4) EdgeR ( 53 ), and 5) DESeq2 ( 54 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [DESeq2, R, edgeR]

### Differential interferon-α subtype induced immune signatures are associated with suppression of SARS-CoV-2 infection. (PNAS 2022)

- DOI: 10.1073/pnas.2111600119 | PMCID: PMC8872780 | PMID: 35131898
- Evidence: Differential gene expression of each condition was assessed using DESeq2 ( 69 ).
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [Pangolin]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: Raw counts of the reads mapped to genes were selected to extract differentially expressed genes using the DESeq2 Bioconductor package ( 58 ) with P value <0.05 and absolute log 2 (fold change) >1 as the threshold.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### Spatiotemporal analysis identifies ABF2 and ABF3 as key hubs of endodermal response to nitrate. (PNAS 2022)

- DOI: 10.1073/pnas.2107879119 | PMCID: PMC8794810 | PMID: 35046022
- Evidence: The gene counts for every sample were combined in a single file, and genes differentially expressed between the TF overexpression libraries and the empty vector libraries were identified using the DESeq2 package ( 80 ) and an FDR-adjusted P < 0.05.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEDTools, ImageJ, MACS2, R]

### Hemochromatosis drives acute lethal intestinal responses to hyperyersiniabactin-producing <i>Yersinia pseudotuberculosis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2110166119 | PMCID: PMC8764673 | PMID: 34969677
- Evidence: Analysis of differential gene expression was performed using the DESeq2 package in R.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> differential/statistical testing [DESeq2]

### Sex-specific splicing of Z- and W-borne <i>nr5a1</i> alleles suggests sex determination is controlled by chromosome conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2116475119 | PMCID: PMC8795496 | PMID: 35074916
- Version used: **1.26.0**
- Evidence: To assess the significance of the difference in female and male gonadal gene expression, a differential expression analysis was performed with DESeq2 (version 1.26.0) on read counts per gene.
- Full pipeline: alignment/mapping [BWA, Clustal Omega] -> quantification [DESeq2 v1.26.0] -> dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R, kallisto]

### Circadian key component CLOCK/BMAL1 interferes with segmentation clock in mouse embryonic organoids. (PNAS 2022)

- DOI: 10.1073/pnas.2114083119 | PMCID: PMC8746294 | PMID: 34930826
- Evidence: Differential gene expression in the RNA-seq data were determined using DESeq2 with thresholds of false discovery rate (FDR) < 0.05, fold change > 1.5, and expression level cutoff > 0.1 fragments per kilobase of exon per million mapped reads (FPKM) ( 47 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [DESeq2, Trimmomatic] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, pheatmap]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: The outputs from StringTie were processed using the DESeq2 package ( 59 ) in R ( https://www.r-project.org ) to identify differentially expressed genes.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### Structure and function of an effector domain in antiviral factors and tumor suppressors SAMD9 and SAMD9L. (PNAS 2022)

- DOI: 10.1073/pnas.2116550119 | PMCID: PMC8795524 | PMID: 35046037
- Evidence: The count table was analyzed by DESeq2 ( 31 ), and the significantly changed mRNAs were analyzed by PANTHER ( 32 ) to search enriched pathways.
- Full pipeline: stage not stated [DESeq2]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Evidence: Enrichment was determined using a two-sided Fisher’s exact test, and P values were corrected for multiple testing using the Benjamini–Hochberg method in R. rlog normalization of core genes was performed on all metatranscriptomes and transcriptomes together using DESeq2 with blind = TRUE in R ( 59 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### A dicer-related helicase opposes the age-related pathology from SKN-1 activation in ASI neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2308565120 | PMCID: PMC10756303 | PMID: 38113255
- Evidence: Read counts were then used for differential expression (DE) analysis using the R package DESeq2 created using R version 3.5.2.
- Full pipeline: read trimming [STAR v2.7.6a, Trim Galore] -> alignment/mapping [STAR v2.7.6a] -> quantification [DESeq2, R v3.5.2] -> differential/statistical testing [DESeq2, R v3.5.2] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.7.1, SAMtools v1.10]

### &lt;i&gt;GRASSY TILLERS1&lt;/i&gt; (&lt;i&gt;GT1&lt;/i&gt;) and &lt;i&gt;SIX-ROWED SPIKE1&lt;/i&gt; (&lt;i&gt;VRS1&lt;/i&gt;) homologs share conserved roles in growth repression. (PNAS 2023)

- DOI: 10.1073/pnas.2311961120 | PMCID: PMC10742383 | PMID: 38096411
- Evidence: Differential expression analysis was performed among ears sized 0.7 to 1.3 cm, when lower flower repression was observed in wild-type plants, using DESeq2 ( 82 ).
- Full pipeline: read trimming [STAR v2.7.9a, Trimmomatic] -> alignment/mapping [HTSeq, MAFFT, STAR v2.7.9a, Trimmomatic] -> differential/statistical testing [DESeq2] -> visualisation [IQ-TREE, R]

### An acetyltranferase moonlights as a regulator of the RNA binding repertoire of the RNA chaperone Hfq in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2311509120 | PMCID: PMC10710024 | PMID: 38011569
- Evidence: Gene expression levels of the hqbA mutants and the WT were compared by DESeq2 ( 44 ) and are shown in Datasets S1 and S2 , and in volcano plots using |log 2 (fold change)| greater than 1.0 and an adjusted p-value below 0.1 as the threshold.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [ImageJ] -> stage not stated [AlphaFold, UCSF Chimera]

### Transcriptional signatures of early-life stress and antidepressant treatment efficacy. (PNAS 2023)

- DOI: 10.1073/pnas.2305776120 | PMCID: PMC10710023 | PMID: 38011563
- Evidence: RNA-seq analyses for these datasets utilized the R packages “DESeq2,” “removeBatchEffect,” and “limma” ( 63 ).
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, limma]

### Peripheral blood TCR clonotype diversity as an age-associated marker of breast cancer progression. (PNAS 2023)

- DOI: 10.1073/pnas.2316763120 | PMCID: PMC10710020 | PMID: 38011567
- Evidence: Pre-ranked GSEA was performed using the FGSEA package (v1.24.0), while the DESeq2 package (v1.38.3) was used for the pre-ranking of gene expression.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [survival (R)] -> stage not stated [DESeq2, GSEA, QuPath, R v4.3]

### Integrated genomic and functional analyses of human skin-associated &lt;i&gt;Staphylococcus&lt;/i&gt; reveal extensive inter- and intra-species diversity. (PNAS 2023)

- DOI: 10.1073/pnas.2310585120 | PMCID: PMC10666031 | PMID: 37956283
- Evidence: DESeq2 package ( 60 ) was used for raw read normalization and differential expression analysis.
- Full pipeline: alignment/mapping [RAxML v1.1.0] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [DADA2, R v4.2, eggNOG, phyloseq]

### Bacterial tolerance to host-exuded specialized metabolites structures the maize root microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2310134120 | PMCID: PMC10622871 | PMID: 37878725
- Evidence: The following further R packages were used: Tidyverse ( 80 ), Broom ( 81 ), DECIPHER ( 82 ), DESeq2 ( 83 ), emmeans ( 84 ), ggthemes ( 85 ), multcomp ( 86 ), phyloseq ( 87 ), phytools ( 88 ), and vegan ( 89 ) in combination with some custom functions.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> stage not stated [DESeq2, R, RAxML v8.2.12, emmeans, phyloseq, phytools]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Version used: **1.34.0**
- Evidence: Differential expression was performed with the R package edgeR (v3.34.1) ( 57 ) or DESeq2 (v1.34.0) ( 58 ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: Differentially expressed genes were identified as (|log2 (fold-change)| ≥1.5 with q < 0.05) using the DESeq2 ( 79 ) (version 3.16).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Evidence: Differential gene expression of the miR-15/16 low vs. miR-15/16 high was then done using DESeq2 ( 86 ) and enrichment of DKO-specific MPP and WT-specific MPP gene signature within these DEGs was done with a Fisher’s test.
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Evidence: DESeq2 ( 54 ) was used to analyze small RNA enrichment on genes with a cutoff of P .adj. < 0.05, log2 fold change > |1| and > 10 reads in both replicates.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### Downregulation of apoptotic repressor <i>AVEN</i> exacerbates cardiac injury after myocardial infarction. (PNAS 2023)

- DOI: 10.1073/pnas.2302482120 | PMCID: PMC10589712 | PMID: 37816050
- Evidence: Differential gene expression analysis was performed using DESeq2 ( 52 ) with a statistical cutoff of FDR (False discovery rate) < 0.05 and fold change > 1.5.
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Disruption of the rice <i>4-DEOXYOROBANCHOL HYDROXYLASE</i> unravels specific functions of canonical strigolactones. (PNAS 2023)

- DOI: 10.1073/pnas.2306263120 | PMCID: PMC10589652 | PMID: 37819983
- Evidence: Differential gene expression was examined using DESeq2 and established by false discovery rate (FDR) ≤ 0.05 ( 54 ).
- Full pipeline: alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2]

### Endothelial deletion of EPH receptor A4 alters single-cell profile and Tie2/Akap12 signaling to preserve blood-brain barrier integrity. (PNAS 2023)

- DOI: 10.1073/pnas.2204700120 | PMCID: PMC10576133 | PMID: 37796990
- Evidence: Differential expression analysis was performed using DESeq2 ( 55 ).
- Full pipeline: quality control [FastQC, Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Trim Galore, scDblFinder]

### Cooperation and cheating orchestrate Vibrio assemblages and polymicrobial synergy in oysters infected with OsHV-1 virus. (PNAS 2023)

- DOI: 10.1073/pnas.2305195120 | PMCID: PMC10556616 | PMID: 37751557
- Version used: **1.36.0**
- Evidence: Finally, we used DESeq2 v1.36.0 and STAMP software ( 71 ) to identify ASVs with significant variation in abundance.
- Full pipeline: quantification [DESeq2 v1.36.0] -> differential/statistical testing [phyloseq] -> structure determination [RAxML] -> stage not stated [DADA2 v1.14, QIIME 2]

### Inducible CRISPR-targeted "knockdown" of human gut <i>Bacteroides</i> in gnotobiotic mice discloses glycan utilization strategies. (PNAS 2023)

- DOI: 10.1073/pnas.2311422120 | PMCID: PMC10523453 | PMID: 37733741
- Evidence: At each time point, the abundance of transcripts from each organism was modeled using DESeq2 ( 35 ) and tested for significant differences in expression (FDR-corrected P < 0.05).
- Full pipeline: alignment/mapping [BCFtools v1.12] -> quantification [DESeq2] -> differential/statistical testing [DESeq2]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We then used DESeq2 ( 78 ) on raw, filtered reads to quantify expression patterns by fitting a generalized linear model following a negative binomial distribution (Wald-test).
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: Analysis of differential gene expression was performed using DESeq2, accounting for conditions and replicates.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Version used: **1.18.1**
- Evidence: Differential expression analysis was performed with DESeq2 (1.18.1).
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### Cooperative regulation of coupled oncoprotein synthesis and stability in triple-negative breast cancer by EGFR and CDK12/13. (PNAS 2023)

- DOI: 10.1073/pnas.2221448120 | PMCID: PMC10515179 | PMID: 37695916
- Version used: **1.22.0**
- Evidence: Differential expression analysis was performed using DESeq2 v1.22.0 ( 90 ) running on R (v3.5.1).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [RSEM v1.2.25, STAR v2.4.1a] -> quantification [ImageJ, RSEM v1.2.25] -> differential/statistical testing [DESeq2 v1.22.0] -> stage not stated [Bioconductor]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: Differential expression at the gene level was determined using DESeq2 ( 61 ) with a false discovery rate of 0.1 and absolute log2 fold change value threshold of 0.1, correcting for rRNA ratio and sex.
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### Systems-level temporal immune-metabolic profile in Crimean-Congo hemorrhagic fever virus infection. (PNAS 2023)

- DOI: 10.1073/pnas.2304722120 | PMCID: PMC10500270 | PMID: 37669378
- Version used: **1.26.0**
- Evidence: DGE analysis with adjustment for confounding factors such as age, gender, cell type proportion, and other possible factors was performed using R/Bioconductor package DESeq2 v1.26.0 ( 40 ).
- Full pipeline: normalisation [R, limma v3.50.0] -> differential/statistical testing [R, limma v3.50.0] -> stage not stated [Bioconductor, DESeq2 v1.26.0, GSEA]

### CD45 alleviates airway inflammation and lung fibrosis by limiting expansion and activation of ILC2s. (PNAS 2023)

- DOI: 10.1073/pnas.2215941120 | PMCID: PMC10483638 | PMID: 37639581
- Evidence: Differential gene expression and PCA were performed using rlog-normalized dRNA-seq data by DESeq2 ( 66 ).
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Metascape]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Version used: **1.30.1**
- Evidence: Briefly, mapped reads were assigned to annotated genes using featureCounts version 1.6.3, and differentially expressed genes were identified using DESeq2 version 1.30.1 with a 5% false discovery rate ( 33 ).
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### SARS-CoV-2 Mac1 is required for IFN antagonism and efficient virus replication in cell culture and in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2302083120 | PMCID: PMC10468617 | PMID: 37607224
- Evidence: DESeq2 was used to identify DEGs between the SARS-CoV-2 WT and ΔMac1-infected samples using simply “treatment” as a factor.
- Full pipeline: stage not stated [DESeq2]

### The mRNA stability factor Khd4 defines a specific mRNA regulon for membrane trafficking in the pathogen <i>Ustilago maydis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2301731120 | PMCID: PMC10450656 | PMID: 37590419
- Evidence: Differential gene expression analysis comparing RNA-seq data was performed using DESeq2.
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape, R]

### Triple-negative breast tumors are dependent on mutant p53 for growth and survival. (PNAS 2023)

- DOI: 10.1073/pnas.2308807120 | PMCID: PMC10450424 | PMID: 37579145
- Evidence: The raw count data were processed and normalized by DESeq2 software to identify differentially expressed genes (DEGs) between the two groups ( 33 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Evidence: DESeq2 Bioconductor package v1.40.0 ( 55 ) was used on the RNA-Seq data to conduct differential expression analyses.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### Targeting STING oligomerization with small-molecule inhibitors. (PNAS 2023)

- DOI: 10.1073/pnas.2305420120 | PMCID: PMC10434303 | PMID: 37549268
- Evidence: Differential gene expression for volcano plots was performed using Salmon v1.6.0 ( 37 ) on the GRCm39 transcriptome and the R DESeq2 ( 38 ) package.
- Full pipeline: differential/statistical testing [DESeq2]

### Engineered calprotectin-sensing probiotics for IBD surveillance in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2221121120 | PMCID: PMC10410751 | PMID: 37523538
- Version used: **1.32.0**
- Evidence: Differential expression between treatments and media conditions using DESeq2 (v1.32.0) was analyzed after removal of genes with <10 assigned counts.
- Full pipeline: alignment/mapping [STAR v2.7.5] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [R v4.0.3, ggplot2 v3.3.0, pheatmap v1.0.12]

### A Mediator subunit imparts robustness to a polyphenism decision. (PNAS 2023)

- DOI: 10.1073/pnas.2308816120 | PMCID: PMC10410750 | PMID: 37527340
- Evidence: 4.1.1 using DESeq2 ( 81 ).
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [BLAST, DESeq2]

### Mitochondrial sulfide promotes life span and health span through distinct mechanisms in developing versus adult treated &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2216141120 | PMCID: PMC10410709 | PMID: 37523525
- Evidence: After RNA sequencing data preprocessing (see SI Appendix , Supplemental Methods section), the DESeq2 package for R ( 88 ) was used to test for differential gene expression.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **1.36.0**
- Evidence: Read count matrices were obtained with featureCounts v2.0.1 and differential expression assessed with DESeq2 v1.36.0 ( 78 ) using a FDR < 0.05 and log2 FC > ± 1.0.
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Activin E-ACVR1C cross talk controls energy storage via suppression of adipose lipolysis in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2309967120 | PMCID: PMC10410708 | PMID: 37523551
- Evidence: Differential gene expression analysis was performed using the DESeq2 package ( 53 ).
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2]

### Host hydrocarbons protect symbiont transmission from a radical host defense. (PNAS 2023)

- DOI: 10.1073/pnas.2302721120 | PMCID: PMC10400980 | PMID: 37487102
- Version used: **1.22.2**
- Evidence: The retained reads were mapped to either the S. coelicolor or S. philanthi genome ( 50 ) using Bowtie2 (v.2.3.2) and StringTie (v.1.3.3b) implemented in KBase ( 98 ) using default settings. rRNA sequences were removed from the dataset before differential gene expression was analyzed using DESeq2 (v.1.22.2) ( 99 ) in RStudio (v1.1.453 with R v3.5.0).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> differential/statistical testing [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> visualisation [ggplot2]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: Indeed, when we independently defined differentially expressed genes between WT and NFIA-Tg adipocytes using DESeq2 ( 16 ), we observed that the Ox-Phos gene set (N = 200) and inflammatory response gene set (N = 200) were reciprocally regulated by NFIA-Tg ( Fig.
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### Disulfiram blocks inflammatory TLR4 signaling by targeting MD-2. (PNAS 2023)

- DOI: 10.1073/pnas.2306399120 | PMCID: PMC10401014 | PMID: 37487070
- Evidence: R package DESeq2 was used to analyze differential expression and fold change.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2, R, pheatmap]

### MicroRNA-335-5p suppresses voltage-gated sodium channel expression and may be a target for seizure control. (PNAS 2023)

- DOI: 10.1073/pnas.2216658120 | PMCID: PMC10372546 | PMID: 37463203
- Evidence: CA1: P = 0.0019, CA3: P = 0.0055, DG: P = 0.00025; pairwise comparison using DESeq2.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [ComplexHeatmap, DESeq2, R, tidyverse]

### IL-7R licenses a population of epigenetically poised memory CD8<sup>+</sup> T cells with superior antitumor efficacy that are critical for melanoma memory. (PNAS 2023)

- DOI: 10.1073/pnas.2304319120 | PMCID: PMC10372654 | PMID: 37459511
- Evidence: Differential expression analysis was performed with DESeq2.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, STAR, featureCounts] -> alignment/mapping [STAR, featureCounts] -> quantification [STAR, featureCounts] -> differential/statistical testing [DESeq2, R v4.0] -> stage not stated [RSEM]

### Ancient vertebrate dermal armor evolved from trunk neural crest. (PNAS 2023)

- DOI: 10.1073/pnas.2221120120 | PMCID: PMC10372632 | PMID: 37459514
- Evidence: Transcript counts were calculated using featureCounts ( 58 ), and DGE analysis was performed using DESeq2 ( 59 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega v1.2.3] -> visualisation [ComplexHeatmap] -> stage not stated [DESeq2, featureCounts]

### Functional calcium-responsive parathyroid glands generated using single-step blastocyst complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2216564120 | PMCID: PMC10334775 | PMID: 37379351
- Evidence: Normalization and DEG analysis were performed using DESeq2 in Galaxy and visualized using ggplot2 in R v4.1.2.
- Full pipeline: normalisation [DESeq2, R v4.1, ggplot2] -> dimensionality reduction/clustering [UMAP] -> visualisation [DESeq2, R v4.1, ggplot2] -> stage not stated [Seurat v4.2.1, tidyverse]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: Differential expression analyses between cell subpopulations were performed using DESeq2 ( 65 ) on the raw read count matrix, whereby the Wald test was used for hypothesis testing.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### ZBTB20 is essential for cochlear maturation and hearing in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2220867120 | PMCID: PMC10268240 | PMID: 37279265
- Version used: **1.4.5**
- Evidence: Significant DEGs between WT control and OV-ZB20KO cochleae were analyzed using DESeq2 (v1.4.5) based on |log2FC|≥1 and Q-value≤0.05, and genes with FPKM<5 in both groups were filtered.
- Full pipeline: quantification [DESeq2 v1.4.5]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Version used: **1.30.0**
- Evidence: DESeq2 (v1.30.0) was utilized to normalize raw counts to read depth, perform PC analysis, and carry out differential expression analysis.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Paf1 complex subunit Rtf1 stimulates H2B ubiquitylation by interacting with the highly conserved N-terminal helix of Rad6. (PNAS 2023)

- DOI: 10.1073/pnas.2220041120 | PMCID: PMC10235976 | PMID: 37216505
- Evidence: To perform the spike-in correction of S. cerevisiae counts, K. lactis read counts (mapping to sense strands only) were fed into DESeq2 ( 54 ) to estimate replicate-specific size factors.
- Full pipeline: alignment/mapping [DESeq2, STAR v2.7.5a] -> quantification [DESeq2] -> stage not stated [AlphaFold, ComplexHeatmap, featureCounts]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: Differential expression analysis was performed using DESeq2 ( 54 ), and genes with an adjusted P -value <0.05 and absolute log2(fold change) > 1 were considered differentially expressed.
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Aneuploidy effects on human gene expression across three cell types. (PNAS 2023)

- DOI: 10.1073/pnas.2218478120 | PMCID: PMC10214149 | PMID: 37192167
- Evidence: ...mapping female samples and with the YPAR-gene masked one when mapping male samples to reduce misaligning between the X and Y chromosomes ( 49 ), iii) DESeq2 ( 50 ) to compare gene expression values across samples with different SCD while adjusting for measured covariates of batch and age, and surrogate variables (SVs) determined by sva package ( 51 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [DESeq2, FastQC, Trimmomatic] -> quantification [FastQC, Trimmomatic] -> dimensionality reduction/clustering [GSEA] -> stage not stated [R v4.1.0]

### Hfq-licensed RNA-RNA interactome in <i>Pseudomonas aeruginosa</i> reveals a keystone sRNA. (PNAS 2023)

- DOI: 10.1073/pnas.2218407120 | PMCID: PMC10214189 | PMID: 37285605
- Evidence: Reads were assessed for quality control and adaptor trimming with bcl2fastq and mapped with bowtie2 (version 2.4.5); read quantification was performed with htseq ( 59 ) and differential gene expression analysis was conducted with DESeq2 ( 60 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, DESeq2] -> read trimming [Bowtie2 v2.4.5, DESeq2] -> alignment/mapping [Bowtie2 v2.4.5, DESeq2] -> quantification [Bowtie2 v2.4.5, DESeq2] -> differential/statistical testing [Bowtie2 v2.4.5, DESeq2] -> stage not stated [R]

### IRIS: Discovery of cancer immunotherapy targets arising from pre-mRNA alternative splicing. (PNAS 2023)

- DOI: 10.1073/pnas.2221116120 | PMCID: PMC10214192 | PMID: 37192158
- Version used: **1.26.0**
- Evidence: Splicing factor ( 36 ) gene expression levels were quantified by FeatureCounts v2.0.1 ( 60 ), followed by DESeq2 v1.26.0 ( 61 ) normalization.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [Cufflinks v2.2.1, DESeq2 v1.26.0, featureCounts v2.0.1] -> normalisation [DESeq2 v1.26.0, featureCounts v2.0.1]

### Chitin utilization by marine picocyanobacteria and the evolution of a planktonic lifestyle. (PNAS 2023)

- DOI: 10.1073/pnas.2213271120 | PMCID: PMC10194020 | PMID: 37159478
- Evidence: MIT9303 and MIT9313 reads were analyzed separately using the DESeq2 R package v1.24.0 ( 71 ) to determine differentially expressed genes.
- Full pipeline: alignment/mapping [HTSeq, MAFFT] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2] -> stage not stated [BLAST]

### Nonpathological inflammation drives the development of an avian flight adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2219757120 | PMCID: PMC10175837 | PMID: 37126698
- Evidence: The bioinformatic analysis was performed on a Linux platform utilizing a custom bioinformatics pipeline that included STAR (version 2.70f) alignment of reads, the SUBREAD featureCounts program (version 2.0.0) to produce count tables, and DESeq2 R software package (1.26.0; R version 2.6.3) for differential expression analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [DESeq2, R v2.70f, STAR v2.70f, featureCounts] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, R v2.70f, STAR v2.70f, featureCounts]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Version used: **1.28.1**
- Evidence: All downstream RNA-seq analyses were performed using count data for the 5,147 core genes, with VST-normalization performed on all samples together in DESeq2 v1.28.1 with blind = TRUE in R ( 55 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Intestinal activating transcription factor 4 regulates stress-related behavioral alterations via paraventricular thalamus in male mice. (PNAS 2023)

- DOI: 10.1073/pnas.2215590120 | PMCID: PMC10175747 | PMID: 37126693
- Evidence: Differential expression analysis of the genes from two groups was performed by using the DESeq2 R package.
- Full pipeline: differential/statistical testing [DESeq2, R]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: GSEA was performed on VST-transformed data using the DESeq2 package ( 64 ).
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### Tumor progression is independent of tumor-associated macrophages in cell lineage-based mouse models of glioblastoma. (PNAS 2023)

- DOI: 10.1073/pnas.2222084120 | PMCID: PMC10120014 | PMID: 37040416
- Evidence: DESeq2 ( 42 ) was used for differential gene expression analysis for all bulk RNAseq studies.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, fgsea]

### Derepression of Y-linked multicopy protamine-like genes interferes with sperm nuclear compaction in <i>D. melanogaster</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220576120 | PMCID: PMC10120018 | PMID: 37036962
- Version used: **1.26.0**
- Evidence: ...ureCounts ( 49 ); v 2.0.1, with “-M –fraction -p -s 2.” After summing gene counts for technical replicates, differential expression was assayed using DESeq2 v1.26.0 ( 50 ), with lfcShrink(type=”ashr”)).
- Full pipeline: alignment/mapping [BEDTools, STAR v2.7.1a] -> quantification [BEDTools] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts] -> stage not stated [ImageJ]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: Cross-sample normalization was done by using DESeq2 based on the RNA sequencing of samples from 12 tissues, including the body wall, muscle, oral tentacles, intestine, rete mirabile, transverse vessel, polian vesicle, respiratory tree, Cuvierian organ, coelomocytes, ovary, and testis.
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### Interrogating bromodomain inhibitor resistance in KMT2A-rearranged leukemia through combinatorial CRISPR screens. (PNAS 2023)

- DOI: 10.1073/pnas.2220134120 | PMCID: PMC10120025 | PMID: 37036970
- Evidence: Normalized counts for each sgRNA were extracted and used to identify differentially enriched sgRNA by DESeq2 ( 51 ).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [RSEM] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GATK v4.1.2.0, GSEA]

### Mutant β<sub>1</sub>-adrenergic receptor improves REM sleep and ameliorates tau accumulation in a mouse model of tauopathy. (PNAS 2023)

- DOI: 10.1073/pnas.2221686120 | PMCID: PMC10104526 | PMID: 37014857
- Evidence: Differential gene expression levels between mutant and WT tissues were analyzed using the DESeq2 R package (version 1.20.0).
- Full pipeline: quantification [featureCounts v1.5.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Evidence: Differentially expressed genes were determined using DESeq2 ( 64 ) separately for WT vs Crebbp HET , WT vs Kmt2d HET , and WT vs dHET, with the following filters: FDR < 0.05 (after Benjamini–Hochberg correction) and absolute fold change (FC) ≥ 1.2.
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### Nasal administration of anti-CD3 mAb (Foralumab) downregulates <i>NKG7</i> and increases <i>TGFB1</i> and <i>GIMAP7</i> expression in T cells in subjects with COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2220272120 | PMCID: PMC10243127 | PMID: 36881624
- Version used: **1.30.1**
- Evidence: Differential expression analysis was conducted using R (v4.0.3) and DESeq2 (v1.30.1).
- Full pipeline: read trimming [Seurat v4.1.1] -> alignment/mapping [STAR] -> quantification [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [Seurat v4.1.1] -> stage not stated [ggplot2 v3.3.6]

### Neuron-specific transcriptomic signatures indicate neuroinflammation and altered neuronal activity in ASD temporal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2206758120 | PMCID: PMC10013873 | PMID: 36862688
- Version used: **1.22.2**
- Evidence: DGE analyses were performed using DESeq2 (1.22.2)( 79 ) with default parameters.
- Full pipeline: quantification [featureCounts v1.6.4] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [DESeq2 v1.22.2, GSEA, WGCNA]

### Multifaceted role for p53 in pancreatic cancer suppression. (PNAS 2023)

- DOI: 10.1073/pnas.2211937120 | PMCID: PMC10013849 | PMID: 36848578
- Evidence: To assess differential accessibility, DESeq2 was applied ( 60 ) using a model to account for mouse model, cell type, and batch.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2]

### Cross-species predictive modeling reveals conserved drought responses between maize and sorghum. (PNAS 2023)

- DOI: 10.1073/pnas.2216894120 | PMCID: PMC10013860 | PMID: 36848555
- Version used: **1.36.0**
- Evidence: We used DESeq2 (v1.36.0) to calculate pairwise differential expression between drought and well-watered conditions for each genotype ( 48 ).
- Full pipeline: quality control [fastp v0.23.2] -> read trimming [fastp v0.23.2] -> variant calling [DESeq2 v1.36.0] -> normalisation [scikit-learn] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [scikit-learn] -> stage not stated [R]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Version used: **3.5.12**
- Evidence: Differential gene expression was determined by DESeq2 v3.5.12 ( 71 ) using normalized read counts and correcting for covariates detected by RUVseq v1.16.1 ( 72 ).
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Human pancreatic islet microRNAs implicated in diabetes and related traits by large-scale genetic analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2206797120 | PMCID: PMC9963967 | PMID: 36757889
- Version used: **1.32.0**
- Evidence: Finally, we used DESeq2 v1.32.0 to identify miRNAs differentially expressed across T2D status, PGSs of T2D and glycemic traits, and other common phenotypes (i.e., sex, age, and BMI).
- Full pipeline: differential/statistical testing [DESeq2 v1.32.0]

### Transcriptomic congruence analysis for evaluating model organisms. (PNAS 2023)

- DOI: 10.1073/pnas.2202584120 | PMCID: PMC9963430 | PMID: 36730203
- Evidence: ...yesP can be single-study DE results from any conventional pipeline (e.g., “LIMMA” for microarray or log2-transformed and normalized RNA-seq data and “DESeq2” for RNA-seq counts). “LIMMA” was used for both case studies 1 and 2 since only normalized expression values are available for these public data.
- Full pipeline: normalisation [DESeq2] -> stage not stated [R, igraph]

### Inducible disruption of <i>Tet</i> genes results in myeloid malignancy, readthrough transcription, and a heterochromatin-to-euchromatin switch. (PNAS 2023)

- DOI: 10.1073/pnas.2214824120 | PMCID: PMC9963276 | PMID: 37406303
- Evidence: P -values were calculated using the Wald test (as implemented in DESeq2), and adjusted using the Benjamini–Hochberg method.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2]

### Generation and analysis of context-specific genome-scale metabolic models derived from single-cell RNA-Seq data. (PNAS 2023)

- DOI: 10.1073/pnas.2217868120 | PMCID: PMC9963017 | PMID: 36719923
- Evidence: In such an approach, the variation across samples is not accounted for, and pooling cells per sample to pseudo-bulk samples followed by applying methods such as DESeq2 ( 23 ), which was originally designed for bulk data, remedies the problem.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2, R v4.1.1]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Evidence: To identify genes that were significantly differentially expressed between treatments across time, we used three methods [DESeq2 ( 114 ), Limma-Voom ( 115 ) and ImpulseDE2 ( 116 ); SI Appendix ].
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### PCIF1-mediated deposition of 5'-cap &lt;i&gt;N&lt;/i&gt;&lt;sup&gt;6&lt;/sup&gt;,2'-&lt;i&gt;O&lt;/i&gt;-dimethyladenosine in ACE2 and TMPRSS2 mRNA regulates susceptibility to SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210361120 | PMCID: PMC9945940 | PMID: 36689652
- Evidence: Transcripts were quantified using HTSeq (0.11.2), and DEGs were determined using DESeq2.
- Full pipeline: read trimming [Cutadapt v1.18, HISAT2 v2.1.0] -> alignment/mapping [Cutadapt v1.18, HISAT2 v2.1.0] -> quantification [DESeq2, HTSeq v0.11.2] -> stage not stated [SAMtools]

### GRAS transcription factors regulate cell division planes in moss overriding the default rule. (PNAS 2023)

- DOI: 10.1073/pnas.2210632120 | PMCID: PMC9942845 | PMID: 36669117
- Evidence: Differentially expressed genes between wild type and ∆ppshr1∆ppshr2 were identified using DESeq2 with the Wald test ( 78 ) from three biological replicates.
- Full pipeline: read trimming [Cutadapt v2.8] -> differential/statistical testing [DESeq2]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Version used: **1.22.2**
- Evidence: Where necessary, raw data were reanalyzed by bowtie2 (2.3.5) ( 77 ) alignment to the most recent Cryptococcus neoformans H99 or KN99α genome ( fungibd.org ), count matrices generated with HTSeq (1.99.2) ( 78 ) and RNA-seq analysis with Bioconductor DESeq2 (1.22.2) ( 79 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: Enrichment analysis was conducted on preranked lists based on shrunken log2 fold changes from DESeq2 lfcShrink option.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: Normalization of read counts and differential expression analysis were performed using DESeq2 ( 61 ).
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Accelerated cell-type-specific regulatory evolution of the human brain. (PNAS 2024)

- DOI: 10.1073/pnas.2411918121 | PMCID: PMC11670112 | PMID: 39680759
- Evidence: For each pairwise comparison, we normalized the counts using DESeq2’s median of ratio method to account for differences between library size both at the species and cell type level.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [Seurat]

### E93 controls adult differentiation by repressing &lt;i&gt;broad&lt;/i&gt; in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2403162121 | PMCID: PMC11665871 | PMID: 39671182
- Evidence: In total 8,963 genes were analyzed for differential expression between groups of samples with DESeq2 ( 45 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [Bioconductor]

### Long-range &lt;i&gt;Atoh1&lt;/i&gt; enhancers maintain competency for hair cell regeneration in the inner ear. (PNAS 2024)

- DOI: 10.1073/pnas.2418098121 | PMCID: PMC11665905 | PMID: 39671177
- Evidence: Bioinformatic analysis used cellranger, Seurat ( 60 ), Signac ( 61 ), deepTools ( 62 ), DESeq2 ( 63 ), DiffBind ( 64 ), and Homer ( 55 ).
- Full pipeline: stage not stated [DESeq2, Seurat, Signac, deepTools]

### Cis-regulatory elements driving motor neuron-selective viral payload expression within the mammalian spinal cord. (PNAS 2024)

- DOI: 10.1073/pnas.2418024121 | PMCID: PMC11626145 | PMID: 39602276
- Evidence: ...; ChAT NEG only, significant enrichment of accessibility in the flowthrough population (ChAT POS /ChAT NEG fold-change ≤ 0.5, FDR-corrected q < 0.05, DESeq2); ChAT POS only, significant enrichment of accessibility in the spinal MN population (ChAT POS /ChAT NEG fold-change ≥ 2, FDR-corrected q < 0.05, DESeq2); Background (n = 2,000), randomly selected genomic loci included for visual comparison.
- Full pipeline: differential/statistical testing [DESeq2]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Version used: **1.40.2**
- Evidence: Normalization and differential expression analysis was performed using DESeq2 v1.40.2 ( 80 ) defaults using R ( 81 ), RStudio v2023.9.0.463, and tidyverse v2.0.0 ( 82 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: A principal component analysis was then applied to normalized read counts from “DESeq2 vst” ( 66 ) method to investigate major axes of variation in the expression data.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### The glucocorticoid receptor potentiates aldosterone-induced transcription by the mineralocorticoid receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2413737121 | PMCID: PMC11588051 | PMID: 39541347
- Evidence: Briefly, we obtained raw count data using analyzeRepeats.pl, and then the raw counts were normalized by default size factors from DESeq2 routine 23 provided via getDiffExpression.pl.
- Full pipeline: quality control [Cutadapt v1.18] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2, STAR v2.70] -> normalisation [DESeq2] -> stage not stated [HOMER, SAMtools]

### &lt;i&gt;Samd7&lt;/i&gt; represses short-wavelength cone genes to preserve long-wavelength cone and rod photoreceptor identity. (PNAS 2024)

- DOI: 10.1073/pnas.2402121121 | PMCID: PMC11588049 | PMID: 39531499
- Evidence: ( C ) Bar plots of opsin expression (DESeq2-normalized counts) from RNA-seq data in panels A and B (mean ± SD; n = 3 per group) *p-adj < 0.05. ns, not significant.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP]

### Subchronic elevation in ambient temperature drives alterations to the sperm epigenome and accelerates early embryonic development in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2409790121 | PMCID: PMC11588121 | PMID: 39527742
- Evidence: The effect of heat stress was assessed by ( B ) an unpaired t test or ( C ) DESeq2, represented by volcano plots of tRF, piRNA, and miRNA expression values with a significance threshold of fold change ± 1.5 and P -value ≤ 0.05.
- Full pipeline: stage not stated [DESeq2]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Version used: **1.40.2**
- Evidence: Differential expression of genes and TEs was then analyzed using DESeq2 (version 1.40.2).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: Count values from dataset GSE131016 were obtained from the NCBI Gene Expression Omnibus data repository and reanalyzed using DESeq2 ( 67 ) in R version 4.3.1 ( 66 ).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### Extensive import of nucleus-encoded tRNAs into chloroplasts of the photosynthetic lycophyte, &lt;i&gt;Selaginella kraussiana&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2412221121 | PMCID: PMC11573648 | PMID: 39503889
- Evidence: The tRNAs from plastid and nucleus fractions were sequenced and analyzed with mim-tRNAseq, and log 2 Fold Change (Plastid/Total) was obtained with DESeq2.
- Full pipeline: stage not stated [DESeq2]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **1.38.0**
- Evidence: Differential expression analysis was performed with DESeq2 version 1.38.0 ( 62 ) on R version 4.2.2.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### A comprehensive transcriptome characterization of individual nuclear receptor pathways in the human small intestine. (PNAS 2024)

- DOI: 10.1073/pnas.2411189121 | PMCID: PMC11551338 | PMID: 39475639
- Evidence: Differential gene expression was performed with DESeq 2 (package version 3.13) in R, for each nuclear receptor condition compared to the control differentiated organoids ( 73 ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [pheatmap]

### Soil viral-host interactions regulate microplastic-dependent carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2413245121 | PMCID: PMC11551317 | PMID: 39467127
- Evidence: Metatranscriptomics analysis using DESeq2 further revealed that more functional genes were high expressed in nondegradable MP treatments than in the control ( SI Appendix , Table S2 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BLAST, Bowtie2, HMMER] -> quantification [Bowtie2] -> stage not stated [DESeq2, R v4.0.3, vegan]

### Perturbation-specific transcriptional mapping for unbiased target elucidation of antibiotics. (PNAS 2024)

- DOI: 10.1073/pnas.2409747121 | PMCID: PMC11551328 | PMID: 39467118
- Evidence: To then assess overall strength of the transcriptional signals, differential gene expression was orthogonally assessed using DESeq2 ( 22 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: Differential gene expression analysis was performed using DESeq2 ( 90 ) in R version 4.1.3 ( 91 ).
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### AMBRA1 controls the translation of immune-specific genes in T lymphocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2416722121 | PMCID: PMC11536168 | PMID: 39436665
- Evidence: Differential expression analysis was performed with DESeq2 within R.
- Full pipeline: quantification [HTSeq] -> normalisation [pheatmap] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, SAMtools, deepTools]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Evidence: Read count data were analyzed using iDEP.96 ( http://bioinformatics.sdstate.edu/idep96/ ) ( 74 , 75 ); hierarchical clustering and principal component analysis were performed, followed by selection of differentially expressed genes (false discovery rate < 0.1) by DESeq2 ( 76 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Version used: **1.36.0**
- Evidence: 6 hrpf) were conducted with DESeq2 1.36.0 ( 78 ) in R.
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Abortive infection of bat fibroblasts with SARS-CoV-2. (PNAS 2024)

- DOI: 10.1073/pnas.2406773121 | PMCID: PMC11513954 | PMID: 39401365
- Evidence: Differential expression analysis was performed using DESeq2 ( 40 ), and we found gene sets enriched in genes changing upon infection using the GSEA tool ( 41 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, GSEA]

### YTHDC2 serves a distinct late role in spermatocytes during germ cell differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2309548121 | PMCID: PMC11494341 | PMID: 39378093
- Evidence: Differential gene expression was calculated using DESeq2 (RRID:SCR_015687) ( 22 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Evidence: Comparing acetylation levels across neuroendocrine tumors revealed 3,866 peaks that are significantly more acetylated (DESeq2, fold-change > 2, FDR < 10%, see Materials and Methods ) in LNETs and 3,231 that are more acetylated in ileal and pancreatic neuroendocrine tumors.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### The &lt;i&gt;ivory&lt;/i&gt; lncRNA regulates seasonal color patterns in buckeye butterflies. (PNAS 2024)

- DOI: 10.1073/pnas.2403426121 | PMCID: PMC11474026 | PMID: 39352931
- Evidence: Differential gene expression analysis was performed using default settings for DESeq2 on the Galaxy Server webtools ( 38 ).
- Full pipeline: alignment/mapping [HISAT2, MACS2] -> differential/statistical testing [DESeq2] -> stage not stated [AUGUSTUS, BUSCO v5.4.7]

### Modulation of diabetes-related retinal pathophysiology by PTX3. (PNAS 2024)

- DOI: 10.1073/pnas.2320034121 | PMCID: PMC11474045 | PMID: 39348530
- Evidence: For the RNAseq dataset GSE160306 ( 19 ), raw table of counts were retrieved from GEO and reanalyzed in R using DESeq2 standard workflow.
- Full pipeline: normalisation [ImageJ] -> stage not stated [DESeq2, Seurat]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: The differential expression analysis was performed with DESeq2 R Bioconductor package (1.39.2) ( 87 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### A sensitive assay for measuring whole-blood responses to type I IFNs. (PNAS 2024)

- DOI: 10.1073/pnas.2402983121 | PMCID: PMC11459193 | PMID: 39312669
- Evidence: Pseudobulk differential expression analysis was performed with DESeq2 ( 103 ).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, fgsea]

### Spaceflight-induced contractile and mitochondrial dysfunction in an automated heart-on-a-chip platform. (PNAS 2024)

- DOI: 10.1073/pnas.2404644121 | PMCID: PMC11459163 | PMID: 39312653
- Evidence: The reads were aligned to the prebuilt Ensembl Transcriptome v96 using Kallisto ( 86 ) and differential expression between the EHTs from space flight and ground control groups was analyzed using DESeq2 ( 87 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [ImageJ]

### In vivo CRISPR screens identify &lt;i&gt;Mga&lt;/i&gt; as an immunotherapy target in triple-negative breast cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2406325121 | PMCID: PMC11441491 | PMID: 39298484
- Evidence: DESeq2 ( 52 ) (v3.18) was used to identify significantly differentially expressed genes with a cutoff (adjusted P -value < 0.05 and fold change > 1.5).
- Full pipeline: alignment/mapping [HISAT2] -> variant calling [CellChat] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [HTSeq v0.6.1p, Scanpy]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **1.36.0**
- Evidence: Differentially expressed genes were identified using DESeq2 (v1.36.0) ( 67 ) with thresholds of |log2FC| > 1 and padj < 0.1.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Transdifferentiation occurs without resetting development-specific DNA methylation, a key determinant of full-function cell identity. (PNAS 2024)

- DOI: 10.1073/pnas.2411352121 | PMCID: PMC11441492 | PMID: 39292740
- Evidence: Differential gene expression analysis was performed using DESeq2 R package (V 1.26.0).
- Full pipeline: read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, SAMtools, Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, R]

### FicD sensitizes cellular response to glucose fluctuations in mouse embryonic fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2400781121 | PMCID: PMC11420183 | PMID: 39259589
- Evidence: To ensure this loss of response was not an artifact of our RNA seq analysis with EdgeR, we compared the EdgeR-defined DEGs to those defined by additional methods (DESeq2, NOISeq, and limma).
- Full pipeline: stage not stated [DESeq2, edgeR, limma]

### Plasma cell-free RNA signatures of inflammatory syndromes in children. (PNAS 2024)

- DOI: 10.1073/pnas.2403897121 | PMCID: PMC11406294 | PMID: 39240972
- Evidence: Gene transcript abundances were compared using a negative binomial model implemented using the DESeq2 R package ( 45 ).
- Full pipeline: quality control [SAMtools v1.14] -> alignment/mapping [SAMtools v1.14] -> quantification [DESeq2, R] -> machine learning [Snakemake] -> stage not stated [featureCounts]

### Conserved moonlighting protein pyruvate dehydrogenase induces robust protection against &lt;i&gt;Staphylococcus aureus&lt;/i&gt; infection. (PNAS 2024)

- DOI: 10.1073/pnas.2321939121 | PMCID: PMC11388329 | PMID: 39186649
- Version used: **1.30.1**
- Evidence: Gene differential expressions analysis was conducted by DESeq2 (v1.30.1) between different conditions ( 52 ).
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [Clustal Omega] -> differential/statistical testing [DESeq2 v1.30.1]

### Parallel ecological and evolutionary responses to selection in a natural bacterial community. (PNAS 2024)

- DOI: 10.1073/pnas.2403577121 | PMCID: PMC11388356 | PMID: 39190353
- Evidence: To determine which of the compost isolates differed in abundance across treatments, we fitted a negative binomial GLM to the data using the “ DESeq ” function in the R package “ DESeq2 ” ( 92 ).
- Full pipeline: quantification [DESeq2, R] -> stage not stated [emmeans, ggplot2, lme4, vegan]

### Platelet-activating factor (PAF) promotes immunosuppressive neutrophil differentiation within tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2406748121 | PMCID: PMC11363292 | PMID: 39178229
- Evidence: DESeq2-1.26.0 was used to normalize count matrix and assess differential expression with adjusted P value < 0.05.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> normalisation [DESeq2, pheatmap v1.0.12] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Conserved 5-methyluridine tRNA modification modulates ribosome translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2401743121 | PMCID: PMC11363252 | PMID: 39159370
- Evidence: Differential expression analysis was performed using DESeq2 ( 61 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.3] -> alignment/mapping [RSEM v1.3.3, STAR v2.7.8a] -> differential/statistical testing [DESeq2]

### Mice lacking &lt;i&gt;Astn2&lt;/i&gt; have ASD-like behaviors and altered cerebellar circuit properties. (PNAS 2024)

- DOI: 10.1073/pnas.2405901121 | PMCID: PMC11348334 | PMID: 39150780
- Evidence: ( F ) Volcano plot depicting differentially expressed genes ( P -adj < 0.05, indicated with red) in P22 Astn2 KO cerebellum, compared with WT littermates, identified using DESeq2.
- Full pipeline: quantification [ImageJ v1.53c] -> differential/statistical testing [DESeq2] -> stage not stated [Python]

### The importance of the location of the N-terminus in successful protein folding in vivo and in vitro. (PNAS 2024)

- DOI: 10.1073/pnas.2321999121 | PMCID: PMC11348275 | PMID: 39145938
- Evidence: The DESeq2 RNA-sequencing analysis package was then used to determine enrichment scores for each CP, to measure error between replicates, and to assign P -values to each score ( 39 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [DESeq2, Python]

### A PIKfyve modulator combined with an integrated stress response inhibitor to treat lysosomal storage diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2320257121 | PMCID: PMC11348278 | PMID: 39150784
- Evidence: Differential expression analysis was assessed using DESeq2 in R, which calculated statistical significance of compound-treated cells compared to DMSO-treated cells, using a standard negative binomial fit of the reads per kilobase per million data to generate fold-change quantifications.
- Full pipeline: quantification [DESeq2, Fiji, ImageJ] -> differential/statistical testing [DESeq2]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: DESeq2 was used to conduct differential gene expression analysis and generate plots.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Alloreactive memory CD4 T cells promote transplant rejection by engaging DCs to induce innate inflammation and CD8 T cell priming. (PNAS 2024)

- DOI: 10.1073/pnas.2401658121 | PMCID: PMC11348247 | PMID: 39136987
- Evidence: Differential gene expression between DCs cultured with allogeneic/syngeneic T EM and unstimulated DCs was evaluated using the DESeq2 R package ( https://doi.org/10.1186/s13059-014-0550-8 ), incorporating the batch information into the model to account for technical variation.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Trim Galore] -> normalisation [limma] -> dimensionality reduction/clustering [ggplot2, limma] -> differential/statistical testing [DESeq2, R] -> visualisation [limma] -> stage not stated [fgsea]

### m&lt;sup&gt;6&lt;/sup&gt;A modification plays an integral role in mRNA stability and translation during pattern-triggered immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2411100121 | PMCID: PMC11331096 | PMID: 39116132
- Evidence: The raw counts for each gene were calculated by HTSeq and normalized by DESeq2 for further analyses ( 54 ).
- Full pipeline: read trimming [STAR, Trim Galore] -> alignment/mapping [Bowtie2, STAR, Trim Galore] -> variant calling [Bioconductor] -> normalisation [Bioconductor, DESeq2, HTSeq]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: Each bar represents the mean ± SEM of three replicates (same clonal cell line analyzed three independent times) and the DE analysis was performed using DESeq2 with default parameters (Wald test, corrected for multiple testing using the Benjamini and Hochberg method), except for normalization to TAF1 exons 1 to 28.
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### UPF1 deficiency enhances mitochondrial ROS which promotes an immunosuppressive microenvironment in pancreatic ductal adenocarcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2401996121 | PMCID: PMC11331118 | PMID: 40591563
- Evidence: Count matrices were then analyzed via the “rna-star-groups-dge” module, which employs DESeq2 to determine differential gene expression, perform gene set enrichment analyses, and generate PCA, volcano, and heatmap plots. scRNA-seq Analysis.
- Full pipeline: read trimming [Picard, STAR, Trimmomatic, featureCounts] -> alignment/mapping [Picard, STAR, Trimmomatic, featureCounts] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2]

### Nutrient and moisture limitations reveal keystone metabolites linking rhizosphere metabolomes and microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2303439121 | PMCID: PMC11317588 | PMID: 39093948
- Evidence: Differentially abundant ASVs between each of the individual treatments and the control samples were determined with the DESeq2 package ( 43 ), and differentially abundant ASVs whose responses to a treatment were driven by only one sample were removed from subsequent analyses.
- Full pipeline: quantification [ImageJ v2.0.0] -> dimensionality reduction/clustering [vegan] -> differential/statistical testing [DESeq2, R v3.6.0, phyloseq, vegan] -> visualisation [Cytoscape, R v3.6.0, igraph, phyloseq] -> stage not stated [DADA2]

### Unraveling clonal CD8 T cell expansion and identification of essential factors in γ-herpesvirus-induced lymphomagenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2404536121 | PMCID: PMC11317613 | PMID: 39088396
- Evidence: DESeq2 was used with a P -adjusted cutoff of 0.05 to identify a total of 8,276 differentially opened regions (DOR).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [Seurat, UMAP] -> stage not stated [GSEA]

### Convergent evolution in toxin detection and resistance provides evidence for conserved bacterial-fungal interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2304382121 | PMCID: PMC11317636 | PMID: 39088389
- Evidence: DESeq2 was employed to analyze differentially expressed genes ( 64 ).
- Full pipeline: read trimming [Bowtie2 v2.4.2] -> alignment/mapping [Bowtie2 v2.4.2, Clustal Omega] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, PyMOL, featureCounts]

### Matrix stiffness-dependent regulation of immunomodulatory genes in human MSCs is associated with the lncRNA CYTOR. (PNAS 2024)

- DOI: 10.1073/pnas.2404146121 | PMCID: PMC11317610 | PMID: 39074278
- Evidence: Subsequently, we analyzed differentially expressed genes (DEGs) with DESeq2’s Likelihood ratio test ( 51 ) ( Dataset S1 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat]

### Identification and characterization of a small-molecule metallophore involved in lanthanide metabolism. (PNAS 2024)

- DOI: 10.1073/pnas.2322096121 | PMCID: PMC11317620 | PMID: 39078674
- Evidence: Using KBase ( 50 ), reads were aligned with HISTAT2, transcripts were assembled with StringTie, and DEGs were identified using DESeq2.
- Full pipeline: alignment/mapping [DESeq2, StringTie] -> dimensionality reduction/clustering [BLAST, HMMER]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: Gene expression analysis was performed using HTSeq ( 41 ) and DESeq2 ( 42 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Mitochondrial antioxidants abate SARS-COV-2 pathology in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2321972121 | PMCID: PMC11287122 | PMID: 39008677
- Evidence: Raw read counts were normalized in R (version 4.2.2) using the “DESeq2” (version 1.38.3) package.
- Full pipeline: quantification [DESeq2, R v4.2.2] -> normalisation [DESeq2, R v4.2.2] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ComplexHeatmap, GSEA v4.3.2, ggplot2]

### Life stage-specific poly(A) site selection regulated by <i>Trypanosoma brucei</i> DRBD18. (PNAS 2024)

- DOI: 10.1073/pnas.2403188121 | PMCID: PMC11260167 | PMID: 38990950
- Evidence: Both paired-end and single-end data were then supplied to the R package DESeq2, with a design controlling for experiment of origin (~ is_paired + treatment). scRNAseq.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, R, Seurat]

### IFIH1 (MDA5) is required for innate immune detection of intron-containing RNA expressed from the HIV-1 provirus. (PNAS 2024)

- DOI: 10.1073/pnas.2404349121 | PMCID: PMC11260138 | PMID: 38985764
- Version used: **1.30.1**
- Evidence: DESeq2 (v1.30.1) was used for differential gene expression analysis.
- Full pipeline: alignment/mapping [RSEM v1.3.1] -> quantification [RSEM v1.3.1] -> dimensionality reduction/clustering [limma v3.46.0] -> differential/statistical testing [DESeq2 v1.30.1]

### TFEB safeguards trophoblast syncytialization in humans and mice. (PNAS 2024)

- DOI: 10.1073/pnas.2404062121 | PMCID: PMC11253012 | PMID: 38968109
- Evidence: ( D ) Dot plots illustrate the average expression and percentage of nuclei in each cluster in which DEGs were identified using DESeq2 with criteria as absolute log 2 FC < −2, P adj. < 0.05 in E9.5.
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Version used: **1.42.0**
- Evidence: Differential expression analysis was conducted using the R Bioconductor package, DESeq2 1.42.0 ( 86 ) yielding the log2 fold change, P -values, and median-ratio normalized counts.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: The analysis was conducted following the Bioconductor RNA-seq workflow and differential gene expression was analyzed using the R package DESeq2 .
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Evidence: These counts were then subjected to variance stabilizing transformation using the vst function from the DESeq2 package ( 49 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Evidence: Reads aligning to annotated mouse transcripts were counted using SummarizeOverlaps in the GenomicAlignments Bioconductor package ( 49 ), and differential expression analysis was performed using the DESeq2 package ( 50 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### Transfection of entomopathogenic <i>Metarhizium</i> species with a mycovirus confers hypervirulence against two lepidopteran pests. (PNAS 2024)

- DOI: 10.1073/pnas.2320572121 | PMCID: PMC11214047 | PMID: 38885380
- Evidence: Genes with an adjusted P -value ≤0.05 and fold-change ≥1.2 found by DESeq2 were assigned as DEGs.
- Full pipeline: read trimming [fastp] -> alignment/mapping [ggplot2] -> quantification [ggplot2] -> dimensionality reduction/clustering [clusterProfiler, ggplot2] -> stage not stated [BLAST, DESeq2, R, pheatmap]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Evidence: DESeq2 ( 93 ) was used for differential expression analyses between sexes, between crosses within each sex, as well as between age groups within each cross and each sex.
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### Innate acting memory Th1 cells modulate heterologous diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2312837121 | PMCID: PMC11181110 | PMID: 38838013
- Evidence: DESeq2 ( 63 ) (version 1.28.1) was used for normalization of counts and PCA.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R v4.0.2, featureCounts, ggplot2, pheatmap v1.0.12]

### TMPRSS2-mediated SARS-CoV-2 uptake boosts innate immune activation, enhances cytopathology, and drives convergent virus evolution. (PNAS 2024)

- DOI: 10.1073/pnas.2407437121 | PMCID: PMC11161796 | PMID: 38814864
- Evidence: We used the DESeq2 R package ( 42 ) for differentially expressed gene (DEG) analysis according to the following workflow.
- Full pipeline: read trimming [fastp] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R]

### SUMO-specific protease 1 regulates germinal center B cell response through deSUMOylation of PAX5. (PNAS 2024)

- DOI: 10.1073/pnas.2314619121 | PMCID: PMC11145296 | PMID: 38776375
- Evidence: Differentially expressed genes were calculated using DESeq2.
- Full pipeline: alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### CRISPRi screens identify the lncRNA, <i>LOUP</i>, as a multifunctional locus regulating macrophage differentiation and inflammatory signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2322524121 | PMCID: PMC11145268 | PMID: 38781216
- Evidence: SgRNAs were counted and passed to DESeq2 for analysis.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, deepTools] -> stage not stated [AlphaFold, DESeq2]

### Astrocyte-to-microglia communication via Sema4B-Plexin-B2 modulates injury-induced reactivity of microglia. (PNAS 2024)

- DOI: 10.1073/pnas.2400648121 | PMCID: PMC11145257 | PMID: 38781210
- Evidence: Differentially expressed genes were identified using DESeq2 ( 37 ) with the betaPrior, cooksCutoff and independent filtering parameters set to False.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### Interferon signaling in the nasal epithelium distinguishes among lethal and common cold coronaviruses and mediates viral clearance. (PNAS 2024)

- DOI: 10.1073/pnas.2402540121 | PMCID: PMC11127059 | PMID: 38758698
- Evidence: Genes with significant up- or downregulation were assessed using DESeq2 followed by Gene Set Enrichment Analysis (GSEA) ( 45 , 46 ).
- Full pipeline: stage not stated [DESeq2, GSEA]

### Macrophage transplantation rescues RNASET2-deficient leukodystrophy by replacing deficient microglia in a zebrafish model. (PNAS 2024)

- DOI: 10.1073/pnas.2321496121 | PMCID: PMC11126979 | PMID: 38753517
- Evidence: Differential expression analysis was performed using DESeq2 ( 41 ) using three-way comparisons between WT sham, rnaset2 sham, and rnaset2 transplanted samples (with separate analyses for microglia-depleted and nondepleted groups).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [R v4.3, fgsea v1.28.0, ggplot2 v3.4.4] -> stage not stated [HTSeq v2.0]

### Clocking out and letting go to unleash green biotech applications in a photosynthetic host. (PNAS 2024)

- DOI: 10.1073/pnas.2318690121 | PMCID: PMC11127020 | PMID: 38739791
- Version used: **1.36.0**
- Evidence: Finally, we generated a read counts matrix using the prepDE.py script provided with stringtie, and this matrix was used for all subsequent statistical analyses Raw read counts were analyzed with DESeq2 v.1.36.0 ( 40 ).
- Full pipeline: alignment/mapping [SAMtools v1.11.0] -> quantification [DESeq2 v1.36.0] -> normalisation [R] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HISAT2 v2.2.1, ggplot2, pheatmap v1.0.12]

### Real-time emulation of future global warming reveals realistic impacts on the phenological response and quality deterioration in rice. (PNAS 2024)

- DOI: 10.1073/pnas.2316497121 | PMCID: PMC11126993 | PMID: 38739807
- Evidence: The Wald test was performed based on raw count data using the “DESeq” function in the R package “DESeq2” (ver.
- Full pipeline: quantification [ComplexHeatmap] -> visualisation [R, ggplot2] -> stage not stated [DESeq2]

### Cancer-stromal cell interactions in breast cancer brain metastases induce glycocalyx-mediated resistance to HER2-targeting therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322688121 | PMCID: PMC11098130 | PMID: 38709925
- Version used: **1.18.1**
- Evidence: Differential gene expression analyses were performed on absolute gene counts for RNA-Seq data and raw read counts for transcriptomic profiling data using DESeq2 v1.18.1 ( 48 ).
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v1.18.1] -> normalisation [edgeR] -> differential/statistical testing [DESeq2 v1.18.1, MACS2 v2.1.1.20160309] -> stage not stated [GSEA, GSVA]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Version used: **1.24.0**
- Evidence: Genes with 1 TPM or more in all three replicates of a sample were considered expressed and included in the analysis of differential expression with DESeq2 v1.24.0 ( 49 ), Only differentially expressed genes (DEGs) whose adjusted P -values ( P -adjust) were under 0.01 were used for metaanalyses.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### TRAF3 loss-of-function reveals the noncanonical NF-κB pathway as a therapeutic target in diffuse large B cell lymphoma. (PNAS 2024)

- DOI: 10.1073/pnas.2320421121 | PMCID: PMC11067025 | PMID: 38662551
- Version used: **1.26.0**
- Evidence: Data processing and DGEA (DESeq2 v1.26.0) for primary lymphoma and cell line samples were performed as previously described ( 14 ).
- Full pipeline: stage not stated [DESeq2 v1.26.0, GSEA v4.1.0, limma]

### Decorin suppresses tumor lymphangiogenesis: A mechanism to curtail cancer progression. (PNAS 2024)

- DOI: 10.1073/pnas.2317760121 | PMCID: PMC11067011 | PMID: 38652741
- Evidence: We counted only exonic reads using a strand-specific library, and we used the gene hit counts table for differential expression analysis using DESeq2, with the Wald test to generate P values and Log 2 fold changes.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Version used: **1.32.0**
- Evidence: Read count data were analyzed with the R package DESeq2 (v.1.32.0) to estimate the fold changes in expression levels and to identify differentially expressed gene levels (DEGs) ( 28 ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Evidence: Differential gene expression analysis (DGEA) was performed using two R (version 4.2.2) packages: tximport ( 88 ) and DESeq2 ( 89 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### Integrated mutational landscape analysis of poorly differentiated high-grade neuroendocrine carcinoma of the uterine cervix. (PNAS 2024)

- DOI: 10.1073/pnas.2321898121 | PMCID: PMC11046577 | PMID: 38625939
- Evidence: Gene differential expression was analyzed using DESeq2 ( 49 ) while gene fusion events were identified using Arriba ( 50 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [CNVkit, GATK]

### APOBEC2 safeguards skeletal muscle cell fate through binding chromatin and regulating transcription of non-muscle genes during myoblast differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2312330121 | PMCID: PMC11047093 | PMID: 38625936
- Evidence: Gene expression changes were identified at a cutoff of padj < 0.05 in DESeq2 ( 68 ).
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [ImageJ, R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, MACS2]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Normalization and differential expression were done with the DESeq2 package (version 1.10.1).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Version used: **1.32.0**
- Evidence: We estimated read counts on genes/peaks with HTSeq-count v0.13.5 ( 88 ), and then compared adults to juveniles using DESeq2 v1.32.0 ( 89 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Version used: **1.32.0**
- Evidence: Differential gene expression analysis was performed using the DESeq2 1.32.0 ( 100 ) model included normalization terms obtained from RUVs analysis.
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: Featurecounts was used to count reads in each sample within each region in the reference file, and input into DESeq2 in R.
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### The MUC1-HIF-1α signaling axis regulates pancreatic cancer pathogenesis through polyamine metabolism remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2315509121 | PMCID: PMC10998584 | PMID: 38547055
- Evidence: TopHat2 was used for alignment and differential expression was done through DESeq2 R package.
- Full pipeline: alignment/mapping [DESeq2, R, TopHat] -> differential/statistical testing [DESeq2, R, TopHat] -> stage not stated [GSEA, ImageJ]

### Normalizing granuloma vasculature and matrix improves drug delivery and reduces bacterial burden in tuberculosis-infected rabbits. (PNAS 2024)

- DOI: 10.1073/pnas.2321336121 | PMCID: PMC10998582 | PMID: 38530888
- Version used: **1.42.0**
- Evidence: Raw count data were normalized using DESeq2 (v.1.42.0).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, featureCounts v1.5.0] -> normalisation [DESeq2 v1.42.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.10.0] -> stage not stated [ImageJ]

### IL7 increases targeted lipid nanoparticle-mediated mRNA expression in T cells in vitro and in vivo by enhancing T cell protein translation. (PNAS 2024)

- DOI: 10.1073/pnas.2319856121 | PMCID: PMC10990120 | PMID: 38513098
- Evidence: Data were aligned using Kalisto ( 47 ), and differential expression analysis was performed using DESeq2 ( 48 ) with counts prefiltered for low expression.
- Full pipeline: alignment/mapping [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Activation of polyamine catabolism promotes glutamine metabolism and creates a targetable vulnerability in lung cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2319429121 | PMCID: PMC10990097 | PMID: 38513095
- Evidence: Differentially expressed gene analysis was conducted using the R package “DESeq2” ( 61 ), applying a threshold of |log2FoldChange| > log2(1.5) and P -value < 0.05.
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.4.2a] -> quantification [RSEM v1.3.3] -> differential/statistical testing [DESeq2, R] -> stage not stated [Metascape]

### Isotype switching in human memory B cells sets intrinsic antigen-affinity thresholds that dictate antigen-driven fates. (PNAS 2024)

- DOI: 10.1073/pnas.2313672121 | PMCID: PMC10990115 | PMID: 38502693
- Evidence: Differential gene expression analysis was done using the DESeq2 package ( 62 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ComplexHeatmap, GSEA, R, fgsea]

### Morc1 reestablishes H3K9me3 heterochromatin on piRNA-targeted transposons in gonocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2317095121 | PMCID: PMC10990106 | PMID: 38502704
- Evidence: Read counts were normalized to RLE using DESeq2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Picard] -> quantification [DESeq2] -> normalisation [DESeq2] -> stage not stated [RepeatMasker]

### SRF transcriptionally regulates the oligodendrocyte cytoskeleton during CNS myelination. (PNAS 2024)

- DOI: 10.1073/pnas.2307250121 | PMCID: PMC10962977 | PMID: 38483990
- Evidence: Statistics by DESeq2.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Epidermal growth factor receptor (EGFR) is a target of the tumor-suppressor E3 ligase FBXW7. (PNAS 2024)

- DOI: 10.1073/pnas.2309902121 | PMCID: PMC10962967 | PMID: 38483988
- Evidence: The reads were mapped on the GRCh37 genome assembly, and the differential gene expression analysis was performed using the DESeq2 package.
- Full pipeline: alignment/mapping [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: A counts table was generated using htseq ( 48 ) and used to perform differential gene expression analysis using DESeq2 ( 49 ) in R.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Aging and comprehensive molecular profiling in acute myeloid leukemia. (PNAS 2024)

- DOI: 10.1073/pnas.2319366121 | PMCID: PMC10927507 | PMID: 38422020
- Evidence: The expression levels (DESeq2 VST normalization) of IL1RN , CYP1B1, and DGAT2 are highly correlated with the monocyte-like score, while that of the CALCRL is most highly correlated with the HSC-like score.
- Full pipeline: normalisation [DESeq2] -> stage not stated [R, survival (R) v0.4.9]

### NOVA1 acts as an oncogenic RNA-binding protein to regulate cholesterol homeostasis in human glioblastoma cells. (PNAS 2024)

- DOI: 10.1073/pnas.2314695121 | PMCID: PMC10927500 | PMID: 38416679
- Evidence: Reads were aligned to the hg19 build using STAR ( 42 ) and analyzed by differential analysis of raw sequencing counts using DESeq2 (Bioconductor, https://www.bioconductor.org/packages/release/bioc/html/DESeq2.html ) ( 43 ).
- Full pipeline: alignment/mapping [Bioconductor, DESeq2, STAR] -> differential/statistical testing [Bioconductor, DESeq2, STAR]

### Ultrafast sound production mechanism in one of the smallest vertebrates. (PNAS 2024)

- DOI: 10.1073/pnas.2314017121 | PMCID: PMC10927587 | PMID: 38408231
- Evidence: Afterward, the differential expression analysis of drumming and trunk muscle was performed in R using tximport and DESeq2 ( 42 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ImageJ, scikit-image]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Version used: **1.28.1**
- Evidence: Package Tximport v1.16.1 ( 54 ) was used to import count tables, and differential gene expression analysis was performed with DESeq2 v1.28.1 ( 44 ).
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Enhancing chimeric antigen receptor T cell therapy by modulating the p53 signaling network with Δ133p53α. (PNAS 2024)

- DOI: 10.1073/pnas.2317735121 | PMCID: PMC10927528 | PMID: 38408246
- Evidence: Differential gene expression between Δ133- and WT-CARs was evaluated using DESeq2, with p-values calculated using the Wald test.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Extracellular vesicle formation in <i>Euryarchaeota</i> is driven by a small GTPase. (PNAS 2024)

- DOI: 10.1073/pnas.2311321121 | PMCID: PMC10927574 | PMID: 38408251
- Evidence: For samples with 3 or more replicates, differential expression was calculated with DESeq2, thereby normalizing EV-associated RNA to intracellular RNA.
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R] -> stage not stated [AlphaFold, ImageJ]

### OCA-B/Pou2af1 is sufficient to promote CD4&lt;sup&gt;+&lt;/sup&gt; T cell memory and prospectively identifies memory precursors. (PNAS 2024)

- DOI: 10.1073/pnas.2309153121 | PMCID: PMC10907311 | PMID: 38386711
- Version used: **1.24.0**
- Evidence: Differentially expressed genes were identified using DESeq2 version 1.24.0 ( 45 ) with a 5% FDR cutoff.
- Full pipeline: quality control [STAR v2.7.3a] -> alignment/mapping [STAR v2.7.3a] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v4.0.0, UMAP, pheatmap]

### Enhanced weathering in the US Corn Belt delivers carbon removal with agronomic benefits. (PNAS 2024)

- DOI: 10.1073/pnas.2319436121 | PMCID: PMC10907306 | PMID: 38386712
- Evidence: Samples were submitted for differential expression analyses through DESeq2 ( 69 ) using prefiltering of 1 read per sample and two factors—the primary factor treatment (basalt/control) and secondary factor—block from which samples are derived ( Dataset S5 ).
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> differential/statistical testing [DESeq2]

### Coordination of rhythmic RNA synthesis and degradation orchestrates 24- and 12-h RNA expression patterns in mouse fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2314690121 | PMCID: PMC10873638 | PMID: 38315868
- Version used: **1.32.0**
- Evidence: INSPEcT first uses DESeq2 (v1.32.0) to calculate variances (which is zero in our case as our dataset only has one biological replica) and arranges samples in a matrix to be analyzed.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, STAR v2.7.7a] -> quantification [HOMER] -> visualisation [SAMtools v1.11] -> stage not stated [DESeq2 v1.32.0, R]

### Viral afterlife: SARS-CoV-2 as a reservoir of immunomimetic peptides that reassemble into proinflammatory supramolecular complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2300644120 | PMCID: PMC10861912 | PMID: 38306481
- Version used: **1.34.0**
- Evidence: Differential expression analysis and PCA analysis are performed with DESeq2 (version 1.34.0) ( 77 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.34.0, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.34.0, clusterProfiler v4.2.2] -> visualisation [ChimeraX]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Evidence: The DEGs of each group were identified using DESeq2 method with default parameters from Delegate, the number of pseudo-replicates was set to 3, and filtered with FDR < 0.05.
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Nutrient-derived signals regulate eosinophil adaptation to the small intestine. (PNAS 2024)

- DOI: 10.1073/pnas.2316446121 | PMCID: PMC10835075 | PMID: 38271336
- Evidence: Differential expression, defined as a fold change ≥ 1.5 and an adjusted P -value ≤ 0.05, was determined using DESeq2 ( 72 ).
- Full pipeline: read trimming [kallisto] -> alignment/mapping [kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [R]

### Extraordinary preservation of gene collinearity over three hundred million years revealed in homosporous lycophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2312607121 | PMCID: PMC10823260 | PMID: 38236735
- Version used: **3.17**
- Evidence: Homoeologous expression bias (HEB) gene sets in H. asiatica were identified between all the homoeologous gene pairs of two subgenomes using the DESeq2 v3.17 package ( 66 ).
- Full pipeline: stage not stated [ANGSD v0.935, BUSCO, DESeq2 v3.17, RAxML v8.2.12]

### BRCA1 and ELK-1 regulate neural progenitor cell fate in the optic tectum in response to visual experience in <i>Xenopus laevis</i> tadpoles. (PNAS 2024)

- DOI: 10.1073/pnas.2316542121 | PMCID: PMC10801852 | PMID: 38198524
- Evidence: We identified 1,130 transcripts that were differentially expressed between NPCs and immature neurons using DESeq2 ( SI Appendix , Figs.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, Cufflinks, Cytoscape, ImageJ]

### DIDO is necessary for the adipogenesis that promotes diet-induced obesity. (PNAS 2024)

- DOI: 10.1073/pnas.2300096121 | PMCID: PMC10801893 | PMID: 38194457
- Evidence: The expression level of all genes was estimated by DESeq2.
- Full pipeline: alignment/mapping [BWA, Picard] -> quantification [StringTie] -> stage not stated [DESeq2]

### Disruption of DNA methylation-mediated cranial neural crest proliferation and differentiation causes orofacial clefts in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2317668121 | PMCID: PMC10801837 | PMID: 38194455
- Evidence: Gene expression was calculated using RSEM which employed a forward probability of 0.0, followed by differential expression analysis using DESeq2 ( 78 ).
- Full pipeline: quality control [FastQC] -> read trimming [RSEM v1.3.1, STAR v2.7.0] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.0] -> variant calling [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### Gut metabolite L-lactate supports <i>Campylobacter jejuni</i> population expansion during acute infection. (PNAS 2024)

- DOI: 10.1073/pnas.2316540120 | PMCID: PMC10786315 | PMID: 38170751
- Evidence: ( B ) Differentially abundant taxa were found on day 3 between infected and uninfected (PBS) ferrets using DESeq2.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### A TLR4/TRAF6-dependent signaling pathway mediates NCoR coactivator complex formation for inflammatory gene activation. (PNAS 2024)

- DOI: 10.1073/pnas.2316104121 | PMCID: PMC10786282 | PMID: 38165941
- Evidence: The significance symbols indicate statistical significance, *** P -adj < 0.001 reported by DESeq2 using the Benjamini–Hochberg method for the multiple-testing correction.
- Full pipeline: differential/statistical testing [DESeq2]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: Differential gene expression analysis was analyzed using DESeq2 in the R statistical computing environment ( 63 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### Distinct classes of gut bacterial molybdenum-dependent enzymes produce urolithins. (PNAS 2025)

- DOI: 10.1073/pnas.2501312122 | PMCID: PMC12771579 | PMID: 41439715
- Version used: **1.44.0**
- Evidence: Then, total RNA was extracted and sequenced, and differential gene expression analysis was performed using DESeq2 v1.44.0 ( 85 ), as described in SI Appendix .
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [statsmodels] -> differential/statistical testing [DESeq2 v1.44.0, statsmodels]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Version used: **1.40.2**
- Evidence: Differential gene expression analysis was performed using DESeq2 1.40.2, differentially expressed genes were defined by having Benjamini and Hochberg-adjusted P value < 0.05 and |log 2 fold change| > 1.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### Antibiotic-induced microbiota depletion impairs the proregenerative response to a biological scaffold. (PNAS 2025)

- DOI: 10.1073/pnas.2510841122 | PMCID: PMC12772165 | PMID: 41428865
- Version used: **1.42.0**
- Evidence: Differential gene expression analysis was performed with DESeq2 v1.42.0 based on a negative binomial model with shrinkage estimation of the logarithmic-fold change (logFC).
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.42.0] -> stage not stated [GSEA, fgsea v1.28.0]

### Maladaptive immunity to the microbiota promotes neuronal hyperinnervation and itch via IL-17A. (PNAS 2025)

- DOI: 10.1073/pnas.2525146122 | PMCID: PMC12772199 | PMID: 41428888
- Version used: **1.44.0**
- Evidence: Differential expression was analyzed in DESeq2 v1.44.0 (no log2FC shrinkage, thresholds: log2FC > 0.3, adj.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.44.0] -> visualisation [UMAP] -> stage not stated [Metascape, R v4.4, Seurat v4.4.0]

### Dual-targeted ping-pong CAR T cells: Leveraging peripheral expansion to improve solid tumor immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2518996122 | PMCID: PMC12745717 | PMID: 41397127
- Evidence: Data were normalized and analyzed using DESeq2 and the top 50 differentially expressed genes were plotted in the form of a heatmap.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Bioconductor, GSVA, R, ggplot2]

### MBNL loss of function in smooth muscle as a model for myotonic dystrophy associated gastrointestinal dysmotility. (PNAS 2025)

- DOI: 10.1073/pnas.2522788122 | PMCID: PMC12718393 | PMID: 41379996
- Version used: **1.42.0**
- Evidence: Sequencing results were quality assessed, aligned, normalized, and analyzed using similar methods as previous work ( 124 ) using FastQC version 0.11.9, STAR version 2.7.10b, RSEM algorithm version 1.3.1 ( 125 ), DESeq2 version 1.42.0 for DGE ( 126 ), and rMATS version 4.1.2 for alternative splicing ( 127 ).
- Full pipeline: quality control [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> alignment/mapping [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> variant calling [ImageJ] -> normalisation [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> stage not stated [Metascape]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Version used: **1.42.0**
- Evidence: Differential analysis was performed with DESeq2 (v 1.42.0), using a cutoff of padj < 0.05 and |log2FC| ≥ 1.
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Galectin-9 binding to HLA-DR in dendritic cells controls immune synapse formation and T cell proliferation. (PNAS 2025)

- DOI: 10.1073/pnas.2501381122 | PMCID: PMC12718305 | PMID: 41359845
- Evidence: Count normalization was performed using rlog normalization via DESeq2 in R (56) .
- Full pipeline: alignment/mapping [STAR] -> normalisation [DESeq2, R] -> differential/statistical testing [Fiji, ImageJ] -> stage not stated [GSEA, fgsea]

### Combination of Cas9 and adeno-associated vectors enables efficient in vivo knockdown of precise miRNAs in the rodent and primate brain. (PNAS 2025)

- DOI: 10.1073/pnas.2513076122 | PMCID: PMC12718335 | PMID: 41359835
- Version used: **1.44.0**
- Evidence: Then raw count data representing the number of sequencing reads mapped to each gene were exported from GeneGlobe for further differential gene expression (DGE) analysis using the DESeq2 (1.44.0) package in Rstudio (4.4.1).
- Full pipeline: read trimming [BLAST, Cutadapt] -> alignment/mapping [BLAST, DESeq2 v1.44.0] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.44.0, R]

### Ace2 safeguards embryonic hematopoietic stem and progenitor cell production by restraining Nlrp3-mediated pyroptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2515641122 | PMCID: PMC12704739 | PMID: 41348733
- Version used: **1.10.1**
- Evidence: Differential expressed gene were identified using DESeq2 (version 1.10.1 under R version 3.2.3) ( 68 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.1.0] -> quantification [StringTie v1.3.3b] -> dimensionality reduction/clustering [clusterProfiler v4.6.1] -> differential/statistical testing [DESeq2 v1.10.1, R v3.2.3] -> stage not stated [GSEA, ImageJ]

### LHPP expression in triple-negative breast cancer promotes tumor growth and metastasis by modulating the tumor microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2505653122 | PMCID: PMC12704765 | PMID: 41343666
- Evidence: To identify DEGs a differential gene expression analysis was done by using DESeq2 with a Benjamini–Hochberg false discovery rate and a differential gene screening threshold of log2 (Fold Change) ≥ 1 and P -adj ≤ 0.05.
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2]

### Oxidative pentose phosphate pathway is required for T cell activation and antitumor immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2516288122 | PMCID: PMC12704759 | PMID: 41337482
- Evidence: Differential expressions were determined using DESeq2.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Evidence: Differential expression analysis was conducted using DESeq2 [v1.49.1 ( 40 )].
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### Glycoside hydrolase-mediated glucomannan catabolism in &lt;i&gt;Segatella copri&lt;/i&gt;, a target of microbiota-directed foods for malnourished children. (PNAS 2025)

- DOI: 10.1073/pnas.2521522122 | PMCID: PMC12704710 | PMID: 41329729
- Evidence: The resulting reads were subjected to routine quality control, mapped to the S. copri BgF5_2 genome using kallisto ( 46 ), and differential expression was determined for individual genes (DESeq2, ref.
- Full pipeline: quality control [DESeq2, kallisto] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [AlphaFold, GSEA, fgsea]

### Brain-wide mapping of developmental trajectories of cerebellar efferent projections. (PNAS 2025)

- DOI: 10.1073/pnas.2521091122 | PMCID: PMC12685143 | PMID: 41289407
- Evidence: Pseudobulk differential expression and gene set enrichment analyses were performed using DESeq2 and clusterProfiler.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [DESeq2, clusterProfiler] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler]

### Microbial necromass carbon enhances arsenic methylation in paddy soils. (PNAS 2025)

- DOI: 10.1073/pnas.2527462122 | PMCID: PMC12685052 | PMID: 41289391
- Version used: **1.44.0**
- Evidence: Differentially abundant taxa harboring the arsM gene across control and treatment groups were identified using DESeq2 v1.44.0 ( 44 ).
- Full pipeline: differential/statistical testing [DESeq2 v1.44.0] -> stage not stated [BLAST, R v4.2, RAxML]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: Differential gene expression was analyzed using DESeq2 ( 62 ) version 1.43.5.
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Evidence: The unique mapped reads were used to calculate transcripts per million using RNA-seq by expectation-maximization (v1.3.0) ( 73 ), and differentially expressed genes were identified with the DESeq2 R package (v1.24.0) ( 74 ), retaining genes with >5 raw counts in at least half of the analyzed samples and applying a Benjamini–Hochberg (BH) adjusted P < 0.1 ( Dataset S2 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### An AINTEGUMENTA phosphoswitch controls bilateral stem cell activity during secondary growth. (PNAS 2025)

- DOI: 10.1073/pnas.2510538122 | PMCID: PMC12663975 | PMID: 41264254
- Evidence: Reads were counted using Tximport, and differential gene expression analysis was performed using DESeq2 ( Dataset S1 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> quantification [R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3, emmeans] -> stage not stated [Galaxy, ggplot2 v3.4.3]

### The liver talks back: NPY orchestrates attraction of cancer cells and CHK2-dependent clonogenicity in the metastatic niche. (PNAS 2025)

- DOI: 10.1073/pnas.2518418122 | PMCID: PMC12663930 | PMID: 41252148
- Evidence: Statistical significance was determined by adjusted P -values which were calculated using the Benjamini–Hochberg method within DESeq2 (DEGs with an adjusted P -value < 0.1 were regarded as statistically significant) ( E and F ) or by one-way ANOVA ( I – K ).
- Full pipeline: differential/statistical testing [DESeq2, GSEA]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Normalization and analysis of the RNA read count matrix were performed using the Bioconductor R package DESeq2 with default settings.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Machine-learning models based on histological images from healthy donors identify imageQTLs and predict chronological age. (PNAS 2025)

- DOI: 10.1073/pnas.2423469122 | PMCID: PMC12646272 | PMID: 41218125
- Evidence: DE analysis for each tissue and nucleus feature was conducted using DESeq2’s standard pipeline with the likelihood ratio test ( 50 ).
- Full pipeline: alignment/mapping [FUMA] -> differential/statistical testing [PLINK v2.0] -> stage not stated [DESeq2, GSEA, QuPath v0.4.3]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Evidence: Statistical testing, normalization, clustering, and enrichment analysis were performed with the DESeq2 module within the NeatSeq-Flow platform ( 90 ).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Version used: **1.20.0**
- Evidence: The resulting read alignment was assembled using Cufflinks (v.2.2.1) and fold changes, significance values were calculated using DESeq2 (v.1.20.0).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: 1.2.0) utilizes DESeq2 for statistical analysis.
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **1.46.0**
- Evidence: Differential expression analysis was conducted in R 4.4.3 using DESeq2 (v1.46.0).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Evidence: Differential expression between large-bodied and miniature species was assessed using the DESeq2 method ( 89 ) in R .
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Joint disruption of &lt;i&gt;Ret&lt;/i&gt; and &lt;i&gt;Ednrb&lt;/i&gt; transcription shifts cell fate trajectories in the enteric nervous system in Hirschsprung disease. (PNAS 2025)

- DOI: 10.1073/pnas.2507062122 | PMCID: PMC12582274 | PMID: 41118220
- Evidence: Cleaned counts were then processed through DESeq2 ( 41 ) along with two general linear models split by time (of the form): Y GE = β Ret .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [clusterProfiler] -> stage not stated [Seurat]

### HIF2α negatively regulates MYCN protein levels and promotes a low-risk noradrenergic phenotype in neuroblastoma. (PNAS 2025)

- DOI: 10.1073/pnas.2516922122 | PMCID: PMC12582314 | PMID: 41118218
- Evidence: Paired-end RNA sequencing was performed by Novogene, and high-throughput sequencing data were processed for quality control, alignment, and differential expression analysis using a combination of established bioinformatics tools, such as FastQC, STAR, and DESeq2.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2, FastQC, GSEA] -> visualisation [UMAP] -> stage not stated [R, Scanpy, Seurat]

### Neuronal plasticity at puberty in mouse hypothalamic &lt;i&gt;Kiss1&lt;/i&gt; neurons that control fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2512855122 | PMCID: PMC12582290 | PMID: 41118223
- Evidence: Differential expression analysis was performed with the DESeq2 R-package.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: Differential expression analysis was done from filtered CPM normalized counts (CPM <1 across half of the samples) using DESeq2 ( 30 ) (Bioconductor Release: 3.14) in R version 3.4.1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### The integrated stress response suppresses antiviral RNA interference by autophagy-mediated degradation of the RNA-induced silencing complex. (PNAS 2025)

- DOI: 10.1073/pnas.2511857122 | PMCID: PMC12541439 | PMID: 41060764
- Evidence: DEGs were identified using DESeq2.
- Full pipeline: stage not stated [DESeq2]

### Regulation of an lncRNA &lt;i&gt;irf8&lt;/i&gt; by the Ikzf1/Myb complex drives neutrophil development. (PNAS 2025)

- DOI: 10.1073/pnas.2502741122 | PMCID: PMC12541332 | PMID: 41060766
- Evidence: ( K ) Fragments per kilobase million (FPKM) for neutrophil marker genes and macrophage related genes across WT and DMs; significance represents the P value from DESeq2 differential analysis comparing DM samples to WT. * P < 0.05, ** P < 0.01, *** P < 0.001, **** P < 0.0001.
- Full pipeline: quantification [DESeq2] -> differential/statistical testing [DESeq2]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Significantly DEGs with absolute fold change ≥ 1.5 and FDR adjusted P value ≤ 0.05 were detected by DESeq2 (NA) ( 58 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: For RNA-seq and ATAC-seq analyses, statistical testing was performed using DESeq2 and DiffBind, respectively.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Targeting the 3D genome by anthracyclines for chemotherapeutic effects. (PNAS 2025)

- DOI: 10.1073/pnas.2500704122 | PMCID: PMC12519215 | PMID: 41042842
- Evidence: Adjusted P values were calculated by DESeq2.
- Full pipeline: differential/statistical testing [DESeq2, limma] -> stage not stated [HOMER]

### Autoimmunity-associated DIORA1 binds the MRCK family of serine/threonine kinases and controls cell motility. (PNAS 2025)

- DOI: 10.1073/pnas.2426917122 | PMCID: PMC12519202 | PMID: 41042840
- Evidence: Transcriptomic data were processed using standard pipelines and analyzed with DESeq2 and gene set enrichment tools, including GSEA and overrepresentation analysis using HALLMARK gene sets.
- Full pipeline: visualisation [STRING db] -> stage not stated [AlphaFold, DESeq2, GSEA, UCSF Chimera]

### The role of colony morphotype in shaping gene essentiality in &lt;i&gt;Mycobacteroides abscessus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500719122 | PMCID: PMC12519085 | PMID: 41026822
- Version used: **1.18.1**
- Evidence: Essential genes were determined using TnSeqDESeq2Essential_mariner.sh and TnGeneBin.pl relying on R v3.4.2, DESeq2 v1.18.1 ( 59 ), and mclust v5.4.
- Full pipeline: stage not stated [Bowtie2 v2.4.2, Cutadapt v3.3, DESeq2 v1.18.1, R v3.4]

### The genome of the vining fern &lt;i&gt;Lygodium microphyllum&lt;/i&gt; highlights genomic and functional differences between life phases of an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2504773122 | PMCID: PMC12501142 | PMID: 40996792
- Version used: **1.44.0**
- Evidence: Analysis of differential gene expression was performed with DESeq2 v1.44.0 ( 93 ) and alternative splicing events identified using a modified pipeline from Chamala et al.
- Full pipeline: differential/statistical testing [DESeq2 v1.44.0] -> stage not stated [BUSCO, hifiasm v0.19.9]

### Posttranscriptional control of the B cell receptor by HuR is essential for innate B cell maintenance and function. (PNAS 2025)

- DOI: 10.1073/pnas.2421149122 | PMCID: PMC12452923 | PMID: 40938701
- Version used: **1.28.0**
- Evidence: DESeq2 (v1.28.0) was used for differential expression analysis using default parameters.
- Full pipeline: differential/statistical testing [DESeq2 v1.28.0] -> stage not stated [Enrichr]

### Replication stress-induced nuclear hypertrophy alters chromatin topology and impacts cancer cell fitness. (PNAS 2025)

- DOI: 10.1073/pnas.2424709122 | PMCID: PMC12452916 | PMID: 40928878
- Evidence: Differential gene expression analysis using DESeq2 ( 41 ) identified 523 genes with increased expression and 713 genes with decreased expression ( SI Appendix, Fig.
- Full pipeline: quantification [CellProfiler v4.2.1] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Version used: **1.40.2**
- Evidence: R package DESeq2 (version 1.40.2) was then used to normalize read counts among samples and to identify differentially expressed genes between biological samples ( 42 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### Evidence for coopetition at the maternal-fetal interface shaping placental invasion. (PNAS 2025)

- DOI: 10.1073/pnas.2323038122 | PMCID: PMC12435225 | PMID: 40906814
- Evidence: Differential expression calculations for P values and fold changes were conducted using DESeq2 on the R platform.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [ImageJ] -> differential/statistical testing [DESeq2]

### Mutations in the circadian cycle drive adaptive plasticity in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2506928122 | PMCID: PMC12435244 | PMID: 40901874
- Version used: **1.34.0**
- Evidence: Differential expression of mRNA transcripts was computed with DESeq2 (v1.34.0) ( 66 ), using a P adj value < 10 −8 as statistical cutoff.
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [StringTie v2.2.1, featureCounts v2.0.1] -> normalisation [StringTie v2.2.1] -> differential/statistical testing [DESeq2 v1.34.0, R v4.2.1]

### Lysosomal reduced thiols are essential for mouse embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2427125122 | PMCID: PMC12435214 | PMID: 40892915
- Evidence: Differential expression analysis was conducted using DESeq2.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Tumor-expressed GPNMB orchestrates Siglec-9&lt;sup&gt;+&lt;/sup&gt; TAM polarization and EMT to promote metastasis in triple-negative breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2503081122 | PMCID: PMC12435292 | PMID: 40892920
- Evidence: ( C ) MSigDB Hallmark pathway enrichment analysis based on DESeq2-filtered differentially expressed genes (Q < 0.05, FC > 2).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [AlphaFold] -> machine learning [UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina, GSEA, R v4.3.0]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: DESeq2 was used to analyze differential gene expression between any two stages among stages 1, 2, 4, and 5.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Shared metabolism between a bacterial and fungal species that reside in the human gut. (PNAS 2025)

- DOI: 10.1073/pnas.2504785122 | PMCID: PMC12415286 | PMID: 40854125
- Version used: **1.40.2**
- Evidence: Count normalization and differential expression analysis was performed using DESeq2 (1.40.2) ( 66 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.14] -> quantification [featureCounts v2.0.1] -> normalisation [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2]

### Coordinated actions of NLR-assembled and glutamate receptor-like calcium channels in plant effector-triggered immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2508018122 | PMCID: PMC12415192 | PMID: 40844808
- Version used: **1.38.0**
- Evidence: DEG were identified by using R package DESeq2 (v1.38.0).
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT v7.505] -> stage not stated [ComplexHeatmap, DESeq2 v1.38.0, R, ggplot2 v3.4.2]

### N&lt;sup&gt;6&lt;/sup&gt;-methyladenine modification of DNA enhances RecA-mediated homologous recombination. (PNAS 2025)

- DOI: 10.1073/pnas.2508652122 | PMCID: PMC12403123 | PMID: 40833402
- Evidence: Differential gene expression analysis was performed using DESeq2.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2]

### Synergistic action of specialized metabolites from divergent biosynthesis in the human oral microbiome. (PNAS 2025)

- DOI: 10.1073/pnas.2504492122 | PMCID: PMC12403116 | PMID: 40828023
- Evidence: We screened three previously published metagenomic datasets of caries and caries-free plaque samples for sequence similarity matches with the BGCs via BWA-MEM ( 35 ) and DESeq2 ( 36 ).
- Full pipeline: read trimming [Trimmomatic] -> stage not stated [BWA, DESeq2]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Evidence: Gene expression differences between KO/nontarget or treated/nontreated samples, after QC filter, were determined using DESeq2 [v1.22.2 ( 63 )].
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Version used: **1.40.2**
- Evidence: DEGs were identified using DESeq2 (version 1.40.2), with a false discovery rate (FDR) of less than 1% and |log 2 (fold change)| > 1.
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Version used: **1.34.0**
- Evidence: Machine learning and model training were performed using DESeq2 (v1.34.0) ( 66 ), Caret33 (v6.0.90) ( 67 ), and pROC34 (v1.18.0) ( 68 ) R packages.
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Version used: **1.44.0**
- Evidence: The resulting counts were then imported into DESeq2(v1.44.0) ( 49 ) with design formulae relevant to each experiment.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Transcription termination promotes splicing efficiency and fidelity in a compact genome. (PNAS 2025)

- DOI: 10.1073/pnas.2507187122 | PMCID: PMC12358841 | PMID: 40763012
- Evidence: DESeq2 ( 36 ) was used to quantify changes in gene expression and for normalizing counts to library size.
- Full pipeline: alignment/mapping [featureCounts, minimap2] -> quantification [DESeq2, featureCounts] -> normalisation [DESeq2] -> stage not stated [BEDTools, SAMtools]

### Pelota-mediated ribosome-associated quality control counteracts aging and age-associated pathologies across species. (PNAS 2025)

- DOI: 10.1073/pnas.2505217122 | PMCID: PMC12358915 | PMID: 40758887
- Version used: **1.28.1**
- Evidence: Raw counts were then normalized by using variance stabilizing transformation (vst) from the DESeq2 (v1.28.1).
- Full pipeline: normalisation [DESeq2 v1.28.1] -> stage not stated [ImageJ]

### Neuronal processes contain the essential components for the late steps of ribosome biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2502424122 | PMCID: PMC12337303 | PMID: 40743395
- Evidence: The DESeq2 package facilitated quality control through PCA plots and differential expression testing., All pipeline code is accessible in the [trnatools] ( https://gitlab.mpcdf.mpg.de/mpibr/schu/trnatools ) repository.
- Full pipeline: quality control [DESeq2] -> read trimming [fastp] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Lysosomal glucocerebrosidase is needed for ciliary Hedgehog signaling: A convergent pathway contributing to Parkinson's disease. (PNAS 2025)

- DOI: 10.1073/pnas.2504774122 | PMCID: PMC12337309 | PMID: 40737317
- Evidence: Genes with an adjusted P -value < = 0.05 found by DESeq2 were assigned as differentially expressed.
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [CellProfiler]

### Deficiency in transmitter release triggers homeostatic transcriptional changes that increase presynaptic excitability. (PNAS 2025)

- DOI: 10.1073/pnas.2322714122 | PMCID: PMC12337328 | PMID: 40729383
- Version used: **1.26.0**
- Evidence: Libraries were normalized by calculating a size factor for each sample from the median ratio of gene expression relative to the geometric mean for each gene as implemented in DESeq2 (ver 1.26.0) ( 84 ).
- Full pipeline: quality control [FastQC v0.11.7, Trimmomatic v0.38] -> read trimming [FastQC v0.11.7, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0, featureCounts] -> normalisation [DESeq2 v1.26.0] -> visualisation [ggplot2 v3.2.1] -> stage not stated [R v4.1.0]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: DEGs were identified using DESeq2 (q < 0.05, foldchange > 2, or foldchange < 0.5).
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### Effects of the gut microbiota on placental angiogenesis and intrauterine growth in gnotobiotic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426341122 | PMCID: PMC12318179 | PMID: 40711921
- Evidence: Genes with statistically significant differences in their levels of expression (differentially expressed genes, DEGs) were identified using DESeq2 ( 26 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, lme4] -> stage not stated [QuPath v0.4.4]

### Complementary genetic and epigenetic changes facilitate rapid adaptation to multiple global change stressors. (PNAS 2025)

- DOI: 10.1073/pnas.2422782122 | PMCID: PMC12305003 | PMID: 40663607
- Evidence: Expression levels and differences were analyzed using DESeq2 ( 75 ), and plastic genes were identified as those changing expression (adjusted P -value < 0.05) within a line following transplant to the opposite environment.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bismark v0.22.3, Bowtie2 v2.2.6] -> differential/statistical testing [R v3.6.0, edgeR] -> stage not stated [BEDTools, DESeq2]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Evidence: DESeq2 was used to analyze differential gene expression ( 53 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Multiorgan transcriptomics in mice identifies immunoglobulin heavy constant mu (&lt;i&gt;Ighm&lt;/i&gt;) as a tissue-level aging biomarker. (PNAS 2025)

- DOI: 10.1073/pnas.2423142122 | PMCID: PMC12280941 | PMID: 40643973
- Evidence: ( H ) Volcano plot of age-related transcripts calculated using DESeq2, with sex and tissue as covariates.
- Full pipeline: read trimming [fastp v0.23.1] -> alignment/mapping [STAR v2.7.11b] -> quantification [ImageJ] -> dimensionality reduction/clustering [edgeR v4.2.1] -> visualisation [edgeR v4.2.1] -> stage not stated [DESeq2, R v4.4.1]

### The WWP1-JARID1B axis sustains acute myeloid leukemia chemoresistance. (PNAS 2025)

- DOI: 10.1073/pnas.2421159122 | PMCID: PMC12280953 | PMID: 40627385
- Evidence: The differential expression analysis was performed using DESeq2 package from Xena Browser.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2, Enrichr] -> stage not stated [ggplot2]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: The DESeq2 package was applied to identify DEGs (fold change > 1.2 and P value < 0.05).
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### HIF1α mediates circadian regulation of skeletal muscle metabolism and substrate preference in response to time-of-day exercise. (PNAS 2025)

- DOI: 10.1073/pnas.2504080122 | PMCID: PMC12280960 | PMID: 40627397
- Evidence: Lowly expressed genes were removed through independent filtering using the mean of normalized counts as a filter statistic in “DESeq2,” with 20,224 genes passing the independent filtering threshold.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> quantification [Python] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [emmeans]

### Human milk IgA promotes normal immune development by limiting Th17-inducing <i>Erysipelatoclostridium ramosum</i> in the infant gut. (PNAS 2025)

- DOI: 10.1073/pnas.2501030122 | PMCID: PMC12280908 | PMID: 40623174
- Evidence: FastQC and STAR were used for data processing and alignment, and the DESeq2 package was used in R for differential abundance analysis.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> quantification [DESeq2, FastQC, R] -> differential/statistical testing [DESeq2, FastQC, R] -> stage not stated [STRING db]

### A transcriptomic, proteomic, and functional genetic atlas dissects neurofibromin function in the peripheral nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2506823122 | PMCID: PMC12260521 | PMID: 40587782
- Evidence: Transcript abundance estimation in transcripts per million (TPM) and differential expression analysis were performed using DESeq2 ( 33 ).
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> visualisation [Cytoscape, STRING db]

### The RRM domain-containing protein Rbp3 interacts with ribosomes and the 3' ends of mRNAs encoding photosynthesis proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2506275122 | PMCID: PMC12232666 | PMID: 40553498
- Evidence: After reverse transcription and sequencing, the RNA sequencing data were mapped to the genome of Synechocystis 6803, followed by a DESeq2 ( 37 ) analysis of transcripts enriched in the Rbp3-3×FLAG pulldown compared to the sfGFP-3×FLAG pulldown.
- Full pipeline: alignment/mapping [DESeq2] -> normalisation [R, limma] -> stage not stated [AlphaFold]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Transcript counts were calculated using featureCounts (Subread) and differential gene expression analysis was performed using DESeq2 ( 62 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Longitudinal sequencing reveals polygenic and epistatic nature of genomic response to selection. (PNAS 2025)

- DOI: 10.1073/pnas.2410452122 | PMCID: PMC12207516 | PMID: 40531879
- Evidence: For each tissue separately, we used a Wald test in DESeq2 ( 62 ) and the following design: Expression ~ Plate + Diet + Genotype, where Plate indicates the 96-well plate in which samples were processed from sample collection through library preparation; Diet represents the dietary condition the flies were exposed to for one generation ( hs or control ); Genotype represents the diet flies evolved in...
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA, Picard] -> variant calling [DESeq2] -> dimensionality reduction/clustering [PLINK] -> stage not stated [R, emmeans]

### Antlers on does: An unexpected role of macrophages in deer biology. (PNAS 2025)

- DOI: 10.1073/pnas.2424448122 | PMCID: PMC12184406 | PMID: 40512783
- Evidence: After cleaning the raw data, and using the deer reference genome, we utilized the workflows of HISAT2, StringTie, and DESeq2 ( 33 ) to analyze differentially expressed genes (DEGs) with |log 2 FoldChange| ≥ 2 and Benjamini–Hochberg P -value < 0.001 between two groups.
- Full pipeline: alignment/mapping [DESeq2, HISAT2, StringTie] -> quantification [ImageJ] -> normalisation [ImageJ] -> differential/statistical testing [DESeq2, HISAT2, StringTie] -> stage not stated [GSEA, Seurat]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: Differentially expressed genes (DEGs) were identified using the R package DESeq2 ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **1.42.1**
- Evidence: The R package DESeq2 v1.42.1 was used with default parameters for the differential gene expression analysis.
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Light at night negatively affects mood in diurnal primate-like tree shrews via a visual pathway related to the perihabenular nucleus. (PNAS 2025)

- DOI: 10.1073/pnas.2411280122 | PMCID: PMC12167994 | PMID: 40478874
- Evidence: After acquiring the expression matrix, differential expression analysis was conducted using the DESeq2 ( 64 ) package for R.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: DAPs were identified through DESeq2 (Version 1.28.1) and annotated by R package ChIPseeker (Version 1.26.2).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Version used: **1.34.0**
- Evidence: Hisat2 v2.2.1 ( https://daehwankimlab.github.io/hisat2/ ) was used to align the reads to the house mouse genome (GCF_000001635.26), Stringtie v2.2.1 ( https://ccb.jhu.edu/software/stringtie/ ) to assemble the transcriptome, and DESeq2 v1.34.0 ( https://bioconductor.org/packages/release/bioc/html/DESeq2.html ) to analyze differential gene expression.
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### Mechanisms of photoreceptor protection upon targeting the &lt;i&gt;Nrl-Nr2e3&lt;/i&gt; pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2500446122 | PMCID: PMC12130857 | PMID: 40397675
- Version used: **1.42.0**
- Evidence: Differential gene expression was calculated using DESeq2 (v1.42.0) ( 49 ), requiring a minimum log 2 fold-change of 1 and an adjusted p-value of 0.05.
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [DESeq2 v1.42.0]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Evidence: Downstream DE analysis was performed by DESeq2 in R.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Mutant &lt;i&gt;IDH1&lt;/i&gt; cooperates with &lt;i&gt;NPM1c&lt;/i&gt; or &lt;i&gt;FLT3&lt;/i&gt;&lt;sup&gt;ITD&lt;/sup&gt; to drive distinct myeloid diseases and molecular outcomes. (PNAS 2025)

- DOI: 10.1073/pnas.2415779122 | PMCID: PMC12107087 | PMID: 40377995
- Evidence: Differential gene expression analysis was performed using DESeq2, and genes with fold-change >1.5 and adjusted P -value <0.01 were regarded as differentially expressed.
- Full pipeline: differential/statistical testing [DESeq2, GSVA] -> stage not stated [GSEA]

### Murine gut microbiota dysbiosis via enteric infection modulates the foreign body response to a distal biomaterial implant. (PNAS 2025)

- DOI: 10.1073/pnas.2422169122 | PMCID: PMC12107164 | PMID: 40354538
- Evidence: Differential gene expression analysis was performed with DESeq2 ( 82 ) based on a negative binomial model with shrinkage estimation of the logarithmic fold change.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, fgsea]

### Dmrt2 and Hmx2 direct intercalated cell diversity in the mammalian kidney through antagonistic and supporting regulatory processes. (PNAS 2025)

- DOI: 10.1073/pnas.2418471122 | PMCID: PMC12107187 | PMID: 40354537
- Evidence: Differential expression analysis was performed using DESeq2 in R.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Monocle, Seurat]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Version used: **1.34.0**
- Evidence: Analysis was performed using DESeq2 (v1.34.0), fgsea, and ranked gene lists.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### NF-κB-mediated developmental delay extends lifespan in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420811122 | PMCID: PMC12088391 | PMID: 40339121
- Evidence: To further characterize the biological processes that were enriched for specific developmental stages and specific genotypes, we performed DESeq2 differential expression analyses ( 44 ) to identify stage-specific genes for each genotype respectively (fold change > 2, FDR < 0.05), followed by DEG identification by comparing wild-type samples and Ptth mutant samples at each developmental stage (see ...
- Full pipeline: variant calling [DESeq2] -> differential/statistical testing [DESeq2]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Evidence: These counts were utilized for differential expression analysis with DESeq2.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Evidence: Gene expression data were preprocessed using tximport ( 88 ), and the differential expression analysis was performed with DESeq2 ( 89 ) in default settings.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### Cryptic genetic variation in brain gene expression precedes the evolution of cannibalism in spadefoot toad tadpoles. (PNAS 2025)

- DOI: 10.1073/pnas.2418431122 | PMCID: PMC12088425 | PMID: 40294283
- Evidence: To assess diet-specific and density-specific brain gene expression in S. holbrookii , we created a single DESeq2 model using both treatments as predictor variables (e.g., ~ density + diet).
- Full pipeline: differential/statistical testing [R, lme4] -> stage not stated [BUSCO, DESeq2, survival (R)]

### Genomic analysis of progenitors in viral infection implicates glucocorticoids as suppressors of plasmacytoid dendritic cell generation. (PNAS 2025)

- DOI: 10.1073/pnas.2410092122 | PMCID: PMC12067256 | PMID: 40294270
- Evidence: Differential expression was defined by DESeq2 with the threshold of FDR < 0.05.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Elevated UDP-glucuronic acid levels mend drug resistance and stress responses via a protease and a transporter in &lt;i&gt;Cryptococcus gattii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2503960122 | PMCID: PMC12054807 | PMID: 40267138
- Evidence: DESeq2 was used to calculate the differentially expressed genes.
- Full pipeline: differential/statistical testing [DESeq2]

### Horizontal transfer of nuclear DNA in transmissible cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2424634122 | PMCID: PMC12067285 | PMID: 40261943
- Evidence: Variants within exons were genotyped using alleleCounter v2.1.2 ( https://github.com/cancerit/alleleCount ), and expression counts were normalized using DESeq2 ( 63 ).
- Full pipeline: variant calling [DESeq2] -> quantification [R] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.2.5]

### Pathogen growth and virulence dynamics drive the host evolution against coinfections. (PNAS 2025)

- DOI: 10.1073/pnas.2412124122 | PMCID: PMC12054814 | PMID: 40267133
- Evidence: We performed differential gene expression analyses and generated heatmaps using the “DESeq2” package in R.
- Full pipeline: differential/statistical testing [DESeq2, emmeans]

### Phospholipid flippase ATP11A brokers uterine epithelial integrity and function. (PNAS 2025)

- DOI: 10.1073/pnas.2420617122 | PMCID: PMC12054786 | PMID: 40261925
- Evidence: Differential expression was calculated using DESeq2 and adjusted for multiple testing correction using the Benjamini–Hochberg method ( Padj < 0.05).
- Full pipeline: quality control [R, Seurat v5.1.0] -> alignment/mapping [STAR v2.6.1a] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq, ImageJ v1.53, Metascape]

### PPARα regulates ER-lipid droplet protein Calsyntenin-3β to promote ketogenesis in hepatocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2426338122 | PMCID: PMC12054784 | PMID: 40258152
- Evidence: Raw count matrices were analyzed using DESeq2 in R for differential gene expression.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### Diet-regulated transcriptional plasticity of plant parasites in plant-mutualist environments. (PNAS 2025)

- DOI: 10.1073/pnas.2421367122 | PMCID: PMC12037023 | PMID: 40244681
- Evidence: Gene counts were quantified by HTSeq ( 53 ) and analyzed by DESeq2 (53 to yield differential gene expression profiles of G. pallida parasitizing potato roots ± distal and concurrent AM fungal colonization.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [DESeq2, HTSeq, ImageJ] -> differential/statistical testing [DESeq2, HTSeq] -> stage not stated [IQ-TREE]

### The multifaceted roles of the transcriptional coactivator TAZ in extravillous trophoblast development of the human placenta. (PNAS 2025)

- DOI: 10.1073/pnas.2426385122 | PMCID: PMC12037006 | PMID: 40228123
- Evidence: ( A ) Volcano plots showing DEGs (dots illustrate individual transcripts, colored according to P values and log2 fold change (DESeq2, standard parameters, P adj < 0.05, DE: fold change > 1.5).
- Full pipeline: differential/statistical testing [DESeq2]

### Perturbing nuclear glycosylation in the mouse preimplantation embryo slows down embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2410520122 | PMCID: PMC12012502 | PMID: 40203037
- Evidence: ( E ) Mean DESeq2-normalized counts of E7 mesoderm markers from ref.
- Full pipeline: read trimming [STAR v2.7.8a] -> alignment/mapping [STAR v2.7.8a] -> normalisation [DESeq2, deepTools v3.0.2] -> stage not stated [GSEA, ImageJ, featureCounts]

### A conserved ARF-DNA interface underlies auxin-triggered transcriptional response. (PNAS 2025)

- DOI: 10.1073/pnas.2501915122 | PMCID: PMC12002309 | PMID: 40168121
- Evidence: Finally, genes with low counts (<90 across all samples together) were removed and differentially expressed genes were calculated with DESeq2 ( 48 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [featureCounts] -> quantification [ilastik v1.3.3] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, HMMER, PyMOL]

### Modulation of host gene expression by the zinc finger antiviral protein. (PNAS 2025)

- DOI: 10.1073/pnas.2420819122 | PMCID: PMC12002351 | PMID: 40146858
- Evidence: Raw reads were aligned to the mouse genome ( Mus musculus ensemble 94) using STAR aligner and differentially gene expression analysis was performed using DESeq2 ( 49 ).
- Full pipeline: alignment/mapping [DESeq2, STAR] -> differential/statistical testing [DESeq2, STAR] -> visualisation [ggplot2] -> stage not stated [Cytoscape]

### The PBAP chromatin remodeling complex mediates summer diapause via H3K4me3-driven juvenile hormone regulation in &lt;i&gt;Colaphellus bowringi&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2422328122 | PMCID: PMC11962415 | PMID: 40112108
- Evidence: DEGs were identified with DESeq2, applying criteria of |fold change| > 1 and FDR-adjusted P < 0.05.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### High-density CRISPRi screens reveal diverse routes to improved acclimation in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2412625122 | PMCID: PMC11962424 | PMID: 40117303
- Evidence: Data depict ( A ) normalized mean enrichment, ( B ) DESeq2-calculated sgRNA enrichment, and ( D ) mean locus enrichment for n = 2 biological replicates.
- Full pipeline: normalisation [DESeq2]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Evidence: Differential gene expression analysis between siblings and wdr5 mutants was performed by DESeq2, applying a threshold of P < 0.05 and an absolute fold change > 1.5.
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### Deficiency in platelet 12-lipoxygenase exacerbates inflammation and disease severity during SARS-CoV-2 infection. (PNAS 2025)

- DOI: 10.1073/pnas.2420441122 | PMCID: PMC11962506 | PMID: 40100623
- Evidence: Normalizations and statistical tests for differential expressions between time points were performed using the “DESeq2” R-package ( 39 ).
- Full pipeline: normalisation [DESeq2, R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R]

### Diel partitioning in microbial phosphorus acquisition in the Sargasso Sea. (PNAS 2025)

- DOI: 10.1073/pnas.2410268122 | PMCID: PMC11929403 | PMID: 40085655
- Evidence: Prior to timeseries analysis, all metatranscriptome read mappings were transformed using the DESeq2 variance stabilizing transformation ( 46 ).
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [BLAST, eggNOG, featureCounts] -> stage not stated [DESeq2]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Evidence: Differential gene-expression analysis was performed using the DESeq2 ( https://github.com/thelovelab/DESeq2 ) R package with parameters of greater than 1.5-fold change in expression and P -value < 0.05.
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Version used: **1.38.3**
- Evidence: Differentially expressed genes were identified in R version 4.2.1 ( 80 ) using the DESeq2 v1.38.3 package ( 81 ) following pairwise comparison of all samples (|log2FC| ≥ 0.5 and P adj ≤ 0.001).
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Evidence: DEGs were identified with DESeq2, applying thresholds of adjusted P -value < 0.05 and |log2FC| > 0.58.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### The NAE1-mediated neddylation operates as an essential post-translational modification checkpoint for effector CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424061122 | PMCID: PMC11912420 | PMID: 40030035
- Evidence: The DEG assay was done by DESeq2 V 3.19.
- Full pipeline: read trimming [HISAT2, SAMtools, Trim Galore v0.6.10] -> alignment/mapping [HISAT2, SAMtools, Trim Galore v0.6.10] -> stage not stated [DESeq2, GSEA, pheatmap]

### Chemical genetic interactions elucidate pathways controlling tuberculosis antibiotic efficacy during infection. (PNAS 2025)

- DOI: 10.1073/pnas.2417525122 | PMCID: PMC11892619 | PMID: 39993187
- Evidence: DEBRA implements a modified version of DESeq2 analysis ( 88 ) optimized for identifying differentially represented barcodes.
- Full pipeline: differential/statistical testing [DESeq2]

### pTDP-43 levels correlate with cell type-specific molecular alterations in the prefrontal cortex of &lt;i&gt;C9orf72&lt;/i&gt; ALS/FTD patients. (PNAS 2025)

- DOI: 10.1073/pnas.2419818122 | PMCID: PMC11892677 | PMID: 39999167
- Evidence: Utilizing the pseudobulk method, we aggregated fragment counts per sample-cell type combination and analyzed them using DESeq2 ( 14 ) with multifactor design to assess the significance of differentially accessible regions between control and C9orf72 ALS/FTD samples with varying levels of pTDP-43.
- Full pipeline: quality control [ArchR, Seurat, SoupX] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [WGCNA]

### The AaFoxA factor regulates female reproduction through chromatin remodeling in the mosquito vector Aedes aegypti. (PNAS 2025)

- DOI: 10.1073/pnas.2411758122 | PMCID: PMC11892592 | PMID: 39993202
- Evidence: The gene counts were normalized using DESeq2’s size factors and scaled using z-scores for heatmap visualization.
- Full pipeline: normalisation [DESeq2] -> visualisation [DESeq2]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Evidence: Counts were loaded into R, and the DESeq2 package was used to identify differentially expressed genes (FDR < 0.05) with a read count threshold at 58.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### Subfunctionalization and epigenetic regulation of a biosynthetic gene cluster in &lt;i&gt;Solanaceae&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420164122 | PMCID: PMC11874288 | PMID: 39977312
- Evidence: ( A ) Normalized read counts after variance-stabilizing transformation using the DESeq2 package ( 28 ) of the union (across leaf and root tissue) of narrow peaks.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> quantification [DESeq2] -> normalisation [DESeq2] -> visualisation [Python v3.9] -> stage not stated [IQ-TREE v2.1.4, OrthoFinder v2.5.4]

### Druggable genome screens identify SPP as an antiviral host target for multiple flaviviruses. (PNAS 2025)

- DOI: 10.1073/pnas.2421573122 | PMCID: PMC11874179 | PMID: 39969998
- Evidence: Count normalization and differential gene expression analysis were performed using the DESeq2 package ( 72 ).
- Full pipeline: alignment/mapping [HISAT2] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2]

### Extensive location bias of the GPCR-dependent translatome via site-selective activation of mTOR. (PNAS 2025)

- DOI: 10.1073/pnas.2414738122 | PMCID: PMC11874449 | PMID: 39964727
- Version used: **3.16**
- Evidence: DESeq2 (version 3.16) was used for differential expression analysis of raw reads.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v3.16] -> stage not stated [Cytoscape, R]

### Identification of FSH-regulated and estrous stage-specific transcriptional networks in mouse ovaries. (PNAS 2025)

- DOI: 10.1073/pnas.2411977122 | PMCID: PMC11848299 | PMID: 39928863
- Evidence: Differential gene expression was performed after filtering for expression using DESeq2 library ( 46 ) with the likelihood ratio test ( P adj < 0.05).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Ethylene-independent modulation of root development by ACC via downregulation of WOX5 and group I CLE peptide expression. (PNAS 2025)

- DOI: 10.1073/pnas.2417735122 | PMCID: PMC11831204 | PMID: 39908106
- Evidence: DEGs were identified using DESeq2 analysis tool on Partek® Flow® data analysis tool, software access provided by UNC Center for Bioinformatics.
- Full pipeline: alignment/mapping [STAR] -> stage not stated [DESeq2, ImageJ]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Evidence: DESeq2 ( 61 ) package in R ( 62 ) was used for differential gene expression analysis and LFC shrinkage to correct for low transcript counts.
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### Fatty acid metabolism and the oxidative stress response support bacterial predation. (PNAS 2025)

- DOI: 10.1073/pnas.2420875122 | PMCID: PMC11804543 | PMID: 39869799
- Evidence: The read counts were then normalized utilizing the DESeq2 method ( 45 ), and genes exhibiting differential expression were identified with a P -adjusted value <0.05 using the Wald test in DESeq2.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap] -> stage not stated [ImageJ]

### Targeting EPHB2/ABL1 restores antitumor immunity in preclinical models of ependymoma. (PNAS 2025)

- DOI: 10.1073/pnas.2319474122 | PMCID: PMC11789170 | PMID: 39841145
- Evidence: DEGs was performed by R Bioconductor package DESeq2 with a P -value of 0.01 and fold-change of 2 as the cutoff.
- Full pipeline: quantification [HTSeq] -> dimensionality reduction/clustering [R, STRING db, pheatmap] -> stage not stated [Bioconductor, DESeq2, Seurat]

### Dual modes of DNA N&lt;sup&gt;6&lt;/sup&gt;-methyladenine maintenance by distinct methyltransferase complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2413037121 | PMCID: PMC11761967 | PMID: 39813249
- Evidence: For RNA-seq, differentially expressed genes were identified by DESeq2 [Log 2 (FoldChange) > 1 or < −1, P < 0.05].
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Codon bias, nucleotide selection, and genome size predict in situ bacterial growth rate and transcription in rewetted soil. (PNAS 2025)

- DOI: 10.1073/pnas.2413032122 | PMCID: PMC11761963 | PMID: 39805015
- Evidence: Expression and normalization counts of mapped transcripts for each annotated gene (excluding rRNA genes) were generated using DESeq2 ( 75 ) using default parameters.
- Full pipeline: alignment/mapping [DESeq2, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [R v4.2.1, ggplot2, tidyverse] -> visualisation [R v4.2.1, ggplot2, tidyverse] -> stage not stated [NumPy, Python v3.8.2]

### Escalation of genome defense capacity enables control of an expanding meiotic driver. (PNAS 2025)

- DOI: 10.1073/pnas.2418541122 | PMCID: PMC11745323 | PMID: 39772737
- Evidence: Differential gene expression was analyzed using DESeq2 ( 55 ).
- Full pipeline: read trimming [Cutadapt] -> variant calling [kallisto] -> quantification [kallisto] -> differential/statistical testing [DESeq2]

### Mitochondrial DNA lineages determine tumor progression through T cell reactive oxygen signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2417252121 | PMCID: PMC11725793 | PMID: 39752523
- Evidence: Differentially expressed genes were identified using DESeq2 ( 57 ) with the betaPrior, cooksCutoff, and independentFiltering parameters set to False.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R] -> stage not stated [MACS2, pheatmap]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: Differentially expressed genes between WT and EndoG KO livers were identified using DESeq2, with the data normalized for library size.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### <i>Salmonella</i> infection accelerates postnatal maturation of the intestinal epithelium. (PNAS 2025)

- DOI: 10.1073/pnas.2403344122 | PMCID: PMC11725846 | PMID: 39793046
- Evidence: Differential gene expression was performed using DESeq2.
- Full pipeline: dimensionality reduction/clustering [GSEA] -> differential/statistical testing [DESeq2]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **1.35.0**
- Evidence: Differentially expressed genes within the harmonine pathway were analyzed using DESeq2 (version 1.35.0) ( 76 ) ( P < 0.01, |log 2 FoldChange| ≥ 1).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Evidence: Differential gene expression analysis was conducted by using the DESeq2 method with an FDR less than 0.05 as the significance cutoff ( 70 ).
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### A receptor kinase complex refines cambium activity in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2532481123 | PMCID: PMC13321232 | PMID: 42330278
- Version used: **1.40.2**
- Evidence: Read count per gene was analyzed using DESeq2(v 1.40.2) ( 45 ) to get P values, adjusted P values, and log2 fold changes.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [ggplot2 v3.4.4] -> stage not stated [pheatmap v1.0.12]

### Endothelial KLF4 depletion drives age-related neurovascular dysfunction and neuropsychiatric impairment. (PNAS 2026)

- DOI: 10.1073/pnas.2426990123 | PMCID: PMC13291589 | PMID: 42313933
- Evidence: Pink dots indicate significant (FDR < 0.001) differential peaks normalized to young WT Cre identified by DiffBind (DESeq2) (DA peaks).
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: Differential expression testing was performed with DESeq2 in R (design ∼ condition), with gene annotation via biomaRt.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### APOBEC2 deficiency disrupts hematopoietic lineage commitment, resulting in emergence of dual identity lymphocytes in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2531122123 | PMCID: PMC13250534 | PMID: 42247564
- Evidence: Differential gene expression analysis was performed using DESeq2 with thresholds of adjusted P -value ≤ 0.05 and |og2 fold change > 1.5.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, scDblFinder]

### Persistent trade-offs balance competition and colonization across centuries. (PNAS 2026)

- DOI: 10.1073/pnas.2534310123 | PMCID: PMC13250502 | PMID: 42228529
- Evidence: Fitness data were calculated and analyzed from these reads with the DESeq2 R package ( 40 ), and scripts can be found on our GitHub page.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [DESeq2, IQ-TREE v2.1.4, R, emmeans]

### Impact of sex chromosomes and gonad type in stress susceptibility in corticostriatal brain regions. (PNAS 2026)

- DOI: 10.1073/pnas.2531920123 | PMCID: PMC13229181 | PMID: 42189975
- Evidence: Differential expression was assessed using DESeq2 ( 74 ).
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.10.3, Metascape] -> stage not stated [Bioconductor, WGCNA]

### TGFb signaling instructs a conserved fibrosis-associated cell state marked by LRRC15. (PNAS 2026)

- DOI: 10.1073/pnas.2536550123 | PMCID: PMC13214008 | PMID: 42160341
- Version used: **1.40.2**
- Evidence: Normalized counts per million (CPM) values were computed as a measure of gene expression using the method in the DESeq2 v1.40.2 R package ( 45 , 46 ).
- Full pipeline: normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.56.1] -> simulation/modelling [Slingshot]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: All DEGs and DARs were identified using DESeq2 ( 67 ) version 1.36.0 with a design including the sample type and the replicate ID except for comparisons between timepoints where only timepoint was included in the design.
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Evidence: We used DESeq2(34)in R(89) to detect DEGs running comparisons 1) between herbivores and carnivores within each lake radiation for each tissue separately and 2) between oral and pharyngeal jaws within each radiation.
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: This count file was then processed using DESeq2 ( 63 ) to look for differentially expressed genes, with normalization performed for four replicates per condition, and conditions run pairwise looking for DE transcripts with an adjusted P -value below 0.05.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Functional dissection of &lt;i&gt;SPOP&lt;/i&gt; at the amino acid level reveals a comprehensive functional landscape of variants during tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523210123 | PMCID: PMC13167761 | PMID: 42090249
- Evidence: These matrices served as input for DESeq2 ( 45 ), and the enrichment ratio between SPOP -expressed and nonexpressed pools was calculated by adapting a pipeline from a previous study ( 46 ).
- Full pipeline: read trimming [Cutadapt, minimap2] -> alignment/mapping [STAR, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> visualisation [PyMOL] -> stage not stated [DESeq2, GATK, R]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Evidence: For downstream analyses, the raw counts were normalized using the “vst” function of the DESeq2 R package.
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### Simple biological controllers drive the evolution of soft modes. (PNAS 2026)

- DOI: 10.1073/pnas.2523032123 | PMCID: PMC13123806 | PMID: 42012951
- Evidence: To investigate the effect of knocking out a low dimensional controller, we analyze the processed data from the original study—DESeq2 had been used to generate normalized expression values ( 40 ), and then the log2 fold change of each gene in each sample with respect to wild type cells in YPD was calculated.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [Python]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Version used: **1.28.1**
- Evidence: Differential gene expression for the samples was explored using the R package (v1.16.1) and analyzed using DESeq2 (v1.28.1) ( Datasets S1 – S4 ).
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Version used: **1.36.1**
- Evidence: Read count normalization and differential expression analysis were performed using DESeq2 (v1.36.1) (DOI: 10.1186/s13059-01 4-0550-8 ), with the betaPrior parameter set to TRUE.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: For RNA-seq count matrices, raw count matrices were transformed using variance-stabilizing transformation (VST, as implemented in the DESeq2 package) ( 52 ), to obtain approximately log-scale, variance-stabilized expression values suitable for ssGSEA.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Evidence: Read counts were normalized across all samples using the counts function in DESeq2 package v.1.30.1 from Bioconductor ( 70 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Evidence: DE between conditions was assessed using DESeq2 ( 33 ) through Seurat’s FindMarkers interface.
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Functional role of small extrachromosomal circular DNA in colorectal cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523047123 | PMCID: PMC13056112 | PMID: 41926541
- Evidence: RNA expression was quantified using Kallisto v0.50.1 with differential expression analysis by DESeq2.
- Full pipeline: quantification [DESeq2, kallisto v0.50.1] -> differential/statistical testing [DESeq2, kallisto v0.50.1] -> stage not stated [CNVkit v0.9.9, Python, R v4.1]

### Versatile SMAD2 and SMAD3 epitope-tagged mouse models for genomic profiling of TGFβ signaling: Uncovering GDF9-SMAD2/3 targets. (PNAS 2026)

- DOI: 10.1073/pnas.2600071123 | PMCID: PMC13056123 | PMID: 41911462
- Version used: **1.48.2**
- Evidence: Count matrices were analyzed in R with DESeq2 v1.48.2 ( 93 ).
- Full pipeline: quality control [Bowtie2] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2, STAR v2.7.11b, featureCounts v2.1.1] -> quantification [STAR v2.7.11b] -> stage not stated [DESeq2 v1.48.2, HOMER v4.11, deepTools v2.4.2]

### Fibro-adipogenic progenitor cells from murine SMA muscles are intrinsically adipogenic. (PNAS 2026)

- DOI: 10.1073/pnas.2525423123 | PMCID: PMC13037897 | PMID: 41886383
- Evidence: Differential gene expression was analyzed using DESeq2-R baseline pipeline on R.
- Full pipeline: quality control [featureCounts] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ, fastp]

### Immune cell profiling reveals expanded stem cell-like memory T cells in anti-GAD65-associated neurological syndromes. (PNAS 2026)

- DOI: 10.1073/pnas.2514753123 | PMCID: PMC13038060 | PMID: 41880578
- Evidence: Pseudobulking was performed and the differential expression was tested with DESeq2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v5.0.1]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Evidence: Differential gene expression was calculated using DESeq2 ( 45 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **1.40.2**
- Evidence: Differential expression analysis of oyster transcripts was conducted using the DESeq2 v.1.40.2 R package.
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### Med14 phosphorylation shapes genomic response to GLP-1 agonists. (PNAS 2026)

- DOI: 10.1073/pnas.2536772123 | PMCID: PMC12974444 | PMID: 41779793
- Evidence: Significance of differential gene expression in bulk RNA-seq was determined by DESeq2 on duplicates.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, Trim Galore] -> quantification [HOMER] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2]

### Differential disease tolerance mediates sex-biased illness severity in sepsis. (PNAS 2026)

- DOI: 10.1073/pnas.2522764123 | PMCID: PMC12956862 | PMID: 41734079
- Version used: **1.48.1**
- Evidence: Differential gene expression analysis was performed using DESeq2 (v1.48.1).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [GSEA, MACS2, R v4.5.0, fgsea v1.34.0]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: DEGs were identified by using DESeq2 ( 54 ) with cutoff of Log 2 (Fold change) ≥ 0.5, P adj ≤ 0.05 for all the samples.
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Mfsd2a is important for maintaining epidermal homeostasis. (PNAS 2026)

- DOI: 10.1073/pnas.2531159123 | PMCID: PMC12933103 | PMID: 41712644
- Evidence: DESeq2 normalized counts available in Dataset S1 .
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.4] -> visualisation [UMAP]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Evidence: Differential expression was analyzed using DESeq2 R package v1.32.0 ( 62 ).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### Foliar dewdroplet-induced redox cascades promote early flowering in &lt;i&gt;Brassicaceae&lt;/i&gt; plants. (PNAS 2026)

- DOI: 10.1073/pnas.2527021123 | PMCID: PMC12933091 | PMID: 41701847
- Evidence: Data were processed using FastQC, Bowtie2, MACS2, and DESeq2.
- Full pipeline: quality control [Bowtie2, DESeq2, FastQC, MACS2] -> stage not stated [WGCNA]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Normalized gene expression values were calculated and expressed as VST from “DESeq2” ( 45 ) package. consensusClusteringPlus ( 46 ) was used to cluster the samples.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### REV-ERB-alpha and -beta coordinately regulate astrocyte reactivity and proteostatic function. (PNAS 2026)

- DOI: 10.1073/pnas.2511093123 | PMCID: PMC12867698 | PMID: 41615759
- Evidence: DESeq2 package in R was utilized to obtain DEG lists after accounting for multiple comparison with normalized log 2 fold change and adjusted P values (q value) to account for multiple comparisons.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, ImageJ, R]

### Intronic polyadenylation-derived long noncoding RNA modulates nucleolar integrity and function. (PNAS 2026)

- DOI: 10.1073/pnas.2514521123 | PMCID: PMC12867753 | PMID: 41615750
- Evidence: RNA-seq data were processed, and differential gene expression analysis was performed using DESeq2 ( Fig.
- Full pipeline: differential/statistical testing [DESeq2]

### Germline fate determination by a single ARGONAUTE protein in &lt;i&gt;Ectocarpus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518712123 | PMCID: PMC12867755 | PMID: 41604268
- Evidence: Pairwise differential expression between the mutants was obtained using raw read count matrices as input for the DESeq2 package ( 93 ) in R v.4.3.1.
- Full pipeline: quality control [Trimmomatic] -> read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT, STAR, featureCounts] -> quantification [DESeq2, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Lack of synergy between AR-targeted therapies and PARP inhibitors in homologous recombination-proficient prostate cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2515790122 | PMCID: PMC12867744 | PMID: 41591905
- Evidence: The VIPER pipeline ( 50 ) was used for STAR alignment to the hg19 genome ( 51 ), read count normalization using Cufflinks ( 52 ) quality control with RSeQC ( 53 ), and differential expression analysis using DESeq2 ( 54 ).
- Full pipeline: quality control [Cufflinks, DESeq2, STAR] -> alignment/mapping [Cufflinks, DESeq2, STAR] -> quantification [CellProfiler, Cufflinks, DESeq2, STAR] -> normalisation [Cufflinks, DESeq2, STAR] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [Cufflinks, DESeq2, STAR]

### A bacterial translation activator with an intrinsically disordered RNA-binding region. (PNAS 2026)

- DOI: 10.1073/pnas.2519770123 | PMCID: PMC12818456 | PMID: 41543904
- Evidence: To assess the relative abundance of RNAs copurifying with PhaF in our CLIP/CLAP-seq experiment or to assess the relative abundance of RNAs obtained from total RNA samples, the libraries were mapped to the PAO1 genome using bowtie2, counted with htseq-count ( 61 ), and analyzed with DESeq2 in R ( 62 ). β-Galactosidase Assays.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, HTSeq, R] -> quantification [Bowtie2, DESeq2, HTSeq, R] -> stage not stated [Cutadapt v2.10]

### Early life-stage thermal resilience is determined by climate-linked regulatory variation. (PNAS 2026)

- DOI: 10.1073/pnas.2518358123 | PMCID: PMC12799179 | PMID: 41505517
- Evidence: 4.2.3) and the package “DESeq2” (v.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Salmon v0.14.1] -> quantification [Salmon v0.14.1] -> stage not stated [DESeq2, R, SAMtools v1.10]

### Gene duplication, horizontal gene transfer, and trait trade-offs drive evolution of postfire resource acquisition in pyrophilous fungi. (PNAS 2026)

- DOI: 10.1073/pnas.2519152123 | PMCID: PMC12773724 | PMID: 41481463
- Evidence: Differential transcription analysis was performed using DESeq2 ( 67 ), with all time points compared against the 0 h for the calculation of fold change in transcription.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [HISAT2 v2.2.1, HMMER v3.4] -> quantification [ImageJ v1.54, R] -> differential/statistical testing [DESeq2, R] -> visualisation [phytools] -> stage not stated [BUSCO, Flye v2.9, InterProScan v5.62, QUAST]

### Host-microbiome mutualism drives urea carbon salvage and acetogenesis during hibernation. (PNAS 2026)

- DOI: 10.1073/pnas.2518978123 | PMCID: PMC12773770 | PMID: 41481471
- Evidence: Overrepresented CAZymes were identified with DESeq2 ( 22 ) and normalized counts were transformed using the Hellinger method ( hellinger , labdsv package in R).
- Full pipeline: read trimming [Bowtie2 v2.2.2, Trimmomatic v0.38] -> normalisation [DESeq2, R] -> differential/statistical testing [R] -> stage not stated [HMMER]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Version used: **1.46.0**
- Evidence: The Bioconductor R package DESeq2 (v.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: Read normalization and exploratory analyses were carried out using the DESeq2 package ( 73 ).
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: First, we performed library size correction and variance stabilization transformation implemented in DESeq2.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Cortical wiring by synapse type-specific control of local protein synthesis. (Science 2022)

- DOI: 10.1126/science.abm7466 | PMCID: PMC7618116 | PMID: 36423280
- Evidence: Differential gene expression was performed using DESeq2 on R, and candidate targets were selected using the SynGO tool and ranked for validation using a set of criteria that included expression and enrichment in MGE-derived interneurons.
- Full pipeline: quality control [FastQC, Picard, SAMtools] -> alignment/mapping [STAR v2.4.0] -> quantification [R v3.2] -> normalisation [R v3.2] -> differential/statistical testing [DESeq2, R v3.2] -> stage not stated [ImageJ]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Evidence: DEGs were determined using the DESeq function (adjusted P < 0.05, fold change > 2) in the DESeq2 R package ( 49 ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Sex-biased gene expression across mammalian organ development and evolution. (Science 2023)

- DOI: 10.1126/science.adf1046 | PMCID: PMC7615307 | PMID: 37917687
- Evidence: We used four time series differential expression algorithms to identify sex-biased genes across organ development: splineTimeR ( 82 ), DESeq2 ( 29 ), MaSigPro ( 83 ), and our own algorithm ( 22 ).
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Evidence: To identify differential expression raw gene level counts were imported into DESeq2 ( 72 ).
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: The gene-level feature counts were then normalized and log 2 -transformed with DESeq2, to obtain gene expression values for all genes and all samples.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Somatic mosaicism in schizophrenia brains reveals prenatal mutational processes. (Science 2024)

- DOI: 10.1126/science.adq1456 | PMCID: PMC11490355 | PMID: 39388546
- Evidence: Oligos with at least 10 barcodes were retained for analysis and oligo counts were normalized for sequencing depth with the DESeq2 median of ratios method.
- Full pipeline: alignment/mapping [GATK] -> normalisation [DESeq2] -> stage not stated [PLINK, R]

### A kalihinol analog disrupts apicoplast function and vesicular trafficking in &lt;i&gt;P. falciparum&lt;/i&gt; malaria. (Science 2024)

- DOI: 10.1126/science.adm7966 | PMCID: PMC11793105 | PMID: 39325875
- Evidence: RNA-seq Differential expression analysis was done by use of R package DESeq2 with an adjusted P -value cutoff of 0.05.
- Full pipeline: differential/statistical testing [DESeq2, R] -> stage not stated [AlphaFold, ChimeraX]

### Transcripts of repetitive DNA elements signal to block phagocytosis of hematopoietic stem cells. (Science 2024)

- DOI: 10.1126/science.adn1629 | PMCID: PMC12012832 | PMID: 39264994
- Evidence: To identify differentially expressed REs, DESeq2 R package ( 43 ). mRNA synthesis and CD34 overexpression For the overexpression of human Erv the respective cDNA was amplified from CD34 cells with PCR and cloned into pJET1.2/ blunt cloning vector (CloneJET PCR Cloning Kit, Thermoscientific, K1232).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [CellProfiler, Metascape, R]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Evidence: We then counted how many reads overlapped an annotated gene (GENECODE v32 annotations) using HTSeq (v2.0.2) ( 122 ) (htseq-count –stranded=reverse –order=name -f bam –additional-attr=gene_name -m union), and used the output counts files to find DEGs with DESeq2 ( 123 ), run with default parameters within the Galaxy platform ( 124 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Evidence: Length-scaled abundance estimates were size-factor normalised by the median ratio method and modelled as a response to CF proportion per genomic cluster (as defined by the number of CF vs non-CF patients and environmental samples) using a negative binomial generalised linear model (GLM) with DESeq2 ( 78 ).
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Evidence: Differential expression analysis was carried out using DESeq2 ( 112 ) using default parameters.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Version used: **1.18.1**
- Evidence: Sequence data were trimmed to remove adaptors and sequences with a quality score below 30 using Trim Galore (version 0.50, Babraham Bioinformatics) and then aligned to the mouse genome (GRCm38) using STAR (version 2.6.0a), and differential expression was calculated using DESeq2 (version 1.18.1) ( 77 ).
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Evidence: Statistical analyses for differentially expressed genes were performed by tximport and DESeq2 ( 95 ).
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

### Silencing mitochondrial gene expression in living cells. (Science 2025)

- DOI: 10.1126/science.adr3498 | PMCID: PMC7618265 | PMID: 40403134
- Version used: **1.40.2**
- Evidence: Differential gene expression analysis was conducted using DESeq2 (version 1.40.2) ( 44 ).
- Full pipeline: quantification [ImageJ v1.47] -> normalisation [limma v3.56.2] -> dimensionality reduction/clustering [clusterProfiler v4.8.3, limma v3.56.2] -> differential/statistical testing [DESeq2 v1.40.2, ImageJ v1.47, limma v3.56.2] -> stage not stated [Bioconductor, R v4.3.0, ggplot2]

### Identification of antigen-presenting cell-T cell interactions driving immune responses to food. (Science 2025)

- DOI: 10.1126/science.ado5088 | PMCID: PMC12017586 | PMID: 39700315
- Evidence: Next, the count matrix was imported to the R environment and processed by the DESeq2 package (v.
- Full pipeline: alignment/mapping [RSEM v1.3.1, STAR] -> stage not stated [DESeq2, MACS2, R, Seurat v4.1.2]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Version used: **1.34**
- Evidence: The read counts were processed in R using the DESeq2 (v1.34) package.
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: Differential expression (DE) analysis was conducted with the DESeq2 package in R.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Differential accessibility analysis was performed using the DESeq2 R package (v1.42.1) ( 81 ).
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Version used: **1.42.1**
- Evidence: Differential gene expression analysis was conducted by iterating through each condition and using DESeq2 (1.42.1) to compare gene expression to that of mCherry-expressing control samples.
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Version used: **1.38.3**
- Evidence: Differentially expressed ILF3 binding in rescued Actg1 -NSD MEFs vs WT was identified using DESeq2 v.1.38.3 as described in https://support.bioconductor.org/p/61509/ in order to identify enrichments after normalizing IP signal to input.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### Blocking RAN translation without altering repeat RNAs rescues &lt;i&gt;C9ORF72&lt;/i&gt;-related ALS and FTD phenotypes. (Science 2026)

- DOI: 10.1126/science.adv2600 | PMCID: PMC13107528 | PMID: 41643021
- Evidence: The raw counts were subjected to differential gene expression using the DESeq2 package in R (version 4.2.1) ( 109 ).
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> quantification [CellProfiler, Fiji, ImageJ] -> differential/statistical testing [DESeq2, R v4.2.1]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: We aggregated gene expression counts across all cells in each sample and determined differential expression between developmental stages (E14 vs P4) using DESeq2 ( 107 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Version used: **1.34.0**
- Evidence: Transcript abundance estimates were imported into R for differential expression analysis using DESeq2 (v1.34.0).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

