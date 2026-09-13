#!/bin/bash
# GS2 MCVE: with -set_min equal to -set_max the gene set size filter is skipped.
# A 30-gene list and three sets of sizes 5, 10 and 20; -set_min 10 -set_max 10 should analyse SIZE10 only.
# Got: all three analysed; and a set with an identifier absent from the list makes the run fail.
# Usage: GSEA_CLI="path/to/gsea-cli.sh" ./mcve_gs2_set_min_equals_max.sh
D=$(mktemp -d /tmp/gsea_mcve_XXXX)
for i in $(seq 1 30); do printf 'g%d\t%d\n' $i $((31 - i)); done > $D/list.rnk
{ printf 'SIZE5\tna'; for i in $(seq 1 5); do printf '\tg%d' $i; done; printf '\n'
  printf 'SIZE10\tna'; for i in $(seq 1 10); do printf '\tg%d' $i; done; printf '\n'
  printf 'SIZE20\tna'; for i in $(seq 6 25); do printf '\tg%d' $i; done; printf '\n'; } > $D/sets.gmt
{ cat $D/sets.gmt; printf 'SIZE10_ABSENT\tna'; for i in $(seq 11 20); do printf '\tg%d' $i; done; printf '\tNOT_IN_LIST\n'; } > $D/sets_absent.gmt
GSEA_CLI=${GSEA_CLI:-"java -Djava.awt.headless=true -cp /tmp/gseawork/src/build/libs/gsea-minimal-user.jar:/tmp/gseawork/src/modules/* xtools.gsea.GseaPreranked"}
run() { $GSEA_CLI -rnk $D/list.rnk -gmx $1 -collapse No_Collapse -scoring_scheme weighted -set_min $2 -set_max $3 \
      -nperm 10 -rnd_seed 149 -plot_top_x 0 -make_sets false -zip_report false -gui false -out $D -rpt_label $4 > $D/$4.log 2>&1
      if ls $D/$4.GseaPreranked.*/gsea_report_for_na_pos_*.tsv > /dev/null 2>&1; then
        echo "$4 (-set_min $2 -set_max $3): analysed $(cut -f1 $D/$4.GseaPreranked.*/gsea_report_for_na_*_*.tsv | grep -v '^NAME' | grep -v '^$' | sort | tr '\n' ' ')"
      else echo "$4 (-set_min $2 -set_max $3): FAILED: $(grep -m1 -o 'Exception.*' $D/$4.log)"; fi; }
run $D/sets.gmt 10 11 control
run $D/sets.gmt 10 10 equal
run $D/sets_absent.gmt 10 10 equal_absent
