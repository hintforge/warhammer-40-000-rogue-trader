# Warhammer 40,000: Rogue Trader -- Exemplar (T3) Talent Pool

**status:** research-integrated
**last_reconciled:** 2026-05-27
**research_run:** doctor 2026-05-27

Tier 3 (Exemplar) unlocks at level 36. Exemplar has NO archetype-specific ability trees -- only a shared universal talent pool, plus selectable re-picks from your T1 and T2 trees. There are no archetype-name-locked Exemplar talents.

_source: doctor research 2026-05-27 (Fextralife Exemplar page · Fandom Exemplar page · GameSkinny Jason Rodriguez · Steam Community Exemplar discussions · GameFAQs Advanced Archetypes) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

_source (rows marked "New, unassessed"): Fextralife wiki talents table, manually clipped 2026-09-16 · capture: manual-clipping · confidence: medium · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_ -- these rows were added on 2026-09-16 and are NOT covered by the research run named above. Rows tagged _(number unconfirmed)_ reproduce a source value the wiki left blank; confirm in game.

**Version notes:** Steel Shell pre-1.1.28 bugged (only doubled armour-source deflection); now correctly doubles all deflection from armour. Perfection Under Fire +10 persistence bug fixed. Psychic Awakening for companions: wiki says companions cannot select it; some Steam reports claim Pasqal can in specific patches -- current behaviour in Build 21262645 is companions cannot.

---

## Universal Exemplar Talent Pool

| Talent | Effect | Build-defining? | Notes |
|---|---|---|---|
| Eager for Battle | First turn of combat, +2 AP | Yes | Universal must-pick |
| Critical Velocity | Crit chance + crit damage = 7% of your dodge | Yes | High AGI builds only |
| Peak Condition | +STR = 20% of max wounds | Yes | Heavy melee (Ulfar, Abelard, melee builds) |
| Perfection Under Fire | +5 to all characteristics; doubled at <25% wounds | Yes | Universal |
| Tough as Steel | +12 wounds +10x(TGH bonus%) | Yes | Tank staple |
| Flesh Wounds | Regen 10% max per round; 20% if below 20% | Yes | Sustain builds |
| Cataclysm | +3% damage per new enemy damaged this combat | Yes (AoE) | Snowball |
| Steel Shell | Deflection from armour doubled | Yes (heavy) | Pre-1.1.28 bugged; now fixed |
| Unbreakable Will | Resistance check bonus = deflection | Yes (tank) | |
| Masterful Display | Single shots hitting non-main targets -- +5 BS end of combat | Yes (snipers) | Yrliet-style sniper |
| Shot Through | Bonus overpenetration based on BS bonus; overpenetration ignores dodge | Yes (Argenta) | Burst-fire builds |
| Deadeye Shots | Deadeye Shots +(2x PER bonus)% damage; abilities like Claim the Bounty gain Deadeye Shot benefits | Yes (BH) | |
| Firebrand | Extra turn -- target +4 MP (if MP given) or +1 AP (if AP given) | Yes (Officer) | |
| Unflinching | After ally takes extra turn provided by you, +7% armour/dodge and +3 MP end of combat (no stack) | Yes (Officer) | |
| Extermination | All damage +3% until end of combat per new enemy damaged | Yes | Stack with Cataclysm |
| Cumulative Mastery | Damage +1 per attack made this combat (not DoT) | Yes | |
| Bringer of Light | Allies within 2 cells +(2x FEL bonus)% damage and -(2x TGH bonus)% incoming (no stack across chars) | Yes (support) | Aura talent |
| Inevitable | Enemies with 0 deflection or 0% armour vs. you -- +10% damage; +20% if both | Yes | Armour-strip synergy |
| Push Through | Push -- +4 MP after attack; collision damage +(STR bonus x10)% | Yes (push) | |
| Through Discipline | Enemy fails WP test -- suffers (3+WP bonus) direct damage; doubled on success | Yes (WP) | |
| Surge of Momentum | When attacked, gain Momentum = attacker's difficulty tier | Yes | |
| Know It All | Bonus to all characteristics by scaling % (min 5%) | Yes | Generalist |
| Hammer of the Emperor | Press the Advantage and Sanctic damage scaling | Yes (Sanctic) | |
| Shield of the Emperor | +2-4 deflection via WP scaling | Yes (Sanctic) | |
| Psychic Awakening | Become unsanctioned psyker, +1 Psy Rating, choose discipline (MC only; companions cannot) | Yes | Universal psyker dip -- see `dependencies.md` DEP-011 for VD/phenomena implications |
| Masterful Precision | Crit chance +2% per 5% gap between your armour pen and target's armour | Yes (high AP) | |
| Attention! | After an ally takes an extra turn provided 1 by the character, the ally gains +7% armour, +7% dodge, and +3 movement points until the end of combat. Does not stack. | Unrated | New, unassessed |
| Breaking Point | Heavy weapons deal +2 damage and ignore 2 deflection. | Unrated | New, unassessed |
| Combat Meditation | The character gains +15 Willpower as long as they have no ranged weapons equipped (staves do not count as ranged weapons). | Unrated | New, unassessed |
| Contagion | Whenever you apply blinded, slowed, fatigued, perplexed, or disturbed effects, one random enemy within 5 cells of the target also gains that effect for 1 round. The same happens if you inflict stunned or prone, but the random target makes a resistance test to avoid the effect. | Unrated | New, unassessed |
| Crushing Assault | The character's first melee attack each round deals an additional +2 damage for every cell between the character's current position and the spot where they started their turn. The distance is measured in a direct line, ignoring all terrain, with every second diagonal cell counting as two. | Unrated | New, unassessed |
| Deadly Aim | If the character's dodge reduction is higher than the enemy's dodge, the character's damage against that enemy is increased by +1% for every 5% difference between the character's dodge reduction and the enemy's dodge. | Unrated | New, unassessed |
| Deathdealer | Every round, after the character kills the first enemy, the character immediately makes an additional single attack against the closest enemy they can target with the same weapon if possible. This attack deals 30% base damage with a +10% bonus for every difficulty tier of the first killed enemy, i.e. if the enemy was of difficulty tier 1, this attack deals 40% damage in total. | Unrated | New, unassessed |
| Degraded Defence | Whenever the character deals damage to an enemy, that enemy suffers +1 stack of the degraded defence effect for every 6 damage that the character has dealt. Whenever an ally attacks that enemy, they deal additional damage equal to the number of degraded defence stacks. | Unrated | New, unassessed |
| Destroyer | Every character's melee attack reduces the target's armour by -% until the end of combat. This reduction is applied before damage is calculated. Stacks. _(number unconfirmed)_ | Unrated | New, unassessed |
| Disastrous Collision | When targets pushed by the character collide with enemies or cover, both the target and the object they collide with suffer an additional +(2 x character's STR bonus) damage. | Unrated | New, unassessed |
| Eager Subordinates | When allies take actions on extra turns given by the character, they deal +15% more damage. | Unrated | New, unassessed |
| Flagbearer | Allies within 2 cells around the character deal +(3 + character's FEL bonus)% more damage and suffer -(3 + character's TGH bonus)% less damage. If multiple characters have this talent, the effect does not stack. | Unrated | New, unassessed |
| Full Attention | Targets that consider the character a priority target deal -40% less damage to the character's allies. | Unrated | New, unassessed |
| Grievous Wounds | Enemies that have 0 deflection or 0% armour against the character's attacks suffer +10% additional damage from the character. If an enemy has both 0 deflection and 0% armour, those damage bonuses stack. | Unrated | New, unassessed |
| Lethal Threat | Enemies hit by the character with a melee attack must pass a Willpower resistance test or make the character their priority target until the start of the character's next turn. | Unrated | New, unassessed |
| Malign Influence | Whenever an enemy fails a Willpower resistance test against the character, they suffer (2 x character's WP bonus) direct damage. On success the damage is doubled. | Unrated | New, unassessed |
| Martyrdom | Whenever the character is attacked by an enemy, they gain momentum equal to the difficulty tier of the attacking creature. | Unrated | New, unassessed |
| Out of My Way | Whenever the character pushes an enemy, the character gains +4 MP Those MP are added after the attack and allow the character to continue movement. Damage dealt by collisions from pushes is increased by +%. _(number unconfirmed)_ | Unrated | New, unassessed |
| Pinpoint Accuracy | The character ignores (BS bonus / 2) of the enemy's deflection (rounded down). | Unrated | New, unassessed |
| Puncture | If the character's armour penetration is higher than the enemy's armour, the character's critical hit chance against that enemy is increased by +2% for every 5% difference between the character's armour penetration and the enemy's armour. | Unrated | New, unassessed |
| Relentless | Whenever the character is healed, they regain +(5 x character's TGH bonus)% more wounds. | Unrated | New, unassessed |
| Revenge | Whenever the character loses wounds, their next melee attack gains +1 damage for every 2 wounds the character has lost. Stacks. | Unrated | New, unassessed |
| Tipping Point | The character's dodge reduction and armour penetration are increased by +10% of their critical hit chance. | Unrated | New, unassessed |
| Tricky Defence | As long as the character wears light armour, their dodge is increased by half of the armour bonus of that armour. | Unrated | New, unassessed |
| Unstoppable | The character becomes immune to all effects that reduce their MP. They gain +(TGH bonus / 2) MP. | Unrated | New, unassessed |
| Vital Points | Whenever the character scores a critical hit, thtey have a chance to increase their critical damage bonus by half. That chance is equal to (character's critical chance - 50)% (minumum of 0%). | Unrated | New, unassessed |

_Note: the wiki-clipped "Psychic Awakening (Biomancy/Divination/Pyromancy/Sanctic Powers/Telepathy)" entries were skipped as duplicates of the existing **Psychic Awakening** row above, which already covers "choose discipline" generically._

---

## Path-Specific Exemplar Picks (community-converged synergy picks)

No Exemplar talents are archetype-locked; the following are the community-converged picks for each T1->T2 path that make best use of those path's mechanics.

| Path | Top Exemplar Picks |
|---|---|
| Warrior->Assassin | Critical Velocity, Eager for Battle, Perfection Under Fire, Push Through |
| Warrior->Arch-Militant | Peak Condition, Steel Shell, Inevitable, Masterful Precision |
| Warrior->Vanguard | Tough as Steel, Steel Shell, Unbreakable Will, Bringer of Light, Flesh Wounds |
| Warrior->Executioner (VS DLC) | Cumulative Mastery, Cataclysm, Extermination, Peak Condition, Psychic Awakening |
| Officer->Master Tactician | Firebrand, Unflinching, Bringer of Light, Perfection Under Fire |
| Officer->Grand Strategist | Firebrand, Unflinching, Through Discipline |
| Officer->Vanguard | Tough as Steel, Steel Shell, Unbreakable Will |
| Officer->Overseer (LI DLC) | Firebrand, Unflinching, Bringer of Light |
| Soldier->Bounty Hunter | Deadeye Shots, Shot Through, Eager for Battle |
| Soldier->Arch-Militant | Peak Condition, Cataclysm, Extermination, Inevitable, Push Through |
| Soldier->Master Tactician | Cumulative Mastery, Firebrand, Inspired Drive (re-pick) |
| Operative->Assassin | Eager for Battle, Critical Velocity, Masterful Display, Knife in the Dark |
| Operative->Bounty Hunter | Deadeye Shots, Shot Through, Masterful Precision |
| Operative->Grand Strategist | Through Discipline, Pinpoint Strikes (re-pick) |
| Operative->Executioner (VS DLC) | Cataclysm, Extermination, Cumulative Mastery, Psychic Awakening |
| Operative->Overseer (LI DLC) | Through Discipline, Surge of Momentum, Firebrand |
| Bladedancer->Assassin (VS DLC) | Critical Velocity, Eager for Battle, Perfection Under Fire, Peak Condition |
| Bladedancer->Master Tactician (VS DLC) | Cumulative Mastery, Bringer of Light, Firebrand |
| Bladedancer->Arch-Militant (VS DLC) | Peak Condition, Critical Velocity, Inevitable |
| Bladedancer->Executioner (VS DLC) | Cataclysm, Extermination, Cumulative Mastery, Peak Condition, Flesh Wounds |
