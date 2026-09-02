# Suite2p verification scripts

Run inside a venv with `pip install suite2p` (verified with suite2p 1.1.0,
torch 2.13 CPU; no GPU needed). Expected outputs are in each docstring.

- `s2_bidiphase_torch.py` — odd-line corruption of `bidiphase.shift` on torch
  tensors, unit level and end-to-end through `register_frames`.
- `s1_classifier_bins.py` — the last-bin wrap for features at the training
  minimum, on the builtin classifier, plus its effect on the training set.
- `s4_s5_numeric.py` — the int16 truncation bias and the float32 index limit.

To validate a patched tree: `PYTHONPATH=/path/to/patched/suite2p python <script>`
from a directory that does not contain an unpatched `suite2p/` (cwd shadows
PYTHONPATH).
