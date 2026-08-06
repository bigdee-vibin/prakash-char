#!/usr/bin/env python3
"""Package the offline release artifact (Milestone 5).

Copies index.html + assets/ (images, audio -- not concept_art, which is
pre-Asset-Register exploratory material, not a shipped asset) into release/,
verifies there are zero http(s):// references and every asset path referenced
in index.html resolves to a real file, then zips release/ into a versioned
archive at the repo root.

Usage:
  python3 scripts/package_release.py [version]   # default version: v1.0
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = ROOT / "release"
INDEX = ROOT / "index.html"


def clean_release_dir():
    if RELEASE_DIR.exists():
        shutil.rmtree(RELEASE_DIR)
    RELEASE_DIR.mkdir(parents=True)


def copy_artifact():
    shutil.copy2(INDEX, RELEASE_DIR / "index.html")
    dest_assets = RELEASE_DIR / "assets"
    dest_assets.mkdir()
    shutil.copytree(ROOT / "assets" / "images", dest_assets / "images")
    shutil.copytree(ROOT / "assets" / "audio", dest_assets / "audio")


def verify():
    html = (RELEASE_DIR / "index.html").read_text(encoding="utf-8")

    http_refs = re.findall(r"https?://[^\s\"'<>]+", html)
    if http_refs:
        print("FAIL: found http(s):// references in index.html:", file=sys.stderr)
        for ref in http_refs:
            print(f"  {ref}", file=sys.stderr)
        sys.exit(1)

    asset_refs = re.findall(r"assets/(?:images|audio)/[A-Za-z0-9_.\-]+", html)
    missing = []
    for ref in sorted(set(asset_refs)):
        if not (RELEASE_DIR / ref).exists():
            missing.append(ref)
    if missing:
        print("FAIL: index.html references assets that don't exist in release/:", file=sys.stderr)
        for m in missing:
            print(f"  {m}", file=sys.stderr)
        sys.exit(1)

    print(f"OK: 0 http(s):// references, {len(set(asset_refs))} asset references all resolve.")


def zip_release(version: str) -> Path:
    out_path = ROOT / f"Prakasha-chara_{version}.zip"
    if out_path.exists():
        out_path.unlink()
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in RELEASE_DIR.rglob("*"):
            if path.is_file():
                zf.write(path, path.relative_to(RELEASE_DIR.parent))
    return out_path


def main():
    version = sys.argv[1] if len(sys.argv) > 1 else "v1.0"
    clean_release_dir()
    copy_artifact()
    verify()
    out_path = zip_release(version)
    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"Packaged: {out_path.relative_to(ROOT)} ({size_mb:.1f} MB)")
    if size_mb > 150:
        print("WARNING: exceeds the 150MB size budget (DECISIONS.md #017).", file=sys.stderr)


if __name__ == "__main__":
    main()
