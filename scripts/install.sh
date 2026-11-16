#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Yuming Fu
# SPDX-License-Identifier: MIT
#
# Install NiceDocs skills into an AI coding tool's skills folder.
# Usage: scripts/install.sh <target> [--link] [--project [DIR]] [--uninstall] [--dry-run]

set -euo pipefail

MARKER=".nicedocs-installed"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"

usage() {
  cat <<'EOF'
Install NiceDocs skills into an AI coding tool's skills folder.

Usage:
  scripts/install.sh <target> [options]

Targets (user-level folder | project-level folder with --project):
  opencode   ~/.config/opencode/skills   | .opencode/skills
  agents     ~/.agents/skills            | .agents/skills   (Codex and other Agent Skills tools)
  codex      alias of "agents"
  claude     ~/.claude/skills            | .claude/skills
  cursor     ~/.cursor/skills            | .cursor/skills
  copilot    ~/.copilot/skills           | .github/skills
  gemini     ~/.gemini/skills            | .gemini/skills

Options:
  --link            Symlink skills instead of copying (updates with `git pull`)
  --project [DIR]   Install into a project folder (default: current directory)
  --uninstall       Remove NiceDocs skills from the target folder
  --dry-run         Print what would happen without changing anything
  -h, --help        Show this help

Tip: Claude Code, Codex, and Gemini CLI can also install NiceDocs as a plugin or
extension. See README.md.
EOF
}

die() { echo "error: $*" >&2; exit 1; }

target=""
mode="copy"
scope="user"
project_dir=""
action="install"
dry_run=0

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    --link) mode="link" ;;
    --uninstall) action="uninstall" ;;
    --dry-run) dry_run=1 ;;
    --project)
      scope="project"
      if [ $# -gt 1 ] && [ "${2#-}" = "$2" ]; then project_dir="$2"; shift; fi
      ;;
    -*) die "unknown option: $1 (see --help)" ;;
    *)
      [ -z "$target" ] || die "only one target allowed (got '$target' and '$1')"
      target="$1"
      ;;
  esac
  shift
done

[ -n "$target" ] || { usage; exit 1; }
[ -d "$SKILLS_SRC" ] || die "skills folder not found at $SKILLS_SRC"

if [ "$scope" = "project" ]; then
  base="$(cd "${project_dir:-.}" 2>/dev/null && pwd)" || die "project folder not found: ${project_dir:-.}"
fi

case "$target" in
  opencode) user_dir="$HOME/.config/opencode/skills"; proj_rel=".opencode/skills" ;;
  agents|codex) user_dir="$HOME/.agents/skills"; proj_rel=".agents/skills" ;;
  claude) user_dir="$HOME/.claude/skills"; proj_rel=".claude/skills" ;;
  cursor) user_dir="$HOME/.cursor/skills"; proj_rel=".cursor/skills" ;;
  copilot) user_dir="$HOME/.copilot/skills"; proj_rel=".github/skills" ;;
  gemini) user_dir="$HOME/.gemini/skills"; proj_rel=".gemini/skills" ;;
  *) die "unknown target: $target (see --help)" ;;
esac

if [ "$scope" = "project" ]; then dest="$base/$proj_rel"; else dest="$user_dir"; fi

run() {
  if [ "$dry_run" -eq 1 ]; then echo "[dry-run] $*"; else "$@"; fi
}

# A destination entry belongs to NiceDocs if it is a symlink into our skills folder
# or a copied folder carrying our marker file.
is_ours() {
  local path="$1"
  if [ -L "$path" ]; then
    case "$(readlink "$path")" in "$SKILLS_SRC"/*) return 0 ;; esac
    return 1
  fi
  [ -f "$path/$MARKER" ]
}

installed=0
skipped=0
removed=0

[ "$action" = "install" ] && run mkdir -p "$dest"

for src in "$SKILLS_SRC"/*/; do
  src="${src%/}"
  name="$(basename "$src")"
  [ -f "$src/SKILL.md" ] || continue
  out="$dest/$name"

  if [ "$action" = "uninstall" ]; then
    if [ -e "$out" ] || [ -L "$out" ]; then
      if is_ours "$out"; then
        run rm -rf "$out"; removed=$((removed + 1)); echo "removed  $out"
      else
        echo "skipped  $out (not installed by NiceDocs)"; skipped=$((skipped + 1))
      fi
    fi
    continue
  fi

  if [ -e "$out" ] || [ -L "$out" ]; then
    if is_ours "$out"; then
      run rm -rf "$out"
    else
      echo "skipped  $out (exists and was not installed by NiceDocs; remove it to install)" >&2
      skipped=$((skipped + 1))
      continue
    fi
  fi

  if [ "$mode" = "link" ]; then
    run ln -s "$src" "$out"
  else
    run cp -R "$src" "$out"
    if [ "$dry_run" -eq 1 ]; then
      echo "[dry-run] write $out/$MARKER"
    else
      printf 'Installed by NiceDocs (https://github.com/rudolffu/nicedocs) from %s\n' "$REPO_ROOT" > "$out/$MARKER"
    fi
  fi
  installed=$((installed + 1))
  echo "$( [ "$mode" = link ] && echo linked || echo copied )   $out"
done

note=""
[ "$skipped" -eq 0 ] || note=", skipped $skipped"
if [ "$action" = "uninstall" ]; then
  echo "Done: removed $removed skill(s) from $dest$note."
else
  echo "Done: installed $installed skill(s) into $dest$note."
  if [ "$installed" -gt 0 ]; then
    echo "Restart $target (or start a new session) to load the skills."
  fi
fi

[ "$skipped" -eq 0 ] || exit 2
