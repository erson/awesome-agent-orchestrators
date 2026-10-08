# Awesome Agent Orchestrators: a metrics index

An index of open-source and source-available tools for orchestrating AI agents. Every project has live GitHub metrics: stars, contributors, commit activity, releases, open work, license, and how recently it was updated.

It starts from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) (CC0-1.0) and adds projects that list does not cover. Figures are a snapshot; see [Methodology](#methodology).

**Metrics collected 2026-10-08 (UTC)** · 256 from the source list · 232 new · 15 adjacent frameworks · refresh with `python3 scripts/update.py`

## At a glance

| Metric | Value |
|---|--:|
| Projects tracked | 503 |
| Total stars | 3,236,695 |
| Median contributors per project | 7 |
| Median days since last commit | 3 |
| Status: Active | 339 |
| Status: Recent | 57 |
| Status: Slow | 101 |
| Status: Stale | 2 |
| Status: Archived | 3 |
| Status: Unavailable | 1 |
| Status: Not fetched | 0 |

### Categories

| Category | Projects | Total stars | Active or recent | Stale or archived |
|---|--:|--:|--:|--:|
| [Terminal](#parallel-coding-agents--terminal-tuicli) | 48 | 110,710 | 40 | 0 |
| [Desktop & web](#parallel-coding-agents--desktop--web) | 132 | 412,489 | 113 | 1 |
| [Swarms](#multi-agent-swarms) | 94 | 535,910 | 66 | 0 |
| [Loop runners](#autonomous-loop-runners) | 30 | 62,756 | 20 | 0 |
| [Task runners](#autonomous-task-runners) | 52 | 231,286 | 42 | 1 |
| [Infrastructure](#agent-infrastructure--primitives) | 59 | 215,016 | 53 | 0 |
| [Assistants](#personal-assistants) | 44 | 1,004,271 | 38 | 0 |
| [Resting](#resting) | 16 | 47,343 | 1 | 3 |
| [Adjacent frameworks](#adjacent-frameworks-general-purpose-agent-sdks) | 28 | 616,914 | 23 | 0 |

### Top 15 by stars

| # | Project | Category | Stars | Contributors | Status |
|--:|---|---|--:|--:|---|
| 1 | [openclaw](https://github.com/openclaw/openclaw) | Assistants | 391,468 | 369 | Active |
| 2 | [hermes-agent](https://github.com/NousResearch/hermes-agent) | Assistants | 252,012 | 398 | Active |
| 3 | [paperclip](https://github.com/paperclipai/paperclip) | Swarms | 98,800 | 202 | Active |
| 4 | [OpenHands](https://github.com/OpenHands/OpenHands) | Task runners | 90,295 | 458 | Active |
| 5 | [Orca](https://github.com/stablyai/orca) | Desktop & web | 87,869 | 421 | Active |
| 6 | [DeerFlow](https://github.com/bytedance/deer-flow) _(new)_ | Adjacent frameworks | 83,528 | 451 | Active |
| 7 | [ruflo](https://github.com/ruvnet/ruflo) | Swarms | 74,138 | 38 | Active |
| 8 | [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Adjacent frameworks | 70,779 | 116 | Slow |
| 9 | [OmO](https://github.com/code-yeongyu/oh-my-openagent) _(new)_ | Swarms | 69,897 | 321 | Active |
| 10 | [AutoGen](https://github.com/microsoft/autogen) | Adjacent frameworks | 61,312 | 440 | Slow |
| 11 | [crewAI](https://github.com/crewAIInc/crewAI) | Swarms | 59,469 | 337 | Active |
| 12 | [multica](https://github.com/multica-ai/multica) | Task runners | 52,198 | 327 | Active |
| 13 | [nanobot](https://github.com/HKUDS/nanobot) | Assistants | 48,875 | 387 | Active |
| 14 | [CowAgent](https://github.com/zhayujie/CowAgent) _(new)_ | Assistants | 47,285 | 151 | Active |
| 15 | [herdr](https://github.com/herdrdev/herdr) | Terminal | 42,957 | 87 | Active |

### Most recent commits

| # | Project | Category | Last commit | Commits (90d) | Status |
|--:|---|---|---|--:|---|
| 1 | [ADE](https://github.com/arul28/ADE) _(new)_ | Desktop & web | 2026-10-08 | 989 | Active |
| 2 | [Claude Octopus](https://github.com/nyldn/claude-octopus) _(new)_ | Swarms | 2026-10-08 | 349 | Active |
| 3 | [Orb](https://github.com/Th0rgal/orb) _(new)_ | Desktop & web | 2026-10-08 | 1,546 | Active |
| 4 | [Gas City](https://github.com/gastownhall/gascity) _(new)_ | Infrastructure | 2026-10-08 | 1,956 | Active |
| 5 | [MCP Agent Mail (Rust)](https://github.com/Dicklesworthstone/mcp_agent_mail_rust) _(new)_ | Infrastructure | 2026-10-08 | 2,057 | Active |
| 6 | [Hive](https://github.com/hivecommons/hive) _(new)_ | Task runners | 2026-10-08 | 6,485 | Active |
| 7 | [OmO](https://github.com/code-yeongyu/oh-my-openagent) _(new)_ | Swarms | 2026-10-08 | 10,056 | Active |
| 8 | [Google ADK](https://github.com/google/adk-python) | Adjacent frameworks | 2026-10-08 | 1,415 | Active |
| 9 | [Atomic](https://github.com/bastani-inc/atomic) _(new)_ | Loop runners | 2026-10-08 | 3,109 | Active |
| 10 | [Mastra](https://github.com/mastra-ai/mastra) | Adjacent frameworks | 2026-10-08 | 4,225 | Active |
| 11 | [Cezar](https://github.com/open-mercato/cezar) _(new)_ | Desktop & web | 2026-10-08 | 1,145 | Active |
| 12 | [hydra-acp](https://github.com/smagnuso/hydra-acp) _(new)_ | Terminal | 2026-10-08 | 532 | Active |
| 13 | [Agent Substrate](https://github.com/agent-substrate/substrate) _(new)_ | Infrastructure | 2026-10-08 | 912 | Active |
| 14 | [Pi Herdsman](https://github.com/boadij/pi-herdsman) _(new)_ | Swarms | 2026-10-08 | 253 | Active |
| 15 | [nodeterm](https://github.com/eneskirca/nodeterm) _(new)_ | Desktop & web | 2026-10-08 | 4,388 | Active |

### Single-maintainer risk

Projects where one person wrote nearly all human commits. Ten highest top-author shares among projects with at least 100 commits that are not archived.

| Project | Top author share | Contributors | Commits (all time, approx.) | Status |
|---|--:|--:|--:|---|
| [amux](https://github.com/andyrewlee/amux) | 100% | 1 | 1,046 | Active |
| [Calyx](https://github.com/yuuichieguchi/Calyx) | 100% | 1 | 880 | Active |
| [openkanban](https://github.com/TechDufus/openkanban) | 100% | 1 | 118 | Slow |
| [tmux-ide](https://github.com/wavyrai/tmux-ide) | 100% | 1 | 2,707 | Active |
| [AI4Kanban](https://github.com/ai4kanban/ai4kanban) | 100% | 1 | 1,026 | Active |
| [ateam](https://github.com/clawnify/ateam) | 100% | 1 | 298 | Active |
| [Dray](https://github.com/monorepo-labs/dray) | 100% | 1 | 645 | Active |
| [Pragma](https://github.com/pragma-sh/pragma) | 100% | 1 | 1,252 | Active |
| [Superagent](https://github.com/pungme/superagent-desktop) | 100% | 1 | 949 | Active |
| [tlbx](https://github.com/tlbx-ai/tlbx) | 100% | 2 | 3,725 | Active |

## Parallel Coding Agents — Terminal (TUI/CLI)

Run and supervise several agent sessions side by side from a terminal — tmux panes, git worktrees, and TUI dashboards.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [herdr](https://github.com/herdrdev/herdr) | Rust background runtime that owns agent terminals so sessions survive reboot and reattach. | 42,957 | 87 | 3,365 | 752 | 2026-10-08 | Active | v0.9.3 (2026-09-29) | 300 / 13 | Apache-2.0 |
| [cmux](https://github.com/manaflow-ai/cmux) | Ghostty-based macOS terminal with vertical tabs and per-agent notifications for many concurrent sessions. | 28,025 | 221 | 2,471 | 13,391 | 2026-10-08 | Active | cmux-app-ffi-eee4e4fffe22964457034c3fd2a8fb22388dec2b (2026-10-08) | 1,655 / 1,520 | Other |
| [claude-squad](https://github.com/smtg-ai/claude-squad) | Runs Claude Code, Codex, and others as detached background sessions in separate worktrees. | 8,581 | 19 | 626 | 3 | 2026-08-20 | Recent | v1.0.20 (2026-08-20) | 16 / 36 | AGPL-3.0 |
| [TUIOS](https://github.com/Gaurav-Gosain/tuios) _(new)_ | Terminal multiplexer whose panes run coding agents that report state and message each other. | 5,046 | 35 | 227 | 3,256 | 2026-10-08 | Active | v0.9.1 (2026-10-08) | 12 / 16 | MIT |
| [abtop](https://github.com/graykode/abtop) _(new)_ | Terminal monitor listing Claude Code, Codex and OpenCode sessions with tokens, context and ports. | 3,708 | 27 | 332 | 16 | 2026-09-14 | Active | v0.5.5 (2026-09-14) | 21 / 10 | MIT |
| [Toad](https://github.com/batrachianai/toad) _(new)_ | Terminal UI that runs multiple coding agents concurrently through the Agent Client Protocol. | 3,469 | 15 | 158 | 0 | 2026-05-26 | Slow | v0.6.20 (2026-05-26) | 4 / 3 | AGPL-3.0 |
| [agent-of-empires](https://github.com/agent-of-empires/agent-of-empires) | TUI paired with a web view so agent sessions stay reachable from a phone. | 3,327 | 118 | 373 | 926 | 2026-10-08 | Active | v1.19.0 (2026-10-08) | 124 / 23 | MIT |
| [dmux](https://github.com/standardagents/dmux) | Dev agent multiplexer that pairs coding agents with git worktrees over tmux. | 1,796 | 16 | 138 | 5 | 2026-08-16 | Recent | v5.11.1 (2026-08-16) | 23 / 16 | MIT |
| [agtx](https://github.com/fynnfluegge/agtx) _(new)_ | Rust terminal kanban board running parallel coding agents in tmux windows and git worktrees. | 1,711 | 16 | 146 | 35 | 2026-10-02 | Active | v1.0.6 (2026-09-16) | 13 / 9 | Apache-2.0 |
| [ai-devkit](https://github.com/codeaholicguy/ai-devkit) | CLI control plane running agents in managed tmux, with shared local memory and workflows. | 1,642 | 9 | 257 | 258 | 2026-10-08 | Active | cli@0.68.0 (2026-10-08) | 19 / 2 | Apache-2.0 |
| [CLI Agent Orchestrator (CAO)](https://github.com/awslabs/cli-agent-orchestrator) _(new)_ | Supervisor agent delegates work to specialist coding CLIs running in isolated tmux sessions. | 1,400 | 73 | 293 | 260 | 2026-10-08 | Active | v2.5.3 (2026-10-08) | 116 / 42 | Apache-2.0 |
| [opensessions](https://github.com/Ataraxy-Labs/opensessions) _(new)_ | Tmux sidebar showing live state of Amp, Claude Code, Codex and OpenCode agent sessions. | 1,234 | 9 | 77 | 0 | 2026-06-07 | Slow | v0.2.0-alpha.12 (2026-06-07) | 5 / 20 | None |
| [agent-deck](https://github.com/asheshgoplani/agent-deck) | TUI for Claude Code, Codex, Gemini, and OpenCode sessions with live status and resume. | 1,039 | 162 | 189 | 1,589 | 2026-10-04 | Active | v1.16.26 (2026-10-04) | 25 / 23 | MIT |
| [agterm](https://github.com/umputun/agterm) | Native macOS terminal with named workspaces, live dashboard, attention states, and scriptable control API. | 660 | 41 | 89 | 663 | 2026-10-08 | Active | v0.35.1 (2026-10-05) | 5 / 4 | MIT |
| [Prowl](https://github.com/onevcat/Prowl) | Native macOS command center for parallel agents with a live canvas of every session. | 638 | 34 | 62 | 1,359 | 2026-10-08 | Active | v2026.10.6 (2026-10-05) | 45 / 9 | Other |
| [agent-manager](https://github.com/YoanWai/agent-manager) | Live-status tmux TUI with diff review that sends line comments back to agents. | 578 | 27 | 58 | 692 | 2026-10-08 | Active | v0.40.0 (2026-10-06) | 56 / 11 | Apache-2.0 |
| [tmux-ide](https://github.com/wavyrai/tmux-ide) | Builds a per-project tmux IDE from a checked-in ide.yml, with preset agent-team layouts. | 550 | 1 | 30 | 1,939 | 2026-10-08 | Active | v2.9.5 (2026-10-08) | 2 / 0 | MIT |
| [tmux-agent-sidebar](https://github.com/hiroppy/tmux-agent-sidebar) _(new)_ | Tmux sidebar tracking Claude Code, Codex and OpenCode panes across sessions, with worktree spawning. | 543 | 10 | 87 | 19 | 2026-10-08 | Active | v0.13.0 (2026-06-18) | 10 / 42 | MIT |
| [agentbox](https://github.com/madarco/agentbox) | Gives each agent its own sandboxed VM, local or cloud, with sub-second checkpoint starts. | 523 | 5 | 49 | 884 | 2026-09-23 | Active | tray-latest (2026-09-21) | 6 / 2 | MIT |
| [termany](https://github.com/thinkany-ai/termany) | Terminal for many agent sessions in one window, with per-pane status and token cost. | 462 | 9 | 39 | 169 | 2026-10-05 | Active | v0.2.5 (2026-09-16) | 23 / 10 | Other |
| [NTM](https://github.com/Dicklesworthstone/ntm) _(new)_ | Go tmux control plane that spawns, dispatches work to, and coordinates multiple coding agents. | 454 | 2 | 70 | 1,365 | 2026-10-07 | Active | v1.37.0 (2026-10-07) | 7 / 0 | Other |
| [tmux-claude-hatch](https://github.com/craftzdog/tmux-claude-hatch) _(new)_ | Plugin for tmux that runs Claude Code sessions per project, with fzf status picker. | 399 | 6 | 53 | 31 | 2026-09-28 | Active | v1.5.0 (2026-09-28) | 1 / 3 | MIT |
| [Calyx](https://github.com/yuuichieguchi/Calyx) | Native macOS terminal built on libghostty with approval inbox, status sidebar, and diff review. | 343 | 1 | 24 | 352 | 2026-10-07 | Active | v0.46.1 (2026-10-07) | 0 / 0 | MIT |
| [claude-tmux](https://github.com/nielsgroen/claude-tmux) _(new)_ | Tmux popup TUI that monitors, switches and manages multiple Claude Code sessions, with worktrees. | 206 | 2 | 28 | 0 | 2026-04-17 | Slow | — | 2 / 5 | Other |
| [amux](https://github.com/andyrewlee/amux) | Minimal TUI that spawns parallel coding agents in git worktrees. | 162 | 1 | 3 | 292 | 2026-10-08 | Active | v0.0.20 (2026-07-17) | 2 / 3 | MIT |
| [Rove](https://github.com/Sma1lboy/rove) | TUI orchestrator giving each task its own worktree and branch, with a Kanban board. | 160 | 7 | 9 | 1,907 | 2026-10-08 | Active | v0.9.244 (2026-10-08) | 5 / 6 | MIT |
| [openkanban](https://github.com/TechDufus/openkanban) | Kanban board in the terminal for orchestrating coding agents. | 148 | 1 | 16 | 0 | 2026-06-12 | Slow | v0.1.1 (2026-06-12) | 5 / 1 | AGPL-3.0 |
| [GridBash](https://github.com/jasonsuhari/gridbash) _(new)_ | Terminal grid running parallel CLI coding agents in PTY panes with per-pane git worktrees. | 134 | 1 | 5 | 268 | 2026-10-08 | Active | v0.3.0-nightly.20261008.103.gf894cab8bd44 (2026-10-08) | 39 / 0 | MIT |
| [jmux](https://github.com/jarredkenny/jmux) _(new)_ | Tmux environment running parallel coding-agent sessions on per-ticket worktrees with a status sidebar. | 86 | 4 | 13 | 427 | 2026-08-29 | Recent | v0.29.0 (2026-08-14) | 0 / 0 | AGPL-3.0 |
| [thurbox](https://github.com/Thurbeen/thurbox) | TUI orchestrator for any CLI agent, with SSH sessions, messaging, and a code-review view. | 84 | 10 | 11 | 652 | 2026-10-08 | Active | v2.54.1 (2026-10-08) | 2 / 0 | MIT |
| [TmuxCC](https://github.com/nyanko3141592/tmuxcc) _(new)_ | TUI dashboard that monitors and approves multiple coding agents running in tmux panes. | 67 | 1 | 5 | 0 | 2026-01-19 | Slow | v0.1.5 (2026-01-18) | 0 / 2 | MIT |
| [opencode-kanban](https://github.com/TomCC7/opencode-kanban) _(new)_ | Rust terminal kanban board that maps tasks to git worktrees and OpenCode tmux sessions. | 66 | 3 | 8 | 4 | 2026-08-31 | Recent | v0.6.3 (2026-08-31) | 0 / 0 | MIT |
| [YYLO](https://github.com/yylo-dev/yylo) | CLI orchestrator running Pi and Codex subagents in worktrees behind a risk-based merge queue. | 63 | 2 | 9 | 1,772 | 2026-10-03 | Active | v0.2.1-rc.14 (2026-09-02) | 0 / 10 | MIT |
| [HexoKit](https://github.com/sahil87/hexokit) _(new)_ | Browser and phone tmux console with a spawner launching agents in separate git worktrees. | 61 | 13 | 19 | 944 | 2026-10-08 | Active | v3.21.7 (2026-10-08) | 1 / 6 | MIT |
| [Claude Code tmux Orchestration](https://github.com/primeline-ai/claude-tmux-orchestration) _(new)_ | Bash heartbeat orchestrator spawning Claude Code worker sessions in tmux windows with file-based coordination. | 39 | 1 | 2 | 1 | 2026-07-30 | Recent | — | 0 / 0 | MIT |
| [agentvm](https://github.com/Twigpine/agentvm) _(new)_ | Pure-bash CLI spawning sandboxed tmux workspaces for parallel coding agents with broadcast commands. | 37 | 1 | 12 | 0 | 2026-04-25 | Slow | — | 0 / 0 | None |
| [hydra-acp](https://github.com/smagnuso/hydra-acp) _(new)_ | Session daemon and TUI that spawns ACP agents and shares live sessions across clients. | 35 | 5 | 5 | 532 | 2026-10-08 | Active | — | 1 / 2 | MIT |
| [Agent CLI Farm](https://github.com/waskosky/agent-cli-farm) _(new)_ | Tmux session manager that runs, monitors, restores, and loops Codex, Claude, and Gemini CLIs. | 34 | 1 | 1 | 51 | 2026-10-06 | Active | v1.3.4 (2026-09-02) | 1 / 0 | MIT |
| [agent-console](https://github.com/buhuipao/agent-console) | Rust TUI that finds Codex and Claude Code sessions and resumes their native UI. | 34 | 1 | 3 | 55 | 2026-09-20 | Active | v0.3.4 (2026-09-20) | 0 / 0 | Apache-2.0 |
| [AgEnD Terminal](https://github.com/suzuke/agend-terminal) _(new)_ | Rust PTY multiplexer launching a fleet.yaml of agents with MCP tools for delegation. | 33 | 5 | 6 | 672 | 2026-09-23 | Active | v0.12.2 (2026-08-17) | 21 / 8 | Apache-2.0 |
| [Orchestra](https://github.com/humanunsupervised/orchestra) _(new)_ | Rust TUI mapping Git worktrees to tmux sessions for running parallel AI coding agents. | 29 | 1 | 2 | 0 | 2025-10-15 | Slow | v0.5.81 (2026-07-16) | 1 / 0 | Other |
| [Vigil](https://github.com/butterlatte-zhang/vigil) | Native macOS terminal where a manager agent spawns workers and sub-managers in a tree. | 29 | 1 | 0 | 15 | 2026-10-08 | Active | v0.1.7 (2026-10-08) | 0 / 0 | GPL-3.0 |
| [OpenCode Mission Control](https://github.com/nigel-dev/opencode-mission-control) _(new)_ | Plugin running parallel agent jobs in git worktrees and tmux sessions, with dependency plans. | 27 | 1 | 5 | 0 | 2026-06-25 | Slow | v1.6.0 (2026-02-17) | 39 / 4 | MIT |
| [agents-in-a-box](https://github.com/stevengonsalvez/agents-in-a-box) _(new)_ | Rust TUI orchestrating Claude Code, Codex, Gemini and Copilot sessions in isolated git worktrees. | 26 | 2 | 8 | 3,298 | 2026-09-13 | Active | v1.28.5 (2026-09-13) | 132 / 13 | MIT |
| [repomon](https://github.com/AliHamzaAzam/repomon) | Rust TUI supervising agents across many repos in durable tmux sessions, approvable by phone. | 22 | 2 | 2 | 1,054 | 2026-10-04 | Active | desktop-preview (2026-09-28) | 2 / 1 | Apache-2.0 |
| [pappardelle](https://github.com/chardigio/pappardelle) | TUI that turns a description into an issue, worktree, PR, and Claude Code session. | 17 | 4 | 5 | 37 | 2026-10-05 | Active | v3.0.14 (2026-10-05) | 1 / 5 | MIT |
| [agent-session-manager](https://github.com/izll/agent-session-manager) | Live tmux TUI with session groups, resume and fork, diff review, and mobile push. | 13 | 1 | 0 | 19 | 2026-09-25 | Active | v0.9.2 (2026-09-25) | 0 / 0 | MIT |
| [Cyclops](https://github.com/cyclops-team/cyclops) | Coordinates coding agents in tmux through a durable mailbox, with an optional workspace UI. | 13 | 4 | 0 | 952 | 2026-09-06 | Recent | v1.1.0 (2026-09-05) | 0 / 1 | MIT |

## Parallel Coding Agents — Desktop & Web

The same parallel-sessions workflow as a desktop app or browser/mobile dashboard, with diff review and merge.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [Orca](https://github.com/stablyai/orca) | Desktop and mobile agentic development environment for running agent fleets on your own subscription. | 87,869 | 421 | 5,623 | 6,839 | 2026-10-08 | Active | v1.4.222 (2026-10-07) | 4,049 / 4,158 | MIT |
| [AionUi](https://github.com/iOfficeAI/AionUi) _(new)_ | Desktop cowork app hosting dozens of CLI agents in one interface, with cron automation. | 33,389 | 104 | 3,468 | 258 | 2026-09-09 | Active | v2.2.2 (2026-09-09) | 704 / 234 | Apache-2.0 |
| [t3code](https://github.com/pingdotgg/t3code) | Web, mobile, and desktop control surface for harnesses like Claude Code, Codex, and Cursor. | 26,377 | 411 | 6,851 | 3,121 | 2026-10-08 | Active | v0.0.46-nightly.20261008.2833 (2026-10-08) | 1,321 / 1,538 | MIT |
| [opcode](https://github.com/winfunc/opcode) _(new)_ | Desktop GUI for managing Claude Code sessions and running custom agents as background processes. | 22,421 | 14 | 1,711 | 1 | 2026-09-18 | Active | v0.2.0 (2025-08-31) | 267 / 65 | AGPL-3.0 |
| [Paseo](https://github.com/getpaseo/paseo) | Self-hosted, telemetry-free daemon running parallel agents, controlled from desktop, mobile, web, or CLI. | 20,148 | 191 | 2,372 | 1,488 | 2026-10-08 | Active | v0.11.1 (2026-10-07) | 597 / 527 | Other |
| [qm](https://github.com/yc-software/qm) | Multiplayer harness with isolated per-teammate agent workspaces, driven from Slack or the web. | 15,362 | 18 | 1,903 | 848 | 2026-10-08 | Active | vendored-slack-socket-mode-2.0.7-qm.1 (2026-10-05) | 304 / 565 | MIT |
| [superset](https://github.com/superset-sh/superset) | Code editor built for running many agents at once on your machine. | 15,005 | 130 | 1,337 | 1,716 | 2026-10-08 | Active | desktop-canary (2026-10-08) | 435 / 477 | Other |
| [cc-haha](https://github.com/NanmiCoder/cc-haha) _(new)_ | Desktop Claude Code workbench with multi-session tabs, worktrees, Agent Teams and sub-agent workflow orchestration. | 14,916 | 34 | 8,599 | 852 | 2026-10-08 | Active | v0.7.0 (2026-10-08) | 114 / 79 | MIT |
| [Aperant](https://github.com/AndyMik90/Aperant) | Runs up to 12 agent terminals with a self-validating QA loop and merge-conflict resolution. | 14,583 | 23 | 1,904 | 0 | 2026-06-14 | Slow | v2.8.0-beta.6 (2026-03-23) | 34 / 2 | AGPL-3.0 |
| [agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | IDE that plans work, spawns agents, and fixes CI failures and merge conflicts unprompted. | 12,926 | 115 | 1,779 | 1,515 | 2026-10-08 | Active | v0.13.5 (2026-10-08) | 435 / 357 | Apache-2.0 |
| [humanlayer](https://github.com/humanlayer/humanlayer) | Human-in-the-loop control for coding agents, now largely deprecated in favor of a rebuild. | 11,678 | 26 | 960 | 0 | 2026-06-19 | Slow | nightly-0.1.0-nightly-20260227142452 (2026-02-27) | 51 / 0 | Other |
| [Ekko Studio](https://github.com/EKKOLearnAI/ekko-studio) _(new)_ | Desktop and web workspace running multiple agent runtimes with group chat and visual workflows. | 11,333 | 82 | 1,387 | 631 | 2026-10-08 | Active | v0.7.32 (2026-10-08) | 348 / 123 | Other |
| [OpenChamber](https://github.com/openchamber/openchamber) | Open-source workspace for supervising AI coding work across desktop, browser, editor, and mobile. | 11,286 | 288 | 1,247 | 2,628 | 2026-10-08 | Active | v2.2.0 (2026-10-08) | 175 / 21 | MIT |
| [Atlas](https://github.com/pacifio/atlas) _(new)_ | Desktop app running Claude Code, Codex and ACP agents side by side with checkpoints. | 9,454 | 42 | 366 | 1,155 | 2026-10-07 | Active | alpha-0.3.4 (2026-09-27) | 24 / 9 | Apache-2.0 |
| [Yao Agents](https://github.com/YaoApp/yao) _(new)_ | Self-hosted workspace running agents across your devices, with a task board and open API. | 8,101 | 9 | 721 | 137 | 2026-10-08 | Active | v1.0.0-rc26 (2026-10-05) | 4 / 6 | Other |
| [ClawX](https://github.com/ValueCell-ai/ClawX) _(new)_ | Electron desktop app for managing specialized OpenClaw agents, channels, and scheduled tasks. | 7,612 | 25 | 1,138 | 126 | 2026-09-29 | Active | v0.6.0 (2026-09-29) | 20 / 23 | MIT |
| [Emdash](https://github.com/generalaction/emdash) | Agentic development environment running parallel agents with any model provider. | 5,941 | 127 | 626 | 1,985 | 2026-10-07 | Active | v1.2.8-canary.98 (2026-10-08) | 66 / 32 | Apache-2.0 |
| [bb](https://github.com/get-bb/bb) | IDE running coding agents in live threads you can follow, steer, or hand off. | 4,191 | 90 | 610 | 2,532 | 2026-10-08 | Active | desktop-v0.45.0 (2026-10-02) | 478 / 72 | MIT |
| [OpenAgents](https://github.com/openagents-org/openagents) _(new)_ | Shared workspace and launcher where Claude Code, Codex and other agents collaborate in threads. | 4,183 | 28 | 427 | 705 | 2026-10-08 | Active | launcher-v1.0.13 (2026-09-30) | 60 / 18 | Apache-2.0 |
| [Codeg](https://github.com/spacering-net/codeg) _(new)_ | Desktop, server and mobile workspace running fifteen coding agents with cross-agent delegation. | 3,857 | 42 | 500 | 1,476 | 2026-10-07 | Active | v0.34.0 (2026-10-07) | 167 / 139 | Apache-2.0 |
| [Maestro](https://github.com/RunMaestro/Maestro) _(new)_ | Desktop app orchestrating parallel Claude Code, Codex and OpenCode agents with worktrees and playbooks. | 3,429 | 49 | 366 | 698 | 2026-10-08 | Active | v0.18.8-RC (2026-10-05) | 60 / 84 | AGPL-3.0 |
| [automaker](https://github.com/AutoMaker-Org/automaker) | Kanban board where agents implement described features in isolated worktrees, running tests and committing. | 3,229 | 41 | 599 | 0 | 2026-05-22 | Slow | v1.0.0 (2026-03-15) | 8 / 2 | Other |
| [Zeron](https://github.com/zeronsh/zeron) | Cross-device control plane for coding agents, with synced sessions and an always-on daemon. | 3,128 | 31 | 296 | 1,766 | 2026-10-08 | Active | v0.2.107 (2026-10-08) | 97 / 191 | MIT |
| [Crystal](https://github.com/stravu/crystal) _(new)_ | Deprecated multi-session AI code assistant manager, replaced by Nimbalyst. | 3,127 | 14 | 198 | 0 | 2026-02-26 | Slow | v0.3.5 (2026-02-26) | 60 / 8 | MIT |
| [collaborator](https://github.com/collabs-inc/collab-public) | Arranges terminals, editors, and files as tiles on an infinite pan-and-zoom canvas, not tabs. | 3,068 | 9 | 305 | 0 | 2026-06-16 | Slow | v0.8.4 (2026-06-16) | 57 / 24 | Other |
| [MonoCode](https://github.com/hardbeat920/monocode) | Cross-platform Tauri desktop UI with agent sessions as tabs, using your existing subscriptions. | 2,798 | 66 | 291 | 846 | 2026-10-08 | Active | v0.10.0 (2026-10-08) | 211 / 163 | MIT |
| [CodeNomad](https://github.com/NeuralNomadsAI/CodeNomad) | Desktop and web workspace for OpenCode, embedding local tools like VS Code as tabs. | 2,614 | 25 | 176 | 310 | 2026-10-08 | Active | v0.20.1-dev-20261008-027f5094 (2026-10-08) | 10 / 13 | MIT |
| [supacode](https://github.com/supabitapp/supacode) | Native macOS command center for development with one git worktree per agent. | 2,397 | 55 | 261 | 110 | 2026-09-05 | Recent | v0.10.8 (2026-08-03) | 80 / 8 | Other |
| [Cate](https://github.com/0-AI-UG/cate) _(new)_ | Infinite-canvas IDE that tracks parallel agent terminals and creates git worktrees per branch. | 2,175 | 17 | 141 | 616 | 2026-10-03 | Active | v2.0.5 (2026-09-30) | 2 / 6 | MIT |
| [synara](https://github.com/Emanuele-web04/synara) | Desktop GUI workspace for running and managing agents across local projects. | 2,062 | 134 | 318 | 2,224 | 2026-10-08 | Active | v1.0.1-beta.2 (2026-10-07) | 149 / 206 | MIT |
| [xum](https://github.com/coder/xum) | Desktop app for isolated, parallel agentic development. | 2,049 | 20 | 140 | 1,333 | 2026-10-08 | Active | v0.30.1-nightly.845 (2026-10-08) | 207 / 220 | AGPL-3.0 |
| [nodeterm](https://github.com/eneskirca/nodeterm) _(new)_ | Canvas terminal manager for parallel tmux-backed agent sessions with a kanban board. | 2,006 | 38 | 223 | 4,388 | 2026-10-08 | Active | v0.4.2 (2026-10-05) | 63 / 25 | Other |
| [nimbalyst](https://github.com/nimbalyst/nimbalyst) | Visual workspace pairing parallel worktree sessions with kanban and direct visual editing. | 1,854 | 43 | 292 | 1,315 | 2026-10-08 | Active | v0.80.4 (2026-10-08) | 645 / 102 | MIT |
| [OpenCove](https://github.com/DeadWaveWave/opencove) _(new)_ | Infinite-canvas desktop workspace for running multiple Claude Code and Codex sessions side by side. | 1,606 | 18 | 142 | 97 | 2026-09-22 | Active | v0.3.3-nightly.20260926.1 (2026-09-25) | 13 / 4 | MIT |
| [Traycer](https://github.com/traycerai/traycer) | Bring-your-own-agent workspace running parallel sessions with context shared across models and providers. | 1,597 | 11 | 213 | 1,411 | 2026-10-08 | Active | desktop-v1.5.0 (2026-10-07) | 228 / 48 | MIT |
| [Waku](https://github.com/egoist/waku) | Native macOS app for local coding agents, keeping sessions and transcripts on your machine. | 1,566 | 16 | 185 | 484 | 2026-10-02 | Active | v0.1.20 (2026-10-02) | 105 / 54 | GPL-3.0 |
| [Agor](https://github.com/preset-io/agor) _(new)_ | Self-hosted web workspace running Claude Code, Codex and Gemini sessions on isolated git branches. | 1,432 | 41 | 131 | 674 | 2026-10-08 | Active | v0.15.0 (2026-03-28) | 166 / 77 | Other |
| [Kimaki](https://github.com/remorses/kimaki) _(new)_ | Discord bot mapping channels to projects and threads to parallel OpenCode coding sessions. | 1,429 | 11 | 118 | 312 | 2026-10-06 | Active | kimaki@0.31.0 (2026-09-28) | 30 / 28 | MIT |
| [Vibeyard](https://github.com/elirantutia/vibeyard) _(new)_ | IDE managing parallel Claude Code, Codex and Gemini CLI sessions with a kanban board. | 1,387 | 12 | 173 | 24 | 2026-09-03 | Recent | v0.3.8 (2026-09-03) | 20 / 13 | MIT |
| [Kanban](https://github.com/cline/kanban) _(new)_ | Local web app running CLI coding agents in parallel, one worktree per kanban card. | 1,355 | 17 | 330 | 4 | 2026-09-04 | Recent | v0.1.70 (2026-07-12) | 204 / 110 | Apache-2.0 |
| [jean](https://github.com/coollabsio/jean) | Desktop and web app orchestrating Claude, Codex, and OpenCode across projects and git worktrees. | 1,315 | 51 | 162 | 666 | 2026-10-08 | Active | v1.0.9 (2026-10-07) | 85 / 46 | Apache-2.0 |
| [Helmor](https://github.com/dohooo/helmor) _(new)_ | Desktop workbench running many coding agents in parallel, each in its own git worktree. | 1,309 | 21 | 119 | 15 | 2026-07-24 | Recent | v0.46.0 (2026-07-24) | 30 / 14 | Apache-2.0 |
| [Flock](https://github.com/Onelevenvy/flock) _(new)_ | Tauri desktop app orchestrating built-in agents and multi-agent team workflows with a visual editor. | 1,117 | 2 | 146 | 0 | 2026-07-06 | Slow | v0.3.1 (2026-06-17) | 1 / 1 | Apache-2.0 |
| [takopi](https://github.com/banteg/takopi) | Telegram bridge putting Codex, Claude Code, OpenCode, and Pi sessions in a chat thread. | 1,049 | 13 | 137 | 0 | 2026-05-25 | Slow | v0.23.4 (2026-05-25) | 16 / 33 | MIT |
| [parallel-code](https://github.com/johannesjo/parallel-code) | Desktop app running Claude Code, Codex, and Gemini CLI in parallel isolated worktrees. | 1,037 | 21 | 144 | 406 | 2026-10-08 | Active | v3.1.0 (2026-09-26) | 38 / 15 | MIT |
| [Berd](https://github.com/block/berd) | Block's open-source desktop app for project chats with AI agents over the Goose backend. | 972 | 24 | 127 | 230 | 2026-10-08 | Active | v0.6.4 (2026-09-10) | 73 / 31 | Apache-2.0 |
| [IM.codes](https://github.com/im4codes/imcodes) | Mobile and web control layer for continuing agent sessions away from your desk. | 972 | 2 | 122 | 674 | 2026-08-23 | Recent | android-dev-v1.1-f03b7bd (2026-10-08) | 1 / 1 | MIT |
| [kandev](https://github.com/kdlbs/kandev) | Kanban workbench whose multi-step workflows assign a different agent per step behind human gates. | 909 | 67 | 149 | 2,214 | 2026-10-08 | Active | v0.97.0 (2026-10-04) | 66 / 82 | AGPL-3.0 |
| [Ghostex](https://github.com/maddada/Ghostex) | Native macOS workspace running CLI agents side by side in low-RAM Ghostty terminals. | 899 | 18 | 52 | 3,745 | 2026-10-08 | Active | v10.15.5 (2026-10-08) | 7 / 4 | MIT |
| [Pocket Server](https://github.com/yayasoumah/pocket-server) _(new)_ | Local runtime exposing agents, terminals, and background coding jobs to the Pocket mobile app. | 837 | 1 | 63 | 0 | 2025-10-21 | Slow | v1.0.6 (2025-10-21) | 4 / 0 | Apache-2.0 |
| [Arbor](https://github.com/penso/arbor) _(new)_ | Native Rust desktop app managing worktrees, terminals and coding agents for parallel sessions. | 836 | 4 | 40 | 2 | 2026-09-21 | Active | 20260316.01 (2026-03-16) | 18 / 5 | MIT |
| [Alethe](https://github.com/Kc1t/alethe-agents) | Local-first desktop workspace running agents and shells as real PTYs that survive app restarts. | 834 | 46 | 104 | 555 | 2026-10-07 | Active | v1.7.0 (2026-09-20) | 32 / 14 | AGPL-3.0 |
| [ai-maestro](https://github.com/23blocks-OS/ai-maestro) | Multi-machine dashboard for coding agents with memory search, code-graph queries, and agent-to-agent messaging. | 816 | 7 | 114 | 217 | 2026-10-07 | Active | v0.60.4 (2026-10-07) | 13 / 0 | MIT |
| [Cezar](https://github.com/open-mercato/cezar) _(new)_ | Web cockpit running queued coding-agent tasks in parallel git worktrees, with workflows and automations. | 559 | 25 | 114 | 1,145 | 2026-10-08 | Active | v0.14.0 (2026-10-02) | 137 / 121 | MIT |
| [omg.dev](https://github.com/BennyKok/omg.dev) | Open-source harness running coding agents in parallel, locally or hosted, from one web UI. | 547 | 9 | 41 | 3,234 | 2026-10-08 | Active | v0.6.207 (2026-10-08) | 4 / 4 | MIT |
| [Async Code Agent](https://github.com/ObservedObserver/async-code) _(new)_ | Self-hosted Codex-style web UI running multiple Claude Code or Codex tasks in parallel containers. | 534 | 3 | 50 | 0 | 2025-08-04 | Stale | — | 11 / 1 | Apache-2.0 |
| [Orb](https://github.com/Th0rgal/orb) _(new)_ | Rust backend and macOS/iOS clients running agent harness missions on local and remote machines. | 516 | 12 | 53 | 1,546 | 2026-10-08 | Active | v0.12.0 (2026-05-16) | 16 / 0 | None |
| [Proliferate](https://github.com/proliferate-ai/proliferate) | Agent IDE running local or cloud sessions, letting you build reusable workflows from them. | 515 | 11 | 85 | 1,464 | 2026-08-28 | Recent | proliferate-v0.4.29 (2026-08-27) | 32 / 72 | AGPL-3.0 |
| [Vicoa](https://github.com/vicoa-ai/vicoa) | Agentic IDE and orchestrator for coding-agent teams across desktop, web, and mobile. | 497 | 1 | 51 | 224 | 2026-10-08 | Active | v0.1.38 (2026-10-08) | 3 / 2 | AGPL-3.0 |
| [AgentHub](https://github.com/jamesrochabrun/AgentHub) _(new)_ | macOS app monitoring and launching parallel Claude Code and Codex sessions across git worktrees. | 487 | 4 | 36 | 48 | 2026-08-19 | Recent | v2.16.0 (2026-08-19) | 16 / 5 | MIT |
| [Hive](https://github.com/morapelker/hive) _(new)_ | Desktop app running parallel Claude Code, OpenCode and Codex sessions in isolated git worktrees. | 470 | 16 | 55 | 451 | 2026-09-29 | Active | v1.2.49 (2026-09-29) | 2 / 1 | MIT |
| [diri](https://github.com/cristicretu/diri) | Native macOS app running agents and shells in parallel across worktrees or remote hosts. | 427 | 10 | 34 | 639 | 2026-10-08 | Active | nightly (2026-10-07) | 17 / 25 | Apache-2.0 |
| [FleetCode](https://github.com/built-by-as/FleetCode) _(new)_ | Desktop terminal app running multiple Claude or Codex sessions in separate git worktrees. | 424 | 2 | 23 | 0 | 2026-03-17 | Slow | v1.0.1-beta.8 (2025-10-26) | 1 / 1 | None |
| [wmux](https://github.com/openwong2kim/wmux) | Terminal workspace for macOS and Windows running agent CLIs in parallel with worktree fan-out. | 415 | 25 | 70 | 1,305 | 2026-10-08 | Active | v4.2.0 (2026-10-08) | 22 / 4 | MIT |
| [Open Session](https://github.com/tellahq/opensession) | Self-hosted server running coding sessions in worktrees or sandboxes, with diff and PR review. | 392 | 7 | 29 | 6,601 | 2026-10-08 | Active | v0.4.75 (2026-10-07) | 10 / 46 | MIT |
| [Harnss](https://github.com/OpenSource03/harnss) _(new)_ | Desktop app running Claude Code, Codex and ACP agents in parallel sessions. | 382 | 2 | 43 | 0 | 2026-06-19 | Slow | v0.22.0-beta.2 (2026-04-14) | 14 / 8 | MIT |
| [Hermes Studio](https://github.com/JPeetz/Hermes-Studio) _(new)_ | Self-hosted web dashboard for Hermes Agent with multi-agent crews, conductor missions and cron scheduling. | 367 | 2 | 78 | 0 | 2026-07-03 | Slow | v1.3.0 (2026-04-22) | 9 / 3 | Other |
| [Orchestration War Room](https://github.com/Naroh091/hermes-war-room) _(new)_ | Browser dashboard that monitors and directs a Hermes Agent team via kanban delegation. | 355 | 4 | 42 | 3 | 2026-09-18 | Active | v1.6.0 (2026-09-18) | 2 / 6 | MIT |
| [dorothy](https://github.com/Charlie85270/Dorothy) | Desktop app combining agent orchestration with automations, Kanban management, and MCP servers. | 350 | 7 | 62 | 0 | 2026-07-07 | Slow | 1.2.9 (2026-07-07) | 7 / 4 | MIT |
| [ClawSuite](https://github.com/outsourc-e/clawsuite) _(new)_ | Web and PWA command center for orchestrating multiple OpenClaw agents and missions. | 340 | 7 | 59 | 0 | 2026-05-23 | Slow | v4.0.0 (2026-03-27) | 1 / 2 | MIT |
| [Agentrove](https://github.com/Mng-dev-ai/agentrove) _(new)_ | Self-hosted web, desktop and iOS workspace where a lead chat spawns worker agent sub-threads. | 334 | 4 | 63 | 372 | 2026-10-07 | Active | v0.1.62 (2026-09-26) | 0 / 0 | Apache-2.0 |
| [Orbital](https://github.com/zqiren/Orbital) _(new)_ | Project agent keeping context in local files and delegating queued tasks to worker agents. | 310 | 2 | 25 | 438 | 2026-10-03 | Active | v0.15.0 (2026-09-28) | 7 / 1 | GPL-3.0 |
| [aizen](https://github.com/vivy-company/aizen) | Workspace for macOS that organizes worktrees, environments, and agent sessions per project. | 308 | 4 | 21 | 9 | 2026-07-25 | Recent | v1.0.83 (2026-07-25) | 3 / 0 | GPL-3.0 |
| [Intent](https://github.com/intent-hq/intent) | Desktop app for coordinating coding agents with tasks, git, terminals, and an iOS companion. | 298 | 6 | 24 | 4,766 | 2026-10-08 | Active | — | 153 / 9 | Apache-2.0 |
| [Termic](https://github.com/simion/termic) _(new)_ | Desktop app running Claude, Codex and other agent CLIs in parallel git worktrees. | 298 | 27 | 43 | 1,228 | 2026-10-08 | Active | v1.14.2 (2026-10-08) | 14 / 0 | AGPL-3.0 |
| [Monet](https://github.com/zenolab124/monet) _(new)_ | Desktop workbench running parallel Claude Code and Codex sessions with monitoring and race mode. | 283 | 3 | 10 | 448 | 2026-10-07 | Active | nightly (2026-09-23) | 7 / 0 | MIT |
| [Runner](https://github.com/yicheng47/runner) | Native macOS and Windows app running CLI agents in split panes as a crew. | 272 | 2 | 17 | 1,436 | 2026-10-08 | Active | v0.13.2 (2026-10-08) | 28 / 1 | MIT |
| [vibe-tree](https://github.com/sahithvibudhi/vibe-tree) | Gives each agent its own git worktree, in desktop, web, and CLI versions. | 267 | 6 | 31 | 72 | 2026-07-25 | Recent | v0.2.0 (2026-07-24) | 10 / 3 | MIT |
| [MulmoTerminal](https://github.com/receptron/mulmoterminal) | Browser grid of live Claude Code and Codex sessions, started with one npx command. | 236 | 3 | 31 | 6,454 | 2026-10-08 | Active | 9.5.0 (2026-10-08) | 8 / 2 | MIT |
| [Sculptor](https://github.com/imbue-ai/sculptor) _(new)_ | Desktop app running coding agents in parallel across isolated workspaces of a repository. | 236 | 7 | 18 | 261 | 2026-09-18 | Active | sculptor-v0.48.0 (2026-09-21) | 0 / 21 | MIT |
| [zuse](https://github.com/swarajbachu/zuse) | Chat-first desktop app wrapping Claude Code, Codex, Grok, Gemini, and others in persistent sessions. | 227 | 4 | 20 | 406 | 2026-10-08 | Active | v0.24.0-preview.4 (2026-10-08) | 20 / 21 | AGPL-3.0 |
| [constellagent](https://github.com/owengretzinger/constellagent) | Mac app giving each agent its own terminal, editor, and worktree in one window. | 216 | 3 | 16 | 0 | 2026-05-05 | Slow | — | 3 / 3 | None |
| [Operator](https://github.com/iishyfishyy/operator-oss) _(new)_ | Web control room running parallel Claude Code and Codex sessions in isolated git worktrees. | 205 | 2 | 29 | 184 | 2026-09-27 | Active | v0.2.0 (2026-09-24) | 1 / 5 | Apache-2.0 |
| [ivy-tendril](https://github.com/Ivy-Interactive/Ivy-Tendril) | Drives agents through a plan-based lifecycle with verification gates, self-improving memory, and human checkpoints. | 201 | 9 | 9 | 1,932 | 2026-09-15 | Active | v1.2.4 (2026-09-14) | 162 / 11 | Other |
| [Tempest](https://github.com/tempestai-dev/tempest) | Tauri desktop app running CLI agents in isolated worktrees, sharing a local code-knowledge graph. | 187 | 6 | 10 | 380 | 2026-10-06 | Active | v0.1.25 (2026-10-06) | 12 / 3 | Apache-2.0 |
| [Claude Command Center (CCC)](https://github.com/amirfish1/claude-command-center) | Local dashboard to spawn, monitor, and resume sessions across Claude Code, Codex, and others. | 178 | 6 | 23 | 3,298 | 2026-10-08 | Active | v5.37.0 (2026-10-05) | 3 / 5 | Other |
| [Ouijit](https://github.com/ouijit/ouijit) | Kanban board and terminals wired by lifecycle hooks and a CLI, with per-task worktrees. | 174 | 2 | 8 | 56 | 2026-10-04 | Active | v1.9.0 (2026-09-03) | 8 / 0 | AGPL-3.0 |
| [TUICommander](https://github.com/sstraus/tuicommander) _(new)_ | Tauri desktop IDE running parallel coding agents in worktrees with an activity dashboard. | 161 | 9 | 33 | 3,330 | 2026-10-08 | Active | nightly (2026-10-08) | 2 / 0 | Apache-2.0 |
| [clideck](https://github.com/rustykuntz/clideck) | Chat-style dashboard for Claude Code, Codex, and others, with autopilot routing and phone control. | 159 | 3 | 28 | 51 | 2026-10-06 | Active | v2.4.0 (2026-09-29) | 2 / 0 | MIT |
| [Gold Band](https://github.com/diodeme/Gold-Band) _(new)_ | Desktop ACP client with workflows and AUTO mode dispatching subtasks to agents in worktrees. | 143 | 7 | 14 | 1,008 | 2026-09-30 | Active | v0.18.0 (2026-09-30) | 8 / 2 | AGPL-3.0 |
| [KanVibe](https://github.com/rookedsysc/kanvibe) _(new)_ | Desktop kanban board linking tasks to git worktrees and tmux sessions running coding agents. | 143 | 3 | 18 | 226 | 2026-10-08 | Active | 1.4.0 (2026-08-31) | 2 / 1 | AGPL-3.0 |
| [Claude Control](https://github.com/sverrirsig/claude-control) _(new)_ | macOS Electron dashboard that monitors Claude Code sessions, approves prompts and creates worktree sessions. | 136 | 5 | 19 | 5 | 2026-09-07 | Recent | v0.19.0 (2026-09-07) | 0 / 0 | MIT |
| [GraphCode](https://github.com/scgopi/GraphCode) | Mac app wiring agent sessions into a graph of live terminals linked by hand-offs. | 136 | 7 | 19 | 2,076 | 2026-10-08 | Active | v0.1.78 (2026-10-04) | 24 / 5 | Other |
| [AgentOS](https://github.com/SapienXai/AgentOS) _(new)_ | Operating layer for creating, scheduling and monitoring teams of OpenClaw-powered digital workers. | 118 | 2 | 20 | 615 | 2026-10-03 | Active | agentos-v0.8.0 (2026-09-14) | 18 / 0 | MIT |
| [ADE](https://github.com/arul28/ADE) _(new)_ | Desktop, web, mobile and terminal workspace managing parallel coding agents across git worktrees. | 114 | 8 | 13 | 989 | 2026-10-08 | Active | v1.2.96 (2026-10-08) | 39 / 4 | AGPL-3.0 |
| [tlbx](https://github.com/tlbx-ai/tlbx) | Self-hosted browser workspace holding persistent PTY sessions, reachable from any browser or phone. | 114 | 2 | 5 | 493 | 2026-09-25 | Active | v10.17.33-dev (2026-10-08) | 3 / 8 | AGPL-3.0 |
| [Dray](https://github.com/monorepo-labs/dray) | Native desktop chat UI wrapping Claude Code and Codex, with one worktree per session. | 110 | 1 | 10 | 645 | 2026-10-08 | Active | v0.27.0-beta.2 (2026-10-07) | 14 / 2 | Apache-2.0 |
| [ADHDev](https://github.com/vilmire/adhdev) _(new)_ | Web and mobile dashboard dispatching queued tasks to coding agents in worktrees across machines. | 105 | 2 | 17 | 1,994 | 2026-10-08 | Active | — | 0 / 0 | AGPL-3.0 |
| [Gas Town GUI](https://github.com/web3dev1337/gastown-gui) _(new)_ | Web GUI managing Gas Town rigs, work assignment, and polecat agent lifecycle through gt. | 93 | 5 | 31 | 3 | 2026-08-31 | Recent | v0.9.7 (2026-03-27) | 7 / 5 | MIT |
| [Garcon](https://github.com/cfal/garcon) | Self-hosted browser and mobile workspace for seven CLI agents, with diff review and approvals. | 91 | 6 | 15 | 613 | 2026-10-08 | Active | v0.3.3 (2026-07-12) | 33 / 8 | Other |
| [Tortie](https://github.com/gregce/tortie) | Native macOS agent multiplexer whose agents survive restarts, with all projects in one window. | 88 | 2 | 9 | 1,919 | 2026-10-08 | Active | v0.110.0 (2026-09-21) | 11 / 1 | Apache-2.0 |
| [Mexus](https://github.com/yofine/Mexus) _(new)_ | Local web console running parallel CLI agents in managed panes with per-agent Git worktrees. | 86 | 1 | 5 | 0 | 2026-05-18 | Slow | — | 0 / 1 | Apache-2.0 |
| [Helicon](https://github.com/HarjjotSinghh/helicon) | Unofficial app for Muse Code, unaffiliated with Meta, listing all threads in one sidebar. | 76 | 8 | 12 | 334 | 2026-10-08 | Active | v0.21.4 (2026-10-08) | 43 / 4 | MIT |
| [intentic](https://github.com/intentic/intentic) | Browser and mobile workspace giving each agent a persistent Docker sandbox, MIT licensed. | 74 | 2 | 14 | 4,228 | 2026-10-08 | Active | v1.329.0 (2026-10-08) | 0 / 1 | MIT |
| [opendray](https://github.com/Opendray/opendray) _(new)_ | Self-hosted server keeping multiple coding agent sessions alive, reattachable from web, mobile and chat. | 67 | 5 | 14 | 115 | 2026-09-24 | Active | v2.17.8 (2026-09-24) | 5 / 10 | Apache-2.0 |
| [Zaivern Code](https://github.com/tacyan/zaivern-code) | Rust desktop cockpit running Claude Code, Codex, Gemini CLI, and 30+ agents in parallel. | 54 | 2 | 1 | 861 | 2026-10-01 | Active | v0.24.9 (2026-09-30) | 0 / 3 | Apache-2.0 |
| [ChatML](https://github.com/chatml/chatml) _(new)_ | macOS app running parallel Claude coding sessions, each in an isolated git worktree. | 52 | 3 | 7 | 0 | 2026-05-12 | Slow | v0.1.16 (2026-03-19) | 51 / 3 | Other |
| [clave](https://github.com/antasphere/clave) | Native macOS app for Claude Code with grid layouts, SSH sessions, and usage analytics. | 51 | 6 | 10 | 447 | 2026-10-05 | Active | v2.0.0 (2026-09-30) | 1 / 2 | MIT |
| [vibepanel](https://github.com/jiangmuran/vibepanel) _(new)_ | Web console organizing many parallel coding-agent sessions by project, with phone and chat-bot approvals. | 50 | 5 | 4 | 569 | 2026-10-08 | Active | v1.26.2 (2026-10-08) | 9 / 0 | Other |
| [Polpo](https://github.com/pugliatechs/polpo) _(new)_ | Phone-first dashboard running multiple coding CLI sessions, with optional goal-to-DAG agent fan-out. | 46 | 2 | 0 | 21 | 2026-09-24 | Active | v1.2.3 (2026-09-24) | 0 / 0 | MIT |
| [Termexo](https://github.com/gemron/Termexo) _(new)_ | Windows workbench running several coding-agent terminals, letting one AI prompt others through MCP. | 43 | 2 | 6 | 172 | 2026-10-08 | Active | v0.10.13 (2026-10-08) | 4 / 0 | MIT |
| [AI4Kanban](https://github.com/ai4kanban/ai4kanban) | AI project manager that turns rough ideas into tasks and coordinates coding agents. | 42 | 1 | 5 | 1,026 | 2026-10-08 | Active | v0.10.0 (2026-10-04) | 0 / 0 | Apache-2.0 |
| [Nuphos](https://github.com/nuphos/nuphos) | Desktop and web team workspace running Claude Code and Codex via ACP across machines. | 40 | 2 | 6 | 91 | 2026-10-08 | Active | runtime-v0.1.18 (2026-10-08) | 0 / 11 | Other |
| [Podium ADE](https://github.com/madeinorbit/podium) | Open-source workspace turning conversations into coordinated coding-agent work through a shared task system. | 35 | 3 | 3 | 16,283 | 2026-10-06 | Active | dev (2026-08-25) | 0 / 7 | Apache-2.0 |
| [vibecraft](https://github.com/rayzhudev/vibecraft) | Workspace styled like a real-time strategy game for commanding coding agents. | 35 | 2 | 3 | 1 | 2026-07-19 | Recent | v0.5.5 (2026-03-02) | 0 / 2 | Apache-2.0 |
| [muxel](https://github.com/ProjectHax/muxel) | GPU-accelerated desktop multiplexer, not a TUI, running coding agents in real terminal panes. | 32 | 4 | 5 | 257 | 2026-10-08 | Active | v0.2.8 (2026-10-06) | 1 / 0 | GPL-3.0 |
| [AGX](https://github.com/ramarlina/agx) | Keeps a persistent agent team on long objectives with wake-work-sleep checkpointing and human gates. | 31 | 3 | 4 | 0 | 2026-04-29 | Slow | app-v2.4.11 (2026-04-28) | 0 / 1 | None |
| [Fletch](https://github.com/fwdai/fletch) | Native macOS IDE isolating agents in separate repo clones under Seatbelt or Docker. | 29 | 2 | 1 | 1,744 | 2026-10-08 | Active | v0.8.9 (2026-10-08) | 0 / 0 | AGPL-3.0 |
| [Superagent](https://github.com/pungme/superagent-desktop) | Mac app giving Claude Code and Codex a browser, iOS Simulator, and phone monitoring. | 29 | 1 | 5 | 1,027 | 2026-10-08 | Active | v1.9.3-beta.20 (2026-10-08) | 0 / 0 | MIT |
| [Vibex](https://github.com/vibex-ai/vibex) _(new)_ | Rust desktop and mobile workbench for ACP agent sessions, Git worktrees, and scheduled runs. | 29 | 1 | 3 | 1,434 | 2026-10-08 | Active | v0.1.0-rc.7 (2026-09-29) | 0 / 0 | AGPL-3.0 |
| [OpenClawdex](https://github.com/alekseyrozh/openclawdex) _(new)_ | Electron desktop app running concurrent Claude Code and Codex sessions grouped by project. | 27 | 2 | 4 | 0 | 2026-04-23 | Slow | v0.6.1 (2026-04-23) | 0 / 1 | MIT |
| [JockeyUI](https://github.com/recailai/jockey) _(new)_ | Tauri desktop app running role-bound Claude Code and Codex agents over ACP. | 25 | 2 | 4 | 6 | 2026-10-07 | Active | — | 0 / 0 | MIT |
| [agent-session-manager-desktop](https://github.com/izll/agent-session-manager-desktop) | Cross-platform desktop GUI over tmux, with agent and shell tabs and ntfy phone push. | 23 | 3 | 4 | 601 | 2026-10-06 | Active | v1.1.23 (2026-10-06) | 0 / 0 | MIT |
| [octomux](https://github.com/ShreyPaharia/octomux) | Local agent dashboard with kanban fleet view, unified permission inbox, and in-app diff review. | 23 | 2 | 0 | 447 | 2026-08-27 | Recent | v1.5.2 (2026-08-17) | 0 / 0 | MIT |
| [AgentWire](https://github.com/dotdevdotdev/agentwire-dev) _(new)_ | Self-hosted web portal managing fleets of Claude Code agents across tmux sessions and worktrees. | 22 | 3 | 6 | 124 | 2026-08-15 | Recent | v1.69.0 (2026-08-11) | 4 / 0 | Apache-2.0 |
| [alas](https://github.com/mrmans0n/alas) | Native macOS workspace with terminals or chat panes per worktree, comment-based review, and merge. | 21 | 3 | 6 | 1,195 | 2026-10-08 | Active | v0.20.7 (2026-10-08) | 16 / 3 | MIT |
| [agent-squid](https://github.com/agent-squid/squid) | Browser UI with named lanes, context shared across agents, and a realtime quota gauge. | 18 | 2 | 0 | 454 | 2026-10-07 | Active | v0.1.5 (2026-08-28) | 0 / 0 | MIT |
| [Reemoat](https://github.com/rends-east/reemoat) | Self-hosted, end-to-end encrypted remote control for supervising any coding agent from anywhere. | 18 | 3 | 1 | 137 | 2026-10-04 | Active | v0.13.0 (2026-10-04) | 0 / 0 | AGPL-3.0 |
| [Pragma](https://github.com/pragma-sh/pragma) | Native desktop app running agent teams in parallel worktrees, with a prompt-to-PR task board. | 17 | 1 | 1 | 950 | 2026-10-08 | Active | github-copilot-cli-plugin-v1.1.1 (2026-10-04) | 4 / 2 | AGPL-3.0 |
| [ateam](https://github.com/clawnify/ateam) | Mac and iPhone app orchestrating Claude Code, OpenCode, and Codex crews in isolated worktrees. | 13 | 1 | 1 | 197 | 2026-10-06 | Active | v0.1.64 (2026-09-28) | 14 / 5 | Other |
| [EvoFlux](https://github.com/evoelsewhere/evoflux) | Local-first desktop workspace coordinating specialist AI agents across files, terminal, browser, Git, and memory. | 11 | 6 | 4 | 1,280 | 2026-10-08 | Active | v3.0.5 (2026-10-07) | 0 / 2 | Apache-2.0 |
| [MultiCC](https://github.com/lsjwzh/MultiCC) | Self-hosted workspace whose tasks and worktrees survive switching between Claude Code, Codex, and OpenCode. | 10 | 3 | 1 | 5,780 | 2026-10-06 | Active | v2.4.1 (2026-10-06) | 0 / 0 | MIT |

## Multi-Agent Swarms

Systems where multiple specialized agents actively coordinate, communicate, and delegate toward a shared goal.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [paperclip](https://github.com/paperclipai/paperclip) | Self-hosted platform where agents claim tickets on heartbeats under org charts, budgets, and approvals. | 98,800 | 202 | 16,686 | 1,888 | 2026-10-08 | Active | v2026.1005.0 (2026-10-06) | 2,866 / 3,359 | MIT |
| [ruflo](https://github.com/ruvnet/ruflo) | Meta-harness for deploying coordinated swarms and conversational multi-agent workflows, formerly claude-flow. | 74,138 | 38 | 8,811 | 1,666 | 2026-10-08 | Active | v3.55.0 (2026-10-07) | 692 / 382 | MIT |
| [OmO](https://github.com/code-yeongyu/oh-my-openagent) _(new)_ | Agent harness turning one prompt into a parallel graph of agents across models. | 69,897 | 321 | 5,743 | 10,056 | 2026-10-08 | Active | v5.1.27 (2026-10-08) | 698 / 476 | Other |
| [crewAI](https://github.com/crewAIInc/crewAI) | Framework for orchestrating autonomous AI agents that collaborate through roles, tools, and task delegation. | 59,469 | 337 | 8,663 | 308 | 2026-10-08 | Active | 1.15.25 (2026-10-07) | 228 / 345 | MIT |
| [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) _(new)_ | Claude Code plugin for multi-agent autopilot pipelines with planning, execution, and QA stages. | 39,695 | 150 | 3,550 | 1,620 | 2026-10-06 | Active | v5.6.2 (2026-10-06) | 4 / 4 | MIT |
| [buzz](https://github.com/block/buzz) | Nostr-relay channels where agents are members with their own keys and audit trails. | 35,675 | 112 | 4,717 | 1,486 | 2026-10-08 | Active | desktop-v0.5.27 (2026-10-06) | 1,632 / 1,960 | Apache-2.0 |
| [gastown](https://github.com/gastownhall/gastown) | Orchestrator scaling to 20-30 agents with git-backed issue tracking and a Bors-style merge queue. | 18,308 | 238 | 1,684 | 47 | 2026-07-23 | Recent | v1.2.1 (2026-06-06) | 375 / 132 | MIT |
| [Edict](https://github.com/cft0808/edict) _(new)_ | OpenClaw multi-agent system of twelve agents with review gates and a live Kanban dashboard. | 16,977 | 15 | 1,766 | 0 | 2026-05-06 | Slow | — | 10 / 4 | MIT |
| [Hive](https://github.com/aden-hive/hive) _(new)_ | Runtime where a Queen agent spawns parallel worker clones to run business processes. | 11,086 | 210 | 5,647 | 22 | 2026-09-14 | Active | v0.11.0 (2026-05-02) | 929 / 428 | Apache-2.0 |
| [oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) _(new)_ | Plugin for OpenCode whose Orchestrator dispatches specialist agents as parallel background tasks. | 9,401 | 128 | 577 | 1,762 | 2026-10-08 | Active | companion-v0.1.4 (2026-10-06) | 36 / 11 | MIT |
| [Munder Difflin](https://github.com/HarnessMD/munder-difflin) _(new)_ | Desktop harness running Claude Code, Codex and other CLIs as a mailbox-coordinated agent office. | 8,595 | 48 | 1,223 | 846 | 2026-10-08 | Active | v0.5.5 (2026-10-01) | 113 / 123 | MIT |
| [OpenRig](https://github.com/mvschwarz/openrig) | YAML-defined agent team running Claude Code and Codex as one persistent tmux system. | 6,095 | 44 | 448 | 2,261 | 2026-10-08 | Active | v0.6.7 (2026-10-08) | 91 / 25 | Apache-2.0 |
| [AgentTeams](https://github.com/agentscope-ai/AgentTeams) _(new)_ | Manager-Workers runtime where a manager agent orchestrates worker agents collaborating in Matrix rooms. | 5,718 | 50 | 706 | 172 | 2026-10-08 | Active | v1.2.4 (2026-09-20) | 200 / 44 | Apache-2.0 |
| [ClawTeam](https://github.com/HKUDS/ClawTeam) | Agents spawn their own teammates from one command, coordinating via file-based or P2P inboxes. | 5,537 | 23 | 765 | 0 | 2026-05-09 | Slow | v0.2.0 (2026-03-23) | 15 / 19 | MIT |
| [Raven](https://github.com/EverMind-AI/Raven) | Host agent planning complex tasks as a DAG and coordinating built-in and third-party agents. | 5,304 | 34 | 152 | 1,685 | 2026-10-08 | Active | v0.2.4 (2026-10-03) | 69 / 23 | Apache-2.0 |
| [Claude Octopus](https://github.com/nyldn/claude-octopus) _(new)_ | Plugin dispatching one task to multiple model CLIs with consensus gates and council deliberation. | 4,191 | 29 | 395 | 349 | 2026-10-08 | Active | v11.12.0 (2026-10-07) | 8 / 1 | MIT |
| [Clawith](https://github.com/dataelement/Clawith) _(new)_ | Open-source multi-agent platform where agents with persistent identity and workspaces delegate and collaborate. | 4,164 | 33 | 698 | 431 | 2026-08-25 | Recent | v1.11.4-fix.1 (2026-08-24) | 184 / 74 | Apache-2.0 |
| [SwarmForge](https://github.com/unclebob/swarm-forge) _(new)_ | Coordinates role-based agents in git worktrees and tmux sessions using durable handoffs. | 3,969 | 3 | 398 | 73 | 2026-09-04 | Recent | — | 27 / 26 | None |
| [pi-subagents](https://github.com/nicobailon/pi-subagents) _(new)_ | Extension that lets Pi delegate work to parallel foreground and background child agents. | 3,880 | 161 | 781 | 1,518 | 2026-10-08 | Active | v0.76.1 (2026-10-06) | 3 / 1 | MIT |
| [TinyAGI](https://github.com/TinyAGI/tinyagi) _(new)_ | Always-on agent teams with handoffs, fan-out and chat channels for Discord, WhatsApp and Telegram. | 3,621 | 10 | 505 | 0 | 2026-03-30 | Slow | v0.0.20 (2026-03-26) | 46 / 26 | MIT |
| [claude_codex_bridge](https://github.com/SeemSeam/claude_codex_bridge) | Workspace for mixing different vendors' CLI agents in one visible collaboration session. | 3,554 | 48 | 349 | 744 | 2026-10-08 | Active | v8.7.8 (2026-10-08) | 71 / 32 | Other |
| [squad](https://github.com/bradygaster/squad) | Human-led agent teams built on GitHub Copilot, with repo-native specialists, coordinator routing, and memory. | 3,257 | 53 | 505 | 664 | 2026-10-08 | Active | v1.0.1 (2026-10-04) | 102 / 5 | MIT |
| [myclaude](https://github.com/stellarlinkco/myclaude) _(new)_ | Installable modules and codeagent-wrapper that let Claude Code orchestrate Codex, Gemini and OpenCode backends. | 2,753 | 14 | 300 | 0 | 2026-05-04 | Slow | v6.8.2 (2026-03-03) | 4 / 3 | AGPL-3.0 |
| [CodeMachine](https://github.com/moazbuilds/CodeMachine-CLI) _(new)_ | Orchestration layer that runs coding agent CLIs through reusable multi-agent workflows with parallel execution. | 2,510 | 7 | 236 | 0 | 2026-02-25 | Slow | v0.8.0 (2026-02-02) | 10 / 0 | Apache-2.0 |
| [agentsmesh](https://github.com/AgentsMesh/AgentsMesh) | Remote AI workstations with PTY sandboxes and worktree isolation, coordinating across channels. | 2,364 | 11 | 246 | 16 | 2026-09-23 | Active | v0.44.8-nightly.20260923 (2026-09-23) | 10 / 13 | Other |
| [Agent Teams](https://github.com/777genius/agent-teams-ai) | Desktop app for directing coding-agent teams that coordinate via messaging, Kanban, and code review. | 2,239 | 27 | 370 | 2,473 | 2026-10-08 | Active | v2.17.6 (2026-10-08) | 23 / 14 | AGPL-3.0 |
| [Orkas](https://github.com/Orkas-AI/Orkas) | A commander agent decomposes goals and dispatches specialists with isolated skills and memory. | 2,156 | 10 | 88 | 279 | 2026-10-08 | Active | v2026.10.1 (2026-10-01) | 1 / 10 | MIT |
| [Zeroshot](https://github.com/the-open-engine/zeroshot) _(new)_ | Multi-agent graph where one agent implements, independent agents review, and failures loop to repair. | 1,932 | 13 | 183 | 271 | 2026-10-08 | Active | zeroshot-python-v10.10.1_1 (2026-10-06) | 14 / 4 | MIT |
| [Routa](https://github.com/phodal/routa) _(new)_ | Workspace and Kanban platform where coordinator, implementer and verifier agents deliver software. | 1,820 | 22 | 253 | 17 | 2026-08-13 | Recent | v0.19.0 (2026-06-22) | 17 / 3 | MIT |
| [scion](https://github.com/GoogleCloudPlatform/scion) | Testbed for orchestrating agents in parallel, isolated containers with dynamic coordination and normalized telemetry. | 1,733 | 30 | 272 | 2,205 | 2026-10-08 | Active | nightly-20261008 (2026-10-08) | 36 / 25 | Apache-2.0 |
| [ClawTeam-OpenClaw](https://github.com/win4r/ClawTeam-OpenClaw) _(new)_ | Swarm coordination where leader agents spawn CLI workers in git worktrees and tmux sessions. | 1,461 | 27 | 318 | 0 | 2026-07-03 | Slow | v0.3.0+openclaw2 (2026-07-03) | 2 / 2 | MIT |
| [multi-agent-shogun](https://github.com/yohey-w/multi-agent-shogun) | Shogun-karo-ashigaru hierarchy running up to 10 agents over tmux with no coordination API cost. | 1,423 | 11 | 292 | 2 | 2026-08-06 | Recent | v5.1.0 (2026-05-23) | 1 / 6 | MIT |
| [TAKT](https://github.com/nrslib/takt) _(new)_ | YAML-defined workflows coordinating multiple coding agents through plan, implement, review and fix steps. | 1,402 | 34 | 115 | 651 | 2026-10-08 | Active | — | 50 / 6 | MIT |
| [Claw-Empire](https://github.com/GreenSheep01201/claw-empire) _(new)_ | Local-first office simulator orchestrating Claude Code, Codex and Gemini CLIs as a virtual company. | 1,401 | 12 | 271 | 0 | 2026-03-16 | Slow | v2.0.4 (2026-03-12) | 3 / 2 | Apache-2.0 |
| [pi-subagents](https://github.com/tintinweb/pi-subagents) _(new)_ | Pi extension spawning parallel background sub-agents with steering, fleet view and scripted workflows. | 1,268 | 26 | 311 | 94 | 2026-09-03 | Recent | v0.19.0 (2026-08-27) | 81 / 61 | MIT |
| [Fusion](https://github.com/Runfusion/Fusion) | Multi-node orchestrator with a kanban board, plan-review-execute gates, per-task worktrees, and hierarchical missions. | 1,261 | 31 | 160 | 3,388 | 2026-10-06 | Active | v0.78.0-beta.7 (2026-09-25) | 45 / 39 | MIT |
| [Chorus](https://github.com/Chorus-AIDLC/Chorus) _(new)_ | Harness coordinating teams of coding agents and humans through proposals, task graphs, and verification. | 1,191 | 7 | 110 | 271 | 2026-10-07 | Active | v0.22.0 (2026-10-07) | 11 / 9 | AGPL-3.0 |
| [Mysti](https://github.com/DeepMyst/Mysti) _(new)_ | VS Code extension coordinating multiple coding agents through parallel opinions, handoffs and brainstorm debates. | 1,141 | 7 | 54 | 246 | 2026-10-05 | Active | v2.0.0-beta.1 (2026-10-03) | 2 / 0 | Apache-2.0 |
| [loki-mode](https://github.com/asklokesh/loki-mode) | PRD-to-deployment SDLC with 41 agents in 8 swarms and quality gates, source-available under BUSL-1.1. | 1,088 | 5 | 208 | 4,508 | 2026-10-08 | Active | v11.3.2 (2026-10-08) | 15 / 1 | Other |
| [SWE-AF](https://github.com/Agent-Field/SWE-AF) _(new)_ | Engineering-team runtime dispatching architect, coder, reviewer and tester agents from one API call. | 1,032 | 13 | 179 | 48 | 2026-10-08 | Active | — | 3 / 2 | Apache-2.0 |
| [Claude Code Agent Farm](https://github.com/Dicklesworthstone/claude_code_agent_farm) _(new)_ | Orchestrator running 20+ parallel Claude Code agents in tmux with lock-based coordination. | 921 | 1 | 108 | 2 | 2026-09-21 | Active | — | 0 / 0 | Other |
| [Agent Swarm](https://github.com/desplega-ai/agent-swarm) _(new)_ | Self-hosted lead agent delegating tasks to Claude Code or Codex workers in Docker containers. | 871 | 29 | 115 | 848 | 2026-10-08 | Active | v1.166.0 (2026-10-08) | 9 / 8 | MIT |
| [openswarm](https://github.com/openswarm-ai/openswarm) | Local mission-control center for launching, monitoring, approving, and coordinating parallel AI agents. | 824 | 0 | 170 | 1 | 2026-10-03 | Active | v1.8.0-exp.6 (2026-10-06) | 0 / 0 | Other |
| [Swarm](https://github.com/joelhooks/swarm-tools) _(new)_ | Decomposes tasks into parallel workers coordinated through Swarm Mail messaging and file reservations. | 745 | 10 | 65 | 0 | 2026-05-21 | Slow | claude-code-swarm-plugin@0.63.3 (2026-02-06) | 30 / 11 | None |
| [SwarmClaw](https://github.com/swarmclawai/swarmclaw) _(new)_ | Self-hosted runtime and dashboard for agent swarms with delegation, schedules, memory and CLI backends. | 688 | 14 | 140 | 0 | 2026-06-30 | Slow | v1.9.40 (2026-06-30) | 12 / 9 | MIT |
| [openteams](https://github.com/openteams-lab/openteams) _(new)_ | Local-first desktop app where coding agents share a session and hand off work. | 629 | 9 | 81 | 478 | 2026-10-04 | Active | v1.0.27-20261004145111 (2026-10-04) | 18 / 0 | Apache-2.0 |
| [Hive](https://github.com/tt-a1i/hive) _(new)_ | Browser workbench running an orchestrator and worker CLI agents as local PTY processes. | 564 | 3 | 73 | 4 | 2026-09-28 | Active | v0.6.0-alpha.0 (2026-05-13) | 23 / 17 | Other |
| [Maestro-Flow](https://github.com/catlog22/maestro-flow) _(new)_ | Multi-agent workflow orchestrator dispatching work across Claude, Codex, Gemini, and other CLIs. | 564 | 7 | 68 | 635 | 2026-10-08 | Active | v0.5.91 (2026-10-08) | 1 / 1 | None |
| [hcom](https://github.com/aannoo/hcom) | Lets Claude Code, Codex, and other agents message, watch, and spawn each other. | 562 | 28 | 85 | 188 | 2026-10-08 | Active | v0.7.28 (2026-10-06) | 19 / 7 | MIT |
| [pi-dynamic-workflows](https://github.com/QuintinShaw/pi-dynamic-workflows) _(new)_ | Pi extension that runs JavaScript workflows fanning tasks out to routed, worktree-isolated subagents. | 555 | 32 | 111 | 146 | 2026-10-06 | Active | v3.14.0 (2026-10-06) | 5 / 1 | MIT |
| [OpenCode Swarm](https://github.com/ZaxbyHub/opencode-swarm) _(new)_ | Plugin that turns one OpenCode session into an architect-led team of gated specialist agents. | 493 | 21 | 54 | 3,645 | 2026-10-08 | Active | v7.192.0 (2026-10-08) | 103 / 9 | MIT |
| [agent-kanban](https://github.com/saltbo/agent-kanban) | Leader-worker task board with cryptographic agent identity, for Claude Code, Codex, and Gemini CLI. | 486 | 1 | 44 | 100 | 2026-09-13 | Active | v1.13.4 (2026-05-19) | 13 / 1 | Other |
| [Maestro](https://github.com/josstei/maestro-orchestrate) _(new)_ | Extension orchestrating 39 specialist subagents across Gemini CLI, Claude Code, Codex and Qwen Code. | 465 | 4 | 37 | 0 | 2026-04-30 | Slow | v1.6.4 (2026-04-30) | 6 / 0 | Apache-2.0 |
| [OneManCompany](https://github.com/1mancompany/OneManCompany) _(new)_ | Agentic OS running hierarchical AI employee teams that delegate tasks and hold meetings. | 441 | 8 | 90 | 25 | 2026-08-26 | Recent | v0.7.73 (2026-05-09) | 13 / 2 | Apache-2.0 |
| [metaswarm](https://github.com/dsifry/metaswarm) _(new)_ | Orchestration framework where coordinators spawn 18 specialist agents with parallel review gates. | 419 | 1 | 54 | 0 | 2026-06-19 | Slow | v0.12.0 (2026-06-17) | 14 / 8 | MIT |
| [SupaConductor](https://github.com/Ibrahim-3d/orchestrator-supaconductor) _(new)_ | Claude Code plugin driving agents and evaluators through a plan, execute, evaluate, fix loop. | 381 | 3 | 39 | 36 | 2026-09-27 | Active | v3.8.0 (2026-09-27) | 2 / 0 | AGPL-3.0 |
| [AgentBridge](https://github.com/raysonmeng/agent-bridge) | Local MIT-licensed CLI keeping Claude Code and Codex as live peers in one session. | 374 | 1 | 60 | 1 | 2026-09-12 | Active | v0.1.31 (2026-09-12) | 16 / 33 | MIT |
| [Full Self Coding](https://github.com/NO-CHATBOT-REVOLUTION/full-self-coding) _(new)_ | Runs Claude Code or Gemini CLI agents on generated tasks in parallel Docker containers. | 368 | 2 | 38 | 0 | 2025-11-30 | Slow | — | 2 / 0 | None |
| [pi-workflow](https://github.com/AgwaB/pi-workflow) _(new)_ | Extension for Pi running multi-step workflows that coordinate subagent workers, with resumable runs. | 364 | 2 | 13 | 310 | 2026-09-29 | Active | v0.15.0 (2026-09-29) | 1 / 0 | MIT |
| [Open Orchestra](https://github.com/0xSero/orchestra) _(new)_ | Plugin for OpenCode whose hub orchestrator spawns and coordinates specialized worker agents. | 281 | 1 | 18 | 0 | 2026-01-02 | Slow | v0.2.3 (2025-12-23) | 1 / 1 | None |
| [OpenCode Ensemble](https://github.com/hueyexe/opencode-ensemble) _(new)_ | Plugin spawning parallel OpenCode teammate agents with messaging, a shared task board and worktrees. | 233 | 5 | 32 | 49 | 2026-09-18 | Active | v0.19.0 (2026-09-18) | 3 / 2 | MIT |
| [Stoneforge](https://github.com/stoneforge-ai/stoneforge) _(new)_ | Web dashboard and runtime where a Director plans, Workers code in worktrees, Stewards merge. | 191 | 4 | 29 | 0 | 2026-05-05 | Slow | v1.25.0 (2026-05-05) | 25 / 14 | Apache-2.0 |
| [OtoDock](https://github.com/OtoDock/oto-dock) | Self-hosted company OS where departments of agents delegate to each other, source-available under FSL-1.1. | 190 | 2 | 15 | 25 | 2026-10-07 | Active | v1.7.1 (2026-10-07) | 0 / 0 | Other |
| [Orca](https://github.com/VirtusLab/orca) _(new)_ | Scala library and CLI for scripting deterministic plan-implement-review flows across coding agents. | 180 | 3 | 16 | 280 | 2026-10-08 | Active | v0.1.10 (2026-09-24) | 5 / 1 | Apache-2.0 |
| [ORCH](https://github.com/oxgeneral/ORCH) | CLI runtime managing agents as typed teams with an explicit state machine and goals. | 170 | 3 | 17 | 25 | 2026-08-01 | Recent | v1.0.34 (2026-08-01) | 2 / 5 | MIT |
| [Outsourcerer](https://github.com/alexgreensh/outsourcerer) _(new)_ | Delegates jobs across Claude, Codex, Cursor and Devin, and convenes parallel model panels. | 170 | 4 | 13 | 264 | 2026-09-19 | Active | v0.13.4 (2026-09-19) | 0 / 5 | Other |
| [NXTG-Forge Orchestrator](https://github.com/nxtg-ai/forge-orchestrator) | Single Rust binary coordinating Claude Code, Codex, and Gemini CLI on one shared repo. | 162 | 1 | 20 | 49 | 2026-10-07 | Active | v1.6.2 (2026-10-07) | 2 / 1 | Other |
| [Claude MPM](https://github.com/bobmatnyc/claude-mpm) _(new)_ | Framework adding a PM agent that routes tasks to specialist agents in Claude Code. | 155 | 14 | 34 | 28 | 2026-08-31 | Recent | v6.5.83 (2026-07-27) | 1 / 1 | Other |
| [ccswarm](https://github.com/nwiizo/ccswarm) _(new)_ | Workflow engine running Claude Code and Codex agents through plan, quorum, implement, review, fix. | 153 | 3 | 15 | 8 | 2026-09-09 | Active | v0.10.1 (2026-09-09) | 0 / 14 | MIT |
| [Rovai AI](https://github.com/murray17/rovai-ai) | Desktop and web workspace where persistent Claude Code, Codex, OpenCode, and Pi agents collaborate. | 146 | 5 | 25 | 2,629 | 2026-10-08 | Active | v0.4.6 (2026-10-07) | 5 / 6 | MIT |
| [pi-task](https://github.com/mjasnikovs/pi-task) _(new)_ | Extension for Pi running a fixed refine-research-grill-compose-critique pipeline with parallel research sub-agents. | 142 | 3 | 12 | 1,442 | 2026-10-08 | Active | — | 0 / 0 | AGPL-3.0 |
| [kodo](https://github.com/ikamensh/kodo) | Directs agents through work cycles where a separate agent independently verifies each result. | 136 | 5 | 6 | 28 | 2026-09-26 | Active | — | 2 / 0 | MIT |
| [Pi Herdsman](https://github.com/boadij/pi-herdsman) _(new)_ | Orchestration layer coordinating Pi sessions through background agents, nested delegation, and manager supervision. | 133 | 3 | 10 | 253 | 2026-10-08 | Active | v0.22.0 (2026-10-08) | 7 / 4 | Apache-2.0 |
| [tutti](https://github.com/nutthouse/tutti) | Config-driven workflows that pass typed artifacts between agents, each working in its own worktree. | 131 | 2 | 11 | 1 | 2026-07-20 | Recent | v0.10.1 (2026-05-04) | 17 / 4 | MIT |
| [pi-teams](https://github.com/burggraf/pi-teams) _(new)_ | Extension for Pi that spawns teammate agents in terminal panes with shared task board. | 122 | 7 | 29 | 0 | 2026-04-03 | Slow | — | 4 / 6 | None |
| [pi-agent-teams](https://github.com/tmustier/pi-agent-teams) _(new)_ | Pi extension spawning teammate sessions with a shared task list, mailboxes and optional worktrees. | 110 | 2 | 19 | 0 | 2026-06-12 | Slow | v0.5.4 (2026-03-27) | 9 / 9 | MIT |
| [OpenAcme](https://github.com/sandydasari/openacme) _(new)_ | Local-first daemon running role-based agents that delegate work through a shared task board. | 89 | 2 | 8 | 2 | 2026-07-28 | Recent | @openacme/config@0.14.0 (2026-06-18) | 0 / 12 | MIT |
| [CompanyHelm](https://github.com/CompanyHelm/companyhelm) | Distributed orchestrator with task management and direct agent-to-agent conversations. | 77 | 1 | 11 | 0 | 2026-06-29 | Slow | — | 0 / 0 | MIT |
| [5dive](https://github.com/5dive-ai/5dive) | Agents on an org chart hand off work and escalate to humans via Telegram. | 66 | 5 | 11 | 1,869 | 2026-10-08 | Active | v0.82.0 (2026-10-08) | 12 / 0 | MIT |
| [AgentArea](https://github.com/agentarea/agentarea) _(new)_ | Self-hosted platform running role-based agent teams that hand off tasks under policy gates. | 65 | 6 | 10 | 296 | 2026-10-08 | Active | v0.1.0 (2026-10-01) | 82 / 1 | Apache-2.0 |
| [Batty](https://github.com/battysh/batty) _(new)_ | Control plane running architect, manager, and engineer agents in tmux with per-engineer git worktrees. | 57 | 1 | 8 | 2 | 2026-08-18 | Recent | v0.11.58 (2026-04-17) | 0 / 0 | MIT |
| [Agents Squads](https://github.com/agents-squads/squads-cli) _(new)_ | CLI running squads of lead, worker and verifier agents with git-backed memory. | 54 | 1 | 2 | 0 | 2026-07-07 | Slow | v0.9.0 (2026-07-07) | 54 / 0 | MIT |
| [Agon](https://github.com/AutoResearch-Factory/Agon) | Orchestrates scientist, coder, and auditor loops from research topic through proposal to experiment. | 54 | 2 | 5 | 71 | 2026-09-30 | Active | — | 1 / 0 | MIT |
| [Let Them Talk](https://github.com/Dekelelz/let-them-talk) _(new)_ | Local MCP broker where CLI agents message each other, assign tasks and run workflows. | 53 | 1 | 15 | 0 | 2026-04-18 | Slow | v5.5.4 (2026-04-18) | 1 / 0 | Other |
| [auto-co](https://github.com/NikitaDmitrieff/auto-co-meta) _(new)_ | Bash loop calling Claude Code every cycle to drive 14 role-based agents building software. | 51 | 1 | 9 | 0 | 2026-06-14 | Slow | v1.1.0 (2026-03-07) | 4 / 7 | MIT |
| [AgentHub](https://github.com/Dmatut7/AgentHub) _(new)_ | Message-router framework launching a coordinator agent and four executor agents in separate terminals. | 43 | 1 | 5 | 0 | 2026-02-03 | Slow | — | 1 / 0 | MIT |
| [open-dynamic-workflows](https://github.com/Suraj1235/open-dynamic-workflows) _(new)_ | Local daemon running model-written JavaScript workflows that fan out parallel agents with adversarial verification. | 43 | 1 | 5 | 0 | 2026-07-09 | Slow | — | 1 / 0 | MIT |
| [Kiro Team](https://github.com/requix/kiro-team) _(new)_ | Team-lead agent delegating plan tasks to parallel builder and validator subagents in Kiro CLI. | 42 | 1 | 6 | 0 | 2026-05-06 | Slow | v2.0.0 (2026-05-06) | 0 / 0 | MIT |
| [shire](https://github.com/victor36max/shire) | Persistent team workspaces with mailboxes and a shared drive for Claude Code, OpenCode, Pi. | 41 | 1 | 8 | 0 | 2026-05-03 | Slow | v1.0.47 (2026-05-03) | 1 / 1 | MIT |
| [TeamHero](https://github.com/sagiyaacoby/TeamHero) _(new)_ | Web dashboard and orchestrator agent managing Claude CLI agent teams via plans and approvals. | 38 | 2 | 7 | 0 | 2026-04-03 | Slow | v3.1.0 (2026-03-30) | 1 / 0 | MIT |
| [AI Dev Team](https://github.com/CelaenoIndustry/OpenSepia) _(new)_ | Cron-driven team of nine Claude Code agents that plan sprints, code, review, and test. | 35 | 0 | 7 | 0 | 2026-03-18 | Slow | — | 1 / 0 | MIT |
| [corellis](https://github.com/CorellisOrg/Corellis) | Multi-agent governance framework for OpenClaw, with goal decomposition, fleet-wide memory, and approval workflows. | 31 | 0 | 2 | 0 | 2026-04-13 | Slow | — | 4 / 0 | MIT |
| [orc](https://github.com/spencermarx/orc) | Framework reusing your existing CLI setup for planning, task decomposition, worktrees, and review. | 26 | 1 | 4 | 0 | 2026-04-01 | Slow | v0.2.13 (2026-03-30) | 0 / 0 | None |
| [CrewBee](https://github.com/CrewBeeLab/CrewBee) _(new)_ | Framework defining reusable agent teams with leader, executor, and reviewer roles for OpenCode. | 20 | 1 | 4 | 1 | 2026-07-25 | Recent | v0.1.24 (2026-05-14) | 0 / 0 | MIT |

## Autonomous Loop Runners

The "keep running until done" pattern — a single goal driven through a retry-until-verified loop.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [Ralph](https://github.com/snarktank/ralph) _(new)_ | Bash loop spawning fresh Amp or Claude Code instances until all PRD stories pass. | 21,932 | 4 | 2,095 | 0 | 2026-02-02 | Slow | — | 34 / 41 | MIT |
| [Loop Engineering](https://github.com/cobusgreyling/loop-engineering) | Designs repeatable coding-agent loops, with starters and a Loop Ready score. | 11,443 | 37 | 1,533 | 355 | 2026-10-08 | Active | v1.6.0 (2026-07-20) | 9 / 12 | MIT |
| [ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | Development loop for Claude Code that detects when the work is actually finished. | 9,671 | 26 | 726 | 9 | 2026-10-08 | Active | — | 8 / 8 | MIT |
| [ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) | Hat-based orchestration that keeps agents looping until done, implementing the Ralph Wiggum technique. | 3,168 | 35 | 300 | 7 | 2026-08-25 | Recent | v2.10.1 (2026-06-23) | 2 / 8 | MIT |
| [ralph-tui](https://github.com/subsy/ralph-tui) | Drives an agent through a task list autonomously, with a TUI to watch it. | 2,451 | 34 | 240 | 138 | 2026-09-03 | Recent | v0.12.0 (2026-05-13) | 33 / 9 | MIT |
| [Open Ralph Wiggum](https://github.com/Th0rgal/open-ralph-wiggum) _(new)_ | CLI looping a chosen coding agent on one prompt until a completion promise appears. | 1,899 | 18 | 144 | 0 | 2026-06-02 | Slow | v1.3.1 (2026-05-26) | 6 / 2 | MIT |
| [LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) | Long-running computer-use harness with fresh-context execution, independent auditing, and verified checkpoints. | 1,700 | 9 | 186 | 40 | 2026-08-20 | Recent | v0.1.7 (2026-08-20) | 26 / 17 | MIT |
| [ralphex](https://github.com/umputun/ralphex) | Executes implementation plans autonomously in fresh per-task sessions, with validation, retries, and multi-phase review. | 1,491 | 35 | 131 | 54 | 2026-10-05 | Active | v1.7.0 (2026-09-07) | 2 / 3 | MIT |
| [bernstein](https://github.com/sipyourdrink-ltd/bernstein) | Orchestrates 40+ CLI agents with zero-token coordination, verifying with tests and auto-committing. | 1,444 | 107 | 175 | 2,286 | 2026-10-08 | Active | v3.21.0 (2026-10-05) | 194 / 55 | Apache-2.0 |
| [Continuous Claude](https://github.com/AnandChowdhary/continuous-claude) _(new)_ | Loops Claude Code through PR, CI and merge cycles until the task is complete. | 1,383 | 2 | 93 | 6 | 2026-09-27 | Active | v0.24.9 (2026-09-27) | 2 / 0 | MIT |
| [Atomic](https://github.com/bastani-inc/atomic) _(new)_ | Runtime executing coding-agent workflows as graphs of parallel stages with checks and approval gates. | 850 | 29 | 116 | 3,109 | 2026-10-08 | Active | 0.9.28 (2026-10-08) | 24 / 6 | Other |
| [ralph-loop-agent](https://github.com/vercel-labs/ralph-loop-agent) _(new)_ | Library wrapping AI SDK tool loops in an outer loop until verifyCompletion passes. | 840 | 2 | 85 | 1 | 2026-09-16 | Active | — | 1 / 2 | Apache-2.0 |
| [fractal](https://github.com/plasma-ai/fractal) | Loops recursively delegating subtasks to child agents, with configurable depth, cost, and time limits. | 782 | 3 | 57 | 210 | 2026-09-17 | Active | — | 5 / 0 | Apache-2.0 |
| [Smart Ralph](https://github.com/tzachbon/smart-ralph) _(new)_ | Claude Code and Codex plugin looping spec tasks through phase-specific agents with fresh context. | 558 | 2 | 50 | 10 | 2026-09-02 | Recent | v4.0.0 (2026-02-20) | 8 / 7 | MIT |
| [Compound Product](https://github.com/snarktank/compound-product) _(new)_ | Turns daily reports into a PRD, then loops agents on tasks until all pass. | 542 | 1 | 66 | 0 | 2026-01-23 | Slow | — | 0 / 0 | None |
| [Ralph Wiggum for Cursor](https://github.com/agrimsingh/ralph-wiggum-cursor) _(new)_ | Loop runner re-running cursor-agent with fresh context until all task checkboxes are checked. | 496 | 1 | 64 | 0 | 2026-01-26 | Slow | — | 6 / 7 | None |
| [MartinLoop](https://github.com/Keesan12/martin-loop) | Caps spend, enforces policy, verifies output, and rolls back failures, leaving inspectable run receipts. | 409 | 3 | 68 | 492 | 2026-10-08 | Active | v0.8.2 (2026-10-08) | 0 / 0 | Apache-2.0 |
| [ArgusBot](https://github.com/waltstephen/ArgusBot) _(new)_ | Supervisor looping Codex CLI or Claude Code with reviewer and planner sub-agents until done. | 317 | 11 | 29 | 0 | 2026-04-26 | Slow | — | 0 / 0 | MIT |
| [Ralph Loop](https://github.com/PageAI-Pro/ralph-loop) _(new)_ | Shell loop that repeatedly runs a CLI agent in Docker Sandboxes until tasks complete. | 314 | 1 | 46 | 0 | 2026-06-28 | Slow | — | 3 / 0 | MIT |
| [Ralph Wiggum](https://github.com/fstandhartinger/ralph-wiggum) _(new)_ | Shell and PowerShell loop scripts rerunning an AI coding agent until spec criteria pass. | 301 | 0 | 29 | 0 | 2026-05-11 | Slow | — | 7 / 1 | MIT |
| [ordewell](https://github.com/ordewell/ordewell) | Turns a goal into editable tasks, each run as an evidence-checked agent session. | 189 | 2 | 15 | 507 | 2026-10-08 | Active | v0.7.2 (2026-10-07) | 42 / 0 | Apache-2.0 |
| [LoopTroop](https://github.com/looptroop-ai/LoopTroop) | LLM council plans, then Ralph-style loops retry failed units with fresh context via OpenCode. | 160 | 2 | 14 | 572 | 2026-10-08 | Active | v0.6.0 (2026-10-01) | 1 / 0 | MIT |
| [future-os](https://github.com/futuregene/future-os) | Multi-surface agent with a loop control plane and verification gates for 24h+ runs. | 111 | 5 | 13 | 1,447 | 2026-10-08 | Active | v1.2.1 (2026-09-24) | 0 / 2 | MIT |
| [Ralph](https://github.com/aymenfurter/ralph) _(new)_ | VS Code extension looping GitHub Copilot agent through PRD tasks until all are complete. | 110 | 3 | 26 | 0 | 2026-02-27 | Slow | v0.5.1 (2026-02-01) | 1 / 1 | MIT |
| [ralph-starter](https://github.com/rubenmarcus/ralph-starter) _(new)_ | CLI running autonomous coding-agent loops from GitHub, Linear and Notion specs with validation. | 108 | 1 | 9 | 0 | 2026-04-08 | Slow | v0.5.2 (2026-04-08) | 0 / 24 | MIT |
| [Pickle Rick for Claude Code](https://github.com/gregorydickson/pickle-rick-claude) _(new)_ | Ralph-loop toolkit that splits a PRD into tickets and drives isolated Claude Code workers. | 31 | 3 | 6 | 2,651 | 2026-10-08 | Active | v2.2.1 (2026-10-07) | 18 / 0 | Apache-2.0 |
| [LoopGate](https://github.com/rxdt/loopgate_harness) _(new)_ | Python harness looping CLI agents with fresh context, accepting only changes passing quality gates. | 23 | 12 | 18 | 54 | 2026-09-30 | Active | v0.1.3 (2026-09-09) | 13 / 2 | MIT |
| [Ralph](https://github.com/nitodeco/ralph) _(new)_ | CLI looping Cursor, Claude Code or Codex agents through PRD tasks until complete. | 21 | 1 | 2 | 6 | 2026-09-11 | Active | 0.16.2 (2026-09-11) | 0 / 0 | MIT |
| [toryo](https://github.com/JesseRWeigel/toryo) | Trust-based delegation chaining Claude Code, Aider, Gemini CLI, and Ollama, with quality ratcheting. | 12 | 2 | 1 | 4 | 2026-09-09 | Active | — | 2 / 1 | MIT |
| [Dex](https://github.com/francescoalemanno/dex) | Human-gated planning, multi-reviewer code review, and dead-end-aware research loops across 7 CLI backends. _(GitHub returned 404 at collection time; the repo may be deleted or private)_ | — | — | — | — | — | Unavailable | — | — | — |

## Autonomous Task Runners

Unattended agents driven by an external source — an issue queue, a work board, or a schedule — that run and sync state back without side-by-side supervision.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [OpenHands](https://github.com/OpenHands/OpenHands) | Self-hostable control center that runs its own agent or drives Claude Code and Codex. | 90,295 | 458 | 11,948 | 694 | 2026-10-08 | Active | v1.26.0 (2026-10-08) | 501 / 449 | MIT |
| [multica](https://github.com/multica-ai/multica) | Managed agents platform for assigning tasks, tracking progress, and compounding agent skills between runs. | 52,198 | 327 | 6,797 | 1,530 | 2026-10-08 | Active | v0.6.1 (2026-10-01) | 998 / 837 | Other |
| [symphony](https://github.com/openai/symphony) | Turns work into isolated autonomous runs, so teams manage work rather than supervising agents. | 27,602 | 9 | 2,873 | 24 | 2026-09-15 | Active | nightly (2026-09-15) | 0 / 8 | Apache-2.0 |
| [open-swe](https://github.com/langchain-ai/open-swe) | Runs Slack-, Linear-, or GitHub-triggered tasks in cloud sandboxes, ending in ticket-linked draft PRs. | 10,823 | 54 | 1,295 | 1,417 | 2026-10-08 | Active | desktop-v0.3.3-nightly.20261008144913 (2026-10-08) | 0 / 122 | MIT |
| [claude-code-action](https://github.com/anthropics/claude-code-action) | Anthropic's official GitHub Action that detects from context whether to answer, review, or implement. | 9,447 | 138 | 2,192 | 137 | 2026-10-08 | Active | v1.0.247 (2026-10-08) | 472 / 345 | MIT |
| [SuperPlane](https://github.com/superplanehq/superplane) | Turns routine backlog issues into review-ready pull requests by coordinating agents, CI, and approvals. | 7,713 | 71 | 649 | 1,131 | 2026-10-08 | Active | v0.30.0 (2026-07-27) | 100 / 351 | Other |
| [gh-aw](https://github.com/github/gh-aw) | Compiles Markdown agentic workflows into GitHub Actions YAML, read-only by default except sanitized safe-outputs. | 5,369 | 32 | 581 | 3,828 | 2026-10-08 | Active | v0.91.6 (2026-10-08) | 401 / 8 | MIT |
| [background-agents](https://github.com/ColeMurray/background-agents) | Triggers sandboxed agent sessions from Slack, GitHub, Linear, webhooks, or cron, opening attributed PRs. | 3,345 | 50 | 489 | 1,028 | 2026-10-08 | Active | — | 58 / 86 | MIT |
| [Autensa](https://github.com/crshdn/mission-control) _(new)_ | Self-hosted dashboard dispatching tasks to OpenClaw agents that research, build, test, and open PRs. | 2,148 | 18 | 439 | 0 | 2026-07-07 | Slow | v2.5.1 (2026-04-29) | 9 / 10 | MIT |
| [run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) | Google's official GitHub Action for Gemini CLI, triggered by events, schedules, or `@gemini-cli /review`. | 2,104 | 38 | 288 | 1 | 2026-08-21 | Recent | v0.1.22 (2026-04-24) | 62 / 23 | Apache-2.0 |
| [Paca](https://github.com/Paca-AI/paca) _(new)_ | Self-hosted Scrum board where AI agents and humans share sprints, tasks and automations. | 1,909 | 16 | 164 | 786 | 2026-10-08 | Active | v0.18.6 (2026-10-06) | 9 / 3 | Apache-2.0 |
| [Coding Agent Template](https://github.com/vercel-labs/coding-agent-template) _(new)_ | Web app running chosen coding agent CLIs on repository tasks inside Vercel Sandboxes. | 1,793 | 6 | 299 | 0 | 2026-02-12 | Slow | — | 5 / 9 | Other |
| [AgentConnect](https://github.com/agentconnect-md/agentconnect) _(new)_ | Runs role-based agents in Slack, Discord and GitHub, started by messages, issues or schedules. | 1,456 | 18 | 65 | 2,499 | 2026-10-08 | Active | v2.3.0 (2026-10-07) | 36 / 3 | Apache-2.0 |
| [centaur](https://github.com/paradigmxyz/centaur) | Multiplayer self-hosted agents with Slack-native conversations, Kubernetes sandboxes, shared tools, and durable workflows. | 1,361 | 60 | 256 | 561 | 2026-10-08 | Active | centaur-0.1.170 (2026-10-08) | 56 / 64 | Other |
| [codex-action](https://github.com/openai/codex-action) | OpenAI's official GitHub Action running Codex CLI headlessly in drop-sudo, unprivileged-user, or read-only sandboxes. | 1,260 | 10 | 177 | 4 | 2026-10-05 | Active | — | 37 / 46 | Apache-2.0 |
| [AgentRQ](https://github.com/agentrq/agentrq) _(new)_ | Task manager delegating scheduled and event-triggered tasks to agents running on enrolled machines. | 1,139 | 17 | 84 | 775 | 2026-10-08 | Active | v0.9.14 (2026-10-08) | 0 / 1 | AGPL-3.0 |
| [Optio](https://github.com/jonwiggins/optio) _(new)_ | Self-hosted Kubernetes orchestration turning tickets, schedules and events into coding-agent runs and PRs. | 1,062 | 11 | 121 | 569 | 2026-10-07 | Active | v0.14.0 (2026-10-07) | 4 / 5 | MIT |
| [agent-qa](https://github.com/vostride/agent-qa) | Runs natural-language web and mobile test suites in a self-healing loop with persistent memory. | 902 | 2 | 20 | 1 | 2026-08-03 | Recent | — | 0 / 0 | Other |
| [CAR (codex-autorunner)](https://github.com/Git-on-my-level/codex-autorunner) _(new)_ | Meta-harness running Codex, Hermes, OpenCode and other ACP agents through a ticket queue. | 875 | 6 | 73 | 27 | 2026-10-08 | Active | v2.2.3 (2026-06-25) | 3 / 3 | MIT |
| [OpenSwarm](https://github.com/Intrect-io/OpenSwarm) _(new)_ | Agentic CI/CD gate fanning reviewer subagents over a codebase, with an optional Linear daemon. | 859 | 5 | 150 | 499 | 2026-10-07 | Active | v0.24.4 (2026-09-29) | 0 / 4 | MIT |
| [cyrus](https://github.com/cyrusagents/cyrus) | Watches Linear, GitHub, GitLab, and Slack for assigned issues, giving each an isolated worktree. | 849 | 25 | 176 | 68 | 2026-10-07 | Active | v0.2.73 (2026-09-30) | 58 / 68 | Apache-2.0 |
| [Sleepless Agent](https://github.com/context-machine-lab/sleepless-agent) _(new)_ | Daemon queueing Slack and CLI tasks for Claude Code in isolated workspaces, opening PRs. | 833 | 4 | 110 | 0 | 2026-03-29 | Slow | v0.1.2 (2025-10-27) | 0 / 1 | MIT |
| [aeon](https://github.com/aeonfun/aeon) | Runs unattended on GitHub Actions, dispatching skills to six coding-agent harnesses behind one contract. | 767 | 55 | 278 | 474 | 2026-10-08 | Active | v0.1.0 (2026-07-09) | 0 / 1 | MIT |
| [Machinist](https://github.com/owainlewis/machinist) | Pulls tasks from trusted ticket queues into isolated Codex workspaces, keeping agents running unattended. | 493 | 2 | 94 | 448 | 2026-09-23 | Active | v0.4.0 (2026-08-31) | 10 / 17 | MIT |
| [Claude GitHub Webhook](https://github.com/claude-did-this/claude-hub) _(new)_ | Webhook-driven service running Claude Code in Docker containers for GitHub issue and PR mentions. | 487 | 2 | 46 | 0 | 2025-06-20 | Stale | v0.1.1 (2025-05-31) | 30 / 18 | None |
| [Claude Nights Watch](https://github.com/aniketkarne/ClaudeNightsWatch) _(new)_ | Daemon executing predefined task.md jobs through Claude CLI on usage-window expiry or schedule. | 369 | 5 | 45 | 1 | 2026-09-10 | Active | — | 3 / 0 | MIT |
| [no_human](https://github.com/no-human-ai/no_human) | Takes tickets to reviewed pull requests locally, with second-model review and human merging; MIT-licensed. | 331 | 12 | 32 | 1,537 | 2026-10-05 | Active | v0.2.4 (2026-09-17) | 55 / 43 | MIT |
| [sudocode](https://github.com/sudocode-ai/sudocode) _(new)_ | Git-native issue graph that runs Claude Code, Codex and Cursor agents in parallel. | 293 | 3 | 27 | 0 | 2026-03-18 | Slow | v0.2.0 (2026-03-18) | 10 / 2 | Apache-2.0 |
| [OpenASE](https://github.com/PacificStudio/openase) _(new)_ | Ticket-driven platform where agents claim tickets and run workflows on managed machines. | 268 | 2 | 28 | 1 | 2026-07-11 | Recent | v0.8.0 (2026-05-13) | 11 / 34 | Apache-2.0 |
| [Terragon](https://github.com/terragon-labs/terragon-oss) _(new)_ | Open-source snapshot of a cloud platform delegating tasks to sandboxed coding agents. | 260 | 1 | 43 | 0 | 2026-02-10 | Slow | — | 0 / 0 | Apache-2.0 |
| [remote-swe-agents](https://github.com/aws-samples/remote-swe-agents) | Serverless Lambda control plane with per-session EC2 workers, triggered by issue and PR activity. | 243 | 10 | 50 | 43 | 2026-10-06 | Active | — | 19 / 5 | MIT-0 |
| [Contrabass](https://github.com/junhoyeo/contrabass) | Terminal-first orchestrator for issue-driven agent runs from Linear, GitHub Issues, or a local board. | 224 | 7 | 28 | 47 | 2026-07-17 | Recent | v0.5.1 (2026-07-16) | 3 / 0 | Apache-2.0 |
| [kanban-md](https://github.com/antopolskiy/kanban-md) _(new)_ | File-based kanban board where multiple agents claim tasks, with a supervisor TUI. | 223 | 7 | 33 | 74 | 2026-10-05 | Active | v0.39.0 (2026-10-05) | 6 / 1 | MIT |
| [Orbi](https://github.com/orbi-build/orbi) | Turns ai-ready GitHub Issues into reviewed, merged PRs and tagged releases, using isolated worktrees. | 207 | 6 | 24 | 2,033 | 2026-10-08 | Active | v0.6.5 (2026-10-08) | 25 / 0 | AGPL-3.0 |
| [sortie](https://github.com/sortie-ai/sortie) | Turns tracker tickets into agent sessions; agent- and tracker-agnostic Go binary with SQLite persistence. | 196 | 6 | 20 | 1,579 | 2026-10-08 | Active | v1.26.0 (2026-10-01) | 47 / 0 | Apache-2.0 |
| [pi-dispatch](https://github.com/edgehero/pi-dispatch) _(new)_ | Self-hosted service running pi agent jobs from cron or forge events in disposable containers. | 178 | 2 | 10 | 893 | 2026-10-08 | Active | admin-v4.0.1 (2026-10-08) | 2 / 0 | MIT |
| [tsk-tsk](https://github.com/dtormoen/tsk-tsk) _(new)_ | Rust CLI queueing tasks to Claude Code or Codex agents in parallel sandbox containers. | 171 | 4 | 17 | 1 | 2026-07-29 | Recent | v0.10.9 (2026-07-29) | 1 / 6 | MIT |
| [20x](https://github.com/peakflo/20x) _(new)_ | Local-first desktop app assigning tracker tasks to coding agents in git worktrees. | 162 | 10 | 22 | 259 | 2026-10-08 | Active | v0.0.166 (2026-10-07) | 3 / 28 | MIT |
| [ABCA](https://github.com/aws-samples/sample-autonomous-cloud-coding-agents) _(new)_ | Sample AWS platform turning tasks from Slack, Linear, Jira or webhooks into pull requests. | 157 | 20 | 49 | 103 | 2026-10-08 | Active | — | 294 / 20 | MIT-0 |
| [Taskuary](https://github.com/ldbumble/taskuary) | Local-first work inbox that triages email, chat, and issue trackers into supervised coding-agent runs. | 137 | 14 | 35 | 2,075 | 2026-10-08 | Active | v0.3.7.14 (2026-10-07) | 4 / 0 | MIT |
| [lalph](https://github.com/tim-smart/lalph) | Orchestrator that takes its work from whichever issue source you point it at. | 132 | 4 | 15 | 0 | 2026-07-08 | Slow | v0.3.139 (2026-07-08) | 0 / 0 | MIT |
| [Code Conductor](https://github.com/ryanmac/code-conductor) _(new)_ | Runs parallel Claude Code agents that claim labelled GitHub issues in separate worktrees. | 112 | 1 | 11 | 0 | 2026-03-30 | Slow | v0.1.3 (2025-07-25) | 3 / 0 | MIT |
| [Wallfacer](https://github.com/changkun/wallfacer) _(new)_ | Local web platform that turns specs into board tasks run by agents in worktrees. | 112 | 2 | 14 | 600 | 2026-10-04 | Active | v0.6.1 (2026-09-26) | 0 / 0 | MIT |
| [Airut](https://github.com/airutorg/airut) _(new)_ | Runs Claude Code tasks in isolated containers, triggered by email, Slack or cron schedules. | 83 | 1 | 3 | 22 | 2026-10-08 | Active | v0.26.0 (2026-09-25) | 0 / 2 | MIT |
| [Claw-Kanban](https://github.com/GreenSheep01201/Claw-Kanban) _(new)_ | Kanban board routing tasks to Claude Code, Codex, Gemini and OpenCode agents by role. | 73 | 1 | 9 | 0 | 2026-02-15 | Slow | — | 0 / 0 | Apache-2.0 |
| [Hive](https://github.com/hivecommons/hive) _(new)_ | Go binary classifying repository issues and pull requests, then dispatching them to AI agents. | 64 | 21 | 43 | 6,485 | 2026-10-08 | Active | v5.145.0 (2026-10-08) | 59 / 14 | Apache-2.0 |
| [Claude Threads](https://github.com/anneschuth/claude-threads) _(new)_ | Bot running concurrent Claude Code sessions, one per Slack or Mattermost thread. | 42 | 9 | 16 | 170 | 2026-10-01 | Active | v1.39.3 (2026-10-01) | 7 / 3 | Apache-2.0 |
| [Vigilante](https://github.com/aliengiraffe/vigilante) _(new)_ | Turns GitHub issues into PRs by launching coding-agent CLIs in per-issue git worktrees. | 40 | 4 | 7 | 26 | 2026-09-08 | Active | main-nightly (2026-09-08) | 5 / 5 | Apache-2.0 |
| [oh-my-multica](https://github.com/xiaohei-info/oh-my-multica) _(new)_ | Delivery loop on Multica dispatching coding agents over a planned DAG with review gates. | 36 | 2 | 6 | 340 | 2026-10-08 | Active | v1.0.0 (2026-07-17) | 0 / 0 | MIT |
| [Tale](https://github.com/tale-project/tale) | Runs project-board tasks in persistent sandboxes with manager-agent delegation and deliverable review. | 32 | 7 | 5 | 1,467 | 2026-10-08 | Active | v0.5.77 (2026-10-07) | 162 / 116 | MIT |
| [NEEDLE](https://github.com/jedarden/NEEDLE) | Unattended runner dispatching queued beads to headless CLIs: Claude Code, Codex, OpenCode, Aider. | 28 | 2 | 3 | 2,785 | 2026-10-08 | Active | v0.6.32 (2026-10-07) | 5 / 1 | MIT |
| [Baton](https://github.com/mraza007/baton) _(new)_ | Polls GitHub Issues and runs concurrent Claude Code workers in isolated git worktrees. | 24 | 1 | 2 | 0 | 2026-03-27 | Slow | — | 1 / 0 | MIT |

## Agent Infrastructure & Primitives

Control planes, coordination protocols, harness adapters, and runtimes — the layer beneath your agents rather than the surface you work in.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | Workflow layer for Codex CLI adding skills, hooks, status surfaces, and team-style commands. | 33,490 | 92 | 2,542 | 846 | 2026-10-06 | Active | v0.21.8 (2026-10-06) | 2 / 0 | MIT |
| [Agent2Agent (A2A) Protocol](https://github.com/a2aproject/A2A) _(new)_ | Open JSON-RPC protocol for agent discovery and collaboration between opaque agentic applications. | 26,076 | 169 | 2,658 | 60 | 2026-10-07 | Active | v1.0.1 (2026-05-28) | 211 / 60 | Apache-2.0 |
| [Archon](https://github.com/coleam00/Archon) | Harness builder for deterministic coding workflows mixing agent steps, scripts, validation gates, and worktrees. | 23,645 | 72 | 3,492 | 1,956 | 2026-10-08 | Active | v0.11.1 (2026-09-25) | 242 / 7 | MIT |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Runs Hermes, LangChain Deep Agents, and OpenClaw inside NVIDIA OpenShell with managed inference. | 22,686 | 181 | 3,131 | 3,054 | 2026-10-08 | Active | ci-native-podman-e2e-2026-10-01 (2026-10-01) | 621 / 126 | Apache-2.0 |
| [openfang](https://github.com/RightNow-AI/openfang) | Open-source operating system for agents. | 18,216 | 62 | 2,291 | 0 | 2026-05-12 | Slow | v0.6.9 (2026-05-12) | 75 / 51 | Apache-2.0 |
| [AX](https://github.com/google/ax) | Google's declarative runtime for cluster-scale agent workloads using Kubernetes-style task specs and sandboxed workspaces. | 13,327 | 15 | 674 | 80 | 2026-09-27 | Active | v0.3.1 (2026-09-25) | 64 / 7 | Apache-2.0 |
| [PAL MCP](https://github.com/BeehiveInnovations/pal-mcp-server) _(new)_ | MCP server letting one coding CLI spawn other CLIs as subagents and consult models. | 11,776 | 30 | 1,037 | 0 | 2025-12-15 | Slow | v9.8.2 (2025-12-15) | 77 / 71 | Other |
| [omnigent](https://github.com/omnigent-ai/omnigent) | Meta-harness running Claude Code, Codex, and others in swappable sandboxes with policy enforcement. | 10,684 | 266 | 1,716 | 3,280 | 2026-10-08 | Active | v0.17.0 (2026-10-06) | 662 / 1,181 | Apache-2.0 |
| [Open Multi-Agent](https://github.com/open-multi-agent/open-multi-agent) | TypeScript runtime that splits a goal into a task DAG for specialized agents. | 6,990 | 58 | 2,437 | 243 | 2026-10-08 | Active | v1.21.1 (2026-10-04) | 4 / 0 | MIT |
| [AIOS](https://github.com/agiresearch/AIOS) _(new)_ | Agent operating system kernel scheduling LLM, memory, storage and tool requests from agents. | 6,455 | 48 | 919 | 12 | 2026-07-20 | Recent | v0.3.0 (2026-01-22) | 54 / 11 | Other |
| [Mission Control](https://github.com/builderz-labs/mission-control) _(new)_ | Self-hosted control plane dispatching tasks to agent runtimes and tracking runs, schedules, and spend. | 6,325 | 50 | 107 | 148 | 2026-09-22 | Active | v2.3.0 (2026-07-25) | 13 / 37 | MIT |
| [Agent Substrate](https://github.com/agent-substrate/substrate) _(new)_ | Kubernetes runtime that schedules, suspends and resumes agent sandboxes across shared worker pods. | 4,605 | 111 | 528 | 912 | 2026-10-08 | Active | v0.4.0 (2026-10-08) | 404 / 286 | Apache-2.0 |
| [acpx](https://github.com/openclaw/acpx) _(new)_ | Headless CLI managing persistent named ACP sessions across coding agents, with scripted multi-step flows. | 3,325 | 69 | 348 | 333 | 2026-10-07 | Active | v0.19.4 (2026-10-01) | 10 / 5 | MIT |
| [Omnara](https://github.com/omnara-ai/omnara) _(new)_ | Self-hostable managed agent platform running agents on any model and machine via API. | 2,899 | 18 | 233 | 274 | 2026-10-08 | Active | cluster-v0.2.1 (2026-10-08) | 5 / 18 | Apache-2.0 |
| [CompozyOS](https://github.com/compozy/compozy) _(new)_ | Daemon runtime supervising ACP agent CLIs with sessions, loops, cron triggers, and approvals. | 2,792 | 29 | 182 | 453 | 2026-10-08 | Active | v0.3.0-beta.31 (2026-10-07) | 10 / 2 | MIT |
| [AgentField](https://github.com/Agent-Field/agentfield) _(new)_ | Control plane that queues, retries and traces calls fanning out across many agents. | 2,606 | 60 | 431 | 458 | 2026-10-05 | Active | v0.1.142-rc.9 (2026-10-05) | 27 / 8 | Apache-2.0 |
| [MCP Agent Mail](https://github.com/Dicklesworthstone/mcp_agent_mail) _(new)_ | Mail-like FastMCP coordination layer giving coding agents identities, inboxes and advisory file reservations. | 2,198 | 1 | 229 | 21 | 2026-10-08 | Active | v0.3.2 (2026-04-16) | 0 / 0 | Other |
| [ClawManager](https://github.com/Yuan-lab-LLM/ClawManager) _(new)_ | Kubernetes-native control plane managing AI agent instances, teams, and shared resources across multiple runtimes. | 1,901 | 12 | 157 | 32 | 2026-09-30 | Active | v2026.10.2 (2026-10-02) | 15 / 8 | MIT |
| [NullHub](https://github.com/nullclaw/nullhub) _(new)_ | Single-binary management console that installs, supervises and monitors NullClaw agent instances and orchestration workflows. | 1,829 | 8 | 88 | 5 | 2026-10-03 | Active | v2026.5.29 (2026-05-29) | 8 / 2 | MIT |
| [sandbox-agent](https://github.com/rivet-dev/agents) | Daemon, HTTP/SSE API, and TypeScript SDK for driving six coding agents inside sandboxes. | 1,600 | 16 | 132 | 39 | 2026-10-08 | Active | v0.5.2 (2026-10-08) | 40 / 45 | Apache-2.0 |
| [Agentlas OS](https://github.com/agentlas-ai/Agentlas-OS) | Specialist-agent hub spinning up a temporary orchestrator per task, with A2A routing; formerly Hephaestus. | 1,580 | 4 | 111 | 606 | 2026-10-08 | Active | v1.2.59 (2026-10-08) | 2 / 0 | Apache-2.0 |
| [Agent Network Protocol (ANP)](https://github.com/agent-network-protocol/AgentNetworkProtocol) _(new)_ | Open protocol suite for agent identity, discovery, negotiation and secure messaging between agents. | 1,444 | 21 | 105 | 57 | 2026-10-01 | Active | v1.2 (2026-09-24) | 21 / 1 | Apache-2.0 |
| [Heym](https://github.com/heymrun/heym) | Self-hosted runtime for tool-using agents and OpenCode workflows, with sub-agents, MCP, approvals, and traces. | 1,429 | 25 | 95 | 632 | 2026-10-07 | Active | v0.0.128 (2026-10-07) | 3 / 2 | Other |
| [Gas City](https://github.com/gastownhall/gascity) _(new)_ | Orchestration-builder SDK whose controller loop runs multi-agent workflows on tmux, Kubernetes and other providers. | 1,347 | 180 | 441 | 1,956 | 2026-10-08 | Active | toolchain-llvm-22.1.8-slice-1 (2026-10-07) | 902 / 602 | MIT |
| [Sympozium](https://github.com/sympozium-ai/sympozium) _(new)_ | Kubernetes-native coordination layer with agent workflows, delegation, shared memory and CRD-defined policies. | 658 | 22 | 82 | 725 | 2026-10-08 | Active | v0.11.4 (2026-10-08) | 41 / 12 | MIT |
| [Claw Orchestrator](https://github.com/Enderfga/claw-orchestrator) _(new)_ | Headless runtime wrapping multiple coding CLIs as persistent sessions with fan-out, handoff and verification. | 586 | 13 | 102 | 212 | 2026-10-07 | Active | v7.9.0 (2026-10-07) | 0 / 1 | MIT |
| [foremerge](https://github.com/naw103/foremerge) | Coordination protocol above Git: agents declare intent first, rules flag collisions, verification gates acceptance. | 538 | 1 | 25 | 118 | 2026-10-04 | Active | v0.5.1 (2026-10-03) | 4 / 1 | Apache-2.0 |
| [Claudexor](https://github.com/razzant/claudexor) | Routes one coding thread across harnesses, rotating subscription profiles by quota, with cross-family review. | 497 | 9 | 53 | 1,935 | 2026-10-08 | Active | v3.22.0 (2026-10-06) | 74 / 1 | MIT |
| [Concord MCP](https://github.com/Get-Concord-AI/concord-mcp) | Coordination protocol for agents to claim work, detect edit collisions, and exchange durable messages. | 423 | 3 | 21 | 263 | 2026-10-07 | Active | v0.11.0 (2026-10-06) | 11 / 5 | MIT |
| [Cotal](https://github.com/Cotal-AI/Cotal) | Open pub/sub standard over NATS JetStream for coding agents sharing channels, presence, and messages. | 313 | 11 | 41 | 6,347 | 2026-10-08 | Active | v0.73.0 (2026-10-07) | 417 / 15 | Apache-2.0 |
| [guild](https://github.com/mathomhaus/guild) | Go binary over local SQLite for shared context, memory, task coordination, and hybrid search. | 302 | 7 | 45 | 7 | 2026-08-26 | Recent | v0.3.2 (2026-05-27) | 21 / 6 | Apache-2.0 |
| [OrcaReplay](https://github.com/Continuum-AI-Corp/OrcaReplay) | Records coding-agent runs for offline replay or forking onto a different model. | 283 | 8 | 68 | 265 | 2026-10-01 | Active | — | 0 / 1 | Apache-2.0 |
| [AIWG](https://github.com/jmagly/aiwg) | Deploys versioned agents, skills, rules, and governed workflows into coding agents' native project paths. | 220 | 4 | 35 | 1,821 | 2026-10-05 | Active | v2026.10.1 (2026-10-05) | 18 / 6 | MIT |
| [MCP Agent Mail (Rust)](https://github.com/Dicklesworthstone/mcp_agent_mail_rust) _(new)_ | Rust MCP server giving coding agents identities, inboxes, file reservations and an operator TUI. | 183 | 3 | 37 | 2,057 | 2026-10-08 | Active | v0.3.38 (2026-10-08) | 15 / 0 | Other |
| [NullBoiler](https://github.com/nullclaw/nullboiler) _(new)_ | Orchestration engine that schedules and dispatches work to agent workers using workflow graphs. | 183 | 6 | 26 | 18 | 2026-10-04 | Active | v2026.5.29 (2026-05-29) | 8 / 1 | MIT |
| [ClawFleet](https://github.com/clawfleet/ClawFleet) _(new)_ | Fleet manager running OpenClaw and Hermes agents in isolated Docker containers from one dashboard. | 174 | 2 | 13 | 0 | 2026-04-27 | Slow | v1.2.1 (2026-04-23) | 13 / 0 | MIT |
| [Farm Table](https://github.com/scion-frontiers/farmtable) _(new)_ | Task runtime giving agents dependency-aware task graphs with atomic claims and ready-task detection. | 123 | 2 | 16 | 500 | 2026-08-12 | Recent | — | 98 / 1 | Apache-2.0 |
| [Orchestrator](https://github.com/backnotprop/orchestrator) _(new)_ | CLI and skill that let one agent run other coding agents as background tasks. | 118 | 1 | 3 | 0 | 2026-07-10 | Recent | v0.1.0 (2026-07-09) | 2 / 1 | Other |
| [aweb](https://github.com/awebai/aweb) _(new)_ | Agent communication layer providing stable identity, durable mail and chat, and wake-up events. | 115 | 3 | 11 | 2,038 | 2026-10-08 | Active | skills-v0.2.14 (2026-08-19) | 12 / 1 | MIT |
| [Culture](https://github.com/agentculture/culture) _(new)_ | IRC-native shared workspace where specialized agents and humans coordinate through rooms, presence and roles. | 113 | 1 | 6 | 1 | 2026-08-23 | Recent | — | 37 / 0 | Apache-2.0 |
| [HAR](https://github.com/os-factory/har) _(new)_ | CLI and MCP harness giving each coding agent an isolated worktree and verification. | 98 | 7 | 12 | 335 | 2026-10-07 | Active | v1.16.0 (2026-10-07) | 4 / 1 | Apache-2.0 |
| [handoff](https://github.com/dazuiba/handoff) | Delegates tasks to DeepSeek, Codex, or Claude from inside Claude Code or Codex sessions. | 91 | 2 | 12 | 12 | 2026-08-02 | Recent | v4.0.2 (2026-08-02) | 1 / 0 | None |
| [sub-agents-skills](https://github.com/shinpr/sub-agents-skills) | Portable Markdown sub-agent definitions routing tasks to a backend, model, effort level, and permissions. | 91 | 2 | 17 | 61 | 2026-09-06 | Recent | v0.13.3 (2026-09-06) | 0 / 1 | MIT |
| [OpenHermit](https://github.com/HCF-STUDIOS/openhermit) _(new)_ | Platform hosting agent fleets with Postgres state, per-agent sandboxes and a gateway control plane. | 86 | 8 | 20 | 72 | 2026-10-05 | Active | — | 0 / 0 | MIT |
| [Coven](https://github.com/OpenCoven/coven) _(new)_ | Local Rust daemon launching and tracking project-scoped Codex, Claude Code and Copilot CLI sessions. | 70 | 9 | 26 | 976 | 2026-10-08 | Active | v0.4.8 (2026-10-03) | 33 / 2 | MIT |
| [Agents Council](https://github.com/MrLesk/agents-council) _(new)_ | MCP server letting Claude Code, Codex and Gemini sessions collaborate, with summonable agents. | 69 | 1 | 24 | 0 | 2026-02-22 | Slow | v0.4.0 (2026-01-18) | 1 / 0 | MIT |
| [Okto Nexus](https://github.com/OktoLabsAI/okto-nexus) _(new)_ | Local MCP coordination hub giving agent teams identities, messaging, handoffs, governance and dashboard. | 68 | 5 | 3 | 584 | 2026-10-06 | Active | v0.1.3 (2026-07-16) | 6 / 1 | Other |
| [ox](https://github.com/sageox/ox) | Go CLI recording persistent context once for recall across agents, machines, and teammates. | 63 | 22 | 20 | 604 | 2026-10-08 | Active | v0.20.0 (2026-10-01) | 120 / 13 | MIT |
| [agenttier](https://github.com/agenttier/agenttier) | Kubernetes runtime giving each agent a Pod and PVC sandbox behind a default-deny NetworkPolicy. | 55 | 2 | 5 | 5 | 2026-07-17 | Recent | v0.8.1 (2026-06-30) | 0 / 27 | Apache-2.0 |
| [Crewplane](https://github.com/crewplaneai/crewplane) | CLI-first control plane turning one-off coding-agent calls into reviewable, resumable Markdown workflows across agents. | 41 | 3 | 6 | 95 | 2026-10-06 | Active | v0.3.6 (2026-10-05) | 1 / 0 | Apache-2.0 |
| [neuralyzer](https://github.com/gintasz/neuralyzer) | Lets an agent wipe its context and rerun the first message, easing Ralph loops. | 40 | 1 | 2 | 0 | 2026-06-20 | Slow | @gintasz/opencode-neuralyzer@0.1.1 (2026-06-20) | 0 / 0 | MIT |
| [codecast](https://github.com/codecast-sh/codecast) | Surfaces local agent sessions in a triage inbox, with searchable history and line-level attribution. | 37 | 5 | 2 | 2,763 | 2026-10-07 | Active | v1.1.177 (2026-10-07) | 0 / 0 | MIT |
| [Agent Messaging Protocol](https://github.com/agentmessaging/protocol) | Open standard for agent-to-agent messaging with Ed25519-signed envelopes, cross-provider federation, and proven delivery. | 36 | 2 | 6 | 8 | 2026-10-04 | Active | — | 3 / 0 | Apache-2.0 |
| [crew](https://github.com/0xmmo/crew) _(new)_ | Shares live status and messages between concurrent Claude Code, Codex and OpenCode sessions. | 27 | 1 | 1 | 16 | 2026-09-13 | Active | — | 1 / 0 | MIT |
| [Mnemoverse](https://github.com/mnemoverse/mcp-memory-server) | Hosted MCP memory engine carrying decisions and lessons across sessions and tools; MIT-licensed server. | 26 | 2 | 4 | 115 | 2026-10-07 | Active | v0.15.0 (2026-10-06) | 9 / 2 | MIT |
| [LionClaw](https://github.com/moshthepitt/lionclaw) | Local control plane running durable, auditable coding-agent workers with explicit state, skills, and checkpoints. | 19 | 2 | 2 | 0 | 2026-07-06 | Slow | v0.8.0 (2026-06-10) | 4 / 8 | MIT |
| [aGiTrack](https://github.com/core-aix/agitrack) | Commits coding-agent turns to git, recording prompt, model, and token cost in the message. | 17 | 4 | 1 | 530 | 2026-10-08 | Active | v0.6.25 (2026-10-08) | 2 / 0 | Apache-2.0 |
| [skillfold](https://github.com/byronxlg/skillfold) | Declares skills in YAML and pins revisions in a lockfile for reproducible installs. | 15 | 1 | 1 | 48 | 2026-10-06 | Active | v2.8.0 (2026-09-26) | 0 / 0 | MIT |
| [agent-runbook](https://github.com/KnoxOps/agent-runbook) | Compiles YAML runbooks (loops, branching, parallelism) into SKILL.md files for Claude Code and Codex. | 13 | 1 | 0 | 8 | 2026-07-15 | Recent | — | 0 / 0 | Apache-2.0 |

## Personal Assistants

Always-on agents you reach over chat or a desktop app. They remember across sessions, run on their own schedule, and hand work off to tools and other agents — coding agents included, though the work isn't limited to code.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [openclaw](https://github.com/openclaw/openclaw) | Personal AI assistant that runs on any OS and any platform. | 391,468 | 369 | 82,299 | 40,565 | 2026-10-08 | Active | v2026.9.9 (2026-10-08) | 6,206 / 3,360 | MIT |
| [hermes-agent](https://github.com/NousResearch/hermes-agent) | Self-improving agent harness with persistent cross-session memory and auto-generated skill documents. | 252,012 | 398 | 54,367 | 35,687 | 2026-10-08 | Active | v0.21.6 (2026-10-08) | 14,648 / 33,139 | MIT |
| [nanobot](https://github.com/HKUDS/nanobot) | Lightweight self-hosted Python assistant with WebUI, tools, memory, MCP, and multi-agent workflows. | 48,875 | 387 | 8,617 | 1,358 | 2026-10-08 | Active | v0.3.5 (2026-09-15) | 216 / 593 | MIT |
| [CowAgent](https://github.com/zhayujie/CowAgent) _(new)_ | Open-source personal assistant running 24/7 across chat channels, with multi-agent teams and skills. | 47,285 | 151 | 10,373 | 1,533 | 2026-10-08 | Active | 2.2.0 (2026-09-30) | 20 / 35 | MIT |
| [QwenPaw](https://github.com/agentscope-ai/QwenPaw) | Personal assistant deployable locally or in the cloud, connecting to chat apps; formerly CoPaw. | 35,512 | 242 | 3,156 | 744 | 2026-10-08 | Active | v2.2.2-beta.4 (2026-09-30) | 662 / 380 | Apache-2.0 |
| [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) | Small, fast, fully autonomous assistant infrastructure written in Rust, deployable anywhere. | 32,943 | 416 | 4,957 | 1,201 | 2026-10-07 | Active | v0.8.5 (2026-09-05) | 571 / 399 | Apache-2.0 |
| [nanoclaw](https://github.com/nanocoai/nanoclaw) | Lightweight OpenClaw alternative running in containers, connecting to WhatsApp, Telegram, Slack, Discord, and Gmail. | 30,900 | 119 | 12,768 | 777 | 2026-10-06 | Active | v2026.10.0-rc.2 (2026-10-05) | 291 / 749 | MIT |
| [picoclaw](https://github.com/sipeed/picoclaw) | Tiny, fast assistant that can be deployed anywhere. | 30,019 | 226 | 4,451 | 3 | 2026-08-19 | Recent | v0.3.1 (2026-07-03) | 30 / 21 | MIT |
| [OpenWorker](https://github.com/andrewyng/openworker) | Desktop AI coworker for security reviews, cloud audits, and inbox triage, logging every action. | 18,478 | 30 | 2,620 | 668 | 2026-10-06 | Active | v0.3.1 (2026-10-05) | 226 / 284 | MIT |
| [rowboat](https://github.com/rowboatlabs/rowboat) | Open-source AI coworker with memory. | 18,002 | 17 | 1,796 | 656 | 2026-10-08 | Active | v1.0.5 (2026-09-30) | 93 / 104 | Apache-2.0 |
| [leon](https://github.com/leon-ai/leon) | Long-running open-source personal assistant with voice and text interfaces. | 17,560 | 21 | 1,473 | 508 | 2026-10-08 | Active | tcp-server_v2.0.0 (2026-02-19) | 95 / 18 | MIT |
| [ironclaw](https://github.com/nearai/ironclaw) | Agent OS written in Rust, focused on privacy, security, and extensibility. | 12,645 | 110 | 1,480 | 802 | 2026-09-10 | Active | ironclaw-v1.4.1 (2026-09-29) | 1,364 / 183 | Apache-2.0 |
| [Cloudflare OS](https://github.com/cloudflare/cloudflare-os) | Self-hostable company OS on Cloudflare Workers where agents do tasks and build sandboxed apps. | 11,279 | 22 | 1,345 | 435 | 2026-10-08 | Active | — | 86 / 50 | Apache-2.0 |
| [Coworker](https://github.com/accomplish-ai/coworker) | Open-source AI coworker that lives on your desktop; formerly accomplish. | 10,858 | 1 | 1,275 | 1 | 2026-08-13 | Recent | — | 13 / 0 | None |
| [nullclaw](https://github.com/nullclaw/nullclaw) | Fully autonomous assistant infrastructure written in Zig. | 8,109 | 91 | 940 | 72 | 2026-10-05 | Active | v2026.5.29 (2026-05-29) | 43 / 29 | MIT |
| [Octop](https://github.com/TencentCloud/Octop) | Self-hosted multi-user assistant with a built-in expert team working in parallel. | 7,986 | 45 | 960 | 637 | 2026-10-08 | Active | v1.0.2b6 (2026-10-04) | 360 / 348 | MIT |
| [lobsterai](https://github.com/netease-youdao/LobsterAI) | Desktop agent for data analysis, slides, docs, and web research. | 6,090 | 28 | 973 | 987 | 2026-10-06 | Active | 2026.9.23 (2026-09-23) | 150 / 41 | MIT |
| [OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Chat-app sidebar bots that are real local Claude or Codex agents behind approval gates. | 4,209 | 109 | 721 | 3,731 | 2026-10-08 | Active | v0.1.101 (2026-10-08) | 211 / 163 | Apache-2.0 |
| [Rakazo](https://github.com/elie222/rakazo) | Self-hosted platform for persistent AI teammates with memory, routines, and peer delegation. | 3,511 | 75 | 609 | 1,132 | 2026-10-08 | Active | v0.1.6 (2026-09-08) | 21 / 10 | Apache-2.0 |
| [MetaClaw](https://github.com/aiming-lab/MetaClaw) | Assistant that learns and evolves from conversation alone. | 3,458 | 16 | 449 | 0 | 2026-06-07 | Slow | v0.4.1 (2026-04-11) | 7 / 10 | MIT |
| [zclaw](https://github.com/tnm/zclaw) | 888 KiB personal assistant running on an ESP32, with GPIO, cron, and custom tools. | 2,235 | 4 | 193 | 0 | 2026-05-17 | Slow | v2.13.0 (2026-03-22) | 7 / 4 | MIT |
| [OpenAkita](https://github.com/openakita/openakita) _(new)_ | Multi-agent AI assistant with parallel agent delegation and hierarchical organization orchestration across chat apps. | 2,003 | 9 | 282 | 334 | 2026-09-24 | Active | v1.27.42 (2026-09-15) | 37 / 8 | AGPL-3.0 |
| [denchclaw](https://github.com/DenchHQ/DenchClaw) | Managed OpenClaw framework for CRM, sales automation, and outreach. | 1,658 | 359 | 125 | 0 | 2026-06-11 | Slow | v4.0.0 (2026-06-11) | 75 / 21 | MIT |
| [row-bot](https://github.com/siddsachar/row-bot) | Local-first desktop assistant with durable memory, scheduled tasks, and child agents; formerly Thoth. | 1,580 | 7 | 179 | 987 | 2026-10-07 | Active | v5.0.0 (2026-10-01) | 19 / 12 | Apache-2.0 |
| [Ouroboros](https://github.com/razzant/ouroboros) | General-purpose agent with durable identity and memory, reviewed self-modification, and multi-agent coordination. | 1,422 | 27 | 652 | 5,947 | 2026-10-05 | Active | v7.6.0 (2026-10-05) | 255 / 11 | MIT |
| [taOS](https://github.com/jaylfc/taOS) | Self-hosted agent OS keeping memory, chats, and files on your hardware, offline by default. | 556 | 2 | 42 | 2,390 | 2026-10-01 | Active | v1.0.0-beta.55 (2026-10-02) | 289 / 22 | AGPL-3.0 |
| [ductor](https://github.com/PleasePrompto/ductor) _(new)_ | Messenger-driven runtime running parallel CLI agent sessions and delegating work between sub-agents. | 457 | 16 | 89 | 83 | 2026-07-23 | Recent | v0.20.1 (2026-07-23) | 19 / 41 | MIT |
| [OwnPilot](https://github.com/ownpilot/OwnPilot) _(new)_ | Self-hosted personal assistant with agent crews that orchestrates Claude Code, Codex and Gemini CLI. | 426 | 4 | 66 | 88 | 2026-09-08 | Active | v0.8.3 (2026-06-23) | 3 / 2 | MIT |
| [OpenInstinct](https://github.com/Merit-Systems/OpenInstinct) | iMessage assistant that drives a real browser for chores, tickets, and groceries; self-hosted. | 425 | 6 | 75 | 497 | 2026-10-05 | Active | — | 1 / 24 | MIT |
| [rho](https://github.com/mikeyobrien/rho) | Assistant that stays running, remembers across sessions, and checks in unprompted. | 372 | 4 | 29 | 0 | 2026-05-26 | Slow | v0.1.12 (2026-03-15) | 0 / 0 | MIT |
| [Tiny Claw](https://github.com/warengonzaga/tinyclaw) _(new)_ | Bun-native personal AI companion that delegates tasks to sub-agents coordinating through a blackboard. | 293 | 2 | 40 | 0 | 2026-02-25 | Slow | v2.0.0 (2026-02-22) | 6 / 3 | GPL-3.0 |
| [lorca](https://github.com/egoist/lorca) | E2E-encrypted chat for personal agent bots that hand work to each other. | 251 | 1 | 21 | 322 | 2026-10-08 | Active | cli-v0.1.10 (2026-10-04) | 32 / 16 | GPL-3.0 |
| [iva](https://github.com/smixs/iva-agent) | Telegram assistant turning messages, voice notes, and photos into an Obsidian-compatible markdown vault; MIT. | 233 | 10 | 55 | 2,218 | 2026-10-08 | Active | v0.4.14 (2026-10-08) | 9 / 2 | MIT |
| [Comma](https://github.com/AFK-surf/Comma) | Sessionless personal agent that breaks goals into tasks and keeps working; self-hostable under AGPL-3.0. | 216 | 1 | 15 | 5 | 2026-10-02 | Active | — | 1 / 1 | AGPL-3.0 |
| [Overlay](https://github.com/LayerNorm/overlay-web) | Open-source, provider-neutral workspace where humans and agents share context and you delegate repeatable work. | 183 | 2 | 23 | 1,365 | 2026-10-06 | Active | v0.1.0-rc.1 (2026-07-16) | 0 / 14 | AGPL-3.0 |
| [PersonalJarvis](https://github.com/PersonalJarvis/PersonalJarvis) | Desktop voice and chat assistant running Claude Code, Codex, and others in Git worktrees. | 153 | 3 | 58 | 4,705 | 2026-10-08 | Active | v2.9.0 (2026-10-05) | 22 / 56 | Apache-2.0 |
| [lemon](https://github.com/z80dev/lemon) | Local-first assistant and coding-agent runtime. | 132 | 3 | 17 | 680 | 2026-09-07 | Recent | v2026.08.1 (2026-08-19) | 31 / 4 | MIT |
| [automata](https://github.com/sentientwave/automata) | Matrix-native workspace using Temporal-backed durable workflows so long tasks survive restarts. | 114 | 1 | 13 | 3 | 2026-09-29 | Active | v0.2.16-ce (2026-09-29) | 0 / 0 | Other |
| [ghostclaw](https://github.com/b1rdmania/ghostclaw) | AI that lives on your computer and does things for you. | 92 | 33 | 9 | 0 | 2026-05-03 | Slow | v0.8.2 (2026-05-03) | 0 / 0 | MIT |
| [assistant](https://github.com/kcosr/assistant) | Panel-based assistant whose plugins share one workspace of notes, lists, and objects. | 89 | 1 | 9 | 131 | 2026-10-06 | Active | v0.18.2 (2026-04-06) | 0 / 0 | None |
| [Hivekeep](https://github.com/MarlBurroW/hivekeep) | Self-hosted team of specialized agents that delegate, remember, and build their own tools; MIT. | 68 | 7 | 16 | 89 | 2026-09-17 | Active | v1.10.0 (2026-07-29) | 7 / 19 | MIT |
| [jelly](https://github.com/dctanner/jelly) | Local-first multi-bot system running persistent agents in project directories from one VM. | 57 | 1 | 6 | 24 | 2026-10-07 | Active | — | 0 / 0 | MIT |
| [goated](https://github.com/Endgame-Labs/goated) _(new)_ | Always-on Go daemon bridging Slack and Telegram to Claude Code or Codex, spawning subagents. | 45 | 10 | 9 | 52 | 2026-10-04 | Active | v0.2.2 (2026-10-04) | 2 / 0 | MIT |
| [lucinate](https://github.com/lucinate-ai/lucinate) | Terminal-native chat client for OpenClaw, Hermes, Ollama, and OpenAI-compatible providers, with cron management. | 12 | 4 | 4 | 38 | 2026-10-04 | Active | v1.25.0 (2026-08-02) | 17 / 2 | Apache-2.0 |

## Resting

Projects the source list had moved to its resting watchlist (no recent push as of 2026-07-28). Status below is recomputed for this snapshot.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [vibe-kanban](https://github.com/BloopAI/vibe-kanban) | Kanban board for managing AI coding agents. | 28,296 | 64 | 3,034 | 10 | 2026-09-19 | Active | v0.1.44-20260424091429 (2026-04-24) | 389 / 155 | Apache-2.0 |
| [1code](https://github.com/21st-dev/1code) | Orchestration layer for Claude Code and Codex. | 5,581 | 17 | 611 | 0 | 2026-02-24 | Archived | v0.0.84 (2026-03-06) | 26 / 19 | Apache-2.0 |
| [CodexMonitor](https://github.com/Dimillian/CodexMonitor) | Orchestrates multiple Codex agents across local workspaces. | 4,345 | 73 | 414 | 0 | 2026-03-26 | Slow | v0.7.67 (2026-03-24) | 79 / 15 | MIT |
| [ralphy](https://github.com/michaelshimeles/ralphy) | Bash script that loops Claude Code, Codex, and others until the task is done. | 2,977 | 23 | 365 | 0 | 2026-02-05 | Slow | — | 26 / 17 | None |
| [antfarm](https://github.com/snarktank/antfarm) | Builds a team of agents in OpenClaw with one command. | 2,495 | 7 | 451 | 0 | 2026-02-26 | Slow | v0.5.1 (2026-02-15) | 45 / 67 | MIT |
| [cashclaw](https://github.com/moltlaunch/cashclaw) | Autonomous agent that takes work, does it, gets paid, and improves at it. | 1,222 | 1 | 229 | 0 | 2026-03-14 | Slow | — | 49 / 5 | MIT |
| [clawe](https://github.com/getclawe/clawe) | Multi-agent coordination system, like Trello for OpenClaw agents. | 748 | 2 | 83 | 0 | 2026-02-23 | Slow | v1.0.4 (2026-02-22) | 4 / 2 | AGPL-3.0 |
| [opengoat](https://github.com/marian2js/opengoat) | Builds organizations of OpenClaw agents coordinating across Codex, Claude Code, Cursor, and OpenCode. | 425 | 1 | 54 | 0 | 2026-04-12 | Slow | v2026.4.12-2 (2026-04-12) | 6 / 0 | MIT |
| [subtask](https://github.com/zippoxer/subtask) | Claude Skill that runs tasks through subagents in git worktrees. | 338 | 1 | 30 | 0 | 2026-04-27 | Slow | v0.2.0 (2026-01-29) | 4 / 1 | MIT |
| [lettabot](https://github.com/letta-ai/lettabot) | Personal assistant that remembers everything. | 326 | 21 | 83 | 0 | 2026-05-03 | Archived | v0.2.0-alpha.13 (2026-03-12) | 76 / 8 | Apache-2.0 |
| [mercury](https://github.com/Michaelliv/mercury) | Personal AI assistant that lives where you chat. | 143 | 1 | 9 | 0 | 2026-03-29 | Archived | v0.5.0-exp.19 (2026-03-29) | 3 / 0 | None |
| [babyagi3](https://github.com/yoheinakajima/babyagi3) | Minimal AI agent that you configure once and then run through natural language. | 130 | 2 | 14 | 0 | 2026-02-08 | Slow | — | 0 / 2 | MIT |
| [wreckit](https://github.com/mikehostetler/wreckit) | Runs the Ralph Wiggum loop over your roadmap. | 130 | 2 | 11 | 0 | 2026-02-08 | Slow | — | 3 / 15 | MIT |
| [gnap](https://github.com/farol-team/gnap) | Git-native protocol that coordinates agents via a shared repo task board, without an orchestrator. | 86 | 2 | 7 | 0 | 2026-03-17 | Slow | — | 2 / 0 | MIT |
| [swarm-protocol](https://github.com/phuryn/swarm-protocol) | Headless MCP coordination for claiming work, detecting file conflicts, heartbeats, and session handoffs. | 55 | 2 | 8 | 0 | 2026-03-15 | Slow | — | 5 / 1 | MIT |
| [wit](https://github.com/amaar-mc/wit) | Locks functions instead of files using Tree-sitter, warning agents of conflicts before they write. | 46 | 1 | 3 | 0 | 2026-03-27 | Slow | v0.1.3 (2026-03-27) | 10 / 0 | MIT |

## Adjacent frameworks: general-purpose agent SDKs

General-purpose agent SDKs and frameworks, not limited to coding. Included because many teams use them to build multi-agent orchestration.

| Project | What it does | Stars | Contributors | Forks | Commits (90d) | Last commit | Status | Latest release | Open issues / PRs | License |
|---|---|--:|--:|--:|--:|---|---|---|--:|---|
| [DeerFlow](https://github.com/bytedance/deer-flow) _(new)_ | Open-source super agent harness orchestrating sub-agents, memory, sandboxes, and skills for long-horizon tasks. | 83,528 | 451 | 11,602 | 1,412 | 2026-10-08 | Active | v2.1.0 (2026-09-24) | 519 / 382 | MIT |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Multi-agent framework that simulates a software company of role-playing agents. | 70,779 | 116 | 9,000 | 0 | 2026-01-21 | Slow | v0.8.2 (2025-03-09) | 12 / 130 | MIT |
| [AutoGen](https://github.com/microsoft/autogen) | Multi-agent conversation framework; Microsoft's successor is Agent Framework. | 61,312 | 440 | 9,275 | 0 | 2026-04-06 | Slow | python-v0.7.5 (2025-09-30) | 558 / 542 | CC-BY-4.0 |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Graph-based runtime for stateful, long-running agents with checkpoints and human review. | 42,912 | 279 | 7,296 | 149 | 2026-10-08 | Active | cli==0.4.33 (2026-10-07) | 566 / 233 | MIT |
| [Agno](https://github.com/agno-agi/agno) | Python framework for agents, teams, and workflows, with memory and tool use. | 42,616 | 439 | 6,113 | 347 | 2026-10-08 | Active | v3.1.2 (2026-10-08) | 867 / 967 | Apache-2.0 |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | Multi-agent framework where role-playing agents build software through a virtual company. | 34,469 | 17 | 4,322 | 3 | 2026-07-24 | Recent | v2.2.0 (2026-03-23) | 54 / 28 | Apache-2.0 |
| [AgentScope](https://github.com/agentscope-ai/agentscope) | Multi-agent framework for agents that communicate through messages and tools. | 32,915 | 158 | 3,619 | 327 | 2026-10-08 | Active | v2.0.9 (2026-09-28) | 324 / 243 | Apache-2.0 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | OpenAI's lightweight SDK for agents with handoffs, guardrails, and tracing. | 29,916 | 398 | 4,853 | 791 | 2026-10-08 | Active | v0.23.1 (2026-10-02) | 6 / 2 | MIT |
| [Mastra](https://github.com/mastra-ai/mastra) | TypeScript framework for agents, workflows, and tool integrations. | 28,645 | 456 | 2,941 | 4,225 | 2026-10-08 | Active | @mastra/core@1.75.0 (2026-10-07) | 297 / 263 | Other |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | Microsoft SDK that adds AI agents and orchestration to C#, Python, and Java apps. | 28,635 | 401 | 4,816 | 62 | 2026-10-07 | Active | dotnet-1.81.0 (2026-10-06) | 128 / 218 | MIT |
| [Swarm](https://github.com/openai/swarm) _(new)_ | Educational Python framework coordinating multiple agents through handoffs, now replaced by OpenAI Agents SDK. | 22,044 | 14 | 2,340 | 0 | 2026-04-15 | Slow | — | 28 / 8 | MIT |
| [Google ADK](https://github.com/google/adk-python) | Google's Agent Development Kit for hierarchical multi-agent systems and workflows. | 21,749 | 423 | 4,119 | 1,415 | 2026-10-08 | Active | v2.11.0 (2026-10-02) | 215 / 196 | Apache-2.0 |
| [OWL](https://github.com/camel-ai/owl) _(new)_ | Multi-agent workforce framework built on CAMEL-AI for general real-world task automation. | 20,153 | 39 | 2,295 | 8 | 2026-10-05 | Active | — | 89 / 30 | None |
| [CAMEL](https://github.com/camel-ai/camel) | Multi-agent framework for studying and building cooperative, role-playing agent societies. | 17,827 | 231 | 2,107 | 55 | 2026-10-05 | Active | v0.2.91a7 (2026-09-03) | 259 / 270 | Apache-2.0 |
| [Eigent](https://github.com/eigent-ai/eigent) | Open-source desktop app that runs a team of agents to complete multi-step work. | 15,477 | 71 | 1,841 | 178 | 2026-10-08 | Active | v1.0.5 (2026-09-25) | 165 / 91 | Apache-2.0 |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Microsoft SDK for single and multi-agent workflows in .NET and Python. | 14,018 | 282 | 2,447 | 935 | 2026-10-08 | Active | python-1.21.0 (2026-10-08) | 577 / 205 | MIT |
| [Strands Agents](https://github.com/strands-agents/harness-sdk) | AWS's Strands Agents SDK: model-driven agents with multi-agent patterns such as swarms and graphs. | 8,743 | 316 | 1,343 | 727 | 2026-10-08 | Active | harness-cli/v0.2.0 (2026-10-08) | 573 / 415 | Apache-2.0 |
| [Agent Squad](https://github.com/2FastLabs/agent-squad) _(new)_ | Framework routing user queries to specialized agents, with a supervisor agent coordinating teams. | 7,790 | 29 | 743 | 57 | 2026-10-02 | Active | typescript_1.1.5 (2026-09-23) | 33 / 81 | Apache-2.0 |
| [Swarms](https://github.com/kyegomez/swarms) | Python framework for enterprise multi-agent orchestration across workflows and tools. | 7,237 | 55 | 1,038 | 301 | 2026-10-08 | Active | 6.8.1 (2024-12-27) | 128 / 170 | Apache-2.0 |
| [ROMA](https://github.com/sentient-agi/ROMA) _(new)_ | Meta-agent framework decomposing tasks recursively into parallel subtasks with planner, executor, aggregator and verifier. | 5,179 | 3 | 774 | 0 | 2026-02-16 | Slow | v0.2.0-beta (2025-10-22) | 13 / 15 | None |
| [AG2](https://github.com/ag2ai/ag2) _(new)_ | Python framework for building agents and coordinating multiple agents via a hub-and-channels Network. | 4,984 | 426 | 740 | 226 | 2026-10-08 | Active | v1.1.2 (2026-10-03) | 19 / 30 | Apache-2.0 |
| [Agency Swarm](https://github.com/VRSEN/agency-swarm) _(new)_ | Python multi-agent framework with role-based agents and directional communication flows, extending OpenAI Agents SDK. | 4,594 | 26 | 1,061 | 111 | 2026-10-08 | Active | v1.11.0 (2026-08-03) | 3 / 5 | MIT |
| [Docker Agent](https://github.com/docker/docker-agent) _(new)_ | CLI plugin running teams of YAML-defined agents that delegate tasks and use MCP tools. | 4,225 | 104 | 494 | 2,488 | 2026-10-08 | Active | v1.149.0 (2026-10-07) | 26 / 19 | Apache-2.0 |
| [agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) _(new)_ | Python multi-agent framework with collaborative pattern components like PEER and DOE. | 2,378 | 61 | 461 | 171 | 2026-07-28 | Recent | v0.0.19 (2025-11-17) | 134 / 2,451 | Apache-2.0 |
| [Agency Orchestrator](https://github.com/jnMetaCode/agency-orchestrator) _(new)_ | YAML DAG orchestrator running teams of 276 expert-persona agents in parallel across LLM providers. | 2,342 | 2 | 309 | 435 | 2026-10-08 | Active | desktop-v0.4.12 (2026-10-08) | 4 / 0 | Apache-2.0 |
| [KiwiQ AI Platform](https://github.com/rcortx/kiwiq) _(new)_ | Python platform executing JSON-defined agent workflows as LangGraph graphs on Prefect with human-in-the-loop. | 2,188 | 1 | 240 | 0 | 2026-04-13 | Slow | — | 6 / 1 | Apache-2.0 |
| [Swarms Rust](https://github.com/The-Swarm-Corporation/swarms-rs) _(new)_ | Rust framework for building LLM agents and orchestrating multi-agent systems. | 181 | 8 | 57 | 16 | 2026-10-03 | Active | — | 16 / 29 | Apache-2.0 |
| [Network-AI](https://github.com/Jovancoding/Network-AI) _(new)_ | TypeScript multi-agent orchestrator with locked shared blackboard, guardrails, budgets and adapters for 32 frameworks. | 78 | 2 | 13 | 45 | 2026-10-05 | Active | v5.15.4 (2026-09-29) | 4 / 0 | MIT |

## Methodology

**Source.** Projects start from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) (CC0-1.0). Projects marked _(new)_ were found by GitHub search, the source's own references, and web search, and were not in that list. Each new project had to meet the same scope: it orchestrates, supervises, or coordinates several AI agents or agent sessions; it is open source or source-available; and it is active. Adjacent frameworks are general-purpose agent SDKs. They are listed separately because many teams use them for multi-agent orchestration.

**Data.** GitHub REST API through the GitHub CLI, collected on the date shown above (UTC). Repository figures refer to the default branch. Statuses and day counts are judged as of each project's collection date.

| Column | Definition |
|---|---|
| Stars, Forks, Language | Repository metadata. |
| License | The SPDX id GitHub detects. Check the license file before reuse; detection can be wrong. "None" means no license was detected, so default copyright applies. |
| Contributors | GitHub accounts (type `User`) with at least one commit on the default branch. Bots are excluded and counted separately in `data/metrics.json`. |
| Commits (90d) | Commits on the default branch in the 90 days before the snapshot. |
| Last commit | Committer date of the newest default-branch commit. `pushed_at` is not used, because it also changes when other branches are pushed. |
| Status | **Active**: last commit within 30 days. **Recent**: 31 to 90 days. **Slow**: 91 to 365 days. **Stale**: older than a year, or no commits. **Archived**: archived on GitHub. **Unavailable**: the API call failed. |
| Latest release | Newest non-draft GitHub Release, pre-releases included. Projects that only push tags show "—". |
| Open issues / PRs | Open issues (excluding pull requests) and open pull requests. |

**Also in `data/projects.csv`.** Top-author share (the top human contributor's share of human contributions; values near 100% mean one person does almost all of the work), commits across all time (approximate: the sum of contributor counts), releases in the last 12 months, stars per month since creation, and age in months.

**Limitations.** Stars are a popularity signal, not a quality measure, and can be inflated. Contributor counts cover GitHub accounts only, so commits made under unlinked emails are not counted. Stale does not mean unusable; many small tools are finished. All figures are a point-in-time snapshot.

## Keeping it current

```sh
python3 scripts/update.py                # fetch metrics older than 7 days, then re-render
python3 scripts/update.py --refresh      # fetch everything again
python3 scripts/update.py --render-only  # rebuild this README from data/metrics.json
```

The script needs the GitHub CLI (`gh`) signed in. To add a project, append an entry to `data/projects.json` with `repo`, `name`, `category`, `origin`, and `description`, then run the script.

## Credits

The starting list, its categories, and its one-line descriptions come from [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators), released under CC0-1.0. The descriptions here are shortened rewrites; the originals are kept in `data/projects.json` as `list_description`.
