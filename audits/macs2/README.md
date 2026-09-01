# MACS2 audit against 475 published papers (2021–2026)

_Fourth survey-driven audit (FreeSurfer, FSL, DESeq2, → MACS2). Generated 2026-09-01._

## What this is

The six-journal survey found **475 papers** using MACS2/MACS3 for peak calling.
Each paper's full text was re-mined for how it called peaks
(`macs2_profiles.jsonl`: data type, invocation modes, downstream use), and the
statistical core of **MACS2 2.2.7.1** — the version papers pin most — was read
in full (~8,000 lines of Cython/Python), with findings cross-checked against
MACS 1.4.3 (2008), MACS2 2.1.1 and current MACS3, and reproduced end-to-end on
the shipped MACS3 3.0.4 binary.

## How the papers use it

| Usage | Papers |
|---|---|
| ChIP-seq / ATAC-seq / scATAC / CUT&RUN | 199 / 181 / 72 / 48 |
| input control mentioned / explicit no-control | 32 / 2 |
| --nomodel / shift+extsize / BAMPE | 49 / 38 / 41 |
| summits / broad peaks / keep-dup | 64 / 26 / 26 |
| peaks → DESeq2/edgeR / DiffBind / IDR | 43 / 28 / 12 |

Most ATAC/CUT&RUN papers run without a control — the code path where the
local-lambda machinery is at its thinnest and the background λ at its lowest.

## Findings (details in `component-reviews/callpeak-core.md`)

**MC1 — CONFIRMED, in every version from 2.1.x through current MACS3,
reproduced on shipped 3.0.4: `--keep-dup auto` filters the control with the
treatment's duplicate threshold.** The control-specific binomial threshold is
computed, logged, and ignored. Demonstration: log prints "binomial = 3" for
the control, then filters it at 1 — 10,000 of 60,000 control reads removed
that the logged threshold would keep. Fires when depths differ ~5–10×
(shallow ChIP vs deep input); distorts local lambda exactly at
high-duplication loci. One-word fix, filed with reproduction.

**MC2 — CONFIRMED 17-year convention note: MACS p-values are P(X > t), one
probability atom smaller than the textbook P(X ≥ t).** At the default
cutoff this admits 2× (λ=25) to 14× (λ=0.5) the nominal null rate — largest
in sparse-background ATAC/CUT&RUN. Identical since MACS 1.4, so results are
mutually consistent across versions; reported as a definition/documentation
issue with exact tables.

**MC3 — CONFIRMED latent: the 2.x cythonization dropped an initialization**
in the large-λ lower-tail Poisson (`cdf` summed from C stack garbage; MACS
1.4 had it right; MACS3 zero-fills but still omits the first term).
Unreachable from the CLI in 2.x — a landmine, not an active bias.

**Notes** (quantified, below materiality): scaled treatment pileup floor()ed
before the Poisson while control λ stays float (conservative half-count when
treatment is scaled down — the default direction); broadPeak output silently
empty for chromosomes with only weak-level regions; q-value ties ranked
conservatively; model fragment length off by ~1 bp from a lag-axis
indexing mismatch.

**Withdrawn during review**: two summit-gating defect candidates
(whole-peak discard and summit-list truncation) turned out to be unreachable
with the single scoring criterion `callpeak` always uses — raised, traced,
and disproven before write-up.

## What held up

The ATAC `--shift/--extsize` arithmetic is exact on both strands; the
local-lambda max-of-windows model is faithful to the paper; the pileup
algorithm's independent sorting trick is mathematically valid; duplicate
filtering, scaling direction, the log-space Poisson series, and the
peak-model pairing checks all verified clean.

## Files

| File | Contents |
|---|---|
| `macs2_profiles.jsonl` / `macs2_profile.py` | 475 papers × usage features; the miner |
| `component-reviews/callpeak-core.md` | full review with file:line evidence |
| `verify/keepdup_demo.py` | MC1 end-to-end reproduction (runs against macs3) |
| `verify/keepdup_thresholds.py` | binomial threshold table (when MC1 fires) |
| `verify/tail_convention.py` | MC2 exact null-rate tables |

## Filing route

`macs3-project/MACS` is on GitHub with issues and PRs open. MC1 is a
one-word PR (`control_max_dup_tags`) plus companion issue with the
reproduction; MC2 is a documentation issue; MC3 a small cleanup PR.
