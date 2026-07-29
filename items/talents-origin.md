# Warhammer 40,000: Rogue Trader -- Origin Talents

**status:** research-integrated
**last_reconciled:** 2026-06-29
**research_run:** doctor 2026-06-29 (Firecrawl)

Each character Origin grants a fixed talent set (plus a Feature and stat/skill profile). These feed the **"Available Common Talents"** level-up screen alongside [homeworld talents](talents-homeworld.md) and the [universal pool](talents-common.md) -- they are NOT archetype talents. If a common-talent name isn't an archetype talent or a homeworld talent, it's an origin talent -- look here.

> **Companion-talent URL gotcha (for maintainers):** Owlcat companion/origin talents that 404 on `https://roguetrader.wiki.fextralife.com/<Talent+Name>` are NOT missing -- their effects live as rows on the master `https://roguetrader.wiki.fextralife.com/Talents` page. Scrape that and grep the name.

_source: doctor research 2026-06-29 (Fextralife Origins page + individual talent pages + master Talents list, via Firecrawl) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

---

## All origins (full list)
Fextralife lists 14 origins. Playable (MC character creation) vs. companion-only (a specific companion's fixed origin) noted.

| Origin | Talents granted | Type |
|---|---|---|
| Astra Militarum Commander | Suppression Fire!, Fix Bayonets!, Trench Warfare, Field of Fire (+ Unflinching Heroism) | Playable |
| Commissar | Motivation, For the Emperor!, Let Them Know Fear!, Summary Execution (Duty and Honour! + Show Them Contempt! removed in 1.5) | Playable |
| Crime Lord | Killing Plan, Escape Plan, Disorienting Plan, Contingency Plan, The Last Plan | Playable (Pandora's origin) |
| Ministorum Priest | Litany of Purification, Tenets of Retribution, Flensing Faith, Litany of Hatred, The Emperor Protects (Shield of Faith removed 1.5) | Playable |
| Navy Officer | Stentorian Voice, Evasive Manoeuvres, Fleet Combat Training, Get Off Me, Get Into Cover! (Do Not Falter!/Scatter/Perfect Timing removed 1.5) | Playable |
| Noble | You. Do Something., You. Protect Me., You. Go on., You. Kill It., You. You Are Next. | Playable |
| Sanctioned Psyker | Psyker Minoris/Majoris/Extremis/Terminus, Still Mind, Sacred Rituals, Enforce Reality, Second Sight, Subtle Manipulation, Inscribed Soul, Blade of Light, Psychic Barrage, Stabilising Factor, Obscured Threat | Playable -> see [`talents-psyker.md`](talents-psyker.md) |
| Arbitrator | 3 sub-paths (Vigilant / Castigator / Subductor) | Playable (Lex Imperialis DLC) -> see [`talents-dlc.md`](talents-dlc.md) |
| Navigator | Eye of Oblivion, Blood Augury, Mind Over Matter, Open to the Warp, Pass Unscathed, Unblinking Stare, Tonicity, Strange Vitality, Perilous Ways, The Course Untravelled, Guide of Souls, Under My Protection, Veil of Protection, Ebb and Flow, Unnatural Allure, Threads and Faults, Mastery of Time, Undam the Sea of Souls, Stable Routes (+ Lidless Stare feature) | Playable (story-gated custom-companion unlock) -> table below |
| Death Cult Assassin | Crimson Tide, Dance of Blood, Dance of Thorns, Open the Veins, Wounds Streaming Blood (+ traits/abilities below) | Companion (Kibellah, Void Shadows DLC) |
| Adepta Sororitas | (no public talent list) | Companion (Argenta) |
| Adeptus Astartes | (no public talent list) | Companion (Ulfar) |
| Asuryani Outcast | (no public talent list) | Companion (Yrliet) |
| Cold Trader | Features: Gunslinger, Never Play Fair, Cold Trader's Acumen | Companion (Jae) |
| Tech-Priest | (no public talent list) | Companion (Pasqal) |

---

## Crime Lord  (Pandora's origin)
**Feature:** Sure-Fire Plan · **Modifiers:** +5 WS, +5 PER; +5 Awareness, +5 Logic

| Talent | Effect |
|---|---|
| Sure-Fire Plan (Feature) | At combat start, gain +(INT bonus) sure-fire plan stacks. Spend 1 stack to strengthen your next action: attack -> +(10 + PER bonus)% damage; move -> +(10 + PER bonus)% dodge & parry until your next turn; non-damaging ability on an enemy -> that enemy takes -(10 + INT bonus)% damage penalty for 1 round. Usable multiple times per turn. |
| Killing Plan | Sure-fire plan's bonus damage +(2x WS bonus)%. Killing an enemy with an attack restores 1 stack. |
| Escape Plan | Sure-fire plan's dodge/parry bonus +(2x AGI bonus)%. Dodging/parrying at least one attack by next round restores 1 stack. |
| Disorienting Plan | An enemy hit by sure-fire plan also takes -(10 + 2x PER bonus)% dodge & parry reduction. |
| Contingency Plan | If you start a turn with 0 stacks, gain +1 stack. |
| The Last Plan | Once per combat, with >=1 stack, you don't die from lethal damage -- instead heal (5 x stacks)% max wounds, lose all stacks, and can't gain more this combat. |

## Astra Militarum Commander
**Feature:** Regimental Tactics (+ Unflinching Heroism)

| Talent | Effect |
|---|---|
| Suppression Fire! | While Regimental Tactics is active, you and allies gain +20% dodge/parry/block reduction and cover penetration vs. enemies already attacked by your allies this combat. |
| Fix Bayonets! | Two-handed las weapons (yours or allies') gain a Bayonet Strike melee attack (1 AP, same damage as the las weapon, doesn't count toward the per-turn attack limit, once per round). |
| Trench Warfare | In partial cover, your las weapon rate of fire +20%; in full cover, +40%. |
| Field of Fire | While under Regimental Tactics, all allies gain +5% rate of fire for every attack they've made since the effect began. |

## Commissar
| Talent | Effect |
|---|---|
| Motivation | +(1 + level/10) MP for you; allies starting their turn within 2 cells also get +(1 + level/10) MP. Once per round, after you attack with a pistol, +(FEL bonus/2) MP. No stack. |
| For the Emperor! | An ally who survives being hit by At All Costs! and then kills an enemy while under it regains 30% of the wounds lost to At All Costs! as temporary wounds. |
| Let Them Know Fear! | While you're adjacent to an enemy, allies gain +(1 + FEL bonus/2) resolve. If no creatures within 2 cells, you gain it instead. |
| Summary Execution | Using At All Costs! while shooting from behind doubles its bonuses. |

## Ministorum Priest
| Talent | Effect |
|---|---|
| Litany of Purification | On War Hymn / Furious Recital, each daemon and xenos within 5 cells takes (5 x zeal stacks) direct damage and +1 perplexed. |
| Tenets of Retribution | +(WP bonus/3) damage and +(WP bonus)% crit damage with bolt weapons; +(WP bonus)% base melta/flamer damage. Doubled vs. daemons/psykers/xenos. |
| Flensing Faith | +(WP bonus)% armour pen with chain/power weapons; crits inflict (WP bonus/2) burning. Doubled vs. daemons/psykers/xenos. |
| Litany of Hatred | On War Hymn / Furious Recital, you and allies within 5 cells deal +(zeal stacks/2) weapon damage for 1 round. Doubled vs. daemons/psykers/xenos. |
| The Emperor Protects | +(WP bonus) max wounds. (Wiki conflict: the prose paragraph instead says "(WP bonus)% chance to ignore any enemy attack" -- effect-box value quoted; verify in-game.) |

## Navy Officer
| Talent | Effect |
|---|---|
| Stentorian Voice | While braced, enemies within 5 cells take -(10 x archetypes chosen) WS and -(10 x archetypes chosen) BS. |
| Evasive Manoeuvres | Allies braced or under your non-attacking abilities gain +(10 + 2x PER bonus)% dodge for 1 round (no stack). You and braced allies don't provoke AoO. |
| Fleet Combat Training | On a crit or successful parry with your primary melee weapon, immediately make the cheapest-AP attack with your secondary weapon vs. the same enemy. |
| Get Off Me | While braced, use Get off me! once per round; your melee targets must pass an AGI test at -10 or fall prone. |
| Get Into Cover! | Allies under Brace for Impact! gain an extra turn (0 AP, 3 MP) and +20% cover efficiency for 1 round; that turn allows only movement abilities, heroic acts, or desperate measures. |

## Noble
_Built around a "servant" companion mechanic (You. Serve Me.)._

| Talent | Effect |
|---|---|
| You. Do Something. | Using an ability on your servant gives them +1 AP next turn (no self-stack). |
| You. Protect Me. | If you and your servant are adjacent at the start of your turn, both gain temporary wounds = the higher of servant's TGH bonus or your FEL bonus. |
| You. Go on. | Your servant gains +2 MP every turn. |
| You. Kill It. | If your servant kills the target you damaged last turn, you gain +1 AP next turn. |
| You. You Are Next. | If the servant is under 30% max wounds, you may use You. Serve Me. again to designate a new servant (can't reuse a prior servant this combat). |

## Navigator
**Feature:** Lidless Stare (the Warp-eye signature ability) · **Modifiers:** +5 PER, +5 WP; +5 Lore (Warp), +5 Awareness · A story-gated origin available only to a custom companion (not the Rogue Trader). Staff-scaling Warp powers. Its active powers (Lidless Stare, Glimpse of Fate, etc.) are abilities, not talents -- see `abilities.md`.

| Talent | Effect |
|---|---|
| Eye of Oblivion | Every enemy in your line of sight has dodge and hit chance reduced by -(PER bonus). |
| Blood Augury | Enemies you damage take +(5 + PER bonus)% additional warp damage; stacks per hit. |
| Mind Over Matter | Make all resistance tests with Willpower if higher than the base stat; if WP > TGH, your wounds are calculated from WP. |
| Open to the Warp | Enemies hit by your abilities take a stacking -10 to their next resistance test vs. your powers (lost after that test). |
| Pass Unscathed | If your Perception is higher than your Agility, dodge is calculated from Perception. |
| Unblinking Stare | Until end of combat, enemies you damage take +(PER bonus) extra damage from attacks of opportunity and can't dodge them. |
| Tonicity | Navigator powers deal +1 damage per 5 bonus characteristic of your equipped staff (castigating/infusing/devastating count as characteristics). |
| Strange Vitality (Navigator) | Heal (WP bonus) wounds at the start of every turn, +1 per Navigator talent taken; healing +1 per creature killed between your turns. |
| Perilous Ways | Enemies you move with abilities take (1 + WP bonus/2) damage at the end of movement, +1 per cell moved. |
| The Course Untravelled | Using a Navigator power not yet used this combat grants +2 PER until end of combat. |
| Guide of Souls | Start all turns (incl. extra) with +3 MP; first ally you target with a single-target ability gets the same next turn. |
| Under My Protection | Allies you target gain +5 to resistance tests vs. warp effects until end of combat; stacks per ability applied. |
| Veil of Protection | Allies you target gain +10% armour, reduced by current veil degradation (min +0%), increased by your staff's infusing. |
| Ebb and Flow | Every even turn: +1 AP. Every odd turn: +20 PER. |
| Unnatural Allure | +5 FEL, plus +1 FEL per Navigator talent and/or power taken. |
| Threads and Faults | When an enemy fails a resistance test vs. your power, attacks on them gain +(20 + 2x PER bonus)% crit chance; stacks, reset by a crit. |
| Mastery of Time | When an ally gains an extra turn, +5 WP until end of combat (up to 5x). |
| Undam the Sea of Souls | Enemies under any Navigator power have armour reduced by -(5 + WP bonus), increased by your staff's devastating (no stack). |
| Stable Routes | Each Navigator ability use reduces veil degradation by -1. |

---

## Death Cult Assassin  (Kibellah -- companion, Void Shadows DLC)

> spoiler: dlc:Void Shadows

A **blood-cult stacking engine**: piles `bloodblessed`/`bloodstained` stacks on enemies and rewards fighting on blood-covered cells. The old P1 names were correct -- they only 404'd because companion talents have no standalone Fextralife pages. Companion build context in [`../crew/kibellah.md`](../crew/kibellah.md).

| Talent (trait) | Effect |
|---|---|
| Crimson Tide | A bloodblessed/bloodstained creature gains +1 stack whenever Raining Blood is re-inflicted on it OR a turn starts on a blood-covered cell. |
| Dance of Blood | Kibellah's allies deal +(2 + AGI bonus)% damage to enemies when both the ally and the target stand on blood-covered cells. |
| Dance of Thorns | Each time Kibellah parries or dodges, all bloodstained enemies gain +1 stack. |
| Open the Veins | A bloodblessed/bloodstained creature gains +1 stack whenever bleed, burning, or toxin is inflicted on it. |
| Wounds Streaming Blood | A bloodblessed/bloodstained creature gains +1 stack whenever it takes damage from bleed/burning/toxin. |
| Raining Blood | Her next melee attack makes the target explode in a burst of blood, covering the floor and enemies behind it; affected enemies take additional damage. (Also has a throwable "blood phial.") Blood-covered cells are what the other Death Cult talents key off. (Game-file confirmed via `../game_text_lookup.ps1`.) |
| Fortune (trait) | Reroll any failed attack/dodge/parry/characteristic/skill test at 20% (capped at the roll's base chance); enemy dodge/parry vs. her has 20% to fail after success. |
| In Death's Footsteps (a.k.a. In Footsteps of Death) | When an ally kills an enemy, +2 MP on her next turn. |
| Blade in His Hand (trait) | Sword attacks deal +(AGI bonus)% damage, doubled with a two-handed sword. |

Her Bladedancer abilities (Bladedance, Death From Above, Captive Audience, Death Waltz) are detailed in [`../crew/kibellah.md`](../crew/kibellah.md) and the Bladedancer section of [`talents-dlc.md`](talents-dlc.md).
