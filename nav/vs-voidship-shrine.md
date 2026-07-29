# Nav -- Void Shadows: Voidship Shrine

**status:** research-integrated
**last_reconciled:** 2026-05-23
**zone-id:** vs-voidship-shrine
**research_run:** P3 cascade 2026-05-23
**dlc:** Void Shadows

> spoiler: dlc:Void Shadows

**Type:** dungeon (voidship deck)
**Chapter:** 1 onward (Void Shadows active)

## Entry

z-ship-upper -> vs-voidship-shrine (two-way, open from Chapter 1 once DLC active).

## Entry tips

1. Kibellah introduces automatically on first visit -- no trigger required.
2. Initiate Ziek's dialogue node closes permanently if you enter vs-bloodspun-temple without speaking to him first. Talk to Ziek before following the clue trail all the way.
3. Save before the pressure-plate puzzle; exiting mid-sequence can corrupt the puzzle state.

## Sequential gates

1. **Pressure-plate companion puzzle** -- requires >= 2 companions standing on separate plates simultaneously. Typical pairing: Abelard + Kibellah. No consumable key required.
   - `point_of_no_return:` none
   - `lock:` companion availability (Kibellah auto-joins here; Abelard always available)
2. **Initiate Ziek dialogue** -- closes if Bloodspun Temple entered without speaking to him.
   - `point_of_no_return:` vs-bloodspun-temple entry (see E-VS-01)
3. **Shrine inner door** -- opened by pressure-plate completion.
   - `point_of_no_return:` none

## Optional branches

- Pressure-plate puzzle completion unlocks "Mysteries of the Ecclesiarchy" achievement chain (hidden).
- Lateral exit to vs-confessor-chapel (two-way sub-zone link).

## Common confusions

- "Only one plate lights up" -- second companion must be placed before confirming; drag both into position first.
- Ziek disappears after Temple visit -- this is intentional; see vs-bloodspun-temple.md.

## Soft-lock warnings

- **Mid-puzzle exit via menu** -- reload if companion positions reset unexpectedly.

## Exit

Back to z-ship-upper; lateral to vs-confessor-chapel.

## Fast-travel

Integrated into voidship internal FT network (added Patch 1.2).

## Autosaves

Zone entry; pre-pressure-plate puzzle; pre-Kibellah dialogue.

## Sources

- Owlcat Games official Void Shadows DLC page
- Fextralife Void Shadows hub: roguetrader.wiki.fextralife.com/Void+Shadows
- TheGamer "All New Locations" Void Shadows feature

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 1 · category: mainline · spoiler: dlc:Void Shadows · entity: kibellah · entity-status: convertible_
> see crew/kibellah.md for full companion summary
