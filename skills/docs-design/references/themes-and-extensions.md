# Themes and extensions

## What makes a good docs theme
The Write the Docs community recommends Sphinx themes that meet four requirements. The
same criteria work for any generator:
1. **Mobile-ready**
2. **Nice fonts and typography**
3. **Installable as a package** (for example a Python module), so versions are pinned and
   upgrades are easy
4. **Maintained and documented**

## Sphinx themes recommended by Write the Docs

| Theme | Character | Good for |
|---|---|---|
| [Furo](https://github.com/pradyunsg/furo) | WTD's first recommendation for new projects. Minimal but customizable, mobile-friendly, carefully designed sidebar and inter-page navigation, built-in dark mode | Most new projects |
| [Read the Docs theme](https://github.com/readthedocs/sphinx_rtd_theme) | The official Read the Docs theme. Clear typography, blue color scheme, full page menu on the left | Projects that want the familiar Read the Docs look |
| [Alabaster](https://github.com/sphinx-doc/alabaster) | Sphinx's default. Very minimal markup that puts the words front and center | Text-heavy, small sites |
| [PyData Sphinx theme](https://github.com/pydata/pydata-sphinx-theme) | Clean three-column Bootstrap layout, widely used by scientific and data projects | Large or complex doc sets |
| [Shibuya](https://github.com/lepture/shibuya) | Modern and responsive, with strong light and dark mode and good Jupyter integration | Projects with notebooks |
| [Clarity](https://readcraft.io/sphinx-clarity-theme) | Professional look, light and dark mode, responsive | Product docs |

Themes for other generators (linked; see each project's docs):
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) (MkDocs),
[Docusaurus](https://docusaurus.io/) (built-in classic theme),
[Just the Docs](https://just-the-docs.com/) (Jekyll),
[Docsy](https://www.docsy.dev/) (Hugo).

## Configure before you customize
Most themes expose options for these. Use them before writing templates or CSS:
- **Logo and favicon.** Provide both light and dark logo variants if the theme supports them.
- **Brand colors.** Set the theme's color variables, then check contrast.
- **Dark mode.** Keep it on, and test images and diagrams in both modes.
- **Source and edit links,** such as "Edit this page" and "View source". They invite
  contributions (the Participatory principle).
- **Footer and header icons,** such as a link to the repository.
- **Announcement banner,** for deprecations or new major versions.

Sphinx with Furo example (`conf.py`):
```python
html_theme = "furo"
html_logo = "_static/logo.svg"
html_theme_options = {
    "source_repository": "https://github.com/OWNER/REPO/",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {"color-brand-primary": "#2b6cb0"},
    "dark_css_variables": {"color-brand-primary": "#90cdf4"},
}
```

## High-value extensions (Sphinx; most generators have equivalents)
Add only what readers will notice. Each extension is a dependency to pin and maintain.

| Need | Extension (linked) |
|---|---|
| Copy button on code blocks | [sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/) |
| Tabs, cards, grids, badges, dropdowns | [sphinx-design](https://sphinx-design.readthedocs.io/) |
| Social preview cards (Open Graph) when links are shared | [sphinxext-opengraph](https://sphinxext-opengraph.readthedocs.io/) |
| Mermaid diagrams from text | [sphinxcontrib-mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) |
| Markdown with directives (admonitions, figures) | [MyST Parser](https://myst-parser.readthedocs.io/) |

## Badges
Badges, for example from [Shields.io](https://shields.io/), give a quick status line at the
top of a README or landing page.
- Keep to meaningful ones: build status, latest version, license, docs link, and the
  repository on the docs site.
- Give each badge alt text that states its meaning ("Build status", "License: MIT").
  Don't use the badge's visible text as its alt text.
- Link each badge to its source, such as the CI run, the package page, or the license file.

## Common theming pitfalls
New Sphinx users find theming hard, because customizing needs an understanding of the
templating system. Start from a recommended theme and its documented options. Override
templates only as a last resort, and record every override so upgrades don't break it.

---

*Adapted from "[Sphinx themes](https://www.writethedocs.org/guide/tools/sphinx-themes/)" (source: [`docs/guide/tools/sphinx-themes.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/tools/sphinx-themes.rst)) and the theming note in "[Community perspectives on Sphinx](https://www.writethedocs.org/guide/tools/sphinx-community/)" (source: [`docs/guide/tools/sphinx-community.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/tools/sphinx-community.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into a table. The configuration, extension, and badge guidance is original work by Yuming Fu, 2026.*
