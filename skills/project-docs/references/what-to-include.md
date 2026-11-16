# What to include in software documentation

## Why the docs are worth writing (use when motivating the work)
- **Future you.** Code written six months ago reads like a stranger's code.
- **Adoption.** People skip projects when they can't tell why the project exists, how to
  install it, or how to use it.
- **Contributions.** Contributors need docs to get started, and doc fixes are often the
  easiest first contribution.
- **Better code.** Writing down API and design decisions forces you to think them through,
  and lets others contribute in line with the original intent.
- **Better writing.** Technical writing is a skill that improves with practice.

## Know the audience
- **Users** want to use the code and do not care how it works.
- **Developers or contributors** want to change the code.
Write for one audience at a time. Separate the user docs from the contributor docs.

## The essential elements

| Element | What good looks like | Exemplar cited by WTD |
|---|---|---|
| Problem the project solves | What it does and why, stated where search and word of mouth land | [Fabric](https://docs.fabfile.org/) |
| Small code example | One common use case, short and runnable | [Requests](https://requests.readthedocs.io/) |
| Code and issue tracker links | Easy to browse the source and file bugs | [The Hitchhiker's Guide to Python](https://docs.python-guide.org/) |
| How to get support | Channels for help and community interaction | [Django](https://docs.djangoproject.com/en/stable/faq/help/) |
| How to contribute | The project's own contribution process and standards | — |
| Installation | One or two lines for the basic case, with a link to details and caveats | [Read the Docs](https://docs.readthedocs.com/dev/latest/install.html) |
| License | One standard license, named clearly | — |

## FAQs: use sparingly
FAQs can be starter docs, but they:
- go out of date quickly
- collect unrelated topics
- become hard to sort and search
- are rarely made of questions real users asked
- tempt authors to use them as a quick fix instead of writing real docs.

## Tools and formats
Developers live in plain text, so their docs should too. Choose plain-text markup that
renders to HTML and is tracked in version control. Markdown and reStructuredText are the
usual choices; see the `docs-markup` skill. Some projects start with the README, before
any code ("README-driven development").

## Further reading
- [README Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html) (Tom Preston-Werner)

---

*Adapted from "[How to write software documentation](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)" (source: [`docs/guide/writing/beginners-guide-to-docs.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/writing/beginners-guide-to-docs.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into tables and checklists for agents by Yuming Fu, 2026.*
