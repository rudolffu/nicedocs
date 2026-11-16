# License

This repository has **two licenses**, depending on the kind of file. The split exists
because the documentation content is adapted from the
[Write the Docs](https://www.writethedocs.org/) Documentation Guide, which is licensed
CC BY-NC-SA 4.0. Its ShareAlike term requires adapted material to keep that license.

| What | Paths | License |
|---|---|---|
| Documentation content (skills, references, templates, prose docs) | `skills/**`, `docs/**/*.md`, `index.md`, `GEMINI.md`, `README.md`, `ATTRIBUTION.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE.md` | [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — full text in [`LICENSES/CC-BY-NC-SA-4.0.txt`](LICENSES/CC-BY-NC-SA-4.0.txt) |
| Code and configuration (scripts, CI, plugin manifests, docs-site config) | `scripts/**`, `docs/conf.py`, `docs/requirements.txt`, `.readthedocs.yaml`, `.github/**`, `.claude-plugin/**`, `.codex-plugin/**`, `.agents/**`, `gemini-extension.json`, `REUSE.toml`, `.gitignore` | [MIT](https://opensource.org/license/mit) — full text in [`LICENSES/MIT.txt`](LICENSES/MIT.txt) |

The authoritative, machine-readable mapping is [`REUSE.toml`](REUSE.toml), which follows
the [REUSE specification](https://reuse.software/spec/).

## Copyright

- Original contributions: © 2026 Yuming Fu.
- Material adapted from the Write the Docs Documentation Guide: © Write the Docs
  contributors. See [`ATTRIBUTION.md`](ATTRIBUTION.md) for sources and changes.

## What this means in practice

- You may share and adapt the **content** for **non-commercial** purposes. You must give
  attribution, note your changes, and license your adaptations under CC BY-NC-SA 4.0
  (or a compatible license).
- You may use the **code** (install and validation scripts, manifests) for any purpose
  under the MIT terms.
- Using the plugin in your own work, for example letting your AI agent follow these
  skills while it writes docs for you, does not by itself make your output an adaptation
  of this material. This is not legal advice. Read the license texts.
- Third-party resources linked from the skills (external style guides, books, tools) are
  **not** included in this repository and are governed by their own terms.
