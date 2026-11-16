# Sphinx and other documentation generators

## Landscape
- **Sphinx:** a Python documentation generator, widely used beyond Python. It converts
  reStructuredText, and Markdown via MyST, to HTML, PDF, and more. Its strengths are code
  introspection, cross-referencing, and multiple output formats.
- **MkDocs:** Markdown-focused, with live preview.
- **Docusaurus:** React-based, with built-in versioning and i18n.
- **Jekyll:** Ruby-based and popular with GitHub Pages.
- **Hugo:** Go-based and very fast.
- **Antora:** AsciiDoc, multi-repo documentation sites (see the `docs-markup` skill).

## Sphinx essentials
Mental model: `reST/MyST source → Sphinx → HTML (and other outputs)`. Your main job is
writing the text files.

Install into a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install sphinx
```

`sphinx-quickstart docs` creates:
```
docs/
├── conf.py     # configuration (extensions, theme, project metadata)
├── index.rst   # landing page with the top-level toctree
└── Makefile    # `make html`, `make linkcheck`, etc. (make.bat on Windows)
```

### Table of contents
There is no single master ToC file. Each parent page declares its children with a
`toctree`, and Sphinx assembles the hierarchy:

```rst
.. toctree::
   :maxdepth: 2

   install
   usage/index
```

Add `:hidden:` to keep the entry in the navigation without listing it on the page.
**Every new page must appear in some toctree.** Sphinx warns about orphan pages.

### Writing and building
- Major topics go in well-named files under `docs/`. When a topic grows, split it into
  a directory with its own `index`.
- reST is whitespace-sensitive. If output looks wrong, check the indentation first.
- Build with `make html`. Output goes to `_build/html/index.html`.
- Use Markdown with `myst-parser` (add `"myst_parser"` to `extensions`). `.rst` and `.md`
  can be mixed.

### Key features
- **Intersphinx:** cross-reference other Sphinx projects without copying their content.
- **Domains:** directives and roles for Python, C, C++, JavaScript, and more.
- **Extensions:** `autodoc` (docs from docstrings), `napoleon` (Google/NumPy docstrings),
  `viewcode`, `todo`, and many community extensions and themes.

## Learn more (linked)
- [Sphinx getting started](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
- [Sphinx directives (toctree)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#table-of-contents)
- [MyST Parser](https://myst-parser.readthedocs.io/)

---

*Adapted from "[Tools for documentation writing](https://www.writethedocs.org/guide/tools/)" (source: [`docs/guide/tools/index.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/tools/index.rst)) and "[Introduction to Sphinx](https://www.writethedocs.org/guide/tools/sphinx/)" (source: [`docs/guide/tools/sphinx.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/tools/sphinx.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed and merged for agents by Yuming Fu, 2026.*
