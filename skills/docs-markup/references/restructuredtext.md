# reStructuredText (reST) reference

reStructuredText is a lightweight markup language used by static site generators such as
Sphinx. It has strong tools for semantic markup, content reuse, and output-specific
filtering. It can be extended with custom **directives**. It is the standard for the
Python language docs and many Python libraries.

**Why choose it:** it reads more easily as plain text than XML formats like DITA. It has
stronger semantic markup than Markdown, and its specification is more tightly defined.

## Paragraphs and inline markup
- Paragraphs are separated by blank lines. All lines in a paragraph have the same indent.
- `*italic*`, `**bold**`, and ``` ``inline code`` ``` (two backticks).
- External link: ``` `Link text <https://example.com/>`_ ``` (note the trailing underscore).

## Headings
Mark headings by underlining them, or underlining and overlining them, with a
non-alphanumeric character (`=`, `-`, `~`, …):

```rst
=========
Chapter 1
=========

Section 1.1
-----------
```

- Within a file, the same character and style always means the same level. Underline-only
  and over-and-underline with the same character count as *different* levels.
- The rule must be at least as long as the heading text.

## Lists
```rst
1. Arabic numbers        A. Letters (upper or lower)       I. Roman numerals
(1) Parenthesized        1) Right bracket                  #. Auto-numbered

* Bullet (``-``, ``+``, or ``*``)

  - Nested bullet. Indent it and put a blank line before it.
```

## Code samples
End the preceding paragraph with `::` and indent the code. Or use a directive for
highlighting:

```rst
Run this::

    pip install sphinx

.. code-block:: python

   import project
```

## Directives you will meet in Sphinx
`.. toctree::`, `.. note::`, `.. warning::`, `.. image::`, `.. include::`,
`.. code-block::`, and the roles `:ref:` and `:doc:`. See the `docs-tooling` skill
for Sphinx.

## Learn more (linked)
- [Sphinx reStructuredText primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
- [Docutils reStructuredText quick start](https://docutils.sourceforge.io/docs/user/rst/quickstart.html)
- [Docutils directives reference](https://docutils.sourceforge.io/docs/ref/rst/directives.html)

---

*Adapted from "[Introduction to reStructuredText](https://www.writethedocs.org/guide/writing/reStructuredText/)" (source: [`docs/guide/writing/reStructuredText.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/reStructuredText.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed; Sphinx directive pointers added for agents by Yuming Fu, 2026.*
