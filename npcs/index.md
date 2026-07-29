# NPCs -- Index

**status:** research-integrated
**last_reconciled:** 2026-05-23
**research_run:** P3 cascade 2026-05-23

> v5 migration note (2026-05-23): renamed from `enemies/index.md` as part of corpus-core-version 4->5. `entity-status: hostile` added to all source lines. Per-entity aggregation files (`npcs/<entity-id>.md`) are created at ingestion time when claims carry `entity: <name>` overlay.

**Current enemy tier: 0 -- no enemy reveals preemptively.** The persona does NOT surface enemy data (weaknesses, locations, boss existence) unless the player asks post-encounter. This index is available for post-encounter help on request.

**Confirmed faction count:** 12+ factions; 30+ distinct unit types in base game.

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression · entity-status: hostile_

## Faction Taxonomy
<!-- Role split (zipper 2026-05-23): this table owns the combat-indexed view -- representative units, chapters active, resistances/weaknesses. Narrative/political/conviction context per faction lives in `factions/<entity>.md`. Cross-ref: `factions/index.md`. -->

| Faction | Representative units | Chapters present | Resistances / weaknesses | Notes |
|---|---|---|---|---|
| Chaos Cultists (Cult of the Final Dawn) | Underhive Rabble, Cultist Leader, Heretek Initiate, Kunrad Voigtvir | 1-5 | Low armor; weak to flame/holy; some Warp resistance | Primary early-game enemy |
| Chaos Space Marines / Word Bearers | Word Bearer Aspiring Champion, Chaos Marauder, Possessed Marine | 2-5 | High armor + deflection; weak to melta/plasma/power weapons | Armored; don't waste las |
| Daemons -- Tzeentch | Herald of Tzeentch (Upperway sewer boss), Pink Horror, Brimstone Horror, Screamer | 2, ruins | Teleport; weak to Dogmatic/holy gear | Herald triggers "Cleaning Out the Tzeentch" achievement |
| Daemons -- Slaanesh | Daemonette | 1, 3 | High agility; charm | Prologue scripted trigger |
| Daemons -- Khorne | Bloodletter, Chaos Spawn (Prologue boss) | Prologue, various | High melee output; weak to ranged AoE | Chaos Spawn is Prologue boss |
| Daemons -- Nurgle | Plaguebearer-type | various | Toxin resist; weak to fire/sacred | Adaptive Antidote useful |
| Drukhari | Kabalite Warrior, Wych, Sybarite, Mandrake, Brutal Sslyth, Khymera | 3, various | High dodge; low TGH; weak to AoE/suppression | "Those Who Are About to Die" achievement: let Khymerae kill all gladiators Ch3 |
| Aeldari Asuryani | Aeldari Ranger, Dire Avenger, Guardian, Farseer | 4 (Quetza Temer) | High BS+dodge; vulnerable to overwhelming fire | Yrliet's Lore (Xenos -65) check can resolve some encounters peacefully |
| Necrons | Necron Warrior, Blighted Immortal, Blighted Deathmark, Canoptek Scarab Swarm, Lokhust Heavy Destroyer, Cryptogeometric Sentinel, Elegy of Sorrow | 5 | Reanimation Protocol (auto-revive once per battle); Living Metal (Destroyers ignore ~95% damage unless flanked); Scarabs heal allies | Main Ch5 enemy; flanking required for Destroyers |
| Pirates / Renegade Humans | Voidsman Pirate, Renegade Cutthroat, Pirate Boarder | 1-3 | Low armor; standard | Weakest faction |
| Tyranid Genestealers | Genestealer, Hybrid Acolyte, Purestrain | various | Very high melee; weak to flame/AoE | Main Void Shadows DLC enemy in base-game cameos |
| Beasts of Janus / Dargonus | Wild megafauna | 2, 4 | Low armor; bleed vulnerability | Environmental/optional encounters |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 1 · puzzle-tier: 0 · category: mainline · spoiler: progression · entity-status: hostile_

## Named Bosses (existence: progression; tactics: post-encounter on request)

| Boss | Chapter | Zone | Existence spoiler | Notes |
|---|---|---|---|---|
| Chaos Spawn | Prologue | z-prologue-flagship | none (tutorial boss; public marketing) | "Don't Touch This" achievement on Daring+ (Ch1 end) |
| Aurora | 1 | z-rykad-minoris | progression | Final Dawn leader; Heinrix required for full dialogue |
| Herald of Tzeentch | 2 | Footfall Upperway sewers | progression | "Cleaning Out the Tzeentch" achievement |
| Defiler | 4 | z-eufrates | late-game | "Preserve the Architecture" achievement: kill without destroying 4 plasma batteries |
| Magus | 4 | various | late-game | "Malum Se Ipsum Devorat": force him to kill himself with his own attack |
| Calligos Winterscale | 4 (optional) | z-quetza | late-game | Saving him is harder than fighting; fight "harder than final boss" per Gamer Guides |
| C'tan Shard | 5 | z-epitaph | late-game | Three-stage final boss; see `sections/missables.md` for Nomos secret-ending prerequisite |

Boss tactics are served post-encounter on request only (enemy tier 0 = "Boss existence hidden" per `warning_tiers.md`).

## Difficulty Scaling

I-VII enemy tier range for difficulty scaling (exact per-zone values deferred to P2/live observation).

## DLC Enemies (P3 confirmed)

**Void Shadows -- Genestealer Cult:**
- Genestealer Initiate, Hybrid Acolyte, Brood Brother (cannon fodder); mid-tier melee
- Cult Magus: psyker-type boss (vs-voidship-crypt Ch2); minion-summoner; vulnerable to Warp-disruption
- Patriarch: Ch4 boss (vs-genestealer-lower); dialogue resolution available (Fool Me Once achievement)
- Vizier: tactical support unit; disrupts RT party targeting

Weakness profile: Genestealers generally weak to flame/AoE; Acolytes have mid-level armor.

**Lex Imperialis -- Arbites and opposition:**
- Arbites Enforcer: armored; shock-maul suppression
- Captain Sargona: li-heartless-bridge boss; "I'm the Captain Here!" achievement
- Sand Boss (li-leethus-sand-zone): unnamed; environmental fight; Glaito chest locked until after this fight

## Sources

- Fextralife enemy/bestiary pages: https://roguetrader.wiki.fextralife.com/
- GameFAQs/Chris Williams walkthrough: https://gamefaqs.gamespot.com/ps5/369358-warhammer-40000-rogue-trader/faqs/82192/
- Gamer Guides: https://www.gamerguides.com/warhammer-40k-rogue-trader/guide/walkthrough/
