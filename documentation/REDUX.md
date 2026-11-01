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
