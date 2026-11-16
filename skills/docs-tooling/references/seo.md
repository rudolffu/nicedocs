# Search engine optimization (SEO) for documentation

For public docs sites, search engines bring a large share of the traffic. SEO is about
improving how pages rank for relevant searches. Search algorithms change often, so
specific tactics go out of date. The good news is that good technical writing already
covers most of what SEO needs.

## Checklist
- [ ] **Headings** are imperative, user-centred, and goal-oriented, for example
      "Configure SSO with Okta", not "SSO".
- [ ] **Skimmable structure:** content is broken into sections under appropriate headings.
- [ ] **Information architecture:** clear navigation, site hierarchy, and breadcrumbs.
- [ ] **Page metadata** in `<head>`: a unique `<title>`, a meta description, the canonical
      URL, and the last-modified date. How you set these depends on the toolchain.
- [ ] **Accessibility** standards are met (see the `docs-review` skill). Many accessibility
      fixes also help SEO.
- [ ] Practical extras: a `sitemap.xml`, descriptive URLs, redirects for moved pages, and a
      canonical URL on versioned docs so the old versions don't compete in search results.

## Search-engine documentation (linked)
- [Google Search Central](https://developers.google.com/search/docs)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)

---

*Adapted from "[Search engine optimization (SEO) for documentation](https://www.writethedocs.org/guide/seo/)" (source: [`docs/guide/seo.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/seo.rst)), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed into a checklist; practical extras added by Yuming Fu, 2026.*
