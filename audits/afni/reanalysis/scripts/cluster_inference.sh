#!/bin/bash
# Cluster-level inference for the SCHZ vs CONTROL contrast under each 3dReHo build, in the
# style of a published design: 3dttest++ -Clustsim (sign-flip randomisation of the residuals,
# 10000 iterations) gives the cluster-size threshold at alpha = 0.05 for several
# cluster-forming p-values; 3dClusterize then extracts surviving clusters.
R=/home/user/reho-pilot; export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64 OMP_NUM_THREADS=4
cd $R/proc_v1
for MASKNAME in mask90 inter; do
  if [ $MASKNAME = mask90 ]; then MASK=$R/group_f09/group_mask+tlrc; else MASK=$R/group/group_mask+tlrc; fi
  for arm in pre post; do
    C=$R/clust/${MASKNAME}_${arm}; mkdir -p $C
    SA=$(sed "s|$|.results/reho_${arm}fix+tlrc|" $R/group/list_SCHZ.txt); SB=$(sed "s|$|.results/reho_${arm}fix+tlrc|" $R/group/list_CONTROL.txt)
    SA=$(echo "$SA" | sed "s|^|$R/proc_v1/|; s| | $R/proc_v1/|g"); SB=$(echo "$SB" | sed "s|^|$R/proc_v1/|; s| | $R/proc_v1/|g")
    ( cd $C && 3dttest++ -overwrite -prefix tt -mask $MASK -setA $SA -setB $SB -labelA SCZ -labelB CONTROL \
      -Clustsim 4 -prefix_clustsim cs > ttest.log 2>&1 )
    echo "$(date +%H:%M) done $MASKNAME $arm"
  done
done
echo "CLUSTSIM DONE"
