# OSINT & Social Engineering — Scrollytelling Brief
### "The OSINT Hotel"
**For:** IW/HAK/15.3, Joint Advanced Cyber Security Course
**Handoff target:** Claude Design (visual build)
**Companion asset:** `OSINT_SE_Session.pptx` (source content — this brief re-skins Segments 1, 4, 5 + the three case studies as an explorable scene; Segments 2, 3, 6, 7 stay live-demo, called out below as pause points)

---

## One-line concept

The trainee peers over the shoulder of an operator at a bank of monitors, gets pulled *into* the central screen, walks a neon Tokyo backstreet toward a glowing "RED TEAM OPS" sign in the far distance — but detours into the **OSINT Hotel** first, where a locked key-wall unlocks each topic as its own room, and select doors don't open into a themed room at all — they open onto a real terminal, because that's the cue to break from the story and run the actual demo.

---

## Full Scene Flow

| # | Scene | Visual | Scroll / Interaction | Maps to | Demo Pause |
|---|-------|--------|----------------------|---------|:---:|
| 0 | **Cold Open** | Dark ops room. Silhouette of a military-uniformed operator, back to camera, lit only by monitor glow. Peeping-over-the-shoulder framing. | Page load, no scroll yet — establishing shot holds for a beat | Title / mood-set | — |
| 1 | **The Monitor Wall** | 4–5 peripheral monitors around a larger, dim central one. Each peripheral runs ambient looping footage of a prior course topic (see *Easter Egg Wall* below). | Slow scroll = slow pan across the monitors, left to right | Callback to Modules I–II (Python, Networking, PowerShell, Bash, Windows) | — |
| 2 | **The Pull** | Peripheral monitors blur and dim. Central monitor brightens, fills the viewport. Content on it morphs from idle static into a neon grid horizon. | Scroll-triggered zoom — camera moves *into* the screen; room fades to black around it | Transition beat | — |
| 3 | **The Lane** | Tron-style neon grid floor, rain-slicked reflective ground, Tokyo-anime backstreet signage (katakana-flavoured glyphs, glowing vending machines, steam vents). Far down the lane, small but visible: a neon sign reading **RED TEAM OPS**. | Scroll = walking forward down the lane. RED TEAM OPS sign grows almost imperceptibly with each scroll stage — a constant, deliberate tease | Sets up IW/HAK/15.4 as "where this is headed" | — |
| 4 | **The Turn — OSINT Hotel** | Partway down the lane, a building with a flickering neon sign: **OSINT HOTEL**. The lane keeps receding behind it toward Red Team Ops. | Scroll/click prompts the "turn" — camera rotates off the main lane through the hotel doors | Entry point to Segment 1 (Foundations) | — |
| 5 | **Reception — The Key Wall** | Old-style hotel pigeonhole key rack behind an empty reception desk. Each slot holds one key, engraved with a topic name. All keys start **greyed out / unlit**. | **This is the hub.** Clicking a key lights it up and opens its corridor door. Non-linear from here — trainee/instructor picks order | Navigation hub for Segments 1, 4, 5 + case studies | — |
| 6a | **Room — Definitions & Sources** | Small study, walls lined with card-catalogue drawers (a library metaphor for "sources"), one drawer left open with light spilling out. | Key: "FOUNDATIONS" | Segment 1 — OSINT definition, sources, info cycle | — |
| 6b | **Room — SignalGate Suite** | A hotel room with a phone lying face-up on the bed, screen cracked, a group-chat notification frozen mid-glitch on the wall as a projected cascade. | Key: "SIGNALGATE" | Case study — SignalGate cascade | — |
| 6c | **Room — Fiery Cross Reef Suite** | Window looking out over a night ocean; a reef visible under moonlight; a small broadcast screen on the desk replaying the same frame-grab on loop. | Key: "FIERY CROSS REEF" | Case study — PLA reveal | — |
| 6d | **Room — Grey Areas** | A room papered floor-to-ceiling with redacted newspaper clippings and blacked-out strips — but hairline cracks of light show verified footage underneath, hinting something got out anyway. | Key: "GREY AREAS & LEGAL" | Segment 4 + Gulf censorship case study | — |
| 6e | **Room — The Bridge** | A room that's literally a short bridge/corridor connecting two doors — one marked "RECON," one marked "PRETEXT" — walking across visibly carries an object (a folder, a set of documents) from one door to the other. | Key: "SE BRIDGE" | Segment 5 — recon → pretext | — |
| 7a | **Terminal Room — Dorking** | Door opens *not* into a themed room but a bare desk with a single glowing terminal, chair pulled out, waiting. | Key: "GOOGLE DORKING" | Segment 2 | **⏸ PAUSE — switch to instructor laptop, live dorking** |
| 7b | **Terminal Room — Tool Chain** | Same desk motif, three terminal panes tiled (theHarvester / Sherlock / SpiderFoot idle prompts). | Key: "OSINT TOOL CHAIN" | Segment 3 | **⏸ PAUSE — switch to instructor laptop, live tool chain** |
| 7c | **Terminal Room — SET** | Desk with a Kali-branded terminal, SET banner idle on screen. | Key: "SET WALKTHROUGH" | Segment 6 | **⏸ PAUSE — switch to Kali VM (air-gapped)** |
| 7d | **Terminal Room — GoPhish** | Desk with a GoPhish dashboard idle on screen, mid-load. | Key: "GOPHISH WALKTHROUGH" | Segment 7 | **⏸ PAUSE — switch to Kali/Debian VM (air-gapped)** |
| 8 | **Check-out** | All lit keys return to the rack, now glowing steady instead of grey. Trainee exits through the lobby doors. | Auto-triggers once all keys visited (or a manual "leave" prompt) | Segment 8 handoff | — |
| 9 | **Back on the Lane** | The lane again, RED TEAM OPS now much closer, sign fully legible, glow intensifying. | Final scroll stretch | — | — |
| 10 | **Cliffhanger Close** | Camera stops just short of the Red Team Ops door. Text overlay: *"To be continued in IW/HAK/15.4 — Gaining Access."* Fade to black. | End of experience | Sets up next module — deliberately doesn't resolve | — |

---

## The Easter Egg Wall (Scene 1 detail)

Each peripheral monitor loops ambient, slightly-illegible code/terminal footage from a completed course topic — texture, not readable content:

- **Monitor A — Python:** scrolling interpreter session. Buried in a comment or docstring, half-obscured by scan-line glare: `# Bridge sessions: concept -> demo -> practice. New pedagogy — Lt Col Dheeraj Bharti, JSACW.` — a signature easter egg, only readable if a viewer pauses and looks closely.
- **Monitor B — Networking:** `ip addr`, subnet math scratch notes, a packet capture scrolling in the background.
- **Monitor C — PowerShell:** AD enumeration commands, Windows fundamentals references scrolling past.
- **Monitor D — Bash:** shell scripting loop, permissions/chmod examples.
- **Central monitor (dim, idle):** the one that will "wake up" in Scene 2 — keep it visually inert until the pull triggers.

---

## Design Language

- **Palette:** Tron-adjacent — near-black base, cyan/electric-blue grid lines, hot-pink/magenta neon accents for signage (OSINT HOTEL, RED TEAM OPS), amber for interactive/clickable elements (matches the deck's orange tag colour — keep this one thread of continuity between the deck and the scrollytelling piece).
- **Texture:** light scan-line/VHS grain overlay throughout — ties the "surveillance footage" feel to the OSINT subject matter itself.
- **Typography:** monospace for all terminal/code moments; a clean geometric sans for room signage and UI, katakana-flavoured decorative glyphs (non-functional, atmosphere only) on background signage in the lane scene.
- **Motion:** scroll-linked (not autoplay) for Scenes 0–4 and 8–10 — the linear "walk." Scenes 5–7 break from scroll into click-driven hub navigation — make that shift in interaction model felt, not just functional (e.g. cursor changes, a subtle "you are now choosing" UI cue at the key wall).

---

## The Pause-for-Demo Component

Needs a distinct, reusable UI moment for Scenes 7a–7d — not just "room ends," but an explicit **handoff cue** telling the instructor/class to look away from the screen:

- Suggested treatment: the terminal on-screen visibly stops looping and displays a simple, calm interstitial — e.g. `>> LIVE DEMO — see instructor workstation` — rather than trying to simulate the actual tool output in-browser (that would undercut the real demo, not support it).
- This should feel like a deliberate "fourth wall" break, distinct from every other room's fully-immersive treatment.

---

## Asset Needs (for the image-providing step)

Real/cached source material to slot in once provided:

- SignalGate reporting screenshots/timeline graphic
- PLA Fiery Cross Reef broadcast frame-grab
- Verified Gulf strike footage / geolocation map (or a stand-in composite if licensing is unclear)
- Any of your own BIWC deck imagery you want carried over
- Optional: prompt-generated art for the lane, hotel exterior, and key-wall if no real-world reference exists for those (they're original scene-setting, not incident documentation)

Everything without a provided source will ship as a labelled placeholder, same convention as the pptx deck, so nothing blocks the build.

---

## Explicit Scope Boundary

This brief covers **Segments 1, 4, 5 and the three case studies only.** Segments 2, 3, 6, 7 (live demos) and Segment 8 (air-gapped exercise) are **not** re-skinned into this experience — they stay exactly as designed on real machines. The pause points above are the seams where the two halves of the session meet.
