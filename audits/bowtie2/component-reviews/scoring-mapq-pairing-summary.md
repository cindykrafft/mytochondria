# Bowtie 2 — scoring, MAPQ, pair classification and the alignment summary

_Read on `BenLangmead/bowtie2` `master` @ `58e34bf` (2026-09-24, VERSION 2.5.5, one commit past
the 2.5.4 release tag range: 41ee86b "Add support for MQ:i SAM flag" of 2026-09-14 is unreleased);
executed on that build and on the release binaries 2.3.5.1, 2.4.2, 2.4.5, 2.5.1 and 2.5.4 from the
GitHub release archives. Every number below comes from a harness in `../verify/` whose captured
output sits next to it (`.out` for the master build, `.v<version>.out` for the releases,
`.patched.out` for the fixes)._

Files read: `scoring.h/.cpp` (penalty tables, `perfectScore`), `simple_func.h` (`--score-min`,
`--n-ceil` evaluation), `unique.h/.cpp` (the three MAPQ calculators; V2 is the default),
`pe.h/.cpp` (`peClassifyPair`, `otherMate`), `aligner_result.h/.cpp` (`setFragmentLength`,
`getExtendedCoords`, `RedundantAlns`, `AlnSetSumm`), `aln_sink.h/.cpp` (`ReportingState`,
`finishRead`, `selectByScore`, `prepareDiscordants`, `reportHits`, `printAlSumm`),
`sam.cpp` (`printAlignedOptFlags`), `aligner_sw_driver.cpp` (mate rescue and the reporting of
anchor and opposite-mate alignments), `pat.cpp/.h` (`-3/-5`, `--trim-to`), and
`MANUAL.markdown` for the documented behaviour.

## Findings

### BW1 — mate 2's MAPQ is computed with its own length in place of mate 1's (master only, since 41ee86b)

`AlnSinkSam::reportHits` (`aln_sink.h:1359-1380`, introduced by 41ee86b when the MAPQ was moved
out of `appendMate` so it could also be printed as the mate's `MQ:i`) calls the calculator for
mate 1 with `rd1->length()` and `rd2->length()`, and for mate 2 with

```cpp
itoa10<TMapq>(mapq.mapq(summ, *flags2, rd2->mate < 2,
                        rd2->length(),
                        rd2 == NULL ? 0 : rd2->length(),   // should be rd1
                        mapqInps2), buf2);
```

`BowtieMapq2::mapq` (`unique.h:171-`) sums the perfect score and the minimum score over both
mates of a concordant pair (`scPer += sc_.perfectScore(ordlen)`, `scMin += scoreMin_.f(ordlen)`),
so mate 2's MAPQ is now computed as if the pair were two copies of mate 2. Before 41ee86b
`appendMate` passed `rdo == NULL ? 0 : rdo->length()`, the opposite read.

Effect (`m1_mapq.py`, concordant pairs, end-to-end unless stated; the port of `BowtieMapq2`
reproduces every value once mate 2's length is fed twice):

| pair | AS mate1 / mate2 | XS | MAPQ mate 1 | MAPQ mate 2 (master) | mate 2 on 2.3.5.1–2.5.4 |
|---|---|---|---|---|---|
| 150/50 bp, 3 + 2 mismatches, unique | −18 / −12 | — | 40 | **23** | 40 |
| 150/75 bp, 4 + 1 mismatches, unique | −24 / −6 | — | 40 | **24** | 40 |
| 150/50 bp in a two-copy repeat (6 substitutions), 1 + 1 mismatches | −6 / −6 | −24 / −24 | 17 | **16** | 17 |
| 150/60 bp in a two-copy repeat (2 substitutions), perfect | 0 / 0 | −6 / −6 | 6 | **30** | 6 |
| local, 150/50 bp in a repeat, 1 + 1 mismatches | 292 / 92 | 268 / 68 | 14 | **21** | 14 |
| local, 150/60 bp in a repeat, perfect | 300 / 120 | 292 / 112 | 11 | **14** | 11 |

Equal-length pairs are unaffected (the two sums coincide). Mates of unequal length are the
norm after adapter/quality trimming (Cutadapt, Trimmomatic, Trim Galore and fastp precede
Bowtie 2 in 119, 90, 61 and 33 cohort papers), so once released this would make the two mates of the same
concordant pair pass or fail a MAPQ filter differently, in both directions. Fix:
`0001-Use-the-opposite-mate-s-length-when-computing-mate-2.patch` (one token); on the patched
build every pair in the table gives both mates the same value as the port
(`m1_mapq.patched.out`).

### BW2 — a mate reported as an unpaired alignment never carries `XS:i` (every version)

`SamConfig::printAlignedOptFlags` (`sam.cpp:148-170`):

```cpp
if(flags.partOfPair()) {
    sco = summ.bestUnchosenPScore(rd.mate < 2);
} else {
    sco = summ.bestUnchosenUScore();
}
```

For a mate that is reported as an unpaired alignment (`YT:Z:UP`: the pair aligned neither
concordantly nor discordantly) `AlnSinkWrap::finishRead` builds the summary from the mate's
unpaired alignments alone, `summ1.init(rd1_, NULL, NULL, NULL, &rs1u_, NULL, ...)`
(`aln_sink.cpp:1058-1060`), and `selectByScore(&rs1u_, NULL, ...)` fills only
`bestUnchosenUScore` (`aln_sink.cpp:1483` + the `rs2 == NULL` branch at +132); the paired
second-best fields stay invalid. `flags.partOfPair()` is still true for such a mate, so `XS:i`
is omitted. The MAPQ for the same record goes through `AlnSetSumm::bestUnchosenScore(mate1)`
(`aligner_result.h:1866`), which returns the unpaired second-best when the summary is not
paired, so the record gets MAPQ 0 or 1 and the summary counts it under "aligned >1 times",
while the tag that most pipelines use to recognise a multi-mapper is absent.

`a1_summary_arithmetic.py`, 30 pairs whose mate 1 lies in an exact 2-kb duplication and whose
mate 2 is unalignable: mate 1 is reported `YT:Z:UP`, MAPQ 1, summary "30 aligned >1 times",
`XS:i` present on 0 of 30 — on 2.3.5.1, 2.4.2, 2.4.5, 2.5.1, 2.5.4 and master; 30 of 30 with
`0001-Report-XS-i-for-mates-aligned-as-unpaired-alignments.patch`, which replaces the branch
with `summ.bestUnchosenScore(rd.mate < 2)`. Concordant and discordant pairs are unaffected
(their summaries are paired and `XS:i` is present, `a1` "conc_dup" rows). A "uniquely mapped"
definition of "no `XS:i` tag" (the cohort's survey sentences speak of "uniquely mapped/aligned" reads or an XS filter in 27
Bowtie 2 papers and of a MAPQ threshold in 60) therefore keeps every
multi-mapping mate of a pair whose other mate failed.

### BW3 — `--no-mixed` also suppresses discordant alignments; the manual says the opposite (every version)

`MANUAL.markdown`, `--no-mixed`: "By default, when bowtie2 cannot find a concordant or
discordant alignment for a pair, it then tries to find alignments for the individual mates.
This option disables that behavior." `--no-discordant` is the separate option for discordant
alignments, and "Mixed mode" says `--no-mixed` "will only consider alignment status of pairs
per se".

In the code a discordant alignment is assembled from the mates' unpaired alignments
(`AlnSinkWrap::prepareDiscordants`, `aln_sink.cpp:1466`: `rs1u_.size() == 1 &&
rs2u_.size() == 1`), and unpaired alignments are only sought and reported while
`ReportingState::doneUnpaired(mate)` is false; `ReportingState::nextRead` (`aln_sink.cpp:39-48`)
sets `doneUnpair1_ = doneUnpair2_ = !p_.mixed` at the start of every pair. With `--no-mixed`
the driver's `if(!msink->state().doneUnpaired(anchor1))` guards (`aligner_sw_driver.cpp:2517,
2563`) are never entered, no unpaired alignment is stored, and no discordant pair can be
formed.

`a1_summary_arithmetic.py`, 80 pairs built to be discordant (50 with a 5-kb fragment, 30 with
both mates forward): default run — 80 `YT:Z:DP`, summary "80 (42.11%) aligned discordantly 1
time"; `--no-mixed` — 0 `YT:Z:DP`, both mates unaligned (`YT:Z:UP`, FLAG 77/141), summary "0
(0.00%) aligned discordantly 1 time", overall alignment rate 58.00 % instead of 82.00 %. Same on
every build. In the cohort's survey sentences `--no-mixed` appears in 24 papers, `--no-discordant` in 20;
of the 20 sentences that name `--no-mixed`, 18 also name `--no-discordant` (where the
behaviour is what the user asked for) and 2 use `--no-mixed` alone. Either the code
or the manual should change; the kit files this as a report and leaves the choice to the
maintainers.

### BW4 — pairs whose fragment is a little longer than `-X` get a mate with a spurious insertion instead of its exact alignment (every version)

Mechanism, from `aligner_sw_driver.cpp` and `pe.cpp`. When the anchor mate has aligned, the
opposite mate is looked for by dynamic programming inside the window that `-I/-X` allow
(`PairedEndPolicy::otherMate`, `pe.cpp`: the right edge is `off + maxfrag - 1`, widened by the
number of gaps the minimum score permits). A fragment that is longer than `-X` by less than
that gap allowance still has its opposite mate partly inside the window, and the DP finds the
best alignment *that fits*: the read's last bases are pushed into an insertion (`94M2I4M`,
`91M5I4M`, ..., `82M12I6M`) so that the alignment ends at the window edge. The pair is then
correctly rejected as non-concordant by `peClassifyPair`, but the gapped mate alignment has
already been reported as the mate's unpaired alignment (`redMate2_.add(r2)`;
`msink->report(0, NULL, r2)`, `aligner_sw_driver.cpp:2423-2445`). When the mate's own seed
search later finds the exact, gap-free alignment starting at the same reference position, it
is dropped as redundant: `RedundantAlns::overlap` (`aligner_result.cpp`) declares two
alignments redundant when they share any (reference offset, read offset) cell, and the 94
matched bases of the gapped alignment are the same cells as the first 94 of the exact one
(`if(!red.overlap(r)) { red.add(r); msink->report(...) }`, `aligner_sw_driver.cpp:2524-2531`
and `2569-2576`). The pair is finally reported as discordant, with the gapped mate.

`x1_maxins_boundary.py` (100-bp mates, exact copies of a random reference, ten pairs per
fragment length; every gap is therefore spurious):

| `-X` | fragment lengths with a gapped mate | share of pairs in that band | example CIGAR / AS / MAPQ | `|TLEN|` reported | clean again from |
|---|---|---|---|---|---|
| 500 (default) | 520, 525, 530 | 10/10 at each | `91M5I4M` / −32 / 40; `87M7I6M` / −50 / 23; `84M12I4M` / −41 / 24 | 513–518 | 535 |
| 500, `--very-sensitive` | 520, 525, 530 | 10/10, 10/10, 9/10 | `94M2I4M` / −29 / 40 ... `82M12I6M` / −53 / 23 | 516–530 | 535 |
| 300 | 320, 325, 330 | 10/10, 10/10, 8/10 | `94M2I4M` / −29 / 40 ... | 316–318 | 335 |
| 500, `--no-discordant` | 520–530 | 29/30 mates | same CIGARs, `YT:Z:UP`, MAPQ 23 / 3 / 0 | 0 | 535 |
| 500, `--no-mixed` | 520–530 | 29/30 mates | same | 516–518 | 535 |
| 500, `--local` | none | 0 | (the DP soft-clips instead) | true length | — |

Identical on 2.3.5.1, 2.4.2, 2.4.5, 2.5.1, 2.5.4 and master. Fragments 505–515 are clean
(they fit the widened window without gaps) and fragments from about `X + 35` on are clean (no
alignment fits, so the exact one is the first reported); the affected band is roughly
`X + 18 .. X + 33` for 100-bp reads at the default scoring, and every pair in it is affected.
The gapped alignments have `XS:i` absent and MAPQ 23–42, i.e. they pass the usual filters.

`x2_maxins_realistic_library.py`, 6,000 pairs of 100-bp mates with fragment lengths
~N(380, 70) at the default `-X 500`: 50 of 12,000 mates (0.42 %) are reported with a 2–12-bp
insertion (MAPQ 23 ×17, 24 ×17, 40 ×12, 42 ×4), the 50 pairs' `|TLEN|` are 517–518 instead of
519–531, and the same reads at `-X 1000` have no gap and exact TLENs. For an indel caller this
is a clean-read library reporting 50 false insertions, all within 20 bp of a read end, all at
fragment lengths in a narrow band above `-X`; for fragment-size analyses the tail above `-X`
is compressed to `X + 18`. A fix needs a decision the maintainers should make (do not report
the rescue alignment as an unpaired alignment when the pair is not concordant, or let
`RedundantAlns` prefer the better-scoring of two alignments that share cells); the kit files
the report with the reproduction and the mechanism and offers to prepare a PR once the shape
is agreed.

### N1 — `-X` bounds the mapped extent; `TLEN` includes outer soft clips by default (note)

`setFragmentLength` uses `getExtendedCoords`, which adds the soft-trimmed bases back unless
`--soft-clipped-unmapped-tlen` is given (`aligner_result.h:893-910, 1311-1343`, with the
comment "We take all clipping, both hard and soft, into account here"); `peClassifyPair`
receives `refExtent()`, the aligned reference span (`aligner_sw_driver.cpp:2378-2397`).
`p1_pair_constraints.py` block 8: `--local`, 20 non-genomic bases on the 5' end of each mate,
mapped outer distance 480, `-X 500` → concordant, `TLEN` ±520; with
`--soft-clipped-unmapped-tlen` ±480. Block 7: mapped distance 170, clipped distance 210,
`-I 200` → not concordant although `TLEN` says 210. The option is documented; that `-I/-X`
are checked on a different length from the one `TLEN` reports is not, and the SAM
specification defines `TLEN` from the mapped bases. Recorded as a note; the tracker has
prior discussion of soft clips in `TLEN` (#180, #346, read in full, see the kit README).

### N2 — `-I/-X` with `-3/-5` are applied to the trimmed mates; the manual says "untrimmed" (note)

`MANUAL.markdown` for `-I` and `-X`: "If trimming options -3 or -5 are also used, the -I
constraint is applied with respect to the untrimmed mates". `pat.cpp` hard-trims the read
before alignment (`r.patFw.trimEnd(pp_.trim3)`, `trimmed5/trimmed3` on the `Read`) and the
aligner's `setShape` calls pass `pretrim5p = pretrim3p = 0` (`aligner_sw.cpp:465-467`,
`aligner_sw_driver.cpp:1210-1212, 1953-1955`), so neither the classifier nor `TLEN` sees the
trimmed bases. `p1_pair_constraints.py` block 4: fragment 520 with `-3 20 -5 20` and `-X 500`
→ concordant, `TLEN` ±480; fragment 230 with `-I 200` → not concordant (`DP`, `TLEN` ±190).
Block 5: `--trim-to 5:80` on a 540 fragment → concordant, `TLEN` ±500 (outer 20 bp of each mate
dropped). Same on every build. Documentation report.

### N3 — the local-mode `--score-min` threshold is truncated toward zero (note)

`SimpleFunc::f<T>` (`simple_func.h`) returns `(T)ret`; the default local function
`G,20,8` gives 56.84 at L = 100 and the threshold applied is 56. `s1_scoring_tags.py`: a 100-bp
read whose best local alignment is 28 matching bases (score 56) is reported (`28M72S`,
`AS:i:56`), 27 bases (54) is not. In end-to-end mode the truncation of a negative value makes
no difference for integer scores. One score unit; documentation-level.

## Held up under execution

- **Scoring and tags** (`s1_scoring_tags.py`, 24 reads × 13 configurations on all six builds):
  `AS:i` recomputed from the manual's penalty formulas (quality-scaled mismatch
  `MN + floor((MX−MN)·min(Q,40)/40)` including Q > 40 and Q = 0, `--ignore-quals`, `--mp 7,1`,
  `--mp 4`, `--np 3` with `--n-ceil`, `--rdg 8,2 --rfg 4,4`, `--phred64`, local `--ma 3`,
  `--very-sensitive[-local]`), `XM/XO/XG/NM/MD/CIGAR/POS` from the construction (mismatches, N
  bases, 1–5-bp insertions and deletions placed where the alignment is unambiguous): 24/24
  everywhere.
- **MAPQ** (`m1_mapq.py`): the port of `BowtieMapq2` (with the single-precision threshold
  constants) reproduces every unpaired MAPQ over eight repeat families × five mismatch counts
  × two qualities in end-to-end and local mode, L = 50/100/150, `--mp 4,2`, and the presets
  (576 aligned reads per build); and every concordant pair's MAPQ on the releases.
- **Pair classification** (`p1_pair_constraints.py` blocks 1–3): the port of `peClassifyPair`
  matches concordance and `TLEN` for fragment lengths across `-I 200 -X 500` (150–1200),
  `--fr/--rf/--ff` on FR/RF/FF pairs, and separate / overlapping / contained / identical /
  dovetailed mates under the defaults, `--no-overlap`, `--no-contain` and `--dovetail`.
- **Summary arithmetic** (`a1_summary_arithmetic.py`, 400 pairs + 200 unpaired reads of six
  classes): every line of the summary and the overall alignment rate agree with counts taken
  from the SAM in the default mode, `--no-discordant`, `--no-mixed`, both, and `-k 2` (given
  BW2, the "mates aligned >1 times" line is checked against MAPQ rather than `XS:i`);
  `--un-conc` = pairs aligned concordantly 0 times, `--al-conc` = the rest, `--un/--al`
  likewise (record counts of the written FASTQ files).

## Withdrawn suspicions

- `unp_sec[11][11]` (MAPQ V3) is not used by default (`mapqv = 2`); not audited.
- The `XS:i` for concordant mates is the per-mate paired second-best, the MAPQ uses the pair
  sum; that is a design choice and both are internally consistent (port matches).
- `printPct` (the summary percentages) is plain double arithmetic; no rounding issue.
