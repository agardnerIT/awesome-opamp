# Contributing to Awesome OpAMP

Thank you for contributing! Please follow these guidelines to keep the list
consistent and high-quality.

## What belongs here

- **Standard OpAMP only.** Projects must implement OpAMP according to the
  [OpenTelemetry specification](https://opentelemetry.io/docs/specs/opamp/).
  Tools that only speak a vendor's own proprietary management API are out of
  scope and will not be accepted.
- Open-source projects, or freely accessible resources (specs, docs, talks,
  articles).
- Working, maintained projects. Dead or abandoned projects may be removed.

## Entry format

Each entry is a single bullet in the correct section:

```markdown
- [Project Name](https://link-to-project) - One-line description of what it does and why it is great.
```

Rules:

- **Name** — the project's proper name; no marketing labels like "Awesome" or
  "Modern".
- **Link** — the canonical link (repository homepage or docs). No deep links to
  binaries or installers.
- **Description** — one line, sentence case, ending with a period. Say what it
  does, not what the README says about it. No "Official website" as a
  description.
- Place the entry alphabetically within its section.
- Sections stay in the same order as the Table of contents — update both if you
  add a new section.

## Submitting

1. Fork the repo and create a branch.
2. Add your entry (and update the table of contents if you add a section).
3. Run `python3 scripts/validate.py` — it enforces the structural rules above and
   must exit 0. (AI agents: see [AGENTS.md](AGENTS.md) for the full agent rules.)
4. Open a pull request using the template. CI runs the validator plus a
   dead-link check — all links must resolve.
5. Keep PRs to one topic so they are easy to review.

## Adding a new section

New sections are welcome if there is enough material to fill them. Put the
section in the README, keep it in sync with the Table of contents, and explain
in your PR why the existing sections don't cover it.
