"""Self-test for save_import.py on a synthetic save (no real save needed).

Run from the guide's top folder: python extract_tools/test_save_import.py
"""
import json
import pathlib
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import save_import  # noqa: E402


def unit(entity_id, uid, name, main=False):
    container = [
        {"$type": "Kingmaker.UnitLogic.Progression.PartUnitProgression, Code",
         "CharacterLevel": 5, "Experience": 1000, "m_Selections": []},
        {"$type": "Kingmaker.UnitLogic.Parts.PartUnitDescription, Code", "CustomName": name},
    ]
    if main:
        container.append({"$type": "Kingmaker.UnitLogic.Parts.UnitPartMainCharacter, Code"})
    ent = {"$id": entity_id, "$type": "Kingmaker.EntitySystem.Entities.UnitEntity, Code",
           "OriginalBlueprint": "bp-" + entity_id, "Parts": {"Container": container}}
    if uid is not None:
        ent["UniqueId"] = uid
    return ent


def write_save(folder, entities):
    path = pathlib.Path(folder) / "Synthetic.zks"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("header.json", json.dumps({"Name": "Synthetic", "PlayerCharacterName": "Alex"}))
        z.writestr("party.json", json.dumps({"m_EntityData": entities}))
    return path


class CharacterKeys(unittest.TestCase):
    def import_units(self, entities):
        with tempfile.TemporaryDirectory() as d:
            return save_import.import_save(write_save(d, entities), {}, {})["characters"]

    def test_two_characters_with_the_same_name_get_different_keys(self):
        chars = self.import_units([
            unit("2", "11111111111111111111111111111111", "Alex", main=True),
            unit("7", "22222222222222222222222222222222", "Alex"),
        ])
        self.assertEqual([c["name"] for c in chars], ["Alex", "Alex"])
        self.assertEqual(sorted(c["key"] for c in chars),
                         ["11111111111111111111111111111111", "22222222222222222222222222222222"])

    def test_non_latin_names_get_distinct_nonempty_keys(self):
        chars = self.import_units([
            unit("2", "aaaa1111", "Алекс", main=True),
            unit("7", "bbbb2222", "亚历克斯"),
        ])
        keys = [c["key"] for c in chars]
        self.assertEqual(len(set(keys)), 2)
        self.assertTrue(all(keys))

    def test_entity_without_unique_id_falls_back_to_its_entity_number(self):
        chars = self.import_units([unit("2", None, "Alex", main=True), unit("7", None, "Alex")])
        self.assertEqual(sorted(c["key"] for c in chars), ["e2", "e7"])

    def test_legacy_name_slug_is_kept_for_older_saved_plans(self):
        chars = self.import_units([unit("2", "u1", "Pandora", main=True)])
        self.assertEqual(chars[0]["slug"], "pandora")


if __name__ == "__main__":
    unittest.main()
