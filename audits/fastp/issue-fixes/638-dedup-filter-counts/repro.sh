#!/usr/bin/env bash
# Reproduction for OpenGene/fastp #638 / #528: with --dedup, the report's
# "reads passed filter" / filtering_result.passed_filter_reads counts the reads
# that --dedup removed, so it disagrees with summary.after_filtering.total_reads
# and with the output file; in --merge mode --dedup removes nothing.
# Usage: repro.sh <path-to-fastp>   (synthetic data, no external files)
set -euo pipefail
FASTP=${1:-./fastp}
W=$(mktemp -d)
python3 - "$W" <<'PY'
import random, sys
w=sys.argv[1]; random.seed(638)
def rc(s): return s.translate(str.maketrans('ACGT','TGCA'))[::-1]
# SE: 2000 distinct 100-nt reads, each written twice -> 4000 reads, 50 % duplicates
reads=[''.join(random.choice('ACGT') for _ in range(100)) for _ in range(2000)]
with open(f'{w}/se.fq','w') as f:
    for tag in ('', '_dup'):
        for i,s in enumerate(reads): f.write(f'@r{i}{tag}\n{s}\n+\n{"I"*100}\n')
# PE: 1000 distinct overlapping pairs (120-nt insert, 2x100), each written twice
with open(f'{w}/pe1.fq','w') as f1, open(f'{w}/pe2.fq','w') as f2:
    for tag in ('a','b'):
        for i in range(1000):
            random.seed(1000+i); ins=''.join(random.choice('ACGT') for _ in range(120))
            f1.write(f'@p{i}{tag}/1\n{ins[:100]}\n+\n{"I"*100}\n'); f2.write(f'@p{i}{tag}/2\n{rc(ins)[:100]}\n+\n{"I"*100}\n')
PY
COMMON="-A -G -Q -L"
echo "fastp: $($FASTP --version 2>&1)"
show() { python3 - "$1" <<'PY'
import json,sys; j=json.load(open(sys.argv[1])); fr=j['filtering_result']
print(f"  filtering_result.passed_filter_reads = {fr['passed_filter_reads']}")
print(f"  filtering_result.duplicated_reads    = {fr.get('duplicated_reads','(absent)')}")
print(f"  summary.after_filtering.total_reads  = {j['summary']['after_filtering']['total_reads']}")
PY
}
echo "== SE, 4000 reads (2000 distinct), --dedup"
$FASTP $COMMON --dedup -i $W/se.fq -o $W/se.out.fq -j $W/se.json -h $W/se.html 2> $W/se.log
grep -E 'reads passed filter|reads failed due to duplication|Duplication rate' $W/se.log | sed 's/^/  stderr: /'
show $W/se.json; echo "  reads written to output      = $(( $(wc -l < $W/se.out.fq) / 4 ))"
echo "== PE, 2000 pairs (1000 distinct), --dedup"
$FASTP $COMMON --dedup -i $W/pe1.fq -I $W/pe2.fq -o $W/pe1.out.fq -O $W/pe2.out.fq -j $W/pe.json -h $W/pe.html 2> $W/pe.log
grep -E 'reads passed filter|reads failed due to duplication|Duplication rate' $W/pe.log | sed 's/^/  stderr: /'
show $W/pe.json; echo "  pairs written to output      = $(( $(wc -l < $W/pe1.out.fq) / 4 ))"
echo "== PE, same pairs, --merge --dedup"
$FASTP $COMMON --dedup -i $W/pe1.fq -I $W/pe2.fq --merge --merged_out $W/mg.fq -j $W/mg.json -h $W/mg.html 2> $W/mg.log
grep -E 'reads passed filter|reads failed due to duplication|Duplication rate|Read pairs merged' $W/mg.log | sed 's/^/  stderr: /'
show $W/mg.json; echo "  merged reads written         = $(( $(wc -l < $W/mg.fq) / 4 ))  (1000 distinct pairs)"
rm -rf "$W"
