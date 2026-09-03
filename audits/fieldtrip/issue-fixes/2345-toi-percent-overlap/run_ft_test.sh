#!/bin/bash
# usage: run_ft_test.sh <fieldtrip-tree> <testname>; prints a RESULT PASS/FAIL line (Octave 8.4)
T=$1; N=$2; A=$(dirname $0)/../../verify   # shims: verify/shims + verify/pull2610-octave
F=$(dirname $0)/ftrun_$$.m   # run from a directory that is NOT the FieldTrip root (its private/ dir confuses Octave)
cat > $F <<M
warning('off','all'); pkg load statistics signal
addpath('$A/shims'); addpath('$A/pull2610-octave');
addpath('$T'); ft_defaults; addpath('$T/test'); addpath('$T/external/signal/dpss_hack');
warning('off','all'); set(0,'DefaultFigureVisible','off');
try
  $N;
  printf('RESULT %s PASS\n', '$N');
catch e
  msg = strrep(strtrim(e.message), char(10), ' ');
  printf('RESULT %s FAIL: %s\n', '$N', msg(1:min(end,220)));
end
M
timeout 900 octave-cli --no-gui -q $F 2>&1 | grep "^RESULT" || echo "RESULT $N FAIL: timeout/crash"
rm -f $F
