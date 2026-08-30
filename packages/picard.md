# Picard

- **Category:** genomics
- **Papers in survey:** 289
- **Journals:** Nature (144), PNAS (119), Cell (19), Science (7)
- **Years:** 2021 (36), 2022 (44), 2023 (46), 2024 (66), 2025 (66), 2026 (31)
- **Versions named:** 2.2.4 (4), 2.9.4 (3), 2.23.4 (3), 2.18.7 (2), 2.27.4 (2), 2.18.14 (2), 2.18.26 (2), 1.119 (2), 3.0.0 (2), 2.25.0 (2)
- **Pipeline stages it appears in:** alignment/mapping (93), read trimming (28), registration (14), variant calling (10), quality control (8), differential/statistical testing (4), dimensionality reduction/clustering (2), quantification (2), visualisation (1), normalisation (1), structure determination (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: Duplicated reads were removed by the mark duplicates function with Picard.
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Microenvironment drives cell state, plasticity, and drug response in pancreatic cancer. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.017 | PMCID: PMC8822455 | PMID: 34890551
- Evidence: Data were analyzed using the Broad Picard pipeline which includes de-multiplexing and data aggregation ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [RSEM] -> alignment/mapping [GATK v1.6] -> registration [GATK v1.6] -> differential/statistical testing [R v4.0] -> stage not stated [Mutect2 v1.1.45, Picard, Python v3.7.4, Seurat v2.3.4]

### The monoclonal antibody combination REGEN-COV protects against SARS-CoV-2 mutational escape in preclinical and human studies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.002 | PMCID: PMC8179113 | PMID: 34161776
- Evidence: ..., 2018 https://github.com/lh3/minimap2 Swiftbiosciences primerclip software (v0.3.8) Swift Biosciences https://github.com/swiftbiosciences/primerclip Picard package Broad Institute https://github.com/broadinstitute/picard samtools (v1.9) Li et al., 2009 http://www.htslib.org GATK HaplotypeCaller (v4.1.8) Broad Insitute https://gatk.broadinstitute.org/hc/en-us/articles/360036194592-Getting-started-...
- Full pipeline: variant calling [GATK, Picard, SAMtools v1.9] -> stage not stated [PHENIX v1.19.1, PyMOL, minimap2]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Evidence: ...2.5.5 Schliep, 2011 https://cran.r-project.org/web/packages/phangorn/index.html PhyML v3.1 Guindon et al., 2010 http://www.atgc-montpellier.fr/phyml/ Picard tools v2.9.0 Broad Institute http://broadinstitute.github.io/picard/ PLINK 1.9 Purcell et al., 2007 https://zzz.bwh.harvard.edu/plink/plink2.shtml popHelper Francis, 2017 http://pophelper.com/ Samtools v.
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...celm/cutadapt FastQC Andrews, 2010 https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ BWA Li and Durbin, 2010 http://bio-bwa.sourceforge.net/ Picard MarkDuplicates http://broadinstitute.github.io/picard http://broadinstitute.github.io/picard MapDamage2.0 Jónsson et al., 2013 https://ginolhac.github.io/mapDamage/ ANGSD Korneliussen et al., 2014 https://github.com/ANGSD/angsd READ Monroy Kuh...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Version used: **1.81**
- Evidence: ...heeler Aligner (BWA) v0.7.15 Li and Durbin, 2009 http://bio-bwa.sourceforge.net/ Samtools v1.3.1 Li and Durbin, 2009 http://samtools.sourceforge.net/ Picard 1.81 N/A http://broadinstitute.github.io/picard/ Mutect v1.1.7 Cibulskis et al., 2013 https://software.broadinstitute.org/cancer/cga/mutect VarScan v2.4.1 Koboldt et al., 2012 http://varscan.sourceforge.net/ Annovar Wang et al., 2010 http://an...
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Evidence: ...ntific-software/prism/ MACS2 Zhang et al., 2008 N/A PoolQ version 3.2.9 Broad Institute https://portals.broadinstitute.org/gpp/public/software/poolq/ Picard Tools v2.9.0 Broad Institute http://broadinstitute.github.io/picard/ STAR aligner v2.7.3a Dobin et al., 2013 N/A SAMTools v1.9 Li et al., 2009 N/A Trimmomatic v0.39 Bolger et al., 2014 N/A CRISPR screen analysis This paper https://github.com/P...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **2.4.1**
- Evidence: (2019) https://github.com/Illumina/paragraph Picard v2.4.1 Van der Auwera and O'Connor (2020) https://broadinstitute.github.io/picard/index.html Plink v1.90 and v2.0 Chang et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### From rare disorders of immunity to common determinants of infection: Following the mechanistic thread. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.004 | PMCID: PMC9386946 | PMID: 35985287
- Evidence: A few are explained by mutations of a few genes that, individually, never account for more than 1% of cases (e.g., invasive pneumococcal or staphylococcal disease in patients with IRAK4 or MyD88 deficiency; Picard et al., 2010 ).
- Full pipeline: stage not stated [Picard]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...s and Wang, 2020 ) https://github.com/stschiff/msmc-tools phy-mer ( Navarro-Gomez et al., 2015 ) https://github.com/MEEIBioinformaticsCenter/phy-mer/ Picard-tools - version 2.9 Broad Institute http://broadinstitute.github.io/picard/ R - version 4.0, 3.7, and 3.6.1 R Core Team (2019) .
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ... Embedded in Fragpipe Perseus 1.6.14.0 ( Tyanova and Cox, 2018 ) https://maxquant.net/perseus/ Philosopher ( da Veiga Leprevost et al., 2020 ) v3.2.9 Picard http://broadinstitute.github.io/picard/ v2.23 https://github.com/broadinstitute/picard prcomp v3.6.2 https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/prcomp Priority Index (Pi) ( Fang et al., 2016a ) http://galahad.well.ox.a...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: 81 https://imagej.nih.gov/ij/ R The Comprehensive R Archive Network https://cran.r-project.org/ Python Python Programming Language https://www.python.org/ BWA Li and Durbin 82 http://bio-bwa.sourceforge.net/bwa.shtml Picard Tools Broad Institute https://broadinstitute.github.io/picard Samtools Li et al.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: Reads were aligned to reference genome (mm10) using Bowtie2 (version 2.2.9) and deduplicated with Java (version 2.3.0) Picard tools ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: 92 https://iupred2a.elte.hu/ PSIPRED Jones 93 http://bioinf.cs.ucl.ac.uk/psipred/ BWA-MEM 0.7.17-r1188 N/A https://github.com/lh3/bwa Picard tool 2.9.0 Broad Institute of MIT and Harvard https://broadinstitute.github.io/picard FreeBayes 1.1.0-3 N/A https://github.com/freebayes/freebayes isobarQuant Franken et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Evidence: 70 http://www.htslib.org/ Picard MarkDuplicates v2.26.10 “Picard Toolkit.” 2019.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Evidence: This paper https://github.com/SinghLabUCSF/Diapause-multiomics Picard Tools v2.22.1 Broad Institute https://broadinstitute.github.io/picard/ SnapGene v7.0 Dotmatic https://www.snapgene.com/ TrimGalore v0.4.1 Felix Krueger https://www.bioinformatics.babraham.ac.uk/projects/trimgalore/ Fiji v2.0.0-rc-68/1.52h FijiTeam https://fiji.sc/ Ingenuity Pathway Analysis (IPA) QIAGEN https://digitalinsights.q...
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Evidence: GATK’s Haplotype Caller from the Genome Analysis Toolkit (GATK version 3.6) 104 SAMtools 105 , and Picard tools were used for variant calling.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Evidence: 97 https://github.com/MikkelSchubert/adapterremoval BWA v0.7.17 Li and Durbin 98 https://github.com/lh3/bwa Picard tools v2.24 Broad Institute https://broadinstitute.github.io/picard/ Samtools v1.11.0 Li et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Evidence: Duplicate reads were identified and removed using Picard MarkDuplicates [Picard Toolkit, Broad Institute, http://broadinstitute.github.io/picard/(2021 ) ].
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Version used: **2.23.4**
- Evidence: Duplicated reads were removed by Picard (version 2.23.4).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: The filtered bam files from split and unsplit R1 and R2 reads were deduplicated with Picard and merged into a single bam file to generate the methylation data.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: For haplogroup identification, reads were mapped to the human mtDNA reference genome (rCRS) 65 and duplicates were removed using Picard MarkDuplicates v.2.18.2 ( https://broadinstitute.github.io/picard ), followed by a left alignment to normalize indels.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Duplicates were marked with Picard tools (v2.20.4) 48 BAM files were recalibrated for base quality scores using Genome Analysis Toolkit (GATK v4.1.3) 49 Base Recalibrator.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Million-year-old DNA sheds light on the genomic history of mammoths. (Nature 2021)

- DOI: 10.1038/s41586-021-03224-9 | PMCID: PMC7116897 | PMID: 33597750
- Evidence: The Picard Liftover tool (‘Picard Toolkit’, 2019) was then used to lift over the identified variants to the LoxAfr3 reference.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.921, BCFtools, Picard, RepeatMasker v4.0.7, SAMtools v1.10]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Evidence: BAM files were then sorted and indexed with samtools v1.11 and PCR optical duplicates removed using Picard ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: The duplicate reads at same locations were removed by MarkDuplicates of Picard package ( broadinstitute.github.io/picard , 2.23.8).
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: The resulting .bam file was filtered for duplicates using Picard ( http://broadinstitute.github.io/picard ) and realigned around indels using GATK 3.0 56 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### A genetic history of the pre-contact Caribbean. (Nature 2021)

- DOI: 10.1038/s41586-020-03053-2 | PMCID: PMC7864882 | PMID: 33361817
- Evidence: Duplicate molecules (those exhibiting the same mapped start and end position and same stand orientation) were removed after alignment using the Broad Institute’s Picard MarkDuplicates tool (available at http://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard] -> structure determination [BWA v0.7.15] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.3.1, SAMtools]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Picard’s MarkDuplicates command (version 2.18.27) was used to remove sequence duplicates (settings: remove_duplicates=TRUE, http://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: We used MarkDuplicates from Picard ( https://github.com/broadinstitute/picard ) to remove duplicates and then we calculated the mapping statistics for each SMAG in the BAM files with the filterBAM program ( https://github.com/aMG-tk/bam-filter ).
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **2.3.0**
- Evidence: The aligned reads were de-duplicated with Picard (v.2.3.0; Broad Institute, 2019) and shifted to correct for Tn5 insertion bias.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: Picard tools (v2.5.0) was used with the resulting BAM files to collect various read quality measures, in addition to the quality measures collected by STAR. verifyBAMID 49 was also used with these BAM files along with known sample genotypes from Parikshak et al.
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **2.5.0**
- Evidence: Read groups were added with Picard v2.5.0 ( http://broadinstitute.github.io/picard ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### The Anglo-Saxon migration and the formation of the early English gene pool. (Nature 2022)

- DOI: 10.1038/s41586-022-05247-2 | PMCID: PMC9534755 | PMID: 36131019
- Evidence: PCR duplicates were identified by tagging all aligned sequences with the same start and stop positions and orientation and, in some cases, in-line barcodes using Picard MarkDuplicates ( http://broadinstitute.Github.io/picard/ ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA, Picard] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, SAMtools]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Evidence: Reads from these genomes were mapped to the dog reference genome using bwa mem (version 0.7.15) 70 , marked for duplicates using Picard Tools (v2.21.4) ( http://broadinstitute.github.io/picard ), genotyped at the sites present in the above dataset using GATK HaplotypeCaller (v3.6) 71 with the ‘-gt_mode GENOTYPE_GIVEN_ALLELES’ argument and then merged into the dataset using bcftools merge ( http://...
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Evidence: We performed concatenation using the SAMtools ‘merge’ command and with the AddOrReplaceReadGroups tool in Picard ( http://broadinstitute.github.io/picard/ ) for assigning a single read group to all reads in each new file.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Duplicate reads were removed using Picard ( http://broadinstitute.github.io/picard/ ) MarkDuplicates (REMOVE_DUPLICATES = true).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **2.21.4**
- Evidence: Indel realignment and marking of duplicates were performed using Picard (v.2.21.4, http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Evidence: PCR duplicates were removed using MarkDuplicates from Picard Tools (2.23.0) using the command ‘MarkDuplicates REMOVE_DUPLICATES=true CREATE_INDEX=true’.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Extensive quality control was performed using SAMtools 58 and Picard Tools 59 to confirm sex and tissue of origin.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: After removing duplicates using Picard tools, gene counts were generated with htseq 40 .
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **2.17.0**
- Evidence: The performance of the library preparation as well as the quality of the sequencing data, target coverage metrics within exonic regions specified by the Nextera target BED file obtained from Illumina (Manifest version 1.2) were generated using Picard (version 2.17.0) CalculateHSMetrics.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Version used: **3.0.0**
- Evidence: 63 ), v.2.3); (4) BAM file processing and QC (samtools 64 , v.1.9; Picard, v.3.0.0); (5) methylome profile generation (allcools, v.1.0.8); and (6) chromatin contact calling (snm3C-seq only).
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Evidence: Duplicated reads were also marked using Picard MarkDuplicates (v.1.65; https://broadinstitute.github.io/picard/ ) and filtered out.
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Version used: **2.23.0**
- Evidence: Duplicates were removed with Picard version 2.23.0 ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **2.9.4**
- Evidence: Duplicated reads were then marked using Picard (v.2.9.4) and only non-duplicated proper paired reads were kept according to SAMtools (parameter ‘-q 1 -F 1804’ v1.9).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Integrated global assessment of the natural forest carbon potential. (Nature 2023)

- DOI: 10.1038/s41586-023-06723-z | PMCID: PMC10700142 | PMID: 37957399
- Evidence: Picard, M.T.F.P., D.P., N.C.A.P., A.D.P., J.R.P., H.P., F.R.A., Z.R.-C., M.R., S.G.R., A.R., F.R., E.R., P.
- Full pipeline: stage not stated [Picard, R]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Version used: **2.6.26**
- Evidence: BAM files were sorted and duplicates were marked using the Picard v.2.6.26 SortSam tool with the following parameters: CREATE_INDEX=true, SORT_ORDER=coordinate, VALIDATION_STRINGENCY = STRICT, and all others set to default; and MarkDuplicates with the parameter REMOVE_DUPLICATES=true, and all others set to default.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Evidence: The mean read insert sizes and their standard deviations were calculated using Picard tools (v.2.18.20).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Evidence: ...thub.com/GregoryFaust/samblaster ), BWA (v0.7.10 mem, https://github.com/lh3/bwa ), GenomeAnalysisTKLite (v2.3.9, https://github.com/broadgsa/gatk ), Picard tools (v1.117, https://broadinstitute.github.io/picard ), Bedtools (v2.25.0-76-g5e7c696z, https://github.com/arq5x/bedtools2 ), Variant Effect Predictor (release 100, https://github.com/Ensembl/ensembl-vep ), BOLT-LMM (v2.1, https://data.broad...
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: Reads were mapped to the mouse reference GRCm38 with the Broad Picard Pipeline ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Long-molecule scars of backup DNA repair in BRCA1- and BRCA2-deficient cancers. (Nature 2023)

- DOI: 10.1038/s41586-023-06461-2 | PMCID: PMC10482687 | PMID: 37587346
- Evidence: Read post-processing was done in accordance with best practices for post-alignment data processing with Picard tools ( https://broadinstitute.github.io/picard/ ) to mark duplicates, the GATK (v.2.7.4) ( https://gatk.broadinstitute.org/hc/en-us ) IndelRealigner module and GATK base quality recalibration.
- Full pipeline: alignment/mapping [BWA, Picard] -> variant calling [GATK] -> registration [Picard] -> stage not stated [R, SnpEff]

### R-loop-dependent promoter-proximal termination ensures genome stability. (Nature 2023)

- DOI: 10.1038/s41586-023-06515-5 | PMCID: PMC10511320 | PMID: 37557913
- Evidence: All unmapped reads, low mapping quality reads (MAPQ < 30) and PCR duplicates were removed using SAMtools (v.1.12) 59 and the MarkDuplicates function of Picard Tools v.2.25.5 (Broad Institute).
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [Picard, SAMtools v1.12] -> quantification [Trim Galore v0.6.6] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [Trim Galore v0.6.6] -> stage not stated [ImageJ, MACS2 v2.2.7.1, R]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Duplicated reads were marked and read groups were assigned using the Picard tools ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **2.9.4**
- Evidence: Resulting BAM files were filtered to remove duplicated reads (marked by Picard (version 2.9.4)) and to remove mitochondrial reads.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Version used: **2.5.0**
- Evidence: The resulting BAM files were further analysed and recalibrated with Picard (v.2.5.0) 51 and the GATK toolkit (v.4.0.0.0) 52 .
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: PCR duplicates were identified using the MarkDuplicates function from Picard tools.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Version used: **2.8.0**
- Evidence: We used Samtools (v1.3.1) 53 to merge the realigned bam fragments and Picard (v2.8.0) to add read groups and to mark PCR duplicates.
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### Widespread somatic L1 retrotransposition in normal colorectal epithelium. (Nature 2023)

- DOI: 10.1038/s41586-023-06046-z | PMCID: PMC10191854 | PMID: 37165195
- Evidence: Duplicated reads were removed by either Picard (available at http://broadinstitute.github.io/picard ) or SAMBLASTER 61 .
- Full pipeline: read trimming [Bismark] -> alignment/mapping [BWA, Bismark, minimap2] -> stage not stated [Cutadapt, DELLY, Picard]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Evidence: Alignments were performed separately for each lane of sequencing and then merged from the same patient region using Sambamba (v.0.7.0) 43 and deduplicated using Picard Tools (v.2.21.9, http://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: Duplicate reads were removed using Picard Tools (v.2.3.0; http://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Version used: **2.26.9**
- Evidence: Samtools 47 (version 1.9) and Picard (version 2.26.9; http://broadinstitute.github.io/picard/ ) were used to sort, deduplicate and index the alignments, and to create a depth file, which was plotted using a custom script in R.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Evidence: A post-mapping step removed any reads mapping to multiple regions of the genome as well as duplicated reads using Picard MarkDuplicates 2.7.1.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: Duplicate reads were marked with Picard/2.8.0 with the command java -jar $PICARD/picard-2.8.0.jar MarkDuplicates REMOVE_DUPLICATES=false.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: PCR duplicates were removed using the Picard MarkDuplicates program with parameter REMOVE_DUPLICATES=True.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Evidence: Reads were trimmed of adapter content with Trimmomatic 60 (v.0.39), aligned to the hg19 genome using BWA MEM 61 (0.7.17-r1188) and PCR duplicates were removed using Picard’s MarkDuplicates (v.2.25.3).
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Trimmed reads were aligned to GRCm39 Ensembl release 103 for quality control purposes using STAR version 2.7.7a 63 and quality control of the aligned reads was carried out using Picard tools (v2.27.3).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **2.2.4**
- Evidence: Picard (v2.2.4, RRID: SCR_006525 ) was used to remove duplicates (Picard Toolkit 2019).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Version used: **2.6.26**
- Evidence: BAM files were sorted and duplicates were marked using Picard (v.2.6.26) SortSam tool with the following parameters: CREATE_INDEX=true, SORT_ORDER=coordinate, VALIDATION_STRINGENCY=STRICT, and all others set to default; and MarkDuplicates with parameter REMOVE_DUPLICATES=true, and all others set to default.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: All aligned reads were merged into BAM using the Picard SortSam tool with query names sorted.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: Mapped reads were deduplicated using the Picard tool MarkDuplicates (v.2.26.2; http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Alignments were filtered to remove duplicate reads with Picard MarkDuplicates v.2.24.0 ( http://broadinstitute.github.io/picard/ ) and improper alignments with Samtools view v.1.11 -F 260 -f 3 (ref.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Evidence: PCR duplicates were removed using Picard tools v.3.1.1 ( https://picard.sourceforge.net/ ).
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Evidence: ...containing all alternate contigs) 55 ; (2) alignment reads were sorted by sort mode of Sentieon utility functions; (3) duplicate reads were marked by Picard ( http://broadinstitute.github.io/picard/ ); (4) indel realignment and base quality score recalibration for aligned reads were carried out by GATK 56 ; (5) and alignment quality control was done by Picard.
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Evidence: Downstream processing was done using the Genome Analysis Toolkit (GATK, v.3.4), SAMtools (v.1.0) and Picard Tools ( http://picard.sourceforge.net ; v.1.92).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: Picard ( http://broadinstitute.github.io/picard/ ) was used to remove duplicates.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Evidence: The resulting BAM files were merged at sample level (Supplementary Table 2 ), and duplicates were identified using MarkDuplicates (v.2.27.4) from Picard Tools.
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **2.20.3**
- Evidence: Non-unique mapped and duplicated reads were excluded using SAMtools (v1.9) 44 and Picard (v2.20.3-SNAPSHOT; http://picard.sourceforge.net ), respectively.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **2.23.8**
- Evidence: Data from multiple lanes were merged before deduplication; duplicates were marked using Picard (v2.23.8) 75 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Alignments were filtered using Samtools (v.1.12) with a mapping quality threshold of 37, and duplicates were removed using Picard MarkDuplicates with default parameters ( http://broadinstitute.github.io/picard/ ) 66 .
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Picard was used to mark unmapped reads and SAMtools to remove these, re-sort and re-index.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: Duplicated reads were removed using the MarkDuplicates command of Picard Tools (v.2.18.23; https://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **2.21.6**
- Evidence: Samtools (v.1.9) 93 was then used to sort the aligned reads and Picard (v.2.21.6) 94 was used to remove redundant reads.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Evidence: Reads were aligned to M. musculus refence genome (mm10) using bwa mem (BWA-0.7.17) 81 before filtering with samtools (v.1.10) 82 view with the flags ‘-h -F 256 -f 2 -q 30’ and deduplicated with Picard toolkit (v.2.9.0) MarkDuplicates 83 .
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Network of large pedigrees reveals social practices of Avar communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07312-4 | PMCID: PMC11078744 | PMID: 38658749
- Evidence: We then used the Picard tools MarkDuplicates function ( https://github.com/broadinstitute/picard ) to remove PCR duplicates.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [BCFtools v1.3, Cytoscape v3.9.1, Picard, igraph]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Version used: **1.119**
- Evidence: 90 ), and Picard v.1.119 ( https://github.com/broadinstitute/picard ) was used to add read group data and mark PCR duplicates.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: SAMtools was used to identify uniquely aligned reads, and Picard was used to remove duplicate reads.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: In brief, the raw, filtered read libraries were converted to sorted BAM files using Picard tools ( http://broadinstitute.github.io/picard ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### Genomic data in the All of Us Research Program. (Nature 2024)

- DOI: 10.1038/s41586-023-06957-x | PMCID: PMC10937371 | PMID: 38374255
- Evidence: Picard GtcToVcf is used to convert the GTC files to VCF format.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [REGENIE] -> stage not stated [Picard]

### IL-10 constrains sphingolipid metabolism to limit inflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07098-5 | PMCID: PMC10954550 | PMID: 38383790
- Evidence: After sorting the generated SAM files (as the output of alignment) with Picard Toolkit ( https://broadinstitute.github.io/picard/ ; Broad Institute), we counted the number of reads mapped to each gene using HTSeq 69 v0.6.1.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HTSeq, Picard] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v4.3.0]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **2.92**
- Evidence: The PCR duplicates were removed using Picard (v2.92) and SAMtools (v1.2) software 39 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Reads were aligned to human assembly hg19 with version 2.3.4.1 of bowtie2 ( http://bowtie-bio.sourceforge.net/bowtie2/index.shtml ) and MarkDuplicates of Picard Tools version 2.16.0 was used for deduplication.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Evidence: CleanSam, from Picard Toolkit version 2.18.29 ( http://broadinstitute.github.io/picard ), was used to clean the provided SAM or BAM files.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Version used: **1.127**
- Evidence: Mapped reads were filtered for mapping quality 30 and sorted using Picard (v.1.127) ( http://picard.sourceforge.net ) and SAMtools 78 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Evidence: Paired- and single-end reads for each library and lane were merged, and duplicates were marked using Picard MarkDuplicates (v2.18.26; http://picard.sourceforge.net ) with a pixel distance of 12,000.
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Evidence: Duplicate reads were removed using samtools 45 , awk scripts and Picard tools (Broad Institute).
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: PCR duplicate reads were identified with Picard and removed with SAMtools.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: Demultiplexing of raw reads was performed by bcl2fastq V3, and trimming, quality control, alignment to the ME49 reference genome (using bwa2) and duplicate read merging (using Picard) were carried out by the nf-core ATAQ-SEQ pipeline 47 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### GDF15 linked to maternal risk of nausea and vomiting during pregnancy. (Nature 2024)

- DOI: 10.1038/s41586-023-06921-9 | PMCID: PMC10808057 | PMID: 38092039
- Evidence: Briefly, the pipeline comprises the following steps: (1) marking duplicate reads using ‘markDuplicate’ of Picard ( https://broadinstitute.github.io/picard/ ), (2) splitting reads that contain ‘N’s in their CIGAR string using ‘splitNRead’ of GATK (subsequent submodules from GATK hereafter), (3) realignment of reads around the indel using ‘IndelRealigner’, (4) recalibrating base quality using ‘BaseR...
- Full pipeline: alignment/mapping [GATK] -> variant calling [BCFtools, SAMtools] -> quantification [BCFtools, SAMtools, lme4] -> registration [Picard] -> stage not stated [PLINK v1.90b, R]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **2.2.4**
- Evidence: Picard (v.2.2.4) was used to remove duplicated reads.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **1.119**
- Evidence: Sequencing analysis and mutation calling were performed as described 45 , using the following tools: Python v.2.7.18, TrimGalore v.0.4.1, BWA v.0.7.13, Samtools v.1.9, Picard v.1.119, GenomeAnalysisTK v.3.5, Bcftools v.1.9, and tabix v.0.2.6.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: These in silico rRNA-depleted reads were then remapped to the main reference, sorted with SAMtools (v.1.2) 61 and passed to Picard ( https://broadinstitute.github.io/picard/ , v.3.1.1) to mark duplicates.
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: Sequencing duplicates were marked and removed using Picard implemented in the Genome Analysis Toolkit (GATK4) 68 .
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **3.0.0**
- Evidence: The PCR duplicates were removed using Picard v.3.0.0 ( http://broadinstitute.github.io/picard/index.html ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Redox-driven mineral and organic associations in Jezero Crater, Mars. (Nature 2025)

- DOI: 10.1038/s41586-025-09413-0 | PMCID: PMC12422973 | PMID: 40931152
- Evidence: Peer review Peer review information Nature thanks Janice Bishop, Aude Picard and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.
- Full pipeline: stage not stated [Picard]

### Single-cell transcriptomic and genomic changes in the ageing human brain. (Nature 2025)

- DOI: 10.1038/s41586-025-09435-8 | PMCID: PMC12527935 | PMID: 40903571
- Evidence: PCR duplicates were then filtered using Picard, and the remaining reads were recalibrated with GATK BaseRecalibrator and ApplyBQSR.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Cellpose, GATK v4.1.8.1, Picard, Seurat]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: Picard tools MarkDuplicate was then used to remove all PCR and optical duplicated reads from the BAM file.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Evidence: List of software and respective versions: AdapterRemoval (v.2.3.1), Burrows–Wheeler Aligner (v.0.7.12), DeDup (v.0.12.2), mapDamage (v.2.0.6), BamUtil (v.1.0.14), EAGER (v.1), Picard tools (v.2.27.3), Sex.DetERRmine (v.1.1.2) ( https://github.com/TCLamnidis/Sex.DetERRmine ), ANGSD (v.0.915), Schmutzi (v.1.5.4), PMDtools (v.0.50), pileupCaller (v.1.4.0.2), samtools (v.1.3.1), Geneious (R9.8.1), Hap...
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: 77 ) (v.2.3.5.1) and were deduplicated using MarkDuplicates from Picard (Broad Institute; v.2.16).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Version used: **2.1.1**
- Evidence: The resulting BAM files were sorted, duplicates marked and indexed using Picard (v2.1.1).
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **2.21.8**
- Evidence: PCR duplicates were removed using Picard (v.2.21.8) MarkDuplicates REMOVE_DUPLICATES=true VALIDATION_STRINGENCY = LENIENT.
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Complete biosynthesis of salicylic acid from phenylalanine in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09175-9 | PMCID: PMC12408352 | PMID: 40702181
- Evidence: Alignments were sorted with SAM tools (v.1.6) and duplicates were marked with Picard Tools (v.2.27.5+dfsg).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.526, Picard, RAxML v8.2.12] -> stage not stated [InterProScan v5.69]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Version used: **2.27.4**
- Evidence: PCR duplicates were marked using Picard v.2.27.4 with the MarkDuplicates tool, and alignment metrics were computed for each cell with the Picard tools CollectWgsMetrics and CollectInsertSizeMetrics.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: Duplicates were removed using the MarkDuplicates (v.3.1.1.0) function from Picard.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: The resulting alignments were sorted with Sambamba and duplicate reads were marked using Picard.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **2.27.1**
- Evidence: Reads were assigned using Picard (v.2.27.1) and the AddOrReplaceReadGroups tool.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Sequence diversity lost in early pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-025-09031-w | PMCID: PMC12176622 | PMID: 40399685
- Evidence: In brief, reads were aligned with BWA mem 52 (v.0.7.10) and marked for duplicates with Picard tools (v.1.117).
- Full pipeline: alignment/mapping [BWA, Picard, R] -> variant calling [Manta v1.6.0] -> differential/statistical testing [R] -> machine learning [ADMIXTURE] -> stage not stated [PLINK, VEP]

### Emergence of Calabi-Yau manifolds in high-precision black-hole scattering. (Nature 2025)

- DOI: 10.1038/s41586-025-08984-2 | PMCID: PMC12078182 | PMID: 40369139
- Evidence: The choice of I 1 ensures that its third-order differential (Picard–Fuchs) equation ( θ ^ = x d d x ), 13 [ θ ^ 3 − 2 x 2 ( 2 + 4 θ ^ + 3 θ ^ 2 + θ ^ 3 ) + x 4 ( 2 + θ ^ ) 3 ] I 1 ∣ ϵ = 0 = 0 , has the explicit solution I 1 ∣ ϵ = 0 ∝ ϖ K3 = 2 π 2 K 2 ( 1 − x 2 ) , that is, it is proportional to a K3 period.
- Full pipeline: differential/statistical testing [Picard]

### Targeting the SHOC2-RAS interaction in RAS-mutant cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-08931-1 | PMCID: PMC12137120 | PMID: 40335703
- Evidence: Picard, K.
- Full pipeline: differential/statistical testing [DESeq2, edgeR] -> stage not stated [Picard, R, fgsea, ggplot2 v3.3.6, ggpubr v0.4.0]

### Picuris Pueblo oral history and genomics reveal continuity in US Southwest. (Nature 2025)

- DOI: 10.1038/s41586-025-08791-9 | PMCID: PMC12137115 | PMID: 40307544
- Version used: **2.25.0**
- Evidence: 103 ), optical duplicates were marked using Picard v.2.25.0 and depth of coverage and average read length estimated using pysam v.0.22.1.
- Full pipeline: quality control [ANGSD v0.931] -> variant calling [BCFtools v1.17] -> stage not stated [ADMIXTURE, BEAST v2.6, Picard v2.25.0, SAMtools v1.3.1]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **2.20.3**
- Evidence: Unmapped, non-unique and duplicated reads were filtered out using SAMtools 64 , 65 (v.1.9) and Picard (v.2.20.3-SNAPSHOT) before variants were called by a standard pipeline of Genome Analysis Toolkit (GATK 65 v.4.1.2) and Sentieon 66 (v.202112.01).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Read duplicates were removed using Picard MarkDuplicates 2.26.0 ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Histone H1 deamidation facilitates chromatin relaxation for DNA repair. (Nature 2025)

- DOI: 10.1038/s41586-025-08835-0 | PMCID: PMC12074999 | PMID: 40240600
- Evidence: Duplicate reads were removed using the Picard tool.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.4, SAMtools] -> stage not stated [AlphaFold, ImageJ, Picard, PyMOL, deepTools v3.5.5]

### PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens. (Nature 2025)

- DOI: 10.1038/s41586-025-08982-4 | PMCID: PMC12176658 | PMID: 40228524
- Evidence: Sequences were mapped to the mouse genome (mm10) with bowtie2 (2.2.3), filtered based on mapping score (MAPQ > 30, Samtools (0.1.19)), and duplicates were removed (Picard).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.3, Picard, SAMtools v0.1.19] -> normalisation [Seurat v5.1] -> dimensionality reduction/clustering [Seurat v5.1, UMAP] -> stage not stated [Signac v1.14]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **2.9.4**
- Evidence: Duplicated reads were flagged using Picard (v.2.9.4) and only unique, properly paired reads were retained using SAMtools (with the parameters ‘-q 1 -F 1804’; v.1.9).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **3.2.0**
- Evidence: For the analysis of the transcriptional switch time courses, reads were mapped with bwa-mem 61 (v.0.7.17) and PCR duplicates were filtered out with Picard (v.3.2.0) ‘MarkDuplicates’ function.
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: ...nome GRCh38 (v1.4.4), provided by the Genome Reference Consortium ( https://www.ncbi.nlm.nih.gov/grc ), mapped reads were marked for duplicates using Picard Markduplicates (v4.2.6.1), and read base-quality scores were recalibrated using GATK BaseRecalibrator (v4.2.6.1) and GATK ApplyBQSR (v4.2.6.1) 54 .
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **2.2.4**
- Evidence: PCR duplicates were also removed using Picard (v.2.2.4).
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Tumour-wide RNA splicing aberrations generate actionable public neoantigens. (Nature 2025)

- DOI: 10.1038/s41586-024-08552-0 | PMCID: PMC11903331 | PMID: 39972144
- Evidence: If RNA-seq data were available only in BAM format, the sequencing file was first converted into FASTQ format utilizing the Picard software (version 2.7.7a).
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, R, RSEM] -> differential/statistical testing [DESeq2, GSEA, R] -> stage not stated [AlphaFold v2.3.2, Picard]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: Data were analysed using the Broad Picard Pipeline, which includes demultiplexing and data aggregation.
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### SKI complex loss renders 9p21.3-deleted or MSI-H cancers dependent on PELO. (Nature 2025)

- DOI: 10.1038/s41586-024-08509-3 | PMCID: PMC11864980 | PMID: 39910293
- Evidence: Data were analysed using the Broad Institute Picard Pipeline ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [ImageJ v1.53k, Picard, RSEM, SciPy]

### Ancient DNA reveals reproductive barrier despite shared Avar-period culture. (Nature 2025)

- DOI: 10.1038/s41586-024-08418-5 | PMCID: PMC11864967 | PMID: 39814885
- Evidence: We applied Picard MarkDuplicates v.2.22.9 function ( https://github.com/broadinstitute/picard ) for PCR duplicates removal, and mapDamage v.2.0 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> read trimming [SAMtools] -> stage not stated [Picard]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Reads were sorted with SAMtools 68 , polymerase chain reaction duplicates were removed with Picard Tools v.2.0.1 and indels were locally realigned using GATK software (v.3.7.0) 69 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: PCR duplicates were removed using MarkDuplicates (v.2.18.29) in Picard.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Evidence: Pair-end reads in which only one mate mapped over 5′ terminal sequence of TE were extracted using Picard tools (v.2.27.5) ( https://broadinstitute.github.io/picard/ ) with the function of ‘FilterSamReads’ and then extracted discordantly mapped reads.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Duplicated reads were eliminated using the Picard ( https://github.com/broadinstitute/picard ) function MarkDuplicates, except for MNase–seq and RNA-seq, for which duplicates were retained.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **2.25.5**
- Evidence: Duplicate reads were removed with Picard (v2.25.5).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Version used: **2.18.7**
- Evidence: Aligned reads were converted to BAM files, merged across libraries at sample level, sorted, filtered and indexed using Samtools (v.1.21) 75 , then duplicates identified using MarkDuplicates from Picard (v2.18.7), with the following options in place: ‘OPTICAL_DUPLICATE_PIXEL_DISTANCE = 12000 REMOVE_DUPLICATES = false TAGGING_POLICY = All VALIDATION_STRINGENCY = LENIENT’.
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Evidence: SNP calling was conducted following GATK best practices for RNA-seq data including steps such as Picard tools, SplitNCigarReads and HaplotypeCaller.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: We marked duplicate reads using Picard MarkDuplicates v.2.17.10 257 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **2.27.4**
- Evidence: Picard (v.2.27.4) was used to remove PCR duplicates, and TSV files containing genomic locations and full cell barcodes were generated for SnapATAC2 (v.2.6.1) 53 .
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: The alignment results in SAM format were converted to the BAM format using the SortSam tool from the Picard suite (v.2.14.0-SNAPSHOT), and samtools (v.1.10) for indexing.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Version used: **2.18.14**
- Evidence: Duplicated reads were removed by Picard (v2.18.14) 66 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Polyclonal selection of immune checkpoint mutations in thyroid autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10493-9 | PMCID: PMC13233322 | PMID: 41981327
- Evidence: Library complexity and coverage statistics were calculated using Picard ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [R, Seurat, ggpubr, tidyverse]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **2.18.26**
- Evidence: PCR or optical duplicates were marked using Picard v.2.18.26 and removed.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Evidence: The resulting .bam file was filtered for duplicates using Picard ( http://broadinstitute.github.io/picard ) and realigned around indels using GATK (v.3.056) 64 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **2.2.4**
- Evidence: PCR duplicates were removed by Picard (v.2.2.4) ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Evidence: The demultiplexed FASTQ files from the post-mortem samples were aligned to the human genome reference GRCh37/hg19 using bwa mem (v0.7.17-r1188) 63 and deduplicated using Picard MarkDuplicates (v2.21.8).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: The mapped reads were processed using samblaster (v.0.1.26) 60 , sambamba (v.0.7.0) 61 and Picard tools (v.2.20.0).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **2.13.3**
- Evidence: Mapped reads were sorted and duplicates removed using SortSam and MarkDuplicates by Picard v.2.13.3 ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: After alignment, the reads were filtered using MarkDuplicates from Picard and then by a quality score of >20 using SAMtools 69 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: To control for technical variation due to the sequencing and library prep we calculated the principal components of the Picard sequencing metrics ( http://broadinstitute.github.io/picard/ ) using the CollectAlignmentSummaryMetrics, CollectRnaSeqMetrics and MarkDuplicates modules, and included them in our model.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Evidence: Reads with poor quality (lower than 20) were filtered using cutadapt (v.2.6) and aligned to the mouse reference genome (GRCm39) using bowtie2 (v.2.4), and duplicated reads were marked and removed by Picard tools (v.3.4).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Duplicate reads in the resulting BAM files were marked using Picard tools ( http://broadinstitute.github.io/picard/ ) ‘MarkDuplicates’.
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: PCR duplicates were removed using Picard MarkDuplicates ( http://picard.sourceforge.net ), and realignment around indels was performed using GATK 67 .
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Picard’s MarkDuplicates ( https://broadinstitute.github.io/picard/ ), SAMtools 77 and BAMTools 78 were used postalignment for filtering and removal of unmapped, multimapped, PCR duplicate and mismatched reads.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **2.18.7**
- Evidence: PCR duplicates were removed using the MarkDuplicates function in Picard (v.2.18.7).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: Reads were filtered based on mapping quality (MAPQ ≥ 20), and duplicate reads were marked with Picard MarkDuplicates (v.2.19.0).
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Evidence: Demultiplexed paired-end FASTQ files were converted to unaligned BAM format using Picard’s FastqToSam tool (v.3.0.0) and trimmed using Trim Galore (v.0.6.6) in paired-end mode with Nextera adapter trimming enabled.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Version used: **2.25.3**
- Evidence: Reads were aligned to the hg19 genome using BWA MEM (v.0.7.17-r1188) 65 and PCR duplicates were removed using MarkDuplicates in Picard (v.2.25.3).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Picard tools 83 were used to mark duplicate sequences as an additional quality control step.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Reads were mapped to mm10 (hisat2), duplicates removed (Picard) and peaks were called using MACS2.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Evidence: Duplicate sequences were marked with Picard (command MarkDuplicates) (v.2.17.10; http: //broadinstitute.github.io/picard/).
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Evidence: PCR duplicates were removed with Picard MarkDuplicates (version 1.95; http://picard.sourceforge.net ) and local realignment around indels was done with GATK ( 67 ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### Genomic evidence for inbreeding depression and purging of deleterious genetic variation in Indian tigers. (PNAS 2021)

- DOI: 10.1073/pnas.2023018118 | PMCID: PMC8670471 | PMID: 34848534
- Evidence: We marked duplicate reads with the Picard Tools “MarkDuplicates” command ( http://broadinstitute.github.io/picard ).
- Full pipeline: alignment/mapping [ANGSD, GATK] -> registration [GATK] -> stage not stated [Picard, Strelka, VCFtools, VEP]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Version used: **2.6.0**
- Evidence: Sequence alignments were preprocessed using Picard v2.6.0 (Broad Institute 2018 https://broadinstitute.github.io/picard/ ) which included merging (MergeSamFiles), coordinate sorting (SortSam) and identifying/removing duplicate reads arising during library amplification (MarkDuplicates).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Version used: **2.18.14**
- Evidence: Sequence duplicates were removed with MarkDuplicates in Picard v2.18.14 ( 54 ).
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Evidence: Sequences with more than 10 soft and hard clipped alignments were filtered out by samclip, and duplicates were removed using Picard’s MarkDuplicates module.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **2.20.2**
- Evidence: Read-group information was added and PCR and optical duplicates were removed from mapped reads using Picard v2.20.2 ( 86 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### High frequency of an otherwise rare phenotype in a small and isolated tiger population. (PNAS 2021)

- DOI: 10.1073/pnas.2025273118 | PMCID: PMC8488692 | PMID: 34518374
- Evidence: We marked the duplicate reads using Picard Tools ( 100 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [BCFtools, BWA] -> variant calling [GATK, VCFtools] -> stage not stated [Picard]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Evidence: Processed reads were then aligned to the mouse reference genome (mm10) using bowtie with parameters “-m1 -v1 –best –strata -X 2000 –trim3 1.” Duplicates were removed using Picard tools.
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Bromodomain containing 9 (BRD9) regulates macrophage inflammatory responses by potentiating glucocorticoid receptor activity. (PNAS 2021)

- DOI: 10.1073/pnas.2109517118 | PMCID: PMC8536317 | PMID: 34446564
- Evidence: Duplicate reads were filtered out using the MarkDuplicate function from Picard tools v.2.17.0 ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.8] -> alignment/mapping [Bowtie2 v2.3.3.1, deepTools v3.3.2] -> quantification [deepTools v3.3.2] -> normalisation [deepTools v3.3.2] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, Picard, fastp]

### Accelerated expansion of pathogenic mitochondrial DNA heteroplasmies in Huntington's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2014610118 | PMCID: PMC8325154 | PMID: 34301881
- Evidence: Martin Picard, Paul Soloway, Haiyuan Yu, Kimberly O’Brien, and Yiping Wang for critical reading and comments on the manuscript.
- Full pipeline: alignment/mapping [SAMtools v1.6, freebayes v1.1.0] -> registration [SAMtools v1.6, freebayes v1.1.0] -> differential/statistical testing [R v3.5.0, lme4 v1.1] -> stage not stated [ANNOVAR, Picard]

### Dynamic chromatin regulatory landscape of human CAR T cell exhaustion. (PNAS 2021)

- DOI: 10.1073/pnas.2104758118 | PMCID: PMC8325267 | PMID: 34285077
- Evidence: Reads were filtered with Picard tools against mitochondrial sequences, quality scores of <20, and PCR duplicates.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [BEDTools, DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2, Picard, R]

### Accurate genomic variant detection in single cells with primary template-directed amplification. (PNAS 2021)

- DOI: 10.1073/pnas.2024176118 | PMCID: PMC8214697 | PMID: 34099548
- Evidence: All files were down sampled to the specified number of reads using Picard DownSampleSam.
- Full pipeline: read trimming [GATK v4.1, Trimmomatic] -> stage not stated [Picard]

### Genetic basis of variation in cocaine and methamphetamine consumption in outbred populations of <i>Drosophila melanogaster</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2104131118 | PMCID: PMC8201854 | PMID: 34074789
- Evidence: The alignments were locally realigned, marked for PCR duplicates using GATK (version 2.4) ( 55 ) and Picard tools (version 1.89) before recalibrating base qualities with GATK.
- Full pipeline: alignment/mapping [GATK v2.4, Picard] -> registration [GATK v2.4, Picard] -> visualisation [Cytoscape v3.8.0]

### A phage mechanism for selective nicking of dUMP-containing DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2026354118 | PMCID: PMC8201957 | PMID: 34074772
- Evidence: Reads were then deduplicated using Picard.
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [GATK v3.7] -> variant calling [Cutadapt] -> stage not stated [Fiji, ImageJ, VEP]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: We extracted human–viral chimeric reads by using the read names from the STAR generated Chimeric.out.junction file to get the read alignments from the STAR generated Chimeric.out.sam file by Picard ( http://broadinstitute.github.io/picard ), using command: java -jar picard.jar FilterSamReads I = Chimeric.out.sam O = hv-Chimeric.out.sam READ_LIST_FILE = hv-Chimeric.out.junction.ids FILTER = include...
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### The genomes of ancient date palms germinated from 2,000 y old seeds. (PNAS 2021)

- DOI: 10.1073/pnas.2025337118 | PMCID: PMC8126781 | PMID: 33941705
- Evidence: We used MarkDuplicates (Picard tools) to flag duplicate read pairs.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> variant calling [GATK v3.5] -> stage not stated [ADMIXTURE, Picard, R]

### Substrate discrimination and quality control require each catalytic activity of TRAMP and the nuclear RNA exosome. (PNAS 2021)

- DOI: 10.1073/pnas.2024846118 | PMCID: PMC8040639 | PMID: 33782132
- Evidence: After mapping, the output SAM files were postprocessed using the Picard tools 1.124 to add or replace read groups, which also sorts the file and converts it to the compressed BAM format.
- Full pipeline: alignment/mapping [HTSeq v0.5.3, Picard] -> quantification [ImageJ] -> normalisation [Bioconductor] -> differential/statistical testing [Bioconductor]

### ELF3 activated by a superenhancer and an autoregulatory feedback loop is required for high-level HLA-C expression on extravillous trophoblasts. (PNAS 2021)

- DOI: 10.1073/pnas.2025512118 | PMCID: PMC7936349 | PMID: 33622787
- Evidence: Duplicates were removed using MarkDuplicates in Picard tools ( broadinstitute.github.io/picard/ ).
- Full pipeline: stage not stated [Picard, Seurat]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: We measured genome-wide GC content with the Picard Tools CollectGcBiasMetrics function.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: Then the Picard tool of MarkDuplicates was employed to mark and remove duplicate reads ( broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Human neutrophil development and functionality are enabled in a humanized mouse model. (PNAS 2022)

- DOI: 10.1073/pnas.2121077119 | PMCID: PMC9618085 | PMID: 36269862
- Evidence: Auerbach at Regeneron Pharmaceuticals, who generated, in collaboration with our groups, the individual knockin alleles combined in MISTRG; Jon Alderman, Caroline Lieber, Elizabeth Hughes-Picard and Beth Cadugan for administrative assistance; Carla Weibel, Patricia Ranney, and Cynthia Hughes for mouse colony management; Judith Stein and Linda Evangelisti for mouse engineering; David Urbanos for hum...
- Full pipeline: stage not stated [Picard]

### Another look at rational torsion of modular Jacobians. (PNAS 2022)

- DOI: 10.1073/pnas.2210032119 | PMCID: PMC9565053 | PMID: 36191227
- Evidence: As such, they also act on geometric objects such as J 0 ( N ) and the divisor group of cusps, but there is some ambiguity as to how a correspondence acts (using either the “Picard” or the “Albanese” functoriality—see the discussion in ref.
- Full pipeline: stage not stated [Picard]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: The library complexity was estimated from the mapped BAM file of each cell using Picard EstimateLibraryComplexity (v2.27.3).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Winter warming post floral initiation delays flowering via bud dormancy activation and affects yield in a winter annual crop. (PNAS 2022)

- DOI: 10.1073/pnas.2204355119 | PMCID: PMC9522361 | PMID: 36122201
- Evidence: Additionally, PCR duplicates were marked and removed by MarkDuplicates of Picard tools v2.26.10.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HISAT2 v2.2.1] -> normalisation [deepTools v2.3] -> visualisation [deepTools v2.3] -> stage not stated [HOMER, Picard, R, WGCNA]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Evidence: PCR duplicates were removed with the MarkDuplicates module from Picard Tools, version 1.126 ( 55 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Dopamine and GPCR-mediated modulation of DN1 clock neurons gates the circadian timing of sleep. (PNAS 2022)

- DOI: 10.1073/pnas.2206066119 | PMCID: PMC9407311 | PMID: 35969763
- Evidence: PCR duplicates were removed using Picard Tools (Picard Toolkit 2019.
- Full pipeline: dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [Bioconductor, Seurat, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [Picard]

### Distinct evolutionary trajectories of SARS-CoV-2-interacting proteins in bats and primates identify important host determinants of COVID-19. (PNAS 2022)

- DOI: 10.1073/pnas.2206610119 | PMCID: PMC9436378 | PMID: 35947637
- Evidence: Analyses were performed as previously described in Picard et al.
- Full pipeline: stage not stated [BLAST, Cytoscape, Picard]

### Microenvironmental sensing by fibroblasts controls macrophage population size. (PNAS 2022)

- DOI: 10.1073/pnas.2205360119 | PMCID: PMC9371703 | PMID: 35930670
- Evidence: Read duplicates were removed and BAM files were generated with the Picard toolkit ( http://broadinstitute.github.io/picard ).
- Full pipeline: alignment/mapping [kallisto] -> stage not stated [MACS2, Picard]

### Three distinct <i>Atoh1</i> enhancers cooperate for sound receptor hair cell development. (PNAS 2022)

- DOI: 10.1073/pnas.2119850119 | PMCID: PMC9371730 | PMID: 35925886
- Evidence: Mapped reads were sorted using Samtools ( 69 ), and duplicated reads were removed using the Picard MarkDuplicates function ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **1.87**
- Evidence: Duplicate reads were removed using Picard version 1.87 ( broadinstitute.github.io/picard ).
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Evidence: For both WGS and sequence-capture data, we converted raw fastq files to unmapped bam files using FastqToSam [Picard toolkit v.2.18.4 ( 75 )] and then, marked Illumina adapters using MarkIlluminaAdapters (Picard).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Expansion of a retrovirus lineage in the koala genome. (PNAS 2022)

- DOI: 10.1073/pnas.2201844119 | PMCID: PMC9231498 | PMID: 35696585
- Version used: **2.23.4**
- Evidence: Sequencing reads were mapped to the koala reference using BWA-MEM ( 31 ), pooled per individual with SAMtools 1.12 ( 32 ), and duplicate reads marked by Picard 2.23.4 (broadinstitute.github.io/picard/).
- Full pipeline: alignment/mapping [BWA, Picard v2.23.4, RepeatMasker, SAMtools v1.12] -> stage not stated [DELLY, R]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Evidence: Briefly, sequence alignments underwent BaseQuality Score Recalibration (GATK) and marking of duplicates (MarkDuplicates; Picard), followed by individual-level variant calling with HaplotypeCaller (GATK).
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### An approach for evaluating the effects of dietary fiber polysaccharides on the human gut microbiome and plasma proteome. (PNAS 2022)

- DOI: 10.1073/pnas.2123411119 | PMCID: PMC9171781 | PMID: 35533274
- Evidence: Duplicate reads (optical, PCR-generated) were removed from the mapped data (Picard MarkDuplicates tool v 2.9.3 – http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [Cutadapt, DADA2 v1.13.0] -> alignment/mapping [Picard, featureCounts] -> stage not stated [Bowtie2]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Potential optical and PCR duplicates were removed with Picard tools ( 66 ), while reads with a mapping quality value (MAPQ) value of <60 were also discarded.
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
- Evidence: Read groups were added using Picard Tools AddOrReplaceReadGroups function ( 129 ).
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SnpEff] -> registration [GATK] -> stage not stated [PLINK v1.9, Picard]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Evidence: Duplicate reads were filtered by using Picard (http://broadinstitute.github.io/picard) and realigned around indels by using GATK 3.0 ( 65 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Loss of TET reprograms Wnt signaling through impaired demethylation to promote lung cancer development. (PNAS 2022)

- DOI: 10.1073/pnas.2107599119 | PMCID: PMC8832965 | PMID: 35110400
- Version used: **2.21.2**
- Evidence: Duplicated reads were removed using Picard (2.21.2).
- Full pipeline: read trimming [Trim Galore v0.5.0] -> stage not stated [DESeq2, Picard v2.21.2, RepeatMasker, SAMtools v1.4]

### Engineering and functional analysis of yeast with a monotypic 40S ribosome subunit. (PNAS 2022)

- DOI: 10.1073/pnas.2114445119 | PMCID: PMC8833219 | PMID: 35105807
- Evidence: Then, Picard tools (v1.119; https://broadinstitute.github.io/picard/ ) were used to covert the sam file to a bam file and to remove the duplicated reads caused by PCR amplification.
- Full pipeline: quality control [FastQC, Trimmomatic v0.36] -> read trimming [FastQC, Trimmomatic v0.36] -> variant calling [GATK v3.5, SnpEff] -> registration [GATK v3.5] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [Picard]

### TRIM14 inhibits OPTN-mediated autophagic degradation of KDM4D to epigenetically regulate inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2113454119 | PMCID: PMC8851536 | PMID: 35145029
- Evidence: Then PCR duplicates were marked by Picard Tools (v 2.14.0).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5] -> dimensionality reduction/clustering [clusterProfiler v4.0.5] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.6, Picard]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Evidence: In a next step, we used the “Picard ( 38 ) MarkDuplicates” option to mark mapped reads that might result from PCR duplication to reduce PCR bias in the abundance of certain DNA fragments during sequencing.
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### CHAF1A/B mediate silencing of unintegrated HIV-1 DNAs early in infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116735119 | PMCID: PMC8795523 | PMID: 35074917
- Version used: **2.23.1**
- Evidence: Potential PCR duplicates were removed by the function “MarkDuplicates” (parameter: REMOVE_DUPLICATES = true) of Picard (v2.23.1).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> stage not stated [Picard v2.23.1]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: Duplicate reads were removed using Picard tools MarkDuplicates.jar ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Next, duplicate reads were marked using the markduplicate utility from Picard (GATK4), for which duplicate reads are defined as originating from a single fragment of DNA.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Neural functional theory for inhomogeneous fluids: Fundamentals and applications. (PNAS 2023)

- DOI: 10.1073/pnas.2312484120 | PMCID: PMC10723051 | PMID: 38060556
- Evidence: A fixed-point (Picard) iteration with mixing parameter α can be used to determine the density profile from Eq.
- Full pipeline: simulation/modelling [Keras, TensorFlow] -> stage not stated [Picard]

### Universal Poisson statistics of a passive tracer diffusing in dilute active suspensions. (PNAS 2023)

- DOI: 10.1073/pnas.2308226120 | PMCID: PMC10723115 | PMID: 38048467
- Evidence: 6 by Picard iteration ( SI Appendix , Eq.
- Full pipeline: stage not stated [Picard]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: The alignment bam files were then sorted, and PCR duplicates were marked using Picard ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### A polygenic explanation for Haldane's rule in butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2300959120 | PMCID: PMC10622916 | PMID: 37856563
- Evidence: Duplicate reads were marked using Picard-2.25.7 ( 50 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [BCFtools] -> stage not stated [Picard]

### In vitro DNA repair genomics using XR-seq with &lt;i&gt;Escherichia coli&lt;/i&gt; and mammalian cell-free extracts. (PNAS 2023)

- DOI: 10.1073/pnas.2314233120 | PMCID: PMC10614213 | PMID: 37844222
- Evidence: The reads were aligned by BWA-backtrack ( 41 ), followed by Picard tools ( https://broadinstitute.github.io/picard/ ) for filtering, sorting, deduplication, and indexing.
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [Bowtie2, Picard]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Evidence: Low mapping quality reads and duplicated reads were removed by SAMtools (version 1.3.1) ( 72 ) and Picard tools ( http://broadinstitute.github.io/picard ) (version 2.26.9).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### Environmentally robust <i>cis</i>-regulatory changes underlie rapid climatic adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2214614120 | PMCID: PMC10523592 | PMID: 37725649
- Evidence: We marked duplicates with the Picard tool MarkDuplicates, and then we used the Genome Analysis Toolkit (GATK) tools HaplotypeCaller and GenotypeGVCFs for joint genotyping across genomic samples.
- Full pipeline: read trimming [DESeq2, fastp] -> alignment/mapping [Bowtie2] -> variant calling [GATK, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, R v4.1.1] -> stage not stated [BEDTools, HTSeq, VCFtools]

### Sequencing 4.3 million mutations in wheat promoters to understand and modify gene expression. (PNAS 2023)

- DOI: 10.1073/pnas.2306494120 | PMCID: PMC10515147 | PMID: 37703281
- Evidence: Alignments were sorted by using samtools v1.7 ( 91 ), and duplicate reads were removed with Picard tools v2.7.1 ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, SAMtools v1.7] -> stage not stated [VEP]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: The resulting SAM files were then sorted (settings: SORT_ORDER = coordinate), converted to BAM format, and processed for duplicate removal with version 2.8.0 of Picard ( http://broadinstitute.github.io/picard/ ) (settings: REMOVE_DUPLICATES = true, ASSUME_SORT_ORDER = coordinate).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Mechanoepigenetic regulation of extracellular matrix homeostasis via Yap and Taz. (PNAS 2023)

- DOI: 10.1073/pnas.2211947120 | PMCID: PMC10235980 | PMID: 37216538
- Evidence: Picard was used to generate bam files and sorted by chromosomal coordinates.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2, Picard, SAMtools, deepTools, featureCounts]

### Differentiation of <i>Plasmodium</i> male gametocytes is initiated by the recruitment of a chromatin remodeler to a male-specific cis-element. (PNAS 2023)

- DOI: 10.1073/pnas.2303432120 | PMCID: PMC10193995 | PMID: 37155862
- Evidence: Duplicate fragments mapped on the genome were removed using Picard MarkDuplicates application ( http://picard.sourceforge.net ).
- Full pipeline: alignment/mapping [Bowtie2, MACS2, Picard]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: PCR duplicates were removed using the MarkDuplicate function from Picard tools ( http://broadinstitute.github.io/picard ) for each cell.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### Digital microfluidics-based digital counting of single-cell copy number variation (dd-scCNV Seq). (PNAS 2023)

- DOI: 10.1073/pnas.2221934120 | PMCID: PMC10193948 | PMID: 37155890
- Evidence: Picard Tools (version 2.18.13) was applied to sort aligned reads (SortSam) and to mark potential PCR duplicates (MarkDuplicates).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.38] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.9] -> differential/statistical testing [SAMtools v1.9] -> stage not stated [BEDTools]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Evidence: Alignments were then sorted, read groups added and duplicates removed using Picard Tools v2.18.16.
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Epistasis reduces fitness costs of influenza A virus escape from stem-binding antibodies. (PNAS 2023)

- DOI: 10.1073/pnas.2208718120 | PMCID: PMC10151473 | PMID: 37068231
- Evidence: Data formatting for GATK was made using Picard ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [BWA, Trimmomatic v0.39] -> alignment/mapping [BWA, Trimmomatic v0.39] -> stage not stated [GATK, Picard]

### Spectra and characteristics of somatic mutations induced by ionizing radiation in hematopoietic stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2216550120 | PMCID: PMC10104525 | PMID: 37018193
- Version used: **2.18.26**
- Evidence: Sequence reads were mapped to the mouse reference genome (UCSC mm10) using BWA-MEM v.0.7.17 with the “−M” option compatible with Picard v2.18.26 (broadinstitute.github.io/picard) used to remove PCR duplicates.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.0.0, Picard v2.18.26, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> differential/statistical testing [R v4.0.3]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Evidence: Sequence Alignment/Map tools (SAMtools) v1.10 (r783) and Picard tools version 2.23.3 ( http://broadinstitute.github.io/picard ) were used to filter, sort, and convert the SAM files.
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: The MarkDuplicates tool ( 115 ) from Picard tools was used to remove potential PCR duplicates and to set read groups.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### Genetic risk factors for Mesoamerican nephropathy. (PNAS 2024)

- DOI: 10.1073/pnas.2404848121 | PMCID: PMC11626114 | PMID: 39585978
- Evidence: Genotypes were called from Genome Reference Consortium Human Build 37 (GRCh37), and coordinates were changed to Build 38 using Picard Tools.
- Full pipeline: variant calling [Beagle, Picard] -> visualisation [ggplot2] -> stage not stated [METAL]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Reads were then aligned to the Atlantic salmon genome downloaded from Ensembl (Salmo_salar-GCA_905237065.2) using “Bowtie2” ( 73 ) and parameters “--very-sensitive --maxins 1500 --end-to-end”. “Samtools view” was used to filter for primary alignments with mapping quality score over 20 (“-F 256 -q 20”). “Picard MarkDuplicates” ( 74 ) was used to identify and remove duplicate reads.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: Duplicate reads were removed from the alignments using the MarkDuplicates function from Picard ( broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Evidence: PCR duplicates were removed with Picard MarkDuplicates version 2.27.4 ( 57 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: We removed duplicated reads using Picard tools ( https://broadinstitute.github.io/picard/ ) and identified SNPs using GATK4 ( 73 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Version used: **1.112**
- Evidence: Further processing involved filtering multiple hits reads and eliminating PCR duplicates using Samtools (v1.7) ( 52 ) and Picard (v1.112) ( https://broadinstitute.github.io/picard/ ) programs, respectively.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### The role of emerging elites in the formation and development of communities after the fall of the Roman Empire. (PNAS 2024)

- DOI: 10.1073/pnas.2317868121 | PMCID: PMC11388374 | PMID: 39159385
- Evidence: Duplicate reads were marked using Picard Tools ( 49 ), and reads shorter than 30 bp were filtered out.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [SAMtools] -> variant calling [VCFtools] -> normalisation [VCFtools] -> stage not stated [ADMIXTURE, Picard]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: Reads were mapped to the human genome (GRCh37) using Bowtie 2 and BAM files were created using Picard.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: Sequence duplicates were removed using the MarkDuplicates function in Picard v/2.18.26 ( 80 ) and indels were realigned using GATK v/3.8.1 ( 81 ).
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### UPF1 deficiency enhances mitochondrial ROS which promotes an immunosuppressive microenvironment in pancreatic ductal adenocarcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2401996121 | PMCID: PMC11331118 | PMID: 40591563
- Evidence: Briefly, raw reads were fed into “rna-star” module of Seq-N-Slide which employs Trimmomatic for adaptor trimming and low-quality base removal, STAR for alignment to reference genomes (mm10), fastq_screen for contaminant detection, Picard for base distribution and 5′/3′ biases, and featureCounts to generate genes-samples count matrices.
- Full pipeline: read trimming [Picard, STAR, Trimmomatic, featureCounts] -> alignment/mapping [Picard, STAR, Trimmomatic, featureCounts] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: PCR duplicates were marked with Picard ( 28 ) and candidate variants called with the GATK HaplotypeCaller algorithm, split by chromosome ( 29 , 30 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: The remaining reads were aligned to the canFam3.1 reference genome using BWA ( 71 ) aln v0.7.17-r1188 (-n 0.01 -l 1024 -o 2), and we deduplicated the mapped reads using “MarkDuplicates.jar” in Picard Tools v2.22.9 ( https://github.com/broadinstitute/picard ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### Long noncoding RNA LIRIL2R modulates FOXP3 levels and suppressive function of human CD4<sup>+</sup> regulatory T cells by regulating IL2RA. (PNAS 2024)

- DOI: 10.1073/pnas.2315363121 | PMCID: PMC11161746 | PMID: 38805281
- Evidence: Alignment, sorting, filtering, and deduplication for the CUT&Tag analysis was performed using Bowtie2 (v2.3.5.1) ( 60 ), Samtools (v1.9) ( 61 ), and Picard ( http://broadinstitute.github.io/picard/ ) MarkDuplicates (v2.21.7) with the same parameters as described in the ATAC-seq analysis.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9, kallisto] -> differential/statistical testing [R, limma v3.42.2] -> stage not stated [GSEA]

### Locus coeruleus integrity is related to an exploitation-based decision-making bias in older adulthood. (PNAS 2024)

- DOI: 10.1073/pnas.2322617121 | PMCID: PMC11145298 | PMID: 38771873
- Evidence: ..., Lisa-Marie Munter , Laurence Maligne Bruneau , Julien Menes , Bery Mohammediyan , Gerhard Multhaup , Eugenia Nita Capota , Valentin Ourry , Cynthia Picard , Judes Poirier , Ting Qiu , Marc James Quesnel , Natasha Rajah , Jean-Michel Raoult , Jordana Remz , Pedro Rosa-Neto , Jean-Paul Soucy , R.
- Full pipeline: stage not stated [Picard]

### Reduced stress propagation leads to increased mechanical failure resistance in auxetic materials. (PNAS 2024)

- DOI: 10.1073/pnas.2312899121 | PMCID: PMC11126950 | PMID: 38739788
- Evidence: Reduced Stress Propagation in Auxetic Materials Following Eshelby ( 53 ), Picard et al.
- Full pipeline: stage not stated [Picard]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Version used: **2.26.10**
- Evidence: We used phyluce to map contigs to probes and followed the BWA -mem and GATK pipeline steps described above but marked duplicates with Picard v2.26.10 MarkDuplicates.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: Duplicate removal was performed using Picard.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: We also deleted PCR duplicates by Picard (MarkDuplicates) and the ENCODE Blacklist genome regions ( 58 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Morc1 reestablishes H3K9me3 heterochromatin on piRNA-targeted transposons in gonocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2317095121 | PMCID: PMC10990106 | PMID: 38502704
- Evidence: After removing reads aligned to regions in the blacklist ( 69 ) and PCR duplicates with Picard, we calculated Pearson correlation coefficients between 10 kb bins of biological replicates on chr1 using Deeptools.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Picard] -> quantification [DESeq2] -> normalisation [DESeq2] -> stage not stated [RepeatMasker]

### Aerosolization of viable <i>Mycobacterium tuberculosis</i> bacilli by tuberculosis clinic attendees independent of sputum-Xpert Ultra status. (PNAS 2024)

- DOI: 10.1073/pnas.2314813121 | PMCID: PMC10962937 | PMID: 38470917
- Version used: **2.9.1**
- Evidence: Reads were then mapped to the reconstructed ancestor of the MTBC ( 61 ) using bwa v0.717 ( 62 ) Duplicates were removed using Picard v2.9.1 ( 63 ), prior to using Samtools v1.5 ( 64 ) and varScan v2.2.4 ( 65 ) call variants, with filters to exclude sites with fewer than 10 reads support and minimum base quality scores of 20.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard v2.9.1, SAMtools v1.5] -> differential/statistical testing [R] -> structure determination [Picard v2.9.1, SAMtools v1.5] -> stage not stated [Kraken2]

### Sexual stage-specific A-to-I mRNA editing is mediated by tRNA-editing enzymes in fungi. (PNAS 2024)

- DOI: 10.1073/pnas.2319235121 | PMCID: PMC10962958 | PMID: 38466838
- Evidence: Duplicate reads were eliminated with the MarkDuplicates tool ( https://broadinstitute.github.io/picard/ ) included in the Picard package.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [featureCounts] -> stage not stated [AlphaFold, Picard]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Version used: **2.25.0**
- Evidence: Picard version 2.25.0 ( 83 ) was used to mark PCR and optical duplicate reads via MarkDuplicates.
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Evidence: We used Samtools ( 94 ) to sort reads, Picard to add read groups, and Samtools to index alignments.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Version used: **2.23.0**
- Evidence: Mapping results were then sorted and marked for duplications via Picard (v2.23.0, https://broadinstitute.github.io/picard ) ( 46 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### A recent gibbon ape leukemia virus germline integration in a rodent from New Guinea. (PNAS 2024)

- DOI: 10.1073/pnas.2220392121 | PMCID: PMC10861895 | PMID: 38305758
- Version used: **1.4**
- Evidence: The raw sequencing reads were demultiplexed, adaptor sequences, low-quality reads (quality cutoff 20 and minimum read length of 30 nt), and duplicates were removed and merged using Cutadapt v1.15 ( 44 ), Trimmomatic v0.27 ( 45 ), Picard v1.4 ( http://broadinstitute.github.io/picard ), and BBMerge ( 46 ), respectively.
- Full pipeline: read trimming [Cutadapt v1.15, Picard v1.4, Trimmomatic v0.27] -> alignment/mapping [PyMOL v2.4] -> differential/statistical testing [MrBayes v3.2.7] -> simulation/modelling [MrBayes v3.2.7] -> stage not stated [QGIS v3.16.10, RAxML v8.2.11]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Evidence: Then, the PCR duplicates were removed using Picard with default paraments, and the FPKM was calculated by Stringtie with the paraments “-e --rf -B” using the Araport11 annotation file ( 107 ).
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Evidence: Library complexity was estimated using the “EstimateLibraryComplexity” function of the Picard toolkit ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### DIDO is necessary for the adipogenesis that promotes diet-induced obesity. (PNAS 2024)

- DOI: 10.1073/pnas.2300096121 | PMCID: PMC10801893 | PMID: 38194457
- Evidence: Alignments were formatted to BAM and duplicates were removed with Picard tools.
- Full pipeline: alignment/mapping [BWA, Picard] -> quantification [StringTie] -> stage not stated [DESeq2]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Evidence: Colette Picard and Dr.
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Evidence: Duplicate reads in the resulting BAM files were marked using Samtools version 1.11 and Picard (GATK version 4.2.0.0).
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: The mapped reads were sorted and indexed by SAMtools ( 43 ), and duplicate reads were marked by Picard MarkDuplicates.
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Evidence: 3.1.0-SNAPSHOT) from Picard tools ( https://broadinstitute.github.io/picard/ ), and reads with a mapping quality of 20 or higher were selected using sambamba (v.1.0.0) ( 51 ).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: Postalignment processing was performed using Picard, MarkDuplicates, SAMtools, and deepTools.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Evidence: We used MarkDuplicates from Picard ( http://broadinstitute.github.io/picard ) to mark read duplicates and clipped overlapping reads with the clipOverlap function from bamUtil ( 67 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Fragmentation signatures in cancer patients resemble those of patients with vascular or autoimmune diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2426890122 | PMCID: PMC12402995 | PMID: 40833414
- Evidence: Picard AddOrReplaceReadGroups ( 87 ) was used to add read groups.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2, SAMtools] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy v1.13.1] -> stage not stated [Picard]

### Minimizing and quantifying uncertainty in AI-informed decisions: Applications in medicine. (PNAS 2025)

- DOI: 10.1073/pnas.2424203122 | PMCID: PMC12402999 | PMID: 40833408
- Evidence: Picard AddOrReplaceReadGroups was used to add read groups ( 82 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2] -> differential/statistical testing [scikit-learn] -> stage not stated [Picard, RepeatMasker, SAMtools]

### DNA polymerase β suppresses somatic indels at CpG dinucleotides in developing cortical neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2506846122 | PMCID: PMC12377747 | PMID: 40802685
- Evidence: We used BWA-MEM v0.7.17 with the “–M” option for Picard compatibility to map sequence reads to the mouse reference genome (UCSC mm10).
- Full pipeline: alignment/mapping [BWA, GATK v4.1.0.0, Picard, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> stage not stated [HOMER]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Evidence: ...WA software (v0.7.12-r1039) ( 46 ); b) use the SAMtools software (v0.1.18) to sort the short sequences and convert the format of the data; c) use the Picard software (v1.134) ( http://broadinstitute.github.io/picard/ ) to mark duplicate reads; d) use the Genome Analysis Toolkit (GATK v3.7) ( 47 ) to identify SNVs and indels; e) perform functional annotation of these variant sites using the ANNOVAR...
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### A genomic test of sex-biased dispersal in white sharks. (PNAS 2025)

- DOI: 10.1073/pnas.2507931122 | PMCID: PMC12358869 | PMID: 40758892
- Evidence: Raw reads were trimmed using trimmomatic-0.39 ( 43 ), aligned against the de novo reference genome ( SI Appendix , Supplementary Note 4 ) using the bwa-mem algorithm ( 44 ), and PCR duplicates were tagged using “MarkDuplicates” of Picard toolkit v2.25.6 ( http://broadinstitute.github.io/picard/ ) ( 45 ).
- Full pipeline: read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> variant calling [GATK v4.0] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools v1.9, PLINK]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: Reads aligning to mitochondrial DNA were discarded and PCR duplicates were removed using Picard tools ( https://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### SCoTCH-seq reveals that 5-hydroxymethylcytosine encodes regulatory information across DNA strands. (PNAS 2025)

- DOI: 10.1073/pnas.2512204122 | PMCID: PMC12337322 | PMID: 40743391
- Version used: **3.1.1**
- Evidence: Data from lanes 1 and 2 of each NovaSeq run were then merged with SAMtools (v1.19.2) ( 46 ) and deduplicated in paired-end mode with Picard (v3.1.1) ( 47 ).
- Full pipeline: read trimming [Cutadapt v4.6, Picard v3.1.1, SAMtools v1.19.2] -> stage not stated [BEDTools v2.31.0, Snakemake v7.3.8, deepTools]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Evidence: Picard removed PCR duplicates (v3.0.0) ( 98 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: PCR duplicates were removed with Picard and variant quality recalibration and calling was performed with GATK.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: PCR duplicates were also deleted with Picard (MarkDuplicates).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Longitudinal sequencing reveals polygenic and epistatic nature of genomic response to selection. (PNAS 2025)

- DOI: 10.1073/pnas.2410452122 | PMCID: PMC12207516 | PMID: 40531879
- Evidence: Following sequencing, we mapped reads to the D. melanogaster reference genome (v6.14) using BWA ( 3 ) 53 , retained only uniquely mapped reads, and removed PCR generated duplicates using Picard (“Picard Toolkit,” 2019).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA, Picard] -> variant calling [DESeq2] -> dimensionality reduction/clustering [PLINK] -> stage not stated [R, emmeans]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Evidence: Picard MarkDuplicates v2.20.1 ( https://github.com/broadinstitute/picard ) has been used to detect and remove PCR and Optical duplicates.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Evidence: Finally, we removed all clipped reads (or pairs of reads for which one read was clipped) and all duplicate reads (Picard Tools v.
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Version used: **2.23.4**
- Evidence: The bam files of mapped reads were merged, sorted, and indexed with Samtools ( 110 ), read groups were added with Picard v.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### Ancient genomes reveal trans-Eurasian connections between the European Huns and the Xiongnu Empire. (PNAS 2025)

- DOI: 10.1073/pnas.2418485122 | PMCID: PMC11892651 | PMID: 39993190
- Evidence: We used the MarkDuplicates function of Picard tools ( https://github.com/broadinstitute/picard ) to remove PCR duplicates.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [Cytoscape v3.9.1, Picard]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Evidence: Uniquely mapped reads were further depleted for PCR duplicates with Picard and computationally size-selected for inserts <150 bp for reads from nucleosome-free regions.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### Estimating realized relatedness in free-ranging macaques by inferring identity-by-descent segments. (PNAS 2025)

- DOI: 10.1073/pnas.2401106122 | PMCID: PMC11760927 | PMID: 39808663
- Evidence: We then removed likely PCR or optical duplicates using Picard MarkDuplicates ( 85 ).
- Full pipeline: quality control [Cutadapt, HISAT2] -> read trimming [Cutadapt, HISAT2] -> alignment/mapping [BCFtools v1.9, Cutadapt, HISAT2] -> variant calling [BCFtools v1.9] -> simulation/modelling [R v4.4] -> stage not stated [Picard]

### Ultrarapid MC1R protein and associated plumage color evolution in the domestic chicken. (PNAS 2026)

- DOI: 10.1073/pnas.2605288123 | PMCID: PMC13273276 | PMID: 42268884
- Version used: **2.18.6**
- Evidence: Resulting BAM files were sorted with SAMtools (version 1.9) ( 49 ), and PCR duplicates were marked/removed using Picard (version 2.18.6, https://broadinstitute.github.io/picard/ ) tools.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [BWA v0.7.17] -> registration [GATK v3.7] -> stage not stated [Picard v2.18.6, PyMOL, SAMtools v1.9, VCFtools v0.1.16]

### A plasma-based DNA test for quantification of disease burden in acute myeloid leukemia patients undergoing bone marrow transplantation. (PNAS 2026)

- DOI: 10.1073/pnas.2537987123 | PMCID: PMC13099560 | PMID: 41980102
- Evidence: Duplicate sequencing clusters were removed with Picard ( http://broadinstitute.github.io/picard ).
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [Picard] -> stage not stated [Mutect2]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Trimming was performed using bbduk, and duplicates were removed using Picard.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Evidence: Clean reads were aligned to the S. carpocapsae reference genome (GCA_000757645.3) using HISAT2 v2.1.0 ( 60 ), and PCR duplicates were removed using Picard Tools v2.25.1.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### Cortical wiring by synapse type-specific control of local protein synthesis. (Science 2022)

- DOI: 10.1126/science.abm7466 | PMCID: PMC7618116 | PMID: 36423280
- Evidence: Sequencing, data analysis, reads repartition, and insert size estimation were performed using FastQC, Picard-Tools, Samtools and rseqc.
- Full pipeline: quality control [FastQC, Picard, SAMtools] -> alignment/mapping [STAR v2.4.0] -> quantification [R v3.2] -> normalisation [R v3.2] -> differential/statistical testing [DESeq2, R v3.2] -> stage not stated [ImageJ]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Evidence: Duplicate reads were removed using the MarkDuplicates function of the Picard tools (v2.17.11).
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Evidence: PCR duplicates and unmapped reads were filtered out using Samtools and Picard.
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Version used: **2.8.0**
- Evidence: Then, duplicate reads were marked by MarkDuplicates of Picard (v.2.8.0), followed by local Indel realignment and base quality score recalibration using Genome Analysis Toolkit (GATK) (v.3.5) ( 45 ) to generate BAM files for mutation calling.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Next, reads were filtered using Markduplicates from Picard in addition to a quality score filtering of >20 via samtools( 59 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Evidence: Reads were aligned to the reference genome using BWA-MEM2( 71 ) (v2.2.1) and duplicates were marked with Picard( 73 ) (gatk, v4.4.0.0).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Duplicated reads were marked and removed using Picard, then replicates per condition and MNase digest conditions (high/low) merged using Samtools.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

