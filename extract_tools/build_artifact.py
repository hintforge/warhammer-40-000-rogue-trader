#!/usr/bin/env python3
"""Assemble artifacts/build_planner.html from the template + its data islands.

  python extract_tools/build_artifact.py

Injects two islands into build_planner.template.html:
  #hf-data  <- artifacts/data/talents.json     (the talent corpus merge)
  #hf-save  <- artifacts/data/save_state.json  (the imported live save, optional)

Refresh everything after playing:

  python extract_tools/build_planner_data.py   # re-merge corpus + wiki talents
  python extract_tools/save_import.py          # re-read the newest save
  python extract_tools/build_artifact.py       # rebuild the planner

The planner opens on the imported save by default. Edits a player makes in the
page live in that browser's localStorage and are NOT clobbered by a later
import -- pressing "Load from save" is what re-applies it.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ART = ROOT / "artifacts"
DATA = ART / "data"

tpl_path = ART / "build_planner.template.html"
out_path = ART / "build_planner.html"

tpl = tpl_path.read_text(encoding="utf-8")

talents = (DATA / "talents.json")
if not talents.exists():
    sys.exit("Missing %s -- run build_planner_data.py first." % talents)
talents_raw = talents.read_text(encoding="utf-8")

save_path = DATA / "save_state.json"
save_raw = save_path.read_text(encoding="utf-8") if save_path.exists() else "null"

for name, raw in (("talents.json", talents_raw), ("save_state.json", save_raw)):
    # A closing script tag inside an island would end the <script> element early.
    if "</script" in raw.lower():
        sys.exit("%s contains a closing script tag; refusing to inject." % name)

html = tpl.replace("__HF_DATA__", talents_raw).replace("__HF_SAVE__", save_raw)
for token in ("__HF_DATA__", "__HF_SAVE__"):
    if token in html:
        sys.exit("Placeholder %s was not substituted." % token)

out_path.write_text(html, encoding="utf-8")

t = json.loads(talents_raw)
msg = "built %s  (%d KB, %d talents" % (out_path.name, len(html) // 1024, t["counts"]["total"])
if save_raw != "null":
    s = json.loads(save_raw)
    picks = sum(len(v) for c in s["characters"] for v in c["picks"].values())
    miss = sum(len(c["unmatched"]) for c in s["characters"])
    msg += ", save '%s' with %d characters, %d matched picks, %d unmatched" % (
        s.get("save_name"), len(s["characters"]), picks, miss)
else:
    msg += ", no save state embedded"
print(msg + ")")
