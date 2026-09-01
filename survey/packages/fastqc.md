# FastQC

- **Category:** genomics
- **Papers in survey:** 322
- **Journals:** PNAS (173), Nature (113), Cell (25), Science (11)
- **Years:** 2021 (32), 2022 (44), 2023 (54), 2024 (59), 2025 (93), 2026 (40)
- **Versions named:** 0.11.9 (52), 0.11.8 (27), 0.11.5 (21), 0.12.1 (12), 0.11.7 (10), 0.11.4 (5), 0.11.2 (4), 0.11.6 (2), 0.11.3 (2), 0.73 (1)
- **Pipeline stages it appears in:** quality control (322), read trimming (107), alignment/mapping (55), differential/statistical testing (12), quantification (9), normalisation (3), visualisation (3), structure determination (2), dimensionality reduction/clustering (2), registration (1)

## Papers

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Evidence: PolyA site usage analysis The quality of the sequenced reads were checked with FastQC and Illumina adapters and low quality positions (Phred score < 10) trimmed using Cutadapt.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: ...on 4.0.1 10X Genomics RRID: SCR_017344 DESeq2 package version 2.3.11 https://bioconductor.org/packages/release/bioc/html/DESeq2.html RRID: SCR_015687 FastQC software package version 0.11.5 Babraham Bioinformatics RRID: SCR_014583 Fiji image processing package Schindelin et al., 2012 RRID: SCR_003070 FlowJo software version 10.6.1 Treestar RRID: SCR_008520 HOMER software version 4.11 http://homer.u...
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### An early cell shape transition drives evolutionary expansion of the human forebrain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.050 | PMCID: PMC8054913 | PMID: 33765444
- Evidence: ...r/TrimGalore/releases Cutadapt v2.4 Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ FASTQC v0.11.5 Andrews, 2010 https://github.com/s-andrews/FastQC HISAT2 v2.0.0-beta Kim et al., 2015 http://daehwankimlab.github.io/hisat2/ HTSeq v0.11.2 Anders et al., 2015 https://htseq.readthedocs.io/en/master/ g:Profiler Reimand et al., 2007 https://biit.cs.ut.ee/gprofiler/gost TCseq Wu and Gu, 2020 htt...
- Full pipeline: quality control [Cutadapt v2.4, FastQC, HISAT2 v2.0.0, HTSeq v0.11.2, Trim Galore] -> stage not stated [R v3.5]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...630 Software and algorithms OxCal Ramsey and Lee, 2013 https://c14.arch.ox.ac.uk/oxcal.html CutAdapt Martin, 2011 https://github.com/marcelm/cutadapt FastQC Andrews, 2010 https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ BWA Li and Durbin, 2010 http://bio-bwa.sourceforge.net/ Picard MarkDuplicates http://broadinstitute.github.io/picard http://broadinstitute.github.io/picard MapDamage2.0 J...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Evidence: ...id ( Carnell et al., 2015 ) p8.91 Software and algorithms Prism 8 GraphPad https://www.graphpad.com/ FlowJo 10.5.3 FlowJo, LLC https://www.flowjo.com FastQC Babraham Institute https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ MultiQC 1.9 MultiQC https://multiqc.info/ Trimmomatic 0.39 USADELLAB http://www.usadellab.org/cms/?page=trimmomatic MiXCR MI Lanoratory https://mixcr.readthedocs.io/...
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Version used: **0.11.5**
- Evidence: Quality control metrics were produced with picard tools (v1.107), FastQC (v0.11.5 - http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and GATK(v3.9).
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: Raw sequence reads were quality checked using FastQC software ( Andrews, 2010 ).
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Evidence: Bulk RNA-Seq analysis The quality of reads was evaluated using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **0.11.3**
- Evidence: (2016) https://alkesgroup.broadinstitute.org/Eagle/ FastQC v0.11.3 https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ GATK v3.5 and v4.1 Van der Auwera and O'Connor (2020) https://gatk.broadinstitute.org/hc/en-us GATK-SV Collins et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ..., 2015 ) v1.15.1 R (statistics) https://www.r-project.org/ v4.1.0 BBmap (BBtools) ( Bushnell et al., 2017 ) v38.90 HISAT2 ( Kim et al., 2015 ) v2.1.0 FastQC https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ v0.11.9 FeatureCounts ( Liao et al., 2014 ) v2.0.1 Astra Wyatt Technology v8.0 Compass Bruker Daltonics v1.2 TopSpin Bruker BioSpin GmbH V4.1.3 Resource availability Lead contact Furth...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: .../strimmerlab.github.io eXploring Genomic Relations (XGR) ( Fang et al., 2016b ) http://galahad.well.ox.ac.uk/XGR Fastcluster ( Mulner, 2013 ) v1.1.25 FastQC ( Andrews, 2010 ) v0.11.9 https://github.com/s-andrews/FastQC featureCounts ( Liao et al., 2014 ) v1.6.4 fgsea ( Korotkevich et al., 2021 ) https://bioconductor.org/packages/release/bioc/html/fgsea.html FlowJo BD Biosciences v10.6 https://www....
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...raphpad.com/scientific-software/prism version 8.2.1 R R Core Team and R Foundation for Statistical Computing, https://www.r-project.org version 3.5.3 FastQC Babraham Bioinformatics, https://www.bioinformatics.babraham.ac.uk version 0.11.9 Samtools Genome Research Limited, http://www.htslib.org version 1.14 MACS2 https://github.com/macs3-project/MACS version 2.1.1.20160309 Recombinant Identificatio...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Mechanopathology of biofilm-like Mycobacterium tuberculosis cords. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.016 | PMCID: PMC10642369 | PMID: 37865090
- Evidence: ...o, Broad Institute RRID: SCR_003199 R Project for Scientific Computing Free Software Foundation RRID: SCR_001905 Star PMID: 23104886 RRID: SCR_004463 FastQC Baraham Institute RRID: SCR_014583 Bioconductor Roswell Park Comprehensive Cancer Center RRID: SCR_006442 Other NalgeneTM square PETG media bottles with closure ThermoFisher Cat#: 2019-0030 Lung-on-chip Emulate Cat#: Chip-S1 Chip Coating Reage...
- Full pipeline: quality control [Bioconductor, FastQC, GSEA, STAR v2.7.10b] -> alignment/mapping [STAR v2.7.10b] -> quantification [R, edgeR] -> stage not stated [ImageJ, MACS2]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: After quality control with FastQC, reads were aligned using rnaSTAR65 to the GRCm38 (mm10) genome with ERCC synthetic RNA added.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **0.11.9**
- Evidence: The quality of the reads from the RNA sequencing was analysed with FastQC v0.11.9, 99 and visualized using MultiQC v1.9.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Evidence: The RNA-seq FASTQ files were first inspected with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to ensure that the raw data were of high quality.
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **0.11.9**
- Evidence: 102 https://bioconductor.org/packages/release/bioc/html/DESeq2.html FastQC v0.11.9 Andrew 103 http://www.bioinformatics.babraham.ac.uk/projects/fastqc MultiQC v1.8 Ewels et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Evidence: We downloaded the raw sequence files from the Gene Expression Omnibus (GEO) with the SRA toolkit (fastq-dump), assessed their quality with FastQC (Babraham Bioinformatics), and removed low-quality reads and bases with Trimmomatic v.0.33 116 .
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Version used: **0.11.9**
- Evidence: ...Foundation for Statistical Computing, https://www.r-project.org version 4.1.1 RepeatMasker Institute for Systems Biology http://www.repeatmasker.org/ FastQC (v0.11.9) Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk bwa-mem Li and Durbin 93 http://maq.sourceforge.net/ Ensembl (V109) Ensembl www.ensembl.org UCSC Genome Browser UCSC www.genome.ucsc.edu GENCODE (V43) GENCODE www.genc...
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Version used: **0.11.9**
- Evidence: 119 RRID: SCR_003070 https://imagej.nih.gov/ij/ Measure Rosette Area Tool (ImageJ macro) Remote-ImageJ project http://dev.mri.cnrs.fr/projects/remote-imagej/files FastQC v0.11.9 Babraham Institute (UK) www.bioinformatics.babraham.ac.uk/projects/fastqc HISAT2 v2.1.0 Kim et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: RNA-seq analysis Quality control of RNA-Seq datasets was performed by FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and Cutadap 52 to remove adaptor sequences and low-quality regions.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Evidence: The code uses FastQC version v0.11.8 129 for sequence quality control before and after adaptor removal, cutadapt 130 version 3.5 with Python 3.7.12 for adaptor removal, SAMtools 131 version 1.9 for indexing, bwa 132 version 0.7.17-r1188 for mapping.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### RNA Pol II inhibition activates cell death independently from the loss of transcription. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.034 | PMCID: PMC12406974 | PMID: 40818455
- Evidence: QUANTIFICATION AND STATISTICAL ANALYSIS RNA sequencing analysis Quality control for the RNAseq datasets were performed using FastQC.
- Full pipeline: quality control [FastQC] -> quantification [FastQC, kallisto] -> normalisation [DESeq2] -> differential/statistical testing [FastQC] -> stage not stated [GSEA]

### The essential host genome for Cryptosporidium survival exposes metabolic dependencies that can be leveraged for treatment. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.001 | PMCID: PMC7618951 | PMID: 40706591
- Evidence: ...geJ v2.1.0/1.53c ImageJ https://imagej.net/ PRISM V10.2.3 GraphPad https://www.graphpad.com/features R v.4.4.1 R Core Team https://www.r-project.org/ FastQC V0.11.7 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ kallisto V0.45.0 Bray et al.
- Full pipeline: quality control [FastQC, ImageJ v2.1.0, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [PHENIX, STRING db v12.0]

### Global genetic interaction network of a human cell maps conserved principles and informs functional interpretation of gene co-essentiality profiles. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.044 | PMCID: PMC13281610 | PMID: 42049019
- Version used: **0.11.9**
- Evidence: After checking the sequencing quality with FastQC (v.0.11.9), reads were aligned to human genome build hg38 with Gencode v32 gene annotations using the STAR short-read aligner (v.2.7.9a) using the following parameters: –outSAMtype BAM SortedByCoordinate –quantMode GeneCounts –sjdbGTFfile gencode.v25.annotation.gtf.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, STAR] -> variant calling [GATK] -> visualisation [Cytoscape] -> stage not stated [ANNOVAR, R, SciPy]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Version used: **0.11.9**
- Evidence: KIN-CLIP read processing, refinement and mapping Raw sequencing reads were assessed for quality (FastQC 0.11.9, https://www.bioinformatics.babraham.ac.uk ) and de-multiplexed.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Version used: **0.10.0**
- Evidence: Quality control of sequence reads We assessed sequence quality of the paired-end reads with FastQC (v0.10.0, http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) for each of 16 whole-genome samples (WGS).
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: Quality of sequencing reads was assessed using FastQC (Babraham Bioinformatics) and aligned to a reference genome (hg19, UCSC Genome Browser) using TopHat.
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Arterialization requires the timely suppression of cell growth. (Nature 2021)

- DOI: 10.1038/s41586-020-3018-x | PMCID: PMC7116692 | PMID: 33299176
- Version used: **0.11.5**
- Evidence: Sequencing reads were processed with a pipeline that used FastQC v0.11.5 (Babraham Bioinformatics, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to evaluate their quality, and cutadapt 35 to trim sequencing reads, thus eliminating Illumina and SMARTer adaptor remains, and discard reads shorter than 30 bp.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5] -> alignment/mapping [RSEM v1.2.30] -> normalisation [limma v3.32.10] -> differential/statistical testing [limma v3.32.10] -> stage not stated [GSEA, ImageJ]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: First, FASTQ files were assessed with FastQC 46 (v0.11.2) to verify that quality was sufficient for further processing.
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: Processing of RNA-seq After initial quality control with FastQC ( https://github.com/s-andrews/FastQC ) and default adapter trimming with Skewer 62 , paired-end reads were aligned to the GRCh38 reference genome and v28 of the Gencode GTF annotation using the STAR two-pass method 108 .
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: The sequenced libraries were quality-inspected using the FastQC tool v0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and de-multiplexed using the Pheniqs tool from biosails v2.1.0.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: In brief, the steps run were quality control of the FASTQ files using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), alignment of short reads to the human reference genome sequence (GRCh38/hg38) using bwa-mem with the ALT-aware option turned on 40 , sorting of reads and marking of PCR duplicates with GATK MarkDuplicates and base quality score recalibration and joint realign...
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Version used: **0.11.5**
- Evidence: FastQC v.0.11.5 and MultiQC v.1.8 were used to confirm the quality of the sequenced libraries 42 , 43 .
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Version used: **0.11.8**
- Evidence: The quality of the resulting data was assessed using FastQC v0.11.8 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), and reads were subsequently quality and adaptor trimmed using cutadapt (v3.4) 50 with stringent settings to remove error-containing reads (‘-q 20 --max-n 0 --max-ee 1’).
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### CCNE1 amplification is synthetic lethal with PKMYT1 kinase inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-04638-9 | PMCID: PMC9046089 | PMID: 35444283
- Version used: **0.11.9**
- Evidence: Raw FASTQ files from a paired-end library were assessed using the FastQC v0.11.9 software ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to determine the quality of the reads; read length was 150 bp.
- Full pipeline: quality control [FastQC v0.11.9] -> stage not stated [GSEA, ImageJ v2.0.0, edgeR v3.30.3]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Version used: **0.11.9**
- Evidence: The quality of the resulting files was evaluated using FastQC (v0.11.9).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **0.11.8**
- Evidence: Read statistics were estimated using FastQC (v.0.11.8).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: TRINITY was used for de novo assembly and the Iterative Refinement Meta-Assembler (IRMA) was used for genome assisted assembly as well as FastQC for quality checks.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Demultiplexing was performed using bcl2fastq2 v.2.17 software (Illumina) using default options. sWGS and WES pre-processing For each exome paired FASTQ file, sequencing quality metrics were generated using the FastQC tool (version 0.11.7) ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: Bioinformatics data processing and analyses were performed using Bash (v4.2.46), R (v3.6) and Python (v3.8.5) programming languages as well as the following tools: FastQC (Babraham Bioinformatics) (v0.11.7) cutadapt 37 (v1.16), HISAT2 38 (v2.1.0), SAMtools 39 (v1.9), sambamba 40 (v0.6.6) and deepTools 41 (v3.1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: CUT&RUN sequencing read alignments, quality control and peak calling To process the CUT&RUN reads, we first performed quality control using FastQC to assess read quality ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Bacteriophages suppress CRISPR-Cas immunity using RNA-based anti-CRISPRs. (Nature 2023)

- DOI: 10.1038/s41586-023-06612-5 | PMCID: PMC10651486 | PMID: 37853129
- Version used: **0.11.9**
- Evidence: The quality of the reads was assessed using FastQC v.0.11.9 (ref.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2, MAFFT, SAMtools v1.16.1]

### Apoptotic stress causes mtDNA release during senescence and drives the SASP. (Nature 2023)

- DOI: 10.1038/s41586-023-06621-4 | PMCID: PMC10584674 | PMID: 37821702
- Evidence: RNA-seq paired-end reads were assessed for quality using the FastQC algorithm, then aligned to the human genome using the splice-aware aligner STAR with a two-pass alignment pipeline.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [Cufflinks, FastQC, STAR] -> quantification [Cufflinks, DESeq2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **0.11.7**
- Evidence: Pre-trimming and post-trimming quality control was done using FastQC (v.0.11.7).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Inhibition of fatty acid oxidation enables heart regeneration in adult mice. (Nature 2023)

- DOI: 10.1038/s41586-023-06585-5 | PMCID: PMC10584682 | PMID: 37758950
- Version used: **0.11.8**
- Evidence: Raw reads were assessed for quality, adapter content and duplication rates with FastQC 0.11.8 ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [FastQC v0.11.8, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Version used: **0.11.9**
- Evidence: Data quality was assessed with FastQC v.0.11.9 ( https://github.com/s-andrews/FastQC ) and MultiQC v.1.9 ( https://multiqc.info/ ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Evidence: Specifically, raw reads were trimmed using Trim Galore v.0.6.6, a wrapper tool of Cutadapt 53 and FastQC 54 .
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Version used: **0.11.9**
- Evidence: Fastq files were assessed using FastQC (v.0.11.9) and Illumina sequencing adapters were trimmed from reads using cutadapt (v.1.18).
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Evidence: Read mapping, quantification and normalization RNA-seq reads were inspected using the FastQC tool for quality control.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Version used: **0.11.7**
- Evidence: The quality of the raw sequencing reads was first confirmed with FastQC v0.11.7 (ref.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### Microbial peptides activate tumour-infiltrating lymphocytes in glioblastoma. (Nature 2023)

- DOI: 10.1038/s41586-023-06081-w | PMCID: PMC10208956 | PMID: 37198490
- Version used: **0.11.8**
- Evidence: Reads were demultiplexed by separating reads into individual FastQ files, quality controlled and trimmed of Illumina adaptor sequences using locus-specific bcl2fastq software version v2.20.0.422, FastQC version 0.11.8 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and cutadapt v3.2 ( http://journal.embnet.org/index.php/embnetjournal/article/view/200 ), respectively.
- Full pipeline: quality control [Cutadapt v3.2, FastQC v0.11.8] -> read trimming [Cutadapt v3.2, FastQC v0.11.8]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **0.11.2**
- Evidence: FastQC (v.0.11.2) 51 was used for quality control, and Trim Galore!
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Version used: **0.11.8**
- Evidence: Alignment Initial quality control of raw paired-end reads (100 bp) was performed using FastQC (v.0.11.8, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and FastQ Screen (v.0.13.0, https://www.bioinformatics.babraham.ac.uk/projects/fastq_screen/ , flags: --subset 100000; --aligner bowtie2).
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: We first processed the pair-end reads (average sequence coverage per genome = 5×), quality checking using FastQC 53 , with barcode and adaptor sequence trimmed by TrimGalore (phred-score = 20).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Version used: **0.11.8**
- Evidence: ChIP–seq data analysis The sequenced reads were demultiplexed using bcl2fastq (v.2.19.0.316), and basic quality control was performed on the resulting FASTQ files using FastQC (v.0.11.8).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **0.11.8**
- Evidence: Read quality was assessed using FastQC (v.0.11.8) 59 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: Reads were quality-checked with FastQC.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Version used: **0.11.9**
- Evidence: TRAP–seq Quality control of the raw reads was performed using FastQC v.0.11.9.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### The rise and transformation of Bronze Age pastoralists in the Caucasus. (Nature 2024)

- DOI: 10.1038/s41586-024-08113-5 | PMCID: PMC11602729 | PMID: 39478221
- Evidence: Raw FastQC files were processed through the EAGER pipeline 63 , for assessment of human DNA content and DNA damage profiles.
- Full pipeline: quality control [ANGSD, FastQC] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Version used: **0.11.9**
- Evidence: RNA-sequencing data analysis Sequence read quality was assessed using FastQC (v0.11.9; http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **0.11.8**
- Evidence: Bulk RNA-seq data processing and analysis FastQC (v.0.11.8, RRID: SCR_014583 ) was used for quality control.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Version used: **0.11.5**
- Evidence: Raw data quality was assessed using FastQC v0.11.5 and raw data were imported in QIIME2 v2020.8 for downstream analysis 28 .
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Analysis Reads were demultiplexed with Bcl2fastq v.2.20.0.422 (Illumina) and quality-checked with FastQC 89 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) was used to validate proper trimming and check overall sequence data quality.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Quality control of the paired-end bulk RNA-seq data was performed using the FastQC program.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Lanes were merged and the quality of sequencing data was evaluated with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Data were demultiplexed and converted to FASTQ files using bcl2fastq and preprocessed as previously described using FastQC 60 .
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Selective haematological cancer eradication with preserved haematopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07456-3 | PMCID: PMC11186773 | PMID: 38778101
- Evidence: After demultiplexing, each sample was assessed for quality using FastQC 52 and processed using the CRISPResso2 tool 53 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> quantification [R]

### Adhesive anti-fibrotic interfaces on diverse organs. (Nature 2024)

- DOI: 10.1038/s41586-024-07426-9 | PMCID: PMC11168934 | PMID: 38778109
- Evidence: Read quality was evaluated using FastQC, and data were pre-processed with Cutadapt 35 for adaptor removal following best practices 36 .
- Full pipeline: quality control [Cutadapt, FastQC] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ v2.1.0]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: In brief, we performed quality control of the fastq files using FastQC and trimmed the filtered reads with Trim Galore software.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Version used: **0.11.6**
- Evidence: Quality control was assessed using FastQC v0.11.6 and RNA-SeQC v1.1.8 49 .
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: The resulting reads were assessed for quality using FastQC ( https://github.com/s-andrews/FastQC ), trimmed with Sickle (v.1.33; https://github.com/najoshi/sickle ) to remove low-quality 5′- and 3′-end bases, and trimmed using Cutadapt 71 (v.1.18) to remove adapters.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: For read alignment and generation of digital expression data, raw sequencing data were inspected using FastQC and multiQC 71 , 72 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Evidence: Bulk RNA-seq Read quality was assessed using FastQC 46 (v0.10.1) to identify sequencing cycles with low average quality, adapter contamination, or repetitive sequences from PCR amplification.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Quality control of sequenced reads was performed by FastQC.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **0.11.9**
- Evidence: After processing the de-multiplexed sequencing reads, sample sequencing quality was analysed with FastQC version 0.11.9 83 , filtering reads with a QC value < 25.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: Pre- and post-trimmed sequence quality and adapter contamination were assessed using FastQC 59 (v.0.11.7).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: The quality of the raw sequencing reads was assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and MultiQC.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **0.11.9**
- Evidence: ...jects/trim_galore/ v.0.6.4, a wrapper program implementing Cutadapt v.2.9 ( https://journal.embnet.org/index.php/embnetjournal/article/view/200 ) and FastQC v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and mapped to the human genome (hg38) using the HISAT2 package (v.2.2.0) (ref.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **0.11.9**
- Evidence: Sequencing FastQ files were applied to FastQC (v.0.11.9; https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) for quality control, adapters were trimmed by Trimmomatic (v.0.39) 73 , and the genomic fragments were aligned to the human, mouse and whale genome reference (hg19, mm10 and the published bowhead whale genome assembly 13 ) using Burrows–Wheeler Aligner (BWA, v.0.7.19) 74 , then sor...
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: Quality control Quality control was conducted using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), DESeq2 (ref.
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Version used: **0.11.8**
- Evidence: Bioinformatics analysis for NGS datasets Read processing Sequencing reads were assessed for quality using FastQC (v.0.11.8) 55 and MultiQC (v.0.92) 56 to ensure the general quality of the datasets.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### Maternal stress triggers early-life eczema through fetal mast cell programming. (Nature 2025)

- DOI: 10.1038/s41586-025-09419-8 | PMCID: PMC12488486 | PMID: 40866704
- Evidence: FastQC was performed on sequence reads to evaluate the sequencing quality.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2 v1.34.0, ImageJ v2.16.0, Seurat, Signac v1.14.0]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Raw sequencing reads were processed using FastQC (Babraham Bioinformatics) and Trimmomatic 72 before alignment to the human genome hg38.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Version used: **0.11.8**
- Evidence: RNA-seq data processing and analysis: raw paired-end reads in FASTQ format were checked for read quality using FastQC (v.0.11.8; http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Evidence: Chromatin accessibility analysis After routine quality control with FastQC, reads were mapped onto the reference genome (hg19) using RSubread (v.2.18.0) in the DNA mode 58 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Version used: **0.73**
- Evidence: Fastq files were quality controlled using FastQC v.0.73 and trimmed with Trim Galore! v.0.6.7.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Version used: **0.11.9**
- Evidence: Raw RNA-sequencing data in FASTQ format were subjected to quality assessment using FastQC (v.0.11.9) and sequencing reads were aligned to mouse genome (mm10) using a STAR aligner 79 with the following options: --outFilterMismatchNmax 999 --outFilterMismatchNoverLmax 0.04 --alignSJDBoverhangMin 1 --alignSJoverhangMin 8 --outFilterMultimapNmax 20 --outFilterType BySJout --alignIntronMin 20 --alignIn...
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Sequence quality was assessed using FastQC followed by the removal of low-quality reads and adapter sequences using Cutadapt.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: Alignment We used Trim Galore to remove adapters and FastQC to generate QC reports before running alignment.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: In brief, raw FASTQ files provided by the sequencing facility were assessed for quality with FastQC 67 , followed by trimming of adapter sequences and removal of low-quality reads with fastp 68 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Reads were preprocessed according to the type of library preparation using cutadapt to trim adapters and FastQC to assess read quality.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Version used: **0.11.9**
- Evidence: Quality control of the raw and trimmed reads was assessed using FastQC (v.0.11.9).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Version used: **0.11.5**
- Evidence: RNA-seq data processing and analysis RNA-seq FASTQ files were processed through FastQC (v.0.11.5), a quality-control tool to evaluate the quality of sequencing reads at both the base and read levels, and RNA-SeQC (v.1.1.8) to generate a series of RNA-seq-related quality-control metrics 51 .
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Version used: **0.12.1**
- Evidence: The sequencing quality was assessed using FastQC (v0.12.1) executed within a containerized environment provided by biocontainers using Podman.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **0.12.1**
- Evidence: Quality assessment of RNA-seq data, including sequence, alignment and quantification metrics, was conducted using FastQC v.0.12.1 and summarized with MultiQC v.1.13.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: RNA-seq analysis was performed using the SUSHI framework 75 , which encompassed the following steps: read quality was inspected using FastQC, and sequencing adaptors were removed using fastp 76 ; pseudoalignment and transcriptomic counts of the RNA-seq reads was performed using the Kallisto Bioconductor R package 77 with the GENCODE human genome build GRCh38.p13 (release 37) 78 ; differential expr...
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Regulation of PV interneuron plasticity by neuropeptide-encoding genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08933-z | PMCID: PMC12222018 | PMID: 40307547
- Evidence: Specifically, sequencing reads were quality-controlled by FastQC (available at https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and quality-trimmed by Trim Galore (available at https://zenodo.org/record/5127899#.Y8fdOi-l3UI ).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> stage not stated [Nextflow v21.03.0, edgeR]

### Microbial metabolite drives ageing-related clonal haematopoiesis via ALPK1. (Nature 2025)

- DOI: 10.1038/s41586-025-08938-8 | PMCID: PMC12137129 | PMID: 40269158
- Version used: **0.11.8**
- Evidence: Statistical analysis of the number of reads, length and mean quality (phred) score were verified using FastQC (v.0.11.8).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [HISAT2] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, FastQC v0.11.8, R] -> stage not stated [MACS2, ggplot2, phyloseq]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **0.11.9**
- Evidence: Fastq files were subjected to quality control with FastQC (0.11.9) and then trimmed with Cutadapt (2.1) with reads less than 20 nucleotides being filtered out.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **0.11.4**
- Evidence: RNA sequencing analysis Sequence read quality was assessed using FastQC v.0.11.4 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Plasticity of the mammalian integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-08794-6 | PMCID: PMC12119373 | PMID: 40140574
- Version used: **0.11.4**
- Evidence: The quality of sequencing reads was confirmed using FastQC (v0.11.4; http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.4] -> read trimming [R] -> alignment/mapping [Bioconductor, HTSeq, featureCounts] -> quantification [ImageJ] -> normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [ImageJ] -> stage not stated [DESeq2]

### Perception of viral infections and initiation of antiviral defence in rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08706-8 | PMCID: PMC12043510 | PMID: 40074903
- Evidence: FastQC software was used to assess the quality of the raw sequencing reads.
- Full pipeline: quality control [FastQC] -> read trimming [TopHat] -> alignment/mapping [TopHat] -> quantification [ImageJ]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Version used: **0.11.9**
- Evidence: Initially, the quality of raw RNA-seq reads from each sample (Supplementary Table 6 ) underwent assessment using FastQC v.0.11.9 ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Evidence: FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) was used for quality control checks with the above data, according to the above results to trim low-quality reads using Trimmomatic 73 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Aspirin prevents metastasis by limiting platelet TXA&lt;sub&gt;2&lt;/sub&gt; suppression of T cell immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-08626-7 | PMCID: PMC12018268 | PMID: 40044852
- Evidence: The FastQ files were then subjected to quality control using FastQC and then alignment to the NCBIM37 Mus musculus genome annotation using the STAR workflow.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3, QuPath]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **0.11.5**
- Evidence: Raw TACIT sequencing data were evaluated using FastQC (v.0.11.5), followed by mapping to the mouse reference genome mm10 by Bowtie2 (v.2.2.9) 55 .
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **0.11.9**
- Evidence: Mapping of RNA-seq expression data Quality checks and trimming on the raw RNA-seq data files were done using FastQC v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), FastP (v.0.20.1) 58 , MultiQC (v.1.9) 59 and FastQ Screen (v.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Version used: **0.11.8**
- Evidence: Preprocessing and mapping quality control was done using FastQC (v.0.11.8) 67 , qualimap (v.2.2.2d) 68 , samtools (v.1.12) 69 and multiqc (v.1.9) 70 .
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Version used: **0.12.0**
- Evidence: For taxonomic analysis, paired-end reads were quality-checked with FastQC v.0.12.0 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and filtered with Trimmomatic 44 v.0.36 to remove adapters and low-quality reads.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### The maternal X chromosome affects cognition and brain ageing in female mice. (Nature 2025)

- DOI: 10.1038/s41586-024-08457-y | PMCID: PMC11798838 | PMID: 39843739
- Evidence: The quality of the reads was determined using FastQC, and more than 90% of reads from each sample had a mean quality score over 30.
- Full pipeline: quality control [FastQC] -> read trimming [STAR] -> alignment/mapping [Bismark, STAR] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, featureCounts]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Version used: **0.25**
- Evidence: More specifically, we included the following filters: FRiP 0.01 or over, FastQC 0.25 or over, uniquely mapped ratio 0.6 or over, peaks with fold change above ten, 500 or more, peaks union DNase I hypersensitive site ratio 0.7 or above and PCR bottleneck coefficient 0.8 or above.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: Sequencing data were quality controlled by FastQC and aligned to the mouse genome (NCBI37/mm9) using STAR (v2.4.0e) (10.1093/bioinformatics/bts635).
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **0.11.8**
- Evidence: The resulting reads were quality controlled using FastQC v.0.11.8 and Trim Galore v.0.6.10, and mapped to M. truncatula v5 genome (MtrunA17r5.0-ANR) using STAR v.2.5.a.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Evidence: Reads were trimmed using Cutadapt 43 (v.3.4) and quality was checked with FastQC 44 (v0.11.9).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Version used: **0.11.9**
- Evidence: (v0.6.6; https://github.com/FelixKrueger/TrimGalore ), after which quality control was performed with FastQC (v0.11.9; https://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Bioinformatics Sequencing data processing and alignment Initial quality-control analysis was performed using the FastQC toolkit ( https://github.com/s-andrews/FastQC ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Macrophages excite muscle spindles with glutamate to bolster locomotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08272-5 | PMCID: PMC11735391 | PMID: 39633045
- Evidence: Read quality controls were carried out using FastQC-v.0.11.9, trimming reads less than Phred33 quality score 20 and removing remaining adapters with Trim-Galore (v.0.6.6).
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [DESeq2, ImageJ, ggplot2, scDblFinder]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **0.11.8**
- Evidence: Bioinformatic analysis of bulk RNA-seq and scRNA-seq data Bulk transcriptomic FASTQ data quality was assessed using FastQC (v.0.11.8) 59 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### H&lt;sub&gt;2&lt;/sub&gt;O&lt;sub&gt;2&lt;/sub&gt; repurposes plant O&lt;sub&gt;2&lt;/sub&gt; sensing to regulate post-hypoxia responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10366-1 | PMCID: PMC13216066 | PMID: 42020755
- Evidence: After a quality check using FastQC, we aligned the reads on the A. thaliana full genome (TAIR 10) using Rsubread 74 (v.2.16.1) and counted them using featureCounts 75 (in the Rsubread package).
- Full pipeline: quality control [FastQC, featureCounts] -> alignment/mapping [FastQC, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR] -> stage not stated [ImageJ, R v4.3.1]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **0.12.1**
- Evidence: Briefly, FASTQ files underwent quality control (FastQC v.0.12.1), adaptors were trimmed (Trim Galore! v.0.6.7), reads were aligned to the GRCh38 human reference transcriptome (STAR v.2.7.9a) and a gene expression matrix was generated (Salmon v.1.10.1).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **0.11.8**
- Evidence: Read quality was verified using FastQC v.0.11.8 and MultiQC v.1.8.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Evidence: Sequencing data were quality controlled using FastQC and aligned to the mouse genome (NCBI38/mm10) using TopHat (v.1.0.13) with up to two mismatches 61 .
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### Natural maternal immunity protects neonates from Escherichia coli sepsis. (Nature 2026)

- DOI: 10.1038/s41586-026-10225-z | PMCID: PMC13108393 | PMID: 41813901
- Version used: **0.12.1**
- Evidence: Raw reads were quality-assessed using FastQC (v.0.12.1) and NanoPlot (v.1.46.0) 86 .
- Full pipeline: quality control [FastQC v0.12.1, NanoPlot v1.46.0] -> alignment/mapping [MAFFT v7.526, QUAST v5.2.0.2] -> stage not stated [Python, SPAdes]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **0.11.5**
- Evidence: RNA-seq sequence, alignment and quantification qualities were assessed using FastQC (v.0.11.5) and MultiQC (v.1.8) 69 .
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **0.11.9**
- Evidence: The quality of the raw sequencing data was assessed using FastQC (v.0.11.9) and MultiQC (v.1.10.1).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Sequencing quality was assessed using FastQC 71 v.0.11.6 and MultiQC 72 v.1.7 viewer for aggregated reports.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Version used: **0.11.9**
- Evidence: In brief, data were trimmed using cutadapt (v.2.9) 75 , quality checked before and after trimming using FastQC (v.0.11.9), and then mapped and quantified using STAR (v.2.7.7a) 76 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Version used: **0.11.9**
- Evidence: ChIP–seq, DRIP–seq, BrdU–seq and TT chem –seq data analysis For all sequencing data, a sequencing quality profile was generated using FastQC (v.0.11.9).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Analysis of bulk RNA-seq of stimulated fibroblasts Raw FASTQ reads were processed using FastQC 70 , Trim Galore ( https://github.com/FelixKrueger/TrimGalore ) and SortMeRNA 71 to remove low-quality reads, adaptors and ribosomal RNA.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **0.11.8**
- Evidence: (v.0.6.2) and assessed for quality using FastQC (v.0.11.8).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Version used: **0.11.2**
- Evidence: Adapters with low-quality ends were trimmed from FASTQ files using Trim Galore (v.0.6) and quality analysis performed using FastQC (v.0.11.2).
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Evidence: Datasets that failed to meet more than one of the following quality thresholds were excluded: raw sequence median quality score (FastQC score) ≥25; ratio of uniquely mapped reads ≥0.6; PBC score ≥80%; union DNase I hypersensitive site overlap of the 5,000 most significant peaks ≥70%; number of peaks with fold change above 10 ≥500; and fraction of reads in peaks ≥1%.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Raw sequence quality was assessed using the FastQC algorithm (v0.11.8).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Raw sequencing reads were then quality checked using FastQC software (v.0.11.9) 55 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### SIGLEC12 mediates plasma membrane rupture during necroptotic cell death. (Nature 2026)

- DOI: 10.1038/s41586-025-09741-1 | PMCID: PMC12779560 | PMID: 41225007
- Version used: **0.11.2**
- Evidence: All the fastq files underwent routine quality checks using FastQC (v.0.11.2; http://www.bioinformatics.babraham.ac.uk/projects/fastqc ) and FastQ Screen (v.0.4.4; http://www.bioinformatics.babraham.ac.uk/projects/fastq_screen ).
- Full pipeline: quality control [FastQC v0.11.2] -> alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [Fiji, ImageJ]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Raw sequencing reads were trimmed and quality-filtered using Trimmomatic and FastQC, respectively.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Evidence: Read quality was initially assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc ) and the FASTX-Toolkit ( http://hannonlab.cshl.edu/fastx_toolkit/ ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### The cyclic dinucleotide 2'3'-cGAMP induces a broad antibacterial and antiviral response in the sea anemone &lt;i&gt;Nematostella vectensis&lt;/i&gt;. (PNAS 2021)

- DOI: 10.1073/pnas.2109022118 | PMCID: PMC8713801 | PMID: 34903650
- Evidence: Read quality was assessed using FastQC.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Clustal Omega, DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Version used: **0.11.8**
- Evidence: The raw fastq files were first quality checked using FastQC (version 0.11.8) software.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Emergent RNA-RNA interactions can promote stability in a facultative phototrophic endosymbiosis. (PNAS 2021)

- DOI: 10.1073/pnas.2108874118 | PMCID: PMC8463893 | PMID: 34521754
- Evidence: Result were subsequently checked with FastQC.
- Full pipeline: quality control [FastQC] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2] -> quantification [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [BLAST]

### Restoring fertility in yeast hybrids: Breeding and quantitative genetics of beneficial traits. (PNAS 2021)

- DOI: 10.1073/pnas.2101242118 | PMCID: PMC8463882 | PMID: 34518218
- Version used: **0.11.5**
- Evidence: Paired-end raw Illumina sequence reads were quality checked through FastQC 0.11.5 ( 95 ) and trimmed through Trimmomatic 0.36 ( 96 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Evidence: Sequence data quality was determined using FastQC software.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Amino acids activate mTORC1 to release roe deer embryos from decelerated proliferation during diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2100500118 | PMCID: PMC8536382 | PMID: 34452997
- Evidence: Basic read statistics and read quality was evaluated based on FastQC reports ( 64 ), and a MultiQC overview report of all samples was generated ( 65 ).
- Full pipeline: quality control [FastQC, MultiQC] -> differential/statistical testing [FastQC, MultiQC, R] -> stage not stated [Galaxy, Trim Galore]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: Quality of sequencing reads was filtered using FastQC ( 37 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Transposon-mediated insertional mutagenesis unmasks recessive insecticide resistance in the aphid <i>Myzus persicae</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100559118 | PMCID: PMC8201860 | PMID: 34074777
- Evidence: FastQC was used to check the quality of the raw reads obtained ( 48 ), and reads were trimmed using TrimGalore ( 49 ).
- Full pipeline: quality control [FastQC, Trim Galore v0.4.5] -> read trimming [FastQC] -> alignment/mapping [HISAT2 v2.1.0, HTSeq] -> differential/statistical testing [edgeR v3.9] -> stage not stated [MUSCLE v3.8]

### Epigenetic inheritance of DNA methylation changes in fish living in hydrogen sulfide-rich springs. (PNAS 2021)

- DOI: 10.1073/pnas.2014929118 | PMCID: PMC8255783 | PMID: 34185679
- Evidence: The FastQC program ( 67 ) was used to assess data quality.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [R, edgeR]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Evidence: The quality of the demultiplexed reads was checked with FastQC ( 54 ) before and after read trimming.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Resetting proteostasis with ISRIB promotes epithelial differentiation to attenuate pulmonary fibrosis. (PNAS 2021)

- DOI: 10.1073/pnas.2101100118 | PMCID: PMC8157939 | PMID: 33972447
- Evidence: FASTQ files were generated using bcl2fast (version 2.19.1) followed by quality control using FastQC, trimming using Trimmomatic (version 0.36), and mapping to the mm10 version of the mouse genome with Spliced Transcripts Alignment to a Reference aligner (STAR, version 2.6.0).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> alignment/mapping [FastQC, Trimmomatic v0.36] -> differential/statistical testing [edgeR v3.28.0] -> stage not stated [Fiji v1.8.0, HTSeq v0.11.2, ImageJ v1.8.0]

### Phylogenomic and ecological analyses reveal the spatiotemporal evolution of global pines. (PNAS 2021)

- DOI: 10.1073/pnas.2022302118 | PMCID: PMC8157994 | PMID: 33941644
- Version used: **0.11.5**
- Evidence: Raw reads were checked with FastQC (v.0.11.5) ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), trimmed using Trimmomatic (v.0.36) ( 63 ), and then assembled using Trinity (v.20140717) ( 64 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> read trimming [FastQC v0.11.5, Trimmomatic v0.36, Trinity] -> dimensionality reduction/clustering [phytools v0.7] -> stage not stated [IQ-TREE v2.0, R v3.6.2, ggplot2]

### The synaptonemal complex imposes crossover interference and heterochiasmy in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023613118 | PMCID: PMC8000504 | PMID: 33723072
- Version used: **0.11.9**
- Evidence: The raw reads were evaluated for quality by using FastQC version 0.11.9 ( 95 ), and then potential adapter sequences were trimmed and low-quality bases were filtered using Trimmomatic version 0.38 ( 96 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.38] -> read trimming [FastQC v0.11.9, Trimmomatic v0.38]

### Cytokine receptor clustering in sensory neurons with an engineered cytokine fusion protein triggers unique pain resolution pathways. (PNAS 2021)

- DOI: 10.1073/pnas.2009647118 | PMCID: PMC7980471 | PMID: 33836560
- Evidence: All samples passed the read quality checks performed using FastQC ( 78 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR]

### <i>Drosophila</i> Fezf functions as a transcriptional repressor to direct layer-specific synaptic connectivity in the fly visual system. (PNAS 2021)

- DOI: 10.1073/pnas.2025530118 | PMCID: PMC8020669 | PMID: 33766917
- Evidence: Raw reads were examined for quality issues using FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to ensure library generation and sequencing data were suitable for further analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2, MACS2 v2.1.1] -> stage not stated [Fiji, ImageJ]

### Lipid droplets in mammalian eggs are utilized during embryonic diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2018362118 | PMCID: PMC7958255 | PMID: 33649221
- Evidence: Raw reads were checked for quality using FastQC software (Babraham Bioinformatics) filtered to remove accidental adapter sequences and low-quality reads and mapped against the Mus musculus GRCm38 genome assembly using TopHat2 ( 44 ) software set for paired-end reads.
- Full pipeline: quality control [FastQC, TopHat] -> read trimming [FastQC, TopHat] -> alignment/mapping [FastQC, HTSeq, TopHat, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Pluripotent stem cell-derived epithelium misidentified as brain microvascular endothelium requires ETS factors to acquire vascular fate. (PNAS 2021)

- DOI: 10.1073/pnas.2016950118 | PMCID: PMC7923590 | PMID: 33542154
- Version used: **0.11.5**
- Evidence: Sample files were checked for sequence quality (FastQC v0.11.5) and processed using the Digital Expression Explorer 2 (DEE2) ( 63 ) workflow.
- Full pipeline: quality control [FastQC v0.11.5, R, edgeR] -> read trimming [R, STAR, edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Heat stress destabilizes symbiotic nutrient cycling in corals. (PNAS 2021)

- DOI: 10.1073/pnas.2022653118 | PMCID: PMC7865147 | PMID: 33500354
- Version used: **0.11.5**
- Evidence: The successful removal of adapters from paired reads was confirmed using FastQC v.0.11.5 ( 87 ).
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [FastQC v0.11.5, Trimmomatic v0.39] -> alignment/mapping [Salmon v1.0.0] -> quantification [Salmon v1.0.0, lme4] -> differential/statistical testing [R, vegan v2.5] -> stage not stated [ImageJ]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Version used: **0.11.7**
- Evidence: The data quality was checked by FastQC v0.11.7 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Inflammatory response to retrotransposons drives tumor drug resistance that can be prevented by reverse transcriptase inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2213146119 | PMCID: PMC9894111 | PMID: 36449545
- Evidence: The quality of the RNA sequencing data was assessed via FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [featureCounts]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: Paired-end 100 bp reads were controlled for quality with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) before trimming Illumina adapters from the 3′ ends using cutadapt ( 62 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### Silencing RNAs expressed from W-linked &lt;i&gt;PxyMasc&lt;/i&gt; "retrocopies" target that gene during female sex determination in &lt;i&gt;Plutella xylostella&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2206025119 | PMCID: PMC9674220 | PMID: 36343250
- Evidence: Sequenced reads were checked for quality using FastQC ( 37 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [BLAST, Clustal Omega]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: The quality of raw, 150-bp paired-end reads in FASTQ format was assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### A scalable framework for the discovery of functional helicase substrates and helicase-driven regulatory switches. (PNAS 2022)

- DOI: 10.1073/pnas.2209608119 | PMCID: PMC9499579 | PMID: 36095194
- Version used: **0.11.5**
- Evidence: Multiplexed sequencing of the pools resulted in 4.6 to 9.5 × 10 6 paired-end reads per pool after quality control filtering (FastQC v0.11.5) and adapter trimming (Cutadapt v1.15).
- Full pipeline: quality control [Cutadapt v1.15, FastQC v0.11.5] -> read trimming [Cutadapt v1.15, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [Galaxy, MACS2, Python]

### Different classes of genomic inserts contribute to human antibody diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2205470119 | PMCID: PMC9457163 | PMID: 36037353
- Evidence: Quality score per base position was assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> read trimming [R, Trim Galore, Trimmomatic] -> alignment/mapping [R, Trimmomatic] -> stage not stated [BEDTools, MACS2, ggplot2]

### Hippo signaling cofactor, WWTR1, at the crossroads of human trophoblast progenitor self-renewal and differentiation. (PNAS 2022)

- DOI: 10.1073/pnas.2204069119 | PMCID: PMC9457323 | PMID: 36037374
- Evidence: The quality of the sequenced data was assessed using FastQC software.
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA, MACS2]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Evidence: The quality of the raw sequencing reads was assessed with FastQC ( 52 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Adaptive laboratory evolution and independent component analysis disentangle complex vancomycin adaptation trajectories. (PNAS 2022)

- DOI: 10.1073/pnas.2118262119 | PMCID: PMC9335240 | PMID: 35858453
- Evidence: The transcriptome analysis was performed using FastQC for quality control, Bowtie2 for mapping, htseq-count to count the number of mapped reads to each gene, and DeSeq2 to assess the differential expression between ancestor and evolved strains.
- Full pipeline: quality control [Bowtie2, FastQC, HTSeq] -> alignment/mapping [Bowtie2, FastQC, HTSeq] -> differential/statistical testing [Bowtie2, FastQC, HTSeq]

### Seed DNA damage responses promote germination and growth in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2202172119 | PMCID: PMC9335332 | PMID: 35858436
- Evidence: The qualities of the FASTQ files were assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [SAMtools] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Version used: **0.11.5**
- Evidence: Reads were quality-checked by FastQC ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### In situ structure of intestinal apical surface reveals nanobristles on microvilli. (PNAS 2022)

- DOI: 10.1073/pnas.2122249119 | PMCID: PMC9214534 | PMID: 35666862
- Evidence: According to the results of FastQC, adaptors or low-quality nucleotides were trimmed by Trim Galore (version [v] 0.5.2) using default parameters.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [IMOD, STAR v2.6.0c] -> stage not stated [ImageJ, MotionCor2, UCSF Chimera]

### A brain-enriched lncRNA shields cancer cells from immune-mediated killing for metastatic colonization in the brain. (PNAS 2022)

- DOI: 10.1073/pnas.2200230119 | PMCID: PMC9295751 | PMID: 35617432
- Evidence: Then, raw RNA-seq data were analyzed by using a commonly used FastQC-Tophat2-cufflinks workflow ( 48 ).
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA]

### A set point in the selection of the αβTCR T cell repertoire imposed by pre-TCR signaling strength. (PNAS 2022)

- DOI: 10.1073/pnas.2201907119 | PMCID: PMC9295770 | PMID: 35617435
- Evidence: The quality of reads was assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> stage not stated [R]

### Enzymes degraded under high light maintain proteostasis by transcriptional regulation in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121362119 | PMCID: PMC9171785 | PMID: 35549553
- Version used: **0.11.7**
- Evidence: Raw read quality was first diagnosed using FastQC (v0.11.7).
- Full pipeline: quality control [FastQC v0.11.7] -> alignment/mapping [SAMtools v1.3.1, featureCounts] -> differential/statistical testing [edgeR] -> stage not stated [Trim Galore]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Version used: **0.11.3**
- Evidence: The libraries were cleaned using Trimmomatic (version 0.32; command line options: LEADING:20 TRAILING:20 SLIDINGWINDOW:5:20 MINLEN:85, phred33) ( 36 ) and FastQC (version 0.11.3) ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to remove adaptors and low-quality reads.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Brap regulates liver morphology and hepatocyte turnover via modulation of the Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2201859119 | PMCID: PMC9171358 | PMID: 35476518
- Evidence: Data quality analysis was performed via FastQC ( 23 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [R]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Version used: **11.5**
- Evidence: Raw paired-ended FASTQ data were assessed for quality with FastQC (version11.5) ( 54 ).
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### The CHARGE syndrome ortholog CHD-7 regulates TGF-β pathways in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2109508119 | PMCID: PMC9169646 | PMID: 35394881
- Evidence: For data assessment, a quality control with FastQC software (v0.11.5) was used.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.5.4a] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [Bioconductor v3.7, R v3.5]

### Engineering and functional analysis of yeast with a monotypic 40S ribosome subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2114445119 | PMCID: PMC8833219 | PMID: 35105807
- Evidence: The quality of the raw reads was first evaluated with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), and then low-quality reads were excluded using Trimmomatic (0.36) with default parameters ( 45 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> variant calling [GATK v3.5, SnpEff] -> registration [GATK v3.5] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [Picard]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Data quality analysis was performed via FastQC ( 53 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### MRP5 and MRP9 play a concerted role in male reproduction and mitochondrial function. (PNAS 2022)

- DOI: 10.1073/pnas.2111617119 | PMCID: PMC8832985 | PMID: 35121660
- Version used: **0.11.7**
- Evidence: FastQC, version 0.11.7, was used as an additional bioinformatics quality control on output reads from sequencing.
- Full pipeline: quality control [FastQC v0.11.7] -> differential/statistical testing [Bioconductor v3.4, DESeq2 v1.12.3, R v3.6.1] -> stage not stated [HOMER]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: The quality of raw data was examined by FastQC, and sequencing adapter and low-quality reads, including those with more than five “N” bases and mean Phred quality score less than 15, were removed through fastp.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### The embryonic node behaves as an instructive stem cell niche for axial elongation. (PNAS 2022)

- DOI: 10.1073/pnas.2108935119 | PMCID: PMC8812687 | PMID: 35101917
- Evidence: Raw data were checked using FastQC ( 58 ) to assess overall quality.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [TopHat] -> normalisation [Cufflinks]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Version used: **0.69**
- Evidence: We used FastQC (version 0.69) to assess read quality, and we used a PHRED cutoff of 20 ( 75 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **0.11.8**
- Evidence: Using only the forward reads from each dataset if paired end, RNA-seq sequencing read quality was confirmed with FastQC v0.11.8 ( 51 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Adapter sequences and low-quality bases were trimmed from Fastq files using trim_galore and FastQC was performed on the trimmed reads.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Adaptive DNA amplification of synthetic gene circuit opens a way to overcome cancer chemoresistance. (PNAS 2023)

- DOI: 10.1073/pnas.2303114120 | PMCID: PMC10710087 | PMID: 38019857
- Version used: **0.11.5**
- Evidence: RNA sequencing reads were first quality-checked by FastQC v0.11.5.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.6.1d] -> quantification [featureCounts] -> stage not stated [Fiji, ImageJ, R v4.1, fastp v0.20.1]

### High-throughput screening of glucocorticoid-induced enhancer activity reveals mechanisms of stress-related psychiatric disorders. (PNAS 2023)

- DOI: 10.1073/pnas.2305773120 | PMCID: PMC10710077 | PMID: 38011552
- Evidence: The STARR libraries were generated by PCR and sequenced on the Illumina MiSeq, and the quality of the reads was assessed using FastQC.
- Full pipeline: quality control [FastQC] -> differential/statistical testing [TwoSampleMR] -> stage not stated [R]

### The emergence and diversification of a zoonotic pathogen from within the microbiota of intensively farmed pigs. (PNAS 2023)

- DOI: 10.1073/pnas.2307773120 | PMCID: PMC10666105 | PMID: 37963246
- Evidence: Raw and preprocessed reads were assessed for quality to ensure cleaning efficiency using FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v1.2.2, QUAST v5.0.1] -> stage not stated [Canu v1.9, Prokka v1.14.5, R]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Evidence: The quality of the resultant 150-bp paired-end RNA-seq reads was assessed by FastQC (available at https://qubeshub.org/resources/fastqc ), and low-quality bases/reads were trimmed or filtered out using Trimmomatic ( 62 ) with default parameters (ILLUMINACLIP:adapter:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Endothelial deletion of EPH receptor A4 alters single-cell profile and Tie2/Akap12 signaling to preserve blood-brain barrier integrity. (PNAS 2023)

- DOI: 10.1073/pnas.2204700120 | PMCID: PMC10576133 | PMID: 37796990
- Evidence: The sequencing quality of raw reads was first assessed using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC, Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Trim Galore, scDblFinder]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: RNA-seq datasets ( GSE101646 ) were subjected to quality control using FastQC, followed by trimming with Trimmomatic to ensure high-quality data.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: The quality of STAR alignments was assessed for evenness of coverage, ribosomal RNA content, exon and intron mapping rate, complexity, and other criteria using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), Qualimap ( 59 ), and MultiQC ( 60 ).
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### Environmental DNA reveals the genetic diversity and population structure of an invasive species in the Laurentian Great Lakes. (PNAS 2023)

- DOI: 10.1073/pnas.2307345120 | PMCID: PMC10500163 | PMID: 37669387
- Version used: **0.11.8**
- Evidence: Sequencing adapters were trimmed with Trimmomatic v0.39 ( 54 ), and sequence quality was assessed with FastQC version 0.11.8 ( 55 ).
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.39] -> read trimming [FastQC v0.11.8, Trimmomatic v0.39] -> differential/statistical testing [R v4.1] -> stage not stated [DADA2, lme4]

### Myo-differentiation reporter screen reveals NF-Y as an activator of PAX3-FOXO1 in rhabdomyosarcoma. (PNAS 2023)

- DOI: 10.1073/pnas.2303859120 | PMCID: PMC10483665 | PMID: 37639593
- Evidence: Quality of the sequencing data was assessed using FastQC.
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Version used: **0.11.4**
- Evidence: Genome-wide methylation analysis for secondary WT and Tet2 KO Th1 and Tfh SMARTA cells was carried out as follows: Sequencing data quality was assessed using FastQC v0.11.4.
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### Triple-negative breast tumors are dependent on mutant p53 for growth and survival. (PNAS 2023)

- DOI: 10.1073/pnas.2308807120 | PMCID: PMC10450424 | PMID: 37579145
- Evidence: RNA-seq FASTQ files were processed through FastQC, a quality control tool used to evaluate the quality of sequencing reads at both the base and read levels.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Version used: **0.11.8**
- Evidence: Indexed samples were deconvoluted after sequencing, and integrity of sequencing data was checked using FastQC (v 0.11.8).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### The genomic landscape of swine influenza A viruses in Southeast Asia. (PNAS 2023)

- DOI: 10.1073/pnas.2301926120 | PMCID: PMC10438389 | PMID: 37552753
- Evidence: The NGS reads were checked with FastQC ( 48 ) in Unipro UGENE v40.1 ( 49 ) and were processed by trimming adaptors via Trimmomatic v0.39 ( 50 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.39] -> read trimming [FastQC, Trimmomatic v0.39] -> structure determination [BEAST v10.4, RAxML v1.1.0] -> stage not stated [BLAST v2.2.18, SPAdes v3.15.3]

### SARS-CoV-2 mouse adaptation selects virulence mutations that cause TNF-driven age-dependent severe disease with human correlates. (PNAS 2023)

- DOI: 10.1073/pnas.2301689120 | PMCID: PMC10410703 | PMID: 37523564
- Version used: **0.11.9**
- Evidence: Quality control analysis of RNA-seq fastq files was performed using FastQC (v0.11.9, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.12] -> alignment/mapping [featureCounts, minimap2 v2.2.4] -> quantification [featureCounts] -> machine learning [StarDist] -> stage not stated [R v4.2, edgeR, limma]

### Activin E-ACVR1C cross talk controls energy storage via suppression of adipose lipolysis in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2309967120 | PMCID: PMC10410708 | PMID: 37523551
- Evidence: Reads were decoded based on their barcodes, and read quality was evaluated with FastQC ( www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2]

### Host hydrocarbons protect symbiont transmission from a radical host defense. (PNAS 2023)

- DOI: 10.1073/pnas.2302721120 | PMCID: PMC10400980 | PMID: 37487102
- Evidence: Sequences were quality-controlled and trimmed using FastQC ( 96 ) and Trimmomatic ( 97 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> differential/statistical testing [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> visualisation [ggplot2]

### IL-7R licenses a population of epigenetically poised memory CD8<sup>+</sup> T cells with superior antitumor efficacy that are critical for melanoma memory. (PNAS 2023)

- DOI: 10.1073/pnas.2304319120 | PMCID: PMC10372654 | PMID: 37459511
- Evidence: Reads were quality filtered and trimmed of Illumina adapters using FastQC and Cutadapt.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, STAR, featureCounts] -> alignment/mapping [STAR, featureCounts] -> quantification [STAR, featureCounts] -> differential/statistical testing [DESeq2, R v4.0] -> stage not stated [RSEM]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Evidence: Illumina sequence data were assessed using FastQC for per base and sequence quality score, GC content, and sequence length distribution.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### The developmental basis for scaling of mammalian tooth size. (PNAS 2023)

- DOI: 10.1073/pnas.2300374120 | PMCID: PMC10288632 | PMID: 37307487
- Evidence: The RNAseq reads of mice and rats were evaluated and bad reads were filtered out using FastQC [v.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> differential/statistical testing [R]

### Osteolectin increases bone elongation and body length by promoting growth plate chondrocyte proliferation. (PNAS 2023)

- DOI: 10.1073/pnas.2220159120 | PMCID: PMC10235998 | PMID: 37216542
- Version used: **0.11.8**
- Evidence: The quality of raw reads was checked using FastQC 0.11.8.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bowtie2 v4.1, Trim Galore v0.6.4] -> alignment/mapping [Bowtie2 v4.1, SAMtools v1.12, Trim Galore v0.6.4] -> stage not stated [deepTools v3.5.1]

### EGR4 is critical for cell-fate determination and phenotypic maintenance of geniculate ganglion neurons underlying sweet and umami taste. (PNAS 2023)

- DOI: 10.1073/pnas.2217595120 | PMCID: PMC10235952 | PMID: 37216536
- Version used: **0.11.5**
- Evidence: The sequencing reads were first quality checked using FastQC (v.0.11.5, Babraham Bioinformatics, Cambridge, UK).
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.5] -> differential/statistical testing [GSEA, edgeR v3.12.1] -> stage not stated [ImageJ]

### Aneuploidy effects on human gene expression across three cell types. (PNAS 2023)

- DOI: 10.1073/pnas.2218478120 | PMCID: PMC10214149 | PMID: 37192167
- Evidence: RNA-seq data from these three cell types were separately submitted to the following workflow ( SI Appendix , Text S1.1 ): i) FastQC ( 45 ), MultQC ( 46 ), and Trimmomatic ( 47 ) for QC and trimming, ii) Salmon ( 48 ) for transcript quantification with the Y chromosome masked reference transcriptome when mapping female samples and with the YPAR-gene masked one when mapping male samples to reduce mi...
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [DESeq2, FastQC, Trimmomatic] -> quantification [FastQC, Trimmomatic] -> dimensionality reduction/clustering [GSEA] -> stage not stated [R v4.1.0]

### Nonpathological inflammation drives the development of an avian flight adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2219757120 | PMCID: PMC10175837 | PMID: 37126698
- Evidence: All fastq files were screened using FastQC for per base sequence quality, and for all reads, mean and median quality scored in the “very good” range (28 to 36) with minimum falloff near the ends of reads (the last 5 to 10 bases).
- Full pipeline: quality control [FastQC] -> alignment/mapping [DESeq2, R v2.70f, STAR v2.70f, featureCounts] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, R v2.70f, STAR v2.70f, featureCounts]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Version used: **0.11.8**
- Evidence: RNA-seq read quality was confirmed with FastQC v0.11.8 ( 50 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Evidence: Reads were aligned to hg38 using a Bpipe ( 92 ) RNA-Seq pipeline that incorporated FastQC quality control, adaptor trimming with Trimmomatic v.0.35 ( 93 ), mapping with STAR 2.7.3a ( 94 ), summarizing reads over genes with featureCounts ( 95 ), and MultiQC ( 96 ) to summarize the analyses.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **0.11.7**
- Evidence: Sequence reads were assessed for quality using FastQC v0.11.7 ( 88 ) and trimmed for adaptor content using cutadapt v1.16 ( 89 ).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Euglenozoan kleptoplasty illuminates the early evolution of photoendosymbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2220100120 | PMCID: PMC10041101 | PMID: 36927158
- Evidence: Quality control of the Illumina MiSeq reads from the genomes of R. viridis and Tetraselmis sp. was performed with the FastQC tool v0.11.6 ( 40 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [IQ-TREE, MAFFT] -> differential/statistical testing [IQ-TREE] -> stage not stated [BUSCO, SPAdes v3.10.1]

### Two differentially stable rDNA loci coexist on the same chromosome and form a single nucleolus. (PNAS 2023)

- DOI: 10.1073/pnas.2219126120 | PMCID: PMC9992848 | PMID: 36821584
- Evidence: Briefly, reads were processed by Illumina barcode and quality trimmed with Trimmomatic ( 55 ) and quality assessed with FastQC ( 56 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2] -> visualisation [ImageJ] -> stage not stated [kallisto]

### Time series transcriptome analysis implicates the circadian clock in the &lt;i&gt;Drosophila melanogaster&lt;/i&gt; female's response to sex peptide. (PNAS 2023)

- DOI: 10.1073/pnas.2214883120 | PMCID: PMC9945991 | PMID: 36706221
- Version used: **0.11.8**
- Evidence: Quality control (QC) of sequenced libraries was performed using FastQC (version 0.11.8; https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R, Seurat] -> visualisation [ComplexHeatmap, ggplot2, igraph] -> stage not stated [edgeR]

### Community-engaged ancient DNA project reveals diverse origins of 18th-century African descendants in Charleston, South Carolina. (PNAS 2023)

- DOI: 10.1073/pnas.2201620120 | PMCID: PMC9934026 | PMID: 36623185
- Version used: **0.11.9**
- Evidence: FastQC v0.11.9 was used to verify the removal of all adapters and assess the overall quality of sequence reads.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.9] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9]

### Non-B-form DNA tends to form in centromeric regions and has undergone changes in polyploid oat subgenomes. (PNAS 2023)

- DOI: 10.1073/pnas.2211683120 | PMCID: PMC9910436 | PMID: 36574697
- Evidence: Quality control of raw reads was performed with FastQC software.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, Trimmomatic v0.36] -> alignment/mapping [BWA, MACS2, SAMtools v1.3.1, deepTools] -> normalisation [deepTools] -> visualisation [deepTools]

### Mutation-based mechanism and evolution of the potent multidrug efflux pump RE-CmeABC in &lt;i&gt;Campylobacter&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2415823121 | PMCID: PMC11665921 | PMID: 39602248
- Evidence: After sequencing, quality control of the raw sequence reads was done by using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and trimmed by Trimmomatic ( 59 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic] -> alignment/mapping [Bowtie2, MAFFT] -> stage not stated [Python]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: After receiving files from the company, read quality was assessed with FastQC ( 86 ).
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Targeting the MAtrix REgulating MOtif abolishes several hallmarks of cancer, triggering antitumor immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2404485121 | PMCID: PMC11494334 | PMID: 39382998
- Evidence: For each sample, quality control was carried out and assessed with the NGS Core Tools FastQC and QualiMap ( 47 ).
- Full pipeline: quality control [FastQC] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, ImageJ]

### miR-96-5p expression is sufficient to induce and maintain the senescent cell fate in the absence of stress. (PNAS 2024)

- DOI: 10.1073/pnas.2321182121 | PMCID: PMC11459134 | PMID: 39325426
- Evidence: Output FASTQ files were processed with FastQC; the Genome Analysis Toolkit (GATK; Broad Institute) was used to clean FASTQ files which were then aligned to hg38 with the (Burrows-Wheeler Aligner) BWA.
- Full pipeline: quality control [FastQC, GATK] -> alignment/mapping [FastQC, GATK] -> differential/statistical testing [MACS2] -> stage not stated [Enrichr]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Quality assessment of raw sequencing data was performed with FastQC software.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Machine learning reveals the transcriptional regulatory network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC 7942. (PNAS 2024)

- DOI: 10.1073/pnas.2410492121 | PMCID: PMC11420160 | PMID: 39269777
- Evidence: Next, Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) was applied with default options for read trimming, followed by FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore, featureCounts] -> read trimming [FastQC, Trim Galore] -> quantification [MultiQC, featureCounts] -> dimensionality reduction/clustering [STRING db] -> stage not stated [scikit-learn]

### Conserved 5-methyluridine tRNA modification modulates ribosome translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2401743121 | PMCID: PMC11363252 | PMID: 39159370
- Evidence: The reads were evaluated with FastQC ( 57 ) (v0.11.8) to determine the quality of the data.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.3] -> alignment/mapping [RSEM v1.3.3, STAR v2.7.8a] -> differential/statistical testing [DESeq2]

### Oxysterol binding protein regulates the resolution of TLR-induced cytokine production in macrophages. (PNAS 2024)

- DOI: 10.1073/pnas.2406492121 | PMCID: PMC11331125 | PMID: 39361877
- Version used: **0.11.5**
- Evidence: For all samples, initial quality assessment was performed with FastQC version 0.11.5 ( 48 ) before read ends consisting of 33% or more of the same nucleotide were removed.
- Full pipeline: quality control [FastQC v0.11.5] -> quantification [ImageJ, limma] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [R, edgeR v3.26.8, limma] -> stage not stated [GSEA, MACS2 v2.1.0, featureCounts]

### Lining the small intestine with mycobacteriophages protects from &lt;i&gt;Mycobacterium avium&lt;/i&gt; subsp. &lt;i&gt;paratuberculosis&lt;/i&gt; and eliminates fecal shedding. (PNAS 2024)

- DOI: 10.1073/pnas.2318627121 | PMCID: PMC11331133 | PMID: 39102547
- Version used: **0.12.1**
- Evidence: Illumina adaptor sequences were trimmed using Trimmomatic, ( 44 ) and quality control was performed using FastQC v0.12.1 ( 45 ).
- Full pipeline: quality control [FastQC v0.12.1, Trimmomatic] -> read trimming [FastQC v0.12.1, SPAdes v3.15.5, Trimmomatic]

### Improvement of a mouse infection model to capture &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt; chronic physiology in cystic fibrosis. (PNAS 2024)

- DOI: 10.1073/pnas.2406234121 | PMCID: PMC11331117 | PMID: 39102545
- Version used: **0.11.9**
- Evidence: After checking read quality in FastQC (v0.11.9), reads were mapped to the genomes of 105 non– P. aeruginosa decoy strains in bowtie2 (v2.4.2) ( 33 ).
- Full pipeline: quality control [Bowtie2 v2.4.2, FastQC v0.11.9] -> read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.4.2, FastQC v0.11.9] -> stage not stated [featureCounts v2.0.1]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Version used: **0.11.9**
- Evidence: Additionally, we used quality control and visualization tools in FastQC v0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and fastP ( 75 ) v0.11.9 to check sequencing quality, duplication levels, overrepresented sequences, and detection of residual adapter/barcode content.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### Intratumoral NKT cell accumulation promotes antitumor immunity in pancreatic cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2403917121 | PMCID: PMC11260137 | PMID: 38980903
- Evidence: In general, FastQC, STAR, featurecounts, RSEM, and GSEA were used for data analysis with the standard setting.
- Full pipeline: quality control [FastQC, RSEM] -> stage not stated [GSEA, ImageJ, MACS2]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: Quality control was performed with FastQC (Version 0.12.1) in Linux and with ATACseqQC (Version 1.16.0) in R (Version 4.1.0) ( 47 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### Beneficial metabolic effects of PAHSAs depend on the gut microbiota in diet-induced obese mice but not in chow-fed mice. (PNAS 2024)

- DOI: 10.1073/pnas.2318691121 | PMCID: PMC11252816 | PMID: 38968121
- Evidence: To ensure read quality, raw reads were assessed using FastQC and MultiQC, and host reads with low quality ends (Phred scores < 28) were filtered using Kneaddata quality control software ( 25 ) for automatic adapter detection, trimming low-quality read bases, and removing host (mouse genome) reads prior to downstream analyses.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, MultiQC] -> alignment/mapping [BLAST, HUMAnN, MetaPhlAn] -> quantification [HUMAnN, MetaPhlAn] -> dimensionality reduction/clustering [BLAST] -> stage not stated [DADA2]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Version used: **0.11.5**
- Evidence: Following quality assessment by FastQC (0.11.5, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), the clean reads were aligned to their corresponding reference genomes with HISAT2 (version 2.1.0) ( 44 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### The role of mitochondria in sex- and age-specific gene expression in a species without sex chromosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2321267121 | PMCID: PMC11181141 | PMID: 38838014
- Version used: **0.11.8**
- Evidence: Trimmomatic v0.38 ( 89 ) was used to perform adapter removal, quality trimming, and length trimming with default parameters, and trimmed reads were evaluated by FastQC v0.11.8 ( 90 ).
- Full pipeline: quality control [FastQC v0.11.8, Trimmomatic v0.38] -> read trimming [FastQC v0.11.8, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.7.2] -> stage not stated [WGCNA, featureCounts]

### Innate acting memory Th1 cells modulate heterologous diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2312837121 | PMCID: PMC11181110 | PMID: 38838013
- Evidence: Raw sequencing files were aligned to the mouse genome (GRCm38) with HiSat2 ( 61 ) (version 2.2.1) following quality control with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ; version 0.11.9).
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> stage not stated [R v4.0.2, featureCounts, ggplot2, pheatmap v1.0.12]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Version used: **0.11.9**
- Evidence: The obtained 100 bp paired-end reads were analyzed with FastQC (v 0.11.9) using parameters by default to assess quality, and adaptor sequences removed with Cutadapt (with parameters ‘--minimum-length=20 --max-n=0.1 --quality-cutoff=30,30’) ( 46 ) and then mapped to the TAIR10 A. thaliana reference genome with HISAT2 ( 47 ). htseq-count was used for read count (parameters: ‘--format=bam --order=nam...
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Version used: **0.11.9**
- Evidence: RNA-Seq FASTQ files were analyzed with FastQC (v.0.11.9) to evaluate the quality of sequencing reads ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Version used: **0.12.1**
- Evidence: Raw reads were processed to verify their quality scores and to confirm the absence of adaptor sequences using FastQC v0.12.1 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### Carbon starvation raises capacities in bacterial antibiotic resistance and viral auxiliary carbon metabolism in soils. (PNAS 2024)

- DOI: 10.1073/pnas.2318160121 | PMCID: PMC11032446 | PMID: 38598339
- Version used: **0.11.9**
- Evidence: The quality of raw data was evaluated by FastQC v0.11.9.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [BLAST v2.5.0] -> stage not stated [HMMER]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: The quality of reads was verified using FastQC.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Version used: **0.11.9**
- Evidence: Read quantity and quality was assessed with FastQC v0.11.9.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Version used: **0.11.2**
- Evidence: Sequence quality was assessed using FastQC v 0.11.2 ( 95 ), and quality trimming was done using Trimmomatic ( 96 ) with parameters TRAILING:30 MINLEN:20.
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Root-exuded specialized metabolites reduce arsenic toxicity in maize. (PNAS 2024)

- DOI: 10.1073/pnas.2314261121 | PMCID: PMC10990099 | PMID: 38513094
- Evidence: First, we performed a quality control using FastQC [V0.11.8, ( 69 )].
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> differential/statistical testing [R v4.1.2]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Evidence: Raw read quality was assessed using FastQC ( 79 ), and reads were trimmed with TrimGalore!
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Version used: **0.11.9**
- Evidence: Paired sequencing reads from each library were quality controlled using FastQC (v0.11.9) before being trimmed using Trimmomatic (v0.39), which retains only paired-end reads without adapters and with a phred score greater than 15 in a 4-base sliding window.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Version used: **0.11.5**
- Evidence: Quality was assessed with FastQC v0.11.5 and MultiQC v1.12 ( 50 ).
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: FastQ files were assessed for quality using FastQC and low-quality bases were trimmed used trimmomatic ( 108 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: The quality of the sequencing data was first checked with FastQC ( 33 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Version used: **0.11.9**
- Evidence: Sequencing run statistics and quality metric were visualized for each sample using FastQC version 0.11.9 and then compared to each other using MultiQC version 1.10 ( 66 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### Disruption of DNA methylation-mediated cranial neural crest proliferation and differentiation causes orofacial clefts in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2317668121 | PMCID: PMC10801837 | PMID: 38194455
- Evidence: An initial check of quality was assessed for each pair-mate using FastQC.
- Full pipeline: quality control [FastQC] -> read trimming [RSEM v1.3.1, STAR v2.7.0] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.0] -> variant calling [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: The quality of the raw and trimmed reads was assessed using FastQC and MultiQC ( 54 , 55 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### MBNL loss of function in smooth muscle as a model for myotonic dystrophy associated gastrointestinal dysmotility. (PNAS 2025)

- DOI: 10.1073/pnas.2522788122 | PMCID: PMC12718393 | PMID: 41379996
- Version used: **0.11.9**
- Evidence: Sequencing results were quality assessed, aligned, normalized, and analyzed using similar methods as previous work ( 124 ) using FastQC version 0.11.9, STAR version 2.7.10b, RSEM algorithm version 1.3.1 ( 125 ), DESeq2 version 1.42.0 for DGE ( 126 ), and rMATS version 4.1.2 for alternative splicing ( 127 ).
- Full pipeline: quality control [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> alignment/mapping [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> variant calling [ImageJ] -> normalisation [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> stage not stated [Metascape]

### A metabolic cell death program downstream of SARM1 couples NAD&lt;sup&gt;+&lt;/sup&gt; depletion to BAX activation and APAF1 degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2522444122 | PMCID: PMC12718333 | PMID: 41364765
- Evidence: Gene trap sequencing data were first subjected to quality control using FastQC to ensure high-quality reads.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, Trimmomatic] -> quantification [featureCounts] -> stage not stated [RSEM]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Version used: **0.11.9**
- Evidence: Quality checks of raw and concatenated FASTQ files were done by FastQC (v0.11.9), and compared using MultiQC (v1.11) ( 50 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### Core microRNAs regulate neural crest delamination and condensation in the developing trigeminal ganglion. (PNAS 2025)

- DOI: 10.1073/pnas.2517668122 | PMCID: PMC12704738 | PMID: 41329730
- Evidence: Sequencing quality was assessed with FastQC [v0.11.9, ( 37 )].
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [ComplexHeatmap v2.6.2] -> stage not stated [ImageJ v1.53, STRING db]

### An AINTEGUMENTA phosphoswitch controls bilateral stem cell activity during secondary growth. (PNAS 2025)

- DOI: 10.1073/pnas.2510538122 | PMCID: PMC12663975 | PMID: 41264254
- Evidence: Adaptors were removed with Trimmomatic using default parameters, and read quality was assessed with FastQC.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> quantification [R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3, emmeans] -> stage not stated [Galaxy, ggplot2 v3.4.3]

### Joubert syndrome 26 protein enforces compartmentalized motility of a ciliary kinesin. (PNAS 2025)

- DOI: 10.1073/pnas.2504374122 | PMCID: PMC12663925 | PMID: 41264249
- Evidence: Raw WGS reads were quality-controlled (FastQC), trimmed (Trim_galore v0.4.4) for adapters/low-quality bases, and aligned to WBcel235 via BWA-MEM2.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [FastQC] -> stage not stated [AlphaFold, ImageJ, SnpEff, freebayes v1.3.6]

### An ADAR2-mimic base editor for efficient C-to-U RNA editing in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2505269122 | PMCID: PMC12625888 | PMID: 41196347
- Version used: **0.12.1**
- Evidence: The quality control of sequencing data was conducted by using FastQC (v.0.12.1), and quality trimming was conducted by Trim Galore (v.0.6.10).
- Full pipeline: quality control [FastQC v0.12.1, Trim Galore v0.6.10] -> read trimming [FastQC v0.12.1, HISAT2, Trim Galore v0.6.10] -> alignment/mapping [HISAT2] -> stage not stated [SAMtools v1.21, SnpEff v5.2]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: 3.12.0) automatically performs quality control using FastQC, followed by read trimming with Trim Galore.
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### Symbiotic solutions for colony nutrition: Conserved nitrogen recycling within the bacterial pouch of &lt;i&gt;Tetraponera&lt;/i&gt; ants. (PNAS 2025)

- DOI: 10.1073/pnas.2514882122 | PMCID: PMC12595465 | PMID: 41150726
- Version used: **0.11.9**
- Evidence: Quality trimming of raw reads was done with Trimmomatic-0.39 ( 70 ), followed by read quality checks using FastQC v0.11.9 ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic] -> read trimming [FastQC v0.11.9, Trimmomatic] -> differential/statistical testing [QUAST] -> stage not stated [BLAST, Flye v2.9, RAxML v8.2.12]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **0.12.1**
- Evidence: Raw reads were processed using fastp (v0.23.4; poly-G trimming enabled, minimum length 150 bp, quality/N-content filtering) and assessed for quality (FastQC v0.12.1, MultiQC v1.23).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Version used: **0.11.5**
- Evidence: Raw read quality was assessed with FastQC v.
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### HIF2α negatively regulates MYCN protein levels and promotes a low-risk noradrenergic phenotype in neuroblastoma. (PNAS 2025)

- DOI: 10.1073/pnas.2516922122 | PMCID: PMC12582314 | PMID: 41118218
- Evidence: Paired-end RNA sequencing was performed by Novogene, and high-throughput sequencing data were processed for quality control, alignment, and differential expression analysis using a combination of established bioinformatics tools, such as FastQC, STAR, and DESeq2.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2, FastQC, GSEA] -> visualisation [UMAP] -> stage not stated [R, Scanpy, Seurat]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: The trimmed FASTQ files were analyzed and quality checked using FastQC program (v.0.11.8).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Quality control was performed with FastQC ( 52 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### Methanogenesis inhibition remodels microbial fermentation and stimulates acetogenesis in ruminants. (PNAS 2025)

- DOI: 10.1073/pnas.2514823122 | PMCID: PMC12541428 | PMID: 41052332
- Version used: **0.11.9**
- Evidence: Read quality assessment was performed using FastQC (v0.11.9) ( 87 ) coupled with MultiQC (v1.13) ( 88 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.13] -> alignment/mapping [Salmon v1.10.2] -> normalisation [seaborn] -> simulation/modelling [AlphaFold]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: FastQ files underwent quality control with FastQC ( 30 ) (v0.12.0) and adapter trimming with Skewer ( 31 ) (v0.2.2).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Loss of the ESX-5 secretion locus in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; reshapes the mycomembrane and enhances ESX-1 substrate secretion. (PNAS 2025)

- DOI: 10.1073/pnas.2509997122 | PMCID: PMC12435201 | PMID: 40901885
- Version used: **0.11.9**
- Evidence: BBDuk trimmer (Biomatters ltd.), and FastQC (v0.11.9) were used to trim and perform quality control on the reads.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Bowtie2 v7.2.2, FastQC v0.11.9] -> alignment/mapping [Bowtie2 v7.2.2] -> stage not stated [ImageJ]

### Shared metabolism between a bacterial and fungal species that reside in the human gut. (PNAS 2025)

- DOI: 10.1073/pnas.2504785122 | PMCID: PMC12415286 | PMID: 40854125
- Version used: **0.11.9**
- Evidence: FastQC (0.11.9) was used to perform quality checks of data ( 59 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.14] -> quantification [featureCounts v2.0.1] -> normalisation [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2]

### Coordinated actions of NLR-assembled and glutamate receptor-like calcium channels in plant effector-triggered immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2508018122 | PMCID: PMC12415192 | PMID: 40844808
- Evidence: Raw FASTQ files were quality-controlled by the FastQC tool (v0.11.9).
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT v7.505] -> stage not stated [ComplexHeatmap, DESeq2 v1.38.0, R, ggplot2 v3.4.2]

### Pervasive and recurrent hybridization prevents inbreeding in Europe's most threatened seabird. (PNAS 2025)

- DOI: 10.1073/pnas.2427223122 | PMCID: PMC12402992 | PMID: 40833417
- Version used: **0.11.7**
- Evidence: We performed quality control and removed adapter sequences in reads using FastQC v0.11.7 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and Trim Galore v0.4.5 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ), respectively.
- Full pipeline: quality control [FastQC v0.11.7, Trim Galore v0.4.5] -> read trimming [FastQC v0.11.7, Trim Galore v0.4.5] -> dimensionality reduction/clustering [ADMIXTURE, Rcpp] -> differential/statistical testing [ADMIXTURE, WhatsHap v1.5] -> visualisation [PLINK v1.90b] -> stage not stated [BEAST, R, SnpEff v5.1, VCFtools v0.1.15, minimap2 v2.11]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Evidence: The bcl files produced were demultiplexed into FASTQ files using Illumina’s bcl2fastq v2.19 (Illumina, San Diego, CA) and, after demultiplexing, the quality of the sequencing data was assessed by FastQC software.
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Version used: **0.12.1**
- Evidence: The trimmed reads were further quality-assessed using FastQC (version 0.12.1).
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Version used: **0.11.9**
- Evidence: The reads were first controlled for quality using FastQC v0.11.9.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Deficiency in transmitter release triggers homeostatic transcriptional changes that increase presynaptic excitability. (PNAS 2025)

- DOI: 10.1073/pnas.2322714122 | PMCID: PMC12337328 | PMID: 40729383
- Version used: **0.11.7**
- Evidence: As described recently ( 71 ), demultiplexed .fastq files were first analyzed with FastQC (ver 0.11.7) ( 79 ) to check for quality and trimmed with Trimmomatic (ver 0.38) ( 80 ).
- Full pipeline: quality control [FastQC v0.11.7, Trimmomatic v0.38] -> read trimming [FastQC v0.11.7, Trimmomatic v0.38] -> alignment/mapping [HISAT2 v2.1.0, featureCounts] -> normalisation [DESeq2 v1.26.0] -> visualisation [ggplot2 v3.2.1] -> stage not stated [R v4.1.0]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Version used: **0.11.9**
- Evidence: To prepare the whole genome data for analysis, read quality was checked with FastQC (v0.11.9) ( 95 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Thalamic CGRP neurons define a spinothalamic pathway for affective pain. (PNAS 2025)

- DOI: 10.1073/pnas.2505889122 | PMCID: PMC12280894 | PMID: 40632570
- Evidence: The FastQC package was utilized to evaluate the sequencing read quality.
- Full pipeline: quality control [FastQC] -> quantification [RSEM v1.2.28, ggplot2] -> visualisation [ggplot2]

### Human milk IgA promotes normal immune development by limiting Th17-inducing <i>Erysipelatoclostridium ramosum</i> in the infant gut. (PNAS 2025)

- DOI: 10.1073/pnas.2501030122 | PMCID: PMC12280908 | PMID: 40623174
- Evidence: FastQC and STAR were used for data processing and alignment, and the DESeq2 package was used in R for differential abundance analysis.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> quantification [DESeq2, FastQC, R] -> differential/statistical testing [DESeq2, FastQC, R] -> stage not stated [STRING db]

### Tandem ssDNA in neutrophil extracellular traps binds thrombin and regulates immunothrombosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418191122 | PMCID: PMC12260427 | PMID: 40608679
- Version used: **0.11.9**
- Evidence: The qualification of the samples is checked by FastQC (v0.11.9) ( 71 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.6] -> stage not stated [BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: We performed an initial quality control using FastQC to assess read quality.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### The role of estrogen receptor β in maintaining basal cells and modulating the immune environment in the prostate. (PNAS 2025)

- DOI: 10.1073/pnas.2505797122 | PMCID: PMC12232695 | PMID: 40549921
- Evidence: The FastQC package v0.11.2 was used to assess the read quality.
- Full pipeline: quality control [FastQC] -> alignment/mapping [TopHat v2.0.9]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: To analyze the bulk ATAC-seq datasets, FastQC was used to perform initial quality checks after sequencing.
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Methane-powered sea spiders: Diverse, epibiotic methanotrophs serve as a source of nutrition for deep-sea methane seep &lt;i&gt;Sericosura&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2501422122 | PMCID: PMC12232434 | PMID: 40523202
- Version used: **1.13**
- Evidence: FastQC v1.13 was used to quality control the raw sequence data and identify trim cutoffs for both the forward and reverse reads, ahead of pairing.
- Full pipeline: quality control [FastQC v1.13] -> read trimming [DADA2] -> stage not stated [tidyverse]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: Raw read quality was examined using FastQC ( 51 ), and the quality trimming was performed using BBduk ( 52 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### BRD9 functions as an HIV-1 latency regulatory factor. (PNAS 2025)

- DOI: 10.1073/pnas.2418467122 | PMCID: PMC12130862 | PMID: 40402245
- Evidence: The RNA sequencing data underwent quality control by FastQC, followed by reads filtering, reads alignment, and mapping onto human reference genome using the Bowtie2 program.
- Full pipeline: quality control [Bowtie2, FastQC] -> alignment/mapping [Bowtie2, FastQC] -> stage not stated [GSEA]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Evidence: Reads were demultiplexed with CASAVA (Illumina, San Diego, CA) and read quality was assessed using FastQC ( 93 ) and MultiQC ( 94 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Evidence: Quality control of the ChIP-Seq reads was performed using FastQC in default settings.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Version used: **0.11.5**
- Evidence: We verified read quality before and after the processing with FastQC (v.0.11.5; 62 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### A conserved ARF-DNA interface underlies auxin-triggered transcriptional response. (PNAS 2025)

- DOI: 10.1073/pnas.2501915122 | PMCID: PMC12002309 | PMID: 40168121
- Evidence: Obtained raw fastq reads were quality controlled using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [featureCounts] -> quantification [ilastik v1.3.3] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, HMMER, PyMOL]

### Nuclear Galectin-1 promotes &lt;i&gt;KRAS&lt;/i&gt;-dependent activation of pancreatic cancer stellate cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424051122 | PMCID: PMC12002210 | PMID: 40172967
- Evidence: The quality of immunoprecipitated DNA reads was assessed with the FastQC tool, considering only reads with a quality score above 30 for downstream analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2]

### Pulsatile flow induces chromatin interaction with lamin-associated proteins to enrich H3K9 methylation in endothelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424566122 | PMCID: PMC11962468 | PMID: 40117319
- Evidence: Quality scores were assessed using FastQC.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [HOMER, ImageJ, MACS2, OpenCV]

### Red-light signaling pathway activates desert cyanobacteria to prepare for desiccation tolerance. (PNAS 2025)

- DOI: 10.1073/pnas.2502034122 | PMCID: PMC11962455 | PMID: 40112114
- Version used: **0.11.4**
- Evidence: Briefly, quality control was performed using FastQC v0.11.4, and rRNA sequences were removed with SortMeRNA v1.9.
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [edgeR v3.20.7] -> dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [edgeR v3.20.7] -> stage not stated [AlphaFold, PyMOL]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Version used: **0.11.8**
- Evidence: Quality control was conducted with FastQC v 0.11.8 ( 114 ), Qualimap v.2.2.1 ( 115 ), and MultiQC version 1.1 ( 116 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Version used: **0.11.9**
- Evidence: All reads were analyzed with FastQC v0.11.9 ( 76 ) and 10 bp were trimmed using BBduk in BBTools v38.18 ( 77 ).
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### Coronavirus endoribonuclease antagonizes ZBP1-mediated necroptosis and delays multiple cell death pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2419620122 | PMCID: PMC11912388 | PMID: 40035769
- Evidence: Raw read quality was examined using FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [FastQC]

### Abscisic acid signaling gates salt-induced responses of plant roots. (PNAS 2025)

- DOI: 10.1073/pnas.2406373122 | PMCID: PMC11831169 | PMID: 39908104
- Evidence: First read quality was analyzed with FastQC ( 56 ) and MultiQC ( 57 ) packages in Python 2.7, followed by trimming of low quality reads with Trim Galore!
- Full pipeline: quality control [FastQC, MultiQC, Python v2.7, Trim Galore] -> read trimming [FastQC, MultiQC, Python v2.7, Trim Galore] -> alignment/mapping [pheatmap] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, R] -> stage not stated [OpenCV v4.5.1.48]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: The RNA sequence was subjected to quality control (FastQC, a quality control tool for high-throughput sequence data and available online at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc ), and trimmomatic (0.37; https://github.com/timflutre/trimmomatic ) to remove adapters, followed by alignment to the human genome (GRCh38) using HISAT2.2 ( https://daehwankimlab.github.io/hisat2/ ).
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Evidence: ...s ( 61 ) (v1.13), star ( 62 ) (v2.6.1d), stringtie ( 63 ) (v2.1.7), Trimgalore (v0.6.7, GitHub—FelixKrueger/TrimGalore: A wrapper around Cutadapt and FastQC to consistently apply adapter and quality trimming to FastQ files, with extra functionality for RRBS data), cutadapt ( 64 ) (v3.4) and ucsc (v377).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Evidence: Sequencing data were assessed using FastQC (Babraham Bioinformatics, Cambridge, UK) and then mapped to the mouse genome (UCSC mm10) using STAR RNA-seq aligner with the parameter: “—outSAMmapqUNIQUE 60”.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### Ultrarapid MC1R protein and associated plumage color evolution in the domestic chicken. (PNAS 2026)

- DOI: 10.1073/pnas.2605288123 | PMCID: PMC13273276 | PMID: 42268884
- Version used: **0.11.8**
- Evidence: Raw sequencing reads were quality-checked with FastQC (version 0.11.8).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [BWA v0.7.17] -> registration [GATK v3.7] -> stage not stated [Picard v2.18.6, PyMOL, SAMtools v1.9, VCFtools v0.1.16]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Version used: **0.11.9**
- Evidence: FastQC version 0.11.9 was used to determine the quality of fastq read files.
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Version used: **0.11.9**
- Evidence: Short read quality was assessed using FastQC v0.11.9 ( 76 ) and reads were trimmed using Trimmomatic v0.39 ( 77 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Version used: **0.11.5**
- Evidence: File assessment before and after quality control was performed using FastQC (v0.11.5).
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Version used: **0.11.9**
- Evidence: The quality of the raw sequencing data was checked with FastQC v.0.11.9 ( 66 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### KLF2 overrides the resident memory CD8 T cell differentiation program, in opposition to KLF3. (PNAS 2026)

- DOI: 10.1073/pnas.2533700123 | PMCID: PMC13037849 | PMID: 41871244
- Version used: **0.12.1**
- Evidence: FastQC v0.12.1 ( 65 ) was used to generate sequence quality reports for raw and trimmed reads. featureCounts v2.0.6 ( 66 ) was used to count mapped reads to genes.
- Full pipeline: quality control [FastQC v0.12.1, featureCounts v2.0.6] -> read trimming [FastQC v0.12.1, featureCounts v2.0.6] -> alignment/mapping [FastQC v0.12.1, featureCounts v2.0.6] -> differential/statistical testing [GSEA] -> stage not stated [HOMER v4.9.1, deepTools v3.3.0]

### Mild SARS-CoV-2 maternal infection in mice induces transient offspring neurodevelopmental aberrance. (PNAS 2026)

- DOI: 10.1073/pnas.2518294123 | PMCID: PMC13012083 | PMID: 41849379
- Version used: **0.11.9**
- Evidence: Quality control on FASTQ reads was performed using FastQC (version 0.11.9) and a threshold set for 95% of bases meeting Q30 within a given read to ensure high sequencing quality.
- Full pipeline: quality control [FastQC v0.11.9] -> dimensionality reduction/clustering [clusterProfiler v4.10.0] -> differential/statistical testing [limma v3.58.1] -> visualisation [ggplot2 v3.5.2] -> stage not stated [R v4.3.2]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Version used: **0.11.9**
- Evidence: Quality control was applied to ChIP raw sequencing data using FastQC v0.11.9 ( 49 ), followed by trimming adaptors and low-quality reads with Trim Galore! v0.6.7 ( 50 ).
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **0.12.1**
- Evidence: The quality of filtered reads was assessed with FastQC v.0.12.1 ( 61 ).
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### Early colonization before inundation consistent with northern glacial refugia in Southern Doggerland revealed by sedimentary ancient DNA. (PNAS 2026)

- DOI: 10.1073/pnas.2508402123 | PMCID: PMC12994208 | PMID: 41805578
- Version used: **0.11.6**
- Evidence: FastQC version 0.11.6 ( 75 ) was used to visually assess the success of adapter and quality trimming.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [FastQC v0.11.6] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BLAST]

### The Nemp1-Nesprin complex mediates cellular responses to matrix mechanics. (PNAS 2026)

- DOI: 10.1073/pnas.2521253123 | PMCID: PMC12956887 | PMID: 41730104
- Version used: **0.11.9**
- Evidence: Quality control of the RNA-seq reads was performed using FastQC v.0.11.9.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [Salmon v1.8.0] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [R, clusterProfiler v4.10.1, edgeR] -> visualisation [pheatmap v1.0.12]

### Foliar dewdroplet-induced redox cascades promote early flowering in &lt;i&gt;Brassicaceae&lt;/i&gt; plants. (PNAS 2026)

- DOI: 10.1073/pnas.2527021123 | PMCID: PMC12933091 | PMID: 41701847
- Evidence: Data were processed using FastQC, Bowtie2, MACS2, and DESeq2.
- Full pipeline: quality control [Bowtie2, DESeq2, FastQC, MACS2] -> stage not stated [WGCNA]

### Early life-stage thermal resilience is determined by climate-linked regulatory variation. (PNAS 2026)

- DOI: 10.1073/pnas.2518358123 | PMCID: PMC12799179 | PMID: 41505517
- Version used: **0.11.7**
- Evidence: We checked the quality of paired-end raw sequence reads using FastQC (v.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Salmon v0.14.1] -> quantification [Salmon v0.14.1] -> stage not stated [DESeq2, R, SAMtools v1.10]

### Combination antiviral and anti-inflammatory therapy mitigates persistent neurological deficits in mice post SARS-CoV-2 infection. (PNAS 2026)

- DOI: 10.1073/pnas.2530209123 | PMCID: PMC12799161 | PMID: 41499397
- Evidence: 2 × 50 bp FastQ paired end reads for 8 samples (n = 39.6 Million average reads per sample) were trimmed using Trimmomatic (v 0.33) enabled with the optional “-q” option; 3 bp sliding-window trimming from 3′ end requiring minimum Q3Quality control on raw sequence data for each sample were performed with FastQC.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.5, Seurat v5.3.0, pheatmap]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Evidence: After sequencing, FASTQ files were examined using FastQC (Version 0.11.9) and multiqc (Version 1.9).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### Cortical wiring by synapse type-specific control of local protein synthesis. (Science 2022)

- DOI: 10.1126/science.abm7466 | PMCID: PMC7618116 | PMID: 36423280
- Evidence: Sequencing, data analysis, reads repartition, and insert size estimation were performed using FastQC, Picard-Tools, Samtools and rseqc.
- Full pipeline: quality control [FastQC, Picard, SAMtools] -> alignment/mapping [STAR v2.4.0] -> quantification [R v3.2] -> normalisation [R v3.2] -> differential/statistical testing [DESeq2, R v3.2] -> stage not stated [ImageJ]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Version used: **0.11.4**
- Evidence: The quality of the sequencing reads was examined using FastQC (v0.11.4).
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **0.11.7**
- Evidence: ChIP-Seq analysis Input and H2A.Z and acetyl-H2A.Z (H2A.Zac) ChIP-seq raw reads were quality-checked with FastQC (v0.11.7) ( 110 ) and aligned onto the human genome (hg38 assembly) using Bowtie2 (v2.4.5) ( 111 ) with the following options:–local –very-sensitive-local –no-unal –no-mixed –no-discordant –phred33 -I 10 -X 700.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Version used: **0.11.8**
- Evidence: Data pre-processing Quality control of all fastq files was conducted by running FastQC (v0.11.8)( 68 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Microglia Rank signaling regulates GnRH neuronal function and the hypothalamic-pituitary-gonadal axis. (Science 2026)

- DOI: 10.1126/science.aeb6999 | PMCID: PMC7619046 | PMID: 41818388
- Evidence: Data processing, normalization, and clustering annotations Bollito ( 98 ) pipeline was employed to perform initial steps of the analysis as follows: sequencing quality was checked with FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ); reads were aligned to the mouse reference genome (GRC39m from GENCODE ( 99 )) with STARsolo (STAR v2.7.1) ( 100 ); Seurat v3.2.3 ( 101 ) software...
- Full pipeline: quality control [FastQC, STAR v2.7.1] -> alignment/mapping [FastQC, GATK, STAR v2.7.1] -> normalisation [FastQC, STAR v2.7.1] -> dimensionality reduction/clustering [FastQC, ImageJ, STAR v2.7.1, UMAP] -> stage not stated [GSEA, Seurat]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: FastQC was used to check the quality of fastq files.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: RNA-seq data processing pipeline: Adaptors were first trimmed from raw sequencing FastQ files using Cutadapt (version 3.1) for removing the last 122 bases of each Read 1 sequence (with parameters -u -122) followed by quality assessment using FastQC.
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Evidence: Sequencing quality of fastq files was evaluated with FastQC, and adaptors were trimmed using Cutadapt (1.18).
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: Adapter trimming, low-quality sequence removal, and quality control were performed using Cutadapt and FastQC, respectively, both of which are incorporated within Trim Galore (v0.6.6) ( 99 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Version used: **0.12.1**
- Evidence: FASTQ files were processed for quality control using FastQC (v0.12.1) to assess sequence quality.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

