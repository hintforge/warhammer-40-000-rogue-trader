# Nav -- Void Dragon Flagship (Prologue)

**status:** research-integrated
**last_reconciled:** 2026-05-23
**zone-id:** z-prologue-flagship
**research_run:** P2 cascade 2026-05-23

**Type:** voidship (tutorial)
**Linear?:** yes
**Chapter:** Prologue

## Entry

New game start (cinematic). No prior zone.

## Entry tips

1. The **south-walkway-stairs** near the bridge fork saves your companions for the finale fight; the **cross-the-bridge** path does not. No backtrack after that choice.
2. Loot **Captain's Quarters** (Rogue Trader's Cloak from safe, Theodora's Rosary from chest, Helmet of the Devoted Protector from Mort) before leaving -- you cannot return.
3. Manual save before the **Wall of Fire** (Theodora apparition) -- it is a conviction-tally choice with no retry.

## Sequential gates

1. **Cathedral platform** -- Meet Kunrad. Tutorial dialogue; no choice consequence.
   - `point_of_no_return:` none
2. **Trophy room** -- Servitor combat tutorial. Introduces turn-based combat.
   - `point_of_no_return:` none
3. **Observation deck** -- Meet Theodora; first Heretic Cutthroat ambush.
   - `point_of_no_return:` none
4. **Bridge fork** -- Cross the bridge (companions die in finale) OR south-walkway-stairs (companions survive). No lock; routing choice only.
   - `point_of_no_return:` missable-trigger (companions saved here join final boss fight)
   _source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
5. **Wall of Fire / Theodora apparition** -- Major conviction-tally choice. Iconoclast: find secret lift. Dogmatic: find alt route. Heretical: accept teleport to armoury (Corrupted Inferno Pistol reward).
   - `point_of_no_return:` none (tally; no routing lock here)
   _source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
6. **Captain's Quarters** -- Loot Rogue Trader's Cloak (safe), Theodora's Rosary (chest), Helmet of the Devoted Protector (Mort). Cannot return after Prologue.
   - `point_of_no_return:` permanent (after E01)
7. **Warrant Chamber gene-lock** -- Kunrad cuts you; demonic implant if Coercion/Psyker dialogue chosen.
   - `lock:` player's blood (forced by Kunrad) -- see architecture.md locks-and-keys
8. **Voidship Bridge** -- Ritual at captain's chair; warp-apparitions of Theodora. Quest ends; Conspiracy trophy fires.
   - `point_of_no_return:` permanent -- leads to E01

## Optional branches

- **Iconoclast route** -- Appears to abandon main objective but is the only way to save bridge crew. Not a detour; it rejoins main path.

## Common confusions

- "Iconoclast wall-of-fire route looks like the wrong direction" -- it re-converges with main path; follow the Iconoclast option safely.
- Companions saved at the bridge fork join the final Prologue boss fight; their survival is meaningful but not tracked beyond this zone.

## Soft-lock warnings

None confirmed.

## Exit

To `z-ship-bridge` via edge E01 (story-gate, one-way, permanent). Triggers after the Bridge ritual.

## Sources

- roguetrader.wiki.fextralife.com/By+the+Right+of+Blood
- neoseeker.com/warhammer-40000-rogue-trader/walkthrough/By_the_Right_of_Blood
- gamefaqs.gamespot.com Prologue page

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
