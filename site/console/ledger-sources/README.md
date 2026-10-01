# Ledger classification pass, 2026-10-01

The `status` / `whose_move` / `evidence` fields in `../seen.json` come from a full read of every thread.

- `prompt.tmpl`: the read-only task given to the helper sessions: the status definitions, plus the
  verbatim data each helper had to publish (a JSON block of its proposals, `id="ledger"`, and one of the
  raw thread data, `id="threads"`).
- 29 helper artifacts. The first 9 batched several repositories, but a helper can only read its own
  source repository, so the other repositories were re-read by 20 single-repository helpers. Every
  artifact is listed below.
- `norm.py` and `verify2.py` check each proposal against the raw thread data in the same artifact:
  - the evidence quote appears verbatim, by that author;
  - an `unanswered` thread has no human item or action from anyone but us;
  - a `resolved` thread has a merge, a completed close or a cited fix;
  - a `withdrawn` thread was closed by us.

  Every flagged item was then read by hand.
- Overrides decided on reading:
  - FreeSurfer PRs #1464/#1466/#1468/#1470/#1472 are `rejected`. They are open and unanswered, but
    buildqa declined the issues they fix ("Please do not file the output from code analysis tools as
    de-facto issues").
  - FieldTrip #2622's next move is the maintainers', because FT18 was posted on 2026-10-01.
- `merge.py` wrote the result into `seen.json`, which has a `status_schema` key. It also paired each PR
  with the issues it says it fixes (`fixes`). One pairing came from the kit rather than the PR text:
  lme4 #1000 goes with our comment on #867.

Result: 131 threads (plus 3 internal), 84 findings. The findings are 27 resolved, 14 rejected,
1 withdrawn, 6 in progress (all waiting on the maintainers) and 36 unanswered.

Helper artifacts:
- afni-a https://claude.ai/artifact/5YyC8UzR2Awe2TaTMBxeHG · afni-b https://claude.ai/artifact/HXqV86EzAvWz6GtAusjdUc
- freesurfer https://claude.ai/artifact/BVbNLhwn1A2egFy415HYJR · fieldtrip https://claude.ai/artifact/8XhEBmjad82d9xEj8quEyL
- spm https://claude.ai/artifact/MsUZnEMAbFDP7WEcKGXcrg · deeptools https://claude.ai/artifact/D5SdJmL3bhnJHPXTNyPLfC
- alphafold3 https://claude.ai/artifact/QNYYBq7fRxaZHkZLPj7CHD · samtools https://claude.ai/artifact/BSS9JXpbqCUMo4Hz4aEnkY
- bcftools https://claude.ai/artifact/SgAGM4cFedutkm5HrXYYrY
- kilosort https://claude.ai/artifact/TCeyGVUCHyayAw4GBj3Jro · umap https://claude.ai/artifact/XvBUXQJZH5ArWEUE5rXHyU
- deseq2 https://claude.ai/artifact/EsDpczMuUZDckfcmpgPH5N · plink-ng https://claude.ai/artifact/9bWooByQbmZnrfuPWBNHMA
- cutadapt https://claude.ai/artifact/8hD24M5ydnBffjRQdBnUWX · iqtree3 https://claude.ai/artifact/NKig6sFPf7o9RPKtjHBDFr
- bedtools2 https://claude.ai/artifact/3w6a7YT7DwabCwjgmwwkkM · lme4 https://claude.ai/artifact/1aSnDoj1xHGhffrSAxZuwB
- STAR https://claude.ai/artifact/Gtxx9esSa94hBEFLZg8HXB · MACS https://claude.ai/artifact/PuwaVmjDYNiLf86f1xmUyu
- fastp https://claude.ai/artifact/2hpVR7zjRVv32BrGhW5882 · gsea-desktop https://claude.ai/artifact/CVrexPfZkdAZtxPb8EQNGi
- htseq https://claude.ai/artifact/Tzxa8kJTdGqBcpS54BjveF · CellphoneDB https://claude.ai/artifact/MYnXKVRzHZCz878ZU6B1q2
- scanpy https://claude.ai/artifact/VDwSJKmgPVBaD1e3SjWah7 · Trimmomatic https://claude.ai/artifact/7QfrUYXPNLiPa8egMmQbiA
- clusterProfiler https://claude.ai/artifact/ERKDPepc6hzohBkP9UnEYx · picard https://claude.ai/artifact/WHfQDLxbSVKvWV9CxXNSEt
- suite2p https://claude.ai/artifact/NfWfTbYmJDXcKTs36mcfyN · fieldtrip/website https://claude.ai/artifact/CDNGitA1UnDnwjACa15Zq8

`merge.py` and `verify2.py` read the artifacts from the session scratchpad. They are kept here as the
record of how the pass was done, not as tools the watcher runs.
