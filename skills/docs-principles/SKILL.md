---
name: docs-principles
description: Quality rubric for software documentation based on the Write the Docs documentation principles (ARID, skimmable, exemplary, consistent, current, nearby, unique, discoverable, addressable, cumulative, complete, beautiful, comprehensive). Use when auditing or scoring existing docs, deciding how to structure a doc set, resolving "where should this content live?", or when another docs skill asks for a principles check.
license: CC-BY-NC-SA-4.0
metadata:
  author: Yuming Fu
  source: Write the Docs Documentation Guide (writethedocs/www@c37669d)
---

# Documentation principles

Software has DRY and KISS; documentation has its own shared principles. Use them as a
rubric when you write, restructure, or review docs. The full explanation of each
principle, with failure signs and fixes, is in
[references/principles.md](references/principles.md). Load it when you need to justify
a finding or the user asks "why".

## The rubric at a glance

| Scope | Principle | One-line test |
|---|---|---|
| Process | **Precursory** | Did docs (specs, README) start before or with the code? |
| Process | **Participatory** | Can developers *and* readers contribute or give feedback easily? |
| Content | **ARID** | Is repetition limited to what readers truly need in each place? |
| Content | **Skimmable** | Can a reader find or skip a concept from headings and first words alone? |
| Content | **Exemplary** | Are the most common use cases shown with examples, separate from dense reference? |
| Content | **Consistent** | Same terms, formatting, and voice throughout (ideally per a style guide)? |
| Content | **Current** | Is anything wrong or out of date? Wrong docs are worse than no docs. |
| Sources | **Nearby** | Is the source stored next to the code it documents (same repo, docstrings)? |
| Sources | **Unique** | Does each fact have exactly one source of truth? |
| Publication | **Discoverable** | Do all the places readers look point to the docs? |
| Publication | **Addressable** | Can readers link to a specific section (stable anchors, URLs)? |
| Publication | **Cumulative** | Are prerequisites covered before the things that depend on them? |
| Publication | **Complete** | For each kind of thing covered, is *every* instance covered, or is the gap stated up front? |
| Publication | **Beautiful** | Is visual style (spacing, capitalisation, layout) intentional? |
| Body | **Comprehensive** | Together, do the publications answer the questions users are *likely* to ask? |

Vocabulary: a **source** is where content is stored and edited (Markdown files, docstrings,
CMS records). A **publication** is one thing readers consume (website, man page, `--help`,
PDF, API reference). The **body** is all publications of a project.

## How to run a principles audit

1. **Scope it.** Identify the sources, the publications they produce, and the main
   audiences (users vs contributors). Ask if this is unclear.
2. **Sample.** For large doc sets, review the entry points (README, index, getting started)
   in full, then a representative sample of reference and how-to pages.
3. **Score each principle** as `pass`, `partial`, or `fail`. Give concrete evidence:
   file path and heading, a quoted phrase under 15 words, or a missing item.
   Mark `n/a` only when a principle truly does not apply.
4. **Prioritise.** Order the fixes by reader impact. Incorrect content (Current) and
   missing entry points (Discoverable) usually come first. Beauty and minor
   consistency come last.
5. **Propose fixes.** Make each fix actionable (what to change, where). Offer to apply
   them, using `project-docs`, `docs-review`, or `docs-tooling` as appropriate.

Output template:

```markdown
## Docs principles audit: <project>
**Scope:** <sources → publications>, audience: <...>

| Principle | Score | Evidence | Fix |
|---|---|---|---|
| Current | fail | `docs/install.md` "Install" uses removed flag `--legacy` | Replace with `--compat`; add CI check |
...

### Top 3 fixes
1. ...
```

## Applying the principles while writing

- Put the identifiable concept first in each heading, paragraph, and list item.
- Link text describes its target, never "click here" or "this page".
- Prefer version-agnostic instructions, such as `tool-<version>.tar.gz` instead of a
  hard-coded release.
- When you must publish something partial, say so at the top and name what is missing.
- Before you duplicate content, check whether a link would do (Unique). Repeat only
  what the reader needs right there (ARID).
- Put tutorials and examples before reference material. Reference sections may then be
  ordered alphabetically or by topic.
