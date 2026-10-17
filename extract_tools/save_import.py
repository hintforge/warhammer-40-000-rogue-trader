#!/usr/bin/env python3
"""Import the live Rogue Trader save state into the build planner.

Reads the newest (or a named) .zks save, resolves its blueprint GUIDs against
the game's own blueprint index, and writes artifacts/data/save_state.json.
The planner embeds that file and uses it as the default build.

READ-ONLY with respect to the save directory. Nothing is ever written there.

  python extract_tools/save_import.py                 # newest save
  python extract_tools/save_import.py --save Quick_2  # a named save
  python extract_tools/save_import.py --list          # list saves, import nothing

WHAT THIS DOES NOT IMPORT, AND WHY
----------------------------------
Characteristic TOTALS are deliberately not imported. A save serialises every
characteristic as `m_BaseValue: 30` -- the universal starting base, identical
for all nine stats. A character's real values are recomputed at load time from
homeworld/origin/gear/buff modifiers that are not stored as numbers here.
Reading those 30s as "the character's stats" is the documented failure that
produced a wrong in-game recommendation once already (see guide_issues.md,
save-read data-semantics entry). So this importer takes only what the save
states exactly: the COUNT of characteristic advances actually chosen, which is
precisely what the planner models. The homeworld modifier is carried through as
a labelled reference line, not folded into a total.
"""
import argparse
import difflib
import json
import os
import pathlib
import re
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "artifacts" / "data"
SAVE_DIR = pathlib.Path(
    os.path.expandvars(r"%USERPROFILE%\AppData\LocalLow\Owlcat Games"
                       r"\Warhammer 40000 Rogue Trader\Saved Games"))
# Optional: the game's own blueprint index (Bundles/cheatdata.json in the install
# folder). Set HF_RT_CHEATDATA to its path to refresh the name cache after a game
# patch. Unset, the importer uses the shipped extract_tools/blueprint_names.json.
CHEATDATA = pathlib.Path(os.environ["HF_RT_CHEATDATA"]) if os.environ.get("HF_RT_CHEATDATA") else None
NAME_CACHE = ROOT / "extract_tools" / "blueprint_names.json"

# Owlcat's internal career-path names -> the archetype names players see.
# The six base Tier 2 paths map by elimination against the corpus list, and the
# mapping is corroborated by known companions (Kibellah = Reaper = Bladedancer,
# Argenta = Soldier, Cassia = Leader, Abelard = Fighter).
CAREER = {
    "FighterCareerPath":    ("Warrior", 1),
    "SoldierCareerPath":    ("Soldier", 1),
    "AdeptCareerPath":      ("Operative", 1),
    "LeaderCareerPath":     ("Officer", 1),
    "ReaperCareerPath":     ("Bladedancer", 1),
    "AssassinCareerPath":   ("Assassin", 2),
    "Vanguard_CareerPath":  ("Vanguard", 2),
    "Hunter_CareerPath":    ("Bounty Hunter", 2),
    "TacticianCareerPath":  ("Master Tactician", 2),
    "StrategistCareerPath": ("Grand Strategist", 2),
    "VeteranCareerPath":    ("Arch-Militant", 2),
    "Executioner_CareerPath": ("Executioner", 2),
    "Master_CareerPath":    ("Overseer", 2),
    "Master_CareerPath_Solomorne_Unique": ("Overseer", 2),
    "AscensionCareerPath":  ("Exemplar", 3),
}
SKIP_PATHS = {"StarshipCareerPath", "AscensionCareerPath_Fake",
              "CareerPathTest", "CareerPathTest2"}

ORIGIN_OVERRIDE = {"Criminal": "Crime Lord"}

# Homeworld characteristic modifiers, from corpus mechanics.md (Homeworlds).
# Carried as a labelled reference only -- never summed into an imported total.
HOMEWORLD_MOD = {
    "Death World":   "+5 STR/AGI/TGH, -5 FEL/INT",
    "Forge World":   "+5 INT/TGH, -5 FEL",
    "Fortress World": "+5 PER/WP, -5 FEL",
    "Hive World":    "+5 FEL/AGI, -5 WP",
    "Imperial World": "no modifiers (+10 to one chosen characteristic)",
    "Voidborn":      "+5 WP/INT, -5 STR",
}

STAT_FROM_ADVANCE = {
    "weaponskill": "Weapon Skill", "ballisticskill": "Ballistic Skill",
    "strength": "Strength", "toughness": "Toughness", "agility": "Agility",
    "intelligence": "Intelligence", "perception": "Perception",
    "willpower": "Willpower", "fellowship": "Fellowship",
}

CAREER_PREFIXES = ("Adept", "Fighter", "Soldier", "Leader", "Reaper", "Assassin",
                   "Vanguard", "Hunter", "Tactician", "Strategist", "Veteran",
                   "Executioner", "Master", "Ascension", "Chargen",
                   # origin / discipline prefixes carry talents too
                   "UnsanctionedPsyker", "SanctionedPsyker", "Psyker", "Navigator",
                   "Telepathy", "Biomancy", "Pyromancy", "Sanctic", "Divination",
                   "Criminal", "Commissar", "MinistorumPriest", "NavyOfficer",
                   "Noble", "AstraMilitarum", "AdeptaSororitas", "Arbitrator")


def words(name):
    """Turn a blueprint name into spaced words: DeathWorld_Homeworld -> Death World Homeworld."""
    s = name.replace("_", " ")
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", s)
    s = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def load_blueprint_names():
    """GUID -> blueprint name. Prefers the game's own index; caches a slim copy."""
    if CHEATDATA is not None and CHEATDATA.exists():
        entries = json.load(open(CHEATDATA, encoding="utf-8-sig"))["Entries"]
        keep = ("BlueprintFeature", "BlueprintCareerPath", "BlueprintOriginPath",
                "BlueprintAttributeAdvancement", "BlueprintSkillAdvancement",
                "BlueprintSelection", "BlueprintFeatureSelection", "BlueprintAbility",
                "BlueprintUnit", "BlueprintStatAdvancement", "BlueprintCareerPathRank")
        out = {}
        for e in entries:
            t = e["TypeFullName"].split(",")[0].split(".")[-1]
            if t in keep:
                out[e["Guid"]] = e["Name"]
        NAME_CACHE.write_text(json.dumps(out), encoding="utf-8")
        return out, "cheatdata.json (game blueprint index)"
    if NAME_CACHE.exists():
        return json.loads(NAME_CACHE.read_text(encoding="utf-8")), "cached blueprint_names.json"
    cat = json.load(open(ROOT / "talent_catalog.json", encoding="utf-8"))
    return {e["Guid"]: e["Name"] for e in cat}, "talent_catalog.json (partial)"


def load_talent_names():
    p = OUT / "talents.json"
    if not p.exists():
        return {}
    data = json.load(open(p, encoding="utf-8"))
    return {norm(t["name"]): t["name"] for t in data["talents"]}


def strip_affixes(bp):
    """Reduce a blueprint name to its bare talent name.

    The career token can sit at either end -- `Adept_InstantExpose_Talent` but
    also `Contempt_Fighter_Talent` -- so it is stripped wherever it appears,
    not just as a prefix.
    """
    s = bp
    for _ in range(4):
        before = s
        # suffix may or may not be underscore-separated: `..._Feature`, `EbbAndFlowFeature`
        s = re.sub(r"_?(Talent|Feature|Ability|Advancement|Selection)\d*$", "", s)
        for tok in CAREER_PREFIXES:
            s = re.sub(r"^" + tok + r"_?", "", s)
            s = re.sub(r"_" + tok + r"(?=_|$)", "", s)
        s = re.sub(r"_?NoKEE$", "", s)
        if s == before:
            break
    return s


def match_talent(bp, talent_names):
    """Blueprint name -> corpus talent display name, or (None, reason).

    Returns (name, how). Exact normalised match first; then a tight fuzzy pass,
    because Owlcat ships typos in blueprint names ("LastingImperssion" for
    Lasting Impression). The cutoff is deliberately high and the match method is
    recorded, so a fuzzy hit is auditable rather than silent. Never invents a
    name that is not already in the talent set.
    """
    cand = strip_affixes(bp)
    for probe in (cand, words(cand)):
        hit = talent_names.get(norm(probe))
        if hit:
            return hit, "exact"
    key = norm(cand)
    if len(key) >= 8:
        near = difflib.get_close_matches(key, list(talent_names.keys()), n=1, cutoff=0.88)
        if near:
            return talent_names[near[0]], "fuzzy"
    return None, None


def canon_homeworld(bp):
    """Normalise a homeworld blueprint to the corpus's spelling.

    Blueprint spellings vary (`VoidBornHomeworld`, `ImperialWorldMilitary`),
    so match against the corpus list rather than echoing the raw words.
    """
    n = norm(bp).replace("homeworld", "")
    for known in HOMEWORLD_MOD:
        if norm(known) in n or n.startswith(norm(known)):
            return known
    if "voidborn" in n or "voidborn" in n:
        return "Voidborn"
    if not n or "unknown" in n:
        return None
    return words(re.sub(r"Homeworld", "", bp)) or None


def get_part(container, frag):
    for c in container:
        if frag in (c.get("$type") or ""):
            return c
    return None


def display_name(custom, blueprint):
    if custom:
        return custom
    b = re.sub(r"Companion.*$", "", blueprint or "")
    b = re.sub(r"^(StartGame_Pregen_|NewCompanion_Pregen_)", "", b)
    return words(b) or (blueprint or "Unknown")


def import_save(path, names, talent_names):
    z = zipfile.ZipFile(path)
    header = json.loads(z.read("header.json").decode("utf-8-sig"))
    party = json.loads(z.read("party.json").decode("utf-8-sig"))

    chars = []
    for ent in party.get("m_EntityData", []):
        if not isinstance(ent, dict) or "Parts" not in ent:
            continue
        container = ent["Parts"].get("Container") or []
        prog = get_part(container, "PartUnitProgression")
        if not prog:
            continue
        paths = {names.get(s.get("Path"), "?") for s in prog.get("m_Selections", [])}
        if paths & SKIP_PATHS and not (paths - SKIP_PATHS - {"ChargenPath_ForPregens",
                                                            "NewCompanion_ChargenPath_ForPregens"}):
            continue  # the starship, not a character

        desc = get_part(container, "PartUnitDescription") or {}
        blueprint = names.get(ent.get("OriginalBlueprint")) or ent.get("OriginalBlueprint")
        is_mc = get_part(container, "UnitPartMainCharacter") is not None
        level = prog.get("CharacterLevel")

        arch = {1: None, 2: None, 3: None}
        for p in paths:
            if p in CAREER:
                nm, tier = CAREER[p]
                arch[tier] = nm

        homeworld = origin = None
        picks = {"1": [], "2": [], "3": []}
        picks_by_level = {}
        advances = {}
        skills = []
        unmatched = []
        fuzzy = []        # near-matches, recorded so they stay auditable
        unresolved_by_level = {}  # real picks with no known display name
        background = []   # Darkest Hour / Moment of Triumph -- narrative chargen picks
        innate = []       # Imperial World's "+10 to one chosen characteristic"

        for s in prog.get("m_Selections", []):
            bp = names.get(s.get("Feature"))
            if not bp:
                unmatched.append({"guid": s.get("Feature"), "reason": "guid not in blueprint index"})
                continue
            lvl = s.get("Level") or 0

            if "Homeworld" in bp:
                homeworld = canon_homeworld(bp)
                continue
            if "_Occupation" in bp or bp in ("UnsanctionedPsyker", "SanctionedPsyker"):
                raw = re.sub(r"_?Occupation.*$", "", bp)
                origin = ORIGIN_OVERRIDE.get(raw, words(raw))
                continue
            if re.search(r"(DarkestHour|MomentOfTriumph)", bp):
                background.append(words(strip_affixes(bp)))
                continue
            if "_Innate_" in bp:
                # Imperial World grants +10 to one chosen characteristic; this
                # blueprint records WHICH one. Recorded, never summed.
                innate.append(words(bp.split("_Innate_")[-1]))
                continue
            if "AttributeAdvancement" in bp:
                key = norm(bp).replace("chargen", "").replace("attributeadvancement", "")
                stat = STAT_FROM_ADVANCE.get(key)
                if stat:
                    bucket = "chargen" if lvl == 0 else ("1" if lvl <= 15 else ("2" if lvl <= 35 else "3"))
                    advances.setdefault(stat, {"chargen": 0, "1": 0, "2": 0, "3": 0})
                    advances[stat][bucket] += 1
                else:
                    unmatched.append({"blueprint": bp, "reason": "unrecognised attribute advance"})
                continue
            if "SkillsAdvancement" in bp or "SkillAdvancement" in bp:
                skills.append({"skill": words(re.sub(r"Skills?Advancement$", "", bp)), "level": lvl})
                continue
            if re.search(r"_Level\d+_Feature$", bp):
                continue  # archetype rank marker, not a chosen talent

            tier = "1" if lvl <= 15 else ("2" if lvl <= 35 else "3")
            hit, how = match_talent(bp, talent_names)
            if hit:
                if hit not in picks[tier]:
                    picks[tier].append(hit)
                    picks_by_level.setdefault(str(lvl), []).append(hit)
                if how == "fuzzy":
                    fuzzy.append({"blueprint": bp, "matched": hit})
            else:
                label = words(strip_affixes(bp)) or bp
                unmatched.append({"blueprint": bp, "level": lvl,
                                  "readable": label,
                                  "reason": "no corpus talent of this name"})
                # UNRESOLVED is not REMOVED: the pick is real and belongs on the
                # ladder at its rank, flagged, rather than silently dropped.
                unresolved_by_level.setdefault(str(lvl), []).append(
                    {"label": label, "blueprint": bp})

        chars.append({
            "key": norm(display_name(desc.get("CustomName"), blueprint)),
            "name": display_name(desc.get("CustomName"), blueprint),
            "blueprint": blueprint,
            "is_main_character": is_mc,
            "level": level,
            "experience": prog.get("Experience"),
            "homeworld": homeworld,
            "origin": origin,
            "archetype_t1": arch[1],
            "archetype_t2": arch[2],
            "archetype_t3": arch[3],
            "picks": picks,
            "picks_by_level": picks_by_level,
            "unresolved_by_level": unresolved_by_level,
            "characteristic_advances": advances,
            "skill_advances": skills,
            "fuzzy_matches": fuzzy,
            "background": background,
            "innate_characteristic": innate,
            "unmatched": unmatched,
        })

    chars.sort(key=lambda c: (not c["is_main_character"], c["name"]))
    return {
        "source_file": pathlib.Path(path).name,
        "save_name": header.get("Name"),
        "player_character": header.get("PlayerCharacterName"),
        "saved_at": header.get("GameSaveTimeText") or header.get("SystemSaveTime"),
        "imported_at": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M"),
        "characteristics_note": (
            "Characteristic TOTALS are not imported. The save stores every "
            "characteristic as base 30 for every character; real values are "
            "recomputed at load from homeworld, origin, gear and buff modifiers "
            "that are not stored as numbers. Only the advances actually chosen "
            "are imported -- each is +5 per the corpus (items/upgrades.md)."),
        "homeworld_modifiers": HOMEWORLD_MOD,
        "characters": chars,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", help="save file name or stem (default: newest)")
    ap.add_argument("--list", action="store_true", help="list saves and exit")
    args = ap.parse_args()

    saves = sorted(SAVE_DIR.glob("*.zks"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not saves:
        raise SystemExit("No .zks saves found in " + str(SAVE_DIR))
    if args.list:
        for s in saves:
            print("%-62s %s" % (s.name, __import__("datetime").datetime.fromtimestamp(
                s.stat().st_mtime).strftime("%Y-%m-%d %H:%M")))
        return

    target = saves[0]
    if args.save:
        want = norm(args.save)
        hit = [s for s in saves if norm(s.stem) == want or want in norm(s.stem)]
        if not hit:
            raise SystemExit("No save matching " + args.save)
        target = hit[0]

    names, provenance = load_blueprint_names()
    talent_names = load_talent_names()
    state = import_save(target, names, talent_names)
    state["blueprint_source"] = provenance

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "save_state.json").write_text(
        json.dumps(state, indent=1, ensure_ascii=False), encoding="utf-8")

    print("imported:", state["source_file"], "->", state["save_name"])
    print("blueprint names from:", provenance)
    for c in state["characters"]:
        picks = sum(len(v) for v in c["picks"].values())
        print("  %-16s lvl %-3s %-12s %-16s picks=%-3d unmatched=%d" % (
            c["name"], c["level"], c["archetype_t1"] or "-",
            (c["homeworld"] or "-") + "/" + (c["origin"] or "-"), picks, len(c["unmatched"])))


if __name__ == "__main__":
    main()
