#!/bin/bash
# runs batch 1 to completion, then the spare top-up; janitors run alongside
R=/home/user/reho-pilot
nohup bash $R/scripts/janitor.sh  >> $R/janitor.log  2>&1 &
nohup bash $R/scripts/janitor2.sh >> $R/janitor2.log 2>&1 &
bash $R/scripts/run_batch.sh  >> $R/batch.log  2>&1
bash $R/scripts/run_batch2.sh >> $R/batch2.log 2>&1
