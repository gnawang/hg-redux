# Pokémon HeartGold Redux

This repo is Pokémon HeartGold Redux, a fork of hg-engine. Before making changes, read
`documentation/REDUX_CHANGES.md`. It lists every change from upstream, the design rules,
and the work still planned.

- Record each change in `documentation/REDUX_CHANGES.md` in the same commit.
- Prefer hg-engine's existing code and config toggles over new code. Keep experimental or
  unstable features off.
- Test changes in the real game when a ROM is available (see below). The developer's own
  playtesting is still the final check.
- The ROM (`rom.nds`) is not in the repo, so a full `make` isn't possible in cloud sessions.
  Compile-check C changes with `arm-none-eabi-gcc -fsyntax-only` and the `Makefile` `CFLAGS`.
- After changing encounters, trainers, Pokémon or learnsets, run `.venv/bin/python scripts/build_reference_docs.py`
  and commit `documentation/reference/`. Those pages are generated, so don't edit them by hand. The script needs a built
  repo (`base/`) and the `upstream` remote fetched. `gift_static.md` is the exception: it's hand-written from the event
  scripts, so update it yourself when scripts or legendaries change.
- Pushing changed reference pages to `main` republishes the reference site through `.github/workflows/reference-site.yml`.
- After changing wild encounters, run `python3 scripts/build_dex_areas.py` too, which updates `data/PokedexArea.c`.
- Map objects and warps are built from `data/eventdata/zone_event/`, which holds only the maps Redux changes (`BUILD_DUMPED_EVENTDATA` is on). To hide an object
  without changing script object IDs, set its `hidden_flag` to `FLAG_GOT_BAG`, which is set in the opening and never cleared. Don't delete it from the list.
  Some outdoor maps, such as Route 47, stack levels on the same tiles, so collision data alone doesn't prove a new object is reachable. Check it in the emulator.
- `data/learnsets/learnsets.json` is generated. Change learnsets through
  `data/learnsets/base/custom.json` and regenerate it with the command in the changes file.

## Building

Follow the README, then run `make`, which writes `test.nds`. Problems seen on macOS on Apple Silicon:

- `base/` keeps files from earlier builds. If a build shows changes that aren't in the repo, such as a reverted map edit, restore that file from `rom.nds`.
- Clone with `--recursive`, or run `git submodule update --init`, or `make` stops at `tools/nitrogfx`.
- Make paths with spaces can fail. Build through a symlink to the repo from a path without spaces.
- A `pyexpat` symbol error from `pip` or `venv` means Homebrew's Python doesn't match the macOS libexpat.
  Install a standalone Python (`uv python install 3.12`) and put a `python3` link to it first on `PATH`
  before the first `make`, which creates `.venv`.
- `brew install --cask gcc-arm-embedded` runs a system installer. If that isn't possible, the same toolchain
  is available as a tarball from Arm that works when added to `PATH`.

## Testing in the emulator

`scripts/emu_test.py` plays `test.nds` headlessly in DeSmuME through `py-desmume`, which is in
`requirements.txt`. Savestates and pictures go in `.scratch/emu/`, which is ignored. Never commit them;
they contain game data. Run it from the repo root with `.venv/bin/python scripts/emu_test.py`.

```bash
.venv/bin/python scripts/emu_test.py new-game start
.venv/bin/python scripts/emu_test.py team start t1 --mon SPECIES_POLIWHIRL:30 --mon SPECIES_ALTARIA:40::MOVE_MOONBLAST+MOVE_DRAGON_PULSE
.venv/bin/python scripts/emu_test.py bag t1 t2 --add ITEM_KINGS_ROCK:1
.venv/bin/python scripts/emu_test.py damage t2 t3 1 1 --status 8
.venv/bin/python scripts/emu_test.py step t3 t4 t:43:115 w150 snap t:62:56 w90
.venv/bin/python scripts/emu_test.py party t4
```

| Command | What it does |
|---|---|
| `new-game OUT` | Plays from power-on to the overworld in Elm's Lab with Totodile, Mom's items in the bag. Takes about a minute. Check `OUT_mom.png`, `OUT_lab.png` and `OUT_starter.png` if it fails |
| `team IN OUT --mon SPECIES:LEVEL[:ITEM[:MOVE+MOVE]]` | Replaces the party, with correct EXP, ability and HP for the species. Leave the item empty with `::` to give moves only |
| `bag IN OUT --add ITEM:QTY[:POCKET]` | Adds items. Pockets: items (default), key, tms, mail, medicine, berries, balls, battle. The game doesn't check pockets for you, so use the item's real one (`fieldPocket` in `data/itemdata/itemdata.c`). Ability Capsules, Ability Patches and Mints are in medicine |
| `damage IN OUT SLOT HP [--status 8]` | Sets HP and status (8 is poison) |
| `party STATE` | Prints species, level, HP, status, ability, item and moves |
| `step IN OUT INPUTS...` | Loads a state (`-` boots the ROM), applies inputs, saves `OUT.ds` and `OUT.png` |

Inputs for `step`:

| Input | Meaning |
|---|---|
| `a`, `b`, `x`, `y`, `l`, `r`, `start`, `select`, `up`, `down`, `left`, `right` | Tap the button |
| `a%6` | Tap 6 times. It's `%` because a shell would expand `*` |
| `left:48` | Hold for 48 frames. Walking takes 16 frames per tile |
| `w120` | Wait 120 frames (60 frames is one second) |
| `t:43:115` | Touch the bottom screen |
| `snap` | Add a frame to the picture. The final frame is always added |

### Working cheaply

Every picture costs tokens, so use the fewest that prove the result.

- Prove results with `party` where you can: numbers are exact and cost little. Use pictures for what
  only the screen shows, such as types, text and graphics.
- Don't play to late-game content. Build the situation with `new-game`, `team` and `bag`. To check
  that a change works, one Pokémon per code path is enough, not every affected species.
- Keep `start` and branch from it. Save a state before anything risky, and reload it after a mistake.
- Batch inputs and `snap` before each risky press. Decide the next input from the picture, not a guess.
- If a route needs map positions, read them from pret/pokeheartgold's
  `files/fielddata/eventdata/zone_event/` instead of exploring.
- Rerun `new-game` after changing code or scripts it passes through. States from an older ROM are
  safe only for text or data changes.

### What the screen and game do

- Pictures show the top screen above the bottom screen. For `t:` subtract 192 from the picture's Y.
- Touch positions, as `t:X:Y`:

| Screen | Positions |
|---|---|
| Field menu | POKéMON 43:75, BAG 43:115 (the menu is always on the bottom screen) |
| Bag | Slots 62:56 and 190:56, then rows 104 and 152 lower down in the same columns |
| Bag item menu | USE 48:144, REGISTER 158:144, CANCEL 222:176 |
| Party list | Slots 60:36, 190:45, 60:84, 190:93, 60:132, 190:141 |

- The camera follows the player, so the player stays at screen centre and the map moves. Compare the
  map between pictures to see if the player moved. Red mats are warps.
- The bag reopens on the last pocket. Change pockets with `r:20` or `l:20`; the D-pad doesn't change them.
- The summary opens on the last tab. Species and types are on the **bottom** screen of the blue tab.
- A level-up takes three A presses: the message, the stat gains, the stat totals. A fourth A with the
  cursor still on the Pokémon uses the item again, so a Rare Candy test can overshoot.
- Inputs are ignored during fades. Evolutions take about 1,500 frames, and more if a move is learned,
  and input sent early lands on the wrong screen. Allow for this and check with `party` afterwards.
- A Mint doesn't change the nature named on the summary's memo tab, as in mainline games. Check the
  red and blue stat names on the skills tab, and the stats themselves.
- Item fanfares lock input for several hundred frames. Wait longer before calling it a hang.
- Runs aren't identical, because the game seeds from the clock: PID, stats and NPC walks vary.
  `new-game` has been reliable, but an NPC could block it. Rerun it once before debugging it.

### Limits

- `team` copies slot 0 for every Pokémon, so they share a PID, IVs and nature. Non-HP stats ignore
  nature until the next level up. Don't use it to check exact stats.
- Open only one emulator per process. A second `DeSmuME()` crashes with no error, so scripts that read
  several states need one process each.
- Reading RAM can catch a Pokémon mid-update. `party`, `team` and `damage` wait for valid checksums; custom
  scripts must do the same (`read_stable_party`).
- After a wild battle, `party` can read the opponent's leftover party instead of yours, until the game overwrites it.
- `team` and `bag` find their data from the party and Mom's two key items, and `bag` assumes
  `ITEM_POCKET_EXPANSION` is on. Update `POCKETS` in the script if bag sizes change.
- Passing here means it works in DeSmuME. It doesn't prove real hardware or a saved and reloaded game.
- To test a saved game, save from the in-game menu, wait about 2,400 frames for "Saving a lot of data" to finish,
  then call `emu.reset()` in the same process and pick Continue. In-game saves go to `~/.config/desmume/test.dsv`
  and outlast the run, so delete that file before and after.
- Battle behaviour needs a real battle in the emulator or `scripts/run_tests.py`.
