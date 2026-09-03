"""Figure 1 of the SPM preprint: (A) the chi-squared EC-density defect, exact ratio;
(B) the artefact-window defect on trial 5 of SPM's MMN tutorial participant;
(C) the robust-averaged MMN before/after the badsamples fix; (D) the sampling-rate
stamp defect: the same MMN under the true and the pre-fix time axis.
Inputs: audits/spm/reproductions/mmn_realdata/ results; the MMN tutorial BDF for (D)."""
import numpy as np, scipy.io as sio, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from math import log, pi, exp
from scipy.special import gammaln
import sys, os
S = sys.argv[1]           # scratch dir holding mmn/ (sp3_*.mat, subject1.bdf)
OUT = sys.argv[2]
BLUE, ORANGE = '#2a78d6', '#eb6834'          # after fix / before fix (validated pair)
INK, INK2, MUTED, GRID, AXIS = '#0b0b0b', '#52514e', '#898781', '#e1e0d9', '#c3c2b7'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':8,'axes.edgecolor':AXIS,'axes.labelcolor':INK2,
    'xtick.color':MUTED,'ytick.color':MUTED,'axes.titlesize':9,'axes.titleweight':'bold','axes.titlecolor':INK,
    'axes.spines.top':False,'axes.spines.right':False,'legend.frameon':False,'legend.fontsize':7.5})
fig, ax = plt.subplots(2, 2, figsize=(7.0, 5.2)); fig.patch.set_facecolor('white')

# ---------- A: chi-squared EC density ratio shipped / correct ----------
a = ax[0,0]; t = np.linspace(4, 40, 200)
a.plot(t, np.sqrt(t), color=BLUE, lw=1.6, label='2-D density: ratio = √t')
a.plot(t, t,          color=BLUE, lw=1.6, ls='--', label='3-D density: ratio = t')
a.axhline(1, color=AXIS, lw=0.8); a.text(39.5, 1.12, '0- and 1-D densities: exact', ha='right', color=INK2, fontsize=7)
a.set_yscale('log'); a.set_xlabel('threshold t'); a.set_ylabel('shipped ÷ correct (log)')
a.set_title('A  χ² EC densities: wrong power of t'); a.grid(axis='y', color=GRID, lw=0.6); a.legend(loc='center left')

# ---------- B: trial-5 window placement (200 Hz, timeOnset -0.1 s) ----------
b = ax[0,1]; fs, t0 = 200.0, -0.1
def ms(sample): return (t0 + (sample-1)/fs)*1000     # 1-based epoch sample -> ms
rows = [('detector wrote', 30, 30+26, MUTED), ('marked, before fix', 51, 77, ORANGE), ('marked, after fix', 31, 57, BLUE)]
b.axvspan(-100, 0, color=GRID, alpha=0.6, lw=0); b.text(-50, 2.62, 'baseline', ha='center', color=INK2, fontsize=7)
for i,(lab,s0,s1,c) in enumerate(rows):
    y = 2-i; b.barh(y, ms(s1)-ms(s0), left=ms(s0), height=0.5, color=c, lw=0)
    b.text(ms(s0)-8, y, lab, ha='right', va='center', color=INK, fontsize=7.5)
b.annotate('', xy=(ms(51), 1.38), xytext=(ms(30), 1.38), arrowprops=dict(arrowstyle='->', color=INK, lw=1))
b.text((ms(30)+ms(51))/2, 1.5, '+100 ms', ha='center', color=INK, fontsize=7.5)
b.set_xlim(-100, 400); b.set_ylim(-0.6, 2.9); b.set_yticks([]); b.set_xlabel('time from tone (ms)')
b.set_title('B  One artefact window, trial 5'); b.axvline(0, color=AXIS, lw=0.8)

# ---------- C: MMN GFP before/after the badsamples fix ----------
c = ax[1,0]
P = sio.loadmat(f'{S}/mmn/sp3_prefix.mat'); M = sio.loadmat(f'{S}/mmn/sp3_merged.mat')
tt = M['t'].ravel(); gp, gm = P['gfp'].ravel(), M['gfp'].ravel()
c.plot(tt, gp, color=ORANGE, lw=1.6, label='before fix'); c.plot(tt, gm, color=BLUE, lw=1.6, ls=(0,(4,2)), label='after fix')
c.axvspan(-100, 0, color=GRID, alpha=0.6, lw=0); c.set_xlim(-100, 400)
c.set_xlabel('time from tone (ms)'); c.set_ylabel('MMN global field power (µV)')
k = np.argmax(gm*(tt>=100)*(tt<=300)); c.plot(tt[k], gm[k], 'o', color=BLUE, ms=6, mec='white', mew=1)
c.text(tt[k]-10, gm[k], f'peak {tt[k]:.0f} ms, both', va='center', ha='right', color=INK, fontsize=7.5)
c.text(395, 0.15, 'RMS difference 100–300 ms: 1.5%', ha='right', color=INK2, fontsize=7.5)
c.set_title('C  Robust-averaged MMN, before and after'); c.grid(axis='y', color=GRID, lw=0.6); c.legend(loc='upper left')

# ---------- D: sampling-rate stamp: same MMN on true vs reported axis ----------
d = ax[1,1]
import mne; from scipy.signal import decimate; mne.set_log_level('ERROR')
raw = mne.io.read_raw_bdf(f'{S}/mmn/subject1.bdf', preload=True); raw.pick_types(eeg=True, stim=True)
ev = mne.find_events(raw, stim_channel='Status'); fs0=raw.info['sfreq']; fac=int(round(fs0/200)); fst=fs0/fac
raw.filter(0.5,30.); raw.set_eeg_reference('average', projection=False)
Xd = decimate(raw.get_data(picks='eeg'), fac, axis=1, zero_phase=True); evd = ev[:,0]//fac
pre, post = int(round(0.1*fst)), int(round(0.4*fst))
def erp(code):
    segs=[Xd[:, s-pre:s+post] for s in evd[ev[:,2]==code] if s-pre>=0 and s+post<=Xd.shape[1]]
    A=np.mean(segs,axis=0); return A-A[:,:pre].mean(axis=1,keepdims=True)
gfp4 = 1e6*(erp(65216)-erp(65152)).std(axis=0); ttrue = (np.arange(len(gfp4))-pre)/fst*1000; trep = ttrue*fst/200.0
k4 = np.where((ttrue>=100)&(ttrue<=300))[0][np.argmax(gfp4[(ttrue>=100)&(ttrue<=300)])]
d.plot(ttrue, gfp4, color=BLUE, lw=1.6, label='after fix (stamped 170.7 Hz)')
d.plot(trep,  gfp4, color=ORANGE, lw=1.6, label='before fix (stamped 200 Hz)')
for x, col in [(ttrue[k4], BLUE), (trep[k4], ORANGE)]:
    d.plot(x, gfp4[k4], 'o', color=col, ms=6, mec='white', mew=1)
d.annotate('', xy=(trep[k4], gfp4[k4]*1.12), xytext=(ttrue[k4], gfp4[k4]*1.12), arrowprops=dict(arrowstyle='->', color=INK, lw=1))
d.text((trep[k4]+ttrue[k4])/2, gfp4[k4]*1.17, f'{ttrue[k4]:.0f} → {trep[k4]:.0f} ms', ha='center', color=INK, fontsize=7.5)
d.set_xlim(-100, 400); d.set_ylim(0, gfp4.max()*1.35); d.set_xlabel('time from tone (ms)'); d.set_ylabel('MMN global field power (µV)')
d.set_title('D  Sampling-rate stamp: two clocks'); d.grid(axis='y', color=GRID, lw=0.6); d.legend(loc='lower right')
for axx in ax.ravel(): axx.set_facecolor('white')
fig.tight_layout(w_pad=2.0, h_pad=1.6); fig.savefig(OUT, format='pdf'); fig.savefig(OUT.replace('.pdf','.png'), dpi=160)
print('figure written:', OUT, '| panel D peak true %.1f ms reported %.1f ms' % (ttrue[k4], trep[k4]), '| panel C peak %.0f ms' % tt[k])
