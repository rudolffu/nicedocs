# NiceDocs

**Documentation-writing skills for AI coding agents, built on the
[Write the Docs](https://www.writethedocs.org/) Documentation Guide.**

NiceDocs gives Claude Code, Codex, OpenCode, Gemini CLI, Cursor, GitHub Copilot, and
any [Agent Skills](https://agentskills.io/)-compatible agent a structured foundation for
writing good software documentation. It covers documentation principles, READMEs,
style and accessibility review, markup languages, docs-as-code tooling, and making the
case for docs.

## Skills

| Skill | Use it to… |
|---|---|
| [`docs-principles`](skills/docs-principles/SKILL.md) | Audit or structure docs against the WTD principles (ARID, skimmable, current, discoverable, complete…) |
| [`project-docs`](skills/project-docs/SKILL.md) | Write a README and core project docs, release notes, and FAQs, with templates |
| [`docs-review`](skills/docs-review/SKILL.md) | Review drafts for style-guide consistency, accessibility, inclusive language, and microcopy |
| [`docs-markup`](skills/docs-markup/SKILL.md) | Write, fix, and convert Markdown, reStructuredText, AsciiDoc, and XML |
| [`docs-tooling`](skills/docs-tooling/SKILL.md) | Set up docs-as-code, pick a generator, add docs CI (build, links, Vale), SEO, API docs |
| [`docs-advocacy`](skills/docs-advocacy/SKILL.md) | Justify docs work, roll out a docs culture, work with support, handle imposter syndrome |

Each skill keeps a short `SKILL.md` and loads its detailed `references/` only when
needed (progressive disclosure), so it costs little context until used.

## Install

### Claude Code
```text
/plugin marketplace add rudolffu/nicedocs
/plugin install nicedocs@nicedocs
```
Skills appear as `nicedocs:docs-review`, `nicedocs:project-docs`, and so on.

### Codex
```bash
codex plugin marketplace add rudolffu/nicedocs
```
Then install **NiceDocs** from the Plugins directory. To install only the skills
instead, clone the repo and run `scripts/install.sh codex`.

### Gemini CLI
```bash
gemini extensions install https://github.com/rudolffu/nicedocs
```

### OpenCode, Cursor, GitHub Copilot, or any Agent Skills tool
Clone the repo, then copy or symlink the skills into the tool's skills folder:

```bash
git clone https://github.com/rudolffu/nicedocs.git
cd nicedocs
```

```bash
scripts/install.sh opencode          # ~/.config/opencode/skills/
```

| Target | User-level folder | With `--project` |
|---|---|---|
| `opencode` | `~/.config/opencode/skills/` | `.opencode/skills/` |
| `agents` / `codex` | `~/.agents/skills/` | `.agents/skills/` |
| `claude` | `~/.claude/skills/` | `.claude/skills/` |
| `cursor` | `~/.cursor/skills/` | `.cursor/skills/` |
| `copilot` | `~/.copilot/skills/` | `.github/skills/` |
| `gemini` | `~/.gemini/skills/` | `.gemini/skills/` |

Options:
- `--link` symlinks instead of copying, so `git pull` updates the skills.
- `--project [DIR]` installs into a project (default: the current directory).
- `--uninstall` removes NiceDocs skills from the target.
- `--dry-run` shows what would happen.

## Example prompts

- "Write a README for this repo."
- "Audit `docs/` against the Write the Docs principles and list the top fixes."
- "Review this PR's docs changes for style, accessibility, and inclusive language."
- "Convert `guide.md` to reStructuredText for our Sphinx site."
- "Add link checking and Vale to our docs CI."
- "Help me write a one-page case for investing in internal docs."

## Repository layout

```
skills/                    # the skills (single source for every platform)
.claude-plugin/            # Claude Code plugin + marketplace manifests
.codex-plugin/             # Codex plugin manifest
.agents/plugins/           # Codex marketplace
gemini-extension.json      # Gemini CLI extension manifest (+ GEMINI.md)
scripts/install.sh         # installer for skills-folder platforms
scripts/validate.py        # spec, manifest, attribution, and link checks (run in CI)
docs/sources.md            # how each Write the Docs resource is used
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate.py` before you
open a pull request.

## License and attribution

- **Content** (`skills/`, `docs/`, prose files) is licensed
  [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). It adapts the
  Write the Docs Documentation Guide, © Write the Docs contributors, which is under the
  same licence.
- **Code and configuration** (`scripts/`, CI, and plugin manifests) are licensed **MIT**.

See [LICENSE.md](LICENSE.md), [REUSE.toml](REUSE.toml), and [ATTRIBUTION.md](ATTRIBUTION.md).
NiceDocs is an independent project and is not affiliated with or endorsed by Write the Docs.

Author: **Yuming Fu** ([@rudolffu](https://github.com/rudolffu)).
