# Documentation principles: detailed reference

Each entry gives the principle, why it matters, signs that it is being broken, and how to
fix it. The principles are grouped by what they apply to.

## General (the documentation process)

### Precursory: document before you develop
- **Why:** Requirements and specifications are the first draft of the docs. Writing them
  early clarifies the path forward and invites peer feedback before code is expensive
  to change (documentation-driven design).
- **Signs it is broken:** Docs are written only after release. Design decisions exist only
  in people's heads or chat logs.
- **Fix:** Start with a README or design doc. Keep the spec in the repo and turn it into
  user docs as features land.

### Participatory: everyone documents
- **Why:** Developers hold the most in-demand knowledge. Readers know where the docs fail
  them. Siloed docs stay thin.
- **Signs it is broken:** Only one person or team ever edits the docs. Readers have no
  feedback channel.
- **Fix:** Make doc changes part of the normal development workflow, for example by
  requiring them in pull requests. Give readers a visible way to comment, suggest, or
  edit. Weigh open editing against your capacity to review it.

## Content (the information itself)

### ARID: Accept (some) Repetition In Documentation
- **Why:** Docs inevitably restate some of what the code expresses. Strict DRY makes docs
  unusable, and full WET makes them unmaintainable.
- **Signs it is broken:** Either readers must follow five links to understand one task, or
  the same paragraph is copied across many pages and the copies disagree.
- **Fix:** Keep content as DRY as is practical. Repeat only the minimum a reader needs in
  context. Remember that any repetition is a reminder to update docs whenever the code
  changes.

### Skimmable: write like a newspaper, not a novel
- **Why:** Most readers arrive with a specific question and want to skip what they know.
- **Signs it is broken:** Vague headings ("Overview", "Misc"). Key terms buried mid-paragraph.
  Link text like "click here".
- **Fix:** Use descriptive, concise headings. Start paragraphs and list items with the
  identifiable concept. Make link text describe the destination.

### Exemplary: include (some) examples
- **Why:** Many readers look for an example first.
- **Signs it is broken:** There are no examples, or so many that the page cannot be skimmed.
  Examples are mixed into dense reference tables.
- **Fix:** Show examples for the most common use cases only. Keep tutorials and examples
  separate from reference material.

### Consistent: same language and formatting
- **Why:** Consistency lowers cognitive load and supports skimmability and visual polish.
  It matters more as the number of authors grows.
- **Signs it is broken:** One thing has several names. Capitalization, code formatting, and
  voice vary from page to page.
- **Fix:** Adopt or write a style guide (see the `docs-review` skill). Keep a terminology list.

### Current: incorrect docs are worse than missing docs
- **Why:** Users act on what the docs say. Outdated instructions cause failures and
  destroy trust.
- **Signs it is broken:** Removed flags, old screenshots, hard-coded version numbers, docs
  that describe a release nobody runs.
- **Fix:** Update docs in the same change as code. Write version-agnostic instructions where
  possible. Publish versioned docs for users on older releases.

## Sources (where content is stored)

### Nearby: store sources close to the code
- **Why:** Docs that live beside the code get updated with it.
- **Signs it is broken:** Docs live in a separate wiki or CMS that developers never touch.
- **Fix:** Keep docs in the same repository, or in docstrings and comments where it fits,
  so that code and doc changes happen together.

### Unique: no overlapping sources
- **Why:** Parallel copies drift apart, or one stops being maintained.
- **Signs it is broken:** The same install steps are in the README, the wiki, and the website,
  and each says something different.
- **Fix:** Give each source a clearly defined scope that does not overlap with others.
  Everywhere else, link to the single source or generate from it.

## Publications (what readers consume)

### Discoverable: funnel readers in from every likely path
- **Why:** Docs nobody can find might as well not exist.
- **Signs it is broken:** No docs link in the README, package metadata, `--help`, error
  messages, or app UI.
- **Fix:** List every place a reader might look and put a pointer in each. The docs do not
  need to be in those places, only links to them.

### Addressable: granular, linkable locations
- **Why:** Readers bookmark, share, and give feedback about specific sections.
- **Signs it is broken:** Very long pages with no anchors, unstable generated IDs, PDFs
  without section numbers.
- **Fix:** Use stable heading anchors and meaningful URLs, or page and section numbers in
  print.

### Cumulative: prerequisites first
- **Why:** Readers who jump in partway should be able to "rewind" to fill a gap.
- **Signs it is broken:** A tutorial uses a concept that is explained only later. Reference
  material comes before the tutorials.
- **Fix:** Put tutorials and examples before reference material, ordered by prerequisite.
  Reference can then be alphabetical or topical.

### Complete: cover a concept fully, or not at all
- **Why:** A map that shows half the fire hydrants is worse than one that shows none,
  because it misleads. A publication can be complete without covering everything. It
  must be complete for the *kinds* of things it chooses to cover. (Example: the `iconv`
  man page documents every option but delegates the list of encodings to `iconv -l`.
  Both publications are complete.)
- **Signs it is broken:** Some CLI flags or API endpoints are documented and others silently
  are not.
- **Fix:** Document all items of a type, or delegate to another complete publication. If you
  must publish something partial, state the gap clearly at the top.

### Beautiful: intentional visual style
- **Why:** Some readers struggle with docs that look careless, and this is true even of
  plain-text `--help` output.
- **Signs it is broken:** Inconsistent spacing, capitalization, and layout, or walls of text.
- **Fix:** Be deliberate about layout and formatting. If visual style isn't your strength,
  ask someone for whom it is.

## Body (all publications together)

### Comprehensive: answer the likely questions
- **Why:** You cannot answer every obscure question, but you can answer the likely ones.
  A doc set that answers rare questions while missing common ones is out of balance.
- **Signs it is broken:** Support tickets and issues repeat the same questions. Search finds
  nothing for common tasks.
- **Fix:** Collect real questions from issues, support, and search logs, and make sure some
  publication answers each. It is fine for an answer to span several publications.

---

*Adapted from "[Documentation principles](https://www.writethedocs.org/guide/writing/docs-principles/)" (source: [`docs/guide/writing/docs-principles.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/docs-principles.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed, reorganized, and rewritten as agent instructions with failure signs and fixes, by Yuming Fu, 2026.*
