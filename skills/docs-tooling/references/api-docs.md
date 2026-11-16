# API documentation

Clear, well-formatted, detailed API docs let developers adopt an API quickly. They
explain what happens on each call and, when a call fails, what went wrong and how to
fix it. From the user's side, **an undocumented feature doesn't exist, and a wrongly
documented one is broken.** Good API docs usually come from a well-designed API.
Docs can't rescue a bad design, so develop the API and its docs together.

## Approaches
- **Documentation-driven design.** Documentation changes are cheap; code changes are
  expensive. Draft the API docs before you build, get feedback, and iterate.
- **Generated reference for existing APIs.** Generate it from the code or the description
  file, and hand-write the overview, concepts, and tutorials.
- **Test-driven documentation.** Hand-write most of the docs, but generate request and
  response snippets from the API's tests, for example with
  [Spring REST Docs](https://spring.io/projects/spring-restdocs). If the API and docs
  drift apart, the tests fail.

## Description languages
- **[OpenAPI](https://www.openapis.org/)** (formerly Swagger) is the most widely used.
- **API Blueprint** (`.apib`) is Markdown plus MSON for data structures, and is
  design-first. File structure: `Metadata → API name → Resource groups → Resources →
  Actions (HTTP verbs) → Data structures` (reusable request and response models).

Machine-readable descriptions make other tools possible:
- mock servers during design
- contract tests that check the API matches the description before deployment
- interactive docs with "try it" requests.

## Rendering and hosting
- Services such as Apiary render API Blueprint or OpenAPI as interactive three-column
  docs with multi-language examples.
- Sphinx can include API docs, for example with OpenAPI extensions, alongside your prose.
- Choose an OpenAPI renderer that fits your site generator.

## Testing API docs
Don't validate descriptions by hand. Tools such as [Schemathesis](https://schemathesis.readthedocs.io/)
test an OpenAPI description against the live API.

## API reference checklist (per endpoint or method)
- [ ] Purpose in one sentence
- [ ] Auth requirements
- [ ] Parameters: name, type, required or optional, default, constraints
- [ ] Request example and response example (success *and* error)
- [ ] Error codes, with causes and fixes
- [ ] Rate limits, pagination, and versioning notes

## Learn more (linked)
- [Documenting APIs (Tom Johnson)](https://idratherbewriting.com/learnapidoc/)
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)

---

*Adapted from "[API documentation tools](https://www.writethedocs.org/guide/api/api-documentation-tools/)" (source: [`docs/guide/api/api-documentation-tools.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/api/api-documentation-tools.rst)) and the "API documentation" section of "[Style Guides](https://www.writethedocs.org/guide/writing/style-guides/#api-documentation)" (source: `docs/guide/writing/style-guides.md`), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed, merged; reference checklist added for agents by Yuming Fu, 2026.*
