# A backend + data exercise: WhatsApp-group chatbot

This is a small exercise in backend engineering and data systems design.  
The goal is to evaluate how well you understand a fuzzy product requirement, scope it, design a robust system, prototype the core, and communicate tradeoffs clearly.

## How we want you to work (read this first)

The problem is **intentionally ambiguous and underspecified**. We grade your process and communication as much as your code.

- **Ask, don't assume.** Questions are never penalized; silent assumptions are. If we are slow to reply, note your assumption, proceed, and flag it.
- **Plan first.** Within your first few hours, send us your understanding, open questions, assumptions, scope cuts and a proposed design before writing significant code.
- **Be deliberate.** For each key design choice, write down what you chose, why, and what you traded off.
- **Update daily.** Send a short update (done, next, blocked) at least once a day and push small commits. No silent days, no final code dump.

Contact: `tech@jumeaucapital.com`

## Expected deliverables and evaluation criteria
- **Working prototype** that demonstrates the end-to-end flow (ingest → decide to respond → generate → reply).
- **System design quality**: architecture, data modeling.
- **Data thinking**: context retrieval strategy, storage, indexing, evaluation, and observability for model outputs.
- **Communication cadence**: frequent progress updates (PRs/commits + short notes) over a last-day dump.
- **Attention to details**: edge cases,testability.

---

## Problem statement
Design a chatbot that can be **added to WhatsApp groups** (or a realistic workaround) such that:

- People can **mention** the bot (e.g., `@bot`) in a WhatsApp group.
- The bot **answers questions** when mentioned.
- The bot uses **group context** (recent messages, prior bot answers, group “memory”) to respond.
- The bot can **browse/surf the internet** (via a search API + page fetch) when needed, and cite sources.

### Constraints / reality check (intentional)
It might not be possible (or straightforward) to add a bot to a WhatsApp group using official means in your setup. You must propose a **workable integration plan**. 

### Reference implementation (optional)
You **may** use `clawdbot` as a starting point/reference to speed up integration work:  
https://github.com/clawdbot/clawdbot  

However, you are **not required** to use it—you're free to evaluate and use other libraries. 

**Your job is to define a plan, list assumptions, and deliver a runnable prototype.**

---

# Task 1 — Requirements, assumptions, and scope

Create a doc with clear requirements, assumptions, and a minimal but realistic spec.

---

# Task 2 — Ingestion and WhatsApp integration adapter
Build a WhatsApp ingestion service that accepts real WhatsApp group past messages when added in a group, stores them with required fields, detects bot mentions to trigger replies.

---

# Task 3 — Data model for group context + retrieval
Implement a context store and retrieval layer.

---

# Task 4 — The answering pipeline (LLM + grounding + web browsing)
Implement an LLM-driven answering pipeline that routes mentioned queries, assembles group context, optionally performs web search + page fetch for grounding with citations, generates a safe response, and logs/stores prompts, sources, and outputs end-to-end.

### Prototype acceptance criteria
- Given a group conversation, when a user mentions the bot:
  - It responds with an answer grounded in group context
  - If it browses, it includes citations and stores the sources used

---

# Task 5 — Evaluation: prove your bot is not making things up
We care about correctness and trust.

Implement a lightweight evaluation harness:
- A small dataset of 15–30 test prompts (some require browsing, some require group context, some should be refused/clarified).

---

## Repository requirements
- Do not fork. Work on a private repo and add collaborator: `tech@jumeaucapital.com`.
- Use **Node.js (TypeScript)**.
- Add `.gitignore`.
- Keep `README.md` updated with reproducible instructions.

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
