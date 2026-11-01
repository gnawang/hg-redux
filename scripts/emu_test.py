#!/usr/bin/env python3
# Plays test.nds headlessly in DeSmuME so changes can be checked in the real game.
# Savestates and screenshots live in .scratch/emu/ and are referred to by name.
#
#   .venv/bin/python scripts/emu_test.py new-game start
#   .venv/bin/python scripts/emu_test.py team start team1 --mon SPECIES_KADABRA:35 --mon SPECIES_MEGANIUM:8
#   .venv/bin/python scripts/emu_test.py bag team1 team2 --add ITEM_KINGS_ROCK:1
#   .venv/bin/python scripts/emu_test.py party team2
#   .venv/bin/python scripts/emu_test.py step team2 opened t:43:115 w150 snap
#
# See "Testing in the emulator" in AGENTS.md for the input syntax and the screen positions.
import argparse
import os
import re
import struct

from desmume.controls import Keys, keymask
from desmume.emulator import DeSmuME
from PIL import Image

STATE_DIR = ".scratch/emu"
RAM_BASE = 0x02000000
RAM_SIZE = 0x400000

MON_SIZE = 0xEC
BOX_SIZE = 0x88
BLOCK_SIZE = 0x20
PARTY_HEADER_SIZE = 8
PARTY_SIZE = 6
BLOCK_ORDERS = ["ABCD", "ABDC", "ACBD", "ACDB", "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
                "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB", "DBAC", "DBCA", "DCAB", "DCBA"]
EXP_MASK = 0x1FFFFF
ABILITY_MSB = 1 << 31

# slots per pocket in save order, from the ITEM_POCKET_EXPANSION branch of include/constants/item.h
POCKETS = [("items", 245), ("key", 92), ("tms", 101), ("mail", 12), ("medicine", 40), ("berries", 64), ("balls", 26), ("battle", 30)]
ITEM_SLOT_SIZE = 4

KEYS = {"a": Keys.KEY_A, "b": Keys.KEY_B, "x": Keys.KEY_X, "y": Keys.KEY_Y, "l": Keys.KEY_L, "r": Keys.KEY_R,
        "start": Keys.KEY_START, "select": Keys.KEY_SELECT, "up": Keys.KEY_UP, "down": Keys.KEY_DOWN,
        "left": Keys.KEY_LEFT, "right": Keys.KEY_RIGHT}
DEFAULT_HOLD = 6
REPEAT_GAP = 12
HOLD_GAP = 4
TOUCH_HOLD = 30
TOUCH_GAP = 40
STABLE_READ_FRAMES = 60

# inputs from power-on to the overworld with a starter; each entry is (checkpoint name, inputs)
NEW_GAME_ROUTE = [
    ("mom", "w700 start w120 start w270 w120 t:132:152 w240 a%6 w60 "                # title, skip the info screens
            "a%12 a%12 a%12 a%12 a%12 w30 start a w60 a%8 a%8 a%8 w60 a%8 w90 "      # Oak, boy, name AAAAAAA
            "left:50 w10 up:20 w10 left:20 w80 right:20 w8 up:20 w8 left:40 w70 "    # bedroom stairs
            "w120 a%10 a%10 a%10 a%10 a%10 w30 a%6 w130 a%10 w200 a%10 w300 b%5 w60 a%5 w60"),  # Mom's scene and gift
    ("lab", "down:120 w120 down:20 left:130 w10 w30 left:32 w10 down:16 w10 left:64 w10 a%25 a%25 a%25 w20 "  # Lyra
            "left:112 w6 up:80 w6 up:80 w10 right:30 w100 down:100 w8 left:18 down:90 w8 "                    # across town
            "up:150 w8 left:17 w8 up:40 w100 a%15 w20 left:32 w8 up:30 w120 a%20 w10 a%20 w10 a%20 w10 "
            "right:17 w8 up:30 w120 a%25 w10 a%25 w10 a%25 w10"),                    # into the lab
    ("starter", "up:60 w30 a%30 w10 a%30 w10 a%30 w10 right:50 w8 up:20 w8 a w60 a%3 w30 "  # Elm
                "right:17 w8 up:17 w8 a w90 w30 t:75:35 w100 a w60 a%4 w40 "                # first ball, Totodile
                "w90 a%20 w20 b%3 a%25 w20 a%25 w20"),                                      # nickname, end of the scene
]


def state_path(name):
    return os.path.join(STATE_DIR, name + ".ds")


def picture_path(name):
    return os.path.join(STATE_DIR, name + ".png")


def open_emulator(rom, state=None):
    emu = DeSmuME()
    emu.open(rom)
    emu.volume_set(0)
    if state is not None:
        emu.savestate.load_file(state_path(state))
        run(emu, 3)
    return emu


def run(emu, frames):
    for _ in range(frames):
        emu.cycle(with_joystick=False)


def press(emu, key, hold, gap):
    emu.input.keypad_add_key(keymask(KEYS[key]))
    run(emu, hold)
    emu.input.keypad_rm_key(keymask(KEYS[key]))
    run(emu, gap)


def run_inputs(emu, commands, name):
    shots = []
    for command in commands:
        if command == "snap":
            shots.append(emu.screenshot().convert("RGB"))
        elif re.fullmatch(r"w\d+", command):
            run(emu, int(command[1:]))
        elif command.startswith("t:"):
            _, x, y = command.split(":")
            emu.input.touch_set_pos(int(x), int(y))
            run(emu, TOUCH_HOLD)
            emu.input.touch_release()
            run(emu, TOUCH_GAP)
        else:
            match = re.fullmatch(r"([a-z]+)(?:%(\d+)|:(\d+))?", command)
            if match is None or match.group(1) not in KEYS:
                raise SystemExit("Unknown input: %s" % command)
            key, repeat, hold = match.groups()
            for _ in range(int(repeat or 1)):
                press(emu, key, int(hold) if hold else DEFAULT_HOLD, HOLD_GAP if hold else REPEAT_GAP)
    run(emu, 2)
    shots.append(emu.screenshot().convert("RGB"))
    save_contact_sheet(shots, picture_path(name))


def save_contact_sheet(shots, path):
    width, height = shots[0].size
    sheet = Image.new("RGB", ((width + 6) * len(shots) - 6, height), (80, 80, 80))
    for index, shot in enumerate(shots):
        sheet.paste(shot, (index * (width + 6), 0))
    sheet.save(path)


def read_constants():
    # returns {"SPECIES_KADABRA": 64, ...} for the headers the tool's arguments can name
    pending = {}
    for path in ("include/constants/species.h", "include/constants/item.h", "include/constants/moves.h", "include/constants/ability.h"):
        with open(path, encoding="utf-8") as source:
            for line in source:
                match = re.match(r"#define\s+(\w+)\s+([^/\n]+)", line)
                if match:
                    pending.setdefault(match.group(1), match.group(2).strip())

    values = {}
    for _ in range(3):
        for name, text in pending.items():
            if name not in values:
                try:
                    values[name] = int(eval(text, {"__builtins__": {}}, values))
                except Exception:
                    pass
    return values


def read_species_data(species_name):
    with open("data/Species.c", encoding="utf-8") as source:
        text = source.read()
    start = text.find("[%s] = {" % species_name)
    if start < 0:
        raise SystemExit("%s is not in data/Species.c" % species_name)
    end = text.find("\n    [SPECIES_", start + 1)
    entry = text[start:end]

    stats = {}
    for field in ("hp", "attack", "defense", "spAttack", "spDefense", "speed"):
        stats[field] = int(re.search(r"\.%s = (\d+)" % field, entry).group(1))
    return {
        "stats": stats,
        "growth": re.search(r"\.expRate = (GROWTH_\w+)", entry).group(1),
        "ability": re.search(r"\.abilities = \{ (\w+)", entry).group(1),
    }


def exp_for_level(growth, level):
    n = level
    if n == 1:
        return 0
    if growth == "GROWTH_MEDIUM_FAST":
        return n ** 3
    if growth == "GROWTH_MEDIUM_SLOW":
        return int(1.2 * n ** 3 - 15 * n ** 2 + 100 * n - 140)
    if growth == "GROWTH_FAST":
        return 4 * n ** 3 // 5
    if growth == "GROWTH_SLOW":
        return 5 * n ** 3 // 4
    if growth == "GROWTH_ERRATIC":
        if n <= 50:
            return n ** 3 * (100 - n) // 50
        if n <= 68:
            return n ** 3 * (150 - n) // 100
        if n <= 98:
            return n ** 3 * ((1911 - 10 * n) // 3) // 500
        return n ** 3 * (160 - n) // 100
    if growth == "GROWTH_FLUCTUATING":
        if n <= 15:
            return n ** 3 * ((n + 1) // 3 + 24) // 50
        if n <= 36:
            return n ** 3 * (n + 14) // 50
        return n ** 3 * (n // 2 + 32) // 50
    raise SystemExit("Unknown growth rate %s" % growth)


def next_random(seed):
    return (seed * 0x41C64E6D + 0x6073) & 0xFFFFFFFF


def crypt(data, seed):
    out = bytearray(data)
    for offset in range(0, len(data), 2):
        seed = next_random(seed)
        struct.pack_into("<H", out, offset, struct.unpack_from("<H", data, offset)[0] ^ (seed >> 16))
    return bytes(out)


def checksum(blocks):
    return sum(struct.unpack("<64H", bytes(blocks))) & 0xFFFF


class Mon:
    # one party Pokemon, decrypted for editing; a and b are the offsets of substructs A and B
    def __init__(self, raw):
        self.pid, self.flags, self.stored_checksum = struct.unpack_from("<IHH", raw, 0)
        self.blocks = bytearray(crypt(raw[8:BOX_SIZE], self.stored_checksum))
        self.party = bytearray(crypt(raw[BOX_SIZE:MON_SIZE], self.pid))
        order = BLOCK_ORDERS[((self.pid & 0x3E000) >> 13) % 24]
        self.a = order.index("A") * BLOCK_SIZE
        self.b = order.index("B") * BLOCK_SIZE

    def valid(self):
        return self.pid != 0 and checksum(self.blocks) == self.stored_checksum

    def encode(self):
        check = checksum(self.blocks)
        header = struct.pack("<IHH", self.pid, self.flags, check)
        return header + crypt(bytes(self.blocks), check) + crypt(bytes(self.party), self.pid)

    def species(self):
        return struct.unpack_from("<H", self.blocks, self.a)[0]

    def item(self):
        return struct.unpack_from("<H", self.blocks, self.a + 2)[0]

    def moves(self):
        return struct.unpack_from("<4H", self.blocks, self.b)

    def status(self):
        return struct.unpack_from("<I", self.party, 0)[0]

    def level(self):
        return self.party[4]

    def hp(self):
        return struct.unpack_from("<HH", self.party, 6)

    def ivs(self):
        packed = struct.unpack_from("<I", self.blocks, self.b + 0x10)[0]
        return [(packed >> (5 * index)) & 31 for index in range(6)]

    def set_hp(self, hp, status):
        struct.pack_into("<H", self.party, 6, hp)
        struct.pack_into("<I", self.party, 0, status)

    def rebuild(self, species, level, item, moves, data, ability):
        struct.pack_into("<HH", self.blocks, self.a, species, item)
        exp_and_flags = struct.unpack_from("<I", self.blocks, self.a + 8)[0]
        exp_and_flags = (exp_and_flags & ~(EXP_MASK | ABILITY_MSB)) | exp_for_level(data["growth"], level)
        if ability > 0xFF:
            exp_and_flags |= ABILITY_MSB
        struct.pack_into("<I", self.blocks, self.a + 8, exp_and_flags)
        self.blocks[self.a + 0xD] = ability & 0xFF

        if moves:
            padded = (list(moves) + [0, 0, 0, 0])[:4]
            struct.pack_into("<4H", self.blocks, self.b, *padded)
            struct.pack_into("<4B", self.blocks, self.b + 8, *[20 if move else 0 for move in padded])

        # natures are ignored here; the game recalculates exactly on the next level up
        base = data["stats"]
        ivs = self.ivs()
        max_hp = (2 * base["hp"] + ivs[0]) * level // 100 + level + 10
        others = [(2 * base[field] + ivs[index]) * level // 100 + 5
                  for field, index in (("attack", 1), ("defense", 2), ("speed", 3), ("spAttack", 4), ("spDefense", 5))]
        struct.pack_into("<I", self.party, 0, 0)
        self.party[4] = level
        struct.pack_into("<HH5H", self.party, 6, max_hp, max_hp, *others)


def read_ram(emu):
    return bytes(emu.memory.unsigned[RAM_BASE:RAM_BASE + RAM_SIZE])


def write_ram(emu, offset, data):
    for index, value in enumerate(data):
        emu.memory.write_byte(RAM_BASE + offset + index, value)


def find_party(ram):
    for count in range(1, PARTY_SIZE + 1):
        pattern = struct.pack("<II", PARTY_SIZE, count)
        offset = ram.find(pattern)
        while offset >= 0:
            if offset % 4 == 0 and Mon(ram[offset + PARTY_HEADER_SIZE:offset + PARTY_HEADER_SIZE + MON_SIZE]).valid():
                return offset, count
            offset = ram.find(pattern, offset + 1)
    return None, 0


def read_party(ram):
    offset, count = find_party(ram)
    if offset is None:
        return None, []
    start = offset + PARTY_HEADER_SIZE
    return offset, [Mon(ram[start + index * MON_SIZE:start + (index + 1) * MON_SIZE]) for index in range(count)]


def read_stable_party(emu):
    # RAM can catch a Pokemon mid-update, so wait for a frame where every checksum passes
    for _ in range(STABLE_READ_FRAMES):
        offset, mons = read_party(read_ram(emu))
        if mons and all(mon.valid() for mon in mons):
            return offset, mons
        run(emu, 1)
    raise SystemExit("No valid party found. Is this state past getting the starter?")


def write_mon(emu, party_offset, slot, mon):
    write_ram(emu, party_offset + PARTY_HEADER_SIZE + slot * MON_SIZE, mon.encode())


def find_pocket(ram, constants, name):
    # Mom's two key items are the fixed landmark; the pockets sit in save order around them
    landmark = struct.pack("<HHHH", constants["ITEM_INFINITE_CANDY"], 1, constants["ITEM_POCKET_PKMN_CENTER"], 1)
    key_pocket = ram.find(landmark)
    if key_pocket < 0:
        raise SystemExit("Bag not found. Is this state past Mom's gift?")

    offset = key_pocket - POCKETS[0][1] * ITEM_SLOT_SIZE
    for pocket, slots in POCKETS:
        if pocket == name:
            return offset, slots
        offset += slots * ITEM_SLOT_SIZE
    raise SystemExit("Unknown pocket %s (one of: %s)" % (name, ", ".join(pocket for pocket, _ in POCKETS)))


def print_party(emu, constants):
    names = {}
    for name, value in constants.items():
        for prefix in ("SPECIES_", "ITEM_", "MOVE_"):
            if name.startswith(prefix):
                names.setdefault((prefix, value), name[len(prefix):])

    _, mons = read_stable_party(emu)
    for slot, mon in enumerate(mons):
        moves = [names.get(("MOVE_", move), str(move)) for move in mon.moves() if move]
        print("%d %-12s Lv.%-3d HP %d/%d status %d item %s moves %s" % (
            slot, names.get(("SPECIES_", mon.species()), mon.species()), mon.level(), mon.hp()[0], mon.hp()[1],
            mon.status(), names.get(("ITEM_", mon.item()), mon.item()), ", ".join(moves)))


def command_step(args):
    emu = open_emulator(args.rom, None if args.state == "-" else args.state)
    run_inputs(emu, args.inputs, args.out)
    emu.savestate.save_file(state_path(args.out))
    print(picture_path(args.out))


def command_new_game(args):
    emu = open_emulator(args.rom)
    for name, inputs in NEW_GAME_ROUTE:
        run_inputs(emu, inputs.split(), args.out + "_" + name)
    constants = read_constants()
    print_party(emu, constants)
    emu.savestate.save_file(state_path(args.out))
    print(state_path(args.out))


def command_party(args):
    emu = open_emulator(args.rom, args.state)
    print_party(emu, read_constants())


def command_team(args):
    if len(args.mon) > PARTY_SIZE:
        raise SystemExit("A party holds at most %d Pokemon" % PARTY_SIZE)

    constants = read_constants()
    emu = open_emulator(args.rom, args.state)
    party_offset, mons = read_stable_party(emu)
    template = mons[0].encode()

    for slot, text in enumerate(args.mon):
        fields = text.split(":")
        species_name = fields[0]
        level = int(fields[1])
        item = constants[fields[2]] if len(fields) > 2 and fields[2] else 0
        moves = [constants[move] for move in fields[3].split("+")] if len(fields) > 3 else None
        mon = Mon(template)
        data = read_species_data(species_name)
        mon.rebuild(constants[species_name], level, item, moves, data, constants[data["ability"]])
        write_mon(emu, party_offset, slot, mon)

    write_ram(emu, party_offset + 4, struct.pack("<I", len(args.mon)))
    print_party(emu, constants)
    emu.savestate.save_file(state_path(args.out))


def command_bag(args):
    constants = read_constants()
    emu = open_emulator(args.rom, args.state)
    for text in args.add:
        fields = text.split(":")
        item, quantity = constants[fields[0]], int(fields[1])
        pocket = fields[2] if len(fields) > 2 else "items"
        ram = read_ram(emu)
        offset, slots = find_pocket(ram, constants, pocket)
        for slot in range(slots):
            position = offset + slot * ITEM_SLOT_SIZE
            if ram[position:position + ITEM_SLOT_SIZE] == bytes(ITEM_SLOT_SIZE):
                write_ram(emu, position, struct.pack("<HH", item, quantity))
                print("%s x%d in %s slot %d" % (fields[0], quantity, pocket, slot))
                break
        else:
            raise SystemExit("Pocket %s is full" % pocket)
    emu.savestate.save_file(state_path(args.out))


def command_damage(args):
    emu = open_emulator(args.rom, args.state)
    party_offset, mons = read_stable_party(emu)
    if not 0 <= args.slot < len(mons):
        raise SystemExit("Slot must be 0 to %d" % (len(mons) - 1))
    mons[args.slot].set_hp(args.hp, args.status)
    write_mon(emu, party_offset, args.slot, mons[args.slot])
    print_party(emu, read_constants())
    emu.savestate.save_file(state_path(args.out))


def main():
    parser = argparse.ArgumentParser(description="Headless DeSmuME testing for test.nds")
    parser.add_argument("--rom", default="test.nds")
    commands = parser.add_subparsers(dest="command", required=True)

    step = commands.add_parser("step", help="load a state ('-' to boot), apply inputs, save a state and a picture")
    step.add_argument("state")
    step.add_argument("out")
    step.add_argument("inputs", nargs="*")
    step.set_defaults(handler=command_step)

    new_game = commands.add_parser("new-game", help="play from power-on to the overworld with a starter")
    new_game.add_argument("out")
    new_game.set_defaults(handler=command_new_game)

    party = commands.add_parser("party", help="print the party from a state")
    party.add_argument("state")
    party.set_defaults(handler=command_party)

    team = commands.add_parser("team", help="replace the party, built from slot 0")
    team.add_argument("state")
    team.add_argument("out")
    team.add_argument("--mon", action="append", required=True, help="SPECIES_X:LEVEL[:ITEM_Y[:MOVE_A+MOVE_B]]")
    team.set_defaults(handler=command_team)

    bag = commands.add_parser("bag", help="add items to the bag")
    bag.add_argument("state")
    bag.add_argument("out")
    bag.add_argument("--add", action="append", required=True, help="ITEM_X:QUANTITY[:POCKET]")
    bag.set_defaults(handler=command_bag)

    damage = commands.add_parser("damage", help="set a party member's HP and status")
    damage.add_argument("state")
    damage.add_argument("out")
    damage.add_argument("slot", type=int)
    damage.add_argument("hp", type=int)
    damage.add_argument("--status", type=int, default=0, help="8 is poison")
    damage.set_defaults(handler=command_damage)

    args = parser.parse_args()
    os.makedirs(STATE_DIR, exist_ok=True)
    args.handler(args)


if __name__ == "__main__":
    main()
