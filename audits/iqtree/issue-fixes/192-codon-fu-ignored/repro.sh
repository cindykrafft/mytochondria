#!/bin/sh
# Reproduction for iqtree/iqtree3 issue #192: +FU{...} silently ignored for GY-type codon models.
# Usage: IQTREE3=/path/to/iqtree3 sh repro.sh [workdir]
# Prints, for each model string, the log-likelihood, the model name and the number of free
# parameters from the .iqtree report. On unpatched master both +FU runs give the same value
# as GY+F (empirical frequencies, 60 free parameters); with the fix they differ and report GY+FU, 0.
set -e
IQ=${IQTREE3:-iqtree3}; D=$(cd "$(dirname "$0")" && pwd); W=${1:-$(mktemp -d)}; cd "$W"
for spec in "skew:$(cat $D/codon_freq.txt)" "uniform:$(cat $D/codon_freq_uniform.txt)"; do
  name=${spec%%:*}; F=${spec#*:}
  $IQ -s $D/codon.fa -st CODON -te $D/codon.tree -blfix -m "GY{0.8,1.07}+FU{$F}" --prefix fu_$name -T 1 -redo -quiet >/dev/null 2>&1
  echo "GY+FU($name):  $(grep -m1 'Log-likelihood of the tree' fu_$name.iqtree | cut -d'(' -f1) | $(grep -m1 'Model of substitution' fu_$name.iqtree) | $(grep -m1 'Number of free parameters' fu_$name.iqtree | sed 's/.*: //') free parameters"
done
for m in "GY{0.8,1.07}+F3X4" "GY{0.8,1.07}+F" "MG{0.8}+F3X4"; do
  $IQ -s $D/codon.fa -st CODON -te $D/codon.tree -blfix -m "$m" --prefix ctl -T 1 -redo -quiet >/dev/null 2>&1
  echo "$m:  $(grep -m1 'Log-likelihood of the tree' ctl.iqtree | cut -d'(' -f1) | $(grep -m1 'Model of substitution' ctl.iqtree) | $(grep -m1 'Number of free parameters' ctl.iqtree | sed 's/.*: //') free parameters"
done
