# Attribution

NiceDocs adapts material from the **Write the Docs Documentation Guide**.

- **Source:** <https://www.writethedocs.org/guide/>
- **Source repository:** [writethedocs/www](https://github.com/writethedocs/www), pinned at
  commit [`c37669d0c87740b1455821cbee7fc10c8ee6cf7f`](https://github.com/writethedocs/www/tree/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide)
- **Copyright:** © Write the Docs contributors
- **Licence:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/),
  as stated in the source repository's
  [`LICENSE.md`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/LICENSE.md)
- **Adapter:** Yuming Fu, 2026

NiceDocs is an independent project. It is not affiliated with, sponsored by, or
endorsed by Write the Docs.

## Changes made

The source pages were **condensed, reorganised, and rewritten as instructions,
checklists, and templates for AI agents**. Specifically:
- Pages were grouped into six skills, and related pages were merged into single references.
- Prose was shortened. Many link lists were trimmed to a selection, and talk lists and
  most book links were dropped.
- Checklists, decision tables, output templates, example rewrites, and agent guardrails
  were added. These additions are original work by Yuming Fu, released under the same
  CC BY-NC-SA 4.0 licence.
- Every adapted file ends with a footer that names its specific source page(s) and
  describes the changes.

## Source page → adapted file map

| WTD source (`docs/guide/…`) | Adapted in |
|---|---|
| `writing/docs-principles.rst` | `skills/docs-principles/references/principles.md`, `skills/docs-principles/SKILL.md` |
| `writing/beginners-guide-to-docs.rst` | `skills/project-docs/references/what-to-include.md`, `skills/project-docs/assets/README.template.md` |
| `Starting-a-new-doc.rst`, `starting.rst` | `skills/project-docs/references/starting-a-new-doc.md`, `skills/docs-advocacy/references/building-mindshare.md` |
| `writing/style-guides.md` | `skills/docs-review/references/style-guides.md`, `skills/docs-review/references/ux-writing.md`, `skills/docs-review/references/inclusive-language.md`, `skills/project-docs/references/content-types.md`, `skills/docs-tooling/references/api-docs.md` |
| `writing/accessibility.md` | `skills/docs-review/references/accessibility.md` |
| `writing/reducing-bias.md` | `skills/docs-review/references/inclusive-language.md` |
| `ux-writing.rst` | `skills/docs-review/references/ux-writing.md` |
| `writing/markdown.md` | `skills/docs-markup/references/markdown.md` |
| `writing/reStructuredText.rst` | `skills/docs-markup/references/restructuredtext.md` |
| `writing/asciidoc.rst` | `skills/docs-markup/references/asciidoc.md` |
| `writing/xml.rst` | `skills/docs-markup/references/xml.md` |
| `docs-as-code.rst`, `doc-ops.rst` | `skills/docs-tooling/references/docs-as-code.md` |
| `choosing-tools.rst` | `skills/docs-tooling/references/choosing-tools.md` |
| `tools/index.rst`, `tools/sphinx.rst` | `skills/docs-tooling/references/sphinx.md` |
| `tools/testing.rst` | `skills/docs-tooling/references/testing.md` |
| `seo.rst` | `skills/docs-tooling/references/seo.md` |
| `api/api-documentation-tools.rst` | `skills/docs-tooling/references/api-docs.md` |
| `writing/mindshare.rst` | `skills/docs-advocacy/references/building-mindshare.md` |
| `writing/support-team.rst` | `skills/docs-advocacy/references/support-teams.md` |
| `imposter.rst` | `skills/docs-advocacy/references/imposter-syndrome.md` |

The `SKILL.md` files summarise their references and are adaptations under the same terms.

## Third-party material

External resources linked from the skills (style guides, books, tools, articles) are
only **linked**, never copied. They remain under their owners' terms. Book titles
appear as bibliographic references only.

## Updating from upstream

When re-syncing with a newer Write the Docs commit, update the pinned SHA in this file,
in every reference footer, and in `scripts/validate.py` (`WTD_SHA`). Record the update
in `CHANGELOG.md`.
