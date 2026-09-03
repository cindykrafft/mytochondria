#!/bin/bash
# Enlarged-sample group analysis: all passed subjects in proc_v1 (first 40) and proc (extension).
# Arm A = reho_prefix (4c2bd54; NaN read as 0 = 4c2bd54+guard), arm B = reho_postfix (AFNI 26.2.06).
# Outputs to group_ext/: lists, masks, 3dttest++ maps, uncorrected comparison, then -Clustsim cluster inference.
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64 OMP_NUM_THREADS=4
G=$R/group_ext; mkdir -p $G; bs(){ 3dBrickStat "$@" | xargs; }
: > $G/list_CONTROL.txt; : > $G/list_SCHZ.txt
for tsv in $R/subjects_rerun.tsv $R/subjects_ext.tsv; do tail -n +2 $tsv | while IFS=$'\t' read SUB GRP; do
  for D in $R/proc_v1 $R/proc; do [ -f $D/$SUB.results/reho_postfix+tlrc.HEAD ] && { echo "$D/$SUB.results" >> $G/list_$GRP.txt; break; }; done
done; done
nC=$(wc -l < $G/list_CONTROL.txt); nS=$(wc -l < $G/list_SCHZ.txt); echo "CONTROL $nC SCHZ $nS"
MASKS=$(cat $G/list_CONTROL.txt $G/list_SCHZ.txt | while read d; do s=$(basename $d .results); echo $d/mask_epi_anat.$s+tlrc.HEAD; done)
3dmask_tool -overwrite -input $MASKS -frac 0.9 -prefix $G/mask90 >/dev/null 2>&1
3dmask_tool -overwrite -input $MASKS -frac 1.0 -prefix $G/inter >/dev/null 2>&1
df=$((nC+nS-2)); tcrit=$(python3 -c "from scipy.stats import t; print(round(t.ppf(0.9995,$df),3))")
for M in mask90 inter; do
  echo "== mask $M: $(bs -count -non-zero $G/$M+tlrc) voxels; df $df; |t| for p<.001 = $tcrit"
  for arm in pre post; do
    SA=$(sed "s|$|/reho_${arm}fix+tlrc|" $G/list_SCHZ.txt); SB=$(sed "s|$|/reho_${arm}fix+tlrc|" $G/list_CONTROL.txt)
    C=$G/clust_${M}_$arm; mkdir -p $C/tmp; cd $C
    3dttest++ -overwrite -prefix tt -mask $G/$M+tlrc -setA $SA -setB $SB -labelA SCZ -labelB CONTROL -Clustsim 4 -prefix_clustsim cs -tempdir tmp > ttest.log 2>&1
    3dcalc -overwrite -a tt+tlrc'[1]' -expr "step(abs(a)-$tcrit)" -prefix supra >/dev/null 2>&1
    3dcalc -overwrite -a tt+tlrc'[1]' -expr "step(abs(a)-1.96)" -prefix supra05 >/dev/null 2>&1
    echo "$M $arm: |t|>$tcrit: $(bs -count -non-zero supra+tlrc) ; |t|>1.96: $(bs -count -non-zero supra05+tlrc)"
    for P in 0.001 0.01; do
      K=$(awk -v p=$P '$1==p{print $7}' cs.CSimA.NN1_bisided.1D)
      3dClusterize -overwrite -inset tt+tlrc -ithr 1 -idat 0 -mask $G/$M+tlrc -NN 1 -bisided p=$P -clust_nvox $K -pref_map clmap_p$P -pref_dat cldat_p$P > clusters_p$P.txt 2>/dev/null
      big=$(3dClusterize -inset tt+tlrc -ithr 1 -idat 0 -mask $G/$M+tlrc -NN 1 -bisided p=$P -clust_nvox 1 2>/dev/null | grep -v '^#' | awk 'NR==1{print $1}')
      n=$(bs -max clmap_p$P+tlrc 2>/dev/null); [ -z "$n" ] && n=0
      echo "$M $arm p=$P: threshold $K, largest cluster ${big:-0}, surviving clusters $n, surviving voxels $( [ -f clmap_p$P+tlrc.HEAD ] && bs -count -non-zero clmap_p$P+tlrc || echo 0)"
    done
  done
  cd $G; A=clust_${M}_pre; B=clust_${M}_post
  echo "$M t-map corr pre vs post: $(python3 $R/scripts/masked_corr.py $M+tlrc "$A/tt+tlrc[1]" "$B/tt+tlrc[1]")"
  echo "$M sign flips: $(3dcalc -overwrite -a $A/tt+tlrc'[1]' -b $B/tt+tlrc'[1]' -m $M+tlrc -expr 'm*step(-a*b)' -prefix sf_$M >/dev/null 2>&1; bs -count -non-zero sf_$M+tlrc)"
  echo "$M overlap |t|>$tcrit (and/or): $(3dcalc -overwrite -a $A/supra+tlrc -b $B/supra+tlrc -expr 'a*b' -prefix oa_$M >/dev/null 2>&1; 3dcalc -overwrite -a $A/supra+tlrc -b $B/supra+tlrc -expr 'step(a+b)' -prefix oo_$M >/dev/null 2>&1; echo "$(bs -count -non-zero oa_$M+tlrc) / $(bs -count -non-zero oo_$M+tlrc)")"
  echo "$M overlap |t|>1.96 (and/or): $(3dcalc -overwrite -a $A/supra05+tlrc -b $B/supra05+tlrc -expr 'a*b' -prefix oa05_$M >/dev/null 2>&1; 3dcalc -overwrite -a $A/supra05+tlrc -b $B/supra05+tlrc -expr 'step(a+b)' -prefix oo05_$M >/dev/null 2>&1; echo "$(bs -count -non-zero oa05_$M+tlrc) / $(bs -count -non-zero oo05_$M+tlrc)")"
  for P in 0.001 0.01; do [ -f $A/clmap_p$P+tlrc.HEAD ] && [ -f $B/clmap_p$P+tlrc.HEAD ] && echo "$M corrected-cluster voxel overlap p=$P (and/or): $(3dcalc -overwrite -a $A/clmap_p$P+tlrc -b $B/clmap_p$P+tlrc -expr 'step(a)*step(b)' -prefix ca_${M}_$P >/dev/null 2>&1; 3dcalc -overwrite -a $A/clmap_p$P+tlrc -b $B/clmap_p$P+tlrc -expr 'step(a+b)' -prefix co_${M}_$P >/dev/null 2>&1; echo "$(bs -count -non-zero ca_${M}_$P+tlrc) / $(bs -count -non-zero co_${M}_$P+tlrc)")"; done
done
echo "GROUP EXT DONE"
