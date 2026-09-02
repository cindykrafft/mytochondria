#!/bin/bash
R=/home/user/reho-pilot
tail -n +2 $R/subjects.tsv | cut -f1 | while read SUB; do
  [ -f $R/proc/$SUB.results/reho_postfix+tlrc.HEAD ] && continue
  grep -qx "$SUB" $R/excluded.txt && continue
  $R/scripts/run_subject.sh $SUB > $R/proc_$SUB.log 2>&1 || echo "FAILED $SUB"
  echo "$(date +%H:%M) $SUB $(grep -c "^DONE sub-" $R/proc_$SUB.log)"
done
echo "BATCH DONE"
