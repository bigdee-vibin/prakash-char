# UI Style Guide
## Prakāśa-chara: In Plain Sight

**Version:** 1.0 (Milestone 1)
**Date:** 2026-08-06
**Status:** Draft — for review
**Related:** [Creative_Bible.md](Creative_Bible.md), [Component_Specification.md](Component_Specification.md), [Architecture.md](Architecture.md)

This guide translates the brief's "Design Language" section into concrete, buildable values. All values here are **proposed defaults for Milestone 2/3** — nothing is generated or coded in this milestone.

---

## 1. Color Palette

| Token | Hex | Usage |
|---|---|---|
| `--pc-bg-base` | `#0A0B0E` | Near-black base — default background for every scene/room |
| `--pc-bg-raised` | `#12141A` | Panels, room-interior surfaces, card backgrounds |
| `--pc-grid-cyan` | `#26E5FF` | Grid lines, structural UI (Lane floor grid, Mission Log HUD borders) |
| `--pc-grid-cyan-dim` | `#0F5C66` | Grid lines at low-emphasis / unlit states |
| `--pc-neon-magenta` | `#FF2FB0` | Signage — "OSINT HOTEL," "RED TEAM OPS," key-wall lit state |
| `--pc-amber` | `#FFB020` | Interactive/clickable elements — matches the source deck's orange tag colour (continuity thread per brief) |
| `--pc-amber-dim` | `#7A5511` | Disabled/locked interactive elements (e.g. an unvisited key before hover) |
| `--pc-text-primary` | `#EAF6F8` | Body copy on dark backgrounds |
| `--pc-text-secondary` | `#9FB4B8` | Captions, metadata, source-slide attributions |
| `--pc-alert-critical` | `#FF4747` | Reserved for the Grey Areas / ethics room's hard-line statements only ("Never test systems... you don't have written authorisation") — used sparingly, not decoratively |
| `--pc-locked-grey` | `#2A2D33` | Mission Board locked/future-expansion placeholders (C-4b) — deliberately duller than `--pc-amber-dim` so an unvisited-but-available key is never confused with a locked one |

**Contrast rule (NFR-7):** `--pc-text-primary` on `--pc-bg-base`/`--pc-bg-raised` must be verified ≥4.5:1 (WCAG AA) at build time; `--pc-text-secondary` targets ≥3:1 for large/secondary text only, never for body copy carrying case-study facts.

## 2. Typography

- **Monospace (terminal/code moments — Component Spec "Terminal Room" motif, code fragments in the Foundations/dorking references):** a bundled OFL-licensed monospace, e.g. **JetBrains Mono** or **Space Mono**, shipped as local `.woff2` files under `assets/fonts/` (no CDN, per DECISIONS.md #003/CLAUDE.md — Google Fonts links are not permitted at runtime). Final font choice to be confirmed at Milestone 2 against license terms and file size.
- **Geometric sans (room signage, UI chrome, body copy):** a bundled OFL-licensed geometric sans, e.g. **Space Grotesk** or **Rajdhani** (Rajdhani's slightly technical/military character may suit the brief better — flag for review). Same local-bundling requirement.
- **System-stack fallback:** `font-family: ui-monospace, "SF Mono", Consolas, monospace;` / `font-family: -apple-system, "Segoe UI", sans-serif;` declared as the fallback in case a bundled font fails to load, so text never becomes unreadable (ties to NFR-6 graceful degradation).
- **Decorative katakana-flavoured glyphs** (Lane-scene background signage, brief §Design Language): atmosphere only, non-functional, must never carry information the trainee needs to progress (accessibility — no content gated behind decorative-only glyphs).

## 3. Texture

- **Scan-line / VHS grain overlay:** a fixed, full-viewport CSS overlay (repeating-linear-gradient scanlines + a subtle noise texture, either a small tiled PNG or a CSS-only noise technique) at low opacity (~4–8%), applied globally to tie the "surveillance footage" motif to the OSINT subject matter (brief's stated intent). Must not reduce text contrast below the NFR-7 thresholds in §1 — verify contrast *with* the overlay applied, not just against the base palette.
- Terminal rooms (7a–7d) may intensify this texture slightly to reinforce the "you're now looking at a real console" feel, in contrast to the narrative rooms.

## 4. Motion Principles

- **Scenes 0–4 and 8–10 (linear walk):** strictly scroll-linked, never autoplay — motion progress is a direct function of scroll position (SRS FR-2–FR-6). No easing that continues animating after scroll input stops.
- **Scenes 5–7 (hub/rooms):** click-driven, not scroll-driven. The shift in interaction model must be *felt*: on entering the Mission Board, the cursor should change (e.g., to a hand/pointer with a subtle glow) and a brief, one-time UI cue (e.g., a soft pulse across the unlit keys) should signal "you are now choosing," per the brief's explicit instruction. Locked/future-expansion placeholders (Creative Bible §7.1) do not participate in this cue — they read as inert from the start.
- **Transitions between modes** (Scene 4's "turn" into the hotel, Scene 9's return to the lane) get a distinct, slightly longer transition (600–900ms proposed) than in-room transitions (200–350ms proposed) to mark the mode shift.
- **`prefers-reduced-motion` (NFR-7):** when set, disable the zoom/rotate camera-move transitions (Scenes 2, 4) in favor of a simple cross-fade, and reduce the Red Team Ops sign's growth animation to a single discrete state change rather than continuous scaling.

## 5. Iconography
No bespoke icon set is specified by the brief. Where UI chrome needs icons (mute toggle, back-to-hub control, key-wall lock/unlit/lit indicator), use simple geometric line-art consistent with the grid/neon palette (stroke in `--pc-grid-cyan` or `--pc-amber` depending on interactive state) rather than a filled/skeuomorphic icon style. Defer final icon set to Milestone 3 (Component Specification defines *behavior*; icon artwork itself is an asset-generation task, Milestone 2).

## 6. Spacing & Layout
- No responsive/mobile layout is required by the SRS (assumption A-2 — desktop/projector delivery); design for a fixed-ish widescreen viewport (1280×800 minimum) rather than a fluid mobile-first grid.
- Room content (narrative rooms 6a–6e) should read comfortably at a max content width (~720–800px proposed) centered within the room's environmental art, so body text doesn't stretch edge-to-edge on wide displays.

## 7. Accessibility Baseline (ties to SRS NFR-7)
- Contrast per §1.
- `prefers-reduced-motion` per §4.
- Every interactive element (keys, back-to-hub, mute) must be reachable and operable via keyboard (Tab + Enter/Space), not click-only — the brief doesn't specify keyboard nav explicitly, but SRS NFR-7's "baseline accessibility" intent requires it; flagged for confirmation at Milestone 3 implementation.
- Audio (§ FR-22) is never the sole carrier of required information — ambient loops only, never narration-as-information.

## 8. Watermark Visual Spec (Decision 006, SRS FR-21, Architecture §10)
- **Text:** `Lt Col Dheeraj Bharti ©2026`
- **Placement:** fixed position, bottom-right corner, ~16px inset from viewport edges.
- **Style:** `--pc-text-secondary` at ~40% opacity, monospace font (ties it visually to the "surveillance footage" texture rather than reading as a decorative credit), small size (~11–12px), `letter-spacing` slightly widened for a stamped/overlay feel.
- **Behavior:** always on top (`z-index` above all scene/room layers), present identically across every scene and room, never included in any "hide UI" or fullscreen-art moment — non-negotiable per Decision 006.

## 9. Open Items Carried Forward
1. Final font selection (JetBrains Mono vs. Space Mono; Space Grotesk vs. Rajdhani) — confirm license + file size at Milestone 2.
2. Confirm exact scanline/grain implementation (tiled PNG vs. pure-CSS) once real asset weight budgets are known (Architecture §8).
3. Keyboard-navigation requirement for the Mission Board — confirm as in-scope for Milestone 3 or defer.
