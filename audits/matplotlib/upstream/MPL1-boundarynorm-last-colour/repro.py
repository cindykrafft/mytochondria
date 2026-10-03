import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.colors as mcolors

print("matplotlib", matplotlib.__version__, "numpy", np.__version__)
# BoundaryNorm Notes: with fewer bins than colours the index is chosen by
# "linearly interpolating the [0, nbins - 1] range onto the [0, ncolors - 1]
# range", so the last bin should get colour ncolors - 1.
for ncolors, nbins in [(16, 12), (256, 26)]:
    bounds = np.arange(nbins + 1)
    norm = mcolors.BoundaryNorm(bounds, ncolors)
    observed = np.asarray(norm(bounds[:-1] + 0.5))
    expected = (ncolors - 1) * np.arange(nbins) // (nbins - 1)
    print(f"ncolors={ncolors}, nbins={nbins}")
    print("  observed:", observed.tolist())
    print("  expected:", expected.tolist())
    cmap = matplotlib.colormaps["viridis"].resampled(ncolors)
    print("  top bin drawn as RGBA", np.round(cmap(norm(nbins - 0.5)), 4).tolist(),
          "expected", np.round(cmap(ncolors - 1), 4).tolist())
