# kallisto

- **Category:** genomics
- **Papers in survey:** 125
- **Journals:** PNAS (62), Nature (48), Cell (10), Science (5)
- **Years:** 2021 (15), 2022 (25), 2023 (23), 2024 (17), 2025 (31), 2026 (14)
- **Versions named:** 0.46.1 (11), 0.46.0 (7), 0.44.0 (6), 0.46.2 (6), 0.48.0 (4), 0.50.1 (3), 0.42.5 (2), 0.46 (2), 0.43.1 (2), 0.45.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (74), quantification (57), read trimming (13), differential/statistical testing (9), quality control (6), normalisation (5), registration (1), structure determination (1), variant calling (1)

## Papers

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Version used: **0.44.0**
- Evidence: ...https://imagej.net/Fiji BioRender BioRender https://biorender.com/ TrimGalore (version 0.5.0) Martin, 2011 https://github.com/FelixKrueger/TrimGalore kallisto (version 0.44.0) Bray et al. , 2016 https://pachterlab.github.io/kallisto/ R Package: tximport (version 1.8.0) Soneson et al., 2015 https://bioconductor.org/packages/release/bioc/html/tximport.html R Package: DESeq2 (version 1.27.32) Love et...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.053 | PMCID: PMC7857060 | PMID: 33657410
- Evidence: Gene expression data were obtained by the kallisto and bustools programs ( Bray et al., 2016 ; Melsted et al., 2019 ), and TCR and BCR sequences were obtained by the CellRanger program.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [SCENIC v1.1.2, Scanpy v1.4.6, Seurat v2.3.0, kallisto, scDblFinder]

### Disrupting autorepression circuitry generates "open-loop lethality" to yield escape-resistant antiviral agents. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.022 | PMCID: PMC9097017 | PMID: 35561685
- Evidence: Sequencing reads were pseudo-aligned with kallisto ( Bray et al., 2016 ).
- Full pipeline: alignment/mapping [kallisto] -> quantification [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Version used: **0.46.0**
- Evidence: ...r.com/ Flowjo v10.6.2 BD https://www.flowjo.com/ GSEA Broad institute https://www.gsea-msigdb.org/ ImageJ v2.1.0/1.53c NIH https://imagej.nih.gov/ij/ Kallisto v.0.46.0 Pachter Lab https://pachterlab.github.io/kallisto/ Olympic cellSens imaging software Olympus LS https://www.olympus-lifescience.com/ Prism v9.3.0 Graphpad https://graphpad.com RStudio v.1.2.5019 The R foundation https://www.r-projec...
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **0.46.2**
- Evidence: 123 : we mapped the reads to the Clicktag barcodes (8 bp barcodes + constant CAG sequences at the end) using kallisto 0.46.2, 124 specifying the 10x v3 chemistry and tolerating one substitution per barcode; and used bustools 0.41.0 108 to correct, sort and count the reads per cell, and obtain a final Clicktag UMI matrix.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Comparative landscape of genetic dependencies in human and chimpanzee stem cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.043 | PMCID: PMC10461406 | PMID: 37343560
- Evidence: RNA-seq analysis Raw bulk RNA-seq reads from knockdown experiments and wild-type chimpanzee and human iPSCs were adapter-trimmed using cutadapt 125 (with option -b AGATCGGAAGAGCACACGTCTGAACTCCAGTCA) and then pseudo-aligned to species-specific transcriptomes using kallisto 126 with options --single -l 200 -s 20.
- Full pipeline: read trimming [Cutadapt, kallisto] -> alignment/mapping [Cutadapt, kallisto] -> quantification [edgeR] -> normalisation [edgeR] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, ImageJ, R, SAMtools, STRING db v11.5]

### The germline coordinates mitokine signaling. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.010 | PMCID: PMC12261959 | PMID: 38959891
- Evidence: Tools included Kallisto Quant v0.48.0+galaxy1 and DESeq2, v2.11.40.8+galaxy0 72 .
- Full pipeline: quantification [ImageJ] -> stage not stated [DESeq2 v2.11.40.8, kallisto]

### RNA Pol II inhibition activates cell death independently from the loss of transcription. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.034 | PMCID: PMC12406974 | PMID: 40818455
- Evidence: Transcript abundance was estimated using Kallisto with parameters –bootstrap-samples 30 –single-overhang –rf-stranded.
- Full pipeline: quality control [FastQC] -> quantification [FastQC, kallisto] -> normalisation [DESeq2] -> differential/statistical testing [FastQC] -> stage not stated [GSEA]

### The essential host genome for Cryptosporidium survival exposes metabolic dependencies that can be leveraged for treatment. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.001 | PMCID: PMC7618951 | PMID: 40706591
- Evidence: ...es R v.4.4.1 R Core Team https://www.r-project.org/ FastQC V0.11.7 Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ kallisto V0.45.0 Bray et al.
- Full pipeline: quality control [FastQC, ImageJ v2.1.0, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [PHENIX, STRING db v12.0]

### Design principles of cell-state-specific enhancers in hematopoiesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.017 | PMCID: PMC12173716 | PMID: 40345201
- Evidence: Sequencing data were analyzed using kallisto.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ArchR] -> machine learning [TensorFlow] -> stage not stated [R, ggplot2, kallisto, pheatmap]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Evidence: Pre-processing single-cell RNA-seq data The 6,295 SMART-seq cells were processed using kallisto with the ‘kallisto pseudo’ command 24 .
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Swarm Learning for decentralized and confidential clinical machine learning. (Nature 2021)

- DOI: 10.1038/s41586-021-03583-3 | PMCID: PMC8189907 | PMID: 34040261
- Version used: **0.43.1**
- Evidence: In brief, all raw data files were downloaded from GEO ( https://www.ncbi.nlm.nih.gov/geo/ ) and the RNA-seq data were preprocessed using the kallisto v0.43.1 aligner against the human reference genome gencode v27 (GRCh38.p10).
- Full pipeline: alignment/mapping [kallisto v0.43.1] -> normalisation [DESeq2 v1.22.2, R] -> machine learning [Docker] -> stage not stated [Keras v2.3.1, TensorFlow v2.2.0, scikit-learn]

### Dynamic regulation of T<sub>FH</sub> selection during the germinal centre reaction. (Nature 2021)

- DOI: 10.1038/s41586-021-03187-x | PMCID: PMC7979475 | PMID: 33536617
- Version used: **0.46**
- Evidence: Computational analysis For differential gene expression analysis in the bulk RNA sequencing experiments we used kallisto (v.0.46) to map sequence reads to Mus musculus transcriptome (GRCm38/ Ensembl release 99).
- Full pipeline: quantification [DESeq2 v1.24.0, R] -> differential/statistical testing [DESeq2 v1.24.0, R, Seurat v3.1.2, kallisto v0.46] -> stage not stated [GSEA]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Version used: **0.46.1**
- Evidence: Expression of each transcript was measured using the whole RNA-seq dataset (as described in ‘Transcriptome assembly’) and the pseudoalignment algorithm implemented in Kallisto v.0.46.1 58 .
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Histone H2B.8 compacts flowering plant sperm through chromatin phase separation. (Nature 2022)

- DOI: 10.1038/s41586-022-05386-6 | PMCID: PMC9668745 | PMID: 36323776
- Version used: **0.43.0**
- Evidence: Kallisto (v.0.43.0) 85 and Sleuth-(v.0.30.0) 86 were used to obtain transcript per million (TPM) values and q values, respectively.
- Full pipeline: alignment/mapping [Bismark v0.22.2, Bowtie2 v2.3.4.1, MUSCLE, TopHat v2.0.10] -> quantification [ImageJ, kallisto v0.43.0] -> normalisation [deepTools v3.1.1] -> visualisation [R v3.6.0, ggplot2] -> stage not stated [BEDTools v2.28.0, Python v3.9, SAMtools, Trim Galore v0.4.1]

### RASA2 ablation in T cells boosts antigen sensitivity and long-term function. (Nature 2022)

- DOI: 10.1038/s41586-022-05126-w | PMCID: PMC9433322 | PMID: 36002574
- Evidence: To analyse the gene expression, reads were mapped to the human reference transcriptome (GRCh38 Ensembl release 96) using Kallisto 56 with default parameters.
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [DESeq2, Seurat, fgsea] -> stage not stated [GSEA, ImageJ v1.52q, R]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Version used: **0.46.1**
- Evidence: Next, kallisto v.0.46.1 was used with a GRCh38 reference to generate the counts of reads mapped to each gene 44 , 45 .
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission. (Nature 2022)

- DOI: 10.1038/s41586-022-05049-6 | PMCID: PMC9433318 | PMID: 35798029
- Evidence: Deconvolution method performance comparison A subset of the spike-in mixtures (one of each type, for a total of 95 mixtures) was used to compare Freyja 34 , cojac (using VOC definitions from the public cojac GitHub repository; lineage A and Epsilon definitions were created manually), the Kallisto-based method from Baaijens et al.
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Python] -> stage not stated [SAMtools, kallisto]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Version used: **0.46.2**
- Evidence: Gene expression and metabolite contents To quantify the expression of all genes, we used Kallisto (v.0.46.2) 74 for all 51,155 gene models in the graph pangenome.
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Island-specific evolution of a sex-primed autosome in a sexual planarian. (Nature 2022)

- DOI: 10.1038/s41586-022-04757-3 | PMCID: PMC9177419 | PMID: 35650439
- Version used: **0.44.0**
- Evidence: Expression was quantified at the transcript level with kallisto (version 0.44.0) 56 and was imported and summarized to gene-level count matrices by tximport 57 .
- Full pipeline: variant calling [GATK v4.1.4.1] -> quantification [kallisto v0.44.0] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [ImageJ, RAxML v0.9.0, VCFtools v0.1.14]

### MCM complexes are barriers that restrict cohesin-mediated loop extrusion. (Nature 2022)

- DOI: 10.1038/s41586-022-04730-0 | PMCID: PMC9159944 | PMID: 35585235
- Evidence: RNA-seq analysis FASTQ files from sequencing mouse G1 zygotes or the human HCT116 cell line were pseudoaligned to the mm10 or hg38 releases of the Mus musculus or Homo sapiens genomes, respectively, using Kallisto with 100 bootstraps 64 .
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ, NumPy, Python, SciPy, ggplot2]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Version used: **0.46**
- Evidence: Genes were quantified using Kallisto release 0.46 (ref.
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: We used kallisto 96 with steps described in a previous study 51 to quantify the SMART-seq at the isoform level with the same GTF file used in transcriptome and methylome analysis above.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Glioma synapses recruit mechanisms of adaptive plasticity. (Nature 2023)

- DOI: 10.1038/s41586-023-06678-1 | PMCID: PMC10632140 | PMID: 37914930
- Evidence: NTRK2 isoform abundances were quantified from FASTQ files using Kallisto 62 (v.0.46.1).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [ImageJ v2.1.0, RSEM, featureCounts, kallisto] -> normalisation [RSEM] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.36.0] -> visualisation [ImageJ v2.1.0] -> stage not stated [R v4.1.1]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **0.46.0**
- Evidence: Trimmed reads were quantified by pseudoalignment to mm10 using Kallisto (v.0.46.0) 53 .
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Transgenic ferret models define pulmonary ionocyte diversity and function. (Nature 2023)

- DOI: 10.1038/s41586-023-06549-9 | PMCID: PMC10533402 | PMID: 37730992
- Evidence: Pseudo-alignment and unique molecular identifier (UMI)-collapsing were performed using the Kallisto toolkit (v.0.48) 46 .
- Full pipeline: alignment/mapping [kallisto] -> variant calling [UMAP] -> quantification [R, Seurat] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [brms] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Version used: **0.46.2**
- Evidence: RNA velocity To obtain count matrices for spliced and unspliced transcripts, we used kallisto (v.0.46.2) 63 through the command line tool loompy from fastq from the python package loompy (v.3.0.7; https://linnarssonlab.org/loompy/ ).
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: 26 , were realigned to the hg38 human genome using kallisto or kb-bustools 59 , 60 .
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Psychedelics reopen the social reward learning critical period. (Nature 2023)

- DOI: 10.1038/s41586-023-06204-3 | PMCID: PMC10284704 | PMID: 37316665
- Version used: **0.46.2**
- Evidence: 71 ) reference transcriptome using kallisto (v0.46.2) with 100 bootstrapped samples and 6 threads.
- Full pipeline: quantification [Bioconductor] -> stage not stated [kallisto v0.46.2]

### Ageing-associated changes in transcriptional elongation influence longevity. (Nature 2023)

- DOI: 10.1038/s41586-023-05922-y | PMCID: PMC10132977 | PMID: 37046086
- Version used: **0.42.5**
- Evidence: We estimated transcript counts using Kallisto version 0.42.5 for each sample.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.5.1b, Trimmomatic] -> quantification [StringTie] -> differential/statistical testing [DESeq2 v1.8.2, GSEA] -> stage not stated [kallisto v0.42.5]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **0.44.0**
- Evidence: Publicly available expression data 16 for nine diverse tissues of Hedin/2 were used to quantify gene expression using Kallisto v0.44.0 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **0.46.2**
- Evidence: Cleaned reads were pseudo-aligned to the filtered gene models using kallisto (v.0.46.2) 99 , and genes with an expression level above an empirically defined threshold of 2 transcripts per million (TPM) were deemed expressed.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Version used: **0.46.0**
- Evidence: RNA velocity calculation To obtain count matrices for the spliced and unspliced transcriptome, we used kallisto (v.0.46.0) 60 by running the command line tool loompy fromfastq from the Python package loompy (v.3.0.6) ( https://linnarssonlab.org/loompy/ ).
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: Gene expression was quantified as transcripts per million (TPM) using kallisto 128 (v.0.48.0) with 100 bootstraps.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Immune system adaptation during gender-affirming testosterone treatment. (Nature 2024)

- DOI: 10.1038/s41586-024-07789-z | PMCID: PMC11374716 | PMID: 39232147
- Evidence: Data analysis of bulk mRNA-seq data Bulk RNA-seq results from 59 samples from 20 individuals undergoing testosterone treatment were preprocessed with Kallisto 64 .
- Full pipeline: dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [Seurat, clusterProfiler, lme4] -> stage not stated [DESeq2, Python, Scanpy v1.9.1, Signac, kallisto]

### Probing plant signal processing optogenetically by two channelrhodopsins. (Nature 2024)

- DOI: 10.1038/s41586-024-07884-1 | PMCID: PMC11424491 | PMID: 39198644
- Evidence: Data processing (fastp) and mapping to the N. tabacum genome (kallisto) 75 was carried out using Amalgkit ( https://github.com/kfuku52/amalgkit ).
- Full pipeline: alignment/mapping [fastp, kallisto] -> normalisation [DESeq2] -> stage not stated [PyMOL, R, pheatmap]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **0.48.0**
- Evidence: For the isoform-level analysis of NECTIN1 , RNA-seq FASTQ files were pseudo-aligned with transcriptome indices (Ensembl release 110) with Kallisto (v.0.48.0) 65 .
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### A maternal brain hormone that builds bone. (Nature 2024)

- DOI: 10.1038/s41586-024-07634-3 | PMCID: PMC11306098 | PMID: 38987585
- Evidence: For all tissue samples, sequencing-generated reads were aligned to the mouse transcriptome (mm10) using Kallisto in gene mode 60 .
- Full pipeline: read trimming [RSEM v1.2.21, STAR v2.4] -> alignment/mapping [RSEM v1.2.21, STAR v2.4, kallisto] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy v1.9, scDblFinder]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Version used: **0.44.0**
- Evidence: Generation of gene set enrichment analysis signature The PLATE-Seq FASTQ files were pseudoaligned to the GRCh38 human transcriptome and gene expression was quantified using kallisto (version 0.44.0), tximport package 50 and biomaRt package 65 .
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### Stress response silencing by an E3 ligase mutated in neurodegeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06985-7 | PMCID: PMC10881396 | PMID: 38297121
- Version used: **0.48.0**
- Evidence: To obtain transcript abundance counts, sequencing reads were mapped to the human reference transcriptome (GRCh38, Ensembl Release 96) using Kallisto (v.0.48.0).
- Full pipeline: alignment/mapping [kallisto v0.48.0] -> quantification [kallisto v0.48.0] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, Cytoscape, Galaxy v2.11.40.7]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: Assemblies were generated for all 118 datasets using MegaHit 33 (v.1.1.4), and the resulting contigs were quantified in each assembly by mapping preprocessed reads to the assembled contigs using kallisto 34 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Determinants of successful AAV-vectored delivery of HIV-1 bNAbs in early life. (Nature 2025)

- DOI: 10.1038/s41586-025-09330-2 | PMCID: PMC12460164 | PMID: 40739359
- Evidence: After initial quality control, the sequence data were quantified using Kallisto 54 , to obtain transcript level abundances using Mmul_10 (Ensembl) as reference.
- Full pipeline: quality control [kallisto] -> quantification [kallisto]

### Precisely defining disease variant effects in CRISPR-edited single cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09313-3 | PMCID: PMC12488502 | PMID: 40702188
- Evidence: Kallisto kite (v.0.27.3) was used to build an ADT reference transcriptome corresponding to the ADT panel (Biolegend TotalSeq A) used and to align ADT reads 44 , 45 .
- Full pipeline: alignment/mapping [kallisto] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> stage not stated [GSEA, R, lme4]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: The cell feature matrices were extracted using kallisto/bustools, and demultiplexed using seurat.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: To quantify the abundances of transcripts from the bulk RNA-seq data, Kallisto pseudo alignment was applied 64 .
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: ... FastQC, and sequencing adaptors were removed using fastp 76 ; pseudoalignment and transcriptomic counts of the RNA-seq reads was performed using the Kallisto Bioconductor R package 77 with the GENCODE human genome build GRCh38.p13 (release 37) 78 ; differential expression using the generalized linear model as implemented by the edgeR Bioconductor R package 79 ; and Gene Ontology (GO) term pathway...
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: This alignment was carried out using the scKB script within the COPILOT preprocessing pipeline 9 , which integrates kallisto 39 and bustools 40 , 41 .
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **0.46.1**
- Evidence: Quality control of raw sequencing reads identified adaptor sequences from the Illumina Nextera platform in some samples, which were subsequently trimmed using Cutadapt (v.4.1) 61 . kallisto (v.0.46.1) 62 was used to quantify transcript-level expression by mapping to a transcript index built from GENCODE human transcript (v.44) 63 .
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: Transcripts were quantified by the alignment-free approach kallisto 63 using index generated from mouse reference genome (mm10) and then summed to obtain gene level counts.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Changes in neurotensin signalling drive hedonic devaluation in obesity. (Nature 2025)

- DOI: 10.1038/s41586-025-08748-y | PMCID: PMC12119351 | PMID: 40140571
- Version used: **0.45.1**
- Evidence: Bioinformatics After sequencing, raw reads were de-multiplexed using Illumina bc12fastq (version 2.20), and pseudo-aligned to the Ensembl GRCm38.95 reference transcriptome and normalized using kallisto (version 0.45.1).
- Full pipeline: alignment/mapping [kallisto v0.45.1] -> normalisation [kallisto v0.45.1] -> differential/statistical testing [edgeR v3.24.3] -> stage not stated [DeepLabCut, ImageJ, Python v3.6.7, R v3.5.1]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Version used: **0.44.0**
- Evidence: A pseudoalignment to a kallisto index was created from transcriptomes (human, GRCh38; mouse, GRCm38) using kallisto (v.0.44.0).
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Version used: **0.46.1**
- Evidence: To estimate CAZyme gene abundance, metagenomic reads were mapped to MAG gene sets using Kallisto v.0.46.1 with quant function 53 and normalized abundance was expressed as transcripts per million (TPM).
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Raw sequences were quantified and annotated using Kallisto 63 and GRCm38 (mm10) cDNA assembly 64 .
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **0.46.1**
- Evidence: Differential expression analysis Raw fastq files, containing an average of 20–30 million reads per sample, were processed for pseudoalignment and abundance quantification using Kallisto (v0.46.1) against the Ensembl Mus musculus reference (v79) 67 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Evidence: The reads were pseudoaligned on the human transcriptome database (hg38) with the Kallisto pipeline and final TPM values for each gene in each sample were received as described 55 .
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Version used: **0.46.0**
- Evidence: Raw reads were mapped to the mouse reference transcriptome (GRCm38) using Kallisto v.0.46.0 (ref.
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Evidence: Finally, reads were aligned to the HuvaT2T genome using the Kallisto pseudoalignment program (v.0.46.0) and data were analysed in the sleuth tool (v.0.30.0).
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: The data for each line were aligned to the relevant reference genome using Kallisto 68 (v.0.48; Supplementary Figs.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### The cyclic dinucleotide 2'3'-cGAMP induces a broad antibacterial and antiviral response in the sea anemone &lt;i&gt;Nematostella vectensis&lt;/i&gt;. (PNAS 2021)

- DOI: 10.1073/pnas.2109022118 | PMCID: PMC8713801 | PMID: 34903650
- Evidence: Reads were mapped to the N. vectensis transcriptome (NCBI: GCF_000209225.1) using kallisto, and differential expression was analyzed in R with DESeq2.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Clustal Omega, DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **0.43.1**
- Evidence: For quality filtering of the resulting transcriptomes, the trimmed RNA-seq reads were mapped back against the transcriptomes using Kallisto v0.43.1 ( 77 ) with options–bias and–rf-stranded, then transcripts with at least 1 TPM in any samples were retained.
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### AGO2 promotes tumor progression in KRAS-driven mouse models of non-small cell lung cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2026104118 | PMCID: PMC8157917 | PMID: 33972443
- Evidence: Transcripts were quantified by pseudoalignment algorithm Kallisto ( 53 ) with mm10 as the reference genome.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> differential/statistical testing [fgsea, limma] -> stage not stated [GSEA]

### Fast and pervasive transcriptomic resilience and acclimation of extremely heat-tolerant coral holobionts from the northern Red Sea. (PNAS 2021)

- DOI: 10.1073/pnas.2023298118 | PMCID: PMC8126839 | PMID: 33941698
- Version used: **0.44.0**
- Evidence: In order to confirm this, filtered reads of the 80 libraries were pseudoaligned to this reference composite transcriptome with Kallisto (0.44.0) ( 34 ).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, Trimmomatic v0.36, kallisto v0.44.0] -> alignment/mapping [R v3.5.2, kallisto v0.44.0] -> variant calling [vegan] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [MultiQC, ggplot2] -> stage not stated [BCFtools, DADA2, SAMtools v1.8]

### An ancient, conserved gene regulatory network led to the rise of oral venom systems. (PNAS 2021)

- DOI: 10.1073/pnas.2021311118 | PMCID: PMC8040605 | PMID: 33782124
- Evidence: We used the “fasterq-dump” function in SRA toolkit 2.9.1 ( https://github.com/ncbi/sra-tools/wiki ) to download fastq files, which were quantified using kallisto ( 94 ).
- Full pipeline: alignment/mapping [Bowtie2, RSEM] -> quantification [Bowtie2, RSEM, kallisto] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [edgeR] -> stage not stated [OrthoFinder, R, WGCNA]

### Long-read assembly of a Great Dane genome highlights the contribution of GC-rich sequence and mobile elements to canine genomes. (PNAS 2021)

- DOI: 10.1073/pnas.2016274118 | PMCID: PMC7980453 | PMID: 33836575
- Version used: **0.46.0**
- Evidence: Expression levels for each of the 22,182 protein-coding gene models were estimated using Kallisto (version 0.46.0) ( 94 ).
- Full pipeline: alignment/mapping [Canu v1.3, Cufflinks v2.2.1, minimap2 v2.9] -> stage not stated [RepeatMasker v4.0.7, kallisto v0.46.0]

### High-salt diet suppresses autoimmune demyelination by regulating the blood-brain barrier permeability. (PNAS 2021)

- DOI: 10.1073/pnas.2025944118 | PMCID: PMC7999868 | PMID: 33723078
- Version used: **0.46.1**
- Evidence: Pseudoalignment and gene-level quantification were performed with Kallisto (version 0.46.1) ( 33 ); Mus musculus genome assembly version mm10/GRCm38 was used for indexing with 100 bootstraps.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [DESeq2 v1.26.1, kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.1, clusterProfiler v3.14.3, limma] -> visualisation [pheatmap, tidyverse]

### Lipid droplets in mammalian eggs are utilized during embryonic diapause. (PNAS 2021)

- DOI: 10.1073/pnas.2018362118 | PMCID: PMC7958255 | PMID: 33649221
- Evidence: The reads mapped to separate genes were counted using HTSeq software [with “Union” mode ( 45 )], and for additional verification, pseudoalignment with the use of Kallisto was performed as well ( 46 ).
- Full pipeline: quality control [FastQC, TopHat] -> read trimming [FastQC, TopHat] -> alignment/mapping [FastQC, HTSeq, TopHat, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ]

### Sunlight exposure exerts immunomodulatory effects to reduce multiple sclerosis severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018457118 | PMCID: PMC7817192 | PMID: 33376202
- Evidence: Bioinformatic analysis was done in R using Kallisto and edgeR .
- Full pipeline: quality control [PLINK v1.90] -> variant calling [PLINK v1.90] -> differential/statistical testing [R v3.6, lme4] -> visualisation [ggplot2] -> stage not stated [edgeR, kallisto]

### Decorating chromatin for enhanced genome editing using CRISPR-Cas9. (PNAS 2022)

- DOI: 10.1073/pnas.2204259119 | PMCID: PMC9894255 | PMID: 36459645
- Version used: **0.48.0**
- Evidence: Transcripts per million for each gene were determined with Kallisto (version 0.48.0) using the GRCh38 reference transcriptome and a kmer size of 31.
- Full pipeline: stage not stated [kallisto v0.48.0]

### Transcriptome-based molecular subtypes and differentiation hierarchies improve the classification framework of acute myeloid leukemia. (PNAS 2022)

- DOI: 10.1073/pnas.2211429119 | PMCID: PMC9894241 | PMID: 36442087
- Version used: **0.46.2**
- Evidence: Raw RNA-Seq reads counts were extracted by both genome alignment-based Featurecounts v2.0.1 ( 40 ) and Htseq v0.11.3 ( 41 ) and alignment-free methods salmon v1.2.1 ( 42 ) and Kallisto v0.46.2 ( 43 ).
- Full pipeline: alignment/mapping [kallisto v0.46.2] -> quantification [DESeq2 v1.28.0] -> normalisation [DESeq2 v1.28.0] -> dimensionality reduction/clustering [ComplexHeatmap] -> machine learning [Python]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: Reads were assigned to each variant using Kallisto ( 40 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Balanced control of thermogenesis by nuclear receptor corepressors in brown adipose tissue. (PNAS 2022)

- DOI: 10.1073/pnas.2205276119 | PMCID: PMC9388101 | PMID: 35939699
- Evidence: Briefly, this pipeline uses Kallisto to align and quantify reads, EnemblDB to annotate data, edgeR to normalize read counts, and Limma to determine differentially expressed genes (DEGs).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, edgeR, kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR, kallisto] -> differential/statistical testing [R v4.1, edgeR, kallisto] -> stage not stated [Enrichr, SAMtools]

### Microenvironmental sensing by fibroblasts controls macrophage population size. (PNAS 2022)

- DOI: 10.1073/pnas.2205360119 | PMCID: PMC9371703 | PMID: 35930670
- Evidence: Illumina fastq files were downloaded from Illumina Basespace and were aligned with Kallisto program with default settings ( 77 ) against all cDNA transcripts in mouse genome annotation GRCm38 ( ftp://ftp.ensembl.org/pub/release-90/fasta/mus_musculus/cdna/ ).
- Full pipeline: alignment/mapping [kallisto] -> stage not stated [MACS2, Picard]

### Organellar transcripts dominate the cellular mRNA pool across plants of varying ploidy levels. (PNAS 2022)

- DOI: 10.1073/pnas.2204187119 | PMCID: PMC9335225 | PMID: 35858449
- Evidence: Reads from all three species (one allopolyploid and diploid models of both the maternal and paternal progenitors) within each genus were mapped to the annotated protein-coding sequences from the polyploid nuclear genome and from the organellar genomes of a representative member of the genus using Kallisto ( 68 ), as described elsewhere ( 58 ).
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R v3.5, emmeans] -> visualisation [ggplot2] -> stage not stated [lme4]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Version used: **0.42.5**
- Evidence: For all RNA-seq datasets, reads were mapped to the 54,718 gene models (see above), using kallisto v.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Kallisto was used to quantify transcripts against a joint reference of GRCh38 Ensembl transcripts and Repbase consensus sequences for repeats.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### Gain of gene regulatory network interconnectivity at the origin of vertebrates. (PNAS 2022)

- DOI: 10.1073/pnas.2114802119 | PMCID: PMC8931241 | PMID: 35263228
- Evidence: In the case of P. flava and X. tropicalis , reads were pseudoaligned to the set of longest isoforms of the currently available transcriptome of P. flava ( 46 ) and to the set of primary coding DNA sequences of the XenTrop v10.0 transcriptome ( 47 ), respectively, using Kallisto with standard parameters ( 48 ).
- Full pipeline: alignment/mapping [Bowtie2, HTSeq, STAR v2.5.3a, kallisto] -> differential/statistical testing [DESeq2 v1.18.0, R v3.4] -> stage not stated [Cytoscape]

### <i>Arabidopsis</i> TBP-ASSOCIATED FACTOR 12 ortholog NOBIRO6 controls root elongation with unfolded protein response cofactor activity. (PNAS 2022)

- DOI: 10.1073/pnas.2120219119 | PMCID: PMC8833210 | PMID: 35115407
- Evidence: Clean reads were aligned to the Arabidopsis reference genome from Araport11 ( 49 ) with a Kallisto–Sleuth pipeline (v0.44.0) ( 50 ) for identifying DEGs.
- Full pipeline: alignment/mapping [kallisto] -> stage not stated [ImageJ v1.53g]

### The dynamic trophic architecture of open-ocean protist communities revealed through machine-guided metatranscriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2100916119 | PMCID: PMC8851463 | PMID: 35145022
- Evidence: The contig abundances were quantified by the pseudoalignment of the paired reads to the assemblies with kallisto ( 70 ) and normalized to the total assigned read pool of the taxonomic bin.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> normalisation [Trimmomatic v0.36, kallisto] -> differential/statistical testing [DESeq2] -> machine learning [XGBoost] -> stage not stated [HMMER v3.1b]

### Natural disaster and immunological aging in a nonhuman primate. (PNAS 2022)

- DOI: 10.1073/pnas.2121663119 | PMCID: PMC8872742 | PMID: 35131902
- Evidence: We mapped cDNA reads to the M. mulatta reference assembly Mmul_10 using kallisto ( 75 ) (average mapping rate = 71.1%).
- Full pipeline: alignment/mapping [ANGSD, kallisto] -> quantification [limma] -> normalisation [limma] -> differential/statistical testing [R v4.0.2] -> stage not stated [HOMER, Seurat]

### Tracing the cis-regulatory changes underlying the endometrial control of placental invasion. (PNAS 2022)

- DOI: 10.1073/pnas.2111256119 | PMCID: PMC8832988 | PMID: 35110402
- Evidence: A transcript-based quantification approach was used to analyze RNA sequencing (RNA-seq) data using the program kallisto ( 55 ).
- Full pipeline: quantification [kallisto]

### Electrophysiological measures from human iPSC-derived neurons are associated with schizophrenia clinical status and predict individual cognitive performance. (PNAS 2022)

- DOI: 10.1073/pnas.2109395119 | PMCID: PMC8784142 | PMID: 35017298
- Evidence: ERCC spike-in sequences were quantified with kallisto ( 55 ), and we further calculated a bias factor for each sample using the observed versus expected abundances [∑((obs − exp)^2)].
- Full pipeline: alignment/mapping [HISAT2 v2.0.4] -> variant calling [SAMtools] -> quantification [featureCounts v1.5.0, kallisto] -> dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [limma]

### Sex-specific splicing of Z- and W-borne <i>nr5a1</i> alleles suggests sex determination is controlled by chromosome conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2116475119 | PMCID: PMC8795496 | PMID: 35074916
- Evidence: In short, P. vitticeps genome Pvi1.1 ( 28 ) and accompanying gene annotation ( http://gigadb.org/dataset/100166 ) were used to derive gene expression values with Kallisto ( 67 ) using a fixed k-mer length of 30 nt.
- Full pipeline: alignment/mapping [BWA, Clustal Omega] -> quantification [DESeq2 v1.26.0] -> dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R, kallisto]

### Convergent evolution of venom gland transcriptomes across Metazoa. (PNAS 2022)

- DOI: 10.1073/pnas.2111392119 | PMCID: PMC8740685 | PMID: 34983844
- Evidence: Raw fastq files were filtered with trimmomatic ( 37 ), their quality checked with fastQC ( 38 ), and quantified with kallisto ( 39 ) using default parameters for paired-end reads and parameters -l 55 -s 1e-08 for single-end reads.
- Full pipeline: quality control [kallisto] -> read trimming [kallisto] -> alignment/mapping [RAxML] -> quantification [kallisto] -> normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR] -> stage not stated [Bioconductor, InterProScan]

### Antigen perception in T cells by long-term Erk and NFAT signaling dynamics. (PNAS 2023)

- DOI: 10.1073/pnas.2308366120 | PMCID: PMC10756264 | PMID: 38113261
- Version used: **0.46.1**
- Evidence: Alignment to the GRCm38/mm10 reference genome was done with Kallisto (v0.46.1) ( 93 ).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [Monocle v1.2.9] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle v1.2.9]

### Adenylate kinase 9 is essential for sperm function and male fertility in mammals. (PNAS 2023)

- DOI: 10.1073/pnas.2305712120 | PMCID: PMC10589668 | PMID: 37812723
- Evidence: The number of reads covering a genomic position was extracted from coordinate sorted STAR-aligned BAM files and subsequently divided by the total number of unique reads that were pseudoaligned during transcript abundance estimation with kallisto.
- Full pipeline: alignment/mapping [kallisto] -> quantification [kallisto]

### A PAX6-regulated receptor tyrosine kinase pairs with a pseudokinase to activate immune defense upon oomycete recognition in <i>Caenorhabditis elegans</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2300587120 | PMCID: PMC10523662 | PMID: 37725647
- Evidence: Kallisto ( 60 ) was used for alignments with the WS283 transcriptome from Wormbase.
- Full pipeline: alignment/mapping [kallisto]

### Evolutionarily diverse origins of deformed wing viruses in western honey bees. (PNAS 2023)

- DOI: 10.1073/pnas.2301258120 | PMCID: PMC10293827 | PMID: 37339224
- Evidence: In addition, we quantified viral abundances using Kallisto ( 32 ) on raw reads mapped to reference viral genomes using the set of viral genomes from ref.
- Full pipeline: alignment/mapping [Bowtie2, kallisto] -> quantification [kallisto] -> differential/statistical testing [vegan] -> structure determination [BEAST v2.6] -> stage not stated [BCFtools, SAMtools, VCFtools, VarScan]

### Nontriplet feature of genetic code in &lt;i&gt;Euplotes&lt;/i&gt; ciliates is a result of neutral evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2221683120 | PMCID: PMC10235951 | PMID: 37216548
- Evidence: For the expression analyses, the expression rate of each transcript was calculated as Transcripts Per Million (TPM) using the Kallisto software with the default parameters ( 107 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [kallisto] -> stage not stated [BLAST]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: Kallisto was used to quantify transcript abundance using AB856846.1 for the Sendai genome.
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### Two differentially stable rDNA loci coexist on the same chromosome and form a single nucleolus. (PNAS 2023)

- DOI: 10.1073/pnas.2219126120 | PMCID: PMC9992848 | PMID: 36821584
- Evidence: RNA sequencing analysis was performed as previously described ( 54 ) using kallisto/sleuth suite with minor modifications.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [Bowtie2] -> visualisation [ImageJ] -> stage not stated [kallisto]

### In vivo expression vector derived from anhydrobiotic tardigrade genome enables live imaging in Eutardigrada. (PNAS 2023)

- DOI: 10.1073/pnas.2216739120 | PMCID: PMC9945988 | PMID: 36693101
- Evidence: Expression levels were computed as transcripts per million (TPM) using kallisto software (v.0.46.1) ( 57 ).
- Full pipeline: quantification [kallisto]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: This pipeline uses kallisto, bustools, busparse, and BSgenome ( 59 – 62 ) to align and quantify counts to the Arabidopsis TAIR10 genome.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### Spaceflight-induced contractile and mitochondrial dysfunction in an automated heart-on-a-chip platform. (PNAS 2024)

- DOI: 10.1073/pnas.2404644121 | PMCID: PMC11459163 | PMID: 39312653
- Evidence: The reads were aligned to the prebuilt Ensembl Transcriptome v96 using Kallisto ( 86 ) and differential expression between the EHTs from space flight and ground control groups was analyzed using DESeq2 ( 87 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [ImageJ]

### Cone photoreceptor differentiation regulated by thyroid hormone transporter MCT8 in the retinal pigment epithelium. (PNAS 2024)

- DOI: 10.1073/pnas.2402560121 | PMCID: PMC11287251 | PMID: 39018199
- Version used: **0.46.0**
- Evidence: To compare transcript abundance, data were quantified using Kallisto (v0.46.0) as transcripts per million reads (TPM).
- Full pipeline: alignment/mapping [STAR v2.7.10b, featureCounts] -> quantification [kallisto v0.46.0] -> normalisation [featureCounts] -> stage not stated [ImageJ]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles up-regulate and directly transfer adherence factors promoting host cell colonization. (PNAS 2024)

- DOI: 10.1073/pnas.2401159121 | PMCID: PMC11194581 | PMID: 38865261
- Evidence: After read mapping with Kallisto ( 73 ), version 0.46.2, TxImport ( 74 ) was used to read Kallisto outputs into the R environment.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [Galaxy]

### Long noncoding RNA LIRIL2R modulates FOXP3 levels and suppressive function of human CD4<sup>+</sup> regulatory T cells by regulating IL2RA. (PNAS 2024)

- DOI: 10.1073/pnas.2315363121 | PMCID: PMC11161746 | PMID: 38805281
- Evidence: The data were pseudoaligned with kallisto ( 55 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9] -> alignment/mapping [Bowtie2 v2.3.5.1, Picard, SAMtools v1.9, kallisto] -> differential/statistical testing [R, limma v3.42.2] -> stage not stated [GSEA]

### Nutrient-derived signals regulate eosinophil adaptation to the small intestine. (PNAS 2024)

- DOI: 10.1073/pnas.2316446121 | PMCID: PMC10835075 | PMID: 38271336
- Evidence: Trimmed and processed sequencing reads were pseudoaligned to the mouse mm10 genome build using Kallisto ( 71 ).
- Full pipeline: read trimming [kallisto] -> alignment/mapping [kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [R]

### Glycoside hydrolase-mediated glucomannan catabolism in &lt;i&gt;Segatella copri&lt;/i&gt;, a target of microbiota-directed foods for malnourished children. (PNAS 2025)

- DOI: 10.1073/pnas.2521522122 | PMCID: PMC12704710 | PMID: 41329729
- Evidence: The resulting reads were subjected to routine quality control, mapped to the S. copri BgF5_2 genome using kallisto ( 46 ), and differential expression was determined for individual genes (DESeq2, ref.
- Full pipeline: quality control [DESeq2, kallisto] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [AlphaFold, GSEA, fgsea]

### Exceptional diversity of allorecognition receptors in a nonvertebrate chordate reveals principles of innate allelic discrimination. (PNAS 2025)

- DOI: 10.1073/pnas.2519372122 | PMCID: PMC12582321 | PMID: 41129228
- Evidence: Raw reads were mapped to FF and FcoR genes using Kallisto and RSEM ( 70 ).
- Full pipeline: alignment/mapping [RSEM, kallisto] -> stage not stated [AlphaFold]

### BTK autoinhibition analyzed by high-throughput swaps of SH2 domains. (PNAS 2025)

- DOI: 10.1073/pnas.2502688122 | PMCID: PMC12541323 | PMID: 41071658
- Evidence: Briefly, Fastq files from MiSeq runs were aligned to the Fasta files containing the full sequences of each variant using Kallisto ( 36 ) to generate read counts for each variant.
- Full pipeline: alignment/mapping [kallisto] -> quantification [kallisto]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: Next, pseudoalignment to the mouse mm10 genome was performed with Kallisto, followed by aggregation of reads by replicate to create a single read counts matrix.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### &lt;i&gt;Sox11&lt;/i&gt; genes affect neuronal differentiation in the developing zebrafish enteric nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2510548122 | PMCID: PMC12342651 | PMID: 40789027
- Evidence: The reads of five libraries generated from ENS cells collected at 2, 3, 4, 5, and 6 dpf were mapped using Kallisto and bustools programs 81,82 to the reference transcriptome based on zebrafish genome assembly GRCz10, and the gene-cell matrices were generated separately.
- Full pipeline: alignment/mapping [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Python, Scanpy]

### Macroevolutionary changes in natural selection on codon usage reflect evolution of the tRNA pool across a budding yeast subphylum. (PNAS 2025)

- DOI: 10.1073/pnas.2419889122 | PMCID: PMC12260425 | PMID: 40591602
- Evidence: Briefly, adapters for each sequence were trimmed using fastp ( 52 ), and genes were quantified using kallisto ( 53 ).
- Full pipeline: read trimming [fastp, kallisto] -> quantification [fastp, kallisto] -> visualisation [ComplexHeatmap] -> stage not stated [R]

### Genetic ancestry shapes dengue virus infection in human skin explants. (PNAS 2025)

- DOI: 10.1073/pnas.2502793122 | PMCID: PMC12280909 | PMID: 40587809
- Evidence: The resulting cleaned fastq read files were used as input to the Kallisto package and used together with an indexed human GRCh38 transcriptome reference (EnsDb.Hsapiens.v105) to produce a pseudoaligned transcript abundance file for each sample.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [kallisto] -> quantification [edgeR, kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0] -> differential/statistical testing [limma] -> stage not stated [Cytoscape v3.9.1, GSEA, R, fgsea]

### &lt;i&gt;Trichomonas vaginalis&lt;/i&gt; extracellular vesicles suppress IFNε-mediated responses driven by its intracellular bacterial symbiont &lt;i&gt;Mycoplasma hominis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2508297122 | PMCID: PMC12232435 | PMID: 40560611
- Evidence: After read mapping with Kallisto ( 87 ), version 0.46.2, TxImport ( 88 ) was used to read Kallisto outputs into the R environment.
- Full pipeline: quality control [MultiQC] -> read trimming [edgeR] -> alignment/mapping [MultiQC, kallisto] -> quantification [edgeR] -> normalisation [edgeR, limma] -> differential/statistical testing [Bioconductor v3.8, R v4.3.0, limma] -> stage not stated [GSEA]

### Defining CDK12 as a tumor suppressor and therapeutic target in mouse models of tubo-ovarian high-grade serous carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2426909122 | PMCID: PMC12184368 | PMID: 40504161
- Evidence: Transcripts were quantified by alignment-free approach kallisto ( 25 ) using index generated from the mouse reference genome (mm10) and then summed to obtain gene-level counts.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, kallisto] -> quantification [kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [Cutadapt, GSEA, GSVA, fgsea]

### Anthropogenic iron alters the spring phytoplankton bloom in the North Pacific transition zone. (PNAS 2025)

- DOI: 10.1073/pnas.2418201122 | PMCID: PMC12168011 | PMID: 40455985
- Evidence: Transcript abundance of the selected environmental sequences was obtained from kallisto quantification ( 68 ) against the assembled metatranscriptomes.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [kallisto] -> stage not stated [HMMER v3.1b, RAxML]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Version used: **0.46.0**
- Evidence: Reads containing adapters were removed using Cutadapt version 2.4 ( 95 ) and reads were mapped to the D. melanogaster transcriptome, FlyBase genome release 6.29, using Kallisto (version 0.46.0) ( 96 ) with default parameters.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Hygrometrically controlled programmed cell death drives anther opening and pollen release. (PNAS 2025)

- DOI: 10.1073/pnas.2420132122 | PMCID: PMC12107150 | PMID: 40377996
- Version used: **0.48.0**
- Evidence: The set of RNA-seq libraries from 12 different stages of A. thaliana anther, three transcriptomes of mature pollen, and one transcriptome of filament was obtained from the ENA repository (in total 22, 10, and 2 libraries, Dataset S4 ) and quantified by Kallisto 0.48.0 using Araport11 representative CDS model as a reference ( Dataset S5 ).
- Full pipeline: quantification [kallisto v0.48.0] -> differential/statistical testing [R] -> stage not stated [emmeans]

### Coding relationship links RNA G-quadruplexes and protein RGG motifs in RNA-binding protein autoregulation. (PNAS 2025)

- DOI: 10.1073/pnas.2413721122 | PMCID: PMC11789052 | PMID: 39847338
- Version used: **0.50.1**
- Evidence: For RT-stop profiling, raw sequencing reads were quantified using kallisto (v0.50.1) ( 70 ) and transcript abundances (in TPM) were summed to obtain gene abundances.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [featureCounts, kallisto v0.50.1]

### Escalation of genome defense capacity enables control of an expanding meiotic driver. (PNAS 2025)

- DOI: 10.1073/pnas.2418541122 | PMCID: PMC11745323 | PMID: 39772737
- Evidence: For D. melanogaster , transcripts from two biological replicates per genotype were quantified by kallisto ( 54 ), using an index file that combines the transcriptome and repeat sequences from RepBase.
- Full pipeline: read trimming [Cutadapt] -> variant calling [kallisto] -> quantification [kallisto] -> differential/statistical testing [DESeq2]

### Genome-wide analysis of mRNA regionalization in a giant single cell. (PNAS 2026)

- DOI: 10.1073/pnas.2537760123 | PMCID: PMC13291615 | PMID: 42296355
- Evidence: We used kallisto ( 32 ) to generate a reference index of predicted protein coding genes and quantify transcript abundance ( SI Appendix , Table S1 ), sleuth to prepare the data ( 33 ), ComBat ( 34 ) to batch correct raw estimated counts ( SI Appendix , Table S2 ), and pydeseq2 ( 35 ) to perform differential enrichment analysis with a permissive q-value cutoff for significance of 0.2 ( SI Appendix ...
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [kallisto] -> normalisation [kallisto] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [kallisto]

### Functional role of small extrachromosomal circular DNA in colorectal cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523047123 | PMCID: PMC13056112 | PMID: 41926541
- Version used: **0.50.1**
- Evidence: RNA expression was quantified using Kallisto v0.50.1 with differential expression analysis by DESeq2.
- Full pipeline: quantification [DESeq2, kallisto v0.50.1] -> differential/statistical testing [DESeq2, kallisto v0.50.1] -> stage not stated [CNVkit v0.9.9, Python, R v4.1]

### Cell type diversification and phenotype convergence underlying white fin-ornamentation of cyprinid fishes. (PNAS 2026)

- DOI: 10.1073/pnas.2537571123 | PMCID: PMC13037925 | PMID: 41875157
- Evidence: Cells were collected by fluorescence-activated cell sorting and replicate libraries prepared for sequencing, mapped by Kallisto ( 88 ), and analyzed with DEseq2 ( 89 ).
- Full pipeline: alignment/mapping [kallisto]

### Synthetic lethality between RB-loss and E2F3 inhibition in small cell cancers targeted by pyrimidine synthesis blockade. (PNAS 2026)

- DOI: 10.1073/pnas.2532814123 | PMCID: PMC13012052 | PMID: 41860961
- Version used: **0.50.1**
- Evidence: Reads were aligned to the GRCh38 human genome using STAR (v2.7.10b) with the parameter “--twopassMode Basic.” Transcripts were quantified with Kallisto (v0.50.1) with default parameters, and splicing events were quantified with rMATS-turbo (v4.2.0) with default parameters ( 66 ).
- Full pipeline: alignment/mapping [STAR v2.7.10b, kallisto v0.50.1] -> quantification [STAR v2.7.10b, kallisto v0.50.1]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Evidence: Loading into the Chromium chip and processing for scRNA-Seq was done as above. scRNA-Seq reads were aligned to the genome using kallisto bustools [kb count with default arguments; kb_python v0.27.1; kallisto: v0.48.0; bustools: v0.41.0; ( 42 , 43 )].
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Differential disease tolerance mediates sex-biased illness severity in sepsis. (PNAS 2026)

- DOI: 10.1073/pnas.2522764123 | PMCID: PMC12956862 | PMID: 41734079
- Version used: **0.46.1**
- Evidence: Raw sequencing reads were pseudoaligned to the Mus musculus reference transcriptome GRCm39 using kallisto (v0.46.1).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [GSEA, MACS2, R v4.5.0, fgsea v1.34.0]

### INDETERMINATE DOMAIN-DELLA protein interactions orchestrate gibberellin-mediated cell elongation in wheat and barley. (PNAS 2026)

- DOI: 10.1073/pnas.2528934123 | PMCID: PMC12867750 | PMID: 41615756
- Evidence: Sequencing reads were trimmed for quality and adapter sequences using Trimmomatic 0.39 (parameters SLIDINGWINDOW:4:20; MINLEN:50) ( 49 ), then aligned and quantified using Kallisto against the IWGSC RefSeq v1.2 annotated gene models ( 47 , 50 ).
- Full pipeline: read trimming [Trimmomatic v0.39, kallisto] -> alignment/mapping [Bowtie2, Trimmomatic v0.39, kallisto] -> quantification [Trimmomatic v0.39, kallisto] -> stage not stated [BLAST, ImageJ v1.48v]

### Dietary folic acid prevents peripheral neuropathy in mouse models of neural tube defects and type 2 diabetes. (PNAS 2026)

- DOI: 10.1073/pnas.2528095123 | PMCID: PMC12773702 | PMID: 41481435
- Version used: **0.46.1**
- Evidence: Trimmed reads were pseudoaligned to the GRCm39 mouse reference genome assembly (GENCODE release M31) and gene expression levels were quantified using Kallisto v0.46.1 ( 66 ).
- Full pipeline: read trimming [fastp v0.20, kallisto v0.46.1] -> alignment/mapping [kallisto v0.46.1] -> quantification [kallisto v0.46.1] -> dimensionality reduction/clustering [clusterProfiler v4.8.1] -> differential/statistical testing [R v3.42.2, edgeR v3.42.2] -> stage not stated [ImageJ]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: Gene quantification based on the ARAPORT11 transcriptome was performed using kallisto quant (0.46.1) ( 65 ), with -b 100 and estimating -l 50 and -s 20 for single-end libraries.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### Base editing rescue of spinal muscular atrophy in cells and in mice. (Science 2023)

- DOI: 10.1126/science.adg6518 | PMCID: PMC10270003 | PMID: 36996170
- Evidence: Trimmed reads were aligned to the GENCODE mouse reference genome M31 (GRCm39) using STAR (v2.7.10a), quantified using kallisto( 127 ), and refined to canonical coding sequences using CCDS release 21( 128 ).
- Full pipeline: read trimming [STAR v2.7.10a, Trim Galore v0.6.7, kallisto] -> alignment/mapping [STAR v2.7.10a, kallisto] -> quantification [STAR v2.7.10a, kallisto] -> structure determination [STAR v2.7.10a, kallisto]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Evidence: Transcriptomic analysis Gene expression data for clinical P. aeruginosa strains (and the UCBPP- PA14 wildtype control strain) was obtained ( 25 ), and pseudoaligned to strain-specific gene indices to produce abundance estimates using Kallisto ( 77 ).
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

### The immunopathological landscape of human pre-TCRα deficiency: From rare to common variants. (Science 2024)

- DOI: 10.1126/science.adh4059 | PMCID: PMC10958617 | PMID: 38422122
- Version used: **0.46.1**
- Evidence: Expression was estimated for five pre-TCRα isoforms, along with the full gene list in Ensembl v96, with kallisto v0.46.1, for each sample ( 51 ).
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, SAMtools v1.14] -> differential/statistical testing [R, tidyverse] -> visualisation [R, tidyverse] -> stage not stated [MACS2, Seurat v4.0.4, kallisto v0.46.1]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Version used: **0.46.1**
- Evidence: Alignment was performed using Kallisto (v0.46.1) to the mouse (mm10/GRCm38) or human (hg38/GRCh38) references( 50 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Intestinal mast cell-derived leukotrienes mediate the anaphylactic response to ingested antigens. (Science 2025)

- DOI: 10.1126/science.adp0246 | PMCID: PMC12513082 | PMID: 40773543
- Version used: **0.45.0**
- Evidence: Sequencing reads were aligned to the mouse transcriptome (GRCm38 ensembl v101; cDNA and ncRNA) and quantified by Kallisto (v0.45.0)( 94 ) with a k-mer index 25 and 60 bootstrapping.
- Full pipeline: quality control [R v4.3.3, Seurat] -> alignment/mapping [kallisto v0.45.0] -> quantification [kallisto v0.45.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [Monocle, ggplot2] -> stage not stated [QuPath]

