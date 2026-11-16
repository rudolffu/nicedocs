---
name: docs-markup
description: Write, fix, and convert documentation markup in Markdown, reStructuredText (reST, Sphinx), AsciiDoc (Asciidoctor, Antora), and XML (DocBook, DITA), and choose between them. Use when formatting docs, converting between .md, .rst, and .adoc, fixing rendering problems such as broken headings, lists, links, or code blocks, or deciding which markup language a docs project should use.
license: CC-BY-NC-SA-4.0
metadata:
  author: Yuming Fu
  source: Write the Docs Documentation Guide (writethedocs/www@c37669d)
---

# Documentation markup

Plain-text markup keeps docs in version control and lets them render to HTML, PDF, and
more. Pick the lightest markup that meets the project's needs, and follow what the
project already uses.

## Choosing a markup language

| Need | Good fit | Why |
|---|---|---|
| READMEs, wikis, contributors with little tooling | **Markdown** | Simplest syntax; renders everywhere. Know which flavour (CommonMark, GitHub-flavoured) |
| Python projects, Sphinx, semantic cross-references, content reuse | **reStructuredText** | Directives and roles, well-defined spec, extensible |
| Book-like publishing to HTML, PDF, EPUB, and man pages; Antora sites | **AsciiDoc** | Rich built-in structure (admonitions, includes, callouts, ToC) |
| Structured authoring, heavy single-sourcing, enterprise pipelines | **XML** (DocBook, DITA) | You define the semantics; very reusable, but heavyweight |
| Sphinx project, but authors prefer Markdown | **MyST Markdown** | Markdown with Sphinx directives and roles |

## Workflow
1. **Detect** the markup and flavour from the file extensions, the generator config
   (`conf.py`, `mkdocs.yml`, `antora.yml`, `docusaurus.config.*`), and the existing files.
   Match the existing conventions, such as heading underline characters and list markers.
2. **Write or fix** using the per-language reference:
   - [references/markdown.md](references/markdown.md)
   - [references/restructuredtext.md](references/restructuredtext.md)
   - [references/asciidoc.md](references/asciidoc.md)
   - [references/xml.md](references/xml.md)
3. **Convert** with the equivalence table below. Then fix by hand the features that have
   no equivalent (reST directives, AsciiDoc callouts). Tools such as
   [Pandoc](https://pandoc.org/) can do a first pass; always review the output.
4. **Verify** by building or previewing when a toolchain is available. Otherwise
   re-read for whitespace-sensitive constructs: reST indentation and AsciiDoc block
   delimiters.

## Quick equivalence table

| Construct | Markdown | reStructuredText | AsciiDoc |
|---|---|---|---|
| Title / H1 | `# Title` | `Title` with `=====` overline and underline | `= Title` |
| Section / H2 | `## Section` | `Section` with `-----` underline | `== Section` |
| Italic | `*text*` | `*text*` | `_text_` |
| Bold | `**text**` | `**text**` | `*text*` |
| Inline code | `` `code` `` | ``` ``code`` ``` | `` `code` `` |
| Link | `[text](https://url)` | ``` `text <https://url>`_ ``` | `https://url[text]` |
| Image | `![alt](img.png)` | `.. image:: img.png` + `:alt: alt` | `image::img.png[alt]` |
| Code block | fenced ```` ```lang ```` | `.. code-block:: lang` + indented body (or `::`) | `[source,lang]` + `----` delimiters |
| Bullet list | `- item` | `- item` (blank line before nested lists) | `* item`, `** nested` |
| Numbered list | `1. item` | `1. item` or `#. item` | `. item`, `.. nested` |
| Note | `> **Note**` (or a flavour-specific alert) | `.. note::` | `NOTE: text` |
| Include file | flavour/tool-specific | `.. include:: file.rst` | `include::file.adoc[]` |

## Common pitfalls
- **Markdown:** different renderers disagree on nested-list indentation and on tables.
  Raw HTML is an escape hatch, but it hurts portability and accessibility.
- **reST:** it is whitespace-sensitive. Inconsistent indentation breaks blocks. Heading
  underlines must be at least as long as the text. The same character means the same
  level within a file.
- **AsciiDoc:** constrained (`*b*`) versus unconstrained (`**b**`) formatting matters in
  the middle of a word. The header must not contain blank lines.
- **All:** use relative links between pages so docs work in the repo and on the site.
