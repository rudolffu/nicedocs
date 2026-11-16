#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Yuming Fu
# SPDX-License-Identifier: MIT
"""Validate the NiceDocs repository (standard library only).

Checks:
  1. Every skills/<name>/SKILL.md follows the Agent Skills spec (frontmatter name and
     description, name equal to the folder name, under 500 lines).
  2. All plugin manifests parse as JSON and agree on name and version.
  3. Every skills/*/references/*.md ends with a Write the Docs attribution footer that
     cites the pinned commit.
  4. Relative Markdown links resolve (templates under assets/ are skipped).

Exit code 0 means everything passed.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WTD_SHA = "c37669d0c87740b1455821cbee7fc10c8ee6cf7f"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE_RE = re.compile(r"^(```|~~~)")

MANIFESTS = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    "gemini-extension.json",
]

errors: list[str] = []


def err(path: Path | str, msg: str) -> None:
    rel = path.relative_to(ROOT) if isinstance(path, Path) else path
    errors.append(f"{rel}: {msg}")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse the top-level scalar keys of a simple YAML frontmatter block."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        key, sep, value = line.partition(":")
        if sep:
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_skills() -> list[str]:
    names = []
    skills_dir = ROOT / "skills"
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            err(skill_dir, "missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            err(skill_md, "missing or malformed YAML frontmatter")
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if not NAME_RE.match(name) or len(name) > 64:
            err(skill_md, f"invalid name {name!r} (lowercase, digits, single hyphens, <=64 chars)")
        if name != skill_dir.name:
            err(skill_md, f"name {name!r} does not match folder {skill_dir.name!r}")
        if not 1 <= len(desc) <= 1024:
            err(skill_md, f"description must be 1-1024 characters (got {len(desc)})")
        if "license" not in fm:
            err(skill_md, "missing license field")
        lines = text.count("\n") + 1
        if lines >= 500:
            err(skill_md, f"SKILL.md has {lines} lines; keep it under 500")
        names.append(name)
    if not names:
        err("skills/", "no skills found")
    return names


def check_manifests() -> None:
    seen: dict[str, tuple[str, str | None]] = {}
    for rel in MANIFESTS:
        path = ROOT / rel
        if not path.is_file():
            err(rel, "manifest missing")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            err(rel, f"invalid JSON: {exc}")
            continue
        if rel.endswith("marketplace.json"):
            entries = [p for p in data.get("plugins", []) if p.get("name") == "nicedocs"]
            if not entries:
                err(rel, "no plugin entry named 'nicedocs'")
                continue
            seen[rel] = ("nicedocs", entries[0].get("version"))
        else:
            seen[rel] = (data.get("name"), data.get("version"))

    names = {n for n, _ in seen.values()}
    versions = {v for _, v in seen.values() if v is not None}
    if len(names) > 1:
        err("manifests", f"plugin names disagree: {sorted(map(str, names))}")
    if len(versions) > 1:
        detail = ", ".join(f"{k}={v}" for k, (_, v) in seen.items() if v)
        err("manifests", f"versions disagree: {detail}")


def check_attribution() -> None:
    for ref in sorted(ROOT.glob("skills/*/references/*.md")):
        tail = ref.read_text(encoding="utf-8").rstrip()[-1500:]
        for needle in ("Adapted from", "CC BY-NC-SA 4.0", f"writethedocs/www/blob/{WTD_SHA}"):
            if needle not in tail:
                err(ref, f"attribution footer missing {needle!r}")


def strip_code(text: str) -> str:
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line.lstrip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(re.sub(r"`[^`]*`", "", line))
    return "\n".join(out)


def check_links() -> None:
    for md in sorted(ROOT.rglob("*.md")):
        rel_parts = md.relative_to(ROOT).parts
        if ".git" in rel_parts or "assets" in rel_parts:
            continue
        for target in LINK_RE.findall(strip_code(md.read_text(encoding="utf-8"))):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path_part = target.split("#", 1)[0]
            if path_part and not (md.parent / path_part).exists():
                err(md, f"broken relative link: {target}")


def main() -> int:
    names = check_skills()
    check_manifests()
    check_attribution()
    check_links()
    if errors:
        print(f"validate: {len(errors)} problem(s) found\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"validate: OK ({len(names)} skills: {', '.join(names)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
