"""plotCorrelation --removeOutliers: Correlation.get_outlier_indices scales by median(|x|)
instead of the median absolute deviation. 5,000 Poisson(100) bins plus one bin of 5,000
(50x the median, 700 MADs away) -> nothing is flagged."""
import numpy as np
from deeptools.correlation import Correlation

data = np.random.RandomState(0).poisson(100.0, 5000).astype(float)
data[123] = 5000.0
med = np.median(data)
mad = np.median(np.abs(data - med))
print("median %.0f, MAD %.0f, planted bin is %.0f MADs from the median" % (med, mad, (5000 - med) / (1.4826 * mad)))
print("flagged by get_outlier_indices (threshold 200):", Correlation.get_outlier_indices(data))
assert 123 in Correlation.get_outlier_indices(data), "the outlier was not flagged"
