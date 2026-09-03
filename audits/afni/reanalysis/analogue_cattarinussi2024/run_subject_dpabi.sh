#!/bin/bash
# DPABI-analogous AFNI pipeline for one ds000030 subject (see PLAN.md), then 3dReHo pre-fix / post-fix.
set -e
SUB=$1; ROOT=/home/user/reho-pilot; D=$ROOT/data/$SUB; P=$ROOT/dpabi/proc; O=$P/$SUB.results
export PATH=/home/user/afni-bin/linux_ubuntu_24_64:$PATH; export LD_LIBRARY_PATH=/home/user/afni-bin/linux_ubuntu_24_64; export OMP_NUM_THREADS=${OMP_NUM_THREADS:-4}
mkdir -p $D/anat $D/func $P
for f in anat/${SUB}_T1w.nii.gz func/${SUB}_task-rest_bold.nii.gz; do
  [ -s $D/$f ] && ! gzip -t $D/$f 2>/dev/null && rm -f $D/$f
  [ -s $D/$f ] || curl -sSf -o $D/$f https://s3.amazonaws.com/openneuro.org/ds000030/$SUB/$f || { echo "DOWNLOAD FAILED $f"; rm -f $D/$f; exit 3; }
done
cd $P
afni_proc.py -subj_id $SUB -script proc.$SUB -scr_overwrite \
  -dsets $D/func/${SUB}_task-rest_bold.nii.gz -copy_anat $D/anat/${SUB}_T1w.nii.gz \
  -blocks tshift align tlrc volreg mask scale \
  -tcat_remove_first_trs 10 -volreg_align_to MIN_OUTLIER -volreg_align_e2a -volreg_tlrc_warp \
  -tlrc_base MNI152_2009_template_SSW.nii.gz \
  -align_unifize_epi local -align_opts_aea -cost lpc+ZZ -giant_move -check_flip \
  -mask_segment_anat yes -mask_segment_erode yes -mask_epi_anat yes \
  -execute
cd $O
MASK=mask_epi_anat.$SUB+tlrc; SCALED=$(ls pb0*.$SUB.r01.scale+tlrc.HEAD | head -1); SCALED=${SCALED%.HEAD}
# motion exclusion: max |translation| > 3 mm or |rotation| > 3 deg (dfile_rall.1D: roll pitch yaw dS dL dP)
python3 - <<PY
import numpy as np; m=np.loadtxt('dfile_rall.1D'); m=m-m[0]
rot=np.abs(m[:,:3]).max(); tr=np.abs(m[:,3:]).max(); print('MOTION maxrot %.2f maxtrans %.2f'%(rot,tr))
open('motion_flag.txt','w').write('EXCLUDE\n' if (rot>3 or tr>3) else 'OK\n')
PY
# Friston-24: 6 params, their squares, lag-1 values, lag-1 squares (rows aligned to the retained volumes)
1d_tool.py -overwrite -infile dfile_rall.1D -demean -write mot_demean.1D
python3 - <<PY
import numpy as np; m=np.loadtxt('mot_demean.1D'); lag=np.vstack([np.zeros((1,6)),m[:-1]])
F=np.hstack([m,m**2,lag,lag**2]); np.savetxt('friston24.1D',F,fmt='%.6f'); print('friston24',F.shape)
PY
# eroded WM and CSF mean signals from the scaled data (masks from -mask_segment_anat)
3dmaskave -quiet -mask mask_WMe_resam+tlrc $SCALED > wm_mean.1D
3dmaskave -quiet -mask mask_CSFe_resam+tlrc $SCALED > csf_mean.1D
1dcat wm_mean.1D csf_mean.1D > wmcsf.1D
# nuisance regression + linear detrend + band-pass 0.01-0.08 Hz, no censoring
3dTproject -overwrite -input $SCALED -mask $MASK -polort 1 -ort friston24.1D -ort wmcsf.1D -passband 0.01 0.08 -prefix errts.$SUB.tproject
ERRTS=errts.$SUB.tproject+tlrc
$ROOT/bin/3dReHo_preguard -overwrite -prefix reho_prefix  -inset $ERRTS -mask $MASK -nneigh 27   # arm A: 4c2bd54 + guard
$ROOT/bin/3dReHo_postfix  -overwrite -prefix reho_postfix -inset $ERRTS -mask $MASK -nneigh 27   # arm B: 26.2.06
$ROOT/bin/3dReHo_hist     -overwrite -prefix reho_hist    -inset $ERRTS -mask $MASK -nneigh 27   # released code before 26.2.04
3dTstat -overwrite -stdev -prefix errts_sd $ERRTS
# z-normalise each ReHo map within the mask (NaN counted as 0 for the pre-fix arm, as any pipeline would), then smooth 4 mm
for arm in prefix postfix hist; do
  3dcalc -overwrite -a reho_$arm+tlrc -m $MASK -expr 'm*a' -prefix tmp_$arm     # NaN -> 0 (3dcalc treats NaN input as 0)
  read MEAN SD <<< $(3dBrickStat -mask $MASK -mean -stdev tmp_$arm+tlrc | xargs)
  3dcalc -overwrite -a tmp_$arm+tlrc -m $MASK -expr "m*(a-$MEAN)/$SD" -prefix zreho_$arm
  3dmerge -overwrite -1blur_fwhm 4.0 -doall -prefix szreho_$arm zreho_$arm+tlrc
  rm -f tmp_$arm+tlrc.*
done
keep_qc=1; rm -f *T1w* anat_w_skull_warped* volumized* mask_WMe* mask_CSFe* mask_GM* pb0*.BRIK* pb0*.HEAD all_runs.* anat_w_skull_warped.* ROI_import* TSNR.* corr_brain.* errts.*.BRIK* errts.*.HEAD fitts.* *_masked+tlrc.* anat_final.* Classes* mask_epi_extents* mask_anat* mask_group* vr_base* final_epi* anat.un* *.nii.gz
rm -rf $D
echo "DONE $SUB $(cat motion_flag.txt)"
