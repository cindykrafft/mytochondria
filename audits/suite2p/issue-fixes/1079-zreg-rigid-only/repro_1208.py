"""Reproduction for MouseLand/suite2p#1208: with reg_tif=True and reg_tif_chan2=True,
the second-channel registration writes its tiffs into reg_tif/ (overwriting the
functional-channel tiffs) and leaves reg_tif_chan2/ empty.

Synthetic two-channel movie, CPU, numpy arrays in place of binary files.
"""
import os, tempfile, glob
import numpy as np
import torch
import tifffile
import suite2p
from suite2p.registration import register

rng = np.random.default_rng(0)
n_frames, Ly, Lx = 6, 48, 48
chan1 = (rng.normal(1000, 50, (n_frames, Ly, Lx))).astype(np.int16)
chan2 = (rng.normal(3000, 50, (n_frames, Ly, Lx))).astype(np.int16)
chan1[:, 10:20, 10:20] += 2000      # bright square in the functional channel
chan2[:, 25:40, 25:40] += 2000      # different bright square in channel 2

settings = suite2p.default_settings()["registration"]
settings.update(dict(reg_tif=True, reg_tif_chan2=True, do_bidiphase=False,
                     nonrigid=False, two_step_registration=False,
                     nimg_init=n_frames, batch_size=3))

save_path = tempfile.mkdtemp(prefix="s2p_1208_")
paths = {k: os.path.join(save_path, k + ".bin") for k in ("raw", "raw2", "reg", "reg2")}
chan1.tofile(paths["raw"]); chan2.tofile(paths["raw2"])
np.zeros_like(chan1).tofile(paths["reg"]); np.zeros_like(chan2).tofile(paths["reg2"])
BF = suite2p.io.BinaryFile
with BF(Ly, Lx, paths["raw"], n_frames) as f_raw, BF(Ly, Lx, paths["raw2"], n_frames) as f_raw2, \
     BF(Ly, Lx, paths["reg"], n_frames, write=True) as f_reg_bf, BF(Ly, Lx, paths["reg2"], n_frames, write=True) as f_reg2_bf:
    out = register.registration_wrapper(f_reg_bf, f_raw=f_raw, f_reg_chan2=f_reg2_bf, f_raw_chan2=f_raw2,
                                        align_by_chan2=False, save_path=save_path,
                                        settings=settings, device=torch.device("cpu"))
f_reg = np.fromfile(paths["reg"], np.int16).reshape(n_frames, Ly, Lx)
f_reg2 = np.fromfile(paths["reg2"], np.int16).reshape(n_frames, Ly, Lx)

print("suite2p", suite2p.version)
for sub in ("reg_tif", "reg_tif_chan2"):
    files = sorted(glob.glob(os.path.join(save_path, sub, "*.tif")))
    print(f"{sub}: {len(files)} tiff file(s)")
    if files:
        mov = np.concatenate([tifffile.imread(f) for f in files], axis=0)
        print(f"  frames in tiffs: {mov.shape[0]}, mean = {mov.mean():.0f}")
        print(f"  equals registered channel 1 (f_reg):       {np.array_equal(mov, f_reg)}")
        print(f"  equals registered channel 2 (f_reg_chan2): {np.array_equal(mov, f_reg2)}")
print("registered channel means: chan1 %.0f  chan2 %.0f" % (f_reg.mean(), f_reg2.mean()))
