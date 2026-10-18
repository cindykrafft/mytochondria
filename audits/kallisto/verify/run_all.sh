#!/bin/sh
# Runs one harness on every build; writes <harness>.<version>.out next to it.
# usage: sh run_all.sh t1_tpm_efflen.py
S=/tmp/claude-0/-home-user-research-software-audit/51868b87-edac-5181-aac9-af38332c9ac8/scratchpad/audit-kallisto
export KHARNESS_TMP=$S/runs; mkdir -p $KHARNESS_TMP
here=$(dirname "$0")
h=$1
for b in ${BUILDS:-} "$S/master-4e9f29c/build/src/kallisto:master" "$S/v0.51.1/build/src/kallisto:v0.51.1" "$S/v0.50.1/build/src/kallisto:v0.50.1" "$S/rel/v0.52.0/x/kallisto/kallisto:release-0.52.0" "$S/rel/v0.51.1/x/kallisto/kallisto:release-0.51.1" "$S/rel/v0.50.1/x/kallisto/kallisto:release-0.50.1" "$S/rel/v0.48.0/x/kallisto/kallisto:v0.48.0" "$S/rel/v0.46.1/x/kallisto/kallisto:v0.46.1"; do
  bin=${b%%:*}; tag=${b##*:}
  [ -x "$bin" ] || continue
  if [ "$tag" = master ]; then out="$here/${h%.py}.out"; else out="$here/${h%.py}.$tag.out"; fi
  python3 -I "$here/$h" "$bin" > "$out" 2>&1
  echo "$tag: $(tail -1 "$out")"
done
