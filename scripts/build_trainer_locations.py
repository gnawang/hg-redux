#!/usr/bin/env python3
# Writes scripts/trainer_locations.json: where each trainer is fought and what the fight is (first battle, rematch, rival's
# starter and so on), for the reference pages. It reads a pret/pokeheartgold checkout, which isn't part of this repo, so the
# JSON is committed and only needs regenerating if trainers move. Run from the repo root:
#
#   python3 scripts/build_trainer_locations.py path/to/pokeheartgold
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_reference_docs import encounter_area_name, tidy_place  # noqa: E402

OUTPUT = "scripts/trainer_locations.json"

# Places split over several maps that read better as one.
PLACE_GROUPS = ((r"^Mahogany Gym .*", "Mahogany Gym"), (r"^Pokémon League (Will|Koga|Bruno|Karen|Lance) Room$", "Pokémon League"),
                (r"^Pokémon League Entrance$", "Indigo Plateau"), (r"^Seafoam Islands Cinnabar Gym$", "Cinnabar Gym (Seafoam Islands)"),
                (r"^Azalea$", "Azalea Town"), (r"^Mt. Silver Cave Summit$", "Mt. Silver Summit"), (r"^Saffron Fighting Dojo$", "Fighting Dojo"), (r"^Route 10 South$", "Route 10"))

# Fights the map data can't place or describe. A value replaces what was found.
OVERRIDES = {
    2: {"location": "Cherrygrove City"}, 3: {"location": "Cherrygrove City"}, 265: {"location": "Cherrygrove City"},
    489: {"fight": "Weekly rematch"}, 490: {"fight": "Weekly rematch"}, 491: {"fight": "Weekly rematch"},
    735: {"fight": "Your partner in the tag battle against Lance and Clair"}, 736: {"fight": "Your partner in the tag battle against Lance and Clair"},
    737: {"fight": "Your partner in the tag battle against Lance and Clair"},
    733: {"fight": "Tag battle, with Clair"}, 734: {"fight": "Tag battle, with Lance"},
    675: {"fight": "Your partner in the Rocket Hideout"}, 700: {"fight": "Celebi event"},
    **{n: {"fight": "First round"} for n in (244, 245, 246, 247, 418)},
    **{n: {"fight": "Second round"} for n in (701, 702, 703, 704, 705)},
}


def read_map_names(pret):
    names = {}
    for constant, code in re.findall(r"#define (MAP_\w+)\s+\d+\s+// MAP_(\w+)", open(os.path.join(pret, "include/constants/maps.h")).read()):
        words = constant[4:].split("_")
        names[code] = tidy_place(" ".join(w if re.fullmatch(r"[0-9]+F|B[0-9]+F|[0-9]+", w) else w.capitalize() for w in words))
    return names


def group_place(name):
    for pattern, replacement in PLACE_GROUPS:
        if re.match(pattern, name):
            return replacement
    return name


def main():
    pret = sys.argv[1]
    ids = {name: int(value) for name, value in re.findall(r"#define (TRAINER_\w+)\s+(\d+)", open(os.path.join(pret, "include/constants/trainers.h")).read())}
    map_names = read_map_names(pret)
    areas = {}
    for key in re.findall(r"^    \[(ENCDATA_\w+)\] = \{", open("data/Encounters.c").read(), re.M):
        code = re.match(r"ENCDATA_([A-Z0-9]+)_", key).group(1)
        areas.setdefault(code, encounter_area_name(key))

    def place(code):
        return group_place(areas.get(code) or map_names.get(code, code))

    found = {}
    for path in sorted(glob.glob(os.path.join(pret, "files/fielddata/eventdata/zone_event/*.json"))):
        code = re.match(r"\d+_(\w+)\.json", os.path.basename(path)).group(1)
        for obj in json.load(open(path)).get("objects", []):
            for trainer in re.findall(r"TRAINER_\w+", str(obj.get("scriptId", ""))):
                found.setdefault(ids.get(trainer), code)
    for path in sorted(glob.glob(os.path.join(pret, "files/fielddata/script/scr_seq/scr_seq_*.s"))):
        match = re.match(r"scr_seq_\d+_(\w+)\.s", os.path.basename(path))
        if not match:  # shared scripts with no map
            continue
        code = match.group(1)
        for line in re.findall(r"^\s*(?:TrainerBattle|MultiBattle) (.*)$", open(path).read(), re.M):
            for trainer in re.findall(r"TRAINER_\w+", line):
                found.setdefault(ids.get(trainer), code)
    found.pop(None, None)

    # Phone rematches: each row is the first fight, then the rematches in the order they're called.
    rematch = {}
    table = open(os.path.join(pret, "src/overlay_26_022598C0.c")).read()
    for row in re.findall(r"\{ (TRAINER_\w+,(?:\s*TRAINER_\w+,?)+) \}", table):
        fights = [ids[t] for t in re.findall(r"TRAINER_\w+", row) if t != "TRAINER_NONE"][1:]
        for number, trainer in enumerate(fights[1:], 1):
            if trainer != fights[0]:
                rematch[trainer] = (fights[0], number)

    out = {}
    for trainer, code in found.items():
        out[trainer] = {"location": place(code)}
    for trainer, (first, number) in rematch.items():
        if first in found:
            out[first]["fight"] = "First battle"
            # Gym Leader rematches are in the table but fought at the Fighting Dojo, which the scripts already found.
            where = place(found[trainer]) if trainer in found else place(found[first])
            out[trainer] = {"location": where, "fight": "Rematch %d" % number}
    for trainer, values in OVERRIDES.items():
        out.setdefault(trainer, {}).update(values)
    # Gym Leaders' rematches have one fight each, so they don't need a number.
    for trainer, values in out.items():
        if values.get("location") == "Fighting Dojo" and values.get("fight") == "Rematch 1":
            values["fight"] = "Rematch"
        if values.get("location", "").endswith(" Gym") and values.get("fight") == "First battle":
            values["fight"] = "Gym battle"
    with open(OUTPUT, "w", encoding="utf-8") as target:
        json.dump({str(k): out[k] for k in sorted(out)}, target, indent=1, ensure_ascii=False)
        target.write("\n")
    print("Wrote %s with %d trainers" % (OUTPUT, len(out)))


if __name__ == "__main__":
    main()
