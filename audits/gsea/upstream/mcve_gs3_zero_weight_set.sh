#!/bin/bash
# GS3 MCVE: a gene set whose members all have ranking score 0 gets a spurious ES/NES under the default weighted scheme.
# 40 genes: 5 positive (3.0 .. 1.0), 15 zeros, 20 negative (-0.1 .. -2.0); set ZEROS = 12 of the zero-scored genes,
# set BOTTOM = the 5 most negative genes as a control.  Expected for ZEROS: no defined ES (N_R = 0), or a warning,
# or the classic value +0.8214 (5 misses of 1/28, then 12 hits of 1/12); got: ES = -5/28 = -0.1786 with NES and p.
# Usage: GSEA_CLI="path/to/gsea-cli.sh" ./mcve_gs3_zero_weight_set.sh
set -e
D=$(mktemp -d /tmp/gsea_mcve_XXXX)
{ for i in $(seq 1 5); do printf 'p%d\t%s\n' $i $(python3 -c "print(3.0 - 0.5*($i-1))"); done
  for i in $(seq 1 15); do printf 'z%d\t0\n' $i; done
  for i in $(seq 1 20); do printf 'n%d\t%s\n' $i $(python3 -c "print(-0.1*$i)"); done; } > $D/list.rnk
{ printf 'ZEROS\tna'; for i in $(seq 1 12); do printf '\tz%d' $i; done; printf '\n'
  printf 'BOTTOM\tna\tn16\tn17\tn18\tn19\tn20\n'; } > $D/sets.gmt
GSEA_CLI=${GSEA_CLI:-"java -Djava.awt.headless=true -cp /tmp/gseawork/src/build/libs/gsea-minimal-user.jar:/tmp/gseawork/src/modules/* xtools.gsea.GseaPreranked"}
for scheme in weighted classic; do
  $GSEA_CLI -rnk $D/list.rnk -gmx $D/sets.gmt -collapse No_Collapse -scoring_scheme $scheme -set_min 5 -set_max 40 \
      -nperm 1000 -rnd_seed 149 -plot_top_x 0 -make_sets false -zip_report false -gui false -out $D -rpt_label $scheme > $D/$scheme.log 2>&1
  echo "$scheme:"; cat $D/$scheme.GseaPreranked.*/gsea_report_for_na_*_*.tsv | cut -f1,4,5,6,7,8,10 | grep -v '^NAME' | grep -v '^$' | sed 's/^/  /'
done
