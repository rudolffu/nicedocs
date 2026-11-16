# XML reference (for documentation)

XML is a meta markup language derived from SGML. HTML defines how data *looks*; XML
defines what data *is*. You invent tags and attributes, which in effect creates your
own markup language and gives documents explicit structure. It is plain text, so it
stays independent of software and hardware, and it underlies Office formats, RSS, SVG,
and documentation standards such as **DocBook** and **DITA**.

## Example: semantic tags
```xml
<tree>
  <name>Sugar Maple</name>
  <height units="m">30</height>
  <type>Deciduous</type>
</tree>
```

## Displaying XML
XML needs a stylesheet (CSS or XSLT) to be readable. Styles target your own tags rather
than HTML's:

```xml
<?xml-stylesheet type="text/css" href="trees.css"?>
```
```css
name { font-size: 2em; font-weight: bold; }
height, type { font-size: 1em; }
```

## Agent guidance
- For documentation, prefer an established schema (DocBook, DITA) over invented tags,
  so existing toolchains, validation, and transforms work.
- Validate against the schema or DTD after editing. Well-formedness alone is not enough.
- Prose linters such as Vale can lint XML if `*.xml` is included in their config. See the
  `docs-tooling` skill.

## Learn more (linked)
- [W3Schools XML tutorial](https://www.w3schools.com/xml/default.asp)
- [DocBook](https://docbook.org/) · [DITA (OASIS)](https://www.oasis-open.org/committees/dita/)

---

*Adapted from "[Introduction to XML](https://www.writethedocs.org/guide/writing/xml/)" (source: [`docs/guide/writing/xml.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/xml.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed; agent guidance on schemas and validation added by Yuming Fu, 2026.*
