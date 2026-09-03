#!/bin/bash
# Run the DPABI-analogous pipeline over dpabi/subjects_dpabi.tsv, skipping finished subjects; failed dirs are removed.
R=/home/user/reho-pilot; L=$R/dpabi/batch.log
tail -n +2 $R/dpabi/subjects_dpabi.tsv | while IFS=$'\t' read SUB GRP; do
  [ -f $R/dpabi/proc/$SUB.results/szreho_postfix+tlrc.HEAD ] && continue
  grep -qx "$SUB" $R/dpabi/excluded.txt 2>/dev/null && continue
  rm -rf $R/dpabi/proc/$SUB.results $R/dpabi/proc/proc.$SUB $R/dpabi/proc/output.proc.$SUB
  bash $R/dpabi/run_subject_dpabi.sh $SUB > $R/dpabi/proc_$SUB.log 2>&1
  if grep -q "^DONE $SUB" $R/dpabi/proc_$SUB.log; then echo "$(date +%H:%M) $SUB $(tail -1 $R/dpabi/proc_$SUB.log | awk '{print $3}')" >> $L
  else echo "$(date +%H:%M) FAILED $SUB" >> $L; echo $SUB >> $R/dpabi/excluded.txt; echo "$SUB	pipeline failure: $(grep -m1 -E 'FATAL|DOWNLOAD FAILED|ERROR' $R/dpabi/proc_$SUB.log | cut -c1-120)" >> $R/dpabi/excluded_reasons.tsv; rm -rf $R/dpabi/proc/$SUB.results $R/dpabi/proc/proc.$SUB $R/dpabi/proc/output.proc.$SUB $R/data/$SUB; fi
done
echo "$(date +%H:%M) DPABI BATCH DONE" >> $L
