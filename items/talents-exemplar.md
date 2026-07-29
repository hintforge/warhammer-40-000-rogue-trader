# Warhammer 40,000: Rogue Trader -- Exemplar (T3) Talent Pool

**status:** research-integrated
**last_reconciled:** 2026-05-27
**research_run:** doctor 2026-05-27

Tier 3 (Exemplar) unlocks at level 36. Exemplar has NO archetype-specific ability trees -- only a shared universal talent pool, plus selectable re-picks from your T1 and T2 trees. There are no archetype-name-locked Exemplar talents.

_source: doctor research 2026-05-27 (Fextralife Exemplar page · Fandom Exemplar page · GameSkinny Jason Rodriguez · Steam Community Exemplar discussions · GameFAQs Advanced Archetypes) · capture: web_fetch · confidence: high · enemy-tier: 0 · puzzle-tier: 0 · category: mainline · spoiler: none_

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
