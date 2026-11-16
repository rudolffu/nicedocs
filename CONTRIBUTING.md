# Contributing to NiceDocs

Thanks for helping improve NiceDocs. You don't need to write code to contribute.
Corrections, clearer wording, and reports of where a skill gave poor advice are all
valuable.

## Ways to contribute

- **Report a problem.** [Open an issue](https://github.com/rudolffu/nicedocs/issues).
  Include the tool you use (for example Claude Code or OpenCode), the prompt, and what
  the agent did that was wrong or unhelpful.
- **Improve a skill.** Fix an error, tighten an instruction, or add a checklist item.
- **Propose a skill.** Open an issue first, describing the task it covers and its sources.
- **Add a platform.** Add an installer target or a manifest for another agent tool.

## Set up

```bash
git clone https://github.com/rudolffu/nicedocs.git && cd nicedocs
```

```bash
python3 scripts/validate.py
```

To try your changes in a tool, install with symlinks so each edit shows up at the next
session:

```bash
scripts/install.sh opencode --project /path/to/test-project --link
```

## Ground rules

- **Licensing.** Content under `skills/` and `docs/` is CC BY-NC-SA 4.0. Code, CI, and
  manifests are MIT (see [LICENSE.md](LICENSE.md)). By contributing, you agree to license
  your contribution under the license that applies to the files you change.
- **Attribution.** If you adapt more material from Write the Docs, end the file with the
  standard footer (copy one from any `references/*.md`). The footer names the source page
  and its path at the pinned commit, and says what you changed. Add the page to the map
  in [ATTRIBUTION.md](ATTRIBUTION.md).
- **No copying third-party content.** Link to external style guides, books, and articles.
  Don't paste them in. Keep any quotation under 15 words and attribute it.

## Writing style

NiceDocs follows its own advice. Run the `docs-review` skill on your changes, and keep to
these project conventions:

- US English spelling (license, organization, color).
- Sentence-case headings ("Set up the docs site", not "Set Up The Docs Site").
- Second person and imperative mood for instructions ("Run the validator").
- Code font for commands, paths, file names, and skill names.
- Link text that names its destination.

## Write or change a skill

Skills follow the [Agent Skills specification](https://agentskills.io/specification):

```
skills/<skill-name>/
├── SKILL.md        # frontmatter (name, description, license, metadata) + workflow
├── references/     # one focused topic per file, loaded on demand
└── assets/         # templates (optional)
```

- `name` uses lowercase letters, digits, and single hyphens, has at most 64 characters,
  and matches the folder name.
- `description` is at most 1024 characters. It says what the skill does **and when to
  use it**, with the words users would type.
- Keep `SKILL.md` under 500 lines. Move detail into `references/`, one level deep.
- Write for an agent: steps, checklists, output formats, and guardrails, such as
  "don't invent URLs".

When you **add** a skill, also update:

1. The skills table in [README.md](README.md).
2. The routing table in [GEMINI.md](GEMINI.md).
3. The source map in [ATTRIBUTION.md](ATTRIBUTION.md), if the skill adapts Write the Docs material.
4. [CHANGELOG.md](CHANGELOG.md), under an `Unreleased` heading.

## Open a pull request

1. Create a branch from `main`.
2. Run `python3 scripts/validate.py` and fix anything it reports. CI runs the same check,
   plus an installer smoke test and a [REUSE](https://reuse.software/) licensing check.
3. Fill in the pull request template checklist.

## Release a new version (maintainers)

1. Set the same version in every manifest: `.claude-plugin/plugin.json`,
   `.claude-plugin/marketplace.json` (both `metadata.version` and the plugin entry),
   `.codex-plugin/plugin.json`, and `gemini-extension.json`. The validator fails if they
   disagree.
2. Move the `Unreleased` changelog entries under the new version and date.
3. Tag the release, for example `git tag v0.2.0 && git push --tags`.

## Sync with upstream Write the Docs

To pick up changes from a newer Write the Docs commit:

1. Compare `docs/guide/` between the pinned commit and the new one.
2. Update the affected `references/*.md` files.
3. Replace the pinned SHA in [ATTRIBUTION.md](ATTRIBUTION.md), in every reference footer,
   and in `WTD_SHA` in `scripts/validate.py`.
4. Record the sync in the changelog.
