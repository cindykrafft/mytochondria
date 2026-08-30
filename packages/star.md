# STAR

- **Category:** genomics
- **Papers in survey:** 489
- **Journals:** Nature (238), PNAS (198), Cell (36), Science (17)
- **Years:** 2021 (42), 2022 (74), 2023 (99), 2024 (110), 2025 (108), 2026 (56)
- **Versions named:** 2.7.10a (26), 2.7.9a (23), 2.7.3a (19), 2.5.2b (14), 2.6.1d (13), 2.5.3a (11), 2.7.1a (11), 2.7.10b (10), 2.7.8a (10), 2.7.11b (9)
- **Pipeline stages it appears in:** alignment/mapping (474), read trimming (111), quantification (48), quality control (37), differential/statistical testing (18), normalisation (9), visualisation (5), dimensionality reduction/clustering (2), variant calling (2), structure determination (1), registration (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: COLON MAP scRNA-seq, alignment and droplet matrix generation We demultiplexed, aligned, and corrected the detected read counts of these libraries with the DropEst pipeline ( Petukhov et al., 2018 ), using the STAR aligner with the Ensembl reference genome ( Dobin et al., 2013 ), GRCh38 release 25.
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Microglia jointly degrade fibrillar alpha-synuclein cargo by distribution through tunneling nanotubes. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.007 | PMCID: PMC8527836 | PMID: 34555357
- Version used: **2.5.3a**
- Evidence: Reads were aligned with STAR (v2.5.3a) against the murine reference genome mm10.
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> dimensionality reduction/clustering [Cytoscape] -> stage not stated [CellProfiler, Fiji, ImageJ, ggplot2, tidyverse]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Evidence: Libraries were aligned using STAR within the Drop-Seq Computational Protocol ( https://github.com/broadinstitute/Drop-seq ) and implemented on Cumulus ( https://cumulus.readthedocs.io/en/latest/drop_seq.html , snapshot 9, default parameters) ( Macosko et al., 2015 ).
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: ...software version 9 GraphPad RRID: SCR_002798 R version 4.05 http://www.r-project.org N/A Seurat package version 4.0 Hao et al., 2021 RRID: SCR_007322 STAR aligner version 2.7.5 Dobin et al., 2013 RRID: SCR_015899 Other Adjusted Calories Diet (60% Fat Kcal, Irradiated) - High Fat Diet Envigo Teklad Diets Cat #TD.06414 Control Diet (10% Fat Kcal, Irradiated) Envigo Teklad Diets Cat #TD.150064 Resour...
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: Briefly, Hi-C reads were trimmed at MboI/DpnII recognition sites (GATC) and aligned to the human genome (GRCh38/hg38) using STAR ( Dobin et al., 2013 ), keeping only read pairs that both map to unique genomic locations for further analysis (MAPQ > 10).
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: ... algorithms Pole tracking analysis Mills et al., 2017 N/A MaxQuant Cox and Mann, 2008 RRID: SCR_014485 Perseus Tyanova and Cox, 2018 RRID: SCR_015753 STAR aligner Dobin et al., 2013 RRID: SCR_015899 CellRanger N/A RRID: SCR_017344 Cutadapt Martin, 2011 RRID: SCR_011841 RNA-SeQC DeLuca et al., 2012 RRID: SCR_005120 RSEM Li and Dewey, 2011 RRID: SCR_013027 Scanpy Wolf et al., 2018 RRID: SCR_018139 B...
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Osteoclasts recycle via osteomorphs during RANKL-stimulated bone resorption. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.002 | PMCID: PMC7938889 | PMID: 33636130
- Version used: **2.4.1**
- Evidence: Alignments were performed using STAR 2.4.1 ( Dobin et al., 2013 ) and expression count quantitated using RSEM ( Li and Dewey, 2011 ) using default parameters. scRNA-seq data normalization Noise reduction, highly variable genes determination and differential gene expression (DGE) analyses were performed using BASiCS package ( Vallejos et al., 2015 ; Vallejos et al., 2016 ) in R.
- Full pipeline: alignment/mapping [STAR v2.4.1] -> normalisation [STAR v2.4.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [RSEM, STAR v2.4.1] -> stage not stated [Cutadapt, ImageJ, MAGMA, ggplot2]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: The sequencing reads were adaptor and quality trimmed and then aligned to the human genome using the splice-aware STAR aligner and SNP calls were generated using the previously published protocol ( Blay et al., 2019 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Meta-analysis of tumor- and T cell-intrinsic mechanisms of sensitization to checkpoint inhibition. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.002 | PMCID: PMC7933824 | PMID: 33508232
- Evidence: FASTQ data underwent quality control and were aligned to the hg19 genome using STAR ( Dobin et al., 2013 ).
- Full pipeline: quality control [FastQC v0.11.5, STAR, Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [GATK, Picard v1.81, SAMtools v1.3.1, STAR] -> quantification [DESeq2, RSEM] -> normalisation [DESeq2, RSEM] -> differential/statistical testing [edgeR] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, R, VarScan v2.4.1, XGBoost]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Version used: **2.7.3a**
- Evidence: ...halo/; RRID: SCR_018350 bcl2fastq v2.20.0.422 Illumina https://support.illumina.com/sequencing/sequencing_software/bcl2fastq-conversion-software.html STAR v2.7.3a Dobin et al., 2013 https://github.com/alexdobin/STAR DESeq2 v1.24.0 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ComplexHeatMap v2.0.0 Gu et al., 2016 https://bioconductor.org/packages/release/bioc/ht...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Identification of Required Host Factors for SARS-CoV-2 Infection in Human Cells. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.030 | PMCID: PMC7584921 | PMID: 33147445
- Evidence: Reads were aligned to hg19 using STAR aligner in the Basespace RNA-Seq Alignment application (Illumina) and processed using DESeq2 ( Love et al., 2014 ).
- Full pipeline: read trimming [Cutadapt v1.13] -> alignment/mapping [STAR] -> stage not stated [DESeq2, GSEA, R, Seurat, fgsea]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Evidence: ...d Institute https://portals.broadinstitute.org/gpp/public/software/poolq/ Picard Tools v2.9.0 Broad Institute http://broadinstitute.github.io/picard/ STAR aligner v2.7.3a Dobin et al., 2013 N/A SAMTools v1.9 Li et al., 2009 N/A Trimmomatic v0.39 Bolger et al., 2014 N/A CRISPR screen analysis This paper https://github.com/PeterDeWeirdt/coronavirus_screen_analysis Resource Availability Lead Contact ...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### Post-gastrulation synthetic embryos generated ex utero from mouse naive ESCs. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.028 | PMCID: PMC9439721 | PMID: 35988542
- Version used: **2.4.2a**
- Evidence: Reads were mapped to genome mm10 using STAR v2.4.2a (parameters: –alignEndsType EndToEnd, –outFilterMismatchNoverLmax 0.05, –twopassMode Basic -alignSoftClipAtReferenceEnds no).
- Full pipeline: alignment/mapping [STAR v2.4.2a] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, R, Seurat, pheatmap]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Version used: **2.7.9a**
- Evidence: PRO-seq data were aligned and quantified using STAR (version 2.7.9a) with parameters alignEndsType=Local, outFilterMultimapNmax=20, outFilterScoreMinOverLread=0.3, and outFilterMatchNminOverLread=0.3.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Version used: **2.7.3**
- Evidence: Whole blood total RNA-seq analysis RNA-sequencing data processing We trimmed adaptor sequences using TrimGalore (v0.6.2, https://github.com/FelixKrueger/TrimGalore ), and aligned reads to the reference genome (GRCh38.100) using multi-sample 2-pass mapping with STAR v2.7.3 ( Dobin et al., 2013 ) (ENCODE Best Practices recommended parameters).
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...eforge.net/ RepeatMasker Institute for Systems Biology http://www.repeatmasker.org/ RSEM (v1.2.22) Li and Dewey, 2011 http://deweylab.github.io/RSEM/ STAR aligner software (2.5.1b) ENCODE https://www.encodeproject.org/software/star/ Prism Graphpad, https://www.graphpad.com/scientific-software/prism version 8.2.1 R R Core Team and R Foundation for Statistical Computing, https://www.r-project.org ve...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Early cellular mechanisms of type I interferon-driven susceptibility to tuberculosis. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.002 | PMCID: PMC10757650 | PMID: 38029747
- Evidence: Sequence reads were trimmed of adapter sequences and low quality nucleotides with Trimmomatic v.0.36 109 and then mapped to the Mus musculus GRCm38 reference genome with STAR aligner v.2.5.2b 110 .
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR, Trimmomatic v0.36] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Version used: **2.6.1d**
- Evidence: All FASTQ sequences passed quality control tests and were aligned with the GRCh38 reference genome with STAR (2.6.1d).
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Mechanopathology of biofilm-like Mycobacterium tuberculosis cords. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.016 | PMCID: PMC10642369 | PMID: 37865090
- Version used: **2.7.10b**
- Evidence: The quality of sequenced Fastq files were analyzed using FastQC (version 0.11.9) and reads were mapped on the ensemble C3HeB/FeJ mouse reference genome (version 1.108) using STAR (v2.7.10b).
- Full pipeline: quality control [Bioconductor, FastQC, GSEA, STAR v2.7.10b] -> alignment/mapping [STAR v2.7.10b] -> quantification [R, edgeR] -> stage not stated [ImageJ, MACS2]

### Arginine reprograms metabolism in liver cancer via RBM39. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.011 | PMCID: PMC10642370 | PMID: 37804830
- Evidence: Differential alternative splicing analysis Aligned bam files were generated from fastq files with STAR-aligner (STAR/2.7.9a-GCC-7.3.0-2.30).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ, R] -> normalisation [RSEM] -> differential/statistical testing [STAR, limma]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Version used: **2.7.10a**
- Evidence: The trimmed reads were aligned to the genome sequences of human (hg38, Ensembl release 106) and SARS-CoV-2 ( NC_045512.2 , GenBank: MN908947.3 ) using STAR (v2.7.10a) 87 with the parameters –outFilterScoreMinOverLread 0 --outFilterMatchNminOverLread 0 --outFilterMatchNmin 0 --outFilterType Normal --alignSoftClipAtReferenceEnds No --alignSJoverhangMin 8 --alignSJDBoverhangMin 1 --outFilterMismatchN...
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **2.7.9a**
- Evidence: 29 https://rdrr.io/github/tanaylab/metacell/ STAR 2.7.9a Dobin et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Humanized mouse liver reveals endothelial control of essential hepatic metabolic functions. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.017 | PMCID: PMC10544749 | PMID: 37562401
- Evidence: Raw sequencing reads were aligned to the human–mouse combined genome with STAR ( https://doi.org/10.1093/bioinformatics/bts635 ), annotated and counted with HTSeq ( https://doi.org/10.1093/bioinformatics/btu638 ), normalized using DESeq2 ( https://doi.org/10.1186/s13059-014-0550-8 ) and graphed using the Broad Institute Morpheus web tool.
- Full pipeline: alignment/mapping [DESeq2, HTSeq, STAR] -> normalisation [DESeq2, HTSeq, STAR] -> stage not stated [Seurat v3.2]

### Engineering RNA export for measurement and manipulation of living cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.013 | PMCID: PMC10528933 | PMID: 37437570
- Version used: **2.7.8a**
- Evidence: Preprocessing of sequencing data Reads from both exported and cellular RNA sequencing were aligned to a custom reference genome using STAR (2.7.8a) 80 with the ENCODE standard options except “--outFilterScoreMinOverLread 0.3 --outFilterMatchNminOverLread 0.3 –outFilterMismatchNmax 20 --outFilterMismatchNoverLmax 0.3 --alignSJoverhangMin 5 --alignSJDBoverhangMin 3”.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.8a] -> quantification [SciPy v1.4.1] -> normalisation [scikit-image v0.19.2] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.5] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [PyMOL]

### Sites of transcription initiation drive mRNA isoform selection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.012 | PMCID: PMC10228280 | PMID: 37178687
- Version used: **2.6.1b**
- Evidence: 91 https://github.com/alexdobin/STAR/blob/master/bin/Linux_x86_64/STARlong STAR v2.6.1b Dobin et al.
- Full pipeline: alignment/mapping [fastp] -> stage not stated [BEDTools v2.27.0, DESeq2, NanoPlot v1.29.1, R v4.1, SAMtools v1.12, STAR v2.6.1b, Seurat, deepTools v3.5.0, ggplot2, minimap2 v2.17, tidyverse]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Version used: **2.7.3a**
- Evidence: For each subject, the two FASTQ files generated were then mapped onto the human reference genome (Ensembl GRCh37 release 75) with STAR v.2.7.3a, in the two-pass mode 197 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: 54 https://satijalab.org/seurat/ STAR aligner Dobin et al.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: 110 Briefly, Cell Ranger mkfastq pipeline was used to demultiplex sample index reads to generate FASTQ files for each sequencing library, and then raw reads were aligned to the mm10 (GENCODE vM23/Ensembl 98) using STAR aligner with default parameters.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **2.7.1a**
- Evidence: 104 https://multiqc.info STAR v2.7.1a Dobin et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: ...CSC Genome Browser UCSC www.genome.ucsc.edu GENCODE (V43) GENCODE www.gencodegenes.org RSEM (v1.2.22) Li and Dewey 94 http://deweylab.github.io/RSEM/ STAR aligner software (2.5.1b) ENCODE https://www.encodeproject.org/software/star/ DAVID v6.8 Huang da et al.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Version used: **2.6.1d**
- Evidence: All FASTQ files passed quality control and were aligned with the GRCh38 reference genome with STAR (2.6.1d).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Version used: **2.7.0**
- Evidence: The high-quality reads were aligned to a Zon lab custom genome 8 using STAR 2.7.0 Spliced Transcripts Alignment tool.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Proximity-specific ribosome profiling reveals the logic of localized mitochondrial translation. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.002 | PMCID: PMC12650760 | PMID: 40876456
- Version used: **2.7.1a**
- Evidence: RNA-seq Raw sequencing reads were aligned to the human genome (GRCh38.99) using STAR 2.7.1a 72 and quantified using featureCounts 1.6.2 73 .
- Full pipeline: alignment/mapping [STAR v2.7.1a, TopHat v2.1.1, featureCounts v1.6.2] -> quantification [STAR v2.7.1a, featureCounts v1.6.2]

### Principles of cotranslational mitochondrial protein import. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.021 | PMCID: PMC12396113 | PMID: 40795856
- Version used: **2.7.10a**
- Evidence: ... > Bowtie2.report.txt Reads that did not align to ribosomal RNA sequences were mapped to human reference genome (GRCh38p13 downloaded from NCBI) with STAR 2.7.10a 58 using the following command: STAR –runThreadN 32 –genomeDir indexed_genome –readFilesIn infile.fastq.gz –outFilterMultimapNmax 1 –outFilterType BySJout –alignIntronMin 5 –outFileNamePrefix Prefix –outReadsUnmapped Fastx –outSAMtype BA...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.5, STAR v2.7.10a] -> stage not stated [AlphaFold, ColabFold]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: ...cquisition-and-analysis-software/metaxpress ; RRID:N/A STREME 5.5.5 (MEME suite) Bailey 49 https://meme-suite.org/meme/tools/streme ; RRID:SCR_001783 STAR aligner Dobin et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Global genetic interaction network of a human cell maps conserved principles and informs functional interpretation of gene co-essentiality profiles. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.044 | PMCID: PMC13281610 | PMID: 42049019
- Evidence: After checking the sequencing quality with FastQC (v.0.11.9), reads were aligned to human genome build hg38 with Gencode v32 gene annotations using the STAR short-read aligner (v.2.7.9a) using the following parameters: –outSAMtype BAM SortedByCoordinate –quantMode GeneCounts –sjdbGTFfile gencode.v25.annotation.gtf.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, STAR] -> variant calling [GATK] -> visualisation [Cytoscape] -> stage not stated [ANNOVAR, R, SciPy]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: ...plementary Table 15 ). scRNA-seq data processing, mapping and expression estimates To calculate expression estimates, mRNA-seq reads were mapped with STAR (spliced transcripts alignment to a reference, v.2.4.2a) 64 and processed with RSEM using the ‘single-cell-prior’ option (RNA-seq by expectation-maximization, v.1.2.25) 65 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### B cell-derived GABA elicits IL-10<sup>+</sup> macrophages to limit anti-tumour immunity. (Nature 2021)

- DOI: 10.1038/s41586-021-04082-1 | PMCID: PMC8599023 | PMID: 34732892
- Version used: **2.5.4b**
- Evidence: Sequencing data were mapped to the mouse genome (mm10 assembly from the UCSC Genome Browser; annotation refFlat from the UCSC Genome Browser) using STAR v.2.5.4b 50 .
- Full pipeline: alignment/mapping [STAR v2.5.4b] -> normalisation [DESeq2 v1.30.1]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Version used: **2.5.3**
- Evidence: Sequence alignment was performed using STAR v2.5.3 49 .
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Morphological diversity of single neurons in molecularly defined cell types. (Nature 2021)

- DOI: 10.1038/s41586-021-03941-1 | PMCID: PMC8494643 | PMID: 34616072
- Version used: **2.5.3**
- Evidence: After sequencing, raw data was quantified using STAR v2.5.3 61 and were aligned to both a Ref-Seq transcriptome index for the mm10 genome, and a custom index consisting of transgene sequences.
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [STAR v2.5.3] -> dimensionality reduction/clustering [R, UMAP, igraph]

### Human neocortical expansion involves glutamatergic neuron diversification. (Nature 2021)

- DOI: 10.1038/s41586-021-03813-8 | PMCID: PMC8494638 | PMID: 34616067
- Version used: **2.5.3**
- Evidence: Sequence alignment was performed using STAR v2.5.3 53 in two pass Mode.
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [ImageJ] -> dimensionality reduction/clustering [Seurat, UMAP, scikit-learn] -> visualisation [scikit-learn] -> stage not stated [statsmodels]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **2.7.3a**
- Evidence: After clipping, the paired-end reads were mapped using spliced transcripts alignment to a reference (STAR v2.7.3a, RRID SCR_015899) with default settings.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Biologically informed deep neural network for prostate cancer discovery. (Nature 2021)

- DOI: 10.1038/s41586-021-03922-4 | PMCID: PMC8514339 | PMID: 34552244
- Evidence: Adapters were trimmed with cutadapt v2.2 and reads were aligned using STAR aligner v2.7.2b 48 , 49 .
- Full pipeline: read trimming [Cutadapt v2.2, STAR] -> alignment/mapping [Cutadapt v2.2, RSEM, STAR] -> quantification [RSEM] -> stage not stated [SAMtools]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: Raw reads were aligned to the human transcriptome v.GRCh38-3.0.0 using STAR aligner (v.2.5.1b).
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### SARS-CoV-2 infection is effectively treated and prevented by EIDD-2801. (Nature 2021)

- DOI: 10.1038/s41586-021-03312-w | PMCID: PMC7979515 | PMID: 33561864
- Version used: **2.7.5a**
- Evidence: We then mapped and quantified on a transcript and gene model basis using STAR (version 2.7.5a) and Salmon (version 1.2.1) 46 , 47 .
- Full pipeline: alignment/mapping [STAR v2.7.5a] -> quantification [STAR v2.7.5a] -> normalisation [DESeq2, R v3.6.3] -> differential/statistical testing [DESeq2, R v3.6.3] -> stage not stated [GSEA, ImageJ, ggplot2 v3.3.1, tidyverse v1.3.0]

### IgA transcytosis and antigen recognition govern ovarian cancer immunity. (Nature 2021)

- DOI: 10.1038/s41586-020-03144-0 | PMCID: PMC7969354 | PMID: 33536615
- Evidence: Raw RNA-seq reads were aligned to the GRCh37 human transcriptome using STAR 24 (v.2.5.3a).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, HTSeq, STAR] -> normalisation [HTSeq] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [GSEA, R v3.6.1]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **2.6.1d**
- Evidence: 0.6.4 and aligned to the hybrid genome described above using STAR 2.6.1d 56 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### In vivo base editing rescues Hutchinson-Gilford progeria syndrome in mice. (Nature 2021)

- DOI: 10.1038/s41586-020-03086-7 | PMCID: PMC7872200 | PMID: 33408413
- Version used: **2.7.3a**
- Evidence: Trimmed reads were aligned to Homo sapiens genome assembly GRCh38 with a custom Cas9-ABEmax gene entry by initially aligning with STAR (version 2.7.3a) to identify splice junction followed by an additional STAR alignment including the splice junctions identified in the first STAR alignment (2-STAR pass).
- Full pipeline: quality control [FastQC v0.10.0, MultiQC] -> read trimming [STAR v2.7.3a, Trim Galore v0.6.2] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.3a] -> normalisation [R, limma] -> differential/statistical testing [R, limma] -> stage not stated [ANNOVAR, BEDTools, GATK, SAMtools]

### Phenotypic variation of transcriptomic cell types in mouse motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-020-2907-3 | PMCID: PMC8113357 | PMID: 33184512
- Version used: **2.5.4b**
- Evidence: Sequencing reads were aligned to the mm10 mouse reference genome using STAR version 2.5.4b 48 and transcript assignment performed with Gencode transcript annotations, version M23.
- Full pipeline: alignment/mapping [STAR v2.5.4b] -> differential/statistical testing [scikit-learn] -> stage not stated [Python]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Version used: **2.7.0e**
- Evidence: STAR (version2.7.0e) was used to map ATAC-Seq reads to the mm10 genome assembly retaining only uniquely mapped pairs (settings: alignEndsType EndToEnd, alignIntronMax 1, alignMatesGapMax 2000, alignEndsProtrude 100 ConcordantPair, outFilterMultimapNmax 1, outFilterScoreMinOverLread 0.9, outFilterMatchNminOverLread 0.9) 62 .
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **2.6**
- Evidence: Raw reads were aligned to the genome indices and gene counts were generated using STAR (v.2.6) 58 with the default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Version used: **2.5.2**
- Evidence: RNAseq reads from datasets (CTOs or chemotherapy treatment) were aligned with STAR (v2.5.2) 51 with default parameters to the Mus musculus reference genome built with annotations version GENCODE_mmusculus_vM25.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Nociceptor neurons affect cancer immunosurveillance. (Nature 2022)

- DOI: 10.1038/s41586-022-05374-w | PMCID: PMC9646485 | PMID: 36323780
- Version used: **2.5.1b**
- Evidence: Sequences were trimmed for sequencing adapters and low-quality 3′ bases using Trimmomatic v.0.35 and aligned to the reference mouse genome version GRCm38 (gene annotation from Gencode v.M23, based on Ensembl 98) using STAR v.2.5.1b (ref.
- Full pipeline: read trimming [STAR v2.5.1b, Trimmomatic v0.35] -> alignment/mapping [STAR v2.5.1b, Trimmomatic v0.35, featureCounts] -> quantification [Bioconductor, RSEM] -> normalisation [Bioconductor, RSEM] -> dimensionality reduction/clustering [R] -> stage not stated [DESeq2 v1.18.1, ImageJ]

### Collagenolysis-dependent DDR1 signalling dictates pancreatic cancer outcome. (Nature 2022)

- DOI: 10.1038/s41586-022-05169-z | PMCID: PMC9588640 | PMID: 36198801
- Evidence: RNA-seq reads were aligned to the mouse genome (GRCm38/mm10) using STAR.
- Full pipeline: quality control [R v4.0.2, Seurat] -> alignment/mapping [STAR] -> quantification [HOMER v4.11] -> dimensionality reduction/clustering [GSEA]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Version used: **2.6.1a**
- Evidence: For all RNA-seq, reads were aligned using STAR (v2.6.1a) with default parameters and only uniquely mapped reads were retained for downstream analysis.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **2.7.7a**
- Evidence: Pre-processing of the Smart-seq2 scRNA-seq dataset Smart-seq2 sequencing data from demultiplexed samples was aligned to the mouse reference genome using STAR v2.7.7a 55 with ‘--twopassMode Basic --outFilterMultimapNmax 1 --quantMode TranscriptomeSAM’.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Version used: **2.6.1d**
- Evidence: Trimmed reads were mapped to the mouse reference genome (mm10) for mouse embryo nuclei, using STAR v2.6.1d 74 with default settings and gene annotations (Gencode VM12 for mouse).
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: The sequencing data were demultiplexed using Cell-Ranger software (v.2.0.2) and the reads were aligned to the mouse mm10 reference genome using STAR aligner.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Live-seq enables temporal transcriptomic recording of single cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05046-9 | PMCID: PMC9402441 | PMID: 35978187
- Version used: **2.7.9a**
- Evidence: All samples were then aligned on this vector using STAR v.2.7.9a (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [edgeR] -> stage not stated [HTSeq, ImageJ, Monocle, R v3.5.0, Seurat, ggplot2 v3.2.1, velocyto]

### Truncated FGFR2 is a clinically actionable oncogene in multiple cancers. (Nature 2022)

- DOI: 10.1038/s41586-022-05066-5 | PMCID: PMC9436779 | PMID: 35948633
- Version used: **2.7.2**
- Evidence: Sequencing reads were then mapped on the basis of the customized fasta and gtf files using STAR (v.2.7.2) 84 .
- Full pipeline: read trimming [edgeR v3.26.6] -> alignment/mapping [BWA v0.7.5a, STAR v2.7.2] -> quantification [RSEM v1.3.0, edgeR v3.26.6, featureCounts v1.6.2] -> normalisation [edgeR v3.26.6] -> differential/statistical testing [R, limma v3.52.1]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Version used: **2.7.9a**
- Evidence: Alignment to the human reference genome GRCh38/hg38 was performed using STAR (v2.7.9a) 44 , based on the GENCODE v30 annotation.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Retrograde movements determine effective stem cell numbers in the intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-04962-0 | PMCID: PMC7614894 | PMID: 35831497
- Version used: **2.5.2b**
- Evidence: Trimmed raw reads (average length 96-102 nucleotides) were aligned to genome mm10 using STAR (version 2.5.2b) 27 for genome assembly and gene count.
- Full pipeline: read trimming [STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> differential/statistical testing [Bioconductor v3.14, R v4.1.1] -> stage not stated [ImageJ, NumPy v1.19.5, Python v3.10, TrackMate]

### GTSF1 accelerates target RNA cleavage by PIWI-clade Argonaute proteins. (Nature 2022)

- DOI: 10.1038/s41586-022-05009-0 | PMCID: PMC9385479 | PMID: 35772669
- Version used: **2.3**
- Evidence: After rRNA removal, the remaining reads were mapped to corresponding genomes (mouse, mm10; rat, rn6; macaque, rheMac8; human, hg19) using STAR 2.3 with default parameters that allowed ≤ 2 mismatches and 100 mapping locations 79 .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4, HTSeq v0.9.1, RAxML v1.0.0, SAMtools v1.8, STAR v2.3] -> quantification [HTSeq v0.9.1] -> visualisation [Clustal Omega v1.2.4, RAxML v1.0.0] -> stage not stated [Bowtie2 v2.5]

### Mitochondrial RNA modifications shape metabolic plasticity in metastasis. (Nature 2022)

- DOI: 10.1038/s41586-022-04898-5 | PMCID: PMC9300468 | PMID: 35768510
- Version used: **2.3**
- Evidence: Genomic mapping was performed with STAR v.2.3 for the filtered reads with human genome 38 (ref.
- Full pipeline: read trimming [STAR v2.3, Trim Galore] -> alignment/mapping [Bismark v0.22.3, R, STAR v2.3] -> normalisation [GSEA v4.0.3] -> differential/statistical testing [GSEA v4.0.3, GSVA, edgeR] -> visualisation [GSVA] -> stage not stated [DESeq2, featureCounts v1.4.5]

### Global Tonga tsunami explained by a fast-moving atmospheric source. (Nature 2022)

- DOI: 10.1038/s41586-022-04926-4 | PMCID: PMC9492550 | PMID: 35697059
- Evidence: Optical imagery from NOAA/NESDIS/STAR visualized by NASA Worldview. b , Detail at 5:10 UTC, with clean and interpreted optical (top pair) and clean and interpreted infrared channel 13 (bottom pair) imagery.
- Full pipeline: visualisation [STAR]

### Molecularly defined circuits for cardiovascular and cardiopulmonary control. (Nature 2022)

- DOI: 10.1038/s41586-022-04760-8 | PMCID: PMC9297035 | PMID: 35650438
- Evidence: Single cell RNAseq data analysis cDNA sequencing reads from the the obtained Amb Cardiac (191) and Amb Laryngeal (77) neurons were pruned for low nucleotide quality scores and adapter sequences using Skewer 42 (version 0.2.2), and aligned to the mm10 genome using STAR 43 (version 2.6.1d) in two-pass mapping mode, in which the first pass identifies novel splice junctions and the second pass aligns ...
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [Seurat v3.1.4] -> normalisation [Seurat v3.1.4]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Evidence: To align the trimmed reads, STAR aligner (v2.4.2a) was used with the GRCh38 reference genome and gene annotations from ensembl release 91.
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Evidence: Cleaned reads from each sample were mapped to the complete ABO sequence from the Bamaxiang reference genome with the A allele at the ABO locus constructed by the authors using STAR (v.020201) 78 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### TDP-43 represses cryptic exon inclusion in the FTD-ALS gene UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04424-7 | PMCID: PMC8891019 | PMID: 35197626
- Version used: **2.7.3a**
- Evidence: RNA-seq reads were mapped to the human (hg38) using STAR v2.7.3a following ENCODE standard options, read counts were generated using RSEM v1.3.1, and differential expression analysis was performed in R v4.0.2 using the DESeq2 package v1.28.1 40 .
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [DESeq2, R v4.0, RSEM v1.3.1, SAMtools, STAR v2.7.3a] -> variant calling [GATK] -> quantification [BEDTools v2.27.1, DESeq2, ImageJ, R v4.0, RSEM v1.3.1, STAR v2.7.3a] -> differential/statistical testing [DESeq2, R v4.0, RSEM v1.3.1, STAR v2.7.3a, lme4] -> stage not stated [BCFtools v1.8, Picard, VCFtools v0.1.16]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Version used: **2.7.0f**
- Evidence: Samples were quality trimmed using Fastp with the parameter “qualified_quality_phred: 10”, and aligned to the GRCh38 genome build using STAR (v2.7.0f) 38 with gene models from GENCODE v31 39 .
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **2.7.3a**
- Evidence: Bioinformatic processing For each sample, raw sequencing reads were trimmed using Trimmomatic (v.0.36) and then mapped to the human reference genome (hg38) with STAR (v.2.7.3a).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### RNA profiles reveal signatures of future health and disease in pregnancy. (Nature 2022)

- DOI: 10.1038/s41586-021-04249-w | PMCID: PMC8770117 | PMID: 34987224
- Evidence: Briefly, raw sequencing reads were trimmed using trimmomatic 38 and then mapped to hg38 using the STAR aligner 39 .
- Full pipeline: quality control [MultiQC] -> read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, Picard, R, fgsea]

### Malaria protection due to sickle haemoglobin depends on parasite genotype. (Nature 2022)

- DOI: 10.1038/s41586-021-04288-3 | PMCID: PMC8810385 | PMID: 34883497
- Version used: **2.7.3a**
- Evidence: In brief, reads were aligned to a concatenated human GRCh38 / Pf3D7 genome using STAR v2.7.3a, informed by the Gencode v38 human and the PlasmoDB v52 Pf3D7 gene annotations.
- Full pipeline: alignment/mapping [MAFFT, STAR v2.7.3a, minimap2] -> variant calling [GATK] -> stage not stated [Stan]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **2.5.2b**
- Evidence: RNA-seq pre-processing FASTQ files for each sample generated from multiple sequencing lanes were merged and aligned using STAR version 2.5.2b 67 , using an index generated from the GRCh37 decoy assembly of the human genome and a transcriptomic Gene Transfer Format (GTF) guide obtained from Ensembl Release 87.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Version used: **2.7.1a**
- Evidence: Samples were aligned to Mouse reference, mm10/genecode.vM23, using STAR (v.2.7.1a). snRNA-seq preprocessing, quality control and removal of second-order nuclei Ambient RNA contamination was removed from each sample using CellBender 56 (v.0.2.1, ‘remove-background’, default parameters).
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **2.7.4**
- Evidence: The trimmed reads were aligned using STAR (v.2.7.4) 58 to an ‘N-masked’ genome, where all the single nucleotide polymorphic sites for Mus musculus CAST/EiJ and Mus musculus C57BL/6 (or 129S1/SvImJ) were masked by ambiguity nucleobase ‘N’ 59 .
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Version used: **2.5.2a**
- Evidence: STAR (version 2.5.2a) was used for mapping the reads and to align them to the mm10 genome reference (provided by Drop‐seq group, GSE63269 ) that was tailored to include the eGFP cDNA transcript. scRNA-seq data analysis All the analyses were performed using the phyton toolkit Scanpy 50 and complementary tools under its ecosystem.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Version used: **2.6.1d**
- Evidence: Trimmed reads were mapped to the mouse reference genome (mm10), using STAR v2.6.1d 56 with default settings and gene annotations (GENCODE VM12 for mouse).
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Autoantibodies against type I IFNs in humans with alternative NF-κB pathway deficiency. (Nature 2023)

- DOI: 10.1038/s41586-023-06717-x | PMCID: PMC10665196 | PMID: 37938781
- Version used: **2.6.1d**
- Evidence: All FASTQ files passed quality control and the sequences were aligned with the GRCh38 reference genome using STAR (v.2.6.1d).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Evidence: Sequencing reads were mapped to the mouse reference genome (mm10) using the STAR aligner (v2.7.3).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Apoptotic stress causes mtDNA release during senescence and drives the SASP. (Nature 2023)

- DOI: 10.1038/s41586-023-06621-4 | PMCID: PMC10584674 | PMID: 37821702
- Evidence: RNA-seq paired-end reads were assessed for quality using the FastQC algorithm, then aligned to the human genome using the splice-aware aligner STAR with a two-pass alignment pipeline.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [Cufflinks, FastQC, STAR] -> quantification [Cufflinks, DESeq2, HTSeq] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, ImageJ]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Version used: **2.7.3a**
- Evidence: RNA-seq data processing and visualization For SOA-KI RNA-seq, the reads were mapped to the ribosomal RNA sequences extracted from the Ensembl AgamP4 genome using the Ensembl AgamP4 annotation (release 48) with STAR (v.2.7.3a) with the following parameters: outFilterMultimapNmax 1000000 outFilterMismatchNoverLmax 0.04 outFilterMismatchNmax 999.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Version used: **2.7.8a**
- Evidence: The unmapped reads were then assigned to the Arabidopsis TAIR 10 genome using STAR v.2.7.8a (ref.
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### Spatial predictors of immunotherapy response in triple-negative breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06498-3 | PMCID: PMC10533410 | PMID: 37674077
- Version used: **2.5.2**
- Evidence: Base call files from each sequencing run were converted to fastq format using bcl2fastq conversion software v.2.20, replicate fastq files for each sample were merged and files were aligned to the Ensembl GRCh37 Homo sapiens reference using STAR v.2.5.2 (ref.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> quantification [Bioconductor] -> differential/statistical testing [R] -> machine learning [ilastik] -> stage not stated [CellProfiler]

### Epitope editing enables targeted immunotherapy of acute myeloid leukaemia. (Nature 2023)

- DOI: 10.1038/s41586-023-06496-5 | PMCID: PMC10499609 | PMID: 37648862
- Evidence: Raw sequencing files were filtered for quality control and aligned to the reference human genome hg38 using STAR workflow 59 , obtaining, as a result, the gene-based count matrices.
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [Python] -> visualisation [ggplot2] -> stage not stated [Bioconductor, R]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Version used: **2.5.2a**
- Evidence: Reads were aligned to the mouse genome (Ensembl GRCm38 release 89) using STAR (version 2.5.2a) 51 and gene level counts were obtained using the RSEM package (version 1.3.0) 52 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Platelet factors attenuate inflammation and rescue cognition in ageing. (Nature 2023)

- DOI: 10.1038/s41586-023-06436-3 | PMCID: PMC10468395 | PMID: 37587343
- Version used: **2.7.3a**
- Evidence: Alignment of RNA-seq reads to the mouse mm10 transcriptome was performed using STAR (v.2.7.3a) 50 using the ENCODE standard options, read counts were generated using RSEM (v.1.3.1) and differential expression analysis was performed in R (v.3.6.1) using the DESeq2 package (v.1.38.0) 51 (detailed pipeline v.2.0.1 and options are available at GitHub ( https://github.com/emc2cube/Bioinformatics/ )).
- Full pipeline: alignment/mapping [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> quantification [DESeq2, ImageJ, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> stage not stated [Enrichr, Seurat]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Version used: **2.2.7a**
- Evidence: Raw RNA-seq reads were aligned against mm10 and transcript annotations using STAR v.2.2.7a 63 .
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Evidence: Reads were then aligned to the GRCm39 reference genome using the STAR aligner v.2.7.7 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### cGAS-STING drives ageing-related inflammation and neurodegeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-06373-1 | PMCID: PMC10412454 | PMID: 37532932
- Evidence: Bulk RNA analysis For the fibroblasts, RNA was mapped to the human genome assembly hg38 (gencode v36, Ensembl 102) using STAR aligner (v.2.7), and counts were generated with HTSeq Count.
- Full pipeline: alignment/mapping [HTSeq, STAR, featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.38.2, ImageJ, Seurat]

### Africa-specific human genetic variation near CHD1L associates with HIV-1 load. (Nature 2023)

- DOI: 10.1038/s41586-023-06370-4 | PMCID: PMC10848312 | PMID: 37532928
- Evidence: Reads were mapped to the human reference sequence v38 using the STAR alignment tool in two-pass mode.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, FastQC, STAR] -> variant calling [GATK] -> quantification [FastQC, HTSeq v0.9.1] -> normalisation [DESeq2, FastQC] -> stage not stated [GCTA v1.25.3, IMPUTE2 v2.3.2, ImageJ, MAGMA v1.10]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Version used: **2.7.10a**
- Evidence: FASTQ files were then processed with STAR (v.2.7.10a).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Evidence: RNA-seq read mapping and feature counting RNA-seq reads from the six tissues of TA299 and TA10622 were mapped to the respective genomes using STAR aligner (v.2.5.2a) 73 with the flags --outFilterMultimapNmax 20000, --outFilterMismatchNoverLmax 0.0, --alignIntronMax 1000.
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Version used: **2.5.2b**
- Evidence: For RNA processing, this involved removal of accessible chromatin contaminating reads using cutadapt (v.3.1) 51 , dropEst (v.0.8.6) 52 to extract cell barcodes and STAR (version 2.5.2b) 53 to align tagged reads to the genome (GRCh38).
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Mast cells link immune sensing to antigen-avoidance behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06188-0 | PMCID: PMC10432277 | PMID: 37438525
- Evidence: Data were mapped using STAR aligner (v.2.5.2b) 68 , and reads were annotated using the FeatureCounts algorithm from the subread package (v.1.5.1) 69 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [DESeq2]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Version used: **2.7.5c**
- Evidence: For alignment, STAR (v.2.7.5c) (ref.
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Version used: **2.3.1**
- Evidence: Unaligned reads were mapped to mouse genome mm10 using STAR (v.2.3.1) 65 and PCR duplicates were removed 55 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### Signalling by senescent melanocytes hyperactivates hair growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06172-8 | PMCID: PMC10284692 | PMID: 37344645
- Version used: **2.4.2a**
- Evidence: For both bulk and single-cell RNA-seq, reads were first aligned using STAR v.2.4.2a with parameters ‘--outFilterMismatchNmax 10 --outFilterMismatchNoverReadLmax 0.07 --outFilterMultimapNmax 10’ to the reference mouse genome (mm10/genocode,vM8).
- Full pipeline: alignment/mapping [RSEM v1.2.25, STAR v2.4.2a] -> quantification [RSEM v1.2.25] -> normalisation [RSEM v1.2.25] -> dimensionality reduction/clustering [R, Seurat] -> differential/statistical testing [edgeR v3.2.2] -> stage not stated [Metascape]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Version used: **2.7.6a**
- Evidence: Alignment and post-alignment processing of sequencing data Sequencing reads were aligned using STAR (v.2.7.6a) ( https://github.com/alexdobin/STAR ) to the Gencode v.25 reference (–twoPassMode basic; –quantMode: TranscriptomeSAM and GeneCounts) and sorted by genomic coordinate.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Version used: **2.6.0c**
- Evidence: We then used STAR (v.2.6.0c) to align processed fastqs to hg38 and created a count matrix.
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Version used: **2.5.2b**
- Evidence: Raw sequencing data were first evaluated using FASTQC (v.0.72) for quality, then aligned against the reference mouse genome GRCm38 using STAR (v.2.5.2b-2) 70 with default parameters.
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **2.7.1a**
- Evidence: The Bolinopsis genome was annotated using BRAKER (v.2.14) 89 supplied with evidence from RNA-seq reads mapped with STAR (v.2.7.1a) 90 and minimap2 (v.2.23) 84 , Iso-Seq reads processed with lima (v.2.2.0; https://github.com/PacificBiosciences/barcoding ) and isoseq3 (v.3.4.0; https://github.com/PacificBiosciences/IsoSeq ) then mapped with minimap2 (v.2.23) 84 , and protein orthology identified usi...
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Version used: **2.7.10a**
- Evidence: In addition, the reads were mapped to the spliced reference using STAR (v.2.7.10a) with default parameters 58 .
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Mitotic clustering of pulverized chromosomes from micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-05974-0 | PMCID: PMC10307639 | PMID: 37165191
- Version used: **2.7.4a**
- Evidence: Sequencing reads were aligned to the transcriptome using STAR (v.2.7.4a) 52 .
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> quantification [ImageJ] -> normalisation [DESeq2, GSEA v4.3.2, HTSeq v0.6.1p] -> differential/statistical testing [DESeq2, GSEA v4.3.2] -> stage not stated [BEDTools]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: Reads were aligned to the mouse mm10 reference genome using the STAR spliced read aligner 54 .
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Ageing-associated changes in transcriptional elongation influence longevity. (Nature 2023)

- DOI: 10.1038/s41586-023-05922-y | PMCID: PMC10132977 | PMID: 37046086
- Version used: **2.5.1b**
- Evidence: Alignment was performed with STAR version 2.5.1b 68 using the following parameters: ‘–outFilterType BySJout–outWigNorm None’ on the genome version mm10, rn5, hg38, dm6 and ce5 for M. musculus , R. norvegicus , H. sapiens , D. melanogaster and C. elegans , respectively.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.5.1b, Trimmomatic] -> quantification [StringTie] -> differential/statistical testing [DESeq2 v1.8.2, GSEA] -> stage not stated [kallisto v0.42.5]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Version used: **2.5.2a**
- Evidence: Fastq read files passing these quality checks were aligned to the UCSC hg19 human reference genome build using STAR (v.2.5.2a) 54 in two-pass mode with ENCODE 3 parameters, generating one BAM file per tumour region.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Version used: **2.5.2b**
- Evidence: Annotation RNA-seq reads of strand-specific libraries from five bulk embryonic stages and 13 organs were aligned to the genome using STAR (v.2.5.2b) 71 and each library assembled independently using stringtie (v.1.3.3) 72 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Version used: **2.7.6a**
- Evidence: Raw reads in fastq files were mapped to GRCm 38 with associated ensemble transcript definitions using STAR (v.2.7.6a) 67 .
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### RHOJ controls EMT-associated resistance to chemotherapy. (Nature 2023)

- DOI: 10.1038/s41586-023-05838-7 | PMCID: PMC10076223 | PMID: 36949199
- Evidence: Approximately 8 million paired-end reads per sample were mapped against the mouse reference genome (GRCm38.p4/mm10) using STAR software to generate read alignments for each sample.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [limma] -> normalisation [HTSeq] -> differential/statistical testing [limma] -> stage not stated [CellProfiler v3.1.9, ImageJ]

### The dietary sweetener sucralose is a negative modulator of T cell-mediated responses. (Nature 2023)

- DOI: 10.1038/s41586-023-05801-6 | PMCID: PMC10033444 | PMID: 36922598
- Version used: **2.7.6**
- Evidence: 51 ) and STAR 2.7.6 (ref.
- Full pipeline: read trimming [Cutadapt v2.10, DADA2 v1.18] -> alignment/mapping [Cutadapt v2.10, RSEM v1.3.1] -> stage not stated [DESeq2 v1.30, R v4.0, STAR v2.7.6, phyloseq]

### Fumarate induces vesicular release of mtDNA to drive innate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-05770-w | PMCID: PMC10017517 | PMID: 36890229
- Version used: **2.6.0c**
- Evidence: Reads were mapped to the mouse reference genome GRCm38 with the STAR (v.2.6.0c) aligner 29 .
- Full pipeline: read trimming [Cutadapt v1.10.0] -> alignment/mapping [Cutadapt v1.10.0, STAR v2.6.0c] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2 v1.18.1] -> stage not stated [GSEA, ImageJ]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **2.7.8a**
- Evidence: The RNA sequencing libraries (Supplementary Table 2 ) were aligned using STAR 2.7.8a 77 , 78 .
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: Raw reads were aligned to the mouse mm10 genome assembly using STAR.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### Microbiota-derived 3-IAA influences chemotherapy efficacy in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05728-y | PMCID: PMC9977685 | PMID: 36813961
- Version used: **2.7.9a**
- Evidence: Afterwards, reads were aligned to the mouse reference assembly (GRCm39.104) using STAR (v.2.7.9a) 47 .
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [STAR v2.7.9a] -> quantification [DADA2] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor, GSEA, ImageJ v2.1.0, fgsea v4.1, phyloseq]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Version used: **2.5.3a**
- Evidence: Read pairs were mapped individually to the most complete assembly available of human subtelomeres ( http://www.wistar.org/lab/harold-c-riethman-phd/page/subtelomere-assemblies ) using STAR v.2.5.3a allowing up to 101 mapping locations 62 .
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### mRNA ageing shapes the Cap2 methylome in mammalian mRNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05668-z | PMCID: PMC9891201 | PMID: 36725932
- Evidence: Ribosomal rRNA reads were removed using STAR aligner 51 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> differential/statistical testing [ImageJ v1.53a] -> visualisation [ImageJ v1.53a] -> stage not stated [BEDTools v2.28.0]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Evidence: Single-cell RNA-sequencing: Alignment, quantification and quality control SMART-seq2 sequencing data were aligned with STAR (v.
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.5.3a**
- Evidence: We then mapped all embryonic and adult transcriptomes and a publicly available dataset 63 (Sequence Read Archive (SRA) identifier: SRR1222288 ) with STAR (v.2.5.3a) 64 after removing low-quality read pairs and read pairs containing Illumina sequencing adapters with trimmomatic (v.0.39) 65 .
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Dendritic cells direct circadian anti-tumour immune responses. (Nature 2023)

- DOI: 10.1038/s41586-022-05605-0 | PMCID: PMC9891997 | PMID: 36470303
- Version used: **2.7.0**
- Evidence: Reads were aligned using STAR (v.2.7.0) 22 to the mouse mm10 UCSC genome.
- Full pipeline: alignment/mapping [STAR v2.7.0] -> quantification [HTSeq v0.9.1] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [ImageJ]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Version used: **2.7.9a**
- Evidence: In brief, STAR v2.7.9a was used.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **2.7.9a**
- Evidence: Using STAR v.2.7.9a and the previously collected data about sample type (3′/5′, 10x Genomics kit version), we applied the STARsolo command to specify UMI collapsing, barcode collapsing, and read clipping algorithms to generate results maximally similar to the default parameters of the “cellranger count” command in Cell Ranger v.6: “--soloUMIdedup 1MM_CR --soloCBmatchWLtype 1MM_multi_Nbase_pseudoco...
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Adult skull bone marrow is an expanding and resilient haematopoietic reservoir. (Nature 2024)

- DOI: 10.1038/s41586-024-08163-9 | PMCID: PMC11618084 | PMID: 39537918
- Version used: **2.7.10a**
- Evidence: Pooled libraries were sequenced by using High Output Kit (Illumina, TG-160-2002) with a NextSeq500 sequencer (Illumina). scRNA-seq Preprocessing: STAR version 2.7.10a (PMID: 23104886) was used to generate a reference genome index for GRCm39, with Gencode annotations vM29, subset to lncRNA and protein-coding genes.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [Matplotlib, UMAP] -> visualisation [Matplotlib] -> stage not stated [AnnData, ImageJ, Scanpy]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Version used: **2.7.7a**
- Evidence: Trimmed reads were aligned to GRCm39 Ensembl release 103 for quality control purposes using STAR version 2.7.7a 63 and quality control of the aligned reads was carried out using Picard tools (v2.27.3).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: Alignment used STAR aligner (v.2.7.5b, RRID: SCR_004463 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Probiotic neoantigen delivery vectors for precision cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08033-4 | PMCID: PMC11560847 | PMID: 39415001
- Evidence: Trimmed reads were aligned to the mm10 reference using STAR aligner v.2.5.2b (ref.
- Full pipeline: read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, STAR] -> normalisation [BCFtools v1.13] -> stage not stated [DESeq2 v1.20.0, GATK, Mutect2, VEP]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: RNA sequencing analysis STAR aligner (v.2.7.3a) 104 was run in two-pass mode (--twoPassMode Basic 105 ) versus GRCh38.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Calcium-permeable AMPA receptors govern PV neuron feature selectivity. (Nature 2024)

- DOI: 10.1038/s41586-024-08027-2 | PMCID: PMC11560848 | PMID: 39358515
- Evidence: We processed RNA-seq reads with bcbio-nextgen (v.1.2.3; 10.5281/zenodo.3564938) 81 , aligning to GRCm38 with the STAR aligner 76 and quantifying counts per gene with Sailfish 82 using the Ensembl annotation.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> stage not stated [DESeq2, ImageJ, Psychtoolbox, SciPy]

### Tuft cells act as regenerative stem cells in the human intestine. (Nature 2024)

- DOI: 10.1038/s41586-024-07952-6 | PMCID: PMC11499303 | PMID: 39358509
- Version used: **2.7.8a**
- Evidence: Reads were mapped to a human genome (hg38) integrated with the Clover transcript using STAR (v.2.7.8a), reads with many mapping positions were excluded.
- Full pipeline: alignment/mapping [STAR v2.7.8a] -> stage not stated [ImageJ]

### Temporal BMP4 effects on mouse embryonic and extraembryonic development. (Nature 2024)

- DOI: 10.1038/s41586-024-07937-5 | PMCID: PMC11485214 | PMID: 39294373
- Evidence: Reads were processed according to the MARS-seq2.0 protocol 70 with the same specifications as previously reported 12 using the STAR aligner for read alignment.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [ImageJ, scDblFinder]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **2.7.3a**
- Evidence: Processing of single-cell transcriptomic data Transcriptomic reads were mapped to the mouse genome build GRCm38 (mm10) with STAR 2.7.3a 69 , using gene annotations downloaded from Ensembl 70 Release 102.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Evidence: The RNA-seq fastq raw data were inspected to ensure that they were of high quality and then mapped onto the human reference genome GRCh38 using STAR aligner (v.2.7) 77 .
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **2.6**
- Evidence: ...y (Weill Cornell Medical College; bulk RNA-sequencing), and raw sequencing reads were aligned to the mouse reference genome (UCSC release mm39) using STAR (v2.6) 69 .
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **2.7.10b**
- Evidence: Trimmed paired-end reads were aligned to the corresponding genome assembly using STAR (v2.7.10b) 62 with the parameters “--twopassMode basic --outFilterMismatchNMax 5 --outFilterMatchNminOverLread 0.80 --alignMatesGapMax 100000 --outSAMstrandField intronMotif --runMode alignReads” and the results were filtered and sorted using SAMtools (v1.10) 63 .
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Mitochondrial complex I promotes kidney cancer metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07812-3 | PMCID: PMC11424252 | PMID: 39143213
- Version used: **2.7.3**
- Evidence: Sequencing reads were aligned to the human reference genome ( hg19 ) by STAR 2.7.3.a with default parameters in the two-pass mode.
- Full pipeline: alignment/mapping [STAR v2.7.3] -> differential/statistical testing [DESeq2 v1.14.1, edgeR] -> stage not stated [HTSeq v0.6.1, ImageJ, R, featureCounts]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Evidence: Trimmed reads were aligned to the W22 reference with STAR in two-pass alignment mode 106 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### ILC2-derived LIF licences progress from tissue to systemic immunity. (Nature 2024)

- DOI: 10.1038/s41586-024-07746-w | PMCID: PMC11338826 | PMID: 39112698
- Version used: **2.6.0a**
- Evidence: Sequence data were trimmed to remove adaptors and sequences with a quality score below 30 using Trim Galore (v.0.50, Babraham Bioinformatics) and then aligned to the mouse genome (GRCm38) using STAR (v.2.6.0a); differential expression was calculated using DESeq2 (v.1.18.1).
- Full pipeline: read trimming [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [tidyverse]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Version used: **2.7.1a**
- Evidence: Clean sequencing data were mapped to human reference GRCh38 using STAR (v.2.7.1a) 95 .
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### Human TMEFF1 is a restriction factor for herpes simplex virus in the brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07745-x | PMCID: PMC11306101 | PMID: 39048830
- Version used: **2.6.1d**
- Evidence: All FASTQ files passed quality control and were aligned with the GRCh38 reference genome with STAR (2.6.1d).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, kallisto v0.48.0] -> quantification [featureCounts v1.6.0] -> normalisation [ComplexHeatmap v2.14.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap v2.14.0, PLINK v1.9, edgeR] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [GATK v3.4, ImageJ, Picard, SAMtools v1.0]

### Neural circuit basis of placebo pain relief. (Nature 2024)

- DOI: 10.1038/s41586-024-07816-z | PMCID: PMC11358037 | PMID: 39048016
- Version used: **2.7.3a**
- Evidence: Single-cell FastQ files were aligned to the mm10 mouse genome (GRCm38) using STAR (v.2.7.3a) 71 .
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Seurat v4.0] -> stage not stated [DeepLabCut, ImageJ, R]

### Symbolic recording of signalling and cis-regulatory element activity to DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07706-4 | PMCID: PMC11357993 | PMID: 39020177
- Version used: **2.7.3**
- Evidence: Sequencing reads were trimmed using Cutadapt 49 and aligned to the human reference genome (hg38) using STAR (v.2.7.3) 50 , both with default settings.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.3] -> alignment/mapping [Cutadapt, STAR v2.7.3] -> differential/statistical testing [DESeq2, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Jupyter]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Version used: **2.7.10a**
- Evidence: ... (‘homerTools trim -3 AGATCGGAAGAGCACACGTCT -mis 2 -minMatchLength 4 -min 20’) and aligned to the appropriate genome (GRCh38/hg38, GRCm38/mm10) using STAR (v.2.7.10a) 77 with the default parameters.
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### Inhibition of IL-11 signalling extends mammalian healthspan and lifespan. (Nature 2024)

- DOI: 10.1038/s41586-024-07701-9 | PMCID: PMC11291288 | PMID: 39020175
- Version used: **2.7.9a**
- Evidence: Reads were mapped to the Mus musculus GRCm39 using STAR v.2.7.9a with the options --outFilterType BySJout --outFilterMultimapNmax 20 --alignSJoverhangMin 8 --alignSJDBoverhangMin 1 --outFilterMismatchNmax 999 --alignIntronMin 20 --alignIntronMax 1000000 --alignMatesGapMax 1000000 in paired-end, single pass mode.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [STAR v2.7.9a] -> quantification [ImageJ v1.53t, pheatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.36.0, R v4.2] -> visualisation [pheatmap] -> stage not stated [featureCounts, fgsea v1.22.0]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Since the BD pipeline uses STAR aligner 70 in the backend, the custom STAR reference genome was generated by the genomeGenerate command in STAR.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### De novo variants in the RNU4-2 snRNA cause a frequent neurodevelopmental syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07773-7 | PMCID: PMC11338827 | PMID: 38991538
- Evidence: The 100 bp paired-read RNA-seq data from BrainVar were aligned to the GRCh38.p12 human genome using STAR aligner 50 (v.2.4.2a), and gene-level read counts for GENCODE v.31 human gene definitions were calculated with DEXSeq 51 (v.1.50.0) and normalized to CPM 52 .
- Full pipeline: alignment/mapping [BEDTools v2.31.0, STAR] -> quantification [STAR] -> normalisation [STAR] -> stage not stated [Python, R v4.0.2, SAMtools]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Version used: **2.5.3a**
- Evidence: STAR v.2.5.3a (ref.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### A maternal brain hormone that builds bone. (Nature 2024)

- DOI: 10.1038/s41586-024-07634-3 | PMCID: PMC11306098 | PMID: 38987585
- Version used: **2.4**
- Evidence: Trimmed reads were then mapped to the mouse genome (v.M20) using STAR (v.2.4), and counts for gene and transcript reads were calculated using RSEM (v.1.2.21).
- Full pipeline: read trimming [RSEM v1.2.21, STAR v2.4] -> alignment/mapping [RSEM v1.2.21, STAR v2.4, kallisto] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy v1.9, scDblFinder]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Version used: **2.7.10a**
- Evidence: Next, reads were aligned to the mouse mm10 genome (with tdTomato sequences added) augmented with ERCC (External RNA Controls Consortium) sequences using STAR (v.2.7.10a) 76 .
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: The RNA-seq reads (Supplementary Data 4 ), ranging from 673 million ( P. pygmaeus ) to 7.3 billion ( P. troglodytes ) were aligned to the assembly using STAR 100 , while the Iso-seq reads (ranging from none for S. syndactylus to 27 million for G. gorilla ) were aligned using minimap2 77 .
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### Paternal microbiome perturbations impact offspring fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07336-w | PMCID: PMC11096121 | PMID: 38693261
- Version used: **2.7.10a**
- Evidence: For quality control and data preprocessing, raw reads were aligned using STAR v.2.7.10a (ref.
- Full pipeline: quality control [STAR v2.7.10a, Seurat, Trim Galore v0.4.3.1] -> read trimming [Bismark v0.20.0, Cutadapt v2.3, DADA2, Picard, Trim Galore v0.4.3.1] -> alignment/mapping [BEDTools, Bismark v0.20.0, Cutadapt v2.3, Picard, SAMtools v1.9, STAR v2.7.10a] -> variant calling [GATK v4.1.6.0] -> quantification [R, featureCounts] -> differential/statistical testing [DESeq2 v1.34.0, R] -> stage not stated [ANNOVAR, Metascape, QuPath v0.2.1]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Evidence: Illumina paired-end sequencing reads were aligned to the human reference GRCh37.75 genome using STAR aligner (version 2.6.0c) and the two-pass method as briefly follows: the reads were aligned in a first round using the --runMode alignReads parameter, then a sample-specific splice-junction index was created using the --runMode genomeGenerate parameter.
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **2.7.9a**
- Evidence: FASTQ reads were trimmed using Trimmomatic v.0.39 and aligned to the P. breviceps genome using STAR v.2.7.9a 86 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: RNA-seq reads were aligned to mm10 using STAR and visualized in the IGV genome browser to determine strand protocol.
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: The trimmed fastq files resulting from the experiment were aligned to the hg38 human genome using STAR.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Evidence: Quantification was performed by STAR during alignment.
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### Ancestral allele of DNA polymerase gamma modifies antiviral tolerance. (Nature 2024)

- DOI: 10.1038/s41586-024-07260-z | PMCID: PMC11041766 | PMID: 38570685
- Evidence: Alignment ready reads were converted from BAM-formatted files to fastq files that were used as an input for STAR aligner 74 .
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [FastQC, STAR] -> variant calling [R, Rcpp, SAIGE] -> quantification [CellProfiler v4.2.6, ilastik v1.3.3] -> differential/statistical testing [DESeq2, R, Rcpp, SAIGE] -> stage not stated [ImageJ v2.0.0, Picard]

### CGRP sensory neurons promote tissue healing via neutrophils and macrophages. (Nature 2024)

- DOI: 10.1038/s41586-024-07237-y | PMCID: PMC11023938 | PMID: 38538784
- Evidence: Reads were aligned to the Mus musculus GRCm38 reference using STAR aligner 63 .
- Full pipeline: quality control [featureCounts] -> alignment/mapping [STAR] -> quantification [featureCounts] -> differential/statistical testing [limma]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Evidence: Reads were aligned to the whole Mus musculus mm10 genome using STAR aligner58 (2.3.0e_r291) with default options, generating mapping files (BAM format).
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Version used: **2.7.10a**
- Evidence: Subsequently, all of the samples were aligned to the GRCh38.p13 genome using STAR v.2.7.10a (paired-end mode) 66 .
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Version used: **2.5.1b**
- Evidence: Reads were mapped to the human hg38 reference genome using STAR (v.2.5.1b).
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **2.5.2a**
- Evidence: STAR (v2.5.2a) 83 was used to align reads, without providing a gene annotation file, to custom references in which the synthetic HPRT1 and HPRT1R sequences were present on separate chromosomes or inserted at their specific integration sites in the SacCer_April2011/sacCer3 or GRCm38/mm10 genomes (produced using the reform tool; https://gencore.bio.nyu.edu/reform/ ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### On the genetic basis of tail-loss evolution in humans and apes. (Nature 2024)

- DOI: 10.1038/s41586-024-07095-8 | PMCID: PMC10901737 | PMID: 38418917
- Version used: **2.7.2a**
- Evidence: Raw sequencing reads were mapped to the mouse genome (mm10) with STAR (v.2.7.2a) aligner 59 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BEDTools v2.30.0, STAR v2.7.2a] -> differential/statistical testing [DESeq2 v1.40.2]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Alignment to the Mus musculus (mm10) refSeq (refFlat) reference gene annotation was performed using the STAR spliced read aligner (v.2.7.5c) with default parameters.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Durable and efficient gene silencing in vivo by hit-and-run epigenome editing. (Nature 2024)

- DOI: 10.1038/s41586-024-07087-8 | PMCID: PMC10937395 | PMID: 38418872
- Version used: **2.7.6a**
- Evidence: High-quality remaining reads were aligned to the mouse reference genome GRCm38 using STAR v2.7.6a (ref.
- Full pipeline: quality control [Trim Galore v0.6.6] -> read trimming [Trim Galore v0.6.6, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.5, STAR v2.7.6a] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [Bioconductor, Bismark]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: Genomic breakpoints of chimeric reads were analysed from supplementarily mapped data from STAR alignment to link the clone-specific chimeric reads with the viral integration sites identified in the corresponding clones.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **2.5.2b**
- Evidence: 5 were mapped against the human genome version hg19 with STAR (v.2.5.2b) 45 .
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Version used: **2.7.7a**
- Evidence: In brief, reads were aligned and counted to the human genome (GRCh38 assembly and Gencode release 43) with salmon v1.4.0 and with STAR 2.7.7a.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Version used: **2.6.1d**
- Evidence: Trimmed reads were mapped to the mouse reference genome (mm10) for mouse embryo nuclei using STAR v2.6.1d 74 with default settings and gene annotations (GENCODE VM12 for mouse).
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Version used: **2.7.9a**
- Evidence: Trimmed reads from human and mouse cell lines were mapped to human GRCh38 (HEK293, HeLa and HCT116 cell lines) and mouse GRCm38 (3T3 cell line) genomes using the STAR 2.7.9a aligner 62 .
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Version used: **2.7.10a**
- Evidence: For RNA-seq data processing and analysis, sequenced reads from the RNA-seq were aligned to the mouse reference genome GRCm39 or mm10 using STAR (v.2.7.10a) 93 .
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Circulating myeloid-derived MMP8 in stress susceptibility and depression. (Nature 2024)

- DOI: 10.1038/s41586-023-07015-2 | PMCID: PMC10901735 | PMID: 38326622
- Version used: **2.5**
- Evidence: Reads were aligned to the mouse genome reference GRCm38 using STAR (version 2.5) 72 .
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, HTSeq v0.12.4, STAR v2.5] -> quantification [ImageJ, Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **2.5.2b**
- Evidence: We aligned the reads to the genome using STAR (v.2.5.2b) with an average 78.7% uniquely mapping reads 79 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Alternative splicing of latrophilin-3 controls synapse formation. (Nature 2024)

- DOI: 10.1038/s41586-023-06913-9 | PMCID: PMC10830413 | PMID: 38233523
- Evidence: Cell-type-specific RiboTag sequencing data 18 reads were aligned to reference genome (GRCm38/mm10) using STAR.
- Full pipeline: alignment/mapping [STAR] -> quantification [scikit-image v0.20.0] -> stage not stated [CaImAn, DESeq2, HOMER, HTSeq, SciPy v1.10.1]

### Nasopharyngeal lymphatic plexus is a hub for cerebrospinal fluid drainage. (Nature 2024)

- DOI: 10.1038/s41586-023-06899-4 | PMCID: PMC10808075 | PMID: 38200313
- Version used: **2.7.9**
- Evidence: Pre-processing of single-cell sequencing data Sequenced libraries were demultiplexed and aligned to mouse reference genome (mm10) by STAR (v.2.7.9.a).
- Full pipeline: read trimming [STAR v2.7.9] -> alignment/mapping [STAR v2.7.9] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [R, Seurat, UMAP] -> stage not stated [ImageJ]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: RNA-seq reads were aligned to the mouse genome (mm10) using STAR 49 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Mucosal boosting enhances vaccine protection against SARS-CoV-2 in macaques. (Nature 2024)

- DOI: 10.1038/s41586-023-06951-3 | PMCID: PMC10849944 | PMID: 38096903
- Version used: **2.7.9a**
- Evidence: Alignment was performed using STAR v.2.7.9a and transcripts were annotated using a composite reference, including the Mmul10 assembly and annotation of the Indian rhesus macaque genome.
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.9a] -> quantification [HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [R] -> stage not stated [GSEA]

### N&lt;sup&gt;1&lt;/sup&gt;-methylpseudouridylation of mRNA causes +1 ribosomal frameshifting. (Nature 2024)

- DOI: 10.1038/s41586-023-06800-3 | PMCID: PMC10764286 | PMID: 38057663
- Version used: **2.7.4a**
- Evidence: Reads were aligned with STAR (version 2.7.4a) 37 .
- Full pipeline: alignment/mapping [STAR v2.7.4a] -> variant calling [R v4.3.0, ggplot2 v3.4.2] -> visualisation [R v4.3.0, ggplot2 v3.4.2]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Version used: **2.5.1b**
- Evidence: Alignment and quantification of human Visium data Raw FASTQ files and histology images were processed, aligned and quantified by sample using the Space Ranger software v.1.1.0, which uses STAR v.2.5.1b52 for genome alignment, against the Cell Ranger hg38 reference genome refdata-cellranger-GRCh38-3.0.0, available at: http://cf.10xgenomics.com/supp/cell-exp/refdata-cellranger-GRCh38-3.0.0.tar.gz .
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Hypoblast from human pluripotent stem cells regulates epiblast development. (Nature 2024)

- DOI: 10.1038/s41586-023-06871-2 | PMCID: PMC10849967 | PMID: 38052228
- Evidence: We used the Cell Ranger pipeline (v.3.1.0, 10x Genomics) for all human 10x Genomics single-cell datasets and STAR aligner (v.2.5.1b) and RSEM (v.1.3.1) tool for Smart-Seq datasets.
- Full pipeline: quality control [Seurat] -> read trimming [Cutadapt v1.15, TopHat] -> alignment/mapping [RSEM v1.3.1, STAR, TopHat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### Prime editing-installed suppressor tRNAs for disease-agnostic genome editing. (Nature 2025)

- DOI: 10.1038/s41586-025-09732-2 | PMCID: PMC12675287 | PMID: 41261131
- Evidence: Fastq reads were trimmed of adapter sequences using Trim Galore, aligned to the human genome using STAR, and differential expression analysis was performed using DESeq2 and custom R scripts.
- Full pipeline: read trimming [Bowtie2, DESeq2, STAR, Trim Galore] -> alignment/mapping [Bioconductor, Bowtie2, DESeq2, STAR, Trim Galore] -> differential/statistical testing [DESeq2, STAR, Trim Galore]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: Alignment Trimmed libraries were initially mapped with relaxed parameters to a chimeric reference comprising the host genome assembly, all viral assemblies and a curated collection of eukaryotic rRNA sequences using the STAR aligner (v.2.7.10a) 60 .
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **2.7.9**
- Evidence: Transcriptomics Reads were mapped on the CDS of the pangenome using STAR v.2.7.9.a 98 with default parameters.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Version used: **2.7.0**
- Evidence: Moreover, we also aligned all queries to the GENCODE (v.38) reference transcriptome using bwa-mem (v.0.7.17-r1188) 88 and against the hg38 human reference genome (GRCh38.p13, packaged with GENCODE v.38) using STAR (v.2.7.0 f) 89 .
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### SPP1 is required for maintaining mesenchymal cell fate in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09574-y | PMCID: PMC12675285 | PMID: 40993391
- Evidence: Reads were aligned to the mouse reference assembly to the Mus musculus GRCm38 reference genome available on ENSEMBL using STAR aligner (v.2.5.2b) 44 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> normalisation [edgeR, survival (R)] -> differential/statistical testing [GSEA v4.0.3] -> stage not stated [Python, QuPath v0.4.2, R, Seurat v3.2.2, scikit-learn]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Version used: **2.7.0**
- Evidence: CLIP libraries were trimmed and demultiplexed using Ultraplex 75 and mapped to a small RNA genome containing all rRNA, small nuclear RNA, tRNA and small nucleolar RNA sequences from GENCODE vM22 using STAR (v2.7.0) 76 .
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: FASTQ files were aligned with STAR aligner (release 2.7.4a at GitHub).
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **2.7.10a**
- Evidence: Filtered reads were mapped to the mouse genome mm39 using STAR v.2.7.10a 67 using ENCODE parameters with a custom gtf file 68 on the basis of Ensembl version 108.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **2.4.2a**
- Evidence: In brief, STAR v2.4.2a was used to align reads to the GRCh38 reference using GENCODE annotation v22.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Reads were adapter-trimmed (Trim Galore, Nextera-specific settings, minimum overlap 3 bases), aligned to the human reference genome (GRCh38.p14, GENCODE release 47; STAR aligner), and counted (featureCounts, paired-end settings).
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Version used: **2.7.2**
- Evidence: RNA-seq data and differential expression analyses Raw FASTQ files were aligned to the human hg38 genome GRCh38.p14 using STAR v.2.7.2 and counted according to GENCODE annotation release version 35 on the fly.
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### Maternal stress triggers early-life eczema through fetal mast cell programming. (Nature 2025)

- DOI: 10.1038/s41586-025-09419-8 | PMCID: PMC12488486 | PMID: 40866704
- Version used: **2.4.0**
- Evidence: Reads were then aligned on GRCm39 (mm10) as a reference genome using STAR (v.2.4.0) 68 aligner and counted with HTseq (v.0.9.1) 69 , and a counting matrix was generated.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2 v1.34.0, ImageJ v2.16.0, Seurat, Signac v1.14.0]

### STING induces ZBP1-mediated necroptosis independently of TNFR1 and FADD. (Nature 2025)

- DOI: 10.1038/s41586-025-09536-4 | PMCID: PMC12629989 | PMID: 40834903
- Evidence: Differential expression analysis RNA-seq reads were aligned to the reference genome (hg38 or mm10) using STAR aligner, followed by transcript quantification with RSEM.
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [Fiji, ImageJ, RSEM, STAR] -> normalisation [ggplot2 v3.5.1] -> differential/statistical testing [DESeq2 v1.44.0, RSEM, STAR] -> stage not stated [GSEA, Metascape]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Version used: **2.5.11**
- Evidence: Trimmomatic was used to remove adapter sequences and low-quality bases from the 3′ end of each read, and the resulting high-quality reads were aligned to the GRCm38 mouse genome using STAR v.2.5.11, which also generated gene-level read counts.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **2.5.2b**
- Evidence: RNA-seq was aligned to the genome using STAR (v.2.5.2b), assembled using stringtie (v.1.3.3b) and also assembled as de novo transcripts using Trinity (v.2.5.1) 72 .
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Evidence: Reads were mapped to the GRCm39 mouse genome using RNA STAR aligner v.2.7.8.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: Raw RNA-sequencing data in FASTQ format were subjected to quality assessment using FastQC (v.0.11.9) and sequencing reads were aligned to mouse genome (mm10) using a STAR aligner 79 with the following options: --outFilterMismatchNmax 999 --outFilterMismatchNoverLmax 0.04 --alignSJDBoverhangMin 1 --alignSJoverhangMin 8 --outFilterMultimapNmax 20 --outFilterType BySJout --alignIntronMin 20 --alignIn...
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: Raw sequencing data were processed using Cell Ranger (v.2.2, 10x Genomics) for 10x data and with STAR aligner (v.2.6.1a), skewer (v.0.2.2), RSEM (v.1.3.1) and HTSEQ (v.2.0) for SS2 data.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Version used: **2.7.9a**
- Evidence: Reads were trimmed with Cutadapt 69 and aligned to the mouse transcriptome (GRCm38, Ensembl release 102) using STAR (v.2.7.9a) 70 and quantified using Salmon (v.1.10.1) 71 .
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### A molecular cell atlas of mouse lemur, an emerging model primate. (Nature 2025)

- DOI: 10.1038/s41586-025-09113-9 | PMCID: PMC12328211 | PMID: 40739356
- Evidence: For SS2 samples, demultiplexed fastq files were mapped to the genome using STAR aligner (v.2.6.1a).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP]

### Mitochondrial origins of the pressure to sleep. (Nature 2025)

- DOI: 10.1038/s41586-025-09261-y | PMCID: PMC12443607 | PMID: 40670797
- Version used: **2.6.1b**
- Evidence: ... to a combination of the Drosophila melanogaster genome release BDGP6.22 and the reference sequences of the GAL4 and EGFP-p10 3’UTR transgenes, using STAR 2.6.1b with default settings 101 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [STAR v2.6.1b, Seurat v4.1]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Evidence: Raw reads from each library were aligned to the reference genome using STAR aligner v.2.7.2b (ref.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **2.7.8a**
- Evidence: All expression data were mapped using STAR (version 2.7.8a) 94 and assembled into transcripts with StringTie (version 2.1.5, parameters -m 150-t -f 0.3) 95 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Version used: **2.6.1**
- Evidence: Reads were trimmed with Trimmomatic (ILLUMINACLIP:TruSeq2-PE.fa:2:30:10:1:FALSE LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36) and aligned to the cDNA annotation of the reference genome sequence of tomato (SL4.0) using STAR (v.2.6.1.d) 65 .
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Mapping and engineering RNA-driven architecture of the multiphase nucleolus. (Nature 2025)

- DOI: 10.1038/s41586-025-09207-4 | PMCID: PMC12350172 | PMID: 40604277
- Version used: **2.7.11a**
- Evidence: Trimmed reads were then aligned to the rDNA genome (GenBank: U13369.1 ) using STAR (v.2.7.11a) 68 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [FastQC v0.11.9, STAR v2.7.11a, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.9, STAR v2.7.11a] -> stage not stated [CellProfiler, Python, featureCounts v1.6.4]

### PPP2R1A mutations portend improved survival after cancer immunotherapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09203-8 | PMCID: PMC12350166 | PMID: 40604275
- Evidence: STAR 2-pass alignment (v.2.7.0 f) 52 was performed with the default parameters to generate RNA-seq BAM files.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [HTSeq, STAR] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v1.42.1, GSEA, R, clusterProfiler v4.6.2] -> machine learning [StarDist] -> visualisation [ggplot2 v3.4.2] -> stage not stated [ImageJ v1.54g, QuPath v0.4.4]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: The reads were aligned to the human GENCODE v.34 reference genome using STAR aligner, and the duplicate reads were collapsed using umi_tools.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Version used: **2.7.11b**
- Evidence: Bulk RNA-seq analysis Bulk RNA-seq reads were mapped to GRCh38 human genome using STAR (v2.7.11b).
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: Filtered data from HEK293K cells were mapped to a custom human genome hg38, including the eGFP sequence cloned using the STAR aligner 84 to hg38 human genome.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: The trimmed reads were aligned to the mouse genome (GRCm39/mm39) using STAR aligner v.2.5.2b, with parameters aligned to the ENCODE long RNA-seq pipeline recommendations ( https://github.com/ENCODE-DCC/long-rna-seq-pipeline ).
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Evidence: RNA-seq data were aligned to the mouse genome GRCm39 release 109 using STAR aligner (2.7.11b). featureCount (v2.0.6) was used to assigned reads exons, transcripts and CDS.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: RNA-seq reads per cell were aligned to the hg38 reference by means of the STAR tool 54 .
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: To process data, raw reads were aligned to the reference genome using STAR (v.020201) 134 in --quantMode to estimate the number of read counts per gene.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Reads were aligned to Michigan State University Rice genome v.7 with the STAR aligner 36 , deduplicated using UMI-Tools 37 and counted with HTSeq-Count. scRNA-seq profiling of rice root protoplasts using the 10X Genomics Chromium system For rice seedling harvesting, gel-grown rice seedlings were directly pulled out from the growth media and root tips were cut in the enzyme solution within the opti...
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **2.7.10a**
- Evidence: Alignment of RNA sequencing tags was restricted to those mapping to the same DNA strand as annotated in the GRCm38 reference genome, using STAR (v.2.7.10a).
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **2.7.0f**
- Evidence: For ER-HOXA9 cell RNA-seq analysis, Fastq reads were aligned to the mouse genome (mm10) using STAR 2.7.0f.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: Differential expression analyses Illumina RNA-seq reads were mapped to the mouse reference genome (GRCm38, ENSEMBL, release 94) using the STAR aligner (v.2.7.6a) 39 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **2.7.10a**
- Evidence: Reads were mapped with STARsolo 48 , 49 (STAR v.2.7.10a) to a hybrid fasta file combining the T. brucei Lister 427 strain genome (Tb427v11, ref.
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Version used: **2.7**
- Evidence: RNA sequencing analysis Reads were aligned to the GRCh38 genome using STAR (v2.7), and the transcripts were quantified with RSEM (v1.3.3).
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Version used: **2.7.5c**
- Evidence: Reads were trimmed using trimmomatic (v.0.39) 66 and then mapped to their respective genome using STAR (v.2.7.5c) 67 and expression was computed in TPM.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Version used: **2.5.1b**
- Evidence: Second, the reads were mapped to the reference genomes using STAR 2.5.1b.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: The STAR aligner 60 was then used to map the fastqs with the following settings: -outSAMtype BAM SortedByCoordinate --outFilterMultimapNmax 1000 --outFilterScoreMinOverLread 0.25 --alignIntronMax 1 --alignEndsType EndToEnd.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Version used: **2.7.8a**
- Evidence: RNA-seq single-end reads were mapped to the GRCm39.103 version of the Mus musculus genome and annotated 61 using STAR (v.2.7.8a) 62 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Tumour-wide RNA splicing aberrations generate actionable public neoantigens. (Nature 2025)

- DOI: 10.1038/s41586-024-08552-0 | PMCID: PMC11903331 | PMID: 39972144
- Evidence: RNA-seq alignment All downloaded RNA-seq datasets were individually aligned using a STAR aligner-based processing pipeline.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, R, RSEM] -> differential/statistical testing [DESeq2, GSEA, R] -> stage not stated [AlphaFold v2.3.2, Picard]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Version used: **2.7.9a**
- Evidence: Sequenced reads (2 × 57 bp, paired-end, ~20 million reads per sample) were trimmed using trimmomatic (v.0.39) 63 and mapped to the P. falciparum 3D7 genome v3.0 ( https://PlasmoDB.org , release 52) 64 using STAR (v.2.7.9a) 65 .
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Version used: **2.5.3a**
- Evidence: Alignment of scRNA-seq data and gene-expression quantifications For Smart-seq2 data, raw sequencing reads were aligned to the reference genome (mm10, GRCm38) using STAR (v.2.5.3a) 50 and gene expression was quantified using htseq-count (v.2.0.1) 51 .
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### Transcriptional adaptation upregulates utrophin in Duchenne muscular dystrophy. (Nature 2025)

- DOI: 10.1038/s41586-024-08539-x | PMCID: PMC11903304 | PMID: 39939773
- Evidence: The processed reads were aligned to the GRCh38/Gencode v46 genome using STAR, and transcript abundance was estimated using HT-Seq, followed by DESeq2 for differential expression analysis in patient myotubes or IsoDE2 for HEK293T cells.
- Full pipeline: alignment/mapping [DESeq2, STAR] -> quantification [DESeq2, STAR] -> differential/statistical testing [DESeq2, STAR]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: Alignment was completed using the STAR alignment algorithm against human reference hg19.
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### SKI complex loss renders 9p21.3-deleted or MSI-H cancers dependent on PELO. (Nature 2025)

- DOI: 10.1038/s41586-024-08509-3 | PMCID: PMC11864980 | PMID: 39910293
- Evidence: Raw BCL files were demultiplexed using bcl2fastq ( https://cumulus.readthedocs.io/en/latest/bcl2fastq.html ); then, reads were aligned to hg38 using STAR ( https://github.com/broadinstitute/depmap_omics/blob/a5308bc41227b86af47de545e14c38e7b8bf33f7/RNA_pipeline/star_wdl1-0.wdl ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [ImageJ v1.53k, Picard, RSEM, SciPy]

### C-terminal amides mark proteins for degradation via SCF-FBXO31. (Nature 2025)

- DOI: 10.1038/s41586-024-08475-w | PMCID: PMC11821526 | PMID: 39880951
- Evidence: Reads were aligned with STAR-aligner 76 (v.2.7.10a) and counting was performed using FeatureCounts 77 (v.2.0.6) against a custom transcriptome reference.
- Full pipeline: alignment/mapping [STAR, featureCounts] -> normalisation [limma v3.58.1] -> differential/statistical testing [DESeq2, limma v3.58.1] -> visualisation [ChimeraX]

### The maternal X chromosome affects cognition and brain ageing in female mice. (Nature 2025)

- DOI: 10.1038/s41586-024-08457-y | PMCID: PMC11798838 | PMID: 39843739
- Evidence: The trimmed reads were mapped to the Mus musculus GRCm38 reference genome available on ENSEMBL using the STAR aligner v.2.5.2b.
- Full pipeline: quality control [FastQC] -> read trimming [STAR] -> alignment/mapping [Bismark, STAR] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, featureCounts]

### Rapid and scalable personalized ASO screening in patient-derived organoids. (Nature 2025)

- DOI: 10.1038/s41586-024-08462-1 | PMCID: PMC11798851 | PMID: 39843740
- Evidence: Amplicon sequencing For visualization, raw sequencing data were aligned to the human genome using STAR with default settings and GENCODE Release 43 as the reference transcriptome 47 .
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> visualisation [STAR]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Version used: **2.4.0e**
- Evidence: Sequencing data were quality controlled by FastQC and aligned to the mouse genome (NCBI37/mm9) using STAR (v2.4.0e) (10.1093/bioinformatics/bts635).
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **2.5**
- Evidence: The resulting reads were quality controlled using FastQC v.0.11.8 and Trim Galore v.0.6.10, and mapped to M. truncatula v5 genome (MtrunA17r5.0-ANR) using STAR v.2.5.a.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **2.7.11b**
- Evidence: The samples were aligned to the GRCm38 mouse genome using STAR (v.2.7.11b) alignReads in mode BAM SortedByCoordinate 60 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Version used: **2.6.1b**
- Evidence: The trimmed and quality-filtered reads were mapped to the Arabidopsis genome (TAIR10) using STAR (v.2.6.1b) 47 with default parameters and transformed to a count per gene per library using featureCounts (v.1.6.0) 48 .
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: Adapters were trimmed with Trimgalore (v.0.6.7) and trimmed reads were aligned to GRCm38 with STAR 43 (v.2.6.1d) and quantified with Salmon 44 (v1.5.2).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Version used: **2.6.1**
- Evidence: High-quality reads were then mapped to the mm39 reference mouse genome (GRCm39) using STAR (v2.6.1; https://github.com/alexdobin/STAR ) and quantified using Salmon (v1.4.0; https://combine-lab.github.io/salmon ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Engineered extrachromosomal oncogene amplifications promote tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08318-8 | PMCID: PMC11754114 | PMID: 39695225
- Evidence: Reads were mapped to mm10 using the STAR aligner 52 , and differential gene expression was calculated using the DESeq2 R package 53 .
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, R, STAR] -> quantification [MACS2 v3.0.0b, deepTools v3.5.3] -> differential/statistical testing [DESeq2, R, STAR] -> stage not stated [CNVkit v0.9.10, fgsea]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Version used: **2.7**
- Evidence: RNA-seq samples were aligned using STAR (v.2.7) 69 with --outFilterMultimapNmax 1.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Evidence: Reads were then aligned with STAR 54 (v2.7.10a) and mapped to GRCh38.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **2.7.11a**
- Evidence: Raw Fastq files were trimmed and aligned to the mouse reference genome (mm10) using STAR (v.2.7.11a) 58 .
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Version used: **2.7.11b**
- Evidence: Data preprocessing Processing of generated bulk RNA-seq data Reads from both bulk RNA-seq datasets (ITP and Klotho -KO) were mapped to the mouse genome (GRCm39) with STAR (v2.7.11b) 192 and counted via featureCounts (v2.0.6) 193 .
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Androgen loss accelerates brain tumour growth via HPA axis activation. (Nature 2026)

- DOI: 10.1038/s41586-026-10451-5 | PMCID: PMC13216072 | PMID: 42092136
- Version used: **2.7.3a**
- Evidence: Reads were aligned to the GRCm38 (mm10) mouse reference genome using STAR (v.2.7.3a) 60 .
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [STAR v2.7.3a, Salmon v0.14.1, clusterProfiler v4.14.6] -> quantification [R v4.4.1, Salmon v0.14.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.46.0, clusterProfiler v4.14.6, limma] -> stage not stated [CellChat v2.1.2, Python v3.12.8, QuPath, Seurat v5.2.1, fgsea]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: Sequencing reads were aligned to the GRCh38 genome (hg38) using the STAR aligner (v2.7.11b) with a pre-built RSEM index 65 .
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Version used: **2.7.3a**
- Evidence: The trimmed FASTQ files were then aligned to the human genome (hg19/GRCh37) using STAR (v2.7.3a) based on Genecode v19 annotations.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **2.7.9a**
- Evidence: STAR (v.2.7.9a) was used to map reads to the hg38 reference genome (GRCh38.p13; GENCODE).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **2.7.10b**
- Evidence: In a second step, reads were aligned to the GRCh38 reference genome (Ensembl release 110) using STAR (v.2.7.10b) 90 .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Version used: **2.7.9a**
- Evidence: Briefly, FASTQ files underwent quality control (FastQC v.0.12.1), adaptors were trimmed (Trim Galore! v.0.6.7), reads were aligned to the GRCh38 human reference transcriptome (STAR v.2.7.9a) and a gene expression matrix was generated (Salmon v.1.10.1).
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **2.5.4b**
- Evidence: Within each chunk of an RNA sublibrary, we performed barcode matching, 10 bp UMI parsing from Read2, and adapter trimming for Read1 only, followed by genome alignment with STAR (v2.5.4b) 95 , gene annotation with featureCounts (v2.0.1) 96 , and conversion of the output BAM file to a more storage-efficient TSV format.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **2.7.9**
- Evidence: The analysis was performed separately using three-field and four-field HLA alleles with AF > 0.05. eQTL analysis To quantify gene expression levels, RNA-seq reads were aligned to GRCh38 using STAR (v.2.7.9) 128 with GENCODE (v.40) annotation.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **2.7.0**
- Evidence: The resulting reads were mapped to the reference genomes (Ensembl 92) using STAR (v.2.7.0; RRID SCR_015899 ).
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Version used: **2.7.9a**
- Evidence: Indexing of the ENSEMBL GRCm39 reference genome as well as alignment of sequencing reads was performed using STAR version 2.7.9a (ref.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Version used: **2.7.10b**
- Evidence: The quality-controlled reads were mapped to concatenated reference genome sequences of the T19-derived 33 stains using STAR v.2.7.10b with ‘outFilterMultimapNmax: 20 alignIntronMax: 1’ parameters.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: Trimmed FASTQ files were subsequently aligned to the mm10 genome using the STAR alignment software v.2.5.2b, with the flags --outSAMAttributes All, --outFilterMultimapNmax 10, --outFilterMultimapScoreRange 1, --outFilterScoreMin 10, --alignEndsType EndToEnd.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Reduced cyclin D3 expression in erythroid cells protects against malaria. (Nature 2026)

- DOI: 10.1038/s41586-026-10110-9 | PMCID: PMC12999499 | PMID: 41708853
- Evidence: RNA-seq reads were aligned using STAR software (v.2.7.10b) 61 against a transcriptome reference generated by RSEM software (v.1.3.1) 62 .
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [ImageJ] -> differential/statistical testing [VCFtools v0.1.12b] -> stage not stated [MACS2]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Version used: **2.4.2a**
- Evidence: Further, RNA reads were aligned to the hg19 reference genome using STAR (v.2.4.2a) 35 for phasing somatic with germline variants, as well as for determining the relative expression of a mutated transcript in comparison to the transcript not carrying the somatic mutation.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Cleavage of mRNAs by a minority of pachytene piRNAs improves sperm fitness. (Nature 2026)

- DOI: 10.1038/s41586-026-10102-9 | PMCID: PMC13061629 | PMID: 41639461
- Version used: **2.3.1**
- Evidence: Unaligned reads were mapped to mouse genome mm10 using STAR (v.2.3.1) 63 , and PCR were duplicates removed 54 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.18.1]

### Single-molecule dynamics of the TRiC chaperonin system in vivo. (Nature 2026)

- DOI: 10.1038/s41586-025-10073-3 | PMCID: PMC13061604 | PMID: 41639457
- Version used: **2.7.10a**
- Evidence: The remaining unaligned reads were mapped against the human genome (hg38) using STAR (v.2.7.10a) with parameters ‘--outFilterMismatchNmax 2 --quantMode TranscriptomeSAM GeneCounts --outSAMattributes MD NH --outFilterMultimapNmax 1’.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10a] -> visualisation [AlphaFold] -> stage not stated [TrackMate]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: Trimmed reads were subsequently aligned to the mouse genome version mm10 using STAR aligner (v.2.7.0d_0221) 67 with parameters according to ENCODE long RNA-seq pipeline ( https://github.com/ENCODE-DCC/long-rna-seq-pipeline ).
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Ontogeny and transcriptional regulation of Thetis cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10198-z | PMCID: PMC13171621 | PMID: 41634202
- Version used: **2.7.11a**
- Evidence: The combined FASTQ files were aligned to the mouse reference genome (GRCm38.p6 from GENCODE release M25) and counted using zUMIs v2.9.7e with STAR v.2.7.11a.
- Full pipeline: read trimming [Seurat v4.4.0] -> alignment/mapping [STAR v2.7.11a] -> dimensionality reduction/clustering [ArchR v1.0.3, Scanpy, UMAP] -> visualisation [ArchR v1.0.3, UMAP]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **2.5.2b**
- Evidence: The reads were mapped to the human genome (hg38) with Gencode v.25 annotations using STAR (v.2.5.2b) 110 and gene expression was quantified using RSEM (v.1.3.0) 111 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Version used: **2.7.7a**
- Evidence: In brief, data were trimmed using cutadapt (v.2.9) 75 , quality checked before and after trimming using FastQC (v.0.11.9), and then mapped and quantified using STAR (v.2.7.7a) 76 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Version used: **2.7.7a**
- Evidence: Sequences were trimmed using TrimGalore (v.0.6.5) and aligned to hg38 using STAR (v.2.7.7a) with the genome file GCA_000001405.15_GRCh38.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Single ended short reads from RNA-seq experiments were quality trimmed using fastp 61 and aligned using the STAR aligner 69 .
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Version used: **2.7.1**
- Evidence: In short, reads with valid barcodes were trimmed by template switching oligonucleotide sequence and aligned using STAR v.2.7.1 with MAPQ adjustment.
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Albumin orchestrates a natural host defence mechanism against mucormycosis. (Nature 2026)

- DOI: 10.1038/s41586-025-09882-3 | PMCID: PMC12804082 | PMID: 41501454
- Evidence: Sequencing reads were aligned to the reference genome ( R. delemar 99-880) using STAR aligner (v.2.7.10) 68 .
- Full pipeline: alignment/mapping [STAR, featureCounts] -> differential/statistical testing [R v4.3.1] -> visualisation [R v4.3.1] -> stage not stated [Fiji, GSEA, ImageJ, pheatmap]

### NAC controls nascent chain fate through tunnel sensing and chaperone action. (Nature 2026)

- DOI: 10.1038/s41586-025-10058-2 | PMCID: PMC13043293 | PMID: 41430436
- Evidence: Briefly, after removing the adaptors and non-coding RNAs as described above, reads were aligned to genome using STAR 80 .
- Full pipeline: read trimming [Cutadapt v1.4.2] -> alignment/mapping [STAR] -> stage not stated [AlphaFold]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: Alignment to the mm10 genome was performed using STAR aligner (v.2.5.1b).
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Sequences were aligned to the mouse mm10 genome using STAR aligner (v.2.4.0j).
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **2.7.9a**
- Evidence: Unaligned reads were subsequently aligned to the C. elegans genome (WBcel235/ce11) using STAR (v.2.7.9a) with the following parameters: --readFilesCommand zcat --alignEndsType Local --outFilterMatchNmin 100 --outFilterScoreMin 100 --outFilterIntronMotifs RemoveNoncanonical --outFilterMultimapNmax 1 --outFilterType BySJout --outSAMunmapped Within --outReadsUnmapped Fastx.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Version used: **2.7.10b**
- Evidence: The remaining sequences were aligned to the human GRCh38 genome (Ensembl v112) using STAR (v.2.7.10b) 64 .
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Evidence: Reads were aligned using STAR 55 to the GRCH38 genome containing a single ribosomal DNA (chrR), originally generated by the Paralkar laboratory 56 .
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Full lentiviral construct sequences (Addgene plasmids #142908 and #142826) were included as additional reference contigs and indexed together with hg38 as a reference genome using STAR aligner 82 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Secretome translation shaped by lysosomes and lunapark-marked ER junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-09718-0 | PMCID: PMC12727531 | PMID: 41193816
- Version used: **2.7.5c**
- Evidence: Sequencing adapters were trimmed from the reads using Cutadapt v2.10 prior to alignment with STAR v2.7.5c against the Homo sapiens GRCh38 genome assembly from Ensembl.
- Full pipeline: read trimming [Cutadapt v2.10, STAR v2.7.5c] -> alignment/mapping [Cutadapt v2.10, STAR v2.7.5c] -> quantification [CellProfiler] -> stage not stated [DESeq2, ImageJ, TrackMate]

### Monoclonal antibody-mediated neutralization of SARS-CoV-2 in an IRF9-deficient child. (PNAS 2021)

- DOI: 10.1073/pnas.2114390118 | PMCID: PMC8609338 | PMID: 34702736
- Evidence: The sequencing reads were mapped onto the human reference genome GRCh38 with STAR aligner v2.7, and the mapped reads were then quantified to determine the gene-level read counts, with featureCounts v2.0.2.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.2] -> quantification [DESeq2, STAR, featureCounts v2.0.2] -> normalisation [DESeq2]

### The translatome of neuronal cell bodies, dendrites, and axons. (PNAS 2021)

- DOI: 10.1073/pnas.2113929118 | PMCID: PMC8639352 | PMID: 34670838
- Version used: **2.7.3**
- Evidence: The remaining reads were aligned to the rat genome (rn6) with the split-aware aligner STAR version 2.7.3.a ( 65 ) with the following arguments: –twopassMode Basic –twopass1readsN -1 –seedSearchStartLmax 15 –outSJfilterOverhangMin 15 8 8 8 –outFilterMismatchNoverReadLmax 0.1.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, Cutadapt] -> alignment/mapping [Bowtie2 v2.3.5.1, STAR v2.7.3, featureCounts v2.0.0] -> stage not stated [DESeq2 v1.30.1, Python]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Version used: **2.5.3a**
- Evidence: For generating genome-guided transcriptome assemblies, trimmed reads were first mapped against the genomes using STAR v2.5.3a ( 75 ) under the “2-pass mapping” mode and default parameters.
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Version used: **2.7.5b**
- Evidence: Mapping of reads to the genome and gene counts were performed using RNA-STAR v2.7.5b ( 67 ) and Galaxy ( 68 ) through the usegalaxy.eu server, and read counts over genes were obtained using htseq-count v0.9.1+galaxy1 ( 69 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Evidence: The splice-aware STAR aligner v.2.7.2b ( 66 ) was used to align the remaining reads against a genome index of the barley reference sequence and annotation of genotype Morex (IBSC v2.0) ( 26 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### Longer or shorter spines: Reciprocal trait evolution in stickleback via triallelic regulatory changes in <i>Stanniocalcin2a</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2100694118 | PMCID: PMC8346906 | PMID: 34321354
- Evidence: We generated an average of 14.5 M 150-bp paired-end Illumina reads for each library and aligned to gasAcu1-4 with STAR two-pass mapping ( 36 ).
- Full pipeline: alignment/mapping [GATK, STAR]

### TET2 as a tumor suppressor and therapeutic target in T-cell acute lymphoblastic leukemia. (PNAS 2021)

- DOI: 10.1073/pnas.2110758118 | PMCID: PMC8403940 | PMID: 34413196
- Version used: **2.6.0c**
- Evidence: Fetal RNA-seq samples from GSE111930 were aligned using STAR v2.6.0c ( 76 ).
- Full pipeline: alignment/mapping [STAR v2.6.0c] -> quantification [ImageJ] -> stage not stated [R]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Evidence: Alignment of sequencing reads was performed with the Cell Ranger Single-Cell Software Suite 3.0 (10× Genomics) using STAR aligner ( 73 ) on the University of Southern California High Performance Cluster.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### Molecular design of the γδT cell receptor ectodomain encodes biologically fit ligand recognition in the absence of mechanosensing. (PNAS 2021)

- DOI: 10.1073/pnas.2023050118 | PMCID: PMC8256041 | PMID: 34172580
- Evidence: The output fastq files were aligned against the Ensembl GRCm38.75 reference genome using STAR aligner (v2.5) ( 86 ) and the resultant binary alignment map (BAM)-format files were filtered to retain only primary-aligned reads (samtools view -F 0 × 0100).
- Full pipeline: alignment/mapping [SAMtools, STAR] -> quantification [DESeq2 v1.6.3, featureCounts v1.4.4] -> differential/statistical testing [DESeq2 v1.6.3, featureCounts v1.4.4]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: To identify human–SARS-CoV-2 chimeric DNA reads, raw sequencing reads were aligned with STAR ( 70 ) (version 2.7.1a) to a human plus SARS-CoV-2 genome made with a fasta file containing the human genome sequence version hg38 with no alternative chromosomes concatenated to the SARS-CoV-2 sequence from National Center for Biotechnology Information (NCBI) reference sequence NC_045512.2 .
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### Cytokine receptor clustering in sensory neurons with an engineered cytokine fusion protein triggers unique pain resolution pathways. (PNAS 2021)

- DOI: 10.1073/pnas.2009647118 | PMCID: PMC7980471 | PMID: 33836560
- Evidence: The sequencing reads from each sample were aligned to the recent reference human genome GRCh38 build 79 assembly from Ensembl (Genome Reference Consortium Mouse Build 38) using the STAR aligner ( 79 , 80 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR]

### Mitochondrial metabolism is essential for invariant natural killer T cell development and function. (PNAS 2021)

- DOI: 10.1073/pnas.2021385118 | PMCID: PMC8020658 | PMID: 33753493
- Evidence: Reads were analyzed through the Ceto pipeline ( https://github.com/ebartom/NGSbartom ) using STAR ( 71 ) for alignment on mm10 mouse genome, HTSEq.
- Full pipeline: alignment/mapping [STAR] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### Pluripotent stem cell-derived epithelium misidentified as brain microvascular endothelium requires ETS factors to acquire vascular fate. (PNAS 2021)

- DOI: 10.1073/pnas.2016950118 | PMCID: PMC7923590 | PMID: 33542154
- Evidence: The resultant filtered reads were mapped to human reference genome GRCh38 using STAR aligner ( 66 ) and gene-wise expression counts generated using the “-quantMode GeneCounts” parameter.
- Full pipeline: quality control [FastQC v0.11.5, R, edgeR] -> read trimming [R, STAR, edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### A genome-scale CRISPR screen reveals factors regulating Wnt-dependent renewal of mouse gastric epithelial cells. (PNAS 2021)

- DOI: 10.1073/pnas.2016806118 | PMCID: PMC7848749 | PMID: 33479180
- Version used: **2.7.2b**
- Evidence: Obtained reads were mapped to the mouse mm9 genome using STAR (v2.7.2b).
- Full pipeline: read trimming [Cutadapt v1.16, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.2b] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [featureCounts v1.6.1]

### OCT4 induces embryonic pluripotency via STAT3 signaling and metabolic mechanisms. (PNAS 2021)

- DOI: 10.1073/pnas.2008890118 | PMCID: PMC7826362 | PMID: 33452132
- Evidence: Genome build GRCm38/mm10 and STAR (spliced transcripts alignment to a reference) 2.5.2a ( 85 ) were used for aligning reads and Ensembl release 87 ( 86 ) was used to guide gene annotation.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> variant calling [WGCNA] -> quantification [Bioconductor, HTSeq] -> dimensionality reduction/clustering [Bioconductor, WGCNA] -> differential/statistical testing [GSEA, R]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Version used: **2.5.2**
- Evidence: Barcodes, adapter sequences, and UMIs were stripped from the reads which were then aligned to the human GRCh38.p7 reference using STAR v.2.5.2.
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Version used: **2.5.2b**
- Evidence: Reads from each cell were mapped to human reference genome (hg19) by STAR version 2.5.2b ( 44 ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Inflammatory response to retrotransposons drives tumor drug resistance that can be prevented by reverse transcriptase inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2213146119 | PMCID: PMC9894111 | PMID: 36449545
- Evidence: Reads were aligned to the mouse reference genome (University of California, Santa Cruz (UCSC) mm10/GRCm38) with STAR RNA-seq aligner ( 50 ) using annotation from the same source.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [featureCounts]

### Transcriptional control of cone photoreceptor diversity by a thyroid hormone receptor. (PNAS 2022)

- DOI: 10.1073/pnas.2209884119 | PMCID: PMC9894165 | PMID: 36454759
- Version used: **2.7.3a**
- Evidence: Ten–20 million single-end 50 base reads/per library were collected, converted by bcl2fastq (version 2) into fastq files and aligned on (GRCm38/mm10) with STAR (version 2.7.3a) ( 55 ).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [deepTools] -> differential/statistical testing [DESeq2, MACS2 v2.2.7.1, edgeR] -> visualisation [deepTools]

### Hedgehog-interacting protein acts in the habenula to regulate nicotine intake. (PNAS 2022)

- DOI: 10.1073/pnas.2209870119 | PMCID: PMC9674224 | PMID: 36346845
- Evidence: RNA-seq reads were aligned to the UCSC mm10 reference genome using STAR ( 89 ), version 2.3.0e_r291, with default settings.
- Full pipeline: alignment/mapping [HTSeq, STAR, Scanpy] -> quantification [HTSeq] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Enrichr]

### Combination of common mtDNA variants results in mitochondrial dysfunction and a connective tissue dysregulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212417119 | PMCID: PMC9659340 | PMID: 36322731
- Evidence: Eighteen Human Tourette RNA-sequencing Fastq files, consisting of 6 controls and 12 mutant samples, were processed using the STAR alignment ( 42 ) tool and subsequently normalized using the RSEM ( 43 ) package based upon the hg38 reference genome ( 44 ) and the Gencode version 23 gene annotation ( 45 ).
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [R, limma] -> stage not stated [GSEA]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Evidence: RNA sequencing reads in the form of FASTQ files underwent quality control, trimming of adaptors (trimgalore/0.4.5), and they were mapped to the reference genome GRCh38 using Spliced Transcript Alignment to a Reference (STAR) aligner (star/2.7.3a).
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### Polycomb group (PcG) proteins prevent the assembly of abnormal synaptonemal complex structures during meiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2204701119 | PMCID: PMC9586294 | PMID: 36215502
- Evidence: RNA-seq reads were aligned against the D. melanogaster BDGP release 6 genome using the STAR aligner ( 70 ).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR, deepTools] -> normalisation [R, deepTools, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [MACS2]

### DNA polymerase epsilon interacts with SUVH2/9 to repress the expression of genes associated with meiotic DSB hotspot in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208441119 | PMCID: PMC9564942 | PMID: 36191225
- Version used: **2.7.9a**
- Evidence: Raw reads were trimmed with Cutadapt and mapped to TAIR10 using STAR version 2.7.9a ( 68 ) with parameters “–alignIntronMax 5000 –outSAMmultNmax 1 –outFilterMultimapNmax 50 –outFilterMismatchNoverLmax 0.1.” DE genes and TEs (fold change ≥2 and P < 0.01) were identified by the R package DESeq2 version 1.30.1 ( 69 ) based on the gene expression matrix quantified by featureCounts version 2.0.0 ( 70 )...
- Full pipeline: read trimming [Bismark v0.22.3, Cutadapt, STAR v2.7.9a] -> alignment/mapping [Bismark v0.22.3, Bowtie2, Cutadapt, STAR v2.7.9a] -> quantification [Bismark v0.22.3, Cutadapt, DESeq2 v1.30.1, R, STAR v2.7.9a, featureCounts v2.0.0] -> stage not stated [ImageJ v1.52]

### Reduced Satb1 expression predisposes CD4<sup>+</sup> T conventional cells to Treg suppression and promotes transplant survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205062119 | PMCID: PMC9546564 | PMID: 36161903
- Version used: **2.5.3a**
- Evidence: The raw sequences were aligned to mouse reference genome GRCm38 using STAR (version 2.5.3a) ( 54 ).
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [STAR v2.5.3a, featureCounts] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [R v3.4.1] -> differential/statistical testing [edgeR]

### Siponimod ameliorates metabolic oligodendrocyte injury via the sphingosine-1 phosphate receptor 5. (PNAS 2022)

- DOI: 10.1073/pnas.2204509119 | PMCID: PMC9546621 | PMID: 36161894
- Version used: **2.6.1d**
- Evidence: Subsequently, the reads were aligned to the mm10 reference genome sequence using STAR v2.6.1d ( 60 ) with default parameters.
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [STAR v2.6.1d]

### Mafba and Mafbb regulate microglial colonization of zebrafish brain via controlling chemotaxis receptor expression. (PNAS 2022)

- DOI: 10.1073/pnas.2203273119 | PMCID: PMC9522419 | PMID: 36122226
- Evidence: Raw reads were first aligned to zebrafish reference genome GRCz11.94 using STAR aligner.
- Full pipeline: alignment/mapping [STAR] -> quantification [featureCounts] -> stage not stated [ImageJ]

### Arsenite toxicity is regulated by queuine availability and oxidation-induced reprogramming of the human tRNA epitranscriptome. (PNAS 2022)

- DOI: 10.1073/pnas.2123529119 | PMCID: PMC9499598 | PMID: 36095201
- Evidence: The reads were aligned using STAR ( 61 ).
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [ImageJ]

### SARS-CoV-2 variant spike and accessory gene mutations alter pathogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2204717119 | PMCID: PMC9477415 | PMID: 36040867
- Version used: **2.7.8a**
- Evidence: Reads were preprocessed using Cutadapt v3.4 and then aligned to the murine genome (assembly GRCm38) using STAR v2.7.8a ( 17 , 18 ).
- Full pipeline: alignment/mapping [Cutadapt v3.4, STAR v2.7.8a] -> differential/statistical testing [DESeq2 v4.1.0, R v4.1.1]

### USP13 promotes deubiquitination of ZHX2 and tumorigenesis in kidney cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2119854119 | PMCID: PMC9457248 | PMID: 36037364
- Version used: **2.5.2b**
- Evidence: Reads were aligned to the reference genome (hg19) using STAR (v2.5.2b) by retaining only primary alignments ( 42 ).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.14.1] -> differential/statistical testing [DESeq2 v1.14.1]

### False-positive IRESes from &lt;i&gt;Hoxa9&lt;/i&gt; and other genes resulting from errors in mammalian 5' UTR annotations. (PNAS 2022)

- DOI: 10.1073/pnas.2122170119 | PMCID: PMC9456764 | PMID: 36037358
- Evidence: The processed data were aligned to the mouse genome using STAR.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [scikit-learn] -> stage not stated [BEDTools, Cutadapt]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Reads were aligned to the hg38 genome in STAR ( 41 ) v2.6.1 and quantified with featureCounts ( 42 ) v1.6.3.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### Tumor-polarized GPX3&lt;sup&gt;+&lt;/sup&gt; AT2 lung epithelial cells promote premetastatic niche formation. (PNAS 2022)

- DOI: 10.1073/pnas.2201899119 | PMCID: PMC9371733 | PMID: 35914155
- Evidence: FASTQs generated from Illumina sequencing output were aligned to the mouse genome with the STAR algorithm ( 37 ), version GRCm38.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Monocle, clusterProfiler v3.14.0] -> differential/statistical testing [GSEA, clusterProfiler v3.14.0] -> stage not stated [Seurat v3.0.2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **2.5.0a**
- Evidence: Reads were mapped to the mouse genome mm10 assembly using STAR (v2.5.0a) ( 48 ).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Evidence: Bulk RNAseq data were processed and aligned to GalGal6 using the default NF-core RNAseq (v2.0) pipeline ( 76 ), which uses the STAR aligner.
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### STING activation promotes robust immune response and NK cell-mediated tumor regression in glioblastoma models. (PNAS 2022)

- DOI: 10.1073/pnas.2111003119 | PMCID: PMC9282249 | PMID: 35787058
- Evidence: Sequencing reads were aligned using STAR ( 90 ) with an average of 3E7 uniquely mapped reads per sample and a mismatch rate per base of <1%.
- Full pipeline: alignment/mapping [STAR] -> quantification [QuPath] -> differential/statistical testing [DESeq2, R, ggplot2] -> stage not stated [Enrichr, ImageJ]

### Leafy and weedy seadragon genomes connect genic and repetitive DNA features to the extravagant biology of syngnathid fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2119602119 | PMCID: PMC9245644 | PMID: 35733255
- Evidence: We trimmed Illumina adaptors and low-quality regions from reads using process_shortreads from the Stacks software suite ( 25 , 26 ) and aligned cleaned RNA-seq reads from both seadragon species to both P. taeniolatus and P. eques genome assemblies using STAR aligner ( 27 ). miRNA-Seq.
- Full pipeline: read trimming [STAR] -> alignment/mapping [InterProScan, STAR] -> dimensionality reduction/clustering [BLAST] -> stage not stated [BUSCO, Flye, RepeatMasker]

### Integrated screens uncover a cell surface tumor suppressor gene <i>KIRREL</i> involved in Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2121779119 | PMCID: PMC9231494 | PMID: 35704761
- Version used: **2.5.3a**
- Evidence: Genome mapping was conducted using STAR (version 2.5.3a) and the human reference genome (GRCh38).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [STAR v2.5.3a] -> quantification [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [STRING db]

### Nuclear speckle integrity and function require TAO2 kinase. (PNAS 2022)

- DOI: 10.1073/pnas.2206046119 | PMCID: PMC9231605 | PMID: 35704758
- Evidence: Quality control–filtered trimmed sequences were aligned to hg19 using STAR ( 46 ).
- Full pipeline: quality control [STAR] -> read trimming [STAR, Trimmomatic] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [Bioconductor v3.11, R v4.0.2]

### In situ structure of intestinal apical surface reveals nanobristles on microvilli. (PNAS 2022)

- DOI: 10.1073/pnas.2122249119 | PMCID: PMC9214534 | PMID: 35666862
- Version used: **2.6.0c**
- Evidence: The Read 1 was split by different cell barcodes in Read 2 and mapped to the C. elegans genome (WS263) by zUMIs (v0.0.6) and STAR (v2.6.0c).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [IMOD, STAR v2.6.0c] -> stage not stated [ImageJ, MotionCor2, UCSF Chimera]

### GPR174 signals via G&lt;i&gt;α&lt;/i&gt;s to control a CD86-containing gene expression program in B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2201794119 | PMCID: PMC9191659 | PMID: 35639700
- Evidence: Sequences were aligned to the mm10 genome with STAR and mapped reads of each gene were counted with HTseq.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [MACS2, pheatmap]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Version used: **2.6**
- Evidence: STAR (v2.6) ( 80 ) aligned FASTQ reads to the mouse mm10 reference genome with annotations from Ensembl release 93 ( 81 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Induction of human trophoblast stem-like cells from primed pluripotent stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2115709119 | PMCID: PMC9171790 | PMID: 35537047
- Version used: **2.5.2b**
- Evidence: Paired-end reads from RNA-seq were aligned to the reference human genome (hg38) using STAR (v2.5.2b) ( 47 ).
- Full pipeline: alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.32.0, R] -> normalisation [DESeq2 v1.32.0, R] -> differential/statistical testing [limma v3.48.3]

### Genomewide CRISPR knockout screen identified PLAC8 as an essential factor for SADS-CoVs infection. (PNAS 2022)

- DOI: 10.1073/pnas.2118126119 | PMCID: PMC9170153 | PMID: 35476513
- Version used: **2.7.7a**
- Evidence: Trimmed reads were aligned to the human genome (hg19) using STAR version 2.7.7a with the parameters --peOverlapNbasesMin 30 --outSAMtype BAM SortedByCoordinate .
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [STAR v2.7.7a] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [R v4.0.3] -> stage not stated [Cytoscape, SAMtools v1.12, featureCounts]

### Mitochondrial mutations alter endurance exercise response and determinants in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2200549119 | PMCID: PMC9170171 | PMID: 35482926
- Evidence: RNASeq fastq files were processed using the Spliced Transcripts Alignment to a Reference (STAR) alignment tool and subsequently normalized using the RNA-Seq by Expectation-Maximization (RSEM) package based upon the mm10 reference genome and the gencode version M17 gene annotation.
- Full pipeline: alignment/mapping [RSEM, STAR] -> normalisation [R, RSEM, STAR, limma] -> differential/statistical testing [Metascape, R, limma] -> machine learning [Metascape] -> stage not stated [ANTs, GSEA, fgsea]

### Brap regulates liver morphology and hepatocyte turnover via modulation of the Hippo pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2201859119 | PMCID: PMC9171358 | PMID: 35476518
- Evidence: The reads were aligned to the mm10 genome using STAR [version 2.6.0c ( 24 )].
- Full pipeline: quality control [FastQC] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [R]

### MicroRNA-29a attenuates CD8 T cell exhaustion and induces memory-like CD8 T cells during chronic infection. (PNAS 2022)

- DOI: 10.1073/pnas.2106083119 | PMCID: PMC9169946 | PMID: 35446623
- Version used: **2.5.0**
- Evidence: Then STAR (version 2.5.0) was used to map reads to the reference genome GRCm38 ( 56 ).
- Full pipeline: quality control [FastQC v11.5] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [STAR v2.5.0, featureCounts v1.5.0] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, limma]

### The CHARGE syndrome ortholog CHD-7 regulates TGF-β pathways in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2109508119 | PMCID: PMC9169646 | PMID: 35394881
- Version used: **2.5.4a**
- Evidence: The remaining sequences were aligned against the reference genome of C. elegans WS260 using STAR (v2.5.4a).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.5.4a] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [Bioconductor v3.7, R v3.5]

### Signaling from the RNA sensor RIG-I is regulated by ufmylation. (PNAS 2022)

- DOI: 10.1073/pnas.2119531119 | PMCID: PMC9169834 | PMID: 35394863
- Evidence: Reads were mapped to the GRCh38v93 version of the human genome and transcriptome ( 67 ) using the STAR RNA-seq alignment tool ( 68 ).
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [HTSeq]

### Layered evolution of gene expression in "superfast" muscles for courtship. (PNAS 2022)

- DOI: 10.1073/pnas.2119671119 | PMCID: PMC9168950 | PMID: 35363565
- Version used: **2.7.3a**
- Evidence: Nonmitochondrial reads for each sample were mapped using STAR (v2.7.3a) ( 44 ) to the P. filicauda reference genome (v1; GenBank: GCA_003945595.1) using single-pass mode with the reference GTF and all other parameters default.
- Full pipeline: alignment/mapping [BCFtools, BWA, RAxML, STAR v2.7.3a] -> differential/statistical testing [limma] -> stage not stated [featureCounts v2.0.1]

### Prevention of the foreign body response to implantable medical devices by inflammasome inhibition. (PNAS 2022)

- DOI: 10.1073/pnas.2115857119 | PMCID: PMC8944905 | PMID: 35298334
- Evidence: Data were aligned to the mm10 mouse genome (Ensembl Release GRCm38.p5) with STAR (v020201) ( 48 ).
- Full pipeline: quality control [MultiQC v0.9, featureCounts v1.5.0] -> alignment/mapping [MultiQC v0.9, STAR] -> quantification [DESeq2, HTSeq, R v3.4] -> normalisation [DESeq2, R v3.4] -> dimensionality reduction/clustering [MultiQC v0.9] -> differential/statistical testing [DESeq2, R v3.4] -> stage not stated [ImageJ]

### Ferroptosis regulation by the NGLY1/NFE2L1 pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2118646119 | PMCID: PMC8931371 | PMID: 35271393
- Evidence: The remaining reads (≥98% of all reads across all conditions) were aligned to the hg19 human reference genome using STAR.
- Full pipeline: alignment/mapping [STAR]

### Gain of gene regulatory network interconnectivity at the origin of vertebrates. (PNAS 2022)

- DOI: 10.1073/pnas.2114802119 | PMCID: PMC8931241 | PMID: 35263228
- Version used: **2.5.3a**
- Evidence: For the data analysis, reads were aligned against GRCz10 (danRer10) and Bl71 assemblies using STAR v2.5.3a ( 44 ) and were assigned to genes using the HTSeq toolkit v0.11.2 ( 45 ).
- Full pipeline: alignment/mapping [Bowtie2, HTSeq, STAR v2.5.3a, kallisto] -> differential/statistical testing [DESeq2 v1.18.0, R v3.4] -> stage not stated [Cytoscape]

### Definition of a mouse microglial subset that regulates neuronal development and proinflammatory responses in the brain. (PNAS 2022)

- DOI: 10.1073/pnas.2116241119 | PMCID: PMC8872761 | PMID: 35177477
- Evidence: The trimmed reads were mapped to the Mus musculus reference genome (ENSEMBL) using STAR aligner v2.5.2b, a splice aligner that detects and incorporates splice junctions to align the entire read sequences.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> stage not stated [MACS2]

### Genetic analysis of cancer drivers reveals cohesin and CTCF as suppressors of PD-L1. (PNAS 2022)

- DOI: 10.1073/pnas.2120540119 | PMCID: PMC8851563 | PMID: 35149558
- Version used: **2.4.2a**
- Evidence: For U937, RNA-seq reads were mapped using STAR version 2.4.2a.
- Full pipeline: alignment/mapping [R, STAR v2.4.2a, featureCounts] -> quantification [DESeq2, GSEA, R, featureCounts]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Version used: **2.6.0c**
- Evidence: The reads were aligned to the mm10 genome using STAR (version 2.6.0c) ( 54 ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### SF3B1 mutant-induced missplicing of MAP3K7 causes anemia in myelodysplastic syndromes. (PNAS 2022)

- DOI: 10.1073/pnas.2111703119 | PMCID: PMC8740767 | PMID: 34930825
- Evidence: In order to annotate novel 3′ss that are not present in current datasets, we adopted the splice junction read output by STAR alignment ( 50 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ, featureCounts] -> normalisation [ImageJ] -> registration [featureCounts] -> differential/statistical testing [ImageJ]

### BRD9 regulates interferon-stimulated genes during macrophage activation via cooperation with BET protein BRD4. (PNAS 2022)

- DOI: 10.1073/pnas.2110812119 | PMCID: PMC8740701 | PMID: 34983841
- Evidence: Paired-end 42-bp, paired-end 75-bp, or single-end 75-bp reads were aligned to mm10 using Spliced Transcripts Alignment to a Reference (STAR) alignment tool (version 2.5).
- Full pipeline: alignment/mapping [STAR] -> quantification [HOMER] -> stage not stated [GSEA]

### Recruitment of an ancient branching program to suppress carpel development in maize flowers. (PNAS 2022)

- DOI: 10.1073/pnas.2115871119 | PMCID: PMC8764674 | PMID: 34996873
- Version used: **2.7.0**
- Evidence: These were then aligned to the Z. mays B73 v3 genome ( 76 ) and processed into BAM files using STAR (version 2.7.0) ( 88 ).
- Full pipeline: quality control [FastQC v0.69] -> read trimming [Trimmomatic v0.36.3] -> alignment/mapping [Bowtie2 v2.3.2.2, Galaxy, STAR v2.7.0] -> quantification [edgeR, featureCounts] -> dimensionality reduction/clustering [edgeR, featureCounts] -> visualisation [R, ggplot2] -> stage not stated [SAMtools, SnpEff v4.3a]

### A dicer-related helicase opposes the age-related pathology from SKN-1 activation in ASI neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2308565120 | PMCID: PMC10756303 | PMID: 38113255
- Version used: **2.7.6a**
- Evidence: Quality-trimmed reads were aligned to the C. elegans reference genome using STAR 2.7.6a.
- Full pipeline: read trimming [STAR v2.7.6a, Trim Galore] -> alignment/mapping [STAR v2.7.6a] -> quantification [DESeq2, R v3.5.2] -> differential/statistical testing [DESeq2, R v3.5.2] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.7.1, SAMtools v1.10]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Version used: **2.5.2**
- Evidence: RNA-seq reads were aligned to the hg19 genome using STAR version 2.5.2 ( 44 ), and only uniquely mapped reads with a two-mismatch threshold were considered for downstream analysis.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### &lt;i&gt;GRASSY TILLERS1&lt;/i&gt; (&lt;i&gt;GT1&lt;/i&gt;) and &lt;i&gt;SIX-ROWED SPIKE1&lt;/i&gt; (&lt;i&gt;VRS1&lt;/i&gt;) homologs share conserved roles in growth repression. (PNAS 2023)

- DOI: 10.1073/pnas.2311961120 | PMCID: PMC10742383 | PMID: 38096411
- Version used: **2.7.9a**
- Evidence: Sequenced RNA libraries were trimmed for quality using Trimmomatic and mapped to the Zea mays (maize) B73 version 5 genome using STAR 2.7.9a ( 78 , 79 ).
- Full pipeline: read trimming [STAR v2.7.9a, Trimmomatic] -> alignment/mapping [HTSeq, MAFFT, STAR v2.7.9a, Trimmomatic] -> differential/statistical testing [DESeq2] -> visualisation [IQ-TREE, R]

### Adaptive DNA amplification of synthetic gene circuit opens a way to overcome cancer chemoresistance. (PNAS 2023)

- DOI: 10.1073/pnas.2303114120 | PMCID: PMC10710087 | PMID: 38019857
- Version used: **2.6.1d**
- Evidence: The clean reads were mapped to the Chinese hamster ( C. griseus CriGri-PICRH-1.0, GCF_003668045.1) reference genome ( 25 , 26 ) complemented with the synthetic gene circuit sequence using STAR 2.6.1d.
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.6.1d] -> quantification [featureCounts] -> stage not stated [Fiji, ImageJ, R v4.1, fastp v0.20.1]

### Genome-wide detection of human intronic AG-gain variants located between splicing branchpoints and canonical splice acceptor sites. (PNAS 2023)

- DOI: 10.1073/pnas.2314225120 | PMCID: PMC10655562 | PMID: 37931111
- Evidence: The raw RNA-seq fastq data were inspected to ensure high quality, and then, RNA-seq reads were mapped onto the human reference genome GRCh38 with STAR aligner ( 38 ).
- Full pipeline: alignment/mapping [STAR]

### Activity-induced MeCP2 phosphorylation regulates retinogeniculate synapse refinement. (PNAS 2023)

- DOI: 10.1073/pnas.2310344120 | PMCID: PMC10623012 | PMID: 37871205
- Version used: **2.5.2b**
- Evidence: Trimmed reads were mapped to the mm10 RefSeq transcriptome and genome using STAR (v2.5.2b) ( 56 ).
- Full pipeline: read trimming [Bowtie2 v2.2.9, STAR v2.5.2b, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.2.9, STAR v2.5.2b] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.34.0, R v3.34.1, edgeR v3.34.1] -> stage not stated [SAMtools v0.1.19, featureCounts]

### mitoSplitter: A mitochondrial variants-based method for efficient demultiplexing of pooled single-cell RNA-seq. (PNAS 2023)

- DOI: 10.1073/pnas.2307722120 | PMCID: PMC10523499 | PMID: 37725654
- Version used: **2.7.3a**
- Evidence: The scRNA-seq data were aligned to the GRCh38 genome using CellRanger v3.1.0 (for 10× Genomic RNA-seq data) or zUMIs v2.9.7e ( 33 ) (for Well-Paired-Seq data), during the sequence alignment process, and the bulk mitochondria RNA-seq data were quality-filtered using cutadapt v1.18 ( 34 ) and aligned to the mitochondrial sequence in the GRCh38 genome using STAR v2.7.3a ( 35 ).
- Full pipeline: alignment/mapping [Cutadapt v1.18, STAR v2.7.3a, minimap2 v2.24] -> variant calling [Scanpy v1.9.1, minimap2 v2.24] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> stage not stated [scikit-learn v1.0.2]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: The cleaned reads were aligned to the Drosophila reference genome (dm6) using the STAR aligner, and the number of reads mapped to each annotated gene was counted using featureCounts.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus. (PNAS 2023)

- DOI: 10.1073/pnas.2310163120 | PMCID: PMC10515167 | PMID: 37703282
- Evidence: The reads were then aligned to tomato reference genome using STAR ( 38 ), and mapped reads with MAPQ 10 were counted and annotated to their corresponding genes using a script (available at https://github.com/BGIResearch/SAW ).
- Full pipeline: quality control [R, Seurat v4.1.0] -> alignment/mapping [STAR] -> normalisation [R, Seurat v4.1.0] -> dimensionality reduction/clustering [R, Seurat v4.1.0, UMAP, clusterProfiler] -> stage not stated [Monocle, velocyto]

### Cooperative regulation of coupled oncoprotein synthesis and stability in triple-negative breast cancer by EGFR and CDK12/13. (PNAS 2023)

- DOI: 10.1073/pnas.2221448120 | PMCID: PMC10515179 | PMID: 37695916
- Version used: **2.4.1a**
- Evidence: Reads were aligned using the alignment tool STAR v2.4.1a ( 88 ) following the proposed 2-pass strategy to first identify a splice junction database to improve the overall mapping quality.
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [RSEM v1.2.25, STAR v2.4.1a] -> quantification [ImageJ, RSEM v1.2.25] -> differential/statistical testing [DESeq2 v1.22.0] -> stage not stated [Bioconductor]

### Mouse models of <i>SYNGAP1</i>-related intellectual disability. (PNAS 2023)

- DOI: 10.1073/pnas.2308891120 | PMCID: PMC10500186 | PMID: 37669379
- Evidence: The quality of STAR alignments was assessed for evenness of coverage, ribosomal RNA content, exon and intron mapping rate, complexity, and other criteria using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), Qualimap ( 59 ), and MultiQC ( 60 ).
- Full pipeline: quality control [FastQC, MultiQC, STAR, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR, featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [GSEA, R]

### <i>Bcl6</i>, <i>Irf2</i>, and <i>Notch2</i> promote nonclassical monocyte development. (PNAS 2023)

- DOI: 10.1073/pnas.2220853120 | PMCID: PMC10469339 | PMID: 37607223
- Version used: **2.7.9a**
- Evidence: RNA-seq reads were aligned to mouse reference genome (GRCm38/ mm10) with STAR version 2.7.9a.
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> normalisation [Bioconductor, edgeR]

### Triple-negative breast tumors are dependent on mutant p53 for growth and survival. (PNAS 2023)

- DOI: 10.1073/pnas.2308807120 | PMCID: PMC10450424 | PMID: 37579145
- Evidence: STAR alignment to a mouse reference genome (GRCm38) was performed with default parameters to generate RNA-seq BAM files ( 31 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, GSEA]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **2.7.6**
- Evidence: Filtered mRNA-sequencing data for D. cochinchinensis (50.5 Gbp) and D. oliveri (54.4 Gbp) from a previous project ( 26 ) (NCBI BioProject: PRJNA593817) were aligned against the genome assembly using STAR v2.7.6 and assembled using the genome-guided mode of Trinity v2.13.2.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Engineered calprotectin-sensing probiotics for IBD surveillance in humans. (PNAS 2023)

- DOI: 10.1073/pnas.2221121120 | PMCID: PMC10410751 | PMID: 37523538
- Version used: **2.7.5**
- Evidence: Reads were aligned to the GCF_003546975.1 assembly of the E. coli Nissle 1917 reference genome with STAR (v2.7.5) using the GeneCounts option.
- Full pipeline: alignment/mapping [STAR v2.7.5] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [R v4.0.3, ggplot2 v3.3.0, pheatmap v1.0.12]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **2.7.4a**
- Evidence: To compare the transcriptomic profiles of A on B off and “solo” transformants relative to WT, 50-base single-end Illumina reads were filtered and trimmed with Trim Galore v0.6.7 and mapped with STAR v.2.7.4a to a reference genome combining the M. furfur CBS14141 nuclear genome and the a1 - NEO - b4 transgene sequence.
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: The sequence reads were aligned to the mm9 genome using STAR (Galaxy Version 2.7.8a+galaxy0) ( 43 ).
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### T cell deletional tolerance restricts AQP4 but not MOG CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2306572120 | PMCID: PMC10372680 | PMID: 37463205
- Version used: **2.5.1**
- Evidence: All datasets were analyzed using the Cell Ranger (v3.1.0) variable diversity joining (VDJ) function, which aligned reads to the GRCm38 Alts Ensembl reference (v3.1.0) using STAR (v2.5.1).
- Full pipeline: alignment/mapping [Clustal Omega, STAR v2.5.1]

### IL-7R licenses a population of epigenetically poised memory CD8<sup>+</sup> T cells with superior antitumor efficacy that are critical for melanoma memory. (PNAS 2023)

- DOI: 10.1073/pnas.2304319120 | PMCID: PMC10372654 | PMID: 37459511
- Evidence: Filtered reads were aligned to referen genome mm10 using STAR aligner and quantified using featureCounts.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, STAR, featureCounts] -> alignment/mapping [STAR, featureCounts] -> quantification [STAR, featureCounts] -> differential/statistical testing [DESeq2, R v4.0] -> stage not stated [RSEM]

### The parasite intraerythrocytic cycle and human circadian cycle are coupled during malaria infection. (PNAS 2023)

- DOI: 10.1073/pnas.2216522120 | PMCID: PMC10268210 | PMID: 37279274
- Version used: **2.7.5c**
- Evidence: Each participant's set of Fastq files were aligned to human and parasite genome reference files using STAR (version 2.7.5c) ( 44 ) and quantified using RSEM (version 1.3.3) ( 45 ).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7.5c] -> quantification [RSEM v1.3.3, STAR v2.7.5c]

### Paf1 complex subunit Rtf1 stimulates H2B ubiquitylation by interacting with the highly conserved N-terminal helix of Rad6. (PNAS 2023)

- DOI: 10.1073/pnas.2220041120 | PMCID: PMC10235976 | PMID: 37216505
- Version used: **2.7.5a**
- Evidence: Using STAR (v2.7.5a) aligner ( 71 ), all reads were first aligned to the K. lactis genome (Ensembl ASM251v1).
- Full pipeline: alignment/mapping [DESeq2, STAR v2.7.5a] -> quantification [DESeq2] -> stage not stated [AlphaFold, ComplexHeatmap, featureCounts]

### EGR4 is critical for cell-fate determination and phenotypic maintenance of geniculate ganglion neurons underlying sweet and umami taste. (PNAS 2023)

- DOI: 10.1073/pnas.2217595120 | PMCID: PMC10235952 | PMID: 37216536
- Version used: **2.5**
- Evidence: The sequence data were then mapped to the mouse reference genome mm10 using the RNA-seq aligner STAR (v.2.5) ( 59 ).
- Full pipeline: quality control [FastQC v0.11.5] -> alignment/mapping [STAR v2.5] -> differential/statistical testing [GSEA, edgeR v3.12.1] -> stage not stated [ImageJ]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: To create gene models, paired-end RNA-Seq Illumina reads were aligned to genome assembly using the STAR program [v2.7.7a; ( 56 )] with parameters --outSAMstrandField intronMotif --outSAMtype BAM SortedByCoordinate --alignIntronMax 20000.
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### <i>oskar</i> acts with the transcription factor Creb to regulate long-term memory in crickets. (PNAS 2023)

- DOI: 10.1073/pnas.2218506120 | PMCID: PMC10214185 | PMID: 37192168
- Version used: **2.7.0e**
- Evidence: 16 , including removing adapters and reads shorter than 20 nucleotides with Cutadapt v3.4 ( 66 ) and quantifying the gene expression in transcripts per million with RSEM v1.2.29 ( 67 ), using STAR v2.7.0e1 ( 68 ) as read mapper against the G. bimaculatus genome ( 36 ) ( SI Appendix , Table S8 ).
- Full pipeline: read trimming [Cutadapt v3.4, RSEM v1.2.29, STAR v2.7.0e] -> alignment/mapping [MAFFT v7.510] -> quantification [Cutadapt v3.4, ImageJ, RSEM v1.2.29, STAR v2.7.0e] -> visualisation [RAxML]

### IRIS: Discovery of cancer immunotherapy targets arising from pre-mRNA alternative splicing. (PNAS 2023)

- DOI: 10.1073/pnas.2221116120 | PMCID: PMC10214192 | PMID: 37192158
- Version used: **2.6.1d**
- Evidence: In this work, the IRIS RNA-seq data processing module used the reference human genome hg19 and STAR 2.6.1d ( 54 ) under the two-pass mode for RNA-seq read alignment.
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [Cufflinks v2.2.1, DESeq2 v1.26.0, featureCounts v2.0.1] -> normalisation [DESeq2 v1.26.0, featureCounts v2.0.1]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: Samples were mapped using the STAR aligner ( 56 ) to the GENCODE version 27 (GRCh38.p10) genome.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### CDYL reinforces male gonadal sex determination through epigenetically repressing <i>Wnt4</i> transcription in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2221499120 | PMCID: PMC10193937 | PMID: 37155872
- Evidence: Raw sequence reads were mapped to mm10 using STAR aligner.
- Full pipeline: alignment/mapping [STAR] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat] -> stage not stated [MACS2, featureCounts v1.6.4]

### Nonpathological inflammation drives the development of an avian flight adaptation. (PNAS 2023)

- DOI: 10.1073/pnas.2219757120 | PMCID: PMC10175837 | PMID: 37126698
- Version used: **2.70f**
- Evidence: The bioinformatic analysis was performed on a Linux platform utilizing a custom bioinformatics pipeline that included STAR (version 2.70f) alignment of reads, the SUBREAD featureCounts program (version 2.0.0) to produce count tables, and DESeq2 R software package (1.26.0; R version 2.6.3) for differential expression analysis.
- Full pipeline: quality control [FastQC] -> alignment/mapping [DESeq2, R v2.70f, STAR v2.70f, featureCounts] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, R v2.70f, STAR v2.70f, featureCounts]

### Modeling human skeletal development using human pluripotent stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2211510120 | PMCID: PMC10175848 | PMID: 37126720
- Version used: **2.7.3a**
- Evidence: Reads were aligned to hg38 using a Bpipe ( 92 ) RNA-Seq pipeline that incorporated FastQC quality control, adaptor trimming with Trimmomatic v.0.35 ( 93 ), mapping with STAR 2.7.3a ( 94 ), summarizing reads over genes with featureCounts ( 95 ), and MultiQC ( 96 ) to summarize the analyses.
- Full pipeline: quality control [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> read trimming [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> alignment/mapping [FastQC, MultiQC, STAR v2.7.3a, Trimmomatic v0.35, featureCounts] -> differential/statistical testing [Bioconductor, edgeR, limma] -> visualisation [ggplot2, tidyverse]

### Tumor progression is independent of tumor-associated macrophages in cell lineage-based mouse models of glioblastoma. (PNAS 2023)

- DOI: 10.1073/pnas.2222084120 | PMCID: PMC10120014 | PMID: 37040416
- Evidence: Samples were aligned using STAR to the mouse GRCm39 or GRCm38 reference genome for the sorted TAM RNAseq and the TAM depletion tumor RNAseq, respectively.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, R, fgsea]

### Phosphatidylserine-positive extracellular vesicles boost effector CD8<sup>+</sup> T cell responses during viral infection. (PNAS 2023)

- DOI: 10.1073/pnas.2210047120 | PMCID: PMC10120060 | PMID: 37040405
- Version used: **2.6.1d**
- Evidence: Sequencing reads were aligned to the mouse reference genome (version GRCm38.99) with STAR (version 2.6.1d).
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler]

### Derepression of Y-linked multicopy protamine-like genes interferes with sperm nuclear compaction in <i>D. melanogaster</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220576120 | PMCID: PMC10120018 | PMID: 37036962
- Version used: **2.7.1a**
- Evidence: The read pairs were mapped to the canonical chromosomes of the D. melanogaster genome (assembly BDGP6/dm6) using STAR 2.7.1a ( 48 ) ; default parameters, except “—alignIntronMax 25000,” indexed with all FlyBase genes (FB2020_06 Dmel Release 6.37) and the option “—sjdbOverhang 100.” Gene counts were obtained using featureCounts ( 49 ); v 2.0.1, with “-M –fraction -p -s 2.” After summing gene counts...
- Full pipeline: alignment/mapping [BEDTools, STAR v2.7.1a] -> quantification [BEDTools] -> normalisation [BEDTools] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts] -> stage not stated [ImageJ]

### Interrogating bromodomain inhibitor resistance in KMT2A-rearranged leukemia through combinatorial CRISPR screens. (PNAS 2023)

- DOI: 10.1073/pnas.2220134120 | PMCID: PMC10120025 | PMID: 37036970
- Version used: **2.7.1a**
- Evidence: Paired-end reads were mapped by STAR(v2.7.1a) using parameters “-c -p 4 --outFilterType BySJout --outFilterMultimapNmax 20 --alignSJoverhangMin 8 --alignSJstitchMismatchNmax 5 -1 5 5 --alignSJDBoverhangMin 10 --outFilterMismatchNmax 999 --outFilterMismatchNoverReadLmax 0.04 --alignIntronMin 20 --alignIntronMax 100000 --alignMatesGapMax 100000 --outSAMmapqUnique 60 --outSAMmultNmax 1 --outSAMstrand...
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [RSEM] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [GATK v4.1.2.0, GSEA]

### NAMPT-dependent NAD<sup>+</sup> biosynthesis controls circadian metabolism in a tissue-specific manner. (PNAS 2023)

- DOI: 10.1073/pnas.2220102120 | PMCID: PMC10083581 | PMID: 36996103
- Evidence: Reads were subjected to 38-bp paired-end sequencing on a NextSeq500 (Illumina) and aligned using STAR v.
- Full pipeline: alignment/mapping [STAR] -> stage not stated [R]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Evidence: Illumina NextSeq 500 with Paired End 42 bp × 42 bp reads was used for sequencing and demultiplexed read sequences and sequences were then aligned to the Homo sapiens (PAR-masked)/hg19 reference using STAR aligner (version 2.5.0a) and the RNA-Seq Alignment App (version 1.1.0) on Illumina Basespace.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Nasal administration of anti-CD3 mAb (Foralumab) downregulates <i>NKG7</i> and increases <i>TGFB1</i> and <i>GIMAP7</i> expression in T cells in subjects with COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2220272120 | PMCID: PMC10243127 | PMID: 36881624
- Evidence: The quantification was performed using the STAR aligner against the GRCh38 transcriptome.
- Full pipeline: read trimming [Seurat v4.1.1] -> alignment/mapping [STAR] -> quantification [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [Seurat v4.1.1] -> stage not stated [ggplot2 v3.3.6]

### Conserved reduction of m&lt;sup&gt;6&lt;/sup&gt;A RNA modifications during aging and neurodegeneration is linked to changes in synaptic transcripts. (PNAS 2023)

- DOI: 10.1073/pnas.2204933120 | PMCID: PMC9992849 | PMID: 36812208
- Evidence: Filtered reads were mapped to the human (hg38) or mouse (mm10) genome using the STAR aligner v2.5.2b ( 66 ).
- Full pipeline: read trimming [Cutadapt v1.11.0, STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v3.5.12, featureCounts v1.5.1] -> normalisation [DESeq2 v3.5.12, deepTools] -> differential/statistical testing [DESeq2 v3.5.12, ggplot2 v3.3.5] -> visualisation [deepTools, ggplot2 v3.3.5] -> stage not stated [Cytoscape v3.7.2, R v3.5.2, SAMtools v1.9.0]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **2.7.10a**
- Evidence: Reads were aligned to the M. lusitanicus MU402 genome ( https://mycocosm.jgi.doe.gov/Muccir1_3/Muccir1_3.home.html ) employing BWA-MEM v.0.7.17 for ChIP DNA, STAR v.2.7.10a for long RNA, and ShortStack v3.8.5 for sRNA reads.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Definition of the contribution of an Osteopontin-producing CD11c<sup>+</sup> microglial subset to Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2218915120 | PMCID: PMC9963365 | PMID: 36730200
- Evidence: The trimmed reads were mapped to the Mus musculus reference genome available on ENSEMBL using the STAR aligner v.2.5.2b, a splice aligner that detects splice junctions and incorporates them to help align entire read sequences, resulting in generation of BAM files.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [MACS2]

### The lncRNA LUCAT1 is elevated in inflammatory disease and restrains inflammation by regulating the splicing and stability of NR4A2. (PNAS 2023)

- DOI: 10.1073/pnas.2213715120 | PMCID: PMC9910463 | PMID: 36577072
- Version used: **2.6.1**
- Evidence: Remaining reads were aligned to the human genome (assembly GRCh38/hg38) using STAR v2.6.1 ( 63 ), and reads were counted using RSEM v1.3.1.
- Full pipeline: read trimming [Cutadapt, minimap2 v2.17] -> alignment/mapping [RSEM v1.3.1, STAR v2.6.1, minimap2 v2.17] -> stage not stated [Bioconductor v3.14]

### SKA2 enhances stress-related glucocorticoid receptor signaling through FKBP4-FKBP5 interactions in neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2417728121 | PMCID: PMC11670087 | PMID: 39705315
- Evidence: Reads were aligned to the NCBI GRCh38Decoy Refseq genome with the basespace application RNA-Seq Alignment (Version: 2.0.1 [workflow version 3.19.1.12+master]) that conducted both splice aware genome alignment with STAR alignment (version 2.6.1a) ( 68 ) and transcriptome quantification with Salmon (version 0.11.2) ( 69 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> stage not stated [ImageJ]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Version used: **2.7.10a**
- Evidence: To evaluate the concordance between RNA-seq alignments and BcTPS gene models, including visually inspecting exon–intron junctions and UTRs, the RNA-seq datasets were mapped to the Bcop_v2 genome using STAR (version 2.7.10a_alpha_220818) ( 60 ), agnostic of gene annotation sets.
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; inositol hexaphosphate pathways couple to RNA interference and pathogen defense. (PNAS 2024)

- DOI: 10.1073/pnas.2416982121 | PMCID: PMC11626161 | PMID: 39602251
- Evidence: The STAR aligner was used to map sequencing reads to transcripts in C. elegans ce11 reference genome.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> differential/statistical testing [edgeR] -> stage not stated [ImageJ]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Trimmed reads were aligned using “STAR” ( 64 ) version 2.7.9a and manual two-pass mode to the Atlantic salmon genome (Salmo_salar-GCA_905237065.2) downloaded from Ensembl.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### The glucocorticoid receptor potentiates aldosterone-induced transcription by the mineralocorticoid receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2413737121 | PMCID: PMC11588051 | PMID: 39541347
- Version used: **2.70**
- Evidence: RNA-seq alignment to mouse mm10 genome was performed by STAR 2.70 using the default parameters with the following modifications: “--genomeDir mm10-125 --outSAMunmapped Within --outFilterType BySJout --outFilterMultimapNmax 20 --outFilterMismatchNmax 999 --outFilterMismatchNoverLmax 0.04 --alignIntronMin 20 --alignIntronMax 1000000 --alignMatesGapMax 1000000 --alignSJoverhangMin 8 --limitSjdbInsert...
- Full pipeline: quality control [Cutadapt v1.18] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2, STAR v2.70] -> normalisation [DESeq2] -> stage not stated [HOMER, SAMtools]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: Specifically, we aligned the snRNAseq reads to a combined reference genome containing both human (GRCh38) and rat (Rnor_6.0) sequences using STAR aligner as implemented in the cellranger pipeline.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Implantable 3D printed hydrogels with intrinsic channels for liver tissue engineering. (PNAS 2024)

- DOI: 10.1073/pnas.2403322121 | PMCID: PMC11588097 | PMID: 39531491
- Evidence: The trimmed reads were mapped to the Rattus norvegicus Rnor6.0 reference genome available on ENSEMBL using the STAR aligner v.2.5.2b.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> stage not stated [GSEA]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Version used: **2.7.10a**
- Evidence: 2) STAR analysis: the cleaned sequencing reads were mapped to the reference genome with STAR (version 2.7.10a) using the parameters “--alignEndsType EndToEnd --alignIntronMax 1 --winAnchorMultimapNmax 5000 --outFilterMultimapNmax 5000.” The outFilterMultimapNmax setting was determined based on computational efficiency and genome properties after testing a range of values from 1,000 to 50,000.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Version used: **2.7.10a**
- Evidence: Filtered reads were aligned on mm10 using STAR version 2.7.10a ( 59 ) with the ENCODE parameters and a custom gtf ( https://doi.org/10.5281/zenodo.7510406 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### A CRISPR-Cas9 knockout screening identifies IRF2 as a key driver of OAS3/RNase L-mediated RNA decay during viral infection. (PNAS 2024)

- DOI: 10.1073/pnas.2412725121 | PMCID: PMC11551408 | PMID: 39475651
- Evidence: For ChiP-seq analysis of IRF2 and STAT2, raw reads were processed using STAR aligner ( 65 ) and aligned to the human genome GRCh38/hg19.
- Full pipeline: alignment/mapping [STAR]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Version used: **2.7**
- Evidence: The clean reads were aligned to the reference human genome (version GRCh38), utilizing STAR v2.7 ( 53 ) as the aligner.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: Reads were aligned to the TAIR10 genome using the STAR aligner, deduplicated using UMI-Tools, and counted with HTSeq-Count.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: Then, the STAR aligner ( 88 ) was used to build a STAR index using the most updated versions of the Apis mellifera genome (GCF_003254395.2 _ Amel_HAv3.1 _ genomic.fna) and gene annotations (GCF_003254395.2 _ Amel_HAv3.1 _ genomic.gtf), and used to align and map the reads to the Apis mellifera genome.
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Dynamics of transcription-coupled repair of cyclobutane pyrimidine dimers and (6-4) photoproducts in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416877121 | PMCID: PMC11536166 | PMID: 39441633
- Evidence: The adaptor trimming was performed with trimmomatic as originally applied with the following parameter: “TRAILING:3.” The alignment was performed with the STAR alignment tool (v 2.6.0).
- Full pipeline: read trimming [Cutadapt v3.4, STAR] -> alignment/mapping [Bowtie2 v2.4.5, STAR] -> stage not stated [BEDTools, Snakemake]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Version used: **2.7.10a**
- Evidence: Raw reads were quality filtered with Trimmomatic 0.36 ( 76 ) then mapped and quantified against the Burmese python reference genome ( 27 ) with STAR 2.7.10a ( 77 ).
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Abortive infection of bat fibroblasts with SARS-CoV-2. (PNAS 2024)

- DOI: 10.1073/pnas.2406773121 | PMCID: PMC11513954 | PMID: 39401365
- Evidence: Reads were mapped with STAR ( 38 ) using a genome index made with either the human genome sequence version hg38 or the bat genome sequence version mRhiFer1_v1.p.
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [DESeq2, GSEA]

### Transcriptional repression by HDAC3 mediates T cell exclusion from &lt;i&gt;Kras&lt;/i&gt; mutant lung tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2317694121 | PMCID: PMC11494357 | PMID: 39388266
- Evidence: Sequenced reads were aligned to the mouse mm10 genome using the STAR aligner.
- Full pipeline: alignment/mapping [HOMER, STAR] -> stage not stated [Enrichr, GSEA, QuPath]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Version used: **2.7.10a**
- Evidence: RNA-seq reads were mapped to the hg38 reference genome using STAR 2.7.10a (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### A sensitive assay for measuring whole-blood responses to type I IFNs. (PNAS 2024)

- DOI: 10.1073/pnas.2402983121 | PMCID: PMC11459193 | PMID: 39312669
- Version used: **2.6.1d**
- Evidence: All FASTQ sequences passed quality control tests and were aligned with the GRCh38 reference genome with STAR (2.6.1d).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, fgsea]

### ERRα and ERRγ coordinate expression of genes associated with Alzheimer's disease, inhibiting &lt;i&gt;DKK1&lt;/i&gt; to suppress tau phosphorylation. (PNAS 2024)

- DOI: 10.1073/pnas.2406854121 | PMCID: PMC11406303 | PMID: 39231208
- Version used: **2.7.10a**
- Evidence: Reads were aligned to the human genome assembly GRCh38.p13 using STAR (version 2.7.10a) and peak calling was performed using MACS2 (version 2.2.7.1).
- Full pipeline: alignment/mapping [MACS2 v2.2.7.1, STAR v2.7.10a] -> quantification [StringTie]

### Platelet-activating factor (PAF) promotes immunosuppressive neutrophil differentiation within tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2406748121 | PMCID: PMC11363292 | PMID: 39178229
- Evidence: Reads were aligned with STAR-2.7.0 and reads quantified with Subread-1.6.4.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> normalisation [DESeq2, pheatmap v1.0.12] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Conserved 5-methyluridine tRNA modification modulates ribosome translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2401743121 | PMCID: PMC11363252 | PMID: 39159370
- Version used: **2.7.8a**
- Evidence: Reads were mapped to the reference genome Saccharomyces_cerevisiae (ENSEMBL) using STAR v2.7.8a and assigned count estimates to genes with RSEM v1.3.3 ( 58 , 59 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v2.3] -> alignment/mapping [RSEM v1.3.3, STAR v2.7.8a] -> differential/statistical testing [DESeq2]

### Polyomavirus ALTOs, but not MTs, downregulate viral early gene expression by activating the NF-κB pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2403133121 | PMCID: PMC11348336 | PMID: 39141346
- Evidence: Alignment was performed against GRCm38 reference using STAR v-2.7.7a ( 42 ) in the two-pass alignment mode.
- Full pipeline: alignment/mapping [Clustal Omega, STAR] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [GSEA]

### The neocortical infrastructure for language involves region-specific patterns of laminar gene expression. (PNAS 2024)

- DOI: 10.1073/pnas.2401687121 | PMCID: PMC11348331 | PMID: 39133845
- Version used: **2.5.1b**
- Evidence: We processed the raw FASTQ files and H&E histology images of sections with Space Ranger software v.1.2.2, using STAR v.2.5.1b ( 77 ) for alignment against the Cell Ranger reference genome refdata-cellranger-GRCh38-3.0.0, available at http://cf.10xgenomics.com/supp/cell-exp/refdata-cellranger-GRCh38-3.0.0.tar.gz .
- Full pipeline: quality control [Bioconductor] -> alignment/mapping [MAGMA, STAR v2.5.1b, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [ImageJ v1.53t, R]

### m&lt;sup&gt;6&lt;/sup&gt;A modification plays an integral role in mRNA stability and translation during pattern-triggered immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2411100121 | PMCID: PMC11331096 | PMID: 39116132
- Evidence: Raw reads were trimmed to remove adaptors and poly(A) sequences by using Trim Galore ( 52 ), and then mapped to the Arabidopsis genome TAIR10 by using the STAR RNA sequencing aligner ( 53 ).
- Full pipeline: read trimming [STAR, Trim Galore] -> alignment/mapping [Bowtie2, STAR, Trim Galore] -> variant calling [Bioconductor] -> normalisation [Bioconductor, DESeq2, HTSeq]

### UPF1 deficiency enhances mitochondrial ROS which promotes an immunosuppressive microenvironment in pancreatic ductal adenocarcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2401996121 | PMCID: PMC11331118 | PMID: 40591563
- Evidence: Briefly, raw reads were fed into “rna-star” module of Seq-N-Slide which employs Trimmomatic for adaptor trimming and low-quality base removal, STAR for alignment to reference genomes (mm10), fastq_screen for contaminant detection, Picard for base distribution and 5′/3′ biases, and featureCounts to generate genes-samples count matrices.
- Full pipeline: read trimming [Picard, STAR, Trimmomatic, featureCounts] -> alignment/mapping [Picard, STAR, Trimmomatic, featureCounts] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2]

### Cone photoreceptor differentiation regulated by thyroid hormone transporter MCT8 in the retinal pigment epithelium. (PNAS 2024)

- DOI: 10.1073/pnas.2402560121 | PMCID: PMC11287251 | PMID: 39018199
- Version used: **2.7.10b**
- Evidence: For each library, ~20 million single-end 50 base reads were collected, then converted using bcl2fastq into fastq files, aligned on GRCm38/mm10 reference genome with STAR (v2.7.10b).
- Full pipeline: alignment/mapping [STAR v2.7.10b, featureCounts] -> quantification [kallisto v0.46.0] -> normalisation [featureCounts] -> stage not stated [ImageJ]

### The DNA damage response of <i>Escherichia coli</i>, revisited: Differential gene expression after replication inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2407832121 | PMCID: PMC11228462 | PMID: 38935560
- Evidence: The input reads averaged 86 to 87 bases with 94 to 95% uniquely mapped to the E. coli MG1655 reference genome (GenBank U00096.3 ) via the STAR RNAseq aligner 2.7.11a ( 85 ).
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, MultiQC] -> alignment/mapping [MultiQC, STAR] -> quantification [edgeR v3.18] -> normalisation [Bioconductor, DESeq2 v1.42.0] -> differential/statistical testing [Bioconductor, DESeq2 v1.42.0] -> stage not stated [R v4.3, ggplot2 v3.5.0]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Evidence: Briefly, reads were mapped with STAR aligner (v2.7.3a) to the mm10/GRCm38 mouse genome using GENCODE annotation version M12.
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### Cancer-stromal cell interactions in breast cancer brain metastases induce glycocalyx-mediated resistance to HER2-targeting therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322688121 | PMCID: PMC11098130 | PMID: 38709925
- Evidence: Fastq files were aligned to the human reference GRCh37/hg19 genome using the STAR RNA-Seq aligner (version STAR_2.5.1b) ( 46 ) followed by transcript assembly using cufflinks v2.2.1 [9] and RseQC v2.6.2 ( 47 ).
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v1.18.1] -> normalisation [edgeR] -> differential/statistical testing [DESeq2 v1.18.1, MACS2 v2.1.1.20160309] -> stage not stated [GSEA, GSVA]

### A time-resolved single-cell roadmap of the logic driving anterior neural crest diversification from neural border to migration stages. (PNAS 2024)

- DOI: 10.1073/pnas.2311685121 | PMCID: PMC11087755 | PMID: 38683994
- Evidence: 10.7, STAR aligner, and DropEst pipeline ( 57 , 58 ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy]

### Decorin suppresses tumor lymphangiogenesis: A mechanism to curtail cancer progression. (PNAS 2024)

- DOI: 10.1073/pnas.2317760121 | PMCID: PMC11067011 | PMID: 38652741
- Evidence: Reads were mapped to the GRCm38 reference genome using STAR aligner v.2.5.2b.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Reads were aligned to the Mus_musculus GRCm38 genome and annotated with Ensembl.GRCm38.gtf by STAR aligner.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### Transcriptional elongation control of hypoxic response. (PNAS 2024)

- DOI: 10.1073/pnas.2321502121 | PMCID: PMC11009653 | PMID: 38564636
- Version used: **2.5.2**
- Evidence: RNA-seq reads were aligned to the GRCh38 genome using STAR v.2.5.2 ( 97 ), and only uniquely mapped reads with a two-mismatch threshold were considered for downstream analysis and quantified to the gene level using HTSeq ( 98 ).
- Full pipeline: quality control [FastQC v0.11.2, Trimmomatic] -> read trimming [Cutadapt v4.1, FastQC v0.11.2, Trimmomatic] -> alignment/mapping [Bowtie2 v2.2.6, HTSeq, STAR v2.5.2] -> quantification [HTSeq, STAR v2.5.2] -> normalisation [DESeq2 v1.32.0] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [deepTools v3.5.1]

### Activation of polyamine catabolism promotes glutamine metabolism and creates a targetable vulnerability in lung cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2319429121 | PMCID: PMC10990097 | PMID: 38513095
- Version used: **2.4.2a**
- Evidence: The RNA-seq reads were mapped to the human genome reference (ENSEMBL genome browser hg38) using STAR version 2.4.2a with default parameters ( 59 ).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.4.2a] -> quantification [RSEM v1.3.3] -> differential/statistical testing [DESeq2, R] -> stage not stated [Metascape]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: Resulting reads were mapped to a reference of the human genome (GRCh38) using STAR ( 46 ), and full read alignments were converted to indexed BAM files with SAMtools ( 47 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### NOVA1 acts as an oncogenic RNA-binding protein to regulate cholesterol homeostasis in human glioblastoma cells. (PNAS 2024)

- DOI: 10.1073/pnas.2314695121 | PMCID: PMC10927500 | PMID: 38416679
- Evidence: Reads were aligned to the hg19 build using STAR ( 42 ) and analyzed by differential analysis of raw sequencing counts using DESeq2 (Bioconductor, https://www.bioconductor.org/packages/release/bioc/html/DESeq2.html ) ( 43 ).
- Full pipeline: alignment/mapping [Bioconductor, DESeq2, STAR] -> differential/statistical testing [Bioconductor, DESeq2, STAR]

### OCA-B/Pou2af1 is sufficient to promote CD4&lt;sup&gt;+&lt;/sup&gt; T cell memory and prospectively identifies memory precursors. (PNAS 2024)

- DOI: 10.1073/pnas.2309153121 | PMCID: PMC10907311 | PMID: 38386711
- Version used: **2.7.3a**
- Evidence: Briefly, Reads were aligned to Mm10 using STAR (v2.7.3a) and checked for quality using multiqc (v1.10).
- Full pipeline: quality control [STAR v2.7.3a] -> alignment/mapping [STAR v2.7.3a] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v4.0.0, UMAP, pheatmap]

### Targeting nuclear receptor corepressors for reversible male contraception. (PNAS 2024)

- DOI: 10.1073/pnas.2320129121 | PMCID: PMC10907271 | PMID: 38377195
- Evidence: Short-read sequences were mapped to the GRCm38 reference sequence using the STAR aligner ( 35 ).
- Full pipeline: alignment/mapping [STAR]

### Coordination of rhythmic RNA synthesis and degradation orchestrates 24- and 12-h RNA expression patterns in mouse fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2314690121 | PMCID: PMC10873638 | PMID: 38315868
- Version used: **2.7.7a**
- Evidence: Reads were mapped with STARv2.7.7a ( 77 ) using options --outFilterScoreMinOverLread 0.3 and --sjdbOverhang 100.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, STAR v2.7.7a] -> quantification [HOMER] -> visualisation [SAMtools v1.11] -> stage not stated [DESeq2 v1.32.0, R]

### Disruption of DNA methylation-mediated cranial neural crest proliferation and differentiation causes orofacial clefts in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2317668121 | PMCID: PMC10801837 | PMID: 38194455
- Version used: **2.7.0**
- Evidence: Trimmed and filtered reads were aligned to the Mus musculus genome (mm10) using RSEM v1.3.1 ( 76 ), which utilized STAR v2.7.0 ( 77 ).
- Full pipeline: quality control [FastQC] -> read trimming [RSEM v1.3.1, STAR v2.7.0] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.0] -> variant calling [ImageJ] -> dimensionality reduction/clustering [R, clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler]

### Sm complex assembly and 5' cap trimethylation promote selective processing of snRNAs by the 3' exonuclease TOE1. (PNAS 2024)

- DOI: 10.1073/pnas.2315259121 | PMCID: PMC10801842 | PMID: 38194449
- Version used: **2.7.8a**
- Evidence: Reads were mapped to the human genome (version hg38) using STAR 2.7.8a ( 65 ).
- Full pipeline: alignment/mapping [BEDTools, SAMtools, STAR v2.7.8a] -> stage not stated [ImageJ]

### Pharmacologic reversion of Merkel cell carcinoma via CBP/p300 inhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2516667122 | PMCID: PMC12772197 | PMID: 41439710
- Version used: **2.7.10b**
- Evidence: Reads from six libraries, representing duplicates for each condition (mock, A-485-treated, dCBP-1-treated), were trimmed by Trimmomatic v.0.38 with default setting for paired-end reads, followed by alignment with STAR v.2.7.10b using human genome reference GRCh38.p14.
- Full pipeline: read trimming [STAR v2.7.10b, Trimmomatic v0.38] -> alignment/mapping [STAR v2.7.10b, Trimmomatic v0.38, featureCounts] -> quantification [R, featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.14.6] -> differential/statistical testing [DESeq2 v1.40.2, R] -> visualisation [clusterProfiler v4.14.6] -> stage not stated [GSEA, GSVA, fgsea v1.26.0]

### Antibiotic-induced microbiota depletion impairs the proregenerative response to a biological scaffold. (PNAS 2025)

- DOI: 10.1073/pnas.2510841122 | PMCID: PMC12772165 | PMID: 41428865
- Version used: **2.7.10a**
- Evidence: Data were aligned using STAR 2.7.10a against GENCODE GRCm39 vM27.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.42.0] -> stage not stated [GSEA, fgsea v1.28.0]

### MBNL loss of function in smooth muscle as a model for myotonic dystrophy associated gastrointestinal dysmotility. (PNAS 2025)

- DOI: 10.1073/pnas.2522788122 | PMCID: PMC12718393 | PMID: 41379996
- Version used: **2.7.10b**
- Evidence: Sequencing results were quality assessed, aligned, normalized, and analyzed using similar methods as previous work ( 124 ) using FastQC version 0.11.9, STAR version 2.7.10b, RSEM algorithm version 1.3.1 ( 125 ), DESeq2 version 1.42.0 for DGE ( 126 ), and rMATS version 4.1.2 for alternative splicing ( 127 ).
- Full pipeline: quality control [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> alignment/mapping [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> variant calling [ImageJ] -> normalisation [DESeq2 v1.42.0, FastQC v0.11.9, RSEM, STAR v2.7.10b] -> stage not stated [Metascape]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Version used: **2.7.11a**
- Evidence: Left reads were aligned to the Arabidopsis reference genome (TAIR10) with STAR (v 2.7.11a) ( 37 ).
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Galectin-9 binding to HLA-DR in dendritic cells controls immune synapse formation and T cell proliferation. (PNAS 2025)

- DOI: 10.1073/pnas.2501381122 | PMCID: PMC12718305 | PMID: 41359845
- Evidence: Reads were aligned to the hg38 human genome using the seq2science pipeline (55) , with STAR used as aligner.
- Full pipeline: alignment/mapping [STAR] -> normalisation [DESeq2, R] -> differential/statistical testing [Fiji, ImageJ] -> stage not stated [GSEA, fgsea]

### Oxidative pentose phosphate pathway is required for T cell activation and antitumor immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2516288122 | PMCID: PMC12704759 | PMID: 41337482
- Evidence: The alignment of reads was done using the STAR aligner with the GRCm39 build of the mouse genome.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Version used: **2.7.11b**
- Evidence: The trimmed reads were aligned to the reference with STAR v2.7.11b ( 53 ), and coverage over the mouse Foxn1 locus was visualized with Gviz v1.46.1 ( 54 ).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### &lt;i&gt;Rroid2&lt;/i&gt; regulates effector-to-memory CD8&lt;sup&gt;+&lt;/sup&gt; T cell differentiation during infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2503450122 | PMCID: PMC12684896 | PMID: 41284876
- Evidence: Reads in fastq format were aligned to the Mus musculus reference genome version GRCm38 with Gencode mV23 annotations ( 60 ) using STAR aligner ( 61 ) version 2.6.1a in 2-pass mode.
- Full pipeline: alignment/mapping [Cufflinks, STAR, TopHat] -> quantification [Cufflinks] -> differential/statistical testing [DESeq2] -> visualisation [ComplexHeatmap, GSEA, ggplot2] -> stage not stated [R]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Version used: **2.7.0f**
- Evidence: The filtered reads were then mapped to the DH Pahang v4 genome with STAR (v2.7.0f) ( 72 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Version used: **2.7.1a**
- Evidence: The processed data were aligned to the hg38 human genome (Ensembl release 99) using STAR (v.2.7.1a).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Genome-wide strand-specific UV mutagenesis in &lt;i&gt;&lt;i&gt;Escherichia coli&lt;/i&gt;&lt;/i&gt; is directed by the Mfd translocase. (PNAS 2025)

- DOI: 10.1073/pnas.2523368122 | PMCID: PMC12646321 | PMID: 41231941
- Version used: **2.7**
- Evidence: Trimmed reads were aligned to the E. coli reference genome (ASM1942v1) using STAR (v2.7) ( 29 ).
- Full pipeline: read trimming [STAR v2.7, Trimmomatic] -> alignment/mapping [SAMtools, STAR v2.7] -> normalisation [deepTools] -> stage not stated [Conda, Snakemake]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Version used: **2.7.10a**
- Evidence: Adapter sequences or poly-A tail from fastq files were trimmed based on fastp, aligned onto genome by STAR (v2.7.10a), and quantified by RSEM (v.1.3.1).
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### A PHF19-YTHDC1 condensate switches EZH2-mediated gene suppression to activation for prostate cancer progression. (PNAS 2025)

- DOI: 10.1073/pnas.2510386122 | PMCID: PMC12582286 | PMID: 41129231
- Version used: **2.7.11b**
- Evidence: Reads were aligned to UCSC hg38 using STAR (v2.7.11b) with spliced alignment parameters, followed by BAM file sorting (sambamba v1.0.1) and indexing (samtools v1.20).
- Full pipeline: quality control [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> read trimming [Bowtie2 v2.5.1, FastQC v0.12.1, MultiQC v1.23, Trimmomatic v0.39, fastp v0.23.4] -> alignment/mapping [Bowtie2 v2.5.1, Picard, SAMtools v1.20, STAR v2.7.11b, Trimmomatic v0.39] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.46.0, R v4.4] -> stage not stated [BEDTools v2.31.0, ImageJ]

### Neuronal plasticity at puberty in mouse hypothalamic &lt;i&gt;Kiss1&lt;/i&gt; neurons that control fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2512855122 | PMCID: PMC12582290 | PMID: 41118223
- Version used: **2.7.9a**
- Evidence: Trimmomatic 0.38 and Cutadapt were used to remove low-quality reads and adapter sequences, respectively, and remaining reads were mapped to the Ensembl mm107 mouse reference genome using STAR (v 2.7.9a).
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Trimmomatic v0.38] -> quantification [featureCounts] -> differential/statistical testing [DESeq2]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: Reads were mapped against the human reference genome (Gencode GRCh38) using STAR aligner (version:2.7.0f_0328) ( 28 ) with default parameters.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Version used: **2.7.11a**
- Evidence: Reads were aligned to the Gencode GRCh38.p13 genome using STAR (v2.7.11a) ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### CRISPR-Cas9 screening reveals microproteins regulating adipocyte proliferation and lipid metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2506534122 | PMCID: PMC12358916 | PMID: 40773238
- Evidence: Briefly, RNA-seq reads were aligned to the mm10 genome using STAR ( 48 ), and transcript models were generated with Stringtie ( 49 ).
- Full pipeline: alignment/mapping [STAR] -> stage not stated [BLAST, RepeatMasker]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Version used: **2.5.3a**
- Evidence: Trimmed reads were aligned to the gene model predictions of the Cassiopea genome version 0.2 ( 52 ), accessed through the Joint Genome Institute genome resource portal ( https://mycocosm.jgi.doe.gov/Casxa1/Casxa1.home.html ) using STAR (version 2.5.3a) with the following settings: --limitOutSJcollapsed 10,00,000 --limitSjdbInsertNsj 10,00,000 --outFilterMultimapNmax 100 --outFilterMismatchNmax 33 ...
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Multiorgan transcriptomics in mice identifies immunoglobulin heavy constant mu (&lt;i&gt;Ighm&lt;/i&gt;) as a tissue-level aging biomarker. (PNAS 2025)

- DOI: 10.1073/pnas.2423142122 | PMCID: PMC12280941 | PMID: 40643973
- Version used: **2.7.11b**
- Evidence: Clean reads were aligned to the GRCm39 mouse genome with Gencode v.M34 annotations using STAR (v2.7.11b) ( 28 ).
- Full pipeline: read trimming [fastp v0.23.1] -> alignment/mapping [STAR v2.7.11b] -> quantification [ImageJ] -> dimensionality reduction/clustering [edgeR v4.2.1] -> visualisation [edgeR v4.2.1] -> stage not stated [DESeq2, R v4.4.1]

### HIF1α mediates circadian regulation of skeletal muscle metabolism and substrate preference in response to time-of-day exercise. (PNAS 2025)

- DOI: 10.1073/pnas.2504080122 | PMCID: PMC12280960 | PMID: 40627397
- Evidence: Reads were aligned to the mouse genome assembly (mm10) using STAR aligner ( 45 ), and transcripts counted using featureCounts ( 46 ).
- Full pipeline: alignment/mapping [STAR, featureCounts] -> quantification [Python] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [emmeans]

### A plant Lysin Motif Receptor-Like Kinase plays an ancestral function in mycorrhiza. (PNAS 2025)

- DOI: 10.1073/pnas.2426063122 | PMCID: PMC12184373 | PMID: 40498450
- Version used: **2.7.10a**
- Evidence: ...2.1 ( 85 ), fq v0.9.1 https://github.com/stjude-rust-labs/fq , gffread v0.12.1 ( 86 ), perl v5.26.2 ( 87 ), python v3.9.5 ( 88 ), rsem v1.3.1 ( 89 ), STAR v2.7.10a ( 90 ), picard v3.0.0 ( 91 ), qualimap v2.3 ( 92 ), rseqc v5.02 ( 93 ), salmon v1.10.1 ( 94 ), summarizedExperiment v1.24.0 ( 95 ), samtools v1.16.1 ( 96 ), stringtie v2.2.1 ( 97 ), tximeta v1.12.0 ( 98 ), UCSC v377, and v445 https://gi...
- Full pipeline: quality control [BEDTools v2.30.0, R v4.0, SAMtools v1.16.1, STAR v2.7.10a] -> alignment/mapping [MUSCLE v3.8, Nextflow v23.10.0, Trim Galore v0.6.7] -> quantification [Nextflow v23.10.0, Trim Galore v0.6.7] -> dimensionality reduction/clustering [clusterProfiler v4.12.3] -> differential/statistical testing [DESeq2 v1.42.1] -> structure determination [IQ-TREE v1.6.12, MUSCLE v3.8] -> stage not stated [ggplot2]

### Light at night negatively affects mood in diurnal primate-like tree shrews via a visual pathway related to the perihabenular nucleus. (PNAS 2025)

- DOI: 10.1073/pnas.2411280122 | PMCID: PMC12167994 | PMID: 40478874
- Evidence: FASTQ sequences were mapped to the tree shrew genome ver 3.0 ( 42 ), which was downloaded from the tree shrew database website ( http://www.treeshrewdb.org/download.html ) and aligned using STAR ( 63 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA]

### Mechanisms of photoreceptor protection upon targeting the &lt;i&gt;Nrl-Nr2e3&lt;/i&gt; pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2500446122 | PMCID: PMC12130857 | PMID: 40397675
- Version used: **2.7.3a**
- Evidence: Paired-end reads were aligned to the mouse genome (GRCm38/mm10) using STAR (v2.7.3a) ( 47 ).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [DESeq2 v1.42.0]

### Macrophages release neuraminidase and cleaved calreticulin for programmed cell removal. (PNAS 2025)

- DOI: 10.1073/pnas.2426644122 | PMCID: PMC12130849 | PMID: 40397678
- Evidence: Sequence data were aligned and normalized using the STAR aligner or DRAGEN RNA pipeline to map reads to the Human Transcriptome Homo Sapiens hg19 (Refseq) and DEseq 2 was used for differential expression analysis.
- Full pipeline: alignment/mapping [STAR] -> normalisation [STAR] -> differential/statistical testing [STAR] -> stage not stated [ImageJ]

### Murine gut microbiota dysbiosis via enteric infection modulates the foreign body response to a distal biomaterial implant. (PNAS 2025)

- DOI: 10.1073/pnas.2422169122 | PMCID: PMC12107164 | PMID: 40354538
- Evidence: FASTQ files were aligned with STAR aligner ( 81 ) to the GENCODE release M27 (GRCm39) mouse genome assembly and annotation.
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, fgsea]

### Quadruple adenine base-edited allogeneic CAR T cells outperform CRISPR/Cas9 nuclease-engineered T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2427216122 | PMCID: PMC12107175 | PMID: 40324075
- Evidence: Sequence reads were trimmed using Trimmomatic v0.36 and aligned to the Homo sapiens GRCh38 reference genome with the STAR aligner v2.5.2b.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, STAR] -> normalisation [limma v3.54.2] -> dimensionality reduction/clustering [clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2, edgeR] -> stage not stated [featureCounts]

### Total whole-arm chromosome losses predict malignancy in human cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505385122 | PMCID: PMC12067283 | PMID: 40314975
- Version used: **2.7.11**
- Evidence: Raw FASTQ files were realigned using STAR (version 2.7.11) to the hg19 reference genome from GENCODE (v19).
- Full pipeline: alignment/mapping [STAR v2.7.11] -> registration [STAR v2.7.11] -> stage not stated [R, survival (R)]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Version used: **2.11a**
- Evidence: Raw reads were filtered using Trimmomatic and aligned to the reference genome using STAR v2.11a, allowing for multimapping reads targeting up to 100 loci ( 79 , 80 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Phospholipid flippase ATP11A brokers uterine epithelial integrity and function. (PNAS 2025)

- DOI: 10.1073/pnas.2420617122 | PMCID: PMC12054786 | PMID: 40261925
- Version used: **2.6.1a**
- Evidence: Read pairs were aligned with STAR (2.6.1a_08-27) to the reference mouse genome (GRCm38/mm10).
- Full pipeline: quality control [R, Seurat v5.1.0] -> alignment/mapping [STAR v2.6.1a] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq, ImageJ v1.53, Metascape]

### PPARα regulates ER-lipid droplet protein Calsyntenin-3β to promote ketogenesis in hepatocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2426338122 | PMCID: PMC12054784 | PMID: 40258152
- Evidence: Trimmed FASTQ files were aligned to GRCm39/mm39 using STAR (-- outFilterMismatchNmax 5 --outFilterMultimapNmax 1).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> stage not stated [HTSeq]

### Perturbing nuclear glycosylation in the mouse preimplantation embryo slows down embryonic development. (PNAS 2025)

- DOI: 10.1073/pnas.2410520122 | PMCID: PMC12012502 | PMID: 40203037
- Version used: **2.7.8a**
- Evidence: For the inspection of reads coverage and the analysis of isoform usage and alternative splicing, fastq files from more runs of the same sample were concatenated before trimming, then mapping was performed using STAR v2.7.8a ( 72 ) in single-sample 2-pass mode for higher accuracy, after genome indexing optimized to read length (--sjdbOverhang set to 100).
- Full pipeline: read trimming [STAR v2.7.8a] -> alignment/mapping [STAR v2.7.8a] -> normalisation [DESeq2, deepTools v3.0.2] -> stage not stated [GSEA, ImageJ, featureCounts]

### Modulation of host gene expression by the zinc finger antiviral protein. (PNAS 2025)

- DOI: 10.1073/pnas.2420819122 | PMCID: PMC12002351 | PMID: 40146858
- Evidence: Raw reads were aligned to the mouse genome ( Mus musculus ensemble 94) using STAR aligner and differentially gene expression analysis was performed using DESeq2 ( 49 ).
- Full pipeline: alignment/mapping [DESeq2, STAR] -> differential/statistical testing [DESeq2, STAR] -> visualisation [ggplot2] -> stage not stated [Cytoscape]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Version used: **2.7.9a**
- Evidence: Reads were mapped to the reference H. schachtii genome ( 31 ) using STAR v2.7.9a ( 78 ) and counted using HTseq v0.13.5.
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Version used: **2.7.0**
- Evidence: Stranded RNA-seq reads were mapped to the D. melanogaster dm6 genome using STAR (v2.7.0) with default parameters.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Version used: **2.7.10b**
- Evidence: Reads were mapped to the Chlamydomonas genome CreinhardtiiCC_4532_707_v6.1 (PhytozomeV13) using STARv.2.7.10b software ( 64 ), with average alignment of 91.65%.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Ancient origin and high diversity of zymocin-like killer toxins in the budding yeast subphylum. (PNAS 2025)

- DOI: 10.1073/pnas.2419860122 | PMCID: PMC11848437 | PMID: 39928860
- Evidence: After preprocessing with Skewer ( 49 ), reads were aligned using STAR ( 61 ) to a subset of the S. cerevisiae genome consisting of a single representative of each tRNA isodecoder, with gaps (N 10 ) between each tRNA gene.
- Full pipeline: read trimming [SPAdes v3.14] -> alignment/mapping [STAR] -> stage not stated [Cytoscape]

### Ethylene-independent modulation of root development by ACC via downregulation of WOX5 and group I CLE peptide expression. (PNAS 2025)

- DOI: 10.1073/pnas.2417735122 | PMCID: PMC11831204 | PMID: 39908106
- Evidence: Initially, raw sequence data FASTA files were uploaded on Partek and then a pipeline was designed to align the raw reads to TAIR 10 genome using STAR aligner ( 58 ) which were then processed to fetch DEGs in ACC-treated samples with respect to Control.
- Full pipeline: alignment/mapping [STAR] -> stage not stated [DESeq2, ImageJ]

### Plastic responses to past environments shape adaptation to novel selection pressures. (PNAS 2025)

- DOI: 10.1073/pnas.2409541122 | PMCID: PMC11804578 | PMID: 39883835
- Version used: **2.7.10a**
- Evidence: We used STAR version 2.7.10a ( 61 ) to map the trimmed reads to the S. uniflora reference genome ( SI Appendix , Methods ).
- Full pipeline: read trimming [STAR v2.7.10a] -> alignment/mapping [STAR v2.7.10a, StringTie v2.2.0] -> stage not stated [R]

### Coding relationship links RNA G-quadruplexes and protein RGG motifs in RNA-binding protein autoregulation. (PNAS 2025)

- DOI: 10.1073/pnas.2413721122 | PMCID: PMC11789052 | PMID: 39847338
- Evidence: Specifically, the sequencing reads were quality- and adapter-trimmed using trim-galore ( 66 ) and aligned to the human reference genome (GRCh38) using STAR aligner ( 67 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [featureCounts, kallisto v0.50.1]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Evidence: The sequences were aligned to the mm10 genome with the STAR aligner, and gene counts were calculated using RSEM.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### ANAC044 orchestrates mitochondrial stress signaling to trigger iron-induced stem cell death in root meristems. (PNAS 2025)

- DOI: 10.1073/pnas.2411579122 | PMCID: PMC11725852 | PMID: 39793035
- Version used: **2.6.1**
- Evidence: RNA-seq read mapping and raw read counting were conducted using STAR (v 2.6.1) and HTSeq (v 0.6.0), respectively; further downstream analysis was all achieved in R (v 4.3.3) as described in SI Appendix , Materials and Methods .
- Full pipeline: alignment/mapping [HTSeq v0.6.0, R v2.6.1, STAR v2.6.1] -> quantification [HTSeq v0.6.0, R v2.6.1, STAR v2.6.1] -> stage not stated [GSEA]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Evidence: Sequencing data were assessed using FastQC (Babraham Bioinformatics, Cambridge, UK) and then mapped to the mouse genome (UCSC mm10) using STAR RNA-seq aligner with the parameter: “—outSAMmapqUNIQUE 60”.
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### A receptor kinase complex refines cambium activity in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2532481123 | PMCID: PMC13321232 | PMID: 42330278
- Evidence: 150 base paired end reads were mapped to the Arabidopsis TAIR10 genome (EnsemblePlants, release 58) sequence with corresponding gtf file to obtain reads per gene using STAR aligner (v 2.7.11a) ( 44 ).
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2 v1.40.2] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [ggplot2 v3.4.4] -> stage not stated [pheatmap v1.0.12]

### Electrical stimulation promotes longevity and regeneration in a colonial chordate. (PNAS 2026)

- DOI: 10.1073/pnas.2610968123 | PMCID: PMC13229227 | PMID: 42190017
- Evidence: Reads were trimmed (trim galore) and aligned to the Botryllus genome ( 14 ) using STAR ( 60 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> stage not stated [ImageJ]

### Ancestral splice variation is a key substrate for rapid diversification in African cichlids. (PNAS 2026)

- DOI: 10.1073/pnas.2516477123 | PMCID: PMC13187723 | PMID: 42118835
- Version used: **2.7.3**
- Evidence: To enable the assembly of novel isoforms we developed a bioinformatics pipeline with the following steps: Reads were assembled using STAR (v2.7.3.a) ( 86 ) in reference guided mode using the Oreochromis niloticus reference genome ( 35 ).
- Full pipeline: quality control [Trimmomatic v0.3.9] -> read trimming [Trimmomatic v0.3.9] -> alignment/mapping [BCFtools, RAxML, SAMtools, STAR v2.7.3, StringTie v2.0.6] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools] -> structure determination [phytools] -> visualisation [R] -> stage not stated [DESeq2]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Version used: **2.7.11b**
- Evidence: These reads were then mapped to the genomic fast of the 102 superscaffolds of our assembly using STAR version 2.7.11b ( 61 ), and with a modified filtered gene set GTF for guidance.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Functional dissection of &lt;i&gt;SPOP&lt;/i&gt; at the amino acid level reveals a comprehensive functional landscape of variants during tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523210123 | PMCID: PMC13167761 | PMID: 42090249
- Evidence: Raw FASTQ files were aligned by STAR aligner in two-pass mode ( 56 ) to the S. cerevisiae reference genome (assembly R64), with WT SPOP appended.
- Full pipeline: read trimming [Cutadapt, minimap2] -> alignment/mapping [STAR, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> visualisation [PyMOL] -> stage not stated [DESeq2, GATK, R]

### Fra-2 controls the response to the KRAS inhibitor MRTX-1133 in pancreatic ductal adenocarcinoma. (PNAS 2026)

- DOI: 10.1073/pnas.2601788123 | PMCID: PMC13142990 | PMID: 42054368
- Version used: **2.7**
- Evidence: Analyses were performed following the procedure described ( 36 ): Reads were aligned to the GRCh38 genome using STAR (v2.7), and the transcripts were quantified with RSEM (v1.3.3).
- Full pipeline: alignment/mapping [RSEM v1.3.3, STAR v2.7] -> quantification [RSEM v1.3.3, STAR v2.7] -> normalisation [DESeq2, GSVA, limma] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, limma] -> stage not stated [GSEA, tidyverse v1.1.4]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Version used: **2.5.2b**
- Evidence: The trimmed reads were then mapped to the danRer11 genome using STAR (v2.5.2b).
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Version used: **2.5.3b**
- Evidence: Raw sequencing data were processed using the Cell Ranger count pipeline (v3.0.0) against the Mus musculus mm10 reference genome using STAR (v2.5.3b) ( 29 ).
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Versatile SMAD2 and SMAD3 epitope-tagged mouse models for genomic profiling of TGFβ signaling: Uncovering GDF9-SMAD2/3 targets. (PNAS 2026)

- DOI: 10.1073/pnas.2600071123 | PMCID: PMC13056123 | PMID: 41911462
- Version used: **2.7.11b**
- Evidence: Alignment and quantification were done using STAR v2.7.11b against mouse genome mm10 ( 92 ).
- Full pipeline: quality control [Bowtie2] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2, STAR v2.7.11b, featureCounts v2.1.1] -> quantification [STAR v2.7.11b] -> stage not stated [DESeq2 v1.48.2, HOMER v4.11, deepTools v2.4.2]

### Synthetic lethality between RB-loss and E2F3 inhibition in small cell cancers targeted by pyrimidine synthesis blockade. (PNAS 2026)

- DOI: 10.1073/pnas.2532814123 | PMCID: PMC13012052 | PMID: 41860961
- Version used: **2.7.10b**
- Evidence: Reads were aligned to the GRCh38 human genome using STAR (v2.7.10b) with the parameter “--twopassMode Basic.” Transcripts were quantified with Kallisto (v0.50.1) with default parameters, and splicing events were quantified with rMATS-turbo (v4.2.0) with default parameters ( 66 ).
- Full pipeline: alignment/mapping [STAR v2.7.10b, kallisto v0.50.1] -> quantification [STAR v2.7.10b, kallisto v0.50.1]

### Coexpression among eastern oyster host and microbiome genes suggests coordinated regulation of calcifying fluid chemistry. (PNAS 2026)

- DOI: 10.1073/pnas.2521539123 | PMCID: PMC12994172 | PMID: 41805583
- Version used: **2.7.11b**
- Evidence: We used splice-aware mapper STAR v.2.7.11b ( 63 ) to map the quality filtered, nonribosomal reads against the C. virginica transcriptome, downloaded from NCBI, to separate oyster from nonoyster reads.
- Full pipeline: quality control [FastQC v0.12.1] -> read trimming [FastQC v0.12.1, Trim Galore v0.6.10] -> alignment/mapping [Bowtie2 v2.3.2, Python, Salmon v1.10.3] -> quantification [Bowtie2 v2.3.2, Salmon v1.10.3] -> normalisation [Salmon v1.10.3] -> differential/statistical testing [DESeq2 v1.40.2] -> visualisation [pheatmap] -> stage not stated [R, STAR v2.7.11b, WGCNA v1.73, eggNOG]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Raw counts for samples were obtained by aligning sequencing reads to the mm10_assembly reference genome using the STAR aligner (v2.7.7a) ( 41 ).
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Germline fate determination by a single ARGONAUTE protein in &lt;i&gt;Ectocarpus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518712123 | PMCID: PMC12867755 | PMID: 41604268
- Evidence: High-quality reads from each library were subsequently mapped to the Ectocarpus Ec32 transcriptome reference ( 82 ) using the STAR aligner ( 91 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT, STAR, featureCounts] -> quantification [DESeq2, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Lack of synergy between AR-targeted therapies and PARP inhibitors in homologous recombination-proficient prostate cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2515790122 | PMCID: PMC12867744 | PMID: 41591905
- Evidence: The VIPER pipeline ( 50 ) was used for STAR alignment to the hg19 genome ( 51 ), read count normalization using Cufflinks ( 52 ) quality control with RSeQC ( 53 ), and differential expression analysis using DESeq2 ( 54 ).
- Full pipeline: quality control [Cufflinks, DESeq2, STAR] -> alignment/mapping [Cufflinks, DESeq2, STAR] -> quantification [CellProfiler, Cufflinks, DESeq2, STAR] -> normalisation [Cufflinks, DESeq2, STAR] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [Cufflinks, DESeq2, STAR]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Evidence: Binned reads were aligned to respective reference genomes and counted using STAR (v.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: Reads were then mapped to a concatenated human (GRCh38, ENSEMBL Release 104) and SARS-CoV-2 ( NC_045512.2 ) genome using STAR with end-to-end alignment mode.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Cortical wiring by synapse type-specific control of local protein synthesis. (Science 2022)

- DOI: 10.1126/science.abm7466 | PMCID: PMC7618116 | PMID: 36423280
- Version used: **2.4.0**
- Evidence: Using STAR v2.4.0 ( 71 ) on the mm10 Mouse genome assembly with an average of 79.8±3.4% of uniquely mapped reads.
- Full pipeline: quality control [FastQC, Picard, SAMtools] -> alignment/mapping [STAR v2.4.0] -> quantification [R v3.2] -> normalisation [R v3.2] -> differential/statistical testing [DESeq2, R v3.2] -> stage not stated [ImageJ]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Version used: **2.7.0e**
- Evidence: We aligned the reads to the human reference genome (NCBI GRCh38) using STAR v2.7.0e ( 47 ).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Conserved γδ T cell selection by BTNL proteins limits progression of human inflammatory bowel disease. (Science 2023)

- DOI: 10.1126/science.adh0301 | PMCID: PMC7615126 | PMID: 37708268
- Version used: **2.5.2a**
- Evidence: Single-end reads were aligned to human genome GRCh38 from Ensembl using STAR (v2.5.2a).
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [STAR v2.5.2a] -> quantification [RSEM v1.3.0] -> differential/statistical testing [DESeq2] -> stage not stated [Bowtie2 v2.2.5, GSEA, Picard]

### Base editing rescue of spinal muscular atrophy in cells and in mice. (Science 2023)

- DOI: 10.1126/science.adg6518 | PMCID: PMC10270003 | PMID: 36996170
- Version used: **2.7.10a**
- Evidence: Trimmed reads were aligned to the GENCODE mouse reference genome M31 (GRCm39) using STAR (v2.7.10a), quantified using kallisto( 127 ), and refined to canonical coding sequences using CCDS release 21( 128 ).
- Full pipeline: read trimming [STAR v2.7.10a, Trim Galore v0.6.7, kallisto] -> alignment/mapping [STAR v2.7.10a, kallisto] -> quantification [STAR v2.7.10a, kallisto] -> structure determination [STAR v2.7.10a, kallisto]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: The sequencing reads of each FASTQ file were then aligned with the GENCODE human reference genome GRCh37.p13 with STAR aligner v2.6 and the alignment quality of each BAM file was evaluated with RSeQC.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Creation of de novo cryptic splicing for ALS and FTD precision medicine. (Science 2024)

- DOI: 10.1126/science.adk2539 | PMCID: PMC7616720 | PMID: 39361759
- Version used: **2.7.0f**
- Evidence: Quantification of cryptic AARS1 expression in published RNA-sequencing Publicly available cell line data were aligned using the pipeline described in ( 7 ) - briefly, samples were aligned to the GRCh38 genome build using STAR (v2.7.0f) ( 32 ) with gene models from GENCODE v31 ( 33 ).
- Full pipeline: alignment/mapping [STAR v2.7.0f, minimap2 v2.1] -> quantification [ImageJ, STAR v2.7.0f] -> stage not stated [BEDTools, CellProfiler, R, Snakemake v5.5.4]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Evidence: RNA-seq analysis RNA sequencing (RNA-seq) raw reads were quality-checked with FastQC (v0.11.7) ( 110 ) and aligned onto the human genome (hg38 assembly) using STAR RNA-Seq aligner (v2.7.10b) ( 121 ), with the following options:–outSJfilterReads Unique –outFilterMultimapNmax 1 –outFilter IntronMotifs RemoveNoncanonical –outSAM-strandField intronMotif.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Version used: **2.7.1a**
- Evidence: Raw sequencing reads were aligned to the mouse genome (mm39) using STAR 2.7.1a and quantified using featureCounts 1.6.2 ( 111 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Version used: **2.6.0a**
- Evidence: Sequence data were trimmed to remove adaptors and sequences with a quality score below 30 using Trim Galore (version 0.50, Babraham Bioinformatics) and then aligned to the mouse genome (GRCm38) using STAR (version 2.6.0a), and differential expression was calculated using DESeq2 (version 1.18.1) ( 77 ).
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Identification of antigen-presenting cell-T cell interactions driving immune responses to food. (Science 2025)

- DOI: 10.1126/science.ado5088 | PMCID: PMC12017586 | PMID: 39700315
- Evidence: Fastq sequence files from smartseq2 generated from libraries were aligned to the mouse genome (mm39) associated with the mouse transcriptome annotations (v. gencode M29) using STAR (v.
- Full pipeline: alignment/mapping [RSEM v1.3.1, STAR] -> stage not stated [DESeq2, MACS2, R, Seurat v4.1.2]

### Microglia Rank signaling regulates GnRH neuronal function and the hypothalamic-pituitary-gonadal axis. (Science 2026)

- DOI: 10.1126/science.aeb6999 | PMCID: PMC7619046 | PMID: 41818388
- Version used: **2.7.1**
- Evidence: ...://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ); reads were aligned to the mouse reference genome (GRC39m from GENCODE ( 99 )) with STARsolo (STAR v2.7.1) ( 100 ); Seurat v3.2.3 ( 101 ) software was used to check the quality of sequenced cells, and perform data normalization, dimensionality reduction and clustering.
- Full pipeline: quality control [FastQC, STAR v2.7.1] -> alignment/mapping [FastQC, GATK, STAR v2.7.1] -> normalisation [FastQC, STAR v2.7.1] -> dimensionality reduction/clustering [FastQC, ImageJ, STAR v2.7.1, UMAP] -> stage not stated [GSEA, Seurat]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Version used: **2.7.1a**
- Evidence: Processed reads were then aligned to the African turquoise killifish reference genome [Nfu_20140520, GCF_001465895.1 ( 39 )] and the gene read count and UMI count matrices were created using STAR (version 2.7.1a) with parameters adjusted according to recommendations for the BRB-seq platform with the Mercurius Protocol (Alithea Genomics) including: – soloCBwhitelist : text file with list of barcode...
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Version used: **2.7.1a**
- Evidence: Paired end RNA-seq reads were aligned to the reference genome (GRCh38) using STAR (2.7.1a).
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Version used: **2.5.3a**
- Evidence: Reads were aligned against the mouse reference genome GRCm38 (mm10), with gene annotations from Ensembl release 102, using STAR 2.5.3a ( 125 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### Blocking RAN translation without altering repeat RNAs rescues &lt;i&gt;C9ORF72&lt;/i&gt;-related ALS and FTD phenotypes. (Science 2026)

- DOI: 10.1126/science.adv2600 | PMCID: PMC13107528 | PMID: 41643021
- Version used: **2.7.9a**
- Evidence: The fastq sequencing files were used to align with human reference genome (hg38) using STAR (version 2.7.9a) ( 108 ).
- Full pipeline: alignment/mapping [STAR v2.7.9a] -> quantification [CellProfiler, Fiji, ImageJ] -> differential/statistical testing [DESeq2, R v4.2.1]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Version used: **2.7.9**
- Evidence: Bulk RNA-sequencing libraries were demultiplexed using bcl2fastq (v2.20) and aligned to the respective genome assemblies (calJac4 for marmoset, Mmul_8.0/rheMac8 for macaque and panPan1 for bonobo) using STAR (v.2.7.9.a) ( 73 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

