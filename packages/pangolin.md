# Pangolin

- **Category:** phylogenetics
- **Papers in survey:** 49
- **Journals:** Cell (15), Nature (14), PNAS (10), Science (8), Lancet (2)
- **Years:** 2021 (18), 2022 (15), 2023 (5), 2024 (7), 2025 (2), 2026 (2)
- **Versions named:** 4.0.6 (2), 2.0 (2), 3.1.5 (1), 4.0 (1), 3.1.11 (1), 2.1.7 (1)
- **Pipeline stages it appears in:** alignment/mapping (3), differential/statistical testing (1), dimensionality reduction/clustering (1)

## Papers

### Elicitation of broadly protective sarbecovirus immunity by receptor-binding domain nanoparticle vaccines. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.015 | PMCID: PMC8440233 | PMID: 34619077
- Evidence: The GD-Pangolin (326-527), WIV1 (316-518), RaTG13 (359-562), RmYN02 (307-492), and ZXC21 (323-507) were synthesized by GenScript into vector pcDNA3.1- or CMVR with a preceding mu-phosphatase signal peptide and a C-terminal octahistidine tag.
- Full pipeline: stage not stated [ChimeraX, Pangolin]

### The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.003 | PMCID: PMC8421097 | PMID: 34537136
- Evidence: We used the GISAID Pangolin annotation to extract sequences assigned to the V1, V2 or V3 lineages discarding all sequences for which sampling dates were not recorded.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [Python] -> stage not stated [Pangolin]

### Generation and transmission of interlineage recombinants in the SARS-CoV-2 pandemic. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.014 | PMCID: PMC8367733 | PMID: 34499854
- Evidence: The aligned sequences were converted from sam to fasta format, and each assigned a Pango lineage ( Rambaut et al., 2020a ) using Pangolin ( O’Toole et al., 2021 ).
- Full pipeline: alignment/mapping [Pangolin, minimap2] -> variant calling [Python] -> structure determination [IQ-TREE v2.1] -> stage not stated [SAMtools, TreeTime]

### Emergence of an early SARS-CoV-2 epidemic in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.030 | PMCID: PMC8313480 | PMID: 34508652
- Version used: **2.0**
- Evidence: ...ork n-CoV-19 V3 primers ARTIC Network https://github.com/artic-network/artic-ncov2019/tree/master/primer_schemes/nCoV-2019/V3 Software and algorithms Pangolin v2.0 Rambaut et al., 2020 https://github.com/cov-lineages/pangolin NextClade v0.12.0 Hadfield et al., 2018 https://github.com/nextstrain/nextclade IQtree2 Minh et al., 2020 https://github.com/iqtree/iqtree2 BEASTv1.10.5pre Suchard et al., 20...
- Full pipeline: stage not stated [BWA, Pangolin v2.0, R, Snakemake]

### A selective sweep in the Spike gene has driven SARS-CoV-2 human adaptation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.007 | PMCID: PMC8260498 | PMID: 34289344
- Evidence: Four genome sequences (Pangolin coronavirus isolate PCoV_GX-P5L: GenBank/ MT040335.1 ; Bat coronavirus RaTG13: GenBank/ MN996532.2 ; Bat SARS-like coronavirus isolate Rs4231: GenBank/ KY417146.1 ; Bat coronavirus BtRs-BetaCoV: GenBank/ MK211376.1 ) were used to assess the nucleotide changes among different Sarbecovirus members.
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> stage not stated [Pangolin, PyMOL]

### Emergence and rapid transmission of SARS-CoV-2 B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.052 | PMCID: PMC8009040 | PMID: 33861950
- Version used: **2.0**
- Evidence: ...om/artic-network/artic-ncov2019/tree/master/primer_schemes/nCoV-2019/V3 Software and algorithms DRAGEN COVIDSeq Test Pipeline v.1.3.0.28 Illumina N/A Pangolin v2.0 O’Toole et al., 2021b https://github.com/cov-lineages/pangolin NextClade v0.12.0 Hadfield et al., 2018 https://github.com/nextstrain/nextclade Iqtree2 Minh et al., 2020 https://github.com/iqtree/iqtree2 BEASTv1.10.5pre Suchard et al., 2...
- Full pipeline: variant calling [Snakemake] -> stage not stated [BWA, Pangolin v2.0]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: The number of B.1.1.7 sequences for each state (top x axis; black dots) was determined by the Pangolin lineage assignment in the https://www.gisaid.org/ metadata.
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### N-terminal domain antigenic mapping reveals a site of vulnerability for SARS-CoV-2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.028 | PMCID: PMC7962585 | PMID: 33761326
- Evidence: VSV-based pseudotype virus production and neutralization assay SARS-CoV-2 S (YP 009724390.1), RaTG13 S ( QHR63300.2 ), Pangolin-Guangdong S( QLR06867.1 ), Pangolin-Guanxi S (EPI ISL 410539), SARS-CoV S (YP 009825051.1), WIV1 S ( AGZ48831.1 ) and WIV16 S ( ALK02457.1 ) pseudotyped VSV viruses were prepared using 293T cells seeded in 10-cm dishes.
- Full pipeline: structure determination [PHENIX, RELION v3.0] -> visualisation [ChimeraX] -> stage not stated [Pangolin, UCSF Chimera]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: We found that three of the RBDs from animal isolates showed strong affinity for hACE2: GD Pangolin, which has a highly similar RBM to SARS-CoV-2, GX Pangolin, which has a more divergent RBM, and Bat CoV WIV1 which is highly divergent ( Figures S2 A and S2B).
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Neutralizing immunity in vaccine breakthrough infections from the SARS-CoV-2 Omicron and Delta variants. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.019 | PMCID: PMC8930394 | PMID: 35429436
- Evidence: Consensus sequences were generated using iVar (version 1.3.1) ( Grubaugh et al., 2019 ) and lineages were assigned using Pangolin ( Rambaut et al., 2020 ) (version 3.1.17).
- Full pipeline: read trimming [BLAST] -> quantification [Python v3.7.10] -> differential/statistical testing [Python v3.7.10] -> visualisation [Python v3.7.10] -> stage not stated [Pangolin, R v4.0, ggplot2, seaborn]

### SARS-CoV-2 breakthrough infections elicit potent, broad, and durable neutralizing antibody responses. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.011 | PMCID: PMC8769922 | PMID: 35123650
- Evidence: Lineage was assigned using the Pangolin COVID-19 Lineage Assigner version 3.1.11 ( https://pangolin.cog-uk.io/ ) ( Paredes et al., 2021 ) Roche anti-N analysis 0.5mL serum/plasma samples were tested in CAP/CLIA-accredited clinical laboratory using the FDA-authorized Roche Elecsys Anti-SARS-CoV-2 for anti-nucleocapsid antibodies using manufacturer’s established positivity cut-off index of ≥1.0 ( Th...
- Full pipeline: stage not stated [Nextstrain v1.0.0, Pangolin]

### The Omicron variant is highly resistant against antibody-mediated neutralization: Implications for control of the COVID-19 pandemic. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.032 | PMCID: PMC8702401 | PMID: 35026151
- Evidence: ..._American Mink ACE2-cMYC This study N/A Plasmid: pQCXIP_Cat ACE2-cMYC This study N/A Plasmid: pQCXIP_Red fox ACE2-cMYC This study N/A Plasmid: pQCXIP_Pangolin ACE2-cMYC This study N/A Plasmid: pQCXIP_Pig ACE2-cMYC This study N/A Plasmid: pQCXIP_Mouse ACE2-cMYC This study N/A Plasmid: pQCXIP_Bat ( Rhinolophus affinis ) ACE2-cMYC This study N/A Plasmid: pQCXIP_Bat ( Rhinolophus landeri ) ACE2-cMYC T...
- Full pipeline: stage not stated [Pangolin]

### A bat MERS-like coronavirus circulates in pangolins and utilizes human DPP4 and host proteases for cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.019 | PMCID: PMC9933427 | PMID: 36803605
- Evidence: 39 N/A ElectroMAX™ DH10B T1 Phage-Resistant Competent Cells Thermo Fisher Scientific Cat#: 12033015 Biological samples Pangolin anal swab and serum sample This paper N/A Chemicals, peptides, and recombinant proteins Lipofectamine 3000 Thermo Fisher Scientific Cat#: L3000015 DAPI Beyotime Cat#: C1002 tribromoethanol (Avertin) Sigma Cat#: T-48402 4% paraformaldehyde Boster Cat#: AR1068 RNAlater Stab...
- Full pipeline: stage not stated [BWA v0.7.12, Cutadapt v1.18, IQ-TREE v1.6.1, ImageJ, Pangolin]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: ...formed in HEK-293T-hACE2 and HEK-293T-R.alc.ACE2, constructs for membrane-anchored S glycoproteins from SARS-CoV-1 Urbani, BA.2.86 ( WPL86459.1 ), GX-Pangolin ( QIA48623.1 ), Khosta-1 ( QVN46559.1 ), Khosta-2 ( QVN46569.1 ), SARS-CoV-1 Civet007 ( AAU04646.1 ), RaTG13delta21 ( QHR63300.2 ), WIV1 ( AGZ48828.1 ), RsSHC014 ( AGZ48806.1 ), PRD-0038 ( QTJ30153.1 ), PRD-0038-dm (harboring mutations of th...
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Immune evasion, infectivity, and fusogenicity of SARS-CoV-2 BA.2.86 and FLip variants. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.026 | PMCID: PMC10872432 | PMID: 38194968
- Evidence: Eight of the samples were confirmed to be XBB.1.5 using COVID-Seq Artic v4 sequencing and typed with Dragen COVID Lineage with Pangolin plug-in (Illumina).
- Full pipeline: alignment/mapping [R] -> quantification [ImageJ] -> stage not stated [Pangolin, PyMOL]

### Efficacy of ChAdOx1 nCoV-19 (AZD1222) vaccine against SARS-CoV-2 variant of concern 202012/01 (B.1.1.7): an exploratory analysis of a randomised controlled trial. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00628-0 | PMCID: PMC8009612 | PMID: 33798499
- Version used: **2.1.7**
- Evidence: Lineages were assigned by Pangolin version 2.1.7 (lineages version 2021–02–12) using the determined consensus genome for each sequenced sample.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.402] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [Pangolin v2.1.7]

### Efficacy of the adjuvanted subunit protein COVID-19 vaccine, SCB-2019: a phase 2 and 3 multicentre, double-blind, randomised, placebo-controlled trial. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)00055-1 | PMCID: PMC8776284 | PMID: 35065705
- Evidence: Pangolin and NextClade were used for viral variants and lineages identification.
- Full pipeline: stage not stated [Pangolin]

### Genomic reconstruction of the SARS-CoV-2 epidemic in England. (Nature 2021)

- DOI: 10.1038/s41586-021-04069-y | PMCID: PMC8674138 | PMID: 34649268
- Evidence: Lineage assignments were made using Pangolin 5 , according to the latest lineage definitions at the time, except for B.1.617, which we reanalysed after the designation of sublineages B.1.617.1, B.1.617.2 and B.1.617.3.
- Full pipeline: stage not stated [Pangolin]

### SARS-CoV-2 B.1.617.2 Delta variant replication and immune evasion. (Nature 2021)

- DOI: 10.1038/s41586-021-03944-y | PMCID: PMC8566220 | PMID: 34488225
- Version used: **3.1.5**
- Evidence: This was noted and all sequences were assigned a lineage with Pangolin v3.1.5 (ref.
- Full pipeline: stage not stated [IQ-TREE v2.1.4, Nextstrain v0.15, Pangolin v3.1.5, PyMOL, R v4.1]

### Emergence and expansion of SARS-CoV-2 B.1.526 after identification in New York. (Nature 2021)

- DOI: 10.1038/s41586-021-03908-2 | PMCID: PMC8481122 | PMID: 34428777
- Evidence: Phylogenetic examination showed that the B.1.526 lineage comprises two closely related sub-lineages harbouring either E484K (B.1.526-E484K; defined as Pangolin lineage B.1.526) or S477N (B.1.526-S477N; Pangolin lineage B.1.526.2), and the additional sub-lineage B.1.526.1, harbouring the L452R substitution (B.1.526-L452R).
- Full pipeline: alignment/mapping [Nextstrain] -> structure determination [IQ-TREE, Nextstrain, TreeTime] -> stage not stated [Pangolin]

### Pandemic-scale phylogenomics reveals the SARS-CoV-2 recombination landscape. (Nature 2022)

- DOI: 10.1038/s41586-022-05189-9 | PMCID: PMC9519458 | PMID: 35952714
- Evidence: Additionally, we find evidence that recombination has influenced the Pangolin SARS-CoV-2 nomenclature system 23 .
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [Pangolin, R]

### Context-specific emergence and growth of the SARS-CoV-2 Delta variant. (Nature 2022)

- DOI: 10.1038/s41586-022-05200-3 | PMCID: PMC9534748 | PMID: 35952712
- Evidence: Scorpio ( https://github.com/cov-lineages/scorpio ) was run as part of Pangolin 43 , and sequences containing the Delta VOC constellation of mutations were kept for further analysis.
- Full pipeline: alignment/mapping [minimap2] -> structure determination [BEAST v1.10] -> visualisation [Python] -> stage not stated [Pangolin]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Evidence: Pseudovirus-neutralization assay SARS-CoV-2 spike (GenBank: MN908947 ), Pangolin-GD spike (GISAID: EPI_ISL_410721), RaTG13 spike (GISAID: EPI_ISL_402131), SARS-CoV-1 spike (GenBank: AY278491 ), Omicron BA.1 spike (A67V, H69del, V70del, T95I, G142D, V143del, Y144del, Y145del, N211del, L212I, ins214EPE, G339D, S371L, S373P, S375F, K417N, N440K, G446S, S477N, T478K, E484A, Q493R, G496S, Q498R, N501Y,...
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### ACE2 binding is an ancestral and evolvable trait of sarbecoviruses. (Nature 2022)

- DOI: 10.1038/s41586-022-04464-z | PMCID: PMC8967715 | PMID: 35114688
- Evidence: 2 ) GD-Pangolin-CoV (consensus RBD sequence reported in figure 3a of ref.
- Full pipeline: alignment/mapping [RAxML v8.2.12] -> stage not stated [Pangolin]

### Altered TMPRSS2 usage by SARS-CoV-2 Omicron impacts infectivity and fusogenicity. (Nature 2022)

- DOI: 10.1038/s41586-022-04474-x | PMCID: PMC8942856 | PMID: 35104837
- Evidence: The mutations detected and viral lineage were determined by using CoVsurver ( https://corona.bii.a-star.edu.sg ) and Pangolin COVID-19 lineage assigner ( https://pangolin.cog-uk.io/ ).
- Full pipeline: read trimming [Bowtie2 v2.3.4.3] -> alignment/mapping [Bowtie2 v2.3.4.3] -> dimensionality reduction/clustering [Fiji] -> visualisation [ChimeraX v1.3] -> stage not stated [GROMACS, ImageJ, Pangolin, Scanpy v1.7.1]

### Multiple pathways for SARS-CoV-2 resistance to nirmatrelvir. (Nature 2023)

- DOI: 10.1038/s41586-022-05514-2 | PMCID: PMC9849135 | PMID: 36351451
- Version used: **4.0.6**
- Evidence: Pangolin 4.0.6 with UShER v.1.6 was used for parsimony-based lineage assignment.
- Full pipeline: dimensionality reduction/clustering [SciPy, seaborn] -> stage not stated [CellProfiler v4.0.7, Nextflow, Pangolin v4.0.6]

### Prevalence of persistent SARS-CoV-2 in a large community surveillance study. (Nature 2024)

- DOI: 10.1038/s41586-024-07029-4 | PMCID: PMC10901734 | PMID: 38383783
- Evidence: To map between Pangolin lineages and Nextstrain clades, we assumed B.1.1.7 ≡ 20I, B.1.617.2 ≡ {21A,21I,21J}, BA.1 ≡ 21K and BA.2 ≡ {21L,22C,22D}.
- Full pipeline: stage not stated [IQ-TREE v1.6.12, Nextstrain, Pangolin]

### Assessing phylogenetic confidence at pandemic scales. (Nature 2025)

- DOI: 10.1038/s41586-025-09567-x | PMCID: PMC12611777 | PMID: 41193798
- Evidence: Tips are coloured according to the Pango 3 lineage assigned by Pangolin 35 v.4.3 (with Pangolin-data v.1.21) to the corresponding genomes.
- Full pipeline: stage not stated [IQ-TREE v2.1.3, Pangolin, RAxML]

### SARS-CoV-2 evolution on a dynamic immune landscape. (Nature 2025)

- DOI: 10.1038/s41586-024-08477-8 | PMCID: PMC11882442 | PMID: 39880955
- Evidence: Variant proportions and spike pseudo-groups If pangolin lineage information was absent in the data, lineage information was assigned using established methods 54 , 55 .
- Full pipeline: stage not stated [Pangolin, Python v3.11.3, R v4.2.3, SciPy]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: We also contextualize the performance of Evo 2 against a wide range of models, including statistical measures of conservation (for example, PhyloP); unsupervised language models of proteins, RNA and DNA (for example, ESM-1b); supervised splicing prediction models (for example, Pangolin and SpliceAI); and human variant effect prediction models (for example, AlphaMissense, GPN-MSA and CADD).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### Advancing regulatory variant effect prediction with AlphaGenome. (Nature 2026)

- DOI: 10.1038/s41586-025-10014-0 | PMCID: PMC12851941 | PMID: 41606153
- Evidence: Even within a single modality like splicing, specialized models such as SpliceAI 4 or Pangolin 11 predict certain aspects (such as splice site prediction) while omitting others (such as splice junction prediction or competition between splice sites).
- Full pipeline: stage not stated [Pangolin]

### Dromedary camel nanobodies broadly neutralize SARS-CoV-2 variants. (PNAS 2022)

- DOI: 10.1073/pnas.2201433119 | PMCID: PMC9170159 | PMID: 35476528
- Evidence: Sequences of coronavirus RBD for Bat_RaTG13 (A0A6B9WHD3), Human BJ01 ( Q6GYR1 ), Pangolin (A0A6G6A2Q2), SARS-CoV-2 ( P0DTC2 ), and SARS-CoV-1 ( P59594 ) are presented for comparison purposes.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.19.2] -> stage not stated [Pangolin]

### Multiple spillovers from humans and onward transmission of SARS-CoV-2 in white-tailed deer. (PNAS 2022)

- DOI: 10.1073/pnas.2121644119 | PMCID: PMC8833191 | PMID: 35078920
- Version used: **3.1.11**
- Evidence: Genetic lineages, variants being monitored, and variants of concern were identified and designated by Pangolin version 3.1.11 ( 14 ) with pangoLEARN module 2021-08-024 .
- Full pipeline: read trimming [SAMtools v1.11] -> alignment/mapping [QGIS, RAxML] -> variant calling [SAMtools v1.11] -> stage not stated [Pangolin v3.1.11]

### Differential interferon-α subtype induced immune signatures are associated with suppression of SARS-CoV-2 infection. (PNAS 2022)

- DOI: 10.1073/pnas.2111600119 | PMCID: PMC8872780 | PMID: 35131898
- Evidence: Virus stock was sequenced and assigned to B.1.1.10 according to the Pangolin database ( 62 ), accession number EPI_ISL_602518.
- Full pipeline: differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [Pangolin]

### Genomic analysis reveals a cryptic pangolin species. (PNAS 2023)

- DOI: 10.1073/pnas.2304096120 | PMCID: PMC10556634 | PMID: 37748052
- Evidence: Our analyses provide robust and compelling evidence that this cryptic species represents a separately evolving pangolin lineage whose demographic history is distinct from all other recognized pangolin species.
- Full pipeline: alignment/mapping [SAMtools v1.3] -> variant calling [GATK] -> stage not stated [BEAST v2.6.6, Metascape, OrthoFinder v2.5.4, PLINK v2.0, Pangolin, SnpEff v4.3t, VCFtools v0.1.13]

### Evolution of coronavirus frameshifting elements: Competing stem networks explain conservation and variability. (PNAS 2023)

- DOI: 10.1073/pnas.2221324120 | PMCID: PMC10193956 | PMID: 37155888
- Evidence: ... (Pi-Bat), NC_030886 for Rousettus bat coronavirus (Ro-Bat), NC_045512 for Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), MT121216 for Pangolin coronavirus, JX993987 for Bat coronavirus Rp, KF367457 for Bat SARS-like coronavirus WIV1, NC_004718 for Severe acute respiratory syndrome coronavirus (SARS-CoV).
- Full pipeline: stage not stated [Pangolin, RAxML v8.2.12]

### White-tailed deer (<i>Odocoileus virginianus</i>) may serve as a wildlife reservoir for nearly extinct SARS-CoV-2 variants of concern. (PNAS 2023)

- DOI: 10.1073/pnas.2215067120 | PMCID: PMC9963525 | PMID: 36719912
- Version used: **4.0.6**
- Evidence: Lineage classification was performed using Pangolin version 4.0.6 ( 18 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.453, QGIS] -> dimensionality reduction/clustering [QGIS] -> visualisation [IQ-TREE, QGIS] -> stage not stated [Nextstrain, Pangolin v4.0.6]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Evidence: To examine the presence of a protease, we aligned with NS3Pro of Classical swine fever virus (CSFV), Pangolin pestivirus, and the divergent flavi-like virus with MAFFT v7.511 ( 65 ) L-INS-I method.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Wnt/Wingless signaling promotes lipid mobilization through signal-induced transcriptional repression. (PNAS 2024)

- DOI: 10.1073/pnas.2322066121 | PMCID: PMC11252803 | PMID: 38968125
- Evidence: Consequently, Drosophila T-cell factor/Pangolin (dTCF/Pan), the T-cell factor (TCF) and lymphoid-enhancing factor (LEF) homolog in Drosophila , is repressed by transcription corepressors such as Groucho (Gro), a Drosophila Transducin-like Enhancer of split (TLE) homolog.
- Full pipeline: stage not stated [Pangolin]

### Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods. (PNAS 2024)

- DOI: 10.1073/pnas.2317284121 | PMCID: PMC10962941 | PMID: 38478692
- Evidence: Then, Pangolin lineages were obtained by running PangoLEARN v1.18 ( 4 ) and taking the “Scorpio call” as “ground truth,” to compare to the clusters detected from the PaCMAP projections.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> dimensionality reduction/clustering [Pangolin, UMAP] -> stage not stated [Python v3.10.0]

### Conversion of monoclonal IgG to dimeric and secretory IgA restores neutralizing ability and prevents infection of Omicron lineages. (PNAS 2024)

- DOI: 10.1073/pnas.2315354120 | PMCID: PMC10801922 | PMID: 38194459
- Evidence: The apparent resistance of DXP-604 to SARS-CoV-2 mutations was confirmed in a S-pseudotype vesicular stomatitis virus neutralization assay showing its potent neutralizing (IC 50 : 0.01 to 1.6 nM) effect against 15 known SARS-CoV-2 variants and other clade 1b sarbecoviruses circulating among other species, including RaTG13 and Pangolin-GD ( 37 ) ( SI Appendix, Fig.
- Full pipeline: stage not stated [Pangolin]

### Broad betacoronavirus neutralization by a stem helix-specific human antibody. (Science 2021)

- DOI: 10.1126/science.abj3321 | PMCID: PMC9268357 | PMID: 34344823
- Evidence: Moreover, S2P6 inhibited SARS-CoV S, Pangolin Guangdong 2019 (PANG/GD) S, MERS-CoV S, and OC43 S VSV pseudotypes with median inhibitory concentration (IC 50 ) values ranging from 0.02 to 17 μg/ml ( Fig.
- Full pipeline: stage not stated [Pangolin]

### Chimeric spike mRNA vaccines protect against Sarbecovirus challenge in mice. (Science 2021)

- DOI: 10.1126/science.abi4506 | PMCID: PMC8899822 | PMID: 34214046
- Evidence: Mice in groups 1 and 2 generated similar-magnitude binding antibody responses against SARS-CoV-2 D614G, Pangolin GXP4L, and RaTG13 spikes ( Fig.
- Full pipeline: stage not stated [Pangolin]

### Genomics and epidemiology of the P.1 SARS-CoV-2 lineage in Manaus, Brazil. (Science 2021)

- DOI: 10.1126/science.abh2644 | PMCID: PMC8139423 | PMID: 33853970
- Evidence: Viral lineages were classified by using the Pangolin ( 26 ) software tool ( http://pangolin.cog-uk.io ), nextclade ( https://clades.nextstrain.org ), and standard phylogenetic analysis using complete reference genomes.
- Full pipeline: alignment/mapping [Pangolin]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Evidence: Lineages were assigned by the Pangolin web server ( 60 ) using the determined consensus genome for each sequenced sample.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

### Broad and potent activity against SARS-like viruses by an engineered human monoclonal antibody. (Science 2021)

- DOI: 10.1126/science.abf4830 | PMCID: PMC7963221 | PMID: 33495307
- Evidence: Thirteen viruses were selected from clade 1—representing the closest known relatives of SARS-CoV-2 (GD-Pangolin and RaTG13) to the most divergent (SHC014 and Rs4231)—as well as four viruses from the distantly related clades 2 and 3, which do not use ACE2 as a host receptor ( 21 ) ( Fig.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [Pangolin]

### Imprinted antibody responses against SARS-CoV-2 Omicron sublineages. (Science 2022)

- DOI: 10.1126/science.adc9127 | PMCID: PMC12945441 | PMID: 36264829
- Evidence: S2X324 cross-reacted with the sarbecovirus clade 1b Pangolin-GD RBD, but did not recognize more divergent sarbecovirus RBDs ( Fig.
- Full pipeline: stage not stated [Pangolin]

### The evolving SARS-CoV-2 epidemic in Africa: Insights from rapidly expanding genomic surveillance. (Science 2022)

- DOI: 10.1126/science.abq5358 | PMCID: PMC9529057 | PMID: 36108049
- Evidence: Lineages that returned no classification with Pangolin (“None”) showed the highest mean N count, suggesting that high mean N count per genome was probably the basis for failed classification.
- Full pipeline: stage not stated [Pangolin, TreeTime]

### Twin peaks: The Omicron SARS-CoV-2 BA.1 and BA.2 epidemics in England. (Science 2022)

- DOI: 10.1126/science.abq4411 | PMCID: PMC9161371 | PMID: 35608440
- Version used: **4.0**
- Evidence: We used the ARTIC protocol ( 34 ) (version 4 for rounds 16 and 17 and version 4.1 for rounds 18 and 19) for viral RNA amplification, CoronaHiT for preparation of sequencing libraries ( 35 ), the ARTIC bioinformatics pipeline ( 34 ) and assigned lineages using Pangolin (v4.0 with pangolin-data v1.2.133) ( 36 ).
- Full pipeline: stage not stated [Pangolin v4.0]

