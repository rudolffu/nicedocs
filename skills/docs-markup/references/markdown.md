# Markdown reference

Markdown is a free, lightweight markup language with simple formatting syntax. It is
used for web pages, documents, and any text that is converted to HTML or other formats.
It lets writers without a technical background produce docs that are easy to
collaborate on.

## Core syntax
| Purpose | Syntax |
|---|---|
| Italic | `*one star each side*` |
| Bold | `**two stars each side**` |
| Strikethrough (GitHub-flavoured) | `~~two tildes~~` |
| Link | `[link text](https://example.com)` |
| Image | `![alt text](path/or/url.png)`, a link with a leading `!` |
| Headings | `#` to `######` for levels 1 to 6 |
| Horizontal rule | `---`, `* * *`, or `___` on its own line |
| Block quote | `> ` at the start of each line |
| Inline code | single backticks: `` `code` `` |
| Code block | a line of three backticks before and after, plus an optional language |

## Lists
- Unordered: start each item with `-` (or `*`).
- Ordered: `1.`, `2.`, … Renderers renumber automatically, so `1.` on every line also works.
- Nesting: indent the child item under the parent's text. The amount varies by renderer
  (2 to 4 spaces). Unordered and ordered lists can be nested inside each other.

## Agent guidance
- Find out the **flavour** (CommonMark, GitHub-flavoured, MyST, MkDocs extensions) before
  using tables, task lists, admonitions, or footnotes.
- Always put a language on fenced code blocks so they are highlighted.
- Use raw HTML only when Markdown can't express something, and check whether the
  renderer allows it.
- Leave a blank line before and after headings, lists, and code blocks so every
  renderer parses them the same way.

## Learn more (linked)
- [Original Markdown syntax](https://daringfireball.net/projects/markdown/)
- [GitHub: basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [CommonMark spec](https://commonmark.org/)
- [Markdown Tutorial (interactive)](https://www.markdowntutorial.com/)

---

*Adapted from "[Introduction to Markdown](https://www.writethedocs.org/guide/writing/markdown/)" (source: [`docs/guide/writing/markdown.md`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/markdown.md)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into a reference table and agent guidance added, by Yuming Fu, 2026.*
