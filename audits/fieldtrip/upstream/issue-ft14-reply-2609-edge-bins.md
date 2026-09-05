Title: (comment on #2609) keep the values in the edge bins, or NaN both edges

<!-- Reply to schoffelen's question of 2026-09-03 on issue #2609: accept the last nbin+1 bins as (correct) data, or NaN them because the integration window is incomplete. -->

Either is defensible. My preference is to keep the values, for consistency with the low-frequency edge: the window is already truncated there (`begindx = max(1, k-n)`), so bins 1..nbin have always carried a partial-window value, and NaN-ing only the top bins would treat the two edges differently. With the fix, the top edge does the same thing the low edge has always done: it sums the products that exist.

If a truncated window should be flagged instead, the consistent version is to NaN both ends (bins 1..nbin and the last nbin+1). That changes the low-edge output that existing users see, so it seems like a separate decision. Happy to implement either.
