# BLAST

- **Category:** phylogenetics
- **Papers in survey:** 325
- **Journals:** PNAS (219), Nature (80), Cell (20), Science (6)
- **Years:** 2021 (33), 2022 (55), 2023 (47), 2024 (78), 2025 (79), 2026 (33)
- **Versions named:** 2.13.0 (6), 2.12.0 (5), 2.7.1 (4), 2.6.0 (4), 2.9.0 (3), 2.11.0 (3), 2.0.9 (3), 2.14.0 (2), 2.13 (2), 2.5.0 (2)
- **Pipeline stages it appears in:** alignment/mapping (69), dimensionality reduction/clustering (16), read trimming (6), structure determination (4), variant calling (3), differential/statistical testing (3), quantification (2), visualisation (1), machine learning (1)

## Papers

### Deciphering osteoarthritis genetics across 826,690 individuals from 9 populations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.038 | PMCID: PMC8459317 | PMID: 34450027
- Evidence: Proteins closely related to targets of approved drugs were identified through a BLAST search (blastp) of Ensembl peptide sequences against the set of approved drug efficacy targets identified from ChEMBL ( Gaulton et al., 2017 ) previously.
- Full pipeline: quality control [IMPUTE2, R] -> variant calling [IMPUTE2] -> quantification [limma] -> normalisation [DESeq2 v1.20] -> differential/statistical testing [DESeq2 v1.20, R, limma] -> stage not stated [BLAST, FUMA, GCTA, GEMMA, LDSC, PLINK v1.9]

### Genome-wide gene expression tuning reveals diverse vulnerabilities of M. tuberculosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.033 | PMCID: PMC8382161 | PMID: 34297925
- Evidence: ...enBank: NC_010397.1 : M. abscessus; GenBank: NC_022040.1 : C. glutamicum ; GenBank: NC_000964.3 : B. subtilis ; and GenBank: NC_000913.3 : E. coli ). blastp was run such that it filtered results to those that had e-values < 0.0001 and so that it reported protein similarity (ppos).
- Full pipeline: alignment/mapping [Python v2.7.18, SciPy v1.2.2] -> stage not stated [BLAST, Stan v2.19.3, statsmodels v0.10.1]

### Identification of novel bat coronaviruses sheds light on the evolutionary origins of SARS-CoV-2 and related viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.008 | PMCID: PMC8188299 | PMID: 34147139
- Evidence: The contigs from MEGAHIT were searched by BLASTn based on the NCBI nt database.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.450] -> stage not stated [BLAST, Bowtie2 v2.4.1, PyMOL v2.4.0a, RAxML, SAMtools v1.10]

### A global metagenomic map of urban microbiomes and antimicrobial resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.002 | PMCID: PMC8238498 | PMID: 34043940
- Evidence: .../github.com/mikkelschubert/adapterremoval Bowtie2 v2.3.0 Langmead and Salzberg, 2013 https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.0/ BLASTn Altschul et al., 1990 https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ KrakenUniq v0.3.2 Breitwieser et al., 2018 https://github.com/fbreitwieser/krakenuniq MASH v2.1.1 Ondov et al., 2016 https://github.com/marbl/Mash HUMAnN2 Fran...
- Full pipeline: read trimming [BLAST, Bowtie2 v2.3.0] -> dimensionality reduction/clustering [R, UMAP] -> structure determination [R] -> visualisation [UMAP] -> stage not stated [Jupyter, SciPy]

### Transmission, infectivity, and neutralization of a spike L452R SARS-CoV-2 variant. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.025 | PMCID: PMC8057738 | PMID: 33991487
- Evidence: In short, Illumina raw paired-end reads were first screened for SARS-CoV-2 sequences using BLASTn (BLAST+ package 2.9.0) alignment against viral reference genome NC_045512 , and then processed using the BBTools suite, v38.87 ( Bushnell, 2021 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT, Nextstrain] -> stage not stated [IQ-TREE v1.6, Python v3.7.9, R v4.0, SciPy]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **2.6.0**
- Evidence: Briefly, we first used the ‘blastn’ function of BLAST v2.6.0 ( Altschul et al., 1990 ) to query each contig against the human genome GRCh38 using the following parameters: ‘-word_size 28 -best_hit_overhang 0.1 -best_hit_score_edge 0.1 -dust yes -evalue 0.0001 -min_raw_gapped_score 100 -penalty −5 -perc_identity 90 -soft_masking true’.
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: ... Q92574 ), TSC2 (UniProt: P49815 ), TBC1D7 (UniProt: Q9P0N9 ), RHEB (UniProt: Q15382 ), and MTOR (UniProt: P42345 ) were used as query proteins for a blastp+ search ( Camacho et al., 2009 ) against the NCBI non-redundant protein sequence database (nr; version 2017-11).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Version used: **2.12.0**
- Evidence: For BCR contigs, heavy chain constant region calls were re-annotated using blastn (v2.12.0+) against curated sequences of CH1 regions corresponding to respective isotype classes from IMGT.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: Any ASVs that were classified by ITSx as non-fungal, were included in the downstream analysis only if their classification as fungi reached a class or lower phylogenetic level by UNITE and were validated by NCBI BLAST to be fungal.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: Bioinformatics analyses To identify OspC homologs in other bacterial species, the Shigella flexneri OspC3 amino acid sequence was subject to BLASTp ( Altschul et al., 1990 ) analysis against the entire NCBI database excluding the Shigella taxid using default parameters.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ... IQtree ( Minh et al., 2020 ) v2.0.4 ModelFinder ( Kalyaanamoorthy et al., 2017 ) N/A iTOL https://itol.embl.de ( Letunic and Bork, 2021 ) v6 Diamond blastp ( Buchfink et al., 2021 ) v2.0.7.145 Cytoscape ( Shannon et al., 2003 ) v3.7.1 R (phylogeny) https://www.r-project.org/ v4.0.3 Phylogram ( Wilkinson and Davy, 2018 ) v2.1.0 Dendextend ( Galili, 2015 ) v1.15.1 R (statistics) https://www.r-proje...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### Neutralizing immunity in vaccine breakthrough infections from the SARS-CoV-2 Omicron and Delta variants. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.019 | PMCID: PMC8930394 | PMID: 35429436
- Evidence: Genome assembly and variant identification Raw sequencing data were simultaneously demultiplexed and converted to FASTQ files and screened for SARS-CoV-2 sequences using BLASTn (BLAST+ package 2.9.0).
- Full pipeline: read trimming [BLAST] -> quantification [Python v3.7.10] -> differential/statistical testing [Python v3.7.10] -> visualisation [Python v3.7.10] -> stage not stated [Pangolin, R v4.0, ggplot2, seaborn]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Version used: **2.12.0**
- Evidence: ...n package) Polański et al., 2020 https://github.com/Teichlab/bbknn Scirpy v0.3 (Python package) Sturm et al., 2020 https://github.com/icbi-lab/scirpy BLASTp v2.12.0+ Altschul et al., 1997 https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins Lifelines v0.26.0 (Python package) Davidson-Pilon, 2021 https://github.com/CamDavidsonPilon/lifelines scikit-learn v0.24.2 (Python package) Pedregosa et al.,...
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Evidence: 86 For each gene family, the collection of homologous proteins was aligned in an all-to-all fashion using diamond v0.9.36 100 (using the high sensitivity mode in blastp and up to 100 alignments per query) and divided into one or more low-granularity homology groups using the Markov Cluster Algorithm MCL v14.137 96 (ABC mode using alignment bit-scores as weights, and a gene family-specific inflatio...
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: Short protein-optimized BLAST (blastp-short) was subsequently used to query for significant alignments (E-value ≤ 1e-4) between our 323 predicted antimicrobial SEPs and all hCom2 ORFs.
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Evidence: These neighbouring genes were annotated against CDD v3.19 147 using rpsblast (-evalue 0.01 -max_hsps 1 -max_target_seqs 5) in BLAST+ v2.9.0, 104 the Pfam protein family database v34.0 148 using PfamScan v1.6 (default setting), 121 and the NCBI RefSeq protein database release 202 149 using DIAMOND v0.9.31 blastp algorithm (--max-hsps 1 --max-target-seqs 1).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **2.7.1**
- Evidence: 27 http://homer.ucsd.edu/homer/ OrthoFinder v2.5.4 Emms and Kelly 100 https://github.com/davidemms/OrthoFinder BLASTp v2.7.1+ Altschul et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Macromolecular condensation organizes nucleolar sub-phases to set up a pH gradient. (Cell 2024)

- DOI: 10.1016/j.cell.2024.02.029 | PMCID: PMC11938373 | PMID: 38503281
- Evidence: BLASTp was then used to keep only the most similar ortholog for each species per nucleolar protein.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [BLAST, ImageJ, Python]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Version used: **2.9.0**
- Evidence: All versus all NCBI BLAST (v2.9.0 57 ) was run using the SAMap script map_genes.sh on the annotated proteins from the VectorBase-58 version of LVP_AGWG genome and the “all translation” file from the FB2023_02 version of the FlyBase genome.
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: Promiscuity to the remainder of the genome was checked by local blastn .
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Universal nomenclature for oxytocin-vasotocin ligand and receptor families. (Nature 2021)

- DOI: 10.1038/s41586-020-03040-7 | PMCID: PMC8081664 | PMID: 33911268
- Evidence: Overall synteny and BLASTn analyses To define orthology in the OT , VT and OTR-VTRs in all vertebrates, we used interspecies synteny analyses at three scales: a manual 10-gene window microsyteny analyses using BLAT and BLAST 38 , 39 searches and cross-species genome alignments; a more automated 100-gene macrosynteny window using SynFind and GeVo 22 ; and automated chromosomal-scale alignments with...
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> stage not stated [RepeatMasker]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: A. ciliaticola’ genome from the metagenome samples from 2016 (further details are provided in Supplementary Methods ) were identified by blastn (identity >95%) and metagenomic reads were mapped back to the contigs using BBmap 60 v.35.43 (minid = 0.98).
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### Direct activation of a bacterial innate immune system by a viral capsid protein. (Nature 2022)

- DOI: 10.1038/s41586-022-05444-z | PMCID: PMC9712102 | PMID: 36385533
- Evidence: Homologues of the major capsid proteins in BASEL phages were identified by BLASTp 55 searches against each phage genome.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> stage not stated [AlphaFold, BLAST, CCP4, PHENIX]

### Borgs are giant genetic elements with potential to expand metabolic capacity. (Nature 2022)

- DOI: 10.1038/s41586-022-05256-1 | PMCID: PMC9605863 | PMID: 36261517
- Evidence: Proteins were compared using blastp and aligned using MAFFT 47 v.7.407 to visualize homologous regions and check conserved amino acid residues that constitute the active site or are required for cofactor and ligand binding.
- Full pipeline: alignment/mapping [BLAST, IQ-TREE v1.6.6, MAFFT, SciPy] -> quantification [SciPy] -> visualisation [BLAST, IQ-TREE v1.6.6, MAFFT] -> stage not stated [HMMER]

### A microbial supply chain for production of the anti-cancer drug vinblastine. (Nature 2022)

- DOI: 10.1038/s41586-022-05157-3 | PMCID: PMC9452304 | PMID: 36045295
- Evidence: Gene discovery Sequence for Vmi 8HGO-A was obtained from V. minor transcriptome data 41 using BLASTn 42 and the C. roseus 8HGO-A sequence (GenBank accession no.
- Full pipeline: stage not stated [BLAST]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: Protein sequences were aligned all-against-all using BLASTp 36 v2.5 [-seg yes, -soft_masking true, -evalue 1e-3].
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Evidence: ... pathway to the previously reported BCFA biosynthetic pathway and de novo biosynthetic pathway of leucine, isoleucine and valine were performed using blastp (NCBI RefSeq database, updated 8 September 2015), Kyoto Encyclopaedia of Genes and Genomes and Geneious v.11.1.4 for pairwise sequence alignments that were previously reported.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Evidence: 64 )); (3) no gaps in genomic coverage were identified in the evaluated window; (4) reads overlapping the SNP sites showed specificity to the Y. pseudotuberculosis complex when screened with BLASTn ( https://blast.ncbi.nlm.nih.gov/Blast.cgi ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Evidence: Local alignment identity of the detected ASVs with the OTU476 and OTU327 from the pig microbiome were measured using blastn 107 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Phage anti-CBASS and anti-Pycsar nucleases subvert bacterial immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-04716-y | PMCID: PMC9117128 | PMID: 35395152
- Evidence: Identification of Acb1 and Apyc1 homologues and generation of phylogenetic trees Homologues of Acb1 and Apyc1 were identified using NCBI BLASTp with default parameters.
- Full pipeline: read trimming [Cutadapt v2.8, SPAdes] -> visualisation [PyMOL v2.3.0] -> stage not stated [BLAST, IQ-TREE, PHENIX]

### The bacterial toxin colibactin triggers prophage induction. (Nature 2022)

- DOI: 10.1038/s41586-022-04444-3 | PMCID: PMC8907063 | PMID: 35197633
- Evidence: 3d ) were compiled from BLASTp results using E. coli ClbS as the query (nr protein sequences database, expect threshold = 0.05, word size = 6, BLOSUM62 matrix, 5,000 entries).
- Full pipeline: quantification [ImageJ v1.53c] -> stage not stated [BLAST]

### Bacteriophages suppress CRISPR-Cas immunity using RNA-based anti-CRISPRs. (Nature 2023)

- DOI: 10.1038/s41586-023-06612-5 | PMCID: PMC10651486 | PMID: 37853129
- Evidence: Next, repeat sequences were aligned with BLASTn 65 against the masked input sequence with task = blastn − short and word size =6.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2, MAFFT, SAMtools v1.16.1]

### Clustering predicted structures at the scale of the known protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06510-w | PMCID: PMC10584675 | PMID: 37704730
- Evidence: When searching the NR database using NCBI BLAST 28 , we found no bacterial hits for the human AIM2 gene.
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX v1.5, ColabFold, Matplotlib v3.6.2, seaborn v0.12.2]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Evidence: The reduced set of sequences was aligned with MUSCLE 64 (v.5.1) and the resulting multiple sequence alignment (MSA) used as input for three independent BLASTp 65 searches over the eukaryotic, archaea and bacterial sequences in nr filtered to 70% sequence identity (nr_euk70, nr_arc70, nr_bac70) through the MPI Bioinformatics toolkit as of January 2023.
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Nuclear genetic control of mtDNA copy number and heteroplasmy in humans. (Nature 2023)

- DOI: 10.1038/s41586-023-06426-5 | PMCID: PMC10447254 | PMID: 37587338
- Version used: **2.13.0**
- Evidence: To search for regions of homology to the mtDNA within the reference nucDNA, we used BLASTn 2.13.0 with the GRCh37 reference genome with a word size of 11, an expected threshold of 0.05, short queries enabled and default values for the other parameters.
- Full pipeline: quality control [BCFtools] -> alignment/mapping [BCFtools, BLAST v2.13.0, GATK v4.2.6.0, MUSCLE, Mutect2] -> variant calling [GATK v4.2.6.0, Mutect2, VEP] -> stage not stated [LDSC, SAIGE v1.1.5, SAMtools v1.9]

### Small protein modules dictate prophage fates during polylysogeny. (Nature 2023)

- DOI: 10.1038/s41586-023-06376-y | PMCID: PMC10432266 | PMID: 37495698
- Evidence: To investigate phage genomes for potential TF 63 -associated marker genes, we first performed a preliminary BLASTp search against the NCBI nr/nt database using TF 63 as a query (accession number WP_016786069 ).
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, Prokka v1.11, Python]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Evidence: IRs (right-end and left-end) seeds were extracted from the same Spu seed locus and used as inputs to search for ends in all contigs from Spu using blastn with a word length of 7.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Inference and reconstruction of the heimdallarchaeial ancestry of eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-023-06186-2 | PMCID: PMC10307638 | PMID: 37316666
- Evidence: Identification of homologous protein families All-versus-all similarity searches of all predicted proteins from the A64 taxon selection (64 Asgard, 76 TACK, 43 Euryarchaea and 41 DPANN archaea; Supplementary Table 2 ) were performed using diamond 90 BLASTp (--more-sensitive --evalue 0.0001 --max-target-seqs 0 --outfmt 6).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, SAMtools v1.3.1, Trimmomatic v0.36] -> alignment/mapping [Bowtie2 v2.3.5.1, SAMtools v1.3.1] -> stage not stated [BLAST, Cutadapt v1.12, IQ-TREE v2.0, Prokka v1.12, SPAdes]

### Tree islands enhance biodiversity and functioning in oil palm landscapes. (Nature 2023)

- DOI: 10.1038/s41586-023-06086-5 | PMCID: PMC10247383 | PMID: 37225981
- Version used: **2.7.1**
- Evidence: OTUs were classified taxonomically using the BLAST (blastn, v.2.7.1) algorithm 66 and the UNITE v.7.2 (UNITE_public_01.12.2017.fasta) reference database 67 .
- Full pipeline: stage not stated [BLAST v2.7.1, Cutadapt v2.5, R, fastp v0.20.0]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Evidence: Orthologue Inference Orthologues were inferred between species by finding reciprocal-best BLASTp 97 hits between the proteins in the genomes, or with OrthoFinder (v.2.3.7) 98 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: ...terATCTCTCTCTTTTCCTCCTCCTCCGTTGTTGTTGTTGAGAGAGAT>gnl|uv|NGB00973.1:1-35 Pacific Biosciences C2 PrimerAAAAAAAAAAAAAAAAAATTAACGGAGGAGGAGGA It then runs blastn with tuned parameters to detect adapter-containing reads as follows: blastn -db ${DATABASE} -query ${HIFI_FASTA} -task blastn -reward 1 -penalty -5 -gapopen 3 -gapextend 3 -dust no -soft_masking true -evalue 700 -searchsp 1750000000000 -outfmt...
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: Curation of hallmark genes The amino acid sequence datasets for RNApolA, RNApolB, DNApolB and TFIIS were manually curated through BLASTp alignments (BLAST 55 v2.10.1) and phylogenetic reconstructions, as previously described for eukaryotic hallmark genes 20 .
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: A BLASTp search was then performed against this database starting from each of the proteins included in the L. erinacea genome.
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Cas12a2 elicits abortive infection through RNA-triggered destruction of dsDNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05559-3 | PMCID: PMC9811890 | PMID: 36599979
- Evidence: These Cas12a2 protein sequences were used as seeds for BLASTp searches of protein data in NCBI and for tBLASTn searches of metagenomic data in NCBI ( https://www.ncbi.nlm.nih.gov ) and JGI ( https://img.jgi.doe.gov ) to identify additional putative Cas12a2 nucleases.
- Full pipeline: read trimming [RAxML] -> alignment/mapping [Bowtie2, MAFFT v7.490, RAxML] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST, Python]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: P. syntrophicum’ were used as queries in BLASTp searches ( e = 1 × 10 −10 ) against the recently published collection of Asgard clusters of orthologous genes 2 to obtain the asCOG numbers and annotation.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Soil microbiomes show consistent and predictable responses to extreme events. (Nature 2024)

- DOI: 10.1038/s41586-024-08185-3 | PMCID: PMC11655354 | PMID: 39604724
- Version used: **2.13**
- Evidence: For identification of dif sequences, we used nucleotide BLAST v.2.13 (blastn 94 ) with the blastn-short task settings, counting every sequence in which at least one match had an e-value of 0.01 or less as a hit.
- Full pipeline: read trimming [Cutadapt v1.2.1] -> quantification [vegan] -> differential/statistical testing [R, ggplot2 v3.3] -> visualisation [vegan] -> stage not stated [BLAST v2.13, DADA2 v1.24, lme4 v3.1, tidyverse]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: The protein search was done using DIAMOND 91 under specific parameters: “blastp -e 1e-10 -k 10000000 --query-cover 66 --subject-cover 50 -b8 -c1”.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Evidence: We used the BLASTn algorithm, the dc-megablast task and a word size of 11 and maintained the defaults for all other settings.
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### A bacterial immunity protein directly senses two disparate phage proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08039-y | PMCID: PMC11578894 | PMID: 39415022
- Evidence: Homologues of the MCPs or Gp54 Bas11 in BASEL phages were identified by BLASTp 44 searches against each phage genome, and aligned by MUSCLE 45 .
- Full pipeline: alignment/mapping [BLAST, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **2.11.0**
- Evidence: First, we obtained H. cetorum gene sequences using BLASTing (blastn v.2.11.0) 72 of a Hardy and a Ubiquitous version of each differentiated gene against the H. cetorum genome.
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Diverse anti-defence systems are encoded in the leading region of plasmids. (Nature 2024)

- DOI: 10.1038/s41586-024-07994-w | PMCID: PMC11541004 | PMID: 39385022
- Evidence: Specifically, we used BLAST+ (v.2.10.0) 73 , with an e value threshold of 10 −6 and the following parameters ‘-task blastn-short -word_size 5’ against relaxase/ traM -containing contigs (11,908 WGS plasmids and 1,019,093 genomic and metagenomic contigs).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [ChimeraX] -> stage not stated [BLAST, HMMER, Prokka]

### Commensal consortia decolonize Enterobacteriaceae via ecological control. (Nature 2024)

- DOI: 10.1038/s41586-024-07960-6 | PMCID: PMC11424487 | PMID: 39294375
- Evidence: The homology search for the predicted genes was performed using diamond 57 version 2.0.15 with “blastp --evalue 0.00001 --id 30 --query-cover 60 --ultra-sensitive” options, with KEGG (downloaded on 19 April 2022) 58 , COG (downloaded on 19 May 2021) 59 , VFDB (downloaded on 10 September 2022) 60 , and UniRef90 (downloaded on 24 May 2022; https://www.uniprot.org/help/uniref ) databases.
- Full pipeline: read trimming [DADA2, R v4.3.3, Trimmomatic] -> alignment/mapping [Bowtie2, featureCounts, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, Prokka v1.14.0]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **2.0.9**
- Evidence: To identify related viruses, we screened the Sequence Read Archive (SRA) RdRp microassemblies generated by Serratus 60 using DIAMOND BLASTx (v2.0.9) 37 ( e -value threshold of 10 −5 and the “--ultra-sensitive” flag) 37 with Haseki tick virus ( UTQ11742 ) as the query.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Evidence: Benchmarking sequence and structure methods For all protein clusters with at least two sequence clusters, we conducted all-by-all alignments between members using MMseqs2 (version b0b8e85f3b8437c10a666e3ea35c78c0ad0d7ec2), DIAMOND blastp 61 (version 0.9.14), or jackhmmer 62 (version 3.1b2).
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Evidence: Predicted gene annotations obtained from BRAKER were processed using a combination of NCBI BLAST+ (v2.9.0-2) 67 , AGAT (v1.2.1) ( https://github.com/NBISweden/AGAT ), InterProScan (v5.64-96.0) 68 , 69 , and R (v4.2.0).
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### An enterococcal phage-derived enzyme suppresses graft-versus-host disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07667-8 | PMCID: PMC11291292 | PMID: 38987594
- Evidence: The prophage contig sequences were searched against the viral RefSeq data mentioned above (‘Viral nucleotide and protein database’) using blastn (BLAST+ v.2.5).
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> dimensionality reduction/clustering [SPAdes v3.13.0] -> differential/statistical testing [SPAdes v3.13.0] -> stage not stated [BLAST, Cutadapt, QIIME 2 v2018.11, R, SAMtools, ggplot2 v3.3.6]

### Bridge RNAs direct programmable recombination of target and donor DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07552-4 | PMCID: PMC11208160 | PMID: 38926615
- Evidence: First, the IS621 protein sequence was searched against the complete IS110 database for orthologues using blastp (‘-max_target_seqs 1000000 -evalue 1e-6’).
- Full pipeline: alignment/mapping [BWA, minimap2] -> dimensionality reduction/clustering [HMMER] -> stage not stated [BEDTools, BLAST, Python]

### Structural mechanism of bridge RNA-guided recombination. (Nature 2024)

- DOI: 10.1038/s41586-024-07570-2 | PMCID: PMC11208158 | PMID: 38926616
- Evidence: In brief, IS621 orthologue sequences were searched (blastp) against a curated database of IS110 elements extracted from publicly available genomic sequence archives 42 .
- Full pipeline: structure determination [ChimeraX] -> visualisation [ChimeraX] -> stage not stated [BLAST, ColabFold]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Evidence: Next, ampliconic regions were identified as a union of palindromes and regions with high intrachromosomal similarity (that is, similar to other locations within non-PAR, here identified as consecutive 5-kb windows mapping with ≥50% identity to the repeat-masked chromosomes using blastn from BLAST+ v.2.5.0 86 , 87 , excluding self-alignments, and spanning >90 kb).
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### The temperature sensor TWA1 is required for thermotolerance in Arabidopsis. (Nature 2024)

- DOI: 10.1038/s41586-024-07424-x | PMCID: PMC11136664 | PMID: 38750356
- Evidence: Protein sequence alignments Homologues of TWA1 were identified through BLASTp searches against genomes on NCBI ( https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins ).
- Full pipeline: alignment/mapping [BLAST]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: T. diatomicola genome were identified using blastn (BLAST+ (ref.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Evidence: We used both NCBI BLASTn and discontinuous mega-blast 72 to identify orthologous sequences for our six GARs.
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### DNA glycosylases provide antiviral defence in prokaryotes. (Nature 2024)

- DOI: 10.1038/s41586-024-07329-9 | PMCID: PMC11078745 | PMID: 38632404
- Evidence: NCBI blastn of the T4-resistant metagenomic DNA sequence To identify possible organisms that our metagenomic DNA comes from, we performed a nucleotide BLAST on NCBI using the algorithm for somewhat similar sequences (blastn) ( https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&BLAST_SPEC=GeoBlast&PAGE_TYPE=BlastSearch ).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MUSCLE, Python] -> normalisation [Python] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, ColabFold]

### A distinct Fusobacterium nucleatum clade dominates the colorectal cancer niche. (Nature 2024)

- DOI: 10.1038/s41586-024-07182-w | PMCID: PMC11006615 | PMID: 38509359
- Evidence: Colony PCR products were sent for Sanger sequencing, and BLASTn analysis of trace sequences was used to confirm bacterial species identity.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2 v2.4.5] -> machine learning [DADA2] -> stage not stated [BLAST, Flye]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Evidence: Additional orthologues of C. elegans piRNA effector genes were identified through reciprocal blastp searches, synteny conservation, and gene trees from Wormbase Parasite 59 .
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: Although the comparison of human and mice non-coding sequences is difficult, a simple mouse/human BLASTn alignment for Sirpa regulatory elements identified conserved ELK1-binding motifs in the Sirpa enhancer and promoter regions (Extended Data Fig.
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Evidence: Proteinortho version 6.0b 96 (using parameters: -p=blastn -singles -keep) was used to conduct an orthology study in order to find orthologous genes in the four reference genomes used 96 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Evidence: We identified Hox and bystander genes in three steps: (i) starting from human gene names, we searched for orthologues in the other species using our set of reconciled gene trees (GeneRax trees); (ii) we used NCBI blastp (ref.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Functional and evolutionary significance of unknown genes from uncultivated taxa. (Nature 2024)

- DOI: 10.1038/s41586-023-06955-z | PMCID: PMC10849945 | PMID: 38109938
- Evidence: For mapping the sequences of the novel families against TARA protein sequences we used DIAMOND blastp with the -- sensitive flag.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega, DIAMOND] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [R] -> structure determination [Clustal Omega] -> stage not stated [ColabFold, HMMER, eggNOG]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: 5 ), using Roary 50 (v.3.12.0) and a 60% minimum sequence identity threshold for BLASTp 51 .
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Version used: **2.6.0**
- Evidence: Phylogenetic tree construction A candidate set of sequences was identified using BLASTp v.2.6.0 62 using the protein sequence for KaiB from S. elongatus (NCBI: WP_011242647.1 ) as a query.
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Evidence: The genes were extracted by searching with Diamond blastp using representative protein sequences as queries from two distantly related cyanophages, P60 and S-SRP02: P60_gp14 (primase-helicase is missing from S-SRP02), P60_gp18 and SSRP02_p034, P60_gp26 and SSRP02_p038, P60_gp27 and SSRP02_p039, P60_gp28 and SSRP02_p040, P60_gp29 and SSRP02_p041, P60_gp30 and SSRP02_p042, P60_gp40 and SSRP02_p011, ...
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Version used: **2.9.0**
- Evidence: For all six pairwise directional comparisons between the three species, we ran tblastx (NCBI BLAST v.2.9.0).
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Version used: **2.7.1**
- Evidence: DGRs were identified using DGRscan 86 with the default settings, and remote VRs were identified querying the template repeat using BLASTn (v.2.7.1+) (-dust no -perc_identity 75 -qcov_hsp_perc 50 -ungapped -word_size 4).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Version used: **2.12.0**
- Evidence: First, we transferred the annotation of the reference CDS on the CDS identified de novo in the assemblies with a nucleotide sequence similarity search, using blastn v.2.12.0 (ref.
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: We constructed a blast database from the Trinity output and searched for the human ZNF729 nucleotide sequence using blastn and tblastx algorithms 85 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Evidence: For relevant lost families, we assessed whether the best blastp match in relevant species belonged to another gene family to disclose potential gene fragmentation related to evolutionary acceleration.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: To infer their identity, we applied BLASTn on each of the DE uTARs against the nucleotide collection (nt) database (with a threshold of maximum e value of 0.01 and a minimum bit score of 50) using either the entire length of the uTAR or the peak coverage region (full width at half maximum region around the absolute peak in coverage after Gaussian smoothing in the uTAR location).
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Version used: **2.12.0**
- Evidence: Potential homologies were detected using blastn 2.12.0 with -perc_identity 80 and -word_size 5, for which the sequences inside the search windows were passed using the -subject and -query parameters.
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Evidence: Subsequently, these sequences were aligned to the unspliced DNA sequences of protein-coding genes from the GRCG7b assembly using BLASTn (BLAST+ 2.4) 64 , with the settings -perc_identity 95 and -evalue 0.001.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### Microbiota-driven antitumour immunity mediated by dendritic cell migration. (Nature 2025)

- DOI: 10.1038/s41586-025-09249-8 | PMCID: PMC12390848 | PMID: 40659786
- Evidence: The species of the strains were determined by NCBI BLAST searches if the similarity between the query and the results exceeded 99%.
- Full pipeline: read trimming [Cutadapt v4.2] -> alignment/mapping [DIAMOND v2.0.13] -> quantification [Bracken v2.9, Kraken2 v2.1.3, QIIME 2 v1.9.1] -> differential/statistical testing [R v4.02] -> visualisation [ImageJ] -> stage not stated [BLAST, DADA2 v1.26.0, Flye v2.9.5, fastp v0.23.2]

### The spatiotemporal distribution of human pathogens in ancient Eurasia. (Nature 2025)

- DOI: 10.1038/s41586-025-09192-8 | PMCID: PMC12286840 | PMID: 40634616
- Evidence: To further authenticate putative hits with low read counts ( n ≤ 100 final reads), we carried out a BLASTn analysis.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [BLAST] -> stage not stated [R]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: 1a , a BLASTp search of a local copy of the NCBI NR database (downloaded April 4, 2023) was queried with 124 DRT9 (i.e., UG28) sequences identified by Mestre et al.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Haplotype gene pairs were identified by reciprocal best hits and synteny using blastp and MCScanX 69 , and only genes shared between both haplotypes were included.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Drivers of avian genomic change revealed by evolutionary rate decomposition. (Nature 2025)

- DOI: 10.1038/s41586-025-08777-7 | PMCID: PMC12119353 | PMID: 40108459
- Evidence: Gene identities were inferred using the best blastn match 85 and used as input for testing enrichment of KEGG terms using clusterProfiler 86 .
- Full pipeline: dimensionality reduction/clustering [BLAST, clusterProfiler] -> differential/statistical testing [brms] -> structure determination [phytools] -> visualisation [phytools] -> stage not stated [IQ-TREE v2.1.2, R]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Version used: **2.13**
- Evidence: Phylogeny CNGC15 sequences were identified through BLASTp and BLASTn v.2.13 searches against genomes on Phytozome v.13 (ref.
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: Each window was searched back to the genome using blastn 56 (v.2.9.0), and windows with a primary alignment score at least 1.5× higher than the secondary alignment (and exceeding a score of 1,000) were considered to be valid.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: As Cas12a2 targets RNA instead of DNA, the identified lower-mismatch-containing sequences were analysed using NCBI BLAST.
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### DNA damage drives antigen diversification in Trypanosoma brucei. (Nature 2026)

- DOI: 10.1038/s41586-026-10337-6 | PMCID: PMC13233330 | PMID: 41951731
- Evidence: VSGs were clustered into family groups using either BLASTn 77 or UCLUST algorithms 85 .
- Full pipeline: alignment/mapping [ChimeraX v1.7.1] -> dimensionality reduction/clustering [BLAST] -> visualisation [ChimeraX v1.7.1] -> stage not stated [ColabFold, R v4.0.2]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **2.13.0**
- Evidence: Non-human sequences (bacterial, viral, fungal and archaeal sequences) were detected by aligning to the NCBI RefSeq database using blastn (v.2.13.0) 69 (-task megablast -word_size 28 -evalue 0.0001 -perc_identity 98.0) and removed.
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Capturing dynamic phage-pathogen coevolution by clinical surveillance. (Nature 2026)

- DOI: 10.1038/s41586-026-10136-z | PMCID: PMC12987554 | PMID: 41813903
- Evidence: We performed BLASTn searches against ICP1 genomes using odn , adi and CRISPR–cas from ICP1_2001_Dha_0, ICP1_2006_Dha_E or ICP1_2011_Dha_A as queries.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [BLAST, ColabFold, IQ-TREE v2.2.0, SPAdes, fastp v0.23.2]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: ID) compares Evo 2-generated proteins with natural proteins found via a BLASTp query. g , Example Evo 2-generated approximately 600-kb DNA sequence.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **2.15.0**
- Evidence: Using blastn (v.2.15.0+), we aligned the reads to the corresponding BGC-rich acidobacterial MAGs reconstructed from the short-read metagenome of the same sample (that is, TARA_SAMEA6034818_MAG_00000048, TARA_SAMEA6034818_MAG_00000020 or TARA_SAMEA6035815_MAG_00000013).
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### Chemical capture of diazo metabolites reveals biosynthetic hydrazone oxidation. (Nature 2026)

- DOI: 10.1038/s41586-025-10079-x | PMCID: PMC13061610 | PMID: 41639443
- Evidence: To begin this analysis, the protein sequence of AzaE ( WP_091038156.1 ) was queried against the NCBI nucleotide collection database (November 2023) and the non-redundant protein sequence database in tblastn and blastp searches, respectively.
- Full pipeline: visualisation [Cytoscape] -> stage not stated [AlphaFold, BLAST, InterProScan, Prokka]

### Construction of complex and diverse DNA sequences using DNA three-way junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-10006-0 | PMCID: PMC12979194 | PMID: 41565816
- Evidence: In this pipeline, read sequences were aligned to fragment references using BLASTn, in which every read was aligned to every fragment reference.
- Full pipeline: alignment/mapping [BLAST] -> visualisation [Python]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Evidence: Methods Orthologue identification, phylogenetic analysis and sequence alignment We used previously identified Cas12a2 protein sequences 27 as queries for tBLASTn and BLASTp searches in the NCBI databases ( https://www.ncbi.nlm.nih.gov ) and the JGI Integrated Microbial Genomes and Microbiomes database ( https://img.jgi.doe.gov ) to identify closely related orthologues.
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### A direct role for a mitochondrial targeting sequence in signalling stress. (Nature 2026)

- DOI: 10.1038/s41586-025-09834-x | PMCID: PMC7618714 | PMID: 41372412
- Version used: **2.14.0**
- Evidence: For species with gene annotations, we blasted the S. cerevisiae MGE1 (blastn v2.14.0+) to the transcriptome to identify the homolog which we then blasted back to the S. cerevisiae (R64) CDS sequences to ensure reciprocal best hit.
- Full pipeline: quantification [R v4.4.1, featureCounts] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [AlphaFold, BLAST v2.14.0, ImageJ]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Version used: **2.13.0**
- Evidence: ORFs were then BLASTed against the S. cerevisiae proteome using a local version of NCBI blastp (v.2.13.0+, default parameters) 55 .
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Evidence: Remaining antitoxin candidates were further characterized using Foldseek Search Server 83 searches of the AlphaFold 3-predicted structures (probability threshold of 0.6), blastp searches against the non-redundant protein database ( e -value threshold of 1) and HHpred searches (probability threshold of more than 90%) 84 to select a final of ten antitoxin candidates.
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Version used: **2.14.0**
- Evidence: Novel core HG validation To test the robustness, novel core HGs were tested by BLASTp v.2.14.0 + 77 using NCBI RefSeq database 78 (downloaded on 23 August 2023), which contains a broad range of high-quality molecular sequences.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### The biosynthesis of thymol, carvacrol, and thymohydroquinone in Lamiaceae proceeds via cytochrome P450s and a short-chain dehydrogenase. (PNAS 2021)

- DOI: 10.1073/pnas.2110092118 | PMCID: PMC8719858 | PMID: 34930840
- Evidence: The limonene-6-hydroxylase from Mentha spicata (CYP71D18) ( 21 ) was used as a query in a blastp search of an EST database generated from peltate trichomes of Origanum vulgare ( 14 ).
- Full pipeline: stage not stated [BLAST, R v4.0.3]

### Anatomy of an extensively drug-resistant <i>Klebsiella pneumoniae</i> outbreak in Tuscany, Italy. (PNAS 2021)

- DOI: 10.1073/pnas.2110227118 | PMCID: PMC8640832 | PMID: 34819373
- Evidence: The peg-344 gene was identified using a BLASTn search of draft genome assemblies (accession no.
- Full pipeline: differential/statistical testing [BEAST v2.6.5] -> machine learning [BEAST v2.6.5] -> stage not stated [BLAST]

### Adaptive divergence in shoot gravitropism creates hybrid sterility in an Australian wildflower. (PNAS 2021)

- DOI: 10.1073/pnas.2004901118 | PMCID: PMC8617494 | PMID: 34789571
- Evidence: The region of the scaffold containing the SNP was annotated using the local alignment search tool BLASTx using The National Center for Biotechnology Information (NCBI) database ( 76 ).
- Full pipeline: alignment/mapping [BLAST] -> variant calling [SAMtools v0.1.16] -> stage not stated [BUSCO, ImageJ, R]

### No evidence for colonization of oral bacteria in the distal gut in healthy adults. (PNAS 2021)

- DOI: 10.1073/pnas.2114152118 | PMCID: PMC8594488 | PMID: 34610963
- Evidence: A nucleotide basic local alignment search tool (BLASTn) search mapped this ASV to D. invisus type strain (DSM 15470) and D. invisus strain JCM 17566 (100% identity; e-value 4 × 10 −150 ).
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [BLAST] -> differential/statistical testing [R v3.4] -> stage not stated [DADA2, phyloseq]

### Emergent RNA-RNA interactions can promote stability in a facultative phototrophic endosymbiosis. (PNAS 2021)

- DOI: 10.1073/pnas.2108874118 | PMCID: PMC8463893 | PMID: 34521754
- Evidence: A BLASTn search of these 23-nt endosymbiont reads was conducted against the “host” transcript dataset to identify host transcripts with ≥95% identity over a 23-nt region.
- Full pipeline: quality control [FastQC] -> read trimming [HISAT2, Trim Galore] -> alignment/mapping [HISAT2] -> quantification [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [BLAST]

### The conserved fertility factor SPACA4/Bouncer has divergent modes of action in vertebrate fertilization. (PNAS 2021)

- DOI: 10.1073/pnas.2108777118 | PMCID: PMC8488580 | PMID: 34556579
- Evidence: ...8 ) were downloaded from uniprot ( https://www.uniprot.org/ ) and searched via the National Center for Biotechnology Information (NCBI) protein BLAST blastp ( https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins ) for homologous protein sequences in Mus musculus (taxid:10090) or Homo sapiens (taxid:9606), reptiles (taxid:8459), Xenopus (taxid:8353), fugu (taxid:31032), Danio rerio (taxid:7955), ...
- Full pipeline: stage not stated [BLAST]

### Biodiversity of coral reef cryptobiota shuffles but does not decline under the combined stressors of ocean warming and acidification. (PNAS 2021)

- DOI: 10.1073/pnas.2103275118 | PMCID: PMC8488634 | PMID: 34544862
- Evidence: Sequences were annotated using three approaches: BLASTn against the Mo’orea BIOCODE Inventory, ecotag ( 97 ), and Informatic Sequence Classification Trees ( 98 ) to maximize annotations due to the paucity of marine invertebrate barcodes within reference databases.
- Full pipeline: stage not stated [BLAST, R v3.5.2]

### Haplotype divergence supports long-term asexuality in the oribatid mite <i>Oppiella nova</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2101485118 | PMCID: PMC8463897 | PMID: 34535550
- Evidence: Additionally, for annotation, scaffolds were blasted using ncbi-blast v2.7.1+ blastn with options -outfmt '6 qseqid staxids bitscore evalue std sscinames sskingdoms stitle' -max_target_seqs 10 -max_hsps 1 -evalue 1e-25 against the nt database v 2016–06.
- Full pipeline: read trimming [STAR v2.5.3a, Trim Galore v0.6.5, Trimmomatic v0.36, kallisto v0.43.1] -> alignment/mapping [BEDTools v2.26.0, Bowtie2 v2.3.4.1, GATK v4.0.3.0, Picard v2.20.2, SAMtools, STAR v2.5.3a, kallisto v0.43.1] -> variant calling [BEDTools v2.26.0, VCFtools v0.1.15] -> quantification [kallisto v0.43.1] -> normalisation [SPAdes v3.10.1, VCFtools v0.1.15] -> dimensionality reduction/clustering [VCFtools v0.1.15] -> differential/statistical testing [BUSCO v3.0.2] -> stage not stated [BLAST, R, RepeatMasker v4.0.7]

### Tracking the transition to agriculture in Southern Europe through ancient DNA analysis of dental calculus. (PNAS 2021)

- DOI: 10.1073/pnas.2102116118 | PMCID: PMC8364157 | PMID: 34312252
- Evidence: We aligned the extracted reads against the CARD database with blastn ( 32 ).
- Full pipeline: read trimming [Kraken2] -> alignment/mapping [BEDTools, BLAST, IQ-TREE, RepeatMasker, SAMtools] -> variant calling [BCFtools] -> quantification [Bracken] -> normalisation [BCFtools] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [pheatmap] -> structure determination [IQ-TREE] -> visualisation [R] -> stage not stated [VCFtools, tidyverse]

### Periscope Proteins are variable-length regulators of bacterial cell surface interactions. (PNAS 2021)

- DOI: 10.1073/pnas.2101349118 | PMCID: PMC8201768 | PMID: 34074781
- Evidence: Repeat sequences were clustered using BLASTp with a bit score threshold of 30 and extracting connected components of the resulting sequence similarity network (SSN).
- Full pipeline: dimensionality reduction/clustering [BLAST] -> simulation/modelling [NAMD] -> structure determination [PHENIX]

### Adaptive differentiation and rapid evolution of a soil bacterium along a climate gradient. (PNAS 2021)

- DOI: 10.1073/pnas.2101254118 | PMCID: PMC8106337 | PMID: 33906949
- Evidence: Briefly, the translated metagenomic paired-end reads were searched against the reference marker gene database with an initial BLASTp database with an E value of 1 × 10 −5 and a secondary filter against the reference hidden Markov model (HMM) profiles with an E value ranging from 1 × 10 −10 to 1 × 10 −15 depending on the individual marker gene.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> stage not stated [BLAST, SPAdes]

### Anaerobic gut fungi are an untapped reservoir of natural products. (PNAS 2021)

- DOI: 10.1073/pnas.2019855118 | PMCID: PMC8106346 | PMID: 33906945
- Evidence: Neighboring orthologous genes in each cluster are defined as bidirectional top-scoring BLASTp hits from filtered model proteins between genomes with E-value threshold of 10 −5 and are indicated by matching colors in each PKS family.
- Full pipeline: alignment/mapping [AUGUSTUS, MAFFT] -> dimensionality reduction/clustering [BLAST] -> visualisation [Cytoscape] -> stage not stated [OrthoFinder, RAxML]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: Genes were assigned to metabolic pathways by querying the mcSEED database using DIAMOND (blastp; e-value < 0.001; percent identity >80%) ( 59 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Reverse-transcribed SARS-CoV-2 RNA can integrate into the genome of cultured human cells and can be expressed in patient-derived tissues. (PNAS 2021)

- DOI: 10.1073/pnas.2105968118 | PMCID: PMC8166107 | PMID: 33958444
- Evidence: We blasted the selected sequences, using blastn, against a BLAST database made with the human and virus sequences described above.
- Full pipeline: alignment/mapping [Picard, SAMtools, STAR, deepTools, minimap2] -> stage not stated [BEDTools, BLAST, Seurat v3.2.2]

### The diversity of stomatal development regulation in <i>Callitriche</i> is related to the intrageneric diversity in lifestyles. (PNAS 2021)

- DOI: 10.1073/pnas.2026351118 | PMCID: PMC8040647 | PMID: 33782136
- Evidence: The transcriptome of each Callitriche species was searched for SMF orthologs using BLASTp (protein-protein BLAST).
- Full pipeline: read trimming [RAxML v8.2.12] -> alignment/mapping [MAFFT v7.453] -> stage not stated [BLAST]

### An introgressed gene causes meiotic drive in <i>Neurospora sitophila</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2026605118 | PMCID: PMC8092558 | PMID: 33875604
- Evidence: Homologs of Spk-1 were identified with BLASTp against the NCBI nonredundant protein database, FungiDB, and 31 additional high-quality Neurospora assemblies.
- Full pipeline: alignment/mapping [Cufflinks] -> differential/statistical testing [RAxML] -> stage not stated [ADMIXTURE, BLAST, IQ-TREE]

### The giant axolotl genome uncovers the evolution, scaling, and transcriptional control of complex gene loci. (PNAS 2021)

- DOI: 10.1073/pnas.2017176118 | PMCID: PMC8053990 | PMID: 33827918
- Evidence: The set of gar proteins and axolotl proteins were used to run a two-way blastp with default settings.
- Full pipeline: alignment/mapping [StringTie] -> stage not stated [BLAST, BUSCO]

### Incipient genome erosion and metabolic streamlining for antibiotic production in a defensive symbiont. (PNAS 2021)

- DOI: 10.1073/pnas.2023047118 | PMCID: PMC8092579 | PMID: 33883280
- Evidence: ...million nucleotides) potentially originated from Streptomyces bacteria, while the majority of the remaining 90% originated from the host according to blastn and blastx results that revealed similarities to insect sequences.
- Full pipeline: quality control [Bowtie2 v2.3.2, StringTie v1.3.3] -> read trimming [Bowtie2 v2.3.2, StringTie v1.3.3] -> alignment/mapping [Bowtie2 v2.3.2, StringTie v1.3.3] -> differential/statistical testing [DESeq2 v1.20.0] -> stage not stated [BLAST, ggplot2, ggpubr]

### The number of catalytic cycles in an enzyme's lifetime and why it matters to metabolic engineering. (PNAS 2021)

- DOI: 10.1073/pnas.2023348118 | PMCID: PMC8020674 | PMID: 33753504
- Evidence: Residue conservation was determined by BLASTp against the National Center for Biotechnology Information nonredundant sequence database.
- Full pipeline: stage not stated [BLAST, PyMOL]

### The cyanobacterium <i>Prochlorococcus</i> has divergent light-harvesting antennae and may have evolved in a low-oxygen ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2025638118 | PMCID: PMC7980375 | PMID: 33707213
- Evidence: Sequence identity between genomic sequences was computed using BLASTn with a bit-score cutoff of 50.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE, SPAdes v3.5]

### Citramalate synthase yields a biosynthetic pathway for isoleucine and straight- and branched-chain ester formation in ripening apple fruit. (PNAS 2021)

- DOI: 10.1073/pnas.2009988118 | PMCID: PMC7826400 | PMID: 33431667
- Evidence: MdCMS had about 60% similarity with AtIPMS1 and 2 and AtMAM1 and 3 based on BLASTp analysis.
- Full pipeline: stage not stated [BLAST]

### MdERDL6-mediated glucose efflux to the cytosol promotes sugar accumulation in the vacuole through up-regulating TSTs in apple and tomato. (PNAS 2021)

- DOI: 10.1073/pnas.2022788118 | PMCID: PMC7817134 | PMID: 33443220
- Evidence: Candidate genes were identified by performing a BLASTp (protein-protein BLAST) analysis against the apple gene set (amino acids) in the Malus × domestica genome, GDDH13 v1.1 ( 25 ).
- Full pipeline: stage not stated [BLAST]

### Lithogenic hydrogen supports microbial primary production in subglacial and proglacial environments. (PNAS 2021)

- DOI: 10.1073/pnas.2007051117 | PMCID: PMC7812807 | PMID: 33419920
- Evidence: Manual BLASTp searches were conducted to search for specific proteins involved in CO 2 fixation pathways, dissimilatory sulfate reduction, dissimilatory nitrate reduction, putative ferric iron reduction pathways, and reversible H 2 oxidation (i.e., [NiFe]- and [FeFe]-hydrogenases).
- Full pipeline: stage not stated [BLAST]

### The squalene route to C30 carotenoid biosynthesis and the origins of carotenoid biosynthetic pathways. (PNAS 2022)

- DOI: 10.1073/pnas.2210081119 | PMCID: PMC9907078 | PMID: 36534808
- Evidence: To identify co-occurrence of the amino oxidases in the genomic context ( Dataset S1, Tab C ), all the coding genes containing the amino oxidase Pfam domain were searched against a homemade database of the different carotenoid amino oxidase subfamilies identified in this study, using blastp with 1e −150 and 1e –10 as the e-value threshold ( 60 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE, MAFFT] -> structure determination [IQ-TREE] -> stage not stated [BLAST]

### The molecular basis for pore pattern morphogenesis in diatom silica. (PNAS 2022)

- DOI: 10.1073/pnas.2211549119 | PMCID: PMC9894196 | PMID: 36459651
- Evidence: (Scale bars: 2 µm.) BLASTp searches of the VSP1.0 against the NCBI database revealed 20 proteins with predicted functions, including the SDV protein Sin1 and seven subunits of the H + -ATPase that was previously shown to be located in SDVs and involved in valve biogenesis ( 24 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn v0.21.3] -> differential/statistical testing [Matplotlib v3.5, seaborn v0.11] -> visualisation [Matplotlib v3.5, seaborn v0.11] -> stage not stated [BLAST, NumPy, SciPy, scikit-image]

### Sex pheromone communication in an insect parasitoid, <i>Campoletis chlorideae</i> Uchida. (PNAS 2022)

- DOI: 10.1073/pnas.2215442119 | PMCID: PMC9894188 | PMID: 36442117
- Evidence: Then, BLASTn and BLASTx searches (E-value < 1e −5 ) against the non-redundant protein database were implemented to annotate the unigenes.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM v1.2.15] -> quantification [RSEM v1.2.15] -> stage not stated [BLAST]

### Interference with LTβR signaling by tick saliva facilitates transmission of Lyme disease spirochetes. (PNAS 2022)

- DOI: 10.1073/pnas.2208274119 | PMCID: PMC9704693 | PMID: 36383602
- Evidence: Based on NCBI BLAST and sequence analysis, several IpSAP homologous proteins of ticks were identified with two conserved EF-hand domains ( Fig.
- Full pipeline: stage not stated [BLAST]

### Silencing RNAs expressed from W-linked &lt;i&gt;PxyMasc&lt;/i&gt; "retrocopies" target that gene during female sex determination in &lt;i&gt;Plutella xylostella&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2206025119 | PMCID: PMC9674220 | PMID: 36343250
- Evidence: Sequences that did not show evidence of mispriming (i.e., those that did show significant homology to PxyMasc in reverse complement) were further characterized through BLASTn and translated reading frames through BLASTp analysis ( https://blast.ncbi.nlm.nih.gov/Blast.cgi ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [BLAST, Clustal Omega]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: We also compared the full element with all elements present in the Maror2 TE library using BLASTn, and retained all hits with an e-value smaller than 0.0001.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Evidence: The amino acid sequence of STE6-2p was searched with BLASTp ( 68 ) against the UniProt-KB/Swiss-Prot database ( 69 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### A generic framework for hierarchical de novo protein design. (PNAS 2022)

- DOI: 10.1073/pnas.2206111119 | PMCID: PMC9618129 | PMID: 36252041
- Evidence: To assess the difference between sequences from the naive and native-like designs, we first used BLASTp ( 53 ) to search for similar sequences in the natural repertoire.
- Full pipeline: stage not stated [AlphaFold, BLAST]

### Cryo-EM structures of light-harvesting 2 complexes from <i>Rhodopseudomonas palustris</i> reveal the molecular origin of absorption tuning. (PNAS 2022)

- DOI: 10.1073/pnas.2210109119 | PMCID: PMC9618040 | PMID: 36251992
- Evidence: This tentative sequence was then used as the basis for a BLASTp search of the Rps. palustris genome.
- Full pipeline: registration [RELION] -> structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, BLAST]

### Deep-branching acetogens in serpentinized subsurface fluids of Oman. (PNAS 2022)

- DOI: 10.1073/pnas.2206845119 | PMCID: PMC9586279 | PMID: 36215489
- Evidence: A recently published comprehensive database of Cdh/Acs complexes in Archaea and Bacteria was used for the analyses ( 53 ), along with reference homologs identified within the GenBank nr database based on protein basic local alignment search tool (BLASTp) searches of CdhA homologs encoded by the MAGs generated in this study.
- Full pipeline: read trimming [Clustal Omega v1.2.4] -> alignment/mapping [BLAST, Bowtie2, Clustal Omega v1.2.4, IQ-TREE v1.6.11] -> quantification [Bowtie2] -> differential/statistical testing [IQ-TREE v1.6.11] -> stage not stated [Prokka v1.14.5]

### Viruses direct carbon cycling in lake sediments under global change. (PNAS 2022)

- DOI: 10.1073/pnas.2202261119 | PMCID: PMC9564219 | PMID: 36206369
- Evidence: Taxonomic classification of viral sequences was performed using a network-clustering approach based on shared protein content. vOTUs' amino acid sequences were predicted by the virus genome annotation service at PATRIC ( 56 ), and a blastp all-against-all similarity search was performed with Diamond ( 94 ) using IMG VR v3 as a reference database ( 95 ).
- Full pipeline: dimensionality reduction/clustering [BLAST] -> differential/statistical testing [R]

### Leveraging orthology within maize and Arabidopsis QTL to identify genes affecting natural variation in gravitropism. (PNAS 2022)

- DOI: 10.1073/pnas.2212199119 | PMCID: PMC9546580 | PMID: 36161933
- Evidence: BBHs (reciprocal best BLAST hits) were identified using Perl scripts to perform reciprocal protein-protein BLAST (blastp from the blastall implementation) ( 46 ) of the predicted proteins from all maize intervals against all Arabidopsis genome predicted proteins, and reciprocally of predicted proteins from the Arabidopsis QTL intervals against all maize predicted proteins.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [MAFFT] -> stage not stated [BEDTools, BLAST]

### Metabolic novelty originating from horizontal gene transfer is essential for leaf beetle survival. (PNAS 2022)

- DOI: 10.1073/pnas.2205857119 | PMCID: PMC9546569 | PMID: 36161953
- Evidence: For BLASTx searches against the nonredundant NCBI protein database (nr database), up to 20 best NR hits per transcript were retained, with an E-value cutoff of ≤10 –3 and a minimum match length of 15 amino acids.
- Full pipeline: stage not stated [BLAST, BUSCO, Flye v2.8.3, InterProScan, R v9.4]

### Recurrent emergence of <i>Klebsiella pneumoniae</i> carbapenem resistance mediated by an inhibitory <i>ompK36</i> mRNA secondary structure. (PNAS 2022)

- DOI: 10.1073/pnas.2203593119 | PMCID: PMC9499542 | PMID: 36095213
- Version used: **2.6.0**
- Evidence: The ompK35 and ompK36 genes were identified in all short-read assemblies by performing BLASTn v2.6.0 ( 42 ) with a query gene from the reference genome ATCC43816 (the parental strain of ICC8001 ( 5 ) (accession CP009208 ).
- Full pipeline: alignment/mapping [BCFtools v0.1.19, BLAST v2.6.0, MUSCLE v3.8, SAMtools] -> stage not stated [Prokka v1.14.5, SPAdes v3.9.0]

### Isolation of a virus causing a chronic infection in the archaeal model organism &lt;i&gt;Haloferax volcanii&lt;/i&gt; reveals antiviral activities of a provirus. (PNAS 2022)

- DOI: 10.1073/pnas.2205037119 | PMCID: PMC9436352 | PMID: 35994644
- Evidence: The viral genome was searched against the Integrated Microbial Genomes/ virus (IMG/VR) database ( 53 ) using Basic Local Alignment Search Tool (BLASTn) ( 54 ), e value < 10 −5 , to detect uncultivated relatives from metagenomes or previous isolates.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BLAST] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R] -> stage not stated [SPAdes v3.13.1]

### Distinct evolutionary trajectories of SARS-CoV-2-interacting proteins in bats and primates identify important host determinants of COVID-19. (PNAS 2022)

- DOI: 10.1073/pnas.2206610119 | PMCID: PMC9436378 | PMID: 35947637
- Evidence: To obtain a maximum number of species along primate and bat phylogenies, further sequences were retrieved from NCBI databases using BLASTn.
- Full pipeline: stage not stated [BLAST, Cytoscape, Picard]

### The structure and activities of the archaeal transcription termination factor Eta detail vulnerabilities of the transcription elongation complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207581119 | PMCID: PMC9371683 | PMID: 35917344
- Evidence: The amino acid sequence for TK0566, encoding Eta in T. kodakarensis , was queried using the blastp suite and aligned using COBALT ( 67 ) versus the 100 top matches from the blastp query ( https://www.ncbi.nlm.nih.gov/ ).
- Full pipeline: alignment/mapping [BLAST] -> structure determination [AlphaFold] -> stage not stated [PHENIX]

### Chemometrics and genome mining reveal an unprecedented family of sugar acid-containing fungal nonribosomal cyclodepsipeptides. (PNAS 2022)

- DOI: 10.1073/pnas.2123379119 | PMCID: PMC9371744 | PMID: 35914151
- Evidence: XJ0827 upon comprehensive BLASTp searches.
- Full pipeline: stage not stated [BLAST]

### Distinct gene expression dynamics in developing and regenerating crustacean limbs. (PNAS 2022)

- DOI: 10.1073/pnas.2119297119 | PMCID: PMC9271199 | PMID: 35776546
- Evidence: Orthology annotation was performed using blastp (results are given in Dataset S29 ).
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, kallisto v0.42.5] -> quantification [R, limma] -> normalisation [R, limma] -> dimensionality reduction/clustering [clusterProfiler v4.0.0] -> differential/statistical testing [DESeq2] -> stage not stated [BLAST, JAGS]

### Leafy and weedy seadragon genomes connect genic and repetitive DNA features to the extravagant biology of syngnathid fishes. (PNAS 2022)

- DOI: 10.1073/pnas.2119602119 | PMCID: PMC9245644 | PMID: 35733255
- Evidence: We defined putative gene families via all-by-all blastp ( 39 ) and clustering with mcl ( 40 ), then we conducted a series of gene family size evolution analyses using CAFE 5 ( 41 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [InterProScan, STAR] -> dimensionality reduction/clustering [BLAST] -> stage not stated [BUSCO, Flye, RepeatMasker]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: 2.2.28+; options: ‘-task blastn -evalue 1e −10 ’) searches.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Essential functions of mosquito ecdysone importers in development and reproduction. (PNAS 2022)

- DOI: 10.1073/pnas.2202932119 | PMCID: PMC9231622 | PMID: 35696563
- Evidence: ...o Ae. aegypti , the African malaria mosquito An. gambiae , and the southern house mosquito C. quinquefasciatus were screened (TBLASTN analysis) using NCBI BLAST ( https://blast.ncbi.nlm.nih.gov/Blast.cgi ) and VectorBase BLAST ( https://vectorbase.org/vectorbase/app/search/transcript/UnifiedBlast ).
- Full pipeline: stage not stated [BLAST, Clustal Omega, ImageJ v1.53v]

### Mosquito  saliva enhances virus infection through sialokinin-dependent vascular leakage. (PNAS 2022)

- DOI: 10.1073/pnas.2114309119 | PMCID: PMC9214539 | PMID: 35675424
- Evidence: Protein sequence searches (BLASTp) of the NCBI nonredundant database returned only AAEL000229 itself ( XP_001660125.1 ) and two other Ae. aegypti variants ( AAD17916.1 and AAD16885.1 ).
- Full pipeline: stage not stated [BLAST]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Evidence: WH5701 were used as the query for tBLASTn, BLASTp, and exonerate searches in all cases below.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Evidence: NCBI BLAST + 2.6.0. was used for BLAST searches.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Variation in upstream open reading frames contributes to allelic diversity in maize protein abundance. (PNAS 2022)

- DOI: 10.1073/pnas.2112516119 | PMCID: PMC9169109 | PMID: 35349347
- Evidence: The Uniprot IDs in the published data were used to obtain protein sequences, which were searched in v5 using blastp ( 62 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HISAT2, HTSeq, SAMtools] -> stage not stated [BLAST, R]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: The NR contig set was compared against the National Center for Biotechnology Information (NCBI) Nucleotide database using BLASTn and against an NR protein sequence database using DIAMOND ( 63 ) for taxonomic annotation [with the lowest-common ancestor approach assigned by KronaTools ( 64 )].
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### A commensal-encoded genotoxin drives restriction of <i>Vibrio cholerae</i> colonization and host gut microbiome remodeling. (PNAS 2022)

- DOI: 10.1073/pnas.2121180119 | PMCID: PMC8931321 | PMID: 35254905
- Evidence: To test the presence of clb , the human metagenomic reads were aligned to the clb cluster ( clbA-S ) using blastn, with the E value cutoff of 0.00001.
- Full pipeline: alignment/mapping [BLAST] -> dimensionality reduction/clustering [BLAST] -> stage not stated [edgeR]

### <i>PRDM9</i> losses in vertebrates are coupled to those of paralogs <i>ZCWPW1</i> and <i>ZCWPW2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2114401119 | PMCID: PMC8892340 | PMID: 35217607
- Evidence: In brief, we first identified putative PRDM9 orthologs using a blastp search ( 30 ) against the RefSeq database and confirmed the orthology of each by visually inspecting where these genes clustered in neighbor-joining trees built with Clustal Omega ( 51 ) for identified KRAB, SSXRD, and SET domain sequences ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [BLAST, Clustal Omega] -> stage not stated [BUSCO, R]

### A widely distributed phosphate-insensitive phosphatase presents a route for rapid organophosphorus remineralization in the biosphere. (PNAS 2022)

- DOI: 10.1073/pnas.2118122119 | PMCID: PMC8812569 | PMID: 35082153
- Evidence: Genomes and metagenomes were stored in genome sets, and for PafA, BLASTp searches (minimum similarity 30%, E-value e −50 ) were set up using the “jobs function.” The diversity, richness, and gene and transcript abundance of phoA , phoD , phoX , and pafA in seawater was determined by searching the Tara ocean metagenome (OM-RGC_v2_metaG) and metatranscriptome (OM-RGC_v2_metaT) databases via the Ocea...
- Full pipeline: alignment/mapping [MUSCLE] -> quantification [BLAST] -> differential/statistical testing [ggplot2, tidyverse] -> visualisation [ggplot2, tidyverse] -> stage not stated [HMMER, IQ-TREE]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: We also mapped the Dll319 peak identified from the FAIRE data to the BaGv2 genome, using blastn, to identify its position in the new genome assembly and test whether the ATAC-seq analysis was also able to identify it.
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### A comparative genomics examination of desiccation tolerance and sensitivity in two sister grass species. (PNAS 2022)

- DOI: 10.1073/pnas.2118886119 | PMCID: PMC8812550 | PMID: 35082155
- Evidence: Sporobolus proteins were considered as homologous if they satisfied at least one of three criteria: 1) a blastp match with an e value of 1e-6 or lower vs. either Arabidopsis proteins [Araport11 annotation ( 43 )]; 2) vs. a collection of Glycine max , Oryza sativa subsp. japonica , Populus trichocarpa , Solanum lycopersicum , S. bicolor , Vitis vinifera , Brachypodium distachyon , Physcomitrella pa...
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, StringTie, minimap2] -> quantification [Bowtie2, StringTie, minimap2] -> dimensionality reduction/clustering [OrthoFinder v2.3.8] -> differential/statistical testing [Cytoscape, DESeq2, Python v3.6.8, edgeR] -> stage not stated [BLAST, BUSCO, InterProScan, Matplotlib, R v3.6, RepeatMasker]

### <i>Bacteroides thetaiotaomicron</i> uses a widespread extracellular DNase to promote bile-dependent biofilm formation. (PNAS 2022)

- DOI: 10.1073/pnas.2111228119 | PMCID: PMC8851478 | PMID: 35145026
- Evidence: The obtained genomes were annotated using RASTtk ( 52 , 53 ) on the patricbrc.org database ( 54 ) and we searched BT3563 nucleic acid and amino acid sequence in these genomes using the BLASTp tool of patricbrc.org ( 55 , 56 ).
- Full pipeline: stage not stated [BLAST, SPAdes v3.13.0]

### A peptide toxin in ant venom mimics vertebrate EGF-like hormones to cause long-lasting hypersensitivity in mammals. (PNAS 2022)

- DOI: 10.1073/pnas.2112630119 | PMCID: PMC8851504 | PMID: 35131940
- Evidence: We used the mature peptide sequence of Mg1a as a query to search (using blastp) the National Center for Biotechnology Information nonredundant (NCBI nr) protein sequence database for related sequences.
- Full pipeline: alignment/mapping [MAFFT v7.304b, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE v2.0.6] -> stage not stated [BLAST]

### Domoic acid biosynthesis in the red alga <i>Chondria armata</i> suggests a complex evolutionary history for toxin production. (PNAS 2022)

- DOI: 10.1073/pnas.2117407119 | PMCID: PMC8833176 | PMID: 35110408
- Evidence: These sequences, in addition to representative diatom P450 sequences from publicly available transcriptomics and top BLASTp hits for RadD and DabD, were used to construct a ML phylogenetic tree ( 37 ).
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [AlphaFold, BLAST, BUSCO v4.0.5]

### Cell-free DNA profiling informs all major complications of hematopoietic cell transplantation. (PNAS 2022)

- DOI: 10.1073/pnas.2113476118 | PMCID: PMC8795552 | PMID: 35058359
- Evidence: Unmapped reads were BLASTed ( 75 ) using hs-blastn ( 76 ) to a list of C-to-T–converted microbial reference genomes.
- Full pipeline: alignment/mapping [BLAST, Bismark] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5]

### Template switching in DNA replication can create and maintain RNA hairpins. (PNAS 2022)

- DOI: 10.1073/pnas.2107005119 | PMCID: PMC8794818 | PMID: 35046021
- Version used: **2.6.0**
- Evidence: The sequences for rRNA were extracted based on the title (982 sequences in total), a Basic Local Alignment Search Tool (BLAST) database was created, and all terminal sequences were screened against it using blastn (version 2.6.0+).
- Full pipeline: read trimming [MAFFT v7.310] -> alignment/mapping [BLAST v2.6.0, MAFFT v7.310] -> dimensionality reduction/clustering [MAFFT v7.310] -> visualisation [R, ggplot2] -> stage not stated [IQ-TREE v1.6.1]

### The ectomycorrhizal fungus <i>Pisolithus microcarpus</i> encodes a microRNA involved in cross-kingdom gene silencing during symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2103527119 | PMCID: PMC8784151 | PMID: 35012977
- Evidence: A BLASTn search found that there were other E. grandis genes encoding a sequence homologous to that found in Eucgr.
- Full pipeline: stage not stated [BLAST]

### Conservation of magnetite biomineralization genes in all domains of life and implications for magnetic sensing. (PNAS 2022)

- DOI: 10.1073/pnas.2108655119 | PMCID: PMC8784154 | PMID: 35012979
- Evidence: The longest RNA transcript per gene ( n = 47,921 transcripts) was selected for inclusion in the reference transcriptome used for read-mapping, differential gene expression analysis, and bidirectional BLASTp comparison to MTB biomineralization proteins (MTB accessions available from Dataset S3 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2 v2.2.1] -> normalisation [R v3.12.1] -> dimensionality reduction/clustering [R v3.12.1] -> differential/statistical testing [BLAST, edgeR] -> visualisation [R v3.12.1] -> stage not stated [ImageJ]

### Oxidative desulfurization pathway for complete catabolism of sulfoquinovose by bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2116022119 | PMCID: PMC8795539 | PMID: 35074914
- Evidence: Each gene within the A. tumefaciens C58 SMO gene cluster ( Atu3277 - Atu3285 ) was submitted as a query to the NCBI BLASTp algorithm to search a database comprised of nonredundant protein sequences with A. tumefaciens (taxid: 358) sequences excluded.
- Full pipeline: dimensionality reduction/clustering [BLAST] -> structure determination [PHENIX, REFMAC]

### A transcriptional program underlying the circannual rhythms of gonadal development in medaka. (PNAS 2023)

- DOI: 10.1073/pnas.2313514120 | PMCID: PMC10756274 | PMID: 38109538
- Evidence: We searched for homologues of every medaka gene using BLAST searches (blastp) for all coding sequences in mice ( Mus musculus ).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5, RSEM v1.2.12] -> quantification [Bowtie2 v2.2.5, RSEM v1.2.12] -> stage not stated [BLAST, DIAMOND, Metascape v3.5, R v3.5]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Evidence: Since the genome assemblies are fragmented, the median coverage of the chromosome was calculated from the first three, largest contigs (total size sum of first three contigs 0.3 to 4.0 Mb), which were confirmed to correspond to chromosomal sequences by using BLASTn against the NCBI nr nucleotide database.
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### Massive intein content in &lt;i&gt;Anaeramoeba&lt;/i&gt; reveals aspects of intein mobility in eukaryotes. (PNAS 2023)

- DOI: 10.1073/pnas.2306381120 | PMCID: PMC10710043 | PMID: 38019867
- Evidence: Inteins detected during this first round of searching were used as queries for additional BLASTp searches. tBLASTn was used to detect potential pseudogenized inteins using the same queries as previously as well as the newly extracted complete set of Anaeramoeba full-length inteins.
- Full pipeline: alignment/mapping [IQ-TREE, MUSCLE] -> structure determination [IQ-TREE] -> visualisation [Cytoscape] -> stage not stated [BLAST]

### The genome of a bunyavirus cannot be defined at the level of the viral particle but only at the scale of the viral population. (PNAS 2023)

- DOI: 10.1073/pnas.2309412120 | PMCID: PMC10691328 | PMID: 37983500
- Evidence: 2 C ), we could not find a single significant match which could indicate the presence of a short sequence snatched from a host mRNA (BLASTn searches against Viridiplantae or Solanaceae accessions).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [IMOD] -> structure determination [IMOD] -> stage not stated [BLAST, ImageJ, NanoPlot v1.40.0]

### Male-killing virus in a noctuid moth &lt;i&gt;Spodoptera litura&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312124120 | PMCID: PMC10655585 | PMID: 37931114
- Evidence: To infer the phylogenetic position of SlMKV among closely related viruses, RdRp amino acid sequences of SlMKV-like viruses were obtained from the NCBI nonredundant protein database using a BLASTp search with a structural motif sequence of the SlMKV RdRp as the query.
- Full pipeline: read trimming [MAFFT, RAxML] -> alignment/mapping [MAFFT, RAxML] -> structure determination [MAFFT, RAxML] -> stage not stated [BLAST]

### Evidence for an ancient aquatic origin of the RNA viral order &lt;i&gt;Articulavirales&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2310529120 | PMCID: PMC10636315 | PMID: 37906647
- Version used: **2.0.9**
- Evidence: Assembled reads were screened against the NCBI nonredundant (nr) protein database (as of June 2022) and a custom RdRp database using Diamond BLASTx v.2.0.9.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.490, MUSCLE v5.1] -> quantification [RSEM v1.3.0] -> visualisation [R v4.1] -> stage not stated [BLAST v2.0.9]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **2.13.0**
- Evidence: A reciprocal best BLASTp (version 2.13.0+) search was performed to identify high-confidence homologous genes among molluscan genomes.
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### The genomic landscape of swine influenza A viruses in Southeast Asia. (PNAS 2023)

- DOI: 10.1073/pnas.2301926120 | PMCID: PMC10438389 | PMID: 37552753
- Version used: **2.2.18**
- Evidence: For each sample, reads were de novo assembled using SPAdes v3.15.3 ( 51 ), and individual gene segment was determined by BLASTn v2.2.18 ( 52 ).
- Full pipeline: quality control [FastQC, Trimmomatic v0.39] -> read trimming [FastQC, Trimmomatic v0.39] -> structure determination [BEAST v10.4, RAxML v1.1.0] -> stage not stated [BLAST v2.2.18, SPAdes v3.15.3]

### A Mediator subunit imparts robustness to a polyphenism decision. (PNAS 2023)

- DOI: 10.1073/pnas.2308816120 | PMCID: PMC10410750 | PMID: 37527340
- Evidence: To identify homologs of P. pacificus , we performed a reciprocal best-hit BLASTp against the C. elegans genome.
- Full pipeline: alignment/mapping [R] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [BLAST, DESeq2]

### A bacterial-like Pictet-Spenglerase drives the evolution of fungi to produce β-carboline glycosides together with separate genes. (PNAS 2023)

- DOI: 10.1073/pnas.2303327120 | PMCID: PMC10372676 | PMID: 37467272
- Evidence: The McbB protein sequence was used to retrieve bacterial PS enzymes and the McbB-like Fcs1 was used for the BLASTp search of fungal homologous proteins against the NCBI databases at a cutoff value of less than 100e-1.
- Full pipeline: stage not stated [AlphaFold, BLAST, PyMOL v2.4]

### A periplasmic phospholipase that maintains outer membrane lipid asymmetry in <i>Pseudomonas aeruginosa</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302546120 | PMCID: PMC10374164 | PMID: 37463202
- Evidence: P. aeruginosa homologs of E. coli MlaA, MlaB, MlaC, MlaD, MlaE, MlaF, and PldA were identified using the UniProt Basic Local Alignment Search Tool (BLAST) program blastp with an E-threshold of 0.0001 and the BLOSUM62 matrix ( 71 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.490, PyMOL] -> stage not stated [AlphaFold, IQ-TREE v1.6.12]

### Pumping iron: A multi-omics analysis of two extremophilic algae reveals iron economy management. (PNAS 2023)

- DOI: 10.1073/pnas.2305495120 | PMCID: PMC10372677 | PMID: 37459532
- Evidence: Protein similarity networks were generated from an all-vs.-all blastp ( 53 ) analysis (pairwise alignment between all pairs of proteins) of sequences in a local sequence database.
- Full pipeline: alignment/mapping [BLAST] -> visualisation [PyMOL v1.7.4] -> stage not stated [ColabFold, Cytoscape v3.4, OrthoFinder v2.5.2]

### A conserved RWP-RK transcription factor VSR1 controls gametic differentiation in volvocine algae. (PNAS 2023)

- DOI: 10.1073/pnas.2305099120 | PMCID: PMC10629530 | PMID: 37436957
- Evidence: S2 C ) but are not a previously defined domain detectable with NCBI BLAST conserved domain search.
- Full pipeline: stage not stated [BLAST]

### Identification of a second glycoform of the clinically prevalent O1 antigen from <i>Klebsiella pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2301302120 | PMCID: PMC10629545 | PMID: 37428935
- Evidence: The difference in genetic data for K. pneumoniae CWK2 and B5055 prompted a broader analysis of wbbZ status, by exploiting a blastn search of the collection of 1,717 geographically diverse Klebsiella isolates from the European Survey of Carbapenemase-Producing Enterobacteriaceae ( 46 ) ( Dataset S1 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MAFFT] -> stage not stated [AlphaFold, BLAST]

### Horizontal gene transfer underlies the painful stings of asp caterpillars (Lepidoptera: Megalopygidae). (PNAS 2023)

- DOI: 10.1073/pnas.2305871120 | PMCID: PMC10629529 | PMID: 37428925
- Evidence: When all lepidopteran aerolysin-like proteins are used as queries in a BLASTp search against all nonlepidopteran sequences, the top hit is between a sequence from the crambid moth Ostrinia furnacalis ( XP_028165651.1 ) to “ Clostridium epsilon toxin ETX/ Bacillus mosquitocidal toxin MTX2 family pore-forming toxin” from Dickeya sp. gammaproteobacteria ( WP_038918640.1 ).
- Full pipeline: stage not stated [BLAST, HMMER]

### Hiding in plain sight: Genome-wide recombination and a dynamic accessory genome drive diversity in <i>Fusarium oxysporum</i> f.sp. <i>ciceris</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220570120 | PMCID: PMC10318998 | PMID: 37364097
- Evidence: SIX gene homologs were identified using BLASTp (E-value cutoff = 1E −6 ) and fourteen SIX gene homologs as queries ( 43 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [GATK v4.1] -> stage not stated [BLAST, BUSCO, PLINK v1.90, R, RepeatMasker, VCFtools v0.1.15]

### Role of the bicarbonate transporter SLC4γ in stony-coral skeleton formation and evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2216144120 | PMCID: PMC10268325 | PMID: 37276409
- Evidence: However, a manual BLASTn search using the Pachyseris speciosa SLC4γ nucleotide sequence as a query against the G. fascicularis genome database identified a clear SLC4γ ortholog that was not present in the predicted protein sequences ( Fig.
- Full pipeline: stage not stated [BLAST, Bowtie2]

### Nontriplet feature of genetic code in &lt;i&gt;Euplotes&lt;/i&gt; ciliates is a result of neutral evolution. (PNAS 2023)

- DOI: 10.1073/pnas.2221683120 | PMCID: PMC10235951 | PMID: 37216548
- Evidence: 5.15 ( 108 ) with parameters: −p = blastn −e = 1e−25 −identity = 70 on obtained transcriptomes.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MUSCLE] -> quantification [kallisto] -> stage not stated [BLAST]

### Disruption of the standard kinetochore in holocentric <i>Cuscuta</i> species. (PNAS 2023)

- DOI: 10.1073/pnas.2300877120 | PMCID: PMC10214151 | PMID: 37192159
- Evidence: These sequences were used for blastp searches to identify their homologs in genome assemblies of C. australis and C. campestris ( 62 , 63 ), representing monocentric Cuscuta species, and in I. nil ( 64 ), selected as a monocentric nonparasitic genus of the family Convolvulaceae.
- Full pipeline: alignment/mapping [SAMtools, STAR] -> structure determination [StringTie] -> stage not stated [BLAST, BUSCO, OrthoFinder, QUAST]

### Chitin utilization by marine picocyanobacteria and the evolution of a planktonic lifestyle. (PNAS 2023)

- DOI: 10.1073/pnas.2213271120 | PMCID: PMC10194020 | PMID: 37159478
- Evidence: To identify genes potentially involved in chitin-degradation, we searched for homologs to known chitin degradation genes ( 12 ) in Prochlorococcus strains MIT9313 and MIT1318 using blastp ( 62 ) v2.12.0+ with default settings.
- Full pipeline: alignment/mapping [HTSeq, MAFFT] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2] -> stage not stated [BLAST]

### Vertebrate-tropism of a cressdnavirus lineage implicated by poxvirus gene capture. (PNAS 2023)

- DOI: 10.1073/pnas.2303844120 | PMCID: PMC10193959 | PMID: 37155884
- Version used: **2.0.15**
- Evidence: Potential HGT-derived features were aligned to the GenBank nr database using DIAMOND BLASTp v2.0.15 ( 66 ) set to “--ultra-sensitive --max-target-seqs 50” to ensure reciprocal cressdnavirus alignment.
- Full pipeline: read trimming [IQ-TREE v2.2.0, MAFFT v7.487] -> alignment/mapping [AlphaFold v2.1.1, BEDTools, BLAST v2.0.15, IQ-TREE v2.2.0, MAFFT v7.487] -> visualisation [AlphaFold v2.1.1]

### Application of a quantitative framework to improve the accuracy of a bacterial infection model. (PNAS 2023)

- DOI: 10.1073/pnas.2221542120 | PMCID: PMC10175807 | PMID: 37126703
- Evidence: To identify genes that are present in most P. aeruginosa strains, the 291 genomes designated as “complete” on NCBI as of April 29, 2021 were downloaded and analyzed with Roary v3.13.0 using 90% as the minimum percentage identity for blastp ( Dataset S2 ) ( 48 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.10] -> read trimming [Bowtie2 v2.3.5, Cutadapt v2.6] -> alignment/mapping [Bowtie2 v2.3.5, featureCounts v2.0.1] -> normalisation [DESeq2 v1.28.1, R] -> stage not stated [BLAST]

### Bacterial origin of a key innovation in the evolution of the vertebrate eye. (PNAS 2023)

- DOI: 10.1073/pnas.2214815120 | PMCID: PMC10120077 | PMID: 37036996
- Evidence: Materials and Methods Human IRBP (also known as RBP3, accession NP_002891.1 ) was used to query the RefSeq protein database using BLASTp ( 37 ) to obtain vertebrate, nonvertebrate eukaryote, and bacterial IRBP homologs.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, BLAST, IQ-TREE, RAxML]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Evidence: Sequenced Paecilomyces genomes were identified through BLASTn searches of the NCBI whole-genome shotgun database.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### NHA1 is a cation/proton antiporter essential for the water-conserving functions of the rectal complex in <i>Tribolium castaneum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2217084120 | PMCID: PMC10068851 | PMID: 36943876
- Evidence: Interestingly, a BLASTp search against Drosophila proteins reveals that Tribolium NHA1 is more closely related to Drosophila NHA1 (53% sequence identity) than to NHA2 (35% sequence identity).
- Full pipeline: stage not stated [BLAST]

### Experimental evidence for the functional importance and adaptive advantage of A-to-I RNA editing in fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2219029120 | PMCID: PMC10041177 | PMID: 36917661
- Evidence: Gene orthologs were identified according to the ortholog families in EnsemblFungi and by BLASTp search in the NCBI nr database.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [R v4.1, featureCounts] -> normalisation [featureCounts] -> visualisation [AlphaFold, R v4.1, UCSF Chimera v1.16] -> stage not stated [BLAST]

### Light-dependent signal transduction in the marine diatom <i>Phaeodactylum tricornutum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216286120 | PMCID: PMC10089185 | PMID: 36897974
- Evidence: Sequences coding for RNA (iRNA) fragments were designed to target the functional domains of six specific genes ( Table 1 ) based on NCBI BLAST annotations.
- Full pipeline: alignment/mapping [Bioconductor] -> differential/statistical testing [Bioconductor] -> stage not stated [BLAST]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Evidence: CS-3B specific k-mers were sequences mappinguniquely (as a single copy) in the genome and trimmed to a density of a kmer/10 bp each using the “-task blastn-short” option within BlastN ( 64 ).
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **2.5.0**
- Evidence: To reconstruct origins of lecsl and leggt in Lentinula , the 28 Lentinula core genomes and all available fungal proteomes in the NCBI and MycoCosm ( 56 ) databases (December, 2020) were searched with BLASTp v2.5.0+ (Ye et al.
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### Discovery of a rapidly evolving yeast defense factor, &lt;i&gt;KTD1&lt;/i&gt;, against the secreted killer toxin K28. (PNAS 2023)

- DOI: 10.1073/pnas.2217194120 | PMCID: PMC9974470 | PMID: 36800387
- Evidence: The 10 DUP240 genes from the reference S. cerevisiae genome were used as BLASTn (BLAST+ v2.10.0) queries against each of the assembled genomes with – word_size 7 , but otherwise default parameters.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ggpubr] -> visualisation [AlphaFold v2.0.0, PyMOL v2.3.0] -> stage not stated [BLAST, R, ggplot2 v3.3.5]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Evidence: Then, BLASTp searches were conducted to retrieve those matches that displayed a positive reciprocal BLAST hit.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Prostaglandin F<sub>2α</sub> drives female pheromone signaling in cichlids, revealing a basis for evolutionary divergence in olfactory signaling. (PNAS 2023)

- DOI: 10.1073/pnas.2214418120 | PMCID: PMC9910499 | PMID: 36584295
- Evidence: To identify the repertoire of potential PGF 2α -sensitive ORs across fish species, we searched the NCBI RefSeq database for sequences similar to zebrafish Or114 -1 ( XP_009289721 ) using BLASTp.
- Full pipeline: stage not stated [BLAST]

### OmpA controls order in the outer membrane and shares the mechanical load. (PNAS 2024)

- DOI: 10.1073/pnas.2416426121 | PMCID: PMC11648852 | PMID: 39630873
- Evidence: Amino acid sequence similarity was assessed by comparison of P0A910 (OmpA) with P0A917 (OmpX) in BLASTp.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [BLAST, ImageJ, Matplotlib]

### Adaptive expression of phage auxiliary metabolic genes in paddy soils and their contribution toward global carbon sequestration. (PNAS 2024)

- DOI: 10.1073/pnas.2419798121 | PMCID: PMC11626168 | PMID: 39602267
- Evidence: The taxonomic annotation of phage was supplemented with the BLASTp mode in vConTACT2 (v0.9.17) ( 86 ).
- Full pipeline: stage not stated [BLAST, Bowtie2, DADA2, HMMER v3.1b, Prokka v1.13, SAMtools v1.16.1, SPAdes v3.14.1, eggNOG v5.0.0]

### Comprehensive deletion scan of anti-CRISPR AcrIIA4 reveals essential and dispensable domains for Cas9 inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2413743121 | PMCID: PMC11621469 | PMID: 39570312
- Evidence: To find naturally occurring AcrIIA4 homologs with deletions relative to the canonical AcrIIA4, we performed a BLASTp search on the NCBI BLASTp server using standard parameters.
- Full pipeline: differential/statistical testing [R, ggplot2] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, ChimeraX, ColabFold v1.5.5]

### Distinct evolutionary trajectories following loss of RNA interference in &lt;i&gt;Cryptococcus neoformans&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416656121 | PMCID: PMC11588098 | PMID: 39536081
- Evidence: Although this element was not identified as mobile in H99, BLASTn results suggest the presence of a similar copy (100% query coverage and 98.41% identity) in the H99 genome.
- Full pipeline: stage not stated [BLAST]

### MurA-catalyzed synthesis of 5-enolpyruvylshikimate-3-phosphate confers glyphosate tolerance in bryophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2412997121 | PMCID: PMC11588093 | PMID: 39527734
- Evidence: EPSPS and MurA amino acid sequences were identified through a protein BLASTp using MpEPSPS (Mp6g04140.1) and MpMurA (Mp5g14110.1) as queries against reference proteomes of archaeplastida, bacteria, and archaea species.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [MAFFT] -> stage not stated [AlphaFold, BLAST, ChimeraX]

### Homeotic and nonhomeotic patterns in the tetrapod vertebral formula. (PNAS 2024)

- DOI: 10.1073/pnas.2411421121 | PMCID: PMC11588047 | PMID: 39527744
- Evidence: We determined the approximate location of the Hox genes by performing a BLAST search (blastn) ( 74 ) on each genome using the gene sequence from the corresponding Hox gene from a model organism in that tetrapod class as the search sequence.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [BLAST, BUSCO, SciPy, phytools]

### SPATEs promote the survival of &lt;i&gt;Shigella&lt;/i&gt; to the plasma complement system upon local hemorrhage and bacteremia. (PNAS 2024)

- DOI: 10.1073/pnas.2319951121 | PMCID: PMC11551430 | PMID: 39475654
- Evidence: The BLASTp similarity search with SigA passenger domain as a query was carried out with default parameters (Expect threshold 0.05, word size 5, BLOSUM62 scoring matrix, gap creation penalty 11, gap extension penalty 1) in the PDB.
- Full pipeline: stage not stated [AlphaFold, BLAST, ColabFold, PyMOL v1.8.4]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: Off-targets of the gRNAs were predicted using a sequence-based approach. gRNAs in length of 30 bps were first aligned to the human transcriptome (Grch38 cdna from emsembl release 100) using blastn.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### The reconstruction of evolutionary dynamics of processed pseudogenes indicates deep silencing of "retrobiome" in naked mole rat. (PNAS 2024)

- DOI: 10.1073/pnas.2313581121 | PMCID: PMC11551321 | PMID: 39467133
- Evidence: The BLASTn command is used to perform a nucleotide sequence search against a specified database, outputting the results in a tabular format.
- Full pipeline: alignment/mapping [BEDTools] -> stage not stated [BLAST]

### Soil viral-host interactions regulate microplastic-dependent carbon storage. (PNAS 2024)

- DOI: 10.1073/pnas.2413245121 | PMCID: PMC11551317 | PMID: 39467127
- Evidence: DIAMOND was employed to align unigenes with bacterial sequences extracted from the NCBI NR database (blastp, e-value ≤ 1e −5 ) ( 75 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BLAST, Bowtie2, HMMER] -> quantification [Bowtie2] -> stage not stated [DESeq2, R v4.0.3, vegan]

### Phylogenetic evidence supporting the nonenveloped nature of hepadnavirus ancestors. (PNAS 2024)

- DOI: 10.1073/pnas.2415631121 | PMCID: PMC11551314 | PMID: 39471221
- Evidence: Protein BLAST (BLASTp) analysis indicated that the closest sequences for the C and P proteins corresponded to HBV (Genbank accession ANQ89943.1 ) and fish-associated HBV ( WAQ80622.1 ), respectively.
- Full pipeline: stage not stated [BLAST]

### Type VI secretion systems promote intraspecific competition and host interactions in a bee gut symbiont. (PNAS 2024)

- DOI: 10.1073/pnas.2414882121 | PMCID: PMC11536156 | PMID: 39441627
- Evidence: BLASTn searches against the NCBI database were conducted when necessary.
- Full pipeline: quality control [FastQC] -> read trimming [QIIME 2 v2024.2] -> alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, emmeans] -> stage not stated [BLAST, Cutadapt, DADA2, R, lme4]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Evidence: The initial BLASTp search of human HPS6 retrieved no positive RBH in the queried genomes.
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### The peptide hormone &lt;i&gt;Pj&lt;/i&gt;CLE1 stimulates haustorium formation in the parasitic plant &lt;i&gt;Phtheirospermum japonicum&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2414582121 | PMCID: PMC11494319 | PMID: 39383005
- Evidence: To test this hypothesis, we searched and identified 14 PjCLE genes by HMMR and BLASTn in its genome, of which four have not been annotated yet ( 6 ).
- Full pipeline: differential/statistical testing [BLAST]

### SHARK enables sensitive detection of evolutionary homologs and functional analogs in unalignable and disordered sequences. (PNAS 2024)

- DOI: 10.1073/pnas.2401622121 | PMCID: PMC11494347 | PMID: 39383002
- Evidence: SHARK-dive was also benchmarked against the most widely used homology search tools, BLASTp (BLAST) and pHMMER (HMMER).
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [BLAST]

### A conserved peptide-binding pocket in HyNaC/ASIC ion channels. (PNAS 2024)

- DOI: 10.1073/pnas.2409097121 | PMCID: PMC11474038 | PMID: 39365813
- Evidence: These sequences were obtained from the database of nonredundant protein sequences via blastp.
- Full pipeline: dimensionality reduction/clustering [UCSF Chimera v1.14] -> visualisation [Matplotlib v3.4.3, Python v3.9.7] -> stage not stated [BLAST]

### Halofilins as emerging bactofilin families of archaeal cell shape plasticity orchestrators. (PNAS 2024)

- DOI: 10.1073/pnas.2401583121 | PMCID: PMC11459167 | PMID: 39320913
- Evidence: Each dot represents one protein sequence, and each line represents pairwise similarity between two sequences, as calculated by BLASTp.
- Full pipeline: stage not stated [AlphaFold, BLAST]

### Snowmelt duration controls red algal blooms in the snow of the European Alps. (PNAS 2024)

- DOI: 10.1073/pnas.2400362121 | PMCID: PMC11474047 | PMID: 39312681
- Evidence: From the data, DNA molecular markers such as internal transcribed spacer (ITS1–ITS2), 18S ribosomal RNA, and plastid rbcL, were analyzed using NCBI BLAST ( 50 ).
- Full pipeline: normalisation [Matplotlib] -> machine learning [Python, SciPy] -> visualisation [Matplotlib] -> stage not stated [BLAST]

### Nuclear dualism without extensive DNA elimination in the ciliate &lt;i&gt;Loxodes magnus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2400503121 | PMCID: PMC11441545 | PMID: 39298487
- Evidence: The top BLASTp hits to GenBank’s nr database for representative Loxodes proteins encoding these domains were to B. stoltei proteins, so these elements may date to the karyorelict/heterotrich common ancestor.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [Bowtie2 v2.3.5, SAMtools, freebayes v1.3.2, minimap2 v2.24] -> variant calling [freebayes v1.3.2] -> stage not stated [BCFtools v1.11, BEDTools v2.27.1, BLAST, BUSCO, Conda, Flye v2.8.1, InterProScan v5.57, RepeatMasker v2.0.1, WhatsHap]

### Evolution of pH-sensitive transcription termination in &lt;i&gt;Escherichia coli&lt;/i&gt; during adaptation to repeated long-term starvation. (PNAS 2024)

- DOI: 10.1073/pnas.2405546121 | PMCID: PMC11441560 | PMID: 39298488
- Evidence: Rho homologs containing a histidine at the analogous E. coli R109 residue were identified using blastp with the Pattern Hit Initiated (PHI-BLAST) algorithm ( 117 ).
- Full pipeline: alignment/mapping [AlphaFold] -> differential/statistical testing [R] -> stage not stated [BLAST, PyMOL]

### Gut bacteria are essential for development of an invasive bark beetle by regulating glucose transport. (PNAS 2024)

- DOI: 10.1073/pnas.2410889121 | PMCID: PMC11331112 | PMID: 39110737
- Evidence: The identification of sugar transporters (STs) was identified based on the presence of predicted transmembrane regions using the TMHMM v.2.0 program and BLASTp in NCBI.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [R] -> stage not stated [BLAST]

### Identification and characterization of a small-molecule metallophore involved in lanthanide metabolism. (PNAS 2024)

- DOI: 10.1073/pnas.2322096121 | PMCID: PMC11317620 | PMID: 39078674
- Evidence: Gene cluster functions were predicted using hmmscan (EMBL webserver) ( 51 , 52 ) and through NCBI BLAST ( 53 ) matches against the rhodopetrobactin BGC from R. palustris TIE-1 ( 25 ).
- Full pipeline: alignment/mapping [DESeq2, StringTie] -> dimensionality reduction/clustering [BLAST, HMMER]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **2.0.9**
- Evidence: All contigs were screened against the RdRp-scan database ( 52 ) and a custom RNA virus databases using DIAMOND BLASTx v2.0.9 ( 53 ) with the setting ultrasensitive and an e-value cutoff of 1e-5.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### A broad survey of choanoflagellates revises the evolutionary history of the Shaker family of voltage-gated K&lt;sup&gt;+&lt;/sup&gt; channels in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2407461121 | PMCID: PMC11287247 | PMID: 39018191
- Evidence: Choanoflagellate Kv channels were identified with TBLASTN ( 65 ) searches of genome drafts (2 species), gene predictions (2 species), and transcriptomes (19 species) housed in the GenBank WGS, NR, and TSA databases using the NCBI BLAST portal.
- Full pipeline: simulation/modelling [NAMD v2.0] -> stage not stated [AlphaFold v2.3.2, BLAST, VMD v1.9.4a]

### The integral role of de novo lipogenesis in the preparation for seasonal dormancy. (PNAS 2024)

- DOI: 10.1073/pnas.2406194121 | PMCID: PMC11260141 | PMID: 38990942
- Evidence: The regions selected for dsRNA synthesis were checked for gene specificity using blastn ( www.blast.ncbi.nlm.nih.go ) against the CPB transcriptome (NCBI BioProject: PRJNA171749). dsRNAs were synthesized using the T7 RiboMAX™ kit (Promega) according to the manufacturer’s instructions (cDNA was obtained as described below from intact females; see SI Appendix , Table S1 for primers).
- Full pipeline: quantification [R] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [BLAST, emmeans]

### Beneficial metabolic effects of PAHSAs depend on the gut microbiota in diet-induced obese mice but not in chow-fed mice. (PNAS 2024)

- DOI: 10.1073/pnas.2318691121 | PMCID: PMC11252816 | PMID: 38968121
- Evidence: 1 D , operational taxonomic units (OTUs) were assigned to sequences above 300 bp with 97 to 99% identity after removal of singleton sequences clustering at 1% divergence and taxonomically classified using BLASTn against the NCBI reference genome database.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [FastQC, MultiQC] -> alignment/mapping [BLAST, HUMAnN, MetaPhlAn] -> quantification [HUMAnN, MetaPhlAn] -> dimensionality reduction/clustering [BLAST] -> stage not stated [DADA2]

### Principal role of fungi in soil carbon stabilization during early pedogenesis in the high Arctic. (PNAS 2024)

- DOI: 10.1073/pnas.2402689121 | PMCID: PMC11252988 | PMID: 38954550
- Evidence: This was determined to capture a realistic picture of fungal OTU richness using fungal mock communities ( 81 ).Operational taxonomic units were created using USEARCH (82) as described previously ( 80 , 81 ).The taxonomic affiliation of the 16S rRNA gene was made as described previously ( 80 ) using BLASTn searches of OTU sequences against the SILVA database ( 83 ).
- Full pipeline: differential/statistical testing [R v4.3.1] -> stage not stated [BLAST, QGIS v3.18]

### Transfection of entomopathogenic <i>Metarhizium</i> species with a mycovirus confers hypervirulence against two lepidopteran pests. (PNAS 2024)

- DOI: 10.1073/pnas.2320572121 | PMCID: PMC11214047 | PMID: 38885380
- Evidence: The assembled contigs were subsequently screened against the NCBI databases using BLASTn and BLASTx searches with default options.
- Full pipeline: read trimming [fastp] -> alignment/mapping [ggplot2] -> quantification [ggplot2] -> dimensionality reduction/clustering [clusterProfiler, ggplot2] -> stage not stated [BLAST, DESeq2, R, pheatmap]

### Widespread detoxifying NO reductases impart a distinct isotopic fingerprint on N<sub>2</sub>O under anoxia. (PNAS 2024)

- DOI: 10.1073/pnas.2319960121 | PMCID: PMC11194513 | PMID: 38865268
- Evidence: Default NCBI protein BLAST blastp parameters were used to identify Fhp orthologs.
- Full pipeline: stage not stated [BLAST]

### Duplication and neofunctionalization of a horizontally transferred xyloglucanase as a facet of the Red Queen coevolutionary dynamic. (PNAS 2024)

- DOI: 10.1073/pnas.2218927121 | PMCID: PMC11181080 | PMID: 38830094
- Evidence: GH12 protein homologs were identified from a selection of eukaryotic (with sampling subsequently focusing on oomycetes and fungi) and prokaryotic genomes using BLASTp ( 71 ); from these hits, a multiple sequence protein alignment was constructed and aligned using automated methods in Seaview ( 72 ) using MUSCLE ( 73 ), which was then edited and masked manually.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Clustal Omega] -> stage not stated [R v4.0.3]

### Misregulation of bromotyrosine compromises fertility in male <i>Drosophila</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2322501121 | PMCID: PMC11126969 | PMID: 38748578
- Evidence: Searches using HMMsearch and blastp did not uncover homologs of halogenases involving flavin adenine dinucleotide, non-heme iron/α-ketoglutarate, vanadium, or manganese.
- Full pipeline: stage not stated [BLAST, ImageJ]

### Frequent nonhomologous replacement of replicative helicase loaders by viruses in <i>Vibrionaceae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2317954121 | PMCID: PMC11087808 | PMID: 38683976
- Evidence: All-verses-all protein BLASTp comparisons were performed using BLAST+ to calculate sequence similarity between genes in different species ( 75 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.212] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, eggNOG]

### Carbon starvation raises capacities in bacterial antibiotic resistance and viral auxiliary carbon metabolism in soils. (PNAS 2024)

- DOI: 10.1073/pnas.2318160121 | PMCID: PMC11032446 | PMID: 38598339
- Version used: **2.5.0**
- Evidence: The blastn v2.5.0 + (coverage = 100, identity = 100), tRNAScan-SE v1.23, and CRISPRCasFinder were used to align sequences, identify tRNAs, and search for CRISPR spacers, respectively.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [BLAST v2.5.0] -> stage not stated [HMMER]

### Intergenerational protective anti-gut commensal immunoglobulin G originates in early life. (PNAS 2024)

- DOI: 10.1073/pnas.2309994121 | PMCID: PMC10990157 | PMID: 38517976
- Evidence: BLASTn of the splenic isolates and IgG + sorted bacteria 16SrRNA matched both S. xylosus and S. saprophyticus.
- Full pipeline: read trimming [Bowtie2 v2.4.1, MAFFT v7.475] -> alignment/mapping [Bowtie2 v2.4.1, MAFFT v7.475] -> dimensionality reduction/clustering [Docker] -> visualisation [R v4.0, phyloseq] -> stage not stated [BLAST, RAxML]

### A diterpene synthase from the sandfly <i>Lutzomyia longipalpis</i> produces the pheromone sobralene. (PNAS 2024)

- DOI: 10.1073/pnas.2322453121 | PMCID: PMC10962984 | PMID: 38470919
- Evidence: FPPS-like homologues were identified from the L . longipalpis genome (Jacobina, NCBI accession PRJNA20279) using blastp searches with TPS enzymes from P. striolata as the query.
- Full pipeline: stage not stated [BLAST]

### Rapid dissemination of host metabolism-manipulating genes via integrative and conjugative elements. (PNAS 2024)

- DOI: 10.1073/pnas.2309263121 | PMCID: PMC10945833 | PMID: 38457521
- Evidence: A broad family of P. syringae ICEs (PsICEs) was identified using BLASTn searches of a collection of sequenced Psa genomes, combined with genomes deposited in the NCBI Genbank and WGS databases (updated to July 2021 and November 2017, respectively) ( 20 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, R]

### Endogenous virophages are active and mitigate giant virus infection in the marine protist <i>Cafeteria burkhardae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2314606121 | PMCID: PMC10945749 | PMID: 38446847
- Evidence: Coding DNA sequences were predicted using GeneMarkS ( 48 ), and functional annotation was carried out using BLASTp ( 49 ) searches against the nonredundant protein collection of the NCBI with manual curation to produce high-quality annotation files.
- Full pipeline: alignment/mapping [minimap2 v2.22] -> stage not stated [BLAST, Flye v2.9.1, SAMtools]

### Short macrocyclic peptides in sponge genomes. (PNAS 2024)

- DOI: 10.1073/pnas.2314383121 | PMCID: PMC10945851 | PMID: 38442178
- Evidence: Query sequences were searched using the blastp algorithm against the SRA assembly database, with an e-value threshold of 1e-10.
- Full pipeline: machine learning [AUGUSTUS v3.3] -> stage not stated [BLAST, Flye]

### Pyrenoid proteomics reveals independent evolution of the CO<sub>2</sub>-concentrating organelle in chlorarachniophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2318542121 | PMCID: PMC10927497 | PMID: 38408230
- Evidence: Functional annotation of the pyrenoid-associated proteins was conducted based on BLASTp searches against the non-redundant protein sequences in the NCBI database.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0]

### Genomes, fossils, and the concurrent rise of modern birds and flowering plants in the Late Cretaceous. (PNAS 2024)

- DOI: 10.1073/pnas.2319696121 | PMCID: PMC10895254 | PMID: 38346181
- Evidence: To identify orthologs of intergenic markers across species, we performed blastn searches using the intergenic segments obtained from the chicken against the genomes of the remaining 124 species with an E-value cutoff of 1e−10.
- Full pipeline: stage not stated [BLAST, OrthoFinder v2.3.12, R, RAxML]

### Isolation, characterization, and circulation sphere of a filovirus in fruit bats. (PNAS 2024)

- DOI: 10.1073/pnas.2313789121 | PMCID: PMC10873641 | PMID: 38335257
- Version used: **0.9.35**
- Evidence: Derived amino acid sequences of ≥50 aa were queried against the Eukaryotic Viral Reference Database (EVRD)-aa version 1.0 ( 46 ) using DIAMOND blastp version 0.9.35 with e-value cutoff 1e−5.
- Full pipeline: quality control [SPAdes, fastp v0.20.0] -> alignment/mapping [Bowtie2 v2.4.1, SAMtools v1.10] -> quantification [ImageJ] -> visualisation [ImageJ, PyMOL v2.4.0] -> stage not stated [BLAST v0.9.35]

### Virus-derived circular RNAs populate hepatitis C virus-infected cells. (PNAS 2024)

- DOI: 10.1073/pnas.2313002121 | PMCID: PMC10873615 | PMID: 38319965
- Evidence: An expectation value cutoff of 10 -5 was used in the blastn ( 35 ).
- Full pipeline: stage not stated [BLAST]

### Flexible B&lt;sub&gt;12&lt;/sub&gt; ecophysiology of &lt;i&gt;Phaeocystis antarctica&lt;/i&gt; due to a fusion B&lt;sub&gt;12&lt;/sub&gt;-independent methionine synthase with widespread homologues. (PNAS 2024)

- DOI: 10.1073/pnas.2204075121 | PMCID: PMC10861871 | PMID: 38306482
- Evidence: A BLASTp alignment confirmed that these two contigs mapped directly to a single contig in the transcriptomic assembly of P. antarctica CCMP1374 and in a Ross Sea metatranscriptome ( 24 ).
- Full pipeline: alignment/mapping [BLAST] -> stage not stated [InterProScan]

### In vivo functional phenotypes from a computational epistatic model of evolution. (PNAS 2024)

- DOI: 10.1073/pnas.2308895121 | PMCID: PMC10861889 | PMID: 38285950
- Evidence: When these late variants were queried on BLASTp ( 38 ), the top hits were to the Pseudomonas aeruginosa TEM-136 that has 33 different point mutations from Late_mf_3_NT and a Citrobacter freundii class A β -lactamase that has 48 different point mutations from Late_bm_3_NT.
- Full pipeline: stage not stated [BLAST]

### The structure of B-ARR reveals the molecular basis of transcriptional activation by cytokinin. (PNAS 2024)

- DOI: 10.1073/pnas.2319335121 | PMCID: PMC10801921 | PMID: 38198526
- Evidence: BLASTp was performed using the deduced amino acid sequence from ARRs from different species.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [BLAST]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Evidence: This set of computationally generated, putative psilocybin BGCs was then manually curated by querying the top three hits against the Psi gene sequences from the chromosomal assembly of P. cubensis using BLASTn to measure their similarities.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### Contingency, repeatability, and predictability in the evolution of a prokaryotic pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2304934120 | PMCID: PMC10769857 | PMID: 38147560
- Evidence: Therefore, using BLASTn ( 45 , 46 ), we subjected the sequences of each gene family involved in any apparent avoidance relationship to a comparison with the gene family they avoid.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [BLAST, R, scikit-learn]

### Combination of Cas9 and adeno-associated vectors enables efficient in vivo knockdown of precise miRNAs in the rodent and primate brain. (PNAS 2025)

- DOI: 10.1073/pnas.2513076122 | PMCID: PMC12718335 | PMID: 41359835
- Evidence: Each sequence from each of these demultiplexed preMir sequence files were aligned (pairwise alignment) to their corresponding reference sequence using blastn ( 84 ).
- Full pipeline: read trimming [BLAST, Cutadapt] -> alignment/mapping [BLAST, DESeq2 v1.44.0] -> quantification [ImageJ] -> differential/statistical testing [DESeq2 v1.44.0, R]

### Microbial necromass carbon enhances arsenic methylation in paddy soils. (PNAS 2025)

- DOI: 10.1073/pnas.2527462122 | PMCID: PMC12685052 | PMID: 41289391
- Evidence: Short-read sequences of the arsM , arrA , arsC1 , and arsC2 and mcrA genes were annotated by DIAMOND BLASTx ( 40 ) (with the option “--sensitive”) against the ROCker ( 41 , 42 , 43 ) database and McycDB.
- Full pipeline: differential/statistical testing [DESeq2 v1.44.0] -> stage not stated [BLAST, R v4.2, RAxML]

### A binary-distributed effector modulates fungal host preference for drosophilids by targeting a lineage-specific immune factor. (PNAS 2025)

- DOI: 10.1073/pnas.2518127122 | PMCID: PMC12646311 | PMID: 41231943
- Evidence: BLASTp analysis revealed that Bhe1 homolog is patchily distributed in other insect- or plant-pathogenic fungi, such as the presence in B. asiatica ( KAK8150687 ; 127 aa, 96% identity at the amino acid level) and M. robertsii (MAA_10575; 107 aa, 76% identity; termed mBhe1 ).
- Full pipeline: stage not stated [BLAST]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Evidence: Annotation was performed using the Trinotate ( 93 ) pipeline, and relied on blastx and blastp, KEGG, GO, and Pfam ( Dataset S2 ).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### Homology-mediated transformation of frog-killing fungus &lt;i&gt;Batrachochytrium dendrobatidis&lt;/i&gt; illuminates chytrid development and pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507572122 | PMCID: PMC12595416 | PMID: 41150711
- Evidence: Integration sites were validated using blastn searches against raw HiFi reads, applying an e-value threshold of 0.0001 and sequence identity >90%.
- Full pipeline: alignment/mapping [SAMtools v1.14, minimap2 v2.28] -> stage not stated [BLAST, BUSCO v5.2.2, QUAST v5.0.0, R v4.0.2]

### Symbiotic solutions for colony nutrition: Conserved nitrogen recycling within the bacterial pouch of &lt;i&gt;Tetraponera&lt;/i&gt; ants. (PNAS 2025)

- DOI: 10.1073/pnas.2514882122 | PMCID: PMC12595465 | PMID: 41150726
- Evidence: Scaffolds with unexpected taxonomic classifications or inconsistent coverage were manually removed following comparison with the NCBI database using BLASTn and BLASTx ( Dataset S6 ).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic] -> read trimming [FastQC v0.11.9, Trimmomatic] -> differential/statistical testing [QUAST] -> stage not stated [BLAST, Flye v2.9, RAxML v8.2.12]

### Jumbo phage-mediated transduction of genomic islands. (PNAS 2025)

- DOI: 10.1073/pnas.2512465122 | PMCID: PMC12595487 | PMID: 41150720
- Evidence: Alignment of the 3 foreign elements was done by Easyfig ( 37 ) based on blastn under the default settings.
- Full pipeline: alignment/mapping [BLAST] -> dimensionality reduction/clustering [R v4.1.2] -> stage not stated [InterProScan, Prokka, eggNOG]

### Parallel shifts in differential gene expression reveal convergent miniaturization in fishes. (PNAS 2025)

- DOI: 10.1073/pnas.2512299122 | PMCID: PMC12582303 | PMID: 41123994
- Evidence: Pairwise query-database protein BLAST searches were then run with blastp using the options “outfmt 6 -evalue 0.001” ( 88 ).
- Full pipeline: quality control [FastQC v0.11.5, HISAT2 v2.0.5] -> read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HISAT2 v2.0.5] -> normalisation [R, pheatmap] -> dimensionality reduction/clustering [R, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, R, pheatmap] -> structure determination [phytools] -> visualisation [R, pheatmap] -> stage not stated [BLAST, BUSCO v5.2.2, OrthoFinder v2.5.4, RAxML v1.1.0, Salmon v1.10.1]

### Apusomonad rhodopsins: A new family of ultraviolet to blue light-absorbing rhodopsin channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510619122 | PMCID: PMC12557545 | PMID: 41082663
- Evidence: To study the presence or absence of microbial rhodopsins in apusomonads blastp, tblastn ( 81 ), and custom HMM profiles ( 82 ) searches were performed against all available proteomes of apusomonads ( 43 , 83 , 85 , 86 ).
- Full pipeline: read trimming [IQ-TREE v1.6.11, MAFFT] -> alignment/mapping [IQ-TREE v1.6.11, MAFFT] -> differential/statistical testing [IQ-TREE v1.6.11] -> structure determination [IQ-TREE v1.6.11] -> stage not stated [AlphaFold, BLAST, GROMACS v4.5.7]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Version used: **2.13.0**
- Evidence: ...eqKit v2.2.0 ) appeared in the middle of the protein sequence; and 3) no matches or percentage of identical matches (pident) < 90 occurred when using BLASTp v2.13.0 + to filter sequences.
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### A nonenzymatic effector disrupts &lt;i&gt;Bacteroides&lt;/i&gt; cell wall homeostasis via OmpA targeting to mediate interbacterial competition. (PNAS 2025)

- DOI: 10.1073/pnas.2513207122 | PMCID: PMC12541434 | PMID: 41055976
- Evidence: A conservation analysis was constructed based on BF9343_3708 and BF9343_3708 286-end , the sequence was used in blastp against the nonredundant (nr) protein database from the National Center for Biotechnology Information (NCBI) including in the Bacteroides database, and 2 to 5 homologous sequences in different strains were chosen with a cutoff identity 60% and aligned using MAFFT (Version 7.487).
- Full pipeline: alignment/mapping [AlphaFold, BLAST, MAFFT] -> structure determination [AlphaFold] -> stage not stated [IQ-TREE]

### Combined pesticide pollution enhances the dissemination of the phage-encoded antibiotic resistome in the soil under nitrogen deposition. (PNAS 2025)

- DOI: 10.1073/pnas.2516722122 | PMCID: PMC12519213 | PMID: 41042849
- Evidence: ARGs within vOTUs were annotated by aligning sequences against the SARG (v3.2) database using BLASTp, with thresholds of e-value ≤10 −5 , query coverage ≥80%, and amino acid identity ≥60%.
- Full pipeline: read trimming [fastp v0.22.08] -> alignment/mapping [BLAST] -> visualisation [Cytoscape v3.10.0] -> stage not stated [HMMER v3.1b, R v4.0.3, eggNOG, vegan]

### Duplication of a conserved mitochondrial enzyme gene arms parasitoid wasps with venom cytotoxicity and oogenesis regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512820122 | PMCID: PMC12501140 | PMID: 40996803
- Evidence: All candidate genes were manually confirmed in NCBI by blastp according to the domains with the HMMER suite ( https://www.ebi.ac.uk/Tools/hmmer/ ) of Pfam ( 59 ).
- Full pipeline: quality control [fastp] -> alignment/mapping [MAFFT] -> quantification [fastp] -> structure determination [phytools] -> stage not stated [AlphaFold, BLAST, HMMER]

### Genetic dissection of nonconventional introns reveals codominant noncanonical splicing code in &lt;i&gt;Euglena&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509937122 | PMCID: PMC12501133 | PMID: 40986342
- Evidence: Open reading frames were predicted using TransDecoder-v3.0.0 ( https://transdecoder.github.io ) with the parameters: “--retain_pfam_hits, --retain_blastp_hits, and --single_best_orf”, after searches against the Pfam-A (release 30.0) dataset using HMMER-v3.1b2 and the NCBI nonredundant (nr) protein datasets using BLASTP-v2.2.30 with the parameter: “-evalue 1e−5.” Base-Pairing Sequence Prediction.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HISAT2, StringTie] -> stage not stated [BLAST, HMMER, ImageJ]

### Language models reveal a complex sequence basis for adaptive convergent evolution of protein functions. (PNAS 2025)

- DOI: 10.1073/pnas.2418254122 | PMCID: PMC12501123 | PMID: 40986350
- Evidence: The BLOSUM62 scores were calculated as in the default blastp ( 82 ) raw score calculation based on BLOSUM62 matrix, with −11 for gap opening and −1 for gap extension.
- Full pipeline: alignment/mapping [MAFFT v7.505] -> differential/statistical testing [IQ-TREE v2.2.5] -> structure determination [IQ-TREE v2.2.5] -> stage not stated [BLAST, OrthoFinder v2.5.5, R]

### The balance between microbial arsenic methylation and demethylation in paddy soils underpins global arsenic risk and straighthead disease in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2508311122 | PMCID: PMC12478174 | PMID: 40966281
- Evidence: These ORFs were compared against two specialized databases: an ArsM database ( 31 ) and the McycDB database ( 69 ) using BLASTp ( 70 ).
- Full pipeline: quality control [fastp] -> differential/statistical testing [pheatmap] -> visualisation [pheatmap] -> stage not stated [BLAST]

### DNA-utilization loci enable exogenous DNA metabolism in gut Bacteroidales. (PNAS 2025)

- DOI: 10.1073/pnas.2505388122 | PMCID: PMC12478041 | PMID: 40956896
- Evidence: ...ron (Bt1: WP_008762511.1 , Bt2: WP_055220680.1 ) and P. vulgatus (Pv1: WP_005843284.1 , Pv2: WP_117829583.1 ) were used as queries ( Dataset S4 ) for BLASTp searches against a database comprising the proteomes of 9,910 Bacteroidota genomes with unambiguous genus and species designations downloaded from NCBI ( Dataset S5 ).
- Full pipeline: read trimming [R v4.0.3] -> alignment/mapping [PyMOL] -> visualisation [ImageJ] -> stage not stated [AlphaFold, BLAST]

### Convergent evolution of &lt;i&gt;NFP&lt;/i&gt;-facilitated root nodule symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2424902122 | PMCID: PMC12452920 | PMID: 40924454
- Evidence: We used a custom script that retrieved the top hit for each locus identified using BLASTp ( 56 ) and retrieved the top hit from the genome sequence using BEDTools ( 57 ).
- Full pipeline: stage not stated [BEDTools, BLAST, MAFFT, RAxML]

### A genome-scale drug discovery pipeline uncovers therapeutic targets and a unique p97 allosteric binding site in &lt;i&gt;Schistosoma mansoni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505710122 | PMCID: PMC12415213 | PMID: 40880532
- Evidence: Identifiers (Ensembl and Uniprot) ( 99 , 100 ) were used in combination with BLASTp ( 29 – 31 ) to establish schistosome genes with similarity to these drug targets (Schistosome proteome: PRJEA36577) (Human Proteome: Homo_sapiens.GRCh38).
- Full pipeline: stage not stated [AlphaFold, BLAST]

### Nano-biochar regulates phage-host interactions, reducing antibiotic resistance genes in vermicomposting systems. (PNAS 2025)

- DOI: 10.1073/pnas.2511986122 | PMCID: PMC12403132 | PMID: 40838886
- Evidence: BLASTn was utilized to query for exact sequence matches between CRISPR spacer regions and phage overlapping clusters, and genes with thresholds > 95% identity and < 1 mismatch were selected as highly reliable phage hosts ( 57 ).
- Full pipeline: read trimming [QUAST] -> dimensionality reduction/clustering [BLAST] -> stage not stated [IQ-TREE, R, eggNOG]

### Protein functional site annotation using local structure embeddings. (PNAS 2025)

- DOI: 10.1073/pnas.2513219122 | PMCID: PMC12403137 | PMID: 40833413
- Evidence: For BLASTp comparisons, we search each validation and test protein against the reference database using default settings and an e-value cutoff of 0.01.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [AlphaFold, BLAST]

### Soil eDNA reflects regionally dominant species rather than local composition of tropical tree communities. (PNAS 2025)

- DOI: 10.1073/pnas.2505772122 | PMCID: PMC12403143 | PMID: 40828011
- Evidence: Sequence data were demultiplexed to intrasample PCR replicates and adaptors/primers trimmed ( 43 , 44 ), denoised with DADA2 ( 41 ), ASV tables curated with LULU ( 45 ) and soil sequences were mapped to LFDP reference library sequences at 100% match in DADA2, then finally a BLASTn search and the MEGAN lowest common ancestor algorithm ( 46 ) used to taxonomically annotate the remaining sequences.
- Full pipeline: read trimming [BLAST, DADA2] -> alignment/mapping [BLAST, DADA2] -> stage not stated [R, vegan]

### CRISPR-Cas9 screening reveals microproteins regulating adipocyte proliferation and lipid metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2506534122 | PMCID: PMC12358916 | PMID: 40773238
- Evidence: Here, we define an “unannotated smORF” as a smORF absent from GenBank and UniProt databases, identified by filtering against mouse reference protein sequences using BLASTp.
- Full pipeline: alignment/mapping [STAR] -> stage not stated [BLAST, RepeatMasker]

### Evolutionarily divergent nidovirus with an exceptionally large genome identified in Pacific oysters undergoing mass mortality. (PNAS 2025)

- DOI: 10.1073/pnas.2426923122 | PMCID: PMC12377751 | PMID: 40758866
- Evidence: To retrieve segment 2 of Megarnavirus gigas viruses, the genomic sequence of PONV1 segment 2 was used as a query in a BLASTn search ( p < 1e-5) against all nonredundant contigs de novo assembled from each metatranscriptome.
- Full pipeline: read trimming [MAFFT, SPAdes v3.15.2, Trimmomatic v0.38] -> alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2.1] -> structure determination [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0.3, InterProScan v5.59]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Version used: **2.11.0**
- Evidence: Known miRNA families were annotated by aligning representative reads of miRNA loci (both miRNA and miRNA*) to monocot-derived miRNAs from miRBase release 22.1 ( 39 , 40 ) using ncbi-blastn v2.11.0+ ( 41 ) with parameters: -strand both -task blastn-short -perc_identity 85 -word_size 7 -evalue 0.01 -num_alignments 1 -no_greedy -ungapped.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### Mutualism between degraders and nondegraders stabilizes the function of a natural biopolymer-degrading community. (PNAS 2025)

- DOI: 10.1073/pnas.2500664122 | PMCID: PMC12318217 | PMID: 40690677
- Evidence: PCR products were sequenced in Beijing Genomics Institute and the acquired sequences were aligned using NCBI BLAST.
- Full pipeline: alignment/mapping [BLAST]

### Unveiling organ-specific metabolism of &lt;i&gt;Citrus clementina&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2503406122 | PMCID: PMC12305039 | PMID: 40668834
- Evidence: The first draft metabolic model was reconstructed using The COBRA ( 27 , 28 ) and The RAVEN ( 26 ) Toolboxes complemented with semiautomated metabolic reconstruction algorithms to optimize the BLASTp cutoff values.
- Full pipeline: normalisation [scikit-learn] -> structure determination [BLAST]

### Ciprofloxacin-driven purifying selection on viral genomes accelerates soil N&lt;sub&gt;2&lt;/sub&gt;O production. (PNAS 2025)

- DOI: 10.1073/pnas.2503199122 | PMCID: PMC12304974 | PMID: 40668828
- Version used: **2.12.0**
- Evidence: Three computational predicting approaches were applied to link each virus to putative hosts: i) CRISPR matching—CRISPR spacers of viral contigs identified by CRISPR Recognition Tool (CRT, v2.1) were matched against microbial scaffolds using BLASTn v2.12.0, satisfying the thresholds of ≥95% identity and ≤2 single nucleotide polymorphisms ( 83 ). ii) tRNA matching—tRNA genes within viral contigs wer...
- Full pipeline: read trimming [fastp] -> visualisation [Cytoscape v3.7.2] -> stage not stated [BLAST v2.12.0, R v4.3.1, eggNOG, ggplot2, pheatmap]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Evidence: Conserved Receptor Structure and Response to Cholinergic Modulators in Cassiopea Protein sequence analysis with BLASTp indicated Cassiopea chrnal-E as having high similarity to Chrna7, 9, and 10-like belonging to other cnidarian species (e.g., Rhopilema esculentum, Clytia hemisphaerica, Hydractinia symbiolongicarpus ) across multiple classes.
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Arylsulfamates inhibit colonic Bacteroidota growth through a sulfatase-independent mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2414331122 | PMCID: PMC12280919 | PMID: 40638084
- Evidence: BLASTp using BT4322 against the nine other arylsulfamate-sensitive Bacteroides bacteria returned a single orthologue from each species, with 100% query coverage, and a minimum of 84% identity suggesting a conserved role for these proteins across these organisms ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, BLAST]

### Decoding and engineering temperature-sensitive lethality in &lt;i&gt;Ceratitis capitata&lt;/i&gt; for pest control. (PNAS 2025)

- DOI: 10.1073/pnas.2503604122 | PMCID: PMC12280921 | PMID: 40623181
- Version used: **2.13.0**
- Evidence: The coding sequence of each FUN-annotated gene with nonsynonymous mutations was used to screen the NCBI nr database using blastn v2.13.0 + (organism: C. capitata ) ( 54 ) to retrieve the accession numbers and sequences of the genes and proteins in the NCBI reference genome Ccap_2.1 (GCA_000347755.4; Annotation release 103) ( 55 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BLAST v2.13.0, Bowtie2]

### An endosymbiotic origin of the crimson pigment from the lac insect. (PNAS 2025)

- DOI: 10.1073/pnas.2501623122 | PMCID: PMC12207437 | PMID: 40523179
- Evidence: Twenty-four of the 30 cloned fungal 28 S rRNA gene sequences amplified from surface-sterilized ovaries were identified as belonging to the order Hypocreales, with a 92 to 93% sequence identity with the entomopathogenic Ophiocordyceps fungus (BLASTn analysis, SI Appendix , Tables S1 and S2 ).
- Full pipeline: stage not stated [BLAST, BUSCO, IQ-TREE, InterProScan]

### Biparental inheritance of germline-specific chromosomes in the sea lamprey and their roles in oocytes. (PNAS 2025)

- DOI: 10.1073/pnas.2421883122 | PMCID: PMC12184396 | PMID: 40504158
- Evidence: For homolog annotation we used DIAMOND v.0.9.24 ( 56 ) blastp with options --more-sensitive, --max-target-seqs 1 to align annotated protein sequences to canonical proteome sets of several species: human ( Homo sapiens ), chicken ( Gallus gallus ), mouse ( Mus musculus ), spotted gar ( Lepisosteus oculatus ), lancelet ( Branchiostoma floridae ), and tunicate ( Ciona intestinalis ) provided by the R...
- Full pipeline: alignment/mapping [BEDTools v2.30.0, BLAST, DIAMOND, HISAT2 v2.2.1, SAMtools v1.14, minimap2 v2.26] -> normalisation [R] -> differential/statistical testing [R] -> stage not stated [Enrichr, OrthoFinder v2.5.4, Trinity v2.13.2]

### &lt;i&gt;Hamiltonella&lt;/i&gt; symbionts benefit whitefly fertilization by regulating the maternal protein Tudor-mediated piRNA pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2427053122 | PMCID: PMC12184435 | PMID: 40504144
- Evidence: Specifically, the blastn software was employed to map piRNA sequences against the whitefly genome ( 53 ).
- Full pipeline: differential/statistical testing [edgeR] -> visualisation [PyMOL v3.1.0] -> stage not stated [AlphaFold, BLAST, ImageJ]

### The great phage escape: Activating and escaping lactococcal antiphage systems. (PNAS 2025)

- DOI: 10.1073/pnas.2426508122 | PMCID: PMC12184496 | PMID: 40498451
- Evidence: O pen r eading f rames (ORFs) were predicted using a combination of Prodigal version 2.6 and BLASTx ( 40 , 41 ), followed by manual assessment, curation, and correction of predicted ORFs.
- Full pipeline: stage not stated [AlphaFold v2.3.1, BLAST, ChimeraX, InterProScan]

### Rhomboid-mediated cleavage of the immune receptor XA21 protects grain set and male fertility in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2502025122 | PMCID: PMC12146745 | PMID: 40445755
- Evidence: OsRBL3b homologs were identified through BLASTp.
- Full pipeline: quantification [ImageJ] -> stage not stated [BLAST, IQ-TREE]

### Independent transitions to fully planktonic life cycles shaped the global distribution of medusozoans in the epipelagic zone. (PNAS 2025)

- DOI: 10.1073/pnas.2415979122 | PMCID: PMC12146771 | PMID: 40440075
- Evidence: The representative sequence of each OTU was aligned by BLASTn against the PR2_V9 database enriched in a nonredundant manner with Opisthokonta 18S sequences (with a length between 100 and 10,000 pb) extracted from the nucleotide database of NCBI.
- Full pipeline: alignment/mapping [BLAST, phytools] -> differential/statistical testing [tidyverse, vegan] -> stage not stated [R, igraph]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Evidence: BLASTp (Basic Local Alignment Search Tool protein) searches were performed to screen for the presence or absence of homologous MN1 amino acid sequences in NCBI ( https://www.ncbi.nlm.nih.gov/ ) and Ensembl ( https://www.ensembl.org/index.html ) using the human MN1 sequence ( NP_002421.3 ) as a query.
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### Horizontal transmission of functionally diverse transposons is a major source of new introns. (PNAS 2025)

- DOI: 10.1073/pnas.2414761122 | PMCID: PMC12130899 | PMID: 40402243
- Evidence: To search for possible HGT of introners, we performed blastn searches ( 65 ) for each introner consensus sequence against the NCBI nucleotide and RefSeq reference genome databases ( 87 ) (accessed 05/15/2024).
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> normalisation [TreeTime] -> structure determination [RepeatMasker]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Evidence: To gain insights into the root-to-shoot signal of AoDev, a comprehensive reannotation of CLE prepropeptides in L. albus was performed using the NCBI BLASTp tool and the M. truncatula genome, identifying 70 sequences that were categorized into the seven previously established CLE groups ( 29 , 30 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### RNA sequencing analysis of viromes of &lt;i&gt;Aedes albopictus&lt;/i&gt; and &lt;i&gt;Aedes vexans&lt;/i&gt; collected from NEON sites. (PNAS 2025)

- DOI: 10.1073/pnas.2403591122 | PMCID: PMC12107137 | PMID: 40354533
- Evidence: For quality assurance, reference genomes present in RVDB were aligned against the National Center for Biotechnology Information (NCBI) Nucleotide Collection database (nr/nt) (version 5 accessed 31 January 2022) using the “blastn” function from the Basic Local Alignment Search Tool (BLAST+ v.2.15.0).
- Full pipeline: read trimming [BWA, fastp v0.21.1] -> alignment/mapping [BLAST, BWA, Kraken2, SAMtools] -> stage not stated [Bowtie2, R]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Evidence: To investigate the evolutionary origin of the BHIKHARI superfamily, we identified related endogenous lokiretroviral sequences in the RepBase v28.08 library of consensus TE sequences ( 60 ) using blastn with the consensus sequences for internal regions of Bik-1-5 ( 61 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Fungal Argonaute proteins act in bidirectional cross-kingdom RNA interference during plant infection. (PNAS 2025)

- DOI: 10.1073/pnas.2422756122 | PMCID: PMC12054834 | PMID: 40267130
- Evidence: We performed a BLASTp search using the full-length protein sequence of the well-characterized N. crassa QDE2 as a query in the genome sequence of the B. cinerea strain B05.10 ( 31 ) to identify BcAGOs.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST]

### A diverse single-stranded DNA-annealing protein library enables efficient genome editing across bacterial phyla. (PNAS 2025)

- DOI: 10.1073/pnas.2414342122 | PMCID: PMC12054835 | PMID: 40258142
- Evidence: To establish dsDNA recombineering in S. aureus and C. glutamicum , we first identified the prophage genome from which the winning phage-derived SSAPs were sourced with BLASTp, then analyzed the operon containing the SSAP.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, Python]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: To identify vitellogenin ( Vg ) and its receptor ( VgR ) genes, we utilized Bitacora v1.4 ( 94 ) in combination with homology-based tools (NCBI BLAST, HMMER, and GEMOMA) ( 95 – 97 ), manually validated candidate genes, and classified them into Vg , partial Vg ( PVg ), or Vg -like ( Vgl ) subgroups.
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### Evolutionary divergent kinetoplast genome structure and RNA editing patterns in the trypanosomatid &lt;i&gt;Vickermania&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426887122 | PMCID: PMC12012515 | PMID: 40203041
- Evidence: The presence of cryptogenes ND7 , A6 , and MURF2 , which contain much shorter blocks of G-rich sequences and require only limited editing to produce translatable mRNAs, was verified by BLASTn search using Leptomonas pyrrhocoris query sequences ( 29 ).
- Full pipeline: stage not stated [BLAST]

### Host ZAP activity correlates with the levels of CpG suppression in primate lentiviruses. (PNAS 2025)

- DOI: 10.1073/pnas.2419489122 | PMCID: PMC12012506 | PMID: 40178887
- Evidence: Human ZAP (genomic sequence from hg38 assembly (chr7:139,043,515-139,109,720) available at the UCSC genome browser; https://genome.ucsc.edu/ ) was used as a bait for the BLASTn searches.
- Full pipeline: stage not stated [BLAST]

### Polymorphic transposable elements contribute to variation in recombination landscapes. (PNAS 2025)

- DOI: 10.1073/pnas.2427312122 | PMCID: PMC11962413 | PMID: 40100633
- Evidence: To annotate TEs, we ran Repeatmodeler2 [version 2.0.3; ( 49 )] and used blastn ( 78 ) to assign candidate TEs to the family level.
- Full pipeline: dimensionality reduction/clustering [minimap2 v2.24] -> stage not stated [BLAST]

### Diel partitioning in microbial phosphorus acquisition in the Sargasso Sea. (PNAS 2025)

- DOI: 10.1073/pnas.2410268122 | PMCID: PMC11929403 | PMID: 40085655
- Evidence: The ORF protein sequences were annotated using eggNOG-mapper v2.1.4 [with DIAMOND blastp alignment ( 44 )] for functional annotation, and aligned to the PhyloDB database ( https://github.com/allenlab/PhyloDB ) using the software package EUKulele ( 45 ) for taxonomic annotation.
- Full pipeline: read trimming [featureCounts] -> alignment/mapping [BLAST, eggNOG, featureCounts] -> stage not stated [DESeq2]

### Characterization of diverse Cas9 orthologs for genome and epigenome editing. (PNAS 2025)

- DOI: 10.1073/pnas.2417674122 | PMCID: PMC11929499 | PMID: 40073054
- Evidence: To determine spacer identity, all spacer sequences for the genera Lactobacillus , Pediococcus , and Streptococcus were compared against NCBI’s Nucleotide Collection database (nt) via nucleotide BLAST ( 54 ) using default parameters with the following exceptions: -e-value 1e-3, -task blastn-short, -dust no.
- Full pipeline: alignment/mapping [AlphaFold, MUSCLE v3.8.425] -> stage not stated [BLAST, RAxML]

### Copy number variation contributes to parallel local adaptation in an invasive plant. (PNAS 2025)

- DOI: 10.1073/pnas.2413587122 | PMCID: PMC11912486 | PMID: 40030023
- Version used: **2.7.1**
- Evidence: We used McScanX v97e74f4 ( 106 ) to determine syntenic gene groups resulting from a self-alignment of protein sequences on haplotype 1 using blastp (-evalue 1e−10) in BLAST v2.7.1 ( 107 ).
- Full pipeline: alignment/mapping [BLAST v2.7.1, SAMtools v1.9, minimap2 v2.1.8] -> variant calling [BLAST v2.7.1, GATK, minimap2 v2.1.8] -> visualisation [minimap2 v2.1.8] -> stage not stated [ANGSD, R, RepeatMasker v4.1.1, VCFtools, emmeans v1.10.2, lme4]

### Genomic divergence across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2319389122 | PMCID: PMC11912424 | PMID: 40014554
- Evidence: Each reference coding sequence was searched against the query genome using the blastn function in BLAST+ (version 2.13.0) ( https://ncbiinsightsncbi.nlm.nih.gov/2022/03/29/blast-2-13-0/ ) applying the following parameters: max_target_seqs = 1, perc_identity = 80, evalue = 1e−50, ungapped = true, with the remaining parameters assigned to default settings.
- Full pipeline: stage not stated [BLAST, BUSCO, SAMtools v1.15.1]

### &lt;i&gt;Enterobacter hormaechei&lt;/i&gt; replaces virulence with carbapenem resistance via porin loss. (PNAS 2025)

- DOI: 10.1073/pnas.2414315122 | PMCID: PMC11874173 | PMID: 39977318
- Version used: **2.11.0**
- Evidence: For identifying porin-related genes in the assemblies downloaded from NCBI, we used a database of 27 nucleotide sequences ( Dataset S1 ) in a blastn v.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.10] -> stage not stated [BLAST v2.11.0, Medaka]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Evidence: The sequences of LHL4, PSBS1, LHCSR3.1, and ELIP1-9 were subjected to a blastp analysis using the online tool available at https://www.ncbi.nlm.nih.gov/ with a percent identity range of 35 to 100% and a query coverage range of 50 to 100%.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### The MutRS quorum-sensing system controls lantibiotic mutacin production in the human pathogen &lt;i&gt;Streptococcus mutans&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421164122 | PMCID: PMC11848300 | PMID: 39946531
- Evidence: Putative peptide pheromone-based QS regulators were identified using homology-guided Basic Local Alignment Search Tool (BLAST) tblastn or blastp searches ( 58 ) queried with previously characterized Rgg and ComR regulators.
- Full pipeline: alignment/mapping [BLAST]

### Uncovering the hidden RNA virus diversity in Lake Nam Co: Evolutionary insights from an extreme high-altitude environment. (PNAS 2025)

- DOI: 10.1073/pnas.2420162122 | PMCID: PMC11831205 | PMID: 39903107
- Evidence: RdRP sequences were identified through a combination of BLASTp ( 95 ), HMMER searches ( 96 ), and the deep learning algorithm Lucaprot ( 8 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [BLAST, HMMER] -> visualisation [UMAP]

### A pentatomomorpha-specific salivary protein activates plant immunity and is critical for insect feeding. (PNAS 2025)

- DOI: 10.1073/pnas.2425190122 | PMCID: PMC11804711 | PMID: 39888915
- Evidence: The Hemiptera phylogenetic tree and the BLASTn results revealed that RpSP1 homologs were extensively dispersed in Pentatomomorpha, which may demonstrate that RpSP1 first evolved as an attack protein to aid insects in feeding on plant sap at the beginning of Pentatomomorpha differentiation.
- Full pipeline: stage not stated [BLAST]

### Fungal evasion of &lt;i&gt;Drosophila&lt;/i&gt; immunity involves blocking the cathepsin-mediated cleavage maturation of the danger-sensing protease. (PNAS 2025)

- DOI: 10.1073/pnas.2419343122 | PMCID: PMC11760918 | PMID: 39819219
- Evidence: Besides Fkp1 and BbFkp1, our BLASTp analysis indicated that the orthologs of Fkp1 are also present in other EPF species and ascomycete plant and nematode pathogenic fungi based on the cutoff E-value ≤1e−20 and amino acid identify >40%.
- Full pipeline: stage not stated [BLAST, ImageJ v1.53]

### Trojan horse peptide conjugates remodel the activity spectrum of clinical antibiotics. (PNAS 2025)

- DOI: 10.1073/pnas.2319483121 | PMCID: PMC11725936 | PMID: 39739799
- Evidence: Notably the E. cloacae clinical isolate was assumed to encode YejA-like transporter with 75 to 80% sequence identity based on the BLASTp search of YejA against the sequenced E. cloacae strains.
- Full pipeline: stage not stated [BLAST]

### PsDMAP1/PsTIP60-regulated H4K16ac is required for ROS-dependent virulence adaptation of &lt;i&gt;Phytophthora sojae&lt;/i&gt; on host plants. (PNAS 2025)

- DOI: 10.1073/pnas.2413127122 | PMCID: PMC11725902 | PMID: 39793040
- Evidence: Utilizing the recently updated P. sojae genome database (v3.0), we identified one ortholog of Homo sapiens DMAP1 encoded in the P. sojae genome ( 39 ) by bidirectional blastp searches with an E-value cut-off of 10 −10 .
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, BLAST, PyMOL v2.6]

### Temperature and developmental stage govern intestinal susceptibility to human coronavirus 229E. (PNAS 2026)

- DOI: 10.1073/pnas.2600632123 | PMCID: PMC13320717 | PMID: 42341040
- Evidence: The HCoV-229E used in this study was genotyped using NCBI BLAST and was found to have 99.89% genomic sequence identity with HCoV-229E strain Seattle/USA/SC2872/2015 (GenBank ID: KY967357.1 ) ( 56 ).
- Full pipeline: variant calling [BLAST] -> differential/statistical testing [R v4.3.3]

### Atlantic to Pacific: Outbreak of bivalve transmissible neoplasia detected in hybridizing soft-shell clams and eDNA in Puget Sound. (PNAS 2026)

- DOI: 10.1073/pnas.2611852123 | PMCID: PMC13320677 | PMID: 42335235
- Evidence: Briefly, new primers were selected within the 200 bp downstream of insertion sites, excluding sites which had multiple blastn hits in the M. arenaria reference genome (GCF_026914265.1), and selecting only one locus per chromosome, starting with chromosome 1.
- Full pipeline: alignment/mapping [BLAST] -> stage not stated [tidyverse]

### Linear-time prediction of proteome-scale microbial protein interactions. (PNAS 2026)

- DOI: 10.1073/pnas.2610619123 | PMCID: PMC13291599 | PMID: 42308045
- Evidence: Interactions involving homologous pairs were filtered using BLASTp (e-value < 10 −5 ) as well as promiscuous hub proteins (defined as > 3 interactions).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [PyTorch] -> visualisation [UMAP] -> stage not stated [AlphaFold, BLAST, STRING db]

### Uncovering thousands of endosymbiont DNA transfer events within single cockroach genomes. (PNAS 2026)

- DOI: 10.1073/pnas.2604240123 | PMCID: PMC13291636 | PMID: 42296358
- Evidence: By mapping insert sequences to RNA contigs using BLASTn, we found that 91.42 to 94.96% of inserts showed no evidence of transcription (although RNA from all life stages and tissues was not assessed).
- Full pipeline: alignment/mapping [BLAST]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Evidence: In order to mine the newly assembled genome for the presence of mint biosynthetic genes specifically, we compiled a list of previously documented biosynthetic genes in peppermint and spearmint ( http://langelabtools.wsu.edu/mgr/pathways ) and used blast-2.16.0 to find homeologous genes in our reference genome, with the following criteria: blastn with an e-value cutoff of 1e-120.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Mycoviruses confer hypovirulence but enhance antifungal volatile organic compound production in a phytopathogenic fungus. (PNAS 2026)

- DOI: 10.1073/pnas.2526822123 | PMCID: PMC13080020 | PMID: 41941638
- Evidence: Viral contigs were identified after de novo assembly using CLC Genomics Workbench (v6.0.4) and subsequent NCBI BLAST analysis.
- Full pipeline: alignment/mapping [ChimeraX, MAFFT v7.0] -> normalisation [ComplexHeatmap] -> dimensionality reduction/clustering [ComplexHeatmap, HMMER v3.3.2] -> visualisation [ChimeraX, ComplexHeatmap, ImageJ] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.2.6]

### Archaeogenetic insights into the demographic history of Late Neanderthals. (PNAS 2026)

- DOI: 10.1073/pnas.2520565123 | PMCID: PMC13037871 | PMID: 41871253
- Evidence: Neanderthal and Denisovan mitochondrial genomes were collected using two complementary approaches: 1) NCBI BLAST searches and 2) manual curation from the literature.
- Full pipeline: stage not stated [BEAST v2.6.7, BLAST]

### Smooth-to-rough morphotype switching, a mechanism of phage resistance in &lt;i&gt;&lt;i&gt;Mycobacterium&lt;/i&gt; abscessus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2531197123 | PMCID: PMC12993973 | PMID: 41811441
- Evidence: Nucleotide BLAST (BLASTn) analysis revealed a query coverage of only 11% between ΦJabs and ΦJun14, confirming their classification as distinct phages ( SI Appendix , Fig.
- Full pipeline: read trimming [SPAdes] -> stage not stated [AlphaFold, BLAST]

### Early colonization before inundation consistent with northern glacial refugia in Southern Doggerland revealed by sedimentary ancient DNA. (PNAS 2026)

- DOI: 10.1073/pnas.2508402123 | PMCID: PMC12994208 | PMID: 41805578
- Evidence: An initial metagenomic BLASTn search version 2.6.0 ( 76 ) was undertaken using the tab output (specified using -outfmt “6 std staxids”) and otherwise default parameters of the Nucleotide (NCBI) database.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [FastQC v0.11.6] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BLAST]

### Plant-fungi interactions in &lt;i&gt;Marchantia polymorpha&lt;/i&gt; are associated with horizontal gene transfer and terpene metabolism. (PNAS 2026)

- DOI: 10.1073/pnas.2532723123 | PMCID: PMC12890914 | PMID: 41637459
- Evidence: Phylogeny for the MTPSL genes (Mp6g04580, Mp6g04590, Mp6g04605, Mp6g04610, and Mp6g04630) and for the RLK GWAS candidate from chromosome 2 (Mp2g20720) was determined by BLASTp+ v2.12.0 ( 61 ) (maximum of 2,000 target sequences and E-value of 10 −5 ) against a database of Viridiplantae genomes ( Dataset S10 ), a database with nonangiosperm transcriptomes from the 1KP initiative ( 62 ), a database w...
- Full pipeline: quality control [Nextflow v21.10.6] -> alignment/mapping [Nextflow v21.10.6] -> differential/statistical testing [R v4.4, edgeR] -> stage not stated [BLAST, GEMMA]

### A factor integrating transcription and repression of surface antigen genes in African trypanosomes. (PNAS 2026)

- DOI: 10.1073/pnas.2531377123 | PMCID: PMC12890818 | PMID: 41632842
- Evidence: For plotting, all VSG transcript sets were defined by BLASTn search using each VSGnome ( 6 ) as query sequences, accepting hits at least 500 nucleotides long, at least 50% of the query sequence, and at least 50% identity with the query.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [BLAST, ImageJ]

### INDETERMINATE DOMAIN-DELLA protein interactions orchestrate gibberellin-mediated cell elongation in wheat and barley. (PNAS 2026)

- DOI: 10.1073/pnas.2528934123 | PMCID: PMC12867750 | PMID: 41615756
- Evidence: Putative IDD family members in wheat and barley were identified using BLASTp searches against the IWGSC RefSeq v1.2 and Morex V3 proteome databases through the Ensembl Plants platform ( https://plants.ensembl.org/index.html ).
- Full pipeline: read trimming [Trimmomatic v0.39, kallisto] -> alignment/mapping [Bowtie2, Trimmomatic v0.39, kallisto] -> quantification [Trimmomatic v0.39, kallisto] -> stage not stated [BLAST, ImageJ v1.48v]

### Soluble adenylyl cyclase in nonmammalian sperm is directly controlled by pH, not by HCO&lt;sub&gt;3&lt;/sub&gt;&lt;sup&gt;-&lt;/sup&gt; or Ca&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2505026123 | PMCID: PMC12867704 | PMID: 41591904
- Evidence: Bioinformatic searches were performed using BLAST (blastp and tblastn) against publicly available genomes (NCBI, November 2021).
- Full pipeline: alignment/mapping [AlphaFold v2.2.4, ColabFold v1.5.2, MAFFT] -> stage not stated [BLAST, SciPy v1.15.1, statsmodels v0.14.4]

### Intercalated bacterial biofilms are intrinsic internal components of calcium-based kidney stones. (PNAS 2026)

- DOI: 10.1073/pnas.2517066123 | PMCID: PMC12867757 | PMID: 41587311
- Evidence: These agar plates were sent for 16S sequencing at GeneWiz and matched to microbial species using the NCBI BLAST database.
- Full pipeline: stage not stated [BLAST]

### A surface-exposed cardiolipin synthase provides an unexpected paradigm for maintaining the Gram-negative outer membrane. (PNAS 2026)

- DOI: 10.1073/pnas.2524588123 | PMCID: PMC12846801 | PMID: 41570074
- Evidence: ( B ) BLASTp scores comparing E. coli CL synthases to putative CL synthases of A. baumannii .
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX]

### Plasmid mutation rates scale with copy number. (PNAS 2026)

- DOI: 10.1073/pnas.2526088123 | PMCID: PMC12846797 | PMID: 41570072
- Version used: **2.9.0**
- Evidence: To identify plasmid-derived contigs for each strain, BLASTn v2.9.0 + was used to align all assembled sequences against the reference plasmid sequence.
- Full pipeline: read trimming [SPAdes, Trim Galore v0.6.6] -> alignment/mapping [BLAST v2.9.0] -> dimensionality reduction/clustering [igraph] -> simulation/modelling [Matplotlib, NumPy, Python] -> stage not stated [Prokka v1.14.5, R]

### The EPS-I exopolysaccharide transforms &lt;i&gt;Ralstonia&lt;/i&gt; wilt pathogen biofilms into viscoelastic fluids for rapid dissemination in planta. (PNAS 2026)

- DOI: 10.1073/pnas.2512757123 | PMCID: PMC12846841 | PMID: 41570073
- Evidence: We used BLASTp to search 399 RSSC genomes and 72 non-RSSC Ralstonia genomes for homologs of the eps cluster genes and the neighboring xpsR gene whose product activates expression of the eps genes ( 38 ).
- Full pipeline: quantification [CellProfiler] -> dimensionality reduction/clustering [BLAST]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: The DIGS screen was conducted using a minimum blastn bitscore of 30 and minimum sequence length of 30 nucleotides.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Diverse phage communities are maintained stably on a clonal bacterial host. (Science 2024)

- DOI: 10.1126/science.adk1183 | PMCID: PMC7617280 | PMID: 39666794
- Evidence: To identify the taxonomic classification of each phage species we first performed whole-genome blastn searches against the virus database ( https://blast.ncbi.nlm.nih.gov/Blast.cgi ) to find the genus and family of phages with high identity.
- Full pipeline: differential/statistical testing [tidyverse v2.0.0] -> visualisation [R] -> stage not stated [BLAST, SPAdes v3.15.0]

### Metagenomic editing of commensal bacteria in vivo using CRISPR-associated transposases. (Science 2025)

- DOI: 10.1126/science.adx7604 | PMCID: PMC12969935 | PMID: 41231980
- Evidence: In brief, MAG fasta input is parsed into all possible 34 base pair k-mers and these are then filtered for k-mers containing a 5’-CN PAM. k-mers are then mapped back to MAGs for counts with BLASTn ( 83 ) at 100% sequence identity and split into two lists containing either multi-mapping spacer candidates or single-mapping spacer candidates.
- Full pipeline: alignment/mapping [BLAST, Bowtie2, ggplot2] -> quantification [ggplot2] -> normalisation [ggplot2, seaborn] -> visualisation [ggplot2, seaborn] -> stage not stated [Python]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: To determine the whole-locus deletion outcome, the collapsed MiSeq reads were aligned to the reference mouse genome ( Mm10 ) using blastn ( Fig.
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: Each killifish gene was then assigned to its human ortholog (best hit protein with BLASTp E-value >1 × 10 −3 ).
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Sequence similarity analysis We performed sequence similarity analyses between the perturbed gene’s cDNA sequence and the aforementioned observed gene’s elements using BLASTn ( 137 ). cDNA sequence of the perturbed gene’s canonical transcript was obtained from Ensembl v109, along with coordinates of exons, cDNA coding region, and UTRs.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

