---
name: docs-review
description: Review and edit documentation drafts for style-guide consistency, accessibility (a11y), inclusive and bias-free language, plain language for non-native readers, and UX microcopy such as error messages, buttons, and labels, using Write the Docs guidance. Use when asked to proofread, copy-edit, review, or polish docs, a README, a docs pull request, CLI help text, or UI strings, or to pick or create a style guide.
license: CC-BY-NC-SA-4.0
metadata:
  author: Yuming Fu
  source: Write the Docs Documentation Guide (writethedocs/www@c37669d)
---

# Documentation review

A consistent style lowers readers' cognitive load and makes content feel authoritative.
If the content design is simple, concise, and clear, you are already doing a lot for
accessibility and localization. Review in the passes below, from the highest impact to
the lowest.

## 0. Establish the standard
- Look for the project's own style guide first: `STYLE.md`, `CONTRIBUTING.md`, a Vale
  config (`.vale.ini`), or a docs README. That guide always wins.
- If there is none, ask which published guide to follow, or default to one well-known
  developer guide and say which one you chose. See
  [references/style-guides.md](references/style-guides.md) for options and for how to
  start a lightweight project style guide.

## 1. Correctness and principles (highest impact)
- Flag anything technically wrong or out of date. Wrong docs are worse than none.
- Run the `docs-principles` checks: Skimmable, Exemplary, Complete, Current.

## 2. Accessibility
Use the checklist in [references/accessibility.md](references/accessibility.md). The key
points:
- Use a real heading hierarchy (no skipped levels) and lists for lists.
- Every image has alt text that conveys its purpose. Diagrams also get a text equivalent.
- Link text describes the destination. Never use "click here".
- Meaning is never carried by color, position, or emphasis alone.
- Tables have header rows. Code goes in code blocks, not images of code.

## 3. Inclusive language and bias
Use [references/inclusive-language.md](references/inclusive-language.md):
- Replace exclusionary or loaded terms and gendered defaults.
- Use diverse, realistic example names, not the same "John" every time.
- Replace idioms, especially violent or culture-specific ones, with literal phrasing.
  Keep established technical terms such as `kill`, canary deployment, and
  monkey-patching.

## 4. Style and consistency
- Use one term per concept, and keep a terminology list if the project has none.
- Keep capitalization of headings, product names, and UI labels consistent.
- Format code, commands, file paths, and placeholders consistently.
- Keep voice and tone steady. Prefer second person and active voice for instructions.

## 5. UX writing and microcopy (when reviewing UI or CLI text)
Use [references/ux-writing.md](references/ux-writing.md), especially the error-message
checklist.

## Reporting
- Give findings as a table or list ordered by pass. Each finding has the location
  (file:line or heading), the issue, a suggested rewrite, and the reason (cite the rule
  or guide).
- Separate **must fix** (wrong, inaccessible, exclusionary) from **suggestions** (style).
- When asked to edit directly, make minimal changes that preserve the author's voice
  and meaning, then summarize what you changed by category.
- If a prose linter is configured (Vale), run it and include its results. See the
  `docs-tooling` skill.
