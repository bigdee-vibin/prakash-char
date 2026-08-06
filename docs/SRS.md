# Software Requirements Specification (SRS)
## Prakāśa-chara: In Plain Sight

**Version:** 1.0 (Milestone 1)
**Date:** 2026-08-06
**Status:** Draft — for review
**Governing documents:** `/Users/dheerajbharti/CLAUDE.md`, [CLAUDE.md](../CLAUDE.md), [PROJECT.md](../PROJECT.md), [DECISIONS.md](../DECISIONS.md), [docs/OSINT_Hotel_Scrollytelling_Brief.md](OSINT_Hotel_Scrollytelling_Brief.md), [docs/Repository_Audit.md](Repository_Audit.md)

---

## 1. Introduction

### 1.1 Purpose
This SRS defines the functional and non-functional requirements for **Prakāśa-chara: In Plain Sight**, an offline, scroll- and click-driven interactive training experience that re-skins the "Foundations," "Grey Areas & Legal," and "Social Engineering — The Bridge" segments (plus three case studies) of the `OSINT & Social Engineering` session (IW/HAK/15.3) into an explorable scene.

### 1.2 Scope
In scope: a single self-contained offline web experience (`index.html`) covering the non-demo, non-air-gapped-practice portions of the session — the material that can be told as a story rather than run live.

Out of scope for this build: anything that must remain a live, instructor-run demonstration on real or virtualized machines (Google Dorking, the OSINT tool chain, SET, GoPhish, the air-gapped exercise). These are represented in the experience only as **handoff cues**, never simulated.

### 1.3 Definitions
| Term | Meaning |
|---|---|
| Trainee | The learner interacting with the experience, individually or as part of an instructor-led class |
| Instructor | The session lead who runs the live-demo segments and drives classroom pacing |
| Scene | One discrete narrative beat in the linear "walk" (Scenes 0–4, 8–10 per the Scene Bible) |
| Room | One node reachable from the Mission Board hub (Scenes 5–7) |
| Demo-pause | A room that ends in a fourth-wall-breaking interstitial handing off to a live, non-web demonstration |
| Freeze | The build-time step of converting all generated/sourced content into static assets bundled with `index.html`, per CLAUDE.md |

### 1.4 References
- Primary source content: `ppt/OSINT SE Session.pptx` (27 slides, IW/HAK/15.3) — see §6 for the full slide-to-scene traceability table
- Secondary source content: `ppt/04 OSINT 1.pptx` (23 slides, "Class 4 of 6") — **not currently in scope; see §6.3**
- Asset inventory: `docs/Asset_Register_v1.0.xlsx`

---

## 2. Overall Description

### 2.1 Product Perspective
A standalone artifact, not a service. It has no backend, no network calls at runtime, and no build-time dependency once frozen. It is designed to be handed to an instructor as a folder (or a single HTML file) that runs by double-click, on a machine that may never touch a network — including during the delivery itself.

### 2.2 Product Functions (summary)
1. Present a fixed narrative "walk" (cold open → monitor wall → pull into the screen → neon lane → turn into the OSINT Hotel) driven by scroll position.
2. Present a non-linear hub (the Mission Board — formerly "Key Wall" in early concept art, renamed per DECISIONS.md #011) where the trainee/instructor selects among nine mission entries in any order, with additional reserved-expansion entries shown locked/inactive.
3. Represent five of those rooms as narrative content (Foundations, SignalGate, Fiery Cross Reef, Grey Areas & Legal, SE Bridge).
4. Represent four *other* topics (Google Dorking, OSINT Tool Chain, SET, GoPhish) as **terminal rooms** that break the fourth wall and hand off to the instructor, rather than simulating the tools.
5. Track which keys have been visited and reflect that state visually (grey → lit) and use it to gate the "Check-out" ending beat.
6. Return to the neon lane and close on a deliberate cliffhanger pointing at IW/HAK/15.4.
7. Persist a visible, non-removable watermark across the experience (Decision 006).
8. Run entirely offline with zero runtime network dependency.

### 2.3 User Characteristics
- **Trainee:** military/institutional cyber-course participant, IW/HAK/15.3, assumed no prior exposure to this specific content; may explore individually or watch as part of a class.
- **Instructor:** delivers the session, uses the four demo-pause rooms as literal cues to switch to a separate laptop/VM; needs the handoff moment to be unambiguous and low-friction, not needing to explain "ignore this, we're doing something else."

### 2.4 Constraints (carried from governing documents)
- **C-1** Final output is `index.html`; vanilla HTML/CSS/JS only — no React/Vue/Node at runtime (CLAUDE.md).
- **C-2** No runtime internet access, no external dependencies — all fonts, images, audio, and scripts must be locally bundled (CLAUDE.md, DECISIONS.md #001–#003).
- **C-3** OpenAI Images API and Firecrawl are build-time tools only, never called at runtime (DECISIONS.md #004–#005).
- **C-4** Live demonstrations remain instructor-led; the product must never simulate Segments 2, 3, 6, 7, 8 in-browser (DECISIONS.md #007, brief §"Explicit Scope Boundary").
- **C-5** A persistent watermark reading "Lt Col Dheeraj Bharti ©2026" must be visible throughout (DECISIONS.md #006).
- **C-6** Definition of Done (PROJECT.md): double-clicking `index.html` runs the complete experience offline, with no missing-asset errors and no network requests firing.

### 2.5 Assumptions
- A-1: Delivery machines have a modern evergreen browser (Chromium/Firefox/Safari, last 2 major versions) installed; no requirement to support legacy browsers such as IE11.
- A-2: Delivery machines have a display capable of at least 1280×800; touch/mobile support is not a stated requirement of the brief (desktop/projector delivery assumed) but should degrade gracefully rather than break.
- A-3: Screen/projector audio output may or may not be available; ambient audio (rain, ops-room tone) must be non-essential to comprehension (see FR-9).
- A-4: The instructor operates the mouse/keyboard/scroll during classroom delivery; the same build also supports solo trainee exploration outside class.

---

## 3. Functional Requirements

### 3.1 Linear Walk (Scenes 0–4, 8–10, plus the post-Mission-Board closing beats)
- **FR-1** The experience SHALL open on a static "Cold Open" beat (Scene 0) that holds before any scroll input, establishing mood, followed by an "Operations Centre" beat (Scene 0b) establishing the SOC environment before the Monitor Wall — per the frozen Scene Bible order (2026-08-06 decision) and Asset Register row B001.
- **FR-2** Scrolling SHALL pan across the Monitor Wall (Scene 1) at a rate proportional to scroll delta, not autoplay.
- **FR-3** Continued scroll SHALL trigger a zoom transition (Scene 2 — "The Pull") into the central monitor, dimming/fading the surrounding room.
- **FR-4** Scroll SHALL then drive forward motion down "The Lane" (Scene 3), with the "HACK METH" signage growing larger by a small, deliberate increment at each scroll stage (DECISIONS.md #012 — supersedes the brief's "RED TEAM OPS" wording).
- **FR-5** A scroll or click prompt at the OSINT Hotel building SHALL trigger a camera-rotation transition (Scene 4) into the hub (Scene 5 — Reception/Mission Board).
- **FR-6** After Check-out (§3.3), continued interaction SHALL return the trainee to the Lane (Scene 9) with the HACK METH sign now visually closer/brighter than in Scene 3.
- **FR-7** The experience SHALL end on a fixed Cliffhanger Close (Scene 10) with a text overlay referencing "IW/HAK/15.4 — Gaining Access" and SHALL NOT resolve further — this ending is deliberately non-terminal.

### 3.2 Mission Board Hub (Scene 5) and Rooms (Scenes 6a–6e, 7a–7d)
*(Named the "Mission Board" in-fiction, not "Key Wall" — Decision 011. UI copy reads "Available Intelligence Missions," not "Select a Room.")*
- **FR-8** The Mission Board SHALL render one key per Version-1 topic (§6.1's nine rooms), all initially in a greyed-out/unlit state.
- **FR-8a** The Mission Board MAY additionally render locked/"Coming Soon" placeholder entries for future-expansion topics not in Version 1 scope (Decision 011). These placeholders SHALL have no click handler, no linked room, no assets, and no content — visual-only.
- **FR-9** Clicking a Version-1 key SHALL: (a) light that key, (b) open/transition into its corresponding room, (c) persist the lit state for the remainder of the session (in-memory; no requirement to persist across page reloads).
- **FR-10** Room selection order SHALL be unconstrained — any key may be opened first, and rooms may be revisited.
- **FR-11** The five narrative rooms (Foundations, SignalGate, Fiery Cross Reef, Grey Areas & Legal, SE Bridge) SHALL each present their mapped content (§6.1) as in-browser narrative/scrollable content within the room. SignalGate and Fiery Cross Reef SHALL remain two separate rooms, never merged (Decision 010).
- **FR-12** The four terminal rooms (Google Dorking, OSINT Tool Chain, SET, GoPhish) SHALL each open on the shared "desk + idle terminal" visual motif, then SHALL transition to the Pause-for-Demo interstitial (§3.4) rather than presenting simulated tool output.
- **FR-13** Each room SHALL provide a clear way back to the Mission Board hub (explicit exit control, not scroll-dependent).

### 3.3 Decision, Mission Brief, Debrief & Check-out
- **FR-14** Once all Version-1 keys (both narrative and terminal — locked future-expansion placeholders per FR-8a are excluded from this condition) have been visited at least once, the experience SHALL auto-trigger the Check-out beat (all keys shown lit, steady glow) OR present a manual "leave" prompt if the trainee chooses to exit before visiting every key.
- **FR-14a** After the terminal rooms are all visited, the experience SHALL present the "Decision" scene (source slide 26 — Decision Dilemma), followed by a "Mission Brief" scene, followed by the "Debrief" scene (source slide 27), in that fixed order, per the frozen Scene Bible.
- **FR-15** Check-out SHALL transition into Scene 9 (Back on the Lane).

### 3.4 Pause-for-Demo Component
- **FR-16** Each of the 4 terminal rooms SHALL display an identical, reusable interstitial component reading a live-demo handoff message (e.g., `>> LIVE DEMO — see instructor workstation`), styled distinctly from every other room's fully-immersive treatment (brief's explicit "fourth wall break" requirement).
- **FR-17** The interstitial SHALL name which physical setup the instructor is switching to, using the mapping in §6.1 (e.g., "Kali VM → Ubuntu VM decoy," "instructor laptop, real internet") so the handoff is unambiguous to the class.
- **FR-18** The interstitial SHALL NOT simulate, mock, or approximate real tool output (no fake terminal scrollback of theHarvester/Sherlock/SpiderFoot/SET/GoPhish results).

### 3.5 Case Studies
- **FR-19** The SignalGate and Fiery Cross Reef case studies SHALL each be presented as factual summaries consistent with the source deck (slides 6–7 of `OSINT SE Session.pptx`), not dramatized beyond the room's atmospheric framing (see Creative Bible §4 for sensitivity handling).
- **FR-20** The Gulf Censorship case study (source slide 16) SHALL be presented within the Grey Areas & Legal room per the brief's mapping.

### 3.6 Persistent Elements
- **FR-21** A watermark reading "Lt Col Dheeraj Bharti ©2026" SHALL be visible in every scene and room, non-obscured by other UI, and SHALL NOT be removable via any in-experience control.
- **FR-22** Ambient audio (rain loop in exterior/lane scenes, ops-room tone in the Cold Open / Monitor Wall) SHALL play if the browser allows autoplay-with-user-gesture, and SHALL have an accessible mute control; absence of audio (blocked autoplay, muted system) SHALL NOT block comprehension or progression of any scene (ties to A-3 and NFR-6).

### 3.7 Easter Egg Wall (Scene 1 detail)
- **FR-23** The four peripheral monitors in Scene 1 SHALL loop ambient, non-narrative footage/imagery referencing prior course topics (Python, Networking/PowerShell, Bash — per brief), including the specified buried signature easter egg on the Python monitor, legible only on close inspection.

---

## 4. Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-1 (Offline) | Zero runtime network requests. Verifiable by loading `index.html` with networking disabled and confirming full functionality. |
| NFR-2 (Portability) | Runs from the local filesystem via `file://` with no local server required. (This has architectural consequences — see [Architecture.md](Architecture.md) §2.) |
| NFR-3 (Self-contained) | All fonts, images, audio, and scripts ship inside the release artifact; no CDN references of any kind. |
| NFR-4 (Performance) | Initial load-to-interactive under 5 seconds on the confirmed training-room baseline (DECISIONS.md #016: dual-core ~2.0GHz+, 8GB RAM, integrated graphics, 1280x800 min., evergreen browser). Scroll/transition animation SHALL target 60fps on that same baseline. |
| NFR-5 (Size budget) | Final release artifact SHALL stay ≤150 MB total (DECISIONS.md #017), covering ~33 registered visual assets (.webp) plus 2 ambient audio loops (.ogg); see [Architecture.md](Architecture.md) §8. |
| NFR-6 (Resilience) | No single missing/blocked asset (e.g., blocked autoplay) SHALL produce a JS error that halts the experience; failures degrade gracefully. |
| NFR-7 (Accessibility, baseline) | Text content SHALL meet WCAG AA contrast against its background per the palette in [UI_Style_Guide.md](UI_Style_Guide.md); `prefers-reduced-motion` SHALL be respected by disabling non-essential scroll-linked animation intensity. |
| NFR-8 (Browser compatibility) | Functions correctly on the last 2 major versions of Chrome, Firefox, Edge, and Safari (desktop). No IE11 support. |
| NFR-9 (Maintainability) | Scene/room content SHALL be data-driven (see Architecture §5 schemas) so that content edits do not require touching rendering logic. |
| NFR-10 (Auditability) | Every visual asset used SHALL trace back to an Asset Register row (existing or newly added) for provenance. |

---

## 5. External Interface Requirements
None. The product has no APIs, no persistence beyond in-memory session state, and no integrations at runtime. The only "external interface" is the human handoff at the 4 demo-pause points, which is a classroom/process interface, not a software one — captured functionally in FR-16–18.

---

## 6. Content Scope & Traceability

### 6.1 In-scope mapping — `OSINT SE Session.pptx` (27 slides)

| Slides | Segment | Scene Bible destination | Treatment |
|---|---|---|---|
| 1–2 | Title / Session Roadmap | Not a scene; informs Cold Open framing and instructor context only | Reference only |
| 3–5 | Segment 1 — Foundations | Room 6a (Foundations Room) | Narrative |
| 6 | Case Study — SignalGate | Room 6b (SignalGate Suite) | Narrative |
| 7 | Case Study — Fiery Cross Reef | Room 6c (Fiery Cross Reef Suite) | Narrative |
| 8–10 | Segment 2 — Google Dorking | Room 7a (Terminal — Dorking) | Demo-pause only |
| 11–13 | Segment 3 — OSINT Tool Chain (incl. "Where AI Fits In OSINT Now") | Room 7b (Terminal — Tool Chain) | Demo-pause room (slides 11–12); slide 13 ("Where AI Fits In OSINT Now") renders as a narrative lead-in within the same room, before the Pause-for-Demo interstitial (DECISIONS.md #014) |
| 14–16 | Segment 4 — Grey Areas & Legal (incl. Gulf Censorship case study) | Room 6d (Grey Areas Room) | Narrative |
| 17–19 | Segment 5 — SE Bridge | Room 6e (The Bridge) | Narrative |
| 20–21 | Segment 6 — SET Walkthrough | Room 7c (Terminal — SET) | Demo-pause only |
| 22–23 | Segment 7 — GoPhish Walkthrough | Room 7d (Terminal — GoPhish) | Demo-pause only |
| 24–25 | Segment 8 — Air-Gapped Exercise | Not represented | Out of scope — live/air-gapped only |
| 26 | Decision Dilemma | Scene "Decision" (post-GoPhish, pre-Mission Brief) | Narrative — see Scene Bible |
| 27 | Debrief | Scene "Debrief" (post-Mission Brief) | Narrative — see Scene Bible |

### 6.2 Traceability note
All three previously-unplaced slides are now resolved (2026-08-06). Slide 13 (Where AI Fits In OSINT Now) renders as a narrative lead-in inside Room 7b, ahead of that room's Pause-for-Demo interstitial (DECISIONS.md #014) — it does not get its own scene. Slides 26 (Decision Dilemma) and 27 (Debrief) are placed as their own scenes per the frozen Scene Bible order (DECISIONS.md #008–#011), with a new "Mission Brief" scene inserted between GoPhish/Decision and Debrief.

### 6.3 `ppt/04 OSINT 1.pptx` — resolved: reference deck only, not in scope
**Resolved 2026-08-06 (DECISIONS.md #009).** This separate, 23-slide deck ("Class 4 of 6," Information Warfare School, "Cyber Crime & Autonomous Threats") — with different framing, a fictional composite case subject ("Hav. [X]," a training persona per Creative Bible §4.5), and different demos (EXIF/GeoSpy, Strava/IDF, Red Flag Drill) — is confirmed as **reference material only** for Version 1: it may inform explanations, examples, or future artwork, but supplies no scenes, rooms, or content in this build. It is not mapped into the Scene Bible. Any future use of this deck's content is a separate, deliberate scope decision (e.g. a later mission/module), not an extension of this one.

---

## 7. Acceptance Criteria (Definition of Done)
Per `PROJECT.md`, the build is done when:
1. Double-clicking `index.html` runs the complete experience with no manual setup.
2. No network request fires at any point (verified with networking disabled).
3. Every FR in §3 is demonstrably satisfied by manual walkthrough.
4. Every NFR in §4 passes its stated verification method.
5. The watermark (FR-21) is present and unremovable in every scene.
6. All four demo-pause handoffs (FR-16–18) are unambiguous to a first-time instructor without additional verbal explanation.

---

## 8. Open Decisions Carried Forward

### 8.1 Resolved 2026-08-06 (see DECISIONS.md #008–#011)
1. ~~`04 OSINT 1.pptx` role~~ — **Resolved: reference-only, not in scope for Version 1** (§6.3).
2. ~~Slides 26, 27 placement~~ — **Resolved: placed as "Decision" and "Debrief" scenes**, with a new "Mission Brief" scene between them (§6.1, §3.3).
3. ~~Key Wall scope~~ — **Resolved: renamed "Mission Board"; scope fixed at the 9 Version-1 rooms; additional concept-art rooms become locked/"Coming Soon" placeholders only** (§3.2, DECISIONS.md #011).
4. ~~SignalGate/Fiery Cross Reef merge~~ — **Resolved: stay two separate rooms** (DECISIONS.md #010).
5. ~~Slide 13 placement~~ — **Resolved: narrative lead-in inside Room 7b (OSINT Tool Chain), before the Pause-for-Demo interstitial** (DECISIONS.md #014).
6. ~~Minimum hardware spec~~ — **Resolved: dual-core ~2.0GHz+, 8GB RAM, integrated graphics, 1280x800 min., evergreen browser** (DECISIONS.md #016). Size budget confirmed at ≤150MB (DECISIONS.md #017).
7. ~~Audio requirement firmness~~ — **Resolved: required to ship (stays High priority), but failure to play (blocked autoplay, no audio device) remains non-blocking per NFR-6** (DECISIONS.md #018).
8. ~~Cold Open / Operations Centre split~~ — **Resolved: confirmed as interpreted in Scene_Bible.md §2.1** (DECISIONS.md #019).
9. ~~Easter Egg Wall assets~~ — **Resolved: registered as EE001–EE004 in Asset_Register_v1.0.xlsx** (DECISIONS.md #015).

### 8.2 Still open
None remaining from this milestone's review. Any new open items surface during Milestone 2 (asset generation) or Milestone 3 (build) will be added here.

These are also tracked in [Repository_Audit.md](Repository_Audit.md) §9 and reflected in [TODO.md](../TODO.md).
