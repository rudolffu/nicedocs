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
REPO_URL = "https://github.com/rudolffu/nicedocs"
# GitHub "mark-github" octicon (16x16), used for the footer link.
GITHUB_ICON = (
    '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">'
    '<path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07'
    ".55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82"
    "-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52"
    ".28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08"
    "-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82"
    " 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29"
    ".25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0"
    '-4.42-3.58-8-8-8z"></path></svg>'
)

html_theme_options = {
    # Adds "View source" and "Edit this page" buttons that open the file on GitHub.
    "source_repository": f"{REPO_URL}/",
    "source_branch": "main",
    "source_directory": "",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": REPO_URL,
            "html": GITHUB_ICON,
            "class": "",
        },
    ],
}


def setup(app):
    # Pygments has no AsciiDoc lexer. Keep ```asciidoc fences (GitHub highlights them)
    # and render them as plain text here instead of warning.
    from pygments.lexers.special import TextLexer

    app.add_lexer("asciidoc", TextLexer)
