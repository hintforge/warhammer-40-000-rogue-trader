# Warhammer 40,000: Rogue Trader -- Abilities

**status:** research-integrated
**last_reconciled:** 2026-05-23
**research_run:** P3 cascade 2026-05-23

Psyker disciplines and archetype-specific abilities. Full per-power enumeration was not a P1 deliverable; this covers system-level mechanics and notable powers. P2/live observation will extend per-power entries.

## Psyker Disciplines (5)

Each discipline provides an innate starting power + ~8 unlockable powers + 8 unique talents.

| Discipline | Governing stats | Starting recommendation | Standout powers |
|---|---|---|---|
| Biomancy | PR + Willpower | Good starter | **Metabolic Overcharge** -- community-rated game-best power; late-arriving |
| Divination | PR + Willpower | Reasonable | Support/debuff; buff allies |
| Pyromancy | PR + Willpower | **Not recommended as starting discipline** -- Psy Rating is 0 until level 10; weak Prologue/Ch1 | AoE fire; converged for CC in arena (Ch3) |
| Sanctic | PR + Resolve | Good for Dogmatic builds | Dogmatic synergy; pairs with Halo Device (Ch4) |
| Telepathy | PR + Willpower | Advanced (needs PR) | **Psychic Shriek** -- single-target damage bypassing armor and dodge; chain-stun CC (Russian DTF.ru Officer chain-stun strategy on Ch5 C'tan clones) |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Psy Rating

Gated at character levels 10 / 20 / 30 / 40. A psyker with no Psy Rating (levels 1-9) has severely diminished power output.

- Sanctioned Psyker origin: -20% phenomena chance (recommended for psyker MCs).
- Idira (Unsanctioned): +1 starting Psy Rating but flat 5% Perils chance regardless of Veil Degradation.
- Cassia's first staff upgrade: reduces VD by 10 + wards warp damage (primary VD management lever).

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Veil Degradation and Psyker Phenomena

See `mechanics.md` Veil Degradation section for thresholds and mitigation. Quick summary:

- 0-14 VD: standard phenomena (Sanctioned 5+PR%; Unsanctioned 10+2*PR%)
- 15-20 VD: elevated phenomena (Sanctioned 10+2*PR%; Unsanctioned 20+4*PR%); Perils of the Warp risk on major powers
- VD decreases 1/round at combat end; minor power +1 VD, major power +3 VD

## Archetype-Specific Abilities (non-psyker)

| Archetype | Key ability / passive | Notes |
|---|---|---|
| Officer | At All Costs (Commissar origin variant) / extra turn generation | Grand Strategist: zone control + extra turns; Master Tactician: momentum-driven AoE |
| Soldier | Calibrated shots; heavy-weapon specialization | Arch-Militant Tier 2 for sustained DPS |
| Warrior | Melee mobility; dodge/counter-attack | Assassin Tier 2: mobile DPS; Vanguard Tier 2: tank |
| Operative | Debuffs; skill coverage | Bounty Hunter Tier 2: sniper-utility |

Full archetype talent trees in [`items/talents-t1.md`](talents-t1.md) (T1), [`items/talents-t2.md`](talents-t2.md) (T2), [`items/talents-exemplar.md`](talents-exemplar.md) (Exemplar), [`items/talents-dlc.md`](talents-dlc.md) (DLC). System overview in [`items/upgrades.md`](upgrades.md).

## DLC Archetype Abilities (Void Shadows)

### Bladedancer (T1 -- Void Shadows)

Mobile melee archetype; paired with Executioner at T2 for peak burst.

| Ability | Type | Notes |
|---|---|---|
| Death From Above | Active | Leap attack; repositions + AoE melee damage |
| Death Waltz | Active | Cleave through multiple enemies; community highlight for grouped fights |
| Acrobatic Artistry | Passive | Movement-triggered dodge bonus |
| Blade Shroud | Active | Defensive deflection buff |
| Blade Dance | Heroic act | Chain multi-hit against all adjacent enemies |

Signature talent: **Death Warden** -- on kill, grants free repositioning move.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:Void Shadows_

### Executioner (T2 -- Void Shadows)

Chaos-flavored melee attrition archetype; requires Bladedancer T1.

| Ability | Type | Notes |
|---|---|---|
| Reckless Abandon | Active | Self-damage for massive burst hit; high risk/reward |
| Carnival of Misery | Active | AoE debuff + damage; pairs with Death Waltz clears |
| Gift of Torment | Passive | Stacking damage bonus on consecutive melee hits |
| Where It Hurts | Active | Single-target exposed-armor strike; strips TGH bonus |

Signature talent: **Anatomy Expert** -- critical hits inflict bleeding DoT.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:Void Shadows_

## DLC Archetype Abilities (Lex Imperialis)

### Arbitrator Origin (Lex Imperialis)

Origin (not archetype tier); provides Familiar bond and three sub-paths.

| Sub-path | Focus |
|---|---|
| Vigilant | Detection + counter-ambush; stealth-breaking |
| Castigator | Punishment burst; high single-target |
| Subductor | Crowd control; suppression + capture |

### Overseer (T2 -- Lex Imperialis)

Requires Officer/Operative or Arbitrator/Sanctioned Psyker/Unsanctioned Psyker origin.

| Ability | Type | Notes |
|---|---|---|
| Familiar bond abilities | Passive/Active | Per-Familiar type (see below) |
| Overcharge | Heroic act | Familiar overdrives for multi-action turn |

**Familiar types and bonuses:**
- Cyber-Mastiff (Glaito variant for Solomorne): frontline flanker; bleeds on bite
- Psyber-Raven: scout reveal + AoE Warp-sight debuff
- Servo-Skull Swarm: area denial; blocks line-of-sight
- Cyber-Eagle: long-range spotter; ranged accuracy debuff on target

Familiars share initiative with bonded character; have independent wound pools; recoverable between fights.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:Lex Imperialis_

## Support Items / Familiars

- **Cyber-Mastiff (base game)** -- summons temporary ally; available after Jae companion questline (Ch4). Achievement: "Release the Hound!" (7 different enemies bitten in one turn, Daring+).
- **Glaito (Solomorne's Familiar, DLC)** -- Cyber-Mastiff variant; designation GL-8-0; permanent Familiar slot via Overseer mechanics. `spoiler: dlc:Lex Imperialis`
- **Glaito (voidship companion, base game)** -- separate entity; "Pet the Dog" achievement. Not the same as Solomorne's Familiar despite shared name origin.

> **Cross-system dependency** -- see `dependencies.md` DEP-005: "Can Glaito open the chest?" has two different answers depending on which Glaito is meant; the voidship Glaito cannot open the li-leethus-sand-zone chest -- only Solomorne's Familiar (GL-8-0) can (SEQ-008).
- No discrete deployable-summon category beyond psyker summons and Familiars confirmed.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
