"""SP4 exposure: for common acquisition -> requested rates, what spm_eeg_downsample with method 'decimate' or
'downsample' actually achieves (factor = round(Fold/Fnew), as in ft_preproc_resample) and how the shipped
stamp (requested rate stored) distorts every time value read back: reported time = true time * achieved / requested."""
acq = {'Biosemi ActiveTwo': [512, 1024, 2048], 'Brain Products / Neuroscan': [500, 1000, 2000, 5000],
       'CTF MEG': [600, 1200, 2400], 'Elekta / MEGIN MEG': [1000, 1100, 2000], 'EGI': [250, 500, 1000]}
targets = [100, 200, 250, 256, 300, 500]
def mround(x):  # MATLAB round: half away from zero
    import math; return int(math.floor(x + 0.5))
rows = []; n_all = 0
for sys_, fs in acq.items():
    for f0 in fs:
        for ft in targets:
            if ft >= f0: continue
            n_all += 1; fac = mround(f0 / ft); ach = f0 / fac
            if abs(ach - ft) > 1e-9: rows.append((sys_, f0, ft, fac, ach, ach / ft))
rows.sort(key=lambda r: -abs(r[5] - 1))
print(f'{"system":28s}{"acquired":>9}{"requested":>10}{"factor":>7}{"achieved":>10}{"reported/true time":>20}')
for r in rows: print(f'{r[0]:28s}{r[1]:9d}{r[2]:10d}{r[3]:7d}{r[4]:10.2f}{r[5]:20.3f}')
print(f'{len(rows)} of {n_all} pairs are non-integer (the defect fires); {sum(1 for r in rows if abs(r[5]-1) >= 0.05)} distort time by 5% or more')
