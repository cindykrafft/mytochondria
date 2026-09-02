#!/bin/bash
# Group-level comparison of pre-fix vs post-fix 3dReHo on the ds000030 pilot.
# 1) per-subject summary (errts SD, mean ReHo pre/post, relative error, spatial correlation)
# 2) SCZ vs CONTROL two-sample t-test on ReHo maps under each binary (3dttest++), same mask
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64 OMP_NUM_THREADS=4
cd $R/proc; mkdir -p $R/group
printf "subject\tgroup\terrts_sd\treho_pre\treho_post\trel_err_mean\trel_err_max\tspatial_corr\tcensored_frac\n" > $R/group/subjects_summary.tsv
PRE_C=""; PRE_S=""; POST_C=""; POST_S=""
while IFS=$'\t' read SUB GRP; do
  d=$SUB.results; [ -f $d/reho_postfix+tlrc.HEAD ] || continue
  M=$d/mask_epi_anat.$SUB+tlrc
  3dcalc -overwrite -a $d/reho_prefix+tlrc -b $d/reho_postfix+tlrc -m $M -expr 'm*abs(a-b)/b' -prefix $d/relerr >/dev/null 2>&1
  sd=$(3dBrickStat -mask $M -mean $d/errts_sd+tlrc); pre=$(3dBrickStat -mask $M -mean $d/reho_prefix+tlrc); post=$(3dBrickStat -mask $M -mean $d/reho_postfix+tlrc)
  rem=$(3dBrickStat -mask $M -mean $d/relerr+tlrc); rex=$(3dBrickStat -mask $M -max $d/relerr+tlrc)
  sc=$(python3 $R/scripts/masked_corr.py $M $d/reho_prefix+tlrc $d/reho_postfix+tlrc)
  cf=$(1deval -a $d/censor_${SUB}_combined_2.1D -expr '1-a' | 3dTstat -mean -prefix - 1D:stdin\' 2>/dev/null | tail -1)
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" $SUB $GRP $sd $pre $post $rem $rex "$sc" "$cf" >> $R/group/subjects_summary.tsv
  if [ $GRP = CONTROL ]; then PRE_C="$PRE_C $d/reho_prefix+tlrc"; POST_C="$POST_C $d/reho_postfix+tlrc"; else PRE_S="$PRE_S $d/reho_prefix+tlrc"; POST_S="$POST_S $d/reho_postfix+tlrc"; fi
done < $R/subjects.tsv
# common group mask: voxels inside every subject's EPI-anat mask
3dmask_tool -overwrite -input $(ls */mask_epi_anat.*+tlrc.HEAD) -frac 1.0 -prefix $R/group/group_mask >/dev/null 2>&1
for arm in pre post; do
  if [ $arm = pre ]; then SA="$PRE_S"; SB="$PRE_C"; else SA="$POST_S"; SB="$POST_C"; fi
  3dttest++ -overwrite -prefix $R/group/ttest_${arm} -mask $R/group/group_mask+tlrc -setA SCZ $SA -setB CONTROL $SB -labelA SCZ -labelB CONTROL >/dev/null 2>&1
done
cd $R/group
for arm in pre post; do
  n=$(3dBrickStat -mask group_mask+tlrc -count -non-zero -abs ttest_${arm}+tlrc'[1]' 2>/dev/null); 
  echo "$arm: group-mask voxels $(3dBrickStat -count -non-zero group_mask+tlrc) | |t|>3.55 (p<.001 two-sided, df 38) voxels: $(3dcalc -a ttest_${arm}+tlrc'[1]' -expr 'step(abs(a)-3.55)' -prefix - 2>/dev/null | 3dBrickStat -count -non-zero - 2>/dev/null)"
done
3dcalc -overwrite -a ttest_pre+tlrc'[1]' -b ttest_post+tlrc'[1]' -m group_mask+tlrc -expr 'm*(a-b)' -prefix t_diff >/dev/null 2>&1
echo "t-map spatial correlation pre vs post: $(python3 $R/scripts/masked_corr.py group_mask+tlrc "ttest_pre+tlrc[1]" "ttest_post+tlrc[1]")"
echo "mean |t_pre - t_post| in mask: $(3dcalc -a t_diff+tlrc -expr 'abs(a)' -prefix - 2>/dev/null | 3dBrickStat -mask group_mask+tlrc -mean - 2>/dev/null)"
