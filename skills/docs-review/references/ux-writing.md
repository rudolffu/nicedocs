# UX writing and microcopy

UX writing produces the text users see in an interface: buttons, labels, tooltips, empty
states, confirmations, error messages, and CLI output. It is often called *microcopy*.
It designs the conversation between a product and its user, and it rests on the same
skills as technical writing: clarity, consistency, precision, revision, and attention
to context and audience. Tech writers and UX writers are often the same person.

## Microcopy checklist
- [ ] **Clear.** Says exactly what happens. Button labels are verbs that name the action
      ("Save draft", not "OK").
- [ ] **Concise.** Shortest wording that is still unambiguous.
- [ ] **Consistent.** The same action has the same name everywhere, matching the docs.
- [ ] **Contextual.** Fits the user's state and task at that moment.
- [ ] **Human.** Plain words, no internal jargon or codes without explanation.

## Error messages
Errors can't be avoided, but how they are worded decides whether users feel alienated
or helped. A good error message:
1. clearly says that something went wrong
2. is written like a human, not a robot
3. doesn't blame the user
4. is short and meaningful
5. describes the exact problem precisely
6. offers constructive advice on how to fix it.

Rewrite pattern: **what happened** + **why, if known** + **what to do next**.

| Before | After |
|---|---|
| `Error 0x80070005` | `Can't save report.pdf: you don't have permission to write to /reports. Choose another folder or ask an admin for access.` |
| `Invalid input` | `Port must be a number between 1 and 65535. You entered "80a".` |

## Learn more (linked)
- [NN/g error message guidelines](https://www.nngroup.com/articles/error-message-guidelines/)
- [PostgreSQL error message style guide](https://www.postgresql.org/docs/current/error-style-guide.html)
- [Microsoft error message guidelines](https://learn.microsoft.com/en-us/windows/win32/debug/error-message-guidelines)
- Books cited by WTD (not reproduced): *Microcopy: The Complete Guide* (Kinneret Yifrah); *Letting Go of the Words* (Janice Redish); *Don't Make Me Think* (Steve Krug)

---

*Adapted from "[UX writing](https://www.writethedocs.org/guide/ux-writing/)" (source: [`docs/guide/ux-writing.rst`](https://github.com/writethedocs/www/blob/c37669d0c87740b1455821cbee7fc10c8ee6cf7f/docs/guide/ux-writing.rst)) and the "Error messages" section of "[Style Guides](https://www.writethedocs.org/guide/writing/style-guides/#error-messages)" (source: `docs/guide/writing/style-guides.md`), © Write the Docs contributors, licensed [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Changes: condensed; checklists and rewrite examples added for agents by Yuming Fu, 2026.*
