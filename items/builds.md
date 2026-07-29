# Warhammer 40,000: Rogue Trader -- Builds

**status:** research-integrated
**last_reconciled:** 2026-05-27
**research_run:** P3 cascade 2026-05-23

Community-converged build recommendations for the MC. Party-composition notes in `mechanics.md` Companion Quests section.

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Psyker-Focused MC

**Path:** Sanctioned Psyker origin -> Pyromancer (or Sanctic) + Arch-Militant (or Master Tactician)
**Key gear:** Eyes of Joyeuse helmet (Janus "Pure Blood" tier-2 colony project, Ch2 -- build the project EARLY), Sanctified Staff / Blooddrinker Staff, Starmist Scarf (Ch4 merchants)
**Notes:**
- Pyromancer + Sanctic is the converged endgame base-game peak (without DLC Bladedancer)
- Psychic Shriek (Telepathy) is an alternative: single-target damage that bypasses armor and dodge
- Biomancy's Metabolic Overcharge is community-rated game-best but arrives late
- Pyromancy NOT recommended as starting discipline (Psy Rating 0 until level 10)
- Cassia + Mind Siege Telepath + Officer extra-turn chain-stun is a documented alternative for late Ch4/Ch5 (Russian StopGame.ru; English guides default to damage race)

**Conviction variant (Dogmatic):** Sanctic-heavy + Halo Device (Ch4); "The Emperor's Servant" achievement (Daring+ Dogmatic Votary completion)
**Conviction variant (Heretical):** Pyromancer or Telepath leaning into Veil Degradation for free Psy Rating via Chaos trinkets; unlocks Uralon (Ch4 end)
[Confirmed: Chris Williams walkthrough; A Little Bit Human; Steam Psyker threads; 5+ sources]

## Melee-Focused MC

**Path:** Warrior -> Assassin (mobile DPS) OR Warrior -> Vanguard (tank)
**Key gear:** Bloodthirster (early Ch1-2), Hekatarii Blade of Bloodthirst (mid-game, requires Drukhari proficiency), Hand of Xenocide (Kiava Gamma colony reward Ch2+)
**Homeworld pairing:** Death World + Crime Lord origin synergy (broad skill bonuses + STR/AGI/TGH)
**Notes:**
- Sword + pistol Warrior debated on Steam as better all-rounder below Unfair vs. Arch-Militant heavy stubber
[Confirmed: community consensus, 4+ sources]

## Ranged-Focused MC

**Path:** Soldier -> Arch-Militant
**Key weapon:** Calibrated heavy stubber (1 AP for 12-round burst -- cheapest sustained DPS in game); switch to heavy bolter from Ryzza (Ch4 acquisition) as endgame BiS
**Notes:**
- Heavy bolter does NOT require Bolt Weapon Proficiency (patch-current quirk)
- Heavy Weapon Proficiency reduces STR requirement by 25
[Confirmed: community consensus, 5+ sources]

## Hybrid Sniper-Utility

**Path:** Operative -> Bounty Hunter
**Key weapon:** Drukhari sniper rifle (Ch3 unique drop)
**Notes:** Pasqal templates this archetype path for skill coverage + debuffs
[Single source -- verify -- class: editorial-en (Chris Williams)]

## Officer Support

**Path:** Officer -> Grand Strategist (zone control + extra turns) OR Officer -> Master Tactician (momentum AoE)
**Notes:**
- Officer is the converged early pick; no second Officer available until Cassia (Ch1 end)
- Grand Strategist + zone-control abilities enables the Cassia + Mind Siege chain-stun strategy (Ch5)
[Confirmed: 4+ sources]

## Party Composition Templates

**Early Ch1 (before full companion roster):** Officer MC + Argenta (Flamer DPS) + Pasqal (Tech-Use / Operative) + Heinrix (Warrior/Biomancer -- "stretched thin" per Chris Williams)
**Ch2-3 general:** Heavy CC tools for Commorragh arena waves (Pyromancer Inflame, Cassia Lidless Stare, grenade stacking)
**Ch5 C'tan fight:** Stack burst output to race clone destruction; heavy bolter (ranged) or Pyromancer self-fire + Hand of Xenocide (melee); Alt+1-6 for direct party targeting

## Exemplar Builds (Tier 3 capstones, P3 confirmed)

All Exemplar builds require Daring+ difficulty to unlock their conviction-path ending. Exemplar talents synthesize the prior two archetype trees.

| Exemplar path | T1 -> T2 -> Exemplar | Playstyle | Notes |
|---|---|---|---|
| Bladedancer-Executioner-Exemplar | Warrior -> Bladedancer (DLC T1) -> Executioner (DLC T2) | Mobile melee AoE burst | DLC-exclusive; Death Waltz cleave + Carnival of Misery; highest single-fight burst in community testing |
| Soldier-Bounty Hunter-Exemplar | Soldier -> Bounty Hunter -> Exemplar | Sustained ranged + target debuff | Generic-capable; pairs with calibrated heavy stubber |
| Officer-Master Tactician-Exemplar | Officer -> Master Tactician -> Exemplar | AP-generation support | Extra-turn economy; best for keeping Cassia + psykers powered |
| Operative-Assassin-Exemplar | Operative -> Assassin -> Exemplar | Crit-focused skirmisher | Drukhari sniper synergy; Yrliet mirrors this path |
| Operative-Overseer-Exemplar | Operative -> Overseer (DLC T2) -> Exemplar | Familiar + battlefield control | DLC-exclusive (Lex Imperialis); Cyber-Mastiff frontline; Psyber-Raven scout |
| Warrior-Vanguard-Exemplar | Warrior -> Vanguard -> Exemplar | Armored tank / frontline | Power Armour investment worth it at Exemplar tier; Abelard mirrors this path |

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Disagreements in Community

- Sword + pistol Warrior vs. heavy stubber Arch-Militant as Ch2 general-purpose build
- Pyromancy vs. Telepathy for single-target psyker damage (Telepathy bypasses defenses; Pyromancy is better AoE)
- Biomancy's late arrival rate vs. its peak performance rating
- Yrliet build: TheGamer promotes Operative+Assassin sniper; InEffect v1.5 explicitly counters: "Bounty Hunter all the way" -- use-case dependent

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Active Bugs Affecting Builds (Patch 1.5)

**Read before investing in extra-attack talent chains.**

**Dual-weapon -20 penalty (all multi-attack builds):** Every attack after the first in a turn applies -20 BS/WS, even single weapon. Any talent granting an extra attack also applies the -20 to those granted attacks. Affects Arch-Militant, Bounty Hunter, and Assassin most severely. Factor this into damage expectations -- actual DPS from extra-attack chains is lower than tooltips suggest.
> **Cross-system dependency** -- see `dependencies.md` DEP-009: This penalty is independently documented in mechanics.md Known Bugs with the same affected archetypes.

**Pyromancer inferno staff melee classification:** Inferno power staves count as melee in Patch 1.5 and can be dodged/parried. Power-only psyker builds using inferno staves should note this until patched.

See `mechanics.md` Known Bugs for full details.
_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Party Synergies (Community-Discovered)

**Cassia force-move + Pasqal AoO axe:** Cassia force-moves enemies into Pasqal's melee threat range; Pasqal's AoE-on-AoO axe then hits all clustered enemies without spending AP. Often clears large portions of a map before other characters act. See crew/cassia-orsellio.md and crew/pasqal-umberto-i.md.

**Bounty Hunter heroic LOS technique:** The BH heroic fires one attack per active Mark Prey target regardless of LOS. Position so that only the highest-priority target is in LOS when the heroic fires -- all attacks focus on that single target. Most effective after stacking as many prey charges as possible before the heroic turn.

**Astra Militarum Unflinching Heroism loop:** Synergizes with momentum-generating parties. Orchestrated Firestorm Heroic can be talented for infinite use, allowing repeated Unflinching Heroism triggers per combat.

**Commissar + Overpenetration:** At All Costs (shoot; if target dies, grant ally extra turn) works with Overpenetration shots piercing multiple enemies -- any kill in the penetration chain triggers the grant. Enables multi-kill setup chains, especially with Bounty Hunter.
> **Cross-system dependency** -- see `dependencies.md` DEP-012: This interaction is independently documented in mechanics.md Combat System (Origins section).

_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

---

## Level-by-Level Talent Pick Guides (doctor 2026-05-27)

Specific talent picks per level bracket for the five community-converged MC builds. For full talent descriptions see [`talents-t1.md`](talents-t1.md), [`talents-t2.md`](talents-t2.md), [`talents-exemplar.md`](talents-exemplar.md), [`talents-dlc.md`](talents-dlc.md).

_source: doctor research 2026-05-27 (Neoseeker InEffect build series · Neoseeker Revan619 series v1.5 · Steam Community "Revan619's Collection of Unfair Builds 1.5") · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Version notes:** Build timings reflect Patch 1.5. Most source guides explicitly state v1.5+. Pre-1.3 guides under-rate Officer-Vanguard; pre-1.2 guides overstate Arch-Militant damage.

### Build 1: Psyker MC (Pyromancer + Arch-Militant)
**Stat priority:** WP > BS > AGI > INT; dump STR.
**Homeworld:** Forge World or Death World. **Origin:** Sanctioned Psyker (Pyromancer).

**Levels 1-15 (T1: Soldier)**
- L1: Ignition + Run and Gun + Cover Mastery
- L2-3: Combat Acrobat + Exploit Surroundings
- L4-5: Combat Addict + Dash
- L6-7: Rapid Reload + Backdraft
- L8-9: Psy Rating advance + Unpredictable
- L10-11: Body of Flames + Tenderise
- L12-13: Combat Medicae or Constant Vigilance + Pain Channelling dip
- L14-15: Get In Their Faces + Pyromancy advance

**Levels 16-25 (early T2: Arch-Militant)**
- L16: Versatility keystone
- L17: Wildfire
- L18: Quick Adaptation
- L19: Ultimate
- L20: Eye of the Storm
- L21: Adaptability + Devastating Attack
- L22: Aggressive Onslaught
- L23: Critical Versatility
- L24: Flashfire
- L25: Master of Arms

**Levels 26-35 (late T2)**
- L26: Heavy Weapon Proficiency
- L27: Ultimate upgrade
- L28: Calm and Steady + Molten Beam
- L29: Distract + Pyromancy advance
- L30: Coordinated Tactics + Hymns of Hatred
- L31: Priority Target Hunter
- L32: Armsmaster + Cautious/Confident Approach
- L33: Reckless Rush
- L34: Versatile Force
- L35: final common

**Levels 36-45 (Exemplar)**
- L36: Eager for Battle + Skirmish Protocol
- L37: Critical Velocity
- L38: Cataclysm
- L39: Inflame or Molten Beam
- L40: Extermination
- L41: Perfection Under Fire
- L42: Firestorm Mastery + Hammer of the Emperor
- L43: Inevitable
- L44: Shot Through
- L45+: Remaining Pyromancy advances

---

### Build 2: Psyker MC (Sanctic + Grand Strategist)
**Stat priority:** WP > INT > FEL.
**Origin:** Sanctioned Psyker (Sanctic). **Homeworld:** Voidborn (Be Smart talent lets INT replace FEL).

**Levels 1-15 (T1: Officer)**
- L1: VoC
- L2: Sanctic discipline
- L3: Commanding Voice
- L4-5: Be Smart + Personal Oversight
- L6: Bring It Down!
- L7: Lasting Impression
- L8-9: Solitary Authority + Psalms of Heroes
- L10-11: Psy Rating + Inspiring Resolve
- L12: Logistical Superiority
- L13-14: Stronghold (T1) + weapon proficiency
- L15: Unflinching Heroism

**Levels 16-25 (early T2: Grand Strategist)**
- L16: Combat Tactics keystone
- L17-18: Frontline Tactics + Sharpshooter Position
- L19: Ultimate
- L20: Combined Stratagem
- L21: Pinpoint Strikes
- L22: Veiled Position
- L23: Combat Locus
- L24-25: Trenchline Mastery + Word of the Emperor

**Levels 26-35**
- L26: staff proficiency
- L27: Ultimate upgrade
- L28: Strategic Reserve
- L29: Iron Discipline
- L30: Bulwark Strategy
- L31: Field Adjustments
- L32: Light of the Emperor
- L33: Officer talent re-pick
- L34-35: Hammer of the Emperor

**Levels 36-45 (Exemplar)**
- L36: Eager for Battle + Officer T1 leftover
- L37: Firebrand
- L38: Unflinching
- L39: missed Officer ability
- L40: Bringer of Light
- L41: Hammer of the Emperor
- L42: Shield of the Emperor
- L43: Through Discipline
- L44: Perfection Under Fire
- L45+: Eyes of Joyeuse / Drusian rep path

---

### Build 3: Ranged MC (Soldier + Arch-Militant)
**Stat priority:** BS > AGI > STR > PER.
**Homeworld:** Fortress World. **Origin:** Astra Militarum Commander.

**Levels 1-15 (T1: Soldier)**
- L1: Run and Gun
- L2-3: Combat Acrobat + Exploit Surroundings
- L4: Rapid Reload
- L5: Cover Mastery
- L6-7: Combat Addict + Concentrated Fire/Rapid Fire
- L8: Unfaltering Fire
- L9: Tenderise
- L10-11: Get In Their Faces + Unpredictable
- L12: Bolt/Plasma/Heavy proficiency
- L13: Vengeance
- L14: Skirmish Protocol
- L15: Wide Spread

**Levels 16-25 (T2: Arch-Militant)**
- L16: Versatility
- L17: Wildfire
- L18: Quick Adaptation
- L19: Ultimate
- L20: Aggressive Onslaught
- L21: Adaptability
- L22: Critical Versatility
- L23: Eye of the Storm
- L24: Master of Arms
- L25: Heavy Armour Proficiency

**Levels 26-35**
- L26: Versatile Force
- L27: Ultimate upgrade
- L28: Kick
- L29: Distract
- L30: Coordinated Tactics
- L31: Priority Target Hunter
- L32: Flashfire
- L33: Armsmaster or Devastating Attack
- L34: Confident Approach
- L35: Reckless Rush

**Levels 36-45 (Exemplar)**
- L36: Eager for Battle
- L37: Critical Velocity
- L38: Inevitable
- L39: Shot Through
- L40: Peak Condition
- L41: Cataclysm
- L42: Extermination
- L43: Cumulative Mastery
- L44: Masterful Display
- L45+: Tough as Steel or Push Through

---

### Build 4: Melee MC (Warrior + Assassin)
**Stat priority:** WS > AGI > STR > TGH.
**Homeworld:** Death World. **Origin:** Crime Lord (Sure-Fire Plan synergy with Killing/Escape Plan).

**Levels 1-15 (T1: Warrior)**
- L1: Charge
- L2-3: Combat Reflexes + Defensive Manoeuvres
- L4: Endure
- L5: Contempt
- L6: Sworn Enemy
- L7: Sworn Enemy talent or Clenched Teeth
- L8: Rigorous Training
- L9: Desolation
- L10: Combat Master
- L11: Enrage
- L12: Heavy Armour Proficiency (or skip for AGI)
- L13: Endurance
- L14: Cripple
- L15: Tenacious Effort

**Levels 16-25 (T2: Assassin)**
- L16: Openings keystone
- L17: Death Whisper
- L18: Strategic Lethality
- L19: Ultimate
- L20: Imminent Demise
- L21: Deadly Calculation
- L22: Lethality Heightens
- L23: Killer Instinct
- L24: Perfect Opening
- L25: Lone Killer

**Levels 26-35**
- L26: Bringer of Doom
- L27: Ultimate upgrade
- L28: Elusive Shadow + Stalking Aspect
- L29: Slowing Onslaught
- L30: Knife in the Dark
- L31: Bleed Out
- L32: Gruesome Gust
- L33: Morbid Pirouette
- L34: Poised
- L35: common

**Levels 36-45 (Exemplar)**
- L36: Eager for Battle
- L37: Critical Velocity
- L38: Perfection Under Fire
- L39: Warrior leftover
- L40: Peak Condition
- L41: Cumulative Mastery
- L42: Extermination
- L43: Cataclysm
- L44: Push Through
- L45+: Conviction-gated Exemplar talents

---

### Build 5: DLC Melee (Bladedancer + Executioner)
**Stat priority:** WS > AGI > WP > Medicae (skill).
**Homeworld:** Death World (Wounded Beast). **Origin:** Sanctioned Psyker (Pyromancer) for Orchestrate Flames synergy.

_source: doctor research 2026-05-27 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:void_shadows_

**Levels 1-15 (T1: Bladedancer)**
- L1: Blade Dance
- L2: Athletics or Medicae
- L3: Death From Above
- L4: Balancing on the Edge
- L5: **Common Talent pick** -- options come from your homeworld + origin + universal pools, NOT the Bladedancer tree (see [`talents-homeworld.md`](talents-homeworld.md), [`talents-origin.md`](talents-origin.md), [`talents-common.md`](talents-common.md)). For a Death World MC, Heavy Armour Proficiency (universal) is available here; "Sword Mastery" is NOT a confirmed talent name -- the universal sword upgrade is **Blade in His Hand** (archetype) / weapon Experts. NOTE: Heavy Armour Proficiency is NOT in companion Kibellah's pool (she's Voidborn + Death Cult Assassin; player-confirmed) -- her Rank 5 universal pick is **Nimble** (+10% dodge).
- L6: Captive Audience or Blood Oath
- L7-8: Medicae and Athletics
- L9: Ultimate
- L10: Facing the End
- L11: Veil of Blades
- L12: Spinning Blades
- L13: skill
- L14: Death Warden
- L15: Blade in His Hand

**Levels 16-25 (T2: Executioner)**
- L16: Scourging Strikes + Forced Repentance (auto)
- L17: Where It Hurts
- L18: Anatomy Expert
- L19: Ultimate
- L20: Fragile Playthings
- L21: Blood Trail
- L22: Forced Endurance
- L23: Punisher's Insight
- L24: Blade of Light
- L25: Death from Plagues

**Levels 26-35**
- L26: Critical DoT
- L27: Carnival of Misery I
- L28: Death in the Air
- L29: Biophysical Distortion (Biomancy dip)
- L30: Armour Strip
- L31: Wound Drinker
- L32: Bleeding Strike
- L33: Carnival of Misery II
- L34: Pain Resonance Mastery
- L35: Carnival of Misery III

**Levels 36-45 (Exemplar)**
- L36: Eager for Battle
- L37: Critical Velocity
- L38: Cataclysm
- L39: Acrobatic Artistry or Exsanguination
- L40: Extermination
- L41: Cumulative Mastery
- L42: Corpus Conversion or Peak Condition
- L43: Inflame
- L44: Psychic Awakening (if not psyker origin)
- L45+: Hammer of the Emperor or remaining DoT capstones

---

## Cross-Archetype Talent Synergies (Top 10)

The mechanics behind the most impactful T1+T2 talent combinations.

_source: doctor research 2026-05-27 (Fextralife talent text · Reddit r/RogueTrader build threads · GameSkinny multi-archetype synergy guides) · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

| T1 Talent | T1 Archetype | T2 Talent | T2 Archetype | Synergy mechanism |
|---|---|---|---|---|
| Desolation | Warrior | Lone Killer | Assassin | Desolation gives +AGI bonus damage on isolated enemies; Lone Killer grants +20% dodge/dodge reduction vs. full-wound enemies -- both prefer same opener (charge isolated, full-HP target) and dodge boost feeds Lethality |
| Combat Reflexes | Warrior | Retaliation | Vanguard | Combat Reflexes cuts AoO damage you take; Retaliation triggers AoO on priority-target enemies entering your space -- punishment engine without trading hits |
| Unflinching Heroism | Officer | Heroic Inspiration | Master Tactician | Officer-granted AP triggers +1 to all characteristics per AP gained; MT begins combat with tactical advantage stacks = enemy count, then Inspire/Linchpin scale on those buffed allies -- loop snowballs together |
| Commanding Voice | Officer | Combined Stratagem | Grand Strategist | VoC extends ability range; Combined Stratagem grants Officer abilities full range to allies in Combat Tactics areas -- free aim on every Officer ability across the map |
| Combat Addict | Soldier | Adaptability | Arch-Militant | Each damage instance +1% crit damage; gaining versatility stack gives +5% crit chance -- multiplicative crit DPS curve snowballs faster than either alone |
| Rapid Reload | Soldier | Aggressive Onslaught | Arch-Militant | Heroic/desperate trigger grants +1 damage and +10% damage; Rapid Reload's free reload lets you fire enough to realize the bonus on the same turn |
| Joint Analysis | Operative | Catch and Maim | Bounty Hunter | Joint Analysis seeds exploits; Catch and Maim applies removable armour/dodge debuff per hit -- each hit stacks both, dropping target defenses fast |
| Hard Strike | Operative | Perfect Opening | Assassin | Hard Strike at PER 10+ grants +1 AP and ignores deflection; Perfect Opening adds % chance to deal +5% max wounds when hitting an opening -- extra AP enables second opening hit per turn |
| Spinning Blades | Bladedancer | Forced Repentance | Executioner | Each parry +1 Blade Dance attack (max AGI bonus stacks); Forced Repentance procs extra DoT instance every time you reapply same-type DoT -- more Blade Dance hits triggers more reapplications |
| Death Warden | Bladedancer | Anatomy Expert | Executioner | Death Warden: Medicae = WS; Anatomy Expert: max wounds = Medicae -- together wounds scale off WS, eliminating TGH investment and producing huge HP on high-WS character |
