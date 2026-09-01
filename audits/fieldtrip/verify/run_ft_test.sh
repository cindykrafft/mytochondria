#!/bin/bash
# usage: run_ft_test.sh <fieldtrip-tree> <testname> ; prints PASS/FAIL line
T=$1; N=$2; S=/tmp/claude-0/-home-user-afni/dc02da2d-922b-53f2-854f-a80f44735787/scratchpad/ft-verify
cat > /tmp/ftrun_$$.m <<M
pkg load statistics signal
addpath('$T'); ft_defaults; addpath('$T/test'); addpath('$T/external/signal/dpss_hack'); addpath('$S/corrshim');
warning('off','all'); set(0,'DefaultFigureVisible','off');
try
  $N;
  printf('RESULT %s PASS\n', '$N');
catch e
  msg = strrep(strtrim(e.message), char(10), ' ');
  printf('RESULT %s FAIL: %s\n', '$N', msg(1:min(end,220)));
end
M
timeout 1500 octave-cli --no-gui -q /tmp/ftrun_$$.m 2>&1 | grep "^RESULT" || echo "RESULT $N FAIL: timeout/crash"
rm -f /tmp/ftrun_$$.m
