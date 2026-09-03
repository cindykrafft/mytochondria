#!/bin/bash
# stop every pilot process without killing the caller
me=$$; par=$PPID; gp=$(ps -o ppid= -p $PPID | tr -d ' ')
for pat in 'run_ext.sh' 'run_subject.sh' 'janitor_ext.sh' 'janitor2_ext.sh' 'afni_proc.py' 'tcsh -xef proc' '3dReHo_' '3dDeconvolve' '3dTproject' '3dvolreg' '3dQwarp' 'auto_warp' '3dSkullStrip' '3dAllineate' 'align_epi_anat'; do
  for p in $(pgrep -f "$pat"); do [ "$p" = "$me" ] || [ "$p" = "$par" ] || [ "$p" = "$gp" ] || kill $p 2>/dev/null; done
done
sleep 2
pgrep -fa 'run_ext.sh|run_subject.sh|janitor|afni_proc|tcsh -xef' | grep -v stop_all | wc -l
