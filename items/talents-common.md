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
| Bolt Weapon Expert | Bolt weapon attacks gain +10% armour penetration. |
| Flame Weapon Expert | Flame weapon attacks cost -1 AP less to use (1 AP minimum). |
| Las Weapon Expert | Enemies suffer a -20% penalty to dodge against las weapon attacks. |
| Melta Weapon Expert | Melta weapon attacks gain +4 maximum damage. |
| Plasma Weapon Expert | Plasma weapon attacks gain +2 maximum damage. |

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
| Dual Weapon Specialist | Using the Sweep attack of the axes and Shove attack of the maces and hammers does not increase the AP cost or reduce the Weapon Skill or Ballistic Skill of another weapon; |
| Duelling Mastery | Grants +15% bonus to parry. |
| Grenadier | first grenade use in combat does not spend AP and does not count toward the attack limit that turn. |
| Hurt Like Hell | When firing heavy weapons, critical chance is increased by BS and critical damage is increased by 3x BS |
| It Will Not Die | Increases wounds by half of the character's level (rounded up). |
| Weapon Specialist | Sweep attack of the axes and Shove attack of the maces and hammers cost 1 less action point. |

> **Note on "combat talents that look generic but aren't":** several survivability/combat talents are actually archetype-restricted and live in the archetype files, not here -- e.g. Second Skin (Soldier), Thick Skin / Hardened Scars (Warrior), Hardened Body (Executioner), Pass Unscathed (Navigator), Swift Escape (Assassin), Martial Art / Point-Blank-class picks (Soldier/Arch-Militant), Sniper Expertise / Deadly Aim (Operative). If a "generic-sounding" talent isn't in this file, check the archetype tables.

---

## Companion-specific talents

Talents locked to one specific companion (not available to the Rogue Trader or other companions). Pasqal is a Tech-Priest; Marazhai and Yrliet are xenos companions with their own small talent pools alongside their archetype talents.

_source: Fextralife wiki talents table, manually clipped 2026-09-16 · capture: manual-clipping · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Pasqal

| Talent | Effect |
|---|---|
| Acceleration Protocols | Pasqal gains 4 MP in the first round of combat. Every successful melee attack grants Pasqal +(INT bonus / 2) MP for the next round. |
| Aiming Protocols | Pasqal gains +(5+INT) to Ballistic Skill and a +(10+INT)% to dodge reduction with plasma and melta weapon ranged attacks. |
| Close-up Scanning | Pasqal's melee attacks apply the machine spirit communion effect on all attacked enemies. |
| Exposing Communion | Pasqal's attacks and effects of the Expose Weakness ability gain bonuses against enemies under the effects machine spirit communion, as if those enemies had 2 more stacks of exploit. |
| Filtering Protocols | When Pasqal uses plasma or melta weapons the first time in a round, he gains a +1 AP. |
| Machine Spirit Scan Protocols | Machine Spirit Communion applies 1 stack of exploit on all affected enemies. |
| Manipulator Push | Manipulator mechadendrite attacks enemies in close combat, pushing them up to 2 cells away and dealing (WS + INT bonus) damage. This attack has (5 x Tech-Priest's PER bonus)% armour penetration. |
| Medicae Mechadendrite | The Tech-Priest can use their mechadendrite to restore the wounds of an ally once per combat. The ally against (6 + Medicae / 5) wounds. |
| Overcharge Protocols | Every time Pasqal uses plasma or melta weapons, his damage with these weapons increases by (5+INT)%. Stacks. If Pasqal does not shoot for 1 round, he loses all stacks. |
| Predictions Protocols | Pasqal gains a +(15+INT)% to dodge reduction and parry reduction with melee weapons. If an enemy dodges or parries his attack, the bonus is doubled for the next melee attack against this enemy. |
| Pulse Amplifier | Pasqal's arc rifle shots gain + (INT / 3)% dodge reduction against primary and secondary targets. |
| Scanner Mechadendrite | An additional servo-skull connected directly to the Tech-Priest's systems increases their Perception by +10. |
| Skirmish Protocols | While Pasqal is under the effects of machine spirit communion, his melee attacks deal an additional +(10+INT)% damage and gain (10+INT)% armour penetration. |
| Utility Mechadenrite | This mechadendrite is equipped with all kinds of tools to communicate with machine spirits. Increases Tech-Use and Demolition by +10. |

_Note: "Skirmish Protocols" (Pasqal, above) is a different talent from Soldier's "Skirmish Protocol" in `talents-t1.md` -- confirmed distinct mechanics despite the near-identical name._

### Marazhai

| Talent | Effect |
|---|---|
| Aeldari Equipment | Able to equip Aeldari armour. |
| Emboldened by Bloodshed | While Marazhai is bleeding, his fellowship and willpower are increased by +15. |
| Kabalite Dracon | Deals STR bonus rending damage to Marazhai and he starts bleeding. While Marazhai is bleeding, he gains +3 Resolve. |
| Mantle of Agony | While bleeding, Marazhai gains +(3 x TGH Bonus)% additional armour. |
| Prey on the Weak | While Marazhai is bleeding, every kill he makes grants him a stacking +5 bonus to weapon skill and ballistic skill. |
| Trueborn Superiority | When Marazhai makes an additional attack granted by Dual-weapon combat, using a drukhari weapon, that attack suffers no penalties and does not have its cost increased. |

### Yrliet

| Talent | Effect |
|---|---|
| Asuryani Outcast | At the start of her next turn (excluding extra turns), if possible, she makes an attack that cannot miss and does not count toward the attack limit per turn. |
| Path of the Outcast | When Yrliet kills a target with a single shot attack from aeldari weapon for the first time in a round, she immediately gains an additional attack. |
| Penetrating Sight | In My Sights gains additional armour penetration equal to PER%. |
| Prescient Sight | In My Sights gains additional dodge reduction equal to Ballistic Skill%. |
| Swift Sight | In My Sights costs only 1 AP. |

### Kibellah

Kibellah's companion talents (Crimson Tide, Dance of Blood, Dance of Thorns, Open the Veins, Wounds Streaming Blood, and others) are already documented under [`talents-origin.md`](talents-origin.md)'s "Death Cult Assassin (Kibellah)" section -- the 2026-09-16 wiki clip's Kibellah entries were all duplicates of that existing table and were not re-added here.

---

## Colony, conviction and quest-granted talents

Talents granted by a Rogue Trader colony trait, a Conviction rank (Iconoclast / Dogmatic / Heretical), or a specific quest/project completion -- not archetype, homeworld, or origin talents. Several of the quest-granted ones are voidship talents (they buff the flagship, not a character).

_source: Fextralife wiki talents table, manually clipped 2026-09-16 · capture: manual-clipping · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Colony Trait

| Talent | Effect |
|---|---|
| Aeldari Machine Taming | All allies gain +10 Lore (Xenos) and +(Lore (Xenos) / 5)% dodge reduction against xenos. |
| Bane of Scipione 84-249 | Grants the Rogue Trader and their allies +2 momentum for each human enemy killed in battle |
| Benevolent Protection | All allies increase their wounds by +(Lore (Imperium) / 15). |
| Blessing of the Data-Angels | All allies gain +5 Perception and +10% armour penetration. May Metal never betray the Master whose deeds please the Omnissiah. |
| Blood of Scipione 84-249 | The Rogue Trader gains +1 deflection and +3% hit chance. Refugess from the fallen hive toil without rest to prove that they deserve the honour of serving the protectorate. These servants have now been tasked with maintaining the Rogue Trader's equipment in perfect condition, and they do so with painstaking care. |
| Celestial Inspiration | Battle Start: Momentum +10. |
| Emperor's Voice | All allies gain +7 Persuasion. |
| Expert Cryptographer | All allies gain +7 Logic. The Rogue Trader's servants have succeeded in identifying and studying the patterns in the peculiar drawings made by convicts on Vheabos VI. |
| Janus Warlord | The Rogue Trader gains +10 Fellowship, +5 Weapon Skill, and +5 Ballistic Skill. |
| Keen Mind | All allies gain +3% dodge reduction against enemies. |
| Leader of the Engine Vandals | The Rogue Trader gains +1 MP. |
| Otherworldly Observer | All allies gain +7 Awareness. |
| Patron of Cults | All allies gain +15 Lore (Imperium). |
| Secrets of Ancient Cybersmiths | All allies deal +(Logic / 15)% more energy and machine damage. |
| Secrets of the Mutated Flesh | The Rogue Trader gains +10 Medicae. |
| The Hammer and the Cog | Medikits always heal +(3 x Rogue Trader's Iconoclast rank) more wounds. By humbling the monks and Tech-Priests, the Rogue Trader has gained a reputation as a great mediator. |
| Wastelander's Prayer | Decreases enemy critical damage by -15%. |
| Witch Collector | The Rogue Trader's party gain +(FEL bonus / 2) momentum when using any pysker or Navigator powers. |

### Conviction: Iconoclast

| Talent | Effect |
|---|---|
| Above the Thundering Guns | The Rogue Trader and two random allies start combat with temporary wounds equal to (their own resolve). Conviction: Iconoclast - Follower. |
| Courage and Steel | The Rogue Trader and their allies need 30 less momentum to activate a heroic act. Conviction: Iconoclast - Votary |
| Excellence | Any attacks from allies that may hit other allies will be dodged if possible. Any allied ability that may target an ally and has a resistance test will be resisted by allies. Conviction: Iconoclast - Zealot. |
| Master of Command | In the first round of every combat, the Rogue Trader and their allies gain +(2 + Rogue Trader's Iconoclast rank) additional MP. Conviction: Iconoclast - Adherent |
| Transcend the Potential | Once per battle the Rogue Trader may choose an ally. The target ally may immediately use their heroic act without spending momentum. >Not applicable to allies whose heroic act is on cooldown. Conviction: Iconoclast - Fanatic. |

### Conviction: Dogmatic

| Talent | Effect |
|---|---|
| Absolution | In the first round of combat, all critical hits scored by the Rogue Trader's party inflict burning. In addition, all fire damage suffered by enemies is increased by +1 for each Dogmatic rank. Conviction: Dogmatic - Adherent. >Burning: at the start of every turn the affected target suffers 10 damage and must pass an Agility resistance test with a -10 penalty to stop burning. |
| Grim Determination | The Rogue Trader and their allies gain a +10% chance to survive with 1 wound instead of falling unconscious. Conviction: Dogmatic - Follower. |
| Instrument of His Will | Until the start of their next turn, the Rogue Trader becomes immune to any attacks from daemons and xenos, and all daemons and xenos in a 5-cell radius consider them a priority target. >Can only be used once per battle. Conviction: Dogmatic - Zealot. |
| Path of Redemption | Any momentum expenditure by the Rogue Trader and their allies, including heroic acts, is reduced by -20%. Conviction: Dogmatic - Votary |
| Piercing Resolution | Once per battle the Rogue Trader may choose an ally (including themselves). For 1 round all the target's weapon attacks ignore enemies' armour. Conviction: Dogmatic - Fanatic. |

### Conviction: Heretical

| Talent | Effect |
|---|---|
| Daemonopathy | Once per battle the Rogue Trader may choose an ally (including themselves) and grant them a +20 bonus to all their characteristics for 2 rounds. After the effect fades, the target falls prone. Conviction: Heretical - Fanatic. |
| Destroy the Weak | For the first round of combat, everyone in the Rogue Trader's party gains a 25% chance to regain 1 AP after killing an enemy, however triggering this effect immediately manifests psychic phenomena. >Does not reset the cooldowns of attacks and abilities. Conviction: Heretical - Adherent. |
| Gifts of the Warp | Any psychic phenomena increase the momentum of the Rogue Trader's party by +(2 to 10) instead of decreasing it by -(1 to 5). Conviction: Heretical - Votary. |
| Power From Beyond the Veil | All weapons on the battlefield become warp-imbued for 1 round, gaining bonus damage equal to +(veil degradation level) and an additional +(5 X veil degradation)% armour penetration. >Can only be used once per combat. Conviction: Heretical - Zealot. |
| Resource Preservation | The Rogue Trader and their allies gain a +20% chance to save a combat stimulant or a medikit after using it. Conviction: Heretical - Follower. |

### Quest and colony one-off grants

Each of these is a single talent tied to one specific quest, project, or colony event -- not a repeating trait pool.

| Talent | Effect | Granted by |
|---|---|---|
| Champion of the Abyss | Permanent +2 bonus to Weapon Skill Tests and +5 bonus to Coercion Tests. | Bottomless Pit |
| Champion of the Darkness | Grants the ability to improve their Lore (Xenos) skill even if their background or archetype does not allow it. +5 to Willpower. | Bottomless Pit |
| Curse of the Abyss | Permanent -5 penalty to Willpower tests. | Bottomless Pit |
| Accusation of Heresy | The Rogue Trader and their allies gain +20% damage against daemons. | Crusade |
| Guidance of the Astronomican | The Rogue Trader gains a +10 bonus to all characteristics during warp encounter battles. This voidship's talent can be obtained after completing the Crusade Project. It applies to all archetypes. | Crusade |
| Advice of the Dark Sages | All allies deal +5% more damage to xenos. | Capella Biologis |
| Blessing of Saint Cognatius | All non-xenos allies gain a +5 bonus to all their characteristics and skills. | Sacred Comet |
| Blessing of the Fallen | The souls of the crewmen laid to rest in the Foulstone Cemetery send blessings to their ship. ~// The flagship gains a +5% bonus to evasion. This voidship's talent can be obtained after completing the Cemetery of the Faithful Project. It applies to all archetypes. | Cemetery of the Faithful |
| Frequency of Faith | All allies gain +(3 X ally's Dogmatic rank)% critical hit chance. | Good Tidings |
| Holy Man | Grants +10% damage for 2 turns and +20 temporary wounds when a character uses their origin ability. | Crucible |
| Master of Flame | All allies deal +10% damage with melta and plasma weapons. | Great Fire |
| Merciful Saviour | Each time an ally is healed in combat, the damage of this ally is increased by +4% until the end of combat. Stacks. | Shelter |
| Shield of Faith (Voidship's talent) | +30% to the prow shield sector. This voidship's talent can be obtained after completing A Celestial Protector Project. It applies to all archetypes. | A Celestial Protector |
| The Emperor's Retribution | +5% to critical hit chance against chaos enemies. This voidship's talent can be obtained after completing the The High Throne Project. It applies to all archetypes. | The High Throne |
| The Thrill of the Dead | Whenever any creature (enemy or ally) dies in combat, the Rogue Trader and their allies with Conviction - Heretical gain +1 to all their characteristics untill the end of combat. Whenever the Rogue Trader's flagship destroys any voidship in space combat, the flagship recovers 5% of its maximum hull integrity. | If you choose to "plunder the monastery" of Flowstone |
| Xenovivisectionist | All allies gain +12% dodge against xenos. | Forbidden Planet |
