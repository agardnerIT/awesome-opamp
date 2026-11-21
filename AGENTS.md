# AGENTS.md

Instructions for AI agents contributing to this repository.

**This is an "awesome list"** — a curated, human-reviewed catalog of OpAMP
(Open Agent Management Protocol) resources. The only artifact is `README.md`.
Everything else is infrastructure (CI, templates, this file).

## Read first

1. [`CONTRIBUTING.md`](CONTRIBUTING.md) — entry format, scope, process. These rules apply to you exactly as to human contributors.
2. [`README.md`](README.md) — the list itself. Note how existing entries look and mirror them.

## Non-negotiable rules

- **Standard OpAMP only.** Projects must implement OpAMP per the
  [OpenTelemetry specification](https://opentelemetry.io/docs/specs/opamp/).
  Tools that only speak a vendor's proprietary management API are out of scope
  — do not add them, do not propose them.
- **Entry format** (exact):
  ```markdown
  - [Project Name](https://canonical-link) - One-line description ending with a period.
  ```
- **Alphabetical order**, case-insensitive, within each section (ties: by URL).
  No prioritizing, no favorites.
- **Neutral descriptions.** Describe what a project does, not how great it is.
  No marketing words ("modern", "best", "awesome"). The list author's own
  projects follow the same rules as everyone else's.
- **Canonical links only** — repo homepage or official docs. Never deep links
  to binaries, releases or installers.
- **One PR per entry.** Don't bundle unrelated entries or drive-by changes.
- **Update the Table of contents** when adding a new `##` section.

## Self-check before committing

```bash
python3 scripts/validate.py
```

This enforces the structural rules above. It must exit 0. CI runs the same
check plus a dead-link scan (lychee) on every PR — your PR must pass both.
If lychee flags your link, the link is wrong: fix it, don't exclude it.

## Common failure modes for agents

- Adding an entry and leaving the `_Nothing here yet — please
  [contribute](CONTRIBUTING.md)!_` placeholder in the same section — the
  validator catches this; remove the placeholder when you add the first entry.
- Inventing a description from a project's marketing site. Prefer the project's
  own repository description; verify the URL resolves.
- Placing yourself (or your operator's projects) first or special-cased.
  Alphabetical, like everything else.
- Rewriting existing entries or rewording others' descriptions in the same PR.

## When you are unsure

If a project's OpAMP support is unclear (client vs server vs both, or
proprietary-vs-standard), say so in the PR description rather than guessing.
A human will verify. Do not merge anything — you cannot; this repo requires
human review anyway.
