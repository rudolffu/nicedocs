# Contributing to NiceDocs

Thanks for helping improve NiceDocs. Issues and pull requests are welcome.

## Ground rules

- **Licensing.** Content under `skills/` and `docs/` is CC BY-NC-SA 4.0. Code, CI, and
  manifests are MIT (see [LICENSE.md](LICENSE.md)). By contributing, you agree to license
  your contribution under the licence that applies to the files you change.
- **Attribution.** If you adapt more material from Write the Docs, end the file with the
  standard footer (copy one from any `references/*.md`). Name the source page and its
  path at the pinned commit, and say what you changed. Add the page to the map in
  [ATTRIBUTION.md](ATTRIBUTION.md).
- **No copying third-party content.** Link to external style guides, books, and articles.
  Don't paste them in. Keep any quotation under 15 words and attribute it.

## Writing a skill

Skills follow the [Agent Skills specification](https://agentskills.io/specification):

```
skills/<skill-name>/
├── SKILL.md        # frontmatter (name, description, license, metadata) + workflow
├── references/     # one focused topic per file, loaded on demand
└── assets/         # templates (optional)
```

- `name` uses lowercase letters, digits, and single hyphens, has at most 64 characters,
  and matches the folder name.
- `description` is at most 1024 characters. Say what the skill does **and when to use
  it**, with the keywords users would type.
- Keep `SKILL.md` under 500 lines. Move detail into `references/`, one level deep.
- Write instructions for an agent: steps, checklists, output formats, guardrails.

## Before you open a pull request

```bash
python3 scripts/validate.py
```

The same check runs in CI. If you change the version, update it in **every** manifest:
`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`,
`.codex-plugin/plugin.json`, and `gemini-extension.json`. Also add an entry to
[CHANGELOG.md](CHANGELOG.md).
