# Testing documentation

Testing keeps docs consistent, gives users a better experience, and takes the stress out
of common problems. The most useful tests run on every commit, in **continuous
integration** (GitHub Actions, GitLab CI/CD).

## Layer 1: the build succeeds
Run the docs tool in CI. Most tools exit with code 0 on success, so CI fails
automatically on errors. Once the docs are clean, turn on the *picky* mode that also
fails on warnings:
- Sphinx: `sphinx-build -W --keep-going -n docs docs/_build/html` (`-n` is nitpicky)
- Jekyll: strict mode for Liquid (`strict_filters`, `strict_variables`)

## Layer 2: links work
Dead links leave users at dead ends, and link checks are easy to automate. Either use
your tool's checker or treat the rendered site as a website:
- Sphinx: `make linkcheck` (the built-in `linkcheck` builder)
- [HTMLProofer](https://github.com/gjtorikian/html-proofer): checks links, images, and
  HTML validity in the output of any SSG
- General-purpose checkers such as [lychee](https://github.com/lycheeverse/lychee) work on
  Markdown sources or built HTML.

Tip: run external-link checks on a schedule rather than on every pull request, so flaky
third-party sites don't block merges.

## Layer 3: style and prose linting
Linters automatically enforce rules such as style-guide terms and brand capitalisation.

**[Vale](https://vale.sh/)** is a fast, syntax-aware prose linter. It ships with no rules.
You add packages from the [Vale package hub](https://vale.sh/explorer), for example
Microsoft, Google, proselint, write-good, and Joblint.

```ini
# .vale.ini at the repository root (Vale finds it automatically)
StylesPath = .vale/styles
MinAlertLevel = suggestion
Packages = Google, write-good

[*.{md,rst,adoc}]
BasedOnStyles = Vale, Google, write-good
```

```bash
vale sync            # download the listed packages
vale ls-config       # confirm the settings were picked up
vale docs/           # lint files or directories
```

Vale also lints XML (DocBook, DITA) if `*.xml` is included in a section glob. Keep a
project vocabulary (`Vocab`) so product names aren't flagged.

Real-world configs to learn from: [Write the Docs](https://github.com/writethedocs/www/blob/main/vale/vale.ini).

## Example GitHub Actions job (Sphinx)
```yaml
name: docs
on: [pull_request]
jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r docs/requirements.txt
      - run: sphinx-build -W --keep-going -n docs docs/_build/html
      - uses: errata-ai/vale-action@v2
```

---

*Adapted from "[Testing your documentation](https://www.writethedocs.org/guide/tools/testing/)" (source: [`docs/guide/tools/testing.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/tools/testing.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into layers, example configs and CI job added for agents, by Yuming Fu, 2026.*
