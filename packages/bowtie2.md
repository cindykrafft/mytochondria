# Bowtie2

- **Category:** genomics
- **Papers in survey:** 477
- **Journals:** PNAS (239), Nature (190), Cell (37), Science (11)
- **Years:** 2021 (44), 2022 (80), 2023 (91), 2024 (110), 2025 (101), 2026 (51)
- **Versions named:** 2.4.2 (24), 2.4.5 (20), 2.3.5.1 (19), 2.4.1 (17), 2.3.5 (14), 2.3.4.1 (13), 2.2.9 (12), 2.2.5 (11), 2.3.4.3 (10), 2.5.1 (8)
- **Pipeline stages it appears in:** alignment/mapping (417), read trimming (125), quality control (25), quantification (20), differential/statistical testing (5), visualisation (3), variant calling (1)

## Papers

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: ...unts Liao et al., 2014 N/A DESeq2 Love et al., 2014 N/A Morpheus Broad Institute N/A DAVID Huang et al., 2009 N/A Trimmomatic Bolger et al., 2014 N/A Bowtie2 Langmead and Salzberg, 2012 N/A SAM tools Li et al., 2009 N/A MACS2 Zhang et al., 2008 N/A Bedtools Quinlan and Hall, 2010 N/A Resource availability Lead contact Further information and requests for resources and reagents should be directed a...
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Identification of novel bat coronaviruses sheds light on the evolutionary origins of SARS-CoV-2 and related viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.008 | PMCID: PMC8188299 | PMID: 34147139
- Version used: **2.4.1**
- Evidence: ...es 1-740 This paper GenBank: NP_001358344 pEGFP-N1 MiaoLingPlasmid Cat# P0133 pEGFP-N1-hACE2 This paper GenBank: NP_001358344 Software and Algorithms Bowtie2 v2.4.1 Langmead and Salzberg, 2012 http://bowtiebio.sourceforge.net/bowtie2 Kraken v2.0.9 Wood et al., 2019 https://ccb.jhu.edu/software/kraken/ Geneious v2021.0.1 The Biomatters development team https://www.geneious.com/ MAFFT v7.450 Nakamur...
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.450] -> stage not stated [BLAST, Bowtie2 v2.4.1, PyMOL v2.4.0a, RAxML, SAMtools v1.10]

### A global metagenomic map of urban microbiomes and antimicrobial resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.002 | PMCID: PMC8238498 | PMID: 34043940
- Version used: **2.3.0**
- Evidence: ...aper https://pngb.io/metasub-2021 Software and algorithms AdapterRemoval v2.17 Schubert et al., 2016 https://github.com/mikkelschubert/adapterremoval Bowtie2 v2.3.0 Langmead and Salzberg, 2013 https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.0/ BLASTn Altschul et al., 1990 https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ KrakenUniq v0.3.2 Breitwieser et al., 2018 https://...
- Full pipeline: read trimming [BLAST, Bowtie2 v2.3.0] -> dimensionality reduction/clustering [R, UMAP] -> structure determination [R] -> visualisation [UMAP] -> stage not stated [Jupyter, SciPy]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: In the case of N. vectensis , we used all available MARS-seq data ( Sebé-Pedrós et al., 2018a ), we re-processed raw reads with same parameters as defined above for S . pistillata (e.g., using STAR read mapping instead of bowtie2 as in the original publication), and we filtered out cells with less than 100 or more than 10,000 UMIs.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### A single-embryo, single-cell time-resolved model for mouse gastrulation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.004 | PMCID: PMC8162424 | PMID: 33932341
- Evidence: In Brief, After removing plate barcodes (4 base pairs) from Read 1, reads were mapped to the mm9 genome using bowtie2.
- Full pipeline: alignment/mapping [Bowtie2]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **2.3.5.1**
- Evidence: ...sion 1.2.3) bcbio https://github.com/bcbio/bcbio-nextgen Atropos (version 1.1.25) Didion, Martin and Collins, 2017 https://github.com/jdidion/atropos Bowtie2 (version 2.3.5.1) Langmead and Salzberg, 2012 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml samblaster (version 0.1.25) Faust and Hall, 2014 https://github.com/GregoryFaust/samblaster VarDict (version 1.6) Lai et al., 2016b https://gi...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Version used: **2.3.4.1**
- Evidence: The quality-controlled reads were aligned to the reference human genome (hg19/GRCh37) using bowtie2 (version 2.3.4.1) ( Langmead and Salzberg, 2012 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Soluble ACE2-mediated cell entry of SARS-CoV-2 via interaction with proteins related to the renin-angiotensin system. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.053 | PMCID: PMC7923941 | PMID: 33713620
- Evidence: ...alysis Through Evolutionary Relationships) Mi et al., 2019 http://www.pantherdb.org/ Cutadapt Martin, 2011 https://cutadapt.readthedocs.io/en/stable/ Bowtie2 Langmead and Salzberg, 2012 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml HTSeq Anders et al., 2015 https://htseq.readthedocs.io/en/master/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html R Gu ...
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> stage not stated [Bowtie2, Cutadapt, DESeq2, HTSeq]

### In vivo structural characterization of the SARS-CoV-2 RNA genome identifies host proteins vulnerable to repurposed drugs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.008 | PMCID: PMC7871767 | PMID: 33636127
- Evidence: .../icSHAPE-pipe IGV ( Robinson et al., 2011 ) https://software.broadinstitute.org/software/igv/ VARNA v3-93 ( Darty et al., 2009 ) http://varna.lri.fr/ Bowtie2 ( Langmead and Salzberg, 2012 ) http://bowtie-bio.sourceforge.net/bowtie2/index.shtml STAR Dobin et al., 2013 https://github.com/alexdobin/STAR samtools ( Li et al., 2009 ) http://samtools.sourceforge.net/ Trimmomatic Bolger et al., 2014 http...
- Full pipeline: read trimming [Bowtie2, SAMtools, Trimmomatic] -> alignment/mapping [MAFFT v7.313] -> differential/statistical testing [SciPy] -> simulation/modelling [UCSF Chimera] -> structure determination [UCSF Chimera] -> visualisation [RAxML v8.2.12] -> stage not stated [AutoDock Vina]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Version used: **2.2.9**
- Evidence: ...Trono Addgene Cat#12260 VSVG Stewart et al., 2003 Addgene Cat#8454 pLenti6/V5-DEST-HMGB1 Scott et al., 2011 Addgene Cat#31208 Software and Algorithms Bowtie2 v2.2.9 Langmead and Salzberg, 2012 N/A Cutadapt Martin, 2011 N/A DESeq2 v1.32 Love et al., 2014 N/A deeptools v3.1.3 Ramírez et al., 2016 N/A Flowjo 10.6.2 FLOWJO https://www.flowjo.com Graphpad Prism 8 Graphpad software https://www.graphpad....
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: ...dy N/A Software and algorithms CRISPR design https://www.benchling.com N/A R https://www.r-project.org N/A MACS2.0 https://github.com/taoliu/MACS N/A Bowtie2 Langmead and Salzberg, 2012 N/A Samtools http://samtools.sourceforge.net N/A HiCUP v0.8.1 Wingett et al., 2015 N/A Cooltools https://zenodo.org/record/5214125 N/A Juicer Durand et al., 2016 N/A Genrich https://github.com/jsh58/Genrich/ N/A UC...
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: ...etabat Concoct 1.0.0 Alneberg et al., 2014 https://github.com/BinPro/CONCOCT BowTie2 2.2.3 Langmead and Salzberg, 2012 https://github.com/BenLangmead/bowtie2 SAMtools 0.1.19 Li et al., 2009 https://github.com/samtools/samtools metaWRAP 1.1.2) Uritskiy et al., 2018 https://github.com/bxlab/metaWRAP CheckM (v.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### The intrinsic and extrinsic effects of TET proteins during gastrulation. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.049 | PMCID: PMC9432429 | PMID: 35908548
- Evidence: ...zenodo.6720248 ImageJ Schneider et al., 2012 https://imagej.nih.gov/ij/ Prism GraphPad https://www.graphpad.com/ FlowJo FlowJo https://www.flowjo.com Bowtie2 Langmead and Salzberg, 2012 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml Bissli2 https://github.com/tanaylab/bissli2 https://github.com/tanaylab/bissli2 Resource availability Lead contact Further information and requests for resource...
- Full pipeline: stage not stated [Bowtie2, HOMER, ImageJ]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...MACS version 2.1.1.20160309 Recombinant Identification Program Los Alamos National Laboratory, https://www.hiv.lanl.gov/content/sequence/RIP/RIP.html Bowtie2 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml version 2.2.9 Homer http://homer.ucsd.edu/homer/interactions/ version 4.10.3 FitHiC2 https://bioconductor.org/packages/release/bioc/html/FitHiC.html version 1.20.0 FIREcaller https://githu...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: ATAC and ChIPmentation The quality of the FASTQ files from ATAC-seq and ChIPmentation were assessed using FASTQC, and the reads aligned to the mm9 mouse genome, using bowtie2.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### Systematic identification and characterization of genes in the regulation and biogenesis of photosynthetic machinery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.007 | PMCID: PMC10760936 | PMID: 38065083
- Evidence: The paired-end 150nt reads were aligned to a reference file that combined the v5.5 Chlamydomonas genome (from Phytozome), the chloroplast and mitochondrial genomes (from NCBI: chloroplast_BK000554.2.gb and mitochondrion_U03843.1.gb) and our CIB1 cassette, 25 using the command “bowtie2 -sensitive-local -k 10 -I 100 -X 650 -S”.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [SciPy] -> stage not stated [AlphaFold, Cutadapt, PyMOL]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: Ribosomal RNA and tRNA reads were removed by bowtie2 alignment with human tRNA and rRNA sequences 102 .
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Version used: **2.3.0**
- Evidence: Next, bowtie2 (version 2.3.0) 107 with default parameters was used to discard reads mapping to rRNA (Genbank identifier U13369.1 ) and to verify the absence of mycoplasma contamination.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Version used: **2.2.9**
- Evidence: Reads were aligned to reference genome (mm10) using Bowtie2 (version 2.2.9) and deduplicated with Java (version 2.3.0) Picard tools ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Version used: **2.4.2**
- Evidence: 10005903 Software and algorithms Trim Galore! v0.0.6 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/ projects/trim_galore/ Bowtie2 v2.4.2 Langmead and Salzberg 69 https://github.com/BenLangmead/bowtie2 SAMtools v1.12 Li et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### Alarming antibody evasion properties of rising SARS-CoV-2 BQ and XBB subvariants. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.018 | PMCID: PMC9747694 | PMID: 36580913
- Version used: **2.3.4**
- Evidence: 43 RRID: Addgene_154104 Software and algorithms Cutadapt v2.1 Martin 44 https://cutadapt.readthedocs.io/en/v2.1/ Bowtie2 v2.3.4 Langmead et al.
- Full pipeline: stage not stated [Bowtie2 v2.3.4, Cutadapt v2.1, PyMOL v2.3.2]

### A replisome-associated histone H3-H4 chaperone required for epigenetic inheritance. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.006 | PMCID: PMC11380579 | PMID: 39094570
- Evidence: ...01591 JalView University of Dundee RRID:SCR_006459 AcquireMP Refeyn, Ltd N/A DiscoverMP Refeyn, Ltd N/A ASTRA, version 7.3.2.21 Wyatt RRID:SCR_016255 Bowtie2 John Hopkins University RRID:SCR_016368 MACS Dana Farber Cancer Institute RRID:SCR_013291 DANPOS Baylor College of Medicine RRID:SCR_015527 Other MagNA Lyser Instrument Roche Cat# 3358968001 QuantStudio ™ 7 Flex Real-Time PCR System, 384-well...
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, ColabFold, UCSF Chimera] -> stage not stated [AlphaFold, Bowtie2, MACS2]

### The fork protection complex promotes parental histone recycling and epigenetic memory. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.017 | PMCID: PMC11383432 | PMID: 39094569
- Version used: **2.4.2**
- Evidence: 111 https://www.rbvi.ucsf.edu/chimerax/ Bowtie2 v2.4.2 Langmead and Salzberg 112 https://github.com/BenLangmead/bowtie2 SAMtools v1.12 Danecek et al.
- Full pipeline: differential/statistical testing [R v4.2.2] -> visualisation [PyMOL v1.2r, ggpubr v0.6.0] -> stage not stated [AlphaFold, Bowtie2 v2.4.2, ChimeraX, MACS2, SAMtools v1.12, deepTools]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Evidence: 140 Contigs larger than 2.5 kb were retained, and sequencing reads from all samples were mapped against each resulting assembly utilizing Bowtie2.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Evidence: 106 https://sourceforge.net/projects/subread/ BowTie2 v2.2.5 Langmead and Salzberg 107 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml Samtools v1.5 Danecek et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: Adapters and low-quality reads were trimmed using Trimmomatic 99 and aligned to the human genome (GRCh38) using Bowtie2.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Microglia maintain structural integrity during fetal brain morphogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.012 | PMCID: PMC10869139 | PMID: 38309258
- Evidence: ...rm 0.3.5 N/A https://github.com/satijalab/sctransform ; RRID: SCR_022146 R package: GlmGamPoi 1.10.2 N/A https://bioconductor.org/packages/glmGamPoi/ Bowtie 2 N/A http://bowtie-bio.sourceforge.net/bowtie2/index.shtml ; RRID: SCR_016368 Illumina HiSeq 4000 system Ilumina https://www.illumina.com/systems/sequencing-platforms/hiseq-3000-4000.html ; RRID: SCR_020127 Rhapsody analysis pipeline BD Biosc...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Bowtie2, ImageJ, Metascape v3.5.20230501, R, Seurat v4.3.0.1, ggplot2, tidyverse]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: ...re Store https://process.innovation.ox.ac.uk/software/ Lanceotron https://doi.org/10.1093/bioinformatics/btac525 https://lanceotron.molbiol.ox.ac.uk/ bowtie2 https://doi.org/10.1038/nmeth.1923 https://github.com/BenLangmead/bowtie2 JASPAR https://doi.org/10.1093/nar/gkab1113 https://jaspar.genereg.net/ DESeq2 https://doi.org/10.1186/s13059-014-0550-8 http://www.bioconductor.org/packages/release/bi...
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Version used: **2.2.1**
- Evidence: ATAC-seq analysis All zebrafish ATAC-Seq datasets were aligned to build version Zv9/danRer7 of the zebrafish genome using Bowtie2 (version 2.2.1) 53 with the following parameters: –end-to-end, -N0, -L20.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: 28 PTaq RNA-Seq library data processing Inline demultiplexing, mapping to the H37Rv ( NC_000962.3 ) genome, and quality control was conducted with a pipeline built on cutadapt and bowtie2 .
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Principles of cotranslational mitochondrial protein import. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.021 | PMCID: PMC12396113 | PMID: 40795856
- Version used: **2.4.5**
- Evidence: The UMI-trimmed reads were mapped to the human ribosomal RNA sequences with Bowtie2 v2.4.5 57 using the following command: bowtie2 -p 32 -t -x rRNA_index -q infile.fastq.gz -p 16 –un outfile.fastq.gz -S /dev/null > Bowtie2.report.txt Reads that did not align to ribosomal RNA sequences were mapped to human reference genome (GRCh38p13 downloaded from NCBI) with STAR 2.7.10a 58 using the following co...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.5, STAR v2.7.10a] -> stage not stated [AlphaFold, ColabFold]

### In vivo prime editing rescues alternating hemiplegia of childhood in mice. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.038 | PMCID: PMC12702498 | PMID: 40695277
- Evidence: Quantification of off-target substitutions and indels at nominated sites Reads were aligned to reference amplicon sequences generated from the off-target site genomic coordinates using Bowtie2 in local alignment mode with the flag “–very-fast-local” to permit alignment of untrimmed adapter sequences.
- Full pipeline: read trimming [Bowtie2, SAMtools] -> alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2] -> machine learning [MACS2]

### Perturb-Multimodal: A platform for pooled genetic screens with imaging and sequencing in intact mammalian tissue. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.022 | PMCID: PMC12324982 | PMID: 40513557
- Evidence: Briefly, we used bowtie2 (flags --very-sensitive --local) to align the reads to the sgRNA probe library.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose, XGBoost] -> stage not stated [AnnData, Scanpy]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 85 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ; RRID:SCR_015687 BEDtools suite 2.26.0 Quinlan and Hall 86 https://bedtools.readthedocs.io/en/latest/index.html ; RRID:SCR_006646 Bowtie2 Langmead and Salzberg 87 https://bowtie-bio.sourceforge.net/bowtie2/index.shtml ; RRID:SCR_016368 NGSplot Shen et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: QUANTIFICATION AND STATISTICAL ANALYSIS ChIP-seq analysis Peak calling: Adaptors for raw reads were trimmed using fastp with default parameters and aligned to the human reference genome hg38 with parameters “–end-to-end –very-sensitive –no-unal –no-mixed –no-discordant -I 100 -X 800” using bowtie2.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **2.3.4.3**
- Evidence: Briefly, raw sequencing reads were first aligned to the reference human transcriptome (hg19) using bowtie2 (v2.3.4.3) 98 .
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: 172 V3.2.26 BioRender BioRender.com N/A Bowtie2 Langmead and Salzberg 173 V2.5.4 BV-BRC platform UChicago V3.55.17 CFX Maestro Bio-Rad V2.3 COBRA MATLAB V2.13.3 DESeq2 Love et al.
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Version used: **2.3.4.3**
- Evidence: GAM data sequence alignment Sequenced reads from each GAM library were mapped to the mouse genome assembly GRCm38 (December 2011, mm10) with Bowtie2 (v.2.3.4.3) using default settings 56 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Version used: **2.1.0**
- Evidence: C. neptuna using Bowtie2 v.2.1.0 with the default settings 80 .
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **2.3.5.1**
- Evidence: For each sample, reads were mapped to contigs using Bowtie 2 (v.2.3.5.1) 77 with default settings (no minimum contig length).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **2.2.6**
- Evidence: FASTQ files were aligned to hg19 (NCBS build 36) using bowtie2 (v2.2.6) 32 and converted from SAM to BAM files with SAMtools (v1.2) 33 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: A. ciliaticola’ using Bowtie2 71 v.2.2.1.0 and standard parameters.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Version used: **2.4.2**
- Evidence: Processed reads were aligned against the mouse genome (mm10) by using bowtie2 2.4.2 41 with the following settings for a 50 bp sequencing run: Number of mismatches allowed in seed alignment during multi-seed alignment = 1 , length of the seed substrings to align during multi-seed alignment = 15 , set a function governing the interval between seed substrings to use during multi-seed alignment = S,1...
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Mapping, peak calling and dynamic peak calling: Fastq files were trimmed with trimGalore and cutadapt 49 , and the filtered, pair-ended reads were aligned to mm9 with bowtie2 50 .
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: The reads were trimmed by Trimmomatic 69 , then aligned to the mouse genome mm10 by Bowtie2 ( bowtie-bio.sourceforge.net/bowtie2 ) 70 .
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Identification of SARS-CoV-2 inhibitors using lung and colonic organoids. (Nature 2021)

- DOI: 10.1038/s41586-020-2901-9 | PMCID: PMC8034380 | PMID: 33116299
- Evidence: For viral RNA analysis, sequencing reads were aligned to the SARS-CoV-2/human/USA/WA-CDC-WA1/2020 genome (GenBank: MN985325.1 ) using Bowtie2 and visualized using IGV software.
- Full pipeline: quality control [R, edgeR] -> alignment/mapping [Bowtie2] -> quantification [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, edgeR] -> machine learning [UMAP] -> visualisation [Bowtie2] -> stage not stated [GSEA, Seurat v3.1.0]

### Decoupling of respiration rates and abundance in marine prokaryoplankton. (Nature 2022)

- DOI: 10.1038/s41586-022-05505-3 | PMCID: PMC9771814 | PMID: 36477536
- Evidence: To identify SSU rRNA gene transcripts, metatranscriptomic reads were mapped on the SILVA SSU library 66 (v.132) using Bowtie2 78 at 95% identity across the length of the read.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [Bowtie2] -> normalisation [SPAdes v3.0.0] -> stage not stated [Prokka]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: Reads labelled as eukaryota, root and unclassified were hereafter mapped with Bowtie2 78 against the SMAGs.
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **2.2.9**
- Evidence: 1 ), raw sequencing reads were aligned to the mouse reference genome (UCSC release mm10) using Bowtie2 (v.2.2.9) 55 using the default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **2.3.4.1**
- Evidence: Sequencing reads were mapped to TAIR10 with Bowtie 2 (v.2.3.4.1) 69 , retaining mononucleosomal fragments.
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **2.3.4.3**
- Evidence: The reads of each sequencing run and library were aligned to the GRCh38 reference genome using Bowtie2 v2.3.4.3 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Version used: **2.1.0**
- Evidence: For ATAC-seq analysis, alignments were performed with Bowtie2 (2.1.0) 52 using the hg38 genome with the pipeline at https://github.com/shenlab-sinai/chip-seq_preprocess .
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### Post-translational control of beige fat biogenesis by PRDM16 stabilization. (Nature 2022)

- DOI: 10.1038/s41586-022-05067-4 | PMCID: PMC9433319 | PMID: 35978186
- Version used: **2.1.0**
- Evidence: The reads were mapped to the latest UCSC transcript set using Bowtie2 v.2.1.0 and the gene expression level was estimated using RSEM (v.1.2.15) 41 .
- Full pipeline: read trimming [edgeR, fastp v0.20.1] -> alignment/mapping [Bowtie2 v2.1.0, RSEM v1.2.15] -> quantification [Salmon v1.4.0] -> normalisation [edgeR] -> stage not stated [Enrichr]

### Nuclear chromosome locations dictate segregation error frequencies. (Nature 2022)

- DOI: 10.1038/s41586-022-04938-0 | PMCID: PMC9300461 | PMID: 35831506
- Version used: **2.3.4**
- Evidence: Raw reads were demultiplexed by their library-specific index and sample-specific DamID barcode, universal DamID adaptor sequence was trimmed with cutadapt (v.1.16) and reads were aligned to reference genome hg19 using bowtie2 (v.2.3.4).
- Full pipeline: read trimming [Bowtie2 v2.3.4, Cutadapt v1.16] -> alignment/mapping [Bowtie2 v2.3.4, Cutadapt v1.16] -> quantification [Fiji v2.0.0, ImageJ v2.0.0]

### GTSF1 accelerates target RNA cleavage by PIWI-clade Argonaute proteins. (Nature 2022)

- DOI: 10.1038/s41586-022-05009-0 | PMCID: PMC9385479 | PMID: 35772669
- Version used: **2.5**
- Evidence: Analysis of RNA-seq data Publicly available datasets 17 , 75 – 77 were analysed. rRNA reads were removed using Bowtie 2.2.5 with default parameters 78 .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4, HTSeq v0.9.1, RAxML v1.0.0, SAMtools v1.8, STAR v2.3] -> quantification [HTSeq v0.9.1] -> visualisation [Clustal Omega v1.2.4, RAxML v1.0.0] -> stage not stated [Bowtie2 v2.5]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Trimmed reads were aligned to mm10 using Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **2.4.2**
- Evidence: The cleaned sequences were mapped to the reference genomic sequences of two OTU476 like strains (generated by ourselves as described above) and E. coli (GenBank: NC_000913.3 ) using Bowtie2 (v.2.4.2) 99 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: Alignment was performed using Bowtie2 with the fragment length set to a minimum of 0 bp and maximum of 2,000 bp and the very-sensitive option was used.
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### Genetic instability from a single S phase after whole-genome duplication. (Nature 2022)

- DOI: 10.1038/s41586-022-04578-4 | PMCID: PMC8986533 | PMID: 35355016
- Version used: **2.2.4**
- Evidence: Reads were afterwards aligned to the human reference genome (GRCh38/hg38) using Bowtie2 (version 2.2.4; ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.4] -> normalisation [RSEM] -> stage not stated [Bioconductor, GSEA, ImageJ]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Reads were demultiplexed and adaptor/quality trimmed using Ultraplex 51 , then aligned with Bowtie2 52 against a reference file containing abundant ncRNAs that are common contaminants of ribosome profiling, including rRNAs.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Altered TMPRSS2 usage by SARS-CoV-2 Omicron impacts infectivity and fusogenicity. (Nature 2022)

- DOI: 10.1038/s41586-022-04474-x | PMCID: PMC8942856 | PMID: 35104837
- Version used: **2.3.4.3**
- Evidence: The trimmed paired-end reads were aligned to the human genome hg38 using bowtie2 (v.2.3.4.3) 50 and unmapped reads were mapped to the original SARS-CoV-2 genome (strain Wuhan-Hu-1, GenBank accession no.
- Full pipeline: read trimming [Bowtie2 v2.3.4.3] -> alignment/mapping [Bowtie2 v2.3.4.3] -> dimensionality reduction/clustering [Fiji] -> visualisation [ChimeraX v1.3] -> stage not stated [GROMACS, ImageJ, Pangolin, Scanpy v1.7.1]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Evidence: The reads were aligned as two single-end reads to the TAIR10 reference genome using bowtie2 (default options), filtered for the SAM flags 0 and 16 (only reads mapped uniquely to the forward and reverse strands), and converted separately to .bam files.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Evidence: The reference genome was indexed using bowtie2-build, and reads were aligned onto the GRCh38/hg38 human reference genome using TopHat2 34 with strand-specificity and allowing only for the best match for each read.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Version used: **2.3.4.1**
- Evidence: Bulk RNA-seq data analysis RNA-seq reads were first trimmed using trimgalore v0.5.0 and reads mapping to abundant sequences included in the iGenomes Ensembl GRCh38 bundle (rDNA, mitochondrial chromosome, phiX174 genome, adapter) were removed using bowtie2 v2.3.4.1 alignment.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Version used: **2.3**
- Evidence: Specifically, the main mapping steps include (1) demultiplexing FASTQ files into single cells (cutadapt, v.2.10); (2) read-level quality control; (3) mapping (one-pass mapping for snmC, two-pass mapping for snm3C) (bismark v.0.20, bowtie2 v.2.3); (4) BAM file processing and quality control (samtools v.1.9, picard v.3.0.0); (5) methylome profile generation (ALLCools v.1.0.8); and (6) chromatin cont...
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Version used: **2.3.5.1**
- Evidence: Mapping to the GRCm38 genome was performed using bowtie2 v.2.3.5.1 and the following parameters: --local --very-sensitive-local --no-unal --no-mixed --no-discordant --phred33 -I 10 -X 700, and deduplicated with picard v.2.22.8 (ref.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Specifically, the main mapping protocol included the following steps: (1) demultiplexing FASTQ files into single cells (cutadapt 61 , v.2.10); (2) read-level QC; (3) mapping (one-pass mapping for snmC, two-pass mapping for snm3C) (bismark 62 , v.0.20; bowtie2 (ref.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **2.3.5**
- Evidence: For all of the samples, reads were then mapped to the ‘N-masked’ genome with Bowtie2 (v.2.3.5) 68 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: De novo motif analysis of FOXP3-occupied sites in vitro and in vivo FoxP PD-seq data were mapped to mm10 using Bowtie2 54 and sorted using samtools 55 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Bacterial cGAS senses a viral RNA to initiate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06743-9 | PMCID: PMC10686824 | PMID: 37968393
- Evidence: Bowtie2 via the Galaxy open-source interface 43 was used to align sequencing reads to phage and host genomes and then visualized using Geneious Prime.
- Full pipeline: alignment/mapping [Bowtie2, PyMOL, Python] -> visualisation [Bowtie2] -> stage not stated [AlphaFold, ColabFold]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: The resulting trimmed reads were subsequently mapped to the human reference genome (GRCh38.d1.vd1.fa.tar.gz) using Bowtie2 93 with the dovetail setting.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Bacteriophages suppress CRISPR-Cas immunity using RNA-based anti-CRISPRs. (Nature 2023)

- DOI: 10.1038/s41586-023-06612-5 | PMCID: PMC10651486 | PMID: 37853129
- Evidence: 56 ) Processed reads were aligned to the P. atrosepticum (genome accession number BX950851.1 ) using Bowtie 2 (ref.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2, MAFFT, SAMtools v1.16.1]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **2.5.0**
- Evidence: Tumour-infiltrating T cell ATAC–seq analysis Trimmed reads were aligned to mm10 using Bowtie2 (v.2.5.0).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Version used: **2.4.5**
- Evidence: CUT&Tag data processing and analysis Reads were trimmed using cutadapt (v.4.0) to remove Illumina adapter sequences and subsequently mapped to the reference genome with bowtie2 (v.2.4.5).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Version used: **2.4.2**
- Evidence: The trimmed reads with a length longer than or equal to 24 nt and shorter than or equal to 35 nt were kept and mapped to the rRNA and tRNA library from the Arabidopsis TAIR 10 genome using Bowtie 2 v.2.4.2 (ref.
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Evidence: To functionally annotate the predicted genes, 1 million filter-passed metagenomic reads per individual were mapped to the combined reference gene set consisting of non-redundant genes identified in this study, JPGM 52 and IGC 53 using Bowtie2 with a 95% identity cut-off.
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: ATAC–seq analysis Sequencing adapters were trimmed with BBduk with the options mink = 3, ktrim = r, before alignment to hg19 with Bowtie2 with the option -X 2000.
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Synergy and oxygen adaptation for development of next-generation probiotics. (Nature 2023)

- DOI: 10.1038/s41586-023-06378-w | PMCID: PMC10412450 | PMID: 37532933
- Version used: **2.3.5.1**
- Evidence: The dependency programs include SPAdes v3.13.0, racon v1.4.1, bowtie2 v2.3.5.1, and pilon v1.23.
- Full pipeline: alignment/mapping [Kraken2] -> quantification [Bracken] -> differential/statistical testing [R, vegan] -> stage not stated [Bowtie2 v2.3.5.1, Prokka v1.14.5, SPAdes v3.13.0]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Trimmed reads were then mapped to the respective genomes using bowtie2 100 with the default parameters.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Cooperation between bHLH transcription factors and histones for DNA access. (Nature 2023)

- DOI: 10.1038/s41586-023-06282-3 | PMCID: PMC10338342 | PMID: 37407816
- Evidence: Demultiplexed files were aligned to the D. melanogaster release 6 reference genome (BDGP6) using Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bioconductor, Bowtie2, ChimeraX, PyMOL] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.6, ImageJ, RELION, SAMtools v1.6]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Evidence: Adaptors were trimmed using CutAdapt v.2.4 and mapped to loci of interest using Bowtie2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Single-cell quantification of ribosome occupancy in early mouse development. (Nature 2023)

- DOI: 10.1038/s41586-023-06228-9 | PMCID: PMC10307641 | PMID: 37344592
- Evidence: After UMI extraction and adapter trimming, reads were aligned to ribosomal and transfer RNAs using Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ, R v4.0, Seurat]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Version used: **2.2.0**
- Evidence: The reformatted reads were then aligned to rRNA using bowtie2 (v.2.2.0) 64 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Version used: **2.3.5.1**
- Evidence: The filtered reads were mapped to the corresponding assembled scaffolds using bowtie2 (v.2.3.5.1) 56 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Evidence: Reads were trimmed to remove adapter sequences and then aligned to hg38 using Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: The trimmed reads were aligned using Bowtie2 as described 49 to the UCSC genome assembly (hg38).
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Version used: **2.4.2**
- Evidence: Trimmed reads were then mapped to the P. aeruginosa PA14 reference genome (available for download from pseudomonas.com ) using Bowtie2 v2.4.2 with default parameters for end-to-end alignment 59 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### Profiling the human intestinal environment under physiological conditions. (Nature 2023)

- DOI: 10.1038/s41586-023-05989-7 | PMCID: PMC10191855 | PMID: 37165188
- Version used: **2.4.1**
- Evidence: Preprocessing of raw sequencing reads and metagenomic assembly Skewer (v.0.2.2) 52 was used to remove Illumina adaptors, after which human reads were removed with Bowtie2 (v.2.4.1) 53 .
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DADA2, DESeq2, R, limma v3.48.3] -> stage not stated [Bowtie2 v2.4.1, HMMER, phyloseq]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **2.4.5**
- Evidence: Bowtie2 (v.2.4.5) 133 was used as a mapper for RSEM.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Evidence: Alignment Initial quality control of raw paired-end reads (100 bp) was performed using FastQC (v.0.11.8, https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) and FastQ Screen (v.0.13.0, https://www.bioinformatics.babraham.ac.uk/projects/fastq_screen/ , flags: --subset 100000; --aligner bowtie2).
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: Human sequences were then removed using the human reference GRCH38 p.9 (Bowtie2 (ref.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Evidence: Briefly, raw FASTQ reads were filtered using BBDuk (version 38.87) 43 for removal of adaptors, primer sequences and low-quality reads, and then HAdV-41 or AAV reads were identified by Bowtie2 (ref.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Version used: **2.4.1**
- Evidence: FASTQ reads were mapped to the GRCm38 (mm10) genome using Bowtie2 (v.2.4.1) using the standard settings.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: Paired-end reads were mapped to the mouse genome using bowtie2/2.2.9 with the following command: bowtie2 --local --very-sensitive-local --no-unal -x mm10 --dovetail --no-mixed --no-discordant --phred33 -I 10 -X 700.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Insulin-regulated serine and lipid metabolism drive peripheral neuropathy. (Nature 2023)

- DOI: 10.1038/s41586-022-05637-6 | PMCID: PMC9891999 | PMID: 36697822
- Version used: **2.4.2**
- Evidence: The resulting sequences were aligned using Bowtie 2 version 2.4.2 56 to the Web of Life (WoL) reference database 57 via the Web of Life Toolkit App ( https://github.com/qiyunzhu/woltka ); this step generated tables at genus, species, per genome, and per gene tables.
- Full pipeline: read trimming [fastp, minimap2 v2.17] -> alignment/mapping [Bowtie2 v2.4.2] -> quantification [ImageJ v1.53e] -> stage not stated [QIIME 2 v2020.11, Stan]

### The person-to-person transmission landscape of the gut and oral microbiomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05620-1 | PMCID: PMC9892008 | PMID: 36653448
- Version used: **2.3.4.3**
- Evidence: Contaminant and host DNA was identified with Bowtie2 (v2.3.4.3) 66 using the -sensitive-local parameter, allowing confident removal of the phiX 174 Illumina spike-in and human-associated reads (hg19 human genome release).
- Full pipeline: dimensionality reduction/clustering [phyloseq v1.28.0] -> differential/statistical testing [ggplot2 v3.3.3, ggpubr v0.4.0] -> visualisation [igraph v1.2.6] -> stage not stated [Bowtie2 v2.3.4.3, MetaPhlAn, Prokka v1.12, R, Trim Galore v0.6.6, vegan v2.5]

### Cas12a2 elicits abortive infection through RNA-triggered destruction of dsDNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05559-3 | PMCID: PMC9811890 | PMID: 36599979
- Evidence: Next, the reads were mapped to the crRNA expression site on the plus strand of pCBS273 using Bowtie2 ( http://bowtie-bio.sourceforge.net/bowtie2/ ).
- Full pipeline: read trimming [RAxML] -> alignment/mapping [Bowtie2, MAFFT v7.490, RAxML] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST, Python]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Initial processing of ATAC-seq data ATAC-seq reads were mapped to the mouse reference genome (GRCm38/mm10) using Bowtie2.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **2.2.5**
- Evidence: The clean reads were then aligned to mm10 mouse genome assembly using Bowtie2 (v.2.2.5) 90 with the settings ‘--very sensitive’.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: 58 ) and aligned to the sgRNA references with Bowtie2 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Undecaprenyl phosphate translocases confer conditional microbial fitness. (Nature 2023)

- DOI: 10.1038/s41586-022-05569-1 | PMCID: PMC9876793 | PMID: 36450355
- Version used: **2.4.1**
- Evidence: Reads were mapped to the V. cho\lerae KW3 genome (NCBI assembly GCA_001318185.1) with Bowtie2 (version 2.4.1) 60 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.3] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, ImageJ v1.53, InterProScan, featureCounts]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Evidence: The sequence data were trimmed by Trimmomatic 22 (v.0.36) to remove adaptor and then mapped to the hg38 assembly of the human genome using Bowtie2 (refs.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Version used: **2.1.0**
- Evidence: Adapter-trimmed reads were aligned to the hg19 genome using Bowtie2 (v.2.1.0).
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **2.1.0**
- Evidence: For each individual sample, paired-end 75-base-pair reads were aligned to the human reference genome (GRCh38/GENCODE release 36, RRID: SCR_014966 ) using Bowtie2 (v.2.1.0, RRID: SCR_016368 ) with default parameters and –X 2000.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Evidence: The resulting reads were aligned to the Aus0233 reference genome by Bowtie2 63 (v.2.5.1) using the --no-mixed flag and read counts were generated using htseq-count 64 (v.0.12.4) using the options -r pos -t CDS -m union --nonunique none.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### Anti-viral defence by an mRNA ADP-ribosyltransferase that blocks translation. (Nature 2024)

- DOI: 10.1038/s41586-024-08102-8 | PMCID: PMC11618068 | PMID: 39443800
- Evidence: RNA-seq and RIP-seq read mapping FASTQ files for each sample were trimmed using cutadapt 54 (version 1.15) and then mapped to the E. coli MG1655 genome (NC_00913.2), the T4 genome ( NC_000866 ), and the plasmid pKVS45-CmdTAC using bowtie2 55 (version 2.3.4.1) with the following arguments: -D 20, -I 40, -X 300, -R 3, -N 0, -L 20, -i S,1,0.50.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, NumPy, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, HMMER]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: Paired-end fastq files were aligned to hg38 reference genome using Bowtie2 with the settings ‘--very-sensitive --no-mixed --no-discordant --phred33 -I 10 -X 700’ 72 .
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors. (Nature 2024)

- DOI: 10.1038/s41586-024-07943-7 | PMCID: PMC11560846 | PMID: 39385035
- Version used: **2.4.4**
- Evidence: Paired-end alignments were constructed between mate-paired reads and library-specific databases of the expected oligonucleotide spike-in and tumour barcode insert sequences using Bowtie2 (v.2.4.4).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> normalisation [DESeq2, Harmony v0.1.1, R, Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **2.4.1**
- Evidence: DNA-seq data analysis Raw reads were trimmed with Trimmomatic (v.0.39) 54 and then mapped to mouse genome (mm10) or human genome (hg38), together with Drosophila melanogaster chromatin (spike-in chromatin), using bowtie2 (v.2.4.1) 55 using the default mode, where multiple alignments are searched and the best one is reported.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: The quality-controlled reads were mapped to the concatenated or Kp-2H7 reference genome using bowtie2 66 version 2.3.4.1.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: The pipeline performed adapter trimming with Trim Galore (10.5281/zenodo.5127898) and reference-genome alignment with Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Evidence: Reads were filtered using pre-alignment to a maize structural RNA consensus database using bowtie2 (ref.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Version used: **2.3.4.1**
- Evidence: Pre-processing of RNA-seq data, including removal of low-quality reads and rRNA reads, was performed using Bowtie2 (v.2.3.4.1) 94 and SOAPnuke.
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### A virally encoded tRNA neutralizes the PARIS antiviral defence system. (Nature 2024)

- DOI: 10.1038/s41586-024-07874-3 | PMCID: PMC11464382 | PMID: 39111359
- Version used: **2.4.4**
- Evidence: Reads were aligned with bowtie2 v.2.4.4, and Hi-C contact maps were generated using hicstuff v.3.0.3 ( https://github.com/koszullab/hicstuff ) with default parameters and using the HpaII enzyme for digestion.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HMMER v3.3.2, MUSCLE v5.1] -> structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.7, SPAdes]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: The sequences were aligned to the sgRNA library using Bowtie2 58 , 59 . sgRNAs were counted using the MAGeCK count function (--norm-method total) 60 , 61 . sgRNA enrichment was calculated using the MAGeCK paired test function.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: Bowtie2 was then used for pre-alignments to remove reads that would map to chrM (revised Cambridge Reference Sequence), alpha satellite repeats, Alu repeats, ribosomal DNA repeats and other repeat regions with “-k 1 -D 20 -R 3 -N 1 -L 20 -i S,1,0.50 -X 2000 --rg-id” options.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Version used: **2.3.2**
- Evidence: Plague phylogenetic analysis For all samples in which Y. pestis was detected in the pathogen screening, we mapped trimmed reads from all libraries of that sample to the reference plague genome (CO92; GCA_000009065.1 ) using bowtie2 (v.2.3.2) with the following parameters: -D 20 -R 3 -N 1 -L 20 -i S,1,0.50 --end-to-end --no-unal.
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Transposase-assisted target-site integration for efficient plant genome engineering. (Nature 2024)

- DOI: 10.1038/s41586-024-07613-8 | PMCID: PMC11254759 | PMID: 38926583
- Evidence: To remove reads that show mPing at its donor location, these 5′ and 3′ trimmed sequences were mapped to the reference mPing donor sequence using the default parameters of bowtie2 67 with the additional parameter to store donor-unmapped reads (--un).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [R, ggplot2]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **2.4.5**
- Evidence: Sequencing reads were mapped using Bowtie2 (v2.4.5) to the C3H_HeJ_v1 reference genome.
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: In brief, paired-end reads were trimmed using Trim Galore and aligned to the human genome (GRCh37/hg19) using Bowtie2.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Widespread horse-based mobility arose around 2200 BCE in Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-024-07597-5 | PMCID: PMC11269178 | PMID: 38843826
- Evidence: The resulting collapsed and uncollapsed read pairs were processed through the Paleomix bam_pipeline (v.1.2.13.2) 53 for Bowtie2 (ref.
- Full pipeline: stage not stated [ANGSD v0.917, Bowtie2]

### Nuclear position and local acetyl-CoA production regulate chromatin state. (Nature 2024)

- DOI: 10.1038/s41586-024-07471-4 | PMCID: PMC11168921 | PMID: 38839952
- Version used: **2.4.2**
- Evidence: (v.0.6.3) ( https://github.com/FelixKrueger/TrimGalore ) before aligning read sequences to the Drosophila genome (dm6) by Bowtie2 (v.2.4.2) 30 , 31 .
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [MACS2]

### Single-cell nascent RNA sequencing unveils coordinated global transcription. (Nature 2024)

- DOI: 10.1038/s41586-024-07517-7 | PMCID: PMC11222150 | PMID: 38839954
- Evidence: The adapter-clipped and demultiplexed reads were first mapped to the mouse ribosomal genome using bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Cutadapt] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Seurat]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **2.3.4.1**
- Evidence: (v.0.6.3) and mapped on the GRCh38.p12 genome using Bismark (v.0.22.1) 81 and Bowtie2 (v.2.3.4.1) with the “-X 2000” option.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: ...rRNA sequences; prodigal 78 v.2.6.3 for gene prediction; HMMER v.3.1b2 ( http://hmmer.org/ ) for HMM homology searches against the Pfam database 79 ; Bowtie2 (ref.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **2.4.2**
- Evidence: Raw ATAC–seq reads were trimmed using NGmerge v.0.2_dev and mapped to the Hi-C P. breviceps assembly using Bowtie2 (v.2.4.2) 54 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: Bowtie2 was then used to align the reads to the hg38 genome.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Version used: **2.3.3**
- Evidence: Alignment of reads to either the reference human (hg38) or mouse (mm10) genome was performed using Bowtie2 (v2.3.3).
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **2.5.0**
- Evidence: The trimmed reads were then aligned to the appropriate reference sequences (pegRNAs or epegRNAs) using Bowtie2 (2.5.0) 52 with default alignment options.
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Evidence: Mapping was performed to the zebrafish reference genome build GRCz11, with TopHat v.2.1.1 and Bowtie1 or Bowtie2 option.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### Single-cell multiplex chromatin and RNA interactions in ageing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07239-w | PMCID: PMC11023937 | PMID: 38538789
- Version used: **5.4.0**
- Evidence: DNA and RNA inserts are mapped to the genome using bowtie2 (v.5.4.0) 59 with the parameters ‘bowtie2 -p 10 -t --phred33 -x’, and bwa (v.0.7.17) 60 mem with parameters ‘-SP5M’, respectively.
- Full pipeline: alignment/mapping [Bowtie2 v5.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Docker, Harmony v0.1.1, R, Seurat v4.3.0, Snakemake]

### A distinct Fusobacterium nucleatum clade dominates the colorectal cancer niche. (Nature 2024)

- DOI: 10.1038/s41586-024-07182-w | PMCID: PMC11006615 | PMID: 38509359
- Version used: **2.4.5**
- Evidence: Metagenomic samples were mapped against the Fna SB010 eut , pdu and gdar operons using Bowtie2 (version 2.4.5, --sensitive parameter) 77 .
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v2.4.5] -> machine learning [DADA2] -> stage not stated [BLAST, Flye]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: ATAC-seq analysis Bowtie2 with default parameters was used to map ATAC-seq.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **2.2.4**
- Evidence: Trimmed reads were aligned to the hg38 reference genome with Bowtie2 (v2.2.4) 101 using the default parameters.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **2.2.9**
- Evidence: Reads were aligned using bowtie2 v2.2.9 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Version used: **2.5.1**
- Evidence: The inferred full-length reads were generated by Bedtools (v2.31.0) and Samtools (v1.17) after mapping to the reference genome ( NC_000913.3 for Eco, NC_008596.1 for Msm and NC_018143.2 for Mtb) with Bowtie 2 (v2.5.1).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Version used: **2.2.5**
- Evidence: Reads were aligned to the boundary sequence around the putative cutting site (400 bp centred on the sgRNA complementary site for Cas9-treated samples or 300 bp centred on the ZFP-8 recognition site for EvoETR-8-treated samples) using bowtie2 v.2.2.5 (refs.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Version used: **2.4.5**
- Evidence: In brief, sequencing reads were trimmed using fastx-toolkit (v0.0.14), aligned using Bowtie2 (v2.4.5) and quantified using featureCounts (v2.0.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **2.4.1**
- Evidence: High-quality reads were mapped to the human genome (build GRCh38/hg38) using Bowtie2 (v.2.4.1) 56 .
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Version used: **2.3.5**
- Evidence: Reads were aligned first to abundant RNAs such as transfer RNA, small nuclear RNA, small nucleolar RNA and ribonuclear RNA, then to the genome with bowtie2 v.2.3.5: bowtie2 --no-unal --un-gz -L 16 --very-sensitive-local -x bt2_index -U fastq_in.fastq.gz -o bam_out.bam.
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Version used: **2.2.5**
- Evidence: Filtered reads were aligned with the reference genome using bowtie2 (v.2.2.5) (ref.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Reads were aligned to human assembly hg19 with version 2.3.4.1 of bowtie2 ( http://bowtie-bio.sourceforge.net/bowtie2/index.shtml ) and MarkDuplicates of Picard Tools version 2.16.0 was used for deduplication.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Adding α,α-disubstituted and β-linked monomers to the genetic code of an organism. (Nature 2024)

- DOI: 10.1038/s41586-023-06897-6 | PMCID: PMC10794150 | PMID: 38200312
- Evidence: Paired end reads were first paired using PEAR 58 , and aligned to a reference sequence of Mm PylRS using Bowtie2 59 .
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [PyMOL]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Version used: **2.3.4.3**
- Evidence: QC of metagenomic sequencing data We removed host-genome-contaminated reads and low-quality reads from the raw metagenomic sequencing data using KneadData (v.0.7.4), Bowtie2 (v.2.3.4.3) 57 and Trimmomatic (v.0.39) 58 .
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Emergence of replication timing during early mammalian development. (Nature 2024)

- DOI: 10.1038/s41586-023-06872-1 | PMCID: PMC10781638 | PMID: 38123678
- Version used: **2.3.5**
- Evidence: Sequencing reads were aligned to the mm10 genome using bowtie2 (v.2.3.5) 58 with the ‘--local’ option.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.3.5] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [BEDTools, ImageJ v1.53k, R v4.0.0, SAMtools v1.9]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: ATAC-seq data processing Adaptor sequences were removed from raw sequencing data with CutAdapt, and reads were aligned to the mouse genome (mm10) using Bowtie2.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: The remaining reads were mapped to the human genome (UCSC hg19) using bowtie2 32 (v.2.3.4.1) and were subsequently filtered to remove Homo sapiens sequences.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Prime editing-installed suppressor tRNAs for disease-agnostic genome editing. (Nature 2025)

- DOI: 10.1038/s41586-025-09732-2 | PMCID: PMC12675287 | PMID: 41261131
- Evidence: For analysis, sequencing reads were initially demultiplexed into individual fastq files by first aligning each read to a corresponding member of the epegRNA library using bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, DESeq2, STAR, Trim Galore] -> alignment/mapping [Bioconductor, Bowtie2, DESeq2, STAR, Trim Galore] -> differential/statistical testing [DESeq2, STAR, Trim Galore]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **2.2.8**
- Evidence: Reads were trimmed for adaptor sequences using Trim Galore (v.0.6.6) 87 and aligned to the mouse reference genome (GRCm38; GENCODE M25) using Bowtie 2 (v.2.2.8) with a maximum fragment length of 2,000 bp (−X 2000) with default sensitivity settings 88 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: Read coverage for each library were obtained on their corresponding genome using Bowtie2 (ref.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: CUT&RUN analysis Standard Illumina adapters were cut from the Illumina reads using Cutadapt 72 and then aligned to a combined hg38 and E. coli genome version using Bowtie2 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Version used: **2.5.3**
- Evidence: The trimmed reads of each sample were then aligned to the corresponding generated de novo assemblies using bowtie2 (v.2.5.3) 66 .
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### Reprogramming neuroblastoma by diet-enhanced polyamine depletion. (Nature 2025)

- DOI: 10.1038/s41586-025-09564-0 | PMCID: PMC12527938 | PMID: 40993392
- Evidence: Reads were then mapped to the canonical transcriptome with bowtie2 using default parameters.
- Full pipeline: alignment/mapping [Bowtie2, Cutadapt, HISAT2, RepeatMasker] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R, ggplot2, ggpubr, limma] -> visualisation [Cytoscape v2.9.0, GSEA, R] -> stage not stated [fgsea]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **2.4.5**
- Evidence: Filtered reads were mapped on mm39 for mouse samples and danRer11 in which alternative contigs were removed for fish samples using Bowtie 2 v.2.4.5 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: The FASTQ files were individually mapped against the human genome reference file including decoy sequences (GRCh38p7.13/hg38, 1000 Genome Project) using bowtie2 (-x 2000, -mm --qc-filter --met 1 --sensitive --no-mixed -t) and subsequently merged and sorted as BAM-formatted files using samtools v.1.14, with only uniquely high-quality mapped reads (MAPQ > 30, SAM flags 0×1, 0×2) retained.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Version used: **2.4.1**
- Evidence: The preprocessed spacer sequences were aligned using Bowtie 2 (v.2.4.1) 60 with the ‘very-sensitive’ preset to the combined alignment reference containing the N. meningitidis 8013 genome sequence (RefSeq accession no.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Reads were aligned to the human genome assembly hg38 using Bowtie 2 (ref.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **2.2.9**
- Evidence: CUT&RUN data processing CUT&RUN reads were mapped to mm10 mouse genome assembly using Bowtie2 (v.2.2.9) with settings --local --very-sensitive-local –no-unal –no-mixed –no-discordant –phred33 -I 10 -X 700.
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **2.4.2**
- Evidence: ATAC–seq reads were aligned to the genome using bowtie2 (v.2.4.2) 94 with the parameters –very-sensitive and -k 10.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Excised DNA circles from V(D)J recombination promote relapsed leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-09372-6 | PMCID: PMC12443594 | PMID: 40770098
- Evidence: In brief, paired-end sequencing data was aligned to the hg19 build of the human genome using Bowtie2 in local alignment mode.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [Python]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: 76 ) (GenBank accession numbers are provided in Supplementary Note 3 ) using bowtie2 (ref.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Version used: **2.5.1**
- Evidence: Trimmed reads were consecutively mapped to the index libraries of species-specific (chicken or mouse) contaminating RNAs obtained from RNAcentral 73 (rRNAs, mitochondrial RNAs and transfer RNAs) using Bowtie 2 v.2.5.1 (ref.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### The spatiotemporal distribution of human pathogens in ancient Eurasia. (Nature 2025)

- DOI: 10.1038/s41586-025-09192-8 | PMCID: PMC12286840 | PMID: 40634616
- Evidence: Read mapping against the selected assembly was carried out using bowtie2 (ref.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [BLAST] -> stage not stated [R]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Version used: **2.3.5.1**
- Evidence: Alignment to the reference rRNA sequence (18S: NR_003286.4 ; 5.8S: NR_003285.2 ; 28S: NR_003287.4 ) was done using Bowtie2 (v.2.3.5.1) with the default parameters.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### Nerve-to-cancer transfer of mitochondria during cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09176-8 | PMCID: PMC12328229 | PMID: 40562940
- Evidence: Quality-trimmed reads were aligned to the Mus musculus mm39 genome using Bowtie2, in paired-end mode with a 500-bp fragment length.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Python, SAMtools] -> quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Python] -> stage not stated [GSEA]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: Sequenced reads were mapped against hg38 using Bowtie2 (ref.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: This toolkit implements Bowtie 2 63 to initially find reads mapped to a plant chloroplast database and SPAdes 64 for de novo assembly and iterative extension.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Evidence: After confirming the sequence quality of the trimmed reads, they were mapped onto the reference genome sequence of the P. falciparum 3D7 strain, which was downloaded from PlasmoDB 62 using the bowtie2 tool 40 .
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: Reads were aligned to the GRCm38 mm10 reference genome using bowtie2 (ref.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: Reads were mapped to the T5 ( NC_005859.1 ) genome or Bas37 genome ( MZ501089.1 ), using Bowtie2 64 (v2.2.1) with default parameters.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Native nucleosomes intrinsically encode genome organization principles. (Nature 2025)

- DOI: 10.1038/s41586-025-08971-7 | PMCID: PMC12240700 | PMID: 40335690
- Evidence: Computation of genome-wide nucleosome condensability First, we obtained coverage profiles along the genome for input control and for the supernatant sample of each titration after the alignment of pair-end reads on the hg38 human genome assembly using Bowtie2 software 52 .
- Full pipeline: alignment/mapping [Bowtie2, Python] -> simulation/modelling [OpenMM] -> stage not stated [GSEA, Jupyter, scikit-learn]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: The assembled scaffolds were used to recruit reads from their own metagenomes and other metagenomes from the same geographical location using Bowtie2 (ref.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Geographic and age variations in mutational processes in colorectal cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09025-8 | PMCID: PMC12221974 | PMID: 40267983
- Evidence: Microbiome analysis To identify microbial reads that map to the pks island ( pks ), non-human reads were aligned to the IHE3034 genome (RefSeq assembly: GCF_000025745.1) using Bowtie2 74 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, fastp] -> variant calling [ANNOVAR] -> quantification [R] -> visualisation [R]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **2.4.5**
- Evidence: Trimmed reads were then combined and aligned using bowtie2 2.4.5 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **2.4.4**
- Evidence: Reads were then mapped against mm10 with Bowtie2 (2.4.4), and duplicate reads were removed with samtools (1.15.1) rmdup, and bam files were converted to bed files with bedtools (2.30.0) bamtobed.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Histone H1 deamidation facilitates chromatin relaxation for DNA repair. (Nature 2025)

- DOI: 10.1038/s41586-025-08835-0 | PMCID: PMC12074999 | PMID: 40240600
- Version used: **2.5.4**
- Evidence: Bowtie2 (v2.5.4) was applied for alignment to the hg38 human genome reference, using the parameters ‘–very-sensitive–no-mixed–no-discordant’.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.4, SAMtools] -> stage not stated [AlphaFold, ImageJ, Picard, PyMOL, deepTools v3.5.5]

### PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens. (Nature 2025)

- DOI: 10.1038/s41586-025-08982-4 | PMCID: PMC12176658 | PMID: 40228524
- Version used: **2.2.3**
- Evidence: Sequences were mapped to the mouse genome (mm10) with bowtie2 (2.2.3), filtered based on mapping score (MAPQ > 30, Samtools (0.1.19)), and duplicates were removed (Picard).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.3, Picard, SAMtools v0.1.19] -> normalisation [Seurat v5.1] -> dimensionality reduction/clustering [Seurat v5.1, UMAP] -> stage not stated [Signac v1.14]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Version used: **2.4.4**
- Evidence: ChIP–seq analysis Raw paired-end FASTQ files were aligned to the GRCh38 reference genome using Bowtie 2 v.2.4.4.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **2.5.0**
- Evidence: Counts per bin were then calculated on the basis of SAM files output from bowtie2 v.2.5.0.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **2.2.9**
- Evidence: Raw TACIT sequencing data were evaluated using FastQC (v.0.11.5), followed by mapping to the mouse reference genome mm10 by Bowtie2 (v.2.2.9) 55 .
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Reconstitution of SPO11-dependent double-strand break formation. (Nature 2025)

- DOI: 10.1038/s41586-025-08601-2 | PMCID: PMC11922745 | PMID: 39972129
- Version used: **2.5.3**
- Evidence: In brief, reads were mapped using bowtie2 (version 2.5.3) 56 with parameters -N 1 -X 1000.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.3, ChimeraX v1.8] -> quantification [ImageJ v1.54g] -> stage not stated [AlphaFold]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Pathway abundance was estimated by aligning metagenomic reads to binned sequences with bowtie2 (ref.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **2.5.0**
- Evidence: The samples were aligned to the hg19 or mm10 genome using bowtie2 (v.2.5.0) 66 , with the following parameters: --local --very-sensitive-local --phred33 -I 10 -X 700 --dovetail --no-unal --no-mixed --no-discordant 63 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **2.5.3**
- Evidence: Briefly, TEd-seq fastq files were mapped to the 5′ terminal sequence of TE (1–144 bp of Evade or 1–105 bp of Tal1 shown in the file of ‘target_TE_sequence_extremity.fa’) using Bowtie2 (v.2.5.3) 51 with the parameter ‘--local --very-sensitive’.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Engineered extrachromosomal oncogene amplifications promote tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08318-8 | PMCID: PMC11754114 | PMID: 39695225
- Evidence: Fastq files from ATAC-seq and WGS were aligned to the mouse genome (mm10) using Bowtie2.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, R, STAR] -> quantification [MACS2 v3.0.0b, deepTools v3.5.3] -> differential/statistical testing [DESeq2, R, STAR] -> stage not stated [CNVkit v0.9.10, fgsea]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: ChIP–seq, ATAC–seq and MNase–seq samples were aligned to mouse reference genome MGSCv37 (mm9) using Bowtie2 67 v.2.3.4.1, using a --very-sensitive call and paired-end settings (or single-end settings where appropriate).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Evidence: Sequence data were aligned to an HLA reference file using Bowtie2 (ref.
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Version used: **2.2.5**
- Evidence: Bowtie2 (v2.2.5) 68 was used to align the trimmed fastqs to GRCh38 using settings --local --very-sensitive --no-mixed --no-discordant --phred33 --dovetail -I 10 -X 700 -p 8 -q and E. coli (EMBL accession U00096.2 ) with settings --local --very-sensitive --no-overlap --no-dovetail --no-mixed --no-discordant --phred33 -I 10 -X 700 -p 8 -q.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **2.3.5.1**
- Evidence: Cut&Tag data processing Cut&Tag reads were aligned to the mm10 genome with Bowtie2 (v2.3.5.1) using the following parameters: --end-to-end --very-sensitive --no-mixed --no-discordant --phred33 -I 10 -X 700.
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Version used: **2.3.4.1**
- Evidence: Reads mapping to abundant sequences included in the iGenomes UCSC GRCm38 reference (mouse rDNA, mouse mitochondrial chromosome, phiX174 genome, adapter) were removed using bowtie2 v.2.3.4.1 alignment.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Evidence: To quantify MAG relative abundance across samples, trimmed metagenomic reads were mapped to the dereplicated MAG set using Bowtie2 84 and output as SAM files, which were then converted to sorted BAM files using samtools.
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **2.5.1**
- Evidence: Genomic analysis END-seq, ATAC–seq and ChIP–seq reads were mapped to the mouse (GRCm38p2/mm10) genomes using Bowtie2 (v.2.5.1-1) 66 using the default parameters.
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Evidence: For each genus identified in each sample, pairwise alignments using bowtie2 89 (v.2.5.4) were made for all reads classified to that genus against all available species reference genomes for the same genus.
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **2.5.0**
- Evidence: Data analysis Raw fastq files were aligned to the hg19 or mm10 genome using bowtie2 (v2.5.0) 97 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **2.2.9**
- Evidence: Sequencing reads were aligned to hg38 with Bowtie2 (v.2.2.9) 68 .
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **2.3**
- Evidence: CATCH-seq data analysis For CATCH-seq, all sequencing reads after trimming by fastp were aligned to the mouse (mm10) using Bowtie 2 v.2.3 (ref.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Bowtie2 (ref.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Dynamics of genetic and somatic trade-offs in ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10407-9 | PMCID: PMC13253337 | PMID: 42020758
- Version used: **2.3.4.1**
- Evidence: FASTQ files were aligned to M. musculus GRCm38.p6/mm10 reference using Bowtie 2 (v2.3.4.1) 81 .
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.3.4.1] -> variant calling [BCFtools, R v4.0] -> dimensionality reduction/clustering [PLINK, TwoSampleMR v0.6.2, clusterProfiler] -> stage not stated [SAMtools v1.6]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Evidence: Reads were aligned to the hg38 reference genome using Bowtie 2.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **2.5.0**
- Evidence: ...hree rounds of 8 bp barcodes that make up a single-cell barcode, followed by Nextera adapter trimming with fastp (v0.23.2) 93 , genome alignment with Bowtie2 (v2.5.0) 94 , and conversion of the output BAM file to a more storage-efficient fragment file.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Version used: **2.4.1**
- Evidence: Trim-Galore tool (v.0.6.5) 78 was used for adaptor trimming and alignment to the mouse mm10 genome assembly was performed with Bowtie2 (v.2.4.1) 79 .
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **2.3.4.1**
- Evidence: The paired-end reads from ATAC-seq were trimmed using BBDuk (v.37.9) and mapped to reference genome mm10 using Bowtie2 (v.2.3.4.1).
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Evidence: FASTA files were mapped to the mouse genome (NCBI37/mm10) using TopHat v.1.0.13 ( http://tophat.cbcb.umd.edu/ ) and Bowtie 2 ( http://bowtie-bio.sourceforge.net/bowtie2/index.shtml ) 62 .
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Evidence: Cleaned reads were next aligned to reference genome mm10 using Bowtie2.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Version used: **2.4.1**
- Evidence: Reads were aligned to the mm10 reference genome using Bowtie2 (v2.4.1) 54 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **2.2.9**
- Evidence: After removing adapters and low-quality bases by cutadapt (v.1.11), paired-end cf-EpiTracing reads were mapped to the human reference genome hg19 and Drosophila reference genome dm3 using Bowtie2 (v.2.2.9) 77 .
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### DICER cleavage fidelity is governed by 5'-end binding pockets. (Nature 2026)

- DOI: 10.1038/s41586-026-10211-5 | PMCID: PMC13171623 | PMID: 41781616
- Evidence: The resulting reads were mapped to a customized reference containing pri-miRNA sequences using Bowtie2 53 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, Bowtie2, Coot v0.9.8.96] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.7, Coot v0.9.8.96, PHENIX v1.20.1] -> stage not stated [PyMOL]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Version used: **2.3.4.3**
- Evidence: CRISPR screen data analysis Sequence reads were aligned to the sgRNA reference library using Bowtie 2 v.2.3.4.3 software.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **2.2.9**
- Evidence: Read-pairs were mapped independently using Bowtie2 (v.2.2.9: –very-sensitive, –rdg 500, 3; –rfg 500, 3) 73 on the corresponding MboI-indexed reference sequence.
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Version used: **2.3.4.1**
- Evidence: FASTQ files for each sample were trimmed using cutadapt (v1.15) 50 and then mapped to the MG1655 genome (NC_00913.2) and the T7 genome ( V01146 ), or the consensus map of rRNA loci as previously described 30 using bowtie2 (v2.3.4.1) 51 with the following arguments: –D 20, –I 40, –X 300, –R 3, –N 0, –L 20, –i S,1,0.50.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### Cleavage of mRNAs by a minority of pachytene piRNAs improves sperm fitness. (Nature 2026)

- DOI: 10.1038/s41586-026-10102-9 | PMCID: PMC13061629 | PMID: 41639461
- Version used: **2.2.0**
- Evidence: The reformatted reads were then aligned to rRNA using bowtie2 (v.2.2.0) 62 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.18.1]

### Single-molecule dynamics of the TRiC chaperonin system in vivo. (Nature 2026)

- DOI: 10.1038/s41586-025-10073-3 | PMCID: PMC13061604 | PMID: 41639457
- Version used: **2.4.2**
- Evidence: The remaining reads were mapped against a non-coding RNA library, including rRNA using Bowtie2 (v.2.4.2) with the parameters ‘-N 1 -L 15’.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10a] -> visualisation [AlphaFold] -> stage not stated [TrackMate]

### Regulatory grammar in human promoters uncovered by MPRA-based deep learning. (Nature 2026)

- DOI: 10.1038/s41586-025-10093-z | PMCID: PMC13017510 | PMID: 41639451
- Version used: **2.5.1**
- Evidence: Subsequently, we used Bowtie2 (v.2.5.1) with default settings to align the reads against human rDNA ( U13369.1 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1] -> stage not stated [NumPy, PyTorch v2.1.1]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Evidence: A bowtie2 index was then built from these merged genomes.
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Version used: **2.5.1**
- Evidence: Next, each synthetic read was aligned using bowtie2 v.2.5.1 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **2.4**
- Evidence: Reads with poor quality (lower than 20) were filtered using cutadapt (v.2.6) and aligned to the mouse reference genome (GRCm39) using bowtie2 (v.2.4), and duplicated reads were marked and removed by Picard tools (v.3.4).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### GlycoRNA complexed with heparan sulfate regulates VEGF-A signalling. (Nature 2026)

- DOI: 10.1038/s41586-025-10052-8 | PMCID: PMC12999495 | PMID: 41606331
- Version used: **2.5.4**
- Evidence: Reads were aligned to a custom reference of human small non-coding RNAs 84 ( https://github.com/y9c/m6A-SACseq/tree/main/db ) using Bowtie2 (v2.5.4) 85 with -k 10 to retain up to 10 alignments per read.
- Full pipeline: read trimming [Cutadapt v4.9, DESeq2 v1.42.1] -> alignment/mapping [Bowtie2 v2.5.4] -> differential/statistical testing [DESeq2 v1.42.1] -> stage not stated [ImageJ, Python, SciPy]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **2.3.4.3**
- Evidence: Contaminant and host DNA was identified with Bowtie2 (v2.3.4.3) 67 using the -sensitive-local parameter, allowing confident removal of the phiX 174 Illumina spike-in and human-associated reads (hg19/GRCh37 human genome release).
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: Paired-end sequencing data were mapped to a reference WT LetA sequence using the bowtie2 (ref.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: All the resulting reads and those remaining paired were mapped against the hs37d5 reference genome using Bowtie 2 (ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Version used: **2.3.4.3**
- Evidence: GAM data sequence alignment Sequenced reads from each GAM library were mapped to the human genome assembly GRCh38 (December 2013, hg38) with bowtie2 (v.2.3.4.3) using the default settings.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Version used: **2.3.4.1**
- Evidence: Specifically, we trimmed the adapter sequence with TrimGalore (v0.5.0) 72 , aligned to the hg19 reference with Bowtie2 (v2.3.4.1) 73 , filtered duplicates with MACS3 (v3.0.3) 74 and called narrow peaks with the MACS3 (v3.0.3) hmmratac command.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **2.5.1**
- Evidence: Read pairs were first aligned to a combined reference that contained repetitive and structural RNA sequences (ribosomal RNAs, snRNAs, snoRNAs, 45S pre-rRNAs and tRNAs) using Bowtie2 (v.2.5.1).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Version used: **2.4.2**
- Evidence: Reads mapping to ribosomal RNA and globin were removed using Bowtie2 (v.2.4.2) 63 , resulting in 25 million reads per sample for further analyses.
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **2.4.5**
- Evidence: The resulting reads were trimmed using fastx-toolkit (v.0.0.14) and subsequently aligned (Bowtie2, v.2.4.5) and quantified (featureCounts, v.2.0.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **2.5.4**
- Evidence: To determine the short-read coverage of integrated phages, we mapped the short reads to the long-read assembly using Bowtie 2 (v.2.5.4) and calculated the per-base coverage using SAMtools (v.1.21).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Version used: **2.3.5.1**
- Evidence: Reads were aligned to the filtered protein-coding transcriptome with Bowtie2 (v2.3.5.1) 71 , using the parameters recommended for use with RSEM: --sensitive --dpad 0 --gbar 99999999 --mp 1,1 --np 1 --score-min L,0,-0.1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### SARS-CoV-2 expresses a microRNA-like small RNA able to selectively repress host genes. (PNAS 2021)

- DOI: 10.1073/pnas.2116668118 | PMCID: PMC8719879 | PMID: 34903581
- Evidence: The reads were mapped with bowtie2 ( 66 ) (–very-sensitive-local) to an index containing human and SARS-CoV-2 genomes. miRNAs were counted by using featureCounts ( 67 ) and annotations obtained from miRBase ( 68 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, featureCounts] -> differential/statistical testing [edgeR] -> visualisation [BEDTools]

### Genome evolution in an agricultural pest following adoption of transgenic crops. (PNAS 2021)

- DOI: 10.1073/pnas.2020853118 | PMCID: PMC8719884 | PMID: 34930832
- Evidence: 1.0, NCBI Bioproject PRJNA378438 ( 36 )] with Bowtie2 ( 94 ).
- Full pipeline: alignment/mapping [GEMMA v0.98.4, R] -> variant calling [BCFtools] -> differential/statistical testing [GEMMA v0.98.4] -> stage not stated [Bowtie2]

### Quantitative assessment reveals the dominance of duplicated sequences in germline-derived extrachromosomal circular DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2102842118 | PMCID: PMC8617514 | PMID: 34789574
- Version used: **2.3.5**
- Evidence: The sequencing reads were trimmed using Trim Galore (v.0.6.1) and Cut Adapt (v2.3) to remove adapters and subsequently aligned to the University of Santa Cruz (UCSC) hg38 human reference genome or mm10 mouse reference genome using Bowtie 2 (v2.3.5).
- Full pipeline: read trimming [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> alignment/mapping [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> stage not stated [RepeatMasker, SAMtools]

### Phytoplankton exudates and lysates support distinct microbial consortia with specialized metabolic and ecophysiological traits. (PNAS 2021)

- DOI: 10.1073/pnas.2101178118 | PMCID: PMC8521717 | PMID: 34620710
- Evidence: CDS read depth was measured by pairwise alignment of shotgun reads to the assembly of all samples using the “Bowtie2” program ( 80 ).
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [R v3.4.0, ggplot2] -> stage not stated [SciPy]

### The translatome of neuronal cell bodies, dendrites, and axons. (PNAS 2021)

- DOI: 10.1073/pnas.2113929118 | PMCID: PMC8639352 | PMID: 34670838
- Version used: **2.3.5.1**
- Evidence: To remove reads originating from noncoding RNA (ncRNA, i.e., rRNA), trimmed reads were aligned to rat ncRNA using Bowtie2 version 2.3.5.1 (–very-sensitive) ( 64 ) and aligned reads were discarded.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt] -> alignment/mapping [Bowtie2 v2.3.5.1, STAR v2.7.3, featureCounts v2.0.0] -> stage not stated [DESeq2 v1.30.1, Python]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Evidence: Sequencing reads were mapped to the mouse reference genome (mm10) from the University of California, Santa Cruz (UCSC) Genome Browser using Bowtie2.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **2.3.4.1**
- Evidence: Reads used to assemble genomes were mapped back to single-copy genes and duplicated genes identified by BUSCO (see above), and additionally to the phased regions and to scaffolds from which the phased regions were derived (but that were masked in the phased regions), using bowtie2 v2.3.4.1 with standard parameters ( 98 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Version used: **2.3.5.1**
- Evidence: Clean reads were then aligned to the Arabidopsis TAIR10 release 43 reference genome using Bowtie2 v2.3.5.1 ( 73 ) with options -k 10 –very-sensitive.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Version used: **2.3.3.1**
- Evidence: Bowtie2 (v2.3.3.1) (–very-sensitive) was used to map ChIP-seq reads to the mouse reference genome GRCm38.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Dynamic chromatin regulatory landscape of human CAR T cell exhaustion. (PNAS 2021)

- DOI: 10.1073/pnas.2104758118 | PMCID: PMC8325267 | PMID: 34285077
- Evidence: Adapter sequences were trimmed from the reads and sequences aligned to the hg19 genome with bowtie2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [BEDTools, DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2, Picard, R]

### Sequence of the supernumerary B chromosome of maize provides insight into its drive mechanism and evolution. (PNAS 2021)

- DOI: 10.1073/pnas.2104254118 | PMCID: PMC8201846 | PMID: 34088847
- Evidence: Roughly, 6× coverage trimmed reads were aligned to the maize W22 reference genome (Zm-W22-REFERENCE-NRGENE-2.0) ( 25 ) or B73 reference genome plus mitochondria and chloroplast genomes ( 24 ) using Bowtie2 ( 70 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [BEDTools v2.25.0, Bowtie2, MUSCLE v3.8.1551] -> visualisation [R, ggplot2] -> stage not stated [AUGUSTUS v2.5.5, InterProScan v5.36, RepeatMasker v4.0.7]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: Bowtie2 ( 100 ) was used to align reads to the database, and samtools ( 101 ) idxstats was used to calculate read coverage and RPKM for each contig.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### Prespacers formed during primed adaptation associate with the Cas1-Cas2 adaptation complex and the Cas3 interference nuclease-helicase. (PNAS 2021)

- DOI: 10.1073/pnas.2021291118 | PMCID: PMC8179228 | PMID: 34035168
- Evidence: Reads were mapped separately to the KD263 genome or plasmid genomes by Bowtie 2 ( 66 ) in a local alignment mode, with minimum and maximum fragment lengths set to 20 and 1,500, respectively.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2]

### Epigenetic inheritance of DNA methylation changes in fish living in hydrogen sulfide-rich springs. (PNAS 2021)

- DOI: 10.1073/pnas.2014929118 | PMCID: PMC8255783 | PMID: 34185679
- Evidence: The reads for each MeDIP sample were mapped to the P. mexciana ( 48 ) genome using Bowtie2 ( 69 ) with default parameter options.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [R, edgeR]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: Reads assigned to the host genome (Ensemble Sus scrofa genome; Sscrofa11.1) and the genomes of two dominant ingredients of the pig diets, corn (Ensemble Zea mays genome; B73_RefGen_v4) and soybean (Ensemble Glycine max genome; Glycine max v2.1), were removed using Bowtie2 ( 54 ) yielding 3.53 × 10 7 ± 1.02 × 10 7 (mean ± SD) reads per sample ( Dataset S2 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: Reads were mapped using Bowtie 2 within the RSEM package, which was also used to quantify transcript abundance ( 79 ).
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### Transcriptional profiling reveals signatures of latent developmental potential in <i>Arabidopsis</i> stomatal lineage ground cells. (PNAS 2021)

- DOI: 10.1073/pnas.2021682118 | PMCID: PMC8092560 | PMID: 33875598
- Evidence: Reads were mapped to TAIR10.18 via Bowtie2 ( 45 ) (read statistics are in Dataset S1 ).
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [Bowtie2, DESeq2] -> stage not stated [Fiji, ImageJ]

### Incipient genome erosion and metabolic streamlining for antibiotic production in a defensive symbiont. (PNAS 2021)

- DOI: 10.1073/pnas.2023047118 | PMCID: PMC8092579 | PMID: 33883280
- Version used: **2.3.2**
- Evidence: Sequenced reads were quality checked and trimmed using the Trimommatic implementation in KBase (v1.2.14, https://www.kbase.us ) ( 88 ), the alignment of the reads to the reference genome was performed with Bowtie 2 (v2.3.2) ( 89 ), and aligned reads were assembled using StringTie (v1.3.3) ( 90 ).
- Full pipeline: quality control [Bowtie2 v2.3.2, StringTie v1.3.3] -> read trimming [Bowtie2 v2.3.2, StringTie v1.3.3] -> alignment/mapping [Bowtie2 v2.3.2, StringTie v1.3.3] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [BLAST, ggplot2, ggpubr]

### Brd4-bound enhancers drive cell-intrinsic sex differences in glioblastoma. (PNAS 2021)

- DOI: 10.1073/pnas.2017148118 | PMCID: PMC8072233 | PMID: 33850013
- Version used: **2.3.4.3**
- Evidence: Raw reads from transposon calling cards were aligned to the murine genome build mm10 using Bowtie 2 (version 2.3.4.3) ( 73 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, HTSeq v0.11.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### <i>Drosophila</i> Fezf functions as a transcriptional repressor to direct layer-specific synaptic connectivity in the fly visual system. (PNAS 2021)

- DOI: 10.1073/pnas.2025530118 | PMCID: PMC8020669 | PMID: 33766917
- Evidence: High quality reads were mapped to the Ensembl build BDGP6 of the D. melanogaster genome using Bowtie2 ( 41 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2, MACS2 v2.1.1] -> stage not stated [Fiji, ImageJ]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Evidence: Cleaned short reads were aligned to reference genome TAIR10 by Bowtie2 ( 56 ), and expression abundance was calculated by RSEM with default parameters ( 57 ).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### Massively parallel discovery of human-specific substitutions that alter enhancer activity. (PNAS 2021)

- DOI: 10.1073/pnas.2007049118 | PMCID: PMC7812811 | PMID: 33372131
- Evidence: Reads were mapped using Bowtie2 (option -X 2000) and open chromatin regions were called using MACS2 (options -B–nomodel–shift -25–extsize 50).
- Full pipeline: alignment/mapping [Bowtie2, MACS2]

### Precise spatial structure impacts antimicrobial susceptibility of <i>S. aureus</i> in polymicrobial wound infections. (PNAS 2022)

- DOI: 10.1073/pnas.2212340119 | PMCID: PMC9907066 | PMID: 36520668
- Version used: **2.3.5**
- Evidence: Reads were mapped to P. aeruginosa strain PA14 (accession number GCF_000014625.1) downloaded from the National Center for Biotechnology Information (NCBI) using Bowtie2 version 2.3.5 ( 65 ) and tallied with featureCounts version 2.0.1.
- Full pipeline: read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0]

### A bacterium from a mountain lake harvests light using both proton-pumping xanthorhodopsins and bacteriochlorophyll-based photosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2211018119 | PMCID: PMC9897461 | PMID: 36469764
- Evidence: Mapping of reads to the S. glacialis AAP5 genome (GenBank accession GCF_004354345.1) was performed using Bowtie 2 in the local mode and allowing for one mismatch in the seed alignment.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [featureCounts]

### Leveraging a natural murine meiotic drive to suppress invasive populations. (PNAS 2022)

- DOI: 10.1073/pnas.2213308119 | PMCID: PMC9674240 | PMID: 36346842
- Evidence: ( 85 ) database and remapped the forward reads of each sample to the transcripts using Bowtie 2 ( 86 ).
- Full pipeline: stage not stated [Bowtie2, R]

### Sequestration of a dual function DNA-binding protein by <i>Vibrio cholerae</i> CRP. (PNAS 2022)

- DOI: 10.1073/pnas.2210115119 | PMCID: PMC9674212 | PMID: 36343262
- Version used: **2.4.1**
- Evidence: Paired-end reads were mapped to V. cholerae N16961 reference genome using Bowtie2 (version 2.4.1).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> stage not stated [GSEA, ImageJ]

### The highest-elevation frog provides insights into mechanisms and evolution of defenses against high UV radiation. (PNAS 2022)

- DOI: 10.1073/pnas.2212406119 | PMCID: PMC9674958 | PMID: 36346846
- Evidence: For N. phrynoides and Q. spinosa , clean reads were mapped to the corresponding reference transcript in Bowtie2 ( 69 ) (-q –phred64 –sensitive –dpad 0 –gbar 99999999 –mp 1,1 –np 1 –score-min L,0,-0.1 -I 1 -X 1000 –no-mixed –no-discordant -p l -k 200).
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RSEM] -> quantification [Python, RSEM] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [R] -> structure determination [Pilon] -> stage not stated [BUSCO, Metascape, RepeatMasker v4.08, StringTie]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Version used: **2.4.2**
- Evidence: Competitive read recruitment against the dereplicated database of vOTUs was performed with Bowtie 2 v2.4.2 ( 79 ) in sensitive mode, and the resulting alignments were sorted and indexed with SAMtools v1.11 ( 80 ).
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Evidence: Cleaned reads were mapped to their respective genome by using Bowtie2 version (v.) 2.3.4.1 ( 94 ) with default parameters.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Polycomb group (PcG) proteins prevent the assembly of abnormal synaptonemal complex structures during meiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2204701119 | PMCID: PMC9586294 | PMID: 36215502
- Evidence: Reads were aligned to Drosophila genome release 6 using bowtie2 ( 68 ) and were q20 filtered with Samtools ( 69 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR, deepTools] -> normalisation [R, deepTools, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [MACS2]

### Microbiome composition modulates secondary metabolism in a multispecies bacterial community. (PNAS 2022)

- DOI: 10.1073/pnas.2212930119 | PMCID: PMC9586298 | PMID: 36215464
- Version used: **2.4.2**
- Evidence: Bowtie2 v2.4.2 ( 61 ) was used to map reads to individually indexed genomes of Bc , Fj , or Pk .
- Full pipeline: alignment/mapping [HTSeq, SAMtools v1.9, fastp v0.20.0] -> quantification [HTSeq, SAMtools v1.9] -> differential/statistical testing [R v4.2] -> stage not stated [Bowtie2 v2.4.2, edgeR, eggNOG]

### Origin recognition complex harbors an intrinsic nucleosome remodeling activity. (PNAS 2022)

- DOI: 10.1073/pnas.2211568119 | PMCID: PMC9586268 | PMID: 36215487
- Evidence: ( 19 ) (SRR034475 and SRR034476), aligned it to the yeast genome (version Scer3) with bowtie2, and used MACS2 to identify the peaks (threshold: effective P = 0.01).
- Full pipeline: alignment/mapping [Bowtie2, MACS2]

### Deep-branching acetogens in serpentinized subsurface fluids of Oman. (PNAS 2022)

- DOI: 10.1073/pnas.2206845119 | PMCID: PMC9586279 | PMID: 36215489
- Evidence: The number of reads mapped to these contigs [as inferred by read mapping using Bowtie2 ( 50 )] was then used to estimate population relative abundances within each of the metagenomes.
- Full pipeline: read trimming [Clustal Omega v1.2.4] -> alignment/mapping [BLAST, Bowtie2, Clustal Omega v1.2.4, IQ-TREE v1.6.11] -> quantification [Bowtie2] -> differential/statistical testing [IQ-TREE v1.6.11] -> stage not stated [Prokka v1.14.5]

### DNA polymerase epsilon interacts with SUVH2/9 to repress the expression of genes associated with meiotic DSB hotspot in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208441119 | PMCID: PMC9564942 | PMID: 36191225
- Evidence: SPO11-1 oligo sequencing and MNase-seq data in WT were downloaded from ENA and mapped to the TAIR10 genome with Bowtie2 following the report of Choi et al.
- Full pipeline: read trimming [Bismark v0.22.3, Cutadapt, STAR v2.7.9a] -> alignment/mapping [Bismark v0.22.3, Bowtie2, Cutadapt, STAR v2.7.9a] -> quantification [Bismark v0.22.3, Cutadapt, DESeq2 v1.30.1, R, STAR v2.7.9a, featureCounts v2.0.0] -> stage not stated [ImageJ v1.52]

### Ectopic expression of meiotic cohesin generates chromosome instability in cancer cell line. (PNAS 2022)

- DOI: 10.1073/pnas.2204071119 | PMCID: PMC9549395 | PMID: 36179046
- Evidence: Then, reads were aligned to whole assembled genome, i.e., Macfas5, NCBI Assembly ID 704988, including all fragments and scaffolds, with Bowtie 2 ( 129 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, clusterProfiler] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [BEDTools, MACS2 v2.2, RepeatMasker]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: Processed reads were mapped to reference genome with bowtie2 -X 2000 –local –mm –no-discordant –no-mixed. hg38 (GRCh38, v26) reference genome was used for human cells, and mm10 (GRCm38, vM19) reference genome was used for mouse cells.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Sperm-inherited H3K27me3 epialleles are transmitted transgenerationally in &lt;i&gt;cis&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2209471119 | PMCID: PMC9546627 | PMID: 36161922
- Evidence: 50 bp single-end (R1 only) reads were mapped (tophat2 with bowtie2) to the Bristol (N2) genome version WS220 twice: once allowing 1 mismatch (1 mm) and a second time allowing 0 mismatches (0 mm).
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> normalisation [R] -> differential/statistical testing [DESeq2, TopHat]

### Cryptic specialized metabolites drive <i>Streptomyces</i> exploration and provide a competitive advantage during growth with other microbes. (PNAS 2022)

- DOI: 10.1073/pnas.2211052119 | PMCID: PMC9546628 | PMID: 36161918
- Evidence: Reads were aligned to the S. venezuelae genome using Bowtie2 ( 60 ), then sorted, indexed, and converted to BAM format using SAMtools ( 61 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### TGFB2-AS1 inhibits triple-negative breast cancer progression via interaction with SMARCA4 and regulating its targets <i>TGFB2</i> and <i>SOX2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2117988119 | PMCID: PMC9522332 | PMID: 36126099
- Version used: **2.3.5**
- Evidence: ChIP-Seq reads were mapped to the human reference genome (UCSC hg19) using Bowtie 2 version 2.3.5 with default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5] -> stage not stated [GSEA, Galaxy, MACS2 v2.1.2]

### Winter warming post floral initiation delays flowering via bud dormancy activation and affects yield in a winter annual crop. (PNAS 2022)

- DOI: 10.1073/pnas.2204355119 | PMCID: PMC9522361 | PMID: 36122201
- Version used: **2.4.4**
- Evidence: The cleans reads were mapped to B. napus genome v4.1 by Bowtie2 v2.4.4 with default parameters ( 39 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HISAT2 v2.2.1] -> normalisation [deepTools v2.3] -> visualisation [deepTools v2.3] -> stage not stated [HOMER, Picard, R, WGCNA]

### A scalable framework for the discovery of functional helicase substrates and helicase-driven regulatory switches. (PNAS 2022)

- DOI: 10.1073/pnas.2209608119 | PMCID: PMC9499579 | PMID: 36095194
- Version used: **2.4.2**
- Evidence: For genomic H-SELEX, curated reads were mapped on the MG1655 genome (NC_00096.3) with Bowtie2 (v2.4.2, default options).
- Full pipeline: quality control [Cutadapt v1.15, FastQC v0.11.5] -> read trimming [Cutadapt v1.15, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [Galaxy, MACS2, Python]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Evidence: The raw reads were quality checked and mapped to the maize reference genome (B73 RefGen_v4, AGPv4) ( 49 ) by Bowtie2 software (version 2.2.3) ( 50 ) and TopHat2 (version 2.0.14) ( 51 ).
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### 2-Guanidino-quinazoline promotes the readthrough of nonsense mutations underlying human genetic diseases. (PNAS 2022)

- DOI: 10.1073/pnas.2122004119 | PMCID: PMC9436315 | PMID: 35994666
- Evidence: RPF (25 to 35 nt) alignment is performed using both HiSat2 and bowtie2 to recover the maximum of reads on GRCh38-hg38 human genome assembly.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ]

### Nucleotide excision repair removes thymidine analog 5-ethynyl-2'-deoxyuridine from the mammalian genome. (PNAS 2022)

- DOI: 10.1073/pnas.2210176119 | PMCID: PMC9436350 | PMID: 35994676
- Evidence: Trimmed reads were aligned to hg38_UCSC by using bowtie2 with arguments -f -very-sensitive ( 45 , 46 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> stage not stated [BEDTools, SAMtools]

### Balanced control of thermogenesis by nuclear receptor corepressors in brown adipose tissue. (PNAS 2022)

- DOI: 10.1073/pnas.2205276119 | PMCID: PMC9388101 | PMID: 35939699
- Version used: **2.4.2**
- Evidence: FASTQ files were aligned to the GRCm38 (mm10) reference genome using the bowtie2 v2.4.2 aligner with the following parameters: -N 1.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, edgeR, kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR, kallisto] -> differential/statistical testing [R v4.1, edgeR, kallisto] -> stage not stated [Enrichr, SAMtools]

### Three distinct <i>Atoh1</i> enhancers cooperate for sound receptor hair cell development. (PNAS 2022)

- DOI: 10.1073/pnas.2119850119 | PMCID: PMC9371730 | PMID: 35925886
- Evidence: The pair-end reads were aligned to the mouse genome (mm10) by using Bowtie2 with the end-to-end parameter ( 68 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: For removing abundant contamination from digested ribosomal RNA (rRNA) present in the libraries, the reads aligned to a collection of rRNA sequences obtained from GenBank and University of California at Santa Cruz using Bowtie2 were discarded.
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; induces a muted host response in human blood that blunts the recruitment of neutrophils. (PNAS 2022)

- DOI: 10.1073/pnas.2123017119 | PMCID: PMC9351360 | PMID: 35881802
- Version used: **3.1**
- Evidence: Reads were mapped by Bowtie2.3.1 ( 60 ) to the hg38 reference genome, and uniquely mapped indices were determined by HTSeq-counts ( 61 ).
- Full pipeline: alignment/mapping [Bowtie2 v3.1, HTSeq] -> differential/statistical testing [DESeq2, R v3.5.1] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [limma]

### Wnt signaling regulates hepatocyte cell division by a transcriptional repressor cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2203849119 | PMCID: PMC9335208 | PMID: 35867815
- Evidence: Raw reads were mapped with Bowtie 2 ( 66 ) and processed and sorted with Samtools ( 67 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [Fiji, ImageJ, MACS2]

### Adaptive laboratory evolution and independent component analysis disentangle complex vancomycin adaptation trajectories. (PNAS 2022)

- DOI: 10.1073/pnas.2118262119 | PMCID: PMC9335240 | PMID: 35858453
- Evidence: The transcriptome analysis was performed using FastQC for quality control, Bowtie2 for mapping, htseq-count to count the number of mapped reads to each gene, and DeSeq2 to assess the differential expression between ancestor and evolved strains.
- Full pipeline: quality control [Bowtie2, FastQC, HTSeq] -> alignment/mapping [Bowtie2, FastQC, HTSeq] -> differential/statistical testing [Bowtie2, FastQC, HTSeq]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **2.2.6**
- Evidence: Reads were mapped to the mouse genome mm10 or human genome hg38 assembly using bowtie2 (v 2.2.6) ( 42 ).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### A long noncoding RNA influences the choice of the X chromosome to be inactivated. (PNAS 2022)

- DOI: 10.1073/pnas.2118182119 | PMCID: PMC9282422 | PMID: 35787055
- Version used: **2.3.4.2**
- Evidence: Reads were aligned to mm10 using Bowtie2 v2.3.4.2 using default parameters.
- Full pipeline: read trimming [Trimmomatic v0.36.6] -> alignment/mapping [Bowtie2 v2.3.4.2] -> stage not stated [Fiji, ImageJ, SAMtools v1.1.2]

### Single-cell transcriptome and accessible chromatin dynamics during endocrine pancreas development. (PNAS 2022)

- DOI: 10.1073/pnas.2201267119 | PMCID: PMC9245718 | PMID: 35733248
- Evidence: Trimmed fastq files were then mapped to the mm10 genome with bowtie2 ( 67 ) and the parameter “–very-sensitive.” Lastly, peaks were called using MACS2 ( 68 ) with “-q 0.01 –shift 0 –nomodel.” At the end of PEPATAC processing, 42 to 88 million reads aligned to the mouse genome, and 15,377 to 55,676 peaks per sample were detected.
- Full pipeline: read trimming [Bowtie2, MACS2] -> alignment/mapping [Bowtie2, MACS2] -> quantification [HOMER] -> dimensionality reduction/clustering [Monocle, R] -> simulation/modelling [Monocle] -> visualisation [R]

### Mapping functional regions of essential bacterial proteins with dominant-negative protein fragments. (PNAS 2022)

- DOI: 10.1073/pnas.2200124119 | PMCID: PMC9245647 | PMID: 35749361
- Evidence: The identity (parental protein, sequence location, and orientation) of each fragment was determined by aligning each read pair to the set of gene sequences included in the library using Bowtie2.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [AlphaFold, R]

### SpyChIP identifies cell type-specific transcription factor occupancy from complex tissues. (PNAS 2022)

- DOI: 10.1073/pnas.2122900119 | PMCID: PMC9231492 | PMID: 35696584
- Evidence: The reads were mapped to Drosophila genome build dm6 by Bowtie2 ( 16 ) using default settings, and peak calling was performed by MACS2 ( 17 ) with the following parameters: –nomodel –extsize 200 (all other parameters were default).
- Full pipeline: alignment/mapping [Bowtie2, MACS2] -> stage not stated [R, ggplot2]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **2.3.5.1**
- Evidence: The trimmed Illumina DNA sequence libraries from the three isolates were aligned against their respective reference genomes using Bowtie2 (v2.3.5.1; –very-sensitive –no-unal) ( 47 ), and the resulting bam files (one from each aligned library) were combined using samtools merge (v1.8).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Version used: **2.3.5**
- Evidence: Processed FASTQs were aligned to the mm10 genome using Bowtie2 (v2.3.5) ( 84 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Zinc finger protein 280C contributes to colorectal tumorigenesis by maintaining epigenetic repression at H3K27me3-marked loci. (PNAS 2022)

- DOI: 10.1073/pnas.2120633119 | PMCID: PMC9295756 | PMID: 35605119
- Version used: **2.2.9**
- Evidence: For analysis of ChIP-seq data, raw reads were aligned to reference genome hg19 by Bowtie2 (version 2.2.9).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, MACS2 v2.1.6] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> visualisation [deepTools v3.1.3] -> stage not stated [GSEA]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Reads identified with the VBIM sequence were aligned to the human genome (GRCh38) using Bowtie 2 using the “very-sensitive local” mode.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### An approach for evaluating the effects of dietary fiber polysaccharides on the human gut microbiome and plasma proteome. (PNAS 2022)

- DOI: 10.1073/pnas.2123411119 | PMCID: PMC9171781 | PMID: 35533274
- Evidence: Human DNA sequences were removed [Bowtie2 ( 58 ); hg19 build of the genome].
- Full pipeline: read trimming [Cutadapt, DADA2 v1.13.0] -> alignment/mapping [Picard, featureCounts] -> stage not stated [Bowtie2]

### Triple-helix potential of the mouse genome. (PNAS 2022)

- DOI: 10.1073/pnas.2203967119 | PMCID: PMC9171763 | PMID: 35503911
- Version used: **2.2.1**
- Evidence: Sequence reads were mapped onto the mouse reference genome (mm10) by bowtie2 version 2.2.1 ( 65 ) with the argument –X 1000.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.1] -> differential/statistical testing [R v3.3.1] -> stage not stated [RepeatMasker]

### Genetic architecture facilitates then constrains adaptation in a host-parasite coevolutionary arms race. (PNAS 2022)

- DOI: 10.1073/pnas.2121752119 | PMCID: PMC9170059 | PMID: 35412865
- Version used: **2.3.5.1**
- Evidence: Each of the remaining samples was then aligned to the complete P. subflava mtDNA using bowtie2 (version 2.3.5.1).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1] -> stage not stated [Python]

### rDNA array length is a major determinant of replicative lifespan in budding yeast. (PNAS 2022)

- DOI: 10.1073/pnas.2119593119 | PMCID: PMC9169770 | PMID: 35394872
- Version used: **2.3.5.1**
- Evidence: Reads were aligned to the S. cerevisiae genome (sacCer3, Release 64) using bowtie2 version 2.3.5.1 with default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, SAMtools] -> stage not stated [BCFtools]

### Gain of gene regulatory network interconnectivity at the origin of vertebrates. (PNAS 2022)

- DOI: 10.1073/pnas.2114802119 | PMCID: PMC8931241 | PMID: 35263228
- Evidence: Reads were aligned with Bowtie2 using GRCz10 (danRer10) and Bl71 ( 6 ) assemblies for zebrafish and amphioxus samples, respectively.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq, STAR v2.5.3a, kallisto] -> differential/statistical testing [DESeq2 v1.18.0, R v3.4] -> stage not stated [Cytoscape]

### An in-frame deletion mutation in the degron tail of auxin coreceptor <i>IAA2</i> confers resistance to the herbicide 2,4-D in <i>Sisymbrium orientale</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2105819119 | PMCID: PMC8892348 | PMID: 35217601
- Evidence: Read alignments to the de novo reference transcriptome were conducted with Bowtie2 ( 38 ) using the default “end-to-end” mode and the “sensitive” option.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [SAMtools] -> differential/statistical testing [R v3.3, edgeR] -> stage not stated [BCFtools, BUSCO]

### The dynamic trophic architecture of open-ocean protist communities revealed through machine-guided metatranscriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2100916119 | PMCID: PMC8851463 | PMID: 35145022
- Evidence: Bowtie2 ( 64 ) was used to assess the percentage of quality-controlled paired-end reads that mapped back to the assemblies.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> normalisation [Trimmomatic v0.36, kallisto] -> differential/statistical testing [DESeq2] -> machine learning [XGBoost] -> stage not stated [HMMER v3.1b]

### Vertical stratification of the air microbiome in the lower troposphere. (PNAS 2022)

- DOI: 10.1073/pnas.2117293119 | PMCID: PMC8851546 | PMID: 35131944
- Version used: **2.4.1**
- Evidence: Potential human contamination was then identified and subsequently removed by aligning the trimmed data against the GRCh38 human genome reference, using Bowtie2 v.2.4.1 with default parameters ( 30 ).
- Full pipeline: quality control [Bowtie2 v2.4.1] -> read trimming [Bowtie2 v2.4.1, Cutadapt v1.8.1] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> visualisation [vegan]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: Evidence of expression was at least one of the following two criteria: 1) an expression value of at least one transcripts per million (TPM) in all replicates of at least one sample in the RNASeq data after bowtie2 ( 55 ) alignment and Salmon ( 56 ) quantification or 2) at least one TPM in the gtf file obtained after a minimap2 ( 57 ) alignment and StringTie ( 58 ) quantification of IsoSeq3 polishe...
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Cutadapt ( 66 ) was used to trim adapters and trimmed sequences were aligned to the mm10 mouse genome assembly using bowtie2 ( 67 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### TRIM14 inhibits OPTN-mediated autophagic degradation of KDM4D to epigenetically regulate inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2113454119 | PMCID: PMC8851536 | PMID: 35145029
- Version used: **2.2.5**
- Evidence: For ChIP-seq analysis, paired-end sequencing reads from ChIP-seq were mapped to mm10 mouse reference genome by using Bowtie2 (v2.2.5) with default parameters, and the SAM files were converted to BAM files.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5] -> dimensionality reduction/clustering [clusterProfiler v4.0.5] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.6, Picard]

### A distinct role of STING in regulating glucose homeostasis through insulin sensitivity and insulin secretion. (PNAS 2022)

- DOI: 10.1073/pnas.2101848119 | PMCID: PMC8851542 | PMID: 35145023
- Version used: **2.3.5.1**
- Evidence: Single-end sequencing was performed by Annoroad Gene Technology, and clean reads with trimmed adapters were aligned to mm10 reference genome with the Bowtie2 (2.3.5.1) package ( 52 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1] -> alignment/mapping [Bowtie2 v2.3.5.1] -> quantification [HOMER v4.11.1] -> normalisation [HOMER v4.11.1] -> dimensionality reduction/clustering [clusterProfiler, pheatmap v1.0.12] -> visualisation [clusterProfiler, pheatmap v1.0.12]

### MadR mediates acyl CoA-dependent regulation of mycolic acid desaturation in mycobacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2111059119 | PMCID: PMC8872791 | PMID: 35165190
- Evidence: Briefly, raw reads were filtered for rRNA transcripts and aligned against the M. smegmatis mc 2 155 genome (ASM1500v1) with Bowtie2 ( 50 ) using the command line option “very-sensitive”.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [DESeq2, R, edgeR]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Evidence: For QuantSeq, raw RNA-seq reads were trimmed using Trimmomatic v.0.39 ( 75 ), and data were aligned using the bowtie2 ( 76 ) algorithm against the hg38 human genome version.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Spatiotemporal analysis identifies ABF2 and ABF3 as key hubs of endodermal response to nitrate. (PNAS 2022)

- DOI: 10.1073/pnas.2107879119 | PMCID: PMC8794810 | PMID: 35046022
- Evidence: Sequencing reads obtained from ChIP DNA and Input DNA for each TF were aligned to the Araport11 genome using Bowtie2 and duplicated reads were removed.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEDTools, ImageJ, MACS2, R]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Version used: **2.3.2.2**
- Evidence: Reads were aligned to version 3 of the B73 reference genome using Bowtie2 (version 2.3.2.2) ( 76 , 77 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: The clean reads were mapped to the Arabidopsis genome using Bowtie2 ( 60 ).
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### Conservation of magnetite biomineralization genes in all domains of life and implications for magnetic sensing. (PNAS 2022)

- DOI: 10.1073/pnas.2108655119 | PMCID: PMC8784154 | PMID: 35012979
- Version used: **2.2.1**
- Evidence: Reads were mapped with Bowtie2 version 2.2.1 ( 57 ) (setting: very sensitive) to a Chinook salmon reference transcriptome based on a Chinook salmon genome ( 36 ) having a total sequence length of 2.54 Gb (National Center for Bioinformatic Information Accession GCF_002872995.1).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2 v2.2.1] -> normalisation [R v3.12.1] -> dimensionality reduction/clustering [R v3.12.1] -> differential/statistical testing [BLAST, edgeR] -> visualisation [R v3.12.1] -> stage not stated [ImageJ]

### Deconstructing <i>Methanosarcina acetivorans</i> into an acetogenic archaeon. (PNAS 2022)

- DOI: 10.1073/pnas.2113853119 | PMCID: PMC8764690 | PMID: 34992140
- Evidence: Trimmomatic v0.39 ( 63 ) was used for quality filtering of the raw reads and Bowtie2 ( 64 ) for the mapping on the reference genome M. acetivorans C2A genome sequence ( 65 ) (accession no.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39]

### Translational control of <i>E2f1</i> regulates the <i>Drosophila</i> cell cycle. (PNAS 2022)

- DOI: 10.1073/pnas.2113704119 | PMCID: PMC8795540 | PMID: 35074910
- Version used: **2.1.0**
- Evidence: Raw reads were aligned to the Drosophila genome version 6 using TopHat2 version 2.0.9 ( 72 ), and Bowtie2 version 2.1.0.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, TopHat v2.0.9] -> quantification [Cufflinks]

### A quantitative framework reveals traditional laboratory growth is a highly accurate model of human oral infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116637119 | PMCID: PMC8764681 | PMID: 34992142
- Version used: **2.3.5**
- Evidence: The reads were mapped using Bowtie2 v2.3.5 to the P. gingivalis ATCC 33277 genome and to concatenated genomes of the 27 strains in the pangenome ( 50 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.9] -> read trimming [Cutadapt v2.6, featureCounts] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts] -> quantification [tidyverse v1.3.0] -> normalisation [DESeq2, pheatmap v1.0.12, tidyverse v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [MetaPhlAn, R v4.0, ggplot2 v3.3.2]

### A transcriptional program underlying the circannual rhythms of gonadal development in medaka. (PNAS 2023)

- DOI: 10.1073/pnas.2313514120 | PMCID: PMC10756274 | PMID: 38109538
- Version used: **2.2.5**
- Evidence: Clean reads were mapped on the Oryzias latipes reference assembly using bowtie2 (version 2.2.5), and the fragments per kilobase of exon per million fragments mapped (FPKM) were calculated using RSEM (version 1.2.12).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5, RSEM v1.2.12] -> quantification [Bowtie2 v2.2.5, RSEM v1.2.12] -> stage not stated [BLAST, DIAMOND, Metascape v3.5, R v3.5]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: For the data analyses, read sequences (50 bp) were aligned to the mm10 mouse reference genome (University of California, Santa Cruz, CA, USA; December 2011) using Bowtie 2 and TopHat (version 1.3.2) software programs.
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Microbiota configuration determines nutritional immune optimization. (PNAS 2023)

- DOI: 10.1073/pnas.2304905120 | PMCID: PMC10710091 | PMID: 38011570
- Version used: **2.4.2**
- Evidence: HUMAnN version 3.0.0-alpha.3 was used with default parameters; the version of the ChocoPhlAn and UniRef90 databases was 201901; the dependency versions were Python v3.8, Bowtie2 v2.4.2, and DIAMOND v2.0.4.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Bowtie2 v2.4.2, HOMER, HUMAnN v3.0, QIIME 2 v2020.2]

### Essential roles of the ANKRD31-REC114 interaction in meiotic recombination and mouse spermatogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2310951120 | PMCID: PMC10666023 | PMID: 37976262
- Evidence: Briefly, adapter sequences were trimmed and reads were mapped to mouse reference genome mm10 using Bowtie2 ( 40 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2]

### Dual thermal ecotypes coexist within a nearly genetically identical population of the unicellular marine cyanobacterium &lt;i&gt;Synechococcus&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2315701120 | PMCID: PMC10665897 | PMID: 37972069
- Version used: **2.4.3**
- Evidence: Read filtering was done with bbduk (bbmap, v.38.90), and all reads mapped to the available reference genome for LA31 GCF_018502385.1 ( 25 ) using bowtie2 v.2.4.3 ( 61 ), and separated from non- Synechococcus reads using samtools v.1.11 ( 62 ) and BEDtools v.2.30 ( 63 ).
- Full pipeline: read trimming [minimap2 v2.17] -> alignment/mapping [BEDTools v2.30, Bowtie2 v2.4.3, SAMtools v1.11, minimap2 v2.17] -> normalisation [SPAdes v3.15.2] -> stage not stated [R]

### The emergence and diversification of a zoonotic pathogen from within the microbiota of intensively farmed pigs. (PNAS 2023)

- DOI: 10.1073/pnas.2307773120 | PMCID: PMC10666105 | PMID: 37963246
- Version used: **1.2.2**
- Evidence: All assemblies were evaluated using QUAST v.5.0.1 ( 53 ) and we mapped reads back to de novo assemblies to investigate polymorphism (indicative of mixed cultures) using Bowtie2 v1.2.2 ( 54 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v1.2.2, QUAST v5.0.1] -> stage not stated [Canu v1.9, Prokka v1.14.5, R]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **2.4.5**
- Evidence: Trimmed reads were then mapped to the human genome (HG38 assembly) using Bowtie2 (v.
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Version used: **2.2.9**
- Evidence: Trimmed reads were mapped to the mm10 genome with Bowtie2 (v2.2.9) with default parameters.
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### In vitro DNA repair genomics using XR-seq with &lt;i&gt;Escherichia coli&lt;/i&gt; and mammalian cell-free extracts. (PNAS 2023)

- DOI: 10.1073/pnas.2314233120 | PMCID: PMC10614213 | PMID: 37844222
- Evidence: Then, the reads were aligned to hg38_UCSC reference genome by bowtie2 ( 40 ) with -f -very-sensitive arguments.
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [Bowtie2, Picard]

### Salicylic acid and RNA interference mediate antiviral immunity of plant stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302069120 | PMCID: PMC10589665 | PMID: 37824524
- Version used: **2.3.5**
- Evidence: Processed reads were aligned to the Arabidopsis genome (TAIR10) and TuMV-Scarlet sequence using bowtie2 v2.3.5 ( 51 ), i) allowing unique mapping to the TuMV-6K2:Scarlet sequence to assess the proportion of viral sRNAs and ii) allowing 1,000 times multimapping for gene-derived sRNA enrichment analysis.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2 v2.3.5] -> visualisation [Bioconductor, ggplot2, tidyverse] -> stage not stated [DESeq2, ImageJ, featureCounts]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Evidence: The Bismark tool ( 66 ) was used for processing the bisulfite sequencing data with default parameters (--bowtie2 --score-min L,0,-0.2 --no-discordant --maxins 500 --dovetail --no-mixed --ignore-quals).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Context-dependent function of the transcriptional regulator Rap1 in gene silencing and activation in <i>Saccharomyces cerevisiae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2304343120 | PMCID: PMC10556627 | PMID: 37769255
- Evidence: Sequencing reads were aligned using Bowtie2, using options = “--local --soft-clipped-unmapped-tlen --no-unal --no-mixed --no-discordant” ( 88 ) to a reference genome.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [ggplot2] -> stage not stated [MACS2]

### Structure of pre-miR-31 reveals an active role in Dicer-TRBP complex processing. (PNAS 2023)

- DOI: 10.1073/pnas.2300527120 | PMCID: PMC10523476 | PMID: 37725636
- Evidence: The resulting sequencing reads were adapter trimmed using Trim Galore and aligned using bowtie2 (“bowtie2–local–no-unal–no-discordant–no-mixed–phred33 40 -L 12”).
- Full pipeline: read trimming [Bowtie2, Trim Galore] -> alignment/mapping [Bowtie2, Trim Galore] -> quantification [ImageJ]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We mapped genomic reads with Bowtie2 ( 81 ) to the mm10 reference genome (setting: –very-sensitive) obtained from Ensembl.
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: The trimmed reads were then mapped to a custom genome, which included dm6 and concatenated barcode sequences corresponding to the SNAP-ChIP K-MetStat Panel, using bowtie2.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Light cues induce protective anticipation of environmental water loss in terrestrial bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2309632120 | PMCID: PMC10515139 | PMID: 37695906
- Version used: **2.2.6**
- Evidence: The clean reads from each sample were aligned to the B728a genome sequence (GCF_000012245.1, 2005 version) using Bowtie2 v2.2.6 ( 62 ) and TopHat2 v2.1.0 ( 63 , 64 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, HTSeq, TopHat v2.1.0] -> quantification [HTSeq] -> differential/statistical testing [R]

### Tet2 deletion in CD4+ T cells disrupts Th1 lineage commitment in memory cells and enhances T follicular helper cell recall responses to viral rechallenge. (PNAS 2023)

- DOI: 10.1073/pnas.2218324120 | PMCID: PMC10483640 | PMID: 37639586
- Evidence: Alignment to the mm10 reference genome was performed using Bismark ( 34 ) v0.19.0 with options (bismark --multicore 6 --bowtie2 -N 1 $MM10 -1 $FORWARD_READS -2 $REVERSE_READS).
- Full pipeline: quality control [FastQC v0.11.4, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark, Bowtie2, DESeq2 v1.30.1, featureCounts v1.6.3] -> differential/statistical testing [DESeq2 v1.30.1, featureCounts v1.6.3] -> stage not stated [BEDTools]

### CRISPR/dCas9 DNA methylation editing is heritable during human hematopoiesis and shapes immune progeny. (PNAS 2023)

- DOI: 10.1073/pnas.2300224120 | PMCID: PMC10450654 | PMID: 37579157
- Version used: **2.4.1**
- Evidence: For sequencing of TET2, data were aligned using bowtie2 (v 2.4.1) to the human genome (hg38), and the variant allele frequency analyzed using VarScan (v 2.4.2) with base quality >15, minimum variant allele frequency > 0.01 and P -value for calling variants >0.01.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [HISAT2 v2.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.4.1, HISAT2 v2.1, VarScan v2.4.2] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Version used: **2.2.7**
- Evidence: To identify the W-linked sequences, male and female Illumina paired-end genomic DNA reads were aligned to the polished and decontaminated contig assembly using Bowtie2 (v2.2.7) ( 68 ).
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Host hydrocarbons protect symbiont transmission from a radical host defense. (PNAS 2023)

- DOI: 10.1073/pnas.2302721120 | PMCID: PMC10400980 | PMID: 37487102
- Version used: **2.3.2**
- Evidence: The retained reads were mapped to either the S. coelicolor or S. philanthi genome ( 50 ) using Bowtie2 (v.2.3.2) and StringTie (v.1.3.3b) implemented in KBase ( 98 ) using default settings. rRNA sequences were removed from the dataset before differential gene expression was analyzed using DESeq2 (v.1.22.2) ( 99 ) in RStudio (v1.1.453 with R v3.5.0).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> differential/statistical testing [Bowtie2 v2.3.2, DESeq2 v1.22.2, R v3.5, StringTie v1.3.3b] -> visualisation [ggplot2]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: The sequence reads were mapped to UCSC build mm9 (NCBI Build 37) assembly using bowtie2 (Galaxy version 2.3.4) with default parameters ( 37 , 38 ).
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### High-resolution mapping reveals the mechanism and contribution of genome insertions and deletions to RNA virus evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2304667120 | PMCID: PMC10400975 | PMID: 37487061
- Evidence: MultiMatch uses bowtie2 as the alignment engine ( 89 , 90 ).
- Full pipeline: alignment/mapping [Bowtie2]

### MicroRNA-335-5p suppresses voltage-gated sodium channel expression and may be a target for seizure control. (PNAS 2023)

- DOI: 10.1073/pnas.2216658120 | PMCID: PMC10372546 | PMID: 37463203
- Evidence: Reads were mapped to the human genome using Bowtie2 with soft-clipping enabled.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler] -> stage not stated [ComplexHeatmap, DESeq2, R, tidyverse]

### Ancient vertebrate dermal armor evolved from trunk neural crest. (PNAS 2023)

- DOI: 10.1073/pnas.2221120120 | PMCID: PMC10372632 | PMID: 37459514
- Evidence: Sterlet/bichir scute/scale RNA sequencing libraries were aligned to the sterlet/bichir sequences, while the zebrafish scale RNA sequencing libraries were aligned to the zebrafish sequences using Bowtie2 ( 57 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega v1.2.3] -> visualisation [ComplexHeatmap] -> stage not stated [DESeq2, featureCounts]

### NOS inhibition reverses TLR2-induced chondrocyte dysfunction and attenuates age-related osteoarthritis. (PNAS 2023)

- DOI: 10.1073/pnas.2207993120 | PMCID: PMC10629581 | PMID: 37428931
- Evidence: Obtained reads were mapped to the hg19 genome (annotation releases: GRCh37.p13) using Tophat2 ( 71 ) and Bowtie2 ( 72 ) with very sensitive settings.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [featureCounts] -> stage not stated [GSEA, MACS2]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: Raw sequence data were first mapped to V. destructor reference genome Vdes_3.0 [GCF_002443255.1] ( 26 ) using Bowtie2 ( 27 ).
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Phosphorylation of DNA-PKcs at the S2056 cluster ensures efficient and productive lymphocyte development in XLF-deficient mice. (PNAS 2023)

- DOI: 10.1073/pnas.2221894120 | PMCID: PMC10288554 | PMID: 37307443
- Evidence: Best-path searching algorithm [related to YAHA ( 83 )] was used to select optimal junctions from Bowtie2-reported top alignments (alignment score > 50).
- Full pipeline: alignment/mapping [Bowtie2]

### Role of the bicarbonate transporter SLC4γ in stony-coral skeleton formation and evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2216144120 | PMCID: PMC10268325 | PMID: 37276409
- Evidence: Briefly, all potential target sites that matched the pattern [G, C, or A]N 20 GG were identified in the exon sequences, and all sites that had exact matches elsewhere in the A. millepora genome were identified using Bowtie2 ( 65 ) and removed from consideration.
- Full pipeline: stage not stated [BLAST, Bowtie2]

### Mechanoepigenetic regulation of extracellular matrix homeostasis via Yap and Taz. (PNAS 2023)

- DOI: 10.1073/pnas.2211947120 | PMCID: PMC10235980 | PMID: 37216538
- Evidence: Sequenced reads were aligned to the mm10 build of the mouse genome using Bowtie2 with default settings ( 67 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2, Picard, SAMtools, deepTools, featureCounts]

### Osteolectin increases bone elongation and body length by promoting growth plate chondrocyte proliferation. (PNAS 2023)

- DOI: 10.1073/pnas.2220159120 | PMCID: PMC10235998 | PMID: 37216542
- Version used: **4.1**
- Evidence: Raw reads were trimmed using TrimGalore 0.6.4 and mapped to the Ensembl GRCh38 mouse reference genome version 100 using Bowtie 2.4.1.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bowtie2 v4.1, Trim Galore v0.6.4] -> alignment/mapping [Bowtie2 v4.1, SAMtools v1.12, Trim Galore v0.6.4] -> stage not stated [deepTools v3.5.1]

### Hfq-licensed RNA-RNA interactome in <i>Pseudomonas aeruginosa</i> reveals a keystone sRNA. (PNAS 2023)

- DOI: 10.1073/pnas.2218407120 | PMCID: PMC10214189 | PMID: 37285605
- Version used: **2.4.5**
- Evidence: Reads were assessed for quality control and adaptor trimming with bcl2fastq and mapped with bowtie2 (version 2.4.5); read quantification was performed with htseq ( 59 ) and differential gene expression analysis was conducted with DESeq2 ( 60 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, DESeq2] -> read trimming [Bowtie2 v2.4.5, DESeq2] -> alignment/mapping [Bowtie2 v2.4.5, DESeq2] -> quantification [Bowtie2 v2.4.5, DESeq2] -> differential/statistical testing [Bowtie2 v2.4.5, DESeq2] -> stage not stated [R]

### Differentiation of <i>Plasmodium</i> male gametocytes is initiated by the recruitment of a chromatin remodeler to a male-specific cis-element. (PNAS 2023)

- DOI: 10.1073/pnas.2303432120 | PMCID: PMC10193995 | PMID: 37155862
- Evidence: Paired-end read sequences were mapped using Bowtie 2 software (version 3) on the P. berghei genome.
- Full pipeline: alignment/mapping [Bowtie2, MACS2, Picard]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: Processing of snATAC-Seq data was performed using SnapATAC ( 18 ), and reads were aligned to the hg38 genome using bowtie2 with the following parameters: bowtie2 -X2000 –no-mixed –no-discordant.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### Generation of zero-valent sulfur from dissimilatory sulfate reduction in sulfate-reducing microorganisms. (PNAS 2023)

- DOI: 10.1073/pnas.2220725120 | PMCID: PMC10194018 | PMID: 37155857
- Version used: **2.33**
- Evidence: The clean reads were first mapped to DvH’s rRNA gene to remove rRNA sequences by Bowtie2 (v2.33) ( 64 ).
- Full pipeline: read trimming [Trimmomatic v0.35] -> alignment/mapping [Bowtie2 v2.33, HTSeq] -> quantification [HTSeq] -> stage not stated [mothur v1.39]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Version used: **2.3.5**
- Evidence: To remove non- P. aeruginosa reads, trimmed reads were mapped with bowtie2 v2.3.5 using default parameters to a metagenome of 105 decoy strains from 59 species, based on species previously identified in sputum samples ( Dataset S1 ) ( 7 , 52 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Ancient DNA from a lost Negev Highlands desert grape reveals a Late Antiquity wine lineage. (PNAS 2023)

- DOI: 10.1073/pnas.2213563120 | PMCID: PMC10151551 | PMID: 37068234
- Version used: **2.2.5**
- Evidence: The archaeological samples were mapped to the grapevine reference genome assembly (12X.v2) ( 65 ) using Bowtie2 version 2.2.5 ( 66 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.5] -> variant calling [GATK, VCFtools] -> dimensionality reduction/clustering [pheatmap] -> visualisation [ggplot2]

### Phylogeographic reconstruction of the emergence and spread of Powassan virus in the northeastern United States. (PNAS 2023)

- DOI: 10.1073/pnas.2218012120 | PMCID: PMC10120011 | PMID: 37040418
- Evidence: PCR duplicates were removed, reads were aligned to the reference genome using Bowtie2, and consensus genomes were called at a minimum frequency threshold of 0.75 and a minimum coverage of 10x using Geneious Prime 2020.0.4.
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [Nextstrain] -> stage not stated [IQ-TREE v1.6.12, R]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Evidence: In four strains FRR 1658, FRR 2889, FRR 3823, and CBS 101075, this presence/absence of Hφ was confirmed by read mapping to the CBS 144490 assembly using bowtie2 ( 62 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### On the origin of appetite: GLWamide in jellyfish represents an ancestral satiety neuropeptide. (PNAS 2023)

- DOI: 10.1073/pnas.2221493120 | PMCID: PMC10104569 | PMID: 37011192
- Evidence: 504557388 sequence reads from 12 Cladonema libraries were mapped against Artemia transcript sequences using Bowtie 2 ( 44 ) (ver.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [R, RSEM] -> dimensionality reduction/clustering [R] -> differential/statistical testing [edgeR] -> stage not stated [InterProScan v5.52]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Evidence: The raw reads were trimmed using Trimomatic v0.33 software ( 51 ), and the trimmed reads were mapped against either WYMV RNA1 (GenBank accession AB627808.1 ) using Bowtie2 software ( bowtie-bio.sourceforge.net/bowtie2/ ), or onto the wheat genome assembly refseq.2 (GCA_900519105: Ensembl plants) using HISAT2 v2-2.2.1 software ( 52 ).
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### Genome-wide maps of rare and atypical UV photoproducts reveal distinct patterns of damage formation and mutagenesis in yeast chromatin. (PNAS 2023)

- DOI: 10.1073/pnas.2216907120 | PMCID: PMC10013872 | PMID: 36853943
- Evidence: The resulting UVDE-seq reads were mapped to the yeast (SacCer3) genome using bowtie2 ( 50 ), and the corresponding dinucleotide damage site was identified and counted, as previously described ( 10 , 14 ).
- Full pipeline: alignment/mapping [BEDTools, Bowtie2, SAMtools] -> visualisation [PyMOL]

### Two differentially stable rDNA loci coexist on the same chromosome and form a single nucleolus. (PNAS 2023)

- DOI: 10.1073/pnas.2219126120 | PMCID: PMC9992848 | PMID: 36821584
- Evidence: Briefly, Hi-C reads were aligned using Bowtie 2 ( 60 ) and processed using command lines based on HiCLib tool developed in the Mirny lab ( 61 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2] -> visualisation [ImageJ] -> stage not stated [kallisto]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Version used: **2.4.4**
- Evidence: To calculate interchromosomal interactions, Hi-C read pairs were mapped to the pri.v2 assembly using Bowtie2 (2.4.4) ( 55 ), with reads uniquely mapped and having mapping quality larger than 30 kept.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### A thermal receptor for nonvisual sunlight detection in myriapods. (PNAS 2023)

- DOI: 10.1073/pnas.2218948120 | PMCID: PMC9974506 | PMID: 36780532
- Version used: **2.26**
- Evidence: These clean reads were then aligned to PacBio isoform sequences using Bowtie 2 (version 2.26) ( 27 ) and quantified by RNA Seq by Expectation Maximization ( 28 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.26] -> quantification [Bowtie2 v2.26]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Version used: **2.4.2**
- Evidence: ...is, and sequenced on a BGISeq 500 instrument. sRNA Libraries Mapping and Comparison. sRNA libraries ( 85 ) were mapped to the MAC + IES assembly with bowtie2 v2.4.2 ( 86 ) using default parameters.
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Version used: **2.3.5**
- Evidence: Where necessary, raw data were reanalyzed by bowtie2 (2.3.5) ( 77 ) alignment to the most recent Cryptococcus neoformans H99 or KN99α genome ( fungibd.org ), count matrices generated with HTSeq (1.99.2) ( 78 ) and RNA-seq analysis with Bioconductor DESeq2 (1.22.2) ( 79 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### ACSL4-mediated H3K9 and H3K27 hyperacetylation upregulates SNAIL to drive TNBC metastasis. (PNAS 2024)

- DOI: 10.1073/pnas.2408049121 | PMCID: PMC11670210 | PMID: 39700137
- Evidence: Human genome (GRch38) was downloaded from iGenomes and indexed using Bowtie2-build with default parameters.
- Full pipeline: stage not stated [Bowtie2]

### Mutation-based mechanism and evolution of the potent multidrug efflux pump RE-CmeABC in &lt;i&gt;Campylobacter&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2415823121 | PMCID: PMC11665921 | PMID: 39602248
- Evidence: The trimmed reads were mapped against C. jejuni NCTC11168 genome sequences using Bowtie2 ( 60 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic] -> alignment/mapping [Bowtie2, MAFFT] -> stage not stated [Python]

### The HUSH epigenetic repressor complex silences PML nuclear body-associated HSV-1 quiescent genomes. (PNAS 2024)

- DOI: 10.1073/pnas.2412258121 | PMCID: PMC11626126 | PMID: 39589886
- Version used: **2.5.1**
- Evidence: Trimmed reads (containing more than 36 nucleotides) were aligned to the human (hg38) reference genome concatenated with the HSV-1 genome (GCF_000859985.2.fa) using bowtie2 (v2.5.1).
- Full pipeline: read trimming [Bowtie2 v2.5.1, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.1] -> stage not stated [ImageJ]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Evidence: Map readings to vOTUs were used to create a bam file of Bowtie2.
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Version used: **2.4.1**
- Evidence: Reads were mapped to the H37Rv genome [RefSeq identifier GCF_000195955.2 with socAB annotation added as previously described ( 76 )] using Bowtie2 v2.4.1 ( 77 ) and sorted using samtools v1.13 ( 78 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### The fork protection complex generates DNA topological stress-induced DNA damage while ensuring full and faithful genome duplication. (PNAS 2024)

- DOI: 10.1073/pnas.2413631121 | PMCID: PMC11626154 | PMID: 39589889
- Evidence: S288c assembly from Saccharomyces Genome Database) using Bowtie 2 ( https://bowtie-bio.sourceforge.net/bowtie2/index.shtml ).
- Full pipeline: stage not stated [Bowtie2, MACS2, SAMtools]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Reads were then aligned to the Atlantic salmon genome downloaded from Ensembl (Salmo_salar-GCA_905237065.2) using “Bowtie2” ( 73 ) and parameters “--very-sensitive --maxins 1500 --end-to-end”. “Samtools view” was used to filter for primary alignments with mapping quality score over 20 (“-F 256 -q 20”). “Picard MarkDuplicates” ( 74 ) was used to identify and remove duplicate reads.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### An E2 ubiquitin-conjugating enzyme links diubiquitinated H2B to H3K27M oncohistone function. (PNAS 2024)

- DOI: 10.1073/pnas.2416614121 | PMCID: PMC11621828 | PMID: 39560642
- Evidence: In Galaxy, fastq files were aligned to the ce10 genome using Bowtie2, and variants were called using MiModD.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [deepTools v3.3.1] -> stage not stated [ChimeraX, SAMtools v1.8]

### The glucocorticoid receptor potentiates aldosterone-induced transcription by the mineralocorticoid receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2413737121 | PMCID: PMC11588051 | PMID: 39541347
- Evidence: The ChIP-seq data were aligned to the mouse reference mm10 genome using Bowtie 2 with command Bowtie2 –p 8 –x bowtie2_ref/genome_prefix –U read1.fastq –S result.sam.
- Full pipeline: quality control [Cutadapt v1.18] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2, STAR v2.70] -> normalisation [DESeq2] -> stage not stated [HOMER, SAMtools]

### Homeotic and nonhomeotic patterns in the tetrapod vertebral formula. (PNAS 2024)

- DOI: 10.1073/pnas.2411421121 | PMCID: PMC11588047 | PMID: 39527744
- Evidence: We mapped the raw reads for the chicken data to the bGalGal1 genome assembly using bowtie2 ( 104 ) with standard parameters and used samtools ( 105 ) with standard parameters to remove duplicates and sort the alignments.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [BLAST, BUSCO, SciPy, phytools]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Version used: **2.2.5**
- Evidence: The cleaned sequence reads were then aligned to the de novo reference genome (Acart.genome.v1) with two different strategies: 1) Bowtie analysis: we used Bowtie2 (version 2.2.5) with the options “--local --no-unal”, reporting only the best alignment for multimapped reads.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### Cytosolic &lt;i&gt;N6AMT1-&lt;/i&gt;dependent translation supports mitochondrial RNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2414187121 | PMCID: PMC11588129 | PMID: 39503847
- Evidence: Retained reads were then mapped to the canonical transcriptome with bowtie2 using default parameters.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, RepeatMasker] -> quantification [CellProfiler, ImageJ v1.53] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [Cutadapt, DESeq2, GSEA, R v4.3.1]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **2.4.5**
- Evidence: Filtered reads were aligned on the in silico mutant genome using bowtie2 version 2.4.5 with default parameters ( 53 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Soil viral-host interactions regulate microplastic-dependent carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2413245121 | PMCID: PMC11551317 | PMID: 39467127
- Evidence: Bowtie2 was used to align the clean reads back to the unigenes with default parameters for quantification of gene expression levels ( 84 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BLAST, Bowtie2, HMMER] -> quantification [Bowtie2] -> stage not stated [DESeq2, R v4.0.3, vegan]

### Dynamics of transcription-coupled repair of cyclobutane pyrimidine dimers and (6-4) photoproducts in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416877121 | PMCID: PMC11536166 | PMID: 39441633
- Version used: **2.4.5**
- Evidence: We aligned the reads to the complete E. coli reference genome (NC_0009133) using Bowtie2 (version 2.4.5) with the seed parameter “--seed 1.” The fasta file was downloaded from NCBI, and Bowtie2 index files were created using the bowtie2-build command.
- Full pipeline: read trimming [Cutadapt v3.4, STAR] -> alignment/mapping [Bowtie2 v2.4.5, STAR] -> stage not stated [BEDTools, Snakemake]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Version used: **2.2.8**
- Evidence: Generated reads were mapped to the human (hg19) reference genome using TopHat v2.1.1 in combination with Bowtie2 v2.2.8 and SAMtools v0.1.18.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **2.3.5**
- Evidence: Illumina MIC and MAC reads ( 83 ) were mapped to MAC reference assembly with bowtie2 v2.3.5 ( 106 ) with default parameters.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **2.4.5**
- Evidence: Paired-end reads were trimmed with TrimGalore and mapped to mm10 using Bowtie2 (v2.4.5) ( 69 ) with the following options: --no-mixed --no-discordant.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: The cleaned reads were then mapped to the reference genome (Gmax v4, Phytozome) using the bowtie2 program ( 51 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Light regulates widespread plant alternative polyadenylation through the chloroplast. (PNAS 2024)

- DOI: 10.1073/pnas.2405632121 | PMCID: PMC11348263 | PMID: 39150783
- Evidence: Briefly, after adapter sequence removal, reads were mapped to the A. thaliana reference genome (TAIR10) by using the Bowtie2 program ( 50 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> stage not stated [Bioconductor]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: Reads were mapped to the human genome (GRCh37) using Bowtie 2 and BAM files were created using Picard.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### m&lt;sup&gt;6&lt;/sup&gt;A modification plays an integral role in mRNA stability and translation during pattern-triggered immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2411100121 | PMCID: PMC11331096 | PMID: 39116132
- Evidence: Three replicates of m 6 A input and IP libraries were aligned to the Arabidopsis genome (TAIR10) using Bowtie2.0 ( 51 ).
- Full pipeline: read trimming [STAR, Trim Galore] -> alignment/mapping [Bowtie2, STAR, Trim Galore] -> variant calling [Bioconductor] -> normalisation [Bioconductor, DESeq2, HTSeq]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Version used: **2.3.4.2**
- Evidence: Reads were quality checked with FASTQC before mapping to hg19 reference genome with Bowtie2 (v2.3.4.2) ( 63 ).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### Improvement of a mouse infection model to capture &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt; chronic physiology in cystic fibrosis. (PNAS 2024)

- DOI: 10.1073/pnas.2406234121 | PMCID: PMC11331117 | PMID: 39102545
- Version used: **2.4.2**
- Evidence: After checking read quality in FastQC (v0.11.9), reads were mapped to the genomes of 105 non– P. aeruginosa decoy strains in bowtie2 (v2.4.2) ( 33 ).
- Full pipeline: quality control [Bowtie2 v2.4.2, FastQC v0.11.9] -> read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.4.2, FastQC v0.11.9] -> stage not stated [featureCounts v2.0.1]

### Convergent evolution in toxin detection and resistance provides evidence for conserved bacterial-fungal interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2304382121 | PMCID: PMC11317636 | PMID: 39088389
- Version used: **2.4.2**
- Evidence: Trimmed reads were then mapped to P. aeruginosa PA14 reference (available for download from Pseudomonas.com ) genome using Bowtie2 v2.4.2 with default parameters for end-to-end alignment.
- Full pipeline: read trimming [Bowtie2 v2.4.2] -> alignment/mapping [Bowtie2 v2.4.2, Clustal Omega] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, PyMOL, featureCounts]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **2.3.31**
- Evidence: Raw reads were aligned with bowtie2 v2.3.31 ( 56 ).
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Life stage-specific poly(A) site selection regulated by <i>Trypanosoma brucei</i> DRBD18. (PNAS 2024)

- DOI: 10.1073/pnas.2403188121 | PMCID: PMC11260167 | PMID: 38990950
- Evidence: Fastq files were then mapped to the T. brucei Lister927 genome using Bowtie2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, R, Seurat]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: Adapters were removed with NGmerge (Version 0.3), and bowtie2 (Version 2.5.1) aligned the resulting sequences to mouse index genome mm10, downloaded from bowtie2’s manual ( https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml ) on 2 May 2023 ( 44 , 45 ) SAMtools (Version 1.13) sort, view, fixmate, and markdup were used to remove PCR duplicates, with SAMtools index and view used to remove mitoch...
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **2.3.5**
- Evidence: Cleaned reads were aligned to tomato M82 genome v1 ( 42 ) using Bowtie2 v2.3.5 using mode “--very-sensitive” ( 43 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### Membrane association of active genes organizes the chloroplast nucleoid structure. (PNAS 2024)

- DOI: 10.1073/pnas.2309244121 | PMCID: PMC11252823 | PMID: 38968115
- Version used: **2.4.4**
- Evidence: Briefly, obtained raw sequencing reads were trimmed using trim_galore v.0.6.7 ( https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ ) with cutadapt v.3.5 ( 58 ) and mapped to the TAIR10 Arabidopsis plastid genome ( www.arabidopsis.org ) using Bowtie2 v.2.4.4 ( 59 ).
- Full pipeline: read trimming [Bowtie2 v2.4.4, Cutadapt v3.5] -> alignment/mapping [Bowtie2 v2.4.4, Cutadapt v3.5] -> quantification [BEDTools v2.30.0, SAMtools v1.13]

### A distal enhancer of GATA3 regulates Th2 differentiation and allergic inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2320727121 | PMCID: PMC11228505 | PMID: 38923989
- Evidence: H3K27ac ChIP-seq data for murine lung CD4 + T cells and transcription factor ChIP-seq for cultured murine CD4 + T cells ( GSE20898 , GSE22104 , GSE40463 , GSE66343 , GSE85172 , GSE109109 , GSE123198 , and GSE237916 ) ( 25 – 32 ) were aligned to mm10 genome assembly using Bowtie2 ( 41 ), and aligned data were visualized using Homer.
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [Bowtie2]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Evidence: The raw Hi-C reads were mapped against the Tibetan sheep genome (GCA_017524585.1) using Bowtie2 ( 78 ).
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Modular binder technology by NGS-aided, high-resolution selection in yeast of designed armadillo modules. (PNAS 2024)

- DOI: 10.1073/pnas.2318198121 | PMCID: PMC11228518 | PMID: 38917007
- Evidence: Single reads were then mapped back to the wild-type dArmRP sequence using Bowtie2 ( 30 ) with triple penalties for gap opening and extension and the noncoding sequences excluded.
- Full pipeline: alignment/mapping [Bowtie2, UMAP] -> dimensionality reduction/clustering [Python, UMAP] -> structure determination [PHENIX] -> visualisation [UMAP] -> stage not stated [CCP4]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: For chromosome anchoring, high-quality paired-end reads were mapped to the assembled contigs using Bowtie2 ( 70 ) with the parameters "-end-to-end --very-sensitive -L 30".
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Long noncoding RNA LIRIL2R modulates FOXP3 levels and suppressive function of human CD4<sup>+</sup> regulatory T cells by regulating IL2RA. (PNAS 2024)

- DOI: 10.1073/pnas.2315363121 | PMCID: PMC11161746 | PMID: 38805281
- Version used: **2.3.5.1**
- Evidence: Alignment, sorting, filtering, and deduplication for the CUT&Tag analysis was performed using Bowtie2 (v2.3.5.1) ( 60 ), Samtools (v1.9) ( 61 ), and Picard ( http://broadinstitute.github.io/picard/ ) MarkDuplicates (v2.21.7) with the same parameters as described in the ATAC-seq analysis.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9, kallisto] -> differential/statistical testing [R, limma v3.42.2] -> stage not stated [GSEA]

### CRISPRi screens identify the lncRNA, <i>LOUP</i>, as a multifunctional locus regulating macrophage differentiation and inflammatory signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2322524121 | PMCID: PMC11145268 | PMID: 38781216
- Evidence: Adapters were trimmed with Ngmerge ( 56 ) and mapped to GRCh38 primary assembly for humans, or GRCm39 for mice, with Bowtie2 (--very-sensitive --maxins 1000) ( 57 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, deepTools] -> stage not stated [AlphaFold, DESeq2]

### DNA polymerase delta governs parental histone transfer to DNA replication lagging strand. (PNAS 2024)

- DOI: 10.1073/pnas.2400610121 | PMCID: PMC11098083 | PMID: 38713623
- Evidence: Sequenced reads were mapped to the reference genome of Saccharomyces cerevisiae (sacCer3) with Bowtie2 software ( 50 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [BEDTools]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: ChIP-Seq reads were aligned to the human genome (hg19) with bowtie2 (v.2-2.4.5) ( 21 ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Version used: **2.2.5**
- Evidence: Small-RNA reads were mapped using Bowtie2 version 2.2.5 ( 85 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: Reads were aligned with bowtie2 ( 84 ) v2.4.2 with options –no-unal –very-sensitive and sorted using samtools ( 81 ) v1.12.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Version used: **2.2.6**
- Evidence: D. melanogaster spiked-in samples were aligned using Bowtie2 v2.2.6 ( 91 ) with parameters --sensitive --no-unal, while non-spiked-in data were aligned using Bowtie v1.1.2 ( 92 ) with parameters -m 1 -v 2, to human GRCh38 genome assembly with Ensembl gene annotation GRCh38 release 78.
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: ChIP-seq libraries were sequenced on a Nextseq 550 (Illumina) and the resulting datasets were mapped to the Drosophila genome (dm6) using Bowtie2 and analyzed using MACS2 ( 51 , 52 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### A sodium-dependent trehalose transporter contributes to anhydrobiosis in insect cell line, Pv11. (PNAS 2024)

- DOI: 10.1073/pnas.2317254121 | PMCID: PMC10998604 | PMID: 38551840
- Evidence: Gene expression was quantified using RSEM v1.3.1 (--bowtie2) ( 78 ) and the following downstream analysis was performed using the Trinity package v2.15.1 (abundance_estimates_to_matrix.pl, run_DE_analysis.pl) ( 79 ).
- Full pipeline: quantification [Bowtie2, RSEM v1.3.1] -> stage not stated [HMMER, ImageJ v1.53t]

### Intergenerational protective anti-gut commensal immunoglobulin G originates in early life. (PNAS 2024)

- DOI: 10.1073/pnas.2309994121 | PMCID: PMC10990157 | PMID: 38517976
- Version used: **2.4.1**
- Evidence: The resulting demultiplexed reads were analyzed with METAPHLAN v3 ( 56 ) and based on taxonomic classification reads were mapped with Bowtie2 v2.4.1 ( 57 ) to reference genome of Staphylococcus xylosus to determine coverage.
- Full pipeline: read trimming [Bowtie2 v2.4.1, MAFFT v7.475] -> alignment/mapping [Bowtie2 v2.4.1, MAFFT v7.475] -> dimensionality reduction/clustering [Docker] -> visualisation [R v4.0, phyloseq] -> stage not stated [BLAST, RAxML]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: We aligned them to the human genome (hg19) using Bowtie2 with the “--very-sensitive” option ( 57 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Morc1 reestablishes H3K9me3 heterochromatin on piRNA-targeted transposons in gonocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2317095121 | PMCID: PMC10990106 | PMID: 38502704
- Evidence: Reads trimmed to 25 bp were aligned to the mouse (mm10) genome using Bowtie2 with -N 1 and -X 2000 parameters.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Picard] -> quantification [DESeq2] -> normalisation [DESeq2] -> stage not stated [RepeatMasker]

### Frequent horizontal chromosome transfer between asexual fungal insect pathogens. (PNAS 2024)

- DOI: 10.1073/pnas.2316284121 | PMCID: PMC10945790 | PMID: 38442176
- Version used: **2.4.4**
- Evidence: Comparison between published short reads as well as the 150 PE Illumina reads generated in this study and the R3-I4 and the R1-A and R3-A assembly was determined by mapping and SNP calling using bowtie2 (version 2.4.4) ( 63 ) and bcftools mpileup (version = 1.14) ( 64 ).
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.4.4] -> variant calling [BCFtools, Bowtie2 v2.4.4] -> differential/statistical testing [R v3.6.0] -> stage not stated [WhatsHap v1.6]

### RNA-catalyzed evolution of catalytic RNA. (PNAS 2024)

- DOI: 10.1073/pnas.2321592121 | PMCID: PMC10945747 | PMID: 38437533
- Version used: **2.4.2**
- Evidence: The sequences were aligned to that of Seq0 using bowtie2 v2.4.2 ( 32 ), and the frequency of substitutions, insertions, and deletions was determined for each of the 27 nucleotide positions that were free to vary ( Fig.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2] -> visualisation [R] -> stage not stated [Python]

### Genome copy number predicts extreme evolutionary rate variation in plant mitochondrial DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2317240121 | PMCID: PMC10927533 | PMID: 38427600
- Version used: **2.4.5**
- Evidence: Bowtie2 v.2.4.5 was used to align raw Illumina reads for each species to fasta files containing nuclear, mitochondrial, or plastid gene sequences for the same species ( 79 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.5, SAMtools] -> differential/statistical testing [R v4.2.2] -> visualisation [ggplot2] -> stage not stated [RAxML, SPAdes]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Version used: **2.3.4.1**
- Evidence: Rsem and Bowtie2 v2.3.4.1 were used to map the reads.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### Mutations of the circadian clock genes &lt;i&gt;Cry&lt;/i&gt;, &lt;i&gt;Per,&lt;/i&gt; or &lt;i&gt;Bmal1&lt;/i&gt; have different effects on the transcribed and nontranscribed strands of cycling genes. (PNAS 2024)

- DOI: 10.1073/pnas.2316731121 | PMCID: PMC10895256 | PMID: 38359290
- Evidence: Reads were aligned to the mm10 mouse genome using bowtie2 with command options bowtie2 -f –very-sensitive -x -u -s.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2] -> stage not stated [STRING db]

### COP1 controls light-dependent chromatin remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2312853121 | PMCID: PMC10895365 | PMID: 38349881
- Evidence: Sequencing reads were mapped to the Arabidopsis reference genome (TAIR10) with Bowtie2.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, deepTools] -> normalisation [deepTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [ImageJ, MACS2]

### Isolation, characterization, and circulation sphere of a filovirus in fruit bats. (PNAS 2024)

- DOI: 10.1073/pnas.2313789121 | PMCID: PMC10873641 | PMID: 38335257
- Version used: **2.4.1**
- Evidence: To check the quality of assembly, we mapped these reads back to the complete sequence using bowtie2 version 2.4.1 and calculated the sequencing coverage using samtools version 1.10.
- Full pipeline: quality control [SPAdes, fastp v0.20.0] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> quantification [ImageJ] -> visualisation [ImageJ, PyMOL v2.4.0] -> stage not stated [BLAST v0.9.35]

### High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310854121 | PMCID: PMC10823218 | PMID: 38241433
- Evidence: CPD-seq reads were aligned to the human reference genome using Bowtie 2 ( 47 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, Python] -> simulation/modelling [GROMACS, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [BEDTools, SAMtools]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: The resulting processed reads were aligned to the reference Mab ATCC 19977 genome (Genome accession: NC_010397 ) using Bowtie2 ( 56 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### The sleep-wake history contributes to rhythmic BMAL1 chromatin binding in the cerebral cortex but not in the liver. (PNAS 2025)

- DOI: 10.1073/pnas.2515047122 | PMCID: PMC12685114 | PMID: 41296730
- Evidence: The reads were aligned to the mouse genome assembly Dec 2011 (GRCm38/mm10) reference using bowtie2 ( 67 ).
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, MultiQC, edgeR] -> visualisation [MultiQC] -> stage not stated [R]

### Nanorate sequencing reveals the &lt;i&gt;Arabidopsis&lt;/i&gt; somatic mutation landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2514194122 | PMCID: PMC12685076 | PMID: 41296725
- Evidence: Reads were aligned to the TAIR10 reference genome using Bowtie2 with -X 800 ( 103 , 104 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2] -> stage not stated [MACS2, SAMtools, SciPy, Snakemake]

### A 120-y time series of genomes reveals the consequences of closed breeding in German Shepherd Dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421755122 | PMCID: PMC12684887 | PMID: 41284896
- Version used: **2.5.3**
- Evidence: Whole-genome sequences from both historical GSDs and medieval Lithuanian dogs were aligned to the UU_Cfam_GSD_1.0 (canFam4) reference genome ( 28 ) using bowtie2 v.2.5.3 with the --very-sensitive-local flag ( 52 , 53 ).
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.5.3, SAMtools v1.9] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.1.4, PLINK v1.90b]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **2.5.1**
- Evidence: Raw sequencing data were subjected to quality control using Trimmomatic (v.0.39) ( 49 ), and the reads were then sequentially mapped to the Escherichia coli reference with bowtie2 (v.2.5.1) ( 50 ).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **2.4.5**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Evidence: Read representation was also high, with Bowtie2 mapping rates averaging 96.71% ( SI Appendix , Table S1 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Sperm and offspring production in a nonobstructive azoospermia mouse model via testicular mRNA delivery using lipid nanoparticles. (PNAS 2025)

- DOI: 10.1073/pnas.2516573122 | PMCID: PMC12557808 | PMID: 41082659
- Version used: **2.3.5.1**
- Evidence: Sequencing reads were trimmed to remove adapter sequences using cutadapt (v3.2), and the resulting high-quality reads were aligned to the mouse reference genome (GRCm39) using bowtie2 (v2.3.5.1) with default parameters.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt v3.2] -> alignment/mapping [Bowtie2 v2.3.5.1, Cutadapt v3.2, SAMtools v1.20] -> stage not stated [deepTools]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: Cleaned reads were aligned to the mouse reference genome (mm10) using Bowtie2.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### The role of colony morphotype in shaping gene essentiality in &lt;i&gt;Mycobacteroides abscessus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500719122 | PMCID: PMC12519085 | PMID: 41026822
- Version used: **2.4.2**
- Evidence: This script selects for reads possessing the MycoMar Inverted Repeat (IR) (CAACCTGT) using Cutadapt v3.3, maps the reads to MAB ATCC 19977 (GCF_000069185.1) with Bowtie2 v2.4.2, and assigns each read to an insertion site.
- Full pipeline: stage not stated [Bowtie2 v2.4.2, Cutadapt v3.3, DESeq2 v1.18.1, R v3.4]

### How to upgrade stolen organelles into permanent plastids: A comparative transcriptomic perspective. (PNAS 2025)

- DOI: 10.1073/pnas.2514821122 | PMCID: PMC12519138 | PMID: 41026821
- Evidence: Read sufficiency using RSEM-based quantification and Bowtie2 mapping showed that more than 88.6% and 89.0% of ODP transcripts were detected with TPM >0.1 from D. capensis and D. kwazulunatalensis , respectively ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: The pipeline aligned the reads to the mouse mm10 genome using Bowtie2.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: Raw reads were trimmed using cutadapt-1.9.1 ( 44 ) and mapped to Arabidopsis thaliana TAIR10 reference genome using bowtie2 ( 50 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Loss of the ESX-5 secretion locus in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; reshapes the mycomembrane and enhances ESX-1 substrate secretion. (PNAS 2025)

- DOI: 10.1073/pnas.2509997122 | PMCID: PMC12435201 | PMID: 40901885
- Version used: **7.2.2**
- Evidence: Genomic DNA isolated from these mutants was sequenced using NextseqXplus (2x151bp PE) platform (Illumina), and the trimmed reads were mapped to the M.tb CDC1551 genome ( NC_002755.2 ) using Bowtie2 (v 7.2.2), and the deletions were verified.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Bowtie2 v7.2.2, FastQC v0.11.9] -> alignment/mapping [Bowtie2 v7.2.2] -> stage not stated [ImageJ]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: 0.26) ( 71 ) and these were aligned to the lined seahorse genome using Bowtie 2 ( 72 ).
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Fragmentation signatures in cancer patients resemble those of patients with vascular or autoimmune diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2426890122 | PMCID: PMC12402995 | PMID: 40833414
- Evidence: Trimmed sequences were then aligned to the hg19 genome with bowtie2 ( 86 ) using end-to-end alignment.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2, SAMtools] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy v1.13.1] -> stage not stated [Picard]

### Minimizing and quantifying uncertainty in AI-informed decisions: Applications in medicine. (PNAS 2025)

- DOI: 10.1073/pnas.2424203122 | PMCID: PMC12402999 | PMID: 40833408
- Evidence: Trimmed sequences were then aligned to the hg19 genome with bowtie2 using end-to-end alignment ( 81 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2] -> differential/statistical testing [scikit-learn] -> stage not stated [Picard, RepeatMasker, SAMtools]

### Cancer cells subvert the primate-specific KRAB zinc finger protein ZNF93 to control APOBEC3B. (PNAS 2025)

- DOI: 10.1073/pnas.2505021122 | PMCID: PMC12403153 | PMID: 40828019
- Evidence: Reads were aligned to the hg19 reference genome using bowtie2 ( 59 ).
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [Bioconductor, data.table, featureCounts, ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler, edgeR, limma] -> stage not stated [BEDTools v2.27.168, GSEA, R, deepTools]

### Measuring the selective packaging of RNA molecules by viral coat proteins in cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505190122 | PMCID: PMC12377776 | PMID: 40789029
- Version used: **2.4.5**
- Evidence: We used Bowtie2 (v2.4.5) ( 77 ) in local alignment mode (--local) to align up to one million reads per sample (-u 1,000,000) to the plasmid reference sequence, using default scoring settings for mismatches and gaps.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1] -> structure determination [PHENIX]

### Neuronal processes contain the essential components for the late steps of ribosome biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2502424122 | PMCID: PMC12337303 | PMID: 40743395
- Evidence: Reads were aligned using [bowtie2] ( https://github.com/BenLangmead/bowtie2 ), reducing the local alignment’s anchor size to 15.
- Full pipeline: quality control [DESeq2] -> read trimming [fastp] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: ATAC-seq reads were aligned to the mm10 reference genome using bowtie2 ( 59 ) in very sensitive mode.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### A population genetic analysis of the nematode &lt;i&gt;Strongyloides stercoralis&lt;/i&gt; in Asia shows that human infection is not a zoonosis from dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2424630122 | PMCID: PMC12304889 | PMID: 40663613
- Evidence: We mapped sequence reads to the S. stercoralis mitochondrial reference genome (NCBI Reference Sequence: NC 028624.1) using Bowtie2 and called and filtered SNPs as above.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, Bowtie2] -> stage not stated [ADMIXTURE]

### Complementary genetic and epigenetic changes facilitate rapid adaptation to multiple global change stressors. (PNAS 2025)

- DOI: 10.1073/pnas.2422782122 | PMCID: PMC12305003 | PMID: 40663607
- Version used: **2.2.6**
- Evidence: Mapping was conducted using Bismark v0.22.3 ( 64 ) and Bowtie2 v2.2.6 with local alignments ( 65 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bismark v0.22.3, Bowtie2 v2.2.6] -> differential/statistical testing [R v3.6.0, edgeR] -> stage not stated [BEDTools, DESeq2]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: High-quality clean data were aligned to the mouse reference genome (mm10) using Bowtie2.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### Decoding and engineering temperature-sensitive lethality in &lt;i&gt;Ceratitis capitata&lt;/i&gt; for pest control. (PNAS 2025)

- DOI: 10.1073/pnas.2503604122 | PMCID: PMC12280921 | PMID: 40623181
- Evidence: Trimmed reads were mapped to the C. capitata LysRS gene (NCBI Gene ID: LOC101451416) using the Bowtie2 plug-in ( 60 ) (Version 7.2.2 with default parameters: end-to-end alignment; high sensitivity).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BLAST v2.13.0, Bowtie2]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: Trimmed reads were mapped using Bowtie2 aligned to the human genome (hg19) ( 62 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Trimmed, paired-end reads were mapped to the zebrafish genome (GRCz11) using Bowtie2 ( 58 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Version used: **2.4.5**
- Evidence: The trimmed reads were then aligned to a reference built from the sgRNA sequences in the library using bowtie2(version 2.4.5) ( 33 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: Adaptor-trimmed reads were aligned to danRer11 by Bowtie2 ( 60 ) (Version 2.3.5.1).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Histone variant H2A.W7 represses meiotic crossover formation in &lt;i&gt;Arabidopsis&lt;/i&gt; heterochromatin. (PNAS 2025)

- DOI: 10.1073/pnas.2414166122 | PMCID: PMC12146724 | PMID: 40440068
- Evidence: Sequencing reads ( 47 ) were mapped to the TAIR10 Col genome assembly using Bowtie 2 and crossover positions were identified using the TIGER pipeline as described ( 26 , 48 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [CellProfiler]

### BRD9 functions as an HIV-1 latency regulatory factor. (PNAS 2025)

- DOI: 10.1073/pnas.2418467122 | PMCID: PMC12130862 | PMID: 40402245
- Evidence: The RNA sequencing data underwent quality control by FastQC, followed by reads filtering, reads alignment, and mapping onto human reference genome using the Bowtie2 program.
- Full pipeline: quality control [Bowtie2, FastQC] -> alignment/mapping [Bowtie2, FastQC] -> stage not stated [GSEA]

### RNA sequencing analysis of viromes of &lt;i&gt;Aedes albopictus&lt;/i&gt; and &lt;i&gt;Aedes vexans&lt;/i&gt; collected from NEON sites. (PNAS 2025)

- DOI: 10.1073/pnas.2403591122 | PMCID: PMC12107137 | PMID: 40354533
- Evidence: A custom Bowtie 2 database ( 36 ) was constructed using core genes and genomes from those organisms detected during the initial survey step.
- Full pipeline: read trimming [BWA, fastp v0.21.1] -> alignment/mapping [BLAST, BWA, Kraken2, SAMtools] -> stage not stated [Bowtie2, R]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Evidence: The NextFlow ATAC-seq pipeline v2.1.2 ( 80 ) was employed with the Bowtie2 aligner and the GRCh38 human genome reference.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Version used: **2.2.7**
- Evidence: ChIP-Seq read alignment as performed using Bowtie2 v2.2.7 ( 79 ) on human genome sequence (assembly hg38) with options --local and alignment files sorted and converted to bam using samtools v1.3 ( 80 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: Sequence reads were trimmed with Trimomatic and aligned to the human genome reference hg19 using bowtie2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### Colony pattern multistability emerges from a bistable switch. (PNAS 2025)

- DOI: 10.1073/pnas.2424112122 | PMCID: PMC12002352 | PMID: 40184178
- Version used: **2.4.1**
- Evidence: Next, the sequencing data were aligned to reference sequences using Bowtie2 (v2.4.1) ( 56 ).
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9] -> quantification [SAMtools v1.9] -> machine learning [Cellpose] -> stage not stated [ImageJ v1.53c]

### Nuclear Galectin-1 promotes &lt;i&gt;KRAS&lt;/i&gt;-dependent activation of pancreatic cancer stellate cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424051122 | PMCID: PMC12002210 | PMID: 40172967
- Evidence: Selected reads were aligned to the human reference genome (Homo sapiens b38, hg38) using Bowtie2.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2]

### Pulsatile flow induces chromatin interaction with lamin-associated proteins to enrich H3K9 methylation in endothelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424566122 | PMCID: PMC11962468 | PMID: 40117319
- Evidence: Reads were aligned to the Homo sapiens genome build hg19 using bowtie2.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [HOMER, ImageJ, MACS2, OpenCV]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Version used: **2.3.5.1**
- Evidence: Reads were aligned to the GRCz11 genome with bowtie2 (version 2.3.5.1).
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **2.2.5**
- Evidence: Clean metagenomic reads were mapped to MAGs using Bowtie2 v2.2.5 ( 66 ).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **2.3.5.1**
- Evidence: Paired-end ChIP-seq reads were aligned to the TAIR10 reference genome using Bowtie2 (version 2.3.5.1) ( 80 ) in local-alignment mode.
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Version used: **2.4.2**
- Evidence: Reads were aligned to the D. melanogaster reference genome dm6 using Bowtie 2 (v 2.4.2) ( 49 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Version used: **2.3.5**
- Evidence: Adapter sequences were trimmed from reads with cutadapt (v2.3) and aligned to the GENCODE Release M31 mouse assembly with bowtie2 (v2.3.5; --very-sensitive, paired-end mode).
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### Structural variant and nucleosome occupancy dynamics postchemotherapy in a HER2+ breast cancer organoid model. (PNAS 2025)

- DOI: 10.1073/pnas.2415475122 | PMCID: PMC11892646 | PMID: 39993200
- Evidence: The ATAC-seq data were first aligned to the mm10 reference genome using bowtie2 ( 54 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [BEDTools, MACS2]

### The genomic and epigenomic landscapes of hemizygous genes across crops with contrasting reproductive systems. (PNAS 2025)

- DOI: 10.1073/pnas.2422487122 | PMCID: PMC11831139 | PMID: 39918952
- Version used: **2.1.0**
- Evidence: Trimmed reads were aligned to reference genomes using Bismark (v0.23.1) ( 81 ) with bowtie2 (v2.1.0) ( 82 ), and methylation status was determined using the bismark_methylation_extractor (minimum coverage = 2).
- Full pipeline: read trimming [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.1, Bowtie2 v2.1.0, HISAT2 v2.2.1, Trimmomatic v0.39, minimap2 v2.24] -> variant calling [BUSCO] -> quantification [featureCounts v2.0.1] -> normalisation [featureCounts v2.0.1] -> visualisation [deepTools] -> stage not stated [BEDTools, OrthoFinder, RepeatMasker]

### tRNA selectivity during ribosome-associated quality control regulates the critical sterility-inducing temperature in two-line hybrid rice. (PNAS 2025)

- DOI: 10.1073/pnas.2417526122 | PMCID: PMC11831146 | PMID: 39913205
- Version used: **2.2.9**
- Evidence: Bowtie2 (2.2.9) ( 57 ) was utilized for these alignments with default settings.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.2.9, Clustal Omega] -> structure determination [Cutadapt v1.18] -> stage not stated [ImageJ, RoseTTAFold]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Reads were aligned to the hg38 genome with bowtie2 ( 54 ) (version 2.4.5) with the options –local –very-sensitive-local –no-unal –no-mixed -no-discordant –phred33 –dovetail -I 0 -X 500.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### Genome-wide CG hypomethylation of the &lt;i&gt;Arabidopsis&lt;/i&gt; ecotype Cvi linked to structural variation and RNAi at the &lt;i&gt;VIM4&lt;/i&gt;-&lt;i&gt;VIM2&lt;/i&gt; locus. (PNAS 2026)

- DOI: 10.1073/pnas.2603682123 | PMCID: PMC13213937 | PMID: 42154559
- Version used: **2.4.2**
- Evidence: The trimmed reads were aligned to VIM2 , VIM3 , and VIM4 genomic sequences—comprising the first exon and 500-bp upstream regions—extracted from the TAIR10 (Col) or Cvi2.0 genomes, using Bowtie2 (v2.4.2, --end-to-end --norc ) ( 34 ).
- Full pipeline: read trimming [Bowtie2 v2.4.2, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [MACS2]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Version used: **2.3.4.1**
- Evidence: Reads were then aligned to the Illumina prebuilt hg38 human reference genome using Bowtie2 (version 2.3.4.1) ( 52 , 53 ).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Versatile SMAD2 and SMAD3 epitope-tagged mouse models for genomic profiling of TGFβ signaling: Uncovering GDF9-SMAD2/3 targets. (PNAS 2026)

- DOI: 10.1073/pnas.2600071123 | PMCID: PMC13056123 | PMID: 41911462
- Evidence: In short, after demultiplexing and quality control, clean reads were mapped to the mouse genome mm10 and the E. coli genome U00096.3 (for Spike-in) by Bowtie2.
- Full pipeline: quality control [Bowtie2] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2, STAR v2.7.11b, featureCounts v2.1.1] -> quantification [STAR v2.7.11b] -> stage not stated [DESeq2 v1.48.2, HOMER v4.11, deepTools v2.4.2]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Version used: **2.3.5.1**
- Evidence: Reads were aligned to the S. cerevisiae genome (sacCer3, Release 64) using bowtie2 version 2.3.5.1 with default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Version used: **2.4.5**
- Evidence: Clean reads were aligned to the UCSC hg19 reference genome using Bowtie2 v2.4.5 ( 51 ).
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **2.3.2**
- Evidence: Quality-filtered nonoyster reads were then mapped to the ORFs using Bowtie2 v.2.3.2 ( 74 ) in very sensitive local mode to estimate abundance.
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### Foliar dewdroplet-induced redox cascades promote early flowering in &lt;i&gt;Brassicaceae&lt;/i&gt; plants. (PNAS 2026)

- DOI: 10.1073/pnas.2527021123 | PMCID: PMC12933091 | PMID: 41701847
- Evidence: Data were processed using FastQC, Bowtie2, MACS2, and DESeq2.
- Full pipeline: quality control [Bowtie2, DESeq2, FastQC, MACS2] -> stage not stated [WGCNA]

### EPOP and MTF2 activate PRC2 activity through DNA-sequence specificity. (PNAS 2026)

- DOI: 10.1073/pnas.2527303123 | PMCID: PMC12890814 | PMID: 41650228
- Evidence: Briefly, reads were aligned to the mouse reference genome mm10 and dm6 for spike-in samples, using Bowtie2 with default parameters.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [BEDTools, deepTools] -> normalisation [BEDTools, deepTools] -> visualisation [BEDTools, deepTools] -> stage not stated [ImageJ, MACS2, SAMtools]

### INDETERMINATE DOMAIN-DELLA protein interactions orchestrate gibberellin-mediated cell elongation in wheat and barley. (PNAS 2026)

- DOI: 10.1073/pnas.2528934123 | PMCID: PMC12867750 | PMID: 41615756
- Evidence: Reads were aligned to IDD5 gene models using Bowtie 2, and the proportion of correctly versus incorrectly spliced reads was calculated from read pileups ( SI Appendix , Fig.
- Full pipeline: read trimming [Trimmomatic v0.39, kallisto] -> alignment/mapping [Bowtie2, Trimmomatic v0.39, kallisto] -> quantification [Trimmomatic v0.39, kallisto] -> stage not stated [BLAST, ImageJ v1.48v]

### A bacterial translation activator with an intrinsically disordered RNA-binding region. (PNAS 2026)

- DOI: 10.1073/pnas.2519770123 | PMCID: PMC12818456 | PMID: 41543904
- Evidence: To assess the relative abundance of RNAs copurifying with PhaF in our CLIP/CLAP-seq experiment or to assess the relative abundance of RNAs obtained from total RNA samples, the libraries were mapped to the PAO1 genome using bowtie2, counted with htseq-count ( 61 ), and analyzed with DESeq2 in R ( 62 ). β-Galactosidase Assays.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, HTSeq, R] -> quantification [Bowtie2, DESeq2, HTSeq, R] -> stage not stated [Cutadapt v2.10]

### Host-microbiome mutualism drives urea carbon salvage and acetogenesis during hibernation. (PNAS 2026)

- DOI: 10.1073/pnas.2518978123 | PMCID: PMC12773770 | PMID: 41481471
- Version used: **2.2.2**
- Evidence: Trimmomatic v0.38 ( 9 ) was used to remove sequencing adapters and low-quality reads, while host DNA was filtered using bowtie2 v2.2.2 ( 10 ) against the 13-lined ground squirrel genome (GenBank and RefSeq assembly accession = GCA_000236235.1).
- Full pipeline: read trimming [Bowtie2 v2.2.2, Trimmomatic v0.38] -> normalisation [DESeq2, R] -> differential/statistical testing [R] -> stage not stated [HMMER]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: Sequencing reads from ChIP DNA and Input DNA were aligned to the Araport11 genome using Bowtie2 ( 75 ), and duplicate reads were removed.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **2.4.1**
- Evidence: Sequence analysis used Bowtie2 (2.4.1) ( 85 ), bcftools and samtools (1.9) ( 86 , 87 ), Geneious Prime (2021.0.3) ( 88 ), ivar (1.2.2) ( 89 ), and MAFFT (4.475) ( 90 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Evidence: Trimmed reads were mapped to the SARS-CoV-2 RefSeq genome of isolate Wuhan-Hu-1 ( NC_045512.2 ) using shiver ( 57 ) version 1.5.7, with either smalt ( 58 ) or bowtie2 ( 59 ) as the mapper.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Evidence: For the alignment, the SARS-CoV-2 spike RBD reference was indexed using bowtie2-build (Version 2.4.1) and samtools (Version 1.10).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Version used: **2.2.5**
- Evidence: Traces of ribosomal DNA and mitochondrial DNA were removed using the Bowtie2 (v2.2.5) ( 74 ).
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### Transcripts of repetitive DNA elements signal to block phagocytosis of hematopoietic stem cells. (Science 2024)

- DOI: 10.1126/science.adn1629 | PMCID: PMC12012832 | PMID: 39264994
- Evidence: Mutagenesis analysis For the analysis the sequencing reads were first trimmed for quality and aligned to the GRCz11/danRer11 assembly using Bowtie2 ( 87 ) with the --very-sensitive setting.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [CellProfiler, Metascape, R]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **2.4.5**
- Evidence: ChIP-Seq analysis Input and H2A.Z and acetyl-H2A.Z (H2A.Zac) ChIP-seq raw reads were quality-checked with FastQC (v0.11.7) ( 110 ) and aligned onto the human genome (hg38 assembly) using Bowtie2 (v2.4.5) ( 111 ) with the following options:–local –very-sensitive-local –no-unal –no-mixed –no-discordant –phred33 -I 10 -X 700.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Version used: **1.2.3**
- Evidence: Analysis of CRISPR screen results 20 nt sgRNA sequences were trimmed from backbone sequences using Cutadapt (version 1.4.1) (5’ GACGAAACACCG, 3’ GTTTTAGAGCTA). sgRNA sequences were aligned to reference sgRNA libraries using Bowtie2 (version 1.2.3). sgRNAs with counts less than 20 (genome-wide screens) or 50 (all other screens) in either of the populations were excluded from the analysis.
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Metagenomic editing of commensal bacteria in vivo using CRISPR-associated transposases. (Science 2025)

- DOI: 10.1126/science.adx7604 | PMCID: PMC12969935 | PMID: 41231980
- Evidence: Specifically, the Bowtie2 alignment tool ( 84 ) was used to evaluate each spacer candidate for potential genome-wide off-targets.
- Full pipeline: alignment/mapping [BLAST, Bowtie2, ggplot2] -> quantification [ggplot2] -> normalisation [ggplot2, seaborn] -> visualisation [ggplot2, seaborn] -> stage not stated [Python]

### Precise targeting of HIV broadly neutralizing antibody precursors in humans. (Science 2025)

- DOI: 10.1126/science.adv5572 | PMCID: PMC12313413 | PMID: 40373114
- Evidence: These germline allele sequences formed the basis of alignment indices for Bowtie2 and IgBLAST ( 84 , 85 ), which were used to filter reads for relevance and to rank assembled chain transcript candidates for each cell.
- Full pipeline: alignment/mapping [Bowtie2] -> structure determination [Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, Nextflow, R, RELION v4.0, Trinity]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: Adapters were trimmed using CutAdapt and mapped to loci of interest using Bowtie2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Demultiplexed reads were trimmed for adapters using Skewer and aligned to the mm10 genome (GENCODE v.30) using Bowtie2.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

