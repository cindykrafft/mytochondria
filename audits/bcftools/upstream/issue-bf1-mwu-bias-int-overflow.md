Title: mpileup: MQBZ/BQBZ/RPBZ/SCBZ are computed with 32-bit accumulators and under-report bias once a quality bin holds 1291 reads

<!-- samtools/bcftools has no issue template (.github/ contains only workflows), so
     this follows the order of the samtools Bug_report.md template: versions,
     environment, then steps/command/output. -->

#### Are you using the latest version of bcftools and HTSlib? If not, please specify.

Yes: `develop` @ `7abcc0d` built against HTSlib `develop` @ `e503e04`
(`bcftools 7abcc0d / Using htslib 1.24-1-ge503e04`). The 1.24 release and 1.13, built
from their tags, give the same output.

#### Please describe your environment.

- OS: Linux 6.18 (Ubuntu 24.04 container), `uname -sr`: Linux 6.18.44
- machine architecture: x86_64
- compiler: gcc 13.3.0

#### Please specify the steps taken to generate the issue, the command you are running and the relevant output.

`calc_mwu_biasZ()` (`bam2bcf.c:817`) computes the tie-corrected Mann-Whitney Z behind
`INFO/MQBZ`, `BQBZ`, `RPBZ`, `SCBZ`, `MQSBZ` and `NMBZ`. The tie correction is built at
`bam2bcf.c:846-847`:

```c
            int p = a[i]+b[i];
            t += (p*p-1)*p;  // adjustment score for ties
```

`t` is `int64_t`, but `(p*p-1)*p` is evaluated in `int`. `p` is the number of reads in one
quality (or position) bin, so the term is cubic in that bin's depth and leaves the range
of a 32-bit `int` at **p = 1291** (1290³ = 2146689000 ≤ INT32_MAX < 1291³ = 2151685171).
`t` is subtracted inside `var2` at `bam2bcf.c:859`, so a wrapped (smaller) `t` inflates
`var2` and shrinks the reported |Z|. Wrapping a positive product can only lower it, so
the error is one-directional: **a site with a real bias is annotated as less biased than
it is, never more.**

The bins are per site, not per sample — `bcf_callaux_clean()` is called once per position
(`mpileup.c:580`, `:593`) after all input files are processed — and `bam2bcf.c:492-493`
clamps MQ and BQ to 59, so with an aligner that gives MQ 60 to most reads, bin 59 holds
almost the whole pileup. The threshold in practice is *1291 reads at the site*: about 30
samples at 100×, 44 samples at 30× WGS, or one deep amplicon/mitochondrial pileup.

Reproduction — two pileups at one mapping-quality-biased site, differing only in the
number of reference reads:

```sh
printf '>ref\n' > ref.fa
awk 'BEGIN{for(i=0;i<200;i++)printf "A"; print ""}' >> ref.fa

for nref in 1140 1400; do
    printf '@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:ref\tLN:200\n' > in.sam
    awk -v nref=$nref 'BEGIN{
        for(i=0;i<50;i++){ref=ref "A"; q=q "I"}
        alt=substr(ref,1,24) "C" substr(ref,26)
        for(i=1;i<=nref;i++) printf "r%d\t0\tref\t76\t60\t50M\t*\t0\t0\t%s\t%s\n",i,ref,q
        for(i=1;i<=60;i++)   printf "a%d\t0\tref\t76\t60\t50M\t*\t0\t0\t%s\t%s\n",i,alt,q
        for(i=1;i<=40;i++)   printf "b%d\t0\tref\t76\t30\t50M\t*\t0\t0\t%s\t%s\n",i,alt,q
    }' >> in.sam
    printf 'reads at ref:100 = %d   ' $((nref + 100))
    bcftools mpileup -f ref.fa -d 100000 in.sam 2>/dev/null |
        awk -F'\t' '$2==100 {n=split($8,a,";"); for(i=1;i<=n;i++) if(a[i]~/^MQBZ=/) print a[i]}'
done
```

Both sites have exactly the same bias: 100 alt reads of which 40 are at MQ 30, against
reference reads all at MQ 60. Expected — the tie-corrected Mann-Whitney Z, which
`scipy.stats.mannwhitneyu(..., method='asymptotic', use_continuity=False)` also gives:

```
reads at ref:100 = 1240   MQBZ=-21.6984
reads at ref:100 = 1500   MQBZ=-23.9783
```

Got:

```
reads at ref:100 = 1240   MQBZ=-21.6984
reads at ref:100 = 1500   MQBZ=-5.75778
```

Shrinking the example showed the condition is exactly one bin reaching 1291 reads:
p = 1290 is right to 4 decimal places and p = 1291 is wrong (−36.0077 becomes −7.7068),
and adding reads to a *second* bin instead of the first never triggers it. Calling
`calc_mwu_biasZ()` directly out of the built object file over a sweep of 431 pileups
(1,300 to 200,000 reads at the site): 430 are wrong, in none of them is |Z| too large,
in none does it reach 0 or nan. Over 160 realistic pileups (total depth × alt fraction ×
fraction of alt reads at the lower MQ), 41 change their verdict under the `MQBZ < -3` cut
used in the calling workflow — for instance a 1,500-read site whose true MQBZ is −12.13
is annotated as −0.83, i.e. as unbiased.

The same function overflows in two more places at higher depth, fixed by the same change:
`m = na*nb / 2.0` (`bam2bcf.c:856`) and `(na*nb)/12.0` / `(na+nb)*(na+nb-1)`
(`bam2bcf.c:859`) are `int` products, and `e`/`l` (`bam2bcf.c:828`) are `int`
accumulators of quantities of order na·nb.

1.9 and 1.10.2 are not affected: they have no `calc_mwu_biasZ()` and emit the older
`MQB`/`BQB`/`RPB` p-values instead.

A patch making `e`, `l`, `na`, `nb` and `p` `int64_t`, with a `test/test-mwu.c` unit test
in the style of `test/test-rbuf` (it fails on unmodified `develop`) and a `NEWS` entry, is
ready and will follow as a PR.

Found in Mytochondria, a volunteer project that checks the numerical core of research software and verifies every finding by execution (methods and harnesses: https://github.com/cindykrafft/mytochondria/tree/main/audits/bcftools)

---
_Generated by [Claude Code](https://claude.ai/code)_
