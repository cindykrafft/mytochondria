TITLE: callpeak: filter the control with its own duplicate threshold

Closes #NNN (companion issue).

With `--keep-dup auto`, `cal_max_dup_tags()` is called separately for the
control and its result logged ("max_dup_tags based on binomial = N"), but the
control was then filtered with the treatment's threshold —
`control_max_dup_tags` was never used. This uses it, and fixes the two log
lines and two xls-header lines that reported the treatment's threshold as the
control's.

**Validation** (MACS3 3.0.4, synthetic BEDs where the treatment threshold is 1
and the control's is 3 — script `keepdup_demo.py` in
cindykrafft/mytochondria, `audits/macs2/verify/`):

| | control reads kept (of 60,000) |
|---|---|
| before | 48,636 (threshold-1 behavior, contradicting the logged 3) |
| after | 59,706 (threshold-3 behavior, matching the log) |

Behavior is unchanged for `--keep-dup all` and for explicit numeric
`--keep-dup` values, where both thresholds are equal. Output changes only for
`--keep-dup auto` runs with a control whose depth differs enough from the
treatment's for the binomial thresholds to differ (roughly 5–10× — see the
companion issue for the threshold table).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
