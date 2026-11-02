#!/usr/bin/env python3
# Rebuilds the time-of-day lists in data/PokedexArea.c from data/Encounters.c, so the Pokédex area maps match
# the wild encounters. Swarm and radio Pokémon are added to the Special lists, which otherwise keep their Headbutt areas.
#
#   python3 scripts/build_dex_areas.py
import re

MAX_SPECIES = 1075  # distance between one list type's members in sPokedexAreaLists
AREA_FILE = "data/PokedexArea.c"
ENCOUNTER_FILE = "data/Encounters.c"
AREA_KINDS = ["SpecialAreasMorning", "SpecialAreasDay", "SpecialAreasNight", "RoutesAndCitiesMorning",
              "RoutesAndCitiesDay", "RoutesAndCitiesNight", "SpecialAreasSpecial", "RoutesAndCitiesSpecial"]

# encounter tables that aren't named after their area, or share one
EXPLICIT_AREAS = {"R02_ROUTE_2_SOUTH_BELOW_VIRIDIAN_FOREST": "ROUTE_2", "R02R0101_ROUTE_2_NORTH_ABOVE_VIRIDIAN_FOREST": "ROUTE_2_2",
                  "R16R0301_ROUTE_16": "ROUTE_16", "T31_MT_SILVER_OUTSIDE_POKEMON_CENTER": "MT_SILVER",
                  "T09_CINNABAR_ISLAND": "CINNABAR_CITY", "D48R0101_CLIFF_EDGE_GATE": "CLIFF_EDGE_GATE",
                  "D50R0101_CLIFF_CAVE": "CLIFF_CAVE"}
PREFIX_AREAS = ["SPROUT_TOWER", "RUINS_OF_ALPH", "UNION_CAVE", "SLOWPOKE_WELL", "ILEX_FOREST", "NATIONAL_PARK", "BURNED_TOWER",
                "BELL_TOWER", "WHIRL_ISLANDS", "MT_MORTAR", "ICE_PATH", "DRAGONS_DEN", "DARK_CAVE", "MT_MOON", "SEAFOAM_ISLANDS",
                "ROCK_TUNNEL", "VICTORY_ROAD", "TOHJO_FALLS", "DIGLETTS_CAVE", "VIRIDIAN_FOREST", "CERULEAN_CAVE"]


def read_tables():
    text = open(ENCOUNTER_FILE).read()
    parts = re.split(r"\n    \[ENCDATA_(\w+)\] = \{", text)
    return list(zip(parts[1::2], parts[2::2]))


def field(body, name):
    match = re.search(rf"\.{name} = (\d+|\{{.*?\n        \}}|\{{[^\n]*\}})", body, re.S)
    return match.group(1) if match else ""


def species_in(body, name):
    return [s for s in re.findall(r"SPECIES_\w+", field(body, name)) if s != "SPECIES_NONE"]


def area_for(table):
    if table in EXPLICIT_AREAS:
        return EXPLICIT_AREAS[table]
    if "UNUSED" in table:
        return None
    if table.startswith("D41"):
        return "MT_SILVER_CAVE"
    for area in PREFIX_AREAS:
        if area in table:
            return area
    match = re.match(r"^[A-Z0-9]+_(.+)$", table)
    return match.group(1) if match else None


def species_numbers():
    text = open("include/constants/species.h").read()
    return {name: int(value, 0) for name, value in re.findall(r"#define\s+(SPECIES_\w+)\s+(\d+|0x[0-9a-fA-F]+)", text)}


def main():
    source = open(AREA_FILE).read()
    enum_text = open("include/constants/pokedex.h").read()
    valid = {name: int(value, 0) for name, value in re.findall(r"DEX_(\w+) = (0x\w+)", enum_text)}
    special_names = list(valid)[1:list(valid).index("NEW_BARK_TOWN")]
    numbers = species_numbers()

    found = {}  # (species number, list kind) -> set of area names
    def add(species_list, area, times):
        prefix = "SpecialAreas" if area in special_names else "RoutesAndCities"
        for species in species_list:
            for time in times:
                found.setdefault((numbers[species], prefix + time), set()).add(area)

    for table, body in read_tables():
        area = area_for(table)
        if area is None:
            continue
        if area not in valid:
            raise SystemExit(f"{table}: no DEX_{area}")
        if field(body, "rateWalk") != "0":
            add(species_in(body, "speciesMorning"), area, ["Morning"])
            add(species_in(body, "speciesDay"), area, ["Day"])
            add(species_in(body, "speciesNight"), area, ["Night"])
        for rate, slots in (("rateSurf", "surfSlots"), ("rateRockSmash", "rockSmashSlots"), ("rateOldRod", "oldRodSlots"),
                            ("rateGoodRod", "goodRodSlots"), ("rateSuperRod", "superRodSlots")):
            if field(body, rate) != "0":
                add(species_in(body, slots), area, ["Morning", "Day", "Night"])
        add(species_in(body, "nightFish"), area, ["Night"])
        add(species_in(body, "landSwarm") + species_in(body, "surfSwarm") + species_in(body, "fishSwarm")
            + species_in(body, "hoennSoundSpecies") + species_in(body, "sinnohSoundSpecies"), area, ["Special"])

    members = dict((name, int(index)) for index, name in re.findall(r"\[(\d+)\] = \{ (sPokedexArea\w+),", source))

    def rewrite(match):
        name, body = match.group(1), match.group(2)
        kind = next((k for k in AREA_KINDS if name.startswith(f"sPokedexArea{k}_")), None)
        if kind is None:
            return match.group(0)
        species = members[name] % MAX_SPECIES
        areas = found.get((species, kind), set())
        if kind.endswith("Special"):
            areas = areas | set(re.findall(r"DEX_(\w+),", body)) - {"END_AREA_DATA"}
        else:
            # Safari Zone tables are separate from Encounters.c and are unchanged
            areas = areas | ({"SAFARI_ZONE_GATE"} & set(re.findall(r"DEX_(\w+),", body)))
        lines = [f"    DEX_{area},\n" for area in sorted(areas, key=lambda a: valid[a])]
        return f"static const u32 {name}[] =\n{{\n{''.join(lines)}    DEX_END_AREA_DATA,\n}};"

    source = re.sub(r"static const u32 (sPokedexArea\w+)\[\] =\n\{\n(.*?)\};", rewrite, source, flags=re.S)
    open(AREA_FILE, "w").write(source)


if __name__ == "__main__":
    main()
