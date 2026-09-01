# Nextflow

- **Category:** workflow
- **Papers in survey:** 45
- **Journals:** Nature (29), PNAS (10), Cell (4), Science (2)
- **Years:** 2021 (5), 2022 (5), 2023 (5), 2024 (4), 2025 (19), 2026 (7)
- **Versions named:** 19.10.0 (3), 21.10.6 (2), 24.04.2 (1), 24.10.5 (1), 24.04.4 (1), 23.10.1.5891 (1), 24.04.3.5916 (1), 21.03.0 (1), 20.07.1 (1), 21.10.3 (1)
- **Pipeline stages it appears in:** alignment/mapping (10), quality control (7), read trimming (3), differential/statistical testing (2), quantification (2), visualisation (1), registration (1), structure determination (1), variant calling (1), dimensionality reduction/clustering (1)

## Papers

### High-resolution profiling of pathways of escape for SARS-CoV-2 spike-binding antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.045 | PMCID: PMC8096189 | PMID: 34010620
- Evidence: ...thon.org/ DNAChisel (version 3.2.2) https://github.com/Edinburgh-Genome-Foundry/DnaChisel phip-flow Matsen Lab https://github.com/matsengrp/phip-flow Nextflow https://www.nextflow.io/ Bowtie https://quay.io/biocontainers/bowtie:1.2.2%5fpy36h2d50403_1 phippery Matsen Lab https://github.com/matsengrp/phippery xarray http://xarray.pydata.org/en/stable/ SAMtools https://quay.io/biocontainers/samtools:...
- Full pipeline: stage not stated [Clustal Omega, Nextflow, R v4.0.2, SAMtools, ggpubr, tidyverse, xarray]

### Evaluating the Effects of SARS-CoV-2 Spike Mutation D614G on Transmissibility and Pathogenicity. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.020 | PMCID: PMC7674007 | PMID: 33275900
- Evidence: ...kygrowth IQtree 1.6.12 ( Minh et al., 2020 ; Rambaut et al., 2020 ) http://www.iqtree.org/ MRC-CLIMB ( Connor et al., 2016 ) https://www.climb.ac.uk/ Nextflow pipeline for processing/assembly of ARTIC protocol amplicons https://github.com/connor-lab/ncov2019-artic-nf https://github.com/connor-lab/ncov2019-artic-nf Resource Availability Lead Contact Further information and requests for resources an...
- Full pipeline: differential/statistical testing [R v3.6] -> stage not stated [BEAST, IQ-TREE, Nextflow, brms v2.13.5]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: (2021) N/A Nfcore/rnaseq pipeline V 3.5 ( Ewels et al., 2020 ) N/A ( Ewels et al., 2020 ) Nextflow domain specific language V 19.10.0 ( Di Tommaso et al., 2017 ) N/A ( DI Tommaso et al., 2017 ) Singularity V 2.6.0 ( Kurtzer et al., 2017 ) N/A( Kurtzer et al., 2017 ) RSEM-STAR Dobin et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Evidence: 18 The analysis pipeline was written using the Nextflow pipeline framework, which allowed for the analysis to be run reproducibly in containers, which were executed in parallel across nodes of the computing cluster.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **19.10.0**
- Evidence: To facilitate reproducible analysis, samples were processed using the publicly available nf-core/RNA-seq pipeline version 1.4.2 implemented in Nextflow 19.10.0 using Singularity 3.2.1–1 with the minimal command nextflow run nf-core/rnaseq -r 1.4.2 –singleEnd -profile singularity –reverseStranded --three_prime_clip_r2 3 53 – 55 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: We also used the wf_artic (ARTIC SARS-CoV-2) pipeline as built using the Nextflow workflow framework 56 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### A druggable copper-signalling pathway that drives inflammation. (Nature 2023)

- DOI: 10.1038/s41586-023-06017-4 | PMCID: PMC10131557 | PMID: 37100912
- Evidence: ChIP–seq data processing and quality controls have been performed with the Institut Curie ChIP–seq Nextflow pipeline (1.0.6) available at https://github.com/bioinfo-pf-curie/ChIP-seq .
- Full pipeline: quality control [Nextflow] -> normalisation [R, deepTools, edgeR v3.30.3] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [clusterProfiler, limma]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **20.07.1**
- Evidence: To ensure the reproducibility and portability of the above pipeline, all steps described were implemented through the Nextflow (v.20.07.1) 62 pipeline manager.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Version used: **19.10.0**
- Evidence: ATAC–seq analysis ATAC–seq data analysis was performed using the nf-core/atacseq pipeline (v.1.0.0) 109 , which runs Nextflow (v.19.10.0) 113 , for quality controls, read alignment against the new skate assembly, filtering, data visualization, peak calling, read count and differential accessibility analysis.
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Version used: **21.10.3**
- Evidence: Sequences from all 20 samples were processed using the Nextflow (v.21.10.3) Sarek pipeline (nf-core/sarek v.3.0).
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Multiple pathways for SARS-CoV-2 resistance to nirmatrelvir. (Nature 2023)

- DOI: 10.1038/s41586-022-05514-2 | PMCID: PMC9849135 | PMID: 36351451
- Evidence: Consensus sequence generation was performed using the ONT Epi2Me ARTIC Nextflow pipeline v.0.3.16 ( https://github.com/epi2me-labs/wf-artic ).
- Full pipeline: dimensionality reduction/clustering [SciPy, seaborn] -> stage not stated [CellProfiler v4.0.7, Nextflow, Pangolin v4.0.6]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: CUT&Tag analysis First, 150b and 155b paired-end CUT&Tag sequencing reads were processed and aligned to the mouse-genome assembly (version GRCm38) using the NF-core (10.5281/zenodo.7715959) CUT&RUN Nextflow pipeline version 3.1 (ref.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Evidence: MMseqs2 and Colabfold_batch were run with a Nextflow 55 pipeline, and all parameters used can be found at https://github.com/jnoms/vpSAT .
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Evidence: The crispr-process-nf Nextflow workflow is available at https://github.com/ZuberLab/crispr-process-nf/tree/566f6d46bbcc2a3f49f51bbc96b9820f408ec4a3 .
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Version used: **19.10.0**
- Evidence: The fastq files were processed with Nextflow (v19.10.0), nf-core/rnaseq (v1.3) and aligned using GRCh38 as reference.
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Version used: **23.10.1.5891**
- Evidence: After sequencing, fastq files were first demultiplexed with sample-specific index primers using bcl2fastq and aligned to GRCh38 using the nf-core/cutandrun pipeline v.3.2.1 with standard settings, Nextflow v.23.10.1.5891 65 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: To ensure comparability, both public and newly generated data underwent processing through an optimized fork of the community-curated Nextflow rnaseq pipeline (v.3.15.1) 56 – 58 , which was executed in the following order: Read preprocessing Adapters, low-quality base pairs, and poly(A) and poly(G) tails were trimmed using the fastp 59 program (v.0.23.4).
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### Sperm sequencing reveals extensive positive selection in the male germline. (Nature 2025)

- DOI: 10.1038/s41586-025-09448-3 | PMCID: PMC12611766 | PMID: 41062690
- Evidence: Base calling and filtering All samples were processed using a Nextflow implementation of the NanoSeq calling pipeline ( https://github.com/cancerit/NanoSeq ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [Bioconductor, ggplot2 v3.4.4, lme4] -> visualisation [R] -> stage not stated [BCFtools, Nextflow]

### Sex and smoking bias in the selection of somatic mutations in human bladder. (Nature 2025)

- DOI: 10.1038/s41586-025-09521-x | PMCID: PMC12611770 | PMID: 41062697
- Evidence: Somatic mutation calling We constructed a computational pipeline (deepUMIcaller) in Nextflow 65 to call mutations from duplex sequencing data on the basis of an early version of nf-core/fastquorum pipeline 66 , which implements the fgbio Best Practices FASTQ to Consensus Pipeline ( https://github.com/fulcrumgenomics/fgbio/blob/main/docs/best-practice-consensus-pipeline.md ) and downstream variant ...
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, Nextflow, VEP]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Evidence: All data were processed using the nf-core RNA-seq Nextflow pipeline (v3.12.0) 63 , and in the case of the 3′ end sequencing data, the additional option --noLengthCorrection was provided to Salmon to prevent length correction for gene expression.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **24.04.3.5916**
- Evidence: Graph generation Nextflow v24.04.3.5916 84 was used to run the nf-core/pangenome v1.1.2 - canguro deployment 85 , 86 of PGGB 22 within the nextflow singularity profile.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Single-cell DNA and RNA sequencing data analysis DNA sequencing reads per cell were initially processed (quality control, alignment) by means of the BJ-DNA-QC Nextflow-based pipeline from BioSkryb using hg38 as the main reference.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Regulation of PV interneuron plasticity by neuropeptide-encoding genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08933-z | PMCID: PMC12222018 | PMID: 40307547
- Version used: **21.03.0**
- Evidence: Bioinformatics High-throughput sequencing data from PV + interneurons-derived ribosome-associated mRNAs were processed using the community-curated Nextflow (version 21.03.0.edge, build 5518 (3 May 2021 10:52 UTC), available at https://zenodo.org/record/3490660#.Y8AhHXbP2Uk ) RNA-seq pipeline 76 .
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> stage not stated [Nextflow v21.03.0, edgeR]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **21.10.6**
- Evidence: CUT&RUN samples were processed via Nextflow (21.10.6), using the nf-core CUT&RUN pipeline (v3.0.0) 79 .
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: Demultiplexed raw reads were processed using the Nextflow 58 , nf-core 59 ampliseq 60 pipeline (v.2.4.0), with the following parameters: -profile singularity --FW_primer GTGYCAGCMGCCGCGGTAA --RV_primer CCGYCAATTYMTTTRAGTTT --dada_ref_taxonomy silva --ignore_empty_input_files --ignore_failed_trimming --min_frequency 10 --retain_untrimmed --trunclenf 240 --trunclenr 160.
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: De novo bulk RNA-seq data analysis Reads were processed with an adapted version of the nf-core 41 pipeline for RNA-seq, using Nextflow 42 (v22.04).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Micro-C libraries were aligned to the mm9 reference genome and processed using the Nextflow ( https://www.nextflow.io/ ) pipeline distiller-nf ( https://github.com/open2c/distiller-nf ) using the following configurations; make_pairsam = False, drop_readid = False, parsing_options: ‘--add-columns mapq --walks-policy mask’, max_mismatch_bp = 1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Next, we ran custom Nextflow 70 pipelines to process the samples.
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Version used: **24.04.2**
- Evidence: Data were analysed using the nf-core/cutandrun pipeline v.3.2.2 with Nextflow v.24.04.2, using the default parameters and following software dependencies: bedtools (v.2.30.0), bowtie (v.2.4.4), deeptools (v.3.5.1), fastqc (v.0.12.1), picard (v.3.1.0), Python (v.3.9.12), samtools (v.1.17), Genrich (v.0.6.1), TrimGalore (v.0.6.6), ucsc (v.377).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Version used: **24.10.5**
- Evidence: The pipeline was executed with Nextflow (v24.10.5) 69 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: The per-library computational analysis workflow described so far was wrapped in a Nextflow 77 pipeline with two processes to enable parallelization and reproducibility.
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **24.04.4**
- Evidence: Reads were processed using the Nextflow (v.24.04.4)-based nf-core/rnasplice pipeline 64 (v.1.0.4), primarily for downstream rMATS analysis 65 (v.4.1.2).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Somatic evolution following cancer treatment in normal tissue. (Nature 2026)

- DOI: 10.1038/s41586-025-09792-4 | PMCID: PMC13190248 | PMID: 41372419
- Evidence: Duplex sequencing bioinformatic analyses Duplex sequencing fastqs were processed using a bespoke Nextflow 47 pipeline that uses the fgbio suite (v.2.2.1) and follows the best practices for duplex sequencing processing ( https://github.com/oriolpich/normal_tissues_nature_2025/tree/main/src/duplex_nf/DuplexPipe ).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> differential/statistical testing [R, lme4] -> stage not stated [Nextflow, SAMtools v1.19.2]

### SARS-CoV-2 evolution in animals suggests mechanisms for rapid variant selection. (PNAS 2021)

- DOI: 10.1073/pnas.2105253118 | PMCID: PMC8612357 | PMID: 34716263
- Evidence: Raw sequencing data were input into a comprehensive Nextflow pipeline for processing next-generation sequencing data and SNV and SV calling.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> stage not stated [GATK, Nextflow, SnpEff]

### Nonparametric coalescent inference of mutation spectrum history and demography. (PNAS 2021)

- DOI: 10.1073/pnas.2013798118 | PMCID: PMC8166128 | PMID: 34016747
- Evidence: All of the analyses and figures for this paper can be reproduced using Nextflow pipelines ( 76 ) and Jupyter notebooks ( https://jupyter.org ) available in ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [BCFtools, Jupyter, Nextflow, Python]

### Phylodynamic signatures in the emergence of community-associated MRSA. (PNAS 2022)

- DOI: 10.1073/pnas.2204993119 | PMCID: PMC9659408 | PMID: 36322765
- Evidence: Quality control, assembly, genotyping, variant calling and ML tree construction, statistical phylodynamic reconstruction, and exploratory Bayesian analyses were implemented in Nextflow ( 65 ) for reproducibility of the workflows ( https://github.com/np-core/phybeast ).
- Full pipeline: quality control [Nextflow] -> variant calling [Nextflow] -> normalisation [TreeTime v0.7.1] -> differential/statistical testing [Nextflow] -> structure determination [Nextflow] -> stage not stated [RAxML]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Evidence: All data alignment and downstream analysis was carried out using NF-core and custom Nextflow pipelines to allow full reproducibility.
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Evidence: We used a publicly available Nextflow ( 75 ) pipeline ( https://github.com/nf-core/rnaseq ) to carry out quality control (FASTQC; ref.
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: We developed a reproducible and scalable Nextflow workflow for heritability estimation and GWAS using PLINK (v1.90b6.21 and v2.00a5LM) ( 92 ) and Genome-wide Complex Trait Analysis (GCTA v1.94.1) ( 109 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Evolutionary histories of functional mutations during the domestication and spread of &lt;i&gt;japonica&lt;/i&gt; rice in Asia. (PNAS 2025)

- DOI: 10.1073/pnas.2514614122 | PMCID: PMC12582302 | PMID: 41115193
- Version used: **20.10.0**
- Evidence: For modern genomes, we used a Nextflow v20.10.0 pipeline in which sequencing reads were aligned to the Shuhui498 v1.0 indica reference genome ( 99 ) using BWA v0.7.17 ( 100 ) in “mem” mode ( 101 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, Nextflow v20.10.0] -> variant calling [PLINK v1.90] -> dimensionality reduction/clustering [R v4.3] -> stage not stated [VCFtools v1.6]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **23.10.0**
- Evidence: RNASeq raw reads from all described conditions were mapped against the genome of M. paleacea ( 18 ) and counted using the Nextflow v23.10.0 ( 77 ) pipeline NF-CORE/RNASeq v3.14 ( 78 ) with the options star_salmon to align and quantify reads, as well as “-nextseq 30 -length 50” as extra parameters of TrimGalore v0.6.7 ( 79 ) to remove reads with quality lower than 30 or a length lower than 50 bp.
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Spatial Patterning Analysis of Cellular Ensembles (SPACE) finds complex spatial organization at the cell and tissue levels. (PNAS 2025)

- DOI: 10.1073/pnas.2412146122 | PMCID: PMC11831171 | PMID: 39903116
- Evidence: ...o Yes No Yes Yes No No Yes No Yes No HistoCAT GUI Yes No Yes No Yes Yes No No No No Yes No ImaCytE GUI No No Yes No Yes Yes No No No No Yes No SIMPLI Nextflow Yes No Yes No Yes Yes No No No No Yes No SOMDE Python Yes No No No Yes No No Yes No No Yes No SpaGCN Python Yes No No No Yes Yes Yes No Yes No Yes No SPARK R Yes No No No Yes No No Yes No No Yes No SpatialDE R/Python Yes No No No Yes No No Y...
- Full pipeline: stage not stated [Cellpose v2.0, ImageJ, Nextflow, R]

### Plant-fungi interactions in &lt;i&gt;Marchantia polymorpha&lt;/i&gt; are associated with horizontal gene transfer and terpene metabolism. (PNAS 2026)

- DOI: 10.1073/pnas.2532723123 | PMCID: PMC12890914 | PMID: 41637459
- Version used: **21.10.6**
- Evidence: The raw reads were processed and mapped to their representative genome (Marchantia polymorpha Tak1 v6 and Marchantia polymorpha CA v1) with Nextflow v21.10.6 ( 56 ) and the nf-core/rnaseq r3.9 ( 57 ) pipeline, using the --skip_qc --aligner star_salmon, and --remove_ribo_rna options.
- Full pipeline: quality control [Nextflow v21.10.6] -> alignment/mapping [Nextflow v21.10.6] -> differential/statistical testing [R v4.4, edgeR] -> stage not stated [BLAST, GEMMA]

### Precise targeting of HIV broadly neutralizing antibody precursors in humans. (Science 2025)

- DOI: 10.1126/science.adv5572 | PMCID: PMC12313413 | PMID: 40373114
- Evidence: BALDR’s Perl wrapper was rewritten to be compatible with up-to-date versions of its components, and the Nextflow workflow manager ( 82 ) was incorporated to accelerate data processing and improve reproducibility.
- Full pipeline: alignment/mapping [Bowtie2] -> structure determination [Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, Nextflow, R, RELION v4.0, Trinity]

### Deep-tissue transcriptomics and subcellular imaging at high spatial resolution. (Science 2025)

- DOI: 10.1126/science.adq2084 | PMCID: PMC12005972 | PMID: 39977545
- Evidence: Consistency and reproducibility in data analysis are facilitated by a scalable and portable Nextflow ( 19 ) image processing workflow that manages essential tasks such as image stitching, cross-cycle registration, spot detection, cell segmentation, and spot-to-cell assignment ( fig.
- Full pipeline: alignment/mapping [BigStitcher] -> registration [BigStitcher, Nextflow] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose]

