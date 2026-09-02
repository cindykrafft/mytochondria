#!/bin/bash
# Group-level comparison of pre-fix vs post-fix 3dReHo on the ds000030 pilot.
# 1) per-subject summary (errts SD, mean ReHo pre/post, relative error, spatial correlation, censoring)
# 2) SCZ vs CONTROL two-sample t-test on ReHo maps under each binary (3dttest++), common mask
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64 OMP_NUM_THREADS=4
G=$R/group; mkdir -p $G; cd $R/proc
bs(){ 3dBrickStat "$@" | xargs; }
printf "subject\tgroup\terrts_sd\treho_pre\treho_post\trel_err_mean\trel_err_max\tspatial_corr\tcensor_frac\n" > $G/subjects_summary.tsv
PRE_C=""; PRE_S=""; POST_C=""; POST_S=""; MASKS=""
cat $R/subjects.tsv $R/subjects_spare.tsv | grep -v '^subject' | sort -u | while IFS=$'\t' read SUB GRP; do
  d=$SUB.results; [ -f $d/reho_postfix+tlrc.HEAD ] || continue
  M=$d/mask_epi_anat.$SUB+tlrc
  3dcalc -overwrite -a $d/reho_prefix+tlrc -b $d/reho_postfix+tlrc -m $M -expr 'm*abs(a-b)/b' -prefix $d/relerr >/dev/null 2>&1
  sd=$(bs -mask $M -mean $d/errts_sd+tlrc); pre=$(bs -mask $M -mean $d/reho_prefix+tlrc); post=$(bs -mask $M -mean $d/reho_postfix+tlrc)
  rem=$(bs -mask $M -mean $d/relerr+tlrc); rex=$(bs -mask $M -max $d/relerr+tlrc)
  sc=$(python3 $R/scripts/masked_corr.py $M $d/reho_prefix+tlrc $d/reho_postfix+tlrc)
  cf=$(grep 'censor fraction' $d/out.ss_review.$SUB.txt | awk -F: '{print $2}' | tr -d ' ')
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" $SUB $GRP $sd $pre $post $rem $rex "$sc" "$cf" >> $G/subjects_summary.tsv
done
# subject lists per group (from the summary, so only passed subjects)
for GRP in CONTROL SCHZ; do
  awk -F'\t' -v g=$GRP '$2==g{print $1}' $G/subjects_summary.tsv > $G/list_$GRP.txt
done
PRE_C=$(sed 's|$|.results/reho_prefix+tlrc|' $G/list_CONTROL.txt);  POST_C=$(sed 's|$|.results/reho_postfix+tlrc|' $G/list_CONTROL.txt)
PRE_S=$(sed 's|$|.results/reho_prefix+tlrc|' $G/list_SCHZ.txt);     POST_S=$(sed 's|$|.results/reho_postfix+tlrc|' $G/list_SCHZ.txt)
MASKS=$(cat $G/list_CONTROL.txt $G/list_SCHZ.txt | while read s; do echo $s.results/mask_epi_anat.$s+tlrc.HEAD; done)
# common group mask: voxels inside every passed subject's EPI-anat mask
3dmask_tool -overwrite -input $MASKS -frac 1.0 -prefix $G/group_mask >/dev/null 2>&1
nC=$(wc -l < $G/list_CONTROL.txt); nS=$(wc -l < $G/list_SCHZ.txt)
if [ $nC -ge 2 ] && [ $nS -ge 2 ]; then
  for arm in pre post; do
    if [ $arm = pre ]; then SA="$PRE_S"; SB="$PRE_C"; else SA="$POST_S"; SB="$POST_C"; fi
    3dttest++ -overwrite -prefix $G/ttest_${arm} -mask $G/group_mask+tlrc -setA SCZ $SA -setB CONTROL $SB -labelA SCZ -labelB CONTROL >/dev/null 2>&1
  done
  cd $G
  df=$((nC+nS-2)); tcrit=$(python3 -c "from scipy.stats import t; print(round(t.ppf(0.9995,$df),3))" 2>/dev/null || echo 3.55)
  echo "SCZ n=$nS, CONTROL n=$nC, df=$df, |t| threshold p<.001 two-sided = $tcrit; group-mask voxels $(bs -count -non-zero group_mask+tlrc)"
  for arm in pre post; do
    3dcalc -overwrite -a ttest_${arm}+tlrc'[1]' -expr "step(abs(a)-$tcrit)" -prefix supra_${arm} >/dev/null 2>&1
    3dcalc -overwrite -a ttest_${arm}+tlrc'[1]' -expr "step(abs(a)-1.96)" -prefix supra05_${arm} >/dev/null 2>&1
    echo "$arm: voxels |t|>$tcrit: $(bs -count -non-zero supra_${arm}+tlrc) ; |t|>1.96: $(bs -count -non-zero supra05_${arm}+tlrc)"
  done
  3dcalc -overwrite -a ttest_pre+tlrc'[1]' -b ttest_post+tlrc'[1]' -m group_mask+tlrc -expr 'm*abs(a-b)' -prefix t_absdiff >/dev/null 2>&1
  3dcalc -overwrite -a ttest_pre+tlrc'[0]' -b ttest_post+tlrc'[0]' -m group_mask+tlrc -expr 'm*abs(a-b)' -prefix d_absdiff >/dev/null 2>&1
  echo "t-map spatial correlation pre vs post: $(python3 $R/scripts/masked_corr.py group_mask+tlrc "ttest_pre+tlrc[1]" "ttest_post+tlrc[1]")"
  echo "mean-difference map (SCZ-CONTROL) spatial correlation pre vs post: $(python3 $R/scripts/masked_corr.py group_mask+tlrc "ttest_pre+tlrc[0]" "ttest_post+tlrc[0]")"
  echo "mean |t_pre - t_post| in mask: $(bs -mask group_mask+tlrc -mean t_absdiff+tlrc)"
  echo "sign disagreements of t (pre vs post): $(3dcalc -overwrite -a ttest_pre+tlrc'[1]' -b ttest_post+tlrc'[1]' -m group_mask+tlrc -expr 'm*step(-a*b)' -prefix signflip >/dev/null 2>&1; 3dBrickStat -count -non-zero signflip+tlrc)"
  echo "overlap of |t|>$tcrit sets (pre∩post / pre∪post): $(3dcalc -overwrite -a supra_pre+tlrc -b supra_post+tlrc -expr 'a*b' -prefix ov_and >/dev/null 2>&1; 3dcalc -overwrite -a supra_pre+tlrc -b supra_post+tlrc -expr 'step(a+b)' -prefix ov_or >/dev/null 2>&1; echo "$(bs -count -non-zero ov_and+tlrc) / $(bs -count -non-zero ov_or+tlrc)")"
else
  echo "not enough subjects per group for the contrast (CONTROL $nC, SCHZ $nS)"
fi
cat $G/subjects_summary.tsv
