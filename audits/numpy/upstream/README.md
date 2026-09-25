# NumPy upstream notes

_Prepared 2026-09-25 against `numpy/numpy` `main` @ `55511445dc`. **Nothing filed, nothing
pushed.**_

## Full inspection kit (2026-09-25)

Two filings, in order; the reasons are in `../full-inspection.md` § Filing order:

1. **NP3**: `issue-np3-unique-nat-equal-nan.md` (fact sheet for `bug-report.yml`), then the PR from
   `0001-BUG-unique-hash-path-honour-equal_nan-for-NaT-pick-t.patch`. It is one commit on `main` @
   `55511445dc`, branch `fix/unique-hash-nat-complex-nan` in the audit clone, and needs a fork of
   numpy/numpy under `cindykrafft`. PR facts and AI disclosure: `pr-bodies.md`.
2. **NP5**: `issue-np5-select-wraps-python-int.md` (fact sheet; no patch prepared).

Everything here is a fact sheet. NumPy's AI policy says "do not use AI to automatically generate
comments, pull request descriptions, or issue descriptions" and "do not use AI to speak for you" in
threads. It also says an AI agent may not submit a PR autonomously, and the PR must carry the AI
disclosure. The reproducers and their outputs can be pasted; the prose is the submitter's. The
security policy (`doc/source/reference/security.rst`) classes segfaults that need NumPy calls as
bugs, not vulnerabilities, so NP2 is queued as a public issue.

## Round 6 (survey-driven) notes

_The round-6 audit found no wrong number for a documented definition; the one measurable
behaviour (float32 reductions along the slow axis, N1 in `../README.md`) is documented and
already open upstream (numpy/numpy#22956, 2023; #8869, 2017; the summation-algorithm thread
#8786), and N2 was fixed in 2.1.0._

## Channel, for any later filing

- `doc/source/dev/ai_policy.rst`: "AI" means generative tools such as LLMs; any PR using AI-generated
  code or text must say so, name the tools and what was generated, and undisclosed use is
  rejected; copyright-questionable contributions are rejected. `.github/PULL_REQUEST_TEMPLATE.md`
  repeats the disclosure requirement and links the policy.
- Issue templates: `bug-report.yml`, `documentation.yml`, `feature-request.yml`, `post-install.yml`,
  `typing.yml`.
- Threads read in full through a helper session (artifact "Mytochondria threads numpy 22956 8869
  8786"): see `../README.md` § Filing channel for what they contained.
