#!/bin/bash
# extension: all remaining SCHZ with a rest scan, and spare CONTROLs until 20 more have passed
R=/home/user/reho-pilot
nohup bash $R/scripts/janitor_ext.sh >> $R/janitor.log 2>&1 &
nohup bash $R/scripts/janitor2_ext.sh >> $R/janitor2.log 2>&1 &
passedC() { tail -n +2 $R/subjects_ext.tsv | awk -F'\t' '$2=="CONTROL"{print $1}' | while read s; do [ -f $R/proc/$s.results/reho_postfix+tlrc.HEAD ] && echo $s; done | wc -l; }
tail -n +2 $R/subjects_ext.tsv | while IFS=$'\t' read SUB GRP; do
  grep -qx "$SUB" $R/deferred.txt 2>/dev/null && { echo "$(date +%H:%M) $SUB deferred"; continue; }
  [ -f $R/proc/$SUB.results/reho_postfix+tlrc.HEAD ] && continue
  grep -qx "$SUB" $R/excluded.txt && continue
  [ $GRP = CONTROL ] && [ $(passedC) -ge 20 ] && continue
  $R/scripts/run_subject.sh $SUB > $R/proc_$SUB.log 2>&1 || echo "FAILED $SUB"
  echo "$(date +%H:%M) $SUB $(grep -c '^DONE sub-' $R/proc_$SUB.log) passedC=$(passedC)"
done
echo "EXT DONE"
