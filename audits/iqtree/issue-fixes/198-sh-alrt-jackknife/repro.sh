#!/bin/bash
# iqtree/iqtree3 #198: SH-aLRT values change when the jackknife (-j/-J) is requested.
# Usage: ./repro.sh <iqtree3 binary> <outdir>
# Simulates a 24-taxon JC alignment (800 sites) with AliSim, then runs -alrt 1000 three times on
# it with the same seed: alone, with UFBoot (-bb 1000) and with UFJack (--ufjack 1000).
# The SH-aLRT values (first number of each "SH/UF" label) should not depend on that choice.
set -e
B=$(readlink -f "$1"); OUT=$2; mkdir -p "$OUT"; cd "$OUT"
[ -f sim.phy ] || "$B" --alisim sim -t "RANDOM{yh/24}" -m JC --length 800 --seed 1 -redo -quiet
for tag in none bb jack; do
  case $tag in bb) X="-bb 1000";; jack) X="--ufjack 1000";; none) X="";; esac
  "$B" -s sim.phy -m JC -alrt 1000 $X -T 1 -seed 7 --prefix run_$tag -redo -quiet
done
echo "binary: $("$B" --version | head -1)"
for tag in none bb jack; do
  printf "%-5s lnL %s  SH-aLRT: " $tag "$(grep -m1 'BEST SCORE' run_$tag.log | grep -o '[-0-9.]*$')"
  grep -o ')[0-9.]*' run_$tag.treefile | tr -d ')' | tr '\n' ' '; echo
done
