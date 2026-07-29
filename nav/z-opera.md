# Nav -- Commorragh Anatomical Opera

**status:** research-integrated
**last_reconciled:** 2026-05-23
**zone-id:** z-opera
**research_run:** P2 cascade 2026-05-23

**Type:** dungeon
**Linear?:** yes (linked to z-chasm hub)
**Chapter:** 3

## Entry

From z-chasm (NE path to Opera entrance). Accessible after arriving in the Chasm.

## Entry tips

1. **Get the Bone Key from Tervantias** -- Required to open Ulfar's cage. As of patch 1.5, missing this permanently locks out Ulfar as a companion. Do this BEFORE the second arena.
2. **Marazhai is on the upper ledge** (not the main floor) -- look up to find him. Missing his dialogue causes the arena portal to fail to unlock (Steam 596268535200653291).
3. **Mon-Keigh Rubbish box** (party gear) only opens after: first arena win + Tervantias dialogue ("require a moment of your precious time"). Do the first arena before expecting to get gear back.

## Sequential gates

1. **Wrack at entrance** -- Kill for Macrosteroidal Gland (Dogmatic path reward).
   - `point_of_no_return:` none
2. **Tervantias dialogue** -- Recruit one psyker companion + body parts trades. Gives the Bone Key for Ulfar.
   - `point_of_no_return:` none
3. **Marazhai dialogue (upper ledge)** -- Must find Marazhai on the upper platform and succeed at dialogue or arena unlock fails.
   - `point_of_no_return:` missable-trigger (Steam 596268535200653291 -- missing him blocks arena)
4. **Ulfar's cage (Bone Key)** -- Bone Key from Tervantias opens the cage; starts Fury in Chains quest.
   - `lock:` Bone Key item (from Tervantias) -- see architecture.md locks-and-keys
   - `point_of_no_return:` permanent (missing Ulfar in Ch.3 patch 1.5+ locks him out permanently -- gamerguides How To Recruit Ulfar)
   _source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression · entity: ulfar · entity-status: convertible_
   > see crew/ulfar.md for full companion summary
5. **Mon-Keigh Rubbish box (gear retrieval)** -- Party gear returned after first arena win + Tervantias "require a moment" dialogue completes.
   - `lock:` story-flag (first arena + Tervantias phrase) -- see architecture.md locks-and-keys
   - `point_of_no_return:` none (available throughout remaining Ch.3)

## Optional branches

- **Psyker and body-parts trades with Tervantias** -- Available alongside main quest interactions.

## Common confusions

- "Ulfar's cage won't open" -- Bone Key must come from Tervantias in this same zone. Get it during Tervantias dialogue before going to the cage.
- "Mon-Keigh box is inert" -- Requires first arena completion + Tervantias dialogue phrase. Can't get gear back before those conditions are met.
- Marazhai is on the upper platform/ledge, not the main floor where Tervantias is.

## Soft-lock warnings

- **Ulfar permanently missable** -- Missing the Bone Key exchange and Ulfar's cage in this zone (Ch.3 patch 1.5+) makes Ulfar permanently unavailable for the run. No later rescue path exists.

## Exit

Back to z-chasm (south return).

## Sources

- gamerguides.com Ch.3 Companion Locations and How To Recruit Ulfar
- neoseeker.com Fury_in_Chains
- Steam community thread 596268535200653291 (Marazhai upper ledge)

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
