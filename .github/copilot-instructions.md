# Repository AI / Copilot Guidance

This file contains concise, project-specific instructions for AI coding agents working in this repository. It synthesizes authoritative patterns discovered in `CLAUDE.md`, `.claude/commands/*`, and the Spec-Kit templates under `.specify`.

- **Primary responsibilities:** Use Spec-Kit tools and templates (`.specify/*`) for specs, plans, tasks, and PHRs. Prefer agent-native PHR creation; fallback to the shell scripts only when required.
- **Key files to consult:** `CLAUDE.md`, `prompt.md`, `hackathone.md`, `.claude/commands/`, and any templates under `.specify/templates/`.

- **Prompt History Records (PHR):** Always create a PHR after implementation or planning work. Route files under `history/prompts/` using the stage taxonomy:
  - `constitution` → `history/prompts/constitution/`
  - feature stages (spec, plan, tasks, red, green, refactor, explainer, misc) → `history/prompts/<feature-name>/`
  - general → `history/prompts/general/`

- **PHR creation (agent-native preferred):** Read `.specify/templates/phr-template.prompt.md` (or `templates/phr-template.prompt.md`), fill fields (ID, TITLE, STAGE, DATE_ISO, SURFACE="agent", MODEL, BRANCH, USER, COMMAND, FILES_YAML, TESTS_YAML, PROMPT_TEXT verbatim, RESPONSE_TEXT), then write under the correct `history/prompts/` path. If template scripts exist but fail, use the shell fallback: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`.

- **ADR recommendations:** When an architectural decision is cross-cutting (framework, data model, security, API contract) suggest creating an ADR. Use the exact suggestion phrasing found in `CLAUDE.md`:
  - `📋 Architectural decision detected: <brief> — Document reasoning and tradeoffs? Run /sp.adr <decision-title>`
  - Do NOT create ADRs without user consent.

- **Git & PR policy (refer `.claude/commands/sp.git.commit_pr.md`):**
  - Validate repo state with: `git rev-parse --is-inside-work-tree`, `git status --porcelain`, `git diff --stat`, `git rev-parse --abbrev-ref HEAD`, `git remote -v`.
  - Only run Git commands during autonomous commit/PR flows. Avoid running build/test/long‑running commands unless explicitly requested.
  - Branch naming: descriptive, 2–4 words, follow existing patterns (examples: `docs-update-readme`, `feat/auth-validation`).
  - Commit message format: `<type>(<scope>): <subject>` (type: feat, fix, chore, docs, test, refactor). Include body explaining *why*.
  - PR creation: use `gh pr create` if available; otherwise provide a manual compare URL.

- **Execution constraints:**
  - Do not run servers, watchers, or long-running processes autonomously.
  - Do not run tests, builds, or other blocking commands unless the user explicitly asks and provides permission.
  - Do not create or expose secrets; use `.env` and documented config files.

- **Spec-Kit & agent commands observed in repo:** The project signals a Spec-Kit workflow (see `prompt.md`): `/sp.constitution`, `/sp.spec` (spec generation), `/sp.plan`, `/sp.tasks`, `/sp.implement`. When these commands appear in prompts, prefer to produce the corresponding `.specify/*` artifacts (`constitution.md`, `spec.md`, `plan.md`, `tasks.md`) and follow the templates.

- **Small-diff rule:** Always prefer the smallest viable change to satisfy the request. Avoid refactoring unrelated files.

- **Where to place outputs / examples:**
  - Specs/plans/tasks → `specs/<feature>/` (use repo template conventions)
  - ADRs → `history/adr/`
  - PHRs → `history/prompts/`

- **Quick examples:**
  - Create PHR (agent-native): Fill `templates/phr-template.prompt.md` and write to `history/prompts/<route>/<ID>-<slug>.<stage>.prompt.md`.
  - Commit & PR (autonomous git agent): `git add . ; git commit -m "feat(spec): add plan for X" ; git push -u origin <branch> ; gh pr create --title "feat(spec): add plan for X" --body "..."`

If anything in this guidance is unclear or you'd like me to include additional examples (e.g., exact PHR frontmatter template or a preferred commit message generator), tell me which section to expand and I will update this file.
