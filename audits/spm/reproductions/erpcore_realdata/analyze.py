"""Group analysis of the SP3 (@meeg/badsamples) fix on ERP CORE: per-subject and group comparison of
the shipped ('prefix') and merged ('merged') builds. Usage: python3 analyze.py <results_root> <out_dir>"""
import sys, os, glob, json
import numpy as np, scipy.io as sio
from scipy import stats
ROOT, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)

def load(task, sub, build):
    return sio.loadmat(f'{ROOT}/{task}/sub{sub:02d}_{build}.mat', squeeze_me=True, struct_as_record=False)

def labels(m):
    return [str(x).strip() for x in np.atleast_1d(m['chanlabels'])]

def cond_index(m, name):
    conds = [str(c).strip() for c in np.atleast_1d(m['erp_conditions'])]
    return conds.index(name)

MEAS = {'P3':  dict(chan='Pz',  win=(300, 600), a='target', b='standard'),
        'ERN': dict(chan='FCz', win=(0, 100),   a='error',  b='correct')}

def measure(m, task, which):
    """mean amplitude of (a - b) at the ERP CORE channel/window, plus the difference wave"""
    erp = m[which]; t = np.atleast_1d(m['time']) * 1000.0
    lab = labels(m); ci = lab.index(MEAS[task]['chan'])
    ia, ib = cond_index(m, MEAS[task]['a']), cond_index(m, MEAS[task]['b'])
    diff = erp[:, :, ia] - erp[:, :, ib]
    w = (t >= MEAS[task]['win'][0]) & (t <= MEAS[task]['win'][1])
    return float(np.nanmean(diff[ci, w])), diff

def mask_stats(mp, mm):
    """mask-level comparison: prefix mask vs merged mask (merged == detector intent, verified on MMN)"""
    bp, bm = mp['bad'].astype(bool), mm['bad'].astype(bool)
    inter = np.logical_and(bp, bm).sum(); union = np.logical_or(bp, bm).sum()
    return dict(bad_pre=int(bp.sum()), bad_post=int(bm.sum()),
                jaccard=float(inter / union) if union else float('nan'),
                excluded_frac=float(inter / bm.sum()) if bm.sum() else float('nan'),   # share of true artefact samples the shipped code excluded
                clean_frac=float(np.logical_and(bp, ~bm).sum() / bp.sum()) if bp.sum() else float('nan'),  # share of shipped exclusions that were clean
                trials_bad_pre=int(np.any(np.any(bp, 0), 0).sum()), trials_bad_post=int(np.any(np.any(bm, 0), 0).sum()))

rows = {}; GA = {}
for task in ['P3', 'ERN']:
    files = sorted(glob.glob(f'{ROOT}/{task}/sub*_merged.mat'))
    R = []
    for f in files:
        sub = int(os.path.basename(f)[3:5])
        if not os.path.exists(f'{ROOT}/{task}/sub{sub:02d}_prefix.mat'): continue
        mp, mm = load(task, sub, 'prefix'), load(task, sub, 'merged')
        r = dict(sub=sub, ntrials=int(mp['bad'].shape[2]))
        r.update(mask_stats(mp, mm))
        r['rej_pre'] = int(np.size(mp['badtrials'])); r['rej_post'] = int(np.size(mm['badtrials']))
        # retained trials per condition in the plain (rejection) path
        for m_, key in [(mp, 'pre'), (mm, 'post')]:
            conds = [str(c).strip() for c in np.atleast_1d(m_['erp_conditions'])]; nt = np.atleast_1d(m_['ntrials_plain'])
            r[f'n_{MEAS[task]["a"]}_{key}'] = int(nt[conds.index(MEAS[task]['a'])]); r[f'n_{MEAS[task]["b"]}_{key}'] = int(nt[conds.index(MEAS[task]['b'])])
        # detector-written windows: how many are pushed entirely outside the epoch by the |timeOnset| shift
        evs = mm['artefact_events']; shift = abs(float(mm['timeonset'])); eplen = mp['bad'].shape[1] / float(mm['fsample'])
        if np.size(evs):
            evs = np.atleast_2d(evs); onset = np.array([float(x) for x in evs[:, 2]]); dur = np.array([float(x) for x in evs[:, 3]])
            r['n_windows'] = int(len(onset)); r['windows_lost_frac'] = float(np.mean(onset + shift >= eplen))
            r['windows_partial_frac'] = float(np.mean((onset + shift < eplen) & (onset + dur + shift > eplen)))
        else:
            r['n_windows'] = 0; r['windows_lost_frac'] = float('nan'); r['windows_partial_frac'] = float('nan')
        lab = labels(mp)
        bcp = [lab[i-1] for i in np.atleast_1d(mp['badchannels']).astype(int)] if np.size(mp['badchannels']) else []
        bcm = [lab[i-1] for i in np.atleast_1d(mm['badchannels']).astype(int)] if np.size(mm['badchannels']) else []
        r['badchan_pre'] = ','.join(bcp); r['badchan_post'] = ','.join(bcm); r['badchan_differs'] = int(set(bcp) != set(bcm))
        for which, key in [('erp_plain', 'plain'), ('erp_robust', 'robust')]:
            ap, dp = measure(mp, task, which); am, dm = measure(mm, task, which)
            r[f'{key}_pre'] = ap; r[f'{key}_post'] = am
            GA.setdefault((task, key), []).append((sub, dp, dm))
            # whole-scalp difference-wave change, RMS over EEG channels and the measurement window, relative to post-fix RMS
            t = np.atleast_1d(mm['time']) * 1000.0; w = (t >= MEAS[task]['win'][0]) & (t <= MEAS[task]['win'][1])
            eeg = [i for i, ty in enumerate(np.atleast_1d(mm['chantype'])) if str(ty).strip() == 'EEG']
            num = np.sqrt(np.nanmean((dp[eeg][:, w] - dm[eeg][:, w]) ** 2)); den = np.sqrt(np.nanmean(dm[eeg][:, w] ** 2))
            r[f'{key}_rms_change'] = float(num / den) if den else float('nan')
        R.append(r)
    rows[task] = R
    # write per-subject table
    if R:
        keys = list(R[0].keys())
        with open(f'{OUT}/{task}_subjects.tsv', 'w') as fh:
            fh.write('\t'.join(keys) + '\n')
            for r in R: fh.write('\t'.join(f'{r[k]:.4g}' if isinstance(r[k], float) else str(r[k]) for k in keys) + '\n')

# group summary
summary = {}
for task, R in rows.items():
    if not R: continue
    n = len(R); g = {}
    g['n'] = n
    for k in ['jaccard', 'excluded_frac', 'clean_frac']:
        v = np.array([r[k] for r in R], float); g[k + '_median'] = float(np.nanmedian(v))
    g['bad_samples_pre_total'] = int(sum(r['bad_pre'] for r in R)); g['bad_samples_post_total'] = int(sum(r['bad_post'] for r in R))
    g['rej_pre_total'] = int(sum(r['rej_pre'] for r in R)); g['rej_post_total'] = int(sum(r['rej_post'] for r in R)); g['trials_total'] = int(sum(r['ntrials'] for r in R))
    g['badchan_differs_n'] = int(sum(r['badchan_differs'] for r in R))
    g['badchan_pre_n'] = int(sum(len([x for x in r['badchan_pre'].split(',') if x]) for r in R)); g['badchan_post_n'] = int(sum(len([x for x in r['badchan_post'].split(',') if x]) for r in R))
    ca = MEAS[task]['a']
    g['subjects_zero_a_post'] = int(sum(r[f'n_{ca}_post'] == 0 for r in R)); g['subjects_zero_a_pre'] = int(sum(r[f'n_{ca}_pre'] == 0 for r in R))
    g['subjects_lt6_a_post'] = int(sum(r[f'n_{ca}_post'] < 6 for r in R)); g['subjects_lt6_a_pre'] = int(sum(r[f'n_{ca}_pre'] < 6 for r in R))
    g['n_a_pre_total'] = int(sum(r[f'n_{ca}_pre'] for r in R)); g['n_a_post_total'] = int(sum(r[f'n_{ca}_post'] for r in R))
    g['windows_total'] = int(sum(r['n_windows'] for r in R)); g['windows_lost_frac_median'] = float(np.nanmedian([r['windows_lost_frac'] for r in R]))
    g['windows_lost_frac_pooled'] = float(sum(r['windows_lost_frac'] * r['n_windows'] for r in R if r['n_windows']) / max(1, g['windows_total']))
    for key in ['plain', 'robust', 'plain_ge6']:
        base = key.replace('_ge6', '')
        a = np.array([r[f'{base}_pre'] for r in R]); b = np.array([r[f'{base}_post'] for r in R])
        ok = np.isfinite(a) & np.isfinite(b)
        if key.endswith('_ge6'): ok &= np.array([(r[f'n_{ca}_pre'] >= 6) & (r[f'n_{ca}_post'] >= 6) for r in R])
        a, b = a[ok], b[ok]; g[f'{key}_n'] = int(ok.sum())
        g[f'{key}_mean_pre'] = float(a.mean()); g[f'{key}_mean_post'] = float(b.mean())
        g[f'{key}_t_pre'] = float(stats.ttest_1samp(a, 0).statistic); g[f'{key}_p_pre'] = float(stats.ttest_1samp(a, 0).pvalue)
        g[f'{key}_t_post'] = float(stats.ttest_1samp(b, 0).statistic); g[f'{key}_p_post'] = float(stats.ttest_1samp(b, 0).pvalue)
        g[f'{key}_paired_t'] = float(stats.ttest_rel(a, b).statistic); g[f'{key}_paired_p'] = float(stats.ttest_rel(a, b).pvalue)
        g[f'{key}_r_pre_post'] = float(np.corrcoef(a, b)[0, 1])
        g[f'{key}_abs_change_median_uV'] = float(np.median(np.abs(a - b))); g[f'{key}_abs_change_max_uV'] = float(np.max(np.abs(a - b)))
        g[f'{key}_rel_change_median'] = float(np.median(np.abs(a - b) / np.abs(b)))
        g[f'{key}_rms_change_median'] = float(np.nanmedian([r[f'{base}_rms_change'] for r in R]))
        g[f'{key}_subjects_change_gt_10pct'] = int(np.sum(np.abs(a - b) / np.abs(b) > 0.10))
        g[f'{key}_subjects_change_gt_1uV'] = int(np.sum(np.abs(a - b) > 1.0))
    summary[task] = g
json.dump(summary, open(f'{OUT}/summary.json', 'w'), indent=1)
ga = {}
for (task, key), L in GA.items():
    m = load(task, L[0][0], 'merged'); t = np.atleast_1d(m['time']) * 1000.0; lab = labels(m); ci = lab.index(MEAS[task]['chan'])
    pre = np.array([dp[ci] for _, dp, _ in L]); post = np.array([dm[ci] for _, _, dm in L])
    ga[f'{task}_{key}_t'] = t; ga[f'{task}_{key}_pre'] = pre; ga[f'{task}_{key}_post'] = post; ga[f'{task}_{key}_subs'] = np.array([s for s, _, _ in L])
np.savez(f'{OUT}/grand_averages.npz', **ga)
for task, g in summary.items():
    print(f'== {task}: n={g["n"]} ==')
    for k, v in g.items():
        if k != 'n': print(f'  {k:32s} {v:.4g}' if isinstance(v, float) else f'  {k:32s} {v}')
