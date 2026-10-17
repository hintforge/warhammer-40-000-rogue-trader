# Build planner: load your own save

`build_planner.html` opens on one player's example party. To see your own Rogue Trader save in it, run these two commands from the guide's top folder (Python 3, nothing to install):

```
python extract_tools/save_import.py
python extract_tools/build_artifact.py
```

Then open `artifacts/build_planner.html` again.

- `save_import.py` reads your newest save and only reads it; it never writes to the save folder. It looks in `%USERPROFILE%\AppData\LocalLow\Owlcat Games\Warhammer 40000 Rogue Trader\Saved Games`. `--list` shows your saves; `--save <name>` picks one.
- It imports what the save states exactly (level, archetype, homeworld, origin, chosen talents, number of characteristic advances). It does not import characteristic totals, because the save does not store them.
- `build_artifact.py` joins `build_planner.template.html`, `data/talents.json` and your `data/save_state.json` into the page. Your save stays on your machine; do not commit `save_state.json` or the rebuilt page if you fork this guide.
- After a game patch adds talents, set `HF_RT_CHEATDATA` to the `Bundles/cheatdata.json` file in your game install and run `save_import.py` once to refresh the name list.
