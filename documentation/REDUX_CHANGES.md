# Pokémon HeartGold Redux: changes from hg-engine

Pokémon HeartGold Redux is a fork of [BluRosie/hg-engine](https://github.com/BluRosie/hg-engine).
This file lists every change Redux makes on top of upstream, the design rules behind them,
and the work still planned. Keep it up to date in the same commit as each change.

## Design rules

- **Roster:** all 493 Pokémon from Gens 1–4, plus later evolutions of normal Gen 1–4 Pokémon
  (Sylveon, Wyrdeer, Kleavor, Ursaluna, Annihilape, Farigiraf, Dudunsparce). No regional forms
  (see [Regional forms](#regional-forms-excluded)) and no other Gen 5–9 species in encounters,
  trainer teams, gifts or shops.
- **Stats:** modern official base stats (hg-engine default). No custom stat changes.
- **Types:** official typings, except 8 final evolutions retyped to their Mega typings (see below).
- **Story:** vanilla cutscenes only. New NPCs, rematches and post-game battles are fine.
- **Difficulty:** harder than vanilla, not a challenge-run hack. One build, no level caps.
- **When unsure:** use hg-engine's existing code and defaults. Follow HeartGold Generations
  ([spearmintz1/hg-engine](https://github.com/spearmintz1/hg-engine)) for implementation and
  Drayano's Sacred Gold for design (trainer teams, level curve).
- **Stability first:** the project has one developer and no automated in-game testing.
  Anything experimental or known to be buggy stays off.

## Building and checking

- Building needs a clean US HeartGold ROM as `rom.nds`, which is not in the repo. The developer
  builds locally.
- Without the ROM, C changes can be compile-checked with `arm-none-eabi-gcc -fsyntax-only` and
  the project `CFLAGS` from the `Makefile`. Generate `include/constants/generated/learnsets.h`
  first (see Learnsets).

## Changes

### Settings (`include/config.h`, `armips/include/config.s`, `header.yaml`, `banner.yaml`)

| Setting | Value | Why |
|---|---|---|
| ROM title and banner | "HG REDUX" / "Pokemon HeartGold Redux" | Hack name |
| `MEGA_EVOLUTIONS`, `PRIMAL_REVERSION` | Off | Replaced by permanent retypes |
| `IMPLEMENT_BDHCAM_ROUTINE` | Off | Keep vanilla camera behaviour |
| `SHINY_ODDS` | 32 (1 in 2048) | Matches HeartGold Generations |
| `DELETABLE_HMS` | On | HMs can be forgotten |
| `FAST_TEXT_PRINTING`, `ALWAYS_HAVE_NATIONAL_DEX` | On | QoL; National Dex from the start |
| Transparent text boxes, level cap, 60 fps, wild double battles | Off (upstream default) | Not wanted, or unstable |
| `ALLOW_SAVE_CHANGES` | On (upstream default) | Required for the expanded Pokédex. Saves aren't PKHeX-compatible. The armips side uses `.ifdef`, so its `0` value still means on |

### Title screen logo (`rawdata/title_demo/`, `data/graphics/title/redux_logo.png`)

The title screen shows "REDUX" in place of "VERSION" under the HeartGold logo, following the layout of HeartGold Generations.
"REDUX" is original pixel art; the rest of the logo is the vanilla art, and it uses the vanilla palette, so there are no
code changes. The logo is one tile row taller than vanilla (16 rows, 32 KB), which is the most that fits before its tilemap in VRAM.

- `narcs.mk`, `Makefile`: `a/0/4/6` gets the same `rawdata` override rule as `a/2/6/2`
- `rawdata/title_demo/6_03`, `6_00`: the logo's tiles and tilemap. To change the logo, edit the PNG, then run
  `python3 scripts/build_title_logo.py` to regenerate them

### Types (`data/Species.c`)

Final stage only; pre-evolutions keep their types.

| Pokémon | Type |
|---|---|
| Meganium | Grass/Fairy |
| Feraligatr | Water/Dragon |
| Ampharos | Electric/Dragon |
| Sceptile | Grass/Dragon |
| Lopunny | Normal/Fighting |
| Chimecho | Psychic/Steel |
| Altaria | Dragon/Fairy |
| Staraptor | Fighting/Flying |

The Pokédex search-by-type lists in `data/PokedexSort.c` are updated to match: Feraligatr, Ampharos and Sceptile are
under Dragon, Lopunny and Staraptor under Fighting, and Chimecho under Steel. Altaria is no longer under Flying and Staraptor
no longer under Normal. The Pokédex has no Fairy search list; upstream never added one, so Fairy types are listed under
their other type or their pre-Fairy type, as in vanilla.

### Learnsets (`data/learnsets/`)

`data/learnsets/learnsets.json` is generated, not hand-edited. Regenerate it with:

```bash
python3 scripts/build_learnsets.py --generate data/learnsets/learnsets.json --cutoff custom --inherit-level --inherit-egg --inherit-machine --inherit-tutor --ignore-files 20_la.json 99_go.json
```

- Level-up and egg moves come from the newest game with data for each species
  (Legends Z-A, then Scarlet/Violet, then older games). The 8 retyped Pokémon get moves of
  their new type from Z-A, e.g. Meganium learns Disarming Voice at level 9.
- TM and tutor compatibility is the union of every game.
- Legends: Arceus and Pokémon GO are ignored. Every Redux species has mainline data.
- `data/learnsets/base/custom.json` applies last. It removes level-up moves hg-engine has not
  implemented (the engine blocks learning them anyway) and replaces Rage Fist with Shadow Punch
  for Primeape and Annihilape. To change one learnset, edit its entry there and rerun the command.

To compile-check without a ROM, generate the header with:

```bash
python3 scripts/build_learnsets.py --learnsets data/learnsets/learnsets.json --machineout build/learnset/MachineMoveLearnsets.c --levelupout build/learnset/LevelupLearnsets.c --eggout build/learnset/EggLearnsets.c --tutorout build/learnset/TutorMoveLearnsets.c --constsout
```

### Evolutions (`data/Evolutions.c`, `data/itemdata/itemdata.c`)

The original methods are kept; Redux adds alternatives or replaces broken ones.

| Change | Species |
|---|---|
| Pure trade evolutions also evolve at **level 36** (Definitive HeartGold's level) | Kadabra, Machoke, Graveler, Haunter |
| Trade-with-item evolutions also evolve by **using the item** from the bag | Poliwhirl and Slowpoke (King's Rock), Onix and Scyther (Metal Coat), Rhydon (Protector), Seadra (Dragon Scale), Electabuzz (Electirizer), Magmar (Magmarizer), Porygon (Up-Grade), Porygon2 (Dubious Disc), Feebas (Prism Scale), Dusclops (Reaper Cloth), Clamperl (Deep Sea Tooth/Scale) |
| Hold-item-and-level evolutions also evolve by **using the item** (no day/night requirement) | Gligar (Razor Fang), Sneasel (Razor Claw), Ursaring (Peat Block), Happiny (Oval Stone) |
| Upstream bug: `EVO_FORM_ARGUMENT` is never evaluated, so these could not evolve. Replaced with **level 35** | Primeape → Annihilape, Stantler → Wyrdeer |

`src/individual/GetMonEvolutionInternal.c` keeps the Gen 4 quirk that an Everstone doesn't stop Kadabra's
*trade* evolution, but no longer applies it to other evolutions, so an Everstone still stops Kadabra's level-36 evolution.

To make the items usable, they're marked usable on party Pokémon in `itemdata.c`
(`fieldUseFunc = 20`, `partyUse = 1`, `evolve = TRUE`), the same settings upstream uses for
Linking Cord and Peat Block. Their held-item battle effects are unchanged.

### Shops (`src/field/mart.c`) and prices (`data/itemdata/itemdata.c`)

Shops use hg-engine's `MART_EXPANSION` lists, wired in through `repoints`. The layout follows
HeartGold Generations.

| Shop | Added items |
|---|---|
| Every Poké Mart (badge-gated) | Max Ether (3 badges), Elixir (5), Max Elixir (7), Max Revive (8) |
| Goldenrod and Celadon Dept. Store 2F, medicine clerk | PP Up, Ability Capsule, Ability Patch, all 21 Nature Mints |
| Goldenrod Dept. Store 3F | King's Rock, Metal Coat, Dragon Scale, Up-Grade, Dubious Disc, Protector, Electirizer, Magmarizer, Reaper Cloth, Prism Scale, Deep Sea Tooth/Scale, Razor Fang, Razor Claw, Oval Stone |
| Goldenrod Dept. Store 5F | Fire, Water, Thunder, Leaf, Moon, Sun and Ice Stones |
| Celadon Dept. Store 3F | Shiny, Dusk and Dawn Stones, Black Augurite (Kleavor), Peat Block (Ursaluna) |

Redux prices (selling to a shop gives half):

| Items | Price |
|---|---|
| Nature Mints | ₽1,000 |
| Ability Capsule, Ability Patch | ₽2,000 |
| All evolution items and stones listed above | ₽1,000 |

### Infinite items

Two custom item IDs follow the last hg-engine item (Canari Bread, 2684). Both are Key Items
and can't be tossed or sold.

| Item | ID | How it works |
|---|---|---|
| Infinite Candy | 2685 (`ITEM_INFINITE_CANDY`) | Same item data as Rare Candy (HeartGold Generations' setup). Use it on a Pokémon from the bag; it's never used up and can be reused in a row. Works for level-100 evolutions like Rare Candy |
| Pocket Center | 2686 (`ITEM_POCKET_PKMN_CENTER`) | Use it from the bag, or register it to the Y button. Either way it runs common script 2074, which plays the heal jingle, heals the whole party (`heal_party`, the Pokémon Center command) and prints a message. Outside battle only |

Files involved:

- `include/constants/item.h`: IDs, `MAX_TOTAL_ITEM_NUM` and `IS_ITEM_INFINITE`
- `data/itemdata/itemdata.c`: item data (copied from Rare Candy and GB Sounds)
- `src/item.c`: field use function 36. `ItemMenuUseFunc_PocketPkmnCenter` handles the bag: it closes the bag and runs the
  script through the start menu's exit task, like pokeheartgold's `StartScriptFromMenu`.
  `ItemFieldUseFunc_PocketPkmnCenter` handles the Y button.
- `rom.ld`, `include/script.h`: `Task_RunScripts`, `ScriptEnvironment_New`, `SetupScriptEngine`. The addresses come from
  KalaayPT/G4Patcher's `QoLItems_HG_SS.asm`; they match hg-engine's existing `EventSet_Script` and
  `FieldSystem_LoadFieldOverlay`, and the function order in pokeheartgold's `script_manager.c`
- `src/bag.c`: `Bag_TakeItem` never removes infinite items
- `src/individual/GetMonEvolutionInternal.c`, `src/pokemon.c`: Infinite Candy gets Rare Candy's special cases
- `data/scr_seq/scr_seq_00003_commonscript.s`: script 2074 (Pocket Center), script 2038 (Mom's handoff, below),
  and 2075 (gives both items directly, for debugging)
- `data/text/040.txt` lines 121–122 (script messages); `222.txt` (names); `221`/`223`/`224`/`829.txt` (custom item descriptions and name forms)
- `data/graphics/itemgra.mk`: icons reuse `rare_candy.png` and `full_restore.png`. The dummy and return icons
  moved to 2689/2690 to stay right after the last item

**Mom gives the items.** Mom's opening scene in New Bark Town ends with `callstd 2038`
(`std_fade_end_mom_music`). Vanilla shares that script's body with five other shared scripts, so Redux gives 2038 its own
entry point. If the player doesn't have the Pocket Center yet, Mom says one extra line and gives both items with the
usual "obtained" fanfare (the vanilla give-item routine `_080A`); then the music fades as before. Her scene is the first
script that calls 2038, and the item check makes it a one-time gift, so no new flag or map script edit is needed.

### Regional forms (excluded)

Redux has no regional forms: they add complexity and don't fit the feel of HeartGold. hg-engine keeps their species
data, but nothing in Redux places them. Upstream's wild encounters, trainers, Safari Zone, Headbutt trees, shops and
scripts don't use them, and no normal Gen 1–4 Pokémon can evolve into one, so they can't appear in a playthrough.
Keep it that way when adding encounters, trainers, gifts, trades and eggs.

| Region | Forms |
|---|---|
| Alolan | Rattata, Raticate, Raichu, Sandshrew, Sandslash, Vulpix, Ninetales, Diglett, Dugtrio, Meowth, Persian, Geodude, Graveler, Golem, Grimer, Muk, Exeggutor, Marowak |
| Galarian | Meowth, Ponyta, Rapidash, Slowpoke, Slowbro, Slowking, Farfetch'd, Weezing, Mr. Mime, Articuno, Zapdos, Moltres, Corsola, Zigzagoon, Linoone |
| Hisuian | Growlithe, Arcanine, Voltorb, Electrode, Typhlosion, Qwilfish, Sneasel |
| Paldean | Wooper, Tauros (Combat, Blaze and Aqua Breeds) |

These later evolutions only come from a regional form, so they're excluded too: **Perrserker** (Galarian Meowth),
**Sirfetch'd** (Galarian Farfetch'd), **Mr. Rime** (Galarian Mr. Mime), **Cursola** (Galarian Corsola), **Obstagoon**
(Galarian Linoone), **Overqwil** (Hisuian Qwilfish), **Sneasler** (Hisuian Sneasel) and **Clodsire** (Paldean Wooper).

Regional forms of Gen 5+ Pokémon (e.g. Galarian Darumaka, Hisuian Zorua) were never in scope. Ursaluna's Bloodmoon form
isn't a regional form, but it's also left out: it can't be reached by evolution.

## Dropped

- **PC anywhere** (L button, from HeartGold Generations): it hooks overworld input and uses an arbitrary game flag. Not worth the risk.

## Planned, not started

- **Roster restriction:** remove Gen 5–9 species from the Pokédex order and keep them, and the regional forms and their
  evolutions listed under [Regional forms](#regional-forms-excluded), out of encounters and trainers.
- **Wild encounters:** place all roster Pokémon at reasonable points; post-game sanctuaries.
- **Trainers:** rebuild teams and level curve along Sacred Gold's lines.
- **Faster egg hatching:** halve every species' `hatchCycles` in `data/Species.c`.
- **Move tutors and Move Relearner:** free. Tutor costs in `src/field/move_tutor.c`, plus script edits.
- **Flash and HM obstacles:** light Dark Cave and Rock Tunnel; remove HM obstacles that don't gate progress.
- **Legendaries and mythicals:** NPCs give the Enigma Stone and Red Orb; make Arceus and Celebi obtainable
  so the vanilla Sinjoh and Ilex events run; post-game encounters or gifts for Pokémon HeartGold lacks.
- **Extra NPCs and battles:** Gym Leader and Elite Four rematches, Kanto Gym Leader boss rush,
  Coach Trainers giving TMs, Kurt making balls instantly, fewer phone calls.
