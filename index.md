<!--
  Landing page of the NiceDocs documentation site (Sphinx + MyST, built by Read the Docs).
  On GitHub, start with README.md instead.
-->

# NiceDocs documentation

NiceDocs teaches AI coding agents to write documentation the way experienced
documentarians do. It is a plugin of Agent Skills built on the
[Write the Docs](https://www.writethedocs.org/) Documentation Guide, for Claude Code,
Codex, OpenCode, Gemini CLI, Cursor, GitHub Copilot, and other Agent Skills tools.

- **New here?** Read the [overview and install guide](README.md).
- **Want to see what the agent follows?** Browse the skills below. Each one links to the
  detailed references it loads on demand.
- **Want to help?** See [Contributing](CONTRIBUTING.md).

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
