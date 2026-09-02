#!/bin/bash
# top-up: run spare subjects until 20 have passed per group
R=/home/user/reho-pilot
passed() { grep -P "\t$1$" $R/subjects.tsv $R/subjects_spare.tsv | cut -d: -f2 | cut -f1 | while read s; do [ -f $R/proc/$s.results/reho_postfix+tlrc.HEAD ] && echo $s; done | wc -l; }
while IFS=$'\t' read SUB GRP; do
  [ $(passed $GRP) -ge 20 ] && continue
  [ -f $R/proc/$SUB.results/reho_postfix+tlrc.HEAD ] && continue
  grep -qx "$SUB" $R/excluded.txt && continue
  $R/scripts/run_subject.sh $SUB > $R/proc_$SUB.log 2>&1 || echo "FAILED $SUB"
  echo "$(date +%H:%M) $SUB passed: CONTROL $(passed CONTROL) SCHZ $(passed SCHZ)"
done < $R/subjects_spare.tsv
echo "BATCH2 DONE: CONTROL $(passed CONTROL) SCHZ $(passed SCHZ)"
