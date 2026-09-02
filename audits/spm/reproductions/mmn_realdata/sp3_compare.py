"""Compare SP3 pipeline outputs: pre-fix vs merged badsamples on SPM's MMN tutorial data."""
import numpy as np, scipy.io as sio
S='/tmp/claude-0/-home-user-afni/d65df75e-7d82-531d-babc-bc1cc192b046/scratchpad/mmn/'
P=sio.loadmat(S+'sp3_prefix.mat'); M=sio.loadmat(S+'sp3_merged.mat')
bp, bm = P['bad'].astype(bool), M['bad'].astype(bool)          # chan x samp x trial
t = M['t'].ravel(); fs = 200; base = int(round(0.1*fs))
print(f"bad-mask shape (chan,samp,trial) = {bp.shape}")
print(f"bad samples marked: pre-fix {bp.sum()}  merged {bm.sum()}")
print(f"trials with any bad: pre-fix {np.any(bp,(0,1)).sum()}  merged {np.any(bm,(0,1)).sum()}")
# per (chan,trial) with a bad run in both: where does the run start?
starts_p, starts_m, shifts = [], [], []
for tr in range(bp.shape[2]):
    for ch in range(bp.shape[0]):
        a, b = np.where(bp[ch,:,tr])[0], np.where(bm[ch,:,tr])[0]
        if len(a) and len(b):
            starts_p.append(a[0]); starts_m.append(b[0]); shifts.append(a[0]-b[0])
shifts=np.array(shifts)
print(f"(chan,trial) pairs with a bad run under both: {len(shifts)}; onset shift pre-fix minus merged: "
      f"median {np.median(shifts):.0f} samples = {np.median(shifts)/fs*1000:.0f} ms (baseline = {base} samples = 100 ms)")
overlap = (bp & bm).sum() / max(1,(bp | bm).sum())
print(f"Jaccard overlap of the two bad masks: {overlap:.3f}  (1.0 would mean the fix changed nothing)")
# the fraction of *detected artefact samples* that pre-fix failed to exclude / clean samples it wrongly excluded
tp = (bp & bm).sum(); print(f"of merged (correct) bad samples, pre-fix excluded {tp/bm.sum()*100:.1f}%; "
      f"pre-fix's marked samples that were actually clean: {(bp & ~bm).sum()/bp.sum()*100:.1f}%")
# marks pushed off the end of the epoch (lost entirely)
print(f"bad runs truncated at epoch end: pre-fix {sum(1 for tr in range(bp.shape[2]) for ch in range(bp.shape[0]) if bp[ch,-1,tr])}, merged {sum(1 for tr in range(bm.shape[2]) for ch in range(bm.shape[0]) if bm[ch,-1,tr])}")
# MMN
mp, mm = P['mmn'], M['mmn']; gp, gm = P['gfp'].ravel(), M['gfp'].ravel()
win=(t>=100)&(t<=300); kp=np.where(win)[0][np.argmax(gp[win])]; km=np.where(win)[0][np.argmax(gm[win])]
print(f"\nMMN (robust average, Remove-bad-data=yes): GFP peak pre-fix {t[kp]:.0f} ms ({gp[kp]:.3f}), merged {t[km]:.0f} ms ({gm[km]:.3f})")
d = mm - mp
print(f"max |MMN difference| across channels x time: {np.abs(d).max():.3f} uV at {t[np.unravel_index(np.abs(d).argmax(), d.shape)[1]]:.0f} ms; "
      f"MMN amplitude at merged GFP peak, largest channel: pre-fix {mp[np.abs(mm[:,km]).argmax(),km]:+.2f} vs merged {mm[np.abs(mm[:,km]).argmax(),km]:+.2f} uV")
print(f"RMS of MMN difference over 100-300 ms window: {np.sqrt((d[:,win]**2).mean()):.3f} uV  (vs MMN RMS {np.sqrt((mm[:,win]**2).mean()):.3f} uV)")
