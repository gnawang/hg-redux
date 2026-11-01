# Wild encounters

Generated from `data/Encounters.c` by `scripts/build_reference_docs.py`. Don't edit by hand.

Percentages are the chance of each Pokémon when an encounter happens, adding up every slot it fills. Chances come from `src/field/encounter_check.c`.

- Grass and caves: 12 slots at 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1 and 1%, with separate morning, day and night tables
- Surfing: 60, 30, 5, 4 and 1%
- All rods: 40, 30, 15, 10 and 5%
- Rock Smash: 80 and 20%

Evening uses the day table, and late night uses the night table.

"Special" lists Pokémon that take over slots under a condition. The tables above don't include them.

| Condition | Effect |
|---|---|
| Land swarm | Takes the two 20% slots, 40% in all |
| Hoenn or Sinnoh Sound on the radio | Each listed Pokémon takes two 10% slots, 20% each |
| Surf swarm | Takes the 60% slot |
| Fishing swarm | Old Rod 15%, Good Rod 65%, Super Rod 100% |
| Night fishing, at night or late night | Good Rod 10%, Super Rod 30% |

Headbutt trees, the Safari Zone and the Bug-Catching Contest are in [special_encounters.md](special_encounters.md). Gift and one-off Pokémon are in [gift_static.md](gift_static.md).

## New Bark Town

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 10–25 |
| Tentacruel | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder

## Route 29

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 55% (Lv 2–4) | 55% (Lv 2–4) | – |
| Sentret | 40% (Lv 2–3) | 40% (Lv 2–3) | – |
| Rattata | 5% (Lv 4) | 5% (Lv 4) | 15% (Lv 2–4) |
| Hoothoot | – | – | 85% (Lv 2–4) |

Special: Land swarm: Pidgey; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Cherrygrove City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 10–25 |
| Tentacruel | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu

## Route 30

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 40% (Lv 2–4) | 50% (Lv 2–4) | – |
| Caterpie | 50% (Lv 3–4) | 35% (Lv 3–4) | – |
| Metapod | 10% (Lv 4) | 15% (Lv 4) | – |
| Spinarak | – | – | 30% (Lv 2) |
| Rattata | – | – | 40% (Lv 3–4) |
| Hoothoot | – | – | 30% (Lv 4) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10–25 |
| Poliwhirl | 10% | 15–32 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Pidgey; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 31

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 30% (Lv 3) | 30% (Lv 3) | – |
| Caterpie | 35% (Lv 4–5) | 35% (Lv 4–5) | – |
| Bellsprout | 20% (Lv 3) | 20% (Lv 3) | 20% (Lv 3) |
| Metapod | 15% (Lv 5) | 15% (Lv 5) | – |
| Spinarak | – | – | 30% (Lv 3) |
| Rattata | – | – | 40% (Lv 4–5) |
| Hoothoot | – | – | 10% (Lv 5) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10–25 |
| Poliwhirl | 10% | 15–32 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Pidgey; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Violet City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10–25 |
| Poliwhirl | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Whiscash; Night fishing: Poliwag

## Sprout Tower 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 3–6) | 100% (Lv 3–6) | 15% (Lv 3–5) |
| Gastly | – | – | 85% (Lv 3–6) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Sprout Tower 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 3–6) | 100% (Lv 3–6) | 15% (Lv 3–5) |
| Gastly | – | – | 85% (Lv 3–6) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Route 32

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Bellsprout | 30% (Lv 6) | 30% (Lv 6) | 20% (Lv 6) |
| Rattata | 35% (Lv 4–6) | 40% (Lv 4–6) | 30% (Lv 4) |
| Mareep | 20% (Lv 6) | 20% (Lv 6) | 10% (Lv 6) |
| Hoppip | 10% (Lv 6) | 10% (Lv 6) | – |
| Zubat | 5% (Lv 4) | – | 5% (Lv 4) |
| Wooper | – | – | 35% (Lv 6) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 10–20 |
| Quagsire | 30% | 15–25 |
| Tentacruel | 10% | 15–36 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 55% | 20 |
| Qwilfish | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 70% | 40 |
| Magikarp | 20% | 40 |
| Qwilfish | 10% | 40 |

Special: Land swarm: Bellsprout; Surf swarm: Tentacool; Fishing swarm: Qwilfish; Night fishing: Tentacool; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Ruins of Alph Outside

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Natu | 90% (Lv 18–24) | 90% (Lv 18–24) | 90% (Lv 18–24) |
| Smeargle | 10% (Lv 20–22) | 10% (Lv 20–22) | 10% (Lv 20–22) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Quagsire | 40% | 10–25 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 100% | 3–14 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Natu; Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Ruins of Alph Inside Main Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Unown | 100% (Lv 5) | 100% (Lv 5) | 100% (Lv 5) |

Special: Land swarm: Unown; Hoenn Sound: Unown, Unown; Sinnoh Sound: Unown, Unown

## Ruins of Alph Inside Main Room Unused

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Unown | 100% (Lv 5) | 100% (Lv 5) | 100% (Lv 5) |

Special: Land swarm: Unown; Hoenn Sound: Unown, Unown; Sinnoh Sound: Unown, Unown

## Ruins of Alph Inside Main Room Unused

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Unown | 100% (Lv 5) | 100% (Lv 5) | 100% (Lv 5) |

Special: Land swarm: Unown; Hoenn Sound: Unown, Unown; Sinnoh Sound: Unown, Unown

## Ruins of Alph Inside Ladder Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Unown | 100% (Lv 5) | 100% (Lv 5) | 100% (Lv 5) |

Special: Land swarm: Unown; Hoenn Sound: Unown, Unown; Sinnoh Sound: Unown, Unown

## Union Cave 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 30% (Lv 6) | 30% (Lv 6) | 30% (Lv 6) |
| Sandshrew | 30% (Lv 6) | 30% (Lv 6) | 30% (Lv 6) |
| Zubat | 25% (Lv 5–7) | 25% (Lv 5–7) | 25% (Lv 5–7) |
| Rattata | 10% (Lv 4) | 10% (Lv 4) | 10% (Lv 4) |
| Onix | 5% (Lv 6) | 5% (Lv 6) | 5% (Lv 6) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Quagsire | 40% | 10–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Geodude; Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Union Cave B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 30% (Lv 8) | 30% (Lv 8) | 30% (Lv 8) |
| Sandshrew | 30% (Lv 8) | 30% (Lv 8) | 30% (Lv 8) |
| Zubat | 25% (Lv 7–9) | 25% (Lv 7–9) | 25% (Lv 7–9) |
| Onix | 10% (Lv 8) | 10% (Lv 8) | 10% (Lv 8) |
| Rattata | 5% (Lv 6) | 5% (Lv 6) | 5% (Lv 6) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Quagsire | 40% | 10–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Geodude; Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Union Cave B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 22) | 30% (Lv 22) | 30% (Lv 22) |
| Raticate | 30% (Lv 22) | 30% (Lv 22) | 30% (Lv 22) |
| Golbat | 20% (Lv 22) | 20% (Lv 22) | 20% (Lv 22) |
| Geodude | 10% (Lv 21) | 10% (Lv 21) | 10% (Lv 21) |
| Rattata | 5% (Lv 20) | 5% (Lv 20) | 5% (Lv 20) |
| Onix | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 10–20 |
| Quagsire | 30% | 15–25 |
| Tentacruel | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Land swarm: Zubat; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 33

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Hoppip | 35% (Lv 6–8) | 35% (Lv 6–8) | – |
| Rattata | 40% (Lv 6–7) | 45% (Lv 4–7) | 60% (Lv 6–7) |
| Spearow | 20% (Lv 6) | 20% (Lv 6) | – |
| Zubat | 5% (Lv 4) | – | 40% (Lv 4–8) |

Special: Land swarm: Hoppip; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Slowpoke Well 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 85% (Lv 5–8) | 85% (Lv 5–8) | 85% (Lv 5–8) |
| Slowpoke | 15% (Lv 6–8) | 15% (Lv 6–8) | 15% (Lv 6–8) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 100% | 5–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Zubat; Surf swarm: Slowpoke; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Slowpoke Well B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 80% (Lv 19–23) | 80% (Lv 19–23) | 80% (Lv 19–23) |
| Slowpoke | 15% (Lv 21–23) | 15% (Lv 21–23) | 15% (Lv 21–23) |
| Golbat | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 90% | 10–25 |
| Slowbro | 10% | 15–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Zubat; Surf swarm: Slowpoke; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Ilex Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Caterpie | 50% (Lv 5–6) | 60% (Lv 5–6) | – |
| Metapod | 30% (Lv 6) | 30% (Lv 5–6) | – |
| Paras | 15% (Lv 5–6) | 5% (Lv 6) | 15% (Lv 5–6) |
| Zubat | 5% (Lv 5) | 5% (Lv 5) | 25% (Lv 5–6) |
| Oddish | – | – | 60% (Lv 5–6) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 5–20 |
| Golduck | 10% | 10–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Caterpie; Surf swarm: Psyduck; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Spoink, Numel; Sinnoh Sound: Budew, Carnivine

## Route 34

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Drowzee | 50% (Lv 10–12) | 50% (Lv 10–12) | 50% (Lv 10–12) |
| Rattata | 35% (Lv 11–13) | 35% (Lv 11–13) | 35% (Lv 11–13) |
| Abra | 10% (Lv 10) | 10% (Lv 10) | 10% (Lv 10) |
| Ditto | 5% (Lv 10) | 5% (Lv 10) | 5% (Lv 10) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 10–25 |
| Tentacruel | 10% | 15–29 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Land swarm: Ralts; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 35

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Nidoran♂ | 30% (Lv 12) | 30% (Lv 12) | 30% (Lv 12) |
| Nidoran♀ | 30% (Lv 12) | 30% (Lv 12) | 30% (Lv 12) |
| Drowzee | 20% (Lv 14) | 20% (Lv 14) | 20% (Lv 14) |
| Abra | 10% (Lv 10) | 10% (Lv 10) | 10% (Lv 10) |
| Pidgey | 5% (Lv 14) | 5% (Lv 14) | – |
| Ditto | 4% (Lv 10) | 4% (Lv 10) | 4% (Lv 10) |
| Yanma | 1% (Lv 12) | 1% (Lv 12) | 1% (Lv 12) |
| Hoothoot | – | – | 5% (Lv 14) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 10–25 |
| Golduck | 10% | 15–31 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Yanma; Surf swarm: Psyduck; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## National Park

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Caterpie | 50% (Lv 10–12) | 30% (Lv 10) | – |
| Metapod | 30% (Lv 10) | 30% (Lv 10) | – |
| Pidgey | 20% (Lv 10–14) | 15% (Lv 12–14) | – |
| Sunkern | – | 25% (Lv 10–12) | – |
| Hoothoot | – | – | 100% (Lv 10–14) |

Special: Land swarm: Caterpie; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 36

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Nidoran♂ | 30% (Lv 12) | 30% (Lv 12) | 30% (Lv 12) |
| Nidoran♀ | 30% (Lv 12) | 30% (Lv 12) | 30% (Lv 12) |
| Pidgey | 25% (Lv 13–15) | 20% (Lv 13) | – |
| Growlithe | 10% (Lv 13) | 15% (Lv 13–15) | 10% (Lv 13) |
| Stantler | 5% (Lv 13) | 5% (Lv 13) | 5% (Lv 13) |
| Hoothoot | – | – | 25% (Lv 13–15) |

Special: Land swarm: Nidoran♂; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 37

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 60% (Lv 13–15) | 50% (Lv 13–15) | – |
| Stantler | 30% (Lv 15) | 30% (Lv 15) | 30% (Lv 15) |
| Growlithe | 10% (Lv 14) | 15% (Lv 14–15) | 10% (Lv 14) |
| Pidgeotto | – | 5% (Lv 15) | – |
| Spinarak | – | – | 40% (Lv 13–15) |
| Hoothoot | – | – | 20% (Lv 15) |

Special: Land swarm: Pidgey; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Ecruteak City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10–25 |
| Poliwhirl | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag

## Burned Tower 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 50% (Lv 13–15) | 50% (Lv 13–15) | 50% (Lv 13–15) |
| Koffing | 35% (Lv 14–16) | 35% (Lv 14–16) | 35% (Lv 14–16) |
| Zubat | 10% (Lv 14) | 10% (Lv 14) | 10% (Lv 14) |
| Raticate | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Burned Tower B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 40% (Lv 14–16) | 35% (Lv 14) | 40% (Lv 14–16) |
| Koffing | 50% (Lv 14–16) | 50% (Lv 14–16) | 50% (Lv 14–16) |
| Zubat | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Magmar | 5% (Lv 14) | 10% (Lv 16) | 5% (Lv 14) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 4F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 5F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 6F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 7F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 8F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 9F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Route 38

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 30% (Lv 16) | 30% (Lv 16) | 40% (Lv 16) |
| Raticate | 30% (Lv 16) | 30% (Lv 16) | 30% (Lv 16) |
| Magnemite | 20% (Lv 16) | 20% (Lv 16) | 20% (Lv 16) |
| Farfetch’d | 10% (Lv 16) | 10% (Lv 16) | – |
| Miltank | 5% (Lv 13) | 5% (Lv 13) | 5% (Lv 13) |
| Tauros | 4% (Lv 13) | 4% (Lv 13) | 4% (Lv 13) |
| Snubbull | 1% (Lv 13) | 1% (Lv 13) | 1% (Lv 13) |

Special: Land swarm: Snubbull; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 39

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 30% (Lv 16) | 30% (Lv 16) | 40% (Lv 16) |
| Raticate | 30% (Lv 17) | 30% (Lv 17) | 30% (Lv 17) |
| Magnemite | 20% (Lv 16) | 20% (Lv 16) | 20% (Lv 16) |
| Farfetch’d | 10% (Lv 16) | 10% (Lv 16) | – |
| Miltank | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Tauros | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |

Special: Land swarm: Rattata; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Olivine City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 10–25 |
| Tentacruel | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu

## Route 40

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 10–25 |
| Tentacruel | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu

## Route 41

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 15–25 |
| Tentacruel | 30% | 15–25 |
| Mantine | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder

## Whirl Islands 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Krabby | 50% (Lv 22–24) | 50% (Lv 22–24) | 50% (Lv 22–24) |
| Zubat | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Seel | 15% (Lv 22–24) | 15% (Lv 22–24) | 15% (Lv 22–24) |
| Golbat | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 15–25 |
| Horsea | 30% | 10–20 |
| Tentacruel | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Horsea | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 40% | 40 |
| Horsea | 30% | 40 |
| Kingler | 20% | 40 |
| Seadra | 10% | 40 |

Special: Land swarm: Krabby; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Horsea; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Whirl Islands B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Krabby | 50% (Lv 22–24) | 50% (Lv 22–24) | 50% (Lv 22–24) |
| Zubat | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Seel | 15% (Lv 22–24) | 15% (Lv 22–24) | 15% (Lv 22–24) |
| Golbat | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

Special: Land swarm: Krabby; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Whirl Islands B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Krabby | 50% (Lv 22–24) | 50% (Lv 22–24) | 50% (Lv 22–24) |
| Zubat | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Seel | 15% (Lv 22–24) | 15% (Lv 22–24) | 15% (Lv 22–24) |
| Golbat | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 60% | 15–25 |
| Tentacruel | 30% | 15–25 |
| Seadra | 10% | 15–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Horsea | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 40% | 40 |
| Horsea | 30% | 40 |
| Kingler | 20% | 40 |
| Seadra | 10% | 40 |

Special: Land swarm: Krabby; Surf swarm: Horsea; Fishing swarm: Magikarp; Night fishing: Horsea; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Whirl Islands B3F Ledge Overlooking Lugia Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Krabby | 50% (Lv 23–25) | 50% (Lv 23–25) | 50% (Lv 23–25) |
| Zubat | 30% (Lv 24) | 30% (Lv 24) | 30% (Lv 24) |
| Seel | 15% (Lv 23–25) | 15% (Lv 23–25) | 15% (Lv 23–25) |
| Golbat | 5% (Lv 24) | 5% (Lv 24) | 5% (Lv 24) |

Special: Land swarm: Krabby; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Cianwood City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 10–25 |
| Tentacruel | 10% | 15–25 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 80% | 15–24 |
| Shuckle | 20% | 23–28 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu

## Route 42

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Mankey | 30% (Lv 15) | 30% (Lv 15) | 30% (Lv 15) |
| Mareep | 30% (Lv 13) | 30% (Lv 13) | 30% (Lv 13) |
| Spearow | 30% (Lv 14–16) | 30% (Lv 14–16) | – |
| Flaaffy | 10% (Lv 15–17) | 10% (Lv 15–17) | 10% (Lv 15–17) |
| Zubat | – | – | 30% (Lv 14–16) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 10–25 |
| Seaking | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Mankey; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Mt Mortar Waterfall Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 60% (Lv 13–15) | 60% (Lv 13–15) | 60% (Lv 13–15) |
| Machop | 20% (Lv 14) | 20% (Lv 14) | 20% (Lv 14) |
| Rattata | 14% (Lv 14–16) | 14% (Lv 14–16) | 14% (Lv 14–16) |
| Geodude | 5% (Lv 14) | 5% (Lv 14) | 5% (Lv 14) |
| Marill | 1% (Lv 15) | 1% (Lv 15) | 1% (Lv 15) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 10–25 |
| Seaking | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Marill; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Mortar Central Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 50% (Lv 13–15) | 50% (Lv 13–15) | 50% (Lv 13–15) |
| Machop | 35% (Lv 13–15) | 35% (Lv 13–15) | 35% (Lv 13–15) |
| Rattata | 10% (Lv 14) | 10% (Lv 14) | 10% (Lv 14) |
| Zubat | 5% (Lv 14) | 5% (Lv 14) | 5% (Lv 14) |

Special: Land swarm: Geodude; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Mortar Room Above Waterfall

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 30% (Lv 31) | 30% (Lv 31) | 30% (Lv 31) |
| Machoke | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Geodude | 20% (Lv 31) | 20% (Lv 31) | 20% (Lv 31) |
| Raticate | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Machop | 5% (Lv 28) | 5% (Lv 28) | 5% (Lv 28) |
| Golbat | 5% (Lv 30) | 5% (Lv 30) | 5% (Lv 30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 15–30 |
| Seaking | 10% | 20–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Graveler; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Mortar B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 60% (Lv 15–17) | 60% (Lv 15–17) | 60% (Lv 15–17) |
| Rattata | 20% (Lv 16) | 20% (Lv 16) | 20% (Lv 16) |
| Machop | 10% (Lv 16) | 10% (Lv 16) | 10% (Lv 16) |
| Geodude | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |
| Raticate | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 10–25 |
| Seaking | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Zubat; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 43

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Flaaffy | 30% (Lv 15) | 40% (Lv 15–17) | 30% (Lv 15) |
| Girafarig | 30% (Lv 15) | 30% (Lv 15) | 30% (Lv 15) |
| Pidgeotto | 25% (Lv 17) | 20% (Lv 17) | – |
| Mareep | 10% (Lv 15) | 10% (Lv 15) | 5% (Lv 16) |
| Venonat | 5% (Lv 16) | – | 15% (Lv 15–17) |
| Noctowl | – | – | 20% (Lv 17) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 5–50 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Flaaffy; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Lake of Rage

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 5–20 |
| Gyarados | 10% | 10–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 20 |
| Gyarados | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 40 |
| Gyarados | 30% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Gyarados

## Route 44

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Tangela | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Weepinbell | 35% (Lv 22–24) | 35% (Lv 22–24) | 35% (Lv 22–24) |
| Bellsprout | 20% (Lv 22) | 20% (Lv 22) | 20% (Lv 22) |
| Lickitung | 15% (Lv 24–26) | 15% (Lv 24–26) | 15% (Lv 24–26) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 15–30 |
| Poliwhirl | 10% | 20–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 55% | 20 |
| Remoraid | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 70% | 40 |
| Magikarp | 20% | 40 |
| Remoraid | 10% | 40 |

Special: Land swarm: Tangela; Surf swarm: Poliwag; Fishing swarm: Remoraid; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Ice Path 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swinub | 40% (Lv 21–23) | 40% (Lv 21–23) | 40% (Lv 21–23) |
| Golbat | 30% (Lv 22) | 30% (Lv 22) | 30% (Lv 22) |
| Zubat | 25% (Lv 22) | 20% (Lv 22) | 25% (Lv 22) |
| Jynx | 5% (Lv 22) | 10% (Lv 22) | 5% (Lv 22) |

Special: Land swarm: Swinub; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Ice Path B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swinub | 40% (Lv 21–23) | 40% (Lv 21–23) | 40% (Lv 21–23) |
| Golbat | 30% (Lv 22) | 30% (Lv 22) | 30% (Lv 22) |
| Zubat | 25% (Lv 22) | 20% (Lv 22) | 25% (Lv 22) |
| Jynx | 5% (Lv 22) | 10% (Lv 22) | 5% (Lv 22) |

Special: Land swarm: Swinub; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Ice Path B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swinub | 40% (Lv 22–24) | 40% (Lv 22–24) | 40% (Lv 22–24) |
| Golbat | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Zubat | 25% (Lv 23) | 20% (Lv 23) | 25% (Lv 23) |
| Jynx | 5% (Lv 23) | 10% (Lv 23) | 5% (Lv 23) |

Special: Land swarm: Swinub; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Ice Path B3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swinub | 40% (Lv 22–24) | 40% (Lv 22–24) | 40% (Lv 22–24) |
| Golbat | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Zubat | 25% (Lv 23) | 20% (Lv 23) | 25% (Lv 23) |
| Jynx | 5% (Lv 23) | 10% (Lv 23) | 5% (Lv 23) |

Special: Land swarm: Swinub; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Blackthorn City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 2–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Poliwag

## Dragons Den

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 5–20 |
| Dratini | 10% | 5–15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 20 |
| Dratini | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 60% | 40 |
| Dratini | 30% | 40 |
| Dragonair | 10% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Dratini

## Route 45

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Graveler | 40% (Lv 23–27) | 40% (Lv 23–27) | 40% (Lv 23–27) |
| Gligar | 20% (Lv 24) | 20% (Lv 24) | 20% (Lv 24) |
| Phanpy | 10% (Lv 20) | 10% (Lv 20) | 10% (Lv 20) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 2–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Swablu; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 46

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 40% (Lv 2–3) | 40% (Lv 2–3) | 45% (Lv 2–3) |
| Spearow | 35% (Lv 2–3) | 35% (Lv 2–3) | – |
| Rattata | 25% (Lv 2–4) | 25% (Lv 2–4) | 55% (Lv 2–4) |

Special: Land swarm: Geodude; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Dark Cave Route 31 Entrance

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 60% (Lv 2–4) | 60% (Lv 2–4) | 60% (Lv 2–4) |
| Zubat | 39% (Lv 2–4) | 39% (Lv 2–4) | 39% (Lv 2–4) |
| Dunsparce | 1% (Lv 4) | 1% (Lv 4) | 1% (Lv 4) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 2–20 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Dunsparce | 80% | 4–8 |
| Geodude | 20% | 8–14 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Dunsparce; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Dark Cave Route 45 Entrance

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Zubat | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Graveler | 20% (Lv 25) | 20% (Lv 25) | 20% (Lv 25) |
| Wobbuffet | 15% (Lv 20–25) | 15% (Lv 20–25) | 15% (Lv 20–25) |
| Golbat | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 2–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Geodude; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 47

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Farfetch’d | 20% (Lv 35) | 20% (Lv 35) | – |
| Miltank | 20% (Lv 35) | 20% (Lv 35) | 20% (Lv 35) |
| Ditto | 41% (Lv 31–40) | 41% (Lv 31–40) | 41% (Lv 31–40) |
| Gloom | 5% (Lv 32) | 5% (Lv 32) | 5% (Lv 32) |
| Spearow | 5% (Lv 31) | 5% (Lv 31) | 5% (Lv 31) |
| Fearow | 4% (Lv 34) | 4% (Lv 34) | 4% (Lv 34) |
| Raticate | 5% (Lv 31–33) | 5% (Lv 31–33) | 5% (Lv 31–33) |
| Noctowl | – | – | 20% (Lv 35) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 15–25 |
| Seel | 30% | 10–20 |
| Staryu | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Land swarm: Ditto; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Mt Moon Outside Area

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 60% | 35 |
| Magikarp | 40% | 30–35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 20 |
| Poliwag | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 100% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag

## Mt Moon Outside Clefairy Active

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 100% | 30–35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10 |
| Magikarp | 10% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 20 |
| Magikarp | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 40 |
| Magikarp | 10% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Poliwag; Night fishing: Magikarp

## Seafoam Islands 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 26–28) | 30% (Lv 26–28) | 30% (Lv 26–28) |
| Golbat | 30% (Lv 30–32) | 30% (Lv 30–32) | 30% (Lv 30–32) |
| Psyduck | 30% (Lv 26–29) | 30% (Lv 26–29) | 30% (Lv 26–29) |
| Golduck | 10% (Lv 32) | 10% (Lv 32) | 10% (Lv 32) |

Special: Land swarm: Zubat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Seel | 30% (Lv 32–34) | 30% (Lv 32–34) | 30% (Lv 32–34) |
| Golbat | 30% (Lv 32–34) | 30% (Lv 32–34) | 30% (Lv 32–34) |
| Psyduck | 16% (Lv 26–28) | 16% (Lv 26–28) | 16% (Lv 26–28) |
| Golduck | 14% (Lv 32–34) | 14% (Lv 32–34) | 14% (Lv 32–34) |
| Zubat | 10% (Lv 28–29) | 10% (Lv 28–29) | 10% (Lv 28–29) |

Special: Land swarm: Seel; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Seel | 30% (Lv 33–35) | 30% (Lv 33–35) | 30% (Lv 33–35) |
| Golbat | 30% (Lv 33–35) | 30% (Lv 33–35) | 30% (Lv 33–35) |
| Psyduck | 16% (Lv 27–30) | 16% (Lv 27–30) | 16% (Lv 27–30) |
| Golduck | 14% (Lv 33–35) | 14% (Lv 33–35) | 14% (Lv 33–35) |
| Zubat | 10% (Lv 29–30) | 10% (Lv 29–30) | 10% (Lv 29–30) |

Special: Land swarm: Seel; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Dewgong | 24% (Lv 35–36) | 24% (Lv 35–36) | 24% (Lv 35–36) |
| Golbat | 30% (Lv 34–36) | 30% (Lv 34–36) | 30% (Lv 34–36) |
| Psyduck | 12% (Lv 31–32) | 12% (Lv 31–32) | 12% (Lv 31–32) |
| Seel | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Golduck | 14% (Lv 34–36) | 14% (Lv 34–36) | 14% (Lv 34–36) |
| Zubat | 10% (Lv 31–32) | 10% (Lv 31–32) | 10% (Lv 31–32) |

Special: Land swarm: Dewgong; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B4F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Dewgong | 24% (Lv 37–38) | 24% (Lv 37–38) | 24% (Lv 37–38) |
| Golbat | 30% (Lv 38–40) | 30% (Lv 38–40) | 30% (Lv 38–40) |
| Psyduck | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Seel | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Jynx | 12% (Lv 38–40) | 12% (Lv 38–40) | 12% (Lv 38–40) |
| Golduck | 14% (Lv 37–38) | 14% (Lv 37–38) | 14% (Lv 37–38) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seel | 60% | 30–40 |
| Horsea | 30% | 30–40 |
| Slowbro | 10% | 35–50 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Psyduck | 30% | 20 |
| Krabby | 20% | 20 |
| Horsea | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 40% | 40 |
| Horsea | 30% | 40 |
| Kingler | 15% | 40 |
| Seadra | 15% | 40 |

Special: Land swarm: Seel; Surf swarm: Seel; Fishing swarm: Magikarp; Night fishing: Horsea; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Silver Moltres Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Quagsire | 40% (Lv 45) | 40% (Lv 45) | 30% (Lv 45) |
| Steelix | 20% (Lv 48) | 20% (Lv 48) | 20% (Lv 48) |
| Golduck | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Donphan | 20% (Lv 47–48) | 20% (Lv 47–48) | 20% (Lv 47–48) |
| Golbat | 5% (Lv 48) | 5% (Lv 48) | 5% (Lv 48) |
| Larvitar | 5% (Lv 15–20) | 5% (Lv 15–20) | 5% (Lv 15–20) |
| Misdreavus | – | – | 10% (Lv 45) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 90% | 30–45 |
| Goldeen | 10% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Quagsire; Surf swarm: Seaking; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Silver 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Quagsire | 30% (Lv 45) | 30% (Lv 45) | 20% (Lv 45) |
| Sneasel | 20% (Lv 48) | 20% (Lv 48) | 20% (Lv 48) |
| Phanpy | 10% (Lv 46) | 10% (Lv 46) | 10% (Lv 46) |
| Golduck | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Donphan | 20% (Lv 48–50) | 20% (Lv 48–50) | 20% (Lv 48–50) |
| Golbat | 5% (Lv 48) | 5% (Lv 48) | 5% (Lv 48) |
| Larvitar | 5% (Lv 15–20) | 5% (Lv 15–20) | 5% (Lv 15–20) |
| Misdreavus | – | – | 10% (Lv 45) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 90% | 30–45 |
| Goldeen | 10% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Quagsire; Surf swarm: Seaking; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Silver 4F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Sneasel | 20% (Lv 50) | 20% (Lv 50) | 20% (Lv 50) |
| Golduck | 30% (Lv 48) | 30% (Lv 48) | 30% (Lv 48) |
| Quagsire | 20% (Lv 45) | 20% (Lv 45) | 10% (Lv 45) |
| Donphan | 20% (Lv 47) | 20% (Lv 47) | 20% (Lv 47) |
| Golbat | 5% (Lv 48) | 5% (Lv 48) | 5% (Lv 48) |
| Larvitar | 5% (Lv 15–20) | 5% (Lv 15–20) | 5% (Lv 15–20) |
| Misdreavus | – | – | 10% (Lv 45) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 90% | 30–45 |
| Goldeen | 10% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Sneasel; Surf swarm: Seaking; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Cliff Edge Gate

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 90% | 20–30 |
| Quagsire | 10% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 20 |
| Poliwag | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 40 |
| Poliwag | 30% | 40 |

Special: Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Magikarp

## Cliff Cave

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 20% (Lv 22) | 20% (Lv 22) | 24% (Lv 20–22) |
| Geodude | 20% (Lv 19) | 20% (Lv 19) | 20% (Lv 19) |
| Krabby | 10% (Lv 20) | 10% (Lv 20) | 10% (Lv 20) |
| Kingler | 10% (Lv 22) | 10% (Lv 22) | 10% (Lv 22) |
| Machop | 10% (Lv 19) | 10% (Lv 19) | 10% (Lv 19) |
| Onix | 10% (Lv 20) | 10% (Lv 20) | 10% (Lv 20) |
| Wooper | 5% (Lv 18) | 5% (Lv 18) | – |
| Quagsire | 5% (Lv 20) | 5% (Lv 20) | – |
| Graveler | 4% (Lv 20) | 4% (Lv 20) | – |
| Machoke | 4% (Lv 22) | 4% (Lv 22) | 4% (Lv 22) |
| Steelix | 2% (Lv 23) | 2% (Lv 23) | 2% (Lv 23) |
| Zubat | – | – | 5% (Lv 18) |
| Misdreavus | – | – | 5% (Lv 20) |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 80% | 20–26 |
| Kingler | 20% | 28–31 |

Special: Land swarm: Golbat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Bell Tower 10F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 100% (Lv 20–24) | 100% (Lv 20–24) | 20% (Lv 22–24) |
| Gastly | – | – | 80% (Lv 20–22) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Mt Silver Outside Pokemon Center

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Tangela | 30% (Lv 41) | 30% (Lv 41) | 30% (Lv 41) |
| Ponyta | 30% (Lv 42) | 30% (Lv 42) | 30% (Lv 42) |
| Donphan | 20% (Lv 42) | 20% (Lv 42) | 20% (Lv 42) |
| Rapidash | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Doduo | 5% (Lv 41) | 5% (Lv 41) | – |
| Dodrio | 5% (Lv 43) | 5% (Lv 43) | – |
| Sneasel | – | – | 10% (Lv 41–43) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 91% | 30–48 |
| Poliwag | 9% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Tangela; Surf swarm: Poliwhirl; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Mt Silver 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Onix | 30% (Lv 42) | 30% (Lv 42) | 30% (Lv 42) |
| Donphan | 30% (Lv 44) | 30% (Lv 44) | 30% (Lv 44) |
| Phanpy | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Graveler | 20% (Lv 41–43) | 20% (Lv 41–43) | 20% (Lv 41–43) |
| Golbat | 5% (Lv 45) | 5% (Lv 45) | 5% (Lv 45) |
| Larvitar | 5% (Lv 15–20) | 5% (Lv 15–20) | 5% (Lv 15–20) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 91% | 30–50 |
| Goldeen | 9% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Goldeen | 30% | 20 |
| Seaking | 20% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 50% | 40 |
| Seaking | 50% | 40 |

Special: Land swarm: Onix; Surf swarm: Seaking; Fishing swarm: Magikarp; Night fishing: Gyarados; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Silver Mountainside

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 40% (Lv 48–51) | 40% (Lv 48–51) | 40% (Lv 48–51) |
| Onix | 30% (Lv 48) | 30% (Lv 48) | 30% (Lv 48) |
| Phanpy | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Donphan | 10% (Lv 50) | 10% (Lv 50) | 10% (Lv 50) |
| Golduck | 5% (Lv 51) | 5% (Lv 51) | 5% (Lv 51) |
| Larvitar | 5% (Lv 15–20) | 5% (Lv 15–20) | 5% (Lv 15–20) |

Special: Land swarm: Golbat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Silver Expert Belt Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Quagsire | 35% (Lv 45) | 35% (Lv 45) | 5% (Lv 45) |
| Golduck | 20% (Lv 48) | 20% (Lv 48) | 20% (Lv 48) |
| Phanpy | 10% (Lv 46) | 10% (Lv 46) | 10% (Lv 46) |
| Donphan | 20% (Lv 47–48) | 20% (Lv 47–48) | 20% (Lv 47–48) |
| Pupitar | 5% (Lv 45) | 5% (Lv 45) | 5% (Lv 45) |
| Golbat | 5% (Lv 48) | 5% (Lv 48) | 5% (Lv 48) |
| Larvitar | 5% (Lv 15–20) | 5% (Lv 15–20) | 5% (Lv 15–20) |
| Misdreavus | – | – | 30% (Lv 45) |

Special: Land swarm: Quagsire; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Silver Top Snowy Area

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Sneasel | 20% (Lv 45) | 20% (Lv 45) | 20% (Lv 45) |
| Golduck | 30% (Lv 48) | 30% (Lv 48) | 20% (Lv 48) |
| Quagsire | 15% (Lv 45) | 15% (Lv 45) | 10% (Lv 45) |
| Donphan | 20% (Lv 47) | 20% (Lv 47) | 20% (Lv 47) |
| Larvitar | 10% (Lv 15–30) | 10% (Lv 15–30) | 10% (Lv 15–30) |
| Golbat | 5% (Lv 48) | 5% (Lv 48) | 5% (Lv 48) |
| Misdreavus | – | – | 15% (Lv 45–48) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 90% | 30–45 |
| Goldeen | 10% | 30–40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Sneasel; Surf swarm: Seaking; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 12

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 25 |
| Quagsire | 30% | 25 |
| Tentacruel | 10% | 25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 70% | 40 |
| Magikarp | 20% | 40 |
| Qwilfish | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Relicanth; Night fishing: Tentacool

## Route 19

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 30–35 |
| Tentacruel | 10% | 35 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Kingler | 80% | 28–31 |
| Krabby | 20% | 24–27 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 50% | 20 |
| Corsola | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 60% | 40 |
| Corsola | 30% | 40 |
| Kingler | 10% | 40 |

Special: Surf swarm: Clamperl; Fishing swarm: Magikarp; Night fishing: Staryu

## Route 20

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 30–35 |
| Tentacruel | 10% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder

## Pallet Town

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 30–35 |
| Tentacruel | 10% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder

## Viridian City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 5–10 |
| Poliwhirl | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag

## Cerulean City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 5–10 |
| Seaking | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen

## Vermilion City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 30–35 |
| Tentacruel | 10% | 35 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Diglett | 80% | 24–37 |
| Shuckle | 20% | 32–35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Surf swarm: Wingull; Fishing swarm: Magikarp; Night fishing: Shellder

## Celadon City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Grimer | 90% | 15–20 |
| Muk | 10% | 15 |

Special: Surf swarm: Grimer

## Fuchsia City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 20 |
| Gyarados | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 40 |
| Gyarados | 30% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Gyarados

## Cinnabar Island

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 30–35 |
| Tentacruel | 10% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder

## Route 48

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Farfetch’d | 20% (Lv 25) | 20% (Lv 25) | – |
| Tauros | 21% (Lv 20–24) | 21% (Lv 20–24) | 21% (Lv 20–24) |
| Hoppip | 11% (Lv 20–22) | 11% (Lv 20–22) | 11% (Lv 20–22) |
| Fearow | 10% (Lv 21) | 10% (Lv 21) | 10% (Lv 21) |
| Gloom | 20% (Lv 22–24) | 20% (Lv 22–24) | 20% (Lv 22–24) |
| Growlithe | 9% (Lv 21–22) | 9% (Lv 21–22) | 29% (Lv 21–25) |
| Girafarig | 5% (Lv 20) | 5% (Lv 20) | 5% (Lv 20) |
| Diglett | 4% (Lv 20) | 4% (Lv 20) | 4% (Lv 20) |

Special: Land swarm: Tauros; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 26

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Doduo | 40% (Lv 28–30) | 40% (Lv 28–30) | – |
| Sandslash | 30% (Lv 28) | 30% (Lv 28) | 30% (Lv 28) |
| Ponyta | 20% (Lv 32) | 20% (Lv 32) | 20% (Lv 32) |
| Raticate | 5% (Lv 30) | 5% (Lv 30) | 40% (Lv 28–30) |
| Dodrio | 5% (Lv 30) | 5% (Lv 30) | – |
| Quagsire | – | – | 10% (Lv 30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 25–30 |
| Tentacruel | 10% | 30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Land swarm: Doduo; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 27

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Doduo | 50% (Lv 28–30) | 50% (Lv 28–30) | – |
| Raticate | 40% (Lv 28–30) | 40% (Lv 28–30) | 40% (Lv 28–30) |
| Ponyta | 5% (Lv 32) | 5% (Lv 32) | 5% (Lv 32) |
| Sandslash | 5% (Lv 30) | 5% (Lv 30) | 5% (Lv 30) |
| Quagsire | – | – | 50% (Lv 28–30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 15–20 |
| Tentacruel | 10% | 20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Land swarm: Doduo; Surf swarm: Luvdisc; Fishing swarm: Magikarp; Night fishing: Shellder; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 28

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Tangela | 30% (Lv 39) | 30% (Lv 39) | 30% (Lv 39) |
| Ponyta | 30% (Lv 40) | 30% (Lv 40) | 30% (Lv 40) |
| Donphan | 20% (Lv 40) | 20% (Lv 40) | 20% (Lv 40) |
| Rapidash | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 41–43) |
| Doduo | 5% (Lv 41) | 5% (Lv 41) | – |
| Dodrio | 5% (Lv 43) | 5% (Lv 43) | – |
| Sneasel | – | – | 10% (Lv 42) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 35–40 |
| Poliwhirl | 10% | 40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Tangela; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Mt Moon 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 6) | 30% (Lv 6) | 30% (Lv 6) |
| Geodude | 30% (Lv 8) | 30% (Lv 8) | 30% (Lv 8) |
| Sandshrew | 20% (Lv 8) | 20% (Lv 8) | 20% (Lv 8) |
| Paras | 10% (Lv 12) | 10% (Lv 12) | 10% (Lv 12) |
| Sandslash | 5% (Lv 10) | 5% (Lv 10) | 5% (Lv 10) |
| Clefairy | 5% (Lv 8) | 5% (Lv 8) | 5% (Lv 8) |

Special: Land swarm: Zubat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt Moon 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 6) | 30% (Lv 6) | 30% (Lv 6) |
| Geodude | 30% (Lv 8) | 30% (Lv 8) | 30% (Lv 8) |
| Sandshrew | 20% (Lv 8) | 20% (Lv 8) | 20% (Lv 8) |
| Paras | 10% (Lv 12) | 10% (Lv 12) | 10% (Lv 12) |
| Sandslash | 5% (Lv 10) | 5% (Lv 10) | 5% (Lv 10) |
| Clefairy | 5% (Lv 8) | 5% (Lv 8) | 5% (Lv 8) |

Special: Land swarm: Zubat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Rock Tunnel 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Cubone | 35% (Lv 10–13) | 35% (Lv 10–13) | 35% (Lv 10–13) |
| Geodude | 30% (Lv 10) | 30% (Lv 10) | 30% (Lv 10) |
| Machop | 20% (Lv 12) | 20% (Lv 12) | 20% (Lv 12) |
| Zubat | 10% (Lv 8) | 10% (Lv 8) | 10% (Lv 8) |
| Machoke | 5% (Lv 14) | 5% (Lv 14) | 5% (Lv 14) |

Special: Land swarm: Cubone; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Rock Tunnel B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Cubone | 30% (Lv 12) | 30% (Lv 12) | 30% (Lv 12) |
| Geodude | 30% (Lv 12) | 30% (Lv 12) | 30% (Lv 12) |
| Onix | 20% (Lv 16) | 20% (Lv 16) | 20% (Lv 16) |
| Zubat | 10% (Lv 10) | 10% (Lv 10) | 10% (Lv 10) |
| Marowak | 5% (Lv 14) | 5% (Lv 14) | 5% (Lv 14) |
| Kangaskhan | 5% (Lv 14) | 5% (Lv 14) | 5% (Lv 14) |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 100% | 12–21 |

Special: Land swarm: Cubone; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Victory Road 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Golbat | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Donphan | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Onix | 15% (Lv 34–36) | 15% (Lv 34–36) | 15% (Lv 34–36) |
| Rhyhorn | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |

Special: Land swarm: Graveler; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 1

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 45% (Lv 2–4) | 45% (Lv 2–4) | – |
| Rattata | 30% (Lv 2) | 30% (Lv 2) | 55% (Lv 2–6) |
| Sentret | 20% (Lv 3) | 20% (Lv 3) | – |
| Furret | 5% (Lv 6) | 5% (Lv 6) | – |
| Hoothoot | – | – | 45% (Lv 2–4) |

Special: Land swarm: Poochyena; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 2 South Below Viridian Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Caterpie | 31% (Lv 3–4) | 31% (Lv 3–4) | – |
| Pidgey | 30% (Lv 3) | 40% (Lv 3–8) | – |
| Metapod | 20% (Lv 5) | 20% (Lv 5) | – |
| Butterfree | 10% (Lv 7–8) | – | – |
| Pidgeotto | 5% (Lv 7) | 9% (Lv 7–10) | – |
| Spinarak | 4% (Lv 10) | – | 31% (Lv 3–4) |
| Hoothoot | – | – | 50% (Lv 3–5) |
| Noctowl | – | – | 14% (Lv 7–10) |
| Ariados | – | – | 5% (Lv 7) |

Special: Land swarm: Caterpie; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 3

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Spearow | 55% (Lv 5–8) | 55% (Lv 5–8) | – |
| Rattata | 35% (Lv 5–10) | 35% (Lv 5–10) | 60% (Lv 5–10) |
| Jigglypuff | 10% (Lv 6) | 10% (Lv 6) | 10% (Lv 6) |
| Zubat | – | – | 30% (Lv 5) |

Special: Land swarm: Baltoy; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 4

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Spearow | 55% (Lv 5–8) | 55% (Lv 5–8) | 30% (Lv 5) |
| Rattata | 35% (Lv 5–10) | 35% (Lv 5–10) | 30% (Lv 8–10) |
| Jigglypuff | 10% (Lv 6) | 10% (Lv 6) | 10% (Lv 6) |
| Zubat | – | – | 30% (Lv 5) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 5–10 |
| Seaking | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Spearow; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 5

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 60% (Lv 13–15) | 60% (Lv 13–15) | – |
| Bellsprout | 30% (Lv 13) | 30% (Lv 13) | 20% (Lv 14) |
| Abra | 10% (Lv 12–14) | 10% (Lv 12–14) | 10% (Lv 12–14) |
| Oddish | – | – | 60% (Lv 13) |
| Gloom | – | – | 10% (Lv 15) |

Special: Land swarm: Pidgey; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 6

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 50% (Lv 13–14) | 50% (Lv 13–14) | – |
| Bellsprout | 30% (Lv 13) | 30% (Lv 13) | 20% (Lv 14) |
| Magnemite | 10% (Lv 15) | 10% (Lv 15) | 10% (Lv 15) |
| Abra | 10% (Lv 12–14) | 10% (Lv 12–14) | 10% (Lv 12–14) |
| Oddish | – | – | 60% (Lv 13) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 5–10 |
| Golduck | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Pidgey; Surf swarm: Psyduck; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 7

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 40% (Lv 15–19) | 35% (Lv 17–19) | 30% (Lv 17) |
| Spearow | 30% (Lv 17) | 30% (Lv 17) | – |
| Growlithe | 20% (Lv 18) | 25% (Lv 15–18) | 20% (Lv 18) |
| Raticate | 10% (Lv 19) | 10% (Lv 19) | 10% (Lv 19) |
| Murkrow | – | – | 35% (Lv 17–19) |
| Houndour | – | – | 5% (Lv 15) |

Special: Land swarm: Rattata; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 8

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgeotto | 65% (Lv 17–19) | 65% (Lv 17–19) | – |
| Abra | 20% (Lv 15) | 20% (Lv 15) | 20% (Lv 15) |
| Growlithe | 10% (Lv 18) | 10% (Lv 18) | 5% (Lv 17) |
| Kadabra | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Noctowl | – | – | 40% (Lv 17–18) |
| Haunter | – | – | 30% (Lv 19) |

Special: Land swarm: Pidgeotto; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 9

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Mankey | 30% (Lv 13) | 30% (Lv 13) | 30% (Lv 13) |
| Rattata | 30% (Lv 15) | 30% (Lv 15) | 40% (Lv 15) |
| Spearow | 20% (Lv 13) | 20% (Lv 13) | – |
| Raticate | 10% (Lv 15) | 10% (Lv 15) | 25% (Lv 13–15) |
| Fearow | 5% (Lv 15) | 5% (Lv 15) | – |
| Primeape | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 10–15 |
| Seaking | 10% | 15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Sableye; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 10

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Spearow | 30% (Lv 16) | 30% (Lv 16) | – |
| Voltorb | 30% (Lv 17) | 30% (Lv 17) | 30% (Lv 17) |
| Raticate | 25% (Lv 16–18) | 20% (Lv 16) | 25% (Lv 16–18) |
| Fearow | 10% (Lv 18) | 10% (Lv 18) | – |
| Electabuzz | 5% (Lv 15) | 10% (Lv 15–18) | 5% (Lv 15) |
| Quagsire | – | – | 40% (Lv 16–18) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 10–15 |
| Seaking | 10% | 15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Spearow; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 11

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Drowzee | 40% (Lv 14–16) | 40% (Lv 14–16) | 40% (Lv 14–16) |
| Rattata | 30% (Lv 15) | 30% (Lv 15) | 30% (Lv 15) |
| Magnemite | 20% (Lv 15) | 20% (Lv 15) | 20% (Lv 15) |
| Hypno | 10% (Lv 16) | 10% (Lv 16) | 10% (Lv 16) |

Special: Land swarm: Drowzee; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 13

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Nidorina | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Nidorino | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Pidgeotto | 20% (Lv 25) | 20% (Lv 25) | – |
| Hoppip | 19% (Lv 22–24) | 19% (Lv 22–24) | – |
| Chansey | 1% (Lv 25) | 1% (Lv 25) | 1% (Lv 25) |
| Noctowl | – | – | 20% (Lv 25) |
| Quagsire | – | – | 19% (Lv 22–24) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 25 |
| Quagsire | 30% | 25 |
| Tentacruel | 10% | 25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 70% | 40 |
| Magikarp | 20% | 40 |
| Qwilfish | 10% | 40 |

Special: Land swarm: Chansey; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Tentacool; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 14

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Nidorina | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Nidorino | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Pidgeotto | 20% (Lv 25) | 20% (Lv 25) | – |
| Hoppip | 10% (Lv 24) | 10% (Lv 24) | – |
| Skiploom | 9% (Lv 26) | 9% (Lv 26) | – |
| Chansey | 1% (Lv 25) | 1% (Lv 25) | 1% (Lv 25) |
| Noctowl | – | – | 20% (Lv 25) |
| Quagsire | – | – | 19% (Lv 24–26) |

Special: Land swarm: Nidorina; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 15

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Nidorina | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Nidorino | 30% (Lv 23) | 30% (Lv 23) | 30% (Lv 23) |
| Pidgeotto | 20% (Lv 25) | 20% (Lv 25) | – |
| Hoppip | 19% (Lv 22–24) | 19% (Lv 22–24) | – |
| Chansey | 1% (Lv 25) | 1% (Lv 25) | 1% (Lv 25) |
| Noctowl | – | – | 20% (Lv 25) |
| Quagsire | – | – | 19% (Lv 22–24) |

Special: Land swarm: Nidorina; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 16

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Grimer | 50% (Lv 26–28) | 50% (Lv 26–28) | 80% (Lv 26–28) |
| Fearow | 40% (Lv 27–29) | 40% (Lv 27–29) | – |
| Slugma | 5% (Lv 27) | 5% (Lv 27) | 5% (Lv 27) |
| Muk | 5% (Lv 30) | 5% (Lv 30) | 5% (Lv 30) |
| Murkrow | – | – | 10% (Lv 29) |

Special: Land swarm: Grimer; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 17

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Fearow | 40% (Lv 28–30) | 40% (Lv 28–30) | – |
| Grimer | 50% (Lv 27–29) | 20% (Lv 29) | 80% (Lv 27–29) |
| Slugma | 5% (Lv 29) | 35% (Lv 27–29) | 5% (Lv 29) |
| Muk | 5% (Lv 32) | 5% (Lv 32) | 15% (Lv 30–32) |

Special: Land swarm: Fearow; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 18

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Grimer | 50% (Lv 26–28) | 50% (Lv 26–28) | 80% (Lv 26–28) |
| Fearow | 40% (Lv 27–29) | 40% (Lv 27–29) | – |
| Slugma | 5% (Lv 27) | 5% (Lv 27) | 5% (Lv 27) |
| Muk | 5% (Lv 30) | 5% (Lv 30) | 15% (Lv 29–30) |

Special: Land swarm: Grimer; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 21

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Tangela | 95% (Lv 20–35) | 90% (Lv 20–35) | 95% (Lv 20–35) |
| Mr. Mime | 5% (Lv 28) | 10% (Lv 28–30) | 5% (Lv 28) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 90% | 30–35 |
| Tentacruel | 10% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Tentacool | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Tentacool | 30% | 20 |
| Chinchou | 20% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 40% | 40 |
| Shellder | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Land swarm: Tangela; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 22

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 30% (Lv 3) | 30% (Lv 3) | 95% (Lv 3–7) |
| Spearow | 50% (Lv 3–5) | 50% (Lv 3–5) | – |
| Doduo | 10% (Lv 4) | 10% (Lv 4) | – |
| Ponyta | 5% (Lv 6) | 5% (Lv 6) | 5% (Lv 6) |
| Fearow | 5% (Lv 7) | 5% (Lv 7) | – |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 5–10 |
| Poliwhirl | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Poliwag | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 80% | 40 |
| Magikarp | 20% | 40 |

Special: Land swarm: Rattata; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 24

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Bellsprout | 60% (Lv 8–10) | 35% (Lv 8) | 5% (Lv 8) |
| Abra | 20% (Lv 9) | 20% (Lv 9) | 20% (Lv 9) |
| Weepinbell | 15% (Lv 12–14) | 15% (Lv 12–14) | 10% (Lv 12) |
| Venonat | 5% (Lv 8) | – | 30% (Lv 8) |
| Sunkern | – | 30% (Lv 10) | – |
| Oddish | – | – | 30% (Lv 10) |
| Venomoth | – | – | 5% (Lv 14) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 5–10 |
| Seaking | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Bellsprout; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 25

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 30% (Lv 8) | 50% (Lv 8) | – |
| Bellsprout | 30% (Lv 10) | 30% (Lv 10) | 5% (Lv 14) |
| Venonat | 20% (Lv 8) | – | 30% (Lv 8) |
| Abra | 10% (Lv 9) | 10% (Lv 9) | 10% (Lv 9) |
| Pidgeotto | 5% (Lv 10) | 5% (Lv 10) | – |
| Weepinbell | 5% (Lv 14) | 5% (Lv 14) | 5% (Lv 10) |
| Oddish | – | – | 30% (Lv 10) |
| Venomoth | – | – | 20% (Lv 8) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 90% | 5–10 |
| Seaking | 10% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Buneary; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Tohjo Falls

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 22) | 30% (Lv 22) | 30% (Lv 22) |
| Raticate | 30% (Lv 22) | 30% (Lv 22) | 30% (Lv 22) |
| Golbat | 20% (Lv 22) | 20% (Lv 22) | 20% (Lv 22) |
| Slowpoke | 15% (Lv 21–23) | 15% (Lv 21–23) | 15% (Lv 21–23) |
| Rattata | 5% (Lv 20) | 5% (Lv 20) | 5% (Lv 20) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 60% | 20 |
| Slowpoke | 30% | 20 |
| Seaking | 10% | 20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Goldeen | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 40 |
| Magikarp | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Zubat; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Digletts Cave

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Diglett | 90% (Lv 13–19) | 90% (Lv 13–19) | 90% (Lv 13–19) |
| Dugtrio | 10% (Lv 19–29) | 10% (Lv 19–29) | 10% (Lv 19–29) |

Special: Land swarm: Diglett; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Victory Road 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Golbat | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Donphan | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Onix | 15% (Lv 34–36) | 15% (Lv 34–36) | 15% (Lv 34–36) |
| Rhyhorn | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |

Special: Land swarm: Graveler; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Victory Road 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Golbat | 30% (Lv 32) | 30% (Lv 32) | 30% (Lv 32) |
| Donphan | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Onix | 15% (Lv 34–36) | 15% (Lv 34–36) | 15% (Lv 34–36) |
| Rhyhorn | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 80% | 24–32 |
| Graveler | 20% | 30–33 |

Special: Land swarm: Graveler; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 2 North Above Viridian Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Caterpie | 31% (Lv 3–4) | 31% (Lv 3–4) | – |
| Pidgey | 30% (Lv 3) | 50% (Lv 3–5) | – |
| Metapod | 20% (Lv 5) | – | – |
| Butterfree | 10% (Lv 7–8) | 10% (Lv 7–8) | – |
| Pidgeotto | 5% (Lv 7) | 9% (Lv 7–10) | – |
| Spinarak | 4% (Lv 10) | – | 31% (Lv 3–4) |
| Hoothoot | – | – | 50% (Lv 3–5) |
| Noctowl | – | – | 14% (Lv 7–10) |
| Ariados | – | – | 5% (Lv 7) |

Special: Land swarm: Caterpie; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Viridian Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Caterpie | 40% (Lv 3) | 40% (Lv 3) | – |
| Metapod | 30% (Lv 3–5) | 30% (Lv 3–5) | – |
| Pidgey | 10% (Lv 3) | 15% (Lv 3–7) | – |
| Butterfree | 10% (Lv 7) | – | – |
| Pidgeotto | 4% (Lv 7) | 9% (Lv 7) | – |
| Pikachu | 6% (Lv 4–7) | 6% (Lv 4–7) | 5% (Lv 4) |
| Hoothoot | – | – | 80% (Lv 3–5) |
| Noctowl | – | – | 15% (Lv 7) |

Special: Land swarm: Kricketot; Hoenn Sound: Spoink, Numel; Sinnoh Sound: Budew, Carnivine

## Cerulean Cave 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Machoke | 24% (Lv 39–40) | 24% (Lv 39–40) | 6% (Lv 39–40) |
| Parasect | 20% (Lv 38) | 20% (Lv 38) | 10% (Lv 38) |
| Golbat | 10% (Lv 38) | 10% (Lv 38) | 50% (Lv 38–39) |
| Primeape | 14% (Lv 38–39) | 14% (Lv 38–39) | 4% (Lv 39) |
| Magneton | 11% (Lv 39–40) | 11% (Lv 39–40) | 10% (Lv 40) |
| Ditto | 11% (Lv 39–40) | 11% (Lv 39–40) | 10% (Lv 39) |
| Electrode | 5% (Lv 40) | 5% (Lv 40) | 5% (Lv 40) |
| Wobbuffet | 5% (Lv 37) | 5% (Lv 37) | 5% (Lv 37) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 35–40 |
| Golduck | 10% | 40 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 80% | 22–24 |
| Graveler | 20% | 26–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 45% | 20 |
| Goldeen | 40% | 20 |
| Magikarp | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 40 |
| Poliwhirl | 30% | 40 |
| Gyarados | 30% | 40 |

Special: Land swarm: Golbat; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Cerulean Cave B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Kadabra | 20% (Lv 42) | 20% (Lv 42) | 20% (Lv 42) |
| Parasect | 20% (Lv 40) | 20% (Lv 40) | 20% (Lv 40) |
| Golbat | 10% (Lv 41) | 10% (Lv 41) | 20% (Lv 41–42) |
| Machoke | 20% (Lv 39–42) | 20% (Lv 39–42) | 10% (Lv 39) |
| Magneton | 10% (Lv 41) | 10% (Lv 41) | 10% (Lv 41) |
| Ditto | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Electrode | 5% (Lv 41) | 5% (Lv 41) | 5% (Lv 41) |
| Wobbuffet | 5% (Lv 42) | 5% (Lv 42) | 5% (Lv 42) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 35–40 |
| Golduck | 10% | 40 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 45% | 20 |
| Goldeen | 40% | 20 |
| Magikarp | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 40 |
| Poliwhirl | 30% | 40 |
| Gyarados | 30% | 40 |

Special: Land swarm: Kadabra; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Cerulean Cave B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Kadabra | 20% (Lv 46) | 20% (Lv 46) | 20% (Lv 46) |
| Parasect | 25% (Lv 45–47) | 25% (Lv 45–47) | 25% (Lv 45–47) |
| Golbat | 10% (Lv 47) | 10% (Lv 47) | 10% (Lv 47) |
| Machoke | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Magneton | 15% (Lv 45–47) | 15% (Lv 45–47) | 15% (Lv 45–47) |
| Ditto | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Electrode | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |
| Wobbuffet | 5% (Lv 49) | 5% (Lv 49) | 5% (Lv 49) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 35–40 |
| Golduck | 10% | 40 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 80% | 22–24 |
| Graveler | 20% | 26–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 45% | 20 |
| Goldeen | 40% | 20 |
| Magikarp | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 40 |
| Poliwhirl | 30% | 40 |
| Gyarados | 30% | 40 |

Special: Land swarm: Kadabra; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling
