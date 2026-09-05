"""Figure: the @meeg/badsamples fix (SPM PR 163) on ERP CORE, 39 participants, two paradigms.
Usage: python3 make_figure.py <out_dir with *_subjects.tsv, grand_averages.npz> <figure.pdf>"""
import sys, csv, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
OUT, FIG = sys.argv[1], sys.argv[2]
BLUE, ORANGE = '#2a78d6', '#eb6834'          # after fix / before fix (validated pair)
INK, INK2, MUTED, GRID, AXIS = '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 8, 'axes.edgecolor': AXIS, 'axes.labelcolor': INK2,
    'xtick.color': MUTED, 'ytick.color': MUTED, 'axes.titlesize': 9, 'axes.titleweight': 'bold', 'axes.titlecolor': INK,
    'axes.spines.top': False, 'axes.spines.right': False, 'legend.frameon': False, 'legend.fontsize': 7.5})
rows = {t: list(csv.DictReader(open(f'{OUT}/{t}_subjects.tsv'), delimiter='\t')) for t in ['P3', 'ERN']}
g = np.load(f'{OUT}/grand_averages.npz')
fig, ax = plt.subplots(2, 2, figsize=(7.0, 5.4)); fig.patch.set_facecolor('white')

# A: share of the detector's windows pushed entirely out of the epoch, per participant, by paradigm
a = ax[0, 0]
for i, (task, col, lab) in enumerate([('P3', MUTED, 'P3, stimulus-locked, epoch starts −200 ms'), ('ERN', INK, 'ERN, response-locked, epoch starts −600 ms')]):
    v = np.array([float(r['windows_lost_frac']) for r in rows[task]]) * 100
    x = i + (np.random.RandomState(1).rand(len(v)) - 0.5) * 0.35
    a.scatter(x, v, s=18, color=col, edgecolor='white', linewidth=0.6, zorder=3)
    a.hlines(np.median(v), i - 0.25, i + 0.25, color=col, lw=2, zorder=4)
    a.text(i, 104, f'median {np.median(v):.0f}%', ha='center', color=INK, fontsize=7.5)
a.set_xticks([0, 1]); a.set_xticklabels(['P3\n(baseline 200 ms)', 'ERN\n(epoch from −600 ms)'], color=INK2)
a.set_ylim(-3, 112); a.set_ylabel('detector windows outside the epoch (%)'); a.grid(axis='y', color=GRID, lw=0.6)
a.set_title('A  Windows the shift pushes out of the epoch')

# B: trials rejected per participant, before vs after, both paradigms
b = ax[0, 1]
for task, mk, lab in [('ERN', 'o', 'ERN'), ('P3', 's', 'P3')]:
    pre = np.array([100 * int(r['rej_pre']) / int(r['ntrials']) for r in rows[task]]); post = np.array([100 * int(r['rej_post']) / int(r['ntrials']) for r in rows[task]])
    b.scatter(post, pre, s=22, marker=mk, facecolor=BLUE if task == 'ERN' else 'white', edgecolor=BLUE, linewidth=1.0, label=lab, zorder=3)
b.plot([0, 100], [0, 100], color=AXIS, lw=0.8); b.set_xlim(0, 100); b.set_ylim(0, 100)
b.set_xlabel('trials rejected after the fix (%)'); b.set_ylabel('trials rejected before the fix (%)'); b.grid(color=GRID, lw=0.6)
b.legend(loc='upper left'); b.set_title('B  Trials rejected, same settings')
b.text(52, 20, 'ERN: 2% rejected before,\n51% after (pooled)', ha='left', color=INK2, fontsize=7.5)

# C: grand-average ERN difference wave at FCz, plain average after rejection (participants with >= 6 error trials in both)
c = ax[1, 0]
ok = np.array([int(r['sub']) for r in rows['ERN'] if int(r['n_error_pre']) >= 6 and int(r['n_error_post']) >= 6])
t = g['ERN_plain_t']; sel = np.isin(g['ERN_plain_subs'], ok)
pre = g['ERN_plain_pre'][sel].mean(0); post = g['ERN_plain_post'][sel].mean(0)
c.axvspan(0, 100, color=GRID, alpha=0.6, lw=0)
c.plot(t, pre, color=ORANGE, lw=1.6, label='before fix'); c.plot(t, post, color=BLUE, lw=1.6, label='after fix')
c.axhline(0, color=AXIS, lw=0.8); c.axvline(0, color=AXIS, lw=0.8)
c.set_xlim(-600, 400); c.set_xlabel('time from response (ms)'); c.set_ylabel('error − correct at FCz (µV)')
c.text(50, 12.5, 'window', ha='center', va='top', color=INK2, fontsize=7)
c.set_title(f'C  Grand-average ERN after rejection (n = {sel.sum()})'); c.legend(loc='upper left'); c.grid(axis='y', color=GRID, lw=0.6)

# D: per-participant ERN amplitude before vs after (same subset)
d = ax[1, 1]
pre_a = np.array([float(r['plain_pre']) for r in rows['ERN'] if int(r['sub']) in ok]); post_a = np.array([float(r['plain_post']) for r in rows['ERN'] if int(r['sub']) in ok])
lim = [min(pre_a.min(), post_a.min()) - 2, max(pre_a.max(), post_a.max()) + 2]
d.plot(lim, lim, color=AXIS, lw=0.8); d.scatter(post_a, pre_a, s=22, color=BLUE, edgecolor='white', linewidth=0.6, zorder=3)
d.set_xlim(lim); d.set_ylim(lim); d.set_xlabel('ERN after the fix (µV)'); d.set_ylabel('ERN before the fix (µV)'); d.grid(color=GRID, lw=0.6)
d.set_title('D  ERN amplitude per participant')
d.text(lim[1] - 0.5, lim[0] + 0.8, f'mean {pre_a.mean():.1f} vs {post_a.mean():.1f} µV\nr = {np.corrcoef(pre_a, post_a)[0,1]:.2f}', ha='right', va='bottom', color=INK2, fontsize=7.5)
for axx in ax.ravel(): axx.set_facecolor('white')
fig.tight_layout(w_pad=2.0, h_pad=1.6); fig.savefig(FIG, format='pdf'); fig.savefig(FIG.replace('.pdf', '.png'), dpi=160)
print('written', FIG)
