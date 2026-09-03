import sys, importlib.util, numpy as np, torch
sys.path.insert(0, '.')
spec = importlib.util.spec_from_file_location('pp_main', sys.argv[1]); pp_main = importlib.util.module_from_spec(spec); spec.loader.exec_module(pp_main)
from kilosort import postprocessing as pp_new
rng = np.random.default_rng(0)
n_chan, n_templ, nearest, n_pcs, n_spk = 16, 6, 4, 3, 400
yc = np.arange(n_chan) * 20.0; xc = np.zeros(n_chan)
iCC = torch.from_numpy(np.stack([np.clip(np.arange(c-1, c+3), 0, n_chan-1) for c in range(n_chan)], 1))  # (4, n_chan)
iU = torch.from_numpy(rng.choice(n_chan, n_templ, replace=False))
ops = {'iU': iU, 'iCC': iCC, 'xc': xc, 'yc': yc, 'nearest_chans': nearest, 'dmin': 20, 'dminx': 32}
def run(mod, spike_templates, spike_clusters, tF):
    return mod.make_pc_features(ops, spike_templates.copy(), spike_clusters.copy(), tF.clone())
# case A: each cluster has its own template(s) -> outputs must be identical
spike_templates = rng.integers(0, n_templ, n_spk).astype(np.int32)
clusters_A = (spike_templates // 2).astype(np.int32)          # templates {0,1}->0, {2,3}->1, {4,5}->2
tF = torch.from_numpy(rng.standard_normal((n_spk, nearest, n_pcs)).astype(np.float32))
fa_old, ia_old = run(pp_main, spike_templates, clusters_A, tF); fa_new, ia_new = run(pp_new, spike_templates, clusters_A, tF)
print('non-shared templates: feature_ind identical:', np.array_equal(ia_old, ia_new), '; pc_features identical:', torch.equal(fa_old, fa_new))
# case B: clusters share templates -> old output depends on cluster labelling order, new does not
clusters_B = rng.integers(0, 3, n_spk).astype(np.int32)
fb_new, ib_new = run(pp_new, spike_templates, clusters_B, tF)
perm = np.array([2, 0, 1]); fb2_new, ib2_new = run(pp_new, spike_templates, perm[clusters_B], tF)
print('shared templates, new code: relabelling clusters permutes feature_ind only:', np.array_equal(ib_new, ib2_new[perm]), '; features unchanged:', torch.equal(fb_new, fb2_new))
fb_old, ib_old = run(pp_main, spike_templates, clusters_B, tF); fb2_old, ib2_old = run(pp_main, spike_templates, perm[clusters_B], tF)
print('shared templates, old code: features unchanged under relabelling:', torch.equal(fb_old, fb2_old), '; feature_ind consistent:', np.array_equal(ib_old, ib2_old[perm]))
