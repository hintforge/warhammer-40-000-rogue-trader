# Warhammer 40,000: Rogue Trader -- Game Guide
<!-- v1 -- 2026-05-22 -->
<!-- forged with hintforge v39 · CC BY-NC-SA 4.0 -->

This folder is a spoiler-controlled, Abelard Werserian-or-Cassia Orsellio-flavored reference for the player's Warhammer 40,000: Rogue Trader playthrough. It is **not** a Claude Code task list. AI agent sessions opened here read this file for orientation, then look up specific topics in the subfolders below.

## Hard rules
- **Spoiler-free unless tier raised.** No story beats, no enemy reveals, no encounter telegraphs. (See `warning_tiers.md`.)
- **PC / Steam (keyboard + mouse).** Translate any other-platform references before quoting.
- **Hint ladder for puzzles & combat encounters.** Smallest nudge first; escalate on request.
- **Don't invent solutions.** If no source has it, say so and link the closest source.
- **Every claim cites a source** in the structured form (see `../../hintforge/templates/claim_format.md`).
- **Conviction path choices (Dogmatic/Iconoclast/Heretical) are story-tier content.** Flag before describing any path-specific quest outcomes, endings, or companion reactions.

## Folder map
- `CHECKPOINT.md` -- current playthrough state. Read first for context.
- `mechanics.md` -- core game-system rules (archetypes, conviction, psyker, navigator, veil degradation).
- `limitations.md` -- blocked sources + **canonical-source rule: talent/ability/item TEXT comes from the game files** (`game_text_lookup.ps1` over the install's `enGB.json`), wiki is fallback. Read its top note before scraping.
- `game_text_lookup.ps1` -- query exact in-game tooltip text (authoritative, patch-current). `talent_catalog.ps1` -- complete blueprint index from the game's `cheatdata.json` (`-Find`/`-Describe`; verify no talent is missing). Both pair with `save_watcher.ps1` (playthrough state).
- `controls.md` -- keybindings, remap recommendations, accessibility notes. Mod stubs link out to mod-specific files.
- `toybox.md` -- Toy Box mod usage guide: tab reference, risk tiers, achievement-enable requirement, recommended settings.
- `settings.md` -- graphics, audio, and accessibility settings affecting gameplay perception.
- `achievements.md` -- achievement trigger conditions, PoNR windows, missability.
- `puzzles/` -- logic and environmental puzzle index + hint ladders.
- `npcs/` -- enemy faction and type index (renamed from `enemies/` at corpus-core-version 5).
- `endings/` -- conviction-path and narrative ending index.
- `paths/` -- branching narrative path tracking (Dogmatic/Iconoclast/Heretical).
- `nav/` -- routing only. `index.md` (rules) + `architecture.md` (zone graph, Optional Content Registry, support topology, locks-and-keys) + per-zone gate-list files.
- `items/` -- weapons / consumables / abilities / upgrades / builds, split by category.
- `sections/` -- main-path regions, missables callouts.
- `persona.md` -- voice toggle. Two voices: **Abelard Werserian** and **Cassia Orsellio**. Active: Abelard Werserian.
- `warning_tiers.md` -- enemy & puzzle tier flags. Check before any preemptive info.
- `research_briefs/` -- P1/P2/P3 handoff briefs for external deep research.
- `research_inbox/` -- drop research result files here, then "ingest the research" in a fresh session.

## Workflow
- When the player arrives at a new section/location, update `CHECKPOINT.md`.
- When research adds new info, update the relevant subfolder file -- don't bloat `mechanics.md`.
- Every fact: structured-claim form with source + confidence.

> Framework: `../../hintforge/`. See `../../hintforge/principles.md` for the full rule set, `../../hintforge/templates/claim_format.md` for source-citation conventions, `../../hintforge/ingestion.md` when the user says "ingest the research" (cascade result integration; runs in a fresh session), and `../../hintforge/stitch_and_zipper.md` when the user says "run stitch" or "run zipper" (post-ingestion synthesis; runs in a fresh session).
