# Starting a brand-new piece of documentation

## Step 1: talk to the experts (or read what they wrote)
Before you write, learn about the product from developers, product managers, or
project managers. As an agent, also read the code, specs, tickets, and existing docs.
Answer these questions:
- What does the product do? What does it let users achieve?
- Is it aimed at a particular kind of user or business role? What do those users care about?

The answers tell you which workflows to cover, which features and concepts need
explaining, and how to organise the content.

## Step 2: let product type and audience choose the shape

| Situation | Likely shape |
|---|---|
| Product must be installed; audience is sysadmins | Cover many installation scenarios, including complex ones |
| Product must be installed; audience is less technical | One recommended install path, written step by step |
| GUI application with fixed ways to do each task | User guide that walks through each workflow step by step |
| SDK or set of APIs used in many ways | Reference guide with one entry per API, easy to scan, often alphabetical |

Understanding the product and its users decides both *what* to write about and *how*.

## Picking a starting point by situation
- **Open-source developer:** start with the README essentials (see
  [what-to-include.md](what-to-include.md)).
- **Developer at a company who must justify docs time:** use the `docs-advocacy` skill to
  make the case and plan the rollout.

---

*Adapted from "[Starting on a new piece of documentation](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/Starting-a-new-doc.rst)" (source: `docs/guide/Starting-a-new-doc.rst`) and "[Getting started: documentation best practices for developers](https://www.writethedocs.org/guide/starting/)" (source: [`docs/guide/starting.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/starting.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed and merged into a decision table for agents by Yuming Fu, 2026.*
