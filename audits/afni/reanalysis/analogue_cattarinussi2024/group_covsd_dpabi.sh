#!/bin/bash
# Post-hoc follow-up 2 (not pre-specified): same test with each subject's residual SD (the quantity the pre-fix defect depends on) as a covariate, prefix and postfix arms.
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64 OMP_NUM_THREADS=4
G=$R/dpabi/group; bs(){ 3dBrickStat "$@" | xargs; }
{ echo "subj errsd"; for d in $(cat $G/list_SCHZ.txt $G/list_CONTROL.txt); do s=$(basename $d .results); echo "$s $(3dBrickStat -mask $d/mask_epi_anat.$s+tlrc -mean $d/errts_sd+tlrc | xargs)"; done; } > $G/cov_sd.txt
tcrit=$(cat $G/tcrit.txt)
for arm in prefix postfix; do
  SA=$(for d in $(cat $G/list_SCHZ.txt); do s=$(basename $d .results); echo "$s $d/szreho_${arm}+tlrc"; done); SB=$(for d in $(cat $G/list_CONTROL.txt); do s=$(basename $d .results); echo "$s $d/szreho_${arm}+tlrc"; done)
  C=$G/clustcovsd_$arm; mkdir -p $C/tmp; cd $C
  3dttest++ -overwrite -prefix tt -mask $G/mask90+tlrc -setA SCZ $SA -setB CONTROL $SB -covariates $G/cov_sd.txt -Clustsim 4 -prefix_clustsim cs -tempdir tmp > ttest.log 2>&1
  echo "$arm (residual-SD covariate): |t|>$tcrit: $(3dcalc -overwrite -a tt+tlrc'[1]' -expr "step(abs(a)-$tcrit)" -prefix supra >/dev/null 2>&1; bs -count -non-zero supra+tlrc)"
  for PP in 0.001 0.01; do
    K=$(awk -v p=$PP '$1==p{print $7}' cs.CSimA.NN1_bisided.1D)
    3dClusterize -overwrite -inset tt+tlrc -ithr 1 -idat 0 -mask $G/mask90+tlrc -NN 1 -bisided p=$PP -clust_nvox $K -pref_map clmap_p$PP > clusters_p$PP.txt 2>/dev/null
    n=$(bs -max clmap_p$PP+tlrc 2>/dev/null); [ -z "$n" ] && n=0; echo "$arm cov p=$PP: threshold $K, surviving clusters $n"
    grep -vE '^#' clusters_p$PP.txt | awk 'NF>=16{printf "   %s vox, mean %s, peak RAI (%s %s %s)\n",$1,$11,$14,$15,$16}'
  done
done
echo "COVSD DONE"
