# PR: extract_traces: build sparse-mask indices as integer tensors

**Target:** `MouseLand/suite2p`, base `main`; branch `fix/extract-index-dtype`
**Patch:** `0001-extract_traces-build-sparse-mask-indices-as-integer-.patch`

## Title

```
extract_traces: build sparse-mask indices as integer tensors
```

## Body

```markdown
`extract_traces` creates the pixel/ROI index tensors for the sparse cell and neuropil mask matrices with `torch.Tensor([...])`, i.e. float32, which represents integers exactly only up to 2**24 = 16,777,216 (`torch.Tensor([16777217]).long()` gives 16777216). Flattened pixel indices in fields of view larger than about 4096 × 4096 are therefore rounded to a neighbouring pixel, silently mixing pixels between ROIs. This creates the index tensors as int64 directly; behaviour is unchanged for smaller fields of view.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
