# Screenshots

## Should this be a screenshot at all?
- Screenshots go stale when the UI changes, add translation cost, and are invisible to
  screen readers without good alt text.
- **When the product changes often, use fewer screenshots** and lean on text, such as
  named UI labels in bold.
- A screenshot earns its place when it orients readers in a complex screen or confirms
  they are in the right place. Don't add one for every step.
- Line drawings survive small UI changes, but they can be harder to maintain than
  screenshots. Weigh this before choosing them.

## A screenshot style guide (for teams)
Write these decisions down once, so every screenshot looks like it belongs to the same docs.

**Capture**
- Use a laptop or main desktop display, unless the product is mobile.
- Set a maximum width (for example 1000 px), and never enlarge small images.
- Choose light mode, dark mode, or both, and apply it consistently.
- Use the same operating system and browser for every capture. Normalize window and
  UI size.
- Tell readers which platform and browser the screenshots show, and that their screen
  may differ by version or enabled features.

**Crop and compose**
- Crop tightly to remove clutter, but keep enough surrounding context to locate the element.
- Crop in a screenshot tool or image editor, not in the authoring tool.
- Show UI elements in context rather than floating on their own.
- Remove or cover interface elements you aren't discussing. That means fewer updates and
  lower translation cost.

**Treat and annotate**
- Add a thin border so light images stand out from a light page.
- Blur or replace real data, such as names, emails, and tokens. Use believable fictional
  data (see the `docs-review` skill's inclusive example names).
- Don't write text on the screenshot itself. It can't be translated, searched, or read
  aloud.
- Use rectangles for groups of elements and arrows or circles for a single element. Leave
  space between annotations and UI edges, and keep annotations to a few per image.
- Describe the annotations in the surrounding text too, for accessibility.

**Files and text**
- Use descriptive file names, such as `settings-api-keys-panel.png`, not `Screenshot 3.png`.
- Write brief, purpose-focused alt text (see [diagrams-and-media.md](diagrams-and-media.md)).
- Coordinate colors, sizes, and branding with design or marketing where they exist.

## Keeping screenshots current
- Update a screenshot when the area it focuses on changes. Changes elsewhere in the UI can
  wait until they are noticeable or confusing.
- If you have many screenshots, automate capture with browser automation such as
  Selenium or Playwright. Automation also helps with localized screenshots.
- Capture tools mentioned by the community include Snagit (paid), Greenshot (free, open
  source), Skitch (free, macOS and iOS), Screenpresso, and LightShot.

---

*Adapted from "Create a screenshot style guide" in the [Write the Docs newsletter, November 2025](https://www.writethedocs.org/blog/newsletter-november-2025/) (source: [`docs/blog/newsletter-november-2025.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/blog/newsletter-november-2025.rst)) and "Tips for creating quality screenshots" in the [newsletter, May 2020](https://www.writethedocs.org/blog/newsletter-may-2020/) (source: [`docs/blog/newsletter-may-2020.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/blog/newsletter-may-2020.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: merged, condensed, and organized into a style-guide template for agents by Yuming Fu, 2026.*
