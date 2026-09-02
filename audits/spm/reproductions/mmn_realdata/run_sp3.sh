#!/bin/bash
S=/tmp/claude-0/-home-user-afni/d65df75e-7d82-531d-babc-bc1cc192b046/scratchpad; F=/home/user/spmfork
for VER in prefix merged; do
  if [ $VER = prefix ]; then git -C $F show 530ec52:@meeg/badsamples.m > $F/@meeg/badsamples.m; else git -C $F show upstream/main:@meeg/badsamples.m > $F/@meeg/badsamples.m; fi
  echo "=== $VER: badsamples fixed-form lines: $(grep -c 'nsamples(this)-1' $F/@meeg/badsamples.m) === $(date)"
  cd $S/mmn && octave --no-gui --quiet --eval "
  addpath('$S/octshim'); addpath('$F'); pkg load signal; spm('defaults','eeg'); spm_jobman('initcfg');
  TAG='$VER'; run('$S/mmn/sp3_pipeline.m');
  " 2>&1 | grep -v "^warning: \(function\|which\|implicit\|range\)\|shadows\|creating layout\|^$" | grep -E "^\[|event values|epoched|error|Error|called from|^    |Completed|Elapsed"
done
git -C $F checkout -q -- @meeg/badsamples.m
echo "=== SP3 DONE $(date) ==="
