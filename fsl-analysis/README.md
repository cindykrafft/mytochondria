# FSL bug analysis against 114 published papers (2021–2026) — IN PROGRESS

Companion to `../freesurfer-analysis/`. Same playbook, adapted for FSL.

## Source and filing channels (verified)

- FSL source is public on Oxford WIN's own GitLab (`git.fmrib.ox.ac.uk`), split into
  ~149 per-component repos under the `fsl` group (`randomise`, `cluster` — which also
  holds `smoothest` and the GRF `infer` code — `flameo`, `film`, `feat5`, `flirt`,
  `topup`, `eddy`, `bet2`, `fast4`, `fdt`, `miscmaths`, …). Anonymous cloning works.
- Issues are enabled on those repos, but external account signup appears closed; FSL's
  own docs route outside bug reports to the FSL JISCMail mailing list and reserve the
  contribute path for the team/OxCIN. Filing kit will therefore be email-flavored
  (ready-to-send list posts + git format-patch attachments), with GitLab issue prefill
  links as a bonus if an account is granted.
- Licensing note: the FSL license is non-commercial "source available", not OSI open
  source.

## How the 114 papers use FSL (mined from full text; `fsl_papers.tsv`)

| Feature | Papers |
|---|---|
| Task fMRI GLM (FEAT/FILM) | 25 |
| Distortion correction (topup/eddy) | 24 |
| Linear registration (FLIRT) | 19 |
| Brain extraction (BET) | 16 |
| Permutation inference (randomise/TFCE) | 10 |
| Group mixed effects (FLAME) | 9 |
| Motion correction (MCFLIRT) | 9 |
| Diffusion fitting (dtifit/bedpostx) | 9 |
| Nonlinear registration (FNIRT) | 7 |
| GRF cluster correction | 7 |

Versions named: 5.0.9 (11), 6.0 (8), 6.0.3 (3), others scattered; most unstated.
Journals: PNAS 92, Nature 19, Cell 2, Science 1.

## Status

- [x] Paper profiling (`fsl_profile.py`, `fsl_papers.tsv`)
- [x] Component repos cloned (24 repos, `/home/user/fsl-src` in the analysis container)
- [ ] Adversarial reviews (wave 1 running: FILM/FEAT, FLAME, randomise, cluster/GRF;
      wave 2 queued: FLIRT/MCFLIRT/FNIRT, topup/eddy, BET/FAST/dtifit)
- [ ] Numerical reproductions
- [ ] Filing kit (mailing-list flavored)
