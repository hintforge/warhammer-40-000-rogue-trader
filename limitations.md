# Warhammer 40,000: Rogue Trader -- Limitations & Blocked Sources

Sources found that look useful but couldn't be fully fetched -- paywalls, Cloudflare, age gates, video-only content, etc. URLs preserved so the player (or a contributor) can open them in a real browser.

> **CANONICAL SOURCE for talent/ability/item/buff text = the GAME FILES, not the wiki.** The install ships `WH40KRT_Data/StreamingAssets/Localization/enGB.json` (~17.8 MB) -- the exact in-game tooltip text, current to the installed patch, including everything wikis lack (companion/DLC talents, Raining Blood, etc.). Two local tools query it:
- [`game_text_lookup.ps1`](game_text_lookup.ps1) -- raw text grep, e.g. `.\game_text_lookup.ps1 "Crimson Tide"`.
- [`talent_catalog.ps1`](talent_catalog.ps1) -- builds `talent_catalog.json` from the game's own blueprint index (`Bundles/cheatdata.json`): the COMPLETE authoritative list of every talent-relevant blueprint (11,594 = 4,712 features + 2,161 abilities + 4,721 buffs) with internal name + GUID + type. Use it to verify the corpus isn't missing a talent (`-Find <regex>`) and to bridge to text (`-Describe <name>`).

Prefer these over Fextralife/Neoseeker scraping: no 404s, no rate limits, no patch lag. Wiki is now the FALLBACK (good for editorial build advice the raw text doesn't give).

**Two layers of authority, and the boundary between them (mapped 2026-06-29):**
1. `cheatdata.json` -- authoritative blueprint INDEX (name+GUID+type). Complete, easy, already wired into `talent_catalog.ps1`. Proves what exists (e.g. confirmed: 8 weapon proficiencies incl. Xenos, NO Las/Solid-Projectile; the 5 Death Cult talent display names Crimson Tide/Dance of Blood/Dance of Thorns/Open the Veins/Wounds Streaming Blood all exist in the installed build, validating the corpus).
2. `enGB.json` -- authoritative TEXT (display names + descriptions), keyed by loc-GUID.
- **The gap:** the blueprint->loc-GUID link (which loc-GUID is a given talent's name/description) lives only in `Bundles/blueprints-pack.bbp`, a BINARY-serialized pack (type/string table + positional records; internal codenames diverge from display names, e.g. `DeathCultAssassin_MarkOfViolence_Talent`). Parsing it offline = a full deserializer for Owlcat's proprietary format -- high effort, high risk of emitting WRONG numbers. The community solves this with a RUNTIME dump (UnityModManager + a dump mod calling the game's own serializer; the `Modding/` toolkit ships in the install). That's the only way to auto-generate fully-paired name->description->numeric tables; deferred as a separate build. Until then: catalog (completeness) + text grep (descriptions, which already contain the numbers) is the working method.

Install root: `E:\SteamLibrary\steamapps\common\Warhammer 40,000 Rogue Trader`. (`save_watcher.ps1` reads the PLAYTHROUGH; these read the STATIC data those GUIDs point at. `blueprint_cache.json` is an earlier partial mine -- Areas/Units GUID->name maps.)

## How to read this file
- Each entry: topic, URL, block type, what was gleaned, best alternative accessed.
- Per-topic files (`puzzles/`, `items/`, `sections/`, etc.) also list their own blocked sources.
- This file is the catch-all for sources that didn't fit a specific topic.

## Block types
- **paywall** -- content gated behind a subscription or article limit
- **cloudflare** -- Cloudflare bot challenge / 403 / 503 from WebFetch
- **video-only** -- YouTube or other video where the answer is shown visually; no readable text equivalent
- **age-gate** -- content blocked behind age verification
- **cookie-wall** -- popup or consent flow that broke the fetch
- **search-snippet-only** -- search engine returned a snippet but the page itself wasn't reachable
- **dead-link** -- URL was in another source but no longer resolves

## Entries

### Steam achievement list -- Stage 0 stub fetch (RESOLVED at P1)
- Source: https://store.steampowered.com/stats/2186680/achievements (NOTE: P1 researcher accessed https://steamcommunity.com/stats/2186680/achievements which is the community stats page, not the store stats page -- this URL succeeded)
- Block type: RESOLVED -- P1 researcher fetched the community stats page successfully
- Resolved: 106 total achievements confirmed; all 101 base-game achievements populated in `achievements.md`; 5 DLC deferred to P3
- Stage 0 estimate of ~105 was close; actual is 106

### TrueAchievements / ExoPhase -- achievement detail (RESOLVED at P1 via community stats page)
- Source: https://www.truesteamachievements.com/game/Warhammer-40000-Rogue-Trader/achievements
- Block type: 403 / rate-limiting during Stage 0
- Resolved: not needed; community stats page provided complete data

### Magic Game World controls page
- Source: (URL not confirmed in P1 research)
- Block type: unreachable during P1 research
- Why: additional controls reference; Fextralife Controls page used as primary source instead
- Gleaned: nothing retrieved

### Overseer archetype -- base game vs. DLC status
- Source: Fextralife archetype page
- Block type: conflicting sources (not a web-block)
- Why: Fextralife describes Overseer as base-game (available to Officer/Operative or psyker-Origin); some community guides describe it as DLC-expanded
- Status: treated as base-present pending P3 clarification
- Deferred to P3 for resolution

### Heavy-weapon proficiency quirk -- "Don't Touch This" achievement
- Source: Steam community discussion threads
- Block type: community dispute (not a web-block)
- Why: achievement text says "Daring+" but community discussion suggests it may fire on Core+ in some patch versions
- Status: flagged for live verification by the player

### Community mechanics reference -- "Things I Wish I Knew" Google doc (partially verified)
- Source: https://docs.google.com/document/d/1fgOtJZBp08VYIzJYL-3ptMwBsz-W7Lr1wcdSzu8VAgU/edit (companion Reddit thread: https://www.reddit.com/r/RogueTraderCRPG/comments/1mjl9pq/)
- Block type: partially verified -- OP explicitly warns "Some of this was changed after recent patches. A lot still applies but origin, pet, and sword of faith changed a lot."
- Author: u/Merlinmast (1000+ hours). Covers psykers, origins, homeworlds, warp travel, basic mechanics, ship combat, bounty hunter, items.
- Status: Claims from the Reddit thread version of this doc were ingested in reddit_sweep 2026-05-27 and cross-checked against Patch 1.5 corpus. The Google doc itself may contain additional claims not in the Reddit thread summary -- treat as supplemental reference, not authoritative source. Verify any claim from the doc against Patch 1.5 before accepting.

### Bladedancer common talent options at Ranks 5, 8, 13 -- RESOLVED 2026-06-29 (doctor, Firecrawl)
- Was: corpus gap -- the "Available Common Talents" pool was undocumented, so screen names had no match in the guide.
- ROOT CAUSE of the confusion: the common-talent pool is THREE pools combined -- **homeworld talents + origin talents + a universal pool** (proficiencies, characteristic training, skill talents, Nimble). The corpus documented only archetype talents, so common-pool names looked unknown. Now documented in full: [`items/talents-homeworld.md`](items/talents-homeworld.md), [`items/talents-origin.md`](items/talents-origin.md), [`items/talents-common.md`](items/talents-common.md).
- Death Cult Assassin talent effects: **NOW FOUND.** The old names (Crimson Tide, Dance of Blood, Dance of Thorns, Open the Veins, Wounds Streaming Blood) were CORRECT all along -- they 404'd only because Fextralife gives companion talents no standalone `/<Talent>` pages; their effects live as rows on the master `/Talents` list. Full effects logged in `crew/kibellah.md` and `items/talents-origin.md`. They are a blood-cult stacking engine (bloodblessed/bloodstained + blood-covered cells).
- Jinx (Voidborn): **NOW FOUND** -- double-edged luck aura (>50% wounds +10% all hit chances in 3 cells incl. enemies; <50% -10%).
- Remaining sub-gap: **Raining Blood** has no effect text on Fextralife (referenced only as a condition). Off-wiki sources describe a melee blood-splash; unconfirmed. Capture in-game tooltip to close.
- Method note for future doctor runs: for Owlcat companion/origin talents that 404 on `/<Talent+Name>`, scrape `https://roguetrader.wiki.fextralife.com/Talents` (the master list) and grep the talent name -- the effect is a row there.

## Always-blocked categories

[Document patterns where no source type can supply the data -- e.g. randomized per-save content, visual-only puzzle layouts without text guides. Add as encountered during research ingestion.]
