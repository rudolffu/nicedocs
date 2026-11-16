# AsciiDoc reference

AsciiDoc is a text format designed for publishing, both print and web. It covers notes,
articles, books, slides, web pages, and technical manuals. It converts to HTML, PDF,
EPUB, DocBook, and man pages. GitHub renders it directly. **Asciidoctor** (2013) is the
modern toolchain (Ruby, JavaScript, JVM), and **Antora** builds documentation sites from it.
Extensibility is a core design goal, which makes AsciiDoc content highly reusable.

## Paragraphs and formatting
- A paragraph is consecutive lines. Separate paragraphs with a blank line. Single line
  breaks inside a paragraph are not shown.
- Constrained formatting works on whole words; unconstrained (doubled) markers work inside
  a word: `*bold*` / `**b**old`, `_italic_` / `__i__talic`, `` `mono` `` / ``` ``m``ono ```.
  These combine, for example `` `*_mono bold italic_*` ``.

## Document title, header, and sections
```asciidoc
= Document Title
Author Name <author@example.com>
v1.0, 2026-01-01
:toc: right

== Level 1 section (rendered as <h2>)
=== Level 2 section
```
The header is optional, may not contain blank lines, and must be followed by one blank line.

## Lists
```asciidoc
* level 1          . Step 1          * [x] done
** level 2         .. Step 1a        * [ ] to do
*** level 3        . Step 2

Term:: Description list entry
Nested term::: Deeper entry
```

## Links, anchors, and cross-references
```asciidoc
https://asciidoctor.org[Asciidoctor]     link:index.html[Docs]
[[install]]== Installation               See <<install>> or <<install,the install guide>>.
```

## Images
```asciidoc
image::diagram.png[Alt text,300,200]          (block)
Click image:icons/play.png[Play] to start.    (inline)
```

## Source code with callouts
```asciidoc
.app.rb
[source,ruby]
----
require 'sinatra' // <1>
----
<1> Library import
```

## Tables, admonitions, includes
```asciidoc
.Table title
|===
|Column 1 |Column 2

|Cell |Cell
|===

NOTE: Five built-in labels: NOTE, TIP, IMPORTANT, WARNING, CAUTION.

[WARNING]
====
Admonition blocks can contain lists and other blocks.
====

include::installation.adoc[]
```

## Learn more (linked)
- [Asciidoctor documentation](https://docs.asciidoctor.org/)
- [AsciiDoc syntax quick reference](https://docs.asciidoctor.org/asciidoc/latest/syntax-quick-reference/)
- [Antora](https://antora.org/)

---

*Adapted from "[Introduction to AsciiDoc](https://www.writethedocs.org/guide/writing/asciidoc/)" (source: [`docs/guide/writing/asciidoc.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/asciidoc.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into compact syntax blocks for agents by Yuming Fu, 2026.*
