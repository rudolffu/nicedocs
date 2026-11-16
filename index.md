<!--
  Landing page of the NiceDocs documentation site (Sphinx + MyST, built by Read the Docs).
  On GitHub, start with README.md instead.
-->

# NiceDocs documentation

[![Source code on GitHub: rudolffu/nicedocs](https://img.shields.io/badge/GitHub-rudolffu%2Fnicedocs-181717?logo=github)](https://github.com/rudolffu/nicedocs)
[![Validate workflow status](https://github.com/rudolffu/nicedocs/actions/workflows/validate.yml/badge.svg)](https://github.com/rudolffu/nicedocs/actions/workflows/validate.yml)
[![Content license: CC BY-NC-SA 4.0](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey)](LICENSE.md)
[![Code license: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE.md)

NiceDocs teaches AI coding agents to write documentation the way experienced
documentarians do. It is a plugin of Agent Skills built on the
[Write the Docs](https://www.writethedocs.org/) Documentation Guide, for Claude Code,
Codex, OpenCode, Gemini CLI, Cursor, GitHub Copilot, and other Agent Skills tools.

- **New here?** Read the [overview and install guide](README.md).
- **Want to see what the agent follows?** Browse the skills below. Each one links to the
  detailed references it loads on demand.
- **Want to help?** See [Contributing](CONTRIBUTING.md), or
  [view the source and open issues on GitHub](https://github.com/rudolffu/nicedocs).

```{toctree}
:caption: Get started
:maxdepth: 2

Overview and install <README>
```

```{toctree}
:caption: Skills
:maxdepth: 1

skills/docs-principles/SKILL
skills/project-docs/SKILL
skills/docs-review/SKILL
skills/docs-markup/SKILL
skills/docs-tooling/SKILL
skills/docs-advocacy/SKILL
skills/docs-design/SKILL
```

```{toctree}
:caption: Project
:maxdepth: 1

CONTRIBUTING
CHANGELOG
docs/sources
ATTRIBUTION
LICENSE
GEMINI
```

```{toctree}
:hidden:
:glob:

skills/*/references/*
```
