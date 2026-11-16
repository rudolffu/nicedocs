# Accessibility (a11y) for documentation

Writing for accessibility means screen readers can read the text, the content is well
organised, emphasis and colour stay readable, and more. Docs are part of the product,
so they need the same accessibility care. (`a11y` is a numeronym: "a", then 11 letters,
then "y".)

## Review checklist
Structure
- [ ] One H1 per page. Heading levels are not skipped. Headings describe their sections.
- [ ] Real list and table markup, not text aligned with spaces.
- [ ] Tables have header rows and are used for data, not for layout.

Text
- [ ] Plain, concise sentences. Jargon and acronyms are expanded on first use.
- [ ] Instructions do not rely only on sensory or spatial cues ("the green button", "on
      the right"). Name the control.
- [ ] Emphasis (bold, italics, colour) is never the only carrier of meaning.

Links
- [ ] Link text describes the destination and is unique on the page. No "click here" or
      "read more".
- [ ] Links that open files or new windows say so.

Images and media
- [ ] Informative images have alt text that conveys their purpose. Decorative images
      have empty alt text.
- [ ] Diagrams and screenshots have a text equivalent for the essential information.
- [ ] Videos have captions and transcripts.
- [ ] Code is shown as text in code blocks, never as an image.

Visual (for rendered sites)
- [ ] Contrast is sufficient, and content still works when zoomed or in high-contrast mode.
- [ ] Code blocks and tables are keyboard-scrollable.

## Learn more (linked)
- [MDN: What is accessibility?](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility)
- [W3C WAI foundations course](https://www.w3.org/WAI/courses/foundations-course/)
- [WebAIM](https://webaim.org/)
- [Mailchimp: writing for accessibility](https://styleguide.mailchimp.com/writing-for-accessibility/)
- [Microsoft Style Guide: accessibility terms](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/accessibility-terms)

---

*Adapted from "[Accessibility guidelines: for writing and beyond](https://www.writethedocs.org/guide/writing/accessibility/)" (source: [`docs/guide/writing/accessibility.md`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/accessibility.md)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed; review checklist written for agents by Yuming Fu, 2026.*
