#!/bin/bash
me=$$; par=$PPID; gp=$(ps -o ppid= -p $PPID | tr -d ' ')
for pat in 'run_batch_dpabi.sh' 'run_subject_dpabi.sh' 'afni_proc.py' 'tcsh -xef proc' '3dReHo_' '3dTproject' '3dvolreg' '3dSkullStrip' '3dAllineate' 'align_epi_anat' '3dQwarp' '3dmerge' '3dTshift'; do
  for p in $(pgrep -f "$pat"); do [ "$p" = "$me" ] || [ "$p" = "$par" ] || [ "$p" = "$gp" ] || kill $p 2>/dev/null; done
done; sleep 2; pgrep -fa 'run_batch_dpabi|run_subject_dpabi|afni_proc|tcsh -xef' | grep -v stop_dpabi | wc -l
