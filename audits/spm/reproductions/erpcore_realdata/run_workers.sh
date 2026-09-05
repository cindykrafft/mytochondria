#!/bin/bash
# run_workers.sh TASK NWORKERS -- distributes subjects (from TASK_files.tsv) across background workers
TASK=$1; N=$2
subs=$(cut -f1 ${TASK}_files.tsv | sort -n | uniq)
for w in $(seq 0 $((N-1))); do
  ( i=0; for s in $subs; do if [ $((i % N)) = $w ]; then ./run_subject.sh $TASK $s; fi; i=$((i+1)); done; echo "WORKER $w DONE $(date)" ) > logs/${TASK}_w$w.log 2>&1 &
done
echo "launched $N workers for $TASK"
