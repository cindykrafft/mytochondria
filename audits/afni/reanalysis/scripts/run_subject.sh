#!/bin/bash
# Pilot: afni_proc.py default-style resting-state pipeline (with the scale block,
# i.e. percent signal change) on one ds000030 subject, then 3dReHo pre-fix vs post-fix
# on the *same* errts input. Usage: run_subject.sh sub-XXXXX
set -e
SUB=$1; ROOT=/home/user/reho-pilot; D=$ROOT/data/$SUB; O=$ROOT/proc/$SUB
export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH; export LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64; export OMP_NUM_THREADS=4
mkdir -p $D/anat $D/func $ROOT/proc
for f in anat/${SUB}_T1w.nii.gz func/${SUB}_task-rest_bold.nii.gz; do
  [ -s $D/$f ] && ! gzip -t $D/$f 2>/dev/null && rm -f $D/$f   # discard truncated/partial downloads
  [ -s $D/$f ] || curl -sSf -o $D/$f https://s3.amazonaws.com/openneuro.org/ds000030/$SUB/$f || { echo "DOWNLOAD FAILED $f"; rm -f $D/$f; exit 3; }
done
cd $ROOT/proc
afni_proc.py -subj_id $SUB -script proc.$SUB -scr_overwrite \
  -dsets $D/func/${SUB}_task-rest_bold.nii.gz -copy_anat $D/anat/${SUB}_T1w.nii.gz \
  -blocks despike tshift align tlrc volreg blur mask scale regress \
  -tcat_remove_first_trs 4 -volreg_align_to MIN_OUTLIER -volreg_align_e2a -volreg_tlrc_warp \
  -tlrc_base MNI152_2009_template_SSW.nii.gz -blur_size 4.0 \
  -regress_censor_motion 0.3 -regress_censor_outliers 0.05 -regress_bandpass 0.01 0.1 \
  -regress_apply_mot_types demean deriv -regress_est_blur_epits -regress_run_clustsim no \
  -execute
# ReHo on the residual time series (errts, in percent-signal units) with both binaries
cd $SUB.results
ERRTS=$(ls errts.${SUB}.tproject+tlrc.HEAD errts.${SUB}+tlrc.HEAD 2>/dev/null | head -1); ERRTS=${ERRTS%.HEAD}
MASK=$(ls mask_epi_anat.${SUB}+tlrc.HEAD 2>/dev/null | head -1); MASK=${MASK%.HEAD}
$ROOT/bin/3dReHo_hist    -overwrite -prefix reho_hist    -inset $ERRTS -mask $MASK -nneigh 27   # code before 2023-09-27 (29384a2^)
$ROOT/bin/3dReHo_prefix  -overwrite -prefix reho_prefix  -inset $ERRTS -mask $MASK -nneigh 27   # 4c2bd54: master for one day, 2026-08-27
$ROOT/bin/3dReHo_preguard -overwrite -prefix reho_preguard -inset $ERRTS -mask $MASK -nneigh 27  # 4c2bd54 + 74a90ac guard: arm A
$ROOT/bin/3dReHo_postfix -overwrite -prefix reho_postfix -inset $ERRTS -mask $MASK -nneigh 27
3dTstat -overwrite -stdev -prefix errts_sd $ERRTS      # per-voxel SD in the units 3dReHo saw
# keep only what the group analysis needs (each results dir is ~1.4 GB otherwise)
rm -f pb0*.BRIK* pb0*.HEAD all_runs.* anat_w_skull_warped.* ROI_import* TSNR.* corr_brain.* errts.*.BRIK* errts.*.HEAD fitts.* *_masked+tlrc.* anat_final.*
rm -rf $D
echo "DONE $SUB"
