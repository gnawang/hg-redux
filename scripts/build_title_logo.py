#!/usr/bin/env python3
# Converts data/graphics/title/encore_logo.png into the title screen files in rawdata/title_demo/.
# The PNG is 256x128 and indexed against the vanilla logo palette (a/0/4/6 file 4), which the
# game keeps using, so edits have to stay on those colours. Index 0 is transparent.
#
# Run it by hand after editing the PNG:
#   python3 scripts/build_title_logo.py
import struct

from PIL import Image

SOURCE = "data/graphics/title/encore_logo.png"
OUTPUT_DIR = "rawdata/title_demo"
TILE_SIZE = 8
WIDTH_TILES = 32
HEIGHT_TILES = 16
# the logo starts 5 tile rows down the top screen, as in vanilla
FIRST_MAP_ROW = 5
MAP_ROWS = 32
GX_TEXFMT_PLTT256 = 4
NSCR_256_COLOURS = 1


def build_ncgr(pixels):
    tiles = bytearray()
    for tile_y in range(HEIGHT_TILES):
        for tile_x in range(WIDTH_TILES):
            for y in range(TILE_SIZE):
                start = (tile_y * TILE_SIZE + y) * WIDTH_TILES * TILE_SIZE + tile_x * TILE_SIZE
                tiles += pixels[start:start + TILE_SIZE]

    char_block = b"RAHC" + struct.pack("<IHHIIIII", 0x20 + len(tiles), HEIGHT_TILES, WIDTH_TILES, GX_TEXFMT_PLTT256, 0, 0, len(tiles), 0x18) + tiles
    pos_block = b"SOPC" + struct.pack("<IIHH", 0x10, 0, WIDTH_TILES, HEIGHT_TILES)
    return b"RGCN\xff\xfe\x01\x01" + struct.pack("<IHH", 0x10 + len(char_block) + len(pos_block), 0x10, 2) + char_block + pos_block


def build_nscr():
    entries = [0] * (WIDTH_TILES * MAP_ROWS)
    for tile in range(WIDTH_TILES * HEIGHT_TILES):
        entries[FIRST_MAP_ROW * WIDTH_TILES + tile] = tile

    data = struct.pack("<%dH" % len(entries), *entries)
    scrn_block = b"NRCS" + struct.pack("<IHHII", 0x14 + len(data), 256, 256, NSCR_256_COLOURS, len(data)) + data
    return b"RCSN\xff\xfe\x00\x01" + struct.pack("<IHH", 0x10 + len(scrn_block), 0x10, 1) + scrn_block


def main():
    image = Image.open(SOURCE)
    expected = (WIDTH_TILES * TILE_SIZE, HEIGHT_TILES * TILE_SIZE)
    if image.mode != "P" or image.size != expected:
        raise SystemExit("%s must be an indexed %dx%d PNG" % (SOURCE, *expected))

    # names match what tools/narcpy.py extracts from a/0/4/6
    with open("%s/6_03" % OUTPUT_DIR, "wb") as out:
        out.write(build_ncgr(image.tobytes()))
    with open("%s/6_00" % OUTPUT_DIR, "wb") as out:
        out.write(build_nscr())


if __name__ == "__main__":
    main()
