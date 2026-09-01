TITLE: Prob: restore the k=0 term in the large-lambda lower-tail Poisson CDF

Closes #NNN (companion issue).

`__poisson_cdf_large_lambda` sums from i=1; MACS 1.4 seeded the sum with the
i=0 term (`cdf = next`), and that line was lost in the MACS2 Cython port —
which also left `cdf` formally uninitialized in the 2.x releases. The current
zero-initialization removed the undefined behavior but still omits the term.
This restores it, matching MACS 1.4.

No observable behavior change today: the branch requires λ > 700 (where the
term is ~e^-700 of the total) and no current CLI path reaches the function.
This is correctness for future callers.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012d2sJAD5EUp4GqAStqoBX7
