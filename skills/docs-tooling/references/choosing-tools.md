# Choosing documentation tools

There are many options: paid proprietary tools that do much of the back-end work, and
highly customisable static site generators (SSGs) that need a big investment of time
and knowledge. Use these questions to choose.

## Questions to ask
1. **Budget.** Plan for both money and time.
2. **Outputs.** Website, PDF, Word, in-product help, eBook, or a help centre
   (Salesforce, Zendesk)?
3. **Programming skills.** Which languages do you, your team, or available developers
   know or want to learn?
4. **Front-end comfort.** Are you happy editing HTML, CSS, and JS, or do you want a tool
   that does the design for you?
5. **Authoring style.** WYSIWYG or a text editor? Either way, you need previews and a
   staging area for reviewers.
6. **Subject-matter-expert reviews.** Does each reviewer need a licence, or training on
   a new tool?
7. **Existing support portal** (Zendesk, Freshdesk, Salesforce Service)? Its knowledge
   base might be the best place for the docs.
8. **Existing company tooling.** Leaning on what users already use (Confluence,
   SharePoint) usually beats launching yet another site.
9. **Version control.** It has big benefits and a learning curve. Use the system the
   company already uses.
10. **Reuse and single-sourcing.** How much do you need?
11. **Markup.** reStructuredText, Markdown, AsciiDoc, DocBook, DITA? (See the
    `docs-markup` skill.)
12. **Contributors and reviewers.** How many? Licence and training costs scale with headcount.
13. **CI/CD.** Do you need pipeline support?
14. **Translation.** Will the content work with a translation pipeline?

## Considerations and gotchas
- Spinning up an SSG can cost as much time as a commercial tool costs in money.
  Consider hiring an expert for initial setup and theming.
- **Plan long-term maintenance.** Who upgrades the tooling? Who fixes it when it breaks?
- Themes get you started, but organisations want their own look. Customising takes time
  and skill.
- Reuse features vary, including how content is reused and who can reuse it.
- **Link maintenance.** Some tools track links and update them when pages move. Others
  leave it to you. Pages *will* move or be deleted, so have a plan (redirects, link
  checks).
- **Import and export.** Third parties may need to consume your content, and you may
  pull content in from elsewhere, such as code samples from an engineering repo.

## Recommendation format (for agents)
> **Recommendation:** <tool>. **Why:** <2–3 reasons tied to the answers above>.
> **Main trade-off:** <cost/risk>. **Maintenance owner:** <who>. **Alternative if <condition>:** <tool>.

---

*Adapted from "[Choosing tools for documentation](https://www.writethedocs.org/guide/choosing-tools/)" (source: [`docs/guide/choosing-tools.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/choosing-tools.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into a numbered checklist with a recommendation format for agents, by Yuming Fu, 2026.*
