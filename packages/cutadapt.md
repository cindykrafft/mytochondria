# Cutadapt

- **Category:** genomics
- **Papers in survey:** 331
- **Journals:** Nature (150), PNAS (145), Cell (28), Science (8)
- **Years:** 2021 (35), 2022 (44), 2023 (56), 2024 (78), 2025 (80), 2026 (38)
- **Versions named:** 1.18 (20), 4.1 (17), 3.4 (15), 1.15 (8), 2.8 (8), 2.6 (6), 2.10 (6), 2.1 (6), 2.3 (5), 2.5 (5)
- **Pipeline stages it appears in:** read trimming (261), alignment/mapping (78), quality control (50), quantification (10), variant calling (5), visualisation (2), structure determination (1), registration (1), differential/statistical testing (1), dimensionality reduction/clustering (1)

## Papers

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Evidence: Analysis of pAseq data Gene expression analysis To quantify gene expression using the pAseq data we trimmed Illumina adapters, low-quality positions (Phred score < 10) and polyA tails using Cutadapt ( Martin, 2011 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### Splice site m<sup>6</sup>A methylation prevents binding of U2AF35 to inhibit RNA splicing. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.062 | PMCID: PMC8208822 | PMID: 33930289
- Evidence: ...355 S. pombe U2AF35 cDNA This study NP_594945.1 , NM_001020376.2 S. pombe U2AF65 cDNA This study NP_595396.1 , NM_001021303.2 Software and algorithms Cutadapt https://doi.org/10.14806/ej.17.1.200 MEME - Motif discovery tool Bailey and Elkan, 1994 https://meme-suite.org/meme/ WebLogo http://weblogo.berkeley.edu/ R R Core Team, 2017 https://www.r-project.org Bowtie Langmead et al., 2009 http://bowti...
- Full pipeline: stage not stated [Bioconductor, Cutadapt, DESeq2, MACS2, R]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Evidence: Adaptors were trimmed with the read trimmer Atropos (version 1.1.25) ( Didion et al., 2017 ), a variant of Cutadapt, and aligned to the mm10 genome using the aligner Bowtie2 (version 2.3.5.1) ( Langmead and Salzberg, 2012 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...ham.ac.uk/projects/hicup/ CHiCAGO Cairns et al., 2016 https://bioconductor.org/packages/release/bioc/html/Chicago.html Graphpad Prism 8.0 Graphpad NA Cutadapt Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ Limma Ritchie et al., 2015 https://bioconductor.org/packages/release/bioc/html/limma.html clusterProfiler Yu et al., 2012 https://bioconductor.org/packages/release/bioc/html/clusterProf...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### An early cell shape transition drives evolutionary expansion of the human forebrain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.050 | PMCID: PMC8054913 | PMID: 33765444
- Version used: **2.4**
- Evidence: ...agej.net/MaMuT PRAGUI MRC LMB https://github.com/lmb-seq/PRAGUI Trim Galore! v0.6.3 Krueger, 2012 https://github.com/FelixKrueger/TrimGalore/releases Cutadapt v2.4 Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ FASTQC v0.11.5 Andrews, 2010 https://github.com/s-andrews/FastQC HISAT2 v2.0.0-beta Kim et al., 2015 http://daehwankimlab.github.io/hisat2/ HTSeq v0.11.2 Anders et al., 2015 https:...
- Full pipeline: quality control [Cutadapt v2.4, FastQC, HISAT2 v2.0.0, HTSeq v0.11.2, Trim Galore] -> stage not stated [R v3.5]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...omega AS1630 Software and algorithms OxCal Ramsey and Lee, 2013 https://c14.arch.ox.ac.uk/oxcal.html CutAdapt Martin, 2011 https://github.com/marcelm/cutadapt FastQC Andrews, 2010 https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ BWA Li and Durbin, 2010 http://bio-bwa.sourceforge.net/ Picard MarkDuplicates http://broadinstitute.github.io/picard http://broadinstitute.github.io/picard MapDa...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: ...2008 RRID: SCR_014485 Perseus Tyanova and Cox, 2018 RRID: SCR_015753 STAR aligner Dobin et al., 2013 RRID: SCR_015899 CellRanger N/A RRID: SCR_017344 Cutadapt Martin, 2011 RRID: SCR_011841 RNA-SeQC DeLuca et al., 2012 RRID: SCR_005120 RSEM Li and Dewey, 2011 RRID: SCR_013027 Scanpy Wolf et al., 2018 RRID: SCR_018139 Bioconductor R Huber et al., 2015 RRID: SCR_001905 Bioconductor packages edgeR Rob...
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Soluble ACE2-mediated cell entry of SARS-CoV-2 via interaction with proteins related to the renin-angiotensin system. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.053 | PMCID: PMC7923941 | PMID: 33713620
- Evidence: ...al., 2007 https://david.ncifcrf.gov/tools.jsp PANTHER (Protein Analysis Through Evolutionary Relationships) Mi et al., 2019 http://www.pantherdb.org/ Cutadapt Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ Bowtie2 Langmead and Salzberg, 2012 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml HTSeq Anders et al., 2015 https://htseq.readthedocs.io/en/master/ DESeq2 Love et al., 2014 http...
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> stage not stated [Bowtie2, Cutadapt, DESeq2, HTSeq]

### Osteoclasts recycle via osteomorphs during RANKL-stimulated bone resorption. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.002 | PMCID: PMC7938889 | PMID: 33636130
- Evidence: ...SCR_019214 biovizBase ( Yin and Cook, 2020 ) https://bioconductor.org/packages/release/bioc/html/biovizBase.html CTAn Skyscan https://www.bruker.com/ Cutadapt ( Martin, 2011 ) https://cutadapt.readthedocs.io/en/stable/ ; RRID: SCR_011841 Drishti-2.4 ( Limaye, 2012 ) https://github.com/nci/drishti ; RRID: SCR_017999 FIJI ( Schindelin et al., 2012 ) https://imagej.net/Fiji ; RRID: SCR_002285 FlowJo ...
- Full pipeline: alignment/mapping [STAR v2.4.1] -> normalisation [STAR v2.4.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [RSEM, STAR v2.4.1] -> stage not stated [Cutadapt, ImageJ, MAGMA, ggplot2]

### Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.030 | PMCID: PMC7584921 | PMID: 33147445
- Version used: **1.13**
- Evidence: We performed adaptor trimming by treating the hU6 promoter sequence as a 5′ adaptor, using cutadapt v1.13 [-e 0.2 -O 5 -m 20 -g TCTTGTGGAAAGGACGAAACACCG].
- Full pipeline: read trimming [Cutadapt v1.13] -> alignment/mapping [STAR] -> stage not stated [DESeq2, GSEA, R, Seurat, fgsea]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Evidence: ...03 Addgene Cat#8454 pLenti6/V5-DEST-HMGB1 Scott et al., 2011 Addgene Cat#31208 Software and Algorithms Bowtie2 v2.2.9 Langmead and Salzberg, 2012 N/A Cutadapt Martin, 2011 N/A DESeq2 v1.32 Love et al., 2014 N/A deeptools v3.1.3 Ramírez et al., 2016 N/A Flowjo 10.6.2 FLOWJO https://www.flowjo.com Graphpad Prism 8 Graphpad software https://www.graphpad.com/scientific-software/prism/ MACS2 Zhang et a...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: ATAC-seq analysis Raw sequencing fastq files were processed using cutadapt ( Martin, 2011 ) for adapter trimming, Bowtie2 { Langmead, 2012 #2898) for mapping, SAMtools ( Li et al., 2009 ) for filtering, sorting and removing duplicates, and deepTools ( Ramírez et al., 2016 ) for generating coverage tracks.
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **1.17**
- Evidence: ...co.ezlab.org/ Mfannot N/A https://github.com/BFL-lab/Mfannot PEAR version 0.9.10 Zhang et al., 2014 https://cme.h-its.org/exelixis/web/software/pear/ cutadapt version 1.17 Martin, 2011 https://cutadapt.readthedocs.io/en/v1.17/ QIIME 2 version 2018.8 Bolyen et al., 2019 https://qiime2.org/ ITSx version 1.1b1 ( Bengtsson-Palme and Ryberg, 2013 https://microbiology.se/software/itsx/ R version 4.03 R ...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: ...aper (cohort 1) Zenodo:10.5281/zenodo.5771937 CellRanger 10x genomics v3.1.0 and v5.0.0 Bcl2fastq2 Illumina v2.20 STAR ( Dobin et al., 2013 ) v2.6.1b Cutadapt ( Martin, 2011 ) v1.16 Dropseq-tools https://github.com/broadinstitute/Drop-seq/ v2.0.0 R https://www.cran.r-project.org v3.6.2; v4.0.3 Seurat (R package) ( Butler et al., 2018 ; Hafemeister and Satija, 2019 ; Stuart et al., 2019 ) v3.1.4; v...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: Non-aligning reads were trimmed using Cutadapt trimgalore and then realigned to the mm9 genome using bowtie2.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### Systematic identification and characterization of genes in the regulation and biogenesis of photosynthetic machinery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.007 | PMCID: PMC10760936 | PMID: 38065083
- Evidence: The sequencing data were analyzed by Cutadapt, Bowtie 2, and python.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [SciPy] -> stage not stated [AlphaFold, Cutadapt, PyMOL]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: Data analysis and statistics Analysis of ribosome footprinting NGS data: Adapter poly-A sequence nucleotides were trimmed from raw reads with cutadapt ( https://doi.org/10.14806/ej.17.1.200 ).
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Version used: **1.18**
- Evidence: Paired-end sequencing reads were adapter- and quality trimmed using cutadapt (v1.18).
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: RNA-seq analysis Raw bulk RNA-seq reads from knockdown experiments and wild-type chimpanzee and human iPSCs were adapter-trimmed using cutadapt 125 (with option -b AGATCGGAAGAGCACACGTCTGAACTCCAGTCA) and then pseudo-aligned to species-specific transcriptomes using kallisto 126 with options --single -l 200 -s 20.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: Mapping of RNA-seq reads to bat genomes and quantifying expression of ERVs To trim adapters and generate quality metrics of the fastq files, we used Trimmgalore v.0.6.6 ( https://github.com/FelixKrueger/Trim-Galore ), a wrapper for Cutadapt ( https://github.com/marcelm/cutadapt ) and FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ).
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### A bat MERS-like coronavirus circulates in pangolins and utilizes human DPP4 and host proteases for cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.019 | PMCID: PMC9933427 | PMID: 36803605
- Version used: **1.18**
- Evidence: ...smid: pCMV-3Tag-8-ORF5 This paper N/A Plasmid: pCMV-3Tag-8-ORF8b This paper N/A Plasmid: pREN2-MjHKU4r-CoV-1 N This paper N/A Software and algorithms Cutadapt (v1.18) Kechin et al.
- Full pipeline: stage not stated [BWA v0.7.12, Cutadapt v1.18, IQ-TREE v1.6.1, ImageJ, Pangolin]

### Alarming antibody evasion properties of rising SARS-CoV-2 BQ and XBB subvariants. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.018 | PMCID: PMC9747694 | PMID: 36580913
- Version used: **2.1**
- Evidence: 43 RRID: Addgene_154104 Software and algorithms Cutadapt v2.1 Martin 44 https://cutadapt.readthedocs.io/en/v2.1/ Bowtie2 v2.3.4 Langmead et al.
- Full pipeline: stage not stated [Bowtie2 v2.3.4, Cutadapt v2.1, PyMOL v2.3.2]

### Vertebrate centromeres in mitosis are functionally bipartite structures stabilized by cohesin. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.014 | PMCID: PMC11164432 | PMID: 38744280
- Version used: **1.18**
- Evidence: 51bp paired end reads were trimmed with Cutadapt v1.18 to remove adapters and low quality sequence with the parameters --minimum-length 20 --nextseq-trim=20.
- Full pipeline: read trimming [BWA v0.7.16, Cutadapt v1.18, ImageJ, LAMMPS, Trimmomatic v0.36, deepTools] -> stage not stated [Snakemake]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: ...A-seq data processing Quality control of SMART-Seq datasets was performed by FastQC ( http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and Cutadapt 52 to remove adaptor sequences and low-quality regions.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: 28 PTaq RNA-Seq library data processing Inline demultiplexing, mapping to the H37Rv ( NC_000962.3 ) genome, and quality control was conducted with a pipeline built on cutadapt and bowtie2 .
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Evidence: The code uses FastQC version v0.11.8 129 for sequence quality control before and after adaptor removal, cutadapt 130 version 3.5 with Python 3.7.12 for adaptor removal, SAMtools 131 version 1.9 for indexing, bwa 132 version 0.7.17-r1188 for mapping.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### Principles of cotranslational mitochondrial protein import. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.021 | PMCID: PMC12396113 | PMID: 40795856
- Version used: **4.1**
- Evidence: Briefly, 3’ adaptor sequences were trimmed from sequencing reads with Cutadapt v4.1 56 using the following command: cutadapt –cores=0 -q20 -m24 -M42 –discard-untrimmed -O6 –no-indels -a adaptor_sequence -o outfile.fastq.gz infile.fastq.gz 1> Cutadapt_report.txt Unique molecular identifiers (UMIs, two random 5’ nucleotides and five random 3’ nucleotides) were trimmed from each read using a Julia sc...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.5, STAR v2.7.10a] -> stage not stated [AlphaFold, ColabFold]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **1.14**
- Evidence: Read pairs were trimmed using cutadapt 1.14.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: In brief, after importing demultiplexed reads into QIIME2, primer sequences were removed using cutadapt 52 and read pairs were joined using vsearch 53 .
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Transposon-associated TnpB is a programmable RNA-guided DNA endonuclease. (Nature 2021)

- DOI: 10.1038/s41586-021-04058-1 | PMCID: PMC8612924 | PMID: 34619744
- Evidence: The pair-end reads shorter than 20 bp were filtered with Cutadapt 34 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [AlphaFold, Cutadapt, Python]

### Biologically informed deep neural network for prostate cancer discovery. (Nature 2021)

- DOI: 10.1038/s41586-021-03922-4 | PMCID: PMC8514339 | PMID: 34552244
- Version used: **2.2**
- Evidence: Adapters were trimmed with cutadapt v2.2 and reads were aligned using STAR aligner v2.7.2b 48 , 49 .
- Full pipeline: read trimming [Cutadapt v2.2, STAR] -> alignment/mapping [Cutadapt v2.2, RSEM, STAR] -> quantification [RSEM] -> stage not stated [SAMtools]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **2.8**
- Evidence: For the archaeological samples, short reads of fewer than 30 bp were removed using Cutadapt (v.2.8) 62 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Mapping, peak calling and dynamic peak calling: Fastq files were trimmed with trimGalore and cutadapt 49 , and the filtered, pair-ended reads were aligned to mm9 with bowtie2 50 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### IgA transcytosis and antigen recognition govern ovarian cancer immunity. (Nature 2021)

- DOI: 10.1038/s41586-020-03144-0 | PMCID: PMC7969354 | PMID: 33536615
- Evidence: Paired-end RNA-seq reads were aligned to the GRCh37 human reference genome using STAR 24 (v.2.5.3a) following adaptor trimming by cutadapt 25 (v.1.8.1).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, HTSeq, STAR] -> normalisation [HTSeq] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [GSEA, R v3.6.1]

### Arterialization requires the timely suppression of cell growth. (Nature 2021)

- DOI: 10.1038/s41586-020-3018-x | PMCID: PMC7116692 | PMID: 33299176
- Evidence: Sequencing reads were processed with a pipeline that used FastQC v0.11.5 (Babraham Bioinformatics, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) to evaluate their quality, and cutadapt 35 to trim sequencing reads, thus eliminating Illumina and SMARTer adaptor remains, and discard reads shorter than 30 bp.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5] -> alignment/mapping [RSEM v1.2.30] -> normalisation [limma v3.32.10] -> differential/statistical testing [limma v3.32.10] -> stage not stated [GSEA, ImageJ]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: For the childhood brain tumour, read 2 was trimmed to remove both the TSO adaptor sequence and poly(A) homopolymers using Cutadapt 36 .
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Version used: **3.4**
- Evidence: The quality of the resulting data was assessed using FastQC v0.11.8 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), and reads were subsequently quality and adaptor trimmed using cutadapt (v3.4) 50 with stringent settings to remove error-containing reads (‘-q 20 --max-n 0 --max-ee 1’).
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### Nuclear chromosome locations dictate segregation error frequencies. (Nature 2022)

- DOI: 10.1038/s41586-022-04938-0 | PMCID: PMC9300461 | PMID: 35831506
- Version used: **1.16**
- Evidence: Raw reads were demultiplexed by their library-specific index and sample-specific DamID barcode, universal DamID adaptor sequence was trimmed with cutadapt (v.1.16) and reads were aligned to reference genome hg19 using bowtie2 (v.2.3.4).
- Full pipeline: read trimming [Bowtie2 v2.3.4, Cutadapt v1.16] -> alignment/mapping [Bowtie2 v2.3.4, Cutadapt v1.16] -> quantification [Fiji v2.0.0, ImageJ v2.0.0]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Bioinformatics and data analysis CUT&RUN data processing Paired-end reads were trimmed to remove Illumina adapters and low-quality basecalls (cutadapt -q 30) 58 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: Mapping of piggyBac-enhancer insertion sites by tagmentation Before aligning paired-end sequencing reads, reads were filtered using an adaptation of cutadapt 63 , processing each read pair in multiple steps.
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### Phage anti-CBASS and anti-Pycsar nucleases subvert bacterial immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-04716-y | PMCID: PMC9117128 | PMID: 35395152
- Version used: **2.8**
- Evidence: Following Illumina sequencing, adapter sequences were removed from the reads using Cutadapt version 2.8 (ref.
- Full pipeline: read trimming [Cutadapt v2.8, SPAdes] -> visualisation [PyMOL v2.3.0] -> stage not stated [BLAST, IQ-TREE, PHENIX]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Version used: **2.3**
- Evidence: After adapter and quality trimming with cutadapt (version 2.3) and removing duplicates with samtools markdup (version 1.10), reads were aligned to the TAIR10 reference genome with bwa-mem (version 0.7.17) and variants were called independently for each sample with GATK HaplotypeCaller version 4.1.0.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: Bioinformatics data processing and analyses were performed using Bash (v4.2.46), R (v3.6) and Python (v3.8.5) programming languages as well as the following tools: FastQC (Babraham Bioinformatics) (v0.11.7) cutadapt 37 (v1.16), HISAT2 38 (v2.1.0), SAMtools 39 (v1.9), sambamba 40 (v0.6.6) and deepTools 41 (v3.1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Version used: **2.10**
- Evidence: Specifically, the main mapping steps include (1) demultiplexing FASTQ files into single cells (cutadapt, v.2.10); (2) read-level quality control; (3) mapping (one-pass mapping for snmC, two-pass mapping for snm3C) (bismark v.0.20, bowtie2 v.2.3); (4) BAM file processing and quality control (samtools v.1.9, picard v.3.0.0); (5) methylome profile generation (ALLCools v.1.0.8); and (6) chromatin cont...
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Specifically, the main mapping protocol included the following steps: (1) demultiplexing FASTQ files into single cells (cutadapt 61 , v.2.10); (2) read-level QC; (3) mapping (one-pass mapping for snmC, two-pass mapping for snm3C) (bismark 62 , v.0.20; bowtie2 (ref.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Version used: **4.0**
- Evidence: CUT&Tag data processing and analysis Reads were trimmed using cutadapt (v.4.0) to remove Illumina adapter sequences and subsequently mapped to the reference genome with bowtie2 (v.2.4.5).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Version used: **4.0**
- Evidence: Next-generation sequencing data analysis The raw sequence reads in FastQ format were cleaned of adapter sequences and size-selected for 18–35-nucleotide inserts (plus 8 random adapter bases) using Cutadapt v.4.0 ( http://cutadapt.readthedocs.org ) with the parameters ‘-a TGGAATTCTCGGGTGCCAAGG -m 26 -M 43’.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Evidence: All primers used can also be found in Supplementary Table 1 . gRNA and UCB recovery and analyses gRNA sequences were extracted by cutting 5′- and 3′-flanking regions with cutadapt (10% error rate, 1–3 nucleotide (nt) overlap, no indels) 58 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Evidence: Specifically, raw reads were trimmed using Trim Galore v.0.6.6, a wrapper tool of Cutadapt 53 and FastQC 54 .
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Version used: **1.18**
- Evidence: Fastq files were assessed using FastQC (v.0.11.9) and Illumina sequencing adapters were trimmed from reads using cutadapt (v.1.18).
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Evidence: Reads were trimmed using Cutadapt for poly(A) and adaptors before mapping.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Version used: **3.1**
- Evidence: For RNA processing, this involved removal of accessible chromatin contaminating reads using cutadapt (v.3.1) 51 , dropEst (v.0.8.6) 52 to extract cell barcodes and STAR (version 2.5.2b) 53 to align tagged reads to the genome (GRCh38).
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Mega-scale experimental analysis of protein folding stability in biology and design. (Nature 2023)

- DOI: 10.1038/s41586-023-06328-6 | PMCID: PMC10412457 | PMID: 37468638
- Evidence: Following sequencing, reads were paired using the PEAR program 56 then the adapter sequences were moved by Cutadapt 57 .
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [AlphaFold, Python v3.9]

### Evolution of a minimal cell. (Nature 2023)

- DOI: 10.1038/s41586-023-06288-x | PMCID: PMC10396959 | PMID: 37407813
- Evidence: Whole-genome sequencing reads were quality controlled using cutadapt 48 to trim low-quality base pairs and remove residual adapter sequences.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> simulation/modelling [Python] -> stage not stated [ImageJ, R]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Version used: **2.4**
- Evidence: After sequencing, raw reads were subjected to adapter and quality trimming using cutadapt (version 2.4; parameters: --quality-cutoff 20 --overlap 5 --minimum-length 25; Illumina TruSeq adapter clipped from both reads), followed by trimming of 10 and 5 nucleotides from the 5′ and 3′ end of the first read and 15 and 5 nucleotides from the 5′ and 3′ end of the second read.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Single-cell quantification of ribosome occupancy in early mouse development. (Nature 2023)

- DOI: 10.1038/s41586-023-06228-9 | PMCID: PMC10307641 | PMID: 37344592
- Evidence: Next, we clipped the 3′ adapter AAAAAAAAAACAAAAAAAAAA, from the Ribo-ITP data, using cutadapt 63 version 1.18 with the parameters “-a AAAAAAAAAACAAAAAAAAAA–overlap=4–trimmed-only”.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ, R v4.0, Seurat]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Version used: **1.12**
- Evidence: Adaptors and DNA spike-ins were removed from the forward and reverse reads using cutadapt (v.1.12) 81 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Engineered tRNAs suppress nonsense mutations in cells and in vivo. (Nature 2023)

- DOI: 10.1038/s41586-023-06133-1 | PMCID: PMC10284701 | PMID: 37258671
- Version used: **1.8.3**
- Evidence: Adapter sequences were removed by cutadapt (1.8.3) with a minimal overlap of 1 nt.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> stage not stated [Python]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Version used: **3.0**
- Evidence: Next, RNA-seq reads were trimmed on the 3′ ends to remove the Illumina adaptor (AGA TCG GAA GAG CAC ACG TCT GAA CTC CAG TCA C) using Cutadapt 3.0 (ref.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### Tree islands enhance biodiversity and functioning in oil palm landscapes. (Nature 2023)

- DOI: 10.1038/s41586-023-06086-5 | PMCID: PMC10247383 | PMID: 37225981
- Version used: **2.5**
- Evidence: Remaining primer sequences were clipped with cutadapt v.2.5 (ref.
- Full pipeline: stage not stated [BLAST v2.7.1, Cutadapt v2.5, R, fastp v0.20.0]

### Microbial peptides activate tumour-infiltrating lymphocytes in glioblastoma. (Nature 2023)

- DOI: 10.1038/s41586-023-06081-w | PMCID: PMC10208956 | PMID: 37198490
- Version used: **3.2**
- Evidence: Reads were demultiplexed by separating reads into individual FastQ files, quality controlled and trimmed of Illumina adaptor sequences using locus-specific bcl2fastq software version v2.20.0.422, FastQC version 0.11.8 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and cutadapt v3.2 ( http://journal.embnet.org/index.php/embnetjournal/article/view/200 ), respectively.
- Full pipeline: quality control [Cutadapt v3.2, FastQC v0.11.8] -> read trimming [Cutadapt v3.2, FastQC v0.11.8]

### Widespread somatic L1 retrotransposition in normal colorectal epithelium. (Nature 2023)

- DOI: 10.1038/s41586-023-06046-z | PMCID: PMC10191854 | PMID: 37165195
- Evidence: Methylation analysis Sequenced reads were processed using Cutadapt 72 to remove adaptor sequences.
- Full pipeline: read trimming [Bismark] -> alignment/mapping [BWA, Bismark, minimap2] -> stage not stated [Cutadapt, DELLY, Picard]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: (Babraham Institute), a wrapper around Cutadapt 52 , was applied with default settings to perform quality and adapter trimming for each set of paired-end fastq files.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### mRNA recognition and packaging by the human transcription-export complex. (Nature 2023)

- DOI: 10.1038/s41586-023-05904-0 | PMCID: PMC7614608 | PMID: 37020021
- Evidence: Adapters were trimmed from sequencing reads using cutadapt through the trim_galore (version 0.6.0) tool with adaptor overlaps set for 3 bp for trimming.
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> normalisation [ImageJ] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX, ImageJ, PyMOL, R, UCSF Chimera] -> stage not stated [AlphaFold, RELION v3.1]

### The dietary sweetener sucralose is a negative modulator of T cell-mediated responses. (Nature 2023)

- DOI: 10.1038/s41586-023-05801-6 | PMCID: PMC10033444 | PMID: 36922598
- Version used: **2.10**
- Evidence: Raw reads were quality and adapter trimmed using cutadapt (version 2.10) before alignment 50 .
- Full pipeline: read trimming [Cutadapt v2.10, DADA2 v1.18] -> alignment/mapping [Cutadapt v2.10, RSEM v1.3.1] -> stage not stated [DESeq2 v1.30, R v4.0, STAR v2.7.6, phyloseq]

### Fumarate induces vesicular release of mtDNA to drive innate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-05770-w | PMCID: PMC10017517 | PMID: 36890229
- Version used: **1.10.0**
- Evidence: Low-quality reads (mapping quality < 20) as well as known adapters and artefacts were filtered out using Cutadapt (v.1.10.0).
- Full pipeline: read trimming [Cutadapt v1.10.0] -> alignment/mapping [Cutadapt v1.10.0, STAR v2.6.0c] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2 v1.18.1] -> stage not stated [GSEA, ImageJ]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **1.15**
- Evidence: In brief, the raw reads from ChIP–seq were trimmed by cutadapt v.1.15 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: Adapters were trimmed from raw reads using cutadapt through the trim_galore wrapper tool with adapter overlaps set to 3 bp for trimming.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.5**
- Evidence: Chromatin accessibility profiling We used cutadapt (v.2.5) 118 to remove sequencing adaptors and trim reads from libraries sequenced in 2 × 150 bp mode to 75 bp reads.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Phenotypic signatures of immune selection in HIV-1 reservoir cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05538-8 | PMCID: PMC9908552 | PMID: 36599977
- Version used: **2.5**
- Evidence: Briefly, for DNA library data, cutadapt (v2.5) 54 was used to trim 5′ and 3′ adaptor sequences, and extract 18-bp cell barcode sequences from read 1.
- Full pipeline: quality control [UMAP] -> alignment/mapping [MAFFT, SAMtools v1.9] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [R] -> visualisation [MAFFT, UMAP] -> stage not stated [Cutadapt v2.5]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Version used: **1.8.3**
- Evidence: Raw reads were first trimmed with cutadapt v.1.8.3 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Raw reads were processed using cutadapt 56 to remove primer sequences followed by the sequence analyses using the QIIME2 pipeline 57 .
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: Reads were trimmed with cutadapt (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Version used: **1.2.1**
- Evidence: Illumina adaptor sequences were detected and removed with Cutadapt (v.1.2.1), before trimming with Sickle 1.200 using a minimum window quality score of 20 and with exclusion of reads shorter than 15 bp.
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **3.3**
- Evidence: To call SNPs, raw sequencing reads were trimmed using cutadapt (v.3.3) 68 and aligned to the MorexV3 reference genome using Minimap2 (v.2.20) 65 .
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: The full pipeline uses trimmomatic 75 (v0.33) to filter reads, Cutadapt 76 (v1.18) to demultiplex, UMI-tools 77 (v0.5.5) to extract UMIs, bwa 78 (v0.7.17) to align, and featureCounts 79 (v1.6.3) to annotate features.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### Tissue spaces are reservoirs of antigenic diversity for Trypanosoma brucei. (Nature 2024)

- DOI: 10.1038/s41586-024-08151-z | PMCID: PMC11634766 | PMID: 39478231
- Evidence: Artefact reads containing the TAG sequence (or its reverse complement) in the cDNA reads were filtered out with Cutadapt 67 (v.4.3).
- Full pipeline: alignment/mapping [deepTools] -> visualisation [R] -> stage not stated [Cutadapt, ImageJ v1.53, SAMtools]

### Anti-viral defence by an mRNA ADP-ribosyltransferase that blocks translation. (Nature 2024)

- DOI: 10.1038/s41586-024-08102-8 | PMCID: PMC11618068 | PMID: 39443800
- Evidence: RNA-seq and RIP-seq read mapping FASTQ files for each sample were trimmed using cutadapt 54 (version 1.15) and then mapped to the E. coli MG1655 genome (NC_00913.2), the T4 genome ( NC_000866 ), and the plasmid pKVS45-CmdTAC using bowtie2 55 (version 2.3.4.1) with the following arguments: -D 20, -I 40, -X 300, -R 3, -N 0, -L 20, -i S,1,0.50.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, NumPy, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, HMMER]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Version used: **1.18**
- Evidence: Demultiplexed reads were trimmed to remove sequencing adaptors using Cutadapt 1.18 with the following parameters in paired-end mode: -f fastq -q 20 -m 50 -a AGATCGGAAGAGCACACGTCTGAAC -A AGATCGGAAGAGCGTCGTGTAGGGA.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **4.0**
- Evidence: Chromatin-associated RNA UBS amplicon-seq analysis Adapter sequences and low-quality reads were trimmed using cutadapt (v.4.0).
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Mechanisms that clear mutations drive field cancerization in mammary tissue. (Nature 2024)

- DOI: 10.1038/s41586-024-07882-3 | PMCID: PMC11374684 | PMID: 39232148
- Evidence: The CNA sequence analysis included the use of cutadapt for adaptor sequence removal and BWA for sequence alignment (using bwa aln, bwa mem) to the mm10 mouse genome.
- Full pipeline: alignment/mapping [BWA, Cutadapt] -> dimensionality reduction/clustering [Python] -> simulation/modelling [Python] -> visualisation [ImageJ, ggplot2] -> stage not stated [QuPath]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **3.1**
- Evidence: Adapter trimming was performed with Cutadapt (v3.1) 99 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Titration of RAS alters senescent state and influences tumour initiation. (Nature 2024)

- DOI: 10.1038/s41586-024-07797-z | PMCID: PMC11410659 | PMID: 39112713
- Evidence: Low-quality reads (mapping quality less than 20) and known adapter contamination were filtered out using Cutadapt 53 .
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [edgeR] -> visualisation [survival (R)] -> stage not stated [Enrichr, Monocle, R, Seurat, fgsea, ggplot2]

### Gut microbiota carcinogen metabolism causes distal tissue tumours. (Nature 2024)

- DOI: 10.1038/s41586-024-07754-w | PMCID: PMC11358042 | PMID: 39085612
- Evidence: Samples were checked for adapter contamination with cutadapt 29 and passed to dada2 30 for denoising, dereplication and chimera filtering; a feature table describing the distribution of reads in each sample among the identified ASVs was created, together with a representative sequence for each of the ASVs.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.5, MultiQC v1.12, QIIME 2 v2020.8, Trimmomatic v0.39] -> read trimming [Cutadapt, MultiQC v1.12, Trimmomatic v0.39] -> alignment/mapping [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Prokka v1.13, QUAST v5.0.2, R v4.0]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Analysis FASTQ files were demultiplexed using Bcl2fastq v.2.20.0.422 (Illumina) and adaptors were trimmed with cutadapt 57 using the following parameters (-g CACCG and -a GTTTT).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Symbolic recording of signalling and cis-regulatory element activity to DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07706-4 | PMCID: PMC11357993 | PMID: 39020177
- Evidence: Sequencing reads were trimmed using Cutadapt 49 and aligned to the human reference genome (hg38) using STAR (v.2.7.3) 50 , both with default settings.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.3] -> alignment/mapping [Cutadapt, STAR v2.7.3] -> differential/statistical testing [DESeq2, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Jupyter]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Version used: **3.4**
- Evidence: To process TSS-MPRA results, raw RNA and DNA sequencing reads, corresponding to the RNA transcripts and input DNA library, respectively, were trimmed for the 5′ adapter sequence GGTAACCGGTCCAGCTCA on the R1 read using cutadapt v.3.4.
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Adapter trimming of the Illumina Universal Adapter (AGATCGGAAGAG) was carried out by Cutadapt.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Evidence: First, adaptor sequences were removed by cutadapt software ( http://cutadapt.readthedocs.io/en/stable/index.html ) (v.1.18).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### Airborne DNA reveals predictable spatial and seasonal dynamics of fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-07658-9 | PMCID: PMC11269176 | PMID: 38987593
- Version used: **4.2**
- Evidence: Demultiplexed paired-end reads were trimmed, denoised and chimera checked using Cutadapt v.4.2 (ref.
- Full pipeline: read trimming [Cutadapt v4.2] -> differential/statistical testing [lme4] -> stage not stated [DADA2 v1.18.0, R, phyloseq]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Version used: **3.3**
- Evidence: The obtained paired-end reads were filtered by length (cutadapt v.3.3 (ref.
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### Transposase-assisted target-site integration for efficient plant genome engineering. (Nature 2024)

- DOI: 10.1038/s41586-024-07613-8 | PMCID: PMC11254759 | PMID: 38926583
- Evidence: 3′ adapter sequences were removed using cutadapt 62 (parameters: -a CTGTCTCTTATACACATCT -m 10).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [R, ggplot2]

### dsRNA formation leads to preferential nuclear export and gene expression. (Nature 2024)

- DOI: 10.1038/s41586-024-07576-w | PMCID: PMC11236707 | PMID: 38898279
- Version used: **2.1**
- Evidence: RNAi coverage analysis and classification For gene coverage of RNAi degradation products, reads were trimmed using Cutadapt (v.2.1) 56 and aligned to the reference genome with TopHat2 (v.2.1.1) 57 .
- Full pipeline: read trimming [Cutadapt v2.1, TopHat v2.1.1] -> alignment/mapping [Cutadapt v2.1, TopHat v2.1.1] -> quantification [featureCounts] -> stage not stated [BEDTools, Bioconductor, DESeq2]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **2.6**
- Evidence: Adaptor sequences were removed using cutadapt (v2.6) 73 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Single-cell nascent RNA sequencing unveils coordinated global transcription. (Nature 2024)

- DOI: 10.1038/s41586-024-07517-7 | PMCID: PMC11222150 | PMID: 38839954
- Evidence: Alignment and pre-processing Adaptor sequences were removed from paired-end fastq files using Cutadapt 54 .
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Cutadapt] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Seurat]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Version used: **2.8**
- Evidence: Reads were trimmed using cutadapt 2.8 according to the kit manufacturer’s instructions.
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Adhesive anti-fibrotic interfaces on diverse organs. (Nature 2024)

- DOI: 10.1038/s41586-024-07426-9 | PMCID: PMC11168934 | PMID: 38778109
- Evidence: Read quality was evaluated using FastQC, and data were pre-processed with Cutadapt 35 for adaptor removal following best practices 36 .
- Full pipeline: quality control [Cutadapt, FastQC] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ v2.1.0]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **1.18**
- Evidence: In brief, all reads were processed using Cutadapt (v.1.18) 67 for trimming of adaptor and poly-A sequences, then mapped onto GRCh38.p12 transcript references using TopHat2 (v.2.1.1) 68 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **2.3**
- Evidence: De novo gDNA-seq Alignment reads were trimmed using Trim Galore (v.0.6.3) 79 , then the first ten 5′ bases of both reads removed with Cutadapt (v.2.3) 80 .
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Version used: **1.8.1**
- Evidence: Read filtering, mapping and genotype calling After demultiplexing, reads were filtered for Illumina adapters using cutadapt v.1.8.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Version used: **2.1**
- Evidence: Cutadapt v2.1 was used to remove random primer bias and trim 3′ end poly-A-tail derived reads.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Version used: **1.6**
- Evidence: First the FASTQ files are processed to remove any adapter sequences at the end of the reads using cutadapt (v1.6).
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: The resulting reads were assessed for quality using FastQC ( https://github.com/s-andrews/FastQC ), trimmed with Sickle (v.1.33; https://github.com/najoshi/sickle ) to remove low-quality 5′- and 3′-end bases, and trimmed using Cutadapt 71 (v.1.18) to remove adapters.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **4.1**
- Evidence: Sequencing reads were demultiplexed through HTSEQ (Princeton University High Throughput Sequencing Database, https://htseq.princeton.edu/ ) and sequencing adapters were trimmed using Cutadapt (4.1) 46 .
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Version used: **1.18**
- Evidence: Small RNA analysis Sequencing adapters were trimmed from 5′ and 3′ ends using Cutadapt v1.18 (ref.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Version used: **4.1**
- Evidence: The correlated 5′-end and 3′-end sequences were extracted by the custom script (fasta_to_paired.sh) using the SeqKit (v2.4.0) and Cutadapt (v4.1) packages.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Version used: **2.8**
- Evidence: To determine the abundance of individual gRNAs per samples, the fastq files were trimmed using cutadapt (v2.8) to retain only the putative gRNA sequences.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### IL-10 constrains sphingolipid metabolism to limit inflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07098-5 | PMCID: PMC10954550 | PMID: 38383790
- Evidence: RNA-seq data analysis Adapter sequences were removed from the raw sequencing reads using the tool Cutadapt ( https://journal.embnet.org/index.php/embnetjournal/article/view/200 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HTSeq, Picard] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v4.3.0]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: Sequence data cleaning was performed by the Cutadapt software (v1.9.1) 43 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Version used: **4.1**
- Evidence: Illumina Trueseq adapters were removed from RNA-seq reads using cutadapt (version 4.1) with the parameters -q 25 -m 25 91 .
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Version used: **4.1**
- Evidence: Short-read RNA-seq data analysis Raw RNA-seq reads were subject to adaptor and quality trimming using cutadapt 4.1.
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### Structural basis of ribosomal 30S subunit degradation by RNase R. (Nature 2024)

- DOI: 10.1038/s41586-024-07027-6 | PMCID: PMC10901742 | PMID: 38326618
- Evidence: Samples were demultiplexed using bcl2fastq, adapter trimming was performed with cutadapt and sequences from Read 2 were taken forward into alignments using Novoalign ( https://www.novocraft.com/ ; v.3.06).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, MotionCor2] -> visualisation [BEDTools, ImageJ] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION v3.1.3]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Sequencing reads were trimmed and filtered for quality and adapter content using version 0.4.5 of TrimGalore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore ) and running version 1.15 of cutadapt and version 0.11.5 of FastQC.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **4.1**
- Evidence: Following processing by cutadapt version 4.1 86 to remove the sequencing adapters, in order to reduce the reference bias, and improve the posterior phylogenetic inference and assignment 87 , the genome reference selection for mapping each sample was determined according to the results from the original manuscript where the genomes were published (see Supplementary Table 3 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Mitochondrial dysfunction abrogates dietary lipid processing in enterocytes. (Nature 2024)

- DOI: 10.1038/s41586-023-06857-0 | PMCID: PMC10781618 | PMID: 38123683
- Evidence: Illumina adapters were clipped off the raw reads using Cutadapt with standard parameters and a minimum read length of 35 after trimming (shorter reads were discarded).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [GSEA] -> stage not stated [Bioconductor v3.11, Fiji v1.53c, featureCounts, fgsea]

### Emergence of replication timing during early mammalian development. (Nature 2024)

- DOI: 10.1038/s41586-023-06872-1 | PMCID: PMC10781638 | PMID: 38123678
- Version used: **3.4**
- Evidence: Paired-end reads were trimmed by cutadapt (v.3.4) with parameters -a CTGTCTCTTATA -A CTGTCTCTTATA -a AGATCGGAAGAGC -A AGATCGGAAGAGC --minimum-length=20.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.3.5] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [BEDTools, ImageJ v1.53k, R v4.0.0, SAMtools v1.9]

### Hypoblast from human pluripotent stem cells regulates epiblast development. (Nature 2024)

- DOI: 10.1038/s41586-023-06871-2 | PMCID: PMC10849967 | PMID: 38052228
- Version used: **1.15**
- Evidence: The sequenced reads were trimmed to remove low-quality bases and adaptor sequences using cutadapt (v.1.15) 67 .
- Full pipeline: quality control [Seurat] -> read trimming [Cutadapt v1.15, TopHat] -> alignment/mapping [RSEM v1.3.1, STAR, TopHat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **2.9**
- Evidence: Bioinformatics analysis of iMgl RNA sequencing Raw sequencing reads were first quality checked and trimmed using Trim Galore ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ v.0.6.4, a wrapper program implementing Cutadapt v.2.9 ( https://journal.embnet.org/index.php/embnetjournal/article/view/200 ) and FastQC v.0.11.9 ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ )...
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: CUT&RUN analysis Standard Illumina adapters were cut from the Illumina reads using Cutadapt 72 and then aligned to a combined hg38 and E. coli genome version using Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Version used: **3.4**
- Evidence: Reads were trimmed with cutadapt v.3.4, using the -g flag to specify the 5′ adapter and stagger (Supplementary Table 1e ).
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: RNA-seq mapping Fastq files were adaptor stripped using cutadapt with a minimum length of 15 and a quality cut-off of 2 (parameters: -a CTGTAGGCACCATCAAT –minimum-length = 15 –quality-cutoff = 2).
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Version used: **4.4**
- Evidence: All 3′ end sequencing data were trimmed using cutadapt (v4.4) 62 to remove poly-A sequences and Illumina adapters.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **4.1**
- Evidence: Raw RNA-seq reads were processed with Cutadapt v.4.1 (-a GATCGGAAGAGCACACGTCTGAACTCCAGTCAC -q 30 -m 15) 66 to remove TruSeq adapters and bad-quality bases.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Version used: **3.7**
- Evidence: 16S sequences were trimmed using Cutadapt (v3.7) and taxonomy was assigned with the Green-Genes reference database (release of May 2013).
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Version used: **2.6**
- Evidence: For new spacers, the read 1 sequences of the paired-end sequencing reads were trimmed to extract new spacer instances using Cutadapt (v.2.6) by identifying the flanking repeat 26 sequence (attgtagcactgcgaaatgagaaagggagctacaac) 57 .
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Sequencing reads were trimmed and filtered for quality control using TrimGalore (v.0.6.7) with a quality setting of 15, Cutadapt 76 (v.4.0) and FastQC v.0.12.1.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Version used: **1.18**
- Evidence: Illumina TruSeq adapters were trimmed from the paired-end reads using cutadapt (v.1.18).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### The geologic history of marine dissolved organic carbon from iron oxides. (Nature 2025)

- DOI: 10.1038/s41586-025-09383-3 | PMCID: PMC12390840 | PMID: 40804515
- Version used: **3.4**
- Evidence: Adaptor sequences were removed using cutadapt v.3.4 (ref.
- Full pipeline: stage not stated [Cutadapt v3.4, DADA2 v1.30]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: Reads were trimmed with Cutadapt 69 and aligned to the mouse transcriptome (GRCm38, Ensembl release 102) using STAR (v.2.7.9a) 70 and quantified using Salmon (v.1.10.1) 71 .
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Sequence quality was assessed using FastQC followed by the removal of low-quality reads and adapter sequences using Cutadapt.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Reads were preprocessed according to the type of library preparation using cutadapt to trim adapters and FastQC to assess read quality.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Version used: **4.4**
- Evidence: Adaptor sequences were trimmed and reads were size-selected using Cutadapt v.4.4.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **4.2**
- Evidence: For this purpose, primers in the reads were trimmed using Cutadapt (v.4.2) 62 , and read pairs without identifiable primers and undetermined bases (Ns) were discarded.
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **1.15**
- Evidence: Reads were trimmed with cutadapt (version 1.15) and aligned to the haplotype 1 sequence assembly of FB19-011-3 with BWA-MEM (v0.7.17-r1188) 73 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Rewiring endogenous genes in CAR T cells for tumour-restricted payload delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09212-7 | PMCID: PMC12328239 | PMID: 40604285
- Version used: **2.1**
- Evidence: RNA-SeQC v.1.1.7 was used to assess the quality of output 57 , and Cutadapt v.2.1 was used to remove random primer bias and poly-A-tail-derived reads.
- Full pipeline: quality control [Cutadapt v2.1] -> read trimming [edgeR v3.8.5] -> alignment/mapping [HISAT2] -> normalisation [edgeR v3.8.5] -> dimensionality reduction/clustering [Seurat] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: Unique molecular identifiers were extracted from the fastq files with umi_tools, and cutadapt was used to remove short and low-quality reads.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: Cutadapt 42 (v4.2) was used to remove adapter sequences, trim low-quality ends from reads, and filter out reads shorter than 15 bp.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **4.1**
- Evidence: Quality control of raw sequencing reads identified adaptor sequences from the Illumina Nextera platform in some samples, which were subsequently trimmed using Cutadapt (v.4.1) 61 . kallisto (v.0.46.1) 62 was used to quantify transcript-level expression by mapping to a transcript index built from GENCODE human transcript (v.44) 63 .
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **4.1**
- Evidence: Reads were trimmed to the bare sgRNA sequence using cutadapt 4.1 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **2.1**
- Evidence: Fastq files were subjected to quality control with FastQC (0.11.9) and then trimmed with Cutadapt (2.1) with reads less than 20 nucleotides being filtered out.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: Analysis of data from 3′-RACE sequencing RA37_N adapter sequence was trimmed from the R2 read (containing poly(A) tail) with cutadapt 34 (options -g CCTTGGCACCCGAGAATTCCANNNNNNNGTCAG –discard-untrimmed).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **1.18**
- Evidence: Adaptors were removed with cutadapt v.1.18, and quality-filtering and trimming were performed using Trimmomatic v.0.38 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: Artefact reads containing the TAG sequence (or its reverse complement) in the cDNA read were filtered out using Cutadapt 47 (v.4.3).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Version used: **3.4**
- Evidence: Data processing Sequencing reads were trimmed for both quality and adaptor sequences using cutadapt (v3.4) 59 .
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: Specifically, reads were trimmed with cutadapt 61 , PhiX, and quality filtering, read pair merging and amplicon sequence variant resolution was performed with DADA2 62 .
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Adapters were removed from single-end data with cutadapt 65 and from paired-end data with AdapterRemoval 66 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: TCR repertoire analyses For the bulk TCR-seq dataset, adaptors were first removed by Cutadapt 60 , then the TCR sequences were assembled by TRUST4 (ref.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Functional evaluation and clinical classification of BRCA2 variants. (Nature 2025)

- DOI: 10.1038/s41586-024-08388-8 | PMCID: PMC11821525 | PMID: 39779857
- Version used: **3.5**
- Evidence: Sequencing data processing FASTQ files of sequenced samples from Illumina MiSeq or NextSeq assays were trimmed for adapter sequences using cutadapt (v.3.5).
- Full pipeline: read trimming [Cutadapt v3.5] -> alignment/mapping [BWA v0.7.17, PyMOL] -> dimensionality reduction/clustering [PyMOL] -> stage not stated [JAGS]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Evidence: Reads were trimmed using Cutadapt 43 (v.3.4) and quality was checked with FastQC 44 (v0.11.9).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Diversity and biogeography of the bacterial microbiome in glacier-fed streams. (Nature 2025)

- DOI: 10.1038/s41586-024-08313-z | PMCID: PMC11735386 | PMID: 39743584
- Evidence: Raw sequences were initially trimmed of primers using the plugin cutadapt 54 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [featureCounts] -> quantification [featureCounts, pheatmap, phyloseq] -> stage not stated [DADA2, QIIME 2 v2020.8, R v4.1.0, ggplot2, scikit-learn, vegan]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **4.4**
- Evidence: TE sequence in Read1 of TEd-seq reads (61 bp of 5′ terminals sequence for EVD or 41 bp of 5′ terminal sequence for Tal1 ) were trimmed with Cutadapt 4.4 (ref.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: ES cell H1 ChIP–seq reads and their associated inputs were trimmed to remove adapters and bases with a phred score of <30 using Cutadapt 66 (cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -q 30).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Version used: **2.10**
- Evidence: In brief, fastq adapter trimming was performed with cutadapt (v2.10).
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **3.4**
- Evidence: For ChIP–seq processing, adapter sequences in FASTQ files were trimmed using Cutadapt (v.3.4).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### The E3 ubiquitin ligase mechanism specifying targeted microRNA degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10232-0 | PMCID: PMC13083262 | PMID: 41851464
- Version used: **4.8**
- Evidence: Processing of sequencing reads was done by trimming adaptors with cutadapt (v.4.8) 84 , filtering out reads with a quality score of 30 or below with FASTX Toolkit v.0.0.14 and then string-matching the first 13 nt of each read against a dictionary of miRNA names and sequences derived mainly from TargetScanFly7 and TargetScanMouse7 (ref.
- Full pipeline: read trimming [Cutadapt v4.8] -> quantification [R] -> normalisation [DESeq2 v1.38.3] -> differential/statistical testing [R] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **1.11**
- Evidence: After removing adapters and low-quality bases by cutadapt (v.1.11), paired-end cf-EpiTracing reads were mapped to the human reference genome hg19 and Drosophila reference genome dm3 using Bowtie2 (v.2.2.9) 77 .
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### DICER cleavage fidelity is governed by 5'-end binding pockets. (Nature 2026)

- DOI: 10.1038/s41586-026-10211-5 | PMCID: PMC13171623 | PMID: 41781616
- Evidence: First, the 3′ and 5′ adapter sequences were removed using the cutadapt tool 43 with the command cutadapt -a TGGAATTCTCGGGTGCCAAGG -A GATCGTCGGACTGTAGAACTCTGAAC.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, Bowtie2, Coot v0.9.8.96] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.7, Coot v0.9.8.96, PHENIX v1.20.1] -> stage not stated [PyMOL]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Version used: **1.18**
- Evidence: FASTQ files were trimmed for indices using cutadapt 1.18.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Version used: **1.15**
- Evidence: FASTQ files for each sample were trimmed using cutadapt (v1.15) 50 and then mapped to the MG1655 genome (NC_00913.2) and the T7 genome ( V01146 ), or the consensus map of rRNA loci as previously described 30 using bowtie2 (v2.3.4.1) 51 with the following arguments: –D 20, –I 40, –X 300, –R 3, –N 0, –L 20, –i S,1,0.50.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **2.3**
- Evidence: Raw reads were preprocessed by trimming Illumina Truseq adapters, poly(A) and poly(T) sequences using cutadapt (v.2.3) 66 with the parameters ‘cutadapt -j 4 -m 20 --interleaved -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -A AGATCGGAAGAGCGTCGTGTAGGG AAAGAGTGT Fastq1 Fastq2 | cutadapt --interleaved -j 4 -m 20 -a “A{100}” -A “A{100}” - | cutadapt -j 4 -m 20 -a “T{100}” -A “T{100}” -’.
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **2.6**
- Evidence: Reads with poor quality (lower than 20) were filtered using cutadapt (v.2.6) and aligned to the mouse reference genome (GRCm39) using bowtie2 (v.2.4), and duplicated reads were marked and removed by Picard tools (v.3.4).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### GlycoRNA complexed with heparan sulfate regulates VEGF-A signalling. (Nature 2026)

- DOI: 10.1038/s41586-025-10052-8 | PMCID: PMC12999495 | PMID: 41606331
- Version used: **4.9**
- Evidence: Raw reads were demultiplexed, unique molecular identifiers (UMI) extracted and adapter trimmed using Cutadapt (v4.9) 83 .
- Full pipeline: read trimming [Cutadapt v4.9, DESeq2 v1.42.1] -> alignment/mapping [Bowtie2 v2.5.4] -> differential/statistical testing [DESeq2 v1.42.1] -> stage not stated [ImageJ, Python, SciPy]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Version used: **2.8**
- Evidence: Samples were demultiplexed, quality checked, filtered and aligned with genome build GRCm38 using pre-established pipelines implemented in snakePipes 64 with STARsolo v.2.7.4a 65 , deeptools v.3.3.2, seqtk v.1.3, pigz v.2.3.4, snpsplit v.0.3.4, samtools v.1.10, fastqc v.0.11.9, cutadapt v.2.8, trim-galore v.0.6.5, multiqc v.1.8, fastp v.0.20.0, umi_tools v.1.0.1 and star v.2.7.4a.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Version used: **1.9.1**
- Evidence: Finally, primer sequences used for amplicon amplification were removed using cutadapt (v1.9.1) 74 .
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Version used: **1.18**
- Evidence: Analysis of EM-Seq data was done as described previously using the Trim Galore (0.6.7), cutadapt (1.18) and Bismarck (v0.23.0) software packages 19 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Version used: **2.9**
- Evidence: In brief, data were trimmed using cutadapt (v.2.9) 75 , quality checked before and after trimming using FastQC (v.0.11.9), and then mapped and quantified using STAR (v.2.7.7a) 76 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### NAC controls nascent chain fate through tunnel sensing and chaperone action. (Nature 2026)

- DOI: 10.1038/s41586-025-10058-2 | PMCID: PMC13043293 | PMID: 41430436
- Version used: **1.4.2**
- Evidence: Adaptor sequences were removed from demultiplexed sequencing reads using Cutadapt v.1.4.2 (ref.
- Full pipeline: read trimming [Cutadapt v1.4.2] -> alignment/mapping [STAR] -> stage not stated [AlphaFold]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: Chromatin dataset processing CUT&Run datasets were processed by trimming adaptors using cutadapt, locally mapping the reads using bowtie2, filtering for quality, removing duplicates and ENCODE blacklisted regions (ENCFF419RSJ) using samtools, and computing the coverage using deeptools.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Gene-drive-capable mosquitoes suppress patient-derived malaria in Tanzania. (Nature 2026)

- DOI: 10.1038/s41586-025-09685-6 | PMCID: PMC12779567 | PMID: 41372414
- Evidence: Adaptor sequences were removed from raw read sequences with Cutadapt 45 and mapped to the P. falciparum 3D7 genome (PlasmoDB v68) with BWA-MEM.
- Full pipeline: alignment/mapping [BWA, Bioconductor, Cutadapt] -> stage not stated [BCFtools, ImageJ]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **4.9**
- Evidence: Sequencing reads were further processed as follows: Illumina adapters were trimmed and low-quality reads removed with Cutadapt (v.4.9) 56 (mismatch rate = 1 mismatch every 10 bp, overlap = 5 bp, minimum read length = 30 bp).
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: Subsequently all reads were oriented while removing primer sequences and filtering reads below 3.5 kb or above 6.5 kb using cutadapt 86 v.3.4.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **4.4**
- Evidence: Demultiplexing of paired-end reads was performed using cutadapt (v.4.4), matching read 1 5′ barcodes were provided in a separate FASTA file, with no trimming applied (--action=none).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **3.6**
- Evidence: CUT&Tag data analysis CUT&Tag reads were trimmed using cutadapt (v.3.6) and aligned to the mouse reference genome (mm10) and Drosophila (BDGP6) using BOWTIE2 (v.2.4.2) with the following options: --very-sensitive-local --no-unal --no-mixed --no-discordant --phred33 -I 10 -X 700.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Version used: **4.1**
- Evidence: Rfoot-seq data processing and analyses Ribosome profiling data were processed by trimming adaptors with Cutadapt v4.1, removing rRNA reads with Bowtie v2.2.6 (ref.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Version used: **1.18**
- Evidence: Cutadapt (v1.18) 69 was used to remove adaptors, trim 3′ bases with Phred scores < 20 and discard reads fewer than 30 and more than 50 bases after trimming.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Cutadapt 80 was used to trim poor-quality bases and Illumina universal adapter sequences from raw reads before alignment.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Secretome translation shaped by lysosomes and lunapark-marked ER junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-09718-0 | PMCID: PMC12727531 | PMID: 41193816
- Version used: **2.10**
- Evidence: Sequencing adapters were trimmed from the reads using Cutadapt v2.10 prior to alignment with STAR v2.7.5c against the Homo sapiens GRCh38 genome assembly from Ensembl.
- Full pipeline: read trimming [Cutadapt v2.10, STAR v2.7.5c] -> alignment/mapping [Cutadapt v2.10, STAR v2.7.5c] -> quantification [CellProfiler] -> stage not stated [DESeq2, ImageJ, TrackMate]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: The adapter sequence (‘AGATCGGAAGAGC’) was removed using cutadapt 71 and then all reads were aligned to the GS7 reference genome using Minimap2 51 , sorted with NovoSort ( https://www.novocraft.com/products/novosort/ ) and converted to a compressed reference-oriented alignment map (CRAM 72 ) file using SAMtools 58 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### SARS-CoV-2 expresses a microRNA-like small RNA able to selectively repress host genes. (PNAS 2021)

- DOI: 10.1073/pnas.2116668118 | PMCID: PMC8719879 | PMID: 34903581
- Evidence: The reads were trimmed of adaptors using Cutadapt ( 65 ) with the following settings: -u 4 -O 7 -a N{4}TGGAATTCTCGGGTGCCAAGG -q 10 -m 18 -M.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, featureCounts] -> differential/statistical testing [edgeR] -> visualisation [BEDTools]

### Single-cell quantification of a broad RNA spectrum reveals unique noncoding patterns associated with cell types and states. (PNAS 2021)

- DOI: 10.1073/pnas.2113568118 | PMCID: PMC8713755 | PMID: 34911763
- Version used: **1.18**
- Evidence: Briefly, for Smart-seq-total v1, reads were trimmed from polyA tails using cutadapt v1.18 with the following parameters: -m 18 -j 4 -a AAAAAAAAAA -a TTTTTTTTTT.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [featureCounts v1.6.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [R, UMAP]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Version used: **1.16**
- Evidence: The raw reads were filtered to remove potential lower quality reads and artifacts using Trimmomatic v0.36 ( 51 ) and cutadapt v1.16 ( 52 ).
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### SARS-CoV-2 evolution in animals suggests mechanisms for rapid variant selection. (PNAS 2021)

- DOI: 10.1073/pnas.2105253118 | PMCID: PMC8612357 | PMID: 34716263
- Evidence: Briefly, data were trimmed for adapters and low quality using Cutadapt ( 63 ), followed by aligning reads to the viral reference sequence.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> stage not stated [GATK, Nextflow, SnpEff]

### The translatome of neuronal cell bodies, dendrites, and axons. (PNAS 2021)

- DOI: 10.1073/pnas.2113929118 | PMCID: PMC8639352 | PMID: 34670838
- Evidence: Sequencing adapters were trimmed using the Cutadapt software version 1.15 ( 63 ) with the following arguments: — cut 1–minimum -length 22 –discard-untrimmed –overlap 3 -e 0.2 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt] -> alignment/mapping [Bowtie2 v2.3.5.1, STAR v2.7.3, featureCounts v2.0.0] -> stage not stated [DESeq2 v1.30.1, Python]

### Microbial population dynamics and evolutionary outcomes under extreme energy limitation. (PNAS 2021)

- DOI: 10.1073/pnas.2101691118 | PMCID: PMC8379937 | PMID: 34385301
- Evidence: Raw reads were cleaned and trimmed using cutadapt ( 67 ).
- Full pipeline: read trimming [Cutadapt] -> stage not stated [R v3.5, statsmodels]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Version used: **2.8**
- Evidence: Paired-end reads were trimmed and quality-filtered using cutadapt (v2.8).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Cell-free reconstitution reveals the molecular mechanisms for the initiation of secondary siRNA biogenesis in plants. (PNAS 2021)

- DOI: 10.1073/pnas.2102889118 | PMCID: PMC8346886 | PMID: 34330830
- Evidence: After removal of adaptor sequences by cutadapt ( 58 ), small RNA sequence reads of 20 to 29 nt length were mapped to the TAS3a sequence used in the tasiRNA biogenesis assay using the FASTX-Toolkit ( http://hannonlab.cshl.edu/fastx_toolkit/ ) and Bowtie ( 59 ) allowing for up to one mismatch.
- Full pipeline: alignment/mapping [BEDTools, Cutadapt, SAMtools, ggplot2]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: The low-quality bases and adapter sequences were removed using cutadapt ( 38 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Evidence: S2 were trimmed at the 3′ end of the sequences for ambiguous nucleotides (Ns) and for artificial poly Gs using cutadapt ( 69 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### A phage mechanism for selective nicking of dUMP-containing DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2026354118 | PMCID: PMC8201957 | PMID: 34074772
- Evidence: For variant calling, Illumina adapters were trimmed from the reads using cutadapt ( 26 ); resulting reads shorter than 30 bp were discarded.
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [GATK v3.7] -> variant calling [Cutadapt] -> stage not stated [Fiji, ImageJ, VEP]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: Demultiplexed reads were quality filtered (Sickle; v1.33) ( 52 ) and Nextera adapter sequences were trimmed (cutadapt; v1.11) ( 53 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Expansions of adaptive-like NK cells with a tissue-resident phenotype in human lung and blood. (PNAS 2021)

- DOI: 10.1073/pnas.2016580118 | PMCID: PMC7980282 | PMID: 33836578
- Version used: **1.14**
- Evidence: Following sequencing and demultiplexing, read pairs were trimmed from Illumina adapters using cutadapt (version 1.14) ( 51 ), and UrQt was used to trim all bases with a phred quality score below 20 ( 52 ).
- Full pipeline: read trimming [Cutadapt v1.14] -> dimensionality reduction/clustering [UMAP]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Version used: **2.5**
- Evidence: Adaptor sequence was trimmed with cutadapt (version 2.5), and trimmed reads were mapped to the reference genome TAIR10 using Bowtie (version 1.2.3) with only one unique hit (-m 1) and zero mismatches (-v 0) ( 59 ).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Version used: **1.16**
- Evidence: (v0.4.4), Trimmomatic (v0.36), and Cutadapt (v1.16).
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### The harsh microenvironment in early breast cancer selects for a Warburg phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2011342118 | PMCID: PMC7826394 | PMID: 33452133
- Evidence: Then cutadapt will be used to trim off adaptor contaminant sequences and low-quality bases at the ends.
- Full pipeline: read trimming [R] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Cutadapt, Enrichr]

### Muscle injury causes long-term changes in stem-cell DNA methylation. (PNAS 2022)

- DOI: 10.1073/pnas.2212306119 | PMCID: PMC9907067 | PMID: 36534800
- Evidence: DNA methylation was analyzed by using sequencing reads from RRBS that were trimmed and quality filtered by trim galore software (v0.3.3), fastQC ( 39 ), and cutadapt ( 40 ), using default parameters for RRBS.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> differential/statistical testing [R] -> stage not stated [DESeq2, HOMER, HTSeq v0.6.0, ImageJ]

### Precise spatial structure impacts antimicrobial susceptibility of <i>S. aureus</i> in polymicrobial wound infections. (PNAS 2022)

- DOI: 10.1073/pnas.2212340119 | PMCID: PMC9907066 | PMID: 36520668
- Version used: **2.6**
- Evidence: Adapters were removed, and reads were trimmed using a minimum read threshold of 22 base pairs with Cutadapt version 2.6 ( 64 ).
- Full pipeline: read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0]

### Temporal changes in plasma membrane lipid content induce endocytosis to regulate developmental epithelial-to-mesenchymal transition. (PNAS 2022)

- DOI: 10.1073/pnas.2212879119 | PMCID: PMC9907157 | PMID: 36508654
- Evidence: Briefly, reads were trimmed using Cutadapt ( 81 ) and aligned to the chicken genome (GRCg6a) using BowTie2 ( 82 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2, featureCounts]

### A gut microbial metabolite of dietary polyphenols reverses obesity-driven hepatic steatosis. (PNAS 2022)

- DOI: 10.1073/pnas.2202934119 | PMCID: PMC9860326 | PMID: 36417437
- Evidence: Paired-end 100 bp reads were controlled for quality with FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) before trimming Illumina adapters from the 3′ ends using cutadapt ( 62 ).
- Full pipeline: quality control [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> read trimming [Cutadapt, FastQC, Prokka, SPAdes, Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [DESeq2, R] -> differential/statistical testing [DESeq2, Metascape, R, edgeR, pheatmap] -> visualisation [ggplot2] -> stage not stated [DADA2, Enrichr, phyloseq]

### DNA polymerase epsilon interacts with SUVH2/9 to repress the expression of genes associated with meiotic DSB hotspot in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208441119 | PMCID: PMC9564942 | PMID: 36191225
- Evidence: Raw reads were trimmed with Cutadapt and mapped to TAIR10 using STAR version 2.7.9a ( 68 ) with parameters “–alignIntronMax 5000 –outSAMmultNmax 1 –outFilterMultimapNmax 50 –outFilterMismatchNoverLmax 0.1.” DE genes and TEs (fold change ≥2 and P < 0.01) were identified by the R package DESeq2 version 1.30.1 ( 69 ) based on the gene expression matrix quantified by featureCounts version 2.0.0 ( 70 )...
- Full pipeline: read trimming [Bismark v0.22.3, Cutadapt, STAR v2.7.9a] -> alignment/mapping [Bismark v0.22.3, Bowtie2, Cutadapt, STAR v2.7.9a] -> quantification [Bismark v0.22.3, Cutadapt, DESeq2 v1.30.1, R, STAR v2.7.9a, featureCounts v2.0.0] -> stage not stated [ImageJ v1.52]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: Then we used cutadapt to trim adapter sequences from both ends according to the 19-bp mosaic end (ME) sequence, with parameters -e 0.22 -a CTGTCTCTTATACACATCT and -e 0.22 -g AGATGTGTATAAGAGACAG for both read 1 and read 2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### A scalable framework for the discovery of functional helicase substrates and helicase-driven regulatory switches. (PNAS 2022)

- DOI: 10.1073/pnas.2209608119 | PMCID: PMC9499579 | PMID: 36095194
- Version used: **1.15**
- Evidence: Multiplexed sequencing of the pools resulted in 4.6 to 9.5 × 10 6 paired-end reads per pool after quality control filtering (FastQC v0.11.5) and adapter trimming (Cutadapt v1.15).
- Full pipeline: quality control [Cutadapt v1.15, FastQC v0.11.5] -> read trimming [Cutadapt v1.15, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [Galaxy, MACS2, Python]

### Loss-of-function mutation survey revealed that genes with background-dependent fitness are rare and functionally related in yeast. (PNAS 2022)

- DOI: 10.1073/pnas.2204206119 | PMCID: PMC9478683 | PMID: 36067306
- Evidence: The reads that contained the amplified part of the transposon were selected, the corresponding 57-bp sequence was trimmed with Cutadapt ( 39 ), and the reads corresponding to the plasmid were discarded.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> stage not stated [R]

### SARS-CoV-2 variant spike and accessory gene mutations alter pathogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2204717119 | PMCID: PMC9477415 | PMID: 36040867
- Version used: **3.4**
- Evidence: Reads were preprocessed using Cutadapt v3.4 and then aligned to the murine genome (assembly GRCm38) using STAR v2.7.8a ( 17 , 18 ).
- Full pipeline: alignment/mapping [Cutadapt v3.4, STAR v2.7.8a] -> differential/statistical testing [DESeq2 v4.1.0, R v4.1.1]

### USP13 promotes deubiquitination of ZHX2 and tumorigenesis in kidney cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2119854119 | PMCID: PMC9457248 | PMID: 36037364
- Evidence: Reads were then filtered for adapter contamination using cutadapt ( 44 ) and filtered using the FASTX-Toolkit (v0.0.14) ( hannonlab.cshl.edu/fastx_toolkit/index.html ) such that at least 90% of bases of each read had a Phred score of >20.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.14.1] -> differential/statistical testing [DESeq2 v1.14.1]

### False-positive IRESes from &lt;i&gt;Hoxa9&lt;/i&gt; and other genes resulting from errors in mammalian 5' UTR annotations. (PNAS 2022)

- DOI: 10.1073/pnas.2122170119 | PMCID: PMC9456764 | PMID: 36037358
- Evidence: Reads were processed using fastq-dump followed by cutadapt.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [scikit-learn] -> stage not stated [BEDTools, Cutadapt]

### NAD&lt;sup&gt;+&lt;/sup&gt; metabolism drives astrocyte proinflammatory reprogramming in central nervous system autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2211310119 | PMCID: PMC9436380 | PMID: 35994674
- Evidence: Poly-A/T stretches and Illumina adapters were trimmed from the reads using cutadapt, and resulting reads shorter than 30 bp were discarded.
- Full pipeline: read trimming [Cutadapt] -> quantification [DESeq2, R] -> normalisation [DESeq2, R] -> stage not stated [Enrichr]

### Isolation of a virus causing a chronic infection in the archaeal model organism &lt;i&gt;Haloferax volcanii&lt;/i&gt; reveals antiviral activities of a provirus. (PNAS 2022)

- DOI: 10.1073/pnas.2205037119 | PMCID: PMC9436352 | PMID: 35994644
- Evidence: The sequenced reads were quality trimmed using the software Cutadapt ( 41 ), with a minimum quality of 30 and a minimum length of 50 (-q 30, -m 50).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BLAST] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [SPAdes v3.13.1]

### Nucleotide excision repair removes thymidine analog 5-ethynyl-2'-deoxyuridine from the mammalian genome. (PNAS 2022)

- DOI: 10.1073/pnas.2210176119 | PMCID: PMC9436350 | PMID: 35994676
- Evidence: Reads were trimmed to remove flanking adapter sequences by cutadapt ( 44 ), and then duplicate reads were removed by fastx_toolkit/0.0.14 ( hannonlab.cshl.edu/fastx_toolkit/index.html ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> stage not stated [BEDTools, SAMtools]

### Intestinal tissue-resident T cell activation depends on metabolite availability. (PNAS 2022)

- DOI: 10.1073/pnas.2202144119 | PMCID: PMC9411733 | PMID: 35969785
- Version used: **1.1**
- Evidence: The barcoded samples were demultiplexed and trimmed with the cutadapt version 1.1 adapter removal software.
- Full pipeline: read trimming [Cutadapt v1.1] -> alignment/mapping [TopHat] -> normalisation [Bioconductor, DESeq2, R v3.1.0] -> differential/statistical testing [Bioconductor, DESeq2, R v3.1.0]

### Plant genetic effects on microbial hubs impact host fitness in repeated field trials. (PNAS 2022)

- DOI: 10.1073/pnas.2201285119 | PMCID: PMC9335298 | PMID: 35867817
- Evidence: The demultiplexed fastq files generated by MiSeq reporter for the first read of each run were quality filtered and truncated to remove potential primer sequences and low-quality base calls using the program cutadapt ( 51 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [Python] -> normalisation [Python] -> stage not stated [Prokka, R, SPAdes, igraph, lme4]

### Seed DNA damage responses promote germination and growth in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2202172119 | PMCID: PMC9335332 | PMID: 35858436
- Evidence: First, the adapter sequences among the reads were removed using Cutadapt ( 44 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [SAMtools] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Version used: **2.10**
- Evidence: Adaptor sequences were trimmed using Cutadapt (v2.10).
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### Voltage-gated sodium channel &lt;i&gt;scn8a&lt;/i&gt; is required for innervation and regeneration of amputated adult zebrafish fins. (PNAS 2022)

- DOI: 10.1073/pnas.2200342119 | PMCID: PMC9282381 | PMID: 35867745
- Evidence: Adapter sequences were trimmed by Cutadapt.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [ImageJ]

### Integrated screens uncover a cell surface tumor suppressor gene <i>KIRREL</i> involved in Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2121779119 | PMCID: PMC9231494 | PMID: 35704761
- Evidence: For RNA-seq data analysis, reads were adapter-trimmed and preprocessed with Cutadapt software (version 1.15) for quality control and data filtering.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.3a] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [STRING db]

### Genome-wide analysis of the <i>in vivo</i> tRNA structurome reveals RNA structural and modification dynamics under heat stress. (PNAS 2022)

- DOI: 10.1073/pnas.2201237119 | PMCID: PMC9231505 | PMID: 35696576
- Evidence: Adapter sequence was trimmed using Cutadapt ( 58 ) and resulting sequencing data were analyzed by ShapeMapper2 ( 25 ).
- Full pipeline: read trimming [Cutadapt]

### Geological activity shapes the microbiome in deep-subsurface aquifers by advection. (PNAS 2022)

- DOI: 10.1073/pnas.2113985119 | PMCID: PMC9231496 | PMID: 35696589
- Evidence: Primer sequences were trimmed from the raw sequencing reads of each sample using cutadapt ( 59 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [R] -> stage not stated [phyloseq]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Sequencing reads generated from the samples were trimmed and quality control checked with a modified version of Cutadapt ( 50 ).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### An approach for evaluating the effects of dietary fiber polysaccharides on the human gut microbiome and plasma proteome. (PNAS 2022)

- DOI: 10.1073/pnas.2123411119 | PMCID: PMC9171781 | PMID: 35533274
- Evidence: Reads were demultiplexed (bcl2fastq, Illumina), adapter sequences were trimmed (cutadapt) ( 56 ) and the reads were quality filtered (Sickle) ( 57 ).
- Full pipeline: read trimming [Cutadapt, DADA2 v1.13.0] -> alignment/mapping [Picard, featureCounts] -> stage not stated [Bowtie2]

### The Long chain Diol Index: A marine palaeotemperature proxy based on eustigmatophyte lipids that records the warmest seasons. (PNAS 2022)

- DOI: 10.1073/pnas.2116812119 | PMCID: PMC9169758 | PMID: 35412908
- Evidence: Thereafter, primers were removed from the reads using the Cutadapt software ( 72 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [Cutadapt, DADA2]

### Signaling from the RNA sensor RIG-I is regulated by ufmylation. (PNAS 2022)

- DOI: 10.1073/pnas.2119531119 | PMCID: PMC9169834 | PMID: 35394863
- Evidence: RNA-seq data were processed using the TrimGalore toolkit ( 65 ), which employs Cutadapt ( 66 ) to trim low-quality bases and Illumina sequencing adapters from the 3′ end of the reads.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [HTSeq]

### Variation in upstream open reading frames contributes to allelic diversity in maize protein abundance. (PNAS 2022)

- DOI: 10.1073/pnas.2112516119 | PMCID: PMC9169109 | PMID: 35349347
- Evidence: Cutadapt ( 70 ) version 1.18 was run using the parameters “-a CTGTAGGCACCATCAAT -m 20” to remove adapters and discard any reads shorter than 20 bp.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2, HTSeq, SAMtools] -> stage not stated [BLAST, R]

### <i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import. (PNAS 2022)

- DOI: 10.1073/pnas.2123353119 | PMCID: PMC8931380 | PMID: 35275795
- Version used: **1.3**
- Evidence: The sequencing data were processed in SolexaQA ( 34 ) and Cutadapt (version 1.3) software to remove low-quality regions and adapter sequences, respectively.
- Full pipeline: read trimming [Cutadapt v1.3, R, edgeR] -> alignment/mapping [BWA, TopHat, VCFtools] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [SAMtools]

### Vertical stratification of the air microbiome in the lower troposphere. (PNAS 2022)

- DOI: 10.1073/pnas.2117293119 | PMCID: PMC8851546 | PMID: 35131944
- Version used: **1.8.1**
- Evidence: Resulting metagenomic datasets for the air samples were processed with Cutadapt v.1.8.1 ( 29 ) to remove adapter sequences and quality trim the sequencing reads with a Phred quality score cutoff of Q20.
- Full pipeline: quality control [Bowtie2 v2.4.1] -> read trimming [Bowtie2 v2.4.1, Cutadapt v1.8.1] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> visualisation [vegan]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Cutadapt ( 66 ) was used to trim adapters and trimmed sequences were aligned to the mm10 mouse genome assembly using bowtie2 ( 67 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### The embryonic node behaves as an instructive stem cell niche for axial elongation. (PNAS 2022)

- DOI: 10.1073/pnas.2108935119 | PMCID: PMC8812687 | PMID: 35101917
- Evidence: Cutadapt ( 59 ) was used to remove low-quality bases (Phred quality score <20) at the 3′ and 5′ ends, adapter sequences, primer sequences, and poly-A tails of each read.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [TopHat] -> normalisation [Cufflinks]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: Cutadapt ( https://cutadapt.readthedocs.io/en/stable/index.html ) was used to trim adaptors.
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **2.6**
- Evidence: Reads were trimmed to remove adapters from the 3′ end of the reads using Cutadapt 2.6 (AGA TCG GAA GAG CAC ACG TCT GAA CTC CAG TCA C and AAG TCG GAG GCC AAG CGG TCT TAG GAA GAC AA for Illumina- and BGISEQ-sequenced reads, respectively) ( 52 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Version used: **3.2**
- Evidence: In brief, over 30 million raw paired-end reads were trimmed with Cutadapt v3.2.
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### Genome evolution and initial breeding of the Triticeae grass &lt;i&gt;Leymus chinensis&lt;/i&gt; dominating the Eurasian Steppe. (PNAS 2023)

- DOI: 10.1073/pnas.2308984120 | PMCID: PMC10623014 | PMID: 37874858
- Version used: **2.1**
- Evidence: The adaptors of raw small RNAseq reads were trimmed by Cutadapt (v2.1).
- Full pipeline: read trimming [Cutadapt v2.1, Trimmomatic] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BUSCO, InterProScan, RAxML, RepeatMasker]

### A polygenic explanation for Haldane's rule in butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2300959120 | PMCID: PMC10622916 | PMID: 37856563
- Evidence: Raw reads were trimmed with Cutadapt-3.4 ( 49 ) to remove adapters (CTGTCTCTTATACACATCT), and subsequently mapped to the reference genome of P. bianor using the BWA-0.7.17 MEM algorithm.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [BCFtools] -> stage not stated [Picard]

### In vitro DNA repair genomics using XR-seq with &lt;i&gt;Escherichia coli&lt;/i&gt; and mammalian cell-free extracts. (PNAS 2023)

- DOI: 10.1073/pnas.2314233120 | PMCID: PMC10614213 | PMID: 37844222
- Evidence: Adaptor sequences were trimmed by cutadapt ( 39 ), and duplicate reads were removed by fastx_toolkit/0.0.14 ( hannonlab.cshl.edu/fastx_toolkit/index.html ).
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [Bowtie2, Picard]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Version used: **1.18**
- Evidence: Prior to analyzing the sequencing data, adapters were removed from sRNA library data by using cutadapt v1.18, selecting read length from 18 to 26 nt.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### mitoSplitter: A mitochondrial variants-based method for efficient demultiplexing of pooled single-cell RNA-seq. (PNAS 2023)

- DOI: 10.1073/pnas.2307722120 | PMCID: PMC10523499 | PMID: 37725654
- Version used: **1.18**
- Evidence: The scRNA-seq data were aligned to the GRCh38 genome using CellRanger v3.1.0 (for 10× Genomic RNA-seq data) or zUMIs v2.9.7e ( 33 ) (for Well-Paired-Seq data), during the sequence alignment process, and the bulk mitochondria RNA-seq data were quality-filtered using cutadapt v1.18 ( 34 ) and aligned to the mitochondrial sequence in the GRCh38 genome using STAR v2.7.3a ( 35 ).
- Full pipeline: alignment/mapping [Cutadapt v1.18, STAR v2.7.3a, minimap2 v2.24] -> variant calling [Scanpy v1.9.1, minimap2 v2.24] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> stage not stated [scikit-learn v1.0.2]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **1.18**
- Evidence: DNA sequence variant calling was done with the Fast-GBS v2.0 pipeline ( 81 ): Illumina raw reads were demultiplexed with Sabre 1.0 ( 82 ) and trimmed with Cutadapt 1.18 ( 83 ) to remove the adaptors.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### IL-7R licenses a population of epigenetically poised memory CD8<sup>+</sup> T cells with superior antitumor efficacy that are critical for melanoma memory. (PNAS 2023)

- DOI: 10.1073/pnas.2304319120 | PMCID: PMC10372654 | PMID: 37459511
- Evidence: Reads were quality filtered and trimmed of Illumina adapters using FastQC and Cutadapt.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, STAR, featureCounts] -> alignment/mapping [STAR, featureCounts] -> quantification [STAR, featureCounts] -> differential/statistical testing [DESeq2, R v4.0] -> stage not stated [RSEM]

### Diversity of plant DNA in stool is linked to dietary quality, age, and household income. (PNAS 2023)

- DOI: 10.1073/pnas.2304441120 | PMCID: PMC10319039 | PMID: 37368926
- Version used: **3.4**
- Evidence: Using cutadapt v.
- Full pipeline: read trimming [QIIME 2] -> stage not stated [Cutadapt v3.4, DADA2 v1.10.0, phyloseq v1.32.0]

### <i>oskar</i> acts with the transcription factor Creb to regulate long-term memory in crickets. (PNAS 2023)

- DOI: 10.1073/pnas.2218506120 | PMCID: PMC10214185 | PMID: 37192168
- Version used: **3.4**
- Evidence: 16 , including removing adapters and reads shorter than 20 nucleotides with Cutadapt v3.4 ( 66 ) and quantifying the gene expression in transcripts per million with RSEM v1.2.29 ( 67 ), using STAR v2.7.0e1 ( 68 ) as read mapper against the G. bimaculatus genome ( 36 ) ( SI Appendix , Table S8 ).
- Full pipeline: read trimming [Cutadapt v3.4, RSEM v1.2.29, STAR v2.7.0e] -> alignment/mapping [MAFFT v7.510] -> quantification [Cutadapt v3.4, ImageJ, RSEM v1.2.29, STAR v2.7.0e] -> visualisation [RAxML]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Version used: **2.6**
- Evidence: Reads were trimmed using Cutadapt v2.6 to remove Illumina adapters from the 3′ end, and reads were retained that were at least 22 base pairs long ( 51 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **1.16**
- Evidence: Sequence reads were assessed for quality using FastQC v0.11.7 ( 88 ) and trimmed for adaptor content using cutadapt v1.16 ( 89 ).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Hydrogen stable isotope probing of lipids demonstrates slow rates of microbial growth in soil. (PNAS 2023)

- DOI: 10.1073/pnas.2211625120 | PMCID: PMC10120080 | PMID: 37036980
- Version used: **1.8.1**
- Evidence: To prepare samples for analysis with the DADA2 (version 1.10.1) bioinformatic pipeline ( 90 ), reads were demultiplexed with adapters and primers were removed using standard settings for cutadapt (version 1.8.1, Martin 2011).
- Full pipeline: read trimming [Cutadapt v1.8.1, DADA2 v1.10.1]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Evidence: Different strains were identified with the 20-bp unique barcodes using Qiime Cutadapt and visualized with Qiime2 View ( https://qiime2.org ).
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Version used: **1.11.0**
- Evidence: Raw reads were processed and demultiplexed using bcl2fastq (v2.20.2), and low-quality reads were filtered out with Cutadapt v1.11.0 ( 65 ).
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### PCIF1-mediated deposition of 5'-cap &lt;i&gt;N&lt;/i&gt;&lt;sup&gt;6&lt;/sup&gt;,2'-&lt;i&gt;O&lt;/i&gt;-dimethyladenosine in ACE2 and TMPRSS2 mRNA regulates susceptibility to SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210361120 | PMCID: PMC9945940 | PMID: 36689652
- Version used: **1.18**
- Evidence: For the analysis, paired-end reads were trimmed by cutadapt (v1.18) and then mapped to the human genome (hg38) using HISAT2 (v2.1.0).
- Full pipeline: read trimming [Cutadapt v1.18, HISAT2 v2.1.0] -> alignment/mapping [Cutadapt v1.18, HISAT2 v2.1.0] -> quantification [DESeq2, HTSeq v0.11.2] -> stage not stated [SAMtools]

### GRAS transcription factors regulate cell division planes in moss overriding the default rule. (PNAS 2023)

- DOI: 10.1073/pnas.2210632120 | PMCID: PMC9942845 | PMID: 36669117
- Version used: **2.8**
- Evidence: Single-end reads were preprocessed with cutadapt 2.8 ( 75 ) to remove adapter sequences and filter low-quality bases.
- Full pipeline: read trimming [Cutadapt v2.8] -> differential/statistical testing [DESeq2]

### The lncRNA LUCAT1 is elevated in inflammatory disease and restrains inflammation by regulating the splicing and stability of NR4A2. (PNAS 2023)

- DOI: 10.1073/pnas.2213715120 | PMCID: PMC9910463 | PMID: 36577072
- Evidence: The fastq files were trimmed with cutadapt using the options “-a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA —minimum-length 1 -j 15” ( 68 ).
- Full pipeline: read trimming [Cutadapt, minimap2 v2.17] -> alignment/mapping [RSEM v1.3.1, STAR v2.6.1, minimap2 v2.17] -> stage not stated [Bioconductor v3.14]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: The reads were trimmed using Cutadapt ( 95 ), removing the adaptor sequences and bases from the 5’ and 3’ ends with a Phred quality score below 20.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### The glucocorticoid receptor potentiates aldosterone-induced transcription by the mineralocorticoid receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2413737121 | PMCID: PMC11588051 | PMID: 39541347
- Version used: **1.18**
- Evidence: Cutadapt 1.18 was used for adapter removal and quality control.
- Full pipeline: quality control [Cutadapt v1.18] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2, STAR v2.70] -> normalisation [DESeq2] -> stage not stated [HOMER, SAMtools]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: Fastq files were adaptor stripped using cutadapt with a minimum length of 15 and a quality cutoff of 2 (parameters: -a NNNNNNCACTCGGGCACCAAGGAC –minimum-length = 15 –quality-cutoff = 2).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **4.1**
- Evidence: For data analysis, adapter and bad quality bases were removed from fastq files using cutadapt version 4.1 ( 53 ) (-a CTGTCTCTTATACACATCTCCGAGCCCACGAGAC -A CTGTCTCTTATACACATCTGACGCTGCCGACGA -q 30 -m 15).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: Primer sequences were removed using the cutadapt plugin ( 94 ), reads were truncated to a length of 130 bp, filtered, denoised, and chimeric reads were removed using the DADA2 plugin ( 95 ).
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Dynamics of transcription-coupled repair of cyclobutane pyrimidine dimers and (6-4) photoproducts in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416877121 | PMCID: PMC11536166 | PMID: 39441633
- Version used: **3.4**
- Evidence: Post-PCR duplicate removal, we trimmed the 3′-end adaptor using cutadapt version 3.4, allowing flexibility in the unique molecular identifier adaptor region with the sequence: GGCTCAGTTCGTATGAGTGCCGNNNNNNNN.
- Full pipeline: read trimming [Cutadapt v3.4, STAR] -> alignment/mapping [Bowtie2 v2.4.5, STAR] -> stage not stated [BEDTools, Snakemake]

### Toward a CRISPR-based mouse model of &lt;i&gt;Vhl&lt;/i&gt;-deficient clear cell kidney cancer: Initial experience and lessons learned. (PNAS 2024)

- DOI: 10.1073/pnas.2408549121 | PMCID: PMC11474080 | PMID: 39365820
- Evidence: Samples were trimmed for adapters using Cutadapt and the trimmed reads were analyzed with CRISPResso2, a software pipeline designed to enable rapid and intuitive interpretation of genome editing experiments ( 85 ).
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1] -> visualisation [ImageJ v1.53] -> stage not stated [GSEA]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Version used: **4.5**
- Evidence: Read UMIs were processed using cutadapt (version 4.5) to identify UMIs ( 64 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### Conserved 5-methyluridine tRNA modification modulates ribosome translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2401743121 | PMCID: PMC11363252 | PMID: 39159370
- Version used: **2.3**
- Evidence: The reads were trimmed using Cutadapt v2.3 ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.3] -> alignment/mapping [RSEM v1.3.3, STAR v2.7.8a] -> differential/statistical testing [DESeq2]

### Improvement of a mouse infection model to capture &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt; chronic physiology in cystic fibrosis. (PNAS 2024)

- DOI: 10.1073/pnas.2406234121 | PMCID: PMC11331117 | PMID: 39102545
- Version used: **3.4**
- Evidence: Briefly, Illumina adapters were trimmed from RNA-seq reads in cutadapt (v3.4) ( 32 ) using a minimal read length threshold of 22 bps.
- Full pipeline: quality control [Bowtie2 v2.4.2, FastQC v0.11.9] -> read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.4.2, FastQC v0.11.9] -> stage not stated [featureCounts v2.0.1]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **1.8.3**
- Evidence: Raw reads were processed by removing sequencing adapters with Cutadapt v1.8.3 ( 49 ) and the parameters: -u 5 -U 5 -q 25 -m 25.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Life stage-specific poly(A) site selection regulated by <i>Trypanosoma brucei</i> DRBD18. (PNAS 2024)

- DOI: 10.1073/pnas.2403188121 | PMCID: PMC11260167 | PMID: 38990950
- Evidence: Adapter sequences were trimmed using cutadapt.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, R, Seurat]

### Membrane association of active genes organizes the chloroplast nucleoid structure. (PNAS 2024)

- DOI: 10.1073/pnas.2309244121 | PMCID: PMC11252823 | PMID: 38968115
- Version used: **3.5**
- Evidence: Briefly, obtained raw sequencing reads were trimmed using trim_galore v.0.6.7 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) with cutadapt v.3.5 ( 58 ) and mapped to the TAIR10 Arabidopsis plastid genome ( www.arabidopsis.org ) using Bowtie2 v.2.4.4 ( 59 ).
- Full pipeline: read trimming [Bowtie2 v2.4.4, Cutadapt v3.5] -> alignment/mapping [Bowtie2 v2.4.4, Cutadapt v3.5] -> quantification [BEDTools v2.30.0, SAMtools v1.13]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Evidence: Trimming of the r1 adapter was conducted using the Cutadapt tool ( 84 ).
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Version used: **4.1**
- Evidence: Adapter contamination was removed from fastq with cutadapt 4.1 ( 47 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Version used: **3.7**
- Evidence: Adapter sequences were removed from sequencing reads with Cutadapt (v3.7), and their quality was assessed with FASTQC (v0.11.9).
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### CRISPRi screens identify the lncRNA, <i>LOUP</i>, as a multifunctional locus regulating macrophage differentiation and inflammatory signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2322524121 | PMCID: PMC11145268 | PMID: 38781216
- Evidence: SgRNA guide adapters were removed with cutadapt ( 46 ), and counts were obtained with the MAGeCK count function from MAGeCK ( 47 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, deepTools] -> stage not stated [AlphaFold, DESeq2]

### Astrocyte-to-microglia communication via Sema4B-Plexin-B2 modulates injury-induced reactivity of microglia. (PNAS 2024)

- DOI: 10.1073/pnas.2400648121 | PMCID: PMC11145257 | PMID: 38781210
- Evidence: Poly-A/T stretches, and Illumina adapters were trimmed from the reads using cutadapt ( 34 ); resulting reads shorter than 30 bp were discarded.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### Macrophage transplantation rescues RNASET2-deficient leukodystrophy by replacing deficient microglia in a zebrafish model. (PNAS 2024)

- DOI: 10.1073/pnas.2321496121 | PMCID: PMC11126979 | PMID: 38753517
- Version used: **3.4**
- Evidence: Reads (data accession number PRJNA1047321) were trimmed using Cutadapt v3.4 ( 38 ) and then mapped to the GRCz11 genome using Spliced Transcripts Alignment to a Reference v2.7.10b ( 39 ).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [R v4.3, fgsea v1.28.0, ggplot2 v3.4.4] -> stage not stated [HTSeq v2.0]

### Genome-wide CRISPR screens in spheroid culture reveal that the tumor suppressor LKB1 inhibits growth via the PIKFYVE lipid kinase. (PNAS 2024)

- DOI: 10.1073/pnas.2403685121 | PMCID: PMC11127050 | PMID: 38743625
- Evidence: Sequencing reads were trimmed and aligned to the TKOv3 library using Cutadapt and Bowtie.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt]

### 3D intrusions transport active surface microbial assemblages to the dark ocean. (PNAS 2024)

- DOI: 10.1073/pnas.2319937121 | PMCID: PMC11087786 | PMID: 38696469
- Version used: **1.13**
- Evidence: Only sequences with an exact match to both primers were kept and primer sequences were trimmed using Cutadapt v.1.13 ( 74 ).
- Full pipeline: read trimming [Cutadapt v1.13] -> stage not stated [QIIME 2, scikit-learn]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Evidence: The obtained 100 bp paired-end reads were analyzed with FastQC (v 0.11.9) using parameters by default to assess quality, and adaptor sequences removed with Cutadapt (with parameters ‘--minimum-length=20 --max-n=0.1 --quality-cutoff=30,30’) ( 46 ) and then mapped to the TAIR10 A. thaliana reference genome with HISAT2 ( 47 ). htseq-count was used for read count (parameters: ‘--format=bam --order=nam...
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### Cross-kingdom RNA interference mediated by insect salivary microRNAs may suppress plant immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2318783121 | PMCID: PMC11032475 | PMID: 38588412
- Evidence: The resulting raw data underwent quality trimming, which involved the removal of adapters and low-quality sequences, using the Cutadapt tool ( 48 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: DNA methylation was analyzed by using sequencing reads from RRBS that were trimmed and quality filtered by trim galore software (v0.6.7), fastQC ( 27 ), and cutadapt ( 28 ), using default parameters for RRBS.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Version used: **3.4**
- Evidence: Reads were trimmed with Cutadapt v3.4 ( 83 ) with options -e 0.1 -O 3 -m 20.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Version used: **4.1**
- Evidence: Reads were trimmed using Cutadapt v4.1 ( 90 ) with parameters --nextseq-trim=30 --minimum-length=20.
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Genomes of historical specimens reveal multiple invasions of LTR retrotransposons in <i>Drosophila melanogaster</i> during the 19th century. (PNAS 2024)

- DOI: 10.1073/pnas.2313866121 | PMCID: PMC11009621 | PMID: 38564639
- Evidence: We removed the adaptor sequence “TGGAATTCTCGGGTGCCAAGG” using cutadapt [v4.4 ( 75 )] and filtered for reads having a length between 18 and 36 nt.
- Full pipeline: alignment/mapping [BEDTools, MUSCLE v3.8.1551] -> visualisation [Python, ggplot2] -> stage not stated [Cutadapt, RepeatMasker]

### Improved RNA stability estimation through Bayesian modeling reveals most <i>Salmonella</i> transcripts have subminute half-lives. (PNAS 2024)

- DOI: 10.1073/pnas.2308814121 | PMCID: PMC10998600 | PMID: 38527194
- Version used: **4.1**
- Evidence: Afterward, Illumina adapters were removed with Cutadapt v4.1, and STAR ( 73 ) was used to align the reads to the SL1344 genome (NCBI accessions: FQ312003.1 , HE654724.1 , HE654725.1 , and HE654726.1 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [Cutadapt v4.1, HTSeq] -> quantification [HTSeq] -> normalisation [Stan] -> differential/statistical testing [GSEA, Stan] -> simulation/modelling [Stan] -> stage not stated [R, edgeR, limma]

### Root-exuded specialized metabolites reduce arsenic toxicity in maize. (PNAS 2024)

- DOI: 10.1073/pnas.2314261121 | PMCID: PMC10990099 | PMID: 38513094
- Evidence: We removed primers with cutadapt [V3.4, ( 70 )] and used sequence headers information to demultiplex the data.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> differential/statistical testing [R v4.1.2]

### Mutations of the circadian clock genes &lt;i&gt;Cry&lt;/i&gt;, &lt;i&gt;Per,&lt;/i&gt; or &lt;i&gt;Bmal1&lt;/i&gt; have different effects on the transcribed and nontranscribed strands of cycling genes. (PNAS 2024)

- DOI: 10.1073/pnas.2316731121 | PMCID: PMC10895256 | PMID: 38359290
- Evidence: Flanking adapter sequences were removed from the reads using cutadaptor ( https://cutadapt.readthedocs.io/en/stable/index.html ) with command options -a T​GGA​ATT​CTC​GGG​TGC​CAA​GGA​ACT​CCA​GTN​NNN​NNA​CGA​TCT​CGT​ATGCCGTCTTCTGCTTG --discard-untrimmed -m 24 -M 29 -o.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2] -> stage not stated [STRING db]

### A recent gibbon ape leukemia virus germline integration in a rodent from New Guinea. (PNAS 2024)

- DOI: 10.1073/pnas.2220392121 | PMCID: PMC10861895 | PMID: 38305758
- Version used: **1.15**
- Evidence: The raw sequencing reads were demultiplexed, adaptor sequences, low-quality reads (quality cutoff 20 and minimum read length of 30 nt), and duplicates were removed and merged using Cutadapt v1.15 ( 44 ), Trimmomatic v0.27 ( 45 ), Picard v1.4 ( http://broadinstitute.github.io/picard ), and BBMerge ( 46 ), respectively.
- Full pipeline: read trimming [Cutadapt v1.15, Picard v1.4, Trimmomatic v0.27] -> alignment/mapping [PyMOL v2.4] -> differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7] -> stage not stated [QGIS v3.16.10, RAxML v8.2.11]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: Adapter content and quality trimming were performed using Cutadapt ( 53 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### A metabolic cell death program downstream of SARM1 couples NAD&lt;sup&gt;+&lt;/sup&gt; depletion to BAX activation and APAF1 degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2522444122 | PMCID: PMC12718333 | PMID: 41364765
- Evidence: ...INACLIP: Genetrap_adapter.fa:2:30:10 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36.” Next, the 5′ common primer sequence of the Gene trap was trimmed using Cutadapt with the command: “cutadapt -j 8 -g CTTGTCTTCGTTGGGAGTGAATTAGCCCTTCCA -m 35 xxx.fastq.gz -o xxx_0.fastq.gz.” Subsequently, the 3′ common sequence of the Gene trap was removed using another Cutadapt command: “cutadapt -j 8 -a “A {10}” -m 35 x...
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, Trimmomatic] -> quantification [featureCounts] -> stage not stated [RSEM]

### Combination of Cas9 and adeno-associated vectors enables efficient in vivo knockdown of precise miRNAs in the rodent and primate brain. (PNAS 2025)

- DOI: 10.1073/pnas.2513076122 | PMCID: PMC12718335 | PMID: 41359835
- Evidence: Then, each of these fastq files were further trimmed using the cutadapt ( https://github.com/marcelm/cutadapt?tab=readme-ov-file ) to produce the corresponding preMiR sequences of fastq files.
- Full pipeline: read trimming [BLAST, Cutadapt] -> alignment/mapping [BLAST, DESeq2 v1.44.0] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.44.0, R]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Version used: **3.2**
- Evidence: Adapter sequences were trimmed using Cutadapt version 3.2, and the processed reads were aligned to the HuNoV reference genome (Norovirus GII.2 strain Env/CHN/2016/GII.P16-GII.2/BJSMQ, GenBank accession number: NC039476) using BWA version 0.7.17.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Version used: **4.9**
- Evidence: Adapter sequences were trimmed from raw reads with cutadapt v4.9 ( 52 ).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Version used: **1.15**
- Evidence: Sequences were quality trimmed and filtered using Trim Galore (v0.4.5) and cutadapt (v1.15), then trimmed reads were filtered for rRNA by the SortMeRNA ( 91 ) program, and de novo assembled into transcripts using the Trinity program ( 92 ) (v2.8.4).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### Neuronal plasticity at puberty in mouse hypothalamic &lt;i&gt;Kiss1&lt;/i&gt; neurons that control fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2512855122 | PMCID: PMC12582290 | PMID: 41118223
- Evidence: Trimmomatic 0.38 and Cutadapt were used to remove low-quality reads and adapter sequences, respectively, and remaining reads were mapped to the Ensembl mm107 mouse reference genome using STAR (v 2.7.9a).
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Emergence of antiphage functions from random sequence libraries reveals mechanisms of gene birth. (PNAS 2025)

- DOI: 10.1073/pnas.2513255122 | PMCID: PMC12557735 | PMID: 41091762
- Evidence: Merged reads were processed with cutadapt ( 71 ) to remove flanking sequences and isolate the random sequences with their start and stop codons.
- Full pipeline: stage not stated [AlphaFold, Cutadapt, ImageJ]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Version used: **1.8**
- Evidence: Raw reads were trimmed and filtered for short sequences using cutadapt v.1.8 ( 27 ), setting minimum-length option to 18, error-rate 0.2, and overlap 5.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Sperm and offspring production in a nonobstructive azoospermia mouse model via testicular mRNA delivery using lipid nanoparticles. (PNAS 2025)

- DOI: 10.1073/pnas.2516573122 | PMCID: PMC12557808 | PMID: 41082659
- Version used: **3.2**
- Evidence: Sequencing reads were trimmed to remove adapter sequences using cutadapt (v3.2), and the resulting high-quality reads were aligned to the mouse reference genome (GRCm39) using bowtie2 (v2.3.5.1) with default parameters.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt v3.2] -> alignment/mapping [Bowtie2 v2.3.5.1, Cutadapt v3.2, SAMtools v1.20] -> stage not stated [deepTools]

### Endosome transcriptomics reveal trafficking of Cajal bodies into multivesicular bodies. (PNAS 2025)

- DOI: 10.1073/pnas.2511840122 | PMCID: PMC12541449 | PMID: 41060753
- Evidence: Raw sequencing reads from OTTR libraries were trimmed and low-quality reads were removed using cutadapt: cutadapt -q 10 -u 7 -a NGATCGGAAGAGCACACG -m 15 -o path/to/output.fq.gz path/to/input.fq.gz For increased confidence, two analysis methods to align and quantify transcripts were used: 1. tRAX maps reads prioritizing tRNAs, followed by other ncRNAs ( 75 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, SAMtools] -> quantification [Cutadapt]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Version used: **4.8**
- Evidence: Reads were trimmed using Cutadapt (v4.8) ( 55 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### The role of colony morphotype in shaping gene essentiality in &lt;i&gt;Mycobacteroides abscessus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500719122 | PMCID: PMC12519085 | PMID: 41026822
- Version used: **3.3**
- Evidence: This script selects for reads possessing the MycoMar Inverted Repeat (IR) (CAACCTGT) using Cutadapt v3.3, maps the reads to MAB ATCC 19977 (GCF_000069185.1) with Bowtie2 v2.4.2, and assigns each read to an insertion site.
- Full pipeline: stage not stated [Bowtie2 v2.4.2, Cutadapt v3.3, DESeq2 v1.18.1, R v3.4]

### Inorganic sulfate is critical for &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; lung tissue colonization and redox balance. (PNAS 2025)

- DOI: 10.1073/pnas.2503966122 | PMCID: PMC12501120 | PMID: 40982672
- Version used: **4.9**
- Evidence: Raw sequencing data were processed using Cutadapt (v4.9) to remove adapter sequences and homopolymers, followed by Ribodetector (v0.3.1) to filter out ribosomal reads.
- Full pipeline: read trimming [Cutadapt v4.9] -> quantification [edgeR] -> normalisation [edgeR] -> stage not stated [ImageJ]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: Raw RNA-seq reads were trimmed using cutadapt-1.9.1 ( 44 ) and mapped to Arabidopsis thaliana TAIR10 reference genome using STAR-2.5.a ( 45 ), featureCounts ( 46 ) was used to count the numbers of reads mapped to each gene.
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### De novo rates of a &lt;i&gt;Trypanosoma&lt;/i&gt;-resistant mutation in two human populations. (PNAS 2025)

- DOI: 10.1073/pnas.2424538122 | PMCID: PMC12415191 | PMID: 40854136
- Evidence: Merged sequences were trimmed from Illumina adapters using Cutadapt ( 105 ) and quality-filtered by Trimmomatic ( 106 ), using a sliding window size of 3 bp, a Phred quality threshold of 30 and a minimum read length threshold of 90 bp.
- Full pipeline: read trimming [Cutadapt, Trimmomatic] -> alignment/mapping [BWA]

### Global profiling of N-terminal cysteine-dependent degradation mechanisms. (PNAS 2025)

- DOI: 10.1073/pnas.2501681122 | PMCID: PMC12377780 | PMID: 40794836
- Evidence: Raw Illumina reads derived from each GPS bin were first trimmed of constant sequences derived from the Ub-GPS vector backbone using Cutadapt ( 65 ) and count tables were generated from reads that aligned perfectly to the reference sequence.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> stage not stated [ImageJ]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Version used: **4.1**
- Evidence: We used cutadapt v4.1 ( 35 ) to preprocess sRNA-seq reads by removing the first 5’ nucleotide (-u 1), trimming the 3’ adapter (-a TGGAATTCTCGGGTGCCAAGG), and filtering reads outside the length range of 19-nt to 25-nt (--minimum-length 19 to --maximum-length 25).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: Low quality reads were filtered and the adaptors were trimmed using Cutadapt ( 58 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### SCoTCH-seq reveals that 5-hydroxymethylcytosine encodes regulatory information across DNA strands. (PNAS 2025)

- DOI: 10.1073/pnas.2512204122 | PMCID: PMC12337322 | PMID: 40743391
- Version used: **4.6**
- Evidence: First, target reads were filtered (based on their containing the correct configuration of adapter sequences) and trimmed using Cutadapt (v4.6) ( 43 ).
- Full pipeline: read trimming [Cutadapt v4.6, Picard v3.1.1, SAMtools v1.19.2] -> stage not stated [BEDTools v2.31.0, Snakemake v7.3.8, deepTools]

### Trigger factor accelerates nascent chain compaction and folding. (PNAS 2025)

- DOI: 10.1073/pnas.2422678122 | PMCID: PMC12318149 | PMID: 40711920
- Evidence: We first used cutadapt to remove adapter sequences and discard short (<20 nt) and long (>45 nt) reads.
- Full pipeline: read trimming [Cutadapt]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: Raw .fastq files were trimmed for adapter sequences using cutadapt and subsequently aligned with bwa mem using default parameters as previously described ( 48 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Version used: **2.8**
- Evidence: Sequencing adapters were then trimmed using Cutadapt v2.8 ( 57 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: Cutadapt ( 32 ) was used to trim reads to the bare sgRNA sequences.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Version used: **1.15**
- Evidence: Cutadapt v1.15 ( 49 ) has been used to remove Illumina TruSeq adapter from the sequencing data and to remove bases with a quality score lower than 20, in both 5′ and 3′ ends of the reads.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Version used: **2.4**
- Evidence: Reads containing adapters were removed using Cutadapt version 2.4 ( 95 ) and reads were mapped to the D. melanogaster transcriptome, FlyBase genome release 6.29, using Kallisto (version 0.46.0) ( 96 ) with default parameters.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Bidirectional disruption of &lt;i&gt;GNAS&lt;/i&gt; transcripts causes broad methylation defects in pseudohypoparathyroidism type 1B. (PNAS 2025)

- DOI: 10.1073/pnas.2423271122 | PMCID: PMC12037034 | PMID: 40249781
- Evidence: After removing the adaptor sequences on the Galaxy server 24.2.rc1, using Cutadapt, sequences were aligned to the reference genome (GRCh38) using RNA STAR and visualized on Integrative Genomics Viewer (IGV, Ver2.19.1) ( 8 ).
- Full pipeline: alignment/mapping [Cutadapt, Galaxy v24.2, minimap2] -> visualisation [Cutadapt, Galaxy v24.2]

### Colony pattern multistability emerges from a bistable switch. (PNAS 2025)

- DOI: 10.1073/pnas.2424112122 | PMCID: PMC12002352 | PMID: 40184178
- Version used: **4.2**
- Evidence: Briefly, raw sequencing files were trimmed adapters using cutadapt (v4.2) ( 55 ).
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9] -> quantification [SAMtools v1.9] -> machine learning [Cellpose] -> stage not stated [ImageJ v1.53c]

### Large-scale combination screens reveal small-molecule sensitization of antibiotic-resistant gram-negative ESKAPE pathogens. (PNAS 2025)

- DOI: 10.1073/pnas.2402017122 | PMCID: PMC12002207 | PMID: 40127266
- Version used: **3.4**
- Evidence: Sequencing reads were adapter trimmed using cutadapt (v3.4) and mapped to sgRNAs using a custom python script (count_guides.py) ( 64 ).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> stage not stated [Python, Snakemake]

### Pulsatile flow induces chromatin interaction with lamin-associated proteins to enrich H3K9 methylation in endothelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424566122 | PMCID: PMC11962468 | PMID: 40117319
- Evidence: In brief, reads were trimmed using cutadapt.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [HOMER, ImageJ, MACS2, OpenCV]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **4.1**
- Evidence: The 16S rRNA gene amplicon data were initially processed with Cutadapt v4.1 ( 34 ) to remove primer sequences.
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Competition for shared resources increases dependence on initial population size during coalescence of gut microbial communities. (PNAS 2025)

- DOI: 10.1073/pnas.2322440122 | PMCID: PMC11929384 | PMID: 40063808
- Evidence: Raw sequencing reads were annotated and demultiplexed using UMI-tools ( 92 ), and primer and adapter sequences were trimmed using cutadapt ( 93 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [R] -> stage not stated [DADA2]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Version used: **1.10**
- Evidence: Using cutadapt v1.10, we performed quality trimming and poly A and adapter trimming.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### tRNA selectivity during ribosome-associated quality control regulates the critical sterility-inducing temperature in two-line hybrid rice. (PNAS 2025)

- DOI: 10.1073/pnas.2417526122 | PMCID: PMC11831146 | PMID: 39913205
- Version used: **1.18**
- Evidence: To refine the raw sequencing data, low-quality reads and 3′-end adaptors were eliminated using Cutadapt (1.18) ( 56 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.2.9, Clustal Omega] -> structure determination [Cutadapt v1.18] -> stage not stated [ImageJ, RoseTTAFold]

### Estimating realized relatedness in free-ranging macaques by inferring identity-by-descent segments. (PNAS 2025)

- DOI: 10.1073/pnas.2401106122 | PMCID: PMC11760927 | PMID: 39808663
- Evidence: After quality control (removing bases with Phred-score of a base call <20 starting from both 5′ and 3′ end of each read) and adapter trimming using cutadapt ( 82 ), we aligned the resulting reads to the rhesus macaque reference genome Mmul10 ( 83 ) using hisat2 ( 84 ).
- Full pipeline: quality control [Cutadapt, HISAT2] -> read trimming [Cutadapt, HISAT2] -> alignment/mapping [BCFtools v1.9, Cutadapt, HISAT2] -> variant calling [BCFtools v1.9] -> simulation/modelling [R v4.4] -> stage not stated [Picard]

### Escalation of genome defense capacity enables control of an expanding meiotic driver. (PNAS 2025)

- DOI: 10.1073/pnas.2418541122 | PMCID: PMC11745323 | PMID: 39772737
- Evidence: The adaptor sequences were trimmed using cutadapt.
- Full pipeline: read trimming [Cutadapt] -> variant calling [kallisto] -> quantification [kallisto] -> differential/statistical testing [DESeq2]

### Mitochondrial DNA lineages determine tumor progression through T cell reactive oxygen signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2417252121 | PMCID: PMC11725793 | PMID: 39752523
- Evidence: The RNA sequence read data were preprocessed including the trimming of Poly-A/T stretches and Illumina adapters using cutadapt ( 53 ).
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R] -> stage not stated [MACS2, pheatmap]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Evidence: ...5.2), samtools ( 61 ) (v1.13), star ( 62 ) (v2.6.1d), stringtie ( 63 ) (v2.1.7), Trimgalore (v0.6.7, GitHub—FelixKrueger/TrimGalore: A wrapper around Cutadapt and FastQC to consistently apply adapter and quality trimming to FastQ files, with extra functionality for RRBS data), cutadapt ( 64 ) (v3.4) and ucsc (v377).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **2.7**
- Evidence: Reads lacking primers and those outside the length range (1,200 to 1,650 bp) were discarded through quality filtering with Cutadapt (version 2.7) ( 66 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Genome-wide CG hypomethylation of the &lt;i&gt;Arabidopsis&lt;/i&gt; ecotype Cvi linked to structural variation and RNAi at the &lt;i&gt;VIM4&lt;/i&gt;-&lt;i&gt;VIM2&lt;/i&gt; locus. (PNAS 2026)

- DOI: 10.1073/pnas.2603682123 | PMCID: PMC13213937 | PMID: 42154559
- Version used: **4.1**
- Evidence: Adapters were trimmed using Cutadapt (v4.1, -m 20 ) ( 33 ).
- Full pipeline: read trimming [Bowtie2 v2.4.2, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [MACS2]

### Functional dissection of &lt;i&gt;SPOP&lt;/i&gt; at the amino acid level reveals a comprehensive functional landscape of variants during tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523210123 | PMCID: PMC13167761 | PMID: 42090249
- Evidence: Error-corrected long-reads were subsequently filtered by length using Seqkit ( 48 ), and regions outside the ORF were trimmed using cutadapt ( 49 ).
- Full pipeline: read trimming [Cutadapt, minimap2] -> alignment/mapping [STAR, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> visualisation [PyMOL] -> stage not stated [DESeq2, GATK, R]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **2.3**
- Evidence: The paired-end read files had adapters removed using Cutadapt v2.3 ( 47 ) and merged using FLASH v1.2.11 ( 48 ).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: The pipeline steps included fastq trimming using Cutadapt (DOI: 10.14806/ej.17.1.200 ) with the following parameters: -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -a “A” --times 2 -u 3 -u -3 -q 20 -m 25.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### The Japanese Archipelago sheltered cave lions, not tigers, during the Late Pleistocene. (PNAS 2026)

- DOI: 10.1073/pnas.2523901123 | PMCID: PMC12890994 | PMID: 41587328
- Version used: **3.2**
- Evidence: The reads were further filtered and trimmed using Cutadapt v3.2 ( 77 ).
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [ANGSD, BWA v0.7.17, SAMtools v1.11] -> stage not stated [MAFFT v7.505, Python]

### A bacterial translation activator with an intrinsically disordered RNA-binding region. (PNAS 2026)

- DOI: 10.1073/pnas.2519770123 | PMCID: PMC12818456 | PMID: 41543904
- Version used: **2.10**
- Evidence: Raw sequencing reads were processed to remove adaptor sequences, low complexity reads, and low-quality ends using cutadapt version 2.10 ( 60 ).
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, HTSeq, R] -> quantification [Bowtie2, DESeq2, HTSeq, R] -> stage not stated [Cutadapt v2.10]

### Mutation rate variability in viral populations: Implications for lethal mutagenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523734123 | PMCID: PMC12799177 | PMID: 41512024
- Evidence: Sequence reads were trimmed using cutadapt (Version 1.18) ( 46 ) and aligned to the A/Netherlands/499/2017 genome sequence using BWA (version 0.7.17) ( 47 ).
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt] -> alignment/mapping [BWA v0.7.17, Cutadapt]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: Libraries were trimmed using cutadapt ( 64 ) based on known adapters with quality thresholds -q 15,10.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: Sample barcodes and sequencing adapter sequences were trimmed off using cutadapt.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Version used: **1.4.1**
- Evidence: Analysis of CRISPR screen results 20 nt sgRNA sequences were trimmed from backbone sequences using Cutadapt (version 1.4.1) (5’ GACGAAACACCG, 3’ GTTTTAGAGCTA). sgRNA sequences were aligned to reference sgRNA libraries using Bowtie2 (version 1.2.3). sgRNAs with counts less than 20 (genome-wide screens) or 50 (all other screens) in either of the populations were excluded from the analysis.
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Version used: **2.5**
- Evidence: PiggyBac ITR sequences were trimmed from read2 using cutadapt (v2.5) with the following parameters: -cores=4–discard-untrimmed -e 0.2 -m 10 -a CCCTAGAAAGATA ( 66 ).
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Version used: **4.6**
- Evidence: Raw reads were subjected to adapter and quality trimming using cutadapt (v4.6; parameters: -quality-cutoff 20 –overlap 5 –minimum-length 25; Illumina TruSeq adapter clipped from both reads), followed by trimming of 10 and 5 nucleotides from the 5′ and 3′ end of the first read and 15 and 5 nucleotides from the 5′ and 3′ end of the second read.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Version used: **3.1**
- Evidence: RNA-seq data processing pipeline: Adaptors were first trimmed from raw sequencing FastQ files using Cutadapt (version 3.1) for removing the last 122 bases of each Read 1 sequence (with parameters -u -122) followed by quality assessment using FastQC.
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Version used: **1.18**
- Evidence: Sequencing quality of fastq files was evaluated with FastQC, and adaptors were trimmed using Cutadapt (1.18).
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Paired-end reads were trimmed to include only the trigger sequences (i.e. between the ATG start codon and TAA stop codon) using the cutadapt tool ( https://cutadapt.readthedocs.io/en/stable/ ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: Adapter trimming, low-quality sequence removal, and quality control were performed using Cutadapt and FastQC, respectively, both of which are incorporated within Trim Galore (v0.6.6) ( 99 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

