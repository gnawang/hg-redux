# Pokémon HeartGold Redux: changes from hg-engine

Pokémon HeartGold Redux is a fork of [BluRosie/hg-engine](https://github.com/BluRosie/hg-engine).
This file lists every change Redux makes on top of upstream, the design rules behind them,
and the work still planned. Keep it up to date in the same commit as each change.

For what's in the game now (wild encounters, every Pokémon, key trainers' teams), see
[the reference pages](reference/README.md).

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
- **Stability first:** the project has one developer and only light in-game testing.
  Anything experimental or known to be buggy stays off.

## Building and checking

- Building needs a clean US HeartGold ROM as `rom.nds`, which is not in the repo. The developer
  builds locally.
- Without the ROM, C changes can be compile-checked with `arm-none-eabi-gcc -fsyntax-only` and
  the project `CFLAGS` from the `Makefile`. Generate `include/constants/generated/learnsets.h`
  first (see Learnsets).
- With a built `test.nds`, `scripts/emu_test.py` plays the game headlessly in DeSmuME and can build test
  teams and bags from savestates. `AGENTS.md` covers its use and the agent instructions. `CLAUDE.md` only
  imports `AGENTS.md`, because Claude Code doesn't read `AGENTS.md` by itself.

## What hg-engine already changes from HeartGold

The rest of this file lists changes from hg-engine. These come with hg-engine and stay on in Redux (see `include/config.h`):

- **Pokémon and battles:** Fairy type and the latest type chart, modern base stats, moves and abilities, hidden abilities, the expanded species list, and Champions power, type, accuracy and effect-chance changes.
- **Catching and growth:** capture experience, critical captures, modern Poké Ball logic, the modern experience formula and vitamin EV caps.
- **Field and items:** reusable TMs, a prompt to use another repel, an EV/IV viewer, expanded bag pockets and PC boxes, and editable shop lists. Poison does no damage in the overworld.

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
| `BUILD_DUMPED_EVENTDATA` | On | Map objects Redux changes come from `data/eventdata/zone_event/`. Only maps in that folder replace the ROM's |
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

### Pokédex (`data/PokedexSort.c`, `data/PokedexArea.c`, `armips/asm/pokedex.s`, `scripts/build_dex_areas.py`)

The National list and every search list hold only the Redux roster of 500 Pokémon: Gens 1–4 and the seven later evolutions. Upstream had those seven only in the National list, so
they're added to the name, height, weight, type and body lists, and Sylveon is listed under Normal. Kyogre, Giratina and Shaymin, missing from upstream's height lists, are added too.

The seven later evolutions are numbered 494 to 500 in roster order, straight after Arceus, instead of their official numbers, so the National grid ends at 500 with no blank run. The numbers come from
one lookup, `redux_dex_species` in `armips/asm/pokedex.s`, which the grid, entry page and summary screen all use. Keep it in the same order as the end of `sPokedexSort_NationalNum`. Their entries in `data/Species.c` are
trimmed where a long line stopped the text from wrapping: Ursaluna, Annihilape, Farigiraf and Dudunsparce. Dudunsparce shows as "Dudunspars" because names are capped at 10 characters.

The area maps' time-of-day lists are generated from `data/Encounters.c` by `scripts/build_dex_areas.py`. Swarm and radio Pokémon go in the Special lists, which
otherwise keep their vanilla Headbutt areas, and Safari Zone entries are kept.

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

`custom.json` also holds a learnset pass over the roster, which adds moves or moves them earlier and removes nothing. Every added move is one the Pokémon or its
pre-evolutions officially get in a mainline game, by level-up, TM, tutor or egg. The exceptions, all asked for by name, are Icicle Crash on Mamoswine and Piloswine, Spore on Breloom, and Moonblast on Meganium.

- Defining moves that the official learnsets give too late or only by TM, tutor or egg.
- Polished Crystal's level-up moves, where the Pokémon officially gets them: strong same-type attacks, coverage for the better attacking stat, and useful recovery or status
  moves. Up to 4 per Pokémon, level 56 or earlier.
- A move from the Pokémon's own TM, tutor or egg pool where it has no 55+ power same-type move by level 30, or, for a final evolution, no 75+ one by level 44.
- Final-stage Pokémon were checked type by type for a usable STAB move, and clearly helpful egg, tutor or TM moves were added to level-up, such as Earthquake on
  Steelix, Roost on Dragonite and Surf on Empoleon. All are official except Moonblast on Meganium, which suits its Fairy retype.
- Dual Wingbeat is added to winged physical attackers short on physical Flying moves: Charizard, Pidgeot, Aerodactyl, Dragonite, Crobat, Ninjask, Salamence, Mothim,
  Vespiquen and Gliscor.
- Extreme Speed keeps its official placement, except that Linoone learns it at level 52, from its official egg move. Strong setup moves such as Dragon Dance and Swords Dance stay at their official level, or at level 50 or later if they aren't
  officially learned by level-up.

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
| Upstream bug: `EVO_FORM_ARGUMENT` is never evaluated, so these could not evolve. Replaced with **level 36** | Primeape → Annihilape, Stantler → Wyrdeer |

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
- `data/scr_seq/scr_seq_00003_commonscript.s`: script 2074 (Pocket Center) and script 2038 (Mom's handoff, below)
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

### Wild encounters (`data/Encounters.c`)

Grass, cave, water, Rock Smash, swarm and radio-sound encounters follow Drayano's
[Sacred Gold wild Pokémon list](https://drayano.wordpress.com/sgss/sgss-wp/) in the 116 areas that list covers. Where a
listed rate can't be made from the game's slots (for example 7% on a water table), the closest fit is used. Land levels are spread across
the listed range. Water and rod levels keep upstream's values except in slots that were empty. Headbutt trees, the Safari Zone,
the Bug-Catching Contest, Cerulean Cave and Mt. Silver are unchanged, and Bell Tower uses Storm Silver's levels because the list gives none for
Sacred Gold. Gifts and static encounters from Sacred Gold aren't added. Roster Pokémon the list leaves out come from [the Collector](reference/gift_static.md).

### Trainers (`data/Trainers.c`)

Key trainers are rebuilt with team design drawn equally from Sacred Gold, Crystal Legacy and Polished Crystal, on top of vanilla rosters.
Levels follow Sacred Gold's curve, matching Redux's wild levels. This covers all 16 Gym Leaders, the first-round Elite Four, Lance, Red, Giovanni,
the Rocket Executives and Silver's fights from Azalea on, except the Cherrygrove and Dragon's Den ones. The full teams are on the [trainer](reference/trainers.md) page.

- Team size starts from vanilla. Early bosses gain one or two Pokémon, the Johto Gyms use 3 to 5, and 6-Pokémon teams start with Lance's
  league fight and the Kanto Gyms. The Elite Four keep 5.
- Silver grows a set team: Teddiursa, then Ursaring, then Ursaluna, and Larvitar through Tyranitar. From the Burned Tower on, his other slots change to
  cover his starter's weaknesses.
- Red keeps his vanilla HeartGold movesets on Sacred Gold's levels, including the three ultimate starter moves.
- Proton's ace is the Zubat line and Petrel's is Weezing; neither uses the other's line.
- Fighting Dojo rematches, the League second round, the tag battles, Kimono Girls and Eusine use Redux's own teams, set by each trainer's theme and place in the
  story. Levels for the Dojo and second round follow Sacred Gold's range.
- Bug Catcher Wade's first two rematches are swapped, because the rematch table calls them in reverse order.

Generic trainers are generated from rules, using Sacred Gold as a reference rather than a template:

- Levels are Sacred Gold's for that fight, with the ace at the top and the rest one lower.
- Team size is Polished Crystal's for the same-named trainer, raised to vanilla's size if Sacred Gold's team is at least that big. It's capped at 3 below level 15,
  4 below 32, 5 below 60 and 6 after.
- Species favour the class's type, then Pokémon on that route, then Johto species. Vanilla's strongest Pokémon stays as the ace.
- Gen 3 and 4 Pokémon appear only where Sacred Gold used them or they live on the route, and fill at most half a team.
- Rematches keep the same lines, evolved for the level. Moves come from level-up learnsets and generic trainers hold no items.

### Egg hatching and evolution friendship (`data/Species.c`, `include/config.h`)

- Every species' `hatchCycles` is halved, rounded down.
- `FRIENDSHIP_EVOLUTION_THRESHOLD` is 80, half of hg-engine's 160 (vanilla is 220). It applies to all friendship evolutions and to
  Sylveon. Pokémon that start above it, such as hatched Pokémon (120) and Chansey (140), evolve on their next level-up.

### Move Tutors and Move Relearner (`src/field/move_tutor.c`, `data/scr_seq/scr_seq_0948_T30R0601.s`, `data/text/635.txt`)

- Every tutor move costs 0 BP. The shared tutor script needs no edit, because a price of 0 passes its BP check.
- The Move Maniac in Blackthorn no longer asks for or takes a Heart Scale, and his lines are updated. His script is the vanilla dump with those
  checks removed. `BUILD_DUMPED_SCR_SEQ` is on so it gets built; only scripts present in `data/scr_seq/` replace the ROM's.

### Flash (`bytereplacement`)

Dark Cave and Rock Tunnel are lit. Each map's weather byte in the arm9 map header table is changed from `WEATHER_FLASH` to none.
Whirl Islands and Cerulean Cave stay dark.

### HM obstacles (`data/eventdata/zone_event/`)

65 Cut trees and Rock Smash rocks are hidden, by setting each object's hidden flag to `FLAG_GOT_BAG`, which is set in the opening and never cleared. They stay in the object list, so
script object IDs don't change. Each obstacle was checked with a flood fill of the map's collision data, then its surroundings were read in the event scripts.

- **Kept because they block required progress:** the Ilex Forest tree, the trees in front of the Vermilion and Celadon Gyms, and the three inside Celadon Gym.
- **Kept as Rock Smash encounter spots:** every rock in Ruins of Alph (outside), Cianwood City, Dark Cave, Cliff Cave, Route 19, Vermilion City, Rock Tunnel, Victory Road and Cerulean Cave. Removing
  them would remove those wild encounters.
- **Kept as puzzles:** all Strength boulders, and the two rocks in Burned Tower B1F that are part of a boulder puzzle.
- **Removed:** every other tree on routes and towns, Viridian Forest's two, and the rocks on Routes 3 and 32, in Pewter and Violet Cities, Burned Tower 1F, Ice Path B3F, Tohjo Falls and Mt. Silver Cave.
  None of them is the only way to a required place. The Route 35 tree opens a shortcut to Route 36 that's west of Sudowoodo, so it doesn't bypass that gate.

### Legendaries and gifts (`data/scr_seq/scr_seq_0228_R30R0101.s`, `data/text/376.txt`, `src/script_new_cmds.c`)

After the Elite Four, a new NPC, the Collector, in the house beside Mr. Pokémon's gives one of each Pokémon with no other source, and the Enigma Stone and Red Orb. See the
[gift page](reference/gift_static.md). Each gift is tracked by one of the unused flags `FLAG_UNK_880` to `FLAG_UNK_8A8`. New script command `SetLastMonFateful` marks the last party Pokémon as a fateful
encounter, because the vanilla Celebi and Arceus events and mythical obedience need that. Giving the Enigma Stone also sets `VAR_UNK_4043` to the value Mystery Gift would have set, so Steven's event runs.

In HeartGold the Embedded Tower hides Groudon and only uses the Blue Orb, which Mr. Pokémon gives for Kyogre. So that the Red Orb does something:

- `data/scr_seq/scr_seq_0260_R47.s`: with the Red Orb and no Groudon caught, the tower door leads to Groudon's room.
- `data/scr_seq/scr_seq_0133_D52R0101.s`: Groudon appears while you hold the Red Orb and returns if you run or knock it out. Catching it ends with no hiker scene and leaves `VAR_SCENE_EMBEDDED_TOWER` alone, because Oak's Blue Orb, Kyogre and Rayquaza event chain runs on that value.

### Battles and NPCs

- **League:** the second-round teams are vanilla's rule, used once `VAR_UNK_4135` reaches 8, after all eight Kanto Gyms. **Gym Leader rematches** are vanilla's, at the Fighting Dojo in Saffron City after
  the phone calls. Neither needed a change.
- **Kanto boss rush** (`data/scr_seq/scr_seq_0832_T11R0101.s`, `data/text/533.txt`): a new NPC in the Fighting Dojo, available with all eight Kanto Badges, runs the eight Kanto Leaders' rematch teams in a row. The party
  is healed between battles and it can be repeated.
- **Kurt** (`data/scr_seq/scr_seq_0874_T23R0501.s`) makes the balls immediately instead of the next day. His phone number step still follows the first batch.
- **Phone calls** (`bytereplacement`): the chance of a random call on each check is 5%, down from 50%. Story calls aren't affected.

### Pocket Center with no Pokémon (`data/scr_seq/scr_seq_00003_commonscript.s`, `data/text/040.txt`)

With an empty party, the Pocket Center now says there's nothing to heal, with no heal jingle.

Ability Capsules, Ability Patches and Mints are hg-engine features. Redux only adds them to shops and sets their prices.

### Developer tools

- `scripts/emu_test.py`: plays `test.nds` headlessly for testing. See `AGENTS.md`
- `scripts/build_reference_docs.py`: generates `documentation/reference/`
- `scripts/build_reference_site.py`: builds the [reference site](https://gnawang.github.io/hg-redux/) from `documentation/reference/`, using `scripts/reference_site.html`. `.github/workflows/reference-site.yml` publishes it to GitHub Pages when those pages change on `main`
- `scripts/build_title_logo.py`: converts the title logo PNG
- `scripts/build_dex_areas.py`: updates `data/PokedexArea.c` from the wild encounters

## Dropped

- **PC anywhere** (L button, from HeartGold Generations): it hooks overworld input and uses an arbitrary game flag. Not worth the risk.

## Planned, not started

- **Coach Trainers giving TMs:** needs a decision on who these NPCs are.
