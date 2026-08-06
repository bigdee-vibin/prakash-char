# Build Scripts

Build-time only — never referenced by `index.html`, never run at delivery time.

## `generate_images.py`
Concept-art generation via the Gemini API (Imagen). **Currently unused** — blocked by a 0 image-model quota on the free tier (DECISIONS.md #020/#021). All 22 image assets were generated manually via ChatGPT instead (DECISIONS.md #023). Kept in case billing is enabled later and the pipeline is revisited.

```bash
python3 scripts/generate_images.py --dry-run           # print prompts, no API calls, no cost
python3 scripts/generate_images.py --only A001,C005    # generate specific assets
```

## `package_release.py`
Packages the shippable artifact (Milestone 5). Copies `index.html` + `assets/images/` + `assets/audio/` into `release/`, verifies zero `http(s)://` references and that every asset path `index.html` references actually resolves, then zips it.

```bash
python3 scripts/package_release.py v1.0
# -> release/  and  Prakasha-chara_v1.0.zip at the repo root
```

Does **not** include `assets/concept_art/` (pre-Asset-Register exploratory art, not a shipped asset), `docs/`, `ppt/`, `prompts/`, or `scripts/` — those are source material, not part of the offline delivery artifact.
