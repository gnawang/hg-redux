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
| Magikarp | 40% | 10 |
| Shellder | 45% | 10 |
| Chinchou | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Shellder | 40% | 20 |
| Chinchou | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Shellder | 40% | 40 |
| Lanturn | 30% | 40 |
| Gyarados | 30% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Lanturn

## Route 29

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 30% (Lv 3–4) | 30% (Lv 3–4) | – |
| Sentret | 20% (Lv 3) | 20% (Lv 3) | – |
| Rattata | 20% (Lv 3–4) | 20% (Lv 3–4) | 40% (Lv 3–4) |
| Hoppip | 10% (Lv 3) | 10% (Lv 3) | – |
| Starly | 5% (Lv 4) | 5% (Lv 4) | – |
| Zigzagoon | 5% (Lv 4) | 5% (Lv 4) | 5% (Lv 4) |
| Bidoof | 5% (Lv 5) | 5% (Lv 5) | 5% (Lv 5) |
| Wurmple | 5% (Lv 5) | 5% (Lv 5) | 5% (Lv 5) |
| Hoothoot | – | – | 40% (Lv 3–4) |
| Poochyena | – | – | 5% (Lv 4) |

Special: Land swarm: Pidgey; Hoenn Sound: Furret, Raticate; Sinnoh Sound: Plusle, Minun

## Cherrygrove City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Marill | 95% | 10–25 |
| Azumarill | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Krabby | 35% | 10 |
| Corphish | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 50% | 20 |
| Magikarp | 30% | 20 |
| Finneon | 15% | 20 |
| Corphish | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Kingler | 50% | 40 |
| Krabby | 30% | 40 |
| Lumineon | 15% | 40 |
| Crawdaunt | 5% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Kingler

## Route 30

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Ledyba | 20% (Lv 4) | – | – |
| Caterpie | 20% (Lv 4) | 20% (Lv 4) | 10% (Lv 4) |
| Weedle | 10% (Lv 4) | 20% (Lv 4) | 10% (Lv 4) |
| Pidgey | 10% (Lv 4) | – | – |
| Taillow | 10% (Lv 5) | 5% (Lv 5) | – |
| Lotad | 10% (Lv 5) | 10% (Lv 5) | 10% (Lv 5) |
| Seedot | 5% (Lv 5) | 5% (Lv 5) | 5% (Lv 5) |
| Kricketot | 5% (Lv 5) | – | 5% (Lv 5) |
| Surskit | 5% (Lv 6) | 5% (Lv 6) | 5% (Lv 6) |
| Ralts | 5% (Lv 6) | 5% (Lv 6) | 5% (Lv 6) |
| Metapod | – | 10% (Lv 4) | – |
| Kakuna | – | 20% (Lv 4–5) | – |
| Spinarak | – | – | 30% (Lv 4–5) |
| Hoothoot | – | – | 20% (Lv 4) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 60% | 15–25 |
| Poliwhirl | 30% | 10–20 |
| Lotad | 5% | 15–25 |
| Lombre | 5% | 15–32 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 10 |
| Goldeen | 30% | 10 |
| Psyduck | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 40% | 20 |
| Goldeen | 30% | 20 |
| Poliwhirl | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 40% | 40 |
| Seaking | 30% | 40 |
| Golduck | 30% | 40 |

Special: Land swarm: Pidgey; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Lombre, Nuzleaf; Sinnoh Sound: Ralts, Ralts

## Route 31

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Ledyba | 20% (Lv 6) | – | – |
| Bellsprout | 20% (Lv 6) | 20% (Lv 6) | 20% (Lv 6) |
| Buizel | 10% (Lv 6) | 10% (Lv 8) | 5% (Lv 9–10) |
| Shinx | 10% (Lv 7) | 5% (Lv 8) | 10% (Lv 6) |
| Abra | 10% (Lv 7) | 20% (Lv 6) | 10% (Lv 7) |
| Natu | 10% (Lv 8) | 10% (Lv 6) | 10% (Lv 8) |
| Exeggcute | 5% (Lv 8) | – | 5% (Lv 8) |
| Psyduck | 5% (Lv 8) | 10% (Lv 7) | 10% (Lv 7) |
| Metapod | 5% (Lv 9–10) | – | 5% (Lv 8) |
| Kakuna | 5% (Lv 9–10) | – | 5% (Lv 9–10) |
| Wurmple | – | 10% (Lv 7) | – |
| Budew | – | 5% (Lv 8) | – |
| Silcoon | – | 5% (Lv 9–10) | – |
| Cascoon | – | 5% (Lv 9–10) | – |
| Spinarak | – | – | 20% (Lv 6) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Marill | 60% | 15–25 |
| Poliwag | 30% | 10–20 |
| Surskit | 5% | 15–25 |
| Masquerain | 5% | 15–32 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 55% | 10 |
| Tentacool | 30% | 10 |
| Feebas | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 50% | 20 |
| Slowpoke | 35% | 20 |
| Feebas | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacruel | 40% | 40 |
| Slowbro | 45% | 40 |
| Feebas | 15% | 40 |

Special: Land swarm: Pidgey; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Feebas; Hoenn Sound: Butterfree, Beedrill; Sinnoh Sound: Budew, Budew

## Violet City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10–25 |
| Poliwhirl | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Poliwag | 30% | 10 |
| Staryu | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 20 |
| Staryu | 30% | 20 |
| Chinchou | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 40% | 40 |
| Staryu | 30% | 40 |
| Lanturn | 30% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Whiscash; Night fishing: Staryu

## Sprout Tower 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 30% (Lv 9) | 30% (Lv 9) | 20% (Lv 9) |
| Pidgey | 30% (Lv 9–10) | 30% (Lv 9–10) | – |
| Zigzagoon | 10% (Lv 10) | 10% (Lv 10) | – |
| Bidoof | 10% (Lv 10) | 10% (Lv 10) | 10% (Lv 10) |
| Starly | 5% (Lv 11) | 5% (Lv 11) | – |
| Meditite | 5% (Lv 11) | 5% (Lv 11) | – |
| Spinda | 5% (Lv 11–12) | 5% (Lv 11–12) | 5% (Lv 11–12) |
| Chatot | 5% (Lv 12) | 5% (Lv 12) | – |
| Gastly | – | – | 30% (Lv 9–10) |
| Bellsprout | – | – | 20% (Lv 9–10) |
| Glameow | – | – | 5% (Lv 11) |
| Stunky | – | – | 5% (Lv 11) |
| Drifloon | – | – | 5% (Lv 12) |

Special: Land swarm: Rattata; Hoenn Sound: Bibarel, Linoone; Sinnoh Sound: Spinda, Spinda

## Sprout Tower 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 30% (Lv 10) | 30% (Lv 10) | 20% (Lv 10) |
| Pidgey | 30% (Lv 10–11) | 30% (Lv 10–11) | – |
| Zigzagoon | 10% (Lv 11) | 10% (Lv 11) | – |
| Bidoof | 10% (Lv 11) | 10% (Lv 11) | 10% (Lv 11) |
| Starly | 5% (Lv 12) | 5% (Lv 12) | – |
| Meditite | 5% (Lv 12) | 5% (Lv 12) | – |
| Spinda | 5% (Lv 12–13) | 5% (Lv 12–13) | 5% (Lv 12–13) |
| Chatot | 5% (Lv 13) | 5% (Lv 13) | – |
| Gastly | – | – | 30% (Lv 10–11) |
| Bellsprout | – | – | 20% (Lv 10–11) |
| Glameow | – | – | 5% (Lv 12) |
| Stunky | – | – | 5% (Lv 12) |
| Drifloon | – | – | 5% (Lv 13) |

Special: Land swarm: Rattata; Hoenn Sound: Bibarel, Linoone; Sinnoh Sound: Spinda, Spinda

## Route 32

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Mareep | 25% (Lv 10–11) | 25% (Lv 10–11) | 25% (Lv 10–11) |
| Bellsprout | 20% (Lv 10) | 20% (Lv 10) | 20% (Lv 10) |
| Nincada | 10% (Lv 10) | 10% (Lv 10) | 10% (Lv 10) |
| Pachirisu | 10% (Lv 10) | 10% (Lv 10) | – |
| Hoppip | 15% (Lv 11–12) | 15% (Lv 11–12) | – |
| Magnemite | 15% (Lv 11–12) | 15% (Lv 11–12) | 15% (Lv 11–12) |
| Ekans | 5% (Lv 11) | 5% (Lv 11) | 5% (Lv 11) |
| Drifloon | – | – | 10% (Lv 10) |
| Wooper | – | – | 15% (Lv 11–12) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Tentacool | 30% | 15–25 |
| Quagsire | 5% | 15–25 |
| Tentacruel | 5% | 15–36 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 40% | 10 |
| Psyduck | 45% | 10 |
| Qwilfish | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 40% | 20 |
| Psyduck | 30% | 20 |
| Qwilfish | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Qwilfish | 40% | 40 |
| Tentacruel | 30% | 40 |
| Golduck | 30% | 40 |

Special: Land swarm: Bellsprout; Surf swarm: Tentacool; Fishing swarm: Qwilfish; Night fishing: Tentacruel; Hoenn Sound: Flaaffy, Magneton; Sinnoh Sound: Drifloon, Pachirisu

## Ruins of Alph Outside

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Natu | 40% (Lv 26) | 40% (Lv 26) | 40% (Lv 26) |
| Smeargle | 40% (Lv 26–28) | 40% (Lv 26–28) | 40% (Lv 26–28) |
| Girafarig | 20% (Lv 28–30) | 20% (Lv 28–30) | 20% (Lv 28–30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 90% | 10–25 |
| Quagsire | 10% | 10–20 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 80% | 8–14 |
| Nosepass | 20% | 3–6 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Remoraid | 30% | 10 |
| Dratini | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Remoraid | 30% | 20 |
| Dratini | 25% | 20 |
| Dragonair | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 40% | 40 |
| Dragonair | 30% | 40 |
| Relicanth | 15% | 40 |
| Octillery | 15% | 40 |

Special: Land swarm: Natu; Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Relicanth; Hoenn Sound: Xatu, Xatu; Sinnoh Sound: Togepi, Togepi

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
| Zubat | 25% (Lv 12–14) | 25% (Lv 12–14) | 25% (Lv 12–14) |
| Sandshrew | 25% (Lv 12–14) | 25% (Lv 12–14) | 25% (Lv 12–14) |
| Whismur | 10% (Lv 12) | 10% (Lv 12) | 10% (Lv 12) |
| Geodude | 10% (Lv 13) | 10% (Lv 13) | 10% (Lv 13) |
| Machop | 10% (Lv 13) | 10% (Lv 13) | 10% (Lv 13) |
| Cubone | 10% (Lv 13) | 10% (Lv 13) | 10% (Lv 13) |
| Makuhita | 5% (Lv 14–15) | 5% (Lv 14–15) | 5% (Lv 14–15) |
| Aron | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Quagsire | 30% | 15–25 |
| Shellos | 5% | 10–20 |
| Gastrodon | 5% | 10–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Goldeen | 35% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Goldeen | 35% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 50% | 40 |
| Seaking | 35% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Geodude; Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Sandslash, Loudred; Sinnoh Sound: Gible, Gible

## Union Cave B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 13–14) | 30% (Lv 13–14) | 30% (Lv 13–14) |
| Sandshrew | 20% (Lv 13) | 20% (Lv 13) | 20% (Lv 13) |
| Onix | 20% (Lv 13–14) | 20% (Lv 13–14) | 20% (Lv 13–14) |
| Geodude | 10% (Lv 14) | 10% (Lv 14) | 10% (Lv 14) |
| Bronzor | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Aron | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Bagon | 5% (Lv 15–16) | 5% (Lv 15–16) | 5% (Lv 15–16) |
| Gible | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Quagsire | 30% | 15–25 |
| Shellos | 5% | 10–20 |
| Gastrodon | 5% | 10–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Goldeen | 35% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Goldeen | 35% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 50% | 40 |
| Seaking | 35% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Geodude; Surf swarm: Wooper; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Golbat, Steelix; Sinnoh Sound: Cubone, Cubone

## Union Cave B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 28–29) | 25% (Lv 28–29) | 25% (Lv 28–29) |
| Sandslash | 20% (Lv 28) | 20% (Lv 28) | 20% (Lv 28) |
| Sableye | 10% (Lv 28) | 10% (Lv 28) | 10% (Lv 28) |
| Graveler | 10% (Lv 28) | 10% (Lv 28) | 10% (Lv 28) |
| Machoke | 10% (Lv 29) | 10% (Lv 29) | 10% (Lv 29) |
| Lickitung | 10% (Lv 29) | 10% (Lv 29) | 10% (Lv 29) |
| Kangaskhan | 5% (Lv 29) | 5% (Lv 29) | 5% (Lv 29) |
| Loudred | 5% (Lv 30) | 5% (Lv 30) | 5% (Lv 30) |
| Mawile | 5% (Lv 30) | 5% (Lv 30) | 5% (Lv 30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Quagsire | 30% | 15–25 |
| Shellos | 5% | 15–25 |
| Gastrodon | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Goldeen | 35% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Goldeen | 35% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 50% | 40 |
| Seaking | 35% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Zubat; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Lickilicky, Exploud; Sinnoh Sound: Kangaskhan, Kangaskhan

## Route 33

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Ekans | 20% (Lv 14) | 20% (Lv 14) | 20% (Lv 14) |
| Aipom | 20% (Lv 14) | 20% (Lv 14) | 20% (Lv 14) |
| Hoppip | 20% (Lv 14–15) | 20% (Lv 14–15) | – |
| Rhyhorn | 20% (Lv 14–15) | 20% (Lv 14–15) | 20% (Lv 14–15) |
| Croagunk | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Skorupi | 5% (Lv 15) | 5% (Lv 15) | 5% (Lv 15) |
| Slakoth | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |
| Swablu | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |
| Meowth | – | – | 20% (Lv 14–15) |

Special: Land swarm: Hoppip; Hoenn Sound: Toxicroak, Drapion; Sinnoh Sound: Lombre, Lombre

## Slowpoke Well 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 25% (Lv 15–16) | 25% (Lv 15–16) | 25% (Lv 15–16) |
| Slowpoke | 25% (Lv 15–16) | 25% (Lv 15–16) | 25% (Lv 15–16) |
| Shellos | 10% (Lv 15) | 10% (Lv 15) | 10% (Lv 15) |
| Gastly | 10% (Lv 15) | 10% (Lv 15) | 10% (Lv 15) |
| Shellder | 10% (Lv 15) | 10% (Lv 15) | 10% (Lv 15) |
| Swinub | 10% (Lv 15) | 10% (Lv 15) | 10% (Lv 15) |
| Snorunt | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |
| Bronzor | 5% (Lv 16) | 5% (Lv 16) | 5% (Lv 16) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 90% | 10–25 |
| Slowbro | 10% | 5–15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Slowpoke | 35% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Slowpoke | 45% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 40% | 40 |
| Slowbro | 45% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Zubat; Surf swarm: Slowpoke; Fishing swarm: Magikarp; Night fishing: Whiscash; Hoenn Sound: Slowbro, Slowbro; Sinnoh Sound: Wynaut, Wynaut

## Slowpoke Well B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 28–31) | 25% (Lv 28–31) | 25% (Lv 28–31) |
| Slowpoke | 25% (Lv 28–31) | 25% (Lv 28–31) | 25% (Lv 28–31) |
| Gastrodon | 10% (Lv 29) | 10% (Lv 29) | 10% (Lv 29) |
| Haunter | 10% (Lv 29) | 10% (Lv 29) | 10% (Lv 29) |
| Shellder | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Piloswine | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Snorunt | 5% (Lv 32–33) | 5% (Lv 32–33) | 5% (Lv 32–33) |
| Bronzong | 5% (Lv 32–33) | 5% (Lv 32–33) | 5% (Lv 32–33) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 60% | 10–20 |
| Slowbro | 40% | 15–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Slowpoke | 35% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Slowpoke | 45% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 40% | 40 |
| Slowbro | 45% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Zubat; Surf swarm: Slowpoke; Fishing swarm: Magikarp; Night fishing: Whiscash; Hoenn Sound: Slowbro, Glalie; Sinnoh Sound: Wobbuffet, Wobbuffet

## Ilex Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Ledyba | 20% (Lv 15) | – | – |
| Pineco | 20% (Lv 15) | 20% (Lv 15) | 10% (Lv 16) |
| Exeggcute | 10% (Lv 15) | 20% (Lv 15) | – |
| Pikachu | 10% (Lv 16) | 10% (Lv 15) | 5% (Lv 17) |
| Butterfree | 10% (Lv 16) | – | – |
| Beedrill | 10% (Lv 16) | – | – |
| Shroomish | 5% (Lv 17) | 10% (Lv 16) | – |
| Buneary | 5% (Lv 17) | 10% (Lv 16) | 10% (Lv 15) |
| Budew | 5% (Lv 17–18) | 5% (Lv 17) | – |
| Roselia | 5% (Lv 18) | 5% (Lv 18) | – |
| Wurmple | – | 10% (Lv 16) | – |
| Beautifly | – | 5% (Lv 17) | – |
| Dustox | – | 5% (Lv 17–18) | – |
| Paras | – | – | 20% (Lv 15) |
| Spinarak | – | – | 20% (Lv 15) |
| Oddish | – | – | 10% (Lv 16) |
| Venonat | – | – | 10% (Lv 16) |
| Murkrow | – | – | 5% (Lv 17) |
| Misdreavus | – | – | 5% (Lv 17–18) |
| Carnivine | – | – | 5% (Lv 18) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 5–20 |
| Golduck | 10% | 10–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Poliwag | 60% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 70% | 20 |
| Gyarados | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 40% | 40 |
| Gyarados | 30% | 40 |
| Poliwrath | 15% | 40 |
| Politoed | 15% | 40 |

Special: Land swarm: Caterpie; Surf swarm: Psyduck; Fishing swarm: Magikarp; Night fishing: Gyarados; Hoenn Sound: Gloom, Venomoth; Sinnoh Sound: Pichu, Pichu

## Route 34

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Drowzee | 20% (Lv 15) | 20% (Lv 15) | 20% (Lv 15) |
| Bonsly | 20% (Lv 15) | 20% (Lv 15) | 20% (Lv 15) |
| Gulpin | 10% (Lv 15) | 10% (Lv 15) | 10% (Lv 15) |
| Electrike | 10% (Lv 16) | 10% (Lv 16) | 10% (Lv 16) |
| Mime Jr. | 10% (Lv 16) | 10% (Lv 16) | 10% (Lv 16) |
| Abra | 10% (Lv 17) | 10% (Lv 17) | 10% (Lv 17) |
| Ditto | 10% (Lv 17–19) | 10% (Lv 17–19) | 10% (Lv 17–19) |
| Snubbull | 10% (Lv 17–19) | 10% (Lv 17–19) | 10% (Lv 17–19) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 95% | 10–25 |
| Tentacruel | 5% | 15–29 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 10 |
| Chinchou | 30% | 10 |
| Staryu | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 20 |
| Chinchou | 30% | 20 |
| Staryu | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 40% | 40 |
| Staryu | 30% | 40 |
| Lanturn | 15% | 40 |
| Starmie | 15% | 40 |

Special: Land swarm: Kadabra; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu; Hoenn Sound: Manectric, Hypno; Sinnoh Sound: Ralts, Kirlia

## Route 35

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Nidoran♂ | 20% (Lv 17) | 20% (Lv 17) | 20% (Lv 17) |
| Nidoran♀ | 20% (Lv 17) | 20% (Lv 17) | 20% (Lv 17) |
| Pidgeotto | 10% (Lv 17) | 10% (Lv 17) | – |
| Ditto | 10% (Lv 17) | 10% (Lv 17) | 10% (Lv 18) |
| Yanma | 10% (Lv 18) | 10% (Lv 18) | 10% (Lv 18) |
| Stunky | 10% (Lv 18) | 10% (Lv 18) | 5% (Lv 18) |
| Glameow | 5% (Lv 18) | 5% (Lv 18) | 5% (Lv 18) |
| Staravia | 5% (Lv 18) | 5% (Lv 18) | – |
| Illumise | 5% (Lv 19) | 5% (Lv 19) | 5% (Lv 19) |
| Volbeat | 5% (Lv 19) | 5% (Lv 19) | 5% (Lv 19) |
| Meowth | – | – | 10% (Lv 17) |
| Noctowl | – | – | 10% (Lv 17) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 90% | 10–25 |
| Golduck | 10% | 15–31 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 55% | 10 |
| Psyduck | 45% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Psyduck | 35% | 20 |
| Luvdisc | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 50% | 40 |
| Gyarados | 35% | 40 |
| Luvdisc | 15% | 40 |

Special: Land swarm: Illumise; Surf swarm: Psyduck; Fishing swarm: Magikarp; Night fishing: Psyduck; Hoenn Sound: Skuntank, Purugly; Sinnoh Sound: Yanma, Yanma

## National Park

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Metapod | 20% (Lv 17) | 20% (Lv 17) | 20% (Lv 17) |
| Kakuna | 20% (Lv 17) | 20% (Lv 17) | 20% (Lv 17) |
| Scyther | 10% (Lv 17) | 10% (Lv 17) | 10% (Lv 17) |
| Pinsir | 10% (Lv 17) | 10% (Lv 18) | 10% (Lv 17) |
| Heracross | 10% (Lv 18) | 10% (Lv 18) | 10% (Lv 18) |
| Combee | 10% (Lv 18) | 5% (Lv 18) | 10% (Lv 18) |
| Taillow | 5% (Lv 18) | 5% (Lv 18) | – |
| Nincada | 5% (Lv 18) | – | 5% (Lv 18) |
| Burmy | 5% (Lv 19) | 5% (Lv 19) | 5% (Lv 19) |
| Kricketune | 5% (Lv 19) | 5% (Lv 19) | 5% (Lv 19) |
| Sunkern | – | 10% (Lv 17) | – |
| Poochyena | – | – | 5% (Lv 18) |

Special: Land swarm: Caterpie; Hoenn Sound: Butterfree, Beedrill; Sinnoh Sound: Scyther, Heracross

## Route 36

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Growlithe | 20% (Lv 17) | 20% (Lv 17) | 20% (Lv 17) |
| Vulpix | 20% (Lv 17) | 20% (Lv 17) | 20% (Lv 17) |
| Nidorino | 10% (Lv 17) | 10% (Lv 17) | 10% (Lv 17) |
| Nidorina | 20% (Lv 17–18) | 20% (Lv 17–18) | 15% (Lv 18) |
| Stantler | 10% (Lv 18) | 10% (Lv 18) | 5% (Lv 18) |
| Combee | 5% (Lv 18) | 5% (Lv 18) | 10% (Lv 17) |
| Plusle | 5% (Lv 18) | 5% (Lv 18) | 5% (Lv 19) |
| Minun | 5% (Lv 19) | 5% (Lv 19) | 5% (Lv 19) |
| Staravia | 5% (Lv 19) | 5% (Lv 19) | – |
| Noctowl | – | – | 10% (Lv 18) |

Special: Land swarm: Nidoran♂; Hoenn Sound: Vespiquen, Vespiquen; Sinnoh Sound: Bonsly, Mime Jr.

## Route 37

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Growlithe | 20% (Lv 21) | 20% (Lv 21) | 30% (Lv 21–22) |
| Vulpix | 20% (Lv 21) | 20% (Lv 21) | 20% (Lv 21) |
| Stantler | 10% (Lv 21) | 10% (Lv 21) | 10% (Lv 21) |
| Ledian | 10% (Lv 22) | 10% (Lv 22) | – |
| Pidgeotto | 10% (Lv 22) | 10% (Lv 22) | – |
| Nidorino | 10% (Lv 22) | 10% (Lv 22) | – |
| Nidorina | 10% (Lv 23) | 10% (Lv 23) | – |
| Zangoose | 5% (Lv 23–24) | 5% (Lv 23–24) | 5% (Lv 23–24) |
| Seviper | 5% (Lv 24) | 5% (Lv 24) | 5% (Lv 24) |
| Ariados | – | – | 10% (Lv 22) |
| Noctowl | – | – | 10% (Lv 22) |
| Mightyena | – | – | 5% (Lv 23) |
| Linoone | – | – | 5% (Lv 23) |

Special: Land swarm: Pidgey; Hoenn Sound: Arcanine, Ninetales; Sinnoh Sound: Zangoose, Seviper

## Ecruteak City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 90% | 10–25 |
| Poliwhirl | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Poliwag | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 40% | 40 |
| Gyarados | 60% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Gyarados

## Burned Tower 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Rattata | 25% (Lv 22–23) | 25% (Lv 22–23) | 25% (Lv 22–23) |
| Koffing | 25% (Lv 22–23) | 25% (Lv 22–23) | 25% (Lv 22–23) |
| Zigzagoon | 10% (Lv 22) | 10% (Lv 22) | 10% (Lv 22) |
| Cubone | 10% (Lv 22) | 10% (Lv 22) | 10% (Lv 22) |
| Magby | 10% (Lv 22) | 10% (Lv 22) | 10% (Lv 22) |
| Grimer | 10% (Lv 22) | 10% (Lv 22) | 10% (Lv 22) |
| Duskull | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |
| Shuppet | 5% (Lv 23) | 5% (Lv 23) | 5% (Lv 23) |

Special: Land swarm: Rattata; Hoenn Sound: Raticate, Marowak; Sinnoh Sound: Chimecho, Chimecho

## Burned Tower B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Raticate | 25% (Lv 23–24) | 25% (Lv 23–24) | 25% (Lv 23–24) |
| Koffing | 25% (Lv 23–24) | 25% (Lv 23–24) | 25% (Lv 23–24) |
| Linoone | 10% (Lv 23) | 10% (Lv 23) | 10% (Lv 23) |
| Cubone | 10% (Lv 23) | 10% (Lv 23) | 10% (Lv 23) |
| Magby | 10% (Lv 23) | 10% (Lv 23) | 10% (Lv 23) |
| Grimer | 10% (Lv 23) | 10% (Lv 23) | 10% (Lv 23) |
| Duskull | 5% (Lv 24) | 5% (Lv 24) | 5% (Lv 24) |
| Shuppet | 5% (Lv 24) | 5% (Lv 24) | 5% (Lv 24) |

Special: Land swarm: Rattata; Hoenn Sound: Weezing, Magmar; Sinnoh Sound: Chimecho, Chimecho

## Bell Tower 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Swinub | 25% (Lv 42–43) | 25% (Lv 42–43) | 25% (Lv 42–43) |
| Snover | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Spheal | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Seel | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |
| Smoochum | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Swinub | 25% (Lv 42–43) | 25% (Lv 42–43) | 25% (Lv 42–43) |
| Snover | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Spheal | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Seel | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |
| Smoochum | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 4F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 42–43) | 25% (Lv 42–43) | 25% (Lv 42–43) |
| Swinub | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Spheal | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Shellder | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Seel | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |
| Smoochum | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Delibird | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 5F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 42–43) | 25% (Lv 42–43) | 25% (Lv 42–43) |
| Swinub | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Spheal | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Shellder | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Seel | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |
| Smoochum | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Delibird | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 6F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 42–43) | 25% (Lv 42–43) | 25% (Lv 42–43) |
| Swinub | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Spheal | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Shellder | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Seel | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |
| Smoochum | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Delibird | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 7F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Piloswine | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Sealeo | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Snorunt | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Dewgong | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Jynx | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Delibird | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 8F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Piloswine | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Sealeo | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Snorunt | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Dewgong | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Jynx | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Delibird | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Bell Tower 9F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Piloswine | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Sealeo | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Snorunt | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Dewgong | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Jynx | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Delibird | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Route 38

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Doduo | 20% (Lv 26) | 20% (Lv 26) | – |
| Magnemite | 20% (Lv 26) | 20% (Lv 26) | 20% (Lv 26) |
| Luxio | 10% (Lv 26) | 10% (Lv 26) | 10% (Lv 26) |
| Cherubi | 10% (Lv 26) | 10% (Lv 26) | – |
| Mankey | 10% (Lv 26) | 10% (Lv 26) | 10% (Lv 26) |
| Voltorb | 10% (Lv 26) | 10% (Lv 26) | 10% (Lv 26) |
| Elekid | 5% (Lv 27) | 5% (Lv 27) | 5% (Lv 27) |
| Farfetch’d | 5% (Lv 27) | 5% (Lv 27) | 5% (Lv 27) |
| Miltank | 5% (Lv 27) | 5% (Lv 27) | 5% (Lv 27) |
| Tauros | 5% (Lv 27) | 5% (Lv 27) | 5% (Lv 27) |
| Meowth | – | – | 20% (Lv 26) |
| Skitty | – | – | 10% (Lv 26) |

Special: Land swarm: Farfetch’d; Hoenn Sound: Dodrio, Electabuzz; Sinnoh Sound: Skitty, Cherubi

## Route 39

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Raticate | 20% (Lv 27) | 20% (Lv 27) | 20% (Lv 27) |
| Ponyta | 20% (Lv 27) | 20% (Lv 27) | 20% (Lv 27) |
| Cherubi | 10% (Lv 27) | 10% (Lv 27) | – |
| Elekid | 10% (Lv 27) | 10% (Lv 27) | 10% (Lv 27) |
| Mankey | 10% (Lv 27) | 10% (Lv 27) | 10% (Lv 27) |
| Voltorb | 10% (Lv 27) | 10% (Lv 27) | 10% (Lv 27) |
| Farfetch’d | 5% (Lv 28) | 5% (Lv 28) | 5% (Lv 28) |
| Miltank | 5% (Lv 28) | 5% (Lv 28) | 5% (Lv 28) |
| Tauros | 5% (Lv 28) | 5% (Lv 28) | 5% (Lv 28) |
| Pidgeotto | 5% (Lv 28) | 5% (Lv 28) | – |
| Meowth | – | – | 10% (Lv 27) |
| Skitty | – | – | 5% (Lv 28) |

Special: Land swarm: Rattata; Hoenn Sound: Rapidash, Primeape; Sinnoh Sound: Skitty, Cherubi

## Olivine City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 65% | 15–25 |
| Tentacruel | 30% | 10–20 |
| Wingull | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Staryu | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Staryu | 30% | 20 |
| Chinchou | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Staryu | 40% | 40 |
| Chinchou | 30% | 40 |
| Lanturn | 15% | 40 |
| Gyarados | 15% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Chinchou

## Route 40

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 15–25 |
| Tentacruel | 30% | 10–20 |
| Wingull | 5% | 15–25 |
| Pelipper | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Tentacool | 60% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Staryu | 50% | 20 |
| Corsola | 35% | 20 |
| Finneon | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Corsola | 50% | 40 |
| Krabby | 30% | 40 |
| Finneon | 15% | 40 |
| Lumineon | 5% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Corsola

## Route 41

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Mantyke | 60% | 15–25 |
| Mantine | 30% | 15–25 |
| Tentacruel | 5% | 15–25 |
| Wingull | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Tentacool | 30% | 10 |
| Horsea | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 40% | 20 |
| Chinchou | 30% | 20 |
| Wailmer | 15% | 20 |
| Corsola | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seadra | 40% | 40 |
| Corsola | 30% | 40 |
| Lanturn | 20% | 40 |
| Wailord | 10% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Corsola

## Whirl Islands 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Spheal | 20% (Lv 34) | 20% (Lv 34) | 20% (Lv 34) |
| Krabby | 25% (Lv 34–35) | 25% (Lv 34–35) | 25% (Lv 34–35) |
| Seel | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Psyduck | 15% (Lv 34–35) | 15% (Lv 34–35) | 15% (Lv 34–35) |
| Golbat | 15% (Lv 35–36) | 15% (Lv 35–36) | 15% (Lv 35–36) |
| Shellder | 15% (Lv 35–36) | 15% (Lv 35–36) | 15% (Lv 35–36) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 90% | 10–25 |
| Seadra | 10% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 100% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 40% | 40 |
| Seadra | 60% | 40 |

Special: Land swarm: Krabby; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Seadra; Hoenn Sound: Kingler, Dewgong; Sinnoh Sound: Staryu, Staryu

## Whirl Islands B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Spheal | 20% (Lv 35) | 20% (Lv 35) | 20% (Lv 35) |
| Krabby | 25% (Lv 35–37) | 25% (Lv 35–37) | 25% (Lv 35–37) |
| Seel | 10% (Lv 35) | 10% (Lv 35) | 10% (Lv 35) |
| Shellder | 15% (Lv 36–37) | 15% (Lv 36–37) | 15% (Lv 36–37) |
| Golbat | 15% (Lv 36–38) | 15% (Lv 36–38) | 15% (Lv 36–38) |
| Golduck | 15% (Lv 36–38) | 15% (Lv 36–38) | 15% (Lv 36–38) |

Special: Land swarm: Krabby; Hoenn Sound: Kingler, Dewgong; Sinnoh Sound: Staryu, Staryu

## Whirl Islands B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Spheal | 20% (Lv 37) | 20% (Lv 37) | 20% (Lv 37) |
| Krabby | 25% (Lv 37–38) | 25% (Lv 37–38) | 25% (Lv 37–38) |
| Seel | 10% (Lv 37) | 10% (Lv 37) | 10% (Lv 37) |
| Shellder | 15% (Lv 37–38) | 15% (Lv 37–38) | 15% (Lv 37–38) |
| Golbat | 15% (Lv 38–39) | 15% (Lv 38–39) | 15% (Lv 38–39) |
| Golduck | 15% (Lv 38–39) | 15% (Lv 38–39) | 15% (Lv 38–39) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 90% | 15–25 |
| Seadra | 10% | 15–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 100% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Horsea | 40% | 40 |
| Seadra | 55% | 40 |
| Kingdra | 5% | 40 |

Special: Land swarm: Krabby; Surf swarm: Horsea; Fishing swarm: Magikarp; Night fishing: Seadra; Hoenn Sound: Sealeo, Dewgong; Sinnoh Sound: Staryu, Staryu

## Whirl Islands B3F Ledge Overlooking Lugia Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Sealeo | 20% (Lv 42) | 20% (Lv 42) | 20% (Lv 42) |
| Kingler | 25% (Lv 42–43) | 25% (Lv 42–43) | 25% (Lv 42–43) |
| Dewgong | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Shellder | 15% (Lv 42–43) | 15% (Lv 42–43) | 15% (Lv 42–43) |
| Golbat | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |
| Golduck | 15% (Lv 43–44) | 15% (Lv 43–44) | 15% (Lv 43–44) |

Special: Land swarm: Krabby; Hoenn Sound: Cloyster, Crobat; Sinnoh Sound: Staryu, Starmie

## Cianwood City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 15–25 |
| Tentacruel | 30% | 10–20 |
| Wingull | 5% | 15–25 |
| Pelipper | 5% | 15–25 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Shuckle | 80% | 15–24 |
| Kingler | 20% | 23–28 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Krabby | 35% | 10 |
| Carvanha | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 50% | 20 |
| Magikarp | 30% | 20 |
| Clamperl | 15% | 20 |
| Carvanha | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 40% | 40 |
| Corsola | 30% | 40 |
| Carvanha | 15% | 40 |
| Clamperl | 10% | 40 |
| Sharpedo | 5% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Clamperl

## Route 42

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Flaaffy | 25% (Lv 30–31) | 25% (Lv 30–31) | 25% (Lv 30–31) |
| Fearow | 20% (Lv 30) | 20% (Lv 30) | – |
| Hippopotas | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Arbok | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Sandslash | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Munchlax | 15% (Lv 31) | 15% (Lv 31) | 15% (Lv 31) |
| Cacnea | 5% (Lv 32) | 5% (Lv 32) | 5% (Lv 32) |
| Trapinch | 5% (Lv 32) | 5% (Lv 32) | 5% (Lv 32) |
| Golbat | – | – | 20% (Lv 30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 95% | 10–25 |
| Seaking | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 55% | 20 |
| Magikarp | 30% | 20 |
| Carvanha | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 40 |
| Seaking | 40% | 40 |
| Carvanha | 15% | 40 |
| Sharpedo | 5% | 40 |

Special: Land swarm: Mankey; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Carvanha; Hoenn Sound: Cacturne, Vibrava; Sinnoh Sound: Tyrogue, Tyrogue

## Mt. Mortar Waterfall Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 30% (Lv 31–34) | 30% (Lv 31–34) | 30% (Lv 31–34) |
| Golbat | 25% (Lv 31–33) | 25% (Lv 31–33) | 25% (Lv 31–33) |
| Lairon | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Meditite | 10% (Lv 32) | 10% (Lv 32) | 10% (Lv 32) |
| Rhyhorn | 10% (Lv 32) | 10% (Lv 32) | 10% (Lv 32) |
| Marill | 15% (Lv 32–34) | 15% (Lv 32–34) | 15% (Lv 32–34) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Marill | 95% | 10–25 |
| Azumarill | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 55% | 20 |
| Magikarp | 30% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 50% | 40 |
| Seaking | 30% | 40 |
| Barboach | 15% | 40 |
| Whiscash | 5% | 40 |

Special: Land swarm: Solrock; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Barboach; Hoenn Sound: Rhydon, Medicham; Sinnoh Sound: Azurill, Azurill

## Mt. Mortar Central Room

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Golbat | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Rhyhorn | 10% (Lv 33) | 10% (Lv 33) | 10% (Lv 33) |
| Marill | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Clefairy | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Lairon | 10% (Lv 35) | 10% (Lv 35) | 10% (Lv 35) |
| Hariyama | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |
| Medicham | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |
| Solrock | 5% (Lv 36–37) | 5% (Lv 36–37) | 5% (Lv 36–37) |
| Lunatone | 5% (Lv 36–37) | 5% (Lv 36–37) | 5% (Lv 36–37) |

Special: Land swarm: Geodude; Hoenn Sound: Rhydon, Azumarill; Sinnoh Sound: Cleffa, Clefairy

## Mt. Mortar Room Above Waterfall

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 20% (Lv 41) | 20% (Lv 41) | 20% (Lv 41) |
| Golbat | 20% (Lv 41) | 20% (Lv 41) | 20% (Lv 41) |
| Rhydon | 10% (Lv 41) | 10% (Lv 41) | 10% (Lv 41) |
| Azumarill | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Clefairy | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Lairon | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Hariyama | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |
| Medicham | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |
| Solrock | 5% (Lv 44–45) | 5% (Lv 44–45) | 5% (Lv 44–45) |
| Lunatone | 5% (Lv 44–45) | 5% (Lv 44–45) | 5% (Lv 44–45) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Marill | 95% | 15–30 |
| Azumarill | 5% | 20–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 55% | 20 |
| Magikarp | 30% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 50% | 40 |
| Seaking | 30% | 40 |
| Barboach | 15% | 40 |
| Whiscash | 5% | 40 |

Special: Land swarm: Graveler; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Barboach; Hoenn Sound: Golem, Clefable; Sinnoh Sound: Cleffa, Azurill

## Mt. Mortar B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Golbat | 20% (Lv 33) | 20% (Lv 33) | 20% (Lv 33) |
| Lairon | 10% (Lv 33) | 10% (Lv 33) | 10% (Lv 33) |
| Rhyhorn | 10% (Lv 33) | 10% (Lv 33) | 10% (Lv 33) |
| Machoke | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Clefairy | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Marill | 5% (Lv 34) | 5% (Lv 34) | 5% (Lv 34) |
| Pupitar | 5% (Lv 34) | 5% (Lv 34) | 5% (Lv 34) |
| Hariyama | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |
| Metang | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Marill | 95% | 10–25 |
| Azumarill | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 55% | 20 |
| Magikarp | 30% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 50% | 40 |
| Seaking | 30% | 40 |
| Barboach | 15% | 40 |
| Whiscash | 5% | 40 |

Special: Land swarm: Zubat; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Barboach; Hoenn Sound: Clefable, Azumarill; Sinnoh Sound: Riolu, Riolu

## Route 43

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgeotto | 30% (Lv 34–35) | 30% (Lv 34–35) | – |
| Girafarig | 20% (Lv 34) | 20% (Lv 34) | 20% (Lv 34) |
| Exeggcute | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Flaaffy | 10% (Lv 34) | 10% (Lv 34) | 10% (Lv 34) |
| Kirlia | 10% (Lv 35) | 10% (Lv 35) | 10% (Lv 35) |
| Swablu | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |
| Bibarel | 5% (Lv 35) | 5% (Lv 35) | 5% (Lv 35) |
| Linoone | 5% (Lv 36) | 5% (Lv 36) | 5% (Lv 36) |
| Manectric | 5% (Lv 36) | 5% (Lv 36) | 5% (Lv 36) |
| Venomoth | – | – | 30% (Lv 34–35) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 100% | 5–50 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 100% | 40 |

Special: Land swarm: Flaaffy; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Gyarados; Hoenn Sound: Altaria, Altaria; Sinnoh Sound: Happiny, Chansey

## Lake of Rage

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 5–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 85% | 10 |
| Feebas | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Gyarados | 35% | 20 |
| Feebas | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 40 |
| Gyarados | 40% | 40 |
| Feebas | 15% | 40 |
| Milotic | 5% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Feebas

## Route 44

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Tangela | 30% (Lv 38) | 30% (Lv 38) | 30% (Lv 38) |
| Lickitung | 20% (Lv 38) | 20% (Lv 38) | 20% (Lv 38) |
| Butterfree | 10% (Lv 38) | 10% (Lv 38) | 10% (Lv 38) |
| Beedrill | 10% (Lv 38) | 10% (Lv 38) | 10% (Lv 38) |
| Skiploom | 10% (Lv 38) | 10% (Lv 38) | – |
| Beautifly | 5% (Lv 39) | 5% (Lv 39) | – |
| Nuzleaf | 5% (Lv 39) | 5% (Lv 39) | 5% (Lv 39) |
| Cherrim | 5% (Lv 39) | 5% (Lv 39) | – |
| Altaria | 5% (Lv 39) | 5% (Lv 39) | 5% (Lv 39) |
| Venomoth | – | – | 10% (Lv 38) |
| Dustox | – | – | 5% (Lv 39) |
| Snover | – | – | 5% (Lv 39) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 60% | 20–30 |
| Poliwhirl | 30% | 15–25 |
| Lotad | 5% | 20–30 |
| Lombre | 5% | 20–30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 10 |
| Remoraid | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Remoraid | 60% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 40 |
| Remoraid | 30% | 40 |
| Gyarados | 20% | 40 |
| Octillery | 10% | 40 |

Special: Land swarm: Tangela; Surf swarm: Poliwag; Fishing swarm: Remoraid; Night fishing: Remoraid; Hoenn Sound: Tangrowth, Lickilicky; Sinnoh Sound: Combee, Lombre

## Ice Path 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 37–40) | 30% (Lv 37–40) | 30% (Lv 37–40) |
| Swinub | 25% (Lv 37–39) | 25% (Lv 37–39) | 25% (Lv 37–39) |
| Snover | 10% (Lv 37) | 10% (Lv 37) | 10% (Lv 37) |
| Spheal | 10% (Lv 38) | 10% (Lv 38) | 10% (Lv 38) |
| Seel | 15% (Lv 38–40) | 15% (Lv 38–40) | 15% (Lv 38–40) |
| Smoochum | 10% (Lv 38) | 10% (Lv 38) | 10% (Lv 38) |

Special: Land swarm: Swinub; Hoenn Sound: Piloswine, Piloswine; Sinnoh Sound: Smoochum, Smoochum

## Ice Path B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 38–40) | 25% (Lv 38–40) | 25% (Lv 38–40) |
| Swinub | 25% (Lv 38–41) | 25% (Lv 38–41) | 25% (Lv 38–41) |
| Spheal | 10% (Lv 38) | 10% (Lv 38) | 10% (Lv 38) |
| Shellder | 10% (Lv 39) | 10% (Lv 39) | 10% (Lv 39) |
| Seel | 15% (Lv 39–41) | 15% (Lv 39–41) | 15% (Lv 39–41) |
| Smoochum | 10% (Lv 39) | 10% (Lv 39) | 10% (Lv 39) |
| Delibird | 5% (Lv 40) | 5% (Lv 40) | 5% (Lv 40) |

Special: Land swarm: Swinub; Hoenn Sound: Piloswine, Sealeo; Sinnoh Sound: Delibird, Delibird

## Ice Path B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 40–43) | 30% (Lv 40–43) | 30% (Lv 40–43) |
| Piloswine | 25% (Lv 40–43) | 25% (Lv 40–43) | 25% (Lv 40–43) |
| Sealeo | 10% (Lv 40) | 10% (Lv 40) | 10% (Lv 40) |
| Snorunt | 10% (Lv 41) | 10% (Lv 41) | 10% (Lv 41) |
| Dewgong | 10% (Lv 41) | 10% (Lv 41) | 10% (Lv 41) |
| Jynx | 10% (Lv 41) | 10% (Lv 41) | 10% (Lv 41) |
| Delibird | 5% (Lv 42) | 5% (Lv 42) | 5% (Lv 42) |

Special: Land swarm: Swinub; Hoenn Sound: Glalie, Froslass; Sinnoh Sound: Delibird, Jynx

## Ice Path B3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Piloswine | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Sealeo | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Glalie | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Dewgong | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Jynx | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Sneasel | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Swinub; Hoenn Sound: Mamoswine, Walrein; Sinnoh Sound: Jynx, Sneasel

## Blackthorn City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 2–20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 10 |
| Dratini | 10% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 20 |
| Dratini | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 40 |
| Dratini | 10% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Magikarp

## Dragon's Den

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 60% | 10–20 |
| Dratini | 30% | 5–15 |
| Gyarados | 10% | 5–15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 80% | 10 |
| Dratini | 20% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 20 |
| Dratini | 20% | 20 |
| Gyarados | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 40 |
| Dratini | 30% | 40 |
| Gyarados | 20% | 40 |
| Dragonair | 10% | 40 |

Special: Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Dratini

## Route 45

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 30% (Lv 42–43) | 30% (Lv 42–43) | 30% (Lv 42–43) |
| Donphan | 20% (Lv 42) | 20% (Lv 42) | 20% (Lv 42) |
| Gligar | 20% (Lv 42–43) | 20% (Lv 42–43) | 20% (Lv 42–43) |
| Skarmory | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Grumpig | 5% (Lv 44) | 5% (Lv 44) | 5% (Lv 44) |
| Camerupt | 5% (Lv 44) | 5% (Lv 44) | 5% (Lv 44) |
| Torkoal | 5% (Lv 44–45) | 5% (Lv 44–45) | 5% (Lv 44–45) |
| Vibrava | 5% (Lv 45) | 5% (Lv 45) | 5% (Lv 45) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 2–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 10 |
| Dratini | 10% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 20 |
| Dratini | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 90% | 40 |
| Dratini | 10% | 40 |

Special: Land swarm: Rhydon; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Magikarp; Hoenn Sound: Gliscor, Golem; Sinnoh Sound: Rhyhorn, Vibrava

## Route 46

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 20% (Lv 4) | 20% (Lv 4) | 25% (Lv 4–5) |
| Spearow | 20% (Lv 4) | 20% (Lv 4) | – |
| Spoink | 10% (Lv 4) | 10% (Lv 4) | 5% (Lv 6) |
| Rattata | 10% (Lv 4) | 10% (Lv 4) | 20% (Lv 4) |
| Jigglypuff | 15% (Lv 5) | 15% (Lv 5) | 10% (Lv 5) |
| Phanpy | 15% (Lv 5) | 15% (Lv 5) | – |
| Swablu | 5% (Lv 6) | 5% (Lv 6) | – |
| Numel | 5% (Lv 6) | 5% (Lv 6) | 10% (Lv 4) |
| Clefairy | – | – | 10% (Lv 4) |
| Houndour | – | – | 15% (Lv 5) |
| Shinx | – | – | 5% (Lv 6) |

Special: Land swarm: Geodude; Hoenn Sound: Graveler, Fearow; Sinnoh Sound: Igglybuff, Igglybuff

## Dark Cave Route 31 Entrance

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Geodude | 20% (Lv 8) | 20% (Lv 8) | 20% (Lv 8) |
| Zubat | 20% (Lv 8) | 20% (Lv 8) | 20% (Lv 8) |
| Bronzor | 10% (Lv 8) | 10% (Lv 8) | 10% (Lv 8) |
| Makuhita | 10% (Lv 8) | 10% (Lv 8) | 10% (Lv 8) |
| Sandshrew | 10% (Lv 9) | 10% (Lv 9) | 10% (Lv 9) |
| Teddiursa | 10% (Lv 9) | 10% (Lv 9) | – |
| Slugma | 10% (Lv 9–10) | 10% (Lv 9–10) | 10% (Lv 9–10) |
| Larvitar | 5% (Lv 9) | 5% (Lv 9) | 5% (Lv 9) |
| Dunsparce | 5% (Lv 10) | 5% (Lv 10) | 5% (Lv 10) |
| Wynaut | – | – | 10% (Lv 9) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Magikarp | 30% | 5–15 |
| Shellos | 5% | 2–10 |
| Gastrodon | 5% | 2–10 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Dunsparce | 80% | 4–8 |
| Nosepass | 20% | 8–14 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 10 |
| Wooper | 45% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 20 |
| Quagsire | 45% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 40% | 40 |
| Quagsire | 45% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Larvitar; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Whiscash; Hoenn Sound: Golbat, Golbat; Sinnoh Sound: Chingling, Chingling

## Dark Cave Route 45 Entrance

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 20% (Lv 26) | 20% (Lv 26) | 20% (Lv 26) |
| Golbat | 20% (Lv 26) | 20% (Lv 26) | 20% (Lv 26) |
| Teddiursa | 20% (Lv 26–27) | 20% (Lv 26–27) | 20% (Lv 26–27) |
| Slugma | 20% (Lv 27–28) | 20% (Lv 27–28) | 20% (Lv 27–28) |
| Wobbuffet | 15% (Lv 28–30) | 15% (Lv 28–30) | 15% (Lv 28–30) |
| Ursaring | 5% (Lv 29–30) | 5% (Lv 29–30) | 5% (Lv 29–30) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 60% | 10–20 |
| Magikarp | 30% | 5–15 |
| Shellos | 5% | 2–10 |
| Gastrodon | 5% | 2–10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 10 |
| Wooper | 45% | 10 |
| Barboach | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 40% | 20 |
| Quagsire | 45% | 20 |
| Barboach | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 40% | 40 |
| Quagsire | 45% | 40 |
| Whiscash | 15% | 40 |

Special: Land swarm: Geodude; Surf swarm: Magikarp; Fishing swarm: Magikarp; Night fishing: Whiscash; Hoenn Sound: Golem, Ursaring; Sinnoh Sound: Quagsire, Quagsire

## Route 47

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Farfetch’d | 25% (Lv 41–45) | 25% (Lv 41–45) | – |
| Ditto | 20% (Lv 41) | 20% (Lv 41) | 20% (Lv 41) |
| Swellow | 10% (Lv 41) | 10% (Lv 41) | – |
| Miltank | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 41) |
| Gloom | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Weepinbell | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 42) |
| Fearow | 5% (Lv 43) | 5% (Lv 43) | 10% (Lv 43) |
| Raticate | 10% (Lv 43–45) | 10% (Lv 43–45) | 10% (Lv 43) |
| Venomoth | – | – | 20% (Lv 41) |
| Noctowl | – | – | 10% (Lv 44–45) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Seel | 60% | 15–25 |
| Tentacool | 30% | 10–20 |
| Wingull | 5% | 15–25 |
| Spheal | 5% | 15–25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 10 |
| Tentacool | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 40% | 20 |
| Shellder | 30% | 20 |
| Chinchou | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Shellder | 40% | 40 |
| Tentacool | 30% | 40 |
| Tentacruel | 20% | 40 |
| Lanturn | 10% | 40 |

Special: Land swarm: Altaria; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Tentacool; Hoenn Sound: Bellossom, Victreebel; Sinnoh Sound: Yanma, Yanma

## Mt. Moon Outside Area

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 64% | 35 |
| Poliwhirl | 31% | 30–35 |
| Quagsire | 5% | 35 |

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
| Poliwhirl | 100% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwhirl

## Mt. Moon Outside Clefairy Active

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Wooper | 64% | 35 |
| Poliwhirl | 31% | 30–35 |
| Quagsire | 5% | 35 |

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
| Poliwhirl | 100% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Poliwag; Night fishing: Poliwhirl

## Seafoam Islands 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Zubat | 30% (Lv 48–49) | 30% (Lv 48–49) | 30% (Lv 48–49) |
| Psyduck | 30% (Lv 48–50) | 30% (Lv 48–50) | 30% (Lv 48–50) |
| Slowpoke | 30% (Lv 51–54) | 30% (Lv 51–54) | 30% (Lv 51–54) |
| Golbat | 10% (Lv 55–58) | 10% (Lv 55–58) | 10% (Lv 55–58) |

Special: Land swarm: Zubat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Seel | 35% (Lv 49–59) | 35% (Lv 49–59) | 35% (Lv 49–59) |
| Golbat | 25% (Lv 49–54) | 25% (Lv 49–54) | 25% (Lv 49–54) |
| Snorunt | 10% (Lv 50) | 10% (Lv 50) | 10% (Lv 50) |
| Slowbro | 15% (Lv 51–55) | 15% (Lv 51–55) | 15% (Lv 51–55) |
| Piloswine | 15% (Lv 52–58) | 15% (Lv 52–58) | 15% (Lv 52–58) |

Special: Land swarm: Seel; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 35% (Lv 56–60) | 35% (Lv 56–60) | 35% (Lv 56–60) |
| Dewgong | 20% (Lv 56) | 20% (Lv 56) | 20% (Lv 56) |
| Sealeo | 10% (Lv 56) | 10% (Lv 56) | 10% (Lv 56) |
| Kingler | 10% (Lv 57) | 10% (Lv 57) | 10% (Lv 57) |
| Piloswine | 10% (Lv 57) | 10% (Lv 57) | 10% (Lv 57) |
| Slowbro | 10% (Lv 58) | 10% (Lv 58) | 10% (Lv 58) |
| Glalie | 5% (Lv 59–60) | 5% (Lv 59–60) | 5% (Lv 59–60) |

Special: Land swarm: Seel; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 56–60) | 25% (Lv 56–60) | 25% (Lv 56–60) |
| Dewgong | 20% (Lv 56) | 20% (Lv 56) | 20% (Lv 56) |
| Sealeo | 10% (Lv 56) | 10% (Lv 56) | 10% (Lv 56) |
| Glalie | 10% (Lv 57) | 10% (Lv 57) | 10% (Lv 57) |
| Kingler | 10% (Lv 57) | 10% (Lv 57) | 10% (Lv 57) |
| Piloswine | 10% (Lv 58) | 10% (Lv 58) | 10% (Lv 58) |
| Delibird | 5% (Lv 58) | 5% (Lv 58) | 5% (Lv 58) |
| Sneasel | 5% (Lv 58) | 5% (Lv 58) | 5% (Lv 58) |
| Jynx | 5% (Lv 59–60) | 5% (Lv 59–60) | 5% (Lv 59–60) |

Special: Land swarm: Dewgong; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Seafoam Islands B4F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 57–60) | 25% (Lv 57–60) | 25% (Lv 57–60) |
| Dewgong | 20% (Lv 57) | 20% (Lv 57) | 20% (Lv 57) |
| Sealeo | 10% (Lv 57) | 10% (Lv 57) | 10% (Lv 57) |
| Glalie | 10% (Lv 58) | 10% (Lv 58) | 10% (Lv 58) |
| Kingler | 10% (Lv 58) | 10% (Lv 58) | 10% (Lv 58) |
| Piloswine | 10% (Lv 58) | 10% (Lv 58) | 10% (Lv 58) |
| Delibird | 5% (Lv 59) | 5% (Lv 59) | 5% (Lv 59) |
| Sneasel | 5% (Lv 59) | 5% (Lv 59) | 5% (Lv 59) |
| Jynx | 5% (Lv 59–60) | 5% (Lv 59–60) | 5% (Lv 59–60) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 30–40 |
| Staryu | 35% | 30–45 |
| Spheal | 5% | 35–50 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 10 |
| Horsea | 15% | 10 |
| Krabby | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Krabby | 30% | 20 |
| Horsea | 15% | 20 |
| Shellder | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Gyarados | 40% | 40 |
| Seadra | 30% | 40 |
| Shellder | 15% | 40 |
| Kingler | 15% | 40 |

Special: Land swarm: Seel; Surf swarm: Seel; Fishing swarm: Magikarp; Night fishing: Seadra; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt. Silver Moltres Room

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

## Mt. Silver 3F

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

## Mt. Silver 4F

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
| Graveler | 25% (Lv 30–32) | 25% (Lv 30–32) | 25% (Lv 30–32) |
| Golbat | 20% (Lv 30) | 20% (Lv 30) | 20% (Lv 30) |
| Baltoy | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Machoke | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Kingler | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Quagsire | 15% (Lv 31–32) | 15% (Lv 31–32) | 15% (Lv 31–32) |
| Trapinch | 5% (Lv 32–33) | 5% (Lv 32–33) | 5% (Lv 32–33) |
| Hippopotas | 5% (Lv 33) | 5% (Lv 33) | 5% (Lv 33) |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 80% | 20–26 |
| Graveler | 20% | 28–31 |

Special: Land swarm: Golbat; Hoenn Sound: Claydol, Hippowdon; Sinnoh Sound: Onix, Misdreavus

## Bell Tower 10F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 42–44) | 30% (Lv 42–44) | 30% (Lv 42–44) |
| Piloswine | 25% (Lv 42–44) | 25% (Lv 42–44) | 25% (Lv 42–44) |
| Sealeo | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Glalie | 10% (Lv 42) | 10% (Lv 42) | 10% (Lv 42) |
| Dewgong | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Jynx | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Sneasel | 5% (Lv 43) | 5% (Lv 43) | 5% (Lv 43) |

Special: Land swarm: Rattata; Hoenn Sound: Zigzagoon, Spinda; Sinnoh Sound: Chatot, Meditite

## Mt. Silver Outside Pokémon Center

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

## Mt. Silver 1F

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

## Mt. Silver Mountainside

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

## Mt. Silver Expert Belt Room

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

## Mt. Silver Top Snowy Area

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
| Slowpoke | 90% | 25 |
| Slowbro | 10% | 25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 20 |
| Goldeen | 30% | 20 |
| Horsea | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seadra | 40% | 40 |
| Poliwhirl | 30% | 40 |
| Qwilfish | 30% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Relicanth; Night fishing: Poliwhirl

## Route 19

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 35 |
| Mantine | 30% | 30 |
| Wingull | 5% | 35 |
| Pelipper | 5% | 35 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 80% | 28–31 |
| Kingler | 20% | 24–27 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 10 |
| Goldeen | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 50% | 20 |
| Krabby | 30% | 20 |
| Finneon | 15% | 20 |
| Clamperl | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 40% | 40 |
| Krabby | 30% | 40 |
| Lumineon | 15% | 40 |
| Huntail | 10% | 40 |
| Gorebyss | 5% | 40 |

Special: Surf swarm: Clamperl; Fishing swarm: Magikarp; Night fishing: Seaking

## Route 20

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 35 |
| Tentacruel | 30% | 30 |
| Wingull | 5% | 35 |
| Pelipper | 5% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 70% | 10 |
| Goldeen | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 50% | 20 |
| Magikarp | 30% | 20 |
| Finneon | 15% | 20 |
| Clamperl | 5% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 40% | 40 |
| Chinchou | 30% | 40 |
| Lumineon | 15% | 40 |
| Huntail | 10% | 40 |
| Gorebyss | 5% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Seaking

## Pallet Town

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Marill | 100% | 30–35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Tentacool | 35% | 10 |
| Finneon | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 100% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Staryu | 100% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Staryu

## Viridian City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 100% | 5–10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 100% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 100% | 40 |

Special: Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Goldeen

## Cerulean City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Hoppip | 60% | 10 |
| Goldeen | 30% | 5 |
| Skiploom | 5% | 10 |
| Masquerain | 5% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Goldeen | 30% | 10 |
| Seaking | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 20 |
| Seaking | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Staryu | 40% | 40 |
| Seaking | 30% | 40 |
| Dratini | 20% | 40 |
| Dragonair | 10% | 40 |

Special: Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Seaking

## Vermilion City

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 35 |
| Tentacruel | 30% | 30 |
| Wingull | 5% | 35 |
| Pelipper | 5% | 35 |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Krabby | 80% | 24–37 |
| Shuckle | 20% | 32–35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 20 |
| Chinchou | 30% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacruel | 40% | 40 |
| Shellder | 40% | 40 |
| Lanturn | 20% | 40 |

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
| Tentacool | 65% | 35 |
| Tentacruel | 30% | 30 |
| Relicanth | 5% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 20 |
| Chinchou | 30% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacruel | 40% | 40 |
| Shellder | 40% | 40 |
| Lanturn | 20% | 40 |

Special: Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder

## Route 48

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Farfetch’d | 20% (Lv 30) | 20% (Lv 30) | – |
| Tangela | 20% (Lv 30) | 20% (Lv 30) | 20% (Lv 30) |
| Diglett | 10% (Lv 30) | 10% (Lv 30) | 10% (Lv 30) |
| Gloom | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Weepinbell | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Girafarig | 10% (Lv 31) | 10% (Lv 31) | 10% (Lv 31) |
| Chansey | 5% (Lv 32) | 5% (Lv 32) | 5% (Lv 32) |
| Kecleon | 5% (Lv 32) | 5% (Lv 32) | 5% (Lv 32) |
| Absol | 5% (Lv 32–33) | 5% (Lv 32–33) | 5% (Lv 32–33) |
| Tropius | 5% (Lv 33) | 5% (Lv 33) | 5% (Lv 33) |
| Houndour | – | – | 20% (Lv 30) |

Special: Land swarm: Tauros; Hoenn Sound: Tangrowth, Dugtrio; Sinnoh Sound: Happiny, Happiny

## Route 26

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Dodrio | 20% (Lv 44) | 20% (Lv 44) | – |
| Skiploom | 20% (Lv 44) | 20% (Lv 44) | – |
| Rapidash | 20% (Lv 44) | 20% (Lv 44) | 20% (Lv 44) |
| Magneton | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Kangaskhan | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Sandslash | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Arbok | 10% (Lv 46) | 10% (Lv 46) | 10% (Lv 46) |
| Quagsire | – | – | 20% (Lv 44) |
| Houndoom | – | – | 20% (Lv 44) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 30 |
| Tentacruel | 30% | 25 |
| Buizel | 5% | 30 |
| Floatzel | 5% | 30 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Tentacool | 35% | 10 |
| Luvdisc | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Tentacool | 35% | 20 |
| Luvdisc | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Lanturn | 50% | 40 |
| Tentacruel | 35% | 40 |
| Luvdisc | 15% | 40 |

Special: Land swarm: Doduo; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Lanturn; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 27

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Doduo | 20% (Lv 42) | 20% (Lv 42) | – |
| Skiploom | 20% (Lv 42) | 20% (Lv 42) | – |
| Ponyta | 20% (Lv 42–43) | 20% (Lv 42–43) | 20% (Lv 42–43) |
| Dodrio | 10% (Lv 43) | 10% (Lv 43) | – |
| Rapidash | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Sandslash | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Arbok | 10% (Lv 44–45) | 10% (Lv 44–45) | 10% (Lv 44–45) |
| Wooper | – | – | 20% (Lv 42) |
| Houndour | – | – | 20% (Lv 42) |
| Quagsire | – | – | 10% (Lv 43) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 20 |
| Tentacruel | 30% | 15 |
| Buizel | 5% | 20 |
| Floatzel | 5% | 20 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 10 |
| Tentacool | 35% | 10 |
| Luvdisc | 15% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 50% | 20 |
| Tentacool | 35% | 20 |
| Luvdisc | 15% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 50% | 40 |
| Shellder | 35% | 40 |
| Luvdisc | 15% | 40 |

Special: Land swarm: Doduo; Surf swarm: Luvdisc; Fishing swarm: Magikarp; Night fishing: Luvdisc; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

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

## Mt. Moon 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 30% (Lv 47) | 30% (Lv 47) | 30% (Lv 47) |
| Clefairy | 20% (Lv 47) | 20% (Lv 47) | 20% (Lv 47) |
| Graveler | 20% (Lv 48) | 20% (Lv 48) | 20% (Lv 48) |
| Sandslash | 15% (Lv 49) | 15% (Lv 49) | 15% (Lv 49) |
| Parasect | 15% (Lv 49–51) | 15% (Lv 49–51) | 15% (Lv 49–51) |

Special: Land swarm: Zubat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Mt. Moon 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 48–49) | 25% (Lv 48–49) | 25% (Lv 48–49) |
| Clefairy | 20% (Lv 48) | 20% (Lv 48) | 20% (Lv 48) |
| Chimecho | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Graveler | 15% (Lv 48–49) | 15% (Lv 48–49) | 15% (Lv 48–49) |
| Sandslash | 10% (Lv 49) | 10% (Lv 49) | 10% (Lv 49) |
| Parasect | 10% (Lv 49) | 10% (Lv 49) | 10% (Lv 49) |
| Solrock | 5% (Lv 50) | 5% (Lv 50) | 5% (Lv 50) |
| Lunatone | 5% (Lv 50) | 5% (Lv 50) | 5% (Lv 50) |

Special: Land swarm: Zubat; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Rock Tunnel 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 20% (Lv 52) | 20% (Lv 52) | 20% (Lv 52) |
| Golbat | 20% (Lv 52) | 20% (Lv 52) | 20% (Lv 52) |
| Lairon | 10% (Lv 52) | 10% (Lv 52) | 10% (Lv 52) |
| Makuhita | 10% (Lv 53) | 10% (Lv 53) | 10% (Lv 53) |
| Cubone | 10% (Lv 53) | 10% (Lv 53) | 10% (Lv 53) |
| Ditto | 10% (Lv 53) | 10% (Lv 53) | 10% (Lv 53) |
| Mankey | 10% (Lv 54–55) | 10% (Lv 54–55) | 10% (Lv 54–55) |
| Magnemite | 10% (Lv 54–55) | 10% (Lv 54–55) | 10% (Lv 54–55) |

Special: Land swarm: Cubone; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Rock Tunnel B1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Graveler | 20% (Lv 53) | 20% (Lv 53) | 20% (Lv 53) |
| Golbat | 20% (Lv 53) | 20% (Lv 53) | 20% (Lv 53) |
| Lairon | 10% (Lv 53) | 10% (Lv 53) | 10% (Lv 53) |
| Hariyama | 10% (Lv 54) | 10% (Lv 54) | 10% (Lv 54) |
| Marowak | 10% (Lv 54) | 10% (Lv 54) | 10% (Lv 54) |
| Primeape | 10% (Lv 54) | 10% (Lv 54) | 10% (Lv 54) |
| Magneton | 10% (Lv 55–56) | 10% (Lv 55–56) | 10% (Lv 55–56) |
| Kangaskhan | 5% (Lv 55) | 5% (Lv 55) | 5% (Lv 55) |
| Onix | 5% (Lv 55–56) | 5% (Lv 55–56) | 5% (Lv 55–56) |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Geodude | 80% | 12–16 |
| Nosepass | 20% | 17–21 |

Special: Land swarm: Cubone; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Victory Road 1F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Golbat | 25% (Lv 44–46) | 25% (Lv 44–46) | 25% (Lv 44–46) |
| Graveler | 20% (Lv 44) | 20% (Lv 44) | 20% (Lv 44) |
| Bronzong | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Rhydon | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Ursaring | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Donphan | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Marowak | 5% (Lv 45) | 5% (Lv 45) | 5% (Lv 45) |
| Steelix | 10% (Lv 45–46) | 10% (Lv 45–46) | 10% (Lv 45–46) |

Special: Land swarm: Graveler; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 1

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgey | 20% (Lv 48) | 20% (Lv 48) | – |
| Rattata | 20% (Lv 49) | 20% (Lv 49) | 20% (Lv 49) |
| Sentret | 10% (Lv 50) | 10% (Lv 50) | – |
| Pidgeotto | 10% (Lv 51) | 10% (Lv 51) | – |
| Raticate | 10% (Lv 52) | 10% (Lv 52) | 10% (Lv 52) |
| Furret | 10% (Lv 53) | 10% (Lv 53) | – |
| Zigzagoon | 5% (Lv 54) | 5% (Lv 54) | 5% (Lv 54) |
| Bidoof | 5% (Lv 55) | 5% (Lv 55) | 5% (Lv 55) |
| Starly | 5% (Lv 56–58) | 5% (Lv 56–58) | – |
| Staravia | 5% (Lv 57–59) | 5% (Lv 57–59) | – |
| Hoothoot | – | – | 20% (Lv 48) |
| Ponyta | – | – | 10% (Lv 50) |
| Noctowl | – | – | 10% (Lv 51) |
| Rapidash | – | – | 10% (Lv 53) |
| Shinx | – | – | 5% (Lv 56–58) |
| Luxio | – | – | 5% (Lv 57–59) |

Special: Land swarm: Poochyena; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 2 South Below Viridian Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Butterfree | 30% (Lv 45–49) | 30% (Lv 45–49) | 25% (Lv 45–47) |
| Beedrill | 25% (Lv 45–47) | 25% (Lv 45–47) | 25% (Lv 45–47) |
| Pachirisu | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Cherrim | 10% (Lv 46) | 10% (Lv 46) | – |
| Ledian | 15% (Lv 46–49) | 15% (Lv 46–49) | – |
| Pidgeotto | 10% (Lv 47) | 10% (Lv 47) | – |
| Ariados | – | – | 15% (Lv 46–49) |
| Noctowl | – | – | 10% (Lv 46) |
| Yanma | – | – | 15% (Lv 47–49) |

Special: Land swarm: Caterpie; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 3

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Staravia | 20% (Lv 46) | 20% (Lv 46) | – |
| Fearow | 20% (Lv 46) | 20% (Lv 46) | 20% (Lv 46) |
| Pidgeotto | 15% (Lv 46–48) | 15% (Lv 46–48) | – |
| Primeape | 15% (Lv 47–48) | 15% (Lv 47–48) | 15% (Lv 47–48) |
| Nidorino | 15% (Lv 47–49) | 15% (Lv 47–49) | 15% (Lv 47–49) |
| Nidorina | 15% (Lv 47–49) | 15% (Lv 47–49) | 15% (Lv 47–49) |
| Jigglypuff | – | – | 20% (Lv 46) |
| Noctowl | – | – | 15% (Lv 46–48) |

Special: Land swarm: Baltoy; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 4

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Fearow | 25% (Lv 46–48) | 25% (Lv 46–48) | 25% (Lv 46–48) |
| Raticate | 25% (Lv 46–48) | 25% (Lv 46–48) | 25% (Lv 46–48) |
| Purugly | 10% (Lv 46) | 10% (Lv 46) | 10% (Lv 46) |
| Skuntank | 10% (Lv 47) | 10% (Lv 47) | 10% (Lv 47) |
| Arbok | 15% (Lv 47–50) | 15% (Lv 47–50) | 15% (Lv 47–50) |
| Jigglypuff | 15% (Lv 48–50) | 15% (Lv 48–50) | 15% (Lv 48–50) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 94% | 5–10 |
| Seaking | 6% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Goldeen | 30% | 10 |
| Seaking | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 20 |
| Goldeen | 30% | 20 |
| Seaking | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 40 |
| Goldeen | 30% | 40 |
| Seaking | 30% | 40 |

Special: Land swarm: Spearow; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 5

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgeotto | 25% (Lv 47–50) | 25% (Lv 47–50) | – |
| Raticate | 25% (Lv 47–50) | 25% (Lv 47–50) | 25% (Lv 47–50) |
| Meditite | 10% (Lv 47) | 10% (Lv 47) | 10% (Lv 48) |
| Chatot | 10% (Lv 48) | 10% (Lv 48) | – |
| Kadabra | 10% (Lv 48) | 10% (Lv 48) | 20% (Lv 47) |
| Jigglypuff | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Machop | 5% (Lv 49) | 5% (Lv 49) | 10% (Lv 48) |
| Weepinbell | 5% (Lv 49) | 5% (Lv 49) | 5% (Lv 49) |
| Mightyena | – | – | 10% (Lv 47) |
| Persian | – | – | 10% (Lv 49–50) |

Special: Land swarm: Pidgey; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 6

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Pidgeotto | 35% (Lv 45–48) | 35% (Lv 45–48) | – |
| Kadabra | 25% (Lv 45–47) | 25% (Lv 45–47) | 25% (Lv 45–47) |
| Cherrim | 10% (Lv 45) | 10% (Lv 45) | – |
| Raticate | 15% (Lv 46–47) | 15% (Lv 46–47) | 20% (Lv 45–46) |
| Weepinbell | 15% (Lv 46–48) | 15% (Lv 46–48) | 20% (Lv 46) |
| Persian | – | – | 25% (Lv 45–47) |
| Gloom | – | – | 10% (Lv 47–48) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Psyduck | 95% | 5–10 |
| Golduck | 5% | 10 |

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
| Poliwag | 70% | 40 |
| Magikarp | 20% | 40 |
| Poliwhirl | 10% | 40 |

Special: Land swarm: Pidgey; Surf swarm: Psyduck; Fishing swarm: Magikarp; Night fishing: Poliwag; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 7

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Weepinbell | 25% (Lv 50–54) | 25% (Lv 50–54) | 20% (Lv 50) |
| Pidgeotto | 20% (Lv 50) | 20% (Lv 50) | – |
| Staravia | 10% (Lv 50) | 10% (Lv 50) | – |
| Growlithe | 10% (Lv 51) | 10% (Lv 51) | 10% (Lv 51) |
| Vulpix | 10% (Lv 51) | 10% (Lv 51) | 10% (Lv 51) |
| Jigglypuff | 10% (Lv 52) | 10% (Lv 52) | 10% (Lv 52) |
| Raticate | 10% (Lv 52–54) | 10% (Lv 52–54) | – |
| Kadabra | 5% (Lv 52) | 5% (Lv 52) | – |
| Gloom | – | – | 20% (Lv 50) |
| Houndour | – | – | 15% (Lv 50–52) |
| Persian | – | – | 10% (Lv 52–54) |
| Houndoom | – | – | 5% (Lv 53–54) |

Special: Land swarm: Rattata; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 8

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Growlithe | 35% (Lv 50–54) | 35% (Lv 50–54) | 30% (Lv 50–54) |
| Vulpix | 25% (Lv 50–52) | 25% (Lv 50–52) | 25% (Lv 50–52) |
| Staravia | 10% (Lv 50) | 10% (Lv 50) | – |
| Kadabra | 15% (Lv 51–52) | 15% (Lv 51–52) | 10% (Lv 51) |
| Xatu | 15% (Lv 51–54) | 15% (Lv 51–54) | 15% (Lv 51–54) |
| Banette | – | – | 10% (Lv 50) |
| Haunter | – | – | 10% (Lv 52) |

Special: Land swarm: Pidgeotto; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 9

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Primeape | 25% (Lv 49–50) | 25% (Lv 49–50) | 25% (Lv 49–50) |
| Fearow | 20% (Lv 49) | 20% (Lv 49) | 20% (Lv 49) |
| Arbok | 20% (Lv 49) | 20% (Lv 49) | 20% (Lv 49) |
| Nidorina | 15% (Lv 50) | 15% (Lv 50) | 15% (Lv 50) |
| Nidorino | 15% (Lv 50–51) | 15% (Lv 50–51) | 15% (Lv 50–51) |
| Marowak | 5% (Lv 51) | 5% (Lv 51) | 5% (Lv 51) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 60% | 15 |
| Seaking | 40% | 10–15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Goldeen | 30% | 10 |
| Seaking | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 20 |
| Seaking | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seaking | 100% | 40 |

Special: Land swarm: Sableye; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 10

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Fearow | 20% (Lv 47) | 20% (Lv 47) | 20% (Lv 47) |
| Electrode | 25% (Lv 47–52) | 25% (Lv 47–52) | 25% (Lv 47–52) |
| Luxio | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Manectric | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Flaaffy | 10% (Lv 49) | 10% (Lv 49) | 10% (Lv 49) |
| Raticate | 10% (Lv 49) | 10% (Lv 49) | 10% (Lv 49) |
| Electabuzz | 10% (Lv 50–52) | 10% (Lv 50–52) | 10% (Lv 50–52) |
| Pikachu | 5% (Lv 50) | 5% (Lv 50) | 5% (Lv 50) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Fearow | 60% | 15 |
| Chinchou | 40% | 10–15 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Chinchou | 80% | 20 |
| Lanturn | 20% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Lanturn | 100% | 40 |

Special: Land swarm: Spearow; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Lanturn; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 11

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Hypno | 40% (Lv 50–52) | 40% (Lv 50–52) | 40% (Lv 50–52) |
| Raticate | 20% (Lv 50) | 20% (Lv 50) | 20% (Lv 50) |
| Drowzee | 10% (Lv 51) | 10% (Lv 51) | 10% (Lv 51) |
| Rattata | 10% (Lv 51) | 10% (Lv 51) | 10% (Lv 51) |
| Plusle | 5% (Lv 53) | 5% (Lv 53) | 5% (Lv 53) |
| Minun | 5% (Lv 53) | 5% (Lv 53) | 5% (Lv 53) |
| Linoone | 5% (Lv 54–55) | 5% (Lv 54–55) | 5% (Lv 54–55) |
| Luxio | 5% (Lv 54–55) | 5% (Lv 54–55) | 5% (Lv 54–55) |

Special: Land swarm: Drowzee; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 13

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swellow | 20% (Lv 50) | 20% (Lv 50) | 20% (Lv 50) |
| Nidorina | 35% (Lv 50–54) | 35% (Lv 50–54) | 35% (Lv 50–54) |
| Nidorino | 15% (Lv 50–52) | 15% (Lv 50–52) | 15% (Lv 50–52) |
| Skiploom | 15% (Lv 51–52) | 15% (Lv 51–52) | – |
| Farfetch’d | 15% (Lv 51–54) | 15% (Lv 51–54) | – |
| Quagsire | – | – | 15% (Lv 51–52) |
| Noctowl | – | – | 15% (Lv 51–54) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Slowpoke | 90% | 25 |
| Slowbro | 10% | 25 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 40% | 20 |
| Goldeen | 30% | 20 |
| Horsea | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Seadra | 40% | 40 |
| Poliwhirl | 30% | 40 |
| Qwilfish | 30% | 40 |

Special: Land swarm: Chansey; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Poliwhirl; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 14

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swellow | 20% (Lv 51) | 20% (Lv 51) | 20% (Lv 51) |
| Nidorina | 35% (Lv 51–55) | 35% (Lv 51–55) | 35% (Lv 51–55) |
| Nidorino | 15% (Lv 51–53) | 15% (Lv 51–53) | 15% (Lv 51–53) |
| Skiploom | 15% (Lv 52–53) | 15% (Lv 52–53) | – |
| Chansey | 15% (Lv 52–55) | 15% (Lv 52–55) | 15% (Lv 52–55) |
| Venomoth | – | – | 15% (Lv 52–53) |

Special: Land swarm: Nidorina; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 15

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Swellow | 20% (Lv 51) | 20% (Lv 51) | 20% (Lv 51) |
| Nidorina | 35% (Lv 51–55) | 35% (Lv 51–55) | 35% (Lv 51–55) |
| Nidorino | 15% (Lv 51–53) | 15% (Lv 51–53) | 15% (Lv 51–53) |
| Skiploom | 15% (Lv 52–53) | 15% (Lv 52–53) | – |
| Ditto | 15% (Lv 52–55) | 15% (Lv 52–55) | 15% (Lv 52–55) |
| Venomoth | – | – | 15% (Lv 52–53) |

Special: Land swarm: Nidorina; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 16

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Grimer | 35% (Lv 52–54) | 35% (Lv 52–54) | 35% (Lv 52–54) |
| Muk | 20% (Lv 52) | 20% (Lv 52) | 20% (Lv 52) |
| Gulpin | 10% (Lv 52) | 10% (Lv 52) | 10% (Lv 52) |
| Magcargo | 15% (Lv 53–54) | 15% (Lv 53–54) | 15% (Lv 53–54) |
| Fearow | 10% (Lv 53) | 10% (Lv 53) | – |
| Skorupi | 5% (Lv 54–55) | 5% (Lv 54–55) | 5% (Lv 54–55) |
| Drapion | 5% (Lv 55) | 5% (Lv 55) | 5% (Lv 55) |
| Murkrow | – | – | 10% (Lv 53) |

Special: Land swarm: Grimer; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 17

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Gulpin | 20% (Lv 52) | 20% (Lv 52) | 20% (Lv 52) |
| Grimer | 30% (Lv 52–55) | 30% (Lv 52–55) | 30% (Lv 52–55) |
| Fearow | 15% (Lv 52–54) | 15% (Lv 52–54) | 15% (Lv 52–54) |
| Muk | 10% (Lv 53) | 10% (Lv 53) | 10% (Lv 53) |
| Magcargo | 15% (Lv 53–55) | 15% (Lv 53–55) | 15% (Lv 53–55) |
| Dodrio | 10% (Lv 53) | 10% (Lv 53) | – |
| Misdreavus | – | – | 10% (Lv 53) |

Special: Land swarm: Fearow; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 18

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Gulpin | 20% (Lv 50) | 20% (Lv 50) | 20% (Lv 50) |
| Grimer | 30% (Lv 50–56) | 30% (Lv 50–56) | 30% (Lv 50–56) |
| Fearow | 15% (Lv 51–54) | 15% (Lv 51–54) | 15% (Lv 51–54) |
| Muk | 10% (Lv 51) | 10% (Lv 51) | 10% (Lv 51) |
| Magcargo | 15% (Lv 52–55) | 15% (Lv 52–55) | 15% (Lv 52–55) |
| Dodrio | 10% (Lv 52) | 10% (Lv 52) | – |
| Murkrow | – | – | 10% (Lv 52) |

Special: Land swarm: Grimer; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Route 21

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Tangela | 35% (Lv 54–59) | 35% (Lv 54–59) | 35% (Lv 54–59) |
| Mr. Mime | 30% (Lv 54–59) | 30% (Lv 54–59) | 30% (Lv 54–59) |
| Pelipper | 10% (Lv 55) | 10% (Lv 55) | 10% (Lv 55) |
| Gastrodon | 10% (Lv 55) | 10% (Lv 55) | 10% (Lv 55) |
| Raticate | 15% (Lv 56–57) | 15% (Lv 56–57) | 15% (Lv 56–57) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 35 |
| Wingull | 30% | 30 |
| Wailmer | 5% | 35 |
| Pelipper | 5% | 35 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacool | 60% | 20 |
| Chinchou | 30% | 20 |
| Shellder | 10% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Tentacruel | 40% | 40 |
| Shellder | 40% | 40 |
| Lanturn | 20% | 40 |

Special: Land swarm: Tangela; Surf swarm: Tentacool; Fishing swarm: Magikarp; Night fishing: Shellder; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 22

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Fearow | 30% (Lv 54–55) | 30% (Lv 54–55) | 30% (Lv 54–55) |
| Dodrio | 30% (Lv 54–55) | 30% (Lv 54–55) | 30% (Lv 54–55) |
| Raticate | 15% (Lv 56–57) | 15% (Lv 56–57) | 15% (Lv 56–57) |
| Primeape | 15% (Lv 56–57) | 15% (Lv 56–57) | 15% (Lv 56–57) |
| Rapidash | 10% (Lv 58–59) | 10% (Lv 58–59) | 10% (Lv 58–59) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 65% | 10 |
| Poliwhirl | 30% | 5 |
| Buizel | 5% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 100% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwag | 100% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Poliwhirl | 95% | 40 |
| Politoed | 5% | 40 |

Special: Land swarm: Rattata; Surf swarm: Poliwag; Fishing swarm: Magikarp; Night fishing: Poliwhirl; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 24

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Weepinbell | 20% (Lv 47) | 20% (Lv 47) | 20% (Lv 47) |
| Skiploom | 30% (Lv 47–48) | 30% (Lv 47–48) | – |
| Pidgeotto | 20% (Lv 47–49) | 20% (Lv 47–49) | – |
| Bellsprout | 10% (Lv 48) | 10% (Lv 48) | – |
| Kirlia | 5% (Lv 49) | 5% (Lv 49) | 5% (Lv 49) |
| Staravia | 5% (Lv 49) | 5% (Lv 49) | – |
| Roselia | 5% (Lv 50–51) | 5% (Lv 50–51) | 5% (Lv 50–51) |
| Surskit | 5% (Lv 50–51) | 5% (Lv 50–51) | 5% (Lv 50–51) |
| Gloom | – | – | 30% (Lv 47–48) |
| Noctowl | – | – | 20% (Lv 47–49) |
| Venonat | – | – | 10% (Lv 48) |
| Mightyena | – | – | 5% (Lv 49) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Hoppip | 60% | 10 |
| Goldeen | 30% | 5 |
| Skiploom | 5% | 10 |
| Masquerain | 5% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Goldeen | 30% | 10 |
| Seaking | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 20 |
| Seaking | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Staryu | 40% | 40 |
| Seaking | 30% | 40 |
| Dratini | 20% | 40 |
| Dragonair | 10% | 40 |

Special: Land swarm: Bellsprout; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Route 25

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Sunkern | 30% (Lv 47–49) | 30% (Lv 47–49) | – |
| Weepinbell | 25% (Lv 47–50) | 25% (Lv 47–50) | 25% (Lv 47–50) |
| Buneary | 10% (Lv 48) | 10% (Lv 48) | 10% (Lv 48) |
| Exeggcute | 15% (Lv 48–50) | 15% (Lv 48–50) | 15% (Lv 48–50) |
| Pidgey | 10% (Lv 49) | 10% (Lv 49) | – |
| Vigoroth | 5% (Lv 51–52) | 5% (Lv 51–52) | 5% (Lv 51–52) |
| Combee | 5% (Lv 51–52) | 5% (Lv 51–52) | 5% (Lv 51–52) |
| Venomoth | – | – | 30% (Lv 47–49) |
| Venonat | – | – | 10% (Lv 49) |

**Surfing**

| Pokémon | Chance | Levels |
|---|---|---|
| Hoppip | 60% | 10 |
| Goldeen | 30% | 5 |
| Skiploom | 5% | 10 |
| Masquerain | 5% | 10 |

**Old Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Magikarp | 40% | 10 |
| Goldeen | 30% | 10 |
| Seaking | 30% | 10 |

**Good Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Goldeen | 70% | 20 |
| Seaking | 30% | 20 |

**Super Rod**

| Pokémon | Chance | Levels |
|---|---|---|
| Staryu | 40% | 40 |
| Seaking | 30% | 40 |
| Dratini | 20% | 40 |
| Dragonair | 10% | 40 |

Special: Land swarm: Buneary; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Seaking; Hoenn Sound: Whismur, Linoone; Sinnoh Sound: Buizel, Bidoof

## Tohjo Falls

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Raticate | 25% (Lv 43–44) | 25% (Lv 43–44) | 25% (Lv 43–44) |
| Azumarill | 20% (Lv 43) | 20% (Lv 43) | 20% (Lv 43) |
| Bronzong | 10% (Lv 43) | 10% (Lv 43) | 10% (Lv 43) |
| Slowbro | 15% (Lv 43–45) | 15% (Lv 43–45) | 15% (Lv 43–45) |
| Dewgong | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Golbat | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Quagsire | 10% (Lv 44–45) | 10% (Lv 44–45) | 10% (Lv 44–45) |

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
| Gyarados | 20% | 40 |
| Seaking | 10% | 40 |

Special: Land swarm: Zubat; Surf swarm: Goldeen; Fishing swarm: Magikarp; Night fishing: Goldeen; Hoenn Sound: Crobat, Crobat; Sinnoh Sound: Azurill, Chingling

## Diglett's Cave

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Diglett | 90% (Lv 15–43) | 90% (Lv 15–43) | 90% (Lv 15–43) |
| Dugtrio | 10% (Lv 47–59) | 10% (Lv 47–59) | 10% (Lv 47–59) |

Special: Land swarm: Diglett; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Victory Road 2F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Machoke | 20% (Lv 44) | 20% (Lv 44) | 20% (Lv 44) |
| Golbat | 20% (Lv 44) | 20% (Lv 44) | 20% (Lv 44) |
| Graveler | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Magneton | 10% (Lv 44) | 10% (Lv 44) | 10% (Lv 44) |
| Venomoth | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Kadabra | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Hariyama | 5% (Lv 45) | 5% (Lv 45) | 5% (Lv 45) |
| Lairon | 5% (Lv 45) | 5% (Lv 45) | 5% (Lv 45) |
| Loudred | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |
| Medicham | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |

Special: Land swarm: Graveler; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Victory Road 3F

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Donphan | 20% (Lv 45) | 20% (Lv 45) | 20% (Lv 45) |
| Ursaring | 20% (Lv 45) | 20% (Lv 45) | 20% (Lv 45) |
| Golbat | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Magneton | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Kadabra | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Lairon | 10% (Lv 45) | 10% (Lv 45) | 10% (Lv 45) |
| Mawile | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |
| Sableye | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |
| Gabite | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |
| Metang | 5% (Lv 46) | 5% (Lv 46) | 5% (Lv 46) |

**Rock Smash**

| Pokémon | Chance | Levels |
|---|---|---|
| Graveler | 80% | 24–32 |
| Nosepass | 20% | 30–33 |

Special: Land swarm: Graveler; Hoenn Sound: Absol, Makuhita; Sinnoh Sound: Bronzor, Chingling

## Route 2 North Above Viridian Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Ledian | 30% (Lv 45–46) | 30% (Lv 45–46) | – |
| Caterpie | 20% (Lv 45) | 10% (Lv 45) | – |
| Pidgey | 10% (Lv 45) | 20% (Lv 45) | – |
| Metapod | 10% (Lv 46) | – | – |
| Beautifly | 10% (Lv 47) | 10% (Lv 47) | 5% (Lv 47) |
| Dustox | 5% (Lv 47) | 5% (Lv 47) | 5% (Lv 47) |
| Staravia | 5% (Lv 47) | 5% (Lv 47) | – |
| Pachirisu | 5% (Lv 48–49) | 5% (Lv 48–49) | 5% (Lv 48–49) |
| Cherrim | 5% (Lv 48–49) | 5% (Lv 48–49) | – |
| Butterfree | – | 10% (Lv 46) | – |
| Ariados | – | – | 30% (Lv 45–46) |
| Yanma | – | – | 30% (Lv 45–47) |
| Hoothoot | – | – | 10% (Lv 45) |
| Spinarak | – | – | 10% (Lv 46) |
| Bibarel | – | – | 5% (Lv 48–49) |

Special: Land swarm: Caterpie; Hoenn Sound: Plusle, Minun; Sinnoh Sound: Shinx, Shinx

## Viridian Forest

**Grass/cave**

| Pokémon | Morning | Day | Night |
|---|---|---|---|
| Exeggcute | 20% (Lv 64) | – | – |
| Pikachu | 20% (Lv 64) | – | – |
| Breloom | 10% (Lv 65) | – | – |
| Ledian | 10% (Lv 66) | – | – |
| Butterfree | 10% (Lv 67) | – | – |
| Beedrill | 10% (Lv 67) | – | – |
| Forretress | 5% (Lv 68) | – | – |
| Yanma | 5% (Lv 69) | – | – |
| Wormadam | 5% (Lv 70–71) | – | – |
| Mothim | 5% (Lv 70–72) | – | – |
| Sunkern | – | 20% (Lv 64) | – |
| Weepinbell | – | 20% (Lv 64) | – |
| Illumise | – | 10% (Lv 65) | – |
| Scyther | – | 10% (Lv 66) | – |
| Pinsir | – | 10% (Lv 67) | – |
| Ambipom | – | 10% (Lv 67) | – |
| Pidgeotto | – | 5% (Lv 68) | – |
| Heracross | – | 5% (Lv 69) | – |
| Volbeat | – | 5% (Lv 70–71) | – |
| Grumpig | – | 5% (Lv 70–72) | – |
| Murkrow | – | – | 20% (Lv 64) |
| Misdreavus | – | – | 20% (Lv 64) |
| Ariados | – | – | 10% (Lv 65) |
| Gloom | – | – | 10% (Lv 66) |
| Parasect | – | – | 10% (Lv 67) |
| Beautifly | – | – | 10% (Lv 67) |
| Dustox | – | – | 5% (Lv 68) |
| Carnivine | – | – | 5% (Lv 69) |
| Kricketune | – | – | 5% (Lv 70–71) |
| Tropius | – | – | 5% (Lv 70–72) |

Special: Land swarm: Heracross; Hoenn Sound: Shiftry, Vileplume; Sinnoh Sound: Ambipom, Raichu

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
