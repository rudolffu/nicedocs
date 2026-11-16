---
name: docs-design
description: Improve the visual design and presentation of documentation, including choosing and configuring a docs theme (Furo, Read the Docs, PyData, Material for MkDocs), layout and typography, callouts/admonitions, screenshots and screenshot style guides, diagrams (Mermaid, diagrams as code), animated GIFs and video, badges, and alt text, using Write the Docs guidance. Use when asked to make docs look better, beautify or polish a docs site or README, pick a theme, add or fix screenshots, diagrams, or callouts, or apply the "Beautiful" documentation principle.
license: CC-BY-NC-SA-4.0
metadata:
  author: Yuming Fu
  source: Write the Docs Documentation Guide and newsletter (writethedocs/www@c37669d)
---

# Documentation design

Visual style should be intentional. It is the **Beautiful** principle in `docs-principles`.
Good design helps readers scan, trust, and act on the content. It never replaces clear
writing, and it must stay accessible. Work through the steps below in order. Most
"ugly docs" problems are fixed in steps 2 and 3, before any theme work.

## 1. Establish the constraints
- **Where the docs render:** a GitHub or GitLab README (Markdown only, no custom CSS), a
  static site generator (Sphinx, MkDocs, Docusaurus…), or a help center. This sets what is
  possible.
- **Existing brand or design system:** colors, logo, fonts. Reuse them instead of
  inventing new ones.
- **Who maintains it:** every custom template or CSS rule is maintenance. Prefer theme
  options and well-maintained extensions to hand-written overrides.

## 2. Fix structure and layout first
See [references/layout-and-callouts.md](references/layout-and-callouts.md):
- Use a clear heading hierarchy, short paragraphs, and lists and tables where the content
  is truly list-like or tabular.
- Ration callouts (note, tip, important, warning). Overuse causes "admonition fatigue".
- Make code blocks copyable, language-tagged, and short.

## 3. Decide on each visual deliberately
For every image, ask: does it show something text can't, and can we keep it current?
- **Screenshots:** follow [references/screenshots.md](references/screenshots.md),
  including a screenshot style guide for teams.
- **Diagrams, animations, video:** follow
  [references/diagrams-and-media.md](references/diagrams-and-media.md). Prefer diagrams as
  code (Mermaid) so they stay versioned and editable. Prefer short videos with controls to
  autoplaying GIFs.
- **Alt text:** every informative image needs purpose-focused alt text of one or two
  sentences (same reference).

## 4. Choose or tune the theme
See [references/themes-and-extensions.md](references/themes-and-extensions.md):
- A theme should be mobile-ready, have good typography, be installable as a package, and
  be maintained and documented.
- Configure the theme's options before writing CSS: logo, colors, dark mode, source and
  edit links, footer icons.
- Add a few high-value extensions (copy buttons, tabs and cards, social preview cards,
  diagrams) instead of many.

## 5. Verify
- Build the site and view key pages at phone width and in both light and dark mode.
- Check color contrast (WCAG AA) for any custom colors, badges, and annotations.
- Check that every image has alt text and that no meaning depends on color alone (see
  `docs-review` accessibility).
- Re-read a page by skimming only headings, callouts, and images. Does the story still
  make sense?

## Guardrails
- Don't trade accessibility for looks: no low-contrast text, no text baked into images
  without an equivalent in the page, no autoplaying flashing media.
- Don't add a visual just to decorate. Every image adds maintenance and translation cost.
- Don't switch themes or add extensions without the user's agreement. Propose them with
  their cost.
- Use badges sparingly and keep them meaningful: build status, version, license, docs link.
