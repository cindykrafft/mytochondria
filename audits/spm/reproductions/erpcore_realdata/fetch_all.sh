#!/bin/bash
# sequential download of ERP CORE raw files listed in <TAG>_files.tsv, with retries; skips complete files
TAG=$1; mkdir -p raw_$TAG
while IFS=$'\t' read -r sub name size url; do
  out=raw_$TAG/$name
  for try in 1 2 3 4 5; do
    if [ -f "$out" ] && [ "$(stat -c %s "$out")" = "$size" ]; then break; fi
    curl -sS -L --retry 3 -o "$out" "${url}?direct" || sleep 20
  done
  [ "$(stat -c %s "$out" 2>/dev/null)" = "$size" ] && echo "ok $name" || echo "FAIL $name"
done < ${TAG}_files.tsv
echo "DONE $TAG $(date)"
