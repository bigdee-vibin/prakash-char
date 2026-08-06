# Component Specification
## Prakāśa-chara: In Plain Sight

**Version:** 1.0 (Milestone 1)
**Date:** 2026-08-06
**Status:** Draft — for review
**Related:** [Architecture.md](Architecture.md), [UI_Style_Guide.md](UI_Style_Guide.md), [Scene_Bible.md](Scene_Bible.md)

Each component below is a specification for Milestone 3 implementation — no code is produced in this milestone. "Data" fields reference the schemas in [Architecture.md](Architecture.md) §5.

---

## C-1 · Scene Container
**Purpose:** the outermost wrapper for any linear scene or room; owns background art, texture overlay, and the watermark's stacking context.
**Data:** one `scene.schema.json` entry.
**Behavior:** renders the scene's background asset (Asset Register ID → resolved local path per Architecture §7), applies the scanline/grain overlay (UI Style Guide §3), and mounts either the Linear Scroll layer (C-2) or the Room layer (C-4/C-5) depending on `type`.
**States:** `entering`, `active`, `exiting` (drives transition classes referenced by `transitions.enter`/`transitions.exit`).
**Accessibility:** background art is decorative (`aria-hidden="true"`); any text content inside is in normal document flow for screen readers.

## C-2 · Linear Scroll Engine
**Purpose:** drives Scenes 0–4 and 8–10 (SRS §3.1).
**Data:** ordered list of `linear-scene` entries from the scene manifest.
**Behavior:**
- Maps scroll position within a scene's allotted scroll range to a 0–1 progress value.
- Applies progress to: Monitor Wall pan (Scene 1), zoom-in transform (Scene 2), forward-motion + HACK METH sign scale (Scenes 3, 9), turn/rotate transform (Scene 4).
- Emits a `scene:complete` event to `PC.state` when a scene's scroll range is exhausted, advancing to the next scene.
**States:** per-scene `progress: 0..1`.
**Reduced motion:** when `prefers-reduced-motion` is set, progress still advances on scroll but transform intensity is capped (UI Style Guide §4) — discrete step rather than continuous scale/rotate.
**Depends on:** C-1.

## C-3 · Camera Transition (Zoom / Turn)
**Purpose:** the two "mode-shift" transitions — Scene 2 (zoom into the central monitor) and Scene 4 (turn into the OSINT Hotel).
**Data:** `transitions.enter`/`exit` ids from the relevant scene entries (`zoom-in`, `rotate-turn`).
**Behavior:** CSS 3D transform sequence (scale/perspective for zoom, rotateY for turn) over the duration band specified in UI Style Guide §4 (600–900ms). Marked as a technical risk to validate early (Architecture §11 item 2) — if CSS 3D transforms underperform on target hardware, this component's implementation (not its interface) would change to a 2D approximation.
**Depends on:** C-1, C-2.

## C-4 · Mission Board Hub
**Purpose:** Scene 5 — the non-linear navigation hub (SRS §3.2). Named "Mission Board" in-fiction (DECISIONS.md #011, formerly "Key Wall" in early concept art) — heading copy reads "Available Intelligence Missions," not "Select a Room."
**Data:** `keywall-state.schema.json` (runtime) + the set of `narrative-room`/`terminal-room` scene entries it points to, plus a static list of locked/future-expansion placeholder labels (no scene entry backs them — see C-4b).
**Behavior:**
- Renders one Key control (C-4a) per entry in `keywall-state.keys` for the 9 Version-1 rooms.
- Renders one Locked Placeholder (C-4b) per reserved-expansion label, visually interleaved with the active keys per the concept art's layout, but non-interactive.
- On entering this hub for the first time in a session, plays the one-time "you are now choosing" UI cue (UI Style Guide §4) and applies the hub cursor style.
- On key click (C-4a only — C-4b has no click handler): sets that key's `state` to `lit`, increments `visitCount`, transitions into the corresponding room (C-5 or C-6), and re-evaluates `allVisited` (feeds C-8 Check-out; locked placeholders are excluded from this evaluation, SRS FR-14).
**States:** `idle`, `key-focused` (hover/keyboard-focus), `transitioning-to-room`.
**Accessibility:** keys are keyboard-focusable buttons (UI Style Guide §7), not bare `<div onclick>`; each announces its topic name and current state (locked/unlit/lit) to assistive tech via `aria-label`. Locked placeholders (C-4b) are `aria-disabled="true"` and excluded from the normal tab order or clearly announced as unavailable — not a silent dead click target.
**Depends on:** C-1, C-4a, C-4b.

### C-4a · Key Control
**Purpose:** a single clickable key element within C-4, representing one of the 9 Version-1 rooms.
**Data:** one `keywall-state.keys[]` entry + its linked `scene.schema.json` `title`.
**Visual states:** `unlit` (`--pc-amber-dim` per UI Style Guide §1), `hover/focus` (brightens toward `--pc-amber`), `lit` (`--pc-neon-magenta` steady glow, per brief's "lit up" description).
**Depends on:** UI Style Guide §1, §4.

### C-4b · Locked Placeholder
**Purpose:** a non-interactive "Coming Soon" / "Available in a future mission" key, representing a reserved-expansion topic from the original concept art (e.g. Threat Intelligence, Dark Web & Leaks, GEOINT Suite, Imagery & Metadata, OPSEC & Privacy, Report & Attribution, Archive Vault) that is explicitly **not** part of Version 1 (Creative Bible §7.1, DECISIONS.md #011).
**Data:** a static label string only — no `scene.schema.json` entry, no assets, no content backs it.
**Visual state:** permanently inert/locked (e.g. a dimmed icon and a lock glyph), visually distinct from C-4a's `unlit` state so it doesn't read as "not yet visited but visitable."
**Behavior:** no click handler; no hover-to-room transition. Hovering may show a static tooltip/label (e.g. "Available in a future mission") but never opens a room.
**Depends on:** C-1.

## C-5 · Narrative Room
**Purpose:** renders the five content rooms — Foundations, SignalGate, Fiery Cross Reef, Grey Areas & Legal, SE Bridge (SRS §3.2, FR-11).
**Data:** one `narrative-room` scene entry, specifically its `content` array (heading/body blocks) and `sourceSlides` (for traceability, not rendered to the trainee).
**Behavior:** renders the room's background art (via C-1), then the content blocks in reading order within the max-content-width column (UI Style Guide §6). Content text must satisfy the Creative Bible §6 fidelity rule — this component does not itself enforce that (it's an authoring-time discipline), it only renders what's authored.
**Exit control:** an explicit, always-visible "Back to Reception" control (C-9) — never relies on scroll-back (SRS FR-13).
**Special case — SignalGate/Fiery Cross Reef/Grey Areas:** these three rooms additionally render a **Case Study Card** (C-7) or, for Grey Areas, the ethics hard-line statement styled per UI Style Guide §1 `--pc-alert-critical` (used sparingly, Creative Bible-consistent).
**Depends on:** C-1, C-7 (where applicable), C-9.

## C-6 · Terminal Room
**Purpose:** renders the four demo-pause rooms — Google Dorking, OSINT Tool Chain, SET, GoPhish (SRS §3.2, FR-12).
**Data:** one `terminal-room` scene entry, specifically its `demoPause` object (`handoffText`, `targetSetup`).
**Behavior:** renders the shared "desk + idle terminal" background art (C-1), then — after a short beat, not instantly, so it doesn't feel like an error state — transitions the terminal's on-screen content to the Pause-for-Demo Interstitial (C-6a). Does **not** render any simulated tool output (Creative Bible §9, SRS FR-18) — this is a hard constraint on this component's implementation, not just a content-authoring choice.
**Exit control:** same C-9 "Back to Reception" control, available once the interstitial is showing (so the instructor/trainee isn't stuck once the live demo concludes and the class returns to the web experience).
**Depends on:** C-1, C-6a, C-9.

### C-6a · Pause-for-Demo Interstitial
**Purpose:** the single reusable "fourth wall break" component (SRS FR-16–18) — this is the brief's most explicitly specified reusable UI moment, and must render **identically in structure** across all 4 terminal rooms (only `handoffText`/`targetSetup` vary).
**Data:** `demoPause.handoffText` (e.g. `>> LIVE DEMO — see instructor workstation`), `demoPause.targetSetup` (e.g. `Kali VM → Ubuntu VM decoy`).
**Visual treatment:** deliberately distinct from every narrative room — calm, static, terminal-styled (monospace, UI Style Guide §2), no ambient camera motion, slightly intensified scanline texture (UI Style Guide §3) — reads as "the screen has stopped performing and is now just informing you."
**Behavior:** static once shown; no auto-dismiss, no timer — the instructor controls pacing in the physical classroom, the component must never rush or auto-advance past this point.
**Depends on:** C-1, UI Style Guide §2/§3.

## C-7 · Case Study Card
**Purpose:** presents a single case study's factual summary (SignalGate, Fiery Cross Reef, Gulf Censorship) within its narrative room, per the Creative Bible §4 fidelity/sensitivity rules.
**Data:** the room's `content` block(s) plus an optional attributed media asset (e.g., a sourced screenshot/frame-grab per the brief's Asset Needs list, or a labelled placeholder — Creative Bible §4.4).
**Behavior:** renders headline/summary/attribution in a fixed card layout; if the backing media asset is a placeholder, the card visibly labels it as such (never silently substitutes without disclosure — matches the brief's own placeholder convention).
**Depends on:** C-5.

## C-8 · Check-out Controller
**Purpose:** Scene 8 logic — auto-trigger or manual "leave" prompt once all keys are visited (SRS FR-14–15).
**Data:** `keywall-state.allVisited`.
**Behavior:** subscribes to `PC.state` key-wall updates; when `allVisited` becomes true, transitions all C-4a keys to their steady-lit "checked out" visual and advances to Scene 9. If the trainee triggers a manual exit before `allVisited`, presents a lightweight confirm ("leave without visiting every room?") rather than blocking — the brief allows leaving early.
**Depends on:** C-4, C-4a.

## C-9 · Back-to-Reception Control
**Purpose:** shared exit control used by C-5 and C-6 (SRS FR-13).
**Behavior:** always visible (not scroll-dependent), returns to C-4 Mission Board Hub, does not reset any room's visited state.
**Accessibility:** keyboard-reachable, labelled clearly (not icon-only without a text label/aria-label).

## C-10 · Watermark Overlay
**Purpose:** the persistent, non-removable credit (Decision 006, SRS FR-21, Architecture §10, UI Style Guide §8).
**Data:** none — static text, hardcoded (this is the one piece of UI text explicitly *not* data-driven, since it must never be edited via content authoring).
**Behavior:** mounted once at the document root, outside the scene/room component tree, so no scene/room transition can ever unmount or cover it.

## C-11 · Audio Controller
**Purpose:** ambient loop playback (SRS FR-22, Architecture §6 `PC.audio`).
**Data:** `audio` field on scene entries (Asset Register audio IDs AU001/AU002).
**Behavior:** plays the mapped loop when a scene/room with an `audio` reference becomes active; crossfades rather than hard-cuts between different loops (e.g., Lane's rain vs. Cold Open's ops tone) if two adjacent scenes specify different tracks; exposes a single global mute toggle (persists only for the session, no runtime storage requirement per SRS).
**Failure mode:** if autoplay is blocked by the browser, fails silently — no error, no blocking UI (NFR-6). A muted-speaker icon reflects actual playback state so the trainee isn't confused about whether audio "should" be playing.

## C-12 · Easter Egg Monitor (Scene 1 detail)
**Purpose:** the four peripheral monitors in the Monitor Wall (SRS FR-23).
**Data:** four static looping assets (Python/Networking/PowerShell/Bash — Asset Register does not yet list these as distinct rows; flagged as a Milestone 2 asset-register gap, see Scene Bible Scene 1 notes).
**Behavior:** looping background-video-style treatment (likely an animated sprite/GIF-equivalent or CSS-animated static art rather than real video, to keep the offline bundle light — implementation choice for Milestone 3); the Python monitor's buried signature line renders as part of that asset's artwork, not as separate DOM text (it's meant to be found by close visual inspection, per the brief).
**Depends on:** C-1, C-2.

---

## Component Dependency Map (summary)

```
PC.state ─┬─ C-2 Linear Scroll Engine ─── C-3 Camera Transition ─── C-12 Easter Egg Monitor
          │
          └─ C-4 Mission Board Hub ─┬─ C-4a Key Control
                                     ├─ C-4b Locked Placeholder
                                     ├─ C-5 Narrative Room ─── C-7 Case Study Card
                                     ├─ C-6 Terminal Room ──── C-6a Pause-for-Demo Interstitial
                                     ├─ C-8 Check-out Controller
                                     └─ C-9 Back-to-Reception Control

C-1 Scene Container   — wraps every scene/room above
C-10 Watermark Overlay — mounted independently, outside the tree above
C-11 Audio Controller  — subscribes to PC.state scene changes, independent of the visual tree
```
