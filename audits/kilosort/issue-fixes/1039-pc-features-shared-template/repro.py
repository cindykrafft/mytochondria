"""Reproduction for MouseLand/Kilosort#1039 (adapted from the reporter's example).

Two final clusters (0 and 1) that share detection template 0, on a two-channel
probe.  Both clusters have their largest PC feature on channel 1, so
pc_feature_ind should be [1, 0] for both, and scattering pc_features back onto
the channels named by pc_feature_ind must reproduce the source features.
"""
import numpy as np
import torch
from kilosort.postprocessing import make_pc_features

ops = {
    "iU": torch.tensor([0]),
    "iCC": torch.tensor([[0], [1]]),
    "xc": np.array([0.0, 0.0]),
    "yc": np.array([0.0, 20.0]),
    "nearest_chans": 2,   # all channels included
    "dmin": 20,
    "dminx": 32,
}

detection_templates = np.zeros(4, dtype=np.int32)          # all from template 0
final_clusters = np.array([0, 1, 0, 1], dtype=np.int32)    # alternate clusters

# columns are channels [0, 1]; one PC per channel
source = np.array([
    [1.0, 20.0],
    [1.0, 10.0],
    [2.0, 18.0],
    [2.0, 8.0],
], dtype=np.float32)

pc_features, pc_feature_ind = make_pc_features(
    ops, detection_templates, final_clusters,
    torch.tensor(source).unsqueeze(-1),
)

restored = np.zeros_like(source)
for spike, cluster in enumerate(final_clusters):
    restored[spike, pc_feature_ind[cluster]] = pc_features[spike, 0].numpy()

print("pc_feature_ind:")
print(pc_feature_ind)
print("restored (should equal source):")
print(restored)
ok_ind = np.array_equal(pc_feature_ind, np.array([[1, 0], [1, 0]], dtype=np.uint32))
ok_val = np.allclose(restored, source)
print(f"pc_feature_ind correct: {ok_ind}; features restored correctly: {ok_val}")
