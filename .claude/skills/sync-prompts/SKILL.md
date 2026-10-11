---
name: sync-prompts
description: Copy this repo's AI chat logs into prompts/ for submission. Use when the user asks to sync, export, or submit their prompts, or before they finish and push their work.
---

Claude Code sessions in this repo are already copied to `prompts/claude-code/` automatically by hooks in `.claude/settings.json` (secrets redacted).

1. Run `python3 scripts/sync_prompts.py --all` to copy every session, including ones from before the hooks were active.
2. List `prompts/` and tell the user what was synced.
3. Remind them: skim the files for anything sensitive, then `git add prompts && git commit && git push`. Do not commit or push for them unless asked.
4. If they also used Cursor, VS Code Copilot or another tool in this repo, those are NOT captured automatically. Tell them to export those chats into `prompts/` manually (see "Submit your AI prompts" in the task README).
