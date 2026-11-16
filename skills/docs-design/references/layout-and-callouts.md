# Layout and callouts

## Callouts (admonitions)
Callouts are boxed sections that stand out from the body text. They highlight important
information and keep docs easy to navigate.

**Use a small, consistent set of types.** Many style guides use four, ordered by severity:

| Type | Use it for | Example |
|---|---|---|
| **Tip** | Helpful advice that makes a task easier but isn't critical | A keyboard shortcut |
| **Note** | Relevant context that doesn't change the outcome of the task | Where a setting is stored |
| **Important** | Information that, if missed, causes frustration or extra work | You must restart after changing this |
| **Warning** | Risk of data loss or a security problem | This deletes all backups |

**Use them sparingly.** Too many notes, tips, and warnings cause *admonition fatigue*:
readers start skipping callouts, including the critical ones.

**Callout or inline text?** If the information is crucial *and* easy to miss, use a
callout. Otherwise, put it in the main text, where it reads more smoothly.

Agent checklist:
- [ ] No more than one or two callouts per screen of text. Never stack callouts back to back.
- [ ] The severity matches the consequence. Warnings are reserved for real risk.
- [ ] Each callout starts with the key point, not "Please note that…".
- [ ] Use the platform's native syntax: GitHub alerts (`> [!NOTE]`), MyST and reST
      directives (`:::{note}` / `.. note::`), AsciiDoc labels (`NOTE:`). See the
      `docs-markup` skill.

## Page layout basics
These are general readability guidelines, added for agents:
- **Line length.** Body text is most comfortable at roughly 50–80 characters per line. If
  a theme runs text edge to edge on wide screens, constrain the content width.
- **One idea per paragraph,** with the key concept in the first sentence (the Skimmable
  principle).
- **Headings every few paragraphs.** Readers navigate by them, and so does the table of
  contents.
- **Tables for comparisons** of three or more items across the same attributes. Lists for
  sequences and sets. Avoid tables used only for layout.
- **Code blocks:** language-tagged, short, copyable, and with prompts (`$`) left out so
  they paste cleanly. Show output separately.
- **White space is not wasted space.** Avoid crowding images, callouts, and code together.

## Further reading (linked)
- "Using callouts/admonitions in tech docs", [WTD newsletter, October 2024](https://www.writethedocs.org/blog/newsletter-october-2024/)
- "What to do about text wrapping", [WTD newsletter, July 2019](https://www.writethedocs.org/blog/newsletter-july-2019/)
- [WTD topic archive](https://www.writethedocs.org/topics/): layout, design, and information architecture talks

---

*Adapted from the "Using callouts/admonitions in tech docs" section of the [Write the Docs newsletter, October 2024](https://www.writethedocs.org/blog/newsletter-october-2024/) (source: [`docs/blog/newsletter-october-2024.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/blog/newsletter-october-2024.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into a table and checklist. The page-layout basics are original work by Yuming Fu, 2026.*
