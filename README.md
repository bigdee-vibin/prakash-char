# Prakāśa-chara — In Plain Sight

An offline, scroll- and click-driven training experience introducing OSINT & Social Engineering (IW/HAK/15.3). Ships as a single self-contained `index.html` + local `assets/` folder — no server, no runtime internet, no external dependencies. See [PROJECT.md](PROJECT.md) for the full vision and [CLAUDE.md](CLAUDE.md) for build constraints and tooling.

## Current status

**Milestone 2 in progress** (asset generation). Milestone 1 (full software specification) is complete. See [TODO.md](TODO.md) for the live checklist and [DECISIONS.md](DECISIONS.md) for the running architecture-decision log — read that log before touching scope, naming, or tooling, since several early assumptions (e.g. image-generation provider, the hub's name, signage text) were revised there.

## Repository layout

```
├── CLAUDE.md, PROJECT.md, DECISIONS.md, TODO.md   # governing docs — read these first
├── docs/
│   ├── SRS.md                       # requirements
│   ├── Architecture.md              # build pipeline, runtime architecture, data schemas
│   ├── Creative_Bible.md            # world, tone, sensitivity rules for real case studies
│   ├── UI_Style_Guide.md            # palette, typography, motion, watermark spec
│   ├── Component_Specification.md   # every reusable UI component
│   ├── Scene_Bible.md               # scene-by-scene breakdown, source-slide traceability
│   ├── Repository_Audit.md          # point-in-time repo audit (2026-08-06)
│   ├── Asset_Register_v1.0.xlsx     # master asset tracker — status/priority/source per asset
│   └── OSINT_Hotel_Scrollytelling_Brief.md   # original creative brief
├── ppt/                             # source decks (OSINT SE Session.pptx is authoritative; the second deck is reference-only, DECISIONS.md #009)
├── prompts/                         # concept-art prompt library (style_lock.md + assets.json)
├── scripts/                         # build-time Python tooling (image generation, etc.)
├── assets/
│   ├── images/                      # generated concept art (.webp), Asset Register naming convention
│   ├── audio/                       # sourced CC0 ambient loops (.ogg)
│   └── concept_art/                 # early exploratory art, pre-dates the Asset Register
├── images/                          # gitignored staging folder for manually-generated art before conversion
└── requirements.txt                 # Python deps for build scripts
```

## Setup

1. Clone the repo and create a Python virtualenv:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in whichever keys you actually need (none are required to read/build docs; API keys are only for build-time asset generation):
   ```bash
   cp .env.example .env
   ```
   `.env` is gitignored — never commit real keys.
3. Build-time tools referenced in `CLAUDE.md` (`ffmpeg`, `ImageMagick`, `Pandoc`) are installed via Homebrew as needed, not bundled in this repo.

## Asset generation workflow

Concept art is currently sourced via **manual ChatGPT generation** (DECISIONS.md #023), not an API — Gemini/Imagen (`scripts/generate_images.py`) is built but blocked on billing, and an Unsplash-photo+overlay hybrid was explored and abandoned. Prompts live in `prompts/assets.json` and the current handoff batch in `prompts/remaining_18_prompts.md`. Generated images are converted to `.webp` and placed in `assets/images/` under the filename each Asset Register row specifies.

Audio loops are sourced from Freesound (CC0) — see `assets/audio/` and DECISIONS.md #024 for exact tracks and attribution.

## Definition of done

Per [PROJECT.md](PROJECT.md): double-clicking the final `index.html` runs the complete experience offline, with zero network requests. See [docs/SRS.md](docs/SRS.md) §7 for the full acceptance criteria.
