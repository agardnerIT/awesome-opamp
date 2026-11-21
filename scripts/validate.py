# scripts/validate.py — structural checks for awesome-opamp
#
# Run before committing:  python3 scripts/validate.py
# CI runs this on every PR. Exit code 0 = pass.
#
# Checks (all entries in list sections of README.md):
#   1. Entry format:      - [Name](https-url) - Description ending with a period.
#   2. Alphabetical:      entries sorted case-insensitively by name (ties by URL).
#   3. Unique names:      no duplicate project names within a section.
#   4. Placeholders:      "_Nothing here yet_" must not coexist with entries.
#   5. No leftovers:      no "Example" entries or example.com/example.org links.
#   6. Table of contents: every TOC link resolves to a heading (and vice versa).

import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

ENTRY_RE = re.compile(
    r"^- \[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\) - (?P<desc>\S.*?)$"
)
HEADING_RE = re.compile(r"^(?P<level>#{2,3}) (?P<text>.+?)$", re.M)
TOC_RE = re.compile(r"^\s*-\s+\[(?P<text>[^\]]+)\]\(#(?P<anchor>[^)]+)\)", re.M)


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def errors_for(entries, section, errors):
    # 1. Format (non-matching bullets already reported by caller)
    # 2. Alphabetical
    keys = [(e["name"].lower(), e["url"].lower()) for e in entries]
    if keys != sorted(keys):
        names = [e["name"] for e in entries]
        expected = [
            n
            for _, n in sorted(
                zip(keys, names), key=lambda t: t[0]
            )
        ]
        errors.append(
            f"{section}: entries not alphabetical. "
            f"Expected order: {', '.join(expected)}"
        )
    # 3. Duplicates
    seen = set()
    for e in entries:
        key = e["name"].lower()
        if key in seen:
            errors.append(f"{section}: duplicate entry '{e['name']}'")
        seen.add(key)


def main() -> int:
    text = README.read_text(encoding="utf-8")
    errors: list[str] = []

    # Example entries live inside HTML comments — strip them before parsing.
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)

    # TOC entries are only required for real content sections.
    toc_exempt = {"contents", "contributing", "license"}

    headings = [(m.group("text"), len(m.group("level"))) for m in HEADING_RE.finditer(text)]

    # Parse list sections: any ## / ### heading followed by content until next heading.
    parts = re.split(r"^(?=#{2,3} )", text, flags=re.M)[1:]
    for part in parts:
        heading_line, _, body = part.partition("\n")
        section = heading_line.lstrip("#").strip()

        if section.lower() == "contents":  # the TOC is a nav list, not entries
            continue

        entries = []
        for line in body.splitlines():
            stripped = line.strip()
            if not stripped.startswith("- ["):
                continue
            m = ENTRY_RE.match(stripped)
            if not m:
                errors.append(f"{section}: bad entry format: {stripped!r}")
                continue
            if not m.group("desc").rstrip().endswith("."):
                errors.append(f"{section}: description must end with a period: {m.group('name')}")
            entries.append(m.groupdict())

        if entries:
            errors_for(entries, section, errors)
            if "_Nothing here yet_" in body:
                errors.append(f"{section}: placeholder text still present alongside entries")
            for e in entries:
                if "example.com" in e["url"] or "example.org" in e["url"]:
                    errors.append(f"{section}: placeholder URL in entry '{e['name']}'")
                if e["name"].lower().startswith("example"):
                    errors.append(f"{section}: placeholder name in entry '{e['name']}'")

    # 6. TOC ↔ headings
    toc_links = TOC_RE.findall(text)
    heading_anchors = {slugify(h) for h, _ in headings}
    for label, anchor in toc_links:
        if anchor not in heading_anchors:
            errors.append(f"TOC: link #{anchor} ({label}) does not match any heading")
    for h, level in headings:
        if level == 2 and h.lower() not in toc_exempt and slugify(h) not in {a for _, a in toc_links}:
            errors.append(f"TOC: missing entry for section '{h}'")

    if errors:
        print(f"validate: {len(errors)} error(s) in README.md")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate: README.md OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
