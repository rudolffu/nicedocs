# NiceDocs

**Teach your AI coding agent to write documentation the way experienced documentarians do.**

NiceDocs is a plugin of [Agent Skills](https://agentskills.io/) built on the community
guidance in the [Write the Docs](https://www.writethedocs.org/) Documentation Guide. It works
with Claude Code, Codex, OpenCode, Gemini CLI, Cursor, GitHub Copilot, and any other tool
that reads Agent Skills. Once it is installed, your agent can audit docs against proven
principles, write READMEs and release notes, review drafts for style and accessibility,
handle Markdown, reStructuredText, and AsciiDoc, and set up docs tooling.

## Quick start

In Claude Code:

```text
/plugin marketplace add rudolffu/nicedocs
/plugin install nicedocs@nicedocs
```

Then ask in plain language:

```text
Audit the docs in this repo against the Write the Docs principles and list the top three fixes.
```

The agent picks the matching skill (`docs-principles`). It scores each principle with
evidence and proposes prioritized fixes. For other tools, see [Install](#install).

## Skills

| Skill | Use it to… |
|---|---|
| [`docs-principles`](skills/docs-principles/SKILL.md) | Audit or structure docs against the WTD principles (ARID, skimmable, current, discoverable, complete…) |
| [`project-docs`](skills/project-docs/SKILL.md) | Write a README and core project docs, release notes, and FAQs, with templates |
| [`docs-review`](skills/docs-review/SKILL.md) | Review drafts for style-guide consistency, accessibility, inclusive language, and microcopy |
| [`docs-markup`](skills/docs-markup/SKILL.md) | Write, fix, and convert Markdown, reStructuredText, AsciiDoc, and XML |
| [`docs-tooling`](skills/docs-tooling/SKILL.md) | Set up docs as code, choose a generator, add docs CI (build, links, Vale), SEO, and API docs |
| [`docs-advocacy`](skills/docs-advocacy/SKILL.md) | Make the case for docs work, build a docs culture, work with support, and handle imposter syndrome |
| [`docs-design`](skills/docs-design/SKILL.md) | Improve visual design: themes, layout, callouts, screenshots, diagrams, GIFs and video, badges, and alt text |

## How it works

- **The agent chooses the skill.** Each skill's description says when to use it, so a
  request such as "review this doc" loads `docs-review` without you naming it. In Claude
  Code you can also call a skill directly, for example `/nicedocs:docs-review`.
- **Context is loaded only when needed.** At startup, agents see only each skill's name
  and description. The full `SKILL.md` loads when the skill is used. The detailed
  `references/` files load only when a step needs them.
- **One source for every platform.** All tools read the same `skills/` folder. The
  platform manifests and the installer only point to it.

## Install

### Claude Code

```text
/plugin marketplace add rudolffu/nicedocs
/plugin install nicedocs@nicedocs
```

### Codex

```bash
codex plugin marketplace add rudolffu/nicedocs
```

```bash
codex plugin add nicedocs@nicedocs
```

### Gemini CLI

```bash
gemini extensions install https://github.com/rudolffu/nicedocs
```

In some Gemini CLI versions, Agent Skills are experimental and must be enabled in
settings. If skills don't load, the extension's `GEMINI.md` still points Gemini to each
skill file.

### OpenCode, Cursor, GitHub Copilot, or another Agent Skills tool

Clone the repository, then run the installer with your tool as the target:

```bash
git clone https://github.com/rudolffu/nicedocs.git && cd nicedocs
```

```bash
scripts/install.sh opencode
```

| Target | Installs to (user level) | Installs to (with `--project`) |
|---|---|---|
| `opencode` | `~/.config/opencode/skills/` | `.opencode/skills/` |
| `agents` (alias `codex`) | `~/.agents/skills/` | `.agents/skills/` |
| `claude` | `~/.claude/skills/` | `.claude/skills/` |
| `cursor` | `~/.cursor/skills/` | `.cursor/skills/` |
| `copilot` | `~/.copilot/skills/` | `.github/skills/` |
| `gemini` | `~/.gemini/skills/` | `.gemini/skills/` |

| Option | Effect |
|---|---|
| `--link` | Symlink instead of copy, so `git pull` updates the skills |
| `--project [DIR]` | Install into a project folder (default: the current directory) |
| `--uninstall` | Remove the skills that NiceDocs installed |
| `--dry-run` | Print what would happen without changing anything |

The installer never overwrites a folder it did not create. It skips the folder, reports
it, and exits with code `2`.

### Requirements

The plugin installs need only the host tool. The installer needs `bash` and `git`. The
validator needs Python 3.9 or later. Neither needs extra packages.

## Update and uninstall

| Platform | Update | Uninstall |
|---|---|---|
| Claude Code | `/plugin marketplace update nicedocs` | `/plugin uninstall nicedocs@nicedocs` |
| Codex | `codex plugin marketplace upgrade nicedocs` | `codex plugin remove nicedocs@nicedocs`, then `codex plugin marketplace remove nicedocs` |
| Gemini CLI | `gemini extensions update nicedocs` | `gemini extensions uninstall nicedocs` |
| Installer targets | `git pull` (with `--link`), or run the installer again | `scripts/install.sh <target> --uninstall` |

## Example prompts

| Ask | Skill used |
|---|---|
| "Write a README for this repo." | `project-docs` |
| "Draft release notes for v2.3 from the merged PRs." | `project-docs` |
| "Review this PR's docs changes for style, accessibility, and inclusive language." | `docs-review` |
| "Rewrite these error messages so they tell users how to fix the problem." | `docs-review` |
| "Convert `guide.md` to reStructuredText for our Sphinx site." | `docs-markup` |
| "Add link checking and Vale to our docs CI." | `docs-tooling` |
| "Help me write a one-page case for investing in internal docs." | `docs-advocacy` |
| "Make our docs site look more polished, and write a screenshot style guide." | `docs-design` |

## Troubleshooting

- **Skills don't appear after installing.** Restart the tool or start a new session.
  Most tools read skills only at startup.
- **The installer printed `skipped … not installed by NiceDocs`.** A folder with the
  same name already exists in the target. Rename or remove it, then run the installer
  again.
- **An agent ignores the skills.** Name the skill in your request, for example "Use the
  docs-review skill on README.md".

## Get help or contribute

- **Questions, bugs, and skill ideas:** [open an issue](https://github.com/rudolffu/nicedocs/issues).
- **Contributions:** see [CONTRIBUTING.md](CONTRIBUTING.md).
- **Documentation practice in general:** the Write the Docs community has a
  [Slack](https://www.writethedocs.org/slack/) and [meetups](https://www.writethedocs.org/meetups/).

## Repository layout

| Path | Contents |
|---|---|
| `skills/` | The skills: one source for every platform |
| `.claude-plugin/` | Claude Code plugin and marketplace manifests |
| `.codex-plugin/`, `.agents/plugins/` | Codex plugin manifest and marketplace |
| `gemini-extension.json`, `GEMINI.md` | Gemini CLI extension manifest and context file |
| `scripts/install.sh` | Installer for tools that read a skills folder |
| `scripts/validate.py` | Checks for skill spec, manifests, attribution, and links (runs in CI) |
| `docs/sources.md` | How each Write the Docs learning resource is used |
| `index.md`, `docs/conf.py`, `.readthedocs.yaml` | Documentation site (Sphinx + MyST, built by Read the Docs) |

## License and attribution

- **Content** (`skills/`, `docs/`, prose files) is licensed
  [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). It adapts the
  Write the Docs Documentation Guide, © Write the Docs contributors, which uses the same
  license.
- **Code and configuration** (`scripts/`, CI, and plugin manifests) are licensed **MIT**.

See [LICENSE.md](LICENSE.md), [REUSE.toml](REUSE.toml), and [ATTRIBUTION.md](ATTRIBUTION.md).
NiceDocs is an independent project and is not affiliated with or endorsed by Write the Docs.

Author: **Yuming Fu** ([@rudolffu](https://github.com/rudolffu)).
