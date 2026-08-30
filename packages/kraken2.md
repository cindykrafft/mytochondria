# Kraken2

- **Category:** microbiome
- **Papers in survey:** 31
- **Journals:** Nature (15), PNAS (13), Cell (3)
- **Years:** 2021 (4), 2022 (3), 2023 (6), 2024 (6), 2025 (9), 2026 (3)
- **Versions named:** 2.1.1 (3), 2.0.8 (2), 2.1.3 (2), 2.1.2 (2)
- **Pipeline stages it appears in:** alignment/mapping (6), quality control (3), quantification (2), read trimming (2), visualisation (1)

## Papers

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Evidence: To identify co-detected microbial taxa present in the cell-associated or ambient RNA of nasopharyngeal swabs, we used the Kraken2 software implemented using the Broad Institute viral-ngs pipelines on Terra ( https://github.com/broadinstitute/viral-pipelines/tree/master ) ( Wood et al., 2019 ).
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Evidence: .../eggnog-mapper Prokka v1.5-135 Seemann, 2014 https://github.com/tseemann/prokka BWA-MEM v0.7.16a-r1181 Li and Durbin, 2009 https://github.com/lh3/bwa Kraken2 Wood et al., 2019 https://github.com/DerrickWood/kraken2 MAFFT v7.453 Katoh et al., 2002 https://mafft.cbrc.jp/alignment/software/ Easyfig v2.2.5 Sullivan et al., 2011 https://mjsull.github.io/Easyfig/files.html Other ICEberg 2.0 Bi et al., 2...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Version used: **2.1.2**
- Evidence: ...f viruses in the Rhinolophus ferrumequinum transcriptome was explored by analysing the RNA-seq and Iso-seq data based on a metagenomic approach using Kraken2 v2.1.2 112 First, the adaptors in the RNA-seq data were removed with Trimgalore v0.6.7 114 and all replicates for corresponding datasets were joined in one file.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Version used: **2.0.8**
- Evidence: Classification of the fused reads against a custom nucleotide database was performed using Kraken 2 (v.2.0.8-beta) 74 using a threshold of 0.15.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: Marine eukaryotic metagenome We sought to identify marine eukaryotes by first taxonomically labelling all quality-controlled reads as Eukaryota, Archaea, Bacteria or Virus using Kraken 2 76 with the parameters ‘--confidence 0.5 --minimum-hit-groups 3’ combined with an extra filtering step that only kept those reads with root-to-leaf score >0.25.
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### Synergy and oxygen adaptation for development of next-generation probiotics. (Nature 2023)

- DOI: 10.1038/s41586-023-06378-w | PMCID: PMC10412450 | PMID: 37532933
- Evidence: For genome capture, high-quality microbial reads were mapped using Kraken 2 (ref.
- Full pipeline: alignment/mapping [Kraken2] -> quantification [Bracken] -> differential/statistical testing [R, vegan] -> stage not stated [Bowtie2 v2.3.5.1, Prokka v1.14.5, SPAdes v3.13.0]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Evidence: 54 ) (v2.12.0), annotated with RepeatMasker (v4.1.2-p1) and Kraken2 (ref.
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: The passed reads were also classified using Kraken2 (ref.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **2.1.1**
- Evidence: The assembled contigs were taxonomically classified using Kraken2 v2.1.1 (ref.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Evidence: All isolates were confirmed to be E. faecium with the Kraken2 database (v.2.1.2) 33 .
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Evidence: Pathogen screening Shotgun data were used for an initial screening of the 99 candidate samples, with Kraken2 software 82 , and 41 samples that had more than 7 hits to T. pallidum were selected for target enrichment.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Host genetic regulation of human gut microbial structural variation. (Nature 2024)

- DOI: 10.1038/s41586-023-06893-w | PMCID: PMC10808065 | PMID: 38172637
- Version used: **2.1.2**
- Evidence: Taxonomic abundance We estimated the relative abundance of gut microbial species from the cleaned metagenomic reads using Kraken2 (v.2.1.2) 59 in conjunction with Bracken (v.2.6.2) 60 based on the same reference genomes included in the database of SGV-Finder, and MetaPhlAn 3 (ref.
- Full pipeline: quality control [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> read trimming [Bowtie2 v2.3.4.3, Trimmomatic v0.39] -> alignment/mapping [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> variant calling [PLINK] -> quantification [Bracken v2.6.2, Kraken2 v2.1.2, MetaPhlAn] -> dimensionality reduction/clustering [RAxML] -> stage not stated [GCTA, R v4.1.0, ape (R) v5.6, vegan v2.6]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: We complemented these MAG assignments using Kraken2 46 (v.2.0.8) and Bracken 47 (v.2.5) and a Kraken2-compatible version of the GTDB reference.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Non-antibiotics disrupt colonization resistance against enteropathogens. (Nature 2025)

- DOI: 10.1038/s41586-025-09217-2 | PMCID: PMC12350171 | PMID: 40670795
- Version used: **2.1.3**
- Evidence: Then, clean reads were taxonomically classified using Kraken2 (v.2.1.3) 73 and Bracken (v.2.9) 74 against a GTDB-formatted database based on the Unified Human Gut Genome catalogue 75 (available at http://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/human-gut/v2.0.2/ ).
- Full pipeline: quality control [QuPath v0.5.1] -> read trimming [fastp v0.23.4] -> alignment/mapping [ape (R) v5.8] -> normalisation [QuPath v0.5.1] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [DESeq2 v1.44.0, clusterProfiler v4.12.6, lme4 v1.1] -> structure determination [ape (R) v5.8] -> visualisation [ggplot2 v3.5.1] -> stage not stated [Bracken v2.9, DADA2 v1.21.0, Kraken2 v2.1.3, R, emmeans v1.10.6, vegan v2.6]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Version used: **2.1.3**
- Evidence: Quantification of species abundances based on metagenome sequencing data Taxonomic profiling using metagenome sequencing data was performed through read-level taxonomic assignment with Kraken2 (v.2.1.3) 69 , followed by estimation of relative abundances using Bracken (v.2.9) 70 .
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Version used: **2.1.1**
- Evidence: The percentage of human DNA per sample was estimated using Kraken2 v.2.1.1 (ref.
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### Evolution of pandemic cholera at its global source. (Nature 2026)

- DOI: 10.1038/s41586-026-10340-x | PMCID: PMC13171446 | PMID: 41922762
- Version used: **2.0.8**
- Evidence: Kraken2 v.2.0.8 was used to screen for ICP1 using a database containing only RefSeq viruses.
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.8] -> read trimming [fastp v0.23.4] -> alignment/mapping [Prokka v1.14.5] -> visualisation [R] -> stage not stated [IQ-TREE v1.6.12, Kraken2 v2.0.8, SPAdes v4.1.0, TreeTime v0.7.4, phytools v2.4]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Evidence: Taxonomic assignment of the decontaminated and quality-controlled reads was performed using Kraken 2 (ref.
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: We used Kraken2 and a custom database updated to November 2020 of bacterial, viral, archaeal, and organelle genomes from the NCBI Reference Sequence (RefSeq) database ( https://www.ncbi.nlm.nih.gov/refseq/ ) for taxonomic classification of merged deduplicated reads, as previously described ( 6 ).
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Taxonomic classification of DNA sequences beyond sequence similarity using deep neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2122636119 | PMCID: PMC9436379 | PMID: 36018838
- Evidence: BERTax is compared against the state-of-the-art database taxonomic classification approaches Kraken2 ( 15 ), sourmash ( 16 ), MMseqs2 ( 14 ), and minimap2 ( 17 ).
- Full pipeline: stage not stated [Kraken2, NumPy v1.19.2, Python v3.7, SciPy v1.6.1, minimap2]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: Finally, Kraken 2 ( 65 ) was used to filter out contigs mapping the human genome (default settings, with “confidence” set at 0.05 as recommended by the authors).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Sex-linked gene traffic underlies the acquisition of sexually dimorphic UV color vision in <i>Heliconius</i> butterflies. (PNAS 2023)

- DOI: 10.1073/pnas.2301411120 | PMCID: PMC10438391 | PMID: 37552755
- Evidence: To decontaminate the microbial sequences from the polished contigs, taxonomic groups were assigned to each contig using Kraken2 ( 54 ).
- Full pipeline: quality control [Bowtie2 v2.2.7, Kraken2] -> alignment/mapping [BEDTools, Bowtie2 v2.2.7, MUSCLE] -> differential/statistical testing [R] -> stage not stated [Canu v1.6, Pilon, StringTie]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Evidence: Trimmed, paired reads for each sample were then decontaminated with Kraken 2 ( 74 ) using the full Kraken 2 standard database from 17/05/2021 (archived at https://benlangmead.github.io/aws-indexes/k2 ).
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### Aerosolization of viable <i>Mycobacterium tuberculosis</i> bacilli by tuberculosis clinic attendees independent of sputum-Xpert Ultra status. (PNAS 2024)

- DOI: 10.1073/pnas.2314813121 | PMCID: PMC10962937 | PMID: 38470917
- Evidence: Kraken2 ( 23 ) was implemented directly on Fastq files on the Sciensano Galaxy instance ( 66 ) with standard parameters against the full Kraken database.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard v2.9.1, SAMtools v1.5] -> differential/statistical testing [R] -> structure determination [Picard v2.9.1, SAMtools v1.5] -> stage not stated [Kraken2]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Evidence: Metagenomic classification of unaligned reads was performed using Kraken2 with the default database and parameters.
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Version used: **2.1.1**
- Evidence: Compositional profiling was performed by Kraken2 (version 2.1.1) 4) with the Genome Taxonomy Database (GTDB) 5).
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Structural basis of the catalytic and allosteric mechanism of bacterial acetyltransferase PatZ. (PNAS 2025)

- DOI: 10.1073/pnas.2419096122 | PMCID: PMC12184503 | PMID: 40498448
- Evidence: The resulting alignments were converted into the Kraken2 sample report format and visualized as Sankey diagrams with Pavian ( 77 ) (version 1.0).
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, Kraken2] -> structure determination [ChimeraX, PHENIX] -> visualisation [Kraken2] -> stage not stated [AlphaFold]

### RNA sequencing analysis of viromes of &lt;i&gt;Aedes albopictus&lt;/i&gt; and &lt;i&gt;Aedes vexans&lt;/i&gt; collected from NEON sites. (PNAS 2025)

- DOI: 10.1073/pnas.2403591122 | PMCID: PMC12107137 | PMID: 40354533
- Evidence: Briefly, the profiling process was initiated by surveying the potential presence of bacterial and archaeal species for each raw metagenomic sample read using Kraken2 ( 33 ) and a prebuilt core gene database ( 34 ) containing k-mers (k = 35) of reference genomes obtained from the EzBioCloud database ( 35 ).
- Full pipeline: read trimming [BWA, fastp v0.21.1] -> alignment/mapping [BLAST, BWA, Kraken2, SAMtools] -> stage not stated [Bowtie2, R]

### Exposure and health risks of livestock air resistomes. (PNAS 2025)

- DOI: 10.1073/pnas.2403866122 | PMCID: PMC12067279 | PMID: 40294268
- Evidence: Microbial composition in metagenomic data was analyzed using Kraken2 ( 46 ) with standard plus database and re-estimated with Bracken ( 47 ).
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [Bracken, Kraken2, QIIME 2 v2020.11]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Evidence: Unmatched fragments were identified and classified by Kraken2 using the LCA strategy.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Evidence: A custom-built Kraken 2 ( 49 ) database including the species listed in Dataset S1 was used for initial identification of species present in the sample.
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

