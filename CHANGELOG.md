# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed
- README reworked after auditing it with NiceDocs' own skills. Added a quick start,
  "How it works", Codex CLI install (`codex plugin add`), update and uninstall commands for
  each platform, requirements, troubleshooting, and a support section.
- CONTRIBUTING expanded with ways to contribute, setup, writing conventions, the files to
  update when adding a skill, and the release and upstream-sync steps.
- Project-docs templates renamed to `*.md.tmpl`, so the docs site offers them as downloads.
- Spelling standardized to US English across all docs and skills.
- `docs/sources.md` skill map converted from a text diagram to an accessible table.
- CI actions updated to current major versions.

### Added
- Documentation site built with Sphinx, MyST, and Furo, configured for Read the Docs
  (`.readthedocs.yaml`, `docs/conf.py`, `index.md`), with a docs build job in CI.
- Pull request template with a docs checklist.
- Weekly external link-check workflow (lychee).

## [0.1.0] - 2026-11-16

### Added
- Six skills adapted from the Write the Docs Documentation Guide (writethedocs/www@c37669d):
  `docs-principles`, `project-docs`, `docs-review`, `docs-markup`, `docs-tooling`, `docs-advocacy`.
- Manifests for Claude Code (plugin + marketplace), Codex (plugin + marketplace), and Gemini CLI.
- `scripts/install.sh` for OpenCode, Cursor, Copilot, Claude, Gemini, and generic Agent Skills folders.
- `scripts/validate.py` and a GitHub Actions workflow.
- Dual licensing (content CC BY-NC-SA 4.0, code MIT), with a REUSE mapping and attribution.
