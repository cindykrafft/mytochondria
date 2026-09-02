"""SP4 impact demo on SPM's MMN tutorial data (subject1.bdf, 512 Hz).
spm_eeg_downsample with method='decimate'|'downsample' and fsample_new=200 calls
ft_preproc_resample, which uses fac=round(512/200)=3, so the data are really at
512/3=170.667 Hz. Pre-fix SPM stamps the file 200 Hz; post-fix 170.667 Hz.
Every downstream time value is derived from the stamped rate."""
import numpy as np, mne
from scipy.signal import decimate
mne.set_log_level('ERROR')
P='/tmp/claude-0/-home-user-afni/d65df75e-7d82-531d-babc-bc1cc192b046/scratchpad/mmn/subject1.bdf'
raw = mne.io.read_raw_bdf(P, preload=True); raw.pick_types(eeg=True, stim=True)
ev = mne.find_events(raw, stim_channel='Status')
fs0 = raw.info['sfreq']; req = 200.0; fac = int(round(fs0/req)); fs_true = fs0/fac
raw.filter(0.5, 30.); raw.set_eeg_reference('average', projection=False)
Xd = decimate(raw.get_data(picks='eeg'), fac, axis=1, zero_phase=True)
evd = ev[:,0]//fac; std_code, dev_code = 65152, 65216

# --- the physics: epoch on the TRUE axis (-100..400 ms), MMN = deviant - standard
pre, post = int(round(0.1*fs_true)), int(round(0.4*fs_true))
def erp(code):
    segs=[Xd[:, s-pre:s+post] for s in evd[ev[:,2]==code] if s-pre>=0 and s+post<=Xd.shape[1]]
    A=np.mean(segs,axis=0); return A - A[:,:pre].mean(axis=1,keepdims=True)
diff = erp(dev_code)-erp(std_code); gfp = diff.std(axis=0)
t_true = (np.arange(diff.shape[1])-pre)/fs_true*1000
win=(t_true>=100)&(t_true<=300); k=np.where(win)[0][np.argmax(gfp[win])]
ch=np.argmax(np.abs(diff[:,k]))
print(f"dataset: {fs0:g} Hz -> requested {req:g} Hz, decimate fac={fac}, TRUE rate {fs_true:.3f} Hz")
print(f"MMN (deviant-standard) GFP peak: sample {k-pre} after onset, max channel {raw.ch_names[ch]} {diff[ch,k]*1e6:+.1f} uV")
print()
for label, fs_lab in [("pre-fix  (file stamped 200 Hz)", req), ("post-fix (file stamped 170.667 Hz)", fs_true)]:
    lat = (k-pre)/fs_lab*1000
    print(f"{label}: MMN peak latency reported = {lat:6.1f} ms   (true {t_true[k]:.1f} ms, error {lat-t_true[k]:+.1f} ms)")
print()
# --- what the user's requested windows really cover under the wrong stamp
for nm,(a,b) in {"epoch window -100..400 ms":(-100,400), "baseline -100..0 ms":(-100,0), "MMN window 100..250 ms":(100,250)}.items():
    a_t, b_t = a*fs_true/req, b*fs_true/req   # samples chosen with stamp 200 Hz, converted to true time
    print(f"{nm:28s} requested under a 200 Hz stamp actually covers {a_t:6.1f}..{b_t:6.1f} ms of real time")
