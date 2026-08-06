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
- [x] Source 2 CC0 audio loops — done 2026-08-06 (DECISIONS.md #024): `assets/audio/rain.ogg` (freesound.org/s/242889, CC0, 48s) and `assets/audio/ops.ogg` (freesound.org/s/715475, CC0, 1:42)
- [x] Quality review of all 22 generated images — 2026-08-06 (DECISIONS.md #025). Found real problems, not cosmetic. Mislabeling fixed mechanically; content/policy issues need your call.
- [x] 22/22 placed in `assets/images/*.webp` (GD001, EN002, DB001 all re-sent 2026-08-06; EN002 confirmed correct — "HACK METH" signage passes review)
- [ ] **Decision needed — DB001 (Mission Debrief):** re-sent, content/checklist now accurate to the real 9-room scope, but the "Next Destination" panel reads both "HACK METH" and "RED TEAM OPS AWAITS" in the same image — self-contradicting, and the latter violates DECISIONS.md #012. Also bakes in "YES / NOT YET" buttons as static art — those need to be real HTML controls at build time.
- [ ] **Decision needed — GD001 (Google Dorking):** re-sent and placed, but bakes in a fully simulated dork query + 10 fake result URLs — same #007/SRS FR-18 violation as the terminal-room trio below.
- [ ] **Decision needed — D003 (Mission Board):** bakes in all 22 concept-art keys as fully unlocked/labeled, including "MISSION DEBRIEF" and "CHECK-OUT" as hub entries — violates #011 (locked-placeholder requirement) and the Scene Bible. Regenerate with only 9 active keys + inert locked placeholders, or accept as reference art and rebuild the key state in HTML/CSS at Milestone 3 (labels/lock-state never baked into the image in the first place)?
- [ ] **Decision needed — SG001 (SignalGate) / FC001 (Fiery Cross Reef):** both bake in fabricated specifics not in the source deck (dramatized "targets confirmed / time to execute" chat text; an invented date/coordinates) — Creative Bible §4 fidelity/sensitivity concern for real, sensitive incidents. Regenerate with less invented specificity, or accept as atmospheric/non-literal?
- [ ] **Decision needed — TC001 / ST001 / GP001 / GD001 (all 4 terminal rooms):** all bake in full simulated tool output (theHarvester/Sherlock/SpiderFoot text, a SET menu, a populated GoPhish dashboard, a dork query + results) — violates #007/SRS FR-18's explicit "no simulated tool output" rule. Regenerate with idle/blank screens, or crop/edit the existing art to blank the screens before use?
- [ ] Remaining 13 Asset Register rows (F002, SG002, FC002, EX001, EX002, DD001, UI001-UI003, EE001-EE004) are HTML/SVG/CSS build-time components, not image-generated — deferred to Milestone 3, not a Milestone 2 gap

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
