# GATK

- **Category:** genomics
- **Papers in survey:** 312
- **Journals:** PNAS (163), Nature (122), Cell (18), Science (9)
- **Years:** 2021 (41), 2022 (59), 2023 (61), 2024 (50), 2025 (68), 2026 (33)
- **Versions named:** 3.7 (12), 3.8 (10), 4.1.4.1 (8), 3.5 (6), 3.6 (5), 4.1.9.0 (5), 4.1 (4), 4.1.2.0 (4), 4.0 (3), 3.0 (3)
- **Pipeline stages it appears in:** variant calling (128), alignment/mapping (97), registration (40), quality control (7), read trimming (7), dimensionality reduction/clustering (2), visualisation (1), machine learning (1), differential/statistical testing (1), quantification (1), structure determination (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: Alignments were further refined, and variants were called using GATK Best Practices tools ( Van der Auwera et al., 2013 ), including mark duplicates with Picard, base quality-score recalibration, and variant calling with HaplotypeCaller and GenotypeGVCFs ( Poplin et al., 2017 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Microenvironment drives cell state, plasticity, and drug response in pancreatic cancer. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.017 | PMCID: PMC8822455 | PMID: 34890551
- Version used: **1.6**
- Evidence: Sequence reads were aligned to reference sequence b37 edition from the Human Genome Reference Consortium using bwa, and further processed using Picard (version 1.90, http://broadinstitute.github.io/picard/ ) to remove duplicates and Genome Analysis Toolkit (GATK, version 1.6-5-g557da77) to perform localized realignment around indel sites.
- Full pipeline: quality control [RSEM] -> alignment/mapping [GATK v1.6] -> registration [GATK v1.6] -> differential/statistical testing [R v4.0] -> stage not stated [Mutect2 v1.1.45, Picard, Python v3.7.4, Seurat v2.3.4]

### The genomic history of the Middle East. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.013 | PMCID: PMC8445022 | PMID: 34352227
- Version used: **3.7**
- Evidence: ...00001000238, EGAS00001000237 Middle Eastern sequencing populations data This study ENA:ERP110713 Software and algorithms Long Ranger pipeline v2.2.2 (GATK v3.7) 10x Genomics https://support.10xgenomics.com/genome-exome/software/downloads/latest GraphTyper v2.0 Eggertsson et al., 2017 https://github.com/DecodeGenetics/graphtyper plink v1.9 Chang et al., 2015 https://www.cog-genomics.org/plink/ covs...
- Full pipeline: stage not stated [ADMIXTURE, BCFtools v1.9, GATK v3.7, RAxML v8.2.10, SAMtools]

### The monoclonal antibody combination REGEN-COV protects against SARS-CoV-2 mutational escape in preclinical and human studies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.002 | PMCID: PMC8179113 | PMID: 34161776
- Evidence: ...tbiosciences/primerclip Picard package Broad Institute https://github.com/broadinstitute/picard samtools (v1.9) Li et al., 2009 http://www.htslib.org GATK HaplotypeCaller (v4.1.8) Broad Insitute https://gatk.broadinstitute.org/hc/en-us/articles/360036194592-Getting-started-with-GATK4 Resource availability Lead contact Further information and requests for resources and reagents should be directed t...
- Full pipeline: variant calling [GATK, Picard, SAMtools v1.9] -> stage not stated [PHENIX v1.19.1, PyMOL, minimap2]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Version used: **3.7**
- Evidence: ....13.2 Hannon lab 2010 http://hannonlab.cshl.edu/fastx_toolkit FigTree v1.4.4 Andrew Rambaut https://groups.google.com/g/figtree-discuss/c/-9_1l88HPOA GATK v3.7 DePristo et al., 2011 https://gatk.broadinstitute.org GenotypeGVCFs Poplin et al., 2017 https://gatk.broadinstitute.org/hc/en-us/articles/360046224151-GenotypeGVCFs GLIMPSE v1.0.1 Rubinacci et al., 2021 https://github.com/odelaneau/GLIMPSE ...
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Evidence: PCR duplicates were marked with samblaster (version 0.1.25) ( Faust and Hall, 2014 ), and GATK base quality score recalibration was completed on the aligned BAM files (gatk version 3.8) ( DePristo et al., 2011 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ....html VCFtools Danecek et al., 2011 http://vcftools.sourceforge.net/ HaploGrep2 Weissensteiner et al., 2016 https://github.com/seppinho/haplogrep-cmd GATK McKenna et al., 2010 https://gatk.broadinstitute.org/hc/en-us BEAST Bouckaert et al., 2019 http://beast.community/ Tracer Rambaut et al., 2018 http://tree.bio.ed.ac.uk/software/tracer/ FigTree http://tree.bio.ed.ac.uk/software/figtree/ http://tr...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: Raw paired-end reads in FASTQ format were aligned to hg19 obtained from the GATK bundle (v2.8) using bwa mem (bwa v0.7.15) ( Li and Durbin, 2009 ; McKenna et al., 2010 ).
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Version used: **4.1.4.1**
- Evidence: Duplicates were removed using the ‘MarkDuplicates’ command from GATK (version 4.1.4.1; --VALIDATION_STRINGENCY=LENIENT --REMOVE_DUPLICATES=true) ( McKenna et al., 2010 ).
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Evidence: ..._2504_high_coverage/ GVCFs This paper IGSR: http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20190425_NYGC_GATK/raw_calls_updated/ SNV/INDEL VCFs This paper EMBL-EBI: PRJEB55077 SNV/INDEL VCFs This paper dbSNP: https://www.ncbi.nlm.nih.gov/SNP/snp_viewTable.cgi?handle=1000G_HIGH_COVERAGE (dbSNP: 1000G_HIGH_COVERAGE) SNV/INDEL VCFs This paper IGSR: http://...
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...2021 ) http://cmpg.unibe.ch/software/fastsimcoal2/ fastqc - version 0.11.5 Babraham Bioinformatics www.bioinformatics.babraham.ac.uk/projects/fastqc/ GATK - version 3.7 ( DePristo et al., 2011 ) https://gatk.broadinstitute.org HIrisPlex-S webtool ( Chaitanya et al., 2018 ; Walsh et al., 2013 ) https://hirisplex.erasmusmc.nl/ IBDSeq v. r1206 ( Browning and Browning, 2013 ) http://faculty.washington...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Ancient genomes reveal origin and rapid trans-Eurasian migration of 7<sup>th</sup> century Avar elites. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.007 | PMCID: PMC9042794 | PMID: 35366416
- Version used: **3.5**
- Evidence: ...et al., 2009 http://www.htslib.org/doc/samtools.html pileupCaller https://github.com/stschiff/sequenceTools https://github.com/stschiff/sequenceTools GATK v3.5 DePristo et al., 2011 https://gatk.broadinstitute.org/hc/en-us GeneImp 1.4 Spiliopoulou et al., 2017 https://pm2.phs.ed.ac.uk/geneimp/ SHAPEIT v2.r790 Delaneau et al., 2013 https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.ht...
- Full pipeline: read trimming [BWA v0.7.12] -> stage not stated [ANGSD v0.910, GATK v3.5, PLINK v1.9, R v4.0, SAMtools v1.3, SHAPEIT]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ... https://bioconductor.org/packages/release/bioc/html/fgsea.html FlowJo BD Biosciences v10.6 https://www.flowjo.com Fragpipe ( Yu et al., 2021 ) v13.0 GATK variant calling ( Van der Auwera and O’Connor, 2020 ) v4.1.7.0 ggraph Pedersen v2.05 https://github.com/thomasp85/ggraph gsfisher ( Croft et al., 2019 ) https://github.com/sansomlab/gsfisher Harmony ( Korsunsky et al., 2019 ) https://github.com/...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: Variant calling was then performed on the aligned reads, with GATK-3.4-46 best practices 97 .
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: Ascertainment of CHIP carriage status in ARIC CHIP was previously determined using whole exome sequencing data using GATK Mutect2 118 and ANNOVAR 119 as reported by Bick et al.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Version used: **3.6**
- Evidence: GATK’s Haplotype Caller from the Genome Analysis Toolkit (GATK version 3.6) 104 SAMtools 105 , and Picard tools were used for variant calling.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **4.1.7**
- Evidence: 120 https://pcingola.github.io/SnpEff/ / SLiM 4.0.1 Haller and Messer 121 https://messerlab.org/slim/ GATK v.4.1.7 McKenna et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Global genetic interaction network of a human cell maps conserved principles and informs functional interpretation of gene co-essentiality profiles. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.044 | PMCID: PMC13281610 | PMID: 42049019
- Evidence: The sequencing data is summarized as follows: Type Platform Depth # of reads mean_length mean_insert_size Illumina HiSeq 145× 1453105919 pair-end reads 150bp 291bp To call variants, we applied the GATK-recommended variant calling workflow 148 with the ploidy parameter for HaplotypeCaller set to 1.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, STAR] -> variant calling [GATK] -> visualisation [Cytoscape] -> stage not stated [ANNOVAR, R, SciPy]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: SNP calling was performed using GATK 32 v.3.7 as per GATK best practices for SNP calling, thus creating the base SNP set.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Version used: **3.8**
- Evidence: In brief, variants from whole-genome sequencing data were called using four independent callers: GATK v3.8, FreeBayes, Strelka, and Platypus.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### Evolutionary and biomedical insights from a marmoset diploid genome assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03535-x | PMCID: PMC8189906 | PMID: 33910227
- Evidence: ... sites from the Mummer alignment between the maternal and paternal haplotypes excluding the sex chromosomes (setA, containing 3.48 million SNVs); (2) GATK pipeline based on mapping of 10X linked-reads from the F 1 offspring (setB); and (3) SAMTools (v.1.8) mpileup followed by bcftools also based on 10X linked-reads mapping (setC).
- Full pipeline: alignment/mapping [BCFtools, BWA, GATK, freebayes v1.3.1, minimap2] -> variant calling [GATK, freebayes v1.3.1]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **4.1.3**
- Evidence: Duplicates were marked with Picard tools (v2.20.4) 48 BAM files were recalibrated for base quality scores using Genome Analysis Toolkit (GATK v4.1.3) 49 Base Recalibrator.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. (Nature 2021)

- DOI: 10.1038/s41586-021-03205-y | PMCID: PMC7875770 | PMID: 33568819
- Version used: **3.5.0**
- Evidence: Genetic variants were jointly called using the GATK v.3.5.0 pipeline across all 31,250 BioMe samples with WES data.
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> stage not stated [BWA, Docker, GATK v3.5.0, R, SAMtools, VEP]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: First, we corrected homozygous SNPs and insertions and/or deletions (indels) by aligning the Illumina 2 × 150 bp library to the release consensus sequence using bwa mem 55 and identifying homozygous SNPs and indels with the UnifiedGenotyper tool of GATK 56 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Evidence: Duplicates were removed using sambamba 56 and GATK was applied 57 .
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Effect of the intratumoral microbiota on spatial and cellular heterogeneity in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05435-0 | PMCID: PMC9684076 | PMID: 36385528
- Evidence: The unmapped reads are then aligned against microbial databases through GATK PathSeq to identify the microbiome composition. h , Distribution of the bacterial UMI count and bacterial reads for top bacterial genera detected in 10x Visium data from the OSCC and CRC cases as it is indicated.
- Full pipeline: alignment/mapping [GATK, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: Following the GATK best practices and the associated set of tools v4.1.4.1 (refs.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### African-specific molecular taxonomy of prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05154-6 | PMCID: PMC9477733 | PMID: 36045292
- Version used: **4.1.2.0**
- Evidence: The Genome Analysis Toolkit (GATK, v.4.1.2.0) was used for base quality recalibration 38 .
- Full pipeline: stage not stated [GATK v4.1.2.0]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: DNA sequence data were processed with Sarek, following the GATK best-practice recommendations 39 , on UPPMAX Clusters at Uppsala University ( https://www.uppmax.uu.se/resources/systems/the-bianca-cluster/ ).
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: SNP and indel calling with GATK is given in Supplementary Note 5 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Evidence: ...ked for duplicates using Picard Tools (v2.21.4) ( http://broadinstitute.github.io/picard ), genotyped at the sites present in the above dataset using GATK HaplotypeCaller (v3.6) 71 with the ‘-gt_mode GENOTYPE_GIVEN_ALLELES’ argument and then merged into the dataset using bcftools merge ( http://www.htslib.org/ ).
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Evidence: SNP calling, heterozygosity estimates and SNP filtering Variant calling was carried out for BSK001 and BSK003, both before and after MALT 62 filtering using the UnifiedGenotyper in the Genome Analysis Toolkit (GATK) v.3.5 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Island-specific evolution of a sex-primed autosome in a sexual planarian. (Nature 2022)

- DOI: 10.1038/s41586-022-04757-3 | PMCID: PMC9177419 | PMID: 35650439
- Version used: **4.1.4.1**
- Evidence: Genetic variants were jointly called by using the Genome Analysis Toolkit (GATK, version 4.1.4.1) with GenomicsDB and GenotypeGVCFs 50 .
- Full pipeline: variant calling [GATK v4.1.4.1] -> quantification [kallisto v0.44.0] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [ImageJ, RAxML v0.9.0, VCFtools v0.1.14]

### Omicron infection enhances Delta antibody immunity in vaccinated persons. (Nature 2022)

- DOI: 10.1038/s41586-022-04830-x | PMCID: PMC9279144 | PMID: 35523247
- Evidence: For Illumina assembly, the GATK HaploTypeCaller –min-pruning 0 argument was added to increase mutation calling sensitivity near sequencing gaps.
- Full pipeline: variant calling [GATK]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **4.2**
- Evidence: Finally, we used a total of 22 genomes to call SNPs in the porcine ABO gene using GATK (v.4.2) 81 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Evidence: Linkage disequilibrium analysis Recalibrated VCF files of 297 ALS patients of European descent generated by GATK HaplotypeCallers were downloaded from Answer ALS in July 2020 ( https://www.answerals.org ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: In brief, paired-end 150-bp reads were aligned to the GRCh38 human reference using the Burrows-Wheeler Aligner (BWA-MEM v0.7.15) 64 and processed using the GATK best-practices workflow.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **3.6**
- Evidence: To select high-quality indel variants, GATK (v.3.6-0) Haplotype Caller (without base quality score recalibration) 63 variant calling was performed with ‘Hard Filters’ (--filterExpression “QD < 2.0 || FS > 200.0 || ReadPosRankSum < −20.0”) .
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Evidence: Duplicate reads were then removed by GATK’s (v.4.1.1) MarkDuplicates tool.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Evidence: Variants were identified with GATK HaplotypeCaller 12 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: For Illumina assembly, the GATK HaploTypeCaller --min-pruning 0 argument was added to increase mutation calling sensitivity near sequencing gaps.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### Emergence of methicillin resistance predates the clinical use of antibiotics. (Nature 2022)

- DOI: 10.1038/s41586-021-04265-w | PMCID: PMC8810379 | PMID: 34987223
- Evidence: ...e genome of mecC -MRSA CC425 isolate LGA251 (GenBank: NC_017349 ) with the Burrows–Wheeler Alignment tool 55 ; (2) SNP calling was achieved using the GATK Unified Genotyper 56 , 57 , setting depth of coverage and unambiguously base calls to ≥10× and ≥90%, respectively, and ignoring insertions and deletions; and (3) SNPs contained in repeats were excluded using NUCmer 58 , 59 .
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> simulation/modelling [R] -> stage not stated [SPAdes v3.15]

### Malaria protection due to sickle haemoglobin depends on parasite genotype. (Nature 2022)

- DOI: 10.1038/s41586-021-04288-3 | PMCID: PMC8810385 | PMID: 34883497
- Evidence: P. falciparum genotypes were called using an established pipeline 11 based on GATK, which calls single nucleotide polymorphisms and short insertion–deletion variants relative to the Pf3D7 reference sequence.
- Full pipeline: alignment/mapping [MAFFT, STAR v2.7.3a, minimap2] -> variant calling [GATK] -> stage not stated [Stan]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Local realignment around insertions and deletions was performed using the Genome Analysis Toolkit (GATK) 51 programs RealignerTargetCreator and IndelRealigner.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Version used: **3.8**
- Evidence: Mitochondrial genetic structure and diversity Mitochondrial variants were called with GATK (v.3.8-0) 78 ‘HaplotypeCaller’ with ploidy set to haploid and validated via several metrics including maternal parent–offspring genotype concordance (Supplementary Note 7 ).
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### Organ aging signatures in the plasma proteome track health and disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06802-1 | PMCID: PMC10700136 | PMID: 38057571
- Evidence: The Genome Analysis Toolkit workflow Germline short variant discovery was used to map genome sequencing data to the reference genome (GRCh38) and to produce high-confidence variant calls using joint-calling 77 .
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> normalisation [DESeq2, SPM] -> registration [SPM] -> differential/statistical testing [statsmodels] -> stage not stated [FreeSurfer, Python, R, STRING db, metafor, scikit-learn]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **4.1.2.0**
- Evidence: Tumour-only somatic mutation calling using bulk data For samples for which paired normal samples were not available, tumour-only somatic variants were called using the Mutect2 (tool from GATK v.4.1.2.0) tumour-only version of the Somaticwrapper pipeline ( https://github.com/ding-lab/somaticwrapper/tree/tonly.v1.0 ) with the GDC panel of normal data ( https://gdc.cancer.gov/about-data/gdc-data-proc...
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Genotyping, sequencing and analysis of 140,000 adults from Mexico City. (Nature 2023)

- DOI: 10.1038/s41586-023-06595-3 | PMCID: PMC10600010 | PMID: 37821707
- Evidence: This set was additionally restricted to 1000 genomes phase 1 high-confidence SNPs from the 1000 Genomes project 36 and gold-standard insertions and deletions from the 1000 Genomes project and a previous study 37 , both available through the GATK resource bundle ( https://gatk.broadinstitute.org/hc/en-us/articles/360035890811-Resource-bundle ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [REGENIE] -> stage not stated [BCFtools, DeepVariant v0.10.0, GATK, WhatsHap]

### Rare variant associations with plasma protein levels in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06547-x | PMCID: PMC10567546 | PMID: 37794183
- Evidence: Detecting CH somatic mutations To detect putative CH somatic variants, we used the same GRCh38 genome reference aligned reads as for germline variant calling, and ran somatic variant calling with GATK’s Mutect2 (v.4.2.2.0) 67 .
- Full pipeline: alignment/mapping [GATK, Mutect2 v4.2.2.0] -> variant calling [GATK, Mutect2 v4.2.2.0] -> differential/statistical testing [R] -> stage not stated [SnpEff, data.table v1.12.8, tidyverse v1.1.0]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Evidence: BamQC (v1.0.0, https://github.com/DecodeGenetics/BamQC ), GraphTyper (v2.7.1, v1.4, v2.7.2, https://github.com/DecodeGenetics/graphtyper ), GATK resource bundle (v4.0.12, gs://genomics-public-data/resources/broad/hg38/v0), Svimmer (v0.1, https://github.com/DecodeGenetics/svimmer ), popSTR (v2.0, https://github.com/DecodeGenetics/popSTR ), Admixture (v1.3.0, https://dalexander.github.io/admixture )...
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Version used: **4.2.6.0**
- Evidence: Initial variant calls in the mtDNA and reference NUMT regions are made from mapped WGS data using Mutect2 and HaplotypeCaller, respectively (using GATK v.4.2.6.0), and haplogroup inference is performed using Haplogrep 52 .
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Long-molecule scars of backup DNA repair in BRCA1- and BRCA2-deficient cancers. (Nature 2023)

- DOI: 10.1038/s41586-023-06461-2 | PMCID: PMC10482687 | PMID: 37587346
- Evidence: HMF provided the following for cases in their dataset: germline SNVs and indels (through GATK HaplotypeCaller), somatic SNVs and indels (through Strelka1 and annotated by SnpEff).
- Full pipeline: alignment/mapping [BWA, Picard] -> variant calling [GATK] -> registration [Picard] -> stage not stated [R, SnpEff]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Evidence: Haplotype phasing and imputation After merging genotypes from AFB, EUB and ASH donors, we filtered genotypes for duplicates with bcftools norm --rm-dup all (v.1.16) 58 and lifted all genotypes over to the human genome assembly GRCh38 with GATK’s (v.4.1.2.0) LiftoverVcf using the RECOVER_SWAPPED_ALT_REF=TRUE option 59 .
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Evidence: Variants (SNPs and small indels) were called using the GATK’s HaplotypeCaller following best practices in an identical manner as was used in the 1000 Genomes Project.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: HaplotypeCaller from GATK 107 (v.4.1.8.0) was used to identify variants and generate individual-specific .gvcf files followed by a joint calling of variants performed by GenotypeGVCFs.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Evidence: 46 ) and pre-processing and quality control were performed according to GATK Best Practice Workflows 12 .
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Version used: **4.3.0**
- Evidence: We performed base quality score recalibration (BQSR) using GATK (v4.3.0) 49 .
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Version used: **4.1.4.1**
- Evidence: Duplicates were removed using the ‘MarkDuplicates’ command from GATK (version 4.1.4.1) and default parameters.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Version used: **4.1.9.0**
- Evidence: For post-alignment processing, we followed the best practice of GATK ( https://gatk.broadinstitute.org/hc/en-us/articles/360035531192-RNAseq-short-variant-discovery-SNPs-Indels- ), which included adding read group information and executing SplitNCigarReads (both using GATK v.4.1.9.0).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### Northwest African Neolithic initiated by migrants from Iberia and Levant. (Nature 2023)

- DOI: 10.1038/s41586-023-06166-6 | PMCID: PMC10266975 | PMID: 37286608
- Version used: **3.5.0**
- Evidence: Before genotype calling, base quality in read ends was reduced and indel realignment conducted with GATK 3.5.0.
- Full pipeline: variant calling [GATK v3.5.0] -> registration [GATK v3.5.0] -> dimensionality reduction/clustering [ADMIXTURE, QGIS] -> stage not stated [BCFtools, PLINK v1.9, SAMtools]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: The resulting BAM files were further analysed and recalibrated with Picard (v.2.5.0) 51 and the GATK toolkit (v.4.0.0.0) 52 .
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Local realignment, duplicate marking and raw variant calling were performed according to GATK best practices 32 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **3.8.1**
- Evidence: The reads were realigned, first using bamleftalign from FreeBayes (v.1.2.0) 120 , and then with ABRA (v.2.23) 121 on target regions that were identified using RealignerTargetCreator from GATK (v.3.8.1) 122 and expanded by 160 nucleotides with bedtools slop (v.2.21.0) 123 .
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Extrachromosomal DNA in the cancerous transformation of Barrett's oesophagus. (Nature 2023)

- DOI: 10.1038/s41586-023-05937-5 | PMCID: PMC10132967 | PMID: 37046089
- Evidence: BAM files underwent subsequent indel realignment with GATK IndelRealigner v.3.4-0-g7e26428 (ref.
- Full pipeline: alignment/mapping [BWA] -> registration [GATK] -> differential/statistical testing [SciPy v1.9.1] -> stage not stated [Strelka v2.0.15, VEP]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **4.1.7.0**
- Evidence: Next, we marked duplicates using the MarkDuplicates function from GATK (v.4.1.7.0) 55 .
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Version used: **3.8.1**
- Evidence: Local realignment around insertions and deletions (indels) was performed using the Genome Analysis toolkit (GATK (v.3.8.1) 44 ).
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: Duplicate reads were identified using the genome analysis toolkit (GATK) 91 , 92 with the MarkDuplicatesSpark command.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Version used: **4.0.7.0**
- Evidence: We called variants for each individual using HaplotypeCaller in BP-RESOLUTION mode with GATK 4.0.7.0 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### FinnGen provides genetic insights from a well-phenotyped isolated population. (Nature 2023)

- DOI: 10.1038/s41586-022-05473-8 | PMCID: PMC9849126 | PMID: 36653562
- Evidence: In brief, the variant call set was produced using the GATK HaplotypeCaller algorithm by following GATK best practices for variant calling.
- Full pipeline: alignment/mapping [SAIGE v0.35.8.8] -> variant calling [GATK] -> differential/statistical testing [SAIGE v0.35.8.8] -> stage not stated [R v4.0, VEP]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Version used: **4.1.0.0**
- Evidence: The mapped files were converted to BAM and sorted with samtools v1.6 56 , and duplicated reads were removed with GATK v4.1.0.0 MarkDuplicates 57 .
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Version used: **4.1.9.0**
- Evidence: CNV calling using WES Somatic CNVs were called using GATK (v.4.1.9.0) 61 .
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Evidence: Somatic single-nucleotide variants and insertion or deletion (indel) variants were called using Illumina Dragen 58 and GATK Mutect2 (ref.
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: Short alignments were removed with NYGC ShortAlignmentMarking (v.2.1) ( https://github.com/nygenome/nygc-short-alignment-marking ), and mate-pair information was added with GATK FixMateInformation (v.4.1.0) 57 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Evidence: We retained mapped reads with a mapping quality greater than 30, removed PCR duplicates using picard MarkDuplicates ( http://picard.sourceforge.net ), carried out local realignment using GATK 82 and computed the MD tag and extended BAQ for each read using the samtools calmd command.
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Evidence: We used the Genome Analysis Software Kit (GATK) (v.3.4-46) best-practice pipeline to analyse our WES data.
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **3.0**
- Evidence: ... b , Pie charts indicating the frequency of the deletion in 1,483 resequenced genomes from maize and teosinte, aligned with the B73 reference genome (GATK 3.0).
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: ... Picard ( http://broadinstitute.github.io/picard/ ); (4) indel realignment and base quality score recalibration for aligned reads were carried out by GATK 56 ; (5) and alignment quality control was done by Picard.
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: Microbiome Microbial identification Microbial sequences 126 were identified using GATK PathSeq 127 aligned against the default PathSeq microbial genome bundles.
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **3.4**
- Evidence: Downstream processing was done using the Genome Analysis Toolkit (GATK, v.3.4), SAMtools (v.1.0) and Picard Tools ( http://picard.sourceforge.net ; v.1.92).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Evidence: Genotype calling was carried out using Genome Analysis Toolkit 59 (v.4.1.9.0).
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **4.1.2**
- Evidence: SNP and indel calling were performed by GATK (v4.1.2) 45 .
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Genotyping was performed with the GATK UnifiedGenotyper (v.3.5) with default parameters and using the output mode ‘EMIT_ALL_SITES’ 87 .
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: We next performed variant calling with GATK Haplotype Caller 122 , conducted joint genotyping with GenotypeGVCFs 122 , and removed low-confident variants.
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **4.1.2.0**
- Evidence: Variant detection and filtering were carried out using GATK (v.4.1.2.0) 95 with the filtering parameters set to ‘QD < 2.0, QUAL < 30.0, SOR > 3.0, FS > 60.0, MQ < 40.0, MQRankSum < −12.5, ReadPosRankSum < −8.0’.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **4.1.6.0**
- Evidence: SNPs and small INDELs were called using GATK (v.4.1.6.0) 84 HaplotypeCaller.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Evidence: Raw SNP and InDel sets were called using GATK with the following parameters: --gcpHMM 10 -stand_emit_conf 10 -stand_call_conf 30.
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Evidence: Mapped reads were further realigned around indels using the Genome Analysis Toolkit (GATK) v.3.8 RealignerTargetCreator and IndelRealigner modules 57 , 58 , to reduce the number of indel miscalls.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Evidence: The marked BAM files are then processed using the GATK toolkit (v 3.2) according to the best practices for tumour normal pairs.
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### Compensatory evolution in NusG improves fitness of drug-resistant M. tuberculosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07206-5 | PMCID: PMC10990936 | PMID: 38509362
- Version used: **3.5**
- Evidence: Single-nucleotide polymorphisms (SNPs) were called and annotated using the HaplotypeCaller tool Genome Analysis Toolkit (version 3.5) using inputs from samtools (version 1.7).
- Full pipeline: variant calling [GATK v3.5, SAMtools v1.7] -> quantification [ImageJ] -> differential/statistical testing [Stan] -> stage not stated [RAxML v8.2.11, freebayes v1.3.1]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **4.0.12**
- Evidence: The somatic mutation candidates were called using MuTect2 from GATK (v4.0.12) software 40 and annotated with ANNOVAR (v20191024) 41 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Version used: **3.3.0**
- Evidence: Sample-level BAMs were re-aligned using GATK (v.3.3.0) and hereafter had the md-tag updated and extended BAQs calculated using samtools calmd (v.1.10) 78 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### GDF15 linked to maternal risk of nausea and vomiting during pregnancy. (Nature 2024)

- DOI: 10.1038/s41586-023-06921-9 | PMCID: PMC10808057 | PMID: 38092039
- Evidence: We used the GATK pipeline 39 to identify SNPs from the RNA-seq alignment data (that is, BAM files).
- Full pipeline: alignment/mapping [GATK] -> variant calling [BCFtools, SAMtools] -> quantification [BCFtools, SAMtools, lme4] -> registration [Picard] -> stage not stated [PLINK v1.90b, R]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **4.2.5.0**
- Evidence: Somatic mutations were detected from tumour samples using MuTect2 (GATK v.4.2.5.0) 76 to call somatic SNVs and small indels (<10 bp).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Evidence: Whole-exome sequencing data were processed using Sarek (v3.1.2) 70 , a pipeline that follows GATK best practices and is distributed by NF-core.
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### Somatic mutation and selection at population scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09584-w | PMCID: PMC12611758 | PMID: 41062696
- Evidence: For analyses relying on both common and rare SNPs we run GATK’s HaplotypeCaller (v.4.0.1.2) 67 , using default options, setting ploidy to 2 except for the male chromosome X (haploid) and providing dbSNP v.141 ( ncbi.nlm.nih.gov/snp , ref.
- Full pipeline: alignment/mapping [MAFFT] -> variant calling [BEDTools, GATK] -> differential/statistical testing [lme4] -> stage not stated [BCFtools, R]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: Sequencing duplicates were marked and removed using Picard implemented in the Genome Analysis Toolkit (GATK4) 68 .
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Evidence: The remaining 177,370 variants were left-aligned using GATK LeftAlignAndTrimVariants v4.1.3.0 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Single-cell transcriptomic and genomic changes in the ageing human brain. (Nature 2025)

- DOI: 10.1038/s41586-025-09435-8 | PMCID: PMC12527935 | PMID: 40903571
- Version used: **4.1.8.1**
- Evidence: Identification of sSNVs in neurons To identify sSNVs, we used both scWGS and corresponding bulk WGS data. scWGS and bulk WGS data were first processed accordingly to the GATK (v.4.1.8.1) best practices 64 .
- Full pipeline: alignment/mapping [BWA v0.7.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Cellpose, GATK v4.1.8.1, Picard, Seurat]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: In brief, we first called the VCF file profiles on all SNP variants per sample individually using GATK HaplotypeCaller to generate cell-line-specific VCF files.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **4.3**
- Evidence: Variant calling We called variants (SNPs) using GATK (v.4.3) 70 .
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### A missing enzyme-rescue metabolite as cause of a rare skeletal dysplasia. (Nature 2025)

- DOI: 10.1038/s41586-025-09397-x | PMCID: PMC12488480 | PMID: 40836090
- Evidence: Sequence variant detection was performed by the Genome Analysis Toolkit HaplotypeCaller (reference: http://www.broadinstitute.org/gatk/ ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: After mapping, the Genome Analysis Toolkit (GATK) (v.4.1.9.0) 113 was used with the operation HaplotypeCaller 114 for variant calling, BaseRecalibrator and ApplyBQSR were used to realign around SNPs and indels, and FastaAlternateReferenceMaker was used to create a sample-specific consensus sequence as a reference for each SCO locus in each sample.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Sequencing data were processed using the GATK best practices workflow.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### In vivo screen of Plasmodium targets for mosquito-based malaria control. (Nature 2025)

- DOI: 10.1038/s41586-025-09039-2 | PMCID: PMC12267055 | PMID: 40399670
- Version used: **3.5**
- Evidence: Raw sequencing reads were aligned to the P. falciparum 3D7 reference genome 53 (PlasmoDB v.13.0) and preprocessed following standard GATK (v.3.5) protocols.
- Full pipeline: alignment/mapping [GATK v3.5] -> stage not stated [ImageJ, Python v3.5, SnpEff]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Variants were called using the GATK best practices pipeline 87 .
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: Unmapped, non-unique and duplicated reads were filtered out using SAMtools 64 , 65 (v.1.9) and Picard (v.2.20.3-SNAPSHOT) before variants were called by a standard pipeline of Genome Analysis Toolkit (GATK 65 v.4.1.2) and Sentieon 66 (v.202112.01).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Detection of small de novo variants Following the parameters outlined previously 10 , we called variants in HiFi data aligned to T2T-CHM13 using GATK HaplotypeCaller 90 (v.4.3.0.0) and DeepVariant 87 (v.1.4.0) and naively identified variants unique to each G2 and G3 sample.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: To compile a high-confidence SNP dataset, we used the ‘VariantFiltration’ function in the Genome Analysis Toolkit 105 (v.4.1.4.0) with the ‘--cluster-window-size 10 --cluster-size 3’ parameters.
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Evidence: Somatic mutations were called by GATK Mutect2 v.4.5 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: ...m.nih.gov/grc ), mapped reads were marked for duplicates using Picard Markduplicates (v4.2.6.1), and read base-quality scores were recalibrated using GATK BaseRecalibrator (v4.2.6.1) and GATK ApplyBQSR (v4.2.6.1) 54 .
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Evidence: We then calibrated base quality by the GATK’s BaseRecalibrator using dbSNP version 138 as reference source.
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Evidence: After adaptor trimming, reads were mapped with BWA-MEM to GRCh38, and genotype calling was carried out with GATK haplotype caller.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### Immune evasion through mitochondrial transfer in the tumour microenvironment. (Nature 2025)

- DOI: 10.1038/s41586-024-08439-0 | PMCID: PMC11798832 | PMID: 39843734
- Version used: **4.1.8**
- Evidence: For each sample, variants were called using Mutect2 in the Genome Analysis Toolkit (v.4.1.8) under mitochondrial mode and with the read filter marked as duplicate disabled.
- Full pipeline: stage not stated [GATK v4.1.8, Mutect2, SnpEff v5.1d]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Reads were sorted with SAMtools 68 , polymerase chain reaction duplicates were removed with Picard Tools v.2.0.1 and indels were locally realigned using GATK software (v.3.7.0) 69 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Evidence: Using GATK 46 (v.4.2.0.0), we kept variants that were present in at least 75% of reads, with a Phred quality score higher than 30, a minimum read depth of 5, a minimum mapping quality of 20 and a string odd ratio of less than 3.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Version used: **4.1**
- Evidence: This pipeline follows the GATK 4.1 best practices workflow for alignment and variant calling.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Evidence: We used snpAD (v.0.3.11) 6 , 57 to call genotypes for the Zlatý kůň and Ranis13 high-coverage genomes after filtering for a base quality of 30 and a sequence length of 30, and after re-aligning indels using GATK 58 (v.1.3-14).
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### Dairy cows inoculated with highly pathogenic avian influenza virus H5N1. (Nature 2025)

- DOI: 10.1038/s41586-024-08166-6 | PMCID: PMC11754099 | PMID: 39406346
- Version used: **4.4**
- Evidence: High-frequency single nucleotide variants (SNVs) were called with GATK v.4.4 (ref.
- Full pipeline: stage not stated [BWA, GATK v4.4, R v4.4]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Evidence: For the three higher coverage genomes we called genotypes in a sample-wise manner using HaplotypeCaller from GATK 90 , followed by a subsequent step of joint haplotype calling using GenotypeGVCFs on the merged dataset.
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Demography and life histories across the Roman frontier in Germany 400-700 CE. (Nature 2026)

- DOI: 10.1038/s41586-026-10437-3 | PMCID: PMC13293882 | PMID: 42056513
- Version used: **3.8**
- Evidence: Reads were merged with ATLAS 60 , duplicates were removed with sambamba 61 , and realigned with GATK 3.8 (ref.
- Full pipeline: alignment/mapping [Matplotlib, Python] -> registration [GATK v3.8] -> differential/statistical testing [statsmodels v0.14.4]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Evidence: A standard GATK best practice pipeline was used to process the samples and call somatic genetic variants using GATK Mutect2 50 .
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **4.1.4.1**
- Evidence: After mapping the JF1/Ms reads to the mouse genome (mm10) using BWA-MEM v.0.7 with the default parameters, SNPs were called using HaplotypeCaller implemented in GATK v.4.1.4.1 (ref.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### The evolutionary history and unique genetic diversity of Indigenous Americans. (Nature 2026)

- DOI: 10.1038/s41586-026-10406-w | PMCID: PMC13149005 | PMID: 42020734
- Evidence: Specifically, sequence data in FASTQ format were aligned to the GRCh38 reference genome and preprocessed according to the GATK Best Practices for germline variant discovery and joint variant calling.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK, VEP] -> normalisation [VEP] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK v1.9, R, SnpEff]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **4.5.0.0**
- Evidence: The alignments were subject to GATK (v4.5.0.0) HaplotypeCaller 71 to call single-nucleotide polymorphism with - ploidy = 4, followed by filtration with genotype quality (QD) < 2.0 | | mapping quality (MQ) < 40.0 | | FisherStrand (FS) > 60.0 | | StrandOddsRatio (SOR) > 3.0 || MQRankSum < −12.5 || ReadPosRankSum < −8.0 parameters.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: On the basis of the GATK Best Practices workflow 79 , base quality score recalibration (BQSR) was performed (v.4.1.4.1), followed by variant calling using HaplotypeCaller in gVCF mode 80 .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Evidence: Following the GATK best practice workflows (v4.1.8.1), variants were identified after base quality score recalibration 68 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: For construction of phylogenetic lineage trees, short variants shared by many samples from the same patient were called and filtered using joint variant calling by GATK HaplotypeCaller (v.4.1.3, part of the NF-IAP pipeline; https://github.com/UMCUGenetics/NF-IAP ).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **4.2.6.1**
- Evidence: For the 1KCP samples, short-read data were aligned using BWA-MEM (v.0.7.17) 62 , and SNV genotypes were called using the GATK (v.4.2.6.1) workflow 63 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **3.6**
- Evidence: Homozygous SNPs and indels were corrected to match the consensus call from Illumina fragment reads (2 × 150, 400 bp insert) by aligning the reads using bwa-mem (v.0.7.17-r1188) 63 and identifying homozygous SNPs and indels with the UnifiedGenotyper tool in GATK (v.3.6-0-g89b7209) 64 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Version used: **3.7**
- Evidence: The resulting bam files were processed according to Genome Analysis Toolkit (GATK v3.7) best practices (picardtools v2.20.7).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: Analysis of genomic sequencing data The analysis of WES data from mouse tumour–normal sample pairs was performed according to the GATK best practice suggestions.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Version used: **4.1.9.0**
- Evidence: Duplicate reads were marked using GATK (v.4.1.9.0) 79 , and BAM files were indexed using Samtools v.1.18.
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Version used: **4.2.3.0**
- Evidence: Sample contamination was estimated using the GATK v.4.2.3.0 tool CalculateContamination 53 .
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **3.3**
- Evidence: To infer genetic ancestry, we called single-nucleotide polymorphisms (SNPs) from the aligned reads using the GATK (v.3.3) Haplotype caller 113 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: Using a .bed file of the HLA region coordinates, these alignments were streamed with the GATK PrintReads commands into the T1K genotyper, which was set to default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: PCR duplicates were removed using Picard MarkDuplicates ( http://picard.sourceforge.net ), and realignment around indels was performed using GATK 67 .
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **4.1.9.0**
- Evidence: Mapping single-nucleotide polymorphisms were genotyped using GATK (v.4.1.9.0), and unique mutations absent in the mapping strains were plotted using R (v.4.4.2).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Version used: **4.0**
- Evidence: Somatic SNVs and short indels were called using Mutect2 (GATK v.4.0) and Strelka2 (v.2.9.10) 60 , 61 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **4.1.8.1**
- Evidence: The SAM file was converted to BAM format using samtools (v.1.15.1) and mutation calling was performed using the AnalyzeSaturationMutagenesis tool from GATK (v.4.1.8.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: After sequencing, raw data were processed using the Genome Analysis Toolkit (GATK) v.3.4 to generate a variant call format (VCF) v.4.1 file.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Evidence: PCR duplicates were removed with Picard MarkDuplicates (version 1.95; http://picard.sourceforge.net ) and local realignment around indels was done with GATK ( 67 ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### Genomic evidence for inbreeding depression and purging of deleterious genetic variation in Indian tigers. (PNAS 2021)

- DOI: 10.1073/pnas.2023018118 | PMCID: PMC8670471 | PMID: 34848534
- Evidence: Mapped reads were realigned around indels using GATK (https://gatk.broadinstitute.org/hc/en-us) IndelRealigner.
- Full pipeline: alignment/mapping [ANGSD, GATK] -> registration [GATK] -> stage not stated [Picard, Strelka, VCFtools, VEP]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Evidence: We additionally performed local realignment for insertion-deletion (InDel) polymorphisms using the Genome Analysis Toolkit (GATK) version 3.7 ( 62 ).
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. (PNAS 2021)

- DOI: 10.1073/pnas.2106844118 | PMCID: PMC8713748 | PMID: 34916285
- Evidence: The sequence data were processed using standard pipelines as described in the Broad Institute’s Genome Analysis Tool Kit (GATK) Best Practices ( 80 ).
- Full pipeline: stage not stated [ADMIXTURE, BEDTools, GATK, R, VEP, WGCNA, scikit-learn]

### Molecular characterization of Barrett's esophagus at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2113061118 | PMCID: PMC8617519 | PMID: 34795059
- Evidence: WGS data were mapped against human reference genome GRCh37 by using the BWA (v0.7.5) mapping tool ( 57 ) with settings 'bwa mem -c 100 -M.' Sequence reads were marked for duplicates by using Sambamba (v0.6.8) and realigned per donor by using Genome Analysis Toolkit (GATK) IndelRealigner (v3.8.1) Raw variants were multisample-called by using the GATK HaplotypeCaller (v3.8-0) ( 58 ) and GATK-Queue (...
- Full pipeline: alignment/mapping [BWA v0.7.5, GATK] -> variant calling [BWA v0.7.5, GATK] -> registration [BWA v0.7.5, GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [R]

### Dendritic cell paucity in mismatch repair-proficient colorectal cancer liver metastases limits immune checkpoint blockade efficacy. (PNAS 2021)

- DOI: 10.1073/pnas.2105323118 | PMCID: PMC8609309 | PMID: 34725151
- Evidence: The Genome Analysis Toolkit ( 69 ) was used to call variants between the cancer cell line and the reference genome.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK] -> quantification [Bioconductor, DESeq2, R] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, GSVA, SnpEff]

### SARS-CoV-2 evolution in animals suggests mechanisms for rapid variant selection. (PNAS 2021)

- DOI: 10.1073/pnas.2105253118 | PMCID: PMC8612357 | PMID: 34716263
- Evidence: Data were preprocessed for quality with GATK ( 64 ), prior to calling SNVs and SVs with LoFrEq ( 65 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> stage not stated [GATK, Nextflow, SnpEff]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: Variants calling were performed for all samples using the UnifiedGenotyper function in GATK software ( 83 ).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### <i>BRCA1/Trp53</i> heterozygosity and replication stress drive esophageal cancer development in a mouse model. (PNAS 2021)

- DOI: 10.1073/pnas.2108421118 | PMCID: PMC8521688 | PMID: 34607954
- Evidence: We also analyzed the WES sequencing data using GATK HaplotypeCaller ( 69 ) in genomic vcf mode from the Broad Institute and confirmed results generated through our qPCR analysis.
- Full pipeline: variant calling [GATK] -> stage not stated [ImageJ]

### Genome evolution of the psammophyte <i>Pugionium</i> for desert adaptation and further speciation. (PNAS 2021)

- DOI: 10.1073/pnas.2025711118 | PMCID: PMC8545485 | PMID: 34649989
- Evidence: Genome-wide single nucleotide polymorphisms (SNPs) were called by GATK.
- Full pipeline: stage not stated [ADMIXTURE, AUGUSTUS, BUSCO, GATK, RepeatMasker]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Version used: **3.8**
- Evidence: SNP calling was performed using the UnifiedGenotyper of the Genome Analysis Toolkit (GATK v3.8) ( 39 ) under the “EMIT_ALL_CONFIDENT_SITES” option with a minimum confidence threshold 10; a vcf file for every ancient genome was produced, and SNPs that were close to each other by less than 20 bp were excluded.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **4.0.3.0**
- Evidence: Reads without a mapping mate were deleted using samtools view ( 87 ) and reads sorted by coordinate using GATK v4.0.3.0 SortSam ( 88 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### High frequency of an otherwise rare phenotype in a small and isolated tiger population. (PNAS 2021)

- DOI: 10.1073/pnas.2025273118 | PMCID: PMC8488692 | PMID: 34518374
- Evidence: We used GATK ( 104 ) to mark any genotype with a genotype quality value less than 10 (GQ < 10) and a depth less than 10 (DP < 10) as a missing genotype.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [BCFtools, BWA] -> variant calling [GATK, VCFtools] -> stage not stated [Picard]

### SAMD9L autoinflammatory or ataxia pancytopenia disease mutations activate cell-autonomous translational repression. (PNAS 2021)

- DOI: 10.1073/pnas.2110190118 | PMCID: PMC8403910 | PMID: 34417303
- Evidence: The GATK suite v3.3-0-g37228af was used for local indel realignment and base quality score recalibration. gVCFs generated with GATK HaplotypeCaller were joint-called as trios using GATK GenotypeGVCFs, and variants recalibrated using GATK Variant Quality Score Recalibrator (VQSR).
- Full pipeline: alignment/mapping [BWA v0.7.10] -> variant calling [GATK] -> registration [GATK] -> stage not stated [VEP]

### Longer or shorter spines: Reciprocal trait evolution in stickleback via triallelic regulatory changes in <i>Stanniocalcin2a</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100694118 | PMCID: PMC8346906 | PMID: 34321354
- Evidence: The reads were aligned to gasAcu1-4 using bwa mem and variants called with GATK following its Best Practices.
- Full pipeline: alignment/mapping [GATK, STAR]

### Accurate genomic variant detection in single cells with primary template-directed amplification. (PNAS 2021)

- DOI: 10.1073/pnas.2024176118 | PMCID: PMC8214697 | PMID: 34099548
- Version used: **4.1**
- Evidence: Data were trimmed using Trimmomatic ( 50 ) to remove adapter sequences and low-quality terminal bases, which was followed by GATK 4.1 best practices with genome assembly GRCh38.
- Full pipeline: read trimming [GATK v4.1, Trimmomatic] -> stage not stated [Picard]

### Genetic mechanisms of HLA-I loss and immune escape in diffuse large B cell lymphoma. (PNAS 2021)

- DOI: 10.1073/pnas.2104504118 | PMCID: PMC8179151 | PMID: 34050029
- Evidence: The presence of copy number aberrations was determined by Sequenza ( 52 ) and confirmed, in a subset of cases, by SNP6 array or GATK analysis; LOHHLA was used to identify haplotype-specific copy number changes of the HLA locus, as described previously ( 24 ).
- Full pipeline: variant calling [GATK]

### Genetic basis of variation in cocaine and methamphetamine consumption in outbred populations of <i>Drosophila melanogaster</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2104131118 | PMCID: PMC8201854 | PMID: 34074789
- Version used: **2.4**
- Evidence: The alignments were locally realigned, marked for PCR duplicates using GATK (version 2.4) ( 55 ) and Picard tools (version 1.89) before recalibrating base qualities with GATK.
- Full pipeline: alignment/mapping [GATK v2.4, Picard] -> registration [GATK v2.4, Picard] -> visualisation [Cytoscape v3.8.0]

### A phage mechanism for selective nicking of dUMP-containing DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2026354118 | PMCID: PMC8201957 | PMID: 34074772
- Version used: **3.7**
- Evidence: Mapped reads were further processed with GATK v.3.7.
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [GATK v3.7] -> variant calling [Cutadapt] -> stage not stated [Fiji, ImageJ, VEP]

### Adaptive differentiation and rapid evolution of a soil bacterium along a climate gradient. (PNAS 2021)

- DOI: 10.1073/pnas.2101254118 | PMCID: PMC8106337 | PMID: 33906949
- Evidence: The timeseries metagenomic data were processed for variant calling by mapping quality filtered sequence data to the complete reference ancestral genome using both the Genome Analysis Toolkit (GATK) best practices pipeline ( 72 ) and breseq version 0.26.1 ( 73 ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> stage not stated [BLAST, SPAdes]

### The genomes of ancient date palms germinated from 2,000 y old seeds. (PNAS 2021)

- DOI: 10.1073/pnas.2025337118 | PMCID: PMC8126781 | PMID: 33941705
- Version used: **3.5**
- Evidence: SNP calling and genotyping were performed with the Genome Analysis Toolkit v.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> variant calling [GATK v3.5] -> stage not stated [ADMIXTURE, Picard, R]

### Efficient detection and post-surgical monitoring of colon cancer with a multi-marker DNA methylation liquid biopsy. (PNAS 2021)

- DOI: 10.1073/pnas.2017421118 | PMCID: PMC7865146 | PMID: 33495330
- Evidence: Sequencing data analysis was performed with a combination of Fgbio, Burrows–Wheeler Aligner, Genome Analysis Toolkit, and MuTect2.
- Full pipeline: alignment/mapping [GATK]

### The mutational load in natural populations is significantly affected by high primary rates of retroposition. (PNAS 2021)

- DOI: 10.1073/pnas.2013043118 | PMCID: PMC8017666 | PMID: 33526666
- Evidence: We followed the general GATK version 3 Best Practices ( 44 ) to call SNP variants ( SI Appendix , Materials and Methods ) and only kept the SNP variants with unambiguous ancestral states in out-group species.
- Full pipeline: stage not stated [GATK, VEP v98.2]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: We called SNVs for each sample independently using the Cebus imitator 1.0 genome and the GATK UnifiedGenotyper pipeline (see SI Appendix for further methodological detail).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Integrated gene analyses of de novo variants from 46,612 trios with autism and developmental disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2203491119 | PMCID: PMC9674258 | PMID: 36350923
- Evidence: Family-level FreeBayes and GATK VCF files for SSC and SAGE samples are available at dbGaP (phs001874.v1.p1) ( 57 ) and also at SFARI Base (SFARI_SSC_WGS_2a).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [R v3.6.2] -> stage not stated [Cytoscape, GATK, STRING db, freebayes]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: JAFLEJ000000000 ] and variants were called with the Genome Analysis Tool Kit (GATK), specifying a haploid ploidy level ( 77 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: Local realignment around insertions and deletions was then performed to correct mapping-related artifacts using the genome analysis toolkit (GATK) ( 66 – 68 ) RealignerTargetCreator and IndelRealigner tools.
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Population dynamics of Baltic herring since the Viking Age revealed by ancient DNA and genomics. (PNAS 2022)

- DOI: 10.1073/pnas.2208703119 | PMCID: PMC9659336 | PMID: 36282902
- Evidence: Modern nuclear sequences were further processed following the GATK best practices pipeline with GATK4 ( 99 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [GATK, IQ-TREE v1.6.12, VCFtools v0.1.16]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Evidence: RealignerTargetCreator and IndelRealigner in the Genome Analysis Toolkit (GATK) v3.7.0 ( 94 ) were used for local realignment around indels.
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Heterozygous LRP1 deficiency causes developmental dysplasia of the hip by impairing triradiate chondrocytes differentiation due to inhibition of autophagy. (PNAS 2022)

- DOI: 10.1073/pnas.2203557119 | PMCID: PMC9477389 | PMID: 36067312
- Evidence: The variants with read depths of less than 4× were filtered out according to the Genome Analysis Toolkit ( 39 ).
- Full pipeline: alignment/mapping [BWA v0.59] -> stage not stated [ANNOVAR, GATK, ImageJ]

### Diploid-dominant life cycles characterize the early evolution of Fungi. (PNAS 2022)

- DOI: 10.1073/pnas.2116841119 | PMCID: PMC9457484 | PMID: 36037379
- Evidence: For short reads, k -mer counting was conducted on raw short reads using kmercountexact in bbtools ( https://sourceforge.net/projects/bbmap/ ) and allele frequencies were calculated from haploid or haploidized assemblies via a standard SNP calling approach using bwa mem v0.7.15 ( 78 ), samtools v1.5 ( 79 ), and GATK HaplotypeCaller v4.1.0.0 ( 80 ).
- Full pipeline: variant calling [GATK, SAMtools v1.5] -> structure determination [phytools] -> stage not stated [BUSCO]

### Additive genetic effects in interacting species jointly determine the outcome of caterpillar herbivory. (PNAS 2022)

- DOI: 10.1073/pnas.2206052119 | PMCID: PMC9456756 | PMID: 36037349
- Version used: **4.1**
- Evidence: We then aligned the DNA sequences to the M. sativa or L. melissa genome and identified SNPs using samtools (versions 1.10), bcftools (version 1.9), and GATK (version 4.1) ( 61 , 62 ) ( SI Appendix , DNA Sequence Alignment and Variant Calling ).
- Full pipeline: alignment/mapping [BCFtools v1.9, GATK v4.1, SAMtools] -> variant calling [BCFtools v1.9, GATK v4.1, SAMtools]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Version used: **3.3.0**
- Evidence: GATK (version 3.3.0; https://www.broadinstitute.org/GATK ) was used for local realignment around indels.
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Comparative genomics uncovers the evolutionary history, demography, and molecular adaptations of South American canids. (PNAS 2022)

- DOI: 10.1073/pnas.2205986119 | PMCID: PMC9407222 | PMID: 35969758
- Evidence: We filtered and mapped raw reads to the domestic dog CanFam3.1 ( 107 ) and conducted genotype calling using a modified pipeline from the Genome Analysis Toolkit ( 108 ) ( SI Appendix ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [PLINK] -> stage not stated [R]

### A missense mutation in &lt;i&gt;Kcnc3&lt;/i&gt; causes hippocampal learning deficits in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2204901119 | PMCID: PMC9351536 | PMID: 35881790
- Evidence: In brief, exomes were captured with SureSelect Mouse All Exon Kit (Agilent, Santa Clara, CA), sequenced with ∼100× coverage, and variants were called with the Genome Analysis Toolkit (GATK) ( 75 ).
- Full pipeline: stage not stated [GATK, R]

### Declines in prevalence alter the optimal level of sexual investment for the malaria parasite &lt;i&gt;Plasmodium falciparum&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122165119 | PMCID: PMC9335338 | PMID: 35867831
- Evidence: ( 60 )] were called with GATK v.3 Haplotype Caller using a set of genotyped pedigreed crosses for variant and base quality score recalibration.
- Full pipeline: variant calling [GATK]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **3.7**
- Evidence: Realignment around INDEL (insert and deletion) regions was performed using the IndelRealigner algorithm with the default settings (GATK version 3.7) ( 46 , 47 ).
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **3.8**
- Evidence: To begin, we used HaplotypeCaller [GATK v.3.8 ( 77 )] on the aligned bam files with the default heterozygosity prior (-hets = 0.005) and –ERC GVCF to produce per-sample genomic Variant Calling Format (gVCF) files.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Mutations in &lt;i&gt;MINAR2&lt;/i&gt; encoding membrane integral NOTCH2-associated receptor 2 cause deafness in humans and mice. (PNAS 2022)

- DOI: 10.1073/pnas.2204084119 | PMCID: PMC9245706 | PMID: 35727972
- Evidence: Genome Analysis Toolkit (GATK) was used for variant calling ( 43 – 45 ).
- Full pipeline: variant calling [GATK]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Evidence: Reads were aligned to the hg38 reference genome using the Burrows–Wheeler Aligner (BWA-MEM) and processed in accordance with Genome Analysis Toolkit (GATK; Broad Institute) workflow best practices ( 42 ).
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: The GATK ( https://gatk.broadinstitute.org/hc/en-us ) and SOAP tool packages (SOAP2, SOAPsnp, SOAPindel) ( 32 , 33 ) were applied for single-base corrections.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Genomic insights into zokors' phylogeny and speciation in China. (PNAS 2022)

- DOI: 10.1073/pnas.2121819119 | PMCID: PMC9171634 | PMID: 35512099
- Evidence: Clean reads were mapped against the chromosome-level reference genome by BWA, and SNPs were called with GATK.
- Full pipeline: alignment/mapping [GATK] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BUSCO, RAxML, VCFtools]

### Neo-sex chromosome evolution shapes sex-dependent asymmetrical introgression barrier. (PNAS 2022)

- DOI: 10.1073/pnas.2119382119 | PMCID: PMC9171612 | PMID: 35512091
- Version used: **3.8**
- Evidence: We aligned the reads to the same D. kepuluana reference (see Sequence Processing ) before genotyping with GATK 3.8.
- Full pipeline: alignment/mapping [GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [VCFtools]

### <i>duper</i> is a null mutation of Cryptochrome 1 in Syrian hamsters. (PNAS 2022)

- DOI: 10.1073/pnas.2123560119 | PMCID: PMC9170138 | PMID: 35471909
- Evidence: Duplicate reads were removed and base quality were recalibrated as suggested in the best-practice using GATK ( 20 ) (v4.1.2).
- Full pipeline: stage not stated [BUSCO v4.0.6, Flye v2.7, GATK, SAMtools, SnpEff]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Variant calling was performed using SAMtools ( 67 ), VarScan ( 68 ), and GATK ( 69 ).
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### Stone Age <i>Yersinia pestis</i> genomes shed light on the early evolution, diversity, and ecology of plague. (PNAS 2022)

- DOI: 10.1073/pnas.2116722119 | PMCID: PMC9169917 | PMID: 35412864
- Evidence: Duplicated reads were removed with Picard Tools v1.140 MarkDuplicates ( 93 ); bam files from the same individual were merged and used to calculate mappings statistics and perform variant calling with GATK UnifiedGenotyper v.3.5 ( 94 ).
- Full pipeline: variant calling [GATK, Picard] -> differential/statistical testing [GATK, Picard] -> visualisation [R, ggplot2] -> stage not stated [BEDTools v2.25.0, RAxML v0.9.0, ggpubr]

### Mutational background influences <i>P. aeruginosa</i> ciprofloxacin resistance evolution but preserves collateral sensitivity robustness. (PNAS 2022)

- DOI: 10.1073/pnas.2109370119 | PMCID: PMC9169633 | PMID: 35385351
- Evidence: Optical and PCR duplicates were detected by using the MarkDuplicates (Picard) function of The Genome Analysis Toolkit ( 70 ).
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R] -> stage not stated [GATK, Picard, SnpEff, freebayes]

### An integrative skeletal and paleogenomic analysis of stature variation suggests relatively reduced health for early European farmers. (PNAS 2022)

- DOI: 10.1073/pnas.2106743119 | PMCID: PMC9169634 | PMID: 35389750
- Evidence: Following the GATK (Genome Analysis Toolkit) workflow ( 130 ), realigning indels was performed using RealignerTargetCreator and IndelRealigner, followed by BaseRecalibrator to minimize sequence error introduced by potential mismatches to the reference ( 131 ).
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SnpEff] -> registration [GATK] -> stage not stated [PLINK v1.9, Picard]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Version used: **3.0**
- Evidence: Duplicate reads were filtered by using Picard (http://broadinstitute.github.io/picard) and realigned around indels by using GATK 3.0 ( 65 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Horizontal transmission enables flexible associations with locally adapted symbiont strains in deep-sea hydrothermal vent symbioses. (PNAS 2022)

- DOI: 10.1073/pnas.2115608119 | PMCID: PMC9168483 | PMID: 35349333
- Evidence: Allele counts (=symbiont strain abundances) and consensus haplotypes (=dominant symbiont strains) were extracted with GATK’s V ariants T o T able tool ( 89 ).
- Full pipeline: variant calling [GATK] -> quantification [GATK] -> stage not stated [Python, R]

### Sympatric speciation of the spiny mouse from Evolution Canyon in Israel substantiated genomically and methylomically. (PNAS 2022)

- DOI: 10.1073/pnas.2121822119 | PMCID: PMC9060526 | PMID: 35320043
- Evidence: SNP was called for each individual using GATK, and genetic diversity was calculated by VCFtools.
- Full pipeline: stage not stated [Bismark, DELLY, GATK, Metascape, R, VCFtools]

### Purging of deleterious burden in the endangered Iberian lynx. (PNAS 2022)

- DOI: 10.1073/pnas.2110614119 | PMCID: PMC8931242 | PMID: 35238662
- Version used: **3.7**
- Evidence: GATK v3.7 HaplotypeCaller ( 97 ) was used to generate variation data for the pool of 60 Iberian and Eurasian lynx samples.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> variant calling [GATK v3.7] -> stage not stated [SnpEff v4.3i]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: Reads mapped to the mitochondrial genome were removed, using samtools idxstats, and reads marked for PCR duplicates were also removed, using GATK MarkDuplicates.
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### Molecular parallelism in signaling function across different sexually selected ornaments in a warbler. (PNAS 2022)

- DOI: 10.1073/pnas.2120482119 | PMCID: PMC8872772 | PMID: 35165176
- Version used: **4.2.1.0**
- Evidence: These SNPs were obtained from transcripts in developing feathers and were discovered following the GATK (v4.2.1.0) ( 53 ) RNA-seq short-variant discovery pipeline ( SI Appendix ).
- Full pipeline: alignment/mapping [R, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.1.0, HISAT2 v2.1.0, ImageJ, SAMtools v1.7]

### Ancient DNA at the edge of the world: Continental immigration and the persistence of Neolithic male lineages in Bronze Age Orkney. (PNAS 2022)

- DOI: 10.1073/pnas.2108001119 | PMCID: PMC8872714 | PMID: 35131896
- Version used: **3.8**
- Evidence: We used GATK (version 3.8) to call pseudohaploid genotypes at known SNP positions, which were then merged with the Human Origins dataset ( 61 ), the 1000 Genomes Project data, and realigned published ancient samples ( SI Appendix ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK v3.8] -> quantification [ADMIXTURE v1.3] -> registration [GATK v3.8] -> differential/statistical testing [ADMIXTURE v1.3]

### Engineering and functional analysis of yeast with a monotypic 40S ribosome subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2114445119 | PMCID: PMC8833219 | PMID: 35105807
- Version used: **3.5**
- Evidence: RealignerTargetCreator and IndelRealigner of the Genome Analysis Toolkit (GATK v3.5) were used to realign the reads around the insertion–deletion mutations (indels) to reduce the errors of SNP calling near the indels ( 47 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> variant calling [GATK v3.5, SnpEff] -> registration [GATK v3.5] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [Picard]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Evidence: Raw reads from all whole-genome sequencing libraries (PCR-free and Chromium) were processed following a modified version of the “Genome Analysis Toolkit Best Practices Pipeline” ( 34 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### No link between population isolation and speciation rate in squamate reptiles. (PNAS 2022)

- DOI: 10.1073/pnas.2113388119 | PMCID: PMC8795558 | PMID: 35058358
- Version used: **4.1.8**
- Evidence: We called variants across all individuals using samtools v1.5 ( 105 ), filtered variants to retain only those with coverage > 20× and quality > 20, and used this variant set to recalibrate alignments using GATK v4.1.8 ( 106 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [GATK v4.1.8, RAxML v8.2.11, SAMtools v1.5] -> stage not stated [R, phytools]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: The variant calling procedure was adapted from the best practice recommendations for the Genome Analysis Toolkit (GATK) workflow ( 73 ) provided by the Broad Institute ( 74 , 75 ).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: The GATK pipeline was used to identify variants from RNA-seq data.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### A role for mutations in &lt;i&gt;AK9&lt;/i&gt; and other genes affecting ependymal cells in idiopathic normal pressure hydrocephalus. (PNAS 2023)

- DOI: 10.1073/pnas.2300681120 | PMCID: PMC10743366 | PMID: 38100419
- Evidence: Single nucleotide variants (SNVs) and insertions/deletions (indels) were identified (Human Genome build GRCh37, bwa-mem, Genome Analysis Toolkit HaplotypeCaller).
- Full pipeline: variant calling [BWA, GATK] -> stage not stated [ImageJ]

### A suppressor screen &lt;i&gt;in C. elegans&lt;/i&gt; identifies a multiprotein interaction that stabilizes the synaptonemal complex. (PNAS 2023)

- DOI: 10.1073/pnas.2314335120 | PMCID: PMC10723054 | PMID: 38055743
- Evidence: We used GATK to call single nucleotide variants and indels relative to the reference genome ( 61 , 62 ).
- Full pipeline: alignment/mapping [BWA, GATK] -> stage not stated [AlphaFold, SnpEff]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Version used: **4.2.3**
- Evidence: Variant calling was carried out following the Genome Analysis Toolkit (GATK version 4.2.3) Best Practices ( 69 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Functional genomic diversity is correlated with neutral genomic diversity in populations of an endangered rattlesnake. (PNAS 2023)

- DOI: 10.1073/pnas.2303043120 | PMCID: PMC10614936 | PMID: 37844221
- Evidence: Sequence preprocessing and mapping was performed following GATK “Best Practice Workflow” ( 64 ) ( SI Appendix, Supplementary Methods ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, SnpEff v4.3] -> stage not stated [BUSCO, R]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Version used: **3.8.1**
- Evidence: The SNPs were identified using GATK (The Genome Analysis Toolkit, version 3.8.1) ( 81 ) and bcftools (Tools for manipulating Variant Call Format and Binary Variant Call Format, version 1.15.1).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Evidence: The Genome Analysis Toolkit (GATK) v.4.1.8 ( 64 ) was used for SNP calling.
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We marked duplicates with the Picard tool MarkDuplicates, and then we used the Genome Analysis Toolkit (GATK) tools HaplotypeCaller and GenotypeGVCFs for joint genotyping across genomic samples.
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### Descent, marriage, and residence practices of a 3,800-year-old pastoral community in Central Eurasia. (PNAS 2023)

- DOI: 10.1073/pnas.2303574120 | PMCID: PMC10483636 | PMID: 37603728
- Version used: **3.6**
- Evidence: PCR duplicates were removed with sambamba markdup ( 110 ), and the remaining reads were realigned around known SNPs and InDels with GATK 3.6 ( 111 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [ANGSD] -> registration [GATK v3.6]

### Using evolutionary constraint to define novel candidate driver genes in medulloblastoma. (PNAS 2023)

- DOI: 10.1073/pnas.2300984120 | PMCID: PMC10438395 | PMID: 37549291
- Version used: **4.1.4**
- Evidence: GATK’s Funcotator module (GATK 4.1.4.) was used to functionally classify the MB and PA somatic point mutation (SPM) and somatic indel mutations (SIM) as being either coding or noncoding changes.
- Full pipeline: stage not stated [BEDTools v2.29.2, GATK v4.1.4]

### The contributions of rare inherited and polygenic risk to ASD in multiplex families. (PNAS 2023)

- DOI: 10.1073/pnas.2215632120 | PMCID: PMC10400943 | PMID: 37506195
- Evidence: Single-nucleotide variants and small insertions/deletions were called using the Genome Analysis Toolkit.
- Full pipeline: stage not stated [GATK]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Version used: **4.1**
- Evidence: Genome-wide variants were called by mapping Illumina reads against the Fol4287 reference using GATK v4.1 ( 77 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### The SHDRA syndrome-associated gene <i>TMEM260</i> encodes a protein-specific O-mannosyltransferase. (PNAS 2023)

- DOI: 10.1073/pnas.2302584120 | PMCID: PMC10214176 | PMID: 37186866
- Evidence: Genome Analysis Toolkit HaplotypeCaller was used for variant calling and Ensembl Variant Effect Predictor for variant annotation.
- Full pipeline: variant calling [GATK, VEP] -> quantification [ImageJ] -> stage not stated [AlphaFold]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **3.8**
- Evidence: Haplotype Caller and GenotypeGVCFs in GATK v3.8 ( 93 ) were used for joint genotyping across all samples.
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Epistasis reduces fitness costs of influenza A virus escape from stem-binding antibodies. (PNAS 2023)

- DOI: 10.1073/pnas.2208718120 | PMCID: PMC10151473 | PMID: 37068231
- Evidence: Analysis of nonconsensus variants was made using LoFreq ( 57 ) following the Genome Analysis Toolkit best practices ( 58 ).
- Full pipeline: read trimming [BWA, Trimmomatic v0.39] -> alignment/mapping [BWA, Trimmomatic v0.39] -> stage not stated [GATK, Picard]

### Ancient DNA from a lost Negev Highlands desert grape reveals a Late Antiquity wine lineage. (PNAS 2023)

- DOI: 10.1073/pnas.2213563120 | PMCID: PMC10151551 | PMID: 37068234
- Evidence: SNPs calling for modern and ancient samples was done using HaplotypeCaller and GenotypeGVCFs protocols of the GATK pipeline ( 69 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.5] -> variant calling [GATK, VCFtools] -> dimensionality reduction/clustering [pheatmap] -> visualisation [ggplot2]

### Standing genetic variation fuels rapid evolution of herbicide resistance in blackgrass. (PNAS 2023)

- DOI: 10.1073/pnas.2206808120 | PMCID: PMC10120058 | PMID: 37043536
- Version used: **4.1.3.0**
- Evidence: Variants were called with GATK v4.1.3.0 ( 69 ), and SNPs were filtered following the recommendations of the RAD-Seq variant-calling pipeline ‘dDocent’ ( 70 ).
- Full pipeline: read trimming [BUSCO] -> alignment/mapping [MAFFT v7.407] -> variant calling [MAFFT v7.407] -> visualisation [MAFFT v7.407] -> stage not stated [ADMIXTURE, ANGSD v0.930, GATK v4.1.3.0, InterProScan]

### Interrogating bromodomain inhibitor resistance in KMT2A-rearranged leukemia through combinatorial CRISPR screens. (PNAS 2023)

- DOI: 10.1073/pnas.2220134120 | PMCID: PMC10120025 | PMID: 37036970
- Version used: **4.1.2.0**
- Evidence: Read duplication was marked with MarkDuplicates from GATK (v4.1.2.0).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [RSEM] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GATK v4.1.2.0, GSEA]

### Spectra and characteristics of somatic mutations induced by ionizing radiation in hematopoietic stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2216550120 | PMCID: PMC10104525 | PMID: 37018193
- Version used: **4.1.0.0**
- Evidence: Sequence alterations from the mouse reference genome were called as genomic variants using GATK v4.1.0.0 HaplotypeCaller with a minimum base quality of 20.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.0.0, Picard v2.18.26, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> differential/statistical testing [R v4.0.3]

### The expansion of agriculture has shaped the recent evolutionary history of a specialized squash pollinator. (PNAS 2023)

- DOI: 10.1073/pnas.2208116120 | PMCID: PMC10104555 | PMID: 37011184
- Evidence: The GATK pipeline v4.3 ( 56 ) was used to remove PCR and optical duplicates, jointly call haplotypes across samples, and filter low-confidence SNP calls.
- Full pipeline: alignment/mapping [AUGUSTUS] -> variant calling [GATK] -> stage not stated [BUSCO v4.0.6, GSEA, R]

### The genomics of linkage drag in inbred lines of sunflower. (PNAS 2023)

- DOI: 10.1073/pnas.2205783119 | PMCID: PMC10083583 | PMID: 36972449
- Evidence: For each assembly, raw reads of 48 landrace and wild samples were aligned to the genome, and a VCF file was generated by using a GATK pipeline ( SI Appendix , SI Text ).
- Full pipeline: alignment/mapping [GATK] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.1.2, Snakemake, VCFtools]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Evidence: Single nucleotide polymorphisms (SNPs) were called using the Genome Analysis Toolkit (GATK) version 3.6 ( 61 , 62 ), according to the GATK Best Practices.
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **3.8**
- Evidence: The raw reads were mapped to the genome using bwa-mem (0.7.16a), and we used GATK (3.8) ( 119 ) pipeline to call variants.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### The evolution of the human DNA replication timing program. (PNAS 2023)

- DOI: 10.1073/pnas.2213896120 | PMCID: PMC10013799 | PMID: 36848554
- Evidence: Chimpanzee SNPs and indels were called with GATK ( 50 ) and used in the rtQTL analysis.
- Full pipeline: stage not stated [GATK]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: We estimated the impacts of variants (SNPs and INDELs) from coding regions using the species-specific genome annotations generated for both species. gVCFs were generated for each individual followed by joint-genotyping using GATK ( 132 ), allowing the reference individuals to include homozygous alleles found in other individuals.
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Changes in the functional diversity of modern bird species over the last million years. (PNAS 2023)

- DOI: 10.1073/pnas.2201945119 | PMCID: PMC9963860 | PMID: 36745783
- Evidence: As part of this previous study, genomes for each species were consistently sequenced and assembled to minimize potential error due to bioinformatics artifacts, and heterozygous information for each species was inferred based on a BWA+GATK pipeline ( 18 , 50 ).
- Full pipeline: stage not stated [GATK, R v3.6]

### Antidepressants can induce mutation and enhance persistence toward multiple antibiotics. (PNAS 2023)

- DOI: 10.1073/pnas.2208344120 | PMCID: PMC9945972 | PMID: 36689653
- Version used: **4.1.4.1**
- Evidence: Bacterial genomic DNA was extracted and sequenced, followed by the SNP calling according to the standard best practice guide of Genome Analysis Toolkit (GATK, v4.1.4.1) ( 72 ).
- Full pipeline: variant calling [GATK v4.1.4.1]

### Genome editing in plants using the compact editor CasΦ. (PNAS 2023)

- DOI: 10.1073/pnas.2216822120 | PMCID: PMC9942878 | PMID: 36652483
- Version used: **4.2.0.0**
- Evidence: GATK (4.2.0.0) ( 37 ) MarkDuplicatesSpark was used to remove PCR duplicate reads.
- Full pipeline: read trimming [BWA v0.7.17, Trim Galore] -> alignment/mapping [BWA v0.7.17, Trim Galore] -> stage not stated [GATK v4.2.0.0, R, Strelka v2.9.2]

### <i>Regulator of Awn Elongation 3</i>, an E3 ubiquitin ligase, is responsible for loss of awns during African rice domestication. (PNAS 2023)

- DOI: 10.1073/pnas.2207105120 | PMCID: PMC9942864 | PMID: 36649409
- Evidence: Individual resequencing datasets were downloaded from the internet as raw reads and aligned to the Nipponbare reference genome using BWA software ( 65 , 66 ) for alignment, and GATK’s HaplotypeCaller algorithm ( 67 – 70 ) for variant-calling.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> stage not stated [AlphaFold]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: We called and filtered variants using GATK ( 88 ) following the GATK best practices ( 89 , 90 ) with the exception of Base Quality Score Recalibration, which was not possible as there does not exist a reference variant set for Anolis cristatellus .
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Evidence: To identify variants in the mouse-passaged isolates, Illumina reads for CPL and CPB samples were aligned to the CU assembly with BWA-MEM v0.7.17 ( 70 ), and variants were called with our publicly available GATK v4 pipeline ( https://github.com/broadinstitute/fungal-wdl/tree/master/gatk4 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Two-speed genome evolution drives pathogenicity in fungal pathogens of animals. (PNAS 2023)

- DOI: 10.1073/pnas.2212633120 | PMCID: PMC9926174 | PMID: 36595674
- Evidence: For Bd , Genome Analysis Toolkit (GATK) v.4.1.2.0 ( 102 ) was used to call variants and dN / dS values for each gene in each lineage determined using the yn00 program of PAML ( 103 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, RAxML] -> stage not stated [BUSCO, Canu v1.8, GATK, HMMER, RepeatMasker v4.0.5]

### Breast cancer patient-derived whole-tumor cell culture model for efficient drug profiling and treatment response prediction. (PNAS 2023)

- DOI: 10.1073/pnas.2209856120 | PMCID: PMC9910599 | PMID: 36574653
- Evidence: Briefly, following the GATK best practices preprocessing steps, each sample was aligned using Burrows–Wheeler Aligner (BWA) MEM algorithm version 0.7.16a ( 63 ) to the human genome assembly (build GRCh38), followed by duplicate marking and base recalibration ( 64 ).
- Full pipeline: alignment/mapping [GATK] -> stage not stated [GSEA, SnpEff]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: Indels were realigned using GATK RealignerTargetCreator followed by GATK IndelRealigner ( 116 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Evidence: Mapped reads were then collated into a single file using samtools v1.9 ( 65 ), which was sorted and duplicate reads marked using biobambam2 ( 66 ), and bases recalibrated using baseRecalibrator from the GATK software suite v3.5 ( 67 ).
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: Duplicate reads were marked using GATK ( 99 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Maternal genetic variants in kinesin motor domains prematurely increase egg aneuploidy. (PNAS 2024)

- DOI: 10.1073/pnas.2414963121 | PMCID: PMC11551467 | PMID: 39475646
- Version used: **3.8**
- Evidence: Data were aligned to the human reference genome (hg19) using BWA ( 77 ), and the joint genotyping was performed using the GATK v3.8 pipeline following the GATK best practices ( 78 ).
- Full pipeline: alignment/mapping [BWA, GATK v3.8] -> variant calling [BWA, GATK v3.8] -> stage not stated [ImageJ]

### miR-96-5p expression is sufficient to induce and maintain the senescent cell fate in the absence of stress. (PNAS 2024)

- DOI: 10.1073/pnas.2321182121 | PMCID: PMC11459134 | PMID: 39325426
- Evidence: Output FASTQ files were processed with FastQC; the Genome Analysis Toolkit (GATK; Broad Institute) was used to clean FASTQ files which were then aligned to hg38 with the (Burrows-Wheeler Aligner) BWA.
- Full pipeline: quality control [FastQC, GATK] -> alignment/mapping [FastQC, GATK] -> differential/statistical testing [MACS2] -> stage not stated [Enrichr]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Filtering of the variant calls was based on the GATK’s best practice guidelines, and we included filters for mapping quality (MQ 3 40 and MQRankSum 3 –12.5), variant confidence (QD 3 2), strand bias (FS < 60), read position bias (ReadPosRankSum 3 –8), and genotype quality (GQ 3 10).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Version used: **4.1.4.1**
- Evidence: Reads were mapped to the GenTig1.0 genome ( 66 ) using BWA-MEM v0.7.17 ( 67 ) and variant calling was subsequently performed by Gencove using the Genome Analysis Toolkit v4.1.4.1 ( 68 ) according to best practices ( 69 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Microevolutionary change in wild stickleback: Using integrative time-series data to infer responses to selection. (PNAS 2024)

- DOI: 10.1073/pnas.2410324121 | PMCID: PMC11406292 | PMID: 39231210
- Evidence: All samples were mapped to v5 of the stickleback reference genome ( 66 ) and genotyped using the genome analysis tool kit (GATK) best practices pipeline ( 67 ).
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> differential/statistical testing [R, Stan, brms] -> stage not stated [ImageJ]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Evidence: After sorting and deduplication of the resulting alignment files, variant calling was performed via the Sentieon Haplotyper pipeline, which is similar to the Genome Analysis Toolkit (GATK) HaplotypeCaller pipeline.
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### An additional proofreader contributes to DNA replication fidelity in mycobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322938121 | PMCID: PMC11348249 | PMID: 39141351
- Evidence: The variant calling was performed with SAMtools and Genome Analysis Toolkit ( 63 ).
- Full pipeline: variant calling [GATK, SAMtools] -> stage not stated [AlphaFold]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: Local realignment was performed using InDels and SNPs from 100 Genomes and base quality score recalibration was performed using GATK.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: Sequence duplicates were removed using the MarkDuplicates function in Picard v/2.18.26 ( 80 ) and indels were realigned using GATK v/3.8.1 ( 81 ).
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: ( 10 ) and best practices of The Genome Analysis Toolkit (GATK) ( 25 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: Single-nucleotide variants and small indels were called with GATK HaplotypeCaller ( 62 ) and Freebayes ( 63 ), and annotated in ANNOVAR ( 64 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Version used: **4.0.0**
- Evidence: Then, single nucleotide polymorphisms were identified by GATK v.4.0.0 employing the parameters “QD < 2.0 || MQ <40.0 || FS >60.0 || SOR >3.0 || MQRankSum <−12.5 || ReadPosRankSum <−8.0” ( 115 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Evidence: We used the Genome Analysis Toolkit (GATK) v4.1.9 tool MarkDuplicatesSpark (as in ref.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Evidence: We took aligned bams and ran them through GATK’s Best Practices to call SNPs, using the HaplotypeCaller algorithm in gvcf mode, Genomics DBImport and GenotypeGVCFs ( 93 ).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### Integrated mutational landscape analysis of poorly differentiated high-grade neuroendocrine carcinoma of the uterine cervix. (PNAS 2024)

- DOI: 10.1073/pnas.2321898121 | PMCID: PMC11046577 | PMID: 38625939
- Evidence: The sequencing data were processed using the GATK Best Practice workflow ( 36 – 38 ).
- Full pipeline: alignment/mapping [HISAT2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [CNVkit, GATK]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Version used: **4.2.0.0**
- Evidence: GATK version 4.2.0.0 ( 84 ) was used to call SNPs.
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Version used: **3.8.0**
- Evidence: We used GATK (v 3.8.0) ( 95 ) to call genotypes.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### Environmental radiation exposure at Chornobyl has not systematically affected the genomes or chemical mutagen tolerance phenotypes of local worms. (PNAS 2024)

- DOI: 10.1073/pnas.2314793121 | PMCID: PMC10945782 | PMID: 38442158
- Version used: **4.3.0.0**
- Evidence: Alignments were genotyped and converted to vcfs using GATK v4.3.0.0 (HaplotypeCaller -ax sr to generate GVCFs, GenomicsDBImport to combine all samples into one database, GenotypeGVCFs -all-sites to produce a vcf) ( 52 ).
- Full pipeline: alignment/mapping [GATK v4.3.0.0, R, SAMtools v1.11, VCFtools v0.1.16, minimap2] -> variant calling [GATK v4.3.0.0] -> stage not stated [BCFtools v1.14, Flye v2.8.1, ImageJ]

### Taking a color photo: A homozygous 25-bp deletion in <i>Bace2</i> may cause brown-and-white coat color in giant pandas. (PNAS 2024)

- DOI: 10.1073/pnas.2317430121 | PMCID: PMC10945837 | PMID: 38437540
- Evidence: The short variants were called and genotyped using NGS reads of 35 genome-resequenced pandas with GATK ( 25 ), and SVs were identified and genotyped with Manta and Graphtyper ( 26 ).
- Full pipeline: variant calling [GATK] -> stage not stated [BUSCO]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Evidence: Duplicate reads in the alignments are marked using GATK MarkDuplicates (v4.2.6.1).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: NGS reads were aligned using BWA ( 41 ), and GATK ( 42 ) performed the variant calling.
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Version used: **4.2.0.0**
- Evidence: Duplicate reads in the resulting BAM files were marked using Samtools version 1.11 and Picard (GATK version 4.2.0.0).
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Evidence: For VAR analysis, variants were called using GATK HaplotypeCaller (v4.1.4.1) ( 66 , 67 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Version used: **4.0**
- Evidence: The single-nucleotide variant (SNV)/indel call analysis pipeline was based on the Genome Analysis Tool Kit (GATK, v4.0; https://software.broadinstitute.org/gatk/ ) best practices ( 17 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### A new late Neanderthal from Crimea reveals long-distance connections across Eurasia. (PNAS 2025)

- DOI: 10.1073/pnas.2518974122 | PMCID: PMC12625898 | PMID: 41144685
- Evidence: Unmapped reads were removed with samtools v.1.20 and PCR duplicates were filtered out with GATK MarkDuplicates v.3.1.1.
- Full pipeline: alignment/mapping [ANGSD, Python] -> stage not stated [GATK, SAMtools v1.20]

### Genetic regulation of the estrogen receptor and inherited predisposition to breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2517736122 | PMCID: PMC12582305 | PMID: 41129222
- Evidence: Subsequent processing was carried out with SAMtools v1.10 ( 51 ) and Genome Analysis Toolkit (GATK) v4.1.4 ( 52 ), including sorting and merging of BAM files, removal of duplicate reads, realigning indels and recalibrating base quality scores.
- Full pipeline: variant calling [freebayes v1.3] -> registration [GATK, SAMtools v1.10]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: We followed the Broad Institute’s GATK Best Practices workflow ( 77 ) to identify variants within our samples.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Evolutionary histories of functional mutations during the domestication and spread of &lt;i&gt;japonica&lt;/i&gt; rice in Asia. (PNAS 2025)

- DOI: 10.1073/pnas.2514614122 | PMCID: PMC12582302 | PMID: 41115193
- Evidence: Alignment of sequencing reads and production of GATK gvcf files were performed as described previously for modern ( 21 ) and herbarium genomes ( 95 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, Nextflow v20.10.0] -> variant calling [PLINK v1.90] -> dimensionality reduction/clustering [R v4.3] -> stage not stated [VCFtools v1.6]

### A species interaction kick-starts ecological speciation in allopatry. (PNAS 2025)

- DOI: 10.1073/pnas.2506625122 | PMCID: PMC12557528 | PMID: 41082661
- Evidence: The GATK-4.1.9.0 pipeline workflow was followed including MarkDuplicates and a base quality recalibration of sequencing reads using the BaseRecalibrator program of GATK-4 .
- Full pipeline: alignment/mapping [BWA] -> stage not stated [BCFtools, GATK, SAMtools, VCFtools, lme4]

### Natural history of liver fluke infection underpins epidemiological patterns of biliary cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2423536122 | PMCID: PMC12541340 | PMID: 41071656
- Version used: **4.1.4.1**
- Evidence: Duplicates were marked and removed using GATK v.4.1.4.1 ( 60 ) and base quality scores recalibrated for tumor sequences with ICGC PCAWG consensus calls for somatic SNVs and indels ( 61 ).
- Full pipeline: stage not stated [GATK v4.1.4.1, Mutect2, SAMtools v1.9]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Variant calling was performed based on the GATK best practice pipeline (version 4.3.0.0).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: Mapping, using BWA-MEM ( 86 ), and SNP calling, using GATK ( 87 ), were performed by Gencove Inc., a service provider.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Version used: **4.1.6.0**
- Evidence: To identify genetic markers from low-coverage WGS data, we used the program HaplotypeCaller in the Genome Analysis Toolkit (GATK version 4.1.6.0) ( 68 ) applying a minimum base quality score of 33 and a minimum mapping quality score of 20 to reduce lane effects ( 69 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Version used: **3.7**
- Evidence: All samples were aligned to the human reference genome (GRCh38) version using bwa 0.7.15, the generated SAM file was compressed into a BAM file and sorted by genomic position using samtools 1.3.1 and variant calling was performed using Genome Analysis Toolkit 3.7 software ( 61 , 62 ).
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### DNA polymerase β suppresses somatic indels at CpG dinucleotides in developing cortical neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2506846122 | PMCID: PMC12377747 | PMID: 40802685
- Version used: **4.1.0.0**
- Evidence: Genomic variants, compared with the mouse reference genome, were called using GATK v4.1.0.0 HaplotypeCaller ( 34 ).
- Full pipeline: alignment/mapping [BWA, GATK v4.1.0.0, Picard, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> stage not stated [HOMER]

### Repeated polyploidization shapes divergence in floral morphology in &lt;i&gt;Lithophragma bolanderi&lt;/i&gt; (Saxifragaceae). (PNAS 2025)

- DOI: 10.1073/pnas.2505119122 | PMCID: PMC12377753 | PMID: 40802687
- Version used: **4.1.4.1**
- Evidence: We mapped reads trimmed with fastp ( 76 ) of both species to the reference genome of L. bolanderi with bwa version 0.7.18 ( 77 ), identified and filtered duplicated reads, and called SNPs with GATK version 4.1.4.1 by using Haplotypecaller to call variants per individual, for their specific ploidy levels, and then aggregate variants using GenotypeGVCFs ( 78 , 79 ).
- Full pipeline: read trimming [GATK v4.1.4.1, fastp] -> alignment/mapping [GATK v4.1.4.1, fastp] -> variant calling [GATK v4.1.4.1, IQ-TREE, VCFtools, fastp] -> quantification [ImageJ] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4] -> stage not stated [BUSCO, WhatsHap]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Version used: **3.7**
- Evidence: ...d convert the format of the data; c) use the Picard software (v1.134) ( http://broadinstitute.github.io/picard/ ) to mark duplicate reads; d) use the Genome Analysis Toolkit (GATK v3.7) ( 47 ) to identify SNVs and indels; e) perform functional annotation of these variant sites using the ANNOVAR software (16 Jul 2016 version).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### A genomic test of sex-biased dispersal in white sharks. (PNAS 2025)

- DOI: 10.1073/pnas.2507931122 | PMCID: PMC12358869 | PMID: 40758892
- Version used: **4.0**
- Evidence: Variant calling was performed on the MC dataset and on the 40 autosomes using GATK v4.0 ( 46 ), following GATK best practices.
- Full pipeline: read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> variant calling [GATK v4.0] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools v1.9, PLINK]

### A recurrent de novo damaging variant in &lt;i&gt;EMP2&lt;/i&gt; causes progressive symmetric erythrokeratoderma. (PNAS 2025)

- DOI: 10.1073/pnas.2509896122 | PMCID: PMC12358830 | PMID: 40758889
- Evidence: Reads were aligned to the GRCh38 reference genome and processed with GATK and CASAVA 1.8.2 for variant calling.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [QuPath] -> dimensionality reduction/clustering [Monocle, Seurat, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ANNOVAR]

### Whole-genome duplication increases genetic diversity and load in outcrossing <i>Arabidopsis arenosa</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2501739122 | PMCID: PMC12337351 | PMID: 40737318
- Version used: **3.7**
- Evidence: We used picard-2.8.1 to mark duplicate reads and called genotypes with GATK (v.3.7).
- Full pipeline: alignment/mapping [minimap2 v2.22] -> variant calling [GATK v3.7, R] -> differential/statistical testing [vegan v2.6] -> stage not stated [SnpEff v5.1]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Version used: **4.2**
- Evidence: We used GATK 4.2 ( 46 ) HaplotypeCaller to produce gVCF files for the 50 individuals using the options - ERC BP_RESOLUTION, minimum mapping quality set to 30 and minimum base quality score set to 25.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### A trans-species cytoplasmic polymorphism is associated with seed shape and aridity across multiple species of sunflowers. (PNAS 2025)

- DOI: 10.1073/pnas.2410943122 | PMCID: PMC12337292 | PMID: 40720659
- Evidence: Variants were called using GATK HaplotypeCaller (v.4.0.1.2) in windows along the genome and then filtered using GATK’s VariantRecalibrator to retain SNPs above tranche = 90.0 ( 91 ).
- Full pipeline: read trimming [Trimmomatic v0.22] -> alignment/mapping [Trimmomatic v0.22] -> variant calling [GATK] -> stage not stated [BCFtools v1.10.2, IQ-TREE, SAMtools v1.10]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: Exome variants were called using the .fastq to .vcf framework available in GATK Best Practices ( 49 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### A preclinical pig model of Angelman syndrome mirrors the early developmental trajectory of the human condition. (PNAS 2025)

- DOI: 10.1073/pnas.2505152122 | PMCID: PMC12318228 | PMID: 40690672
- Evidence: Raw sequencing reads were quality-filtered using Trimmomatic v0.39, and alignments were generated for each sample following the GATK v3 Best Practices Workflow ( 67 ).
- Full pipeline: read trimming [GATK, Trimmomatic v0.39] -> alignment/mapping [GATK, Trimmomatic v0.39] -> stage not stated [IQ-TREE]

### Inference of human pigmentation from ancient DNA by genotype likelihoods. (PNAS 2025)

- DOI: 10.1073/pnas.2502158122 | PMCID: PMC12304992 | PMID: 40663601
- Evidence: For the probabilistic approach, we computed, for each of the 41 informative positions, the genotype likelihoods for each of the ten possible genotypes within the R environment v4.3.3 ( 19 ) applying the formula of the first version of GATK (dragon) ( 44 ).
- Full pipeline: alignment/mapping [SAMtools v1.11] -> variant calling [GATK]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Evidence: The GATK suite v3.3-0-g37228af was used for local indel realignment and base quality score recalibration ( 89 ).
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Evidence: We then used samtools v1.8 ( 72 ) to sort and index the alignments as well as to remove duplicates and GATK IndelRealigner v3.4.0 ( 73 ) to realign the reads mapped around indels.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### Homoploid hybridization adds clarity to the origins of octoploid strawberries. (PNAS 2025)

- DOI: 10.1073/pnas.2502814122 | PMCID: PMC12207424 | PMID: 40531871
- Evidence: SNPs and indels were called and filtered using GATK V4.4.0 ( 56 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [GATK, IQ-TREE, OrthoFinder, SAMtools]

### Population sequencing for phylogenetic diversity and transmission analyses. (PNAS 2025)

- DOI: 10.1073/pnas.2424797122 | PMCID: PMC12167970 | PMID: 40460116
- Evidence: The population reads underwent quality control and were preprocessed using the GATK Best Practices workflow ( 26 ) and were aligned against the MSHR1435 reference sequence [Accession Nos.
- Full pipeline: quality control [BWA v0.7.17, GATK, fastp v0.20.1] -> alignment/mapping [BWA v0.7.17, GATK, fastp v0.20.1] -> variant calling [BWA v0.7.17, fastp v0.20.1]

### &lt;i&gt;CACNA1D&lt;/i&gt; is a circadian gene and causes familial advanced sleep phase. (PNAS 2025)

- DOI: 10.1073/pnas.2424387122 | PMCID: PMC12167976 | PMID: 40460120
- Version used: **3.0**
- Evidence: Paired-end 125 bp reads were aligned to 1000 Genomes Phase 2 (GRCh37/hg19) human genome reference build using BWA-mem 0.7.8 and GATK 3.0.
- Full pipeline: alignment/mapping [GATK v3.0]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Evidence: We then used GATK HaplotypeCaller v4.1.4.1 ( 49 ) tool to call variants and snpEff 4.3t ( 50 ) to annotate them.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Version used: **3.7**
- Evidence: 1.96) and then realigned indels using GATK v.
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: We performed variant calling and filtering with the GATK software [v.3.7; ( 65 )], following GATK best practices ( 64 ).
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### A rare variant in &lt;i&gt;GPR156&lt;/i&gt; associated with depression in a Mennonite pedigree causes habenula hyperactivity and stress sensitivity in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2404754122 | PMCID: PMC12037005 | PMID: 40228124
- Evidence: Single nucleotide and indel variants and genotypes were called using GATK’s HaplotypeCaller.
- Full pipeline: variant calling [GATK]

### Biallelic variants in the conserved ribosomal protein chaperone gene &lt;i&gt;PDCD2&lt;/i&gt; are associated with hydrops fetalis and early pregnancy loss. (PNAS 2025)

- DOI: 10.1073/pnas.2426078122 | PMCID: PMC12012559 | PMID: 40208938
- Evidence: All the individual data from this family were combined, and SNVs and indels were called using GATK and annotated using AnnoVar.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> stage not stated [GATK, VEP v103.0, fastp v0.21.0]

### Genomic analysis of 11,555 probands identifies 60 dominant congenital heart disease genes. (PNAS 2025)

- DOI: 10.1073/pnas.2420343122 | PMCID: PMC12002227 | PMID: 40127276
- Version used: **3.7**
- Evidence: Variants were called using GATK v3.7 ( 72 ) using default parameters, disabling of variant quality score recalibration due to lack of training SNPs in the MIPseq panel; variants were also called with Freebayes v1.3.2 ( https://github.com/ekg/freebayes ) using default parameters.
- Full pipeline: alignment/mapping [ANNOVAR, BCFtools] -> variant calling [ANNOVAR, BCFtools] -> machine learning [GATK v3.7, freebayes]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Version used: **3.6**
- Evidence: 2.23.4 ( 111 ), and reads surrounding indels were realigned with GATK v3.6 ( 112 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Evidence: The GATK pipeline ( 55 ) was used to call individual SNPs and InDels.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Evidence: ( 15 , 85 , 86 ), using the Paleomix v1.2.13.4 ( 87 ) pipeline and GATK UnifiedGenotyper v3.7 ( 88 ).
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Version used: **2.3.9**
- Evidence: In summary, this assay consists of the following standard workflow: Reads are mapped using BWA MEM and indel-realigned and baseQ-recalibrated using GATK; then mutations are called using MuTect (v1.1.4) and SomaticIndelDetector (GATK v2.3.9).
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **3.7.0**
- Evidence: Clean reads were aligned to the Texas Marker-1 (TM-1) genome (CR1_v1: https://www.cottongen.org/node/13354433 ) ( 65 ) using BWA-MEM (v0.7.17-r1188 v0.7.17-r1188) ( 66 ), with variants called by GATK (v3.7.0) ( 67 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Ultrarapid MC1R protein and associated plumage color evolution in the domestic chicken. (PNAS 2026)

- DOI: 10.1073/pnas.2605288123 | PMCID: PMC13273276 | PMID: 42268884
- Version used: **3.7**
- Evidence: Local realignment around indels was performed with GATK (version 3.7; RealignerTargetCreator and IndelRealigner) ( 50 ), followed by base quality score recalibration (BQSR) using BaseRecalibrator and PrintReads to reduce systematic errors.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [BWA v0.7.17] -> registration [GATK v3.7] -> stage not stated [Picard v2.18.6, PyMOL, SAMtools v1.9, VCFtools v0.1.16]

### Ancient DNA from shells reveals delayed genomic erosion and rapid immune adaptation in the critically endangered black abalone. (PNAS 2026)

- DOI: 10.1073/pnas.2600483123 | PMCID: PMC13229213 | PMID: 42207912
- Evidence: Finally, we filtered these variant sites using GATK VariantFiltration (Van der Auwera et al.
- Full pipeline: read trimming [fastp] -> variant calling [SAMtools] -> stage not stated [GATK, IQ-TREE, R]

### Evolution of genome-wide barriers to gene flow during complex speciation in rattlesnakes. (PNAS 2026)

- DOI: 10.1073/pnas.2609058123 | PMCID: PMC13214041 | PMID: 42166239
- Evidence: We mapped filtered reads to the C. pyrrhus reference genome using BWA mem ( 121 ), and called variants using GATK ( 122 ).
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [BUSCO]

### Functional dissection of &lt;i&gt;SPOP&lt;/i&gt; at the amino acid level reveals a comprehensive functional landscape of variants during tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523210123 | PMCID: PMC13167761 | PMID: 42090249
- Evidence: Variants were called using AnalyzeSaturationMutagenesis in GATK ( 44 ), and the resulting variantCounts files used as per-variant count matrices.
- Full pipeline: read trimming [Cutadapt, minimap2] -> alignment/mapping [STAR, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> visualisation [PyMOL] -> stage not stated [DESeq2, GATK, R]

### Rhesus macaques with an &lt;i&gt;OPA1&lt;/i&gt; mutation demonstrate features of autosomal dominant optic atrophy. (PNAS 2026)

- DOI: 10.1073/pnas.2509165123 | PMCID: PMC13099570 | PMID: 41984835
- Evidence: Following the GATK pipeline, the single nucleotide variants (SNVs) and short insertion/deletions (indels) were called.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [ANNOVAR, GATK, ImageJ]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: VCFs for the CVI natural and intercross populations ( 27 , 35 ) were generated using GATK ( 59 , 60 ).
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: Following GATK Best Practices, GATK4 was used for duplicate marking, and Strelka2 was applied for variant calling using matched normal liver tissue as control ( 57 – 59 ).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Ultrapotent antibodies against diverse and highly transmissible SARS-CoV-2 variants. (Science 2021)

- DOI: 10.1126/science.abh1766 | PMCID: PMC9269068 | PMID: 34210892
- Version used: **4.1.9.0**
- Evidence: Single nucleotide polymorphisms (SNPs) were called using HaplotypeCaller from the Genome Analysis Tool Kit (GATK, v4.1.9.0).
- Full pipeline: variant calling [GATK v4.1.9.0] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, UCSF Chimera]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Evidence: Variant calling was performed using default GATK HaplotypeCaller (Version 4.1.8.1), and variants were inspected in bam.files using IGV.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### The contribution of historical processes to contemporary extinction risk in placental mammals. (Science 2023)

- DOI: 10.1126/science.abn5856 | PMCID: PMC10184782 | PMID: 37104572
- Evidence: Estimating historical effective population sizes and genome-wide heterozygosity We called heterozygous positions in all genomes with short-read data using the GATK best practices pipeline as described previously( 7 ).
- Full pipeline: alignment/mapping [BWA v0.7.15] -> variant calling [BWA v0.7.15] -> differential/statistical testing [R] -> stage not stated [GATK, SnpEff v5.0e, scikit-learn v1.0.2]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Version used: **3.5**
- Evidence: Whole-genome sequencing analysis and annotation of variants Raw sequencing reads were aligned to the P. falciparum 3D7 reference genome (PlasmoDB v13.0) and pre-processed following standard GATK version 3.5 protocols ( 13 ).
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

### Somatic mosaicism in schizophrenia brains reveals prenatal mutational processes. (Science 2024)

- DOI: 10.1126/science.adq1456 | PMCID: PMC11490355 | PMID: 39388546
- Evidence: Briefly, fastq files were aligned to the GRCh37 reference genome using bwa v0.7.17 ( 50 ), and preprocessed using the GATK best practices.
- Full pipeline: alignment/mapping [GATK] -> normalisation [DESeq2] -> stage not stated [PLINK, R]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Evidence: Then, duplicate reads were marked by MarkDuplicates of Picard (v.2.8.0), followed by local Indel realignment and base quality score recalibration using Genome Analysis Toolkit (GATK) (v.3.5) ( 45 ) to generate BAM files for mutation calling.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Evidence: Reads were adaptor- and quality-trimmed using Trim Galore!( 69 ) (v0.6.5) and aligned to the GATK Genome Reference Consortium Human Build 38 (GRCh38)( 70 ) using bwa-mem (v0.7.17)( 71 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Microglia Rank signaling regulates GnRH neuronal function and the hypothalamic-pituitary-gonadal axis. (Science 2026)

- DOI: 10.1126/science.aeb6999 | PMCID: PMC7619046 | PMID: 41818388
- Evidence: We used an in-house pipeline to analyze the raw sequences (FASTQ files) that utilized the Burrows-Wheeler Alignment algorithm (BWA) ( 73 ) for mapping the reads to the human reference sequence (GRCh38) and the Genome Analysis Toolkit (GATK) ( 74 ) to detect single nucleotide variants (SNVs) and insertion/deletions.
- Full pipeline: quality control [FastQC, STAR v2.7.1] -> alignment/mapping [FastQC, GATK, STAR v2.7.1] -> normalisation [FastQC, STAR v2.7.1] -> dimensionality reduction/clustering [FastQC, ImageJ, STAR v2.7.1, UMAP] -> stage not stated [GSEA, Seurat]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Evidence: In those with CHIP mutations at baseline, rs17834140 genotypes were extracted using GATK’s HaplotypeCaller ( 91 ).
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

