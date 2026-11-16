# Style guides

A style guide is a set of standards for writing and designing content. It keeps style,
voice, and tone consistent, whether you write alone or with a large team. It gives one
reference for common topics and can cover different deliverables: API reference,
tutorials, release notes, concept overviews.

## Write your own, or adopt one?
- A style guide can be as small as a list of decisions about how to refer to the things
  you often write about, or as large as a publisher's manual.
- A lone writer or a new small team can start their own. Still consult existing guides:
  they show which decisions matter.
- A practical pattern: **adopt a published guide as the base, and keep a short project
  guide of overrides** (product names, terminology, capitalization, code formatting).

Minimal project style guide outline:
1. Base guide and precedence ("We follow X except where noted").
2. Voice and tone (for example: second person, active voice, present tense).
3. Terminology list: preferred term, terms to avoid, capitalization.
4. Formatting: headings, code, UI labels, placeholders, notes and warnings.
5. Accessibility and inclusive-language rules (see the sibling references).
6. Content-type rules: tutorials, how-tos, reference, release notes, error messages.

## Published guides (linked; consult the original)
Traditional general references: [AP Stylebook](https://www.apstylebook.com/),
[Chicago Manual of Style](https://www.chicagomanualofstyle.org/).

Software documentation:
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)
- [Apple Style Guide](https://help.apple.com/applestyleguide/)
- [Google developer documentation style guide](https://developers.google.com/style)
- [Red Hat supplementary style guide](https://redhat-documentation.github.io/supplementary-style-guide/)
- [Mailchimp content style guide](https://styleguide.mailchimp.com/)

Government and plain language:
- [GOV.UK writing guidance](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/tone-of-voice/)
- [US Federal Plain Language Guidelines](https://digital.gov/guides/plain-language)

Open source:
- [SUSE Documentation Style Guide](https://documentation.suse.com/style/current/)
- [GNOME developer documentation guidelines](https://developer.gnome.org/documentation/guidelines/devel-docs.html)

## Developer, API, and CLI content
- **API reference comments:** follow your language's conventions, for example the
  [Google API reference comments guide](https://developers.google.com/style/api-reference-comments).
- **CLI docs and help text:** see [Command Line Interface Guidelines](https://clig.dev/#guidelines),
  the [Heroku CLI style guide](https://devcenter.heroku.com/articles/cli-style-guide),
  and the Google guide's [command-line syntax conventions](https://developers.google.com/style/code-syntax).
  Document syntax with clear placeholders and mark optional versus required arguments
  consistently.
- **API docs in general:** if a feature is undocumented, it doesn't exist for users. If it
  is documented wrongly, it is broken. Docs cannot fix a poorly designed API, so design
  and document together (see the `docs-tooling` skill on documentation-driven design).

## Idioms to flag
Idioms that refer to violence toward animals confuse non-native readers and are easy
to replace:

| Instead of | Use |
|---|---|
| kill two birds with one stone | accomplish two things at once |
| beat a dead horse | belabor the point |
| more than one way to skin a cat | more than one way to do this |

Leave established technical terms unchanged: `kill` (signal), canary deployment,
monkey-patching.

---

*Adapted from "[Style Guides](https://www.writethedocs.org/guide/writing/style-guides/)" (source: [`docs/guide/writing/style-guides.md`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/style-guides.md)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed, selected links, and added a project style-guide outline for agents, by Yuming Fu, 2026.*
