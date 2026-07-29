# Warhammer 40,000: Rogue Trader -- Psyker Talents

**status:** research-integrated
**last_reconciled:** 2026-06-29
**research_run:** doctor 2026-06-29 (Firecrawl)

Sanctioned Psyker is a base-game T1 archetype that was missing from `talents-t1.md` (which covers Warrior/Officer/Soldier/Operative). This file holds its **class talents** plus the **per-discipline talents** (Biomancy / Divination / Pyromancy / Sanctic / Telepathy). Psychic powers themselves and Psy Rating gating are in [`abilities.md`](abilities.md); this file is the talent layer.

_source: doctor research 2026-06-29 (Fextralife Sanctioned Psyker page + individual talent/discipline pages, via Firecrawl) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

---

## Sanctioned Psyker -- class talents
_Psy Rating tiers: Minoris (Psy 1, char lvl 9 / SP lvl 4) -> Majoris (lvl 19 / 14) -> Extremis (Psy 3, lvl 29 / 24) -> Terminus (Psy 4, lvl 39 / 34). Each tier unlocks new powers and strengthens damaging ones._

| Talent | Effect |
|---|---|
| Psyker Minoris / Majoris / Extremis / Terminus | Each level of psy rating grants access to new psychic powers and strengthens damaging psychic powers (the four are the same effect at successive Psy Rating breakpoints). |
| Still Mind | +(WP bonus/2) resolve while veil degradation is 10 or lower. |
| Sacred Rituals | Psychic powers have a 25% chance to refund AP spent on them while veil degradation is 10 or lower. |
| Enforce Reality | Using a heroic act lowers veil degradation by (INT bonus). |
| Second Sight | Psychic powers with range >=2 cells gain +(PER bonus) range. |
| Subtle Manipulation | Use a damaging psychic power in melee threat without provoking AoO. (Non-damaging powers never provoke AoO regardless.) |
| Inscribed Soul | Grants the Inscribed Soul ability: 0 AP, deals 25% of your max wounds to yourself; your next psychic power won't trigger phenomena/perils and won't degrade the veil. |
| Blade of Light | Force weapon attacks deal +(1 + psy rating) damage and +(5 + 5x psy rating)% armour penetration. |
| Psychic Barrage | Damaging psychic powers on targets 6+ cells away deal +(BS bonus) extra damage. |
| Stabilising Factor | First psychic power each turn raises veil degradation by 2 less; if that would push it below 0, veil degradation drops by 1 instead. |
| Obscured Threat | While you're out of the target's line of sight or in cover, the target's resistance tests suffer -(4x psy rating). |

---

## Biomancy discipline talents
| Talent | Effect |
|---|---|
| Iron Arm (ability) | Target ally within 10 cells gains +(10 + 4x psy rating) STR and TGH until end of combat. 1 AP, 1-round cooldown. |
| Adrenaline Surge | On the first turn of combat, all Biomancy powers cost -1 AP. |
| Sanguine Siphon | Dealing damage grants +1 stack (+2 if the target is adjacent). On lethal damage, remove stacks to reduce that damage by -1 each until non-lethal or out of stacks. |
| Corpus Conversion | When an enemy adjacent to an ally dies, that ally gains a stacking corpus conversion. Your next power targeting only that ally acts as +2 psy rating, won't damage the veil / trigger phenomena / perils, and removes 1 stack. |
| Warp Saturation (page formerly "Strange Vitality") | When you or your allies are under psychic-power effects, +5 TGH per such effect. |
| Biophysical Distortion | All your attacks (incl. damaging powers) poison enemies for (4x psy rating) damage per turn. |
| Confer Immunity | Healing a character already at full wounds grants temporary wounds equal to the healing instead (no stack). |
| Pulse of Life | Your healing can crit-heal at (5 + 2x WP bonus)%, scaled by crit-chance and crit-damage bonuses. |
| Deterioration | Any effect you apply that increases damage a target suffers is increased by half (a +20% becomes +30%). |

## Divination discipline talents
| Talent | Effect |
|---|---|
| Edge of Fate | At combat start, allies gain +15% crit chance; the first crit removes it. |
| Flawless Plan | Every 9th combined dodge/parry by you and allies grants you +2 AP next turn. |
| Unnatural Luck | Casting a Divination power on an ally grants unnatural luck: their next critical hit taken becomes a normal hit, then the effect is removed. |
| Fatebringer | Allies under at least one psychic power gain +(5 + 2x psy rating)% armour penetration. |
| Predicted Downfall | Each enemy's first dodge attempt in combat suffers -(7x psy rating)%. |
| Forewarning | CAVEAT: the Fextralife "Forewarning" page documents a Soldier talent (Controlled Shot -1 AP near an ally), NOT the Diviner feature. Treat the Diviner innate as NOT YET CONFIRMED on Fextralife. |

## Pyromancy discipline talents
| Talent | Effect |
|---|---|
| Ignite (ability) | Target within 12 cells takes (1 + WP bonus + 6x psy rating)-(2x WP bonus + 10x psy rating) damage + warp burn (deals WP bonus + 2x psy rating at end of their turn; AGI test at -(5x psy rating) to stop). 1 AP. |
| Blazing Inferno | +1% crit chance until end of combat each time you deal damage by any means. |
| Body of Flames | +(8x psy rating)% armour vs. fire, and half that vs. las/melta/plasma energy damage. |
| Burning Blood | When you use a power (or take burning/bleeding/melee damage), all adjacent enemies take (4x psy rating) direct damage. |
| Melting Armour | Each time an enemy takes damage from you, its armour -5% (or -1 deflection if armour is already 0). |
| Backdraft | When a power you use deals damage, a random enemy within 2 cells of the target takes half that damage (doesn't re-trigger). |
| Relentless Blaze | While burning: +1 psy rating, +2 resolve, and fire no longer reduces your momentum. |
| Fire Within | Every time you kill or crit 8 creatures in one combat, your next attack costs 0 AP and has no cooldown. |
| Sparks of the Greater Flame | Your DoT effects gain (5 + 5x psy rating)% crit chance, scaled by crit-chance bonuses. |

## Sanctic discipline talents
| Talent | Effect |
|---|---|
| Word of the Emperor (ability) | All allies in a 5-cell radius gain +(1 + psy rating) resolve until end of combat; each extra stack adds +2. 1 AP. |
| Destined | +5% armour, increasing another +5% at the start of every combat turn after the first. |
| Eternal Glory | The first time momentum hits 200 on your turn: +5 all characteristics, +1 resolve, +1 deflection, +1 all damage until end of combat. |
| Psalms of Heroes | +1 psy rating until end of combat each time an ally uses a heroic act. |
| Edge of Dawn | Enemies adjacent to you take +10% more damage. |
| Hymns of Hatred | Any crit within your line of sight (incl. yours) gives +1% crit damage until end of combat. Stacks. |
| Sanctified Slayer | +Resolve% crit chance. |

## Telepathy discipline talents
| Talent | Effect |
|---|---|
| Psychic Shriek (ability) | Target within 12 cells takes (1 + WP bonus x psy rating)-(4 + WP bonus x (1+psy rating)) damage. 2 AP. Bypasses armour/dodge (single-target mental). |
| Aftershock | When you deal mental damage from any other source, the target takes half as much mental damage at the end of its next turn. |
| Mind Siege | Enemies that failed a WP resistance test vs. your powers take +(4x psy rating) extra mental damage whenever they take mental damage, until end of combat. |
| Pain Channelling | When a power kills with overkill, the excess damage hits the nearest enemy. |
| Warp Minds | Every 6th power use: all enemies take a stacking -5 to all characteristics until end of combat. |
| Mental Breach | Enemies that have taken damage from you take -20 to all resistance tests vs. you until end of combat. |
| Mind Thief | First time an enemy is targeted by a given ability: -5 INT/PER to them, +2 INT/PER to you until end of combat. |
| Visions of Doom | Enemies targeted by your powers take a stacking -5% dodge/parry until end of combat. |
| Weak Hearts | Enemies you've blinded/stunned/immobilised/proned take +10% more damage. |

---

## Unsanctioned Psyker
**Not a standalone archetype.** "Unsanctioned Psyker" is a psyker *state* a non-psyker reaches by taking the **Psychic Awakening (\<discipline\>)** talent at the **Exemplar** rank (the companion who walks this path is Idira Tlass). It has no keystone/characteristics-pool/ultimate of its own. The defining trait: unsanctioned psykers start at **Psy Rating 1** (vs. Sanctioned's 0) but **lack the Sanctioned feature's -20% reduced chance to trigger psychic phenomena** -- earlier power for higher backlash risk. They share the full discipline talent sets above; their unique additions:

| Talent | Effect |
|---|---|
| Psychic Awakening (Telepathy / Divination / Biomancy / Pyromancy / Sanctic) | The character becomes an unsanctioned psyker and gains +1 psy rating. One per discipline; taken at Exemplar rank. (The Sanctic version also deals (1 + WP bonus x psy rating)-(4 + WP bonus x (1+psy rating)) damage.) |
| Thriving in Peril | Every Perils of the Warp increases momentum by +(WP bonus + resolve + psy rating). (Idira -- rewards backlash.) |
| Power Conduit | After triggering psychic phenomena or Perils of the Warp the first time each turn, your next psychic power costs -1 AP. (Idira -- rewards backlash.) |
| Advice and Guidance | The first time in combat an ally is targeted by your psychic power, that ally gains +10 WS and BS until end of combat. (Idira.) |

> Discipline power lists (the active psychic powers themselves) live in [`abilities.md`](abilities.md).
