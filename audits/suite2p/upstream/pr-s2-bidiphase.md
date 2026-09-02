# PR: bidiphase.shift: copy the source slice before the overlapping in-place assignment

**Target:** `MouseLand/suite2p`, base `main`; branch `fix/bidiphase-torch-overlap`
**Patch:** `0001-bidiphase.shift-copy-the-source-slice-before-the-ove.patch`
**Fixes:** the S2 issue (insert its number)

## Title

```
bidiphase.shift: copy the source slice before the overlapping in-place assignment
```

## Body

```markdown
Fixes #NNN2.

`bidiphase.shift` shifts the odd scan lines with an in-place assignment whose source and destination slices overlap. numpy handles that with a temporary copy; `torch.Tensor.copy_` does not, so since the registration path started passing torch tensors (v1.0.0.1) every odd line was corrupted instead of shifted (with `bidiphase=3`, 34 % of odd-line pixels in `register_frames`' output differ from the intended shift), while the reference image — still shifted through the numpy path in `registration_wrapper` — was correct.

This copies the source slice first (`clone()` for torch, `copy()` for numpy), restoring the numpy semantics for both array types. Verified on 1.1.0 + this patch: `register_frames(..., bidiphase=3)` reproduces the numpy result exactly, for positive and negative offsets.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
