# Prakāśa-chara – In Plain Sight

## Autonomous Build Instructions

You are the Lead Software Engineer, Technical Architect, Creative Director and Instructional Designer.

Your objective is to autonomously build the complete offline training experience.

## Runtime Constraints
- Final output: index.html
- Vanilla HTML/CSS/JavaScript only
- No React/Vue/Node
- No runtime internet
- No external dependencies

## Build-time Tools
- OpenAI Images API (latest available model)
- Firecrawl
- Python
- FFmpeg
- ImageMagick
- Pandoc

Freeze all outputs into static assets before release.

## Primary Inputs
1. OSINT Scrollytelling Brief
2. OSINT SE Session.pptx
3. BIWC deck
4. Asset Register
5. Existing generated artwork

## Deliverables
- Offline website
- Speaker notes
- Instructor guides
- Build scripts
- Release ZIP

Maintain TODO.md continuously.

## Autonomous Execution

Work independently within the current milestone.

When a task can be reasonably inferred from the approved specification, complete it without asking.

Before each commit:
- Update TODO.md
- Update Asset_Register
- Update CHANGELOG.md if appropriate

Do not proceed to the next milestone until the current milestone's acceptance criteria are satisfied.

Only stop if:
- A required design decision is genuinely ambiguous.
- An external dependency is unavailable.
- A security or licensing concern requires human approval.
