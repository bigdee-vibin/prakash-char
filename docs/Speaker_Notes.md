# Speaker Notes
## Prakāśa-chara: In Plain Sight — IW/HAK/15.3

**Version:** 1.0 (Milestone 4)
**Date:** 2026-08-06
**Audience:** the instructor delivering the session live, reading these while the class watches the screen (individually or projected).
**Related:** [Instructor_Guide.md](Instructor_Guide.md), [Scene_Bible.md](Scene_Bible.md), [Creative_Bible.md](Creative_Bible.md)

Notes are grouped in the order the experience actually plays in `index.html`. Timing is a rough guide, not a script — let the room's pace set it, especially through the Mission Board.

---

## Linear Walk (pre-hub)

**Cold Open** (~5s, no input needed)
Just let it sit. Don't narrate over the title card — it's meant to be a beat, not a slide.

**Operations Centre**
> "This is where OSINT work actually starts — not with a target, but with a watch."
Good moment to mention this session builds on Modules I–II (Python, Networking, PowerShell, Bash) without dwelling on it — the Easter Egg Wall in the next scene is the callback, not this one.

**Monitor Wall**
If anyone asks about the peripheral screens: they're texture, not content — a nod to prior coursework, not something they need to read.

**The Pull → The Lane**
> "We're about to walk into a version of the internet as a place. Neon city, rain, a street that doesn't end — and one sign you'll keep seeing: HACK METH. That's not tonight's session. That's next."
This is the moment to set expectations: today is Foundations, two case studies, ethics, and the SE bridge — not the live tool demos yet (those happen inside the hotel, and they're real, not simulated on screen).

**Reception — The Turn**
> "OSINT Hotel. Every topic today has a room."

---

## Mission Board (hub)

> "Nine keys. Pick any order. Five open into rooms you read. Four open onto a real terminal — that's your cue to look at me, not the screen."

Call out explicitly, once, before anyone clicks: **the grey/locked tiles below the active nine are not part of today's session** — they're future material. Nobody needs to ask what they are.

---

## Room-by-room

### Foundations Room
Source: `OSINT SE Session.pptx` #3–5. Anchor the Information Cycle here — Direction → Collection → Processing → Analysis → Dissemination — this is the model the rest of the day keeps referring back to. If time is short, this is the room to slow down in, not skip.

### SignalGate Suite
Source: slide #6. Keep it factual — this happened, no hacking was involved, the failure was tool choice and group management. **Do not embellish beyond what's on screen.** If a trainee asks "what did the messages actually say," the honest answer is: not something this room dramatizes, and not something you should either.

### Fiery Cross Reef Suite
Source: slide #7. The teaching point is "official propaganda is a legitimate OSINT source" — a state's own broadcast did the work here, not an adversary. Keep coordinates/dates you cite limited to what's actually documented; don't improvise specifics.

### Grey Areas & Legal
Source: slides #14–16. This room carries the one hard rule of the day:
> "Never test systems or people you don't have written authorisation to test. Passive OSINT is not blanket permission."
Say it plainly once. Don't soften it.

### The Bridge (SE)
Source: slides #17–19. This is the conceptual hinge of the whole session — recon becomes pretext. If you only have time to land one idea from this room: *the dossier isn't the product, it's raw material for the next stage.* That next stage is IW/HAK/15.4.

### Terminal rooms (Google Dorking / Tool Chain / SET / GoPhish)
All four follow the same shape: the room opens, then hands off with `>> LIVE DEMO — see instructor workstation`. **This is your cue, not a suggestion** — switch to the real setup named on screen (instructor laptop / Kali VM / air-gapped VM pair, per room). See [Instructor_Guide.md](Instructor_Guide.md) for exact pre-staging per room.

The Tool Chain room additionally shows a short note on AI-assisted OSINT before the handoff (slide #13) — worth a beat: faster triage, not better judgment, and every AI-assisted finding still needs manual verification.

---

## Post-Mission-Board

**Decision**
Read the dilemma aloud, then stop talking. This is discussion bait, not a quiz — there's no on-screen answer.

**Mission Brief → Debrief**
Debrief prompts: *where did findings converge/diverge, what did the exercise leak that a real org leaks too, and the dossier feeds straight into 15.4.* Good closing beat for Q&A before the cliffhanger.

**Cliffhanger**
Let it play without narration. The next module handles the reveal.

---

## Known display caveats (say nothing unless asked)
A few generated backgrounds still have minor visual issues (documented in TODO.md/DECISIONS.md #025) — none affect what you say, only what's on screen behind you. Not worth flagging to trainees.
