---
name: docs-tooling
description: Set up and improve documentation tooling and workflow, including docs-as-code, DocOps, choosing a static site generator (Sphinx, MkDocs, Docusaurus, Hugo, Jekyll, Antora), CI checks for docs (build errors, link checking, Vale prose linting), SEO for docs sites, and API documentation (OpenAPI, API Blueprint, documentation-driven design). Use when creating a docs site or pipeline, adding docs tests to CI, picking docs tools, or documenting an API.
license: CC-BY-NC-SA-4.0
metadata:
  author: Yuming Fu
  source: Write the Docs Documentation Guide (writethedocs/www@c37669d)
---

# Documentation tooling and workflow

## Default stance: docs as code
Write docs with the same tools as code: issue trackers, version control, plain-text
markup, code review, and automated tests. Writers and developers then share ownership.
Developers often write the first draft. Teams can block merging a feature that lacks
docs. Background: [references/docs-as-code.md](references/docs-as-code.md).

## Workflows

### A. Choose tools for a new docs project
1. Go through the questions in [references/choosing-tools.md](references/choosing-tools.md):
   budget (money and time), outputs, skills available, WYSIWYG versus text, review
   process, existing company tools, version control, reuse needs, contributor count,
   CI/CD, translation.
2. Prefer what already exists in the organization or ecosystem. For example, Python
   projects usually choose Sphinx and JS projects often choose Docusaurus.
3. Recommend one option with reasons and the main trade-off. Name who will maintain it
   long-term.

### B. Scaffold a docs site
- Sphinx: see [references/sphinx.md](references/sphinx.md) (`docs/` with `conf.py` and
  `index.rst`, toctrees, MyST for Markdown).
- Others (MkDocs, Docusaurus, Hugo, Jekyll, Antora): use the tool's official quick start.
  Keep the docs in the same repo as the code (Nearby principle).
- Add a page hierarchy that answers "where do I put it?": tutorials, how-to guides,
  reference, and explanation, or the project's existing taxonomy.

### C. Add docs tests to CI
Follow [references/testing.md](references/testing.md). Add layers in this order:
1. **Build passes**, with warnings treated as errors once the docs are clean (Sphinx
   `-W` or nitpicky mode, Jekyll strict mode).
2. **Link checking** (Sphinx `linkcheck`, HTMLProofer, or a site link checker).
3. **Prose and style linting** with Vale and a style package.
Run the checks on every pull request (GitHub Actions or GitLab CI).

### D. Improve discoverability (SEO)
Apply [references/seo.md](references/seo.md): imperative, goal-oriented headings,
skimmable sections, clear navigation, page metadata, and accessibility.

### E. Document an API
Use [references/api-docs.md](references/api-docs.md): describe the API in a
machine-readable format (OpenAPI first), generate reference docs, hand-write the
concepts and tutorials, and test the description against the live API.

## Guardrails
- Don't introduce a new toolchain without the user's agreement. Propose it and explain
  the maintenance cost.
- Pin tool versions in config (`requirements.txt`, `package.json`) so CI builds are
  reproducible.
- When you add CI checks to a repo with many existing failures, start them as warnings
  or scope them to changed files, then tighten.
