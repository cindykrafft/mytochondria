#!/bin/bash
# GS1 MCVE: weighted_p1.5 gives a wrong ES for a gene set with members on the negative side.
# Twelve genes scored 6..1, -1..-6; the set {g, i, k} has scores -1, -3, -5.
# Expected ES (P_hit with |r|^1.5 weights): -0.7202 at rank 7 (gene h); got: -1.0000.
# Usage: GSEA_CLI="path/to/gsea-cli.sh" ./mcve_gs1_weighted_p15.sh   (default: the jar built from the audited commit)
set -e
D=$(mktemp -d /tmp/gsea_mcve_XXXX)
printf 'a\t6\nb\t5\nc\t4\nd\t3\ne\t2\nf\t1\ng\t-1\nh\t-2\ni\t-3\nj\t-4\nk\t-5\nl\t-6\n' > $D/list.rnk
printf 'NEG_SPREAD\tna\tg\ti\tk\n' > $D/set.gmt
GSEA_CLI=${GSEA_CLI:-"java -Djava.awt.headless=true -cp /tmp/gseawork/src/build/libs/gsea-minimal-user.jar:/tmp/gseawork/src/modules/* xtools.gsea.GseaPreranked"}
for scheme in weighted_p1.5 weighted_p2; do
  $GSEA_CLI -rnk $D/list.rnk -gmx $D/set.gmt -collapse No_Collapse -scoring_scheme $scheme -set_min 3 -set_max 12 \
      -nperm 10 -rnd_seed 149 -plot_top_x 0 -make_sets false -zip_report false -gui false -out $D -rpt_label $scheme > $D/$scheme.log 2>&1
  echo "$scheme: $(cut -f1,4,5 $D/$scheme.GseaPreranked.*/gsea_report_for_na_neg_*.tsv | sed -n 2p | tr '\t' ' ')   (NAME SIZE ES)"
done
