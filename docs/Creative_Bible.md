# Creative Bible
## Prakāśa-chara: In Plain Sight

**Version:** 1.0 (Milestone 1)
**Date:** 2026-08-06
**Status:** Draft — for review
**Related:** [Scene_Bible.md](Scene_Bible.md), [UI_Style_Guide.md](UI_Style_Guide.md), [docs/OSINT_Hotel_Scrollytelling_Brief.md](OSINT_Hotel_Scrollytelling_Brief.md)

---

## 1. Title & Premise

**Prakāśa-chara** (प्रकाशचर) — "moving/existing in the light," i.e. **in plain sight**. The title states the thesis of the entire session: nothing in these case studies required a breach. It required only looking at what was already visible, and having the discipline to look properly.

**One-line concept** (from the brief, signage updated per DECISIONS.md #012): the trainee peers over the shoulder of an operator at a bank of monitors, gets pulled into the central screen, walks a neon backstreet toward a distant "HACK METH" sign — but detours into the **OSINT Hotel**, where a key wall unlocks topics as rooms, and some doors don't open into a room at all — they open onto a real terminal, the cue to break from the story and run the actual demo.

## 2. World & Tone

- **Genre register:** Tron-adjacent cyber-noir. Restrained, not campy — this is professional military training, not a game skin. Neon and grid-lines exist to make abstract information-security concepts spatially legible (a "room per topic" mnemonic), not to be spectacle for its own sake.
- **Mood arc:** cold/observational (Cold Open, Monitor Wall) → propulsive curiosity (The Pull, The Lane) → contemplative/investigative (the five narrative rooms) → a deliberate tonal break (the four terminal rooms — calm, procedural, almost clinical, in contrast to everything else) → quiet close with unresolved tension (Cliffhanger).
- **Restraint principle:** the case-study rooms (SignalGate, Fiery Cross Reef, Gulf Censorship) are the tonal ballast of the piece — they are real incidents with real consequences. The neon/noir treatment applies to the *architecture* (the hotel, the lane, the key wall) never to the *content* of a case study itself. A case-study room's walls can glow; the facts inside it must not be sensationalized. See §4.

## 3. POV & Voice

- **The trainee is the player-character** and is never named, voiced, or given dialogue — the camera work in the Scene Bible *is* their POV. This keeps the piece usable across a whole class watching one screen, not just a single named protagonist's story.
- **The silhouetted operator** (Cold Open) is atmospheric framing only — not a character who speaks or is later revealed. Do not develop them into a mentor/guide figure; the brief's design intentionally leaves them as a wordless establishing presence.
- **No narrator voice-over is specified or assumed.** All information delivery is environmental/textual (room signage, on-screen text blocks pulled from the source deck) plus, where the class is live, the instructor's own narration — the product supports the instructor, it doesn't replace them.
- **Writing voice for in-room text:** direct, procedural, confident — matches the source deck's register ("The camera didn't lie — an official broadcast did the exposing," "Official channels went silent. Open sources didn't."). Preserve the deck's existing phrasing where it's already load-bearing; do not "improve" or dramatize wording found in `OSINT SE Session.pptx` when it lands in a room (see §6, content fidelity rule).

## 4. Real-World Case Studies — Sensitivity & Fidelity Rules

Three rooms dramatize real, named, publicly reported incidents (SignalGate, PLA Fiery Cross Reef, Gulf Censorship). These rules govern how they may be presented:

1. **Facts stay exactly as reported in the source deck.** No embellishment, no invented dialogue, no invented internal details not present in the source slide. The deck's own wording (slides 6, 7, 16 of `OSINT SE Session.pptx`) is the ceiling of specificity — the web experience may present it more visually, never more speculatively.
2. **No real individuals are depicted, named-and-pictured, or given a likeness.** Where the source material references a "senior official" or unnamed state personnel, the room's imagery stays environmental (a phone on a bed, a broadcast frame reference, a reef under moonlight) — never a generated portrait standing in for a real person.
3. **State/national framing is handled neutrally.** "PLA Cyberspace Force," "Gulf" strikes, and any named government stay factual and non-editorializing — the lesson is the OSINT tradecraft (official media as a source; geolocation/verification methodology), not a political position on the incident itself.
4. **Media assets sourced from real reporting** (SignalGate screenshots, the Fiery Cross Reef frame-grab, verified Gulf strike footage/geolocation maps — per the brief's Asset Needs section) must carry attribution when used, and a labelled placeholder must be used instead if provenance/licensing can't be confirmed by build time (brief's own fallback rule — do not block the build waiting on rights clearance).
5. **`ppt/04 OSINT 1.pptx` is reference-only for Version 1** (resolved 2026-08-06, DECISIONS.md #009) — it supplies no scenes or rooms in this build. Should any future mission ever dramatize it, this rule set applies equally: that deck's "Hav. [X]" case file is explicitly a **fictionalized composite training persona**, not a real service member, and must stay clearly framed as a training construct, never presented as a real individual's history.

## 5. Themes

1. **Passive OSINT is not passive in consequence.** No hacking occurred in either headline case study — the throughline of Segment 1 and both case studies is that public information, correctly correlated, is itself an operational risk.
2. **Discipline over tooling.** The Information Cycle (Direction → Collection → Processing → Analysis → Dissemination) is presented as a *process*, not a tool list — the rooms should reinforce that the hard part is judgment (Analysis), not access.
3. **Authorization is not optional just because a source is public.** Segment 4's ethics content ("Passive OSINT ≠ blanket permission") is a hard line the Grey Areas room must not soften.
4. **Recon feeds pretext.** The SE Bridge room's physical "carrying an object between two doors" motif exists specifically to make the Recon → Pretext handoff visually concrete — this is the single most important conceptual bridge in the whole piece, since it's the literal link into IW/HAK/15.4.
5. **The experience deliberately withholds resolution.** Both the Cliffhanger Close and (per SRS §6.2) the still-unplaced Decision Dilemma/Debrief slides exist to keep the trainee in an active, unresolved thinking state rather than a "lesson complete" state — any future placement of those slides should preserve, not resolve, that tension.

## 6. Content Fidelity Rule (binding on all future content work)
Any body text pulled into a room from `OSINT SE Session.pptx` must be traceable verbatim or near-verbatim to its source slide (see SRS §6.1 traceability table). This is a production discipline, not just a style preference: it keeps the web experience and the live-taught deck in sync so an instructor is never caught explaining a discrepancy between what the class saw on-screen and what the slide deck says.

## 7. Naming Conventions (canon, do not alter without a DECISIONS.md entry)
| Name | Refers to |
|---|---|
| OSINT Hotel | The hub building; reception houses the Mission Board |
| Mission Board | The hub navigation surface (formerly "Key Wall" in early concept art — renamed per DECISIONS.md #011). UI copy reads "Available Intelligence Missions," not "Select a Room." |
| HACK METH | The distant sign on the Lane (canonical name per DECISIONS.md #012, supersedes the brief's "RED TEAM OPS"); destination of the *next* module (IW/HAK/15.4), never entered in this build |
| The Lane | The Tokyo-backstreet connective scene (Scenes 3, 9) |
| The Bridge | SE Bridge room (Scene 6e) — also a thematic pun (see Themes §5.4) |
| Apex Dynamics | The decoy training org used in the live demo segments (SET/GoPhish/Exercise) — referenced only in demo-pause handoff text, never built out as in-browser content, since it belongs to the live/air-gapped world |

### 7.1 Mission Board — reserved expansion entries (DECISIONS.md #011)
Early concept art for the hub depicted ~20 keys, far beyond Version 1's 9 rooms (5 narrative + 4 terminal). That art was exploratory — meant to make the room feel like a real intelligence facility and suggest future depth, not to redefine the syllabus. The resolution: the extra entries (Threat Intelligence, Dark Web & Leaks, GEOINT Suite, Imagery & Metadata, OPSEC & Privacy, Report & Attribution, Archive Vault, and similar) may still appear on the Mission Board **as locked, inert placeholders** — a "Coming Soon" or "Available in a future mission" treatment, exactly like a game campaign screen — with no click handler, no room, no content behind them (SRS FR-8a). This gives the room its intended visual richness without expanding what Version 1 actually teaches.

## 8. Continuity to IW/HAK/15.4
The entire piece is structured as a first chapter, not a standalone story: the HACK METH sign is visible from Scene 3 onward and never entered; the Cliffhanger Close names the next module explicitly; the SE Bridge room's "recon becomes pretext" framing is the direct conceptual handoff (source slide 19: "This is the direct link into IW/HAK/15.4"). Any future module built for IW/HAK/15.4 should be treated as free to open on "arriving at the HACK METH door," picking up exactly where this build stops.

## 9. What This Experience Is Not
- Not a game with failure states, scoring, or branching narrative outcomes — the Mission Board is a navigation menu with a visited/unvisited state (plus inert locked placeholders, §7.1), not a puzzle with a wrong answer.
- Not a simulation of any live tool (dorking, theHarvester, Sherlock, SpiderFoot, SET, GoPhish) — see DECISIONS.md #007 and SRS FR-18. If a future contributor is tempted to "just mock up what the terminal would show," that is explicitly out of scope and undercuts the real demo per the brief.
- Not a vehicle for embellishing real incidents for dramatic effect (§4).
