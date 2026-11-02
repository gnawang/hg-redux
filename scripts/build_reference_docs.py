#!/usr/bin/env python3
# Generates the player reference in documentation/reference/ from the game data, so the tables can't
# drift from what the game does. Rerun it after changing encounters, trainers, Pokemon or learnsets:
#   python3 scripts/build_reference_docs.py
#
# "Changed from hg-engine" sections compare against the commit Redux last merged from upstream.
import argparse
import json
import os
import re
import struct
import subprocess

OUTPUT_DIR = "documentation/reference"

# chance of each slot, from src/field/encounter_check.c
LAND_RATES = [20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1]
SURF_RATES = [60, 30, 5, 4, 1]
ROD_RATES = [40, 30, 15, 10, 5]
ROCK_SMASH_RATES = [80, 20]
HEADBUTT_RATES = [50, 15, 15, 10, 5, 5]
SAFARI_SLOT_RATE = 10
HEADBUTT_SLOTS_PER_TREE = 6
# these tables are placeholders: the contest and the Safari Zone use their own data
PLACEHOLDER_AREAS = ["ENCDATA_D22R0102_NATIONAL_PARK_BUG_CATCHING_CONTEST", "ENCDATA_D47R0102_SAFARI_ZONE_PLACEHOLDER_UNUSED"]

BUG_CONTEST_FILE = "base/root/data/mushi/mushi_encount.bin"
BUG_CONTEST_SLOT_SIZE = 8
BUG_CONTEST_SLOTS = 10
BUG_CONTEST_SETS = ["Johto Dex", "National Dex, Tuesday", "National Dex, Thursday", "National Dex, Saturday"]

# the Redux roster besides the 493 Pokemon of Gens 1-4, from the design rules in REDUX_CHANGES.md
ROSTER_EXTRAS = ["SPECIES_SYLVEON", "SPECIES_WYRDEER", "SPECIES_KLEAVOR", "SPECIES_URSALUNA", "SPECIES_ANNIHILAPE",
                 "SPECIES_FARIGIRAF", "SPECIES_DUDUNSPARCE"]
LAST_GEN_4_SPECIES = 493

KEY_TRAINER_GROUPS = [
    ("Rival", ["RIVAL"]),
    ("Johto Gym Leaders", ["LEADER_FALKNER", "LEADER_BUGSY", "LEADER_WHITNEY", "LEADER_MORTY", "LEADER_CHUCK",
                           "LEADER_JASMINE", "LEADER_PRYCE", "LEADER_CLAIR"]),
    ("Elite Four and Champion", ["ELITE_FOUR_WILL", "ELITE_FOUR_KOGA", "ELITE_FOUR_BRUNO", "ELITE_FOUR_KAREN",
                                 "CHAMPION", "PKMN_TRAINER_LANCE"]),
    ("Kanto Gym Leaders", ["LEADER_BROCK", "LEADER_MISTY", "LEADER_LT_SURGE", "LEADER_ERIKA", "LEADER_JANINE",
                           "LEADER_SABRINA", "LEADER_BLAINE", "LEADER_BLUE"]),
    ("Team Rocket", ["EXECUTIVE_ARCHER", "EXECUTIVE_ARIANA", "EXECUTIVE_PROTON", "EXECUTIVE_PETREL", "ROCKET_BOSS"]),
    ("Red", ["PKMN_TRAINER_RED"]),
]

EVOLUTION_TEXT = {
    "EVO_LEVEL": "Level {level}",
    "EVO_LEVEL_FEMALE": "Level {level}, female",
    "EVO_LEVEL_MALE": "Level {level}, male",
    "EVO_LEVEL_DAY": "Level {level}, day",
    "EVO_LEVEL_NIGHT": "Level {level}, night",
    "EVO_LEVEL_DUSK": "Level {level}, dusk",
    "EVO_LEVEL_RAIN": "Level {level}, raining",
    "EVO_LEVEL_ATK_GT_DEF": "Level {level}, Attack above Defense",
    "EVO_LEVEL_ATK_EQ_DEF": "Level {level}, Attack equal to Defense",
    "EVO_LEVEL_ATK_LT_DEF": "Level {level}, Attack below Defense",
    "EVO_LEVEL_PID_LO": "Level {level}, personality low",
    "EVO_LEVEL_PID_HI": "Level {level}, personality high",
    "EVO_LEVEL_NINJASK": "Level {level}",
    "EVO_LEVEL_SHEDINJA": "Level {level}, spare party slot and Poké Ball",
    "EVO_STONE": "Use {item}",
    "EVO_STONE_MALE": "Use {item}, male",
    "EVO_STONE_FEMALE": "Use {item}, female",
    "EVO_TRADE": "Trade",
    "EVO_TRADE_ITEM": "Trade holding {item}",
    "EVO_ITEM_DAY": "Level up holding {item}, day",
    "EVO_ITEM_NIGHT": "Level up holding {item}, night",
    "EVO_HAS_MOVE": "Level up knowing {move}",
    "EVO_FRIENDSHIP": "Level up with high friendship",
    "EVO_FRIENDSHIP_DAY": "Level up with high friendship, day",
    "EVO_FRIENDSHIP_NIGHT": "Level up with high friendship, night",
    "EVO_BEAUTY": "Level up with high beauty",
    "EVO_MAGNETIC_FIELD": "Level up in a magnetic field",
}


# the game's own names, filled in by load_game_names, so "ITEM_KINGS_ROCK" reads "King's Rock"
GAME_NAMES = {}


def load_game_names():
    for header, text_file in (("include/constants/item.h", "data/text/222.txt"), ("include/constants/ability.h", "data/text/720.txt")):
        with open(text_file, encoding="utf-8") as source:
            names = source.read().split("\n")
        with open(header, encoding="utf-8") as source:
            for constant, value in re.findall(r"#define ((?:ITEM|ABILITY)_\w+)\s+(\d+)", source.read()):
                if int(value) < len(names):
                    GAME_NAMES.setdefault(constant, names[int(value)])

    with open("data/Moves.c", encoding="utf-8") as source:
        GAME_NAMES.update(re.findall(r'\[(MOVE_\w+)\] = \{.*?\.name = "([^"]*)"', source.read(), re.S))


def pretty(constant):
    if constant in GAME_NAMES:
        return GAME_NAMES[constant]
    words = re.sub(r"^(SPECIES|MOVE|ITEM|ABILITY|TYPE|TRAINERCLASS)_", "", constant).replace("_", " ").title()
    return re.sub(r"\b(Of|The|In)\b", lambda match: match.group(1).lower(), words)


def block(text, key):
    # returns what's inside the braces of `.key = { ... }`
    start = re.search(r"\.%s =\s*\{" % key, text)
    if start is None:
        return ""
    depth = 1
    position = start.end()
    while depth:
        depth += {"{": 1, "}": -1}.get(text[position], 0)
        position += 1
    return text[start.end():position - 1]


def split_entries(text, pattern):
    # splits a C array into (key, body) for each `[KEY] = {`
    matches = list(re.finditer(pattern, text, re.M))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        yield match.group(1), text[match.end():end]


def read_file(path, revision=None):
    if revision is None:
        with open(path, encoding="utf-8") as source:
            return source.read()
    return subprocess.run(["git", "show", "%s:%s" % (revision, path)], capture_output=True, text=True, encoding="utf-8", check=True).stdout


def read_species(revision=None):
    species = {}
    for key, body in split_entries(read_file("data/Species.c", revision), r"^    \[(SPECIES_\w+)\] = \{"):
        name = re.search(r'\.name = "([^"]*)"', body)
        types = re.search(r"\.types = \{ (\w+), (\w+) \}", body)
        abilities = re.search(r"\.abilities = \{ (\w+), (\w+) \}", body)
        if name and types and abilities:
            species[key] = {
                "name": name.group(1),
                "types": list(dict.fromkeys(types.groups())),
                "abilities": [ability for ability in dict.fromkeys(abilities.groups()) if ability != "ABILITY_NONE"],
                "stats": [int(re.search(r"\.%s = (\d+)" % stat, body).group(1))
                          for stat in ("hp", "attack", "defense", "spAttack", "spDefense", "speed")],
                "hatch_cycles": int(re.search(r"\.hatchCycles = (\d+)", body).group(1)),
            }
    return species


def read_evolutions(revision=None):
    evolutions = {}
    for key, body in split_entries(read_file("data/Evolutions.c", revision), r"^    \[(SPECIES_\w+)\] = \{"):
        entries = re.findall(r"\{ (EVO_\w+), (\w+), (\w+)", body)
        evolutions[key] = [entry for entry in entries if entry[0] != "EVO_NONE"]
    return evolutions


def read_hidden_abilities(revision=None):
    return dict(re.findall(r"\[(SPECIES_\w+)\s*\] = (ABILITY_\w+)", read_file("data/HiddenAbilityTable.c", revision)))


def read_learnsets(revision=None):
    return json.loads(read_file("data/learnsets/learnsets.json", revision))


def read_game_moves(path):
    return {move for move in re.findall(r"\bMOVE_\w+", read_file(path)) if move != "MOVE_NONE" and not move.startswith("MOVE_TUTOR_NPC")}


def read_species_ids():
    with open("include/constants/species.h", encoding="utf-8") as source:
        return {name: int(value) for name, value in re.findall(r"#define (SPECIES_\w+)\s+(\d+)", source.read())}


def evolution_text(method, argument, names):
    template = EVOLUTION_TEXT.get(method)
    if template is None:
        return "%s (%s)" % (pretty(method.replace("EVO_", "")), pretty(argument))
    return template.format(level=argument, item=pretty(argument), move=pretty(argument))


def percent_cell(entries):
    if not entries:
        return "–"
    levels = sorted(level for _, level in entries)
    level_text = "%d" % levels[0] if levels[0] == levels[-1] else "%d–%d" % (levels[0], levels[-1])
    return "%d%% (Lv %s)" % (sum(rate for rate, _ in entries), level_text)


def land_table(body, names):
    land = block(body, "landSlots")
    levels = [int(value) for value in re.findall(r"\d+", block(land, "levels"))]
    species_by_time = [re.findall(r"SPECIES_\w+", block(land, "species%s" % time)) for time in ("Morning", "Day", "Night")]

    rows = {}
    for time, slots in enumerate(species_by_time):
        for slot, species in enumerate(slots):
            if species != "SPECIES_NONE":
                rows.setdefault(species, ([], [], []))[time].append((LAND_RATES[slot], levels[slot]))
    return ["| %s | %s | %s | %s |" % (names.get(species, pretty(species)), *map(percent_cell, cells)) for species, cells in rows.items()]


def slot_rows(slots, rates, names):
    # slots is (species, min level, max level) in slot order
    rows = {}
    for rate, (species, low, high) in zip(rates, slots):
        if species != "SPECIES_NONE":
            row = rows.setdefault(species, [0, int(low), int(high)])
            row[0] += rate
            row[1] = min(row[1], int(low))
            row[2] = max(row[2], int(high))

    lines = []
    for species, (rate, low, high) in rows.items():
        levels = "%d" % low if low == high else "%d–%d" % (low, high)
        lines.append("| %s | %d%% | %s |" % (names.get(species, pretty(species)), rate, levels))
    return lines


def slot_table(body, key, rates, names):
    slots = [(species, low, high) for low, high, species in re.findall(r"\{ (\d+), (\d+), (SPECIES_\w+) \}", block(body, key))]
    return slot_rows(slots, rates, names)


def encounter_area_name(key):
    return pretty(re.sub(r"^ENCDATA_[A-Z0-9]+_", "", key))


def build_encounters(species):
    names = {key: value["name"] for key, value in species.items()}
    lines = ["# Wild encounters", "",
             "Generated from `data/Encounters.c` by `scripts/build_reference_docs.py`. Don't edit by hand.", "",
             "Percentages are the chance of each Pokémon when an encounter happens, adding up every slot it fills. "
             "Chances come from `src/field/encounter_check.c`.", "",
             "- Grass and caves: 12 slots at 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1 and 1%, with separate morning, day and night tables",
             "- Surfing: 60, 30, 5, 4 and 1%", "- All rods: 40, 30, 15, 10 and 5%", "- Rock Smash: 80 and 20%", "",
             "Evening uses the day table, and late night uses the night table.", "",
             "\"Special\" lists Pokémon that take over slots under a condition. The tables above don't include them.", "",
             "| Condition | Effect |", "|---|---|",
             "| Land swarm | Takes the two 20% slots, 40% in all |",
             "| Hoenn or Sinnoh Sound on the radio | Each listed Pokémon takes two 10% slots, 20% each |",
             "| Surf swarm | Takes the 60% slot |",
             "| Fishing swarm | Old Rod 15%, Good Rod 65%, Super Rod 100% |",
             "| Night fishing, at night or late night | Good Rod 10%, Super Rod 30% |", "",
             "Headbutt trees, the Safari Zone and the Bug-Catching Contest are in [special_encounters.md](special_encounters.md). "
             "Gift and one-off Pokémon are in [gift_static.md](gift_static.md).", ""]

    text = read_file("data/Encounters.c")
    for key, body in split_entries(text, r"^    \[(ENCDATA_\w+)\] = \{"):
        if key in PLACEHOLDER_AREAS:
            continue

        area = []
        land = land_table(body, names)
        if land:
            area += ["**Grass/cave**", "", "| Pokémon | Morning | Day | Night |", "|---|---|---|---|"] + land + [""]

        for label, block_key, rates in (("Surfing", "surfSlots", SURF_RATES), ("Rock Smash", "rockSmashSlots", ROCK_SMASH_RATES),
                                        ("Old Rod", "oldRodSlots", ROD_RATES), ("Good Rod", "goodRodSlots", ROD_RATES),
                                        ("Super Rod", "superRodSlots", ROD_RATES)):
            table = slot_table(body, block_key, rates, names)
            if table:
                area += ["**%s**" % label, "", "| Pokémon | Chance | Levels |", "|---|---|---|"] + table + [""]

        special = []
        for label, pattern in (("Land swarm", r"\.landSwarm = (\w+)"), ("Surf swarm", r"\.surfSwarm = (\w+)"),
                               ("Fishing swarm", r"\.fishSwarm = (\w+)"), ("Night fishing", r"\.nightFish = (\w+)")):
            match = re.search(pattern, body)
            if match and match.group(1) != "SPECIES_NONE" and area:
                special.append("%s: %s" % (label, names.get(match.group(1), pretty(match.group(1)))))
        for label, block_key in (("Hoenn Sound", "hoennSoundSpecies"), ("Sinnoh Sound", "sinnohSoundSpecies")):
            sound = [names.get(value, pretty(value)) for value in re.findall(r"SPECIES_\w+", block(body, block_key)) if value != "SPECIES_NONE"]
            if sound:
                special.append("%s: %s" % (label, ", ".join(sound)))
        if special:
            area += ["Special: " + "; ".join(special), ""]

        if area:
            lines += ["## %s" % encounter_area_name(key), ""] + area
    return lines


def words_from_camel_case(key):
    words = re.sub(r"(?<=[a-z])(?=[A-Z0-9])", " ", key)
    return words[0].upper() + words[1:]


def build_headbutt(names):
    lines = ["## Headbutt trees", "",
             "Each tree uses the common or rare table, decided by the tree and the last digit of your Trainer ID. Slots are "
             "50, 15, 15, 10, 5 and 5%. Secret trees are a third kind of tree.", ""]
    text = read_file("data/Headbutt.c")
    data = text[text.index("const HeadbuttArchiveData __data"):]
    for key, body in split_entries(data, r"^    \.(\w+) = \{"):
        regular = int(re.search(r"\.normalTreeCount = (\d+)", body).group(1))
        secret = int(re.search(r"\.specialTreeCount = (\d+)", body).group(1))
        if regular + secret == 0:
            continue

        normal = re.findall(r"\{ (SPECIES_\w+), (\d+), (\d+) \}", block(body, "normalSlots"))
        special = re.findall(r"\{ (SPECIES_\w+), (\d+), (\d+) \}", block(body, "specialSlots"))
        lines += ["### %s" % words_from_camel_case(key), ""]
        for label, slots in (("Common trees", normal[:HEADBUTT_SLOTS_PER_TREE]), ("Rare trees", normal[HEADBUTT_SLOTS_PER_TREE:]), ("Secret trees", special if secret else [])):
            rows = slot_rows(slots, HEADBUTT_RATES, names)
            if rows:
                lines += ["**%s**" % label, "", "| Pokémon | Chance | Levels |", "|---|---|---|"] + rows + [""]
    return lines


def safari_cell(slot, names):
    return "%s (Lv %s)" % (names.get(slot[0], pretty(slot[0])), slot[1])


def safari_needs(condition):
    needs = re.findall(r"SAFARI_ZONE_OBJECT_TYPE_(\w+), (\d+)", condition)
    return ", ".join("%s %s" % (name.title(), count) for name, count in needs if name != "NONE")


def build_safari(names):
    lines = ["## Safari Zone", "",
             "Every area has 10 equal slots, each 10%. Evening uses the day table, and late night uses the night table.", "",
             "Bonus Pokémon are locked until the area has reached the listed levels of Plains, Forest, Peak or Water objects. "
             "Each unlocked bonus takes one of the 10 slots, so it's a 10% chance.", ""]
    text = read_file("data/SafariEncounters.c")
    slot_pattern = r"\{ (SPECIES_\w+), (\d+) \}"
    for key, body in split_entries(text, r"^    \[SAFARI_ZONE_AREA_(\w+)\] = \{"):
        lines += ["### %s" % pretty(key), ""]
        for label, section_key in (("Grass/cave", "land"), ("Surfing", "surf"), ("Old Rod", "oldRod"), ("Good Rod", "goodRod"), ("Super Rod", "superRod")):
            section = block(body, section_key)
            rows = {}
            for time, name in enumerate(("Morning", "Day", "Night")):
                for species, level in re.findall(slot_pattern, block(section, "species%s" % name)):
                    if species != "SPECIES_NONE":
                        rows.setdefault(species, ([], [], []))[time].append((SAFARI_SLOT_RATE, int(level)))
            lines += ["**%s**" % label, "", "| Pokémon | Morning | Day | Night |", "|---|---|---|---|"]
            lines += ["| %s | %s | %s | %s |" % (names.get(species, pretty(species)), *map(percent_cell, cells)) for species, cells in rows.items()] + [""]

            bonuses = [re.findall(slot_pattern, block(section, "bonusSpecies%s" % name)) for name in ("Morning", "Day", "Night")]
            conditions = re.findall(r"\{ \.objects = .*\}", block(section, "bonusUnlockConditions"))
            if bonuses[0]:
                lines += ["| Bonus: morning | Bonus: day | Bonus: night | Needs |", "|---|---|---|---|"]
                for morning, day, night, condition in zip(*bonuses, conditions):
                    lines.append("| %s | %s | %s | %s |" % (safari_cell(morning, names), safari_cell(day, names), safari_cell(night, names), safari_needs(condition)))
                lines.append("")
    return lines


def build_bug_contest(names, ids):
    if not os.path.exists(BUG_CONTEST_FILE):
        raise SystemExit("%s is missing. Run make first." % BUG_CONTEST_FILE)
    with open(BUG_CONTEST_FILE, "rb") as source:
        data = source.read()

    species_by_id = {number: key for key, number in ids.items()}
    lines = ["## Bug-Catching Contest", "",
             "Held on Tuesdays, Thursdays and Saturdays. Without the National Dex the game always uses the first set. With it, "
             "the set depends on the day. Redux's `ALWAYS_HAVE_NATIONAL_DEX` setting should mean you get the National Dex sets. "
             "Levels are random within the range.", ""]
    for index, label in enumerate(BUG_CONTEST_SETS):
        lines += ["### %s" % label, "", "| Pokémon | Chance | Levels | Base score |", "|---|---|---|---|"]
        threshold = 100
        for slot in range(BUG_CONTEST_SLOTS):
            species, low, high, rate, score = struct.unpack_from("<HBBBB", data, (index * BUG_CONTEST_SLOTS + slot) * BUG_CONTEST_SLOT_SIZE)
            key = species_by_id[species]
            levels = "%d" % low if low == high else "%d–%d" % (low, high)
            lines.append("| %s | %d%% | %s | %d |" % (names.get(key, pretty(key)), threshold - rate, levels, score))
            threshold = rate
        lines.append("")
    return lines


def build_special_encounters(species):
    names = {key: value["name"] for key, value in species.items()}
    lines = ["# Special wild encounters", "",
             "Generated by `scripts/build_reference_docs.py` from `data/Headbutt.c`, `data/SafariEncounters.c` and the "
             "built ROM's Bug-Catching Contest table. Don't edit by hand.", ""]
    return lines + build_headbutt(names) + build_safari(names) + build_bug_contest(names, read_species_ids())


def trainer_ability(entry, data, species, hidden):
    abilities = species.get(data, {}).get("abilities", [])
    if not abilities:
        return "–"
    if "ABILITY_HIDDEN" in entry and data in hidden:
        return pretty(hidden[data])
    second = "ABILITY_2" in entry
    return pretty(abilities[1] if second and len(abilities) > 1 else abilities[0])


def build_trainers(species):
    names = {key: value["name"] for key, value in species.items()}
    hidden = read_hidden_abilities()
    lines = ["# Key trainers", "",
             "Generated from `data/Trainers.c` by `scripts/build_reference_docs.py`. Don't edit by hand.", "",
             "Teams are listed in trainer ID order, which is roughly the order you meet them. A trainer with several "
             "entries has several fights, and the rival's entries also vary with your starter.", "",
             "\"Default\" moves means the Pokémon uses the latest moves it would know at that level.", ""]

    trainers = {}
    for key, body in split_entries(read_file("data/Trainers.c"), r"^    \[(\d+)\] = \{"):
        trainer_class = re.search(r"\.trainerClass = TRAINERCLASS_(\w+)", body)
        if trainer_class:
            trainers.setdefault(trainer_class.group(1), []).append((int(key), body))

    for group, classes in KEY_TRAINER_GROUPS:
        lines += ["## %s" % group, ""]
        for trainer_class in classes:
            for number, body in trainers.get(trainer_class, []):
                party = block(body, "party")
                entries = re.findall(r"\{\s*\.ivs.*?\.ballSeal = \d+,\s*\}", party, re.S)
                if not entries:
                    continue
                name = re.search(r'\.name = "([^"]*)"', body).group(1)
                bag = [pretty(item) for item in re.findall(r"ITEM_\w+", re.search(r"\.items = \{([^}]*)\}", body).group(1)) if item != "ITEM_NONE"]
                lines += ["### %s (trainer %d)" % (name, number), ""]
                if bag:
                    lines += ["Uses in battle: %s" % ", ".join(bag), ""]
                lines += ["| Pokémon | Level | Ability | Held item | Moves |", "|---|---|---|---|---|"]
                for entry in entries:
                    mon = re.search(r"\.species = (SPECIES_\w+)", entry).group(1)
                    level = re.search(r"\.level = (\d+)", entry).group(1)
                    item = re.search(r"\.item = (ITEM_\w+)", entry)
                    moves = re.search(r"\.moves = \{([^}]*)\}", entry)
                    move_text = "Default"
                    if moves:
                        move_text = ", ".join(pretty(move) for move in re.findall(r"MOVE_\w+", moves.group(1)) if move != "MOVE_NONE")
                    held = pretty(item.group(1)) if item and item.group(1) != "ITEM_NONE" else "–"
                    lines.append("| %s | %s | %s | %s | %s |" % (names.get(mon, pretty(mon)), level, trainer_ability(entry, mon, species, hidden), held, move_text))
                lines.append("")
    return lines


def level_moves(learnset):
    return [(entry["Level"], entry["Move"]) for entry in learnset.get("LevelMoves", [])]


def level_text(level):
    return "evolve" if level == 0 else "Lv %d" % level


def move_change_text(old, new):
    old_levels, new_levels = {}, {}
    for levels, moves in ((old_levels, old), (new_levels, new)):
        for level, move in moves:
            levels.setdefault(move, level)
    added = [move for level, move in new if move not in old_levels]
    removed = [move for level, move in old if move not in new_levels]
    moved = [move for move, level in new_levels.items() if move in old_levels and old_levels[move] != level]
    parts = []
    if added:
        parts.append("added " + ", ".join("%s (%s)" % (pretty(move), level_text(new_levels[move])) for move in dict.fromkeys(added)))
    if moved:
        parts.append("moved " + ", ".join("%s (%s → %s)" % (pretty(move), level_text(old_levels[move]), level_text(new_levels[move])) for move in moved))
    if removed:
        parts.append("removed " + ", ".join("%s (%s)" % (pretty(move), level_text(old_levels[move])) for move in dict.fromkeys(removed)))
    return "; ".join(parts)


def learnable_moves(learnset, field, game_moves=None):
    moves = dict.fromkeys(learnset.get(field, []))
    return [move for move in moves if game_moves is None or move in game_moves]


def move_list_text(moves):
    return ", ".join(sorted(map(pretty, moves))) or "None"


def set_change_text(old, new):
    added, removed = sorted(map(pretty, set(new) - set(old))), sorted(map(pretty, set(old) - set(new)))
    parts = []
    if added:
        parts.append("added " + ", ".join(added))
    if removed:
        parts.append("removed " + ", ".join(removed))
    return "; ".join(parts)


def friendship_threshold():
    return int(re.search(r"#define FRIENDSHIP_EVOLUTION_THRESHOLD (\d+)", read_file("include/config.h")).group(1))


def build_pokemon(species, base):
    names = {key: value["name"] for key, value in species.items()}
    base_species = read_species(base)
    evolutions, base_evolutions = read_evolutions(), read_evolutions(base)
    hidden, base_hidden = read_hidden_abilities(), read_hidden_abilities(base)
    learnsets, base_learnsets = read_learnsets(), read_learnsets(base)
    machine_moves, tutor_moves = read_game_moves("data/MachineMoves.c"), read_game_moves("src/field/move_tutor.c")
    ids = read_species_ids()
    roster = sorted((key for key, number in ids.items() if 1 <= number <= LAST_GEN_4_SPECIES and key in species), key=ids.get)
    roster += [key for key in ROSTER_EXTRAS if key in species]

    summary = []
    entries = []
    for key in roster:
        data = species[key]
        old = base_species.get(key, data)
        changes = []
        if data["types"] != old["types"]:
            changes.append("Type: %s → %s" % ("/".join(map(pretty, old["types"])), "/".join(map(pretty, data["types"]))))
        if data["abilities"] != old["abilities"] or hidden.get(key) != base_hidden.get(key):
            changes.append("Abilities changed from %s" % ", ".join(map(pretty, old["abilities"])))
        if data["stats"] != old["stats"]:
            changes.append("Base stats changed from %s" % "/".join(map(str, old["stats"])))
        old_evolutions, new_evolutions = base_evolutions.get(key, []), evolutions.get(key, [])
        for method, argument, target in new_evolutions:
            if (method, argument, target) not in old_evolutions:
                changes.append("New evolution: %s → %s" % (evolution_text(method, argument, names), names.get(target, pretty(target))))
        for method, argument, target in old_evolutions:
            if (method, argument, target) not in new_evolutions:
                changes.append("Removed evolution: %s → %s" % (evolution_text(method, argument, names), names.get(target, pretty(target))))
        if changes:
            summary.append("| %s | %s |" % (data["name"], "<br>".join(changes)))

        learnset = learnsets.get(key, {})
        moves = level_moves(learnset)
        evolution_lines = ["%s → %s" % (evolution_text(method, argument, names), names.get(target, pretty(target))) for method, argument, target in new_evolutions]
        ability_text = ", ".join(map(pretty, data["abilities"])) or "None"
        if key in hidden and hidden[key] != "ABILITY_NONE":
            ability_text += " (hidden: %s)" % pretty(hidden[key])

        entries += ["## %03d %s" % (ids[key], data["name"]), "",
                    "- Type: %s" % "/".join(map(pretty, data["types"])),
                    "- Abilities: %s" % ability_text,
                    "- Base stats (HP/Atk/Def/SpA/SpD/Spe): %s" % "/".join(map(str, data["stats"]))]
        if evolution_lines:
            entries.append("- Evolves: %s" % "; ".join(evolution_lines))
        entries.append("- Level-up moves: %s" % ", ".join("%s (%s)" % (pretty(move), "evolve" if level == 0 else level) for level, move in moves))
        move_fields = (("TMs/HMs", "MachineMoves", machine_moves), ("Tutor moves", "TutorMoves", tutor_moves), ("Egg moves", "EggMoves", None))
        for label, field, game_moves in move_fields:
            entries.append("- %s: %s" % (label, move_list_text(learnable_moves(learnset, field, game_moves))))
        if data["hatch_cycles"]:
            entries.append("- Egg cycles: %d" % data["hatch_cycles"])

        details = list(changes)
        base_learnset = base_learnsets.get(key, {})
        level_difference = move_change_text(level_moves(base_learnset), moves)
        if level_difference:
            details.append("Level-up moves: %s" % level_difference)
        for label, field, game_moves in move_fields:
            difference = set_change_text(learnable_moves(base_learnset, field, game_moves), learnable_moves(learnset, field, game_moves))
            if difference:
                details.append("%s: %s" % (label, difference))
        if data["hatch_cycles"] != old["hatch_cycles"]:
            details.append("Egg cycles: %d → %d" % (old["hatch_cycles"], data["hatch_cycles"]))
        if details:
            entries.append("- Changes from hg-engine:")
            entries += ["  - %s" % detail for detail in details]
        entries.append("")

    lines = ["# Pokémon", "",
             "Generated from the data files by `scripts/build_reference_docs.py`. Don't edit by hand.", "",
             "Covers the Redux roster: all 493 Pokémon of Gens 1–4 plus the later evolutions it adds. \"Changed\" means "
             "different from hg-engine, not from the original HeartGold, so changes hg-engine already made aren't flagged.", "",
             "TMs/HMs and tutor moves list only what the game teaches. Friendship evolutions need %d friendship in every case." % friendship_threshold(), "",
             "## Changes from hg-engine", "",
             "This table covers types, abilities, stats and evolutions. Each Pokémon's entry below lists these along with its move and egg cycle changes.", "",
             "| Pokémon | Change |", "|---|---|"] + summary + [""]
    return lines + entries


def write(name, lines):
    with open("%s/%s.md" % (OUTPUT_DIR, name), "w", encoding="utf-8") as out:
        out.write("\n".join(lines).rstrip() + "\n")


def main():
    parser = argparse.ArgumentParser(description="Generate documentation/reference/")
    parser.add_argument("--base", help="hg-engine revision to compare against (default: the merge base with upstream/main)")
    args = parser.parse_args()
    base = args.base or subprocess.run(["git", "merge-base", "HEAD", "upstream/main"], capture_output=True, text=True, check=True).stdout.strip()

    load_game_names()
    species = read_species()
    write("encounters", build_encounters(species))
    write("special_encounters", build_special_encounters(species))
    write("trainers", build_trainers(species))
    write("pokemon", build_pokemon(species, base))


if __name__ == "__main__":
    main()
