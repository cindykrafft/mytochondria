#!/usr/bin/env python3
"""Probe for a second, separate bdgdiff defect noticed while reproducing
issue #715 (NOT fixed by the #715 patch; held for its own issue).

TwoConditionScores.build_chromosome stores, for each interval, the
interval's START position (`pre_p`) next to the interval's log10LR
values, but TwoConditionScores.call_peaks reads the stored positions as
END positions (`endpos = pos[idx]`, `startpos = pos[idx-1]`). Every
reported region is therefore displaced by one bedGraph interval to the
left: it starts at the start of the interval before the first
significant one and ends at the start of the last significant one.

The same two statements exist in MACS2 2.2.9.1 (ScoreTrack.pyx:1414 /
1642-1643) and MACS3 3.0.0 (ScoreTrack.pyx:1120 / 1356-1357), so this is
long-standing and test/standard_results_bdgdiff carries it too.

Run inside a MACS3 environment: python interval_shift_probe.py
"""
from MACS3.Signal.ScoreTrack import TwoConditionScores
from MACS3.Signal.BedGraph import bedGraphTrackI

# (start, end, t1, c1, t2, c2): only [1000, 3000) is cond1 > cond2
regions = [(0, 1000, 20.0, 2.0, 18.0, 2.0),
           (1000, 2000, 20.0, 2.0, 15.0, 2.0),
           (2000, 3000, 40.0, 2.0, 15.0, 2.0),
           (3000, 4000, 2.0, 2.0, 2.0, 2.0)]
bdgs = [bedGraphTrackI() for _ in range(4)]
for (s, e, t1, c1, t2, c2) in regions:
    for (bdg, v) in zip(bdgs, (t1, c1, t2, c2)):
        bdg.add_loc(b"chr1", s, e, v)
tcs = TwoConditionScores(bdgs[0], bdgs[1], bdgs[2], bdgs[3], 1.0, 1.0)
tcs.build()
tcs.finalize()
pos, t1_vs_c1, t2_vs_c2, t1_vs_t2 = tcs.get_data_by_chr(b"chr1")
print("stored position vs interval it describes (position is the interval START):")
for i in range(len(pos)):
    print(f"  i={i} pos={pos[i]:5d}  interval=[{regions[i][0]},{regions[i][1]})  "
          f"t1_vs_t2={t1_vs_t2[i]:.4f}")
(cat1, cat2, cat3) = tcs.call_peaks(min_length=200, max_gap=100, cutoff=0.2)
for pk in cat1.get_data_from_chrom(b"chr1"):
    print(f"cond1 region reported: chr1:{pk['start']}-{pk['end']}  "
          f"(intervals with log10LR >= 0.2 span 1000-3000)  score={pk['score']:.4f}")
print(f"common regions reported: {cat3.total} (interval [0,1000) qualifies but is dropped: "
      "its index is 0, so startpos is forced to 0 and endpos = pos[0] = 0, length 0)")
