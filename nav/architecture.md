# Warhammer 40,000: Rogue Trader -- Architecture

**status:** research-integrated
**last_reconciled:** 2026-05-23
**research_run:** P3 cascade 2026-05-23

Cross-zone structural primitives. The persona reads this file for all cross-zone reasoning -- lookahead warnings (Rule 2), backtrack queries (Rule 3), reachability checks (Rule 4), locks-and-keys notifications (Rule 5). Per-zone gate lists live in `nav/<zone>.md` and reference this file's graph by edge ID (deferred to P2). Drift between this file and per-zone files is a bug; run a consistency pass after each ingestion.

## Hintforge manifest

```
corpus-core-version: 5
game-version: "Build 21262645"
game-version-platform: "PC / Steam"
game-version-as-of: 2026-05-22
vector-extensions: puzzles, npcs, endings, paths, crew, factions
```

## Vector extensions

- `puzzles/` -- discrete logic and environmental puzzle files with hint ladders, indexed by `puzzles/index.md`
- `npcs/` -- hostile NPC factions and named bosses, indexed by `npcs/index.md` (renamed from `enemies/` at v5)
- `endings/` -- conviction-path and narrative ending files, indexed by `endings/index.md`
- `paths/` -- branching narrative path files (Dogmatic/Iconoclast/Heretical), indexed by `paths/index.md`
- `crew/` -- named companion entity files, indexed by `crew/index.md` (scaffold; populated via ingestion)
- `factions/` -- faction entity files, indexed by `factions/index.md` (scaffold; populated via ingestion)

## Zone Graph

**Game-type label:** hub-and-spoke-with-dungeons (confirmed -- voidship is persistent hub; galactic chart is inter-system overworld; each system contains 1-6 planets/anomalies opening into landmark dungeon maps; Ch3 Commorragh is a linear funnel exception)
**Localization-mechanism class:** hybrid (star-system map for inter-system + landmark-based for dungeons/surfaces; no continuous open world; node-to-node travel on galactic chart then per-zone load)
**Entry node:** z-prologue-flagship
**Hub nodes:** z-ship-bridge (persistent voidship), z-foot-dock / z-foot-atrium / z-foot-martyr (Footfall)
**Source-language set:** Russian (Owlcat Games developer), English, German, French, Spanish (Spain), Simplified Chinese, Japanese (text+UI in all seven); Turkish added post-launch patch 1.3.2.8; voice acting English only

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Zone list (43 zones, base game)

| Zone-id | Canonical name | Parent hub | Type | Chapter(s) |
|---|---|---|---|---|
| z-prologue-flagship | Void Dragon Flagship (Prologue) | -- | dungeon (one-shot) | Prologue |
| z-ship-bridge | Voidship Bridge | Voidship | voidship | 1-5 |
| z-ship-upper | Voidship Upper Deck (Astropathic Choir, Navigator's Quarters) | Voidship | voidship | 1-5 |
| z-ship-lower | Voidship Lower Deck | Voidship | voidship | 1-5 |
| z-ship-cargo | Voidship Cargo / Reclusiam | Voidship | voidship | 1-5 |
| z-ship-quarters | Lord Captain's Quarters | Voidship | voidship | 1-5 |
| z-rykad-minoris | Rykad Minoris -- Starport / Streets / Command Center | Rykad system | surface | 1 |
| z-electrodyn | Hallowed Electrodunamic Cenobium | Rykad Minoris | dungeon | 1 |
| z-rykadi-philia | Rykadi Philia (prison planetoid) | Rykad system | dungeon | 1 |
| z-eurac-v | Eurac V -- Navis Nobilite Station | Rykad system | dungeon | 1 |
| z-mysterious-ship | Drifting Voidship (Furibundus / Rykad Majoris) | Furibundus | dungeon (optional) | 1-2 |
| z-foot-dock | Footfall -- Void Dock Alpha-Rho | Footfall | hub | 2, 4 |
| z-foot-atrium | Footfall -- Atrium | Footfall | hub | 2, 4 |
| z-foot-liege | Footfall -- Liege's Residence | Footfall | hub | 2, 4 |
| z-foot-shadow | Footfall -- Shadow Quarters | Footfall | hub | Ch2 only |
| z-foot-quarantine | Footfall -- Quarantine Zone & Mutant Lair | Footfall Shadow Quarters | dungeon (optional) | Ch2 only |
| z-foot-martyr | Footfall -- Martyr's Endurance | Footfall | hub | 2, 4 |
| z-janus | Janus colony surface | Telikos Epsilon | surface (colony) | 2, 4 |
| z-janus-temple | Janus -- heretical temple | Janus | dungeon | 2 |
| z-kiava-gamma | Kiava Gamma -- Forge World | Cranach | surface (colony) | 2, 4 |
| z-dargonus | Dargonus -- von Valancius Palace & grounds | Mundus Valancius | surface (colony) | 2, 4 |
| z-foulstone | Foulstone -- colony | Trinnitos | surface (colony) | 2-5 |
| z-vheabos | Vheabos VI -- colony | Mortus Acies | surface (colony) | 2-5 |
| z-uniden-ruins | Unidentified Ruins (dead world) | Latotian's Passage | dungeon (optional, puzzle) | 2+ |
| z-aviorus | Aviorus -- Main Computing Cathedral | Aviorus | dungeon (optional) | 2 |
| z-chartist | Chartist Vessel (boarding hulk) | Atlassian Reach | dungeon (story) | end of Ch2 -> Ch3 |
| z-pit | Commorragh -- The Pit (Corpse Pile) | Commorragh | dungeon | 3 |
| z-chasm | Commorragh -- The Chasm streets | Commorragh | dungeon | 3 |
| z-mangled | Commorragh -- Mangled Sector | Commorragh | dungeon | 3 |
| z-opera | Commorragh -- Anatomical Opera | Commorragh | dungeon | 3 |
| z-arena | Commorragh -- Reaving Tempest Spire (Arena) | Commorragh | dungeon (gated) | 3 |
| z-webway | Commorragh -- Webway Gate / Tower | Commorragh | dungeon (one-way) | 3 |
| z-eufrates | Eufrates II -- Siege | Emperor's Palm | dungeon | 4 |
| z-quetza | Quetza Temer -- Aeldari hunt | Nameless Star | dungeon | 4 |
| z-system-speculo | System Speculo -- Ark Mechanicus Hermetico | Speculo | dungeon (Pasqal quest) | 4 |
| z-vheabos-vi-quest | Vheabos VI -- [zone label under review; Solomorne's actual recruitment trigger is li-footfall-dock-alpha-rho Ch2, not Vheabos VI Ch4 -- see crew/solomorne-anthar.md] | Mortus Acies | companion-quest | 4 |
| z-fenrys | Fenrys Hjolda -- Ulfar quest | various | companion-quest | 4 |
| z-mundus-nullius | Mundus Nullius -- Abandoned Palace | Mundus Nullius | dungeon (optional, trophy) | 4 |
| z-debris-battiada | Debris of Battiada -- ice planet | Debris of Battiada | dungeon | 5 |
| z-cinerus | Cinerus Maleficum -- Necron sites | Cinerus Maleficum | dungeon | 5 |
| z-winterscale | Winterscale's Realm | -- | dungeon | 5 |
| z-unbeholden | Unbeholden Reaches | -- | dungeon | 5 |
| z-epitaph | Epitaph -- Necron Tomb World (final) | Cinerus Maleficum | dungeon (one-way) | 5 |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

### Zone graph edges

| Edge-id | From | To | Type | Direction | Condition | PoNR | Notes |
|---|---|---|---|---|---|---|---|
| E01 | z-prologue-flagship | z-ship-bridge | story-gate | one-way | accept Warrant of Trade | permanent | refusing yields bad ending |
| E02 | z-ship-bridge | koronus-expanse-map | hub-spoke | bidirectional | story chapter >= 1 | -- | central nav hub |
| E03 | koronus-expanse-map | star-system | fast-travel | bidirectional | Navigator's Insight point greens route | -- | green routes recommended to reduce warp events |
| E04 | star-system | planet-surface | hub-spoke | bidirectional | scanned + landing party | -- | per-zone load |
| E05 | z-rykad-minoris | koronus-expanse-map | story-gate | one-way | finish Ch1 main quests | chapter-bound | "Stolen Star" achievement fires |
| E06 | z-foot-dock | z-foot-shadow | story-gate | one-way | complete Reclaim What Was Lost (Kiava Gamma) | missable-trigger (Ch2 only) | by Ch4 removed from fast-travel entirely |
| E07 | z-dargonus | z-pit | story-gate | one-way | Dargonus enthronement cutscene (finish Ch2 main quests) | permanent (Ch2->Ch3) | Footfall partially cordoned; merchants unavailable Ch3; Footfall Shadow Quarters gone Ch4+ |
| E08 | z-chartist | z-pit | story-gate | one-way | board Chartist Vessel | permanent | player enters Pit with no equipment |
| E09 | z-arena | z-webway | story-gate | one-way | win 3rd arena fight | chapter-bound | locks ALL Commorragh side exploration |
| E10 | z-webway | z-janus | story-gate | one-way | escape Commorragh via Webway Gate | permanent | |
| E11 | z-foot-liege | ch4-partial | conditional | one-way | refuse to repent (Heretical Ch4 Liege audience) | point-of-divergence | companion loyalty breaks possible; "half your party" at risk |
| E12 | ch5-systems | ch5-systems | hub-spoke | bidirectional | enter Act 5 | -- | 4 contained systems: Cauldron, Cinerus Maleficum, Winterscale's Realm, Unbeholden Reaches |
| E13 | ch5-systems | earlier-systems | -- | blocked | -- | permanent | "Act 5 is the point of no return act" |
| E14 | z-epitaph | final-boss | story-gate | one-way | scan Epitaph + enter descent | permanent | ending split here |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

### DLC zone graph edges

| Edge-id | From | To | Type | Direction | Condition | PoNR | Notes |
|---|---|---|---|---|---|---|---|
| E-VS-01 | vs-voidship-crypt | vs-bloodspun-temple | story-gate | one-way | complete clue trail 3/3 + defeat Magus (Ch2) | permanent | `spoiler: dlc:Void Shadows` |
| E-VS-02 | z-ship-upper | vs-genestealer-lower | story-gate | one-way | Ch4 gate; Patriarch confrontation | PoNR-VS-01 | `spoiler: dlc:Void Shadows` |
| E-LI-01 | li-mundus-nullius-system | li-heartless-bridge | story-gate | one-way | board the Heartless after void combat | PoNR-LI-01 (frigate fate locked) | `spoiler: dlc:Lex Imperialis` |
| E-LI-02 | li-heartless-engine | z-ship-bridge | story-gate | one-way | Bone Key puzzle solved; exit The Heartless | permanent | `spoiler: dlc:Lex Imperialis` |
| E-LI-03 | li-silbannacos-system | li-palace-of-justice | story-gate | one-way | DLC story progression triggers | PoNR-LI-03 | `spoiler: dlc:Lex Imperialis` |

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

**Fast-travel network:** inter-system warp on galactic chart, gated by Navigator's Insight points that "green" a route (reducing warp-event probability). No ground-side fast-travel inside zones; movement is point-and-click.
_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Companion-quest-gated zones / windows (base game)

| Companion | Quest | Zone | Chapter window |
|---|---|---|---|
| Pasqal | Let the Cycle Be Discontinued | z-system-speculo | Ch4 |
| Ulfar | The Baneful Howl / Fenrys Hjolda | z-fenrys | Ch4 |
| Abelard | Blood Ties (bug-prone pre-patch 1.073) | z-dargonus | Ch4 |
| Argenta | Driven (Repentia split in "Whodunit?" Ch3; resolution Ch4-5) | various | Ch3 trigger |
| Marazhai | Shards of the Tempest / Runaway | Commorragh / Ch5 | Ch5 |
| Yrliet | The Path We Lost / Outcast's Duty | various | Ch4+ |
| Jae | Rat Hunting | z-foot-atrium | Ch4 Footfall return |
| Cassia | The Price of Power | various | late Ch4 / Ch5 |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

## Chapter -- Zone Mapping

| Chapter | In-game title | Approx. levels | Zones | Key notes |
|---|---|---|---|---|
| Prologue | "Conspiracy" | 1-3 | z-prologue-flagship | Tutorial; conviction primer; Chaos Spawn boss; Defective Servitors missable starts |
| Chapter 1 | "Stolen Star" | 1-15 | z-rykad-minoris, z-electrodyn, z-rykadi-philia, z-eurac-v, z-mysterious-ship (optional), z-ship-* | ~15-25 hrs; Cassia recruited at Eurac V; Pasqal on Rykad Minoris; Argenta, Heinrix in Ch1 |
| Chapter 2 | "Trade Empire" | 16-30 | z-foot-*, z-janus, z-janus-temple, z-kiava-gamma, z-dargonus, z-foulstone, z-vheabos, z-uniden-ruins (optional), z-aviorus (optional), z-chartist (Ch2 end) | ~35-50 hrs; most missable content in game; Footfall open; 4 colonies; PoNR at Dargonus enthronement |
| Chapter 3 | "Commorragh Survivors" | 31-36 | z-pit, z-chasm, z-mangled, z-opera, z-arena, z-webway | ~15-25 hrs; linear funnel; equipment stripped at entry; 3rd arena is PoNR for Commorragh side content |
| Chapter 4 | "Expanse Calamity" | 37-42 | z-eufrates, z-quetza, z-system-speculo, z-vheabos-vi-quest, z-fenrys, z-mundus-nullius (optional), z-foot-* (partial), z-dargonus | ~25-40 hrs; companion-quest-dense; secret companions unlock at Ch4 end |
| Chapter 5 | "Grand Finale" | 43-45 | z-debris-battiada, z-cinerus, z-winterscale, z-unbeholden, z-epitaph | ~8-15 hrs; all past PoNR; 4 contained systems; final boss at Epitaph |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

Run-length baseline (Steam community member Morgian, 140-hour Normal first run): Ch1 25h / Ch2 45h / Ch3 20h / Ch4 35h / Ch5 15h.
[Confirmed: community consensus, 5+ sources]

## Optional Content Registry

| Name | Unlock condition | Access window | Parent zone | Rec. chapter | Failure mode |
|---|---|---|---|---|---|
| Dreams and Stories (Footfall hidden caches x4) | Talk to Skatov; explore 4 cache locations | Ch2 only | z-foot-dock/atrium/shadow | Ch2 | missable -- Shadow Quarters closes Ch3+ |
| Where the Shadows Are Deepest of All | Complete Reclaim What Was Lost (Kiava Gamma) first; bug on full-Dogmatic-incognito | Ch2 only | z-foot-shadow / z-foot-quarantine | Ch2 | missable; Shadow Quarters removed from fast-travel Ch4+ |
| Unidentified Ruins double-puzzle | Approach on galactic chart; Lore (Warp) +20 check | Ch2+ (pre-Ch5 PoNR) | z-uniden-ruins (Latotian's Passage) | Ch2 | permanent until Ch5 end |
| Aviorus -- Main Computing Cathedral | Scan Aviorus system | Ch2+ | z-aviorus | Ch2 | accessible until Ch5 PoNR |
| Drifting Voidship (Rykad Majoris / Furibundus) | Scan Furibundus / Rykad Majoris | Ch1-2 | z-mysterious-ship | Ch1 | missable after Chapter 2; unique Drukhari weapon drop |
| Defective Servitors quest | High Factotum's area, Voidship | Ch1 (starts); chain through Ch4 | z-ship-* | Ch1 | missable; required for "How Did It All End?" achievement chain |
| Theodora's data caches (Kiava Gamma cogitator + Dargonus safe) | Kiava Gamma gear room; Dargonus bedroom | Ch2 pre-enthronement | z-kiava-gamma, z-dargonus | Ch2 | missable; required for "How Did It All End?" |
| Bridge cogitator hack (Ch1 end) | Interact with bridge cogitator at Ch1 climax | Ch1 end (one-time) | z-rykad-minoris | Ch1 | missable; required for "How Did It All End?" |
| Mundus Nullius -- Abandoned Palace | Scan Mundus Nullius | Ch4 | z-mundus-nullius | Ch4 | optional; awards trophy |
| Pet the Dog (Glaito) | Voidship; interact with dog | Ch2+ | z-ship-* | any | achievement |
| Well-Deserved Rest (bath with every companion) | Lord Captain's Quarters | Ch3+ | z-ship-quarters | Ch3+ | per-companion missable if companion dies |
| Janus Aeldari in Distress (Yrliet) | Visit Janus gazebo before completing World Shapers | Ch2 | z-janus | Ch2 | missable |
| Chasing the Elusive Contempt | Latotian's Passage | Ch4 | z-uniden-ruins area | Ch4 | optional |

_source: P1 research cascade 2026-05-22 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

### DLC Optional Content Registry -- Void Shadows

| Name | Unlock condition | Access window | Parent zone | Rec. chapter | Failure mode |
|---|---|---|---|---|---|
| VS-OPT-01: Trolley Problem | Visit vs-freight-line with Jinevra in party | Before vs-freight-line closes | vs-freight-line | Ch2-3 | missable if Jinevra not in active party |
| VS-OPT-02: It Itches! | Contract infestation at vs-freight-line; carry to temple | Before temple initiation | vs-freight-line -> vs-bloodspun-temple | Ch2-3 | missable; spoiler: dlc:Void Shadows |
| VS-OPT-03: Ziek's quest | Complete before vs-bloodspun-temple initiation | Before initiation | vs-voidship-shrine, vs-bloodspun-temple | Ch2 | missable on PoNR |
| VS-OPT-04: Clue trail 3/3 | Find all 3 clues before Magus boss | Before Magus defeated | vs-voidship-crypt | Ch2 | missable on boss kill |
| VS-OPT-05: Confessor no-down | Defeat Confessor boss without any companion going down | vs-confessor-chapel access | vs-confessor-chapel | Ch2-3 | requires party prep; "This Is Fine" achievement |
| VS-OPT-06: Mind Your Head crane | Solve crane puzzle | Before vs-freight-line closes | vs-freight-line | Ch2-3 | missable |
| VS-OPT-07: Fool Me Once / This Is My Throne! | Patriarch confrontation choice | Before PoNR-VS-01 | vs-genestealer-lower | Ch4 | choice-exclusive; hidden achievements |

### DLC Optional Content Registry -- Lex Imperialis

| Name | Unlock condition | Access window | Parent zone | Rec. chapter | Failure mode |
|---|---|---|---|---|---|
| LI-OPT-01: Not a Scratch | Complete void combat at Mundus Nullius without hull damage | During li-mundus-nullius void combat | li-mundus-nullius-system | Ch2-3 | missable mid-combat |
| LI-OPT-02: One Step Ahead | Collect all clues before final briefing | Before PoNR-LI-02 | li-thassera-citadel | Ch3 | missable at final briefing trigger |
| LI-OPT-03: Tank / Of Course sequences | RT drives tank; destroy 5 enemies | Tank sequence window | li-leethus-surface | Ch4 | missable at sequence end |
| LI-OPT-04: Thorough Audit | Glaito opens DLC-exclusive chest | Before li-leethus-sand-zone closes | li-leethus-sand-zone | Ch4 | requires Solomorne + Glaito Familiar |
| LI-OPT-05: Rogue Trader One Item | Buy from Tertius Quart | Before li-leethus-surface closes | li-leethus-surface | Ch4 | missable |

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: dlc:Void Shadows, dlc:Lex Imperialis_

## Support Topology

### Save system
Manual save available from menu at any time (EXCEPT during a combat turn -- must wait until end of turn). Autosaves at story checkpoints: zone entry, pre-boss encounters, pre-major-choice dialogue, companion recruitment scenes. Autosave timing is "inconsistent" and not officially documented (Steam 4416425017208915444); **recommended practice: manual save after every warp jump and every zone entry.** No discrete save-station objects anywhere in the base game. Difficulty cannot be changed mid-run if Grim Darkness (ironman) was selected at game start.
_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Autosave checkpoint locations (per-zone, feature-anchored where observable)
Community-derived from walkthrough save-prompts; not officially documented. Best-effort only.
- z-prologue-flagship: pre-Theodora ambush; post-Mort discovery; pre-Kunrad cut
- z-rykad-minoris: Starport landing; pre-Aurora; pre-final boss
- z-eurac-v: dock entry; pre-Felek fight; pre-elevator up
- z-janus: landing pad; pre-Muaran webway dialogue
- z-kiava-gamma: manufactorum entry; pre-Cubis Delphim; pre-Uralon
- z-chasm / z-pit / z-arena: zone entry only; no per-fight autosaves observed (Steam 4416425017208915444)
- z-webway: landing; pre-Tervantias; pre-Yremeryss
- z-eufrates: foothold landing; pre-Doomscream; pre-final boss
- z-epitaph: landing; pre-mirror-self fight; pre-final boss console
- All other zones: source-uncertain on per-feature autosave anchors; zone-entry autosave is the reliable checkpoint.
_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Fast-travel network (exhaustive base-game list)
| Node | Zone-id | Access condition | Chapters |
|---|---|---|---|
| Koronus Expanse Map console | z-ship-bridge | Always-available after Prologue | 1-5 |
| Section-map (voidship internal) | z-ship-bridge <-> z-ship-upper/lower/cargo/quarters | Always-available on voidship | 1-5 |
| Janris Danrok fast-track traders dialogue | z-ship-bridge | After meeting each merchant | 2-5 (Footfall traders cordoned Ch.3) |

> **Cross-system dependency** -- see `dependencies.md` DEP-007: Janris Danrok's voidship vendor dialogue is the sole remaining merchant access during the Ch3 Footfall cordon; also documented in `mechanics.md` Profit Factor section and `items/consumables.md` merchant table.

**No ground-level fast-travel nodes exist anywhere in the base game.** Every ground zone exit requires walking to the shuttle/airlock and selecting "Return to voidship" or following a story-mandated exit. Confirmed exhaustive: P1 and P2 research found no additional nodes. (Steam Community 4416425017208915444; GameFAQs chris-williams Voidship Management; gamerguides.com Koronus Expanse Exploration.)
_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### Hub access
All dungeon-type zones: return to voidship by approaching shuttle/airlock dialogue. Confirmed for all 43 base-game zones. Voidship sub-zones (z-ship-bridge/upper/lower/cargo/quarters) are inter-accessible via section map at all times. One-way zones with no return: E01 z-prologue-flagship->z-ship-bridge, E08 z-chartist->z-pit, E09 z-arena->z-webway, E10 z-webway->z-janus, E14 z-epitaph->final-boss (confirmed complete -- no additional one-way ground-to-ground transitions found by P2).

**Footfall partial cordon:** all six Footfall sub-zones (z-foot-dock, z-foot-atrium, z-foot-liege, z-foot-shadow, z-foot-quarantine, z-foot-martyr) are effectively inaccessible between Dargonus inauguration (Ch.2 end) and Ch.4 inquisitorial martial-law arrival. Conservative reading: treat all as unreachable in Ch.3 (Steam 4038104984934310792 user Morgian).
_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

### DLC zones -- Void Shadows (7 zones, released September 24 2024)

All zones prefixed `vs_`. Accessible from Ch.1 onward (voidship internal DLC arc).
Voidship internal fast-travel nodes added by Patch 1.2 for VS zones.

| Zone-id | Canonical name | Parent hub | Type | Chapter(s) |
|---|---|---|---|---|
| vs-voidship-shrine | Bloodspun Shrine (Voidship Upper Deck) | Voidship | voidship-dlc | 1+ |
| vs-voidship-crypt | Genestealer Crypt (Voidship Lower Deck) | Voidship | voidship-dlc | 1-2 |
| vs-freight-line | Freight Line District | Voidship | voidship-dlc | 1+ |
| vs-bloodspun-temple | Bloodspun Temple (Voidship Underbelly) | Voidship | voidship-dlc | 2+ |
| vs-confessor-chapel | Confessor's Chapel | Voidship | voidship-dlc | 2+ |
| vs-genestealer-lower | Genestealer Patriarch's Lair | Voidship | voidship-dlc (one-way Ch4) | 4 |
| vs-overlook-walkway | Overlook Walkway | Voidship | voidship-dlc (banter only) | 2+ |

### DLC zones -- Lex Imperialis (13 zones, released June 24 2025)

All zones prefixed `li_`. Accessible after triggering DLC at Footfall docking in Ch.1/2.

| Zone-id | Canonical name | Parent hub | Type | Chapter(s) |
|---|---|---|---|---|
| li-footfall-dock-alpha-rho | Footfall Dock Alpha-Rho (DLC access pier) | Footfall | hub-dlc | 2 |
| li-dargonus-arbites-audience | Dargonus -- Arbites Audience Hall | Dargonus | cutscene sub-zone | 2 |
| li-mundus-nullius-system | Mundus Nullius System Map (void combat) | -- | system map | 2-3 |
| li-heartless-bridge | The Heartless (frigate) -- Bridge | Li-mundus-nullius | dungeon | 2-3 |
| li-heartless-engine | The Heartless -- Engine Room | Li-heartless-bridge | dungeon | 2-3 |
| li-lavellas-heart-system | Lavellas Heart System Map | -- | system map | 3 |
| li-thassera-citadel | Thassera -- Royal Citadel | Lavellas Heart | dungeon | 3 |
| li-thassera-square | Thassera -- Central Square | Lavellas Heart | dungeon | 3 |
| li-neos-charoitus-system | Neos Charoitus System Map | -- | system map | 4 |
| li-leethus-surface | Leethus -- Surface Settlement | Neos Charoitus | surface | 4 |
| li-leethus-sand-zone | Leethus -- Sand Wastes | Neos Charoitus | dungeon | 4 |
| li-silbannacos-system | Silbannacos System Map | -- | system map | 5 |
| li-palace-of-justice | Palace of Justice | Silbannacos | dungeon (one-way) | 5 |

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_

## Locks and Keys

P1 cross-zone locks (conviction-path and secret-ending gates):

| Lock location | Lock description | Key required | Key type | Key source zone | Visible before key? | Notes |
|---|---|---|---|---|---|---|
| Footfall Shadow Quarters (E06) | Quarantine gate in z-foot-shadow (SE) | Complete Reclaim What Was Lost (Kiava Gamma) | story-flag | z-kiava-gamma | yes (gate visible from Ch.2) | missable; Shadow Quarters removed Ch.4+ |
| Commorragh 3rd arena side content (E09) | Arena portal progression | Win 3 arena fights without exiting | story-flag | z-arena progression | no (encounter-locked) | locks ALL remaining Ch.3 optional content |
| Ch.4 secret companion: Calligos Winterscale | Conviction branch | Iconoclast conviction path to Ch.4 end | story-flag / conviction | Ch.1-4 conviction choices | no | branch-exclusive |
| Ch.4 secret companion: Incendia Bastaal-Chorda | Conviction branch | Dogmatic conviction path to Ch.4 end | story-flag / conviction | Ch.1-4 conviction choices | no | branch-exclusive |
| Ch.4 secret companion: Uralon | Conviction branch | Heretical path + Prologue blade-fragment + Sameth name reveal at Edge of Daybreak | story-flag / conviction | Ch.1-4 conviction + specific Prologue dialogue | no | branch-exclusive; most requirements |
| Nomos secret ending ("How Did It All End?") | Multi-step chain | Defective Servitors + Kiava Gamma cogitator + Dargonus safe + bridge cogitator hack + Pasqal alive + accept Asclepius/Forgefiend vessel | story-flag | scattered Ch.1-4 | no | multi-stage; easiest route uses Nomos in Forgefiend body vs C'tan |

> **Cross-system dependency** -- see `dependencies.md` SEQ-004: The secret ending chain spans nav locks (this table), puzzle rewards (`puzzles/`), companion survival (Pasqal, `crew/`), and the "How Did It All End?" achievement (`achievements.md`); all 7 steps must be completed across the full run.

P2 per-zone locks (item, ability, puzzle, and story-flag gates within zones):

| Lock location | Lock description | Key required | Key type | Key source zone | Visible before key? | Notes |
|---|---|---|---|---|---|---|
| z-prologue-flagship -- Warrant Chamber gene-lock | Blood-keyed door | Player's blood (forced by Kunrad) | story-flag | z-prologue-flagship | yes | Cannot avoid; demonic implant if Coercion/Psyker option |
| z-rykad-minoris -- Warehouse circuit | Relay-damper-motive force | Puzzle (see corpus puzzles/) | ability (Tech-Use) | in-zone | yes | Skippable but loot-gated |
| z-rykad-minoris -- Upperway orb | Floating sphere energy field | Altar dialogue + correct console order | ability (Logic) | in-zone | yes | Bug: prompts may not appear -- reload |
| z-eurac-v -- Laboratory door | Sealed adamantium door | Main-chamber cogitator: Option A ("Switch to main chamber controls -> Open all doors") | ability (Tech-Use) | z-eurac-v cogitator room | yes | Distinct option from elevator (gamerguides.com) |
| z-eurac-v -- Upper elevator | Inactive lift | Main-chamber cogitator: Option B ("Main elevator controls -> Activate the elevator") | ability (Tech-Use) | z-eurac-v cogitator room | yes | Distinct from door-unlock (use both options) |
| z-eurac-v -- Armoury door | High-Logic locked door | Logic check | ability (Logic) | in-zone | yes | Flamer Digi-Weapon Ring reward |
| z-foot-dock -- SW loot crate | 4-button code (sequence) | Sequence 3-5-4-1 | puzzle | in-zone | yes | Interrogation Goggles + Psyker's Footwear |
| z-foot-atrium -- Upper gate | Cogitator gate | Pasqal-only Tech-Use | ability | in-zone | yes | Unyielding Vanguard Boots chest |
| z-foot-shadow -- Quarantine gate | Extermination Brigade gate (SE) | Story flag: Kiava Gamma main quest complete | story-flag | z-kiava-gamma | yes (visible from Ch.2) | Where the Shadows Are Deepest of All |
| z-foot-shadow -- Sewer access | Locked sewer hatch | EITHER Jae recruitment (Persona Non Grata) OR Denz funeral entry (Underworld/Fidelio) | story-flag | z-foot-atrium / z-foot-liege | yes | Soft-lock: refusing both blocks Rat Hunting permanently |
| z-kiava-gamma -- Theodora data cache | Toxic-gas defenses | Phrase "Litanies of the Motive Force" | story-flag | z-ship-bridge Pasqal cogitator | yes | Required for "How Did It All End?"; "Disable the Gas" only appears if Pasqal cogitator spoken first |
| z-dargonus -- Bedchamber saferoom | Disguised bedroom bookshelf | Book on nightstand interaction (sequence: nightstand -> couch -> Flame of Purity wine + Litanies book + Symphony Pt 2) | ability / puzzle | z-dargonus bedroom | no (hidden) | Required for "How Did It All End?" chain |
| z-aviorus -- Sealed door (Compressor Hall) | No power; main door | Backup-generator puzzle (5 stabilizers, pressure 10) | puzzle / ability | in-zone | yes | Gates Forgefiend boss |
| z-aviorus -- Breakable wall | Entrance corridor wall | Melta Charge | item | external (cargo) | yes | Safe behind; Tech-Use unlock |
| z-pit -- Pillar compartment | Hidden compartment | Awareness check + switch | ability | in-zone | no | Extra gear |
| z-opera -- Mon-Keigh Rubbish box | Gear locked | First arena win + Tervantias dialogue ("require a moment of your precious time") | story-flag | z-opera | yes (visible but inert) | Cannot retrieve gear before these conditions |
| z-opera -- Ulfar's cage | Massive cage | Bone Key | item | z-opera (Tervantias dialogue) | yes | **CRITICAL: missing this in Ch.3 (patch 1.5+) permanently locks out Ulfar** |
| z-webway -- Toxin turrets | Acid-projectile turret network | Lore (Xenos) consoles | ability | in-zone | yes | Bypass significantly cuts difficulty |
| z-webway -- Eklendyl's cage | Hanging cage | Two consoles (top + bottom) | ability | in-zone (Eastern chamber) | yes | Frees Eklendyl |
| z-webway -- Stifler force field | Tervantias's protective field | Destroy (Dogmatic/Heretical/Warp-Votary) | story-flag / ability | in-zone | yes | +10 Veil Degradation to remaining Commorragh fights if destroyed |
| z-webway -- Webway Portal | Final gate | Webway Resonance Device OR Marazhai active companion | item / companion | z-webway eastern locker / z-opera Marazhai recruit | yes | One-way E10 exit |

> **Cross-system dependency** -- see `dependencies.md` SEQ-006: Marazhai (optional recruit via specific 2nd arena dialogue) is an alternative key for this portal exit; missing his recruitment window (before 3rd arena, PON-002) removes this option and leaves only the Webway Resonance Device.
| z-eufrates -- East door | Locked behind cogitator | Cogitator access (route through Prayer Halls) | ability (Tech-Use) | in-zone | yes | Required for east route |
| z-eufrates -- West fire-doors | Fire-hazard rooms | Fire-protection gear (strongly recommended) | gear-recommendation | external | yes | Incongruous Defiler beyond |
| z-quetza -- Demolition archway | Crumbling stone arch | Demolition -60 | ability | external | yes | Cloak of Mercy crate |
| z-epitaph -- Landing crate | Tech-Use locked | Tech-Use -55 | ability | external | yes | Rack and Ruin foehammers + Astral Currents boots |
| z-epitaph -- Inquisitorial barrier | Conviction-gated barrier | Dogmatic/Iconoclast = passage; Heretical = destroy | conviction / story-flag | story | yes | Conviction-gated; blocks opposite path |
| z-epitaph -- Stair turrets (x2) | Necron turrets at stair-bottoms | Demolition barricade + ranged DPS | ability | external | yes | Two separate stair-bottoms |
| z-epitaph -- Obelisk | Inactive Necron obelisk | Lore: Xenos -90 | ability | external | yes | Spawns crate with Singer of Fearsome Sagas + Rallying Boots + Mind Assemble Circlet |
| z-epitaph -- C'tan binding console | Final progression console | Story progression | story-flag | in-zone | yes | One-way E14 -> final boss |
| Three Sorrowful Phalanges system | System locked on galactic chart | 6th Dargonus colony event (any tier-5 project completion) | story-flag | z-dargonus colony tier 5 | no (system invisible until trigger) | Fextralife: explicitly the "6th Dargonus colony event" |

**DLC companion windows:**

| Companion | DLC | Zone | Miss condition |
|---|---|---|---|
| Kibellah | Void Shadows | vs-voidship-shrine | Not missable -- auto-joins at shrine Ch1 |
| Solomorne Anthar | Lex Imperialis | li-footfall-dock-alpha-rho | Permanently missable if Footfall Ch2 meeting ignored; Patch 1.5 allows earlier trigger |

**DLC locks-and-keys (P3):**

| Lock location | Lock description | Key required | Key type | Key source zone | Visible before key? | Notes |
|---|---|---|---|---|---|---|
| vs-voidship-crypt -- Magus final chamber | Locked until clue trail complete | 3/3 clues found | story-flag | vs-voidship-crypt | yes | `spoiler: dlc:Void Shadows` |
| vs-bloodspun-temple -- Initiation chamber | Requires ritual completion | To Become the Flagship's Blood quest flags | story-flag | vs-bloodspun-temple | yes | `spoiler: dlc:Void Shadows` |
| vs-genestealer-lower -- Patriarch access | Ch4 one-way gate | Ch4 story progression | story-flag | E-VS-02 | no | `spoiler: dlc:Void Shadows` |
| li-heartless-engine -- Bone Key puzzle | Locked puzzle chamber | Bone Key item | item | li-heartless-bridge (Captain Sargona drop) | yes | `spoiler: dlc:Lex Imperialis` |
| li-leethus-sand-zone -- Glaito chest | DLC-exclusive locked chest | Glaito Familiar (Solomorne's) | companion/ability | Solomorne recruited + Overseer T2 | no (hidden) | "Thorough Audit" achievement |
| li-palace-of-justice -- Palace approach | One-way story gate | DLC story progression (E-LI-03) | story-flag | li-silbannacos-system | no | PoNR-LI-03 |

**Priority soft-lock callouts (P2 confirmed):**
1. **z-opera Ulfar Bone Key** -- Missing in Ch.3 permanently locks out Ulfar (no later rescue path since patch 1.5).
2. **z-foulstone protection refusal** -- Permanent lock on colony and Dargonus tier-5 chain.
3. **z-foot-shadow sewer locks** -- Refusing both Jae AND Fidelio funeral routes permanently locks Rat Hunting.
4. **z-webway elevator (Yrliet)** -- Owlcat-confirmed bug: Yrliet must be in active party (roguetrader.owlcat.games/news/en/33).
5. **Footfall trader cordon** -- Buy all needed Footfall trader items before Dargonus inauguration.

> **Cross-system dependency** -- see `dependencies.md` SEQ-001: Ulfar is permanently missable (callout #1 above) if the Bone Key is not obtained from Tervantias in z-opera before the 3rd arena fight locks all Commorragh side content (PON-002).
> **Cross-system dependency** -- see `dependencies.md` SEQ-003: Jae's Persona Non Grata errand (callout #3) is one of two sewer-access routes; if BOTH Jae and Fidelio routes are missed, Rat Hunting is permanently inaccessible; see `crew/jae.md`.
> **Cross-system dependency** -- see `dependencies.md` PON-003: The equipment strip at E08 (Chartist -> z-pit) means stimms for the "Fully Prepared" achievement must be pre-stocked in Ch1-2; they cannot be obtained after boarding.

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: progression_
