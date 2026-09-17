# Puzzle -- Aviorus Main Computing Cathedral (Pressure Stabilisers)

**status:** research-integrated
**last_reconciled:** 2026-09-17
**research_run:** P1 cascade 2026-05-22
**puzzle-tier-required:** 1 (type named on entry; full solution available on request)

**Zone:** z-aviorus (Aviorus -- Main Computing Cathedral, optional zone)
**Type:** numeric combination -- enable pressure stabilisers summing to a target
**Chapter:** 2+ (accessible until Ch5 PoNR; not urgently missable)
**Missable:** no (permanent accessibility)

## Context

An optional dungeon accessible by scanning the Aviorus system. Not required for any main quest but yields archeotech rewards. Russian DTF.ru and StopGame.ru catalog it as a must-do before enthronement due to unique weapon/item drops.

**Puzzle type (Tier 1 announce):** A numeric combination puzzle at the sealed door -- pick which pressure stabilisers to enable so they total the required pressure. No skill check gates it.

**CORRECTION 2026-09-17:** this file previously described a "hacking minigame (Tech-Use skill sequence)" and told the player to bring Pasqal. That was wrong on both counts. `nav/architecture.md` had it right all along ("Backup-generator puzzle (5 stabilizers, pressure 10)"); the two files disagreed and the nav file was correct.

## Hint Ladder

**Lvl 1 (nudge):** The sealed door in the Compressor Hall has no power. There is a backup generator at the far end of the hall, and the floor around it is flooded with toxic gas. Send ONE character through the gas rather than the whole party -- damage is taken per character crossing it.

**Lvl 2 (more):** Five pressure stabilisers can be enabled. They do not all carry the same value, and you do not enable all five -- you pick a subset that adds up to exactly the pressure the cogitator asks for. Interact with the Compressor Hall main cogitator to set them, then interact again once the total is right to vent the gas.

**Lvl 3 (full solution):** Target pressure is **exactly 10**. Two subsets of the five stabilisers reach it: **1 + 2 + 5**, or **2 + 3 + 4**. Either works. Procedure: send one character through the gas to reach the cogitator, enable the chosen three, then interact with the cogitator again to neutralise the gas -- after which the rest of the party can cross safely.

**Consequence worth knowing before you pull it:** activating the backup generator permanently raises **Veil Degradation by +5** for this level and opens new encounters when backtracking. The sealed area holds a crate guarded by two traps; **Augmented Gloves** are found separately, nearby in the same hall.

## Reward

Archeotech rewards. Confirmed at container level: **Augmented Gloves** in the hall, plus a trapped crate inside the sealed area (two traps). Full item enumeration still incomplete.

_source: P1 research cascade 2026-05-22 - capture: web_fetch - confidence: medium - enemy-tier: 0 - puzzle-tier: 1 - category: mainline - spoiler: progression_

_source (solution + type correction): Fextralife "Enter the Main Computing Cathedral" + GameSkinny Drifting Voidship puzzle guide - capture: web_fetch 2026-09-17 - confidence: high (two independent sources agree on target 10; the valid subsets come from GameSkinny, Fextralife confirms the target and the gas/cogitator procedure) - enemy-tier: 0 - puzzle-tier: 1 - category: mainline - spoiler: progression_

## Sources

- StopGame.ru forum (Russian): https://stopgame.ru/game/warhammer_40_000_rogue_trader
- DTF.ru community (Russian): https://dtf.ru/games/3671840-obzor-warhammer-40-000-rogue-trader-ot-owlcat
- Fextralife: https://roguetrader.wiki.fextralife.com/Enter_the_Main_Computing_Cathedral
- GameSkinny: https://www.gameskinny.com/tips/warhammer-40k-rogue-trader-drifting-voidship-puzzle-guide/
