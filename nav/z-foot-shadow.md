# Nav -- Footfall Shadow Quarters

**status:** research-integrated
**last_reconciled:** 2026-05-23
**zone-id:** z-foot-shadow
**research_run:** P2 cascade 2026-05-23

**Type:** dungeon
**Linear?:** yes with quarantine gate
**Chapter:** 2 & 4

## Entry

From z-foot-dock (south exit). Contains the quarantine gate (SE) requiring Kiava Gamma completion to open.

## Entry tips

1. The **Extermination Brigade quarantine gate (SE)** is the most-searched "how do I get back in" question on Steam. You need to complete Reclaim What Was Lost (Kiava Gamma) first.
2. The **sun-symbol floor** (Astray quest) is the pickup point for the Shadow Quarters missable chain -- grab it in Ch.2.
3. **Both sewer access routes** are here: rat-hunting sewers via Jae AND Crematorium via Denz's funeral (Fidelio/Underworld chain). At least one must be taken to avoid permanently locking Rat Hunting.

## Sequential gates

1. **Anver thug fight (west)** -- Combat clearing west approach.
   - `point_of_no_return:` none
2. **Sun-symbol floor (Astray quest pickup)** -- Missable Ch.2-only quest pickup. Grab it during Ch.2 sweep.
   - `point_of_no_return:` missable-trigger (Shadow Quarters removed from fast-travel Ch.4+)
3. **Adeptus Amasecus (south exit)** -- Route to adjacent area.
   - `point_of_no_return:` none
4. **Quarantine gate SE** -- Locked until Kiava Gamma main quest complete (Reclaim What Was Lost). E06.
   - `lock:` story-flag (Kiava Gamma completion) -- see architecture.md locks-and-keys
   - `point_of_no_return:` none (opens once trigger met)
5. **Tunnel under bridge** -- Theodora's note cache. Part of "How Did It All End?" chain.
   - `point_of_no_return:` missable-trigger (Ch.2 only)

## Optional branches

- **Rat Hunting sewers (via Jae)** -- Jae's sewer entry after Persona Non Grata completion.
- **Crematorium route (Fidelio/Underworld)** -- During Denz's funeral; requires Fidelio impersonation chain active.

## Common confusions

- "Quarantine gate won't open" -- Must complete Kiava Gamma (Reclaim What Was Lost) first. This is the #1 Steam community confusion for Shadow Quarters.
- Shadow Quarters itself is entirely inaccessible in Ch.3; the quarantine zone (z-foot-quarantine) becomes available inside it when re-entering in Ch.4.

## Soft-lock warnings

- **Rat Hunting permanently locked** -- Refusing both Jae recruitment (Persona Non Grata) AND Underworld/Fidelio funeral entry blocks both sewer routes. Complete at least one before Ch.3.

## Exit

Back to z-foot-dock (north); to z-foot-quarantine (SE, after Kiava Gamma completion).

## Sources

- gamerguides.com Where-the-Shadows guide
- neoseeker.com Tattered_Spirit
- thegamer.com Underworld guide
- Steam community (quarantine gate thread)

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
