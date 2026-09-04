# IQ3 — thread count changes SH-aLRT and UFBoot at a fixed seed (not to be filed; #228 exists)

Issue #228 (iqtree/iqtree2, "Sequence order in the input and parallelism affect
reproducibility", opened 2024-06-11 on 2.3.4, closed 2024-06-17 after 5 comments) reports
that `--seed` does not make multi-threaded runs reproducible; the reporter already found
that `-nt 1` restores reproducibility. This project reproduced the SH-aLRT part on 2.4.0
(`../verify/heldup_ufboot.py`): `-alrt 1000 -seed 3` gives 95.8 / 97.6 / 95.3 / 99.8 /
97.7 with `-T 1` and 96.1 / 97.3 / 95.8 / 99.8 / 98.1 with `-T 2`; two `-T 1` runs are
byte-identical; 12 of 1,000 UFBoot replicate trees differ between `-T 1` and `-T 2` with
the printed supports unchanged on that alignment.

Mechanism (for the record): per-thread random streams seeded `ran_seed + thread` with the
replicate loop split across threads (`tree/phylotree.cpp:5268-5271`;
`tree/iqtree.cpp:3594-3600`; `tree/discordance.cpp:46` for `--scf`).

The only thing missing is a sentence in the manual's `-seed` row
(`doc/Command-Reference.md:84`, currently "Specify a random number seed to reproduce a
previous run"): *"Runs are reproducible only with the same number of threads (`-T`); the
random streams are per thread."* If the IQ1 manual PR is accepted, add it there in a
follow-up rather than reopening #228.
