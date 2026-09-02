#!/usr/bin/env python3
"""S4/S5: two small numeric facts behind code-read findings.

S4: nonrigid.transform_data returns fr_shift.squeeze().short() - truncation
    toward zero of the bilinearly interpolated frame, not rounding, so every
    nonrigidly registered frame carries a mean offset of about -0.5 intensity
    units (for positive data).
S5: extraction.extract_traces builds the pixel/ROI index tensors with
    torch.Tensor([...]) (float32), which represents integers exactly only up
    to 2**24 = 16,777,216; flattened pixel indices beyond that (fields of
    view larger than ~4096 x 4096) are rounded to a neighbouring pixel.

Expected output:

    S4 .short() truncation: mean(x - x.short()) = 0.4999  (rounding would give ~0)
    S5 float32 index tensor: 16777216 -> 16777216  (exact)
    S5 float32 index tensor: 16777217 -> 16777216  (WRONG)
    S5 float32 index tensor: 16789561 -> 16789560  (WRONG)
"""
import torch
x = torch.rand(1_000_000) * 2000 + 100
print("S4 .short() truncation: mean(x - x.short()) = %.4f  (rounding would give ~0)"
      % (x - x.short().float()).mean())
for npix in [2**24, 2**24 + 1, 4096 * 4096 + 12345]:
    t = torch.Tensor([npix]).long().item()
    print(f"S5 float32 index tensor: {npix} -> {t}  ({'exact' if t == npix else 'WRONG'})")
