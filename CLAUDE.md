# Pokémon HeartGold Redux

This repo is Pokémon HeartGold Redux, a fork of hg-engine. Before making changes, read
`documentation/REDUX_CHANGES.md`. It lists every change from upstream, the design rules,
and the work still planned.

- Record each change in `documentation/REDUX_CHANGES.md` in the same commit.
- Prefer hg-engine's existing code and config toggles over new code. Keep experimental or
  unstable features off. The developer can only test by building and playing locally.
- The ROM (`rom.nds`) is not in the repo, so a full `make` isn't possible in cloud sessions.
  Compile-check C changes with `arm-none-eabi-gcc -fsyntax-only` and the `Makefile` `CFLAGS`.
- `data/learnsets/learnsets.json` is generated. Change learnsets through
  `data/learnsets/base/custom.json` and regenerate it with the command in the changes file.
