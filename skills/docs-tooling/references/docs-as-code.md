# Docs as code and DocOps

## Docs as code
*Docs as Code* means writing documentation with the same tools as code:
- issue trackers
- version control (Git)
- plain-text markup (Markdown, reStructuredText, AsciiDoc)
- code reviews
- automated tests.

Writers then follow the development team's workflows and are part of the product team.
Both writers and developers feel ownership of the docs.

Benefits:
- Writers integrate better with development teams.
- Developers often write the first draft.
- Merges can be blocked when new features lack docs, so features get documented while
  they are fresh.

Implementation checklist for agents:
- [ ] Docs live in the code repo (or a sibling repo with the same review flow).
- [ ] The pull request template asks "Docs updated?". Optionally, CI fails if code
      changes under `src/` have no change under `docs/`.
- [ ] Docs build and checks run in CI (see [testing.md](testing.md)).
- [ ] Preview builds for pull requests, where the host supports them.
- [ ] `CODEOWNERS` routes docs reviews to writers.

Books recommended by WTD (titles only): *Docs Like Code* (Anne Gentle); *Modern
Technical Writing* (Andrew Etter); *Crafting Docs for Success* (Diana Lakatos). One
open-source implementation of the approach: [docToolchain](https://doctoolchain.org/docToolchain/).

## DocOps
DocOps applies the DevOps idea to documentation: a set of practices that automate and
integrate how docs are developed across engineering, product, support, and technical
writing. It stresses collaboration and continuous improvement. DocOps often goes with
docs as code but doesn't require it. A DITA, CMS, or wiki setup can be run in a DocOps
way too.

Typical DocOps responsibilities, which are useful when scoping work:
- selecting and supporting the tools: markup, static site generator, hosting
- defining processes, including where docs fit in agile or other methods
- setting documentation priorities and deliverables
- training authors so more people can contribute
- managing content
- building and maintaining the site theme
- modelling the versioning strategy for the docs
- creating and maintaining build scripts
- keeping the barrier to contributing low.

---

*Adapted from "[Docs as code](https://www.writethedocs.org/guide/docs-as-code/)" (source: [`docs/guide/docs-as-code.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/docs-as-code.rst)) and "[DocOps](https://www.writethedocs.org/guide/doc-ops/)" (source: [`docs/guide/doc-ops.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/doc-ops.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed, merged, and an implementation checklist added for agents by Yuming Fu, 2026.*
