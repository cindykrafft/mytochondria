# BCFtools

- **Category:** genomics
- **Papers in survey:** 202
- **Journals:** Nature (98), PNAS (86), Cell (13), Science (5)
- **Years:** 2021 (23), 2022 (25), 2023 (36), 2024 (41), 2025 (52), 2026 (25)
- **Versions named:** 1.9 (27), 1.10.2 (10), 1.13 (6), 1.11 (4), 1.8 (4), 1.14 (4), 1.21 (3), 1.15.1 (3), 1.20 (2), 1.17 (2)
- **Pipeline stages it appears in:** variant calling (65), alignment/mapping (42), normalisation (7), read trimming (6), quality control (5), differential/statistical testing (2), dimensionality reduction/clustering (2), registration (2), structure determination (1), quantification (1)

## Papers

### The genomic history of the Middle East. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.013 | PMCID: PMC8445022 | PMID: 34352227
- Version used: **1.9**
- Evidence: ...enetics/graphtyper plink v1.9 Chang et al., 2015 https://www.cog-genomics.org/plink/ covstats Pedersen et al., 2017 https://github.com/brentp/goleft/ bcftools v1.9 N/A https://samtools.github.io/bcftools/ CrossMap v0.4.2 Zhao et al., 2014 https://crossmap.readthedocs.io/en/latest/ BEAST v1.8.4 Drummond and Rambaut 2007 https://beast.community/2016-06-17_BEAST_v1.8.4_released.html RAxML v8.2.10 Sta...
- Full pipeline: stage not stated [ADMIXTURE, BCFtools v1.9, GATK v3.7, RAxML v8.2.10, SAMtools]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Version used: **1.4**
- Evidence: In order to determine the Y chromosome haplogroups bcftools v.
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: ...ryinference/ CircularMapper Peltzer et al., 2016 https://github.com/apeltzer/CircularMapper SAMtools Li et al., 2009 http://samtools.sourceforge.net/ BCFtools Li et al., 2009 http://samtools.github.io/bcftools/bcftools.html VCFtools Danecek et al., 2011 http://vcftools.sourceforge.net/ HaploGrep2 Weissensteiner et al., 2016 https://github.com/seppinho/haplogrep-cmd GATK McKenna et al., 2010 https:...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: The script was adapted from the ‘extract_variants_by_coordinate.sh’ script for germline variants ( https://research-help.genomicsengland.co.uk/display/GERE/Extract+variants+by+coordinate ) and was run on the command line within the Genomics England Research environment using bcftools ( https://samtools.github.io/bcftools/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Evidence: We used bcftools consensus ( Li, 2011 ) with parameter -H A using the rCRS reference sequence to generate an alignment of the sequences of all individuals.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **1.9**
- Evidence: ...mes Project Coriell Institute for Medical Research Data S1 Software and algorithms Absinthe github.com/nygenome/absinthe github.com/nygenome/absinthe BCFtools v1.9, 1.12, and v1.15 Li (2011) , Danecek et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...l., 2017 ) https://bitbucket.org/wegmannlab/atlas/ ATLAS-Pipeline, commit 6df90e7 Wegmann lab, Ilektra Schulz bitbucket.org/wegmannlab/atlas-pipeline bcftools versions: 1.9 and 0.1.15 ( Danecek et al., 2021 ) https://samtools.github.io/bcftools/howtos/index.html bwa - Burrows-Wheeler Alignment Tool - versions 0.7.15 and 0.7.17 ( Li, 2013 ) bio-bwa.sourceforge.net BEDOPS v2.4.40 ( Neph et al., 2012...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### A genetic history of the Balkans from Roman frontier to Slavic migrations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.10.018 | PMCID: PMC10752003 | PMID: 38065079
- Evidence: A consensus sequence was first determined using bcftools and SAMTools 60 using a majority rule and requiring a minimum coverage of two.
- Full pipeline: quality control [ANGSD] -> stage not stated [BCFtools]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Version used: **1.10.2**
- Evidence: Variants were called against the consensus of the respective sample using an in-house pipeline that leverages trimmomatic v.0.39, 123 bwa-mem v.0.7.17, 124 lofreq v.2.1.5, 125 and bcftools v.1.10.2.
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Loss of transient receptor potential channel 5 causes obesity and postpartum depression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.001 | PMCID: PMC11961024 | PMID: 38959890
- Evidence: Using bcftools 77 multi-allelic variants were split and left-normalised, and all variants filtered using a missingness based approach.
- Full pipeline: quantification [ImageJ] -> normalisation [BCFtools] -> stage not stated [VEP]

### Long shared haplotypes identify the southern Urals as a primary source for the 10th-century Hungarians. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.002 | PMCID: PMC12711333 | PMID: 41106360
- Evidence: A consensus for mitochondrial DNA was determined by using bcftools( 113 ) and SAMTools( 114 ).
- Full pipeline: dimensionality reduction/clustering [NetworkX] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools, R]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: For each cohort, all isolate breseq variant calls and missing data sites were merged into a single variant call file (VCF) with a single variant per row using bcftools .
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Evidence: 109 https://samtools.github.io/bcftools/ Winsfs v0.7.0 Rasmussen et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### The genomic origins of the Bronze Age Tarim Basin mummies. (Nature 2021)

- DOI: 10.1038/s41586-021-04052-7 | PMCID: PMC8580821 | PMID: 34707286
- Version used: **1.7**
- Evidence: For these SNPs, we called each individual’s genotype using bcftools v.1.7 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools v1.7] -> stage not stated [ADMIXTURE v1.3.0, PLINK v1.90]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: Consensus was called with bcftools consensus 92 with -i’QUAL>1 && (GT=’’AA’’ || GT = ‘’Aa’’)’ -Hla.
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Evolutionary and biomedical insights from a marmoset diploid genome assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03535-x | PMCID: PMC8189906 | PMID: 33910227
- Evidence: ....48 million SNVs); (2) GATK pipeline based on mapping of 10X linked-reads from the F 1 offspring (setB); and (3) SAMTools (v.1.8) mpileup followed by bcftools also based on 10X linked-reads mapping (setC).
- Full pipeline: alignment/mapping [BCFtools, BWA, GATK, freebayes v1.3.1, minimap2] -> variant calling [GATK, freebayes v1.3.1]

### Million-year-old DNA sheds light on the genomic history of mammoths. (Nature 2021)

- DOI: 10.1038/s41586-021-03224-9 | PMCID: PMC7116897 | PMID: 33597750
- Evidence: We ascertained heterozygous sites in three high-coverage genomes — E . maximus and M. primigenius (Oimyakon and Wrangel) 5 — using the SAMtools v.1.10 33 ‘mpileup’ command and bcftools.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.921, BCFtools, Picard, RepeatMasker v4.0.7, SAMtools v1.10]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Evidence: A consensus sequences of nucleic acids with a minimum whole-genome coverage of at least 20× were generated with BCFtools using a 0% majority threshold.
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: The resulting .vcf file was filtered using bcftools 88 using a minimum minor allele frequency of 0.1, and considering only insertions and deletions between 100 and 1,500 bp in length.
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### A genetic history of the pre-contact Caribbean. (Nature 2021)

- DOI: 10.1038/s41586-020-03053-2 | PMCID: PMC7864882 | PMID: 33361817
- Version used: **1.3.1**
- Evidence: We constructed a consensus sequence with samtools and bcftools version 1.3.1 using a majority rule and then determined the haplogroup with HaploGrep2, using Phylotree version 17.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard] -> structure determination [BWA v0.7.15] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.3.1, SAMtools]

### Genetic diversity fuels gene discovery for tobacco and alcohol use. (Nature 2022)

- DOI: 10.1038/s41586-022-05477-4 | PMCID: PMC9771818 | PMID: 36477530
- Evidence: URLs for software use BCFtools, http://samtools.github.io/bcftools/ ; BOLT-LMM, https://data.broadinstitute.org/alkesgroup/BOLT-LMM/ ; cov-LDSC, https://github.com/immunogenomics/cov-ldsc ; EAGLE, https://alkesgroup.broadinstitute.org/Eagle/ ; GCTA, http://cnsgenomics.com/software/gcta/ ; IMPUTE2, https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ; LDpred, https://github.com/bvilhjal/ldpred/ ; ...
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [BCFtools, GCTA, IMPUTE2, PLINK, SAMtools, SHAPEIT, VCFtools]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: We used bcftools 89 to make an mpileup and call a vcf file, using options for haploidy and disabling the default calling algorithm, which can slightly biases the calls towards the reference sequence, in favour of a majority call on bases that passed the default base quality cut-off of 13.
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Evidence: ... in the above dataset using GATK HaplotypeCaller (v3.6) 71 with the ‘-gt_mode GENOTYPE_GIVEN_ALLELES’ argument and then merged into the dataset using bcftools merge ( http://www.htslib.org/ ).
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **1.9**
- Evidence: To infer the phylogeny of the 432 accessions, reads were mapped to the DM v4 reference genome using BWA (0.7.5a-r405) 49 , and single-nucleotide polymorphisms (SNPs) were then extracted using SAMtools (v.1.9) 50 and BCFtools (v.1.9) 49 .
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Version used: **1.10.2**
- Evidence: Aggregation for the 100,000 Genomes Project cohort was performed using Illumina’s gvcfgenotyper v.2019.02.26, merged with bcftools v.1.10.2 and normalized with vt v.0.57721.
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Ancient DNA and deep population structure in sub-Saharan African foragers. (Nature 2022)

- DOI: 10.1038/s41586-022-04430-9 | PMCID: PMC8907066 | PMID: 35197631
- Evidence: We performed the calling using BCFtools/RoH 74 , which is able to accommodate unphased, relatively low-coverage data (at least for calling long ROH) and does not rely on a reference haplotype panel.
- Full pipeline: read trimming [BWA v0.6.1] -> alignment/mapping [BWA v0.6.1] -> variant calling [BCFtools]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Version used: **1.8**
- Evidence: The filtered VCF files were merged using BCFtools (1.8).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **1.10.2**
- Evidence: The intersection was performed using the bcftools (v.1.10.2) 77 isec function after normalizing variant calls and left-aligning ambiguous alignment gaps using the bcftools norm function.
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Omicron extensively but incompletely escapes Pfizer BNT162b2 neutralization. (Nature 2022)

- DOI: 10.1038/s41586-021-04387-1 | PMCID: PMC8866126 | PMID: 35016196
- Version used: **1.7**
- Evidence: We polished the initial assembly obtained from Genome Detective by aligning mapped reads to the reference sequences and filtering out low-quality mutations using the bcftools 1.7-2 mpileup method.
- Full pipeline: alignment/mapping [BCFtools v1.7]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Evidence: Runs of homozygosity The number of ROH segments greater than 1 megabase (Mb) and the sum of their length were estimated using bcftools roh 66 (v.1.11, default parameters) in the NCIG + PNG + high-coverage 1000 Genomes dataset (Fig.
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### The landscape of genomic structural variation in Indigenous Australians. (Nature 2023)

- DOI: 10.1038/s41586-023-06842-7 | PMCID: PMC10733147 | PMID: 38093003
- Evidence: Variants from clair3 and sniffles2 were incorporated in a haplotype-specific fashion into the local genome sequence using bcftools consensus (v.1.12) 53 , and the modified hap1/hap2 sequences were extracted in a ±50-bp window centred on the STR site; these constitute the consensus STR allele sequences for a given individual at a given STR site, with the larger being designated ‘allele_A’ and the s...
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools] -> visualisation [ggplot2] -> stage not stated [BEDTools, R, RepeatMasker v4.1.2, ape (R), vegan]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Version used: **1.31**
- Evidence: W created consensus sequences with samtools and bcftools version 1.31 using majority rule and then using HaploGrep2 with Phylotree version 17.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Genotyping, sequencing and analysis of 140,000 adults from Mexico City. (Nature 2023)

- DOI: 10.1038/s41586-023-06595-3 | PMCID: PMC10600010 | PMID: 37821707
- Evidence: Following completion of all jobs, we used bcftools merge to join the resulting dosage VCFs spanning all samples.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [REGENIE] -> stage not stated [BCFtools, DeepVariant v0.10.0, GATK, WhatsHap]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Evidence: We have constructed and released a mapping from our QC-pass UKB GRCh37 variants to GRCh38 coordinates, built using the bcftools +liftover tool ( https://github.com/freeseek/score ) with default parameters.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Evidence: Haplotype phasing and imputation After merging genotypes from AFB, EUB and ASH donors, we filtered genotypes for duplicates with bcftools norm --rm-dup all (v.1.16) 58 and lifted all genotypes over to the human genome assembly GRCh38 with GATK’s (v.4.1.2.0) LiftoverVcf using the RECOVER_SWAPPED_ALT_REF=TRUE option 59 .
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Version used: **1.9**
- Evidence: Trimmed high-quality reads from the two parents were aligned to the TA299 and TA10622 assemblies separately using SAMtools 69 (v.1.8) and variants were called using BCFtools (v.1.9) 70 .
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Early contact between late farming and pastoralist societies in southeastern Europe. (Nature 2023)

- DOI: 10.1038/s41586-023-06334-8 | PMCID: PMC10412445 | PMID: 37468624
- Evidence: We then determined genotype likelihoods from trimmed bam files using bcftools 89 with the 1,000G panel (The 1,000 Genomes Project consortium 90 ) as a reference.
- Full pipeline: quality control [ANGSD] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools v1.3]

### A pangenome reference of 36 Chinese populations. (Nature 2023)

- DOI: 10.1038/s41586-023-06173-7 | PMCID: PMC10322713 | PMID: 37316654
- Evidence: We grouped the alternative alleles in multiallelic SV sites by their length and split them into biallelic records using bcftools norm -m -any.
- Full pipeline: alignment/mapping [SAMtools, minimap2] -> variant calling [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BCFtools, QUAST v5.2.0, pheatmap v1.0.12]

### Northwest African Neolithic initiated by migrants from Iberia and Levant. (Nature 2023)

- DOI: 10.1038/s41586-023-06166-6 | PMCID: PMC10266975 | PMID: 37286608
- Evidence: We computed average sequencing depth (avg.DP) over all called positions for each individual and filtered for QUAL > 30 and a depth span from fivefold to 3× avg.DP per individual, using BCFtools view.
- Full pipeline: variant calling [GATK v3.5.0] -> registration [GATK v3.5.0] -> dimensionality reduction/clustering [ADMIXTURE, QGIS] -> stage not stated [BCFtools, PLINK v1.9, SAMtools]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Version used: **1.10.2**
- Evidence: For copy-number analysis, SNVs were jointly identified for all samples from each patient using bcftools (v.1.10.2; commands mpileup and call).
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: The variants were then filtered to include only the biallelic SNPs with a variant frequency higher than 0.3 and genotype quality higher than 10. bcftools view -Ov -f PASS -m2 -M2 -v snps -e ‘FORMAT/VAF < 0.3 || FORMAT/GQ < 10’ ${OUTPUT_VCF} > ${SNPS_VCF} Having the biallelic SNPs, we found the alignments with alternative alleles and removed them from the bam file.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **1.10.2**
- Evidence: After this first filtering step, BCFtools (v1.10.2) 88 was run to select only PASS biallelic SNVs.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: After genotyping, the cleaned read data are mapped using BWA to the relevant reference sequence (or sequences), and SNPs and small insertions and deletions are called using bcftool (version1.15.1, https://github.com/samtools/bcftools ) and a consensus sequence is generated also with bcftools, masking with Ns positions that do not have enough read support (15× by default).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **1.8**
- Evidence: The alignments were sorted using Novosort v3.06.05 ( http://www.novocraft.com ), and BCFtools v.1.8 was used to call SNPs and short indels.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Version used: **1.2**
- Evidence: In addition, we called variants with bcftools (version 1.2) 67 in the region of the candidate DNMs and removed the sites that appeared as false-positive calls (that is, at least one parent had the same variant as the offspring or the offspring had no variant).
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: Genotyping information was called using bcftools based on (sc)RNA-seq (B7, H1 and HES3) or DNA-seq data (H9 and 409B2) 25 , 55 or downloaded from the HipSci (WIBJ2, HOIK1) or Allen Institute (WTC) website.
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Version used: **1.9**
- Evidence: BCFtools (v.1.9) 69 was used to call SNPs and short indels.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### The rise and transformation of Bronze Age pastoralists in the Caucasus. (Nature 2024)

- DOI: 10.1038/s41586-024-08113-5 | PMCID: PMC11602729 | PMID: 39478221
- Evidence: Genotype likelihoods were determined from trimmed bam files (2 bp) using bcftools with the 1000 Genome Phase 3 release as a reference.
- Full pipeline: quality control [ANGSD, FastQC] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Version used: **1.13**
- Evidence: VCF files were left aligned and normalized, with splitting of multiallelic sites into several sites using bcftools v.1.13 (ref.
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Evidence: Single nucleotide polymorphisms were called using two different tools—Snippy and bcftools 64 .
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Genetic links between ovarian ageing, cancer risk and de novo mutation rates. (Nature 2024)

- DOI: 10.1038/s41586-024-07931-x | PMCID: PMC11410666 | PMID: 39261734
- Evidence: First, we processed population-level variant call format (VCF) files by splitting and left-correcting multi-allelic variants into separate alleles using ‘bcftools norm’ 69 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> differential/statistical testing [REGENIE v2.2.4, statsmodels] -> visualisation [pheatmap, tidyverse] -> stage not stated [R v4.1.2]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Version used: **1.9**
- Evidence: In brief, we used bcftools (v1.9) 67 to filter HGDP and 1KG variant data for designated genomic regions on chromosome 1, including the amylase SVR and flanking regions defined as bundle 0 and bundle 1 (distal and proximal, respectively) using the GRCh38 reference coordinate system (--region chromosome 1: 103,456,163–103,863,980 in GRCh38).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Evidence: Variants were called using BCFtools mpileup (v1.9) 63 with the setting “-C 60 -q 5 -Q 20”, and only SNPs were retained as variants.
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **1.14**
- Evidence: BCFtools 1.14 (ref.
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Version used: **1.9**
- Evidence: The mpileup function in bcftools (v.1.9) was used to count allele depths in the PoN.
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Evidence: Using bcftools 81 , these VCFs were then filtered for samples and variants observed from 67 individuals corresponding to PRO-cap samples from Gene Expression Omnibus (GEO) accession GSE110638 .
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### Repeated plague infections across six generations of Neolithic Farmers. (Nature 2024)

- DOI: 10.1038/s41586-024-07651-2 | PMCID: PMC11291285 | PMID: 38987589
- Evidence: To generate the phylogenetic tree we converted the vcf file to a multifasta using bcftools consensus, replacing missing data with N (flag: -M N) and filtering out regions with high proportions of reads of mapping quality zero (flag: -m [bedfile]; Supplementary Note 2 ).
- Full pipeline: read trimming [Bowtie2 v2.3.2] -> alignment/mapping [BCFtools, Bowtie2 v2.3.2, RAxML v0.9.0, SAMtools v1.12, minimap2 v2.17] -> variant calling [GATK] -> visualisation [R v4.2.2] -> stage not stated [BEDTools, Picard]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Evidence: Step 3: Merge all RIL groups to generate vcf files using the bcftools merge command.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: ...derthal and Denisovan F1 individual 105 , genotypes were called at the disease-associated chr21q22 candidate SNPs from the respective BAM files using bcftools mpileup with base and mapping quality options -q 20 -Q 20 -C 50 and using bcftools call -m -C alleles, specifying the two alleles expected at each site in a targets file (-T option).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **1.15.1**
- Evidence: The ‘PASS’ marked SNPs with genotypes of ‘1/1’ and ‘1/2’ were extracted, and the reference fasta files for GRCh38.p12 at these positions were replaced with ALT bases using the “bcftools consensus” command of bcftools (v.1.15.1) to make a F1/F2- AGVT custom genomic reference.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Network of large pedigrees reveals social practices of Avar communities. (Nature 2024)

- DOI: 10.1038/s41586-024-07312-4 | PMCID: PMC11078744 | PMID: 38658749
- Version used: **1.3**
- Evidence: We then used the integrated GLIMPSE_ligate and GLIMPSE_sample functions and bcftools v1.3 (refs.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [SAMtools v1.9] -> stage not stated [BCFtools v1.3, Cytoscape v3.9.1, Picard, igraph]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Version used: **1.5**
- Evidence: Genotype calling was performed using the bcftools v.1.5 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Version used: **1.16**
- Evidence: We processed the output data from the MoChA imputation workflow 58 , 59 using BCFtools (v.1.16) and the MoChA score (v.2022-12-21) 58 , 59 workflow ( https://github.com/freeseek/score ) to compute schizophrenia polygenic scores across all 2,413 imputed samples from the McLean cohort.
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### Population genomics of post-glacial western Eurasia. (Nature 2024)

- DOI: 10.1038/s41586-023-06865-0 | PMCID: PMC10781627 | PMID: 38200295
- Version used: **1.10**
- Evidence: We first generated genotype likelihoods at the biallelic 1000 Genomes variant sites from the bam files with bcftools v.1.10 and the command bcftools mpileup with parameters -I -E -a ‘FORMAT/DP’ --ignore-RG, followed by bcftools call -Aim -C alleles.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [GATK v3.3.0, Picard v1.127, SAMtools] -> variant calling [BCFtools v1.10] -> dimensionality reduction/clustering [ADMIXTURE, GCTA] -> stage not stated [BEDTools v2.23.0, R, RAxML, igraph]

### 100 ancient genomes show repeated population turnovers in Neolithic Denmark. (Nature 2024)

- DOI: 10.1038/s41586-023-06862-3 | PMCID: PMC10781617 | PMID: 38200294
- Evidence: We utilized a new computational method optimized for low-coverage data 21 , to impute genotypes based on genotype likelihoods of ancient individuals with the samtools/bcftools pipeline, and using the 1000 Genomes phased data 78 as a reference panel.
- Full pipeline: quality control [ADMIXTURE] -> variant calling [ADMIXTURE, BCFtools, PLINK, R, SAMtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [PLINK, R]

### A novel antibiotic class targeting the lipopolysaccharide transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06873-0 | PMCID: PMC10794144 | PMID: 38172634
- Evidence: Variant calling was performed using Freebayes (v.1.1.0) 46 followed by filtering using bcftools 47 to remove variants present in the corresponding parent strain and requiring a read depth >5 and a variant frequency >0.8.
- Full pipeline: read trimming [Pilon v1.23, Prokka v1.14.0, SPAdes v3.12, Trimmomatic v0.36] -> alignment/mapping [Pilon v1.23] -> variant calling [BCFtools] -> registration [minimap2 v2.17] -> stage not stated [Picard, SAMtools]

### GDF15 linked to maternal risk of nausea and vomiting during pregnancy. (Nature 2024)

- DOI: 10.1038/s41586-023-06921-9 | PMCID: PMC10808057 | PMID: 38092039
- Evidence: As homozygous reference alleles are not called by ‘HaplotypeCaller’, we used ‘mpileup’ command of samtools and bcftools to detect the read counts from the BAM files generated by the previous step.
- Full pipeline: alignment/mapping [GATK] -> variant calling [BCFtools, SAMtools] -> quantification [BCFtools, SAMtools, lme4] -> registration [Picard] -> stage not stated [PLINK v1.90b, R]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Version used: **1.13**
- Evidence: The VCF files generated by the pipeline were then normalized (left alignment of insertion–deletions and splitting multiallelic sites into multiple sites) using bcftools 1.13.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **1.18.1**
- Evidence: Low-quality genotypes (DP < 10 and GQ < 20) were set to missing using bcftools v.1.18.1 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### Somatic mutation and selection at population scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09584-w | PMCID: PMC12611758 | PMID: 41062696
- Evidence: We called SNPs with bcftools 61 using the following commands: bcftools mpileup --max-depth 20000 -Ou -f $genome $bam | bcftools call --ploidy GRCh37 -mv -Ob -o BCFTOOLS/$OUT_PREFIX.calls.bcf; bcftools view -i ‘%QUAL > = 100’ BCFTOOLS/$OUT_PREFIX.calls.bcf > BCFTOOLS/$OUT_PREFIX.calls.filtered.vcf.
- Full pipeline: alignment/mapping [MAFFT] -> variant calling [BEDTools, GATK] -> differential/statistical testing [lme4] -> stage not stated [BCFtools, R]

### Sperm sequencing reveals extensive positive selection in the male germline. (Nature 2025)

- DOI: 10.1038/s41586-025-09448-3 | PMCID: PMC12611766 | PMID: 41062690
- Evidence: This step involved calling germline variants from all targeted and exome samples using bcftools mpileup 69 at sites where there were >10 reads and a mutation call with VAF > 0.3.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [Bioconductor, ggplot2 v3.4.4, lme4] -> visualisation [R] -> stage not stated [BCFtools, Nextflow]

### A haplotype-based evolutionary history of barley domestication. (Nature 2025)

- DOI: 10.1038/s41586-025-09533-7 | PMCID: PMC12629985 | PMID: 40993384
- Version used: **1.15.1**
- Evidence: Variant calling was done with bcftools (v1.15.1) 49 using the command ‘mpileup -a DP,AD -q 20 -Q 20 --ns 3332’.
- Full pipeline: alignment/mapping [minimap2 v2.24] -> variant calling [BCFtools v1.15.1, DeepVariant v1.6.0, SnpEff v4.3t, minimap2 v2.24] -> visualisation [R v3.5.1] -> stage not stated [ADMIXTURE, PLINK, SAMtools v1.16.1]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Version used: **1.15.1**
- Evidence: Consensus sequences for 5,856 single-copy orthologue genes (BUSCO genes) were extracted from vcf files using bcftools (v.1.15.1) consensus 74 , with heterozygous position treated as missing data.
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Parent-of-origin effects on complex traits in up to 236,781 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-09357-5 | PMCID: PMC12527933 | PMID: 40770099
- Version used: **1.8**
- Evidence: We then used the UK Biobank SNPs quality control file (UK Biobank resource 1955) to filter the data using BCFtools (v1.8) to keep only variants used for the official phasing of the original UK Biobank data release 39 , resulting in 670,741 variant sites across the 22 autosomes and 16,601 variant sites on the X chromosome.
- Full pipeline: quality control [BCFtools v1.8] -> variant calling [PLINK v1.90b] -> dimensionality reduction/clustering [igraph] -> stage not stated [R, REGENIE v3.2.9]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: We first genotyped all SNPs from the short-read haplotype reference panel with an allele count greater than or equal to 6 in all samples using bcftools 67 .
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Evidence: We used the resulting reference panel to reconstruct personal genomes for all 3,202 individuals by implanting phased variants into the CHM13 reference genome with BCFtools 93 to create the 6,404 consensus haplotype sequences of all 1kGP individuals ( Supplementary Methods ).
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **1.9**
- Evidence: BCFtools (v1.9) 59 was used to call SNPs.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Whole-genome ancestry of an Old Kingdom Egyptian. (Nature 2025)

- DOI: 10.1038/s41586-025-09195-5 | PMCID: PMC12367555 | PMID: 40604286
- Version used: **1.19**
- Evidence: First, we called genotypes using bcftools v.1.19 (ref.
- Full pipeline: quality control [ANGSD v0.933] -> variant calling [BCFtools v1.19] -> dimensionality reduction/clustering [ADMIXTURE v1.2] -> stage not stated [PLINK v1.9]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Version used: **1.9**
- Evidence: SNPs were called with the filtered alignments by bcftools (v.1.9) 112 .
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Per-autosome vcf files were concatenated into a single file for each assembly using bcftools 65 and then processed with vcfbub --max-ref-length 100000 --max-level 0 to flatten nested variants and remove those >100 kb in length 20 (see 16csatAsms_pggbByChrom_<assembly>.vcf.gz and 16csatAsms_pggbByOriginalChrom_<assembly>.vcf.gz for vcfs from graphs generated with consistent- and mixed-orientation i...
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Therefore, variants were initially called independently with three pipelines: BCFtools 88 , Varscan 89 and GATK 87 .
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Results were also confirmed using the bcftools method 50 on the full merged pseudobulk snATAC-seq data with standard settings.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Picuris Pueblo oral history and genomics reveal continuity in US Southwest. (Nature 2025)

- DOI: 10.1038/s41586-025-08791-9 | PMCID: PMC12137115 | PMID: 40307544
- Version used: **1.17**
- Evidence: Y-chromosome analysis Genotypes for positions located in the single-copy short-read callable 10-Mb region of the Y-chromosome 110 were called using bcftools v.1.17 mpileup, excluding triallelic locus, indels and variants called in less than 95% frequency in the locus.
- Full pipeline: quality control [ANGSD v0.931] -> variant calling [BCFtools v1.17] -> stage not stated [ADMIXTURE, BEAST v2.6, Picard v2.25.0, SAMtools v1.3.1]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: TRGT was run using the default parameters: trgt --threads 32 --genome {in_reference} --repeats {in_bed} --reads {in_bam} --output-prefix {out_prefix} --karyotype {karyotype}`bcftools sort -m 3072M -Ob -o {out_prefix}.sorted.vcf.gz {out_prefix}.vcf.gzbcftools index --threads 4 {out_prefix}.sorted.vcf.gzsamtools sort -@ 8 -o {out_prefix}.spanning.sorted.bam {out_prefix}.spanning.bamsamtools index -@...
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### Punic people were genetically diverse with almost no Levantine ancestors. (Nature 2025)

- DOI: 10.1038/s41586-025-08913-3 | PMCID: PMC12226237 | PMID: 40269169
- Evidence: We built a mitochondrial DNA consensus sequence using bcftools ( https://github.com/samtools/bcftools ) and SAMTools 49 , only analyzing sites with a minimum of two-fold coverage and determining allelic status by majority rule.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK, R, SAMtools]

### Translational genomics of osteoarthritis in 1,962,069 individuals. (Nature 2025)

- DOI: 10.1038/s41586-025-08771-z | PMCID: PMC12119359 | PMID: 40205036
- Version used: **1.13**
- Evidence: Code availability Analyses were conducted using publicly available software: BCFtools v.1.13 ( https://samtools.github.io/bcftools/bcftools.html ), CrossMap v.0.5.4 ( https://crossmap.readthedocs.io/en/latest/ ), EasyQC v.23.8, 5 June 2020 ( https://www.uni-regensburg.de/medizin/epidemiologie-praeventivmedizin/genetische-epidemiologie/softwssare ), GWAMA v.2.2.2 ( https://genomics.ut.ee/en/tools )...
- Full pipeline: quality control [BCFtools v1.13, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [Enrichr, GCTA, PLINK]

### A genomic history of the North Pontic Region from the Neolithic to the Bronze Age. (Nature 2025)

- DOI: 10.1038/s41586-024-08372-2 | PMCID: PMC11909631 | PMID: 39910299
- Evidence: We determined a consensus sequence for mitochondrial DNA using bcftools ( https://github.com/samtools/bcftools ) and SAMtools 59 requiring a minimum of 2-fold coverage to call the nucleotide and a majority rule to determine its value.
- Full pipeline: quality control [ANGSD] -> stage not stated [ADMIXTURE, BCFtools, SAMtools]

### The genetic origin of the Indo-Europeans. (Nature 2025)

- DOI: 10.1038/s41586-024-08531-5 | PMCID: PMC11922553 | PMID: 39910300
- Evidence: We determined a consensus for mitochondrial DNA using bcftools ( https://github.com/samtools/bcftools ) and SAMTools 85 , requiring a minimum of 2-fold coverage to call the nucleotide and a majority rule to determine its value.
- Full pipeline: quality control [ANGSD] -> stage not stated [BCFtools, SAMtools]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Evidence: We then corrected base errors using bcftools consensus v.1.12 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Leveraging a phased pangenome for haplotype design of hybrid potato. (Nature 2025)

- DOI: 10.1038/s41586-024-08476-9 | PMCID: PMC11981936 | PMID: 39843749
- Version used: **1.13**
- Evidence: For SNPs and indels, we merged the output of assembly-based variation calling from SyRI using BCFtools (v.1.13) 98 .
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, StringTie v2.2.1, minimap2 v2.17] -> variant calling [BEDTools v2.30.0, HISAT2 v2.2.1, StringTie v2.2.1, WhatsHap v1.1, ggplot2, hifiasm] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, ggplot2] -> visualisation [R v4.2.0, ggplot2] -> stage not stated [AUGUSTUS v3.4.0, BCFtools v1.13, BUSCO v5.4.4, IQ-TREE v2.0.6, InterProScan v5.34, RepeatMasker, SAMtools v1.17]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Version used: **1.10.2**
- Evidence: Variants were called using BCFtools (v1.10.2) 70 , and the resulting VCF (variant call format) file was inputted into HaploGrep2 (ref.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### High-resolution genomic history of early medieval Europe. (Nature 2025)

- DOI: 10.1038/s41586-024-08275-2 | PMCID: PMC11693606 | PMID: 39743601
- Evidence: Imputation of ancient genomes We follow the recommended pipeline of GLIMPSE 73 and first call genotype likelihoods for each genome in the 1000GP, segregating sites using bcftools mpileup with filter -q 20, -Q 20 and -C 50.
- Full pipeline: variant calling [BCFtools]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Version used: **1.21**
- Evidence: Diploid genotypes were called using bcftools (v.1.21), and for the analysis of IBD segment sharing, missing diploid genotypes were imputed using GLIMPSE 84 (for samples with a minimum autosomal genome coverage of 0.1×) following the approach in ref.
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: Variants were called using HaplotypeCaller tool, and SNP filtering was performed with bcftools 75 (v.1.10.2) using stringent criteria: QD < 2.0||FS > 60.0||MQ < 40.0||MQRankSum < −12.5||ReadPosRankSum < −8.0||SOR > 3.0.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### Dynamics of genetic and somatic trade-offs in ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10407-9 | PMCID: PMC13253337 | PMID: 42020758
- Evidence: Variant calling We called short sequence variants using bcftools 82 in three steps: (1) we created text pileup output for all BAM files using mpileup with mapping quality of 30 or greater; (2) we called using default settings; (3) we removed variants with a read depth of less than 100 across all samples or a QUAL score of less than 100.
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.3.4.1] -> variant calling [BCFtools, R v4.0] -> dimensionality reduction/clustering [PLINK, TwoSampleMR v0.6.2, clusterProfiler] -> stage not stated [SAMtools v1.6]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: In detail, for each sample we used bcftools mpileup (v1.13) 260 to generate genotype likelihoods for all variants (SNPs and indels).
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **1.10.2**
- Evidence: The view and norm functions in bcftools (v.1.10.2) were applied to process each VCF file.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **1.20**
- Evidence: For evaluating the SV callset, HWE P values were calculated for SV alleles using the fill-tags plugin in BCFtools (v.1.20) 70 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **1.9**
- Evidence: To select sites that captured dynamics of population structure, we selected putatively neutral and unlinked variants using bcftools (v.1.9) 101 with the following filtering parameters: invariant sites and sites with strand bias in variant-supporting reads (>90%) were removed.
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Version used: **1.11**
- Evidence: Various bam file processing operations were performed using Samtools/htslib/bcftools (v1.11).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Evidence: Variants were filtered using BCFtools in Samtools (v.1.18) 82 with the following criteria: quality score > 30, filtered read depth > 4, variant type = ‘SNP’, minimum and maximum allowed alleles = 2 and homozygous genotypes across all samples.
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Ancestry and somatic profile indicate acral melanoma origin and prognosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09967-z | PMCID: PMC12960246 | PMID: 41708869
- Version used: **1.9**
- Evidence: VCF handling was done using bcftools v.1.9 (ref.
- Full pipeline: quality control [GATK v4.2.3.0, SAMtools v1.9] -> variant calling [Mutect2] -> normalisation [DESeq2 v1.48.1, R, limma v3.64.1] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [ADMIXTURE, BCFtools v1.9, CNVkit, HTSeq, PLINK v1.9]

### Lasting Lower Rhine-Meuse forager ancestry shaped Bell Beaker expansion. (Nature 2026)

- DOI: 10.1038/s41586-026-10111-8 | PMCID: PMC12978843 | PMID: 41673154
- Evidence: Haplogroup assignment of uniparentally inherited markers: We created consensus mitochondrial haplotypes with samtools and bcftools.
- Full pipeline: quality control [ANGSD] -> variant calling [BCFtools, SAMtools]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Evidence: ...er.com/jp/en/home/life-science/microarray-analysis/microarray-analysis-partners-programs/affymetrix-developers-network/affymetrix-power-tools.html ), BCFtools/liftover ( https://github.com/freeseek/score ), Transanno v.0.4.5 ( https://github.com/informationsea/transanno ).
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Mutations were called from the duplicate-marked BAM files using samtools ‘mpileup’ and subsequently processed with bcftools 64 to generate a single VCF file 65 containing mutations identified in the WT and mutant genomes.
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Version used: **1.17**
- Evidence: 69 ) with default parameters, and genotypes were called using bcftools (v.1.17; ref.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **1.13**
- Evidence: Reads were aligned to the C. elegans genome (WBcel235/ce11) using BWA-MEM (v.0.7.17-r1188), and variants were identified using Samtools (v.1.3.1) and bcftools (v.1.13).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Gene-drive-capable mosquitoes suppress patient-derived malaria in Tanzania. (Nature 2026)

- DOI: 10.1038/s41586-025-09685-6 | PMCID: PMC12779567 | PMID: 41372414
- Evidence: Genetic variants were called and consensus sequences for each of the four genes assayed in each sample were generated with BCFtools 46 .
- Full pipeline: alignment/mapping [BWA, Bioconductor, Cutadapt] -> stage not stated [BCFtools, ImageJ]

### Homo sapiens-specific evolution unveiled by ancient southern African genomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09811-4 | PMCID: PMC12872451 | PMID: 41339558
- Evidence: All of the sample VCF files, on a per-chromosome basis, were then merged and annotated using dbSNP v.142 using bcftools annotate 80 .
- Full pipeline: stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK v1.9, SAMtools, SnpEff]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Version used: **1.9**
- Evidence: Variant call format (VCF) files were processed with bcftools (v.1.9).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: The resulting mapping files from the PanOat assemblies and the G.O.D. were merged into a VCF file using bcftools mpileup 58 with filtering for Q40 or larger and a minimum of 50% missing data per position or SNP.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Version used: **1.9**
- Evidence: Subsequently, variant calling was performed with the mpileup and call commands in BCFtools v1.9 ( 52 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### Genome evolution in an agricultural pest following adoption of transgenic crops. (PNAS 2021)

- DOI: 10.1073/pnas.2020853118 | PMCID: PMC8719884 | PMID: 34930832
- Evidence: SNP genotypes were called with BCFtools ( 95 ), and SNP filtering criteria are provided in SI Appendix .
- Full pipeline: alignment/mapping [GEMMA v0.98.4, R] -> variant calling [BCFtools] -> differential/statistical testing [GEMMA v0.98.4] -> stage not stated [Bowtie2]

### High frequency of an otherwise rare phenotype in a small and isolated tiger population. (PNAS 2021)

- DOI: 10.1073/pnas.2025273118 | PMCID: PMC8488692 | PMID: 34518374
- Evidence: We aligned the retained reads to the reference Bengal Tiger Genome (BenTig1.0, NCBI accession: JAHFZI000000000 ) using BWA-MEM ( 98 ) with a mismatch penalty value of 3 and called variants using bcftools ( 99 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [BCFtools, BWA] -> variant calling [GATK, VCFtools] -> stage not stated [Picard]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Version used: **1.9**
- Evidence: The alignments from each sample were sorted and indexed using NovoSort and used for variant calling using SAMtools/BCFtools version 1.9 ( 42 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: After rescaling quality scores of nucleotide variants in the reads originating from postmortem deamination processes with mapDamage, variant calling was performed with samtools and bcftools.
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Herded and hunted goat genomes from the dawn of domestication in the Zagros Mountains. (PNAS 2021)

- DOI: 10.1073/pnas.2100901118 | PMCID: PMC8237664 | PMID: 34099576
- Version used: **1.5**
- Evidence: For long ROH (≥5 Mb), we followed an observation-based approach by calculating the rate of transversion heterozygous sites in 500-kbp nonoverlapping windows using bcftools v1.5, downsampling genomes to 2X to control for varying coverage.
- Full pipeline: alignment/mapping [MUSCLE] -> registration [MUSCLE] -> differential/statistical testing [ANGSD] -> stage not stated [BCFtools v1.5, BEAST]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Evidence: BAM files were used for calling SNPs with the bcftools option call -v -m from SAMtools (1.8) ( 66 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### Nonparametric coalescent inference of mutation spectrum history and demography. (PNAS 2021)

- DOI: 10.1073/pnas.2013798118 | PMCID: PMC8166128 | PMID: 34016747
- Evidence: We generated k -SFS data for each 1KG population using mutyper ( 80 , 81 ) and BCFtools ( 82 , 83 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [BCFtools, Jupyter, Nextflow, Python]

### A versatile platform for locus-scale genome rewriting and verification. (PNAS 2021)

- DOI: 10.1073/pnas.2023952118 | PMCID: PMC7958457 | PMID: 33649239
- Version used: **1.9**
- Evidence: Variant calling was performed on sequenced BL6xCAST samples to verify correct allele-specific engineering using a standard pipeline based on bcftools v1.9: bcftools mpileup–redo-BAQ–adjust-MQ 50–gap-frac 0.05–max-depth 10000–max-idepth 200000 -a DP,AD–output-type u | bcftools call–keep-alts –ploidy 1–multiallelic-caller -f GQ–output-type u Raw pileups were filtered using: bcftools norm–check-ref w...
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: For each individual, we extracted the OR gene region from the gVCF and generated a consensus sequence defaulting to the reference allele at variable site using bcftools ( 107 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Prediction of Alzheimer's disease-specific phospholipase c gamma-1 SNV by deep learning-based approach for high-throughput screening. (PNAS 2021)

- DOI: 10.1073/pnas.2011250118 | PMCID: PMC7826347 | PMID: 33397809
- Version used: **1.3**
- Evidence: We performed SNV calls using the SAMtools (v.1.3) and bcftools (v.1.3) with bam files from two samples (WT and 5xFAD cortex).
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [ANNOVAR, BCFtools v1.3, Cufflinks]

### Identification and functional validation of super-enhancers in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2215328119 | PMCID: PMC9860255 | PMID: 36409894
- Evidence: InDels were identified using BCFtools ( 80 , 81 ) with parameters “-Q 0 -B -A -F 0 -m 0” for “bcftools mpileup” and “-cv –p 1” for “bcftools call”.
- Full pipeline: alignment/mapping [BWA, SAMtools, minimap2] -> stage not stated [BCFtools, BEDTools, R v4.0.4]

### Recurrent emergence of <i>Klebsiella pneumoniae</i> carbapenem resistance mediated by an inhibitory <i>ompK36</i> mRNA secondary structure. (PNAS 2022)

- DOI: 10.1073/pnas.2203593119 | PMCID: PMC9499542 | PMID: 36095213
- Version used: **0.1.19**
- Evidence: A pipeline comprising SAMtools mpileup v0.1.19 ( 40 ) and BCFtools v0.1.19 was used to call SNPs and generate a pseudogenome alignment.
- Full pipeline: alignment/mapping [BCFtools v0.1.19, BLAST v2.6.0, MUSCLE v3.8, SAMtools] -> stage not stated [Prokka v1.14.5, SPAdes v3.9.0]

### Additive genetic effects in interacting species jointly determine the outcome of caterpillar herbivory. (PNAS 2022)

- DOI: 10.1073/pnas.2206052119 | PMCID: PMC9456756 | PMID: 36037349
- Version used: **1.9**
- Evidence: We then aligned the DNA sequences to the M. sativa or L. melissa genome and identified SNPs using samtools (versions 1.10), bcftools (version 1.9), and GATK (version 4.1) ( 61 , 62 ) ( SI Appendix , DNA Sequence Alignment and Variant Calling ).
- Full pipeline: alignment/mapping [BCFtools v1.9, GATK v4.1, SAMtools] -> variant calling [BCFtools v1.9, GATK v4.1, SAMtools]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Evidence: Locus VCF files were then concatenated using BCFtools concat (v.1.10.2) and haplotypes were disassembled with vt (v.0.5772) ( 70 , 72 ) to dissociate indels from multiple-nucleotide variants.
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Genetic variation that determines &lt;i&gt;TAPBP&lt;/i&gt; expression levels associates with the course of malaria in an HLA allotype-dependent manner. (PNAS 2022)

- DOI: 10.1073/pnas.2205498119 | PMCID: PMC9303992 | PMID: 35858344
- Version used: **1.9**
- Evidence: The trimmed mean of M-values normalization method, as implemented in the R package edgeR, was used for normalization, and genotypes at SNP positions were determined by using the bcftools (v1.9) mpileup function with sorted binary alignment map files of RNA-sequencing (RNA-Seq) reads aligned to the human reference genome as input ( 50 , 51 ).
- Full pipeline: read trimming [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, Trimmomatic v0.33, edgeR] -> alignment/mapping [BCFtools v1.9, HISAT2 v2.1.0, HTSeq v0.6.1, R, edgeR] -> variant calling [BCFtools v1.9, R, edgeR] -> normalisation [BCFtools v1.9, R, edgeR]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Version used: **1.11**
- Evidence: We also retained invariant sites with QUAL ≥ 20 using bcftools v.1.11-95 ( 79 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### Targeted base editing in the mitochondrial genome of <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121177119 | PMCID: PMC9171795 | PMID: 35561225
- Evidence: SNPs were then called using samtools mpileup command (-uf -d 50000 -L 2000) and bcftools call command [-m -A -P 0.1 ( 46 )].
- Full pipeline: alignment/mapping [BWA v0.7.12] -> stage not stated [BCFtools, SAMtools]

### Estimating bonobo (<i>Pan</i><i>paniscus</i>) and chimpanzee (<i>Pan</i><i>troglodytes</i>) evolutionary history from nucleotide site patterns. (PNAS 2022)

- DOI: 10.1073/pnas.2200858119 | PMCID: PMC9170072 | PMID: 35452306
- Evidence: We used bcftools ( 75 ) to perform further variant filtering and provide the command line inputs in parentheses.
- Full pipeline: visualisation [ggplot2 v3.3.3] -> stage not stated [BCFtools, Conda, Jupyter, Snakemake]

### rDNA array length is a major determinant of replicative lifespan in budding yeast. (PNAS 2022)

- DOI: 10.1073/pnas.2119593119 | PMCID: PMC9169770 | PMID: 35394872
- Evidence: Sequence variations were called using the bcftools software package.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, SAMtools] -> stage not stated [BCFtools]

### Layered evolution of gene expression in "superfast" muscles for courtship. (PNAS 2022)

- DOI: 10.1073/pnas.2119671119 | PMCID: PMC9168950 | PMID: 35363565
- Evidence: Reference genome read alignments were converted to VCF files using BCFtools ( 45 ).
- Full pipeline: alignment/mapping [BCFtools, BWA, RAxML, STAR v2.7.3a] -> differential/statistical testing [limma] -> stage not stated [featureCounts v2.0.1]

### An in-frame deletion mutation in the degron tail of auxin coreceptor <i>IAA2</i> confers resistance to the herbicide 2,4-D in <i>Sisymbrium orientale</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2105819119 | PMCID: PMC8892348 | PMID: 35217601
- Evidence: The command “bcftools” was used to retain only SNPs that had a quality score higher than 10 and read depth higher than 10.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [SAMtools] -> differential/statistical testing [R v3.3, edgeR] -> stage not stated [BCFtools, BUSCO]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Version used: **1.9**
- Evidence: We used mpileup in SAMtools v1.6 ( 39 ) and call in bcftools v1.9 ( 42 ) to call SNPs and a customized R script to filter for high-confidence SNPs of interest (see Data Accessibility ) as follows.
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: After removing all Serranus samples, the SNPs only dataset was filtered to exclude sites with linkage disequilibrium coefficients greater than 0.5 within 50-kb windows using the BCFtools ( 97 ) plug-in prune (git 17.1 to 17.4).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### A polygenic explanation for Haldane's rule in butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2300959120 | PMCID: PMC10622916 | PMID: 37856563
- Evidence: We used BCFtools-1.9 ( 51 ) to pile up reads with very light quality filtering and called variants with associated genotype likelihoods.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [BCFtools] -> stage not stated [Picard]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Evidence: The SNPs were identified using GATK (The Genome Analysis Toolkit, version 3.8.1) ( 81 ) and bcftools (Tools for manipulating Variant Call Format and Binary Variant Call Format, version 1.15.1).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### Changes in parrot diversity after human arrival to the Caribbean. (PNAS 2023)

- DOI: 10.1073/pnas.2301128120 | PMCID: PMC10576146 | PMID: 37748079
- Version used: **1.12**
- Evidence: 1.10 (-C 30; -Q 20) to produce a VCF file in bcftools v.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BWA v0.7.13, IQ-TREE v2.1.2, SAMtools v1.10] -> stage not stated [BCFtools v1.12, MAFFT v7.455, R v4.1]

### Inducible CRISPR-targeted "knockdown" of human gut <i>Bacteroides</i> in gnotobiotic mice discloses glycan utilization strategies. (PNAS 2023)

- DOI: 10.1073/pnas.2311422120 | PMCID: PMC10523453 | PMID: 37733741
- Version used: **1.12**
- Evidence: These alignments were then processed (bcftools, v1.12, ref.
- Full pipeline: alignment/mapping [BCFtools v1.12] -> quantification [DESeq2] -> differential/statistical testing [DESeq2]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **1.9**
- Evidence: Finally, linkage equilibrium among SNPs was estimated using BCFtools 1.9 ( 85 ), and one SNP was removed from all SNP pairs with r 2 > 0.5 in a genomic window of 5 Kbp.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: To generate the phylogenies, we first merged the VCF files of the isolates in each group (L1, L2, L3, L4A, L4B, L4C, L5, L6) with bcftools ( 60 ) using only SNPs detected within the VCF files.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Natural genetic variation in the pheromone production of <i>C. elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2221150120 | PMCID: PMC10293855 | PMID: 37339205
- Evidence: We used BCFtools ( 45 ) to filter variants below a 5% minor allele frequency and variants with missing genotypes and used PLINK v1.9 ( 46 , 47 ) to prune genotypes using LD.
- Full pipeline: alignment/mapping [minimap2] -> variant calling [BCFtools, PLINK v1.9] -> stage not stated [GCTA, R, SnpEff]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: Then, viral sequences of each sample were extracted using BCFtools ( 29 ).
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Complex evolutionary processes maintain an ancient chromosomal inversion. (PNAS 2023)

- DOI: 10.1073/pnas.2300673120 | PMCID: PMC10288594 | PMID: 37311002
- Version used: **1.6**
- Evidence: Next, we used samtools (version 1.5) and bcftools (version 1.6) for variant calling ( 67 ).
- Full pipeline: alignment/mapping [RepeatMasker v4.0.7, SAMtools v1.5] -> variant calling [BCFtools v1.6] -> stage not stated [BEAST v2.6.6, BUSCO v4.0.5, R v4.0.2]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Version used: **1.10.2**
- Evidence: We used bcftools v1.10.2 ( 38 ) to exclude calls with mapping quality or base quality scores <20.
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Version used: **1.9**
- Evidence: The resulting SNP data were filtered for biallelic sites using BCFtools v1.9 ( 94 ).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Version used: **1.10**
- Evidence: Polymorphic sites were called using bcftools v1.10 software and were annotated using SNPeff v4 software ( 56 ).
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Evidence: We filtered the SNPs with the following criteria: QD < 2.0 || FS > 60.0 || MQRankSum < -12.5 || RedPosRankSum < -8.0 || SOR > 3.0 || MQ < 40.0, and used the biallelic SNPs (bcftools -m2 -M2) to screen for sex-linked variants.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Divergent sensory and immune gene evolution in sea turtles with contrasting demographic and life histories. (PNAS 2023)

- DOI: 10.1073/pnas.2201076120 | PMCID: PMC9962930 | PMID: 36749728
- Evidence: We used SAMtools ( 134 ) and BCFtools ( 135 ) to call genotypes with base and mapping quality filters of >Q30, before filtering for insert size (50 to 5,000bp) and allele balance (AB), and retaining only biallelic sites with an AB of <0.25 and >0.75.
- Full pipeline: alignment/mapping [BCFtools, SAMtools] -> variant calling [BCFtools, GATK, SAMtools] -> stage not stated [ANGSD, BUSCO, OrthoFinder, PLINK]

### Resurrection genomics provides molecular and phenotypic evidence of rapid adaptation to salinization in a keystone aquatic species. (PNAS 2023)

- DOI: 10.1073/pnas.2217276120 | PMCID: PMC9963159 | PMID: 36730191
- Evidence: We called variants using the bcftools mpileup and call pipeline using all individuals together ( 79 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools, BEDTools, SAMtools, VEP]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: To subset the vcf file by municipality (San Juan, Arecibo, and Mayagüez), we used bcftools ( 95 ).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Community-engaged ancient DNA project reveals diverse origins of 18th-century African descendants in Charleston, South Carolina. (PNAS 2023)

- DOI: 10.1073/pnas.2201620120 | PMCID: PMC9934026 | PMID: 36623185
- Version used: **1.9**
- Evidence: Variants were called using BCFtools v1.9 ( 71 ) specifying for haploid ploidy and filtered for quality (>30) and depth (>5) using RTG tools v3.10.1 vcffilter.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.9] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Evidence: After indel realignment, SNP calling was performed using BCFTtools mpileup , computing genotype likelihoods based on alignments with a minimum mapping quality of 5 (−q 5), followed by BCFtools call to identify SNPs from the pileup output and generate VCFs ( 114 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Evidence: Genotype imputation was performed for each resulting chromosome chunk using GLIMPSE_phase and the resulting VCF files for each chunk combined using Glimpse_ligate , with all imputed loci having genotype probabilities lower than 0.9 set to missing using the BCFtools plugin ( 69 ).
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### Fitness consequences of structural variation inferred from a House Finch pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2409943121 | PMCID: PMC11588099 | PMID: 39531493
- Evidence: Variants were called from the graphs using tools vg ( 113 ), vcfwave ( 114 ), vcflib ( 114 ), and bcftools ( 115 ).
- Full pipeline: variant calling [BUSCO, hifiasm] -> stage not stated [BCFtools, PLINK, RepeatMasker]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: BCFtools was used to call SNPs and generate a VCF file for each sample using the “mpileup” command followed by the “call” command with the multiallelic flag (-m) ( 101 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **1.11**
- Evidence: VCF files were processed (e.g., merging, indexing) with bcftools v1.11 ( 104 ).
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Version used: **1.6**
- Evidence: We restricted calls to biallelic sites using BCFtools v1.6 ( 70 ), and subsequently filtered for quality, missingness, and depth.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Large-scale genome sequencing of giant pandas improves the understanding of population structure and future conservation initiatives. (PNAS 2024)

- DOI: 10.1073/pnas.2406343121 | PMCID: PMC11388402 | PMID: 39186654
- Version used: **1.11**
- Evidence: We applied BCFtools (v1.11) ( 64 ) statistics to obtain the summary information of variants for each population and the whole population.
- Full pipeline: read trimming [GATK, Trimmomatic v0.33.0] -> alignment/mapping [GATK] -> variant calling [GATK] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0, GCTA, PLINK v1.9, clusterProfiler] -> differential/statistical testing [BCFtools v1.11] -> stage not stated [ANNOVAR, IQ-TREE v1.6.12, R v4.1.2, SnpEff v4.3, VCFtools v0.1.16]

### A genome-guided strategy for climate resilience in American chestnut restoration populations. (PNAS 2024)

- DOI: 10.1073/pnas.2403505121 | PMCID: PMC11287244 | PMID: 39012830
- Evidence: Finally, BCFtools was used to remove INDELs, multiallelic SNPs, and sites with high missingness (>10% missing data) ( 27 ).
- Full pipeline: variant calling [Picard] -> differential/statistical testing [Matplotlib, Python] -> stage not stated [ADMIXTURE, BCFtools, GATK, PLINK v1.9, R, SAMtools, SnpEff, vegan]

### Rapid vertebrate speciation via isolation, bottlenecks, and drift. (PNAS 2024)

- DOI: 10.1073/pnas.2320040121 | PMCID: PMC11145251 | PMID: 38771882
- Evidence: Population structure was evaluated using PCAngsd ( 61 ), NGSadmix ( 62 ), and runs of homozygosity were identified using bcftools ( 63 ).
- Full pipeline: stage not stated [BCFtools]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Version used: **1.14**
- Evidence: We prepared PSMC input files by creating a consensus diploid sequence for each sample (i.e., a single representative individual from each country-level population with >18× coverage) using a pipeline combining SAMtools v1.14 ( 89 ), Picard v2.26.10, and BCFtools v1.14.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Mapping seasonal migration in a songbird hybrid zone -- heritability, genetic correlations, and genomic patterns linked to speciation. (PNAS 2024)

- DOI: 10.1073/pnas.2313442121 | PMCID: PMC11067064 | PMID: 38648483
- Evidence: We used bcftools to provide STITCH with an initial set of SNPs ( 89 ) (--min-BQ 20, --min-MQ 20, %QUAL>500, --skip-variants indels).
- Full pipeline: alignment/mapping [BUSCO, GATK] -> variant calling [GATK] -> stage not stated [BCFtools, GEMMA, PLINK v1.9b, R, SAMtools, SnpEff v5.1d, VCFtools]

### Cross-pollination in seed-blended refuge and selection for Vip3A resistance in a lepidopteran pest as detected by genomic monitoring. (PNAS 2024)

- DOI: 10.1073/pnas.2319838121 | PMCID: PMC10990109 | PMID: 38513093
- Evidence: 1.0, PRJNA767434], variant calling with bcftools [( 89 ), v.
- Full pipeline: variant calling [BCFtools] -> stage not stated [ImageJ, R, VCFtools]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Evidence: To remove potential host contamination in the DFTD SNP set (i.e., obtain a set of tumor-specific somatic mutations), tumor SNPs were further filtered using BCFtools isec ( 82 ) to remove any SNPs common to both the devil and tumor VCF files.
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Evidence: We first surveyed average depth and percent missing data across all individuals and scaffolds using the BCFtools ( 94 ) stat function and custom R scripts.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### Frequent horizontal chromosome transfer between asexual fungal insect pathogens. (PNAS 2024)

- DOI: 10.1073/pnas.2316284121 | PMCID: PMC10945790 | PMID: 38442176
- Evidence: Comparison between published short reads as well as the 150 PE Illumina reads generated in this study and the R3-I4 and the R1-A and R3-A assembly was determined by mapping and SNP calling using bowtie2 (version 2.4.4) ( 63 ) and bcftools mpileup (version = 1.14) ( 64 ).
- Full pipeline: alignment/mapping [BCFtools, Bowtie2 v2.4.4] -> variant calling [BCFtools, Bowtie2 v2.4.4] -> differential/statistical testing [R v3.6.0] -> stage not stated [WhatsHap v1.6]

### Environmental radiation exposure at Chornobyl has not systematically affected the genomes or chemical mutagen tolerance phenotypes of local worms. (PNAS 2024)

- DOI: 10.1073/pnas.2314793121 | PMCID: PMC10945782 | PMID: 38442158
- Version used: **1.14**
- Evidence: Genetic distances were generated by selecting two strains at a time, filtering them for only sites in which both samples had a read depth >5, and counting the fraction of sites that differed between the pair using bcftools v1.14 ( 53 ) (bcftools view -s strain1, strain2 -m 2 -M 2 -i ‘MIN(FMT/DP)>5’).
- Full pipeline: alignment/mapping [GATK v4.3.0.0, R, SAMtools v1.11, VCFtools v0.1.16, minimap2] -> variant calling [GATK v4.3.0.0] -> stage not stated [BCFtools v1.14, Flye v2.8.1, ImageJ]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Version used: **1.10.2**
- Evidence: We filtered single-nucleotide polymorphisms (SNPs) using bcftools (v1.10.2), GATK VariantFiltration (v4.2.6.1), and plink (v1.90), retaining only biallelic SNPs and discarding those with quality less than 30, quality per depth less than 2, Fisher strand ratio greater than 60, and strand odds ratio greater than three.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### The genome of the black-footed cat: Revealing a rich natural history and urgent conservation priorities for small felids. (PNAS 2024)

- DOI: 10.1073/pnas.2310763120 | PMCID: PMC10786289 | PMID: 38165928
- Version used: **1.1**
- Evidence: (sand cat, European wildcat, Chinese mountain cat, Asian wildcat, and African wildcat) were mapped to those of their close relative with a high-quality assembly genome, the domestic cat (GCF_018350175.1) with the bwa mem algorithm ( 64 ) and samtools/bcftools (v1.1) ( 65 ) with its consensus algorithm, to generate five consensus genomes.
- Full pipeline: quality control [fastp v0.20.1] -> alignment/mapping [BCFtools v1.1, RAxML v8.2.12, SAMtools] -> quantification [VCFtools v0.1.16] -> stage not stated [ANGSD, AUGUSTUS v3.2.3, BUSCO, Flye v2.8.1, RepeatMasker v1.0.11, SnpEff v5.0, eggNOG, minimap2]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Version used: **1.9**
- Evidence: Variant calling was performed with Mutect2 (GATK version 4.2.0.0), and consensus sequences were generated using bcftools version 1.9.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### The impacts of European arrival on Australian dingoes. (PNAS 2025)

- DOI: 10.1073/pnas.2421749122 | PMCID: PMC12684890 | PMID: 41284893
- Version used: **1.9**
- Evidence: We then used bcftools v.1.9 ( 73 ) to merge our nonmodern (n = 21) and modern (n = 33) genomes with publicly available genomes of purebred (n = 115) and village (n = 67) dogs, Australian (n = 11) and New Guinean (n = 17) dingoes, and a coyote for a final dataset of 266 canids ( SI Appendix , Table S1 C ).
- Full pipeline: read trimming [SAMtools v1.9] -> alignment/mapping [SAMtools v1.9] -> differential/statistical testing [ADMIXTURE v1.3.0] -> stage not stated [BCFtools v1.9, BEDTools, IQ-TREE v2.1.4, PLINK v1.90b, R, VCFtools]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: Specifically, we implemented the multiallelic caller within bcftools mpileup and bcftools call v1.9 ( 78 ) to output only variants at sites with a minimum base quality and mapping quality of 30.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### A species interaction kick-starts ecological speciation in allopatry. (PNAS 2025)

- DOI: 10.1073/pnas.2506625122 | PMCID: PMC12557528 | PMID: 41082661
- Evidence: Raw variants were then filtered using bcftools and vcftools to retain only biallelic autosomal SNPs, thus excluding variants on the known sex chromosomes chrY and chrXIX, as well as those on chrM (mitochondrial genome) and chrUn (unassembled scaffolds).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [BCFtools, GATK, SAMtools, VCFtools, lme4]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: We further characterized population divides identified in Admixture and PCA by calculating the number of shared versus private SNPs among groups using BCFtools ( 95 ), pairwise F ST using VCFtools, and the rate of rare variant sharing among groups using VCFtools and PLINK.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Version used: **1.16**
- Evidence: To parallel the genotype calling process, we generated genomic databases in ~3 Mb intervals across the genome and combined and indexed the genotyped VCF files with BCFtools 1.16 ( 70 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Factors underlying a latitudinal gradient in the S/G lignin monomer ratio in natural poplar variants. (PNAS 2025)

- DOI: 10.1073/pnas.2503491122 | PMCID: PMC12403099 | PMID: 40833412
- Evidence: SNPs and InDels were called using SAMtools/BCFtools and annotated with SnpEff.
- Full pipeline: dimensionality reduction/clustering [R, WGCNA] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BCFtools, SAMtools, SnpEff]

### Inbreeding reduces fitness in spatially structured populations of a threatened rattlesnake. (PNAS 2025)

- DOI: 10.1073/pnas.2501745122 | PMCID: PMC12403008 | PMID: 40825128
- Version used: **1.9.64**
- Evidence: We filtered SNPs using bcftools v.1.9.64 ( 66 ) to retain SNPs with more than seven reads in 90% of individuals and with genotype quality scores greater than 19 in 90% of individuals.
- Full pipeline: alignment/mapping [BWA v07.17, SAMtools v1.9] -> variant calling [BCFtools v1.9.64] -> stage not stated [R]

### A genomic test of sex-biased dispersal in white sharks. (PNAS 2025)

- DOI: 10.1073/pnas.2507931122 | PMCID: PMC12358869 | PMID: 40758892
- Version used: **1.9**
- Evidence: Following the tutorial of PSMC ( https://github.com/lh3/psmc ), the consensus sequence of each individual was produced on the masked genome with the “mpileup” command of BCFtools 1.9 ( 58 , 59 ) with the -c flag.
- Full pipeline: read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> variant calling [GATK v4.0] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools v1.9, PLINK]

### Synthesis of large single-transcript pathways from oligonucleotide pools: Design of STARBURST, an autobioluminescent reporter. (PNAS 2025)

- DOI: 10.1073/pnas.2508109122 | PMCID: PMC12337302 | PMID: 40729380
- Evidence: Briefly, it uses minibar ( 46 ) to demultiplex reads, chopper ( 47 ) to remove low-quality reads, minimap2 ( 48 ) to map reads to reference sequences, and samtools ( 49 ), bcftools ( 49 ), bedtools ( 50 ), racon ( 51 ), medaka ( 52 ), seqtk ( 53 ), emboss ( 54 ), and parallel ( 55 ) to generate consensus sequences, annotate variants, and output summaries.
- Full pipeline: read trimming [BCFtools, BEDTools, SAMtools, minimap2]

### A trans-species cytoplasmic polymorphism is associated with seed shape and aridity across multiple species of sunflowers. (PNAS 2025)

- DOI: 10.1073/pnas.2410943122 | PMCID: PMC12337292 | PMID: 40720659
- Version used: **1.10.2**
- Evidence: Variants were then called using samtools (v1.10) mpileup and bcftools (v1.10.2) call assuming a haploid state for individual samples for the entire cytoplasmic genome, and then merged together into a single VCF ( 87 ).
- Full pipeline: read trimming [Trimmomatic v0.22] -> alignment/mapping [Trimmomatic v0.22] -> variant calling [GATK] -> stage not stated [BCFtools v1.10.2, IQ-TREE, SAMtools v1.10]

### A population genetic analysis of the nematode &lt;i&gt;Strongyloides stercoralis&lt;/i&gt; in Asia shows that human infection is not a zoonosis from dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2424630122 | PMCID: PMC12304889 | PMID: 40663613
- Evidence: For Bangladesh, Cambodia, Thailand, Fiji, Myanmar, and Japan iL3 from QC-passed sequence data we detected SNPs compared to the S. stercoralis reference genome using BCFtools with the recommended multiallelic calling option.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, Bowtie2] -> stage not stated [ADMIXTURE]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Version used: **1.14**
- Evidence: Variants were then called using mpileup from bcftools (version 1.14) ( 93 ) with the final output being a variant call file (vcf) for each sample.
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Version used: **1.8**
- Evidence: We then genotyped variants on all the modern genomes using bcftools v1.8 ( 78 ).
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### An ancient origin of the naked grains of maize. (PNAS 2025)

- DOI: 10.1073/pnas.2503748122 | PMCID: PMC12207465 | PMID: 40526715
- Version used: **1.13**
- Evidence: We treated the major allele across the 26 outgroup samples taxa as the ancestral state at each SNP and made an ancestral reference genome with bcftools version 1.13 ( 91 ) “consensus” command.
- Full pipeline: alignment/mapping [BCFtools v1.13] -> variant calling [R v4.4.2, SAMtools v1.13, VCFtools v0.1.13] -> dimensionality reduction/clustering [R v4.4.2] -> visualisation [R v4.4.2]

### Deep origins, distinct adaptations, and species-level status indicated for a glacial relict seal. (PNAS 2025)

- DOI: 10.1073/pnas.2503368122 | PMCID: PMC12207470 | PMID: 40493204
- Version used: **1.9**
- Evidence: Sites within 1 Mbp windows were extracted with BCFtools (v.1.9) ( 89 ), excluding positions with missing data and leaving 0.5 Mbp gaps between adjacent windows.
- Full pipeline: dimensionality reduction/clustering [ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, RAxML v8.2.12, VCFtools]

### Organellar genome divergence and environmental stress induce transcriptional cytonuclear responses in wheat alloplasmic hybrids. (PNAS 2025)

- DOI: 10.1073/pnas.2424424122 | PMCID: PMC12184502 | PMID: 40489605
- Evidence: Nuclear SNPs were identified with bcftools based on the IWGSC reference v2.1( 16 ).
- Full pipeline: stage not stated [BCFtools]

### Natural dispersal is better than translocation for reducing risks of inbreeding depression in eastern black rhinoceros (&lt;i&gt;Diceros bicornis michaeli&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2414412122 | PMCID: PMC12167989 | PMID: 40460127
- Evidence: In order to avoid confounding missing genotypes with monomorphic sites in estimation of pairwise nucleotide diversity (pi), an all site vcf was called using the bcftools call –m –Oz –f GQ as described in the pixy manual ( 59 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [SAMtools] -> variant calling [BCFtools] -> differential/statistical testing [emmeans] -> stage not stated [ADMIXTURE, PLINK v1.9, R, VCFtools]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: Variants were called and filtered using BCFtools (V.1.10.2) ( 53 ) and VCFtools (V.0.1.16) ( 54 ) respectively.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### Genomic analysis of 11,555 probands identifies 60 dominant congenital heart disease genes. (PNAS 2025)

- DOI: 10.1073/pnas.2420343122 | PMCID: PMC12002227 | PMID: 40127276
- Evidence: The union of these variant calls was annotated using ANNOVAR ( 73 ), multiallelic sites were split with BCFtools ( 74 ), and insertion-deletion variants were left-aligned with BCFtools ( SI Appendix ).
- Full pipeline: alignment/mapping [ANNOVAR, BCFtools] -> variant calling [ANNOVAR, BCFtools] -> machine learning [GATK v3.7, freebayes]

### Estimating realized relatedness in free-ranging macaques by inferring identity-by-descent segments. (PNAS 2025)

- DOI: 10.1073/pnas.2401106122 | PMCID: PMC11760927 | PMID: 39808663
- Version used: **1.9**
- Evidence: To genotype the five high-depth samples, we used bcftools v1.9 ( 86 ) to call genotypes at 23,874,572 predefined variant sites from the mGAP 2.4 reference panel ( 56 ) with both minimum base call and minimum mapping quality set to 30.
- Full pipeline: quality control [Cutadapt, HISAT2] -> read trimming [Cutadapt, HISAT2] -> alignment/mapping [BCFtools v1.9, Cutadapt, HISAT2] -> variant calling [BCFtools v1.9] -> simulation/modelling [R v4.4] -> stage not stated [Picard]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Version used: **1.18**
- Evidence: We then identified SNPs in our samples using bcftools v1.18 ( 139 ) and filtered variants using vcftools v0.1.16 ( 140 ) with the following parameters: minor allele frequency of 0.05, minimum depth of 10×, minimum average quality of 40, and a maximum variant missing of 0.995.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### Pneumococcal membrane particles promote serotype-independent cellular and humoral immunity and protect against pneumococcal colonization. (PNAS 2026)

- DOI: 10.1073/pnas.2537226123 | PMCID: PMC13214003 | PMID: 42154558
- Evidence: Alignments were sorted and indexed using SAMtools v1.22 ( 45 ), and consensus sequences were generated using bcftools mpileup, bcftools call, and bcftools consensus v1.22 ( 46 ).
- Full pipeline: alignment/mapping [BCFtools, BWA v0.7.19, SAMtools v1.22] -> stage not stated [SPAdes v3.15.5]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Evidence: SNP calling on mapped mRNAseq reads was conducted using bcftools ( 94 ) across all samples.
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **1.20**
- Evidence: Variant calling was done using BCFtools v1.20 mpileup and call ( 72 ), applying a minimum mapping and base quality of 30, and disabling probabilistic realignment (-q 30, -Q 30, -B).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### Domestication drives repeated evolution of sexual-asexual life cycle trade-offs in yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2526682123 | PMCID: PMC12798947 | PMID: 41505518
- Version used: **1.21**
- Evidence: Duplicated reads were flagged and variants were called using bcftools (1.21) with a fixed ploidy of 1( --ploidy ).
- Full pipeline: read trimming [fastp v0.24.2] -> alignment/mapping [SAMtools v1.21] -> stage not stated [BCFtools v1.21, R, VCFtools]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **1.21**
- Evidence: Briefly, variants were called as described above, and high-quality biallelic SNPs were filtered with VCFtools v0.1.16 and bcftools v1.21 ( 56 ).
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Evidence: Sequence analysis used Bowtie2 (2.4.1) ( 85 ), bcftools and samtools (1.9) ( 86 , 87 ), Geneious Prime (2021.0.3) ( 88 ), ivar (1.2.2) ( 89 ), and MAFFT (4.475) ( 90 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: The PCA for data heterogeneity was performed with the R FactoMineR package and the following individual sequence quality parameters calculated with bcftools stats: number of alleles, number of ALT alleles, number of heterozygous variants, Ts/Tv ratio, number of indels, mean depth of coverage, number of singletons, and number of missing genotypes.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Functional maps of a genomic locus reveal confinement of an enhancer by its target gene. (Science 2025)

- DOI: 10.1126/science.ads6552 | PMCID: PMC7618358 | PMID: 40966339
- Version used: **1.9**
- Evidence: To construct the 129S1/CAST genome, mouse strain-specific variants were obtained from the Mouse Genomes Project ( 42 ), homozygous SNPs were filtered using SnpSift v4.3p ( 46 )), and bcftools v1.9 ( 47 ) was used to insert single nucleotide variants into the GRCm38/mm10 mouse genome obtained from the Ensembl database.
- Full pipeline: alignment/mapping [BWA] -> quantification [deepTools v3.0] -> normalisation [deepTools v3.0] -> visualisation [Signac] -> stage not stated [BCFtools v1.9, MACS2, SnpEff v4.3p]

### Introgression dynamics of sex-linked chromosomal inversions shape the Malawi cichlid radiation. (Science 2025)

- DOI: 10.1126/science.adr9961 | PMCID: PMC7617772 | PMID: 40504893
- Evidence: We aligned all sequencing data to the A. calliptera reference genome (fAstCal1.2; RefSeq: GCF_900246225.1) using BWA-MEM ( 79 ) and called variants according to the bcftools paradigm ( 80 ).
- Full pipeline: quality control [SnpEff] -> alignment/mapping [BCFtools, BWA] -> differential/statistical testing [ANGSD, GEMMA]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Evidence: Raw FASTQ files were aligned to hg38 using bwa (v0.7.18), BAM files were generated with samtools (v1.20), and bcftools mpileup was used to call ‘C’ and ‘T’ alleles at rs17834140.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

