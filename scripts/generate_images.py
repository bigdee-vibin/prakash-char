#!/usr/bin/env python3
"""Generate registered concept-art images via the Gemini API (Imagen, build-time only).

Reads prompts/assets.json + prompts/style_lock.md, calls Gemini's image generation for
each asset, converts the result to .webp, and writes it to assets/images/<fileName>.
Never invoked at runtime — CLAUDE.md / DECISIONS.md #005/#020 restrict image generation
to build time. Switched from OpenAI Images to Gemini per DECISIONS.md #020 (no OpenAI
key available) — purely a credential decision, not a style change.

Usage:
  python3 scripts/generate_images.py --dry-run           # print final prompts, no API calls, no cost
  python3 scripts/generate_images.py                     # generate all assets not already on disk
  python3 scripts/generate_images.py --only A001,C005    # generate specific assets
  python3 scripts/generate_images.py --force              # regenerate even if the file already exists
"""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_FILE = ROOT / "prompts" / "assets.json"
STYLE_LOCK_FILE = ROOT / "prompts" / "style_lock.md"
OUTPUT_DIR = ROOT / "assets" / "images"

# Update here if a newer Imagen model becomes available at build time.
IMAGEN_MODEL = "imagen-4.0-generate-001"

SIZE_TO_ASPECT_RATIO = {
    # "WxH" descriptive size (from assets.json) -> nearest Imagen aspect_ratio string
    "1536x1024": "16:9",
    "1024x1536": "9:16",
    "1024x1024": "1:1",
}


def load_style_lock_preamble() -> str:
    text = STYLE_LOCK_FILE.read_text(encoding="utf-8")
    quote_lines = []
    in_quote = False
    for line in text.splitlines():
        if line.startswith("> "):
            in_quote = True
            quote_lines.append(line[2:].rstrip())
        elif in_quote:
            break  # blockquote ended at the first non-'> ' line
    if not quote_lines:
        raise RuntimeError(f"Could not find a '> ' preamble blockquote in {STYLE_LOCK_FILE}")
    return " ".join(l for l in quote_lines if l)


def load_assets() -> list:
    return json.loads(PROMPTS_FILE.read_text(encoding="utf-8"))


def build_final_prompt(preamble: str, asset: dict) -> str:
    return f"{preamble}\n\n{asset['prompt']}"


def aspect_ratio_for(asset: dict) -> str:
    return SIZE_TO_ASPECT_RATIO.get(asset.get("size", "1536x1024"), "16:9")


def generate_one(client, asset: dict, preamble: str, force: bool) -> None:
    from google.genai import types

    out_path = OUTPUT_DIR / asset["fileName"]
    if out_path.exists() and not force:
        print(f"[skip] {asset['assetId']} — {out_path.name} already exists (use --force to regenerate)")
        return

    prompt = build_final_prompt(preamble, asset)
    aspect_ratio = aspect_ratio_for(asset)
    print(f"[gen ] {asset['assetId']} — {asset['title']} ({aspect_ratio})")

    response = client.models.generate_images(
        model=IMAGEN_MODEL,
        prompt=prompt,
        config=types.GenerateImagesConfig(number_of_images=1, aspect_ratio=aspect_ratio),
    )
    if not response.generated_images:
        print(f"       [warn] no image returned for {asset['assetId']} — check API response/safety filters")
        return

    image_bytes = response.generated_images[0].image.image_bytes

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    tmp_png = out_path.with_suffix(".png")
    tmp_png.write_bytes(image_bytes)

    try:
        from PIL import Image

        img = Image.open(tmp_png).convert("RGB")
        img.save(out_path, "WEBP", quality=88)
        tmp_png.unlink()
        print(f"       -> {out_path.relative_to(ROOT)}")
    except ImportError:
        print(f"       Pillow not available — left as {tmp_png.relative_to(ROOT)}, convert to .webp manually")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print final prompts, make no API calls")
    parser.add_argument("--only", type=str, default=None, help="comma-separated asset IDs to generate")
    parser.add_argument("--force", action="store_true", help="regenerate even if the output file exists")
    args = parser.parse_args()

    preamble = load_style_lock_preamble()
    assets = load_assets()

    if args.only:
        wanted = {a.strip().upper() for a in args.only.split(",")}
        assets = [a for a in assets if a["assetId"].upper() in wanted]

    if args.dry_run:
        for asset in assets:
            print(f"=== {asset['assetId']} — {asset['title']} -> {asset['fileName']} ({aspect_ratio_for(asset)}) ===")
            print(build_final_prompt(preamble, asset))
            print()
        print(f"{len(assets)} prompt(s) shown, 0 API calls made.")
        return

    try:
        from dotenv import load_dotenv

        load_dotenv(ROOT / ".env")
    except ImportError:
        pass

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set (checked .env and environment). Aborting.", file=sys.stderr)
        sys.exit(1)

    from google import genai

    client = genai.Client(api_key=api_key)

    for asset in assets:
        generate_one(client, asset, preamble, args.force)


if __name__ == "__main__":
    main()
