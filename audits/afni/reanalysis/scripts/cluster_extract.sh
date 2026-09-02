#!/bin/bash
# Extract clusters surviving alpha = 0.05 (bi-sided, NN1) for cluster-forming p = 0.001 and 0.01,
# under each build and mask, from the 3dttest++ -Clustsim output; write cluster tables and
# surviving-cluster masks, and compute before/after overlap of surviving voxels.
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64
for MASKNAME in mask90 inter; do
  if [ $MASKNAME = mask90 ]; then MASK=$R/group_f09/group_mask+tlrc; else MASK=$R/group/group_mask+tlrc; fi
  for P in 0.001 0.01; do
    for arm in pre post; do
      C=$R/clust/${MASKNAME}_${arm}
      # cluster-size threshold at alpha 0.05 from the bi-sided NN1 table (columns: pthr then alpha 0.10..0.01)
      K=$(awk -v p=$P '$1==p{print $4}' $C/cs.CSimA.NN1_bisided.1D)   # alpha=0.05 column
      3dClusterize -overwrite -inset $C/tt+tlrc -ithr 1 -idat 0 -mask $MASK -NN 1 -bisided p=$P -clust_nvox $K \
        -pref_map $C/clmap_p$P -pref_dat $C/cldat_p$P > $C/clusters_p$P.txt 2>/dev/null
      n=$(3dBrickStat -max $C/clmap_p$P+tlrc 2>/dev/null | xargs); [ -z "$n" ] && n=0
      v=$(3dBrickStat -count -non-zero $C/clmap_p$P+tlrc 2>/dev/null | xargs); [ -z "$v" ] && v=0
      echo "$MASKNAME p=$P $arm: cluster-size threshold $K voxels; surviving clusters $n; surviving voxels $v"
    done
    A=$R/clust/${MASKNAME}_pre/clmap_p$P+tlrc; B=$R/clust/${MASKNAME}_post/clmap_p$P+tlrc
    if [ -f ${A}.HEAD ] && [ -f ${B}.HEAD ]; then
      3dcalc -overwrite -a $A -b $B -expr 'step(a)*step(b)' -prefix $R/clust/ov_${MASKNAME}_p$P >/dev/null 2>&1
      3dcalc -overwrite -a $A -b $B -expr 'step(a+b)' -prefix $R/clust/un_${MASKNAME}_p$P >/dev/null 2>&1
      echo "$MASKNAME p=$P overlap of surviving voxels (pre ∩ post / pre ∪ post): $(3dBrickStat -count -non-zero $R/clust/ov_${MASKNAME}_p$P+tlrc | xargs) / $(3dBrickStat -count -non-zero $R/clust/un_${MASKNAME}_p$P+tlrc | xargs)"
    fi
  done
done
