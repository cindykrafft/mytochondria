#!/bin/bash
# run_subject.sh TASK SUB  -- runs stage A (if needed) + stage B under both builds
S=/tmp/claude-0/-home-user-afni/d65df75e-7d82-531d-babc-bc1cc192b046/scratchpad; R=$S/erpcore
TASK=$1; SUB=$2
for BUILD in prefix merged; do
  if [ $BUILD = prefix ]; then F=/home/user/spm_prefix; else F=/home/user/spmfork; fi
  [ -f $R/results/$TASK/$(printf 'sub%02d' $SUB)_$BUILD.mat ] && continue
  cd $R && octave --no-gui --quiet --eval "
  addpath('$S/octshim'); addpath('$F'); pkg load signal; spm('defaults','eeg'); spm_jobman('initcfg');
  SUB=$SUB; TASK='$TASK'; BUILD='$BUILD'; ROOT='$R'; run('$R/erpcore_pipeline.m');
  " 2>&1 | grep -v "^warning: \(function\|which\|implicit\|range\)\|shadows\|creating layout\|^$" | grep -E "^\[|error|Error|called from|^    " | sed "s/^/[$TASK $SUB $BUILD] /"
done
