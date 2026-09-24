# Rules for contributions to Google's open-source repositories

These rules apply to everything written for an upstream project: PR descriptions, issue reports,
commit messages, and replies to maintainers. They also apply to helper agents and sessions that
draft that text.

## Don't overstate. Say only what we know from reading the code.

The maintainers are the experts on their code; we are not. A claim that goes one step past the
evidence costs credibility. On gson #3128 we paraphrased a code comment as assuming invalid strings
are rejected "without a lookup". The comment doesn't say that, and the maintainer had to correct us.

- **Quote, don't paraphrase,** when describing what a comment, doc or maintainer says. Quote the
  exact words and link to the line at a fixed commit.
- **Separate what was checked from what is inferred.** State what the code does, with file:line,
  and what a repro printed, with the output. Mark anything else as an inference or a question: "I
  think", "as far as I can tell", "is that intended?".
- **Don't guess at intent or history.** Don't say what a PR or design "was meant to" do unless its
  own text says so, and then quote it.
- **Keep impact claims to what was shown.** Don't add scenarios that weren't demonstrated, such as
  "several DNS queries", "security issue", "data corruption in production" or "affects all users".
  If the impact is only a plausible consequence, say so, or leave it out.
- **Check claims about other code at its source.** For behaviour of the JDK, libc, the OS or
  another library, read the source or run it before stating it. Otherwise say "in my testing on
  <version>".
- **Keep a modest tone.** Ask rather than assert when the right behaviour is a judgement call. No
  "clearly", "obviously", "exactly" or "always" unless it was verified exhaustively.
- **When corrected, say "you're right" plainly** and fix the text. Don't re-argue the point.

Before any upstream text is handed to the owner, re-read it once against these rules and cut or
soften every sentence that isn't backed by code we read or output we ran.
