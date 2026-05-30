#!/usr/bin/env python3
"""Generate uniform cover cards for the natural-science journal packs.

Creates SVG source files and PNG renderings for both the homepage wall
(`assets/covers/<slug>.png`) and each pack-local cover (`<Pack>/assets/cover.png`).
Uses `rsvg-convert` when available, with macOS `sips` as a fallback.
"""
import os
import shutil
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "covers")
NAVY = "#1f3a5f"

# slug, discipline banner, big name, big font-size, english subtitle, skills, pack dir
JOURNALS = [
    ("science", "MULTIDISCIPLINARY", "Science",     40, "AAAS",                       12, "Science-Skills"),
    ("cell",    "LIFE SCIENCES",     "Cell",        46, "Cell Press",                 12, "Cell-Skills"),
    ("pnas",    "MULTIDISCIPLINARY", "PNAS",        46, "Nat'l Academy of Sciences",  12, "PNAS-Skills"),
    ("nejm",    "CLINICAL MEDICINE", "NEJM",        44, "New England J. of Medicine", 12, "NEJM-Skills"),
    ("lancet",  "CLINICAL MEDICINE", "The Lancet",  30, "Founded 1823",               12, "Lancet-Skills"),
]

SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 320" width="240" height="320">
<rect width="240" height="320" fill="#ffffff"/>
<rect x="5" y="5" width="230" height="310" rx="13" fill="#ffffff" stroke="{navy}" stroke-width="2"/>
<path d="M5,18 a13,13 0 0 1 13,-13 h204 a13,13 0 0 1 13,13 v60 h-230 z" fill="{navy}"/>
<text x="120" y="35" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="10.5" letter-spacing="2.5" font-weight="700" fill="#ffffff">{banner}</text>
<rect x="74" y="45" width="92" height="2" rx="1" fill="#ffffff" opacity="0.7"/>
<text x="120" y="63" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="8.5" letter-spacing="1.5" fill="#ffffff" opacity="0.8">JOURNAL · AGENT SKILLS</text>
<text x="120" y="167" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="{bigsize}" font-weight="700" fill="#1a1a1a">{bigname}</text>
<text x="120" y="238" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="11" fill="#6a6a6a">{subtitle}</text>
<line x1="42" y1="276" x2="198" y2="276" stroke="{navy}" stroke-width="1" opacity="0.3"/>
<rect x="78" y="285" width="84" height="22" rx="11" fill="{navy}"/>
<text x="120" y="300" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="11" font-weight="700" fill="#ffffff">{skills} skills</text>
</svg>
'''

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_png(svg_path, png_path):
    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-w", "480", "-h", "640", "-o", png_path, svg_path],
            check=True,
        )
        return
    if shutil.which("sips"):
        subprocess.run(
            ["sips", "-s", "format", "png", "-z", "640", "480", svg_path, "--out", png_path],
            check=True,
            stdout=subprocess.DEVNULL,
        )
        return
    raise SystemExit("Install rsvg-convert (librsvg) or run this script on macOS with sips.")


for slug, banner, bigname, bigsize, subtitle, skills, packdir in JOURNALS:
    svg = SVG.format(navy=NAVY, banner=esc(banner), bigsize=bigsize,
                     bigname=esc(bigname), subtitle=esc(subtitle), skills=skills)
    svg_path = os.path.join(COVERS, f"{slug}.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    # homepage wall PNG (render at 2x for crispness: 480x640)
    wall_png = os.path.join(COVERS, f"{slug}.png")
    render_png(svg_path, wall_png)
    # pack-local cover.png
    pack_assets = os.path.join(ROOT, packdir, "assets")
    os.makedirs(pack_assets, exist_ok=True)
    render_png(svg_path, os.path.join(pack_assets, "cover.png"))
    print(f"{slug}: svg + wall png + {packdir}/assets/cover.png")

print("done")
