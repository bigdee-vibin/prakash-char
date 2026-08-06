# Scene Bible
## Prakāśa-chara: In Plain Sight — Version 1

**Version:** 1.0 (Milestone 1)
**Date:** 2026-08-06
**Status:** Draft — for review. Scene order and room set are **frozen** per the 2026-08-06 product decision (DECISIONS.md #008–#011); content details within each scene remain refinable in Milestone 2.
**Related:** [SRS.md](SRS.md) §6, [Creative_Bible.md](Creative_Bible.md), [Component_Specification.md](Component_Specification.md), [Asset_Register_v1.0.xlsx](Asset_Register_v1.0.xlsx)

---

## 0. Frozen Scene Order

```
Cold Open → Operations Centre → Monitor Wall → (The Pull) → Cyber Lane → Reception
   → Mission Board (hub) ─┬→ Foundations
                           ├→ SignalGate
                           ├→ Fiery Cross Reef ("PLA")
                           ├→ Grey Areas & Legal
                           ├→ SE Bridge
                           ├→ Google Dorking (terminal)
                           ├→ OSINT Tool Chain (terminal)
                           ├→ SET (terminal)
                           └→ GoPhish (terminal)
   → Decision → Mission Brief → Debrief → Ending (Lane Return → Cliffhanger)
```
Mission Board rooms (Foundations through GoPhish) are non-linear/click-order-free per SRS FR-10; everything before and after the hub is the fixed linear walk.

---

## 1. Scene-by-Scene Detail

### Scene 0 — Cold Open
- **Type:** linear-scene · **Interaction:** static hold, no scroll yet
- **Visual:** title/mission-splash card — Prakāśa-chara mark, minimal, holds for a beat before scroll unlocks (SRS FR-1).
- **Asset:** `A001` Mission Splash (Opening category, status: To Generate, High priority).
- **Audio:** none (silence before the ops-room tone begins).
- **Note:** see §2.1 — this reassigns the original brief's "dark ops room, silhouette of operator" description to the *next* scene (Operations Centre), since the frozen order treats them as two distinct beats.

### Scene 0b — Operations Centre
- **Type:** linear-scene · **Interaction:** static/minimal parallax, scroll not yet the primary driver
- **Visual:** dark SOC room, silhouette of a military-uniformed operator, back to camera, lit only by monitor glow — the brief's original Cold Open framing.
- **Asset:** `B001` Operations Centre (Cold Open category, status: To Generate, High priority).
- **Source:** brief §"Full Scene Flow" row 0.
- **Audio:** `AU002` Operations (SOC ambience loop, To Source).

### Scene 1 — Monitor Wall
- **Type:** linear-scene · **Interaction:** scroll = slow pan, left to right (SRS FR-2)
- **Visual:** 4–5 peripheral monitors around a dim central monitor; each peripheral loops ambient footage referencing a prior course topic.
- **Asset:** `B002` Monitor Wall (Cold Open category, To Generate, High priority).
- **Easter Egg Wall assets (Python / Networking / PowerShell / Bash looping monitors):** **not currently rows in the Asset Register** — flagged gap, see §3.1.
- **Component:** C-12 Easter Egg Monitor (Component Specification).
- **Audio:** `AU002` continues.

### Scene 1b — The Pull
- **Type:** linear-scene (transition) · **Interaction:** scroll-triggered zoom (SRS FR-3)
- **Visual:** peripheral monitors blur/dim; central monitor brightens and fills the viewport; room fades to black around it.
- **Asset:** `B003` Screen Pull (Cold Open category, To Generate, High priority).
- **Component:** C-3 Camera Transition (`zoom-in`).

### Scene 2 — Cyber Lane
- **Type:** linear-scene · **Interaction:** scroll = walking forward (SRS FR-4)
- **Visual:** Tron-style neon grid floor, rain-slicked reflective ground, Tokyo-backstreet signage. Far down the lane: the distant sign that grows almost imperceptibly with each scroll stage.
- **Asset:** `C001` Cyber Lane (To Generate, High priority); distant-sign detail per `C005` (see §3.2 naming flag).
- **Audio:** `AU001` Rain (To Source, High priority).
- **Note:** sets up the next module as "where this is headed" (brief), never entered in Version 1.

### Scene 3 — Reception ("The Turn")
- **Type:** linear-scene (transition into hub) · **Interaction:** scroll/click prompt triggers camera rotation (SRS FR-5)
- **Visual:** the OSINT Hotel building, flickering neon sign; camera rotates off the lane through the hotel doors into the lobby.
- **Assets:** `C004` OSINT HQ exterior (building) + `D001` Reception Lobby (both To Generate, High priority).
- **Component:** C-3 Camera Transition (`rotate-turn`).

### Scene 4 — Mission Board (hub)
- **Type:** linear-scene entry point → non-linear hub · **Interaction:** click-driven (SRS §3.2)
- **Visual:** the reception desk's hub surface — 9 active mission keys (all initially unlit) plus reserved-expansion placeholders shown locked (Creative Bible §7.1, DECISIONS.md #011). Heading copy: "Available Intelligence Missions."
- **Asset:** `D003` Key Wall (Reception category, To Generate, High priority) — visual asset name predates the Mission Board rename; same artwork, renamed in-fiction only, no new generation needed solely for the rename.
- **Components:** C-4 Mission Board Hub, C-4a Key Control (×9), C-4b Locked Placeholder (×N reserved).
- **UI cue:** one-time "you are now choosing" pulse (UI Style Guide §4) on first entry.

---

### Room 6a — Foundations
- **Type:** narrative-room · **Key:** FOUNDATIONS
- **Source slides:** `OSINT SE Session.pptx` #3–5 (Segment 1 — Definition & Sources, The Information Cycle)
- **Content beats:** OSINT definition; source categories (search engines/dorking, social media, public records, DNS/WHOIS, satellite imagery, cert transparency, breach DBs, code repos); the 5-stage Information Cycle (Direction → Collection → Processing → Analysis → Dissemination).
- **Assets:** `F001` Foundations Room, `F002` Source Board (HTML/SVG — buildable in-code, not image-generated).
- **Visual motif:** study with card-catalogue drawers, one open with light spilling out (library-as-sources metaphor, per brief).

### Room 6b — SignalGate
- **Type:** narrative-room (case study) · **Key:** SIGNALGATE
- **Source slide:** `OSINT SE Session.pptx` #6
- **Content beat:** the accidental group-chat addition → cascading disclosure; "no hacking required to start the chain."
- **Assets:** `SG001` SignalGate Room, `SG002` Timeline (SVG/HTML).
- **Visual motif:** phone face-up on the bed, cracked screen, a frozen group-chat notification cascade projected on the wall.
- **Sensitivity handling:** Creative Bible §4 rules 1–2 apply in full — facts stay exactly as reported, no invented details, no depiction of the real official involved.

### Room 6c — Fiery Cross Reef ("PLA")
- **Type:** narrative-room (case study) · **Key:** FIERY_CROSS_REEF
- **Source slide:** `OSINT SE Session.pptx` #7
- **Content beat:** the Lunar New Year broadcast that inadvertently revealed a PLA Cyberspace Force unit's location; "official propaganda is a legitimate OSINT source."
- **Assets:** `FC001` Fiery Cross Reef (Broadcast room), `FC002` Cable Overlay (map, SVG).
- **Visual motif:** window over a night ocean/reef; a small broadcast screen replaying the same frame-grab on loop.
- **Kept separate from SignalGate per DECISIONS.md #010** — distinct lesson: broadcast/GEOINT/visual-intelligence/infrastructure analysis vs. operational-security/human-error/messaging.

### Room 6d — Grey Areas & Legal
- **Type:** narrative-room · **Key:** GREY_AREAS
- **Source slides:** `OSINT SE Session.pptx` #14–16 (Segment 4 — Ethics & Authorisation; case study — Gulf Censorship vs. OSINT Exposure)
- **Content beats:** "Passive OSINT ≠ blanket permission"; authorization-in-writing rule; the Gulf case study (official silence vs. verified open-source geolocation).
- **Asset:** `GA001` Grey Areas Room.
- **Visual motif:** room papered floor-to-ceiling with redacted clippings, hairline cracks of light showing verified footage underneath.
- **Style note:** hard-line ethics statements render in `--pc-alert-critical` per UI Style Guide §1 — used only here, sparingly.

### Room 6e — SE Bridge
- **Type:** narrative-room · **Key:** SE_BRIDGE
- **Source slides:** `OSINT SE Session.pptx` #17–19 (Segment 5 — SE Definition & Types; Recon → Pretext: The Bridge)
- **Content beats:** SE definition and vectors (phishing/spear-phishing, vishing incl. deepfake-enabled, smishing, pretexting); "every SE pretext is only as good as the recon behind it"; direct link into IW/HAK/15.4.
- **Asset:** `SB001` SE Bridge.
- **Visual motif:** a short bridge/corridor between two doors ("RECON," "PRETEXT") — walking across visibly carries an object (folder/documents) from one door to the other.

---

### Room 7a — Google Dorking (terminal)
- **Type:** terminal-room · **Key:** GOOGLE_DORKING
- **Source slides:** `OSINT SE Session.pptx` #8–10 (Segment 2)
- **Handoff text:** `>> LIVE DEMO — see instructor workstation`
- **Target setup:** "Instructor laptop — real internet, pre-cleared target only"
- **Asset:** `GD001` Google Dorking Terminal.

### Room 7b — OSINT Tool Chain (terminal)
- **Type:** terminal-room · **Key:** TOOL_CHAIN
- **Source slides:** `OSINT SE Session.pptx` #11–12 (Segment 3). **Slide 13 ("Where AI Fits In OSINT Now") remains unplaced** — SRS §8.2 open item; candidate for a short narrative lead-in here before the terminal transition, not yet decided.
- **Handoff text:** `>> LIVE DEMO — see instructor workstation`
- **Target setup:** "Instructor laptop — theHarvester → Sherlock → SpiderFoot, real internet"
- **Asset:** `TC001` Tool Chain.

### Room 7c — SET (terminal)
- **Type:** terminal-room · **Key:** SET
- **Source slides:** `OSINT SE Session.pptx` #20–21 (Segment 6)
- **Handoff text:** `>> LIVE DEMO — see instructor workstation`
- **Target setup:** "Kali VM (attacker) → Ubuntu VM (Apex Dynamics decoy) — air-gapped"
- **Asset:** `ST001` SET Room.

### Room 7d — GoPhish (terminal)
- **Type:** terminal-room · **Key:** GOPHISH
- **Source slides:** `OSINT SE Session.pptx` #22–23 (Segment 7)
- **Handoff text:** `>> LIVE DEMO — see instructor workstation`
- **Target setup:** "Kali/Debian VM → Ubuntu VM decoy mailbox — air-gapped"
- **Asset:** `GP001` GoPhish Room.

---

### Scene 5 — Decision
- **Type:** linear-scene (post-hub) · **Trigger:** after Check-out (all 9 keys visited, SRS FR-14)
- **Source slide:** `OSINT SE Session.pptx` #26 — Decision Dilemma ("As an officer supervising an OSINT team, you're asked to profile a mediator nation's minister ahead of sensitive talks... What's your one-line authorisation policy before tasking begins?")
- **Asset:** `DD001` Decision Screen (Decision category, "Instructor discussion" — exact match).
- **Function:** a deliberately unresolved prompt — per Creative Bible §5.5, this scene should provoke class discussion, not present a "correct" answer in-browser.

### Scene 6 — Mission Brief
- **Type:** linear-scene · **Position:** between Decision and Debrief (new scene, no direct pptx slide source)
- **Candidate asset:** `EX001` Mission Control ("Apex briefing") — **flagged for reconciliation**, see §3.3: this row is currently categorized "Exercise" in the Asset Register, associated with Segment 8 (the air-gapped exercise, out of scope per SRS §6.1). Needs a decision on whether this asset is repurposed for this scene or a new one is registered.
- **Function:** TBD content — likely a short wrap framing the trainee's mission as complete before Debrief. Content authoring deferred to Milestone 2.

### Scene 7 — Debrief
- **Type:** linear-scene
- **Source slide:** `OSINT SE Session.pptx` #27 — Debrief ("Same target. Different dossiers... The dossier you built is exactly what IW/HAK/15.4 picks up next.")
- **Asset:** `DB001` Mission Debrief (Debrief category, "Summary room" — exact match).

### Scene 8 — Ending (Lane Return → Cliffhanger)
- **Type:** linear-scene · **Interaction:** final scroll stretch (SRS FR-6–7)
- **Visual:** back on the Lane, distant sign now closer/brighter; camera stops just short of its door; text overlay: *"To be continued in IW/HAK/15.4 — Gaining Access."* Fade to black.
- **Assets:** `EN001` Lane Return, `EN002` "HACK METH Reveal" (see §3.2 naming flag).
- **Deliberately non-terminal** per Creative Bible §5.5 and §8 — no resolution.

---

## 2. Reconciliation Notes (Cold Open / Operations Centre split)

### 2.1
The original brief describes a single Scene 0 ("Cold Open — dark ops room, silhouette of operator") that the Asset Register also captures as a single row (`B001` Operations Centre). The 2026-08-06 frozen order names **two** sequential beats: "Cold Open" then "Operations Centre." This Scene Bible resolves that by treating "Cold Open" as a new, minimal title/splash beat (using `A001` Mission Splash) and reassigning the brief's original dark-ops-room description to "Operations Centre" (using `B001`). **This is an interpretation, not a confirmed decision** — flag for sign-off if a different split was intended.

## 3. Open Items / Flags Requiring a Decision

### 3.1 Easter Egg Wall assets missing from the register
The four peripheral-monitor loops (Python, Networking, PowerShell, Bash — brief §"Easter Egg Wall") have no corresponding Asset Register rows. Needs 4 new rows (or one combined asset) added at Milestone 2.

### 3.2 "RED TEAM OPS" vs. "HACK METH" signage — naming conflict
The written brief consistently names the Lane's distant signage **"RED TEAM OPS"** (the destination sign, tied to IW/HAK/15.4 — "Gaining Access"). The Asset Register (`C005` "HACK METH — Future module exterior", `EN002` "HACK METH Reveal") and prior exploratory concept art both use **"HACK METH"** instead. These are two different labels for what should be the same in-world sign. Per the scope-authority decision (DECISIONS.md #008, brief text is authoritative for instructional content), this Scene Bible does **not** silently pick one — this is a naming decision for you to confirm before Milestone 2 asset generation, since it determines what text gets baked into generated signage art (expensive to redo).

### 3.3 "Mission Brief" scene — asset and content ambiguity
`EX001` ("Mission Control") and `EX002` ("Apex Dossier") are registered under category "Exercise," which — per SRS §6.1 — maps to Segment 8 (the air-gapped exercise, explicitly out of scope for the web build; live/air-gapped only). The new "Mission Brief" scene in the frozen order has no clear source slide or confirmed asset. Needs a decision: reuse `EX001` for this narrative beat (renaming its register purpose), or register a new asset, or fold "Mission Brief" content into the adjacent Decision/Debrief scenes instead of standing alone.

### 3.4 UI chrome components not yet scene-mapped
`UI001` Mission Log, `UI002` Notebook, `UI003` Evidence Card are registered as reusable HUD/widget assets but aren't tied to specific scenes in this bible — they're persistent chrome likely available across some or all narrative rooms (per Component Specification, C-7 Case Study Card is related but distinct). Which rooms use which widgets is deferred to Milestone 3 component wiring, not blocking this milestone.

### 3.5 Slide 13 placement (carried from SRS §8.2)
"Where AI Fits In OSINT Now" has no confirmed home; §Room 7b above proposes a narrative lead-in as one option, not yet decided.
