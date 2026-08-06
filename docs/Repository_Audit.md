# Repository Audit — Prakāśa-chara: In Plain Sight

**Date:** 2026-08-06
**Scope:** Full repository read (excluding `.git` internals and `.venv` third-party packages). No application code was written or modified as part of this audit, per instruction.
**Governing document:** `/Users/dheerajbharti/CLAUDE.md` (Karpathy Guidelines) + `CLAUDE.md` (project build instructions).

---

## 1. Current Repository Structure

```
prakash-char/
├── .env                                    # OPENAI_API_KEY, FIRECRAWL_API_KEY (real values; correctly gitignored)
├── .gitignore
├── .venv/                                  # local Python 3.9 virtualenv (gitignored, not tracked)
├── CLAUDE.md                               # governing build instructions (this project)
├── DECISIONS.md                            # 7 numbered architecture decisions
├── LICENSE                                 # MIT, copyright "bigdee-vibin" 2026
├── PROJECT.md                              # vision + definition of done
├── README.md                               # 2-line stub
├── TODO.md                                 # 8-item master checklist, all unchecked
├── requirements.txt                        # 34 pinned Python packages (openai, firecrawl-py, pillow, etc.)
├── assets/
│   └── concept_art/
│       ├── 5AB9839E-EFB9-4B07-A4CC-2293FA9FEB66.jpeg      (438 KB)
│       ├── a_dramatic_cinematic_poster_banner_style_scene_ov.png  (2.2 MB)
│       ├── a_dramatic_cinematic_poster_like_digital_illustra.png  (2.0 MB)
│       └── PrakashaChara_Images_Sprint01.zip               (4.7 MB — duplicate archive of the 3 files above)
├── docs/
│   ├── Asset_Register_v1.0.xlsx            # 33-row asset tracker (see §4)
│   └── OSINT_Hotel_Scrollytelling_Brief.md # design brief for Segments 1, 4, 5 + 3 case studies
└── ppt/
    ├── OSINT SE Session.pptx               # 27 slides — primary source content (IW/HAK/15.3)
    └── 04 OSINT 1.pptx                     # 23 slides — companion BIWC-style deck (15 MB, Class 4 of 6)
```

**Not present anywhere in the tree:** `index.html`, any `.css`/`.js` file, a `src/`, `scripts/`, `build/`, `release/`, `prompts/`, `schemas/`, or `audio/` directory. **The build has not started** — the repository currently contains only source inputs and planning documents.

### Working-tree state (uncommitted)
`git status` shows the repo mid-reorganization: four files were deleted from the repo root (`5AB9839E...jpeg`, `PrakashaChara_GitHub_Starter_Kit.zip`, and the two poster PNGs) and are now untracked under `assets/`, `docs/`, `ppt/`, plus new `.gitignore` and `requirements.txt`. This is a straightforward "unzip the starter kit into proper folders" move — confirmed by inspecting `PrakashaChara_GitHub_Starter_Kit.zip` at its last committed revision (`ec4531a`): its contents map 1:1 onto the current `assets/`, `docs/`, `ppt/` layout, so no source content was lost. Nothing is currently staged or committed for this reorganization.

**One file from the starter kit was not carried forward:** the kit contained a nested `PrakashaChara_GitHub_Handoff_Files.zip`, which in turn held `README.md`, `CLAUDE.md`, `PROJECT.md`, `TODO.md`, `DECISIONS.md` (all already present at repo root, content matches) **and a `.env.example` template** (`OPENAI_API_KEY=` / `FIRECRAWL_API_KEY=`, empty values) that was never extracted into the working tree. See §2.

---

## 2. Missing Documentation

| Item | Why it matters |
|---|---|
| `.env.example` | Was present in the original handoff bundle but never extracted; without it, a new contributor has no template for the two required API keys and no confirmation of which env vars the build scripts expect. |
| **Content mapping doc** (pptx segments → HTML scenes) | `OSINT_Hotel_Scrollytelling_Brief.md` explicitly covers only Segments 1, 4, 5 + 3 case studies of the 27-slide `OSINT SE Session.pptx`. Segments 2, 3, 6, 7, 8 are called out as "stays live-demo" but there is no document mapping *all* 27 slides (or the second deck's 23 slides) to a build artifact, so it's not traceable which slide content is fully covered, dropped, or pending a decision. |
| **Speaker notes** (explicit CLAUDE.md deliverable) | No file, folder, or stub exists. |
| **Instructor guides** (explicit CLAUDE.md deliverable) | No file, folder, or stub exists. |
| **Build scripts documentation** (explicit CLAUDE.md deliverable) | No `scripts/` folder or README describing the OpenAI Images / Firecrawl / ffmpeg / ImageMagick / Pandoc build pipeline exists yet. |
| **Release process doc** | CLAUDE.md requires a "Release ZIP" deliverable; no packaging/versioning process is documented. |
| **README.md expansion** | Current README is a 2-line stub with no setup instructions, no explanation of `requirements.txt`, no pointer to `PROJECT.md`/`CLAUDE.md`/`DECISIONS.md`. |
| **Second deck's relationship to the brief** | `04 OSINT 1.pptx` ("BIWC deck" per CLAUDE.md's primary inputs) is a distinct 6-class series (Class 4 of 6) with different content (e.g., "Pentagon Pizza Meter") from `OSINT SE Session.pptx`. No document states how/whether this second deck's content is folded into the single `index.html` experience. |

---

## 3. Missing Folders

| Folder | Purpose implied by CLAUDE.md / brief |
|---|---|
| `src/` or equivalent | Where the vanilla HTML/CSS/JS for `index.html` would be authored before freezing into the final static file. |
| `scripts/` | Build-time tooling: OpenAI Images generation calls, Firecrawl scraping, ffmpeg/ImageMagick asset processing, Pandoc doc generation — `requirements.txt` implies Python scripts exist or are planned, but none are checked in. |
| `prompts/` | Per-asset image-generation prompt library (see §5). |
| `schemas/` | JSON schema definitions for scene data / asset manifest (see §6). |
| `audio/` | Destination for the two CC0 ambient tracks listed in the Asset Register (`rain.ogg`, `ops.ogg`) — currently nothing exists even as a placeholder folder. |
| `release/` | CLAUDE.md deliverable "Release ZIP"; `.gitignore` already reserves `release/` and `build/` but neither exists yet. |
| `docs/instructor/` and `docs/speaker-notes/` (or similar) | To house the two documentation deliverables above once produced. |

---

## 4. Missing Assets

`docs/Asset_Register_v1.0.xlsx` catalogs **33 planned assets** across Opening, Cold Open, Cyber Lane, Reception, Foundations, Case Study (SignalGate, Fiery Cross Reef), Demo, Ethics, Bridge, Exercise, Decision, Debrief, Ending, UI, and Audio categories. Status breakdown:

- **1 of 33** marked `Draft` (A002 — Ancient Spotlight)
- **31 of 33** marked `To Generate`
- **2 of 33** marked `To Source` (both audio)
- **0 of 33** marked `Ready`/`Final`

The four files physically present in `assets/concept_art/` (one JPEG, two PNGs, one redundant zip bundling the same three) **do not match the Asset Register's ID/filename convention** (`A001_mission_splash.webp`, etc.) — they appear to be unregistered exploratory concept art, not registry-tracked, finished assets. Effectively **0 of 31 registry-tracked visual assets and 0 of 2 audio assets currently exist as finished, correctly named files.**

Specifically missing, high-priority (per register's "High" priority flag — 29 of 33 rows):
- Mission Splash / Ancient Spotlight (Opening) — `.webp`, not yet generated despite being highest-priority
- Operations Centre, Monitor Wall, Screen Pull (Cold Open)
- Cyber Lane, OSINT HQ exterior, HACK METH exterior (Cyber Lane)
- Reception Lobby, Key Wall (Reception hub — brief's central navigation mechanic)
- Foundations Room + Source Board
- SignalGate Room + Timeline graphic
- Fiery Cross Reef Room + Cable Overlay map
- Google Dorking / Tool Chain / SET / GoPhish terminal-room art (the brief's 4 "pause-for-demo" rooms)
- Grey Areas Room, SE Bridge
- Exercise (Mission Control, Apex Dossier), Decision Screen, Mission Debrief
- Lane Return, HACK METH Reveal (ending beats)
- Reusable UI components: Mission Log HUD, Notebook widget, Evidence Card (SVG/HTML — these are buildable in-code, not image-generated, but no stub exists)
- `rain.ogg`, `ops.ogg` ambient audio loops (CC0-sourced, per register)

Also missing: a **watermark asset** implementing Decision 006 ("Persistent watermark: Lt Col Dheeraj Bharti ©2026") — no watermark graphic, CSS overlay, or spec for where/how it renders exists yet.

Additional source assets referenced by the brief but not yet in the repo: SignalGate reporting screenshots/timeline graphic, PLA Fiery Cross Reef broadcast frame-grab, and verified Gulf strike footage/geolocation map (brief explicitly allows labelled placeholders if unavailable — no placeholder convention has been established in-repo yet).

---

## 5. Missing Prompts

The Asset Register designates **"OpenAI Images"** as the source for roughly 24 of the 33 assets, and CLAUDE.md names the OpenAI Images API as a build-time tool — but **no prompt library exists anywhere in the repository.** There is no `prompts/` folder, no `prompts.json`, no per-asset prompt text, negative prompts, style-lock phrases, or seeds. This means:
- The two already-drafted concept art pieces in `assets/concept_art/` have no recorded prompt provenance (can't be regenerated or iterated with confidence).
- Nothing captures the Design Language section of the brief (Tron-adjacent palette, scan-line/VHS grain, monospace/geometric-sans typography, katakana-flavoured background glyphs) as reusable, consistent prompt fragments — a real risk for visual drift across 24+ separately generated images (see §9).

---

## 6. Missing JSON Schemas

No `.json` or `.schema.json` files exist in the repository. Given the brief's described interaction model (a non-linear key-wall hub, per-key state — greyed-out vs. lit — and scroll-stage progression for the linear scenes), a data-driven build would need at minimum:
- A **scene/room manifest schema** (id, title, asset refs, entry trigger, exit trigger, demo-pause flag)
- A **key-wall state schema** (key id → visited/locked/lit state, to drive the "auto-triggers once all keys visited" check-out logic)
- An **asset manifest schema** tying `Asset_Register_v1.0.xlsx` rows to actual filenames/paths (the register itself is the only current source of truth, in spreadsheet form, not machine-readable JSON)
- A **content-mapping schema** linking pptx slide numbers to scene IDs (ties into the missing content-mapping doc in §2)

None of these exist yet, even as drafts.

---

## 7. Missing HTML Components

**Zero HTML/CSS/JS exists in the repository.** No `index.html`, no component files, no stylesheet, no script. Per the brief and CLAUDE.md, the following components will eventually be required and have no current scaffold:
- Scroll-driven scene container/engine (Scenes 0–4, 8–10 per the brief's linear "walk")
- Click-driven hub navigation for the Key Wall (Scenes 5–7)
- The reusable "Pause-for-Demo" interstitial component (`>> LIVE DEMO — see instructor workstation`) — explicitly called out in the brief as needing a **distinct, reusable UI treatment**, used identically across 4 terminal rooms
- Persistent watermark overlay (Decision 006)
- UI widgets cataloged in the Asset Register: Mission Log (HUD), Notebook, Evidence Card
- Audio playback/ambience controller for the two ogg loops
- Any asset-loading/preload strategy for an offline, air-gapped, single-file deployment (CLAUDE.md requires "no runtime internet," meaning all assets must be inlined or bundled — no strategy for this is documented yet)

---

## 8. Missing Audio

Both audio assets in the register (`AU001` — Rain / ambient loop, `AU002` — Operations / SOC ambience) are marked `To Source`, CC0 licensed, with target filenames `rain.ogg` and `ops.ogg`. **Neither file exists in the repository, and no `audio/` folder or sourcing note (e.g., candidate CC0 URLs) has been recorded.** The brief does not otherwise call for voice-over or narration audio, so this is the full scope of the audio gap.

---

## 9. Risks

1. **Scale mismatch between ambition and current completion.** The brief specifies a 10-scene, non-linear, scroll-and-click hybrid experience with ~33 tracked assets, 4 distinct demo-pause interstitials, and a full pptx-to-scene mapping — and the repository currently has 0% of the HTML build, 0% of the audio, and effectively 0% of the registry-tracked visual assets complete. This is a large amount of remaining work relative to what exists today.
2. **No prompt library = inconsistent visual style risk.** With ~24 images to be independently generated via the OpenAI Images API and no shared prompt/style-lock record, later-generated assets risk drifting from the two existing drafts and from each other (palette, grain texture, typography treatment).
3. **API keys live in `.env` at repo root.** Correctly gitignored and not committed — but there is no `.env.example`, so the convention isn't self-documenting for anyone else who clones this repo, and a careless `git add -A` or gitignore edit is one mistake away from committing real secrets.
4. **Two source decks with unclear content boundaries.** `OSINT SE Session.pptx` (27 slides, IW/HAK/15.3) and `04 OSINT 1.pptx` (23 slides, 15 MB, "Class 4 of 6," different framing/examples e.g. "Pentagon Pizza Meter") both sit in `ppt/` as "primary inputs" per CLAUDE.md, but only the first is addressed by the existing scrollytelling brief. Without a decision on the second deck's role, later content-integration work risks scope confusion or duplicated/conflicting content.
5. **Uncommitted large reorganization.** The current working tree has 4 deletions and 5 new untracked paths (some large: `04 OSINT 1.pptx` at 15 MB) sitting uncommitted. Until committed, this state is fragile — a `git checkout`/`clean`/`reset` run without care could lose the reorganization work (though the underlying content itself is recoverable from commit `ec4531a`, as verified in this audit).
6. **Offline/air-gapped constraint vs. large binary assets.** CLAUDE.md mandates a single `index.html`, vanilla only, no runtime internet. With ~2 MB+ PNGs already in play and 24 more images plus 2 audio loops still to add, the "freeze all outputs into static assets" instruction will need an explicit asset-compression/inlining strategy (e.g., `.webp` as the register already specifies) to keep the final artifact a reasonable size — no such budget or strategy is documented yet.
7. **`requirements.txt` exists but no build entrypoint script does.** The pinned dependencies (openai, firecrawl-py, pillow, etc.) imply a Python build pipeline is intended, but there's no script yet that uses them — so it's not verified that the pinned versions actually work together, or what the pipeline's entrypoint/invocation will look like.
8. **License clarity for third-party source material.** The repo brief references real-world incident material (SignalGate reporting, PLA Fiery Cross Reef broadcast, Gulf strike footage) that may carry copyright/licensing constraints distinct from the repo's own MIT license (which covers the software, not necessarily embedded journalistic imagery). The brief itself acknowledges this ("stand-in composite if licensing is unclear") but no formal policy is recorded in `DECISIONS.md`.

---

## 10. Recommended Milestone Plan

**M0 — Repository hygiene (small, do first)**
- Commit the pending reorganization (`assets/`, `docs/`, `ppt/`, `.gitignore`, `requirements.txt`)
- Add `.env.example` (recovered content: `OPENAI_API_KEY=`, `FIRECRAWL_API_KEY=`)
- Expand `README.md` with setup/run instructions
- Verify: `git status` clean, fresh clone + `pip install -r requirements.txt` succeeds

**M1 — Content mapping & schema foundation**
- Produce the pptx-segment-to-scene mapping doc (all 27 + 23 slides accounted for, explicitly marking what's in-scope for `index.html` vs. live-demo-only)
- Decide and document the second deck's (`04 OSINT 1.pptx`) role
- Draft JSON schemas: scene manifest, key-wall state, asset manifest, content mapping
- Verify: every register row and every pptx segment has a documented destination (scene, live-demo pause, or explicitly out-of-scope)

**M2 — Prompt library & asset generation (High-priority assets first)**
- Build the `prompts/` library: one style-lock preamble + per-asset prompt, covering all "High" priority rows in the Asset Register
- Generate the 29 "High"-priority `To Generate` visual assets via OpenAI Images, correctly named per the register's `File Name` convention
- Source the 2 CC0 audio loops
- Verify: Asset Register status column reflects `Ready` for all High-priority rows; filenames match convention

**M3 — HTML engine build**
- Build `index.html` scaffold: scroll engine (linear scenes), click-hub engine (key wall), reusable pause-for-demo component, watermark overlay
- Wire in UI components (Mission Log, Notebook, Evidence Card)
- Integrate generated assets and audio
- Verify: double-click `index.html` runs fully offline (per `PROJECT.md` Definition of Done), no network requests fire, all 10 scenes reachable

**M4 — Documentation deliverables**
- Write speaker notes and instructor guides
- Document the build scripts (`scripts/`) that produced the frozen assets
- Verify: a new instructor can run the experience and follow the 4 demo-pause handoffs using only the guides

**M5 — Packaging & release**
- Build the release ZIP packaging script
- Final QA pass against `PROJECT.md`'s Definition of Done and all 7 items in `DECISIONS.md`
- Verify: release ZIP unzips and runs standalone on a machine with no prior repo state

---

*This audit performed no writes to application code, `index.html`, or asset files. `TODO.md` has been updated separately to reflect these findings.*
