# NumPy upstream notes

_Prepared 2026-09-25 against `numpy/numpy` `main` @ `55511445dc`. **Nothing to file, nothing
pushed.** The audit found no wrong number for a documented definition; the one measurable
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
