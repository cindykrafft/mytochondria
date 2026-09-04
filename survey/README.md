# Open-source software in *Nature*, *Science*, *PNAS*, *NEJM*, *The Lancet* and *Cell*, 2021–2026

_Generated 2026-08-30 from the Europe PMC REST API. Reproducible with the scripts in `scripts/`._

## Read this first

The request behind this document was to read **every** paper published in these six journals
over five years and record the open-source software each used. That is not achievable, and a
document claiming to have done it would be untrustworthy. Two hard limits:

- **Volume.** These journals published **44,198 research articles** in 2021–2026 (plus ~30,730
  news, editorial, comment, letter and correction items, excluded here).

- **Access.** Only **20,501** of those (46%) have machine-readable full text. The rest are
  paywalled or deposited abstract-only, so their Methods sections — where software is named —
  cannot be read.

What follows therefore covers **the 20,501 research articles whose full text is openly readable**.
Every row is extracted from the article's own text and carries a quotable evidence sentence, so
each claim is checkable. The **23,697 articles that could not be read** are listed individually in
`data/gap_list.tsv` — a stated blind spot, not a silent omission.


### Coverage is very uneven by journal

| Journal | Research articles | Full text read | Coverage | ≥1 OSS package |
|---|---|---|---|---|
| Nature | 7,542 | 3,014 | 40% | 2,148 |
| Science | 6,144 | 311 | 5% | 172 |
| PNAS | 20,603 | 16,074 | 78% | 7,560 |
| New England J. of Medicine | 3,757 | 247 | 7% | 31 |
| The Lancet | 3,724 | 471 | 13% | 104 |
| Cell | 2,428 | 384 | 16% | 349 |

**This is the single most important caveat.** PNAS is fully open and supplies most of the
corpus; NEJM, *The Lancet* and *Science* are largely closed. Absolute counts below reflect
**what is readable, not what is used**. A package favoured in Lancet clinical trials will look
rarer than one favoured in PNAS papers even if real-world use is identical. Compare packages
within a journal, not across them.


## Headline numbers

| Metric | Value |
|---|---|
| Research articles identified (2021–2026) | 44,198 |
| Full text retrieved and parsed | 20,501 |
| Articles naming ≥1 open-source package | 10,364 (51% of those read) |
| Distinct open-source packages detected | 270 |
| Total (paper × package) usage records | 36,424 |
| Articles that could not be read (gap list) | 23,697 |
| Usage records with a version captured | 9,439 (26%) |


Articles using open-source software, by year: **2021** 1,024, **2022** 1,934, **2023** 1,913, **2024** 2,150, **2025** 2,567, **2026** 776


## Most-used open-source packages

| # | Package | Domain | Papers | Versions most often named |
|---|---|---|---|---|
| 1 | R | general | 2,959 | 4.0, 4.1, 4.2.2 |
| 2 | ImageJ | imaging | 2,443 | 1.53, 2.1.0, 1.53t |
| 3 | AlphaFold | structbio | 1,197 | 2.0, 2.2.0, 2.3.2 |
| 4 | UMAP | single-cell | 1,111 | 0.2.7.0, 3.1, 0.5.1 |
| 5 | Python | general | 964 | 3.7, 3.9, 3.6 |
| 6 | PHENIX | structbio | 905 | 1.20.1, 1.19.2, 1.21 |
| 7 | DESeq2 | genomics | 886 | 1.30.1, 1.26.0, 1.32.0 |
| 8 | Seurat | single-cell | 767 | 4.3.0, 4.1.0, 5.1.0 |
| 9 | GSEA | genomics | 720 | 4.3.2, 4.0.3, 4.1.0 |
| 10 | PyMOL | structbio | 700 | 2.5, 2.5.2, 2.5.4 |
| 11 | SAMtools | genomics | 692 | 1.9, 1.10, 1.3.1 |
| 12 | ChimeraX | structbio | 679 | 1.3, 1.8, 1.5 |
| 13 | ggplot2 | general | 587 | 3.3.5, 3.5.1, 3.4.2 |
| 14 | STAR | genomics | 489 | 2.7.10a, 2.7.9a, 2.7.3a |
| 15 | Bowtie2 | genomics | 477 | 2.4.2, 2.4.5, 2.3.5.1 |
| 16 | MACS2 | genomics | 475 | 2.2.7.1, 2.2.6, 2.1.1.20160309 |
| 17 | SciPy | general | 472 | 1.10.1, 1.4.1, 1.11.4 |
| 18 | RELION | structbio | 466 | 3.1, 3.0, 4.0 |
| 19 | BWA | genomics | 418 | 0.7.17, 0.7.15, 0.7.12 |
| 20 | Coot | structbio | 373 | 0.9.8.1, 0.9, 0.9.8 |
| 21 | MAFFT | phylogenetics | 346 | 7.475, 7.490, 7.453 |
| 22 | featureCounts | genomics | 331 | 2.0.1, 2.0.0, 1.5.0 |
| 23 | Cutadapt | genomics | 331 | 1.18, 4.1, 3.4 |
| 24 | BLAST | phylogenetics | 325 | 2.13.0, 2.12.0, 2.7.1 |
| 25 | scikit-learn | general | 322 | 1.0.2, 1.2.2, 0.21.3 |
| 26 | FastQC | genomics | 322 | 0.11.9, 0.11.8, 0.11.5 |
| 27 | edgeR | genomics | 318 | 3.36.0, 3.32.1, 3.26.8 |
| 28 | GATK | genomics | 312 | 3.7, 3.8, 4.1.4.1 |
| 29 | lme4 | general | 312 | 1.1, 3.1, 1.1.27.1 |
| 30 | UCSF Chimera | structbio | 305 | 1.14, 1.15, 1.16 |
| 31 | BEDTools | genomics | 302 | 2.30.0, 2.29.2, 2.26.0 |
| 32 | Trimmomatic | genomics | 291 | 0.39, 0.36, 0.38 |
| 33 | MotionCor2 | structbio | 290 | 1.4.0, 1.1.0, 1.5 |
| 34 | Picard | genomics | 289 | 2.2.4, 2.9.4, 2.23.4 |
| 35 | IQ-TREE | phylogenetics | 258 | 1.6.12, 2.0.3, 2.1.2 |
| 36 | Clustal Omega | phylogenetics | 257 | 1.2.4, 1.2.2, 1.2.3 |
| 37 | NumPy | general | 253 | 1.24.3, 1.19.2, 1.19.5 |
| 38 | GROMACS | md | 249 | 2021.5, 2020.1, 2021.3 |
| 39 | clusterProfiler | genomics | 244 | 4.10.1, 4.6.2, 3.14.3 |
| 40 | Matplotlib | general | 240 | 3.7.1, 3.5.2, 3.5.1 |
| 41 | tidyverse | general | 238 | 2.0.0, 1.1.4, 1.3.1 |
| 42 | limma | genomics | 234 | 3.46.0, 3.58.1, 3.34.9 |
| 43 | Bioconductor | general | 216 | 3.14, 3.8, 3.15 |
| 44 | BCFtools | genomics | 202 | 1.9, 1.10.2, 1.13 |
| 45 | Scanpy | single-cell | 200 | 1.9.1, 1.6.0, 1.8.2 |
| 46 | Fiji | imaging | 198 | 2.1.0, 2.9.0, 2.0.0 |
| 47 | HISAT2 | genomics | 185 | 2.1.0, 2.2.1, 2.0.5 |
| 48 | PLINK | statgen | 184 | 1.9, 1.90b, 2.0 |
| 49 | scDblFinder | single-cell | 179 | 2.0.3, 0.2.1, 0.2.3 |
| 50 | Cytoscape | genomics | 178 | 3.9.1, 3.7.2, 3.7.1 |
| 51 | ColabFold | structbio | 177 | 1.5.5, 1.5.2, 1.3 |
| 52 | minimap2 | genomics | 173 | 2.17, 2.24, 2.26 |
| 53 | HOMER | genomics | 171 | 4.11, 4.10, 4.11.1 |
| 54 | Trim Galore | genomics | 169 | 0.6.6, 0.6.7, 0.6.10 |
| 55 | RAxML | phylogenetics | 167 | 8.2.12, 8.2.11, 8.2.10 |
| 56 | deepTools | genomics | 167 | 3.5.1, 3.5.0, 3.3.1 |
| 57 | pheatmap | general | 167 | 1.0.12 |
| 58 | BUSCO | phylogenetics | 165 | 5.2.2, 3.0.2, 4.0.5 |
| 59 | VMD | md | 165 | 1.9.3, 1.9.4, 1.9 |
| 60 | HMMER | phylogenetics | 162 | 3.1b, 3.3.2, 3.4 |

Complete ranking of all 270 packages: `data/package_index.tsv`.


## By research domain

| Domain | Distinct packages | Usage records |
|---|---|---|
| genomics | 64 | 10,667 |
| general | 39 | 8,123 |
| structbio | 17 | 5,704 |
| imaging | 12 | 3,276 |
| single-cell | 17 | 2,982 |
| phylogenetics | 19 | 2,322 |
| md | 14 | 862 |
| statgen | 17 | 666 |
| neuroimaging | 24 | 604 |
| microbiome | 10 | 343 |
| workflow | 8 | 321 |
| physical | 19 | 280 |
| neuro-tools | 10 | 274 |


## Most common analysis pipelines

Each tool's pipeline stage is inferred from the sentence that names it, then ordered
canonically. The 25 most frequent stage sequences:

| Papers | Pipeline stage sequence |
|---|---|
| 685 | differential/statistical testing |
| 420 | simulation/modelling |
| 395 | quantification |
| 379 | alignment/mapping |
| 350 | dimensionality reduction/clustering |
| 259 | visualisation |
| 251 | structure determination |
| 140 | machine learning |
| 126 | structure determination → visualisation |
| 119 | dimensionality reduction/clustering → visualisation |
| 112 | alignment/mapping → structure determination |
| 104 | alignment/mapping → differential/statistical testing |
| 91 | read trimming → alignment/mapping |
| 90 | dimensionality reduction/clustering → differential/statistical testing |
| 76 | normalisation |
| 71 | differential/statistical testing → visualisation |
| 70 | alignment/mapping → visualisation |
| 67 | quantification → differential/statistical testing |
| 61 | alignment/mapping → dimensionality reduction/clustering |
| 61 | alignment/mapping → quantification |
| 47 | simulation/modelling → visualisation |
| 44 | alignment/mapping → structure determination → visualisation |
| 39 | read trimming |
| 38 | registration |
| 38 | quantification → normalisation |

Per-paper pipelines are in `data/papers.tsv` (`pipeline` column) and `data/pipelines.jsonl`.


## Neuroimaging stack (relevance to this repository)

This survey was run in the AFNI repository, so neuroimaging tools are broken out. A bug in
any of these would propagate to the papers listed on its package page.

| Package | Papers | Journals | Versions named |
|---|---|---|---|
| FreeSurfer | 116 | PNAS (96), Nature (18), Science (1), Cell (1) | 6.0.0, 7.1.1, 7.1, 6.0.1 |
| FSL | 114 | PNAS (92), Nature (19), Cell (2), Science (1) | 5.0.9, 6.0, 6.0.3, 6.0.7.8 |
| SPM | 76 | PNAS (65), Nature (8), Cell (3) | — |
| DeepLabCut | 71 | Nature (34), PNAS (27), Cell (9), Science (1) | 2.2.0.6, 2.2.3, 2.3.8, 2.2.1.1 |
| Kilosort | 60 | Nature (39), PNAS (17), Cell (4) | 2.5, 2.0, 1.0, 4.0 |
| ANTs | 55 | PNAS (44), Nature (9), Science (1), Cell (1) | 2.2.0, 2.1, 2.1.0, 2.3.3 |
| FieldTrip | 42 | PNAS (36), Nature (5), Cell (1) | 3.5 |
| Psychtoolbox | 41 | PNAS (24), Nature (15), Cell (2) | 3.0.9, 3.0.18, 3.0.16, 3.0.11 |
| AFNI | 39 | PNAS (38), Nature (1) | 21.1.10, 2016.09.04.1341 |
| fMRIPrep | 34 | PNAS (31), Nature (3) | 20.2.3, 1.2.3, 20.2.1, 20.2.0 |
| Suite2p | 32 | Nature (19), PNAS (10), Cell (2), Science (1) | — |
| PsychoPy | 25 | PNAS (19), Nature (6) | 2.22, 2021.1.4, 2021.2.3, 1.90.3 |
| EEGLAB | 22 | PNAS (20), Nature (1), Cell (1) | 2019.1, 2021.0, 13.6.5b |
| Connectome Workbench | 19 | PNAS (12), Nature (5), Science (1), Cell (1) | 1.5, 1.2.3, 1.0 |
| Nilearn | 14 | PNAS (11), Nature (2), Science (1) | 0.4.2, 0.5.2, 0.6.2 |
| CaImAn | 14 | Nature (9), PNAS (5) | — |
| Nipype | 13 | PNAS (12), Nature (1) | 1.5.1, 1.6.1, 1.2.0, 1.1.1 |
| MRtrix3 | 12 | PNAS (12) | — |
| SLEAP | 10 | Nature (6), PNAS (3), Science (1) | 1.3.3, 1.3.0 |
| jsPsych | 10 | PNAS (7), Nature (3) | 7.3.3 |
| MNE-Python | 9 | PNAS (6), Nature (3) | 0.22.0, 0.24, 0.23.0 |
| Brian2 | 8 | Nature (4), PNAS (4) | 2.2.2.1 |
| CONN toolbox | 7 | PNAS (7) | — |
| SUMA | 6 | PNAS (6) | — |
| dcm2niix | 4 | Nature (2), PNAS (2) | — |
| NiBabel | 4 | PNAS (2), Nature (1), Cell (1) | 3.2.2, 3.2.0 |
| DIPY | 4 | PNAS (3), Nature (1) | — |
| BrainNet Viewer | 4 | PNAS (4) | — |
| SpikeInterface | 3 | Nature (3) | — |
| MRIQC | 3 | PNAS (2), Nature (1) | 0.16.1, 0.15.1, 0.15.0 |
| Camino | 3 | PNAS (2), Lancet (1) | — |
| QSIPrep | 2 | PNAS (2) | — |
| Brainstorm | 1 | PNAS (1) | — |
| CIVET | 1 | PNAS (1) | — |


## Discovery signals: packages outside the dictionary

Most-cited GitHub repositories in the corpus. These are candidates for extending the
dictionary — detection is dictionary-bounded, so this is where its blind spots show.

| GitHub repository | Papers |
|---|---|
| FelixKrueger/TrimGalore | 37 |
| alexdobin/STAR | 21 |
| cortex-lab/phy | 19 |
| stschiff/sequenceTools | 19 |
| bulik/ldsc | 16 |
| broadinstitute/picard | 15 |
| lh3/bwa | 15 |
| macs3-project/MACS | 13 |
| MouseLand/Kilosort | 13 |
| samtools/samtools | 12 |
| jstjohn/SeqPrep | 12 |
| PacificBiosciences/pbmm2 | 12 |
| lh3/minimap2 | 12 |
| nicolaroberts/hdp | 11 |
| lh3/seqtk | 11 |
| satijalab/seurat | 11 |
| kevinblighe/EnhancedVolcano | 10 |
| tseemann/snippy | 10 |
| nanoporetech/medaka | 9 |
| swolock/scrublet | 9 |
| simonhmartin/genomics_general | 9 |
| TransDecoder/TransDecoder | 9 |
| sokrypton/ColabFold | 9 |
| immunogenomics/harmony | 8 |
| lmcinnes/umap | 8 |
| broadinstitute/inferCNV | 8 |
| deepmind/alphafold | 8 |
| pysam-developers/pysam | 7 |
| PacificBiosciences/ccs | 7 |
| chris-mcginnis-ucsf/DoubletFinder | 7 |
| aidenlab/Juicebox | 7 |
| AllenInstitute/scrattch.hicat | 7 |
| DReichLab/ADNA-Tools | 7 |
| rrwick/Filtlong | 7 |
| evogytis/baltic | 7 |
| BenLangmead/bowtie2 | 7 |
| rambaut/figtree | 7 |
| helenginn/mabscape | 7 |
| PacificBiosciences/IsoSeq | 6 |
| nanoporetech/dorado | 6 |


## Cross-check against an independent source

Europe PMC's own full-text search over the same six journals and years, compared with
this survey's counts. The two measure different things: EPMC searches the **whole**
article including its reference list, so a paper that merely *cites* a tool counts
there but not here. EPMC also searches articles this survey could not parse. Its
numbers are therefore an upper bound, and a ratio below 1 is expected and healthy —
a ratio near or above 1 would suggest this survey is over-counting.

| Package | This survey | EPMC full-text hits | Ratio |
|---|---|---|---|
| FreeSurfer | 116 | 131 | 0.89 |
| fMRIPrep | 34 | 38 | 0.89 |
| MRtrix3 | 12 | 12 | 1.00 |
| FSL | 114 | 114 | 1.00 |
| Seurat | 767 | 1,241 | 0.62 |
| GROMACS | 249 | 305 | 0.82 |
| DESeq2 | 886 | 1,446 | 0.61 |
| Scanpy | 200 | 317 | 0.63 |
| Bowtie2 | 477 | 657 | 0.73 |
| AlphaFold | 1,197 | 1,162 | 1.03 |
| RELION | 466 | 670 | 0.70 |
| PyMOL | 700 | 1,117 | 0.63 |
| Nextflow | 45 | 80 | 0.56 |
| Snakemake | 54 | 102 | 0.53 |


## Files

| File | Contents |
|---|---|
| `data/papers.tsv` | One row per paper: identifiers, packages used, full pipeline string |
| `data/paper_software.tsv` | One row per (paper × package): version, stage, **evidence sentence** |
| `data/package_index.tsv` | One row per package: paper count, journals, versions, typical stages |
| `data/pipelines.jsonl` | Per-paper pipeline stages and per-package evidence, machine-readable |
| `data/gap_list.tsv` | Every research article that could not be read, with the reason |
| `packages/<name>.md` | Per-package page: every paper using it, with version and pipeline |
| `scripts/` | The harvest, extraction and report code, to re-run or extend the survey |


**For the next step (finding bugs that affect these papers), start at
`packages/<name>.md`.** It gives, per package, the papers at risk and the **specific version
each reported**, so a bug can be matched against the version range actually used.


## Method

1. **Corpus.** Europe PMC queried by **ISSN** for the six journals, 2021–2026, so sibling
   titles (*Nature Communications*, *Science Advances*, *Cell Reports*) are excluded — a
   journal-name search would have pulled them in.
2. **Filtering.** News, editorials, comments, letters and corrections removed by publication
   type and title pattern, leaving research articles.
3. **Full text.** `fullTextXML` fetched per article and parsed as XML (not regexed over raw
   markup); Methods located by section title and `sec-type`.
4. **Detection.** A curated dictionary of **286 packages (496 name variants)** across 13 domains.
   Names colliding with ordinary language require a disambiguating context match: `STAR` must
   look like the aligner rather than *Cell*'s “STAR Methods”; `MUSCLE` the aligner, not tissue;
   `Fiji` the image suite, not the country; `Salmon` the quantifier, not the fish; `R` must
   appear with a version or an `R Core Team` citation. Detection runs over Methods first, then
   the rest of the body, because tools are also named in figure legends and data-availability
   statements.
5. **Pipelines.** The sentence naming each tool is classified into analysis stages (quality
   control, trimming, alignment, variant calling, quantification, normalisation, registration,
   clustering, statistical testing, simulation, structure determination, machine learning,
   visualisation) and ordered canonically.
6. **Licence.** Proprietary tools (MATLAB, Imaris, VASP and similar) are detected but excluded
   from open-source counts and never reported as OSS.


## Limitations

- **23,697 research articles could not be read** (`data/gap_list.tsv`). Roughly a third of these
  are indexed in Europe PMC but serve no full-text XML; the rest are paywalled outright.

- **Detection is dictionary-bounded.** Packages not in the dictionary are missed. GitHub,
  Zenodo, CRAN, Bioconductor and RRID signals are captured to expose that tail, but a survey
  of one-off custom tools this is not.

- **Supplementary methods are not fetched.** Many papers put full Methods in a PDF supplement
  outside the JATS body; tools named only there are missed.

- **Stage classification is heuristic.** It reads the one sentence naming the tool, so a tool
  described across several sentences may get an incomplete stage list. The evidence sentence
  is included in every row precisely so this can be checked.

- **Presence ≠ dependence.** A named package may have produced one supplementary figure rather
  than the central result. Read the evidence sentence before concluding a bug matters.

- **Some names denote a method or a database as often as a program.** UMAP, GSEA and
  AlphaFold are recorded whenever named, but a paper may mean the algorithm, a published
  embedding, or the AlphaFold Protein Structure Database rather than a run of the software.
  AlphaFold is the one package whose cross-check ratio exceeds 1, which is the signature of
  exactly this effect — treat its count as an upper bound.

- **A version is recorded only when it is stated adjacent to the package name** —
  `STAR (v2.7.5c)`, `Seurat v5.0.1`, `R version 4.1.2`. Where a paper separates the two
  (`AFNI, http://... ) software (v.23.1.06)`) the version field is left empty rather than
  guessed, because binding the wrong number would mismatch a bug's affected range in the
  next step. 26% of usage records carry a version; for the rest, the evidence sentence is
  in `data/paper_software.tsv` and often contains it.

- **Counts are of papers, not of runs.** A paper naming a package once and a paper built
  entirely on it both count as 1.
