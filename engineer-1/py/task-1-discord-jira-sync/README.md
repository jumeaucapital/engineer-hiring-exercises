# A backend exercise: Discord → JIRA sync bot

A small exercise in backend engineering and API integration.
The goal is to see how well you can read a spec, integrate two external services, write clean Python, and back it up with tests.

**Time budget: ~2 days.** If you find yourself in scope creep, stop and write down what you cut.

## How we want you to work (read this first)

The problem is **intentionally ambiguous and underspecified**. We grade your process and communication as much as your code.

- **Ask, don't assume.** Questions are never penalized; silent assumptions are. If we are slow to reply, note your assumption, proceed, and flag it.
- **Plan first.** Within your first few hours, send us your understanding, open questions, assumptions, scope cuts and a proposed design before writing significant code.
- **Be deliberate.** For each key design choice, write down what you chose, why, and what you traded off.
- **Update daily.** Send a short update (done, next, blocked) at least once a day and push small commits. No silent days, no final code dump.

Contact: `tech@jumeaucapital.com`

## Expected Deliverables and Evaluation Criteria

- **Working prototype** that mirrors Discord activity into a JIRA Cloud instance.
- **Code quality**: clear module boundaries and readable, maintainable Python.
- **Tests**: meaningful unit tests covering the JIRA client and sync logic.
- **Communication**: frequent progress updates (commits and short notes), rather than a last-minute code dump.

**Many details have been intentionally omitted from the specification.**

A key part of this exercise is demonstrating how you approach an ambiguous problem. Before implementing a solution, you should:

1. Break the problem into manageable components.
2. Identify the technologies and services needed for each component.
3. Propose an overall system design.
4. Validate your assumptions and proposed scope with us before proceeding.

Planning, communication, and scope alignment are as important as the implementation itself.

---

## Problem statement

Consider a small engineering team that operates **Discord-first** and has no project manager. Work happens in Discord, but reporting is expected in JIRA, and nobody wants to double-write. Build a bot that bridges the two.

Assume the following Discord convention:

- Channels prefixed `proj-` are **project channels** (e.g. `proj-checkout`).
- **Threads** under a project channel are **milestones** of that project.
- Discord users map to JIRA accounts via a simple config file you decide the shape of.

Entity mapping the bot should maintain:

| Discord                          | JIRA                                |
|----------------------------------|-------------------------------------|
| `proj-<name>` channel            | JIRA project, key `<NAME>`          |
| Thread under a project channel   | JIRA issue (type: Story)            |
| Message in that thread           | Comment, optionally a status transition |

JIRA project creation is out of scope — if the project doesn't exist, the bot logs and skips.

### Supported actions (v1 — full list)

1. **Create issue.** New thread under a `proj-*` channel → create a Story in the matching JIRA project, with thread author as reporter.
2. **Comment.** New message in a milestone thread → comment on the linked issue, attributed to the message author.
3. **Transition.** Message in a milestone thread containing `status: <todo|in_progress|done|blocked>` → transition the linked issue. The comment is still recorded.
   Map `todo` → To Do, `in_progress` → In Progress, `done` → Done. Look up available transitions from JIRA rather than hardcoding ids. `blocked` has no equivalent in the default JIRA workflow: decide how to handle it (e.g. custom status, label, or reject) and flag your choice.

Anything not listed above (edits, deletes, renames, bot messages, etc.) is out of scope for v1 unless you propose it and we agree.

### Constraints

- **JIRA Cloud.** Set up your own free Atlassian sandbox.
- **No duplicates.** If the bot sees the same Discord message twice (e.g. on restart), it should not create a duplicate JIRA comment or issue. Keep a small local record of what you've already synced — SQLite is fine.
- **Include tests.** Use `pytest`. At minimum, the JIRA client and the message-parsing logic should be unit tested with mocks (no real network in tests).

---

## Part A — JIRA client

Build a thin Python wrapper around the JIRA Cloud REST API for the operations the bot needs (lookup, create issue, comment, transition). Design the interface and document it briefly in the README.

## Part B — Discord bot

Build the Discord side using `discord.py` or `py-cord`. The bot should listen for new threads under `proj-*` channels and new messages inside those threads, and call the sync logic for each event.


## Part C — Run locally

A reviewer should be able to clone your repo, follow the README, set their env vars (Discord token, JIRA credentials), and run the bot locally with a single command (e.g. `python -m bot` or `make run`).

---

## Acceptance criteria

A reviewer should be able to:

1. Follow the README, set env vars, and start the bot locally.
2. Create a thread under a `proj-*` channel in their test Discord server and see the corresponding Story appear in their JIRA sandbox.
3. Post `wrapping this up, status: done` in that thread and see the issue transition to `Done` with the message as a comment.
4. Stop the bot, post a couple of messages, restart, and see no duplicate JIRA mutations for messages the bot had already processed.
5. Run `pytest` and see it pass.

---

## Repository requirements

- Do not fork. Work on a private repo and add collaborator: `tech@jumeaucapital.com`.
- Use **Python**. SQLite is fine for local state.
- Keep `README.md` updated with reproducible instructions.
- Commits should reflect incremental progress — we read the history.

### Submit your AI prompts

We want to see **how you worked with AI tools**, not just the final code. Commit your prompts and chat logs to your repo in a top-level `prompts/` folder.

1. **Create `prompts/`** in the repo root. Put one file per session or tool, named by date/tool, e.g. `prompts/2026-01-15-claude-code.jsonl`.
2. **Export your chats** using the steps for your tool:
   - **Claude Code (automatic if you work inside a clone of this repo)**: hooks in `.claude/settings.json` copy every session into `prompts/claude-code/` (secrets redacted) as you work. Run `/sync-prompts` at the end to catch anything missed. If you work in a different repo, copy this repo's `.claude/` and `scripts/` folders into it. Manual fallback: your transcripts are saved on your machine (not in the repo), under `~/.claude/projects/<your-project-path>/*.jsonl`. Copy those files into `prompts/`. Committing the project's `.claude/` folder is *not* enough, as it holds settings, not your conversations. Alternatively, run `/export` inside a session and save the output to `prompts/`.
   - **Cursor**: open the chat panel, use the chat's `...` menu → **Export Chat** (saves Markdown), and save it into `prompts/`. Cursor has no built-in bulk export; export each important chat.
   - **VS Code (Copilot Chat)**: run **Chat: Export Chat...** from the Command Palette and save the JSON into `prompts/`.
   - **Any other tool (ChatGPT, Gemini, etc.)**: use its export/share feature, or copy-paste the conversation into a `.md` file in `prompts/`.
3. **Remove secrets** before committing: search the files for API keys, tokens and passwords, and redact them.
4. **Commit and push** `prompts/` along with your code, then mention it in your README. Include **all** sessions, including dead ends and ones you abandoned. We evaluate how you prompt, iterate and recover, not how polished the prompts look.
5. If you wrote prompts by hand that no tool logged, add them to `prompts/notes.md`.

---

**All the best!**
