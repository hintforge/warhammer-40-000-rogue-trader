# Warhammer 40,000: Rogue Trader -- Mechanics

**status:** research-integrated
**last_reconciled:** 2026-05-27
**research_run:** P3 cascade 2026-05-23

Core game-system rules. Stable cross-zone knowledge surface. Do not bloat with per-zone or per-item facts.

## Level-Up UI -- Thumbs Icon

A thumbs-up icon appears next to characteristics in the Available Characteristics screen during level-up. It marks the game's recommended picks for that character's archetype -- safe choices that are unlikely to result in a bad build. It does not indicate the theoretically optimal pick for a focused build; strong options sometimes appear lower in the list without a thumb. Use as a sanity check, not a directive.

_source: Steam community r/RogueTraderCRPG + Warhammer 40k Rogue Trader Steam Discussions 2026-06-08 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

---

## Archetype System

Three-tier progression. One archetype per tier; Tier 2 depends on Tier 1 selection.

**Tier 1 (Levels 1-15):** Warrior, Officer, Soldier, Operative.
**Tier 2 (Levels 16-35):** Assassin, Arch-Militant, Bounty Hunter, Grand Strategist, Master Tactician, Vanguard (each Tier 1 grants access to ~3 of these); Overseer (Lex Imperialis DLC, T2) requires Officer/Operative or Arbitrator/Sanctioned Psyker/Unsanctioned Psyker origin.
**Tier 3 / Exemplar (Levels 36-45):** capstone advanced talents derived from the prior two archetypes.

DLC archetypes: Bladedancer (T1, Void Shadows), Executioner (T2, Void Shadows), Overseer (T2, Lex Imperialis), Arbitrator origin (Lex Imperialis).

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

See `items/upgrades.md` for full archetype talent-tree details.

## Conviction System (Dogmatic / Iconoclast / Heretical)

Three mutually-exclusive paths shaped by cumulative dialogue and quest choices throughout the run.
- **Dogmatic** -- Imperial orthodoxy; gates Incendia Bastaal-Chorda as secret Ch4 companion; Halo Device synergy; specific quest resolutions.
- **Iconoclast** -- pragmatic humanism; gates Calligos Winterscale as secret Ch4 companion; some dialogue bypasses combat.
- **Heretical** -- chaos-aligned; gates Uralon as secret Ch4 companion (requires Prologue blade-fragment dialogue + Sameth name reveal). High-risk high-reward: companion loyalty breaks possible at Ch4 Liege confrontation.

Conviction ranks progress: **Follower -> Adept -> Believer -> Votary -> Zealot**. Capstone companion reactions trigger at the Zealot rank for several companions (Heinrix, Argenta, Ulfar, Yrliet).

All three Votary endings (Deepest Conviction / Merciful Soul / The Emperor's Servant / Sweet Perdition / Chaos Incarnate) require **Daring+** difficulty. Conviction-path content is `spoiler: story` -- the persona does not reveal path-specific outcomes without tier raise.

> **Cross-system dependency** -- see `dependencies.md` SEQ-009: Each conviction path gates a different secret companion (locks-and-keys in `nav/architecture.md`; roster in `crew/index.md`); Uralon's extra Prologue requirements are the easiest to miss -- the blade-fragment dialogue must be chosen at the very start of the game.
> **Cross-system dependency** -- see `dependencies.md` DEP-003: Dogmatic specifically enables the Sanctic psyker + Halo Device build stack and The Emperor's Servant achievement (Daring+ Dogmatic Votary completion); see `items/builds.md` and `achievements.md`.
> **Cross-system dependency** -- see `dependencies.md` SEQ-011: Reaching Heretical Zealot at the Ch4 Liege confrontation triggers simultaneous permanent departure of Heinrix, Argenta, Ulfar, and Yrliet -- all four companion quest chains lock at the same moment.
_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: story_

## Psyker Disciplines

Five disciplines. Each has an innate starting power plus ~8 unlockable powers and 8 unique talents.

| Discipline | Governing stats | Notes |
|---|---|---|
| Biomancy | Psy Rating + Willpower | Metabolic Overcharge rated game-best by community; arrives late |
| Divination | Psy Rating + Willpower | Support/debuff focus |
| Pyromancy | Psy Rating + Willpower | AoE damage; not recommended as starting discipline (Psy Rating 0 until level 10) |
| Sanctic | Psy Rating + Resolve | Dogmatic synergy; Halo Device pairing |
| Telepathy | Psy Rating + Willpower | Psychic Shriek bypasses armor and dodge; chain-stun CC |

Psy Rating gated at character levels 10 / 20 / 30 / 40. A psyker is weakest in levels 1-9 before the first Psy Rating perk lands.

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

See `items/abilities.md` for full discipline power lists.

## Veil Degradation

Psychic power use accumulates Veil Degradation (VD). Degradation decreases by 1 per round at combat end; minor power +1 VD, major power +3 VD.

| VD range | Effect |
|---|---|
| 0-14 | Standard psychic phenomena chance: Sanctioned `5 + PR`%; Unsanctioned `10 + 2*PR`% |
| 15-20 | Elevated phenomena chance: Sanctioned `10 + 2*PR`%; Unsanctioned `20 + 4*PR`%; major powers can roll **Perils of the Warp** (push, damage, daemon summon) |

**Key mitigation:** Cassia's first staff upgrade reduces VD by 10 and wards against warp damage -- the primary management lever. Stable Routes + Stabilizing Factor + Inscribed Soul + Cassia anti-Veil talents stack for VD-heavy zones.

**Idira exception:** Unsanctioned psyker carries a flat 5% Perils chance regardless of VD (origin penalty, trades against +1 starting Psy Rating).

**Global meter:** VD is a single shared pool for the entire party -- any psyker power cast by any party member adds to the same counter. Not per-character.

**Unsanctioned psyker class:** Idira and any character who takes the Exemplar Psychic Awakening talent are unsanctioned psykers: +1 Psy Rating, but increased phenomena chance and the 5% Perils floor at 0 VD (see Idira exception above). Exemplar Psychic Awakening specifically makes otherwise-sanctioned characters unsanctioned.
> **Cross-system dependency** -- see `dependencies.md` DEP-011: Exemplar Psychic Awakening (items/talents-exemplar.md) converts an otherwise-Sanctioned character to unsanctioned status, with all phenomena-rate and Perils implications documented in both files independently.

**Common error:** "Veil Degradation always starts at 0" is false -- Chaos-heavy zones (Hallowed Electrodunamic Cenobium Ch1, Commorragh Chasm Ch3 starting at VD 12-15) and scripted triggers can produce VD spikes from turn 1.
[Confirmed: 5+ sources; StopGame.ru first documented zone VD elevation]

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**[BUG Patch 1.2+, persists Patch 1.5] VD animation bug -- IMPORTANT:** If "skip non-attack animations" is enabled in combat speed settings, non-attack psy powers grant zero VD increase. VD gain is tied to the casting animation actually playing. Also (1.5 regression): casting from behind cover (psyker steps out to cast, steps back in) may also fail to register VD even with animations on. If your psyker never accumulates VD or seems immune to phenomena buildup, check this setting first. This is why some sanctioned runs feel "safe" -- VD is being suppressed artificially.
_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Navigator's Insight

Resource spent to chart safe routes between star systems. Greened routes reduce warp-event probability. Community reports starvation in late-game (1-2 points per system insufficient for multiple route attempts). Cassia levels up Navigator's Insight pool.

**Per-system route costs (approximate):** standard systems 1-2 NI; contested warp zones 3-4 NI; Ch4-5 deep expanse systems 4-6 NI. Budget 2-3 NI per hop to avoid shortage.

**Largest lump-sum sources:**
- House Orsellio deal (Act 2): +15 NI -- highest single gain in the game; accept Felek's terms (see `factions/navis-nobilite.md`).
- Pulvis Platinum system exploration: +10 NI.
- Warp Reef anomaly resolution: +6 NI.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Warp travel route colors (after scripted events are exhausted):**

| Color | Meaning |
|---|---|
| Green | No event |
| Yellow | Event fires but usually no choice prompt; small chance of prompt fight or cargo-cancel option |
| Orange | Almost always a fight with no prompt + some ship damage |
| Red | Very likely crew kill -- avoid unless prepared |

_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Profit Factor (Economy)

Profit Factor (PF) replaces traditional gold/currency. It is an **access gate, not a spend.** Buying an item does not reduce your PF -- if your PF >= the item's PF requirement you can buy it freely.

- Starting PF: 10. Merchants stock items at or below your current PF; higher PF unlocks higher-tier wares.
- **Reputation** with a faction is a separate gating layer -- both PF and Reputation must meet thresholds to access specific wares.
- **Respec costs Profit Factor.** Avoid unnecessary respeccing to preserve your PF level.

**Primary PF sources:**
- Main story progression (automatic gains per chapter)
- Dialogue -- "insist on a reward" options (typically Commerce skill check gated)
- Contracts (Contracts page on voidship; typically +2 to +3 each)
- Colony projects (most impactful long-term; +1 to +7 per project; some carry -5 penalties)

**Janris Danrok (High Factotum, voidship; available all chapters):** dialogue "I would like to order the shipping and transportation of some goods" opens faction vendor access from the ship without traveling to Footfall. Critical QoL -- use between zones to restock.

> **Cross-system dependency** -- see `dependencies.md` DEP-007: Janris Danrok is the sole vendor access point during the Ch3 Footfall cordon (E07/PON-001); documented independently in `nav/architecture.md` fast-travel network and `items/consumables.md` merchant table.

_source: Game Rant / Fextralife / Steam community 2026-05-24 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Inventory, Looting, and Cargo

**Two distinct item pools:**
- **Character inventory** -- items equipped on or carried by party members. Opened with `I`.
- **Cargo hold** -- looted goods stored aboard the voidship; tracked as category stacks filling toward 100%. Opened with `B`.

**Looting:**
- Interact with dead enemies or world containers (approach + prompt). A loot window opens; take items individually or take all. Weapons / armor can go directly to character inventory or be right-clicked -> "Add to Cargo."
- **Exception:** Void cargo from space combat (e.g., trophies) must be manually moved to inventory before registering in the cargo tracking system.

**Cargo system:**
- Looted "goods" items auto-sort into cargo stacks by category. Each stack fills toward 100%; at 100% that batch is ready to trade. Stacks can exceed 100% -- the system auto-creates a new stack. No penalty for overfilling.
- To sort cargo from anywhere: drop an item, then pick it back up. This triggers the temporary-container UI for free sorting between cargo, inventory, and ground.
- Match cargo types to factions -- different factions prefer different cargo categories; mismatched cargo yields lower Reputation gains.

**Trading cargo:**
- Cargo is **not sold for PF.** It is traded to factions for **Reputation.** High Reputation improves a faction's merchant stock and tier access.
- Reputation is not freely stackable across all factions -- maximizing one limits others. Prioritize factions whose wares match your build and conviction path.
- Janris Danrok "shipping and transportation" dialogue handles all cargo trades from the voidship (see Profit Factor section above).

_source: Steam community / Game Rant / search snippets 2026-05-24 · capture: web_fetch + community · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Combat System

Turn-based tactical combat. Action points (AP) and Movement Points (MP) per character per turn. Momentum system grants extra actions on chain kills.

Key mechanics:
- **Dodge/evasion** -- high AGI characters (Drukhari, Aeldari, Assassin archetype) rely on dodge as primary defense.
- **Suppression** -- ranged burst fire imposes accuracy penalties; effective against high-dodge enemies.
- **Psyker Perils** -- see Veil Degradation above.
- **Difficulty** -- Story / Normal / Core / Hard / Daring / Grim Darkness (ironman). Difficulty can be changed mid-run except Grim Darkness.
- **Co-op** -- up to 6 players added free post-launch.
- **Area attacks and dodge bypass:** Enemies dodge area attacks by physically moving out of the affected area (max 3 cells). Angle the AoE to cover all 3-cell escape paths and the enemy cannot dodge at all -- more effective than centering on the target.
- **Bonus turns do NOT trigger start/end-of-turn effects:** Most buffs, damage-over-time, and cooldown ticks marked "start/end of turn" do not fire during bonus turns unless explicitly stated. "Round" and "turn" are used interchangeably in tooltips; bonus turns skip nearly all duration effects.
- **Heroic act stops per-turn resolve gain:** Once a character uses their Heroic act in combat, they stop gaining resolve per turn for the rest of that combat. Per-turn resolve is the smallest source, so the practical impact is minor.
- **Single-shot talents always use the first weapon ability slot:** Any talent or ability that causes a "single shot" uses weapon ability slot 1. This interacts with shotguns (special-first-shot), flamers, and quick-fire laspistols (which only have their specials in slot 1).

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
_source (area/bonus/heroic/single-shot): reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Known Bugs (Patch 1.5 / Build 21262645)

**Ship event softlock ("last land party" bug):** Resolving a ship event while the game expects the RT to be the last character aboard can lock the ship menu. Workaround: before resolving any pending ship events after returning from a surface mission, land on any surface zone and immediately leave without doing anything, then return to the ship -- this resets the party-tracking flag.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**[BUG Patch 1.5 regression] Pyromancer inferno staff melee classification:** Inferno power staff attacks are classified as melee, allowing enemies to dodge and parry them. Cripples power-only psyker builds relying on inferno staff output. No confirmed fix as of Build 21262645.
_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**[BUG multi-patch, present Patch 1.5] Dual-weapon -20 BS/WS penalty on all extra attacks:** Every attack after the first in a turn applies the dual-weapon -20 BS/WS penalty, even with a single weapon equipped. Any talent or ability that grants an extra attack also applies the -20 penalty to those granted attacks. Affects all multi-attack builds (Arch-Militant, Bounty Hunter, Assassin). Factor into DPS expectations when planning extra-attack talent chains. See `items/builds.md` bug flags.
> **Cross-system dependency** -- see `dependencies.md` DEP-009: This bug directly degrades the effective DPS of extra-attack talent chains; both this file and items/builds.md independently document the same affected archetypes and the same penalty value.
_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**[BUG present Patch 1.5] Cassia turn reset via Grand Strategy zone drops:** Cassia occasionally resets her full turn (all AP and cooldowns restored) when dropping Grand Strategy zones. Triggers fairly consistently; up to 3 full turns observed in a single combat. Whether intentional is unconfirmed. See `crew/cassia-orsellio.md`.
_source: reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**[BUG player-observed, intermittent] White wall blocking map visibility:** Large white wall appears on the map, blocking vision. Occurs intermittently across multiple sessions; game reload clears it. No community-documented root cause or fix found (web search 2026-06-27). Possible causes: VRAM/shader cache hiccup, or graphics settings reset by Nvidia GeForce Experience. If it recurs, check Options > Graphics for zeroed settings before reloading.
_source: player observation 2026-06-27 · capture: manual_paste · confidence: low · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Homeworlds (character creation, base game -- 6)

| Homeworld | Stat bonuses | Penalty | Origin trait |
|---|---|---|---|
| Death World | +5 STR/AGI/TGH | -5 FEL/INT | Survival Instinct |
| Forge World | +5 INT/TGH | -5 FEL | Forged for a Purpose |
| Fortress World | +5 PER/WP | -5 FEL | Never Stop Shooting |
| Hive World | +5 FEL/AGI | -5 WP | Strength in Numbers |
| Imperial World | no modifiers | -- | Humanity's Finest (+10 to chosen characteristic, half to non-xenos allies) |
| Voidborn | +5 WP/INT | -5 STR | Fortune (20% reroll) |

"Noble World" is not a homeworld -- Noble is an Origin.

**Voidborn -- Be Smart talent:** Substitutes INT for FEL in ALL formulas in the game (not just skill checks), including Resolve (normally FEL-based) and any formula listing both stats (INT+FEL becomes INT+INT). Distinct from Forge World's Calculated Relations, which applies only to skill checks. Build 2 (Sanctic + Grand Strategist) specifically targets this.

**Death World + Confident Approach trap:** Death World's crit-chance bonuses become useless if you take Confident Approach (which changes the hit mechanic in a way that invalidates crit synergies). If planning an AM build with Confident Approach, do not rely on Death World's crit bonuses.

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
_source (Be Smart / Death World trap): reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Origins (character creation, base game -- 7 playable + 1 conditional)

| Origin | Key trait / ability | Notes |
|---|---|---|
| Astra Militarum Commander | Suppression Fire! | Imperial Guard officer; ranged suppression focus |
| Commissar | At All Costs: mark enemy -> ally that kills it gets extra turn +2 AP/+3 MP | High turn-economy potential |
| Crime Lord | broad skill bonuses | Melee-focused; pairs well with Death World homeworld |
| Ministorum Priest | War Hymn; +5 TGH/WP/Lore(Imperium)/Medicae | Support/tanky |
| Navy Officer | dual-wield / counter-attack focus | Ranged skirmisher |
| Noble | designate servant companion; Fellowship-driven | Fellowship-scaling builds |
| Sanctioned Psyker | one starting discipline; -20% phenomena chance | Psyker origin; recommended for psyker builds |
| Navigator (conditional) | conditional / semi-secret | Only playable if Cassia is removed from party |

| Arbitrator (DLC) | Vigilant/Castigator/Subductor paths; Familiar bond (Cyber-Mastiff etc.) | Lex Imperialis DLC; unlocks Overseer T2; Solomorne companion uses this origin |

**Familiar mechanic (Arbitrator origin, Lex Imperialis):** Familiar types -- Cyber-Mastiff, Psyber-Raven, Servo-Skull Swarm, Cyber-Eagle. Familiars share initiative with their bonded character but have independent wound pools; they can be downed and recovered between fights.

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

**Commissar -- At All Costs + Overpenetration:** The Commissar ability (shoot a target; if it dies, grant an ally extra turn +2 AP/+3 MP) works with Overpenetration shots that pierce multiple enemies -- if any of the hit enemies die from the penetrating shot, the grant triggers. Enables flexible multi-kill setups, especially useful when combined with Bounty Hunter.
> **Cross-system dependency** -- see `dependencies.md` DEP-012: This interaction is independently documented in items/builds.md Party Synergies.

**Grand Strategist mechanic:** Designate zones on the ground that buff allies in the area, then activate stratagems on those zones for a variety of utility, buff, and offensive effects. One Grand Strategist is strong; two or more trivializes combat through overwhelming action economy -- many fights end on turn 1 even on un-optimized builds. Recommended: field at most one Grand Strategist.
> **Cross-system dependency** -- see `dependencies.md` DEP-010: The overpower arises specifically from pairing GS on both the MC and Cassia; crew/cassia-orsellio.md independently documents the same "field at most one" recommendation.
_source (Commissar/GS): reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Ship Combat

Turn-based tactical fleet combat on a separate map. Fires between ground zones and on certain story beats.

**Weapon modes:** Flak cannon gives an alternate torpedo attack type; fighter craft gives an alternate broadside cannon attack type. Switch modes by clicking the small tab on the weapon slot during combat. Cannot switch modes while a weapon is on cooldown.

**Interceptors** do not suffer the accuracy penalty from Drukhari ships' Shadow Field effect.

**Ship post companion recommendations:**
- **Abelard -- Supreme Commander:** His post upgrade unlocks Swing Run, letting you choose 3 possible ship heading landing spots instead of 1. Best-in-slot for that post.
- **Pasqal -- Master Cannoneer:** His post upgrade allows using the ability during the acceleration phase AND reloads torpedoes. Best-in-slot for that post.

Ship skill level affects how many rounds an Ultimate ability lasts (high skill ~13 rounds vs. low skill ~6; most fights end within 6).

**Custom NPC ship specialists:** Via Janris Danrok you can create fully customizable NPCs dedicated solely to ship battle posts (e.g. a cannoneer built for ship combat only). Limitation: only story companions can unlock a post's upgrade abilities -- custom NPCs cannot. See crew/abelard-werserian.md and crew/pasqal-umberto-i.md for companion post recommendations.
> **Cross-system dependency** -- see `dependencies.md` DEP-008: Abelard (Supreme Commander) and Pasqal (Master Cannoneer) have uniquely impactful post upgrades independently documented in their crew files and here.

**Fleet battles scale sharply in Act 3** and can be non-winnable for unprepared parties. If ground combat difficulty is high, reduce fleet difficulty separately. The extra ship from the Lex Imperialis DLC substantially eases Act 3 fleet fights.
_source (ship combat): reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
_source (fleet Act 3 warning): reddit_sweep r/RogueTraderCRPG 2026-05-27 · capture: manual_paste · confidence: medium · enemy-tier: 2 · puzzle-tier: 0 · category: mainline · spoiler: late-game_

## Companion Quests

Several companions have time-gated personal quest lines. Missing the trigger window permanently locks quest content and companion-specific items. Key windows documented in `nav/architecture.md` companion-quest table and `sections/missables.md`.

Base companions (recruitment chapter):
- Abelard Werserian -- Ch1 (available from start)
- Argenta -- Ch1
- Pasqal -- Ch1 (Rykad Minoris)
- Heinrix -- Ch1 (Hallowed Electrodunamic Cenobium)
- Cassia Orsellio -- Ch1 (Eurac V)
- Yrliet -- Ch2 (Janus, requires Aeldari in Distress trigger)
- Jae -- Ch2
- Marazhai -- Ch3 (requires specific arena dialogue)
- Ulfar -- Ch4

Secret companions (Ch4 end, conviction-gated): Calligos Winterscale / Incendia Bastaal-Chorda / Uralon. `spoiler: story`

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

## Consumables -- Quick reference

See `items/consumables.md` for slot rules, stacking rules, and full consumable roster.

## Armour System

Three tiers: Light, Medium, Heavy. **No stat-based equip requirements** -- armor is talent-gated, not stat-gated.

- **Light / Medium:** No talent required. Medium trades some dodge for more damage reduction.
- **Heavy:** Requires **Heavy Armour Proficiency** talent. Adds unique **Deflection** stat (flat damage reduction per hit). Imposes a **Dodge Penalty** multiplier (typically ×0.5) on the wearer's dodge chance.

**Dodge formula:** `Base dodge = 30 + (Agility − enemy Perception)`. Heavy armour's ×0.5 Dodge Penalty halves the result. Agility is therefore the stat most affected by heavy armour -- high-AGI characters lose more absolute dodge in heavy armour but may still out-dodge low-AGI characters.

**Stat-conditional bonuses** appear on individual pieces (e.g. +3 Deflection if STR > 70, +10% dodge if AGI > 50) -- these are bonuses, not equip gates.

**Power Armour Proficiency** is a separate talent; only 3 base-game suits exist before late Ch4 (~level 45); Patch 1.5 / Lex Imperialis adds 3 more. Generally not worth investing early.

_source: roguetrader.wiki.fextralife.com/Armour · web search 2026-06-27 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Weapon Proficiency

Each weapon family requires a single 1-point Proficiency talent. No multi-step "feat tax" weapon classes. Exception: **Power Armour Proficiency** is effectively a feat tax -- only 3 suits exist in base game, none arrive before late Ch4 / ~level 45. **Heavy bolters do not require Bolt Weapon Proficiency** (Chris Williams, GameFAQs -- patch-current quirk). Xeno weapons require their faction proficiency.
_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
