# Architecture Decisions

001 Offline-first
002 One HTML output
003 Vanilla HTML/CSS/JS only
004 Firecrawl build-time only
005 OpenAI Images build-time only
006 Persistent watermark:
Lt Col Dheeraj Bharti ©2026
007 Live demonstrations remain instructor-led

008 Scope authority: the approved `docs/OSINT_Hotel_Scrollytelling_Brief.md`
and the 27-slide `OSINT SE Session.pptx` (IW/HAK/15.3) are the sole
authoritative instructional sources for Version 1. Exploratory concept
art may suggest richer environments but does not by itself expand scope.

009 `ppt/04 OSINT 1.pptx` is a reference deck only for this release — it
may inform explanations, examples, or artwork, but supplies no scenes,
rooms, or content in Version 1. Revisit only as a deliberate, separate
scope decision (e.g. a future mission/module).

010 SignalGate and PLA Fiery Cross Reef remain two independent
investigation rooms (not merged into one "Case Studies" room) — they
teach distinct lessons: operational security/human error/messaging
timeline vs. broadcast/GEOINT/visual-intelligence/infrastructure analysis.

011 The hub is named the "Mission Board" (not "Key Wall") in-fiction.
It may display additional, visually-designed entries beyond Version 1's
scope as locked/"Coming Soon" placeholders — inert UI only, with no
navigation, assets, or content behind them.

012 The Lane's distant signage reads "HACK METH" (not "RED TEAM OPS").
This overrides the wording in docs/OSINT_Hotel_Scrollytelling_Brief.md,
which is left as-authored for historical record. HACK METH prevails
because it matches the Asset Register (C005, EN002) and existing
concept art; it still names/teases the next module's destination and
is never entered in this build.

013 The "Mission Brief" scene (between Decision and Debrief) reuses
asset EX001 ("Mission Control"), repurposed from its original
Exercise/Segment-8 categorisation (out of scope, DECISIONS.md #008) to
this in-scope wrap scene. EX002 ("Apex Dossier") is NOT repurposed and
stays tied to the out-of-scope air-gapped exercise. Asset_Register_v1.0.xlsx
updated accordingly.

014 Slide 13 ("Where AI Fits In OSINT Now," OSINT SE Session.pptx) is
placed as a narrative lead-in inside Room 7b — OSINT Tool Chain —
rendered before that room transitions to its Pause-for-Demo
interstitial. It does not get its own scene/room. Rationale: same
source segment (3) as the theHarvester/Sherlock/SpiderFoot demo it
already precedes in the deck; thematically continuous (AI-assisted
correlation/enrichment tooling feeds directly into the tool-chain
demo the room hands off to).

015 Easter Egg Wall assets (Scene 1 peripheral monitors: Python,
Networking, PowerShell, Bash) are registered as EE001-EE004,
category "Cold Open," Medium priority (atmospheric, non-blocking per
FR-23 — distinct from the High-priority core scene/room assets).
Source = HTML/CSS: implemented as CSS-animated monospace text scroll,
not video or generated imagery, to keep the offline bundle light
(Architecture.md C-12).

016 Minimum hardware/runtime baseline for NFR-4/NFR-5: a training-room
laptop with a dual-core ~2.0GHz+ CPU, 8GB RAM, integrated graphics,
1280x800 minimum display, running an evergreen browser (Chrome/
Firefox/Edge/Safari, last 2 major versions) on Windows 10/11 or
equivalent. This is the baseline the 5s load-to-interactive and 60fps
scroll targets (NFR-4) are measured against.

017 Release artifact size budget confirmed at ≤150MB total
(Architecture.md §8's proposed figure), covering ~33 registered
visual assets (.webp) plus 2 ambient audio loops (.ogg).

018 Ambient audio (rain.ogg, ops.ogg) is REQUIRED to ship in the
release (stays High priority in the Asset Register) but its runtime
FAILURE MODE remains non-blocking per NFR-6 — if autoplay is blocked
or a device has no audio output, the experience must still be fully
usable. "Required to exist," not "required to play," resolves the
ambiguity between the Asset Register's High priority and NFR-6's
graceful-degradation requirement.

019 Cold Open / Operations Centre split confirmed as interpreted in
Scene_Bible.md §2.1: "Cold Open" is a new, minimal title/splash beat
(asset A001, Mission Splash) and "Operations Centre" carries the
brief's original dark-ops-room/silhouette description (asset B001).
This resolves the two-beats-vs-one-row discrepancy between the frozen
scene order and the brief/Asset Register.

020 SUPERSEDES 005. Concept-art generation switches from the OpenAI
Images API to the Gemini API (Imagen), because no OpenAI API key is
available. Reason is purely credential availability, not a quality or
style judgment — CLAUDE.md, requirements.txt, prompts/style_lock.md,
scripts/generate_images.py, and Asset_Register_v1.0.xlsx's Source
column updated accordingly (OpenAI Images -> Gemini Images
everywhere it named the generation tool). Still build-time only, same
restriction as before (never called at runtime).

021 SUPERSEDES 020. Gemini's image-generation models require billing
enabled (free tier has a hard 0 quota for image models — not a rate
limit, confirmed via a live 429 RESOURCE_EXHAUSTED response). Rather
than wait on billing, asset sourcing switches to Unsplash stock
photography for the 22 "OpenAI Images"/"Gemini Images"-sourced rows.

This is a real art-direction change, not just a tooling swap: Unsplash
supplies real photography, not custom illustration, so it cannot
render bespoke signage/UI text (e.g. "OSINT HOTEL," "HACK METH," the
Mission Board's engraved key labels, terminal idle prompts). Resolution:
Unsplash photos become mood/environment BACKGROUND LAYERS only; every
piece of bespoke text/signage/neon UI that was previously expected to
be baked into generated art is now rendered as a CSS/SVG OVERLAY at
build/runtime instead (Component Specification C-1's scene container
gains an explicit overlay sub-layer for this — see Component_Specification.md).
The neon/scanline/palette visual language in UI_Style_Guide.md is
unchanged; only where it lives (overlay vs. baked-into-background)
changes.

Asset_Register_v1.0.xlsx Source column updated: the 22 rows move from
"Gemini Images" to "Unsplash" (background photo) with an added Notes
entry naming the required overlay content per asset (see Scene Bible/
Component Specification for overlay content, prompts/assets.json for
the corresponding search queries).

022 REFINES 021 into a hybrid sourcing split, not a blanket move to
Unsplash. 18 of the 22 assets are realistically photographable subjects
(rainy neon streets, SOC rooms, hotel lobbies, terminal desks, a
vintage hotel key rack) and stay sourced from Unsplash + CSS/SVG
overlay per #021. The remaining 4 — A001 (Mission Splash title card),
A002 (Ancient Spotlight), B003 (Screen Pull transition), SB001
(SE Bridge, the two-door/carried-folder staging) — depict compositions
too bespoke/symbolic/narrative-specific to exist as stock photography.
For these 4, ChatGPT-ready illustration prompts are provided directly
to the user (self-contained, style-locked text) for manual generation
outside this session; resulting images are shared back and placed by
Asset ID/fileName. prompts/assets.json's `sourceMethod` field records
"unsplash" vs "chatgpt-manual" per asset; Asset_Register_v1.0.xlsx's
Source column reflects the same split.

023 SUPERSEDES the Unsplash portion of 021/022. A001, A002, B003,
SB001 generated successfully via manual ChatGPT prompts (2026-08-06)
and landed in assets/images/ as .webp; the remaining 18 assets switch
from Unsplash+overlay back to ChatGPT-manual generation as well, for
workflow consistency (single sourcing method, one handoff batch)
rather than maintaining two pipelines. Full illustration prompts for
all 18 (previously drafted for Gemini/Unsplash-overlay use) are
repackaged as prompts/remaining_18_prompts.md and handed to the user
as a zip for manual generation outside this session, matching the
A001/A002/B003/SB001 workflow. Unsplash integration (scripts, API
keys) is left in place but unused — no code deleted, in case a hybrid
approach is wanted again later. Asset_Register_v1.0.xlsx Source
column and prompts/assets.json's sourceMethod field updated to
"ChatGPT (manual)" / "chatgpt-manual" for all 22 rows.

024 Audio sourced 2026-08-06: AU001 (rain.ogg) = "Rain from Indoors -
Perfect loop" by samesamesame, freesound.org/people/samesamesame/
sounds/242889/, genuinely CC0, 48s. AU002 (ops.ogg) = "AMBTech_Server
Room Noise 01_KVV_FREE" by KVV_Audio, freesound.org/people/KVV_Audio/
sounds/715475/, genuinely CC0, 1:42. Both converted from source MP3
to .ogg (libvorbis via ffmpeg) and placed in assets/audio/. Pixabay
candidates were considered first (user-approved) but abandoned after
their download flow proved unscriptable (Cloudflare-protected SPA,
no stable direct file URL); Freesound's CDN serves preview files
directly and its license is genuinely CC0 (matching the Asset
Register's stated requirement exactly, unlike Pixabay's merely
similar Content License).
