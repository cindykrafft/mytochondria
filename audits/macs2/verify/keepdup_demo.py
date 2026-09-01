#!/usr/bin/env python3
"""MC1 end-to-end demo (run against any MACS2/MACS3 with --keep-dup auto):
builds synthetic BEDs where the treatment binomial threshold is 1 and the
control's is 3 (control has 5,000 positions with exactly 3 duplicates),
then shows the control is filtered at the treatment's threshold.

  macs3 callpeak -t t.bed -c c.bed -g 1000000 -n kd --keep-dup auto \
        --nomodel --extsize 150 --outdir kd_out

Observed on MACS3 3.0.4 (and the same code is in 2.1.x/2.2.x):
  #1  max_dup_tags based on binomial = 3        <- control's own threshold, logged
  #1  tags after filtering in control: 48636    <- but filtered at threshold 1:
     60,000 - 2x5,000 duplicate reads - collisions = 48,636
With the logged threshold 3, ~59,99x reads would remain.
"""
import random, subprocess, sys, re
random.seed(5)
with open("t.bed","w") as f:
    for i in range(2000):
        p = random.randrange(0, 900000)
        f.write(f"chr1\t{p}\t{p+50}\t.\t0\t+\n")
with open("c.bed","w") as f:
    n = 0
    for i in range(5000):
        p = random.randrange(0, 900000)
        for _ in range(3):
            f.write(f"chr1\t{p}\t{p+50}\t.\t0\t+\n"); n += 1
    while n < 60000:
        p = random.randrange(0, 900000)
        f.write(f"chr1\t{p}\t{p+50}\t.\t0\t+\n"); n += 1

macs = sys.argv[1] if len(sys.argv) > 1 else "macs3"
out = subprocess.run([macs, "callpeak", "-t", "t.bed", "-c", "c.bed", "-g", "1000000",
                      "-n", "kd", "--keep-dup", "auto", "--nomodel", "--extsize", "150",
                      "--outdir", "kd_out"], capture_output=True, text=True).stderr
for line in out.splitlines():
    if re.search(r"max_dup_tags|after filtering|total tags", line):
        print(line.split("] ")[-1])
