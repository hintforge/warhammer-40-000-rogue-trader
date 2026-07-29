# Nav -- Eurac V (Navis Nobilite Station)

**status:** research-integrated
**last_reconciled:** 2026-05-23
**zone-id:** z-eurac-v
**research_run:** P2 cascade 2026-05-23

**Type:** dungeon (station)
**Linear?:** yes with side rooms
**Chapter:** 1

## Entry

Emergency dock from Rykad System scan.

## Entry tips

1. The **main-chamber cogitator** has TWO distinct options -- one opens all doors on level; the other activates the elevator. Players often use only one and miss the other (gamerguides.com). Use both.
2. **Save before each component** of the lab puzzle -- it is bug-prone (Fextralife Eurac V comments). See corpus puzzles/eurac_v_lab.md.
3. The **Armoury door** (high Logic check) is in this zone -- grab it before the elevator if Logic is sufficient; reward: Flamer Digi-Weapon Ring.

## Sequential gates

1. **Docking ring** -- Felek Orsellio dialogue; choice tree (help / negotiate / attack). Commerce 40 + take-Child option skips forced combat.
   - `point_of_no_return:` none
2. **Lobby Felek fight** -- Forced unless Commerce 40 + take-Child dialogue chosen.
   - `point_of_no_return:` none
3. **Bookshelf [Athletics] block** -- Athletics check to access stairs leading further in.
   - `point_of_no_return:` none
4. **Library / Navigator Flesh Sample hallway** -- Loot: Navigator Flesh Sample. Side corridor.
   - `point_of_no_return:` none
5. **Mutant ambush room** -- Combat; clears path to cogitator.
   - `point_of_no_return:` none
6. **Two doors (one locked, one open)** -- Both lead to the same guard room. Neither is a dead end or permanent loss.
   - `point_of_no_return:` none
7. **Main cogitator: Option A** -- "Awake -> Switch to main chamber controls -> Open all doors on level." Opens laboratory door.
   - `lock:` Tech-Use check -- see architecture.md locks-and-keys (z-eurac-v laboratory door)
   - `point_of_no_return:` none (these are two separate options on the same machine)
8. **Main cogitator: Option B** -- "Main elevator controls -> Activate the elevator." Activates upper chamber elevator. DISTINCT from Option A -- use both (gamerguides.com).
   - `lock:` Tech-Use check -- see architecture.md locks-and-keys (z-eurac-v upper elevator)
   - `point_of_no_return:` none
9. **Laboratory puzzle** -- Flask connector puzzle. See corpus puzzles/eurac_v_lab.md. Rewards: Shimmering Emulsion (psyker-only, +1 Psy Rating) OR Viscous Solution (+1 Deflection, -10 AGI), one each, permanent effects.
   - `point_of_no_return:` none (after selecting reward branch, the other is gone)
10. **Elevator up** -- Upper chamber; Cassia recruitment.
    - `point_of_no_return:` missable-trigger (failing Cassia's recruitment dialogue locks out Cassia for the run)
    _source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression · entity: cassia-orsellio · entity-status: convertible_
    > see crew/cassia-orsellio.md for full companion summary

## Optional branches

- **Armoury door** -- High Logic check; reward: Flamer Digi-Weapon Ring. Off the main path between cogitator and lab.
- **Lab puzzle reward fork** -- Shimmering Emulsion (psyker-only, +1 Psy Rating, +30% Perils) OR Viscous Solution (+1 Deflection, -10 AGI). Both are one-use permanent injectors.

## Common confusions

- "Cogitator only opens doors, elevator still inactive" -- Players use Option A only and miss Option B. Both options are on the same cogitator screen; select them in sequence (gamerguides.com).
- Lab puzzle is bug-prone: save before each component placement.

## Soft-lock warnings

- **Cassia recruitment dialogue failure** -- Does not hard-lock the game but Cassia is permanently unavailable for this run if her recruitment dialogue is failed.

## Exit

Shuttle from upper chamber to Rykad System map.

## Sources

- gamerguides.com/Navis-Nobilite-Laboratory-Puzzle (cogitator two-option clarification)
- roguetrader.wiki.fextralife.com/Eurac+V and /Secrets+of+the+Navis+Nobilite
- neoseeker.com Navis_Nobilite_Secrets
- gamespot.com Navis Nobilite Lab Puzzle guide

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
