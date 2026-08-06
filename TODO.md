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

## M2 — Prompt library & asset generation (core work complete — 2026-08-06)
- [x] Build prompts/ library (style-lock preamble + per-asset prompts) — [prompts/style_lock.md](prompts/style_lock.md), [prompts/assets.json](prompts/assets.json)
- [x] Sourcing method decided: ChatGPT manual generation for all 22 image assets (DECISIONS.md #020–#023; Gemini/Imagen and Unsplash paths built but unused — left in place, not deleted)
- [x] Source 2 CC0 audio loops — done 2026-08-06 (DECISIONS.md #024): `assets/audio/rain.ogg` (freesound.org/s/242889, CC0, 48s) and `assets/audio/ops.ogg` (freesound.org/s/715475, CC0, 1:42)
- [x] Quality review of all 22 generated images — 2026-08-06 (DECISIONS.md #025)
- [x] 22/22 placed in `assets/images/*.webp`
- [x] Remaining 13 Asset Register rows (F002, SG002, FC002, EX001, EX002, DD001, UI001-UI003, EE001-EE004) confirmed as HTML/SVG/CSS build-time components, not image-generated — correctly deferred to Milestone 3

### Backlog — regeneration requested 2026-08-06 (DECISIONS.md #026), waiting on returned images
Corrected prompts for all 8 sent as `prompts/regenerate_8_flagged.md` (zipped, handed to user). Once returned: convert to `.webp`, place in `assets/images/`, update Asset_Register + prompts/assets.json, re-verify in `index.html`.
- [ ] **D003 (Mission Board)** — reprompted with zero baked-in labels (all labeling/lock-state stays in the runtime overlay, which already renders correctly)
- [ ] **DB001 (Mission Debrief)** — reprompted for a single "HACK METH" destination, no baked-in buttons
- [ ] **SG001 (SignalGate) / FC001 (Fiery Cross Reef)** — reprompted to drop fabricated dramatized content/invented specifics
- [ ] **GD001 / TC001 / ST001 / GP001 (all 4 terminal rooms)** — reprompted for idle/blank screens, no simulated tool output

## M3 — HTML engine build (first working run-through — 2026-08-06)
- [x] `index.html` built as a single self-contained file (Decision 002) — scroll engine (C-2), camera transitions (C-3, simplified), Mission Board hub (C-4/C-4a/C-4b), narrative rooms (C-5), terminal rooms + Pause-for-Demo (C-6/C-6a), case study card accent (C-7), check-out controller (C-8), back-to-reception (C-9), watermark (C-10), audio controller (C-11)
- [x] Full run-through tested in-browser end to end: Cold Open → Operations Centre → Monitor Wall → Pull → Lane → Reception → Mission Board (9 keys + 7 locked placeholders) → all 9 rooms → Check Out → Decision → Mission Brief → Debrief → Lane Return → Cliffhanger
- [x] Verified zero network requests (all `file://`, satisfies NFR-1) and no console errors
- [x] Fixed 2 bugs found during testing: "Back to Reception" button visible before entering a room; cliffhanger caption text duplicating/overlapping text already baked into the EN002 art
- [ ] Implement schemas as `schemas/*.schema.json` (drafted in Architecture.md §5) — data is currently inlined directly in index.html rather than schema-validated, a pragmatic simplification for a single-file artifact
- [ ] Wire in UI components (Mission Log, Notebook, Evidence Card — UI001-UI003) — not yet built
- [ ] Easter Egg Wall monitors (EE001-EE004) — not yet built, Monitor Wall scene currently shows only the background art
- [ ] Keyboard navigation for Mission Board keys — currently click-only, not yet keyboard-focusable (SRS NFR-7 gap)
- [ ] Bundle real fonts per UI_Style_Guide §2 — currently using system font-stack fallback only
- [ ] Camera transitions (Scene 2 zoom, Scene 4 rotate) implemented as scroll-snap + fade rather than the CSS 3D transforms Architecture §11 flagged as unvalidated — reliability chosen over full visual fidelity
- [ ] The 4 backlog image issues (D003, DB001, GD001, terminal-room simulated output) are now live in the running experience — see below

## M4 — Documentation deliverables (complete — 2026-08-06)
- [x] Speaker notes — [docs/Speaker_Notes.md](docs/Speaker_Notes.md)
- [x] Instructor guide — [docs/Instructor_Guide.md](docs/Instructor_Guide.md) (setup, session flow, all 4 demo-handoff pre-staging steps, troubleshooting, known display caveats)
- [x] Build scripts documented — [scripts/README.md](scripts/README.md)

### Also fixed during this pass (not milestone-scoped, found via use)
- [x] Removed redundant eyebrow text from Cold Open title card
- [x] Simplified "The Turn — OSINT Hotel" / "Enter the Hotel" to "The Turn" / "Enter"
- [x] Scroll feel: switched hard `mandatory` snap to `proximity` + cross-fade between scenes (was jerky)
- [x] Audio: added a low-pass filter + reduced volume (was harsh) so ambient loops read as subtle/distant rather than raw recordings

## M5 — Packaging & release (complete — 2026-08-06)
- [x] `scripts/package_release.py` built and run — copies `index.html` + `assets/images/` + `assets/audio/` into `release/`, verifies zero `http(s)://` refs and that every asset path resolves, zips to `Prakasha-chara_v1.0.zip` (8.8MB, well under the 150MB budget)

## M5 — Packaging & release
- [ ] Package release (release ZIP + build scripts)
