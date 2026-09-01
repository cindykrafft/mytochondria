# PR: Warn about uncorrected two-sided testing for any alpha

**Target:** `fieldtrip/fieldtrip`, base `master`; branch `fix/twosided-warning`
**Patch:** `0001-Warn-about-uncorrected-two-sided-testing-for-any-alp.patch`

## Title

```
Warn about uncorrected two-sided testing for any alpha
```

## Body

```markdown
`ft_statistics_montecarlo` warns that a two-sided test with `cfg.correcttail='no'` evaluates each tail at the full alpha, but only when `cfg.alpha==0.05` exactly. A user who sets alpha to 0.01 or 0.1 is in the same situation and gets no warning. This drops the alpha condition so the warning is issued whenever `cfg.tail==0` and `cfg.correcttail=='no'`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
