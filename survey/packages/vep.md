# VEP

- **Category:** genomics
- **Papers in survey:** 75
- **Journals:** Nature (42), PNAS (29), Science (2), Cell (2)
- **Years:** 2021 (6), 2022 (12), 2023 (14), 2024 (13), 2025 (18), 2026 (12)
- **Versions named:** 93.2 (2), 94.5 (1), 103.0 (1), 98.2 (1)
- **Pipeline stages it appears in:** variant calling (3), normalisation (1)

## Papers

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Evidence: (2019) https://github.com/hall-lab/svtools Variant Effect Predictor (VEP) v104 McLaren et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### Loss of transient receptor potential channel 5 causes obesity and postpartum depression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.001 | PMCID: PMC11961024 | PMID: 38959890
- Evidence: 26 Variants were annotated using Ensembl VEP v96 with GRCh37 human reference.
- Full pipeline: quantification [ImageJ] -> normalisation [BCFtools] -> stage not stated [VEP]

### Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. (Nature 2021)

- DOI: 10.1038/s41586-021-03205-y | PMCID: PMC7875770 | PMID: 33568819
- Evidence: Identifying pLOF variants pLOF variants were identified using Loss Of Function Transcript Effect Estimator (LOFTEE) v.0.3-beta 85 and Variant Effect Predictor (VEP) v.94 86 .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> stage not stated [BWA, Docker, GATK v3.5.0, R, SAMtools, VEP]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **93.2**
- Evidence: 33 , 83 were filtered with the Variant Effect Predictor v93.2 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: Saturation at methylated CpG sites For each potential CpG>TpG at a methylated site, we assessed its most significant potential consequence with Variant Effect Predictor 68 v.
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### A joint NCBI and EMBL-EBI transcript set for clinical genomics and research. (Nature 2022)

- DOI: 10.1038/s41586-022-04558-8 | PMCID: PMC9007741 | PMID: 35388217
- Evidence: Source data We collaborated with resources such as ExAC/gnomAD, ClinGen, ClinVar, DECIPHER and the Ensembl Variant Effect Predictor (VEP) 17 , all of which had different preferred transcripts, to encourage adoption of the MANE Select set, achieve standardization and ensure consistency.
- Full pipeline: stage not stated [HISAT2 v2.1, HOMER, VEP]

### Whole-genome sequencing reveals host factors underlying critical COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-04576-6 | PMCID: PMC9259496 | PMID: 35255492
- Evidence: Gene name annotation indicates genes that are affected by the predicted worst consequence type of each lead variant (annotation by Variant Effect Predictor (VEP)).
- Full pipeline: quality control [SAIGE] -> variant calling [BCFtools v1.10.2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [LDSC, REGENIE, SAIGE] -> machine learning [R] -> stage not stated [COLOC, GCTA, METAL, PLINK v1.9, VEP]

### Mapping clustered mutations in cancer reveals APOBEC3 mutagenesis of ecDNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04398-6 | PMCID: PMC8850194 | PMID: 35140399
- Evidence: The predicted effect of each overlapping variant was determined using ENSEMBL’s Variant Effect Predictor tool by reporting only the most severe consequence 59 .
- Full pipeline: stage not stated [VEP]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Somatic variants were annotated using Ensembl Variant Effect Predictor (version 87) 52 , 53 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: Variant Effect Predictor 68 was used to annotate the effect of a variant using the humdiv database, and picking one consequence (or transcript) per variant according to a criterion that includes the canonical status of the transcript, APPRIS isoform annotation, transcript support level, biotype of transcript (‘protein_coding’ preferred) and consequence rank preferring high impact.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Plasma proteomic associations with genetics and health in the UK Biobank. (Nature 2023)

- DOI: 10.1038/s41586-023-06592-6 | PMCID: PMC10567551 | PMID: 37794186
- Evidence: Variant annotation Annotation was performed using Ensembl Variant Effect Predictor (VEP), WGS Annotator (WGSA) and UCSC Genome Browser’s variant annotation integrator ( http://genome.ucsc.edu/cgi-bin/hgVai ).
- Full pipeline: machine learning [R] -> stage not stated [PLINK, REGENIE v2.2.1, VEP]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Evidence: ...oadgsa/gatk ), Picard tools (v1.117, https://broadinstitute.github.io/picard ), Bedtools (v2.25.0-76-g5e7c696z, https://github.com/arq5x/bedtools2 ), Variant Effect Predictor (release 100, https://github.com/Ensembl/ensembl-vep ), BOLT-LMM (v2.1, https://data.broadinstitute.org/alkesgroup/BOLT-LMM/downloads ), IMPUTE2 (v2.3.1, https://mathgen.stats.ox.ac.uk/impute/impute_v2.html ), dbSNP (v140, ht...
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Evidence: For all sites, a minimum coverage threshold of 100 was used to distinguish between homoplasmic reference calls and sites without variant calls due to low variant calling confidence as done previously 21 . mtDNA variants were annotated using the Variant Effect Predictor v.101 (ref.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Extrachromosomal DNA in the cancerous transformation of Barrett's oesophagus. (Nature 2023)

- DOI: 10.1038/s41586-023-05937-5 | PMCID: PMC10132967 | PMID: 37046089
- Evidence: 55 ) and Variant Effect Predictor v.78 (ref.
- Full pipeline: alignment/mapping [BWA] -> registration [GATK] -> differential/statistical testing [SciPy v1.9.1] -> stage not stated [Strelka v2.0.15, VEP]

### Tracking early lung cancer metastatic dissemination in TRACERx using ctDNA. (Nature 2023)

- DOI: 10.1038/s41586-023-05776-4 | PMCID: PMC7614605 | PMID: 37055640
- Version used: **94.5**
- Evidence: ... contained the same TNC-group error rate as the true MRD variant it is replacing, it was not a known population SNP variant as dictated by Ensemble's Variant Effect Predictor version 94.5, had a error-corrected coverage delta no more than 2,000 compared with the true MRD variant, and was not used within any other mock tumour signature, including itself.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R] -> differential/statistical testing [lme4 v3.1, survival (R) v0.4.9] -> visualisation [ggplot2 v3.3.5, ggpubr v0.4] -> stage not stated [ComplexHeatmap v2.11.1, GSVA v1.42.0, VEP v94.5, data.table v1.14.6, edgeR v3.36.0, limma v3.50.3, tidyverse v1.3.2]

### Aberrant phase separation and nucleolar dysfunction in rare genetic diseases. (Nature 2023)

- DOI: 10.1038/s41586-022-05682-1 | PMCID: PMC9931588 | PMID: 36755093
- Evidence: The resulting VCF file was filtered for protein-coding variant consequences using Ensembl Variant Effect Predictor (VEP, v.104)).
- Full pipeline: visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BEDTools v2.30.0, ColabFold, R, VEP, ggplot2]

### FinnGen provides genetic insights from a well-phenotyped isolated population. (Nature 2023)

- DOI: 10.1038/s41586-022-05473-8 | PMCID: PMC9849126 | PMID: 36653562
- Evidence: Variant annotation We utilized Variant Effect Predictor ( https://www.ensembl.org/info/docs/tools/vep/index.html ) for annotating imputation panel variants.
- Full pipeline: alignment/mapping [SAIGE v0.35.8.8] -> variant calling [GATK] -> differential/statistical testing [SAIGE v0.35.8.8] -> stage not stated [R v4.0, VEP]

### Examining the role of common variants in rare neurodevelopmental conditions. (Nature 2024)

- DOI: 10.1038/s41586-024-08217-y | PMCID: PMC11634775 | PMID: 39567701
- Evidence: Analyses of polygenic scores and rare coding variants Sequence data from DDD, GEL and MCS were annotated with the Ensembl Variant Effect Predictor (VEP) 92 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GCTA, LDSC] -> stage not stated [PLINK, VEP]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Evidence: The variant ID is from dbSNP, the base-pair locations are in build 37 and the annotations are from Variant Effect Predictor.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Variant annotation was performed using Ensembl VEP 60 .
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Evidence: Somatic VCFs were annotated with The Ensembl Variant Effect Predictor (VEP Ensembl v.104) 65 .
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **93.2**
- Evidence: Variants were merged across callers and annotated using Ensembl (v.93) 65 , COSMIC (v.86) 66 , 1000Genomes (Phase3) 67 , ClinVar (201706) 68 , PolyPhen (v.2.2.2) 69 , SIFT (v.5.2.2) 70 , FATHMM (v.2.1) 71 , gnomAD (r.2.0.1) 72 and dbSNP (v.150) 73 using Variant Effect Predictor (v.93.2) 74 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### The genomic landscape of 2,023 colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07747-9 | PMCID: PMC11374690 | PMID: 39112709
- Evidence: Single-nucleotide variant and indel drivers Mutation annotation Somatic mutations were annotated to Ensembl (v.101, GRCh38) using Variant Effect Predictor (VEP) 73 .
- Full pipeline: alignment/mapping [GATK, Mutect2] -> stage not stated [ANNOVAR, BCFtools v1.9, BEDTools v2.3.0, DELLY, R, RSEM, Strelka v2.4.7, VEP, igraph]

### Sources of gene expression variation in a globally diverse human cohort. (Nature 2024)

- DOI: 10.1038/s41586-024-07708-2 | PMCID: PMC11291278 | PMID: 39020179
- Evidence: Bars represent the first, second (median) and third quartiles of the data and whiskers are bound to 1.5× the interquartile range. c , Enrichment of lead sQTLs ( n = 13,107 unique sVariants total, at least 5 per category) within functional annotation categories from Ensembl Variant Effect Predictor (left), along with the proportion of all lead sQTLs falling into each annotation category (right).
- Full pipeline: dimensionality reduction/clustering [ADMIXTURE] -> visualisation [ADMIXTURE] -> stage not stated [VEP]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Evidence: Functional annotation of the resulting mutation calls was accomplished with Variant Effect Predictor and further annotated with oncoKB 47 .
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### Identification of constrained sequence elements across 239 primate genomes. (Nature 2024)

- DOI: 10.1038/s41586-023-06798-8 | PMCID: PMC10808062 | PMID: 38030727
- Evidence: Coding variants were annotated as loss-of-function, missense, or synonymous using the Ensembl Variant Effect Predictor (VEP) v85 71 .
- Full pipeline: alignment/mapping [SAIGE, minimap2] -> differential/statistical testing [LDSC, SAIGE] -> stage not stated [RepeatMasker v4.1.2, VEP]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Overlapped transcripts were identified for each variant and the effects of the variants on the transcripts were predicted by Ensembl VEP 104.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Sex and smoking bias in the selection of somatic mutations in human bladder. (Nature 2025)

- DOI: 10.1038/s41586-025-09521-x | PMCID: PMC12611770 | PMID: 41062697
- Evidence: Next, we obtained the consequence type (missense, synonymous, nonsense or splice-affecting) of these mutations on the MANE transcript 76 of each gene from the output of the Variant Effect Predictor v.111 (ref.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, Nextflow, VEP]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: SV impact estimation on genomic features We used Ensembl VEP with annotation from the CHM13 rapid release of Ensembl (107) to estimate the impact of the SVs on genomic features.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Complex genetic variation in nearly complete human genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09140-6 | PMCID: PMC12350169 | PMID: 40702183
- Evidence: SVs affecting genes We annotated the potential effect of long-read SVs on genes using the coding transcripts and exons defined in GENCODE (v.45) 106 , as per Ensembl VEP (v.111) 107 .
- Full pipeline: quality control [minimap2 v2.26] -> alignment/mapping [BCFtools, BEDTools v2.29.0, MUSCLE v3.38.31, minimap2 v2.26] -> variant calling [BCFtools, SHAPEIT] -> quantification [DESeq2 v1.38.3] -> differential/statistical testing [DESeq2 v1.38.3] -> structure determination [BCFtools] -> visualisation [ggplot2] -> stage not stated [DELLY v1.1.6, DeepVariant v1.6, HMMER v3.3.2d, RepeatMasker v4.1.6, SAMtools v1.15.1, VEP, hifiasm]

### Sequence diversity lost in early pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-025-09031-w | PMCID: PMC12176622 | PMID: 40399685
- Evidence: Annotation of pathogenic variants Sequence variants were annotated on the basis of release 100 of the Variant Effect Predictor (VEP) 66 using RefSeq gene annotations 67 .
- Full pipeline: alignment/mapping [BWA, Picard, R] -> variant calling [Manta v1.6.0] -> differential/statistical testing [R] -> machine learning [ADMIXTURE] -> stage not stated [PLINK, VEP]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Evidence: Mutation calls were annotated with Ensembl VEP v.112 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### Clonal dynamics and somatic evolution of haematopoiesis in mouse. (Nature 2025)

- DOI: 10.1038/s41586-025-08625-8 | PMCID: PMC12074984 | PMID: 40044850
- Evidence: Next, VarDict 64 was used to identify all putative variants, followed by functional annotation using Ensembl Variant Effect Predictor 65 .
- Full pipeline: alignment/mapping [BWA] -> simulation/modelling [R] -> stage not stated [VEP, lme4]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: Variants were then annotated with the ENSEMBL Variant Effect Predictor (VEP) 64 v.10448 with the ‘everything’ flag and the LOFTEE plugin 65 and prioritized a single MANE v.0.97 or VEP canonical ENSEMBL transcript and most damaging consequence as defined by VEP defaults.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: Variants were annotated using SnpEff (v.5.1), ANNOVAR and Ensembl Variant Effect Predictor (v.107) and an array of databases for variant allele frequency and effect on the encoded protein, conservation, tissue expression, deleteriousness and disease association.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Evolutionary characterization of lung cancer metastasis. (Nature 2026)

- DOI: 10.1038/s41586-026-10428-4 | PMCID: PMC13190308 | PMID: 42056508
- Evidence: Detection of driver alterations Somatic mutations were annotated using OncoKB 30 , 31 , openCRAVAT 66 ( https://www.opencravat.org/ ) and the Ensembl Variant Effect Predictor (v.114) 67 .
- Full pipeline: stage not stated [VEP]

### The evolutionary history and unique genetic diversity of Indigenous Americans. (Nature 2026)

- DOI: 10.1038/s41586-026-10406-w | PMCID: PMC13149005 | PMID: 42020734
- Evidence: Variants in the joint cohort variant call format were then normalized and annotated using the Ensembl Variant Effect Predictor (VEP) 70 v.113, incorporating several annotation sources.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK, VEP] -> normalisation [VEP] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK v1.9, R, SnpEff]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Evidence: Variants predicted by Variant Effect Predictor to have high-impact consequences were considered putative LoF variants.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: Second, as only non-synonymous (protein-altering) variants can be potentially immunogenic in immunocompetent settings, the TMB output was filtered for variants with a predicted impact classified as MODERATE or HIGH based on the Ensembl Variant Effect Predictor (referred to as the TMB of protein-coding alterations, pTMB).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Evidence: Coding variants within the credible SNP sets (cumulative PIP: 0.95) were annotated using Ensembl Variant Effect Predictor 77 (VEP; release 113), ClinVar (version June, 2023) 78 and AlphaMissense prediction scores 79 .
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: We identified high-confidence LoF sites using the Variant Effect Predictor in Ensembl 82 with the LOFTEE plugin 83 and restricted our analyses to variants with MAF < 1%.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Decay of driver mutations shapes the landscape of intestinal transformation. (Nature 2026)

- DOI: 10.1038/s41586-025-09762-w | PMCID: PMC12804087 | PMID: 41339549
- Evidence: The consequences of variants were annotated with the Ensembl Variant Effect Predictor (VEP) 80 using gene builds from Ensembl release 96.
- Full pipeline: alignment/mapping [BWA v0.7.17, R] -> quantification [QuPath] -> visualisation [ggplot2] -> stage not stated [VEP]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Evidence: Variant annotation was performed using the Ensembl Variant Effect Predictor (VEP, release 112) 65 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### Specificity, length and luck drive gene rankings in association studies. (Nature 2026)

- DOI: 10.1038/s41586-025-09703-7 | PMCID: PMC12823407 | PMID: 41193809
- Evidence: We used the consequence information in the file, which corresponds to Ensembl Variant Effect Predictor (v85) 78 , for annotating variants.
- Full pipeline: differential/statistical testing [MAGMA] -> stage not stated [BEDTools, LDSC, REGENIE, VEP]

### Genomic evidence for inbreeding depression and purging of deleterious genetic variation in Indian tigers. (PNAS 2021)

- DOI: 10.1073/pnas.2023018118 | PMCID: PMC8670471 | PMID: 34848534
- Evidence: We used Ensembl Variant Effect Predictor ( 59 ) on SNPs to identify the consequence of a mutation and classify them as missense, LOF, or intergenic as described by Xue et al.
- Full pipeline: alignment/mapping [ANGSD, GATK] -> registration [GATK] -> stage not stated [Picard, Strelka, VCFtools, VEP]

### Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. (PNAS 2021)

- DOI: 10.1073/pnas.2106844118 | PMCID: PMC8713748 | PMID: 34916285
- Evidence: Per-variant quality was also assessed, and only variants with a “PASS” in the filter column were retained and annotated utilizing Ensembl Variant Effect Predictor (VEP) v.95 ( 83 ).
- Full pipeline: stage not stated [ADMIXTURE, BEDTools, GATK, R, VEP, WGCNA, scikit-learn]

### SAMD9L autoinflammatory or ataxia pancytopenia disease mutations activate cell-autonomous translational repression. (PNAS 2021)

- DOI: 10.1073/pnas.2110190118 | PMCID: PMC8403910 | PMID: 34417303
- Evidence: VCF files were annotated with Variant Effect Predictor (VEP) v76 using the LoFTEE and dbNSFP plugins (including CADD v1.3) and assembled into GEMINI databases (v0.18.3).
- Full pipeline: alignment/mapping [BWA v0.7.10] -> variant calling [GATK] -> registration [GATK] -> stage not stated [VEP]

### A phage mechanism for selective nicking of dUMP-containing DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2026354118 | PMCID: PMC8201957 | PMID: 34074772
- Evidence: Ensembl’s Variant Effect Predictor was used for annotation ( https://bacteria.ensembl.org/index.html ).
- Full pipeline: read trimming [Cutadapt, Picard] -> alignment/mapping [GATK v3.7] -> variant calling [Cutadapt] -> stage not stated [Fiji, ImageJ, VEP]

### The mutational load in natural populations is significantly affected by high primary rates of retroposition. (PNAS 2021)

- DOI: 10.1073/pnas.2013043118 | PMCID: PMC8017666 | PMID: 33526666
- Version used: **98.2**
- Evidence: We predicted the functional effects of each SNP by using Ensembl VEP v98.2 ( 32 ), based on the gene annotation data from Ensembl version 87 ( 41 ).
- Full pipeline: stage not stated [GATK, VEP v98.2]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: If the risk variant could not be assigned to overlapping or distal active promoters in neurons, we then assigned them to genes according to proximity-based annotations from the Ensembl Variant Effect Predictor ( 66 ).
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### An intermediate-effect size variant in &lt;i&gt;UMOD&lt;/i&gt; confers risk for chronic kidney disease. (PNAS 2022)

- DOI: 10.1073/pnas.2114734119 | PMCID: PMC9388113 | PMID: 35947615
- Evidence: Annotation and in silico analyses were performed using the VarSome platform ( 51 ) and Ensembl VEP considering ENST00000302509.8 as the reference transcript.
- Full pipeline: stage not stated [PyMOL, VEP]

### Targeted RNA editing in brainstem alleviates respiratory dysfunction in a mouse model of Rett syndrome. (PNAS 2022)

- DOI: 10.1073/pnas.2206053119 | PMCID: PMC9388114 | PMID: 35939700
- Evidence: To predict the impact of RNA-editing and annotate the sites genome-wide, we used Variant Effect Predictor ( SI Appendix , Supplemental Methods ).
- Full pipeline: stage not stated [VEP]

### Microbiome-associated human genetic variants impact phenome-wide disease risk. (PNAS 2022)

- DOI: 10.1073/pnas.2200551119 | PMCID: PMC9245617 | PMID: 35749358
- Evidence: Variants were annotated and accessed using a web interface for Variant Effect Predictor ( 48 ) and SNPNexus ( 49 ), both utilizing the Ensembl genome database ( 47 ) for reference.
- Full pipeline: variant calling [PLINK] -> visualisation [ComplexHeatmap v2.12] -> stage not stated [R, SAIGE, VEP]

### Impact of natural selection on global patterns of genetic variation and association with clinical phenotypes at genes involved in SARS-CoV-2 infection. (PNAS 2022)

- DOI: 10.1073/pnas.2123000119 | PMCID: PMC9173769 | PMID: 35580180
- Evidence: We used Ensembl Variant Effect Predictor (VEP) for variant annotations ( 67 ) ( SI Appendix ).
- Full pipeline: visualisation [VMD] -> stage not stated [VEP]

### DNA language models are powerful predictors of genome-wide variant effects. (PNAS 2023)

- DOI: 10.1073/pnas.2311219120 | PMCID: PMC10622914 | PMID: 37883436
- Evidence: All possible SNPs in the region Chr5:3,500,000-4,500,000 were generated and their consequences annotated with Ensembl Variant Effect Predictor ( 41 ) web interface https://plants.ensembl.org/Arabidopsis_thaliana/Tools/VEP , with the upstream/downstream argument set to 500, used to call variants as upstream/downstream instead of intergenic.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [VEP]

### Sequencing 4.3 million mutations in wheat promoters to understand and modify gene expression. (PNAS 2023)

- DOI: 10.1073/pnas.2306494120 | PMCID: PMC10515147 | PMID: 37703281
- Evidence: We determined mutation effects using the Variant Effect Predictor (VEP) program ( 43 ) ( SI Appendix, Method S4 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, SAMtools v1.7] -> stage not stated [VEP]

### Large-scale functional screen identifies genetic variants with splicing effects in modern and archaic humans. (PNAS 2023)

- DOI: 10.1073/pnas.2218308120 | PMCID: PMC10214146 | PMID: 37192163
- Evidence: Ensembl Variant Effect Predictor (VEP) Annotations.
- Full pipeline: stage not stated [VCFtools v0.1.16, VEP]

### The SHDRA syndrome-associated gene <i>TMEM260</i> encodes a protein-specific O-mannosyltransferase. (PNAS 2023)

- DOI: 10.1073/pnas.2302584120 | PMCID: PMC10214176 | PMID: 37186866
- Evidence: Genome Analysis Toolkit HaplotypeCaller was used for variant calling and Ensembl Variant Effect Predictor for variant annotation.
- Full pipeline: variant calling [GATK, VEP] -> quantification [ImageJ] -> stage not stated [AlphaFold]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Evidence: To identify deleterious mutations, we predicted the functional effects of the polarized SNPs using both SnpEff v5.0 ( 104 ) and the Variant Effect Predictor (VEP) v99.2 ( 105 ).
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Resurrection genomics provides molecular and phenotypic evidence of rapid adaptation to salinization in a keystone aquatic species. (PNAS 2023)

- DOI: 10.1073/pnas.2217276120 | PMCID: PMC9963159 | PMID: 36730191
- Evidence: In addition to testing for GO term enrichment, we also surveyed all genes for potential SNPs and small indels mutations potentially driving selection using Ensembl’s Variant Effect Predictor ( 42 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools, BEDTools, SAMtools, VEP]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Evidence: The remaining sites, with felCat8 coordinates, were annotated with an impact and consequence using Ensembl Variant Effect Predictor (VEP) v92.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Integrating extensive functional annotations and multiomics of cattle enhances climate resilience prediction and mapping. (PNAS 2025)

- DOI: 10.1073/pnas.2514736122 | PMCID: PMC12704747 | PMID: 41284851
- Evidence: This was followed by several sets of variants related to coding sequence and genetic and/or epigenetic regulation, including allele-specific-binding QTL (asbQTLs) in blood and cis gene expression QTL (eQTLs) from 16 tissues of the Cattle GTEx ( 20 , 25 , 26 ) and variants annotated by Variant Effect Predictor (VEP) ( 27 ) related to protein coding (VEP_coding.related).
- Full pipeline: machine learning [R] -> stage not stated [GCTA, VEP]

### Germline variants in &lt;i&gt;UHRF1&lt;/i&gt; are associated with multilocus imprinting disturbance in humans and mice. (PNAS 2025)

- DOI: 10.1073/pnas.2505884122 | PMCID: PMC12403135 | PMID: 40825131
- Evidence: The generated VCF files were manipulated using VCFTools 0.1.13 ( 63 ) and annotated using ANNOVAR and Variant Effect Predictor V109 ( 64 ).
- Full pipeline: quality control [Bismark, FastQC] -> read trimming [Bismark, FastQC, Trim Galore] -> alignment/mapping [Bismark, GATK v3.7, SAMtools v1.3.1] -> variant calling [GATK v3.7, SAMtools v1.3.1] -> stage not stated [ANNOVAR, VEP]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Evidence: VCF files were annotated with Variant Effect Predictor (VEP) v79 using plugins including LoFTEE, dbNSFP v2.9, and CADD v1.3.
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### The importance of small-island populations for the long-term survival of endangered large-bodied insular mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422690122 | PMCID: PMC12232422 | PMID: 40553499
- Evidence: To assess the efficiency of purifying selection across different populations, we first built unfolded site frequency spectra (SFS) using ANGSD ( 28 ), based on alleles that have been assigned different impact ratings by the Variant Effect Predictor ( 29 ), i.e., low, modifier, moderate, and high ( Fig.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [ANGSD, QGIS, R, VEP]

### Single Antisense Oligonucleotides Correct Diverse Splicing Mutations in Hotspot Exons. (PNAS 2025)

- DOI: 10.1073/pnas.2425659122 | PMCID: PMC12207475 | PMID: 40523177
- Evidence: ( B ) The proportion of singleton variants from MyCode was calculated for variant sets based on their annotation as synonymous, missense, splice region, or stop-gained variants by the Ensembl Variant Effect Predictor (VEP) ( Left ) or based on their MaPSy splicing score ( Right ) (error bars represent P ± 2 × SD of P ; P -values from two-sample proportion Z-test).
- Full pipeline: differential/statistical testing [limma] -> stage not stated [SAMtools, VEP]

### Cross-species modeling of plant genomes at single-nucleotide resolution using a pretrained DNA language model. (PNAS 2025)

- DOI: 10.1073/pnas.2421738122 | PMCID: PMC12184517 | PMID: 40489624
- Evidence: All potential mutations in the genic regions and 1 kb flanking regions of maize and sorghum chromosome 8 were generated and annotated using the Ensembl Variant Effect Predictor (VEP) local API ( 44 ), with the upstream/downstream parameter set to 1,000 to classify variants as either upstream or downstream.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [XGBoost] -> visualisation [UMAP] -> stage not stated [BEDTools, BUSCO, VEP]

### Biallelic variants in the conserved ribosomal protein chaperone gene &lt;i&gt;PDCD2&lt;/i&gt; are associated with hydrops fetalis and early pregnancy loss. (PNAS 2025)

- DOI: 10.1073/pnas.2426078122 | PMCID: PMC12012559 | PMID: 40208938
- Version used: **103.0**
- Evidence: Variants were annotated using the Ensembl Variant Effect Predictor (v.103.0).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> stage not stated [GATK, VEP v103.0, fastp v0.21.0]

### A disease-specific convergence of host and Epstein-Barr virus genetics in multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418783122 | PMCID: PMC12002260 | PMID: 40184175
- Evidence: 1 D were identified using Variant Effect Predictor version 98.
- Full pipeline: differential/statistical testing [lme4] -> stage not stated [Cytoscape v3.9.1, R v1.1.456, VEP]

### Neanderthal adaptive introgression shaped &lt;i&gt;LCT&lt;/i&gt; enhancer region diversity without linking to lactase persistence in East Asian populations. (PNAS 2025)

- DOI: 10.1073/pnas.2404393122 | PMCID: PMC11929401 | PMID: 40063818
- Evidence: Variants were annotated using the Ensembl Variant Effect Predictor (VEP) ( 91 ) with the corresponding VEP-compiled annotation database (v109_GRCh38).
- Full pipeline: variant calling [R] -> stage not stated [VEP]

### Host genetic regulation of rumen 6-hydroxymelatonin reduces methane emissions in dairy cattle. (PNAS 2026)

- DOI: 10.1073/pnas.2604454123 | PMCID: PMC13291679 | PMID: 42258707
- Evidence: The Variant Effect Predictor ( https://www.ensembl.org/vep ) was used for gene annotation.
- Full pipeline: quality control [fastp] -> alignment/mapping [fastp] -> dimensionality reduction/clustering [R] -> differential/statistical testing [GEMMA, TwoSampleMR v0.5.6] -> stage not stated [GCTA, PLINK, VEP, lavaan]

### The persistence and loss of hard selective sweeps amid admixture in ancient Eurasians. (PNAS 2026)

- DOI: 10.1073/pnas.2528672123 | PMCID: PMC13123867 | PMID: 42008668
- Evidence: To understand if the genes within these 32 sweeps are enriched for any functions, we annotated all protein coding genes within 300 Kb distance upstream and downstream of the central SNP in the window with highest probability within a sweep using Ensembl Variant Effect Predictor (VEP) ( Dataset S2 ).
- Full pipeline: alignment/mapping [FUMA] -> stage not stated [VEP]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: High-confidence variants were annotated with Ensembl VEP v107 and converted to Mutation Annotation Format (MAF) using vcf2maf ( https://github.com/mskcc/vcf2maf ).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Diversity and scale: Genetic architecture of 2068 traits in the VA Million Veteran Program. (Science 2024)

- DOI: 10.1126/science.adj1182 | PMCID: PMC12857194 | PMID: 39024449
- Evidence: Bars are colored by the proportion of each represented by each grouped Variant Effect Predictor (VEP) annotation and the black boxes illustrate the proportion of each bar attributable to coding variation.
- Full pipeline: stage not stated [FUMA, LDSC, SAIGE, VEP]

### Ciliopathy patient variants reveal organelle-specific functions for TUBB4B in axonemal microtubules. (Science 2024)

- DOI: 10.1126/science.adf5489 | PMCID: PMC7616230 | PMID: 38662826
- Evidence: Variant annotation was obtained from the Ensembl Variant Effect Predictor (v99, ( 55 )).
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ, Seurat, ilastik] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [ChimeraX, IMOD, PHENIX, RELION] -> visualisation [ImageJ, ilastik] -> stage not stated [VEP]

