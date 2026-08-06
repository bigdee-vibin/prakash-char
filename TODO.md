# Master TODO

- [x] Read all project documents
- [x] Bootstrap repository
- [x] Repository audit (see [docs/Repository_Audit.md](docs/Repository_Audit.md)) — 2026-08-06

## M0 — Repository hygiene
- [ ] Commit pending reorganization (assets/, docs/, ppt/, .gitignore, requirements.txt)
- [ ] Add .env.example (OPENAI_API_KEY=, FIRECRAWL_API_KEY=)
- [ ] Expand README.md with setup/run instructions

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

### Open decisions before Milestone 2 (see SRS §8.2, Scene Bible §3)
- [ ] Slide 13 ("Where AI Fits In OSINT Now") placement — no scene assigned yet
- [ ] "RED TEAM OPS" (brief) vs. "HACK METH" (Asset Register / concept art) — signage naming conflict, needs one canonical name before generating Lane/Ending signage art
- [ ] "Mission Brief" scene — confirm whether `EX001`/`EX002` (currently registered under out-of-scope "Exercise"/Segment 8) are repurposed, or new assets are registered
- [ ] Easter Egg Wall assets (Python/Networking/PowerShell/Bash monitor loops) — not yet rows in the Asset Register
- [ ] Minimum hardware spec (training-room baseline) — needed for performance/size budgets
- [ ] Audio requirement firmness (required-by-launch vs. nice-to-have)
- [ ] Cold Open / Operations Centre split — confirm the Scene Bible §2.1 interpretation (new title-splash beat + reassigned dark-ops-room beat) is what was intended

## M2 — Prompt library & asset generation
- [ ] Resolve open decisions above (esp. signage naming — affects generated art)
- [ ] Build prompts/ library (style-lock preamble + per-asset prompts)
- [ ] Generate remaining artwork — 29 High-priority "To Generate" assets in Asset_Register_v1.0.xlsx
- [ ] Register the 4 missing Easter Egg Wall assets + reconcile Mission Brief asset
- [ ] Source 2 CC0 audio loops (rain.ogg, ops.ogg)

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
