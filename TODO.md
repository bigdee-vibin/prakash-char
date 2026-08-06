# Master TODO

- [x] Read all project documents
- [x] Bootstrap repository
- [x] Repository audit (see [docs/Repository_Audit.md](docs/Repository_Audit.md)) — 2026-08-06

## M0 — Repository hygiene
- [x] Commit pending reorganization (assets/, docs/, ppt/, .gitignore, requirements.txt) — committed in Milestone 1
- [x] Add .env.example — done 2026-08-06 (UNSPLASH_*, GEMINI_API_KEY, OPENAI_API_KEY, FIRECRAWL_API_KEY)
- [x] Expand README.md with setup/run instructions — done 2026-08-06

## M1 — Software specification (complete — 2026-08-06)
- [x] SRS — [docs/SRS.md](docs/SRS.md)
- [x] Architecture — [docs/Architecture.md](docs/Architecture.md) (incl. scene manifest / Mission Board state / asset manifest / content-mapping schema drafts)
- [x] Creative Bible — [docs/Creative_Bible.md](docs/Creative_Bible.md)
- [x] UI Style Guide — [docs/UI_Style_Guide.md](docs/UI_Style_Guide.md)
- [x] Component Specification — [docs/Component_Specification.md](docs/Component_Specification.md)
- [x] Scene Bible — [docs/Scene_Bible.md](docs/Scene_Bible.md)
- [x] Resolved: Mission Board scope frozen at 9 Version-1 rooms; concept-art's extra rooms become locked/"Coming Soon" placeholders only ([DECISIONS.md](DECISIONS.md) #011)
- [x] Resolved: `04 OSINT 1.pptx` is reference-only for Version 1, not mapped into scenes (DECISIONS.md #009)
- [x] Resolved: SignalGate and Fiery Cross Reef stay separate rooms (DECISIONS.md #010)
- [x] Resolved: Decision Dilemma (slide 26) and Debrief (slide 27) placed as their own scenes, with a new Mission Brief scene between them

### Open decisions before Milestone 2 (see SRS §8.2, Scene Bible §3) — ALL RESOLVED 2026-08-06
- [x] "RED TEAM OPS" (brief) vs. "HACK METH" (Asset Register / concept art) — **HACK METH prevails** (DECISIONS.md #012)
- [x] "Mission Brief" scene asset — **EX001 reused**, EX002 stays out-of-scope (DECISIONS.md #013)
- [x] Slide 13 ("Where AI Fits In OSINT Now") placement — **narrative lead-in inside Room 7b (OSINT Tool Chain), before the Pause-for-Demo interstitial** (DECISIONS.md #014)
- [x] Easter Egg Wall assets — **registered as EE001–EE004**, category Cold Open, Medium priority, Source HTML/CSS (DECISIONS.md #015)
- [x] Minimum hardware spec — **confirmed**: dual-core ~2.0GHz+, 8GB RAM, integrated graphics, 1280x800 min., evergreen browser (DECISIONS.md #016); size budget ≤150MB (DECISIONS.md #017)
- [x] Audio requirement firmness — **required to ship** (stays High priority), but playback failure remains non-blocking per NFR-6 (DECISIONS.md #018)
- [x] Cold Open / Operations Centre split — **confirmed** as Scene Bible §2.1 interpreted it (DECISIONS.md #019)

## M2 — Prompt library & asset generation
- [x] Build prompts/ library (style-lock preamble + per-asset prompts) — [prompts/style_lock.md](prompts/style_lock.md), [prompts/assets.json](prompts/assets.json)
- [x] Sourcing method decided: ChatGPT manual generation for all 22 image assets (DECISIONS.md #020–#023; Gemini/Imagen and Unsplash paths built but unused — left in place, not deleted)
- [x] 17/22 generated and placed → `assets/images/*.webp`: A001, A002, B001, B002, B003, C001, C004, C005, D001, D003, F001, FC001, GA001, GD001, SB001, SG001, TC001
- [ ] 5/22 pending: ST001, GP001, DB001, EN001, EN002 — prompts in [prompts/remaining_18_prompts.md](prompts/remaining_18_prompts.md), zipped and sent 2026-08-06
- [ ] Remaining Easter Egg Wall assets (EE001-EE004, HTML/CSS) — build-time, not image-generated, deferred to Milestone 3
- [x] Source 2 CC0 audio loops — done 2026-08-06 (DECISIONS.md #024): `assets/audio/rain.ogg` (freesound.org/s/242889, CC0, 48s) and `assets/audio/ops.ogg` (freesound.org/s/715475, CC0, 1:42)

## M3 — HTML engine build
- [ ] Implement schemas as `schemas/*.schema.json` (drafted in Architecture.md §5)
- [ ] Build HTML engine (scroll engine, Mission Board hub, pause-for-demo component, watermark overlay)
- [ ] Wire in UI components (Mission Log, Notebook, Evidence Card)
- [ ] Integrate content and assets

## M4 — Documentation deliverables
- [ ] Generate speaker notes
- [ ] Generate instructor guides
- [ ] Document build scripts

## M5 — Packaging & release
- [ ] Package release (release ZIP + build scripts)
