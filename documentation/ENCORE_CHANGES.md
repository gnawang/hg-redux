# Pokémon HeartGold Encore: changes from hg-engine

Pokémon HeartGold Encore (called HeartGold Redux until November 2026) is a fork of [BluRosie/hg-engine](https://github.com/BluRosie/hg-engine).
This file lists every change Encore makes on top of upstream, the design rules behind them,
and the work still planned. Keep it up to date in the same commit as each change.

For what's in the game now (wild encounters, every Pokémon and move, trainers' teams, shop stock), see
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

The rest of this file lists changes from hg-engine. These come with hg-engine and stay on in Encore (see `include/config.h`):

- **Pokémon and battles:** Fairy type and the latest type chart, modern base stats, moves and abilities, hidden abilities, the expanded species list, and Champions power, type, accuracy and effect-chance changes.
- **Catching and growth:** capture experience, critical captures, modern Poké Ball logic, the modern experience formula and vitamin EV caps.
- **Field and items:** reusable TMs, a prompt to use another repel, an EV/IV viewer, expanded bag pockets and PC boxes, and editable shop lists. Poison does no damage in the overworld.

## Changes

### Settings (`include/config.h`, `armips/include/config.s`, `header.yaml`, `banner.yaml`)

| Setting | Value | Why |
|---|---|---|
| ROM title and banner | "HG ENCORE" / "Pokemon HeartGold Encore" | Hack name |
| `MEGA_EVOLUTIONS`, `PRIMAL_REVERSION` | Off | Replaced by permanent retypes |
| `IMPLEMENT_BDHCAM_ROUTINE` | Off | Keep vanilla camera behaviour |
| `SHINY_ODDS` | 32 (1 in 2048) | Matches HeartGold Generations |
| `DELETABLE_HMS` | On | HMs can be forgotten |
| `FAST_TEXT_PRINTING`, `ALWAYS_HAVE_NATIONAL_DEX` | On | QoL; National Dex from the start |
| Transparent text boxes, level cap, 60 fps, wild double battles | Off (upstream default) | Not wanted, or unstable |
| `BUILD_DUMPED_EVENTDATA` | On | Map objects Encore changes come from `data/eventdata/zone_event/`. Only maps in that folder replace the ROM's |
| `ALLOW_SAVE_CHANGES` | On (upstream default) | Required for the expanded Pokédex. Saves aren't PKHeX-compatible. The armips side uses `.ifdef`, so its `0` value still means on |

### Title screen logo (`rawdata/title_demo/`, `data/graphics/title/encore_logo.png`)

The title screen shows "ENCORE" in place of "VERSION" under the HeartGold logo, following the layout of HeartGold Generations.
"ENCORE" is original pixel art in the style of the earlier "REDUX" lettering: the same 16×20 letters with the vanilla
logo's gradient, a dark outline and a gold border. The rest of the logo is the vanilla art, and it uses the vanilla palette, so there are no
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

The National list and every search list hold only the Encore roster of 500 Pokémon: Gens 1–4 and the seven later evolutions. Upstream had those seven only in the National list, so
they're added to the name, height, weight, type and body lists, and Sylveon is listed under Normal. Kyogre, Giratina and Shaymin, missing from upstream's height lists, are added too.

The seven later evolutions are numbered 494 to 500 in roster order, straight after Arceus, instead of their official numbers, so the National grid ends at 500 with no blank run. The numbers come from
one lookup, `encore_dex_species` in `armips/asm/pokedex.s`, which the grid, entry page and summary screen all use. Keep it in the same order as the end of `sPokedexSort_NationalNum`. Their entries in `data/Species.c` are
trimmed where a long line stopped the text from wrapping: Ursaluna, Annihilape, Farigiraf and Dudunsparce. Dudunsparce shows as "Dudunspars" because names are capped at 10 characters.

The area maps' time-of-day lists are generated from `data/Encounters.c` by `scripts/build_dex_areas.py`. Swarm and radio Pokémon go in the Special lists, which
otherwise keep their vanilla Headbutt areas, and Safari Zone entries are kept.

### Learnsets (`data/learnsets/`)

`data/learnsets/learnsets.json` is generated, not hand-edited. Regenerate it with:

```bash
python3 scripts/build_learnsets.py --generate data/learnsets/learnsets.json --cutoff custom --inherit-level --inherit-egg --inherit-machine --inherit-tutor --ignore-files 20_la.json 99_go.json
```

- Level-up and egg moves are the union of hg-engine's sets, the learnset pass below, HeartGold/SoulSilver, Scarlet/Violet and Legends Z-A, so a
  Pokémon learns everything it learns in any of them. A move already in hg-engine's set or the learnset pass keeps that level. A move only the other
  games have takes its Scarlet/Violet level, else its Z-A level, else its HeartGold level, so evolved Pokémon also get newer games' level-1 moves.
  The 8 retyped Pokémon get moves of their new type from Z-A, e.g. Meganium learns Disarming Voice at level 9.
- Only moves hg-engine implements are kept. Moves flagged `FLAG_UNUSABLE_UNIMPLEMENTED` in `data/Moves.c`, such as Echoed Voice, Round and Ally Switch,
  are left out of level-up and egg moves; with `BLOCK_LEARNING_UNIMPLEMENTED_MOVES` the game wouldn't teach them anyway.
- TM and tutor compatibility is the union of every game. TM01–TM92, the HMs, the move tutors and the newer TMs and TRs sold in shops (see Shops) can be used in the game.
  hg-engine's other expansion TMs and TRs exist as items but nothing gives or sells them; they teach moves already on a vanilla TM or a tutor, or unimplemented ones.
- Legends: Arceus and Pokémon GO are ignored. Every Encore species has mainline data.
- `data/learnsets/base/custom.json` applies last and holds every roster Pokémon's full level-up and egg moves, with the union above already applied.
  Rage Fist, which hg-engine hasn't implemented, is replaced with Shadow Punch for Primeape and Annihilape. To change one learnset, edit its entry there and rerun the command.

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
- Egg moves that are key to a final evolution's moveset, and that no TM, TR or tutor in the game teaches, are added to its level-up moves. Level 1 means the
  Pokémon gets it on evolving or from the Move Relearner:
  - Morning Sun: Arcanine, Rapidash, Sunflora (1), Venomoth (37). Moonlight: Exeggutor (1). Strength Sap: Vileplume, Bellossom, Victreebel, Jumpluff (1). Wish: Clefable (1).
  - Rapid Spin: Tentacruel, Kabutops, Armaldo, Cloyster (1). Rock Blast: Cloyster (1).
  - Fake Out: Raichu, Medicham, Infernape, Ambipom, Lopunny, Toxicroak, Weavile (1). Mach Punch and Bullet Punch: Hitmontop (1). Bullet Punch: Hariyama (1).
    Ice Shard: Donphan (1). Aqua Jet: Crawdaunt (1). Sucker Punch: Arbok (32).
  - Fire Fang and Ice Fang: Luxray (1). Freeze-Dry: Lapras (42). Belly Drum: Azumarill (50). Shell Smash: Torterra (50).

To compile-check without a ROM, generate the header with:

```bash
python3 scripts/build_learnsets.py --learnsets data/learnsets/learnsets.json --machineout build/learnset/MachineMoveLearnsets.c --levelupout build/learnset/LevelupLearnsets.c --eggout build/learnset/EggLearnsets.c --tutorout build/learnset/TutorMoveLearnsets.c --constsout
```

### Evolutions (`data/Evolutions.c`, `data/itemdata/itemdata.c`)

The original methods are kept; Encore adds alternatives or replaces broken ones.

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
| Town Poké Marts, Goldenrod 5F and Celadon 3F | 71 newer TMs and 22 TRs, see Newer TMs below |

Encore prices (selling to a shop gives half):

| Items | Price |
|---|---|
| Nature Mints | ₽1,000 |
| Ability Capsule, Ability Patch | ₽2,000 |
| All evolution items and stones listed above | ₽1,000 |
| TM01–TM92 | HeartGold's own prices again (₽1,000–7,500). hg-engine had given them newer games' prices, e.g. Hyper Beam ₽1,600 and False Swipe ₽20,000 |
| Newer TMs | By power, on the scale HeartGold already uses: ₽5,500 like Thunder, Blizzard and Fire Blast for 100–135 power, ₽7,500 like Hyper Beam for 140+, ₽3,000 for 70–99, ₽2,000 under 70 and for status moves, ₽1,500 for stat-raising moves like Swords Dance |
| TRs | Cheaper than TMs because they're used up, by how useful the move is: ₽500 (Focus Energy, Metronome, Work Up, Cosmic Power, Venom Drench, Electro Ball, Stored Power), ₽1,000 (Tri Attack, Blaze Kick, Body Slam), ₽2,500 (Megahorn, Power Whip), ₽1,500 the rest |

**Newer TMs.** Every newer move that a roster Pokémon can learn by TM in some game, and that the game otherwise can't teach, is sold as hg-engine's
existing TM item, or its TR item when hg-engine has no TM for it. Moves already on TM01–TM92, an HM or a move tutor aren't sold, nor are Draco Meteor,
Blast Burn, Hydro Cannon and Frenzy Plant, which the Blackthorn tutor teaches. Multi-hit and variable-power attacks are priced by their typical power, e.g. Icicle Spear as 75.
The TMs are spread through the story's Poké Marts (the town's second clerk), growing in impact; none are sold before Violet City. The vanilla TMs stay where they were.

| Shop | Badges | Kind | Newer TMs |
|---|---|---|---|
| Violet City | 0 | Supporting, niche | Haze, Eerie Impulse, Metal Sound, Feather Dance, Coaching, Charge |
| Azalea Town | 1 | Low damage, support and the terrains | Sand Tomb, Smack Down, Weather Ball, Electroweb, Grassy Glide, Encore, Electric, Grassy, Misty and Psychic Terrain |
| Goldenrod Dept. Store 5F | 2 | Medium damage, niche | Breaking Swipe, Skitter Smack, Scorching Sands, Psychic Noise, Temper Flare, Lash Out, Mega Punch, Reversal, Heavy Slam, Heat Crash, Baton Pass |
| Ecruteak City | 3 | High utility | Flip Turn, Scald, Leech Life, Icicle Spear, Scale Shot, Lunge, Ice Spinner, Throat Chop |
| Olivine City | 4 | Consistent, stronger | Dual Wingbeat, Aura Sphere, Triple Axel, Bug Buzz, Crunch, Power Gem, Drill Run, Liquidation, Expanding Force, Pollen Puff |
| Mahogany Town shop, after the Rocket Hideout | 6 | Setup | Dragon Dance, Nasty Plot, Amnesia, Curse |
| Blackthorn City (also the Battle Frontier's shop) | 7 | Strong | High Horsepower, Play Rough, Wild Charge, Phantom Force, Hyper Voice, Muddy Water, Sludge Wave, Petal Blizzard |
| Indigo Plateau | 8 | Strong | Double-Edge, Supercell Slam, Misty Explosion, Meteor Beam |
| Celadon Dept. Store 3F | Kanto | Strongest | Close Combat, Brave Bird, Future Sight, Hydro Pump, Poltergeist, Leaf Storm, Flare Blitz, Hurricane, Solar Blade, Steel Beam |

TRs are the 22 moves with no TM item. Goldenrod 5F sells the niche ones (Focus Energy, Metronome, Work Up, Cosmic Power, Venom Drench, Electro Ball, Stored Power,
Tri Attack, Blaze Kick, Body Slam) and Celadon 3F the stronger ones (Agility, Spikes, Toxic Spikes, Psyshock, Psychic Fangs, Dazzling Gleam, Darkest Lariat, Foul Play,
Leaf Blade, Body Press, Megahorn, Power Whip). hg-engine's other 78 TRs teach moves already on a TM, an HM or a tutor, or Ally Switch, which isn't implemented, so they aren't sold.
The full lists are on the [shops page](reference/items.md).

- TMs are reusable (`REUSABLE_TMS`); TRs are used up, as in Sword and Shield.
- The TM pocket holds 200 kinds of item instead of 101 (`NUM_BAG_TMS_HMS` in `include/constants/item.h`), so all 193 can be carried. This changes the save layout,
  so saves from before this change don't load correctly. Tested in the emulator: a game with 96 TMs saved, reset and continued with the pocket intact.
- `data/graphics/item/tm100_sv.png`, the Dragon Dance TM's icon, was hg-engine's "?" placeholder. It's now the Dragon-type disc, copied from TM02.

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
(`std_fade_end_mom_music`). Vanilla shares that script's body with five other shared scripts, so Encore gives 2038 its own
entry point. If the player doesn't have the Pocket Center yet, Mom says one extra line and gives both items with the
usual "obtained" fanfare (the vanilla give-item routine `_080A`); then the music fades as before. Her scene is the first
script that calls 2038, and the item check makes it a one-time gift, so no new flag or map script edit is needed.

### Regional forms (excluded)

Encore has no regional forms: they add complexity and don't fit the feel of HeartGold. hg-engine keeps their species
data, but nothing in Encore places them. Upstream's wild encounters, trainers, Safari Zone, Headbutt trees, shops and
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
Sacred Gold. Gifts and static encounters from Sacred Gold aren't added. Encore has no 1% wild encounters: wherever a Pokémon filled only the 1% grass or surf slots, they hold the Pokémon from the 4% slot next to them instead (37 slots). Lapras, Phione and Wigglytuff left the wild this way; they come from Union Cave, breeding Manaphy and evolution. Roster Pokémon the list leaves out come from [the Collector](reference/gift_static.md).

Johto and Kanto Pokémon are the common finds, as in HeartGold, and Hoenn and Sinnoh Pokémon are uncommon. A Pokémon counts as Johto or Kanto when any
member of its evolution family is #1–251, so Azurill, Munchlax and Magnezone do. In each grass, cave, surf, rod and Rock Smash table:

- Every Pokémon stays in the table it was in, so nothing became harder to obtain than "uncommon".
- Hoenn and Sinnoh Pokémon hold one slot each, taken from the rarest up, and together at most 20% where the table has room: usually 5–10% each.
  A table with more than four of them goes over 20%; Sprout Tower and Routes 30 and 31 are about 40%, spread over six Pokémon.
- Johto and Kanto Pokémon fill the rest, most common first, taking turns so none takes several big slots. Where a table had too few of them
  (fewer than 4 on land, 2 on water), it gets upstream's vanilla HeartGold Pokémon for that table, e.g. Tentacool on the Route 26, 27 and Cianwood waters,
  Magikarp and Krabby in Cianwood's rods and Geodude in Rock Tunnel B1F's rocks.
- Slot levels are unchanged, so a Pokémon moved to a rarer slot takes that slot's level. Swarms, radio sounds and Headbutt trees are unchanged.

Overall the Hoenn and Sinnoh share fell from 20% to 15% of grass and cave encounters, and from about 15% to 3–6% of water encounters.

### Trainers (`data/Trainers.c`)

Key trainers are rebuilt with team design drawn equally from Sacred Gold, Crystal Legacy and Polished Crystal, on top of vanilla rosters.
Levels follow Sacred Gold's curve, matching Encore's wild levels. This covers all 16 Gym Leaders, the first-round Elite Four, Lance, Red, Giovanni,
the Rocket Executives and Silver's fights from Azalea on, except the Cherrygrove and Dragon's Den ones. The full teams are on the [trainer](reference/trainers.md) page.

- Team size starts from vanilla. Early bosses gain one or two Pokémon, the Johto Gyms use 3 to 5, and 6-Pokémon teams start with Lance's
  league fight and the Kanto Gyms. The Elite Four keep 5.
- Silver grows a set team: Teddiursa, then Ursaring, then Ursaluna, and Larvitar through Tyranitar. From the Burned Tower on, his other slots change to
  cover his starter's weaknesses.
- Red keeps his vanilla HeartGold movesets on Sacred Gold's levels, including the three ultimate starter moves.
- Proton's ace is the Zubat line and Petrel's is Weezing; neither uses the other's line.
- Fighting Dojo rematches, the League second round, the tag battles, Kimono Girls and Eusine use Encore's own teams, set by each trainer's theme and place in the
  story. Levels for the Dojo and second round follow Sacred Gold's range.
- Later team changes:
  - Whitney's rematch has Wyrdeer instead of Stantler. Pryce's Sneasel is a Weavile. Chuck's Poliwrath uses Close Combat instead of Dynamic Punch.
  - Brock leads with Onix and ends with Golem. In his rematch Tyranitar leads, holding Smooth Rock, in place of Steelix.
  - Janine is set apart from Koga: Roserade and Tentacruel, both with Toxic Spikes, replace Ariados and Qwilfish, and her rematch has Weezing instead of Drapion.
  - Blue's rematch has Machamp instead of Tyranitar. Sabrina's rematch Espeon has Magic Bounce. Koga's Ariados sets Sticky Web instead of using Sucker Punch.
  - Will leads with a Trick Room Farigiraf in both rounds, replacing Jynx and then Espeon, and his Xatu has Magic Bounce.
  - Clair's rematch and tag battle have Flygon instead of Salamence; the tag battle Flygon uses Dragon Claw and Rock Slide so it doesn't lock into Outrage.
    Lance's first round has Flygon and his second round Salamence instead of the weaker Dragonite.
  - Proton adds Toxicroak. Archer has Drapion instead of Raticate, and adds a Magnezone with Sturdy.
  - Some key trainers use the egg moves added to level-up above: Pryce's Lapras (Freeze-Dry), Karen's rematch Vileplume (Strength Sap), Blaine's rematch
    Arcanine (Morning Sun) and Ariana's Arbok (Sucker Punch).
- Bug Catcher Wade's first two rematches are swapped, because the rematch table calls them in reverse order.

Generic trainers are generated from rules, using Sacred Gold as a reference rather than a template:

- Levels are Sacred Gold's for that fight, with the ace at the top and the rest one lower.
- Team size is Polished Crystal's for the same-named trainer, raised to vanilla's size if Sacred Gold's team is at least that big. It's capped at 3 below level 15,
  4 below 32, 5 below 60 and 6 after.
- Species favour the class's type, then Pokémon on that route, then Johto species. Vanilla's strongest Pokémon stays as the ace.
- Gen 3 and 4 Pokémon appear only where Sacred Gold used them or they live on the route, and fill at most half a team.
- Rematches keep the same lines, evolved for the level. Moves come from level-up learnsets and generic trainers hold no items.
- No generic trainer has more Pokémon than the same fight in Sacred Gold. 59 teams that did, such as Swimmer George on Route 41 (5 against 1), lost their
  extra Pokémon from the front of the team, which is where route Pokémon were added to pad it. Double battles keep at least 2.
- Within an area, one species fills at most about a third of the trainers' teams, apart from themed sets (Sprout Tower's Bellsprout, Rocket Grunts, Blackthorn
  and Dragon's Den). 20 extra copies of padding species, such as Ditto on Route 15 and Lanturn on Route 26, became a species from the same trainer's Sacred Gold team.
  Trainers with rematches were left alone so their rematches still match.

The result is a small step below Sacred Gold: the same level curve and ace levels, but generic teams are never bigger and usually smaller (2.0 Pokémon on average
against Sacred Gold's 2.5), generic trainers hold no items, the Johto Gym Leaders use 3 to 5 Pokémon instead of 6, and bosses hold one or two items rather than
one on every Pokémon. AI flags and IVs are vanilla.

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

Ability Capsules, Ability Patches and Mints are hg-engine features. Encore only adds them to shops and sets their prices.

### Developer tools

- `scripts/emu_test.py`: plays `test.nds` headlessly for testing. See `AGENTS.md`
- `scripts/build_reference_docs.py`: generates `documentation/reference/`
- `scripts/build_reference_site.py`: builds the [reference site](https://gnawang.github.io/hg-redux/) from `documentation/reference/`, using `scripts/reference_site.html`.
  Its tabs are Pokémon, moves (with who learns each and how), abilities (with who has each, the battle rules from `data/AbilityFlags.c`, and
  caveats where an ability works differently from its in-game text or not at all, kept in `ABILITY_NOTES` in `build_reference_docs.py`), locations, trainers, key trainers, shops, and events and gifts (from the hand-written
  `gift_static.md`). Locations holds every wild area plus the places that only have trainers, such as Gyms, and lists the trainers fought in each. Place names
  elsewhere link to their location. Each tab opens on its first entry and keeps its search, selection and scroll position when you switch away and back. Hovering a move
  outside the Moves tab shows its type, power, accuracy, PP and description. Every listed move shows its type to its left. Hovering a Pokémon's name shows its
  number, types and abilities beside a hexagon of its base stats. Hovering an ability shows its name and description, and clicking it opens it on
  the Abilities tab. A Pokémon's "Changed in Encore" box lists its TM, tutor and egg move changes one move per row, like its level-up changes. `.github/workflows/reference-site.yml` publishes it to GitHub Pages when those pages change on `main`
- `scripts/build_trainer_locations.py`: writes `scripts/trainer_locations.json`, where each trainer is fought and what the fight is (Gym battle, rematch, the
  rival's fight for your starter and so on), which `build_reference_docs.py` adds to the trainer pages. It reads a [pret/pokeheartgold](https://github.com/pret/pokeheartgold)
  checkout: the map objects and scripts that start each battle, and the phone rematch table. That checkout isn't in the repo, so the JSON is committed. Fights the
  map data can't place or name, such as the Cherrygrove rival and the tag battles, are set by hand in the script. Rerun it if trainers move or the area names change
- `scripts/build_title_logo.py`: converts the title logo PNG
- `scripts/build_dex_areas.py`: updates `data/PokedexArea.c` from the wild encounters

## Dropped

- **PC anywhere** (L button, from HeartGold Generations): it hooks overworld input and uses an arbitrary game flag. Not worth the risk.
- **Coach Trainers giving TMs:** not needed, because every TM can be bought (see Shops).

## Planned, not started

Nothing.
