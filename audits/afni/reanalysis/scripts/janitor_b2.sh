#!/bin/bash
# prune finished subject dirs to the files the group analysis needs; never touch a dir without reho_postfix
R=/home/user/reho-pilot
while true; do
  for d in $R/proc/sub-*.results; do
    [ -f $d/reho_postfix+tlrc.HEAD ] || continue
    [ -f $d/.pruned ] && continue
    sub=$(basename $d .results)
    find $d -mindepth 1 -maxdepth 1 ! -name 'reho_pre*' ! -name 'reho_post*' ! -name 'mask_epi_anat.*' ! -name 'errts_sd*' ! -name 'censor_*' ! -name 'dfile_rall.1D' ! -name 'motion_*enorm*' ! -name 'out.ss_review*' ! -name 'relerr*' -exec rm -rf {} +
    rm -rf $R/data/$sub; touch $d/.pruned; echo "$(date +%H:%M) pruned $sub $(du -sh $d | cut -f1)"
  done
  grep -q "BATCH2 DONE" $R/batch2.log 2>/dev/null && exit 0
  sleep 60
done
