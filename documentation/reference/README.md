# Pokémon HeartGold Redux reference

What's in the game now. The [reference site](https://gnawang.github.io/hg-redux/) shows the same data in a searchable page. `scripts/build_reference_docs.py` generates the data pages from the game's data, so don't
edit them by hand. Rerun it after changing that data. Only [gift_static.md](gift_static.md) is written by hand,
because that information is in the game's event scripts.

| Page | Contents |
|---|---|
| [encounters.md](encounters.md) | Wild Pokémon for each area: chances and levels by time of day, plus surfing, Rock Smash, fishing, swarms and radio sounds |
| [special_encounters.md](special_encounters.md) | Headbutt trees, the Safari Zone and the Bug-Catching Contest |
| [gift_static.md](gift_static.md) | Gift Pokémon, eggs, prizes, one-off battles and roaming Pokémon |
| [pokemon.md](pokemon.md) | Every Pokémon in the roster: types, abilities, stats, evolutions, full movesets and egg cycles, with what changed from hg-engine |
| [trainers.md](trainers.md) | Teams for the rival, Gym Leaders, Elite Four, Champion, Team Rocket's leaders and Red |
| [other_trainers.md](other_trainers.md) | Teams for every other trainer, by trainer class |
| [moves.md](moves.md) | Every move a Redux Pokémon can learn: type, power, accuracy, PP, where to buy its TM, and who learns it by level-up, TM, tutor or egg |
| [items.md](items.md) | What every shop sells, with prices, badge requirements and descriptions |

New items, prices and game settings are in [REDUX_CHANGES.md](../REDUX_CHANGES.md), which also explains
why each change was made and lists the work still planned.
