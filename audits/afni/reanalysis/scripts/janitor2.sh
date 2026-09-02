#!/bin/bash
# remove directories of subjects whose run failed (FATAL in log, no reho output, not currently running)
R=/home/user/reho-pilot
while true; do
  for log in $R/proc_sub-*.log; do
    s=$(basename $log .log); s=${s#proc_}
    [ -f $R/proc/$s.results/reho_postfix+tlrc.HEAD ] && continue
    grep -q "FATAL ERROR" $log || continue
    pgrep -f "run_subject.sh $s" >/dev/null && continue
    rm -rf $R/proc/$s.results $R/data/$s $R/proc/proc.$s $R/proc/output.proc.$s && echo "$(date +%H:%M) removed failed $s"
  done
  grep -q "BATCH2 DONE" $R/batch2.log 2>/dev/null && exit 0
  sleep 120
done
