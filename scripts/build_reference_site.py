#!/usr/bin/env python3
# Builds the browsable reference site from documentation/reference/, using the page in scripts/reference_site.html.
# It needs no ROM, so the GitHub Pages workflow can run it. Rerun build_reference_docs.py first if the game data changed.
#
#   python3 scripts/build_reference_site.py [output folder]
import json
import os
import re
import sys

REFERENCE_DIR = "documentation/reference"
TEMPLATE = "scripts/reference_site.html"
DEFAULT_OUTPUT = "build/reference_site"


def read_lines(name):
    with open(os.path.join(REFERENCE_DIR, name), encoding="utf-8") as source:
        return source.read().split("\n")


def read_table(lines, index):
    header = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
    rows = []
    index += 2
    while index < len(lines) and lines[index].startswith("|"):
        rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
        index += 1
    return header, rows, index


def name_list(text):
    return [] if text in ("None", "–", "") else [name.strip() for name in text.split(", ")]


def read_pokemon():
    parts = re.split(r"\n## (\d{3}) (.+)\n", "\n".join(read_lines("pokemon.md")))
    pokemon = []
    for number, name, body in zip(parts[1::3], parts[2::3], parts[3::3]):
        entry = {"n": int(number), "name": name, "lvl": [], "tm": [], "tutor": [], "egg": [], "evo": [], "chg": [], "cyc": None, "hid": None}
        for line in body.split("\n"):
            if line.startswith("- Type: "):
                entry["types"] = line[8:].split("/")
            elif line.startswith("- Abilities: "):
                match = re.match(r"(.*?)(?: \(hidden: (.*)\))?$", line[13:])
                entry["ab"] = name_list(match.group(1))
                entry["hid"] = match.group(2)
            elif line.startswith("- Base stats"):
                entry["st"] = [int(value) for value in line.split(": ")[1].split("/")]
            elif line.startswith("- Evolves: "):
                entry["evo"] = line[11:].split("; ")
            elif line.startswith("- Level-up moves: "):
                entry["lvl"] = [[level, move.strip()] for move, level in re.findall(r"([^,()]+) \((evolve|\d+)\)", line[18:])]
            elif line.startswith("- TMs/HMs: "):
                entry["tm"] = name_list(line[11:])
            elif line.startswith("- Tutor moves: "):
                entry["tutor"] = name_list(line[15:])
            elif line.startswith("- Egg moves: "):
                entry["egg"] = name_list(line[13:])
            elif line.startswith("- Egg cycles: "):
                entry["cyc"] = int(line[14:])
            elif line.startswith("    - "):
                entry["chg"][-1][2].append(line[6:])
            elif line.startswith("  - "):
                key, _, value = line[4:-1].partition(":") if line.endswith(":") else line[4:].rpartition(": ")
                entry["chg"].append([key, value, []])
        pokemon.append(entry)
    return pokemon


def read_areas(name, heading, group_heading=None):
    lines = read_lines(name)
    areas = []
    group = area = kind = None
    index = 0
    while index < len(lines):
        line = lines[index]
        if group_heading and line.startswith(group_heading):
            group = line[len(group_heading):]
            area = None
        elif line.startswith(heading):
            area = {"a": line[len(heading):], "m": [], "sp": None}
            if group:
                area["g"] = group
            areas.append(area)
            kind = None
        elif area is not None and line.startswith("**"):
            kind = line.strip("*")
        elif area is not None and line.startswith("Special: "):
            area["sp"] = line[9:].split("; ")
        elif area is not None and line.startswith("|"):
            header, rows, index = read_table(lines, index)
            area["m"].append({"k": kind, "h": header, "r": rows})
            continue
        index += 1
    return areas


def read_trainers(name):
    lines = read_lines(name)
    trainers = []
    group = trainer = None
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("## "):
            group = line[3:]
        elif line.startswith("### "):
            match = re.match(r"### (.*) \(trainer (\d+)\)", line)
            trainer = {"g": group, "name": match.group(1), "id": int(match.group(2)), "it": None, "t": []}
            trainers.append(trainer)
        elif trainer is not None and line.startswith("Uses in battle: "):
            trainer["it"] = line[16:]
        elif trainer is not None and line.startswith("|"):
            _, trainer["t"], index = read_table(lines, index)
            continue
        index += 1
    return trainers


def read_moves():
    parts = re.split(r"\n## (.+)\n", "\n".join(read_lines("moves.md")))
    moves = []
    for name, body in zip(parts[1::2], parts[2::2]):
        fields = dict(re.findall(r"^- ([^:]+): (.*)$", body, re.M))
        moves.append({"name": name, "type": fields["Type"], "cat": fields["Category"], "pow": fields["Power"], "acc": fields["Accuracy"],
                      "pp": fields["PP"], "desc": fields["Description"], "src": fields.get("Machine", "").split("; ") if fields.get("Machine") else [],
                      "lvl": [[mon.strip(), level] for mon, level in re.findall(r"([^,()]+) \((evolve|Lv \d+)\)", fields.get("Level-up", ""))],
                      "tm": name_list(fields.get("TM/HM", "")), "tutor": name_list(fields.get("Tutor", "")), "egg": name_list(fields.get("Egg", ""))})
    return moves


def read_shops():
    lines = read_lines("items.md")
    shops = []
    index = 0
    while index < len(lines):
        if lines[index].startswith("## "):
            shops.append({"name": lines[index][3:]})
        elif lines[index].startswith("|") and shops:
            shops[-1]["h"], shops[-1]["r"], index = read_table(lines, index)
            continue
        index += 1
    return shops


def main():
    output = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    data = {"P": read_pokemon(), "E": read_areas("encounters.md", "## "), "S": read_areas("special_encounters.md", "### ", "## "),
            "T": read_trainers("trainers.md"), "O": read_trainers("other_trainers.md"), "M": read_moves(), "I": read_shops()}
    with open(TEMPLATE, encoding="utf-8") as source:
        page = source.read()
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    os.makedirs(output, exist_ok=True)
    with open(os.path.join(output, "index.html"), "w", encoding="utf-8") as target:
        target.write(page.replace("__DATA__", text))
    print("Wrote %s with %d Pokémon, %d areas, %d trainer fights, %d moves and %d shops" % (os.path.join(output, "index.html"), len(data["P"]),
          len(data["E"]) + len(data["S"]), len(data["T"]) + len(data["O"]), len(data["M"]), len(data["I"])))


if __name__ == "__main__":
    main()
