# An exercise in data analysis

This is a small exercise in the kinds of skills that may be required of you.  
The goal here is to evaluate how well you understand the problem, scope it, come up with a strategy to solve it, and execute it.  
More formally, we will look for the following in our evaluation:

## How we want you to work (read this first)

The problem is **intentionally ambiguous and underspecified**. We grade your process and communication as much as your code.

- **Ask, don't assume.** Questions are never penalized; silent assumptions are. If we are slow to reply, note your assumption, proceed, and flag it.
- **Plan first.** Within your first few hours, send us your understanding, open questions, assumptions, scope cuts and a proposed design before writing significant code.
- **Be deliberate.** For each key design choice, write down what you chose, why, and what you traded off.
- **Update daily.** Send a short update (done, next, blocked) at least once a day and push small commits. No silent days, no final code dump.

Contact: `tech@jumeaucapital.com`

## Expected deliverables and evaluation criteria
- Have a working prototype of the task described below. It is fine if your prototype's performance does not match the quality you may have in mind. We value a prototype showcasing all the required tasks moderately well over a prototype which solves just a few of the required tasks very well.
- (We will) assess how well you scope and assess the different components involved which will solve this problem
- Assess how you divide your labor into the components you identify, and how quickly you're able to prototype and finish implementing those components. Remember, there's a time budget of a few days.
- Assess your attention to little details. This is important for us--how much you care for details shows us how much you can own any work assigned to you.
- Assess how you resolve situations when you're stuck.
- Assess how well you communicate and let all stakeholders know of your progress. We emphasize constant communication over receiving no communication for days, and just seeing a dump of the results on the day of your submission. This has multiple drawbacks: (1) it gives us no insight into the process you employ to evaluate a problem and come up with a solution. (2) it gives us no room to help you in case you're stuck on any step. Consider this to be a task you will receive on your job - demonstrate to us how you will work on the task in such a setting.

## Task
The aim is to build a small dashboard which will give us a sense for the kinds of discussions happening in a city around a specific topic.
The use-case we will explore is specifically that of a political organization getting a sense for what people are discussing.

## Task 1 - Gather data
Write a function to list out the hot topics that are currently in the news in a city.  
The inputs to this task will be the name of the city.  
Find relevant sources you may want to pull this information from. List out the sources. They could be a few, limited, and popular set of sources. For example, any one news channel.  
Have a script which displays the top 5 topics currently in the news for a given city.

## Task 2 - Gather relevant discussions
For each of the topics found out in task 1, gather current discussions happening on public forums.  
For the purpose of this task, let your information sources be 
- Facebook 
- Twitter 
- Reddit

For each of these three sources, you can decide any two public groups and gather information from it.
Note:  
For each source, there could be multiple discussions that you gather.  
Also, for each discussion, there could be multiple comments that offer diverse views on the topic.

## Task 3 - Analyze gathered information
For the discussions that you gather in Task 2, summarize what is being discussed in each discussion.  
What can you analyze about this information? 
- Remember, each discussion can comprise multiple comments. Each comment can offer a diverse and different viewpoint on the topic. How can we get a sense for all the unique viewpoints expressed?  
- Of the diverse views being discussed, are there some that are positive, and some that are negative? Can you identify those?
- What is the best way to present this information?
- How will you ensure the different viewpoints for a given post that you gather are accurate? How can you ensure you can rely on the generated descriptions of the viewpoints.

For example, if a post on topic XYZ has 10 total comments - of which 4 are in favor of it, 3 are against it, and 3 are neutral.  
Of the 4 that are in favor, three of them express support using argument A, while the other comment uses a totally different and unique argument B. Similarly, of the 3 that are against the topic, two comments use a similar argument C, while the third comment uses a different argument D. How can your system summarize all this information?

Hint: Use an LLM to gather these insights.

## Task 4 - Build a small front-end to display your analyzed information
Build out a very simple front-end where a user can look at your results and analysis on a webpage.
The webpage should have a form which accepts the city name, and preferably shows drop-downs for each of the sources you selected in Task 1 and 2.  
Given these inputs, show the results from Task 3.

## Task 5 - Extend to states (no implementation; just a thought experiment)
Think about how you would extend your software to have the same dashboard, but for an entire state (which consists of multiple cities). This should be in addition to the city-level information you report.  
How would you design the backend? What changes will you make to your code.  
You do not have to implement this change -- we will discuss this on a call.

## Instructions to submit your work
- Do not fork this repo. Work on a local copy. Add `tech@jumeaucapital.com` as a collaborator to the repo. Keep the repo private.
- Once you have created the repo, please share a link to the repo, and mention that you've gotten started with the task. Ensure that you reply-to-all when responding to emails on the thread.
- Make it a habit to push changes upstream to your repo as frequently as feasible.
- Use `Python` for this work.
- We greatly value reproducability of results. Use `conda` to create an environment and set up your repository. 
- Use a `.gitignore` file to ensure you are not adding junk files to the repo.
- Have a `./src/` folder containing the source.
- Have a `./env/` folder containing the Conda environment file you create for this project.
- Have a `./data/` folder containing all the data your source accesses.
- Have a `./tests/` folder to write out unit tests for key functions. Look up the `unittest` package in Python if you haven't used it before. Also, not every function you write needs to be tested---exercise your judgement and prioritize which function you want tested.
- Keep updating this README with instructions which will help with the reproducability of your work/results.  
- The topmost section of your readme file should be titled `Approach`. In this section, concisely describe the overeall approach you considered to solve this problem. Describe the general strategy you used, the key tools you considered, the different metrics you considered to evaluate your work, and any other detail relevant to the task goals and the evaluation criteria mentioned above.

Focus on getting the core functionality right first, and have a working prototype of your solution.  
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

All the best!
