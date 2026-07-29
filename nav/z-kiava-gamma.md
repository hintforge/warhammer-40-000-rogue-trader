# Nav -- Kiava Gamma (Forge World)

**status:** research-integrated
**last_reconciled:** 2026-05-23
**zone-id:** z-kiava-gamma
**research_run:** P2 cascade 2026-05-23

**Type:** dungeon (forge world)
**Linear?:** yes
**Chapter:** 2 & 4

## Entry

Shuttle from Cranach system (after 5-ship Chaos fleet void combat).

## Entry tips

1. **Speak to the Pasqal cogitator on your voidship first** before entering this zone -- it gives you the "Litanies of the Motive Force" phrase that disables the toxic-gas data cache room. Without it, the "Disable the Gas" option does not appear in the data cache room.
2. **Heinrix's Secrets of the Cult side room** is south of the circular platform -- complete it before leaving the zone or his companion quest fails.
3. **Save before the Forgefiend** -- kill OR take for voidship Daemonic Presence ability. Irreversible choice.

## Sequential gates

1. **Manufactorum entrance** -- Entry combat; standard approach.
   - `point_of_no_return:` none
2. **Corrupted servitors (west room)** -- Medicae + Agility check to recruit them as combat allies ("follow default programming"). Optional.
   - `point_of_no_return:` none
3. **Tech-Priest ladder/lift confrontation** -- Progress gate; combat or dialogue.
   - `point_of_no_return:` none
4. **Theodora data-cache room (toxic gas)** -- Disable gas with "Litanies of the Motive Force" phrase (from Pasqal cogitator on voidship). "Disable the Gas" option only appears if you spoke to the Pasqal cogitator first. Required for "How Did It All End?" chain.
   - `lock:` story-flag ("Litanies of the Motive Force" from Pasqal voidship cogitator) -- see architecture.md locks-and-keys
   - `point_of_no_return:` missable-trigger (Ch.2 window before Dargonus inauguration)
5. **Dementz fight** -- Pasqal companion quest combat.
   - `point_of_no_return:` none
6. **Cubis Delphim arena** -- Rotate bridges puzzle/encounter.
   - `point_of_no_return:` none
7. **Chaos Marine Uralon midboss** -- Combat encounter.
   - `point_of_no_return:` none
   _source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression_
8. **Forgefiend final encounter** -- Kill for loot OR take for voidship Daemonic Presence ability (major permanent choice).
   - `point_of_no_return:` permanent (choice irreversible)

## Optional branches

- **Heinrix's Secrets of the Cult side room** -- South of circular platform. Must complete before leaving; fail = Heinrix companion quest fails. Treat as mandatory.

## Common confusions

- "'Disable the Gas' option is missing" -- Requires prior interaction with Pasqal's cogitator on the voidship bridge. If the option is absent, you likely skipped that step.
- Heinrix's side room is easy to miss by going straight to the Forgefiend. Clear the room south of the circular platform first.

## Soft-lock warnings

- **Leaving without Heinrix's side room** -- Fails his companion quest. Complete it before exiting.

## Exit

Shuttle to system map.

## Sources

- gamerguides.com Kiava Gamma walkthrough
- neoseeker.com Flame_in_the_Dark
- roguetrader.wiki.fextralife.com/Flame+in+the+Dark and /Kiava+Gamma

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
