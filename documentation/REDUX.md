# Pokémon HeartGold Redux — project notes

Pokémon HeartGold Redux is built on [hg-engine](https://github.com/BluRosie/hg-engine).
This file records how Redux's data was generated so it can be reproduced.

## Learnsets

`data/learnsets/learnsets.json` is generated, not hand-edited. Regenerate it with:

```bash
python3 scripts/build_learnsets.py --generate data/learnsets/learnsets.json --cutoff custom --inherit-level --inherit-egg --inherit-machine --inherit-tutor --ignore-files 20_la.json 99_go.json
```

- Level-up and egg moves come from the newest game that has data for each species
  (Legends Z-A first, then Scarlet/Violet, then older games).
- TM and tutor compatibility is the union of every game.
- Legends: Arceus and Pokémon GO are ignored. Every Redux species already has data
  from a mainline game.
- `data/learnsets/base/custom.json` applies last. It holds Redux overrides: level-up
  moves that hg-engine has not implemented are removed (the engine blocks learning them
  anyway). Rage Fist is replaced with Shadow Punch for Primeape and Annihilape.

To change a single learnset, edit its entry in `custom.json` and rerun the command above.

## Evolutions

Vanilla and hg-engine evolution methods are kept. Redux adds or replaces these:

| Change | Species |
|---|---|
| Pure trade evolutions also evolve at **level 36** | Kadabra, Machoke, Graveler (incl. Alolan), Haunter |
| Trade-with-item evolutions also evolve by **using the item** from the bag | Poliwhirl and Slowpoke (King's Rock), Onix and Scyther (Metal Coat), Rhydon (Protector), Seadra (Dragon Scale), Electabuzz (Electirizer), Magmar (Magmarizer), Porygon (Up-Grade), Porygon2 (Dubious Disc), Feebas (Prism Scale), Dusclops (Reaper Cloth), Clamperl (Deep Sea Tooth/Scale) |
| Hold-item-and-level evolutions also evolve by **using the item** (no day/night requirement) | Gligar (Razor Fang), Sneasel (Razor Claw), Hisuian Sneasel (Razor Claw), Ursaring (Peat Block), Happiny (Oval Stone) |
| `EVO_FORM_ARGUMENT` is not evaluated by hg-engine, so it is replaced with **level 35** | Primeape → Annihilape, Stantler → Wyrdeer |

For the "use the item" evolutions, the items are marked usable on party Pokémon in
`data/itemdata/itemdata.c` (`fieldUseFunc = 20`, `partyUse = 1`, `evolve = TRUE`), the same
settings hg-engine already uses for Linking Cord and Peat Block. Their held-item battle
effects are unchanged.

## Shops

Shops use hg-engine's `MART_EXPANSION` lists in `src/field/mart.c`. Additions follow
HeartGold Generations' layout:

| Shop | Added items |
|---|---|
| Every Poké Mart (badge-gated) | Max Ether (3 badges), Elixir (5), Max Elixir (7), Max Revive (8) |
| Goldenrod and Celadon Dept. Store 2F, medicine clerk | PP Up, Ability Capsule, Ability Patch, all 21 Nature Mints |
| Goldenrod Dept. Store 3F | King's Rock, Metal Coat, Dragon Scale, Up-Grade, Dubious Disc, Protector, Electirizer, Magmarizer, Reaper Cloth, Prism Scale, Deep Sea Tooth/Scale, Razor Fang, Razor Claw, Oval Stone |
| Goldenrod Dept. Store 5F | Fire, Water, Thunder, Leaf, Moon, Sun and Ice Stones |
| Celadon Dept. Store 3F | Shiny, Dusk and Dawn Stones, Black Augurite, Peat Block, Galarica Cuff and Wreath |

Prices are the modern defaults from `itemdata.c` (Mints ₽20,000, Ability Capsule ₽100,000,
Ability Patch ₽500,000).
