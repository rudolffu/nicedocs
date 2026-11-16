---
name: project-docs
description: Plan and write the core documentation a software project needs, including the README, project description, quick-start example, installation, support, contributing, license, FAQ, and release notes, following Write the Docs guidance. Use when creating or rewriting a README, documenting a new or open-source project, starting a brand-new doc for a product, writing release notes or an FAQ, or when a user asks "what docs does my project need?".
license: CC-BY-NC-SA-4.0
metadata:
  author: Yuming Fu
  source: Write the Docs Documentation Guide (writethedocs/www@c37669d)
---

# Project documentation

Good docs answer three questions that stop people using code: *why does this exist?*,
*how do I install it?*, and *how do I use it?* This skill gets a project from nothing to
those answers. It then grows the docs to cover contributors, support, and releases.

## Workflow

### 1. Understand the product and audience first
Read the code, existing docs, package metadata, and issue tracker before writing. If you
can't tell, ask the user (or the experts they name):
- What does the product do, and what does it let users achieve?
- Who is it for: **users** (want to use it, don't care how it works), **contributors**
  (want to change it), or a specific role (sysadmin, data analyst, API consumer)?
- How is it used: installed and run, imported as a library, called as an API, or
  driven through a GUI?

The answers decide the *form* of the docs. A GUI app needs step-by-step task guides.
An SDK or API needs reference material organized so readers can look things up. A tool
installed by sysadmins needs more installation scenarios. See
[references/starting-a-new-doc.md](references/starting-a-new-doc.md).

### 2. Write the README (the first thing users see)
Start from [assets/README.template.md.tmpl](assets/README.template.md.tmpl). Every README needs:

1. **What and why.** Name the problem the project solves, in the first lines.
2. **A small code example.** Show the most common use case, and make it runnable.
3. **Installation.** One or two lines for the basic case. Link to a full guide for
   platforms, options, and caveats.
4. **Links to the code and issue tracker.**
5. **Support.** Say where to ask for help (forum, chat, mailing list, discussions).
6. **Contributing.** Say how to contribute, or link to `CONTRIBUTING.md`.
7. **License.** Name one standard license.

Details and rationale: [references/what-to-include.md](references/what-to-include.md).

### 3. Grow beyond the README when needed
- Installation, tutorials, how-to guides, and reference get their own pages once the
  README is longer than a screen or two. Use
  [assets/doc-page.template.md.tmpl](assets/doc-page.template.md.tmpl) for task pages.
- **Avoid using an FAQ as the main docs.** It is fine as a stop-gap, but FAQs go stale,
  collect unrelated content, become hard to search, and rarely reflect questions users
  actually asked. Move FAQ answers into proper pages as soon as you can.
- **Release notes:** use [assets/release-notes.template.md.tmpl](assets/release-notes.template.md.tmpl)
  and the checklist in [references/content-types.md](references/content-types.md).

### 4. Check before you hand it over
- Apply the `docs-principles` rubric, at least Skimmable, Exemplary, Current, and
  Discoverable.
- Run every command and code sample you wrote, or say clearly which ones you could
  not run.
- Check that each link resolves and that the license named matches the `LICENSE` file.
- Leave claims you could not verify as clearly marked `TODO:` items for the user. Do
  not invent features, URLs, maintainers, or support channels.

## Conventions
- Name the file `README.md` (Markdown) or `README.rst` (reStructuredText) so code hosts
  render it.
- Put headings in this order: what it is, example, features, install, usage, contribute,
  support, license.
- Keep the README for orientation and put depth in linked pages (Unique principle).
