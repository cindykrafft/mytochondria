# freebayes

- **Category:** genomics
- **Papers in survey:** 29
- **Journals:** PNAS (19), Nature (8), Cell (2)
- **Years:** 2021 (6), 2022 (5), 2023 (4), 2024 (4), 2025 (8), 2026 (2)
- **Versions named:** 1.3.1 (3), 1.1.0 (3), 1.3.2 (3), 1.2.0 (1), 1.0.2 (1), 1.3.6 (1), 1.3 (1), 1.1.0.46 (1)
- **Pipeline stages it appears in:** variant calling (15), alignment/mapping (6), registration (2), differential/statistical testing (2), dimensionality reduction/clustering (1), machine learning (1)

## Papers

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **1.1.0.46**
- Evidence: .../github.com/Illumina/strelka Mutect2 (gatk version 3.8) Cibulskis et al., 2013 https://gatk.broadinstitute.org/hc/en-us/articles/360037593851-Mutect2 freebayes (version 1.1.0.46) Garrison and Marth, 2012 https://github.com/freebayes/freebayes HaplotypeCaller (gatk version 3.8) DePristo et al., 2011 https://gatk.broadinstitute.org/hc/en-us/articles/360037225632-HaplotypeCaller Manta (version 1.6.0)...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Version used: **1.1.0**
- Evidence: 92 https://iupred2a.elte.hu/ PSIPRED Jones 93 http://bioinf.cs.ucl.ac.uk/psipred/ BWA-MEM 0.7.17-r1188 N/A https://github.com/lh3/bwa Picard tool 2.9.0 Broad Institute of MIT and Harvard https://broadinstitute.github.io/picard FreeBayes 1.1.0-3 N/A https://github.com/freebayes/freebayes isobarQuant Franken et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: In brief, variants from whole-genome sequencing data were called using four independent callers: GATK v3.8, FreeBayes, Strelka, and Platypus.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **1.1.0**
- Evidence: A Bayesian approach to variant analysis was performed using FreeBayes (v.1.1.0) 66 and haplogroups were identified by inputting the variant calling file into HaploGrep (v.2.1.21) 67 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: Later, for the VGP pipeline, we used FreeBayes 85 as Pilon 84 was not computationally scalable for large genomes with the updated Longranger 2.2.2.
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Evolutionary and biomedical insights from a marmoset diploid genome assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03535-x | PMCID: PMC8189906 | PMID: 33910227
- Version used: **1.3.1**
- Evidence: The parental haplotypes were then combined in a single assembly and underwent two rounds of short-read polishing using Long Ranger (v.2.2.2) 66 for short-read alignment and freebayes (v.1.3.1) 67 for polishing ( Supplementary Note ).
- Full pipeline: alignment/mapping [BCFtools, BWA, GATK, freebayes v1.3.1, minimap2] -> variant calling [GATK, freebayes v1.3.1]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: The main difference is that DipAsm used HiFi reads for SNP calling with DeepVariant and the Dovetail protocol used Omni-C reads (Hi-C1) for SNP calling with FreeBayes.
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **1.2.0**
- Evidence: The reads were realigned, first using bamleftalign from FreeBayes (v.1.2.0) 120 , and then with ABRA (v.2.23) 121 on target regions that were identified using RealignerTargetCreator from GATK (v.3.8.1) 122 and expanded by 160 nucleotides with bedtools slop (v.2.21.0) 123 .
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Compensatory evolution in NusG improves fitness of drug-resistant M. tuberculosis. (Nature 2024)

- DOI: 10.1038/s41586-024-07206-5 | PMCID: PMC10990936 | PMID: 38509362
- Version used: **1.3.1**
- Evidence: Variant detection was performed by Snippy (v4.6.0)/freebayes (v1.3.1).
- Full pipeline: variant calling [GATK v3.5, SAMtools v1.7] -> quantification [ImageJ] -> differential/statistical testing [Stan] -> stage not stated [RAxML v8.2.11, freebayes v1.3.1]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Variants were called using FreeBayes based on 1000 Genomes Project reference, and only informative heterozygous loci (≥5 cells with both reference and alternative alleles) were retained.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Accelerated expansion of pathogenic mitochondrial DNA heteroplasmies in Huntington's disease. (PNAS 2021)

- DOI: 10.1073/pnas.2014610118 | PMCID: PMC8325154 | PMID: 34301881
- Version used: **1.1.0**
- Evidence: Reads mapped to target regions were locally realigned by using freebayes (version 1.1.0) ( 72 ), and their base qualities were recalibrated by using samtools (version 1.6) ( 73 ).
- Full pipeline: alignment/mapping [SAMtools v1.6, freebayes v1.1.0] -> registration [SAMtools v1.6, freebayes v1.1.0] -> differential/statistical testing [R v3.5.0, lme4 v1.1] -> stage not stated [ANNOVAR, Picard]

### Integrated gene analyses of de novo variants from 46,612 trios with autism and developmental disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2203491119 | PMCID: PMC9674258 | PMID: 36350923
- Evidence: Family-level FreeBayes and GATK VCF files for SSC and SAGE samples are available at dbGaP (phs001874.v1.p1) ( 57 ) and also at SFARI Base (SFARI_SSC_WGS_2a).
- Full pipeline: dimensionality reduction/clustering [Seurat] -> differential/statistical testing [R v3.6.2] -> stage not stated [Cytoscape, GATK, STRING db, freebayes]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Version used: **1.3.2**
- Evidence: The SNP calling was done using FreeBayes (v.1.3.2) with -ploidy 1 ( 71 ) to identify sequence polymorphisms.
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Mutational background influences <i>P. aeruginosa</i> ciprofloxacin resistance evolution but preserves collateral sensitivity robustness. (PNAS 2022)

- DOI: 10.1073/pnas.2109370119 | PMCID: PMC9169633 | PMID: 35385351
- Evidence: Single-nucleotide polymorphism (SNPs) and small insertions and deletions (INDELs) were detected by using freebayes ( 72 ).
- Full pipeline: alignment/mapping [SAMtools] -> differential/statistical testing [R] -> stage not stated [GATK, Picard, SnpEff, freebayes]

### Epistatic genetic interactions govern morphogenesis during sexual reproduction and infection in a global human fungal pathogen. (PNAS 2022)

- DOI: 10.1073/pnas.2122293119 | PMCID: PMC8872808 | PMID: 35169080
- Evidence: Variant calling was carried out using the FreeBayes [v1.2.0 ( 88 )] haplotype caller, resulting in 114,223 unfiltered genetic variants, the majority of which are between the progenitor strains NIH12 and NIH433 ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [ImageJ, scikit-learn]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Evidence: FreeBayes-parallel was run on 10,000-bp subsets of the indexed reference genome using parameter “-C 10” to set a minimum of 10 observations per variant.
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Community interactions drive the evolution of antibiotic tolerance in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2209043119 | PMCID: PMC9934204 | PMID: 36634144
- Version used: **1.3.2**
- Evidence: To identify mutations and genetic variation in the sequenced samples, we used the Bayesian genetic variant detector FreeBayes v1.3.2 using the following settings: –ploidy 1 –haplotype-length 0 –min-alternate-count 1 –pooled-continuous .
- Full pipeline: read trimming [Trimmomatic v0.36] -> variant calling [freebayes v1.3.2] -> differential/statistical testing [freebayes v1.3.2]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: Variant calling was performed using freebayes, and the resulting variant call format (VCF) file was separated into three VCF files—one for each of the nuclear, mitochondrial, and plastid genomes ( 100 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Version used: **1.3.2**
- Evidence: Variants were first called from mapped Illumina reads with FreeBayes v1.3.2-dirty ( 107 ) in “naive” mode to verify ploidy (options: -g 400 --haplotype-length 0 --min-alternate-count 1 --min-alternate-fraction 0 --pooled-continuous), filtered with vcffilter from vcflib v1.0.0_rc2 ( 108 ) to retain variant calls with Phred quality score >20.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### The RPD3L deacetylation complex is required for facultative heterochromatin repression in &lt;i&gt;Neurospora crassa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2404770121 | PMCID: PMC11317574 | PMID: 39074265
- Evidence: Mapping of the critical mutations was performed as previously described ( 53 , 54 ) using FreeBayes and VCFtools ( 26 , 27 ).
- Full pipeline: alignment/mapping [VCFtools, freebayes] -> normalisation [R] -> dimensionality reduction/clustering [UMAP]

### Joubert syndrome 26 protein enforces compartmentalized motility of a ciliary kinesin. (PNAS 2025)

- DOI: 10.1073/pnas.2504374122 | PMCID: PMC12663925 | PMID: 41264249
- Version used: **1.3.6**
- Evidence: Variants were called (freebayes v1.3.6), annotated (SnpEff), and filtered (depth > 5, allele frequency>0.8) to minimize false positives.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [FastQC] -> stage not stated [AlphaFold, ImageJ, SnpEff, freebayes v1.3.6]

### Anthropocene genetic diversity loss in the marine tropics. (PNAS 2025)

- DOI: 10.1073/pnas.2513012122 | PMCID: PMC12646237 | PMID: 41231948
- Version used: **1.3.1**
- Evidence: Variants were called with FreeBayes v.1.3.1 ( 71 ).
- Full pipeline: quality control [VCFtools v0.1.14] -> alignment/mapping [SAMtools v1.9, SPAdes v3.15.3] -> dimensionality reduction/clustering [ADMIXTURE v1.3, PLINK v1.9] -> stage not stated [freebayes v1.3.1]

### Genetic regulation of the estrogen receptor and inherited predisposition to breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2517736122 | PMCID: PMC12582305 | PMID: 41129222
- Version used: **1.3**
- Evidence: To detect SNPs and indels, we integrated calls from GATK HaplotypeCaller ( 54 ) and from FreeBayes v1.3 ( 53 ).
- Full pipeline: variant calling [freebayes v1.3] -> registration [GATK, SAMtools v1.10]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: To assess whether additional genetic heterogeneity was present in cells marked with m.7076A > G, we split the full single-cell .bam file based on high-confidence cells with either the m.7076A or m.7076G allele and used FreeBayes ( 47 ) to genotype variants in the nuclear chromosomes using pseudobulk .bam files of the scATAC-seq profiles.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### Systemic in utero gene editing as a treatment for cystic fibrosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418731122 | PMCID: PMC12184489 | PMID: 40493185
- Evidence: Samples were analyzed as previously described using the variant caller FreeBayes on basepairtech.com ( 56 ).
- Full pipeline: variant calling [freebayes]

### Eradication efforts catalyze rapid evolution in an invasive predatory fish. (PNAS 2025)

- DOI: 10.1073/pnas.2424067122 | PMCID: PMC12184416 | PMID: 40489606
- Evidence: To call SNP genotypes, we first generated a filtered vcf file with freebayes ( 59 ) v.1.3.5 ( SI Appendix ), then selected only SNPs with quality > 20 and sum read depth > 400.
- Full pipeline: variant calling [freebayes] -> visualisation [R]

### Genomic analysis of 11,555 probands identifies 60 dominant congenital heart disease genes. (PNAS 2025)

- DOI: 10.1073/pnas.2420343122 | PMCID: PMC12002227 | PMID: 40127276
- Evidence: Variants were called using GATK v3.7 ( 72 ) using default parameters, disabling of variant quality score recalibration due to lack of training SNPs in the MIPseq panel; variants were also called with Freebayes v1.3.2 ( https://github.com/ekg/freebayes ) using default parameters.
- Full pipeline: alignment/mapping [ANNOVAR, BCFtools] -> variant calling [ANNOVAR, BCFtools] -> machine learning [GATK v3.7, freebayes]

### Genomics highlight an underestimation of phenology sensitivity to the urban heat island effect. (PNAS 2025)

- DOI: 10.1073/pnas.2408564122 | PMCID: PMC11962471 | PMID: 40100635
- Evidence: We called SNPs using freebayes, creating a master VCF (variant call format) file ( 42 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [PLINK, R]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **1.0.2**
- Evidence: Variant calling for 22 species using individual female resequencing data ( SI Appendix , Table S2 ) was carried out by aligning reads with BWA v0.7.18 ( 49 ), removing PCR duplicates with sambamba markdup v1.2.1 ( 50 ), and calling variants with FreeBayes v1.0.2 ( 51 ) with clustering disabled.
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

