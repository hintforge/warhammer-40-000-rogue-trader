# Localization toolkit -- Warhammer 40,000: Rogue Trader

**status:** research-integrated
**last_reconciled:** 2026-05-23
**research_run:** P3 cascade 2026-05-23

The persona reads this file when `CHECKPOINT.md`'s `player_position.confidence < high`. It tells the persona how to ask the player where they are, and how to map their answer to a `current_zone` in `architecture.md`.

For `hybrid` localization-mechanism games: the star-system map handles inter-system orientation (use map prompts); landmark-based navigation handles dungeon and planet-surface zones (use landmark prompts). The localization mechanism class for this game is **hybrid** (confirmed P1+P2).

**Special note -- Quetza Temer (z-quetza):** This forest zone is procedurally variable -- the route on one playthrough is different from the next (Fextralife Ch.4). Directional guides from other playthroughs will not match. Use feature-anchored prompts only for this zone; never give directional instructions.

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Landmark -> zone resolution

Per-zone distinctive landmarks. When the player describes their surroundings, match against this table to resolve `current_zone`.

| Landmark / feature | Resolves to zone-id | Notes |
|---|---|---|
| Trophy room (servitor combat); Wall of fire (Theodora apparition); Bridge fork (south-walkway vs cross-bridge); Warrant Chamber gene-lock; Captain's safe | z-prologue-flagship | Tutorial voidship; one-shot |
| Koronus Expanse Map console; Captain's chair; Vigdis station (foot of stairs); Janris desk; north exit to Voidship Shrine | z-ship-bridge | Persistent voidship hub; inter-system FT here |
| FURIA plate altar; Confessor Adalbert; Astropathic Choir; Navis Sanctum (Cassia); Janris's office | z-ship-upper | Upper deck; same ship |
| Valve puzzle row (5 valves); Macro-Cannon Chamber (Pink Horror encounter) | z-ship-lower | Lower deck; same ship |
| Cargo hold containers; Heartless docking port (Ch.4) | z-ship-cargo | Cargo deck; same ship |
| Lord Captain's bed (dream trigger); defunct captain's safe; trophy display | z-ship-quarters | Lord Captain's quarters; same ship |
| Starport landing pad; Warehouse circuit room; Upperway orb sphere; Star Thoroughfare; Governor's bunker | z-rykad-minoris | Ch.1 surface |
| Monastery gate; reactor antechamber; reactor core; Pasqal recruitment spot | z-electrodyn | Ch.1 Adeptus Mechanicus dungeon |
| Landing pad with Pilot Raquel; Barracks with traps; Pit entrance with Casteglia | z-rykadi-philia | Ch.1 prison planetoid |
| Dock entry corpses; bookshelf [Athletics] staircase block; library / Navigator Flesh Sample hallway; main-chamber cogitator; flask laboratory; upper-chamber (Cassia) | z-eurac-v | Ch.1 Navis station |
| System-map dialogue encounter; no walkable map | z-mysterious-ship | Text-encounter only; Ch.1-2 |
| Bloodstained Amelia ambush; SW four-button crate (3-5-4-1); Opticon-22 south; east Atrium gate | z-foot-dock | Footfall entry dock |
| Hieronymus mutant-refugee event spot SW; Daggen Fidelio bait; Ryzza bar back room; Pasqal upper cogitator; chapel of Saint Drusus | z-foot-atrium | Footfall central hub |
| Vladaym audience hall; Octaviana rumor desk; Ryzza side-room | z-foot-liege | Footfall Liege's Palace |
| Sun-symbol floor pattern; Extermination Brigade quarantine gate SE; Anver thug west alley; tunnel under bridge cache | z-foot-shadow | Footfall Shadow Quarters |
| Cult cells; infected workshops; boss chamber | z-foot-quarantine | Footfall Quarantine Zone (post-Kiava Gamma access) |
| Bar; Vladaym + Ryzza eavesdrop alcove (Ch.4 only) | z-foot-martyr | Footfall Martyr's Endurance bar |
| Vyatt's Estate ceremony arena; ravine with fallen-tree fork; trap bridge to Aeldari ruins; webway gateway (Muaran's site) | z-janus | Janus colony surface |
| Webway portal emergence spot; flying ferry shuttle pad; Old Man witness | z-janus-temple | Brief vignette; Ch.4 start only; no exploration |
| Manufactorum entry corridor; corrupted-servitor west room; toxic-gas data cache room; circular bridge platform; Forgefiend chamber | z-kiava-gamma | Kiava Gamma forge world |
| Shuttle pad with nobles; Throne Room (Clementia & Achilleas); Lord Captain's bedchamber saferoom; Gardens; Drukhari assault perimeter | z-dargonus | Dargonus palace colony |
| Monastery gate; cloister; Order of the Hammer chapel | z-foulstone | Foulstone colony |
| Senior Jailer landing area; Pit central; NE chest alcove with Scorpion Sting | z-vheabos | Vheabos VI colony |
| Stash of Children of Asuryan; charred ruins; wrecked voidship scan nodes | z-uniden-ruins | Cinerus cluster exploration nodes |
| Sliding-door corridor; turret puzzle hallway; backup-generator with 5 stabilizers; Compressor Hall cogitator; Forgefiend sealed chamber | z-aviorus | Aviorus drifting voidship; optional Ch.2+ |
| Boarding ramp; nervous officer dialogue; Marazhai trap reveal | z-chartist | Chartist Vessel; Ch.2->Ch.3 commit point |
| Gladiator platform; gladiators' pile; Malice's room (central); Awareness pillar | z-pit | Commorragh Pit; no gear on arrival |
| Crossroads (Yrliet rescue); Mangled Sector lift SE; Pit south; Opera NE; Arena portal NW | z-chasm | Commorragh Streets; hub zone |
| Ugly Beggar position; Abelard's platform (Athletics jump); Cthonos arena (Athletics gate) | z-mangled | Commorragh Mangled Sector |
| Wrack at entrance; Tervantias workshop; Marazhai upper ledge; psyker cages; Ulfar's cage; Mon-Keigh Rubbish box | z-opera | Commorragh Anatomical Opera |
| Khymerae starting platform; Sergeant Vigastes ramp; Marazhai/Keykeross final platform | z-arena | Commorragh Arena |
| Landing platform with Marazhai/Yrliet offers; toxin-turret Lore Xenos consoles; two large vats + Regicide board; Eklendyl hanging cage; central stair-extend console; Tervantias stifler force field; NE Awareness chest; Yremeryss boss platform; Webway Portal | z-webway | Spire of the Reaving Tempest; Ch.3 end |
| Foothold landing; locked east door cogitator; west fire-doors; Incongruous Defiler chamber; Doomscream fork | z-eufrates | Eufrates II forge-world battlefield; Ch.4 |
| Forest Settlement / Speaks-With-Gods ritual stone; wrecked tanks midpoint; Winterscale's hunting camp; Aeldari butchery pile; demolition archway spot | z-quetza | Quetza Temer forest; procedurally variable layout |
| Energy Beam puzzle floor; Xeno Altar; second box puzzle | z-system-speculo | System Speculo xeno temple |
| Senior Jailer landing; SW hidden bag; east Tech-Use crate; NW corner Solomorne | z-vheabos-vi-quest | Vheabos VI penal revisit; Solomorne quest |
| Stolen-shuttle wreck; Imperial trading-vessel hulk; sentry circle (book event); ghostwolf battle ground; Ulfar's saga ring | z-fenrys | Fenrys Hjolda ice world; Ulfar quest |
| Sargona fleet position; Heartless boarding airlock | z-mundus-nullius | Mundus Nullius; Heartless Void |
| Ice-world signal source; main cogitator; minefield-codes terminal | z-debris-battiada | Battiada ice world; Ch.5 start |
| Mysterious Object scan spot; plasma-drive boarding airlock; reactor area; Stash of Children of Asuryan | z-cinerus | Cinerus Maleficum cluster |
| Nameless Star bunker; Oasis V valve puzzle; Langrenn's Belt sub-nodes | z-winterscale | Winterscale's Realm cluster |
| Drukhari hideout planet; Runaway-quest known ladder bug | z-unbeholden | Unbeholden Reaches cluster |
| Landing platform with Heavy Destroyer; Elegy of Sorrow encounter; Taniaka acolyte; Lore Xenos obelisk; memory cores; mirror-selves arena; C'tan binding console | z-epitaph | Epitaph final dungeon |
| Altar with pressure plates; Kibellah standing by an idol; ritual circle with candles | vs-voidship-shrine | VS DLC; voidship underbelly; Kibellah auto-joins here |
| Genestealer egg clusters; cogitator clue stations (x3); sealed Magus chamber | vs-voidship-crypt | VS DLC; Magus boss behind 3/3 clues |
| Freight cars; trolley track junction; crane controls; It Itches! symptom trigger area | vs-freight-line | VS DLC; Jinevra trolley puzzle |
| Blood-red stone nave; initiation ritual dais; cult banners | vs-bloodspun-temple | VS DLC; PoNR for Ziek quest |
| Chapel pews; Confessor robes; confession booth puzzle | vs-confessor-chapel | VS DLC; Confessor boss; "This Is Fine" |
| Patriarch cocoon chamber; brood-brothers ring; one-way grate descent | vs-genestealer-lower | VS DLC; Ch4 one-way; PoNR-VS-01 |
| Open walkway with crew banter; no combat area | vs-overlook-walkway | VS DLC; banter-only zone |
| Arbites sigil dock; uniformed Solomorne figure; Imperial law-enforcement signage | li-footfall-dock-alpha-rho | LI DLC; Footfall Ch2 meet-Solomorne zone |
| Ornate audience hall; Clementia in formal dress; Arbites flanking | li-dargonus-arbites-audience | LI DLC; cutscene sub-zone only |
| System-level void map; Heartless frigate marker; boarding trajectory line | li-mundus-nullius-system | LI DLC system map |
| Frigate bridge with Captain Sargona; sealed bulkheads; override console | li-heartless-bridge | LI DLC; Captain Sargona boss; Bone Key dropped |
| Engine room; large pipes; Bone Key slot puzzle | li-heartless-engine | LI DLC; one-way exit to z-ship-bridge |
| Royal Citadel throne room; briefing table with map; spire view | li-thassera-citadel | LI DLC; One Step Ahead puzzle; PoNR-LI-02 |
| Market square; disguised NPCs; Thrill of the Game impostor hunt | li-thassera-square | LI DLC; 5-impostor puzzle |
| Sand-baked settlement; Tertius Quart's inventory stall; tank garage | li-leethus-surface | LI DLC; tank sequence; Rogue Trader One Item |
| Open desert; sand creatures; Glaito-locked chest (ornate) | li-leethus-sand-zone | LI DLC; Thorough Audit achievement |
| Palace of Justice exterior; grand courtroom; defendant dock | li-palace-of-justice | LI DLC; one-way; PoNR-LI-03 |
| System-level star map; Lavellas Heart label | li-lavellas-heart-system | LI DLC system map |
| System-level star map; Neos Charoitus label | li-neos-charoitus-system | LI DLC system map |
| System-level star map; Silbannacos label | li-silbannacos-system | LI DLC system map |

_source: P3 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Ask-the-player prompts (ground zones / dungeons)

When `confidence < high` and the player asks a nav-class question in a dungeon or surface zone:

1. "What's the last big environmental feature you remember? (e.g., a wall of fire, a sealed door with a cogitator, a fallen tree, a hanging cage, a generator room)"
2. "Was there a named character standing nearby? (Vigdis, Janris, Tervantias, the Old Man at the webway emergence, Senior Jailer, Magos Mahla, etc.)"
3. "What does the section-map overlay show as the current zone label? (e.g., 'Streets of the Chasm', 'Forests of Janus', 'Foothold', 'Spire of the Reaving Tempest')"
4. "What was the last loot container you opened, and what did it contain? (Items map cleanly to zones via the corpus loot index.)"
5. "What was the last skill check you saw? Lore (Xenos)? Tech-Use? Demolition? Athletics? Coercion? (The check distribution is zone-characteristic.)"

Match the player's response against the landmark table above to resolve `current_zone`. If multiple zones could match, ask one disambiguating follow-up -- don't guess.

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

## Map-element prompts (hybrid -- star-system map)

For zones at the inter-system level (player is navigating the Koronus Expanse):

1. "What does your star-system map show as the highlighted destination -- a planet, a station, a debris field, or a 'Mysterious Object'?"
2. "Are you currently on the Koronus Expanse Map, a system map (one level down), or aboard the voidship? (Three distinct UIs.)"
3. "What route color leads to your next jump -- yellow (safe), red (deadly), orange (dangerous) -- and does Cassia or Heinrix's Navigator's Insight pool show enough to shorten it?"

_source: P2 research cascade 2026-05-23 · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_
