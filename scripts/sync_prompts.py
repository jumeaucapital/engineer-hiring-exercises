#!/usr/bin/env python3
"""Copy Claude Code transcripts into ./prompts/claude-code/ (secrets redacted).

Usage:
  sync_prompts.py --hook   # called by Claude Code hooks; reads JSON on stdin
  sync_prompts.py --all    # copy every transcript Claude Code has for this repo

Standard library only. Never commits or pushes; you do that.
"""
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "prompts" / "claude-code"

# Best-effort redaction. Still skim prompts/ before you push.
SECRETS = [
    re.compile(r"sk-[A-Za-z0-9_\-]{16,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
    re.compile(r"(?i)(bearer\s+)[A-Za-z0-9._\-]{16,}"),
    re.compile(r"(?i)((?:api[_-]?key|secret|token|password)[\"']?\s*[:=]\s*[\"']?)[^\s\"',}]{8,}"),
]


def redact(text: str) -> str:
    for pat in SECRETS:
        if pat.groups:
            text = pat.sub(lambda m: m.group(1) + "[REDACTED]", text)
        else:
            text = pat.sub("[REDACTED]", text)
    return text


def copy_one(src: Path) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / src.name
    dest.write_text(redact(src.read_text(errors="replace")))
    print(f"synced {src.name} -> {dest.relative_to(REPO)}")


def project_dir() -> Path:
    # Claude Code stores transcripts under ~/.claude/projects/<path with / and . as ->
    encoded = re.sub(r"[/.]", "-", str(REPO))
    return Path.home() / ".claude" / "projects" / encoded


def main() -> int:
    if "--hook" in sys.argv:
        try:
            src = Path(json.load(sys.stdin)["transcript_path"])
        except Exception:
            return 0  # never break the session
        if src.is_file():
            copy_one(src)
        return 0
    if "--all" in sys.argv:
        files = sorted(project_dir().glob("*.jsonl"))
        if not files:
            print(f"no transcripts found in {project_dir()}")
            return 1
        for f in files:
            copy_one(f)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
