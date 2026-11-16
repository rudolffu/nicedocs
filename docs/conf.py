# SPDX-FileCopyrightText: 2026 Yuming Fu
# SPDX-License-Identifier: MIT
"""Sphinx configuration for the NiceDocs documentation site.

The configuration lives in docs/, but the source directory is the repository root,
so the existing Markdown files (README.md, skills/**, ...) build in place and their
relative links keep working. Build locally from the repository root:

    python -m sphinx -W --keep-going -b html -c docs . _build/html
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# -- Project information ----------------------------------------------------
project = "NiceDocs"
author = "Yuming Fu"
copyright = "2026 Yuming Fu; adapted content © Write the Docs contributors"
# Single source of truth for the version: the Claude Code plugin manifest.
release = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())["version"]
version = release

# -- General configuration --------------------------------------------------
extensions = ["myst_parser"]
source_suffix = {".md": "markdown"}
root_doc = "index"

exclude_patterns = [
    "_build",
    ".venv",
    "venv",
    ".git",
    ".github",
    "LICENSES",
]
# Fill-in templates in skills/*/assets/ end in .md.tmpl, so Sphinx does not build them
# as pages. Links to them become downloadable files.

# GitHub-style heading anchors, so links such as README.md#install work on the site.
myst_heading_anchors = 3
myst_enable_extensions = ["colon_fence"]

# -- HTML output -------------------------------------------------------------
html_theme = "furo"
html_title = f"NiceDocs {release}"
html_theme_options = {
    "source_repository": "https://github.com/rudolffu/nicedocs/",
    "source_branch": "main",
    "source_directory": "",
}


def setup(app):
    # Pygments has no AsciiDoc lexer. Keep ```asciidoc fences (GitHub highlights them)
    # and render them as plain text here instead of warning.
    from pygments.lexers.special import TextLexer

    app.add_lexer("asciidoc", TextLexer)
