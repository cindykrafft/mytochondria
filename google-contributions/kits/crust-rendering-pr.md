**Title:** Fix course pages that render incorrectly

A few pages don't render the way their source intends. I found most of these through `mdbook build` warnings, and I checked each one in a local build (mdbook 0.5.3, the version pinned in MODULE.bazel) before and after the change.

- **Outline tables drop generic parameters.** mdbook-course writes chapter names into the outline tables without escaping, so `Box<T>` renders as "Box" in the Smart Pointers outline, and `Pin<Ptr>` as "Pin" in the Pinning outline (mdbook warns "unclosed HTML tag `<t>`"). `Table::add_row` now escapes `&`, `<` and `>`. I added a unit test, and `cargo test -p mdbook-course` passes.
- **course-structure.md:** `{{%course outline Unsafe}}` renders as "not found - {{%course outline Unsafe}}" on the published page. The course is named `Unsafe Deep Dive` in unsafe-deep-dive/welcome.md, and `find_course` compares names exactly, so the directive now uses the full name.
- **unsafe-deep-dive/safety-preconditions/references.md:** the page closes a `</details>` but never opens one, so the speaker notes and the suggested solution show on the slide. I added `<details>` after the first code block. Could you check that this is where the notes are meant to start?
- **chromium/.../generating-gn-build-rules.md:** `</detail>` → `</details>`.
- **unsafe-deep-dive/initialization/maybeuninit.md and zeroed-method.md:** `MaybeUninit<T>` outside backticks renders as "MaybeUninit". Now in backticks.
- **modules/solution.md:** removed 9 leftover `// ANCHOR:` / `// ANCHOR_END:` lines. They are in plain code blocks, so they show on the page, and exercise.rs no longer defines those anchors.
- **references/exercise.md:** removed `{{#include exercise.rs:magnitude}}` and `{{#include exercise.rs:normalize}}`. exercise.rs has no such anchors, so they render as empty lines.
- **running-the-course.md:** the installation link pointed at `#building`, but the README has no such heading. It now points at `#setup`.

After this change the only `mdbook build` warning left is the one in unsafe-deep-dive/pinning.md, which #3284 fixes. `mdbook test` and `dprint check` pass.
