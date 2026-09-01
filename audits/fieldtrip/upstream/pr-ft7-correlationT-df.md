# PR: ft_statfun_correlationT: use n-2 degrees of freedom

**Target:** `fieldtrip/fieldtrip`, base `master`; branch `fix/correlationT-df`
**Patch:** `0001-ft_statfun_correlationT-use-n-2-degrees-of-freedom.patch`

## Title

```
ft_statfun_correlationT: use n-2 degrees of freedom
```

## Body

```markdown
`ft_statfun_correlationT` computes `t = r*sqrt(n-2)/sqrt(1-r^2)`, which has n−2 degrees of freedom, but sets `df = nrepl - 1`. The parametric critical value used as the cluster-forming threshold (and the optional parametric `prob`) is therefore computed with one degree of freedom too many, i.e. a slightly liberal threshold:

    n= 8: FieldTrip df=7 critval=2.3646 | correct df=6 critval=2.4469 | ratio 0.966
    n=12: FieldTrip df=11 critval=2.2010 | correct df=10 critval=2.2281 | ratio 0.988
    n=20: FieldTrip df=19 critval=2.0930 | correct df=18 critval=2.1009 | ratio 0.996

Both lines date from the same 2015 overhaul commit (2a54f12). One-line fix; the `df<1` guard is unchanged (it now requires n ≥ 3, which the statistic needs anyway).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
