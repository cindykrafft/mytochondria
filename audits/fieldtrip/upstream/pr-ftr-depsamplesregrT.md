# PR: ft_statfun_depsamplesregrT: fix undefined variable in the cvar branch

**Target:** `fieldtrip/fieldtrip`, base `master`; branch `fix/depsamplesregrT-cvar`
**Patch:** `0001-ft_statfun_depsamplesregrT-fix-undefined-variable-in.patch`

## Title

```
ft_statfun_depsamplesregrT: fix undefined variable in the cvar branch
```

## Body

```markdown
The control-variable branch of `ft_statfun_depsamplesregrT` indexes `design(cfg.cvar, unitselved)`; the variable is `unitselvec`, so any call with a non-empty `cfg.cvar` fails with `'unitselved' undefined` (line 98). Reproduced on master: without `cfg.cvar` the statfun runs; with `cfg.cvar = 3` it errors. One-character fix.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
```
