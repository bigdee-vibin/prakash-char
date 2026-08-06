# Architecture Specification
## Prakāśa-chara: In Plain Sight

**Version:** 1.0 (Milestone 1)
**Date:** 2026-08-06
**Status:** Draft — for review
**Related:** [SRS.md](SRS.md), [Component_Specification.md](Component_Specification.md), [DECISIONS.md](../DECISIONS.md)

---

## 1. Overview & Goals

The architecture has one governing tension to resolve: **a data-driven, maintainable build process** (so content/scene edits don't require touching rendering code) versus **a zero-dependency, single-artifact, `file://`-loadable runtime** (CLAUDE.md's hard constraint). The design below keeps those two worlds strictly separated: a conventional, script-driven **build-time** pipeline produces a **frozen, dependency-free runtime**.

## 2. Deployment Model

### 2.1 Runtime environment
The shipped artifact runs by double-clicking `index.html`, which loads over the `file://` protocol — not `http://`. This has concrete consequences that every other architectural decision below must respect:

- **`fetch()` and `XMLHttpRequest` against local files are blocked by browser CORS policy under `file://`** in Chrome and most Chromium-based browsers by default. This means the scene manifest, asset manifest, and any other JSON data **cannot** be loaded via `fetch('data/scenes.json')` at runtime.
- **Consequence (binding decision):** all structured data (scene manifest, key-wall config, room content) must be **inlined as JavaScript objects/literals directly in the shipped script**, not fetched as separate `.json` files at runtime. The JSON Schemas in §5 describe the *shape* of this data; the build step (§7) is responsible for validating authored JSON against these schemas and then emitting it as an inlined `<script>` block or a bundled `.js` file referenced by a normal `<script src="...">` tag (which *is* permitted under `file://`, unlike `fetch`).
- Images/audio referenced via `<img src="assets/...">`, `background-image: url(...)`, and `<audio src="...">` **do** load correctly under `file://` with relative paths — no inlining as base64 is required for those, though small/critical assets (e.g., the watermark) may still be inlined to guarantee they can never 404.
- No `<script type="module">` cross-origin restrictions apply if scripts are same-directory relative includes; ES module `import` of local files under `file://` is unreliable across browsers, so **plain, non-module `<script>` tags with an IIFE/namespace pattern are used**, not ES modules.

### 2.2 Shipped artifact shape
Per CLAUDE.md, the "final output" is `index.html`. In practice this means an `index.html` **plus a co-located `assets/` folder** (images, audio, fonts) that travels with it as a single folder — this satisfies "double-click index.html runs it offline" without requiring every byte to be base64-inlined into one file (which would bloat parse time and make the HTML unreviewable). The **Release ZIP** (Milestone 5) is this folder, zipped.

## 3. Build-Time vs Run-Time Separation

```
BUILD TIME (this machine, has Python, network, API keys)
─────────────────────────────────────────────────────────
  docs/*.md, ppt/*.pptx, docs/Asset_Register_v1.0.xlsx
          │
          ▼
  scripts/  (Python: OpenAI Images, Firecrawl, Pillow/ImageMagick, ffmpeg, Pandoc)
          │  reads: prompts/*.json, schemas/*.schema.json
          │  writes: assets/ (webp/png/ogg), src/data/*.json (authored, validated)
          ▼
  scripts/freeze.py
          │  validates src/data/*.json against schemas/
          │  inlines data into src/js/data.generated.js
          │  copies/optimizes assets/ → release-ready assets/
          ▼
  release/  →  index.html + assets/  (zipped for distribution)

RUN TIME (training-room machine, may be air-gapped, file:// only)
─────────────────────────────────────────────────────────
  index.html
    ├─ <script src="assets/js/data.generated.js">   (inlined scene/key-wall data, no fetch)
    ├─ <script src="assets/js/engine.js">            (scroll engine, hub engine, state)
    ├─ <link  href="assets/css/style.css">
    ├─ <img/audio src="assets/...">                  (relative paths, file:// safe)
    └─ zero network calls, zero build tools present
```

Nothing under `scripts/`, `prompts/`, `schemas/`, or `.env` ships in the release artifact — those are build-time only and stay out of `release/`.

## 4. Proposed Directory Layout

```
prakash-char/
├── src/                      # authored source, pre-freeze
│   ├── index.html            # authored shell (becomes release/index.html)
│   ├── css/
│   ├── js/                   # engine.js, hub.js, audio.js, watermark.js, state.js
│   └── data/                 # authored scene/room/keywall JSON — validated against schemas/, never fetched at runtime
├── prompts/                  # OpenAI Images prompt library (one file per asset or per category)
│   └── style_lock.md         # shared palette/texture/typography preamble, referenced by every prompt
├── schemas/                  # JSON Schema definitions (§5) — build-time validation only
├── scripts/                  # Python build pipeline (generate, source, optimize, freeze, package)
├── assets/                   # source concept art + build outputs staged here before optimization
│   ├── concept_art/          # existing exploratory art (unchanged)
│   ├── images/                # generated, registry-tracked, correctly named per Asset Register
│   └── audio/
├── docs/                     # this spec set + brief + register + audit
├── ppt/                      # source decks (unchanged)
├── release/                  # gitignored build output — the shippable folder/zip
└── requirements.txt
```

This is a **proposed** layout for Milestone 3 (HTML engine build) — no code or folders beyond documentation are created in this milestone, per instruction.

## 5. Data Model / Schemas

These four schemas are the "schema foundation" carried over from the Repository Audit's Milestone 1 recommendation. They are documentation artifacts in this milestone (not yet implemented as `.schema.json` files under `schemas/`) — creating the actual schema files is Milestone 2/3 build work.

### 5.1 Scene Manifest Schema
Covers the linear-walk scenes (0–4, 8–10) and the five narrative rooms (6a–6e).

```json
{
  "$id": "scene.schema.json",
  "type": "object",
  "required": ["id", "type", "title", "assets", "transitions"],
  "properties": {
    "id": { "type": "string", "pattern": "^[a-z0-9-]+$", "description": "e.g. scene-00-cold-open, room-foundations" },
    "type": { "enum": ["linear-scene", "narrative-room", "terminal-room"] },
    "title": { "type": "string" },
    "sourceSlides": {
      "type": "array",
      "items": { "type": "string" },
      "description": "e.g. ['OSINT SE Session.pptx#3-5'] — traceability back to SRS §6.1"
    },
    "assets": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Asset Register IDs, e.g. ['F001','F002']"
    },
    "content": {
      "type": "array",
      "items": { "type": "object", "properties": { "heading": {"type":"string"}, "body": {"type":"string"} } },
      "description": "Narrative/body copy blocks rendered inside the room (narrative-room only)"
    },
    "demoPause": {
      "type": ["object", "null"],
      "properties": {
        "handoffText": { "type": "string" },
        "targetSetup": { "type": "string", "description": "e.g. 'Kali VM → Ubuntu VM decoy'" }
      },
      "description": "Present only when type === terminal-room; see Component_Specification.md §Pause-for-Demo"
    },
    "transitions": {
      "type": "object",
      "properties": {
        "enter": { "type": "string", "description": "transition id, e.g. zoom-in, rotate-turn" },
        "exit": { "type": "string" }
      }
    },
    "audio": { "type": ["string", "null"], "description": "Asset Register audio ID, e.g. AU001" }
  }
}
```

### 5.2 Mission Board State Schema
*(File/schema id kept as `keywall-state.schema.json` for internal continuity with early build notes; the in-fiction/UI name is "Mission Board" — DECISIONS.md #011.)*
Runtime, in-memory state — not persisted to disk (NFR/FR-9 requires only session-lifetime persistence). Covers the 9 Version-1 rooms only; locked/future-expansion placeholders (SRS FR-8a) are static UI, not modeled here — they carry no state and are excluded from `allVisited`.

```json
{
  "$id": "keywall-state.schema.json",
  "type": "object",
  "required": ["keys"],
  "properties": {
    "keys": {
      "type": "array",
      "maxItems": 9,
      "items": {
        "type": "object",
        "required": ["keyId", "roomId", "state"],
        "properties": {
          "keyId": { "type": "string", "description": "e.g. FOUNDATIONS, SIGNALGATE, FIERY_CROSS_REEF, GREY_AREAS, SE_BRIDGE, GOOGLE_DORKING, TOOL_CHAIN, SET, GOPHISH" },
          "roomId": { "type": "string", "description": "references scene.schema.json id" },
          "state": { "enum": ["unlit", "lit"], "description": "Version-1 rooms only; 'locked' is reserved for future-expansion placeholders, which are not modeled in this array at all (SRS FR-8a)" },
          "visitCount": { "type": "integer", "minimum": 0 }
        }
      }
    },
    "allVisited": { "type": "boolean", "description": "derived from the 9 Version-1 keys only; drives FR-14 auto check-out trigger" }
  }
}
```

### 5.3 Asset Manifest Schema
Machine-readable mirror of `docs/Asset_Register_v1.0.xlsx`, generated by the build pipeline (single source of truth stays the spreadsheet; this is a build artifact, not hand-authored).

```json
{
  "$id": "asset-manifest.schema.json",
  "type": "array",
  "items": {
    "type": "object",
    "required": ["assetId", "category", "name", "status", "priority", "source"],
    "properties": {
      "assetId": { "type": "string", "description": "e.g. A001, F002, AU001" },
      "category": { "type": "string" },
      "name": { "type": "string" },
      "description": { "type": "string" },
      "status": { "enum": ["To Generate", "To Source", "Draft", "Ready"] },
      "priority": { "enum": ["High", "Medium", "Low"] },
      "fileName": { "type": ["string", "null"] },
      "source": { "enum": ["OpenAI Images", "HTML/SVG", "SVG/HTML", "SVG", "HTML/CSS", "HTML", "CC0"] },
      "notes": { "type": ["string", "null"] }
    }
  }
}
```

### 5.4 Content Mapping Schema
Formalizes SRS §6.1's traceability table so it's checkable by a build-time script (e.g., "every slide range has a destination or an explicit `outOfScope` marker").

```json
{
  "$id": "content-mapping.schema.json",
  "type": "array",
  "items": {
    "type": "object",
    "required": ["deck", "slideRange", "destination"],
    "properties": {
      "deck": { "type": "string", "description": "e.g. 'OSINT SE Session.pptx'" },
      "slideRange": { "type": "string", "description": "e.g. '3-5'" },
      "segment": { "type": "string" },
      "destination": {
        "oneOf": [
          { "type": "string", "description": "scene.schema.json id" },
          { "const": "out-of-scope" },
          { "const": "unresolved" }
        ]
      }
    }
  }
}
```

## 6. Runtime Architecture

Four cooperating, dependency-free JS modules (namespaced globals, no bundler required since there's no build step at runtime — the "build" already happened before freeze):

| Module | Responsibility |
|---|---|
| `PC.state` | Holds key-wall state (§5.2) and current scene pointer in memory; exposes get/set + a tiny pub-sub for the other modules to react to state changes. No `localStorage`/`sessionStorage` dependency required by the spec (session-lifetime only), though using it is not precluded — flagged as an implementation choice for Milestone 3, not a constraint here. |
| `PC.linearEngine` | Drives Scenes 0–4 and 8–10: listens to scroll position, maps it to scene/sub-stage progress (e.g., Red Team Ops sign scale), triggers enter/exit transitions from the scene manifest. |
| `PC.hubEngine` | Drives Scenes 5–7: renders the Mission Board from `keywall-state` plus the static locked-placeholder list, handles key clicks → room transitions, renders narrative-room content or the terminal-room + Pause-for-Demo component, provides the explicit "back to hub" control (FR-13), and evaluates the FR-14 auto-check-out condition. |
| `PC.audio` | Thin wrapper over `<audio>` elements for ambient loops; exposes mute toggle; never throws if playback is blocked (NFR-6). |

Rendering approach: plain DOM + CSS transitions/animations (transform, opacity) driven by scroll and click handlers — no canvas/WebGL requirement implied by the brief's visual language (largely static art + CSS-driven camera-move illusions), keeping the runtime simple and dependency-free. This should be revisited in Milestone 3 if a specific transition (e.g., the Scene 2 "zoom into the screen") proves impractical in pure CSS.

## 7. Build Pipeline (Milestone 2/3 work — described here for sequencing only)

1. **Author** scene/room content JSON under `src/data/`, validated against §5 schemas (a small Python validator using `jsonschema`, already compatible with `requirements.txt`'s pinned stack once added).
2. **Generate** imagery: `scripts/generate_images.py` reads `prompts/` (per-asset prompt + `prompts/style_lock.md` preamble), calls the OpenAI Images API, writes to `assets/images/` using the Asset Register's `File Name` convention.
3. **Source** audio: manually sourced CC0 files placed at `assets/audio/rain.ogg`, `assets/audio/ops.ogg` per the register.
4. **Optimize**: ImageMagick/Pillow converts to `.webp` at defined dimensions/quality; ffmpeg normalizes audio loop points and encodes to `.ogg`.
5. **Freeze**: `scripts/freeze.py` validates all data against schemas, inlines scene/key-wall JSON into `assets/js/data.generated.js`, copies optimized assets into `release/assets/`, copies `src/index.html` → `release/index.html` with asset paths verified to resolve.
6. **Verify**: automated check that `release/` has zero references to `http(s)://` and that every asset path referenced in HTML/CSS/JS resolves to a file that exists in `release/assets/`.
7. **Package**: zip `release/` → `Prakasha-chara_v{version}.zip` (Milestone 5).

## 8. Asset Optimization Budget

No hardware/size budget is fixed yet (SRS §8, open item 3). Proposed working target, to confirm at Milestone 2: **≤150 MB total release folder** — roughly 30 `.webp` images at ~2–4 MB each pre-optimization budget (register specifies `.webp`, which typically halves PNG size at comparable quality) plus 2 short `.ogg` ambient loops (a looped ambient bed rarely needs to exceed a few MB). This is a proposal for sign-off, not a locked constraint.

## 9. Browser/Runtime Compatibility
Target: last 2 major versions of Chrome, Firefox, Edge, Safari (desktop), per SRS NFR-8. No transpilation/polyfill build step is planned, since a network-connected build machine authors the JS directly against this modern baseline — CLAUDE.md's "vanilla JS only" already precludes framework polyfill layers.

## 10. Watermark Implementation Approach
Per Decision 006 and SRS FR-21: a fixed-position, low-opacity `<div>` (not an `<img>`, to avoid an asset dependency and guarantee it renders even if all image assets fail) containing the text "Lt Col Dheeraj Bharti ©2026", styled per [UI_Style_Guide.md](UI_Style_Guide.md) §8, placed as a direct child of `<body>` with a high `z-index` so no scene/room content can visually cover it, and with no in-experience control exposed to hide or dismiss it (satisfies "non-removable").

## 11. Open Items Carried Forward
1. Confirm whether `localStorage` use (e.g., to remember Mission Board progress across a reload mid-session) is desirable — not required by SRS, but low-cost if wanted; needs a decision before Milestone 3.
2. Confirm the Scene 2 "zoom into the screen" and Scene 4 "camera rotation" transitions are achievable with CSS 3D transforms at acceptable performance on training-room hardware (NFR-4) — flagged as a technical risk to validate early in Milestone 3, not blocking this milestone.
3. Size budget (§8) needs sign-off once real asset weights are known (Milestone 2).
