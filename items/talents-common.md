# Warhammer 40,000: Rogue Trader -- Universal Common Talents

**status:** research-integrated
**last_reconciled:** 2026-06-29
**research_run:** doctor 2026-06-29 (Firecrawl)

The third pool feeding the **"Available Common Talents"** level-up screen, alongside [homeworld talents](talents-homeworld.md) and [origin talents](talents-origin.md). These are available to (essentially) every archetype: weapon/armour proficiencies, characteristic training, skill talents, and a few generic combat talents. When a name on the common-talent screen isn't an archetype talent (see `talents-t1/t2/dlc.md`), a homeworld talent, or an origin talent, it's here.

_source: doctor research 2026-06-29 (Fextralife individual talent pages, via Firecrawl) · capture: web_fetch · confidence: high (some pages 404 -- noted inline) · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

---

## Weapon Proficiencies (gate weapon use; pick to USE a weapon family)
| Talent | Effect |
|---|---|
| Bolter Weapon Proficiency | Allows use of bolt weapons (bolter, bolt pistol, etc.). |
| Flame Weapon Proficiency | Allows use of flame weapons (flamer, heavy flamer, hand flamer). |
| Melta Weapon Proficiency | Allows use of melta weapons (meltagun, multi-melta, etc.). |
| Plasma Weapon Proficiency | Allows use of plasma weapons (plasma gun, plasma pistol, etc.). |
| Aeldari Weapon Proficiency | Allows use of Aeldari weapons (long rifle, shuriken catapult, etc.). |
| Drukhari Weapon Proficiency | Allows use of Drukhari weapons. |
| Xenos Weapon Proficiency | Allows use of xenos weapons (the umbrella covering Aeldari/Drukhari and other alien arms). |
| Heavy Weapon Proficiency | Reduces the Strength requirement of heavy weapons by -25 (does not "unlock" -- lowers the STR gate). |

> **Game-file verified 2026-06-29:** the COMPLETE proficiency set is exactly the 8 above (Aeldari, Bolter, Drukhari, Flame, Heavy, Melta, Plasma, Xenos). There is **no "Las Weapon Proficiency" and no "Solid Projectile Weapon Proficiency"** -- Fextralife listed them in error; las and solid-projectile weapons require no proficiency. Confirmed against the game's `enGB.json` localization (see `../game_text_lookup.ps1`).

## Weapon Experts (damage upgrades; pick to BUFF a weapon family)
| Talent | Effect |
|---|---|
| Chain Weapon Expert | Chain weapon attacks gain +4 maximum damage. |
| Power Weapon Expert | Power weapon attacks gain +10% armour penetration. |
| Solid Projectile Weapon Expert | Solid-projectile weapon attacks gain +2 minimum damage. |

## Armour
| Talent | Effect |
|---|---|
| Heavy Armour Proficiency | Allows the wearing of heavy armour. (NOT in Kibellah's pool -- player-confirmed; she's a light-armour Bladedancer.) |
| Medium Armour Specialist | No Fextralife page exists under any title variant. The mechanic (medium armour stops reducing dodge) ships on specific archetypes as **Second Skin** (Soldier) -- see `talents-t1.md`. |

## Characteristic Training
**Characteristic Training: \<X\>** -- grants **+5** to the named characteristic, AND lets you improve that characteristic even if your archetype/origin normally wouldn't allow it. One talent exists per characteristic (WS, BS, STR, TGH, AGI, INT, PER, WP, FEL).

## Skill Talents
- **Base Skill: \<X\>** -- grants **+7** to the named skill and lets you improve it regardless of archetype/origin restrictions.
- **Advanced Skill: \<X\>** -- grants **+13** to the named skill AND lets you reroll failed tests of that skill (+1 attempt per test).

## Generic combat talents (universal or near-universal)
| Talent | Effect |
|---|---|
| Nimble | +10% dodge. (Fextralife: available to "All Archetypes" -- this is the universal-pool pick InEffect takes for Kibellah at Rank 5.) |
| Swift Movements | +2 Movement Points. |
| Tough as Steel | +12 wounds, further scaled by Toughness at +(10 x TGH bonus)% like base wounds. |
| Dual-Weapon Combat | Lets you attack with the off-hand weapon in addition to your normal one attack per round; that extra attack takes -20 WS/BS and costs +1 AP. |

> **Note on "combat talents that look generic but aren't":** several survivability/combat talents are actually archetype-restricted and live in the archetype files, not here -- e.g. Second Skin (Soldier), Thick Skin / Hardened Scars (Warrior), Hardened Body (Executioner), Pass Unscathed (Navigator), Swift Escape (Assassin), Martial Art / Point-Blank-class picks (Soldier/Arch-Militant), Sniper Expertise / Deadly Aim (Operative). If a "generic-sounding" talent isn't in this file, check the archetype tables.
