Title: (comment on #212) agree with the plan; PR to follow, two questions first

<!-- Reply to s-andrews (OWNER) on #212, 2026-10-02 07:10 UTC (issuecomment-5947171884): confirms the bug as "a known limitation of quality value detection" and lays out the fix he wants: (1) stop autodetecting and default to Phred+33 (he writes "Phred32"), (2) warn on an ASCII value implying an unrealistically high score (">= 80 for example"), (3) a --phred64 option, (4) an error if --phred64 is chosen and the file holds values incompatible with it. Thread read in full 2026-10-02 through a helper session (transcript https://claude.ai/code/artifact/371dd757-fc21-45a4-aea0-566f4ae06dfb). Code touched: PhredEncoding.getFastQEncodingOffset (called from BasicStats, PerBaseQualityScores, PerSequenceQualityScores, PerTileQualityScores), FastQCConfig (system properties), and the Python launcher `fastqc` (argparse -> -Dfastqc.* properties). Open PR #210 (ewels) also changes encoding choice for BAM/SAM, hence the second question. Nothing is written or pushed until the owner approves this reply. -->

Thanks, that plan makes sense. I'll put together a PR along those lines:

1. The quality encoding defaults to Phred+33; the lowest-character guess goes.
2. A warning when a quality character at or above ASCII 80 appears (Q47 or higher under Phred+33), since that suggests the file is Phred+64.
3. A `--phred64` option in the launcher, passed through as a `fastqc.phred64` property like the other options.
4. With `--phred64`, an error if the file contains a quality character below ASCII 64.

Two questions before I start:

- Should the warning only go to stderr, or also show up in the report (for example, as a line in Basic Statistics)?
- #210 also changes how the encoding is chosen, for BAM/SAM input. Would you prefer this built on top of #210, or kept separate and rebased by whichever lands second?
