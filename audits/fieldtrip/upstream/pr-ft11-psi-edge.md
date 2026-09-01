# PR: ft_connectivity_psi: exclude the last frequency bin from the slope window

**Target:** `fieldtrip/fieldtrip`, base `master`; branch `fix/psi-edge-bin`
**Patch:** `0001-ft_connectivity_psi-exclude-the-last-frequency-bin-f.patch`
**Fixes:** the FT11 issue (insert its number)

## Title

```
ft_connectivity_psi: exclude the last frequency bin from the slope window
```

## Body

```markdown
Fixes #NNN11.

`phaseslope` overwrites `x(1:end-1)` with the products conj(C(f))·C(f+δf) but leaves `x(end)` as the raw coherency at the highest frequency, so the last `nbin+1` output bins add `imag(C(fmax))` to the phase slope index; with `normalize='yes'` `coh(end)` stays 0 and those bins are ±Inf.

This zeroes the last element after forming the products and sets its normalizer to 1. Verified (20-bin synthetic coherency, `nbin=3`): the edge bins now match the Nolte et al. (2008) definition to machine precision, and the normalized output is finite everywhere; bins below the edge window are unchanged.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
