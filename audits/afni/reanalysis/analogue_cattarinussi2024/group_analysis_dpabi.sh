#!/bin/bash
# Group analysis for the DPABI-analogous pipeline (PLAN.md): SCZ vs HC on smoothed z-ReHo from each build,
# 3dttest++ -Clustsim cluster inference, between-build overlap, and scoring against Cattarinussi 2024's regions.
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64 OMP_NUM_THREADS=4
G=$R/dpabi/group; P=$R/dpabi/proc; mkdir -p $G; bs(){ 3dBrickStat "$@" | xargs; }
: > $G/list_CONTROL.txt; : > $G/list_SCHZ.txt; : > $G/motion_excluded.txt
tail -n +2 $R/dpabi/subjects_dpabi.tsv | while IFS=$'\t' read SUB GRP; do
  d=$P/$SUB.results; [ -f $d/szreho_postfix+tlrc.HEAD ] || continue
  if grep -q EXCLUDE $d/motion_flag.txt; then echo "$SUB $GRP" >> $G/motion_excluded.txt; else echo $d >> $G/list_$GRP.txt; fi
done
nC=$(wc -l < $G/list_CONTROL.txt); nS=$(wc -l < $G/list_SCHZ.txt); echo "CONTROL $nC SCHZ $nS motion-excluded $(wc -l < $G/motion_excluded.txt)"
MASKS=$(cat $G/list_CONTROL.txt $G/list_SCHZ.txt | while read d; do s=$(basename $d .results); echo $d/mask_epi_anat.$s+tlrc.HEAD; done)
3dmask_tool -overwrite -input $MASKS -frac 0.9 -prefix $G/mask90 >/dev/null 2>&1
df=$((nC+nS-2)); tcrit=$(python3 -c "from scipy.stats import t; print(round(t.ppf(0.9995,$df),3))")
echo $tcrit > $G/tcrit.txt; echo "== mask90: $(bs -count -non-zero $G/mask90+tlrc) voxels; df $df; |t| for p<.001 = $tcrit"
for arm in prefix postfix hist; do
  SA=$(sed "s|$|/szreho_${arm}+tlrc|" $G/list_SCHZ.txt); SB=$(sed "s|$|/szreho_${arm}+tlrc|" $G/list_CONTROL.txt)
  C=$G/clust_$arm; mkdir -p $C/tmp; cd $C
  3dttest++ -overwrite -prefix tt -mask $G/mask90+tlrc -setA $SA -setB $SB -labelA SCZ -labelB CONTROL -Clustsim 4 -prefix_clustsim cs -tempdir tmp > ttest.log 2>&1
  3dcalc -overwrite -a tt+tlrc'[1]' -expr "step(abs(a)-$tcrit)" -prefix supra >/dev/null 2>&1
  echo "$arm: |t|>$tcrit: $(bs -count -non-zero supra+tlrc) (SCZ<HC $(3dcalc -overwrite -a tt+tlrc'[1]' -expr "step(-a-$tcrit)" -prefix neg >/dev/null 2>&1; bs -count -non-zero neg+tlrc), SCZ>HC $(3dcalc -overwrite -a tt+tlrc'[1]' -expr "step(a-$tcrit)" -prefix pos >/dev/null 2>&1; bs -count -non-zero pos+tlrc))"
  for PP in 0.001 0.01; do
    K=$(awk -v p=$PP '$1==p{print $7}' cs.CSimA.NN1_bisided.1D)
    3dClusterize -overwrite -inset tt+tlrc -ithr 1 -idat 0 -mask $G/mask90+tlrc -NN 1 -bisided p=$PP -clust_nvox $K -pref_map clmap_p$PP > clusters_p$PP.txt 2>/dev/null
    n=$(bs -max clmap_p$PP+tlrc 2>/dev/null); [ -z "$n" ] && n=0
    echo "$arm p=$PP: threshold $K, surviving clusters $n"
    grep -vE '^#' clusters_p$PP.txt | awk 'NF>=16{printf "   %s vox, mean %s, peak RAI (%s %s %s)\n",$1,$11,$14,$15,$16}'
  done
done
cd $G; A=clust_prefix; B=clust_postfix
echo "t-map corr prefix vs postfix: $(python3 $R/scripts/masked_corr.py mask90+tlrc "$A/tt+tlrc[1]" "$B/tt+tlrc[1]")"
echo "sign flips: $(3dcalc -overwrite -a $A/tt+tlrc'[1]' -b $B/tt+tlrc'[1]' -m mask90+tlrc -expr 'm*step(-a*b)' -prefix sf >/dev/null 2>&1; bs -count -non-zero sf+tlrc) of $(bs -count -non-zero mask90+tlrc)"
echo "overlap |t|>$tcrit (and/or): $(3dcalc -overwrite -a $A/supra+tlrc -b $B/supra+tlrc -expr 'a*b' -prefix oa >/dev/null 2>&1; 3dcalc -overwrite -a $A/supra+tlrc -b $B/supra+tlrc -expr 'step(a+b)' -prefix oo >/dev/null 2>&1; bs -count -non-zero oa+tlrc) / $(bs -count -non-zero oo+tlrc)"
for PP in 0.001 0.01; do [ -f $A/clmap_p$PP+tlrc.HEAD ] && [ -f $B/clmap_p$PP+tlrc.HEAD ] && echo "corrected-cluster overlap p=$PP (and/or): $(3dcalc -overwrite -a $A/clmap_p$PP+tlrc -b $B/clmap_p$PP+tlrc -expr 'step(a)*step(b)' -prefix ca >/dev/null 2>&1; 3dcalc -overwrite -a $A/clmap_p$PP+tlrc -b $B/clmap_p$PP+tlrc -expr 'step(a+b)' -prefix co >/dev/null 2>&1; bs -count -non-zero ca+tlrc) / $(bs -count -non-zero co+tlrc)"; done
python3 $R/dpabi/score_targets.py
echo "DPABI GROUP DONE"
