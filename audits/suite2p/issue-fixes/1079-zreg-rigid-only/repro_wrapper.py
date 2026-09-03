"""End-to-end check for MouseLand/suite2p#1079: registration_wrapper with a list of two
reference images, one and two channels, nonrigid off and on (synthetic data, CPU,
BinaryFile inputs). Before the fix the two nonrigid=False cases fail at register.py:459."""
import os, tempfile, sys
import numpy as np, torch, suite2p
from suite2p.registration import register
rng = np.random.default_rng(0)
n_frames, Ly, Lx = 6, 64, 64
chan1 = rng.normal(1000, 50, (n_frames, Ly, Lx)).astype(np.int16); chan1[:, 10:20, 10:20] += 2000
chan2 = rng.normal(3000, 50, (n_frames, Ly, Lx)).astype(np.int16); chan2[:, 25:40, 25:40] += 2000
refs = [chan1[0].copy(), np.roll(chan1[0], 5, axis=0).copy()]
for nonrigid, twoc in [(False, False), (False, True), (True, False), (True, True)]:
    settings = suite2p.default_settings()["registration"]
    settings.update(dict(do_bidiphase=False, nonrigid=nonrigid, block_size=[32, 32], two_step_registration=False,
                         nimg_init=n_frames, batch_size=3))
    sp = tempfile.mkdtemp(prefix="s2p_1079_")
    paths = {k: os.path.join(sp, k + ".bin") for k in ("raw", "raw2", "reg", "reg2")}
    chan1.tofile(paths["raw"]); chan2.tofile(paths["raw2"]); np.zeros_like(chan1).tofile(paths["reg"]); np.zeros_like(chan2).tofile(paths["reg2"])
    BF = suite2p.io.BinaryFile
    try:
        with BF(Ly, Lx, paths["raw"], n_frames) as f_raw, BF(Ly, Lx, paths["raw2"], n_frames) as f_raw2, \
             BF(Ly, Lx, paths["reg"], n_frames, write=True) as f_reg, BF(Ly, Lx, paths["reg2"], n_frames, write=True) as f_reg2:
            out = register.registration_wrapper(f_reg, f_raw=f_raw, f_reg_chan2=f_reg2 if twoc else None,
                                                f_raw_chan2=f_raw2 if twoc else None, refImg=refs,
                                                align_by_chan2=False, save_path=sp, settings=settings, device=torch.device("cpu"))
        print(f"nonrigid={nonrigid} twochan={twoc}: OK zpos={out.get('zpos_registration')}")
    except Exception as e:
        import traceback; tb = traceback.extract_tb(sys.exc_info()[2])[-1]
        print(f"nonrigid={nonrigid} twochan={twoc}: {type(e).__name__}: {e}  [{os.path.basename(tb.filename)}:{tb.lineno}]")
