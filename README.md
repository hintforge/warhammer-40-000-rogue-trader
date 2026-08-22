# Warhammer 40,000: Rogue Trader — Hintforge Companion

![Rogue Trader companion status — coverage, how current it is, spoiler control, and save reader](assets/readme-status-card.svg)

A spoiler-controlled hint companion for **Warhammer 40,000: Rogue Trader**, Owlcat's grimdark CRPG in the Koronus Expanse. Built in the [Hintforge](https://github.com/hintforge/builder) format: a loyal sidekick that answers only from these guide files — never from guesswork — at the spoiler level you set, and that tracks where you are so you can step away for months and pick right back up.

## Use it

You need a Hintforge reader running in Claude Code, Codex, or OpenClaw. Point it at this repo:

> Load the Rogue Trader guide from github.com/hintforge/warhammer-40-000-rogue-trader

Then just ask — *"how do I build this companion," "how do I beat this fight," "where was I."* Runtime setup lives in [`hintforge/reader`](https://github.com/hintforge/reader).

## How current it is

This guide was last verified against **Build 21262645 (May 2026)**. The game has since moved on — **Patch 1.6 and The Infinite Museion DLC (June–July 2026)** landed after that check — so newer patch changes and the latest DLC content aren't reflected yet. Everything it *does* cover is deep (the full base campaign — mechanics, crew, factions, items, and all achievements); it just hasn't caught up to the newest release. That's why the card is stamped **"CHECKED"** rather than "VERIFIED."

## Spoilers & the save reader

**You** control how much this guide volunteers, through two independent dials you set:

- **Enemy warnings (Tier 0–5)** — from "say nothing" up to full boss strategy.
- **Puzzle warnings (Tier 0–3)** — from "silent, ask when you want a hint" up to a step-by-step walkthrough.

Both start **silent** — the guide volunteers nothing pre-emptively until you raise a dial. The guide only honors what you set.

Rogue Trader's saves are readable, so the companion can recap your saves and resolved party/game state. As with any save reading, that's the one surface where a spoiler could slip — so it's the place to watch — but no leak has been recorded for this guide.

## What's inside

A structured Markdown corpus — mechanics (deep stat math), crew/companions, factions, items, puzzles, quests, and all achievements — plus a save-state tracker (`save_watcher.ps1`) that lists, backs up, and resolves your saves. Interactive build and party planners are on the roadmap, not yet built. The companion reads and writes only the files you control.
