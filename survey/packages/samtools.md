# SAMtools

- **Category:** genomics
- **Papers in survey:** 692
- **Journals:** PNAS (316), Nature (313), Cell (50), Science (13)
- **Years:** 2021 (71), 2022 (113), 2023 (109), 2024 (149), 2025 (172), 2026 (78)
- **Versions named:** 1.9 (81), 1.10 (34), 1.3.1 (24), 1.11 (17), 1.16.1 (15), 1.12 (14), 1.3 (13), 1.6 (12), 1.13 (12), 1.17 (12)
- **Pipeline stages it appears in:** alignment/mapping (380), read trimming (40), variant calling (36), quality control (25), quantification (23), visualisation (11), differential/statistical testing (9), registration (8), dimensionality reduction/clustering (3), normalisation (2), structure determination (2), simulation/modelling (1)

## Papers

### Generation and transmission of interlineage recombinants in the SARS-CoV-2 pandemic. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.014 | PMCID: PMC8367733 | PMID: 34499854
- Evidence: (2021) https://github.com/robj411/sequencing_coverage Samtools Li et al.
- Full pipeline: alignment/mapping [Pangolin, minimap2] -> variant calling [Python] -> structure determination [IQ-TREE v2.1] -> stage not stated [SAMtools, TreeTime]

### The genomic history of the Middle East. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.013 | PMCID: PMC8445022 | PMID: 34352227
- Evidence: ...1.9 Chang et al., 2015 https://www.cog-genomics.org/plink/ covstats Pedersen et al., 2017 https://github.com/brentp/goleft/ bcftools v1.9 N/A https://samtools.github.io/bcftools/ CrossMap v0.4.2 Zhao et al., 2014 https://crossmap.readthedocs.io/en/latest/ BEAST v1.8.4 Drummond and Rambaut 2007 https://beast.community/2016-06-17_BEAST_v1.8.4_released.html RAxML v8.2.10 Stamatakis 2014 https://cme.h...
- Full pipeline: stage not stated [ADMIXTURE, BCFtools v1.9, GATK v3.7, RAxML v8.2.10, SAMtools]

### Identification of novel bat coronaviruses sheds light on the evolutionary origins of SARS-CoV-2 and related viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.008 | PMCID: PMC8188299 | PMID: 34147139
- Version used: **1.10**
- Evidence: ...software/ Clustal Omega v1.2.2 Sievers et al., 2011 http://www.clustal.org/omega/ BLAST Camacho et al., 2009 https://blast.ncbi.nlm.nih.gov/Blast.cgi SAMtools v1.10 Li et al., 2009 http://samtools.sourceforge.net/ Figtree v1.4.4 http://tree.bio.ed.ac.uk/software/figtree/ MEGAHIT v1.2.9 Li et al., 2015 https://github.com/voutcn/megahit coronaSPAdes v3.15.0 Meleshko et al., 2021 https://cab.spbu.ru/...
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.450] -> stage not stated [BLAST, Bowtie2 v2.4.1, PyMOL v2.4.0a, RAxML, SAMtools v1.10]

### The monoclonal antibody combination REGEN-COV protects against SARS-CoV-2 mutational escape in preclinical and human studies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.002 | PMCID: PMC8179113 | PMID: 34161776
- Version used: **1.9**
- Evidence: ...are (v0.3.8) Swift Biosciences https://github.com/swiftbiosciences/primerclip Picard package Broad Institute https://github.com/broadinstitute/picard samtools (v1.9) Li et al., 2009 http://www.htslib.org GATK HaplotypeCaller (v4.1.8) Broad Insitute https://gatk.broadinstitute.org/hc/en-us/articles/360036194592-Getting-started-with-GATK4 Resource availability Lead contact Further information and re...
- Full pipeline: variant calling [GATK, Picard, SAMtools v1.9] -> stage not stated [PHENIX v1.19.1, PyMOL, minimap2]

### High-resolution profiling of pathways of escape for SARS-CoV-2 spike-binding antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.045 | PMCID: PMC8096189 | PMID: 34010620
- Evidence: ...y.io/biocontainers/bowtie:1.2.2%5fpy36h2d50403_1 phippery Matsen Lab https://github.com/matsengrp/phippery xarray http://xarray.pydata.org/en/stable/ SAMtools https://quay.io/biocontainers/samtools:1.3%5fh0592bc0_3 R (version 4.0.2) https://www.R-project.org/ tidyverse https://www.tidyverse.org/ ggpubr https://github.com/kassambara/ggpubr corrr https://github.com/tidymodels/corrr cowplot https://g...
- Full pipeline: stage not stated [Clustal Omega, Nextflow, R v4.0.2, SAMtools, ggpubr, tidyverse, xarray]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: For downsampling re-analysis ( Figures S1G–S1J ), we first randomly downsampled reads at the desided target (90% to 5%) using samtools, then recomputed single-cell UMI matrices and finally we performed metacell clustering keeping the same parameters described above.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Version used: **1.10**
- Evidence: ...stitute.github.io/picard/ PLINK 1.9 Purcell et al., 2007 https://zzz.bwh.harvard.edu/plink/plink2.shtml popHelper Francis, 2017 http://pophelper.com/ Samtools v.
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Characterizing genetic intra-tumor heterogeneity across 2,658 human cancer genomes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.009 | PMCID: PMC8054914 | PMID: 33831375
- Evidence: After fitting integer (total) copy numbers, JaBbA uses allelic read counts at germline heterozygotic sites (obtained via samtools pileup at HapMap v3 sites) to infer likely allelic copy numbers at genomic segments.
- Full pipeline: quantification [SAMtools] -> stage not stated [GSEA, IMPUTE2, Mutect2, R, fgsea]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: ..., 2010 MAFFT https://mafft.cbrc.jp/alignment/software/ Katoh and Standley, 2013 iVar 1.2.1 https://github.com/andersen-lab/ivar Grubaugh et al., 2019 Samtools http://samtools.sourceforge.net/ Li et al., 2009 TrimGalore https://github.com/FelixKrueger/TrimGalore https://github.com/FelixKrueger/TrimGalore RAMPART ARTIC Network https://github.com/artic-network/rampart ARTIC Network Bioinformatic prot...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Version used: **1.8**
- Evidence: Aligned reads were then sorted using samtools (version 1.8) ( Li et al., 2009 ) and duplicate reads were removed using picard (version 1.89) ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...t al., 2013 https://sites.google.com/site/rfmixlocalancestryinference/ CircularMapper Peltzer et al., 2016 https://github.com/apeltzer/CircularMapper SAMtools Li et al., 2009 http://samtools.sourceforge.net/ BCFtools Li et al., 2009 http://samtools.github.io/bcftools/bcftools.html VCFtools Danecek et al., 2011 http://vcftools.sourceforge.net/ HaploGrep2 Weissensteiner et al., 2016 https://github.c...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: To estimate SARS-CoV-2 replication levels, sequence reads were aligned to SARS-CoV-2 only, and samtools ( Li et al., 2009 ) version 1.9 was used to estimate the mapping rate of the reads to the viral genes.
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **1.5**
- Evidence: Mapped reads were filtered with samtools v1.5 ( Li et al., 2009 ) to remove secondary alignments (‘samtools view -F 256’) and each viral species was considered present in a sample if the mapped reads covered > 75% of the genome length.
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### In vivo structural characterization of the SARS-CoV-2 RNA genome identifies host proteins vulnerable to repurposed drugs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.008 | PMCID: PMC7871767 | PMID: 33636127
- Evidence: ...wtie2 ( Langmead and Salzberg, 2012 ) http://bowtie-bio.sourceforge.net/bowtie2/index.shtml STAR Dobin et al., 2013 https://github.com/alexdobin/STAR samtools ( Li et al., 2009 ) http://samtools.sourceforge.net/ Trimmomatic Bolger et al., 2014 http://www.usadellab.org/cms/?page=trimmomatic Infernal 1.1.3 ( Nawrocki and Eddy, 2013b ) http://eddylab.org/infernal/ RNAstructure ( Reuter and Mathews, 2...
- Full pipeline: read trimming [Bowtie2, SAMtools, Trimmomatic] -> alignment/mapping [MAFFT v7.313] -> differential/statistical testing [SciPy] -> simulation/modelling [UCSF Chimera] -> structure determination [UCSF Chimera] -> visualisation [RAxML v8.2.12] -> stage not stated [AutoDock Vina]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Version used: **1.3.1**
- Evidence: ....6.2 Becton Dickinson N/A FacsDIVAv9.0 Becton Dickinson N/A Burrows-Wheeler Aligner (BWA) v0.7.15 Li and Durbin, 2009 http://bio-bwa.sourceforge.net/ Samtools v1.3.1 Li and Durbin, 2009 http://samtools.sourceforge.net/ Picard 1.81 N/A http://broadinstitute.github.io/picard/ Mutect v1.1.7 Cibulskis et al., 2013 https://software.broadinstitute.org/cancer/cga/mutect VarScan v2.4.1 Koboldt et al., 201...
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: The script was adapted from the ‘extract_variants_by_coordinate.sh’ script for germline variants ( https://research-help.genomicsengland.co.uk/display/GERE/Extract+variants+by+coordinate ) and was run on the command line within the Genomics England Research environment using bcftools ( https://samtools.github.io/bcftools/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Evidence: Alignments were filtered using SAMtools ( Li et al., 2009 ), and peak calls and enrichment tracks were created using MACS2 ( Zhang et al., 2008 ).
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Evidence: For each SNP, we obtained the read counts for each allele from the processed BAM files using samtools mpileup ( Li, 2011 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Version used: **1.9**
- Evidence: ...e and algorithms fastp v0.21.0 Chen et al., 2018 https://github.com/OpenGene/fastp BWA-MEM v0.7.17 Li and Durbin, 2009 http://bio-bwa.sourceforge.net SAMtools v1.9 Li et al., 2009 http://www.htslib.org snpEff v5.0e Cingolani et al., 2012 http://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis pipeline) GitHub https://github.com/roblanf/sarscov2phylo Minimap2 ...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: ...sign https://www.benchling.com N/A R https://www.r-project.org N/A MACS2.0 https://github.com/taoliu/MACS N/A Bowtie2 Langmead and Salzberg, 2012 N/A Samtools http://samtools.sourceforge.net N/A HiCUP v0.8.1 Wingett et al., 2015 N/A Cooltools https://zenodo.org/record/5214125 N/A Juicer Durand et al., 2016 N/A Genrich https://github.com/jsh58/Genrich/ N/A UCSC genome browser https://genome.ucsc.ed...
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Version used: **0.1.19**
- Evidence: ...oncoct 1.0.0 Alneberg et al., 2014 https://github.com/BinPro/CONCOCT BowTie2 2.2.3 Langmead and Salzberg, 2012 https://github.com/BenLangmead/bowtie2 SAMtools 0.1.19 Li et al., 2009 https://github.com/samtools/samtools metaWRAP 1.1.2) Uritskiy et al., 2018 https://github.com/bxlab/metaWRAP CheckM (v.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Evidence: (2021) http://samtools.github.io/bcftools/bcftools.html BWA-MEM v0.7.15 Li (2013) http://bio-bwa.sourceforge.net/ bedtools v2.26.0 Quinlan and Hall (2010) https://github.com/arq5x/bedtools2 CrossMap v0.5.3 Zhao et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...commit 6df90e7 Wegmann lab, Ilektra Schulz bitbucket.org/wegmannlab/atlas-pipeline bcftools versions: 1.9 and 0.1.15 ( Danecek et al., 2021 ) https://samtools.github.io/bcftools/howtos/index.html bwa - Burrows-Wheeler Alignment Tool - versions 0.7.15 and 0.7.17 ( Li, 2013 ) bio-bwa.sourceforge.net BEDOPS v2.4.40 ( Neph et al., 2012 ) https://bedops.readthedocs.io/en/latest/ Bedtools 2.25.0 ( Quinl...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **1.9**
- Evidence: ...gorithms fastp v0.21.0 ( Chen et al., 2018 ) https://github.com/OpenGene/fastp BWA-MEM v0.7.17 ( Li and Durbin, 2009 ) http://bio-bwa.sourceforge.net SAMtools v1.9 ( Li et al., 2009 ) http://www.htslib.org snpEff v5.0e ( Cingolani et al., 2012 ) http://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis pipeline) GitHub,2022 https://github.com/roblanf/sarscov2ph...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Ancient genomes reveal origin and rapid trans-Eurasian migration of 7<sup>th</sup> century Avar elites. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.007 | PMCID: PMC9042794 | PMID: 35366416
- Version used: **1.3**
- Evidence: ...per ANGSD 0.910 Korneliussen et al., 2014 http://www.popgen.dk/angsd/index.php/ANGSD Schmutzi Renaud et al., 2015 https://github.com/grenaud/schmutzi SAMtools 1.3 Li et al., 2009 http://www.htslib.org/doc/samtools.html pileupCaller https://github.com/stschiff/sequenceTools https://github.com/stschiff/sequenceTools GATK v3.5 DePristo et al., 2011 https://gatk.broadinstitute.org/hc/en-us GeneImp 1.4...
- Full pipeline: read trimming [BWA v0.7.12] -> stage not stated [ANGSD v0.910, GATK v3.5, PLINK v1.9, R v4.0, SAMtools v1.3, SHAPEIT]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: (2013) https://github.com/alexdobin/STAR Samtools Li et al.
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...roft et al., 2019 ) https://github.com/sansomlab/gsfisher Harmony ( Korsunsky et al., 2019 ) https://github.com/immunogenomics/harmony HTSlib v1.10.2 Samtools http://www.htslib.org/ imagesc MATLAB https://uk.mathworks.com/help/matlab/ref/imagesc.html IMGT database ( Lefranc, 2011 ) https://www.imgt.org/ IMGT V-QUEST ( Giudicelli et al., 2004 ) https://www.imgt.org/IMGTindex/V-QUEST.php InstantClue...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...atistical Computing, https://www.r-project.org version 3.5.3 FastQC Babraham Bioinformatics, https://www.bioinformatics.babraham.ac.uk version 0.11.9 Samtools Genome Research Limited, http://www.htslib.org version 1.14 MACS2 https://github.com/macs3-project/MACS version 2.1.1.20160309 Recombinant Identification Program Los Alamos National Laboratory, https://www.hiv.lanl.gov/content/sequence/RIP/R...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: Resultant SAM files were filtered, sorted, and PCR duplicates removed, using SAMtools (samtools view, sort, and rmdup, respectively).
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: 81 https://imagej.nih.gov/ij/ R The Comprehensive R Archive Network https://cran.r-project.org/ Python Python Programming Language https://www.python.org/ BWA Li and Durbin 82 http://bio-bwa.sourceforge.net/bwa.shtml Picard Tools Broad Institute https://broadinstitute.github.io/picard Samtools Li et al.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **1.11**
- Evidence: We evaluated the quality of our ATAC-seq and peak calling procedures by measuring the mapping rates of each species-specific library with the flagstat utility in the samtools 1.11 package, 141 and the insert size distribution and fraction of reads in peaks using the plotEnrichment and bamPEFragmentSize utilities in deeptools .
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: Gene-level features for all genes listed as cyclins, cyclin dependent kinases, and class III Cys-based CDC25 phosphatases in the HGNC database 140 were selected from a recent chimpanzee gene annotation 141 and the coverage at each base across the full length of each gene in the set for each library was counted and summed using samtools mpileup 142 .
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Version used: **1.3.1**
- Evidence: PCR duplicates were further removed using samtools (v1.3.1) 67 , gene counts were computed using HTseq (v0.6.1) 68 , gene expression level (FPKM) was further calculated using cufflinks (v2.1.1) 66 .
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Version used: **1.12**
- Evidence: 94 https://github.com/comprna/SUPPA BSgenome.Dmelanogaster.UCSC.dm6 N/A https://bioconductor.org/packages/release/data/annotation/html/BSgenome.Dmelanogaster.UCSC.dm6.html Rsamtools_2.10.0 N/A https://bioconductor.org/packages/Rsamtools samtools 1.12 N/A https://github.com/samtools/htslib.git UpSetR 1.4.0.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Version used: **1.3.1**
- Evidence: Reads were flittered to reads smaller or equal to 120 bp using samtools (version 1.3.1).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **1.10**
- Evidence: The reads were mapped with HISAT2 v2.2.1, 101 the .sam files resulting from each mapping were converted into .bam files and indexed using SAMtools v1.10 102 and the reads mapped against each gene were counted using featureCounts v2.0.1.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Version used: **1.12**
- Evidence: 10005903 Software and algorithms Trim Galore! v0.0.6 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/ projects/trim_galore/ Bowtie2 v2.4.2 Langmead and Salzberg 69 https://github.com/BenLangmead/bowtie2 SAMtools v1.12 Li et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Version used: **1.10**
- Evidence: 87 SAMtools (version 1.10) 88 was used to discard the mapped reads with a mapping quality score <15, and PICARD tools (version 2.12.0) was applied to remove optical PCR duplicates.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### The fork protection complex promotes parental histone recycling and epigenetic memory. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.017 | PMCID: PMC11383432 | PMID: 39094569
- Version used: **1.12**
- Evidence: 111 https://www.rbvi.ucsf.edu/chimerax/ Bowtie2 v2.4.2 Langmead and Salzberg 112 https://github.com/BenLangmead/bowtie2 SAMtools v1.12 Danecek et al.
- Full pipeline: differential/statistical testing [R v4.2.2] -> visualisation [PyMOL v1.2r, ggpubr v0.6.0] -> stage not stated [AlphaFold, Bowtie2 v2.4.2, ChimeraX, MACS2, SAMtools v1.12, deepTools]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Evidence: 124 RRID: SCR_016366 SAMtools Danecek et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: Bam files were sorted with samtools software (v1.9).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **1.5**
- Evidence: 106 https://sourceforge.net/projects/subread/ BowTie2 v2.2.5 Langmead and Salzberg 107 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml Samtools v1.5 Danecek et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Evidence: GATK’s Haplotype Caller from the Genome Analysis Toolkit (GATK version 3.6) 104 SAMtools 105 , and Picard tools were used for variant calling.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### A synthetic differentiation circuit in Escherichia coli for suppressing mutant takeover. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.024 | PMCID: PMC10882425 | PMID: 38320549
- Version used: **1.12**
- Evidence: 82 https://github.com/lh3/minimap2 samtools (v.
- Full pipeline: stage not stated [SAMtools v1.12, minimap2 v2.21]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: ...ard deviations from the mean number of low quality sites called by breseq , (2) greater than 3 standard deviations from the mean error rate called by samtools , (3) less than 98% genome coverage, (4) mutect2 called a high proportion of “mixed” single nucleotide variants (less than 75% of single nucleotide variants called by mutect2 had an allele frequency greater than 90%), or (5) had greater than...
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Evidence: The code uses FastQC version v0.11.8 129 for sequence quality control before and after adaptor removal, cutadapt 130 version 3.5 with Python 3.7.12 for adaptor removal, SAMtools 131 version 1.9 for indexing, bwa 132 version 0.7.17-r1188 for mapping.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### In vivo prime editing rescues alternating hemiplegia of childhood in mice. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.038 | PMCID: PMC12702498 | PMID: 40695277
- Evidence: Using the SAMtools software package, the resulting Sequence Alignment Map (SAM) file was converted to a sorted binary alignment map (BAM) and demultiplexed into individual fastq files, each corresponding to a single target amplicon.
- Full pipeline: read trimming [Bowtie2, SAMtools] -> alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2] -> machine learning [MACS2]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **1.11.0**
- Evidence: 97 https://github.com/MikkelSchubert/adapterremoval BWA v0.7.17 Li and Durbin 98 https://github.com/lh3/bwa Picard tools v2.24 Broad Institute https://broadinstitute.github.io/picard/ Samtools v1.11.0 Li et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: Samtools were used to remove duplicates from mapped reads using ‘samtools rmdup’ and then sort and index.bam files.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **1.3.1**
- Evidence: Reads mapping to the reference genome were separated according to whether they were R1 or R2, sorted via samtools 1.3.1 (-n), and subsequently converted to bedGraph format using a custom script (bowtie2stdBedGraph.pl; 10.5281/zenodo.5519915).
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Version used: **1.3.1**
- Evidence: BAM files were sorted and indexed using Samtools (v.1.3.1) 73 and normalized (reads per kilobase of transcript per million (RPKM)) bigwigs were generated using Deeptools (v.3.1.3) 74 bamCoverage.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### Triangulation supports agricultural spread of the Transeurasian languages. (Nature 2021)

- DOI: 10.1038/s41586-021-04108-8 | PMCID: PMC8612925 | PMID: 34759322
- Version used: **1.3**
- Evidence: The cleaned reads with both base quality (Phred-scale quality) and mapping quality (Phred-scale mapping quality) over 30 were piled up by SAMtools 1.3 60 with the mpileup function.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12, SAMtools v1.3] -> simulation/modelling [BEAST v2.6]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Version used: **1.10**
- Evidence: The resulting SAM mapping file was converted into the BAM format, sorted and indexed using SAMtools v.1.10 (ref.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### Transposon-associated TnpB is a programmable RNA-guided DNA endonuclease. (Nature 2021)

- DOI: 10.1038/s41586-021-04058-1 | PMCID: PMC8612924 | PMID: 34619744
- Evidence: The remaining reads were mapped to the transposon-encoding plasmid (pTWIST-ISDra2; Supplementary Table 1 ) using BWA 35 and converted to the BAM file format with SAMtools 36 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [AlphaFold, Cutadapt, Python]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **1.9**
- Evidence: Following alignment, duplicate reads were removed using samtools v1.9 rmdup, which yielded only single copies of uniquely mapped paired reads in BAM format.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Biologically informed deep neural network for prostate cancer discovery. (Nature 2021)

- DOI: 10.1038/s41586-021-03922-4 | PMCID: PMC8514339 | PMID: 34552244
- Evidence: Reads were downloaded as FASTQs from TCGA (ISB-CGC; https://isb-cgc.appspot.com/ ) and as CRAMs from SU2C (from Amazon S3 bucket, dbGaP accession code, phs000915.v2.p2) and then converted to FASTQs using samtools fastq.
- Full pipeline: read trimming [Cutadapt v2.2, STAR] -> alignment/mapping [Cutadapt v2.2, RSEM, STAR] -> quantification [RSEM] -> stage not stated [SAMtools]

### Genome of a middle Holocene hunter-gatherer from Wallacea. (Nature 2021)

- DOI: 10.1038/s41586-021-03823-6 | PMCID: PMC8387238 | PMID: 34433944
- Version used: **1.3**
- Evidence: ...med 2 bp off the 1240K-captured double-stranded library data and genotyped the trimmed and untrimmed sequences individually for the 1240K panel using samtools v.1.3 ( https://github.com/samtools/samtools ) and pileupCaller v.1.4.0.2 ( https://github.com/stschiff/sequenceTools ), which randomly calls one allele per SNP site.
- Full pipeline: read trimming [BWA, SAMtools v1.3] -> alignment/mapping [BWA] -> variant calling [SAMtools v1.3] -> differential/statistical testing [ggplot2 v3.3.3] -> visualisation [ggplot2 v3.3.3] -> stage not stated [PLINK v1.9, QGIS]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **1.9**
- Evidence: The resulting alignment file was sorted and indexed with SAMtools (v.1.9) 78 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Initial Upper Palaeolithic humans in Europe had recent Neanderthal ancestry. (Nature 2021)

- DOI: 10.1038/s41586-021-03335-3 | PMCID: PMC8026394 | PMID: 33828320
- Evidence: PCR duplicates were removed using bam-rmdup (version: 0.6.3; https://github.com/mpieva/biohazard-tools ) and SAMtools (version: 1.3.1) 52 was used to filter for fragments that were at least 35 bp long and that had a mapping quality equal to or greater than 25.
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R] -> stage not stated [BEDTools]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **1.2**
- Evidence: FASTQ files were aligned to hg19 (NCBS build 36) using bowtie2 (v2.2.6) 32 and converted from SAM to BAM files with SAMtools (v1.2) 33 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: Sorted and indexed BAM files were generated using samtools 72 v.0.1.19 and transcripts per feature (based on the Prokka annotation) were quantified using EDGE-pro 73 v.1.3.1 and standard settings.
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Million-year-old DNA sheds light on the genomic history of mammoths. (Nature 2021)

- DOI: 10.1038/s41586-021-03224-9 | PMCID: PMC7116897 | PMID: 33597750
- Version used: **1.10**
- Evidence: After obtaining initial quality metrics for the genomes, we removed reads <35 base pairs from the BAM-files using samtools v1.10 33 and awk for all remaining analysis ( Supplementary Section 4 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.921, BCFtools, Picard, RepeatMasker v4.0.7, SAMtools v1.10]

### Loop extrusion as a mechanism for formation of DNA damage repair foci. (Nature 2021)

- DOI: 10.1038/s41586-021-03193-z | PMCID: PMC7116834 | PMID: 33597753
- Evidence: Each sample was then demultiplexed using a specific python script from the FourCSeq R package 47 thus assigning each read to a specific viewpoint based to its primer sequence into separate fastQ files. bwa mem was then used for mapping and samtools for sorting and indexing.
- Full pipeline: read trimming [R, SAMtools] -> alignment/mapping [R, SAMtools] -> normalisation [Bioconductor, deepTools] -> differential/statistical testing [deepTools] -> visualisation [Bioconductor] -> stage not stated [MACS2, ggplot2]

### Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. (Nature 2021)

- DOI: 10.1038/s41586-021-03205-y | PMCID: PMC7875770 | PMID: 33568819
- Evidence: Fusera, samtools and other tools are also packaged in a Docker container for ease of use and are available for download from Docker Hub 83 .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> stage not stated [BWA, Docker, GATK v3.5.0, R, SAMtools, VEP]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Evidence: The BAM index of mapped reads corresponding to the 16 KIN-CLIP libraries was then converted to BED/bedgraph using the standard command line version of –bedtools (V2.29.1) and –samtools (V1.10) 42 .
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Version used: **1.11**
- Evidence: BAM files were then sorted and indexed with samtools v1.11 and PCR optical duplicates removed using Picard ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: Multi-sample SNP calling was done using SAMtools mpileup 88 and Varscan V2.4.0 89 with a minimum coverage of eight and a minimum alternate allele count of four.
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Evidence: First, we used “samtools view” (v0.1.18) 54 to extract any reads that map to AAV9 C- or N-terminal contigs.
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### A genetic history of the pre-contact Caribbean. (Nature 2021)

- DOI: 10.1038/s41586-020-03053-2 | PMCID: PMC7864882 | PMID: 33361817
- Evidence: We constructed a consensus sequence with samtools and bcftools version 1.3.1 using a majority rule and then determined the haplogroup with HaploGrep2, using Phylotree version 17.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard] -> structure determination [BWA v0.7.15] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.3.1, SAMtools]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: Read pairs were next sorted based on genomic coordinates followed by PCR duplicate removal using samtools rmdup.
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Measuring DNA mechanics on the genome scale. (Nature 2021)

- DOI: 10.1038/s41586-020-03052-3 | PMCID: PMC7855230 | PMID: 33328628
- Evidence: In addition to Bowtie 1 36 , SAMtools 37 , smCamera, and MATLAB (Matworks) versions 9.0, 9.2, 9.4, 9.6 were used to analyze the data.
- Full pipeline: stage not stated [SAMtools]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Evidence: Alignments were sorted and indexed with samtools 43 , and aligned reads assigned to the Ensembl reference transcriptome release 90 with featureCounts 44 .
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Version used: **1.3.1**
- Evidence: Non-concordant read pairs were then removed from the BAM file using Samtools (version 1.3.1) 63 . bedtools (version 2.17.0) was used to convert BAM files to BED files and to extend each read to 15bp upstream and 22bp downstream from the read 5’-end in a stranded manner 64 , in order to account for steric hindrance of Tn5-DNA contacts 65 .
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: URLs for software use BCFtools, http://samtools.github.io/bcftools/ ; BOLT-LMM, https://data.broadinstitute.org/alkesgroup/BOLT-LMM/ ; cov-LDSC, https://github.com/immunogenomics/cov-ldsc ; EAGLE, https://alkesgroup.broadinstitute.org/Eagle/ ; GCTA, http://cnsgenomics.com/software/gcta/ ; IMPUTE2, https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; LDpred, https://github.com/bvilhjal/ldpred/ ; ...
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: All alignments were hereafter merged using samtools and sorted using gz-sort (v.
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Evidence: SAM files were converted to BAM by using samtools-1.2 view –b and sorted with samtools-1.2 sort.
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Evidence: Duplicated reads were removed using Samtools-1.7 rmdup.
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **1.9**
- Evidence: After sorting the reads with SAMtools v1.9 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: ...x asm20 -t96 -r2k dbg.raw.fa ../rawdata/SRR10382244.fasta ../rawdata/SRR10382245.fasta’; ‘../rawdata/SRR10382248.fasta ../rawdata/SRR10382249.fasta | samtools sort -m 2g -@96 -o dbg.bam’; ‘samtools view -F0x900 dbg.bam | wtpoa-cns -t 96 -d dbg.raw.fa -i - -fo dbg.cns.fa’; ‘ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: Extracting mitochondrial DNA sequences and detecting variants The subset of sequencing reads which aligned to the mitochondrial genome were extracted from each WGS BAM file using Samtools 57 .
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Version used: **1.9**
- Evidence: Ten million reads from each individual technical replicate were subsetted (SAMtools v1.9, seed 1) and merged, and each condition was then merged across biological replicates.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### The Anglo-Saxon migration and the formation of the early English gene pool. (Nature 2022)

- DOI: 10.1038/s41586-022-05247-2 | PMCID: PMC9534755 | PMID: 36131019
- Evidence: A pileup file was generated using samtools mpileup with parameters -q 30 -Q 30 -B containing only sites overlapping with our capture panel.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA, Picard] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, SAMtools]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **1.11**
- Evidence: Alignment files were individually name-sorted using Samtools v1.11 57 , and then used to create a cell-by-gene count matrix using featureCounts 58 (subread v2.0.1).
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: Alignment files were converted to BAM files using SAMtools 48 (settings: -bS -t).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### The role of somatosensory innervation of adipose tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05137-7 | PMCID: PMC9477745 | PMID: 36045288
- Version used: **1.10**
- Evidence: NGS data alignment and processing Raw FASTQ files from NGS runs were aligned to an AAV9-template DNA fragment containing the 21 bp diversified region between amino acids 588 and 589 using SAMtools (v.1.10).
- Full pipeline: alignment/mapping [SAMtools v1.10, Salmon v1.5.1] -> quantification [ImageJ, Salmon v1.5.1] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [Metascape]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Version used: **1.9**
- Evidence: Furthermore, we created a sequence cache of the reference FASTA file using the ‘seq_cache_populate.pl’ script distributed with samtools 1.9.
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### ADAR1 averts fatal type I interferon induction by ZBP1. (Nature 2022)

- DOI: 10.1038/s41586-022-04878-9 | PMCID: PMC9329096 | PMID: 35859176
- Evidence: Detection and analysis of A-to-I editing Read alignments were processed with samtools markdup 57 to identify likely PCR duplicates within the sequenced libraries, and A-to-I editing was assessed using JACUSA2 (ref.
- Full pipeline: quality control [Cutadapt v3.4, FastQC v0.11.8] -> read trimming [Cutadapt v3.4, FastQC v0.11.8] -> alignment/mapping [HISAT2 v2.1.0, SAMtools, featureCounts] -> quantification [DESeq2 v1.22.1] -> normalisation [DESeq2 v1.22.1] -> differential/statistical testing [DESeq2 v1.22.1] -> visualisation [DESeq2 v1.22.1] -> stage not stated [QuPath v0.3.2]

### Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission. (Nature 2022)

- DOI: 10.1038/s41586-022-05049-6 | PMCID: PMC9433318 | PMID: 35798029
- Evidence: Sequencing depth and SNV calls were obtained using samtools mpileup 31 and the iVar variants method 20 .
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Python] -> stage not stated [SAMtools, kallisto]

### A male steroid controls female sexual behaviour in the malaria mosquito. (Nature 2022)

- DOI: 10.1038/s41586-022-04908-6 | PMCID: PMC9352575 | PMID: 35794471
- Version used: **1.3.1**
- Evidence: Reads with mapping quality (MAPQ) scores <30 were removed using Samtools (version 1.3.1).
- Full pipeline: alignment/mapping [HISAT2 v2.0.5, HTSeq v0.9.1, SAMtools v1.3.1] -> quantification [DESeq2, R v4.0.3] -> normalisation [DESeq2, R v4.0.3] -> differential/statistical testing [DESeq2, R v4.0.3]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Version used: **1.9**
- Evidence: Mitochondrial genome phylogenetic analysis and evolutionary dating We extracted reads mapped to the mitochondrial genome for the ancient wolf samples using samtools (v1.9) 74 .
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### GTSF1 accelerates target RNA cleavage by PIWI-clade Argonaute proteins. (Nature 2022)

- DOI: 10.1038/s41586-022-05009-0 | PMCID: PMC9385479 | PMID: 35772669
- Version used: **1.8**
- Evidence: Mapped results were generated in SAM format, duplicates removed and translated to BAM format using SAMtools 1.8 80 .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4, HTSeq v0.9.1, RAxML v1.0.0, SAMtools v1.8, STAR v2.3] -> quantification [HTSeq v0.9.1] -> visualisation [Clustal Omega v1.2.4, RAxML v1.0.0] -> stage not stated [Bowtie2 v2.5]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Version used: **1.3**
- Evidence: Subsequently, we used SAMtools v.1.3 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **1.9**
- Evidence: To infer the phylogeny of the 432 accessions, reads were mapped to the DM v4 reference genome using BWA (0.7.5a-r405) 49 , and single-nucleotide polymorphisms (SNPs) were then extracted using SAMtools (v.1.9) 50 and BCFtools (v.1.9) 49 .
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Version used: **1.2**
- Evidence: Quality metrics were compiled from PICARD (v1.134), FASTQC (v0.11.3), Samtools (v1.2), and HTSeq-count (v0.4.1).
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: Reads were filtered by mapping quality 60 (samtools view -q 40) and fragment length 61 (deepTools alignmentSieve --maxFragmentLength 120).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **1.6**
- Evidence: Samtools (v.1.6) 52 was used to convert SAM format to BAM format.
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: After reads were aligned to the genome, sambamba 64 was used to remove duplicates and samtools 65 was used to filter out read pairs that were not properly paired.
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Evidence: Uniquely mapped reads were then filtered for using the command ‘samtools view -b -q 255’.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Evidence: Extensive quality control was performed using SAMtools 58 and Picard Tools 59 to confirm sex and tissue of origin.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **1.9**
- Evidence: RNASEH2B copy number was determined using a combination of Canvas, Manta, read depth counts with samtools (v.1.9) and confirmed by manual inspection using IGV (v.2.5.0) 68 .
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Attenuated fusogenicity and pathogenicity of SARS-CoV-2 Omicron variant. (Nature 2022)

- DOI: 10.1038/s41586-022-04462-1 | PMCID: PMC8942852 | PMID: 35104835
- Version used: **1.9**
- Evidence: Variant calling, filtering and annotation were performed using SAMtools v.1.9 48 and snpEff v.5.0e 49 .
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [fastp v0.21.0] -> variant calling [SAMtools v1.9] -> differential/statistical testing [Stan v2.28.1] -> simulation/modelling [Stan v2.28.1] -> stage not stated [BWA v0.7.17, ImageJ, R v3.6]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Evidence: After adapter and quality trimming with cutadapt (version 2.3) and removing duplicates with samtools markdup (version 1.10), reads were aligned to the TAIR10 reference genome with bwa-mem (version 0.7.17) and variants were called independently for each sample with GATK HaplotypeCaller version 4.1.0.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Version used: **1.3.1**
- Evidence: Paired-end .fastq files were trimmed and uniquely aligned to the GRCh38/hg38 human genome assembly using Novoalign (Novocraft) (with the parameters -r None -k -q 13 -k -t 60 -o sam –a CTGTCTCTTATACACATCT), and converted to .bam files using SAMtools (version 1.3.1).
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Enhanced fusogenicity and pathogenicity of SARS-CoV-2 Delta P681R mutation. (Nature 2022)

- DOI: 10.1038/s41586-021-04266-9 | PMCID: PMC8828475 | PMID: 34823256
- Version used: **1.9**
- Evidence: Variant calling, filtering and annotation were performed using SAMtools (v.1.9) 41 and snpEff (v.5.0e) 42 .
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [MAFFT, fastp v0.21.0] -> variant calling [SAMtools v1.9] -> stage not stated [BWA v0.7.17, IQ-TREE, ImageJ v2.2.0]

### Genome surveillance by HUSH-mediated silencing of intronless mobile elements. (Nature 2022)

- DOI: 10.1038/s41586-021-04228-1 | PMCID: PMC8770142 | PMID: 34794168
- Evidence: Bioinformatics data processing and analyses were performed using Bash (v4.2.46), R (v3.6) and Python (v3.8.5) programming languages as well as the following tools: FastQC (Babraham Bioinformatics) (v0.11.7) cutadapt 37 (v1.16), HISAT2 38 (v2.1.0), SAMtools 39 (v1.9), sambamba 40 (v0.6.6) and deepTools 41 (v3.1.0).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, HISAT2, SAMtools, deepTools] -> stage not stated [RepeatMasker, data.table v1.13.2, edgeR]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Version used: **1.9**
- Evidence: ...ol; (3) mapping (one-pass mapping for snmC, two-pass mapping for snm3C) (bismark v.0.20, bowtie2 v.2.3); (4) BAM file processing and quality control (samtools v.1.9, picard v.3.0.0); (5) methylome profile generation (ALLCools v.1.0.8); and (6) chromatin contact calling.
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Version used: **1.9**
- Evidence: Files were converted with SAMtools v.1.9 and BEDtools v.2.26.0 to generate bedgraph files 43 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: 63 ), v.2.3); (4) BAM file processing and QC (samtools 64 , v.1.9; Picard, v.3.0.0); (5) methylome profile generation (allcools, v.1.0.8); and (6) chromatin contact calling (snm3C-seq only).
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: De novo motif analysis of FOXP3-occupied sites in vitro and in vivo FoxP PD-seq data were mapped to mm10 using Bowtie2 54 and sorted using samtools 55 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Evidence: W created consensus sequences with samtools and bcftools version 1.31 using majority rule and then using HaploGrep2 with Phylotree version 17.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: Duplicated reads were then marked using Picard (v.2.9.4) and only non-duplicated proper paired reads were kept according to SAMtools (parameter ‘-q 1 -F 1804’ v1.9).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: The output SAM file was converted to a BAM using samtools ( https://github.com/samtools/samtools ; v.1.14) view with parameter -Shb, and all of the other parameters set to default.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Bacteriophages suppress CRISPR-Cas immunity using RNA-based anti-CRISPRs. (Nature 2023)

- DOI: 10.1038/s41586-023-06612-5 | PMCID: PMC10651486 | PMID: 37853129
- Version used: **1.16.1**
- Evidence: 57 ) with local parameters and the alignment was converted to BAM format using SAMtools v.1.16.1 (ref.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2, MAFFT, SAMtools v1.16.1]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: Samtools was used to generate BAM files with reads based on their mapping location (hg19 or dm6).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **1.6**
- Evidence: Outputs (.sam) from Bowtie2 were converted to bam files and sorted using samtools (v.1.6).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **1.9**
- Evidence: ...alTimeGenomics/rtg-tools ), bcl2fastq (v2.20.0.422, https://support.illumina.com/sequencing/sequencing_software/bcl2fastq-conversion-software.html ), Samtools (v1.9, v1.3, https://github.com/samtools/samtools ), samblaster (v0.1.24, https://github.com/GregoryFaust/samblaster ), BWA (v0.7.10 mem, https://github.com/lh3/bwa ), GenomeAnalysisTKLite (v2.3.9, https://github.com/broadgsa/gatk ), Picard ...
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Version used: **1.10**
- Evidence: ...et ) with the parameters ‘-v 1 -M 1 -y --best --strata --trim5 4 --trim3 4 -S’ and the SAM alignment files were converted into sorted BAM files using Samtools v.1.10 ( http://www.htslib.org ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Version used: **1.9**
- Evidence: Computing mean nucDNA coverage in UKB As mean nucDNA coverage was not available for UKB, we used samtools v.1.9 idxstats 56 , samtools flagstat and GATK v.4.2.6.0 CollectQualityYieldMetrics as part of the mtSwirlMulti pipeline to efficiently and economically estimate mean coverage on the nucDNA.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Version used: **1.13**
- Evidence: Alignment maps were filtered with samtools (version 1.13) to only keep primary alignments with a length ≥800 bp, and a mapping quality 50 of 60.
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Version used: **1.7**
- Evidence: Primary alignments were selected using samtools (v.1.7) and reads per genomic feature were counted with featureCounts (v.2.0.1 from Subread package).
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### R-loop-dependent promoter-proximal termination ensures genome stability. (Nature 2023)

- DOI: 10.1038/s41586-023-06515-5 | PMCID: PMC10511320 | PMID: 37557913
- Version used: **1.12**
- Evidence: All unmapped reads, low mapping quality reads (MAPQ < 30) and PCR duplicates were removed using SAMtools (v.1.12) 59 and the MarkDuplicates function of Picard Tools v.2.25.5 (Broad Institute).
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [Picard, SAMtools v1.12] -> quantification [Trim Galore v0.6.6] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [Trim Galore v0.6.6] -> stage not stated [ImageJ, MACS2 v2.2.7.1, R]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: Trimmed high-quality reads from the two parents were aligned to the TA299 and TA10622 assemblies separately using SAMtools 69 (v.1.8) and variants were called using BCFtools (v.1.9) 70 .
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Evolutionary histories of breast cancer and related clones. (Nature 2023)

- DOI: 10.1038/s41586-023-06333-9 | PMCID: PMC10432280 | PMID: 37495687
- Evidence: Mutation calling for WGA organoid samples was performed after merging each pair of two .bam files of WGA samples derived from a single organoid using Samtools 59 (v.1.10); each mutation call was then reviewed back to the original two .bam files using GenomonMutationFilter 2 (v.0.2.1); mutations detected in both the WGA samples with two or more variant reads each were considered true somatic mutati...
- Full pipeline: stage not stated [ANNOVAR, MACS2, Mutect2, R, SAMtools]

### Early contact between late farming and pastoralist societies in southeastern Europe. (Nature 2023)

- DOI: 10.1038/s41586-023-06334-8 | PMCID: PMC10412445 | PMID: 37468624
- Version used: **1.3**
- Evidence: Coverage statistics calculations and bam filtering were done using samtools (v.1.3; ref.
- Full pipeline: quality control [ANGSD] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools v1.3]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Version used: **1.10**
- Evidence: The sorted BAM files were indexed using SAMtools (v.1.10) (ref.
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### Cooperation between bHLH transcription factors and histones for DNA access. (Nature 2023)

- DOI: 10.1038/s41586-023-06282-3 | PMCID: PMC10338342 | PMID: 37407816
- Version used: **1.6**
- Evidence: (parameter “--end-to-end --very-sensitive --no-unal --no-mixed --no-discordant -X 400”) and filtered for quality using SAMtools 1.6 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bioconductor, Bowtie2, ChimeraX, PyMOL] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.6, ImageJ, RELION, SAMtools v1.6]

### Continuous synthesis of E. coli genome sections and Mb-scale human DNA assembly. (Nature 2023)

- DOI: 10.1038/s41586-023-06268-1 | PMCID: PMC7614783 | PMID: 37380776
- Version used: **1.16.1**
- Evidence: The alignment files were indexed and filtered using Samtools (v1.16.1) 47 for unique mapping and pairing (view -q 10 -F 1284 -f 0x02).
- Full pipeline: read trimming [minimap2] -> alignment/mapping [SAMtools v1.16.1, minimap2] -> variant calling [Mutect2] -> stage not stated [GATK v4.3.0, Python, RepeatMasker, deepTools v3.5.1]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: A sorted BAM file was obtained and indexed using SAMtools with the ‘sort’ and ‘index’ commands (version 1.10).
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Single-cell quantification of ribosome occupancy in early mouse development. (Nature 2023)

- DOI: 10.1038/s41586-023-06228-9 | PMCID: PMC10307641 | PMID: 37344592
- Evidence: 64 ) for all alignments and SAMtools 65 version 1.11 for processing BAM files.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ, R v4.0, Seurat]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Version used: **1.0.0**
- Evidence: Unaligned reads were mapped to mouse genome mm10 using STAR (v.2.3.1) 65 , alignments with soft clipping of ends were removed using SAMtools (v.1.0.0) 68 and reads with the same 5′ end were merged to represent a single 5′-monophosphorylated RNA species.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### A pangenome reference of 36 Chinese populations. (Nature 2023)

- DOI: 10.1038/s41586-023-06173-7 | PMCID: PMC10322713 | PMID: 37316654
- Evidence: Variant identification from the phased assembly The obtained HiFi reads were aligned to the T2T-CHM13 v2.0 reference by minimap2 using the preset parameters -ax map-hifi, and then sorted by samtools sort.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> variant calling [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BCFtools, QUAST v5.2.0, pheatmap v1.0.12]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Version used: **1.3.1**
- Evidence: Trimmed reads were mapped back to the contigs to determine read coverage using Bowtie 2 (v.2.2.9) 56 , 65 and SAMtools (v.1.3.1) 66 .
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Northwest African Neolithic initiated by migrants from Iberia and Levant. (Nature 2023)

- DOI: 10.1038/s41586-023-06166-6 | PMCID: PMC10266975 | PMID: 37286608
- Evidence: For each library we merged bam files resulting from all resequencing rounds using SAMtools merge v.1.5 (ref.
- Full pipeline: variant calling [GATK v3.5.0] -> registration [GATK v3.5.0] -> dimensionality reduction/clustering [ADMIXTURE, QGIS] -> stage not stated [BCFtools, PLINK v1.9, SAMtools]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: Mutations were quantified using samtools mpileup.
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: For long-term dnMCAK and micronuclei ATAC-seq experiments in RPE-1 and 4T1 cells, reads were mapped to the hg38 (RPE-1) or mm10 (4T1) genome assembly using Bowtie2 with the following parameters: -X2000 --no-mixed --no-discordant and reads were filtered using samtools for the 1804 FLAG and mapq score of 30.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### A Pseudomonas aeruginosa small RNA regulates chronic and acute infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06111-7 | PMCID: PMC10247376 | PMID: 37225987
- Version used: **1.13**
- Evidence: To examine the alignment pattern of sicX reads, samtools v1.13 was used to measure the read depth encompassing the sicX locus at each nucleotide position 62 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.4.2, Cutadapt v3.0] -> alignment/mapping [Bowtie2 v2.4.2, MUSCLE, SAMtools v1.13] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R, featureCounts]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Version used: **1.3.1**
- Evidence: We used Samtools (v1.3.1) 53 to merge the realigned bam fragments and Picard (v2.8.0) to add read groups and to mark PCR duplicates.
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: Samtools was used to pass through the mapped reads and calculate statistics.
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Version used: **1.6**
- Evidence: Clonality Whole-exome sequence reads of tumour–normal paired samples of patients were aligned to the reference human genome (hg19) using the Burrows–Wheeler alignment tool (bwa mem v.0.7.17) and samtools (v.1.6).
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: These contigs were then dropped from the assemblies using a WDLized version of samtools faidx.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: 44 ; minimum identity of 95%) and stored the recruited reads as BAM files using samtools 45 ; anvi’o profiled each BAM file to estimate the coverage and detection statistics of each contig, and combined mapping profiles into a merged profile database for each metagenomic set.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **1.9**
- Evidence: Next, RNA coverage was calculated for single nucleotide variants (SNVs) detected in matched whole-exome sequencing data per tumour region using SAMtools (v.1.9) 61 mpileup.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Version used: **1.9**
- Evidence: Further quality control following alignment was performed using a combination of Somalier (0.2.7, https://github.com/brentp/somalier ), Samtools (v.1.9) 45 , Picard Tools and Conpair (v.0.2) 46 to identify sample swaps or contamination events.
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: Mapped reads in SAM format were converted to BAM format; BAM files were sorted and indexed using SAMtools 138 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Version used: **1.12**
- Evidence: BAM files were sorted with a chromosome coordinate using samtools (v.1.12).
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: Samtools 47 (version 1.9) and Picard (version 2.26.9; http://broadinstitute.github.io/picard/ ) were used to sort, deduplicate and index the alignments, and to create a depth file, which was plotted using a custom script in R.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Version used: **1.10**
- Evidence: Mapping and processing Paired-end fastq files for each sample were aligned jointly to human_g1k_hs37d5 from the 1000 Genomes Phase 3 using bwa mem (v.0.7.17) and sorted with samtools (v.1.10) 90 using the sort command.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **1.15.1**
- Evidence: The alignments were converted to BAM format using SAMtools v1.15.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Palaeogenomics of Upper Palaeolithic to Neolithic European hunter-gatherers. (Nature 2023)

- DOI: 10.1038/s41586-023-05726-0 | PMCID: PMC9977688 | PMID: 36859578
- Evidence: Reads with a mapping quality below 30 were then filtered with samtools, and the consensus sequences were generated by Schmutzi 69 .
- Full pipeline: quality control [ANGSD v0.934] -> read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12, SAMtools] -> differential/statistical testing [R v3.5]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Evidence: Fastq sequences were obtained using bam format aligned sequences of one randomly selected father per species and were converted into fastq format using samtools mpileup command and vcf2fq.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Version used: **1.10**
- Evidence: The resulting SAM files were converted to BAM files using the SAMtools (v.1.10) view command, after which the BAM files were sorted and indexed, and potential PCR duplicates were removed using the rmdup function.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: Duplicates were subsequently removed using samtools/1.3.1 samtools view -b -F 1796.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **1.9**
- Evidence: Gene prediction and functional annotation We used SAMtools (v.1.9) 62 and the annotation of repeats to soft mask O. fusiformis genome assembly before gene prediction.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### A DNA methylation atlas of normal human cell types. (Nature 2023)

- DOI: 10.1038/s41586-022-05580-6 | PMCID: PMC9811898 | PMID: 36599988
- Version used: **1.9**
- Evidence: WGBS computational processing Paired-end FASTQ files were mapped to the human (hg19, hg38), lambda, pUC19 and viral genomes using bwa-meth (v.0.2.0) 51 then converted to BAM files using SAMtools (v.1.9) 52 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> dimensionality reduction/clustering [SciPy v1.6.3] -> differential/statistical testing [HOMER] -> stage not stated [BEDTools v2.26.0, deepTools v3.4.1, scikit-learn]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Mapped reads were filtered and sorted using the samtools ‘view’ and ‘sort’, respectively.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Phenotypic signatures of immune selection in HIV-1 reservoir cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05538-8 | PMCID: PMC9908552 | PMID: 36599977
- Version used: **1.9**
- Evidence: Single-cell alignments were filtered according to criteria implemented in the Tapestri pipeline, and indexed using samtools (v1.9) 56 .
- Full pipeline: quality control [UMAP] -> alignment/mapping [MAFFT, SAMtools v1.9] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [R] -> visualisation [MAFFT, UMAP] -> stage not stated [Cutadapt v2.5]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Version used: **1.6**
- Evidence: The mapped files were converted to BAM and sorted with samtools v1.6 56 , and duplicated reads were removed with GATK v4.1.0.0 MarkDuplicates 57 .
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **1.3.1**
- Evidence: Low-mapping-quality reads were removed using samtools (v.1.3.1) 91 with the settings ‘-q 30’.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Mapped reads were converted to BAM format using samtools 75 , and bedtools bamtofastq 76 was used to obtain the reads in FASTQ format.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Version used: **1.13**
- Evidence: For each rRE locus and sample in its corresponding cancer, samtools v1.13 was used with the parameter depth -r to find the read depth at each base pair within the locus and a 500-bp region encompassing the start and stop positions of the TR.
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **1.12**
- Evidence: Finally, published datasets that had been generated at WSI were downloaded from iRODs v.4.2.7 in the form of cram files and converted to fastq files using samtools v.1.12. using the command ‘samtools collate -O -u -@16 $CRAM $TAG.tmp | samtools fastq -N -F 0×900 -@16 −1 $TAG.R1.fastq.gz −2 $TAG.R2.fastq.gz -’.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: Read depth was calculated with SAMtools 78 v.1.16.1.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Version used: **1.8**
- Evidence: Reads with MAPQ values less than 10 were filtered using SAMtools (v.1.8).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Version used: **1.9**
- Evidence: Aligned reads were filtered for quality using samtools (v.1.9) 71 , duplicate fragments were removed using Picard’s MarkDuplicates (v.2.25.3) and peaks were called using MACS2 (v.2.2.7.1) 72 with a q -value cut-off of 0.01 and with a no-shift model.
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Version used: **1.20**
- Evidence: The reads were first converted back to FASTQ format using samtools (version 1.20).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Version used: **1.11**
- Evidence: Reads were sorted using SAMtools (v1.11, RRID: SCR_002105 ), and mitochondrial and pseudo-chromosomal alignments were removed.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tissue spaces are reservoirs of antigenic diversity for Trypanosoma brucei. (Nature 2024)

- DOI: 10.1038/s41586-024-08151-z | PMCID: PMC11634766 | PMID: 39478231
- Evidence: The following software and versions were used in the pipeline: Trinity 51 , 52 (v.2.8.5), Bowtie 53 (v.1.2.3), Biopython 54 (v.1.72), Blast 55 , 56 (v.2.9), Bedtools 57 (v.2.29.2), cd-hit 58 , 59 (v.4.8.1), trim-galore 60 (v.0.6.4) and samtools 61 (v.1.9).
- Full pipeline: alignment/mapping [deepTools] -> visualisation [R] -> stage not stated [Cutadapt, ImageJ v1.53, SAMtools]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: The output SAM file was converted to a BAM file using the samtools ( https://github.com/samtools/samtools ; v.1.14) view with parameters -Shb, and all others set to default.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Evidence: Pileup files were generated using Samtools (options -B -q 1), followed by variant calling with VarScan2 (options --min-coverage 100, --min-var-freq 0.01).
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### Anti-viral defence by an mRNA ADP-ribosyltransferase that blocks translation. (Nature 2024)

- DOI: 10.1038/s41586-024-08102-8 | PMCID: PMC11618068 | PMID: 39443800
- Evidence: Sam files generated from bowtie2 mapping were then converted to bam files using samtools 56 (version 1.7) and then further converted to numpy arrays using the genomearray3 python library 57 for use in downstream analyses.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, NumPy, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, HMMER]

### Circadian plasticity evolves through regulatory changes in a neuropeptide gene. (Nature 2024)

- DOI: 10.1038/s41586-024-08056-x | PMCID: PMC11602725 | PMID: 39415010
- Version used: **1.19.2**
- Evidence: We obtained 41 D. sechellia genomes sampled in the Seychelles archipelago from the Sequence Read Archive 42 , aligned them to the D. sechellia reference genome (ASM438219v2), phasing the data by chromosome (Samtools v.1.19.2), and created consensus sequences for the 82 Pdf 5’-regulatory haplotypes.
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551, SAMtools v1.19.2] -> variant calling [SAMtools v1.19.2] -> visualisation [R]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: SAM files were converted to BAM files using samtools 73 .
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **1.18**
- Evidence: Assembly of circular ecDNA contigs ONT reads were aligned to GRCh38 with minimap2 (v.2.26-r1175) 112 with flags -a–L -–D --cs -x map-ont, and coordinate-sorted with samtools (v.1.18) 113 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Evidence: Each variant call produced by each of the tools was manually checked by analysing the read alignments at variant positions using samtools pileup.
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Version used: **1.16.1**
- Evidence: Mapped reads were separated by strands with samtools (v.1.16.1) 63 and peaks on each strand were called using MACS2 (v.2) 56 with parameter ‘-nomodel, --keep-dup 5, -g 1.3e8, -extsize 150’ separately.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Alignments were filtered to remove duplicate reads with Picard MarkDuplicates v.2.24.0 ( http://broadinstitute.github.io/picard/ ) and improper alignments with Samtools view v.1.11 -F 260 -f 3 (ref.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Ancient Rapanui genomes reveal resilience and pre-European contact with the Americas. (Nature 2024)

- DOI: 10.1038/s41586-024-07881-4 | PMCID: PMC11390480 | PMID: 39261618
- Evidence: We retained mapped reads with a mapping quality greater than 30, removed PCR duplicates using picard MarkDuplicates ( http://picard.sourceforge.net ), carried out local realignment using GATK 82 and computed the MD tag and extended BAQ for each read using the samtools calmd command.
- Full pipeline: alignment/mapping [GATK, SAMtools] -> normalisation [ADMIXTURE] -> registration [GATK, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [Matplotlib v3.5.3, R, ggplot2 v3.3.2] -> stage not stated [ANGSD v0.930, PLINK v1.9.20200712]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Evidence: For each short-read sample, extracted all the reads spanning the region of interest using SAMTOOLS (v1.18; ‘samtools fasta’) 67 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **1.17**
- Evidence: The output.sam files were name-sorted and duplicate reads were marked and removed using SAMtools (v.1.17) 83 .
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **1.10**
- Evidence: Trimmed paired-end reads were aligned to the corresponding genome assembly using STAR (v2.7.10b) 62 with the parameters “--twopassMode basic --outFilterMismatchNMax 5 --outFilterMatchNminOverLread 0.80 --alignMatesGapMax 100000 --outSAMstrandField intronMotif --runMode alignReads” and the results were filtered and sorted using SAMtools (v1.10) 63 .
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **1.10**
- Evidence: Alignments were filtered by mapping quality (mapQ ≥ 30), and PCR duplicates were removed using SAMtools (v1.10) 101 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **1.0**
- Evidence: Downstream processing was done using the Genome Analysis Toolkit (GATK, v.3.4), SAMtools (v.1.0) and Picard Tools ( http://picard.sourceforge.net ; v.1.92).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: SAMtools was used to sort and isolate uniquely mapped reads using “-f 2 -q 10 -b -@ 20” options.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### De novo variants in the RNU4-2 snRNA cause a frequent neurodevelopmental syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07773-7 | PMCID: PMC11338827 | PMID: 38991538
- Evidence: Assessing the sensitivity to detect the n.64_65insT variant in exome sequencing data We used a Python script that uses samtools mpileup to retrieve the coverage and base change at the n.64_65 critical locus to identify putative carriers of the insertion ( https://github.com/francois-lecoquierre/genomics_shortcuts/blob/main/find_RNU4-2_recurrent_variant.py ).
- Full pipeline: alignment/mapping [BEDTools v2.31.0, STAR] -> quantification [STAR] -> normalisation [STAR] -> stage not stated [Python, R v4.0.2, SAMtools]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Evidence: The read depths were counted by samtools bedcov.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Version used: **1.12**
- Evidence: The resulting alignments were converted to BAM files and merged, sorted and filtered using Samtools (v.1.12).
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Geographical migration and fitness dynamics of Streptococcus pneumoniae. (Nature 2024)

- DOI: 10.1038/s41586-024-07626-3 | PMCID: PMC11236706 | PMID: 38961295
- Evidence: We multiply mapped all genomes from each dominant GPSC against these references, respectively, using a custom mapping, variant calling and local realignment around indels pipeline (multiple_mappings_to_bam.py) 57 using bwa-MEM (v.0.7.17) 58 and samtools mpileup (v.1.6) 59 .
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SAMtools] -> registration [SAMtools] -> differential/statistical testing [BEAST v1.10.4, R v3.6.2] -> stage not stated [RAxML]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **1.9**
- Evidence: Non-unique mapped and duplicated reads were excluded using SAMtools (v1.9) 44 and Picard (v2.20.3-SNAPSHOT; http://picard.sourceforge.net ), respectively.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Evidence: Multiallelic mutation rates Aligned reads spanning genomic positions of somatic mutations were re-genotyped using SAMtools mpileup (v1.9) 61 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Version used: **1.3**
- Evidence: Samtools (v.1.3) was used for indexing and filtering of unmapped sequences, and low-complexity reads were removed using a parallelized implementation of PRINSEQ (-lc_method dust, -lc_threshold 7; https://github.com/spabinger/prinseq_parallel ; refs.
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Ancient genomes reveal insights into ritual life at Chichén Itzá. (Nature 2024)

- DOI: 10.1038/s41586-024-07509-7 | PMCID: PMC11208145 | PMID: 38867041
- Evidence: We used samtools mpileup (parameters –q 30 –Q 30 –B) to generate a pileup file from the merged sequence data of each individual and used a custom script (pileupCaller v.8.2.2; ref.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [ADMIXTURE v1.3.0, SAMtools]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: 74 ) and converted to BAM files, sorted and indexed using SAMtools 75 .
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Senescent glia link mitochondrial dysfunction and lipid accumulation. (Nature 2024)

- DOI: 10.1038/s41586-024-07516-8 | PMCID: PMC11168935 | PMID: 38839958
- Evidence: Alignment sorted BAM files (samtools v.15) for each sample were merged across sequencing runs (picard) 64 .
- Full pipeline: alignment/mapping [DESeq2, HISAT2 v2.1.0, HTSeq v0.9.1, SAMtools] -> differential/statistical testing [DESeq2, HTSeq v0.9.1, edgeR, ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: For the analysis of mtDNA heteroplasmy, uniquely mapped reads were extracted from the BAM files using samtools and used to estimate mtDNA heteroplasmy with MitoHEAR (mitochondrial heteroplasmy analyzeR; https://github.com/ScialdoneLab/MitoHEAR ) 73 .
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **1.15.1**
- Evidence: The mapping.bam”files from two runs were sorted and merged using samtools (v.1.15.1) 85 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### The rise of baobab trees in Madagascar. (Nature 2024)

- DOI: 10.1038/s41586-024-07447-4 | PMCID: PMC11136661 | PMID: 38750363
- Version used: **1.9**
- Evidence: Samtools (v.1.9) 93 was then used to sort the aligned reads and Picard (v.2.21.6) 94 was used to remove redundant reads.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MrBayes v3.1.2, Picard v2.21.6, SAMtools v1.9] -> structure determination [R, ape (R) v5.6] -> stage not stated [AUGUSTUS v3.2.3, GATK v4.1.2.0, Pilon v1.23, RAxML, RepeatMasker v2.0]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: 42 ) v.2.22-r1101 (‘-ax map-hifi’ for long reads and ‘-ax sr --score-N 2’ for short reads) and the sam mapping files were converted into bam format using SAMtools 43 v.1.14 (‘samtools view’) and filtered to retain only reads that mapped with more than 98% identity (and more than 80% of the read length for short reads only) using CoverM v.0.6.1 ( https://github.com/wwood/CoverM ).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **1.9**
- Evidence: Alignment sam files were converted to bam files using samtools v.1.9 and bam files were converted to bed files using bedtools v.2.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Version used: **1.9**
- Evidence: DNA reads were mapped to the mouse GRCm39 genome assembly using BWA-MEM (v.0.7.17), filtered using samtools (v.1.9) and visualized using IGV (Integrative Genomics Viewer, Broad Institute, v.2.12.3).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Network of large pedigrees reveals social practices of Avar communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07312-4 | PMCID: PMC11078744 | PMID: 38658749
- Version used: **1.9**
- Evidence: The reads with phred mapping quality of less than 30 were then discarded using -q (q30-reads) in Samtools v1.9 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [BCFtools v1.3, Cytoscape v3.9.1, Picard, igraph]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **1.12**
- Evidence: Alignments were further processed by removing duplicates using picard MarkDuplicates SNAPSHOT v.2.21.4 ( http://broadinstitute.github.io/picard ), and samtools (v.1.12) 55 was used to filter reads and convert files into BAM format.
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Transient loss of Polycomb components induces an epigenetic cancer fate. (Nature 2024)

- DOI: 10.1038/s41586-024-07328-w | PMCID: PMC11096130 | PMID: 38658752
- Evidence: Then, sequencing reads were aligned to the dm6 version of the Drosophila genome using Burrows–Wheeler aligner with default parameters and duplicate reads were removed using samtools and PICARD ( http://picard.sourceforge.net ).
- Full pipeline: quality control [fastp] -> alignment/mapping [DESeq2, SAMtools, featureCounts] -> differential/statistical testing [DESeq2, featureCounts] -> stage not stated [GATK, Mutect2, R, data.table v1.14.2]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Version used: **1.13**
- Evidence: For coverage analysis on Tcf7 /TCF1 + and Tcf7 /TCF1 − clusters, BAM files were split by cell barcodes from clusters 1–2 or clusters 3–8 using samtools (v.1.13) 64 before coverage estimation.
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Evidence: BAM files were then sorted and indexed with Samtools (ref.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: SAMtools was used to identify uniquely aligned reads, and Picard was used to remove duplicate reads.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Version used: **1.4.1**
- Evidence: The resulting SAM files were converted to BAM files using Samtools (v1.4.1) using the view command, which were subsequently sorted and indexed, with potential PCR duplicates marked with Samtools markdup.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: We aligned the reads in the FASTQ files to the T2T-CHM13 reference genome 4 (v.2.0) using BWA 58 (v.0.7.17-r1188), sorted the alignments using SAMtools 59 (v.1.9) and marked duplicate reads using sambamba 60 (v.1.0).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### A brain-specific angiogenic mechanism enabled by tip cell specialization. (Nature 2024)

- DOI: 10.1038/s41586-024-07283-6 | PMCID: PMC11041701 | PMID: 38570687
- Version used: **1.16.1**
- Evidence: Adapter sequences were removed using Trim Galore v.0.4.4 before read mapping and doublets were removed using Samtools v.1.16.1 software.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore v0.4.4] -> alignment/mapping [Bowtie2, SAMtools v1.16.1, TopHat v2.1.1, Trim Galore v0.4.4, featureCounts] -> quantification [featureCounts] -> stage not stated [DESeq2 v1.12, ImageJ v1.53c, Seurat]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Evidence: Samtools 58 was then used to merge individual bam files (from each HiFi sequencing run) and exclude unmapped reads and supplementary alignments.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Evidence: Alignment quality was analysed using SAMtools flagstat with default parameters.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### Compensatory evolution in NusG improves fitness of drug-resistant M. tuberculosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07206-5 | PMCID: PMC10990936 | PMID: 38509362
- Version used: **1.7**
- Evidence: Single-nucleotide polymorphisms (SNPs) were called and annotated using the HaplotypeCaller tool Genome Analysis Toolkit (version 3.5) using inputs from samtools (version 1.7).
- Full pipeline: variant calling [GATK v3.5, SAMtools v1.7] -> quantification [ImageJ] -> differential/statistical testing [Stan] -> stage not stated [RAxML v8.2.11, freebayes v1.3.1]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Version used: **1.10**
- Evidence: For 22 G, only reads mapped to the coding sequences were analysed; for 21U, reads mapped to coding sequences, tRNAs and rRNAs were excluded using seqkit v0.13 and samtools v1.10.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.3.1**
- Evidence: Uniquely mapped reads were extracted with samtools (v.1.3.1) 102 view using the parameters -h -b -F 3844 -q 10.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **1.9**
- Evidence: Locus copy number estimation For copy number estimation in yeast strains, coverage depth was calculated from whole-genome sequencing data for the synthetic HPRT1 and HPRT1R loci as well as the entire yeast genome (excluding chrM) using samtools v1.9 depth 86 , and the calculated depth of the synthetic loci was divided by the genome average.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Version used: **1.15**
- Evidence: To estimate the VAF of KRAS G12D mutation and cell fraction of KRAS G12D -carrying cells within malignant and non-malignant epithelial cell subpopulations (for example, malignant cells from all LUADs, malignant cells from KM-LUADs, KACs from KM-LUADs), reads were first extracted based on their unique cell barcodes and BAM files were generated for each subpopulation using samtools (v.1.15).
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Version used: **1.17**
- Evidence: The inferred full-length reads were generated by Bedtools (v2.31.0) and Samtools (v1.17) after mapping to the reference genome ( NC_000913.3 for Eco, NC_008596.1 for Msm and NC_018143.2 for Mtb) with Bowtie 2 (v2.5.1).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **1.2**
- Evidence: The PCR duplicates were removed using Picard (v2.92) and SAMtools (v1.2) software 39 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **1.9**
- Evidence: The ‘alignmentSieve’ function of Deeptools (v.3.5.0) 58 and ‘sort’ and ‘index’ functions of Samtools (v.1.9) 59 were used to isolate fragments in nucleosome-free regions.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Bile salt hydrolase catalyses formation of amine-conjugated bile acids. (Nature 2024)

- DOI: 10.1038/s41586-023-06990-w | PMCID: PMC10881385 | PMID: 38326609
- Version used: **1.10**
- Evidence: Obtained alignments were sorted using samtools (v.1.10) (ref.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Trimmomatic, fastp v0.12.4] -> alignment/mapping [Bowtie2 v2.2.5, SAMtools v1.10, featureCounts v2.0.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [Prokka]

### Homo sapiens reached the higher latitudes of Europe by 45,000 years ago. (Nature 2024)

- DOI: 10.1038/s41586-023-06923-7 | PMCID: PMC10849966 | PMID: 38297117
- Evidence: Reads from the libraries generated from the same skeletal fragment were then merged using Samtools merge 71 .
- Full pipeline: alignment/mapping [BWA] -> registration [MAFFT v7.453] -> structure determination [MAFFT v7.453] -> stage not stated [BEAST v2.6.6, QGIS, R v4.1, SAMtools]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **1.7**
- Evidence: After generating a text pileup output for the BAM files with the mpileup tool from Samtools version 1.7 90 , SNPs were called using VarScan version 2.4.3 91 (using parameters: -p-value 0.01, -min-reads2 1, -min-coverage 1, -min-freq-for-hom, 0.4 -min-var-freq 0.05, -output-vcf 1).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Evidence: Sequence data were aligned to the E. atami genome assembly using BWA-mem (v.0.7.5a-r416) 108 with option -a and filtered by samtools view 108 with option -F2308.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Evidence: Mapped reads were filtered for mapping quality 30 and sorted using Picard (v.1.127) ( http://picard.sourceforge.net ) and SAMtools 78 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### 100 ancient genomes show repeated population turnovers in Neolithic Denmark. (Nature 2024)

- DOI: 10.1038/s41586-023-06862-3 | PMCID: PMC10781617 | PMID: 38200294
- Evidence: We utilized a new computational method optimized for low-coverage data 21 , to impute genotypes based on genotype likelihoods of ancient individuals with the samtools/bcftools pipeline, and using the 1000 Genomes phased data 78 as a reference panel.
- Full pipeline: quality control [ADMIXTURE] -> variant calling [ADMIXTURE, BCFtools, PLINK, R, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [PLINK, R]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Version used: **1.10**
- Evidence: Read depth and coverage were determined using samtools (v1.10) 55 with all sites used in the calculation (-a).
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Evidence: Duplicate reads were removed using samtools 45 , awk scripts and Picard tools (Broad Institute).
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### Emergence of replication timing during early mammalian development. (Nature 2024)

- DOI: 10.1038/s41586-023-06872-1 | PMCID: PMC10781638 | PMID: 38123678
- Version used: **1.9**
- Evidence: Duplicates were marked using SAMtools (v.1.9) ‘markdup’ as described by SAMtools 59 documentation (the commands ‘fixmate’ and ‘sort samtools’ were used for this purpose accordingly).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2 v2.3.5] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [BEDTools, ImageJ v1.53k, R v4.0.0, SAMtools v1.9]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: SAMtools was used to select uniquely aligning reads by removing reads with alignment quality alignments below 30 (-q 30).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Version used: **1.4**
- Evidence: Sam files were converted to bam and sorted using Samtools 1.4.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### GDF15 linked to maternal risk of nausea and vomiting during pregnancy. (Nature 2024)

- DOI: 10.1038/s41586-023-06921-9 | PMCID: PMC10808057 | PMID: 38092039
- Evidence: As homozygous reference alleles are not called by ‘HaplotypeCaller’, we used ‘mpileup’ command of samtools and bcftools to detect the read counts from the BAM files generated by the previous step.
- Full pipeline: alignment/mapping [GATK] -> variant calling [BCFtools, SAMtools] -> quantification [BCFtools, SAMtools, lme4] -> registration [Picard] -> stage not stated [PLINK v1.90b, R]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Version used: **1.16.1**
- Evidence: By using SAMtools (v.1.16.1; RRID: SCR_002105 ) 80 , reads were sorted and deduplicated and reads from the blacklisted regions ( https://www.encodeproject.org/files/ENCFF356LFX/ ) were cleaned.
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **1.11**
- Evidence: Post-filtering Binary Alignment Map files for all samples were merged using the merge function from Samtools (v.1.11), followed by peak calling using MACS2 (v.2.1.0) with parameters --nomodel, --nolambda, --keep-dup all and --slocal 10000, optimized for paired data (−f BAMPE) using the mouse genome (−g mm) 89 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **1.9**
- Evidence: Sequencing analysis and mutation calling were performed as described 45 , using the following tools: Python v.2.7.18, TrimGalore v.0.4.1, BWA v.0.7.13, Samtools v.1.9, Picard v.1.119, GenomeAnalysisTK v.3.5, Bcftools v.1.9, and tabix v.0.2.6.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Version used: **1.2**
- Evidence: These in silico rRNA-depleted reads were then remapped to the main reference, sorted with SAMtools (v.1.2) 61 and passed to Picard ( https://broadinstitute.github.io/picard/ , v.3.1.1) to mark duplicates.
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: Genome coverage in 100 bp increments was obtained using Samtools 69 (v.1.9) and Deeptools 70 (v.3.1.3) and the average modified z score, coverage fold increase and Cohen’s D of prophage regions was calculated as follows: 1 z -score ave = mean ( 0.6745 × ( x p − x ~ ) / median ⌈ x h − x ~ ⌉ ) where z -score ave is the average z score of the predicted region, x p is 100 bp coverage increments of the...
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Evidence: 71 ) with default parameters and samtools sort v.1.15.1 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Version used: **1.17**
- Evidence: The filtered reads were mapped to the mouse reference genome mm10 using HISAT2 (v.2.2.1) 76 , and samtools (v.1.17) 77 was used to convert and sort BAM files.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: PCR duplicates were removed from the analysis using Samtools 76 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Version used: **1.16.1**
- Evidence: 22 ) using SAMtools (v1.16.1) 49 with the command ‘samtools view -s 0.FRAC’ (FRAC is the sampling rate).
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Evidence: Analysis of combinatorial screens Combinatorial screening data were processed as follows: Raw reads were extracted from unaligned BAM files (samtools view with flag -f 64 for read 1 and -f 128 for read 2), joined by the read identifier (column1 or QNAME of the BAM), and CROP-seq-multi features (spacer1, iBAR1, spacer2 and iBAR2) were extracted based on their position.
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Version used: **1.17**
- Evidence: The alignments were then converted to sorted BAM files containing only primary mappings with samtools (v.1.17) 65 : # HiFi readspbmm2 align {genome}.mmi {bam_with_meth_calls} -j 42 > {output.bam}samtools view -@ 24 -Sb -F 2048 {output.bam} | samtools sort -@ 24 -T {temporary_directory} - > {output.bam}samtools index {output.bam}# ONT readswinnowmap -t 48 -W {genome}_repetitive_k15.txt -ax map-ont ...
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **1.16.1**
- Evidence: Only pairs mapping concordantly outside of mitochondria were kept (Samtools v.1.16.1) (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **1.3.1**
- Evidence: Analysis of piggyBac insertions Sequencing reads that contained internal transposon sequences were excluded, and the remaining reads were aligned against the GRCm38 reference using BWA v0.7.15 and samtools v1.3.1.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Fluctuating DNA methylation tracks cancer evolution at clinical scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09374-4 | PMCID: PMC12443617 | PMID: 40931062
- Evidence: In all samples, the generated unmapped BAM files after the basecalling were converted to FASTQ files using the SAMtools fastq -T Mm, Ml command.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [Bioconductor, R, SAMtools, Stan, dynesty, ggplot2 v3.5.2, survival (R) v0.4.9]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Version used: **1.14**
- Evidence: The FASTQ files were individually mapped against the human genome reference file including decoy sequences (GRCh38p7.13/hg38, 1000 Genome Project) using bowtie2 (-x 2000, -mm --qc-filter --met 1 --sensitive --no-mixed -t) and subsequently merged and sorted as BAM-formatted files using samtools v.1.14, with only uniquely high-quality mapped reads (MAPQ > 30, SAM flags 0×1, 0×2) retained.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **1.15.1**
- Evidence: Unmapped reads and secondary alignments were discarded using SAMtools (v.1.15.1) 66 with the view command and option -F 260.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Cas9 senses CRISPR RNA abundance to regulate CRISPR spacer acquisition. (Nature 2025)

- DOI: 10.1038/s41586-025-09577-9 | PMCID: PMC12477760 | PMID: 40902823
- Version used: **1.9**
- Evidence: Reads that mapped ambiguously were removed from further analysis using Samtools (v.1.9) 61 .
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v0.92] -> read trimming [Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9, minimap2] -> stage not stated [BEDTools]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Evidence: A pileup file was generated using samtools mpileup with parameters -q 30 -Q 30 -B containing only sites overlapping with our capture panel.
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **1.9**
- Evidence: Unmapped, unpaired and low-quality reads (MAPQ ≤ 5) were removed using samtools (v.1.9) view with settings -q 5 -f 2.
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Excised DNA circles from V(D)J recombination promote relapsed leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-09372-6 | PMCID: PMC12443594 | PMID: 40770098
- Evidence: Following alignment to the genome, the data were filtered for discordant reads at the immunoglobulin and TCR loci using Samtools.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [Python]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Version used: **1.16.1**
- Evidence: Cell-type specific scRNA-seq reads were identified by their 10x barcodes, parsed from the original post-alignment BAM files for each lemur and counted using Samtools (v.1.16.1) across the respective gene.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: Samtools 65 was used to sort the alignments and convert to CRAM.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Version used: **1.15.1**
- Evidence: The sequences of Alu elements, L1s and SVAs identified by RepeatMasker within the centromere HOR array boundaries were retrieved using SAMtools (v.1.15.1) 93 .
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Version used: **1.20**
- Evidence: The per-sample coverage depth across chromosome Z was calculated using SAMtools 1.20 (ref.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **1.16.1**
- Evidence: Aligned reads were converted to FASTQ format with SAMtools (version 1.16.1) 59 and assembled with Canu (version 2.1.1) 60 in the PacBio HiFi mode with expected genome sizes ranging from 120 kb to 400 kb in 10-kb increments.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### The spatiotemporal distribution of human pathogens in ancient Eurasia. (Nature 2025)

- DOI: 10.1038/s41586-025-09192-8 | PMCID: PMC12286840 | PMID: 40634616
- Evidence: Mapped BAM files were subjected to duplicate marking using ‘samtools markdup’ 63 , and filtered for mapping quality MAPQ ≥ 20.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [BLAST] -> stage not stated [R]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Version used: **1.9**
- Evidence: Reads were sorted and indexed using Samtools (v.1.9-4) 69 and only uniquely mapped reads were kept for further analysis.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### Nerve-to-cancer transfer of mitochondria during cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09176-8 | PMCID: PMC12328229 | PMID: 40562940
- Evidence: SAM and BAM files were processed with SAMtools and Sambamba, and alignment quality was assessed using SAMtools idxstats, retaining only reads aligning to mm39.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, Python, SAMtools] -> quantification [DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Python] -> stage not stated [GSEA]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: For this purpose, chromosomes of subgenomes S1_h1, S1_h2, S3, R3 and R4 were aligned against each other within each linkage group (Rca1–Rca7) by minimap2 76 , 77 using the following command: minimap2 -ax asm5 --eqx -t 16 genome1.fa genome2.fa | samtools sort -@8 > aln.sorted.bam.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Evidence: For UCSC genome browser visualization, reads were mapped to the mm10 mouse reference genome ( https://genome.ucsc.edu/cgi-bin/hgGateway?db=mm10 ) using hisat2 v.2.1.0 with the options ‘--no-softclip -k 100 | samtools view -q 10 -Sb - | samtools sort’.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Ancient DNA reveals a two-clanned matrilineal community in Neolithic China. (Nature 2025)

- DOI: 10.1038/s41586-025-09103-x | PMCID: PMC12310535 | PMID: 40468069
- Version used: **1.9**
- Evidence: The reads with phred mapping quality of less than 30 were then discarded using -q (q30-reads) in Samtools v1.9 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [R]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Evidence: We quantified allelic counts for filtered SNPs using samtools mpileup 55 (v1.10).
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: SAMtools 44 (v1.17) was used to sort and index alignments.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Mapping rates were calculated with samtools flagstat 65 .
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: HyPo arguments included approximate genome length of 35 megabases (-s 35m; based on a previous study 65 ) and the average read depth of each genome (-c) (calculated with Samtools depth 66 ).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Genomics reveals zoonotic and sustained human mpox spread in West Africa. (Nature 2025)

- DOI: 10.1038/s41586-025-09128-2 | PMCID: PMC12310364 | PMID: 40388983
- Evidence: In brief, we mapped reads against a clade IIb reference genome ( NC_063383 , an early hMPXV-1 genome from Nigeria) with bwa-mem 34 , and called consensus using samtools 35 and iVar 36 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> structure determination [IQ-TREE v2.0] -> stage not stated [Nextstrain]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Mapped files were converted to bam files and merged by sample using SAMtools 86 .
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: The SAM files generated were converted to BAM files using Samtools 52 (v.1.9).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Picuris Pueblo oral history and genomics reveal continuity in US Southwest. (Nature 2025)

- DOI: 10.1038/s41586-025-08791-9 | PMCID: PMC12137115 | PMID: 40307544
- Version used: **1.3.1**
- Evidence: Mitochondrial DNA analysis Consensus sequences were obtained using samtools v.1.3.1 mpileup 105 ), requiring a minimum of five reads and more than 70% frequency in a locus to call a base.
- Full pipeline: quality control [ANGSD v0.931] -> variant calling [BCFtools v1.17] -> stage not stated [ADMIXTURE, BEAST v2.6, Picard v2.25.0, SAMtools v1.3.1]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Evidence: Unmapped, non-unique and duplicated reads were filtered out using SAMtools 64 , 65 (v.1.9) and Picard (v.2.20.3-SNAPSHOT) before variants were called by a standard pipeline of Genome Analysis Toolkit (GATK 65 v.4.1.2) and Sentieon 66 (v.202112.01).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Aligned reads were sorted by genomic position using SAMtools 67 (v.1.10) and duplicate reads were marked using sambamba 68 (v.1.0).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### Punic people were genetically diverse with almost no Levantine ancestors. (Nature 2025)

- DOI: 10.1038/s41586-025-08913-3 | PMCID: PMC12226237 | PMID: 40269169
- Evidence: We built a mitochondrial DNA consensus sequence using bcftools ( https://github.com/samtools/bcftools ) and SAMTools 49 , only analyzing sites with a minimum of two-fold coverage and determining allelic status by majority rule.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK, R, SAMtools]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **1.9**
- Evidence: Alignments were sorted and filtered for mapping quality >= 20 using samtools 1.9 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **1.15.1**
- Evidence: Reads were then mapped against mm10 with Bowtie2 (2.4.4), and duplicate reads were removed with samtools (1.15.1) rmdup, and bam files were converted to bed files with bedtools (2.30.0) bamtobed.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### The phased pan-genome of tetraploid European potato. (Nature 2025)

- DOI: 10.1038/s41586-025-08843-0 | PMCID: PMC12158759 | PMID: 40240601
- Evidence: The contigs were classified on the basis of sequencing coverage (using samtools 53 depth function (v.1.9)): according to the average sequencing depth per haplotype d , contigs with [0, 1.5 d ], [1.5 d + 1, 2.5 d ], [2.5 d + 1, 3.5 d ], [3.5 d , 4.5 d ] and [4.5 d + 1, infinite] were determined as haplotig, diplotig, triplotig, tetraplotig and replotig (Supplementary Fig.
- Full pipeline: alignment/mapping [minimap2 v2.20] -> variant calling [DeepVariant v1.4.0, SAMtools, minimap2 v2.20] -> dimensionality reduction/clustering [OrthoFinder v2.5.5] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v5.2.2, IQ-TREE v2.1.2, R v4.3, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: These alignments were then converted into bed or bam format by SAMtools 69 (v.1.20), and processed with YaHS 70 (v.1.1).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Histone H1 deamidation facilitates chromatin relaxation for DNA repair. (Nature 2025)

- DOI: 10.1038/s41586-025-08835-0 | PMCID: PMC12074999 | PMID: 40240600
- Evidence: Samtools was used to convert SAM files to BAM format, applying a filter criterion of a minimum mapping quality score of 10.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.4, SAMtools] -> stage not stated [AlphaFold, ImageJ, Picard, PyMOL, deepTools v3.5.5]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Version used: **1.9**
- Evidence: 80 (q-bio.GN)) under default parameters, and duplicated reads were flagged using Samtools v.1.9 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Version used: **1.9**
- Evidence: Determining poly(A) lengths from DRS Basecalled nanopore reads were mapped to the respective transcriptome references (Gencode 26 or Gencode 38 for mouse and human samples, respectively) using Minimap2 2.17 with options -k 14 -ax map-ont –secondary=no, and processed with Samtools 1.9 to filter out supplementary alignments and read mapping to reverse strand (Samtools view -b -F 2320).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens. (Nature 2025)

- DOI: 10.1038/s41586-025-08982-4 | PMCID: PMC12176658 | PMID: 40228524
- Version used: **0.1.19**
- Evidence: Sequences were mapped to the mouse genome (mm10) with bowtie2 (2.2.3), filtered based on mapping score (MAPQ > 30, Samtools (0.1.19)), and duplicates were removed (Picard).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.3, Picard, SAMtools v0.1.19] -> normalisation [Seurat v5.1] -> dimensionality reduction/clustering [Seurat v5.1, UMAP] -> stage not stated [Signac v1.14]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Version used: **1.6**
- Evidence: The resulting BAM files were sorted and indexed with Samtools v.1.6.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Evidence: Code availability Analyses were conducted using publicly available software: BCFtools v.1.13 ( https://samtools.github.io/bcftools/bcftools.html ), CrossMap v.0.5.4 ( https://crossmap.readthedocs.io/en/latest/ ), EasyQC v.23.8, 5 June 2020 ( https://www.uni-regensburg.de/medizin/epidemiologie-praeventivmedizin/genetische-epidemiologie/softwssare ), GWAMA v.2.2.2 ( https://genomics.ut.ee/en/tools )...
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **1.17**
- Evidence: Per-gene counts were generated by aligning reads using bowtie2 against the gene catalogue and generating a per-sample count with SAMtools v.1.17.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Ancient DNA from the Green Sahara reveals ancestral North African lineage. (Nature 2025)

- DOI: 10.1038/s41586-025-08793-7 | PMCID: PMC12043513 | PMID: 40175549
- Version used: **1.3**
- Evidence: Double-stranded 1240k-captured sequences from TKH009 and single-stranded Twist-captured sequences from TKH001 were genotyped using Samtools v.1.3 and pileupCaller from SequenceTools v.1.4.0.2 ( https://github.com/stschiff/sequenceTools ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, MAFFT] -> variant calling [SAMtools v1.3] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> stage not stated [PLINK, tidyverse v1.3.0]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Evidence: Duplicated reads were flagged using Picard (v.2.9.4) and only unique, properly paired reads were retained using SAMtools (with the parameters ‘-q 1 -F 1804’; v.1.9).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: In the first step the pipeline uses samtools 51 (v.1.17) to convert a BAM file to a SAM file.
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **1.9**
- Evidence: Mapped reads with MAPQ vales less than 30 were considered as multi-mapped reads and filtered out using Samtools (v.1.9).
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: Afterwards, samtools 76 was used to remove reads mapped to chrM or contigs.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### In vitro reconstitution of meiotic DNA double-strand-break formation. (Nature 2025)

- DOI: 10.1038/s41586-024-08551-1 | PMCID: PMC11922769 | PMID: 39972125
- Version used: **1.9**
- Evidence: The ‘view’ and ‘sort’ functions in SAMtools (v.1.9) were used to convert and sort the mapping output, generating sorted BAM files 41 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> quantification [ImageJ] -> dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.25.0]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Version used: **1.12**
- Evidence: Preprocessing and mapping quality control was done using FastQC (v.0.11.8) 67 , qualimap (v.2.2.2d) 68 , samtools (v.1.12) 69 and multiqc (v.1.9) 70 .
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: 61 ) v.2.4.5 and calculating bin TPMs (SAMtools 62 v.1.15.1).
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Evidence: We used SAMtools 82 and BGT 83 to extract the allele counts of the relevant variants from those datasets.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### A genomic history of the North Pontic Region from the Neolithic to the Bronze Age. (Nature 2025)

- DOI: 10.1038/s41586-024-08372-2 | PMCID: PMC11909631 | PMID: 39910299
- Evidence: We determined a consensus sequence for mitochondrial DNA using bcftools ( https://github.com/samtools/bcftools ) and SAMtools 59 requiring a minimum of 2-fold coverage to call the nucleotide and a majority rule to determine its value.
- Full pipeline: quality control [ANGSD] -> stage not stated [ADMIXTURE, BCFtools, SAMtools]

### The genetic origin of the Indo-Europeans. (Nature 2025)

- DOI: 10.1038/s41586-024-08531-5 | PMCID: PMC11922553 | PMID: 39910300
- Evidence: We determined a consensus for mitochondrial DNA using bcftools ( https://github.com/samtools/bcftools ) and SAMTools 85 , requiring a minimum of 2-fold coverage to call the nucleotide and a majority rule to determine its value.
- Full pipeline: quality control [ANGSD] -> stage not stated [BCFtools, SAMtools]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **1.17**
- Evidence: HiFi reads for 10 accessions were generated using the ccs program version 6.4.0 ( https://github.com/PacificBiosciences/ccs ) and subreads obtained from the Pacific Biosciences Sequel II platform, which were then converted to FASTQ format by SAMtools (v.1.17) 62 .
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### A map of the rubisco biochemical landscape. (Nature 2025)

- DOI: 10.1038/s41586-024-08455-0 | PMCID: PMC11839469 | PMID: 39843747
- Evidence: All reads of a given barcode were aligned and a consensus sequence was obtained using SAMtools 33 .
- Full pipeline: alignment/mapping [SAMtools]

### Ancient DNA reveals reproductive barrier despite shared Avar-period culture. (Nature 2025)

- DOI: 10.1038/s41586-024-08418-5 | PMCID: PMC11864967 | PMID: 39814885
- Evidence: We made random pseudo-haploid calls on 1,240,000 sites using pileupCaller ( https://github.com/stschiff/sequenceTools ), based on trimmed BAM files after quality filtering using samtools 60 with flags -q30 -Q30.
- Full pipeline: quality control [ANGSD v0.910] -> read trimming [SAMtools] -> stage not stated [Picard]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Reads were sorted with SAMtools 68 , polymerase chain reaction duplicates were removed with Picard Tools v.2.0.1 and indels were locally realigned using GATK software (v.3.7.0) 69 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **1.9**
- Evidence: Low-quality reads were filtered out using Samtools (v.1.9) with a cut-off MAPQ score of 30, and only unique reads were retained for further processing 67 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: Sorting and indexing of the bam files was done with SAMtools 45 (v.1.14).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **1.9**
- Evidence: Those reads were then mapped to Col-CEN_v1.2 reference genome using Bowtie2 with the parameter ‘--local --very-sensitive’, and the mapped data was converted to BAM files using SAMtools (v.1.9) to generate ‘clip_disc-local.sorted.bam’ files.
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Aligned reads were sorted and subsequently converted to BAM format using the samtools suite 68 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Evidence: ... including AdapterRemoval v2 71 for removal of adapters and trimming of low-confidence base calls at the 3′ end of reads, bwa v0.7.17 72 for mapping, samtools c1.12 73 for the removal of reads with low mapping quality (<37), dedup v0.21.8 for removal of duplicates, and DamageProfiler 74 for analysing damage percentages in reads, among others.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Evidence: We filtered each library accordingly for minimum length, and mapping quality of 25, using SAMtools 56 (v.1.3.1).
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: Bam files were generated with SAMtools 69 , 70 (v1.9) view -bS -F 0 × 04 and bam-to-bed conversion performed with bedtools (v2.30.0) bamtobed -bedpe.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### A functional microbiome catalogue crowdsourced from North American rivers. (Nature 2025)

- DOI: 10.1038/s41586-024-08240-z | PMCID: PMC11666465 | PMID: 39567690
- Evidence: To quantify MAG relative abundance across samples, trimmed metagenomic reads were mapped to the dereplicated MAG set using Bowtie2 84 and output as SAM files, which were then converted to sorted BAM files using samtools.
- Full pipeline: read trimming [Bowtie2, SAMtools, edgeR] -> alignment/mapping [Bowtie2, MUSCLE v3.8.31, Python, RAxML, SAMtools] -> quantification [Bowtie2, SAMtools] -> visualisation [R v4.2.1, ggplot2 v3.3.6, pheatmap v1.0.12, tidyverse v1.2.0, vegan v2.6]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Version used: **1.21**
- Evidence: Aligned reads were converted to BAM files, merged across libraries at sample level, sorted, filtered and indexed using Samtools (v.1.21) 75 , then duplicates identified using MarkDuplicates from Picard (v2.18.7), with the following options in place: ‘OPTICAL_DUPLICATE_PIXEL_DISTANCE = 12000 REMOVE_DUPLICATES = false TAGGING_POLICY = All VALIDATION_STRINGENCY = LENIENT’.
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **1.9**
- Evidence: Low-quality reads were filtered using Samtools (v1.9) with a MAPQ cut-off score of 30 98 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Evidence: Aligned read pairs were randomly downsampled using samtools 115 (v.1.18) at predefined fractions to achieve target sequencing depths of 20×, 15×, 10× and 5× for each sample.
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Version used: **1.3.1**
- Evidence: The Hisat2 output files (SAM) were converted to the BAM format and were sorted and indexed using SAMtools (v.1.3.1).
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Version used: **1.9**
- Evidence: Quality control of FASTQ and BAM files was performed with FASTQC (v0.11.7) and samtools (v1.9) respectively 52 .
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Telomere-to-telomere assembly using HERRO-corrected Nanopore Simplex reads. (Nature 2026)

- DOI: 10.1038/s41586-026-10563-y | PMCID: PMC13323052 | PMID: 42045451
- Evidence: We first aligned assembly sequences to the reference sequences using minigraph and indexed the reference with Samtools 56 1.19.2 (Using htslib 57 1.19.1).
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BEDTools, BUSCO, Canu, Flye, QUAST]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Per base read depth was then counted for each position with samtools 84 (v.1.21) using the command: samtools depth -a -Q 10 -b t4.bed {sample}_sorted.bam > {sample}.coverage.txt.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Dynamics of genetic and somatic trade-offs in ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10407-9 | PMCID: PMC13253337 | PMID: 42020758
- Version used: **1.6**
- Evidence: BAM files were sorted and indexed using samtools (v1.6) 82 , and read group information was added using picard tools (v2.14.1).
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.3.4.1] -> variant calling [BCFtools, R v4.0] -> dimensionality reduction/clustering [PLINK, TwoSampleMR v0.6.2, clusterProfiler] -> stage not stated [SAMtools v1.6]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **1.13**
- Evidence: Reads with a mapping score of 30 or higher were selected using SAMtools (v.1.13).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **1.10**
- Evidence: The alignment results in SAM format were converted to the BAM format using the SortSam tool from the Picard suite (v.2.14.0-SNAPSHOT), and samtools (v.1.10) for indexing.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Polyclonal selection of immune checkpoint mutations in thyroid autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10493-9 | PMCID: PMC13233322 | PMID: 41981327
- Evidence: For the latter, BAM files were pre-filtered using SAMtools 66 (v.1.13) to retain only those reads mapping to the human immunoglobulin and T cell receptor genes.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [R, Seurat, ggpubr, tidyverse]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Version used: **1.10**
- Evidence: The ‘rmdup’ module of SAMtools (v.1.10) 80 was used to remove duplicated read pairs.
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### The DNA virome varies with human genes and environments. (Nature 2026)

- DOI: 10.1038/s41586-026-10288-y | PMCID: PMC13215884 | PMID: 41882355
- Evidence: Read alignments were filtered to those for which both the read and its mate were mapped (samtools view -F 12) and were then collated within 500 bp bins of each of the two reference genomes using mosdepth with the same parameters as above, with the exception that the filter on insert size (-l 100 -u 1000) was dropped, as insert size was undefined in situations in which a read mapped to EBV type 1 a...
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [DeepVariant] -> differential/statistical testing [LDSC] -> stage not stated [R]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Version used: **1.16**
- Evidence: Duplicates were removed, and unique reads with mapping quality > 20 were selected using SAMtools v.1.16 (RRID: SCR_003030 ; https://github.com/samtools/samtools ).
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **1.9**
- Evidence: Aligned reads were filtered using samtools v.1.9 to keep alignments that have a minimum mapping quality of 30.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Version used: **1.17**
- Evidence: Subsequent SAM files were converted to BAM files, and PCR duplicate reads were filtered out using SAMtools (v1.17) 55 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **1.7**
- Evidence: Multisample SNP calling was done using SAMtools (v.1.7) mpileup 86 and Varscan (v.2.4.089) 87 with a minimum coverage of eight and a minimum alternate allele count of four.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **1.9**
- Evidence: Uniquely mapped reads with map quality greater than 30 were used for the following analyses, using Samtools (v.1.9).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Evidence: Various bam file processing operations were performed using Samtools/htslib/bcftools (v1.11).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### Precancerous niche remodelling dictates nascent tumour persistence. (Nature 2026)

- DOI: 10.1038/s41586-026-10157-8 | PMCID: PMC13148994 | PMID: 41781610
- Evidence: Duplicate reads were marked using SAMtools 70 (v.1.11).
- Full pipeline: variant calling [R] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [SAMtools, scDblFinder]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **1.19.2**
- Evidence: Aligned sorted bam files were generated using SAMtools v.1.19.2 and visualized using Integrative Genomics Viewer v.2.17.4.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: For sex analysis, the number of uniquely mapped reads was calculated for each chromosome using samtools coverage (v.1.17).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Version used: **1.18**
- Evidence: The mapped reads were converted to BAM format and sorted using Samtools (v.1.18) 78 .
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Version used: **1.20**
- Evidence: Reads mapping to the EBV genome ( NC_007605.1 ) were accessed in CRAM files (field 24048), which had been previously generated by aligning fastq data to a GRCh38 graph genome (including the contig chrEBV) and were extracted using samtools (v1.20).
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: Reads were filtered to include only those with barcodes assigned to a cell type in the short-read data using samtools view (v.1.18) with parameters -h -D CB.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **1.9**
- Evidence: For the mononucleosome analysis, we filtered reads with estimated insert sizes in the 120–180 bp range using SAMtools (v.1.9).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Version used: **1.9**
- Evidence: Sequencing quality filters were performed using Samtools v.1.9 stats 51 and fastqc v.0.11.3 (ref.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Version used: **0.1.19**
- Evidence: The resulting alignment files were converted to BAM format using SAMtools (v.0.1.19) 33 .
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Lasting Lower Rhine-Meuse forager ancestry shaped Bell Beaker expansion. (Nature 2026)

- DOI: 10.1038/s41586-026-10111-8 | PMCID: PMC12978843 | PMID: 41673154
- Evidence: Haplogroup assignment of uniparentally inherited markers: We created consensus mitochondrial haplotypes with samtools and bcftools.
- Full pipeline: quality control [ANGSD] -> variant calling [BCFtools, SAMtools]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Version used: **1.7**
- Evidence: Sam files generated from bowtie2 mapping were converted to bam files using samtools (v1.7) 52 , and then converted to numpy arrays using the genomearray3 Python library 30 .
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### Cleavage of mRNAs by a minority of pachytene piRNAs improves sperm fitness. (Nature 2026)

- DOI: 10.1038/s41586-026-10102-9 | PMCID: PMC13061629 | PMID: 41639461
- Version used: **1.0.0**
- Evidence: Unaligned reads were mapped to mouse genome mm10 using STAR (v.2.3.1) 63 , alignments with soft clipping of ends were removed with SAMtools (v.1.0.0) 66 , and reads with the same 5′ end were merged to represent a single 5′-monophosphorylated RNA species.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.18.1]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: After alignment, the reads were filtered using MarkDuplicates from Picard and then by a quality score of >20 using SAMtools 69 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **1.17**
- Evidence: Data were analysed using the nf-core/cutandrun pipeline v.3.2.2 with Nextflow v.24.04.2, using the default parameters and following software dependencies: bedtools (v.2.30.0), bowtie (v.2.4.4), deeptools (v.3.5.1), fastqc (v.0.12.1), picard (v.3.1.0), Python (v.3.9.12), samtools (v.1.17), Genrich (v.0.6.1), TrimGalore (v.0.6.6), ucsc (v.377).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Version used: **1.15.1**
- Evidence: Unmapped reads were converted to compressed FASTQ with samtools (v.1.15.1) and then used as input for microbiome profiling using MetaPhlAn (v.4.0.6) with the vOct22 reference database.
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Sequencing depth was calculated using Samtools depth command (v.1.9) 120 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Version used: **1.1**
- Evidence: 49 ); and tabulation of 5′ read endpoints using samtools v.1.1 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: WGS data and cohort analyses in the UKB For the UKB, we obtained per-base abundance of EBV DNA of the 490,560 WGS libraries by extracting reads aligning to chrEBV in the hg38 human genome reference that had a read mapping quality (MAPQ) ≥ 30 (q30) via the SAMtools view command 61 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **1.13**
- Evidence: The resulting processed bam files were split into forward and reverse strands according to SAM flags (SAMtools, v.1.13).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Version used: **1.10**
- Evidence: Samples were demultiplexed, quality checked, filtered and aligned with genome build GRCm38 using pre-established pipelines implemented in snakePipes 64 with STARsolo v.2.7.4a 65 , deeptools v.3.3.2, seqtk v.1.3, pigz v.2.3.4, snpsplit v.0.3.4, samtools v.1.10, fastqc v.0.11.9, cutadapt v.2.8, trim-galore v.0.6.5, multiqc v.1.8, fastp v.0.20.0, umi_tools v.1.0.1 and star v.2.7.4a.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **1.19**
- Evidence: Then, SAMtools (v1.19) and bedtools (v2.30) were used to compute the breadth of coverage of each genome.
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Version used: **1.9**
- Evidence: 71 ) algorithm (v2.4.1), filtered with samtools (v1.9) 72 (flags -f 2 -q 42), and overlapping paired ends were merged into a single sequence with PANDAseq (v2.11) 73 .
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Version used: **1.11**
- Evidence: Duplicate reads were removed using SAMtools (v.1.11) with fixmate -m and markdup -r settings.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Mutations were called from the duplicate-marked BAM files using samtools ‘mpileup’ and subsequently processed with bcftools 64 to generate a single VCF file 65 containing mutations identified in the WT and mutant genomes.
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Version used: **1.9**
- Evidence: The resulting SAM files were converted to BAM files, sorted and indexed using SAMtools (v.1.9) 72 .
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Picard’s MarkDuplicates ( https://broadinstitute.github.io/picard/ ), SAMtools 77 and BAMTools 78 were used postalignment for filtering and removal of unmapped, multimapped, PCR duplicate and mismatched reads.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: Chromatin dataset processing CUT&Run datasets were processed by trimming adaptors using cutadapt, locally mapping the reads using bowtie2, filtering for quality, removing duplicates and ENCODE blacklisted regions (ENCFF419RSJ) using samtools, and computing the coverage using deeptools.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **1.3.1**
- Evidence: Reads were aligned to the C. elegans genome (WBcel235/ce11) using BWA-MEM (v.0.7.17-r1188), and variants were identified using Samtools (v.1.3.1) and bcftools (v.1.13).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Somatic evolution following cancer treatment in normal tissue. (Nature 2026)

- DOI: 10.1038/s41586-025-09792-4 | PMCID: PMC13190248 | PMID: 41372419
- Version used: **1.19.2**
- Evidence: The bams were reformatted and template-coordinate sorted using ZipperBam and samtools (v.1.19.2) respectively.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> differential/statistical testing [R, lme4] -> stage not stated [Nextflow, SAMtools v1.19.2]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: The command line tool in Python implementation was adapted to be able to work with BAM files generated by BD Rhapsody, using samtools 64 to format the files, mainly by removing all possible alignments with antibodies and renaming the UMI barcode tag to ‘UB’ instead of ‘MA’.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Homo sapiens-specific evolution unveiled by ancient southern African genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09811-4 | PMCID: PMC12872451 | PMID: 41339558
- Evidence: BAM files from resequenced libraries were merged using Samtools merge (v.0.1.19) 64 before PCR duplicates were identified and collapsed using a slightly modified version of FilterUniqeSAMCons.py 60 .
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK v1.9, SAMtools, SnpEff]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: 128 ) v.2.24 with the -ax sr option and SAMtools 129 v.1.16.1 with samtools view -Sb -F 2308 - | samtools sort options.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.17**
- Evidence: In brief, the raw sequencing reads were converted to fastq format with samtools (v.1.17).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **1.21**
- Evidence: To determine the short-read coverage of integrated phages, we mapped the short reads to the long-read assembly using Bowtie 2 (v.2.5.4) and calculated the per-base coverage using SAMtools (v.1.21).
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Evidence: Fastq files were generated using samtools bam2fq (v.1.6) 70 , aligned to a custom reference (hg19_pUC19) comprising the pUC19 sequence appended to the hg19 genome using minimap2 (v.2.17) 71 and sorted and indexed using samtools.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Evidence: Aligned reads were sorted and indexed using samtools 57 and deduplicated using umi_tools dedup.
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Version used: **1.9**
- Evidence: The resulting BAM files were sorted and indexed with samtools (v1.9) and deduplicated using UMI-tools with the directional method.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: Alignment records were converted to binary Sequence Alignment/Map format using SAMtools 52 and sorted with Novosort ( http://www.novocraft.com/products/novosort/ ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Version used: **1.3.1**
- Evidence: Variants were first called across all samples independently using both HaplotypeCaller in GATK and mpileup in Samtools version 1.3.1 ( 63 ).
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### An ancient antimicrobial protein co-opted by a fungal plant pathogen for in planta mycobiome manipulation. (PNAS 2021)

- DOI: 10.1073/pnas.2110968118 | PMCID: PMC8670511 | PMID: 34853168
- Evidence: Next, the mapping files were converted to bam format using SAMtools ( 65 ) version 1.10, and the number of reads mapped to the contigs of a single genus were converted to “reads per million” for the individual samples.
- Full pipeline: alignment/mapping [HMMER, SAMtools] -> quantification [ImageJ, R v3.6.1, phyloseq] -> differential/statistical testing [DESeq2] -> visualisation [HMMER]

### Quantitative assessment reveals the dominance of duplicated sequences in germline-derived extrachromosomal circular DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2102842118 | PMCID: PMC8617514 | PMID: 34789574
- Evidence: For paired-read analysis, the orientation of read pairs was determined using the samtools stats function (v1.9).
- Full pipeline: read trimming [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> alignment/mapping [Bowtie2 v2.3.5, Trim Galore v0.6.1] -> stage not stated [RepeatMasker, SAMtools]

### Adaptive divergence in shoot gravitropism creates hybrid sterility in an Australian wildflower. (PNAS 2021)

- DOI: 10.1073/pnas.2004901118 | PMCID: PMC8617494 | PMID: 34789571
- Version used: **0.1.16**
- Evidence: We then used SAMtools 0.1.16 ( 75 ) to create an mpileup file of all samples with a minimum Phred quality score of 10, minimum sequencing depth per sample of 6×, and a minimum percent of population genotyped of 75%.
- Full pipeline: alignment/mapping [BLAST] -> variant calling [SAMtools v0.1.16] -> stage not stated [BUSCO, ImageJ, R]

### Linked supergenes underlie split sex ratio and social organization in an ant. (PNAS 2021)

- DOI: 10.1073/pnas.2101427118 | PMCID: PMC8609651 | PMID: 34772805
- Version used: **1.8**
- Evidence: We merged overlapping paired-end reads with PEAR version 0.9.10 ( 69 ), aligned the reads to the F. selysi reference genome ( 29 ) using BWA-MEM version 0.7.17 ( 70 ), and removed PCR duplicates with Samtools version 1.8 ( 71 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.8] -> variant calling [VCFtools v0.1.13] -> visualisation [R] -> stage not stated [GEMMA v0.94]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: Alignment files were converted to BAM files using SAMtools software ( 82 ).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Trained innate immunity, long-lasting epigenetic modulation, and skewed myelopoiesis by heme. (PNAS 2021)

- DOI: 10.1073/pnas.2102698118 | PMCID: PMC8545490 | PMID: 34663697
- Evidence: Duplicate and low-quality reads were removed after alignment using Samtools and Bamtools.
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [R] -> dimensionality reduction/clustering [ArchR v0.9.5, UMAP] -> differential/statistical testing [R] -> visualisation [ArchR v0.9.5] -> stage not stated [HOMER, MACS2, Seurat]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Version used: **0.1.19**
- Evidence: SAM files were converted to the BAM format using SAMtools (v0.1.19) ( 58 ).
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Version used: **1.9**
- Evidence: Subsequently, the filtered reads were mapped against the CO92 assembly with BWA mem model (v0.7.17) ( 37 ), and the aligned reads were extracted from bam files using SAMtools (v1.9) ( 38 ) view command (-bF 4); then, different runs of the same sample were merged using SAMtools merge command.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Evidence: Reads without a mapping mate were deleted using samtools view ( 87 ) and reads sorted by coordinate using GATK v4.0.3.0 SortSam ( 88 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Version used: **1.10**
- Evidence: PCR duplicates and reads mapping to the organellar genomes were removed with samtools v1.10 ( 76 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Cell-free reconstitution reveals the molecular mechanisms for the initiation of secondary siRNA biogenesis in plants. (PNAS 2021)

- DOI: 10.1073/pnas.2102889118 | PMCID: PMC8346886 | PMID: 34330830
- Evidence: Sequence Alignment Map (SAM) files were converted to BAM files using SAMtools ( 60 ) and then to BED files with BEDTools ( 61 ).
- Full pipeline: alignment/mapping [BEDTools, Cutadapt, SAMtools, ggplot2]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Version used: **1.3**
- Evidence: Morex reference genome ( 26 ) with BWA v.7.12 ( 54 ) and variants in the genomic space were called with SAMtools v.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Evidence: The 10,280 million trimmed reads generated from sequencing of 10,262 samples (germplasm collection plus CM334 control accessions) ( SI Appendix , Table S8 ) were then aligned to reference genome sequence C. annuum CM334 version 1.6 available at http://peppergenome.snu.ac.kr ( 39 ) using BWA-MEM version 0.7 ( 40 ) and converted to binary alignment map format using SAMtools ( 41 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: Average fragment length of reads mapping to microbial species was calculated with samtools stats.
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Accelerated expansion of pathogenic mitochondrial DNA heteroplasmies in Huntington's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2014610118 | PMCID: PMC8325154 | PMID: 34301881
- Version used: **1.6**
- Evidence: Reads mapped to target regions were locally realigned by using freebayes (version 1.1.0) ( 72 ), and their base qualities were recalibrated by using samtools (version 1.6) ( 73 ).
- Full pipeline: alignment/mapping [SAMtools v1.6, freebayes v1.1.0] -> registration [SAMtools v1.6, freebayes v1.1.0] -> differential/statistical testing [R v3.5.0, lme4 v1.1] -> stage not stated [ANNOVAR, Picard]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: Bowtie2 ( 100 ) was used to align reads to the database, and samtools ( 101 ) idxstats was used to calculate read coverage and RPKM for each contig.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### Molecular design of the γδT cell receptor ectodomain encodes biologically fit ligand recognition in the absence of mechanosensing. (PNAS 2021)

- DOI: 10.1073/pnas.2023050118 | PMCID: PMC8256041 | PMID: 34172580
- Evidence: The output fastq files were aligned against the Ensembl GRCm38.75 reference genome using STAR aligner (v2.5) ( 86 ) and the resultant binary alignment map (BAM)-format files were filtered to retain only primary-aligned reads (samtools view -F 0 × 0100).
- Full pipeline: alignment/mapping [SAMtools, STAR] -> quantification [DESeq2 v1.6.3, featureCounts v1.4.4] -> differential/statistical testing [DESeq2 v1.6.3, featureCounts v1.4.4]

### Evolutionary and phylogenetic insights from a nuclear genome sequence of the extinct, giant, "subfossil" koala lemur <i>Megaladapis edwardsi</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2022117118 | PMCID: PMC8255780 | PMID: 34162703
- Evidence: The resulting SAM (Sequence Alignment Map) files were converted to BAM (Binary Alignment Map) format using SAMtools ( 97 ) and then used to generate exon consensus sequences using SAMtools mpileup (default settings).
- Full pipeline: alignment/mapping [RAxML, SAMtools]

### Epigenetic inheritance of DNA methylation changes in fish living in hydrogen sulfide-rich springs. (PNAS 2021)

- DOI: 10.1073/pnas.2014929118 | PMCID: PMC8255783 | PMID: 34185679
- Evidence: The mapped read files were then converted to sorted BAM (Binary Sequence Alignment/Map) files using SAMtools ( 70 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools] -> differential/statistical testing [R, edgeR]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Version used: **1.8**
- Evidence: BAM files were used for calling SNPs with the bcftools option call -v -m from SAMtools (1.8) ( 66 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: We extracted viral reads from the generated BAM file by samtools ( 71 ) (version 1.11) using command: samtools view -b Aligned.sortedByCoord.out.bam NC_045512v2 > NC_Aligned.sortedByCoord.out.bam.
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### Host barriers to SARS-CoV-2 demonstrated by ferrets in a high-exposure domestic setting. (PNAS 2021)

- DOI: 10.1073/pnas.2025601118 | PMCID: PMC8106344 | PMID: 33858941
- Evidence: Consensus was called using SAMtools, and replicate Illumina/Minion libraries were compared to confirm consistency ( 48 ).
- Full pipeline: stage not stated [RAxML, SAMtools]

### Predicting transcriptional responses to cold stress across plant species. (PNAS 2021)

- DOI: 10.1073/pnas.2026330118 | PMCID: PMC7958178 | PMID: 33658387
- Version used: **1.9**
- Evidence: Samtools (v1.9) ( 44 ) was used to convert the raw Sequence Alignment Map (SAM) output from GSNAP to sorted Binary Alignment Map (BAM) files.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [HTSeq v0.6.1, MAFFT v7.149, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [BEAST v5.1, DESeq2] -> simulation/modelling [BEAST v5.1] -> stage not stated [R]

### DNA methylation-linked chromatin accessibility affects genomic architecture in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2023347118 | PMCID: PMC7865151 | PMID: 33495321
- Evidence: Duplicated reads were deduplicated with SAMtools rmdup (version 1.9).
- Full pipeline: read trimming [Cutadapt v2.5, SAMtools] -> alignment/mapping [Bowtie2, Cutadapt v2.5, RSEM] -> quantification [Bowtie2, RSEM] -> differential/statistical testing [R v3.30.0, edgeR v3.30.0] -> visualisation [pheatmap] -> stage not stated [BEDTools v2.26.0]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: For each low-coverage fecal-derived genome, we located the position of the tuning site in the bam file using SAMtools tview and manually called the variant when possible.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Prediction of Alzheimer's disease-specific phospholipase c gamma-1 SNV by deep learning-based approach for high-throughput screening. (PNAS 2021)

- DOI: 10.1073/pnas.2011250118 | PMCID: PMC7826347 | PMID: 33397809
- Evidence: Mapping was performed with reference genes and each of bam files was indexed with SAMtools.
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [ANNOVAR, BCFtools v1.3, Cufflinks]

### Ecological adaptation in European eels is based on phenotypic plasticity. (PNAS 2021)

- DOI: 10.1073/pnas.2022620118 | PMCID: PMC7848574 | PMID: 33479174
- Version used: **1.10**
- Evidence: The resulting alignments were sorted using Samtools v1.10 ( http://www.htslib.org/ ) and finally processed with MarkDuplicates from PicardTools v1.92 ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: alignment/mapping [SAMtools v1.10] -> variant calling [ANGSD v0.933] -> dimensionality reduction/clustering [R v3.6.1] -> differential/statistical testing [R v3.6.1]

### Testing hypotheses of a coevolutionary key innovation reveals a complex suite of traits involved in defusing the mustard oil bomb. (PNAS 2022)

- DOI: 10.1073/pnas.2208447119 | PMCID: PMC9907077 | PMID: 36508662
- Evidence: Using a published Pool-seq dataset ( P. napi ) ( 59 ), and two generated for this study ( P. brassicae, P. rapae; SI Appendix , Text 13 ) ( 60 ), each containing 24 individuals, reads were filtered and cleaned with SAMtools ( 61 ), and then mapped to their respective reference genomes with NextGenMap (v 0.5.5) ( 62 ).
- Full pipeline: alignment/mapping [SAMtools] -> visualisation [tidyverse] -> stage not stated [R]

### The human pathobiont <i>Malassezia furfur</i> secreted protease Mfsap1 regulates cell dispersal and exacerbates skin inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2212533119 | PMCID: PMC9894114 | PMID: 36442106
- Evidence: SAMtools ( 65 ) was used to index and sort the mapped BAM file from BWA.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R v4.0.0]

### Transposable elements drive intron gain in diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2209766119 | PMCID: PMC9860276 | PMID: 36417430
- Evidence: We aligned the RNA reads to the reference genome using STAR ( 51 ), calculated the depth at each site using samtools ( 52 ), and identified splice junctions using leafcutter ( 53 ).
- Full pipeline: alignment/mapping [MAFFT, SAMtools] -> differential/statistical testing [R, lme4] -> stage not stated [Python, RepeatMasker, phytools]

### Identification and functional validation of super-enhancers in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2215328119 | PMCID: PMC9860255 | PMID: 36409894
- Evidence: DNase-seq reads were mapped to A. thaliana TAIR10 genome using BWA aln ( 71 ) with default parameters and then convert to BAM format by SAMtools ( 72 ).
- Full pipeline: alignment/mapping [BWA, SAMtools, minimap2] -> stage not stated [BCFtools, BEDTools, R v4.0.4]

### Silencing RNAs expressed from W-linked &lt;i&gt;PxyMasc&lt;/i&gt; "retrocopies" target that gene during female sex determination in &lt;i&gt;Plutella xylostella&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2206025119 | PMCID: PMC9674220 | PMID: 36343250
- Evidence: The mapped alignment file was processed to identify sense and antisense reads using SAMtools ( 41 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [BLAST, Clustal Omega]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Version used: **1.7**
- Evidence: Samtools v1.7 and samjs v2927d9787 ( 98 ) were used to filter bam files.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: Summary statistics of read alignments were obtained using SAMtools flagstat ( 65 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Spatial turnover of soil viral populations and genotypes overlain by cohesive responses to moisture in grasslands. (PNAS 2022)

- DOI: 10.1073/pnas.2209132119 | PMCID: PMC9659419 | PMID: 36322723
- Version used: **1.11**
- Evidence: Competitive read recruitment against the dereplicated database of vOTUs was performed with Bowtie 2 v2.4.2 ( 79 ) in sensitive mode, and the resulting alignments were sorted and indexed with SAMtools v1.11 ( 80 ).
- Full pipeline: read trimming [Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.4.2, SAMtools v1.11] -> quantification [DESeq2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [QIIME 2] -> differential/statistical testing [DESeq2, R v3.6] -> stage not stated [ggplot2, igraph]

### Two intrinsic timing mechanisms set start and end times for dendritic arborization of a nociceptive neuron. (PNAS 2022)

- DOI: 10.1073/pnas.2210053119 | PMCID: PMC9659368 | PMID: 36322763
- Evidence: After an initial quality check, the reads were mapped to WS220 using BWA ( 67 ) and filtered using SAMtools ( 68 ).
- Full pipeline: quality control [BWA, SAMtools] -> alignment/mapping [BWA, SAMtools] -> quantification [ImageJ] -> visualisation [MACS2]

### Spatial scale of tuberculosis transmission in Lima, Peru. (PNAS 2022)

- DOI: 10.1073/pnas.2207022119 | PMCID: PMC9659349 | PMID: 36322726
- Evidence: We mapped the paired-end raw sequencing data to the H37Rv reference genome using the BWA-MEM (Burroughs Wheeler Aligner-Maximal Exact Match) algorithm ( 11 ) and used SAMtools and Pilon to identify the single-nucleotide polymorphisms (SNPs) and the insertions and deletions using a coverage-based approach ( 12 , 13 ).
- Full pipeline: alignment/mapping [BWA, Pilon, SAMtools]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Version used: **1.13**
- Evidence: After alignment, the 3′UTR was truncated from each bam file using samtools version 1.13 for analysis with REDItools and the AEI as described above to match the exact human chromosomal coordinates used with the NEPTUNE dataset.
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **1.9**
- Evidence: Mapped reads were then filtered by using SAMtools v.1.9 ( 95 ) to retain only correctly read pairs with a mapping-quality score of 10 or higher.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Polycomb group (PcG) proteins prevent the assembly of abnormal synaptonemal complex structures during meiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2204701119 | PMCID: PMC9586294 | PMID: 36215502
- Evidence: Reads were aligned to Drosophila genome release 6 using bowtie2 ( 68 ) and were q20 filtered with Samtools ( 69 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR, deepTools] -> normalisation [R, deepTools, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [MACS2]

### Microbiome composition modulates secondary metabolism in a multispecies bacterial community. (PNAS 2022)

- DOI: 10.1073/pnas.2212930119 | PMCID: PMC9586298 | PMID: 36215464
- Version used: **1.9**
- Evidence: Resulting SAM (sequence alignment map) files were sorted with samtools v1.9 ( 62 ) and quantified by HTSeq (high throughput sequencing Python library) v0.12.4 ( 63 ) under mode “intersection-strict” against the GFF (general feature format) files previously annotated by prodigal and antiSMASH.
- Full pipeline: alignment/mapping [HTSeq, SAMtools v1.9, fastp v0.20.0] -> quantification [HTSeq, SAMtools v1.9] -> differential/statistical testing [R v4.2] -> stage not stated [Bowtie2 v2.4.2, edgeR, eggNOG]

### Cryptic specialized metabolites drive <i>Streptomyces</i> exploration and provide a competitive advantage during growth with other microbes. (PNAS 2022)

- DOI: 10.1073/pnas.2211052119 | PMCID: PMC9546628 | PMID: 36161918
- Evidence: Reads were aligned to the S. venezuelae genome using Bowtie2 ( 60 ), then sorted, indexed, and converted to BAM format using SAMtools ( 61 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **1.3.1**
- Evidence: The aligned BAM files were sorted, and PCR-duplicated reads were removed using SAMtools v1.3.1 ( 93 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Recurrent emergence of <i>Klebsiella pneumoniae</i> carbapenem resistance mediated by an inhibitory <i>ompK36</i> mRNA secondary structure. (PNAS 2022)

- DOI: 10.1073/pnas.2203593119 | PMCID: PMC9499542 | PMID: 36095213
- Evidence: A pipeline comprising SAMtools mpileup v0.1.19 ( 40 ) and BCFtools v0.1.19 was used to call SNPs and generate a pseudogenome alignment.
- Full pipeline: alignment/mapping [BCFtools v0.1.19, BLAST v2.6.0, MUSCLE v3.8, SAMtools] -> stage not stated [Prokka v1.14.5, SPAdes v3.9.0]

### Diploid-dominant life cycles characterize the early evolution of Fungi. (PNAS 2022)

- DOI: 10.1073/pnas.2116841119 | PMCID: PMC9457484 | PMID: 36037379
- Version used: **1.5**
- Evidence: For short reads, k -mer counting was conducted on raw short reads using kmercountexact in bbtools ( https://sourceforge.net/projects/bbmap/ ) and allele frequencies were calculated from haploid or haploidized assemblies via a standard SNP calling approach using bwa mem v0.7.15 ( 78 ), samtools v1.5 ( 79 ), and GATK HaplotypeCaller v4.1.0.0 ( 80 ).
- Full pipeline: variant calling [GATK, SAMtools v1.5] -> structure determination [phytools] -> stage not stated [BUSCO]

### Additive genetic effects in interacting species jointly determine the outcome of caterpillar herbivory. (PNAS 2022)

- DOI: 10.1073/pnas.2206052119 | PMCID: PMC9456756 | PMID: 36037349
- Evidence: We then aligned the DNA sequences to the M. sativa or L. melissa genome and identified SNPs using samtools (versions 1.10), bcftools (version 1.9), and GATK (version 4.1) ( 61 , 62 ) ( SI Appendix , DNA Sequence Alignment and Variant Calling ).
- Full pipeline: alignment/mapping [BCFtools v1.9, GATK v4.1, SAMtools] -> variant calling [BCFtools v1.9, GATK v4.1, SAMtools]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Evidence: Those reads aligned to multiple loci and those duplicated reads aligned to the same locus were filtered out using SAMtools ( 58 ).
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Version used: **1.3**
- Evidence: To create genome sequences in a fasta format file, we extracted all reads mapping to the mtDNA using SAMtools, version 1.3 ( http://samtools.sourceforge.net ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### Nucleotide excision repair removes thymidine analog 5-ethynyl-2'-deoxyuridine from the mammalian genome. (PNAS 2022)

- DOI: 10.1073/pnas.2210176119 | PMCID: PMC9436350 | PMID: 35994676
- Evidence: The output .sam files were converted into .bam files by using SAMtools ( 47 ) and then were converted into .bed files using bedtools ( 48 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> stage not stated [BEDTools, SAMtools]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Evidence: We then used SAMtools to manipulate, convert, and sort output files from bwa-mem ( 70 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Balanced control of thermogenesis by nuclear receptor corepressors in brown adipose tissue. (PNAS 2022)

- DOI: 10.1073/pnas.2205276119 | PMCID: PMC9388101 | PMID: 35939699
- Evidence: Duplicate reads were removed with samtools rmdup.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, edgeR, kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR, kallisto] -> differential/statistical testing [R v4.1, edgeR, kallisto] -> stage not stated [Enrichr, SAMtools]

### Three distinct <i>Atoh1</i> enhancers cooperate for sound receptor hair cell development. (PNAS 2022)

- DOI: 10.1073/pnas.2119850119 | PMCID: PMC9371730 | PMID: 35925886
- Evidence: Mapped reads were sorted using Samtools ( 69 ), and duplicated reads were removed using the Picard MarkDuplicates function ( http://broadinstitute.github.io/picard ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Version used: **1.3**
- Evidence: Reads were aligned to Morex v1 reference sequence ( 44 ) with BWA v7.12 ( 45 ) and variants in the genomic space were called with SAMtools v1.3 ( 46 ), filtering for a minimum read depth of 5×, PHRED quality > 40.
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### Wnt signaling regulates hepatocyte cell division by a transcriptional repressor cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2203849119 | PMCID: PMC9335208 | PMID: 35867815
- Evidence: Raw reads were mapped with Bowtie 2 ( 66 ) and processed and sorted with Samtools ( 67 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [Fiji, ImageJ, MACS2]

### Pervasive transcription enhances the accessibility of H-NS-silenced promoters and generates bistability in &lt;i&gt;Salmonella&lt;/i&gt; virulence gene expression. (PNAS 2022)

- DOI: 10.1073/pnas.2203011119 | PMCID: PMC9335307 | PMID: 35858437
- Evidence: Read depth values (determined by the bedcov tool of the Samtools suite) were normalized to the values from the entire genome.
- Full pipeline: normalisation [SAMtools]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **0.1.18**
- Evidence: Binary sequence alignment files were generated and sorted using SAMtools version 0.1.18 ( 45 ).
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### Seed DNA damage responses promote germination and growth in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2202172119 | PMCID: PMC9335332 | PMID: 35858436
- Evidence: The clean reads were mapped onto the Arabidopsis reference genome (TAIR10) downloaded from Ensembl Plants (release 50) ( 46 ) using STAR ( 47 ), followed by converting, sorting, and indexing of the alignment files using SAMtools ( 48 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [SAMtools] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **1.9**
- Evidence: Integrated Genome Browser–compatible files were made using samtools (v1.9), sort and index, deepTools (v3.2.0), and bamCompare ( 44 , 45 ).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### A long noncoding RNA influences the choice of the X chromosome to be inactivated. (PNAS 2022)

- DOI: 10.1073/pnas.2118182119 | PMCID: PMC9282422 | PMID: 35787055
- Version used: **1.1.2**
- Evidence: Unmapped and nonprimary reads were removed with Samtools v1.1.2 (“Filter SAM or BAM, output SAM or BAM”).
- Full pipeline: read trimming [Trimmomatic v0.36.6] -> alignment/mapping [Bowtie2 v2.3.4.2] -> stage not stated [Fiji, ImageJ, SAMtools v1.1.2]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **1.10**
- Evidence: For the X chromosome, we specified a prior input ploidy based on a comparison of coverage with the autosomes using samtools depth [samtools v.1.10 ( 78 )].
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Version used: **1.11**
- Evidence: Graphpad Prism 8.0.2; Geneious Prime 2020.2.2; HISAT2 version 2.2.1; StringTie version 2.1.1; bwa version: 0.7.17-r1188; macs2 version 2.2.7.1; deeptools version 3.5.0; homer version 4.11; samtools version 1.11; bedtools version 2.30.0; R version 4.1.0; Custom code for using R packages are deposited at https://github.com/yl-lu/Rice_EC .
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### Expansion of a retrovirus lineage in the koala genome. (PNAS 2022)

- DOI: 10.1073/pnas.2201844119 | PMCID: PMC9231498 | PMID: 35696585
- Version used: **1.12**
- Evidence: Sequencing reads were mapped to the koala reference using BWA-MEM ( 31 ), pooled per individual with SAMtools 1.12 ( 32 ), and duplicate reads marked by Picard 2.23.4 (broadinstitute.github.io/picard/).
- Full pipeline: alignment/mapping [BWA, Picard v2.23.4, RepeatMasker, SAMtools v1.12] -> stage not stated [DELLY, R]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Evidence: The trimmed Illumina DNA sequence libraries from the three isolates were aligned against their respective reference genomes using Bowtie2 (v2.3.5.1; –very-sensitive –no-unal) ( 47 ), and the resulting bam files (one from each aligned library) were combined using samtools merge (v1.8).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### Targeted base editing in the mitochondrial genome of <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121177119 | PMCID: PMC9171795 | PMID: 35561225
- Evidence: SNPs were then called using samtools mpileup command (-uf -d 50000 -L 2000) and bcftools call command [-m -A -P 0.1 ( 46 )].
- Full pipeline: alignment/mapping [BWA v0.7.12] -> stage not stated [BCFtools, SAMtools]

### Enzymes degraded under high light maintain proteostasis by transcriptional regulation in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121362119 | PMCID: PMC9171785 | PMID: 35549553
- Version used: **1.3.1**
- Evidence: Uniquely aligned reads were sorted and indexed using Samtools v1.3.1 ( 75 ).
- Full pipeline: quality control [FastQC v0.11.7] -> alignment/mapping [SAMtools v1.3.1, featureCounts] -> differential/statistical testing [edgeR] -> stage not stated [Trim Galore]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: SAMtools ( 41 ) was then applied to convert Sam files to binary Bam files.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### A synthetic lethality screen reveals ING5 as a genetic dependency of catalytically dead Set1A/COMPASS in mouse embryonic stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2118385119 | PMCID: PMC9171609 | PMID: 35500115
- Evidence: Output binary alignment map files were converted into SAM (sequence alignment map) files using SAMtools ( 69 ), from which CIGAR strings were retrieved for each F0 sample and subsequently analyzed to determine which F0 mouse harbored an intended mutation in the Set1A SET domain.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [ImageJ, MACS2, Metascape]

### Genomewide CRISPR knockout screen identified PLAC8 as an essential factor for SADS-CoVs infection. (PNAS 2022)

- DOI: 10.1073/pnas.2118126119 | PMCID: PMC9170153 | PMID: 35476513
- Version used: **1.12**
- Evidence: BAM files were indexed using Samtools version 1.12.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [STAR v2.7.7a] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [R v4.0.3] -> stage not stated [Cytoscape, SAMtools v1.12, featureCounts]

### <i>duper</i> is a null mutation of Cryptochrome 1 in Syrian hamsters. (PNAS 2022)

- DOI: 10.1073/pnas.2123560119 | PMCID: PMC9170138 | PMID: 35471909
- Evidence: BAMs from the same samples were merged using samtools ( 52 ) (v1.9.0) merge.
- Full pipeline: stage not stated [BUSCO v4.0.6, Flye v2.7, GATK, SAMtools, SnpEff]

### Brap regulates liver morphology and hepatocyte turnover via modulation of the Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2201859119 | PMCID: PMC9171358 | PMID: 35476518
- Evidence: Alignments were visualized using samtools ( 25 ) and the IGV browser ( 26 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [R]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Variant calling was performed using SAMtools ( 67 ), VarScan ( 68 ), and GATK ( 69 ).
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### Ancient DNA gives new insights into a Norman Neolithic monumental cemetery dedicated to male elites. (PNAS 2022)

- DOI: 10.1073/pnas.2120786119 | PMCID: PMC9170172 | PMID: 35446690
- Version used: **1.3.1**
- Evidence: We merged together the libraries belonging to the same individuals using samtools v1.3.1 ( 72 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [SAMtools v1.3.1]

### rDNA array length is a major determinant of replicative lifespan in budding yeast. (PNAS 2022)

- DOI: 10.1073/pnas.2119593119 | PMCID: PMC9169770 | PMID: 35394872
- Evidence: Second, the alignments were filtered, requiring that both reads in the pair are mapped concordantly, using the “0 × 2” flag in samtools.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, SAMtools] -> stage not stated [BCFtools]

### Mutational background influences <i>P. aeruginosa</i> ciprofloxacin resistance evolution but preserves collateral sensitivity robustness. (PNAS 2022)

- DOI: 10.1073/pnas.2109370119 | PMCID: PMC9169633 | PMID: 35385351
- Evidence: SAMtools was used to index alignment files in BAM format ( 71 ).
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R] -> stage not stated [GATK, Picard, SnpEff, freebayes]

### An integrative skeletal and paleogenomic analysis of stature variation suggests relatively reduced health for early European farmers. (PNAS 2022)

- DOI: 10.1073/pnas.2106743119 | PMCID: PMC9169634 | PMID: 35389750
- Evidence: SAMtools was used to sort mapped reads and filter for mapping quality 30 and minimum bp 30, with duplicates removed using SAMtools rmdup ( 128 ).
- Full pipeline: alignment/mapping [SAMtools] -> variant calling [SnpEff] -> registration [GATK] -> stage not stated [PLINK v1.9, Picard]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Evidence: Multisample SNP calling was done by using SAMtools mpileup ( 66 ) and Varscan V2.4.0 ( 67 ) with a minimum coverage of eight and a minimum alternate allele count of four.
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Variation in upstream open reading frames contributes to allelic diversity in maize protein abundance. (PNAS 2022)

- DOI: 10.1073/pnas.2112516119 | PMCID: PMC9169109 | PMID: 35349347
- Evidence: The alignments were sorted and indexed with samtools ( 72 ) version 1.11, and reads that mapped to more than one location in the genome were discarded.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2, HTSeq, SAMtools] -> stage not stated [BLAST, R]

### Recombination resolves the cost of horizontal gene transfer in experimental populations of <i>Helicobacter pylori</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2119010119 | PMCID: PMC8944584 | PMID: 35298339
- Evidence: Donor coverage sequences were aligned to the putative HGT genomes produced from the application of the core HGT dataset via long-read mapping with BBMap ( https://jgi.doe.gov/data-and-tools/bbtools/ ) and consensus sequences generated with Samtools ( 72 ).
- Full pipeline: alignment/mapping [SAMtools, SPAdes] -> dimensionality reduction/clustering [R] -> stage not stated [Prokka]

### <i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import. (PNAS 2022)

- DOI: 10.1073/pnas.2123353119 | PMCID: PMC8931380 | PMID: 35275795
- Evidence: Single nucleotide polymorphisms (SNPs) were called using the “mpileup” function of SAMtools ( 36 ).
- Full pipeline: read trimming [Cutadapt v1.3, R, edgeR] -> alignment/mapping [BWA, TopHat, VCFtools] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [SAMtools]

### Precision targeting tumor cells using cancer-specific InDel mutations with CRISPR-Cas9. (PNAS 2022)

- DOI: 10.1073/pnas.2103532119 | PMCID: PMC8892319 | PMID: 35217600
- Version used: **1.10**
- Evidence: After removing the duplicated hits with Samtools (version 1.10) ( 39 ), we used Strelka2 (version 2.9.10) ( 40 ) with the default setting for calling germline variations.
- Full pipeline: stage not stated [SAMtools v1.10]

### An in-frame deletion mutation in the degron tail of auxin coreceptor <i>IAA2</i> confers resistance to the herbicide 2,4-D in <i>Sisymbrium orientale</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2105819119 | PMCID: PMC8892348 | PMID: 35217601
- Evidence: Raw read counts were extracted using sequence alignment/map (SAMtools) ( 39 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [SAMtools] -> differential/statistical testing [R v3.3, edgeR] -> stage not stated [BCFtools, BUSCO]

### LINEAGE: Label-free identification of endogenous informative single-cell mitochondrial RNA mutation for lineage analysis. (PNAS 2022)

- DOI: 10.1073/pnas.2119767119 | PMCID: PMC8812554 | PMID: 35086932
- Version used: **1.9**
- Evidence: A bam file consisting of mitochondrial DNA records, which were extracted from the alignment result with Samtools (version 1.9) ( 36 ), was obtained.
- Full pipeline: alignment/mapping [Python, SAMtools v1.9] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [GSEA, Seurat]

### Multiple spillovers from humans and onward transmission of SARS-CoV-2 in white-tailed deer. (PNAS 2022)

- DOI: 10.1073/pnas.2121644119 | PMCID: PMC8833191 | PMID: 35078920
- Version used: **1.11**
- Evidence: 49 ), samtools version 1.11 ( 50 ) for sequence and file manipulation ( 51 ), and iVar version 1.2.2 ( 52 ) for primer trimming and variant calling ( 53 ).
- Full pipeline: read trimming [SAMtools v1.11] -> alignment/mapping [QGIS, RAxML] -> variant calling [SAMtools v1.11] -> stage not stated [Pangolin v3.1.11]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: The resulting SAM files were converted to binary alignment map (BAM) files, using SAMtools-0.1.7a ( 31 ).
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### Molecular parallelism in signaling function across different sexually selected ornaments in a warbler. (PNAS 2022)

- DOI: 10.1073/pnas.2120482119 | PMCID: PMC8872772 | PMID: 35165176
- Version used: **1.7**
- Evidence: Next, we dropped reads with a quality score below 20 and converted the SAM files to BAM format using SAMtools (v1.7) ( 47 ).
- Full pipeline: alignment/mapping [R, featureCounts] -> normalisation [DESeq2] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.1.0, HISAT2 v2.1.0, ImageJ, SAMtools v1.7]

### Vertical stratification of the air microbiome in the lower troposphere. (PNAS 2022)

- DOI: 10.1073/pnas.2117293119 | PMCID: PMC8851546 | PMID: 35131944
- Version used: **1.10**
- Evidence: Mapped and unmapped reads were separated using Samtools v.1.10 ( 32 ).
- Full pipeline: quality control [Bowtie2 v2.4.1] -> read trimming [Bowtie2 v2.4.1, Cutadapt v1.8.1] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> visualisation [vegan]

### Loss of TET reprograms Wnt signaling through impaired demethylation to promote lung cancer development. (PNAS 2022)

- DOI: 10.1073/pnas.2107599119 | PMCID: PMC8832965 | PMID: 35110400
- Version used: **1.4**
- Evidence: Duplicated reads were removed using SAMtools (v1.4) for the subsequent analysis.
- Full pipeline: read trimming [Trim Galore v0.5.0] -> stage not stated [DESeq2, Picard v2.21.2, RepeatMasker, SAMtools v1.4]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Alignments were visualized using samtools ( 55 ) and the IGV browser ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### Epistatic genetic interactions govern morphogenesis during sexual reproduction and infection in a global human fungal pathogen. (PNAS 2022)

- DOI: 10.1073/pnas.2122293119 | PMCID: PMC8872808 | PMID: 35169080
- Evidence: For each of the above samples, paired-end, 100-bp sequenced reads were aligned to a JEC21(α) C. deneoformans reference genome ( 85 ) using BWA [v0.7.12-r1039 ( 86 )], and binary alignment maps were constructed using SAMtools [v0.1.1996b5f2294a ( 87 )].
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [ImageJ, scikit-learn]

### Stabilizing selection on Atlantic cod supergenes through a millennium of extensive exploitation. (PNAS 2022)

- DOI: 10.1073/pnas.2114904119 | PMCID: PMC8872764 | PMID: 35165196
- Evidence: Reads were aligned to the Atlantic cod reference genome gadMor2 ( 24 ) with the BWA software package ( 89 ) v0.7.5, before the alignments were indexed and sorted with the Samtools software package ( 90 ) v1.3.1.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R] -> stage not stated [VCFtools]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Version used: **1.6**
- Evidence: For each library, we calculated read coverage using “SAMtools v1.6 ( 39 ) depth” per bp and used average values for each 1-kb window.
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Evidence: A barcode of 738 exonic/coding SNPs were genotyped using the RNA-seq data to confirm sample identities using SAMtools mpileup ( 56 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Evidence: Variants were called using Samtools Mpileup (version 2.1.3) and filtered using Varscan (version 0.1) and Samtools filter pileup for SNPs and indels ( 78 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### No link between population isolation and speciation rate in squamate reptiles. (PNAS 2022)

- DOI: 10.1073/pnas.2113388119 | PMCID: PMC8795558 | PMID: 35058358
- Version used: **1.5**
- Evidence: We called variants across all individuals using samtools v1.5 ( 105 ), filtered variants to retain only those with coverage > 20× and quality > 20, and used this variant set to recalibrate alignments using GATK v4.1.8 ( 106 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [GATK v4.1.8, RAxML v8.2.11, SAMtools v1.5] -> stage not stated [R, phytools]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Evidence: SAMtools ( 36 ) view was used to filter uniquely mapped proper pairs with the following parameters: -b -q 60 -f 2.
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### AnchorWave: Sensitive alignment of genomes with high sequence diversity, extensive structural polymorphism, and whole-genome duplication. (PNAS 2022)

- DOI: 10.1073/pnas.2113075119 | PMCID: PMC8740769 | PMID: 34934012
- Version used: **1.10**
- Evidence: To calculate the proportion of the reference genome that was aligned and matched, all the alignments in MAF were reformatted into bam files using the “maf-convert sam” command of LAST and SAMtools v1.10 ( 52 ).
- Full pipeline: alignment/mapping [SAMtools v1.10, minimap2]

### A dicer-related helicase opposes the age-related pathology from SKN-1 activation in ASI neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2308565120 | PMCID: PMC10756303 | PMID: 38113255
- Version used: **1.10**
- Evidence: BAM files were sorted with Samtools v 1.10.
- Full pipeline: read trimming [STAR v2.7.6a, Trim Galore] -> alignment/mapping [STAR v2.7.6a] -> quantification [DESeq2, R v3.5.2] -> differential/statistical testing [DESeq2, R v3.5.2] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.7.1, SAMtools v1.10]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Finally, analysis-ready BAM files were generated by excluding reads with MAPQ < 30 using samtools.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Evidence: Samtools depth v1.12 ( 57 ) with the -a flag was used to obtain read depths at each genomic position and the median read coverage for pOXA-48 and chromosome was computed with GNU datamash v1.4 (gnu.org/software/datamash).
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: HOMER tag directories were created using the HOMER platform ( 51 ) (makeTagDirectory) from the aligned SAM formats using Samtools ( 52 ).
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### A Novel mechanism of herbicide action through disruption of pyrimidine biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2313197120 | PMCID: PMC10691210 | PMID: 37988466
- Evidence: High-quality sequences were aligned to TAIR10_cDNA reference database and SNPs were identified by using SAMtools ( http://samtools.sourceforge.net/ ) packages.
- Full pipeline: alignment/mapping [AlphaFold, SAMtools] -> stage not stated [PHENIX]

### Dual thermal ecotypes coexist within a nearly genetically identical population of the unicellular marine cyanobacterium &lt;i&gt;Synechococcus&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2315701120 | PMCID: PMC10665897 | PMID: 37972069
- Version used: **1.11**
- Evidence: Read filtering was done with bbduk (bbmap, v.38.90), and all reads mapped to the available reference genome for LA31 GCF_018502385.1 ( 25 ) using bowtie2 v.2.4.3 ( 61 ), and separated from non- Synechococcus reads using samtools v.1.11 ( 62 ) and BEDtools v.2.30 ( 63 ).
- Full pipeline: read trimming [minimap2 v2.17] -> alignment/mapping [BEDTools v2.30, Bowtie2 v2.4.3, SAMtools v1.11, minimap2 v2.17] -> normalisation [SPAdes v3.15.2] -> stage not stated [R]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Version used: **1.9**
- Evidence: Samtools v1.9 ( 86 ) was used to extract the unique mapped reads.
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### Expression signature of human endogenous retroviruses in chronic lymphocytic leukemia. (PNAS 2023)

- DOI: 10.1073/pnas.2307593120 | PMCID: PMC10622969 | PMID: 37871223
- Version used: **1.6**
- Evidence: Afterward, the mapped reads in SAM format were converted into BAM format, sorted (for coordinates), and indexed using Samtools (v.
- Full pipeline: read trimming [Bowtie2 v2.4.5, HISAT2 v2.1.0, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.1.0, SAMtools v1.6, featureCounts v2.0.0] -> quantification [R] -> differential/statistical testing [R, pheatmap v1.0.12] -> stage not stated [ComplexHeatmap, Cytoscape v3.9.1]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Version used: **0.1.19**
- Evidence: PCR duplicate reads were removed with SAMtools (v0.1.19) rmdup.
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Version used: **1.3.1**
- Evidence: ...o the soybean ZH13 reference genome ( 35 ) using Burrows Wheeler Aligner BWA-MEM software ( 71 ) with default parameters and were further filtered by SAMtools (version 1.3.1) ( 72 ) for nonunique and duplicated reads.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Version used: **1.3**
- Evidence: BAM alignment files were generated using SAMtools v.1.3 ( 63 ).
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Changes in parrot diversity after human arrival to the Caribbean. (PNAS 2023)

- DOI: 10.1073/pnas.2301128120 | PMCID: PMC10576146 | PMID: 37748079
- Version used: **1.10**
- Evidence: SAM files produced from the BWA mapping were converted to BAM files and sorted with SAMtools v.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BWA v0.7.13, IQ-TREE v2.1.2, SAMtools v1.10] -> stage not stated [BCFtools v1.12, MAFFT v7.455, R v4.1]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: The resulting Sequence Alignment/Map (SAM) files were converted to BAM format, sorted, and indexed using samtools.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Compression drives diverse transcriptomic and phenotypic adaptations in melanoma. (PNAS 2023)

- DOI: 10.1073/pnas.2220062120 | PMCID: PMC10523457 | PMID: 37722033
- Version used: **1.11**
- Evidence: Then, the mapping result is indexed by samtools (1.11).
- Full pipeline: alignment/mapping [SAMtools v1.11] -> dimensionality reduction/clustering [clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.18.1, GSEA, R] -> stage not stated [Cytoscape, GSVA, HTSeq v0.13.5, ImageJ]

### Sequencing 4.3 million mutations in wheat promoters to understand and modify gene expression. (PNAS 2023)

- DOI: 10.1073/pnas.2306494120 | PMCID: PMC10515147 | PMID: 37703281
- Version used: **1.7**
- Evidence: Alignments were sorted by using samtools v1.7 ( 91 ), and duplicate reads were removed with Picard tools v2.7.1 ( http://broadinstitute.github.io/picard/ ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, SAMtools v1.7] -> stage not stated [VEP]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Version used: **1.2**
- Evidence: Using samtools 1.2, sam files were compressed to bam files and then sorted and indexed.
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **1.9**
- Evidence: The SAM alignment files were converted to BAM format and indexed using SAMtools 1.9 ( 85 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Pangenome analyses reveal impact of transposable elements and ploidy on the evolution of potato species. (PNAS 2023)

- DOI: 10.1073/pnas.2211117120 | PMCID: PMC10401005 | PMID: 37487084
- Version used: **1.13**
- Evidence: The resulting binary alignment map (BAM) files were merged using Samtools v1.13 ( 89 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.7, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.13, Trim Galore v0.6.7] -> dimensionality reduction/clustering [R v4.1] -> stage not stated [AUGUSTUS, BUSCO v5.2.2, QUAST v5.0.2, RepeatMasker v4.1.1]

### Echoes of ancient introgression punctuate stable genomic lineages in the evolution of figs. (PNAS 2023)

- DOI: 10.1073/pnas.2222035120 | PMCID: PMC10334730 | PMID: 37399402
- Evidence: Variants were called using SAMtools, and a consensus sequence was generated using the mpileup command ( 72 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.450, RAxML] -> stage not stated [SAMtools]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: The processed BAM files were then indexed with Samtools ( 60 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: A pileup format was created using SAMtools ( 29 ), then variants were called using VarScan ( 30 ).
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Complex evolutionary processes maintain an ancient chromosomal inversion. (PNAS 2023)

- DOI: 10.1073/pnas.2300673120 | PMCID: PMC10288594 | PMID: 37311002
- Version used: **1.5**
- Evidence: We then used samtools (version 1.5) to compress, sort and index the alignments ( 67 ).
- Full pipeline: alignment/mapping [RepeatMasker v4.0.7, SAMtools v1.5] -> variant calling [BCFtools v1.6] -> stage not stated [BEAST v2.6.6, BUSCO v4.0.5, R v4.0.2]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: Quality control filtering was applied using Samtools.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Mechanoepigenetic regulation of extracellular matrix homeostasis via Yap and Taz. (PNAS 2023)

- DOI: 10.1073/pnas.2211947120 | PMCID: PMC10235980 | PMID: 37216538
- Evidence: Picard and Samtools were used to generate bam files and to filter out duplicates and mitochondrial reads.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2, Picard, SAMtools, deepTools, featureCounts]

### Osteolectin increases bone elongation and body length by promoting growth plate chondrocyte proliferation. (PNAS 2023)

- DOI: 10.1073/pnas.2220159120 | PMCID: PMC10235998 | PMID: 37216542
- Version used: **1.12**
- Evidence: Mapped reads were quality-filtered using SAMtools 1.12 to keep reads of MAPQ score > 10.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bowtie2 v4.1, Trim Galore v0.6.4] -> alignment/mapping [Bowtie2 v4.1, SAMtools v1.12, Trim Galore v0.6.4] -> stage not stated [deepTools v3.5.1]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: Resulting alignments were merged into a single BAM file using samtools ( 57 ).
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: Low mapping quality (MAPQ < 20) and PCR-duplicated reads were removed by (Sequence Alignment/Map format (SAMtools) and sambamba, respectively.
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: WGS data were also mapped to the hg38 genome using bowtie2 ( 59 ) (options: –no-mixed –no-discordant), and reads were further filtered using SAMtools ( 60 ) (options: -F 1804 –q 30).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### Digital microfluidics-based digital counting of single-cell copy number variation (dd-scCNV Seq). (PNAS 2023)

- DOI: 10.1073/pnas.2221934120 | PMCID: PMC10193948 | PMID: 37155890
- Version used: **1.9**
- Evidence: After sorting, SAMtools (version 1.9) was used to index the sorted and aligned reads; meanwhile, a summary file documenting all statistics was generated for each library.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.38] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.9] -> differential/statistical testing [SAMtools v1.9] -> stage not stated [BEDTools]

### The PLOD2/succinate axis regulates the epithelial-mesenchymal plasticity and cancer cell stemness. (PNAS 2023)

- DOI: 10.1073/pnas.2214942120 | PMCID: PMC10194013 | PMID: 37155842
- Evidence: Low-quality reads and duplicate reads were removed by SAMtools.
- Full pipeline: stage not stated [BEDTools, SAMtools]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **1.9**
- Evidence: Unmapped reads were removed from the alignment files using SAMtools v1.9 ( 91 ).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Spectra and characteristics of somatic mutations induced by ionizing radiation in hematopoietic stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2216550120 | PMCID: PMC10104525 | PMID: 37018193
- Evidence: To minimize false variant calls, we used only high-mapping-quality reads defined as MQ60 reads that met the following conditions: 1) properly mapped according to the aligner, 2) having a minimum mapping quality of 60 by SAMtools-1.9 (samtools view -q 60 -f 0 × 2 -F 0 × 500), and 3) mapped to the reference without clipping.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.0.0, Picard v2.18.26, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> differential/statistical testing [R v4.0.3]

### Genomics-driven breeding for local adaptation of durum wheat is enhanced by farmers' traditional knowledge. (PNAS 2023)

- DOI: 10.1073/pnas.2205774119 | PMCID: PMC10083613 | PMID: 36972461
- Evidence: Sequences of SNP marker probes were obtained by TraitGenetics GmbH (Germany) and mapped on the Svevo reference genome ( 38 ) available at the European Nucleotide Archive (Project: PRJEB22687) using bwa ( 58 ) and samtools ( 59 ) with no upstream filtering, obtaining a hypothetical genomic physical position for each marker.
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [R, ggplot2, tidyverse]

### Aneuploidy and gene dosage regulate filamentation and host colonization by &lt;i&gt;Candida albicans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2218163120 | PMCID: PMC10089209 | PMID: 36893271
- Evidence: Sequence Alignment/Map tools (SAMtools) v1.10 (r783) and Picard tools version 2.23.3 ( http://broadinstitute.github.io/picard ) were used to filter, sort, and convert the SAM files.
- Full pipeline: alignment/mapping [Picard, SAMtools, minimap2 v2.17] -> variant calling [VCFtools, minimap2 v2.17] -> differential/statistical testing [R] -> visualisation [Cutadapt] -> stage not stated [GATK, ImageJ, RAxML v8.2.12]

### Genome-wide maps of rare and atypical UV photoproducts reveal distinct patterns of damage formation and mutagenesis in yeast chromatin. (PNAS 2023)

- DOI: 10.1073/pnas.2216907120 | PMCID: PMC10013872 | PMID: 36853943
- Evidence: The resulting alignment files were processed with SAMtools ( 51 ) and BEDtools ( 52 ), and custom Perl scripts were used to identify the dinucleotide sequence immediately upstream of the 5′ end of each sequencing read.
- Full pipeline: alignment/mapping [BEDTools, Bowtie2, SAMtools] -> visualisation [PyMOL]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: The repeat masked assembly (Lenedo1_AssemblyScaffolds_Repeatmasked.fasta.gz from JGI) was indexed with bwa index (BWA), and paired-end Illumina reads (from QC) were mapped with bwa mem (BWA) using parameters “-M -t16” and samtools view using “-buS” (SAMtools).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Version used: **1.9.0**
- Evidence: The resulting bam files were sorted and indexed, and the unmapped reads removed using SAMtools v1.9.0 ( 67 ).
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Evidence: Alignment duplications were marked with sambamba (0.6.3) ( 65 ) and were filtered with samtools (view -q 30 -F 2308).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: We used SAMtools ( 134 ) and BCFtools ( 135 ) to call genotypes with base and mapping quality filters of >Q30, before filtering for insert size (50 to 5,000bp) and allele balance (AB), and retaining only biallelic sites with an AB of <0.25 and >0.75.
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Resurrection genomics provides molecular and phenotypic evidence of rapid adaptation to salinization in a keystone aquatic species. (PNAS 2023)

- DOI: 10.1073/pnas.2217276120 | PMCID: PMC9963159 | PMID: 36730191
- Evidence: The resulting files were piped through samtools ( 78 ) to mark duplicates, fix mates and sort the bam files.
- Full pipeline: quality control [Trimmomatic] -> read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools, BEDTools, SAMtools, VEP]

### PCIF1-mediated deposition of 5'-cap &lt;i&gt;N&lt;/i&gt;&lt;sup&gt;6&lt;/sup&gt;,2'-&lt;i&gt;O&lt;/i&gt;-dimethyladenosine in ACE2 and TMPRSS2 mRNA regulates susceptibility to SARS-CoV-2 infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210361120 | PMCID: PMC9945940 | PMID: 36689652
- Evidence: Sam files were converted to bam files and sorted using Samtools.
- Full pipeline: read trimming [Cutadapt v1.18, HISAT2 v2.1.0] -> alignment/mapping [Cutadapt v1.18, HISAT2 v2.1.0] -> quantification [DESeq2, HTSeq v0.11.2] -> stage not stated [SAMtools]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Version used: **1.10**
- Evidence: Mapped reads were sorted and indexed with samtools v1.10 ( 80 ) and then used for predicting IESs with BleTIES MILRAA v0.1.9, with options: --type subreads --junction_flank 5 --min_ies_length 15 --min_break_coverage 10 --subreads_pos_max_cluster_dist 5.
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### Community-engaged ancient DNA project reveals diverse origins of 18th-century African descendants in Charleston, South Carolina. (PNAS 2023)

- DOI: 10.1073/pnas.2201620120 | PMCID: PMC9934026 | PMID: 36623185
- Version used: **1.9**
- Evidence: Mapped reads were merged between sequencing runs and filtered for quality (>30), duplicates, and reads with multiple mappings using SAMtools v1.9 ( 60 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.9] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9]

### Non-B-form DNA tends to form in centromeric regions and has undergone changes in polyploid oat subgenomes. (PNAS 2023)

- DOI: 10.1073/pnas.2211683120 | PMCID: PMC9910436 | PMID: 36574697
- Version used: **1.3.1**
- Evidence: Mapped reads with SAMtools view -F -20 were extracted for subsequent analysis, and duplicates were removed using SAMtools v.1.3.1 ( 44 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA, Trimmomatic v0.36] -> alignment/mapping [BWA, MACS2, SAMtools v1.3.1, deepTools] -> normalisation [deepTools] -> visualisation [deepTools]

### High-frequency and functional mitochondrial DNA mutations at the single-cell level. (PNAS 2023)

- DOI: 10.1073/pnas.2201518120 | PMCID: PMC9910596 | PMID: 36577067
- Evidence: Reads mapped to the target regions were locally realigned with Freebayes bamleftalign (version 1.1.0) ( 82 ), and their base qualities were recalibrated with samtools calmd (version 1.6) ( 83 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools] -> registration [SAMtools] -> stage not stated [ANNOVAR, ggplot2]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: Following mapping, samtools was used to convert the alignment files from sequence alignment map (SAM) format to sorted, indexed binary alignment map (BAM) files, while discarding any alignment with mapping quality below 10 (−q 10) ( 114 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Version used: **1.9**
- Evidence: Mapped reads were then collated into a single file using samtools v1.9 ( 65 ), which was sorted and duplicate reads marked using biobambam2 ( 66 ), and bases recalibrated using baseRecalibrator from the GATK software suite v3.5 ( 67 ).
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Version used: **1.16.1**
- Evidence: The original data were transformed into bam documents by BWA-MEN (v0.7.17) ( 85 ) and SAMtools (v1.16.1) ( 93 ).
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: The alignments were sorted and indexed using Samtools ( 98 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Version used: **1.13**
- Evidence: Reads were mapped to the H37Rv genome [RefSeq identifier GCF_000195955.2 with socAB annotation added as previously described ( 76 )] using Bowtie2 v2.4.1 ( 77 ) and sorted using samtools v1.13 ( 78 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### The fork protection complex generates DNA topological stress-induced DNA damage while ensuring full and faithful genome duplication. (PNAS 2024)

- DOI: 10.1073/pnas.2413631121 | PMCID: PMC11626154 | PMID: 39589889
- Evidence: SAM files were then converted into sorted BAM files by using SAMtools ( http://samtools.sourceforge.net/ ).
- Full pipeline: stage not stated [Bowtie2, MACS2, SAMtools]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Reads were then aligned to the Atlantic salmon genome downloaded from Ensembl (Salmo_salar-GCA_905237065.2) using “Bowtie2” ( 73 ) and parameters “--very-sensitive --maxins 1500 --end-to-end”. “Samtools view” was used to filter for primary alignments with mapping quality score over 20 (“-F 256 -q 20”). “Picard MarkDuplicates” ( 74 ) was used to identify and remove duplicate reads.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### An E2 ubiquitin-conjugating enzyme links diubiquitinated H2B to H3K27M oncohistone function. (PNAS 2024)

- DOI: 10.1073/pnas.2416614121 | PMCID: PMC11621828 | PMID: 39560642
- Version used: **1.8**
- Evidence: Bam files were sorted and indexed using samtools v1.8.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [deepTools v3.3.1] -> stage not stated [ChimeraX, SAMtools v1.8]

### The glucocorticoid receptor potentiates aldosterone-induced transcription by the mineralocorticoid receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2413737121 | PMCID: PMC11588051 | PMID: 39541347
- Evidence: Bam files were merged using samtools.
- Full pipeline: quality control [Cutadapt v1.18] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2, STAR v2.70] -> normalisation [DESeq2] -> stage not stated [HOMER, SAMtools]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: For identification of retrograde transported barcodes unmapped reads from the Cell Ranger output was extracted (samtools) and remapped to a hybrid genome mCherry inserted.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Homeotic and nonhomeotic patterns in the tetrapod vertebral formula. (PNAS 2024)

- DOI: 10.1073/pnas.2411421121 | PMCID: PMC11588047 | PMID: 39527744
- Evidence: We mapped the raw reads for the chicken data to the bGalGal1 genome assembly using bowtie2 ( 104 ) with standard parameters and used samtools ( 105 ) with standard parameters to remove duplicates and sort the alignments.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [BLAST, BUSCO, SciPy, phytools]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: Trimmed reads were mapped to the template genome assembly of LAB-S, a susceptible lab strain of H. zea (from Benzon Research Inc.), and to the de novo genome assembly of H. zea strain GA-R ( 61 ) using BWA ( 100 ) and sorted using SAMtools ( 101 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **1.16.1**
- Evidence: Nonprimary alignments were removed with samtools version 1.16.1 ( 69 ) and coverage was generated by BEDTools version 2.30.0 ( 58 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### A novel &lt;i&gt;N&lt;/i&gt;4,&lt;i&gt;N&lt;/i&gt;4-dimethylcytidine in the archaeal ribosome enhances hyperthermophily. (PNAS 2024)

- DOI: 10.1073/pnas.2405999121 | PMCID: PMC11551388 | PMID: 39471227
- Evidence: Using samtools, alignments were removed where the MAPQ score was <20 and when detected as a PCR duplicate.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [AlphaFold]

### AMBRA1 controls the translation of immune-specific genes in T lymphocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2416722121 | PMCID: PMC11536168 | PMID: 39436665
- Evidence: To create bigwig files, BAM files were first indexed with samtools using default settings, and bigwig files were generated with the bamCoverage function from deepTools.
- Full pipeline: quantification [HTSeq] -> normalisation [pheatmap] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, SAMtools, deepTools]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Version used: **0.1.18**
- Evidence: Generated reads were mapped to the human (hg19) reference genome using TopHat v2.1.1 in combination with Bowtie2 v2.2.8 and SAMtools v0.1.18.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Unveiling the DHX15-G-patch interplay in retroviral RNA packaging. (PNAS 2024)

- DOI: 10.1073/pnas.2407990121 | PMCID: PMC11459146 | PMID: 39320912
- Evidence: The genome coverage was calculated using the SAMtools ( 70 ).
- Full pipeline: stage not stated [AlphaFold, SAMtools]

### Local cryptic diversity in salinity adaptation mechanisms in the wild outcrossing &lt;i&gt;Brassica fruticulosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407821121 | PMCID: PMC11459175 | PMID: 39316046
- Evidence: Rsubread package was used to map the paired-end reads to the reference genome ( 84 ) and samtools ( 85 ) was used for sorting and indexing.
- Full pipeline: quality control [FastQC] -> read trimming [Trim Galore, Trimmomatic] -> alignment/mapping [GATK, SAMtools, Trimmomatic] -> variant calling [ANGSD v0.939, GATK] -> differential/statistical testing [Bioconductor, DESeq2, R v4.2] -> visualisation [ggplot2] -> stage not stated [BUSCO v5.2.2, Flye, HTSeq, Picard, Pilon v1.24]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Version used: **1.16.1**
- Evidence: Reads were filtered using samtools (version 1.16.1) for mapping quality of >10 for Z. mays , S. bicolor , U. fusca , and O. sativa .
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Evidence: Falcon primary contigs were polished with Racon v1.4.20 ( 93 ) using read mappings from pbmm2 v1.4.0 filtered with samtools view using options -F 1796 -q 20 (exclude unmapped reads, nonprimary alignments, reads that fail platform/quality checks, and PCR or optical duplicates; minimum quality Phred 20).
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **1.10**
- Evidence: Multi- or no mate reads were removed with samtools (v1.10) ( 70 ) view (-q 4 -F 0x2).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### Transdifferentiation occurs without resetting development-specific DNA methylation, a key determinant of full-function cell identity. (PNAS 2024)

- DOI: 10.1073/pnas.2411352121 | PMCID: PMC11441492 | PMID: 39292740
- Evidence: Reads were aligned using the biscuit align command and the output was sorted using the “sort” command from “samtools” package.
- Full pipeline: read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, SAMtools, Trim Galore] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, R]

### Plasma cell-free RNA signatures of inflammatory syndromes in children. (PNAS 2024)

- DOI: 10.1073/pnas.2403897121 | PMCID: PMC11406294 | PMID: 39240972
- Version used: **1.14**
- Evidence: DNA contamination was estimated by calculating the ratio of reads mapping to introns and exons. rRNA contamination was measured using SAMtools (v1.14).
- Full pipeline: quality control [SAMtools v1.14] -> alignment/mapping [SAMtools v1.14] -> quantification [DESeq2, R] -> machine learning [Snakemake] -> stage not stated [featureCounts]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Evidence: The alignment files (SAM) were further refined using SAMtools, applying a parameter (“-q 30”), to eliminate reads with multiple hits, and were converted to BAM format.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Imprinted X chromosome inactivation in marsupials: The paternal X arrives at the egg with a silent DNA methylation profile. (PNAS 2024)

- DOI: 10.1073/pnas.2412185121 | PMCID: PMC11388282 | PMID: 39190362
- Evidence: Hisat2 version 2.1.0 and samtools ( 49 ) version 1.13 were used.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bismark] -> normalisation [R] -> stage not stated [SAMtools]

### The role of emerging elites in the formation and development of communities after the fall of the Roman Empire. (PNAS 2024)

- DOI: 10.1073/pnas.2317868121 | PMCID: PMC11388374 | PMID: 39159385
- Evidence: This involved trimming and merging reads, which were then mapped to GRCh37 using samtools ( 48 ).
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [SAMtools] -> variant calling [VCFtools] -> normalisation [VCFtools] -> stage not stated [ADMIXTURE, Picard]

### An additional proofreader contributes to DNA replication fidelity in mycobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322938121 | PMCID: PMC11348249 | PMID: 39141351
- Evidence: The variant calling was performed with SAMtools and Genome Analysis Toolkit ( 63 ).
- Full pipeline: variant calling [GATK, SAMtools] -> stage not stated [AlphaFold]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: Reads that mapped to multiple locations in the reference genome or had quality scores below 25 were excluded using SAMtools v/1.9 ( 79 ).
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: Resulting SAM files were converted into sorted BAM file using samtools ( 68 ).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### Directed evolution of material-producing microorganisms. (PNAS 2024)

- DOI: 10.1073/pnas.2403585121 | PMCID: PMC11295069 | PMID: 39042685
- Version used: **1.3.1**
- Evidence: To quantify the quality of the assembly, coverage statistics were calculated using the short read data using samtools 1.3.1 ( 63 ).
- Full pipeline: alignment/mapping [Prokka v1.13] -> quantification [SAMtools v1.3.1] -> differential/statistical testing [SAMtools v1.3.1] -> stage not stated [ImageJ]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: Resulting SAM files were converted to sorted binary files (BAM) and indexed using SAMtools ( 27 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: To determine the proportion of forward strand read counts belonging to mRNA and cRNA, the ratio of mRNA to cRNA reads was determined by calculating the depth of coverage on the forward strand at either the 3′ polyA tail sequence (for the mRNA) or a segment-specific 3′ cRNA sequence following 5 to 6 adenosines (for the cRNA) using SAMtools ( 40 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: Reads with a mapping quality Phred score >30 were selected and retained using the SAMtools ( 86 ) v1.4 view command (-q 30), and duplicate reads were discarded using “FilterUniqueSAMCons.py” ( 87 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Version used: **1.9**
- Evidence: We converted the output SAM files into BAM, removed duplicates using the fixmate mode with the -m flag and the markdup mode with the -r flag and sorted them out by their leftmost coordinates with SAMtools v1.9 ( 57 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: ...es to mouse index genome mm10, downloaded from bowtie2’s manual ( https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml ) on 2 May 2023 ( 44 , 45 ) SAMtools (Version 1.13) sort, view, fixmate, and markdup were used to remove PCR duplicates, with SAMtools index and view used to remove mitochondrial sequences ( 46 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### Membrane association of active genes organizes the chloroplast nucleoid structure. (PNAS 2024)

- DOI: 10.1073/pnas.2309244121 | PMCID: PMC11252823 | PMID: 38968115
- Version used: **1.13**
- Evidence: Read counts on defined genomic regions (annotated genes or bins) were determined using samtools v.1.13 ( 60 ) and bedtools v.2.30.0 ( 61 ).
- Full pipeline: read trimming [Bowtie2 v2.4.4, Cutadapt v3.5] -> alignment/mapping [Bowtie2 v2.4.4, Cutadapt v3.5] -> quantification [BEDTools v2.30.0, SAMtools v1.13]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Version used: **1.12**
- Evidence: Subsequently, the SAM file was converted to BAM format and sorted using SAMtools (v1.12) ( 70 ).
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Modeling 0.6 million genes for the rational design of functional <i>cis</i>-regulatory variants and de novo design of <i>cis-</i>regulatory sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2319811121 | PMCID: PMC11214048 | PMID: 38889146
- Version used: **1.9**
- Evidence: The resulting bam files were sorted by SAMtools (version 1.9) ( 45 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.1.0] -> alignment/mapping [FastQC v0.11.5, HISAT2 v2.1.0] -> quantification [StringTie v2.0, featureCounts] -> normalisation [StringTie v2.0, featureCounts] -> dimensionality reduction/clustering [Python] -> stage not stated [DESeq2, Keras, SAMtools v1.9, TensorFlow, WGCNA]

### A MOZ-TIF2 leukemia mouse model displays KAT6-dependent H3K23 propionylation and overexpression of a set of active developmental genes. (PNAS 2024)

- DOI: 10.1073/pnas.2405905121 | PMCID: PMC11214132 | PMID: 38889153
- Version used: **1.14**
- Evidence: Duplicate reads were removed with samtools 1.14 using the markdup command ( 55 ).
- Full pipeline: quality control [Cutadapt v4.1, Trimmomatic v0.36] -> read trimming [Cutadapt v4.1, Trimmomatic v0.36] -> alignment/mapping [Bioconductor, DESeq2, deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA] -> visualisation [ggplot2] -> stage not stated [BEDTools, SAMtools v1.14]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Version used: **1.9**
- Evidence: SAMtools (version 1.9) was used for SNP calling with default settings.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Long noncoding RNA LIRIL2R modulates FOXP3 levels and suppressive function of human CD4<sup>+</sup> regulatory T cells by regulating IL2RA. (PNAS 2024)

- DOI: 10.1073/pnas.2315363121 | PMCID: PMC11161746 | PMID: 38805281
- Version used: **1.9**
- Evidence: Alignment, sorting, filtering, and deduplication for the CUT&Tag analysis was performed using Bowtie2 (v2.3.5.1) ( 60 ), Samtools (v1.9) ( 61 ), and Picard ( http://broadinstitute.github.io/picard/ ) MarkDuplicates (v2.21.7) with the same parameters as described in the ATAC-seq analysis.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9, kallisto] -> differential/statistical testing [R, limma v3.42.2] -> stage not stated [GSEA]

### Clocking out and letting go to unleash green biotech applications in a photosynthetic host. (PNAS 2024)

- DOI: 10.1073/pnas.2318690121 | PMCID: PMC11127020 | PMID: 38739791
- Version used: **1.11.0**
- Evidence: 2.2.1 ( 39 ) was used to build an index using assembly sequences available in NCBI (GenBank assembly accession: GCA_000012525.1) and to align our sequencing reads with the genome, and samtools v.
- Full pipeline: alignment/mapping [SAMtools v1.11.0] -> quantification [DESeq2 v1.36.0] -> normalisation [R] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HISAT2 v2.2.1, ggplot2, pheatmap v1.0.12]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Version used: **1.14**
- Evidence: We prepared PSMC input files by creating a consensus diploid sequence for each sample (i.e., a single representative individual from each country-level population with >18× coverage) using a pipeline combining SAMtools v1.14 ( 89 ), Picard v2.26.10, and BCFtools v1.14.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### DNA lesion bypass and the stochastic dynamics of transcription-coupled repair. (PNAS 2024)

- DOI: 10.1073/pnas.2403871121 | PMCID: PMC11098089 | PMID: 38717857
- Evidence: The transcription strand of RNA-seq reads was resolved using read-end and mapping orientation extracted by Samtools view (v.1.7.0) and read-pairs exclusively mapping within annotated exons were identified using Bedtools intersect (v.2.29.2).
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Evidence: We converted the resulting sam files to bam format with samtools ( 88 ), cleaned, sorted, added read groups, and marked duplicates using picardtools ( https://broadinstitute.github.io/picard ).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Evidence: Reads were aligned to the reference genome using hisat2 v2.2.1 ( 80 ) with parameters –no-unal –max-intronlen 25000 –dta and sorted using samtools ( 81 ) v1.12.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: Samtools was used to remove PCR duplicates and Sambamba was used to remove multimapping reads ( 61 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### Development of an orally bioavailable mSWI/SNF ATPase degrader and acquired mechanisms of resistance in prostate cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2322563121 | PMCID: PMC11009648 | PMID: 38557192
- Evidence: Data were then transformed into Binary Alignment Map (BAM) files using SAMtools.
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [Strelka]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: Subsequent analyses for visualization of ChIP-seq were done using samtools ( 60 ), deeptools ( 61 ), and SparK ( 62 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Aerosolization of viable <i>Mycobacterium tuberculosis</i> bacilli by tuberculosis clinic attendees independent of sputum-Xpert Ultra status. (PNAS 2024)

- DOI: 10.1073/pnas.2314813121 | PMCID: PMC10962937 | PMID: 38470917
- Version used: **1.5**
- Evidence: Reads were then mapped to the reconstructed ancestor of the MTBC ( 61 ) using bwa v0.717 ( 62 ) Duplicates were removed using Picard v2.9.1 ( 63 ), prior to using Samtools v1.5 ( 64 ) and varScan v2.2.4 ( 65 ) call variants, with filters to exclude sites with fewer than 10 reads support and minimum base quality scores of 20.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard v2.9.1, SAMtools v1.5] -> differential/statistical testing [R] -> structure determination [Picard v2.9.1, SAMtools v1.5] -> stage not stated [Kraken2]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Evidence: Trimmed reads were aligned to the reference genome mSarHar1.11 ( 25 ) using BWA MEM version 0.7.17 ( 81 ) with the -M flag and default settings, and Samtools ( 82 ) was used to sort the aligned reads.
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Evidence: We used Samtools ( 94 ) to sort reads, Picard to add read groups, and Samtools to index alignments.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### Endogenous virophages are active and mitigate giant virus infection in the marine protist <i>Cafeteria burkhardae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2314606121 | PMCID: PMC10945749 | PMID: 38446847
- Evidence: Coverage of integrated virophages was determined with “samtools bedcov” v1.9 ( 47 ) and aggregated with a custom R script.
- Full pipeline: alignment/mapping [minimap2 v2.22] -> stage not stated [BLAST, Flye v2.9.1, SAMtools]

### Environmental radiation exposure at Chornobyl has not systematically affected the genomes or chemical mutagen tolerance phenotypes of local worms. (PNAS 2024)

- DOI: 10.1073/pnas.2314793121 | PMCID: PMC10945782 | PMID: 38442158
- Version used: **1.11**
- Evidence: These subsetted Illumina reads for each sample were aligned to CEW1 reference genome using minimap2 v2.17 and samtools v1.11 ( 48 , 51 ) (minimap2 -ax sr -R [manually added readgroup], samtools view -S -b, samtools sort, samtools index).
- Full pipeline: alignment/mapping [GATK v4.3.0.0, R, SAMtools v1.11, VCFtools v0.1.16, minimap2] -> variant calling [GATK v4.3.0.0] -> stage not stated [BCFtools v1.14, Flye v2.8.1, ImageJ]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: Resulting reads were mapped to a reference of the human genome (GRCh38) using STAR ( 46 ), and full read alignments were converted to indexed BAM files with SAMtools ( 47 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Genome copy number predicts extreme evolutionary rate variation in plant mitochondrial DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2317240121 | PMCID: PMC10927533 | PMID: 38427600
- Evidence: Samtools-depth v.1.14 was used to calculate the mapping depth for each base pair of each gene ( 80 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.5, SAMtools] -> differential/statistical testing [R v4.2.2] -> visualisation [ggplot2] -> stage not stated [RAxML, SPAdes]

### Genomic ancestry and social dynamics of the last hunter-gatherers of Atlantic France. (PNAS 2024)

- DOI: 10.1073/pnas.2310545121 | PMCID: PMC10927518 | PMID: 38408241
- Evidence: For each library, we merged bam files resulting from all resequencing rounds using samtools merge v1.5.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [PLINK, SAMtools]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Evidence: The alignments are then compressed using Samtools view in CRAM format, sorted by coordinates using Samtools sort, and indexed using Samtools index (v1.10).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Version used: **1.3**
- Evidence: The resulting bam files were sorted, PCR duplicates removed, SNPs phased, and merged using SAMtools ver.
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: Alignments were sorted and subsequently merged into VCF files using SAMtools ( 112 ), BEDtools ( 113 ), and VCFtools ( 114 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### Targeted hypermutation of putative antigen sensors in multicellular bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316469121 | PMCID: PMC10907252 | PMID: 38354254
- Evidence: Mapped reads were extracted with samtools ( 89 ).
- Full pipeline: read trimming [MAFFT v7.407] -> alignment/mapping [MAFFT v7.407, SAMtools, minimap2 v2.24] -> visualisation [HMMER] -> stage not stated [InterProScan]

### Isolation, characterization, and circulation sphere of a filovirus in fruit bats. (PNAS 2024)

- DOI: 10.1073/pnas.2313789121 | PMCID: PMC10873641 | PMID: 38335257
- Version used: **1.10**
- Evidence: To check the quality of assembly, we mapped these reads back to the complete sequence using bowtie2 version 2.4.1 and calculated the sequencing coverage using samtools version 1.10.
- Full pipeline: quality control [SPAdes, fastp v0.20.0] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> quantification [ImageJ] -> visualisation [ImageJ, PyMOL v2.4.0] -> stage not stated [BLAST v0.9.35]

### Coordination of rhythmic RNA synthesis and degradation orchestrates 24- and 12-h RNA expression patterns in mouse fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2314690121 | PMCID: PMC10873638 | PMID: 38315868
- Version used: **1.11**
- Evidence: The bam files generated by STAR (see above) were sorted and indexed by Samtools (version 1.11) ( 79 ) and converted into bigWig files by DeepTools (version 3.5.0) ( 80 ) with the option -filterRNAstrand in order to visualize strand specifically.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, STAR v2.7.7a] -> quantification [HOMER] -> visualisation [SAMtools v1.11] -> stage not stated [DESeq2 v1.32.0, R]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: Samtools software ( 43 ) was used to mark duplicates.
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### Streamlined identification of clinically and functionally relevant genetic regulators of lower-tract urogenital development. (PNAS 2024)

- DOI: 10.1073/pnas.2309466121 | PMCID: PMC10861909 | PMID: 38300866
- Evidence: Per base read counts were obtained using the Samtools ( 74 ) mpileup algorithm.
- Full pipeline: quantification [ImageJ, SAMtools] -> stage not stated [HOMER]

### High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310854121 | PMCID: PMC10823218 | PMID: 38241433
- Evidence: PCR duplicates were removed and the precise locations of CPD lesions were extracted using Samtools and Bedtools ( 44 , 48 ), as described in our published methods.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, Python] -> simulation/modelling [GROMACS, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [BEDTools, SAMtools]

### Sm complex assembly and 5' cap trimethylation promote selective processing of snRNAs by the 3' exonuclease TOE1. (PNAS 2024)

- DOI: 10.1073/pnas.2315259121 | PMCID: PMC10801842 | PMID: 38194449
- Evidence: Briefly, reads were first mapped to the human hg38 genome (STAR --outFilterMultimapNmax 1000 --alignIntronMin 9999999 --outFilterMultimapScoreRange --outFilterMismatchNoverLmax 0.2) and reads mapping to small RNA genes were extracted using bedtools ( 66 ) and samtools ( 67 ).
- Full pipeline: alignment/mapping [BEDTools, SAMtools, STAR v2.7.8a] -> stage not stated [ImageJ]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Evidence: (sand cat, European wildcat, Chinese mountain cat, Asian wildcat, and African wildcat) were mapped to those of their close relative with a high-quality assembly genome, the domestic cat (GCF_018350175.1) with the bwa mem algorithm ( 64 ) and samtools/bcftools (v1.1) ( 65 ) with its consensus algorithm, to generate five consensus genomes.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Anellovirus protein encoded by &lt;i&gt;ORF2/3&lt;/i&gt; functions as the viral replication initiation protein. (PNAS 2025)

- DOI: 10.1073/pnas.2516306122 | PMCID: PMC12772153 | PMID: 41433061
- Version used: **1.20**
- Evidence: We used the resulting alignments form the RNA-seq pipeline to quantify the host and nrVL4619 transcript isoforms using StringTie v2.2.3 ( 80 ), in units of Transcripts per Million Mapped (TPM), then extracted the nrVL4619 transcripts using samtools v1.20 ( 81 ) to quantify the relative TPM values of the nrVL4619 transcripts exclusively.
- Full pipeline: alignment/mapping [SAMtools v1.20, StringTie v2.2.3] -> quantification [SAMtools v1.20, StringTie v2.2.3] -> stage not stated [AlphaFold, Conda, fastp v0.23.4]

### Distinguishing subtypes of endothelial cells in the mouse aorta. (PNAS 2025)

- DOI: 10.1073/pnas.2525755122 | PMCID: PMC12704785 | PMID: 41343672
- Evidence: Samtools software (version 1.16.1) was used to filter out the duplicated reads, and the Subread package (version 1.4.6-p5) was used to summarize the gene counts with the featureCounts function.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat] -> stage not stated [R, SAMtools, featureCounts]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Version used: **1.11**
- Evidence: Duplicate reads in the resulting BAM files were marked using Samtools version 1.11 and Picard (GATK version 4.2.0.0).
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: Barcodes and scars were extracted from the GFP-positive cells by using Samtools, facilitating the construction of lineage networks and enabling a detailed analysis of cellular trajectories and clonal relationships ( Fig.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### Nanorate sequencing reveals the &lt;i&gt;Arabidopsis&lt;/i&gt; somatic mutation landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2514194122 | PMCID: PMC12685076 | PMID: 41296725
- Evidence: Optical duplicates were then marked using SAMtools fixmate -m, Sambamba sort, and SAMtools markdup -d 2500 ( 105 , 106 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2] -> stage not stated [MACS2, SAMtools, SciPy, Snakemake]

### A 120-y time series of genomes reveals the consequences of closed breeding in German Shepherd Dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421755122 | PMCID: PMC12684887 | PMID: 41284896
- Version used: **1.9**
- Evidence: Raw reads were processed with AdapterRemoval v.2.3.3 ( 47 ), with collapsed reads mapped to the CanFam3.1 reference assembly ( 48 ) using bwa aln v.0.7.17-r1188 ( 49 ), PCR duplicates removed with samtools v.1.9 ( 50 ), and ancient DNA authenticated with MapDamage ( 51 ).
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.5.3, SAMtools v1.9] -> stage not stated [ADMIXTURE v1.3.0, IQ-TREE v2.1.4, PLINK v1.90b]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Version used: **1.9**
- Evidence: Reads were processed using AdapterRemoval v.2.3.3 ( 68 ), with collapsed reads mapped to the CanFam3.1 reference assembly ( 26 ) using bwa aln v.0.7.17-r1188 ( 69 ), PCR duplicates removed with samtools v.1.9 ( 70 ), and ancient DNA authenticated with MapDamage [ SI Appendix , Fig.
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### Anthropocene genetic diversity loss in the marine tropics. (PNAS 2025)

- DOI: 10.1073/pnas.2513012122 | PMCID: PMC12646237 | PMID: 41231948
- Version used: **1.9**
- Evidence: Reads with a minimum mapping quality less than 30, unmapped reads, and reads with secondary or supplementary alignments were filtered with SAMtools v.1.9 ( 69 ).
- Full pipeline: quality control [VCFtools v0.1.14] -> alignment/mapping [SAMtools v1.9, SPAdes v3.15.3] -> dimensionality reduction/clustering [ADMIXTURE v1.3, PLINK v1.9] -> stage not stated [freebayes v1.3.1]

### Genome-wide strand-specific UV mutagenesis in &lt;i&gt;&lt;i&gt;Escherichia coli&lt;/i&gt;&lt;/i&gt; is directed by the Mfd translocase. (PNAS 2025)

- DOI: 10.1073/pnas.2523368122 | PMCID: PMC12646321 | PMID: 41231941
- Evidence: Output BAM files were sorted by coordinate and filtered using samtools to retain only properly paired alignments.
- Full pipeline: read trimming [STAR v2.7, Trimmomatic] -> alignment/mapping [SAMtools, STAR v2.7] -> normalisation [deepTools] -> stage not stated [Conda, Snakemake]

### An ADAR2-mimic base editor for efficient C-to-U RNA editing in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2505269122 | PMCID: PMC12625888 | PMID: 41196347
- Version used: **1.21**
- Evidence: Next, data (bam files) were sorted and indexed using SAMtools (v.1.21).
- Full pipeline: quality control [FastQC v0.12.1, Trim Galore v0.6.10] -> read trimming [FastQC v0.12.1, HISAT2, Trim Galore v0.6.10] -> alignment/mapping [HISAT2] -> stage not stated [SAMtools v1.21, SnpEff v5.2]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: The mapped reads were sorted and indexed by SAMtools ( 43 ), and duplicate reads were marked by Picard MarkDuplicates.
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Homology-mediated transformation of frog-killing fungus &lt;i&gt;Batrachochytrium dendrobatidis&lt;/i&gt; illuminates chytrid development and pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507572122 | PMCID: PMC12595416 | PMID: 41150711
- Version used: **1.14**
- Evidence: Mapping rates (≥99.8%) and sequencing depth (range: 217 to 411) were then calculated using Samtools v1.14 ( 40 ).
- Full pipeline: alignment/mapping [SAMtools v1.14, minimap2 v2.28] -> stage not stated [BLAST, BUSCO v5.2.2, QUAST v5.0.0, R v4.0.2]

### A new late Neanderthal from Crimea reveals long-distance connections across Eurasia. (PNAS 2025)

- DOI: 10.1073/pnas.2518974122 | PMCID: PMC12625898 | PMID: 41144685
- Version used: **1.20**
- Evidence: Unmapped reads were removed with samtools v.1.20 and PCR duplicates were filtered out with GATK MarkDuplicates v.3.1.1.
- Full pipeline: alignment/mapping [ANGSD, Python] -> stage not stated [GATK, SAMtools v1.20]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **1.20**
- Evidence: Reads were aligned to UCSC hg38 using STAR (v2.7.11b) with spliced alignment parameters, followed by BAM file sorting (sambamba v1.0.1) and indexing (samtools v1.20).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Genetic regulation of the estrogen receptor and inherited predisposition to breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2517736122 | PMCID: PMC12582305 | PMID: 41129222
- Version used: **1.10**
- Evidence: Subsequent processing was carried out with SAMtools v1.10 ( 51 ) and Genome Analysis Toolkit (GATK) v4.1.4 ( 52 ), including sorting and merging of BAM files, removal of duplicate reads, realigning indels and recalibrating base quality scores.
- Full pipeline: variant calling [freebayes v1.3] -> registration [GATK, SAMtools v1.10]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Version used: **1.9**
- Evidence: We then used samtools v1.9-4-deb_cv1 ( 78 ) to fix mate-pairs, remove PCR duplicates, and remove reads with a mapping quality less than 20.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Mitotic recombination events and single-base mutations induced by ultraviolet light in G1-arrested yeast cells. (PNAS 2025)

- DOI: 10.1073/pnas.2518046122 | PMCID: PMC12557804 | PMID: 41091767
- Evidence: Raw reads were aligned to the reference genome of S288c using BWA ( 39 ), and the resulting alignments were processed with Samtools ( 40 ) for format conversion, sorting, and indexing.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [VarScan]

### A species interaction kick-starts ecological speciation in allopatry. (PNAS 2025)

- DOI: 10.1073/pnas.2506625122 | PMCID: PMC12557528 | PMID: 41082661
- Evidence: SAM files were converted to BAM format using samtools .
- Full pipeline: alignment/mapping [BWA] -> stage not stated [BCFtools, GATK, SAMtools, VCFtools, lme4]

### Sperm and offspring production in a nonobstructive azoospermia mouse model via testicular mRNA delivery using lipid nanoparticles. (PNAS 2025)

- DOI: 10.1073/pnas.2516573122 | PMCID: PMC12557808 | PMID: 41082659
- Version used: **1.20**
- Evidence: Aligned reads were converted to BAM format and sorted using SAMtools (v1.20).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt v3.2] -> alignment/mapping [Bowtie2 v2.3.5.1, Cutadapt v3.2, SAMtools v1.20] -> stage not stated [deepTools]

### Natural history of liver fluke infection underpins epidemiological patterns of biliary cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2423536122 | PMCID: PMC12541340 | PMID: 41071656
- Version used: **1.9**
- Evidence: The resulting BAM files were then sorted and indexed with samtools v.1.9.
- Full pipeline: stage not stated [GATK v4.1.4.1, Mutect2, SAMtools v1.9]

### Endosome transcriptomics reveal trafficking of Cajal bodies into multivesicular bodies. (PNAS 2025)

- DOI: 10.1073/pnas.2511840122 | PMCID: PMC12541449 | PMID: 41060753
- Evidence: ...d zcat Individual ncRNA hits were validated by comparing their alignment in Integrative Genomics Viewer after creating an index of each bam file with samtools: samtools index output.bam Northern Blot Analysis.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, SAMtools] -> quantification [Cutadapt]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We calculated the depth and breadth of coverage for each sample from BAM files using SAMtools ( 88 ) ( SI Appendix , Table S1 ).
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Evidence: Postalignment processing was performed using Picard, MarkDuplicates, SAMtools, and deepTools.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Version used: **1.16**
- Evidence: After mapping, the resulting SAM files were sorted, converted to BAM files, and indexed using Samtools version 1.16 ( 66 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: Uniquely mapped reads were kept for downstream analysis using Samtools-1.9 and Sambamba-6.7 ( 51 , 52 ), bigwig files were calculated using deepTools-3.1.1 ( 53 ) with a bin size of 50 bp, before visualization in IGV-2.12.3 ( 54 ).
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Mutations in the circadian cycle drive adaptive plasticity in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2506928122 | PMCID: PMC12435244 | PMID: 40901874
- Version used: **1.6**
- Evidence: The processed reads were aligned against the complete genome sequence of S. elongatus , strain PCC 7942 (GenBank accession number: GCF_000012525.1) using Hisat (v2.2.1) ( 63 ), processing the intermediate alignment files and merging the technical replicates with Samtools (v1.6) ( 64 ).
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [StringTie v2.2.1, featureCounts v2.0.1] -> normalisation [StringTie v2.2.1] -> differential/statistical testing [DESeq2 v1.34.0, R v4.2.1]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: The bam files of each sample were merged by Samtools, and subsequently, styleDnase.pl of Homer2 was used for peak-calling.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Shared metabolism between a bacterial and fungal species that reside in the human gut. (PNAS 2025)

- DOI: 10.1073/pnas.2504785122 | PMCID: PMC12415286 | PMID: 40854125
- Version used: **1.14**
- Evidence: After alignment, resulting BAM files were filtered using Samtools (1.14) to discard any reads less than 30 bp long ( 64 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.14] -> quantification [featureCounts v2.0.1] -> normalisation [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2]

### Aphid herbivory on macrophytes drives adaptive evolution in an aquatic community via indirect effects. (PNAS 2025)

- DOI: 10.1073/pnas.2502742122 | PMCID: PMC12403121 | PMID: 40838887
- Evidence: Raw data were quality-checked and trimmed using TrimGalore v0.6.1 ( 29 ), and reads were mapped toward the D. magna reference genome ( 30 ) using BWA ( 31 ) and SAMtools ( 32 ).
- Full pipeline: quality control [BWA, SAMtools, Trim Galore v0.6.1] -> read trimming [BWA, SAMtools, Trim Galore v0.6.1] -> alignment/mapping [BWA, SAMtools, Trim Galore v0.6.1] -> differential/statistical testing [lme4]

### Factors underlying a latitudinal gradient in the S/G lignin monomer ratio in natural poplar variants. (PNAS 2025)

- DOI: 10.1073/pnas.2503491122 | PMCID: PMC12403099 | PMID: 40833412
- Evidence: SNPs and InDels were called using SAMtools/BCFtools and annotated with SnpEff.
- Full pipeline: dimensionality reduction/clustering [R, WGCNA] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BCFtools, SAMtools, SnpEff]

### Fragmentation signatures in cancer patients resemble those of patients with vascular or autoimmune diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2426890122 | PMCID: PMC12402995 | PMID: 40833414
- Evidence: Samtools flagstat ( 88 ) was used to evaluate alignment.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2, SAMtools] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy v1.13.1] -> stage not stated [Picard]

### Minimizing and quantifying uncertainty in AI-informed decisions: Applications in medicine. (PNAS 2025)

- DOI: 10.1073/pnas.2424203122 | PMCID: PMC12402999 | PMID: 40833408
- Evidence: Samtools flagstat ( 83 ) was used to evaluate sequencing quality.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2] -> differential/statistical testing [scikit-learn] -> stage not stated [Picard, RepeatMasker, SAMtools]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Version used: **1.3.1**
- Evidence: All samples were aligned to the human reference genome (GRCh38) version using bwa 0.7.15, the generated SAM file was compressed into a BAM file and sorted by genomic position using samtools 1.3.1 and variant calling was performed using Genome Analysis Toolkit 3.7 software ( 61 , 62 ).
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### Inbreeding reduces fitness in spatially structured populations of a threatened rattlesnake. (PNAS 2025)

- DOI: 10.1073/pnas.2501745122 | PMCID: PMC12403008 | PMID: 40825128
- Version used: **1.9**
- Evidence: Alignments were filtered and sorted using Samtools v.
- Full pipeline: alignment/mapping [BWA v07.17, SAMtools v1.9] -> variant calling [BCFtools v1.9.64] -> stage not stated [R]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Evidence: For visualization purposes, mapped reads of each replicate sample were merged using SAMtools [v1.10; ( 56 )].
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### DNA polymerase β suppresses somatic indels at CpG dinucleotides in developing cortical neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2506846122 | PMCID: PMC12377747 | PMID: 40802685
- Evidence: For SNV and small indel calling, to minimize false variant calls, we exclusively used only highly reliable (HR) reads meeting the following conditions were extracted: 1) properly mapped according to the aligner, 2) mapping with a quality score of ≥60 using SAMtools-1.9 (samtools view -q 60 -f 0 × 2 -F 0 × 500) ( 72 ), and 3) mapping to the reference without clipping.
- Full pipeline: alignment/mapping [BWA, GATK v4.1.0.0, Picard, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> stage not stated [HOMER]

### A 65-kb deletion survey identifies a distal &lt;i&gt;cis-&lt;/i&gt;regulatory region for red-light induction of &lt;i&gt;Ghd7&lt;/i&gt;, a key rice floral repressor. (PNAS 2025)

- DOI: 10.1073/pnas.2423119122 | PMCID: PMC12377723 | PMID: 40811470
- Version used: **1.19**
- Evidence: SAMtools (version 1.19) was used to convert SAM files to BAM format and create index files.
- Full pipeline: quality control [FastQC v0.12.1, fastp v0.23.4] -> read trimming [FastQC v0.12.1, fastp v0.23.4] -> alignment/mapping [HISAT2 v2.2.1, minimap2] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [SAMtools v1.19, featureCounts]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **1.16.1**
- Evidence: Contig read depth was calculated with samtools v1.16.1 (only primary alignments) ( 131 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Evidence: ...processed through the subsequent steps: a) map the short reads to a reference genome (hg19) using the BWA software (v0.7.12-r1039) ( 46 ); b) use the SAMtools software (v0.1.18) to sort the short sequences and convert the format of the data; c) use the Picard software (v1.134) ( http://broadinstitute.github.io/picard/ ) to mark duplicate reads; d) use the Genome Analysis Toolkit (GATK v3.7) ( 47 )...
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### Targeted deletions of large syntenic regions in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419744122 | PMCID: PMC12377758 | PMID: 40789032
- Version used: **1.17**
- Evidence: In order to verify the locations of the deletions in each sample, the reads were then mapped to the Araport11 A. thaliana Col-0 genome from Phytozome ( https://phytozome-next.jgi.doe.gov/info/Athaliana_Araport11 ) using minimap2 v2.24-r1122 ( 43 ) and samtools v1.17 ( 44 ) to sort the resulting mapping file.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17, minimap2 v2.24] -> quantification [ImageJ] -> visualisation [seaborn v0.12.2] -> stage not stated [DESeq2 v1.44.0, Python, eggNOG]

### Measuring the selective packaging of RNA molecules by viral coat proteins in cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505190122 | PMCID: PMC12377776 | PMID: 40789029
- Version used: **1.16.1**
- Evidence: The alignment results, initially stored in sequence alignment map (SAM) format, were converted to binary alignment map (BAM) format using samtools (v1.16.1) ( 78 ) view command.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1] -> structure determination [PHENIX]

### Transcription termination promotes splicing efficiency and fidelity in a compact genome. (PNAS 2025)

- DOI: 10.1073/pnas.2507187122 | PMCID: PMC12358841 | PMID: 40763012
- Evidence: Resulting bam files were coordinate sorted and converted to bed files using SAMtools ( 35 ) and Bedtools ( https://bedtools.readthedocs.io/en/latest/ ) for downstream analyses.
- Full pipeline: alignment/mapping [featureCounts, minimap2] -> quantification [DESeq2, featureCounts] -> normalisation [DESeq2] -> stage not stated [BEDTools, SAMtools]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Evidence: The clean reads were mapped to the durum wheat genome assembly Svevo.v1 ( 36 ) and the reference-guide de novo transcript assembly described above with HiSat2 ( 43 ), and UMIs quantified with SAMtools ( 58 ) and UMI-tools ( 59 ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### SCoTCH-seq reveals that 5-hydroxymethylcytosine encodes regulatory information across DNA strands. (PNAS 2025)

- DOI: 10.1073/pnas.2512204122 | PMCID: PMC12337322 | PMID: 40743391
- Version used: **1.19.2**
- Evidence: Data from lanes 1 and 2 of each NovaSeq run were then merged with SAMtools (v1.19.2) ( 46 ) and deduplicated in paired-end mode with Picard (v3.1.1) ( 47 ).
- Full pipeline: read trimming [Cutadapt v4.6, Picard v3.1.1, SAMtools v1.19.2] -> stage not stated [BEDTools v2.31.0, Snakemake v7.3.8, deepTools]

### Synthesis of large single-transcript pathways from oligonucleotide pools: Design of STARBURST, an autobioluminescent reporter. (PNAS 2025)

- DOI: 10.1073/pnas.2508109122 | PMCID: PMC12337302 | PMID: 40729380
- Evidence: Briefly, it uses minibar ( 46 ) to demultiplex reads, chopper ( 47 ) to remove low-quality reads, minimap2 ( 48 ) to map reads to reference sequences, and samtools ( 49 ), bcftools ( 49 ), bedtools ( 50 ), racon ( 51 ), medaka ( 52 ), seqtk ( 53 ), emboss ( 54 ), and parallel ( 55 ) to generate consensus sequences, annotate variants, and output summaries.
- Full pipeline: read trimming [BCFtools, BEDTools, SAMtools, minimap2]

### Genomics of Neotropical biodiversity indicators: Two butterfly radiations with rampant chromosomal rearrangements and hybridization. (PNAS 2025)

- DOI: 10.1073/pnas.2410939122 | PMCID: PMC12337270 | PMID: 40720651
- Version used: **1.17**
- Evidence: Samtools (v1.17) ( 99 ) and GATK3 HaplotypeCaller (v3.8.1.0) ( 100 , 101 ) were used for variant calling, with a minimum base quality score of 20.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [RepeatMasker v4.1.5, minimap2] -> variant calling [SAMtools v1.17, minimap2] -> normalisation [vegan] -> dimensionality reduction/clustering [vegan] -> visualisation [R, minimap2, phytools, vegan] -> stage not stated [ADMIXTURE, BEAST, BUSCO v5.7.1, Picard, VCFtools v0.1.16]

### Genomic origins and evolution of neo-sex chromosomes in Pacific Island birds. (PNAS 2025)

- DOI: 10.1073/pnas.2503746122 | PMCID: PMC12337287 | PMID: 40720643
- Version used: **1.11**
- Evidence: We calculated the mean read depth on each contig using samtools (v1.11; ref.
- Full pipeline: read trimming [Trim Galore v0.6.2, hifiasm] -> alignment/mapping [Trim Galore v0.6.2, hifiasm] -> stage not stated [BUSCO v5.2.2, R, RepeatMasker v4.1.2, SAMtools v1.11, minimap2 v2.26]

### Genetic rescue of Florida panthers reduced homozygosity but did not swamp ancestral genotypes. (PNAS 2025)

- DOI: 10.1073/pnas.2410945122 | PMCID: PMC12337334 | PMID: 40720660
- Evidence: The mapped alignment files were viewed with the command “samtools view -Sb -F 1804,” followed by sorting and indexing.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [GATK v4.2, SAMtools] -> variant calling [GATK v4.2] -> normalisation [BEDTools] -> visualisation [BEDTools] -> stage not stated [RepeatMasker, SnpEff, tidyverse]

### A trans-species cytoplasmic polymorphism is associated with seed shape and aridity across multiple species of sunflowers. (PNAS 2025)

- DOI: 10.1073/pnas.2410943122 | PMCID: PMC12337292 | PMID: 40720659
- Version used: **1.10**
- Evidence: Variants were then called using samtools (v1.10) mpileup and bcftools (v1.10.2) call assuming a haploid state for individual samples for the entire cytoplasmic genome, and then merged together into a single VCF ( 87 ).
- Full pipeline: read trimming [Trimmomatic v0.22] -> alignment/mapping [Trimmomatic v0.22] -> variant calling [GATK] -> stage not stated [BCFtools v1.10.2, IQ-TREE, SAMtools v1.10]

### Inference of human pigmentation from ancient DNA by genotype likelihoods. (PNAS 2025)

- DOI: 10.1073/pnas.2502158122 | PMCID: PMC12304992 | PMID: 40663601
- Version used: **1.11**
- Evidence: For the direct and probabilistic approaches, we generated a pileup file from the alignment data for the 41 HIrisPlex-S positions using SAMtools v1.11 mpileup command ( 43 ).
- Full pipeline: alignment/mapping [SAMtools v1.11] -> variant calling [GATK]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Version used: **1.14**
- Evidence: The reads aligned to the NOD2 region (chr 16, positions 50727517-50766986) were extracted in sam format with sam-dump from the same toolkit and converted to bam format using samtools (version 1.14) ( 93 ).
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Tandem ssDNA in neutrophil extracellular traps binds thrombin and regulates immunothrombosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418191122 | PMCID: PMC12260427 | PMID: 40608679
- Version used: **1.6**
- Evidence: The raw reads are aligned by BWA/MEM (0.7.17-r1188) ( 72 ) and the product was transformed into bam file and sorted with samtools (v1.6) ( 73 ).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.6] -> stage not stated [BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1]

### Signal peptide-independent secretion of keratin-19 by pancreatic cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2426218122 | PMCID: PMC12260553 | PMID: 40591600
- Evidence: The base called reads were aligned to the reference genome (hg38 for Panc1 and m39 for FC1242) using minimap2 (v2.26) with the parameter “-ax splice.” All primary alignments to KRT19 that have a mapping quality of at least 30 were extracted with “samtools view.” The coverage along the gene was visualized as a UCSC Genome Browser track.
- Full pipeline: alignment/mapping [SAMtools, minimap2 v2.26] -> visualisation [SAMtools, minimap2 v2.26] -> stage not stated [ImageJ]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Version used: **1.8**
- Evidence: We then used samtools v1.8 ( 72 ) to sort and index the alignments as well as to remove duplicates and GATK IndelRealigner v3.4.0 ( 73 ) to realign the reads mapped around indels.
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### In vivo directed evolution of an ultrafast Rubisco from a semianaerobic environment imparts oxygen resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2505083122 | PMCID: PMC12260525 | PMID: 40587785
- Evidence: Alignments were down-sampled to 10% to reduce file size, then were indexed, sorted, and a pileup file was generated using Samtools ( 53 ).
- Full pipeline: alignment/mapping [SAMtools]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: Reads that aligned twice or more and unassembled reads (chrM, random, and chrUn) were removed by using samtools ( 63 ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: Samtools (view-s) was used to downsample each replicate to approximately 95 million reads ( 59 ).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### An ancient origin of the naked grains of maize. (PNAS 2025)

- DOI: 10.1073/pnas.2503748122 | PMCID: PMC12207465 | PMID: 40526715
- Version used: **1.13**
- Evidence: Using bam files containing the raw reads for ZEAMAP individuals, we verified and further assessed genotypes at the causal mutation for all individuals in the ZEAMAP dataset with the SAMtools v.1.13 ( 95 ) mpileup function.
- Full pipeline: alignment/mapping [BCFtools v1.13] -> variant calling [R v4.4.2, SAMtools v1.13, VCFtools v0.1.13] -> dimensionality reduction/clustering [R v4.4.2] -> visualisation [R v4.4.2]

### Homoploid hybridization adds clarity to the origins of octoploid strawberries. (PNAS 2025)

- DOI: 10.1073/pnas.2502814122 | PMCID: PMC12207424 | PMID: 40531871
- Evidence: Read coverage for every 10-kb window was obtained using the bedcov function in samtools V1.19 ( 61 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [GATK, IQ-TREE, OrthoFinder, SAMtools]

### Single Antisense Oligonucleotides Correct Diverse Splicing Mutations in Hotspot Exons. (PNAS 2025)

- DOI: 10.1073/pnas.2425659122 | PMCID: PMC12207475 | PMID: 40523177
- Evidence: SAMtools idxstats ( 48 ) was used to count the number of reads corresponding to each input and output species in each replicate sequencing library.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [SAMtools, VEP]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Version used: **1.14**
- Evidence: Candidate GRC sequences were also identified by mapping male germline and somatic short reads (PRJNA779416) with bwa v.0.7.17 ( 70 ) to the female assembly, filtering out alignments to remove those with mapping quality < 30 (samtools v.1.14) and calculating the degree of germline enrichment using DifCover v.3.0.1 ( 9 , 10 ) to process all discontiguous 1 kb intervals of low-copy sequence with read...
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **1.16.1**
- Evidence: ... ), STAR v2.7.10a ( 90 ), picard v3.0.0 ( 91 ), qualimap v2.3 ( 92 ), rseqc v5.02 ( 93 ), salmon v1.10.1 ( 94 ), summarizedExperiment v1.24.0 ( 95 ), samtools v1.16.1 ( 96 ), stringtie v2.2.1 ( 97 ), tximeta v1.12.0 ( 98 ), UCSC v377, and v445 https://github.com/ucscGenomeBrowser/kent .
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: The mapping quality score ≥ 30 were kept by Samtools ( 61 ) (Version 1.9).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### High-throughput metabolic engineering of &lt;i&gt;Yarrowia lipolytica&lt;/i&gt; through gene expression tuning. (PNAS 2025)

- DOI: 10.1073/pnas.2426686122 | PMCID: PMC12168020 | PMID: 40460129
- Evidence: Subsequently, Samtools (accessible at https://github.com/samtools/samtools ) was utilized to calculate the average coverage, coverage rate, and abundance for each plasmid.
- Full pipeline: alignment/mapping [minimap2] -> quantification [SAMtools] -> stage not stated [Python]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Evidence: The mapped reads were sorted and duplicates were marked with samtools ( 57 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: Alignments were then sorted and indexed using Samtools (V.1.10) ( 52 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Version used: **1.7**
- Evidence: S1 ) and trimmed 3 bp from all ancient mapped reads using the TrimBam function of bamUtil v.1.0.6 ( 108 ) and reindexed using samtools v1.7 ( 109 ).
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### Genomic map of the functionally extinct northern white rhinoceros (&lt;i&gt;Ceratotherium simum cottoni&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2401207122 | PMCID: PMC12107126 | PMID: 40359041
- Evidence: We aligned the nanopore reads to the reference genome using Minimap2 ( 59 ) with parameters -ax map-ont and kept primary alignments using Samtools ( 60 ) with parameter -F 2308.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> stage not stated [BUSCO, Pilon]

### RNA sequencing analysis of viromes of &lt;i&gt;Aedes albopictus&lt;/i&gt; and &lt;i&gt;Aedes vexans&lt;/i&gt; collected from NEON sites. (PNAS 2025)

- DOI: 10.1073/pnas.2403591122 | PMCID: PMC12107137 | PMID: 40354533
- Evidence: Sequence Alignment/Maptools v1.9 [SAMtools ( 37 )] was used to convert and sort the output BAM (Binary Alignment and Map) file.
- Full pipeline: read trimming [BWA, fastp v0.21.1] -> alignment/mapping [BLAST, BWA, Kraken2, SAMtools] -> stage not stated [Bowtie2, R]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Version used: **1.3**
- Evidence: ChIP-Seq read alignment as performed using Bowtie2 v2.2.7 ( 79 ) on human genome sequence (assembly hg38) with options --local and alignment files sorted and converted to bam using samtools v1.3 ( 80 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Version used: **1.18**
- Evidence: 68 . a region of the genome containing the locus and 50 kb of flanking sequence was extracted using BEDtools v2.30.0 and SAMtools v1.18 ( 69 , 70 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: ( 64 ), we processed the mapping results with samtools [v.0.1.19; ( 63 )] to keep only primary alignments and mark potential read duplicates.
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### Colony pattern multistability emerges from a bistable switch. (PNAS 2025)

- DOI: 10.1073/pnas.2424112122 | PMCID: PMC12002352 | PMID: 40184178
- Version used: **1.9**
- Evidence: Specifically, all properly mapped reads were separated according to their mapped strands using samtools (v1.9) ( 57 ). mRNA abundance ϕ i m was calculated by the following equation: ϕ i m = 10 - 6 · TPM i = # i reads / l i ∑ j # j reads / l j , where # i reads represents the number of mapped reads of gene i , l i denotes the length of gene i .
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.9] -> quantification [SAMtools v1.9] -> machine learning [Cellpose] -> stage not stated [ImageJ v1.53c]

### &lt;i&gt;LMX1B&lt;/i&gt; missense-perturbation of regulatory element footprints disrupts serotonergic forebrain axon arborization. (PNAS 2025)

- DOI: 10.1073/pnas.2411716122 | PMCID: PMC12002326 | PMID: 40168115
- Evidence: Biological replicate read data were merged with Samtools and mapped reads were downsampled to 100 M reads each with sambamba v1.0 ( 59 ).
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [MACS2, R v4.3, ggplot2 v3.4.4]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Version used: **1.9**
- Evidence: Only uniquely mapped reads with quality score ≥20 were retained for each sample using Samtools (version 1.9).
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### Genomics highlight an underestimation of phenology sensitivity to the urban heat island effect. (PNAS 2025)

- DOI: 10.1073/pnas.2408564122 | PMCID: PMC11962471 | PMID: 40100635
- Evidence: To align sequence reads to the Q. rubra reference genome [ https://phytozome-next.jgi.doe.gov/info/Qrubra_v2_1 ; ( 22 )], we indexed the reference genome and aligned the sequences to the assembly using BWA-MEM ( 40 ) and generated binary alignment map (BAM) files using SAMtools ( 41 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [PLINK, R]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Evidence: The bam files of mapped reads were merged, sorted, and indexed with Samtools ( 110 ), read groups were added with Picard v.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **1.10**
- Evidence: Unmapped reads, multimapped reads, and unpaired reads were filtered by Samtools (version 1.10, https://github.com/samtools/samtools ), and PCR-duplicated reads were removed using Sambamba (version 0.7.1) ( 81 ).
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### The NAE1-mediated neddylation operates as an essential post-translational modification checkpoint for effector CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424061122 | PMCID: PMC11912420 | PMID: 40030035
- Evidence: The resulting raw reads were trimmed by Trim Galore v0.6.10 and aligned to reference genome mm10 with HISAT2 V2.2.1 in combination with Samtools V1.2.
- Full pipeline: read trimming [HISAT2, SAMtools, Trim Galore v0.6.10] -> alignment/mapping [HISAT2, SAMtools, Trim Galore v0.6.10] -> stage not stated [DESeq2, GSEA, pheatmap]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Version used: **1.9**
- Evidence: In order to identify CNV within our resequenced common ragweed individuals, we analyzed depth of coverage in nonoverlapping 10 kbp windows using Samtools v1.9 depth ( 89 ) on alignment bam files.
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Genomic divergence across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2319389122 | PMCID: PMC11912424 | PMID: 40014554
- Version used: **1.15.1**
- Evidence: Genomic regions with a match to the reference were extracted from the query using samtools (v1.15.1) and culled of redundancies and any genomic fragments smaller than 100 bp in length.
- Full pipeline: stage not stated [BLAST, BUSCO, SAMtools v1.15.1]

### Ancient genomes reveal trans-Eurasian connections between the European Huns and the Xiongnu Empire. (PNAS 2025)

- DOI: 10.1073/pnas.2418485122 | PMCID: PMC11892651 | PMID: 39993190
- Version used: **1.9**
- Evidence: We discard reads with phred mapping quality <30 with “-q” parameter in Samtools v1.9 ( 81 ).
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [Cytoscape v3.9.1, Picard]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Version used: **1.9**
- Evidence: Reads were depleted for mitochondria alignment and for multimapped reads with samtools (v1.9).
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### Exercise intensity and training alter the innate immune cell type and chromosomal origins of circulating cell-free DNA in humans. (PNAS 2025)

- DOI: 10.1073/pnas.2406954122 | PMCID: PMC11761974 | PMID: 39805013
- Evidence: The nuclear:mitochondrial read coverage ratio was calculated using samtools to obtain the average base pair coverage for the mitochondrial genome (mitochondrial read coverage) and an equivalent sized region of chromosome 7 (nuclear read coverage).
- Full pipeline: quantification [Bismark] -> stage not stated [BEDTools, SAMtools]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Version used: **0.1.19**
- Evidence: SAMtools (version 0.1.19) removed the low-quality reads (MAPQ < 30) and PCR duplication reads.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Evidence: The workflow used bedtools ( 58 ) (v2.30.0), bioconductor-summarized experiment (v1.20.0), bioconductor-tximeta (v1.8.0), gffread ( 59 ) (v0.12.1), picard (v2.25.7), salmon ( 60 ) (v1.5.2), samtools ( 61 ) (v1.13), star ( 62 ) (v2.6.1d), stringtie ( 63 ) (v2.1.7), Trimgalore (v0.6.7, GitHub—FelixKrueger/TrimGalore: A wrapper around Cutadapt and FastQC to consistently apply adapter and quality trim...
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Version used: **1.17**
- Evidence: Transcriptome data were aligned to the genome using HISAT v2.2.1 ( 49 ), and the successfully aligned reads were converted into a BAM file using Samtools v1.17 ( 50 ).
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Restriction-modification systems are required for &lt;i&gt;Neisseria gonorrhoeae&lt;/i&gt; pilin antigenic variation. (PNAS 2026)

- DOI: 10.1073/pnas.2602688123 | PMCID: PMC13321361 | PMID: 42335229
- Evidence: The sequencing data were aligned with the pilE 1-81-S2 sequence as a reference genome using Hisat2 ( 66 ) and Samtools ( 67 ).
- Full pipeline: read trimming [Matplotlib, minimap2] -> alignment/mapping [SAMtools, minimap2] -> visualisation [Matplotlib]

### Ultrarapid MC1R protein and associated plumage color evolution in the domestic chicken. (PNAS 2026)

- DOI: 10.1073/pnas.2605288123 | PMCID: PMC13273276 | PMID: 42268884
- Version used: **1.9**
- Evidence: Resulting BAM files were sorted with SAMtools (version 1.9) ( 49 ), and PCR duplicates were marked/removed using Picard (version 2.18.6, https://broadinstitute.github.io/picard/ ) tools.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [BWA v0.7.17] -> registration [GATK v3.7] -> stage not stated [Picard v2.18.6, PyMOL, SAMtools v1.9, VCFtools v0.1.16]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Samtools ( 55 ) (version 1.11) suite was used to remove duplicate and incorrectly paired reads.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### Ancient DNA from shells reveals delayed genomic erosion and rapid immune adaptation in the critically endangered black abalone. (PNAS 2026)

- DOI: 10.1073/pnas.2600483123 | PMCID: PMC13229213 | PMID: 42207912
- Evidence: Pseudohaploid genotypes were called with SAMtools ( 97 ) v1.9 using mpileup -B -q25 -Q30 and pileupCaller from sequenceTools v1.5.2 ( https://github.com/stschiff/sequenceTools ) with the --randomHaploid and --singleStrandMode options, which allowed for excluding genotypes calls potentially originating from ancient DNA damage.
- Full pipeline: read trimming [fastp] -> variant calling [SAMtools] -> stage not stated [GATK, IQ-TREE, R]

### Meiosis-specific genes play roles in ploidy reduction in &lt;i&gt;Cryptococcus neoformans&lt;/i&gt; titan cells. (PNAS 2026)

- DOI: 10.1073/pnas.2522069123 | PMCID: PMC13215162 | PMID: 42189998
- Version used: **1.18**
- Evidence: Alignment files were processed using samtools (v1.18) ( 60 ) for sorting, indexing, and extracting unmapped reads.
- Full pipeline: alignment/mapping [SAMtools v1.18] -> visualisation [Matplotlib v3.5.3, NumPy v1.21.6, seaborn v0.12.2]

### Pneumococcal membrane particles promote serotype-independent cellular and humoral immunity and protect against pneumococcal colonization. (PNAS 2026)

- DOI: 10.1073/pnas.2537226123 | PMCID: PMC13214003 | PMID: 42154558
- Version used: **1.22**
- Evidence: Alignments were sorted and indexed using SAMtools v1.22 ( 45 ), and consensus sequences were generated using bcftools mpileup, bcftools call, and bcftools consensus v1.22 ( 46 ).
- Full pipeline: alignment/mapping [BCFtools, BWA v0.7.19, SAMtools v1.22] -> stage not stated [SPAdes v3.15.5]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: Reads were then indexed using samtools index ( 54 ) and duplicates removed using picard MarkDuplicates (version 2.9.0).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Evidence: Mapping statistics were generated with samtools idxstats (v1.9) ( 36 , 87 ).
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### Genome degradation in plant tissue culture. (PNAS 2026)

- DOI: 10.1073/pnas.2530182123 | PMCID: PMC13123843 | PMID: 42018421
- Version used: **1.13**
- Evidence: The resulting binary alignment map (BAM) files were sorted, duplicates were marked, and the files were indexed with SAMtools v1.13 ( 78 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39, minimap2 v2.17] -> alignment/mapping [MUSCLE, R, SAMtools v1.13, minimap2 v2.17] -> variant calling [DeepVariant v1.6.1, minimap2 v2.17] -> stage not stated [SnpEff v5.1d]

### WWOX maintains epidermal identity and suppresses EMT to prevent aggressive cutaneous squamous cell carcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2534844123 | PMCID: PMC13099603 | PMID: 41984841
- Evidence: BAM files were sorted, indexed, and filtered with SAMtools.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2, Trim Galore] -> quantification [deepTools] -> normalisation [deepTools] -> differential/statistical testing [DESeq2 v1.28.1, R] -> stage not stated [GSEA, SAMtools]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Evidence: Duplicates were removed twice, once before and once after merging the BAM files per sample, using SAMtools rmdup v1.21 ( 52 ).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Evidence: Alignment files were processed to remove unmapped reads, nonprimary alignment, or PCR duplicates using samtools ( 52 ).
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### Med14 phosphorylation shapes genomic response to GLP-1 agonists. (PNAS 2026)

- DOI: 10.1073/pnas.2536772123 | PMCID: PMC12974444 | PMID: 41779793
- Evidence: Mitochondrial, low quality mapped reads and duplicated reads were filtered out with samtools and peaks were called with macs2.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, Trim Galore] -> quantification [HOMER] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Version used: **1.19.2**
- Evidence: The aligned files were then indexed with SAMtools (v1.19.2), and gene expression levels were quantified using featureCounts.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### EPOP and MTF2 activate PRC2 activity through DNA-sequence specificity. (PNAS 2026)

- DOI: 10.1073/pnas.2527303123 | PMCID: PMC12890814 | PMID: 41650228
- Evidence: Reads of quality score less than 30 were removed using samtools and PCR duplicates were removed using picard.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [BEDTools, deepTools] -> normalisation [BEDTools, deepTools] -> visualisation [BEDTools, deepTools] -> stage not stated [ImageJ, MACS2, SAMtools]

### A factor integrating transcription and repression of surface antigen genes in African trypanosomes. (PNAS 2026)

- DOI: 10.1073/pnas.2531377123 | PMCID: PMC12890818 | PMID: 41632842
- Evidence: Reads were aligned to the predicted transcriptome using BWA-MEM with default settings, then filtered to only uniquely mapped reads using samtools view with the command line flags -q 10, -F 0x504 and -f 0x02.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [BLAST, ImageJ]

### The Japanese Archipelago sheltered cave lions, not tigers, during the Late Pleistocene. (PNAS 2026)

- DOI: 10.1073/pnas.2523901123 | PMCID: PMC12890994 | PMID: 41587328
- Version used: **1.11**
- Evidence: Mapped reads were processed with SAMtools v1.11 ( 79 ) to sort alignments, remove PCR duplicates, and filter out reads with mapping quality below 30.
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [ANGSD, BWA v0.7.17, SAMtools v1.11] -> stage not stated [MAFFT v7.505, Python]

### Domestication drives repeated evolution of sexual-asexual life cycle trade-offs in yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2526682123 | PMCID: PMC12798947 | PMID: 41505518
- Version used: **1.21**
- Evidence: Clean reads were aligned to the S. cerevisiae reference genome (R64-3-1) using bwa-mem2 (2.2.1) ( 49 ) and resulting BAM alignment files were sorted and indexed using samtools (1.21) ( 50 ).
- Full pipeline: read trimming [fastp v0.24.2] -> alignment/mapping [SAMtools v1.21] -> stage not stated [BCFtools v1.21, R, VCFtools]

### Early life-stage thermal resilience is determined by climate-linked regulatory variation. (PNAS 2026)

- DOI: 10.1073/pnas.2518358123 | PMCID: PMC12799179 | PMID: 41505517
- Version used: **1.10**
- Evidence: Calculations were done directly from the bam files outputted from the DEST pipeline and processed using samtools v1.10 ( 104 ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Salmon v0.14.1] -> quantification [Salmon v0.14.1] -> stage not stated [DESeq2, R, SAMtools v1.10]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: To assess enrichment of iCLIP reads mapping to each chromosome contigs, Samtools/idxstat was used to report alignment summary statistics of deduplicated reads.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **1.9**
- Evidence: Sequence analysis used Bowtie2 (2.4.1) ( 85 ), bcftools and samtools (1.9) ( 86 , 87 ), Geneious Prime (2021.0.3) ( 88 ), ivar (1.2.2) ( 89 ), and MAFFT (4.475) ( 90 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Evidence: For the alignment, the SARS-CoV-2 spike RBD reference was indexed using bowtie2-build (Version 2.4.1) and samtools (Version 1.10).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### Cortical wiring by synapse type-specific control of local protein synthesis. (Science 2022)

- DOI: 10.1126/science.abm7466 | PMCID: PMC7618116 | PMID: 36423280
- Evidence: Sequencing, data analysis, reads repartition, and insert size estimation were performed using FastQC, Picard-Tools, Samtools and rseqc.
- Full pipeline: quality control [FastQC, Picard, SAMtools] -> alignment/mapping [STAR v2.4.0] -> quantification [R v3.2] -> normalisation [R v3.2] -> differential/statistical testing [DESeq2, R v3.2] -> stage not stated [ImageJ]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Evidence: PCR duplicates and unmapped reads were filtered out using Samtools and Picard.
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **1.15.1**
- Evidence: Bowtie2 .sam output files were converted to .bam format, sorted and indexed with Samtools (v1.15.1) ( 112 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### The immunopathological landscape of human pre-TCRα deficiency: From rare to common variants. (Science 2024)

- DOI: 10.1126/science.adh4059 | PMCID: PMC10958617 | PMID: 38422122
- Version used: **1.14**
- Evidence: The aligned reads were converted to BAM format with samtools v1.14 and the triplicates were combined with the merge function and loaded onto the Integrated Genome Viewer for figure preparation ( 52 , 53 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, SAMtools v1.14] -> differential/statistical testing [R, tidyverse] -> visualisation [R, tidyverse] -> stage not stated [MACS2, Seurat v4.0.4, kallisto v0.46.1]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Evidence: Sequencing depth was estimated using the total number of properly mapped and paired reads (from samtools stats) multiplied by read length and divided by the whole genome length.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Next, reads were filtered using Markduplicates from Picard in addition to a quality score filtering of >20 via samtools( 59 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Version used: **1.13.0**
- Evidence: Resulting BAM files were merged, sorted and indexed with samtools (v1.13.0)( 72 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Evidence: VarScan2 output from SAMtools mpileup (minimum mapping quality = 20) was used to identify somatic variants between lesion and matched germline samples.
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: BAM files were filtered using samtools ( 78 ) -F 1804 -f 2 -q 30 to remove unmapped reads, secondary alignments, optical duplicates, and reads that failed platform or vendor quality checks or had low mapping quality.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Version used: **1.20**
- Evidence: Raw FASTQ files were aligned to hg38 using bwa (v0.7.18), BAM files were generated with samtools (v1.20), and bcftools mpileup was used to call ‘C’ and ‘T’ alleles at rs17834140.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

