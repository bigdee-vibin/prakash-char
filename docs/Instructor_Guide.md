# Instructor Guide
## Prakāśa-chara: In Plain Sight — IW/HAK/15.3

**Version:** 1.0 (Milestone 4)
**Date:** 2026-08-06
**Related:** [Speaker_Notes.md](Speaker_Notes.md), [SRS.md](SRS.md), [Scene_Bible.md](Scene_Bible.md)

---

## 1. Setup (before class)

1. Copy the release folder (or unzip the release ZIP — see [Repository README](../README.md)) onto the delivery machine. No installation, no server, no internet required.
2. Double-click `index.html`. It opens in the default browser and runs fully offline.
3. Confirm audio isn't muted in the top-right chrome if you want the ambient loops (optional — the experience works identically muted).
4. **Pre-stage the four live-demo setups** you'll switch to during the session (see §3) — do this before class starts, not during a Pause-for-Demo moment.

**Minimum machine spec** (DECISIONS.md #016): dual-core ~2.0GHz+, 8GB RAM, integrated graphics, 1280×800 minimum display, an evergreen browser (Chrome/Firefox/Edge/Safari, last 2 major versions) on Windows 10/11 or equivalent.

## 2. Session Flow

The web experience covers: Foundations, two case studies (SignalGate, Fiery Cross Reef), Grey Areas & Legal, and the SE Bridge — plus four **handoff points** to your live demos. It does **not** simulate Google Dorking, the OSINT tool chain, SET, or GoPhish on screen — those stay real, on real machines, per the session's own design (DECISIONS.md #007).

Rough shape:
1. Linear intro (no interaction needed beyond scrolling) — Cold Open through Reception.
2. **Mission Board** — trainee/class picks rooms in any order. Five are readable content; four are live-demo handoffs.
3. Once all nine are visited, Check Out unlocks → Decision → Mission Brief → Debrief → Cliffhanger.

You control pacing entirely — nothing on screen auto-advances past a demo handoff.

## 3. The Four Demo Handoffs

Each terminal room ends on a static screen reading `>> LIVE DEMO — see instructor workstation`. When you see it, switch away from the web experience. Pre-staging needed per room:

| Room | Switch to | Pre-stage |
|---|---|---|
| Google Dorking | Instructor laptop, real internet | A pre-cleared target confirmed reachable; dork queries ready (site:, filetype:, intitle:, inurl:, - exclusion) |
| OSINT Tool Chain | Instructor laptop, real internet | theHarvester, Sherlock, SpiderFoot installed and tested against a safe target domain |
| SET Walkthrough | Kali VM (attacker) → Ubuntu VM (Apex Dynamics decoy) — air-gapped | Both VMs booted, network isolated from the internet, decoy login page live on the Ubuntu VM |
| GoPhish Walkthrough | Kali/Debian VM → Ubuntu VM decoy mailbox — air-gapped | GoPhish running, decoy mailboxes provisioned, landing page cloned |

When the live portion is done, return to the browser tab and click **← Back to Reception** to resume.

## 4. Troubleshooting

- **No audio plays.** Expected in some browsers until a user gesture occurs (autoplay policy) — click anywhere on the page first, or it's simply not required; nothing else is affected (NFR-6, graceful degradation by design).
- **Trainee wants to revisit a room.** Fully supported — click any lit key again from the Mission Board at any time.
- **Someone leaves before visiting all nine keys.** No penalty state exists; Check Out simply won't appear on the Mission Board until all nine are lit. There's no requirement to force completion.
- **Blank/black screen after opening `index.html`.** Confirm the `assets/` folder is in the same directory as `index.html` — it must travel together, not be split apart.

## 5. Known Display Caveats (2026-08-06)

A handful of generated background images have minor visual issues, tracked in [TODO.md](../TODO.md) and DECISIONS.md #025 — none affect narration, functionality, or the session's factual content:
- The Mission Board's background art still shows extra key labels behind the (correctly functioning) 9-key/7-locked overlay.
- The Mission Debrief background shows a small text inconsistency (two destination names) in one corner.
- The four terminal-room backgrounds show illustrative screen content that doesn't fully match the "idle terminal" design intent — cosmetic only, no functional demo is simulated regardless of the artwork.

None of these require any action from you during delivery.

## 6. Content Traceability

Every fact presented in the five narrative rooms is sourced from `ppt/OSINT SE Session.pptx` (see [Scene_Bible.md](Scene_Bible.md) for the exact slide-to-room mapping). If a trainee asks where something came from, that deck is the answer.
